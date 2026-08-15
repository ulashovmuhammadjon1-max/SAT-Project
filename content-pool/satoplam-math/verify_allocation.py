# -*- coding: utf-8 -*-
"""Gate the allocation before anything is written to a database.

    python3 verify_allocation.py

Exits non-zero on any ERROR. Everything checked here has been shipped broken
at least once on this project, which is why each check exists rather than
being assumed.
"""
import json, os, re, sys
from collections import Counter

import sim

HERE = os.path.dirname(os.path.abspath(__file__))
tests = json.load(open(f"{HERE}/allocation.json"))

errors, warnings = [], []


def err(m): errors.append(m)
def warn(m): warnings.append(m)


# --- structure -------------------------------------------------------------
seen = {}
for t in tests:
    for mod, m in t["modules"].items():
        qs = m["questions"]
        where = f"{t['title']} {mod}"
        if len(qs) != 22:
            err(f"{where}: {len(qs)} questions, expected 22")
        fr = sum(1 for q in qs if not q.get("choices"))
        if fr > 5:
            err(f"{where}: {fr} free-response, cap is 5")
        for q in qs:
            if q["id"] in seen:
                err(f"{q['id']} appears in both {seen[q['id']]} and {where}")
            seen[q["id"]] = where
            if mod == "M2E" and q["id"].startswith("sathard"):
                err(f"{where}: Hard Book question {q['id']} in Module 2 Easy")

# --- every question is answerable and explained ----------------------------
for t in tests:
    for mod, m in t["modules"].items():
        for q in m["questions"]:
            lab, val = q.get("answerLabel"), q.get("answerValue")
            if not lab and val in (None, ""):
                err(f"{q['id']}: no answer")
            if lab and not any(c["label"] == lab for c in q.get("choices") or []):
                err(f"{q['id']}: keyed {lab} but no such choice")
            if q.get("choices") and val:
                err(f"{q['id']}: has both choices and a free-response answer")
            if not (q.get("whyCorrect") or "").strip():
                err(f"{q['id']}: no explanation")
            if q.get("choices"):
                labels = [c["label"] for c in q["choices"]]
                if labels != ["A", "B", "C", "D"]:
                    err(f"{q['id']}: choice labels {labels}")
                bodies = [re.sub(r"\s+", " ", c["content"]).strip() for c in q["choices"]]
                if len(set(bodies)) != 4:
                    err(f"{q['id']}: duplicate answer choices")

# --- co-visibility ---------------------------------------------------------
# A student sits Module 1 plus ONE Module 2 branch, so these are the pairings
# that can be met in a single sitting. M2E against M2H is not one of them.
COVIS = [("M1", "M1"), ("M2E", "M2E"), ("M2H", "M2H"),
         ("M1", "M2E"), ("M1", "M2H")]
worst = []
for t in tests:
    sig = {q["id"]: sim.sig(q)
           for m in t["modules"].values() for q in m["questions"]}
    for a, b in COVIS:
        qa = t["modules"][a]["questions"]
        qb = t["modules"][b]["questions"]
        for i, x in enumerate(qa):
            for j, y in enumerate(qb):
                if a == b and j <= i:
                    continue
                s = sim.score(sig[x["id"]], sig[y["id"]])[0]
                if s >= 0.35:
                    err(f"{t['title']}: {a} {x['id']} vs {b} {y['id']} score {s:.2f}")
                worst.append((s, t["title"], x["id"], y["id"]))
worst.sort(reverse=True)

# --- house style, the checks CLAUDE.md records ----------------------------
IMG = re.compile(r"<img[^>]*>", re.I)
MATHSPAN = re.compile(r"\\\((.*?)\\\)|\\\[(.*?)\\\]", re.S)


def outside_math(html):
    """The text with every math span removed, so a check cannot fire inside one."""
    return MATHSPAN.sub(" ", IMG.sub(" ", html or ""))


BAD = [
    (re.compile(r"\^"),                       "caret exponent outside math"),
    (re.compile(r"sqrt\s*\("),                "sqrt( outside math"),
    (re.compile(r"\d\s*\*\s*\w|\w\s*\*\s*\d"), "asterisk multiply outside math"),
    (re.compile(r"(?<![\d/])\d+\s*/\s*\d+(?![\d/])"), "slash fraction outside math"),
    (re.compile(r"!=|<=|>="),                 "ASCII comparison outside math"),
    (re.compile(r"\\[a-zA-Z]+"),              "LaTeX macro outside math"),
    (re.compile(r"(?<![A-Za-z])(sin|cos|tan|log)\s*\("), "bare function outside math"),
    (re.compile(r"(?<![A-Za-z])(pi|theta|alpha|beta)(?![A-Za-z])"), "Greek spelled out"),
    (re.compile(r"\$(?=\D)"),                 "TeX dollar math"),
    (re.compile(r"(?<!\*)\*(?!\*)"),          "stray markdown asterisk"),
]

NOUN = r"(?:table|graph|figure|chart|plot|scatterplot|diagram|histogram|number line)"
VISUAL = re.compile(
    rf"(?:{NOUN}\s+(?:above|below|shown|shows|is shown|displayed)"      # "figure shown"
    rf"|(?:shown|given|following)\s+{NOUN}"                              # "the given table"
    rf"|{NOUN}\s+\w{{0,12}}\s*(?:above|below)\b"                         # "table on page above"
    rf"|Note:\s*Figure"                                                  # the book's own caption
    rf"|(?:according to|based on)\s+the\s+{NOUN})", re.I)


for t in tests:
    for mod, m in t["modules"].items():
        for q in m["questions"]:
            parts = [q["stem"]] + [c["content"] for c in q.get("choices") or []]
            for part in parts:
                bare = outside_math(part)
                for pat, why in BAD:
                    hit = pat.search(bare)
                    if hit:
                        warn(f"{q['id']}: {why} -> {hit.group(0)!r}")
            # A stem promising a PRINTED visual must carry one. The naive
            # version of this check looked for the bare words table/graph/
            # figure/shown and fired on 110 sound questions: "the graph of
            # y = f(x) passes through (-3, 0)" names a mathematical object,
            # not a picture, and every coordinate-geometry question says it.
            # The discriminator is the visual noun bound to a deictic cue.
            # The visual can also live in the CHOICES: "for which of the
            # following tables are all the values solutions" prints four
            # tables as the options and none in the stem.
            if VISUAL.search(re.sub(r"<[^>]+>", " ", q["stem"])):
                has = ("<table" in q["stem"] or q.get("imageUrl")
                       or any("<table" in c["content"] for c in q.get("choices") or []))
                if not has:
                    err(f"{q['id']}: stem promises a printed visual, has neither table nor image")

print(f"tests {len(tests)}   questions {sum(len(m['questions']) for t in tests for m in t['modules'].values())}")
print(f"highest co-visible similarity: {worst[0][0]:.2f} "
      f"({worst[0][1]} {worst[0][2]} / {worst[0][3]})" if worst else "")

if warnings:
    c = Counter(w.split(": ", 1)[1].split(" ->")[0] for w in warnings)
    print(f"\nWARNINGS {len(warnings)}:")
    for k, v in c.most_common():
        print(f"  {v:4}  {k}")
    for w in warnings[:12]:
        print("   " + w[:150])

print(f"\nERRORS {len(errors)}")
for e in errors[:40]:
    print("  " + e[:160])

sys.exit(1 if errors else 0)
