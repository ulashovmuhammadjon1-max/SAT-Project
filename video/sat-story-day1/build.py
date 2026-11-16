#!/usr/bin/env python3
"""Build Day 1's timeline from the narration.

Reads assets/voice/L1..L7.wav and their word timings (assets/voice/words.json, from whisper), works out
every beat's time from them, then writes:
  - the TT block in compositions/world.html (camera cuts, phone buzz, laptop screen modes),
  - compositions/captions.html (HUD, hook, question card, countdown, reveal, chat, A/B split, follow, captions),
  - index.html (sub-compositions, voice, music, sound effects).
Run it again whenever a voice line changes; nothing else needs hand-editing.
"""
import html, json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VOICE = ROOT / "assets/voice"


def dur(p):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)]).decode())


D = {k: round(dur(VOICE / f"{k}.wav"), 3) for k in ["L1", "L2", "L3", "L4", "L5", "L6", "L7"]}
WORDS = json.loads((VOICE / "words.json").read_text())  # {"L1": [{"text":..,"start":..,"end":..}, ...]}


def word_at(line, needle, which=0):
    hits = [w for w in WORDS[line] if needle.lower() in re.sub(r"[^a-z0-9]", "", w["text"].lower())]
    if not hits:
        sys.exit(f"word {needle!r} not found in {line}: {[w['text'] for w in WORDS[line]]}")
    return hits[which]["start"]


r = lambda x: round(x, 3)
T = {}
T["L1"] = 0.05
T["s2"] = r(T["L1"] + D["L1"] + 0.1)
T["L2"] = T["s2"]
T["q"] = r(T["L2"] + D["L2"] + 0.12)
T["L3"] = r(T["q"] + 0.3)
T["cd"] = r(T["L3"] + D["L3"] + 0.15)
T["rv"] = r(T["cd"] + 3.0)
T["L4"] = r(T["rv"] + 0.05)
T["maxsaid"] = r(T["L4"] + word_at("L4", "max"))
T["wrong"] = r(T["L4"] + word_at("L4", "wrong"))
T["vol"] = r(T["L4"] + word_at("L4", "volume"))
T["ans"] = r(T["L4"] + word_at("L4", "1500"))
T["phone"] = r(T["L4"] + D["L4"] + 0.55)
T["buzz"] = r(T["phone"] + 0.1)
T["L5"] = r(T["phone"] + 0.35)
T["split"] = r(T["L5"] + D["L5"] + 0.3)
T["L6"] = r(T["split"] + 0.35)
T["follow"] = r(T["L6"] + D["L6"] + 0.45)
T["L7"] = r(T["follow"] + 0.1)
T["loop"] = r(T["L7"] + D["L7"] + 0.45)
T["end"] = r(T["loop"] + 1.4)
END = T["end"]
print("durations", D)
print("timeline", T)
assert END <= 40.0, f"too long: {END}s"

# ---------------------------------------------------------------- world.html
wp = ROOT / "compositions/world.html"
w = wp.read_text()
tt = {"s2": T["s2"], "q": T["q"], "phone": T["phone"], "buzz": T["buzz"], "split": T["split"], "follow": T["follow"], "loop": T["loop"], "end": END}
w = re.sub(r"/\*TT\*/.*?/\*TT\*/", "/*TT*/" + json.dumps(tt) + "/*TT*/", w)
w = re.sub(r'data-duration="[0-9.]+"', f'data-duration="{END}"', w)
wp.write_text(w)

# ---------------------------------------------------------------- captions (spoken words)
HOT = {"1500", "1210", "30", "everything", "cost", "cube", "wrong", "240", "96", "party", "study", "follow"}
caps = []
for line in ["L1", "L2", "L3", "L4", "L5", "L6", "L7"]:
    ws = WORDS[line]
    groups, cur = [], []
    for wd in ws:
        cur.append(wd)
        nxt = ws[ws.index(wd) + 1]["text"] if len(ws) > ws.index(wd) + 1 else ""
        nxt_is_num = bool(re.match(r"[0-9]", nxt)) or len(nxt.strip(".,?!…")) == 1
        if (len(cur) >= 3 and not nxt_is_num) or len(cur) == 4 or re.search(r"[.?!,…]$", wd["text"]):
            groups.append(cur); cur = []
    if cur:
        groups.append(cur)
    for g in groups:
        caps.append([T[line] + g[0]["start"], T[line] + g[-1]["end"], g])
