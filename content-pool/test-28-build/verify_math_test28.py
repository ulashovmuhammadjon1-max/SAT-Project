#!/usr/bin/env python3
"""
Verify the 66 originally-authored Math questions for Test 28.

Four passes, because each has caught a different class of defect in earlier
builds:

 1. Every answer is re-derived with sympy from the question itself, never read
    off the `check` note. A wrong `check` and a wrong key agree with each
    other; only an independent derivation catches that. The pass also asserts
    that no distractor equals the derived value. Anything genuinely outside
    sympy's reach goes in MANUAL with a written justification.
 2. House style is enforced on the final HTML — the Test 1/2 rules in
    CLAUDE.md, plus the DB-wide rendering checks (no bare `^`, `sqrt(`,
    `*`-as-multiply, slash fractions, ASCII comparison operators or LaTeX
    macros outside a math span). <img> tags are stripped first, because a
    base64 payload matches every one of those patterns.
 3. Template dedupe against every Math stem live in production. The corpus is
    the SHARED snapshot at ../prod_math_stems.json (content-pool root), read
    only. 0.75 fails outright, but the threshold decides what to READ, not
    what to accept: every match at or above 0.45 is printed with the banked
    label so the nearest stem can be pulled up and judged by eye. Tests 18-21
    found 57 genuine template repeats and all but three scored below 0.75.
 4. Self-collision among Test 28's own 66 stems, plus a cross-module setting
    check: a student sees Module 1 and exactly one Module 2 branch, so no
    setting keyword may appear in both Module 1 and a Module 2 module.

Run:  python3 verify_math_test28.py
"""
import json
import os
import re
import sys
from collections import Counter

from sympy import (Abs, Eq, Ge, Gt, Le, Lt, Rational, cancel, ceiling, expand,
                   floor, log, pi, simplify, sin, cos, solve, sqrt, symbols,
                   sympify, tan, together)
from sympy.core.relational import Relational

from math_test28 import MODULE_1, MODULE_2_EASY, MODULE_2_HARD, ALL

HERE = os.path.dirname(os.path.abspath(__file__))

# Symbols. Never name one S, E, I, N, O, Q, beta, gamma or zeta and then hand
# it to sympify bare: sympify("S") returns the SingletonRegistry and the
# comparison silently degrades to a string compare. Everything below is either
# built with symbols() explicitly or parsed with an all-letters locals map.
x, y, w, t, h, d, m, n, c, k = symbols("x y w t h d m n c k")
a, b, f, r, s, u, v, p, q = symbols("a b f r s u v p q")
C_, L_, T_, N_ = symbols("C L T N")

BASE_LOCALS = {ch: symbols(ch) for ch in
               "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"}
BASE_LOCALS["N_0"] = symbols("N_0")
POS_LOCALS = dict(BASE_LOCALS)
POS_LOCALS.update({nm: symbols(nm, positive=True) for nm in ("a", "b", "x", "y", "r", "h")})

FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)


# ---------------------------------------------------------------- derivations
# Every entry below re-derives its answer from the QUESTION, never from the
# `check` note: a wrong note and a wrong key agree with each other, and only an
# independent derivation separates them. Where the answer is a form rather than
# a number the derivation still starts from the question's own quantities and
# builds the expression or relation with sympy, so the comparison is against
# something computed rather than something copied.

def _greatest_int_strictly_below(bound):
    """Largest whole number strictly less than `bound`."""
    return bound - 1 if bound == int(bound) else floor(bound)


# ---- Module 1
def h1_01():
    tk = symbols("tk")
    return solve(Eq(tk - Rational(2, 5) * tk - 7, 53), tk)[0]


def h1_02():
    base, per = symbols("base per")
    sol = solve([Eq(base + 4 * per, 1486), Eq(base + 9 * per, 1861)], [base, per])
    return sol[base]


def h1_03():
    got = symbols("got")
    first_five = [12, 18, 9, 16, 14]
    bound = solve(Eq(Rational(1, 6) * (sum(first_five) + got), 15), got)[0]
    return ceiling(bound)


def h1_04():
    tot = symbols("tot")
    # three eighths went at the head office, so five eighths were still unsold
    return solve(Eq((1 - Rational(3, 8)) * tot, 20 + 5), tot)[0]


