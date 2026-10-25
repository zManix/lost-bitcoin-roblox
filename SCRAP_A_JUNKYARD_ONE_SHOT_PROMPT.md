````
# ONE-SHOT BUILD PROMPT — "SCRAP A JUNKYARD" (Roblox)

You are a senior Roblox engineer + technical artist. Build a complete, polished Roblox game called SCRAP A JUNKYARD in
Roblox Studio, end to end, from this document alone. You have never seen any earlier conversation; everything you need
is here. Work through the whole spec without stopping to ask. Only stop for: a login, a payment, a CAPTCHA, the
image-approval gate (B2), or a decision that truly belongs to the owner. Where something is unspecified, pick the
sensible default, log it as [ASSUMPTION] in the BuildLog, and keep going.

WHY THIS DESIGN (protect these when you make trade-offs)
- Proven lane: "clear the whole area in runs" — Chop A Forest (Roblox, launched 2026-09-21: 76K peak, 52K live, 93% likes).
  Its skeleton: START A RUN with bare hands → run-only coins buy tools/vehicles → clear zones → boss per zone → permanent
  Gems buy classes (random 5-min restock), pets, permanent vehicles → mutated items drop Gems → day/night with thieves →
  solo & friend runs save. We copy that MECHANIC skeleton (no assets, names or text).
- Our edge (protect it): Lost Bitcoin-style THROUGHPUT VERBS into a live FURNACE that sprays coins (pack and tip out a
  backpack, vacuum a tank and blow it in, shoot a magnet cluster, winch heavy junk), JUNK TOWER COLLAPSES, NO-GUN JUNK
  GOLEM bosses beaten with your own tools, FIRE HATCH of pets (flame color reveal), and Mystery Sticks with a rolling-digit
  reveal.
- Two earlier junkyard games died: one used a real-physics scrap pile (lag) + a party lobby before playing + "find one
  key" as the only goal + thin polish (60% likes). Do the opposite: no free physics piles, instant START A RUN, clear
  zones as the goal, heavy juice.
- Roblox ranks on: first-minute bounce, 28-day retention, days played, playtime, co-play days. Low-end phone crashes
  count as bounces. ~80% of players are on mobile. Design and test for that.

====================================================================================================
## A. YOUR ENVIRONMENT (given)
====================================================================================================
- Claude Code on Windows.
- Roblox Studio MCP tools: list_roblox_studios, execute_luau, multi_edit, script_read, start_stop_play, screen_capture,
  input simulation, insert_asset, generate_mesh, upload_image. Pass studio_id on EVERY call.
  Another Studio may be open. Lock onto the right place:
    1) list_roblox_studios  2) in the place you build: workspace:SetAttribute("ScrapAJunkyardAgent", true)
    3) before every batch of work probe: return workspace:GetAttribute("ScrapAJunkyardAgent")  → must be true.
  If not true you are in the wrong Studio: re-list and re-lock. NEVER edit, run or screenshot another Studio.
- Blender MCP for all 3D models: chunky, low-poly, stylized. Export FBX. Upload via the Roblox Open Cloud Assets API
  (API key + user/group ID are in the owner's env vars or memory notes, e.g. ROBLOX_OPEN_CLOUD_KEY, ROBLOX_USER_ID /
  ROBLOX_GROUP_ID). Insert the uploaded MeshParts. Use REAL uploaded meshes; never runtime EditableMesh (renders as
  boxes in live games).
- Images: Vertex AI with the newest Gemini image model available. POSITIVE-ONLY prompts: describe exactly what you
  want to see; never list things to avoid.

====================================================================================================
## B. HARD RULES
====================================================================================================
B1 Content safety (strict moderation): no skulls, blood, gore, robed or hooded figures, religious symbols, guns or any
   weapon aimed at people or creatures, text inside images, real brands/logos, real currencies or crypto symbols.
   Bosses are cartoon junk golems taken apart with cleaning tools; raccoons are shooed, never hurt.
B2 Image gate: every 2D image is saved first to pending_review\ with a .txt (prompt + intended use). STOP and wait for
   the owner's OK before uploading. Batch images to ask rarely; keep building with grey placeholders while waiting.
B3 Quality loop: small steps. After EACH step: smoke test → start_stop_play playtest → screen_capture → inspect → fix.
B4 Smoke test: ServerScriptService/Tests/SmokeTest (run via execute_luau): require every ModuleScript, check every remote
   exists, validate Config (no nil, no negative costs, cost curves strictly increasing, every odds table sums to exactly
   100, every unlock reachable), confirm DataStore TEST mode in Studio, tick every service once with a fake player, print
   "SMOKE PASS n/n" or each failure. Run after every change; 0 failures before moving on.
B5 Platforms: test Phone 20:9 (800x360), Phone 16:9 (640x360), Tablet (1024x768), Console (1920x1080, 10-foot UI), PC
   (1920x1080 and 1366x768). Use Studio device emulation if you can drive it; otherwise the overlap checker's "virtual
   viewport" mode (parent the HUD into a Frame of each target size and measure).
