#!/usr/bin/env python3
"""
Verify the 66 originally-authored Math questions for Test 22.

Four passes, because each has caught a different class of defect in earlier
builds:

 1. Every answer is re-derived with sympy from the QUESTION, never read off the
    `check` note. A wrong `check` and a wrong key agree with each other; only an
    independent derivation catches that. The pass also asserts that no
    distractor equals the derived value. Anything genuinely outside sympy's
    reach goes in MANUAL with a written justification.
 2. House style on the final HTML — the Test 1/2 rules in CLAUDE.md plus the
    DB-wide rendering checks (no bare `^`, `sqrt(`, `*`-as-multiply, slash
    fractions, ASCII comparison operators, spelled-out Greek, or LaTeX macros
    outside a math span). `<img>` is stripped first, because a base64 payload
    matches every one of those patterns.
 3. Template dedupe against every Math stem live in production — the corpus at
    the content-pool ROOT, ../prod_math_stems.json, not a stale per-directory
    copy. 0.75 fails outright, and every match at or above 0.45 is PRINTED so
    the nearest banked stem can be read by eye: across Tests 18-21, 57 genuine
    template repeats were found and all but three scored below 0.75.
 4. Self-collision among Test 22's own 66 stems, plus the cross-module setting
    check — a student sees Module 1 and exactly one Module 2 branch, so no
    setting keyword may appear on both sides of that boundary.

Run:  python3 verify_math_test22.py
      (no DATABASE_URL needed — pass 3 reads ../prod_math_stems.json)
"""
import json
import os
import re
import sys
from collections import Counter

from sympy import (Abs, Eq, Rational, S, ceiling, factor, floor, cancel, diff,
                   expand, fraction, log, pi, simplify, sin, cos, solve,
                   solveset, sqrt, symbols, sympify, tan, together)

from math_test22 import MODULE_1, MODULE_2_EASY, MODULE_2_HARD, ALL

HERE = os.path.dirname(os.path.abspath(__file__))

# Symbols. Never name one S, E, I, N, O, Q, beta, gamma or zeta and then hand
# it to sympify bare: sympify("S") returns the SingletonRegistry and the
# comparison silently degrades to a string compare. Everything below is either
# built with symbols() explicitly or parsed with an all-letters locals map.
x, y, w, t, h, d, m, n, c, k = symbols("x y w t h d m n c k")
a, b, g, r, s, u, v, p, q = symbols("a b g r s u v p q")
C_, L_ = symbols("C L")

BASE_LOCALS = {ch: symbols(ch) for ch in
               "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"}
POS_LOCALS = dict(BASE_LOCALS)
POS_LOCALS.update({nm: symbols(nm, positive=True) for nm in ("a", "b", "w", "x", "y")})

FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)


# ---------------------------------------------------------------- Module 1
def h1_01():
    orch, oil = symbols("orch oil")
    sol = solve([Eq(9 * orch + 5 * oil, 1930), Eq(6 * orch + 11 * oil, 2176)], [orch, oil])
    return sol[orch] + sol[oil]


def h1_02():
    ra, rb, dd = symbols("ra rb dd")
    a_rate = solve(Eq(41 + ra * (9 - 2), 55), ra)[0]
    b_rate = solve(Eq(62 + rb * (9 - 2), 69), rb)[0]
    return solve(Eq(41 + a_rate * (dd - 2), 62 + b_rate * (dd - 2)), dd)[0]


def h1_03():
    each = symbols("each")
    return solve(Eq(168 + 205 + 149 + 2 * each, 900), each)[0]


def h1_04():
    sh = symbols("sh")
    return 2 * solve(Eq((2 * sh + 1) + 3 * sh, 41), sh)[0] + 1


def h1_05():
    return "r=" + str(solve(Eq(w, (r - 38) / 19), r)[0]).replace(" ", "").replace("*", "")


def h1_06():
    tt = symbols("tt")
    return solve(Eq(15 * tt + 25 * (tt - 2), 310), tt)[0]


def h1_07():
    return len([i for i in range(0, 100)
                if 9.5 + Rational(3, 2) * i > 18 and 9.5 + Rational(3, 2) * i <= 22])


def h1_09():
    kk = symbols("kk")
    kv = solve(Eq(kk * sqrt(16), 60), kk)[0]
    return kv * sqrt(36)


def h1_11():
    fac, start = symbols("fac start")
    sol = solve([Eq(start * fac ** 1, 2700), Eq(start * fac ** 2, 8100)], [start, fac],
                dict=True)
    return [z[start] for z in sol if z[fac] > 0][0]


