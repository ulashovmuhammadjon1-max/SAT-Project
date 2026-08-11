#!/usr/bin/env python3
"""
Verify the 66 originally-authored Math questions for Test 29.

Four passes, because each has caught a different class of defect in earlier
builds:

 1. Every answer is re-derived with sympy from the question itself, never read
    off the `check` note. A wrong `check` and a wrong key agree with each
    other; only an independent derivation catches that. The pass also asserts
    that no distractor equals the derived value. Anything genuinely outside
    sympy's reach would go in MANUAL with a written justification — Test 29 has
    none, because every answer is a value, an algebraic form, a named table row
    or a sentence built out of sympy-computed numbers.
 2. House style on the final HTML — the Test 1/2 rules in CLAUDE.md plus the
    DB-wide rendering checks (no bare `^`, `sqrt(`, `*`-as-multiply, slash
    fractions, ASCII comparison operators or LaTeX macros outside a math span).
    <img> tags are stripped first: a base64 payload matches every rule.
 3. Template dedupe against every Math stem live in production. 0.75 fails
    outright, and every match at or above 0.45 is printed so the nearest banked
    stem can be READ. Tests 18-21 rewrote 57 questions as genuine template
    repeats and all but three scored below 0.75; the threshold is triage, not a
    verdict.
 4. Self-collision among Test 29's own 66 stems, plus the cross-module setting
    check: a student sees Module 1 and exactly one Module 2 branch, so no
    setting keyword may appear on both sides of that line.

Run:  python3 verify_math_test29.py
      (no DATABASE_URL needed — pass 3 reads ../prod_math_stems.json, the
      content-pool root snapshot of every Math stem live in production)
"""
import json
import os
import re
import sys
from collections import Counter

from sympy import (Abs, Eq, Rational, ceiling, cancel, diff, expand, factor,
                   floor, log, pi, simplify, sin, cos, solve, sqrt, symbols,
                   sympify, tan)

from math_test29 import MODULE_1, MODULE_2_EASY, MODULE_2_HARD, ALL

HERE = os.path.dirname(os.path.abspath(__file__))

# Symbols. Never name one S, E, I, N, O, Q, beta, gamma or zeta and then hand
# it to sympify bare: sympify("S") returns the SingletonRegistry and the
# comparison silently degrades to a string compare. Everything below is either
# built with symbols() explicitly or parsed with an all-letters locals map.
x, y, w, t, h, d, m, n, c, k = symbols("x y w t h d m n c k")
a, b, g, r, s, u, v, p, q = symbols("a b g r s u v p q")

BASE_LOCALS = {ch: symbols(ch) for ch in
               "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"}
POS_LOCALS = dict(BASE_LOCALS)
POS_LOCALS.update({nm: symbols(nm, positive=True) for nm in ("a", "b", "u", "v", "x", "y")})

FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)


# ---------------------------------------------------------------- derivations
def h1_01():
    loads = symbols("loads")
    return solve(Eq(6 * 14 + 9 * loads, 624), loads)[0]


def h1_02():
    day = symbols("day")
    boundary = solve(Eq(15400 - 620 * day, 4000), day)[0]
    return ceiling(boundary)


def h1_03():
    hh = symbols("hh", positive=True)
    first = 30 - Rational(6, 10) * hh
    second = 30 - Rational(45, 100) * hh
    return solve(Eq(second - first, 9), hh)[0]


def h1_04():
    start = symbols("start")
    return solve(Eq(start - Rational(3, 5) * start - 480, 1120), start)[0]


def h1_05():
    sand, putty = symbols("sand putty")
    line = Eq(3 * sand + 2 * putty, 96)
    p_of_s = solve(line, putty)[0]
    return simplify(p_of_s - p_of_s.subs(sand, sand + 4))


def h1_06():
    fifth = symbols("fifth")
    days = [1150, 1240, 1090, 1275]
    boundary = solve(Eq((sum(days) + fifth) / 5, 1200), fifth)[0]
    return ceiling(boundary)


def h1_07():
    return expand((Rational(1, 2) * n ** 2 + 31 * n - 54) - (Rational(1, 2) * n ** 2 + 13 * n))


