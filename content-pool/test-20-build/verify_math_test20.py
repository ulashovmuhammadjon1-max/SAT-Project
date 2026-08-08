#!/usr/bin/env python3
"""
Verify the 66 originally-authored Math questions for Test 20.

Four passes, because each has caught a different class of defect in earlier
builds:

 1. Every answer is re-derived with sympy *from the question itself*, never
    read off the `check` note. A wrong `check` and a wrong key agree with each
    other; only an independent derivation catches that. The derivation must
    match the marked choice and must NOT match any distractor. Anything
    genuinely not sympy-checkable is listed in MANUAL with a written
    justification.
 2. House style is enforced on the final rendered HTML — the Test 1/2 rules in
    CLAUDE.md plus the DB-wide rendering checks (no bare `^`, `sqrt(`,
    `*`-as-multiply, slash fractions, ASCII comparison operators, spelled-out
    Greek, or LaTeX macros outside a math span), with <img> tags stripped
    first so base64 payloads cannot false-positive.
 3. Template dedupe against every Math stem live in production (the local
    snapshot `prod_math_stems.json`, 1,188 stems from Tests 1-18). Not just
    exact duplicates: a question that reuses a template with new numbers is a
    repeat, so stems are compared by token signature with all numbers and
    LaTeX stripped. The threshold decides what gets READ, not what is
    accepted — every match above 0.45 is printed so the nearest banked stem
    can be judged by hand.
 4. Self-collision among Test 20's own 66 questions, plus a setting check: a
    student sees Module 1 and exactly one Module 2 branch, so no setting
    keyword may appear in both Module 1 and either Module 2 module.

Run:  python3 verify_math_test20.py      (no DATABASE_URL needed)
"""
import json
import os
import re
from collections import Counter

from sympy import (Abs, Eq, Rational, cancel, expand, pi, simplify, sin, solve,
                   sqrt, symbols, sympify)

from math_test20 import MODULE_1, MODULE_2_EASY, MODULE_2_HARD, ALL

HERE = os.path.dirname(os.path.abspath(__file__))

# Symbol names are chosen to avoid sympy's singletons: S, E, I, N, O and Q all
# resolve to registry objects rather than free symbols, which silently degrades
# a comparison to a string compare. beta/gamma/zeta are avoided for the same
# reason. Lowercase q is a plain symbol and is safe.
x, y, c, m, n, t, v, s = symbols("x y c m n t v s")
w, p, d, h, r, u, k, b, q, f = symbols("w p d h r u k b q f")
a = symbols("a", positive=True)
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
def h1_15():
    """Which crane moved the most: four products, then the largest."""
    rows = [("No. 1", 46, Rational(35, 10)), ("No. 2", 38, Rational(42, 10)),
            ("No. 3", 52, Rational(30, 10)), ("No. 4", 30, Rational(54, 10))]
    return max(rows, key=lambda z: z[1] * z[2])[0]


def h1_17():
    """32 m of jib at 62 degrees, lifted 4 m by the pivot, to the nearest metre."""
    height = 32 * sin(62 * pi / 180) + 4
    return Rational(round(float(height)))


def h2h_17():
    """sin A = BC/AB fixes AB; Pythagoras then fixes the third side AC."""
    hyp = solve(Eq(Rational(7, 25), 21 / u), u)[0]
    return sqrt(hyp ** 2 - 21 ** 2)


def h1_10():
    """d = 14 * cube root of m, solved for m rather than read off the note."""
    roots = solve(Eq(14 * m ** Rational(1, 3), 56), m)
    real = [z for z in roots if z.is_real and z > 0]
    return real[0]


def h2h_01():
    sol = solve([Eq(3 * x + 5 * y, 41), Eq(5 * x + 3 * y, 39)], [x, y], dict=True)[0]
    return simplify(sol[x] + sol[y])


def h2h_02():
    slope = Rational(-7 - 9, 6 - (-2))
    intercept = 9 - slope * (-2)
    return slope + intercept


def h2h_03():
    """An inequality chain: the binding upper bound is the answer."""
    lo = solve(Eq(3 * q - 8, 40), q)[0]
    hi = solve(Eq(2 * q + 5, 65), q)[0]
    assert lo <= hi, "the two conditions do not overlap"
    return hi


def h1_19():
    """An OPEN-topped tank: base plus four sides, and no lid."""
    return 3 * 2 + 2 * (3 * Rational(15, 10)) + 2 * (2 * Rational(15, 10))


