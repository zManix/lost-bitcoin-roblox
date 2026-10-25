````
# ONE-SHOT BUILD PROMPT — "HAUL & HATCH" (Roblox)

You are a senior Roblox engineer + technical artist. Build a complete, polished Roblox game called HAUL & HATCH in
Roblox Studio, end to end, from this document alone. You have never seen any earlier conversation; everything you need
is here. Work through the whole spec without stopping to ask. Only stop for: a login, a payment, a CAPTCHA, the
image-approval gate (B2), or a decision that truly belongs to the owner. Where something is unspecified, pick the
sensible default, log it as [ASSUMPTION] in the BuildLog, and keep going.

WHY THIS DESIGN (so you protect what matters when you make trade-offs)
- Every pillar is copied from live, proven Roblox hits: creature hatching with rarity/Secret/mutations (Steal An Egg),
  creatures earning on your plot incl. offline (Steal a Brainrot / Grow a Garden), your collectible IS your progression
  (Ride a Pet / Ride a Dino), throwing junk into a fire (Feed the Fire), a risky run against a sweeping hazard (Escape
  Tsunami), a restock clock (Grow a Garden), co-op carry (carry obbies in Roblox's "Fun with Friends" chart, R.E.P.O.).
- The ONE new thing is TEAM CARRY: big junk clumps are too heavy for one player; friends lift together; bigger clump =
  rarer hatch; EVERY carrier gets their own hatch. Protect this feeling above everything: smooth, funny, readable.
- Roblox ranks on: first-minute bounce, 28-day retention, days played, playtime, co-play days. Low-end phone crashes
  count as bounces. 80% of players are on mobile. Design and test for that.

====================================================================================================
## A. YOUR ENVIRONMENT (given)
====================================================================================================
- Claude Code on Windows.
- Roblox Studio MCP tools: list_roblox_studios, execute_luau, multi_edit, script_read, start_stop_play, screen_capture,
  input simulation, insert_asset, generate_mesh, upload_image. Pass studio_id on EVERY call.
  Another Studio may be open. Lock onto the right place:
    1) list_roblox_studios  2) in the place you build: workspace:SetAttribute("HaulAndHatchAgent", true)
    3) before every batch of work probe: return workspace:GetAttribute("HaulAndHatchAgent")  → must be true.
  If it is not true you are in the wrong Studio: re-list and re-lock. NEVER edit, run or screenshot another Studio.
- Blender MCP for all 3D models: chunky, low-poly, stylized. Export FBX. Upload through the Roblox Open Cloud Assets
  API (API key + user/group ID are in the owner's env vars or memory notes, e.g. ROBLOX_OPEN_CLOUD_KEY,
  ROBLOX_USER_ID / ROBLOX_GROUP_ID). Insert the uploaded MeshParts. Use REAL uploaded meshes; never runtime
  EditableMesh (it renders as boxes in live games).
- Images: Vertex AI with the newest Gemini image model available. POSITIVE-ONLY prompts: describe exactly what you
  want to see; never list things to avoid.

====================================================================================================
## B. HARD RULES
====================================================================================================
B1 Content safety (strict moderation): no skulls, blood, gore, robed or hooded figures, religious symbols, weapons
   aimed at people, text inside images, real brands/logos, real currencies or crypto symbols. Nothing scary for kids:
   the Crusher is a cartoon magnet crane, ragdolls are bouncy and funny.
B2 Image gate: every 2D image is saved first to pending_review\ with a .txt (prompt + intended use). STOP and wait for
   the owner's OK before uploading. Batch images to ask rarely; keep building with grey placeholders while waiting.
B3 Quality loop: small steps. After EACH step: smoke test → start_stop_play playtest → screen_capture → inspect → fix.
   Never stack untested work.
B4 Smoke test: ServerScriptService/Tests/SmokeTest (run via execute_luau). Requires every ModuleScript, checks every
   remote exists, validates Config (no nil, no negative costs, every cost curve strictly increasing, every odds table
   sums to exactly 100, every unlock reachable), confirms DataStore TEST mode in Studio, ticks every service once with a
   fake player, prints "SMOKE PASS n/n" or each failure. Run after every change. 0 failures before moving on.
