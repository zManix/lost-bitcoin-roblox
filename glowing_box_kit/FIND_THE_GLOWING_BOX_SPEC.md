# MASTER SPEC: "FIND THE GLOWING BOX" (Roblox, first person)

This is the source of truth. You have never seen any earlier conversation. Read it fully, then read FTB_STUDY.md
(the deep study of the original) and look at EVERY image in style_refs\.

Mechanics and mood are inspired by the Steam game "Find The Box" (Taco Inc, Nov 4, 2026). Copy its MECHANICS, its
UI LAYOUT IDEAS and its overall MOOD (palette, lighting, composition). NEVER copy its assets, names, card names, text,
logo, or its hairy-hand art. Every model, texture, name and line of text is ours.

=====================================================================================================================
## 0. WHY THIS GAME + WHAT FAILED LAST TIME (protect these in every trade-off)
- Proven on Roblox: "Search For The Needle" (find one needle in a giant haystack, beat your time): 86K peak
  concurrent players (Sep 2026), 95.7% likes, 117M visits. It then dropped to about 6K because it has no long-term
  layer. "Dig to Escape" (dig to find a secret tunnel) has 607M visits. No Find-The-Box-style game exists on Roblox
  (checked live on 2026-10-26).
- Our edge, the retention layer Needle lacks: roguelite card builds, Risks, a Collection, Daily Cube, leaderboards,
  cube sizes, buried Specials, a persistent cube, Box Buddies. Plus Roblox social: a SHARED SPACE WITH GHOSTS and an
  hourly LIVE RACE.
- The last 10-hour build passed 771 tests and the owner called it "ugly and boring". So LOOK and FEEL are graded
  first (§16 Visual QA, §17 Fun QA). Tests are necessary but never enough.

## 1. PITCH
"There's a glowing box hidden inside a giant cube of a million blocks. Punch your way in and find it. Go slow and
cozy, or level up and pick crazy powers to tear the cube apart. Everyone in your server is digging too: you'll see
their ghosts drifting through the rock. Race them, or just relax."

## 2. THE SHARED SPACE (the Roblox twist; nothing interferes)
- ONE place, MaxPlayers 10. ONE Hall. ONE cube location in the world. Every player (or party) digs their OWN private
  copy of the cube in that same spot.
