#!/usr/bin/env python3
"""
Verify the 66 originally-authored Math questions for Test 18.

Four passes, because each has caught a different class of defect in earlier
builds:

 1. Every answer is re-derived with sympy from the question itself, never read
    off the `check` note. A wrong `check` and a wrong key agree with each
    other; only an independent derivation catches that. The two questions whose
    answers are English judgements rather than values sit in MANUAL, each with
    a written justification.
 2. House style is enforced on the final HTML — the Test 1/2 rules in
    CLAUDE.md, plus the DB-wide rendering checks (no bare `^`, `sqrt(`,
    `*`-as-multiply, slash fractions, ASCII comparison operators or LaTeX
    macros outside a math span).
 3. Template dedupe against every Math stem live in production, not just exact
    duplicates: a question that reuses a template with new numbers is a repeat.
    Anything scoring 0.75 or above on the token Jaccard is a failure.
 4. Self-collision: the same Jaccard check among Test 18's own 66 stems.

Run:  python3 verify_math_test18.py
      (no DATABASE_URL needed — pass 3 reads the local prod_math_stems.json
      snapshot of the 990 Math stems live in production)
"""
import json
import os
import re
import sys
from collections import Counter

from sympy import (Eq, Rational, ceiling, floor, cancel, diff, expand, latex,
                   log, pi, simplify, sin, cos, solve, sqrt, symbols, sympify, tan)

from math_test18 import MODULE_1, MODULE_2_EASY, MODULE_2_HARD, ALL

HERE = os.path.dirname(os.path.abspath(__file__))

# Symbols. Never name one S, E, I, N, O, Q, beta, gamma or zeta and then hand
# it to sympify bare: sympify("S") returns the SingletonRegistry and the
# comparison silently degrades to a string compare. Everything below is either
# built with symbols() explicitly or parsed with an all-letters locals map.
x, y, w, t, h, d, m, n, c, k = symbols("x y w t h d m n c k")
a, b, g, r, s, u, v, p, q = symbols("a b g r s u v p q")
A_ = symbols("A")
N_ = symbols("N")
T_ = symbols("T")
XP, YP = symbols("x y", positive=True)

# Every single letter maps to a plain Symbol, so a choice such as
# \(\frac{3A}{2N}\) cannot pick up sympy's own N (numerical evaluation) or S.
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
    sol = solve([Eq(8 * s + 3 * h, 131), Eq(5 * s + 6 * h, 152)], [s, h])
    return 6 * sol[s] + 2 * sol[h]


def h1_04():
    shifts = solve(Eq(340 + 25 * s, 460 + 15 * s), s)[0]
    return 340 + 25 * shifts


def h1_05():
    hours = solve(Eq(1250 + 340 * h, 12450), h)[0]
    return ceiling(hours / 9)


def h1_06():
    per = solve(Eq(560 - 12 * r, 344), r)[0]
    return 560 - 20 * per


def h1_07():
    sol = solve([Eq(g + b, 34), Eq(8 * g + 14 * b, 386)], [g, b])
    return sol[b]


def h1_11():
    const = solve(Eq(500, k / Rational(12, 10) ** 2), k)[0]
    return const / 2 ** 2


def h1_13():
    width = [z for z in solve(Eq(w * (3 * w + 4), 644), w) if z > 0][0]
    return 3 * width + 4


def h1_16():
    rows = [("Aldergate", 120, 90000), ("Chalk Down", 150, 108000),
            ("Barrow Fen", 180, 148500), ("Denhill", 200, 156000)]
    return max(rows, key=lambda row: Rational(row[2], row[1]))[0]


def h2e_17():
    rows = [("Thursday", 14), ("Friday", 11), ("Saturday", 23), ("Sunday", 19)]
    return max(rows, key=lambda row: row[1])[0]


def h2e_05():
    bound = solve(Eq(78 + a, 130), a)[0]
    return "\\(a\\le " + latex(bound) + "\\)"


def h2h_03():
    lo = solve(Eq(4 - 3 * x, 13), x)[0]
    hi = solve(Eq(4 - 3 * x, -7), x)[0]
    return "\\(" + latex(lo) + "\\le x<" + latex(hi) + "\\)"


