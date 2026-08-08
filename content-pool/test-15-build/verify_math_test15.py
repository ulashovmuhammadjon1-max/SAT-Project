#!/usr/bin/env python3
"""
Verify the 66 originally-authored Math questions for Test 15.

Four passes, because each has caught a different class of defect in earlier
builds:

 1. Answers are re-derived with sympy from the question itself, never read off
    the `check` note. A wrong `check` and a wrong key agree with each other;
    only an independent derivation catches that.
 2. House style is enforced on the final HTML — the Test 1/2 rules in
    CLAUDE.md, plus the DB-wide rendering checks (no bare `^`, `sqrt(`,
    `*`-as-multiply, slash fractions or LaTeX macros outside a math span).
 3. Template dedupe against every Math stem live in production, not just exact
    duplicates: a question that reuses a template with new numbers is a repeat.
 4. Cross-check against the sibling Test 13 and Test 14 builds, which the
    production pass cannot see because those tests are not shipped yet. Both
    are read strictly read-only.

Run:  DATABASE_URL='postgresql://...' python3 verify_math_test15.py
      (without DATABASE_URL it verifies everything except the dedupe pass)
"""
import json
import os
import re
import subprocess
import sys
from collections import Counter

from sympy import (Eq, Rational, S, solve, sqrt, symbols, simplify, sympify,
                   pi, sin, tan, expand, cancel, log)

from math_test15 import MODULE_1, MODULE_2_EASY, MODULE_2_HARD, ALL

HERE = os.path.dirname(os.path.abspath(__file__))
x, y, k, b, c, n, t, v, s = symbols("x y k b c n t v s")
w, m, p, g, a, d, u, h, F = symbols("w m p g a d u h F")
r = symbols("r")
B_POS = symbols("b", positive=True)
FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)


# ---------------------------------------------------------------- derivations
def h1_01():
    sol = solve([Eq(5 * r + 2 * b, 76), Eq(3 * r + 4 * b, 68)], [r, b])
    return sol[b]


def h1_04():
    bikes = solve(Eq(b + (2 * b + 3), 78), b)[0]
    return 2 * bikes + 3


def h1_05():
    sol = solve([Eq(u + 7 * m, 332), Eq(u + 12 * m, 532)], [u, m])
    return sol[u]


def h1_07():
    sol = solve([Eq(a + 45 * k, 1140), Eq(a + 70 * k, 1740)], [a, k])
    return sol[a] + 100 * sol[k]


def h2h_02():
    sol = solve([Eq(-k + b, 11), Eq(5 * k + b, -7)], [k, b])
    return 9 * sol[k] + sol[b]


def h2h_05():
    rate = solve(Eq(95 + m * (130 - 40), 455), m)[0]
    return 95 + rate * (200 - 40)


def h2h_06():
    sol = solve([Eq(3 * a + 5 * c, 41), Eq(5 * a + 3 * c, 47)], [a, c])
    return sol[a] + sol[c]


def h2h_11():
    wid = [z for z in solve(Eq(w * (w + 7), 330), w) if z > 0][0]
    return 2 * (wid + (wid + 7))


def h2h_13():
    const = solve(Eq(Rational(1, 50) * (0 - 30) ** 2 + c, 20), c)[0]
    return Rational(1, 50) * (50 - 30) ** 2 + const


