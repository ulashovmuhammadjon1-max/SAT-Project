#!/usr/bin/env python3
"""
Verify the 66 originally-authored Math questions for Test 27.

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
    macros outside a math span).
 3. Template dedupe against every Math stem live in production. NOTE: this
    reads the ROOT corpus ../prod_math_stems.json (1,386 stems), not a copy
    inside this directory. 0.75 fails outright, and every match at or above
    0.45 is printed so the nearest banked stem can actually be READ — the
    Test 18-21 finding is that a threshold decides what to read, not what to
    accept: 57 genuine template repeats across those four builds all but three
    scored BELOW 0.75.
 4. Self-collision among Test 27's own 66 stems, plus a setting check: a
    student sees Module 1 and one Module 2 branch, so no setting keyword may
    appear in both Module 1 and a Module 2 module.

Run:  python3 verify_math_test27.py
"""
import json
import os
import re

from sympy import (Abs, Eq, Rational, atan, ceiling, floor, cancel, expand,
                   factor, nsimplify, pi, simplify, sin, solve, sqrt, symbols,
                   sympify, together)

from math_test27 import MODULE_1, MODULE_2_EASY, MODULE_2_HARD, ALL

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# Symbols. Never name one S, E, I, N, O, Q, beta, gamma or zeta and then hand
# it to sympify bare: sympify("S") returns the SingletonRegistry and the
# comparison silently degrades to a string compare. Everything below is either
# built with symbols() explicitly or parsed with an all-letters locals map.
x, y, w, t, h, d, m, n, c, k = symbols("x y w t h d m n c k")
a, b, g, r, s, u, v, p, q = symbols("a b g r s u v p q")

BASE_LOCALS = {ch: symbols(ch) for ch in
               "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"}
POS_LOCALS = dict(BASE_LOCALS)
POS_LOCALS.update({nm: symbols(nm, positive=True) for nm in ("a", "b", "n", "x", "y")})

FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)


# ---------------------------------------------------------------- derivations
def h1_01():
    west = symbols("west")
    wv = solve(Eq(west + (2 * west + 260), 4160), west)[0]
    return 2 * wv + 260


def h1_02():
    blocks = symbols("blocks")
    return solve(Eq(48 + Rational(60, 100) * blocks, Rational(135, 100) * blocks), blocks)[0]


def h1_03():
    days = symbols("days")
    return solve(Eq(18 * days + 40, 24 * days + 16), days)[0]


def h1_04():
    rate = symbols("rate")
    # 186 tonnes on day 8, 132 on day 26
    rv = solve(Eq(186 + rate * (26 - 8), 132), rate)[0]
    return solve(Eq(186 + rv * (d - 8), 0), d)[0]


def h1_05():
    bu = symbols("bu")
    exact = solve(Eq(Rational(240, 100) * bu - (560 + Rational(35, 100) * bu), 900), bu)[0]
    return ceiling(exact)


def h1_06():
    wk = symbols("wk")
    exact = solve(Eq(310 - Rational(46, 10) * wk, Rational(15, 100) * 310), wk)[0]
    return ceiling(exact)


def h1_07():
    large = symbols("large")
    return solve(Eq(42 * large + 26 * (96 - large), 3232), large)[0]


def h1_09():
    npos = symbols("n", positive=True)
    return simplify((8 * npos ** 6 / 27) ** Rational(2, 3))


def h1_10():
    return [z for z in solve(Eq(h ** 2 - 18 * h + 96, 24), h) if 0 <= z <= 9][0]


def h1_11():
    model = lambda wk: 240 * Rational(3, 4) ** wk
    return model(1) - model(2)


def h1_12():
    dep = symbols("dep", positive=True)
    return solve(Eq(9 * sqrt(dep), 63), dep)[0]


def h1_13():
    lo, hi = sorted(solve(Eq(-s ** 2 + 22 * s - 40, 0), s))
    return max(i for i in range(-50, 200) if lo < i < hi)


def h1_14():
    rows = [("Ashwell", 480, 396), ("Barrow", 350, 301),
            ("Cranford", 620, 496), ("Deeping", 540, 459)]
    return max(rows, key=lambda row: Rational(row[1] - row[2], row[1]))[0]