DERIVE = {
 # ------------------------------------------------------------------ Module 1
 "H1-01": lambda: (2 * solve(Eq(p + (2 * p + 3), 84), p)[0] + 3) * Rational(45, 100),
 "H1-02": lambda: 1180 - 18 * solve(Eq(60 * (15 - u) + 130 * u, 1180), u)[0],
 "H1-03": lambda: (750 - (310 - 5 * Rational(618 - 310, 12 - 5))) / Rational(618 - 310, 12 - 5),
 "H1-04": lambda: (420 - (96 - 40 * Rational(252 - 96, 105 - 40))) / Rational(252 - 96, 105 - 40),
 "H1-05": lambda: max(i for i in range(200) if 640 * i + 1180 <= 9500),
 "H1-06": lambda: solve(Eq(9 * (q + 4) + 14 * q, 634), q)[0] + 4,
 "H1-07": lambda: expand((2 * x - 5) ** 2 - (x - 8) ** 2),
 "H1-08": lambda: (lambda sv: -2 * sv ** 2 + 72 * sv - 160)(Rational(-72, 2 * -2)),
 "H1-09": lambda: [z for z in solve(Eq(w * (w + 3), 54), w) if z > 0][0],
 "H1-10": h1_10,
 "H1-11": lambda: solve(Eq(expand(((n + 1) ** 2 + 6 * (n + 1)) - (n ** 2 + 6 * n)), 39), n)[0],
 "H1-12": lambda: expand((x + 6) * (x - 2) - (x - 3) * (x + 4)),
 "H1-13": lambda: 240 * Rational(88, 100) * 62 - 240 * 46,
 "H1-14": lambda: Rational(12500 * 72, 10) / 1000 * Rational(44, 100),
 "H1-15": h1_15,
 "H1-16": lambda: Rational(180 - 45 - 63, 180),
 "H1-17": h1_17,
 "H1-18": lambda: Rational((8 - 2) * 180, 8),
 "H1-19": h1_19,
 "H1-20": lambda: (300 * Rational(55, 100) + 240 * Rational(60, 100)
                   + 180 * Rational(45, 100) + 260 * Rational(50, 100)),
 "H1-21": lambda: 8 * (Rational(51, 10) - Rational(6, 10)),
 "H1-22": lambda: 40 * 30 * 20 - 35 * 25 * 15,

 # ------------------------------------------------------------- Module 2 Easy
 "H2E-01": lambda: Rational(154, 7),
 "H2E-02": lambda: 468 - 129,
 "H2E-03": lambda: 250 * 6 + 400,
 "H2E-05": lambda: "\\(6\\le n\\le 11\\)",
 "H2E-06": lambda: solve(Eq(x / 4 + 7, 19), x)[0],
 "H2E-07": lambda: expand(4 * (3 * x - 7) + 5 * x),
 "H2E-08": lambda: expand((x + 9) * (x - 9)),
 "H2E-09": lambda: 5 ** 2 - 9,
 "H2E-10": lambda: (Rational(125, 100) - 1) * 100,
 "H2E-11": lambda: simplify(solve(Eq(3 * 2 ** y, 96), y)[0]),
 "H2E-12": lambda: {-2: 11, -1: 4, 0: -1, 1: -4}[1],
 "H2E-13": lambda: Rational(21, 3) * 8,
 "H2E-14": lambda: Rational(120, 100) * Rational(125, 100),
 "H2E-15": lambda: 61 - 37,
 "H2E-16": lambda: max([22, 19, 25, 19, 30]) - min([22, 19, 25, 19, 30]),
 "H2E-17": lambda: 37 - 14,
 "H2E-18": lambda: 1250 * 18,
 "H2E-19": lambda: "(%s,%s)" % (Rational(-4 + 10, 2), Rational(7 + 1, 2)),
 "H2E-20": lambda: Rational(sorted([34, 41, 38, 45, 39, 43])[2]
                            + sorted([34, 41, 38, 45, 39, 43])[3], 2),
 "H2E-21": lambda: 72 * Rational(5, 8),
 "H2E-22": lambda: Rational(7, 25),

 # ------------------------------------------------------------- Module 2 Hard
 "H2H-01": h2h_01,
 "H2H-02": h2h_02,
 "H2H-03": h2h_03,
 "H2H-04": lambda: solve([Eq(4 * d + 7 * v, 63), Eq(7 * d + 4 * v, 69)], [d, v], dict=True)[0][d],
 "H2H-05": lambda: (Rational(2050 - 1290, 50 - 30) * m
                    + (1290 - 30 * Rational(2050 - 1290, 50 - 30))),
 "H2H-06": lambda: (Rational(52, 10) - Rational(12, 10)) / (Rational(84 - 52, 10) / (7 - 3)),
 "H2H-07": lambda: simplify(((2 * x - 5) + 5) / 2),
 "H2H-08": lambda: simplify(1 / (1 / u + 1 / v)),
 "H2H-09": lambda: solve(Eq(k * 4 ** Rational(15, 5), 1728), k)[0],
 "H2H-10": lambda: sum(solve(Eq(3 * x ** 2 - 12 * x - 7, 0), x)),
 "H2H-11": lambda: sum(solve(Eq(Abs(2 * xr - 9), 15), xr)),
 "H2H-12": lambda: simplify(a ** Rational(3, 4) / a ** Rational(1, 6)),
 "H2H-14": lambda: Rational(24, 60),
 "H2H-15": lambda: (Rational(115, 100) * Rational(120, 100) - 1) * 100,
 "H2H-16": lambda: 12 * Rational(154, 10) - 11 * Rational(156, 10),
 "H2H-17": h2h_17,
 "H2H-18": lambda: pi * 3 ** 2 * 10 + Rational(4, 3) * pi * 3 ** 3,
 "H2H-19": lambda: 7 * solve(Eq(7 * x - 4, 3 * x + 24), x)[0] - 4,
 "H2H-20": lambda: 2 * solve(Eq(f + 2 * f + (2 * f + 40), 620), f)[0] + 40,
 "H2H-21": lambda: 1150 * Rational(2, 25) * Rational(340, 100),
 "H2H-22": lambda: Rational(35, 10) * Rational(24, 10) * 6 * 60,
}

