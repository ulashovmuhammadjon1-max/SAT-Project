#!/usr/bin/env python3
"""
Verify the 66 originally-authored Math questions for Test 11.

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
 4. Cross-check against the sibling Test 12 build, which the production pass
    cannot see because that test is not shipped yet. Read-only.

Run:  DATABASE_URL='postgresql://...' python3 verify_math_test11.py
      (without DATABASE_URL it verifies everything except the dedupe pass)
"""
import json
import os
import re
import subprocess
import sys
from collections import Counter

from sympy import (Eq, Rational, S, solve, sqrt, symbols, simplify, sympify,
                   pi, tan, expand, cancel, log)

from math_test11 import MODULE_1, MODULE_2_EASY, MODULE_2_HARD, ALL

HERE = os.path.dirname(os.path.abspath(__file__))
x, y, k, b, c, n, t, v, s = symbols("x y k b c n t v s")
w, m, p, g, a, d, R, h = symbols("w m p g a d R h")
A_POS = symbols("a", positive=True)
FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)


# ---------------------------------------------------------------- derivations
def d1_02():
    sol = solve([Eq(4 * s + 3 * g, 141), Eq(6 * s + 5 * g, 223)], [s, g])
    return sol[g]


def d1_06():
    sol = solve([Eq(b - 12 * k, 348), Eq(b - 30 * k, 186)], [b, k])
    return sol[b]


def d1_18():
    av = solve(Eq(x + 2 * x + (3 * x - 24), 180), x)[0]
    return max(av, 2 * av, 3 * av - 24)


def d2h_02():
    slope = Rational(13 - (-5), 8 - 2)
    return -5 + slope * (-3 - 2)


def d2h_04():
    return [r for r in solve(Eq((12 + 2 * w) * (8 + 2 * w) - 96, 96), w) if r > 0][0]


def d2h_07():
    return [r for r in solve(Eq(1 / s + 1 / (s - 6), Rational(1, 4)), s) if r > 6][0]


def d2h_15():
    summer = 15200 * Rational(925, 100)
    others = (8400 * Rational(650, 100) + 7600 * Rational(580, 100)
              + 4300 * Rational(420, 100))
    return summer - others


def d2h_20():
    slope = Rational(510 - 342, 10 - 6)
    base = 342 - 6 * slope
    return base + 15 * slope


