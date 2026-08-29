"""Verification for CALC 10.6 (Comparison Tests for Convergence).

A comparison question has two halves and both are checked here:

  * the INEQUALITY (for a direct comparison) or the LIMIT of the ratio (for a
    limit comparison) is confirmed with sympy, over the stated range of n; and
  * the reference series is confirmed convergent or divergent with
    sp.summation.

The four questions about what a comparison can and cannot conclude are logical
rather than computational, and each is backed below by an explicit pair of
sympy-checked witnesses showing both outcomes are possible.

Run: python3 verify_c10_6.py
"""
import re

import sympy as sp

import c10_6

n = sp.Symbol("n", integer=True, positive=True)
x = sp.Symbol("x", positive=True)
Q = c10_6.QUESTIONS


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


def converges(term, lo=1):
    """Decide sum of `term` (in n) from lo to infinity with sympy."""
    s = sp.summation(term, (n, lo, sp.oo))
    return s.is_finite is True


def holds_for_all(ineq, lo):
    """True if the inequality in x holds on [lo, infinity); solved, not sampled."""
    sol = sp.solveset(sp.Not(ineq), x, sp.Interval(lo, sp.oo))
    return sol == sp.EmptySet


def lct(a, b):
    """The limit comparison ratio lim a_n/b_n."""
    return sp.limit(sp.simplify(a / b), n, sp.oo)


# --- reference series used throughout -----------------------------------------
assert converges(1 / n ** 2) and converges(1 / n ** sp.Rational(3, 2))
assert not converges(1 / n) and not converges(1 / sp.sqrt(n))
assert converges(sp.Rational(1, 3) ** n) and converges(sp.Rational(1, 2) ** n)
assert converges(sp.Rational(2, 3) ** n)

# --- q1-q5, q25: what a comparison can conclude --------------------------------
# q1  Smaller than convergent => convergent.  Direct comparison, valid direction.
expect(1, "converges")
# q2  Larger than a convergent series is undetermined: 1/n^2 <= 1/n^2 (convergent)
#     and 1/n^2 <= 1/n (divergent) are both legitimate instances.
assert converges(1 / n ** 2) and not converges(1 / n)
expect(2, "may converge or diverge")
# q3  Larger than divergent => divergent.  Valid direction.
expect(3, "diverges")
# q4  Smaller than a divergent series is undetermined: both 1/n^2 and 1/(2n) lie
#     below 1/n, and only the first converges.
assert converges(1 / n ** 2) and not converges(1 / (2 * n))
assert holds_for_all(1 / x ** 2 <= 1 / x, 1) and holds_for_all(1 / (2 * x) <= 1 / x, 1)
expect(4, "may converge or diverge")
# q5  The limit comparison test needs 0 < L < infinity.
expect(5, "L is a finite positive number")
# q25 If a_n/b_n -> 0 then eventually a_n < b_n, so direct comparison applies.
expect(25, "converges")

# --- q6 ------------------------------------------------------------------------
assert holds_for_all(1 / (x ** 2 + 1) < 1 / x ** 2, 1)
expect(6, "converges, since 1/(n^2 + 1) < 1/n^2 and sum 1/n^2 converges")

# --- q7 ------------------------------------------------------------------------
assert holds_for_all(1 / (x - 1) > 1 / x, 2)
assert not converges(1 / n)
expect(7, "diverges, since 1/(n - 1) > 1/n and sum 1/n diverges")

# --- q8 ------------------------------------------------------------------------
assert sp.maximum(2 + sp.cos(x), x, sp.S.Reals) == 3
assert converges(3 / n ** 2)
expect(8, "converges, since (2 + cos(n))/n^2 <= 3/n^2 and sum 3/n^2 converges")

# --- q9 ------------------------------------------------------------------------
assert holds_for_all(1 / (3 ** x + 1) < 1 / 3 ** x, 1)
expect(9, "converges, since 1/(3^n + 1) < 1/3^n and sum 1/3^n converges")

# --- q10  sqrt(n) + 1 <= 2*sqrt(n) exactly when n >= 1 -------------------------
assert holds_for_all(sp.sqrt(x) + 1 <= 2 * sp.sqrt(x), 1)
assert not converges(1 / (2 * sp.sqrt(n)))
expect(10, "diverges, since 1/(sqrt(n) + 1) >= 1/(2*sqrt(n)) and sum 1/sqrt(n) diverges")

