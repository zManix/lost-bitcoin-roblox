# SPEC: "FIND THE GLOWING BOX" (Roblox)

Source of truth for the build. You have never seen any earlier conversation. Mechanics and mood are inspired by the
Steam game "Find The Box" (Taco Games, releasing Nov 4, 2026). Copy its MECHANICS and its overall LOOK (palette,
lighting mood, composition). NEVER copy its assets, names, card names, text or logo. All models, textures, names
and text must be our own.

## 0. Why this game (protect these when you make trade-offs)
- Proven on Roblox: "Search For The Needle" (find one hidden needle in a giant haystack, beat your best time)
  launched 2026-08-23. It peaked at 86K concurrent players with 95.7% likes, then fell to about 6K. "Find the hidden
  thing" pulls huge numbers but people drop off fast. "Dig to Escape" (dig to find a secret tunnel) has 607M visits.
- Our edge: the RETENTION LAYER that Needle lacks, taken from Find The Box: a level-up card pick (choose 1 of 3) for
  crazy builds, a Daily Cube, global speedrun leaderboards, cube sizes, Normal/Hard, upgrades on/off, buried Specials,
  a persistent cube. Roblox additions: co-op cubes with friends, a Box Buddy collection, and cosmetic gloves.
- Nothing like this exists on Roblox today (checked live on 2026-10-26).
- TIMING: the Steam game launches Nov 4. If it goes viral, "find the box" searches will spike on Roblox. Be first.
- The last build failed because it was ugly and boring while passing 771 tests. This time LOOKS and FUN are graded
  first: see section 9 (Visual QA) and section 10 (Fun QA).

## 1. Pitch
"There's a glowing box hidden inside a giant cube of a million blocks. Punch your way in and find it. Go slow and cozy,
or level up and pick crazy powers to tear the cube apart. Race the world on the leaderboards, or dig with friends."

## 2. Look (match the style_refs folder — open and study every image before building anything visual)
- **Camera:** FIRST PERSON (CameraMode LockFirstPerson). Two big chunky cartoon GLOVED fists as the viewmodel (our own
  design: thick dark ink outline, soft cel shading, cream glove with a colored cuff). Punch animation: a fast jab with
  a squash on impact, alternating hands.
- **The Hall (hub):** a quiet candlelit spa hall. Dark walls with warm uplight strips, glossy dark floor tiles with
  light seams, dozens of small candles (warm PointLights) and cushions. The giant CUBE sits in the middle on a low
  plinth. A circular glowing pool / portal is the exit after a find.
- **Blocks:** 4-stud cubes with a smooth stone texture, faint dark crack veins, and thin LIGHT SEAMS on every block edge
  (the white grid look in the refs). Block faces show a subtle hand-drawn ink line. Inside tunnels the light comes
  from embedded candle discs (small glowing round lamps set into the walls), not from the sky.
- **Depth bands:** the color of the whole world changes as you get closer to the box (distance to the box, in 5 bands):
  | Band | Walls | Shadow / ambient | Mood |
  |---|---|---|---|
  | B1 outer | warm sand-brown #B07A4A | #3A2416 | cozy spa |
  | B2 | rose-magenta #C2185B | #5A1030 | dreamy |
  | B3 | lemon-gold #E8C547 | #6B4A10 | bright |
  | B4 | night-blue #3D4FB8 | #141A40 | calm night |
  | B5 near box | mint-green #3FBF8A | #0F3A2A | magical |
  Tween ColorCorrection tint + ambient when you cross into a band (1.5 s), and show a quiet band name ("rose layer").
- **The Glowing Box:** a cube with a mint-white cracked-crystal / cell-pattern texture, a strong glow (Neon parts +
  PointLight + bloom), a slow bob and a soft hum.
- **Tokens:** cream-white glowing discs with a dark ink outline. They pop out of broken blocks, hover for a moment,
  then fly into you with a rising "tick".
- **UI:** dark translucent teal-black panels, thin gold accents, a clean thin sans font (Gotham / Montserrat), lowercase
  cozy flavor lines ("take your time.", "it's somewhere."). Bottom center: level bar + 4 spell slots. Bottom-left:
  timer pill. Bottom-right: the next passive / charge meter. Top-center: progress / hint chip.
