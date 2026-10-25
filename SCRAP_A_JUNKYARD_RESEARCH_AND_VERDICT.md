# SCRAP A JUNKYARD: final concept (v4), research and verdict

Date: 2026-10-25. This is the FINAL pick, after 3 rejected concepts and 2 adversarial reviews.
Raw research is in `research/`. All Roblox numbers come from Roblox's own APIs or RoWatcher, pulled today.

## 0. The hard lesson from about 350 Roblox searches

| Concept | What killed it |
|---|---|
| v1 Scrap to Riches (straight port) | Two straight Lost Bitcoin ports already exist and are dead: **Clear the Junkyard** (Oct 2: physics scrap mountain, 3 friends, find the lost Golden Key; **2 live, 60% likes**) and **Find The Lost Bitcoin** (about 30K visits, dead) |
| v2 Forge a Bot | 6 junk-to-worker-robot games exist, all under 650 live |
| v3 Haul & Hatch | Team carry already shipped: **Steal Eggs Together** (carry GIANT/TITAN eggs with a friend; 1.1K live). Crew giant egg: 0 live. Solo Lift Rock for Eggs does better (7.4K) |

**What the data actually says wins on Roblox in Oct 2026:** take a formula that is rising RIGHT NOW, put a strong new theme and verbs on it, out-execute the leader, and ship fast.

| Proof | Formula | Leader | How far behind |
|---|---|---|---|
| Steal An Egg: 1.2M live | Steal a Brainrot + eggs | Steal a Brainrot | Weeks |
| Break and Steal an Egg: 108K live, growing, 1.3M peak | Steal An Egg + "break" | Steal An Egg | Weeks |
| Ride a Dino: 65K live | Ride a Pet + dinos | Ride a Pet | Weeks |

Being first with a "fresh" idea is not what wins. Every idea already exists somewhere. **Picking the right lane and executing better does.**

## 1. The lane: "clear the area" runs (the Chop A Forest formula)

**Chop A Forest:** created Sep 21, 2026. **76K peak (Oct), 52K live now, 29.1M visits, 93.2% likes, 107K favorites.** One leader and no strong second:
- Chop Together: 356 live
- Clear the Junkyard: 2 live
- Chop a Bamboo Forest: 79 live

Other skins of "clear it all" that work:
- Clean all the Leaves: 232M visits, 7K live
- Clean the House: 6.3K
- Smash the City: 4K
- Destroy a Vault: 9K

Its skeleton (fan wikis and the store page):
- **Runs:** press START A RUN, begin with bare hands, clear every zone. "Solo & friend runs save."
- **Run currency:** coins buy run-only tools: Axe 150 → Backpack 175 → Vacuum 1,000 → Chainsaw 7,500. Run vehicles carry 50 / 75 / 100 logs (500 / 2,800 / 6,500 coins).
- **Permanent currency:** Gems buy classes (up to 4,000 Gems: +200% power, +100% sell, +100% rare luck), permanent vehicles (125–200 logs), pets and luck.
- **Gems come from:** mutated trees (Golden ×3, Candy ×4, Frost ×5), bosses, daily (35 every 6 h), group (100 once).
- **Class shop:** random stock that restocks every 5 minutes, the Grow a Garden scarcity clock.
- **Day and night:** 8-minute day, 4-minute night. Night enemies steal logs and regrow trees. Peaceful mode exists.
- **Bosses:** 8 bosses, one at the end of each zone. Pets come from eggs that bosses and night enemies drop. Speedrun timer.

**This is Lost Bitcoin's loop:** start with bare hands, then 64 upgrades through hands → backpack → vacuum → magnet → winch. The original port idea was right. My v1 had the wrong frame: one long solo save, no runs, no permanent layer, no clocks.

## 2. Why the two junkyard ports died, and how we avoid it

| Clear the Junkyard / Find the Lost Bitcoin did this | We do this |
|---|---|
| A real-physics pile that "shifts and slides" (lag on phones; crashes count as bounces) | Anchored, pooled junk props in scripted STACKS that topple with tweens; no free physics |
| Party lobby, then drop in (friction before fun) | START A RUN pad right in the hub, like Chop. Friends join your run in one tap |
| "Find the one key" as the whole goal | Clear every pile → boss → next zone. Finding the Golden Drive is a *bonus*, not the goal |
| Sell to an NPC | Lost Bitcoin's **furnace coin fountain**: throw, tip out a backpack, blow a vacuum tank, shoot a magnet cluster (Feed the Fire: 98% likes) |
| 60% likes (thin quality) | Juice budget: sounds, squash, flame bursts, number pops (section C17 of the prompt) |