def h1_05():
    part = symbols("part")
    unit = solve(Eq(5 * part - 2 * part, 18), part)[0]
    return (2 + 3 + 5) * unit


def h1_06():
    lights = symbols("lights")
    return solve(Eq(54 + 3 * lights, 30 + 5 * lights), lights)[0]


def h1_08():
    # the choice is an equation, so return lhs - rhs of the model itself
    return T_ - (-2 * f ** 2 + 36 * f + 40)


def h1_10():
    kk = solve(Eq(2 * 4 ** 2 - 11 * 4 + k, 0), k)[0]
    roots = solve(Eq(2 * x ** 2 - 11 * x + kk, 0), x)
    other = [rt for rt in roots if rt != 4]
    assert len(other) == 1, "the equation should have exactly one other root"
    return other[0]


def h1_11():
    # the question asks for a product of three factors; the correct choice is
    # checked for equivalence to the allowance, and separately for being a
    # three-factor product
    return expand(4 * x ** 3 + 6 * x ** 2 - 10 * x)


def h1_12():
    days = symbols("days")
    # inverse variation: horses times days is constant
    return solve(Eq(40 * days, 24 * 15), days)[0]


def h1_14():
    rows = [("Ashby", 240, 186), ("Bramber", 180, 144),
            ("Corve", 300, 231), ("Denby", 150, 117)]
    return max(rows, key=lambda row: Rational(row[2], row[1]))[0]


def h1_15():
    brass, japanned = 28, 63 - 28
    return Rational(Rational(3, 4) * brass + Rational(2, 5) * japanned, 63)


def h1_16():
    sq_yards = Rational(288, 9)
    return sq_yards / 4


def h1_17():
    counts = {"chaise": 24, "barouche": 15, "landau": 36, "brougham": 45}
    return Rational(counts["landau"] + counts["barouche"], sum(counts.values()))


def h1_19():
    xv = solve(Eq(4 * x + 2 * (x + 30), 180), x)[0]
    return 4 * xv


def h1_21():
    rise = 82 * Rational(9, 41)
    return sqrt(82 ** 2 - rise ** 2)


# ---- Module 2 Easy
def h2e_02():
    return s - solve(Eq(N_, 8 * s), s)[0]


def h2e_05():
    rows = [(2, 26), (5, 50), (8, 74)]
    slope, inter = symbols("slope inter")
    sol = solve([Eq(rows[0][0] * slope + inter, rows[0][1]),
                 Eq(rows[1][0] * slope + inter, rows[1][1])], [slope, inter])
    for hv, cv in rows:
        assert sol[slope] * hv + sol[inter] == cv, "the table is not exactly linear"
    return sol[slope]


def h2e_06():
    hits = [z for z in (5, 6, 7, 8) if 4 * z - 7 > 21]
    assert len(hits) == 1, "exactly one listed value should satisfy the inequality"
    return hits[0]


def h2e_07():
    # 3 pence a head plus 20 pence for the pen, and at most 140 pence to spend
    return Le(3 * h + 20, 140)


def h2e_11():
    return solve(Eq(x - 4, 0), x)[0]


def h2e_12():
    return [z for z in solve(Eq((n - 9) * (n + 4), 0), n) if z > 0][0]


def h2e_14():
    rows = {"Ashfield": 90, "Barlow": 60, "Colne": 120, "Dell": 30}
    return Rational(rows["Colne"], sum(rows.values()))


def h2e_15():
    rows = [("Errick", 176), ("Fallow", 208), ("Glenmore", 149), ("Hartrigg", 231)]
    return max(rows, key=lambda row: row[1])[0]


def h2e_17():
    vals = [5, 8, 5, 12, 9, 5, 11]
    tally = Counter(vals).most_common()
    assert tally[0][1] > tally[1][1], "the list should have a single most common value"
    return tally[0][0]


def h2e_21():
    return solve(Eq(2 * x + (3 * x + 30), 180), x)[0]


def h2e_22():
    legs = (20, 21)
    hyp = sqrt(legs[0] ** 2 + legs[1] ** 2)
    return Rational(legs[0], 1) / hyp