for i in range(len(caps)):
    nxt = caps[i + 1][0] if i + 1 < len(caps) else END
    caps[i][1] = min(max(caps[i][1] + 0.15, caps[i][0] + 0.35), nxt - 0.02)


def cap_html(g):
    out = []
    for wd in g:
        t = html.escape(wd["text"])
        key = re.sub(r"[^a-z0-9-]", "", wd["text"].lower())
        bare = wd["text"].strip(".,?!")
        hot = (key in HOT and key not in {"a", "b", "two"}) or bare in {"A", "B"}
        out.append(f'<span class="hot">{t}</span>' if hot else t)
    return " ".join(out)


# ---------------------------------------------------------------- captions.html
BOLT = '<svg class="bolt" viewBox="0 0 24 24"><path d="M13 2L4 14h7l-1 8 9-12h-7z" fill="#ffd23f"/></svg>'
CHECK = '<svg viewBox="0 0 24 24" width="54" height="54" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12.5l5 5L20 6.5"/></svg>'
ARROW = '<svg viewBox="0 0 24 24" width="58" height="58" fill="none" stroke="#111" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4v15M5 12l7 7 7-7"/></svg>'

# cone geometry in the card's SVG (inverted cones: apex at the bottom)
APEX_Y = 452
SMALL = {"cx": 210, "h": 156, "r": 62}
BIG = {"cx": 600, "h": 390, "r": 155}


def cone_paths(c):
    top = APEX_Y - c["h"]
    body = f'M{c["cx"] - c["r"]},{top} L{c["cx"]},{APEX_Y} L{c["cx"] + c["r"]},{top}'
    return top, body


s_top, s_body = cone_paths(SMALL)
b_top, b_body = cone_paths(BIG)


def liquid(c, frac):
    hh = c["h"] * frac
    rr = c["r"] * frac
    y = APEX_Y - hh
    return f'M{c["cx"] - rr:.1f},{y:.1f} L{c["cx"]},{APEX_Y} L{c["cx"] + rr:.1f},{y:.1f} Z'


svg = f'''<svg id="cones" viewBox="0 0 860 516" width="860" height="516">
  <defs><linearGradient id="liq" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4aa8ff"/><stop offset="1" stop-color="#1f5fd1"/></linearGradient></defs>
  <path d="{liquid(SMALL, 1.0)}" fill="url(#liq)"/>
  <ellipse cx="{SMALL['cx']}" cy="{s_top}" rx="{SMALL['r']}" ry="{SMALL['r'] * 0.26:.1f}" fill="#7cc0ff"/>
  <path d="{s_body}" fill="none" stroke="#1c2433" stroke-width="7" stroke-linejoin="round"/>
  <ellipse cx="{SMALL['cx']}" cy="{s_top}" rx="{SMALL['r']}" ry="{SMALL['r'] * 0.26:.1f}" fill="none" stroke="#1c2433" stroke-width="7"/>
  <path id="bigliq" d="{liquid(BIG, 0.0001)}" fill="url(#liq)"/>
  <ellipse id="bigsurf" cx="{BIG['cx']}" cy="{APEX_Y}" rx="0" ry="0" fill="#7cc0ff"/>
  <path d="{b_body}" fill="none" stroke="#1c2433" stroke-width="7" stroke-linejoin="round"/>
  <ellipse cx="{BIG['cx']}" cy="{b_top}" rx="{BIG['r']}" ry="{BIG['r'] * 0.26:.1f}" fill="none" stroke="#1c2433" stroke-width="7"/>
  <line x1="{SMALL['cx'] - SMALL['r'] - 34}" y1="{s_top}" x2="{SMALL['cx'] - SMALL['r'] - 34}" y2="{APEX_Y}" stroke="#e32b3a" stroke-width="5"/>
  <text x="{SMALL['cx'] - SMALL['r'] - 52}" y="{(s_top + APEX_Y) / 2 + 16}" class="dim" text-anchor="end">2</text>
  <line x1="{BIG['cx'] + BIG['r'] + 34}" y1="{b_top}" x2="{BIG['cx'] + BIG['r'] + 34}" y2="{APEX_Y}" stroke="#e32b3a" stroke-width="5"/>
  <text x="{BIG['cx'] + BIG['r'] + 50}" y="{(b_top + APEX_Y) / 2 + 16}" class="dim">5</text>
  <text x="{SMALL['cx']}" y="{APEX_Y + 46}" class="vol" text-anchor="middle">96 L</text>
  <text id="bigq" x="{BIG['cx']}" y="{APEX_Y + 46}" class="vol" text-anchor="middle">? L</text>
</svg>'''