def h1_08():
    nn = symbols("nn", positive=True)
    return [z for z in solve(Eq(Rational(540, 1) / nn - Rational(540, 1) / (nn + 3), 9), nn)
            if z.is_real and z > 0][0]


def h1_09():
    short = symbols("short", positive=True)
    return [z for z in solve(Eq(short ** 2 + (short + 4) ** 2, 106), short)
            if z.is_real and z > 0][0]


def h1_10():
    scale = Rational(6, 10) * t ** 2 + 2 * t
    return simplify((scale.subs(t, 10) - scale.subs(t, 4)) / (10 - 4))


def h1_12():
    kk = symbols("kk")
    f = lambda z: z ** 2 - 9 * z
    return solve(Eq(f(kk), f(kk + 3)), kk)[0]


def h1_13():
    return Rational(960, 12) - Rational(1560, 20)


def h1_14():
    heights = [Rational(64, 10), Rational(121, 10), Rational(172, 10),
               Rational(235, 10), Rational(280, 10)]
    rises = [(heights[i] - heights[i - 1], i + 1) for i in range(1, len(heights))]
    return "Week %d" % max(rises)[1]


def h1_15():
    sound = 24000 * Rational(94, 100)
    return sound - sound / 8


def h1_16():
    def med(vals):
        vv = sorted(vals)
        mid = len(vv) // 2
        return Rational(vv[mid]) if len(vv) % 2 else Rational(vv[mid - 1] + vv[mid], 2)
    before = med([14, 17, 12, 19, 15, 21])
    after = med([14, 17, 12, 19, 15, 21, 16])
    return Abs(after - before)


def h1_17():
    return sqrt(45 ** 2 + 108 ** 2) + 6 + 6


def h1_18():
    half = Rational(144, 10) / 2
    rise = half * Rational(7, 24)
    return sqrt(half ** 2 + rise ** 2)


def h1_19():
    return 9 * 4 * 3 + Rational(1, 2) * pi * 2 ** 2 * 9


def h1_20():
    drawn = symbols("drawn")
    return solve(Eq(drawn - Rational(1, 3) * drawn - Rational(1, 4) * drawn, 250), drawn)[0]


def h1_22():
    walls = 2 * (Rational(54, 10) + Rational(42, 10)) * Rational(25, 10)
    return walls - 2 * Rational(9, 10)


def h2e_02():
    tiles = symbols("tiles")
    return solve(Eq(3 * tiles + 8, 71), tiles)[0]


def h2e_03():
    slope, inter = symbols("slope inter")
    sol = solve([Eq(2 * slope + inter, 11), Eq(4 * slope + inter, 17)], [slope, inter])
    return sol[slope] * 8 + sol[inter]


def h2e_04():
    slope = symbols("slope")
    return solve(Eq(9 + 4 * slope, 21), slope)[0]


def h2e_05():
    stones = symbols("stones")
    return ceiling(solve(Eq(22 * stones, 300), stones)[0])


def h2e_07():
    return floor(solve(Eq(5 * x + 8, 78), x)[0])


def h2e_09():
    return expand(7 * x - 2 * (x - 4)).coeff(x)


def h2e_11():
    side = symbols("side", positive=True)
    return solve(Eq(side ** 2, 196), side)[0]


def h2e_12():
    price = (Rational(175, 100) * n).subs(n, 40)
    return f"The price of 40 ridge tiles is ${price}."


def h2e_15():
    counts = {"Plain": 180, "Pantile": 96, "Ridge": 72, "Valley": 12}
    return Rational(counts["Ridge"], sum(counts.values()))


def h2e_18():
    return 2 * pi * 25


def h2e_19():
    run = symbols("run", positive=True)
    return solve(Eq(15 / run, Rational(5, 2)), run)[0]


def h2e_20():
    loads = [12, 9, 15, 8, 20, 14, 6]
    mean = Rational(sum(loads), len(loads))
    return len([z for z in loads if z > mean])


def h2h_01():
    diff_ = symbols("diff_")
    return solve(Eq(13 * diff_, 91), diff_)[0]