DERIVE = {
 "H1-01": h1_01,
 "H1-02": lambda: 1985 + solve(Eq(412 + Rational(445 - 412, 30) * t, 500), t)[0],
 "H1-03": lambda: max(i for i in range(500) if 265 + 74 * i <= 1150),
 "H1-04": h1_04,
 "H1-05": h1_05,
 "H1-06": lambda: Rational(1764, 38 + 46),
 "H1-07": h1_07,
 "H1-08": lambda: cancel((6 * x ** 2 - 7 * x - 20) / (3 * x + 4)),
 "H1-09": lambda: Rational(192, 2 * 8),
 "H1-10": lambda: simplify(log(Rational(6250, 2), 5)),
 "H1-11": lambda: sum(solve(Eq(x ** 2 + 4 * x - 7, 6 * x + 8), x)),
 "H1-12": lambda: solve(Eq(F, (5 * g - 8) / 3), g)[0],
 "H1-13": lambda: 5 - Rational(12 ** 2, 4 * 3),
 "H1-14": lambda: round(float(12500 * 0.82 ** 3)),
 "H1-15": lambda: Rational(21, 3) * 8 * Rational(13, 2),
 "H1-16": lambda: Rational(85 * 140, 100),
 "H1-17": lambda: (250 * Rational(8, 100) + 180 * Rational(5, 100)
                   + 320 * Rational(10, 100) + 150 * Rational(4, 100)),
 "H1-18": lambda: Rational(12 * 525 - 8 * 450, 100 * 4),
 "H1-19": lambda: 3 * solve(Eq(40 + 3 * t + t, 180), t)[0],
 "H1-20": lambda: simplify(12 / sin(pi / 3)),
 "H1-21": lambda: 350 * 3 ** 3,
 "H1-22": lambda: Rational(27 * 1000, 1800),

 "H2E-01": lambda: solve(Eq(5 * x - 13, 42), x)[0],
 "H2E-02": lambda: solve(Eq(4 * 5 + 9 * k, 65), k)[0],
 "H2E-03": lambda: 260 - 3 * d,
 "H2E-04": lambda: "fixed charge on every journey",
 "H2E-05": lambda: "no more than 40",
 "H2E-06": lambda: 3 * 42,
 "H2E-07": lambda: 30 - Rational(25, 10) * 6,
 "H2E-08": lambda: expand((5 * m + 8) + (3 * m - 2)),
 "H2E-09": lambda: "common factor 3y",
 "H2E-10": lambda: 7 ** 2 - 3,
 "H2E-11": lambda: solve(Eq(2 ** x, 64), x)[0],
 "H2E-12": lambda: Rational(144, 4 ** 2),
 "H2E-13": lambda: expand(4 * (2 * p - 3) + 5 * p),
 "H2E-14": lambda: 80 * Rational(1, 2) ** 3,
 "H2E-15": lambda: Rational(3, 5) * 45,
 "H2E-16": lambda: Rational((250 - 210) * 100, 250),
 "H2E-17": lambda: 62 + 48 + 35 + 41,
 "H2E-18": lambda: sorted([42, 55, 61, 38, 74, 50, 66])[3],
 "H2E-19": lambda: 180 - 63,
 "H2E-20": lambda: pi * 9 ** 2,
 "H2E-21": lambda: 4 * 3 * 5,
 "H2E-22": lambda: sqrt(S(9) ** 2 + 12 ** 2),

 "H2H-01": lambda: Rational(9, 6) * (-4),
 "H2H-02": h2h_02,
 "H2H-03": lambda: max(i for i in range(1000) if 3 * (3 * i) + 8 * i <= 240),
 "H2H-04": lambda: 21 * solve(Eq(14 * (t + 2), 21 * t), t)[0],
 "H2H-05": h2h_05,
 "H2H-06": h2h_06,
 "H2H-07": lambda: "controller range",
 "H2H-08": lambda: solve(Eq(a * (3 ** 2 - 2) + 7, 35), a)[0],
 "H2H-09": lambda: cancel((2 * x ** 2 - 18) / (x ** 2 + 6 * x + 9)),
 "H2H-10": lambda: 13 - Rational(6 ** 2, 4),
 "H2H-11": h2h_11,
 "H2H-12": lambda: simplify((27 * B_POS ** 6) ** Rational(4, 3) / (9 * B_POS ** 5)),
 "H2H-13": h2h_13,
 "H2H-14": lambda: 12 * 3 ** (t / S(5)),
 "H2H-15": lambda: Rational(14 * 42 + 6 * 57, 10 * 20),
 "H2H-16": lambda: Rational(54, 54 + 96),
 "H2H-17": lambda: Rational(13500, 45 * 60),
 "H2H-18": lambda: Rational(21 * 900, 60),
 "H2H-19": lambda: 8 * Rational(6 + 9, 6),
 "H2H-20": lambda: pi * 3 ** 2 * 5 + Rational(1, 3) * pi * 3 ** 2 * 4,
 "H2H-21": lambda: Rational(24, 25),
 "H2H-22": lambda: Rational(10 ** 3, 25 * 8),
}

