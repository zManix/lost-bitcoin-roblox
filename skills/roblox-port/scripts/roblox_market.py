#!/usr/bin/env python3
"""Live Roblox market data from Roblox's own public web APIs (no key needed).

Subcommands:
  search  "q1" "q2" ... [--n 8] [--json out.json] [--enrich] [--min-live N]
                                                               -> top results per query (name, live, upvotes, universeId).
                                                                  --enrich adds visits/created/favorites/like% for every unique
                                                                  game (batched) and prints a deduped table sorted by live players
  details ID [ID ...]                                          -> visits, live, favorites, created, updated, max players, description
  passes  ID [ID ...]                                          -> game pass names + Robux prices (proven price points)
  votes   ID [ID ...]                                          -> up/down votes and like ratio
  charts  [--n 12] [--sort ID]                                 -> every sort the explore API returns (front page + genre sorts when
                                                                  present); --sort filters to sort ids containing ID.
                                                                  Note: event weeks (Halloween, holidays) skew front-page sorts.
IDs are universe ids (the search output prints them). Standard library only.
"""
import argparse, json, random, string, sys, urllib.parse, urllib.request

UA = {"User-Agent": "Mozilla/5.0 roblox-port-research/1.0", "Accept": "application/json"}
SID = "".join(random.choices(string.ascii_lowercase + string.digits, k=16))


def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


def enrich(uids):
    info = {}
    uids = [str(u) for u in uids]
    for i in range(0, len(uids), 30):
        chunk = ",".join(uids[i:i + 30])
        try:
            for g in get(f"https://games.roblox.com/v1/games?universeIds={chunk}").get("data", []):
                info[str(g["id"])] = {"visits": g["visits"], "created": g["created"][:10], "fav": g["favoritedCount"],
                                      "maxP": g["maxPlayers"]}
            for v in get(f"https://games.roblox.com/v1/games/votes?universeIds={chunk}").get("data", []):
                tot = (v["upVotes"] + v["downVotes"]) or 1
                info.setdefault(str(v["id"]), {})["like"] = round(100 * v["upVotes"] / tot, 1)
        except Exception as e:  # noqa: BLE001
            print(f"enrich error: {e}")
    return info


def search(queries, n, out, do_enrich=False, min_live=0):
    allr = {}
    for q in queries:
        url = (f"https://apis.roblox.com/search-api/omni-search?searchQuery={urllib.parse.quote(q)}"
               f"&sessionId={SID}&pageType=all")
        try:
            d = get(url)
        except Exception as e:  # noqa: BLE001
            print(f"=== {q}: ERROR {e}")
            continue
        rows = []
        for r in d.get("searchResults", []):
            for c in r.get("contents", []):
                if "name" in c and "universeId" in c:
                    rows.append({"name": c.get("name"), "live": c.get("playerCount"), "up": c.get("totalUpVotes"),
                                 "down": c.get("totalDownVotes"), "universeId": c.get("universeId")})
        allr[q] = rows[:n]
        print(f"=== {q}")
        for x in rows[:n]:
            print(f"  {str(x['name'])[:56]:56} | live {x['live']} | up {x['up']} | uid {x['universeId']}")
    if do_enrich:
        uniq = {}
        for rows in allr.values():
            for x in rows:
                uniq.setdefault(str(x["universeId"]), x)
        info = enrich(list(uniq))
        table = []
        for uid, x in uniq.items():
            x.update(info.get(uid, {}))
            if (x.get("live") or 0) >= min_live:
                table.append(x)
        table.sort(key=lambda x: -(x.get("live") or 0))
        print(f"\n=== ENRICHED ({len(table)} unique games, live >= {min_live})")
        for x in table:
            print(f"  {str(x['name'])[:48]:48} | live {x.get('live')} | visits {x.get('visits', 0):,} | created "
                  f"{x.get('created')} | like {x.get('like')}% | fav {x.get('fav', 0):,} | uid {x['universeId']}")
        allr["_enriched"] = table
    if out:
        json.dump(allr, open(out, "w", encoding="utf-8"), indent=1)


def details(ids):
    for i in range(0, len(ids), 30):
        chunk = ",".join(ids[i:i + 30])
        d = get(f"https://games.roblox.com/v1/games?universeIds={chunk}")
        for g in d.get("data", []):
            print(f"### {g['name']} | uid {g['id']} | visits {g['visits']:,} | live {g['playing']:,} | fav "
                  f"{g['favoritedCount']:,} | created {g['created'][:10]} | updated {g['updated'][:10]} | maxP {g['maxPlayers']}"
                  f" | {g.get('genre_l1')}/{g.get('genre_l2')}")
            print("   ", (g.get("description") or "")[:600].replace("\n", " "))


def passes(ids):
    for u in ids:
        try:
            d = get(f"https://apis.roblox.com/game-passes/v1/universes/{u}/game-passes?passView=Full&pageSize=50")
        except Exception as e:  # noqa: BLE001
            print(f"=== {u}: ERROR {e}")
            continue
        ps = d.get("gamePasses") or d.get("data") or []
        print(f"=== universe {u}: {len(ps)} passes")
        for p in ps:
            price = p.get("price") or p.get("priceInRobux")
            if price:
                print(f"  {price:>6} R$  {p.get('name') or p.get('displayName')}")


def votes(ids):
    d = get(f"https://games.roblox.com/v1/games/votes?universeIds={','.join(ids)}")
    for v in d.get("data", []):
        tot = (v["upVotes"] + v["downVotes"]) or 1
        print(f"  uid {v['id']}: up {v['upVotes']:,} down {v['downVotes']:,} like {100 * v['upVotes'] / tot:.1f}%")


def charts(n, sort_filter=None):
    d = get(f"https://apis.roblox.com/explore-api/v1/get-sorts?sessionId={SID}&device=computer&country=all")
    for s in d.get("sorts", []):
        games = s.get("games") or []
        if not games:
            continue
        if sort_filter and sort_filter.lower() not in str(s.get("sortId", "")).lower():
            continue
        print(f"## {s.get('sortDisplayName') or s.get('sortId')}")
        for g in games[:n]:
            print(f"   {str(g.get('name'))[:50]:50} live {g.get('playerCount')} uid {g.get('universeId')}")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("search"); p.add_argument("queries", nargs="+"); p.add_argument("--n", type=int, default=8)
    p.add_argument("--json"); p.add_argument("--enrich", action="store_true"); p.add_argument("--min-live", type=int, default=0)
    for name in ("details", "passes", "votes"):
        p = sub.add_parser(name); p.add_argument("ids", nargs="+")
    p = sub.add_parser("charts"); p.add_argument("--n", type=int, default=12); p.add_argument("--sort")
    a = ap.parse_args()
    try:
        if a.cmd == "search":
            search(a.queries, a.n, a.json, a.enrich, a.min_live)
        elif a.cmd == "details":
            details(a.ids)
        elif a.cmd == "passes":
            passes(a.ids)
        elif a.cmd == "votes":
            votes(a.ids)
        else:
            charts(a.n, a.sort)
    except Exception as e:  # noqa: BLE001
        sys.exit(f"Roblox API error: {e}")


if __name__ == "__main__":
    main()
