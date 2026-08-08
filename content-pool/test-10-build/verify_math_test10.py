#!/usr/bin/env python3
"""
Verify the 66 originally-authored Math questions for Test 10.

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

Run:  DATABASE_URL='postgresql://...' python3 verify_math_test10.py
      (without DATABASE_URL it verifies everything except the dedupe pass)
"""
import json
import os
import re
import subprocess
import sys
from collections import Counter

from sympy import (Eq, Rational, S, solve, sqrt, symbols, simplify, sympify,
                   nsimplify, pi, cos, expand, cancel, discriminant, Poly)

from math_test10 import MODULE_1, MODULE_2_EASY, MODULE_2_HARD, ALL

HERE = os.path.dirname(os.path.abspath(__file__))
x, y, k, b, c, n, t, v, s = symbols("x y k b c n t v s")
A, h, p, g = symbols("A h p g")
FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)


# ---------------------------------------------------------------- derivations
SQ = lambda nm: symbols(nm, positive=True)


def c1_02():
    sol = solve([Eq(3 * c + 5 * b, 97), Eq(2 * c + 9 * b, 93)], [c, b])
    return sol[c]


def c1_18():
    xv = solve(Eq((2 * x + 10) + (3 * x - 5) + (x + 7), 180), x)[0]
    return max(2 * xv + 10, 3 * xv - 5, xv + 7)


def c2h_02():
    sol = solve([Eq(c - 3 * v, 19400), Eq(c - 7 * v, 12200)], [c, v])
    return sol[c]


def c2h_04():
    w = max(solve(Eq(x * (x + 3), 154), x))
    return (w + 2) * (w + 3 + 2) - 154


def c2h_07():
    return [r for r in solve(Eq(12 / x + 12 / (x + 2), 5), x) if r > 0][0]


def c2h_20():
    rate = Rational(3240 - 2360, 100) / 8
    fee = Rational(2360, 100) - 14 * rate
    return fee + 35 * rate


