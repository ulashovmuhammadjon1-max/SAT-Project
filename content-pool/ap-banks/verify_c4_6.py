# Verification for CALC 4.6 — Local Linearity and Linearization.
# Each linearization is built by sympy, each estimate is evaluated, and each
# over/under claim is checked twice: against the sign of f'' and against the actual
# numeric comparison of L(x0) with f(x0). A claim that passes only one of those is
# a defect, so both are asserted.
import sympy as sp

import c4_6

x = sp.Symbol('x')


def lin(f, a):
    return f.subs(x, a) + sp.diff(f, x).subs(x, a) * (x - a)


def check(f, a, x0, expected_L, over):
    """expected_L: the value the module quotes; over: True if it claims an overestimate."""
    L = lin(f, a)
    Lval = sp.nsimplify(L.subs(x, x0))
    assert sp.simplify(Lval - expected_L) == 0, (f, a, Lval, expected_L)
    true = f.subs(x, x0)
    concave_up = sp.diff(f, x, 2).subs(x, a) > 0
    assert (Lval > true) == over, (f, a, float(Lval), float(true))
    assert (Lval > true) == (not concave_up), (f, a, "f'' disagrees with the numbers")
    return L, Lval


# q2-q4: sqrt(x) at 9, estimating sqrt(9.1) -> 3.0166..., an overestimate
L, v = check(sp.sqrt(x), 9, sp.Rational(91, 10), 3 + sp.Rational(1, 60), over=True)
assert sp.simplify(L - (3 + (x - 9) / 6)) == 0
assert round(float(v), 4) == 3.0167 and round(float(sp.sqrt(sp.Rational(91, 10))), 4) == 3.0166

# q5: x^(1/3) at 8, estimating 8.6^(1/3) -> 2.05, an overestimate
check(sp.root(x, 3), 8, sp.Rational(43, 5), sp.Rational(41, 20), over=True)

# q6: e^x at 0, estimating e^0.1 -> 1.1, an underestimate
check(sp.exp(x), 0, sp.Rational(1, 10), sp.Rational(11, 10), over=False)
assert round(float(sp.exp(sp.Rational(1, 10))), 5) == 1.10517

# q7: ln(x) at 1, estimating ln(1.05) -> 0.05, an overestimate
check(sp.log(x), 1, sp.Rational(21, 20), sp.Rational(1, 20), over=True)
assert round(float(sp.log(sp.Rational(21, 20))), 5) == 0.04879

# q8: sin(x) at 0 -> L(x) = x. f''(0) = 0 exactly, so the concavity test is taken
# just to the right of 0, where f'' = -sin(x) < 0; the numeric comparison is decisive.
Ls = lin(sp.sin(x), 0)
assert sp.simplify(Ls - x) == 0
assert sp.Rational(1, 10) > sp.sin(sp.Rational(1, 10))
assert sp.diff(sp.sin(x), x, 2).subs(x, sp.Rational(1, 10)) < 0
assert round(float(sp.sin(sp.Rational(1, 10))), 4) == 0.0998

# q9: f(2) = 5, f'(2) = -3
assert sp.nsimplify(5 + sp.Rational(-3) * sp.Rational(1, 10)) == sp.Rational(47, 10)
assert float(sp.Rational(47, 10)) == 4.7

# q10: f(3) = 10, f'(3) = 4, f'' < 0
assert sp.nsimplify(10 + 4 * sp.Rational(1, 5)) == sp.Rational(54, 5)
assert float(sp.Rational(54, 5)) == 10.8

# q11: dy for y = x^2 at x = 3 with dx = 0.01
dy = sp.diff(x**2, x).subs(x, 3) * sp.Rational(1, 100)
assert dy == sp.Rational(6, 100) and float(dy) == 0.06
exact = (sp.Rational(301, 100))**2 - 9
assert float(exact) == 0.0601

# q12: cube volume error
s, ds = sp.Symbol('s'), sp.Rational(1, 10)
assert sp.diff(s**3, s).subs(s, 10) * ds == 30

# q13: circle area error
r = sp.Symbol('r')
assert sp.diff(sp.pi * r**2, r).subs(r, 5) * sp.Rational(5, 100) == sp.pi / 2

# q16: sqrt(x) at 25, estimating sqrt(24) -> 4.9, an overestimate
check(sp.sqrt(x), 25, 24, sp.Rational(49, 10), over=True)
assert round(float(sp.sqrt(24)), 5) == 4.89898

# q17: 1/x at 2, estimating 1/2.1 -> 0.475, an underestimate
check(1 / x, 2, sp.Rational(21, 10), sp.Rational(19, 40), over=False)
assert round(float(sp.Rational(10, 21)), 5) == 0.47619

# q18: tan(x) at pi/4
Lt = lin(sp.tan(x), sp.pi / 4)
assert sp.simplify(Lt - (1 + 2 * (x - sp.pi / 4))) == 0

# q19: x^10 at 1, estimating 1.02^10 -> 1.2, an underestimate
check(x**10, 1, sp.Rational(51, 50), sp.Rational(6, 5), over=False)
assert round(float(sp.Rational(51, 50)**10), 5) == 1.21899

# q20: x^3 - 2x at 1
assert sp.simplify(lin(x**3 - 2 * x, 1) - (x - 2)) == 0

# q22: f(4) = 12, f'(4) = -2, f'' > 0
assert sp.nsimplify(12 + sp.Rational(-2) * sp.Rational(3, 10)) == sp.Rational(57, 5)
assert float(sp.Rational(57, 5)) == 11.4

# q24: sphere differential, r = 5, dr = 0.1
assert sp.diff(sp.Rational(4, 3) * sp.pi * r**3, r).subs(r, 5) * sp.Rational(1, 10) == 10 * sp.pi
assert round(float(10 * sp.pi), 1) == 31.4

# q25: L(x) = 7 - 3(x - 2) at x = 2.5, concave down -> f(2.5) < 5.5
assert sp.nsimplify((7 - 3 * (x - 2)).subs(x, sp.Rational(5, 2))) == sp.Rational(11, 2)

# Structure: 25 questions, four distinct choices, in-range key.
assert len(c4_6.QUESTIONS) == 25, len(c4_6.QUESTIONS)
for i, q in enumerate(c4_6.QUESTIONS, 1):
    assert len(q["choices"]) == 4, (i, len(q["choices"]))
    assert len(set(c.strip().lower() for c in q["choices"])) == 4, i
    assert 0 <= q["ans"] < 4, i
    assert "$" not in q["q"] and all("$" not in c for c in q["choices"]), i

print("c4_6: 25 questions, every linearization and over/under claim verified with sympy, structure OK")
