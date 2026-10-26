# Roblox platform facts (snapshot: Oct 2026)

These come from research in Oct 2026 (Roblox investor reports, creator docs, DevForum staff, Rolimons/RoWatcher). They
change. If today is more than about 60 days after Oct 2026, spend 5 minutes re-checking the items marked ⟳ (WebSearch
+ create.roblox.com) before relying on them.

## Ranking / discovery ⟳
- Since 2026-06-15 Roblox evaluates on 28-day windows and favors highly retentive games.
- Top signals (users from Recommended-For-You only, averaged per user): play-through rate, first-play bounce (< 60 s
  and 61–180 s), play days (D1, D2–7, D8–28), playtime (capped at 60 min per user per day). Second tier: co-play days,
  qualified sessions, spend days, Robux spent.
- Penalized: titles implying money or giveaways, close clones, thumbnails that don't match gameplay.
- A custom thumbnail is required for Home impressions. Keep 2–5 thumbnails active (Roblox tests them per segment;
  about +8.5% play-through on average).
- Update notes ≤ 60 characters, max once per 3 days.

## Audience ⟳
- DAU about 123–132M (Q1–Q2 2026). About 80% mobile, 17% PC, 3% console (FY2024 split).
- Age-checked split about 35% under 13, 38% 13–17, 27% 18+.
- Median session 6.6 min; the 19–24 min bucket retains best. A good D1 is relative; the top 2% of 19–24 min games
  reach about 32% D1, 8.5% D7, 3% D30.
- New games reach age-checked 16+ players first. Kids/Select catalogs need 250 engaged plays from 16+ within 60 days
  (or an expedited path), ID verification and 2-Step Verification.

## Proven patterns (2025–2026 hits)
1. A plot/base that earns while you're away, filled by active play (Steal a Brainrot, Grow a Garden, Steal An Egg,
   Merge a Nuke).
2. A rarity ladder + random multipliers (mutations/sizes) + a "Secret" top tier (Steal An Egg: 13.4M players → 1.9M
   hatched a Secret).
3. A fixed weekly update + a live admin event (every record peak was an event day; the admin war hit 47.4M concurrent
   on the platform).
4. Light recoverable theft with defenses (viral, but those games also collapse fastest).
5. Scarcity clocks (Grow a Garden's 5-min global restock; limited items that leave the pool).
6. Small servers for sims (6–8); social/horror 20–100.
7. "Verb a Noun" titles that explain the loop.
8. Sell speed, multipliers, protection and visible cosmetics; over-monetizing kills games (Fisch).
9. Co-op with one threat/goal retains far longer than meme sims (99 Nights).
10. Collectible = progression gives the longest sessions (Ride a Pet 14.7 min).

## Failure patterns
- Sessions under 10 min collapse.
- Meme-only hooks fade (brainrot games down about 99%).
- Late clones stall at 50–140K unless shipped within weeks.
- Solo collecting fades (Dig & Clean 269K → 2K).
- Trading invites bot farms.
- "Find the one item" with no long-term layer spikes then dies (Search For The Needle 86K → 6K).
- Exact straight ports of Steam games often already exist and are dead: check first.

## Monetization ⟳
- Creators get 70% of passes/products. DevEx $0.0038 per Robux.
- About 1.4% of DAU pay daily; the median purchase is $0.51–1.29.
- Proven pass prices (live, Oct 2026): 2x Money 99–399 · VIP 149–379 · 2x Luck 149–199 · Offline/Storage/Auto ~99–149 ·
  permanent tools 99–249 · pets 499. Timed boosts ~29–49. A permanent pass ≈ 8–10× its 15-minute boost.
- Policy:
  - Paid random items, AND anything that changes paid odds (luck boosts), must show exact % odds before purchase.
  - Check `PolicyService:GetPolicyInfoForPlayerAsync` (ArePaidRandomItemsRestricted / IsPaidItemTradingAllowed) and
    hide restricted items.
  - Simulated and real gambling are banned.
  - Unrated experiences are unplayable (fill the maturity questionnaire).
  - Rewards for watching media feeds are banned from Kids/Select.
- Leaderboard/competitive modes: make paid boosts not count (ranked runs ignore boosts) so it isn't pay-to-win.

## Tech facts ⟳
- `Lighting.Technology` is deprecated. Use `LightingStyle` (Realistic/Soft) + `PrioritizeLightingQuality`.
- Highlight: up to 255 per client (the first one costs the most GPU, up to ~1 ms on mobile).
- UnreliableRemoteEvent payloads > 1,000 bytes are dropped. About 500 remote calls/s per client.
- DataStore value ≤ 4,194,304 chars; Get/Set budget 60 + 40×players per minute per server.
- OrderedDataStore: integers only, 100 per page, writes 30 + 5×players/min, list reads only 5 + 2×players/min per
  server. Cache boards on the server; new period = new store name.
- MemoryStore: memory 64 KB + 1.2 KB × users; requests 1,000 + 120×players/min; sorted-map reads ≤ 200 items.
- `buffer`: up to 1 GiB; copied across remotes/Actors. EncodingService offers compression (zstd) for saves.
- EditableMesh: needs an ID-verified 13+ owner, has memory-budget failures, doesn't replicate. Avoid for core geometry
  (it showed as boxes in live games for one user).
- Client-created Terrain: staff say avoid. Workspace Terrain is shared (no per-player terrain).
- Phones: target ≤ 300–500 draw calls, ≤ 300k–500k visible triangles, a few thousand parts; textures ≤ 512² (1024² for
  hero). About 60% of Android players have 2–4 GB RAM. Crashes count as bounces.
- MeshId can't be set by scripts: upload once, keep a template MeshPart, clone it. TextureID is runtime-settable;
  SurfaceAppearance maps only at edit time.
