#!/usr/bin/env python3
"""
Verify the 66 originally-authored Math questions for Test 25.

Four passes, because each has caught a different class of defect in earlier
builds:

 1. Every answer is re-derived with sympy from the question itself, never read
    off the `check` note. A wrong `check` and a wrong key agree with each
    other; only an independent derivation catches that. The pass also asserts
    that no distractor equals the derived value. Anything genuinely outside
    sympy's reach would go in MANUAL with a written justification — Test 25
    has none, because every answer is a value, an algebraic form, or a named
    table row picked out by a comparison over the printed data.
 2. House style on the final HTML — the Test 1/2 rules in CLAUDE.md plus the
    DB-wide rendering checks (no bare `^`, `sqrt(`, `*`-as-multiply, slash
    fractions, ASCII comparison operators or LaTeX macros outside a math span).
    <img> tags are stripped first; a base64 payload matches every rule below.
 3. Template dedupe against every Math stem live in production — the ROOT
    corpus ../prod_math_stems.json, 1,386 stems, not a per-directory copy.
    0.75 fails outright, and every match at or above 0.45 is PRINTED so the
    nearest banked stem can be read. Across Tests 18-21, 57 questions were
    rewritten as genuine template repeats and all but three scored BELOW 0.75:
    a repeat that changes the setting words while keeping the mathematics
    scores low precisely because it changed the words.
 4. Self-collision among Test 25's own 66 stems, plus a setting check: a
    student sees Module 1 and exactly one Module 2 branch, so no setting
    keyword may appear in both Module 1 and a Module 2 module.

Run:  python3 verify_math_test25.py
"""
import json
import os
import re
import sys
from collections import Counter

from sympy import (Abs, Eq, Rational, atan, ceiling, diff, floor, cancel, expand,
                   nsimplify, pi, simplify, sin, cos, solve, sqrt, symbols,
                   sympify, tan, together)

from math_test25 import MODULE_1, MODULE_2_EASY, MODULE_2_HARD, ALL

HERE = os.path.dirname(os.path.abspath(__file__))

# Symbols. Never name one S, E, I, N, O, Q, beta, gamma or zeta and then hand
# it to sympify bare: sympify("S") returns the SingletonRegistry and the
# comparison silently degrades to a string compare. Everything below is either
# built with symbols() explicitly or parsed with an all-letters locals map.
x, y, w, t, h, d, m, n, c, k = symbols("x y w t h d m n c k")
a, b, g, r, s, u, v, p, q = symbols("a b g r s u v p q")
M_ = symbols("M")
XP = symbols("x", positive=True)

BASE_LOCALS = {ch: symbols(ch) for ch in
               "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"}
POS_LOCALS = dict(BASE_LOCALS)
POS_LOCALS.update({nm: symbols(nm, positive=True) for nm in ("a", "b", "x", "y", "w", "M", "r")})

FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)


# ---------------------------------------------------------------- derivations
def m1_01():
    tt = symbols("tt")
    return solve(Eq(8 * (tt + 15), 11 * tt), tt)[0]


def m1_02():
    hrs = symbols("hrs")
    # 35 hours at 16 dollars, every further hour at 24
    return solve(Eq(35 * 16 + 24 * (hrs - 35), 824), hrs)[0]


def m1_03():
    rate = symbols("rate")
    wound = 4180 + 20 * 260
    return solve(Eq(wound + 40 * rate, 15380), rate)[0]


def m1_04():
    fifth = symbols("fifth")
    return solve(Eq((4 * 940 + fifth) / 5, 960), fifth)[0]


def m1_05():
    total = symbols("total")
    wove = Rational(3, 5) * total
    cartridge = Rational(2, 5) * total
    return solve(Eq(wove - cartridge, 84), total)[0]


def m1_06():
    cart = symbols("cart")
    return solve(Eq(5 * cart - 36, 3 * cart), cart)[0]


def m1_07():
    quires = symbols("quires")
    return solve(Eq(40 * 9 + Rational(6, 10) * quires, 540), quires)[0]


def m1_09():
    rows = [(1, 18), (3, 6), (5, 6), (7, 18)]
    pair = [(xa, xb) for i, (xa, fa) in enumerate(rows)
            for xb, fb in rows[i + 1:] if fa == fb and xa != xb]
    lo, hi = min(pair, key=lambda z: z[1] - z[0])
    return Rational(lo + hi, 2)


def m1_10():
    return [z for z in solve(Eq(n ** 2 + 18 * n, 63 * n), n) if z > 0][0]


