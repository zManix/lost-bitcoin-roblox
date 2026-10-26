# Phase 2 playbook: the Roblox market check (is it proven? does it already exist? what's rising?)

Rule from experience: on Roblox, small versions of nearly EVERY idea already exist. "Fresh" means "nobody successful
owns it", never "nobody ever tried". Three concepts in a row were killed because the freshness check was too shallow
(10 searches). Do at least 40 searches before claiming anything is new, and let an adversarial subagent do 40+ more. In a test run,
61 searches across 5 families still missed the decisive competitor; it only surfaced via a SHELTER/BASE synonym (family 6).

## 1. What's rising right now
`python <skill>/scripts/roblox_market.py charts --n 15` prints every sort the API returns (front page + genre sorts
when present; `--sort <id>` filters). Note the formulas that are rising (a new game at 20K+ live within weeks is a
signal). During event weeks (Halloween, holidays) the front page is dominated by event/horror games: look at the
genre sorts too, and say the snapshot is event-skewed.

## 2. Searches (at least 40, in 6 families)
Run `roblox_market.py search "q1" "q2" ... --n 8 --enrich --json <ws>/research/market_search.json`. `--enrich` adds
visits, created date, favorites and like % to every unique game and prints one deduped table sorted by live players,
so you don't need a separate details call per lead. Omni-search is semantic and noisy ("keeper" returns soccer
games): judge results by the enriched table, not the raw lists.
1. **Direct:** the game's title, title words, "<core verb> the <core noun>", the premise in 3 words, the
   developer's own phrases from the store page.
2. **Core verb + object:** e.g. "dig", "find the", "break the cube", "punch blocks", "1 million blocks", "feed the",
   "carry", "mine a".
3. **Theme:** the setting/creatures/items ("junkyard", "haystack", "spa", "hamster").
4. **Twists you're considering:** each planned differentiator as its own query ("carry together", "ghost players",
   "co-op hatch").
5. **Formula names:** "+1 <x>", "steal a", "grow a", "ride a", "chop a", "<x> for eggs", "<x> tycoon", "<x> simulator".
6. **Shelter/base nouns + trending characters:** what the player defends, lives in or returns to (bunker, base, dome,
   house, camp, fort, outpost, hatch, shop, plot) combined with the core verb ("bunker defense", "defend the base",
   "dig to base"), plus any character/meme names trending in the charts right now (e.g. a viral NPC). Viral games
   often name the character, not the mechanic.

## 3. Details on everything close or big
`roblox_market.py details <ids>`, `votes <ids>`, `passes <ids>` for:
- every close match
- the top 3–5 games of the lane (proven price points)
- the 3 biggest rising games from the charts

For peak concurrent players and trends: WebFetch `https://rowatcher.com/games/<universeId>/<slug>` ("all-time peak,
date, trend"). Caveat: RoWatcher's "all-time peak" only covers its tracking window. Trust it for games created in
the last ~2 months; for older games, use visits/favorites/like % and write "peak unknown" (e.g. a game with 60M
visits showing a "peak" of 3K is a tracking artifact, not the truth).

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
