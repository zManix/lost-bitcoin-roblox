# Blender → Roblox asset pipeline (Blender MCP + Open Cloud), verified 2026-10-26

Audience: a Claude Code agent on Windows driving Blender through the Blender MCP server and uploading to Roblox through Open Cloud. Goal: meshes that import at the right scale and orientation, look good with an ink-outline/comic style, and run on cheap Android phones.

## How this was verified

- **[OFFICIAL]**: read in Roblox's own docs. The source is the `Roblox/creator-docs` GitHub repo (which create.roblox.com is built from), last commit **2026-10-24**, or the Open Cloud OpenAPI specs in that repo. Each claim carries its create.roblox.com URL.
- **[SOURCE]**: read in tool source code, for example Blender's FBX exporter or the blender-mcp repo at its **2026-10-24** HEAD.
- **[STAFF]**: from a Roblox staff DevForum post.
- **[COMMUNITY]**: from DevForum or third-party tools. Not official.
- **[REC]**: my recommendation or inference. Not an official number. Test it.
- **[UNVERIFIED]**: plausible, but I found no confirmation. Test it before relying on it.

---

## 0. Toolchain facts (read first)

### Blender MCP (github.com/ahujasid/blender-mcp) [SOURCE]

- **The project was renamed.** The PyPI package `blender-mcp` is now **`mcp-for-blender`**. `uvx blender-mcp` still works, but new installs should use `uvx mcp-for-blender`. Source: https://github.com/ahujasid/blender-mcp (README "Quickstart").
- **Windows setup.**
  - Install uv with `winget install --id=astral-sh.uv -e`, then run `uvx mcp-for-blender setup`. This configures the clients and installs the addon.
  - To install only the addon, run `uvx mcp-for-blender install-addon`. Then enable "Interface: MCP for Blender" in Blender, press N in the viewport, open the MCP for Blender tab and click Start MCP Server.
  - For Claude Code, run `claude mcp add blender uvx mcp-for-blender`.
  - If uvx can't be found, use `"command": "cmd", "args": ["/c","uvx","mcp-for-blender"]`, or the full path to `uvx.exe` (`where uvx`).
- **Connection settings.** The socket listens on `localhost:9876` by default (`BLENDER_HOST`, `BLENDER_PORT`). It has no authentication, so keep it on localhost. Run only one MCP client against it at a time.
  - `BLENDER_MCP_SAFE_MODE=1` blocks file, network and process access from scripts.
  - `DISABLE_TELEMETRY=true` turns telemetry off.
- **Current tool list: 9 tools (HEAD 2026-10-24).**
  - `execute_blender_code`
  - `look`: viewport, camera, multi-angle `angles` sheet or `frames`, in solid, material, rendered, wireframe or xray shading.
  - `get_scene_info`: fields, `root`, `query`.
  - `generate_3d`: Tripo, Hunyuan3D, Hyper3D Rodin or Meshy.
  - `search_assets` and `import_asset`: Poly Haven, Sketchfab and Poly Pizza.
  - `get_addon_status`
  - `disable_telemetry`
  - `record_trajectory_feedback`
  - Note: `get_object_info` no longer exists. Use `get_scene_info(root="Name")` or `execute_blender_code`.
- **Legacy tool names (Dec 2025 build).** An older install or fork exposes these instead: `get_scene_info`, `get_object_info`, `get_viewport_screenshot`, `execute_blender_code`, `get_polyhaven_categories`, `search_polyhaven_assets`, `download_polyhaven_asset`, `set_texture`, `get_polyhaven_status`, `get_hyper3d_status`, `get_sketchfab_status`, `search_sketchfab_models`, `download_sketchfab_model`, `generate_hyper3d_model_via_text`, `generate_hyper3d_model_via_images`, `poll_rodin_job_status`, `import_generated_asset`, `get_hunyuan3d_status`, `generate_hunyuan3d_model`, `poll_hunyuan_job_status`, `import_generated_asset_hunyuan`. Check which set your MCP lists. [SOURCE: git history of the repo]
- **Scale gotchas.**
  - `import_asset(target_size=…)` is in **metres** and assumes Blender's default units.
  - Section 1 sets 1 Blender unit = 1 stud. Under that setup, `target_size=1.0` makes the object **1 stud** long, which is about 28 cm.
  - Convert real sizes before calling it: studs = metres ÷ 0.28. Or rescale afterwards.
  - `generate_3d` output "arrives at arbitrary scale and facing". AI-generated meshes are usually far over a mobile triangle budget, so decimate and retopologize them (section 6). [SOURCE: server.py docstrings]

### Roblox Studio MCP (built into Studio) [OFFICIAL]

https://create.roblox.com/docs/studio/mcp

- **How to enable it.** In Studio, open "… › Manage MCP Servers" and turn on "Enable Studio as MCP server".
- **Windows command.** `cmd.exe /c %LOCALAPPDATA%\Roblox\mcp.bat`, using stdio transport.
- **Tools that matter for this pipeline.**
  - `execute_luau`: takes `datamodel_type` Edit, Client or Server.
  - `insert_asset`: inserts by numeric asset ID. It handles models, meshes, images, animations and packages.
  - `upload_image`: uploads from **HTTP URLs**, not local files.
  - `store_image`
  - `search_game_tree`
  - `inspect_instance`
  - `screen_capture`
  - `start_stop_play`
  - `get_console_output`
  - `generate_mesh` and `generate_material`
- This MCP is the easiest way to turn an uploaded Model asset ID into MeshIds and textures (section 3.5).

---

## 1. Blender scene setup and FBX export

### 1.1 Units and scale

- **1 stud = 28 cm.** [OFFICIAL] Source: https://create.roblox.com/docs/physics/units
  - In practice, compare against an avatar instead. A default avatar is about 5 to 6 studs tall, and doors are usually 7 to 8 studs. [REC]
- **Official Blender file setup.** Scene Properties › Units › **Unit System = None**, **Rotation = Degrees**. The docs say this keeps measurements "consistent with studs", so 1 Blender unit = 1 stud. [OFFICIAL] Source: https://create.roblox.com/docs/art/blender#configure-units
- **Official FBX scale fix:** set **Transform › Apply Scalings = "FBX Unit Scale"** on export. Keep every other scale at the default 1.0, both the export Scale and the scene Unit Scale. The docs call this "the recommended way to export `.fbx` files at the same scale". [OFFICIAL] Source: https://create.roblox.com/docs/art/blender#adjust-scale-fbx
- **Alternatives the same page lists.**
  - Export Scale = 0.01.
  - Scene Unit Scale = 0.01. The docs warn this causes camera and modifier issues in Blender.