def m1_08():
    side = symbols("side")
    roots = solve(Eq(side ** 2, x ** 2 - 14 * x + 49), side)
    # for x > 7 the side length is the root with a positive x-coefficient
    return 4 * [rt for rt in roots if rt.coeff(x) > 0][0]


def m1_11():
    # the piecewise rule read straight off the stem
    f = lambda z: 3 * z + 7 if z < 5 else z ** 2 - 4
    return sympify(f(6) - f(2))


def m1_13():
    fx = x ** 2 + 2 * x
    return simplify((fx.subs(x, 5) - fx.subs(x, 1)) / (5 - 1))


def m1_15():
    before = [78, 79, 80, 81, 96]
    after = [78, 79, 80, 81, 82]
    mean = lambda vs: Rational(sum(vs), len(vs))
    median = lambda vs: sorted(vs)[len(vs) // 2]
    sgn = lambda z: (1 if z > 0 else 0) - (1 if z < 0 else 0)
    key = (sgn(mean(after) - mean(before)), sgn(median(after) - median(before)))
    return {(-1, 0): "The mean decreases and the median is unchanged.",
            (0, -1): "The mean is unchanged and the median decreases.",
            (-1, -1): "Both the mean and the median decrease.",
            (0, 0): "Both the mean and the median are unchanged."}[key]


def m1_16():
    laid = 765 - (310 + 95 + 220)
    return laid * Rational(1250, 100)


def m1_19():
    area = pi / 4 * (900 ** 2 - 100 ** 2)          # square millimetres
    length_mm = area / Rational(1, 10)             # 0.10 mm thick
    metres = length_mm / 1000
    return floor(metres + Rational(1, 2))          # nearest whole metre


def m1_20():
    part = symbols("part")
    unit = solve(Eq((2 + 3 + 7) * part, 180), part)[0]
    return 7 * unit


def m1_21():
    ef = symbols("ef")
    # tan A = BC/AC and tan D = EF/DF, and the two tangents are equal
    return solve(Eq(Rational(8, 15), ef / 45), ef)[0]


def m2e_02():
    return solve(Eq(Rational(1, 4) * (3 * x + 1), 7), x)[0]


def m2e_05():
    return [z for z in (3, 4, 6, 8) if z > 4 and 3 * z < 21][0]


def m2e_10():
    kk = symbols("kk")
    return solve(Eq(3 ** 2 + kk, 14), kk)[0]


def m2e_11():
    rails = symbols("rails", positive=True)
    return solve(Eq(rails ** 2 + 5, 41), rails)[0]


def m2e_12():
    return max(solve(Eq(x ** 2 - 9, 0), x))


def m2e_13():
    ss = symbols("ss", positive=True)
    return solve(Eq(ss ** 3, 125), ss)[0]


def m2e_16():
    vals = [24, 31, 24, 40, 24, 31, 52]
    return Counter(vals).most_common(1)[0][0]


def m2h_01():
    sk = symbols("sk")
    return solve(Eq(90 + 6 * sk, 9 * sk), sk)[0]


def m2h_02():
    cc = symbols("cc")
    return solve(Eq(4 * (20 - cc), 3 * 20 + 8), cc)[0]


def m2h_03():
    slope = Rational(0 - (-8), 12 - 0)
    return solve(Eq(slope * x - 8, -2), x)[0]


def m2h_04():
    # 3x - a > 12  <=>  x > (12+a)/3 ; that boundary is stated to be 9
    aa = symbols("aa")
    return solve(Eq(Rational(1, 3) * (12 + aa), 9), aa)[0]


def m2h_05():
    mins = symbols("mins")
    return solve(Eq((18 - 11) * mins, 154), mins)[0]


def m2h_06():
    rr, ww, MM = symbols("rr ww MM", positive=True)
    val = solve(Eq(MM, ww * (1 + rr / 100)), rr)[0]
    return val.subs({MM: symbols("M"), ww: symbols("w")})


def m2h_07():
    return max(Rational(xv - yv, yv) for xv in (2, 6) for yv in (1, 4))


def m2h_08():
    xv = solve(Eq(2 * x - 1, 7), x)[0]
    return (6 * x + 5).subs(x, xv)


def m2h_09():
    # a+b+c is the value of the expanded quadratic at x = 1
    return expand((3 * x - 4) ** 2 - (2 * x - 4) * (2 * x + 4)).subs(x, 1)


def m2h_10():
    return [z for z in solve(Eq((24 + 2 * w) * (18 + 2 * w), 616), w) if z > 0][0]


def m2h_11():
    aa = symbols("aa")
    # f(x-4) vanishes where its argument is the original intercept
    return solve(Eq(aa - 4, 6), aa)[0]


def m2h_12():
    xp = symbols("xp", positive=True)
    root = solve(Eq(xp + 1 / xp, 5), xp)[0]
    return simplify(root ** 2 + 1 / root ** 2)


def m2h_13():
    kk = symbols("kk")
    # 3 is a root, so k follows; the other root then follows from k
    kval = solve(Eq(3 ** 2 - kk * 3 + 18, 0), kk)[0]
    return [z for z in solve(Eq(x ** 2 - kval * x + 18, 0), x) if z != 3][0]


def m2h_14():
    hrs = symbols("hrs", positive=True)
    return solve(Eq(4 * 15, 6 * hrs), hrs)[0]


def m2h_15():
    vals = symbols("v0:7")
    total = solve(Eq(sum(vals) / 7, 24), vals[0])[0] + sum(vals[1:])
    return simplify(sum(3 * vv - 5 for vv in vals).subs(vals[0], total - sum(vals[1:])) / 7)


def m2h_16():
    old = [81, 54, 45]
    return Rational(old[0], sum(old)) * 100


def m2h_17():
    f = symbols("f")
    return solve(Eq(30 * f + 18 * (1 - f), 22), f)[0]


def m2h_18():
    kk = symbols("kk")
    vermilion = 60 * Rational(2, 5)
    return solve(Eq(vermilion / (60 + kk), Rational(1, 3)), kk)[0]


def m2h_19():
    return 20 ** 2 - pi * (Rational(20, 2)) ** 2


def m2h_20():
    a_side, b_side = 9, 14
    return [c for c in (4, 5, 18, 23) if b_side - a_side < c < b_side + a_side][0]


def m2h_21():
    half_base = Rational(48, 2)
    height = sqrt(26 ** 2 - half_base ** 2)
    return height / 26


def m2h_22():
    litres = 24 * 5
    return Rational(litres * 1000, 80 * 50)


DERIVE = {
 "M1-01": m1_01,
 "M1-02": m1_02,
 "M1-03": m1_03,
 "M1-04": m1_04,
 "M1-05": m1_05,
 "M1-06": m1_06,
 "M1-07": m1_07,
 "M1-08": m1_08,
 "M1-09": m1_09,
 "M1-10": m1_10,
 "M1-11": m1_11,
 "M1-12": lambda: solve(Eq(a - 3, 12), a)[0],
 "M1-13": m1_13,
 "M1-14": lambda: Rational(320 * 60 * 42 * 80, 10 * 1000),
 "M1-15": m1_15,
 "M1-16": m1_16,
 "M1-17": lambda: Rational(198, 12) - Rational(310, 20),
 "M1-18": lambda: Rational(27, 18 + 27 + 15),
 "M1-19": m1_19,
 "M1-20": m1_20,
 "M1-21": m1_21,
 "M1-22": lambda: (210 + 12) * (297 + 2 * 9),

 "M2E-01": lambda: solve(Eq(4 * s + 35, 155), s)[0],
 "M2E-02": m2e_02,
 "M2E-03": lambda: (45 - 3 * m).subs(m, 8),
 "M2E-04": lambda: (Rational(65, 10) - Rational(4, 10) * h).subs(h, 0),
 "M2E-05": m2e_05,
 "M2E-06": lambda: solve(Eq(2 * p + 5, 47), p)[0],
 "M2E-07": lambda: solve(Eq(3 * q + 7, 34), q)[0],
 "M2E-08": lambda: expand((x + 7) ** 2),
 "M2E-09": lambda: expand(4 * a + 9 * b - a + 2 * b),
 "M2E-10": m2e_10,
 "M2E-11": m2e_11,
 "M2E-12": m2e_12,
 "M2E-13": m2e_13,
 "M2E-14": lambda: Rational(3, 10) * 40,
 "M2E-15": lambda: Rational(45, 60),
 "M2E-16": m2e_16,
 "M2E-17": lambda: 46 + 9 + 17 + 28,
 "M2E-18": lambda: Rational(18, 18 + 27),
 "M2E-19": lambda: 2 * (8 * 5 + 8 * 3 + 5 * 3),
 "M2E-20": lambda: Rational(1, 2) * 14 * 9,
 "M2E-21": lambda: Rational(46, 24 - 1),
 "M2E-22": lambda: simplify(9 / cos(pi / 4)),

 "M2H-01": m2h_01,
 "M2H-02": m2h_02,
 "M2H-03": m2h_03,
 "M2H-04": m2h_04,
 "M2H-05": m2h_05,
 "M2H-06": m2h_06,
 "M2H-07": m2h_07,
 "M2H-08": m2h_08,
 "M2H-09": m2h_09,
 "M2H-10": m2h_10,
 "M2H-11": m2h_11,
 "M2H-12": m2h_12,
 "M2H-13": m2h_13,
 "M2H-14": m2h_14,
 "M2H-15": m2h_15,
 "M2H-16": m2h_16,
 "M2H-17": m2h_17,
 "M2H-18": m2h_18,
 "M2H-19": m2h_19,
 "M2H-20": m2h_20,
 "M2H-21": m2h_21,
 "M2H-22": m2h_22,
}

# Nothing in Test 25 resists a symbolic derivation, so MANUAL is empty and
# pass 1 covers all 66. If an item ever has to go in here it needs a written
# justification, not just an entry.
MANUAL = {}


def latex_to_expr(text):
    """Turn one answer choice into something sympify can read."""
    t = text.replace("&deg;", "").replace("&gt;", ">").replace("&lt;", "<")
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"\\left|\\right", "", t)
    t = re.sub(r"\\\((.*?)\\\)", r"\1", t, flags=re.S)
    # An exponent can sit inside a fraction (\frac{4a^{3}}{b^{4}}) as readily as
    # a fraction inside an exponent (a^{\frac{7}{12}}), so NEITHER fixed order
    # works. Alternate the two rewrites and iterate to a fixed point.
    for _ in range(8):
        before = t
        t = re.sub(r"\^\{([^{}]*)\}", r"**(\1)", t)
        t = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"((\1)/(\2))", t)
        if t == before:
            break
    t = t.replace("\\pi", "pi").replace("\\cdot", "*").replace("\\sqrt", "sqrt")
    t = t.replace("{,}", "").replace(",", "").replace("$", "").replace("%", "")
    t = t.replace("^", "**").replace("{", "(").replace("}", ")")
    # A choice written as an equation ("r=\frac{100(M-w)}{w}") is compared on its
    # right-hand side; every distractor in such a set carries the same "r=".
    t = re.sub(r"^\s*[A-Za-z]\s*=\s*", "", t)
    # implicit multiplication: after a digit, after a closing paren, and after a
    # lone symbol — \(x(x+7)\) parses to nonsense without the last of the three,
    # and the lookbehind keeps sqrt( / cos( from being mangled.
    t = re.sub(r"(\d)\s*([a-zA-Z(])", r"\1*\2", t)
    t = re.sub(r"\)\s*\(", ")*(", t)
    t = re.sub(r"(?<![a-zA-Z])([a-zA-Z])\s*\(", r"\1*(", t)
    # A surviving multi-letter run is an implicit product, not one symbol:
    # without this \frac{uv}{u+v} parses as a symbol named "uv" and the key
    # silently fails to match. Known function names are left alone.
    t = re.sub(r"(?<![a-zA-Z_])(?!sqrt|sin|cos|tan|log|exp|abs|pi)([a-zA-Z]{2,})(?![a-zA-Z_(])",
               lambda mo: "*".join(mo.group(1)), t)
    return t.strip()