def h2h_02():
    # slope read off 5x+2y=9, then the point (-2,13) fixes the intercept
    slope = solve(Eq(5 * x + 2 * y, 9), y)[0].coeff(x)
    inter = solve(Eq(13, slope * (-2) + b), b)[0]
    return slope * 6 + inter


def h2h_05():
    rate, fee = symbols("rate fee")
    sol = solve([Eq(fee + 140 * rate, 1930), Eq(fee + 260 * rate, 3250)], [fee, rate])
    return sol[fee] + 400 * sol[rate]


def h2h_13():
    vertex = solve(diff(a * (x - 8) * (x - 20), x), x)[0]
    return solve(Eq(a * (vertex - 8) * (vertex - 20), 12), a)[0]


def h2h_14():
    newt = symbols("newt")
    return solve(Eq(12 * 18 - 16 + newt, 12 * Rational(37, 2)), newt)[0]


def h2h_15():
    cast = [(2018, 120), (2019, 138), (2020, 156), (2021, 195), (2022, 234)]
    growth = [(yr, Rational(cnt - prev, prev))
              for (_, prev), (yr, cnt) in zip(cast, cast[1:])]
    return str(max(growth, key=lambda row: row[1])[0])


def h2h_19():
    xv = solve(Eq(3 * x + 10, 5 * x - 30), x)[0]
    return 180 - (3 * xv + 10)


def h2h_20():
    hc = solve(diff(x ** 2 - 10 * x, x), x)[0]
    kc = solve(diff(y ** 2 + 6 * y, y), y)[0]
    return sqrt(2 + hc ** 2 + kc ** 2)


def h2h_21():
    sin_r = Rational(5, 13)
    return simplify(sin_r / sqrt(1 - sin_r ** 2))


DERIVE = {
 "H1-01": h1_01,
 "H1-02": lambda: solve(Eq(96 - Rational(96 - 51, 3) * t, 21), t)[0],
 "H1-03": lambda: max(i for i in range(200) if 195 + 2 * 74 + 18 * i <= 480),
 "H1-04": h1_04,
 "H1-05": h1_05,
 "H1-06": h1_06,
 "H1-07": h1_07,
 "H1-08": lambda: expand((2 * w + 5) * (w - 3) - (w ** 2 - 4 * w)),
 "H1-09": lambda: solve(Eq(288 / (h + 4), 18), h)[0],
 "H1-10": lambda: simplify(3 * log(Rational(1600, 100), 2)),
 "H1-11": h1_11,
 "H1-12": lambda: solve(Eq(N_, 3 * A_ / (2 * t)), t)[0],
 "H1-13": h1_13,
 "H1-14": lambda: floor(Rational(3300, 11) * 7 / 15),
 "H1-15": lambda: 4800 * Rational(75, 100) * Rational(112, 100),
 "H1-16": h1_16,
 "H1-17": lambda: Rational(84 * 100, 84 + 56 + 60),
 "H1-18": lambda: 9 * 284 - 8 * 246,
 "H1-19": lambda: (lambda xv: xv + 8)(
     solve(Eq(3 * x + (x + 8) + (2 * x - 5), 63), x)[0]),
 "H1-20": lambda: 45 - simplify(14 / cos(pi / 3)),
 "H1-21": lambda: Rational(12, 10) * Rational(8, 10) * Rational(5, 10) * 2700,
 "H1-22": lambda: Rational(2 ** 2 * 5, 5 ** 2),

 "H2E-01": lambda: Rational(153, 9),
 "H2E-02": lambda: solve(Eq(340 + x, 425), x)[0],
 "H2E-03": lambda: 15 + 4 * w,
 "H2E-05": h2e_05,
 "H2E-06": lambda: solve(Eq(90 - 7 * d, 34), d)[0],
 "H2E-07": lambda: 84 + 6 * 5,
 "H2E-08": lambda: expand(3 * (2 * q - 7)),
 "H2E-09": lambda: expand(x ** 2 - 49),
 "H2E-10": lambda: 5 * 6 ** 2 + 40,
 "H2E-11": lambda: solve(Eq(sqrt(n + 7), 5), n)[0],
 "H2E-12": lambda: 81 * Rational(1, 3) ** 2,
 "H2E-13": lambda: expand((2 * x ** 3) ** 4),
 "H2E-14": lambda: 40 * Rational(135, 100),
 "H2E-15": lambda: Rational(12, 100) * 250,
 "H2E-16": lambda: 52 - 38,
 "H2E-17": h2e_17,
 "H2E-18": lambda: Rational(82 + 95 + 74 + 110 + 88 + 91, 6),
 "H2E-19": lambda: 90 - 34,
 "H2E-20": lambda: 2 * (8 * 5) + 2 * (8 * 3) + 2 * (5 * 3),
 "H2E-21": lambda: solve(Eq(4 * v, 48), v)[0] ** 2,
 "H2E-22": lambda: simplify(18 * sin(pi / 6)),

 "H2H-01": lambda: solve(Eq(4 * 9 - (-6) * k, 0), k)[0],
 "H2H-02": h2h_02,
 "H2H-03": h2h_03,
 "H2H-04": lambda: solve(Eq(Rational(12, 100) * 60,
                            Rational(9, 100) * (60 + x)), x)[0],
 "H2H-05": h2h_05,
 "H2H-06": lambda: solve(Eq(c * m + 3 * c * n, T_), c)[0],
 "H2H-07": lambda: solve(Eq(Rational(62, 100) * m, 3410), m)[0],
 "H2H-08": lambda: expand(3 * (x ** 2 + 1) - 4),
 "H2H-09": lambda: cancel((x ** 2 - x - 12) / (x ** 2 - 16)),
 "H2H-10": lambda: solve(Eq(24 ** 2 - 4 * k * 16, 0), k)[0],
 "H2H-11": lambda: solve(Eq(9 ** (2 * x - 1), 27 ** (x + 3)), x)[0],
 "H2H-12": lambda: simplify((16 * XP ** 8 / YP ** 4) ** Rational(3, 4)),
 "H2H-13": h2h_13,
 "H2H-14": h2h_14,
 "H2H-15": h2h_15,
 "H2H-17": lambda: Rational(35, 10) * Rational(32, 20) * 15 * 60,
 "H2H-18": lambda: Rational(456 * 7, 12),
 "H2H-19": h2h_19,
 "H2H-20": h2h_20,
 "H2H-21": h2h_21,
 "H2H-22": lambda: 400 * Rational(3, 2) ** 2 * Rational(4, 5),
}

