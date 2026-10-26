# Private cubes in one shared space: a Roblox technical study

Researched 2026-10-26. The design: every player digs their **own** 100×100×100 cube of 4-stud blocks (400 studs wide).
All cubes sit at the **same world position**, so players see each other as "ghosts" moving through their own tunnels.
Blocks and collisions are never shared.

Legend: **[DOC]** official create.roblox.com docs · **[STAFF]** a Roblox staff post · **[COMM]** a community or DevForum
post · **[EST]** my own estimate or inference · **[UNVERIFIED]** not confirmed by any source; test it in Studio.

---

## 1. Client-only geometry (parts made by a LocalScript)

**Does it collide with the local character? Yes.**
- A part made by a LocalScript exists only on that client. The client simulates its own character (it owns the
  character's network ownership), so the character collides with local parts. Local client-sided obbies and doors are
  built on this. [COMM] https://devforum.roblox.com/t/are-local-parts-possible/951032 ("the client will register the
  collision. This won't cross between other clients"),
  https://devforum.roblox.com/t/local-collision-filtering/493897
- Local parts that are unanchored can still be pushed by other players' replicated characters on your client. Our blocks
  are **anchored**, so this doesn't apply. [COMM] https://devforum.roblox.com/t/local-pushing-boxes/1801910

**Gotchas**
1. **The server sees the player floating or "inside walls".** The server has no blocks in the cube volume, so to it
   every player hangs in empty air inside a 400-stud box. A player's character is client-owned, so the server doesn't
   simulate gravity on it and won't "correct" it. Don't run a generic anti-fly or anti-noclip check that uses server
   parts or raycasts. Do all movement checks against **that player's own server grid** (see §5).
2. **Never teleport a player from the server without a grid-safe target.** `PivotTo` or `CFrame` sets from the server,
   such as an anti-cheat rollback or a respawn, can drop the character inside local solid blocks. That gets it stuck or
   flung. Pick the target from the per-player grid: an air cell with air above it and solid below it. [EST]
3. **Spawning and loading order.** Set `Players.CharacterAutoLoads = false`. Spawn (`LoadCharacter`) only after the
   client reports "cube meshed around the spawn point". Otherwise the character falls through geometry that isn't built
   yet. [EST]
4. **Server Authority (2026).** Roblox's new server-authoritative physics (`Workspace.AuthorityMode = Server`, with
   client prediction and rollback) predicts near the local player and rolls back to the server's state. [DOC]
   https://create.roblox.com/docs/en-us/projects/server-authority.md · announcement (July 2026)
   https://about.roblox.com/newsroom/2026/07/creating-responsive-cheat-resistant-games-roblox-server-authority
   The server has no blocks, so it can't agree with client collisions against client-only walls. **Keep AuthorityMode on
   the default (client-owned characters).** [EST, inference. The docs don't discuss client-only parts.]
5. **StreamingEnabled.** Roblox staff confirmed that **client-created Terrain** can be streamed out and stop colliding.
   They advised: "I would avoid client created terrain if possible" (Sep 4, 2025). [STAFF]
   https://devforum.roblox.com/t/client-sided-terrain-stops-being-interactable-with-after-being-streamed-out-and-back-in/3910355
   Client-created **Parts** are generally believed to be left alone by streaming. [UNVERIFIED] Test this. Turning off
   StreamingEnabled for this place is reasonable, because the map is tiny (a hub plus one cube volume).
6. **Server physics touches:** none. The server never sees your blocks, so `Touched` on the server, server raycasts, and
   NPC pathfinding against blocks don't work. Keep all block logic grid-based.
7. **Progress must be server-validated.** Anything a LocalScript does is invisible to the server. Every dig goes through
   a remote and is validated against the server grid. [COMM] https://devforum.roblox.com/t/2536167

**How existing games do per-player client worlds:** client-sided obbies and doors, and per-player effects. The pattern is
always "server holds truth, client renders". [COMM] (threads above). I found no public write-up of a big Roblox hit that
uses overlapping per-player worlds in one physical space. [UNVERIFIED that any top game does exactly this.] The closest
public voxel engines (below) are server-streamed and shared, not per-player.

---

## 2. Making other players non-colliding ghosts

**CollisionGroups**
- Only **server** Scripts can register groups and change group-vs-group rules. A **LocalScript can set an individual
  part's `CollisionGroup` property**, and that change is local only. [DOC]
  https://create.roblox.com/docs/en-us/reference/engine/classes/PhysicsService.md · [COMM]
  https://devforum.roblox.com/t/local-collision-filtering/493897
- Registering groups at runtime has overhead that grows with the number of BaseParts, so register them in Studio at edit
  time. [DOC] (PhysicsService page)
- A LocalScript setting the *character's* group doesn't change what the server sees. Set character groups **on the
  server** (on CharacterAdded). [COMM] https://devforum.roblox.com/t/2495068
- **Setup:** in Studio, register the groups `Players`, `Blocks` and `Ghosts`. Rules: `Players`↔`Players` = false,
  `Players`↔`Blocks` = true, `Ghosts`↔everything = false. The server puts every character part in `Players`. Each
  client puts its own block parts in `Blocks`, and *locally* moves other characters' parts to `Ghosts`. That's
  belt-and-braces: other characters are kinematic replicas on your client anyway.

**Ghost look**
- Use `BasePart.LocalTransparencyModifier` or `Transparency` on other characters' parts from a LocalScript. This is
  client-only and doesn't replicate. The default first-person camera script also writes `LocalTransparencyModifier`, but
  only on *your own* character, so use it freely on others. Apply the change on `DescendantAdded` and don't loop every
  frame. [COMM] https://devforum.roblox.com/t/2591071,
  https://devforum.roblox.com/t/choppy-arms-when-forcing-first-person-localtransparencymodifier/1709769
- **Seeing through your own walls:** other players are usually inside *your* solid stone, so they're hidden. Fix:
  `Highlight` with `DepthMode = AlwaysOnTop`, a pale FillColor, FillTransparency ~0.7 and a soft outline.
  - **Limit is now 255 highlights per client**, not 31. The docs say: "As a performance limit, Studio only displays 255
    simultaneous Highlight instances on the client-side at a time." [DOC]
    https://create.roblox.com/docs/en-us/effects/highlighting (older pages and threads still say 31:
    https://devforum.roblox.com/t/increase-highlight-limit/2628557/13)
  - Performance [DOC, same page]: the **first** highlight on screen costs the most GPU, and extra ones add little.
    Adding or removing a Highlight forces a geometry rebuild, so toggle properties instead of creating and destroying
    them. Mobile cost grows with the screen area covered. Off-screen, disabled or fully transparent highlights cost
    nothing. **With 8–12 players this is fine.** Use one Highlight per character model, not per part.
- **Cheap alternatives or extras:** a `BillboardGui` with `AlwaysOnTop = true` (name and a dot, distance-scaled, hidden
  past N studs). `SelectionBox` on the HumanoidRootPart, also drawn on top. A tiny low-poly "ghost" MeshPart welded
  locally, with ForceField or Neon material and Transparency 0.5. These cost basically nothing at 12 players.
- **"Big effects" from others:** the server rebroadcasts a compact cosmetic event, for example `{userId, effectId,
  cellIndex}`, using an **UnreliableRemoteEvent** (it's fine to lose one). Each client plays the particles and sound
  only. It **never** edits its own grid from someone else's event.

---

## 3. Voxel storage and meshing in Luau

### 3.1 `buffer`
- Max size is **1 GiB** (1,073,741,824 bytes). Integer and float reads and writes are little-endian. It has
  `readbits`/`writebits` (0–32 bits), `copy` (safe for overlapping ranges) and `fill`. Passing a buffer through
  Roblox APIs and events delivers a **copy**, and one buffer object can't be used from several Actors. [DOC]
  https://create.roblox.com/docs/en-us/reference/engine/libraries/buffer.md · RFC https://rfcs.luau.org/type-byte-buffer.html
- No official ns-per-read numbers. In practice `buffer.readu8` and `writeu8` are among the fastest operations in Luau,
  especially under `--!native`. [COMM] https://devforum.roblox.com/t/is-it-possible-to-optimize-this/4037540 [EST:
  roughly 10–50M reads/s on desktop, a few times slower on low-end phones. **Benchmark it.**]
- **Layout:** 1 byte per cell, `index = x + y*N + z*N*N`. 100³ = **1,000,000 bytes (≈1 MB)** per cube. The 126³ "Large"
  cube is ≈2 MB. With 8 players × 1 MB on the server, that's trivial. Values: 0 = air, 1–5 = depth band, 10+ = special
  or the box. Bit-pack only for **save and network** (1 dug bit per cell = 125,000 bytes).

### 3.2 Meshing: use **3D greedy box merging into Parts**, not face meshing
- Classic greedy *face* meshing (2D quads per face direction) suits mesh renderers. **With Parts, each part is a
  solid box**, so the right method is **3D greedy box decomposition of solid cells**: grow along X, then Z, then Y.
  - An untouched chunk is **1 part**. A tunnel through a chunk splits it into a handful of boxes. Collision exactly
    matches the grid, with no holes and no z-fighting (boxes don't overlap).
  - Explainer: "Consume everything – how greedy meshing works" [COMM] https://devforum.roblox.com/t/-/452717 ·
    https://devforum.roblox.com/t/greedy-meshing-different-sized-voxels/1516576
- **Evidence that part count is the main lever:** one developer reports **15,931 instances dropping to 508** after
  merging [COMM, via a search summary]. Roblox draws parts even when hidden, so part count drives cost. [COMM]
  https://devforum.roblox.com/t/voxels-in-roblox/644824
- **Open-source and public examples:**
  - `tamarthur/voxel-engine` (GitHub, Oct 2026): greedy meshing into parts, **16 Actors** for parallel chunk builds,
    and a sparse lazily allocated "Tensor" store. No timings published. https://github.com/tamarthur/voxel-engine
  - VoxelDestruct 2.1: greedy meshing, a part cache (default `CachePrecreated = 10000`, `CacheExtra = 100`) and optional
    client offloading. No benchmarks.
    https://devforum.roblox.com/t/voxeldestruct-21-voxelated-destruction-physics-with-greedy-meshing-hitboxes-and-more/3044264
  - Voxel Destruction System: per-chunk greedy meshing, "all the hard work done in parallel", main thread only sets
    part properties, BulkMoveTo plus a part cache, and a queue that spreads part updates over frames. No numbers.
    https://devforum.roblox.com/t/voxel-destruction-system/3864250
  - "Optimizing chunked terrain made of parts": 11×1×11 chunks. Splitting work over 4–8 Actors "didn't help much", and
    moving table reads and writes into Actors "broke everything". Advice: pool parts, keep each frame's work under
    ~8 ms with dynamic yielding. [COMM] https://devforum.roblox.com/t/optimizing-chunked-terrain-made-of-parts/3730494
  - **No public, trustworthy ms-per-chunk benchmark exists.** [UNVERIFIED] My estimate for a 3D greedy pass over a
    20³ = 8,000-cell chunk in `--!native` Luau: **≈0.3–1 ms desktop, ≈1–4 ms mid-range phone**. [EST, benchmark it in
    M1]

### 3.3 Chunk size
- **Pick a size that divides the cube edge**, so there are no partial chunks: **20 for 100³** (5³ = 125 chunks),
  **21 or 18 for 126³**. 16 is fine too, with clipped edge chunks.
- Trade-offs [EST]: smaller chunks (8–10) re-mesh faster per dig, but untouched space costs more parts (1,000 chunks
  for 100³ at size 10). Bigger chunks (32) mean fewer parts but slower re-meshes. With 3D box merging, untouched chunks
  are 1 part each, so **20 is the sweet spot**: the initial cube is ~125 parts, and one dig re-meshes 8,000 cells plus
  up to 3 neighbors only when on a border. (You only need neighbors with *face-meshing*. With box merging, a chunk
  doesn't depend on its neighbors, so **only the touched chunk re-meshes**.)
- The cube's outside: by default the hub sees all 6 faces. Since box merging gives ~125 parts for the untouched cube,
  no special "outer shell" mesh is needed.

### 3.4 Parallel Luau
- Write APIs on instances are not parallel-safe. Do the math in parallel, then make or modify parts serially. [STAFF]
  https://devforum.roblox.com/t/full-release-of-parallel-luau/1836187
- Buffers are copied when sent between Actors, and one buffer can't be used from several Actors [DOC buffer page]. Use
  `SharedTable` or message a copy of the chunk slice (8 KB for 20³, cheap).
- [EST] For one player digging ~10–30 cells/s, **serial meshing of one 20³ chunk per frame is enough**. Use Actors only
  for the initial build of a saved, heavily dug cube (125 chunks), or for spells that touch many chunks at once.

### 3.5 Part budget, pooling, creation cost
- There's no official mobile part limit. Community reports say ~13k parts is OK, and 15–20k+ starts to hurt mobile.
  [COMM] https://devforum.roblox.com/t/13000-parts-is-it-too-much/344990,
  https://devforum.roblox.com/t/some-questions-about-part-count/365805
  Roblox instancing batches identical meshes and materials into few draw calls. [STAFF 2017]
  https://devforum.roblox.com/t/rendering-updates-september-2017/54148
- **Target: ≤3,000 block parts on mobile, ≤8,000 on PC.** [EST] With 3D merging, a heavily dug cube (tens of
  thousands of cells dug) should stay at low thousands. If it goes over, merge long-untouched chunks more aggressively or
  hide chunks beyond ~150 studs (the player is underground, so the far view is walls anyway).
- Per-block parts are impossible: 1,000,000 parts, or ~60k even for a "visible shell" only.
- **Pooling:** reuse parts (ObjectCache or PartCache style). `Instance.new` plus parenting is the costly part. Park
  unused parts far away and move them with `workspace:BulkMoveTo(parts, cframes, Enum.BulkMoveMode.FireCFrameChanged)`.
  [COMM] https://github.com/Pyseph/ObjectCache,
  https://devforum.roblox.com/t/objectcache-a-modern-blazing-fast-model-and-part-cache/3104112,
  https://devforum.roblox.com/t/partcache-for-all-your-quick-part-creation-needs/246641
  Resizing a pooled part (`Size`) still costs a physics update. [EST] Fine at a few parts per dig.
- **Part settings:** `Anchored = true`, `CastShadow = false` (the docs recommend turning off shadows on parts where
  they're not needed), `CanTouch = false`. Set `CanQuery = false` if digging uses a **grid DDA raycast** (recommended:
  faster and exact). `CollisionFidelity` doesn't apply to box parts. [DOC]
  https://create.roblox.com/docs/performance-optimization/improve.md

### 3.6 Look: Texture vs SurfaceAppearance vs MaterialVariant
- `SurfaceAppearance` applies to MeshParts only, not to box Parts. Skip it.
- **MaterialVariant** (a custom PBR material on a base Material, with `StudsPerTile = 4`) gives **zero extra
  instances** and tiles across merged boxes. Its alignment origin on merged parts is **[UNVERIFIED]**. If tiles land
  half a block off on odd-length boxes, block seams won't line up with the 4-stud grid.
- A `Texture` object per face has a corner origin with `StudsPerTileU/V = 4` plus `OffsetStudsU/V`, so it aligns
  exactly when boxes sit on the 4-stud grid. [DOC] https://create.roblox.com/docs/reference/engine/classes/Texture.md
  · [COMM] https://devforum.roblox.com/t/how-to-avoid-texture-to-do-this/1377658
  The catch: up to 6 extra instances per part, and decals and textures each add draw calls. [COMM]
  https://devforum.roblox.com/t/does-roblox-use-mesh-instancing/399564
- Recommendation: use **MaterialVariant per depth band** (5 variants, color by band). Verify grid alignment in M1. If
  it's misaligned, fall back to Textures only on faces that face air (≤2–3 per part in tunnels).
- Image budget: ≤512×512 per texture, since 1024² uses 4× the GPU memory. [DOC, improve page]

### 3.7 EditableMesh: current state (Oct 2026) and verdict
- **Still needs ID verification.** In published experiences the owner must be "**13+, ID-verified, and explicitly
  opted-in**" (the "Allow Mesh / Image APIs" toggle). For group games, the group owner. [STAFF]
  https://devforum.roblox.com/t/client-beta-in-experience-mesh-image-apis-now-available-in-published-experiences/3267293
  Roblox listed "Reconciling the extra ID Verification requirement" as **still in progress** in Aug–Sep 2026.
  [STAFF] https://devforum.roblox.com/t/full-release-editablemesh-batching-apis-parallel-queries/4779401
  (Feature request: https://devforum.roblox.com/t/remove-required-id-verification-for-editablemeshesimages/3981479)
- **Limits:** "60,000 vertices and 20,000 triangles" per EditableMesh [DOC]
  https://create.roblox.com/docs/en-us/reference/engine/classes/EditableMesh.md. There's a **dynamic per-device memory
  budget**: creation returns `nil` when it's used up, and low-end devices get less [STAFF, 2024 post above]. One
  developer hit the budget at **8 EditableMeshes** on a client [COMM, Apr 2026]
  https://devforum.roblox.com/t/editablemesh-restrictions/4566101. **No replication**: clients see a checkerboard box
  for a server-made mesh (same thread). Mesh edits don't update **collision** until you call
  `CreateMeshPartAsync` / `ApplyMesh` again, which yields. Precise collision for tunnels would need
  PreciseConvexDecomposition, the most expensive mode [DOC improve page].
- New in 2026: batching APIs (~8× faster) and parallel *read* queries (~2×), live in published experiences from Sep 15,
  2026 [STAFF, same post]. `CreateDataModelContentAsync` (beta) gives higher memory budgets and replication.
  [COMM] https://devforum.roblox.com/t/editablemesh-restrictions/4566101
- **Verdict:** don't use it for the cube. The ID-verify gate, nil-on-budget on phones, collision rebuilds that yield,
  and render bugs (flat axis-aligned planes may not render, frustum culling glitches [STAFF 2024 post]) all cost more
  than they save. At most, use it later as an optional cosmetic skin layer over invisible collision parts on PC.

---

## 4. Terrain per player?

- `Workspace.Terrain` is **one shared object**, so a "server-side terrain cube per player at the same spot" is
  **impossible**. Confirmed by design.
- **Client-side Terrain edits** (`FillBlock`, `WriteVoxels` from a LocalScript) **stay local and don't replicate**. The
  local character collides with them, so per-client terrain is technically possible [COMM]
  https://devforum.roblox.com/t/can-we-tween-terrain/914108,
  https://devforum.roblox.com/t/where-should-i-render-terrain/2091534. But:
  - Roblox staff (Sep 2025): client-created terrain **can be streamed out and stop colliding**. "I would avoid client
    created terrain if possible." [STAFF] (link in §1)
  - A mining game saw client-generated terrain blocks **randomly missing collision**; staff couldn't reproduce it.
    [COMM] https://devforum.roblox.com/t/terrain-hitbox-not-generating/3795113
  - **It doesn't look blocky.** Terrain is smooth-meshed. Occupancy and neighbors morph cell shapes, edges are
    bevelled, and automatic LOD makes distant terrain chunkier. The cells are 4 studs, which matches our grid, and some
    "cube-shaped" materials look squarer. [COMM]
    https://devforum.roblox.com/t/improving-terrain-generation/3140228, https://devforum.roblox.com/t/terrain-lod-grid/2771370
    No true blocky or Minecraft terrain mode exists. `Terrain.Decoration` is only animated grass.
  - The upsides are real: native meshing, very cheap 1-cell edits, near-zero instance count, and MaterialVariants can
    reskin terrain materials.
- **Verdict:** keep Terrain as an **emergency fallback** only, for example if part counts explode on phones and you
  accept a soft "rock cave" look. Turn off StreamingEnabled if you ever use it. Primary: **client Parts with 3D greedy
  boxes.**

---

## 5. Networking and validation

- **UnreliableRemoteEvent:** payloads **>1000 bytes are dropped** (the current docs, up from 900). It's unordered and
  lost events aren't resent. [DOC]
  https://create.roblox.com/docs/en-us/reference/engine/classes/UnreliableRemoteEvent.md
- **Rate limit:** client→server `FireServer` is "approximately **500 requests per second, per client**", shared
  across all remotes of the same type. [DOC]
  https://create.roblox.com/docs/reference/engine/classes/RemoteEvent.md
  "50 KB/s per player" is a **community** figure, not documented. [COMM]
  https://devforum.roblox.com/t/2597139
- **Dig protocol:** use a **reliable RemoteEvent**, batched every ~0.1 s. Payload: a `buffer` of 3-byte cell indices
  (100³ < 2²⁴) plus a 1-byte tool id. At 30 digs/s that's ~10 events/s and ~100 B/s per player. Explosive spells send
  `{center, radius, spellId}` (≈10 bytes) and the server expands them. Cosmetic rebroadcast to others goes over
  **Unreliable**.
- **Client prediction:** remove cells locally right away and re-mesh. If the server rejects a dig, it replies with a
  correction (the cell index and its true value), and the client restores it.
- **Server validation per dig** (all O(1) [EST]):
  1. The cell is in range, solid, and not bedrock or out of bounds.
  2. **Exposed:** at least one face neighbor is air, or the cell is on the cube surface. This blocks "dig through
     walls".
  3. **Reach:** distance from the server-side HumanoidRootPart to the cell center ≤ reach + latency slack (e.g. 3
     blocks + 6 studs).
  4. **Rate:** a token bucket per player sized to their build (e.g. 30/s, burst 10).
  - Cost: 8 players × 30 digs/s = 240 checks/s × ~10 buffer reads = **~2,400 reads/s, which is microseconds per frame**.
    [EST]
- **Anti-noclip (per-player grid):** at 5–10 Hz, sample the root position. Map the character's 1×2-cell footprint to
  cells. If any are **solid in that player's grid** for more than ~0.5–1 s (grace for in-flight digs, since physics
  replication and remotes aren't mutually ordered), flag it. Also walk a **3D DDA** between consecutive samples to catch
  fast passes through solid. Respond with a soft rollback to the last valid position (grid-safe), then a kick on
  repeats. Keep counters per player, never global. [COMM]
  https://devforum.roblox.com/t/how-do-you-stop-no-clipping/691640,
  https://devforum.roblox.com/t/simplifying-anti-no-clip/1542813, https://devforum.roblox.com/t/ways-to-make-anticheat-better/966350
- **Speed and fly:** max horizontal speed per sample. "Falling" is legal only when the cell below is air in the grid.

---

## 6. Persistence

- DataStore value limit: **4,194,304 characters per key**, measured on the serialized (JSON) string. Roblox's own
  internal compression doesn't help you. [DOC]
  https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits.md
- Per-key throughput: **write 4 MB/min, read 25 MB/min**, rounded up per 1 KB. The old **6 s same-key cooldown was
  removed**. [DOC] + [STAFF] https://devforum.roblox.com/t/2436230
- Server budget: Get and Set are each **60 + 40 × players per minute** (current docs; older posts say +10).
  `UpdateAsync` uses both budgets. Experience storage is **500 MB + 1 MB × lifetime users**. [DOC, same page]
- **Compression:** `EncodingService:CompressBuffer(buf, Enum.CompressionAlgorithm.Zstd, level)` (levels −7..22,
  default 1), then `Base64Encode`, then store the string. Decompression caps at 1 GB. Call `GetDecompressedBufferSize`
  before decompressing untrusted data. [DOC]
  https://create.roblox.com/docs/en-us/reference/engine/classes/EncodingService.md · community wrapper:
  https://devforum.roblox.com/t/fastest-text-compression-zstd/3815978
  (Storing a raw `buffer` value directly in DataStores: **[UNVERIFIED]**, not found in current docs. Use the explicit
  compress + base64 path.)
- **What to save:** `{v=1, seed, size, mode, elapsedMs, ...}` plus the **dug-set**. Blocks come from the seed, so only
  dug cells need saving. Use a 1-bit-per-cell bitset (125,000 bytes for 100³), then zstd, then base64. A typical dug set
  (≤10% dug, clustered tunnels) should compress to **a few KB to tens of KB**. [EST] The worst case is uncompressed
  125 KB → 167 KB base64, still 4% of the limit. Even the raw 1 MB byte grid, base64'd, is 1.33 MB and fits.
- **Frequency:** save on leave plus `BindToClose`, autosave every 60–120 s if dirty, and on finish. Use session locking
  (ProfileStore or `UpdateAsync` with a lock field) so a teleport or rejoin can't overwrite newer data.

---

## 7. Leaderboards

- **OrderedDataStore:** values must be **integers**. `GetSortedAsync` page size defaults to 50, max **100**. No
  versioning or metadata. [DOC] https://create.roblox.com/docs/reference/engine/classes/OrderedDataStore.md
  Budgets per server per minute: OrderedWrite **30 + 5 × players**, OrderedRead 60 + 40 × players, **GetSorted (list)
  5 + 2 × players**. Experience-wide budgets also apply. [DOC limits page] There's no "rank of player X" call.
- **Times:** store as **integer milliseconds**, read with `ascending = true`. Write only on improvement (`UpdateAsync`
  with a compare).
- **Key design (one OrderedDataStore per board, key = tostring(userId)):**
  `LB1_{size}_{mode}_{diff}_{period}` where period is `A` (all-time), `D20261026`, `W2026-44` (ISO week), or
  `M202610`, e.g. `LB1_S_box_N_D20261026`. Names stay ≤50 chars. [DOC: 50-char names and keys]
  **Reset is automatic:** a new day or week means a new store name. Old stores just age out, so no deletes are needed.
  4 sizes × 3 modes × 2 difficulties × 4 periods = 96 boards, but each finish writes only **4** (its own combination ×
  4 periods) = well inside 30 + 5 × 8 = 70 writes/min.
- **Reading many boards:** the GetSorted budget is tiny (5 + 2 × 8 = 21/min). **Never let clients trigger reads.** A
  server job refreshes boards round-robin (e.g. the 1–3 visible ones every 60 s), caches the top 100, and pushes to
  clients. For cross-server freshness, cache board snapshots in MemoryStore (one HashMap key per board, refreshed by
  whichever server holds a "refresh lock").
- **MemoryStore SortedMap for "today" (and Daily Cube):** `SetAsync(userId, {name, ms}, expiration, sortKey = ms)`.
  `GetRangeAsync(Ascending, ≤200)`. Expiration max is 45 days, so set ~2 days for daily. Up to 1M items and 100 MB
  per map, values ≤32 KB. Game-wide quotas: memory **64 KB + 1.2 KB × users**, requests **1000 + 120 × CCU per
  minute**, ~30k units/min per partition. No rank call. [DOC]
  https://create.roblox.com/docs/en-us/cloud-services/memory-stores.md ·
  https://create.roblox.com/docs/reference/engine/classes/MemoryStoreSortedMap.md
  Use MemoryStore for **live "today" boards**, with fast and frequent reads. Keep ODS as the durable record (all-time,
  week, month, and day archives).

---

## 8. How "Search For The Needle" does multiplayer

- Universe **10756011174**: "[IMPOSSIBLE 😈] Search For The Needle" by **Garage Games** (group 279288859). Created
  **Aug 23, 2026**, **117.5M visits**, ~7.9K playing at research time, **MaxPlayers 20**. [Roblox API]
  https://games.roblox.com/v1/games?universeIds=10756011174
- The universe has **6 places**: the lobby (root), **Chapter 1 (FARMHOUSE)**, **Chapter 2 (BASEMENT)**, Chapter 3,
  Chapter 5, and GRAVEYARD. [Roblox API] https://develop.roblox.com/v1/universes/10756011174/places
- Guides: the lobby has "multiple game queues. Pick solo or join other players, then step into the designated circle to
  start" (https://games.gg/roblox/guides/search-for-the-needle-beginners-guide/). "Create a party for FARMHOUSE on
  NORMAL and teleport in" (https://allthings.how/search-for-the-needle-how-to-find-the-needle-fast-in-roblox/). Party
  size 1 "keeps a private pile to yourself", and a team of four "can strip the stack far faster"
  (https://allthings.how/search-for-the-needle-how-to-win-fast-roblox/).
- **Conclusion [EST, inferred from the place list plus guides, not confirmed by the developer]:** Needle uses a **lobby
  plus a teleport to a per-party chapter server** (almost certainly reserved servers). **The haystack is shared within a
  party and private per party.** It does **not** overlay several private piles in one space. Your "shared space, private
  cubes, ghosts" idea is a real differentiator: lobby energy without queues or teleports.

---

## RECOMMENDED ARCHITECTURE

1. **One place, MaxPlayers 8 (up to 12), one cube origin.** Every player's (or party's) cube is drawn at the same world
   position. The server Workspace holds **no collidable geometry** in or on the cube volume. Each client renders its
   own cube, which is also what it sees from the hub. Spawn players on the top face, and have the client confirm that
   face is built first.
2. **Server truth:** one `buffer` per active cube (1 byte per cell; 1 MB at 100³, ~2 MB at 126³), generated from
   `seed`. Parties share one buffer. Solo players own one each. 8 cubes ≈ 8–16 MB of server memory.
3. **Client rendering:** the client keeps its own copy of *its* cube's buffer and renders it as **anchored Parts from 3D
   greedy box merging per 20³ chunk** (125 chunks; an untouched cube ≈125 parts). Re-mesh only the touched chunk, at
   most one chunk per frame, with a frame budget of ≤4 ms on mobile. Settings: CastShadow off, CanTouch off, CanQuery
   off, CollisionGroup `Blocks`. Use a part pool plus `BulkMoveTo`. Use one MaterialVariant per depth band (verify
   4-stud alignment, else per-air-face Textures). Budget: ≤3k block parts on mobile.
4. **Digging:** use a client-side **grid DDA raycast** from the camera (no physics raycasts). Predict instantly, then
   batch indices into a `buffer` and send it over a reliable RemoteEvent every 100 ms. The server validates each dig
   (exposed, reach, rate, solid) in O(1), applies it, and echoes corrections. Party members get the confirmed digs
   reliably and apply them to their copy.
5. **Ghosts:** in Studio, register the groups `Players`, `Blocks` and `Ghosts`. Players↔Players off, Players↔Blocks on,
   Ghosts↔all off. The server assigns `Players`. Each client locally sets other characters to `Ghosts` and
   `LocalTransparencyModifier` 0.5, and adds **one Highlight per other character** (`AlwaysOnTop`, faint fill; the limit
   is 255, which is plenty), plus an AlwaysOnTop BillboardGui name and dot, hidden past ~200 studs.
6. **Shared "big effects":** clients send effects to the server, and the server rebroadcasts `{userId, effectId,
   cellIndex, radius}` over **UnreliableRemoteEvent** (≤1000 B). Other clients play VFX and SFX only. They never touch
   their grid.
7. **Spawning and safety:** `CharacterAutoLoads = false`. Spawn after the client signals "spawn area meshed". Every
   server teleport picks a **grid-safe cell** from that player's buffer. Keep `AuthorityMode` on the default (not
   Server). Keep StreamingEnabled off (small map), or verify that local parts survive it.
8. **Anti-cheat:** at 10 Hz, check root position vs **that player's grid** (footprint in solid > 0.75 s means a
   violation), plus a DDA path check between samples, a speed cap, and the dig token bucket. Do a soft rollback, then
   kick. Counters are per player.
9. **Persistence:** save `seed + meta + zstd(bitset of dug cells) → base64` per active cube (typically KB, worst case
   167 KB at 100³). Save on leave, `BindToClose`, every 90 s when dirty, and on finish, with ProfileStore-style session
   locks. Stay far below 4 MB per key and 4 MB/min per key.
10. **Leaderboards:** one OrderedDataStore per board, `LB1_{size}_{mode}_{diff}_{A|Dyyyymmdd|Wyyyy-ww|Myyyymm}`,
    key = userId, value = integer ms, read ascending. Writes happen only on improvement (4 writes per finish). A server
    cache refreshes visible boards round-robin within `5 + 2 × players` GetSorted calls per minute. A **MemoryStore
    SortedMap** holds "Today" and the Daily Cube (sortKey = ms, 2-day expiry, top 200 reads).
11. **Fallbacks (only if M1 perf tests fail on a low-end phone):** (a) hide chunks more than N chunks from the player;
    (b) bigger merge boxes for long-untouched regions; (c) client-local Terrain as a smooth-cave skin, with
    StreamingEnabled off and staff caveats accepted. **Don't use EditableMesh** while the ID-verify gate, memory nil
    returns and collision rebuilds remain.
12. **M1 proof tests:** a random-dig correctness test (box set == grid, no overlap); mesh ms per chunk on PC and a
    low-end Android; part count after 20k and 100k digs; 8 bots digging at 30/s for server CPU; a noclip test with 250
    ms latency.
