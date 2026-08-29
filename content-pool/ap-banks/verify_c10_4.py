"""Verification for CALC 10.4 (Integral Test for Convergence).

Every convergence claim here is decided by actually evaluating the improper
integral with sp.integrate, and every "the hypotheses fail" claim is decided by
examining the sign of f' with sympy rather than by assertion.

Run: python3 verify_c10_4.py
"""
import re

import sympy as sp

import c10_4

x = sp.Symbol("x", positive=True)
n = sp.Symbol("n", integer=True, positive=True)
Q = c10_4.QUESTIONS


def key(i):
    item = Q[i - 1]
    return item["choices"][item["ans"]]


def expect(i, text):
    assert key(i) == text, f"q{i}: key is {key(i)!r}, expected {text!r}"


def numeric_value(s):
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

# q1  The three hypotheses.  Not computational; q20 exhibits a positive
#     continuous term sequence for which the decreasing hypothesis fails.
expect(1, "positive, continuous, and decreasing on [k, infinity)")

# q2  (-1)^n/n takes negative values, so positivity fails.
assert (-1) ** 1 / sp.Integer(1) < 0
expect(2, "sum from n=1 to infinity of (-1)^n/n")

I1 = sp.integrate(1 / x ** 2, (x, 1, sp.oo))
assert I1 == 1
expect(3, "converges")

# q4  The integral is 1 but the sum is pi^2/6 -- they are different numbers.
assert sp.summation(1 / n ** 2, (n, 1, sp.oo)) == sp.pi ** 2 / 6
assert sp.pi ** 2 / 6 != 1 and sp.N(sp.pi ** 2 / 6) > 1
expect(4, "converges, but the integral's value is not the sum")

assert sp.integrate(1 / (x * sp.log(x)), (x, 2, sp.oo)) is sp.oo
expect(5, "diverges, because int from 2 to infinity of dx/(x*ln(x)) diverges")
assert sp.integrate(1 / (x * sp.log(x) ** 2), (x, 2, sp.oo)) == 1 / sp.log(2)
expect(6, "converges")
assert sp.integrate(x * sp.exp(-x ** 2), (x, 1, sp.oo)) == 1 / (2 * sp.E)
expect(7, "converges")
assert sp.integrate(1 / (x ** 2 + 1), (x, 1, sp.oo)) == sp.pi / 4
expect(8, "pi/4")
assert sp.integrate(x / (x ** 2 + 1), (x, 1, sp.oo)) is sp.oo
expect(9, "diverges, since int from 1 to infinity of x/(x^2 + 1) dx diverges")
assert sp.integrate(x ** sp.Rational(-1, 2), (x, 1, sp.oo)) is sp.oo
expect(10, "diverges, since int from 1 to infinity of x^(-1/2) dx diverges")
assert sp.integrate(sp.log(x) / x, (x, 2, sp.oo)) is sp.oo
expect(11, "diverges")

# q12  f(x) = x/(x^2+1): f' = (1 - x^2)/(x^2+1)^2, negative exactly for x > 1.
f12 = x / (x ** 2 + 1)
d12 = sp.simplify(sp.diff(f12, x))
assert sp.simplify(d12 - (1 - x ** 2) / (x ** 2 + 1) ** 2) == 0
assert d12.subs(x, sp.Rational(1, 2)) > 0 and d12.subs(x, 2) < 0 and d12.subs(x, 1) == 0
expect(12, "x >= 1")

# q13  f(x) = ln(x)/x: f' = (1 - ln x)/x^2 < 0 for x > e; smallest integer is 3.
d13 = sp.simplify(sp.diff(sp.log(x) / x, x))
assert sp.simplify(d13 - (1 - sp.log(x)) / x ** 2) == 0
assert d13.subs(x, 2) > 0 and d13.subs(x, 3) < 0
assert sp.ceiling(sp.E) == 3
expect(13, "3")

# q14, q15  remainder bounds
assert sp.integrate(1 / x ** 2, (x, 10, sp.oo)) == sp.Rational(1, 10)
expect(14, "1/10")
assert sp.integrate(x ** -3, (x, 5, sp.oo)) == sp.Rational(1, 50)
expect(15, "1/50")

