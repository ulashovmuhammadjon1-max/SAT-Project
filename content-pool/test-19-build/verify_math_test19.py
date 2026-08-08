#!/usr/bin/env python3
"""
Verify the 66 originally-authored Math questions for Test 19.

Four passes, because each of them has caught a different class of defect in
earlier builds:

 1. Every answer is re-derived with sympy *from the question itself*, never
    read off the `check` note. A wrong `check` and a wrong key agree with each
    other; only an independent derivation catches that. Every distractor is
    also asserted to differ from the derived value. Anything sympy cannot hold
    is listed in MANUAL with a written reason, and MANUAL is deliberately
    tiny.
 2. House style on the rendered HTML — the Test 1/2 rules in CLAUDE.md plus
    the DB-wide rendering checks (no bare `^`, `sqrt(`, `*`-as-multiply, slash
    fractions, ASCII comparison operators, spelled-out Greek, or a LaTeX macro
    outside a math span).
 3. Template dedupe against every Math stem live in production, read from the
    local snapshot `prod_math_stems.json`. Not just exact duplicates: a
    question that reuses a template with new numbers is a repeat, so stems are
    reduced to a number-free token signature and compared by Jaccard. Every
    match above 0.45 is printed, because the threshold decides what to READ,
    not what to accept.
 4. Self-collision among Test 19's own 66 questions, plus a setting check: no
    setting keyword may appear in both Module 1 and either Module 2 branch,
    since a student sees Module 1 plus one Module 2 branch and would otherwise
    meet the same peat bank twice in one sitting.

Run:  python3 verify_math_test19.py      (no DATABASE_URL needed)
"""
import json
import os
import re
from collections import Counter

from sympy import (Abs, Eq, Le, Integer, Rational, cos, expand, pi, simplify,
                   solve, sqrt, symbols, sympify)
from sympy.core.relational import Relational

from math_test19 import MODULE_1, MODULE_2_EASY, MODULE_2_HARD, ALL

HERE = os.path.dirname(os.path.abspath(__file__))

# Symbol names deliberately avoid S, E, I, N, O, Q and beta/gamma/zeta:
# sympify("S") returns the SingletonRegistry and silently degrades a
# comparison to a string compare.
a, b, c, d, f, g, h, k = symbols("a b c d f g h k")
m, n, p, q, r, s, t = symbols("m n p q r s t")
u, v, w, x, y = symbols("u v w x y")
A_POS = symbols("a", positive=True)
X_POS = symbols("x", positive=True)
X_REAL = symbols("x", real=True)

FAIL = []
PROD_THRESHOLD = 0.75
SELF_THRESHOLD = 0.75
READ_THRESHOLD = 0.45


def check(cond, msg):
    if not cond:
        FAIL.append(msg)


# ---------------------------------------------------------------- derivations
def h1_01():
    # 3 hours at 240 turves/hour, then h more hours at 180, total 1,440
    hv = solve(Eq(3 * 240 + 180 * h, 1440), h)[0]
    return 3 + hv


def h1_02():
    step = Rational(40 - 70, 8 - 3)
    return 70 + step * (12 - 3)


def h1_03():
    sv = solve(Eq(65 + 18 * s, 23 * s), s)[0]
    return 23 * sv


def h1_04():
    cap = 46 * Rational(5, 2)
    return max(i for i in range(500) if 74 + Rational(i, 2) <= cap)


def h1_05():
    uv = solve(Eq(u + 3 * u + (u + 6), 56), u)[0]
    return uv + 6


def h1_07():
    slope = Rational(70 - 34, 20 - 5)          # (7.0-3.4)/(2.0-0.5)
    inter = Rational(34, 10) - Rational(5, 10) * slope
    return solve(Eq(slope * h + inter, Rational(106, 10)), h)[0]


def h1_09():
    bv = [z for z in solve(Eq(180 * b ** 3, 1440), b) if z.is_real and z > 0][0]
    n0 = solve(Eq(n * bv ** 2, 180), n)[0]
    return n0 * bv ** 4


def h1_10():
    roots = sorted(solve(Eq(x ** 2 - 8 * x + 20, 5), x))
    return roots[1] - roots[0]