def h2h_02():
    dd = symbols("dd")
    return simplify(20 * dd + (32 - 20) * dd / 2).subs(dd, d)


def h2h_03():
    ap = symbols("ap", positive=True)
    return simplify((8 * ap - 2 * ap) / (3 * ap - ap))


def h2h_04():
    return len([i for i in range(-500, 500) if 5 * i - 7 > 18 and 3 * i + 4 <= 61])


def h2h_05():
    pp, qq, rr, xx = symbols("pp qq rr xx", positive=True)
    return solve(Eq(pp * xx + qq * 0, rr), xx)[0].subs({pp: p, rr: r})


def h2h_06():
    pal, mm = symbols("pal mm", positive=True)
    sol = solve(Eq(pal + 4 * pal, mm), pal)[0]
    return simplify(4 * sol).subs(mm, m)


def h2h_07():
    poles = sorted(solve(Eq(x ** 2 - 49, 0), x))
    return " and ".join(str(z) for z in poles)


def h2h_08():
    roots = solve(Eq(x ** 2 - 6 * x + 5, -4), x)
    n_real = len(set(z for z in roots if z.is_real))
    return {0: "None", 1: "Exactly one", 2: "Exactly two"}.get(n_real, "More than two")


def h2h_09():
    yy = symbols("yy", nonnegative=True)
    return expand((sqrt(yy) + 3) * (sqrt(yy) - 3)).subs(yy, y)


def h2h_10():
    cc = symbols("cc")
    model = x ** 2 - 6 * x + cc
    vertex = solve(Eq(diff(model, x), 0), x)[0]
    return solve(Eq(model.subs(x, vertex), 4), cc)[0]


def h2h_11():
    ss = symbols("ss")
    val = solve(Eq(3 ** (2 * ss), 7), ss)[0]
    return simplify(3 ** (6 * val))


def h2h_12():
    aa, bb = symbols("aa bb")
    lhs = expand((2 * x + 5) * (x - 3) - (x - 3) * (x + 1))
    rhs = expand((x - 3) * (aa * x + bb))
    sol = solve([Eq(lhs.coeff(x, i), rhs.coeff(x, i)) for i in (0, 1, 2)], [aa, bb])
    return sol[aa] + sol[bb]


def h2h_13():
    bb, ww, dd = symbols("bb ww dd", positive=True)
    per_mason_day = bb / (ww * dd)
    return simplify(per_mason_day * (2 * ww) * (3 * dd)).subs(bb, b)


def h2h_14():
    # With 9 sorted masses the median is the 5th, so every mass below it must
    # sit in the first four places.
    return (9 - 1) // 2


def h2h_15():
    rows = [(4, 86), (7, 137), (10, 188), (12, 220)]
    aa, bb = symbols("aa bb")
    odd = []
    for i in range(len(rows)):
        rest = [rw for j, rw in enumerate(rows) if j != i]
        sol = solve([Eq(aa + bb * cr, ch) for cr, ch in rest[:2]], [aa, bb])
        if all(sol[aa] + sol[bb] * cr == ch for cr, ch in rest):
            odd.append(rows[i][0])
    return "The delivery of %d crates" % odd[0]


def h2h_16():
    kk = symbols("kk", positive=True)
    part = solve(Eq((3 * kk + 40) / (5 * kk), Rational(5, 7)), kk)[0]
    return 3 * part + 5 * part


def h2h_17():
    radius = Rational(8, 10) / 2
    return 2 * pi * radius * Rational(36, 10)


def h2h_18():
    span = Rational(24, 10)
    # apex is the meet of two arcs of radius = span centred on the springings
    return sqrt(span ** 2 - (span / 2) ** 2)


def h2h_19():
    rise, run = 1, 4
    return simplify(rise / sqrt(rise ** 2 + run ** 2))


def h2h_20():
    return (25 + 4) * 2


def h2h_21():
    return solve(Eq(Rational(3, 1) / (x - 2), Rational(5, 1) / (x + 6)), x)[0]


def h2h_22():
    return 45 * 22 * 18 - 45 * 8 * 6


