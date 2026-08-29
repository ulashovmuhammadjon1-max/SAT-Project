"""Verification for CALC 10.2 (Working with Geometric Series).

Every sum is recomputed with sp.summation, which handles the ratio test for
geometric series internally; the divergent cases are confirmed by showing the
terms do not approach 0 (or that the partial sums oscillate).

Run: python3 verify_c10_2.py
"""
import re

import sympy as sp

import c10_2

n = sp.Symbol("n", integer=True, nonnegative=True)
k = sp.Symbol("k", integer=True, positive=True)
x = sp.Symbol("x")
Q = c10_2.QUESTIONS


def key(i):
    item = Q[i - 1]
    return item["choices"][item["ans"]]


def expect(i, text):
    assert key(i) == text, f"q{i}: key is {key(i)!r}, expected {text!r}"


def numeric_value(s):
    """Numeric value of a choice, ignoring a leading 'converges to' if present."""
    s = re.sub(r"^(the series |the sum )?converges to ", "", s.strip())
    try:
        return sp.nsimplify(sp.sympify(s.replace("^", "**")))
    except (sp.SympifyError, TypeError, ValueError, SyntaxError, AttributeError):
        return None


for idx, item in enumerate(Q, 1):
    assert len(item["choices"]) == 4, f"q{idx}: needs exactly four choices"
    assert len(set(item["choices"])) == 4, f"q{idx}: repeated choice text"
    vals = [v for v in (numeric_value(c) for c in item["choices"]) if v is not None]
    assert len(vals) == len({sp.simplify(v) for v in vals}), (
        f"q{idx}: two numeric choices are equal as numbers")

# q1  Definition: |r| < 1.  Not a computation; the criterion is the standard one
#     and q10/q15/q24 exhibit the three failing cases r > 1, r = -1, r < -1.
expect(1, "|r| < 1")

assert sp.summation(sp.Rational(1, 3) ** n, (n, 0, sp.oo)) == sp.Rational(3, 2)
expect(2, "3/2")
assert sp.summation(sp.Rational(1, 3) ** n, (n, 1, sp.oo)) == sp.Rational(1, 2)
expect(3, "1/2")
assert sp.summation(sp.Rational(1, 3) ** n, (n, 2, sp.oo)) == sp.Rational(1, 6)
expect(4, "1/6")
assert sp.summation(5 * sp.Rational(2, 5) ** n, (n, 0, sp.oo)) == sp.Rational(25, 3)
expect(5, "25/3")
assert sp.summation(3 * sp.Rational(1, 4) ** (n - 1), (n, 1, sp.oo)) == 4
expect(6, "4")
assert sp.summation(sp.Rational(1, 2) ** n, (n, 3, sp.oo)) == sp.Rational(1, 4)
expect(7, "1/4")
assert sp.summation(sp.Rational(-1, 2) ** n, (n, 0, sp.oo)) == sp.Rational(2, 3)
expect(8, "2/3")
assert sp.summation(2 * sp.Rational(-1, 3) ** n, (n, 1, sp.oo)) == sp.Rational(-1, 2)
expect(9, "-1/2")

# q10  r = 3/2: the terms grow without bound, so the series diverges.
assert sp.limit(sp.Rational(3, 2) ** k, k, sp.oo) is sp.oo
expect(10, "diverges")

assert sp.summation(4 ** n / 5 ** (n + 1), (n, 0, sp.oo)) == 1
expect(11, "1")
assert sp.summation(2 ** (n + 1) / 3 ** n, (n, 1, sp.oo)) == 4
expect(12, "4")

# q13, q14  repeating decimals as geometric series
assert sp.summation(7 * sp.Rational(1, 10) ** n, (n, 1, sp.oo)) == sp.Rational(7, 9)
expect(13, "7/9")
assert sp.summation(36 * sp.Rational(1, 100) ** n, (n, 1, sp.oo)) == sp.Rational(4, 11)
expect(14, "4/11")

# q15  r = -1: partial sums alternate between 3 and 0, so there is no limit.
j = sp.Symbol("j", integer=True, nonnegative=True)
assert {sp.summation(3 * (-1) ** j, (j, 0, m)) for m in range(0, 8)} == {0, 3}
expect(15, "diverges")

assert sp.summation(sp.Rational(-1, 5) ** n, (n, 0, sp.oo)) == sp.Rational(5, 6)
expect(16, "5/6")
assert sp.summation(2 ** n / 7 ** (n - 1), (n, 1, sp.oo)) == sp.Rational(14, 5)
expect(17, "14/5")
assert sp.summation(3 * sp.Rational(1, 2) ** n, (n, 2, sp.oo)) == sp.Rational(3, 2)
expect(18, "3/2")

# q19, q20  solve for the parameter, then confirm |r| < 1 at the solution
sol19 = sp.solve(sp.Eq(1 / (1 - x / 3), 4), x)
assert sol19 == [sp.Rational(9, 4)] and abs(sp.Rational(9, 4) / 3) < 1
assert sp.summation((sp.Rational(9, 4) / 3) ** n, (n, 0, sp.oo)) == 4
expect(19, "9/4")
sol20 = sp.solve(sp.Eq(2 / (1 - x), 5), x)
assert sol20 == [sp.Rational(3, 5)]
assert sp.summation(2 * sp.Rational(3, 5) ** n, (n, 0, sp.oo)) == 5
expect(20, "3/5")

# q21  bouncing ball: the drop plus two of every rebound height
assert 10 + 2 * sp.summation(10 * sp.Rational(3, 5) ** k, (k, 1, sp.oo)) == 40
expect(21, "40 feet")

# q22, q23  irrational ratios, both of absolute value < 1
assert sp.N(sp.E / 3) < 1 and sp.N(sp.pi / 4) < 1
assert sp.simplify(sp.summation((sp.E / 3) ** n, (n, 0, sp.oo)) - 3 / (3 - sp.E)) == 0
expect(22, "3/(3 - e)")
assert sp.simplify(sp.summation((sp.pi / 4) ** n, (n, 1, sp.oo)) - sp.pi / (4 - sp.pi)) == 0
expect(23, "pi/(4 - pi)")

# q24  |r| = 5/4 > 1, so the terms are unbounded and the series diverges.
assert sp.limit(sp.Abs(3 * sp.Rational(-5, 4) ** k), k, sp.oo) is sp.oo
expect(24, "diverges")

assert sp.summation((2 ** k + 3 ** k) / 6 ** k, (k, 1, sp.oo)) == sp.Rational(3, 2)
expect(25, "3/2")

print("c10_2: all 25 keys verified")