- **Exporter detail:** when Unit System = None, the exporter ignores Unit Scale. Its unit factor is hard-coded to `100.0 if unit_settings.system == 'NONE' else 100.0 * scale_length`. So the "Unit Scale 0.01" alternative only works under the Metric system. Don't combine Unit System None with Unit Scale 0.01. [SOURCE: Blender `io_scene_fbx/fbx_utils.py` `units_blender_to_fbx_factor`]
- **Blender's default (`FBX_SCALE_NONE`, "All Local") is why models import huge.** It bakes the ×100 (m → cm) conversion into the object transforms. [SOURCE: `io_scene_fbx/__init__.py`]
- **Studio side.** File Geometry › **Scale Unit = Studs** is the default. [OFFICIAL] Source: https://create.roblox.com/docs/studio/importer
- **glTF is an alternative.** Studio also takes `.gltf` and `.glb`, which "do not require these additional scaling configurations". [OFFICIAL] The trade-off is a different hierarchy: each glTF mesh arrives as a nested `Model` holding one `MeshPart` per primitive. [OFFICIAL, importer page]
- **Do a scale test on the first export of every project.** [REC]
  1. Export a 4×1×2 box. That is the default Roblox Part size.
  2. Import or upload it.
  3. Confirm that `MeshPart.Size` reads exactly `4, 1, 2`.

### 1.2 Axes

- **Official Blender → Studio export axes:** **Forward = "Z Forward"**, **Up = "Y Up"**, with Include › **Limit to Selected Objects** on. [OFFICIAL] Source: https://create.roblox.com/docs/art/blender#export-settings
  - Blender's default is `-Z` Forward. The Roblox docs say `Z`.
  - Studio's importer defaults are World Forward = Front and World Up = Top. Keep them.
  - Model the asset's front facing **-Y** in Blender, which is what Blender's Front view (numpad 1) shows. With `axis_forward='Z'`, that face becomes Roblox's front (-Z, the `LookVector`).
- **Confirm orientation once per project.** The docs and the axis math agree, but the importer may also read the FBX `FrontAxis` and `UpAxis` header. [REC/UNVERIFIED]
  1. Export an arrow or wedge pointing toward -Y in Blender.
  2. In Studio, check that it points along the part's `CFrame.LookVector`.
  3. If it's flipped, try `axis_forward='-Z'`.

### 1.3 Full export call (bpy, through `execute_blender_code`)

```python
import bpy
sc = bpy.context.scene
sc.unit_settings.system = 'NONE'          # official: Unit System None
sc.unit_settings.system_rotation = 'DEGREES'
sc.unit_settings.scale_length = 1.0       # keep default (ignored under NONE anyway)

# select only what you export, apply transforms first (see 1.4)
bpy.ops.export_scene.fbx(
    filepath=r"C:\work\roblox\export\Crate.fbx",
    use_selection=True,                 # "Limit to Selected Objects" [OFFICIAL]
    object_types={'MESH'},              # add 'ARMATURE' (and 'EMPTY') for rigs [REC]
    global_scale=1.0,
    apply_unit_scale=True,
    apply_scale_options='FBX_SCALE_UNITS',  # "FBX Unit Scale" [OFFICIAL]
    axis_forward='Z', axis_up='Y',          # [OFFICIAL]
    use_space_transform=True, bake_space_transform=False,
    use_mesh_modifiers=True,            # apply modifiers (Blender default) [REC]
    mesh_smooth_type='FACE',            # [REC] write smoothing; custom normals still exported
    use_triangles=True,                 # [REC] deterministic triangulation = what you counted
    use_tspace=False,
    colors_type='SRGB',                 # vertex colors are imported by Studio [OFFICIAL importer page]
    add_leaf_bones=False,               # [OFFICIAL] "disable Add Leaf Bones"
    bake_anim=False,                    # [OFFICIAL] unless exporting animation
    path_mode='COPY', embed_textures=True,  # [OFFICIAL] Path Mode Copy + Embed Textures
)
```

The parameter names were checked against Blender's `io_scene_fbx/__init__.py` (main branch). [SOURCE]

- **Apply Modifiers:** the exporter applies modifiers to mesh objects, except Armature modifiers, and the tooltip warns this "prevents exporting shape keys". [SOURCE]
- **Mesh only:** use `object_types={'MESH'}` for static props. Add `ARMATURE` for skinned or rigged assets.
- **Triangulate:** Roblox's spec says "Meshes must be in quads where possible". That is an authoring and topology rule. [OFFICIAL] Studio stores triangles either way, so triangulating at export only fixes the split. [REC]

### 1.4 Pivot and origin, transforms, normals

