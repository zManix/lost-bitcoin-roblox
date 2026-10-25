# HAUL & HATCH: final concept, research and verdict

Date: 2026-10-25. This is concept v3.
- v1, "Scrap to Riches" (a straight port), scored 6/10.
- v2, "Forge a Bot", was KILLED by an adversarial review. Six junk-to-worker-robot games already exist on Roblox, all under 650 live players. Only robot *fighting* games pull (Steel Fighters 29K). See section 5.

Raw research (about 26K words, sources inline) is in `research/`. Roblox numbers come from Roblox's own APIs, pulled 2026-10-25.

---

## 1. The one-line pitch

**Team up to haul giant junk clumps into the Big Furnace. The fire burns the junk away and a Scrapkin creature hatches out. The bigger the clump, the rarer the Scrapkin, and the more friends you need to lift it. Every player who carried gets their own hatch.**

## 2. Why this, backed by evidence

| Part | Proven by (live data 2026-10-25) |
|---|---|
| **Hatch a creature with a rarity ladder, a Secret tier, size and paint mutations** | Steal An Egg: 9.46B visits, **1.2M live today**, 14.3M peak. Its badges show 13.4M players → 1.9M hatched a Secret. Ride a Dino: 65K live, 527K favorites in 2 months |
| **Creatures sit on your plot and earn every second, even offline** | Every #1 sim of 2025–26: Steal a Brainrot, Grow a Garden, Steal An Egg, Merge a Nuke (452M) |
| **Your collectible IS your progression** (a Scrapkin follower adds lifting strength) | Ride a Pet had the longest sessions of 2026 (14.66 min avg). Ride a Dino |
| **Weight gates** ("Too heavy: 55 kg / you 12 kg") | Lost Bitcoin's trailer. Carry Heavy Eggs (5.2M visits), but solo, and now dead at 157 live |
| **TEAM carry** (the twist) | Co-op carry obbies chart in Roblox's own "Fun with Friends" sort: Carry the Glass Together (7K live), Carry A Friend (310K likes), Chained (142K likes). Steam: R.E.P.O. (about 16M sold, team-carry physics loot), Chained Together. Backseat Rally (46K live, 112K favorites in 3 weeks) proves "needs a friend" games are rising **right now**. Roblox's ranking counts **co-play days** |
| **Throwing junk into a fire** feels great | Feed the Fire: 98% likes, 3.1M visits. Lost Bitcoin's whole trailer |
| **Reveal tension** (flame color climbs white → blue → purple → gold → rainbow) | Lost Bitcoin's rolling-digit USB reader, Steal An Egg hatching, Dig & Clean's cleaning reveal (269K peak), TCG Card Shop's pack opening |
| **Risky run against a timer** (the Crusher sweeps the outer heap) | Escape Tsunami for Brainrots (5.0M peak), Dome Keeper, Motherload |
| **Ragdoll comedy when the Crusher hits you** | Ragdoll Reality (53K live, Oct 13), R.E.P.O., PEAK clips |
| **Server event that needs everyone** (Titan Clump) | 99 Nights (394K live now), Feed the Fire storm, Lethal/R.E.P.O. quota |
| **Restock clock** (Junk Train every 5 min) | Grow a Garden (22.4M peak) |
| **Weekly update + admin event + limited Scrapkins that leave the pool** | Every record day on Roblox was an event day (admin war: 47.4M on the platform) |
| **Server of 8, "Verb & Verb" title that explains the game** | Ride a Dino 8, Steal An Egg 7; Steal a Brainrot, Grow a Garden, Chop A Forest |
| **Proven pass prices** (pulled from live game-pass APIs) | 2x Money 99–399 · VIP 149–379 · 2x Luck 149–199 · Offline/Storage about 149 |

## 3. Freshness check (about 200 Roblox searches in total)

| Closest game | Live | Why we're different |
|---|---|---|
| Carry Heavy Eggs! (carry an egg home, train strength, pets earn) | 157 | **Solo**, with PvP fighting over eggs. Ours is **team** carry, a furnace reveal and a shared win |
| Carry the Glass Together and other carry obbies | 7K | Obby only: no collecting, no economy, no reason to return |
| Steal An Egg / Dig For Eggs / Drill for Eggs | 1.2M / 7.2K / 3.3K | Eggs and theft or digging; nothing heavy, no teamwork |
| Feed the Fire / feed the pit | 7.8K / 363 | Feeding a fire for money, no creatures, no team carry |
| Dig & Clean | 2.2K | Solo reveal and museum, died from no interaction |

