> **SUPERSEDED (v1), do not build.** Use `SCRAP_A_JUNKYARD_ONE_SHOT_PROMPT.md`.

````
# ONE-SHOT BUILD PROMPT — "SCRAP TO RICHES" (Roblox)

You are a senior Roblox engineer + technical artist. You will build a complete, polished Roblox game called
SCRAP TO RICHES in Roblox Studio, end to end, from this document alone. You have never seen any earlier
conversation. Everything you need is here. Work through the whole spec without stopping to ask. Only stop for:
a login, a payment, a CAPTCHA, an image-approval gate (see B2), or a decision that truly belongs to the owner.
Where something is unspecified, pick the sensible default, write it down in the BuildLog as [ASSUMPTION], and keep going.

====================================================================================================
## A. YOUR ENVIRONMENT (given)
====================================================================================================

- You run as Claude Code on Windows.
- Roblox Studio MCP tools: list_roblox_studios, execute_luau, multi_edit, script_read, start_stop_play,
  screen_capture, input simulation, insert_asset, generate_mesh, upload_image.
  - Pass studio_id on EVERY call.
  - Another Studio may be open. Lock onto the right place:
    1. Call list_roblox_studios.
    2. In the place you are building, run: workspace:SetAttribute("ScrapToRichesAgent", true)
    3. Before every batch of work, probe: return workspace:GetAttribute("ScrapToRichesAgent")
       If it isn't true, you're in the wrong Studio. Re-list and re-lock. NEVER edit, run or screenshot another Studio.
- Blender MCP: for all 3D models. Low-poly, stylized. Export FBX. Upload through the Roblox Open Cloud Assets API
  (API key + user/group ID are in the owner's env vars or memory notes; look for ROBLOX_OPEN_CLOUD_KEY,
  ROBLOX_USER_ID / ROBLOX_GROUP_ID or similar). Insert the uploaded MeshParts into the place.
  Use REAL uploaded meshes. Do NOT use runtime EditableMesh (it renders as boxes in live games).
- Images: Vertex AI, using the newest Gemini image model available there. Write POSITIVE-ONLY prompts:
  describe exactly what you want to see. Never list things to avoid.

====================================================================================================
## B. HARD RULES
====================================================================================================

B1. Content safety (Roblox moderation is strict). Never make or use: skulls, blood, gore, robed or hooded figures,
    religious symbols, weapons aimed at people, text inside images, real brands or logos, real currencies or
    crypto symbols. Tools in this game are only ever aimed at junk, crates and dirt.
B2. Image gate: every 2D image (textures, icons, thumbnails) is saved first to pending_review\ (with a .txt next to
    it holding the prompt and its intended use). Then STOP and wait for the owner's OK before uploading.
    Batch images so you ask as few times as possible, and keep building with grey placeholders while you wait.
B3. Quality loop: build in small steps. After EACH step: run the smoke test → playtest via start_stop_play →
    screen_capture → look for problems → fix → move on. Never stack untested work.
B4. Smoke test: ServerScriptService/Tests/SmokeTest (run it through execute_luau). It must:
    require every ModuleScript, check every RemoteEvent/RemoteFunction exists, validate Config (no nil, no negative
    costs, every cost curve strictly increasing, every unlock reachable), confirm DataStore is in TEST mode in Studio,
    simulate one tick of every service with a fake player table, and print "SMOKE PASS n/n" or each failure.
    Run it after every change. 0 failures before moving on.
B5. Platforms: test Phone 20:9 (e.g. 800x360), Phone 16:9 (640x360), Tablet (1024x768), Console (1920x1080, 10-foot UI)
    and PC (1920x1080 and 1366x768). Use Studio device emulation if you can drive it. If you can't, run the overlap
    checker in "virtual viewport" mode (parent the HUD into a Frame of each target size and measure).
B6. UI overlap check: script StarterPlayerScripts/Dev/OverlapCheck. Checks every visible GuiObject's AbsolutePosition and
    AbsoluteSize against every other one (skip parent/child pairs and explicit tooltips), and against reserved zones:
    the Roblox top bar buttons (GuiService.TopbarInset), chat, the mobile thumbstick (bottom-left), and the jump
    button (bottom-right). Result must be 0 overlaps on every device. Every touch target ≥ 44 px.
B7. Performance: StreamingEnabled ON. Reuse meshes (same MeshId = instanced). Part budget (see C12).
    Adaptive quality controller (see C12). Must stay smooth on cheap phones.
B8. Data: DataStore with session locking (UpdateAsync lock with server JobId + timestamp, steal after 30 min stale),
    autosave every 90 s plus on leave and BindToClose, retry with exponential backoff (5 tries), data versioning +
    migration function. In Studio ALWAYS use the test store "STR_TEST_v1". The live store "STR_LIVE_v1" is only used
    when not RunService:IsStudio(). Never read or write the live store while testing.
B9. Server authority: the server owns coins, gears, keys, items, upgrades, purchases and damage. The client only asks.
    Every remote: type-check args, distance/ownership checks, per-player rate limits (token bucket), and log + ignore
    bad requests (kick only after repeated clear abuse). Purchases go through MarketplaceService.ProcessReceipt with
    a receipt ledger saved in data (no double grants).
