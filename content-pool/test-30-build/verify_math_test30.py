#!/usr/bin/env python3
"""
Verify the 66 originally-authored Math questions for Test 30.

Four passes, because each has caught a different class of defect in earlier
builds:

 1. Every answer is re-derived with sympy from the question itself, never read
    off the `check` note. A wrong `check` and a wrong key agree with each
    other; only an independent derivation catches that. The pass also asserts
    that no distractor equals the derived value. Anything genuinely outside
    sympy's reach would go in MANUAL with a written justification — Test 30 has
    none, because every answer is a value, an algebraic form, a form built out
    of sympy-computed coefficients, or a named table row picked out by a
    comparison over the printed data.
 2. House style is enforced on the final HTML — the Test 1/2 rules in
    CLAUDE.md, plus the DB-wide rendering checks (no bare `^`, `sqrt(`,
    `*`-as-multiply, slash fractions, ASCII comparison operators or LaTeX
    macros outside a math span).
 3. Template dedupe against every Math stem live in production. The corpus is
    the SHARED one at ../prod_math_stems.json (1,386 stems), not a build-local
    copy. 0.75 fails outright, but the threshold is triage, not a verdict:
    every match at or above 0.45 is printed in full so the nearest banked stem
    can actually be read. Across Tests 18-21, 57 genuine template repeats all
    but three scored BELOW 0.75.
 4. Self-collision among Test 30's own 66 stems, plus a cross-module setting
    check: a student sees Module 1 and one Module 2 branch, so no setting
    keyword may appear in both Module 1 and a Module 2 module.

Run:  python3 verify_math_test30.py
      (no DATABASE_URL needed — pass 3 reads ../prod_math_stems.json)
"""
import json
import os
import re
import sys
from collections import Counter

from sympy import (Abs, Eq, Integer, Rational, ceiling, diff, expand, floor,
                   pi, simplify, solve, sqrt, symbols, sympify, together)

from math_test30 import MODULE_1, MODULE_2_EASY, MODULE_2_HARD, ALL

HERE = os.path.dirname(os.path.abspath(__file__))

# Symbols. Never name one S, E, I, N, O, Q, beta, gamma or zeta and then hand
# it to sympify bare: sympify("S") returns the SingletonRegistry and the
# comparison silently degrades to a string compare. Everything below is either
# built with symbols() explicitly or parsed with an all-letters locals map.
x, y, t, m, n, d, h, k, w = symbols("x y t m n d h k w")
a, b, c, l, p, r, s, u, v = symbols("a b c l p r s u v")

BASE_LOCALS = {ch: symbols(ch) for ch in
               "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"}
POS_LOCALS = dict(BASE_LOCALS)
POS_LOCALS.update({nm: symbols(nm, positive=True) for nm in ("a", "b", "k", "r", "x", "y")})

FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)


# ---------------------------------------------------------------- derivations
def h1_01():
    beds = symbols("beds")
    return solve(Eq(Rational(6, 10) * beds - Rational(4, 10) * beds, 33), beds)[0]


def h1_02():
    per = symbols("per")
    rows = solve(Eq(9 * per + 14, 11 * per - 8), per)[0]
    return 9 * rows + 14


def h1_03():
    pep, lav = symbols("pep lav")
    sol = solve([Eq(pep + lav, 91), Eq(pep, 2 * lav - 14)], [pep, lav])
    return sol[pep]


def h1_06():
    pts = [(20, 148), (35, 253), (50, 358)]
    slope = Rational(pts[1][1] - pts[0][1], pts[1][0] - pts[0][0])
    inter = pts[0][1] - slope * pts[0][0]
    # the third row must lie on the same line, or the item is not linear
    check(slope * pts[2][0] + inter == pts[2][1], "H1-06: table is not linear")
    return f"V = {slope}m + {inter}"


def h1_07():
    return min(i for i in range(1, 400) if 150 + 2 * i < 6 * i)


def h1_10():
    model = Rational(1, 4) * t ** 2 - 8 * t + 102
    top = solve(Eq(diff(model, t), 0), t)[0]
    return model.subs(t, top)


