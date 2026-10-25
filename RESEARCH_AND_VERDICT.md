> **SUPERSEDED (v1).** A straight Lost Bitcoin port already exists on Roblox and is dead (Clear the Junkyard: 2 live; Find The Lost Bitcoin). See `SCRAP_A_JUNKYARD_RESEARCH_AND_VERDICT.md`.

# Lost Bitcoin → Roblox: Dossier + Verdict

Researched 2026-10-25. Build prompt: `SCRAP_TO_RICHES_ONE_SHOT_PROMPT.md`.

## Phase 1: Dossier

**Big caveat:** Lost Bitcoin (Velto Games, Steam app 5427110) is **not released**. Its store page says "Coming soon", there's no price, it has **0 reviews** and **0 forum threads**, and the dev has no web footprint. Everything below comes from the store page, the API data and **7 screenshots**. Reviews come from its two direct ancestors: *A Game About Digging A Hole* (AGADAH, Very Positive, about 18.9K reviews, 1M+ sold) and *One Man's Trash* (about 82% positive from about 321 reviews, also a "lost Bitcoin in a landfill" game).

### 1. Pitch
- You dig through a giant junkyard, burn the scrap for coins, upgrade your gear and build a factory, all to find your one real Bitcoin USB stick among many identical ones.
- Genre: first-person digging + incremental + light factory automation. Tags: Simulation, Mining, Automation, Physics, Relaxing, Procedural.
- Comparable games: A Game About Digging A Hole, One Man's Trash, Motherload, PowerWash-style "zen sims", and on Roblox, **Dig & Clean** (peak 270K concurrent players in Aug 2026).

### 2. Core loop
| Scale | What you do |
|---|---|
| Second | Grab, magnet-pull or vacuum scrap, then throw it or blow it into the furnace for a coin burst |
| Minute | Buy skill-tree upgrades, dig deeper for better junk, cut open crates and safes, read USB sticks at the computer, place factory machines |
| Session | Grow the factory's per-minute income, reach deeper layers and set pieces (a sunken sailing ship), find the real stick (the end goal) |

### 3. Systems (confirmed from screenshots/store page unless marked)
- **Tools (hotbar 1–4):** Hand/Grabber, Scrap Vacuum (tank + blow-out), Cutting Torch, Magnet. There's also a Winch (shown in the HUD).
- **Skill tree "Scrap Shop":** 7 branches: Player, Tools, Processing, Furnace, Automation, Search, Factory. 60+ upgrades, with more planned.
- **Currencies:** coins (shown with 2 decimals), a second counter with a key icon (1→2) [ESTIMATE: keys open safes].
- **Inventory:** a backpack (0/2 → 0/6 slots) and a vacuum tank (%). Items have weight (e.g. "Old tire 9 kg").
- **Treasure:** identical USB sticks (read at the platform computer, "Reading stick 93%"), crates, safes, golden pieces, a buried sailing ship you cut your way into.
- **Factory (on the deck):** cranes, belts, sorting gates, rolling mill, 3D printer. It makes drones, engines, washing machines and robots, and runs while you dig. It uses a grid build mode (rotate, demolish, build menu).
- **Enemies:** none mentioned. Modes: single-player only. Save: "Save anytime".
- **Not present:** co-op, prestige, quests and events (none mentioned).