- **Level-up cards:** 3 tall cards with an art circle, a name, a rarity label, short text, a NEW / UPGRADE tag;
  Reroll (n) and Skip buttons. Rarity colors: Common teal-green, Rare blue, Epic purple, Legendary gold glow.
- **Lighting:** Technology Future (ShadowMap on Low). Bloom Intensity 1.0, Threshold 0.9, Size 24. Mild DepthOfField
  in the hub only. No sky inside the cube. Each band has its own ColorCorrection.

## 3. Core loop
- Seconds: look at a block → PUNCH (click / tap / RT) → crack decal (hit 1) → break with chips + dust + a pitch-varied
  "tock" → tokens fly to you.
- Minutes: tokens fill the level bar → LEVEL UP → pick 1 of 3 cards → your build gets crazier (more blocks per
  second, companions tunnelling, bigger blasts) → hints say "closer" / "further" → buried Specials → band colors
  change → the box.
- Session: break the last block around the box → slow-mo → the box opens → a BOX BUDDY pops out → the timer stops →
  leaderboard → gems → a new cube, or the Daily Cube tomorrow.

## 4. Modes (Config.Modes)
- Cube sizes: STANDARD 100³ = 1M blocks (start) · LARGE 126³ ≈ 2M (unlock: find 1 box in Standard) · VERY LARGE
  159³ ≈ 4M (unlock: 1 box in Large). HUMONGOUS 200³ = 8M is a later update (flag off).
- Difficulty: NORMAL (hints on) · HARD (no hints).
- Upgrades ON (roguelite cards, default) · PURE (just fists; own leaderboards).
- BOXLESS: no box; clear X% of the cube as fast as you can (Standard 50%, Large 35%, Very Large 25%).
- DAILY CUBE: the same seed for everyone each UTC day; the first finished attempt per day is ranked.
- SEEDS: type a seed to race a friend on the same cube (unranked).
- SOLO or PARTY (up to 4 friends dig the same cube; party leaderboards are separate).

## 5. The cube engine (the biggest technical risk — build and prove it first, in M1)
- **Grid:** server-authoritative `buffer` per cube, 1 byte per cell (0 = air, 1–5 = band material, 10+ = special/box
  parts). A Standard cube is 1 MB. Block size 4 studs, so the cube is 400 studs wide. The player fits a 1×2 tunnel.
- **Rendering (client-only parts, never replicated):** split into 16³ chunks. For each chunk, GREEDY-MESH the exposed
  faces: merge coplanar exposed cells into the largest boxes possible, one Part per merged rectangle (slab thickness
  1 block). An untouched cube renders as about 240 big slabs. Re-mesh only the touched chunk (+ neighbors on a border)
  within one frame budget (≤ 4 ms; spread over frames if needed). Only mesh chunks within 160 studs of the camera; the
  far outer shell stays as big slabs. Use a pooled set of Parts with a SurfaceAppearance/texture per band;
  CastShadow off on small slabs.
- **Collision:** client parts collide with the local character (characters are client-simulated). The server
  sanity-checks positions: a player standing inside solid cells for > 1 s is nudged to the nearest air cell.
- **Digging:** client raycast → remote Dig(cellIndex, toolId). Server checks: the cell is solid, within reach
  (≤ 3 blocks for fists; more for spells), rate limits (punches per second from your build), the cube owner/party.
  Then it sets air, awards tokens, and broadcasts the changed cells in batches to the party (UnreliableRemoteEvent
  for visuals, a reliable diff every 0.5 s as the source of truth).
- **Generation (seeded):** pick the box cell at least 20 blocks inside the surface; carve the BOX ROOM (5³, glowing
  walls); place 8–12 SPECIAL ROOMS (section 7) at random depths; set band ids by distance to the box.
- **Persistence:** "every hole stays dug". Save each player's active cube per size as seed + an RLE-encoded dug
  bitset (base64) in its own DataStore key; autosave every 60 s and on leave. Resume puts you where you left off,
  with the timer paused.