B10. Logging: ServerStorage/BuildLog (a ModuleScript holding a list of timestamped entries: step, result, assumptions).
    Keep MORNING_REPORT.md in the project folder: what's done, what's broken, what's next, all [ASSUMPTION]s.
    Mirror EVERY script to a local live_src\ folder (same tree as the place, .lua files) after every edit.
B11. Don't publish. Don't create game passes or dev products on the website yourself; create placeholder IDs in Config
    and list what the owner must create. When done, tell the owner exactly: "SAVE NOW (Ctrl+S) + PUBLISH".
B12. Loop: keep going through every milestone until the hand-off checklist (section E) is green.

====================================================================================================
## C. GAME SPEC
====================================================================================================

### C1. Name, pitch, fantasy
- Name: SCRAP TO RICHES
- Pitch: Dig through a giant junkyard with your friends, burn the junk for coins, upgrade your gear, build a
  money factory, and find the one Golden Stick hidden deep in the pile.
- Core fantasy: "Trash in the furnace → coins rain out." Big junk = big fountain of coins.
- Guide character: SPARKY, a small, round, friendly scrap robot with one big round eye-lens and stubby arms.
  Sparky gives the tutorial in short speech bubbles (max 8 words each).
- Goal of each Yard: somewhere deep in the pit is the GOLDEN STICK (a memory stick). Dozens of identical-looking
  MYSTERY STICKS are buried as well. Only the READER computer on the deck shows what's on a stick.

### C2. Art direction
- Style: chunky low-poly, stylized, toy-like proportions, soft bevels, slightly oversized props. Junk is cheerful,
  colorful and readable, not grimy.
- Palette (Config.Colors):
  Sunset haze #E9A65B | Deep shadow #3B2A22 | Rust #B5532B | Teal paint #4FA39A | Cream #F2E3C2 |
  Furnace glow #FF8A1F | Coin gold #FFC83D | UI panel #1E1A17 (92% opaque) | UI accent orange #FF9A2E |
  Bought green #5BD16B | Locked grey #6E6A66
- Lighting: Technology = Future (fall back to ShadowMap on low quality). ClockTime 17.2 (golden hour).
  Atmosphere Density 0.35, Haze 2, Color #E9A65B, Decay #8A5A3A. ColorCorrection warm (+0.05 saturation, tint #FFF1DE).
  Bloom 0.6 threshold 1.4 (the furnace and coins glow). The pit gets darker with depth: drive an underground ambience
  tween from the player's depth, so the Headlamp upgrade matters.
- Camera: third-person by default (best on mobile), max zoom 20, with a first-person toggle in Settings.
  The camera gently lowers its FOV when the vacuum runs; small kick on big throws.
- Music: chill, funky lo-fi "junkyard groove" for the surface; a softer, deeper ambient loop underground;
  an upbeat brass sting for upgrades; a big fanfare for the Golden Stick. Use the Creator Store audio library
  (insert_asset). Pick tracks marked free to use. [ASSUMPTION]
- Key SFX: furnace roar (pitch scales with item mass), coin clinks (stacked, randomized pitch), vacuum whoosh (pitch
  rises as the tank fills), tank-full ding, magnet hum, cutter sizzle, crate pop, safe clunk, reader beeps,
  layer-break rumble, UI click, upgrade chime, combo ticks rising in pitch.

### C3. World layout (one place, single server)
- Server MaxPlayers 12. 6 YARD PLOTS arranged in a ring around a central LOBBY HUB.
- LOBBY HUB: a plaza with 3 YARD GATES (Easy / Normal / Hard; locked tiers show a padlock icon and the unlock
  requirement), a MUSEUM building (collection book in 3D), a DAILY REWARD kiosk, a STORE kiosk, global leaderboards
  (Deepest Dig, Golden Sticks Found), and a Sparky statue. Spawn point is here.
- Each YARD PLOT has: a DECK (surface platform) beside a PIT.
  - Deck: the FURNACE (with a wide glowing mouth and a coin chute), the READER computer (2 reading slots),
    the SCRAP SHOP terminal (opens the upgrade tree), 12 FACTORY PADS in a chain with belts, the LIFT top station,
    and a HEAVY CHUTE where the winch drops big items.
  - Pit: 64 x 64 studs footprint. Depth by difficulty (see C5). Built from Roblox Terrain (cheap, streams well,
    carvable) with junk props embedded.
  - LIFT: a platform elevator in one pit corner. Its shaft automatically extends to the party's deepest point.
    Plus a free "Back to Deck" button (20 s cooldown) — nobody should ever be stuck at the bottom.
- No fall damage anywhere. No death.

### C4. Core loop
- Second-to-second: aim → suck/grab junk → watch the tank/backpack fill → carry or blow it into the furnace →
  coin fountain + number pop.
- Minute-to-minute: spend coins in the Scrap Shop tree → dig deeper (deeper = harder ground, better junk) → find
  crates, safes, Mystery Sticks → read sticks at the deck → place factory machines for passive income.