def as_expr(text):
    """Parse a choice, trying the plain and the positive-assumption reading.

    symbols("y", positive=True) is a different Symbol from symbols("y"), so a
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
        # A named row: the derivation picks it out of the printed data with a
        # comparison, so this is still a check against a derived result.
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
    check("T19" not in json.dumps(qq), f"{tag}: a Test 19 provenance string survived")
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

    for blk in blocks:
        bare = re.sub(r"<img[^>]*>", " ", blk)
        check(not bare.strip().startswith("<p>"), f"{tag}: stem is <p>-wrapped")
        check("\u00b0" not in bare, f"{tag}: raw degree glyph, use &deg;")
        check(not re.search(r"\d\s*degrees?\b(?!\s*(?:Celsius|Fahrenheit|Kelvin))", bare),
              f"{tag}: 'degrees' spelled out instead of &deg;")
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
        for mm in re.finditer(r"\\(pi|frac|sqrt|cdot|le|ge|ne|times|div|circ|sin|cos|tan|log|ln|"
                              r"left|right|overline|text)\b", bare):
            check(inside(mm.start()), f"{tag}: LaTeX macro outside math mode")
        for mm in re.finditer(r"(!=|<=|>=)", bare):
            check(False, f"{tag}: ASCII comparison operator, use \\ne / \\le / \\ge")
        for mm in re.finditer(r"(?<![A-Za-z\\])(theta|alpha|beta|lambda|mu|sigma)(?![A-Za-z])",
                              bare):
            check(inside(mm.start()), f"{tag}: Greek letter spelled out in prose")
        for mm in re.finditer(r"(?<![A-Za-z\\])pi(?![A-Za-z])", bare):
            check(inside(mm.start()), f"{tag}: bare word pi outside math mode")
        for mm in re.finditer(r"(?<!\\)\b(sin|cos|tan|log|ln)\s*\(", bare):
            check(False, f"{tag}: bare function call")

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

# -------------------------------------------------------------------- dedupe
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
prod_path = os.path.join(HERE, "..", "prod_math_stems.json")
worst_prod = 0.0
if os.path.exists(prod_path):
    prod = json.load(open(prod_path))
    print(f"   comparing against {len(prod)} live Math stems (root corpus)")
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
    for sc, tag, lab in [row for row in worst if row[0] < READ_THRESHOLD][:8]:
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
# across that boundary shows the same scene twice in one sitting.
#
# Every keyword below is a trade noun with no everyday sense. Words that mean
# something ordinary as well — "ink" is fine but "size", "leaf", "board",
# "gathering", "ground", "press", "sheet", "laid" and "weld" are not — are
# deliberately absent: a checker that over-matches is worse than no checker.
SETTING_KEYWORDS = [
    # Module 1: papermaking and the bindery
    "paper", "papermaking", "pulp", "beater", "couching", "ream", "quire",
    "grammage", "guillotine", "bindery", "reel", "stationer", "cartridge",
    "blotting", "wove", "mill", "fore-edge", "web",
    # Module 2 branches: dye house, ink and pigment, marbling
    "dye", "dyed", "dyeing", "dyer", "skein", "madder", "alum", "indigo",
    "mordant", "pigment", "ink", "vermilion", "ochre", "verdigris",
    "lampblack", "ultramarine", "muller", "marbling", "marbler", "colourman",
    "watercolour", "scarlet", "trough", "liquor",
]
m1_text = " ".join(qq["stem"].lower() for qq in MODULE_1)
m2_text = " ".join(qq["stem"].lower() for qq in MODULE_2_EASY + MODULE_2_HARD)


def has(kwd, text):
    """Whole word or simple plural, with explicit lookarounds on both sides.

    A prefix match is what produced the "fen" inside "fence" false positive and
    the `\\bpi` false negative in earlier builds; requiring a non-letter on each
    side means "mill" does not match "millimetres" and "ink" does not match
    "inking".
    """
    return re.search(r"(?<![a-z])" + re.escape(kwd) + r"(?:e?s)?(?![a-z])", text) is not None


shared = [kwd for kwd in SETTING_KEYWORDS if has(kwd, m1_text) and has(kwd, m2_text)]
check(not shared, f"settings reused across Module 1 and a Module 2 branch: {shared}")
in_m1 = [kwd for kwd in SETTING_KEYWORDS if has(kwd, m1_text)]
in_m2 = [kwd for kwd in SETTING_KEYWORDS if has(kwd, m2_text)]
print(f"   {len(in_m1)} setting keywords in Module 1, {len(in_m2)} in Module 2, "
      f"{len(shared)} shared")

# --------------------------------------------------------------------- report
print()
print(f"questions: {len(ALL)}   M1 domains: {dict(Counter(qq['domain'] for qq in MODULE_1))}")
print(f"                    M2E domains: {dict(Counter(qq['domain'] for qq in MODULE_2_EASY))}")
print(f"                    M2H domains: {dict(Counter(qq['domain'] for qq in MODULE_2_HARD))}")
print(f"skills: {dict(sorted(Counter(qq['skill'] for qq in ALL).items()))}")
for nm, mod in (("M1", MODULE_1), ("M2E", MODULE_2_EASY), ("M2H", MODULE_2_HARD)):
    print(f"answer key {nm}: "
          f"{dict(sorted(Counter(qq['correct'] for qq in mod if qq['type']=='MC').items()))}")
print(f"highest Jaccard vs production: {worst_prod:.2f}   within Test 25: {worst_self:.2f}")

if FAIL:
    print(f"\n{len(FAIL)} FAILURES:")
    for f in FAIL:
        print("  -", f)
    raise SystemExit(1)
print("\nALL CHECKS PASSED")