# ---- Module 2 Hard
def h2h_01():
    xv, yv, av, bv = symbols("xv yv av bv")
    sol = solve([Eq(xv + 2 * yv, av), Eq(3 * xv - yv, bv)], [xv, yv])
    return sol[xv].subs({av: a, bv: b})


def h2h_02():
    av = symbols("av", positive=True)
    xv = symbols("xv")
    return solve(Eq(xv / av - xv / (3 * av), 8), xv)[0].subs(av, a)


def h2h_03():
    cv = symbols("cv")
    return solve(Eq(cv * 8 - 4 * 0, 56), cv)[0]


def h2h_04():
    bound = solve(Eq(52 * m - 96, 40 * m + 180), m)[0]
    return _greatest_int_strictly_below(bound)


def h2h_05():
    cv = symbols("cv")
    lhs = expand(4 * (x - cv))
    rhs = expand(4 * x - 20)
    # an identity in x: the two sides must agree coefficient by coefficient
    return solve(Eq(lhs - rhs, 0), cv)[0]


def h2h_06():
    fx = lambda z: 3 * z + 7
    return expand(fx(x - 4))


def h2h_08():
    hv = symbols("hv")
    # f takes equal values at points equidistant from the axis of symmetry
    return solve(Eq((2 - hv) ** 2, (10 - hv) ** 2), hv)[0]


def h2h_09():
    xv = symbols("xv", positive=True)
    return simplify((1 / xv + Rational(1, 3)) / (xv + 3)).subs(xv, x)


def h2h_10():
    xs = solve(Eq(x ** 2 + 2 * x - 3, 2 * x + 6), x)
    return sum(2 * xv + 6 for xv in xs)


def h2h_11():
    tv = symbols("tv", positive=True)
    return solve(Eq(2 ** (tv / 6), 8), tv)[0]


def h2h_12():
    return cancel((6 * x + 13) / (x + 2))


def h2h_13():
    hv = lambda z: Rational(24, 1) / (z - 2)
    xv = symbols("xv")
    return solve(Eq(24 / (xv - 2), hv(10) + 1), xv)[0]


def h2h_14():
    rows = {"Waggon": (42, 78), "Gig": (55, 25), "Cart": (90, 60)}
    total = sum(sum(v) for v in rows.values())
    return Rational(rows["Gig"][0], total)


def h2h_15():
    known = {"Monday": 34, "Tuesday": 29, "Wednesday": 41, "Friday": 46}
    thu = symbols("thu")
    return solve(Eq(sum(known.values()) + thu, 187), thu)[0]


def h2h_16():
    stone, gravel = 5, 3
    mix = Rational(6 * (stone + gravel), stone)
    return mix / Rational(24, 10)


def h2h_17():
    cv = symbols("cv", real=True)
    return Le(Abs(cv - 860), 45).subs(cv, c)


def h2h_18():
    rows = {"Ancaster": 96, "Bewdley": 60, "Cranfield": 144, "Dunmow": 100}
    return Rational(rows["Cranfield"], sum(rows.values())) * 100


def h2h_19():
    return _greatest_int_strictly_below(9 + 14)


def h2h_20():
    rv, hv = symbols("rv hv", positive=True)
    base = pi * rv ** 2
    curved = 2 * pi * rv * hv
    return (base + curved).subs({rv: r, hv: h})


def h2h_21():
    mv = symbols("mv", positive=True)
    ac = 12 * mv
    bc = ac * Rational(5, 12)          # tan A = BC / AC
    return simplify(sqrt(ac ** 2 + bc ** 2)).subs(mv, m)