B5 Platforms: test Phone 20:9 (800x360), Phone 16:9 (640x360), Tablet (1024x768), Console (1920x1080, 10-foot UI),
   PC (1920x1080 and 1366x768). Use Studio device emulation if you can drive it; otherwise the overlap checker's
   "virtual viewport" mode (parent the HUD into a Frame of each target size and measure).
B6 UI overlap check: StarterPlayerScripts/Dev/OverlapCheck. Every visible GuiObject vs every other (skip parent/child and
   tooltips) and vs reserved zones: Roblox top bar (GuiService.TopbarInset), chat, mobile thumbstick (bottom-left),
   jump button (bottom-right). Must be 0 overlaps on all devices. Every touch target ≥ 44 px.
B7 Performance: StreamingEnabled ON (StreamOutBehavior Opportunistic). Reuse meshes (same MeshId). Budgets in C14.
   Adaptive quality controller (C14). Must run smooth on 2 GB Android phones.
B8 Data: DataStore with session locking (UpdateAsync lock = JobId + timestamp, steal after 30 min stale), autosave every
   90 s + on leave + BindToClose, retries with exponential backoff (5 tries), data version + migrations. In Studio ALWAYS
   use "HNH_TEST_v1". The live store "HNH_LIVE_v1" is only used when not RunService:IsStudio(). Never touch live data
   while testing.
B9 Server authority: server owns cash, Scrapkins, upgrades, purchases, carry state, hatch rolls. Client only asks.
   Every remote: type checks, distance/ownership checks, per-player token-bucket rate limits, log + ignore bad requests
   (kick only on repeated clear abuse). Purchases through MarketplaceService.ProcessReceipt with a saved receipt ledger.
B10 Logging: ServerStorage/BuildLog (timestamped entries: step, result, assumptions). MORNING_REPORT.md in the project
   folder: done / broken / next / all [ASSUMPTION]s. Mirror EVERY script to a local live_src\ folder (same tree, .lua)
   after every edit.
B11 Don't publish. Don't create passes/products on the website; put placeholder IDs in Config and list what the owner
   must create. At the end tell the owner exactly: "SAVE NOW (Ctrl+S) + PUBLISH".
B12 Loop: keep going through every milestone until the hand-off checklist (E) is all green.

====================================================================================================
## C. GAME SPEC
====================================================================================================

### C1 Name, pitch, fantasy
- HAUL & HATCH. Pitch: "Team up to haul giant junk clumps into the Big Furnace. The fire burns the junk away and a
  Scrapkin hatches out. Bigger clump = rarer Scrapkin = more friends needed. Everyone who carried gets one!"
- SCRAPKINS: cute little creatures that live inside junk. Built from a round soft body + junk parts (a bottle-cap hat,
  a spring tail, a teacup body, button eyes). Big friendly eyes, waddle walk, squeaky voices.
- Guide character: GUS, a big gentle furnace-keeper bear in overalls and a hard hat (no hood). Short speech bubbles,
  max 8 words.
- Iconic Secret Scrapkin: GOLDEN BYTE, a tiny golden memory-stick critter with a glowing smile.

### C2 Art direction
- Chunky low-poly, toy-like, soft bevels, oversized props. Junk is colorful and cheerful.
- Palette (Config.Colors): Sunset haze #E9A65B | Deep shadow #3B2A22 | Rust #B5532B | Teal #4FA39A | Cream #F2E3C2 |
  Furnace glow #FF8A1F | Coin gold #FFC83D | UI panel #1E1A17 (92%) | UI accent #FF9A2E | Bought green #5BD16B |
  Locked grey #6E6A66. Rarity colors: Common #CFCFCF, Uncommon #6BD36B, Rare #4DA3FF, Epic #B06BFF, Legendary #FFC83D,
  Mythic #FF5FA2, Secret = animated rainbow gradient.
