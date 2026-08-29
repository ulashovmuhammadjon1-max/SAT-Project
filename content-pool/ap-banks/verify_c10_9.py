"""Verification for CALC 10.9 (Determining Absolute or Conditional Convergence).

Each classification is settled twice with sympy:

  * the ABSOLUTE series -- convergent or divergent, by sp.summation, by the
    integral test (sp.integrate), or by a checked comparison; and
  * the SIGNED series -- convergent by the alternating series test (b_n shown
    decreasing via the sign of the derivative, and b_n -> 0 via sp.limit), or
    divergent because b_n does not approach 0.

"Absolutely convergent" requires the first to converge; "conditionally
convergent" requires the first to diverge and the second to converge.

Run: python3 verify_c10_9.py
"""
import re

import sympy as sp

import c10_9

n = sp.Symbol("n", integer=True, positive=True)
x = sp.Symbol("x", positive=True)
Q = c10_9.QUESTIONS


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


def decreasing_to_zero(b, lo=1):
    """AST hypotheses for b (a function of n), checked on [lo, oo)."""
    d = sp.simplify(sp.diff(b.subs(n, x), x))
    sol = sp.solveset(d >= 0, x, sp.Interval.open(lo, sp.oo))
    if isinstance(sol, sp.ConditionSet):
        raise RuntimeError(f"solveset inconclusive for {d}")
    return sol == sp.EmptySet and sp.limit(b.subs(n, x), x, sp.oo) == 0


def abs_converges(b, lo=1):
    """Convergence of sum b_n (b_n >= 0), decided by sp.summation."""
    return sp.summation(b, (n, lo, sp.oo)).is_finite is True


# --- q1, q2, q3, q18: the definitions ------------------------------------------
expect(1, "sum |a_n| converges")
expect(2, "sum a_n converges but sum |a_n| diverges")
# q3  Absolute convergence implies convergence: 0 <= a_n + |a_n| <= 2|a_n|, so
#     sum (a_n + |a_n|) converges by comparison and a_n = (a_n + |a_n|) - |a_n|.
expect(3, "converges")
expect(18, "conditionally convergent")

# --- the conditional cases -----------------------------------------------------
assert decreasing_to_zero(1 / n) and not abs_converges(1 / n)
expect(4, "converges conditionally")
assert decreasing_to_zero(1 / sp.sqrt(n)) and not abs_converges(1 / sp.sqrt(n))
expect(6, "converges conditionally")

# q11  ln(n)/n decreases past e; sum ln(n)/n diverges by the integral test
assert decreasing_to_zero(sp.log(n) / n, 3)
assert sp.integrate(sp.log(x) / x, (x, 2, sp.oo)) is sp.oo
expect(11, "converges conditionally")

# q12  1/ln(n) decreases to 0, and exceeds 1/n since ln(x) < x on [2, oo)
assert decreasing_to_zero(1 / sp.log(n), 2)
assert sp.minimum(x - sp.log(x), x, sp.Interval(2, sp.oo)) > 0
assert not abs_converges(1 / n, 2)
expect(12, "converges conditionally")

# q13  1/(2n-1) >= 1/(2n), and sum 1/(2n) diverges
assert decreasing_to_zero(1 / (2 * n - 1))
assert sp.solveset(sp.Not(1 / (2 * x - 1) >= 1 / (2 * x)), x, sp.Interval(1, sp.oo)) == sp.EmptySet
assert not abs_converges(1 / (2 * n))
assert sp.summation((-1) ** (n + 1) / (2 * n - 1), (n, 1, sp.oo)) == sp.pi / 4
expect(13, "converges conditionally")

# q15  2n/(n^2+1) decreases to 0; limit comparison with 1/n gives 2
assert decreasing_to_zero(2 * n / (n ** 2 + 1))
assert sp.limit((2 * n / (n ** 2 + 1)) / (1 / n), n, sp.oo) == 2
assert sp.integrate(2 * x / (x ** 2 + 1), (x, 1, sp.oo)) is sp.oo
expect(15, "converges conditionally")

