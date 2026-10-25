# Roblox Hits 2024–2026: Evidence-Based Loop Breakdown

Researched 2026-10-25. Purpose: help a designer choose proven loops for a new Roblox game.

## How to read this

- **Stats source:** Unless noted otherwise, peak CCU, visits, like ratio, server size and average playtime come from **Rolimons game pages fetched on 2026-10-25** (`https://www.rolimons.com/game/<placeId>`). Rolimons only records what it has tracked, so for games older than its tracking window (mainly Adopt Me, MM2, DOORS) the "all-time peak" may be lower than the true historical peak.
- **Like ratio** = upvotes / (upvotes + downvotes).
- **Monthly averages** (avg CCU) come from Max Power Gaming, which uses Rolimons daily data:
  - July 2026: https://www.maxpowergaming.co/post/roblox-top-games-july-26
  - Aug 2026: https://www.maxpowergaming.co/post/roblox-s-top-games-in-august-2026-murder-mystery-2-and-steal-an-egg-take-over
  - Sep 2026: https://www.maxpowergaming.co/post/roblox-s-top-games-in-september-2026-steal-an-egg-pulls-away-as-ride-a-pet-arrives
- **[UNVERIFIED]** marks a claim from one weak source, a modeled estimate, or a claim that sources disagree on.
- **[GK]** marks gameplay detail taken from general, widely documented knowledge of the game (fan wikis, guides) that I did **not** re-fetch this session. Treat it as unverified, but it's low risk.
- Trackers disagree a lot. For example, RoWatcher's own game pages give much lower "all-time peaks" than its news articles. I preferred Rolimons for every number and cite the other trackers where they conflict.

---

## 0. Platform context (this changes what works in 2026)

| Fact | Source |
|---|---|
| Platform CCU record: about 47.4M on 2025-08-23, during the Grow a Garden × Steal a Brainrot "admin war" | https://www.ign.com/articles/roblox-hits-fresh-player-record-towering-over-steam-and-fortnite-amid-war-between-its-two-most-popular-games-grow-a-garden-and-steal-a-brainrot |
| DAUs peaked at 151.5M in Q3 2025. Q2 2026: 123M DAU (+10% YoY), bookings $1.6B (+8%), revenue $1.5B | https://www.shacknews.com/article/150208/roblox-daus-grew-10-percent-yoy |
| Roblox's Q2 2026 explanation: engagement shifted from "high monetizing, 2025-vintage viral games" to "newer and continuously popular games with lower monetization rates per hour". Roblox **intentionally changed "Recommended for You" to favor highly retentive games** over near-term monetization | https://respawn.outlookindia.com/gaming/gaming-news/roblox-q2-2026-revenue-soars-36-to-15b-despite-bookings-miss |
| Top-10 games' share of hours is about 20% now, versus about 30% three years ago [UNVERIFIED: from a transcript summary] | https://transcripts.platformaeronaut.com/summaries/RBLX-2Q26-AI-Summary |
| Chat now requires a global age check, and matchmaking reportedly puts age-checked users in the same servers [UNVERIFIED for the matchmaking part] | https://ir.roblox.com/news/news-details/2026/Roblox-Requires-Users-Worldwide-to-Age-Check-to-Access-Chat/default.aspx |
| Aug 2026: new policy bars games that **reward watching in-game media feeds** (reels, autoplay, infinite scroll) from the Kids and Select catalogs. It was triggered by Steal an Egg's treadmill "Reels" | https://kotaku.com/roblox-cracks-down-on-doomscrolling-games-like-steal-an-egg-that-forces-players-to-watch-reels-while-running-on-a-treadmill-2000727952 |
| Live platform CCU on 2026-10-25 12:00 UTC: about 17.2M (24h range 14.1–22.3M) | https://rowatcher.com/roblox-player-count |
| Roblox's Halloween 2026 meta-event "The Hollow" (from Oct 22) features monsters from horror hits such as The Deer (99 Nights) and Seek (DOORS) | https://gamesbeat.com/?p=337339 |

**What this means for design:** in 2026 the recommendation algorithm rewards **retention** (D1/D7, session length), not just a launch spike. 2026's one-mechanic novelty games got huge peaks but kept almost none of those players (see section 3).

---

## 1. Game-by-game breakdown

### A. Biggest new hits of Jan–Oct 2026

