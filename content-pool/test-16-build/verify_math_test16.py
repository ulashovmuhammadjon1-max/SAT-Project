#!/usr/bin/env python3
"""
Verify the 66 originally-authored Math questions for Test 16.

Four passes, because each of them has caught a different class of defect in
earlier builds:

 1. Every answer is re-derived with sympy *from the question itself*, never
    read off the `check` note. A wrong `check` and a wrong key agree with each
    other; only an independent derivation catches that. Anything that is not
    a value sympy can compare against is listed in MANUAL with a written
    reason, and MANUAL is deliberately tiny.
 2. House style is enforced on the rendered HTML — the Test 1/2 rules in
    CLAUDE.md plus the DB-wide rendering checks (no bare `^`, `sqrt(`,
    `*`-as-multiply, slash fractions, ASCII comparison operators, spelled-out
    Greek, or a LaTeX macro outside a math span).
 3. Template dedupe against every Math stem live in production, read from the
    local snapshot `prod_math_stems.json`. Not just exact duplicates: a
    question that reuses a template with new numbers is a repeat, so stems are
    reduced to a number-free token signature and compared by Jaccard.
 4. The same Jaccard check among Test 16's own 66 questions, so the test does
    not repeat itself internally.

Run:  python3 verify_math_test16.py      (no DATABASE_URL needed)
"""
import json
import os
import re
import sys
from collections import Counter

from sympy import (Eq, Ge, Integer, Rational, cancel, cos, expand, pi, simplify,
                   solve, sqrt, symbols, sympify)
from sympy.core.relational import Relational

from math_test16 import MODULE_1, MODULE_2_EASY, MODULE_2_HARD, ALL

HERE = os.path.dirname(os.path.abspath(__file__))

# Symbol names deliberately avoid S, E, I, N, O, Q and beta/gamma/zeta:
# sympify("S") returns the SingletonRegistry and silently degrades a
# comparison to a string compare.
a, b, c, d, g, h, k = symbols("a b c d g h k")
m, n, p, r, s, t = symbols("m n p r s t")
u, v, w, x, y = symbols("u v w x y")
P_POS = symbols("p", positive=True)

FAIL = []
PROD_THRESHOLD = 0.75
SELF_THRESHOLD = 0.75


def check(cond, msg):
    if not cond:
        FAIL.append(msg)


# ---------------------------------------------------------------- derivations
def h1_01():
    sol = solve([Eq(7 * h + 4 * m, 258), Eq(3 * h + 8 * m, 274)], [h, m])
    return sol[h]


def h1_05():
    sol = solve([Eq(c + b, 46), Eq(38 * c + 22 * b, 1332)], [c, b])
    return sol[c]


def h1_09():
    kv = 40 * Integer(3) ** 2
    return [rr for rr in solve(Eq(kv / d ** 2, 10), d) if rr > 0][0]


def h1_12():
    return [rr for rr in solve(Eq(g, P_POS ** 2 / 4 - 9), P_POS)
            if rr.subs(g, 7) > 0][0]


def h1_13():
    sol = solve([Eq(a + c, 14), Eq(4 * a + c, 26)], [a, c])
    return sol[a] * 36 + sol[c]


