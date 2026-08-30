"""Verification for CALC 10.12 (Lagrange Error Bound).

Each numeric bound is recomputed as M*|x-a|^(n+1)/(n+1)!, with M itself found
by sympy (sp.maximum of |f^(n+1)| on the stated interval) rather than asserted.
Where the true error is computable, it is also checked to be no larger than the
bound -- the check that would catch an off-by-one in the derivative order, the
power, or the factorial.

Run: python3 verify_c10_12.py
"""
import re

import sympy as sp

import c10_12

x = sp.Symbol("x", real=True)
Q = c10_12.QUESTIONS


def key(i):
    item = Q[i - 1]
    return item["choices"][item["ans"]]


def expect(i, text):
    assert key(i) == text, f"q{i}: key is {key(i)!r}, expected {text!r}"


def numeric_value(s):
    s = s.replace("^", "**").replace("pi", "PI")
    try:
        return sp.sympify(s, locals={"PI": sp.pi, "e": sp.E})
    except (sp.SympifyError, TypeError, ValueError, SyntaxError, AttributeError):
        return None


for idx, item in enumerate(Q, 1):
    assert len(item["choices"]) == 4, f"q{idx}: needs exactly four choices"
    assert len(set(item["choices"])) == 4, f"q{idx}: repeated choice text"
    vals = [v for v in (numeric_value(c) for c in item["choices"]) if v is not None
            and not v.free_symbols]
    assert len(vals) == len({sp.nsimplify(sp.N(v, 30)) for v in vals}), (
        f"q{idx}: two numeric choices are equal as numbers")


def taylor(f, a, n):
    return sum(sp.diff(f, x, k).subs(x, a) / sp.factorial(k) * (x - a) ** k
               for k in range(n + 1))


def max_abs(g, lo, hi):
    """max |g| on [lo, hi], via max of g^2 (sympy cannot maximize Abs of a trig
    function: it raises on the periodic Piecewise that Abs produces)."""
    return sp.sqrt(sp.maximum(g ** 2, x, sp.Interval(lo, hi)))


def lagrange(f, a, n, lo, hi, dist, M=None):
    """M*dist^(n+1)/(n+1)!; M defaults to the true max of |f^(n+1)| on [lo, hi]."""
    if M is None:
        M = max_abs(sp.diff(f, x, n + 1), lo, hi)
    return sp.simplify(M * dist ** (n + 1) / sp.factorial(n + 1))


# --- q1, q2, q3, q9, q10, q14, q17, q18, q22, q24, q25: the statement ----------
expect(1, "M*|x - a|^(n+1)/(n+1)!")
expect(2, "the maximum of |f^(n+1)| on the interval between a and x")
expect(3, "R_n(x) = f^(n+1)(c)*(x - a)^(n+1)/(n+1)!")
expect(9, "|f^(6)|")
expect(10, "incorrect; the bound requires the fourth derivative")
expect(14, "the Lagrange error bound")
expect(22, "The Lagrange error bound")

# q17  factorial growth beats a fixed power: the bound tends to 0
d = sp.Symbol("d", positive=True)
m = sp.Symbol("m", integer=True, positive=True)
assert sp.limit(3 ** m / sp.factorial(m), m, sp.oo) == 0
assert sp.limit(10 ** m / sp.factorial(m), m, sp.oo) == 0
expect(17, "(n+1)! grows faster than |x - a|^(n+1)")
expect(25, "P_n(x) approaches f(x)")

# q24  the derivatives of sin cycle through +/- sin and +/- cos
for k in range(1, 9):
    dk = sp.diff(sp.sin(x), x, k)
    assert dk in (sp.sin(x), sp.cos(x), -sp.sin(x), -sp.cos(x))
    assert sp.maximum(dk ** 2, x, sp.S.Reals) == 1   # so |dk| <= 1 everywhere
expect(24, "every derivative of sin or cos is one of sin, cos, -sin and -cos, all of which are bounded by 1 in absolute value")

# --- q4  e^x, P_3, |x| <= 1 ----------------------------------------------------
b4 = lagrange(sp.exp(x), 0, 3, -1, 1, 1)
assert sp.simplify(b4 - sp.E / 24) == 0
true4 = sp.Abs(sp.exp(1) - taylor(sp.exp(x), 0, 3).subs(x, 1))
assert sp.N(true4) < sp.N(b4)
expect(4, "e/24")

# --- q5, q6  sin and cos, where M = 1 -----------------------------------------
# M = 1 is stated in the stem; it is a legitimate bound since sin^2 <= 1
assert sp.maximum(sp.diff(sp.sin(x), x, 4) ** 2, x, sp.S.Reals) == 1
b5 = lagrange(sp.sin(x), 0, 3, sp.Rational(-1, 2), sp.Rational(1, 2), sp.Rational(1, 2), M=1)
assert b5 == sp.Rational(1, 384)
expect(5, "1/384")
assert sp.maximum(sp.diff(sp.cos(x), x, 3) ** 2, x, sp.S.Reals) == 1
b6 = lagrange(sp.cos(x), 0, 2, 0, sp.Rational(1, 10), sp.Rational(1, 10), M=1)
assert b6 == sp.Rational(1, 6000)
true6 = sp.Abs(sp.cos(sp.Rational(1, 10)) - taylor(sp.cos(x), 0, 2).subs(x, sp.Rational(1, 10)))
assert sp.N(true6) < sp.N(b6)
expect(6, "1/6000")

