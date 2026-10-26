# VERDICT — Dome Keeper → Roblox (2026-10-26)

## 1. One-line pitch
**Defend the Dome**: land a glass dome on an alien planet with up to 5 friends. Dig the mine below for ore while a
wave clock ticks, drag your loot back, and get everyone into a turret seat before the monsters hit. Find the relic at
the bottom, or see how many waves you can hold. It is the run-based, discovery-driven answer to Bunker vs Verity.

## 2. The source game (3 lines)
Dome Keeper (Bippinbits/Raw Fury, 2022) is a 2D roguelike that alternates between digging resources under your dome
and defending it from alien waves with one upgradable weapon. It sold about 625K units, has 1M+ players, is 90% Very
Positive, and added 4-player co-op in 2025 and mobile in Oct 2026. Players love the dig/defend tension and hate the
thin content and the lack of persistent progression.

## 3. Concept choice: **Port + Roblox layer** (co-op skeleton, positioned against Bunker vs Verity)
- **Not a straight port.** Simulator-style "dig + defend" died twice (Dig to Defend 5.1M visits → 0 live; Dig and
  Survive 4K peak → 13).
- The real-time version is alive and owned by **Bunker vs Verity** (61K peak this month, 8.2K live; found in the
  review). So we must be clearly different, not "another bunker game".
- **Not a pivot.** The source's verbs map cleanly onto the most proven co-op skeleton on Roblox: 99 Nights in the
  Forest (11.2M peak, 172K live today): gather by day, defend the base when the threat comes, a numbered goal.
