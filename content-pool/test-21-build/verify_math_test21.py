#!/usr/bin/env python3
"""
Verify the 66 originally-authored Math questions for Test 21.

Four passes, because each has caught a different class of defect in earlier
builds:

 1. Every answer is re-derived with sympy from the question itself, never read
    off the `check` note. A wrong `check` and a wrong key agree with each
    other; only an independent derivation catches that. The pass also asserts
    that no distractor equals the derived value. Anything genuinely outside
    sympy's reach would go in MANUAL with a written justification — Test 21
    has none, because every answer is a value, a form or a named table row.
 2. House style is enforced on the final HTML — the Test 1/2 rules in
    CLAUDE.md, plus the DB-wide rendering checks (no bare `^`, `sqrt(`,
    `*`-as-multiply, slash fractions, ASCII comparison operators or LaTeX
    macros outside a math span).
 3. Template dedupe against every Math stem live in production, not just exact
    duplicates: a question that reuses a template with new numbers is a repeat.
    0.75 fails outright, and every match at or above 0.45 is printed so the
    nearest banked stem can actually be read — Test 18 found nine genuine
    template repeats that all scored below 0.75.
 4. Self-collision among Test 21's own 66 stems, plus a setting check: a
    student sees Module 1 and one Module 2 branch, so no setting keyword may
    appear in both Module 1 and a Module 2 module.

Run:  python3 verify_math_test21.py
      (no DATABASE_URL needed — pass 3 reads the local prod_math_stems.json
      snapshot of the 1,188 Math stems live in production)
"""
import json
import os
import re
import sys
from collections import Counter

from sympy import (Eq, Rational, acos, ceiling, floor, cancel, diff, expand,
                   latex, log, pi, simplify, sin, cos, solve, sqrt, symbols,
                   sympify, tan)

from math_test21 import MODULE_1, MODULE_2_EASY, MODULE_2_HARD, ALL

HERE = os.path.dirname(os.path.abspath(__file__))

# Symbols. Never name one S, E, I, N, O, Q, beta, gamma or zeta and then hand
# it to sympify bare: sympify("S") returns the SingletonRegistry and the
# comparison silently degrades to a string compare. Everything below is either
# built with symbols() explicitly or parsed with an all-letters locals map.
x, y, w, t, h, d, m, n, c, k = symbols("x y w t h d m n c k")
a, b, g, r, s, u, v, p, q = symbols("a b g r s u v p q")
D_ = symbols("D")
XP, YP = symbols("x y", positive=True)

# Every single letter maps to a plain Symbol, so a choice such as
# \(\frac{4D}{r}+2\) cannot pick up sympy's own D, N or S.
BASE_LOCALS = {ch: symbols(ch) for ch in
               "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"}
POS_LOCALS = dict(BASE_LOCALS)
POS_LOCALS.update({nm: symbols(nm, positive=True) for nm in ("a", "b", "x", "y")})

FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)


# ---------------------------------------------------------------- derivations
def h1_01():
    pin, ries = symbols("pin ries")
    sol = solve([Eq(pin + ries, 47), Eq(ries, pin + 3)], [pin, ries])
    return sol[ries] * 210 + sol[pin] * 260


def h1_02():
    slope, inter = symbols("slope inter")
    sol = solve([Eq(2 * slope + inter, 7), Eq(5 * slope + inter, 16)], [slope, inter])
    return "d=" + str(sol[slope]) + "h+" + str(sol[inter])


def h1_05():
    rate = symbols("rate")
    per = solve(Eq(264 - 4 * rate, 148), rate)[0]
    return 264 + 3 * per


def h1_06():
    slope = symbols("slope")
    sl = solve(Eq(46 + 3 * slope, 64), slope)[0]
    return solve(Eq(46 + sl * (t - 2), 100), t)[0]


def h1_09():
    return [z for z in solve(Eq(180 - a ** 2 / 500, 135), a) if z > 0][0]


def h1_11():
    const = solve(Eq(45, k * 30 ** 2), k)[0]
    return const * 40 ** 2


def h1_13():
    return [z for z in solve(Eq(d ** 2 - 4 * d + 15, 75), d) if 0 <= z <= 30][0]