- Lighting: Future (ShadowMap on Low). ClockTime 17.2. Atmosphere Density 0.35, Haze 2, Color #E9A65B, Decay #8A5A3A.
  ColorCorrection warm (+0.05 sat, tint #FFF1DE). Bloom 0.6 / threshold 1.4. The furnace is the brightest thing.
- Camera: third-person, max zoom 22; slight zoom-out while carrying big clumps; small kick when a clump drops in.
- Music: chill funky "junkyard groove"; tense percussion layer during Crusher warnings; triumphant brass sting on
  Epic+ hatches; big fanfare for Secret. Use free Creator Store audio (insert_asset). [ASSUMPTION]
- SFX: lift grunt (cartoon), heavy footstep thuds scaled by clump weight, furnace whoomph, rising "reveal" tone per
  flame color step, Scrapkin squeak pop, coin clinks, Crusher siren + magnet hum + boing ragdoll, train horn, UI clicks.

### C3 World layout (one place, server MaxPlayers 8)
- CENTER: the PLAZA with the BIG FURNACE (huge cute furnace with a wide glowing mouth and a ramp; Gus stands beside it).
  A DROP ZONE ring (radius 14 studs) around the mouth: any carried clump inside it can be dropped in.
- Around the plaza: THE HEAP, 4 concentric RINGS of junk terrain (hills, pits, tunnels made of piled junk props on a
  Terrain base). Ring gates unlock by Rebirth: R1 Toybox Yard (start), R2 Kitchen Tip, R3 Garage Gulch, R4 Tech Canyon.
  Further rings = bigger clumps = rarer odds = longer carry = more Crusher risk.
- Outer edge: 8 PLAYER PLOTS (the "Pad Terrace"), each with Scrapkin pads, a Collect plate, a sign with the owner's
  name + display name, and a short bridge back to the plaza. Players can visit any plot.
- RAIL LINE around the Heap: the Junk Train arrives here (C9).
- No death, no fall damage, no lost items, ever.

### C4 Core loop
- Seconds: spot a glowing clump → tap LIFT → (friends tap LIFT on it too) → walk it to the furnace while the Crusher
  rumbles → DROP IN → flame climbs white→blue→purple→gold→rainbow → a Scrapkin pops out → it hops to your plot.
- Minutes: Scrapkins on pads earn cash every second → tap Collect → buy Strength / Speed / Backpack / Luck / Pads →
  lift bigger clumps → rarer Scrapkins. Equip your best Scrapkin as FOLLOWER: it adds lifting strength.
- Session: fill the Index, catch a Titan Clump event with the server, ride Golden Trains, Rebirth into the next ring.
- Week: daily streak + quests, Saturday update + Admin Junk Rain with limited Scrapkins that leave the pool.

### C5 Clumps & team carry (Config.Clumps) — THE CORE, build it first and make it feel great
| Size | Weight kg | Rings | Note |
|---|---|---|---|
| Pebble | 8 | R1–R4 | goes in the Backpack (slots), carry several |
| Lump | 20 | R1–R4 | solo from minute 1 |
| Chunk | 60 | R1–R4 | strong solo or 2 players |
| Boulder | 150 | R2–R4 | 2–3 players, or a strong solo + good follower |
| Mega | 400 | R3–R4 | 3–4 players |
| Titan | event | plaza | needs the server (C10) |
- Ring multiplier on weight: R1 ×1, R2 ×1.5, R3 ×2.2, R4 ×3.2 (with matching value multipliers in C7).
- Strength: base 25 kg (+ upgrades + follower bonus + boosts). Team strength = sum of carriers.
- Lift rule: ratio = teamStrength / weight. ratio < 0.6 → cannot lift; show "Needs 1–2 more lifters or +X kg".
  0.6–1.0 → speed = 40%→100% of walk speed (linear). ≥1.0 → 100% (cap 110% at ratio ≥ 1.25).
- Up to 4 carriers per clump (anchor points around it). Each carrier must contribute ≥ 15% of the required lift and be
  holding for ≥ 50% of the carry to earn a hatch ("Helping ✓" tag above their head). AFK > 10 s auto-drops them.
- CARRY IMPLEMENTATION (do this exactly; prototype in M1 and test 4 clients on emulated phones):
  * The clump is a model with an anchored root controlled by the SERVER. No unanchored physics, no client network
    ownership. Each carrier character gets an AlignPosition/AlignOrientation (client-owned) pulling them to their anchor
    point beside the clump, so their own character stays responsive.
  * Server tick (20 Hz): target = average of carriers' requested move vectors (from their Humanoid MoveDirection sent
    via an unreliable remote at ≤ 15 Hz), weighted by each carrier's strength; move the clump root by
    speed × dt along it, clamp to walkable ground via a downward raycast, collide by spherecast. Replicate the root
    CFrame; clients interpolate (render-step lerp, 100 ms buffer) so it looks smooth.
  * Anti-exploit: server ignores move vectors > length 1, caps speed, rejects joins from > 8 studs away, and checks the
    clump never moves more than maxSpeed × dt per tick.
  * Carry animation: arms-up lift pose, wobble on the clump (spring), sweat-drop particles when ratio < 0.8.