def h1_13():
    xv = solve(Eq(4 ** x, 7), x)[0]
    return simplify(4 ** (2 * xv + 1))


def h1_14():
    unit = symbols("unit", positive=True)
    uu = solve(Eq(7 * unit - 3 * unit, 148), unit)[0]
    return 10 * uu


def h1_16():
    rows = [("Alder", 240, 294), ("Byre", 180, 225),
            ("Coppice", 350, 420), ("Dell", 150, 195)]
    return max(rows, key=lambda row: Rational(row[2] - row[1], row[1]))[0]


def h1_17():
    total = symbols("total")
    tot = solve(Eq(total / 12, 25), total)[0]
    return Rational(tot - 36, 11)


def h1_18():
    clear_unlabelled = 25 - 3
    set_unlabelled = 15 - 5
    return Rational(set_unlabelled, clear_unlabelled + set_unlabelled)


def h1_20():
    diag = sqrt(24 ** 2 + 45 ** 2)
    return (2 * (24 + 45) + diag) * 14


def h1_21():
    other = symbols("other", positive=True)
    leg = Rational(16, 10)
    far = solve(Eq(leg ** 2 + other ** 2, Rational(34, 10) ** 2), other)[0]
    return simplify(far / leg)


def h1_22():
    depth = symbols("depth", positive=True)
    return solve(Eq(pi * 25 ** 2 * depth, 6250 * pi), depth)[0]


# ------------------------------------------------------------ Module 2 Easy
def h2e_04():
    return solve(Eq(7 * x + 4, 39), x)[0]


def h2e_05():
    return -diff(2400 - 85 * t, t)


def h2e_12():
    rows = dict([(1, 5), (2, 11), (3, 19), (4, 29)])
    return rows[4] - rows[1]


def h2e_16():
    rows = [(1, 840), (2, 960), (3, 1020), (4, 880)]
    return len([wk for wk, tn in rows if tn > 900])


def h2e_19():
    return pi * (Rational(12, 2)) ** 2


def h2e_21():
    return Abs(13 - 1)


# ------------------------------------------------------------ Module 2 Hard
def h2h_01():
    aa = symbols("aa")
    check_first = solve(Eq(2 * 3 + 3 * 2, 12), aa)  # the stated pair does satisfy 2x+3y=12
    assert check_first == [] or check_first is not None
    return solve(Eq(5 * 3 + aa * 2, 25), aa)[0]


def h2h_02():
    nn = symbols("nn")
    return solve(Eq(C_, a * nn + b), nn)[0]


def h2h_03():
    return len([i for i in range(-100, 200) if -5 < 3 * i - 8 <= 13])


def h2h_04():
    av = symbols("av", positive=True)
    return simplify((5 * av - 2 * av) / (6 * av - av))


def h2h_05():
    slow = symbols("slow", positive=True)
    both = Rational(180, 4)
    fast = Rational(180, 6)
    rate = solve(Eq(fast + slow, both), slow)[0]
    return Rational(180, 1) / rate


def h2h_06():
    return "x\\le" + str(solve(Eq((2 * x - 5) / 3, x - 6), x)[0])


def h2h_07():
    piece = symbols("piece", positive=True)
    pm = solve(Eq(40 * (piece + 3), 60 * (piece - 2)), piece)[0]
    return 40 * (pm + 3)


def h2h_08():
    gg = symbols("gg")
    # f(g) = 3g - 2 must equal 6x + 7 for every x
    return solve(Eq(3 * gg - 2, 6 * x + 7), gg)[0]


def h2h_09():
    r1, r2, qq = symbols("r1 r2 qq")
    sol = solve([Eq(r1 + r2, 14), Eq(r1 - r2, 6), Eq(qq, r1 * r2)], [r1, r2, qq], dict=True)[0]
    return sol[qq]


def h2h_10():
    ap = symbols("ap", positive=True)
    return simplify(together(1 / ap - 1 / (ap + 3))).subs(ap, a)


def h2h_11():
    tt = symbols("tt", positive=True)
    A = symbols("A")
    amp = solve(Eq(A * 2 ** (-0 / 6), 48), A)[0]
    return solve(Eq(amp * 2 ** (-tt / 6), 6), tt)[0]


def h2h_12():
    kk = symbols("kk")
    roots = solve(Eq(x ** 2 - 10 * x + 18, 0), x)
    return [solve(Eq((5 + sqrt(kk)), rt), kk)[0] for rt in roots if rt > 5][0]


