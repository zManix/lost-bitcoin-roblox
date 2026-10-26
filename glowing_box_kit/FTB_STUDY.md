# Find The Box: deep study (for the build agent)

Sources:
- the Steam page and 16 screenshots
- the "Game Trailer" (35 s) and "Gameplay Trailer" (76 s), at 1 fps plus full-1080p frames at key moments plus 10-fps
  animation strips
- the Taco Inc site
- the YouTube search list

YouTube downloads were blocked on the research machine, so the build agent studies the gameplay videos itself
(see step R0 in START_PROMPT.md).

## 1. What the game is
- Single-player, first person, released 2026-11-04 on Steam (Windows), by Taco Inc (small studio; also makes
  Endless Onslaught and Wizard Clicker on mobile).
- A box is hidden in a solid cube of 1M+ blocks inside a quiet, candlelit spa hall. Find it.
- Two ways to play:
  - **pure:** punch, breathe, repeat (meditative)
  - **roguelite:** every block drops a token → level up → pick 1 of 3 cards → build a "block-destroying powerhouse"
- No enemies, no fail state. Every hole stays dug (autosave), including the box location.
- Modes:
  - Normal (warmer/colder hints) or Hard (no hints)
  - upgrades on/off (separate boards)
  - 4 cube sizes: 1M / 2M / 4M / 8M (beat a size to unlock the next)
  - Boxless (clear 50% → 25% of the cube as fast as possible; HUD shows "173,396 / 500,000 · 34.6%")
  - Daily Cube (same cube for everyone, one try a day, one board)
  - Seeds (race a friend on the same cube; unranked)
- Leaderboards: Find the Box / Boxless → Local / Global / Daily → Upgrades / No upgrades → cube size (◀ ▶) →
  Normal / Hard → Today / This week / This month / All time. Rank rows "#1 name 07:51". Top Standard-Hard weekly
  times are about 7:51–14:29.
- Playtime: "under half an hour" for Standard; Humongous Hard is a multi-evening project.
- Content: 18 spells, 100+ perks/upgrades, dozens of buried specials, 70+ achievements.

## 2. Why it works (the design lessons to protect)
1. **One clear goal, zero explanation needed:** "There is a box. Find it." The title is the tutorial (like Search For
   The Needle on Roblox: 86K peak).
2. **Instant tactile feedback:** every punch breaks a block, the block DROPS as a little tumbling cube, and lamps fall
   out still glowing. The world reacts physically to every click.
3. **Throughput escalation:** from 1 block per punch → chain cracks → bombs → drill companions → screen-filling chaos
   at Lv 98 (hundreds of tokens and dozens of cubes flying). The "number go up" made visible.
4. **A choice every level:** the 3-card pick (Vampire Survivors / Megabonk lineage) makes every run a different build.
   Reroll, banish and skip give control.
5. **Mystery + hot/cold:** "closer / further" plus distance-to-Special pings keep your direction meaningful.
6. **Little surprises:** buried Specials (shrines with one-line lore: "She saw everything. She'll remember.";
   Token Geodes: "Crack it open. Let the shiny out.").
7. **Cozy vs crazy:** the same game serves relaxers (pure mode, candlelight) and speedrunners (leaderboards, Daily).
8. **Mood through color:** each depth band floods the world with one color: brown → rose → gold → blue → mint. You
   FEEL progress without a number.
9. **Short, endless:** a 15–30 min run, and always "try again" (the timer "quietly suggests you try again").

## 3. Visual language (what to match: mood, not pixels)
- **Post-process look:** comic/ink. Dark ink outlines on silhouettes, posterized warm shading, cross-hatch texture on
  the hands. On Roblox: bake ink lines and hatching into textures (hands, props), use thin LIGHT seams on block edges,
  and slight per-block brightness variation (±6%) so the grid reads.
- **Blocks:** big smooth faces with faint dark marble crack veins, thin white/cream seam lines on every edge, and dark
  ink lines where tunnels open. Tunnel walls show the grid. Small embedded LAMPS: round glowing discs
  (cream-white, about ⅓ block wide) set into block faces, the main light source in tunnels.
- **Hands:** realistic-ish bare forearms with heavy ink hatching (THEIRS). OURS: chunky cartoon GLOVED fists with a
  baked ink outline and hatching, so the vibe matches without copying.