def h1_11():
    kv = solve(Eq((2 * 5 + k) / (5 - 3), 7), k)[0]
    return (2 * 4 + kv) / (4 - 3)


def h1_12():
    # (3x+m)(2x-5) must equal 6x^2-9x-15 for every x
    poly = expand((3 * x + m) * (2 * x - 5) - (6 * x ** 2 - 9 * x - 15))
    return solve(poly.as_poly(x).all_coeffs(), m)[m]


def h1_16():
    rows = [(2760, 6), (3150, 7), (2000, 5), (3840, 8)]
    rates = [Rational(cut, hrs) for cut, hrs in rows]
    return max(rates) - min(rates)


def h1_17():
    return Rational(12 * 25 - 18 + 42, 12)


def h1_21():
    # the weir face is adjacent to the 60-degree angle
    return simplify(12 * cos(pi / 3))


def h2e_03():
    return Rational(3000 - 1400, 6 - 2)


def h2e_06():
    sol = solve([Eq(a + b, 40), Eq(a - b, 6)], [a, b])
    return sol[a]


def h2e_10():
    return max(solve(Eq(x ** 2 + 5 * x - 24, 0), x))


def h2h_01():
    pv = solve(Eq(p * 2 + 4 * 5, 26), p)[0]
    qv = solve(Eq(3 * 2 - q * 5, 1), q)[0]
    return pv + qv


def h2h_02():
    slope = Rational(31 - 7, 10 - 2)
    inter = 7 - slope * 2
    return solve(Eq(slope * x + inter, 100), x)[0]


def h2h_03():
    lo = solve(Eq((2 * x - 5) / 4, 3), x)[0]
    hi = solve(Eq((2 * x - 5) / 4, 7), x)[0]
    return max(lo, hi)


def h2h_04():
    sol = solve([Eq(4 * w + 3 * b, 62), Eq(6 * w + 5 * b, 98)], [w, b])
    return 5 * sol[w] + 4 * sol[b]


def h2h_05():
    return solve(Eq(p - q * t, p / 2), t)[0]


def h2h_06():
    return max(i for i in range(41) if 20 * (40 - i) + 45 * i <= 26 * 60)


def h2h_10():
    return solve(Eq(9 ** (x + 1), 27 ** (x - 1)), x)[0]


def h2h_11():
    sol = solve([Eq(-p / 2, 5), Eq(1 + p + q, 9)], [p, q])
    return sol[q]


def h2h_13():
    return sum(solve(Eq(Abs(2 * X_REAL - 7), X_REAL + 1), X_REAL))


def h2h_14():
    # 6 cutters x 15 days of work, spread over 9 days, minus the 6 on hand
    return solve(Eq(9 * n, 6 * 15), n)[0] - 6


def h2h_15():
    rows = [("Osier Green", 168, 32), ("Sedge Fen", 108, 42)]
    worst = max(rows, key=lambda z: Rational(z[2], z[1] + z[2]))
    other = [z for z in rows if z[0] != worst[0]][0]
    return Integer(worst[2] - other[2])


def h2h_16():
    rows = [("Willow Ham", 4200, 15), ("Long Drove", 3800, 6),
            ("North Rhyne", 4500, 21), ("Sedge Bank", 4000, 11)]
    return max(rows, key=lambda z: z[1] * (100 - z[2]))[0]


def h2h_19():
    rsq = solve(Eq(pi * v * 4, 36 * pi), v)[0]      # v stands for r squared
    return pi * rsq * Rational(3, 2)


def h2h_20():
    leg = [z for z in solve(Eq((3 * v) ** 2 + (4 * v) ** 2, 45 ** 2), v) if z > 0][0]
    return Rational(1, 2) * (3 * leg) * (4 * leg)


def h2h_21():
    opp = Rational(5, 13) * 26
    adj = sqrt(Integer(26) ** 2 - opp ** 2)
    return simplify(Rational(1, 2) * opp * adj)


def h2h_22():
    long_leg = Rational(4, 3) * Rational(3, 2)
    return Rational(1, 2) * Rational(3, 2) * long_leg * 20