- Tests: CubeTest (mesh correctness on random dig patterns: no holes, no z-fighting, collision matches the grid),
  PerfTest (dig 20 blocks/s for 5 minutes on emulated phone: FPS ≥ 45, part count ≤ 6,000).

## 6. Leveling, cards, spells, perks, companions (Config.Cards) — Upgrades ON only
- Tokens: 1 per block (×1.0 B1 → ×1.5 B5), Specials burst 50–200. Level thresholds: need(L) = round(12 × 1.1^(L-1))
  [ESTIMATE; BalanceSim tunes]. Target: Level 1 within 20 s, a card pick about every 30–60 s early.
- LEVEL UP: 3 cards slide in (the world keeps running: it's multiplayer). Pick with a click/tap or 1/2/3. Reroll ×3
  and Banish ×3 per run. Auto-pick the left card after 20 s if ignored.
- Card types: SPELL (active, takes one of 4 hotbar slots, cooldown, keys 1–4 / tap), PERK (passive), COMPANION
  (helpers), UPGRADE (levels an owned spell/companion).
- Launch spells (12, our names): SHOCKWAVE PUNCH (next punch breaks a 3×3×3), CHAIN CRACK (cracks spread to touching
  blocks), BORE BEAM (drills a 1×2 tunnel 15 blocks forward), BOMB (throw; 5³ blast), FLARE (lights 40 studs and
  pings Specials), RUMBLE STOMP (breaks the floor in a 5×5 under you), JET BOOTS (hold jump to fly up 3 s), GRAVITY
  WELL (pulls tokens), TIME BREATH (+2 s cooldown refresh), MOLE CANNON (fires a mole that bores a long tunnel),
  ECHO PULSE (Normal: points to the box for 3 s; Hard: disabled), CONFETTI BLAST (big radius, low damage, huge juice).
- Perks (40): punch speed +10% · reach +1 · fists break 2 blocks in a line · crit punch 10% (3×3) · tokens +10% ·
  sprint · slide · wall climb 1.5 s · wall jump · double jump · longer slide · token magnet radius · cooldowns −10% ·
  spell charges +1 · every 50th block = free Shockwave · bombs leave cracks · beams are wider · moles +1 · moles faster
  · lucky blocks (1% break bursts with tokens) · golden blocks appear (×5 tokens) · Special radar · "closer" hint every
  1.5 s · band bonus tokens · aftershock (each block breaks −0.1 s off cooldowns) · and 15 more of the same style
  (keep each effect visible, show "now → next").
- Companions (4): MOLELINGS (little moles dig short tunnels ahead of you), DRILL MOLE (one big mole digs long
  straight tunnels), LANTERN BUGS (light and collect tokens), BUILDER BEES (break blocks around you slowly).
  Upgrades: +1 count, speed, size.
- Movement baseline: walk 16, jump. Sprint/slide/wall moves come from perks (on in Pure only when unlocked as
  permanent meta perks — see 8).

## 7. Specials and hints
- 8–12 SPECIAL ROOMS per cube, with our own whimsical shrines: a frog lantern, a sleepy cat statue, a snail on a
  cushion, a teapot garden, a tiny moon room, a rubber-boot fountain, a paper-crane mobile, a mushroom grove, a
  clock with no hands, a goldfish bowl. Each gives a token burst, a free card pick, an Index entry, and one quiet
  flavor line (ours, e.g. "it was waiting for someone.", "the clock forgot what time it is.").
- NORMAL hints: a top-center chip compares your distance to the box every 3 s → "closer" / "further" (soft color
  pulse). Within 12 blocks of a Special: "special · 9 m" with a direction arrow. HARD: no hints at all.
- BOXLESS: a top-center progress bar "123,456 / 500,000 · 24.6%".

## 8. Meta progression (permanent, saved) — the retention layer Needle lacks
- GEMS: from finding boxes (Standard 20, Large 40, Very Large 80; Hard ×1.5; Daily ×2), Specials (2), daily login,
  quests, group reward (50 once), codes.
- BOX BUDDIES: every found box contains a Box Buddy (a cute creature curled up in a box) rolled from a free rarity
  table (Common 55 / Uncommon 25 / Rare 12 / Epic 6 / Legendary 1.8 / Secret 0.2; harder modes shift the odds up,
  shown in the Index). 30 at launch. They live in your BUDDY SHELF in the Hall (visible to everyone in the server)
  and one can sit on your shoulder in the hub. No stat power (keeps leaderboards fair).
- UNLOCKS (gems): expand the card pool (new spells/perks/companions enter the pool), permanent movement (sprint,
  slide, wall jump) for Pure mode, new Hall decorations, cube themes (cosmetic block skins for unranked runs).
- Index: Specials found, Box Buddies, cards seen. Rewards every 10 entries.
- Daily: login streak (gems), 3 quests (find a box, dig 5,000 blocks, find 3 Specials, play the Daily Cube), and the
  Daily Cube itself.

## 9. VISUAL QA (mandatory loop — this is what failed last time)
- Before any visual work, open EVERY image in style_refs\ and write STYLE_NOTES.md (palette, light sources, seams,
  hands, UI layout, glow) in your own words.
- After every visual change: screen_capture the same view types as the refs (hub with the cube, tunnel B1, tunnel B2,
  card pick, box find, HUD) and save to visual_qa\<step>\. Score each against the refs 1–10 on: palette, light mood,
  block texture + seams, viewmodel hands, UI cards/HUD, glow + juice. Log the scores in VISUAL_QA.md.
- An area is DONE only when its average is ≥ 8 AND it would look good as a Roblox thumbnail. If it scores < 8, list
  what's off and fix it before moving on. Never mark visual work done on "it works".
- The refs are for mood only: never upload them, trace them, or copy their pixels, names or text.

## 10. FUN QA (mandatory)
At every milestone, play 3 real minutes (input simulation) and log in FUN_QA.md:
- Is there visible feedback on EVERY punch (crack, chips, sound, tiny camera kick)? Must be yes.
- Time to first token / first level / first card pick: targets 2 s / 20 s / 20 s.
- Is there a new choice or surprise at least every 60 s in the first 10 minutes? Must be yes.
- The three best moments and the three dullest moments. Fix the dullest before moving on.

## 11. Juice
- Punch: impact squash on the fist, crack decal, 6–10 chips with gravity, dust puff, randomized "tock" pitch, 2-frame
  hit stop on a break, a tiny camera kick.
- Shockwave/bomb: shock ring, chunk chips, bass thump, small shake (respect Reduced Motion).
- Tokens: pop, hover 0.2 s, swoop to the player, tick sound rising in pitch within a combo.
- Level up: a whoosh + time-slow 0.3 s (local visual only), cards slide in with a sparkle edge.
- Band change: color wash + soft chime + band name. Special found: shrine light-up + harp + flavor line.
- BOX FOUND: last block → 0.6 s slow-mo, box glow flare, white flash, hum swells, confetti, timer freezes big in the
  middle, leaderboard rank pops, the Box Buddy reveal (rarity color beam), music sting.

## 12. Roblox structure
- One place, MaxPlayers 8. THE HALL is the hub. Each player (or party) gets their own CUBE INSTANCE placed far apart
  (2,000 studs); clients only mesh their own cube.
- Hall stations: CUBE PORTAL (mode select panel: size, difficulty, upgrades on/off/pure, boxless, daily, seed, solo or
  party), LEADERBOARD WALL (size × mode × difficulty × solo/party × today/week/month/all time; Daily board), BUDDY
  SHELVES, store kiosk, daily gift, the group/codes board.
- Party: invite from the portal panel or join a friend's open cube; all members share the dig, tokens are per player,
  each picks their own cards, the find counts for everyone.

## 13. Controls
- PC: mouse look, LMB punch (hold = auto-punch), 1–4 spells, Space jump (wall jump), Shift sprint, C slide, Tab
  leaderboard, E interact.
- Mobile: thumbstick (left), drag-to-look (right half), big PUNCH button (right, ≥ 90 px; hold = auto-punch), 4 spell
  buttons in an arc above it, a jump button, a slide button; soft aim assist snaps to the nearest block face under the
  crosshair. Card picks are big tappable cards.
- Console: RT punch, LT/RB/LB/Y spells, A jump, B slide, X sprint toggle, View leaderboard; full GuiService selection.

## 14. Monetization (honest; placeholder IDs; create the real ones via Open Cloud)
Rule: RANKED runs (Daily, all leaderboard runs) ignore every paid boost; boosts only work in CASUAL (unranked) runs,
and the mode panel says so. No paid random items. Cosmetics are the main shop.
| Type | Name | R$ | Effect |
|---|---|---|---|
| Pass | VIP | 249 | gold name, VIP lounge in the Hall, exclusive glove, +10% gems |
| Pass | 2x Gems | 99 | double gems |
| Pass | Glove Locker | 199 | 6 glove skins (fire, galaxy, candy, gold, cloud, neon) |
| Pass | Box Effects | 149 | 4 box-find effects (fireworks, petals, stars, bubbles) |
| Pass | Lucky Cards (casual) | 199 | level-ups show 4 cards in casual runs |
| Pass | Starter Spell (casual) | 249 | start casual runs with a chosen unlocked spell |
| Pass | Extra Rerolls (casual) | 149 | +3 rerolls in casual runs |
| Product | Token Rush 15 min (casual) | 29 | ×2 tokens in casual runs |
| Product | Single glove skins | 49–99 | cosmetic |

## 15. Tech architecture
ReplicatedStorage/Shared: Config, Remotes, Format, Grid (cell index math), Mesher (greedy, pure), CardDefs, Odds, Signal.
Server services: DataService (reuse), CubeService (grids, gen, dig validation, persistence), PartyService (reuse/adapt),
CardService (levels, offers, picks), SpellService, CompanionService, SpecialService, BoxService (find, buddy roll),
LeaderboardService (OrderedDataStore per board key + period), DailyService, QuestService, MonetizationService (reuse),
AntiExploit (reuse), LiveEventService (reuse), Bootstrap.
Client controllers: Viewmodel (fists), Input, CubeRenderer (chunks + mesher + pool), Dig (raycast, aim assist), HUD,
Cards, Spells, Juice, Bands (color), Hall, Leaderboard, Store, Tutorial, Quality, Settings. Dev/OverlapCheck (reuse).
Tests: SmokeTest (reuse harness), CubeTest, PerfTest, OddsTest, BalanceSim.
REUSE from the previous project folder (%USERPROFILE%\Desktop\ScrapAJunkyard\live_src): DataService (session lock,
retries, migrations), MonetizationService (receipts, PolicyService), AntiExploit, SocialService (friends, invites,
group, codes), LeaderboardService, LiveEventService, OverlapCheck, QualityController, the SmokeTest harness.
Adapt them; don't rewrite them. All build time goes into the cube, the look and the fun.

## 16. Onboarding (first 60 s)
- Spawn in the Hall facing the giant glowing-edged cube. One line: "there's a box in there. find it." The portal
  glows → tap → Standard · Normal · Upgrades ON is preselected → GO (two taps total).
- First punch within 5 s (a pulsing PUNCH button / "click to punch" chip). Tokens fly at once. Level 1 within 20 s →
  the first card pick, always containing SHOCKWAVE PUNCH → instant power fantasy.
- "closer / further" explained by a single chip the first time it appears. Nothing else is explained in text.

## 17. Balance targets (BalanceSim must prove them)
- Standard Normal, upgrades ON, average player: box found in 15–25 min. Pure Standard: 30–45 min.
- First card ≤ 20 s; a card about every 30–60 s for the first 10 minutes, then about every 90 s.
- Daily Cube Standard: top players about 6–8 min (leaderboard spread).

## 18. Safety
No skulls, blood, gore, robed or hooded figures, religious symbols, weapons aimed at anything, text in images, real
brands. Fists only punch blocks. Gems and boxes are never sold for Robux.