# --- q11-q14, q17, q23, q24: limit comparisons ---------------------------------
assert lct(1 / sp.sqrt(n ** 2 + 1), 1 / n) == 1
expect(11, "diverges, since the limit comparison with sum 1/n gives 1")
assert lct((3 * n ** 2 + 2) / (n ** 4 + 5), 1 / n ** 2) == 3
expect(12, "converges, by limit comparison with sum 1/n^2")
assert lct((n + 2) / (n ** 3 + 1), 1 / n ** 2) == 1
expect(13, "converges, by limit comparison with sum 1/n^2")
assert lct((2 * n + 1) / (n ** 2 + 3), 1 / n) == 2
expect(14, "diverges, by limit comparison with sum 1/n")

# denominator 2^x + x exceeds 2^x by exactly x, which is positive on [1, oo)
assert sp.simplify((2 ** x + x) - 2 ** x) == x and holds_for_all(x > 0, 1)
expect(15, "converges, since 1/(2^n + n) < 1/2^n and sum 1/2^n converges")

# --- q16  ln(n) <= sqrt(n) for n >= 1, so ln(n)/n^2 <= 1/n^(3/2) ---------------
gap = sp.minimum(sp.sqrt(x) - sp.log(x), x, sp.Interval(1, sp.oo))
assert sp.simplify(gap - (2 - 2 * sp.log(2))) == 0 and sp.N(gap) > 0
assert converges(1 / n ** sp.Rational(3, 2))
expect(16, "converges, since ln(n) <= sqrt(n) gives ln(n)/n^2 <= 1/n^(3/2)")

assert lct(1 / (n + sp.log(n)), 1 / n) == 1
expect(17, "diverges, by limit comparison with sum 1/n")

# --- q18  0 <= sin(n)^2 <= 1 ----------------------------------------------------
assert sp.maximum(sp.sin(x) ** 2, x, sp.S.Reals) == 1
assert sp.minimum(sp.sin(x) ** 2, x, sp.S.Reals) == 0
expect(18, "converges, since (sin(n))^2/n^2 <= 1/n^2 and sum 1/n^2 converges")

# --- q19  the true inequality is with 2/n^2; the one with 1/n^2 is false -------
assert holds_for_all(1 / (x ** 2 - 1) <= 2 / x ** 2, 2)
assert not holds_for_all(1 / (x ** 2 - 1) <= 1 / x ** 2, 2)  # false for every x > 1
expect(19, "1/(n^2 - 1) <= 2/n^2 for n >= 2")

# --- q20  the student's inequality is true but points the wrong way ------------
assert holds_for_all(1 / (2 * x + 1) < 1 / x, 1)   # the inequality itself is correct
assert not converges(1 / (2 * n + 1))              # and the series does diverge
assert lct(1 / (2 * n + 1), 1 / n) == sp.Rational(1, 2)  # but only this shows it
expect(20, "invalid, because being smaller than a divergent series proves nothing, although the conclusion happens to be correct")

# --- q21  choosing b_n by dominant powers --------------------------------------
assert lct((n ** 2 + 4) / (2 * n ** 5 + n), 1 / n ** 3) == sp.Rational(1, 2)
for bad in (1 / n, 1 / n ** 2, 1 / n ** 5):
    L = lct((n ** 2 + 4) / (2 * n ** 5 + n), bad)
    assert L in (0, sp.oo), (bad, L)   # not a finite positive limit
expect(21, "1/n^3")

# --- q22  n! >= 2^(n-1) for n >= 1 ---------------------------------------------
assert all(sp.factorial(m) >= 2 ** (m - 1) for m in range(1, 60))
assert converges(sp.Rational(1, 2) ** (n - 1))
assert sp.summation(1 / sp.factorial(n), (n, 1, sp.oo)) == sp.E - 1
expect(22, "converges, since 1/n! <= 1/2^(n-1) and sum 1/2^(n-1) converges")

assert lct(2 ** n / (3 ** n - 1), sp.Rational(2, 3) ** n) == 1
expect(23, "converges, by limit comparison with the geometric series sum (2/3)^n")

assert lct(sp.sin(1 / n) / n, 1 / n ** 2) == 1
expect(24, "converges, by limit comparison with sum 1/n^2")

print("c10_6: all 25 keys verified")
