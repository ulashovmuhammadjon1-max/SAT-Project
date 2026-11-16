#!/usr/bin/env python3
"""Mix the soundtrack straight from index.html's <audio> clips with ffmpeg (start, media-start, duration,
volume, fades), so an audio-only fix doesn't need a full video re-render.
Usage: remix.py OUT.wav [--override id=attr:value ...]"""
import re, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent
html = (ROOT / "index.html").read_text()
end = float(re.search(r'id="root"[^>]*data-duration="([0-9.]+)"', html).group(1))
over = {}
for a in sys.argv[2:]:
    k, v = a.split("=", 1); attr, val = v.split(":", 1); over.setdefault(k, {})[attr] = val
clips = []
for m in re.finditer(r"<audio ([^>]*)></audio>", html):
    at = dict(re.findall(r'([\w-]+)="([^"]*)"', m.group(1)))
    at.update(over.get(at["id"], {}))
    clips.append(at)
args, fl = ["ffmpeg", "-nostdin", "-v", "error", "-y"], []
for i, c in enumerate(clips):
    args += ["-i", str(ROOT / c["src"])]
    st, d = float(c["data-start"]), float(c["data-duration"]); ms = float(c.get("data-media-start", 0))
    ch = int(subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "a:0", "-show_entries", "stream=channels", "-of", "csv=p=0", str(ROOT / c["src"])]).decode().strip().split(",")[0])
    up = "pan=stereo|c0=c0|c1=c0" if ch == 1 else "aformat=channel_layouts=stereo"
    f = f"[{i}:a]aresample=48000,{up},atrim={ms}:{ms + d},asetpts=PTS-STARTPTS,volume={c.get('data-volume', 1)}"
    if c.get("data-fade-in"): f += f",afade=t=in:d={c['data-fade-in']}"
    if c.get("data-fade-out"): f += f",afade=t=out:st={max(0, d - float(c['data-fade-out']))}:d={c['data-fade-out']}"
    f += f",adelay={int(st * 1000)}|{int(st * 1000)}[a{i}]"
    fl.append(f)
fl.append("".join(f"[a{i}]" for i in range(len(clips))) + f"amix=inputs={len(clips)}:normalize=0:duration=longest,atrim=0:{end}[out]")
args += ["-filter_complex", ";".join(fl), "-map", "[out]", "-ar", "48000", sys.argv[1]]
subprocess.check_call(args)
print("mixed", len(clips), "clips ->", sys.argv[1])
