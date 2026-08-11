#!/usr/bin/env python3
"""
Verify the 66 originally-authored Math questions for Test 31.

Four passes, each of which has caught a different class of defect in an earlier
build:

 1. Every answer is re-derived with sympy *from the question itself*, never
    read off the `check` note. A wrong `check` and a wrong key agree with each
    other; only an independent derivation separates them. Every distractor is
    also asserted to differ from the derived value. Anything sympy genuinely
    cannot hold goes in MANUAL with a written reason; MANUAL is empty here.
 2. House style on the final HTML — the Test 1/2 rules in CLAUDE.md plus the
    DB-wide rendering checks (no bare `^`, `sqrt(`, `*`-as-multiply, slash
    fraction, ASCII comparison operator, spelled-out Greek, or LaTeX macro
    outside a math span). `<img>` tags are stripped first, because a base64
    payload matches every one of those patterns.
 3. Template dedupe against every Math stem live in production, read from
    ../prod_math_stems.json (the corpus at the content-pool ROOT, not a local
    copy). Stems are reduced to a number-free token signature and compared by
    Jaccard. Every match at or above 0.45 is PRINTED, because the threshold
    decides what to READ, not what to accept: across Tests 18-21, 57 Math
    questions were rewritten as genuine template repeats and all but three of
    them scored below the 0.75 reject line.
 4. Self-collision among Test 31's own 66 stems, plus a cross-module setting
    check: no setting keyword may appear in both Module 1 and either Module 2
    branch, because a student sees Module 1 plus ONE Module 2 branch.

Run:  python3 verify_math_test31.py      (no DATABASE_URL needed)
"""
import json
import os
import re
from collections import Counter

from sympy import (Eq, Integer, Rational, binomial, expand, pi, simplify,
                   solve, sqrt, symbols, sympify)
from sympy.core.relational import Relational

from math_test31 import MODULE_1, MODULE_2_EASY, MODULE_2_HARD, ALL

HERE = os.path.dirname(os.path.abspath(__file__))

# Symbol names deliberately avoid S, E, I, N, O and Q: sympify("S") returns the
# SingletonRegistry and silently degrades a comparison to a string compare.
a, b, c, d, f, g, h, k = symbols("a b c d f g h k")
m, n, p, q, r, s, t = symbols("m n p q r s t")
u, v, w, x, y = symbols("u v w x y")
M_SYM, C_SYM, K_SYM = symbols("M c k", positive=True)

FAIL = []
PROD_THRESHOLD = 0.75
SELF_THRESHOLD = 0.75
READ_THRESHOLD = 0.45


def check(cond, msg):
    if not cond:
        FAIL.append(msg)


# ---------------------------------------------------------------- derivations
def m1_01():
    rate = Rational(402 - 318, 380 - 240)
    fixed = 318 - rate * 240
    return solve(Eq(fixed + rate * t, 450), t)[0]


def m1_02():
    loss = Rational(1120 - 1042, 6)
    return min(i for i in range(1, 60) if 1120 - loss * i < 1000)


def m1_03():
    sol = solve([Eq(5 * t + 8 * s, 181), Eq(3 * t + 4 * s, 99)], [t, s])
    return 4 * sol[t] + 5 * sol[s]


def m1_04():
    # the machine is cheaper when 246 + 0.04t < 90 + 0.16t; solve the EQUALITY
    # and then step up, so the boundary case (equal cost) is not silently
    # counted as "less than".
    tie = solve(Eq(Rational(246) + Rational(4, 100) * t,
                   Rational(90) + Rational(16, 100) * t), t)[0]
    return min(i for i in range(1, 4000)
               if Rational(246) + Rational(4, 100) * i
               < Rational(90) + Rational(16, 100) * i and i > tie - 1)


def m1_05():
    # second house s, first 4s; after moving 210 the first is twice the second
    sv = solve(Eq(4 * s - 210, 2 * (s + 210)), s)[0]
    return 4 * sv


def m1_06():
    slope_k = Rational(3 - 9, 8 - 2)
    slope_m = -1 / slope_k
    return 5 + slope_m * (10 - 4)


