#!/usr/bin/env python3
"""
Verify the 66 originally-authored Math questions for Test 26.

Four passes, because each has caught a different class of defect in earlier
builds:

 1. Every answer is re-derived with sympy *from the question itself*, never
    read off the `check` note. A wrong `check` and a wrong key agree with each
    other; only an independent derivation catches that. The derivation must
    match the marked choice and must NOT match any distractor. Anything
    genuinely not sympy-checkable goes in MANUAL with a written justification;
    the target is zero.
 2. House style on the final rendered HTML — the Test 1/2 rules in CLAUDE.md
    plus the DB-wide rendering checks (no bare `^`, `sqrt(`, `*`-as-multiply,
    slash fractions, ASCII comparison operators, spelled-out Greek, or LaTeX
    macros outside a math span), with <img> tags stripped first so a base64
    payload cannot false-positive on every pattern.
 3. Template dedupe against every Math stem live in production — the corpus at
    the content-pool ROOT (../prod_math_stems.json, 1,386 stems), not a local
    copy. Stems are compared by token signature with numbers and LaTeX
    stripped, so a template reused with new numbers still scores high. The
    threshold decides what gets READ, not what is accepted: every match at or
    above 0.45 is printed so the nearest banked stem can be judged by hand.
 4. Self-collision among Test 26's own 66 stems, plus the cross-module setting
    check — a student sits Module 1 and exactly one Module 2 branch, so no
    setting keyword may appear in Module 1 and in either branch.

Run:  python3 verify_math_test26.py      (no DATABASE_URL needed)
"""
import json
import os
import re
from collections import Counter

from sympy import (Abs, Eq, Rational, cancel, cos, expand, factor, pi, simplify,
                   sin, solve, sqrt, symbols, sympify, tan)

from math_test26 import MODULE_1, MODULE_2_EASY, MODULE_2_HARD, ALL

HERE = os.path.dirname(os.path.abspath(__file__))

# Symbol names avoid sympy's singletons: S, E, I, N, O and Q all resolve to
# registry objects rather than free symbols, which silently degrades a
# comparison to a string compare. beta/gamma/zeta are avoided for the same
# reason.
x, y, c, m, n, t, v, s = symbols("x y c m n t v s")
w, p, d, h, r, u, k, b, q, f = symbols("w p d h r u k b q f")
ap = symbols("a", positive=True)
bp = symbols("b", positive=True)
# Abs() can only be solved over a symbol sympy knows to be real.
xr = symbols("xr", real=True)

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
def h1_01():
    cl = solve(Eq(c + (3 * c + 12) + c / 2, 237), c)[0]
    return 6 * (3 * cl + 12)


def h1_03():
    slope = Rational(1960 - 1480, 260 - 180)
    inter = 1480 - 180 * slope
    assert 340 * slope + inter == 2440, "the third table row does not lie on the same line"
    return 500 * slope + inter


def h1_04():
    slope = Rational(360 - 414, 10) / (15 - 6)
    return solve(Eq(Rational(414, 10) + slope * (q - 6), Rational(324, 10)), q)[0]


def h1_05():
    return max(i for i in range(50) if 1300 + 16 * 240 * i <= 12500)


def h1_10():
    return [z for z in solve(Eq(18 / x, x - 3), x) if z > 0][0]


def h1_17():
    rows = [("Bell A", 240, 1560), ("Bell B", 360, 2232),
            ("Bell C", 480, 2832), ("Bell D", 600, 3660)]
    return min(rows, key=lambda z: Rational(z[2], z[1]))[0]


def h1_19():
    """Two legs at 68 degrees: the feet are 2 x 7.5 cos(68 deg) apart."""
    val = 2 * Rational(75, 10) * cos(68 * pi / 180)
    return Rational(round(float(val), 1)).limit_denominator(1000)


def h1_21():
    grams = 140 * 22 * 22 * Rational(72, 100)
    return Rational(round(float(grams) / 1000, 1)).limit_denominator(1000)


