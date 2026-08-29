"""Verification for CALC 10.3 (The nth Term Test for Divergence).

Each computational item reduces to a limit of the general term, computed with
sp.limit.  The items about what the test can and cannot conclude are logical,
not computational; the reasoning is given in comments, and the two directions
are pinned down by explicit sympy witnesses:

  * lim a_n != 0  =>  divergence          (q3, q4, q6 ... )
  * lim a_n =  0  =>  no conclusion       (witnessed by 1/n, which diverges,
                                           and 1/n^2, which converges, both
                                           with terms tending to 0)

Run: python3 verify_c10_3.py
"""
import re

import sympy as sp

import c10_3

n = sp.Symbol("n", positive=True)
m = sp.Symbol("m", integer=True, positive=True)
Q = c10_3.QUESTIONS


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

# --- the two witnesses that make "inconclusive" the right word ----------------
assert sp.limit(1 / n, n, sp.oo) == 0 and sp.summation(1 / m, (m, 1, sp.oo)) is sp.oo
assert sp.limit(1 / n ** 2, n, sp.oo) == 0
assert sp.summation(1 / m ** 2, (m, 1, sp.oo)) == sp.pi ** 2 / 6

# q1  Statement of the test.  Note choice D is the (true but different)
#     contrapositive-of-the-converse; the test itself is the implication in B.
expect(1, "if lim as n -> infinity of a_n is not 0 or does not exist, then sum a_n diverges")
# q2  The witnesses above show both outcomes occur when lim a_n = 0.
expect(2, "nothing; the test is inconclusive")

assert sp.limit(n / (2 * n + 1), n, sp.oo) == sp.Rational(1, 2) != 0
expect(3, "diverges by the nth term test")
assert sp.limit((3 * n ** 2 + 1) / (n ** 2 + 5), n, sp.oo) == 3
expect(4, "diverges")

# q5  Terms -> 0, so the test is inconclusive here even though the series diverges.
expect(5, "nothing; the terms approach 0 so the test is inconclusive")

# q6, q7  (-1)^n and cos(n*pi) = (-1)^n take only the values 1 and -1
assert {(-1) ** j for j in range(6)} == {1, -1}
assert all(sp.cos(j * sp.pi) == (-1) ** j for j in range(8))
expect(6, "diverges, because the terms do not approach a limit")
expect(7, "diverges by the nth term test")

assert sp.limit(n / sp.log(n), n, sp.oo) is sp.oo
expect(8, "diverges, because the terms increase without bound")
assert sp.limit((1 + 1 / n) ** n, n, sp.oo) == sp.E
expect(9, "diverges, because the terms approach e")
assert sp.limit(n * sp.sin(1 / n), n, sp.oo) == 1
expect(10, "diverges, because the terms approach 1")

# q11  2^n/n! -> 0, so the test is inconclusive; the series does converge.
assert sp.limit(2 ** m / sp.factorial(m), m, sp.oo) == 0
assert sp.summation(2 ** m / sp.factorial(m), (m, 1, sp.oo)) == sp.E ** 2 - 1
expect(11, "is inconclusive, because the terms approach 0")

# q12  Only one of the four has a nonzero term limit.
assert sp.limit(1 / n, n, sp.oo) == 0
assert sp.limit(1 / sp.sqrt(n), n, sp.oo) == 0
assert sp.limit(1 / n ** 2, n, sp.oo) == 0
assert sp.limit(n / (n + 4), n, sp.oo) == 1
expect(12, "sum from n=1 to infinity of n/(n+4)")

# q13  1/n^2 converges (value pi^2/6 above) but not by the nth term test.
expect(13, "the nth term test can never establish convergence")

assert sp.limit(sp.log(n) / n, n, sp.oo) == 0
assert sp.integrate(sp.log(n) / n, (n, 2, sp.oo)) is sp.oo  # the series really diverges
expect(14, "is inconclusive, since the terms approach 0")

assert sp.limit(sp.exp(-n), n, sp.oo) == 0
assert sp.simplify(sp.summation(sp.exp(-m), (m, 1, sp.oo)) - 1 / (sp.E - 1)) == 0
expect(15, "is inconclusive")

assert sp.limit(sp.factorial(m) / 2 ** m, m, sp.oo) is sp.oo
expect(16, "diverges, because the terms increase without bound")
assert sp.limit(sp.atan(n), n, sp.oo) == sp.pi / 2
expect(17, "diverges, because the terms approach pi/2")
assert sp.limit(n ** 2 / 2 ** n, n, sp.oo) == 0
expect(18, "is inconclusive, since the terms approach 0")
assert sp.limit(sp.sqrt(n) / (sp.sqrt(n) + 1), n, sp.oo) == 1
expect(19, "diverges")
assert sp.limit((5 * n ** 3 - 2) / (3 * n ** 3 + n), n, sp.oo) == sp.Rational(5, 3)
expect(20, "diverges")

# q21  sin(n) has no limit: sympy reports the accumulation bounds [-1, 1], and
#      integer arguments really do come arbitrarily close to both ends.
assert sp.limit(sp.sin(n), n, sp.oo) == sp.AccumBounds(-1, 1)
assert max(sp.sin(j) for j in range(1, 400)) > sp.Float("0.999")
assert min(sp.sin(j) for j in range(1, 400)) < sp.Float("-0.999")
expect(21, "diverges, because lim as n -> infinity of sin(n) does not exist")

# q22  Contrapositive of the test: a_n = S_n - S_(n-1) -> L - L = 0.
Sn = 5 - 1 / n
assert sp.limit(Sn - Sn.subs(n, n - 1), n, sp.oo) == 0
expect(22, "equals 0")
# q23  The harmonic series is the standard counterexample (checked above).
expect(23, "False; the harmonic series sum 1/n is a counterexample")

assert sp.limit((1 - 1 / n) ** n, n, sp.oo) == sp.exp(-1)
assert sp.exp(-1) != 0
expect(24, "diverges, because the terms approach 1/e")

# q25  n^p fails to approach 0 exactly for p >= 0.
assert sp.limit(n ** 0, n, sp.oo) == 1
for p in (sp.Rational(1, 2), 1, 3):
    assert sp.limit(n ** p, n, sp.oo) is sp.oo
for p in (sp.Rational(-1, 2), -1, -3):
    assert sp.limit(n ** p, n, sp.oo) == 0
expect(25, "p >= 0")

print("c10_3: all 25 keys verified")
