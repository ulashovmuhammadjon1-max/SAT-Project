#!/usr/bin/env python3
"""
Verify the 66 originally-authored Math questions for Test 13.

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
 4. Cross-check against the sibling Test 14 and Test 15 builds, which the
    production pass cannot see because those tests are not shipped yet. The
    sibling sources are read and exec'd, never imported, so nothing (not even a
    __pycache__ entry) is written into another agent's build directory.

Run:  DATABASE_URL='postgresql://...' python3 verify_math_test13.py
      (without DATABASE_URL it verifies everything except the dedupe pass)
"""
import json
import os
import re
import subprocess
import sys
from collections import Counter

from sympy import (Eq, Integer, Rational, solve, sqrt, symbols, simplify,
                   sympify, pi, sin, expand, cancel, log)

from math_test13 import MODULE_1, MODULE_2_EASY, MODULE_2_HARD, ALL

HERE = os.path.dirname(os.path.abspath(__file__))
x, y, k, b, c, n, t, v, s = symbols("x y k b c n t v s")
w, m, p, g, a, d, r, h = symbols("w m p g a d r h")
A_POS = symbols("a", positive=True)
FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)


# ---------------------------------------------------------------- derivations
def f1_01():
    sol = solve([Eq(3 * h + 2 * t, 96), Eq(5 * h + 4 * t, 178)], [h, t])
    return sol[t]


def f1_11():
    roots = solve(Eq(x ** 2 + 4 * x - 12, 3 * x + 8), x)
    return roots[0] * roots[1]


def f2h_01():
    # every solution of 6x-4y=10 also solves 9x+cy=15, so the second equation
    # is a multiple of the first
    lam = Rational(9, 6)
    assert 10 * lam == 15
    return -4 * lam


def f2h_04():
    width = [rr for rr in solve(Eq(w * (w + 3), 154), w) if rr > 0][0]
    return 2 * (width + (width + 3))


def f2h_10():
    # a radical equation: sympy's own solve already discards the extraneous
    # root, but the filter is kept so the derivation stands on its own
    return [rr for rr in solve(Eq(sqrt(2 * x + 11), x + 4), x)
            if simplify(sqrt(2 * rr + 11) - (rr + 4)) == 0][0]


def f2h_09():
    kv = solve(Eq(k * (0 + 2) * (0 - 6), -36), k)[0]
    return kv * (2 + 2) * (2 - 6)


def f2h_21():
    sol = solve([Eq(2 * c + 5 * d, 197), Eq(4 * c + 3 * d, 219)], [c, d])
    return sol[c] + sol[d]