- Session-to-session: clear a Yard by finding the Golden Stick → celebration → choose KEEP GOING or REBIRTH
  (reset coins + Scrap Shop tree for GEARS, the permanent currency) → unlock harder Yards → fill the Museum →
  daily rewards and quests → offline factory income waiting for you.

### C5. Difficulty / Yards (Config.Yards)
| Yard | Unlock | Depth | Golden Stick depth | Mystery Sticks | Hazards | Gear mult | Target first clear |
|---|---|---|---|---|---|---|---|
| Backlot Yard (Easy) | start | 100 | 80–100 | 12 | none (pure relaxing) | 1.0 | 18–22 min |
| Rust Canyon (Normal) | clear Easy once | 150 | 120–150 | 20 | Rust Rats (light) + Buried Galleon | 1.6 | 24–28 min |
| Deep Dump (Hard) | clear Normal once | 200 | 170–200 | 30 | Rust Rats + Junk Slides | 2.5 | 28–32 min |

- Rust Rat: a cute round raccoon-like critter with goggles. If it touches you, it steals 1 backpack item and runs.
  Bonk it with the Grabber (tap) to make it drop the item + 1 coin pop. Max 3 alive per yard. Never deals damage.
- Junk Slide: telegraphed 2 s with a rumble + falling-dust particles, then refills a small area with loose junk.
  It costs time, never progress.
- Leaving a run: coins and upgrades are saved. When you come back, the yard regenerates with a shaft already dug
  down to 70% of your saved run depth ("Sparky kept your dig site!"). The Golden Stick location re-rolls.

### C6. Ground layers (Config.Layers)
| Layer | Depth (studs) | Terrain material (MaterialVariant name) | Hardness | Item value | Item weight |
|---|---|---|---|---|---|
| L1 Topsoil Junk | 0–25 | Ground → "PackedJunk" | 1 | 3–8 | 2–15 kg |
| L2 Rust Layer | 25–60 | Slate → "RustPack" | 2 | 12–40 | 5–30 kg |
| L3 Old Machines | 60–100 | Basalt → "MachinePack" | 3 | 60–200 | 10–60 kg |
| L4 Deep Dump | 100–150 | Rock → "DeepDump" | 4 | 300–900 | 15–120 kg |
| L5 Core Pile | 150–200 | Pavement → "CorePile" | 5 | 1,200–4,000 | 20–250 kg |
- Suction Power level must be ≥ layer hardness to dig that layer. Otherwise show a toast "Too hard! Upgrade Suction"
  with a button that opens the shop on that node.
- Entering a new layer: rumble, a layer banner ("RUST LAYER — junk worth more!"), 1 s slowmo of falling dust.
- Golden variant: 3% of items spawn golden (×5 value, sparkle particles, shimmer sound).
- Loose "scrap bits" from carved terrain go into the vacuum tank at 0.4 coin/kg × layer multiplier.

### C7. Tools (custom tool system, NOT Roblox Tool objects; hide the default Backpack CoreGui)
Hotbar slots 1–5. The item in hand shows as a viewmodel attached to the character's right hand.
1. GRABBER GLOVE (start): tap/click junk within 10 studs → it goes into the BACKPACK (start 2 slots). Weight limit
   20 kg (Hydraulic Grabber: 60 kg). THROW: hold to show an arc, release to throw. The server checks a ballistic
   landing point. If it lands in the furnace mouth volume → burn. Else it drops near the landing point.
2. JUNK VAC (unlock 100 coins): hold to suck. It carves Terrain in a sphere at the aim point (radius from Suction Radius)
   and pulls loose items ≤ (8 kg × Suction Power level) into the TANK (start capacity 20 kg). Alt action = BLOW-OUT:
   within 25 studs of the furnace, the tank streams into it at Blow-out Speed kg/s, paying coins per kg.
   Multi Nozzle = 1/2/3 visible streams (faster blow-out).
3. MAGNET (unlock 1,500): pulls up to Capacity items within Radius whose weight ≤ Strength; they stick to the magnet
   in a wobbly cluster. Release over the furnace.
4. CUTTER (unlock 5,000): hold on a crate (3 s), a safe (6 s, needs 1 Key), or the Galleon hull (10 s) to open it.
   It only ever targets these objects. It's a hand-held glowing cutter with an orange spark shower.
5. WINCH HOOK (unlock 800): attach to an item heavier than your grab limit (cars, fridges); the hook lifts it to the
   Heavy Chute, which burns it automatically. Winch Speed upgrade = faster lift.

### C8. Scrap Shop upgrade tree (Config.Upgrades) — 7 branches, target 60 nodes
Cost formula: cost(level) = round(baseCost × growth^(level-1)). Show cost, level x/max, and "now → next" stat on each node.
Nodes unlock when their parent node is bought. Branch completion = confetti + small permanent badge.

PLAYER
| Node | Max | Base cost | Growth | Effect |
|---|---|---|---|---|
| Walk Speed | 10 | 15 | 1.6 | 16 → +1.5/lvl |
| Backpack Slots | 6 | 25 | 2.0 | 2 → +1/lvl |
| Jump Power | 5 | 40 | 1.8 | +5/lvl |
| Throw Power | 5 | 45 | 1.8 | throw range 18 → +4 studs/lvl |
| Headlamp | 3 | 200 | 3.0 | light range 20 → 40 → 60 → 80 |
| Lift Speed | 5 | 150 | 1.7 | +20%/lvl |
| Lucky Boots (secret, from Jump Power 3) | 3 | 3,000 | 2.5 | +5% golden chance/lvl |

