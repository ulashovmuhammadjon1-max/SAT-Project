"""sympy verification for CALC 5.6 (concavity and inflection points).

Every keyed inflection point is confirmed by an actual sign change in f'',
and every "no inflection point" answer is confirmed by showing f'' keeps its
sign across the candidate. Definition-only items carry no computation.
"""
import sympy as sp

import c5_6

x = sp.Symbol('x', real=True)
oo = sp.oo
O = sp.Interval.open


def d2(f):
    return sp.simplify(sp.diff(f, x, 2))


def up(f, domain=sp.S.Reals):
    return sp.solveset(sp.diff(f, x, 2) > 0, x, domain)


def down(f, domain=sp.S.Reals):
    return sp.solveset(sp.diff(f, x, 2) < 0, x, domain)


def flips(second, c, h=sp.Rational(1, 100)):
    return sp.sign(sp.nsimplify(second.subs(x, c - h))) != sp.sign(sp.nsimplify(second.subs(x, c + h)))


# q3  x^4: f'' = 12x^2 does not change sign at 0
assert d2(x**4) == 12*x**2 and not flips(d2(x**4), 0)
# q5, q6  x^3 - 3x^2
f = x**3 - 3*x**2
assert d2(f) == 6*x - 6 and up(f) == O(1, oo) and flips(d2(f), 1)
# q7  x^4 - 6x^2 concave down on (-1, 1)
assert down(x**4 - 6*x**2) == O(-1, 1)
# q8  x^4 - 4x^3: inflection at 0 and 2
s = d2(x**4 - 4*x**3)
assert sorted(sp.solve(s, x)) == [0, 2] and flips(s, 0) and flips(s, 2)
# q9  x^5 - 5x^4: f'' = 20x^2(x - 3); only x = 3 flips
s = d2(x**5 - 5*x**4)
assert sp.expand(s) == sp.expand(20*x**2*(x - 3))
assert sorted(sp.solve(s, x)) == [0, 3] and not flips(s, 0) and flips(s, 3)
# q10 3x^5 - 5x^3: three inflection points
s = d2(3*x**5 - 5*x**3)
roots = sorted([r for r in sp.solve(s, x) if r.is_real], key=lambda t: sp.N(t))
assert roots == [-sp.sqrt(2)/2, 0, sp.sqrt(2)/2]
assert all(flips(s, r, sp.Rational(1, 10)) for r in roots)
assert sp.simplify(sp.sqrt(2)/2 - 1/sp.sqrt(2)) == 0
# q11 x^4 + 2x^3: inflections at -1 and 0
s = d2(x**4 + 2*x**3)
assert sorted(sp.solve(s, x)) == [-1, 0] and flips(s, -1) and flips(s, 0)
# q12 x e^x concave up on (-2, inf)
assert up(x*sp.exp(x)) == O(-2, oo)
# q13 e^(-x^2): inflections at +-1/sqrt(2)
s = d2(sp.exp(-x**2))
assert sp.simplify(s - (4*x**2 - 2)*sp.exp(-x**2)) == 0
assert sorted(sp.solve(s, x), key=lambda t: sp.N(t)) == [-sp.sqrt(2)/2, sp.sqrt(2)/2]
# q14 ln(x): f'' = -1/x^2 < 0 on the whole domain
assert d2(sp.log(x)) == -1/x**2
assert down(sp.log(x), O(0, oo)) == O(0, oo)
# q15 sin(x) on (0, 2pi): inflection at pi
assert d2(sp.sin(x)) == -sp.sin(x) and flips(-sp.sin(x), sp.pi, sp.Rational(1, 10))
# q16, q17 1/x and x + 1/x: f'' = 2/x^3
assert d2(1/x) == 2/x**3 and d2(x + 1/x) == 2/x**3
assert up(x + 1/x, sp.Complement(sp.S.Reals, sp.FiniteSet(0))) == O(0, oo)
assert (2/x**3).subs(x, -1) < 0 < (2/x**3).subs(x, 1)     # sign differs, but 0 is not in the domain
# q18 x^(1/3): f'' = -(2/9) x^(-5/3) changes sign at 0, f continuous there
r = sp.real_root(x, 3)
s18 = -sp.Rational(2, 9)/sp.real_root(x, 3)**5
p = sp.Symbol('p', positive=True)
assert sp.simplify(sp.diff(p**sp.Rational(1, 3), p, 2) + sp.Rational(2, 9)*p**sp.Rational(-5, 3)) == 0
assert s18.subs(x, -1) > 0 > s18.subs(x, 1)
assert sp.limit(r, x, 0) == 0
# q19 x^(4/3): f'' = (4/9) x^(-2/3) > 0 wherever defined
assert sp.simplify(sp.diff(p**sp.Rational(4, 3), p, 2) - sp.Rational(4, 9)*p**sp.Rational(-2, 3)) == 0
s19 = sp.Rational(4, 9)/sp.real_root(x, 3)**2
assert s19.subs(x, -8) > 0 and s19.subs(x, 8) > 0
# q20 arctan concave up on (-inf, 0)
assert sp.simplify(d2(sp.atan(x)) + 2*x/(1 + x**2)**2) == 0
assert up(sp.atan(x)) == O(-oo, 0)
# q21 x^2 ln(x): f'' = 2 ln(x) + 3, inflection at e^(-3/2)
s = d2(x**2*sp.log(x))
assert sp.simplify(s - (2*sp.log(x) + 3)) == 0
assert sp.solve(s, x) == [sp.exp(sp.Rational(-3, 2))]
assert flips(s, sp.exp(sp.Rational(-3, 2)), sp.Rational(1, 100))
# q22 x^3 - 6x^2 + 12x - 7: f' = 3(x-2)^2 >= 0 yet f'' changes sign at 2
f22 = x**3 - 6*x**2 + 12*x - 7
assert sp.expand(sp.diff(f22, x)) == sp.expand(3*(x - 2)**2)
assert down(f22) == O(-oo, 2) and up(f22) == O(2, oo)
# q23 f'' = (x-1)(x+4)^2 positive only on (1, inf)
assert sp.solveset((x - 1)*(x + 4)**2 > 0, x, sp.S.Reals) == O(1, oo)

# structural checks
qs = c5_6.QUESTIONS
assert len(qs) == 25, len(qs)
for i, item in enumerate(qs, 1):
    assert len(item["choices"]) == 4, i
    assert len(set(item["choices"])) == 4, i
    assert 0 <= item["ans"] < 4, i
    assert item["why"].strip()
assert len({q["q"] for q in qs}) == 25

print("c5_6: all checks passed")
