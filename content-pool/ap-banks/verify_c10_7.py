"""Verification for CALC 10.7 (Alternating Series Test for Convergence).

For every item the two hypotheses are checked separately with sympy:

  * decreasing -- the derivative of the continuous extension is negative on the
    stated interval (or, for factorial terms, the ratio b_(n+1)/b_n is < 1); and
  * lim b_n = 0 -- computed with sp.limit.

A series is keyed "diverges" only when sp.limit shows b_n does not approach 0.

Run: python3 verify_c10_7.py
"""
import re

import sympy as sp

import c10_7

n = sp.Symbol("n", integer=True, positive=True)
x = sp.Symbol("x", positive=True)
Q = c10_7.QUESTIONS


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


def tends_to_zero(b):
    return sp.limit(b.subs(n, x), x, sp.oo) == 0


def decreasing_from(b, lo):
    """True if the continuous extension of b has negative derivative on (lo, oo).

    Solved with solveset, not sampled.  If solveset cannot decide (it returns a
    ConditionSet), this raises rather than quietly returning False, so that no
    "decreasing" claim can slip through unproved; the three terms it cannot
    handle are argued explicitly further down.
    """
    d = sp.simplify(sp.diff(b.subs(n, x), x))
    sol = sp.solveset(d >= 0, x, sp.Interval.open(lo, sp.oo))
    if isinstance(sol, sp.ConditionSet):
        raise RuntimeError(f"solveset inconclusive for d/dx {b} = {d}")
    return sol == sp.EmptySet


def ast_applies(b, lo=1):
    return tends_to_zero(b) and decreasing_from(b, lo)


# q1  Both hypotheses.  q12 is the case where only the limit condition holds.
expect(1, "b_n is eventually decreasing and lim as n -> infinity of b_n = 0")

# --- the divergent ones: b_n does not approach 0 -------------------------------
assert sp.limit(x / (x + 1), x, sp.oo) == 1
expect(2, "diverges, because b_n = n/(n+1) does not approach 0")
assert sp.limit(x / (2 * x + 1), x, sp.oo) == sp.Rational(1, 2)
expect(6, "diverges, because b_n approaches 1/2 rather than 0")
assert sp.limit(3 * x / (x + 5), x, sp.oo) == 3
expect(19, "diverges, because b_n approaches 3")
assert sp.limit(sp.atan(x), x, sp.oo) == sp.pi / 2
expect(23, "diverges, because arctan(n) approaches pi/2")

# --- the convergent ones -------------------------------------------------------
assert ast_applies(1 / n)
expect(3, "converges by the alternating series test")
assert ast_applies(1 / sp.sqrt(n))
expect(4, "converges by the alternating series test")
assert ast_applies(1 / n ** 2)
expect(5, "converges by the alternating series test")

# q7  ln(x)/x decreases past x = e, so from n = 3 on
assert tends_to_zero(sp.log(n) / n) and decreasing_from(sp.log(n) / n, 3)
assert sp.integrate(sp.log(x) / x, (x, 2, sp.oo)) is sp.oo  # absolute series diverges
expect(7, "converges by the alternating series test, since ln(n)/n decreases to 0 for n >= 3")

# q8  1/n! : the ratio b_(n+1)/b_n = 1/(n+1) < 1 for every n >= 1
assert sp.simplify(sp.factorial(n) / sp.factorial(n + 1)) == 1 / (n + 1)
assert sp.limit(1 / sp.factorial(n), n, sp.oo) == 0
assert sp.summation((-1) ** n / sp.factorial(n), (n, 1, sp.oo)) == 1 / sp.E - 1
expect(8, "converges by the alternating series test")

assert ast_applies(n / (n ** 2 + 1))
assert sp.integrate(x / (x ** 2 + 1), (x, 1, sp.oo)) is sp.oo
expect(9, "converges by the alternating series test")

# q10  2^n/n! : ratio is 2/(n+1), which is < 1 exactly for n >= 2
r10 = sp.simplify((2 ** (n + 1) / sp.factorial(n + 1)) / (2 ** n / sp.factorial(n)))
assert r10 == 2 / (n + 1)
assert r10.subs(n, 1) == 1 and all(r10.subs(n, m) < 1 for m in range(2, 20))
assert sp.limit(2 ** n / sp.factorial(n), n, sp.oo) == 0
expect(10, "converges by the alternating series test, since 2^n/n! decreases to 0 for n >= 2")

# q11  d/dx sin(1/x) = -cos(1/x)/x^2.  For x >= 1 the angle 1/x lies in (0, 1],
#      an interval inside (0, pi/2) where cosine is positive, so the derivative
#      is negative; and sin(1/n) is positive there for the same reason.
u = sp.Symbol("u", positive=True)
assert sp.simplify(sp.diff(sp.sin(1 / x), x) + sp.cos(1 / x) / x ** 2) == 0
assert sp.N(1) < sp.N(sp.pi / 2)
assert sp.minimum(sp.cos(u), u, sp.Interval(0, 1)) == sp.cos(1) and sp.N(sp.cos(1)) > 0
assert sp.minimum(sp.sin(u), u, sp.Interval(0, 1)) == 0 and sp.N(sp.sin(1)) > 0
assert tends_to_zero(sp.sin(1 / n))
expect(11, "converges by the alternating series test")