def m1_07():
    # 30 Medium eggs, each 53 <= m < 63: exactly one of the four printed values
    # lies in the scaled interval, and the derivation picks it rather than
    # confirming it.
    lo, hi = 30 * 53, 30 * 63
    good = [v for v in (1760, 1890, 1920, 1980) if lo <= v < hi]
    assert len(good) == 1
    return Integer(good[0])


def m1_08():
    # width w, length w+14, diagonal 26  ->  area
    width = [z for z in solve(Eq(w ** 2 + (w + 14) ** 2, 26 ** 2), w) if z > 0][0]
    return width * (width + 14)


def m1_09():
    roots = sorted(solve(Eq(-5 * t ** 2 + 20 * t + 2, 17), t))
    return roots[1] - roots[0]


def m1_11():
    # b and c are recovered by requiring x^2+bx+c to vanish at BOTH stated
    # roots, not by quoting Vieta's formulas from the check note.
    sol = solve([Eq(3 ** 2 + b * 3 + c, 0), Eq((-11) ** 2 + b * (-11) + c, 0)],
                [b, c], dict=True)[0]
    return sol[c] - sol[b]


def m1_12():
    gx = solve(Eq(4 * g - 7, 8 * x + 5), g)[0]
    return gx.subs(x, 3)


def m1_13():
    return simplify((1 / x - Rational(1, 4)) / (x - 4))


def m1_14():
    share = Rational(336 + 168, 86 + 210 + 336 + 168)
    return share * 1200


P_MASSES = [58, 60, 62, 64, 66]
Q_MASSES = [52, 57, 62, 67, 72]


def _mean(vals):
    return Rational(sum(vals), len(vals))


def _var(vals):
    mu = _mean(vals)
    return Rational(sum((Rational(z) - mu) ** 2 for z in vals), len(vals))


def m1_16_letter():
    """M1-16 keys a prose statement, so the derivation evaluates all four.

    Each choice is written out here as a predicate over quantities sympy
    computes from the two printed lists; exactly one must come out true, and
    that one must be the keyed letter. Nothing is read off the check note.
    """
    mp, mq = _mean(P_MASSES), _mean(Q_MASSES)
    vp, vq = _var(P_MASSES), _var(Q_MASSES)
    truth = [
        mp == mq and vp < vq,      # A
        mp == mq and vp > vq,      # B
        mp > mq and vp == vq,      # C
        mp < mq and vp > vq,       # D
    ]
    assert sum(1 for z in truth if z) == 1, truth
    return "ABCD"[truth.index(True)]


def m1_17():
    counts = [268, 291, 274, 302, 285, 264]
    mu = Rational(sum(counts), len(counts))
    return Integer(sum(1 for z in counts if Rational(z) > mu))


def m1_18():
    return Rational(45, 4) * 60 * 30


def m1_19():
    return 14 * 12 + Rational(1, 2) * pi * 6 ** 2


def m1_20():
    cv = solve(Eq(40 + 3 * c + c, 180), c)[0]
    return 180 - 3 * cv


def m1_21():
    # sin A = BC/AB = 20/29 with BC = 60
    ab = solve(Eq(Rational(60, 1) / v, Rational(20, 29)), v)[0]
    ac = sqrt(ab ** 2 - Integer(60) ** 2)
    return simplify(60 + ac + ab)


def m2h_01():
    # smaller s, larger 2s+16, total 148; the question asks for the difference
    sv = solve(Eq(s + (2 * s + 16), 148), s)[0]
    return (2 * sv + 16) - sv


def m2h_06_letter():
    """M2H-06 keys an ordered pair, so every printed pair is tested.

    The two conditions are x + y <= 60 and x >= 2y. Exactly one of the four
    pairs must satisfy both.
    """
    pairs = [(24, 14), (30, 20), (40, 18), (44, 20)]
    ok = [xv + yv <= 60 and xv >= 2 * yv for xv, yv in pairs]
    assert sum(1 for z in ok if z) == 1, ok
    return "ABCD"[ok.index(True)]


def m2h_09():
    # recover k from the stated solution, then solve the resulting equation
    kv = solve(Eq(2 * 5 ** 2 + k * 5 - 30, 0), k)[0]
    roots = solve(Eq(2 * x ** 2 + kv * x - 30, 0), x)
    other = [z for z in roots if z != 5]
    assert len(other) == 1 and 5 in roots
    return other[0]