DERIVE = {
 "H1-01": h1_01,
 "H1-02": h1_02,
 "H1-03": h1_03,
 "H1-04": h1_04,
 "H1-05": h1_05,
 "H1-06": lambda: solve(Eq(40 * 12 + 20 * n, 15 * (40 + n)), n)[0],
 "H1-07": h1_07,
 "H1-08": lambda: expand(2 * x ** 2 - 20 * x + 63),
 "H1-09": h1_09,
 "H1-10": h1_10,
 "H1-11": h1_11,
 "H1-12": h1_12,
 "H1-13": lambda: max(z for z in solve(Eq(x ** 4 - 13 * x ** 2 + 36, 0), x)
                      if z.is_real),
 "H1-14": lambda: 400 * 5 * (1 - Rational(64, 100)),
 "H1-15": lambda: min(i for i in range(100)
                      if 120 * i >= Rational(14 * 6 * 9, 2)),
 "H1-16": h1_16,
 "H1-17": h1_17,
 "H1-18": lambda: Rational(75, 45 + 75),
 "H1-19": lambda: sqrt(Integer(14 - 2) ** 2 + Integer(13 + 3) ** 2) / 2,
 "H1-20": lambda: 18 * 7 - 12 * Rational(5, 2),
 "H1-21": h1_21,
 "H1-22": lambda: Rational(2, 3) * Integer(3) ** 3,

 "H2E-01": lambda: 24 * 7,
 "H2E-02": lambda: Rational(322, 14),
 "H2E-03": h2e_03,
 "H2E-04": lambda: 24 * d + 130,
 "H2E-05": lambda: Le(m, 2400),
 "H2E-06": h2e_06,
 "H2E-08": lambda: expand((4 * x + 15) + (6 * x - 7)),
 "H2E-09": lambda: Integer(6) ** 2 + 4 * 6,
 "H2E-10": h2e_10,
 "H2E-11": lambda: Rational(48, 6) + 5,
 "H2E-12": lambda: expand((3 * x ** 4) * (5 * x ** 3)),
 "H2E-13": lambda: 640 * Rational(1, 2) ** 3,
 "H2E-14": lambda: Rational(18, 100) * 450,
 "H2E-15": lambda: Rational(96, 8) * 3,
 "H2E-16": lambda: 46 + 58 + 39 + 67,
 "H2E-17": lambda: Integer(sorted([14, 9, 12, 20, 11, 9, 17])[3]),
 "H2E-18": lambda: Rational(40 - 24, 40),
 "H2E-19": lambda: 360 - 145 - 132,
 "H2E-20": lambda: Rational(84, 12),
 "H2E-21": lambda: Rational(1, 2) * Integer(4) ** 2,
 "H2E-22": lambda: Rational(7, 25),

 "H2H-01": h2h_01,
 "H2H-02": h2h_02,
 "H2H-03": h2h_03,
 "H2H-04": h2h_04,
 "H2H-05": h2h_05,
 "H2H-06": h2h_06,
 "H2H-07": lambda: solve(Eq((2 * x + 7) / 3 - (x - 4) / 2, 5), x)[0],
 "H2H-08": lambda: expand(((4 * x + 1) ** 2 - 3 * (4 * x + 1))
                          - (4 * (x ** 2 - 3 * x) + 1)),
 "H2H-09": lambda: solve(Eq((6 * x + 19) / (x + 3), 6 + k / (x + 3)), k)[0],
 "H2H-10": h2h_10,
 "H2H-11": h2h_11,
 "H2H-12": lambda: expand(2 * x ** 3 + 3 * x ** 2 - 8 * x - 12),
 "H2H-13": h2h_13,
 "H2H-14": h2h_14,
 "H2H-15": h2h_15,
 "H2H-16": h2h_16,
 "H2H-17": lambda: Rational(6, 15) * Rational(5, 14),
 "H2H-18": lambda: 27 * 16 - 27,
 "H2H-19": h2h_19,
 "H2H-20": h2h_20,
 "H2H-21": h2h_21,
 "H2H-22": h2h_22,
}

