#!/usr/bin/env python3
"""Study gameplay videos from YouTube with yt-dlp, for private reference (Claude reads frames + captions).

Subcommands:
  search "query" [--n 15] [--json FILE]        -> id | title | channel | seconds | views (also appended to FILE as JSON lines,
                                                  so the list can go straight into STUDY.md / TODO R0)
  get ID [ID ...] --out DIR [--height 720]     -> downloads video + English auto-captions, writes ID.transcript.txt
                                                  and frame sheets every --every seconds (default 20) via frames.py
If YouTube asks to "confirm you're not a bot", this script stops and says so. Do not try to get around it: report it,
and rely on the trailers/screenshots instead (or ask the user to download a video manually).
"""
import argparse, glob, json, os, re, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))


def need_ytdlp():
    if shutil.which("yt-dlp") is None:
        sys.exit("yt-dlp missing. Install: pip install -U yt-dlp  (then open a new shell)")


def search(q, n, out=None):
    r = subprocess.run(["yt-dlp", "--flat-playlist", "-j", f"ytsearch{n}:{q}"], capture_output=True, text=True)
    if "not a bot" in r.stderr:
        sys.exit("YouTube bot check: stop here and report it (don't work around it).")
    for line in r.stdout.splitlines():
        try:
            d = json.loads(line)
        except ValueError:
            continue
        print(f"{d.get('id')} | {str(d.get('title'))[:80]} | {d.get('channel')} | {d.get('duration')} s | {d.get('view_count')}")
        if out:
            with open(out, "a", encoding="utf-8") as f:
                f.write(json.dumps({"query": q, "id": d.get("id"), "title": d.get("title"), "channel": d.get("channel"),
                                    "seconds": d.get("duration"), "views": d.get("view_count"),
                                    "url": f"https://www.youtube.com/watch?v={d.get('id')}"}) + "\n")


def vtt_to_text(path):
    out, last = [], ""
    for line in open(path, encoding="utf-8", errors="replace"):
        line = line.strip()
        if not line or "-->" in line or line.startswith(("WEBVTT", "Kind:", "Language:")) or line.isdigit():
            continue
        line = re.sub(r"<[^>]+>", "", line)
        if line != last:
            out.append(line)
            last = line
    return "\n".join(out)


def get(ids, out, height, every):
    os.makedirs(out, exist_ok=True)
    for vid in ids:
        url = f"https://www.youtube.com/watch?v={vid}"
        r = subprocess.run(["yt-dlp", "-f", f"bv*[height<={height}]+ba/b[height<={height}]", "--merge-output-format", "mp4",
                            "--write-auto-subs", "--write-subs", "--sub-langs", "en.*,en", "--sub-format", "vtt",
                            "--write-info-json", "-o", os.path.join(out, "%(id)s.%(ext)s"), url],
                           capture_output=True, text=True)
        if "not a bot" in r.stderr:
            print(f"{vid}: YouTube bot check. Skipping (don't work around it).")
            continue
        if r.returncode != 0:
            print(f"{vid}: download failed: {r.stderr[-300:]}")
            continue
        subs = sorted(glob.glob(os.path.join(out, f"{vid}*.vtt")))
        if subs:
            open(os.path.join(out, f"{vid}.transcript.txt"), "w", encoding="utf-8").write(vtt_to_text(subs[0]))
        mp4 = os.path.join(out, f"{vid}.mp4")
        if os.path.exists(mp4):
            subprocess.run([sys.executable, os.path.join(HERE, "frames.py"), "sheets", mp4, "--out",
                            os.path.join(out, f"{vid}_frames"), "--fps", str(1.0 / every), "--max", "180"])
        print(f"{vid}: done (video, transcript={'yes' if subs else 'no'}, frames)")


def main():
    need_ytdlp()
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("search"); p.add_argument("query"); p.add_argument("--n", type=int, default=15); p.add_argument("--json")
    p = sub.add_parser("get"); p.add_argument("ids", nargs="+"); p.add_argument("--out", required=True)
    p.add_argument("--height", type=int, default=720); p.add_argument("--every", type=float, default=20)
    a = ap.parse_args()
    if a.cmd == "search":
        search(a.query, a.n, a.json)
    else:
        get(a.ids, a.out, a.height, a.every)


if __name__ == "__main__":
    main()
