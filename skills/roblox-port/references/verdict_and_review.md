# Phase 3–4 playbook: concept, verdict, adversarial review, pivots

## 1. Pick the concept
Start from the source game. Then:
1. **Straight port** (same mechanics, new name/art) when MARKET.md says the lane is open AND the loop is proven
   (on Steam or Roblox).
2. **Port + Roblox layer** (most common): keep the source's core loop and add what Roblox players need:
   - friends in the same space
   - short sessions with saves
   - a daily reason to return
   - visible show-off cosmetics
   - a weekly-update-ready structure
3. **Pivot** if the straight version already exists and died, or the idea doesn't pull: find the nearest RISING
   Roblox formula whose skeleton matches the source game's verbs, and put the source's best mechanics on that skeleton.

   Real example: a junkyard digging game → its straight port was dead on Roblox twice → its loop matched "Chop A
   Forest" (rising, 52K live), so the pivot became "Scrap a Junkyard" on Chop's run structure with the source's
   furnace and tool verbs.

## 2. Score it with this rubric (out of 10; show the table)
| Factor | What earns a high score |
|---|---|
| Lane demand | Live Roblox evidence (peaks, current, likes) of the core loop |
| Competition | No successful owner of the exact combo; weak clones |
| Freshness | A clear twist players can see in a thumbnail; at least 40 searches support it |
| First 60 s | Fun in under 10 s, first reward in under 30 s, no wall of text (bounce rate is a top ranking signal) |
| 28-day retention | Daily reason, meta progression, collection, weekly updates (Roblox ranks on 28-day retention since June 2026) |
| Co-play | Friends make it better (co-play days are a ranking signal) |
| Mobile / perf | Feasible on 2 GB Android phones (80% of players are on mobile) |
| Honesty / policy | No paid random items, odds shown, nothing pay-to-win against players |

Total = weighted average, rounded to 0.5: Lane demand ×2, Competition ×1.5, 28-day retention ×1.5, every other factor
×1 (divide by 10). Then adjust by at most ±0.5 with a one-line reason, and also state a realistic range (e.g.
"6.8, realistically 6–7").

Be honest. NEVER promise a 10/10 on paper: launch results depend on execution, weekly updates and thumbnails. When the
user asks for a 10, explain what turns the paper score into a real result (ship fast, update every Saturday, juice,
thumbnail testing).

## 3. Adversarial review (always; up to 2 rounds)
Spawn a fresh general-purpose subagent (it must NOT see your reasoning, only the files) with this brief:

"You are a ruthless Roblox game-design reviewer and market analyst. Today is <date>. Read <ws>/VERDICT.md,
<ws>/MARKET.md and <ws>/STUDY.md. Your job: try to KILL this concept with evidence. Do not edit files.
1. Freshness: run at least 40 varied Roblox searches yourself with `python <skill>/scripts/roblox_market.py search
   ...` aimed at the concept's core loop AND its twist (synonyms, formula names, the theme), plus `details` on close
   matches. Report every close match (live, visits, created, how close).
2. Holes: what's weak or confusing for a 9-year-old on a phone, too complex for a first build, or contradicts
   MARKET.md (server size, griefing, solo viability, performance, monetization rules).
3. Missing proven pillars worth adding (with evidence) and ones to skip.
4. A ranked fix list (max 15) and your honest score /10 before and after the fixes. If a BETTER concept is supported
   by the data, name it and justify it with numbers.
Final message ≤ 900 words with the close-match table."

No subagent tool available? Then do the review yourself as a deliberately separate HOSTILE PASS: re-read only the
three files (not your notes), run 40+ NEW searches (different words than Phase 2, especially family 6), argue against
your own concept, and label the round "self-review (not independent)" in VERDICT.md. If a remote-session tool exists
(e.g. create_session), you may use it instead, but it needs the files copied in.

Then:
- **VERIFY its claims yourself** (run `details` on its top matches). Reviewers can be wrong; so can you.
- If it finds the twist already shipped and dead, or a much better lane, pivot (§1) and run ONE more review round.
- Apply the fixes that survive. Record everything in VERDICT.md under "Review rounds".

## 4. Naming
- "Verb a Noun" / "Verb the Noun" titles explain the loop (Grow a Garden, Steal an Egg, Chop A Forest, Find the
  Glowing Box).
- Check the name with `roblox_market.py search "<name>"`. Avoid the source game's exact title (IP) but keep its
  search words when legal (e.g. "Find the Glowing Box" still catches "find the box").
- Give 5 options and pick one.

## 5. VERDICT.md template
Example of an honest verdict with review rounds: references/examples/example_VERDICT_dome_keeper.md.
1. One-line pitch
2. What the source game is (3 lines)
3. The evidence table (part → proven by → numbers)
4. Freshness check (the close-match table)
5. Design guardrails (what to avoid, from MARKET + reviews)
6. Score table + honest total + "what makes it a real 9–10"
7. Name pick + 4 alternatives
8. Top 3 risks + fixes
9. Review rounds (findings, what changed)