B6 UI overlap check: StarterPlayerScripts/Dev/OverlapCheck: every visible GuiObject vs every other (skip parent/child and
   tooltips) and vs reserved zones (Roblox top bar via GuiService.TopbarInset, chat, mobile thumbstick bottom-left, jump
   button bottom-right). 0 overlaps on all devices. Every touch target ≥ 44 px.
B7 Performance: StreamingEnabled ON (StreamOutBehavior Opportunistic). Reuse meshes (same MeshId). Budgets in C16.
   Adaptive QualityController (C16). Must run smooth on 2 GB Android phones.
B8 Data: DataStore with session locking (UpdateAsync lock = JobId + timestamp, steal after 30 min stale), autosave every
   90 s + on leave + BindToClose, retries with exponential backoff (5 tries), data version + migrations. In Studio ALWAYS
   use "SAJ_TEST_v1"; the live store "SAJ_LIVE_v1" only when not RunService:IsStudio(). Never touch live data in tests.
B9 Server authority: the server owns coins, gems, items, tools, runs, hatch rolls, purchases, boss state. The client
   only asks. Every remote: type checks, distance/ownership checks, per-player token-bucket rate limits, log + ignore bad
   requests (kick only on repeated clear abuse). Purchases via MarketplaceService.ProcessReceipt + saved receipt ledger.
B10 Logging: ServerStorage/BuildLog (timestamped: step, result, assumptions). MORNING_REPORT.md in the project folder:
   done / broken / next / all [ASSUMPTION]s. Mirror EVERY script to a local live_src\ folder (same tree, .lua) after
   every edit.
B11 Don't publish. Don't create passes/products on the website; put placeholder IDs in Config and list what the owner
   must create. At the end tell the owner exactly: "SAVE NOW (Ctrl+S) + PUBLISH".
B12 Loop: keep going through every milestone until the hand-off checklist (E) is all green.

====================================================================================================
## C. GAME SPEC
====================================================================================================

### C1 Name, pitch, characters
- SCRAP A JUNKYARD. Pitch: "Grandma Barb will pay a mountain of coins if you clear her whole junkyard! Start with bare
  hands, toss junk into the furnace for coins, get a vacuum, a magnet and a winch, topple junk towers, beat the Junk
  Golems and hatch Scrapkins in the fire. Solo or with friends — your run saves."
- GRANDMA BARB: cheerful junkyard owner, overalls, hard hat, big boots, thumbs-up. Short speech bubbles (≤ 8 words).
- SCRAPKINS: cute pets made of junk parts (bottle-cap hat, spring tail, teacup body, button eyes).
- RACCOON BANDITS: round, goggles, tiny sacks; mischievous, never scary.
- JUNK GOLEMS: big lumbering cartoon figures built from the zone's junk with glowing loose ARMOR PLATES and a glowing CORE.
- Iconic Secret Scrapkin: GOLDEN BYTE (a tiny golden memory-stick critter with a glowing smile).

### C2 Art direction
- Chunky low-poly, toy-like, soft bevels, oversized props. Junk is colorful and cheerful, never grimy.
- Palette (Config.Colors): Sunset haze #E9A65B | Deep shadow #3B2A22 | Rust #B5532B | Teal #4FA39A | Cream #F2E3C2 |
  Furnace glow #FF8A1F | Coin gold #FFC83D | Gem cyan #46E0FF | UI panel #1E1A17 (92%) | UI accent #FF9A2E |
  Bought green #5BD16B | Locked grey #6E6A66. Rarity colors: Common #CFCFCF, Uncommon #6BD36B, Rare #4DA3FF,
  Epic #B06BFF, Legendary #FFC83D, Mythic #FF5FA2, Secret = animated rainbow gradient.
