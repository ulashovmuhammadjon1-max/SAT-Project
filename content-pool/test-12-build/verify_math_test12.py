#!/usr/bin/env python3
"""
Verify the 66 originally-authored Math questions for Test 12.

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

Run:  DATABASE_URL='postgresql://...' python3 verify_math_test12.py
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

from math_test12 import MODULE_1, MODULE_2_EASY, MODULE_2_HARD, ALL

HERE = os.path.dirname(os.path.abspath(__file__))
x, y, k, b, c, n, t, v, s = symbols("x y k b c n t v s")
A, h, p, g = symbols("A h p g")
a, d, m, w, r, L, Y = symbols("a d m w r L Y")
FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)


# ---------------------------------------------------------------- derivations
SQ = lambda nm: symbols(nm, positive=True)


def e1_02():
    rate = Rational(1240 - 1096, 2017 - 2005)          # metres per year
    return 2017 + Rational(1396 - 1240) / rate


def e1_05():
    rr = solve(Eq(18 - r * 7, Rational(124, 10)), r)[0]
    return 18 - rr * 15


def e1_09():
    wd = max(solve(Eq(x * (x + 7), 330), x))
    return 2 * (wd + (wd + 7))


def e1_17():
    xv = solve(Eq(4 * x + 16, 6 * x - 14), x)[0]
    return 4 * xv + 16


def e1_20():
    sol = solve([Eq(3 * c + 5 * v, 196), Eq(5 * c + 2 * v, 181)], [c, v])
    return sol[c]


def e2h_02():
    sol = solve([Eq(a + 6 * b, 27), Eq(a + 14 * b, 51)], [a, b])
    return sol[a] + sol[b]


def e2h_04():
    return [rt for rt in solve(Eq(1 / s + 1 / (s - 5), Rational(1, 6)), s) if rt > 5][0]


def e2h_06():
    xp, yp = SQ("x"), SQ("y")
    return simplify((16 * xp ** 8 / yp ** -4) ** Rational(3, 4))


def e2h_10():
    """Only one listed value of c gives two distinct real intersections."""
    good = [cv for cv in (-5, -3, -2, 1)
            if discriminant(Poly(x ** 2 - 6 * x + (7 - cv), x)) > 0]
    return good[0] if len(good) == 1 else None


DERIVE = {
 "E1-01": lambda: solve(Eq(9 * (40 - x) + 14 * x, 470), x)[0],
 "E1-02": e1_02,
 "E1-03": lambda: max(i for i in range(400) if 3 * 46 + Rational(275, 100) * i <= 540),
 "E1-04": lambda: solve(Eq(6 * s * 24, 4320), s)[0],
 "E1-05": e1_05,
 "E1-06": lambda: 1410 + Rational(1860 - 1410, 10 - 4) * 10,
 "E1-07": lambda: solve(Eq(Y, (3 * m - 2 * w) / 5), m)[0],
 "E1-08": lambda: solve(Eq(-50 * b + 900, 0), b)[0],
 "E1-09": e1_09,
 "E1-10": lambda: simplify((4 * a ** 3 * b) ** 2 / (8 * a * b ** 4)),
 "E1-11": lambda: round(float(250 * 0.97 ** 8)),
 "E1-12": lambda: max(solve(Eq(t ** 2 - 30 * t + 200, 0), t)),
 "E1-13": lambda: Rational(140, 8) * 3,
 "E1-14": lambda: Rational(9, 10) * 400 * 7,
 "E1-15": lambda: (Rational(240, 10) - Rational(155, 10)) * Rational(180, 100),
 "E1-16": lambda: 10 * 63 - 9 * 62,
 "E1-17": e1_17,
 "E1-18": lambda: "45 tan 52 degrees",
 "E1-19": lambda: Rational(15, 10) ** 2 * Rational(24, 10) * Rational(8, 10),
 "E1-20": e1_20,
 "E1-21": lambda: Rational(30 ** 2, 20) + Rational(30, 2),
 "E1-22": lambda: solve(Eq(Rational(30, 60), h / 400), h)[0],

 "E2E-01": lambda: solve(Eq(14 * x, 322), x)[0],
 "E2E-02": lambda: Rational(546, 7),
 "E2E-03": lambda: 18 + 7 * 4,
 "E2E-04": lambda: 45 - 9 * 3,
 "E2E-05": lambda: "fewer than 9",
 "E2E-06": lambda: solve(Eq(24 * h, 180), h)[0],
 "E2E-07": lambda: expand(4 * (3 * n - 7) + 5 * n),
 "E2E-08": lambda: simplify(x ** 4 * x ** 2),
 "E2E-09": lambda: 7 ** 2 + 5,
 "E2E-10": lambda: 3 * 2 ** 4,
 "E2E-11": lambda: [rt for rt in solve(Eq(p ** 2 - 9, 40), p) if rt > 0][0],
 "E2E-12": lambda: expand((x + 4) * (x - 9)),
 "E2E-13": lambda: Rational(5, 2) * 14,
 "E2E-14": lambda: Rational(35, 100) * 420,
 "E2E-15": lambda: 155 - 96,
 "E2E-16": lambda: Rational(4 + 5 + 5 + 6 + 7 + 9, 6),
 "E2E-17": lambda: 90 - 37,
 "E2E-18": lambda: 35 ** 2,
 "E2E-19": lambda: (pi * 6 ** 2) / pi,
 "E2E-20": lambda: Rational(45, 10) / 6,
 "E2E-21": lambda: 5 * 6 ** 2,
 "E2E-22": lambda: Rational(15, 8),

 "E2H-01": lambda: solve(Eq(3 / m, Rational(3, 5)), m)[0],
 "E2H-02": e2h_02,
 "E2H-03": lambda: max(i for i in range(18) if 32 * (17 - i) + 19 * i >= 460),
 "E2H-04": e2h_04,
 "E2H-05": lambda: expand((2 * x - 5) ** 2 + 1),
 "E2H-06": e2h_06,
 "E2H-07": lambda: [bb for bb in solve(Eq(b ** 2 - 4 * 2 * 18, 0), b) if bb > 0][0],
 "E2H-08": lambda: cancel((x ** 2 - 9) / (x ** 2 + x - 12)),
 "E2H-09": lambda: solve(Eq(a * (10 - 4) ** 2 - 12, 15), a)[0],
 "E2H-10": e2h_10,
 "E2H-11": lambda: solve(Eq(a / (-3), Rational(8, 4)), a)[0],
 "E2H-12": lambda: "random assignment supports causation",
 "E2H-13": lambda: "mean above median",
 "E2H-14": lambda: solve(Eq(Rational(12, 100) * (45 - y) + Rational(30, 100) * y,
                           Rational(18, 100) * 45), y)[0],
 "E2H-15": lambda: Rational(21, 13 + 21),
 "E2H-16": lambda: Rational(12, 12 + 18) * 45,
 "E2H-17": lambda: (Rational(4, 3) * pi * 6 ** 3) / (pi * 2 ** 2 * 9),
 "E2H-18": lambda: Rational(9, sqrt(S(9) ** 2 + 40 ** 2)),
 "E2H-19": lambda: min(i for i in range(21) if 6 * i + 4 * (20 - i) >= 90),
 "E2H-20": lambda: solve(Eq(3 * b + b + (3 * b - 400), 3800), b)[0],
 "E2H-21": lambda: solve(Eq(9 + Rational(-7 - 9, 6 + 2) * (x + 2), 0), x)[0],
 "E2H-22": lambda: Rational((40 + 60) * 30, 2) * 200 / 1000,
}

FORM = {
 "E1-18": "\\tan 52",
 "E2E-05": "n<9",
 "E2H-12": "caused greater gains in flexibility",
 "E2H-13": "mean is greater than the median",
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
    # `8x^{6}y^{3}` becomes `8*x**(6)y**(3)`; without this the implicit product
    # after a closing paren is a syntax error and the choice silently fails to
    # parse, which reads as a wrong answer rather than a parse bug.
    t = re.sub(r"\)\s*([a-zA-Z])", r")*\1", t)
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
          f"{tag}: skill {q['skill']} does not belong to domain {q['domain']}")

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
        for mm in re.finditer(r"\\(pi|frac|sqrt|cdot|le|ge|ne|circ|sin|cos|tan|log|overline)\b", blk):
            check(inside(mm.start()), f"{tag}: LaTeX macro outside math mode")
        for mm in re.finditer(r"(!=|<=|>=)", blk):
            check(False, f"{tag}: ASCII comparison operator, use \\ne / \\le / \\ge")
        for mm in re.finditer(r"(?<![A-Za-z])(pi|theta|alpha|beta)(?![A-Za-z])", blk):
            check(inside(mm.start()), f"{tag}: Greek letter spelled out in prose")

        for aa, bnd in spans:
            span_text = blk[aa:bnd]
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


def jaccard(aset, bset):
    return len(aset & bset) / max(1, len(aset | bset))


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
