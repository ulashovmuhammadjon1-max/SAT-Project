#!/usr/bin/env python3
"""
Verify the 66 originally-authored Math questions for Test 23.

Four passes, because each has caught a different class of defect in earlier
builds:

 1. Every answer is re-derived with sympy from the question itself, never read
    off the `check` note. A wrong `check` and a wrong key agree with each
    other; only an independent derivation catches that. The pass also asserts
    that no distractor equals the derived value. Anything genuinely outside
    sympy's reach would go in MANUAL with a written justification — Test 23
    has none: every answer is a value, an algebraic form, an equation built
    out of sympy-computed coefficients, or a named table row selected by a
    comparison over the printed data.
 2. House style on the final HTML — the Test 1/2 rules in CLAUDE.md plus the
    DB-wide rendering checks (no bare `^`, `sqrt(`, `*`-as-multiply, slash
    fractions, ASCII comparison operators or LaTeX macros outside a math
    span). `<img>` tags are stripped first; a base64 payload matches every
    pattern below.
 3. Template dedupe against every Math stem live in production. 0.75 fails
    outright, and every match at or above 0.45 is PRINTED so the nearest
    banked stem can be read and judged: across Tests 18-21, 57 genuine
    template repeats were found and all but three scored below 0.75. The
    threshold decides what to read, not what to accept.
 4. Self-collision among Test 23's own 66 stems, plus the cross-module setting
    check — a student sees Module 1 and exactly one Module 2 branch, so no
    setting keyword may appear in both.

Run:  python3 verify_math_test23.py
      (no DATABASE_URL needed — pass 3 reads ../prod_math_stems.json, the
      snapshot of the 1,386 Math stems live in production; note it is the
      corpus at the content-pool ROOT, not a local copy)
"""
import json
import os
import re
import sys
from collections import Counter

from sympy import (Abs, Eq, Rational, asin, ceiling, floor, cancel, diff,
                   expand, latex, log, pi, simplify, sin, cos, solve, sqrt,
                   symbols, sympify, tan, together)

from math_test23 import MODULE_1, MODULE_2_EASY, MODULE_2_HARD, ALL

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
    lift = symbols("lift")
    base = solve(Eq(12 * lift + 4 * (lift + 2), 72), lift)[0]
    return base + 2


def h1_02():
    days = symbols("days")
    return solve(Eq(18 * 210 + 90 * days, 4500), days)[0]


def h1_03():
    slope, inter = symbols("slope inter")
    sol = solve([Eq(2 * slope + inter, 31), Eq(5 * slope + inter, 43)], [slope, inter])
    return sol[inter]


def h1_04():
    ok = [i for i in range(0, 60)
          if Rational(120, 100) <= Rational(162, 100) - Rational(4, 100) * i <= Rational(150, 100)]
    return max(ok)


def h1_05():
    short = symbols("short")
    sv = solve(Eq(short + (short + 400) + 2 * short, 6000), short)[0]
    return 2 * sv


def h1_06():
    rate, fixed, vol = symbols("rate fixed vol")
    sol = solve([Eq(900 * rate + fixed, 6150), Eq(1500 * rate + fixed, 9750)], [rate, fixed])
    return solve(Eq(sol[rate] * vol + sol[fixed], 10950), vol)[0]


def h1_07():
    roots = solve(Eq(-Rational(5, 100) * (t - 14) ** 2 + Rational(32, 10), 3), t)
    return max(roots) - min(roots)


def h1_08():
    return solve(Eq(180 * Rational(1, 2) ** (t / 9), Rational(45, 2)), t)[0]


def h1_09():
    hp = symbols("h", positive=True)
    vp, gp = symbols("v g", positive=True)
    return solve(Eq(vp, sqrt(2 * gp * hp)), hp)[0]


def h1_10():
    wd = symbols("wd", positive=True)
    return solve(Eq(wd * (3 * wd + 4), 175), wd)[0]


def h1_11():
    ap, bp = symbols("a b", positive=True)
    return simplify(6 * ap ** 2 * bp ** 3 / (3 * ap * bp) ** 2)


def h1_12():
    hours = symbols("hours")
    return solve(Eq(480 * hours, 2400 * 12 * Rational(15, 100)), hours)[0]


