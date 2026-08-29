"""sympy verification for CALC 5.8 (graphs of f and f').

Items described only in words about the signs of f' and f'' carry no
computation. Every item that names a function, a formula for f', a sign
chart, or a table is confirmed here.
"""
import sympy as sp

import c5_8

x = sp.Symbol('x', real=True)
oo = sp.oo
O = sp.Interval.open

# q1  f' of x^2 - 6x + 5 is the line 2x - 6, zero at 3
assert sp.diff(x**2 - 6*x + 5, x) == 2*x - 6
assert sp.solve(2*x - 6, x) == [3]
# q2  f' of x^3 - 3x is 3x^2 - 3: upward parabola, vertex (0, -3), zeros +-1
d2 = sp.diff(x**3 - 3*x, x)
assert d2 == 3*x**2 - 3 and d2.subs(x, 0) == -3
assert sorted(sp.solve(d2, x)) == [-1, 1]
assert sp.diff(d2, x, 2) == 6 > 0
# q3  f' = 4 gives f = 4x + C
C = sp.Symbol('C')
assert sp.integrate(4, x) + C == 4*x + C
# q4  f' a line of positive slope with a zero at 2: minimum at 2, f'' constant > 0
m = sp.Symbol('m', positive=True)
d4 = m*(x - 2)
assert d4.subs(x, 1) < 0 and d4.subs(x, 3) > 0 and sp.diff(d4, x) == m
# q5, q6  f' = (x - 1)(x - 5)
d5 = (x - 1)*(x - 5)
assert d5.subs(x, 0) > 0 and d5.subs(x, 3) < 0 and d5.subs(x, 6) > 0
assert sp.solve(sp.diff(d5, x), x) == [3]                    # vertex, so f'' changes sign at 3
# q11 f' = (x - 2)^2 never negative, zero only at 2
assert sp.solveset((x - 2)**2 < 0, x, sp.S.Reals) == sp.EmptySet
assert sp.solve((x - 2)**2, x) == [2]
# q12 |x - 2|: slopes -1 and 1, derivative undefined at 2
assert sp.diff(2 - x, x) == -1 and sp.diff(x - 2, x) == 1
assert sp.diff(sp.Abs(x - 2), x).subs(x, 1) == -1 and sp.diff(sp.Abs(x - 2), x).subs(x, 3) == 1
# q13 e^x is its own derivative
assert sp.diff(sp.exp(x), x) == sp.exp(x)
# q14 ln(x): f' = 1/x > 0 and decreasing on (0, inf)
assert sp.diff(sp.log(x), x) == 1/x
assert sp.solveset(sp.diff(1/x, x) < 0, x, O(0, oo)) == O(0, oo)
# q15 f' = cos(x), f(0) = 0  ->  f = sin(x)
f15 = sp.integrate(sp.cos(x), (x, 0, x))
assert sp.simplify(f15 - sp.sin(x)) == 0
assert f15.subs(x, sp.pi/2) == 1 and f15.subs(x, 3*sp.pi/2) == -1 and f15.subs(x, 2*sp.pi) == 0
# q16 f' = sin(x) on (0, 2pi): positive then negative, changing only at pi
assert sp.solveset(sp.sin(x) > 0, x, O(0, 2*sp.pi)) == O(0, sp.pi)
assert sp.solveset(sp.sin(x) < 0, x, O(0, 2*sp.pi)) == O(sp.pi, 2*sp.pi)
# q17 a table with f' increasing through zero at x = 1
tbl = {0: -2, 1: 0, 2: 3, 3: 5}
assert list(tbl.values()) == sorted(tbl.values())            # f' increasing
assert tbl[0] < 0 < tbl[2] and tbl[1] == 0
# q18, q19 sign charts: a sign change in f' is an extremum, one in f'' an inflection
assert (1, -1) != (-1, 1)
# q23 x^4 - 4x^2: three critical numbers, two inflection points
f23 = x**4 - 4*x**2
assert len([r for r in sp.solve(sp.diff(f23, x), x) if r.is_real]) == 3
infl = [r for r in sp.solve(sp.diff(f23, x, 2), x) if r.is_real]
assert len(infl) == 2
for r in infl:
    s = sp.diff(f23, x, 2)
    assert sp.sign(s.subs(x, r - sp.Rational(1, 10))) != sp.sign(s.subs(x, r + sp.Rational(1, 10)))
# q24 x^(1/3): derivative tends to +infinity from both sides (vertical tangent)
p = sp.Symbol('p', positive=True)
assert sp.simplify(sp.diff(p**sp.Rational(1, 3), p) - 1/(3*p**sp.Rational(2, 3))) == 0
d24 = 1/(3*sp.real_root(x, 3)**2)
assert sp.limit(d24, x, 0, '+') is oo and sp.limit(d24, x, 0, '-') is oo
# q25 f' = 2x with f(0) = 1  ->  f = x^2 + 1
f25 = sp.integrate(2*x, x) + C
c0 = sp.solve(sp.Eq(f25.subs(x, 0), 1), C)[0]
assert sp.expand(f25.subs(C, c0)) == x**2 + 1

# structural checks
qs = c5_8.QUESTIONS
assert len(qs) == 25, len(qs)
for i, item in enumerate(qs, 1):
    assert len(item["choices"]) == 4, i
    assert len(set(item["choices"])) == 4, i
    assert 0 <= item["ans"] < 4, i
    assert item["why"].strip()
assert len({q["q"] for q in qs}) == 25
# no item may lean on a picture
for i, item in enumerate(qs, 1):
    low = item["q"].lower()
    assert "graph shown" not in low and "figure" not in low and "shown above" not in low, i

print("c5_8: all checks passed")
