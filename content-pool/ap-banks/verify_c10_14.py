"""Verification for CALC 10.14 (Finding Taylor or Maclaurin Series).

Every keyed series is written out as a sympy general term and summed far enough
to compare its coefficients, one power at a time, against sp.series of the
function it is supposed to represent.  The distractor general terms are checked
too: each is confirmed to DISAGREE with the function somewhere in the same
range of powers, so no question has a second correct answer.

Run: python3 verify_c10_14.py
"""
import sympy as sp

import c10_14

x = sp.Symbol("x")
k = sp.Symbol("k", integer=True, nonnegative=True)
Q = c10_14.QUESTIONS


def key(i):
    item = Q[i - 1]
    return item["choices"][item["ans"]]


def expect(i, text):
    assert key(i) == text, f"q{i}: key is {key(i)!r}, expected {text!r}"


for idx, item in enumerate(Q, 1):
    assert len(item["choices"]) == 4, f"q{idx}: needs exactly four choices"
    assert len(set(item["choices"])) == 4, f"q{idx}: repeated choice text"


def coeffs(expr, order, a=0):
    """Coefficients of (x - a)^0 .. (x - a)^order in expr, expanded about a."""
    u = sp.Symbol("u")
    e = sp.expand(expr.subs(x, a + u))
    return [sp.simplify(e.coeff(u, m)) for m in range(order + 1)]


def series_coeffs(f, order, a=0):
    u = sp.Symbol("u")
    e = sp.series(f.subs(x, a + u), u, 0, order + 1).removeO()
    return [sp.simplify(sp.expand(e).coeff(u, m)) for m in range(order + 1)]


def partial(term, lo, hi):
    """Sum of `term` (a function of k) for k = lo..hi."""
    return sum(term.subs(k, j) for j in range(lo, hi + 1))


def agrees(f, term, lo, order, a=0, nterms=None):
    """True if the series built from `term` matches f through (x - a)^order."""
    hi = lo + (nterms if nterms is not None else order + 2)
    return coeffs(partial(term, lo, hi), order, a) == series_coeffs(f, order, a)


def check(i, f, term, lo, order, a=0):
    assert agrees(f, term, lo, order, a), f"q{i}: keyed series does not match"


# --- the five standard series ---------------------------------------------------
check(1, sp.exp(x), x ** k / sp.factorial(k), 0, 6)
expect(1, "sum from n=0 to infinity of x^n/n!")
check(2, sp.sin(x), (-1) ** k * x ** (2 * k + 1) / sp.factorial(2 * k + 1), 0, 7)
expect(2, "sum from n=0 to infinity of (-1)^n*x^(2n+1)/(2n+1)!")
check(3, sp.cos(x), (-1) ** k * x ** (2 * k) / sp.factorial(2 * k), 0, 8)
expect(3, "sum from n=0 to infinity of (-1)^n*x^(2n)/(2n)!")
check(4, 1 / (1 - x), x ** k, 0, 6)
expect(4, "sum from n=0 to infinity of x^n")
check(5, sp.log(1 + x), (-1) ** (k + 1) * x ** k / k, 1, 6)
expect(5, "sum from n=1 to infinity of (-1)^(n+1)*x^n/n")

# --- built by substitution -------------------------------------------------------
check(6, sp.exp(-x), (-1) ** k * x ** k / sp.factorial(k), 0, 6)
expect(6, "sum from n=0 to infinity of (-1)^n*x^n/n!")
check(7, sp.exp(x ** 2), x ** (2 * k) / sp.factorial(k), 0, 8)
expect(7, "sum from n=0 to infinity of x^(2n)/n!")
check(8, sp.sin(x ** 2), (-1) ** k * x ** (4 * k + 2) / sp.factorial(2 * k + 1), 0, 10)
expect(8, "sum from n=0 to infinity of (-1)^n*x^(4n+2)/(2n+1)!")
check(9, 1 / (1 + x), (-1) ** k * x ** k, 0, 6)
expect(9, "sum from n=0 to infinity of (-1)^n*x^n")
check(10, 1 / (1 - 2 * x), 2 ** k * x ** k, 0, 6)
expect(10, "sum from n=0 to infinity of 2^n*x^n")
check(14, sp.cos(2 * x), (-1) ** k * 4 ** k * x ** (2 * k) / sp.factorial(2 * k), 0, 8)
expect(14, "sum from n=0 to infinity of (-1)^n*4^n*x^(2n)/(2n)!")
check(20, sp.log(1 - x), -x ** k / k, 1, 6)
expect(20, "-sum from n=1 to infinity of x^n/n")
check(24, 1 / (1 + x ** 2), (-1) ** k * x ** (2 * k), 0, 8)
expect(24, "sum from n=0 to infinity of (-1)^n*x^(2n)")