# Structural answers, where the marked choice is a form, an interval or a
# sentence rather than a value sympy can compare against.
FORM = {
 "H2E-04": "fixed charge",
 "H2E-05": "\\le 40",
 "H2E-09": "3y(2y-5)",
 "H2H-07": "16\\le r\\le 20.8",
}


def latex_to_expr(text):
    """Turn one answer choice into something sympify can read."""
    t = text.replace("&deg;", "").replace("&gt;", ">").replace("&lt;", "<")
    t = re.sub(r"\\left|\\right", "", t)
    t = re.sub(r"\\\((.*?)\\\)", r"\1", t, flags=re.S)
    # Exponents first: \frac{4a^{3}}{b^{4}} has braces nested inside the
    # numerator, and a non-recursive \frac pattern silently fails to match it.
    # Rewriting ^{...} to **(...) flattens the nesting so \frac then matches.
    t = re.sub(r"\^\{([^{}]*)\}", r"**(\1)", t)
    t = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"((\1)/(\2))", t)
    t = t.replace("\\pi", "pi").replace("\\cdot", "*").replace("\\sqrt", "sqrt")
    t = t.replace("{,}", "").replace(",", "").replace("$", "").replace("%", "")
    t = t.replace("^", "**").replace("{", "(").replace("}", ")")
    t = re.sub(r"(\d)\s*([a-zA-Z(])", r"\1*\2", t)
    t = re.sub(r"\)\s*\(", ")*(", t)
    return t.strip()


print("== pass 1: independent sympy derivation")
for q in ALL:
    tag = q["n"]
    got = DERIVE[tag]()

    if tag in FORM:
        # structural answer: assert the marked choice carries the derived form
        marker = FORM[tag]
        text = q["choices"]["ABCD".index(q["correct"])] if q["type"] == "MC" else ""
        norm = text.replace(" ", "")
        check(marker.replace(" ", "") in norm or marker in text,
              f"{tag}: correct choice {text!r} does not carry {marker!r}")
        continue

    if q["type"] == "FR":
        ok = False
        for ans in q["answers"]:
            try:
                ok = ok or simplify(sympify(latex_to_expr(ans)) - got) == 0
            except Exception:
                ok = ok or ans.strip() == str(got).strip()
        check(ok, f"{tag}: sympy got {got}, accepted answers are {q['answers']}")
        continue

    text = q["choices"]["ABCD".index(q["correct"])]
    # Try plain symbols first, then the positive-assumption reading. A symbol
    # declared positive is a *different* Symbol from an undeclared one, so a
    # single parse can miss a match that is really there — whichever side of the
    # comparison happens to carry the assumption.
    ok = False
    for loc in ({}, {nm: symbols(nm, positive=True) for nm in ("a", "b", "x", "y")}):
        try:
            if simplify(sympify(latex_to_expr(text), locals=loc) - got) == 0:
                ok = True
                break
        except Exception:
            pass
    if not ok:
        ok = latex_to_expr(text).replace(" ", "") == str(got).replace(" ", "")
    check(ok, f"{tag}: sympy got {got}, but choice {q['correct']} is {text!r}")

    # every distractor must be genuinely different from the key
    for i, alt in enumerate(q["choices"]):
        if i == "ABCD".index(q["correct"]):
            continue
        bad = False
        try:
            bad = simplify(sympify(latex_to_expr(alt)) - got) == 0
        except Exception:
            bad = False
        check(not bad, f"{tag}: distractor {'ABCD'[i]} ({alt!r}) equals the key")