# The only question whose key is a sentence rather than a value or a form
# sympy can hold. Its answer is checked against the phrase the derivation
# demands instead, which is the strongest check available for prose.
MANUAL = {
 "H2E-07": ("The four choices are English sentences interpreting a coefficient "
            "in a linear model; there is no expression for sympy to compare. "
            "Checked by requiring the key to be the sentence identifying 24 "
            "as a fixed charge, which is what a term not multiplied by n "
            "means."),
}
MANUAL_MARKER = {
 "H2E-07": "fixed charge",
}


def latex_to_expr(text):
    """Turn one answer choice into something sympify can read."""
    t = text.replace("&deg;", "").replace("&gt;", ">").replace("&lt;", "<")
    t = re.sub(r"\\left|\\right", "", t)
    t = re.sub(r"\\\((.*?)\\\)", r"\1", t, flags=re.S)
    t = re.sub(r"\\\[(.*?)\\\]", r"\1", t, flags=re.S)
    t = t.replace("\\ge", ">=").replace("\\le", "<=").replace("\\ne", "!=")
    t = t.replace("\\div", "/")
    # \sqrt is parked behind a non-letter placeholder so the implicit-product
    # rules below never turn "sqrt(" into "sqrt*(".
    t = t.replace("\\sqrt", "#")
    t = t.replace("\\pi", "pi").replace("\\cdot", "*")
    t = t.replace("{,}", "").replace(",", "").replace("$", "").replace("%", "")
    # Exponents and fractions are rewritten in the SAME loop, alternating, and
    # iterated to a fixed point. Neither can go first on its own: \frac's
    # arguments are matched with a non-recursive [^{}]* pattern, so a \frac
    # holding an exponent (\frac{9a^{4}}{4}) needs the exponent flattened
    # first, while an exponent holding a \frac (^{\frac{2}{3}}) needs the
    # fraction flattened first.
    for _ in range(12):
        new = re.sub(r"\^\{([^{}]*)\}", r"**(\1)", t)
        new = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"((\1)/(\2))", new)
        if new == t:
            break
        t = new
    t = t.replace("^", "**").replace("{", "(").replace("}", ")")
    # Implicit products: after a digit, after a closing paren and after a
    # symbol. Without the last two, "\(x(x+7)\)" and "x**(3)y" parse to
    # nonsense instead of failing loudly.
    t = re.sub(r"(\d)\s*([a-zA-Z(#])", r"\1*\2", t)
    t = re.sub(r"\)\s*([A-Za-z0-9(#])", r")*\1", t)
    t = re.sub(r"(?<=[a-zA-Z])\s*\(", "*(", t)
    t = t.replace("#", "sqrt")
    t = t.replace("*<", "<").replace("*>", ">").replace("*!", "!")
    return t.strip()


def parse_choice(text, loc=None):
    return sympify(latex_to_expr(text), locals=loc or {})


def same(got, other):
    """True when a parsed choice matches the derived answer."""
    if isinstance(got, str):
        return got.strip().lower() in str(other).strip().lower()
    if isinstance(got, Relational) or isinstance(other, Relational):
        return bool(got == other)
    try:
        diff = simplify(other - got)
    except Exception:
        return False
    if diff == 0:
        return True
    # a decimal choice against an exact Rational derivation ("1.8" vs 9/5)
    # differs by a float epsilon rather than by zero
    try:
        val = complex(diff.evalf())
    except Exception:
        return False
    return abs(val) < 1e-9