- Mobile: when near a clump a big LIFT button appears (bottom-right arc, above jump). While carrying: LET GO button;
  near the furnace: big DROP IN button (pulsing). PC: E lift / E drop in / Q let go. Console: X lift / X drop / B let go.
- Griefing guards: the clump moves with the strength-weighted majority; anyone can let go; joining a clump never takes
  anything from anyone (everyone gets their own hatch), so there is nothing to steal.

### C6 Hatching (Config.HatchOdds) — the reveal must feel amazing
- DROP IN → clump slides into the mouth → 2.5 s reveal: furnace shakes, flame color steps up through rarity colors and
  STOPS at the result (each step: pitch-rising tone + spark burst; Epic+ adds screen glow + small shake) → the Scrapkin
  pops out with squash-and-stretch, confetti in its rarity color, a name card (name, rarity, mutations, income/s), then
  waddles/hops toward the owner's plot (and is placed on a free pad; if none free → into Storage, toast).
- Each eligible carrier rolls separately and sees their own reveal on their screen; everyone sees the flames.
- Base odds by size (%, must sum to 100): Common / Uncommon / Rare / Epic / Legendary / Mythic / Secret
  Pebble 70 / 22 / 7 / 0.9 / 0.09 / 0.01 / 0
  Lump 55 / 28 / 13 / 3.5 / 0.45 / 0.05 / 0
  Chunk 40 / 32 / 19 / 7 / 1.7 / 0.29 / 0.01
  Boulder 25 / 32 / 26 / 12 / 4 / 0.9 / 0.1
  Mega 10 / 25 / 32 / 21 / 9 / 2.6 / 0.4
  Titan 0 / 0 / 40 / 35 / 18 / 6 / 1
- Glow (visible on clumps: none / sparkle / aura / beam = 0–3): multiplies Rare+ weights by (1 + 0.5 × glow), then
  renormalize. Furnace Luck upgrade: +5% Rare+ weights per level. Luck boosts: ×2 Epic+ weights. ALWAYS renormalize and
  show the FINAL odds.
- HATCH ODDS CARD: when you look at / are near a clump, a small card shows size, weight, lifters needed and the exact
  final % per rarity for YOU (with your luck). Also shown inside the store before any luck purchase.
- Mutations (rolled independently): Size Tiny 10% (×0.8) / Normal 80% / Big 8.5% (×1.5) / HUGE 1.5% (×5; model scale ×2);
  Paint none 94.5% / Golden 5% (×3) / Rainbow 0.5% (×10). Golden Train: Golden 15%. Secret hatch = server-wide banner.

### C7 Scrapkins (Config.Scrapkins)
- Launch roster: 10 per ring × 4 rings + 2 Secrets (GOLDEN BYTE, DISCO DUMPSTER) = 42.
  R1 Toybox: Ducky Bop, Teddy Patch, Yo-Yo Pup, Block Bunny, Kite Moth, Marble Mouse, Robo Roo, Drum Bug, Sock Snail, Top Spin.
  R2 Kitchen: Toaster Pup, Kettle Frog, Spatula Crab, Mixer Mole, Cup Cub, Jar Jelly, Whisk Kitty, Pan Penguin, Fork Fox, Teapot Tortoise.
  R3 Garage: Tire Turtle, Spanner Snake, Bolt Bat, Hubcap Hedgehog, Oilcan Owl, Jack Jackal, Plug Pig, Chain Chameleon, Gear Goat, Muffler Monkey.
  R4 Tech: Monitor Moth, Cable Cat, Chip Chick, Mouse Mouse, Remote Raccoon, Speaker Seal, Pixel Pup, Antenna Ant, Battery Bear, Router Rhino.
  Each ring's 10 are assigned rarities Common×3, Uncommon×2, Rare×2, Epic, Legendary, Mythic.
- Income/s by rarity: Common 1, Uncommon 4, Rare 15, Epic 60, Legendary 250, Mythic 1,200, Secret 6,000;
  × ring value (R1 ×1, R2 ×4, R3 ×16, R4 ×64) × mutations × (1 + 0.25 × rebirths) × boosts.