# ---------------------------------------------------------------- shape rules
print("== pass 2: shape and house style")
for nm, md in (("Module 1", MODULE_1), ("Module 2 Easy", MODULE_2_EASY),
               ("Module 2 Hard", MODULE_2_HARD)):
    check(len(md) == 22, f"{nm} has {len(md)}, expected 22")

for name, mod in (("M1", MODULE_1), ("M2E", MODULE_2_EASY), ("M2H", MODULE_2_HARD)):
    fr = [q for q in mod if q["type"] == "FR"]
    check(len(fr) == 3, f"{name}: {len(fr)} free-response, the target is exactly 3")
    dom = Counter(q["domain"] for q in mod)
    check(dom["ALG"] == 7 and dom["ADV"] == 7 and dom["PSDA"] == 4 and dom["GT"] == 4,
          f"{name}: domain mix is {dict(dom)}, wanted 7 ALG / 7 ADV / 4 PSDA / 4 GT")
    bal = Counter(q["correct"] for q in mod if q["type"] == "MC")
    check(max(bal.values()) <= 8, f"{name}: answer key unbalanced {dict(bal)}")

VALID_SKILLS = {
    "ALG": {"ALG-LE", "ALG-LF", "ALG-LI"},
    "ADV": {"ADV-NF", "ADV-EQ", "ADV-NE"},
    "PSDA": {"PSDA-RP", "PSDA-ST", "PSDA-DI"},
    "GT": {"GT-AV", "GT-LA", "GT-TR"},
}

SPAN = re.compile(r"\\\((.*?)\\\)|\\\[(.*?)\\\]", re.S)

seen_ids = set()
for q in ALL:
    tag = q["n"]
    check(tag not in seen_ids, f"{tag}: duplicate question id")
    seen_ids.add(tag)
    check(q["skill"] in VALID_SKILLS[q["domain"]],
          f"{tag}: skill {q['skill']} is not a {q['domain']} skill")

    blocks = [q["stem"]] + list(q.get("choices") or [])
    if q["type"] == "MC":
        check(len(q["choices"]) == 4, f"{tag}: needs exactly 4 choices")
        check(len(set(q["choices"])) == 4, f"{tag}: duplicate answer choice")
        check(q["correct"] in "ABCD", f"{tag}: bad answer label")
    else:
        check(bool(q.get("answers")), f"{tag}: free response with no accepted answer")

    for blk in blocks:
        check(not blk.strip().startswith("<p>"), f"{tag}: stem is <p>-wrapped")
        check("°" not in blk, f"{tag}: raw degree glyph, use &deg;")
        spans = [mm.span() for mm in SPAN.finditer(blk)]
        inside = lambda i: any(aa <= i < bb for aa, bb in spans)

        for mm in re.finditer(r"\^", blk):
            check(inside(mm.start()), f"{tag}: caret outside math mode")
        for mm in re.finditer(r"\bsqrt\s*\(", blk):
            check(False, f"{tag}: plain-text sqrt(")
        for mm in re.finditer(r"[\dA-Za-z)]\s*\*\s*[\dA-Za-z(]", blk):
            check(inside(mm.start()), f"{tag}: asterisk multiplication outside math mode")
        for mm in re.finditer(r"(?<![\d/:])\d+\s*/\s*\d+(?![\d/])", blk):
            check(inside(mm.start()), f"{tag}: slash fraction outside math mode")
        for mm in re.finditer(r"\\(pi|frac|sqrt|cdot|le|ge|ne|circ|sin|cos|tan|log)\b", blk):
            check(inside(mm.start()), f"{tag}: LaTeX macro outside math mode")
        for mm in re.finditer(r"(!=|<=|>=)", blk):
            check(False, f"{tag}: ASCII comparison operator, use \\ne / \\le / \\ge")
        for mm in re.finditer(r"(?<![A-Za-z])(theta|alpha|beta)(?![A-Za-z])", blk):
            check(inside(mm.start()), f"{tag}: Greek letter spelled out in prose")
        for mm in re.finditer(r"(?<![A-Za-z])pi(?![A-Za-z])", blk):
            check(inside(mm.start()), f"{tag}: bare word pi outside math mode")

        for aa, bnd in spans:
            span_text = blk[aa:bnd]
            for fn in ("sin", "cos", "tan", "log", "ln"):
                check(not re.search(r"(?<!\\)\b" + fn + r"\b", span_text),
                      f"{tag}: unescaped {fn} inside math mode")
            words = re.findall(r"[A-Za-z]{3,}", re.sub(r"\\[a-zA-Z]+", "", span_text))
            check(len(words) < 2, f"{tag}: prose inside math mode: {span_text!r}")

        # an inline span must not be glued to the surrounding prose
        for mo in re.finditer(r"[A-Za-z0-9]\\\(", blk):
            check(False, f"{tag}: math span opens with no space before it")
        for mo in re.finditer(r"\\\)[A-Za-z0-9]", blk):
            check(False, f"{tag}: math span closes with no space after it")

    if re.search(r"\btable\b", q["stem"], re.I):
        check("<table" in q["stem"], f"{tag}: mentions a table but has no <table> markup")
    if re.search(r"\b(shown|the figure|following (?:graph|figure|chart)|graph above)\b",
                 q["stem"], re.I):
        check("<table" in q["stem"] or "<img" in q["stem"],
              f"{tag}: refers to a visual it does not contain")

