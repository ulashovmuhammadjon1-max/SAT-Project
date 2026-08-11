#!/usr/bin/env python3
"""
Verify the 66 originally-authored Math questions for Test 24.

Four passes, because each has caught a different class of defect in earlier
builds:

 1. Every answer is re-derived with sympy from the question itself, never read
    off the `check` note. A wrong `check` and a wrong key agree with each
    other; only an independent derivation catches that. The pass also asserts
    that no distractor equals the derived value. Anything genuinely outside
    sympy's reach would go in MANUAL with a written justification — Test 24
    has none, because every answer is a value, an algebraic form, an equation
    built from sympy-computed coefficients, or a named table row picked out by
    a comparison over the printed data.
 2. House style on the final HTML — the Test 1/2 rules in CLAUDE.md plus the
    DB-wide rendering checks (no bare `^`, `sqrt(`, `*`-as-multiply, slash
    fractions, ASCII comparison operators or LaTeX macros outside a math span).
    `<img>` tags are stripped first: a base64 payload matches every one of
    those patterns.
 3. Template dedupe against every Math stem live in production. The corpus is
    the READ-ONLY snapshot at the content-pool ROOT (`../prod_math_stems.json`,
    1,386 stems), not a local copy — the template's own verifier reads a stale
    per-directory copy and this one deliberately does not.

    0.75 fails outright, but the threshold is triage, not a verdict. Across
    Tests 18-21 fifty-seven Math questions were rewritten as genuine template
    repeats and all but three scored BELOW 0.75, because a repeat that changes
    the setting words while keeping the mathematics scores *low* precisely
    because it changed the words. Every match at or above 0.45 is therefore
    printed so it can be read and judged by hand.
 4. Self-collision among Test 24's own 66 stems, plus the cross-module setting
    check: a student sees Module 1 and exactly one Module 2 branch, so no
    setting keyword may appear in both Module 1 and a Module 2 module.

Run:  python3 verify_math_test24.py     (no DATABASE_URL needed)
"""
import json
import os
import re
import sys
from collections import Counter

from sympy import (Abs, Eq, Rational, ceiling, floor, cancel, diff, expand,
                   nsimplify, pi, simplify, sin, cos, solve, sqrt, symbols,
                   sympify, tan)

from math_test24 import MODULE_1, MODULE_2_EASY, MODULE_2_HARD, ALL

HERE = os.path.dirname(os.path.abspath(__file__))

# Symbols. Never name one S, E, I, N, O, Q, beta, gamma or zeta and then hand
# it to sympify bare: sympify("S") returns the SingletonRegistry and the
# comparison silently degrades to a string compare. Everything below is either
# built with symbols() explicitly or parsed with an all-letters locals map.
x, y, w, t, d, m, n, c, k = symbols("x y w t d m n c k")
a, b, g, r, s, u, v, p, q, L = symbols("a b g r s u v p q L")

BASE_LOCALS = {ch: symbols(ch) for ch in
               "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"}
POS_LOCALS = dict(BASE_LOCALS)
POS_LOCALS.update({nm: symbols(nm, positive=True) for nm in ("a", "b", "x", "y", "p", "q")})

FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)


# ---------------------------------------------------------------- Module 1
def h1_01():
    light = symbols("light")
    lv = solve(Eq(light + (light + 40) + light / 2, 720), light)[0]
    return lv / 2


def h1_02():
    rate, fixed = symbols("rate fixed")
    sol = solve([Eq(fixed + 14 * rate, 89), Eq(fixed + 22 * rate, 113)], [rate, fixed])
    return sol[fixed] + 9 * sol[rate]


def h1_03():
    return ceiling(Rational(910 - 216, 38))


def h1_04():
    return 3 * solve(Eq(6 * (y - 4), 2 * y + 44), y)[0]


def h1_05():
    rate, start = symbols("rate start")
    sol = solve([Eq(start + 4 * rate, 220), Eq(start + 16 * rate, 172)], [rate, start])
    return solve(Eq(sol[start] + sol[rate] * t, 100), t)[0]


def h1_06():
    hl, hh = symbols("hl hh")
    sol = solve([Eq(hl + hh, 9), Eq(30 * hl + 18 * hh, 222)], [hl, hh])
    return sol[hh]


def h1_07():
    return floor((512 - 146 - 40 * Rational(8, 10)) / Rational(35, 10))