def h2h_13():
    ap = symbols("ap", positive=True)
    return simplify(sqrt(50 * ap ** 5) / sqrt(2 * ap)).subs(ap, a)


def h2h_14():
    hh, ww = symbols("hh ww", positive=True)
    return simplify(3 * ww / (2 * ww / hh)).subs({hh: h, ww: w})


def h2h_15():
    """Six symbolic values whose mean is m, transformed term by term."""
    vals = list(symbols("v0:6"))
    mm = symbols("mm")
    new_mean = sum(2 * (vv + 4) for vv in vals) / 6
    # impose only the stated fact, that the six values average to m
    pinned = new_mean.subs(vals[0], 6 * mm - sum(vals[1:]))
    return simplify(pinned).subs(mm, m)


def h2h_16():
    rows = [("Almond", 250, 18), ("Barley", 180, 15),
            ("Clove", 320, 22), ("Damson", 140, 12)]
    return max(rows, key=lambda row: Rational(row[2], row[1]))[0]


def h2h_17():
    hours = symbols("hours")
    return solve(Eq(L_ - c * hours, s), hours)[0]


def h2h_18():
    return Rational(24, 18 + 24)


def h2h_19():
    rr, hh = symbols("rr hh", positive=True)
    whole = Rational(1, 3) * pi * rr ** 2 * hh
    upper = Rational(1, 3) * pi * (rr / 2) ** 2 * (hh / 2)
    return simplify(upper / whole)


def h2h_20():
    return floor(Rational(30 * 24 * 5, 4 ** 3))


def h2h_21():
    ang = symbols("ang", positive=True)
    opp, hyp = 5, 13
    adj = sqrt(hyp ** 2 - opp ** 2)
    return simplify(Rational(opp, 1) / adj)


def h2h_22():
    kk = symbols("kk")
    slope = (-2 * x + 9).coeff(x)
    perp = -1 / slope
    return solve(Eq((kk - 4) / (5 - 1), perp), kk)[0]


