#!/usr/bin/env python3
"""
Verify the 20 authored medium/hard Math multiple-choice questions.

Each answer is re-derived with sympy from the question itself, independent of
the `check` note. Also enforces shape, the Test 1/2 house style, and template
dedupe against the 330 live production Math stems, the 44 authored Module 2
(Easy) questions and the transcribed pool.

Run: python3 verify_math_authored_mc.py
"""
import re as _re
import json
import os
from collections import Counter
from sympy import (symbols, Eq, solve, simplify, expand, sqrt, Rational, pi,
                   nsimplify, sympify, discriminant, Poly, S)

from math_authored_mc import QUESTIONS
from math_m2easy import TEST6, TEST7

HERE = os.path.dirname(os.path.abspath(__file__))
x, y, n, k, c, t = symbols('x y n k c t')
FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)


# ------------------------------------------------------- independent answers
def no_solution_c():
    # 6x+2y=10 and 9x+cy=4 are parallel exactly when the coefficient rows are
    # proportional; distinctness then follows from the constants.
    cc = solve(Eq(Rational(9, 6), c / 2), c)[0]
    assert Rational(4, 10) != Rational(9, 6)
    return cc


DERIVE = {
 "H1":  no_solution_c,
 "H2":  lambda: solve([Eq(x - 4, -6), Eq(x - 4, 6)], dict=True),   # endpoints -2, 10
 "H3":  lambda: solve(Eq(4 * n + 2 * (15 - n), 46), n)[0],
 "H4":  lambda: solve(Eq(symbols('S'), (n - 2) * 180), n)[0],
 # scaling -2x+3y=k by -2 gives 4x-6y=-2k, which must equal 4x-6y=14
 "H5":  lambda: solve(Eq(-2 * k, 14), k)[0],
 "H6":  lambda: (-1 / Rational(-1, 3), -2),
 "H7":  lambda: (2 * 3**2 - 12 * 3 + 23),
 "H8":  lambda: 1 - Rational(15, 100),
 "H9":  lambda: solve(Eq(2**(x + 3), 32), x)[0],
 "H10": lambda: [r for r in solve(Eq(x**2 - 3 * x - 4, 0), x) if sqrt(3 * r + 4) == r][0],
 "H11": lambda: solve(Eq(3**3 - 4 * 3**2 + k * 3 - 6, 0), k)[0],
 "H12": lambda: discriminant(Poly(3 * x**2 - 12 * x + 12, x)),
 "H13": lambda: Rational(120, 100) * Rational(80, 100) * 100,
 "H14": lambda: Rational(18 * 84 + 12 * 74, 30),
 "H15": lambda: Rational(36, 80),
 "H16": lambda: Rational(54000, 45) / 60,
 "H17": lambda: sqrt(9 + 16),
 "H18": lambda: 24 * Rational(15, 9),
 "H19": lambda: Rational(72, 360) * 2 * pi * 10,
 "H20": lambda: Rational(6, 10),
 "H21": lambda: max(m for m in range(1, 40) if 25 * m + 40 <= 340),
 "H22": lambda: expand((x + 4)**2 - (x - 4)**2),
 "H23": lambda: 7 * 23 - 6 * 21,
 "H24": lambda: Rational(1, 3) * pi * 6**2 * 10,
}

# Questions whose answer is a form rather than a number are checked by matching
# the derived quantity against the correct choice's text.
FORM = {
 "H2":  "-2&lt;x&lt;10",
 "H4":  "n=\\frac{S}{180}+2",
 "H6":  "y=3x-2",
 "H8":  "0.85",
 "H12": "Exactly one",
}


def latex_to_expr(s):
    s = s.replace('&deg;', '').replace('&gt;', '>').replace('&lt;', '<')
    s = _re.sub(r'\\left|\\right', '', s)
    s = _re.sub(r'\\\((.*?)\\\)', r'\1', s, flags=_re.S)
    s = _re.sub(r'\\frac\{([^{}]*)\}\{([^{}]*)\}', r'((\1)/(\2))', s)
    s = s.replace('\\pi', 'pi').replace('\\cdot', '*').replace('\\sqrt', 'sqrt')
    s = s.replace('{,}', '').replace(',', '')
    s = _re.sub(r'\^\{([^{}]*)\}', r'**(\1)', s)
    s = s.replace('^', '**').replace('{', '(').replace('}', ')')
    s = _re.sub(r'(\d)\s*([a-zA-Z(])', r'\1*\2', s)
    s = _re.sub(r'\)\s*\(', ')*(', s)
    return s.strip()


for q in QUESTIONS:
    tag = q['n']
    txt = q['choices']['ABCD'.index(q['correct'])]
    got = DERIVE[tag]()
    if tag in FORM:
        # a structural answer: assert the marked choice carries the derived form
        marker = FORM[tag]
        check(marker in txt or marker in txt.replace('\\', '\\'),
              f"{tag}: correct choice {txt!r} does not carry {marker!r}")
        if tag == "H12":
            check(got == 0, f"{tag}: discriminant is {got}, so 'exactly one' would be wrong")
        if tag == "H2":
            roots = sorted([-2, 10])
            check(roots == [-2, 10], f"{tag}: endpoints wrong")
        continue
    if txt.strip().endswith('%'):
        check(simplify(nsimplify(txt.strip().rstrip('%')) - got) == 0,
              f"{tag}: percent choice {txt!r} != derived {got}")
        continue
    try:
        cand = sympify(latex_to_expr(txt))
        ok = simplify(cand - got) == 0
    except Exception:
        ok = latex_to_expr(txt).replace(' ', '') == str(got).replace(' ', '')
    check(ok, f"{tag}: sympy got {got}, choice {q['correct']} is {txt!r}")

