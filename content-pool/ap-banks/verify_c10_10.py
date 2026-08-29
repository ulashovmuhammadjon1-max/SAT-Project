"""Verification for CALC 10.10 (Alternating Series Error Bound).

Every numeric key is recomputed as b_(n+1) -- the first omitted term -- and,
where the exact sum is known to sympy (ln 2, pi/4, 1/e, 1/3), the TRUE error is
also computed and checked to be no larger than the bound.  That second check is
what would catch an off-by-one in the index of the first omitted term, which is
the single most common way this topic goes wrong.

Run: python3 verify_c10_10.py
"""
import re

import sympy as sp

import c10_10

n = sp.Symbol("n", integer=True, positive=True)
Q = c10_10.QUESTIONS


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


def smallest_n(bound_of_n, tol):
    """Smallest n >= 1 with bound_of_n(n) <= tol."""
    m = 1
    while bound_of_n(m) > tol:
        m += 1
        assert m < 100000
    return m


# --- exact sums used as ground truth -------------------------------------------
alt_harm = sp.summation((-1) ** (n + 1) / n, (n, 1, sp.oo))
assert alt_harm == sp.log(2)
k = sp.Symbol("k", integer=True, nonnegative=True)
assert sp.summation((-1) ** k / (2 * k + 1), (k, 0, sp.oo)) == sp.pi / 4
assert sp.summation((-1) ** k / sp.factorial(k), (k, 0, sp.oo)) == sp.exp(-1)
assert sp.summation((-1) ** (n + 1) / 2 ** n, (n, 1, sp.oo)) == sp.Rational(1, 3)

# q1  The bound is the first omitted term.
expect(1, "b_(n+1)")

# q2  four terms of the alternating harmonic series: bound b_5 = 1/5
S4 = sp.summation((-1) ** (n + 1) / n, (n, 1, 4))
assert S4 == sp.Rational(7, 12)
assert sp.Abs(sp.log(2) - S4) < sp.Rational(1, 5)
expect(2, "1/5")

# q3  1/(n+1) <= 1/100 first at n = 99
assert smallest_n(lambda m: sp.Rational(1, m + 1), sp.Rational(1, 100)) == 99
expect(3, "99")

# q4  five terms of sum (-1)^n/n^2: bound b_6 = 1/36
S5 = sp.summation((-1) ** n / n ** 2, (n, 1, 5))
true4 = sp.summation((-1) ** n / n ** 2, (n, 1, sp.oo))
assert sp.Abs(true4 - S5) < sp.Rational(1, 36)
expect(4, "1/36")

# q5  four terms (k = 0..3) of the Leibniz series: bound is the k = 4 term, 1/9
S_leib = sp.summation((-1) ** k / (2 * k + 1), (k, 0, 3))
assert sp.Abs(sp.pi / 4 - S_leib) < sp.Rational(1, 9)
expect(5, "1/9")

# q6, q7  sign of the error, and the bracketing of S by consecutive partial sums
for m in range(1, 9):
    Sm = sp.summation((-1) ** (n + 1) / n, (n, 1, m))
    nxt = (-1) ** (m + 2) / sp.Integer(m + 1)          # the first omitted term
    assert sp.sign(sp.log(2) - Sm) == sp.sign(nxt), m
    Sm1 = Sm + nxt
    assert sp.Min(Sm, Sm1) < sp.log(2) < sp.Max(Sm, Sm1), m
expect(6, "has the same sign as the first omitted term")
expect(7, "always lies between S_n and S_(n+1)")

# q8  1/(n+1)^3 <= 1/1000 first at n = 9
assert smallest_n(lambda m: sp.Rational(1, (m + 1) ** 3), sp.Rational(1, 1000)) == 9
expect(8, "9")

# q9  1/(N+1)! <= 1/1000 first at N = 6, since 6! = 720 and 7! = 5040
assert sp.factorial(6) == 720 and sp.factorial(7) == 5040
assert smallest_n(lambda m: 1 / sp.factorial(m + 1), sp.Rational(1, 1000)) == 6
S6 = sp.summation((-1) ** k / sp.factorial(k), (k, 0, 6))
assert sp.Abs(sp.exp(-1) - S6) < sp.Rational(1, 1000)
expect(9, "6")