CHOICES = [("A", "240"), ("B", "600"), ("C", "1,500"), ("D", "6,000")]
choices_html = "".join(f'<div class="ch" id="ch-{l}"><b>{l})</b> {v}</div>' for l, v in CHOICES)

conf = "".join(f'<i class="cf" id="cf{i}" style="left:{(i * 97) % 1040 + 10}px;background:{["#ffd23f", "#ff4d8d", "#5ce1e6", "#7c3aed", "#4ade80"][i % 5]}"></i>' for i in range(34))

clips = []
def clip(id_, cls, start, dur_, inner, extra=""):
    clips.append(f'<div id="{id_}" class="{cls} clip" data-start="{r(start)}" data-duration="{r(dur_)}"{extra}>{inner}</div>')

hud = f'<div class="chip">DAY 1 / 30</div><div class="chip" id="hud-en">{BOLT}<span>30%</span></div><div class="chip">SCORE <span class="red">1210</span> → 1500</div>'
clip("hud", "hud", 0, END, hud)
hook = '<p>HE NEEDS <b>1500</b><br/>IN 30 DAYS</p><div class="sub"><span>YOU CONTROL HIM</span></div>'
clip("hook", "hook", 0, T["s2"], hook)
clip("short", "pill", T["s2"], T["q"] - T["s2"], '<span><span class="red">1210</span> · 290 SHORT</span>')
card = f'''<div class="card"><div class="tag">TEST 31 · MATH · QUESTION 22</div>
  <div class="ttl">Two similar cones. Heights 2 : 5.<br/>The small one holds 96 L. The big one?</div>
  {svg}
  <div id="step"><span id="step-t">VOLUME GROWS WITH THE CUBE</span></div>
  <div class="chs">{choices_html}<div id="xmark"><svg viewBox="0 0 24 24" width="120" height="120" fill="none" stroke="#e32b3a" stroke-width="3.6" stroke-linecap="round"><path d="M5 5l14 14M19 5L5 19"/></svg></div><div id="maxtag">MAX</div><div id="ring"></div></div>
  <div class="src">From Test 31 · free on scholarly.space</div></div>'''
clip("qcard", "qcard", T["q"], T["phone"] - T["q"] + 0.05, card)
clip("cd", "cd", T["cd"], 3.0, '<div class="ring"><span id="cd-n">3</span></div><div class="cdt">SOLVE IT BEFORE MAX</div>')
chat = '<div class="notif"><div class="av">A</div><div><div class="nm">Aziz <small>now</small></div><div class="msg">party at mine TOMORROW. u in??</div></div></div>'
clip("chat", "chat", T["buzz"] + 0.15, T["split"] - T["buzz"] - 0.15, chat)
party = f'''<div class="party"><div class="blob b1"></div><div class="blob b2"></div><div class="blob b3"></div>{conf}
  <div class="opt"><div class="let">A</div><div class="nmw">PARTY</div><div class="why">{BOLT}+50% energy · but he loses a night</div></div></div>'''
clip("pA", "pA", T["split"], T["follow"] - T["split"], party)
clip("band", "band", T["split"], T["follow"] - T["split"], f'<div class="bd"><span class="cta">COMMENT A OR B {ARROW}</span><span class="dec">THE TOP ANSWER DECIDES DAY 2</span></div>')
clip("pB", "pB", T["split"], T["follow"] - T["split"], f'<div class="opt"><div class="let">B</div><div><div class="nmw">STUDY</div><div class="why">practice test #2 · {BOLT}−20% energy</div></div></div>')
clip("fol", "pill", T["follow"], T["loop"] - T["follow"], '<span class="fol">FOLLOW FOR DAY 2</span>')
clip("hook2", "hook", T["loop"], END - T["loop"], hook)

