"""Verification for CALC 10.15 (Representing Functions as Power Series).

Two kinds of check, matching the two directions the topic runs in:

  * function -> series: the keyed general term is summed far enough and its
    coefficients compared, power by power, with sp.series of the function; the
    radius is recomputed from the ratio test.
  * series -> number: the numerical sum is evaluated directly with
    sp.summation, independently of the power-series argument the stem gives.

Run: python3 verify_c10_15.py
"""
import sympy as sp

import c10_15

x = sp.Symbol("x")
k = sp.Symbol("k", integer=True, nonnegative=True)
n = sp.Symbol("n", integer=True, positive=True)
Q = c10_15.QUESTIONS


def key(i):
    item = Q[i - 1]
    return item["choices"][item["ans"]]


def expect(i, text):
    assert key(i) == text, f"q{i}: key is {key(i)!r}, expected {text!r}"


for idx, item in enumerate(Q, 1):
    assert len(item["choices"]) == 4, f"q{idx}: needs exactly four choices"
    assert len(set(item["choices"])) == 4, f"q{idx}: repeated choice text"


def coeffs(expr, order):
    e = sp.expand(expr)
    return [sp.simplify(e.coeff(x, m)) for m in range(order + 1)]


def series_coeffs(f, order):
    e = sp.series(f, x, 0, order + 1).removeO()
    return [sp.simplify(sp.expand(e).coeff(x, m)) for m in range(order + 1)]


def partial(term, lo, hi):
    return sum(term.subs(k, j) for j in range(lo, hi + 1))


def agrees(f, term, lo, order):
    return coeffs(partial(term, lo, lo + order + 2), order) == series_coeffs(f, order)


def check(i, f, term, lo, order):
    assert agrees(f, term, lo, order), f"q{i}: keyed series does not match"


def radius(coeff_of_k):
    """R from the ratio test on the coefficient sequence."""
    L = sp.limit(sp.Abs(sp.simplify(coeff_of_k.subs(k, k + 1) / coeff_of_k)), k, sp.oo)
    return sp.oo if L == 0 else sp.simplify(1 / L)


# --- q1  the algebraic rewrite --------------------------------------------------
assert sp.simplify(1 / (3 - x) - sp.Rational(1, 3) * 1 / (1 - x / 3)) == 0
expect(1, "(1/3)*1/(1 - x/3)")

# --- function -> series ----------------------------------------------------------
check(2, 1 / (3 - x), x ** k / 3 ** (k + 1), 0, 6)
assert radius(1 / 3 ** (k + 1)) == 3
expect(2, "sum from n=0 to infinity of x^n/3^(n+1)")

check(3, 1 / (2 + x), (-1) ** k * x ** k / 2 ** (k + 1), 0, 6)
assert radius((-1) ** k / 2 ** (k + 1)) == 2
expect(3, "sum from n=0 to infinity of (-1)^n*x^n/2^(n+1)")

check(4, 1 / (1 + x ** 3), (-1) ** k * x ** (3 * k), 0, 9)
expect(4, "sum from n=0 to infinity of (-1)^n*x^(3n)")

# q5  the geometric ratio is -x^3, so convergence needs |x|^3 < 1
y = sp.Symbol("y", positive=True)
assert sp.solveset(y ** 3 < 1, y, sp.Interval.open(0, sp.oo)) == sp.Interval.open(0, 1)
expect(5, "|x| < 1")

check(6, x / (1 - x), x ** (k + 1), 0, 6)
expect(6, "sum from n=0 to infinity of x^(n+1)")
check(7, x ** 2 / (1 - x), x ** (k + 2), 0, 6)
expect(7, "sum from n=0 to infinity of x^(n+2)")

# q8  differentiating sum x^n term by term
d8 = sp.diff(partial(x ** k, 0, 9), x)
assert coeffs(d8, 7) == series_coeffs(1 / (1 - x) ** 2, 7)
check(8, 1 / (1 - x) ** 2, (k + 1) * x ** k, 0, 7)
expect(8, "1/(1 - x)^2, as sum from n=0 to infinity of (n+1)*x^n")

check(9, 1 / (1 - x ** 2), x ** (2 * k), 0, 8)
expect(9, "sum from n=0 to infinity of x^(2n)")
check(10, x / (1 + x ** 2), (-1) ** k * x ** (2 * k + 1), 0, 9)
expect(10, "sum from n=0 to infinity of (-1)^n*x^(2n+1)")