def h2e_05():
    """Solve the capacity condition, then state it as the printed inequality."""
    bound = solve(Eq(6 + n, 15), n)[0]
    return "\\(n\\le %s\\)" % bound


def h2e_10():
    return [z for z in solve(Eq(x ** 2, 3 * x), x) if z != 0][0]


def h2e_16():
    vals = sorted([24, 31, 19, 27, 22, 35, 29])
    return vals[len(vals) // 2]


def h2h_01():
    sol = solve([Eq(3 * f + 2 * r, 51), Eq(5 * f + 4 * r, 93)], [f, r], dict=True)[0]
    return sol[r]


def h2h_02():
    slope = Rational(11 - 3, 3 - 1)          # (11a - 3a) / (3a - a)
    return 3 * ap + slope * (7 * ap - ap)


def h2h_03():
    """Fewest flue pipes for a given number of reeds is exactly twice, so the
    binding case is f = 2r; both resource limits are then checked."""
    best = 0
    for rr in range(0, 60):
        ff = 2 * rr
        if 3 * ff + 5 * rr <= 240 and 50 * ff + 160 * rr <= 6400:
            best = rr
    return best


def h2h_07():
    bound = solve(Eq(Rational(1, 3) * (2 * x - 5), Rational(1, 2) * (x + 4)), x)[0]
    return int(bound) if bound == int(bound) else int(bound // 1)


def h2h_10():
    r1, r2 = symbols("r1 r2")
    sol = solve([Eq(r1 + r2, 16), Eq(r1 - r2, 6)], [r1, r2], dict=True)[0]
    return sol[r1] * sol[r2]


def h2h_13():
    roots = solve(Eq(x ** 2 + (2 * x) ** 2, 45), x)
    return roots[0] * roots[1]


def h2h_19():
    """tan A = a/b fixes the legs; sin A follows from the hypotenuse."""
    hyp = sqrt(ap ** 2 + bp ** 2)
    return ap / hyp


def h2h_21():
    rr, ll = symbols("rr ll", positive=True)
    return simplify((2 * pi * (2 * rr) * (ll / 2)) / (2 * pi * rr * ll))


DERIVE = {
 # ------------------------------------------------------------------ Module 1
 "H1-01": h1_01,
 "H1-02": lambda: 26 * solve(Eq(t + (5 * t + 4), 646), t)[0],
 "H1-03": h1_03,
 "H1-04": h1_04,
 "H1-05": h1_05,
 "H1-06": lambda: Rational(6, 2) * (152 + (152 + 5 * 84)),
 "H1-07": lambda: 4 * solve(Eq(x + 90, 4 * x - 90), x)[0],
 "H1-08": lambda: cancel((x ** 2 - 9) / (x ** 2 + 7 * x + 12)),
 "H1-09": lambda: (lambda nv: nv ** 2 - 36 * nv + 520)(Rational(36, 2)),
 "H1-10": h1_10,
 "H1-11": lambda: 640 * Rational(92, 100) ** n,
 "H1-12": lambda: expand((3 * x - 4) * (2 * x + 7)).coeff(x, 1),
 "H1-13": lambda: Rational(3 + 11, 2),
 "H1-14": lambda: (Rational(522, 1) / Rational(96, 100)) * 1000 / Rational(87, 10),
 "H1-15": lambda: 1216 * Rational(1, 4) ** 3,
 "H1-16": lambda: Rational(1134, 10) * 1000 / (45 * 7 * 60),
 "H1-17": h1_17,
 "H1-18": lambda: Rational(18 + 12 - 3, 240),
 "H1-19": h1_19,
 "H1-20": lambda: sqrt(10 ** 2 + 24 ** 2) / 2,
 "H1-21": h1_21,
 "H1-22": lambda: pi * 21 ** 2 * (60 - 8),

 # ------------------------------------------------------------- Module 2 Easy
 "H2E-01": lambda: solve(Eq(5 * b + 13, 63), b)[0],
 "H2E-02": lambda: Rational(1260, 42),
 "H2E-03": lambda: Rational(528 - 120, 3),
 "H2E-04": lambda: 100 - 3 * 14,
 "H2E-05": h2e_05,
 "H2E-06": lambda: Rational(27 - 11, 6 - 2),
 "H2E-07": lambda: solve(Eq(1240 - 85 * r, 815), r)[0],
 "H2E-08": lambda: factor(6 * x ** 2 + 15 * x),
 "H2E-09": lambda: (lambda wv: wv ** 2 - 5 * wv + 40)(6),
 "H2E-10": h2e_10,
 "H2E-11": lambda: 1800 * Rational(104, 100) ** 0,
 "H2E-12": lambda: expand((x + 6) ** 2),
 "H2E-13": lambda: 7 + 3 * Rational(17 - 7, 3 - 1),
 "H2E-14": lambda: Rational(36, 4),
 "H2E-15": lambda: Rational(15, 100) * 340,
 "H2E-16": h2e_16,
 "H2E-17": lambda: 30 - 19,
 "H2E-18": lambda: Rational(12, 48),
 "H2E-19": lambda: Rational(36, 100) / (Rational(12, 10) * Rational(5, 10)),
 "H2E-20": lambda: Rational(360, 8),
 "H2E-21": lambda: 8 * cos(12 * pi / 180),
 "H2E-22": lambda: 2 * pi * 14,

 # ------------------------------------------------------------- Module 2 Hard
 "H2H-01": h2h_01,
 "H2H-02": h2h_02,
 "H2H-03": h2h_03,
 "H2H-04": lambda: solve(Eq(3 / (x - 4), 5 / (x + 2)), x)[0],
 "H2H-05": lambda: 13 * ap + 4 * Rational(13 - 5, 6 - 2) * ap,
 "H2H-06": lambda: 3 * solve(Eq(p + (p + 12) + (3 * p - 9), 183), p)[0] - 9,
 "H2H-07": h2h_07,
 "H2H-08": lambda: expand((x - 3) ** 2 + 5 * (x - 3)),
 "H2H-09": lambda: expand(3 * (x + 1) - 2 * (x - 2)),
 "H2H-10": h2h_10,
 "H2H-11": lambda: simplify(2 ** Rational(19, 12) / 2 ** Rational(7, 12)),
 "H2H-12": lambda: simplify(ap ** Rational(5, 6) / ap ** Rational(1, 3)),
 "H2H-13": h2h_13,
 "H2H-14": lambda: simplify((m + 3 * m / n) / (n + 1)),
 "H2H-15": lambda: Rational(63, 90),
 "H2H-16": lambda: Rational(1701, 1) / (Rational(108, 100) * Rational(105, 100)),
 "H2H-17": lambda: Rational(30 * 48 - 12 * 60, 18),
 "H2H-18": lambda: Rational(50 * 96 + 30 * 60 + 20 * 30, 100),
 "H2H-19": h2h_19,
 "H2H-20": lambda: 2 * sqrt(25 ** 2 - 20 ** 2),
 "H2H-21": h2h_21,
 "H2H-22": lambda: Rational(1, 8),
}

# Every one of the 66 is derived independently; nothing is taken on trust.
MANUAL = {}

FUNC_NAMES = ("sqrt", "sin", "cos", "tan", "log", "ln", "exp", "asin", "acos", "atan")
# Every variable in these choices is a single letter, so any surviving run of
# two or more letters that is not a function or constant name is an implicit
# product: \frac{uv}{u+v} must read as u*v/(u+v), not as a symbol called "uv".
KNOWN_WORDS = set(FUNC_NAMES) | {"pi"}


def _split_letter_run(mo):
    word = mo.group(0)
    return word if word.lower() in KNOWN_WORDS else "*".join(word)


def latex_to_expr(text):
    """Turn one answer choice into something sympify can read."""
    t = text.replace("&deg;", "").replace("&gt;", ">").replace("&lt;", "<")
    t = re.sub(r"\\left|\\right", "", t)
    t = re.sub(r"\\\((.*?)\\\)", r"\1", t, flags=re.S)
    t = t.replace("{,}", "").replace(",", "").replace("$", "").replace("%", "")
    # A degree mark has to become a radian factor BEFORE the generic exponent
    # rewrite, or 12^{\circ} turns into 12**(\circ) and never parses.
    t = re.sub(r"(\d+)\s*\^\{\\circ\}", r"(\1*pi/180)", t)
    # \frac must be flattened BEFORE the exponent rewrite when the fraction is
    # the exponent (a^{\frac{5}{6}}), and AFTER it when the exponent is inside
    # the fraction (\frac{4a^{3}}{b^{4}}); a non-recursive pattern never matches
    # nested braces either way. Alternating the two passes to a fixed point
    # handles both — no single ordering can.
    # \sqrt is in the same loop for the same reason: \frac{a}{\sqrt{a^{2}+b^{2}}}
    # needs the exponent gone before \sqrt can flatten, and \sqrt gone before
    # \frac can flatten, while \sqrt{\frac{p}{q}} needs the opposite order.
    for _ in range(5):
        t = re.sub(r"\\sqrt\{([^{}]*)\}", r"sqrt(\1)", t)
        t = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"((\1)/(\2))", t)
        t = re.sub(r"\^\{([^{}]*)\}", r"**(\1)", t)
    t = t.replace("\\pi", "pi").replace("\\cdot", "*")
    for fn in FUNC_NAMES:
        t = t.replace("\\" + fn, fn)
    t = t.replace("^", "**").replace("{", "(").replace("}", ")")
    # implicit multiplication: after a digit, after a closing paren, and after a
    # lone symbol — \(x(x+7)\) otherwise parses as a function call. The
    # lookbehind keeps sqrt(/sin( and friends intact, since their last letter is
    # preceded by another letter.
    t = re.sub(r"[A-Za-z]{2,}", _split_letter_run, t)
    t = re.sub(r"(\d)\s*([a-zA-Z(])", r"\1*\2", t)
    t = re.sub(r"\)\s*\(", ")*(", t)
    t = re.sub(r"(?<![A-Za-z])([a-zA-Z])\s*\(", r"\1*(", t)
    for fn in FUNC_NAMES:
        t = t.replace(fn + "*(", fn + "(")
    t = t.strip()
    if "=" in t:
        lhs, rhs = t.split("=", 1)
        t = "(%s)-(%s)" % (lhs, rhs)
    return t


def norm_text(text):
    """Bare comparison form for a structural (non-numeric) answer."""
    tt = re.sub(r"\\\(|\\\)", "", text)
    return re.sub(r"\s+", "", tt)


POSITIVE_LOCALS = {nm: symbols(nm, positive=True)
                   for nm in ("a", "b", "c", "k", "m", "n", "r", "u", "v", "w", "x", "y")}


def matches(text, got):
    """Does one answer string represent the derived value?"""
    if isinstance(got, str):
        return norm_text(text) == norm_text(got)
    parsed = latex_to_expr(text)
    # A symbol declared positive is a *different* Symbol from an undeclared one,
    # so try both readings before declaring a mismatch.
    for loc in ({}, POSITIVE_LOCALS):
        try:
            if eq0(sympify(parsed, locals=loc) - got):
                return True
        except Exception:
            pass
    return parsed.replace(" ", "") == str(got).replace(" ", "")


print("== pass 1: independent sympy derivation")
derived_count = 0
for qq in ALL:
    tag = qq["n"]
    if tag in MANUAL:
        continue
    check(tag in DERIVE, f"{tag}: no derivation and not listed in MANUAL")
    if tag not in DERIVE:
        continue
    got = DERIVE[tag]()
    derived_count += 1

    if qq["type"] == "FR":
        check(any(matches(ans, got) for ans in qq["answers"]),
              f"{tag}: sympy got {got}, accepted answers are {qq['answers']}")
        continue

    key = qq["choices"]["ABCD".index(qq["correct"])]
    check(matches(key, got), f"{tag}: sympy got {got}, but choice {qq['correct']} is {key!r}")
    for i, alt in enumerate(qq["choices"]):
        if i == "ABCD".index(qq["correct"]):
            continue
        check(not matches(alt, got),
              f"{tag}: distractor {'ABCD'[i]} ({alt!r}) equals the key")

print(f"   re-derived {derived_count} of {len(ALL)} questions "
      f"({len(MANUAL)} in MANUAL: {', '.join(sorted(MANUAL)) or 'none'})")
check(len(MANUAL) < 4, f"MANUAL has {len(MANUAL)} entries, the cap is 3")

# ---------------------------------------------------------------- shape rules
print("== pass 2: shape and house style")
for nm, md in (("Module 1", MODULE_1), ("Module 2 Easy", MODULE_2_EASY),
               ("Module 2 Hard", MODULE_2_HARD)):
    check(len(md) == 22, f"{nm} has {len(md)} questions, expected 22")

for name, mod in (("M1", MODULE_1), ("M2E", MODULE_2_EASY), ("M2H", MODULE_2_HARD)):
    fr = [qq for qq in mod if qq["type"] == "FR"]
    mc = [qq for qq in mod if qq["type"] == "MC"]
    check(len(fr) == 3, f"{name}: {len(fr)} free-response, the target is exactly 3")
    check(len(mc) == 19, f"{name}: {len(mc)} multiple-choice, the target is exactly 19")
    dom = Counter(qq["domain"] for qq in mod)
    check(dom["ALG"] == 7 and dom["ADV"] == 6 and dom["PSDA"] == 5 and dom["GT"] == 4,
          f"{name}: domain mix is {dict(dom)}, wanted 7 ALG / 6 ADV / 5 PSDA / 4 GT")
    bal = Counter(qq["correct"] for qq in mc)
    check(max(bal.values()) <= 7, f"{name}: answer key unbalanced {dict(bal)}")
    check(len(bal) == 4, f"{name}: answer key never uses one of the four letters {dict(bal)}")
    trig = sum(1 for qq in mod if qq["skill"] == "GT-TR")
    check(1 <= trig <= 2, f"{name}: {trig} trigonometry questions, wanted 1 or 2")

VALID_SKILLS = {
    "ALG": {"ALG-LE", "ALG-LF", "ALG-LI"},
    "ADV": {"ADV-NF", "ADV-EQ", "ADV-NE"},
    "PSDA": {"PSDA-RP", "PSDA-ST", "PSDA-DI"},
    "GT": {"GT-AV", "GT-LA", "GT-TR"},
}

SPAN = re.compile(r"\\\((.*?)\\\)|\\\[(.*?)\\\]", re.S)
VISUAL = re.compile(r"\b(table|graph|figure|chart|plot|shown|diagram)\b", re.I)

seen_ids = set()
for qq in ALL:
    tag = qq["n"]
    check(tag not in seen_ids, f"{tag}: duplicate question id")
    seen_ids.add(tag)
    check(qq["skill"] in VALID_SKILLS[qq["domain"]],
          f"{tag}: skill {qq['skill']} is not a {qq['domain']} skill")
    check(bool(qq.get("check")), f"{tag}: no check note")

    if qq["type"] == "MC":
        check(len(qq["choices"]) == 4, f"{tag}: needs exactly 4 choices")
        check(len(set(qq["choices"])) == 4, f"{tag}: duplicate answer choice")
        check(qq["correct"] in "ABCD", f"{tag}: bad answer label")
        for ch in qq["choices"]:
            check(bool(re.search(r"[A-Za-z0-9]", ch)), f"{tag}: choice with no letter or digit")
    else:
        check(bool(qq.get("answers")), f"{tag}: free response with no accepted answer")
        for ans in qq["answers"]:
            check(re.fullmatch(r"-?\d+(\.\d+)?(/\d+)?", ans),
                  f"{tag}: free-response answer {ans!r} is not a plain number")

    blocks = [qq["stem"]] + list(qq.get("choices") or [])
    for blk in blocks:
        blk = re.sub(r"<img[^>]*>", " ", blk)   # base64 payloads match everything
        check(not blk.strip().startswith("<p>"), f"{tag}: stem is <p>-wrapped")
        check("\u00b0" not in blk, f"{tag}: raw degree glyph, use &deg;")
        check("*" not in blk, f"{tag}: literal asterisk")

        spans = [mo.span() for mo in SPAN.finditer(blk)]

        def inside(i, spans=spans):
            return any(aa <= i < bb for aa, bb in spans)

        for mo in re.finditer(r"\^", blk):
            check(inside(mo.start()), f"{tag}: caret outside math mode")
        for mo in re.finditer(r"(?<![A-Za-z])sqrt\s*\(", blk):
            check(False, f"{tag}: plain-text sqrt(")
        for mo in re.finditer(r"(?<![\d/:])\d+\s*/\s*\d+(?![\d/])", blk):
            check(inside(mo.start()), f"{tag}: slash fraction outside math mode")
        for mo in re.finditer(r"\\(pi|frac|sqrt|cdot|le|ge|ne|circ|sin|cos|tan|log|ln|theta"
                              r"|alpha|times|div|pm)(?![a-zA-Z])", blk):
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
                check(not re.search(r"(?<!\\)(?<![A-Za-z])" + fn + r"(?![A-Za-z])", span_text),
                      f"{tag}: unescaped {fn} inside math mode")
            words = re.findall(r"[A-Za-z]{3,}", re.sub(r"\\[a-zA-Z]+", "", span_text))
            check(len(words) < 2, f"{tag}: prose inside math mode: {span_text!r}")

        # an inline span must not be glued to the surrounding prose
        for mo in re.finditer(r"[A-Za-z0-9]\\\(", blk):
            check(False, f"{tag}: math span opens with no space before it")
        for mo in re.finditer(r"\\\)[A-Za-z0-9]", blk):
            check(False, f"{tag}: math span closes with no space after it")

    stem_txt = re.sub(r"<[^>]+>", " ", qq["stem"])
    if VISUAL.search(stem_txt):
        check("<table" in qq["stem"] or "<img" in qq["stem"],
              f"{tag}: refers to a visual it does not contain")
    if "system of" in stem_txt.lower():
        check("<br/>" in qq["stem"], f"{tag}: system of equations not stacked with <br/>")
    check(qq["stem"].count("<table") == qq["stem"].count("</table>"),
          f"{tag}: unbalanced table markup")
    check("T20" not in qq["stem"] and "Test 20" not in qq["stem"],
          f"{tag}: scaffolding provenance from the reference template survived")

# ------------------------------------------------------------------- dedupe
print("== pass 3: template dedupe against production")


def sig(text):
    tt = re.sub(r"<img[^>]*>", " ", text)
    tt = re.sub(r"<[^>]+>", " ", tt)
    tt = re.sub(r"&[a-z]+;", " ", tt)
    math = []
    for mo in SPAN.findall(tt):
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
    tt = re.sub(r"\\[a-zA-Z]+", " ", tt)
    tt = re.sub(r"[-+]?\d[\d,.]*", "#", tt)
    joined = re.sub(r"[^a-z#]+", " ", tt.lower()).strip() + " " + " ".join(sorted(set(math)))
    return set(joined.split())


def jaccard(aa, bb):
    return len(aa & bb) / max(1, len(aa | bb))


# The corpus lives at the content-pool ROOT and is READ ONLY.
prod_path = os.path.join(HERE, "..", "prod_math_stems.json")
worst_prod = 0.0
READ_THRESHOLD = 0.45
if os.path.exists(prod_path):
    prod = json.load(open(prod_path))
    print(f"   comparing {len(ALL)} stems against {len(prod)} live production Math stems")
    others = [(pq["label"], sig(pq["stem"])) for pq in prod]
    worst = []
    for qq in ALL:
        s0 = sig(qq["stem"])
        score, label = max(((jaccard(s0, o), lab) for lab, o in others), key=lambda z: z[0])
        worst.append((score, qq["n"], label))
        worst_prod = max(worst_prod, score)
        check(score < 0.75, f"{qq['n']}: template similarity {score:.2f} to {label}")
    worst.sort(reverse=True)
    above = [row for row in worst if row[0] >= READ_THRESHOLD]
    print(f"   {len(above)} stems score at or above {READ_THRESHOLD:.2f} and were read by hand:")
    for sc, tag, lab in (above or worst[:8]):
        print(f"     {sc:.2f}  {tag}  vs {lab}")
else:
    check(False, "../prod_math_stems.json is missing — the dedupe pass cannot run")

print("== pass 4: self-collision and cross-module settings")
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

# A student sits Module 1 and exactly ONE Module 2 branch, so a setting that
# appears in Module 1 and in either branch would be met twice in one sitting.
#
# Every keyword below is either multi-word or a term with no everyday sense.
# Single ordinary words are deliberately excluded: "bell", "ring", "peal",
# "stop", "pipe", "tone", "band" and "change" all have everyday meanings, and a
# boundary-free substring match in a checker is worse than no check at all —
# earlier builds had "fen" match *fence*, "must" match the modal, and "<u"
# match "<ul". Matching uses explicit lookarounds, never \b, because a digit
# and a letter are both \w.
SETTING_KEYWORDS = {
 "M1": ["bell founder", "bell metal", "casting pit", "crucible", "foundry", "loam",
        "tuning lathe", "headstock", "shear legs", "clapper", "crown staple", "soundbow"],
 "M2E": ["ringing chamber", "practice night", "quarter peal", "striking", "ringing master",
         "bell rope", "tower fund", "tower captain", "touches", "ringers"],
 "M2H": ["organ", "voicer", "carillon", "clavier", "reed pipe", "flue pipe", "semitones",
         "tuner", "speaking length", "temperament"],
}


def kw_search(word, text):
    """Whole-term match with explicit lookarounds on both sides."""
    pat = r"(?<![a-z])" + r"\s+".join(re.escape(pp) for pp in word.split()) + r"(?![a-z])"
    return re.search(pat, text) is not None


def module_text(mod):
    return " ".join(re.sub(r"<[^>]+>", " ", qq["stem"]).lower() for qq in mod)


TEXTS = {"M1": module_text(MODULE_1), "M2E": module_text(MODULE_2_EASY),
         "M2H": module_text(MODULE_2_HARD)}

for owner, words in SETTING_KEYWORDS.items():
    for word in words:
        check(kw_search(word, TEXTS[owner]),
              f"setting keyword {word!r} claimed by {owner} but unused there")
    for other in ("M1", "M2E", "M2H"):
        if other == owner:
            continue
        # Only Module 1 against a Module 2 branch matters: the two branches are
        # never sat by the same student.
        if not ({owner, other} & {"M1"}):
            continue
        for word in words:
            check(not kw_search(word, TEXTS[other]),
                  f"setting keyword {word!r} appears in both {owner} and {other}")
print(f"   setting keywords checked: "
      f"{sum(len(v) for v in SETTING_KEYWORDS.values())} across the three modules")

# ------------------------------------------------------------------- report
print()
print(f"questions: {len(ALL)}    M1 domains: {dict(Counter(qq['domain'] for qq in MODULE_1))}")
print(f"                      M2E domains: {dict(Counter(qq['domain'] for qq in MODULE_2_EASY))}")
print(f"                      M2H domains: {dict(Counter(qq['domain'] for qq in MODULE_2_HARD))}")
print(f"skills: {dict(sorted(Counter(qq['skill'] for qq in ALL).items()))}")
for nm, md in (("M1 ", MODULE_1), ("M2E", MODULE_2_EASY), ("M2H", MODULE_2_HARD)):
    print(f"answer key {nm}: "
          f"{dict(sorted(Counter(qq['correct'] for qq in md if qq['type'] == 'MC').items()))}"
          f"   FR: {sum(1 for qq in md if qq['type'] == 'FR')}")
print(f"highest similarity vs production: {worst_prod:.2f}   "
      f"vs own set: {worst_self[0][0]:.2f}")

if FAIL:
    print(f"\n{len(FAIL)} FAILURES:")
    for fl in FAIL:
        print("  -", fl)
    raise SystemExit(1)
print("\nALL CHECKS PASSED")