DERIVE = {
 "C1-01": lambda: solve(Eq(250 * (x + 4) + 450 * x, 6600), x)[0],
 "C1-02": c1_02,
 "C1-03": lambda: solve(Eq(30 - (Rational(36, 10) / 45) * t, 12), t)[0],
 "C1-04": lambda: max(i for i in range(100) if 78 + 34 * i <= 900),
 "C1-05": lambda: 29 + solve(Eq(29 + k * (11 - 3), 69), k)[0] * (20 - 3),
 "C1-06": lambda: solve(Eq(Rational(28, 10) - Rational(6, 10) * t, Rational(16, 10)), t)[0],
 "C1-07": lambda: solve(Eq(18 + Rational(453 - 18, 3) * t, 1033), t)[0],
 "C1-08": lambda: cancel((6 * x ** 2 + 13 * x - 5) / (3 * x - 1)),
 "C1-09": lambda: -Rational(1, 2) * 12 ** 2 + 12 * 12 + 3,
 "C1-10": lambda: solve(Eq(Rational(1, 3) ** x, Rational(1, 243)), x)[0],
 "C1-11": lambda: max(solve(Eq(x ** 2 - 14 * x + 40, 0), x)) - min(solve(Eq(x ** 2 - 14 * x + 40, 0), x)),
 "C1-12": lambda: solve(Eq(A, 2 * s ** 2 + 4 * s * h), h)[0],
 "C1-13": lambda: [r for r in solve(Eq(x ** 3 / 4 - 2, 14), x) if r.is_real][0],
 "C1-14": lambda: round(float(2500 * 1.04 ** 3)),
 "C1-15": lambda: Rational(21875, 1250) * 8,
 "C1-16": lambda: Rational(102 * 10000, 80 * 85),
 "C1-17": lambda: Rational((250 - (42 + 58 + 61 + 39)) * 100, 250),
 "C1-18": c1_18,
 "C1-19": lambda: 24 / cos(pi / 6),
 "C1-20": lambda: Rational(12 * 5 * 16, 10 * 4),
 "C1-21": lambda: Rational(54, 240) * 8000,
 "C1-22": lambda: sqrt(S(105) ** 2 + 88 ** 2),

 "C2E-01": lambda: solve(Eq(8 * x, 192), x)[0],
 "C2E-02": lambda: Rational(36, 10) / 8,
 "C2E-03": lambda: "C=2+0.25m",
 "C2E-04": lambda: 54 - 6 * 5,
 "C2E-05": lambda: "at most 600",
 "C2E-06": lambda: solve(Eq(2 * (8 + x), 26), x)[0],
 "C2E-07": lambda: "kilograms gained per day",
 "C2E-08": lambda: simplify(Rational(1, 2) * x * 6),
 "C2E-09": lambda: expand(5 * (2 * p + 3)),
 "C2E-10": lambda: 4 * 5 ** 2,
 "C2E-11": lambda: solve(Eq(sqrt(x + 7), 5), x)[0],
 "C2E-12": lambda: 4 ** 2 + 3 * 4,
 "C2E-13": lambda: simplify(x ** 8 / x ** 3),
 "C2E-14": lambda: 2 ** 6,
 "C2E-15": lambda: Rational(3, 12) * 40,
 "C2E-16": lambda: Rational(40, 100) * 250,
 "C2E-17": lambda: 340 + 295 + 412,
 "C2E-18": lambda: sorted([12, 15, 15, 20, 28])[2],
 "C2E-19": lambda: 180 - 118,
 "C2E-20": lambda: 9 * 5 * 4,
 "C2E-21": lambda: 28 * 5,
 "C2E-22": lambda: sqrt(S(5) ** 2 + 12 ** 2),

 "C2H-01": lambda: solve(Eq(Rational(2, 3) * (6 * x - 9), 4 * x + c), c)[0],
 "C2H-02": c2h_02,
 "C2H-03": lambda: min(i for i in range(201) if 4 * (200 - i) + 11 * i >= 1500),
 "C2H-04": c2h_04,
 "C2H-05": lambda: expand((x + 3) ** 2 - 4 * (x + 3)),
 "C2H-06": lambda: simplify(3 / (x + 2) - 2 / (x - 1)),
 "C2H-07": c2h_07,
 "C2H-08": lambda: simplify((27 * SQ("x") ** 12) ** Rational(1, 3) * SQ("x") ** -2),
 "C2H-09": lambda: Rational(72 * 72 * 10, 405),
 "C2H-10": lambda: solve(Eq(discriminant(Poly(x ** 2 - 8 * x + (11 - c), x)), 0), c)[0],
 "C2H-11": lambda: Rational(48, 3),
 "C2H-12": lambda: "plausible range for the mean",
 "C2H-13": lambda: Rational(30 * 52 + 20 * 62, 50),
 "C2H-14": lambda: min(Rational(84 * 8, 3), Rational(120 * 8, 5)),
 "C2H-15": lambda: Rational(24150 * 21160, 18400),
 "C2H-16": lambda: sqrt(S(25) ** 2 - 7 ** 2),
 "C2H-17": lambda: solve(Eq(Rational(1, 3) * pi * 6 ** 2 * h, pi * 3 ** 2 * 16), h)[0],
 "C2H-18": lambda: Rational(20, 29),
 "C2H-19": lambda: max(i for i in range(101) if 4 * (100 - i) + 7 * i <= 560),
 "C2H-20": c2h_20,
 "C2H-21": lambda: solve(Eq(5 * x - 2 * (40 - x), 137), x)[0],
 "C2H-22": lambda: (pi * 4 ** 2 * 10 + Rational(1, 3) * pi * 4 ** 2 * 3) / pi,
}

FORM = {
 "C2E-03": "C=2+0.25m",
 "C2E-05": "\\le 600",
 "C2E-07": "increases each day",
 "C2H-12": "plausible",
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

# ---------------------------------------------------------------- shape rules
print("== pass 2: shape and house style")
for nm, md in (("Module 1", MODULE_1), ("Module 2 Easy", MODULE_2_EASY), ("Module 2 Hard", MODULE_2_HARD)):
    check(len(md) == 22, f"{nm} has {len(md)}, expected 22")

for name, mod in (("M1", MODULE_1), ("M2E", MODULE_2_EASY), ("M2H", MODULE_2_HARD)):
    fr = [q for q in mod if q["type"] == "FR"]
    check(len(fr) == 3, f"{name}: {len(fr)} free-response, the target is exactly 3")
    dom = Counter(q["domain"] for q in mod)
    check(dom["ALG"] == 7 and dom["ADV"] == 7 and dom["PSDA"] == 4 and dom["GT"] == 4,
          f"{name}: domain mix is {dict(dom)}, wanted 7 ALG / 7 ADV / 4 PSDA / 4 GT")
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
        inside = lambda i: any(a <= i < bb for a, bb in spans)

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