- **Band colors** (sampled from frames): brown/sand (walls ~#8A5A35, light ~#E3B07A) · rose/magenta (~#B0185A, glow
  ~#FF3FA0) · lemon/gold (~#D8B23A) · night-blue (~#3D4FB8 with white star dots) · mint/green (~#3FBF8A). The Hall:
  dark brown walls with warm cream uplight strips, a glossy tile floor with white seams, hundreds of tiny candles.
- **The box:** a cube with a white-mint cracked-cell (Voronoi) texture, a strong glow, shown in a teal-green lit room.
  Trailer title cards use the same glowing-cell cube.
- **Tokens:** big cream discs with a thin olive ink rim, emissive. They spray out in huge numbers at high level.
- **Companions:** chubby cartoon hamsters (cyan, hot pink) and blobby creatures that tunnel around you.
- **UI fonts:** thin, wide-tracked geometric sans in caps for titles ("L E V E L  U P !", "COLLECTION"); a clean
  humanist sans for body text. Palette: near-black teal panels (~#0E1A1C at 85–90%), cream text (#F2E6D0), gold
  accent (#E8B45A, selected tab pills), cyan accent (#5BE0F0) for the active mode pill.

## 4. UI inventory (from the full-res frames)
- **HUD (in run):**
  - bottom center: a "Lv N" pill with a thin gold progress bar
  - under it, 4 square spell slots with key numbers 1–4, charge count "x4", a cooldown number overlay; the selected
    slot is cream-gold
  - bottom right: a passive/spell readiness tab with an icon + name ("CHARGE", "BIG PUNCH", "CANNON", "DRILL
    HAMSTER") + a colored progress line
  - bottom left: a timer pill "05:24"
  - center: a tiny hollow circle crosshair
  - top center (Boxless): a progress pill
  - above the level bar: a flavor/tooltip pill ("A Token Geode: Crack it open…") + "SPECIAL 8 m"
  - top: a hint chip "◀ FURTHER ▶"
- **Level-up screen:**
  - background blurred and darkened; title "L E V E L  U P !"; subtitle "LEVEL 27 · PICK ONE"
  - 3 tall cards. Each card:
    - "DEPTH I/II/III" with dash ornaments (the card's tier/level)
    - a category dot + label: DIGGER, MOTION, BLAST, CASTER, ECONOMY, UTILITY, COMPANIONS, WILD
    - a circular medallion icon with a wavy liquid line through the card
    - rarity (COMMON / RARE / EPIC / LEGENDARY)
    - NAME, a one-line description, a stat line ("Move speed 108%", "Extra room +2 → +4")
    - a pill tag (NEW PERK / UPGRADE / NEW SPELL)
  - card glow by rarity: Common dark teal, Rare emerald, Epic violet, Legendary amber
  - per-card "BANISH (n left)"
  - bottom: "REROLL (2)" and "SKIP", plus the hint "Click a card to take it · Banish removes it for the rest of the
    run"
- **Collection:**
  - tabs CORE / PERKS / SPELLS / RISKS; a SHOW filter with colored category dots
  - card grid grouped by category with a big detail card on the right
  - undiscovered cards are a glowing-cube back ("POD 054", "Are you happy yet?")
  - footer with controller hints
- **Leaderboard:** see §1. Mode pills on top (cyan selected), gold pills for the selected filters, a list with rank,
  name and time; the cursor is visible (mouse UI).
- **Main menu / hall:** you stand in the hall in first person with the giant cube in front of you; a menu appears
  over the hall (not observed in detail).

## 5. Systems observed
- **Card categories:** DIGGER (punch power, chain crack), MOTION (move speed, jetpack, air dash, extra jump, tuck &
  roll, slipgate, wall run), BLAST (radius, chain reaction, shock fist), CASTER (cooldowns, charges, aftershock),
  ECONOMY (appraiser, lucky blocks, gold knuckles, heavy hands, greed, daredevil), UTILITY, COMPANIONS (digger hamster,
  hamster hotel, hamster cannon, hamster laps), WILD.
- **RISKS:** opt-in downside cards that boost token rewards (Daredevil: "bonus token chance per block for each Risk
  you own").
- **Card depth tiers I–III:** taking an owned card again raises its depth.
- **Spells observed:** Big Punch, Bomb (throwable, 5³ blast), Hamster Cannon, Charge, Flare, Cannon, Drill/Digger
  Hamster, Second Wind ("store more casts before the cooldown starts"), Aftershock ("every block you break shortens
  your spell cooldown").
- **Specials:** shrine rooms (owl + moon on a perch, rubber duck in a glowing box niche, cow toy in a teal pool, a pink
  creature), Token Geodes, etc. Each shows a single quiet line.
- **Movement tutorial pills:** "Climb, then press Space Bar in mid-air to kick off the wall. Bounce between the walls
  to the top." / "Sprint and jump at the wall at an angle to run along it. Press Space Bar to jump off."
- **Flavor text:** lowercase-ish, gentle, slightly eerie ("Try not to worry.", "Are you happy yet?").
- **Animation timing:** alternating punches about every 0.2–0.3 s early; broken blocks drop as small physics cubes;
  lamps fall out glowing. Level-up cards slide up with a glow; the camera keeps moving behind the blur.

## 6. Roblox translation decisions
- Keep: the first-person punch feel, the cube, bands, tokens, 3-card levels with Banish/Reroll/Skip/Risks,
  categories, depth tiers, Specials with one-liners, hot/cold, all modes, Daily, leaderboards, Collection.
- Change: OUR names and art for every card/spell/companion (moles/bunnies instead of hamsters), gloved fists instead
  of hairy arms, our own shrine props and lines.
- ADD (Roblox): a **shared space with ghosts**. Everyone in the server digs their own private cube in the SAME place,
  and sees others as soft glowing silhouettes moving through the rock. Plus big shared moments (a box-found beam,
  Legendary pick sparkles) and a **Live Daily Race** (everyone races the same seed at the same time, ghosts visible).
  Nothing interferes.

## 7. Videos for the build agent to study (R0)
| ID | Title | Length |
|---|---|---|
| r28z2gU6tVU | "I Had To Find A 1 in 2,000,000 Box" (166K views) | 84 min |
| xHYT7ybiSwY | "Incrementally Destroying A Cube With Hamsters ~ Find The Box" | 58 min |
| RdlnEbMLS98 | Hultutigamer, Find The Box | 45 min |
| aUM3xPa7DS8 | Hultutigamer, Find The Box | 18 min |
| HLcefgt8pQk / fMhTnfhv9Sg | official shorts | |
| EjfV2pyTSBk | "ROBLOX FIND THE NEEDLE" by CaylusBlox (the Roblox comp) | 15 min |