TOOLS
| Node | Max | Base cost | Growth | Effect |
|---|---|---|---|---|
| Junk Vac (unlock) | 1 | 100 | – | unlocks Vac |
| Vac Tank | 8 | 60 | 1.6 | 20 kg → +15 kg/lvl |
| Suction Power | 4 | 150 | 6.0 | hardness 1 → +1/lvl (max 5); the depth gate: 150 / 900 / 5,400 / 32,400 |
| Suction Radius | 6 | 90 | 1.7 | 3 → +0.6 studs/lvl |
| Blow-out Speed | 8 | 80 | 1.6 | 10 → +6 kg/s/lvl |
| Multi Nozzle | 3 | 3,000 | 3.0 | 1→2→3→4 streams (×stream count speed) |
| Hydraulic Grabber | 1 | 400 | – | grab limit 60 kg |
| Winch (unlock) | 1 | 800 | – | unlocks Winch |
| Winch Speed | 5 | 1,000 | 1.7 | +25%/lvl |
| Magnet (unlock) | 1 | 1,500 | – | unlocks Magnet |
| Magnet Radius | 8 | 500 | 1.5 | 6 → +1.5 studs/lvl |
| Magnet Capacity | 8 | 1,000 | 1.5 | 3 → +1 item/lvl |
| Magnet Strength | 5 | 2,000 | 2.2 | 35 kg → +23 kg/lvl |
| Cutter (unlock) | 1 | 5,000 | – | unlocks Cutter |
| Cutter Speed | 5 | 8,000 | 2.0 | −15% cut time/lvl |

PROCESSING
| Shredder | 5 | 500 | 2.0 | +10% item value/lvl |
| Gold Sorter | 3 | 5,000 | 3.0 | golden ×5 → ×6 → ×7 → ×8 |
| Heavy Bonus | 5 | 1,200 | 2.0 | +2% value per 10 kg/lvl |

FURNACE
| Furnace Heat | 10 | 40 | 1.75 | +15% coins/lvl |
| Wide Mouth | 4 | 300 | 2.0 | furnace catch volume +25%/lvl (easier throws) |
| Combo Burner | 4 | 2,500 | 2.2 | combo cap ×1.5 → ×3.0 |
| Coin Magnet | 1 | 600 | – | coins from the fountain fly to you automatically |

AUTOMATION
| Factory Crane (unlock) | 1 | 1,200 | – | unlocks the factory, Crane on pad 1 |
| Auto Chute | 1 | 4,000 | – | junk dropped in the pit-edge chute burns by itself |
| Helper Drone | 3 | 15,000 | 2.5 | a little drone vacuums the surface layer near you |

SEARCH
| Reader Speed | 5 | 300 | 1.8 | read time 6 s → 1 s |
| Junk Scanner | 3 | 1,000 | 2.5 | pings nearest stick/crate (range 30/60/90) |
| Lucky Finder | 5 | 2,000 | 2.0 | +10% treasure outcomes/lvl |
| Depth Radar | 1 | 20,000 | – | hot/cold meter for the Golden Stick |

FACTORY branch = the factory machines (C10).
Fill the tree to ~60 nodes total by adding a few small-effect nodes in the same style (keep every effect visible;
no invisible +1% nodes — always show "now → next").

