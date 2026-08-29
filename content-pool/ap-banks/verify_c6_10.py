"""sympy verification for CALC 6.10 Integrating Functions Using Long Division
and Completing the Square.

Antiderivatives are checked by differentiation (two correct antiderivatives can
differ by a constant, so expressions are never compared directly), each long
division is confirmed with sp.div, each completed square is confirmed as an
identity, and the definite integrals are evaluated with sp.integrate.

CONCEPTUAL questions -- no computation, reasoning stated here:
  1  division is needed exactly when the numerator's degree is at least the
     denominator's
 24  x^2 - 5x + 6 factors, so it is a partial-fractions problem rather than a
     completing-the-square one (the factorization is still checked below)
"""
import sympy as sp

from c6_10 import QUESTIONS

x = sp.Symbol('x', real=True)

CONCEPTUAL = {1, 24}
checked = set()

SAMPLES = (sp.Rational(1, 5), sp.Rational(4, 5), sp.Rational(13, 10),
           sp.Rational(23, 10), sp.Rational(-7, 10))


def is_zero(e, var=x):
    if sp.simplify(e) == 0:
        return True
    vals = []
    for v in SAMPLES:
        try:
            val = complex(sp.N(e.subs(var, v)))
        except TypeError:
            continue
        if val != val:
            continue
        vals.append(abs(val))
    return bool(vals) and max(vals) < 1e-10


def anti(i, integrand, exprs):
    q = QUESTIONS[i - 1]
    assert len(exprs) == len(q["choices"]), f"q{i}: wrong number of expressions"
    key = exprs[q["ans"]]
    assert is_zero(sp.diff(key, x) - integrand), f"q{i}: key is not an antiderivative"
    for j, e in enumerate(exprs):
        if e is None or j == q["ans"]:
            continue
        assert not is_zero(sp.diff(e, x) - integrand), f"q{i}: distractor {j} also works"
    checked.add(i)


def value(i, computed, values):
    q = QUESTIONS[i - 1]
    for p in range(len(values)):
        for r in range(p + 1, len(values)):
            assert sp.simplify(values[p] - values[r]) != 0, f"q{i}: choices {p},{r} equal"
    assert sp.simplify(computed - values[q["ans"]]) == 0, f"q{i}: key mismatch"
    checked.add(i)


def divide(num, den):
    """(quotient, remainder) from sympy's polynomial division."""
    return sp.div(sp.Poly(num, x), sp.Poly(den, x))


L = lambda e: sp.log(sp.Abs(e))

# --- long division -------------------------------------------------------
q2, r2 = divide(x + 3, x)
assert q2.as_expr() == 1 and r2.as_expr() == 3
anti(2, (x + 3) / x, [x + 3 * L(x), 1 + 3 * L(x), L(x) + 3 * x, None])

q3, r3 = divide(2 * x + 1, x)
assert q3.as_expr() == 2 and r3.as_expr() == 1
anti(3, (2 * x + 1) / x, [2 * x + L(x), 2 + L(x), 2 * x + 1 / x, x**2 + L(x)])

q4, r4 = divide(x, x + 2)
assert q4.as_expr() == 1 and r4.as_expr() == -2
anti(4, x / (x + 2), [x - 2 * L(x + 2), x + 2 * L(x + 2), L(x + 2), None])

q5, r5 = divide(3 * x, x - 1)
assert q5.as_expr() == 3 and r5.as_expr() == 3
anti(5, 3 * x / (x - 1),
     [3 * x + 3 * L(x - 1), 3 * x - 3 * L(x - 1), 3 * L(x - 1),
      3 * x**2 / 2 + L(x - 1)])

q6, r6 = divide(4 * x + 5, x + 2)
assert q6.as_expr() == 4 and r6.as_expr() == -3
anti(6, (4 * x + 5) / (x + 2),
     [4 * x - 3 * L(x + 2), 4 * x + 3 * L(x + 2), 4 * x + 5 * L(x + 2),
      4 - 3 / (x + 2)**2])

q7, r7 = divide(x**2, x + 1)
assert q7.as_expr() == x - 1 and r7.as_expr() == 1
anti(7, x**2 / (x + 1),
     [x**2 / 2 - x + L(x + 1), x**2 / 2 + x + L(x + 1),
      x**2 / 2 - x - L(x + 1), None])

assert sp.simplify(sp.factor(x**2 - 4) - (x - 2) * (x + 2)) == 0
anti(8, x + 2, [x**2 / 2 + 2 * x, x**2 / 2 - 2 * x, L(x - 2), None])

q9, r9 = divide(x**2, x**2 + 1)
assert q9.as_expr() == 1 and r9.as_expr() == -1
anti(9, x**2 / (x**2 + 1),
     [x - sp.atan(x), x + sp.atan(x), sp.atan(x), None])

q10, r10 = divide(2 * x**2 + 3, x**2 + 1)
assert q10.as_expr() == 2 and r10.as_expr() == 1
anti(10, (2 * x**2 + 3) / (x**2 + 1),
     [2 * x + sp.atan(x), 2 * x - sp.atan(x), 2 * x + 3 * sp.atan(x),
      2 + sp.atan(x)])