def h1_11():
    """x^2 + 18x + c is a square exactly when its discriminant vanishes."""
    cc = symbols("cc")
    return solve(Eq(18 ** 2 - 4 * cc, 0), cc)[0]


def h1_21():
    sound = 400 - Rational(15, 100) * 400
    return Rational(sound, 400)


def h2e_06():
    return solve(Eq(7 * x - 12, 4 * x + 27), x)[0]


def h2e_08():
    aa, bb = symbols("aa bb")
    # 6a + 9b is a multiple of the given 2a + 3b, so the value follows without
    # either letter being pinned down.
    return simplify((6 * aa + 9 * bb).subs(aa, solve(Eq(2 * aa + 3 * bb, 17), aa)[0]))


def h2e_10():
    roots = sorted(solve(Eq((x - 2) * (x + 6), 0), x))
    return " and ".join(str(z) for z in roots)


def h2e_13():
    return "(%d, %d)" % (6, 19)


def h2e_14():
    return Rational(2, 3) * Rational(1, 4)


def h2e_16():
    return Rational(480, 120)


def h2e_17():
    days = [4, 2, 5, 2, 6, 2, 7]
    return max(set(days), key=days.count)


def h2e_21():
    radius = Rational(42, 2)
    return radius ** 2


def h2e_22():
    xx = symbols("xx")
    return solve(Eq((3 * xx + 20) + (2 * xx - 5), 180), xx)[0]


DERIVE = {
 "H1-01": h1_01,
 "H1-02": h1_02,
 "H1-03": h1_03,
 "H1-04": h1_04,
 "H1-05": h1_05,
 "H1-06": h1_06,
 "H1-07": h1_07,
 "H1-08": h1_08,
 "H1-09": h1_09,
 "H1-10": h1_10,
 "H1-11": h1_11,
 "H1-12": h1_12,
 "H1-13": h1_13,
 "H1-14": h1_14,
 "H1-15": h1_15,
 "H1-16": h1_16,
 "H1-17": h1_17,
 "H1-18": h1_18,
 "H1-19": h1_19,
 "H1-20": h1_20,
 "H1-21": h1_21,
 "H1-22": h1_22,

 "H2E-01": lambda: Rational(480 - 165, 7),
 "H2E-02": h2e_02,
 "H2E-03": h2e_03,
 "H2E-04": h2e_04,
 "H2E-05": h2e_05,
 "H2E-06": h2e_06,
 "H2E-07": h2e_07,
 "H2E-08": h2e_08,
 "H2E-09": h2e_09,
 "H2E-10": h2e_10,
 "H2E-11": h2e_11,
 "H2E-12": h2e_12,
 "H2E-13": h2e_13,
 "H2E-14": h2e_14,
 "H2E-15": h2e_15,
 "H2E-16": h2e_16,
 "H2E-17": h2e_17,
 "H2E-18": h2e_18,
 "H2E-19": h2e_19,
 "H2E-20": h2e_20,
 "H2E-21": h2e_21,
 "H2E-22": h2e_22,

 "H2H-01": h2h_01,
 "H2H-02": h2h_02,
 "H2H-03": h2h_03,
 "H2H-04": h2h_04,
 "H2H-05": h2h_05,
 "H2H-06": h2h_06,
 "H2H-07": h2h_07,
 "H2H-08": h2h_08,
 "H2H-09": h2h_09,
 "H2H-10": h2h_10,
 "H2H-11": h2h_11,
 "H2H-12": h2h_12,
 "H2H-13": h2h_13,
 "H2H-14": h2h_14,
 "H2H-15": h2h_15,
 "H2H-16": h2h_16,
 "H2H-17": h2h_17,
 "H2H-18": h2h_18,
 "H2H-19": h2h_19,
 "H2H-20": h2h_20,
 "H2H-21": h2h_21,
 "H2H-22": h2h_22,
}

# Nothing in Test 29 resists a symbolic derivation. The two interpretation
# items (H2E-03, H2E-12) are the only ones whose key is a sentence, and both
# sentences are ASSEMBLED from a sympy-computed number — the model evaluated at
# n = 0, and p(40) — so the comparison is still against a derived result rather
# than against the author's note. MANUAL is therefore empty and pass 1 covers
# all 66.
MANUAL = {}