def h1_09():
    dd = symbols("dd")
    return [z for z in solve(Eq(240 - dd ** 2 / 80, 195), dd) if 0 <= z <= 80][0]


def h1_10():
    model = 2 * x ** 2 - 16 * x + 46
    lo = solve(Eq(diff(model, x), 0), x)[0]
    return model.subs(x, lo)


def h1_11():
    # (9y^2-64)/(3y+8) is equivalent to 3y-c; recover c from the quotient.
    quo = cancel((9 * y ** 2 - 64) / (3 * y + 8))
    return simplify(3 * y - quo)


def h1_12():
    fx = 2.4 * x + 11
    at = solve(Eq(fx, 131), x)[0]
    return nsimplify(fx.subs(x, at + 25))


def h1_13():
    return max(solve(Eq(90 - (x - 6) ** 2, 65), x))


def h1_15():
    whole = symbols("whole")
    return solve(Eq(Rational(65, 100) * Rational(80, 100) * whole, 195), whole)[0]


def h1_17():
    rows = [("Ashcombe", 480, 1200), ("Bardsley", 520, 1352),
            ("Coldharbour", 640, 1536), ("Denhurst", 700, 1890)]
    return max(rows, key=lambda row: Rational(row[2], row[1]))[0]


def h1_18():
    data = [4, 9, 6, 4, 11, 7, 4]
    ordered = sorted(data)
    median = ordered[len(ordered) // 2]
    mode = Counter(data).most_common(1)[0][0]
    return Abs(median - mode)


def h1_19():
    return sqrt(24 ** 2 + 10 ** 2) + sqrt(8 ** 2 + 6 ** 2)


def h1_21():
    return 9 * pi * (5 ** 2 - 2 ** 2)


def h1_22():
    xv = solve(Eq(4 * x + 15, 6 * x - 25), x)[0]
    return 180 - (4 * xv + 15)


# ---------------------------------------------------------- Module 2 (Easy)
def h2e_03():
    return -diff(480 - 32 * d, d)


def h2e_05():
    return [z for z in (6, 7, 8, 9) if 4 * z + 5 < 33][0]


def h2e_07():
    return floor(Rational(96 - 11, 4))


def h2e_10():
    return [z for z in solve(Eq((m - 9) * (m + 5), 0), m) if z > 0][0]


def h2e_11():
    rows = [(1, 15), (2, 8), (3, 0), (4, -6)]
    return [xv for xv, fv in rows if fv == 0][0]


def h2e_13():
    yp = symbols("yp", positive=True)
    return simplify(yp ** 11 / yp ** 4).subs(yp, symbols("y"))


def h2e_16():
    rows = [("Halstow", 34), ("Kingsdown", 51), ("Marden", 29), ("Newlyn", 47)]
    return max(rows, key=lambda row: row[1])[0]


def h2e_17():
    vals = [14, 18, 11, 20, 17]
    return Rational(sum(vals), len(vals))


def h2e_21():
    return 180 - 38 - 64


# ---------------------------------------------------------- Module 2 (Hard)
def h2h_01():
    av = symbols("av")
    # No solution: the coefficient rows are proportional but the constants are
    # not. Proportionality is the vanishing 2x2 determinant.
    sol = solve(Eq(av * 3 - 6 * 4, 0), av)[0]
    assert Rational(15, 9) != Rational(6, 3)          # constants not in ratio
    return sol


def h2h_02():
    slope = Rational(-5 - 11, 6 - (-2))
    line = 11 + slope * (x + 2)
    cands = [(3, 2), (0, 9), (8, -8), (10, -13)]
    on = [pt for pt in cands if line.subs(x, pt[0]) == pt[1]]
    assert len(on) == 1, on
    return f"({on[0][0]}, {on[0][1]})"


def h2h_03():
    pv = symbols("pv")
    # (p-3)x <= 20 flips to x >= 20/(p-3) exactly when p-3 < 0.
    got = solve(Eq(20 / (pv - 3), -4), pv)[0]
    assert got - 3 < 0
    return got


def h2h_04():
    r1, r2, r3 = symbols("r1 r2 r3")
    sol = solve([Eq(r1 + r2, 34), Eq(r2 + r3, 47), Eq(r1 + r3, 39)], [r1, r2, r3])
    return sol[r3]


def h2h_05():
    slope, inter = symbols("slope inter")
    sol = solve([Eq(120 * slope + inter, 510), Eq(200 * slope + inter, 750)],
                [slope, inter])
    return f"C={sol[slope]}A+{sol[inter]}"


def h2h_06():
    wr = symbols("wr", real=True)
    return min(solve(Eq(Abs(wr - Rational(345, 10)), Rational(8, 10)), wr))


def h2h_07():
    bl, th = symbols("bl th")
    sol = solve([Eq(5 * bl + 8 * th, 137), Eq(8 * bl + 5 * th, 149)], [bl, th])
    return sol[bl] + sol[th]


def h2h_08():
    gx = symbols("gx")
    # f(x) = 2x+7, so f(g(x)) = 2g(x)+7 must equal 6x-1.
    return solve(Eq(2 * gx + 7, 6 * x - 1), gx)[0]


def h2h_09():
    kk, pp, qq = symbols("kk pp qq", positive=True)
    got = solve(Eq(1 / kk, 1 / pp + 1 / qq), kk)[0]
    return got.subs({pp: symbols("p"), qq: symbols("q")})


def h2h_10():
    ln, wd = symbols("ln_ wd")
    sols = solve([Eq(ln + wd, 22), Eq(ln * wd, 96)], [ln, wd])
    return max(max(pair) for pair in sols)


def h2h_11():
    ap = symbols("a", positive=True)
    return simplify(sqrt(50 * ap ** 7))


def h2h_12():
    fx = x ** 2 - 14 * x + 53
    av = solve(Eq(diff(fx, x), 0), x)[0]
    return av + fx.subs(x, av)


def h2h_13():
    kk = symbols("kk")
    return solve(Eq(expand((x - 5) ** 2 - 9), expand(x ** 2 - 10 * x + kk)), kk)[0]


def h2h_14():
    return (3 * Rational(240, 100) + 2 * Rational(165, 100)) / 5


def h2h_15():
    other = symbols("other", positive=True)
    return solve(Eq(Rational(1, 20) + 1 / other, Rational(1, 12)), other)[0]


def h2h_17():
    return Rational(120, 100) * Rational(85, 100) * 100


def h2h_18():
    slope, inter = symbols("slope inter")
    sol = solve([Eq(12 * slope + inter, 30), Eq(20 * slope + inter, 46)], [slope, inter])
    for nn, LL in ((28, 62), (36, 78)):
        assert sol[slope] * nn + sol[inter] == LL
    return f"L={sol[slope]}n+{sol[inter]}"


def h2h_19():
    rr, LL = symbols("rr LL", positive=True)
    first = pi * rr ** 2 * LL
    second = pi * (2 * rr) ** 2 * (LL / 3)
    return simplify(second / first)


def h2h_20():
    bc = symbols("bc")
    return solve(Eq(Rational(6, 6 + 9), 8 / bc), bc)[0]


def h2h_21():
    th = symbols("th", positive=True)
    tv = Rational(7, 24)
    # sin = tan / sqrt(1 + tan^2)
    return simplify(tv / sqrt(1 + tv ** 2))


def h2h_22():
    area = Rational(1, 2) * 18 * 24
    return area * Rational(27, 18) ** 2


DERIVE = {
 "H1-01": h1_01,
 "H1-02": h1_02,
 "H1-03": h1_03,
 "H1-04": h1_04,
 "H1-05": h1_05,
 "H1-06": h1_06,
 "H1-07": h1_07,
 "H1-08": lambda: expand((4 * n + 3) ** 2 - (16 * n ** 2 + 5)),
 "H1-09": h1_09,
 "H1-10": h1_10,
 "H1-11": h1_11,
 "H1-12": h1_12,
 "H1-13": h1_13,
 "H1-14": lambda: Rational(7 * 840, 4) * 9,
 "H1-15": h1_15,
 "H1-16": lambda: Rational(6 * 42 + 70, 7),
 "H1-17": h1_17,
 "H1-18": h1_18,
 "H1-19": h1_19,
 "H1-20": lambda: Rational(40, 41),
 "H1-21": h1_21,
 "H1-22": h1_22,

 "H2E-01": lambda: solve(Eq(8 * n + 17, 121), n)[0],
 "H2E-02": lambda: 26 * 7,
 "H2E-03": h2e_03,
 "H2E-04": lambda: solve(Eq(5 * (t - 3), 40), t)[0],
 "H2E-05": h2e_05,
 "H2E-06": lambda: solve(Eq(240 - 18 * c, 96), c)[0],
 "H2E-07": h2e_07,
 "H2E-08": lambda: expand(3 * (2 * k + 7) - 5 * k),
 "H2E-09": lambda: expand((x + 6) * (x + 4)),
 "H2E-10": h2e_10,
 "H2E-11": h2e_11,
 "H2E-12": lambda: (7 * x - 6).subs(x, 4),
 "H2E-13": h2e_13,
 "H2E-14": lambda: Rational(96, 8),
 "H2E-15": lambda: Rational(30, 100) * 180,
 "H2E-16": h2e_16,
 "H2E-17": h2e_17,
 "H2E-18": lambda: Rational(18, 45),
 "H2E-19": lambda: 14 * 9,
 "H2E-20": lambda: 4 * 3 * 2,
 "H2E-21": h2e_21,
 "H2E-22": lambda: Rational(8, 17),

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
 "H2H-16": lambda: Rational(27, 43),
 "H2H-17": h2h_17,
 "H2H-18": h2h_18,
 "H2H-19": h2h_19,
 "H2H-20": h2h_20,
 "H2H-21": h2h_21,
 "H2H-22": h2h_22,
}

# Nothing in Test 24 resists a symbolic derivation, so MANUAL is empty and
# pass 1 covers all 66.
MANUAL = {}


def latex_to_expr(text):
    """Turn one answer choice into something sympify can read."""
    t = text.replace("&deg;", "").replace("&gt;", ">").replace("&lt;", "<")
    t = re.sub(r"\\left|\\right", "", t)
    t = re.sub(r"\\lvert|\\rvert", "|", t)
    t = re.sub(r"\\\((.*?)\\\)", r"\1", t, flags=re.S)
    # The rewrite order cannot be fixed by choosing an order: a fraction can
    # sit inside an exponent (a^{\frac{7}{12}}) as readily as an exponent
    # inside a fraction (\frac{4a^{3}}{b^{4}}), and either fixed order fails
    # one of them. Alternate the two to a fixed point instead.
    for _ in range(8):
        before = t
        t = re.sub(r"\^\{([^{}]*)\}", r"**(\1)", t)
        t = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"((\1)/(\2))", t)
        if t == before:
            break
    t = t.replace("\\pi", "pi").replace("\\cdot", "*").replace("\\sqrt", "sqrt")
    t = t.replace("{,}", "").replace(",", "").replace("$", "").replace("%", "")
    t = t.replace("^", "**").replace("{", "(").replace("}", ")")
    # implicit multiplication: after a digit, after a closing paren, and after
    # a lone symbol; the lookbehind keeps sqrt( / cos( from being mangled.
    t = re.sub(r"(\d)\s*([a-zA-Z(])", r"\1*\2", t)
    t = re.sub(r"\)\s*\(", ")*(", t)
    t = re.sub(r"(?<![a-zA-Z])([a-zA-Z])\s*\(", r"\1*(", t)
    # A surviving multi-letter run is an implicit product, not one symbol:
    # without this \frac{pq}{p+q} parses as a symbol named "pq" and the key
    # silently fails to match. sqrt/pi are the only real multi-letter names.
    def split_run(mo):
        word = mo.group(0)
        if word in ("sqrt", "pi"):
            return word
        return "*".join(word)
    t = re.sub(r"(?<![\\\w])[a-zA-Z]{2,}(?![\w(])", split_run, t)
    return t.strip()