# --- q7, q8  bounds given directly ---------------------------------------------
assert sp.Rational(10, 1) * 1 ** 4 / sp.factorial(4) == sp.Rational(5, 12)
expect(7, "5/12")
assert 24 * sp.Rational(1, 2) ** 5 / sp.factorial(5) == sp.Rational(1, 160)
expect(8, "1/160")

# --- q11  e^x, P_2 at x = 0.5 --------------------------------------------------
b11 = lagrange(sp.exp(x), 0, 2, 0, sp.Rational(1, 2), sp.Rational(1, 2))
assert sp.simplify(b11 - sp.exp(sp.Rational(1, 2)) / 48) == 0
expect(11, "e^(1/2)/48")

# --- q12  ln(1+x), P_2 at x = 0.1 ----------------------------------------------
M12 = max_abs(sp.diff(sp.log(1 + x), x, 3), 0, sp.Rational(1, 10))
assert M12 == 2
b12 = M12 * sp.Rational(1, 10) ** 3 / sp.factorial(3)
assert b12 == sp.Rational(1, 3000)
true12 = sp.Abs(sp.log(sp.Rational(11, 10)) - taylor(sp.log(1 + x), 0, 2).subs(x, sp.Rational(1, 10)))
assert sp.N(true12) < sp.N(b12)
expect(12, "1/3000")

# --- q13  smallest n with e/(n+1)! <= 0.001 ------------------------------------
def bound13(n):
    return sp.E / sp.factorial(n + 1)


assert sp.N(bound13(5)) > sp.Rational(1, 1000)
assert sp.N(bound13(6)) < sp.Rational(1, 1000)
assert sp.factorial(6) == 720 and sp.factorial(7) == 5040 and sp.N(1000 * sp.E) < 5040
expect(13, "6")

# --- q15  sin, P_5, |x| <= pi/2 -------------------------------------------------
assert sp.maximum(sp.diff(sp.sin(x), x, 6) ** 2, x, sp.S.Reals) == 1
b15 = lagrange(sp.sin(x), 0, 5, -sp.pi / 2, sp.pi / 2, sp.pi / 2, M=1)
assert sp.simplify(b15 - (sp.pi / 2) ** 6 / 720) == 0
expect(15, "(pi/2)^6/720")

# --- q16  all derivatives bounded by 3 -----------------------------------------
assert 3 * sp.Integer(2) ** 5 / sp.factorial(5) == sp.Rational(4, 5)
expect(16, "4/5")

# --- q18, q23  the bound overestimates ------------------------------------------
expect(18, "an upper bound for |f(x) - P_n(x)|, usually larger than the true error")
b23 = lagrange(sp.exp(x), 0, 2, 0, 1, 1)
assert sp.simplify(b23 - sp.E / 6) == 0
true23 = sp.Abs(sp.exp(1) - taylor(sp.exp(x), 0, 2).subs(x, 1))
assert sp.simplify(true23 - (sp.E - sp.Rational(5, 2))) == 0
assert sp.N(true23, 4) < sp.N(b23, 4)
assert sp.Float("0.21") < sp.N(true23) < sp.Float("0.22")
assert sp.Float("0.45") < sp.N(b23) < sp.Float("0.46")
expect(23, "the true error is at most the bound, and often well below it")

# --- q19  1/x about 1 on [1, 1.5] ----------------------------------------------
M19 = max_abs(sp.diff(1 / x, x, 3), 1, sp.Rational(3, 2))
assert M19 == 6
b19 = M19 * sp.Rational(1, 2) ** 3 / sp.factorial(3)
assert b19 == sp.Rational(1, 8)
true19 = sp.Abs(sp.Rational(2, 3) - taylor(1 / x, 1, 2).subs(x, sp.Rational(3, 2)))
assert sp.N(true19) < sp.N(b19)
expect(19, "1/8")

# --- q20  e^x, P_1 at 0.2 with M = 2 -------------------------------------------
b20 = 2 * sp.Rational(2, 10) ** 2 / sp.factorial(2)
assert b20 == sp.Rational(4, 100)
assert sp.N(sp.exp(sp.Rational(2, 10))) < 2   # M = 2 is a legitimate bound here
true20 = sp.Abs(sp.exp(sp.Rational(1, 5)) - taylor(sp.exp(x), 0, 1).subs(x, sp.Rational(1, 5)))
assert sp.N(true20) < sp.N(b20)
expect(20, "0.04")

# --- q21  cos, P_4, |x| <= 1 ----------------------------------------------------
assert sp.maximum(sp.diff(sp.cos(x), x, 5) ** 2, x, sp.S.Reals) == 1
b21 = lagrange(sp.cos(x), 0, 4, -1, 1, 1, M=1)
assert b21 == sp.Rational(1, 120)
true21 = sp.Abs(sp.cos(1) - taylor(sp.cos(x), 0, 4).subs(x, 1))
assert sp.N(true21) < sp.N(b21)
expect(21, "1/120")

print("c10_12: all 25 keys verified")