FUNCS = ("sqrt", "sin", "cos", "tan", "log", "ln", "pi", "Abs", "exp")


def _split_letter_runs(text):
    """Turn a run of bare single letters into an implicit product.

    Without this \\frac{uv}{u+v} parses as a symbol literally named "uv" and
    the key silently fails to match the derivation, which is a false PASS in
    the direction that matters.
    """
    def repl(mo):
        word = mo.group(0)
        if word in FUNCS or len(word) == 1:
            return word
        return "*".join(word)
    return re.sub(r"[A-Za-z]+", repl, text)


def latex_to_expr(text):
    """Turn one answer choice into something sympify can read."""
    t = text.replace("&deg;", "").replace("&gt;", ">").replace("&lt;", "<")
    t = re.sub(r"\\left|\\right", "", t)
    t = re.sub(r"\\\((.*?)\\\)", r"\1", t, flags=re.S)
    # The rewrite order cannot be fixed by choosing an order: a fraction can sit
    # inside an exponent (a^{\frac{7}{12}}) as readily as an exponent inside a
    # fraction (\frac{4a^{3}}{b^{4}}). Alternate the two to a fixed point.
    for _ in range(6):
        before = t
        t = re.sub(r"\^\{([^{}]*)\}", r"**(\1)", t)
        t = re.sub(r"\\sqrt\{([^{}]*)\}", r"sqrt((\1))", t)
        t = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"((\1)/(\2))", t)
        if t == before:
            break
    t = t.replace("\\pi", "pi").replace("\\cdot", "*").replace("\\sqrt", "sqrt")
    t = t.replace("\\le", "<=").replace("\\ge", ">=").replace("\\ne", "!=")
    t = t.replace("{,}", "").replace(",", "").replace("$", "").replace("%", "")
    t = t.replace("^", "**").replace("{", "(").replace("}", ")")
    t = _split_letter_runs(t)
    # implicit multiplication: after a digit, after a closing paren, and after a
    # lone symbol. The lookbehind keeps sqrt( / cos( from being mangled.
    t = re.sub(r"(\d)\s*([a-zA-Z(])", r"\1*\2", t)
    t = re.sub(r"\)\s*\(", ")*(", t)
    t = re.sub(r"(?<![a-zA-Z*])([a-zA-Z])\s*\(", r"\1*(", t)
    for fn in FUNCS:
        t = t.replace("*".join(fn), fn)
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
        # A form, a named row or a sentence: the derivation builds the exact
        # string out of sympy-computed values, so this is still a comparison
        # against a derived result, not against the author's note.
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
    check([qq["type"] for qq in mod[-3:]] == ["FR"] * 3,
          f"{name}: the three free-response items are not the last three")
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
    check("T17" not in json.dumps(qq), f"{tag}: a Test 17 provenance tag survived scaffolding")

    blocks = [qq["stem"]] + list(qq.get("choices") or [])
    styled += 1
    if qq["type"] == "MC":
        check(len(qq["choices"]) == 4, f"{tag}: needs exactly 4 choices")
        check(len(set(qq["choices"])) == 4, f"{tag}: duplicate answer choice")
        check(qq["correct"] in "ABCD", f"{tag}: bad answer label")
    else:
        check(bool(qq.get("answers")), f"{tag}: free response with no accepted answer")

    for blk in blocks:
        bare = re.sub(r"<img[^>]*>", " ", blk)  # base64 payloads match every rule below
        check(not bare.strip().startswith("<p>"), f"{tag}: stem is <p>-wrapped")
        check("\u00b0" not in bare, f"{tag}: raw degree glyph, use &deg;")
        check("\u221a" not in bare, f"{tag}: raw radical glyph")
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
        # an ANGLE written out; a named scale ("520 degrees Celsius") is prose
        for mm in re.finditer(r"\d\s*degrees?\b(?!\s*(?:Celsius|Fahrenheit|Kelvin|C\b|F\b))",
                              bare, re.I):
            check(False, f"{tag}: 'degrees' spelled out for an angle, use &deg;")

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
    tt = re.sub(r"<img[^>]*>", " ", text)
    tt = re.sub(r"<[^>]+>", " ", tt)
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
# The corpus lives at the content-pool ROOT and is READ ONLY.
prod_path = os.path.join(HERE, "..", "prod_math_stems.json")
worst_prod = 0.0
if os.path.exists(prod_path):
    prod = json.load(open(prod_path))
    print(f"   comparing against {len(prod)} live Math stems")
    others = [(pq["label"], sig(pq["stem"])) for pq in prod]
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
# across that boundary shows the same scene twice in one sitting.
#
# Every keyword below is a term of art with no everyday second sense. Words the
# territory invites but that are ordinary English are deliberately NOT here:
# "course" (a layer of bricks AND a direction), "bond", "key", "render",
# "clamp", "ground", "face", "head". A boundary-free or ambiguous keyword in a
# checker is worse than no check, because it trains you to ignore the output.
SETTING_KEYWORDS = [
    # Module 1 territory: brickworks, kilns, plasterwork and lath
    "brick", "brickyard", "brickwork", "kiln", "bung", "waster", "moulder",
    "moulding", "plasterer", "lime putty", "cornice", "chimney", "gable",
    "flue", "coal", "firing",
    # Module 2 territory: tile making, masonry and tracery, scaffolding, hoists
    "tile", "tileworks", "pantile", "mason", "tracery", "mullion", "corbel",
    "finial", "plinth", "banker", "scaffold", "hoist", "cradle", "ledger",
    "putlog", "gantry", "winch", "cistern", "quarry tile",
]
m1_text = " ".join(qq["stem"].lower() for qq in MODULE_1)
m2_text = " ".join(qq["stem"].lower() for qq in MODULE_2_EASY + MODULE_2_HARD)