def as_expr(text):
    """Parse a choice under both the plain and the positive-assumption reading.

    symbols("a", positive=True) is a different Symbol from symbols("a"), so a
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
    check(len(bal) == 4, f"{name}: answer key never lands on {set('ABCD') - set(bal)}")
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
    check("T18" not in json.dumps(qq) and "Test 18" not in json.dumps(qq),
          f"{tag}: Test 18 provenance survived the scaffolding")

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
        for mm in re.finditer(r"sqrt\s*\(", bare):
            check(False, f"{tag}: plain-text sqrt(")
        for mm in re.finditer(r"[\dA-Za-z)]\s*\*\s*[\dA-Za-z(]", bare):
            check(inside(mm.start()), f"{tag}: asterisk multiplication outside math mode")
        for mm in re.finditer(r"(?<![\d/:])\d+\s*/\s*\d+(?![\d/])", bare):
            check(inside(mm.start()), f"{tag}: slash fraction outside math mode")
        for mm in re.finditer(r"\\(pi|frac|sqrt|cdot|le|ge|ne|circ|sin|cos|tan|log|ln|"
                              r"left|right|overline|text|theta|lvert|rvert)\b", bare):
            check(inside(mm.start()), f"{tag}: LaTeX macro outside math mode")
        for mm in re.finditer(r"(!=|<=|>=)", bare):
            check(False, f"{tag}: ASCII comparison operator, use \\ne / \\le / \\ge")
        for mm in re.finditer(r"(?<![A-Za-z])(theta|alpha|beta|lambda)(?![A-Za-z])", bare):
            check(inside(mm.start()), f"{tag}: Greek letter spelled out in prose")
        # \bpi never matches: a digit and a letter are both \w, so "3pi" has no
        # boundary between them. The lookaround is letter-specific on purpose.
        for mm in re.finditer(r"(?<![A-Za-z])pi(?![A-Za-z])", bare):
            check(inside(mm.start()), f"{tag}: bare word pi outside math mode")

        # A raw "<" outside a tag and outside a math span is invalid HTML. It
        # is fine INSIDE a span: MathContent pulls math out of the raw string
        # with a regex before anything is parsed as HTML, and hands "<" to
        # KaTeX unchanged. "&lt;" inside a span is the real bug — KaTeX would
        # receive the literal ampersand.
        for mm in re.finditer(r"<(?![a-zA-Z/!])", bare):
            check(inside(mm.start()), f"{tag}: raw < outside a tag and outside math mode")
        for aa, bb2 in spans:
            check("&lt;" not in bare[aa:bb2] and "&gt;" not in bare[aa:bb2],
                  f"{tag}: HTML entity inside a math span — KaTeX gets the ampersand")

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
        # and it must not be followed by a floating comma/period/question mark
        for mo in re.finditer(r"\\\)\s+[,.?]", bare):
            check(False, f"{tag}: space between a math span and its punctuation")

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
# The corpus lives at the content-pool ROOT and is READ ONLY. The template
# directory keeps a stale local copy; this verifier deliberately ignores it.
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
# Every keyword below is chosen so that a word-boundary PREFIX match cannot
# collide with an ordinary English word or with the other module's vocabulary:
#   * "tarpaulin" and "tar kettle" are listed separately — a bare "tar" prefix
#     matches both, which is the same family of bug as \bfen matching "fence".
#   * "net", "knot", "yarn", "line", "block" and "strand"-as-a-verb are NOT
#     used: they all have everyday senses, and a boundary-free substring match
#     in a checker is worse than no check because it trains you to ignore it.
M1_SETTINGS = ["ropewalk", "cordage", "hemp", "hackl", "twine", "hawser",
               "bobbin", "fathom", "tar kettle", "tarred", "spinner"]
M2_SETTINGS = ["mesh", "netting", "net maker", "net loft", "sailmaker",
               "sail loft", "canvas", "tarpaulin", "thimble", "seamer",
               "splice", "stitch", "tabling"]
SETTING_KEYWORDS = M1_SETTINGS + M2_SETTINGS

m1_text = " ".join(qq["stem"].lower() for qq in MODULE_1)
m2_text = " ".join(qq["stem"].lower() for qq in MODULE_2_EASY + MODULE_2_HARD)


def has(kwd, text):
    """Prefix match at an opening word boundary: "splice" catches "spliced",
    but "tarpaulin" cannot catch "tar" and "mesh" cannot be found inside a
    longer word that merely ends in it."""
    return re.search(r"(?<![a-z])" + re.escape(kwd), text) is not None


shared = [kwd for kwd in SETTING_KEYWORDS if has(kwd, m1_text) and has(kwd, m2_text)]
check(not shared, f"settings reused across Module 1 and a Module 2 branch: {shared}")
stray_m1 = [kwd for kwd in M2_SETTINGS if has(kwd, m1_text)]
stray_m2 = [kwd for kwd in M1_SETTINGS if has(kwd, m2_text)]
check(not stray_m1, f"Module 2 settings appearing in Module 1: {stray_m1}")
check(not stray_m2, f"Module 1 settings appearing in Module 2: {stray_m2}")
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
print(f"highest Jaccard vs production: {worst_prod:.2f}   within Test 24: {worst_self:.2f}")

if FAIL:
    print(f"\n{len(FAIL)} FAILURES:")
    for f in FAIL:
        print("  -", f)
    raise SystemExit(1)
print("\nALL CHECKS PASSED")