def h1_11():
    x0, y0 = 3, 10
    return f"({x0 + 2}, {y0 + 5})"


def h1_12():
    root = [z for z in solve(Eq(3 * r ** 2, 108), r) if z > 0][0]
    return root + 3 * root


def h1_16():
    base = [34, 41, 47, 52, 58]
    good = []
    for cand in (38, 44, 50, 55):
        six = sorted(base + [cand])
        if Rational(six[2] + six[3], 2) == Rational(99, 2):
            good.append(cand)
    check(len(good) == 1, f"H1-16: {len(good)} of the four choices give a median of 49.5")
    return good[0]


def h1_17():
    def var(vals):
        mu = Rational(sum(vals), len(vals))
        return sum((Rational(z) - mu) ** 2 for z in vals) / len(vals)
    first = [40, 44, 48, 52, 56, 60]
    second = [46, 47, 49, 51, 53, 54]
    check(Rational(sum(first), 6) == Rational(sum(second), 6),
          "H1-17: the two lists do not have the same mean")
    if var(first) > var(second):
        return ("The standard deviation of the first list is greater than the standard "
                "deviation of the second list.")
    if var(second) > var(first):
        return ("The standard deviation of the second list is greater than the standard "
                "deviation of the first list.")
    return "The two lists have the same standard deviation."


def h1_19():
    ht = symbols("ht", positive=True)
    return solve(Eq(Rational(1, 3) * pi * 15 ** 2 * ht, 1125 * pi), ht)[0]


def h1_22():
    scale = 29 / sqrt(Integer(20) ** 2 + Integer(21) ** 2)
    return simplify(Rational(1, 2) * (20 * scale) * (21 * scale))


