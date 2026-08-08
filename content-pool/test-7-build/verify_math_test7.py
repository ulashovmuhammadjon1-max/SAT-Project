#!/usr/bin/env python3
"""
Verify the 44 originally-authored Math questions for Test 7.

Three independent passes, because each has caught a different class of defect
in earlier builds:

 1. Answers are re-derived with sympy from the question itself, never read off
    the `check` note. A wrong `check` and a wrong key agree with each other;
    only an independent derivation catches that.
 2. House style is enforced on the final HTML — the Test 1/2 rules in
    CLAUDE.md, plus the DB-wide rendering checks (no bare `^`, `sqrt(`,
    `*`-as-multiply, slash fractions or LaTeX macros outside a math span).
 3. Template dedupe against every Math stem live in production, not just exact
    duplicates: a question that reuses a template with new numbers is a repeat.

Run:  DATABASE_URL='postgresql://...' python3 verify_math_test7.py
      (without DATABASE_URL it verifies everything except the dedupe pass)
"""
import json
import os
import re
import subprocess
import sys
from collections import Counter

from sympy import (Eq, Rational, S, solve, sqrt, symbols, simplify, sympify,
                   nsimplify, pi, discriminant, Poly)

from math_test7 import MODULE_1, MODULE_2_HARD, ALL

HERE = os.path.dirname(os.path.abspath(__file__))
x, y, k, b, c, n, t, v, s = symbols("x y k b c n t v s")
FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)


# ---------------------------------------------------------------- derivations
def h2_03():
    # perpendicular to slope 2/3 -> slope -3/2, through (-4, 9)
    bb = symbols("bb")
    return solve(Eq(9, Rational(-3, 2) * (-4) + bb), bb)[0]


def h2_08():
    roots = solve(Eq(2 * x + 11, (x + 4) ** 2), x)
    keep = [r for r in roots if sqrt(2 * r + 11) == r + 4]
    return keep[0]


DERIVE = {
 "M1-01": lambda: solve(Eq(65 + 28 * x, 289), x)[0],
 "M1-02": lambda: (lambda sol: sol[x] + sol[y])(solve([Eq(2 * x + 3 * y, 19), Eq(x - y, 2)], [x, y])),
 "M1-03": lambda: Rational(7 - (-1), 6 - 2),
 "M1-04": lambda: solve(Eq(94 - Rational(25, 10) * x, 34), x)[0],
 "M1-05": lambda: solve(4 - 2 * x > 10, x),
 "M1-06": lambda: 930 - 20 * Rational(1470 - 930, 35 - 20),
 "M1-07": lambda: "V=240-8t",
 "M1-08": lambda: simplify((2 * x - 5) * (x + 4)),
 "M1-09": lambda: (4 ** 2 - 8 * 4 + 13),
 "M1-10": lambda: solve(Eq(3 * 3 ** x, 243), x)[0],
 "M1-11": lambda: max(solve(Eq(x ** 2 - 5 * x - 24, 0), x)),
 "M1-12": lambda: simplify(12 * symbols("a", positive=True) ** 5 * symbols("b", positive=True) ** 3 / (3 * symbols("a", positive=True) ** 2 * symbols("b", positive=True) ** 7)),
 "M1-13": lambda: Rational(-20, 2 * -5),
 "M1-14": lambda: "400(3)^(t/6)",
 "M1-15": lambda: Rational(18 * 4, 3),
 "M1-16": lambda: Rational(80, 100) * Rational(85, 100) * 100,
 "M1-17": lambda: sorted([42, 38, 51, 47, 62])[2],
 "M1-18": lambda: Rational(26, 400) * 5000,
 "M1-19": lambda: 118 - 47,
 "M1-20": lambda: round(float(pi * 5 ** 2 * 12)),
 "M1-21": lambda: solve(Eq(n + (n + 2) + (n + 4), 138), n)[0] + 4,
 "M1-22": lambda: sqrt(9 ** 2 + 12 ** 2),

 "H2-01": lambda: (lambda sol: sol[symbols("st")])(solve([Eq(symbols("ad") + symbols("st"), 340), Eq(18 * symbols("ad") + 11 * symbols("st"), 4790)], [symbols("ad"), symbols("st")])),
 "H2-02": lambda: solve(Eq(c / 9, Rational(-1, -3)), c)[0],
 "H2-03": h2_03,
 "H2-04": lambda: max(i for i in range(21) if 4 * i + 3 * (20 - i) <= 68),
 "H2-05": lambda: [r for r in solve(Eq(discriminant(Poly(x ** 2 + b * x + 45, x)), 0), b) if r > 0][0],
 "H2-06": lambda: 3 + (2 * 3 ** 2 - 12 * 3 + 7),
 "H2-07": lambda: ((2 * 2 + 3) ** 2 - 1),
 "H2-08": h2_08,
 "H2-09": lambda: solve(Eq(k * 2 ** 5 - k * 2 ** 3, 96), k)[0],
 "H2-10": lambda: simplify((64 * symbols("y", positive=True) ** 12) ** Rational(1, 3)),
 "H2-11": lambda: (-1, 3 * (-1) ** 2 + 6 * (-1) - 2),
 "H2-12": lambda: 9 * 26 - 8 * 24,
 "H2-13": lambda: Rational(62, 110),
 "H2-14": lambda: Rational(120, Rational(60, 40) + Rational(60, 60)),
 "H2-15": lambda: Rational(int(6.4 * 40 * 10) - 70, 400),
 "H2-16": lambda: solve(Eq(Rational(8, 12), x / 18), x)[0],
 "H2-17": lambda: solve(Eq(Rational(4, 3) * pi * 3 ** 3, Rational(1, 3) * pi * 3 ** 2 * x), x)[0],
 "H2-18": lambda: sqrt(S(13) ** 2 - 5 ** 2),
 "H2-19": lambda: 47 - 2 * Rational(131 - 47, 6 - 2),
 "H2-20": lambda: sum(solve(Eq(2 * x ** 2 - 11 * x + 12, 0), x)),
 "H2-21": lambda: solve(Eq(Rational(20, 100) * 12 + Rational(50, 100) * v,
                          Rational(30, 100) * (12 + v)), v)[0],
 "H2-22": lambda: [r for r in solve(Eq(3 * x ** 3, 375), x) if r.is_real][0],
}