## 3. What's NEW versus Chop A Forest (our reason to exist)

1. **Throughput verbs instead of "hit tree, sell".** Packing and tipping out the backpack, vacuum tank blow-out, magnet cluster shots, winching heavy items, all into a live furnace that shoots coins. This is Lost Bitcoin's best idea, and it is not on Roblox at scale.
2. **Junk Tower collapses.** Pull the right piece and a whole stack topples. Satisfying, clip-friendly destruction (Smash the City and Destroy a Vault prove destruction sells).
3. **No-gun bosses.** Chop A Forest hands you an AK-style rifle and a pistol for its bosses. Ours are **Junk Golems** made from the zone's last pile. You beat them with YOUR tools: vacuum the armour plates off, blow them into the furnace, magnet the core. Safer for kids and moderation, and it fixes the ancestor complaint "the endgame takes your tools away".
4. **Fire hatch.** Scrap Capsules (from bosses, nights and rare piles) hatch inside the furnace. The flame color climbs white → blue → purple → gold → rainbow, then a Scrapkin pet pops out. The adversarial review confirmed this mechanic is unclaimed on Roblox.
5. **Mystery Sticks** (Lost Bitcoin's USB reader): a rolling-digit reveal at the Reader gives bonus Gems. In each zone, ONE stick is the **Golden Drive** (big Gem jackpot plus a badge), with odds shown.
6. **Night Raccoon Bandits**, non-violent. They sneak in at night and steal junk from your backpack and wagon or re-pile cleared junk. Shoo them with the Blower and they drop coins or a Capsule. A Peaceful mode toggle is included.

## 4. Verdict

**Honest score: 7.5/10.** Not 10, and here's exactly why:

| Factor | Score | Evidence |
|---|---|---|
| Lane demand | 9 | Chop A Forest is at 52–76K and still near its peak; "clear it" skins at 4–9K each |
| Competition in our theme | 8 | Both junkyard attempts are dead for fixable reasons (physics lag, lobby friction, weak goal, low quality) |
| Freshness | 6 | Structurally a Chop-like. The verbs, bosses, fire hatch and sticks are new; the skeleton isn't. No skeleton is new on Roblox |
| First 60 s | 9 | Junk in the furnace under 10 s, first upgrade under 30 s, first stack collapse under 60 s |
| Retention (28-day ranking) | 7 | Runs, permanent Gems, classes, pets, 5-min restock, nights, daily. Chop-likes haven't proven a 28-day tail yet |
| Mobile / performance | 8 | No physics piles; budgets set |
| Honesty / policy | 10 | No guns, no paid hatches, odds shown, PolicyService gating |

**What turns 7.5 into a real 9–10 is not the concept, it's you:**
1. **Ship the first playable in about 3 weeks.** Chop A Forest's lane is hot NOW; clones will fill it.
2. **Update every Saturday for 8 weeks** (new zone, Golem or Scrapkin set). Every record day in the research was an update day.
3. **Juice.** Furnace fountains, stack collapses and the flame reveal must feel incredible. The 60%-likes junk port shows what thin quality gets you.
4. **Thumbnails.** Show a giant junk tower collapsing into a furnace coin explosion. Test 3–5 thumbnails; Roblox's built-in testing gave +8.5% play-through on average.

Anyone who promises you a 10/10 on paper is lying. This is the best bet the evidence supports.

**Names:**
- **Scrap a Junkyard** ✅ my pick: "Verb a Noun" in Chop A Forest's pattern, describes the game, no match on Roblox
- Clean Up a Junkyard
- Crush a Junkyard
- Junkyard Cleanup Crew
- Burn the Junkyard (risky wording for kids)

**Top 3 risks**
1. **A Chop A Forest junk update, or a fast clone.** Fix: speed plus the unique verbs. Their skeleton can't copy our tool feel overnight.
2. **Chop-likes fade** (no 28-day proof yet). Fix: permanent meta (classes, pets, index), weekly zones, speedrun leaderboards.
3. **Many junk props on phones.** Fix: pooled anchored meshes, per-run instanced zones streamed, a part budget, the QualityController.
