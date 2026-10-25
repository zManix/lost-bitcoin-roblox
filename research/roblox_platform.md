# Roblox Platform Research: What Makes a Game Succeed (2025-2026)

Compiled 2026-10-25. Every number has a source link. **[UNVERIFIED]** marks figures from single, unattributed, or low-quality sources, and also claims I could not confirm. Q3 2026 earnings (due about Oct 30, 2026) were not yet out, so the latest official data is **Q2 2026** (quarter ended June 30, 2026).

Primary sources used most:
- Q2 2026 shareholder letter (SEC 8-K Ex. 99.1): https://www.sec.gov/Archives/edgar/data/0001315098/000162828026051059/ex991-robloxq22026earnin.htm
- Q2 2026 supplemental slides: https://s27.q4cdn.com/984876518/files/doc_financials/2026/q2/Roblox-Q2-2026-Supplemental-Materials.pdf
- Q1 2026 letter: https://www.sec.gov/Archives/edgar/data/0001315098/000162828026028882/ex991-q12026earningsshar.htm
- Q3 2025 letter: https://www.sec.gov/Archives/edgar/data/1315098/000131509825000326/ex991-q32025shareholderl.htm
- FY2025 10-K: https://www.sec.gov/Archives/edgar/data/1315098/000131509826000024/rblx-20251231.htm
- Discovery docs: https://create.roblox.com/docs/discovery
- RFY 28-day algorithm DevForum post (2026-06-15): https://devforum.roblox.com/t/recommended-for-you-algorithm-improvements-that-better-value-long-term-retention/4684575

---

## 0. Macro context a designer must know (2025 boom, then 2026 reset)

| Quarter | DAU (M) | Hours (B) | Bookings | YoY bookings | Monthly unique payers (M) |
|---|---|---|---|---|---|
| Q2 2025 | 112 | — | ~$1.44B | — | 23.4 |
| Q3 2025 (peak) | 151.5 | 39.6 | $1.92B | +70% | 35.8 |
| Q4 2025 | 144 | ~35 | ~$2.2B | +63% | 36.7 |
| Q1 2026 | 132 | 31 | $1.73B | +43% | 30.7 |
| Q2 2026 | 123 | 29 | $1.557B | +8% | 27.0 |
| Q3 2026 guide | "sequential DAU increase" | — | $1.576–1.653B | **−14% to −18%** | — |

Sources: DAU and MUP charts from the Q2 2026 supplemental (slides 7 and 16); Q3 2025, Q1 2026, and Q2 2026 letters (above); Q4 2025 figures from the earnings call transcript https://www.marketbeat.com/earnings/reports/2026-2-5-roblox-corp-stock/ and https://www.fool.com/earnings/call-transcripts/2026/02/05/roblox-rblx-q4-2025-earnings-call-transcript/

Why it matters:
- **The 2025 surge came from viral hits.** Grow a Garden, Steal a Brainrot, and 99 Nights drove it (Q3 2025 letter).
- **2026 is a correction.** Roblox gives three causes:
  1. Mandatory age checks for chat (global since January 2026)
  2. The Russia ban (December 2025)
  3. A **deliberate algorithm change toward 28-day retention**, which "intentionally provides more impressions for highly retentive games at the expense of near term monetization", especially among younger users in the US and Canada (Q2 2026 letter).
- **Engagement moved away from the 2025 viral games.** It shifted from high-monetizing 2025 viral games toward new and evergreen titles. Recent Q2 2026 hits: *Animal Hospital*, *Grow a Garden 2*, *Kick a Lucky Block*.
- **Concentration is falling.** The **top 10 games hold ~20% of hours, down from 30% three years earlier**. Content outside the top 10 grew +25% in hours and +20% in Robux spend YoY (Q2 2026 letter). In Q1 2026, games outside the top 10 produced 65% of Robux-spend growth (Q1 2026 letter).

**Design implication:** the 2026 algorithm rewards D2–D28 return behaviour, not hype spikes. A viral spike that doesn't retain will be throttled.

---

## 1. Audience

### 1a. Age split (age-checked data, global, last 7 days of quarter)

| Cohort | Q1 2026 | Q2 2026 |
|---|---|---|
| Under 13 | 36% | **35%** |
| 13–17 | 38% | **38%** |
| 18+ | 26% | **27%** |

Sources: Q1 2026 letter; Q2 2026 letter.

- **The adult cohort is the fastest-growing:**
  - US 18+ is about **one-third** of age-checked US DAU.
  - US 18+ DAU grew +32% YoY and hours +27% (Q2 2026).
  - US 18–34 DAU grew +42% (Q2 2026) and >50% (Q1 2026).
- **Caveats on the age data:**
  - Only 57% of global DAU were age-checked in Q2 2026 (US and Australia >70%; target 90%).
  - The numbers are not comparable with older self-reported data. Roblox reported no age data for Q4 2025 (10-K).