- Follower strength bonus by rarity: 5 / 10 / 20 / 40 / 80 / 160 / 320 kg (× size mutation multiplier).
- Pads: start 6, upgrade +2 per level to 40. Cash accumulates on each pad (floating counter). Step on the Collect plate
  (or tap Collect within your plot) to bank it. Offline: 50% for up to 2 h (8 h with Night Shift pass).
- Sell a Scrapkin: 30 × its income/s. Storage holds 50 (expand later).
- Index (collection book): silhouette until hatched; tracks mutations seen. Every 10 new discoveries → reward
  (cash, Luck potion, cosmetic pad skin). Completing a ring set → permanent +5% income.

### C8 Upgrades (Config.Upgrades) — cost(level) = round(base × growth^(level-1)); always show "now → next"
| Upgrade | Max | Base | Growth | Effect |
|---|---|---|---|---|
| Strength | 25 | 50 | 1.45 | +10 kg/lvl |
| Walk Speed | 10 | 40 | 1.5 | 16 → +1/lvl |
| Backpack | 8 | 75 | 1.7 | Pebble slots 1 → +1/lvl |
| Furnace Luck | 10 | 500 | 1.8 | +5% Rare+ weights/lvl |
| Pad Slots | 17 | 200 | 1.6 | +2 pads/lvl (6 → 40) |
| Collector Range | 5 | 300 | 1.9 | collect from further away |
| Glow Scanner | 3 | 1,000 | 3.0 | see clump glow through junk at 30/60/90 studs |
- REBIRTH (Gus's "Bigger Furnace"): needs cash 25,000 × 4^rebirths and ≥ 6 Index entries from your current ring.
  Resets cash + all upgrade levels. KEEPS Scrapkins, Index, follower, cosmetics, passes. Gives +25% income (stacks) and
  unlocks the next ring. Show a "You keep / You reset / You gain" screen before confirming.

### C9 Clocks (keep it to these)
- JUNK TRAIN every 5 min (server-local): horn, train rolls around the rail, cranes drop fresh clumps to refill each ring
  to its target density (R1 40, R2 30, R3 22, R4 16 clumps). 10% chance it's a GOLDEN TRAIN (all new clumps +1 glow,
  Golden paint 15%). Top-center timer chip.
- CRUSHER SWEEP every 4 min (server-local): 20 s siren + red sector lights + a big cartoon magnet crane swings over ONE
  outer sector (R2+, never R1) for 8 s. Players caught are ragdolled for 2 s (bouncy, funny, no damage) and drop what
  they carry; clumps stay where they fall. New players get a 3-minute "Shielded" bubble (visible) after joining.
- TITAN CLUMP every 20 min when ≥ 1 player has hatched ≥ 3 Scrapkins (C10).
- Saturday ADMIN JUNK RAIN (global via MessagingService at a fixed UTC time from Config; testable with a Studio-only
  trigger): 30 min of junk raining from the sky, ×3 luck, limited-time Scrapkins that leave the pool afterwards.

### C10 Titan Clump (the server moment)
- A giant glowing clump crashes into the plaza edge (camera shake for everyone, banner "TITAN CLUMP! Everyone lift!").
- Required lift = max(150, 110 × playersInServer) kg, shown live on it ("320 / 440 kg"). Up to 8 carriers.
- 90 s to get it into the furnace. Every helper gets a Titan hatch roll (Rare+ guaranteed). If time runs out it
  crumbles into 6 Chunks (no one loses anything). Solo servers can do it because the requirement scales.

### C11 Onboarding (first 60 s fun, no wall of text) — funnel-log each step (AnalyticsService:LogOnboardingFunnelStepEvent)
- 0–5 s: spawn on the plaza next to the furnace; Gus waves: "Lift that glowing lump!" A guaranteed sparkly LUMP sits
  2 studs away with a bouncing arrow; the LIFT button pulses.
- 5–20 s: lift → walk 10 studs → DROP IN pulses → reveal → a guaranteed Uncommon pops out → hops to your plot
  (camera follows it briefly) → "+4/s!" Your plot glows.
- 20–40 s: Gus: "Collect your cash!" → Collect → buy Strength (50) — first upgrade < 40 s.
- 40–90 s: Gus points at a CHUNK: "Too heavy? Grab a friend!" with an Invite button (SocialService:PromptGameInvite)
  and a "Lift with someone" hint arrow to the nearest player; solo players see "or get stronger!" → Strength.
