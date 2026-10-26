# Phase 2 playbook: the Roblox market check (is it proven? does it already exist? what's rising?)

Rule from experience: on Roblox, small versions of nearly EVERY idea already exist. "Fresh" means "nobody successful
owns it", never "nobody ever tried". Three concepts in a row were killed because the freshness check was too shallow
(10 searches). Do at least 40 searches before claiming anything is new, and let an adversarial subagent do 40+ more.

## 1. What's rising right now
`python scripts/roblox_market.py charts --n 15`. It reads Top Trending, Up-and-Coming, Top Playing Now and Fun with
Friends. Note the formulas that are rising (a new game at 20K+ live within weeks is a signal).

## 2. Searches (at least 40, in 5 families) — `roblox_market.py search "q1" "q2" ... --n 8 --json <ws>/research/market_search.json`
1. **Direct:** the game's title, title words, "<core verb> the <core noun>", the premise in 3 words, the
   developer's own phrases from the store page.
2. **Core verb + object:** e.g. "dig", "find the", "break the cube", "punch blocks", "1 million blocks", "feed the",
   "carry", "mine a".
3. **Theme:** the setting/creatures/items ("junkyard", "haystack", "spa", "hamster").
4. **Twists you're considering:** each planned differentiator as its own query ("carry together", "ghost players",
   "co-op hatch").
5. **Formula names:** "+1 <x>", "steal a", "grow a", "ride a", "chop a", "<x> for eggs", "<x> tycoon", "<x> simulator".

## 3. Details on everything close or big
`roblox_market.py details <ids>`, `votes <ids>`, `passes <ids>` for:
- every close match
- the top 3–5 games of the lane (proven price points)
- the 3 biggest rising games from the charts

For peak concurrent players and trends: WebFetch `https://rowatcher.com/games/<universeId>/<slug>` ("all-time peak,
date, trend").

## 4. Read the numbers honestly
| Signal | Meaning |
|---|---|
| Peak 50K+ and still above 10% of peak | proven and alive |
| Peak 50K+, now < 10% of peak | proven demand, weak retention: your edge must be the retention layer |
| Many attempts, all < 1K live | the idea does NOT pull (e.g. junk→worker-robots: 6 games, all < 650) |
| One leader, weak clones | an open lane if you ship fast (e.g. Chop A Forest: 52–76K, clones < 400) |
| Exact copy of your concept exists and is dead | find out why (lag, lobby friction, weak goal, low like-ratio = quality) before deciding |
| Like ratio < 80% | quality problem, not concept proof |

## 5. Write MARKET.md
- the charts snapshot
- a close-match table (name, live, visits, created, like %, how close)
- lane leaders (peak, current, loop)
- proven price points (from passes)
- "what exists / what's open"
- every query you ran (so the reviewer can see coverage)