- Lighting: Future (ShadowMap on Low). Day ClockTime 14→17.5 golden hour; Night = soft blue moonlight (ClockTime 21,
  Ambient #3A4A6A), lamps on, furnace glows brighter. Atmosphere Density 0.3, Haze 2, Color #E9A65B by day.
  Bloom 0.6 / threshold 1.4. ColorCorrection warm by day.
- Camera: third-person, max zoom 22; a light FOV pulse when the vacuum runs; small kick on big furnace drops.
- Music: chill funky "junkyard groove" by day, sneaky pizzicato at night, big brass for boss fights, fanfare on zone
  clear. Free Creator Store audio via insert_asset. [ASSUMPTION]
- SFX: grab pop, throw whoosh, furnace WHOOMPH (pitch by mass), coin clink cascades, vacuum whoosh (pitch rises with
  tank %), tank-full ding, magnet hum + clack, winch ratchet, stack wobble creak + crash, raccoon giggle + "eep!",
  golem stomp + plate pop, reveal tones, UI clicks.

### C3 World & runs (one place; server MaxPlayers 12)
- HUB (spawn): Grandma Barb's trailer, the START A RUN pad, a class shop booth (C10), a Scrapkin pen showing your
  equipped pets, leaderboards (fastest Zone 1, fastest full run, solo + party), daily-reward mailbox, store kiosk.
- RUNS: stepping on START A RUN → "Solo" or "Invite friends" (players in the server can tap "Join run" on the run
  card for 20 s; max 4). The server spawns a RUN INSTANCE: a copy of the run map placed far away (instances 2,500 studs
  apart; up to 6 at once), streamed. Each run map = 5 ZONES in a row behind gates:
  Z1 Backlot Yard · Z2 Rust Hills · Z3 Appliance Alley · Z4 Car Canyon · Z5 Tech Dump.
  Each zone has a HUB PAD with a big FURNACE (wide glowing mouth on a ramp; vehicles can back up to it), a READER desk
  (retro computer for Mystery Sticks), and a zone progress bar on a sign.
- RUN SAVE: runs save and resume (solo slot + 1 party slot owned by the party leader). Saved: zone, per-pile remaining
  counts, coins + run tools per member, run timer, run level. Permanent progress (gems, classes, pets, permanent
  vehicles, passes) always saves to each player.
- RUN COMPLETE (after the Z5 boss): celebration, gem payout, badge, speedrun time posted, then "Start Run Level N+1"
  (all values ×1.5, golem plates ×1.25, gem payouts ×1.4). This is the endless prestige — tools never get taken away.
- No death, no fall damage, nothing permanent is ever lost.

### C4 Core loop
- Seconds: grab junk → (pack it) → throw it / tip out the backpack / blow the vacuum tank / shoot the magnet cluster into
  the furnace → flame burst + coin fountain + "+n".
- Minutes: buy run tools and upgrades with coins → bigger, heavier junk → topple whole junk towers → drive a junk wagon to
  the furnace → clear 100% of the zone → JUNK GOLEM boss → gems + a Zone Capsule → next zone.
- Session: spend gems on classes (5-min restock), permanent vehicles, luck; hatch Capsules in the fire for Scrapkins;
  read Mystery Sticks; survive nights; push speedrun times; complete the run → Run Level up.

### C5 Junk, stacks, weight gates (Config.Junk, Config.Stacks)
- JUNK TOWERS (piles): each zone has N towers (Z1 12, Z2 14, Z3 16, Z4 18, Z5 20). A tower = 15–40 junk pieces
  stacked on a scripted "stack graph" (each piece knows what it supports). All pieces are ANCHORED pooled MeshParts.
  Pull a SUPPORT piece (glowing outline when you aim at it) → the pieces above it wobble 0.4 s, then topple with
  tweened arcs and bounces (TweenService, no physics) and land as loose pieces around the base. Big collapses = screen
  shake (≤ 0.2 s), dust burst, crash sound. This is a key clip moment — make it feel great.
- Loose pieces are grabbable. Value = weightKg × 0.6 coins × zone multiplier (Z1 ×1, Z2 ×3, Z3 ×9, Z4 ×27, Z5 ×81) ×
  mutation × class/pet/pass/run-level multipliers.
- Weight classes: small 1–15 kg (cans, boxes, toasters, jerrycans) · medium 15–60 kg (tires, drums, TVs, chairs) ·
  heavy 60–250 kg (fridges, washing machines, car doors, engines) · giant 250–600 kg (car bodies, Z4+, winch only).
- Weight gate prompts (exact style): "Too heavy: 55 kg (carry strength 12 kg)" in red under the hover card. Hover card
  always shows name, kg and coin value ("Fridge · 55 kg · 140 coins").
- Mutations on junk (rolled at zone generation; luck raises them): Golden 4% (×3 value, +2 Gems when burned),
  Neon 1.5% (×4, +3 Gems), Prism 0.5% (×5, +6 Gems). Mutated pieces sparkle and hum.
- Mystery Sticks: 6 per zone hidden inside towers (look identical). Read at the READER (C9).

### C6 Tools & upgrades (run-only, bought with coins; Config.Tools) — cost(level) = round(base × 1.6^(level-1))
| Tool / upgrade | Price | Max lvl | Effect |
|---|---|---|---|
| Hands (start) | – | – | grab 1 piece ≤ carry strength; throw (hold = harder) |
| Carry Strength | 25 | 15 | 12 kg → +6 kg/lvl |
| Walk Speed | 30 | 10 | 16 → +1/lvl |
| Throw Power | 40 | 5 | +4 studs throw range/lvl |
| Backpack | 100 | – | pack pieces (F) and DOUBLE-TAP F at the furnace to tip ALL out; 4 slots |
| Backpack Slots | 150 | 8 | +1 slot/lvl (4 → 12) |
| Vacuum | 1,000 | – | hold to suck loose pieces ≤ suction kg into the TANK; alt = BLOW the tank into the furnace |
| Vac Tank | 400 | 8 | 30 kg → +20 kg/lvl |
| Suction Power | 600 | 6 | sucks pieces up to 5 → +5 kg/lvl |
| Blow Speed | 500 | 6 | 15 → +8 kg/s/lvl; Multi Nozzle at lvl 6 (3 streams) |
| Magnet | 4,000 | – | pull up to 4 pieces (≤ 50 kg each) into a cluster; release = SHOOT it |
| Magnet Radius/Capacity/Strength | 1,500 / 2,000 / 3,000 | 6 each | +1.5 studs / +1 piece / +25 kg |
| Winch | 8,000 | – | hook a heavy/giant piece; it reels to the furnace or your vehicle |
| Winch Speed | 3,500 | 5 | +25%/lvl |
| Mega Claw | 40,000 | – | (Z3+) grab the top section of a tower (up to 6 pieces) at once |
| Furnace Heat | 50 | 12 | +12% coins/lvl (applies in every zone furnace this run) |
| Appraiser's Eye | 20 | – | shows coin values on hover (bought first in tutorial) |
| X-Ray Pulse | 12,000 | – | 20 s cooldown pulse that outlines Mystery Sticks + mutated pieces within 40 studs |
- Every upgrade shows "now → next" and the change must be visible/feelable (no invisible +1%).

### C7 Vehicles (Config.Vehicles)
- Simple arcade vehicles (VehicleSeat-free custom controller; mobile thumbstick drives). Pieces you throw/vacuum/magnet
  into the BED stack visually. Back up to a furnace ramp and press DUMP → the bed tips → giant coin explosion.
| Vehicle | Cost | Capacity (pieces) | Type |
|---|---|---|---|
| Junk Wagon | 500 coins | 30 | run-only |
| Pickup | 3,000 coins | 60 | run-only |
| Dump Truck | 9,000 coins | 100 | run-only |
| Hauler | 300 gems | 120 | permanent |
| Big Dumper | 800 gems | 160 | permanent |
| Monster Mover | 2,000 gems | 220 | permanent |

### C8 Junk Golem bosses (Config.Bosses) — no weapons, beat it with your tools
- At 100% zone clear, the last loose junk flies together into a JUNK GOLEM in the zone arena (cutscene 3 s, music swap).
- Golem has ARMOR PLATES (Z1 10, Z2 14, Z3 18, Z4 22, Z5 26; × (1, 1.5, 2, 2.5) for party size 1–4; × run-level scaling).
  Plates glow; VACUUM them off (2–4 s hold each, plate flies into your tank) and BLOW/THROW them into the furnace to
  destroy them (or a nearby portable "Boss Furnace" chute that appears in the arena).
- Attacks (all telegraphed with red ground rings 1.2 s ahead): STOMP (shockwave ring — jump it; hit = knockback + drop
  carried items), JUNK TOSS (lobs a piece at your spot — dodge), at 50% plates: SPIN (sweeping arm, duck behind cover).
  No HP for players; getting hit = funny knockback only.
- All plates gone → the glowing CORE drops. MAGNET or WINCH the core into the furnace → victory: gems
  (Z1 50, Z2 100, Z3 200, Z4 400, Z5 800 × run-level), a ZONE CAPSULE for every participant, the next gate opens.

### C9 Mystery Sticks & the Reader (Lost Bitcoin homage)
- Plug a stick in → "READING STICK 0%→100%" (3 s, lights fill) → digits ROLL like a counter, slow down and stop on the
  result (big numbers flash past first — the tension beat) → result card. Outcomes (Config.StickOdds, shown in the Reader
  info panel): Gems 5 (50%) · Gems 15 (30%) · Gems 40 (14%) · Basic Capsule (5%) · GOLDEN DRIVE (1%: 250 gems + badge +
  Golden Capsule + server banner). Odds sum to 100; luck boosts are NOT applied to sticks (keep sticks simple).

### C10 Gems, classes, restock (permanent; Config.Classes)
- Gem sources: mutated junk, bosses, sticks, daily drip (35 gems every 6 h, claim at the mailbox), group reward (100
  once), codes, quests, run complete.
- CLASS SHOP: shows 3 random classes from the pool; restocks every 5 minutes on a global clock (same for every server:
  slot = floor(os.time()/300), seeded random). Owned classes are permanent; equip one at a time.
| Class | Gems | Bonuses |
|---|---|---|
| Scrapper | free | – |
| Picker | 150 | +10% carry, +10% speed |
| Hauler | 400 | +25% carry, +10% sell |
| Tinkerer | 700 | +25% tool power, +15% sell |
| Magnetic | 1,000 | +50% magnet radius, +20% sell |
| Blaster | 1,500 | +50% blow speed, +25% sell, +15% rare luck |
| Tycoon | 2,200 | +50% sell, +25% rare luck |
| Junk Baron | 3,000 | +100% power, +25% speed, +50% sell, +50% rare luck, +3 carry slots |
| Golden Hands | 4,000 | +150% power, +35% speed, +100% sell, +100% rare luck, +5 carry slots |
| Cosmic Collector | 6,000 (unlocks after first Run Complete) | +200% power, +40% speed, +150% sell, +150% rare luck, +6 slots |
- Permanent upgrades (gems): Mutation Luck (10 lvls, 100 × 1.7), Starting Coins (5 lvls), Night Shield (fewer raccoons).

### C11 Night & Raccoon Bandits (Config.Night)
- Each run instance has its own clock: DAY 8 min → NIGHT 4 min. Night banner + music swap + moonlight.
- Raccoons: 2 + 1 per player (cap 6) sneak in from the edges. Each picks a goal: steal 1 piece from a backpack, steal 3
  pieces from a vehicle bed, or re-pile 5 pieces onto a cleared tower spot. They carry loot in a little sack.
- Shoo them: BLOW them with the vacuum (alt), or TAP/BONK with hands. They tumble (cartoon spin, stars), drop their sack
  + 3–10 coins, 10% chance of a BASIC CAPSULE, and run off. No damage to anyone, ever.
- PEACEFUL MODE (Settings): no nights, no raccoons, no raccoon capsules, no speedrun leaderboard entry.

### C12 Fire hatch & Scrapkins (Config.Capsules, Config.Scrapkins)
- Capsules: BASIC (raccoons, sticks), ZONE (each boss: themed to that zone), GOLDEN (Golden Drive).
- Hatch = throw the capsule into ANY furnace → 2.5 s reveal: the furnace shakes, the flame color steps up
  white → green → blue → purple → gold → pink → rainbow and STOPS at the result (pitch-rising tone + sparks per step;
  Epic+ adds a glow + shake) → the Scrapkin pops out with squash-and-stretch and rarity confetti → name card.
- Odds (%, sum 100): Common / Uncommon / Rare / Epic / Legendary / Mythic / Secret
  Basic 60 / 25 / 10 / 4 / 0.9 / 0.1 / 0
  Zone 30 / 30 / 22 / 12 / 4.5 / 1.3 / 0.2
  Golden 0 / 0 / 35 / 35 / 20 / 8 / 2
  Show the exact odds (with the player's luck applied) on an ODDS card before throwing. Luck passes/potions ×2 the
  Epic+ weights, then renormalize, and the card shows the final numbers.
- Roster at launch: 6 per zone theme × 5 zones + 2 Secrets (GOLDEN BYTE, DISCO DUMPSTER) = 32. Size mutation on hatch:
  Big 8% (×1.5 bonus), HUGE 1% (×3 bonus).
- Bonuses (equip 3; +2 slots with pass): Common +2% sell · Uncommon +4% sell · Rare +8% sell, +5% luck · Epic +15% sell,
  +10% power · Legendary +30% sell, +10% speed · Mythic +60% sell/power/luck · Secret +100% sell/power/luck/speed.
  Equipped Scrapkins follow you (simple hop movement, no Humanoid; max 3 rendered per player; others' hidden on Low).
- Index (collection book): silhouettes until found; rewards every 5 discoveries (gems, cosmetic trails).

### C13 Onboarding (first 60 s fun, no wall of text) — funnel-log every step (AnalyticsService:LogOnboardingFunnelStepEvent)
- 0–5 s: spawn in the Hub; Barb: "Clear my yard, get rich!" START A RUN pad pulses → tap → Solo (pre-selected).
- 5–15 s: Z1 hub. A small junk pile sits next to the furnace. "Grab junk! Throw it in!" → first throw → coin fountain
  "+3". Pulse the shop button: buy APPRAISER'S EYE (20) → values appear on hover.
- 15–30 s: buy CARRY STRENGTH (25). First upgrade < 30 s.
- 30–60 s: a tutorial tower with one glowing support piece next to the furnace: "Pull the glowing piece!" → COLLAPSE
  → pile of loose junk → toss it in → "+40".
- ~1:30 Backpack (100) → "Pack with F, double-tap F to tip it all out!" (mobile: PACK / TIP OUT buttons).
- ~3 min Junk Wagon (500). ~5–6 min Vacuum (1,000) → "Suck it up, blow it in!". First night ≈ 8 min with a 1-time
  raccoon tip. First boss ≈ 10–12 min. Tutorial skippable; steps auto-skip if done.

### C14 Controls (ContextActionService; hints swap on LastInputType)
- PC: WASD, LMB use tool (hold = harder throw / suck), RMB alt (put down / blow / release magnet), F pack, double-F tip
  out, E interact (reader, dump, capsule), 1–6 tool slots, Q pulse, B shop, Tab index, Shift sprint.
- Mobile: thumbstick; big USE button (right) + ALT button above it; PACK and TIP OUT chips; tool wheel (6 slots, arc
  above jump, each ≥ 44 px); context button (DUMP / READ / HATCH); soft auto-aim to the nearest valid piece in a 25° cone.
- Console: RT use, LT alt, X pack (double-X tip), Y shop, LB/RB tools, B back, D-pad menus; full GuiService selection.
- Vehicles: thumbstick / WASD / left stick; DUMP button at the furnace.

### C15 UI (scale-based; UIAspectRatioConstraint + UISizeConstraint)
- HUD: coins (top-left under topbar inset) + "+n" fly-ins; gems chip; zone progress bar + run timer (top-center);
  day/night chip; tool bar; Backpack x/y, Vac Tank %, Magnet x/y bars (bottom-right, above jump on mobile — no overlap);
  hover card (center-bottom: name · kg · coins, red weight-gate line when too heavy); context button; mini quest tracker.
- Screens: Scrap Shop (tabs: Player / Tools / Vehicles / Furnace — each upgrade card with "now → next", cost, BUY);
  Class Shop (3 cards + restock timer); Reader; Odds card; Hatch reveal card; Index; Pets (equip); Run card (Solo /
  Invite / Join); Boss bar (plates left); Zone clear + Run complete screens; Daily (7-day); Quests (3 daily, 2 weekly);
  Store (passes + products, exact effects, odds where relevant); Settings (music, SFX, graphics Auto/Low/High, reduced
  shake, Peaceful mode, skip tutorial); Welcome Back; Toasts (max 3).

### C16 Performance budgets + QualityController
- Junk pieces: ~30 pooled meshes, anchored, CanTouch off (use raycasts for interaction), CastShadow off for small,
  CollisionFidelity Box. Max live pieces per run instance: 1,200 (only the current zone + next zone loaded; earlier
  zones unload). Up to 6 instances per server → hard cap 7,000 pieces server-wide (print counts).
- Tower collapses: tween at most 40 pieces per collapse; extra pieces pop in place with a dust puff.
- Raccoons and Golems: simple rigs with AnimationControllers; no Humanoid physics. Scrapkin followers: tweened hops.
- Target: < 1,000 draw calls, < 1M triangles on screen; textures ≤ 512².
- QualityController: sample FPS every 2 s; < 40 → step down (shadows off on props, half particles, fewer coin sprites,
  shorter decoration fade); > 55 for 10 s → step up. Settings can force Low/High.

### C17 Juice (JuiceController; all respect Settings → reduced shake)
- Furnace: flame burst scales with mass; coin fountain (5–40 coin sprites) arcs to the HUD counter; counter bounces.
- Number pops at the furnace, color by value tier (white < 100 < green < 1K < gold < 10K < rainbow).
- Tower collapse: wobble, creak, cascading tumble, dust, shake. Vacuum: particle stream into the nozzle, tank pitch
  rise, full = ding + bar bounce. Magnet: pieces snap to the cluster with clacks; shoot = whoosh + trail.
- Upgrade bought: card squash, sparkle, rising chime; max level = gold frame. Zone clear: confetti + Barb cheer.
- Golem: plate pop with spark ring, core drop slow-mo 0.5 s, victory fanfare. Hatch: see C12. Golden Drive: server
  banner + golden beam from the Reader.

### C18 Monetization (honest; placeholder IDs in Config.Monetization; prices from live comparable games)
Rules: show the exact effect before buying; no fake discounts/countdowns; NO paid capsules/hatches or any paid random
item; never sell gems or any currency that buys something random. Luck items show exact resulting odds and are hidden
for players where PolicyService:GetPolicyInfoForPlayerAsync says ArePaidRandomItemsRestricted. Co-op game: nothing gives
power over another player.
| Type | Name | R$ | Effect |
|---|---|---|---|
| Pass | 2x Coins | 199 | +100% coins |
| Pass | 2x Gems | 199 | +100% gems from all sources |
| Pass | Infinite Backpack | 149 | backpack slots unlimited (stack visual caps at 20) |
| Pass | Vacuum Forever | 199 | start every run with the Vacuum |
| Pass | Magnet Forever | 249 | start every run with the Magnet |
| Pass | Helper Bot | 399 | a small robot buddy auto-picks small loose junk near you into your backpack |
| Pass | Lucky Hatch | 149 | ×2 Epic+ capsule weights (odds shown) |
| Pass | +2 Pet Slots | 149 | equip 5 Scrapkins |
| Pass | VIP | 249 | +10% coins & gems, gold name tag, VIP hub lounge, 1 free daily quest reroll |
| Product | 2x Coins 15 min | 29 | timed |
| Product | Luck Potion 15 min | 39 | ×2 Epic+ capsule weights + ×2 junk mutation chance (odds shown) |
| Product | Golden Hour (server gift) | 99 | 10 min ×2 mutation chance for everyone in the server; gifter's name shown |
| Product | Coin Pack | 49 | exactly 15 min of your current average income (shown before buying) |

### C19 Retention, social, live ops
- Daily: 7-day streak (gems → Luck Potion → coins → gems → trail → Basic Capsule → Day 7 Zone Capsule). Missing a day
  drops 2 days, not to zero. Gem drip 35 every 6 h. 3 daily quests (topple 5 towers, burn 300 kg, shoo 3 raccoons, read
  2 sticks, beat a golem) + 2 weekly.
- Friends: +10% coins per real Roblox friend in your run (cap +30%; friend accounts ≥ 7 days old). Invite button
  (SocialService:PromptGameInvite). Use Roblox's official referral rewards if available. Group reward: 100 gems once
  (Player:IsInGroup). Codes (Config.Codes, e.g. "SCRAPIT").
- Speedrun leaderboards (OrderedDataStore): fastest Z1 and full run, solo and party; weekly reset board + all-time.
- Live ops: Config.LiveEvents (UTC windows, multipliers, limited Scrapkins that leave the pool), Saturday ADMIN
  "GOLDEN JUNK RAIN" (MessagingService, 30 min ×3 mutation chance, junk falls from the sky in every run), 60-char
  Config.UpdateNote, Studio-only test command to fire any event.
- MORNING_REPORT.md must include an 8-week Saturday update plan (e.g. W1 Halloween/seasonal Scrapkins, W2 Zone 6 "Toy
  Mountain", W3 new golem attack + classes, W4 vehicles, W5 Zone 7, W6 limited event, W7 pets set, W8 Run Level rewards).

### C20 Asset list
3D (Blender → FBX → Open Cloud → MeshPart; low-poly 200–1,500 tris; shared palette atlas):
- Junk (30): cardboard box, jerrycan, tin can, toaster, kettle, radio, desk lamp, old tire, oil drum, TV, chair, bicycle,
  shopping cart, traffic cone, pipe bundle, spring, sofa, fridge, washing machine, car door, engine block, gear, hubcap,
  keyboard, monitor, speaker, cable spool, toy blocks, rubber duck, car body (giant).
- Mutation materials (in-engine): Golden, Neon, Prism (sparkle particle + hum).
- Zone dressing per theme (fences, cranes, lamp posts, rails, crates, signs without text), zone gates, hub pads.
- Furnace (mouth, ramp, chimney, animated flame planes), Reader desk (CRT + keyboard + stick slot + 5 lights),
  Mystery Stick, Golden Drive, Capsules ×3, START A RUN pad, class shop booth, mailbox, leaderboards, Barb's trailer.
- Tools (viewmodels): glove, backpack, vacuum (tank + nozzle, multi-nozzle variant), magnet, winch hook, mega claw.
- Vehicles ×6 with a tipping bed. Helper Bot.
- Characters: Grandma Barb (rigged: wave/point/cheer), Raccoon Bandit (run, steal, tumble, flee), Junk Golem base rig
  (plates attach to sockets; 5 zone skins), 8 Scrapkin base bodies + 30 junk attachments to assemble the 32 roster.
2D (Vertex → pending_review\ → OK → upload_image):
- MaterialVariant ground textures per zone ("seamless tileable texture of packed colorful cartoon junk and dirt, warm
  sunset light, stylized low-poly game art, top-down view"; variants with tones per zone).
- UI icons (512², flat, a centered object on a plain rounded dark background): coin, gem, each tool, each vehicle, each
  class emblem, capsules, rarity gems, daily gift, index book, store items.
- Game icon + 3 thumbnails: "a giant cheerful junk tower toppling toward a huge glowing furnace that sprays a fountain of
  gold coins, blocky kids cheering with a vacuum and a magnet, a cute junk creature popping out of the flames, golden-hour
  junkyard, vivid warm colors, kids' game art" — scenes only, no lettering. Make 3 variants for thumbnail testing.

### C-TECH Architecture
ReplicatedStorage/Shared: Config, Remotes, Format (1.2K / 3.4M / 5.6B), Odds (pure, unit-tested), StackGraph, Types, Signal.
ServerScriptService/Services: DataService, RunService (instances, save/resume, run level), ZoneService (towers, collapse,
progress, gates), JunkService (pieces, weights, mutations, pooling), ToolService (grab/pack/tip/vacuum/magnet/winch/claw,
validation), FurnaceService (burn → coins/gems, hatch), VehicleService, BossService, NightService (raccoons), StickService,
CapsuleService, PetService, ClassService (restock), UpgradeService, QuestService, DailyService, SocialService (friends,
invites, group, codes), LeaderboardService, MonetizationService (receipts, passes, PolicyService), LiveEventService,
AntiExploit, Bootstrap.
ServerScriptService/Tests: SmokeTest, OddsTest (100k rolls per table within ±0.2%), BalanceSim, StackTest (every tower's
graph is valid; every piece reachable).
StarterPlayerScripts/Controllers: Input, Tool (viewmodels, aim assist), Camera, HUD, Shop, ClassShop, Reader, Hatch, Pets,
Index, Vehicle, Boss, Run, Store, Tutorial, Juice, Audio, Quality, Settings. Dev/OverlapCheck.
Remote rate limits (per second): Grab 8, Throw 4, Pack 6, TipOut 2, VacuumTick 12 (unreliable), Blow 6, Magnet 4,
Winch 2, Claw 2, Dump 2, Read 1, Hatch 2, BuyUpgrade 6, BuyClass 2, Equip 3, Run 2, ClaimDaily 1, ClaimQuest 2, Code 1.
Server checks: reach ≤ 12 studs for grab, furnace drop only inside the mouth volume (server position), vacuum target
within range and line of sight, per-tick movement caps for winched pieces and vehicles.

====================================================================================================
## D. BUILD ORDER (log each milestone in BuildLog + MORNING_REPORT.md)
====================================================================================================
M0 Setup: lock Studio, folders, Config, Remotes, DataService (TEST), BuildLog, live_src\ mirror, SmokeTest, OddsTest.
   DONE WHEN: smoke passes; data loads/saves/locks across 2 test sessions; every odds table sums to 100.
M1 Greybox Z1 loop: hub + START A RUN (solo) + one zone + 3 towers + grab/throw + furnace + coins + Appraiser + Carry Strength.
   DONE WHEN: in playtest, first throw < 10 s and first upgrade < 30 s (screenshots).
M2 Stack collapse: StackGraph, support highlight, tweened topple, zone progress %.
   DONE WHEN: StackTest passes; a collapse of 40 pieces keeps FPS ≥ 50 on emulated phone; looks satisfying in captures.
M3 Tools: backpack pack/tip-out, vacuum tank + blow, magnet cluster shoot, winch, weight gates + hover card.
   DONE WHEN: each tool works on PC, touch (input simulation) and gamepad; no exploit path in a spam/bad-args test.
M4 Vehicles: wagon/pickup/dump truck, bed stacking, DUMP at furnace.
   DONE WHEN: a 30-piece dump pays exactly the sum of piece values (log proves it).
M5 Boss: Junk Golem Z1 (plates, attacks, core, victory, gate).
   DONE WHEN: solo and 3-player clears both work; plates scale with party size; no player can be stuck.
M6 Gems + classes + restock + permanent upgrades + permanent vehicles.
   DONE WHEN: the class shop shows the same 3 classes on two servers in the same 5-minute slot.
M7 Night + raccoons + Peaceful mode.
   DONE WHEN: raccoons steal/re-pile and can always be shooed; Peaceful disables nights entirely.
M8 Sticks + Reader + capsules + fire hatch + Scrapkins + Index.
   DONE WHEN: 1,000 simulated hatches match odds; the reveal sequence plays correctly for each rarity.
M9 Zones 2–5 + run save/resume + run complete + Run Level.
   DONE WHEN: a run can be saved mid-zone, rejoined, finished, and Run Level 2 starts with the right scaling.
M10 Parties: invite/join run (max 4), friend boost, shared boss scaling, per-member coins saved in the party slot.
   DONE WHEN: Studio Test with 3 clients completes Z1 together, then each rejoins and the party run resumes.
M11 Real assets (Blender + uploads; textures after owner OK).
   DONE WHEN: no greybox in the main loop; screenshots of hub, every zone, a collapse, a golem, a hatch.
M12 UI: every screen in C15, all input types.
   DONE WHEN: OverlapCheck = 0 on all 6 targets; touch targets ≥ 44 px; gamepad reaches every button.
M13 Onboarding (C13).
   DONE WHEN: a fresh TEST save hits every step in order within the target times.
M14 Balance: BalanceSim.
   DONE WHEN: first upgrade < 30 s, Backpack ≈ 1–2 min, Vacuum ≈ 5–6 min, Z1 boss ≈ 10–12 min, first full run 60–90 min
   (solo, can span sessions), a Run Level 2 Z1 clear with a mid-tier class ≈ 5–7 min. Tune Config until true.
M15 Monetization: passes, products, receipt ledger, PolicyService gating, Store UI with exact effects/odds.
   DONE WHEN: each product grants exactly once (incl. forced retry); restricted-policy test hides luck items.
M16 Retention + live ops: daily, quests, gem drip, codes, group reward, leaderboards, LiveEventService, Golden Junk Rain.
   DONE WHEN: a TEST-only time offset rolls the day (quests reset, streak advances) and the event trigger runs start → end.
M17 Performance: 12-client stress (6 run instances, collapses, night, a boss).
   DONE WHEN: server heartbeat ≥ 55, client FPS ≥ 40 on Low, under the piece caps (print counts).
M18 Final QA → section E.

====================================================================================================
## E. FINAL HAND-OFF CHECKLIST
====================================================================================================
[ ] SmokeTest PASS n/n; OddsTest PASS; StackTest PASS; 0 errors in Output during a 10-min 3-client playtest.
[ ] OverlapCheck 0 on Phone 20:9, Phone 16:9, Tablet, Console, PC 1080p, PC 768p; touch targets ≥ 44 px.
[ ] Screenshots in screenshots\<device>\ of: hub, run card, each zone, a collapse, vacuum blow, magnet shot, vehicle dump,
    golem fight, hatch reveal, reader roll, shop, class shop, store, index.
[ ] BalanceSim report in MORNING_REPORT.md (all M14 targets with actual numbers).
[ ] DataStore session lock/autosave/retry/migration + run save/resume tested on the TEST store only.
[ ] Remotes validated + rate-limited; exploit test (spam, bad args, far grabs, fake furnace drops, teleported pieces)
    changes nothing.
[ ] Every 2D image approved before upload; no banned content (B1).
[ ] live_src\ mirrors the place; BuildLog complete.
[ ] MORNING_REPORT.md: done / broken / next / [ASSUMPTION]s / passes + products to create (name, price, description,
    Config key) / the 8-week Saturday update plan / 3 thumbnail variants for testing.
[ ] Tell the owner exactly: "SAVE NOW (Ctrl+S) + PUBLISH"
````