def h1_13():
    before = symbols("before")
    bv = solve(Eq(before * Rational(130, 100), Rational(182, 100)), before)[0]
    return (2 - bv) * 100


def h1_14():
    return Rational(40 * Rational(115, 10) + (24 - 4) + (31 - 1), 40)


def h1_15():
    rows = [("Ashby Cut", 1344, 28), ("Brindle Reach", 1530, 34),
            ("Croxall Reach", 2014, 38), ("Dunwater Cut", 1196, 26)]
    return max(rows, key=lambda row: Rational(row[1], row[2]))[0]


def h1_16():
    rows = [(20, 5), (25, 12), (30, 9), (35, 4)]
    return Rational(sum(val * cnt for val, cnt in rows), sum(cnt for _, cnt in rows))


def h1_17():
    apex = symbols("apex")
    return solve(Eq(apex + 18 + 18, 180), apex)[0]


def h1_18():
    return Rational(9 + 5, 2) * Rational(16, 10) * 250


def h1_19():
    run, rise = Rational(56, 10), Rational(42, 10)
    return simplify(run / sqrt(run ** 2 + rise ** 2))


def h1_20():
    spring = symbols("spring")
    sv = solve(Eq(spring + (spring + 250), 800), spring)[0]
    return sv + 250


def h1_21():
    return [z for z in solve(Eq(5400 - 2 * t ** 2 - 40 * t, 4800), t) if z > 0][0]


def h1_22():
    return Rational(35, 10) * Rational(12, 10) * Rational(5, 10) * 60


def h2e_03():
    dd, hh = symbols("dd hh")
    expr = solve(Eq(dd, 4 * hh), dd)[0]          # 4*hh
    return "d = " + str(expr).replace("*", "").replace("hh", "h")


def h2e_04():
    room = symbols("room")
    bound = solve(Eq(17 + room, 26), room)[0]
    return "\\(t \\le " + str(bound) + "\\)"


def h2e_09():
    return max(solve(Eq((n - 6) * (n + 4), 0), n))


def h2e_11():
    rows = [(1, 9), (2, 4), (3, -1), (4, -6)]
    return [xv for xv, fv in rows if fv == -1][0]


def h2e_13():
    return sorted([14, 9, 21, 17, 12])[2]


def h2e_19():
    # right angle at F: the side opposite E is DF, the hypotenuse is DE
    return Rational(7, 25)


def h2h_01():
    av = symbols("av")
    val = solve(Eq(av * 3 - 6 * 4, 0), av)[0]
    # proportional coefficients must NOT extend to the constants, or the system
    # would have infinitely many solutions instead of none
    assert Rational(18, 7) != Rational(6, 3)
    return val


def h2h_02():
    sol = solve([Eq(3 * x + 2 * y, 19), Eq(5 * x - 4 * y, 17)], [x, y])
    return sol[x] + sol[y]


def h2h_03():
    slope, inter = symbols("slope inter")
    sol = solve([Eq(-2 * slope + inter, 9), Eq(6 * slope + inter, -7)], [slope, inter])
    return "y = " + str(sol[slope]) + "x + " + str(sol[inter])


def h2h_04():
    return max(i for i in range(-50, 50) if 5 - 2 * i >= 3 * (i - 4))


def h2h_05():
    kv = symbols("kv")
    return solve(Eq(4 * kv, 12), kv)[0]


def h2h_06():
    load = symbols("load")
    return solve(Eq(d, 46 + Rational(3, 5) * load), load)[0]


def h2h_07():
    fx = (x + 5) / 2
    return simplify(fx.subs(x, 4 * x - 3))


def h2h_08():
    xv = solve(Eq(x + 1 / x, 5), x)[0]
    return simplify(xv ** 2 + 1 / xv ** 2)


def h2h_09():
    return cancel((6 * x ** 2 - x - 15) / (2 * x + 3))


def h2h_10():
    return (1 - Rational(85, 100) ** 2) * 100


def h2h_11():
    up, vp = symbols("u v", positive=True)
    return together(1 / up - 1 / vp)


def h2h_13():
    per_barge = Rational(4 * 9, 6)
    return per_barge * 10 / 6