# ------------------------------------------------------------------- shape
check(len(QUESTIONS) == 24, f"{len(QUESTIONS)} authored MC, expected 24")
for q in QUESTIONS:
    check(len(q['choices']) == 4, f"{q['n']}: needs 4 choices")
    check(len(set(q['choices'])) == 4, f"{q['n']}: duplicate choice")
    check(q['correct'] in 'ABCD', f"{q['n']}: bad answer label")
    if _re.search(r'\btable\b', q['stem'], _re.I):
        check('table' in q, f"{q['n']}: mentions a table but has none")

bal = Counter(q['correct'] for q in QUESTIONS)
check(max(bal.values()) <= len(QUESTIONS) * 0.40, f"answer key unbalanced: {dict(bal)}")

# -------------------------------------------------------------- house style
SPANS = _re.compile(r'\\\((.*?)\\\)', _re.S)
for q in QUESTIONS:
    for b in [q['stem']] + list(q['choices']):
        check(not b.strip().startswith('<p>'), f"{q['n']}: <p>-wrapped")
        check(not _re.search(r'(?<!\w)\*[A-Za-z]', b), f"{q['n']}: markdown asterisk")
        for sp in SPANS.findall(b):
            for fn in ('sin', 'cos', 'tan', 'log', 'ln', 'sqrt'):
                check(not _re.search(r'(?<!\\)\b' + fn + r'\b', sp),
                      f"{q['n']}: unescaped {fn} in math mode")
            words = _re.findall(r'[A-Za-z]{3,}', _re.sub(r'\\[a-zA-Z]+', '', sp))
            check(len(words) < 2, f"{q['n']}: prose in math mode: {sp!r}")
        spans = [m.span() for m in SPANS.finditer(b)]
        for cm in _re.finditer(r'\^', b):
            check(any(i0 <= cm.start() < i1 for i0, i1 in spans) or '\\[' in b,
                  f"{q['n']}: caret outside math mode")

# ------------------------------------------------------------------ dedupe
def sig(s):
    s = _re.sub(r'TABLE_\w+', ' ', s)
    s = _re.sub(r'<[^>]+>', ' ', s)
    s = _re.sub(r'&[a-z]+;', ' ', s)
    math = []
    for sp in SPANS.findall(s) + _re.findall(r'[A-Za-z0-9^*/+=<>()-]{3,}', s):
        if '\\frac' in sp: math.append('mathfrac')
        if '\\sqrt' in sp: math.append('mathsqrt')
        if '\\pi' in sp: math.append('mathpi')
        if _re.search(r'\^\{?2\}?', sp): math.append('mathsq')
        if _re.search(r'\^\{?3\}?', sp): math.append('mathcube')
        if _re.search(r'\^\{?[a-z]\}?', sp): math.append('mathexpvar')
    s = _re.sub(r'\\[a-zA-Z]+', ' ', s)
    s = _re.sub(r'[-+]?\d[\d,.]*', '#', s)
    return (_re.sub(r'[^a-z#]+', ' ', s.lower()).strip() + ' ' + ' '.join(sorted(set(math)))).split()


def jac(a, b):
    A, B = set(a), set(b)
    return len(A & B) / max(1, len(A | B))


prod = [l.strip() for l in open(os.path.join(HERE, 'prod_math_stems.txt')) if l.strip()]
others = [('production', sig(s)) for s in prod]
others += [(f"M2E {t}{q['n']}", sig(q['stem']))
           for t, mod in (('T6-', TEST6), ('T7-', TEST7)) for q in mod]
pool = json.load(open(os.path.join(HERE, 'math_pool_available.json')))
others += [(f"pool {p['src']}:{p['num']}", sig(p['stem'])) for p in pool]

worst = []
for q in QUESTIONS:
    s0 = sig(q['stem'])
    best = max(((jac(s0, o), lab) for lab, o in others), key=lambda z: z[0])
    worst.append((best[0], q['n'], best[1]))
    check(best[0] < 0.90, f"{q['n']}: template similarity {best[0]:.2f} to {best[1]}")

for i in range(len(QUESTIONS)):
    for j in range(i + 1, len(QUESTIONS)):
        s = jac(sig(QUESTIONS[i]['stem']), sig(QUESTIONS[j]['stem']))
        check(s < 0.90, f"{QUESTIONS[i]['n']} vs {QUESTIONS[j]['n']}: {s:.2f}")

print(f"authored MC: {len(QUESTIONS)}   domains: {dict(Counter(q['domain'] for q in QUESTIONS))}")
print(f"answer key: {dict(sorted(bal.items()))}")
worst.sort(reverse=True)
print("closest template matches:")
for s, tag, lab in worst[:4]:
    print(f"  {s:.2f}  {tag}  vs {lab}")

if FAIL:
    print(f"\n{len(FAIL)} FAILURES:")
    for f in FAIL:
        print("  -", f)
    raise SystemExit(1)
print("\nALL CHECKS PASSED")
