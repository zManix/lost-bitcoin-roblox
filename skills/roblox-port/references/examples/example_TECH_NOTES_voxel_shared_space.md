# TECH NOTES: cube engine, shared space, networking, persistence, leaderboards

Source: a research pass on 2026-10-26 (Roblox docs, staff posts, community).
- **[DOC]** official docs
- **[EST]** estimate
- **[TEST]** prove it in Studio before relying on it

## 1. Architecture (do exactly this; prove it in milestone M2 before building anything on top)
1. **One place, one cube position.** MaxPlayers 10. Every cube is rendered at the SAME world position. The server
   has NO collidable geometry there. Set `Players.CharacterAutoLoads = false`; spawn a character only after its
   client reports that its top face is built.
2. **Server truth:** one `buffer` per active cube, built from the seed, 1 byte per cell.
   - Cell values: 0 air, 1–5 band, 10+ special, 99 box.
   - Size: 100³ = 1 MB; 126³ ≈ 2 MB.
   - A party shares one buffer.
   - Note [DOC]: `buffer` max is 1 GiB, and it is copied when sent across remotes or Actors.
3. **Client rendering:** anchored Parts from **3D greedy BOX merging** of SOLID cells.
   - Chunks: 20³ cells, so 125 chunks for a Standard cube. A chunk's boxes don't depend on its neighbors.
   - An untouched cube is about 125 parts.
   - After a dig, re-mesh only the touched chunk, at most one chunk per frame (queue the rest).
   - Part settings: Anchored; CastShadow, CanTouch and CanQuery off; CollisionGroup "Blocks". Pool the parts and move
     them with `workspace:BulkMoveTo`.
   - Budget: ≤ 3,000 block parts on phones [EST]. Fallbacks if phone tests fail: hide chunks beyond 160 studs,
     re-merge old dug regions.
   - **Look on merged boxes:**
     - PRIMARY: one MaterialVariant per band, StudsPerTile 16, using a 1024² image of a 4×4 block grid with the seams
       and the ±6% per-block variation baked in. MaterialVariants batch; Texture instances don't.
     - FALLBACK if tiling doesn't line up across merged boxes [TEST]: Texture instances on air-facing faces only,
       StudsPerTileU/V 16, with OffsetStudsU/V from the world position.
     - Lamps are tiny separate parts (a disc + a PointLight) placed on air-facing faces of seeded "lamp cells".
4. **Digging:**
   - The client aims with a DDA ray through ITS OWN GRID (not a physics raycast) and removes the block locally at once.
   - It sends dig cell indices in batches every 100 ms over a reliable RemoteEvent (3 bytes per cell).
   - The server validates each one: the cell is solid, touches air (or is a spell-area cell), is within reach of the
     server-known position, and is within the rate limit. It applies the change to the buffer and sends a correction
     (re-solidify) when it rejects one.
   - Spells send one cast message; the server computes the affected cells deterministically and sends back the
     authoritative list.
5. **Ghosts (other players):**
   - Register CollisionGroups in Studio: `Players` (doesn't collide with Players), `Blocks` (collides with Players),
     `Ghosts` (collides with nothing). Only the server/Studio can set group rules.
   - The server puts every character in `Players`.
   - Each client locally sets OTHER characters' parts to the `Ghosts` group and `LocalTransparencyModifier = 0.5`, adds
     one `Highlight` (DepthMode AlwaysOnTop, soft fill in the aura color, outline 0.3). The limit is 255 per client
     [DOC]; the first one costs the most GPU.
   - Add a BillboardGui name tag (AlwaysOnTop, fades in within 30 studs).
6. **Shared big effects:** the server re-broadcasts small effect messages over an UnreliableRemoteEvent
   (payloads ≤ 1,000 bytes or they are dropped [DOC]): box-found column, legendary sparkle, geode spray, emote,
   race events. Other clients only play visuals/sound and NEVER touch their own grid.
7. **Safety:**
   - Every server-side teleport chooses a safe air cell from that player's grid.
   - Keep `Workspace.AuthorityMode` at default. Server-authority physics would roll players back because the server
     has no walls [inference].
   - StreamingEnabled: client-created parts may behave differently. Either turn StreamingEnabled OFF (the Hall is
     small; the cube is client-only) or prove that client parts survive streaming [TEST]. Recommended: OFF.
8. **Anti-noclip:**
   - 10 times a second, test the character's footprint against that player's grid (plus sweep the path between
     samples).
   - Flag > 0.75 s inside solid cells; cap speed by the player's movement build.
   - Respond with a soft rollback to the last safe cell; kick on repeats. Keep counters per player.
9. **Persistence:**
   - Format: seed + metadata + a 1-bit-per-cell dug bitset → `EncodingService` zstd → base64 → its own DataStore key
     (`cube_{userId}_{size}`).
   - Worst case about 167 KB vs the 4,194,304-character limit [DOC].
   - Save on leave, BindToClose, every 90 s if changed, and on finish; use the session lock (reuse DataService).
10. **Leaderboards:**
    - One OrderedDataStore per board, named `LB1_{goal}_{size}_{diff}_{upg}_{grp}_{A|Dyyyymmdd|Wyyyy-ww|Myyyymm}`.
    - key = userId, value = integer milliseconds, sorted ascending.
    - A new period = a new name, so there are no deletes. On finish, write only on improvement.
    - Budget [DOC]: writes 30 + 5×players per minute; list reads only 5 + 2×players per minute per server. So the
      server refreshes boards on a timer (every 60–120 s, round-robin) and caches them; clients never trigger reads.
    - MemoryStore sorted maps for the live "Today", Daily and Live Race boards (fast); ODS for week/month/all-time.
11. **Tests in M2 (must pass before M3):**
    - CubeTest: mesh = grid on 1,000 random dig patterns; no holes or overlaps.
    - Measure ms per chunk re-mesh on emulated phone (target ≤ 4 ms).
    - Part count after 20k and 100k digs (≤ 3,000 visible).
    - 8 bot clients digging at 30 per second (server CPU, bandwidth).
    - A noclip test at 250 ms simulated latency.

## 2. Key limits
| What | Limit |
|---|---|
| Highlight per client | 255 [DOC] |
| UnreliableRemoteEvent payload | ≤ 1,000 bytes [DOC]; remotes ~500 calls/s per client |
| DataStore value | 4,194,304 chars [DOC]; Get/Set budget 60 + 40×players per minute |
| OrderedDataStore | integers only; ≤ 100 per page; writes 30 + 5×players/min; list reads 5 + 2×players/min |
| MemoryStore | memory 64 KB + 1.2 KB × users; requests 1,000 + 120×players/min; sorted map reads ≤ 200 items; values ≤ 32 KB |
| Parts on phones | about 13K OK, 15–20K hurts (community); our target ≤ 3,000 block parts |
| EditableMesh | requires an ID-verified 13+ owner, has memory-budget failures and doesn't replicate. Do NOT use |
| Client-created Terrain | staff say avoid; it's smooth, not blocky. Do NOT use |

## 3. Search For The Needle (for context)
It uses a lobby plus chapter places and teleports a party into its own server ("a private pile to yourself"). It does
NOT overlay private piles in one space. Our shared-space ghosts are a genuine difference.
