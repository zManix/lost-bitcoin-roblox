# Proven Loops from Steam/Mobile Hits: Digging, Junk, Cleaning, Treasure, Incremental, Automation, Friendslop

Research date: 2026-10-25. Built for a designer making a new Roblox game.

## Method and data caveats (read first)

- **Release dates, prices, total review counts** come from the Steam store API (`store.steampowered.com/api/appdetails`, field `recommendations.total` = all-language review count) and the store pages. These were pulled on 2026-10-25.
- **Review % for older games** comes from the SteamSpy API positive/negative counts (`steamspy.com/api.php?request=appdetails&appid=<id>`). For games from 2025-26, SteamSpy is stale (it shows "0..20,000" owners for PEAK, Megabonk and others), so for those I used the English review % shown on the Steam store page.
- **Sales** are the developer's or publisher's own figure wherever one exists. Otherwise I cite a named tracker (Alinea, GameDiscoverCo, VG Insights via SteamPulse, Raijin, AppMagic) and label it as an estimate. SteamSpy "owners" ranges are given as context only.
- **Review quotes** come from Steam community "most helpful" review pages (`steamcommunity.com/app/<id>/negativereviews/?browsefilter=toprated&filterLanguage=english` and `/positivereviews/`). A summarizer extracted them, so treat them as close to verbatim, not character-exact. Hours shown = that reviewer's playtime on record.
- **Unverifiable claims are tagged [UNVERIFIED].** My own design inferences are tagged (inference).
- SteamDB and Gamalytic block fetches or need an API key, so neither was used.

---

## Part 1: Game-by-game

Abbreviations: **Rev** = total Steam reviews, all languages. **%** = positive share. **Loop (s/m/S)** = second-to-second / minute-to-minute / session.

### A. Digging and mining