- ~3 min: equip a follower ("Your Scrapkin helps you lift!"). ~5 min: first Junk Train. Tutorial skippable in Settings;
  steps auto-skip if already done.

### C12 Controls (ContextActionService; hints swap on LastInputType)
- PC: WASD, E lift/drop in, Q let go, F collect (on plot), Tab index, B shop, 1–3 quick slots.
- Mobile: thumbstick; LIFT / DROP IN / LET GO context button (big, bottom-right arc above jump); Collect button on plot;
  Shop/Index/Store buttons top-right column. Soft auto-target: LIFT targets the nearest clump in a 30° cone.
- Console: X lift/drop, B let go, Y shop, LB/RB menus, D-pad UI; full GuiService selection with an orange outline.

### C13 UI (scale-based with UIAspectRatioConstraint + UISizeConstraint)
- HUD: cash (top-left under topbar inset) with "+n" fly-in; strength chip "Strength 85 kg (+20 follower)"; Train and
  Crusher timer chips (top-center); carry panel while carrying (team strength / weight bar, speed %, lifters icons);
  context button; mini quest tracker (collapsible); Shop / Index / Store / Settings buttons.
- Screens: Hatch reveal card; Hatch Odds card; Shop (upgrades with "now → next"); Plot panel (pads, sell, storage,
  equip follower); Index; Rebirth (keep/reset/gain); Daily Rewards (7-day); Quests (3 daily + 2 weekly); Store
  (passes + products with exact effects, odds where relevant); Settings (music, SFX, graphics Auto/Low/High, reduced
  shake, skip tutorial); Welcome Back (offline cash); Toasts (max 3 stacked); Titan and Admin Rain banners.

### C14 Performance budgets + QualityController
- Junk props: anchored MeshParts from a pool of ~30 meshes, CanTouch off, CastShadow off when small, CollisionFidelity
  Box, streamed. Clumps: max 120 active per server. Scrapkins on pads: static meshes with a tiny tweened idle bob (no
  Humanoids); only followers walk (simple AlignPosition hop, no Humanoid). Max 1 follower rendered per player; other
  players' followers hidden beyond 60 studs on Low.
- Target: < 1,000 draw calls and < 1M triangles on screen; textures ≤ 512².
- QualityController: sample FPS every 2 s; < 40 → step down (shadows off on props, particle rates halved, fewer coin
  sprites, decoration fade distance shorter); > 55 for 10 s → step up. Settings can force Low/High.

### C15 Monetization (honest; Config.Monetization with placeholder IDs; prices from live comparable games)
Rules: show the exact effect before buying; no fake discounts or countdowns; NO paid hatches or paid random items;
luck boosts show the exact resulting odds and are hidden for players where PolicyService:GetPolicyInfoForPlayerAsync
says ArePaidRandomItemsRestricted; nothing gives power over another player (the game is co-op).
| Type | Name | R$ | Effect |
|---|---|---|---|
| Pass | 2x Cash | 249 | +100% Scrapkin income |
| Pass | VIP | 249 | +10% income, gold name tag, VIP pad skin, +1 daily quest reroll |
| Pass | Lucky Furnace | 199 | ×2 Epic+ weights (odds shown) |
| Pass | Super Strength | 199 | +50% strength |
| Pass | Big Plot | 199 | +10 pads |
| Pass | Night Shift | 149 | offline cap 2 h → 8 h |
| Pass | Auto Collect | 99 | pad cash banks automatically |
| Product | Luck Potion 15 min | 39 | ×2 Epic+ weights, 15 min (odds shown) |
| Product | Cash Potion 15 min | 29 | ×2 income, 15 min |
| Product | Strength Potion 15 min | 25 | +50% strength, 15 min |
| Product | Golden Train (server gift) | 99 | next train is Golden for the whole server; gifter's name shown |
| Product | Summon Titan (server gift) | 149 | spawns a Titan Clump now for everyone; gifter's name shown |
| Product | Cash Pack S / L | 49 / 149 | exactly 15 min / 1 h of your current income (shown before buying) |

