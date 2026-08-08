#!/usr/bin/env python3
"""
Verify the 66 originally-authored Math questions for Test 9.

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

Run:  DATABASE_URL='postgresql://...' python3 verify_math_test9.py
      (without DATABASE_URL it verifies everything except the dedupe pass)
"""
import json
import os
import re
import subprocess
import sys
from collections import Counter

from sympy import (Abs, Eq, Rational, S, solve, sqrt, symbols, simplify, sympify,
                   nsimplify, pi, discriminant, Poly, diff, expand)

from math_test9 import MODULE_1, MODULE_2_EASY, MODULE_2_HARD, ALL

HERE = os.path.dirname(os.path.abspath(__file__))
x, y, k, b, c, n, t, v, s = symbols("x y k b c n t v s")
a, m, L, w = symbols("a m L w")
d = symbols("d", real=True)
FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)


# ---------------------------------------------------------------- derivations
SQ = lambda nm: symbols(nm, positive=True)


def b1_09():
    f = Rational(1, 2) * x ** 2 - 6 * x + 38
    return f.subs(x, solve(Eq(diff(f, x), 0), x)[0])


def b1_11():
    sol = solve([Eq(x + y, 14), Eq(x - y, 6)], [x, y])
    return sol[x] * sol[y]


def b1_20():
    roots = solve(Eq(-5 * t ** 2 + 40 * t, 60), t)
    return max(roots) - min(roots)


DERIVE = {
 "B1-01": lambda: solve(Eq(60 + 4 * x, Rational(13, 2) * x), x)[0],
 "B1-02": lambda: (lambda s_: 3 * s_[x] + 2 * s_[y])(
     solve([Eq(4 * x + 3 * y, 26), Eq(2 * x + 5 * y, 20)], [x, y])),
 "B1-03": lambda: solve(Eq(1410 + Rational(1050 - 1410, 12 - 6) * (t - 6), 450), t)[0],
 "B1-04": lambda: min(i for i in range(200) if 22 * i - 140 >= 500),
 "B1-05": lambda: solve(Eq(18 + Rational(6, 100) * (m - 250), Rational(396, 10)), m)[0],
 "B1-06": lambda: Rational(-3, 5) * 5,
 "B1-07": lambda: solve(Eq(28 * n, 21 * (n + 3)), n)[0],
 "B1-08": lambda: simplify((2 * x + 5) * (x - 3) - x ** 2),
 "B1-09": b1_09,
 "B1-10": lambda: simplify(solve(Eq(50 * 3 ** t, 4050), t)[0]),
 "B1-11": b1_11,
 "B1-12": lambda: simplify((x ** 2 - 9) / (x ** 2 + 7 * x + 12)),
 "B1-13": lambda: 18000 * Rational(85, 100) ** 2,
 "B1-14": lambda: Rational(21000, Rational(1250, 25)) / 60,
 "B1-15": lambda: Rational(150 - 96, 96) * 100,
 "B1-16": lambda: Rational(45, 200) * 12000,
 "B1-17": lambda: 2 * solve(Eq(x + (x + 32) + 2 * x, 180), x)[0],
 "B1-18": lambda: simplify(((2 * x) ** 2 * (y / 2)) / (x ** 2 * y)),
 "B1-19": lambda: 5 / sqrt(S(13) ** 2 - S(5) ** 2),
 "B1-20": b1_20,
 "B1-21": lambda: Rational(2500, 40) * 6,
 "B1-22": lambda: Rational(80 * 40 * 50 * 3, 4 * 1000),

 "B2E-01": lambda: Rational(350, 25),
 "B2E-02": lambda: solve(Eq(x + 7, -8), x)[0],
 "B2E-03": lambda: 150 - 3 * t,
 "B2E-04": lambda: 4 + Rational(15, 10) * 10,
 "B2E-05": lambda: S(9) - Rational(54, 10),
 "B2E-06": lambda: solve(Eq(3 * x - 5, 22), x)[0],
 "B2E-07": lambda: (24 - 2 * 1) - (24 - 2 * 2),
 "B2E-08": lambda: simplify((3 * x + 2) + (5 * x - 9)),
 "B2E-09": lambda: simplify(SQ("x") ** 8 / SQ("x") ** 5),
 "B2E-10": lambda: 2 * 3 ** 2 + 1,
 "B2E-11": lambda: S(27) ** Rational(1, 3),
 "B2E-12": lambda: 30 * 2 ** y,
 "B2E-13": lambda: simplify(6 * (2 * x - 5)),
 "B2E-14": lambda: [r for r in solve(Eq((x - 2) * (x + 6), 0), x) if r > 0][0],
 "B2E-15": lambda: Rational(12, 5) * 15,
 "B2E-16": lambda: sorted([3, 8, 11, 14, 21])[2],
 "B2E-17": lambda: 145 - 87,
 "B2E-18": lambda: Rational(3, 8),
 "B2E-19": lambda: 180 - 118,
 "B2E-20": lambda: Rational(30 * 16, 2),
 "B2E-21": lambda: 2 * (25 + 12),
 "B2E-22": lambda: sqrt(S(9) ** 2 + S(12) ** 2),

 "B2H-01": lambda: (solve(Eq(a / 4, Rational(18, 12)), a)[0]
                    + solve(Eq(S(6) / k, Rational(18, 12)), k)[0]),
 "B2H-02": lambda: solve(Eq(m * solve(Eq(2 * x + 5 * 0, 20), x)[0] + 7, 0), m)[0],
 "B2H-03": lambda: 3 * 10 + 2 * 4,
 "B2H-04": lambda: solve(Eq(s + (3 * s + k), L), s)[0],
 "B2H-05": lambda: c + Rational(21, 6) * 10,
 "B2H-06": lambda: 1 / (Rational(1, 6) + Rational(1, 9)),
 "B2H-07": lambda: min(solve(Eq(Abs(d - Rational(125, 10)), Rational(4, 100)), d)),
 "B2H-08": lambda: solve(Eq(discriminant(Poly(2 * x ** 2 - 12 * x + c, x)), 0), c)[0],
 "B2H-09": lambda: (lambda f: f ** 2 + 2 * f)(3 * 3 - 4),
 "B2H-10": lambda: simplify(2 / (x - 3) - 5 / (x + 2)),
 "B2H-11": lambda: solve(Eq(n * Rational(12, 10) ** 3, 864), n)[0],
 "B2H-12": lambda: [r for r in solve(Eq(5 * x + 6, x ** 2), x) if r > 0][0],
 "B2H-13": lambda: Rational(3, 7) + 1,
 "B2H-14": lambda: Rational(18 * 76 + 12 * 86, 30),
 "B2H-15": lambda: solve(Eq(Rational(140, 100) * Rational(75, 100) * x, 63), x)[0],
 "B2H-16": lambda: Rational(0 * 4 + 1 * 9 + 2 * 5 + 3 * 4 + 4 * 3, 25) - 1,
 "B2H-17": lambda: Rational(58, 100) * 4500,
 "B2H-18": lambda: Rational(9 * (6 + 4), 6),
 "B2H-19": lambda: 3 * solve(Eq(5 * x, 20), x)[0],
 "B2H-20": lambda: (lambda p_: p_.coeff(x, 1) + p_.coeff(x, 0))(expand((x - 3) ** 2 - 4)),
 "B2H-21": lambda: Rational(12, 10) ** 2 * Rational(75, 100) * 100,
 "B2H-22": lambda: solve(Eq(2 * x + 3 * x, 90), x)[0],
}