#### 1. A Game About Digging A Hole (AGADAH): Cyberwave / rokaplay
- **Release / price:** Feb 7, 2025, $4.99. Mobile July 31, 2025. Game Pass Dec 2025. Co-op sequel *A Game About Digging A Hole Together* is due Dec 4, 2026 (4-player online, cross-play). [store](https://store.steampowered.com/app/3244220) · [Wikipedia](https://en.wikipedia.org/wiki/A_Game_About_Digging_a_Hole) · [Inven Global, sequel](https://www.invenglobal.com/articles/27425/a-game-about-digging-a-hole-together-launches-december-4th-with-xbox-game-pass)
- **Sales:** 220k in 5 days and more than 250k in week 1, per the publisher. More than 1M by summer 2025, per GamesMarket and the publisher. [GamesMarket](https://www.gamesmarket.global/viral-hit-the-unlikely-smash-hit-of-a-game-about-digging-a-hole-by-cyberwave-und-rokaplay-e8a7fdd83064b0ffc558c65513937b0b) · [1M](https://www.gamesmarket.global/viral-hit-a-game-about-digging-a-hole-tops-one-million-sales-82fed80996941736a1a54c31381ab20b)
- **Reviews:** 19,023 total. English: 90% of 11,512 (Very Positive). Recent: 79%.
- **Dev / marketing:** One developer built it in about 3-4 weeks (Wikipedia says about 14 days) on reused voxel tech and licensed assets. It went from an initial target of 10k wishlists to about 140k. Short-form views: 14.5M on Instagram Reels, 5M on TikTok, 2.2M on YouTube Shorts. IGN reshared it without being asked.
- **Loop:** s = hold the shovel and watch voxels vanish as ore pops out. m = inventory fills, walk up to the barn, sell, buy a shovel/battery/bag upgrade, dig deeper. S = about 2 hours to the ending, then an achievement mode. Moles harass you deeper down, and there is a mystery at the bottom.
- **Hook:** An absurdly simple premise ("it's a game about digging a hole") plus the big red X on the lawn made it easy to clip. Players recognized it as nostalgic Motherload ("the game they'd been waiting for since the flash game Motherload", 1.5h). The hole itself became a meme.
- **Praised:** (1) Relaxing: "very relaxing" (5.6h). (2) Controls: "The controls? Flawless." (82.2h). (3) Deeper than expected: "goes a lot deeper than he thought" (3.0h).
- **Complaints:** (1) Too short: "only has 2 hours of gameplay that ends quickly and abruptly" (2.3h). (2) The ending removes the core verb: "The endgame is not about digging, you can't use your tools" (1.4h), "the game changes genre" (1.8h). (3) The economy runs out: "money becomes functionally useless once you've gotten the upgrades" (1.2h). Also "no physics on anything you dig" (3.5h).
- **Session:** About 1-2 hours per sitting, about 2 hours total.
- **Roblox:** Translates very well: one verb, a visible hole, a short sell trip, upgrade tiers. Doesn't translate: the horror mood and a one-time ending. Roblox needs an endless depth ladder (prestige or new biomes), not a credits roll.

#### 2. One Man's Trash: Jony Pazu Games
- **Release / price:** July 23, 2025, $6.85. Spin-off *One Man's Trash: Pawn Shop After Dark* released Sep 10, 2026 at $2.99 (store lists co-op). [store](https://store.steampowered.com/app/3692070) · [Bleeding Cool](https://bleedingcool.com/games/one-mans-trash-confirmed-for-steam-release-this-month/) · [ITC](https://itc.ua/en/news/real-life-satire-one-man-s-trash-game-about-a-man-who-threw-7-500-bitcoins-into-the-trash-is-out)
- **Sales:** No public figure. With 314 reviews, the Boxleiter rule of thumb (30-60 sales per review) gives roughly 10-20k copies (estimate). Commercially it is small.
- **Reviews:** 84% of 314.
- **Loop:** "Suck. Sell. Upgrade. Repeat." You dig a landfill with a vacuum, and the vacuum can also blow debris out to build structures and climb. Collectibles go on a trophy display. The goal is a lost hard drive, satirizing the real story of a man who threw away about 7,500-8,000 BTC. The game credits AGADAH as partial inspiration.
- **Hook:** The real-world lost-fortune meme, junk with pop-culture relics, and "the deeper you go, the weirder it gets" (7.1h).
- **Praised:** (1) Compulsion: "the urge to keep playing is ridiculously strong" (7.1h). (2) More collectibles than AGADAH and "no scripted dying at the end" (7.7h). (3) Easter eggs and weird finds deeper down (53.2h).
- **Complaints:** (1) Jumpscare worms in a game not labeled horror: "The worms ruined it." (2.6h). (2) Weak upgrades: "Everything just says 'Capacity: +5%'" (12.2h), "nothing changes in the game" (2.0h). (3) Derivative: "basically a carbon copy of the game about digging a hole" (6.5h). Also crashes, the hole refilling and wiping progress, and no way to buy health.
- **Session:** 2-8 hours total (reviewer range 1.8-20.8h).
- **Roblox:** The junk theme and trophy shelf translate well. Avoid jumpscares for a young audience, and make every upgrade visibly change the tool.

#### 3. Lost Bitcoin: Velto Games (UNRELEASED)
- **Status:** "Coming soon" on Steam, no price. Single-player. [store](https://store.steampowered.com/app/5427110)
- **Pitch (from the store page):** Dig a giant junkyard, haul scrap to a furnace and burn it for coins ("the deeper you dig, the more it pays"). More than 60 skill-tree upgrades. Vacuum up a full tank of scrap and shoot it into the furnace. Build a factory on the deck (cranes, belts, sorting gates, machines that make drones, engines, washing machines and robots) that "earns money while you dig." Crack crates and safes, and read identical-looking USB sticks at a computer to find your lost wallet. There is also a buried sailing ship.
- **Note:** The store page discloses that generative AI made "almost all of the game's content." Undisclosed AI art drew review backlash for TCG Card Shop Simulator and Chained Together (see below). Lost Bitcoin does disclose it, but the same perception risk applies (inference).
- **Read:** On paper it combines AGADAH/One Man's Trash (dig-sell) with Hydroneer/Satisfactory (automation) and a treasure reveal (USB sticks). That is combination B in Part 3. No sales or review data exists yet.

#### 4. Motherload (2004 Flash) / Super Motherload (2014): XGen Studios
- **Facts:** A free Flash game on Mars. You drill down, sell minerals, and upgrade the drill, hull, fuel tank and cargo bay. Its sequel Super Motherload was a PS4 launch title, then came to Steam on Apr 4, 2014 at $14.99. [XGen Wikipedia](https://en.wikipedia.org/wiki/XGen_Studios) · [Super Motherload Wikipedia](https://en.wikipedia.org/wiki/Super_Motherload) · [Game Informer](https://gameinformer.com/games/super_motherload/b/playstation4/archive/2013/11/08/dig-deep-in-ps4-launch-title)
- **Sales:** No play-count data found for the Flash original [UNVERIFIED popularity, though it is widely cited as the genre ancestor]. Super Motherload: 784 Steam reviews, 76% positive (SteamSpy). Commercially modest.
- **Loop:** s = drill a tile. m = watch the fuel gauge, get back to the surface before you run dry, sell, refuel. S = 30-90 minutes.
- **Hook:** **Fuel tension.** Reviewers of the sequel praise "the original's fuel tension and the drill-sell-upgrade loop" (8.7h) and "the fear of running low on fuel" (3.3h).
- **Super Motherload complaints:** (1) "The digging feels weightless, blocks simply disappear with no animation" (3.4h). (2) "Tons of rocks that need bombs" (7.5h). (3) Upgrades gated by story, plus "no tooltips for most of the upgrades" (3.3h).
- **Roblox:** The fuel or oxygen return-trip tension is the single best risk lever for a dig loop. The sequel shows that losing dig feedback kills the game.

#### 5. SteamWorld Dig (2013) and SteamWorld Dig 2 (2017): Image & Form
- **Prices / reviews:** SWD1 $9.99, 6,536 reviews, 94%. SWD2 $19.99, 5,744 reviews, 96% (SteamSpy). [SWD1 store](https://store.steampowered.com/app/252410) · [SWD2 store](https://store.steampowered.com/app/571310)
- **Sales:** SWD1 sold more than 1M across all platforms, per the CEO in 2017. SWD2 "started way, way better," with no number given. [Kotaku](https://kotaku.com/the-making-of-a-switch-sleeper-hit-1820022642) · [Nintendo Everything](https://nintendoeverything.com/first-steamworld-dig-has-sold-over-a-million-copies-sequel-sales-on-switch-much-higher-than-other-platforms/)
- **Loop:** Dig down, your lamp/light runs out, return to town, sell ore, buy upgrades. SWD2 adds Metroid-style ability gates. About 6-10 hours in total.
- **Praised (SWD2):** "Metroid-style upgrades are satisfyingly powerful" (14.9h). "some of the best Quality of life I've seen" (35.1h). "A high level of polish" (15.4h).
- **Complaints:** SWD1: "it all ends as soon as it gets started" (8.7h), "oodles of backtracking" (12.2h), "The grind is seriously irritating" (4.5h). SWD2: "So much dialogue. I just wanna dig." (44.0h), and mining "becomes more of a chore" (5.7h).
- **Roblox:** Ability upgrades that open new routes translate well (for example, a drill that breaks a new rock type). Long dialogue and linear story do not.

#### 6. Dome Keeper: Bippinbits / Raw Fury
- **Release / price:** Sep 27, 2022, $17.99. 19,252 reviews, 92%. [store](https://store.steampowered.com/app/1637320)
- **Sales:** More than 500k copies by Oct 2023 [80.lv](https://80.lv/articles/indie-miner-dome-keeper-surges-with-2-500-increase-in-concurrent-players/). VGI estimate about 625k units and $7.1M ([SteamPulse](https://steampulse.org/game/1637320), estimate). 1M players by Sep 2024. Grossed $1M soon after launch ([GWO](https://gameworldobserver.com/2022/10/17/dome-keeper-1-million-revenue-wishlists-success-raw-fury)).
- **Loop:** Mine under your dome during the calm phase, a wave timer counts down, rush back up and defend the dome against the wave, spend ore on upgrades. Roguelike runs of about 30-60 minutes.
- **Hook:** Dig greed versus a timer: "a really fun blend of resource gathering/balancing and base defense" (5.2h). "It's Motherload, but actually good." (146.9h)
- **Complaints:** "you just keep doing the same thing" (10.3h), "does not justify an 18$ price point" (10.5h), "maps are rather empty" (5.1h).
- **Roblox:** A dig-then-defend timer is a natural round structure for co-op servers (one player mines, one defends). Keep maps dense.

#### 7. Deep Rock Galactic: Ghost Ship Games / Coffee Stain
- **Release / price:** 1.0 on May 13, 2020 (Early Access 2018), $29.99. 304,099 reviews, 97%. [store](https://store.steampowered.com/app/548430)
- **Sales:** More than 8M copies across platforms by early 2024 (2.56M of them in 2023). More than 1M MAU on Steam. [WN Hub](https://wnhub.io/news/finance/item-42726). A 12M figure from 2025 is [UNVERIFIED]. Spin-off *DRG: Survivor* sold 500k in its first week of Early Access ([press release](https://mynewsdesk.com/uk/swipe-right/news/deep-rock-galactic-survivor-reaches-500000-units-sold-one-week-after-early-access-release-479844)).
- **Loop:** A 4-dwarf co-op mission of about 20-40 minutes: dig through fully destructible caves, mine the objective mineral, survive swarms, call the drop pod, extract. Between missions: perks, cosmetics, a free battle pass.
- **Hook:** Strangers cooperate ("You have never seen a game where strangers will work together", 168.6h). Voice lines like "Rock and Stone" became a meme. Free cosmetics, no pay-to-win.
- **Praised:** (1) Cooperation. (2) A free battle pass, "no paywalls" (573.7h). (3) Gunplay (1,057h).
- **Complaints:** (1) Colorblind accessibility (0.2h). (2) "Once you have your first OC you have effectively reached the end of progression" (4,204h). (3) Slow bug fixes.
- **Roblox:** Co-op dig-and-extract with a shared objective and a call-in extraction translates very well. Its shooter depth does not need to.

#### 8. Hydroneer: Foulball Hangover
- **Release / price:** 1.0 on May 8, 2020, $14.99. 27,303 reviews, 87%. PS5/Xbox May 8, 2026. [store](https://store.steampowered.com/app/1106840)
- **Sales:** "Over a million copies on Steam," per the developer as reported by Rutab [UNVERIFIED primary]. GameDiscoverCo covered it in 2021 as an under-the-radar hit of about 500k ([GameDiscoverCo](https://newsletter.gamediscover.co/p/this-game-sold-nearly-500k-copies)).
- **Loop:** Dig dirt by hand, pan it for gold and gems, sell, buy drills, conveyors and water-powered sluices that automate the panning, expand the base.
- **Praised:** "Building elaborate systems of conveyors and drills and plumbing is good fun" (20.9h). "The aesthetic is relaxing and cute" (20.9h). Customization (22.6h).
- **Complaints:** (1) Save wipes: "my world is completely wiped" (176h). (2) "multiple non-exchangeable currencies to gate progress with grinding delivery tasks" (118h). (3) "You can only hold one item at the time" (56h). Also bugs.
- **Roblox:** Closest proven ancestor of "dig and also build a machine that digs for you." Copy the conveyor joy, but fix carry friction and use one currency.

#### 9. Gold Rush: The Game, now "Gold Mining Simulator": Code Horizon
- **Release / price:** Oct 13, 2017, $19.99. 15,166 reviews, 72% (Mixed-leaning). Renamed after the Discovery license ended. [store](https://store.steampowered.com/app/451340)
- **Sales:** "Over 2 million copies across PC and consoles," per the developer's press release for the sequel ([Game Developer PR](https://www.gamedeveloper.com/press-release/gold-mining-simulator-2)). Self-reported.
- **Loop:** Run excavators, trucks and wash plants, pay out the gold, buy bigger machines and claims. Sessions of several hours.
- **Praised:** "the base mechanics of the game actually work really well" (18.6h), terrain detail, the variety of claims.
- **Complaints:** Dishonest communication about updates, critics banned, "not finished" with poor performance, "should've had a multiplayer/co-op" (12.3h). The sequel announced in 2025 leads with multiplayer.
- **Roblox:** Heavy-machinery fantasy works. The Roblox fix is co-op crews and arcade physics.

#### 10. Idle mining incrementals: Idle Miner Tycoon (mobile), Mr.Mine, Keep on Mining!
- **Idle Miner Tycoon (Kolibri Games, July 2016, F2P mobile):** More than 150M downloads by Sep 2022. Ubisoft bought 75% in Feb 2020 at a €160M valuation. Built in 8 weeks. [Kolibri press](https://kolibrigames.com/press/kolibri-games-hit-title-idle-miner-tycoon-surpasses-150-million-downloads) · [Kolibri Wikipedia](https://en.wikipedia.org/wiki/Kolibri_Games). Loop: tap the shaft, elevator and warehouse, hire managers to automate each, upgrade, open new shafts, prestige into new mines. Revenue is not public.
- **Mr.Mine (Steam F2P with IAP, Sep 30, 2020):** 92% of about 17k (SteamSpy), 500k-1M owners (SteamSpy). Complaints: "progress is just too slow" (2,697h), "a gatcha with very low drop rate" (459h), not truly idle ("Save your mouse", 681h), and paying real money to revive scientists. [store](https://store.steampowered.com/app/1397920)
- **Keep on Mining! (EagleEye, July 30, 2025, $4.99):** 91% of 3,109 English (8,378 total). Hover over rocks to mine, ore becomes bars, bars buy a skill tree, pick 1 of 3 talent cards on each level-up, then an idle "Mine" unlocks. [store](https://store.steampowered.com/app/3769130). Complaints: "Feels like a demo" (5.4h), endgame grind (4.9h), "All systems rely heavily on RNG" (4.0h), and the passive Mine "never worth investing a single penny" (5.1h).
- **Roblox:** The manager-automation and prestige layer is the proven mobile monetization frame. Avoid gacha-gated progress and passive income that isn't worth buying.

### B. Junk, scrap, cleaning and "satisfying" sims

#### 11. PowerWash Simulator: FuturLab
- **Release / price:** July 14, 2022, $24.99. 51,091 reviews, 97%. PWS2: Oct 23, 2025, $24.99, 11,150 reviews. [store](https://store.steampowered.com/app/1290000)
- **Sales:** More than 12M players by Apr 2024 and more than 17M later. Players, not sales, since the count includes Game Pass. [FuturLab](https://www.futurlab.co.uk/news/thank-you-for-12-million-powerwash-simulator-players) · [PCGamesInsider 17M](https://www.pcgamesinsider.biz/news/75072/powerwash-simulator-reaches-17m-players/). PWS2 estimate: 699k+ copies, $17.8M+ ([AppMagic](https://appmagic.rocks/blog/steam-simulation-games-2026), estimate).
- **Loop:** s = spray, and dirt vanishes in a stripe. m = each object dings when it hits 100%. S = one job (a house, vehicle or park) takes 30-90 minutes. Co-op washing. Licensed DLC packs (SpongeBob, Back to the Future, Warhammer).
- **Hook:** A visible, deterministic completion meter. Even a child "still recognizes the satisfaction of clean" (77.5h).
- **Praised:** Satisfying cleaning that parent and child can share. "very simple concept that is pulled off well" (18.1h). Replay value.
- **Complaints:** (1) "60% of the achievements are dlc locked" (32.7h). (2) "paid DLCs are overpriced" (128h). (3) Privacy policy with no decline button. Also "The Guest is paid 25% for each job" in co-op (0.9h).
- **Roblox:** The per-object "ding at 100%" is ideal and low-tech: show the % outline. Never lock completion goals behind paid content, and pay guests fully in co-op.

#### 12. House Flipper: Empyrean / Frozen District / PlayWay
- **Release / price:** May 17, 2018, $24.99 (shows $1.99 on sale). 92,689 reviews, 94%. [store](https://store.steampowered.com/app/613100)
- **Sales:** 2.1M on PC by 2021 ([GamePressure](https://www.gamepressure.com/newsroom/tags/empyrean/z452e8)). "Over 5M globally" in later reporting [UNVERIFIED primary]. House Flipper 2 passed 1M ([Gamereactor](https://www.gamereactor.eu/?p=119695), [GameDiscoverCo](https://newsletter.gamediscover.co/p/house-flipper-2-how-the-sequel-cleaned)).
- **Loop:** Clean trash and grime, repair, paint, furnish, sell for profit, buy a bigger house.
- **Praised:** "overwhelmingly theraputic" (5.0h), "oddly satisfying and great attention to detail" (6.1h), "as chill or as serious as you want to be" (421h). Played with a retired mom (695h).
- **Complaints:** Performance, repetitive buyers, DLC-locked basics ("Buy our $20 DLC or your yards stay disgusting!"), updates wiping progress.
- **Roblox:** A "before and after" reveal plus profit. The flip-for-profit layer suits shop-tycoon structures.

#### 13. Junkyard Simulator: Rebelia / PlayWay
- **Release / price:** Oct 13, 2021 (still Early Access), $19.99. 2,189 reviews, about 62-64% (Mixed). 100-200k owners (SteamSpy). [store](https://store.steampowered.com/app/671970)
- **Loop:** Process scrap with heavy machinery, restore cars and furniture, sell on a scrap market, buy random loot containers.
- **Complaints (the useful part):** "locations and items sometimes just decide not to load" (51.8h), "UI is fugly" (6.1h), "no sense of progression" (7.5h), "feels like busy work" (17.1h), "the renovation 'minigame' for found objects is lackluster" (14.3h).
- **Read:** Proof that the junkyard theme alone doesn't sell. Feedback, progression and polish do. The renovation verb was the weak link (see combination D).

#### 14. Supermarket Simulator: Nokta Games
- **Release / price:** Early Access Feb 20, 2024. 1.0 June 19, 2025. $19.99. 79,834 reviews, 94%. Four-person studio. [store](https://store.steampowered.com/app/2670630)
- **Sales:** AppMagic estimates 3.4M+ copies and $45M+. Raijin estimates 1.8M on Steam. Both are estimates. [AppMagic](https://appmagic.rocks/blog/steam-simulation-games-2026)
- **Loop:** Order stock, carry boxes, fill shelves, set prices, scan at checkout, expand and decorate.
- **Praised:** "simple but addictive" (133h), customization, steady QoL updates ("Tablet & Scanner"), "brain numbing in a good way" (546h).
- **Complaints:** Base content locked behind DLC ("NOT worth a total of $47"), bugs, "more Restocking+cashier simulator" (16.6h).
- **Roblox:** The job-sim loop is already a Roblox staple. The lesson is the QoL-upgrade cadence (tools that remove tedium are rewards in themselves).

#### 15. Cleaning and tidying wave, 2025-26: Librarian, Cash Cleaner, Goblin Cleanup, Hozy, Storage Hunter, ReStory
All figures are AppMagic estimates ([AppMagic](https://appmagic.rocks/blog/steam-simulation-games-2026)) unless noted:
- **Librarian: Tidy Up the Arcane Library!** (Apr 30, 2026, $5.99, 25,994 reviews): 1.2M+ copies, $7.2M+. Sort 3,000+ misplaced books, with spells that automate shelving.
- **Cash Cleaner Simulator** (May 8, 2025, $19.99, 7,451 reviews, 88%): 510k+ copies, $7.3M+. Clean, sort and count cash under deadlines.
- **Storage Hunter Simulator** (Nov 27, 2025, $24.99, 3,909 reviews, 83%): 547k copies, $8M+. Bid on storage units and dig out valuables.
- **Goblin Cleanup** (co-op, $19.99): 257k copies. Clean a dungeon after the heroes leave.
- **Hozy:** 368k+ copies. ASMR chores.
- **ReStory** (repairing retro electronics, $18-20): about 500k units in about a month, per GameDiscoverCo ([Aug 2026](https://newsletter.gamediscover.co/p/august-2026s-top-new-pc-and-console)).
- **Read:** "Restore order from chaos" keeps printing mid-size hits at $6-25, and co-op versions (Goblin Cleanup) exist.

#### 16. TCG Card Shop Simulator: OPNeon Games
- **Release / price:** Early Access Sep 2024. 1.0 Sep 14, 2026. $19.99. 48,328 reviews, 97% (SteamSpy). [store](https://store.steampowered.com/app/3070070)
- **Sales:** Raijin estimates about 1.1M on Steam. More than 3.5M across Steam and Xbox during Early Access, per Pokde ([Pokde](https://pokde.net/gaming/pc-master-race/tcg-card-shop-simulator-version-1-0)).
- **Loop:** Stock and sell packs, and **open packs yourself** (rarity reveal, collection binder), sell singles, run the shop.
- **Praised:** "Opening packs is so satisfying" (242h). It gives the TCG loop "with no lootbox spending" (84.7h).
- **Complaints:** Undisclosed AI art ("some AI art I wasn't expecting", 7.4h), repetitive, "'pack opening' simulator, NOT a simulation of running a card shop" (391h), slow updates, lag since 1.0.
- **Roblox:** Rarity reveal plus collection is a native Roblox pattern. Paid random items on Roblox carry platform rules [UNVERIFIED current policy specifics; check the Roblox Creator docs].

#### 17. Satisfying puzzle sims (Viewfinder, Unpacking), for context
- **Viewfinder** (July 18, 2023, $24.99): 12,271 reviews, 94%, 200-500k owners (SteamSpy). Perspective puzzles. [store](https://store.steampowered.com/app/1382070)
- **Unpacking** (Nov 1, 2021, $19.99): 35,415 reviews, 93%, 500k-1M owners (SteamSpy). [store](https://store.steampowered.com/app/1135690)
- **Read:** Both are high-quality but finite, authored puzzles. The repeatable part is "putting things in their place," which Librarian scaled with automation (inference).

### C. Treasure, fishing and lite-adventure

#### 18. Dave the Diver: Mintrocket (Nexon)
- **Release / price:** June 28, 2023, $19.99. 144,276 reviews, 97%. [store](https://store.steampowered.com/app/1868140)
- **Sales:** More than 5M across platforms (Nov 2024, official). [Gematsu](https://www.gematsu.com/2024/11/dave-the-diver-sales-top-five-million)
- **Loop:** Day: dive and harpoon fish until oxygen or weight forces you up. Night: serve those fish in a sushi restaurant, earn money, upgrade gear. A dual loop where each half feeds the other.
- **Praised:** "Combining the diving/exploration component with the restaurant management works wonders" (40.2h), the many minigames, humor, music.
- **Complaints:** "30 hours of non-stop tutorials" (27.2h), "Each day becomes a maaassive chore" (27.3h), a "laundry list of to-do's" (31.4h).
- **Roblox:** "Gather, then sell in your own shop" is a proven dual loop. Cap the number of systems.

#### 19. DREDGE: Black Salt Games / Team17
- **Release / price:** Mar 30, 2023, $24.99. 48,221 reviews, 96%. [store](https://store.steampowered.com/app/1562430)
- **Sales:** More than 1M by Oct 2023. The internal target was 100k in year one, which it hit in 24 hours. [80.lv](https://80.lv/articles/an-indie-game-dredge-has-sold-over-1-million-copies/)
- **Loop:** Fish with a timing minigame, fit the catch into a grid cargo hold (Tetris-style inventory), get back to port before night brings dread, sell, upgrade the boat. Some catches are mutated "aberrations."
- **Praised:** "The gameplay loop feels incredible" (38.8h), the fishing minigames, relaxing pace with creeping dread.
- **Complaints:** Every fishing minigame feels the same, "80% of your time going back and forth" (14.2h), late upgrades "didn't matter anymore" (19.8h).
- **Roblox:** Grid inventory packing plus "get home before dark" is an elegant risk loop. Rare mutated variants are collectible.

#### 20. WEBFISHING: lamedeveloper
- **Release / price:** Oct 11, 2024, $4.99. 57,423 reviews, 98% (SteamSpy). [store](https://store.steampowered.com/app/3146520)
- **Sales:** Estimates cluster around 1-2M (Raijin 1.3M, SteamSpy 1-2M owners). Vaporlens' 5M is an outlier. [Wikipedia](https://en.wikipedia.org/wiki/Webfishing). GameDiscoverCo puts median playtime at about 8.5 hours, high for a $5 game ([GameDiscoverCo](https://newsletter.gamediscover.co/p/what-were-steams-most-unexpected)).
- **Loop:** Fish, chat with a text bubble or voice, emote, decorate, draw with chalk. A social hangout first and a game second.
- **Praised:** "very relaxing and fun" (11.1h), "no pressure to be at a certain level" (11.9h), friends made there.
- **Complaints:** Hackers exposing player data, development abandoned, no reporting or moderation, NSFW harassment, strangers joining "offline" sessions.
- **Roblox:** Roblox already is this hangout, with moderation built in. The proven part is a low-pressure shared activity as an excuse to hang out.

#### 21. How to Fish: Dazed Games (Landfall-funded), 2026 breakout
- **Release / price:** Aug 20, 2026, $7.99. 75,522 reviews. English 95% of 29,101 (Overwhelmingly Positive). [store](https://store.steampowered.com/app/4001890)
- **Sales:** 1M in 2 days ([Dot Esports](https://dotesports.com/indies/news/how-to-fish-game-sales-friendslop-steam-indie-coop)). More than 8.5M units and $38M+ lifetime, per GameDiscoverCo's estimate ([Sept 2026](https://newsletter.gamediscover.co/p/september-2026s-top-new-pc-and-console)). Peak CCU about 341-370k.
- **Loop:** 1-4 players stranded on an island. Fish, fight fish, sell or **gamble** the catch, buy gear, beat fish bosses to unlock islands. Rare variants to collect, trick-shot bonuses (snipe seagulls). A finite campaign of a couple of hours.
- **Complaints:** Backend and multiplayer security, crashes, items vanishing from the floor, "complete within an hour" (3.3h), repetitive.
- **Roblox:** A short co-op campaign with a sell/gamble/upgrade economy and bosses unlocking areas. It maps directly to a Roblox "world progression" game.

### D. Co-op "friendslop"

#### 22. Lethal Company: Zeekerss
- **Release / price:** Oct 23, 2023 (Early Access), $9.99. 412,009 reviews, 97%. [store](https://store.steampowered.com/app/1966720)
- **Sales:** About 9.4-10M estimated by early 2024 (Boxleiter method, not official). [Game Developer](https://gamedeveloper.com/business/lethal-company-sold-an-estimated-10-million-copies) · [Wikipedia](https://en.wikipedia.org/wiki/Lethal_Company)
- **Loop:** A 4-person crew lands on a moon, scavenges scrap from a facility while monsters hunt them, extracts, and sells scrap to hit a rising **profit quota** every 3 days. Fail and you're fired, which wipes the run. Sessions of 1-2 hours.
- **Hook:** Proximity voice chat makes deaths funny. "Genuine horror, loony toons slapstick comedy, and a scooby doo chase scene" (382h).
- **Complaints:** "there is no ending" and no save files (87h), lobbies hard to find, difficulty raised "so high its basically unplayable" (1,036h), repetitive interiors, stalled updates.
- **Roblox:** The quota-scavenge-extract structure is fully portable. Horror intensity must be dialed down for a young audience.

#### 23. R.E.P.O.: semiwork
- **Release / price:** Feb 26, 2025 (Early Access), $9.99. 346,178 reviews, 96-97%. [store](https://store.steampowered.com/app/3241660)
- **Sales:** 16.4M copies on Steam in H1 2025, #1 of all co-op games (Alinea estimate) ([gamedevreports](https://gamedevreports.substack.com/p/alinea-analytics-co-op-games-generated)). $147M gross Steam revenue in 2025 and 19.6M players ([Alinea](https://alineaanalytics.substack.com/p/the-top-new-2025-games-by-players)). Not official.
- **Loop:** Like Lethal Company, but the loot is **physics objects** (fragile vases, TVs) carried with a grab gun. Break it and you lose value. Hit the extraction quota, then shop. A 1-2 hour run.
- **Hook:** Physics plus ragdolls plus proximity voice equals clips of friends smashing a $10k vase.
- **Praised:** Developer responsiveness, "polished, balanced and a lot of fun with friends" (82h), small touches, "Perfect co-op experience" (28h).
- **Complaints:** Tier-3 monsters too early ("supposed to be a fun and silly friend 'party' game", 44h), "STOP. MAKING. THE. GAME. HARDER." (243h), item costs too steep, respawning at 1 HP.
- **Roblox:** Physics-carry plus fragile loot plus a quota is a top-tier Roblox fit. Keep it a party game.

#### 24. PEAK: Aggro Crab and Landfall
- **Release / price:** June 16, 2025, $7.99 ($5 in launch week). 309,999 reviews. English 95% of 147,410. [store](https://store.steampowered.com/app/3527290)
- **Sales:** 4.5M in about 3 weeks, per the studio head. Launched with only 29,384 wishlists, with the Steam page live 4 days before launch. Median playtime 3h53m. [GameDiscoverCo](https://newsletter.gamediscover.co/p/how-peak-sold-45m-copies-in-less). About 10M by mid-Aug 2025 (Alinea, estimate). $87M Steam revenue in 2025 (Alinea).
- **Loop:** s = climb while a damageable **stamina bar** drains (weight, poison and cold eat into it). m = rest, cook, help or revive friends. S = one mountain per run, with a new procedural mountain daily.
- **Hook:** Emotes and ghost-form spectating after death make it fun to watch. "one of the funniest (and most chaotic) adventures" (113h). Dev quote: "a terrain to climb up, and the uniquely damageable stamina bar."
- **Complaints:** Post-launch EULA, devs making it harder, no public lobby browser, the Roots biome, server dependence.
- **Roblox:** One readable resource bar plus friends plus a daily procedural map. Roblox already has huge "climb with friends" obbies (inference).

#### 25. Content Warning: Landfall
- **Release / price:** Apr 1, 2024, free for 24 hours, then $7.99. 73,078 reviews, 95%. [store](https://store.steampowered.com/app/2881650)
- **Sales:** About 6.2M free claims, 204k peak CCU, then more than 1M paid within about 2 weeks. [Wikipedia](https://en.wikipedia.org/wiki/Content_Warning) · [Game Developer](https://gamasutra.com/business/content-warning-sells-1-million-copies-following-launch-giveaway)
- **Loop:** Film monsters in the "Old World" on a camera, upload the footage, earn views (the quota), buy gear.
- **Praised:** "death is actually fun and rewarding" (19h), "silly and amazing physics" (10h), finding your old camera where you died.
- **Complaints:** Abandoned ("left to get milk and never came back", 60h), all content seen in about 10 hours, "only one person REALLY is in control" (4.0h), "so much luck involved" (3.2h).
- **Roblox:** Make every role matter, not just the camera holder. Footage-as-score is clever, but live updates are what keep it alive.

#### 26. Chained Together: Anegar Games
- **Release / price:** June 19, 2024, $4.99. 55,340 reviews, 91%. [store](https://store.steampowered.com/app/2567870)
- **Sales:** Peak 85,638 CCU, 11th-biggest Steam launch of 2024 by CCU ([GWO](https://gameworldobserver.com/2024/06/25/chained-together-85k-concurrent-players-launch-steam)). No unit figure. SteamSpy shows 2-5M owners (context only). It took 48% of all friendslop CCU at its peak ([How To Market A Game](https://howtomarketagame.com/2026/07/30/is-friendslop-saturated)).
- **Loop:** A vertical climb while physically chained to friends. One fall drags everyone down.
- **Praised:** Blame-based comedy ("It's about the friends we lost along the way", 9.9h), cheap.
- **Complaints:** "Needs a shove button" (6.1h), chain clipping, region lock, "asset flipped, AI generated" (0.2h).
- **Roblox:** Shared-fate physics comedy. Roblox obby culture already supports it (inference).

#### 27. RV There Yet?: Nuggets Entertainment
- **Release / price:** Oct 21, 2025, $7.99. 76,371 reviews. English 89% of 32,166. [store](https://store.steampowered.com/app/3949040)
- **Sales:** 1,288,515 in 5 days, per the developer ([Insider Gaming](https://insider-gaming.com/rv-there-yet-steam-indie-sensation-sells-1-3-million-units-in-first-week/)). More than 4.5M by Dec 2025 [UNVERIFIED secondary]. Peak about 100k CCU. Its 7-day sales-to-wishlist ratio peaked at 48x the median (GameDiscoverCo).
- **Loop:** 4 friends drive one RV over terrible terrain, using a physics winch to get past obstacles, scavenging repairs and supplies.
- **Complaints:** "needed more time to cook" (6.0h), wobbly physics, lost checkpoint progress, repetitive winch, random players griefing the RV.

#### 28. MECCHA CHAMELEON: two developers in Japan (2026's biggest seller)
- **Release / price:** June 9, 2026, $5.99. 81,063 reviews. English 90% of 44,156. [store](https://store.steampowered.com/app/4704690)
- **Sales:** 15M in about 25 days, per the developers (1M in 4 days, 10M in 16 days). Peak about 340k CCU. Built in about 2 months by two Fortnite UEFN creators. [Windows Central](https://www.windowscentral.com/gaming/the-viral-hit-of-2026-has-sold-15-million-copies-in-a-month-on-steam-costs-usd5-and-was-made-by-2-people) · [Hitmarker](https://hitmarker.net/news/indie-hit-meccha-chameleon-is-now-the-best-selling-game-of-2026-1944965). A 20M figure is [UNVERIFIED].
- **Loop:** Hide and seek for up to 10 players. Hiders **paint their white bodies** to camouflage into the stage. Rounds of a few minutes.
- **Hook:** "an art contest for the hider" (12.7h). Reveals that are easy to clip. Built-in streamer viewer-lobby support.
- **Complaints:** Security or malware fears, cheating, polish and UI, lobbies that never fill, public play degenerating into "hiding in dark corners."
- **Roblox:** Hide-and-seek and prop-hunt are already Roblox-native. Meccha proves that one creative verb (paint) refreshes an old mode.

#### 29. Gamble With Your Friends: TENSTACK
- **Release / price:** May 1, 2026, $7.99. 21,973 reviews. English 88% of 12,656. [store](https://store.steampowered.com/app/3892270)
- **Sales:** 1M in about a week ([games.gg](https://games.gg/news/gamble-with-your-friends-steam-friendslop/)). Just over 2M in May, per GameDiscoverCo ([May 2026 report](https://gamedevreports.substack.com/p/gamediscoverco-top-games-on-steam-ab4)).
- **Loop:** 1-6 players share one bank account and one debt. Each "day" gives 5 minutes in the casino to hit the loan shark's quota. 17 games of chance, risky items. A 2-3 hour campaign with 3 endings.
- **Complaints:** "Being pressured by a 5 minute timer is not fun" (0.6h), "zero point to go over quota" (12.8h), "No items are persistent" (1.9h), little real cooperation.
- **Roblox:** A shared wallet plus a quota is a strong social glue. Real-money-adjacent gambling themes are a policy risk for minors on Roblox (inference).

#### 30. Other 2025-26 friendslop data points
GameDiscoverCo and HTMAG data, estimates unless the developer stated them:
- **YAPYAP** (Feb 2026, $10): more than 700k.
- **Super Battle Golf** ($8-13): 500k in 9 days.
- **Mage Arena** ($2.99): 624k in week 1, $3.7M net, while holding only 11.75% of friendslop CCU ([HTMAG](https://howtomarketagame.com/2026/07/30/is-friendslop-saturated)).
- **Big Walk** ($15-20): more than 1.6M on Steam in Aug 2026.
- **BOMBANANA!** (chaotic co-op bomb disposal, Sep 2026): more than 1M.
- **Grain Rot** ($9-10, co-op extraction "unbuilder"): more than 200k in 3 weeks.

[GameDiscoverCo Feb 2026](https://newsletter.gamediscover.co/p/february-2026s-top-selling-new-steam) · [Aug 2026](https://newsletter.gamediscover.co/p/august-2026s-top-new-pc-and-console) · [Sep 2026](https://newsletter.gamediscover.co/p/september-2026s-top-new-pc-and-console)

**Genre-level facts:**
- Co-op games grossed about $4.1B on Steam in H1 2025, an all-time high (+11% year over year). The top 5 sellers by copies in H1 2025 were all co-op ([Alinea via gamedevreports](https://gamedevreports.substack.com/p/alinea-analytics-co-op-games-generated)).
- Top friendslop titles take more than 50% of genre CCU, then fade to about 10% within 3-9 months. The audience is "hungry," not saturated ([HTMAG](https://howtomarketagame.com/2026/07/30/is-friendslop-saturated)).
- Common traits: low barrier, proximity voice, physics, low-fi 3D, under $20 ([Wikipedia: Friendslop](https://en.wikipedia.org/wiki/Friendslop)).

### E. Incremental, idle and roguelite "number go up"

#### 31. Cookie Clicker: Orteil / DashNet / Playsaurus
- **Facts:** Browser Aug 8, 2013. Steam Sep 1, 2021 at $4.99. 88,880 reviews, 97%. More than 60k CCU at the Steam launch. Raijin estimates about 2.5M Steam copies, about $10.8M. [Wikipedia](https://en.wikipedia.org/wiki/Cookie_Clicker) · [store](https://store.steampowered.com/app/1454400)
- **Loop:** Click, buy buildings (each costs 15% more than the last), and click golden cookies for random buffs. Then ascend: reset for heavenly chips worth +1% production per level. The cost of the next level scales with the cube of the level.
- **Praised:** "Number go up, brain give chemical." (25,312h). Cloud saves and the C418 music.
- **Complaints:** Late game relies too heavily on golden-cookie luck, slow time-gated sugar lumps, a memory leak.

#### 32. Egg, Inc.: Auxbrain (mobile, 2016)
- **Facts:** More than 10M installs on Google Play ([AppBrain](https://www.appbrain.com/dev/Auxbrain+Inc/)). Revenue not public. [Wikipedia](https://en.wikipedia.org/wiki/Egg,_Inc.)
- **Loop:** Tap to hatch chickens, build housing, vehicles and silos, research upgrades. A "nested" prestige converts progress into soul eggs, a permanent multiplier.
- **Roblox:** Idle-farm plus prestige is a standard Roblox simulator spine (inference).

#### 33. Bongo Cat: Irox Games / Marcel Zurawka
- **Facts:** Mar 5, 2025, free. About 5.7M players by Feb 2026 and about 194k all-time peak CCU (trackers). 91k+ reviews, 97% ([GamesMarket](https://www.gamesmarket.global/bongo-cat-is-on-its-way-to-6-million-players)). Despite the scale, the developer reported only about $2-4k a month of net profit in 2025 ([Yardbarker](https://www.yardbarker.com/video_games/articles/150k_players_daily_yet_bongo_cat_isnt_profitable/s1_17458_42389339)).
- **Loop:** A cat in the corner of your screen bongos whenever you press a key in any app. Time spent drops a cosmetic item about every 30 minutes. Items can be traded and sold on the Steam market. Friends' cats are visible (multiplayer update).
- **Praised:** "rewards you an item every 30 minutes" (79h), "the psychological grind is unmatched" (938h), motivation to study.
- **Complaints:** Limited items feed scalpers, "paid FOMO into a free game" (battle pass), CPU use, data trust.
- **Read:** Passive-time drops plus tradeable rarity can drive massive engagement, but the developer's own monetization was weak. Steam's market captured the value. Roblox's own economy (UGC and trading) changes that (inference).

#### 34. Vampire Survivors: poncle
- **Facts:** Oct 20, 2022, $4.99. 252,572 reviews, 98.5%. More than 27M players (official, 2026) ([Push Square](https://www.pushsquare.com/news/2026/04/vampire-survivors-dev-doesnt-need-to-at-us-its-working-on-15-projects)). Steam estimates of 6.6-7.9M copies (Raijin, VGI).
- **Loop:** Move only (attacks fire automatically), pick up XP gems, choose 1 of 3 upgrades on each level-up, evolve weapons, survive 30 minutes. Gold buys meta upgrades.
- **Praised:** "simple, and addictive" (97h), one-handed play (94h), "100 hours ... out of a $3 game" (120h), "just going to play one more run" (43h).
- **Complaints:** "shallow manufactured addiction" (3.9h), repetitive late game, "starts feeling like an idle game" (11.8h), no skill expression.

#### 35. Megabonk: vedinad (solo)
- **Facts:** Sep 18, 2025, $9.99. 101,373 reviews. English 93% of 58,692. 1M in about 2 weeks (developer) ([GWO](https://gameworldobserver.com/2025/10/03/megabonk-is-a-new-indie-hit-on-steam-the-games-sales-have-surpassed-one-million-copies)). [store](https://store.steampowered.com/app/3405340)
- **Loop:** Vampire Survivors in 3D, with movement tech (jumps, slides), random maps and bosses, chests, and build stacking.
- **Praised:** "when things pop off, it's very satisfying" (28h), "evaporate swarms of enemies" (19h), playing with dad (401h).
- **Complaints:** Few viable builds, late spikes punish anything off-meta, grindy unlocks, slow movement, few updates.

#### 36. BALL x PIT: Kenny Sun / Devolver
- **Facts:** Oct 15, 2025, $14.99. 25,293 reviews. 300k in 5 days, 1M by Dec 2025, more than 2M by Aug 2026 (official). Devolver's internal target was 300k in year 1. [Game Developer PR](https://www.gamedeveloper.com/press-release/devolver-digital-s-ball-x-pit-s-final-free-update-the-naturalist-update-arrives-today-as-the-ball-hit-crosses-2-million-copies-sold)
- **Loop:** Breakout-style ball-bouncing roguelite runs that fuse balls into evolutions, plus a city-building meta layer between runs.

#### 37. Balatro: LocalThunk / Playstack
- **Facts:** Feb 20, 2024, $14.99. 162,271 reviews, 98%. More than 5M (Jan 2025, official, excluding Apple Arcade). [MobileSyrup](https://mobilesyrup.com/2025/01/21/balatro-5-million-copies-sold-update/)
- **Loop:** Play poker hands, and jokers multiply the score, so numbers explode. Beat each blind's threshold or the run ends.
- **Praised:** "the CIV of card games" (176h), stakes as depth, "simple, elegant, addictive, endlessly replayable."
- **Complaints:** All-or-nothing blinds, "feel like a slot machine" (35.5h), repetitive after a few plays.

### F. Automation

#### 38. Factorio: Wube
- **Facts:** 1.0 on Aug 14, 2020, $35. 196,870 reviews, 97%. 3.5M sold by late 2022, at about 500k a year (official) ([PC Gamer](https://pcgamer.com/factorio-has-sold-35-million-copies)). Space Age DLC: more than 400k at launch.
- **Praised:** "zero grind, because everything can be automated" (106h), "always something to do" (106h), logistics robots and blueprints (1,985h).

#### 39. Satisfactory: Coffee Stain
- **Facts:** 1.0 on Sep 10, 2024, $39.99. 236,782 reviews, 97%. More than 5.5M by Feb 2024 (official) ([GWO](https://gameworldobserver.com/?p=26400)).
- **Complaints:** "no way to set buildings en masse" (75h), frustrating first-person placement, no meta-progression, "Nothing threatens you" (485h).
- **Read:** Automation's proven joy is "the factory works while I do something else." Its proven pain is placement tedium. For Roblox, use snap-to-grid placement and pre-built modules (inference).

#### 40. Schedule I: TVGS (solo)
- **Facts:** Mar 24, 2025 (Early Access), $19.99. 293,234 reviews, 98%. AppMagic estimates 10.2M+ copies and $189M+. Alinea: 9M copies in H1 2025 and $151M 2025 Steam revenue (the #1 new indie). Peak about 450k CCU (Beebom). [AppMagic](https://appmagic.rocks/blog/steam-simulation-games-2026) · [Alinea](https://alineaanalytics.substack.com/p/the-top-new-2025-games-by-players)
- **Loop:** Grow, mix and package product, deal to customers, hire employees and buy machines to **automate production**, expand territory. Co-op.
- **Praised:** "Easily 30-40 hours of game play" (50h), "satisfying pacing in growth" (109h), "keeps blowing your mind as you progress" (107h).
- **Complaints:** "almost 0 endgame" (92h), progression blocked by cartel spawns, multiplayer bugs, "only grinding" (45h), employee-related stutter.
- **Roblox:** The drug theme is unusable on Roblox. The structure is the takeaway: hand-craft first, then hire or automate, then expand.

### G. 2026 breakout that is a warning sign: Needle In A Haystack (Simulator)
- A viral clip got 50M+ views on X, and the game was cloned on Steam more than 10-14 times before the original even released. Press called this the "Robloxification of Steam." [Kotaku](https://kotaku.com/the-proliferation-of-copycats-on-steam-makes-discovering-original-games-like-finding-a-needle-in-a-haystack-2000734794) · [Dexerto](https://www.dexerto.com/gaming/needle-in-a-haystack-simulator-dev-apologizes-to-steam-for-the-flood-of-rip-offs-his-game-inspired-3411907/) · [Plagiarism Today](https://www.plagiarismtoday.com/2026/09/17/the-attack-of-the-roblox-clones/). No sales data.
- **Read:** A one-verb "absurd task" sim (search, dig, clean) can go viral from a single clip. Speed to market and a defensible depth layer matter more than the premise (inference).

---

## Part 2: Synthesis

### The 10 strongest proven loop ingredients

1. **Dig, sell, upgrade, deeper (the Motherload ladder).** Proven by AGADAH (1M+ at $5, built in under a month), SteamWorld Dig (1M+), Dome Keeper (>500k, 92%), DRG (8M+), Idle Miner Tycoon (150M downloads), Keep on Mining (91%), and Dave the Diver (5M; dive deeper and sell). Evidence: reviewers keep naming Motherload as what they want ("It's Motherload, but actually good"). The fail cases fail on feedback (Super Motherload's "blocks simply disappear") and length, not on the loop itself.
2. **Return-trip tension (a resource that forces you back).** Fuel in Motherload, light in SteamWorld Dig, oxygen in Dave the Diver, night or sanity in DREDGE, the wave timer in Dome Keeper, stamina in PEAK. Evidence: reviewers cite "the fear of running low on fuel," and PEAK's devs call the damageable stamina bar "the main tension." It turns a grind into a decision.
3. **Friends plus proximity voice plus physics or ragdoll (the clip generator).** Lethal Company (~10M est.), R.E.P.O. (16.4M in H1'25, est.), PEAK (4.5M in 3 weeks from 29k wishlists), Content Warning, Chained Together, RV There Yet (1.29M in 5 days), Meccha Chameleon (15M in 25 days). Evidence: co-op is the top Steam revenue segment ($4.1B in H1'25). PEAK and Meccha grew almost entirely from streamer and Twitch clips.
4. **Shared quota or extraction with collective stakes.** Lethal Company (profit quota), R.E.P.O. (extraction quota with fragile loot), Gamble With Your Friends (shared debt, 2M), Content Warning (a view quota), DRG (mission objective plus drop pod). It creates a group goal, blame and comedy in a single number.
5. **Visible "before and after" completion (satisfying clean or reveal).** PowerWash (17M players, 97%), House Flipper (2.1M+ PC, 94%), Librarian (1.2M est.), Cash Cleaner (510k est.), Unpacking (93%), ReStory (~500k). Evidence: "even a child recognizes the satisfaction of clean." The per-object 100% ding works across ages.
6. **Number go up, with prestige multipliers.** Cookie Clicker (the idle genre's origin, 97%), Egg Inc (nested prestige), Idle Miner Tycoon (150M), Balatro (5M; multiplicative scoring), Vampire Survivors (27M players). Evidence: "Number go up, brain give chemical." Prestige restarts the dopamine curve and fixes "money becomes useless" (AGADAH's complaint).
7. **Automation that pays you while you do the fun thing.** Factorio ("zero grind, because everything can be automated"), Satisfactory (5.5M+), Hydroneer (conveyors as the joy), Schedule I (hire and automate, about 10M est., $151M+), Idle Miner Tycoon managers, Librarian's shelving spells. Lost Bitcoin's pitch ("a factory that works for you while you dig") sits here.
8. **Random rarity reveal plus a collection to fill.** TCG Card Shop ("Opening packs is so satisfying," 1.1-3.5M), How to Fish (rare variants, gamble the catch, 8.5M est.), Storage Hunter (547k est.), DREDGE aberrations, Bongo Cat drops (5.7M players), One Man's Trash trophy shelf, Balatro jokers. Variable reward is what makes "one more dig" compulsive.
9. **Choose 1 of 3 upgrades on level-up (build drafting).** Vampire Survivors, Megabonk (1M in 2 weeks), BALL x PIT (2M), Keep on Mining talent cards, Balatro jokers. Evidence: "just going to play one more run." It adds decisions to auto-play loops at near-zero UI cost.
10. **Cheap, absurd, one-verb premise that explains itself in a 5-second clip, playable in a sitting.** AGADAH ($5, about 2h, 14.5M Reels views), Meccha ($6, paint to hide), Needle in a Haystack (50M+ clip views), PEAK ($8, median 3h53m), How to Fish ($8, a couple of hours), Gamble With Your Friends ($8, 2-3h). For Roblox, "cheap and short" becomes free, instantly joinable, and a short round.

Honorable mentions:
- **Day/night dual loop:** gather, then sell in your own shop (Dave the Diver, Dome Keeper, Roadside Research at 774k est.).
- **The lost-fortune mystery at the bottom:** AGADAH's mystery, One Man's Trash's hard drive, Lost Bitcoin's wallet. It is a strong framing, but only One Man's Trash is proof, and it is small.

### Recurring complaints to design against

| Complaint | Games where reviewers said it | Design counter |
|---|---|---|
| Too short / abrupt end / no endgame | AGADAH, One Man's Trash, SteamWorld Dig, Keep on Mining, Content Warning, Schedule I, Lethal Company, How to Fish, DRG (end after first OC) | Endless depth ladder plus prestige/rebirth plus new biomes. No "credits." |
| Final act removes the core verb | AGADAH ("can't use your tools") | Never take the shovel away. Bosses must be dig-based. |
| Upgrades feel invisible ("+5%") / money becomes useless | One Man's Trash, AGADAH, DREDGE (late upgrades don't matter), Super Motherload (no tooltips) | Each tier changes the tool's look, sound and dig radius. Always have a money sink (prestige, cosmetics, automation). |
| Weightless digging feedback | Super Motherload, AGADAH ("no physics on anything you dig") | Particles, debris chunks, screen shake, a pitch-rising pickup chime, physics loot. |
| Horror or jumpscares the audience didn't expect | One Man's Trash worms, REPO/Lethal/PEAK difficulty creep | Spooky-cute, not scary. Make hazards readable and avoidable. |
| Devs keep making it harder | R.E.P.O., Lethal Company, PEAK | Difficulty is player-chosen (deeper equals harder). Never retro-nerf a party game. |
| Grind, backtracking, carry friction | DREDGE ("80% ... back and forth"), SteamWorld Dig, Hydroneer (one item at a time), Satisfactory (no mass placement), Dave the Diver chores | Fast-travel elevator, vacuum or bulk carry, snap/blueprint placement. QoL is an unlock reward (Supermarket's "Tablet & Scanner"). |
| Progress loss from bugs or saves | Hydroneer, House Flipper, One Man's Trash (hole refills), RV There Yet checkpoints, Cookie Clicker | Server-side DataStore saves, autosave on every sell, no terrain regen that deletes work. |
| Paywalled base content / predatory DLC / FOMO | PowerWash (60% of achievements DLC-locked), Supermarket ($47 total), House Flipper, Bongo Cat (limited items, paid pass), Mr.Mine (pay to revive) | Cosmetic-only or convenience passes. Never lock completion. Co-op guests earn full rewards. |
| RNG over agency | Mr.Mine ("gatcha"), Keep on Mining, Content Warning, Balatro ("slot machine") | Pity timers, guaranteed rare per depth tier, odds shown. |
| Lobby, griefing, hacking, moderation | WEBFISHING, PEAK, Meccha, RV There Yet, How to Fish, Lethal Company | Roblox gives matchmaking and moderation. Still add private servers, vote-kick, and protected shared assets (a shared RV, a shared hole). |
| One player carries, others idle | Content Warning ("only one person REALLY is in control"), Gamble With Your Friends ("not much co-operating") | Role-split jobs (digger, hauler, sorter, defender), each with its own upgrade track. |
| Harsh timers | Gamble With Your Friends ("5 minute timer is not fun") | Soft timers (wave or night) with an option to extend. |
| Undisclosed AI assets | TCG Card Shop, Chained Together | Hand-polish hero assets, and be transparent. |

### Five fresh genre combinations (each backed by 2+ proven hits, no dominant single game yet)

**A. Co-op quota dig ("Lethal Company, but you dig").** A 4-player crew digs a shared hole. Ore is a physics object you must haul up without breaking. Hit the day's quota at the sell station, then buy upgrades, and the quota rises.
- **Proof:** dig ladder from AGADAH (1M+), SteamWorld Dig (1M+), Dome Keeper (>500k), DRG (8M+). Quota and physics-loot friendslop from Lethal Company (~10M est.), R.E.P.O. (16.4M est.), PEAK (4.5M+).
- **Gap check:** DRG is the closest, but it is a $30 shooter with long missions. *A Game About Digging A Hole Together* launches Dec 4, 2026, and Keep Digging (77% of ~1.2k reviews) and DIG are small. Nothing dominant yet, but the window is closing.
- **Roblox fit:** high. Friends, voice, physics, short rounds.

**B. Dig plus "factory that pays you while you dig."** Active first-person digging feeds conveyors, sorters and machines that keep converting scrap into cash between sessions (offline earnings).
- **Proof:** AGADAH and One Man's Trash (dig-sell). Hydroneer (1M+ claimed, conveyor joy). Schedule I (about 10M est.; hand-craft, then automate). Satisfactory and Factorio (5.5M+ and 3.5M+). Idle Miner Tycoon (150M downloads; managers automate shafts).
- **Gap check:** Hydroneer is the closest, but reviewers cite its grind, one-item carrying and save loss. Lost Bitcoin is pitching exactly this, but it is unreleased and single-player.
- **Roblox fit:** high. The offline-earnings idle layer is a proven mobile retention lever (inference).

**C. Treasure-dig "pack opening": sealed finds plus a reveal plus a collection book.** Dig up sealed crates, safes, USB sticks and capsules with rarity tiers. Crack them open in a reveal animation, then fill a museum or trophy shelf. Duplicates sell or fuse.
- **Proof:** TCG Card Shop (pack-opening satisfaction, 1.1-3.5M). Storage Hunter (547k est., bid and dig out valuables). How to Fish (rare variants and gambling the catch, 8.5M est.). Bongo Cat (rarity drops, 5.7M players). One Man's Trash (trophy display is its most-praised addition). Balatro and Gamble With Your Friends (risk/reward).
- **Gap check:** No dominant game combines digging with a rarity-reveal collection.
- **Roblox fit:** very high, but keep paid random items within Roblox policy [UNVERIFIED current rules], and favor earned crates.

**D. Restore what you dig (excavate, clean or repair, appraise, then sell or display).** Junk comes out filthy or broken. A PowerWash-style spray or a repair minigame reveals its true value, and fully restored items are worth multiples.
- **Proof:** PowerWash (17M players, 97%), House Flipper (2.1M+ PC), ReStory (~500k in about a month), Cash Cleaner (510k est.), Car Dealer Simulator (658k est., buy-repair-flip), AGADAH and One Man's Trash for the dig.
- **Gap check:** Junkyard Simulator tried part of this and stalled (64%, "renovation minigame is lackluster"). That is an execution gap, not a demand gap.
- **Roblox fit:** high. The clean-percentage meter reads instantly on mobile.

**E. Co-op roguelite auto-dig runs (Vampire-Survivors-style drafting inside a mine).** Your drill auto-fires. You steer, pick 1 of 3 upgrades on each level-up, and race a wave or oxygen timer back to the dome. Meta-upgrades between runs. 10-15 minute runs with friends.
- **Proof:** Vampire Survivors (27M players), Megabonk (1M in 2 weeks), BALL x PIT (2M), Keep on Mining (talent cards, 91%), Dome Keeper (dig vs wave timer), DRG: Survivor (500k in its first Early Access week, a single-player version of this mix).
- **Gap check:** No dominant co-op, mobile-first, short-round version.
- **Roblox fit:** good. Note that survivors-likes draw "shallow manufactured addiction" critiques, so lean on co-op roles.

### Roblox translation rules distilled
Inferences drawn from the evidence above:
1. One verb with juicy feedback beats systems. AGADAH beat Junkyard Simulator on far less content.
2. Make the hole or the factory **visible and shared** in the server. Social proof and screenshot value come from that.
3. Sessions of 10-20 minutes with a clear loop end (a quota met, a run finished, a crate opened). Persistent progress across sessions.
4. Endless depth plus prestige replaces the Steam "2-hour ending" that reviewers hated.
5. Friends-first: role-split co-op, physics comedy, no harsh horror.
6. Monetize convenience and cosmetics. Never sell completion, and never shortchange co-op guests. Those were the most-cited review grievances.