**No game found does team-carry + furnace hatch + plot income.** Every *part* is proven. The *combination* and the *social twist* are new. Honest caveat: on Roblox, small versions of nearly everything exist, so "fresh" means "nobody successful owns it", not "nobody ever tried".

## 4. Design guardrails taken from the research and both reviews
- **Short sessions die** (+1 Speed −98.6%), so target 20-minute sessions, with offline income and dailies.
- **Solo collecting dies** (Dig & Clean 269K → 2K), so team carry, shared events, a friend boost, and visiting plots.
- **Don't punish newcomers.** No Crusher in Ring 1, nothing is ever lost, the Titan event scales down to 1 player.
- **No hidden recipes.** A live "Hatch Odds" card is shown on every clump, which is clearer and also meets Roblox's odds rule.
- **No paid hatches.** Luck boosts show exact odds and are hidden where PolicyService restricts paid random items.
- **No trading at launch.** Trading attracts bot farms and scams.
- **Mobile first.** Tap LIFT, auto-follow carry, one DROP IN button at the furnace. One rendered follower per player. No free physics piles.
- **Rebirth is clear.** Cash and upgrade levels reset; Scrapkins, Index and cosmetics are kept; +25% income and a new Heap ring. A "You keep" screen is shown first.
- **6 systems in the first build** (heap + carry, furnace hatch, plot income, upgrades + rebirth, Crusher + Junk Train, Index + daily). Everything else ships in weekly updates.
- **Kids/Select:** launch to age-checked 16+ players first (the new-game rule), aiming for 250 engaged plays within 60 days. Minimal maturity rating, ID and 2SV ready.

## 5. Why Forge a Bot (v2) was killed
- **The space is crowded and dead:** +1 Ore to Forge Robots (4 live), Build A Golem (495), Build A Mech (134), Scrap Titans (24), Scrap Empire Tycoon (0), Robot Evolution (20).
- **Only robot fighting pulls players:** Steel Fighters (29K), Create a Robot Fighter (11.6K).
- **Too many systems** (about 18).
- **A hidden recipe** a 9-year-old wouldn't understand.
- **The shared mountain got stripped** by 32 bots.
- **Four overlapping clocks.**
- **A storm that punished new players.**

## 6. Verdict

**Honest score: 8/10.**

| Check | Score | Notes |
|---|---|---|
| Every pillar proven by live hits | 10 | Section 2 |
| Fresh combination | 8 | Nothing like it is successful, but "carry something heavy" has small solo versions |
| First 60 s fun | 9 | Lift a glowing clump next to the furnace → flame reveal → Scrapkin, under 45 s |
| 28-day retention design | 8 | Pads, offline, Index, rebirth rings, weekly limiteds |
| Co-play | 10 | It's the core twist: a friend = a bigger clump = a rarer hatch, and everyone gets one |
| Mobile and performance | 7 | Team-carry netcode is the biggest technical risk (see risks) |
| Monetization honesty | 10 | Proven prices, no paid hatches, odds shown |

**Why not 10:**
1. Nobody can prove a launch result on paper.
2. Team-carry sync on phones must feel smooth or the twist turns into a bug.
3. The creature-hatch genre is busy, so art and juice must be top tier.

It only hits 10 in the real world if you ship the first build in about 3 weeks and then **update every Saturday for 8 weeks**. Every record day in the research was an update day.

**Name pick:** **HAUL & HATCH**. Two verbs that explain the whole loop; nothing on Roblox uses it. Others: Carry & Hatch, Burn to Hatch, Junk Hatchers, Heave & Hatch.

**Top 3 risks and fixes**
1. **Carry sync jitter.** The clump is not a raw physics object. The server moves it along the carriers' average position, and clients smooth it. Prototype this FIRST (milestone M1), with a "done when" test of 4 clients on emulated phones.
2. **Genre fatigue / copycats.** Lead with what clones skip: the team-lift moment, Crusher ragdoll clips, and the flame-color reveal. Ship fast; weekly limited Scrapkins.
3. **Empty servers at launch.** Every clump size up to Boulder is soloable with upgrades and your follower. The Titan's requirement scales with player count. Friend invite and referral rewards.