- Your client renders ONLY your own blocks. Other players appear as GHOSTS: softly glowing, semi-transparent
  silhouettes (their aura color is a cosmetic) drifting through "your" solid rock as they move through their own
  tunnels. No collision between players (CollisionGroup "Players" doesn't collide with itself). You never see their
  blocks, tokens or debris.
- Party (up to 4 friends): a party SHARES one grid (true co-op digging, you see each other's tunnels and the same
  box). Everyone else is a ghost.
- SHARED MOMENTS (visible to everyone in the server, through the rock):
  - BOX FOUND: a tall column of light shoots up from the finder's position through the cube to the Hall ceiling for
    6 s, with a soft chime for everyone and a top banner "Mira found the box · 12:34".
  - LEGENDARY PICK: a gold sparkle burst over that player's ghost.
  - TOKEN GEODE CRACKED: their ghost sprays shiny particles for 2 s.
  - EMOTES: wave, point, cheer (radial menu); visible on ghosts.
  - Ghost NAME TAGS fade in within 30 studs; level shown small ("Lv 23").
- LIVE RACE (the event, every hour at :00 and :30 server time, 20 minutes max): the Hall announces "Live Race in
  2:00". Players who join get the SAME seed (Standard, Normal, upgrades ON), private grids, and start together on a
  countdown (3-2-1-PUNCH). A live race sidebar (top-right) shows positions by "distance to box" (rank only, not the
  numbers). The first finder gets the winner beam (gold); the top 3 get gems and a race badge. Ranked separately.
- DAILY CUBE: the same seed for everyone each UTC day; ghosts of anyone else playing the Daily show up in your cube.
  The first finished attempt is ranked.

## 3. CORE LOOP
- Seconds:
  - look at a block → PUNCH (alternating fists)
  - hit 1 cracks it, hit 2 breaks it (B1; harder bands take 3)
  - the block pops out as a small tumbling cube that falls and fades
  - tokens spray out and fly into you
- Minutes: the token bar fills → LEVEL UP → pick 1 of 3 cards → your build grows → "closer / further" steers you →
  Specials surprise you → band colors shift as you near the box.
- Session: break into the BOX ROOM → slow-mo → the box opens → a BOX BUDDY pops out → the timer stops → rank and gems →
  next cube / Daily / Live Race. Every hole stays dug if you leave mid-run.

## 4. MODES (Config.Modes)
| Mode | Detail |
|---|---|
| Size | STANDARD 100³ = 1M (start) · LARGE 126³ ≈ 2M (unlock: find 1 Standard box) · VERY LARGE 159³ ≈ 4M (unlock: 1 Large box) · HUMONGOUS 200³ = 8M (flag off at launch) |
| Difficulty | NORMAL (hints) · HARD (no hints at all) |
| Upgrades | ON (roguelite cards) · PURE (fists only, own boards) |
| Goal | FIND THE BOX · BOXLESS (clear Standard 50% / Large 35% / Very Large 25%) |
| Daily Cube | daily seed, first attempt ranked |
| Live Race | §2 |
| Seeds | type a seed, unranked |
| Casual | any run with paid boosts on is unranked (§15) |

## 5. LOOK (match style_refs mood; our own art)
- **Camera:** first person (CameraMode LockFirstPerson), FOV 80 (setting 70–95). Tiny head-bob when walking, kick on
  punch, a FOV punch on spells. Crosshair: a tiny hollow circle.
- **Fists (viewmodel):** chunky cartoon GLOVES (cream glove, colored cuff, short sleeve), a baked dark ink outline +
  light cross-hatch shading in the texture, plus an inverted-hull outline shell. Alternate jabs about every 0.25 s
  (scaled by punch speed): 0.06 s extend with a slight overshoot, a squash on impact, 0.12 s return. The idle fists
  bob and breathe. Glove skins are cosmetics.
- **Blocks:** 4-stud cubes. Texture: a smooth matte face with faint dark marble veins, a thin cream seam line on all 4
  edges, a subtle inner bevel shade; ±6% brightness variation per block (seeded) so the grid reads. Hit 1 = a crack
  decal. Embedded LAMPS: 1 in 18 surface-exposed blocks shows a round glowing disc (cream-white emissive + a small
  PointLight, max 24 active lights near you) — the main light in tunnels.
- **Depth bands** (by distance to the box, 5 bands; each tweens ColorCorrection tint, Ambient, OutdoorAmbient, block
  tint and lamp color over 1.5 s, with a quiet band name toast):
  | Band | Block tint | Ambient | Lamp | Mood |
  |---|---|---|---|---|
  | B1 Sandstone | #A8794D | #3A2416 | #FFE2B0 | cozy spa |
  | B2 Rose | #B0185A | #4A0E28 | #FFB3D9 | dreamy |
  | B3 Honey | #D8B23A | #5A4410 | #FFF3B0 | bright |
  | B4 Night | #3D4FB8 | #121838 | #CFE0FF (+ tiny star dots in the texture) | calm |
  | B5 Mint | #3FBF8A | #0E3426 | #D8FFE9 | magical, the box is near |
- **Hall (hub):** a quiet candlelit spa hall. Dark warm-brown walls with cream uplight strips at the top, a glossy dark
  tile floor with thin light seams, hundreds of tiny candles (pooled, a few real lights), cushions, low plants. The
  GIANT CUBE on a low plinth in the middle, its outer face lit by warm spotlights. A circular glowing pool where you
  emerge after a find. The LEADERBOARD WALL, BUDDY SHELVES, RACE GATE, STORE alcove.
- **The Glowing Box:** a 1-block cube in a 5³ BOX ROOM with mint-teal glowing tiles. White-mint cracked-cell
  (Voronoi) texture, emissive glow, a PointLight, a slow bob and a hum.
- **Tokens:** cream discs with a thin olive ink rim, emissive; they pop, hover 0.15 s, then swoop into you. Pool 300;
  above that, merge into bigger "x5" discs.
- **Lighting:** `Lighting.Technology` is deprecated. Use `LightingStyle = Soft` (+ PrioritizeLightingQuality on High
  preset), EnvironmentDiffuseScale 0–0.3, EnvironmentSpecularScale 0. Bloom Intensity 0.9, Threshold 0.85, Size 28. No
  sky inside the cube (it's dark; lamps light it). Hall: a soft DepthOfField.
- **UI style:** near-black teal panels (#0E1A1C, 88%) with 1 px gold rims (#E8B45A at 50%). Titles in a thin,
  wide-tracked geometric caps font (Roblox: Montserrat Light / Gotham; LetterSpacing via spaces if needed); body text
  in a clean sans. Cream text #F2E6D0. Gold pills for selected filters; a cyan pill (#5BE0F0) for the active mode.
  Gentle lowercase flavor lines ("take your time.", "it's somewhere.", "are you happy yet?" is THEIRS: write our own).

## 6. HUD (in a run)
- Bottom center: a "Lv N" pill with a thin gold XP bar; directly under it 4 square SPELL SLOTS (keys 1–4) with icon,
  charges "x2", a dark cooldown sweep + seconds number, and the selected slot in cream-gold.
- Bottom right: a PASSIVE TAB (icon + name of your newest/ready ability + a colored charge line).
- Bottom left: a TIMER pill (mm:ss; pauses in the Hall and when you leave).
- Top center: the HINT CHIP (Normal): "‹ closer ›" in warm green / "‹ further ›" in soft red, pulsing on change.
  Boxless: a PROGRESS PILL "173,396 / 500,000 · 34.6%".
- Above the level bar: a TOOLTIP PILL for flavor and Special names, plus "special · 8 m" with a small arrow.
- Top right (Live Race only): a race sidebar (positions, avatars).
- Mobile: a big PUNCH button bottom-right (≥ 96 px, hold = auto-punch), 4 spell buttons in an arc above it, JUMP and
  SLIDE buttons; the level bar + slots move up so nothing overlaps the thumbstick or buttons.

## 7. LEVEL-UP CARDS (the heart of the roguelite)
- Tokens: 1 per block × band multiplier (B1 1.0 → B5 1.6), Specials 50–300, Token Geodes 400–1,200.
  need(L) = round(10 × 1.09^(L-1)) [ESTIMATE; BalanceSim tunes]. Lv 1 within 15 s. Mid-run levels every 30–90 s.
- Level-ups BANK: a pulsing "cards ×N" pill; the player opens the screen (Tab / tap / gamepad Y). Never auto-open.
- LEVEL UP: a whoosh + 0.3 s local time-slow (visual only); the screen blurs and darkens behind; the title
  "L E V E L  U P !" and "level 27 · pick one" appear; 3 cards rise in with a staggered 0.08 s spring and a rarity glow.
  The world keeps running (multiplayer), which is fine because nothing can hurt you. No auto-pick; a "later" button.
- Card anatomy:
  - top: "DEPTH I/II/III" with dash ornaments
  - a category dot + label
  - a round medallion with a flat icon and a wavy liquid line crossing the card
  - rarity label, NAME, a 1–2 line description, a stat line "now → next"
  - a bottom tag: NEW PERK / NEW SPELL / UPGRADE / RISK
  - under each card: "banish (n)"
  - bottom bar: "reroll (2)" "skip"
  - hint: "tap a card to take it · banish removes it for this run"
- Rarity glow: Common #1F5A55, Rare #22C27A, Epic #8A4DFF, Legendary #F0A830 (Legendary cards shimmer).
- Rarity odds per offer slot (luck shifts them): Common 62 / Rare 26 / Epic 10 / Legendary 2. Taking an owned card
  again raises its DEPTH (I → II → III; max III).
- Rerolls 2 per run (+ perks), banishes 3 per run, skip gives +10% of the level's tokens.

### 7a. SPELLS (12; active, hotbar, cooldowns, charges)
| Name | Cat | Effect (I → II → III) | CD |
|---|---|---|---|
| MEGA FIST | Blast | next punch breaks a 3³ → 4³ → 5³ cube | 6 s, 2 charges |
| POP BOMB | Blast | throw; 5³ blast → 6³ → 7³ | 8 s |
| BORE BEAM | Digger | 1×2 tunnel forward 15 → 25 → 40 blocks | 10 s |
| QUAKE STOMP | Blast | breaks 5×5×2 below you → 7×7×2 → 9×9×3 | 9 s |
| MOLE CANNON | Companions | fire a mole that bores 30 → 45 → 60 blocks in a wobbly line | 12 s |
| FLARE | Utility | lights 40 studs for 20 s and pings Specials in range | 15 s |
| SKY BOOTS | Motion | hold jump to fly up for 2 → 3 → 4 s | 8 s |
| TOKEN VORTEX | Economy | pulls all tokens in 30 studs for 5 s; +15% → +25% → +35% tokens | 20 s |
| ECHO PING | Utility | (Normal only) a 3 s arrow to the box → 4 s → 5 s | 30 s |
| CONFETTI CANNON | Wild | a cone that breaks 8 → 12 → 16 blocks randomly with huge confetti | 7 s |
| REWIND | Caster | refresh all other cooldowns | 45 → 38 → 30 s |
| GRAVITY DROP | Motion | slam straight down breaking a 2×2 column of 6 → 10 → 14 | 10 s |

### 7b. PERKS (48; passive) — keep every effect visible, show "now → next"
- DIGGER: Quick Jabs (+12% punch speed) · Long Reach (+1 block reach) · Double Tap (punches break 2 in a line) ·
  Crit Fist (10% chance to break a 3³) · Soft Rock (−1 hit on hard bands) · Wide Swing (punches also break 1 to the
  side, 25%) · Crack Spread (20% chance a broken block cracks a neighbor) · Corner Cutter (diagonal punches).
- MOTION: Jog (+8% speed) · Sprint (Shift) · Slide (C) · Wall Climb (1.5 s) · Wall Kick (jump off walls) · Double Jump
  · Air Dash (punch the air while airborne to dash) · Feather Fall · Ledge Pop (auto-climb 1 block).
- BLAST: Bigger Booms (+1 radius) · Chain Reaction (blasts can trigger a second small blast) · Shock Knuckles (every
  25th block = a free 3³) · Echo Blast (blasts repeat at 50% after 0.5 s).
- CASTER: Quick Cast (−10% cooldowns) · Extra Charge (+1 charge to your newest spell) · Aftertaste (each broken block
  −0.05 s on cooldowns) · Overflow (casting with full charges gives +10% tokens for 5 s).
- ECONOMY: Shiny Eye (Specials glint through rock from 20 studs and pay +25%) · Lucky Blocks (1% of blocks burst for
  ×20 tokens) · Golden Veins (golden blocks appear: ×5 tokens) · Token Magnet (+50% pickup radius) · Interest (+1% of
  your tokens per minute) · Greedy Fists (+10% tokens, −5% punch speed).
- UTILITY: Warm Compass (hints every 1.5 s) · Special Radar (shows the nearest Special distance at 30 studs) · Reroll
  Plus (+1 reroll) · Banish Plus (+1 banish) · Night Eyes (brighter tunnels).
- COMPANIONS: Moleling Burrow (+2 molelings) · Mole Speed (+20%) · Big Mole (drill mole size +1) · Lantern Swarm (+3
  lantern bugs) · Bee Hive (+2 busy bees).
- WILD: Coin Flip (every level 50%: +1 extra card choice or nothing) · Pinball (bombs bounce once) · Party Popper
  (every 100 blocks: confetti + 50 tokens) · Butterfly Fists (punches leave glowing butterflies that break 1 block
  each later).
### 7c. RISKS (6; opt-in, appear sometimes as offers; each Risk owned = +12% tokens, shown)
Heavy Gloves (−15% punch speed) · Short Fuse (spells −1 charge) · Foggy (view distance 60 studs) · Quiet Compass
(hints every 6 s) · Butterfingers (5% punches miss) · Night Shift (lamps dimmer).
### 7d. COMPANIONS (4; follow, act on their own, upgrade with cards)
MOLELINGS (2 → 4 → 6 little moles digging short side tunnels near you) · DRILL MOLE (one big mole digging long straight
tunnels toward where you look) · LANTERN BUGS (light the tunnel, collect tokens) · BUSY BEES (break random blocks around
you slowly). Visual cap: max 8 companion models rendered per player; the rest are "virtual" (they still dig).

## 8. SPECIALS, HINTS, THE BOX
- Generation (seeded): the BOX at least 20 blocks inside the surface; a 5³ BOX ROOM around it (mint glowing tiles);
  10–14 SPECIALS per Standard cube (scale with size), never within 8 blocks of each other.
- Special types (ours):
  - **SHRINES** (3³ rooms with a prop on a pedestal, tinted by band, one line):
    | Shrine | Line |
    |---|---|
    | frog lantern | "it was waiting for someone." |
    | sleepy cat | "don't wake her." |
    | snail on a cushion | "slow is also a speed." |
    | teapot garden | "still warm." |
    | moon in a jar | "it fell. we kept it." |
    | rubber boots fountain | "someone forgot them." |
    | paper cranes | "make a wish. quietly." |
    | glowing mushrooms | "they hum at night." |
    | handless clock | "it stopped asking what time it is." |
    | goldfish bowl | "he has seen things." |

    Punch the prop to claim (tooltip "<name> · punch to claim"): it lights up, the line types out, a pop shows
    "+N tokens · free card" + an Index entry; it stays lit.
  - **TOKEN GEODE:** a crystal block that bursts 400–1,200 tokens ("a pocket of shine. crack it.").
  - **CARD CACHE:** a chest that gives one Epic+ card pick.
  - **GOLD VEIN:** 6–10 golden blocks in a line (×5 tokens).
- Hints (Normal):
  - the top chip compares your distance to the box after every ≥ 2 blocks moved → "closer" (warm chime) / "further"
    (low tone); taught once: "dig straight. when it says further, turn."
  - "special · 9 m" + an arrow when a Special is within 12 blocks
  - Hard: nothing
- BOX FOUND (make this give goosebumps):
  1. breaking the last block of the room → 0.6 s slow-mo
  2. the box flares; a white flash; the hum swells
  3. confetti in band colors; the timer freezes big in the center ("12:34.56")
  4. rank pops ("#14 today · new best!")
  5. the box unfolds and a BOX BUDDY peeks out (a rarity color beam)
  6. "find another?" / "back to the hall"
  7. everyone in the server sees your light column (§2)

## 9. META PROGRESSION (permanent)
- GEMS: from finding boxes (Standard 20 · Large 40 · Very Large 80; Hard ×1.5; Daily ×2; Live Race top 3: 60/40/25),
  Specials (2), the daily gift, quests, group reward (50 once), codes, Index milestones.
- UNLOCKS (gems, permanent): new cards entering the pool (start with about 60% of the pool unlocked; the rest cost
  15–60 gems each), permanent PURE movement (Sprint 40, Slide 60, Wall Kick 80), Hall decorations, cube themes
  (cosmetic block skins for unranked runs), ghost auras.
- BOX BUDDIES: each found box contains one (free rarity roll: Common 55 / Uncommon 25 / Rare 12 / Epic 6 / Legendary
  1.8 / Secret 0.2; Hard, Large and Daily shift the odds up, shown in the Index). 30 at launch (cute creatures curled
  in little boxes: a sock fox, a toast cat, a moss turtle, a jelly bear…). They sit on your BUDDY SHELF in the Hall
  (everyone can see shelves) and one rides on your shoulder (visible on your ghost). No stat power.
- COLLECTION (menu like the original's): tabs CORE / PERKS / SPELLS / RISKS / BUDDIES / SPECIALS, a category filter,
  undiscovered = a glowing-box card back.
- Daily: a login streak (gems), 3 quests (find a box · break 5,000 blocks · find 3 Specials · play the Daily · join a
  Live Race), and the Daily Cube.

## 10. LEADERBOARDS
- Boards: goal (Box / Boxless) × size × difficulty (Normal / Hard) × upgrades (On / Pure) × group (Solo / Party) ×
  period (Today / This week / This month / All time), plus a DAILY board and a LIVE RACE board (wins).
- Hall LEADERBOARD WALL (a big SurfaceGui) + a full menu with the same filters as the original (pills).
  Rows: rank, avatar headshot, name, time. Your own best row pinned at the bottom.
- Anti-cheat: the server times runs (start = first dig, end = server confirms the box cell broken); reject impossible
  times (Standard < 3:00 with upgrades, < 8:00 pure) for manual review.

## 11. THE HALL & FLOW
- Spawn in the Hall, in first person, facing the cube (a slow camera push-in on first join). A single line: "there's a
  box in there. find it."
- The CUBE PORTAL (walk into the glowing plinth gate) opens the MODE PANEL: size, difficulty, upgrades on/pure, goal,
  daily, seed, solo/party → "dig". Preselected for new players: Standard · Normal · Upgrades ON. Two taps total.
- Your run starts at the cube's top face (you drop onto it). Leaving: menu → "back to the hall" (the run is saved and
  the timer paused).
- Stations: LEADERBOARD WALL · BUDDY SHELVES (yours glow when you look at them) · RACE GATE (countdown sign) · STORE
  alcove · daily gift lantern · group/codes board.

## 12. ONBOARDING (first 60 s, no walls of text)
- 0–5 s: spawn, the cube in front, the portal pulses; tap → the preselected mode → "dig".
- 5–10 s: you land on the cube; a pulsing "punch" chip (mobile: the PUNCH button pulses). First break → tokens fly.
- ≤ 15 s: LEVEL 1 → the first card pick ALWAYS includes MEGA FIST → instant power.
- First "closer / further": one explanation chip, once. First Special: its line is the explanation.
- Funnel-log every step (AnalyticsService:LogOnboardingFunnelStepEvent).

## 13. CONTROLS
- PC: mouse look; LMB punch (hold = auto-punch); 1–4 spells (or scroll + RMB to cast the selected one); Space jump
  (wall kick); Shift sprint; C slide; Tab boards; Q emote wheel; Esc menu.
- Mobile: thumbstick; drag to look; PUNCH (hold = auto); 4 spell buttons; JUMP; SLIDE; aim assist snaps the crosshair
  to the nearest block face within 6° when punching.
- Console: RT punch, LT cast selected, LB/RB cycle spells, A jump, B slide, L3 sprint, View boards, Menu, D-pad emotes;
  full GuiService selection for menus and cards.

## 14. JUICE CHECKLIST (every item must exist)
- Punch: a fist squash, a crack decal on hit 1, the block POPS (scale 1 → 0.6 cube that tumbles and falls 1 s, fades;
  max 40 debris), a dust puff, a pitch-randomized "tock" (pitch rises in a 1 s combo), a 2-frame hit stop on a break, a
  0.5° camera kick.
- Lamp blocks: the lamp drops out still glowing and bounces.
- Tokens: a pop, hover 0.15 s, a swoop, a "tick" rising in pitch within a combo; the XP bar has a sweeping highlight.
- Spells: a FOV punch, a shock ring, chunk debris, a bass thump, a small shake (Reduced Motion setting respected).
- Level up: a whoosh, a time-slow, cards rising with a staggered spring, a Legendary shimmer.
- Band change: a color wash + a soft chime + the band name.
- Special: a shrine light-up, a harp arpeggio, its line typed out.
- Box found: §8.
- Ambience per band: a quiet drone + soft chimes; the Hall: water trickle + candle crackle + soft piano.

## 15. MONETIZATION (honest; placeholder IDs in Config; create the real ones via Open Cloud)
RANKED runs (all leaderboard runs, Daily, Live Race) ignore every paid boost; boosts only work in CASUAL runs, and the
mode panel says so. No paid random items. No gems sold. Cosmetics others can SEE (ghost auras, trails, glove skins on
your ghost's hands, find-beam colors, shoulder buddy hats) are the main shop, because the shared space makes them
show-off items.
| Type | Name | R$ | Effect |
|---|---|---|---|
| Pass | VIP | 249 | gold name, VIP Hall lounge, exclusive aura + glove, +10% gems |
| Pass | 2x Gems | 99 | double gems |
| Pass | Glove Locker | 199 | 6 glove skins |
| Pass | Aura Pack | 199 | 5 ghost auras + trails others see |
| Pass | Find-Beam Colors | 149 | 6 box-found column colors |
| Pass | Lucky Cards (casual) | 199 | 4 cards per level-up in casual runs |
| Pass | Starter Spell (casual) | 249 | start casual runs with a chosen unlocked spell |
| Product | Token Rush 15 min (casual) | 29 | ×2 tokens in casual runs |
| Product | Single glove / aura | 49–99 | cosmetic |

## 16. VISUAL QA (mandatory loop)
- Before any visual work: study every image in style_refs\ and FTB_STUDY.md §3–§4. Write STYLE_NOTES.md in your own
  words.
- After every visual change: screen_capture the same view types as the refs (hall with the cube, a B1 tunnel, a B2
  tunnel, a card pick, the HUD, a Special, a box find, the leaderboard). Save them to visual_qa\<step>\. Score each 1–10
  vs the refs on: palette, light mood, block texture + seams, fists, UI cards/HUD, glow + juice. Log in VISUAL_QA.md.
- An area is DONE only at an average ≥ 8 AND when it would look good as a Roblox thumbnail. Below 8: list what's off,
  fix it, re-shoot. Never mark visual work done on "it works".
- The refs are for mood and layout only: never upload, trace or copy their pixels, names or text.

## 17. FUN QA (mandatory)
At every milestone, play 3 real minutes (input simulation). Log in FUN_QA.md:
- Visible + audible feedback on EVERY punch? (must be yes)
- Seconds to the first break / token / level / card: targets 3 / 3 / 15 / 15.
- A new choice or surprise at least every 60 s in the first 10 minutes? (must be yes)
- The 3 best and 3 dullest moments; fix the dullest before moving on.
- With 2+ clients: do ghosts and shared moments make it feel alive without distracting?

## 18. BALANCE TARGETS (BalanceSim proves them)
- Standard · Normal · upgrades ON, average player: box in 15–25 min; a top player: about 6–9 min.
- Pure Standard Normal: 30–45 min.
- Card picks: about every 20–40 s for the first 5 minutes, then about every 60–90 s; a run ends at Lv 40–70
  (Standard).
- Live Race winner usually 8–14 min.

## 19. SAFETY
No skulls, blood, gore, robed or hooded figures, religious symbols, weapons aimed at anything, text in images, real
brands. Fists only punch blocks. Ghosts are friendly glowing silhouettes, never scary.

## 20. TECH: see TECH_NOTES.md (cube engine, shared-space ghosts, networking, persistence, leaderboards).
## 21. ART PIPELINE: see BLENDER_PIPELINE.md (asset list, Blender rules, export, upload, textures).
