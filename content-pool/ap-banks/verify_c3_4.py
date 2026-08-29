"""sympy verification for CALC 3.4.

Choices are transcribed as sympy expressions in module order and compared
against sp.diff. The pairwise non-equivalence check runs on the difference
simplified over 0 < x < 1, where all the radicals involved are real, because
several natural distractors here are algebraically equal to the key when they
are written differently.

Conceptual questions (17, 18, 19): arcsin + arccos is constant (checked), the
vertical tangent at x = 1 (checked as an infinite one-sided limit), and the
identity behind the implicit derivation (checked).
"""
import importlib
import sympy as sp

M = importlib.import_module("c3_4")
x = sp.Symbol("x", positive=True)

CONCEPTUAL = {17, 18, 19}
checked = set()
R = sp.Rational
asin, acos, atan, acot, asec = sp.asin, sp.acos, sp.atan, sp.acot, sp.asec
sqrt, exp = sp.sqrt, sp.exp


def check(n, exprs, true_val):
    item = M.QUESTIONS[n - 1]
    assert len(exprs) == 4 == len(item["choices"]), f"q{n}: expected 4 choices"
    diff = sp.simplify(exprs[item["ans"]] - true_val)
    assert diff == 0, f"q{n}: keyed choice {item['ans']} != computed ({diff})"
    for i in range(4):
        for j in range(i + 1, 4):
            d = sp.sympify(exprs[i] - exprs[j])
            # Compare as functions on (0, 1/4), where every radical here is real.
            num = [sp.N(d.subs(x, sp.Rational(k, 40))) for k in (1, 3, 7, 9)]
            same = all(abs(v) < 1e-9 for v in num) and sp.simplify(d) == 0
            assert not same, f"q{n}: choices {i} and {j} are the same function"
    checked.add(n)


def d(f):
    return sp.diff(f, x)


check(1, [1 / sqrt(1 - x**2), -1 / sqrt(1 - x**2), 1 / (1 + x**2), 1 / sqrt(x**2 - 1)],
      d(asin(x)))
check(2, [-1 / sqrt(1 - x**2), 1 / sqrt(1 - x**2), -1 / (1 + x**2), -1 / sqrt(x**2 - 1)],
      d(acos(x)))
check(3, [1 / (1 + x**2), -1 / (1 + x**2), 1 / sqrt(1 - x**2), 1 / (1 - x**2)],
      d(atan(x)))
check(4, [-1 / (1 + x**2), 1 / (1 + x**2), -1 / sqrt(1 - x**2), -1 / (1 - x**2)],
      d(acot(x)))
check(5, [2 / sqrt(1 - 4 * x**2), 1 / sqrt(1 - 4 * x**2), 2 / sqrt(1 - x**2),
          -2 / sqrt(1 - 4 * x**2)], d(asin(2 * x)))
check(6, [3 / (1 + 9 * x**2), 1 / (1 + 9 * x**2), 3 / (1 + 3 * x**2), 3 / (1 + x**2)],
      d(atan(3 * x)))
check(7, [2 * x / sqrt(1 - x**4), 1 / sqrt(1 - x**4), 2 * x / sqrt(1 - x**2),
          -2 * x / sqrt(1 - x**4)], d(asin(x**2)))
check(8, [2 * x / (1 + x**4), 1 / (1 + x**4), 2 * x / (1 + x**2),
          2 * x / (1 + x**4) ** 2], d(atan(x**2)))
check(9, [-2 / sqrt(1 - 4 * x**2), 2 / sqrt(1 - 4 * x**2), -1 / sqrt(1 - 4 * x**2),
          -2 / sqrt(1 - x**2)], d(acos(2 * x)))
check(10, [atan(x) + x / (1 + x**2), atan(x) + 1 / (1 + x**2), x / (1 + x**2),
           1 / (1 + x**2)], d(x * atan(x)))
check(11, [exp(atan(x)) / (1 + x**2), exp(atan(x)), exp(1 / (1 + x**2)),
           exp(atan(x)) / (1 + x**2) ** 2], d(exp(atan(x))))