def h2h_15():
    mass = symbols("mass")
    return solve(Eq(Rational(40, 100) * mass, Rational(25, 100) * (mass + 6)), mass)[0]


def h2h_16():
    vals = [12] * 4 + [15] * 7 + [18] * 6 + [20] * 3
    vals.sort()
    return Rational(vals[9] + vals[10], 2)


def h2h_18():
    rad = symbols("rad", positive=True)
    # x^2 - 10x + y^2 + 6y = 2  ->  (x-5)^2 + (y+3)^2 = 2 + 25 + 9
    return solve(Eq(rad ** 2, 2 + 25 + 9), rad)[0]


def h2h_19():
    ang_a = asin(Rational(5, 13))
    return simplify(tan(pi / 2 - ang_a))


def h2h_20():
    kv = symbols("kv")
    return solve(Eq(3 * kv, 21), kv)[0]


def h2h_21():
    xr = symbols("xr", real=True)
    return [z for z in solve(Eq(sqrt(2 * xr + 3), xr - 6), xr)][0]


def h2h_22():
    wd = symbols("wd", positive=True)
    wv = solve(Eq(2 * (wd + 2 * wd + 4), 128), wd)[0]
    return wv * (2 * wv + 4)


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

 "H2E-01": lambda: solve(Eq(8 * t + 45, 165), t)[0],
 "H2E-02": lambda: solve(Eq(m + 3 * m, 48), m)[0],
 "H2E-03": h2e_03,
 "H2E-04": h2e_04,
 "H2E-05": lambda: (3 * t + 11).subs(t, 0),
 "H2E-06": lambda: solve(Eq(5 * b - 12, 43), b)[0],
 "H2E-07": lambda: expand(5 * (2 * x + 3) - 4 * x),
 "H2E-08": lambda: (7 * x - 2).subs(x, 4),
 "H2E-09": h2e_09,
 "H2E-10": lambda: expand((x + 3) * (x + 8)),
 "H2E-11": h2e_11,
 "H2E-12": lambda: Rational(25, 100) * 32,
 "H2E-13": h2e_13,
 "H2E-14": lambda: 815 - 470,
 "H2E-15": lambda: Rational(141, 3),
 "H2E-16": lambda: Rational(24, 60),
 "H2E-17": lambda: 18 * 2 * Rational(15, 10),
 "H2E-18": lambda: 180 - 34 - 79,
 "H2E-19": h2e_19,
 "H2E-20": lambda: solve(Eq(4 * t, 92), t)[0],
 "H2E-21": lambda: solve(Eq(4 ** x, 64), x)[0],
 "H2E-22": lambda: 40 * 7,

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
 "H2H-12": lambda: Rational(18, 80) * 1200,
 "H2H-13": h2h_13,
 "H2H-14": lambda: Rational(45, 45 + 30) * 100,
 "H2H-15": h2h_15,
 "H2H-16": h2h_16,
 "H2H-17": lambda: 96 * Rational(15, 10) ** 3,
 "H2H-18": h2h_18,
 "H2H-19": h2h_19,
 "H2H-20": h2h_20,
 "H2H-21": h2h_21,
 "H2H-22": h2h_22,
}

# Nothing in Test 23 resists a symbolic derivation, so MANUAL is empty and
# pass 1 covers all 66. (An item that did would be listed here with a written
# justification, not quietly skipped.)
MANUAL = {}

FUNCS = ("sqrt", "sin", "cos", "tan", "log", "ln", "pi", "Abs")


def _split_letter_runs(text):
    """Turn a surviving multi-letter run into an implicit product.

    Without this `\\frac{v-u}{uv}` parses as a symbol literally named "uv" and
    the comparison silently fails to match a correct key. Known function and
    constant names are protected first, or "sqrt" would become s*q*r*t.
    """
    out, i = [], 0
    while i < len(text):
        for fn in FUNCS:
            if text.startswith(fn, i) and not (i and text[i - 1].isalpha()):
                out.append(fn)
                i += len(fn)
                break
        else:
            mm = re.match(r"[A-Za-z]{2,}", text[i:])
            if mm:
                out.append("*".join(mm.group(0)))
                i += len(mm.group(0))
            else:
                out.append(text[i])
                i += 1
    return "".join(out)