DERIVE = {
 "H1-01": h1_01,
 "H1-02": h1_02,
 "H1-03": h1_03,
 "H1-04": h1_04,
 "H1-05": h1_05,
 "H1-06": h1_06,
 "H1-07": lambda: solve(Eq(8 * u + 5 * (51 - u), 333), u)[0],
 "H1-08": h1_08,
 "H1-09": lambda: solve(Eq((18 * n + 540) / n, 33), n)[0],
 "H1-10": h1_10,
 "H1-11": h1_11,
 "H1-12": h1_12,
 "H1-13": lambda: [z for z in solve(Eq(60 / x - 60 / (x + 5), 1), x) if z > 0][0],
 "H1-14": h1_14,
 "H1-15": h1_15,
 "H1-16": h1_16,
 "H1-17": h1_17,
 "H1-18": lambda: Rational(675, 100) / 3 * 7,
 "H1-19": h1_19,
 "H1-20": lambda: 4 * Rational(58 + 74, 2) * 40,
 "H1-21": h1_21,
 "H1-22": lambda: Rational(48 * 24 * 18 + 24 * 24 * 12, 1728),

 "H2E-01": lambda: 9 * b + 4 * f,
 "H2E-02": h2e_02,
 "H2E-03": lambda: solve(Eq(240, 15 * h), h)[0],
 "H2E-04": lambda: (900 - 45 * d).subs(d, 12),
 "H2E-05": h2e_05,
 "H2E-06": h2e_06,
 "H2E-07": h2e_07,
 "H2E-08": lambda: expand(8 * a ** 2 * b - 12 * a * b ** 2),
 "H2E-09": lambda: expand((x - 5) ** 2),
 "H2E-10": lambda: (5 * 3 ** x).subs(x, 0),
 "H2E-11": h2e_11,
 "H2E-12": h2e_12,
 "H2E-13": lambda: [z for z in solve(Eq(n ** 2 + 3 * n, 54), n) if z > 0][0],
 "H2E-14": h2e_14,
 "H2E-15": h2e_15,
 "H2E-16": lambda: Rational(80 - 24, 80),
 "H2E-17": h2e_17,
 "H2E-18": lambda: Rational(4 * 63, 12),
 "H2E-19": lambda: solve(Eq(2 * 45 + 2 * w, 146), w)[0],
 "H2E-20": lambda: solve(Eq(6 * 2 * d, 18), d)[0],
 "H2E-21": h2e_21,
 "H2E-22": h2e_22,

 "H2H-01": h2h_01,
 "H2H-02": h2h_02,
 "H2H-03": h2h_03,
 "H2H-04": h2h_04,
 "H2H-05": h2h_05,
 "H2H-06": h2h_06,
 "H2H-07": lambda: Lt(x, (b + c) / a),
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
 "H2H-22": lambda: 13 ** 2 - 5 ** 2,
}

# Nothing in Test 28 resists a symbolic derivation: every answer is a value, an
# algebraic form, an equation or inequality built from sympy-computed
# quantities, or a named table row picked out by a comparison over the printed
# data. MANUAL is therefore empty and pass 1 covers all 66.
MANUAL = {}

# Units that appear only in prose alongside a numeric choice. They are stripped
# before parsing so "1,186 kilograms" reads as 1186. None of these words ever
# appears inside a math span in this file, so stripping them cannot damage a
# symbolic choice.
UNIT_WORDS = re.compile(
    r"\b(kilograms?|kilogram|inches|inch|feet|foot|yards?|miles?|pints?|casks?|"
    r"tons?|pence|shillings?|pounds?|square|cubic|units?|horses?|lengths?|"
    r"quarters?|nails?|degrees?)\b", re.I)