for i, (a, b, g) in enumerate(caps):
    clips.append(f'<div id="cap{i}" class="cap clip" data-start="{r(a)}" data-duration="{r(b - a)}"><p>{cap_html(g)}</p></div>')

# step targets for the big cone: 96 (fills 2/5 of the height), then x2.5 three times
steps = [(0.4, "96 L = THE SMALL CONE"), ((240 / 1500) ** (1 / 3), "× 2.5 HEIGHT → 240"), ((600 / 1500) ** (1 / 3), "× 2.5 WIDTH → 600"), (1.0, "× 2.5 DEPTH → 1,500")]
st0, st1 = T["vol"], T["ans"]
span = max(1.2, st1 - st0)
step_times = [st0 + span * k / 3 for k in range(4)]

js = []
A = js.append
A('const tl = gsap.timeline({ paused: true });')
A('const big = document.getElementById("bigliq"), surf = document.getElementById("bigsurf");')
A(f'const BIG = {json.dumps(BIG)}, APEX = {APEX_Y};')
A('const lv = { f: 0.0001 };')
A('const drawBig = () => { const hh = BIG.h * lv.f, rr = BIG.r * lv.f, y = APEX - hh; big.setAttribute("d", `M${BIG.cx - rr},${y} L${BIG.cx},${APEX} L${BIG.cx + rr},${y} Z`); surf.setAttribute("cy", y); surf.setAttribute("rx", rr); surf.setAttribute("ry", rr * 0.26); };')
A('drawBig();')
A('tl.fromTo("#hook p", { scale: 1.06 }, { scale: 1, duration: 0.5, ease: "power3.out" }, 0);')
A(f'tl.fromTo("#hook .sub span", {{ scale: 1 }}, {{ scale: 1.1, duration: 0.14, yoyo: true, repeat: 1, ease: "power2.out", immediateRender: false }}, {r(T["s2"] - 0.9)});')
A(f'tl.fromTo("#short span", {{ scale: 0.5, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.25, ease: "back.out(2.6)" }}, {T["s2"]});')
A(f'tl.fromTo("#qcard .card", {{ y: 120, opacity: 0, scale: 0.94 }}, {{ y: 0, opacity: 1, scale: 1, duration: 0.35, ease: "back.out(1.6)" }}, {T["q"]});')
A(f'tl.to("#qcard .card", {{ y: -80, opacity: 0, duration: 0.25, ease: "power2.in" }}, {r(T["phone"] - 0.2)});')
A(f'tl.fromTo("#cd .ring", {{ scale: 0.4, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.25, ease: "back.out(2.4)" }}, {T["cd"]});')
A(f'tl.fromTo("#cd .cdt", {{ y: 24, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.25, ease: "power3.out" }}, {r(T["cd"] + 0.05)});')
A('const cdn = document.getElementById("cd-n"), cv = { v: 0 };')
A(f'tl.fromTo(cv, {{ v: 0 }}, {{ v: 3, duration: 3.0, ease: "none", onUpdate: () => {{ cdn.textContent = String(Math.max(1, 3 - Math.floor(cv.v))); }} }}, {T["cd"]});')
A(f'[{r(T["cd"] + 1)}, {r(T["cd"] + 2)}].forEach((at) => tl.fromTo("#cd .ring", {{ scale: 1.15 }}, {{ scale: 1, duration: 0.25, ease: "power2.out", immediateRender: false }}, at));')
A(f'tl.fromTo("#maxtag", {{ opacity: 0, x: -30 }}, {{ opacity: 1, x: 0, duration: 0.2, ease: "power3.out" }}, {T["maxsaid"]});')
A(f'tl.fromTo("#xmark", {{ scale: 2.2, opacity: 0, rotation: -20 }}, {{ scale: 1, opacity: 1, rotation: 0, duration: 0.22, ease: "back.out(2.2)" }}, {T["wrong"]});')
A(f'tl.to("#ch-A", {{ backgroundColor: "#fde2e4", color: "#b3121f", duration: 0.15 }}, {T["wrong"]});')
A(f'tl.fromTo("#step", {{ opacity: 0, y: 16 }}, {{ opacity: 1, y: 0, duration: 0.2, ease: "power3.out" }}, {r(T["vol"] - 0.05)});')
bigq = ["96 L", "240 L", "600 L", "1,500 L"]
for k, (f, label) in enumerate(steps):
    at = r(step_times[k])
    A(f'tl.to(lv, {{ f: {f:.4f}, duration: 0.35, ease: "power2.out", onUpdate: drawBig }}, {at});')
    A(f'tl.call(() => {{ document.getElementById("step-t").textContent = {json.dumps(label)}; document.getElementById("bigq").textContent = {json.dumps(bigq[k])}; }}, null, {at});')
    A(f'tl.fromTo("#step span", {{ scale: 1.12 }}, {{ scale: 1, duration: 0.2, ease: "power2.out", immediateRender: false }}, {at});')