### C9. Coins, combos, furnace math (Config.Economy)
- itemCoins = baseValue × layerMult × (1 + shredder) × goldenMult × heavyBonus × furnaceHeat × comboMult × gearPerk × boosts
- Combo: each burn within 2.0 s of the last adds ×0.1 (cap 1.5, raised by Combo Burner). Show "COMBO x7!" text.
- Party share: when you burn, every party member in the same yard also gets +20% of that value as "Team Heat"
  (it's created as a bonus, never taken from you).
- Multipliers from passes and boosts stack ADDITIVELY and are shown clearly in a "Multipliers" panel.
- Coins are whole numbers. Format: 999 → 1.2K → 3.4M → 5.6B.

### C10. Factory (Config.Factory) — persists through Rebirth
12 pads in a chain on the deck. Tap a pad → buy or upgrade. Mobile-friendly: NO free placement. Belts animate between
pads (texture scroll), products ride the belts as small props. Each machine needs the one before it.
| # | Machine | Cost | Income/min | Product prop |
|---|---|---|---|---|
| 1 | Crane | 1,200 | 30 | junk bundle |
| 2 | Sorter Gate | 4,000 | 80 | sorted bins |
| 3 | Scrap Press | 10,000 | 200 | metal plates |
| 4 | 3D Printer | 20,000 | 350 | toy parts |
| 5 | Rolling Mill | 40,000 | 600 | metal rolls |
| 6 | Engine Assembler | 100,000 | 1,400 | small engines |
| 7 | Washer Works | 180,000 | 2,400 | washing machines |
| 8 | Drone Factory | 300,000 | 3,800 | drones |
| 9 | Robot Works | 700,000 | 8,000 | little robots |
| 10–12 | Polisher / Painter / Packer | 1.5M / 3M / 6M | 15K / 28K / 50K | gift boxes |
- Each machine upgrades 5 levels: +50% income/lvl, cost ×2.2 per level.
- Offline income: 50% of the factory rate, max 2 h (8 h with the Night Shift pass). Shown on join as a "Welcome back!"
  card with a big Collect button.

### C11. Sticks, crates, safes, Galleon, Museum
- Mystery Sticks are identical props. Read at the Reader (2 slots; queue). Outcome table (Config.StickOdds; Lucky
  Finder and luck boosts shift weight from "Empty" to the others):
  Empty file (funny filename popup + 2 coins) 55% | Coin cache (layer avg value ×10) 25% | Museum Photo 12% | Key 6% | Gear 2%.
  The Golden Stick is ONE physical stick placed by the server in the jackpot depth band. It looks identical to the
  others until it's read.
  Funny filenames (UI text, not image text): "homework_final_FINAL2", "cat_pictures_4000", "my_secret_recipe",
  "dance_moves_v3", "grocery_list_old" ... write 40.
- First-run guarantee: one Mystery Stick sits in L1 near the deck in the first 90 s and always reads "Coin cache"
  (teaches the Reader early).
- Crates: 15 per yard, Cutter 3 s → coins (×20 layer avg) or a Key (20%) or a Mystery Stick (15%).
- Safes: 5 per yard, need 1 Key + Cutter 6 s → Gear 30% / big coins 50% / Museum piece 20%.
- Buried Galleon (Normal + Hard, at ~85 studs): an old wooden sailing ship's hull, cut in (10 s) → a cargo hold with 3
  chests and a guaranteed Museum piece. The hold has a ship's wheel, barrels and rope coils. (No cannons.)
- Daily Golden Crate: one per yard per player per day, glowing, with a guaranteed Museum piece.
- Museum: 5 sets × 8 pieces (Retro Tech, Toy Box, Sea Treasure, Kitchen Gadgets, Golden Odds). A finished set gives a
  permanent +5% coin perk. Pieces show on pedestals in the Museum building and in the Collection Book UI.

### C12. Golden Stick clear, Rebirth, Gears
- Reading the Golden Stick: 1.5 s slowmo, a golden light beam from the Reader, the music cuts to the fanfare, confetti,
  a server-wide banner "<Name>'s crew found the Golden Stick!", and a big clear screen showing run time, depth,
  treasures and Gears earned.
- Gears earned = floor(10 × yardGearMult × (1 + 0.05 × treasuresFoundThisRun)).
- Every party member in that yard gets the clear. The next Yard tier unlocks.
- Then choose: KEEP GOING (keep coins + tree, the yard re-rolls a new Golden Stick for half Gears) or
  REBIRTH (reset coins + Scrap Shop tree; keep Factory, Gears, Museum, Keys, cosmetics; get the full Gears).
- Gear Perks (Config.GearPerks): +10% coins/lvl (10 lvls, 5 gears × 1.5^lvl), Start with Vac (8), Start with Magnet (25),
  +1 Backpack (15), Faster Lift (10), Second Reader slot speed +50% (20), Sparky's Head Start (start with 500 coins, 12).

### C13. Lobby, parties, difficulty select
- Walk into a Yard Gate ring → a panel: difficulty card (Easy/Normal/Hard with depth, hazards, Gear mult, lock reason),
  "Start Solo", "Start Party (15 s countdown, up to 4)", and a list of open yards you can "Join".
- Party invite: a Party button in the HUD lists players in the server → Invite → they get a toast with Accept.
  Friends get a "Friend" badge. Party leader picks the yard. Leaving the party = return to lobby, keep your progress.
- On start, the server assigns a free plot, generates its terrain + junk for that difficulty, and teleports the party
  (CFrame move, same server). If all 6 plots are busy, solo players can join open yards.
- An ACTIVE yard keeps running while at least 1 member is in it. When empty for 60 s, it's cleaned up.

### C14. Onboarding (first 60 seconds = fun, no wall of text)
Sparky flies next to you. One instruction at a time, a bouncing 3D arrow + a pulse on the right button:
- 0–10 s: you spawn in the lobby, the Easy gate glows → walk in → Start Solo is pre-selected (one tap).
- 10–20 s: on your deck. Junk is piled right next to the furnace. "Tap junk to grab!" → grab 2.
- 20–30 s: "Throw it in the fire!" → coin fountain → "+11". First upgrade button pulses (Walk Speed 15 or
  Furnace Heat 40). Target: first upgrade bought before 30 s.
- 30–120 s: "Dig deeper = better junk!" → buy the Junk Vac at 100 coins (~2 min).
- ~1:30: the guaranteed Mystery Stick → "Read it on the computer!" → Coin cache popup.
- ~4–5 min: Factory Crane (1,200) → "Your factory makes money while you dig!" (first big unlock < 5 min).
- Funnel-log every step with AnalyticsService:LogOnboardingFunnelStepEvent. Tutorial can be skipped in Settings.
  Any step is skipped automatically if the player already did it.

### C15. Controls
- PC: WASD move, mouse aim, LMB use tool, RMB alt action (Blow-out / release), 1–5 tools, F throw, E interact,
  Tab shop, Q drop, M map of the yard, Shift sprint (if enabled).
- Mobile: thumbstick (left), USE button (big, right), ALT/THROW button above it, 5 tool buttons in an arc above jump
  (all ≥ 44 px, no overlap with jump), tap junk to grab, soft auto-aim to the nearest valid target in a 25° cone.
- Console: RT use, LT alt, X throw, Y shop, LB/RB cycle tools, B back, D-pad menus, full GuiService selection support
  (every menu navigable with a gamepad, visible selection outline in accent orange).
- Use ContextActionService. Show button hints that match the current input type (swap on LastInputType change).

### C16. UI screens (all built in code or with clear names; scale-based, with UIAspectRatioConstraint + UISizeConstraint)
- HUD: coins (top-left under the Roblox topbar inset) with "+n" fly-in, Gears + Keys chips, factory "+n/min" (top-right),
  depth meter (right edge, current layer color, Golden Stick band shown once Depth Radar is bought), backpack x/y +
  tank % bars (bottom, above the hotbar), hotbar 1–5, 1-line quest tracker (collapsible), Party button, Store button,
  Back to Deck button. Mobile: hotbar moves to the right arc.
- Scrap Shop: tabs per branch (Player, Tools, Processing, Furnace, Automation, Search, Factory) and inside each, a vertical
  tree with connecting lines (no free panning; mobile-friendly). Node states: locked / available / bought / maxed.
  Detail card: name, level x/max, "now → next", cost, BUY button (hold-to-buy-max on PC/console).
- Reader screen: retro green-on-dark monitor look, progress bar, outcome reveal card.
- Factory pad panel: machine card, income, upgrade button, next machine preview.
- Clear screen + Keep Going / Rebirth choice. Gear Perks screen.
- Museum / Collection Book. Daily Rewards (7-day calendar). Quests (3 daily + 2 weekly). Store (passes + products,
  each showing its exact effect). Settings (music, SFX, graphics quality Auto/Low/High, reduced camera shake,
  first-person toggle, skip tutorial). Party / Yard Gate panel. Welcome Back (offline income). Toasts (max 3 stacked).

### C17. Juice (JuiceController, all toggles respect Settings)
- Coin fountain from the furnace: count scales with value (5–40 coin sprites), arcs toward the HUD coin counter,
  counter ticks up with a bounce.
- Number pop-ups: "+128" at the furnace; color tier by value (white < 100 < green < 1K < gold < 10K < orange rainbow).
- Furnace flame burst scales with item mass; heavy items (≥ 50 kg) add a small screen shake (0.15 s) and a deeper roar.
- Vacuum: particle stream into the nozzle, suction sound pitch rises with tank %, tank full = "ding" + bar bounce + Sparky
  "Tank full! To the fire!".
- Dig: dirt-puff particles, junk wobble before it pops loose.
- Upgrade bought: button squash-and-stretch, sparkle burst, rising chime; maxed = gold frame; branch done = confetti.
- Combo text grows with combo level. Layer banner on new layer. Golden items shimmer.
- Golden Stick: see C12.

### C18. Monetization (honest; Config.Monetization with placeholder IDs; owner creates them)
Rules: show the exact effect before buying; no fake discounts, no fake countdown timers, no paid random items, no
paid power over other players (the game is co-op only). Prices are [ASSUMPTION], tune after launch.
Permanent passes ≈ 10× the matching 15-minute boost.
| Type | Name | Price (R$) | Effect |
|---|---|---|---|
| Dev product | Coin Boost 15 min | 39 | ×2 coins, 15 min (stacks time) |
| Game pass | Double Coins Forever | 399 | +100% coins, permanent |
| Dev product | Lucky Boost 15 min | 49 | ×2 treasure luck on sticks/crates/golden chance, 15 min |
| Game pass | Lucky Digger | 449 | ×2 treasure luck, permanent |
| Dev product | Speed Reader 15 min | 25 | instant stick reading, 15 min |
| Game pass | Instant Reader | 249 | instant stick reading, permanent |
| Game pass | Big Backpack | 149 | +3 backpack slots |
| Game pass | Auto Blow-out | 199 | tank empties into the furnace automatically when near it |
| Game pass | Night Shift | 199 | offline factory cap 2 h → 8 h |
| Game pass | VIP | 299 | +10% coins, gold name tag, VIP lounge in lobby, 1 free daily quest reroll |
| Dev product | Team Heat 15 min | 99 | ×2 coins for EVERYONE in your yard (a gift; name shown in the toast) |
| Dev product | Coin Pack S / L | 49 / 299 | exactly 15 min / 2 h of your current factory income (amount shown before buying) |

### C19. Retention
- Daily reward: 7-day streak calendar (coins → Key → Lucky Boost 5 min → Gears → coins → Key ×2 → Day 7 cosmetic
  "Sparky Trail"). Missing a day drops the streak by 2 days, not to zero.
- Daily quests (3, reset 00:00 UTC): e.g. burn 150 junk, read 8 sticks, open 3 crates, reach 60 studs deep, earn 5K
  coins from the factory. Weekly (2): bigger versions. Rewards: coins scaled to progress, Keys, Gears.
- Daily Golden Crate in every yard (guaranteed Museum piece).
- Offline factory income waiting on return.
- Weekend "Golden Hour" (Sat+Sun, UTC): golden chance 3% → 6%. Announced in the lobby.
- Museum sets = a long-term collection goal.

### C20. Asset list
3D (Blender → FBX → Open Cloud upload → MeshPart). Low-poly, 200–1,500 tris each, one shared palette texture atlas
where possible. Each junk prop also gets a golden material variant (in-engine, not a new mesh).
- Junk props (20): old tire, oil drum, wooden crate (loose), washing machine, fridge, bicycle, traffic cone, old TV,
  car body (heavy), big gear, jerrycan, pipe bundle, bed spring, old sofa, toaster, radio, kettle, desk lamp,
  shopping cart, office chair.
- Treasure: Mystery Stick, Golden Stick (same mesh, golden only after reading), locked crate, safe, golden chest,
  Buried Galleon (hull exterior + cargo hold interior, modular), Museum pedestal.
- Deck: furnace (with mouth + chute), Reader computer desk (retro CRT monitor + keyboard), Scrap Shop terminal, lift
  platform + shaft rails, heavy chute, deck floor tiles, railings, lamp posts, crane gantry.
- Factory: Crane, Sorter Gate, Scrap Press, 3D Printer, Rolling Mill, Engine Assembler, Washer Works, Drone Factory,
  Robot Works, Polisher, Painter, Packer, belt segment (straight + corner) + products (plate, toy part, roll, engine,
  washer, drone, robot, gift box).
- Tools (viewmodels): Grabber Glove, Junk Vac (with tank), Magnet, Cutter, Winch Hook.
- Characters: Sparky (rigged simple bones: body bob, arm wave, eye blink), Rust Rat (run cycle, steal, dizzy).
- Lobby: plaza tiles, 3 yard gates, Museum building, kiosks, leaderboard boards, Sparky statue, junk-art decorations.
- Background: distant junk mountains (low detail), cranes on the skyline.
2D (Vertex AI Gemini image model → pending_review\ → owner OK → upload_image). Positive-only prompt examples:
- "Seamless tileable texture of tightly packed colorful cartoon junk pieces, warm sunset lighting, stylized low-poly
  game art, soft orange and teal tones, top-down view" (PackedJunk; similar ones for RustPack, MachinePack, DeepDump,
  CorePile with deeper and darker tones).
