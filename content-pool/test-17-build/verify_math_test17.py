#!/usr/bin/env python3
"""
Verify the 66 originally-authored Math questions for Test 17.

Four passes, because each has caught a different class of defect in earlier
builds:

 1. Every answer is re-derived with sympy *from the question itself*, never
    read off the `check` note. A wrong `check` and a wrong key agree with each
    other; only an independent derivation catches that. Anything genuinely not
    sympy-checkable is listed in MANUAL with a written justification.
 2. House style is enforced on the final rendered HTML — the Test 1/2 rules in
    CLAUDE.md plus the DB-wide rendering checks (no bare `^`, `sqrt(`,
    `*`-as-multiply, slash fractions, ASCII comparison operators, spelled-out
    Greek, or LaTeX macros outside a math span), with <img> tags stripped
    first so base64 payloads cannot false-positive.
 3. Template dedupe against every Math stem live in production (the local
    snapshot `prod_math_stems.json`, 990 stems from Tests 1-15). Not just
    exact duplicates: a question that reuses a template with new numbers is a
    repeat, so stems are compared by token signature with all numbers and
    LaTeX stripped.
 4. Self-collision: the same Jaccard check among Test 17's own 66 questions.

Run:  python3 verify_math_test17.py      (no DATABASE_URL needed)
"""
import json
import os
import re
from collections import Counter

from sympy import (Eq, Poly, Rational, acos, cancel, expand, log, pi, simplify,
                   sin, solve, sqrt, symbols, sympify)

from math_test17 import MODULE_1, MODULE_2_EASY, MODULE_2_HARD, ALL

HERE = os.path.dirname(os.path.abspath(__file__))

# Symbol names are chosen to avoid sympy's singletons: S, E, I, N, O and Q all
# resolve to registry objects rather than free symbols, which silently degrades
# a comparison to a string compare. beta/gamma/zeta are avoided for the same
# reason.
x, y, c, m, n, t, v, s = symbols("x y c m n t v s")
w, p, a, d, h, r, u, k, b = symbols("w p a d h r u k b")
Y = symbols("Y")

FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)


def eq0(expr):
    """True when a sympy difference is zero, exactly or numerically."""
    try:
        sim = simplify(expr)
    except Exception:
        return False
    if sim == 0:
        return True
    try:
        return abs(complex(sim)) < 1e-9
    except Exception:
        return False


# ---------------------------------------------------------------- derivations
def h1_12():
    """m is fixed by matching coefficients of an identity in x."""
    expr = expand((3 * x + m) * (2 * x - 5) - (6 * x ** 2 - 7 * x - 20))
    sol = solve(Poly(expr, x).all_coeffs(), m)
    return (sol[m] if isinstance(sol, dict) else sol[0])


def h2h_01():
    """The second equation must be a constant multiple of the first."""
    ratio = Rational(9, 6)
    assert ratio * 14 == 21, "the constants do not share the coefficient ratio"
    return ratio * (-4)


def h2h_03():
    """An inequality chain: the heaviest allowed rate covers the least ground."""
    lo = Rational(1320, 80)
    hi = Rational(1320, 55)
    return "%s\\le h\\le %s" % (float(lo), hi)


def h2h_05():
    """Perpendicular to 4x-6y=15 through (-3,7), in the choices' normal form."""
    slope_fence = Rational(4, 6)
    slope_cut = -1 / slope_fence
    return expand(2 * (y - 7 - slope_cut * (x + 3)))


def h2h_12():
    expr = expand(3 * (x + r) ** 2 + w - (3 * x ** 2 + 24 * x + 61))
    sols = solve(Poly(expr, x).all_coeffs(), [r, w])
    rr, ww = [(pr, pw) for pr, pw in sols if pr.is_real][0]
    return rr + ww


def h2h_18():
    rad = [z for z in solve(Eq(pi * r ** 2 * (2 * r), 2000 * pi), r)
           if z.is_real and z > 0][0]
    return 2 * rad


