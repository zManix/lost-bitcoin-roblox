#!/usr/bin/env python3
"""Fetch everything public about a Steam game: details, description, screenshots, trailers, store clips, reviews.

Usage:
  python steam_fetch.py <steam URL | app id | game name> --out <dir>

Writes into <dir>:
  app.json, summary.md, description.txt, screenshots/sNN.jpg, trailers/tN.mp4 (needs ffmpeg),
  extras/xN.mp4 (gif-style clips from the description; may include promos/other games: skim first), reviews_*.json (if the API answers),
  REVIEW_PAGES.txt (community review URLs to read with WebFetch).
Standard library only (+ ffmpeg/ffprobe on PATH for trailers).
"""
import argparse, html, json, os, re, shutil, subprocess, sys, urllib.parse, urllib.request

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) roblox-port-research/1.0"}


def get(url, binary=False, timeout=60):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        data = r.read()
        ctype = r.headers.get("Content-Type", "")
    return data if binary else (data.decode("utf-8", "replace"), ctype)


def resolve_appid(arg):
    m = re.search(r"/app/(\d+)", arg)
    if m:
        return m.group(1)
    if arg.isdigit():
        return arg
    q = urllib.parse.quote(arg)
    text, _ = get(f"https://store.steampowered.com/api/storesearch/?term={q}&cc=us&l=en")
    items = json.loads(text).get("items", [])
    if not items:
        sys.exit(f"No Steam game found for '{arg}'. Pass the store URL instead.")
    print("Search matches:")
    for it in items[:5]:
        print(f"  {it['id']}  {it['name']}")
    return str(items[0]["id"])


def strip_html(s):
    s = re.sub(r"<br\s*/?>|</p>|</li>|</h\d>", "\n", s or "")
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    return re.sub(r"[ \t]+", " ", re.sub(r"\n\s*\n+", "\n\n", s)).strip()


def have(tool):
    return shutil.which(tool) is not None


def ffmpeg_copy(src, dst):
    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", src, "-c", "copy", dst]
    try:
        subprocess.run(cmd, check=True, timeout=900)
        return True
    except Exception as e:  # noqa: BLE001
        print(f"  ffmpeg failed for {dst}: {e}")
        return False


def duration(path):
    try:
        out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
                             capture_output=True, text=True, timeout=60).stdout.strip()
        return float(out)
    except Exception:  # noqa: BLE001
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("game")
    ap.add_argument("--out", required=True)
    ap.add_argument("--no-video", action="store_true")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)

    appid = resolve_appid(a.game)
    text, _ = get(f"https://store.steampowered.com/api/appdetails?appids={appid}&cc=us&l=en")
    blob = json.loads(text)[appid]
    if not blob.get("success"):
        sys.exit(f"Steam returned no data for app {appid}.")
    d = blob["data"]
    json.dump(d, open(os.path.join(a.out, "app.json"), "w", encoding="utf-8"), indent=1)
    desc = strip_html(d.get("detailed_description", ""))
    open(os.path.join(a.out, "description.txt"), "w", encoding="utf-8").write(desc)

    rel = d.get("release_date", {})
    lines = [f"# {d.get('name')} (Steam app {appid})", "",
             f"- Store: https://store.steampowered.com/app/{appid}/",
             f"- Developer: {', '.join(d.get('developers', []))} | Publisher: {', '.join(d.get('publishers', []))}",
             f"- Release: {rel.get('date')} (coming soon: {rel.get('coming_soon')})",
             f"- Price: {(d.get('price_overview') or {}).get('final_formatted', 'n/a')} | Free: {d.get('is_free')}",
             f"- Genres: {', '.join(g['description'] for g in d.get('genres', []))}",
             f"- Categories: {', '.join(c['description'] for c in d.get('categories', []))}",
             f"- Recommendations: {(d.get('recommendations') or {}).get('total', 'n/a')}",
             f"- Metacritic: {(d.get('metacritic') or {}).get('score', 'n/a')}",
             f"- Demo: {d.get('demos')}",
             f"- Website: {d.get('website')} | Support: {(d.get('support_info') or {}).get('url')}",
             f"- Short description: {d.get('short_description')}",
             f"- Trailers: {[m.get('name') for m in d.get('movies', [])]}",
             f"- Screenshots: {len(d.get('screenshots', []))}",
             f"- AI content note: {d.get('ai_content_disclosure') or 'see description/notes'}", ""]
    open(os.path.join(a.out, "summary.md"), "w", encoding="utf-8").write("\n".join(lines))
    print("\n".join(lines))

    sdir = os.path.join(a.out, "screenshots"); os.makedirs(sdir, exist_ok=True)
    for i, s in enumerate(d.get("screenshots", []), 1):
        try:
            open(os.path.join(sdir, f"s{i:02d}.jpg"), "wb").write(get(s["path_full"], binary=True))
        except Exception as e:  # noqa: BLE001
            print(f"  screenshot {i} failed: {e}")
    print(f"Saved {len(os.listdir(sdir))} screenshots -> {sdir}")

    if not a.no_video:
        if not have("ffmpeg"):
            print("ffmpeg not found: trailers skipped. Install it (Windows: winget install Gyan.FFmpeg) and rerun.")
        else:
            tdir = os.path.join(a.out, "trailers"); os.makedirs(tdir, exist_ok=True)
            for i, m in enumerate(d.get("movies", []), 1):
                src = m.get("hls_h264") or m.get("dash_h264") or (m.get("mp4") or {}).get("max")
                if not src:
                    continue
                dst = os.path.join(tdir, f"t{i}.mp4")
                if ffmpeg_copy(src, dst):
                    print(f"  trailer t{i} '{m.get('name')}' {duration(dst)} s")
            edir = os.path.join(a.out, "extras"); os.makedirs(edir, exist_ok=True)
            clips = sorted(set(re.findall(r'(https?://[^"\s]+?\.mp4[^"\s]*)', d.get("detailed_description", ""))))
            for i, u in enumerate(clips, 1):
                try:
                    open(os.path.join(edir, f"x{i}.mp4"), "wb").write(get(u, binary=True))
                except Exception as e:  # noqa: BLE001
                    print(f"  clip {i} failed: {e}")
            print(f"Saved {len(clips)} store clips -> {edir}")

    for kind in ("negative", "positive"):
        saved = False
        for flt in ("all", "recent"):
            try:
                t, ctype = get(f"https://store.steampowered.com/appreviews/{appid}?json=1&filter={flt}&review_type={kind}"
                               f"&num_per_page=50&language=english&purchase_type=all&cc=us&l=english")
                if "json" in ctype or t.strip().startswith("{"):
                    open(os.path.join(a.out, f"reviews_{kind}.json"), "w", encoding="utf-8").write(t)
                    print(f"Saved reviews_{kind}.json (filter={flt})")
                    saved = True
                    break
            except Exception as e:  # noqa: BLE001
                print(f"Reviews API failed ({kind}, {flt}): {e}")
        if not saved:
            print(f"Reviews API gave no JSON for {kind} (common; region redirect). Use REVIEW_PAGES.txt with WebFetch.")
    open(os.path.join(a.out, "REVIEW_PAGES.txt"), "w").write(
        f"https://steamcommunity.com/app/{appid}/negativereviews/?browsefilter=toprated&filterLanguage=english\n"
        f"https://steamcommunity.com/app/{appid}/positivereviews/?browsefilter=toprated&filterLanguage=english\n"
        f"https://steamcommunity.com/app/{appid}/discussions/\n"
        f"https://store.steampowered.com/news/app/{appid}\n")
    print(f"APPID={appid}")


if __name__ == "__main__":
    main()