DERIVE = {
 "F1-01": f1_01,
 "F1-02": lambda: solve(Eq(s + (s + 6) + s / 2, 96), s)[0] / 2,
 "F1-03": lambda: solve(Eq(412 + Rational(328 - 412, 12) * (t - 5), 300), t)[0],
 "F1-04": lambda: 45 + 38 * solve(Eq(45 + 24 * r, 141), r)[0],
 "F1-05": lambda: 34 + Rational(124 - 34, 12 - 2) * (20 - 2),
 "F1-06": lambda: max(i for i in range(100) if 26 * i + 14 * 8 <= 300),
 "F1-07": lambda: solve(Eq(3 * v + 2 * (v + 6), 152), v)[0],
 "F1-08": lambda: cancel((6 * x ** 2 + 11 * x - 35) / (3 * x - 5)),
 "F1-09": lambda: Rational(448, 2 * 8),
 "F1-10": lambda: simplify(log(Rational(6250, 50), 5)),
 "F1-11": f1_11,
 "F1-12": lambda: solve(Eq(w, (5 * g - 14) / 3), g)[0],
 "F1-13": lambda: solve(Eq(c * 6 ** 3, 108), c)[0] * 10 ** 3,
 "F1-14": lambda: round(float(2000 * 1.15 ** 5)),
 "F1-15": lambda: Rational(96, 4) * 7 * 3,
 "F1-16": lambda: solve(Eq(Rational(80, 100) * Rational(135, 100) * p, 54), p)[0],
 "F1-17": lambda: Rational((250 - 200) * 100, 200),
 "F1-18": lambda: Rational(14 * 78 - 6 * 62, 8),
 "F1-19": lambda: 3 * solve(Eq(a + 3 * a + (a + 20), 180), a)[0],
 "F1-20": lambda: simplify(15 / sin(pi / 6)) / 2,
 "F1-21": lambda: Rational(448, 4 ** 3),
 "F1-22": lambda: Rational(24, 18) * Rational(315, 10),

 "F2E-01": lambda: Rational(152, 8),
 "F2E-02": lambda: Rational(23 - 5, 3),
 "F2E-03": lambda: 18 + 13 * 5,
 "F2E-04": lambda: 240 - 15 * w,
 "F2E-05": lambda: "no more than 8",
 "F2E-06": lambda: Rational(50 - 14, 4),
 "F2E-07": lambda: "rate of decrease per hour",
 "F2E-08": lambda: expand((5 * m - 8) + (3 * m + 14)),
 "F2E-09": lambda: expand(3 * (2 * x + 5)),
 "F2E-10": lambda: 3 * 4 ** 2,
 "F2E-11": lambda: [rr for rr in solve(Eq(x ** 2 / 50, 8), x) if rr > 0][0],
 "F2E-12": lambda: Rational(5 + 9, 5 - 1),
 "F2E-13": lambda: Integer(16) ** Rational(3, 4),
 "F2E-14": lambda: 3 * 4 ** 3,
 "F2E-15": lambda: Rational(5, 3) * 45,
 "F2E-16": lambda: Rational((250 - 200) * 100, 250),
 "F2E-17": lambda: 84 + 96 + 78 + 102,
 "F2E-18": lambda: sorted([9, 4, 2, 7, 6])[2],
 "F2E-19": lambda: 180 - 35 - 35,
 "F2E-20": lambda: 6 * 4 * 3,
 "F2E-21": lambda: 4 * sqrt(Integer(169)),
 "F2E-22": lambda: sqrt(Integer(5) ** 2 + 12 ** 2),

 "F2H-01": f2h_01,
 "F2H-02": lambda: solve(Eq(17 + Rational(-3 - 17, 6 + 4) * (x + 4), 5), x)[0],
 "F2H-03": lambda: max(i for i in range(1000) if 12 * 30 + 18 * i <= 960),
 "F2H-04": f2h_04,
 "F2H-05": lambda: expand((5 * x - 1) ** 2 + 3),
 "F2H-06": lambda: 3 * x ** 2 + 24 * x + 50,
 "F2H-07": lambda: [rr for rr in solve(Eq((20 - 2 * x) * (16 - 2 * x), 192), x)
                    if 0 < rr < 8][0],
 "F2H-08": lambda: cancel((x ** 2 - 9) / (x ** 2 + 7 * x + 12)),
 "F2H-09": f2h_09,
 "F2H-10": f2h_10,
 "F2H-11": lambda: solve(Eq(Rational(40, 100) * (90 - y) + Rational(70, 100) * y,
                           Rational(60, 100) * 90), y)[0],
 "F2H-12": lambda: "causal claim for the sampled population",
 "F2H-13": lambda: Rational(90, 90 + 120),
 "F2H-14": lambda: (45 * 240 * 16) // 500,
 "F2H-15": lambda: Rational(40 * 25 + 60 * 40 + 50 * 32 + 50 * 50, 10 * 200),
 "F2H-16": lambda: 180 - 2 * (180 - 118),
 "F2H-17": lambda: pi * 3 ** 2 * 5 + Rational(1, 3) * pi * 3 ** 2 * 4,
 "F2H-18": lambda: Rational(3, 5),
 "F2H-19": lambda: min(i for i in range(1, 50) if 8 * i + 5 * 4 >= 60 and i + 4 <= 9),
 "F2H-20": lambda: 27 - 40 * Rational(51 - 27, 100 - 40),
 "F2H-21": f2h_21,
 "F2H-22": lambda: solve(Eq(pi * 6 ** 2 * h, Rational(1, 3) * pi * 9 ** 2 * 4), h)[0],
}

# Structural answers, where the marked choice is a form or a sentence rather
# than a value sympy can compare against.
FORM = {
 "F2E-05": "\\le 8",
 "F2E-07": "decreases each hour",
 "F2H-12": "likely to cause higher assessment scores",
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
        print(f"   WARNING: could not refresh the production dump ({res.stderr.strip()[:200]})")
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
print("== pass 4: cross-check against the sibling Test 14 and Test 15 builds")
for sib_test in ("14", "15"):
    sibling = os.path.abspath(os.path.join(HERE, "..", f"test-{sib_test}-build",
                                           f"math_test{sib_test}.py"))
    if not os.path.exists(sibling):
        print(f"   SKIPPED — ../test-{sib_test}-build/math_test{sib_test}.py does not exist yet")
        continue
    # Read and exec the source rather than importing it: an ordinary import
    # would drop a __pycache__ entry into the other agent's build directory,
    # and this pass must be strictly read-only over there.
    try:
        ns = {"__name__": f"math_test{sib_test}_readonly", "__file__": sibling}
        exec(compile(open(sibling).read(), sibling, "exec"), ns)
        sib = ns["ALL"]
        print(f"   comparing against {len(sib)} unshipped Test {sib_test} Math stems")
        worst_sib = []
        for q in ALL:
            s0 = sig(q["stem"])
            score, label = max(((jaccard(s0, sig(o["stem"])), o["n"]) for o in sib),
                               key=lambda z: z[0])
            worst_sib.append((score, q["n"], label))
            check(score < 0.75,
                  f"{q['n']}: Test {sib_test} similarity {score:.2f} to {label}")
        worst_sib.sort(reverse=True)
        print("   closest matches:")
        for sc, tag, lab in worst_sib[:6]:
            print(f"     {sc:.2f}  {tag}  vs Test {sib_test} {lab}")
    except Exception as exc:  # the sibling may still be mid-write
        print(f"   SKIPPED — could not read the Test {sib_test} build ({exc})")

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