### C16 Retention & social
- Daily: 7-day streak (cash → Luck Potion → Glow Scanner trial → Cash Potion → cosmetic → Strength Potion → Day 7 exclusive
  "Gus Plush" Scrapkin). Missing a day drops 2 days, not to zero. 3 daily quests (e.g. carry 5 clumps with a friend,
  hatch 10, catch a Golden Train, lift a Boulder) + 2 weekly; rewards scale with progress.
- Friend boost: +10% income per friend in server (cap +30%). Invite button. Referral: GetJoinData launch data from an
  invite link → both get a Luck Potion (once per pair).
- Group reward: join the group → free "Group Gremlin" Scrapkin (Uncommon, unique look); verify via
  Player:IsInGroup on join. Codes: Config.Codes list (e.g. "LIFTOFF").
- Show-off: Legendary+ hatches announce in server chat-style banner; visit any plot; "Best Scrapkin" pedestal on plot.
- Live ops scaffolding: Config.LiveEvents (scheduled UTC windows, multipliers, limited roster), a 60-character update
  note in Config.UpdateNote, and a Studio-only test command to fire any event.

### C17 Asset list
3D (Blender → FBX → Open Cloud → MeshPart), low-poly 200–1,500 tris, one shared palette atlas where possible:
- Junk props (30): tire, oil drum, crate, washing machine, fridge, bicycle, traffic cone, TV, car door, gear, jerrycan,
  pipes, spring, sofa, toaster, radio, kettle, lamp, shopping cart, chair, teddy, toy blocks, rubber duck, pots, pan,
  keyboard, monitor, cables, speaker, hubcap.
- Clumps: 6 size variants built as a rounded lump of fused junk (modular so ring themes can swap junk pieces); glow
  shells for glow 1–3.
- Scrapkins: 8 base bodies (round, bean, tall, flat, egg, box, blob, long) + 30 junk attachments; assemble the 42
  roster from these + palette; HUGE uses scale. Each with a simple idle bob/hop (tween-based).
- Big Furnace (mouth, ramp, chimney, flame planes), Gus (rigged, wave/point/cheer), Junk Train (engine + 4 cars), rail,
  Crusher magnet crane, plot pads, Collect plate, plot sign, bridges, plaza tiles, ring gates, lamp posts.