# q16  For a decreasing positive f the remainder satisfies
#      int_(n+1)^oo f <= R_n <= int_n^oo f, which is choice B.
#      Sanity check with f = 1/x^2 at n = 10: 1/11 <= R_10 <= 1/10.
S10 = sp.summation(1 / n ** 2, (n, 1, 10))
R10 = sp.pi ** 2 / 6 - S10
assert sp.integrate(1 / x ** 2, (x, 11, sp.oo)) <= R10 <= sp.integrate(1 / x ** 2, (x, 10, sp.oo))
expect(16, "S_n + int from (n+1) to infinity of f(x) dx <= S <= S_n + int from n to infinity of f(x) dx")

assert sp.integrate(sp.exp(-x), (x, 1, sp.oo)) == sp.exp(-1)
assert sp.simplify(sp.summation(sp.exp(-n), (n, 1, sp.oo)) - 1 / (sp.E - 1)) == 0
expect(17, "converges, since int from 1 to infinity of e^(-x) dx = 1/e")
assert sp.integrate(x ** sp.Rational(-3, 2), (x, 1, sp.oo)) == 2
expect(18, "converges, since int from 1 to infinity of x^(-3/2) dx = 2")

# q19  u = arctan x: the integral is (arctan x)^2/2 evaluated from 1 to infinity.
I19 = sp.integrate(sp.atan(x) / (1 + x ** 2), (x, 1, sp.oo))
assert sp.simplify(I19 - 3 * sp.pi ** 2 / 32) == 0
expect(19, "converges")

# q20  f(x) = (2 + sin x)/x^2 is positive but f' changes sign arbitrarily far out:
#      near x = 2*pi*k the derivative is positive once x exceeds about 4.
f20 = (2 + sp.sin(x)) / x ** 2
d20 = sp.diff(f20, x)
assert all(d20.subs(x, 2 * sp.pi * k).evalf() > 0 for k in (2, 5, 10, 50))
assert sp.minimum(2 + sp.sin(x), x, sp.S.Reals) == 1  # 2 + sin x >= 1 > 0: terms positive
expect(20, "cannot be used, because f(x) = (2 + sin(x))/x^2 is not decreasing on any interval [k, infinity)")

# q21  int_2^oo dx/(x (ln x)^p) = (ln 2)^(1-p)/(p-1) for p > 1, divergent otherwise.
for p in (sp.Rational(3, 2), 2, 3):
    assert sp.integrate(1 / (x * sp.log(x) ** p), (x, 2, sp.oo)).is_finite
for p in (sp.Rational(1, 2), 1):
    assert sp.integrate(1 / (x * sp.log(x) ** p), (x, 2, sp.oo)) is sp.oo
expect(21, "p > 1")

assert sp.integrate(1 / (3 * x + 2), (x, 1, sp.oo)) is sp.oo
expect(22, "diverges, since int from 1 to infinity of dx/(3x + 2) diverges")
assert sp.integrate(x * sp.exp(-x), (x, 1, sp.oo)) == 2 / sp.E
expect(23, "converges, since int from 1 to infinity of x*e^(-x) dx = 2/e")

# q24  exactly one of the four integrals is finite
assert sp.integrate(x ** sp.Rational(-1, 2), (x, 1, sp.oo)) is sp.oo
assert sp.integrate(1 / (x * sp.log(x)), (x, 2, sp.oo)) is sp.oo
assert sp.integrate(x / (x ** 2 + 1), (x, 1, sp.oo)) is sp.oo
assert sp.integrate(x ** sp.Rational(-11, 10), (x, 1, sp.oo)) == 10
expect(24, "sum from n=1 to infinity of 1/n^(1.1)")

# q25  R_n <= 1/n, and 1/n <= 1/100 first holds at n = 100.
assert sp.integrate(1 / x ** 2, (x, 100, sp.oo)) == sp.Rational(1, 100)
assert sp.Rational(1, 99) > sp.Rational(1, 100)
expect(25, "100")

print("c10_4: all 25 keys verified")
