#!/usr/bin/env python3
"""Turn videos/images into things Claude can LOOK at (Claude can't watch video, so it reads frames).

Subcommands:
  sheets  VIDEO --out DIR [--fps 1] [--max 90] [--dedupe]  -> frames at fps, tiled 3x3 (640x360 each), timestamps burned in.
                                                             --dedupe drops near-duplicate/static frames (end cards, holds)
  key     VIDEO --times 12.5,40,61.2 --out DIR             -> full-resolution PNGs at exact times (for reading UI)
  strip   VIDEO --start 12.6 --dur 1.2 --fps 10 --out FILE [--crop x,y,w,h]
                                                             -> one 4x3 tile of a short moment (animation timing);
                                                                --crop zooms into a region first (tiny sprites)
  images  DIR --out DIR                                     -> tile a folder of screenshots 3x3 (prints images -> tiles)
  palette IMAGE [--crop x,y,w,h] [--n 8]                    -> dominant colors as hex (for palette tables)
Needs ffmpeg + ffprobe on PATH. Timestamps use drawtext; if no font is available it retries without text.
"""
import argparse, glob, math, os, shutil, subprocess, sys


def run(cmd, binary=False):
    return subprocess.run(cmd, capture_output=True, text=not binary)


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


def crop_filter(crop):
    if not crop:
        return ""
    x, y, w, h = [int(v) for v in crop.split(",")]
    return f"crop={w}:{h}:{x}:{y},"


def sheets(video, out, fps, maxf, dedupe):
    os.makedirs(out, exist_ok=True)
    tag = os.path.splitext(os.path.basename(video))[0]
    d = dur(video)
    if maxf and d * fps > maxf:
        fps = maxf / d
    pre = "mpdecimate=hi=64*24:lo=64*12:frac=0.5," if dedupe else ""
    vf_t = f"{pre}fps={fps},scale=640:360,drawtext=text='{tag} %{{pts\\:hms}}':x=8:y=8:fontsize=22:fontcolor=yellow:box=1:boxcolor=black"
    vf_p = f"{pre}fps={fps},scale=640:360"
    pat = os.path.join(out, f"{tag}_%03d.jpg")
    base = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", video]
    ff(base + ["-vf", vf_t, "-fps_mode", "vfr", pat], base + ["-vf", vf_p, "-fps_mode", "vfr", pat])
    n = len(glob.glob(os.path.join(out, f"{tag}_[0-9][0-9][0-9].jpg")))
    run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", pat, "-vf", "tile=3x3",
         os.path.join(out, f"{tag}_sheet_%02d.jpg")])
    sheets_made = sorted(glob.glob(os.path.join(out, f"{tag}_sheet_*.jpg")))
    print(f"{video}: {d:.1f}s, {n} frames at {fps:.3f} fps{' (deduped)' if dedupe else ''} -> {len(sheets_made)} sheets")
    for s in sheets_made:
        print("  ", s)


def key(video, times, out):
    os.makedirs(out, exist_ok=True)
    tag = os.path.splitext(os.path.basename(video))[0]
    for t in times:
        dst = os.path.join(out, f"{tag}_{t:07.2f}.png")
        run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-ss", str(t), "-i", video, "-frames:v", "1", dst])
        print("  ", dst)


def strip(video, start, length, fps, out, crop):
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    base = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-ss", str(start), "-t", str(length), "-i", video]
    c = crop_filter(crop)
    vf_t = f"{c}fps={fps},scale=480:270,drawtext=text='%{{pts\\:hms}}':x=6:y=6:fontsize=16:fontcolor=yellow:box=1:boxcolor=black,tile=4x3"
    vf_p = f"{c}fps={fps},scale=480:270,tile=4x3"
    ff(base + ["-vf", vf_t, "-frames:v", "1", out], base + ["-vf", vf_p, "-frames:v", "1", out])
    print("  ", out)


def images(src, out):
    os.makedirs(out, exist_ok=True)
    files = sorted(f for f in glob.glob(os.path.join(src, "*")) if f.lower().endswith((".jpg", ".jpeg", ".png")))
    tmp = os.path.join(out, "_tmp"); os.makedirs(tmp, exist_ok=True)
    ok = 0
    for i, f in enumerate(files, 1):
        # Normalize size AND pixel format so mixed sources tile correctly.
        r = run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", f,
                 "-vf", "scale=640:360:force_original_aspect_ratio=decrease,pad=640:360:(ow-iw)/2:(oh-ih)/2,format=yuvj420p",
                 os.path.join(tmp, f"i{i:03d}.jpg")])
        ok += r.returncode == 0
    run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", os.path.join(tmp, "i%03d.jpg"), "-vf", "tile=3x3",
         os.path.join(out, "screens_sheet_%02d.jpg")])
    shutil.rmtree(tmp, ignore_errors=True)
    sheets_made = sorted(glob.glob(os.path.join(out, "screens_sheet_*.jpg")))
    print(f"{len(files)} images ({ok} converted) -> {len(sheets_made)} sheets ({math.ceil(len(files) / 9)} expected)")
    for s in sheets_made:
        print("  ", s)


def palette(img, crop, n):
    vf = f"{crop_filter(crop)}scale=96:54"
    r = run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", img, "-vf", vf, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
            binary=True)
    data = r.stdout
    if not data:
        sys.exit("could not read image")
    buckets = {}
    for i in range(0, len(data) - 2, 3):
        rgb = data[i:i + 3]
        k = (rgb[0] >> 4, rgb[1] >> 4, rgb[2] >> 4)
        s = buckets.setdefault(k, [0, 0, 0, 0])
        s[0] += rgb[0]; s[1] += rgb[1]; s[2] += rgb[2]; s[3] += 1
    total = len(data) // 3
    top = sorted(buckets.values(), key=lambda v: -v[3])[:n]
    for r_, g, b, c in top:
        print(f"  #{r_ // c:02X}{g // c:02X}{b // c:02X}  {100 * c / total:4.1f}%")


def main():
    if not shutil.which("ffmpeg"):
        sys.exit("ffmpeg not found. Windows: winget install Gyan.FFmpeg (then open a new shell).")
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("sheets"); p.add_argument("video"); p.add_argument("--out", required=True)
    p.add_argument("--fps", type=float, default=1.0); p.add_argument("--max", type=int, default=90)
    p.add_argument("--dedupe", action="store_true")
    p = sub.add_parser("key"); p.add_argument("video"); p.add_argument("--times", required=True); p.add_argument("--out", required=True)
    p = sub.add_parser("strip"); p.add_argument("video"); p.add_argument("--start", type=float, required=True)
    p.add_argument("--dur", type=float, default=1.2); p.add_argument("--fps", type=float, default=10)
    p.add_argument("--out", required=True); p.add_argument("--crop")
    p = sub.add_parser("images"); p.add_argument("src"); p.add_argument("--out", required=True)
    p = sub.add_parser("palette"); p.add_argument("image"); p.add_argument("--crop"); p.add_argument("--n", type=int, default=8)
    a = ap.parse_args()
    if a.cmd == "sheets":
        sheets(a.video, a.out, a.fps, a.max, a.dedupe)
    elif a.cmd == "key":
        key(a.video, [float(x) for x in a.times.split(",")], a.out)
    elif a.cmd == "strip":
        strip(a.video, a.start, a.dur, a.fps, a.out, a.crop)
    elif a.cmd == "images":
        images(a.src, a.out)
    else:
        palette(a.image, a.crop, a.n)


if __name__ == "__main__":
    main()