# --- built by multiplying by a power of x ----------------------------------------
check(11, x * sp.exp(x), x ** (k + 1) / sp.factorial(k), 0, 6)
# the three distractors really are different functions
assert not agrees(x * sp.exp(x), x ** k / sp.factorial(k), 0, 6)
assert not agrees(x * sp.exp(x), x ** (k + 1) / sp.factorial(k + 1), 0, 6)
assert not agrees(x * sp.exp(x), x ** (2 * k) / sp.factorial(k), 0, 6)
expect(11, "sum from n=0 to infinity of x^(n+1)/n!")
check(18, x ** 2 * sp.sin(x), (-1) ** k * x ** (2 * k + 3) / sp.factorial(2 * k + 1), 0, 9)
expect(18, "sum from n=0 to infinity of (-1)^n*x^(2n+3)/(2n+1)!")

# --- built by differentiating or integrating --------------------------------------
# q12  term-by-term differentiation of the sine series gives the cosine series
d12 = sp.diff(partial((-1) ** k * x ** (2 * k + 1) / sp.factorial(2 * k + 1), 0, 6), x)
assert coeffs(d12, 8) == series_coeffs(sp.cos(x), 8)
expect(12, "cos(x)")
check(13, sp.atan(x), (-1) ** k * x ** (2 * k + 1) / (2 * k + 1), 0, 9)
expect(13, "sum from n=0 to infinity of (-1)^n*x^(2n+1)/(2n+1)")
# q21  integrating sum x^n term by term gives x + x^2/2 + ... = -ln(1 - x)
i21 = sp.integrate(partial(x ** k, 0, 8), x)
assert coeffs(i21, 7) == series_coeffs(-sp.log(1 - x), 7)
expect(21, "-ln(1 - x)")

# --- Taylor series about a center other than 0 -------------------------------------
check(15, sp.exp(x), sp.E * (x - 1) ** k / sp.factorial(k), 0, 6, a=1)
expect(15, "sum from n=0 to infinity of e*(x - 1)^n/n!")
check(16, 1 / x, (-1) ** k * (x - 1) ** k, 0, 6, a=1)
expect(16, "sum from n=0 to infinity of (-1)^n*(x - 1)^n")

# --- products, single coefficients, and a limit -------------------------------------
# q17  e^x cos x: the x^2 terms cancel
c17 = series_coeffs(sp.exp(x) * sp.cos(x), 3)
assert c17 == [1, 1, 0, sp.Rational(-1, 3)]
expect(17, "1 + x - x^3/3")

assert series_coeffs(sp.sin(x), 5)[5] == sp.Rational(1, 120)
expect(19, "1/120")

assert sp.limit((sp.sin(x) - x) / x ** 3, x, 0) == sp.Rational(-1, 6)
assert series_coeffs(sp.sin(x) - x, 5) == [0, 0, 0, sp.Rational(-1, 6), 0, sp.Rational(1, 120)]
expect(22, "-1/6")

# q23  the definition of the Taylor series about a
expect(23, "sum from n=0 to infinity of f^(n)(a)*(x - a)^n/n!")

# q25  e^x/(1 - x): 1, 1+1 = 2, 1 + 1 + 1/2 = 5/2
c25 = series_coeffs(sp.exp(x) / (1 - x), 2)
assert c25 == [1, 2, sp.Rational(5, 2)]
expect(25, "1 + 2x + 5x^2/2")

print("c10_14: all 25 keys verified")
