"""sympy verification for CALC 5.7 (the second derivative test).

Each computational item is checked by solving f'(c) = 0 and evaluating
f''(c); each inconclusive item is checked by confirming f''(c) = 0 and then
settling the outcome with the sign of f' on either side.
"""
import sympy as sp

import c5_7

x = sp.Symbol('x', real=True)


def crit(f):
    return sorted([s for s in sp.solve(sp.diff(f, x), x) if s.is_real], key=lambda t: sp.N(t))


def second(f, c):
    return sp.simplify(sp.diff(f, x, 2).subs(x, c))


def fp_signs(f, c, h=sp.Rational(1, 100)):
    d = sp.diff(f, x)
    return (sp.sign(sp.nsimplify(d.subs(x, c - h))), sp.sign(sp.nsimplify(d.subs(x, c + h))))


# q5  x^2 - 4x + 1
f = x**2 - 4*x + 1
assert crit(f) == [2] and second(f, 2) == 2 > 0
# q6  x^3 - 12x: max at -2
f = x**3 - 12*x
assert crit(f) == [-2, 2] and second(f, -2) == -12 and second(f, 2) == 12
# q7  x^3 - 3x^2 - 9x: min at 3
f = x**3 - 3*x**2 - 9*x
assert crit(f) == [-1, 3] and second(f, -1) == -12 and second(f, 3) == 12
# q8  x^4 - 2x^2 at 0
f = x**4 - 2*x**2
assert 0 in crit(f) and second(f, 0) == -4
# q9  x + 4/x
f = x + 4/x
assert crit(f) == [-2, 2] and second(f, 2) == 1 and second(f, -2) == -1
# q10 x e^(-x) at 1
f = x*sp.exp(-x)
assert crit(f) == [1] and second(f, 1) == -sp.exp(-1)
# q11 x^2 + 16/x
f = x**2 + 16/x
assert [c for c in crit(f)] == [2] and second(f, 2) == 6
# q12 sin on (0, 2pi)
f = sp.sin(x)
assert second(f, sp.pi/2) == -1 and second(f, 3*sp.pi/2) == 1
# q13 x^2 e^x
f = x**2*sp.exp(x)
assert crit(f) == [-2, 0]
assert second(f, -2) == -2*sp.exp(-2) and second(f, 0) == 2
# q14 x/(x^2 + 1) at 1
f = x/(x**2 + 1)
assert crit(f) == [-1, 1] and second(f, 1) == sp.Rational(-1, 2)
assert sp.simplify(sp.diff(f, x, 2) - (2*x**3 - 6*x)/(x**2 + 1)**3) == 0
# q15 ln(x) - x
f = sp.log(x) - x
assert crit(f) == [1] and second(f, 1) == -1
# q16 2x + 1/x^2: minimum value 3 at x = 1
f = 2*x + 1/x**2
assert [c for c in crit(f) if c > 0] == [1] and second(f, 1) == 6 and f.subs(x, 1) == 3
# q17 x^4: inconclusive, first derivative test gives a minimum
assert second(x**4, 0) == 0 and fp_signs(x**4, 0) == (-1, 1)
# q18 -x^4: inconclusive, maximum
assert second(-x**4, 0) == 0 and fp_signs(-x**4, 0) == (1, -1)
# q19 x^3: inconclusive, no extremum
assert second(x**3, 0) == 0 and fp_signs(x**3, 0) == (1, 1)
# q20 x^5: inconclusive, no extremum
assert sp.diff(x**5, x).subs(x, 0) == 0 and second(x**5, 0) == 0
assert fp_signs(x**5, 0) == (1, 1)
# q21 (x + 1)^3: inconclusive at -1, no extremum
f = (x + 1)**3
assert crit(f) == [-1] and second(f, -1) == 0 and fp_signs(f, -1) == (1, 1)
# q22 x + cos(x): critical at pi/2, f'' = 0 there, f' never negative
f = x + sp.cos(x)
assert sp.diff(f, x).subs(x, sp.pi/2) == 0 and second(f, sp.pi/2) == 0
assert fp_signs(f, sp.pi/2, sp.Rational(1, 10)) == (1, 1)
assert sp.solveset(sp.diff(f, x) < 0, x, sp.S.Reals) == sp.EmptySet
# q23 x^6: inconclusive but a genuine minimum
assert sp.diff(x**6, x).subs(x, 0) == 0 and second(x**6, 0) == 0
assert fp_signs(x**6, 0) == (-1, 1)
assert second(x**2, 0) == 2                      # x^2 is conclusive, so not the answer
# q25 x^2(x - 4): max at 0, min at 8/3
f = x**2*(x - 4)
assert crit(f) == [0, sp.Rational(8, 3)]
assert second(f, 0) == -8 and second(f, sp.Rational(8, 3)) == 8

# structural checks
qs = c5_7.QUESTIONS
assert len(qs) == 25, len(qs)
for i, item in enumerate(qs, 1):
    assert len(item["choices"]) == 4, i
    assert len(set(item["choices"])) == 4, i
    assert 0 <= item["ans"] < 4, i
    assert item["why"].strip()
assert len({q["q"] for q in qs}) == 25

print("c5_7: all checks passed")