def h1_18():
    counts = [(1, 4), (2, 7), (3, 9), (4, 5)]
    vals = [sup for sup, cnt in counts for _ in range(cnt)]
    vals.sort()
    assert len(vals) % 2 == 1
    return Integer(vals[len(vals) // 2])


def h2h_01():
    sol = solve([Eq(5 * x + 2 * y, 94), Eq(2 * x + 5 * y, 109)], [x, y])
    return sol[x] + sol[y]


def h2h_02():
    slope = Rational(14 - (-2), 11 - 3)
    return -2 - slope * 3


def h2h_07():
    sol = solve([Eq(3 * p + 4 * w, 131), Eq(5 * p + 2 * w, 139)], [p, w])
    return sol[p] - sol[w]


def h2h_11():
    av = solve(Eq(a * (2 - 6) ** 2 - 40, 8), a)[0]
    return av * (9 - 6) ** 2 - 40


def h2h_13():
    hv = Rational(12, 2 * 3)
    return hv + (3 * hv ** 2 - 12 * hv + 7)


def h2h_16():
    rows = [("Salt", 120, 45), ("Baled wool", 40, 130),
            ("Glass sand", 90, 62), ("Coiled rope", 55, 98)]
    return max(rows, key=lambda z: z[1] * z[2])[0]


def h2h_21():
    pq = Rational(8, 17) * 51
    return sqrt(Integer(51) ** 2 - pq ** 2)


DERIVE = {
 "H1-01": h1_01,
 "H1-02": lambda: 410 + Rational(690 - 410, 7 - 3) * (5 - 3),
 "H1-03": lambda: solve(Eq(96 + Rational(60 - 96, 11 - 2) * (t - 2), 0), t)[0],
 "H1-04": lambda: max(i for i in range(200) if 50 * i + 35 * 6 <= 14 * 60),
 "H1-05": h1_05,
 "H1-06": lambda: solve(Eq((2 * m - 4) - 6, m + 6), m)[0],
 "H1-07": lambda: 18 * Rational(63, 18 + 24),
 "H1-08": lambda: cancel((9 * x ** 2 - 64) / (3 * x + 8)),
 "H1-09": h1_09,
 "H1-10": lambda: solve(Eq(12 ** 2 - 4 * 2 * k, 0), k)[0],
 "H1-11": lambda: solve(Eq(p * Rational(8, 10) ** 3, 256), p)[0],
 "H1-12": h1_12,
 "H1-13": h1_13,
 "H1-14": lambda: Rational(320, 40) * 3 * Rational(15, 2),
 "H1-15": lambda: solve(Eq(40 * Rational(15, 100) * p, 69), p)[0],
 "H1-16": lambda: (400 * Rational(1, 4) + 320 * Rational(1, 2)
                   + 260 * Integer(1) + 120 * Rational(3, 2)),
 "H1-17": lambda: Rational(9 * 46 - 4 * 51, 5),
 "H1-18": h1_18,
 "H1-19": lambda: Rational(240, 96) * Rational(28, 10),
 "H1-20": lambda: simplify(14 / cos(pi / 3)),
 "H1-21": lambda: Rational(3 * 12 * 8, 100) * 1000 / 96,
 "H1-22": lambda: 96 * Rational(18, 12) ** 3,

 "H2E-01": lambda: Rational(336, 12),
 "H2E-02": lambda: Rational(97 - 19, 6),
 "H2E-03": lambda: 30 + 45 * 4,
 "H2E-04": lambda: 1200 - 15 * h,
 "H2E-05": lambda: Ge(a, 15),
 "H2E-06": lambda: solve(Eq(14 * p + 35, 203), p)[0],
 "H2E-08": lambda: expand((9 * k + 40) - (3 * k - 8)),
 "H2E-09": lambda: 2 * Integer(3) ** 3,
 "H2E-10": lambda: [rr for rr in solve(Eq(3 * x ** 2, 75), x) if rr > 0][0],
 "H2E-11": lambda: Rational(120, 8 + 2),
 "H2E-12": lambda: Integer(27) ** Rational(2, 3),
 "H2E-13": lambda: 200 * Integer(2) ** 4,
 "H2E-14": lambda: 38 * 24,
 "H2E-15": lambda: Rational(12, 100) * 750,
 "H2E-16": lambda: 90 - 63,
 "H2E-17": lambda: Rational(12 + 9 + 15 + 9 + 11 + 16, 6),
 "H2E-18": lambda: Rational(9, 40),
 "H2E-19": lambda: 360 - 95 - 78 - 120,
 "H2E-20": lambda: 32 * 18,
 "H2E-21": lambda: solve(Eq(2 * pi * r, 14 * pi), r)[0],
 "H2E-22": lambda: sqrt(Integer(10) ** 2 - Integer(6) ** 2),

 "H2H-01": h2h_01,
 "H2H-02": h2h_02,
 "H2H-03": lambda: max(i for i in range(1000)
                       if 180 * 9 + 120 * i <= 4200 and i >= 2 * 9),
 "H2H-04": lambda: 5 * solve(Eq(3 * x + 2 * 4, 17), x)[0] - 4 * 4,
 "H2H-05": lambda: (39 - 12 * Rational(59 - 39, 20 - 12)
                    + Rational(59 - 39, 20 - 12) * d),
 "H2H-06": lambda: Ge(40 * a + 65 * b, 500),
 "H2H-07": h2h_07,
 "H2H-08": lambda: expand((x / 2 + 3) ** 2 - 4 * (x / 2 + 3)),
 "H2H-09": lambda: simplify(2 / (x - 3) - 1 / (x + 2)),
 "H2H-10": lambda: sum(solve(Eq(6 / (x - 2), x + 3), x)),
 "H2H-11": h2h_11,
 "H2H-12": lambda: simplify((4 * x ** 3 * y) ** 2 / (8 * x ** 4 * y ** 3)),
 "H2H-13": h2h_13,
 "H2H-14": lambda: 1 / (Rational(1, 6) + Rational(1, 12)),
 "H2H-15": lambda: Rational(6, 200) * 15000,
 "H2H-16": h2h_16,
 "H2H-17": lambda: 12 * 84 - 11 * 82,
 "H2H-18": lambda: solve(Eq(Rational(3, 4) * Rational(4, 5) * n, 240), n)[0],
 "H2H-19": lambda: [rr for rr in solve(Eq(pi * r ** 2 * 18,
                                          Rational(4, 3) * pi * 6 ** 3), r)
                    if rr > 0][0],
 "H2H-20": lambda: solve(Eq(2 * b + b, 129), b)[0],
 "H2H-21": h2h_21,
 "H2H-22": lambda: [rr for rr in solve(Eq(2 * w * w * 3, 150), w) if rr > 0][0],
}

# The only question whose key is a sentence rather than a value or a form
# sympy can hold. Its answer is checked against the phrase the derivation
# demands instead, which is the strongest check available for prose.
MANUAL = {
 "H2E-07": ("The four choices are English sentences interpreting a constant in "
            "a linear model; there is no expression to compare. Checked by "
            "requiring the key to be the sentence identifying 1.8 as the "
            "height at low water, i.e. the value of H when t is 0."),
}
MANUAL_MARKER = {
 "H2E-07": "at low water",
}


def latex_to_expr(text):
    """Turn one answer choice into something sympify can read."""
    t = text.replace("&deg;", "").replace("&gt;", ">").replace("&lt;", "<")
    t = re.sub(r"\\left|\\right", "", t)
    t = re.sub(r"\\\((.*?)\\\)", r"\1", t, flags=re.S)
    t = re.sub(r"\\\[(.*?)\\\]", r"\1", t, flags=re.S)
    t = t.replace("\\ge", ">=").replace("\\le", "<=").replace("\\ne", "!=")
    # \sqrt is parked behind a non-letter placeholder so the implicit-product
    # rules below never turn "sqrt(" into "sqrt*(".
    t = t.replace("\\sqrt", "#")
    t = t.replace("\\pi", "pi").replace("\\cdot", "*")
    t = t.replace("{,}", "").replace(",", "").replace("$", "").replace("%", "")
    # Exponents first, then fractions, each to a fixed point: \frac's arguments
    # are matched with a non-recursive [^{}]* pattern, so any braces nested
    # inside them (an exponent, or a second \frac) have to be flattened first
    # or the outer \frac silently never matches.
    for _ in range(6):
        new = re.sub(r"\^\{([^{}]*)\}", r"**(\1)", t)
        if new == t:
            break
        t = new
    for _ in range(6):
        new = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"((\1)/(\2))", t)
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
        return simplify(other - got) == 0
    except Exception:
        return False


print("== pass 1: independent sympy derivation")
derived_count = 0
for q in ALL:
    tag = q["n"]

    if tag in MANUAL:
        marker = MANUAL_MARKER[tag]
        text = q["choices"]["ABCD".index(q["correct"])] if q["type"] == "MC" else ""
        check(marker.lower() in text.lower(),
              f"{tag}: MANUAL key {text!r} does not carry {marker!r}")
        continue

    check(tag in DERIVE, f"{tag}: no derivation registered")
    if tag not in DERIVE:
        continue
    got = DERIVE[tag]()
    derived_count += 1

    if q["type"] == "FR":
        ok = False
        for ans in q["answers"]:
            try:
                ok = ok or same(got, parse_choice(ans))
            except Exception:
                ok = ok or ans.strip() == str(got).strip()
        check(ok, f"{tag}: sympy derived {got}, accepted answers are {q['answers']}")
        continue

    text = q["choices"]["ABCD".index(q["correct"])]
    if isinstance(got, str):
        check(same(got, text), f"{tag}: sympy derived {got!r}, key is {text!r}")
    else:
        # Try plain symbols first, then the positive-assumption reading: a
        # symbol declared positive is a *different* Symbol from an undeclared
        # one, so one parse can miss a match that is really there.
        ok = False
        for loc in ({}, {nm: symbols(nm, positive=True)
                         for nm in ("a", "b", "g", "p", "r", "x", "y")}):
            try:
                if same(got, parse_choice(text, loc)):
                    ok = True
                    break
            except Exception:
                pass
        if not ok:
            ok = latex_to_expr(text).replace(" ", "") == str(got).replace(" ", "")
        check(ok, f"{tag}: sympy derived {got}, but choice {q['correct']} is {text!r}")

    # every distractor must be genuinely different from the key
    for i, alt in enumerate(q["choices"]):
        if i == "ABCD".index(q["correct"]):
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
    fr = [q for q in mod if q["type"] == "FR"]
    mc = [q for q in mod if q["type"] == "MC"]
    check(len(fr) == 3, f"{name}: {len(fr)} free-response, the target is exactly 3")
    check(len(mc) == 19, f"{name}: {len(mc)} multiple-choice, expected 19")
    dom = Counter(q["domain"] for q in mod)
    check(dom["ALG"] == 7 and dom["ADV"] == 6 and dom["PSDA"] == 5 and dom["GT"] == 4,
          f"{name}: domain mix is {dict(dom)}, wanted 7 ALG / 6 ADV / 5 PSDA / 4 GT")
    bal = Counter(q["correct"] for q in mc)
    check(max(bal.values()) <= 7, f"{name}: answer key unbalanced {dict(bal)}")

check(sum(1 for q in ALL if q["skill"] == "GT-TR") >= 1,
      "the whole test has no GT-TR question")

VALID_SKILLS = {
    "ALG": {"ALG-LE", "ALG-LF", "ALG-LI"},
    "ADV": {"ADV-NF", "ADV-EQ", "ADV-NE"},
    "PSDA": {"PSDA-RP", "PSDA-ST", "PSDA-DI"},
    "GT": {"GT-AV", "GT-LA", "GT-TR"},
}

SPAN = re.compile(r"\\\((.*?)\\\)|\\\[(.*?)\\\]", re.S)

seen_ids = set()
for q in ALL:
    tag = q["n"]
    check(tag not in seen_ids, f"{tag}: duplicate question id")
    seen_ids.add(tag)
    check(q["skill"] in VALID_SKILLS[q["domain"]],
          f"{tag}: skill {q['skill']} is not a {q['domain']} skill")
    check(bool(q.get("check")), f"{tag}: no check note")

    blocks = [q["stem"]] + list(q.get("choices") or [])
    if q["type"] == "MC":
        check(len(q["choices"]) == 4, f"{tag}: needs exactly 4 choices")
        check(len(set(q["choices"])) == 4, f"{tag}: duplicate answer choice")
        check(q["correct"] in "ABCD", f"{tag}: bad answer label")
    else:
        check(bool(q.get("answers")), f"{tag}: free response with no accepted answer")

    for blk in blocks:
        # <img> payloads would false-positive on every pattern below; there
        # are none in this build, but strip them so the rule holds if one is
        # ever added.
        blk = re.sub(r"<img[^>]*>", " ", blk)

        check(not blk.strip().startswith("<p>"), f"{tag}: stem is <p>-wrapped")
        check("°" not in blk, f"{tag}: raw degree glyph, use &deg;")
        spans = [mm.span() for mm in SPAN.finditer(blk)]

        def inside(i, spans=spans):
            return any(aa <= i < bb for aa, bb in spans)

        for mm in re.finditer(r"\^", blk):
            check(inside(mm.start()), f"{tag}: caret outside math mode")
        for mm in re.finditer(r"\bsqrt\s*\(", blk):
            check(False, f"{tag}: plain-text sqrt(")
        for mm in re.finditer(r"[\dA-Za-z)]\s*\*\s*[\dA-Za-z(]", blk):
            check(inside(mm.start()), f"{tag}: asterisk multiplication outside math mode")
        for mm in re.finditer(r"(?<![\d/:])\d+\s*/\s*\d+(?![\d/])", blk):
            check(inside(mm.start()), f"{tag}: slash fraction outside math mode")
        for mm in re.finditer(r"\\(pi|frac|sqrt|cdot|le|ge|ne|circ|sin|cos|tan|log|ln)\b", blk):
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

    stem = q["stem"]
    if re.search(r"\btables?\b", stem, re.I):
        check("<table" in stem, f"{tag}: mentions a table but has no <table> markup")
    if re.search(r"\b(shown|the figure|graph|chart|plot|diagram|following (?:graph|figure|chart))\b",
                 stem, re.I):
        check("<table" in stem or "<img" in stem,
              f"{tag}: refers to a visual it does not contain")
    if "system" in stem.lower() and len(re.findall(r"=", stem)) >= 2:
        check("<br/>" in stem, f"{tag}: a system of equations must be stacked with <br/>")


# ------------------------------------------------------------------- dedupe
def sig(text):
    t = re.sub(r"<img[^>]*>", " ", text)
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"&[a-z]+;", " ", t)
    math = []
    for mm in SPAN.findall(t):
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
    t = re.sub(r"\\[a-zA-Z]+", " ", t)
    t = re.sub(r"[-+]?\d[\d,.]*", "#", t)
    tokens = (re.sub(r"[^a-z#]+", " ", t.lower()).strip() + " "
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
    for q in ALL:
        s0 = sig(q["stem"])
        score, label = max(((jaccard(s0, o), lab) for lab, o in others),
                           key=lambda z: z[0])
        worst.append((score, q["n"], label))
        check(score < PROD_THRESHOLD,
              f"{q['n']}: template similarity {score:.2f} to {label}")
    worst.sort(reverse=True)
    print(f"   highest similarity seen: {worst[0][0]:.2f}")
    print("   closest matches:")
    for sc, tag, lab in worst[:8]:
        print(f"     {sc:.2f}  {tag}  vs {lab}")

print("== pass 4: self-collision inside Test 16")
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

# ------------------------------------------------------------------- report
print()
print(f"questions: {len(ALL)}")
for label, mod in (("M1 ", MODULE_1), ("M2E", MODULE_2_EASY), ("M2H", MODULE_2_HARD)):
    doms = dict(sorted(Counter(q["domain"] for q in mod).items()))
    keys = dict(sorted(Counter(q["correct"] for q in mod if q["type"] == "MC").items()))
    frs = sum(1 for q in mod if q["type"] == "FR")
    print(f"  {label}: {len(mod)} questions, {frs} FR, domains {doms}, key {keys}")
print(f"skills: {dict(sorted(Counter(q['skill'] for q in ALL).items()))}")

if FAIL:
    print(f"\n{len(FAIL)} FAILURES:")
    for f in FAIL:
        print("  -", f)
    raise SystemExit(1)
print("\nALL CHECKS PASSED")