DERIVE = {
 # ------------------------------------------------------------------ Module 1
 "H1-01": lambda: solve(Eq(6 * (3 * s) + 11 * s, 87), s)[0] * 3,
 "H1-02": lambda: 40 - solve(Eq(11 * d + 7 * (40 - d), 356), d)[0],
 "H1-03": lambda: solve(Eq(412 + Rational(542 - 412, 900 - 250) * (d - 250), 620), d)[0],
 "H1-04": lambda: 91 - Rational(7, 2) * Rational(151 - 91, 1) / (6 - Rational(7, 2)),
 "H1-05": lambda: max(i for i in range(200) if 6 * 34 + 9 * i <= 260),
 "H1-06": lambda: solve(Eq(v + (2 * v - 4) + 6, 44), v)[0],
 "H1-07": lambda: solve(Eq(Y, 5 * m / (m + 4)), m)[0],
 "H1-08": lambda: Rational(sum(solve(Eq((150 - 5 * p) * (p - 8), 0), p)), 2),
 "H1-09": lambda: solve(Eq(v * Rational(6, 10) ** 3, 1296), v)[0],
 "H1-10": lambda: solve(Eq(9 * sqrt(r) + 12, 93), r)[0],
 "H1-11": lambda: solve(Eq(k * 6 ** 2, 900), k)[0] * 10 ** 2,
 "H1-12": h1_12,
 "H1-13": lambda: Rational(1296, 18) * 25 / 60 / 6,
 "H1-14": lambda: 40 * Rational(105, 100) * Rational(72, 100),
 "H1-15": lambda: Rational((80 - 30) * 100, 80),
 "H1-16": lambda: (300 * Rational(42, 10) + 200 * Rational(37, 10)) / 500,
 "H1-17": lambda: simplify(420 / sin(pi / 6)) * 18,
 "H1-18": lambda: solve(Eq((4 * x - 10) + (6 * x + 40), 180), x)[0],
 "H1-19": lambda: Rational(90 * 60 * 75 * 88, 100) / 1800,
 "H1-20": lambda: Rational(9 * 128 - 96, 8),
 "H1-21": lambda: (Rational(24, 12) + Rational(6, 8)) * 60,
 "H1-22": lambda: (Rational(12, 10) + Rational(6, 10)) / 2 * Rational(15, 10) * 40,

 # ------------------------------------------------------------- Module 2 Easy
 "H2E-01": lambda: Rational(96, 8),
 "H2E-02": lambda: Rational(340 - 85, 5),
 "H2E-03": lambda: 6 + 3 * 9,
 "H2E-04": lambda: Rational(39 - 15, 6 - 2),
 "H2E-05": lambda: 6 - 2,
 "H2E-06": lambda: solve(Eq(7 * t + 16, 709), t)[0],
 "H2E-07": lambda: expand((9 * p + 14) - (4 * p + 5)),
 "H2E-08": lambda: cancel(c ** 9 / c ** 4),
 "H2E-09": lambda: 45 - 2 * 8,
 "H2E-10": lambda: 2000 * Rational(15, 10) ** 2,
 "H2E-11": lambda: simplify(log(Rational(1080, 40), 3)),
 "H2E-12": lambda: (-2) ** 2 - 6 * (-2),
 "H2E-13": lambda: 25 * Rational(14, 10),
 "H2E-14": lambda: Rational(45 * 100, 250),
 "H2E-15": lambda: 14 + 9 + 17 + 12,
 "H2E-16": lambda: sorted([Rational(26, 10), Rational(31, 10), Rational(34, 10),
                           Rational(34, 10), Rational(40, 10)])[2],
 "H2E-17": lambda: 180 - 118,
 "H2E-18": lambda: 2 * pi * 9,
 "H2E-19": lambda: 2 * (140 + 85),
 "H2E-20": lambda: Rational(38 + 44 + 41 + 47 + 40, 5),
 "H2E-21": lambda: 14 * 32,
 "H2E-22": lambda: sqrt(Rational(250) ** 2 - 150 ** 2),

 # ------------------------------------------------------------- Module 2 Hard
 "H2H-01": h2h_01,
 "H2H-02": lambda: Rational(52, 11 - 3) * (7 - 5),
 "H2H-03": h2h_03,
 "H2H-04": lambda: solve(Eq(4 * (u + (u + Rational(3, 2))), 26), u)[0] + Rational(3, 2),
 "H2H-05": h2h_05,
 "H2H-06": lambda: solve(Eq(Rational(240, 100) * (320 - w) - Rational(90, 100) * w,
                           Rational(71520, 100)), w)[0],
 "H2H-07": lambda: expand((3 * x + 2) ** 2 - 5 * (3 * x + 2)),
 "H2H-08": lambda: simplify(1 / (x - 3) - 2 / (x + 1)),
 "H2H-09": lambda: sum(8 - z for z in solve(Eq(x ** 2 - 2 * x, 8 - x), x)),
 "H2H-10": lambda: solve(Eq(sqrt(3 * x + 16), x + 2), x)[0],
 "H2H-11": lambda: Rational(3, 4) ** Rational(18, 6) / Rational(3, 4) ** Rational(6, 6),
 "H2H-12": h2h_12,
 "H2H-14": lambda: Rational(12 * 180 + 8 * 240 + 15 * 160 + 5 * 300, 40),
 "H2H-15": lambda: Rational(48 * 2500 ** 2, 100 ** 2),
 "H2H-16": lambda: Rational(12 * 65 - 5 * 58, 7),
 "H2H-17": lambda: simplify(sin(pi / 2 - acos(Rational(9, 41)))),
 "H2H-18": h2h_18,
 "H2H-19": lambda: 8 * Rational(6 + 9, 6),
 "H2H-20": lambda: solve(Eq(5 * u - 3 * u, 96), u)[0] * 8,
 "H2H-21": lambda: 4500 * Rational(12, 10) * Rational(65, 100),
 "H2H-22": lambda: Rational(250 * 14 * 8, 100) / 14,
}