# q12  A failed hypothesis leaves the test with no conclusion in either
#      direction; convergence must be settled some other way.
expect(12, "cannot be applied, and another argument is needed")

assert ast_applies(1 / (2 * n - 1))
assert sp.summation((-1) ** (n + 1) / (2 * n - 1), (n, 1, sp.oo)) == sp.pi / 4
expect(13, "converges by the alternating series test")

# q14  (-1)^n * cos(n*pi) = (-1)^(2n) = 1, so the series is the harmonic series
assert all(sp.simplify((-1) ** m * sp.cos(m * sp.pi)) == 1 for m in range(1, 12))
assert sp.summation(1 / n, (n, 1, sp.oo)) is sp.oo
expect(14, "diverges, because the series simplifies to the harmonic series")

assert ast_applies(sp.sqrt(n) / (n + 1))
expect(15, "converges by the alternating series test")
assert ast_applies(sp.exp(-n))
expect(16, "converges by the alternating series test")

# q17  x/(x^2+4): derivative (4 - x^2)/(x^2+4)^2 is negative for x > 2, and the
#      sequence itself already satisfies b_2 > b_3 > ...; b_1 < b_2, so N = 2.
d17 = sp.simplify(sp.diff(x / (x ** 2 + 4), x))
assert sp.simplify(d17 - (4 - x ** 2) / (x ** 2 + 4) ** 2) == 0
assert d17.subs(x, sp.Rational(3, 2)) > 0 and d17.subs(x, 3) < 0
b17 = [sp.Rational(m, m ** 2 + 4) for m in range(1, 8)]
assert b17[0] < b17[1] and all(b17[i] > b17[i + 1] for i in range(1, 6))
expect(17, "2")

# q18  exactly one of the four has b_n not approaching 0
assert sp.limit(x ** sp.Rational(-1, 3), x, sp.oo) == 0
assert sp.limit((x + 1) / x ** 2, x, sp.oo) == 0
assert sp.limit(1 / (x + 3), x, sp.oo) == 0
assert sp.limit((x ** 2 + 1) / (x ** 2 + 2), x, sp.oo) == 1
expect(18, "sum from n=1 to infinity of (-1)^n*(n^2+1)/(n^2+2)")

assert tends_to_zero(1 / sp.log(n)) and decreasing_from(1 / sp.log(n), 2)
# 1/ln(n) > 1/n for n >= 2, and the harmonic series diverges
assert sp.minimum(x - sp.log(x), x, sp.Interval(2, sp.oo)) > 0
assert sp.summation(1 / n, (n, 2, sp.oo)) is sp.oo
expect(20, "converges by the alternating series test")

# q21  x^2/2^x decreases once x > 2/ln 2 = 2.885..., so from n = 3 on
#      d/dx (x^2 * 2^(-x)) = x*2^(-x)*(2 - x*ln 2), negative exactly when
#      x > 2/ln(2) = 2.885..., so certainly for x > 3.
assert sp.simplify(sp.diff(x ** 2 / 2 ** x, x) - x * 2 ** (-x) * (2 - x * sp.log(2))) == 0
assert sp.N(2 / sp.log(2)) < 3
assert tends_to_zero(n ** 2 / 2 ** n)
expect(21, "converges by the alternating series test, since n^2/2^n decreases to 0 for n >= 3")

assert ast_applies((n + 1) / n ** 2)
assert sp.summation((n + 1) / n ** 2, (n, 1, sp.oo)) is sp.oo
expect(22, "converges by the alternating series test")

# q24  d/dx 1/(x*ln x) = -(1 + ln x)/(x*ln x)^2, and for x >= 2 both 1 + ln x
#      and the square are positive, so the derivative is negative.
assert sp.simplify(sp.diff(1 / (x * sp.log(x)), x) + (1 + sp.log(x)) / (x * sp.log(x)) ** 2) == 0
assert sp.minimum(1 + sp.log(x), x, sp.Interval(2, sp.oo)) == 1 + sp.log(2)
assert tends_to_zero(1 / (n * sp.log(n)))
assert sp.integrate(1 / (x * sp.log(x)), (x, 2, sp.oo)) is sp.oo
expect(24, "converges by the alternating series test")

# q25  1/n^p decreases to 0 exactly when p > 0
for p in (sp.Rational(1, 10), sp.Rational(1, 2), 1, 2):
    assert ast_applies(1 / n ** p), p
for p in (0, sp.Rational(-1, 2), -2):
    assert sp.limit(x ** -p, x, sp.oo) != 0, p
expect(25, "p > 0")

print("c10_7: all 25 keys verified")
