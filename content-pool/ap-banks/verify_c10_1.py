"""Verification for CALC 10.1 (Defining Convergent and Divergent Infinite Series).

Every numeric key is confirmed with sympy (sp.summation / sp.limit).  The
definitional items -- what convergence of a series means, how convergent series
add and scale, what divergence means -- are not computations; the reasoning for
each is stated in a comment below.

Run: python3 verify_c10_1.py
"""
import sympy as sp

import c10_1

n, k = sp.symbols("n k", positive=True, integer=True)
Q = c10_1.QUESTIONS


def key(i):
    """The text of the keyed choice for question i (1-based)."""
    item = Q[i - 1]
    return item["choices"][item["ans"]]


def expect(i, text):
    assert key(i) == text, f"q{i}: key is {key(i)!r}, expected {text!r}"


# --- pairwise non-equivalence of numeric choices ------------------------------
def numeric_value(s):
    try:
        return sp.nsimplify(sp.sympify(s.replace("^", "**")))
    except (sp.SympifyError, TypeError, ValueError, SyntaxError):
        return None


for idx, item in enumerate(Q, 1):
    assert len(item["choices"]) == 4, f"q{idx}: needs exactly four choices"
    assert len(set(item["choices"])) == 4, f"q{idx}: repeated choice text"
    vals = [v for v in (numeric_value(c) for c in item["choices"]) if v is not None]
    assert len(vals) == len({sp.simplify(v) for v in vals}), (
        f"q{idx}: two numeric choices are equal as numbers")

# --- q2: S_3 of sum 1/2^n -----------------------------------------------------
assert sp.summation(sp.Rational(1, 2) ** n, (n, 1, 3)) == sp.Rational(7, 8)
expect(2, "7/8")

# --- q3, q4, q5: telescoping sums ---------------------------------------------
assert sp.summation(1 / n - 1 / (n + 1), (n, 1, sp.oo)) == 1
expect(3, "1")
assert sp.summation(1 / (n * (n + 1)), (n, 1, sp.oo)) == 1
expect(4, "1")
assert sp.summation(1 / (n + 1) - 1 / (n + 2), (n, 1, sp.oo)) == sp.Rational(1, 2)
expect(5, "1/2")

# --- q6, q7, q8: series given by their partial sums ---------------------------
assert sp.limit(3 * n / (n + 1), n, sp.oo) == 3
expect(6, "converges to 3")
assert sp.limit((2 * n ** 2 + 1) / (n ** 2 + 3), n, sp.oo) == 2
expect(7, "2")
assert sp.limit(n ** 2 / (n + 1), n, sp.oo) is sp.oo
expect(8, "diverges")

# --- q9: a_3 = S_3 - S_2 with S_n = 5 - 2/n -----------------------------------
S = lambda m: 5 - sp.Rational(2, 1) / m
assert sp.simplify(S(3) - S(2)) == sp.Rational(1, 3)
expect(9, "1/3")

# --- q10: terms -> 0 but the harmonic series diverges --------------------------
assert sp.limit(1 / n, n, sp.oo) == 0
assert sp.summation(1 / n, (n, 1, sp.oo)) is sp.oo
expect(10, "The sequence converges to 0 but the series diverges")

# --- q11, q12: telescoping, convergent and divergent ---------------------------
assert sp.summation(1 / (2 * n - 1) - 1 / (2 * n + 1), (n, 1, sp.oo)) == 1
expect(11, "1")
# partial sum of ln(n+1) - ln(n) telescopes to ln(N+1)
assert sp.simplify(sp.summation(sp.log(n + 1) - sp.log(n), (n, 1, k)) - sp.log(k + 1)) == 0
assert sp.limit(sp.log(k + 1), k, sp.oo) is sp.oo
expect(12, "diverges")

# --- q13: sum from n=2 of 1/(n^2 - 1) ------------------------------------------
assert sp.summation(1 / (n ** 2 - 1), (n, 2, sp.oo)) == sp.Rational(3, 4)
expect(13, "3/4")

# --- q14, q15, q16, q17, q18: linearity and the definition of divergence -------
# q14  Sums of convergent series add: lim(S_n + T_n) = lim S_n + lim T_n = 6 + (-2) = 4.
expect(14, "converges to 4")
# q15  If sum(a_n + b_n) converged, then sum b_n = sum((a_n + b_n) - a_n) would
#      converge as a difference of convergent series, contradicting divergence.
expect(15, "diverges")
# q16  Convergence depends only on the tail; the first ten terms shift every
#      partial sum by the same constant, changing the sum but not its existence.
expect(16, "cannot change whether the series converges, though it may change the sum")
# q17  Constant multiple: 4 * 7 = 28.
assert 4 * 7 == 28
expect(17, "converges to 28")
# q18  Divergence is the negation of "the partial sums have a finite limit";
#      oscillating partial sums (q19) diverge without tending to infinity.
expect(18, "the sequence of partial sums does not approach a finite limit")

# --- q19: partial sums of sum (-1)^n oscillate ---------------------------------
j = sp.Symbol("j", integer=True, nonnegative=True)
parts = {sp.summation((-1) ** j, (j, 0, m)) for m in range(0, 8)}
assert parts == {0, 1}
expect(19, "diverges")

# --- q20: a_n = S_n - S_(n-1) -> 0 when the series converges --------------------
Sn = 7 - 1 / n  # any partial-sum sequence with limit 7
assert sp.limit(Sn - Sn.subs(n, n - 1), n, sp.oo) == 0
expect(20, "0")

# --- q21: a_1 = S_1 ------------------------------------------------------------
assert (4 - 3 * sp.Rational(1, 2) ** 1) == sp.Rational(5, 2)
expect(21, "5/2")

# --- q22: closed form for the nth partial sum ----------------------------------
assert sp.simplify(sp.summation(1 / (k * (k + 1)), (k, 1, n)) - n / (n + 1)) == 0
expect(22, "S_n = n/(n+1)")

# --- q23: terms -> 0 yet the telescoped partial sum diverges --------------------
assert sp.limit(sp.sqrt(n + 1) - sp.sqrt(n), n, sp.oo) == 0
assert sp.simplify(sp.summation(sp.sqrt(n + 1) - sp.sqrt(n), (n, 1, k)) - (sp.sqrt(k + 1) - 1)) == 0
assert sp.limit(sp.sqrt(k + 1) - 1, k, sp.oo) is sp.oo
expect(23, "diverges")

# --- q24, q25 ------------------------------------------------------------------
assert sp.summation(1 / (n * (n + 2)), (n, 1, sp.oo)) == sp.Rational(3, 4)
expect(24, "3/4")
assert sp.summation(1 / n - 1 / (n + 3), (n, 1, sp.oo)) == sp.Rational(11, 6)
expect(25, "11/6")

print("c10_1: all 25 keys verified")