# The two questions whose answers are judgements about a model or about
# statistical inference rather than values or forms. There is nothing for sympy
# to compute in either; both were hand-checked and both are kept deliberately.
MANUAL = {
 "H2E-04": ("the meaning of a coefficient in a linear model. The key is right because 380 is "
            "the multiplier on m, so it is the cost added by each extra mile; the distractors "
            "misread it as the whole cost, as a count of miles, or as the constant term 1,450."),
 "H2H-13": ("a statistical-inference judgement with prose choices. The key is right because a "
            "random sample supports inference about the population it was drawn from — the 400 "
            "working places in that one mine — while the distractors either refuse any inference, "
            "over-reach to every mine in the district, or name a different population entirely."),
}

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
    # \frac must be flattened BEFORE the exponent rewrite when the fraction is
    # the exponent (a^{\frac{7}{12}}), and AFTER it when the exponent is inside
    # the fraction (\frac{4a^{3}}{b^{4}}); a non-recursive pattern never matches
    # nested braces either way. Alternating the two passes handles both.
    for _ in range(4):
        t = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"((\1)/(\2))", t)
        t = re.sub(r"\^\{([^{}]*)\}", r"**(\1)", t)
    t = t.replace("\\pi", "pi").replace("\\cdot", "*").replace("\\sqrt", "sqrt")
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
      f"({len(MANUAL)} in MANUAL: {', '.join(sorted(MANUAL))})")
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

    stem_txt = re.sub(r"<[^>]+>", " ", qq["stem"])
    if VISUAL.search(stem_txt):
        check("<table" in qq["stem"] or "<img" in qq["stem"],
              f"{tag}: refers to a visual it does not contain")
    if "system of" in stem_txt.lower():
        check("<br/>" in qq["stem"], f"{tag}: system of equations not stacked with <br/>")
    check(qq["stem"].count("<table") == qq["stem"].count("</table>"),
          f"{tag}: unbalanced table markup")

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


prod_path = os.path.join(HERE, "prod_math_stems.json")
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
    check(False, "prod_math_stems.json is missing — the dedupe pass cannot run")

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
# Two Test 18 items shipped that way and had to be reskinned; this is the check
# that would have caught them.
SETTING_KEYWORDS = {
 "M1": ["coal", "collier", "tub", "hewing", "cast iron", "casting", "mould", "coke",
        "foundry", "cupola", "pattern maker", "shield", "tunnel", "heading", "spoil",
        "crane", "jib", "quay", "dock", "scrap", "bale", "runner"],
 "M2E": ["gas works", "retort", "gas holder", "tram", "trolleybus", "depot", "fare",
         "conductor", "signal cabin", "lever", "wire-drawing", "coil", "die", "greas",
         "pumping engine", "gallon"],
 "M2H": ["telegraph", "cable", "repeater", "boiler", "rivet", "plate", "ventilation", "fan",
         "drift", "airway", "mine", "working place", "stay wire", "seam", "nautical"],
}


def module_text(mod):
    return " ".join(re.sub(r"<[^>]+>", " ", qq["stem"]).lower() for qq in mod)


TEXTS = {"M1": module_text(MODULE_1), "M2E": module_text(MODULE_2_EASY),
         "M2H": module_text(MODULE_2_HARD)}

for owner, words in SETTING_KEYWORDS.items():
    for word in words:
        check(word in TEXTS[owner], f"setting keyword {word!r} claimed by {owner} but unused there")
    for other in ("M1", "M2E", "M2H"):
        if other == owner:
            continue
        # only Module 1 against a Module 2 branch matters: the two branches are
        # never sat by the same student.
        if not ({owner, other} & {"M1"}):
            continue
        for word in words:
            check(word not in TEXTS[other],
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