# q22  1/(n ln n): derivative -(1 + ln x)/(x ln x)^2 < 0 for x >= 2
assert sp.simplify(sp.diff(1 / (x * sp.log(x)), x) + (1 + sp.log(x)) / (x * sp.log(x)) ** 2) == 0
assert sp.minimum(1 + sp.log(x), x, sp.Interval(2, sp.oo)) == 1 + sp.log(2)
assert sp.limit(1 / (x * sp.log(x)), x, sp.oo) == 0
assert sp.integrate(1 / (x * sp.log(x)), (x, 2, sp.oo)) is sp.oo
expect(22, "converges conditionally")

# --- the absolute cases --------------------------------------------------------
assert sp.summation(1 / n ** 2, (n, 1, sp.oo)) == sp.pi ** 2 / 6
expect(5, "converges absolutely")
assert abs_converges(1 / n ** 3)
expect(7, "converges absolutely")
assert sp.summation(1 / sp.factorial(n), (n, 1, sp.oo)) == sp.E - 1
expect(9, "converges absolutely")
assert sp.summation(sp.Rational(1, 2) ** n, (n, 1, sp.oo)) == 1
expect(10, "converges absolutely")

# q14  |sin(n)| <= 1, so the absolute series is dominated by 1/n^2
assert sp.maximum(sp.sin(x) ** 2, x, sp.S.Reals) == 1  # so |sin(x)| <= 1
expect(14, "converges absolutely, since |sin(n)|/n^2 <= 1/n^2")

# q16  ratio test on absolute values
assert sp.limit(sp.simplify(3 ** (n + 1) / sp.factorial(n + 1) * sp.factorial(n) / 3 ** n), n, sp.oo) == 0
assert sp.summation(3 ** n / sp.factorial(n), (n, 1, sp.oo)) == sp.E ** 3 - 1
expect(16, "converges absolutely")

# q23  |cos(n)| <= 1, dominated by 1/n^3
assert sp.maximum(sp.cos(x) ** 2, x, sp.S.Reals) == 1  # so |cos(x)| <= 1
assert abs_converges(1 / n ** 3)
expect(23, "converges absolutely")

# q24  arctan(n) < pi/2 for every n
assert sp.limit(sp.atan(x), x, sp.oo) == sp.pi / 2
assert sp.solveset(sp.Not(sp.atan(x) < sp.pi / 2), x, sp.Interval(1, sp.oo)) == sp.EmptySet
assert abs_converges(sp.pi / (2 * n ** 2))
expect(24, "converges absolutely, since arctan(n)/n^2 <= (pi/2)/n^2")

# --- the divergent case --------------------------------------------------------
assert sp.limit(x / (x + 1), x, sp.oo) == 1  # terms do not approach 0
expect(8, "diverges")

# --- q17, q19, q20, q21, q25 ---------------------------------------------------
# q17  Both remaining outcomes really occur when sum |a_n| diverges:
#      sum (-1)^n/n converges (conditionally) and sum 1/n diverges.
assert not abs_converges(1 / n) and decreasing_to_zero(1 / n)
expect(17, "may converge conditionally or may diverge")

# q19, q20  the p ranges, recomputed on both sides
for p in (sp.Rational(1, 4), sp.Rational(1, 2), 1):
    assert decreasing_to_zero(1 / n ** p) and not abs_converges(1 / n ** p), p
for p in (sp.Rational(11, 10), 2, 3):
    assert abs_converges(1 / n ** p), p
for p in (0, sp.Rational(-1, 2)):
    assert sp.limit(x ** -p, x, sp.oo) != 0, p   # not even convergent
expect(19, "0 < p <= 1")
expect(20, "p > 1")

# q21  sum (-1)^n/n^2 is alternating and absolutely convergent
expect(21, "False; sum (-1)^n/n^2 converges absolutely")

# q25  Riemann's rearrangement theorem.  Not a computation; the statement is
#      that absolute convergence is rearrangement-invariant while a
#      conditionally convergent series can be rearranged to any real sum.
#      The two ingredients that make it possible for sum (-1)^n/n: the positive
#      part and the negative part each diverge on their own.
assert sp.summation(1 / (2 * n), (n, 1, sp.oo)) is sp.oo
assert sp.summation(1 / (2 * n - 1), (n, 1, sp.oo)) is sp.oo
expect(25, "The terms of an absolutely convergent series may be rearranged without changing the sum, but a conditionally convergent series can be rearranged to sum to any value")

print("c10_9: all 25 keys verified")
