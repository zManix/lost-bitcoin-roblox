# BLENDER → ROBLOX PIPELINE (generic; copy into each kit and fill §H)

Source: a research pass on 2026-10-26 (Roblox docs repo as of 2026-10-24, the Open Cloud specs, blender-mcp README,
staff posts). Nothing here has been run end to end yet, so do the
SCALE/ORIENTATION TEST (step A3) on your very first export.

## A. Setup
A1. **Blender MCP** (now "mcp-for-blender"; the old "blender-mcp" name still works).
- Tools: execute_blender_code, look, get_scene_info, generate_3d, search_assets, import_asset (older builds:
  get_object_info and per-service Poly Haven/Rodin/Sketchfab tools).
- It listens on localhost:9876. Use `look` to screenshot your Blender viewport and check every model visually.
A2. **Scene units for Roblox:** Unit System = None, Unit Scale = 1.0, Rotation = Degrees. Then **1 Blender unit = 1
stud** (a block is 4 units; a character is about 5 units tall).
- Do NOT also apply the "unit scale 0.01" trick: with System None, the FBX exporter ignores Unit Scale.
- import_asset(target_size) takes meters; convert first (1 stud ≈ 0.28 m).
A3. **Scale/orientation test (first thing):** export a 4×1×2 box with its front facing −Y, import it, check that
MeshPart.Size reads (4,1,2) and that the front matches LookVector. Fix the settings until it does, and log the result
in PROGRESS.md.
A4. **FBX export** (via execute_blender_code `bpy.ops.export_scene.fbx`):
- use_selection=True, apply_scale_options='FBX_SCALE_UNITS', axis_forward='Z', axis_up='Y'
- use_mesh_modifiers=True, use_triangles=True, mesh_smooth_type='FACE'
- add_leaf_bones=False, bake_anim=False, path_mode='COPY', embed_textures=True
- The importer keeps each object's own origin as its pivot: put origins where pivots should be (fists at the
  wrist, props at the base center).

## B. Mesh rules
- ≤ 20,000 triangles per mesh (hard limit). Our budgets are lower: see the asset list.
- ONE material and ONE UV set (0–1) per mesh. ≤ 4 bone influences per vertex (we use none).
- Clean topology, no n-gons after triangulate, applied scale/rotation, normals outward, merged by distance.
- CollisionFidelity: Box for props (or CanCollide false); RenderFidelity Automatic.
- MeshId cannot be set by scripts. Upload each mesh ONCE, create a template MeshPart, and CLONE it everywhere (same
  mesh + same texture = instanced/batched draw).

## C. Stylized ink/toon look (use when the style calls for outlines/cel shading)
- **Outline:** an INVERTED HULL inside the same mesh. Duplicate the shell, push it out 0.03–0.06 studs along normals,
  flip its normals, and UV it onto a black texel in the same texture. Roblox meshes are single-sided by default, so
  this costs no extra draw call. Use it on hero items: viewmodel, key props, creatures. Not on terrain/blocks (use baked seams in textures).
- **Shading:** bake 2–3 flat cel tones + thin ink lines + light cross-hatching into the color texture (Blender: paint
  or bake from a toon shader). Render the meshes with Material SmoothPlastic + TextureID (or SurfaceAppearance
  ColorMap only, no normal map needed).
- **Lighting (Roblox):** `Lighting.Technology` is deprecated. Use `LightingStyle = Soft`, raise Ambient, set
  EnvironmentDiffuseScale 0–0.3 and EnvironmentSpecularScale 0. Then a mild ColorCorrection per band and a low Bloom.
- Keep Highlights OFF the fists and props (the first Highlight on screen costs up to about 1 ms GPU on mobile). Use
  Highlights only for ghosts.

## D. Textures (Gemini image model → pending_review\ → auto-check → upload)
- Size: 512² for props/fists/buddies (1024² max for hero items); 1024² for the 5 band block tiles. Normal maps (if
  any) must be OpenGL tangent space.
- Upload each texture as assetType "Image" via Open Cloud and assign it with MeshPart.TextureID (runtime-settable) or
  as SurfaceAppearance.ColorMap (edit-time only, set via execute_luau in Studio).
- The safest path is to upload textures separately and assign them in Studio. Don't rely on textures embedded in an
  Open Cloud FBX upload.