def h1_16():
    rows = [("Ashdown", 62, 91), ("Braylea", 78, 96),
            ("Cowden", 45, 83), ("Denbrook", 70, 102)]
    best = max(rows, key=lambda row: row[2] - row[1])
    return best[1] + best[2]


def h1_19():
    xv = solve(Eq((2 * x + 15) + (3 * x - 10) + (x + 7), 180), x)[0]
    return max([2 * xv + 15, 3 * xv - 10, xv + 7])


def h1_20():
    hyp = sqrt(24 ** 2 + 7 ** 2)
    return simplify(24 / hyp)


def h1_21():
    depth = symbols("depth", positive=True)
    # every drop landing on the funnel mouth ends up in the tube
    return solve(Eq(pi * 10 ** 2 * Rational(12, 10), pi * 2 ** 2 * depth), depth)[0]


def h2e_05():
    return [z for z in (6, 7, 8, 9) if 3 * z - 8 > 16][0]


def h2e_10():
    rows = [(1, 12), (2, 5), (3, 0), (4, -3)]
    return [xv for xv, fv in rows if fv == 0][0]


def h2e_11():
    return [z for z in solve(Eq((n - 7) * (n + 2), 0), n) if z > 0][0]


def h2e_17():
    rows = [("Alder", 120, 7), ("Birch", 96, 11), ("Cedar", 140, 5), ("Dunn", 88, 9)]
    return max(rows, key=lambda row: row[2])[0]


def h2e_18():
    return sorted([38, 45, 41, 52, 39, 47, 44])[3]


def h2h_01():
    sol = solve([Eq(2 * x + 5 * y, 31), Eq(4 * x - 3 * y, 23)], [x, y])
    return sol[x] / sol[y]


def h2h_02():
    slope = solve(Eq(4 * x - 6 * y, 15), y)[0].coeff(x)
    perp = -1 / slope
    inter = symbols("inter")
    return solve(Eq(-1, perp * 8 + inter), inter)[0]


def h2h_03():
    return len([i for i in range(-200, 400) if 7 * i - 4 > 3 * i + 16 and 2 * i + 5 <= 41])


def h2h_04():
    return solve(Eq(Rational(20, 100) * 45 + Rational(50, 100) * x,
                    Rational(32, 100) * (45 + x)), x)[0]


def h2h_05():
    slope, inter = symbols("slope inter")
    sol = solve([Eq(-4 * slope + inter, 21), Eq(6 * slope + inter, -9)], [slope, inter])
    return sol[slope] + sol[inter]


def h2h_06():
    xv = solve(Eq(2 * x + 3 * 2, 8), x)[0]
    return solve(Eq(4 * xv + k * 2, 20), k)[0]


def h2h_08():
    fx = (x + 7) / 2
    gx = x ** 2 - 1
    return gx.subs(x, fx.subs(x, 11))


def h2h_11():
    return solve(Eq(8 ** x / 4 ** (x - 3), 32), x)[0]


def h2h_13():
    pv, qv = symbols("pv qv")
    poly = x ** 2 + pv * x + qv
    sol = solve([Eq(diff(poly, x).subs(x, 5), 0), Eq(poly.subs(x, 5), -14)], [pv, qv])
    return sol[pv] + sol[qv]


def h2h_14():
    other = symbols("other")
    return solve(Eq(8 * 34 + 58 + other, 10 * Rational(392, 10)), other)[0]


def h2h_19():
    scale = Rational(9 + 6, 9)
    return 12 * scale


def h2h_20():
    rad = symbols("rad", positive=True)
    rv = solve(Eq(2 * pi * rad ** 2, 72 * pi), rad)[0]
    return Rational(2, 3) * pi * rv ** 3


def h2h_21():
    ang_a = acos(Rational(7, 25))
    return simplify(sin(pi / 2 - ang_a))


def h2h_22():
    side = symbols("side", positive=True)
    sv = solve(Eq(side ** 2 * 30, 12000), side)[0]
    return sv ** 2 + 4 * sv * 30