def h2e_16():
    vals = sorted([24, 31, 28, 35, 27])
    return Integer(vals[len(vals) // 2])


def h2e_18():
    rows = [("Alder", 45), ("Bryony", 62), ("Comfrey", 38), ("Dittany", 57)]
    return Integer(max(z[1] for z in rows) - min(z[1] for z in rows))


def h2h_01():
    xr = symbols("xr", real=True)
    return sum(solve(Eq(Abs(3 * xr - 8), xr + 4), xr))


def h2h_02():
    sol = solve([Eq(y, 4 * x - 7), Eq(2 * x + 3 * y, 35)], [x, y])
    return sol[x] * sol[y]


def h2h_03():
    lg = symbols("lg")
    return solve(Eq(Rational(30, 100) * (620 - lg) + Rational(45, 100) * lg, 231), lg)[0]


def h2h_04():
    wk = symbols("wk")
    return solve(Eq(5400 - r * wk, 3000 - Rational(1, 3) * r * wk), wk)[0]


def h2h_05():
    slope = Rational(3 - 9, 8 - (-4))
    return -5 + slope * (14 - 2)


def h2h_06():
    bound = solve(Eq((2 * x - 7) / 3, (x + 1) / 2), x)[0]
    holds_below = ((2 * 0 - 7) / Integer(3)) <= ((0 + 1) / Integer(2))
    op = "\\le" if holds_below else "\\ge"
    return f"\\(x{op} {bound}\\)"


def h2h_07():
    av = symbols("av")
    # (a-5)x > -20; the inequality reverses only for a < 5, and the boundary is 5
    return solve(Eq(-20 / (av - 5), 5), av)[0]


def h2h_09():
    return expand((3 * x - 7).subs(x, x + 4))


def h2h_10():
    av = symbols("av")
    # a/(x+2) = x  ->  x^2 + 2x - a = 0, one real solution when the discriminant is 0
    quad = expand(x * (x + 2) - av)
    disc = quad.coeff(x, 1) ** 2 - 4 * quad.coeff(x, 2) * quad.coeff(x, 0)
    return solve(Eq(disc, 0), av)[0]


def h2h_11():
    bv, cv = symbols("bv cv")
    bb = solve(Eq(1 + bv + cv, 81 + 9 * bv + cv), bv)[0]
    axis = -bb / 2
    return solve(Eq(axis ** 2 + bb * axis + cv, -7), cv)[0]


def h2h_12():
    sols = solve(Eq(sqrt(2 * x + 11), x - 2), x)
    check(len(sols) == 1, f"H2H-12: sympy returned {sols}, expected a single valid solution")
    return sols[0]


def h2h_13():
    return sum(z for z in solve(Eq(x ** 4 - 13 * x ** 2 + 36, 0), x) if z > 0)


def h2h_15():
    per_clerk = Rational(3, 4) / 5          # sheets each clerk mounts in a minute
    clerks = symbols("clerks")
    return solve(Eq(per_clerk * clerks * 35, 63), clerks)[0]


def h2h_18():
    rows = [("Aldworth", 250, 200), ("Bramfield", 320, 272),
            ("Culworth", 180, 144), ("Denshaw", 400, 312)]
    return max(rows, key=lambda row: Rational(row[2], row[1]))[0]


def h2h_19():
    rad = symbols("rad", positive=True)
    rv = solve(Eq(2 * pi * rad * (2 * rad), 100 * pi), rad)[0]
    return pi * rv ** 2 * (2 * rv)


def h2h_20():
    wd = symbols("wd", positive=True)
    wv = solve(Eq(2 * (wd + 2 * wd), 210), wd)[0]
    return wv * 2 * wv


def h2h_21():
    rad2 = (16 - 4) ** 2 + (2 - (-3)) ** 2
    return pi * rad2


DERIVE = {
 "H1-01": h1_01,
 "H1-02": h1_02,
 "H1-03": h1_03,
 "H1-04": lambda: 268 + 3 * (65 - 40),
 "H1-05": lambda: solve(Eq(9 * t + 45, 4 * (9 * 0 + 45)), t)[0],
 "H1-06": h1_06,
 "H1-07": h1_07,
 "H1-08": lambda: expand((2 * x + 7) ** 2 - (2 * x - 7) ** 2),
 "H1-09": lambda: simplify((x ** 2 - 49) / (x ** 2 - 11 * x + 28)),
 "H1-10": h1_10,
 "H1-11": h1_11,
 "H1-12": h1_12,
 "H1-13": lambda: solve(Eq(5 / (x - 2), 3 / (x + 4)), x)[0],
 "H1-14": lambda: 3 * Rational(220, 8 - 3),
 "H1-15": lambda: (Rational(34, 8) - Rational(60, 15)) * 100,
 "H1-16": h1_16,
 "H1-17": h1_17,
 "H1-18": lambda: Rational(120, 320) * 100,
 "H1-19": h1_19,
 "H1-20": lambda: Rational(3 * 12 * 4, 10 * 10) / Rational(6, 100),
 "H1-21": lambda: Rational(180 - 44, 2) / 2,
 "H1-22": h1_22,

 "H2E-01": lambda: solve(Eq(8 * n + 15, 111), n)[0],
 "H2E-02": lambda: 15 * 24,
 "H2E-03": lambda: Rational(480, 24),
 "H2E-04": lambda: (190 - 8 * d).subs(d, 12),
 "H2E-05": lambda: (9 * x + 40).subs(x, 7),
 "H2E-06": lambda: 640 - 8 * 45,
 "H2E-07": lambda: [z for z in (5, 6, 7, 8) if 5 * z + 3 > 38][0],
 "H2E-08": lambda: expand(6 * (2 * k - 5) + 3 * k),
 "H2E-09": lambda: expand((x + 6) * (x + 4)),
 "H2E-10": lambda: expand((3 * m ** 4) ** 2),
 "H2E-11": lambda: (18 - d ** 2 / 4).subs(d, 6),
 "H2E-12": lambda: (-h ** 2 + 12 * h).subs(h, 5),
 "H2E-13": lambda: [z for z in solve(Eq(x ** 2 + 3, 52), x) if z > 0][0],
 "H2E-14": lambda: 7 * 60,
 "H2E-15": lambda: Rational(2400, 16),
 "H2E-16": h2e_16,
 "H2E-17": lambda: Rational(96 - 36, 96),
 "H2E-18": h2e_18,
 "H2E-19": lambda: 50 * 30 * 6,
 "H2E-20": lambda: 2 * (42 + 26),
 "H2E-21": lambda: 180 - 43 - 68,
 "H2E-22": lambda: Rational(12, 37),

 "H2H-01": h2h_01,
 "H2H-02": h2h_02,
 "H2H-03": h2h_03,
 "H2H-04": h2h_04,
 "H2H-05": h2h_05,
 "H2H-06": h2h_06,
 "H2H-07": h2h_07,
 "H2H-08": lambda: together(1 / a - 1 / b),
 "H2H-09": h2h_09,
 "H2H-10": h2h_10,
 "H2H-11": h2h_11,
 "H2H-12": h2h_12,
 "H2H-13": h2h_13,
 "H2H-14": lambda: (3600 * Rational(6, 10) + 600) * Rational(75, 100),
 "H2H-15": h2h_15,
 "H2H-16": lambda: (Rational(85, 100) * 240 + Rational(70, 100) * 160) / 400 * 100,
 "H2H-17": lambda: (Rational(380, 400) - Rational(260, 400)) * 100,
 "H2H-18": h2h_18,
 "H2H-19": h2h_19,
 "H2H-20": h2h_20,
 "H2H-21": h2h_21,
 "H2H-22": lambda: 1 / symbols("k", positive=True),
}

# Nothing in Test 30 resists a symbolic derivation, so MANUAL is empty and
# pass 1 covers all 66. The four non-numeric answers (a model equation, a
# transformed point, an inequality, a named table row) are still derived: each
# derivation computes the coefficients, the coordinates, the boundary and the
# direction, or the winning row, with sympy, and only then formats the string.
MANUAL = {}

FUNCTION_WORDS = {"sqrt", "pi", "sin", "cos", "tan", "log", "ln", "exp", "Abs"}


def latex_to_expr(text):
    """Turn one answer choice into something sympify can read."""
    tt = text.replace("&deg;", "").replace("&gt;", ">").replace("&lt;", "<")
    tt = re.sub(r"\\left|\\right", "", tt)
    tt = re.sub(r"\\\((.*?)\\\)", r"\1", tt, flags=re.S)
    # Thousands separators go FIRST. \frac{3{,}600}{r} carries braces inside the
    # numerator, so the (non-recursive) \frac pattern cannot match it until the
    # {,} is gone — stripping it later leaves a half-rewritten \frac behind.
    tt = tt.replace("{,}", "").replace(",", "").replace("$", "").replace("%", "")
    # Exponent-inside-fraction and fraction-inside-exponent are both real, and
    # NEITHER fixed order handles both. Alternate to a fixed point instead.
    for _ in range(8):
        before = tt
        tt = re.sub(r"\^\{([^{}]*)\}", r"**(\1)", tt)
        tt = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"((\1)/(\2))", tt)
        if tt == before:
            break
    tt = tt.replace("\\pi", "pi").replace("\\cdot", "*").replace("\\sqrt", "sqrt")
    tt = tt.replace("^", "**").replace("{", "(").replace("}", ")")
    # implicit multiplication: after a digit, after a closing paren, and after a
    # lone symbol — \(x(x+7)\) parses to nonsense without the last of the three,
    # and the lookbehind keeps sqrt( / cos( from being mangled.
    tt = re.sub(r"(\d)\s*([a-zA-Z(])", r"\1*\2", tt)
    tt = re.sub(r"\)\s*\(", ")*(", tt)
    tt = re.sub(r"(?<![a-zA-Z])([a-zA-Z])\s*\(", r"\1*(", tt)

    # A surviving multi-letter run is an implicit product, not a symbol:
    # without this \frac{uv}{u+v} parses as one symbol named uv and the key
    # silently fails to match. Known function names are left alone.
    def split_run(mo):
        run = mo.group(0)
        return run if run in FUNCTION_WORDS else "*".join(run)
    tt = re.sub(r"[a-zA-Z]{2,}", split_run, tt)
    return tt.strip()


def as_expr(text):
    """Parse a choice, trying the plain and the positive-assumption reading.

    symbols("k", positive=True) is a different Symbol from symbols("k"), so a
    single parse can miss a match that is really there, whichever side of the
    comparison happens to carry the assumption.
    """
    out = []
    for loc in (BASE_LOCALS, POS_LOCALS):
        try:
            out.append(sympify(latex_to_expr(text), locals=loc))
        except Exception:
            pass
    return out


def same(expr, got):
    try:
        if simplify(expr - got) == 0:
            return True
    except Exception:
        pass
    try:
        if abs(complex(expr.evalf() - got.evalf())) < 1e-9:
            return True
    except Exception:
        pass
    return False


def matches(text, got):
    for expr in as_expr(text):
        if same(expr, got):
            return True
    return latex_to_expr(text).replace(" ", "") == str(got).replace(" ", "")


print("== pass 1: independent sympy derivation")
derived = 0
for qz in ALL:
    tag = qz["n"]
    if tag in MANUAL:
        continue
    check(tag in DERIVE, f"{tag}: no derivation and not listed in MANUAL")
    if tag not in DERIVE:
        continue
    got = DERIVE[tag]()
    derived += 1

    if qz["type"] == "FR":
        ok = False
        for ans in qz["answers"]:
            try:
                ok = ok or same(sympify(latex_to_expr(ans), locals=BASE_LOCALS), got)
            except Exception:
                ok = ok or ans.strip() == str(got).strip()
        check(ok, f"{tag}: sympy got {got}, accepted answers are {qz['answers']}")
        continue

    text = qz["choices"]["ABCD".index(qz["correct"])]

    if isinstance(got, str):
        # A form, a point, an inequality or a named row: the derivation builds
        # the exact string out of sympy-computed values, so this is still a
        # comparison against a derived result, not against the author's note.
        norm = lambda z: z.replace(" ", "")
        check(norm(text) == norm(got),
              f"{tag}: derived {got!r} but choice {qz['correct']} is {text!r}")
        for i, alt in enumerate(qz["choices"]):
            if i != "ABCD".index(qz["correct"]):
                check(norm(alt) != norm(got),
                      f"{tag}: distractor {'ABCD'[i]} ({alt!r}) equals the key")
        continue

    check(matches(text, got),
          f"{tag}: sympy got {got}, but choice {qz['correct']} is {text!r}")

    for i, alt in enumerate(qz["choices"]):
        if i == "ABCD".index(qz["correct"]):
            continue
        bad = any(same(expr, got) for expr in as_expr(alt))
        check(not bad, f"{tag}: distractor {'ABCD'[i]} ({alt!r}) equals the key")

print(f"   {derived} of {len(ALL)} re-derived with sympy; {len(MANUAL)} in MANUAL")

# ---------------------------------------------------------------- shape rules
print("== pass 2: shape and house style")
for nm, md in (("Module 1", MODULE_1), ("Module 2 Easy", MODULE_2_EASY),
               ("Module 2 Hard", MODULE_2_HARD)):
    check(len(md) == 22, f"{nm} has {len(md)}, expected 22")

for name, mod in (("M1", MODULE_1), ("M2E", MODULE_2_EASY), ("M2H", MODULE_2_HARD)):
    fr = [qq for qq in mod if qq["type"] == "FR"]
    mc = [qq for qq in mod if qq["type"] == "MC"]
    check(len(fr) == 3, f"{name}: {len(fr)} free-response, the target is exactly 3")
    check(len(mc) == 19, f"{name}: {len(mc)} multiple-choice, expected 19")
    dom = Counter(qq["domain"] for qq in mod)
    check(dom["ALG"] == 7 and dom["ADV"] == 6 and dom["PSDA"] == 5 and dom["GT"] == 4,
          f"{name}: domain mix is {dict(dom)}, wanted 7 ALG / 6 ADV / 5 PSDA / 4 GT")
    bal = Counter(qq["correct"] for qq in mc)
    check(max(bal.values()) <= 7, f"{name}: answer key unbalanced {dict(bal)}")
    trig = sum(1 for qq in mod if qq["skill"] == "GT-TR")
    check(1 <= trig <= 2, f"{name}: {trig} GT-TR questions, wanted 1 or 2")

VALID_SKILLS = {
    "ALG": {"ALG-LE", "ALG-LF", "ALG-LI"},
    "ADV": {"ADV-NF", "ADV-EQ", "ADV-NE"},
    "PSDA": {"PSDA-RP", "PSDA-ST", "PSDA-DI"},
    "GT": {"GT-AV", "GT-LA", "GT-TR"},
}

SPAN = re.compile(r"\\\((.*?)\\\)|\\\[(.*?)\\\]", re.S)

seen_ids = set()
styled = 0
for qq in ALL:
    tag = qq["n"]
    check(tag not in seen_ids, f"{tag}: duplicate question id")
    seen_ids.add(tag)
    check(qq["skill"] in VALID_SKILLS[qq["domain"]],
          f"{tag}: skill {qq['skill']} is not a {qq['domain']} skill")
    check(bool(qq.get("check")), f"{tag}: no check note")

    blocks = [qq["stem"]] + list(qq.get("choices") or [])
    styled += 1
    if qq["type"] == "MC":
        check(len(qq["choices"]) == 4, f"{tag}: needs exactly 4 choices")
        check(len(set(qq["choices"])) == 4, f"{tag}: duplicate answer choice")
        check(qq["correct"] in "ABCD", f"{tag}: bad answer label")
    else:
        check(bool(qq.get("answers")), f"{tag}: free response with no accepted answer")
        for ans in qq["answers"]:
            check("," not in ans, f"{tag}: free-response answer {ans!r} carries a comma")

    for blk in blocks:
        bare = re.sub(r"<img[^>]*>", " ", blk)  # base64 payloads match every rule below
        check(not bare.strip().startswith("<p>"), f"{tag}: stem is <p>-wrapped")
        check("\u00b0" not in bare, f"{tag}: raw degree glyph, use &deg;")
        spans = [mm.span() for mm in SPAN.finditer(bare)]
        inside = lambda i: any(aa <= i < bb for aa, bb in spans)

        for mm in re.finditer(r"\^", bare):
            check(inside(mm.start()), f"{tag}: caret outside math mode")
        for mm in re.finditer(r"(?<![A-Za-z])sqrt\s*\(", bare):
            check(False, f"{tag}: plain-text sqrt(")
        for mm in re.finditer(r"[\dA-Za-z)]\s*\*\s*[\dA-Za-z(]", bare):
            check(inside(mm.start()), f"{tag}: asterisk multiplication outside math mode")
        for mm in re.finditer(r"(?<![\d/:])\d+\s*/\s*\d+(?![\d/])", bare):
            check(inside(mm.start()), f"{tag}: slash fraction outside math mode")
        for mm in re.finditer(r"\\(pi|frac|sqrt|cdot|le|ge|ne|circ|sin|cos|tan|log|ln|"
                              r"left|right|overline|text)\b", bare):
            check(inside(mm.start()), f"{tag}: LaTeX macro outside math mode")
        for mm in re.finditer(r"(!=|<=|>=)", bare):
            check(False, f"{tag}: ASCII comparison operator, use \\ne / \\le / \\ge")
        for mm in re.finditer(r"(?<![A-Za-z])(theta|alpha|beta|lambda)(?![A-Za-z])", bare):
            check(inside(mm.start()), f"{tag}: Greek letter spelled out in prose")
        for mm in re.finditer(r"(?<![A-Za-z])pi(?![A-Za-z])", bare):
            check(inside(mm.start()), f"{tag}: bare word pi outside math mode")

        for aa, bb2 in spans:
            span_text = bare[aa:bb2]
            for fn in ("sin", "cos", "tan", "log", "ln"):
                check(not re.search(r"(?<!\\)\b" + fn + r"\b", span_text),
                      f"{tag}: unescaped {fn} inside math mode")
            words = re.findall(r"[A-Za-z]{3,}", re.sub(r"\\[a-zA-Z]+", "", span_text))
            check(len(words) < 2, f"{tag}: prose inside math mode: {span_text!r}")

        # an inline span must not be glued to the surrounding prose
        for mo in re.finditer(r"[A-Za-z0-9]\\\(", bare):
            check(False, f"{tag}: math span opens with no space before it")
        for mo in re.finditer(r"\\\)[A-Za-z0-9]", bare):
            check(False, f"{tag}: math span closes with no space after it")

    if re.search(r"\btables?\b", qq["stem"], re.I):
        check("<table" in qq["stem"], f"{tag}: mentions a table but has no <table> markup")
    if re.search(r"\b(shown|the figure|following (?:graph|figure|chart|table|plot)|"
                 r"graph above|chart|plot)\b", qq["stem"], re.I):
        check("<table" in qq["stem"] or "<img" in qq["stem"],
              f"{tag}: refers to a visual it does not contain")

print(f"   {styled} of {len(ALL)} questions style-checked (stems and every choice)")

# ------------------------------------------------------------------- dedupe
print("== pass 3: template dedupe against production")


def sig(text):
    tt = re.sub(r"<[^>]+>", " ", text)
    tt = re.sub(r"&[a-z]+;", " ", tt)
    math = []
    for mm in SPAN.findall(tt):
        sp = mm[0] or mm[1]
        if "\\frac" in sp: math.append("mathfrac")
        if "\\sqrt" in sp: math.append("mathsqrt")
        if "\\pi" in sp: math.append("mathpi")
        if re.search(r"\^\{?2\}?", sp): math.append("mathsq")
        if re.search(r"\^\{?[a-z]\}?", sp): math.append("mathexpvar")
    tt = re.sub(r"\\[a-zA-Z]+", " ", tt)
    tt = re.sub(r"[-+]?\d[\d,.]*", "#", tt)
    return set((re.sub(r"[^a-z#]+", " ", tt.lower()).strip()
                + " " + " ".join(sorted(set(math)))).split())


def jaccard(aa, bb):
    return len(aa & bb) / max(1, len(aa | bb))


READ_THRESHOLD = 0.45
# The SHARED corpus at the content-pool root, not a build-local copy. READ ONLY.
prod_path = os.path.join(HERE, "..", "prod_math_stems.json")
worst_prod = 0.0
if os.path.exists(prod_path):
    prod = json.load(open(prod_path))
    print(f"   comparing against {len(prod)} live Math stems")
    others = [(pq["label"], sig(re.sub(r"<img[^>]*>", " ", pq["stem"]))) for pq in prod]
    worst = []
    for qq in ALL:
        s0 = sig(qq["stem"])
        score, label = max(((jaccard(s0, o), lab) for lab, o in others), key=lambda z: z[0])
        worst.append((score, qq["n"], label))
        check(score < 0.75, f"{qq['n']}: template similarity {score:.2f} to {label}")
    worst.sort(reverse=True)
    worst_prod = worst[0][0]
    flagged = [row for row in worst if row[0] >= READ_THRESHOLD]
    print(f"   {len(flagged)} match(es) at or above {READ_THRESHOLD:.2f} — read each one:")
    for sc, tag, lab in flagged:
        print(f"     {sc:.2f}  {tag}  vs {lab}")
    print("   next closest:")
    for sc, tag, lab in [row for row in worst if row[0] < READ_THRESHOLD][:6]:
        print(f"     {sc:.2f}  {tag}  vs {lab}")
else:
    check(False, "../prod_math_stems.json is missing — the dedupe pass cannot run")

# ------------------------------------------------------------ self-collision
print("== pass 4: self-collision and cross-module settings")
pairs = []
for i in range(len(ALL)):
    for j in range(i + 1, len(ALL)):
        sc = jaccard(sig(ALL[i]["stem"]), sig(ALL[j]["stem"]))
        pairs.append((sc, ALL[i]["n"], ALL[j]["n"]))
        check(sc < 0.75, f"{ALL[i]['n']} vs {ALL[j]['n']}: internal similarity {sc:.2f}")
pairs.sort(reverse=True)
worst_self = pairs[0][0]
print(f"   {len(pairs)} pairs compared; closest:")
for sc, aa, bb2 in pairs[:5]:
    print(f"     {sc:.2f}  {aa}  vs {bb2}")

# A student sees Module 1 and exactly one Module 2 branch, so a setting reused
# across that boundary shows the same scene twice in one sitting. Module 1 has
# the physic garden and the distilling; both Module 2 branches have the
# apothecary, the herbarium and the seed store.
#
# Every keyword below is a word that has NO ordinary-English sense that could
# make the prefix match fire on the wrong module. Deliberately excluded, and
# the reason each was excluded: "still" (a vessel and an adverb), "press"
# (matches "pressure", "impress"), "drying" and "dried" (ordinary), "grain"
# (a weight and a cereal), "bed"/"sheet"/"lot"/"store"/"case"/"charge"/"dose"
# (all ordinary English). This is the same family as the \bpi bug and the
# "fen" inside "fence": a boundary-free or over-broad substring match in a
# checker is worse than no check.
SETTING_KEYWORDS = [
    # Module 1's territory
    "physic", "alembic", "retort", "distiller", "distilling", "distillation",
    "lavender", "peppermint", "ointment", "infusion", "compost", "cutting",
    "gardener", "garden",
    # Module 2's territory
    "apothecary", "drachm", "herbarium", "germinat", "moisture", "seed",
    "specimen", "sedge", "packet", "pill", "mounting", "mounted",
]
m1_text = " ".join(qq["stem"].lower() for qq in MODULE_1)
m2_text = " ".join(qq["stem"].lower() for qq in MODULE_2_EASY + MODULE_2_HARD)


def has(kwd, text):
    """Prefix match at a word boundary: "seed" catches "seeds", but "print"
    does not catch "footprint" and "moth" would not catch "months" — the kind
    of silent over-match that the \\bpi\\b bug was made of."""
    return re.search(r"\b" + re.escape(kwd), text) is not None


shared = [kwd for kwd in SETTING_KEYWORDS if has(kwd, m1_text) and has(kwd, m2_text)]
check(not shared, f"settings reused across Module 1 and a Module 2 branch: {shared}")
in_m1 = [kwd for kwd in SETTING_KEYWORDS if has(kwd, m1_text)]
in_m2 = [kwd for kwd in SETTING_KEYWORDS if has(kwd, m2_text)]
print(f"   {len(in_m1)} setting keywords in Module 1, {len(in_m2)} in Module 2, "
      f"{len(shared)} shared")

# The scaffolding trap: substituting the Math tag AUTHORED/T18- while leaving
# the R&W tag AUTHORED-T18: stamps the template test's provenance on this one.
for qq in ALL:
    for field in ("stem", "check"):
        check("T18" not in qq.get(field, ""), f"{qq['n']}: a T18 string survives in {field}")

# ------------------------------------------------------------------- report
print()
print(f"questions: {len(ALL)}   M1 domains: {dict(Counter(qq['domain'] for qq in MODULE_1))}")
print(f"                    M2E domains: {dict(Counter(qq['domain'] for qq in MODULE_2_EASY))}")
print(f"                    M2H domains: {dict(Counter(qq['domain'] for qq in MODULE_2_HARD))}")
print(f"skills: {dict(sorted(Counter(qq['skill'] for qq in ALL).items()))}")
print(f"answer key M1:  {dict(sorted(Counter(qq['correct'] for qq in MODULE_1 if qq['type']=='MC').items()))}")
print(f"answer key M2E: {dict(sorted(Counter(qq['correct'] for qq in MODULE_2_EASY if qq['type']=='MC').items()))}")
print(f"answer key M2H: {dict(sorted(Counter(qq['correct'] for qq in MODULE_2_HARD if qq['type']=='MC').items()))}")
print(f"highest Jaccard vs production: {worst_prod:.2f}   within Test 30: {worst_self:.2f}")

if FAIL:
    print(f"\n{len(FAIL)} FAILURES:")
    for f in FAIL:
        print("  -", f)
    raise SystemExit(1)
print("\nALL CHECKS PASSED")