print("== pass 1: independent sympy derivation")
derived_count = 0
for question in ALL:
    tag = question["n"]

    if tag in MANUAL:
        marker = MANUAL_MARKER[tag]
        text = (question["choices"]["ABCD".index(question["correct"])]
                if question["type"] == "MC" else "")
        check(marker.lower() in text.lower(),
              f"{tag}: MANUAL key {text!r} does not carry {marker!r}")
        continue

    check(tag in DERIVE, f"{tag}: no derivation registered")
    if tag not in DERIVE:
        continue
    got = DERIVE[tag]()
    derived_count += 1

    if question["type"] == "FR":
        ok = False
        for ans in question["answers"]:
            try:
                ok = ok or same(got, parse_choice(ans))
            except Exception:
                ok = ok or ans.strip() == str(got).strip()
        check(ok, f"{tag}: sympy derived {got}, accepted answers are "
                  f"{question['answers']}")
        continue

    text = question["choices"]["ABCD".index(question["correct"])]
    if isinstance(got, str):
        check(same(got, text), f"{tag}: sympy derived {got!r}, key is {text!r}")
    else:
        # Try plain symbols first, then the positive-assumption reading: a
        # symbol declared positive is a *different* Symbol from an undeclared
        # one, so one parse can miss a match that is really there.
        ok = False
        for loc in ({}, {nm: symbols(nm, positive=True)
                         for nm in ("a", "b", "g", "p", "q", "r", "s", "x", "y")}):
            try:
                if same(got, parse_choice(text, loc)):
                    ok = True
                    break
            except Exception:
                pass
        if not ok:
            ok = latex_to_expr(text).replace(" ", "") == str(got).replace(" ", "")
        check(ok, f"{tag}: sympy derived {got}, but choice {question['correct']} "
                  f"is {text!r}")

    # every distractor must be genuinely different from the key
    for i, alt in enumerate(question["choices"]):
        if i == "ABCD".index(question["correct"]):
            continue
        bad = False
        try:
            bad = same(got, alt if isinstance(got, str) else parse_choice(alt))
        except Exception:
            bad = False
        check(not bad, f"{tag}: distractor {'ABCD'[i]} ({alt!r}) matches the key")

print(f"   {derived_count} of {len(ALL)} questions derived by sympy; "
      f"{len(MANUAL)} in MANUAL")

# ---------------------------------------------------------------- shape rules
print("== pass 2: shape and house style")
for nm, md in (("Module 1", MODULE_1), ("Module 2 Easy", MODULE_2_EASY),
               ("Module 2 Hard", MODULE_2_HARD)):
    check(len(md) == 22, f"{nm} has {len(md)} questions, expected 22")

for name, mod in (("M1", MODULE_1), ("M2E", MODULE_2_EASY), ("M2H", MODULE_2_HARD)):
    fr = [z for z in mod if z["type"] == "FR"]
    mc = [z for z in mod if z["type"] == "MC"]
    check(len(fr) == 3, f"{name}: {len(fr)} free-response, the target is exactly 3")
    check(len(mc) == 19, f"{name}: {len(mc)} multiple-choice, expected 19")
    dom = Counter(z["domain"] for z in mod)
    check(dom["ALG"] == 7 and dom["ADV"] == 6 and dom["PSDA"] == 5 and dom["GT"] == 4,
          f"{name}: domain mix is {dict(dom)}, wanted 7 ALG / 6 ADV / 5 PSDA / 4 GT")
    bal = Counter(z["correct"] for z in mc)
    check(max(bal.values()) <= 7, f"{name}: answer key unbalanced {dict(bal)}")
    trig = sum(1 for z in mod if z["skill"] == "GT-TR")
    check(1 <= trig <= 2, f"{name}: {trig} GT-TR questions, wanted 1 or 2")

VALID_SKILLS = {
    "ALG": {"ALG-LE", "ALG-LF", "ALG-LI"},
    "ADV": {"ADV-NF", "ADV-EQ", "ADV-NE"},
    "PSDA": {"PSDA-RP", "PSDA-ST", "PSDA-DI"},
    "GT": {"GT-AV", "GT-LA", "GT-TR"},
}

SPAN = re.compile(r"\\\((.*?)\\\)|\\\[(.*?)\\\]", re.S)