DERIVE = {
 "H1-01": h1_01,
 "H1-02": h1_02,
 "H1-03": lambda: solve(Eq(4 * b + 18, 210), b)[0],
 "H1-04": lambda: solve(Eq(3 * d - 24, 2 * (d + 6)), d)[0],
 "H1-05": h1_05,
 "H1-06": h1_06,
 "H1-07": lambda: ceiling(Rational(294 - 4 * 45, 36)),
 "H1-08": lambda: expand((3 * n + 4) ** 2 - (9 * n ** 2 + 7)),
 "H1-09": h1_09,
 "H1-10": lambda: (Rational(15, 10) ** 2 - 1) * 100,
 "H1-11": h1_11,
 "H1-12": lambda: solve(Eq(D_, r * (s - 2) / 4), s)[0],
 "H1-13": h1_13,
 "H1-14": lambda: Rational(738, 9) * 4,
 "H1-15": lambda: solve(Eq(Rational(88, 100) * m, 2024), m)[0],
 "H1-16": h1_16,
 "H1-17": lambda: Rational((20 + 50 + 30) * 100, 100 + 20 + 130 + 50 + 70 + 30),
 "H1-18": lambda: Rational(14 * 205 + 6 * 240, 20),
 "H1-19": h1_19,
 "H1-20": h1_20,
 "H1-21": h1_21,
 "H1-22": lambda: 9 * 5 * 4 + Rational(1, 2) * 5 * 2 * 9,

 "H2E-01": lambda: solve(Eq(6 * t + 14, 92), t)[0],
 "H2E-02": lambda: 45 * 16,
 "H2E-03": lambda: 12 * 6 + 35,
 "H2E-04": lambda: Rational(19 - 7, 6 - 2),
 "H2E-05": h2e_05,
 "H2E-06": lambda: solve(Eq(320 - 24 * d, 152), d)[0],
 "H2E-07": lambda: 24 - 9,
 "H2E-08": lambda: expand(4 * (3 * k + 5) - 7 * k),
 "H2E-09": lambda: expand(x ** 2 + 9 * x + 20),
 "H2E-10": h2e_10,
 "H2E-11": h2e_11,
 "H2E-12": lambda: 8 * 3 ** 3,
 "H2E-13": lambda: simplify(XP ** 9 / XP ** 4),
 "H2E-14": lambda: Rational(78, 6),
 "H2E-15": lambda: Rational(2, 5) * 140,
 "H2E-16": lambda: 14 + 9 + 17 + 12,
 "H2E-17": h2e_17,
 "H2E-18": h2e_18,
 "H2E-19": lambda: sqrt((11 - 3) ** 2 + (4 - (-2)) ** 2),
 "H2E-20": lambda: pi * 6 ** 2,
 "H2E-21": lambda: 30 * 24 * 12,
 "H2E-22": lambda: Rational(8, 15),

 "H2H-01": h2h_01,
 "H2H-02": h2h_02,
 "H2H-03": h2h_03,
 "H2H-04": h2h_04,
 "H2H-05": h2h_05,
 "H2H-06": h2h_06,
 "H2H-07": lambda: floor(Rational(240 - 12 * 14, 6)),
 "H2H-08": h2h_08,
 "H2H-09": lambda: cancel((6 * x ** 2 + 7 * x - 3) / (2 * x + 3)),
 "H2H-10": lambda: solve(Eq(x ** 2 - 6 * x + 13, 2 * x - 3), x)[0],
 "H2H-11": h2h_11,
 "H2H-12": lambda: simplify((27 * XP ** 12) ** Rational(1, 3)),
 "H2H-13": h2h_13,
 "H2H-14": h2h_14,
 "H2H-15": lambda: Rational(84, 84 + 96 + 60),
 "H2H-16": lambda: 5000 * Rational(106, 100) * Rational(94, 100),
 "H2H-17": lambda: Rational(200, 3 * 60 + 20) * (5 * 60 + 15),
 "H2H-18": lambda: Rational(15 - 3, 40 - 3),
 "H2H-19": h2h_19,
 "H2H-20": h2h_20,
 "H2H-21": h2h_21,
 "H2H-22": h2h_22,
}