# ------------------------------------------------------------------- dedupe
print("== pass 3: template dedupe against production")


def sig(text):
    t = re.sub(r"<[^>]+>", " ", text)
    t = re.sub(r"&[a-z]+;", " ", t)
    math = []
    for mm in SPAN.findall(t):
        sp = mm[0] or mm[1]
        if "\\frac" in sp: math.append("mathfrac")
        if "\\sqrt" in sp: math.append("mathsqrt")
        if "\\pi" in sp: math.append("mathpi")
        if re.search(r"\^\{?2\}?", sp): math.append("mathsq")
        if re.search(r"\^\{?[a-z]\}?", sp): math.append("mathexpvar")
    t = re.sub(r"\\[a-zA-Z]+", " ", t)
    t = re.sub(r"[-+]?\d[\d,.]*", "#", t)
    return set((re.sub(r"[^a-z#]+", " ", t.lower()).strip() + " " + " ".join(sorted(set(math)))).split())


def jaccard(aa, bb):
    return len(aa & bb) / max(1, len(aa | bb))


prod_path = os.path.join(HERE, "prod_math_stems.json")
if os.environ.get("DATABASE_URL"):
    js = """
    const { neon } = await import("@neondatabase/serverless");
    const sql = neon(process.env.DATABASE_URL);
    const rows = await sql`SELECT t.title, m."order" AS mo, m.difficulty AS d, q."order" AS qo, q.stem
      FROM "Question" q JOIN "Module" m ON m.id=q."moduleId" JOIN "Test" t ON t.id=m."testId"
      WHERE m.subject='MATH'`;
    process.stdout.write(JSON.stringify(rows.map(r => ({
      label: `${r.title} M${r.mo}${r.d[0]} Q${r.qo}`, stem: r.stem.replace(/<img[^>]*>/g, " ") }))));
    """
    out = os.path.join(HERE, "_dump_prod.mjs")
    open(out, "w").write(js)
    res = subprocess.run(["node", out], capture_output=True, text=True, cwd=HERE)
    if res.returncode == 0 and res.stdout.strip():
        open(prod_path, "w").write(res.stdout)
    else:
        print(f"   WARNING: production dump failed: {res.stderr.strip()[:400]}")
    os.remove(out)