A(f'tl.call(() => {{ document.getElementById("step-t").textContent = "VOLUME GROWS WITH THE CUBE"; document.getElementById("bigq").textContent = "? L"; }}, null, {r(T["vol"] - 0.06)});')
A(f'tl.fromTo("#ring", {{ opacity: 0, scale: 0.6 }}, {{ opacity: 1, scale: 1, duration: 0.3, ease: "back.out(2.4)" }}, {r(T["ans"] + 0.05)});')
A(f'tl.to("#ch-C", {{ backgroundColor: "#dcfce7", color: "#0f6b33", duration: 0.15 }}, {r(T["ans"] + 0.05)});')
A(f'tl.fromTo("#chat .notif", {{ y: -80, opacity: 0, scale: 0.9 }}, {{ y: 0, opacity: 1, scale: 1, duration: 0.3, ease: "back.out(1.8)" }}, {r(T["buzz"] + 0.15)});')
A(f'[0, 0.6, 1.6].forEach((d) => tl.fromTo("#chat .notif", {{ x: -10 }}, {{ x: 0, duration: 0.4, ease: "elastic.out(1.2, 0.2)", immediateRender: false }}, {r(T["buzz"] + 0.2)} + d));')
A(f'[0, 0.5, 1.0, 1.5].forEach((d) => tl.fromTo("#hud-en", {{ backgroundColor: "rgba(227,43,58,0.95)", scale: 1.12 }}, {{ backgroundColor: "rgba(10,12,22,0.78)", scale: 1, duration: 0.45, ease: "power2.out", immediateRender: false }}, {r(T["buzz"] + 0.6)} + d));')
A(f'tl.fromTo("#pA .party", {{ yPercent: -100 }}, {{ yPercent: 0, duration: 0.35, ease: "power3.out" }}, {T["split"]});')
A(f'tl.fromTo("#band .bd", {{ scaleX: 0 }}, {{ scaleX: 1, duration: 0.3, ease: "power3.out" }}, {r(T["split"] + 0.2)});')
A(f'tl.fromTo("#pB .opt", {{ x: 200, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.3, ease: "back.out(1.6)" }}, {r(T["split"] + 0.3)});')
A(f'tl.fromTo("#band .cta", {{ scale: 1 }}, {{ scale: 1.08, duration: 0.3, yoyo: true, repeat: 5, ease: "sine.inOut", immediateRender: false }}, {r(T["L6"] + 1.3)});')
SD = r(T["follow"] - T["split"])
A(f'tl.fromTo(".b1", {{ x: -200, y: 80 }}, {{ x: 380, y: 260, duration: {SD}, ease: "sine.inOut" }}, {T["split"]});')
A(f'tl.fromTo(".b2", {{ x: 700, y: 300 }}, {{ x: 120, y: 60, duration: {SD}, ease: "sine.inOut" }}, {T["split"]});')
A(f'tl.fromTo(".b3", {{ x: 300, y: 520 }}, {{ x: 760, y: 420, duration: {SD}, ease: "sine.inOut" }}, {T["split"]});')
for i in range(34):
    A(f'tl.fromTo("#cf{i}", {{ y: {-60 - (i * 53) % 400}, rotation: {(i * 37) % 180} }}, {{ y: 980, rotation: {(i * 37) % 180 + 540}, duration: {2.6 + (i % 5) * 0.5}, ease: "none", repeat: 3 }}, {r(T["split"] + (i % 7) * 0.2)});')