- **Older self-reported trend:** Q3 2025 13+ DAU grew +89% YoY vs +44% for under-13 (GamesBeat: https://gamesbeat.com/?p=309290).
- **Grow a Garden:** its developer said ~35% of its players are under 13 (Wikipedia, citing interview: https://en.wikipedia.org/wiki/Grow_a_Garden). [UNVERIFIED primary]

### 1b. Device split

The latest official split covers **FY2024** (Roblox annual report via PocketGamer.biz, https://www.pocketgamer.biz/80-of-roblox-users-are-on-mobile-contributing-46-of-robux-revenue/):

| Platform | Share of DAU |
|---|---|
| Mobile | **80%** |
| PC | 17% |
| Console | 3% |

- **Mobile stores are under half of Robux revenue.** The App Store (30%) and Google Play (16%) together produce **46%**, so mobile monetizes below its DAU share.
- **The FY2025 10-K text gives no device percentages.** It says only "mobile, desktop, and console". The 10-K does note that Xbox was <2% of DAU before Q4 2023 (Q4 2025 supplemental).
- **GameAnalytics sample, 2025 (players, top games with >1M MAU):** https://www.gameanalytics.com/reports/2025-roblox-report
  - PC + mobile: 48.4%
  - PC only: 37.6%
  - Mobile only: 7–10%
  - Console only: ~2%
  - This is biased toward PC-heavy top titles. It shows that many players use multiple devices.
- **VR (Meta Quest):** no official share found. [UNVERIFIED / not disclosed]
- **Console share of PlayStation playtime:** ~3% (Newzoo via https://gamedevreports.substack.com/p/newzoo-roblox-as-a-platform-in-2025). [secondary]

### 1c. Session length and engagement

- **Hours per DAU per day:**
  - FY2025: **2.7 hours**. The 10-K reports 123.9B hours and 127M average DAU, and says users explored **>24 experiences/month**.
  - Q2 2026: 29B hours / (123M × 91 days) ≈ **2.6 h/DAU/day** (my calculation).
  - "Hours engaged" includes non-active time (10-K definition).
- **Per-session (GameAnalytics 2025, platform-level player distribution):**

  | Metric | P25 | P50 (median) | P75 | P90 | P95 |
  |---|---|---|---|---|---|
  | Session length (min) | 2.4 | **6.6** | 14.5 | 26.4 | 37.1 |
  | Sessions per day | 1.4 | **2.0** | 3.5 | 6 | 8 |
  | Daily playtime per player per game (min) | 6.6 | **16.8** | 34.6 | 64.9 | 93.8 |

  Source: https://www.gameanalytics.com/reports/2025-roblox-report
- **Discovery caps playtime credit at 60 minutes per user, per game, per day** (https://create.roblox.com/docs/discovery). Playtime past an hour earns no extra ranking credit.

### 1d. Regional split (DAU, millions)

Source: Q2 2026 supplemental, slide 7.

| Region | Q3 2025 (peak) | Q2 2026 | Q2 2026 YoY |
|---|---|---|---|
| US & Canada | 26 | **22** (18%) | +6% |
| Europe | 34 | **26** (21%) | +1% |
| APAC | 46 | **41** (33%) | +15% |
| Rest of world | 45 | **34** (28%) | +15% |
| **Total** | 152 | **123** | +10% |

- **Fastest growth:** Japan DAU +67%, India +64% (Q2 2026 letter).
- **Revenue by billing region, FY2025** (10-K):

  | Region | Revenue | Share |
  |---|---|---|
  | US & Canada | $2.97B | **61%** |
  | Europe | — | 19% |
  | APAC | — | 11% |
  | Rest of world | — | 9% |

  The US alone was 57%.
- **Average bookings per DAU (ABPDAU), Q2 2026, per quarter** (supplemental slide 15):

  | Region | ABPDAU per quarter |
  |---|---|
  | US & Canada | **$38.63** |
  | Europe | $13.35 |
  | APAC | $4.90 |
  | Rest of world | $4.88 |

  A US/Canada DAU is worth about 8x an APAC DAU.

---

## 2. Discovery algorithm

### 2a. Official ranking signals (current, post-June 15, 2026)

Source: https://create.roblox.com/docs/discovery and the DevForum post above.

**How the system works:**
- **Two stages.** Retrieval picks candidate games, then ranking personalizes the order.
- **Organic users only.** Signals use only users who **organically joined from the Recommended For You sort on Home**. Engagement, monetization, and retention of users from ads or other sources are not counted.
- **Per-user averages, not totals.** A small, highly engaged game is not penalized for its size.
- **"Explore and expand."** Roblox tests the game on new user cohorts and expands to similar cohorts if engagement and monetization are good.

**Signals, by stated priority:**

| Priority | Signal | Detail |
|---|---|---|
| Most important | **Play-through rate (PTR)** | Plays after seeing the game in Recommended for You. It replaced "QPTR" (qualified play-through rate) in June 2026. |
| Most important | **First-play bounce rate** (negative) | Measured in two buckets: <60 s and 61–180 s |
| Most important | **Play days per user** | Day 1, Days 2–7, Days 8–28 |
| Most important | **Playtime per user** | Capped at 60 min/user/game/day |
| Important | **Intentional co-play days per user** | Joins, invites, private servers |
| Important | Qualified play sessions per user | — |
| Important | **Spend days per user** | — |
| Important | **Robux spent per user** | — |

- **Monetization counts, but below retention and engagement.** Spend days and Robux spent are "Important", not "Most important".
- **The June 2026 change** (newsroom: https://about.roblox.com/newsroom/2026/06/optimizing-discovery-great-games-reach-millions-players-roblox):
  - The window grew from **7 days to 28 days**.
  - The rationale: short-term proxies "could favor games with exciting thumbnails that win attention but lack long-term value."
  - The change was tested from April and rolled out June 15, 2026.
  - Exact weights appear only as an image in the DevForum post, so I could not extract them. [weights UNVERIFIED]
- **Earlier version:** the 2025 RFY algorithm ranked on QPTR, weekly playtime, and intentional co-play. It was activated in March 2025, per Tubefilter (https://www.tubefilter.com/2025/03/20/roblox-discovery-roadmap-2025/) and Dubit (https://dubit.io/blog/roblox-top-20-rfy). [secondary]
- **Benchmarks:** similar-game benchmarks need **100+ DAU**, update daily, and "do not impact the recommendation algorithm in any way" (DevForum; analytics docs https://create.roblox.com/docs/production/analytics).

### 2b. Exposure penalties and eligibility (official, discovery docs)

- **A custom thumbnail is required** for Home recommendation impressions. A game with only the default thumbnail is ineligible.
- **Money in the metadata.** "Metadata that implies any type of monetary reward is not prioritized" (for example, giveaway titles). Also: "You should not rely on promotional monetary rewards to drive engagement."
- **Clones.** Games whose metadata and place files "closely resemble existing games" are "no longer prioritized" and rank lower in search.
- **Mismatches.** Metadata or thumbnails that don't match the gameplay are not recommended and rank lower in search.
- **Quality reclassification.** Roblox "continually reclassifies content quality with every update", and a reduced-exposure banner appears in the Creator Dashboard (refreshed daily).
- **Impression drivers.** Impressions depend on your gameplay and updates, Roblox's algorithm changes, Home traffic seasonality (weekly, summer and back-to-school, holidays), and competitors' performance.

### 2c. Thumbnails and icons (official)

Source: https://create.roblox.com/docs/production/publishing/thumbnails

- **Thumbnail personalization (built-in A/B testing):**
  - Activate 2–5 thumbnails. Roblox serves each to random user groups, then routes impressions to the winner **per user segment**, keeping minimal traffic on the others.
  - The test metric is (Q)PTR. Result: **average +8.5% QPTR; some games about +50%.**
- **Specs:**
  - 16:9, ideally 1920×1080, <3 MB.
  - Up to 10 images or videos per detail page.
  - Video uploads: 3 per month. Videos must show real gameplay: no fake features, no enhanced graphics, no voice-over, no ads or claims.
- **Recommendations:** keep multiple thumbnails active, and test new thumbnails with every major update.
- **Winner memory (2025):** new tests now keep traffic on the current winner. Result: +0.19% QPTR and 21% fewer impressions wasted on losing thumbnails (https://devforum.roblox.com/t/thumbnail-personalization-now-remembers-your-existing-winning-thumbnails/3793665).
- **PTR next:** Roblox "will be testing updating thumbnail personalization to use PTR too" (June 2026 DevForum).
- **Icon A/B testing:** no official icon A/B test found. [UNVERIFIED / not documented]

### 2d. Sorts and surfaces

| Surface | What it is |
|---|---|
| Recommended For You (Home) | The main algorithmic surface (above) |
| Continue Playing, Friends | Other Home sections |
| Sponsored | Paid placement via Ads Manager. **45,000+ games used Ads Manager in 2025 (to Aug 5), +70% YoY** (RDC 2025: https://about.roblox.com/newsroom/2025/09/roblox-rdc-2025). Ads-acquired users don't count toward RFY signals. |
| Curated / "Standout Games" | Hand-picked for unique mechanics, distinctive visuals, or underrepresented genres |
| **Top Trending** (Charts) | Official definition: "games that players have been spending more time in over the past two weeks" (https://www.roblox.com/charts/top-trending). Genre "Trending in X" charts use the same definition. |
| **Up-and-Coming** (Charts) | **No official definition found** [UNVERIFIED]. A DevForum complaint says it shows games with 10K–200K+ CCU. |
| Top Playing Now (Charts) | Launched 2025 (https://devforum.roblox.com/t/introducing-top-playing-now-on-charts/3529809). Formula not published. |
| **Trending Events in Experiences** (Charts) | Ranks active events by the game's DAU. To qualify, the event must have **started within the last 7 days, have 1,000+ RSVPs, and be public** (https://create.roblox.com/docs/production/promotion/experience-events). |
| Search | Semantic search in all supported languages |
| Roblox Moments | Beta since September 2025 (13+). Short gameplay clips (≤30 s) with tap-to-join (https://about.roblox.com/newsroom/2025/09/roblox-moments-user-generated-discovery). No join metrics published. |

### 2e. Updates, "update logs", and notifications

- **Updates move the signals.** Changes to gameplay "influence recommendation signals", and quality is re-assessed on every update (discovery docs).
- **No "updated recently" ranking boost is documented.** [no evidence either way]
- **Official update cadence** (retention docs: https://create.roblox.com/docs/production/analytics/retention):
  - **Smaller updates to existing mechanics every 2–4 weeks**
  - **Larger feature updates every 2–3 months**
  - FTUE: get users "to the fun in 5 minutes or less"
- **Update announcements to followers:**
  - Limited to **60 characters**, **once every 3 days**.
  - Analytics report views, visit rate, and unfollow rate (experience-events docs).
- **Events:**
  - Up to 10 live or upcoming at once.
  - Players click "Notify Me" to get a notification when the event starts.
  - Off-platform featuring requires submission ≥7 days ahead.
  - A "Live Events" Home section exists (discovery docs).
- **Experience Notifications** (https://create.roblox.com/docs/production/promotion/experience-notifications):
  - **Only for opted-in users aged 13+.** Under-13 users get only update notifications.
  - **One per user per experience per day**, plus an undisclosed cross-experience cap.
  - The game needs 100+ visits.
  - The opt-in prompt can't be re-shown within 30 days.
  - Banned: false time pressure, bait-and-switch, and gating gameplay on opt-in.

---

## 3. Retention benchmarks

- **Roblox's own position.** Roblox publishes no numeric "good D1" figure. It tells creators to bring D1 and session time "comparable to or above" the similar-game benchmarks in Creator Analytics (100+ DAU needed) before scaling user acquisition. Since October 2025, creators can view D1, D7, and D30 retention **by acquisition source** (https://devforum.roblox.com/t/analytics-view-retention-by-acquisition-source-and-select-your-benchmark-set/4010157).
- **Definitions:**
  - D1 = returned the next day.
  - D7 = returned on day 8 (exactly day 7, not rolling).
  - D30 = returned on day 31.
  - Source: https://create.roblox.com/docs/production/analytics/retention
- **GameAnalytics 2025 game-level benchmarks, by average session length** (https://www.gameanalytics.com/reports/2025-roblox-report; per-percentile tables also at https://investgame.net/news/pdf/the-2025-roblox-benchmark-report/):

| Avg session | D1 median | D1 P90 | D1 P98 | D7 median | D7 P90 | D7 P98 | D30 median | D30 P98 |
|---|---|---|---|---|---|---|---|---|
| 0–3 min | 4.3% | 9.3% | 12.3% | 0.41% | 1.8% | 3.2% | 0.13% | 0.81% |
| 7–12 min | 7.9% | 11.6% | 15.8% | 0.90% | 2.0% | 3.6% | 0.24% | 1.49% |
| 13–18 min | 10.2% | 15.0% | 20.9% | 1.2% | 2.7% | 4.6% | 0.34% | 1.94% |
| 19–24 min | 11.5% | 18.2% | **32.3%** | 1.6% | 5.2% | **8.5%** | 0.46% | **2.99%** |
| 25+ min | 10.8% | 18.9% | 25.4% | 1.8% | 5.9% | 7.0% | 0.50% | 2.87% |

- **Caveat on the GameAnalytics figures.** They count every new user, including one-click bouncers and cross-promo traffic, so they sit far below "forum rule-of-thumb" numbers. Use them as a **relative** ladder. The clear finding: **longer sessions go with roughly 2.5x the D1 and 4x the D7.**
- **Community rules of thumb** [UNVERIFIED, not Roblox data]:
  - "Aim for 20–25% D1"
  - Obby: D1 25–35%, D7 10–15%
  - Source: https://rowatcher.com/news/retention-benchmarks-by-roblox-genre-what-good-actually-looks-like
- **What top games hit:** no published D1/D7 for Grow a Garden, Steal a Brainrot, or 99 Nights. [Not disclosed.] Indirect evidence:
  - Grow a Garden held ~1M+ CCU baseline months after launch, against 21–22M event peaks (Tubefilter, below).
  - 99 Nights stayed "#3 by DAU" after two weeks with no updates (PC Gamer via https://www.inkl.com/news/with-a-peak-player-count-of-14-2-million-99-nights-in-the-forest-has-an-audience-other-multiplayer-games-would-kill-for-to-find-these-behemoth-playerbases-you-need-to-be-on-a-platform-like-roblox).

---

## 4. Monetization benchmarks

### 4a. Platform-level (official)

- **ABPDAU, Q2 2026:** **$12.66 per DAU per quarter**, about **$0.14 per DAU per day** in gross bookings (supplemental slide 14; per-day figure is my calculation).
  - Q4 is the seasonal high: $15.38 in Q4 2025 and $15.97 in Q4 2024.
- **Payers:**
  - FY2025: about **1.8M daily unique payers out of 127M DAU, roughly 1.4% daily payer rate** (10-K).
  - Roblox told the University of Sydney/press that **1.4%** of 132M Q1 2026 DAU were payers (https://ia.acs.org.au/article/2026/roblox-sucking-up-money-from-young-players--study.html).
  - Monthly unique payers: 27.0M in Q2 2026, about 22% of average DAU.
  - **Average bookings per monthly unique payer: $19.25/month** (Q2 2026, slide 16).
- **Durable vs consumable** (FY2025, share of virtual-item revenue, 10-K):

  | Type | FY2023 | FY2024 | FY2025 |
  |---|---|---|---|
  | Durable | 91% | 91% | 85% |
  | Consumable | 9% | 9% | **15%** |

  Consumables are the fastest-growing share. The viral 2025 games were consumable-heavy: seeds, eggs, luck boosts.
- **Paying users:** they spend purchased Robux within about **3 days** on average. The estimated paying-user lifetime is **27 months** (Q4 2025 supplemental).

### 4b. Game-level (GameAnalytics 2025, top games)

- **Daily average revenue per paying user (ARPPU), across all players:** P50 **$0.72**, P75 $3.00, P90 $9.91, P95 $20.65.
- **Median ARPPU by average session length:**

  | Avg session | Median ARPPU |
  |---|---|
  | 0–3 min | $0.48 |
  | 7–12 min | $0.77 |
  | 13–18 min | $1.21 |
  | 19–24 min | $1.71 |
  | 25+ min | **$2.12** |

- **Median average transaction value:** **$0.51–$1.29**, which is about 50–130 Robux at roughly $0.01/Robux.
- **The 19–24 min bucket at P95:** $8.49 average transaction and $27 ARPPU.
- Source: https://www.gameanalytics.com/reports/2025-roblox-report
- **Best-selling price points:** no official Roblox list exists [UNVERIFIED]. The GameAnalytics transaction medians suggest the bulk of purchases are **under 150 Robux**.
- **Price tools (official):**
  - **Price Optimization:** median **+4% earnings** for creators who ran a test. Eligibility: ≥60K transactions per month. Tests often recommend *lowering* prices.
  - **Regional Pricing:** in early tests, the share of users spending rose **+17% in Mexico, +26% in Brazil, +52% in the Philippines**.
  - Source: https://about.roblox.com/newsroom/2025/04/roblox-launches-regional-pricing-for-in-experience-items
- **Game pass vs developer product split:** not disclosed by Roblox. One third-party estimate: passes about 55%, developer products about 30% [UNVERIFIED: https://rolearn.dev/trend-reports/creator-economy-2025-report].

### 4c. Revenue shares and product rules (official)

Sources: https://create.roblox.com/docs/get-started/monetization and https://create.roblox.com/docs/production/monetization/subscriptions

- **Game passes and developer products:** creator keeps **70%** of Robux; Roblox's marketplace fee is 30%.
- **Experience subscriptions:**
  - Local-currency tiers: **$2.99, $4.99, $7.99, $9.99, $14.99**. Robux subscriptions can be priced from ≥49 Robux.
  - Local currency pays **70% in month 1 and 100% from month 2**. Robux subscriptions pay 70% every month.
  - Limits: up to 50 subscriptions per game, no mutually exclusive tiers, local-currency prices can't be changed, and benefits can't be revoked.
- **Creator Rewards** (launched July 2025; replaced engagement-based payouts):
  - **5 Robux** per "Active Spender" (spent ≥$9.99 in the last 60 days) who plays ≥10 min, for the first 3 games they play that day.
  - **35% share** of the first $100 of Robux purchases by new or returning users acquired via direct link or search.
- **UGC avatar items:** creator 30%, seller 40%, Roblox 30%. Sold inside your own game, you take **70%**.
- **Immersive ads:** paid on views, impressions, and teleports. Rates not published.
- **Rewarded video ads:**
  - Launched in partnership with Google, April 2025 (videos up to 30 s).
  - **Shown only to users 13+** (https://create.roblox.com/docs/production/promotion/ad-integrations).
  - API: `AdService:ShowRewardedVideoAdAsync`, which grants a developer product through ProcessReceipt (https://create.roblox.com/docs/reference/engine/classes/AdService).
  - Per-view payout not published. A third-party estimate of $3–15 per 1K DAU per month [UNVERIFIED].
  - Roblox calls it a "strong product-market fit". A Studio plugin and pre-gameplay placement are due Q4 2026 (Q1 2026 letter; RDC 2026 via https://www.mediapost.com/publications/article/417959/).
- **Roblox Plus** (launched April 30, 2026, $4.99/month; replaces Premium for new sign-ups):
  - Roblox funds item discounts, so creators get the same Robux per item.
  - Creators are paid for Plus subscribers' time in paid private servers.
  - Sources: https://www.nasdaq.com/press-release/roblox-announces-roblox-plus-new-subscription-plan-offering-exclusive-platform and the Q1 2026 letter.
- **Brand integrations / independent ads:**
  - Must be registered in Ads Manager ≥5 days ahead and labelled. Rewarded video is 13+ only.
  - From **January 1, 2027** Roblox takes a revenue share. Rates per 1,000 qualified visits: **US $1.50, Tier-1 $0.75, Tier-2 $0.20, Tier-3 $0.05** for the first 28 days, then $0.10. Cap: $400K per campaign.
  - Source: https://create.roblox.com/docs/en-us/production/promotion/ad-integrations

### 4d. DevEx (cash-out) and creator payouts

| Item | Figure | Source |
|---|---|---|
| Standard DevEx rate | **$0.0038 per earned Robux** since Sept 5, 2025 (+8.5% from $0.0035). Minimum cash-out 30,000 Robux. | Q3 2025 letter; RDC 2025 |
| Effective creator take of $1 spent | 70% × $0.0038 × 100 Robux = **26.6%** | Q1 2026 letter |
| **Age-checked 18+ US spenders** (from June 8, 2026) | Effective creator take rises to **37.8%** of spend. The game must use the R15 avatar. | Q1 2026 letter |
| DevEx fees Q2 2026 | $363M (23% of bookings) | Q2 2026 letter |
| DevEx fees Q4 2025 | $477M | Q4 2025 call |
| DevEx fees Q3 2025 | $427.9M | Q3 2025 letter |
| FY2025 creator earnings | **>$1.5B**; top 1,000 creators averaged **$1.3M** (+50%) | Q4 2025 call: https://transcripts.platformaeronaut.com/transcripts/RBLX-4Q25-transcript |
| Roblox Wallet | Earn directly in USD (announced RDC 2026, Sept 10–12) | https://pokde.net/gaming/game-industry/roblox-developers-conference-2026 |

**Design implication:** an age-checked US adult's spend is now worth about 42% more to the creator (37.8 vs 26.6), and US/Canada ABPDAU is about 8x APAC. Content that appeals to 18+ (and uses R15) pays better per player.

---

## 5. Viral mechanics evidence

### 5a. CCU records (dated)

| Date | Game / event | Peak CCU | Source |
|---|---|---|---|
| May 18, 2025 | Grow a Garden | ~5M (then a Roblox record) | Wikipedia GaG |
| June 14, 2025 | Grow a Garden | 16M+ | Wikipedia GaG |
| **June 21, 2025** | Grow a Garden (Saturday update / event) | **21.3–21.6M** (Roblox-confirmed 21.6M "late June") | Fortune: https://fortune.com/2025/07/30/roblox-video-game-grow-a-garden-viral-summer-hit/ ; Calcalist: https://www.calcalistech.com/ctechnews/article/dj4lxef8r |
| July 2025 | Grow a Garden | "nearly 22M" | Q3 2025 letter |
| **Aug 23, 2025** | **"Admin War"**: GaG vs Steal a Brainrot (simultaneous Admin Abuse events) | GaG 21.1–22.3M; SaB ~20M; **platform 47.3–47.4M** (Roblox letter: ">45M") | Tubefilter: https://www.tubefilter.com/2025/08/25/roblox-grow-garden-steal-brainrot-admin-war-record/amp/ ; Q3 2025 letter |
| Sept 13, 2025 | Steal a Brainrot "Extinct Event" | ~24M | https://en.wikipedia.org/wiki/Steal_a_Brainrot |
| **Oct 7, 2025** | Steal a Brainrot | **25.4M** (all-time single-game record) | https://www.pocketgamer.biz/robloxs-steal-a-brainrot-becomes-first-game-to-surpass-25m-concurrent-players |
| 2025 | 99 Nights in the Forest | 14.2M | PC Gamer / TheWrap: https://www.thewrap.com/creative-content/movies/20th-century-studios-roblox-game-99-nights-in-the-forest/ |
| January 2026 | Steal a Brainrot × Bruno Mars concert | 12.8M | Wikipedia SaB |

**Event spike vs baseline.** Both GaG and SaB averaged **~1M CCU** on normal days around the August 2025 admin war, then spiked **~20x** during weekend admin events (Tubefilter). Admin Abuse means developers spawn limited items and weather for players online during a set window. It is pure FOMO plus a scheduled time, so it concentrates DAU into one hour. Before the August 23 war, each game's events had already reached ~15M.

### 5b. Mechanics with evidence

- **Short global restock timers (Grow a Garden):**
  - The seed shop restocks **every 5 minutes**, and stock is **global**: every player sees the same items.
  - A YouTuber (5.3M subscribers) quoted in Fortune: "there's always something pulling you back."
  - The egg shop restocks about every 30 minutes [secondary: https://allthings.how/grow-a-garden-2-stock-predictor-how-restock-timing-works/].
  - Plants grow while offline, and weekly limited items must be claimed while online (Wikipedia GaG).
- **Weekly Saturday update cadence (GaG):** updates went live on Saturdays, and the record CCU days (June 21, Aug 23) fell on Saturdays. No primary statement of the fixed day was found. [cadence UNVERIFIED]
- **Monetization (GaG):** Robux to skip waits, buy perks, buy pet eggs (loot boxes), and steal crops. **~$12M gross Robux spend in May 2025 alone** [UNVERIFIED: Calcalist, unattributed]. Ownership: BMWLux (the original 16-year-old dev) ~50%, Splitting Point (Jandel/Janzen Madsen) bought in April 2025 at ~1,000 CCU, DoBig minority (Wikipedia).
- **Stealing and raiding (Steal a Brainrot):**
  - Buy characters off a shared conveyor belt, or steal them from other players' bases.
  - Characters produce passive income.
  - A temporary base-lock shield, traps and items (some Robux-only), and rebirth resets.
  - Polygon: "the best items are only available for cash" (Wikipedia SaB).
  - Viral loop: clips of kids losing Brainrots got "tens of millions of views" on TikTok and YouTube [UNVERIFIED aggregate].
  - The developers have filed ≥4 lawsuits against clones since November 2025 (Bloomberg, March 24, 2026: https://www.bloomberg.com/news/articles/2026-03-24/roblox-s-hit-game-steal-a-brainrot-battles-its-many-imitators).
  - Note: Roblox now deprioritizes close clones (discovery docs).
- **Trading:**
  - Off-platform real-money trading of GaG pets (e.g., a polar bear pet sold for >$200) is against Roblox rules (Calcalist; Community Standards).
  - In-game trading must respect `IsPaidItemTradingAllowed` per user (see Section 6).
- **Co-op (99 Nights):** a 2–5-player survival game. Intentional co-play days are an "Important" ranking signal.
- **Friend-invite rewards (official system, April 23, 2025):**
  - The invite modal shows a creator-defined reward banner.
  - Read `ReferredByPlayerId` from `GetJoinData()` and reward both inviter and invitee.
  - Invite links never expire and work for non-friends.
  - Source: https://create.roblox.com/docs/production/promotion/referral-system
  - Note: friend-driven joins don't feed RFY signals, but co-play days do.
- **Group join rewards:** `GroupService:PromptJoinAsync()` offers an in-game group-join prompt (https://create.roblox.com/docs/reference/engine/classes/GroupService). No data on effect size.
- **Short-form video:**
  - Roblox Moments: 240M video captures and 930M screenshots were made between July and September 2025 (https://techcrunch.com/2025/09/05/roblox-announces-short-form-video-feed-for-gameplay-clips-new-ai-tools-for-creators-and-more).
  - No platform data ties TikTok or Shorts views to CCU. [UNVERIFIED causal link]
  - An Aftermath podcast host attributed GaG's spread to short clips of dramatic moments such as stolen crops (https://aftermath.site/podcasts/aftermath-hours-podcast-roblox-grow-a-garden-geoguessr/). [opinion]
- **Bot-inflation allegation:** TD Cowen alleged bots inflated GaG's numbers, then retracted the claim. Roblox said the popularity was genuine (Wikipedia GaG).
- **Durability caveat (2026):**
  - The 2025 viral cohort monetized well per hour, but engagement moved away from it in 2026 (Q2 2026 letter).
  - Brainrot-genre CCU fell sharply. One tracker cites SaB at ~215K CCU later [UNVERIFIED: https://rowatcher.com/news/is-the-brainrot-trend-dying-what-ccu-data-from-three-top-games-reveals].
  - The 28-day algorithm is designed to stop rewarding spike-only games.

---

## 6. Policy constraints (2025–2026)

- **Paid random items** (https://create.roblox.com/docs/production/monetization/paid-random-items; updated 2026-10-23):
  - **Scope:** any random outcome bought directly or indirectly with Robux, including Robux-bought soft currency. Covers eggs, wheels, chests, enhancement potions, synthesis, and **luck boosts and pity systems**.
  - **Odds display:** show every outcome with numerical % odds summing to 100%, before purchase. An "Info/Details" pop-up is allowed; a bare (i) icon is not. Odds must update when an item can only be won once. Luck boosts must show numerical effects live.
  - **Per-user policy check:** call `PolicyService:GetPolicyInfoForPlayerAsync()`.
  - If `ArePaidRandomItemsRestricted` is true, you must offer a free path, a fixed order, direct purchase, or hide or block the item.
  - If `IsPaidItemTradingAllowed` is false, you must block trading of paid items.
  - Free, earnable random rewards need no odds disclosure.
- **Gambling.** "we prohibit both simulated and actual gambling activities on the platform. No real money, Robux, or in-game items of value may be exchanged in connection with any gambling activities." Creators also may not run contests or games of chance (https://about.roblox.com/community-standards).
  - Pressure is rising: a University of Sydney study (March 2026) of 15 top earners found 14 misleading practices, including fake daily discounts and opaque random rewards (https://www.sydney.edu.au/news-opinion/news/2026/05/17/inside-the-pay-to-play-world-of-roblox-targeting-children-.html).
  - US groups asked the FTC to investigate in May 2026 (https://www.newstribune.com/news/2026/may/22/child-safety-groups-want-ftc-to-investigate-roblox/).
- **Crypto, NFTs, real money:**
  - The Community Standards don't name crypto or NFTs.
  - They prohibit using third-party services to buy, sell, or trade Robux; off-platform secondary-market sales of virtual items; selling on-platform items via off-platform services; directing users off-platform; and "deceptive, sensational… misleading content or metadata".
  - The 2023 Advertising Standards **ban crypto and NFT ads** (https://www.dglaw.com/faced-with-increasing-pressure-roblox-adopts-new-advertising-standards/).
  - Financial services are a "highly regulated" category. No authoritative financial claims are allowed.
  - **Implication for a Bitcoin-themed game:** use fictional in-game currency only. No real-coin pricing, no "earn crypto" claims, no investment framing, and no off-platform redemption. [Interpretation; no explicit "crypto theme ban" text was found.]
- **Pay-to-win and misleading monetization:**
  - No explicit pay-to-win ban.
  - Rules that do apply: discovery deprioritizes metadata implying monetary rewards; notifications may not use "false time pressure" or "bait-and-switch rewards"; subscription benefits can't be revoked; thumbnails and videos can't misrepresent gameplay.
- **Maturity labels and ratings:**
  - Labels: Minimal, Mild, Moderate, Restricted (18+).
  - **From Sept 30, 2025, unrated experiences were made unplayable** until the creator completes the Maturity & Compliance questionnaire (https://techloy.com/roblox-removes-unrated-games-over-child-safety-concerns). "Millions of unrated experiences" were removed from access (Q3 2025 letter).
  - IARC ratings are being adopted.
- **Age checks and chat:**
  - Facial age estimation (or ID or parental consent) sorts users into **<9, 9–12, 13–15, 16–17, 18–20, 21+** (https://corp.roblox.com/age-estimation).
  - Enforcement started in Australia, New Zealand, and the Netherlands in December 2025, and went **global in January 2026** for text and voice chat (Q1 2026 letter).
  - Chat runs only within similar age groups or Trusted Connections.
  - 57% of DAU were age-checked by Q2 2026.
  - On-platform communication is still "below pre-age-check levels" (Q2 2026 letter).
- **Kids and Select accounts** (from June 2026) (https://create.roblox.com/docs/production/publishing/kids-and-select; https://about.roblox.com/newsroom/2026/04/introducing-roblox-kids-and-select-accounts):
  - **Roblox Kids (5–8):** only Minimal or Mild games; chat off.
  - **Roblox Select (9–15):** up to Moderate.
  - Both exclude social hangouts, free-form drawing, and sensitive-issue games by default.
  - **To reach users under 16, a creator needs** an age-checked and ID-verified account, 2-Step Verification, and either a refundable per-game fee or 2+ months of Plus/Premium.
  - **Evaluation:** the game first launches to age-checked 16+ users only and must reach **250 unique plays from highly engaged, age-checked players within 60 days**, plus a safety review. An expedited review costs **50,000 Robux** (refundable).
  - About **30,000 games** were available to younger users at launch (Q2 2026 letter).
  - **Implication:** a new game can't reach under-16s on day one. Plan the launch audience as 16+ first.
- **Ads policy** (https://create.roblox.com/docs/en-us/production/promotion/ad-integrations):
  - Ad rules cover paid promotions, off-platform calls to action, and self-promoting merchandise.
  - Ads must be registered in Ads Manager and use the standard labels, with larger labels for audiences aged ≤12.
  - Rewarded video is 13+ only.
  - Misleading tactics ("free Robux") are banned.
  - Brands must hide ads from under-13 users via PolicyService (2023 standards).
  - Updated ad policies took effect around May 2026 (Q1 2026 letter).

---

## 7. Technical reality

- **Mobile is 80% of DAU**, and low-end Android is the binding constraint.
  - Roblox's stated goal is 100-player games "on low-end **2GB** Android devices".
  - The Harmony memory system cut **out-of-memory crashes on low-end Android by 21%**, and occlusion culling cut render time on the slowest devices by **35%**.
  - Source: RDC24 recap, https://devforum.roblox.com/t/rdc24-what-we-announced/3148833
  - A secondary source reports a 64% overall crash reduction [UNVERIFIED: https://progameguides.com/roblox/roblox-aiming-for-100-player-games-with-good-performance].
- **Frame budget:** 16.67 ms at 60 FPS.
- **Baseline-device rendering guidance:** "below **1,000 draw calls and 1,000,000 triangles**" (https://create.roblox.com/docs/performance-optimization/design).
- **Textures** (https://create.roblox.com/docs/performance-optimization/improve):
  - Memory scales with pixel count: a 1024² texture uses 4x the memory of a 512².
  - Most images should be ≤512², and minor images <256².
  - Watch LuaHeap and InstanceCount.
  - Shadows turn off below graphics quality level 4.
  - Physics steps adaptively at 60/120/240 Hz.
- **Part and instance budget:** Roblox publishes no official part budget [UNVERIFIED community numbers only]. The SLIM demo scene shows what a heavy scene looks like: **159,745 → 92,536 client instances, 20M → 3.35M triangles, 2,402 → 1,454 draw calls** with streaming plus SLIM (https://about.roblox.com/newsroom/2025/12/introducing-roblox-slim-scalable-lightweight-interactive-models).
- **StreamingEnabled** (https://create.roblox.com/docs/workspace/streaming):
  - **On by default for new places.**
  - Defaults: `StreamingMinRadius` = 64 studs, `StreamingTargetRadius` = 1024.
  - `StreamOutBehavior` defaults to LowMemory. Setting it to **Opportunistic** is recommended to reduce out-of-memory crashes.
  - Use `ModelStreamingMode` Atomic or Persistent sparingly, and `WaitForChild` on the client.
  - Content in ReplicatedStorage and ReplicatedFirst is never streamed.
- **Texture streaming (2025–2026):** Harmony sets a per-frame texture budget from free device memory to avoid texture out-of-memory crashes (https://devforum.roblox.com/t/introducing-texture-streaming/4144855). No crash-reduction figure was given.
- **Low-end memory headroom:**
  - Developers report that 1GB devices (for example, Amazon Fire HD) kill the app at around 900MB or less (https://devforum.roblox.com/t/amazon-tablets-crash-rates/1689945).
  - One developer cites about 250MB of headroom on some phones [UNVERIFIED anecdote].
  - No official per-device memory budget is published.
  - Low-end crashes also inflate first-play bounce rate, which is a top-priority ranking signal. Developers raised this in the June 2026 DevForum thread, and Roblox did not answer.
- **Platform roadmap (RDC 2025 and RDC 2026):**
  - Server authority enabled by default for standard characters and physics.
  - Custom matchmaking.
  - A long-term goal of 100K players on one server (RDC 2025).
  - Standalone app publishing on mobile, PC, and console; Chrome in-browser play by the end of 2026; offline and single-player modes in development (RDC 2026, Sept 10–12, 2026: https://gamesbeat.com/roblox-hits-20-and-opens-rdc-2026-to-invite-the-world-to-play-and-make-games-dave-baszucki-keynote/).

---

## 8. Evidence-based design takeaways (derived from the data above)

1. **Retention over spikes.** RFY now scores D1, D2–7, and D8–28 play days, PTR, and bounce rate in under 60 s and 61–180 s. The first 3 minutes and the reason to return on days 2–28 are worth more than launch hype. Target the fun in ≤5 minutes (Roblox docs).
2. **Session length predicts both retention and revenue.** Games averaging 19–24+ minutes per session have roughly 2.5x the D1, 4x the D7, and 3–4x the median ARPPU of games averaging 0–3 minutes (GameAnalytics). Playtime credit caps at 60 min/day, so very long grind sessions add nothing to ranking.
3. **Co-play is a ranking signal.** Build for parties, private servers, and invites, and use the official referral reward banner.
4. **Scheduled shared-time events work.** Restocks every 5 minutes with global stock, plus weekend admin events, produced ~20x CCU spikes in 2025. The 2026 algorithm values them only if the players come back.
5. **Monetize consumables carefully.** Consumable revenue grew from 9% to 15% of the item mix. Any Robux-linked randomness (including luck boosts) needs exact odds and PolicyService gating. Simulated gambling is banned outright.
6. **Adults pay more.** The age-checked US 18+ DevEx uplift (26.6% to 37.8%, R15 required) and US/Canada ABPDAU 8x APAC favour 13+ and 18+-friendly themes. Under-16 reach requires the Kids/Select evaluation (250 engaged plays in 60 days from 16+ players).
7. **Thumbnails:** keep 2–5 active for personalization (+8.5% average QPTR). Never misrepresent gameplay, and never put money or giveaways in the title.
8. **Performance:** treat 2GB Android as the floor. Keep StreamingEnabled with Opportunistic stream-out, stay under 1K draw calls and 1M triangles, and use ≤512² textures.
9. **Crypto or real-money themes:** keep the economy fictional. No off-platform value, no investment claims. Crypto and NFT advertising is banned.
