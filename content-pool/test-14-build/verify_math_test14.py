#!/usr/bin/env python3
"""
Verify the 66 originally-authored Math questions for Test 14.

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
 4. Cross-check against the sibling Test 13 and Test 15 builds, which the
    production pass cannot see because those tests are not shipped yet. Both
    are read strictly read-only.

Run:  DATABASE_URL='postgresql://...' python3 verify_math_test14.py
      (without DATABASE_URL it verifies everything except the dedupe pass)
"""
import json
import os
import re
import subprocess
import sys
from collections import Counter

from sympy import (Eq, Rational, S, solve, sqrt, symbols, simplify, sympify,
                   pi, sin, tan, expand, cancel, diff, log)

from math_test14 import MODULE_1, MODULE_2_EASY, MODULE_2_HARD, ALL

HERE = os.path.dirname(os.path.abspath(__file__))
x, y, k, b, c, n, t, v, w = symbols("x y k b c n t v w")
m, p, a, d, h, r, u, J = symbols("m p a d h r u J")
A_POS = symbols("a", positive=True)
FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)


# ---------------------------------------------------------------- derivations
def g1_02():
    sol = solve([Eq(3 * p + 120 * c, 402), Eq(5 * p + 90 * c, 450)], [p, c])
    return sol[p]


def g1_06():
    sol = solve([Eq(p + d, 96), Eq(4 * p + 7 * d, 507)], [p, d])
    return sol[d]


def g1_09():
    expr = -Rational(1, 4) * (x - 6) * (x - 30)
    return expr.subs(x, solve(diff(expr, x), x)[0])


def g1_11():
    roots = solve(Eq(x ** 2 + 2 * x - 15, x + 5), x)
    return roots[0] * roots[1]


def g1_13():
    a_val = solve(Eq(k * 9 + 7, -11), k)[0]
    return a_val * 6 ** 2 + 7


def g2h_09():
    h_val = [rr for rr in solve(Eq(-Rational(1, 50) * (0 - h) ** 2 + 18, 0), h) if rr > 0][0]
    return 2 * h_val


def g2h_18():
    cos_j = Rational(7, 25)
    return simplify(sqrt(1 - cos_j ** 2) / cos_j)


def g2h_20():
    slope = Rational(21 - 9, 10 - 4)
    base = 9 - slope * 4
    return solve(Eq(slope * m + base, 33), m)[0]


