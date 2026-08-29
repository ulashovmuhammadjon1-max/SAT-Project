"""sympy verification for CALC 5.9 (connecting f, f', and f'').

Items that only combine the meanings of the signs of f' and f'' carry no
computation. Every item naming a function, formula, table, or set of values
is confirmed here, including the two tangent-line arguments.
"""
import sympy as sp

import c5_9

x = sp.Symbol('x', real=True)
oo = sp.oo
O = sp.Interval.open
R = sp.S.Reals


def inc(f, dom=R):
    return sp.solveset(sp.diff(f, x) > 0, x, dom)


def dec(f, dom=R):
    return sp.solveset(sp.diff(f, x) < 0, x, dom)


def cup(f, dom=R):
    return sp.solveset(sp.diff(f, x, 2) > 0, x, dom)


def cdown(f, dom=R):
    return sp.solveset(sp.diff(f, x, 2) < 0, x, dom)


# q3  sqrt(x) is increasing with a decreasing derivative
assert inc(sp.sqrt(x), O(0, oo)) == O(0, oo)
assert cdown(sp.sqrt(x), O(0, oo)) == O(0, oo)
# q7, q8  x^3 - 3x^2
f = x**3 - 3*x**2
assert dec(f).intersect(cup(f)) == O(1, 2)
assert dec(f).intersect(cdown(f)) == O(0, 1)
# q9  x^4 - 4x^3 decreasing and concave down on (0, 2)
f = x**4 - 4*x**3
assert dec(f).intersect(cdown(f)) == O(0, 2)
# q10 e^(-x^2) increasing and concave down on (-1/sqrt(2), 0)
f = sp.exp(-x**2)
assert inc(f).intersect(cdown(f)) == O(-sp.sqrt(2)/2, 0)
assert sp.simplify(sp.sqrt(2)/2 - 1/sp.sqrt(2)) == 0
# q11 x + 2 cos(x) at 2pi/3: decreasing, concave up
f = x + 2*sp.cos(x)
assert sp.simplify(sp.diff(f, x).subs(x, 2*sp.pi/3)) == 1 - sp.sqrt(3)
assert sp.N(1 - sp.sqrt(3)) < 0
assert sp.simplify(sp.diff(f, x, 2).subs(x, 2*sp.pi/3)) == 1
# q12, q13 f' = x^2 - 4, f'' = 2x
d1, d2 = x**2 - 4, 2*x
assert d1.subs(x, -2) == 0 and d2.subs(x, -2) == -4
assert sp.solve(d2, x) == [0] and d2.subs(x, -1) < 0 < d2.subs(x, 1)
# q14 table with f' decreasing through zero between 2 and 3
tbl = {1: 4, 2: 1, 3: -3}
assert list(tbl.values()) == sorted(tbl.values(), reverse=True)
assert tbl[2] > 0 > tbl[3]
# q16 f'' = 6x - 12 with f'(2) = 0: f' has a minimum value of 0 at x = 2
d = sp.integrate(6*x - 12, x)                 # f' up to a constant
C = sp.Symbol('C')
c0 = sp.solve(sp.Eq((d + C).subs(x, 2), 0), C)[0]
fp = sp.expand(d + c0)
assert fp == 3*x**2 - 12*x + 12 and sp.factor(fp) == 3*(x - 2)**2
assert sp.solveset(fp < 0, x, R) == sp.EmptySet        # no sign change, so no extremum
assert (6*x - 12).subs(x, 1) < 0 < (6*x - 12).subs(x, 3)   # concavity does change
# q17 x^3 - 3x^2 + 2
f = x**3 - 3*x**2 + 2
assert sorted(sp.solve(sp.diff(f, x), x)) == [0, 2]
assert sp.solve(sp.diff(f, x, 2), x) == [1]
assert sp.diff(f, x).subs(x, -1) > 0 > sp.diff(f, x).subs(x, 1)    # max at 0
assert sp.diff(f, x).subs(x, 1) < 0 < sp.diff(f, x).subs(x, 3)     # min at 2
# q19 ln(x^2 + 1) at x = 2
f = sp.log(x**2 + 1)
assert sp.diff(f, x).subs(x, 2) == sp.Rational(4, 5)
assert sp.simplify(sp.diff(f, x, 2) - (2 - 2*x**2)/(x**2 + 1)**2) == 0
assert sp.diff(f, x, 2).subs(x, 2) == sp.Rational(-6, 25)
# q20 the three functions that share f'(0) = f''(0) = 0 with different outcomes
for g, want in ((-x**4, 'max'), (x**4, 'min'), (x**3, 'neither')):
    assert sp.diff(g, x).subs(x, 0) == 0 and sp.diff(g, x, 2).subs(x, 0) == 0
    left = sp.sign(sp.diff(g, x).subs(x, -1))
    right = sp.sign(sp.diff(g, x).subs(x, 1))
    got = 'max' if (left, right) == (1, -1) else 'min' if (left, right) == (-1, 1) else 'neither'
    assert got == want, (g, got)