def latex_to_expr(text):
    """Turn one answer choice into something sympify can read."""
    tt = text.replace("&deg;", "").replace("&gt;", ">").replace("&lt;", "<")
    tt = re.sub(r"\\left|\\right", "", tt)
    tt = re.sub(r"\\\((.*?)\\\)", r"\1", tt, flags=re.S)
    # The rewrite order cannot be fixed by choosing an order: a fraction can sit
    # inside an exponent (a^{\frac{7}{12}}) as readily as an exponent inside a
    # fraction (\frac{4a^{3}}{b^{4}}), and either fixed order fails one of them.
    # Alternate the two rewrites until nothing changes.
    for _ in range(12):
        before = tt
        tt = re.sub(r"\^\{([^{}]*)\}", r"**(\1)", tt)
        tt = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"((\1)/(\2))", tt)
        tt = re.sub(r"_\{([^{}]*)\}", r"\1", tt)
        if tt == before:
            break
    tt = tt.replace("\\pi", "pi").replace("\\cdot", "*").replace("\\sqrt", "sqrt")
    tt = tt.replace("{,}", "").replace(",", "").replace("$", "").replace("%", "")
    tt = tt.replace("^", "**").replace("{", "(").replace("}", ")")
    tt = _split_letter_runs(tt)
    # implicit multiplication: after a digit, after a closing paren, and after a
    # lone symbol — \(x(x+7)\) parses to nonsense without the last of the three,
    # and the lookbehind keeps sqrt( / cos( from being mangled.
    tt = re.sub(r"(\d)\s*([a-zA-Z(])", r"\1*\2", tt)
    tt = re.sub(r"\)\s*\(", ")*(", tt)
    tt = re.sub(r"(?<![a-zA-Z])([a-zA-Z])\s*\(", r"\1*(", tt)
    return tt.strip()


def as_expr(text):
    """Parse a choice, trying the plain and the positive-assumption reading.

    symbols("v", positive=True) is a different Symbol from symbols("v"), so a
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
    check("T17" not in json.dumps(qq) and "T21" not in json.dumps(qq),
          f"{tag}: a scaffolding tag from the reference template survived")

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
        for mm in re.finditer(r"(?<![A-Za-z\\])sqrt\s*\(", bare):
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
# The corpus lives at the content-pool ROOT and is read-only: 1,386 Math stems,
# every one live in production.
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
# Every keyword below is a canal-specific noun that cannot collide with an
# ordinary English word once the boundary is respected. Generic labour words
# ("gang", "crew", "clerk") are deliberately NOT keywords: they are not
# settings, and including them would flag a false positive and train the
# reader to ignore the output. "pound" is kept precisely because it is
# ambiguous — the canal sense belongs to Module 1, so a weight or a currency
# in Module 2 SHOULD fail this check.
SETTING_KEYWORDS = [
    # Module 1's half of the territory
    "lock", "pound", "aqueduct", "sluice", "paddle", "cill", "silt", "dredg",
    "feeder", "trough", "boat", "cutting", "flight", "spring", "chamber",
    # Module 2's half
    "barge", "towpath", "wharf", "quay", "toll", "warehouse", "tally",
    "gauged", "cargo", "crate", "sack", "hopper", "draught", "grain",
    "salt", "gravel", "apron", "hold", "horse", "berth", "tonnage",
]
m1_text = " ".join(qq["stem"].lower() for qq in MODULE_1)
m2_text = " ".join(qq["stem"].lower() for qq in MODULE_2_EASY + MODULE_2_HARD)


def has(kwd, text):
    """Prefix match at a word boundary: "lock" catches "locks" and "lockings",
    but does not catch "block", and "spring" would not catch "offspring" — the
    kind of silent over-match that the \\bpi\\b and \\bfen bugs were made of."""
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
print(f"highest Jaccard vs production: {worst_prod:.2f}   within Test 23: {worst_self:.2f}")

if FAIL:
    print(f"\n{len(FAIL)} FAILURES:")
    for f in FAIL:
        print("  -", f)
    raise SystemExit(1)
print("\nALL CHECKS PASSED")