A(f'tl.fromTo("#fol .fol", {{ scale: 0.5, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.3, ease: "back.out(2.6)" }}, {T["follow"]});')
A(f'tl.fromTo("#fol .fol", {{ scale: 1 }}, {{ scale: 1.08, duration: 0.25, yoyo: true, repeat: 3, ease: "sine.inOut", immediateRender: false }}, {r(T["follow"] + 0.5)});')
for i, (a, b, g) in enumerate(caps):
    A(f'tl.fromTo("#cap{i} p", {{ scale: 0.75, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.12, ease: "back.out(2.5)" }}, {r(a)});')
A('window.__timelines["captions"] = tl;')

css = (ROOT / "captions.css").read_text()
cap_doc = f'''<template>
  <style>
{css}
  </style>
  <div id="root" data-composition-id="captions" data-width="1080" data-height="1920">
    {chr(10).join("    " + c for c in clips).strip()}
  </div>
  <script>
    (function () {{
      {chr(10).join("      " + l for l in js).strip()}
    }})();
  </script>
</template>
'''
(ROOT / "compositions/captions.html").write_text(cap_doc)

# ---------------------------------------------------------------- index.html
aud = []
def audio(id_, src, start, d, vol, extra="", track=10):
    aud.append(f'<audio id="{id_}" class="clip" src="{src}" data-start="{r(start)}" data-duration="{r(d)}" data-volume="{vol}" data-track-index="{track}"{extra}></audio>')

for k in ["L1", "L2", "L3", "L4", "L5", "L6", "L7"]:
    audio("vo-" + k, f"assets/voice/{k}.wav", T[k], D[k], 1.2, track=10 + int(k[1]) % 2)
audio("mus0", "assets/sfx/music.mp3", 0, T["cd"], 0.13, ' data-media-start="0"', 8)
audio("mus1", "assets/sfx/music.mp3", T["cd"], 3.0, 0.3, f' data-media-start="{T["cd"]}" data-fade-in="0.2" data-fade-out="0.2"', 8)
audio("mus2", "assets/sfx/music.mp3", T["rv"], END - T["rv"], 0.13, f' data-media-start="{T["rv"]}" data-fade-out="1.0"', 8)
audio("sfx-intro", "assets/sfx/whoosh.mp3", 0, 1.3, 0.28, ' data-media-start="0.5"', 16)
for i, at in enumerate([T["q"], T["phone"], T["split"], T["follow"], T["loop"]]):
    audio(f"sfx-wh{i}", "assets/sfx/whoosh.mp3", at - 0.72, 2.0, 0.24, "", 17 + i % 2)
audio("sfx-tick", "assets/sfx/tick.mp3", T["cd"], 3.0, 3.6, ' data-fade-out="0.15"', 12)
audio("sfx-buzz", "assets/sfx/buzz.mp3", T["wrong"], 0.3, 0.2, "", 13)
audio("sfx-ding", "assets/sfx/ding.mp3", T["ans"] + 0.05, 0.36, 1.0, "", 13)
audio("sfx-vib", "assets/sfx/vibrate.wav", T["buzz"], 1.2, 0.9, "", 14)
audio("sfx-vib2", "assets/sfx/vibrate.wav", T["buzz"] + 1.6, 0.6, 0.8, "", 15)

idx = f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
    <style>
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ margin: 0; width: 1080px; height: 1920px; overflow: hidden; background: #000; }}
      #root {{ position: relative; width: 1080px; height: 1920px; background: #000; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{END}" data-width="1080" data-height="1920">
      <div id="world" data-composition-id="world" data-composition-src="compositions/world.html"
        data-start="0" data-duration="{END}" data-track-index="1" data-track-kind="graphics" data-width="1080" data-height="1920"></div>
      <div id="captions" data-composition-id="captions" data-composition-src="compositions/captions.html"
        data-start="0" data-duration="{END}" data-track-index="2" data-track-kind="captions" data-width="1080" data-height="1920" style="z-index:2"></div>
      {chr(10).join("      " + a for a in aud).strip()}
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      window.__timelines["main"] = gsap.timeline({{ paused: true }});
    </script>
  </body>
</html>
'''
(ROOT / "index.html").write_text(idx)
(ROOT / "timeline.json").write_text(json.dumps({"durations": D, "timeline": T, "end": END}, indent=1))
print("end", END)