DERIVE = {
 "D1-01": lambda: solve(Eq(7 * (3 * x) + 18 * x, 1404), x)[0],
 "D1-02": d1_02,
 "D1-03": lambda: 2010 + solve(Eq(3150 + Rational(3614 - 3150, 8) * t, 4020), t)[0],
 "D1-04": lambda: max(i for i in range(200) if 215 + 58 * i <= 840),
 "D1-05": lambda: 380 + solve(Eq(380 + 26 * k, 1290), k)[0] * 41,
 "D1-06": d1_06,
 "D1-07": lambda: solve(Eq(220 + Rational(355 - 220, 9) * t, 1000), t)[0],
 "D1-08": lambda: cancel((10 * x ** 2 + x - 21) / (2 * x + 3)),
 "D1-09": lambda: Rational(540, 2 * 15),
 "D1-10": lambda: simplify(log(Rational(8748, 108), 3)),
 "D1-11": lambda: sum(solve(Eq(x ** 2 - 3 * x - 10, 2 * x - 4), x)),
 "D1-12": lambda: solve(Eq(R, (2 * m + 9) / 4), m)[0],
 "D1-13": lambda: [r for r in solve(Eq(v ** 2 / 800 + Rational(3, 2), Rational(7, 2)), v) if r > 0][0],
 "D1-14": lambda: round(float(4000 * 0.88 ** 4)),
 "D1-15": lambda: Rational(1080, 45) * 2 * 19,
 "D1-16": lambda: solve(Eq(Rational(125, 100) * Rational(88, 100) * p, 264), p)[0],
 "D1-17": lambda: Rational(147 * 100, 84 + 126 + 147 + 63),
 "D1-18": d1_18,
 "D1-19": lambda: simplify(45 / tan(pi / 6)),
 "D1-20": lambda: (S(30) / 6) ** 3,
 "D1-21": lambda: 12 * 86 - 11 * 84,
 "D1-22": lambda: Rational(27 * 15 ** 2, 9 ** 2),

 "D2E-01": lambda: Rational(126, 7),
 "D2E-02": lambda: Rational(27 - 9, 4),
 "D2E-03": lambda: 35 + 22 * 4,
 "D2E-04": lambda: 150 - 18 * w,
 "D2E-05": lambda: "at least 12",
 "D2E-06": lambda: Rational(96, 3) + 9,
 "D2E-07": lambda: "value when draining begins",
 "D2E-08": lambda: expand((6 * b + 9) + (4 * b - 2)),
 "D2E-09": lambda: "factored area",
 "D2E-10": lambda: 5 ** 2 + 2,
 "D2E-11": lambda: [r for r in solve(Eq(5 * t ** 2, 45), t) if r > 0][0],
 "D2E-12": lambda: Rational(120, 4 + 2),
 "D2E-13": lambda: simplify((a ** 4) ** 3),
 "D2E-14": lambda: 5 * 2 ** 4,
 "D2E-15": lambda: Rational(2, 3) * 480,
 "D2E-16": lambda: Rational((460 - 400) * 100, 400),
 "D2E-17": lambda: 65 - 48,
 "D2E-18": lambda: Rational(1 + 3 + 3 + 4 + 9, 5),
 "D2E-19": lambda: 180 - 48 - 79,
 "D2E-20": lambda: Rational(1, 2) * 14 * 6,
 "D2E-21": lambda: 7 ** 3,
 "D2E-22": lambda: sqrt(S(26) ** 2 - 10 ** 2),

 "D2H-01": lambda: solve(Eq(4 * 9, 3 * k), k)[0],
 "D2H-02": d2h_02,
 "D2H-03": lambda: max(i for i in range(1000) if 2 * (2 * i) + 5 * i <= 240),
 "D2H-04": d2h_04,
 "D2H-05": lambda: expand((2 * x - 5) ** 2 + (2 * x - 5)),
 "D2H-06": lambda: 2 * x ** 2 - 16 * x + 35,
 "D2H-07": d2h_07,
 "D2H-08": lambda: simplify((8 * A_POS ** 9) ** Rational(2, 3) / (2 * A_POS ** 3)),
 "D2H-09": lambda: solve(Eq(4, k * (5 - 3) ** 2 - 8), k)[0],
 "D2H-10": lambda: [r for r in solve(Eq(k ** 2 - 4 * 3 * 12, 0), k) if r > 0][0],
 "D2H-11": lambda: solve(Eq(Rational(15, 100) * (500 - y) + Rational(40, 100) * y,
                           Rational(24, 100) * 500), y)[0],
 "D2H-12": lambda: "sample estimate for the population",
 "D2H-13": lambda: Rational(9 * 14 - 8 + 26, 9),
 "D2H-14": lambda: Rational(3600, 12) / 25,
 "D2H-15": d2h_15,
 "D2H-16": lambda: sqrt(S(4) * 9),
 "D2H-17": lambda: Rational(1, 3) * pi * 3 ** 2 * 8,
 "D2H-18": lambda: Rational(5, 13),
 "D2H-19": lambda: min(i for i in range(1000) if 4 * i + 7 * 8 >= 88),
 "D2H-20": d2h_20,
 "D2H-21": lambda: solve(Eq(d / 12 + 2 * d / 8, 4), d)[0],
 "D2H-22": lambda: (Rational(4, 3) * pi * 6 ** 3) / (pi * 2 ** 2 * 3),
}

# Structural answers, where the marked choice is a form or a sentence rather
# than a value sympy can compare against.
FORM = {
 "D2E-05": "\\ge 12",
 "D2E-07": "when draining begins",
 "D2E-09": "x(x+7)",
 "D2H-12": "reasonable to estimate",
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

# ------------------------------------------- pass 4: sibling unshipped build
print("== pass 4: cross-check against the sibling Test 12 build")
sibling = os.path.abspath(os.path.join(HERE, "..", "test-12-build", "math_test12.py"))
if os.path.exists(sibling):
    sys.path.insert(0, os.path.dirname(sibling))
    try:
        import math_test12  # noqa: E402  (read-only import)
        sib = math_test12.ALL
        print(f"   comparing against {len(sib)} unshipped Test 12 Math stems")
        worst12 = []
        for q in ALL:
            s0 = sig(q["stem"])
            score, label = max(((jaccard(s0, sig(o["stem"])), o["n"]) for o in sib),
                               key=lambda z: z[0])
            worst12.append((score, q["n"], label))
            check(score < 0.75, f"{q['n']}: Test 12 similarity {score:.2f} to {label}")
        worst12.sort(reverse=True)
        print("   closest matches:")
        for sc, tag, lab in worst12[:8]:
            print(f"     {sc:.2f}  {tag}  vs Test 12 {lab}")
    except Exception as exc:  # the sibling may still be mid-write
        print(f"   SKIPPED — could not import the Test 12 build ({exc})")
else:
    print("   SKIPPED — ../test-12-build/math_test12.py does not exist yet")

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