- Icons (512x512, flat stylized, centered object on a plain dark rounded background): coin, gear, key, each tool,
  each shop branch, each machine, each museum piece, daily reward items.
- Game icon + 3 thumbnails: "A cheerful stylized low-poly junkyard at golden hour, a glowing furnace shooting a
  fountain of gold coins, a small round friendly robot with one big eye cheering, kids' game art, vivid warm colors".
The game icon and thumbnails show a scene only, with no lettering.

====================================================================================================
## C-TECH. ARCHITECTURE
====================================================================================================
ReplicatedStorage/Shared: Config (ALL numbers above), Remotes (creates/holds every remote), Format (number formatting),
  Types, Signal.
ServerScriptService/Services: DataService, YardService (terrain gen, carve, lift), JunkService (lazy spawn, pickup, weight),
  ToolService, FurnaceService, UpgradeService, StickService (reader, odds, Golden Stick), TreasureService (crates, safes,
  Galleon), FactoryService (income tick, offline), PartyService, LobbyService, QuestService, DailyService,
  MonetizationService (ProcessReceipt + passes), HazardService (rats, slides), LeaderboardService (OrderedDataStore),
  AntiExploit (rate limits, validation helpers), Bootstrap (start order).
ServerScriptService/Tests: SmokeTest, BalanceSim.
StarterPlayerScripts/Controllers: Input, Tool, Camera, HUD, Shop, Reader, Factory, Party, Juice, Audio, Tutorial, Quality,
  Settings, Store, Museum. Dev/OverlapCheck.
