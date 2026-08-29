"""Verification for CALC 10.5 (Harmonic Series and p-Series).

Convergence of every p-series below is decided by sp.summation: it returns
zeta(p) (finite) when p > 1 and oo when p <= 1, so the p > 1 criterion is being
recomputed rather than assumed.  The boundary cases p = 1, p = 0 and p = -2 are
checked explicitly.

Run: python3 verify_c10_5.py
"""
import re

import sympy as sp

import c10_5

n = sp.Symbol("n", integer=True, positive=True)
Q = c10_5.QUESTIONS


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


def pseries(p):
    """True if sum 1/n^p converges, decided by sympy."""
    s = sp.summation(1 / n ** sp.nsimplify(p), (n, 1, sp.oo))
    return s.is_finite is True


# q1  The criterion itself, recomputed on both sides of p = 1.
for p in (sp.Rational(101, 100), sp.Rational(3, 2), 2, 3):
    assert pseries(p), p
for p in (sp.Rational(1, 3), sp.Rational(1, 2), sp.Rational(2, 3), 1):
    assert not pseries(p), p
expect(1, "p > 1")

assert sp.summation(1 / n, (n, 1, sp.oo)) is sp.oo
expect(2, "diverges")
assert sp.summation(1 / n ** 2, (n, 1, sp.oo)) == sp.pi ** 2 / 6
expect(3, "converges, since p = 2 > 1")
assert not pseries(sp.Rational(1, 2))
expect(4, "diverges, since p = 1/2 is not greater than 1")
assert pseries(3)
expect(5, "converges")

# q6, q7  the two sides of p = 1 at a hundredth of a unit
assert not pseries(sp.Rational(999, 1000))
expect(6, "diverges, since p = 0.999 is not greater than 1")
assert pseries(sp.Rational(1001, 1000))
expect(7, "converges")

assert not pseries(sp.Rational(1, 3))
expect(8, "diverges")

# q9  constant multiple of the harmonic series
assert sp.summation(5 / n, (n, 1, sp.oo)) is sp.oo
expect(9, "diverges")
# q10  a tail of the harmonic series
assert sp.summation(1 / n, (n, 100, sp.oo)) is sp.oo
expect(10, "diverges")
# q11  convergent + divergent
assert sp.summation(1 / n ** 2 + 1 / n, (n, 1, sp.oo)) is sp.oo
expect(11, "diverges, since 1/n diverges")

assert pseries(sp.Rational(4, 3))
expect(12, "converges")
assert sp.simplify(1 / (n * sp.sqrt(n)) - n ** sp.Rational(-3, 2)) == 0 and pseries(sp.Rational(3, 2))
expect(13, "converges, since it is the p-series with p = 3/2")
assert not pseries(sp.Rational(2, 3))
expect(14, "diverges, since p = 2/3 is not greater than 1")

# q15  exactly one of the four converges
assert not pseries(sp.Rational(2, 3)) and not pseries(1) and pseries(sp.Rational(5, 4))
assert sp.summation(2 / (3 * n), (n, 1, sp.oo)) is sp.oo
expect(15, "sum from n=1 to infinity of 1/n^(5/4)")

assert sp.summation(2 / n ** 3 - 3 / n, (n, 1, sp.oo)) is sp.S.NegativeInfinity
expect(16, "diverges")

# q17  H_n -> oo but H_n - ln(n) -> Euler's constant
assert sp.limit(sp.harmonic(n), n, sp.oo) is sp.oo
assert sp.limit(sp.harmonic(n) - sp.log(n), n, sp.oo) == sp.EulerGamma
assert sp.EulerGamma.is_finite
expect(17, "H_n - ln(n) approaches a finite constant, while H_n itself increases without bound")

# q18  terms -> 0 yet the series diverges
assert sp.limit(1 / n, n, sp.oo) == 0 and sp.summation(1 / n, (n, 1, sp.oo)) is sp.oo
expect(18, "Its terms approach 0, yet it diverges")

assert sp.simplify(sp.sqrt(n) / n ** 2 - n ** sp.Rational(-3, 2)) == 0
expect(19, "converges, since it is the p-series with p = 3/2")
assert pseries(sp.Rational(5, 2))  # the constant 3 does not affect convergence
expect(20, "converges")

# q21  1/n^(-2) = n^2
assert sp.simplify(1 / n ** -2 - n ** 2) == 0
assert sp.summation(n ** 2, (n, 1, sp.oo)) is sp.oo
expect(21, "diverges, since the series is sum of n^2")
# q22  every term is 1
assert sp.summation(n ** 0, (n, 1, sp.oo)) is sp.oo
expect(22, "diverges, since every term equals 1")

# q23  the convergence set {p : p > 1} is open, so it has no least element:
#      for any p > 1 the smaller exponent (1 + p)/2 is still greater than 1.
for p in (sp.Rational(11, 10), sp.Rational(1001, 1000), sp.Rational(100001, 100000)):
    smaller = (1 + p) / 2
    assert 1 < smaller < p and pseries(smaller)
expect(23, "There is no smallest such value")

assert not pseries(sp.Rational(2, 3)) and pseries(sp.Rational(3, 2))
expect(24, "Only sum 1/n^(3/2) converges")

# q25  n^k/n^3 = 1/n^(3-k); convergence needs 3 - k > 1, i.e. k < 2
for k in (0, 1, sp.Rational(3, 2), sp.Rational(19, 10)):
    assert pseries(3 - k), k
for k in (2, sp.Rational(21, 10), 3):
    assert not pseries(3 - k), k
expect(25, "k < 2")

print("c10_5: all 25 keys verified")