seen_ids = set()
for question in ALL:
    tag = question["n"]
    check(tag not in seen_ids, f"{tag}: duplicate question id")
    seen_ids.add(tag)
    check(question["skill"] in VALID_SKILLS[question["domain"]],
          f"{tag}: skill {question['skill']} is not a {question['domain']} skill")
    check(bool(question.get("check")), f"{tag}: no check note")

    blocks = [question["stem"]] + list(question.get("choices") or [])
    if question["type"] == "MC":
        check(len(question["choices"]) == 4, f"{tag}: needs exactly 4 choices")
        check(len(set(question["choices"])) == 4, f"{tag}: duplicate answer choice")
        check(question["correct"] in "ABCD", f"{tag}: bad answer label")
    else:
        check(bool(question.get("answers")),
              f"{tag}: free response with no accepted answer")

    for blk in blocks:
        # <img> payloads would false-positive on every pattern below; there
        # are none in this build, but strip them so the rule holds if one is
        # ever added.
        blk = re.sub(r"<img[^>]*>", " ", blk)

        check(not blk.strip().startswith("<p>"), f"{tag}: stem is <p>-wrapped")
        check("\u00b0" not in blk, f"{tag}: raw degree glyph, use &deg;")
        spans = [mm.span() for mm in SPAN.finditer(blk)]

        def inside(i, spans=spans):
            return any(aa <= i < bb for aa, bb in spans)

        for mm in re.finditer(r"\^", blk):
            check(inside(mm.start()), f"{tag}: caret outside math mode")
        for mm in re.finditer(r"\bsqrt\s*\(", blk):
            check(False, f"{tag}: plain-text sqrt(")
        for mm in re.finditer(r"[\dA-Za-z)]\s*\*\s*[\dA-Za-z(]", blk):
            check(inside(mm.start()),
                  f"{tag}: asterisk multiplication outside math mode")
        for mm in re.finditer(r"(?<![\d/:])\d+\s*/\s*\d+(?![\d/])", blk):
            check(inside(mm.start()), f"{tag}: slash fraction outside math mode")
        for mm in re.finditer(
                r"\\(pi|frac|sqrt|cdot|div|le|ge|ne|circ|sin|cos|tan|log|ln)\b", blk):
            check(inside(mm.start()), f"{tag}: LaTeX macro outside math mode")
        for mm in re.finditer(r"(!=|<=|>=)", blk):
            check(False, f"{tag}: ASCII comparison operator, use \\ne / \\le / \\ge")
        for mm in re.finditer(r"(?<![A-Za-z])(theta|alpha|beta|lambda)(?![A-Za-z])", blk):
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

    stem = question["stem"]
    if re.search(r"\btables?\b", stem, re.I):
        check("<table" in stem, f"{tag}: mentions a table but has no <table> markup")
    if re.search(r"\b(shown|the figure|graph|chart|plot|diagram|"
                 r"following (?:graph|figure|chart))\b", stem, re.I):
        check("<table" in stem or "<img" in stem,
              f"{tag}: refers to a visual it does not contain")
    if "system" in stem.lower() and len(re.findall(r"=", stem)) >= 2:
        check("<br/>" in stem, f"{tag}: a system of equations must be stacked with <br/>")


# ------------------------------------------------------------------- dedupe
def sig(text):
    tx = re.sub(r"<img[^>]*>", " ", text)
    tx = re.sub(r"<[^>]+>", " ", tx)
    tx = re.sub(r"&[a-z]+;", " ", tx)
    math = []
    for mm in SPAN.findall(tx):
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
    tx = re.sub(r"\\[a-zA-Z]+", " ", tx)
    tx = re.sub(r"[-+]?\d[\d,.]*", "#", tx)
    tokens = (re.sub(r"[^a-z#]+", " ", tx.lower()).strip() + " "
              + " ".join(sorted(set(math)))).split()
    return set(tokens)


def jaccard(aa, bb):
    return len(aa & bb) / max(1, len(aa | bb))


print("== pass 3: template dedupe against production")
prod_path = os.path.join(HERE, "prod_math_stems.json")
if not os.path.exists(prod_path):
    check(False, "prod_math_stems.json is missing — the dedupe pass cannot run")