Remotes (all validated + rate-limited, per second): Grab 8, Throw 4, Vacuum 12, BlowOut 4, Magnet 4, Cut 4, Winch 2,
  BuyUpgrade 6, ReadStick 2, FactoryBuy 4, Party 3, Yard 2, ClaimDaily 1, ClaimQuest 2, Settings 2.
- Terrain carving runs on the server (Terrain:FillBall with Air), clamped radius, only inside your yard bounds, only if
  Suction Power ≥ layer hardness.
- Junk spawning is lazy by 16x16x16 chunk, only when a party member is within 24 studs. Max 600 active junk props per
  yard, 2,500 per server. Props are Anchored until grabbed, CanTouch off, CastShadow off when small,
  CollisionFidelity Box.
- QualityController: samples FPS each 2 s; if < 40 → step down (shadows off on props, fewer particles, shorter
  decoration fade distance, lower coin-sprite counts); if > 55 for 10 s → step back up. Settings can force Low/High.

====================================================================================================
## D. BUILD ORDER (milestones, each with a "done when" test; log each in BuildLog + MORNING_REPORT.md)
====================================================================================================
M0 Setup — lock the Studio (marker attribute), folder structure, Config, Remotes, DataService (TEST store), BuildLog,
   live_src\ mirror, SmokeTest.
   DONE WHEN: SmokeTest passes, data loads/saves/locks in a 2-session test, live_src\ matches the place.