# Nothing in Test 21 resists a symbolic derivation: every answer is a value, an
# algebraic form, an equation built from sympy-computed coefficients, or a
# named table row picked out by a sympy/Python comparison over the printed
# data. MANUAL is therefore empty, and pass 1 covers all 66.
MANUAL = {}


def latex_to_expr(text):
    """Turn one answer choice into something sympify can read."""
    t = text.replace("&deg;", "").replace("&gt;", ">").replace("&lt;", "<")
    t = re.sub(r"\\left|\\right", "", t)
    t = re.sub(r"\\\((.*?)\\\)", r"\1", t, flags=re.S)
    # Exponents first: \frac{8x^{6}}{y^{3}} has braces nested inside the
    # numerator, and a non-recursive \frac pattern silently fails to match it.
    # Rewriting ^{...} to **(...) flattens the nesting so \frac then matches.
    t = re.sub(r"\^\{([^{}]*)\}", r"**(\1)", t)
    for _ in range(3):
        t = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"((\1)/(\2))", t)
    t = t.replace("\\pi", "pi").replace("\\cdot", "*").replace("\\sqrt", "sqrt")
    t = t.replace("{,}", "").replace(",", "").replace("$", "").replace("%", "")
    t = t.replace("^", "**").replace("{", "(").replace("}", ")")
    # implicit multiplication: after a digit, after a closing paren, and after a
    # lone symbol — \(x(x+7)\) parses to nonsense without the last of the three,
    # and the lookbehind keeps sqrt( / cos( from being mangled.
    t = re.sub(r"(\d)\s*([a-zA-Z(])", r"\1*\2", t)
    t = re.sub(r"\)\s*\(", ")*(", t)
    t = re.sub(r"(?<![a-zA-Z])([a-zA-Z])\s*\(", r"\1*(", t)
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
        # A form, an equation or a named row: the derivation builds the exact
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

print(f"   {derived} of {len(ALL)} re-derived with sympy; "
      f"{len(MANUAL)} in MANUAL")

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

    for blk in blocks:
        bare = re.sub(r"<img[^>]*>", " ", blk)  # base64 payloads match every rule below
        check(not bare.strip().startswith("<p>"), f"{tag}: stem is <p>-wrapped")
        check("\u00b0" not in bare, f"{tag}: raw degree glyph, use &deg;")
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
prod_path = os.path.join(HERE, "prod_math_stems.json")
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
    check(False, "prod_math_stems.json is missing — the dedupe pass cannot run")

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
# across that boundary shows the same scene twice in one sitting. Test 18 had
# two Module 2 Easy items with distinct maths on a Module 1 item's setting.
SETTING_KEYWORDS = [
    "vineyard", "grape", "riesling", "pinot", "veraison", "must",
    "cart", "wheelwright", "dray", "spoke", "wheel",
    "rain gauge", "weather station", "rainfall",
    "tobacco", "curing", "flue",
    "saddler", "harness", "strap", "billet",
    "hay", "bale", "rick",
    "seed", "chaff", "germination",
    "silk", "skein", "reeler", "reeling", "cocoon", "moth",
    "spectacle", "lens", "optician", "grinder", "grinding",
    "observatory", "dome", "telescope", "astrograph", "coelostat",
    "darkroom", "photographic", "plate", "contact sheet", "developer",
    "exposure", "print",
    "spring", "steel strip",
]
m1_text = " ".join(qq["stem"].lower() for qq in MODULE_1)
m2_text = " ".join(qq["stem"].lower() for qq in MODULE_2_EASY + MODULE_2_HARD)
shared = [kwd for kwd in SETTING_KEYWORDS if kwd in m1_text and kwd in m2_text]
check(not shared, f"settings reused across Module 1 and a Module 2 branch: {shared}")
in_m1 = [kwd for kwd in SETTING_KEYWORDS if kwd in m1_text]
in_m2 = [kwd for kwd in SETTING_KEYWORDS if kwd in m2_text]
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
print(f"highest Jaccard vs production: {worst_prod:.2f}   within Test 21: {worst_self:.2f}")

if FAIL:
    print(f"\n{len(FAIL)} FAILURES:")
    for f in FAIL:
        print("  -", f)
    raise SystemExit(1)
print("\nALL CHECKS PASSED")