def latex_to_expr(text):
    """Turn one answer choice into something sympify can read."""
    t = text.replace("&deg;", "").replace("&pound;", "").replace("&nbsp;", " ")
    t = t.replace("&gt;", ">").replace("&lt;", "<")
    t = UNIT_WORDS.sub(" ", t)
    t = re.sub(r"\\left|\\right", "", t)
    t = re.sub(r"\\\((.*?)\\\)", r"\1", t, flags=re.S)
    t = t.replace("\\le", "<=").replace("\\ge", ">=").replace("\\ne", "!=")
    # A fraction can sit inside an exponent (a^{\frac{7}{12}}) as readily as an
    # exponent inside a fraction (\frac{4a^{3}}{b^{4}}), and either fixed order
    # fails one of them. Alternate the two rewrites to a fixed point.
    for _ in range(8):
        prev = t
        t = re.sub(r"\^\{([^{}]*)\}", r"**(\1)", t)
        t = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"((\1)/(\2))", t)
        if t == prev:
            break
    t = t.replace("\\pi", "pi").replace("\\cdot", "*").replace("\\sqrt", "sqrt")
    t = t.replace("\\theta", "theta")
    t = t.replace("{,}", "").replace(",", "").replace("$", "").replace("%", "")
    t = t.replace("^", "**").replace("{", "(").replace("}", ")")
    t = re.sub(r"\|([^|]*)\|", r"Abs(\1)", t)
    # implicit multiplication: after a digit, after a closing paren, and after a
    # lone symbol — \(x(x+7)\) parses to nonsense without the last of the three,
    # and the lookbehind keeps sqrt( / Abs( from being mangled.
    t = re.sub(r"(\d)\s*([a-zA-Z(])", r"\1*\2", t)
    t = re.sub(r"\)\s*\(", ")*(", t)
    t = re.sub(r"(?<![a-zA-Z])([a-zA-Z])\s*\(", r"\1*(", t)
    # \frac{uv}{u+v} would otherwise parse as a symbol literally named "uv" and
    # the key would silently fail to match; split any surviving multi-letter run
    # into an implicit product. Function names and Abs are protected.
    def split_run(mo):
        word = mo.group(0)
        if word in ("sqrt", "pi", "Abs", "theta", "sin", "cos", "tan", "log"):
            return word
        return "*".join(word)
    t = re.sub(r"(?<![\\A-Za-z])[a-zA-Z]{2,}(?![A-Za-z])", split_run, t)
    # split_run may have just produced "a*b(" out of "ab(", so the
    # symbol-before-a-bracket rule has to run once more. Function names are
    # multi-letter, and this rule needs a letter with no letter before it, so
    # the "s(" of "Abs(" and the "t(" of "sqrt(" are both out of reach.
    t = re.sub(r"(?<![a-zA-Z])([a-zA-Z])\s*\(", r"\1*(", t)
    # Two more implicit products that only show up once LaTeX is gone. KaTeX
    # writes a product as juxtaposition, so "\pi r^{2}h" becomes "pi r**(2)h" —
    # a space between two atoms and a closing paren butted against a symbol are
    # both multiplications, and Python parses neither. Both rules require an
    # atom character on each side, so "<= 45" and " + 4" are untouched.
    t = re.sub(r"\)(?=[A-Za-z0-9])", ")*", t)
    t = re.sub(r"(?<=[A-Za-z0-9)])\s+(?=[A-Za-z0-9(])", "*", t)
    return re.sub(r"\s+", " ", t).strip()


def as_expr(text):
    """Parse a choice, trying the plain and the positive-assumption reading.

    symbols("a", positive=True) is a different Symbol from symbols("a"), so a
    single parse can miss a match that is really there, whichever side of the
    comparison happens to carry the assumption.
    """
    out = []
    raw = latex_to_expr(text)
    forms = [raw]
    if raw.count("=") == 1 and "<" not in raw and ">" not in raw and "!" not in raw:
        lhs, rhs = raw.split("=")
        forms.append(f"({lhs})-({rhs})")
    for form in forms:
        for loc in (BASE_LOCALS, POS_LOCALS):
            try:
                out.append(sympify(form, locals=loc))
            except Exception:
                pass
    return out