# The only two answers that are an English judgement rather than a value or a
# form sympy can compare against. Both are checked by hand and the reason each
# resists a symbolic derivation is recorded here.
MANUAL = {
 "H2E-04": ("The answer is the meaning of the coefficient 0.60 in C(m)=38+0.60m, "
            "so all four choices are English sentences. Verified by hand: 0.60 "
            "multiplies m, so it is the charge added by each further airborne "
            "minute; choice D says exactly that and no other choice does."),
 "H2H-16": ("The answer is which inference a margin of error licenses, so all four "
            "choices are English sentences. Verified by hand: 412 plus or minus 9 "
            "is a plausible range for the MEAN of the sampled population (the 1,500 "
            "blocks cut that month), which is choice A; B misreads it as a range "
            "for individual blocks, C drops the uncertainty, D extends it past the "
            "population that was actually sampled."),
}


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


def matches(text, got):
    for expr in as_expr(text):
        try:
            if simplify(expr - got) == 0:
                return True
        except Exception:
            pass
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
                ok = ok or simplify(sympify(latex_to_expr(ans), locals=BASE_LOCALS) - got) == 0
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
        bad = False
        for expr in as_expr(alt):
            try:
                bad = bad or simplify(expr - got) == 0
            except Exception:
                pass
        check(not bad, f"{tag}: distractor {'ABCD'[i]} ({alt!r}) equals the key")

print(f"   {derived} of {len(ALL)} re-derived with sympy; "
      f"{len(MANUAL)} in MANUAL ({', '.join(sorted(MANUAL))})")

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

check(sum(1 for qq in ALL if qq["skill"] == "GT-TR") >= 2,
      "the package needs at least one GT-TR question in the mix")