- **The Roblox layer, on purpose:**
  1. **Co-op on one dome** (1–6 players, one shared threat). Every player gets a **turret seat** on the dome (2 seats
     at start, up to 6 by upgrade), so nobody idles in waves. Solo works: an empty seat auto-fires at 25% power.
  2. **The clock you can see underground:** a big wave bar on the HUD, a siren 20 s before, and the dome glows through
     the tunnels as a homing beacon. The last player back gets a "just made it" cheer.
  3. **Carried ore slows you** (the source's best tension). Teammates can grab your chain and help haul: a visible
     co-op moment.
  4. **Two goals:**
     - the Relic run: 30 waves or bring the relic up, with badges at 5/10/20/30
     - after the first relic, **Endless**: "how many waves can you hold?", lifetime best on the lobby board
  4b. **Recall:** hold 2 s to teleport home but drop all carried ore. Keeps the tension and saves kids from getting
      lost.
  5. **Persistent meta (the fix for Steam's #1 complaint):** Keeper Rank XP after every run, even a loss. A permanent
     unlock tree for 4 keeper classes, 4 dome types and the gadget pool, paid with Star Shards (the meta currency).
  6. **Collection:** relics found deep in the mine roll a rarity (Common → Mythic → Secret). They are kept on a lobby
     shelf and give small passive perks. Odds are shown; they are never sold for Robux.
  7. **Show-off:** dome skins, beam colors, drill trails, all visible to the server.
  8. **Weekly-update-ready:** a daily modifier run ("Mass Ore + Fast Monsters"), a weekly board with no boosts
     counted, and new enemy/biome packs on Saturdays.

**Run shape (target 18 min):**
- Mining phase 60–75 s, then a wave of 25–45 s.
- Waves 1–10 are on the surface biome. Waves 11–20 bring a biome shift (sky color, new enemy). Waves 21–30 are the
  Night biome with a boss on 10/20/30.
- A relic chamber sits at the bottom of the map. Bringing it up ends the run early with a big bonus (the "Relic Hunt"
  mode, our own design).

## 4. The evidence table
| Part | Proven by | Numbers |
|---|---|---|
| Dig → wave clock → defend | Dome Keeper | ~625K units, 90% positive, 1M players |
| **Dig a base + control turrets vs waves, on Roblox** | **Bunker vs Verity** (found in review) | **61K peak Oct 2026**, 8.2K live, 24M visits in 5 weeks, 83% |
| Haul to the base before a clock | Feed the Fire | 12K peak Oct 2026, 3.5K live, 97.7% |
| Co-op gather + defend base + numbered goal | 99 Nights in the Forest | 11.2M peak, 172K live, 30.3B visits, 90.5% |
| Co-op descend + monsters + upgrades + cards | Drill to Earth's Core | 31K peak Sep 2026, 9K live (29% of peak), 84M visits, 92% |
| PvE defend-a-building waves | Protect The House / Survive The Night | 19K peak / 12K peak (Oct 2026), 92% / 96% |
| Mining as a satisfying verb | Mine a Mountain, Prospecting!, Dig to Escape | 151M / 273M / 608M visits, 96–98% |
| Collection with a Secret tier | Steal An Egg (platform facts) | 13.4M players, 1.9M hatched a Secret |
| Prices | DtEC, Protect the House, Survive the Night, Bunker vs Verity | carry +5 at 199, 3X Mining Speed 129, +turret slots 129, VIP 149–499 |

## 5. Freshness check (from MARKET.md §2)
| Close match | Live | Visits | Verdict |
|---|---|---|---|
| Dig to Defend | 0 | 5.1M | same verbs, simulator, dead |
| Dig and Survive | 13 | 2.6M | zombie town, peaked 4K, dead |
| Stranded: Mine to Survive | 113 | 40K | same theme, 3 weeks old, small |
| Drill to Earth's Core | 8,957 | 84M | lane leader for co-op dig + monsters, no base clock |
| Protect the House | 1,430 | 157M | defense half only |
| **Bunker vs Verity** | **8,240** | 24M | **same verbs (dig + turrets + waves), alive, 61K peak this month, meme-boosted, 13% of peak** |
| BvV clones (3) | 500–688 | small | clone wave already stalled |

**Freshness = low-medium (after review).** Dig + defend is now proven AND owned on Roblox by Bunker vs Verity. Our
difference is structure, not verbs: run-based, a mine full of discoveries, ore you haul under a visible clock, one big
aimed weapon, gadget picks, a relic finale and persistent meta.

The thumbnail picture: a glass dome on top, friends in turret seats firing beams, and a cutaway of the mine below with a keeper dragging glowing ore. Nobody successful owns that picture.

## 6. Design guardrails
- **First 60 s:** spawn in the dome. The first block breaks in under 3 s and the first ore pops out within 10 s. The
  first wave comes at 45 s (short) and is easy and spectacular. No text walls: arrows and a ghost hand.
- **Session:** an 18-min run plus lobby. Rejoin a running server between waves.
- **Fix the Steam complaints:** variety per run (1 of 3 modifiers at launch, growing weekly; 3-card gadget picks), at least 6 enemy types by
  launch, boss waves, persistent unlocks.
- **Servers:** 6 max (sim/co-op sweet spot). Matchmaking prefers friends.
- **Performance:**
  - The mine is a 3D grid of 4-stud blocks (24×24 footprint, 48 deep) and only exposed blocks exist as parts.
  - Cap visible blocks at about 3–4K. Ore uses instanced MeshParts. Enemies are silhouettes with one emissive eye
    material.
  - No EditableMesh, no runtime Terrain (platform facts).
- **Content safety:** aliens are blobby silhouettes, no skulls or gore. Turrets only target monsters. Our own names
  and art; no Dome Keeper text, designs or logo.
- **Monetization (honest):**
  - 3X Drill Speed 129, +2 Turret Seats (party) 129, +Carry 199, VIP 149–399, dome skins / beam colors / trails
    19–249.
  - Timed boosts don't count for the weekly board. No paid random items.

## 7. Score (after review round 1)
| Factor | v1 | Final | Why |
|---|---|---|---|
| Lane demand | 7 | **8** | Bunker vs Verity hit 61K this month with dig + turret waves; 99 Nights / Feed the Fire prove co-op base + clock |
| Competition | 6 | **4** | an alive 5-week-old leader with the same verbs; its clones stalled under 700, so being "another one" fails |
| Freshness | 6 | **5** | the twist is structural (runs, haul clock, relic, meta), so it is harder to show in one thumbnail |
| First 60 s | 6 | **7** | after the fixes: first ore in 10 s, a short first wave, siren + beacon + Recall |
| 28-day retention | 6 | **7** | meta tree + relic shelf + daily modifier + endless board; this is the edge over BvV (13% of peak) |
| Co-play | 8 | 8 | everyone has a seat in waves, hauling together |
| Mobile / perf | 6 | 6 | the voxel mine is still the main tech risk (Voxel Winter Survival 4.2K live shows voxels can run) |
| Honesty / policy | 9 | 9 | no gacha, odds shown, boosts excluded from boards |
| **Total** | 6.8 | **6.8 / 10 → realistic 6–7** | a B-tier bet that wins only on quality + speed + retention, not on novelty |

**Honest summary:** worth building only if you can ship in about 3–4 weeks while the dig-and-defend wave is hot, and
then update weekly. If the goal is a safe hit, this is not it. If the goal is a well-made game in a proven, live lane
with a clear retention edge, it is a reasonable bet.

**What makes it a real 8–9:**
- ship in about 3–4 weeks
- defense that feels amazing on a phone (soft auto-aim, big beams, screen shake)
- one memorable original enemy character for thumbnails (BvV's spike came from a character, but make it our own,
  not a meme)
- 3 thumbnails tested
- a Saturday update with a new enemy/biome every week
- an admin "Monster Moon" event in week 2

## 8. Name
**Pick: "Defend the Dome"**. It is a "Verb the Noun" title that explains the threat. The thumbnail shows the dig.
Search check: no existing game with this name.

Alternatives:
- "Dig & Defend the Dome" (clearer, longer)
- "Mine Under the Dome"
- "30 Waves on an Alien Planet" (dropped after review: 99 Nights-style titles read as clones; 99 Nights in the Bunker
  479 live, in the Arctic 360)
- "Dome Diggers"

## 9. Top 3 risks + fixes
1. **Seen as a Bunker vs Verity clone** (clones stall at 500–700). Fix:
   - Lead every thumbnail and the first minute with what BvV doesn't have: the glowing mine cutaway, hauled ore
     chains, and a big aimed dome beam.
   - Run-based structure with a relic finale.
   - Ship fast.
   Also avoid the deaths of Dig to Defend / Dig and Survive: no simulator auto-battle, meta from day 1.
2. **Phone aiming in waves feels bad.** Fix: tap-to-target with soft auto-aim, a hold-to-fire beam, and a big
   on-screen fire button. Seats auto-fire at 25% when empty or idle.
3. **Voxel mine perf/lag.** Fix:
   - a server-authoritative grid in a `buffer`; the client renders only exposed blocks
   - block changes batched on a reliable RemoteEvent (≤ 10/s)
   - UnreliableRemoteEvent (< 900 bytes) only for cosmetic chips/drill sparks
   - a 24×24×48 mine per server

## 10. Review rounds
**Process note:** no subagent tool was available in this run, so the review was a separate self-review pass. It
re-read the three docs as a hostile reviewer, ran 54 new searches (42 + 12), and verified every claimed match with
`details`/`votes`/`passes` and RoWatcher. It is not independent: treat it as weaker than the skill intends.
[LIMITATION]

**Round 1: 42 searches**
- Queries: man the turret, turret defense, defend the base co-op, space station defense, planet defense, alien
  invasion survive, colony defense, outpost defense, bunker defense, glass dome, biodome, dome survival, mars base,
  mars mining, moon mining, asteroid mining, space colony, drill and defend, ore defense, haul ore, minecart, mining
  expedition, extraction, dig and extract, cave survival, underground survival, keep the fire alive, nights in the,
  survive 99, defend the core, protect the core, protect the crystal, crystal defense, power the generator, wave
  survival co-op, tower defense mining, space survival, alien monsters, mine for survival, dig by day, relic, rocket
  escape planet.

| Finding (verified) | Numbers | Effect |
|---|---|---|
| **Bunker vs Verity** = dig a bunker + wall + place/CONTROL turrets + waves + retreat underground | created 2026-09-22, 24.1M visits, 8,240 live, 61K peak (Oct 2026), 83% like, 6/server | Lane demand ↑, competition ↓↓, freshness ↓. The v1 claim "dig+defend untested/dead" was WRONG. |
| Feed the Fire = drag fuel to a central fire before the storm clock | 3.5M visits, 3.5K live, 12K peak, 97.7% | Proves the haul-before-clock tension; copy its physical dragging feel. |
| 99 Nights clones stall | in the Bunker 479 live, in the Arctic 360 | Drop the "30 Waves on…" naming. |
| HUSH (extraction, clock, lose what you carry) | 8M visits, 3.2K live, 92% | Optional: "lose half your carried ore if you're caught outside" as a Hard modifier. |
| Voxel Winter Survival (voxel base + storm) | 4.2K live, 71% | Voxels are feasible on Roblox; its low like % warns that quality matters. |
| Turret Barrage Defense ("man the AA guns") | 103 live, new | Turret seats alone don't pull. They must sit inside a bigger loop. |

**Round 2: 12 searches for BvV clones**
- Queries: vs verity, bunker vs, dig a bunker, hatch defense, build a bunker, verity, dig bunker defend waves,
  underground hatch, fortify bunker, raid waves turret, dome vs, mine vs monsters waves.
- Result: the clone wave already arrived ("Build Base to Survive VERITY" 500, "Build and Hide…" 688, "Build a
  Bunker" 558/695). All stalled.
- Verity is a cross-game trending character (Steal A Verity 6.5K, Beat Up Verity 3.6K). Part of BvV's demand is that
  meme.
- Decision: **no pivot**. No better lane is supported by the data. A pivot onto BvV's skeleton would just be another
  stalled clone. Keep the Dome Keeper structure and reposition against BvV.

**Fixes applied (ranked):**
1. Position as the run-based, discovery-driven alternative to BvV. Lead with the mine cutaway + haul + big beam.
2. Scope for the first build:
   - 2 keepers, 2 domes, 10 gadgets, 3 run modifiers, 6 enemies + 1 boss, 2 biomes
   - mine 24×24×48
   - the rest goes into weekly updates
3. Add **Recall**: hold 2 s to teleport home but drop all carried ore. Add a siren at −20 s and a dome beacon visible
   through rock. This makes it clear for a 9-year-old on a phone.
4. Add **Endless mode** after the first relic ("how many waves can you hold?"). BvV players expect it. Boosts don't
   count on the board.
5. Physical hauling like Feed the Fire: ore chunks are big, glowing and visible from the surface when hauled. A
   teammate can grab the chain.
6. Pass prices aligned with live data:
   - 3X Drill Speed 129
   - +2 Turret Seats (party) 129
   - +Carry 199
   - VIP 149–399
   - Dome skins / beam colors 19–249 (Feed the Fire shows many cheap cosmetics sell)
7. Name kept: **Defend the Dome**. "30 Waves on an Alien Planet" dropped.
8. One original signature enemy (a cute-scary round alien) for thumbnails. Not a meme, not a copy of Verity.

**Score:** v1 6.8 → reviewer "before fixes" 6.0 → final 6.8 (realistic 6–7). The score held only because demand
evidence went up as much as freshness went down.