- **Importer defaults** [OFFICIAL] (https://create.roblox.com/docs/studio/importer):
  - "Set Pivot to Scene Origin" is **on**. The whole model's pivot goes to the Blender world origin.
  - Per object, "Use Imported Pivot" is **on**. Each MeshPart keeps its Blender object origin as its pivot.
  - "Insert Using Scene Position" is **off**.
  - "Anchored" is **off**. Anchor props after import.
- **Before every export, in Blender:** [REC]
  1. Apply rotation and scale (Ctrl+A › Rotation & Scale). Never export negative scale.
  2. Set the object origin where the Roblox pivot should be:
     - bottom-center for props;
     - the wrist or forearm root for viewmodel arms;
     - the hinge for doors.
  3. Put each asset at the world origin when you export it alone.
- **Rig bones:** all bones need scale 1,1,1 and rotation 0,0,0, frozen. The root sits at 0,0,0 with no skin influences. A vertex can have at most **4 bone influences**. [OFFICIAL] Source: https://create.roblox.com/docs/art/modeling/specifications
- **Normals.**
  - Recalculate outside (Shift+N).
  - Shade with Smooth by Angle, or Auto Smooth, for hard edges.
  - Studio's importer has **"Invert Negative Faces"** (off by default) and **"Make Double Sided"** (off by default; "more performance intensive"). Leave both off. [OFFICIAL]
  - Roblox culls back faces unless `MeshPart.DoubleSided` is true. The inverted-hull outline relies on this (section 4.4).
- **Watertight, with volume.** "All geometry must be watertight without exposed holes or backfaces" and "Meshes cannot be 0 thickness". [OFFICIAL, specifications]

### 1.5 Limits

| Item | Limit | Status |
|---|---|---|
| Triangles per mesh (MeshPart) | **20,000** ("Individual meshes can not exceed 20,000 triangles") | [OFFICIAL] specifications; repeated in https://create.roblox.com/docs/parts/models |
| Triangles per import or file | No documented total. Each MeshPart counts separately. | [UNVERIFIED] |
| Vertices per imported mesh | Not documented. EditableMesh, the runtime mesh API, is capped at 60,000 vertices and 20,000 triangles. | [OFFICIAL for EditableMesh only] |
| Bone influences per vertex | 4 | [OFFICIAL] |
| Materials per mesh object | **1** ("Mesh objects can only have one material assigned") | [OFFICIAL] https://create.roblox.com/docs/art/modeling/texture-specifications |
| UV sets | 1, inside 0–1. Overlaps are allowed. | [OFFICIAL] texture-specifications |
| Animation per FBX | 1 track per file | [OFFICIAL] specifications |
| Open Cloud upload size | 20 MB per call | [OFFICIAL] https://create.roblox.com/docs/cloud/guides/usage-assets |

**Multiple meshes per file.**

- FBX and glTF can hold several mesh objects plus their hierarchy. [OFFICIAL]
- "Import Only As Model" is on by default and gives one `Model` containing N `MeshPart`s. "Merge Meshes" (off by default) collapses them into one MeshPart.
- The Importer does **not** de-duplicate meshes. Import or upload each reusable mesh once and duplicate it inside Studio, otherwise instancing breaks (section 6). [OFFICIAL] https://create.roblox.com/docs/performance-optimization/improve

**Naming.**

- Blender object names become the MeshPart names.
- Avoid these reserved suffixes unless you mean them: `_Att` becomes an Attachment, `_OuterCage` becomes a WrapTarget, and an `_InnerCage`/`_OuterCage` pair becomes a WrapLayer. [OFFICIAL] https://create.roblox.com/docs/parts/meshes
- In glTF, a node and a mesh with the same name get a `_Node` suffix. [OFFICIAL]
- Open Cloud `displayName`: keep it ≤ 50 characters. [COMMUNITY: asphalt trims to 50]

### 1.6 Collision and render fidelity

**`CollisionFidelity`** [OFFICIAL] (https://create.roblox.com/docs/parts/meshes):

| Option | What it gives |
|---|---|
| `Box` | Bounding box. Cheapest. |
| `Hull` | Convex hull. |
| `Default` | Approximate shape that supports concavity. |
| `PreciseConvexDecomposition` | Most precise and most expensive. |
| `Tunable` | Shows a `CollisionPrecision` slider. |

[REC] for collision:

- Decoration and viewmodels: `CanCollide=false`, `CanQuery=false`, `CanTouch=false`, `CollisionFidelity=Box`.
- Walkable meshes: `Hull` or `Default`.
- Complex walkable geometry: invisible primitive Parts for collision, with the mesh set to `CanCollide=false`.
- Avoid `PreciseConvexDecomposition`.

**`RenderFidelity`** [OFFICIAL]:

| Value | Behavior |
|---|---|
| `Automatic` (default) | Highest under 250 studs, Medium at 250–500, Lowest past 500 |
| `Precise` | Always full detail. The perf page calls many Precise meshes a "common problem". |
| `Performance` | "Push performance as much as possible…" |

[REC] for render fidelity:

- Small, numerous props: `Performance`.
- Hero props: `Automatic`.
- Never `Precise` on scenery.

**Setting fidelity from scripts.** `MeshId` and `MeshContent` are **not writable by scripts or plugins** (write = `NotAccessibleSecurity`). Use these instead: [OFFICIAL] MeshPart API reference

- `AssetService:CreateMeshPartAsync(Content.fromUri("rbxassetid://ID"), {CollisionFidelity=…, RenderFidelity=…})`
- `MeshPart:ApplyMesh(src)`

### 1.7 How the Importer and Open Cloud treat FBX

- **Importer output:** FBX → `Model` → `MeshPart`(s). Cages become WrapLayer. Rigs become `Bone` instances. [OFFICIAL]
- **Textures:** if the Blender material is a Principled BSDF with Image Texture nodes, the Importer brings textures in as PBR (SurfaceAppearance) or a basic texture. Wire it like this: [OFFICIAL] https://create.roblox.com/docs/art/modeling/assign-textures
  - Base Color ← color map
  - Metallic ← metalness
  - Roughness ← roughness
  - Normal ← Normal Map node ← image
- **Open Cloud `assetType:"Model"` with FBX or glTF** "Imports custom 3D models as a `Model` container containing one or more `MeshPart` objects" and "Will be uploaded as packages". [OFFICIAL]
- **Open Cloud and embedded FBX textures.** I found no official statement that an Open Cloud FBX upload applies the embedded textures the way the Studio Importer does. [UNVERIFIED]
  - Staff on the DevForum point to the Importer when you need import settings. [STAFF]
  - **Robust path:** upload textures separately as Image assets and assign them in Studio (section 2).

---

## 2. Texturing

### 2.1 SurfaceAppearance vs TextureID

**`MeshPart.TextureID`** (Content: `TextureContent`)

- One color texture.
- Writable from any script, including at runtime (write security `None`). [OFFICIAL API ref]
- It is ignored when a SurfaceAppearance exists: "setting a Texture ID can't override the PBR textures". [OFFICIAL] parts/meshes

**`SurfaceAppearance`** (child of the MeshPart)

- Maps: `ColorMap`, `NormalMap`, `RoughnessMap`, `MetalnessMap`, plus `EmissiveMaskContent` with `EmissiveStrength` and `EmissiveTint`. [OFFICIAL] https://create.roblox.com/docs/art/modeling/surface-appearance
- **The map properties are PluginSecurity for writes.** They can be set in Studio in edit mode (Properties window, plugins, and most likely Studio MCP `execute_luau` in Edit). Game scripts **cannot** set them at runtime: "you can't modify `SurfaceAppearance` properties by scripts during a game".
- `Color` (tint), `AlphaMode` and the emissive strength and tint **are** runtime-writable. [OFFICIAL API ref]
- At runtime, `AssetService:CreateSurfaceAppearanceAsync` builds one from EditableImages. [OFFICIAL]

**`MaterialVariant`** (in MaterialService)

- PBR maps plus physical properties.
- **`StudsPerTile`** makes it tile on Parts. [OFFICIAL]
- The best fit for repeating block or terrain textures (2.4).

**Recommendation for a stylized or comic look on mobile:** one hand-painted or baked color texture through `TextureID`, with `Material = SmoothPlastic`. [REC]

- That is one texture in memory instead of up to four.
- Add a SurfaceAppearance only when you need a normal map, an alpha mode or an emissive mask.

### 2.2 Map formats, sizes, alpha

**Formats** [OFFICIAL] texture-specifications:

| Map | Format |
|---|---|
| Albedo/color | RGB (24-bit), or RGBA for alpha |
| Normal | RGB, **OpenGL, tangent space only**. Blender bakes OpenGL by default. Flat normal is `[127,127,255]`. |
| Roughness, Metalness, Emissive mask | 8-bit grayscale |
| Upload file types | `.png`, `.jpg`, `.tga`, `.bmp` |

**Resolution.** The docs contradict each other:

- "Roblox supports up to 4096×4096".
- The UV section says "up to 1024×1024 pixel spaces".
- The PBR budget table lists 1024×1024 as "(maximum)".

Treat **1024 as the practical maximum**. [OFFICIAL + REC]

**Official sizing guidance:**

| Object size | Texture |
|---|---|
| 5×5 stud object | 256² |
| 10×10 stud object | 512² |
| 20×20 stud object | 1024² |

- PBR budget: 256² per 2×2×2-unit volume.
- Parts use 1024² per 8×8 stud face.
- Graphics memory scales with pixel count: 1024² costs 4× a 512². Images are transcoded to a fixed format, so compressing or dropping alpha before upload does **not** save GPU memory. [OFFICIAL] performance-optimization/improve
- "Unless an image is occupying a large amount of physical space on the screen, it usually needs at most 512x512 pixels. Most minor images should be smaller than 256x256." [OFFICIAL]
- Texture streaming is automatic. It loads baseline quality first and raises quality per device memory. Keep texel density near uniform. [OFFICIAL] parts/textures-decals

**`AlphaMode`** [OFFICIAL]:

| Mode | Behavior |
|---|---|
| `Overlay` (default) | Transparent areas reveal `MeshPart.Color` |
| `Transparency` | Cutout or blend. For hard-edged cutouts keep `MeshPart.Transparency = 0`. For soft blending set it to ≥ 0.02. |
| `TintMask` | Alpha controls where `SurfaceAppearance.Color` tints |
| `Opaque` | Ignores alpha. Beta: "MaterialVariant Alpha Mode". |

Color tint (`SurfaceAppearance.Color`) multiplies the ColorMap and is free. Reusing one grayscale map with tints saves memory.

### 2.3 Upload images through Open Cloud and get the ID for TextureID

- `POST https://apis.roblox.com/assets/v1/assets`, multipart, with `assetType` **`"Image"`** (or `"Decal"`).
  - Content types: `image/png`, `image/jpeg`, `image/bmp`, `image/tga`.
  - Images must be smaller than 8000×8000.
  - Images can't be updated. Upload a new asset instead.
  - [OFFICIAL] https://create.roblox.com/docs/cloud/guides/usage-assets
- **Use `"Image"`.**
  - The returned `assetId` is then the image itself, and you use it directly: `meshPart.TextureID = "rbxassetid://<assetId>"`, or `Content.fromAssetId(id)` for Content properties.
  - The docs list "Decal, Image" together.
  - The community tool asphalt (active Rust uploader, 2026-07) uploads all images with `assetType "Image"`.
  - [OFFICIAL + COMMUNITY]
- **Decal caveat.** A `"Decal"` upload gives a Decal asset ID, which historically differs from the underlying Image ID. A Decal ID in `TextureID` may fail with "Asset type does not match requested type". If you're stuck with a Decal ID, insert it in Studio and read `Decal.ColorMapContent`/`Texture` to get the image ID. [COMMUNITY/UNVERIFIED]
- **Asset Privacy.** It can make new Images, Decals and Meshes "Restricted". Your own games can always use your own assets. [OFFICIAL] https://create.roblox.com/docs/projects/assets/privacy
  - **Create assets with the same owner as the experience** (`userId` vs `groupId`), or the game can't load them.
- **Studio MCP's `upload_image`** takes HTTP URLs only. Local PNGs exported from Blender go through Open Cloud. [OFFICIAL]

### 2.4 Repeating block textures on Parts

**`Texture` instance** [OFFICIAL] https://create.roblox.com/docs/parts/textures-decals

- One per face (`Face` = Top, Bottom, Front, Back, Left, Right).
- **Tiles in world studs:** `StudsPerTileU` and `StudsPerTileV` set the tile size, and `OffsetStudsU` and `OffsetStudsV` shift it. Resizing the part only changes how many repeats you see.
- Image property: `ColorMapContent`, the newer Content API. `Texture` is still accepted.
- **Drawback:** "decals, textures, and particles don't batch well and introduce additional draw calls". That is 6 extra objects per fully textured block. [OFFICIAL] performance-optimization/improve

**`MaterialVariant`, preferred for many blocks** [REC based on OFFICIAL]

1. Create it under `MaterialService` with `BaseMaterial` (for example Plastic), a `ColorMap` (and optionally normal and roughness maps) and **`StudsPerTile`** (for example 4).
2. Set `Part.Material = BaseMaterial` and `Part.MaterialVariant = "Name"`.

- It tiles on every face with no extra instances.
- Parts with identical materials can instance together.
- It is also texture-streamed.
- **Constraint:** its map properties are PluginSecurity, so create it at edit time.
- For a voxel/block game, prefer MaterialVariants over 6 `Texture` instances per block. [REC]

---

## 3. Uploading meshes with the Open Cloud Assets API

### 3.1 API key and scopes [OFFICIAL]

- Create the key at Creator Dashboard › Credentials, with **Access Permissions › Assets API** and **Read + Write**.
  - Group assets require group permissions.
  - OAuth equivalents: `asset:read` and `asset:write`.
- Header: `x-api-key: <key>`.
- IP restriction is optional. Leave it off on a dynamic home IP.
- Never commit the key. Put it in an environment variable such as `ROBLOX_API_KEY`.
- Source: https://create.roblox.com/docs/cloud/auth/api-keys and the usage-assets guide.
- The OpenAPI spec (`reference/cloud/assets/v1.json`) gives `POST /v1/assets` security `asset:read` plus `asset:write`. Status: **BETA**. [OFFICIAL]

### 3.2 Request format [OFFICIAL]

```
POST https://apis.roblox.com/assets/v1/assets
Content-Type: multipart/form-data
  request     = JSON: {"assetType":"Model","displayName":"Crate","description":"...",
                       "creationContext":{"creator":{"userId":"123"}  // or {"groupId":"456"}
                                          ,"expectedPrice":0}}      // optional; 400 if actual fee > expected
  fileContent = @Crate.fbx ; type=model/fbx
```

**Content types for `"Model"`:**

| File | Content type |
|---|---|
| `.fbx` | `model/fbx` |
| `.gltf` | `model/gltf+json` |
| `.glb` | `model/gltf-binary` |
| `.rbxm`, `.rbxmx` | `model/x-rbxm` |

**Other asset types:**

| Asset type | Formats | Notes |
|---|---|---|
| `"Animation"` | `.rbxm` or `.rbxmx`, as `model/x-rbxm` | Files "edited outside of Studio might not upload or function" |
| `"Mesh"` | Roblox mesh data only | Only re-uploads of Asset-Delivery downloads. Not FBX. |
| Audio | | 100 uploads/month ID-verified, 10 otherwise |
| Video | | |

- **Updating content:** `PATCH /v1/assets/{assetId}` with a new file works for **`.fbx` only** and creates a new version. Images, meshes, audio and video can't be updated. [OFFICIAL]
- **Staff announcement (2025-10-23)** added `.rbxm` models, animations and Roblox-format meshes. It also deprecated the legacy `Upload.ashx`, `UploadNewMesh` and `UploadNewAnimation` endpoints. [STAFF] https://devforum.roblox.com/t/open-cloud-upload-support-for-more-asset-types/4022082

### 3.3 Operation polling [OFFICIAL]

1. Create returns an Operation, for example `{"path":"operations/<id>","operationId":"<id>","done":false}`. asphalt reads `operationId`.
2. Poll `GET https://apis.roblox.com/assets/v1/operations/<id>` with the same header until `done:true`.
3. The result is in `response`:
   - `assetId`
   - `assetType` (for example `ASSET_TYPE_MODEL`)
   - `revisionId`
   - `moderationResult.moderationState`
   - …or in `error` (a Status).
4. Back off exponentially (1 s, 2 s, 4 s…). asphalt uses 10 polls with doubling. [COMMUNITY]

**Moderation states.** The spec lists `Reviewing`, `Rejected` and `Approved`. The JSON returns `MODERATION_STATE_APPROVED`, and so on. [OFFICIAL]

- Treat `Rejected` as failure.
- A `Reviewing` asset may render blank or not load until approved. [UNVERIFIED]

**Limits and quotas.**

- One asset per call, ≤ 20 MB. [OFFICIAL]
- An older staff post said 30 MB. Use 20. [COMMUNITY]
- The OpenAPI spec lists no explicit per-minute rate limit for `/assets/v1/assets`. Handle **HTTP 429** and wait for the `x-ratelimit-reset` header (seconds), as asphalt does. [OFFICIAL spec + COMMUNITY]
- Check quotas with `GET https://apis.roblox.com/cloud/v2/users/{userId}/asset-quotas` (scope `asset:read`, 60 requests/min). It returns `RATE_LIMIT_UPLOAD` per `assetType` with `usage`, `capacity` and `expirationTime`. [OFFICIAL openapi.json]

### 3.4 Windows uploader (Python; avoid PowerShell's `curl` alias, or use `curl.exe`)

```python
# upload_asset.py  — usage: python upload_asset.py <file> <Model|Image|Animation> <displayName>
import json, os, sys, time, requests
API = "https://apis.roblox.com/assets/v1"
KEY = os.environ["ROBLOX_API_KEY"]
CREATOR = {"userId": os.environ["ROBLOX_USER_ID"]}          # or {"groupId": "..."} — must own the game
CT = {".fbx":"model/fbx", ".glb":"model/gltf-binary", ".gltf":"model/gltf+json",
      ".rbxm":"model/x-rbxm", ".rbxmx":"model/x-rbxm",
      ".png":"image/png", ".jpg":"image/jpeg", ".jpeg":"image/jpeg", ".bmp":"image/bmp", ".tga":"image/tga"}

def _send(fn):
    for attempt in range(6):
        r = fn()
        if r.status_code == 429:
            time.sleep(float(r.headers.get("x-ratelimit-reset", 2 ** attempt))); continue
        r.raise_for_status(); return r.json()
    raise RuntimeError("rate limited")

def upload(path, asset_type, name):
    req = {"assetType": asset_type, "displayName": name[:50], "description": name,
           "creationContext": {"creator": CREATOR}}
    ext = os.path.splitext(path)[1].lower()
    with open(path, "rb") as f:
        data = f.read()
    op = _send(lambda: requests.post(f"{API}/assets", headers={"x-api-key": KEY},
               files={"request": (None, json.dumps(req), "application/json"),
                      "fileContent": (os.path.basename(path), data, CT[ext])}))
    op_id = op.get("operationId") or op["path"].split("/")[-1]
    delay = 1
    for _ in range(12):
        o = _send(lambda: requests.get(f"{API}/operations/{op_id}", headers={"x-api-key": KEY}))
        if o.get("done"):
            if "error" in o: raise RuntimeError(o["error"])
            resp = o["response"]
            state = resp.get("moderationResult", {}).get("moderationState", "")
            if "REJECTED" in state.upper(): raise RuntimeError(f"moderation rejected: {resp}")
            return resp            # resp["assetId"]
        time.sleep(delay); delay = min(delay * 2, 30)
    raise TimeoutError(op_id)

if __name__ == "__main__":
    print(json.dumps(upload(sys.argv[1], sys.argv[2], sys.argv[3]), indent=2))
```

### 3.5 Getting MeshIds out of an uploaded Model asset

The Model asset ID is a **package**, not a mesh. The MeshParts inside reference their own mesh asset IDs, and nothing else returns them. [OFFICIAL + COMMUNITY] https://devforum.roblox.com/t/how-to-get-meshid-from-model-upload-cloud-assets-api/3226166

**A. Studio MCP, recommended for this agent.** Call `execute_luau` with `datamodel_type="Edit"`, or use `insert_asset(<modelId>)` and then inspect.

```lua
local InsertService = game:GetService("InsertService")
local ok, model = pcall(InsertService.LoadAsset, InsertService, MODEL_ID)  -- works if you own the asset
assert(ok, model)
local out = {}
for _, d in model:GetDescendants() do
    if d:IsA("MeshPart") then
        table.insert(out, string.format("%s|%s|%s|%s", d.Name, d.MeshId, d.TextureID, tostring(d.Size)))
    end
end
-- keep a clean template: move MeshParts out of the package container into ServerStorage/ReplicatedStorage
local lib = game:GetService("ReplicatedStorage"):FindFirstChild("MeshLib") or Instance.new("Folder")
lib.Name = "MeshLib"; lib.Parent = game:GetService("ReplicatedStorage")
for _, d in model:GetDescendants() do if d:IsA("MeshPart") then d.Parent = lib end end
model:Destroy()
return table.concat(out, "\n")
```

- `LoadAsset` security: the asset must be created or owned by the game creator, shared with them, or owned by Roblox. [OFFICIAL InsertService ref]
- Uploaded models arrive as packages, so you may see a `PackageLink`. Pulling the MeshParts out, as above, avoids package auto-update surprises. [REC]

**B. Headless: Open Cloud Luau Execution** (a staff-suggested path). [STAFF + OFFICIAL spec]

- Call `POST https://apis.roblox.com/cloud/v2/universes/{universeId}/places/{placeId}/luau-execution-session-tasks` with body `{"script":"<the Luau above, ending in return …>"}`.
- Scope: `universe.place.luau-execution-session:write`.
- Rate limit: **5 creates/min** per key owner.
- Poll the returned task path with `GET` (200/min) until `state` is `COMPLETE`, then read `output`.
- The script takes no arguments, so splice the asset ID into the script text.

**C. Building MeshParts from a MeshId later.** `MeshId` can't be assigned. Use either of these: [OFFICIAL]

- `AssetService:CreateMeshPartAsync(Content.fromUri("rbxassetid://"..meshId), {CollisionFidelity=Enum.CollisionFidelity.Box, RenderFidelity=Enum.RenderFidelity.Automatic})`
- Clone a template MeshPart (preferred, because clones keep instancing).

**D. Assign textures uploaded separately** (edit time, through `execute_luau`):

- `mp.TextureID = "rbxassetid://"..imageId`
- Or create `SurfaceAppearance` with `ColorMap="rbxassetid://…"`, `NormalMap=…`, and so on. This needs plugin-level security; the Studio MCP Edit context is expected to have it. [UNVERIFIED: test once]

**Studio Importer instead of Open Cloud.** For anything with textures or rigs, or that needs import options, the Studio Importer is still the official recommendation: preview, error checks, settings. [OFFICIAL] Open Cloud is ideal for batch static meshes.

---

## 4. First-person viewmodel hands

### 4.1 Asset structure

**[REC] Use separate rigid meshes, not a skinned rig, for cheap phones.**

- Make the viewmodel 2 or 3 MeshParts: `LeftArm` and `RightArm` (forearm plus fist), plus an optional held item.
- Parent them under a `Model` with an invisible, anchored, non-colliding `Root` part as the `PrimaryPart`, connected with `Motor6D`s from Root to each arm.

Why not a skinned rig:

- Skinned meshes cost more.
- Skinned MeshParts in a Model without a Humanoid use spatial FastClusters that rebuild when they move. The docs call this "Unnecessary skinned MeshPart movement". [OFFICIAL] performance-optimization/improve
- If you do skin (one mesh with bones), add a `Humanoid` or accept the cluster cost. Use `AnimationController` + `Animator` for playback.
- Bone rules: ≤ 4 influences, root at 0,0,0, `add_leaf_bones=False`.

Budget [REC]:

- About 1.5k–3k triangles per arm, including the outline hull.
- One 512² color texture shared by both arms (UV-mirrored).

**Blender.**

- Model the arms in "camera space": camera at the origin looking down -Y, which becomes Roblox -Z.
- Set each arm's origin at its forearm or shoulder pivot.
- Export one FBX with both arms.
- The Importer and Open Cloud keep each object's pivot ("Use Imported Pivot" is on by default).

### 4.2 Camera attachment (client LocalScript)

```lua
local RunService = game:GetService("RunService")
local cam = workspace.CurrentCamera
local vm = game.ReplicatedStorage.Viewmodel:Clone()      -- client-only: don't replicate viewmodels [OFFICIAL perf tip]
for _, p in vm:GetDescendants() do
    if p:IsA("BasePart") then
        p.Anchored = true; p.CanCollide = false; p.CanQuery = false; p.CanTouch = false
        p.CastShadow = false; p.Massless = true
    end
end
vm.Parent = cam
local OFFSET = CFrame.new(0, -1.2, -1.6)                    -- tune; keep geometry > 0.5 stud from camera
RunService:BindToRenderStep("Viewmodel", Enum.RenderPriority.Camera.Value + 1, function(dt)
    vm:PivotTo(cam.CFrame * OFFSET * swayCF * bobCF)         -- springs computed per frame
end)
```

- Bind **after** the camera update. The default camera runs at `RenderPriority.Camera` (200). [OFFICIAL RunService ref]
- `RenderStepped` also works and isn't deprecated, but `BindToRenderStep` with a priority is deterministic. [OFFICIAL]
- Use `PivotTo`. `SetPrimaryPartCFrame` is legacy. [REC]
- For animated joints, write `Motor6D.Transform`, not `C0`/`C1`. That is the documented efficient path. [OFFICIAL] performance-optimization/improve
- Hide the real character's arms in first person through `LocalTransparencyModifier`. Default first-person mode already hides the character except Tools. [COMMUNITY + OFFICIAL camera docs]

### 4.3 Field of view and clipping

- **FOV:** `Camera.FieldOfView` is the **vertical** FOV, clamped 1–120, default 70. [OFFICIAL]
  - Roblox has no separate viewmodel FOV and no depth-layer clear for the world camera.
  - Wide FOVs (above about 80) stretch the arms. Compensate by moving the arms closer and down. [REC]
- **Near plane:** `Camera.NearPlaneZ` is read-only and between -0.1 and -0.5 studs depending on platform. Keep all viewmodel geometry at least **0.5 stud** in front of the camera, or it gets cut on some devices. [OFFICIAL]
- **Wall clipping options** [REC/COMMUNITY]:
  1. Keep the arms small and close (scale the whole viewmodel down, for example 0.5×, and pull it in). The effective reach then stays under about 1.5 studs and rarely enters walls.
  2. Each frame, raycast from the camera along `LookVector` for about 2 studs, excluding the character and viewmodel. When it hits, lerp the viewmodel back and down, or play a "lowered" pose.
  3. A `ViewportFrame` render of the viewmodel never clips and has its own camera FOV. But it loses world lighting and shadows, and adds a GUI render pass. Use it only if 1 and 2 fail. [UNVERIFIED perf on low-end]

### 4.4 Animation options

**Procedural CFrame springs** [REC]

- Covers idle sway, walk bob, recoil and punch jab.
- No assets to upload, no moderation, works everywhere.
- Drive `vm:PivotTo` plus `Motor6D.Transform` from small spring or lerp functions.

**Animation assets**

- Need an `AnimationController` + `Animator` in the viewmodel with Motor6D or Bone names that match the rig.
- Animation assets must be owned by the experience's creator (user or group). [REC/COMMUNITY]
- **Official route from Blender:**
  1. Export FBX with `bake_anim=True`.
  2. In Studio, open the Animation Editor on the matching rig and use "… › Import › **From FBX Animation**". [OFFICIAL] https://create.roblox.com/docs/art/characters/export-avatar-animations-from-maya
  3. Save. This creates a `KeyframeSequence` under the rig's `AnimSaves` or `ServerStorage.RBX_ANIMSAVES`.
  4. Publish from the Animation Editor.
  - The Animation Editor steps are manual UI, so an agent can't run them through MCP tools.
- **Open Cloud path:** `assetType "Animation"` accepts a `.rbxm` or `.rbxmx` containing a KeyframeSequence (`model/x-rbxm`). [OFFICIAL + STAFF]
- **Getting the `.rbxm` without manual UI** [UNVERIFIED end-to-end; each link is documented]:
  1. In Studio `execute_luau` (plugin context), build the KeyframeSequence, or take the one the Animation Editor saved.
  2. Call `game:GetService("SerializationService"):SerializeInstancesAsync({kfs})`. It returns `.rbxm` as a buffer and is plugin- or Luau-Execution-only. [OFFICIAL]
  3. Base64 it and return it as text.
  4. Write the file and upload it as `"Animation"`.
- **Studio-only testing:** `AnimationClipProvider:RegisterActiveAnimationClip(kfs)` gives a temporary `active://` ID. It doesn't work in live games. [OFFICIAL]
- `AssetService:CreateAssetAsync` can't publish animations. It supports only Model, Plugin, Mesh, Image and Audio. [OFFICIAL]

### 4.5 Outline options for the hands

| Option | Mobile cost | Notes |
|---|---|---|
| **Inverted hull baked into the same mesh** [REC, best] | +~100% triangles, **0 extra draw calls** | 1. In Blender, duplicate the arm mesh. 2. Shrink/Fatten (Alt+S) by 0.02–0.04 studs. 3. Flip its normals. 4. Join it into the arm object. 5. Map all hull UVs onto a pure-black texel of the atlas. Roblox back-face culling (`DoubleSided=false`, importer "Make Double Sided" off) shows only the hull's back side as a rim. It stays one MeshPart, one material and one draw call. |
| Separate hull MeshPart | +1 draw call per part (instanced if repeated) | Easier to tweak. Same `DoubleSided=false` requirement. |
| Ink lines painted or baked into the ColorMap | Free | Use for interior creases (knuckles, fingers). Combine with the hull for the silhouette. |
| `Highlight` (OutlineColor black, FillTransparency 1) | First highlight **up to ~1 ms GPU on mobile**. Cost grows with screen coverage on mobile. Each highlighted object is drawn individually (an extra draw call) plus a post-process pass. | **Avoid on hands** because they cover a big part of the screen. Limit: **255** Highlights client-side; disabled ones still count. The old "31" limit is obsolete (raised 2025-11-10). [OFFICIAL] https://create.roblox.com/docs/effects/highlighting · [STAFF] https://devforum.roblox.com/t/lights-camera-more-highlights/4061534 |

---

## 5. Ink-outline / comic-shaded look on Roblox

Roblox has no custom shaders. The style comes from the art and the global lighting. [REC unless noted]

### 5.1 Geometry and texture

**Silhouette lines:** inverted hull (4.5) on characters, viewmodel and hero props.

- Line width is in world units, so distant lines get thinner, which reads as natural "ink".
- On props that repeat, keep the hull in the same mesh so instancing still applies.

**Interior lines and cel bands baked into the color map.** This is the cheapest and fully mobile-safe.

1. In Blender, build the shader: Shader to RGB → Color Ramp (Constant, 2–3 bands) → Emission. EEVEE is needed for Shader to RGB.
2. Bake the shading into the texture. Or hand-paint bands.
3. Overlay crease and contour lines. Bake a cavity, AO or edge mask, threshold it to black, and multiply it in.
4. Export at 256–512.

**Flat colors.**

- `Material = SmoothPlastic` with `TextureID`. Avoid PBR normal and roughness maps that fight the flat look.
- If you use SurfaceAppearance, set roughness to 1 and metalness to 0.

**Emissive mask.** `SurfaceAppearance.EmissiveMaskContent` plus `EmissiveStrength` can keep ink and highlight colors punchy regardless of lighting. [OFFICIAL feature; stylistic use UNVERIFIED]

### 5.2 Lighting

**Lighting technology settings have changed.** [OFFICIAL]

- **`Lighting.Technology` (Future, ShadowMap, Voxel, Compatibility) is deprecated.**
- It is replaced by **`Lighting.LightingStyle`** (`Realistic` | `Soft`) and **`Lighting.PrioritizeLightingQuality`** (bool).
- "Soft" is "a flat, retro-Roblox look with softer lights and shadows".
- "Soft with [PrioritizeLightingQuality] enabled uses shadow maps rather than voxel lighting".
- `ShadowSoftness` only applies with Realistic.
- LightingStyle can only be set "in the Properties window". Expect to set it by hand. Via MCP it is [UNVERIFIED].
- Sources:
  - https://create.roblox.com/docs/environment/lighting
  - https://create.roblox.com/docs/reference/engine/classes/Lighting

**For a comic look on mobile** [REC]:

- `LightingStyle = Soft`.
- `PrioritizeLightingQuality = false`. It favors view distance on low-end devices. Set it to true only if crisp sun shadows are core to the style.
- Raise `Ambient` and `OutdoorAmbient` (for example around RGB 110–140 gray) so shadow sides don't go muddy. The baked bands provide the "shading".
- `EnvironmentDiffuseScale` 0–0.3 and `EnvironmentSpecularScale` 0 flatten PBR response.
- Few or no shadow-casting local lights. Set `CastShadow = false` on small props.
- The engine disables shadows entirely below graphics quality 4. Don't rely on shadows for readability. [OFFICIAL] performance-optimization/improve

### 5.3 Post-processing [REC]

- **`ColorCorrectionEffect`:** Saturation +0.15–0.3, Contrast +0.1–0.2. This is the cheapest "comic pop".
- **`BloomEffect`:** low Intensity (about 0.3), high Threshold (about 1.5–2) so only emissives glow. High bloom washes out ink lines.
- Skip `DepthOfField`, `SunRays` and `Blur` for mobile.
- The available effects are Bloom, Blur, ColorCorrection, DepthOfField, SunRays and ColorGrading. [OFFICIAL] https://create.roblox.com/docs/environment/post-processing-effects

**`Highlight` usage:** only for gameplay signals (interactables, enemies), one per Model, with `DepthMode = Occluded` unless you need see-through. Change properties instead of adding and removing Highlights, because adding or removing triggers geometry rebuilds. [OFFICIAL]

---

## 6. Mobile performance budgets

**Player base** [OFFICIAL] https://create.roblox.com/docs/performance-optimization/test-on-hardware

- About 65% Android.
- About 60% of Android players have **2–4 GB RAM**.
- More than 50% of players are on devices scoring 10k–20k PassMark.
- Example low-end test devices: Infinix Smart 9, Moto G05, Oppo A18, Fire HD 10 (2023).

**Official example ceiling:** "stay below **1,000 draw calls** and **1,000,000 triangles**" on *their* baseline device. Measure with Shift+F2 Render stats. [OFFICIAL] https://create.roblox.com/docs/performance-optimization/design

**[REC] targets for cheap phones (aim well under the official example):**

| Budget | Target |
|---|---|
| Visible draw calls | ≤ 300–500 |
| Visible triangles | ≤ 300k–500k |
| Viewmodel (both arms + hull) | ≤ 5k tris, 1× 512² texture |
| Small prop | 100–800 tris, 128–256² |
| Medium prop or furniture | 800–3k tris, 256–512² |
| Hero or large structure | ≤ 8k tris, ≤ 1024² (often a trim sheet) |
| Characters/NPCs | 3k–8k tris, 512² |
| Unique textures loaded at once | Keep total pixel count low. One 1024² costs as much as four 512². |

**Instancing rule** [OFFICIAL] performance-optimization/improve:

- Meshes with the **same `MeshContent`** are drawn in one draw call when their **SurfaceAppearance is identical**.
- If there is no SurfaceAppearance, the **TextureContent must be identical**.
- If there is neither, the **Material must be identical**.

What breaks instancing:

- Importing a whole scene at once, which gives duplicate mesh IDs for identical props.
- Per-instance texture variants. Tint with `MeshPart.Color` or `SurfaceAppearance.Color` instead.

**Other official levers:**

- Instance streaming, on by default for new places.
- `Model.LevelOfDetail = SLIM` for distant models.
- `RenderFidelity = Performance` or `Automatic`.
- Trim sheets and atlases for batchable parts. Prefer unique textures otherwise, because streaming loads an entire atlas at the requested resolution.
- Avoid stacked semi-transparency (overdraw).
- Avoid many `Texture`, `Decal` and particle instances. They don't batch.

---

## 7. Checklist: "Blender → Roblox asset is done when…"

1. **Scene units.** Unit System = None, Rotation = Degrees, Unit Scale 1.0. The asset is sized in studs (1 stud = 28 cm; avatar about 5–6 studs).
2. **Topology.**
   - Watertight, no zero-thickness faces, quads where possible.
   - ≤ 20,000 triangles per mesh (hard), and inside the [REC] budget for its class (section 6).
   - AI or `generate_3d` meshes are decimated and retopologized.
3. **Transforms.**
   - Rotation and scale applied, no negative scale.
   - Origin set to the intended Roblox pivot.
   - Asset placed at the world origin.
   - Front faces -Y.
4. **Normals.** Recalculated outside, Smooth by Angle set, no flipped faces (except the intentional outline hull).
5. **Materials and UVs.**
   - One material per object, one UV set inside 0–1.
   - Principled BSDF wired as in 1.7.
   - Normal maps are OpenGL.
   - Textures 256–512 (1024 only for heroes).
6. **Naming.** Clean names, no accidental `_Att`, `_InnerCage` or `_OuterCage` suffixes. Rigs: no leaf bones, ≤ 4 influences, root at 0,0,0 with no influences.
7. **Export.** FBX with `use_selection`, `FBX_SCALE_UNITS`, `axis_forward='Z'`, `axis_up='Y'`, Apply Modifiers, `add_leaf_bones=False`, `bake_anim=False` (unless it's an animation), `path_mode='COPY'` plus `embed_textures=True`. The file is ≤ 20 MB.
8. **Upload.**
   - Textures went up as `assetType "Image"` and the meshes as `"Model"`, using the same creator (user or group) as the experience.
   - The operation is `done`, the moderation state isn't Rejected, and the asset IDs are recorded in a manifest (file → assetId → meshIds → imageIds).
9. **Extract.**
   - Model inserted through Studio MCP and MeshParts moved to a `MeshLib` template folder.
   - `MeshId`, `TextureID` and `Size` logged.
   - Scale test passed (4×1×2 test box reads 4,1,2), and orientation test passed (front = `LookVector`).
10. **Configure.**
    - `Anchored` set.
    - `CollisionFidelity` is Box, Hull or Default (never Precise).
    - `CanCollide`, `CanQuery` and `CanTouch` set deliberately.
    - `RenderFidelity` is Automatic or Performance.
    - `CastShadow` is off on small or decorative pieces.
    - `DoubleSided` is off.
    - Textures assigned (`TextureID`, or a SurfaceAppearance at edit time).
11. **Reuse.** Every copy in the place is a clone of the template (same MeshId and texture), so instancing works. There are no duplicate uploads of the same mesh.
12. **Look.**
    - Outline hull visible and evenly thick.
    - Baked ink and cel bands read under `LightingStyle=Soft`.
    - Checked with Studio MCP `screen_capture` at a distance and up close.
13. **Perf.** Shift+F2 in a busy view stays under the [REC] budgets on a low-end device (or the Device Emulator, with real-device memory checks later), and there are no Highlights on large screen areas.

---

## Sources

**Roblox Creator Docs** (all read from `github.com/Roblox/creator-docs`, commit of 2026-10-24):

- https://create.roblox.com/docs/art/blender (units, axes, FBX scale)
- https://create.roblox.com/docs/art/modeling/export-requirements
- https://create.roblox.com/docs/art/modeling/specifications
- https://create.roblox.com/docs/art/modeling/texture-specifications
- https://create.roblox.com/docs/art/modeling/surface-appearance
- https://create.roblox.com/docs/art/modeling/assign-textures
- https://create.roblox.com/docs/art/modeling/rigging
- https://create.roblox.com/docs/art/characters/export-avatar-animations-from-maya (From FBX Animation)
- https://create.roblox.com/docs/studio/importer
- https://create.roblox.com/docs/studio/mcp
- https://create.roblox.com/docs/parts/meshes
- https://create.roblox.com/docs/parts/textures-decals
- https://create.roblox.com/docs/parts/materials
- https://create.roblox.com/docs/parts/models
- https://create.roblox.com/docs/physics/units
- https://create.roblox.com/docs/cloud/guides/usage-assets
- https://create.roblox.com/docs/cloud/auth/api-keys
- https://create.roblox.com/docs/cloud/reference/rate-limits
- https://create.roblox.com/docs/projects/assets/privacy
- https://create.roblox.com/docs/effects/highlighting
- https://create.roblox.com/docs/environment/lighting
- https://create.roblox.com/docs/environment/post-processing-effects
- https://create.roblox.com/docs/performance-optimization/improve
- https://create.roblox.com/docs/performance-optimization/design
- https://create.roblox.com/docs/performance-optimization/test-on-hardware

**Roblox API reference:**

- Engine classes: MeshPart, SurfaceAppearance, MaterialVariant, Highlight, Lighting, Camera, RunService, InsertService, AssetService, SerializationService, AnimationClipProvider
- Enums: RenderFidelity, CollisionFidelity, LightingStyle, AlphaMode
- Open Cloud specs: `reference/cloud/assets/v1.json` and `reference/cloud/openapi.json` (asset-quotas, luau-execution)

**DevForum:**

- [STAFF] https://devforum.roblox.com/t/open-cloud-upload-support-for-more-asset-types/4022082 (2025-10-23)
- [STAFF] https://devforum.roblox.com/t/lights-camera-more-highlights/4061534 (2025-11-10, Highlight limit 255)
- [COMMUNITY+STAFF reply] https://devforum.roblox.com/t/how-to-get-meshid-from-model-upload-cloud-assets-api/3226166
- [COMMUNITY] Viewmodel threads:
  - https://devforum.roblox.com/t/designing-an-fps-framework-beginners-guide/1198208
  - https://devforum.roblox.com/t/animating-fps-viewmodel-arms/1122319
  - https://devforum.roblox.com/t/fps-viewmodel-help/396845

**Tools:**

- https://github.com/ahujasid/blender-mcp (README and `src/blender_mcp/server.py`, HEAD 2026-10-24; legacy tool names from the 2025-12-08 commit)
- Blender FBX exporter: https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core/io_scene_fbx (`__init__.py`, `fbx_utils.py`, `export_fbx_bin.py`)
- asphalt uploader (community reference implementation): https://github.com/jackTabsCode/asphalt (`src/web_api.rs`, `src/asset.rs`)