FORM = {
 "B1-06": "(5, -3)",
 "B2E-03": "d=150-3t",
 "B2E-05": "w\\le 3.6",
 "B2H-03": "(10, 4)",
 "B2H-08": "c<18",
 "B2H-17": "between 2,610 and 2,970",
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

# ---------------------------------------------------------------- shape rules
print("== pass 2: shape and house style")
for nm, md in (("Module 1", MODULE_1), ("Module 2 Easy", MODULE_2_EASY), ("Module 2 Hard", MODULE_2_HARD)):
    check(len(md) == 22, f"{nm} has {len(md)}, expected 22")

for name, mod in (("M1", MODULE_1), ("M2E", MODULE_2_EASY), ("M2H", MODULE_2_HARD)):
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
        inside = lambda i: any(lo <= i < hi for lo, hi in spans)

        for mt in re.finditer(r"\^", blk):
            check(inside(mt.start()), f"{tag}: caret outside math mode")
        for mt in re.finditer(r"\bsqrt\s*\(", blk):
            check(False, f"{tag}: plain-text sqrt(")
        for mt in re.finditer(r"[\dA-Za-z)]\s*\*\s*[\dA-Za-z(]", blk):
            check(inside(mt.start()), f"{tag}: asterisk multiplication outside math mode")
        for mt in re.finditer(r"(?<![\d/:])\d+\s*/\s*\d+(?![\d/])", blk):
            check(inside(mt.start()), f"{tag}: slash fraction outside math mode")
        for mt in re.finditer(r"\\(pi|frac|sqrt|cdot|le|ge|ne|circ|sin|cos|tan|log)\b", blk):
            check(inside(mt.start()), f"{tag}: LaTeX macro outside math mode")
        for mt in re.finditer(r"(!=|<=|>=)", blk):
            check(False, f"{tag}: ASCII comparison operator, use \\ne / \\le / \\ge")

        for lo, hi in spans:
            span_text = blk[lo:hi]
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
    for mt in SPAN.findall(t):
        sp = mt[0] or mt[1]
        if "\\frac" in sp: math.append("mathfrac")
        if "\\sqrt" in sp: math.append("mathsqrt")
        if "\\pi" in sp: math.append("mathpi")
        if re.search(r"\^\{?2\}?", sp): math.append("mathsq")
        if re.search(r"\^\{?[a-z]\}?", sp): math.append("mathexpvar")
    t = re.sub(r"\\[a-zA-Z]+", " ", t)
    t = re.sub(r"[-+]?\d[\d,.]*", "#", t)
    return set((re.sub(r"[^a-z#]+", " ", t.lower()).strip() + " " + " ".join(sorted(set(math)))).split())


def jaccard(p, r):
    return len(p & r) / max(1, len(p | r))


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
        print("   warning: prod dump failed:", res.stderr.strip()[:400])
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