# q23 x/(x^2 + 1): two horizontal tangents, three inflection points
f = x/(x**2 + 1)
assert sorted(sp.solve(sp.diff(f, x), x)) == [-1, 1]
s = sp.simplify(sp.diff(f, x, 2))
assert sp.simplify(s - (2*x**3 - 6*x)/(x**2 + 1)**3) == 0
roots = sorted([r for r in sp.solve(s, x) if r.is_real], key=lambda t: sp.N(t))
assert roots == [-sp.sqrt(3), 0, sp.sqrt(3)]
for r in roots:
    assert sp.sign(s.subs(x, r - sp.Rational(1, 10))) != sp.sign(s.subs(x, r + sp.Rational(1, 10)))
# q24 concave up everywhere means f lies strictly above its tangent line y = 2 - x
sample = sp.exp(-x) + 1                      # f(0) = 2, f'(0) = -1, f'' = e^(-x) > 0
assert sample.subs(x, 0) == 2 and sp.diff(sample, x).subs(x, 0) == -1
assert sp.solveset(sp.diff(sample, x, 2) > 0, x, R) == R
gap = sp.simplify(sample - (2 - x))          # e^(-x) + x - 1, the vertical distance to the tangent
assert sp.solve(sp.diff(gap, x), x) == [0] and gap.subs(x, 0) == 0
assert sp.solveset(sp.diff(gap, x, 2) > 0, x, R) == R      # so 0 is a strict global minimum
assert all(sp.N(gap.subs(x, t)) > 0 for t in (-3, -1, sp.Rational(1, 2), 2, 5))
assert sp.diff(2 - x, x) == -1               # the tangent's slope matches f'(0)
# q25 x^4 - 4x^3 + 10: two horizontal tangents, two inflection points
f = x**4 - 4*x**3 + 10
assert sorted(sp.solve(sp.diff(f, x), x)) == [0, 3]
infl = sorted(sp.solve(sp.diff(f, x, 2), x))
assert infl == [0, 2]
for r in infl:
    s = sp.diff(f, x, 2)
    assert sp.sign(s.subs(x, r - sp.Rational(1, 10))) != sp.sign(s.subs(x, r + sp.Rational(1, 10)))

# structural checks
qs = c5_9.QUESTIONS
assert len(qs) == 25, len(qs)
for i, item in enumerate(qs, 1):
    assert len(item["choices"]) == 4, i
    assert len(set(item["choices"])) == 4, i
    assert 0 <= item["ans"] < 4, i
    assert item["why"].strip()
    low = item["q"].lower()
    assert "graph shown" not in low and "figure" not in low and "shown above" not in low, i
assert len({q["q"] for q in qs}) == 25

print("c5_9: all checks passed")