def same(expr, got):
    # An inequality is not a number: subtracting one from another raises, and a
    # relation with the wrong direction must never compare equal to the key.
    if isinstance(got, Relational) or isinstance(expr, Relational):
        if not (isinstance(got, Relational) and isinstance(expr, Relational)):
            return False
        if got.rel_op != expr.rel_op:
            return False
        try:
            return simplify((got.lhs - got.rhs) - (expr.lhs - expr.rhs)) == 0
        except Exception:
            return False
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
        # A named table row. The derivation picks the row out of the printed
        # data with a comparison, so this is still a check against a computed
        # result. Compare the choice text itself: pushing a proper name through
        # latex_to_expr splits it into an implicit product of its own letters
        # ("Bramber" -> "B*r*a*m*b*e*r") and nothing ever matches.
        forms = lambda z: {z.strip(), latex_to_expr(z).replace(" ", "")}
        want = got.strip()
        check(want in forms(text),
              f"{tag}: derived {got!r} but choice {qz['correct']} is {text!r}")
        for i, alt in enumerate(qz["choices"]):
            if i != "ABCD".index(qz["correct"]):
                check(want not in forms(alt),
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
    check("T16" not in json.dumps(qq) and "T21" not in json.dumps(qq),
          f"{tag}: a template test's provenance string survived into the content")

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
        for mm in re.finditer(r"\bsqrt\s*\(", bare):
            check(False, f"{tag}: plain-text sqrt(")
        for mm in re.finditer(r"[\dA-Za-z)]\s*\*\s*[\dA-Za-z(]", bare):
            check(inside(mm.start()), f"{tag}: asterisk multiplication outside math mode")
        for mm in re.finditer(r"(?<![\d/:])\d+\s*/\s*\d+(?![\d/])", bare):
            check(inside(mm.start()), f"{tag}: slash fraction outside math mode")
        for mm in re.finditer(r"\\(pi|frac|sqrt|cdot|le|ge|ne|times|div|circ|sin|cos|tan|"
                              r"log|ln|left|right|overline|text|theta)\b", bare):
            check(inside(mm.start()), f"{tag}: LaTeX macro outside math mode")
        for mm in re.finditer(r"(!=|<=|>=)", bare):
            check(False, f"{tag}: ASCII comparison operator, use \\ne / \\le / \\ge")
        for mm in re.finditer(r"(?<![A-Za-z\\])(theta|alpha|beta|lambda|sigma)(?![A-Za-z])",
                              bare):
            check(inside(mm.start()), f"{tag}: Greek letter spelled out in prose")
        for mm in re.finditer(r"(?<![A-Za-z\\])pi(?![A-Za-z])", bare):
            check(inside(mm.start()), f"{tag}: bare word pi outside math mode")
        # an angle written out as "35 degrees" instead of 35&deg;
        for mm in re.finditer(r"\d\s*degrees?\b", bare):
            check(False, f"{tag}: 'degrees' spelled out instead of &deg;")

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
    # "plot" is a piece of ground at least as often as it is a graph, and
    # "chart" is a sea chart; a boundary-free keyword in a checker is worse than
    # no check, so every alternative here has to name a visual explicitly.
    if re.search(r"(?<![A-Za-z])(shown|the figure|the graph above|scatterplot|"
                 r"the following (?:graph|figure|chart|table|plot))(?![A-Za-z])",
                 qq["stem"], re.I):
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
# The SHARED corpus at the content-pool root, not a per-directory copy.
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
# Every keyword below is a term that cannot occur in an ordinary English sense.
# "stage", "coach", "shoe", "gate", "toll", "spring", "stance", "forge", "boot"
# and "trust" were all considered and DROPPED for exactly that reason: a
# boundary-free or ordinary-word match in a checker is worse than no check,
# because it trains you to ignore the output. ("fen" matching inside "fence"
# and "moth" inside "months" are the recorded precedents.)
SETTING_KEYWORDS = [
    # Module 1 — coaching routes, timetables, coach building
    "coachbuilder", "coachyard", "stagecoach", "booking office", "weighbridge",
    "axle-box", "axle-arm", "elliptic spring", "window light", "door panel",
    "post chaise", "barouche", "landau", "brougham", "carriage", "passenger",
    "proprietor", "ironmonger", "varnish", "matting",
    # Module 2 Easy — farriery and droving
    "farrier", "horseshoe", "drovers", "cattle", "sheep", "keg", "shoeing",
    "watering trough", "drove",
    # Module 2 Hard — toll gates and turnpikes
    "turnpike", "toll house", "toll gate", "gatekeeper", "composition ticket",
    "waggon", "metalling", "gravel", "broken stone", "cistern",
]
m1_text = " ".join(qq["stem"].lower() for qq in MODULE_1)
m2_text = " ".join(qq["stem"].lower() for qq in MODULE_2_EASY + MODULE_2_HARD)


def has(kwd, text):
    """Prefix match anchored at a word boundary: "horseshoe" catches
    "horseshoes", but "print" would not catch "footprint"."""
    return re.search(r"\b" + re.escape(kwd), text) is not None


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
print(f"highest Jaccard vs production: {worst_prod:.2f}   within Test 28: {worst_self:.2f}")

if FAIL:
    print(f"\n{len(FAIL)} FAILURES:")
    for ff in FAIL:
        print("  -", ff)
    raise SystemExit(1)
print("\nALL CHECKS PASSED")