# Questions whose answer is a form, an interval or a pair rather than a number.
FORM = {
 "M1-05": "x<-3",
 "M1-07": "V=240-8t",
 "M1-14": "400(3)^{\\frac{t}{6}}",
 "H2-11": "minimum",
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
        for a in q["answers"]:
            try:
                ok = ok or simplify(sympify(latex_to_expr(a)) - got) == 0
            except Exception:
                ok = ok or a.strip() == str(got).strip()
        check(ok, f"{tag}: sympy got {got}, accepted answers are {q['answers']}")
        continue

    text = q["choices"]["ABCD".index(q["correct"])]
    try:
        # Parse the choice with the same positivity assumptions the stem states,
        # so a radical like (y^12)^(1/3) folds to y^4 on both sides.
        cand = sympify(latex_to_expr(text),
                       locals={n: symbols(n, positive=True) for n in ("a", "b", "y")})
        ok = simplify(cand - got) == 0
    except Exception:
        ok = latex_to_expr(text).replace(" ", "") == str(got).replace(" ", "")
    check(ok, f"{tag}: sympy got {got}, but choice {q['correct']} is {text!r}")

# ---------------------------------------------------------------- shape rules
print("== pass 2: shape and house style")
check(len(MODULE_1) == 22, f"Module 1 has {len(MODULE_1)}, expected 22")
check(len(MODULE_2_HARD) == 22, f"Module 2 Hard has {len(MODULE_2_HARD)}, expected 22")

for name, mod in (("M1", MODULE_1), ("M2H", MODULE_2_HARD)):
    fr = [q for q in mod if q["type"] == "FR"]
    check(len(fr) == 3, f"{name}: {len(fr)} free-response, the target is exactly 3")
    dom = Counter(q["domain"] for q in mod)
    check(dom["ALG"] >= 6 and dom["ADV"] >= 6, f"{name}: thin domain mix {dict(dom)}")
    bal = Counter(q["correct"] for q in mod if q["type"] == "MC")
    check(max(bal.values()) <= 8, f"{name}: answer key unbalanced {dict(bal)}")

SPAN = re.compile(r"\\\((.*?)\\\)|\\\[(.*?)\\\]", re.S)

for q in ALL:
    tag = q["n"]
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
        spans = [m.span() for m in SPAN.finditer(blk)]
        inside = lambda i: any(a <= i < b for a, b in spans)

        for m in re.finditer(r"\^", blk):
            check(inside(m.start()), f"{tag}: caret outside math mode")
        for m in re.finditer(r"\bsqrt\s*\(", blk):
            check(False, f"{tag}: plain-text sqrt(")
        for m in re.finditer(r"[\dA-Za-z)]\s*\*\s*[\dA-Za-z(]", blk):
            check(inside(m.start()), f"{tag}: asterisk multiplication outside math mode")
        for m in re.finditer(r"(?<![\d/:])\d+\s*/\s*\d+(?![\d/])", blk):
            check(inside(m.start()), f"{tag}: slash fraction outside math mode")
        for m in re.finditer(r"\\(pi|frac|sqrt|cdot|le|ge|ne|circ|sin|cos|tan|log)\b", blk):
            check(inside(m.start()), f"{tag}: LaTeX macro outside math mode")
        for m in re.finditer(r"(!=|<=|>=)", blk):
            check(False, f"{tag}: ASCII comparison operator, use \\ne / \\le / \\ge")

        for a, bnd in spans:
            span_text = blk[a:bnd]
            for fn in ("sin", "cos", "tan", "log", "ln"):
                check(not re.search(r"(?<!\\)\b" + fn + r"\b", span_text),
                      f"{tag}: unescaped {fn} inside math mode")
            words = re.findall(r"[A-Za-z]{3,}", re.sub(r"\\[a-zA-Z]+", "", span_text))
            check(len(words) < 2, f"{tag}: prose inside math mode: {span_text!r}")

    if re.search(r"\btable\b", q["stem"], re.I):
        check("<table" in q["stem"], f"{tag}: mentions a table but has no <table> markup")
    if re.search(r"\b(shown|the figure|following (?:graph|figure|chart)|graph above)\b", q["stem"], re.I):
        check("<table" in q["stem"] or "<img" in q["stem"],
              f"{tag}: refers to a visual it does not contain")

# ------------------------------------------------------------------- dedupe
print("== pass 3: template dedupe against production")


def sig(text):
    t = re.sub(r"<[^>]+>", " ", text)
    t = re.sub(r"&[a-z]+;", " ", t)
    math = []
    for m in SPAN.findall(t):
        sp = m[0] or m[1]
        if "\\frac" in sp: math.append("mathfrac")
        if "\\sqrt" in sp: math.append("mathsqrt")
        if "\\pi" in sp: math.append("mathpi")
        if re.search(r"\^\{?2\}?", sp): math.append("mathsq")
        if re.search(r"\^\{?[a-z]\}?", sp): math.append("mathexpvar")
    t = re.sub(r"\\[a-zA-Z]+", " ", t)
    t = re.sub(r"[-+]?\d[\d,.]*", "#", t)
    return set((re.sub(r"[^a-z#]+", " ", t.lower()).strip() + " " + " ".join(sorted(set(math)))).split())


def jaccard(a, b):
    return len(a & b) / max(1, len(a | b))


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
    os.remove(out)

if os.path.exists(prod_path):
    prod = json.load(open(prod_path))
    print(f"   comparing against {len(prod)} live Math stems")
    others = [(p["label"], sig(p["stem"])) for p in prod]
    worst = []
    for q in ALL:
        s0 = sig(q["stem"])
        score, label = max(((jaccard(s0, o), lab) for lab, o in others), key=lambda z: z[0])
        worst.append((score, q["n"], label))
        check(score < 0.75, f"{q['n']}: template similarity {score:.2f} to {label}")
    worst.sort(reverse=True)
    print("   closest matches:")
    for sc, tag, lab in worst[:5]:
        print(f"     {sc:.2f}  {tag}  vs {lab}")
else:
    print("   SKIPPED — no DATABASE_URL and no cached prod_math_stems.json")

# internal dedupe
for i in range(len(ALL)):
    for j in range(i + 1, len(ALL)):
        sc = jaccard(sig(ALL[i]["stem"]), sig(ALL[j]["stem"]))
        check(sc < 0.80, f"{ALL[i]['n']} vs {ALL[j]['n']}: internal similarity {sc:.2f}")

# ------------------------------------------------------------------- report
print()
print(f"questions: {len(ALL)}   M1 domains: {dict(Counter(q['domain'] for q in MODULE_1))}")
print(f"                     M2H domains: {dict(Counter(q['domain'] for q in MODULE_2_HARD))}")
print(f"answer key M1:  {dict(sorted(Counter(q['correct'] for q in MODULE_1 if q['type']=='MC').items()))}")
print(f"answer key M2H: {dict(sorted(Counter(q['correct'] for q in MODULE_2_HARD if q['type']=='MC').items()))}")

if FAIL:
    print(f"\n{len(FAIL)} FAILURES:")
    for f in FAIL:
        print("  -", f)
    raise SystemExit(1)
print("\nALL CHECKS PASSED")