M1 Greybox loop — 1 yard, grey parts, terrain pit with 5 layers, Grabber, throw, furnace, coins, 5 upgrades.
   DONE WHEN: in playtest you can grab → throw → earn → buy an upgrade in < 30 s (screenshot proof).
M2 Full toolset + layers — Vac (carve + tank + blow-out), Magnet, Cutter, Winch, hardness gate, lift, Back to Deck.
   DONE WHEN: a playtest bot script digs from 0 to 100 studs with no stuck states and no errors.
M3 Treasure + Golden Stick — sticks, Reader, crates, safes, Galleon, Golden Stick clear, Keep Going / Rebirth, Gears.
   DONE WHEN: a full Easy clear is possible start → finish in one playtest, and Rebirth resets correctly.
M4 Factory — 12 pads, belts, income tick, offline income.
   DONE WHEN: income matches Config within 1% over a simulated 10 min; offline card shows correct capped value.
M5 Real assets — Blender models, uploads, swap greybox for meshes; textures after owner OK.
   DONE WHEN: no greybox left in the main loop; screenshots of deck, pit (each layer), factory, lobby.
M6 UI — every screen in C16, all input types, button hints.
   DONE WHEN: OverlapCheck = 0 on all 6 device targets; every touch target ≥ 44 px; gamepad can reach every button.
M7 Progression + balance — full tree (~60 nodes), Gear Perks, Museum, BalanceSim.
   DONE WHEN: BalanceSim shows first upgrade < 30 s, Vac ≈ 2 min, Factory Crane < 5 min, Easy clear 18–22 min,
   Normal 24–28, Hard 28–32 (fresh player), and a rebirthed player clears Easy in < 12 min. Tune Config until true.
M8 Lobby + co-op — hub, gates, difficulty select, parties, invites, join open yards, Team Heat, plot recycling.
   DONE WHEN: a 3-player local server test (Studio Test > Clients) clears a yard together with shared credit and no
   desync; plots recycle after 60 s empty.
M9 Hazards — Rust Rats, Junk Slides (Normal/Hard only).
   DONE WHEN: hazards never block progress and never trigger on Easy.
M10 Onboarding — Sparky tutorial (C14) + funnel analytics.
   DONE WHEN: a fresh TEST save hits every tutorial step in order within the target times, with no text wall.
M11 Monetization — passes, products, ProcessReceipt ledger, Store UI, multipliers panel.
   DONE WHEN: each product grants exactly once in a Studio purchase test (including a forced retry), passes are
   checked on join + on purchase, and nothing gives power over another player.
M12 Retention — daily rewards, quests, Daily Golden Crate, Golden Hour, leaderboards.
   DONE WHEN: a simulated day rollover (fake os.time offset in TEST mode only) resets quests and advances the streak.
M13 Mobile/console polish — auto-aim, hotbar arc, gamepad selection, haptics (HapticService) on big burns.
   DONE WHEN: screenshots on every device show a clean HUD and you can play the first 5 minutes with gamepad only and
   with touch only (input simulation).
M14 Performance — StreamingEnabled tuning, part budget audit, QualityController.
   DONE WHEN: a 12-player stress test (6 yards active) keeps server heartbeat ≥ 55 and client FPS ≥ 40 on the Low preset;
   active parts under budget (print the counts).
M15 Final QA — run every test, fix, write the report.
   DONE WHEN: section E is all green.

====================================================================================================
## E. FINAL HAND-OFF CHECKLIST (all must be true)
====================================================================================================
[ ] SmokeTest: SMOKE PASS n/n, 0 errors in Output during a 10-min playtest.
[ ] OverlapCheck: 0 overlaps on Phone 20:9, Phone 16:9, Tablet, Console, PC 1080p, PC 768p. Touch targets ≥ 44 px.
[ ] Screenshots saved (screenshots\<device>\...) for: lobby, deck, each layer, Scrap Shop, Reader, factory, clear screen,
    store, daily rewards — on every device.
[ ] BalanceSim report (time to first upgrade, Vac, Crane, Easy/Normal/Hard clear, rebirth clear) pasted in MORNING_REPORT.md.
[ ] DataStore: session lock, autosave, retry, migration tested on the TEST store only. Live store never touched.
[ ] All remotes validated + rate-limited; a quick exploit test (spam, wrong args, far distance) changes nothing.
[ ] Every 2D image was approved by the owner before upload. No banned content (B1) anywhere.
[ ] live_src\ mirror matches the place. BuildLog complete.
[ ] MORNING_REPORT.md: done / broken / next / all [ASSUMPTION]s / the list of game passes + dev products the owner must
    create on the website (name, price, description, which Config key to paste the ID into).
[ ] Then say to the owner, exactly: "SAVE NOW (Ctrl+S) + PUBLISH"
````