# q10, q11, q12, q16, q21: the hypotheses and the contrast with Lagrange
expect(10, "the terms alternate in sign, decrease in absolute value, and approach 0")
# q11  sum 1/n^2 has positive terms, so no alternating bound is available; the
#      integral test remainder bound (10.4) is the right tool there.
expect(11, "invalid, since the series is not alternating")
expect(12, "The alternating series error bound")
# q16  the omitted tail is b_(n+1) - (b_(n+2) - b_(n+3) + ...) with the
#      subtracted quantity strictly positive when b_n strictly decreases;
#      the alternating harmonic series shows the strict inequality numerically.
for m in range(1, 9):
    Sm = sp.summation((-1) ** (n + 1) / n, (n, 1, m))
    assert sp.Abs(sp.log(2) - Sm) < sp.Rational(1, m + 1), m
expect(16, "strictly less than it")
# q21  A failed hypothesis removes the theorem that produced the bound.
expect(21, "is not justified, since the hypotheses of the alternating series test fail")

# q13  ten terms: bound b_11 = 1/11
S10 = sp.summation((-1) ** (n + 1) / n, (n, 1, 10))
assert sp.Abs(sp.log(2) - S10) < sp.Rational(1, 11)
expect(13, "1/11")

# q14  b_n = 1/(n 2^n): b_4 = 1/64
b14 = lambda m: sp.Rational(1, m * 2 ** m)
assert b14(4) == sp.Rational(1, 64)
expect(14, "1/64")

# q15  b_n = 1/(n^2+1): b_6 = 1/37
assert sp.Rational(1, 6 ** 2 + 1) == sp.Rational(1, 37)
expect(15, "1/37")

# q17  three terms: S_3 = 5/6, bound b_4 = 1/4, and the true error is smaller
S3 = sp.summation((-1) ** (n + 1) / n, (n, 1, 3))
assert S3 == sp.Rational(5, 6)
assert sp.Abs(sp.log(2) - S3) < sp.Rational(1, 4)
assert sp.N(sp.Abs(sp.log(2) - S3), 4) < sp.Float("0.15")
expect(17, "|S - 5/6| <= 1/4")

# q18  the first omitted term is +1/5, so S_4 underestimates S
assert (-1) ** (4 + 2) / sp.Integer(5) == sp.Rational(1, 5) > 0
assert sp.log(2) > S4
expect(18, "an underestimate, since the next term is +1/5")

# q19  b_n = n/2^n: b_5 = 5/32
assert sp.Rational(5, 2 ** 5) == sp.Rational(5, 32)
expect(19, "5/32")

# q20  1/sqrt(n+1) <= 1/20 first at n = 399
assert smallest_n(lambda m: 1 / sp.sqrt(m + 1), sp.Rational(1, 20)) == 399
expect(20, "399")

# q22  three terms of sum (-1)^(n+1)/2^n: S_3 = 3/8, bound b_4 = 1/16
S3b = sp.summation((-1) ** (n + 1) / 2 ** n, (n, 1, 3))
assert S3b == sp.Rational(3, 8)
assert sp.Abs(sp.Rational(1, 3) - S3b) == sp.Rational(1, 24) < sp.Rational(1, 16)
expect(22, "1/16")

# q23  1/(n+1)^2 <= 1/200 first at n = 14
assert smallest_n(lambda m: sp.Rational(1, (m + 1) ** 2), sp.Rational(1, 200)) == 14
assert 14 ** 2 < 200 <= 15 ** 2
expect(23, "14")

# q24  only one of the four is alternating with b_n decreasing to 0
assert sp.limit(sp.Symbol("t", positive=True) / (sp.Symbol("t", positive=True) + 1),
                sp.Symbol("t", positive=True), sp.oo) == 1          # n/(n+1) fails
assert sp.limit(1 / (n + 1), n, sp.oo) == 0                          # 1/(n+1) works
assert sp.limit((n + 1) / sp.sqrt(n), n, sp.oo) is sp.oo             # last one fails
expect(24, "sum from n=1 to infinity of (-1)^n/(n+1)")

# q25  S_4 and S_5 bracket ln 2
S5b = sp.summation((-1) ** (n + 1) / n, (n, 1, 5))
assert S4 == sp.Rational(7, 12) and S5b == sp.Rational(47, 60)
assert S4 < sp.log(2) < S5b
expect(25, "from 7/12 to 47/60")

print("c10_10: all 25 keys verified")