# The one question whose answer is a judgement about statistical inference
# rather than a value or a form. There is nothing for sympy to compute: the key
# is right because a margin of error bounds a plausible interval for the
# POPULATION mean, while the three distractors claim certainty about the
# population mean, a property of every individual cheese, or that no inference
# is possible at all. Hand-checked; kept deliberately to one item.
MANUAL = {
 "H2H-13": "prose statistical-inference judgement; no numeric answer to derive",
}


def latex_to_expr(text):
    """Turn one answer choice into something sympify can read."""
    t = text.replace("&deg;", "").replace("&gt;", ">").replace("&lt;", "<")
    t = re.sub(r"\\left|\\right", "", t)
    t = re.sub(r"\\\((.*?)\\\)", r"\1", t, flags=re.S)
    # Exponents first: \frac{4a^{3}}{b^{4}} has braces nested inside the
    # numerator, and a non-recursive \frac pattern silently fails to match it.
    # Rewriting ^{...} to **(...) flattens the nesting so \frac then matches.
    t = re.sub(r"\^\{([^{}]*)\}", r"**(\1)", t)
    for _ in range(3):
        t = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"((\1)/(\2))", t)
    t = t.replace("\\pi", "pi").replace("\\cdot", "*").replace("\\sqrt", "sqrt")
    t = t.replace("{,}", "").replace(",", "").replace("$", "").replace("%", "")
    t = t.replace("^", "**").replace("{", "(").replace("}", ")")
    # implicit multiplication: after a digit, after a closing paren, and after a
    # bare symbol — \(x(x+7)\) otherwise parses to a function call.
    t = re.sub(r"(\d)\s*([a-zA-Z(])", r"\1*\2", t)
    t = re.sub(r"\)\s*\(", ")*(", t)
    t = t.strip()
    if "=" in t:
        lhs, rhs = t.split("=", 1)
        t = "(%s)-(%s)" % (lhs, rhs)
    return t


def norm_text(text):
    """Bare comparison form for a structural (non-numeric) answer."""
    t = re.sub(r"\\\(|\\\)", "", text)
    return re.sub(r"\s+", "", t)


def matches(text, got):
    """Does one answer string represent the derived value?"""
    if isinstance(got, str):
        return norm_text(text) == norm_text(got)
    parsed = latex_to_expr(text)
    # A symbol declared positive is a *different* Symbol from an undeclared one,
    # so try both readings before declaring a mismatch.
    for loc in ({}, {nm: symbols(nm, positive=True)
                     for nm in ("a", "b", "c", "m", "r", "u", "x", "y", "Y")}):
        try:
            if eq0(sympify(parsed, locals=loc) - got):
                return True
        except Exception:
            pass
    return parsed.replace(" ", "") == str(got).replace(" ", "")


print("== pass 1: independent sympy derivation")
derived_count = 0
for q in ALL:
    tag = q["n"]
    if tag in MANUAL:
        continue
    check(tag in DERIVE, f"{tag}: no derivation and not listed in MANUAL")
    if tag not in DERIVE:
        continue
    got = DERIVE[tag]()
    derived_count += 1

    if q["type"] == "FR":
        check(any(matches(ans, got) for ans in q["answers"]),
              f"{tag}: sympy got {got}, accepted answers are {q['answers']}")
        continue

    key = q["choices"]["ABCD".index(q["correct"])]
    check(matches(key, got), f"{tag}: sympy got {got}, but choice {q['correct']} is {key!r}")
    for i, alt in enumerate(q["choices"]):
        if i == "ABCD".index(q["correct"]):
            continue
        check(not matches(alt, got),
              f"{tag}: distractor {'ABCD'[i]} ({alt!r}) equals the key")