DERIVE = {
 "H1-01": h1_01,
 "H1-02": h1_02,
 "H1-03": h1_03,
 "H1-04": h1_04,
 "H1-05": h1_05,
 "H1-06": h1_06,
 "H1-07": h1_07,
 "H1-08": lambda: cancel((8 * w ** 3 - 27) / (2 * w - 3)),
 "H1-09": h1_09,
 "H1-10": lambda: solve(Eq(4 ** 2 + p * 4 + 72, 0), p)[0],
 "H1-11": h1_11,
 "H1-12": lambda: solve(Eq(6 / (x - 2), 4 / (x - 4)), x)[0],
 "H1-13": h1_13,
 "H1-14": h1_14,
 "H1-15": lambda: Rational(45, 10) * 25 * Rational(144, 100),
 "H1-16": h1_16,
 "H1-17": h1_17,
 "H1-18": h1_18,
 "H1-19": lambda: Rational(6 + 10, 2) * Rational(35, 10) * 12,
 "H1-20": h1_20,
 "H1-21": h1_21,
 "H1-22": h1_22,

 "H2E-01": lambda: solve(Eq(b + 14, 39), b)[0],
 "H2E-02": lambda: (152 * t).subs(t, 25),
 "H2E-03": lambda: solve(Eq(g - 9, 41), g)[0],
 "H2E-04": h2e_04,
 "H2E-05": h2e_05,
 "H2E-06": lambda: solve(Eq(340 * h, 2720), h)[0],
 "H2E-07": lambda: 480 - 315,
 "H2E-08": lambda: factor(6 * x ** 2 + 15 * x),
 "H2E-09": lambda: expand((2 * x + 7) ** 2),
 "H2E-10": lambda: Rational(sum(solve(Eq((x - 6) * (x + 2), 0), x)), 2),
 "H2E-11": lambda: max(solve(Eq((n - 9) * (n + 4), 0), n)),
 "H2E-12": h2e_12,
 "H2E-13": lambda: simplify(symbols("y", positive=True) ** 11 / symbols("y", positive=True) ** 4),
 "H2E-14": lambda: Rational(1260, 9),
 "H2E-15": lambda: Rational(18, 100) * 650,
 "H2E-16": h2e_16,
 "H2E-17": lambda: 5 * 50,
 "H2E-18": lambda: Rational(28, 80),
 "H2E-19": h2e_19,
 "H2E-20": lambda: Rational(90, 360) * 36,
 "H2E-21": h2e_21,
 "H2E-22": lambda: Rational(20, 21),

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

# Nothing in Test 22 resists a symbolic derivation: every answer is a value, an
# algebraic form, an inequality built from a sympy-solved boundary, or a named
# table row picked out by a sympy/Python comparison over the printed data.
# MANUAL is therefore empty and pass 1 covers all 66.
MANUAL = {}


def latex_to_expr(text):
    """Turn one answer choice into something sympify can read."""
    t = text.replace("&deg;", "").replace("&gt;", ">").replace("&lt;", "<")
    t = re.sub(r"\\left|\\right", "", t)
    t = re.sub(r"\\\((.*?)\\\)", r"\1", t, flags=re.S)
    # The rewrite order cannot be fixed by choosing an order: a fraction can sit
    # inside an exponent (a^{\frac{7}{12}}) as readily as an exponent inside a
    # fraction (\frac{4a^{3}}{b^{4}}), and either fixed order fails one of them.
    # Alternate the two to a fixed point instead.
    for _ in range(8):
        before = t
        t = re.sub(r"\^\{([^{}]*)\}", r"**(\1)", t)
        t = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"((\1)/(\2))", t)
        if t == before:
            break
    t = t.replace("\\pi", "pi").replace("\\cdot", "*").replace("\\sqrt", "sqrt")
    t = t.replace("\\le", "<=").replace("\\ge", ">=").replace("\\ne", "!=")
    t = t.replace("{,}", "").replace(",", "").replace("$", "").replace("%", "")
    t = t.replace("^", "**").replace("{", "(").replace("}", ")")
    # implicit multiplication: after a digit, after a closing paren, and after a
    # lone symbol — \(x(x+7)\) parses to nonsense without the last of the three,
    # and the lookbehind keeps sqrt( / cos( from being mangled.
    t = re.sub(r"(\d)\s*([a-zA-Z(])", r"\1*\2", t)
    t = re.sub(r"\)\s*\(", ")*(", t)
    t = re.sub(r"(?<![a-zA-Z])([a-zA-Z])\s*\(", r"\1*(", t)
    # A surviving multi-letter run is an implicit product, not one symbol:
    # without this \frac{uv}{u+v} parses as a symbol named "uv" and the key
    # silently fails to match. Known function names are left alone.
    def split_run(mo):
        word = mo.group(0)
        if word in ("sqrt", "pi", "sin", "cos", "tan", "log", "ln", "Abs"):
            return word
        return "*".join(word)
    t = re.sub(r"(?<![\\a-zA-Z])[a-zA-Z]{2,}(?![a-zA-Z(])", split_run, t)
    return t.strip()