- **Block textures:** 5 band MaterialVariants (base material SmoothPlastic or Slate), StudsPerTile 16, using a
  1024² image that contains a 4×4 grid of blocks with thin cream seams, faint marble veins and ±6% per-block
  brightness variation. Assign them to the cube parts by band. Prefer a MaterialVariant over Texture instances
  (Texture instances don't batch). If tiling doesn't line up across merged boxes [TEST], fall back to Texture
  instances on air-facing faces only, with OffsetStudsU/V from the world position.
- Prompt style (positive-only), e.g.:
  - "seamless tileable square texture, a 4 by 4 grid of smooth matte sandstone blocks, thin cream seam lines between
    blocks, faint dark marble veins, subtle variation in brightness per block, warm brown tones, flat lighting,
    stylized hand-painted game texture"
  - "cartoon glove texture atlas, cream canvas glove with bold dark ink outlines and light cross-hatch shading, comic
    book style, flat colors"

## E. Upload (Open Cloud) and getting mesh IDs
- POST https://apis.roblox.com/assets/v1/assets (header x-api-key = ROBLOX_API_KEY).
  - multipart with part `request` = {"assetType":"Model","displayName":…,"description":…,"creationContext":
    {"creator":{"userId":ROBLOX_USER_ID}}}
  - and part `fileContent` = the .fbx (content-type model/fbx)
  - Images: assetType "Image" (png).
- Poll GET /assets/v1/operations/{id} until done, then read response.assetId and moderationResult (Reviewing /
  Approved / Rejected).
- Limits: 1 asset and 20 MB per call; images < 8000×8000. On HTTP 429 wait for x-ratelimit-reset.
- An uploaded Model comes back as a MODEL asset id, not a mesh id. Get the meshes via Studio MCP execute_luau:
  `game:GetService("InsertService"):LoadAsset(id)`. Find the MeshParts, keep them as TEMPLATES in
  ServerStorage/Assets, and record their MeshIds in Config.Assets. (Alternative: the Studio MCP insert_asset tool.)
- Assets must be owned by the same user/group as the experience (ROBLOX_USER_ID).
- Write tools\upload_asset.py (or .js) once; log every upload in ASSET_LOG.md (file, asset id, mesh id, moderation
  state).

## F. First-person viewmodels (hands, tools, weapons-as-tools)
- Two rigid glove meshes (L/R) + short sleeve meshes. Parent them to an anchored, non-colliding root part via Motor6D
  or weld offsets (NOT a skinned rig).
  - All parts: CanCollide/CanTouch/CanQuery false, CastShadow false, LocalTransparencyModifier 0.
- Attach on the client with RunService:BindToRenderStep("Viewmodel", Enum.RenderPriority.Camera.Value + 1, …),
  using root:PivotTo(camera.CFrame * offset). Keep the geometry ≥ 0.5 studs from the camera (near plane). Pull the
  fists back when a short forward ray hits a wall (anti-clipping).
- Animate PROCEDURALLY with springs:
  - jab = extend along the look vector + rotate the wrist, overshoot, return; alternate hands
  - idle = slow breathing bob; walk = small sway; spell cast = both fists push forward + glow
- Viewmodel total ≤ 5k triangles.

## G. Performance targets (cheap phones)
- About 60% of Android players have 2–4 GB RAM. Targets: ≤ 300–500 draw calls, ≤ 300k–500k visible triangles,
  ≤ 3,000 block parts, viewmodel ≤ 5k tris, total texture memory small (reuse the atlases).

## H. ASSET LIST (per game: the skill fills this in)
Write a table: # | Asset | Count | Tris each | Notes. Budgets:
- viewmodel/hands ≤ 1,200 each (total ≤ 5k)
- hero props ≤ 3,000
- small props ≤ 800
- creatures/pets ≤ 1,500–2,000
- repeated decor ≤ 120 (instanced)
- 2D: area textures (1024²), prop atlases (512²), UI icons (flat, no text), the game icon + 3 thumbnails (scenes, no
  lettering)

Cover every model the SPEC mentions; nothing may stay greybox in the main loop.

## I. "Asset DONE when…"
1. The scale/orientation test passed once (A3).
2. Triangles are within budget; one material; UVs 0–1.
3. Origin/pivot is correct.
4. The ink hull is visible at gameplay distance.
5. The texture is uploaded and approved.
6. The mesh is uploaded, approved, and stored as a template.
7. It's cloned (not re-uploaded) everywhere.
8. CollisionFidelity/RenderFidelity are set.
9. It's checked with Blender `look` AND a Studio screen_capture in game lighting.
10. VISUAL_QA ≥ 8 for its scene.
11. It's logged in ASSET_LOG.md.
12. No banned content.
13. It looks good on the Low quality preset on an emulated phone.