def h1_15():
    rows = [(14, 5), (15, 9), (16, 12), (17, 8), (18, 7)]
    vals = [thick for thick, days in rows for _ in range(days)]
    assert len(vals) % 2 == 1
    return vals[len(vals) // 2]


def h1_16():
    block = Rational(5, 10) * Rational(4, 10) * Rational(3, 10) * 920
    return floor(1150 / block)


def h1_19():
    dep = symbols("dep")
    return solve(Eq(Rational(45, 10) * Rational(32, 10) * dep, Rational(216, 100)), dep)[0]


def h1_20():
    return sqrt(16 ** 2 + Rational(16, 2) ** 2)


def h1_22():
    return simplify(sin(atan(Rational(7, 24))))


def h2e_02():
    boxes = symbols("boxes")
    return solve(Eq(8 * boxes + 4, 236), boxes)[0]


def h2e_11():
    xr = symbols("xr", real=True)
    return [z for z in solve(Eq(xr ** 3, 125), xr) if z.is_real][0]


def h2e_13():
    return factor(4 * y ** 2 - 36)


def h2e_14():
    rows = [("Fennhaven", 2140), ("Garrow", 3480), ("Halden", 2905), ("Ivory Quay", 3260)]
    return max(rows, key=lambda row: row[1])[0]


def h2e_20():
    nn = symbols("nn")
    return solve(Eq(3 * nn + 4 * nn + 5 * nn, 180), nn)[0]


def h2h_01():
    yv = solve(Eq(3 * 3 - 2 * y, 5), y)[0]
    av = symbols("av")
    return solve(Eq(av * 3 + 4 * yv, 26), av)[0]


def h2h_02():
    return n * t + (n - 1) * c


def h2h_03():
    large, small = symbols("large small")
    return solve([Eq(large + small, 348),
                  Eq((large - 40) - (small + 40), 26)], [large, small])[large]


def h2h_04():
    apos = symbols("a", positive=True)
    slope = (11 * apos - 3 * apos) / (3 * apos - apos)
    inter = symbols("inter")
    return simplify(solve(Eq(3 * apos, slope * apos + inter), inter)[0])


def h2h_05():
    mm = symbols("mm", real=True)
    lo, hi = sorted(solve(Eq(Abs(mm - 38), Rational(5, 2)), mm))
    return "\\(%s\\le m\\le %s\\)" % (float(lo), float(hi))


def h2h_06():
    slope = Rational(17 - 5, 4 - 1)
    inter = -5          # the line passes through (0, -5)
    return slope + inter


def h2h_07():
    mack = symbols("mack")
    exact = solve(Eq(Rational(4, 10) * 300 + Rational(7, 10) * mack, 280), mack)[0]
    return floor(exact)


def h2h_08():
    apos = symbols("ap", positive=True)
    av = solve(Eq(2 * apos ** 2 - 5, 45), apos)[0]
    return 2 * (2 * av) ** 2 - 5


def h2h_09():
    bb, cc = 14, 58
    return (x + Rational(bb, 2)) ** 2 + (cc - Rational(bb, 2) ** 2)


def h2h_10():
    kk = symbols("kk", positive=True)
    # the square of a binomial <=> the discriminant vanishes
    return solve(Eq(kk ** 2 - 4 * 4 * 49, 0), kk)[0]


def h2h_11():
    return simplify(3 ** Rational(20, 5))


def h2h_12():
    xp = symbols("xp", positive=True)
    vals = {simplify(z + 1 / z) for z in solve(Eq(xp ** 2 + 1 / xp ** 2, 23), xp)
            if z.is_real and z > 0}
    assert len(vals) == 1, vals
    return vals.pop()


def h2h_13():
    lo, hi = sorted(solve(Eq(-3 * x ** 2 + 42 * x - 135, 0), x))
    return hi - lo


def h2h_14():
    ww = symbols("ww")
    return solve(Eq(45 * Rational(42, 10) + 6 * ww,
                    Rational(45, 10) * (45 + ww)), ww)[0]


def h2h_15():
    per_rack = Rational(45, 3)
    return Rational(1200, 1) / (per_rack * 5)


def h2h_16():
    rows = [("3.0 to 3.4", 12), ("3.5 to 3.9", 23), ("4.0 to 4.4", 31), ("4.5 to 4.9", 14)]
    vals = [name for name, cnt in rows for _ in range(cnt)]
    lo, hi = vals[len(vals) // 2 - 1], vals[len(vals) // 2]
    assert lo == hi, (lo, hi)
    return lo


def h2h_20():
    # right triangle with legs 12 and 5 -> hypotenuse 13, area 30
    hyp = sqrt(12 ** 2 + 5 ** 2)
    ratio = Rational(39, 1) / hyp
    return Rational(1, 2) * 12 * 5 * ratio ** 2


def h2h_21():
    return 12 * 7 * 3 - 4 * (Rational(1, 2) * Rational(1, 2) * 3)


def h2h_22():
    bc = symbols("bc", positive=True)
    return simplify(bc / (3 * bc))


DERIVE = {
 "H1-01": h1_01,
 "H1-02": h1_02,
 "H1-03": h1_03,
 "H1-04": h1_04,
 "H1-05": h1_05,
 "H1-06": h1_06,
 "H1-07": h1_07,
 "H1-08": lambda: expand((5 * p + 6) * (2 * p - 3)),
 "H1-09": h1_09,
 "H1-10": h1_10,
 "H1-11": h1_11,
 "H1-12": h1_12,
 "H1-13": h1_13,
 "H1-14": h1_14,
 "H1-15": h1_15,
 "H1-16": h1_16,
 "H1-17": lambda: Rational(168, 210),
 "H1-18": lambda: Rational(46000 * 1840, 1472),
 "H1-19": h1_19,
 "H1-20": h1_20,
 "H1-21": lambda: Rational(6 * 45 * 4, 10 * 10) / Rational(9, 10),
 "H1-22": h1_22,

 "H2E-01": lambda: 340 - 12 * 9,
 "H2E-02": h2e_02,
 "H2E-03": lambda: Rational(153, 9),
 "H2E-04": lambda: Rational(46, 10) - Rational(5, 100) * 12,
 "H2E-06": lambda: floor(Rational(45, 3)),
 "H2E-07": lambda: 7 * 22 + 40,
 "H2E-08": lambda: factor(15 * p + 35),
 "H2E-09": lambda: simplify(sqrt(81 * symbols("b", positive=True) ** 4)),
 "H2E-10": lambda: Rational(120, 8),
 "H2E-11": h2e_11,
 "H2E-12": lambda: Rational(200, 7 + 3),
 "H2E-13": h2e_13,
 "H2E-14": h2e_14,
 "H2E-15": lambda: Rational(12, 60) * 100,
 "H2E-16": lambda: Rational(25, 10) * 14,
 "H2E-17": lambda: Rational(36, 36 + 27 + 17),
 "H2E-18": lambda: 46 + 38 + 52 + 29,
 "H2E-19": lambda: Rational(1, 2) * 4 * Rational(15, 10) * 6,
 "H2E-20": h2e_20,
 "H2E-21": lambda: Rational(9, 10) ** 2 * 7,
 "H2E-22": lambda: 18 * sin(pi / 6),

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
 "H2H-17": lambda: Rational(84, 120),
 "H2H-18": lambda: 5 * solve(Eq(4 * 5 * k, 5 * (3 * k + 48)), k)[0],
 "H2H-19": lambda: pi * 60 * 100,
 "H2H-20": h2h_20,
 "H2H-21": h2h_21,
 "H2H-22": h2h_22,
}

# The one item whose answer is a sentence rather than a value. sympy still does
# the arithmetic that decides it — 6r + 24 evaluated at r = 0 is 24, so the
# constant term is the count with no extra rail fitted — but choosing which of
# four English sentences says that is a reading judgement, not a computation,
# so it is recorded here rather than pretended into pass 1.
MANUAL = {
 "H2E-05": ("Interpretation of the constant term of 6r + 24. sympy confirms "
            "(6*r + 24).subs(r, 0) == 24 and that the coefficient of r is 6, which "
            "makes 24 the number hung before any extra rail is fitted and 6 the "
            "number each rail adds; matching that to the keyed sentence is a "
            "reading step. Verified below by an explicit substitution check."),
}


def manual_h2e_05():
    """The arithmetic behind the keyed interpretation, done by sympy."""
    rr = symbols("rr")
    expr = 6 * rr + 24
    check(expr.subs(rr, 0) == 24, "H2E-05: constant term is not 24")
    check(expr.coeff(rr) == 6, "H2E-05: coefficient of r is not 6")
    q = [z for z in ALL if z["n"] == "H2E-05"][0]
    keyed = q["choices"]["ABCD".index(q["correct"])]
    check("before any extra rail" in keyed,
          f"H2E-05: keyed choice is not the constant-term reading: {keyed!r}")


FUNCTION_NAMES = {"sqrt", "pi", "sin", "cos", "tan", "log", "ln", "exp", "Abs"}


def split_runs(text):
    """Split a run of two or more letters into an implicit product.

    Without this `\\frac{uv}{u+v}` parses as a symbol named `uv` and the key
    silently fails to match — the failure mode recorded in CLAUDE.md. Function
    and constant names are exempt, or `sqrt` becomes s*q*r*t.
    """
    def repl(mo):
        run = mo.group(0)
        if run in FUNCTION_NAMES:
            return run
        return "*".join(run)
    return re.sub(r"[A-Za-z]{2,}", repl, text)


def latex_to_expr(text):
    """Turn one answer choice into something sympify can read."""
    t = text.replace("&deg;", "").replace("&gt;", ">").replace("&lt;", "<")
    t = re.sub(r"\\left|\\right", "", t)
    t = re.sub(r"\\\((.*?)\\\)", r"\1", t, flags=re.S)
    # Exponents and fractions nest either way round — a fraction can sit inside
    # an exponent as readily as an exponent inside a fraction — so neither
    # rewrite can simply go first. Alternate them to a fixed point.
    for _ in range(6):
        before = t
        t = re.sub(r"\^\{([^{}]*)\}", r"**(\1)", t)
        t = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"((\1)/(\2))", t)
        if t == before:
            break
    t = t.replace("\\pi", "pi").replace("\\cdot", "*").replace("\\sqrt", "sqrt")
    t = t.replace("\\le", "<=").replace("\\ge", ">=").replace("\\ne", "!=")
    t = t.replace("{,}", "").replace(",", "").replace("$", "").replace("%", "")
    t = t.replace("^", "**").replace("{", "(").replace("}", ")")
    t = split_runs(t)
    # implicit multiplication: after a digit, after a closing paren, and after a
    # lone symbol — \(x(x+7)\) parses to nonsense without the last of the three,
    # and the lookbehind keeps sqrt( / cos( from being mangled.
    t = re.sub(r"(\d)\s*([a-zA-Z(])", r"\1*\2", t)
    t = re.sub(r"\)\s*\(", ")*(", t)
    t = re.sub(r"\)\s*([a-zA-Z])", r")*\1", t)
    t = re.sub(r"(?<![a-zA-Z*])([a-zA-Z])\s*\(", r"\1*(", t)
    t = t.replace("**(", "@@(").replace("*(", "*(").replace("@@(", "**(")
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
        # A form, an interval or a named row: the derivation builds the exact
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

manual_h2e_05()
print(f"   {derived} of {len(ALL)} re-derived with sympy; "
      f"{len(MANUAL)} in MANUAL (each with a written justification)")

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
    dom = {}
    for qq in mod:
        dom[qq["domain"]] = dom.get(qq["domain"], 0) + 1
    check(dom.get("ALG") == 7 and dom.get("ADV") == 6 and dom.get("PSDA") == 5
          and dom.get("GT") == 4,
          f"{name}: domain mix is {dom}, wanted 7 ALG / 6 ADV / 5 PSDA / 4 GT")
    bal = {}
    for qq in mc:
        bal[qq["correct"]] = bal.get(qq["correct"], 0) + 1
    check(max(bal.values()) <= 7, f"{name}: answer key unbalanced {bal}")
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
        bare = re.sub(r"<[^>]+>", " ", bare)    # table markup carries no math
        check(not blk.strip().startswith("<p>"), f"{tag}: stem is <p>-wrapped")
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

    # provenance: nothing from the structural template may survive
    for blk in blocks + [qq.get("check", "")]:
        check("T21" not in blk and "Test 21" not in blk,
              f"{tag}: Test 21 provenance string survived into the content")

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
prod_path = os.path.join(ROOT, "prod_math_stems.json")   # ROOT corpus, read only
worst_prod = 0.0
if os.path.exists(prod_path):
    prod = json.load(open(prod_path))
    print(f"   comparing against {len(prod)} live Math stems ({prod_path})")
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
    check(False, f"{prod_path} is missing — the dedupe pass cannot run")

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
# Every keyword below is a term that cannot carry an everyday sense in this
# content. Deliberately NOT used as keywords: "salt", "ice", "cure", "rind",
# "cave", "block" and "wheel" on their own — each is either ordinary English or
# a word whose other sense would fire on the wrong module, which is the same
# family of bug as \bfen matching "fence" and \bpi never matching at all. Where
# a bare word is unavoidable it is anchored to its compound ("ice house",
# "cheese cave").
SETTING_KEYWORDS = [
    # Module 1 territory
    "saltworks", "salt pan", "evaporating pan", "brine", "bushel", "sea water",
    "ice house", "ice gang", "ice saw", "ice merchant", "ice warden", "sledge",
    "root cellar", "cartload", "potato", "turnip", "sprouted",
    # Module 2 territory
    "smokehouse", "smoking", "smoke", "herring", "mackerel", "curer",
    "hearth", "rack", "flue", "draught", "chimney",
    "cheese", "affineur", "ripening", "truckle", "baffle", "moulds",
]
m1_text = " ".join(qq["stem"].lower() for qq in MODULE_1)
m2_text = " ".join(qq["stem"].lower() for qq in MODULE_2_EASY + MODULE_2_HARD)


def has(kwd, text):
    """Prefix match anchored at a word boundary on the LEFT and, for anything
    that could be a prefix of an unrelated word, a boundary on the right too.

    "smoking" must catch "smokings" but "rack" must not catch "bracket" and
    "moth" must not catch "months" — the silent over-match the \\bpi\\b bug was
    made of. A left-only \\b is safe here because every keyword is either a
    whole word or a compound whose continuation is a plural or an inflection.
    """
    return re.search(r"\b" + re.escape(kwd) + r"(?![a-z])" if kwd in ("rack", "smoke")
                     else r"\b" + re.escape(kwd), text) is not None


shared = [kwd for kwd in SETTING_KEYWORDS if has(kwd, m1_text) and has(kwd, m2_text)]
check(not shared, f"settings reused across Module 1 and a Module 2 branch: {shared}")
in_m1 = [kwd for kwd in SETTING_KEYWORDS if has(kwd, m1_text)]
in_m2 = [kwd for kwd in SETTING_KEYWORDS if has(kwd, m2_text)]
print(f"   {len(in_m1)} setting keywords in Module 1, {len(in_m2)} in Module 2, "
      f"{len(shared)} shared")

# ------------------------------------------------------------------- report
from collections import Counter
print()
print(f"questions: {len(ALL)}   M1 domains: {dict(Counter(qq['domain'] for qq in MODULE_1))}")
print(f"                    M2E domains: {dict(Counter(qq['domain'] for qq in MODULE_2_EASY))}")
print(f"                    M2H domains: {dict(Counter(qq['domain'] for qq in MODULE_2_HARD))}")
print(f"skills: {dict(sorted(Counter(qq['skill'] for qq in ALL).items()))}")
print(f"answer key M1:  {dict(sorted(Counter(qq['correct'] for qq in MODULE_1 if qq['type']=='MC').items()))}")
print(f"answer key M2E: {dict(sorted(Counter(qq['correct'] for qq in MODULE_2_EASY if qq['type']=='MC').items()))}")
print(f"answer key M2H: {dict(sorted(Counter(qq['correct'] for qq in MODULE_2_HARD if qq['type']=='MC').items()))}")
print(f"highest Jaccard vs production: {worst_prod:.2f}   within Test 27: {worst_self:.2f}")

if FAIL:
    print(f"\n{len(FAIL)} FAILURES:")
    for f in FAIL:
        print("  -", f)
    raise SystemExit(1)
print("\nALL CHECKS PASSED")