# 11: the quotient itself
assert sp.simplify(sp.cancel((x**2 + 3 * x + 2) / (x + 1)) - (x + 2)) == 0
value(11, x + 2, [x + 2, x + 3, x**2 + 2, x - 2])

# --- completing the square -----------------------------------------------
assert sp.expand((x + 3)**2 + 4 - (x**2 + 6 * x + 13)) == 0
value(12, (x + 3)**2 + 4,
      [(x + 3)**2 + 4, (x + 3)**2 + 13, (x + 6)**2 - 23, (x - 3)**2 + 4])

assert sp.expand((x + 2)**2 + 1 - (x**2 + 4 * x + 5)) == 0
anti(13, 1 / (x**2 + 4 * x + 5),
     [sp.atan(x + 2), sp.atan(x + 4), sp.log(sp.Abs(x**2 + 4 * x + 5)),
      sp.atan((x + 2) / 2) / 2])

assert sp.expand((x - 3)**2 + 4 - (x**2 - 6 * x + 13)) == 0
anti(14, 1 / (x**2 - 6 * x + 13),
     [sp.atan((x - 3) / 2) / 2, sp.atan(x - 3), 2 * sp.atan((x - 3) / 2),
      sp.log(sp.Abs(x**2 - 6 * x + 13)) / 2])

assert sp.expand((x + 1)**2 + 4 - (x**2 + 2 * x + 5)) == 0
anti(15, 1 / (x**2 + 2 * x + 5),
     [sp.atan((x + 1) / 2) / 2, sp.atan(x + 1), sp.atan(x + 1) / 2,
      sp.atan((x + 1) / 2) / 4])

assert sp.expand((x - 1)**2 + 9 - (x**2 - 2 * x + 10)) == 0
anti(16, 1 / (x**2 - 2 * x + 10),
     [sp.atan((x - 1) / 3) / 3, sp.atan((x - 1) / 9) / 3,
      3 * sp.atan((x - 1) / 3), sp.atan((x - 1) / 3)])

assert sp.expand(9 - (x - 1)**2 - (8 + 2 * x - x**2)) == 0
anti(17, 1 / sp.sqrt(8 + 2 * x - x**2),
     [sp.asin((x - 1) / 3), sp.asin((x + 1) / 3), sp.asin((x - 1) / 3) / 3,
      sp.atan((x - 1) / 3)])

# --- definite integrals ---------------------------------------------------
value(18, sp.integrate((x + 1) / x, (x, 1, 2)),
      [1 + sp.log(2), sp.log(2), 1 + 2 * sp.log(2), sp.Rational(3, 2)])
value(19, sp.simplify(sp.integrate(1 / (x**2 + 2 * x + 2), (x, 0, 1))),
      [sp.atan(2) - sp.pi / 4, sp.atan(2), sp.pi / 4, sp.log(5) / 2])
value(20, sp.simplify(sp.integrate(x / (x + 2), (x, 0, 2))),
      [2 - 2 * sp.log(2), 2 + 2 * sp.log(2), 2 * sp.log(2), sp.Rational(1, 2)])

# --- the two harder mixed ones -------------------------------------------
anti(21, (x + 3) / (x**2 + 2 * x + 5),
     [sp.log(x**2 + 2 * x + 5) / 2 + sp.atan((x + 1) / 2),
      sp.log(x**2 + 2 * x + 5) / 2,
      sp.log(x**2 + 2 * x + 5) + sp.atan((x + 1) / 2),
      sp.log(x**2 + 2 * x + 5) / 2 + sp.atan((x + 1) / 2) / 2])

q22, r22 = divide(x**2 + 2 * x, x + 1)
assert q22.as_expr() == x + 1 and r22.as_expr() == -1
anti(22, (x**2 + 2 * x) / (x + 1),
     [x**2 / 2 + x - L(x + 1), x**2 / 2 + x + L(x + 1),
      x**2 / 2 + 2 * x - L(x + 1), x + 1 - L(x + 1)])

anti(23, (x**3 + 2) / x**2,
     [x**2 / 2 - 2 / x, x**2 / 2 + 2 / x, x**2 / 2 - 2 * L(x), None])

q25, r25 = divide(x**2 + 1, x - 1)
assert q25.as_expr() == x + 1 and r25.as_expr() == 2
anti(25, (x**2 + 1) / (x - 1),
     [x**2 / 2 + x + 2 * L(x - 1), x**2 / 2 + x - 2 * L(x - 1),
      x**2 / 2 - x + 2 * L(x - 1), x**2 / 2 + x + L(x - 1)])

# 24: the denominator really does factor over the reals
assert sp.factor(x**2 - 5 * x + 6) == (x - 2) * (x - 3)

assert checked | CONCEPTUAL == set(range(1, 26)), sorted(set(range(1, 26)) - (checked | CONCEPTUAL))
assert not (checked & CONCEPTUAL)
assert len(QUESTIONS) == 25
for k, q in enumerate(QUESTIONS, 1):
    assert len(q["choices"]) == 4 and len(set(q["choices"])) == 4, f"q{k}: choices"
    assert 0 <= q["ans"] < 4, f"q{k}: ans"
print(f"c6_10: {len(checked)} computational questions verified, "
      f"{len(CONCEPTUAL)} conceptual; all 25 checked for shape.")
