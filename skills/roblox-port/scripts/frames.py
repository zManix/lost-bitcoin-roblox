#!/usr/bin/env python3
"""Turn videos/images into things Claude can LOOK at (Claude can't watch video, so it reads frames).

Subcommands:
  sheets  VIDEO --out DIR [--fps 1] [--max 90]      -> frames at fps, tiled 3x3 (640x360 each), timestamps burned in
  key     VIDEO --times 12.5,40,61.2 --out DIR      -> full-resolution PNGs at exact times (for UI reading)
  strip   VIDEO --start 12.6 --dur 1.2 --fps 10 --out FILE -> one 4x3 tile of a short moment (animation timing)
  images  DIR --out DIR                              -> tile a folder of screenshots 3x3
Needs ffmpeg + ffprobe on PATH. Timestamps use drawtext; if no font is available it retries without text.
"""
import argparse, glob, os, shutil, subprocess, sys


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def dur(path):
    out = run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path]).stdout.strip()
    return float(out) if out else 0.0


def ff(args_with_text, args_plain):
    r = run(args_with_text)
    if r.returncode != 0:
        r = run(args_plain)
    if r.returncode != 0:
        print(r.stderr[-800:])
    return r.returncode == 0


def sheets(video, out, fps, maxf):
    os.makedirs(out, exist_ok=True)
    tag = os.path.splitext(os.path.basename(video))[0]
    d = dur(video)
    if maxf and d * fps > maxf:
        fps = maxf / d
    vf_t = f"fps={fps},scale=640:360,drawtext=text='{tag} %{{pts\\:hms}}':x=8:y=8:fontsize=22:fontcolor=yellow:box=1:boxcolor=black"
    vf_p = f"fps={fps},scale=640:360"
    pat = os.path.join(out, f"{tag}_%03d.jpg")
    base = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", video]
    ff(base + ["-vf", vf_t, pat], base + ["-vf", vf_p, pat])
    n = len(glob.glob(os.path.join(out, f"{tag}_[0-9][0-9][0-9].jpg")))
    run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", pat, "-vf", "tile=3x3",
         os.path.join(out, f"{tag}_sheet_%02d.jpg")])
    sheets_made = sorted(glob.glob(os.path.join(out, f"{tag}_sheet_*.jpg")))
    print(f"{video}: {d:.1f}s, {n} frames at {fps:.3f} fps -> {len(sheets_made)} sheets")
    for s in sheets_made:
        print("  ", s)


def key(video, times, out):
    os.makedirs(out, exist_ok=True)
    tag = os.path.splitext(os.path.basename(video))[0]
    for t in times:
        dst = os.path.join(out, f"{tag}_{t:07.2f}.png".replace(":", "_"))
        run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-ss", str(t), "-i", video, "-frames:v", "1", dst])
        print("  ", dst)


def strip(video, start, length, fps, out):
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    base = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-ss", str(start), "-t", str(length), "-i", video]
    vf_t = f"fps={fps},scale=480:270,drawtext=text='%{{pts\\:hms}}':x=6:y=6:fontsize=16:fontcolor=yellow:box=1:boxcolor=black,tile=4x3"
    vf_p = f"fps={fps},scale=480:270,tile=4x3"
    ff(base + ["-vf", vf_t, "-frames:v", "1", out], base + ["-vf", vf_p, "-frames:v", "1", out])
    print("  ", out)


def images(src, out):
    os.makedirs(out, exist_ok=True)
    files = sorted(f for f in glob.glob(os.path.join(src, "*")) if f.lower().endswith((".jpg", ".jpeg", ".png")))
    tmp = os.path.join(out, "_tmp"); os.makedirs(tmp, exist_ok=True)
    for i, f in enumerate(files, 1):
        run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", f, "-vf", "scale=640:360", os.path.join(tmp, f"i{i:03d}.jpg")])
    run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", os.path.join(tmp, "i%03d.jpg"), "-vf", "tile=3x3",
         os.path.join(out, "screens_sheet_%02d.jpg")])
    shutil.rmtree(tmp, ignore_errors=True)
    for s in sorted(glob.glob(os.path.join(out, "screens_sheet_*.jpg"))):
        print("  ", s)


def main():
    if not shutil.which("ffmpeg"):
        sys.exit("ffmpeg not found. Windows: winget install Gyan.FFmpeg (then open a new shell).")
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("sheets"); p.add_argument("video"); p.add_argument("--out", required=True)
    p.add_argument("--fps", type=float, default=1.0); p.add_argument("--max", type=int, default=90)
    p = sub.add_parser("key"); p.add_argument("video"); p.add_argument("--times", required=True); p.add_argument("--out", required=True)
    p = sub.add_parser("strip"); p.add_argument("video"); p.add_argument("--start", type=float, required=True)
    p.add_argument("--dur", type=float, default=1.2); p.add_argument("--fps", type=float, default=10); p.add_argument("--out", required=True)
    p = sub.add_parser("images"); p.add_argument("src"); p.add_argument("--out", required=True)
    a = ap.parse_args()
    if a.cmd == "sheets":
        sheets(a.video, a.out, a.fps, a.max)
    elif a.cmd == "key":
        key(a.video, [float(x) for x in a.times.split(",")], a.out)
    elif a.cmd == "strip":
        strip(a.video, a.start, a.dur, a.fps, a.out)
    else:
        images(a.src, a.out)


if __name__ == "__main__":
    main()