print(f"   re-derived {derived_count} of {len(ALL)} questions "
      f"({len(MANUAL)} in MANUAL: {', '.join(sorted(MANUAL))})")
check(len(MANUAL) < 6, f"MANUAL has {len(MANUAL)} entries, the cap is 6")

# ---------------------------------------------------------------- shape rules
print("== pass 2: shape and house style")
for nm, md in (("Module 1", MODULE_1), ("Module 2 Easy", MODULE_2_EASY),
               ("Module 2 Hard", MODULE_2_HARD)):
    check(len(md) == 22, f"{nm} has {len(md)} questions, expected 22")

for name, mod in (("M1", MODULE_1), ("M2E", MODULE_2_EASY), ("M2H", MODULE_2_HARD)):
    fr = [q for q in mod if q["type"] == "FR"]
    mc = [q for q in mod if q["type"] == "MC"]
    check(len(fr) == 3, f"{name}: {len(fr)} free-response, the target is exactly 3")
    check(len(mc) == 19, f"{name}: {len(mc)} multiple-choice, the target is exactly 19")
    dom = Counter(q["domain"] for q in mod)
    check(dom["ALG"] == 7 and dom["ADV"] == 6 and dom["PSDA"] == 5 and dom["GT"] == 4,
          f"{name}: domain mix is {dict(dom)}, wanted 7 ALG / 6 ADV / 5 PSDA / 4 GT")
    bal = Counter(q["correct"] for q in mc)
    check(max(bal.values()) <= 7, f"{name}: answer key unbalanced {dict(bal)}")
    check(len(bal) == 4, f"{name}: answer key never uses one of the four letters {dict(bal)}")

check(sum(1 for q in ALL if q["skill"] == "GT-TR") >= 1,
      "no trigonometry question anywhere in the package")

VALID_SKILLS = {
    "ALG": {"ALG-LE", "ALG-LF", "ALG-LI"},
    "ADV": {"ADV-NF", "ADV-EQ", "ADV-NE"},
    "PSDA": {"PSDA-RP", "PSDA-ST", "PSDA-DI"},
    "GT": {"GT-AV", "GT-LA", "GT-TR"},
}

SPAN = re.compile(r"\\\((.*?)\\\)|\\\[(.*?)\\\]", re.S)
VISUAL = re.compile(r"\b(table|graph|figure|chart|plot|shown|diagram)\b", re.I)

seen_ids = set()
for q in ALL:
    tag = q["n"]
    check(tag not in seen_ids, f"{tag}: duplicate question id")
    seen_ids.add(tag)
    check(q["skill"] in VALID_SKILLS[q["domain"]],
          f"{tag}: skill {q['skill']} is not a {q['domain']} skill")
    check(bool(q.get("check")), f"{tag}: no check note")

    if q["type"] == "MC":
        check(len(q["choices"]) == 4, f"{tag}: needs exactly 4 choices")
        check(len(set(q["choices"])) == 4, f"{tag}: duplicate answer choice")
        check(q["correct"] in "ABCD", f"{tag}: bad answer label")
    else:
        check(bool(q.get("answers")), f"{tag}: free response with no accepted answer")
        for ans in q["answers"]:
            check(re.fullmatch(r"-?\d+(\.\d+)?(/\d+)?", ans),
                  f"{tag}: free-response answer {ans!r} is not a plain number")

    blocks = [q["stem"]] + list(q.get("choices") or [])
    for blk in blocks:
        blk = re.sub(r"<img[^>]*>", " ", blk)   # base64 payloads match everything
        check(not blk.strip().startswith("<p>"), f"{tag}: stem is <p>-wrapped")
        check("°" not in blk, f"{tag}: raw degree glyph, use &deg;")
        check("*" not in blk.replace("&deg;", ""), f"{tag}: literal asterisk")

        spans = [mo.span() for mo in SPAN.finditer(blk)]

        def inside(i, spans=spans):
            return any(aa <= i < bb for aa, bb in spans)

        for mo in re.finditer(r"\^", blk):
            check(inside(mo.start()), f"{tag}: caret outside math mode")
        for mo in re.finditer(r"\bsqrt\s*\(", blk):
            check(False, f"{tag}: plain-text sqrt(")
        for mo in re.finditer(r"(?<![\d/:])\d+\s*/\s*\d+(?![\d/])", blk):
            check(inside(mo.start()), f"{tag}: slash fraction outside math mode")
        for mo in re.finditer(r"\\(pi|frac|sqrt|cdot|le|ge|ne|circ|sin|cos|tan|log|ln|theta"
                              r"|alpha|times|div|pm)\b", blk):
            check(inside(mo.start()), f"{tag}: LaTeX macro outside math mode")
        for mo in re.finditer(r"(!=|<=|>=)", blk):
            check(False, f"{tag}: ASCII comparison operator, use \\ne / \\le / \\ge")
        for mo in re.finditer(r"(?<![A-Za-z])(theta|alpha|beta|lambda)(?![A-Za-z])", blk):
            check(inside(mo.start()), f"{tag}: Greek letter spelled out in prose")
        for mo in re.finditer(r"(?<![A-Za-z])pi(?![A-Za-z])", blk):
            check(inside(mo.start()), f"{tag}: bare word pi outside math mode")

        for aa, bb in spans:
            span_text = blk[aa:bb]
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

    stem_txt = re.sub(r"<[^>]+>", " ", q["stem"])
    if VISUAL.search(stem_txt):
        check("<table" in q["stem"] or "<img" in q["stem"],
              f"{tag}: refers to a visual it does not contain")
    if "system of" in stem_txt.lower():
        check("<br/>" in q["stem"], f"{tag}: system of equations not stacked with <br/>")