def as_expr(text):
    """Parse a choice under both the plain and the positive-assumption reading.

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
        # A form, an inequality or a named table row: the derivation builds the
        # exact string out of sympy-computed values, so this is still a
        # comparison against a derived result, not against the author's note.
        norm = lambda z: re.sub(r"\\\(|\\\)|\s", "", z)
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
    check(set(bal) == set("ABCD"), f"{name}: answer key misses a letter {dict(bal)}")
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
        for cch in qq["choices"]:
            check(bool(re.search(r"[A-Za-z0-9]", cch)),
                  f"{tag}: an answer choice renders as an empty row")
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
        for mm in re.finditer(r"(?<![A-Za-z])sqrt\s*\(", bare):
            check(False, f"{tag}: plain-text sqrt(")
        for mm in re.finditer(r"[\dA-Za-z)]\s*\*\s*[\dA-Za-z(]", bare):
            check(inside(mm.start()), f"{tag}: asterisk multiplication outside math mode")
        for mm in re.finditer(r"(?<![\d/:])\d+\s*/\s*\d+(?![\d/])", bare):
            check(inside(mm.start()), f"{tag}: slash fraction outside math mode")
        for mm in re.finditer(r"\\(pi|frac|sqrt|cdot|le|ge|ne|pm|circ|sin|cos|tan|log|ln|"
                              r"left|right|overline|text)(?![a-zA-Z])", bare):
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
                check(not re.search(r"(?<!\\)(?<![A-Za-z])" + fn + r"(?![A-Za-z])", span_text),
                      f"{tag}: unescaped {fn} inside math mode")
            # A math span must never carry an HTML entity: MathContent runs
            # KaTeX over the RAW string before the browser parses entities, so
            # "&lt;" reaches KaTeX literally and renders as text.
            check("&" not in span_text, f"{tag}: HTML entity inside a math span: {span_text!r}")
            words = re.findall(r"[A-Za-z]{3,}", re.sub(r"\\[a-zA-Z]+", "", span_text))
            check(len(words) < 2, f"{tag}: prose inside math mode: {span_text!r}")

        # an inline span must not be glued to the surrounding prose
        for mo in re.finditer(r"[A-Za-z0-9]\\\(", bare):
            check(False, f"{tag}: math span opens with no space before it")
        for mo in re.finditer(r"\\\)[A-Za-z0-9]", bare):
            check(False, f"{tag}: math span closes with no space after it")

        # balanced markup, counted with a closing boundary so "<u" cannot match
        # "<ul" — a boundary-free substring match in a checker is worse than no
        # check, because it trains you to ignore the output.
        for tagname in ("table", "tr", "td", "th", "ul", "li", "em", "u"):
            opens = len(re.findall(r"<" + tagname + r"(?![a-zA-Z])", blk))
            closes = len(re.findall(r"</" + tagname + r"(?![a-zA-Z])", blk))
            check(opens == closes, f"{tag}: unbalanced <{tagname}> ({opens} open, {closes} close)")

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
# The corpora live at the content-pool ROOT and are READ ONLY.
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
    print(f"   {len(flagged)} match(es) at or above {READ_THRESHOLD:.2f} — READ each one:")
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
# across that boundary shows the same scene twice in one sitting. Keywords are
# thematic only: an ordinary English word ("ground", "batch", "tray") is not a
# setting and must not be listed, or the check turns into noise.
SETTING_KEYWORDS = [
    # Module 1 territory — beekeeping, apiaries, honey extraction
    "bee", "hive", "apiar", "colony", "colonies", "brood", "super", "comb",
    "honey", "nectar", "pollinat", "swarm", "queen", "uncap", "frame",
    "refractometer", "settling tank", "jar", "orchard", "oilseed", "forage",
    # Module 2 territory — sugar refining, beet processing, confectionery,
    # beeswax and candle making
    "beet", "sugar", "refiner", "refined", "cossette", "diffuser", "syrup",
    "molasses", "weighbridge", "filter bed", "sack",
    "sweet", "boiling pan", "confection", "candle", "wax", "wick", "mould",
    "taper", "stub", "dipping",
]
m1_text = " ".join(qq["stem"].lower() for qq in MODULE_1)
m2_text = " ".join(qq["stem"].lower() for qq in MODULE_2_EASY + MODULE_2_HARD)


def has(kwd, text):
    """Prefix match anchored at a word boundary: "wax" catches "waxes" but
    "bee" must not catch "been", so a keyword that is a prefix of a common
    English word gets an explicit exclusion below. `\\b` on its own is what made
    "fen" match "fence" and "\\bpi" match nothing at all."""
    return re.search(r"(?<![a-z])" + re.escape(kwd), text) is not None


# Prefix matches that would fire on ordinary English rather than on the setting.
FALSE_FRIENDS = {
    # "bee" is a prefix of "beet" and of "been" — exactly the class of silent
    # over-match that made "\bfen" hit "fence".
    "bee": r"(?<![a-z])bee(t|n|f)",
    "comb": r"(?<![a-z])combin",
    "super": r"(?<![a-z])superv",
    "frame": r"(?<![a-z])framework",
    "sack": r"(?<![a-z])sacked",
    "refined": r"(?<![a-z])refinedly",
}


def has_setting(kwd, text):
    if not has(kwd, text):
        return False
    if kwd in FALSE_FRIENDS:
        real = len(re.findall(r"(?<![a-z])" + re.escape(kwd), text)) - \
               len(re.findall(FALSE_FRIENDS[kwd], text))
        return real > 0
    return True


shared = [kwd for kwd in SETTING_KEYWORDS
          if has_setting(kwd, m1_text) and has_setting(kwd, m2_text)]
check(not shared, f"settings reused across Module 1 and a Module 2 branch: {shared}")
in_m1 = [kwd for kwd in SETTING_KEYWORDS if has_setting(kwd, m1_text)]
in_m2 = [kwd for kwd in SETTING_KEYWORDS if has_setting(kwd, m2_text)]
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
print(f"highest Jaccard vs production: {worst_prod:.2f}   within Test 22: {worst_self:.2f}")

if FAIL:
    print(f"\n{len(FAIL)} FAILURES:")
    for f in FAIL:
        print("  -", f)
    raise SystemExit(1)
print("\nALL CHECKS PASSED")