VALID_SKILLS = {
    "ALG": {"ALG-LE", "ALG-LF", "ALG-LI"},
    "ADV": {"ADV-NF", "ADV-EQ", "ADV-NE"},
    "PSDA": {"PSDA-RP", "PSDA-ST", "PSDA-DI"},
    "GT": {"GT-AV", "GT-LA", "GT-TR"},
}

SPAN = re.compile(r"\\\((.*?)\\\)|\\\[(.*?)\\\]", re.S)

seen_ids = set()
styled = 0
for q in ALL:
    tag = q["n"]
    check(tag not in seen_ids, f"{tag}: duplicate question id")
    seen_ids.add(tag)
    check(q["skill"] in VALID_SKILLS[q["domain"]],
          f"{tag}: skill {q['skill']} is not a {q['domain']} skill")
    check(bool(q.get("check")), f"{tag}: no check note")

    blocks = [q["stem"]] + list(q.get("choices") or [])
    styled += 1
    if q["type"] == "MC":
        check(len(q["choices"]) == 4, f"{tag}: needs exactly 4 choices")
        check(len(set(q["choices"])) == 4, f"{tag}: duplicate answer choice")
        check(q["correct"] in "ABCD", f"{tag}: bad answer label")
    else:
        check(bool(q.get("answers")), f"{tag}: free response with no accepted answer")

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
        for mm in re.finditer(r"\\(pi|frac|sqrt|cdot|le|ge|ne|circ|sin|cos|tan|log|ln)\b", bare):
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

    if re.search(r"\btables?\b", q["stem"], re.I):
        check("<table" in q["stem"], f"{tag}: mentions a table but has no <table> markup")
    if re.search(r"\b(shown|the figure|following (?:graph|figure|chart|table|plot)|"
                 r"graph above|chart|plot)\b", q["stem"], re.I):
        check("<table" in q["stem"] or "<img" in q["stem"],
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


prod_path = os.path.join(HERE, "prod_math_stems.json")
worst_prod = 0.0
if os.path.exists(prod_path):
    prod = json.load(open(prod_path))
    print(f"   comparing against {len(prod)} live Math stems")
    others = [(pq["label"], sig(re.sub(r"<img[^>]*>", " ", pq["stem"]))) for pq in prod]
    worst = []
    for q in ALL:
        s0 = sig(q["stem"])
        score, label = max(((jaccard(s0, o), lab) for lab, o in others), key=lambda z: z[0])
        worst.append((score, q["n"], label))
        check(score < 0.75, f"{q['n']}: template similarity {score:.2f} to {label}")
    worst.sort(reverse=True)
    worst_prod = worst[0][0]
    print("   closest matches:")
    for sc, tag, lab in worst[:8]:
        print(f"     {sc:.2f}  {tag}  vs {lab}")
else:
    check(False, "prod_math_stems.json is missing — the dedupe pass cannot run")

# ------------------------------------------------------------ self-collision
print("== pass 4: self-collision among Test 18's own 66 stems")
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

# ------------------------------------------------------------------- report
print()
print(f"questions: {len(ALL)}   M1 domains: {dict(Counter(qq['domain'] for qq in MODULE_1))}")
print(f"                    M2E domains: {dict(Counter(qq['domain'] for qq in MODULE_2_EASY))}")
print(f"                    M2H domains: {dict(Counter(qq['domain'] for qq in MODULE_2_HARD))}")
print(f"skills: {dict(sorted(Counter(qq['skill'] for qq in ALL).items()))}")
print(f"answer key M1:  {dict(sorted(Counter(qq['correct'] for qq in MODULE_1 if qq['type']=='MC').items()))}")
print(f"answer key M2E: {dict(sorted(Counter(qq['correct'] for qq in MODULE_2_EASY if qq['type']=='MC').items()))}")
print(f"answer key M2H: {dict(sorted(Counter(qq['correct'] for qq in MODULE_2_HARD if qq['type']=='MC').items()))}")
print(f"highest Jaccard vs production: {worst_prod:.2f}   within Test 18: {worst_self:.2f}")

if FAIL:
    print(f"\n{len(FAIL)} FAILURES:")
    for f in FAIL:
        print("  -", f)
    raise SystemExit(1)
print("\nALL CHECKS PASSED")
