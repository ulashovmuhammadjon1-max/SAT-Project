"""Verification for CALC 10.13 (Radius and Interval of Convergence).

For each power series the radius is recomputed from the ratio test with
sp.limit, and then EACH ENDPOINT is substituted and its numerical series
decided separately with sp.summation (or, where sympy leaves the sum
unevaluated, by the alternating series test hypotheses / the nth term test).
That endpoint-by-endpoint check is the whole point of the topic: six of these
series converge at one end and diverge at the other.

Run: python3 verify_c10_13.py
"""
import re

import sympy as sp

import c10_13

n = sp.Symbol("n", integer=True, positive=True)
t = sp.Symbol("t", positive=True)          # stands for |x - a|
Q = c10_13.QUESTIONS


def key(i):
    item = Q[i - 1]
    return item["choices"][item["ans"]]


def expect(i, text):
    assert key(i) == text, f"q{i}: key is {key(i)!r}, expected {text!r}"


for idx, item in enumerate(Q, 1):
    assert len(item["choices"]) == 4, f"q{idx}: needs exactly four choices"
    assert len(set(item["choices"])) == 4, f"q{idx}: repeated choice text"


def radius(coeff):
    """R from lim |c_(n+1)/c_n|: R = 1/L, with the two degenerate cases."""
    L = sp.limit(sp.Abs(sp.simplify(coeff.subs(n, n + 1) / coeff)), n, sp.oo)
    if L == 0:
        return sp.oo
    if L is sp.oo:
        return sp.Integer(0)
    return sp.simplify(1 / L)


def series_converges(term, lo=1):
    """Decide sum term (numeric, in n) with sympy; True/False.

    First sp.summation; if sympy leaves the sum unevaluated (it does for
    sum 1/sqrt(n)), fall back to the integral test, after checking with sympy
    that the integrand really is positive and decreasing on [lo, oo).
    """
    s = sp.summation(term, (n, lo, sp.oo))
    if s.is_finite is True:
        return True
    if s in (sp.oo, -sp.oo):
        return False
    z = sp.Symbol("z", positive=True)
    f = term.subs(n, z)
    assert sp.minimum(f, z, sp.Interval(lo, sp.oo)) >= 0, f
    d = sp.simplify(sp.diff(f, z))
    assert sp.solveset(d >= 0, z, sp.Interval.open(lo, sp.oo)) == sp.EmptySet, d
    I = sp.integrate(f, (z, lo, sp.oo))
    if I is sp.oo:
        return False
    assert I.is_finite is True, I
    return True


def alternating_converges(b, lo=1):
    """AST: b_n positive, decreasing (derivative sign), and tending to 0."""
    y = sp.Symbol("y", positive=True)
    d = sp.simplify(sp.diff(b.subs(n, y), y))
    sol = sp.solveset(d >= 0, y, sp.Interval.open(lo, sp.oo))
    assert not isinstance(sol, sp.ConditionSet), d
    return sol == sp.EmptySet and sp.limit(b.subs(n, y), y, sp.oo) == 0


def terms_fail_to_vanish(term):
    y = sp.Symbol("y", positive=True)
    return sp.limit(sp.Abs(term.subs(n, y)), y, sp.oo) != 0


# --- q1, q2, q16, q18, q21, q22: the general facts ------------------------------
expect(1, "the series converges for |x - a| < R and diverges for |x - a| > R")
expect(2, "gives L = 1 and is inconclusive, so another test is needed")
# q16  All four endpoint patterns occur among q3, q4, q5 and q17 below, so the
#      radius alone cannot determine the interval.
expect(16, "except at the two endpoints, which must be tested separately")
# q18  |5 - 3| = 2 and |9 - 3| = 6.
assert abs(5 - 3) == 2 and abs(9 - 3) == 6
expect(18, "2 <= R <= 6")
# q21  center 1, R = 4 gives guaranteed convergence on (1-4, 1+4)
assert (1 - 4, 1 + 4) == (-3, 5)
expect(21, "-3 < x < 5")
# q22  At x = a every term with n >= 1 vanishes, so the sum is c_0.
expect(22, "at x = a, at least")

# --- q3  sum x^n/n --------------------------------------------------------------
assert radius(1 / n) == 1
assert not series_converges(1 / n)                       # x = 1
assert alternating_converges(1 / n)                      # x = -1
expect(3, "[-1, 1)")

# --- q4  sum x^n/n^2 ------------------------------------------------------------
assert radius(1 / n ** 2) == 1
assert series_converges(1 / n ** 2) and series_converges((-1) ** n / n ** 2)
expect(4, "[-1, 1]")

