"""Verification for CALC 10.8 (Ratio Test for Convergence).

Every L in this module is recomputed as sp.limit(|a_(n+1)/a_n|, n, oo).  The
four items with L = 1 are additionally checked against what the series really
does (1/n and n/(n^2+1) diverge, 1/n^2 and the general L = 1 witnesses
converge), which is what makes "inconclusive" the only defensible key.

Run: python3 verify_c10_8.py
"""
import re

import sympy as sp

import c10_8

n = sp.Symbol("n", integer=True, positive=True)
x = sp.Symbol("x", positive=True)
Q = c10_8.QUESTIONS


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


def ratio_L(a):
    """L = lim |a_(n+1)/a_n|, simplified before the limit is taken."""
    r = sp.simplify(sp.Abs(a.subs(n, n + 1) / a))
    return sp.limit(r, n, sp.oo)


# q1, q2  the statement, and the fact that L = 1 covers both behaviours
assert ratio_L(1 / n) == 1 and sp.summation(1 / n, (n, 1, sp.oo)) is sp.oo
assert ratio_L(1 / n ** 2) == 1 and sp.summation(1 / n ** 2, (n, 1, sp.oo)) == sp.pi ** 2 / 6
expect(1, "L < 1")
expect(2, "may converge or diverge; the test is inconclusive")

assert ratio_L(n / 2 ** n) == sp.Rational(1, 2)
expect(3, "1/2")
assert ratio_L(2 ** n / sp.factorial(n)) == 0
expect(4, "converges, since L = 0")
assert ratio_L(sp.factorial(n) / 10 ** n) is sp.oo
expect(5, "diverges, since L = infinity")

expect(6, "L = 1, so the test is inconclusive; the series in fact diverges")
expect(7, "L = 1, so the test is inconclusive; the series in fact converges")

assert ratio_L(n ** 2 / 3 ** n) == sp.Rational(1, 3)
expect(8, "converges, since L = 1/3")
assert ratio_L((-1) ** n * 3 ** n / sp.factorial(n)) == 0
expect(9, "converges absolutely, since L = 0")
assert ratio_L(sp.factorial(n) / sp.factorial(2 * n)) == 0
expect(10, "converges, since L = 0")
assert ratio_L(3 ** n / (n * 2 ** n)) == sp.Rational(3, 2)
expect(11, "diverges, since L = 3/2")
assert ratio_L(sp.factorial(n) ** 2 / sp.factorial(2 * n)) == sp.Rational(1, 4)
expect(12, "converges, since L = 1/4")

# q13  every rational function gives L = 1; the series itself diverges
assert ratio_L(n / (n ** 2 + 1)) == 1
assert sp.limit((n / (n ** 2 + 1)) / (1 / n), n, sp.oo) == 1  # limit comparison with 1/n
assert sp.integrate(x / (x ** 2 + 1), (x, 1, sp.oo)) is sp.oo
expect(13, "L = 1, so the test is inconclusive")

assert ratio_L(1 / sp.factorial(n)) == 0
expect(14, "0")
assert ratio_L(sp.factorial(2 * n) / sp.factorial(n) ** 2) == 4
expect(15, "diverges, since L = 4")
assert ratio_L((-2) ** n / n ** 2) == 2
assert sp.limit(sp.Abs((-2) ** n / n ** 2), n, sp.oo) is sp.oo  # terms do not approach 0
expect(16, "diverges, since L = 2")

# q17  the ratio collapses to (1 + 1/n)^n
r17 = sp.simplify(sp.Abs((n + 1) ** (n + 1) / sp.factorial(n + 1) * sp.factorial(n) / n ** n))
assert sp.simplify(r17 - (1 + 1 / n) ** n) == 0
assert sp.limit(r17, n, sp.oo) == sp.E and sp.N(sp.E) > 1
expect(17, "diverges, since L = e")

assert ratio_L(5 ** n / (n ** 2 * 4 ** n)) == sp.Rational(5, 4)
expect(18, "diverges, since L = 5/4")

# q19  exactly one of the four has L = 1
assert ratio_L(3 ** n / sp.factorial(n)) == 0
assert ratio_L((2 * n + 3) / (n ** 3 + 1)) == 1
assert ratio_L(sp.factorial(n) / 5 ** n) is sp.oo
assert ratio_L(n / 4 ** n) == sp.Rational(1, 4)
expect(19, "sum from n=1 to infinity of (2n + 3)/(n^3 + 1)")

# q20  L = 1 for both a divergent and a convergent series (checked at the top)
expect(20, "unjustified, since L = 1 gives no information at all")

assert ratio_L((n + 1) / (n * 3 ** n)) == sp.Rational(1, 3)
expect(21, "converges, since L = 1/3")
assert ratio_L(1 / sp.factorial(2 * n)) == 0
expect(22, "converges, since L = 0")
assert ratio_L((-1) ** n * n ** 3 / sp.factorial(n)) == 0
expect(23, "converges absolutely, since L = 0")
assert ratio_L(2 ** n / n ** 2) == 2
expect(24, "diverges, since L = 2")

# q25  L = |x|, so the test gives convergence exactly for |x| < 1
t = sp.Symbol("t", positive=True)
assert sp.limit(sp.simplify(sp.Abs((n + 1) * t ** (n + 1) / (n * t ** n))), n, sp.oo) == t
for val in (sp.Rational(1, 2), sp.Rational(9, 10)):
    assert sp.summation(n * val ** n, (n, 1, sp.oo)).is_finite
assert sp.limit(n * 1 ** n, n, sp.oo) is sp.oo          # x = 1: terms diverge
assert sp.limit(sp.Abs(n * (-1) ** n), n, sp.oo) is sp.oo  # x = -1: terms diverge
expect(25, "|x| < 1")

print("c10_8: all 25 keys verified")
