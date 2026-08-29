"""sympy verification for CALC 5.12 (behaviors of implicit relations).

Each relation is differentiated with sympy's idiff and compared with the
keyed expression; horizontal-tangent points are found by solving dy/dx = 0
together with the relation itself, and vertical tangents by setting the
denominator to zero and checking the numerator does not vanish there.
"""
import sympy as sp

import c5_12

x, y = sp.symbols('x y', real=True)


def same(a, b):
    return sp.simplify(sp.together(a - b)) == 0


def horizontals(rel, slope):
    """Points on rel = 0 where the slope's numerator vanishes."""
    num, den = sp.fraction(sp.together(slope))
    pts = sp.solve([sp.Eq(rel, 0), sp.Eq(num, 0)], [x, y], dict=True)
    return sorted([(p[x], p[y]) for p in pts if x in p and y in p and den.subs(p) != 0],
                  key=lambda t: (sp.N(t[0]), sp.N(t[1])))


def verticals(rel, slope):
    num, den = sp.fraction(sp.together(slope))
    pts = sp.solve([sp.Eq(rel, 0), sp.Eq(den, 0)], [x, y], dict=True)
    return sorted([(p[x], p[y]) for p in pts if x in p and y in p and num.subs(p) != 0],
                  key=lambda t: (sp.N(t[0]), sp.N(t[1])))


# q1-q8  the circle of radius 5
circ = x**2 + y**2 - 25
s = sp.idiff(circ, y, x)
assert same(s, -x/y)
assert horizontals(circ, s) == [(0, -5), (0, 5)]
assert verticals(circ, s) == [(-5, 0), (5, 0)]
assert s.subs({x: 3, y: 4}) == sp.Rational(-3, 4)
assert sp.Rational(-1, 1)/sp.Rational(-3, 4) == sp.Rational(4, 3)      # the normal slope
s2 = sp.simplify(sp.idiff(circ, y, x, 2))
assert same(s2, -(x**2 + y**2)/y**3)
assert same(s2.subs(x**2, 25 - y**2), -25/y**3)      # using the relation itself
assert (-25/y**3).subs(y, 3) < 0                                       # concave down where y > 0
# q6  slope 1 on x^2 + y^2 = 8
c8 = x**2 + y**2 - 8
s8 = sp.idiff(c8, y, x)
pts = sp.solve([sp.Eq(c8, 0), sp.Eq(s8, 1)], [x, y], dict=True)
assert sorted([(p[x], p[y]) for p in pts], key=lambda t: sp.N(t[0])) == [(-2, 2), (2, -2)]
# q9  ellipse
ell = x**2/9 + y**2/4 - 1
assert same(sp.idiff(ell, y, x), -4*x/(9*y))
# q10 x^2 + 4y^2 = 16: vertical tangents at (+-4, 0)
e16 = x**2 + 4*y**2 - 16
s16 = sp.idiff(e16, y, x)
assert same(s16, -x/(4*y))
assert verticals(e16, s16) == [(-4, 0), (4, 0)]
# q11, q12 hyperbola
hyp = x**2 - y**2 - 1
sh = sp.idiff(hyp, y, x)
assert same(sh, x/y)
assert verticals(hyp, sh) == [(-1, 0), (1, 0)]
assert horizontals(hyp, sh) == []                    # x = 0 is not on the curve
# q13, q14 xy = 1
rel = x*y - 1
sxy = sp.idiff(rel, y, x)
assert same(sxy, -y/x)
assert same(sxy.subs(y, 1/x), -1/x**2)
assert horizontals(rel, sxy) == [] and verticals(rel, sxy) == []
# q15, q16 x^2 + xy + y^2 = 3
rel = x**2 + x*y + y**2 - 3
s = sp.idiff(rel, y, x)
assert same(s, -(2*x + y)/(x + 2*y))
assert horizontals(rel, s) == [(-1, 2), (1, -2)]
# q17, q18 the folium x^3 + y^3 = 6xy
fol = x**3 + y**3 - 6*x*y
sf = sp.idiff(fol, y, x)
assert same(sf, (6*y - 3*x**2)/(3*y**2 - 6*x))
assert sp.solve(sp.Eq(6*y - 3*x**2, 0), y) == [x**2/2]
# q19 y^3 - y = x^2: three horizontal tangents, all at x = 0
rel = y**3 - y - x**2
s = sp.idiff(rel, y, x)
assert same(s, 2*x/(3*y**2 - 1))
hs = horizontals(rel, s)
assert [p[0] for p in hs] == [0, 0, 0]
assert sorted([p[1] for p in hs], key=sp.N) == [-1, 0, 1]
# q20 astroid
ast = sp.Pow(x**2, sp.Rational(1, 3)) + sp.Pow(y**2, sp.Rational(1, 3)) - 1
u, v = sp.symbols('u v', positive=True)
sa = sp.idiff(u**sp.Rational(2, 3) + v**sp.Rational(2, 3) - 1, v, u)
assert same(sa, -(v/u)**sp.Rational(1, 3))
# q21 x^2 y + y^2 = 5
rel = x**2*y + y**2 - 5
assert same(sp.idiff(rel, y, x), -2*x*y/(x**2 + 2*y))
# q22 shifted circle
rel = x**2 + y**2 - 2*x - 4*y
s = sp.idiff(rel, y, x)
assert same(s, (2 - 2*x)/(2*y - 4))
assert horizontals(rel, s) == [(1, 2 - sp.sqrt(5)), (1, 2 + sp.sqrt(5))]
# q24 (3, 5) is not on the circle of radius 5
assert circ.subs({x: 3, y: 5}) != 0 and circ.subs({x: 3, y: 4}) == 0
# q25 y^2 = x: two y-values for each x > 0, vertical tangent at the origin
rel = y**2 - x
assert sp.solve(rel.subs(x, 4), y) == [-2, 2]
sv = sp.idiff(rel, y, x)
assert same(sv, 1/(2*y))
assert verticals(rel, sv) == [(0, 0)]

# structural checks
qs = c5_12.QUESTIONS
assert len(qs) == 25, len(qs)
for i, item in enumerate(qs, 1):
    assert len(item["choices"]) == 4, i
    assert len(set(item["choices"])) == 4, i
    assert 0 <= item["ans"] < 4, i
    assert item["why"].strip()
assert len({q["q"] for q in qs}) == 25

print("c5_12: all checks passed")