# --- q5  sum x^n ----------------------------------------------------------------
assert radius(sp.Integer(1) ** n) == 1
assert terms_fail_to_vanish(sp.Integer(1) ** n) and terms_fail_to_vanish((-1) ** n)
expect(5, "(-1, 1)")

# --- q6, q7  the two degenerate radii -------------------------------------------
assert radius(1 / sp.factorial(n)) is sp.oo
expect(6, "all real numbers")
assert radius(sp.factorial(n)) == 0
assert sp.limit(sp.factorial(n) * sp.Rational(1, 1000) ** n, n, sp.oo) is sp.oo
expect(7, "only x = 0")

# --- q8  sum (x-2)^n/n, center 2 -------------------------------------------------
assert radius(1 / n) == 1
assert alternating_converges(1 / n)                      # x = 1 gives (-1)^n/n
assert not series_converges(1 / n)                       # x = 3 gives 1/n
expect(8, "[1, 3)")

# --- q9  sum (x+3)^n/3^n, center -3, R = 3 --------------------------------------
assert radius(1 / 3 ** n) == 3
assert terms_fail_to_vanish(sp.Integer(1) ** n) and terms_fail_to_vanish((-1) ** n)
expect(9, "(-6, 0)")

# --- q10  sum (2x)^n/n -----------------------------------------------------------
assert radius(2 ** n / n) == sp.Rational(1, 2)
assert not series_converges(1 / n) and alternating_converges(1 / n)
expect(10, "[-1/2, 1/2)")

# --- q11  sum (x-1)^n/(n 2^n), center 1, R = 2 -----------------------------------
assert radius(1 / (n * 2 ** n)) == 2
assert alternating_converges(1 / n)                      # x = -1
assert not series_converges(1 / n)                       # x = 3
expect(11, "[-1, 3)")

# --- q12  sum n x^n ---------------------------------------------------------------
assert radius(sp.Integer(1) * n) == 1
assert terms_fail_to_vanish(n) and terms_fail_to_vanish(n * (-1) ** n)
expect(12, "(-1, 1)")

# --- q13  sum x^n/sqrt(n) ---------------------------------------------------------
assert radius(1 / sp.sqrt(n)) == 1
assert not series_converges(1 / sp.sqrt(n))              # x = 1
assert alternating_converges(1 / sp.sqrt(n))             # x = -1
expect(13, "[-1, 1)")

# --- q14  sum x^(2n)/n: the ratio is |x|^2 -----------------------------------------
y = sp.Symbol("y", positive=True)
L14 = sp.limit(sp.simplify((y ** (2 * (n + 1)) / (n + 1)) / (y ** (2 * n) / n)), n, sp.oo)
assert sp.simplify(L14 - y ** 2) == 0
assert sp.solveset(y ** 2 < 1, y, sp.Interval.open(0, sp.oo)) == sp.Interval.open(0, 1)
expect(14, "1")

# --- q15  L = 1/5 gives R = 5 -------------------------------------------------------
assert 1 / sp.Rational(1, 5) == 5
expect(15, "5")

# --- q17  sum (-1)^n x^n/(n+1) -------------------------------------------------------
assert radius((-1) ** n / (n + 1)) == 1
# x = 1 gives sum (-1)^n/(n+1): alternating, decreasing to 0
assert alternating_converges(1 / (n + 1))
# x = -1 gives sum 1/(n+1): the harmonic tail, divergent
assert not series_converges(1 / (n + 1))
expect(17, "(-1, 1]")

# --- q19  center of (x + 4)^n --------------------------------------------------------
expect(19, "x = -4")

# --- q20  sum (x-2)^n/n^2, center 2 ---------------------------------------------------
assert radius(1 / n ** 2) == 1
assert series_converges(1 / n ** 2) and series_converges((-1) ** n / n ** 2)
expect(20, "[1, 3]")

# --- q23  sum n^2 x^n/2^n --------------------------------------------------------------
assert radius(n ** 2 / 2 ** n) == 2
expect(23, "2")

# --- q24  sum n x^n/2^n ----------------------------------------------------------------
assert radius(n / 2 ** n) == 2
assert terms_fail_to_vanish(n) and terms_fail_to_vanish(n * (-1) ** n)
expect(24, "(-2, 2)")

# --- q25  sum (x-1)^n/(n^2 3^n), center 1, R = 3 ---------------------------------------
assert radius(1 / (n ** 2 * 3 ** n)) == 3
assert series_converges(1 / n ** 2) and series_converges((-1) ** n / n ** 2)
expect(25, "[-2, 4]")

print("c10_13: all 25 keys verified")
