"""sympy verification for CALC 5.1 (Using the Mean Value Theorem).

Conceptual items (statements of the hypotheses, Rolle's Theorem, the
zero-derivative corollary) carry no computation and are checked by hand;
every item with a number in it is confirmed below.
"""
import sympy as sp

import c5_1

x, c = sp.symbols('x c', real=True)


def mvt_values(f, a, b):
    """All c in (a, b) with f'(c) equal to the average rate of change."""
    avg = (f.subs(x, b) - f.subs(x, a)) / (b - a)
    sols = sp.solve(sp.Eq(sp.diff(f, x).subs(x, c), avg), c)
    return sorted([s for s in sols if s.is_real and a < s < b], key=lambda s: sp.N(s))


# q4  f(x) = x^2 on [1, 5]  ->  c = 3
assert mvt_values(x**2, 1, 5) == [sp.Integer(3)]
# q5  f(x) = x^3 on [0, 3]  ->  c = sqrt(3)
assert mvt_values(x**3, 0, 3) == [sp.sqrt(3)]
# q6  f(x) = sqrt(x) on [0, 4]  ->  c = 1
assert mvt_values(sp.sqrt(x), 0, 4) == [sp.Integer(1)]
# q7  f(x) = 1/x on [1, 4]  ->  c = 2
assert mvt_values(1/x, 1, 4) == [sp.Integer(2)]
# q8  f(x) = ln(x) on [1, e]  ->  c = e - 1
assert mvt_values(sp.log(x), 1, sp.E) == [sp.E - 1]
assert 1 < sp.E - 1 < sp.E
# q9  f(x) = sin(x) on [0, pi]  ->  c = pi/2
assert mvt_values(sp.sin(x), 0, sp.pi) == [sp.pi/2]
# q10 Rolle for x^2 - 6x + 8 on [2, 4]  ->  c = 3
f10 = x**2 - 6*x + 8
assert f10.subs(x, 2) == f10.subs(x, 4) == 0
assert mvt_values(f10, 2, 4) == [sp.Integer(3)]
# q11 f(x) = x^3 - x on [0, 2]  ->  c = 2/sqrt(3) = 2*sqrt(3)/3
assert mvt_values(x**3 - x, 0, 2) == [2*sp.sqrt(3)/3]
assert sp.simplify(2/sp.sqrt(3) - 2*sp.sqrt(3)/3) == 0
# the three distractors of q11 are genuinely different numbers
vals11 = [2*sp.sqrt(3)/3, sp.sqrt(3)/3, sp.Integer(1), sp.Rational(4, 3)]
assert len({sp.nsimplify(v) for v in vals11}) == 4
# q12 f(x) = x^3 - 3x on [-2, 2]  ->  exactly two values of c
assert len(mvt_values(x**3 - 3*x, -2, 2)) == 2
# q13 1/x is discontinuous inside [-1, 2] only
assert sp.limit(1/x, x, 0, '+') is sp.oo
# q14 |x - 1| on [0, 3]: average slope 1/3, but f' is only -1 or 1
f14 = sp.Abs(x - 1)
avg14 = (f14.subs(x, 3) - f14.subs(x, 0)) / 3
assert avg14 == sp.Rational(1, 3)
assert set(sp.diff(f14, x).subs(x, t) for t in (sp.Rational(1, 2), 2)) == {-1, 1}
assert not sp.solve(sp.Eq(sp.diff(x - 1, x), avg14))       # slope 1 never equals 1/3
assert not sp.solve(sp.Eq(sp.diff(1 - x, x), avg14))       # slope -1 never equals 1/3
# q15 x^(2/3) on [-1, 8]: the only solution of f'(t) = 1/3 is t = 8, an endpoint
f15 = sp.Pow(x**2, sp.Rational(1, 3))
avg15 = (sp.Integer(4) - 1) / sp.Integer(9)
assert avg15 == sp.Rational(1, 3)
assert sp.solve(sp.Eq(sp.Rational(2, 3) * c**sp.Rational(-1, 3), avg15), c) == [sp.Integer(8)]
assert not mvt_values(f15, -1, 8)
# q16 tan(x) blows up at pi/2, inside [0, pi]
assert sp.limit(sp.tan(x), x, sp.pi/2, '-') is sp.oo
# q17 average velocity 120 miles over 2 hours
assert sp.Rational(120, 2) == 60
# q18 (20 - 5)/(7 - 2) = 3
assert sp.Rational(20 - 5, 7 - 2) == 3
# q19 f(0) = 1 and |f'| <= 3  ->  f(4) <= 13
assert 1 + 3 * (4 - 0) == 13
# q20 g(1) = 8 and g' >= 2  ->  g(6) >= 18
assert 8 + 2 * (6 - 1) == 18
# q23 the piecewise function is differentiable at x = 1, and c = 3/4
left, right = x**2, 2*x - 1
assert left.subs(x, 1) == right.subs(x, 1)
assert sp.diff(left, x).subs(x, 1) == sp.diff(right, x).subs(x, 1)
avg23 = (right.subs(x, 2) - left.subs(x, 0)) / 2
assert avg23 == sp.Rational(3, 2)
assert sp.solve(sp.Eq(sp.diff(left, x).subs(x, c), avg23), c) == [sp.Rational(3, 4)]
# q24 e^x on [0, ln 4]  ->  c = ln(3/ln 4), which lies in the open interval
sol24 = sp.solve(sp.Eq(sp.exp(c), 3/sp.log(4)), c)
assert sp.simplify(sol24[0] - sp.log(3/sp.log(4))) == 0
assert 0 < sp.N(sol24[0]) < sp.N(sp.log(4))
vals24 = [sp.log(3/sp.log(4)), sp.log(3)/sp.log(4), sp.log(2), 3/sp.log(4)]
assert len({round(float(v), 9) for v in vals24}) == 4
# q25 p'(x) = 3x^2 + 4 has no real zero, so p has at most one real zero
p = x**3 + 4*x - 9
assert [s for s in sp.solve(sp.diff(p, x), x) if s.is_real] == []
assert len([s for s in sp.solve(p, x) if s.is_real]) == 1

# structural checks
qs = c5_1.QUESTIONS
assert len(qs) == 25, len(qs)
for i, item in enumerate(qs, 1):
    assert len(item["choices"]) == 4, i
    assert len(set(item["choices"])) == 4, i
    assert 0 <= item["ans"] < 4, i
    assert item["why"].strip()
assert len({q["q"] for q in qs}) == 25

print("c5_1: all checks passed")