# ------------------------------------------------------------------- dedupe
print("== pass 3: template dedupe against production")


def sig(text):
    t = re.sub(r"<img[^>]*>", " ", text)
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"&[a-z]+;", " ", t)
    math = []
    for mo in SPAN.findall(t):
        sp = mo[0] or mo[1]
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
    joined = re.sub(r"[^a-z#]+", " ", t.lower()).strip() + " " + " ".join(sorted(set(math)))
    return set(joined.split())


def jaccard(aa, bb):
    return len(aa & bb) / max(1, len(aa | bb))


prod_path = os.path.join(HERE, "prod_math_stems.json")
worst_prod = 0.0
if os.path.exists(prod_path):
    prod = json.load(open(prod_path))
    print(f"   comparing {len(ALL)} stems against {len(prod)} live production Math stems")
    others = [(pq["label"], sig(pq["stem"])) for pq in prod]
    worst = []
    for q in ALL:
        s0 = sig(q["stem"])
        score, label = max(((jaccard(s0, o), lab) for lab, o in others), key=lambda z: z[0])
        worst.append((score, q["n"], label))
        worst_prod = max(worst_prod, score)
        check(score < 0.75, f"{q['n']}: template similarity {score:.2f} to {label}")
    worst.sort(reverse=True)
    print("   closest matches:")
    for sc, tag, lab in worst[:8]:
        print(f"     {sc:.2f}  {tag}  vs {lab}")
else:
    check(False, "prod_math_stems.json is missing — the dedupe pass cannot run")

print("== pass 4: self-collision among Test 17's own 66 questions")
worst_self = []
for i in range(len(ALL)):
    for j in range(i + 1, len(ALL)):
        sc = jaccard(sig(ALL[i]["stem"]), sig(ALL[j]["stem"]))
        worst_self.append((sc, ALL[i]["n"], ALL[j]["n"]))
        check(sc < 0.75, f"{ALL[i]['n']} vs {ALL[j]['n']}: internal similarity {sc:.2f}")
worst_self.sort(reverse=True)
print("   closest internal pairs:")
for sc, aa, bb in worst_self[:6]:
    print(f"     {sc:.2f}  {aa}  vs {bb}")

# ------------------------------------------------------------------- report
print()
print(f"questions: {len(ALL)}    M1 domains: {dict(Counter(q['domain'] for q in MODULE_1))}")
print(f"                      M2E domains: {dict(Counter(q['domain'] for q in MODULE_2_EASY))}")
print(f"                      M2H domains: {dict(Counter(q['domain'] for q in MODULE_2_HARD))}")
print(f"skills: {dict(sorted(Counter(q['skill'] for q in ALL).items()))}")
for nm, md in (("M1 ", MODULE_1), ("M2E", MODULE_2_EASY), ("M2H", MODULE_2_HARD)):
    print(f"answer key {nm}: "
          f"{dict(sorted(Counter(q['correct'] for q in md if q['type'] == 'MC').items()))}"
          f"   FR: {sum(1 for q in md if q['type'] == 'FR')}")
print(f"highest similarity vs production: {worst_prod:.2f}   "
      f"vs own set: {worst_self[0][0]:.2f}")

if FAIL:
    print(f"\n{len(FAIL)} FAILURES:")
    for f in FAIL:
        print("  -", f)
    raise SystemExit(1)
print("\nALL CHECKS PASSED")