### 4. Numbers (read off the screenshots)
| Thing | Value |
|---|---|
| Walk speed upgrade | 152 coins (lvl 4/10) |
| Jump power | 60 (1/5) · Throw power 68 (0/5) |
| Vacuum tank | MAX 8/8 · Suction power 1,520 (4/8) · Blow-out speed 900 (2/8) · Multi nozzle 15,000 (1/3) |
| Magnet radius | 4,560 (5/8) · capacity 9,110 (6/8) · strength 19,200 (2/5, lifts 59→82 kg) |
| Winch speed | 1,000 (1/5) · Torch speed 115,000 (0/5) |
| 3D printer (factory) | 20,000 coins |
| Factory income | about 4,800/min when holding 50K–150K coins |
| Burn pop-ups | +30 to +429 per item mid-game |
| Cost curve | [ESTIMATE] about ×1.6–1.8 per level (base about 30) |
| Full game length | [ESTIMATE] 4–8 h (AGADAH is 1–2 h, One Man's Trash about 5 h) |

### 5. Pacing
[ESTIMATE] Early game is the hand + vacuum near the surface. The factory comes in mid-game (10K–20K coins). The torch and ship come late (100K+). It's one long save that ends when you find the real stick.

### 6. UI/HUD
Coins top-left with a "+n" fly-in, the key counter, "Factory +n/minute" top-right, the tool hotbar bottom-left, Backpack/Tank/Winch bars bottom-right, a context tooltip at the center bottom ("Old tire 9 kg · Left mouse: pick up"). The Scrap Shop is a dark panel with orange lines and bought/unlocked/locked states, and a hover card that shows "59 kg → 82 kg". Juice: a coin fountain plus flames from the furnace, and a glowing furnace mouth.

### 7. Art/Audio
Stylized low-poly toy junk. Warm sepia/orange haze, golden hour, teal and cream accents. First-person camera. The deck has cranes on the skyline. Audio: unknown.

### 8. Love / Hate (from the ancestor games)
| Love | Hate |
|---|---|
| "Just one more dig" upgrade loop | Too short: "beat in an hour or two" |
| Relaxing, zen: "it was very relaxing" | Bad or abrupt ending: "ends just as it starts becoming interesting" |
| Motherload nostalgia | Money is useless late: "functionally useless once you've gotten the upgrades" |
| Freedom to dig anywhere | Tiny invisible upgrades: "+5% range, +5% power" |
| Simple, smooth controls: "Flawless." | Derivative and repetitive: "a carbon copy", plus crashes and lost saves |

### 9. Unknowns
Price, release date, map size and depth, layer list, whether keys are a currency, real cost curves, factory product values, offline income, the ending, audio, whether there are any hazards or enemies. Note that the dev says "almost all content" was made with generative AI.

## Phase 2: Verdict — 6/10

**Why not higher:** it's a copy of a copy of a copy (Motherload → AGADAH → One Man's Trash → Lost Bitcoin). The original has zero reviews, so nothing about *this* game is proven. Roblox already has a 270K-CCU "dig up junk and identify it" hit (Dig & Clean). The crypto theme is a bad fit for a kids' platform.

**Why not lower:** the loop is proven on Roblox right now. It's naturally co-op, mobile-friendly if built right, and the furnace coin fountain makes a great clip. The factory adds the tycoon half that Roblox loves.

**Changes for Roblox:**
- Drop Bitcoin entirely. The goal becomes the **Golden Stick**. No crypto symbols.
- Co-op: 4-player party in a shared pit, with a 20% "Team Heat" bonus that's created as a bonus, never taken from anyone.
- 20-minute Yards (Easy/Normal/Hard), then Rebirth for permanent Gears. This fixes "too short" and "money useless".
- Third-person by default, plus first-person as an option. Tap-to-grab with soft auto-aim. Full gamepad support.
- Fixed factory pads instead of free building (phones can't handle drag-building).
- Every upgrade shows "now → next". No invisible +5%.
- No death or fall damage. A lift plus a "Back to Deck" button.
- Daily streak, quests, a Daily Golden Crate, a Museum of collectibles, offline factory income.
- Honest monetization: passes ≈ 10× a 15-minute boost, nothing usable against other players, no paid random items.

**Name options:** Scrap to Riches ✅, Dig & Burn, Junkyard Jackpot (the word "jackpot" sounds like gambling, risky), Feed the Furnace (too close to *Feed the Fire*), Burn the Junk.
**Pick: SCRAP TO RICHES** [ASSUMPTION: check the name is free on Roblox].

**Top 3 risks:**
1. **Late and derivative, behind Dig & Clean.** Counter: lead with what Dig & Clean doesn't have: the furnace fountain, the factory, co-op pits and the Golden Stick hunt. The thumbnail should be the coin explosion.
2. **Mobile performance and feel** with deep pits and lots of props. Counter: Terrain carving, anchored pooled props loaded lazily, a 600-prop cap per yard, the QualityController, and the lift.
3. **Retention cliff after the stick is found** (AGADAH's #1 complaint). Counter: Rebirth, harder Yards, Museum sets, a factory that persists, daily hooks.