2D (Vertex → pending_review\ → OK → upload_image): MaterialVariant junk textures per ring ("seamless tileable texture
of tightly packed colorful cartoon junk pieces, warm sunset light, stylized low-poly game art, top-down view"); UI icons
(512², flat, centered object on a plain rounded dark background): cash, strength, luck, each upgrade, each pass, each
rarity gem, index, daily gift; game icon + 3 thumbnails ("a group of cheerful blocky kids lifting a giant glowing junk
clump toward a huge friendly furnace, a cute little creature popping out in a burst of rainbow sparks, golden-hour
junkyard, vivid warm colors, kids' game art") — scenes only, no lettering.

### C-TECH Architecture
ReplicatedStorage/Shared: Config, Remotes, Format (1.2K/3.4M), Odds (pure functions, unit-tested), Types, Signal.
ServerScriptService/Services: DataService, HeapService (rings, clump spawn/despawn, density), CarryService (C5),
FurnaceService (hatch rolls, reveal events), ScrapkinService (pads, income tick, offline, sell, storage, follower),
UpgradeService, RebirthService, TrainService, CrusherService, TitanService, IndexService, QuestService, DailyService,
SocialService (friend boost, referral, group, codes), MonetizationService (ProcessReceipt, passes, PolicyService),
LiveEventService, AntiExploit, Bootstrap.
ServerScriptService/Tests: SmokeTest, BalanceSim, OddsTest (100k rolls per table within ±0.2% of shown odds).
StarterPlayerScripts/Controllers: Input, Carry (interp + anims), Camera, HUD, Shop, Hatch (reveal), Plot, Index, Store,
Tutorial, Juice, Audio, Quality, Settings. Dev/OverlapCheck.
Remote rate limits (per second): CarryMove 15 (unreliable), Lift 4, LetGo 4, DropIn 2, Collect 4, BuyUpgrade 6,
Equip 3, Sell 4, Rebirth 1, ClaimDaily 1, ClaimQuest 2, Code 1, Settings 2.

====================================================================================================
## D. BUILD ORDER (log each milestone in BuildLog + MORNING_REPORT.md)
====================================================================================================
M0 Setup: lock Studio, folders, Config, Remotes, DataService (TEST), BuildLog, live_src\ mirror, SmokeTest, OddsTest.
   DONE WHEN: smoke passes; data loads/saves/locks across 2 test sessions; odds tables sum to 100.
M1 TEAM CARRY PROTOTYPE (greybox): clumps, lift rule, server-driven carry, client interpolation, let go, AFK drop.
   DONE WHEN: with Studio Test > 4 clients on emulated phones, 4 players carry a Mega together across 60 studs with no
   visible jitter or rubber-banding in screenshots/recording, speed matches the lift rule, and exploit tests (huge move
   vectors, far joins) change nothing.
M2 Furnace + hatch: drop zone, reveal sequence, per-carrier rolls, eligibility, Scrapkin pop + walk to plot.
   DONE WHEN: 1,000 simulated hatches match odds; a 2-player carry gives 2 independent reveals.
M3 Plots + income: pads, collect, offline, sell, storage, follower strength.
   DONE WHEN: income over a simulated 10 min matches Config within 1%; offline card shows the capped value.
M4 Upgrades + Rebirth + Index.
   DONE WHEN: rebirth resets/keeps exactly per C8 and unlocks R2; Index rewards fire every 10.
M5 Clocks: Junk Train (incl. Golden), Crusher (ragdoll + drop + shield), Titan Clump (scaling).
   DONE WHEN: a solo server can finish a Titan; Crusher never touches R1 or shielded players.
M6 Real assets (Blender + uploads; textures after OK).
   DONE WHEN: no greybox left in the main loop; screenshots of plaza, each ring, plots, reveal.
M7 UI: every screen in C13, all input types.
   DONE WHEN: OverlapCheck = 0 on all 6 targets; touch targets ≥ 44 px; gamepad reaches every button.
M8 Onboarding (C11).
   DONE WHEN: a fresh TEST save hits every step in order; first hatch < 25 s; first upgrade < 40 s.
M9 Balance: BalanceSim.
   DONE WHEN: sim shows first hatch < 25 s, first Chunk lift (solo, with upgrades) ≈ 4 min, first Rebirth 25–35 min solo
   and 15–25 min in a 3-player team, R4 unlocked ≈ 4–6 h total; tune Config until true.
M10 Social + retention: friend boost, invites, referral, group reward, codes, daily, quests.
   DONE WHEN: a simulated day rollover (TEST-only time offset) resets quests and advances the streak.
M11 Monetization: passes, products, receipts ledger, PolicyService gating, Store UI with exact odds.
   DONE WHEN: each product grants exactly once (incl. forced retry); restricted-policy test hides luck items.
M12 Live ops: LiveEventService + Admin Junk Rain + limited roster that leaves the pool.
   DONE WHEN: the Studio test trigger runs a full event start → end and limited Scrapkins stop dropping after.
M13 Polish + juice pass (C2/C6 sounds, particles, shakes, banners).
M14 Performance: 8-client stress test with 120 clumps, all pads full, Titan event.
   DONE WHEN: server heartbeat ≥ 55, client FPS ≥ 40 on Low, under budgets (print counts).
M15 Final QA → section E.

====================================================================================================
## E. FINAL HAND-OFF CHECKLIST
====================================================================================================
[ ] SmokeTest PASS n/n; OddsTest PASS; 0 errors in Output during a 10-min 4-client playtest.
[ ] OverlapCheck 0 on Phone 20:9, Phone 16:9, Tablet, Console, PC 1080p, PC 768p; touch targets ≥ 44 px.
[ ] Screenshots in screenshots\<device>\ of: plaza, carry with 4 players, reveal, plot, shop, index, store, rebirth.
[ ] BalanceSim report pasted in MORNING_REPORT.md (first hatch, first upgrade, first Chunk, first Rebirth solo/team).
[ ] DataStore session lock/autosave/retry/migration tested on TEST store only.
[ ] Remotes validated + rate-limited; exploit test (spam, bad args, teleport clump, far join) changes nothing.
[ ] Every 2D image approved before upload; no banned content (B1).
[ ] live_src\ mirrors the place; BuildLog complete.
[ ] MORNING_REPORT.md: done / broken / next / [ASSUMPTION]s / list of passes + products to create (name, price,
    description, Config key) / 8-week update plan (new ring theme or Scrapkin set every Saturday).
[ ] Tell the owner exactly: "SAVE NOW (Ctrl+S) + PUBLISH"
````