else:
    prod = json.load(open(prod_path))
    print(f"   comparing against {len(prod)} live Math stems")
    others = [(pq["label"], sig(pq["stem"])) for pq in prod]
    worst = []
    to_read = []
    for question in ALL:
        s0 = sig(question["stem"])
        scored = sorted(((jaccard(s0, o), lab) for lab, o in others),
                        key=lambda z: z[0], reverse=True)
        score, label = scored[0]
        worst.append((score, question["n"], label))
        for sc, lab in scored[:5]:
            if sc >= READ_THRESHOLD:
                to_read.append((sc, question["n"], lab))
        check(score < PROD_THRESHOLD,
              f"{question['n']}: template similarity {score:.2f} to {label}")
    worst.sort(reverse=True)
    print(f"   highest similarity seen: {worst[0][0]:.2f}")
    print("   closest matches:")
    for sc, tag, lab in worst[:8]:
        print(f"     {sc:.2f}  {tag}  vs {lab}")
    to_read.sort(reverse=True)
    print(f"   {len(to_read)} pairs at or above {READ_THRESHOLD:.2f} "
          f"(each one read by hand during authoring):")
    for sc, tag, lab in to_read:
        print(f"     {sc:.2f}  {tag}  vs {lab}")

print("== pass 4: self-collision inside Test 19")
worst_self = (0.0, "", "")
for i in range(len(ALL)):
    for j in range(i + 1, len(ALL)):
        sc = jaccard(sig(ALL[i]["stem"]), sig(ALL[j]["stem"]))
        if sc > worst_self[0]:
            worst_self = (sc, ALL[i]["n"], ALL[j]["n"])
        check(sc < SELF_THRESHOLD,
              f"{ALL[i]['n']} vs {ALL[j]['n']}: internal similarity {sc:.2f}")
print(f"   highest internal similarity: {worst_self[0]:.2f} "
      f"({worst_self[1]} vs {worst_self[2]})")

# A student sees Module 1 plus ONE Module 2 branch, so a setting reused across
# that boundary reads as a repeat even when the mathematics is different. This
# is the check Test 18 was missing when its Easy branch showed the same hop
# kiln twice.
SETTING_WORDS = [
    "peat", "turbary", "turf", "turves", "staithe", "tanner", "tannery",
    "tanning", "hide", "bark", "leather", "charcoal", "billet", "thatch",
    "straw", "eel", "elver", "weir", "saltmarsh", "grazier", "ewe", "lamb",
    "sluice",
    "mill", "miller", "millwright", "millstone", "grind", "grain",
    "wheat", "barley", "flour", "basket", "osier", "withy", "lime",
    "limeburner", "kiln", "limestone", "fen", "drain", "drainage", "pump",
    "sump", "reed", "hurdle",
]
print("== pass 4b: settings disjoint between Module 1 and Module 2")
m1_text = " ".join(z["stem"] + " " + " ".join(z.get("choices") or [])
                   for z in MODULE_1).lower()
m2_text = " ".join(z["stem"] + " " + " ".join(z.get("choices") or [])
                   for z in MODULE_2_EASY + MODULE_2_HARD).lower()
# The boundary has to close as well as open: a bare "\\bfen" matches the
# "fen" inside "fence", which is exactly the silent over-match the \\bpi bug
# was. Plural and participle endings are allowed explicitly instead.
def uses(word, text):
    return re.search(r"\b" + word + r"(s|es|ing|ed|er|ers)?\b", text) is not None


shared = [word for word in SETTING_WORDS
          if uses(word, m1_text) and uses(word, m2_text)]
check(not shared, f"settings used in both Module 1 and a Module 2: {shared}")
print(f"   {len(SETTING_WORDS)} setting keywords checked, {len(shared)} shared")

# ------------------------------------------------------------------- report
print()
print(f"questions: {len(ALL)}")
for label, mod in (("M1 ", MODULE_1), ("M2E", MODULE_2_EASY), ("M2H", MODULE_2_HARD)):
    doms = dict(sorted(Counter(z["domain"] for z in mod).items()))
    keys = dict(sorted(Counter(z["correct"] for z in mod
                               if z["type"] == "MC").items()))
    frs = sum(1 for z in mod if z["type"] == "FR")
    print(f"  {label}: {len(mod)} questions, {frs} FR, domains {doms}, key {keys}")
print(f"skills: {dict(sorted(Counter(z['skill'] for z in ALL).items()))}")

if FAIL:
    print(f"\n{len(FAIL)} FAILURES:")
    for failure in FAIL:
        print("  -", failure)
    raise SystemExit(1)
print("\nALL CHECKS PASSED")