check(12, [sqrt(3) / 2, R(2, 3), 2 * sqrt(3) / 3, R(4, 3)], d(asin(x)).subs(x, R(1, 2)))
check(13, [R(1, 4), R(1, 2), 1, 2], d(atan(x)).subs(x, 1))
check(14, [-1, R(-1, 2), 0, 1], d(acos(x)).subs(x, 0))
check(15, [1 / sqrt(9 - x**2), 3 / sqrt(9 - x**2), 1 / (3 * sqrt(9 - x**2)),
           1 / sqrt(1 - x**2)], d(asin(x / 3)))
check(16, [2 / (4 + x**2), 1 / (4 + x**2), 1 / (2 * (1 + x**2)), 2 / (1 + x**2)],
      d(atan(x / 2)))
check(20, [1 / (2 * sqrt(x - x**2)), 1 / sqrt(1 - x), 1 / (2 * sqrt(x)),
           1 / (2 * sqrt(1 - x**2))], d(asin(sqrt(x))))
check(21, [exp(x) / (1 + exp(2 * x)), exp(x) / (1 + exp(x)), 1 / (1 + exp(2 * x)),
           exp(x) / (1 + exp(x)) ** 2], d(atan(exp(x))))
check(22, [2 * atan(x) / (1 + x**2), 2 * atan(x), 2 / (1 + x**2),
           atan(x) ** 2 / (1 + x**2)], d(atan(x) ** 2))
check(24, [0, 2 / sqrt(1 - x**2), 1, 2 * asin(x)], d(asin(x) + acos(x)))
check(25, [1 / (4 * sqrt(3)), 1 / (2 * sqrt(3)), 1 / sqrt(3), 2 / sqrt(3)],
      sp.simplify(d(asec(x)).subs(x, 2)))

# q23: the tangent line to y = arctan(x) at x = 1.
t23 = d(atan(x)).subs(x, 1) * (x - 1) + atan(sp.Integer(1))
check(23, [(x - 1) / 2 + sp.pi / 4, 2 * (x - 1) + sp.pi / 4,
           (x - 1) / 2 + sp.pi / 2, x / 2 + sp.pi / 4], sp.expand(t23))

# q17: arcsin(x) + arccos(x) really is the constant pi/2. sympy will not
# collapse the sum symbolically, so the constancy is shown by the vanishing
# derivative and the value checked at several points of the domain.
assert sp.simplify(sp.diff(asin(x) + acos(x), x)) == 0
for v in (-sp.Rational(9, 10), -sp.Rational(1, 3), 0, sp.Rational(1, 2), sp.Rational(9, 10)):
    assert abs((asin(v) + acos(v) - sp.pi / 2).evalf()) < 1e-30, f"q17 at x = {v}"

# q18: the one-sided slope blows up at x = 1, so the tangent is vertical.
# The limit is taken over a plain real symbol: with x declared positive sympy
# reads the "-" direction in the complex plane and reports the wrong sign.
t = sp.Symbol("t", real=True)
assert sp.limit(sp.diff(asin(t), t), t, 1, "-") == sp.oo
assert sp.limit(sp.diff(asin(t), t), t, -1, "+") == sp.oo
assert sp.sqrt(1 - sp.Integer(1) ** 2) == 0

# q19: the identity cos(arcsin(x)) = sqrt(1 - x^2) on the range of arcsin.
assert sp.simplify(sp.cos(asin(x)) - sqrt(1 - x**2)) == 0

assert len(M.QUESTIONS) == 25, f"expected 25 questions, found {len(M.QUESTIONS)}"
assert checked | CONCEPTUAL == set(range(1, 26)), \
    f"unaccounted questions: {set(range(1, 26)) - checked - CONCEPTUAL}"
assert not (checked & CONCEPTUAL)
for i, item in enumerate(M.QUESTIONS, 1):
    assert len(item["choices"]) == 4 == len(set(item["choices"])), f"q{i}: choices"
print(f"c3_4: {len(checked)} verified with sympy, {len(CONCEPTUAL)} conceptual, 25 total")