if os.path.exists(prod_path):
    prod = json.load(open(prod_path))
    print(f"   comparing against {len(prod)} live Math stems")
    others = [(pq["label"], sig(pq["stem"])) for pq in prod]
    worst = []
    for q in ALL:
        s0 = sig(q["stem"])
        score, label = max(((jaccard(s0, o), lab) for lab, o in others), key=lambda z: z[0])
        worst.append((score, q["n"], label))
        check(score < 0.75, f"{q['n']}: template similarity {score:.2f} to {label}")
    worst.sort(reverse=True)
    print("   closest matches:")
    for sc, tag, lab in worst[:8]:
        print(f"     {sc:.2f}  {tag}  vs {lab}")
else:
    print("   SKIPPED — no DATABASE_URL and no cached prod_math_stems.json")

# internal dedupe
for i in range(len(ALL)):
    for j in range(i + 1, len(ALL)):
        sc = jaccard(sig(ALL[i]["stem"]), sig(ALL[j]["stem"]))
        check(sc < 0.80, f"{ALL[i]['n']} vs {ALL[j]['n']}: internal similarity {sc:.2f}")

# ------------------------------------------ pass 4: sibling unshipped builds
print("== pass 4: cross-check against the sibling Test 13 / Test 14 builds")
for sib_dir, sib_file in (("test-13-build", "math_test13.py"),
                          ("test-14-build", "math_test14.py")):
    sibling = os.path.abspath(os.path.join(HERE, "..", sib_dir, sib_file))
    if not os.path.exists(sibling):
        print(f"   SKIPPED — ../{sib_dir}/{sib_file} does not exist yet")
        continue
    # Read and exec the source rather than importing it: an ordinary import
    # would drop a __pycache__ entry into the other agent's build directory,
    # and this pass must be strictly read-only over there.
    try:
        ns = {"__name__": f"{sib_file[:-3]}_readonly", "__file__": sibling}
        exec(compile(open(sibling).read(), sibling, "exec"), ns)
        sib = ns["ALL"]
        print(f"   comparing against {len(sib)} unshipped {sib_dir} Math stems")
        worst_sib = []
        for q in ALL:
            s0 = sig(q["stem"])
            score, label = max(((jaccard(s0, sig(o["stem"])), o["n"]) for o in sib),
                               key=lambda z: z[0])
            worst_sib.append((score, q["n"], label))
            check(score < 0.75, f"{q['n']}: {sib_dir} similarity {score:.2f} to {label}")
        worst_sib.sort(reverse=True)
        print("   closest matches:")
        for sc, tag, lab in worst_sib[:6]:
            print(f"     {sc:.2f}  {tag}  vs {sib_dir} {lab}")
    except Exception as exc:  # the sibling may still be mid-write
        print(f"   SKIPPED — could not read the {sib_dir} build ({exc})")

# ------------------------------------------------------------------- report
print()
print(f"questions: {len(ALL)}   M1 domains: {dict(Counter(q['domain'] for q in MODULE_1))}")
print(f"                    M2E domains: {dict(Counter(q['domain'] for q in MODULE_2_EASY))}")
print(f"                    M2H domains: {dict(Counter(q['domain'] for q in MODULE_2_HARD))}")
print(f"answer key M1:  {dict(sorted(Counter(q['correct'] for q in MODULE_1 if q['type']=='MC').items()))}")
print(f"answer key M2E: {dict(sorted(Counter(q['correct'] for q in MODULE_2_EASY if q['type']=='MC').items()))}")
print(f"answer key M2H: {dict(sorted(Counter(q['correct'] for q in MODULE_2_HARD if q['type']=='MC').items()))}")

if FAIL:
    print(f"\n{len(FAIL)} FAILURES:")
    for f in FAIL:
        print("  -", f)
    raise SystemExit(1)
print("\nALL CHECKS PASSED")