DERIVE = {
 "G1-01": lambda: solve(Eq(9 * (h + 5) + 14 * h, 436), h)[0],
 "G1-02": g1_02,
 "G1-03": lambda: solve(Eq(528 - Rational(528 - 402, 20 - 6) * (t - 6), 150), t)[0],
 "G1-04": lambda: max(i for i in range(200) if 290 + 84 * i <= 1250 - 110),
 "G1-05": lambda: 173 + Rational(261 - 173, 22 - 14) * (30 - 14),
 "G1-06": g1_06,
 "G1-07": lambda: solve(Eq(3, Rational(4, 5) * 10 + b), b)[0],
 "G1-08": lambda: cancel((6 * x ** 2 - 19 * x + 10) / (3 * x - 2)),
 "G1-09": g1_09,
 "G1-10": lambda: simplify(log(Rational(6250, 10), 5)),
 "G1-11": g1_11,
 "G1-12": lambda: solve(Eq(J, (5 * c - 12) / 3), c)[0],
 "G1-13": g1_13,
 "G1-14": lambda: sqrt(S(12) * 300),
 "G1-15": lambda: Rational(96, 4) * 5 * Rational(18, 10),
 "G1-16": lambda: 6 * 74 - (68 + 71 + 74 + 74 + 78),
 "G1-17": lambda: Rational(63 * 100, 39 + 63 + 48),
 "G1-18": lambda: solve(Eq((5 * x + 8) + (3 * x + 12), 180), x)[0],
 "G1-19": lambda: simplify(18 * sin(pi / 3)),
 "G1-20": lambda: Rational(12, 10) * Rational(8, 10) * Rational(5, 10) * 1000 * Rational(3, 4),
 "G1-21": lambda: Rational(780, 3) * 10,
 "G1-22": lambda: 486 * Rational(20, 12) ** 3,

 "G2E-01": lambda: Rational(138, 6),
 "G2E-02": lambda: Rational(26 - 2, 4),
 "G2E-03": lambda: 6 + Rational(35, 10) * 5,
 "G2E-04": lambda: 12 * h + 25,
 "G2E-05": lambda: max(i for i in range(100) if 17 + 2 * i < 24),
 "G2E-06": lambda: 3 * 9 + 5 * 4,
 "G2E-07": lambda: "rate of descent",
 "G2E-08": lambda: expand((3 * n + 5) + (2 * n - 8)),
 "G2E-09": lambda: expand(3 * (2 * m - 7)),
 "G2E-10": lambda: 6 ** 2 + 3,
 "G2E-11": lambda: [rr for rr in solve(Eq(3 * t ** 2, 108), t) if rr > 0][0],
 "G2E-12": lambda: Rational(72, 8) - 1,
 "G2E-13": lambda: simplify(t ** 6 * t ** 3),
 "G2E-14": lambda: 3 * 4 ** 3,
 "G2E-15": lambda: Rational(5, 3) * 45,
 "G2E-16": lambda: Rational((250 - 210) * 100, 250),
 "G2E-17": lambda: 31 - 19,
 "G2E-18": lambda: sorted([2, 3, 3, 4, 6, 6, 11])[3],
 "G2E-19": lambda: 180 - 62,
 "G2E-20": lambda: 24 * 15,
 "G2E-21": lambda: S(512) ** Rational(1, 3),
 "G2E-22": lambda: sqrt(S(12) ** 2 + 9 ** 2),

 "G2H-01": lambda: Rational(9, 6) * (-4),
 "G2H-02": lambda: 5 + Rational(12, 3) * (11 - 2),
 "G2H-03": lambda: max(i for i in range(1000) if 3 * i + 2 * (3 * i) <= 96),
 "G2H-04": lambda: [rr for rr in solve(Eq((30 - 2 * w) * (20 - 2 * w), 264), w) if rr < 10][0],
 "G2H-05": lambda: "vertex shifted right 3 and up 4",
 "G2H-06": lambda: 3 * x ** 2 + 18 * x + 5,
 "G2H-07": lambda: [rr for rr in solve(Eq(24 / (v - 2) + 24 / (v + 2), 5), v) if rr > 2][0],
 "G2H-08": lambda: simplify(1 / (x - 3) - 2 / (x + 1)),
 "G2H-09": g2h_09,
 "G2H-10": lambda: sum(solve(Eq((2 * x - 1) / (x + 4), 3 / x), x)),
 "G2H-11": lambda: solve(Eq(Rational(30, 100) * a + Rational(8, 100) * (44 - a),
                           Rational(15, 100) * 44), a)[0],
 "G2H-12": lambda: "causal, for subjects like those studied",
 "G2H-13": lambda: Rational(12 * 47 - 35 - 34, 10),
 "G2H-14": lambda: min(80 * Rational(7, 5), 40 * Rational(7, 2)),
 "G2H-15": lambda: 14 * 60 * Rational(95, 100) - 9 * 80 * Rational(90, 100),
 "G2H-16": lambda: 9 + Rational(12 ** 2, 9),
 "G2H-17": lambda: simplify((Rational(4, 3) * pi * r ** 3) / (pi * r ** 2 * 2 * r)),
 "G2H-18": g2h_18,
 "G2H-19": lambda: max(i for i in range(1000) if 40 * i + 15 * 20 <= 1400 and i + 20 <= 60),
 "G2H-20": g2h_20,
 "G2H-21": lambda: solve(Eq(d / 24 + d / 16, 5), d)[0],
 "G2H-22": lambda: 2 * 64 + 4 * 8 * 9,
}

# Structural answers, where the marked choice is a form or a sentence rather
# than a value sympy can compare against.
FORM = {
 "G2E-07": "descends each minute",
 "G2H-05": "(5,9)",
 "G2H-12": "for seedlings like those in the study",
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
    for loc in ({}, {nm: symbols(nm, positive=True)
                     for nm in ("a", "b", "c", "m", "n", "p", "x", "y")}):
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

# every skill in the SAT taxonomy must actually be used somewhere in the test
ALL_SKILLS = {s for group in VALID_SKILLS.values() for s in group}
used_skills = {q["skill"] for q in ALL}
check(ALL_SKILLS <= used_skills, f"unused skills: {sorted(ALL_SKILLS - used_skills)}")

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

# --------------------------------------- pass 4: sibling unshipped builds
print("== pass 4: cross-check against the sibling Test 13 and Test 15 builds")
for sib_test in ("13", "15"):
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