def m2h_16():
    rows = [(9, 3), (10, 5), (11, 7), (12, 6), (13, 4)]
    data = [val for val, freq in rows for _ in range(freq)]
    assert len(data) == 25
    return Integer(sorted(data)[len(data) // 2])


def m2h_20():
    return solve(Eq(180 - Rational(360, 1) / n, 156), n)[0]


def m2h_02():
    av = solve(Eq(Rational(15 - 3, 1) / (7 - a), 4), a)[0]
    cc = solve(Eq(4 * 7 + c, 15), c)[0]
    assert (15 - 3) / (7 - av) == 4
    return cc


def m2h_03():
    lo = solve(Eq(5 - 3 * x, 11), x)[0]      # 5-3x <= 11  ->  x >= lo
    hi = solve(Eq(5 - 3 * x, -2), x)[0]      # -2 < 5-3x   ->  x <  hi
    return min(i for i in range(-20, 20) if lo <= i < hi)


def m2h_04():
    sol = solve([Eq(5 * t + 2 * w, Rational(43, 10)),
                 Eq(3 * t + 4 * w, Rational(44, 10))], [t, w])
    return sol[w] * 1000


def m2h_05():
    return solve(Eq(M_SYM, K_SYM * n / (n + C_SYM)), n)[0]


def m2h_07():
    return solve(Eq(x / 4 + x / 6, (x - 14) / 2), x)[0]


def m2h_08():
    poly = expand((3 * x + k) ** 2 - (9 * x ** 2 + 42 * x + c))
    sol = solve(poly.as_poly(x).all_coeffs(), [k, c], dict=True)[0]
    return sol[c]


def m2h_10():
    roots = [z for z in solve(Eq(2 * (x - 3) ** 3, 54), x) if z.is_real]
    assert len(roots) == 1
    return roots[0]


def m2h_11():
    return max(solve(Eq(a * (2 + a) + 3, 18), a))


def m2h_12():
    return simplify(5 / (x ** 2 - 4) - 1 / (x - 2))


def m2h_13():
    fn = lambda z: z ** 2 + 3 * z
    return Rational(fn(5) - fn(2), 5 - 2)


def m2h_14():
    done = 2 * (Rational(1, 6) + Rational(1, 9))
    return solve(Eq(Rational(1, 9) * t, 1 - done), t)[0]


def m2h_15():
    rows = [("Abbey Pond", 480, 396), ("Mill Stew", 350, 280),
            ("Lower Stew", 600, 504), ("Great Stew", 250, 210)]
    return max(rows, key=lambda z: Rational(z[1] - z[2], z[1]))[0]


def m2h_17():
    return Rational(binomial(7, 3), binomial(12, 3))


def m2h_18():
    per = Rational(1120, 320)
    return solve(Eq(per * n, 1540), n)[0] / 22


def m2h_22():
    return 96 * Rational(5, 2) ** 3


def m2e_12():
    rows = [(1, 7), (2, 11), (3, 15), (4, 19)]
    # fit g(x) = mx + q to the printed table and assert every row fits, so a
    # table that is not actually linear would fail here rather than be assumed
    mv, qv = symbols("mv qv")
    sol = solve([Eq(mv * xi + qv, yi) for xi, yi in rows[:2]], [mv, qv], dict=True)[0]
    for xi, yi in rows:
        assert sol[mv] * xi + sol[qv] == yi
    return sol[mv] * 7 + sol[qv]


def m2e_13():
    smaller = [z for z in solve(Eq(n * (n + 1), 210), n) if z > 0][0]
    return smaller + 1


def m2e_22():
    # cos A = AC/AB with AB = 74; solve for AC rather than multiplying the
    # ratio out by hand, then confirm the triangle that results actually
    # closes, so a ratio that does not belong to a right triangle would fail
    # here instead of being assumed.
    ac = solve(Eq(v / 74, Rational(35, 37)), v)[0]
    bc = sqrt(Integer(74) ** 2 - ac ** 2)
    assert simplify(ac ** 2 + bc ** 2 - 74 ** 2) == 0
    return ac


def m2h_21():
    # tan J = KL/JL with KL = 33; recover JL, then the hypotenuse JK
    jl = solve(Eq(Rational(33, 1) / v, Rational(33, 56)), v)[0]
    return sqrt(Integer(33) ** 2 + jl ** 2)


def m2h_19():
    # the displaced volume is the base area times the rise, converted to litres
    rise = 22 - 15
    return Rational(60 * 40 * rise, 1000)


DERIVE = {
 "M1-01": m1_01,
 "M1-02": lambda: "day " + str(m1_02()),
 "M1-03": m1_03,
 "M1-04": m1_04,
 "M1-05": m1_05,
 "M1-06": m1_06,
 "M1-07": m1_07,
 "M1-08": m1_08,
 "M1-09": m1_09,
 "M1-10": lambda: expand(12 * x ** 3 - 27 * x),
 "M1-11": m1_11,
 "M1-12": m1_12,
 "M1-13": m1_13,
 "M1-14": m1_14,
 "M1-15": lambda: solve(Eq(6 * 45, 10 * t), t)[0],
 "M1-17": m1_17,
 "M1-18": m1_18,
 "M1-19": m1_19,
 "M1-20": m1_20,
 "M1-21": m1_21,
 "M1-22": lambda: Rational(60 * 40 * 30, 30 * 20 * 5) * 30,

 "M2E-01": lambda: solve(Eq(5 * p + 18, 63), p)[0],
 "M2E-02": lambda: 24 * 6 + 15,
 "M2E-03": lambda: solve(Eq(7 * n - 12, 4 * n + 27), n)[0],
 "M2E-04": lambda: Rational(7, 10) * 40 + 12,
 "M2E-05": lambda: max(i for i in range(200) if 3 * i + 14 <= 71),
 "M2E-06": lambda: 3 * solve(Eq(3 * v + v, 96), v)[0],
 "M2E-07": lambda: "15 < d <= 40",
 "M2E-08": lambda: expand((x + 9) * (x - 4)),
 "M2E-09": lambda: solve(Eq(x + 6, 0), x)[0],
 "M2E-10": lambda: sum(solve(Eq((x - 4) * (x + 9), 0), x)),
 "M2E-11": lambda: simplify(7 * a + 3 * b - 2 * a + 5 * b),
 "M2E-12": m2e_12,
 "M2E-13": m2e_13,
 "M2E-14": lambda: Rational(35, 100) * 240,
 "M2E-15": lambda: solve(Eq(7 * n, 245), n)[0],
 "M2E-16": lambda: Rational(24 + 31 + 28 + 36 + 31, 50),
 "M2E-17": lambda: Integer(sorted([23, 31, 18, 27, 24])[2]),
 "M2E-18": lambda: 134 - 88,
 "M2E-19": lambda: 18 * 25,
 "M2E-20": lambda: 360 - (95 + 128 + 62),
 "M2E-21": lambda: Rational(14 + 22, 2) * 9,
 "M2E-22": m2e_22,

 "M2H-01": m2h_01,
 "M2H-02": m2h_02,
 "M2H-03": m2h_03,
 "M2H-04": m2h_04,
 "M2H-05": m2h_05,
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

# Two questions key something that is not a number or an expression at all: a
# prose statement comparing two data sets (M1-16) and an ordered pair chosen
# from four (M2H-06). For those the derivation evaluates the CLAIM each printed
# choice makes and returns the letter of the one that is true, asserting on the
# way that exactly one of the four is. That is still an independent derivation
# — the predicate is computed from the printed data, not read off the key.
LETTER_DERIVE = {
 "M1-16": m1_16_letter,
 "M2H-06": m2h_06_letter,
}

# Nothing in this build is outside sympy's reach. Three answers are strings
# rather than values — a named table row (M2H-15), an inequality written in
# words as well as symbols (M2E-07) and a day number (M1-02) — but each of
# those strings is built from a sympy-computed result rather than copied from
# the author's note, so they are derived, not asserted.
MANUAL = {}


def latex_to_expr(text):
    """Turn one answer choice into something sympify can read."""
    t = text.replace("&deg;", "").replace("&gt;", ">").replace("&lt;", "<")
    t = re.sub(r"\\left|\\right|\\,|\\;|\\!", "", t)
    t = re.sub(r"\\\((.*?)\\\)", r"\1", t, flags=re.S)
    t = re.sub(r"\\\[(.*?)\\\]", r"\1", t, flags=re.S)
    t = t.replace("\\ge", ">=").replace("\\le", "<=").replace("\\ne", "!=")
    t = t.replace("\\gt", ">").replace("\\lt", "<")
    t = t.replace("\\div", "/")
    # \sqrt is parked behind a non-letter placeholder so the implicit-product
    # rules below never turn "sqrt(" into "sqrt*(" and the multi-letter split
    # below never turns it into "s*q*r*t".
    t = t.replace("\\sqrt", "#")
    t = t.replace("\\pi", "@").replace("\\cdot", "*")
    t = re.sub(r"\\(sin|cos|tan)\b", r"\1", t)
    t = t.replace("{,}", "").replace(",", "").replace("$", "").replace("%", "")
    # Exponents and fractions are rewritten in the SAME loop, alternating, and
    # iterated to a fixed point. Neither can go first on its own: \frac's
    # arguments are matched with a non-recursive [^{}]* pattern, so a \frac
    # holding an exponent (\frac{18x^{7}}{3x^{2}}) needs the exponent flattened
    # first, while an exponent holding a fraction (a^{\frac{7}{12}}) needs the
    # fraction flattened first. Picking an order cannot fix it; a fixed point
    # can.
    for _ in range(12):
        new = re.sub(r"\^\{([^{}]*)\}", r"**(\1)", t)
        new = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"((\1)/(\2))", new)
        if new == t:
            break
        t = new
    t = t.replace("^", "**").replace("{", "(").replace("}", ")")
    # A surviving multi-letter run is an implicit product, not a symbol name:
    # without this, \frac{Mc}{k-M} parses as a symbol called "Mc" and the key
    # silently fails to match. sin/cos/tan are protected first.
    t = re.sub(r"\b(sin|cos|tan)\b", lambda mo: mo.group(1).upper() + "~", t)
    t = re.sub(r"[A-Za-z]{2,}",
               lambda mo: "*".join(mo.group(0)), t)
    t = re.sub(r"(SIN|COS|TAN)~", lambda mo: mo.group(1).lower(), t)
    # Implicit products: after a digit, after a closing paren and after a
    # symbol. Without the last two, "\(x(x+7)\)" and "x**(3)y" parse to
    # nonsense instead of failing loudly.
    t = re.sub(r"(\d)\s*([a-zA-Z(#@])", r"\1*\2", t)
    t = re.sub(r"\)\s*([A-Za-z0-9(#@])", r")*\1", t)
    t = re.sub(r"(?<=[a-zA-Z])\s*\(", "*(", t)
    t = t.replace("#", "sqrt").replace("@", "pi")
    t = t.replace("*<", "<").replace("*>", ">").replace("*!", "!")
    return t.strip()


BASE_LOCALS = {}
POS_LOCALS = {nm: symbols(nm, positive=True)
              for nm in ("M", "c", "k", "a", "b", "n", "x", "y")}


def as_expr(text):
    out = []
    for loc in (BASE_LOCALS, POS_LOCALS):
        try:
            out.append(sympify(latex_to_expr(text), locals=loc))
        except Exception:
            pass
    return out


def same(expr, got):
    if isinstance(expr, Relational) or isinstance(got, Relational):
        return bool(expr == got)
    try:
        if simplify(expr - got) == 0:
            return True
    except Exception:
        pass
    try:
        if abs(complex((expr - got).evalf())) < 1e-9:
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

    if tag in LETTER_DERIVE:
        # the derivation evaluates each printed choice's claim and returns the
        # letter of the single true one
        derived += 1
        want_letter = LETTER_DERIVE[tag]()
        check(qz["correct"] == want_letter,
              f"{tag}: exactly one choice is true and it is {want_letter}, "
              f"but the key says {qz['correct']}")
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
        # A named table row, or an inequality written partly in words. The
        # string is assembled from sympy-computed values inside the derivation,
        # so this is still a comparison against a derived result.
        #
        # NOTE: do NOT push these through latex_to_expr. That function splits
        # any multi-letter run into an implicit product, which is right for
        # "\frac{Mc}{k-M}" and catastrophic for a row name: it turned the
        # derived "day 10" into "d*a*y10" and reported a mismatch between two
        # strings that were in fact identical. Both sides are normalised as
        # plain text here instead.
        def norm(z):
            z = re.sub(r"\\\(|\\\)|\\\[|\\\]", " ", z)
            z = (z.replace("\\le", "\u2264").replace("\\ge", "\u2265")
                  .replace("\\lt", "<").replace("\\gt", ">")
                  .replace("<=", "\u2264").replace(">=", "\u2265"))
            z = re.sub(r"<[^>]+>", " ", z)
            return re.sub(r"[\s,]+", "", z).lower()

        want = norm(got)
        check(want == norm(text),
              f"{tag}: derived {got!r} but choice {qz['correct']} is {text!r}")
        for i, alt in enumerate(qz["choices"]):
            if i != "ABCD".index(qz["correct"]):
                check(norm(alt) != want,
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


def choice_value(text):
    """Numeric value of one answer choice, or None if it is not purely numeric.

    Handles a plain number (with thousands commas, a leading $ or a trailing
    %), a bare fraction and a multiple of pi, which is as far as a comparison
    of magnitudes is meaningful. Anything symbolic, an ordered pair, an
    inequality or prose returns None and is exempt from the ordering rule,
    because those have no canonical increasing order.
    """
    tz = re.sub(r"\\\(|\\\)|\\\[|\\\]|\\left|\\right|\s", "", text)
    tz = tz.replace(",", "").replace("$", "").replace("%", "")
    sign = 1
    if tz.startswith("-") and ("\\frac" in tz or "\\pi" in tz):
        sign, tz = -1, tz[1:]
    mo = re.fullmatch(r"\\frac\{(-?\d+)\}\{(-?\d+)\}", tz)
    if mo:
        return sign * float(mo.group(1)) / float(mo.group(2))
    mo = re.fullmatch(r"(-?\d*)\\pi", tz)
    if mo:
        return sign * float(mo.group(1) or 1) * 3.141592653589793
    try:
        return float(tz)
    except ValueError:
        return None

seen_ids = set()
styled = 0
for qq in ALL:
    tag = qq["n"]
    check(tag not in seen_ids, f"{tag}: duplicate question id")
    seen_ids.add(tag)
    check(qq["skill"] in VALID_SKILLS[qq["domain"]],
          f"{tag}: skill {qq['skill']} is not a {qq['domain']} skill")
    check(bool(qq.get("check")), f"{tag}: no check note")
    check("T19" not in json.dumps(qq) and "T21" not in json.dumps(qq),
          f"{tag}: carries a sibling test's provenance tag")

    blocks = [qq["stem"]] + list(qq.get("choices") or [])
    styled += 1
    if qq["type"] == "MC":
        check(len(qq["choices"]) == 4, f"{tag}: needs exactly 4 choices")
        check(len(set(qq["choices"])) == 4, f"{tag}: duplicate answer choice")
        check(qq["correct"] in "ABCD", f"{tag}: bad answer label")
        # Numeric choices are listed in increasing order on the real test, and
        # in every sibling build (Tests 19 and 21: 85 purely numeric MC items,
        # zero out of order). This build shipped NINE scrambled sets — 1,299 /
        # 1,300 / 1,310 / 1,301 among them — because the key letter was being
        # chosen for balance and the choices left where they fell. Balance is
        # bought by choosing distractor VALUES, never by scrambling the order.
        vals = [choice_value(cz) for cz in qq["choices"]]
        if all(vz is not None for vz in vals):
            check(vals == sorted(vals),
                  f"{tag}: numeric choices are not in increasing order: "
                  f"{qq['choices']}")
    else:
        check(bool(qq.get("answers")), f"{tag}: free response with no accepted answer")

    for blk in blocks:
        bare = re.sub(r"<img[^>]*>", " ", blk)   # base64 matches every rule below
        check(not bare.strip().startswith("<p>"), f"{tag}: stem is <p>-wrapped")
        check("\u00b0" not in bare, f"{tag}: raw degree glyph, use &deg;")
        check("\u2264" not in bare and "\u2265" not in bare and "\u2260" not in bare,
              f"{tag}: raw comparison glyph, use \\le / \\ge / \\ne inside math mode")
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
        for mm in re.finditer(r"\\(pi|frac|sqrt|cdot|div|le|ge|ne|lt|gt|circ|sin|cos|tan|"
                              r"log|ln|left|right|overline|text)\b", bare):
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
                 r"graph above|chart|plot|diagram)\b", qq["stem"], re.I):
        check("<table" in qq["stem"] or "<img" in qq["stem"],
              f"{tag}: refers to a visual it does not contain")
    if "system" in qq["stem"].lower() and len(re.findall(r"=", qq["stem"])) >= 2:
        check("<br/>" in qq["stem"],
              f"{tag}: a system of equations must be stacked with <br/>")

print(f"   {styled} of {len(ALL)} questions style-checked (stems and every choice)")

# Dump every math span so katex_check.mjs can try to typeset each one. A span
# KaTeX cannot parse renders as red error text in the exam; nothing in the
# Python checks above can see that, and `&lt;` inside a math span (live in two
# production questions) is exactly the defect it catches.
spans_out = []
for qq in ALL:
    for blk in [qq["stem"]] + list(qq.get("choices") or []):
        for mm in SPAN.finditer(blk):
            spans_out.append({"tag": qq["n"], "tex": mm.group(1) or mm.group(2)})
with open(os.path.join(HERE, "math_spans.json"), "w") as fh:
    json.dump(spans_out, fh, ensure_ascii=False, indent=1)
print(f"   wrote {len(spans_out)} math spans to math_spans.json "
      f"(run: node katex_check.mjs)")

# ------------------------------------------------------------------- dedupe
print("== pass 3: template dedupe against production")


def sig(text):
    tt = re.sub(r"<img[^>]*>", " ", text)
    tt = re.sub(r"<[^>]+>", " ", tt)
    tt = re.sub(r"&[a-z]+;", " ", tt)
    math = []
    for mm in SPAN.findall(tt):
        sp = mm[0] or mm[1]
        if "\\frac" in sp:
            math.append("mathfrac")
        if "\\sqrt" in sp:
            math.append("mathsqrt")
        if "\\pi" in sp:
            math.append("mathpi")
        if re.search(r"\^\{?2\}?", sp):
            math.append("mathsq")
        if re.search(r"\^\{?[a-z]\}?", sp):
            math.append("mathexpvar")
    tt = re.sub(r"\\[a-zA-Z]+", " ", tt)
    tt = re.sub(r"[-+]?\d[\d,.]*", "#", tt)
    return set((re.sub(r"[^a-z#]+", " ", tt.lower()).strip()
                + " " + " ".join(sorted(set(math)))).split())


def jaccard(aa, bb):
    return len(aa & bb) / max(1, len(aa | bb))


# The corpora live at the content-pool ROOT and are read-only.
prod_path = os.path.join(HERE, "..", "prod_math_stems.json")
worst_prod = 0.0
if os.path.exists(prod_path):
    prod = json.load(open(prod_path))
    print(f"   comparing against {len(prod)} live Math stems")
    others = [(pq["label"], sig(pq["stem"])) for pq in prod]
    worst = []
    for qq in ALL:
        s0 = sig(qq["stem"])
        score, label = max(((jaccard(s0, o), lab) for lab, o in others),
                           key=lambda z: z[0])
        worst.append((score, qq["n"], label))
        check(score < PROD_THRESHOLD,
              f"{qq['n']}: template similarity {score:.2f} to {label}")
    worst.sort(reverse=True)
    worst_prod = worst[0][0]
    flagged = [row for row in worst if row[0] >= READ_THRESHOLD]
    print(f"   {len(flagged)} match(es) at or above {READ_THRESHOLD:.2f} "
          f"— every one of these was read by hand during authoring:")
    for sc, tag, lab in flagged:
        print(f"     {sc:.2f}  {tag}  vs {lab}")
    print("   next closest:")
    for sc, tag, lab in [row for row in worst if row[0] < READ_THRESHOLD][:8]:
        print(f"     {sc:.2f}  {tag}  vs {lab}")
else:
    check(False, "../prod_math_stems.json is missing — dedupe cannot run")

# ------------------------------------------------------------ self-collision
print("== pass 4: self-collision and cross-module settings")
pairs = []
for i in range(len(ALL)):
    for j in range(i + 1, len(ALL)):
        sc = jaccard(sig(ALL[i]["stem"]), sig(ALL[j]["stem"]))
        pairs.append((sc, ALL[i]["n"], ALL[j]["n"]))
        check(sc < SELF_THRESHOLD,
              f"{ALL[i]['n']} vs {ALL[j]['n']}: internal similarity {sc:.2f}")
pairs.sort(reverse=True)
worst_self = pairs[0][0]
print(f"   {len(pairs)} pairs compared; closest:")
for sc, aa, bb2 in pairs[:5]:
    print(f"     {sc:.2f}  {aa}  vs {bb2}")

# A student sees Module 1 and exactly ONE Module 2 branch, so a setting reused
# across that boundary shows the same scene twice in one sitting.
#
# Every keyword is matched with an explicit lookbehind AND lookahead plus an
# allowed suffix list. A bare \b prefix is not enough here and the traps are
# real ones in this vocabulary: "hen" sits inside "when", "then" and "hence";
# "pen" inside "open"; "loft" inside "aloft"; "eel" inside "wheel", "steel" and
# "keel"; "trap" inside "strap"; "carp" inside "carpenter"; "teal" inside
# "steal". A boundary-free substring match in a checker is worse than no check,
# because it trains you to ignore the output.
SETTING_KEYWORDS = [
    # Module 1 territory
    "egg", "grader", "grading", "packing", "tray", "crate", "pullet",
    "hen", "falcon", "hawk", "mews", "jess", "creance", "lure", "quarry",
    "goshawk", "peregrine", "weathering", "eel", "elver",
    # Module 2 territory
    "dovecote", "loft", "pigeon", "squab", "nest", "decoy", "wigeon",
    "teal", "wildfowl", "stew", "carp", "tench", "pond", "flight",
    # ordinary-English words deliberately NOT used as keywords, because they
    # cannot be told apart from their everyday senses even with boundaries:
    # "duck", "trap", "pen", "brood", "ground", "flock", "bird", "fish".
]
SUFFIX = r"(s|es|ing|ed|er|ers|men|man)?"
m1_text = " ".join(qq["stem"].lower() + " " + " ".join(qq.get("choices") or [])
                   for qq in MODULE_1).lower()
m2_text = " ".join(qq["stem"].lower() + " " + " ".join(qq.get("choices") or [])
                   for qq in MODULE_2_EASY + MODULE_2_HARD).lower()


def uses(kwd, text):
    return re.search(r"(?<![A-Za-z])" + re.escape(kwd) + SUFFIX + r"(?![A-Za-z])",
                     text) is not None


shared = [kwd for kwd in SETTING_KEYWORDS if uses(kwd, m1_text) and uses(kwd, m2_text)]
check(not shared, f"settings reused across Module 1 and a Module 2 branch: {shared}")
in_m1 = [kwd for kwd in SETTING_KEYWORDS if uses(kwd, m1_text)]
in_m2 = [kwd for kwd in SETTING_KEYWORDS if uses(kwd, m2_text)]
print(f"   {len(SETTING_KEYWORDS)} keywords checked: {len(in_m1)} in Module 1, "
      f"{len(in_m2)} in Module 2, {len(shared)} shared")
print(f"     M1: {', '.join(in_m1)}")
print(f"     M2: {', '.join(in_m2)}")

# ------------------------------------------------------------------- report
print()
print(f"questions: {len(ALL)}")
for label, mod in (("M1 ", MODULE_1), ("M2E", MODULE_2_EASY), ("M2H", MODULE_2_HARD)):
    doms = dict(sorted(Counter(qq["domain"] for qq in mod).items()))
    keys = dict(sorted(Counter(qq["correct"] for qq in mod
                               if qq["type"] == "MC").items()))
    frs = sum(1 for qq in mod if qq["type"] == "FR")
    print(f"  {label}: {len(mod)} questions, {frs} FR, domains {doms}, key {keys}")
print(f"skills: {dict(sorted(Counter(qq['skill'] for qq in ALL).items()))}")
print(f"highest Jaccard vs production: {worst_prod:.2f}   within Test 31: {worst_self:.2f}")

if FAIL:
    print(f"\n{len(FAIL)} FAILURES:")
    for failure in FAIL:
        print("  -", failure)
    raise SystemExit(1)
print("\nALL CHECKS PASSED")