check(11, 3 / (1 - 2 * x), 3 * 2 ** k * x ** k, 0, 6)
assert radius(3 * 2 ** k) == sp.Rational(1, 2)
expect(11, "sum from n=0 to infinity of 3*2^n*x^n, for |x| < 1/2")

# q12  1/(4 + x^2) = (1/4)*sum (-1)^n (x/2)^(2n): radius 2
check(12, 1 / (4 + x ** 2), (-1) ** k * x ** (2 * k) / 4 ** (k + 1), 0, 8)
assert sp.solveset((y / 2) ** 2 < 1, y, sp.Interval.open(0, sp.oo)) == sp.Interval.open(0, 2)
expect(12, "2")

# --- q13, q14  what differentiation and integration do to the radius --------------
# Same radius both ways: sum x^n, its derivative sum n x^(n-1) and its integral
# sum x^(n+1)/(n+1) all have R = 1, checked by the ratio test on coefficients.
assert radius(sp.Integer(1) ** k) == 1
assert radius(k + 1) == 1            # coefficients of the differentiated series
assert radius(1 / (k + 1)) == 1      # coefficients of the integrated series
expect(13, "the same as the original")
# Endpoints can change: sum x^n diverges at x = -1, while sum x^n/n converges there.
assert sp.limit(sp.Abs((-1) ** n), n, sp.oo) != 0
assert sp.summation((-1) ** n / n, (n, 1, sp.oo)) == -sp.log(2)
expect(14, "the same radius of convergence, though the endpoint behavior may differ")

# --- q15, q16  integrating a known series -----------------------------------------
i15 = sp.integrate(partial((-1) ** k * x ** k, 0, 8), x)
assert coeffs(i15, 7) == series_coeffs(sp.log(1 + x), 7)
expect(15, "ln(1 + x)")
i16 = sp.integrate(partial((-1) ** k * x ** (2 * k), 0, 5), x)
assert coeffs(i16, 9) == series_coeffs(sp.atan(x), 9)
expect(16, "arctan(x)")

# --- q17, q18  series for antiderivatives with no elementary form ------------------
t = sp.Symbol("t")
F17 = sp.integrate(sp.series(sp.exp(-t ** 2), t, 0, 12).removeO(), (t, 0, x))
assert coeffs(F17, 11) == coeffs(partial((-1) ** k * x ** (2 * k + 1) / (sp.factorial(k) * (2 * k + 1)), 0, 6), 11)
expect(17, "sum from n=0 to infinity of (-1)^n*x^(2n+1)/(n!*(2n+1))")

F18 = sp.integrate(sp.series(sp.sin(t) / t, t, 0, 12).removeO(), (t, 0, x))
assert coeffs(F18, 11) == coeffs(partial((-1) ** k * x ** (2 * k + 1) / ((2 * k + 1) * sp.factorial(2 * k + 1)), 0, 6), 11)
expect(18, "sum from n=0 to infinity of (-1)^n*x^(2n+1)/((2n+1)*(2n+1)!)")

# --- series -> number, each evaluated directly -------------------------------------
assert sp.simplify(sp.summation(n * x ** n, (n, 1, sp.oo)).rewrite(sp.Pow)
                   .subs(x, sp.Rational(1, 2))) == 2
assert sp.summation(n * sp.Rational(1, 2) ** n, (n, 1, sp.oo)) == 2
expect(19, "2")

assert sp.summation(sp.Rational(1, 2) ** n / n, (n, 1, sp.oo)) == sp.log(2)
expect(20, "ln(2)")

assert sp.summation((-1) ** k / (2 * k + 1), (k, 0, sp.oo)) == sp.pi / 4
assert sp.atan(1) == sp.pi / 4
expect(21, "pi/4")

assert sp.summation((-1) ** (n + 1) / n, (n, 1, sp.oo)) == sp.log(2)
expect(22, "ln(2)")

assert sp.summation((-1) ** k / 3 ** k, (k, 0, sp.oo)) == sp.Rational(3, 4)
expect(23, "3/4")

assert sp.summation(1 / sp.factorial(k), (k, 0, sp.oo)) == sp.E
expect(24, "e")

# q25  sum n(n-1)x^n = 2x^2/(1-x)^3, evaluated at x = 1/2
assert sp.simplify(2 * sp.Rational(1, 2) ** 2 / (1 - sp.Rational(1, 2)) ** 3) == 4
assert sp.summation(n * (n - 1) * sp.Rational(1, 2) ** n, (n, 2, sp.oo)) == 4
expect(25, "4")

print("c10_15: all 25 keys verified")