#### 1. Steal An Egg (and Collect Rare Pets)
- **Studio:** Roblox group "and Collect Rare Pets". The Fandom wiki says it is owned by Badr_Omega [UNVERIFIED]: https://roblox.fandom.com/wiki/And_Collect_Rare_Pets
- **Launch:** 2026-07-25 (MPG August).
- **Peak CCU:**
  - **14,293,524 on 2026-09-19** (Rolimons, https://www.rolimons.com/game/107778070777162)
  - RoStats gives 14,313,917 (https://rostats.io/records)
- **Visits:** 9.46B. **Like ratio:** 91.7%. **Server size:** 7.
- **Monthly average CCU:**
  - Aug 2026: 543K (#2)
  - Sep 2026: **1,447,549 (#1, +167%)**
  - About 1.26M live on 2026-10-25
- **Core loop:**
  - *Second:* run, grab an egg from a wild pet or a rival base, and get away.
  - *Minute:* hatch eggs into pets. Pets earn money, which goes into treadmill speed training and base upgrades.
  - *Session:* chase rarer eggs (Secret, Eternal tiers) and fuse pets [UNVERIFIED].
  - Sources: Kotaku and https://stealanegg.net/ (fan site).
  - Badge data shows the rarity funnel: "WELCOME!" 13.36M awards → "Hatched Secret!" 1.94M → "Hatched Eternal!" 1.00M (stealanegg.net snapshot, 2026-09-26).
- **Social hook:** egg theft between players, and pets that lay eggs also steal them back. Kotaku calls it a "competitive, stressful environment".
- **Retention:**
  - Weekly themed updates: Rifts (9/5), Angels & Demons (9/12), drones (9/19), boss + egg-exchange lab (9/26).
  - Admin events.
  - "Dr. Scramble" boss roughly every 30 minutes during an event [UNVERIFIED].
- **Monetization:**
  - Speed can be bought with Robux (Kotaku).
  - X2 MONEY 399 R$, X2 GROWTH SPEED 467 R$ (stealanegg.net snapshot 2026-09-05).
- **Viral trigger:**
  - It grafts Steal a Brainrot's theft and base-defense structure onto pet-sim egg hatching (MPG).
  - Its treadmill showed a "Reels" screen of short videos (AI-generated and uncredited TikToks). Roblox took the game down temporarily and wrote a new policy. The game came back without Reels and **kept growing** (Kotaku; MPG August).
- **Decline:** not yet. MPG notes "early signs of cooling" at the end of September (the last Saturday was lower than the two before it).
- **Clones (all 2026, via https://rblxstat.com/lists/record-breaking-roblox-games):**
  - Break and Steal an Egg: 1.31M
  - Fake an Egg: 142K
  - Steal Animal Egg: 107K
  - Steal an Clown Egg: 73.7K
  - Steal From The Rich!: 58K
  - Steal ASMR: 45.5K

#### 2. [🎵] +1 Speed Keyboard Escape | Candy & Chocolate
- **Studio:** SecretVerse Studio.
- **Launch:** Rolimons lists creation as 2026-01-18. MPG says it "debuted March".
- **Peak CCU:** **7,263,327 on 2026-07-18** (https://www.rolimons.com/game/95082159892680).
- **Visits:** 6.59B. **Like ratio:** **96.75%**. **Server size:** 22. **Average playtime: 7.45 min** (the shortest of the big hits).
- **Monthly average CCU:** July 2026 350K+ (top 4), August 222K (−37%). About 101K live now.
- **Core loop:**
  - *Second:* every step gives +1 Speed.
  - *Minute:* run an obby of giant keyboard keys. A miss sends you back to the start. Train to unlock multipliers.
  - *Session:* become the fastest player on the server (Rolimons description).
- **Social hook:** server speed leaderboard and racing friends.
- **Retention:** multiplier tiers and trails. Weak beyond that.
- **Monetization:** game passes include "Candy Treadmill", "Speed Multiplier [Tier 7]", "GalaxyTrail" and "More Equipped Items (20 slots)" (Rolimons listings). Prices not captured.
- **Viral trigger:**
  - An instantly readable incremental number (+1) plus ASMR-style visuals and sound (Rolimons description).
  - It spawned a whole "+1 X" genre: +1 Stone Skipping 163K, +1 Loot To Forge 92K, +1 Pickaxe Swing for Eggs 54.6K, +1 Tongue Escape 48K, +1 Venom Evolution 47K (rblxstat).
- **Decline:** the shortest playtime of any top hit and a single mechanic. It fell about 98.6% from its peak to today's live count.

#### 3. Escape Tsunami For Brainrots!
- **Studio:** Wave of Brainrots group. MPG says DoBig Studios owns it.
- **Launch:** created mid-December 2025 (RoWatcher 2025-12-15). MPG says launched 2026-01-05.
- **Peak CCU:** **4,996,032 on 2026-01-24** (https://www.rolimons.com/game/131623223084840).
- **Visits:** 5.74B. **Like ratio:** 83.1%. **Server size:** 8. **Average playtime:** 9.55 min.
- **Current CCU:** about 6.8K live. That is **−99.9%**.
- **Core loop:**
  - *Second:* sprint down a long, narrow map.
  - *Minute:* grab Brainrots before the tsunami wave hits. Getting hit ends the run.
  - *Session:* upgrade speed and carry capacity, expand base slots, use Spawn Machines and Lucky Blocks, and rebirth for permanent multipliers.
  - Source: https://www.maxpowergaming.co/post/escape-tsunami-for-brainrots-roblox-s-next-brainrot-juggernaut
- **Social hook:** showing off rare Brainrots as status, close calls that make good clips, and optional stealing.
- **Retention:** rebirths, ultra-rare "Infinity Brainrots", limited-time modes, admin abuse events.
- **Monetization (R$):** VIP 175, VIP+ 888, Speed Boost 129, Super Speed Boost 329, Harpoon Gun 640, Rainbow Shield 295, Double Jump Coil 160, Infinity Ball 245, Shockwave Bomb 349, **Anti-Wave Device 699** (Rolimons). It sells **escape from the core threat**.
- **Viral trigger:**
  - Adds an active, risky run to the proven Brainrot base-income framework.
  - It was also put on Fortnite Creative.
  - Steal a Brainrot answered with its own "Escape Tsunami" limited-time mode.
- **Decline:** RoWatcher cites meme fatigue, a "low-effort slop" reputation, and fast replacement within the genre: https://rowatcher.com/news/is-the-brainrot-trend-dying-what-ccu-data-from-three-top-games-reveals

#### 4. Kick a Lucky Block
- **Studio:** No More Flops.
- **Launch:** 2026-04-07.
- **Peak CCU:** **1.7M in May 2026** (RoWatcher https://rowatcher.com/games/10004244222/kick-a-lucky-block and Rotrends). RoStats only shows 374K for its tracked window.
- **Visits:** 1.9B. **Like ratio:** about 95%. **Current CCU:** about 13–21K.
- **Core loop:** kick lucky blocks to win brainrots, survive a tsunami, place brainrots on your plot for income (Rolimons description via search). Kick → reveal → place → income.
- **Monetization:** x2 Cash 399 R$, **Auto Kick 99 R$** (Rolimons via search).
- **Viral trigger:** a lucky-block reveal (gacha) mashed up with Brainrot plot income, plus a trading world.
- **Decline:** about −99% from peak. It is a remix of an existing formula.

#### 5. Ride A Pet
- **Studio:** "this game is gud".
- **Launch:** 2026-04-14. It broke out in late September 2026.
- **Peak CCU:** **1,553,904, about 2026-10-03** (https://www.rolimons.com/game/124216119978534; RoStats dates it Oct 3).
- **Visits:** 429M. **Like ratio:** 96.3%. **Server size:** 6. **Average playtime: 14.66 min** (the longest of the 2026 viral hits).
- **Core loop:**
  - *Second:* ride your pet across the map.
  - *Minute:* find an egg and race back to base **before a timer runs out**, then hatch it.
  - *Session:* faster pets are better mounts, so you can reach rarer eggs. Mutations make pets faster. Radars, food effects and rebirth add depth (MPG September; Rolimons).
- **Social hook:** small servers and showing off pets [GK-light].
- **Monetization:** game passes exist ("Midas", "Super Pet Storage" appear on Rolimons) [UNVERIFIED: prices and contents].
- **Viral trigger:** the collectible is also the traversal upgrade, so progress is something you can *feel*. That's a clear loop for clips.
- **Decline:** about 23K live now (−98%). It peaked only three weeks ago, during Halloween season.

#### 6. Animal Hospital (Anomaly)
- **Studio:** Animal Anomaly (group owner Roytt).
- **Launch:** 2026-05-10.
- **Peak CCU:** **1,273,105 on 2026-07-10** (https://www.rolimons.com/game/78515283254292).
- **Visits:** 2.47B. **Like ratio:** 93.1%. **Server size:** 30. **Average playtime:** 11.28 min.
- **Monthly average CCU:** July 2026 471K (#2 on Roblox) → August 179K (−62%). About 48K live now.
- **Core loop:** "Patient arrives → Check-in → Diagnose → Treat → Repeat". Some patients are **disguised anomalies**, and players must check reception info against photos and security footage before admitting them. Source: https://www.maxpowergaming.co/post/animal-hospital-s-simple-loop-hides-surprising-depth
- **Social hook:** up to 4-player co-op night shift. Cute animals contrast with horror.
- **Retention:** shift milestones (10/25/50/100), recurring NPCs who drip lore, secrets, and named updates (Harlow's Favorite, Hazmat, a lore expansion).
- **Monetization:** **no game passes at all** (Rolimons: "This game has no known gamepasses"). It won a 2026 Roblox Innovation Award (Variety, via Wikipedia).
- **Viral trigger:** the "anomaly spotting" (Papers-Please / I'm-on-Observation-Duty) format plus co-op, which streamers like [UNVERIFIED as the trigger].
- **Decline:** −55% from July to August. Shift-based content runs out.

#### 7. Break and Steal an Egg
- **Studio:** ILGames x Eggs. **Launch:** 2026-09-05.
- **Peak CCU:** **1,312,221** (Rolimons https://www.rolimons.com/game/114326934417838). RoStats gives 1,311,860 on 2026-10-18.
- **Visits:** 250M. **Like ratio:** 97.5%. **Server size:** 7.
- **Loop:** break eggs to hatch animals, steal them, place them in your base for cash. The description openly says it was "inspired by steal an egg".
- **Note:** a fast clone of a #1 hit reached 1.3M within six weeks. Clones of the current #1 still work if you ship within weeks.

#### 8. Grow a Garden 2
- **Studio:** Strawberreh Squad group, with Jandel (Splitting Point).
- **Launch:** created 2026-05-21, public launch June 2026.
- **Peak CCU:** **929,371 on 2026-06-19** (https://www.rolimons.com/game/97598239454123). It had 400K+ concurrent players 20 minutes after launch, with queues (https://www.gosugamers.net/entertainment/news/78614-grow-a-garden-2-has-launched-on-roblox-here-s-everything-new-added-in-this-sequel).
- **Visits:** 1.68B. **Like ratio:** 87.8%. **Server size:** 8.
- **Monthly average CCU:** 450K+ in June and July → about 247K in August (−47%). August started near 479K and ended near 21K, which MPG ties possibly to bot enforcement. **About 1.6K live now.**
- **Loop changes from GaG1:**
  - **Night stealing:** you can enter others' gardens at night, but not while the owner is inside the plot.
  - Defensive plants.
  - **Guilds** with global competitions.
  - Sell-shop bargaining.
  - Pets spawn on the map instead of in eggs.
  - Central hub.
- **Decline:** the sequel split the audience, the novelty wore off, and possibly bot purges. A cautionary case: **a hit sequel does not inherit retention**.

#### 9. Sailor Piece
- **Studio:** Shadowrise Devs. **Launch:** 2025-11-17.
- **Peak CCU:** **745,280** (Rolimons via search, https://www.rolimons.com/game/77747658251236). Date unclear, around April 2026 [UNVERIFIED date].
- **Visits:** 1.6B. **Like ratio:** about 95.9%.
- **Loop:** One Piece-style anime RPG: grind mobs and bosses, roll races, swords and fruits, and push through seas.
- **Retention:** **weekly Wednesday updates**. Sea 2 launched 2026-04-16.
- **Monetization:** Fruit Storage, **Race Reroll 2,500 R$**, Stat Reset, Teleport, XP Boost, inventory expansion. Marketed as "fully playable free". Sources: https://rowatcher.com/news/blox-fruits-vs-sailor-piece-which-anime-rpg-is-actually-growing-faster-in-2026 and the RoWatcher week of April 6 piece (502K CCU, +6.7%).
- **Viral trigger:** named updates pushed through YouTube and TikTok, plus code giveaways at CCU milestones (215K/230K/245K/290K/305K).

#### 10. Dig & Clean 🧼 (the closest comparable for a digging/junk game)
- **Studio:** Squeaky Clean! group. **Launch:** 2026-07-09.
- **Peak CCU:** **269,053 on 2026-08-16** (https://www.rolimons.com/game/83038462357724).
- **Visits:** 128.6M. **Like ratio: 96.5%**. **Server size:** 6.
- **Current CCU:** **about 2.2K live** (−99%). The 30-day peak was 71.5K.
- **Core loop** (https://allthings.how/how-to-play-dig-clean-on-roblox-beginner-s-guide/):
  - *Second:* the Detector marks a glowing spot. Click or tap to start digging, then **rapid-tap to fill a dig meter**.
  - *Minute:* take the dirty item to the Cleaning Station and spray it. **Type, condition and value are hidden until it's fully washed** (a mystery-box reveal).
  - *Session:* put items on **museum podiums, where tourists pay based on what's displayed** (passive income), or sell them. Upgrade Shovel Power (required for higher-rarity items), the Detector, and the Spray Bottle or Pressure Washer. Unlock islands. Shipwreck Cove costs 1M and gives a permanent 2× luck. Later shovels: Cobalt for legendary items, Diamond for mythic.
- **Retention:** codes for luck boosts (UPDATE1 2× luck 30 min, SECRET10 10× luck 10 min) and update drops.
- **Monetization:** game passes exist (robolibrary wiki blocked) [UNVERIFIED].
- **Viral trigger:** satisfying ASMR cleaning reveals [UNVERIFIED as the trigger].
- **Decline:** there is **no player interaction or stealing**, the update cadence appears thin, and the end of the summer audience hit it. It fell from 269K to 2K in about 10 weeks. **There is demand, but this game didn't keep it.**

#### 11. Karinderya!
- **Studio:** SILOG. **Launch:** 2026-08-07.
- **Peak CCU:** **294,485 on 2026-09-19** (https://rostats.io/records). **Visits:** 86M.
- **Loop:** co-op Filipino eatery sim: serve customers, upgrade, reach 5 stars (https://www.player.one/roblox-karinderya-codes-august-2026-run-your-own-local-eatery-serving-popular-filipino-meals-163944).
- **Note:** regional and cultural theming can hit about 300K. SEA audiences are large.

#### Other 2026 signals (rblxstat list and RoStats)

| Game | Peak / note |
|---|---|
| Jump for Animals! | 234,817 peak |
| Hooked! (fishing) | +9,019% growth in Q1 2026, but only a 48.5K peak (Rotrends) |
| Swing Obby for Brainrots | 87K peak |
| Bunker vs Verity | 62K |
| Mine Antarctica (mining) | 27K, created 2026-07-19: https://www.rolimons.com/game/138686218420016 |
| +1 Loot To Forge | 92K |
| Illegal Soccer | 77K |
| Command An Army | 85K |
| Cameraman Tower Defense | 75K |
| The Hollow | Roblox's own event hub: 452K |

---

### B. 2025 breakouts

#### 12. Steal a Brainrot
- **Studio:** SpyderSammy, owned by DoBig Studios (Wikipedia). **Launch:** 2025-05-16.
- **Peak CCU:** **25,836,222 on 2025-10-11** (https://www.rolimons.com/game/109983668079237). PocketGamer.biz reported 25.4M on Oct 7.
- **Visits: 74.15B.** **Like ratio:** 85.1%. **Server size:** 8.
- **Current CCU:** about 327K live. Monthly average July 2026 about 212K. The 30-day peak was 1.29M (Halloween update).
- **Core loop** (https://en.wikipedia.org/wiki/Steal_a_Brainrot):
  - *Second:* run, grab a Brainrot from the conveyor or a rival base, and carry it home.
  - *Minute:* each Brainrot earns passive cash. Buy better ones off the belt. Hit **"lock base"** to get a temporary shield.
  - *Session:* fill base slots and **rebirth** for multipliers.
- **Social hook:** capture-the-flag theft and loss aversion. "Viral TikTok and YouTube clips show children crying after losing their Brainrots" (Wikipedia).
- **Retention:**
  - Weekly fixed schedule: **Saturday update ~3 PM ET + Admin Abuse**, and **"Taco Tuesday" 6 PM ET** (https://www.eldorado.gg/blog/steal-a-brainrot-en/steal-a-brainrot-admin-abuse-schedule-explained/).
  - During admin abuse, Sammy spawns limited brainrots across **all servers**, with luck boosts up to ×15, mutation boosts and trait stacks (Taco trait ×3). Exclusives **leave the pool when the event ends**, so their trading value is locked in.
- **Monetization:** gear and traps for Robux, and the best items are cash-only (Polygon, via Wikipedia). **Server admin powers are sold.** Lucky blocks.
- **Viral trigger:**
  - The Italian Brainrot meme wave.
  - Theft drama clips.
  - The **"admin war" with Grow a Garden on 2025-08-23**, which set the platform record of 47.4M.
  - Extinct Event, 24M (2025-09-13).
  - Bruno Mars in-game concert in Jan 2026: **12.8M CCU and 10M livestream viewers** (https://www.gamesindustry.biz/roblox-claims-bruno-mars-steal-a-brainrot-performance-drew-a-record-128-million-concurrent-users-issued-54-million-brainrot-collectibles).
- **Decline:** −98.7% from peak.
  - Each event peak "was followed by a steeper drop than the last".
  - Meme fatigue: creators declared the subgenre "dead" in December 2025.
  - Replaced by Escape Tsunami in January 2026.
  - Source: https://rowatcher.com/news/is-the-brainrot-trend-dying-what-ccu-data-from-three-top-games-reveals
  - It still holds a 200–300K baseline, which makes it a franchise.

#### 13. Grow a Garden
- **Studio:** BMWLux (16 years old) built it in about 3 days. Splitting Point (Jandel) bought in in April 2025 at about 1K CCU. DoBig holds a minority share (https://en.wikipedia.org/wiki/Grow_a_Garden).
- **Launch:** 2025-03-26.
- **Peak CCU:** **22,375,597 on 2025-08-23** (https://www.rolimons.com/game/126884695634066).
- **Visits: 35.99B.** **Like ratio:** 89.9%. **Current CCU:** about 26K live (30-day peak 132K).
- **CCU ladder (each step was an update or event day):**
  - 5M: Blood Moon, May 18
  - 8.9M: May
  - 11.7M: Bizzy Bees, May 31
  - 16M: June 14
  - 21.3M: Summer Update, June 21, 3 PM BST
  - 22.3M: admin war, Aug 23
- **Decay:** **within an hour of the June 21 peak it was at 7.6M, and 5.5M an hour later.** The 14-day average was 2.7M (https://www.pocketgamer.biz/robloxs-grow-a-garden-hits-industry-record-213m-concurrent-users-surpassing-pubg-fortnite-and-more/).
- **Core loop:**
  - *Second:* plant and harvest.
  - *Minute:* sell for Sheckles and buy seeds. **Seed and gear shops restock on a global 5-minute timer, synced across all servers**, and rare seeds are scarce (https://allthings.how/grow-a-garden-2-stock-predictor-how-restock-timing-works/).
  - *Session / day:* **crops grow while offline**, so you come back tomorrow.
  - Weather events apply mutations (Blood Moon and others) [GK]. Pets come from eggs (loot boxes).
- **Social hook:** walk into neighbors' gardens, trade, and later steal crops with Robux (Wikipedia: "Robux can… steal other players' crops").
- **Retention:**
  - Weekly exclusives you must claim *while online*.
  - Saturday weekly update preceded by an admin event (~60 min before). "Watering Wednesday" was added in April 2026 (https://bloxswaps.com/blog/grow-a-garden-admin-abuse) [UNVERIFIED single source].
  - Two dedicated event teams formed in July 2025.
- **Monetization:**
  - Skip waits, buy perks, steal.
  - About **$12M from virtual items in May 2025** (https://www.calcalistech.com/ctechnews/article/dj4lxef8r) [UNVERIFIED press estimate].
  - About $150M bookings in three months (RoWatcher) [UNVERIFIED].
  - An off-platform real-money trade in fruits and pets on eBay and Discord (Bloomberg 2025-05-30, via Wikipedia).
- **Viral trigger:**
  - Zero-stakes cozy loop that is mobile-friendly. About 35% of players are under 13.
  - Restock FOMO.
  - Celebrity takeover (Travis Kelce, July 2025).
  - Admin war.
  - Bot allegations (TD Cowen, later retracted) say the algorithm amplified it.
- **Decline:** fell to about 26K live. Causes:
  - Steal a Brainrot took the attention.
  - Jandel's team left in January 2026 [UNVERIFIED wiki] and later made GaG2.
  - DoBig was criticized for over-monetizing.
  - The trading economy was open to bots.

#### 14. 99 Nights in the Forest
- **Studio:** Grandma's Favourite Games (Alec Kieft, Cameron Angland, Matthew Hufton).
- **Launch:** created 2025-03-04, broke out mid-2025.
- **Peak CCU:**
  - **14,153,173 on 2025-10-04** (https://www.rolimons.com/game/79546208627805)
  - PC Gamer and Wikipedia say 14.2M
  - RoWatcher's game page says 11.2M in September 2025 (conflict)
- **Visits: 30.25B.** **Like ratio:** 90.5%. **Server size:** 25.
- **CCU now and over time:**
  - About 415K live now; 30-day peak 2.14M; RoStats peak 2,173,929 on 2026-10-17 (Halloween)
  - Monthly averages: 557K+ in January 2026, about 187K in May, 243K in July
  - **It has the strongest long-tail of any 2025 viral hit.**
- **Core loop** (Wikipedia list article):
  - *Second:* chop wood, fight wolves and bears.
  - *Minute:* feed the campfire, which expands the safe zone, and craft defenses.
  - *Session:* survive nights against **The Deer** and cultists, earn cave keys by killing a set number of animals, **rescue four missing kids**, and reach day 99.
  - Classes are bought with diamonds [GK].
- **Social hook:** co-op survival in 25-player servers. Emergent chaos clips: the Deer jump-scare and trolling teammates.
- **Retention:**
  - Biome updates (Jungle Biome Part 2, March 2026 crafting update).
  - Seasonal shops (Easter 2026 eggs and bunny classes).
  - Halloween 2026.
  - The Deer features in Roblox's "The Hollow".
- **Monetization:** diamonds buy classes and cosmetics [GK]. Robux revives [UNVERIFIED].
- **Viral trigger:**
  - Horror creature as a meme (The Deer), plus an "it's only 99 nights" goal.
  - Won Best Adventure and Best Horror at RIA 2025.
  - **Film by 20th Century Studios (April 2026)** and a **Fortnite Chapter 7 Season 4 collab (August 2026)**, via https://en.wikipedia.org/wiki/List_of_Roblox_games
- **Decline:** gradual, not a collapse. It keeps a horror audience between events.

#### 15. Plants vs Brainrots
- **Studio:** "Splitting Point - PVB" per Rolimons (the Jandel-led studio). One article credits "Yo Gurt Studio" [UNVERIFIED, conflicting].
- **Launch:** August 2025.
- **Peak CCU:** **8,654,525 on 2025-10-11** (https://www.rolimons.com/game/127742093697776). That is the **same day as Steal a Brainrot's record**, so it was a coordinated event weekend.
- **Visits:** 4.72B. **Like ratio: 94.8%**. **Server size:** 5.
- **Current CCU:** **about 4.5K live (−99.95%)**.
- **Loop:** Grow a Garden-style planting, but plants defend your lane against waves of walking Brainrots (a PvZ mash-up). Defeated Brainrots join your collection and earn money [GK].
- **Viral trigger:** two peak memes (GaG farming plus Brainrot) fused with PvZ nostalgia, pushed by cross-promotion and events in the Splitting Point network.
- **Decline:** the meme wore off, and this is the most extreme decay in the dataset.

#### 16. Dead Rails
- **Studio:** RCM Games. **Launch:** created 2025-01-01, broke out in late February 2025.
- **Peak CCU:** **1,476,198 on 2025-04-19** (https://www.rolimons.com/game/116495829188952).
- **Visits:** 6.62B. **Like ratio: 92.6%**. **Server size:** 16. **Current CCU:** about 64K (Halloween event).
- **Core loop:**
  - *Second:* shoot zombies and scavenge buildings.
  - *Minute:* **fuel the train** with coal and loot, and sell loot for money.
  - *Session:* drive the train to a fixed end distance (80 km) through day/night cycles. Classes and Bonds [GK].
- **Social hook:** co-op crew on one train with shared fate.
- **Monetization:** classes and paid items [GK, UNVERIFIED].
- **Viral trigger:** **Roblox's own TikTok, Instagram and X accounts promoted it in late February 2025**, and then the YouTubers piled in (Flamingo 2M+ views, KreekCraft, Thinknoodles, Sketch). Source: https://www.gameanalytics.com/blog/dead-rails-and-the-hit-makers-formula
- **Decline:** a fixed-length run gets repetitive. It still has a cult following: 92.6% likes and steady events.

#### 17. Fish It!
- **Studio:** Fish Atelier. **Launch:** 2024-10-21.
- **Peak CCU:** **2,716,766 on 2025-12-07** (https://www.rolimons.com/game/121864768012064).
- **Visits:** 4.8B. **Like ratio:** 82.8%. **Server size:** 20. **Current CCU:** about 79K live.
- **Growth:** about 50K average CCU in August 2025 → **over 1M by December 2025** (https://rowatcher.com/news/the-simulation-takeover-why-casual-sims-rule-roblox-in-2026).
- **Core loop:**
  - *Second:* cast and use a simplified reel.
  - *Minute:* sell fish and upgrade rods and bait.
  - *Session:* chase rarity tiers up to "Forgotten" at 1 in 25M [UNVERIFIED].
  - **Auto-fishing gives AFK progression.**
- **Monetization:** rod skins, event passes, luck boosts. "Atlantis Boost" machines take fish submissions and give **server-wide buffs**. Revenue estimate about $3.0M a month [UNVERIFIED model].
- **Viral trigger:** it took Fisch's audience when Fisch was over-monetized under DoBig. It is **simpler, idle, and friendly to kids on mobile**.

#### 18. Forsaken
- **Studio:** Forsaken Dev Team. **Launch:** created 2024-07-28, wider launch around December 2024 [UNVERIFIED].
- **Peak CCU:** **1,221,080 on 2025-11-01** (https://www.rolimons.com/game/18687417158).
- **Visits:** 5.87B. **Like ratio:** 84.4%. **Server size:** 9 (8 survivors vs 1 killer).
- **Loop:** asymmetric, Dead by Daylight-like: survivors do objectives (generators) and escape, while the killer hunts. Rounds last about 3–5 minutes [GK].
- **Social hook:** cast of Roblox nostalgia characters (Noob, Builderman, Guest 666). Played as killer vs survivors.
- **Monetization:** buy characters and skins [GK].
- **Viral trigger:** Roblox lore characters plus a "Roblox's own DBD" pitch. Won Best Survival at RIA 2025.
- **Decline:** −37.7% one week in April 2026 after an update that didn't hold players (https://rowatcher.com/news/roblox-week-of-april-6-2026-platform-slump-masks-real-winners). Halloween 30-day peak 382K.

#### 19. Ink Game (Squid Game-like)
- **Studio:** "games i think". **Launch:** 2024-12-31.
- **Peak CCU:** **810,470 on 2025-08-31** (https://www.rolimons.com/game/99567941238278).
- **Visits:** 3.37B. **Like ratio:** 79.2% (low). **Server size: 100**.
- **Loop:** survive deadly elimination mini-games (Squid Game style). Three endings: Rebel, Final Fight, Sky Squid Games. You can also play as a guard with tiered weapons.
- **Monetization:** powers (Mythic: Time Skip, Magician), emotes, cosmetics, guard progression. WON currency.
- **Viral trigger:** Squid Game Season 3 (June 2025) IP wave and 100-player spectacle [UNVERIFIED as the trigger].
- **Decline:** the IP moment passed, and paid powers lowered sentiment (79% likes). About 20K live now.

#### 20. The Forge
- **Studio:** The Forge Community. **Launch:** 2025-05-10.
- **Peak CCU:** **1.1M** (Rotrends https://www.rotrends.com/game/7671049560/The-Forge-BETA, date not given; it was the top engagement title in mid-December 2025 with 623K active).
- **Visits:** 1B. **Like ratio: 94.4%**. **Genre:** mining and forging action RPG (Robipedia lists it as the top mining game by visits).
- **Loop:** mine ores → forge weapons and armor from the ores (quality rolls) → fight mobs and bosses → reach deeper areas [GK].
- **Relevance:** **the most successful mining-based game** in the dataset. Mining works when it feeds crafting and combat power.

#### 21. Fisch
- **Studio:** Fisching (creator WoozyNate). DoBig acquired it around 2024-11-02 to 04 and **returned it to WoozyNate on 2025-08-21** (https://rosenberryrooms.com/roblox-fisch-fishing-comeback/) [UNVERIFIED secondary].
- **Launch:** 2024.
- **Peak CCU:** **1,273,618 on 2025-10-18** (https://www.rolimons.com/game/16732694052). That came **after** it went back to its creator.
- **Visits:** 5.06B. **Like ratio:** 90.8%. **Server size:** 20. **Current CCU:** about 102K live; 30-day peak 511K (Horseman Halloween).
- **Loop:** cast, then a skill reel minigame, then appraise or sell. Upgrade rods. Mutations, bestiary, new islands. Server-wide hunts (Megalodon, Kraken) [GK].
- **Monetization:** under DoBig, "4× luck" passes and coin shops were called a cash grab and players fell to about 10K [UNVERIFIED].
- **Lesson:** **over-monetization after an acquisition nearly killed it, and the creator's return revived it.**

---

### C. Evergreen giants (benchmarks)

| # | Game | Studio / launch | Rolimons peak (date) | Visits | Like % | Server | Core loop | Social hook | Retention | Monetization | Why it lasts / declines |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 22 | **Blox Fruits** | Gamer Robot, 2019-01 | **2,781,531 (2024-12-31, Dragon rework)** | 65.1B | 92.3% | 12 | Grind mobs/bosses → level → find/eat Devil Fruits → raids | Fruit trading economy (Update 15, 2022), PvP | Major update every 2–3 months; seas; Fourth Sea planned Dec 2026 | Game passes: Fruit Notifier **2,700 R$**, 2× Mastery 450, 2× Money 299, Fast Boats 299 (pass suite ~5,500 R$); permanent fruits [GK]; est. $474M+ lifetime [UNVERIFIED] | Anime IP plus huge content depth. Lost about half its January 2026 audience by mid-year; Blox Fruits Timeline: https://rowatcher.com/news/the-blox-fruits-timeline-from-2019-launch-to-60-billion-visits-in-2026 |
| 23 | **The Strongest Battlegrounds** | Yielding Arts, 2022-08 | **1,395,324 (2024-12-22)** | 19.5B | 83.7% | 15 | Free-for-all brawling with anime-hero movesets (One Punch Man style) [GK] | Skill-expressive PvP, combo clips | New characters every few months [GK] | Cosmetics and emotes, private servers [GK] | Peak on a character drop. ~96K live now |
| 24 | **Pet Simulator 99** | BIG Games, 2023-12-01 | **732,936 (2023-12-09)** | 2.68B | **94.7%** | 10 | Tap/break coins → hatch eggs → pet power → next zone | Trading Plaza, Huges as status | **Weekly Saturday 5 PM GMT update** | Triple/Octuple egg passes, **400 R$ exclusive eggs**, timed exclusives, Huge/Titanic chase. BIG Games $100M+ lifetime [UNVERIFIED]. Source: https://rowatcher.com/news/inside-big-games-how-pet-simulator-became-a-100m-roblox-empire | Pay-to-win backlash. ~96K live |
| 25 | **Adopt Me!** | Uplift, 2017 | **1,884,171 (2021-04-16)** | 45.2B | 86.4% | 35 | Care for pet tasks → age up → Neon/Mega Neon fusion [GK] | **Trading economy**, roleplay homes | Seasonal events, limited pets | Eggs, limited pets, gamepasses | Scarcity plus trading. 30-day peak 1.35M (Halloween 2026) |
| 26 | **Brookhaven RP** | Wolfpaq → **Voldex (Feb 2025)**, 2020 | **1,296,208 (2025-12-19)** | **88.9B** | 85.9% | 30 | Open roleplay: houses, cars, scenarios | Pure social sandbox | Steady updates; brand collabs (Minions × NBCU) | Soft: houses/vehicles passes; **not in top-40 earners** (https://www.maxpowergaming.co/post/roblox-s-most-played-games-aren-t-its-top-earners) | Most consistent game on Roblox (400K+ monthly average since June 2023) |
| 27 | **DOORS** | LSPLASH, 2022 | 381,720 (2023-01-29; tracking window) | 7.95B | 93.0% | 50 lobby | Co-op hotel room-by-room escape, entity avoidance [GK] | 4-player squads, jump-scare clips | Floor updates, events (Seek in The Hollow) | Revives/Knobs, modifiers [GK] | Quality horror IP with plushies. ~100K live |
| 28 | **RIVALS** | Nosniy Games, 2024-05-26 | **967,342 (2026-02-14)** | 19.0B | **93.7%** | 40 | 1v1–5v5 FPS duels, first to 5 | Ranked, streamers | Codes at milestones, seasons | **Keys** unlock guns and refresh the daily skin shop, wraps, cases. Top-earner list. Est. revenue widely varies [UNVERIFIED] | Won RIA 2026 Best Shooter. 5 straight monthly declines by July 2026 |
| 29 | **Murder Mystery 2** | Nikilis, 2014 | **2,159,199 (live 2026-10-25)** | 31.8B | 90.8% | 12 | Hidden-role rounds (innocent/sheriff/murderer) | Social deduction | Summer 2026 event: avg 341K → 633K, peak 1.1M (Nikilis) | **Knife/gun skins and trading** | Bot-farming concern: limited weapons keep trade value, so alt-farming pays (MPG August). Treat today's 2.1M with caution |
| 30 | **Bee Swarm Simulator** | Onett (solo), 2018-03 | **264,505 (2025-12-29, Beesmas)** | 4.63B | **95.6%** | 6 | Collect pollen → make honey → buy bees/gear → quests | Small co-op servers | **Rare but huge updates, annual Beesmas** | Tickets, Royal Jelly, passes [GK] | Developer trust; slow, substantial updates |
| 31 | **A Dusty Trip** | Jandel's Road Trip, 2024-02-16 | **572,612 (2024-05-18)** | 2.6B | 90.1% | 25 | Drive a car across a desert road, scavenge parts/fuel, survive hazards [GK] | Co-op road trip | Variants: Fishing/Bike/Bunker/Hardcore | Car parts, passes [GK] | Jandel's earlier hit, a forerunner of Dead Rails' "vehicle + journey" loop. ~17K live |
| 32 | **Dress To Impress** | Gigi (age 14), 2023-11-11 | **1,743,147 (2024-12-14)** | 11.2B | 90.6% | 13 | Theme → **6 min to dress** → runway → 1–5 star votes | Peer voting, Pose 28 meme | Collabs: Charli XCX Brat (651K), Lady Gaga, Wicked, Flee the Facility crossover (Jan 2026); modes | VIP items (seen as advantage), toys with codes | TikTok (150M+ posts). Spite-voting complaints. Source: https://rowatcher.com/news/dress-to-impress-how-a-teen-developer-s-fashion-game-hit-9-7-billion-visits |
| 33 | **Jujutsu Shenanigans** | Tze's Shenanigans, 2022-04 | 697,083 (2026-10-23, RoStats) | 7.8B | n/a | — | Anime battlegrounds with objectives | PvP | Updates aligned with anime seasons | Top-earner list (MPG) | Growing 44% YoY (RoWatcher March 2026) |

---

## 2. Synthesis: the 10 most repeated, proven patterns

### 1. A plot that earns money while you're idle, filled with collectibles you got through action
Collect a unit, put it on your base, and it pays you every second. Upgrade the base for more slots.
- **Proof:** Steal a Brainrot (25.8M), Grow a Garden (22.4M), Steal an Egg (14.3M), Plants vs Brainrots (8.65M), Escape Tsunami (5.0M), Kick a Lucky Block (1.7M), Break & Steal an Egg (1.31M).
- Dig & Clean uses the same idea as a **museum where tourists pay per displayed item**.
- Every one of the top 3 peaks of 2025–26 except 99 Nights uses it.

### 2. Rarity ladder plus random multipliers (mutations, traits, luck) and a "Secret" top tier
- Steal an Egg's badge funnel shows the chase working: 13.4M → 1.9M Secret → 1.0M Eternal.
- **Proof:** SAB traits (Taco ×3, ×15 luck), GaG weather mutations, Fish It "Forgotten" at 1 in 25M, Fisch mutations, Ride a Pet mutations (faster mounts), Dig & Clean hidden condition and value, PS99 Huges.

### 3. A weekly fixed-time update plus a live "Admin Abuse" event (appointment gaming)
**Every record peak in this dataset happened on an event or update day:**
- GaG: June 21 Summer Update; Aug 23 admin war
- SAB: Oct 11 (Yin Yang); Sep 13 Extinct
- Plants vs Brainrots: same Oct 11
- Steal an Egg: Sep 19 drone event
- SAB schedule: Saturday 3 PM ET plus Taco Tuesday
- GaG2: "Admin Party"
- Sailor Piece: Wednesday updates; PS99: Saturday updates

Peaks drop back fast (GaG went from 21.3M to 7.6M within an hour), but the habit builds a recurring audience.

### 4. Light, recoverable PvP theft inside a casual loop
Loss aversion is a strong engagement driver, and children crying over lost Brainrots went viral.
- **Proof:** SAB, Steal an Egg, Break & Steal an Egg, GaG (paid stealing), GaG2 (night stealing), Escape Tsunami (optional stealing).
- Defenses (lock base, owner-present protection) keep it fair enough.
- **Counter-example:** Dig & Clean had no interaction at all and lost 99% in about 10 weeks.

### 5. Scarcity clocks: global restock timers, limited stock, items that "leave the pool"
- GaG: global 5-minute restock synced across servers.
- SAB: event exclusives are removed after the event.
- Others: MM2 limited event weapons, PS99 timed exclusives, Adopt Me limited pets.
- This drives FOMO, gives trades value, and builds secondary markets (eBay and Discord for GaG).

### 6. Small servers for sims, big servers for social and horror
Sim hits run **4–8-player servers**:

| Game | Server size |
|---|---|
| Grow a Garden | 4 |
| Plants vs Brainrots | 5 |
| Ride a Pet | 6 |
| Dig & Clean | 6 |
| Steal an Egg | 7 |
| Steal a Brainrot | 8 |
| Escape Tsunami | 8 |
| Grow a Garden 2 | 8 |

Social, horror and PvP games run 25–100: 99 Nights 25, Animal Hospital 30, Brookhaven 30, Rivals 40, DOORS lobby 50, Ink Game 100. A small server makes your base and your theft feel personal, and it's easier on mobile.

### 7. "Verb a Noun" titles that state the loop in three words, often with meme characters
Steal a Brainrot, Grow a Garden, Steal an Egg, Kick a Lucky Block, Ride a Pet, Escape Tsunami for Brainrots, Dig & Clean, Break and Steal an Egg, +1 Speed Keyboard Escape. The thumbnail and title *are* the tutorial, which matters for click-through in Roblox discovery.

### 8. Selling speed, multipliers and protection rather than cosmetics
- SAB: gear and traps.
- Steal an Egg: X2 money 399 R$, X2 growth 467 R$, speed for Robux.
- Escape Tsunami: Speed 129/329 R$, **Anti-Wave 699 R$**.
- Kick a Lucky Block: x2 Cash 399 R$, Auto Kick 99 R$.
- Sailor Piece: Race Reroll 2,500 R$. Blox Fruits: Notifier 2,700 R$.
- Top earners sell competitive advantage (Gakuran, Rivals, Blox Fruits), and pure-social Brookhaven isn't in the top 40 earners (MPG).
- **The limit:** Fisch's luck passes under DoBig caused a collapse, so over-monetization kills a game.

### 9. Co-op horror or survival with one clear threat and one simple goal
- 99 Nights: keep the fire lit, survive the Deer, rescue 4 kids. 14.15M peak and the best long tail of any 2025 hit.
- Animal Hospital: spot the anomaly on shift (1.27M, **no game passes**).
- Others: Forsaken 8v1 (1.22M), Dead Rails (train to 80 km, 1.48M), DOORS, Ink Game (100-player elimination).
- These games keep audiences longer than meme sims and get platform features (Roblox's Hollow event, RIAs, film and Fortnite deals).

### 10. Push from outside Roblox: platform features, creators, crossovers and live spectacles
- Dead Rails: promoted by Roblox's official socials, then YouTubers.
- GaG × SAB admin war: platform record of 47.4M.
- SAB × Bruno Mars concert: 12.8M.
- DTI: TikTok's Pose 28 and Charli XCX collab.
- Sailor Piece: CCU-milestone code drops.
- 99 Nights: film and Fortnite.

Honorable mentions:
- **Rebirth / prestige multipliers:** SAB, Escape Tsunami, Ride a Pet, +1 Speed, PS99.
- **Offline progress:** GaG crops, Fish It auto-fish.

---

## 3. What failed or is now saturated

| Pattern | Evidence | Lesson |
|---|---|---|
| **One-mechanic novelty with <10 min sessions** | +1 Speed Keyboard Escape (7.45-min average playtime): 7.26M → 101K. Escape Tsunami (9.55 min): 5.0M → 6.8K. Kick a Lucky Block: 1.7M → ~20K. Ride a Pet: 1.55M → 23K in 3 weeks. RoWatcher: meme games average 8–12 min sessions and fade | Peaks are cheap. Roblox's 2026 algorithm now favors retention, so a game without a mid- and long-term loop dies within weeks |
| **Brainrot meme layer** | SAB −98.7%, Plants vs Brainrots −99.95%, Escape Tsunami −99.9%. Meme creators declared the subgenre "dead" in December 2025 | The meme drives the spike; the system keeps players. Theme should be swappable |
| **Clones of clones** ("Steal a X", "+1 X", "Kick/Break a Lucky Block") | Steal an Clown Egg 74K, Steal Animal Egg 107K, Steal A Verity 55K, Fake an Egg 142K, +1 Venom 47K, +1 Tongue 48K. Copycats now appear "within hours" via AI coding (https://gaminghq.eu/2026/10/18/indie-developers-roblox-copycat-games/) | A clone only wins if it ships within weeks of the original (Break & Steal an Egg 1.31M) **or** adds a genuinely new verb (Steal an Egg added hatching to SAB) |
| **Sequels splitting the audience** | Grow a Garden 2: 929K peak → 1.6K live; also cut into GaG1 | A sequel's peak doesn't carry over the original's retention |
| **Over-monetization / pay-to-win after acquisition** | Fisch under DoBig fell to about 10K and recovered after going back to its creator [UNVERIFIED secondary]. PS99 petition and pay-to-win criticism. Polygon on SAB's "best items only for cash" | Sell speed and convenience, but keep the best chase items earnable |
| **Reward-for-watching feeds** | Steal an Egg Reels, banned from the Kids and Select catalogs (Aug 2026) | Policy risk. Never tie rewards to media consumption |
| **Trading economies that invite bots** | GaG bot allegations, real-money trade; MM2 alt-farming; GaG2's August drop "possibly tied to bot enforcement" | Limited tradeables need anti-bot design (trade locks, account age gates) |
| **Isolated, solo-feeling sims** | Dig & Clean −99% in 10 weeks despite 96.5% likes | Liked but not sticky. It needed social pressure, events and an endgame |
| **Saturated genres** | ROLearn early 2026: Obby (0.20), Simulator (0.25), Tycoon (0.30) are "highly saturated" [UNVERIFIED vendor methodology]: https://rolearn.dev/insights/unsaturated-roblox-game-genres-2026/ | Ship sims/tycoons only with a strong differentiating verb |

---

## 4. White space: demand exists but no dominant game holds it

1. **Digging / junk / treasure tycoon with social pressure and a long-term loop.**
   - Demand proof: Dig & Clean hit 269K with 96.5% likes, The Forge hit 1.1M (mining → crafting), "+1 Pickaxe Swing for Eggs" 54.6K, Mine Antarctica 27K.
   - No one holds it: Dig & Clean is at 2K now and The Forge at about 12K.
   - Missing pieces, by pattern: a base or museum that earns while idle (#1), weekly events and admin digs (#3), raids or "claim-jumping" on rare finds (#4), and a global stock or limited dig-site rotation (#5).
   - **This is the clearest gap for a junkyard-digging game.**
2. **Co-op "work a shift" sims with light horror or anomaly twists.**
   - Animal Hospital reached 1.27M with **no monetization at all**, and Karinderya reached 294K.
   - Nobody has combined the shift loop with Brainrot-style collection and economy depth yet.
3. **Survival plus base collection.** 99 Nights has the best retention of the 2025 hits but only light collection. A co-op survival game where rescued or collected things earn on your base is unclaimed.
4. **Fishing plus base or aquarium plus theft.** Fishing is proven (Fish It 2.7M, Fisch 1.27M, Hooked!'s Q1 2026 surge), but both leaders are solo-ish loops. An aquarium that earns while idle and can be raided would combine patterns #1, #2 and #4.
5. **Mounts and traversal as progression.** Ride a Pet had the longest average playtime of any 2026 viral hit (14.66 min), and an ARPG or exploration version is open.
6. **Competitive sports with ranked seasons.** ROLearn rates it "unsaturated" [UNVERIFIED]. Volleyball Legends (152K), Blue Lock: Rivals (109K) and Illegal Soccer (77K) show demand, but no game has a breakout above 1M.
7. **Narrative horror with a story** (DOORS-like). ROLearn calls it under-served [UNVERIFIED]. Roblox itself promotes horror through The Hollow.

---

## 5. Source index (main)

**Trackers**
- Rolimons game pages: https://www.rolimons.com/game/{placeId}
- RoStats: https://rostats.io/records
- RBLXStat: https://rblxstat.com/lists/record-breaking-roblox-games
- RoWatcher: https://rowatcher.com
- Rotrends: https://www.rotrends.com

**Monthly rankings:** Max Power Gaming (July, August and September 2026; links in "How to read this").

**News**
- Kotaku (Steal an Egg Reels): https://kotaku.com/roblox-cracks-down-on-doomscrolling-games-like-steal-an-egg-that-forces-players-to-watch-reels-while-running-on-a-treadmill-2000727952
- PocketGamer.biz (GaG): https://www.pocketgamer.biz/robloxs-grow-a-garden-hits-industry-record-213m-concurrent-users-surpassing-pubg-fortnite-and-more/
- PocketGamer.biz (SAB 25M): https://www.pocketgamer.biz/robloxs-steal-a-brainrot-becomes-first-game-to-surpass-25m-concurrent-players
- GamesIndustry.biz (Bruno Mars): https://www.gamesindustry.biz/roblox-claims-bruno-mars-steal-a-brainrot-performance-drew-a-record-128-million-concurrent-users-issued-54-million-brainrot-collectibles
- GameAnalytics (Dead Rails): https://www.gameanalytics.com/blog/dead-rails-and-the-hit-makers-formula

**Wikipedia**
- https://en.wikipedia.org/wiki/Grow_a_Garden
- https://en.wikipedia.org/wiki/Steal_a_Brainrot
- https://en.wikipedia.org/wiki/List_of_Roblox_games

**Roblox**
- Q2 2026 results: https://respawn.outlookindia.com/gaming/gaming-news/roblox-q2-2026-revenue-soars-36-to-15b-despite-bookings-miss
- Age-check release: https://ir.roblox.com/news/news-details/2026/Roblox-Requires-Users-Worldwide-to-Age-Check-to-Access-Chat/default.aspx