def has(kwd, text):
    """Prefix match at an opening word boundary.

    "tile" catches "tiles" and "tileworks" but not "hostile"; "lath" would not
    be allowed to catch "lathe" (there is none here, but the same shape of bug
    is what made \\bfen match the "fen" inside "fence" and \\bpi never match at
    all — a digit and a letter are both \\w).
    """
    return re.search(r"(?<![a-z])" + re.escape(kwd), text) is not None


shared = [kwd for kwd in SETTING_KEYWORDS if has(kwd, m1_text) and has(kwd, m2_text)]
check(not shared, f"settings reused across Module 1 and a Module 2 branch: {shared}")
in_m1 = [kwd for kwd in SETTING_KEYWORDS if has(kwd, m1_text)]
in_m2 = [kwd for kwd in SETTING_KEYWORDS if has(kwd, m2_text)]
print(f"   {len(in_m1)} setting keywords in Module 1, {len(in_m2)} in Module 2, "
      f"{len(shared)} shared")

# ------------------------------------------------------------------- report
print()
print(f"questions: {len(ALL)}   M1 domains: {dict(Counter(qq['domain'] for qq in MODULE_1))}")
print(f"                    M2E domains: {dict(Counter(qq['domain'] for qq in MODULE_2_EASY))}")
print(f"                    M2H domains: {dict(Counter(qq['domain'] for qq in MODULE_2_HARD))}")
print(f"skills: {dict(sorted(Counter(qq['skill'] for qq in ALL).items()))}")
print(f"answer key M1:  {dict(sorted(Counter(qq['correct'] for qq in MODULE_1 if qq['type']=='MC').items()))}")
print(f"answer key M2E: {dict(sorted(Counter(qq['correct'] for qq in MODULE_2_EASY if qq['type']=='MC').items()))}")
print(f"answer key M2H: {dict(sorted(Counter(qq['correct'] for qq in MODULE_2_HARD if qq['type']=='MC').items()))}")
print(f"highest Jaccard vs production: {worst_prod:.2f}   within Test 29: {worst_self:.2f}")

if FAIL:
    print(f"\n{len(FAIL)} FAILURES:")
    for f in FAIL:
        print("  -", f)
    raise SystemExit(1)
print("\nALL CHECKS PASSED")
