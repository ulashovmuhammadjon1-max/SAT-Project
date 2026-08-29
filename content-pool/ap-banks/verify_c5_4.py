"""sympy verification for CALC 5.4 (the first derivative test).

For each function the critical numbers are found and the sign of f' is
evaluated on both sides of each one, so a keyed "relative maximum" claim is
confirmed by an actual + to - sign change rather than by f'(c) = 0 alone.
"""
import sympy as sp

import c5_4

x = sp.Symbol('x', real=True)


def sign_change(fprime, c, h=sp.Rational(1, 100)):
    """('sign left', 'sign right') of f' immediately around c."""
    return (sp.sign(sp.nsimplify(fprime.subs(x, c - h))),
            sp.sign(sp.nsimplify(fprime.subs(x, c + h))))


MAXI, MINI = (1, -1), (-1, 1)

# q5  x^3 - 3x: max at -1, min at 1
d = sp.diff(x**3 - 3*x, x)
assert sorted(sp.solve(d, x)) == [-1, 1]
assert sign_change(d, -1) == MAXI and sign_change(d, 1) == MINI
# q6  x^3 - 6x^2 + 9x: min at 3
f6 = x**3 - 6*x**2 + 9*x
assert sign_change(sp.diff(f6, x), 3) == MINI
assert sign_change(sp.diff(f6, x), 1) == MAXI
# q7  2x^3 - 9x^2 + 12x: relative max value f(1) = 5
f7 = 2*x**3 - 9*x**2 + 12*x
assert sign_change(sp.diff(f7, x), 1) == MAXI
assert f7.subs(x, 1) == 5
assert f7.subs(x, 2) == 4          # the relative minimum value, a distractor
# q8  x^4 - 4x^3: min at 3, nothing at 0
f8 = x**4 - 4*x**3
assert sign_change(sp.diff(f8, x), 3) == MINI
assert sign_change(sp.diff(f8, x), 0) == (-1, -1)
# q9  x e^(-x): max value 1/e at x = 1
f9 = x*sp.exp(-x)
assert sign_change(sp.diff(f9, x), 1) == MAXI
assert sp.simplify(f9.subs(x, 1) - sp.exp(-1)) == 0
# q10 x^2 e^x: max at -2, min at 0
f10 = x**2*sp.exp(x)
assert sign_change(sp.diff(f10, x), -2) == MAXI
assert sign_change(sp.diff(f10, x), 0) == MINI
# q11 x/(x^2+1): min value -1/2 at x = -1
f11 = x/(x**2 + 1)
assert sign_change(sp.diff(f11, x), -1) == MINI
assert f11.subs(x, -1) == sp.Rational(-1, 2)
# q12 x + 1/x: max value -2 at x = -1, min value 2 at x = 1
f12 = x + 1/x
assert sign_change(sp.diff(f12, x), -1) == MAXI and f12.subs(x, -1) == -2
assert sign_change(sp.diff(f12, x), 1) == MINI and f12.subs(x, 1) == 2
# q13 (x-2)^2 (x+1): max at 0
f13 = (x - 2)**2*(x + 1)
assert sp.expand(sp.diff(f13, x)) == sp.expand(3*x*(x - 2))
assert sign_change(sp.diff(f13, x), 0) == MAXI
# q14 x - 2 sqrt(x): min value -1 at x = 1
f14 = x - 2*sp.sqrt(x)
assert sign_change(sp.diff(f14, x), 1) == MINI
assert f14.subs(x, 1) == -1
# q15 ln(x)/x: max value 1/e at x = e
f15 = sp.log(x)/x
assert sign_change(sp.diff(f15, x), sp.E, sp.Rational(1, 2)) == MAXI
assert sp.simplify(f15.subs(x, sp.E) - sp.exp(-1)) == 0
# q16 sin + cos: max at pi/4
f16 = sp.sin(x) + sp.cos(x)
assert sign_change(sp.diff(f16, x), sp.pi/4, sp.Rational(1, 10)) == MAXI
assert sign_change(sp.diff(f16, x), 5*sp.pi/4, sp.Rational(1, 10)) == MINI
# q17 x^4 + 4x: min at -1, only real critical number
f17 = x**4 + 4*x
assert [s for s in sp.solve(sp.diff(f17, x), x) if s.is_real] == [-1]
assert sign_change(sp.diff(f17, x), -1) == MINI
# q18 (x+1)^3: no sign change at -1
assert sign_change(sp.diff((x + 1)**3, x), -1) == (1, 1)
# q19 |x^2 - 4|: minima at -2 and 2, maximum at 0
f19 = sp.Abs(x**2 - 4)
for c, want in ((-2, MINI), (2, MINI), (0, MAXI)):
    assert sign_change(sp.diff(f19, x), c) == want, c
assert f19.subs(x, 0) == 4
# q20 f' = (x-1)(x-3)^2: min at 1, nothing at 3
d20 = (x - 1)*(x - 3)**2
assert sign_change(d20, 1) == MINI and sign_change(d20, 3) == (1, 1)
# q21 f' = x^2 (x+4): min at -4, nothing at 0
d21 = x**2*(x + 4)
assert sign_change(d21, -4) == MINI and sign_change(d21, 0) == (1, 1)
# q22 f' = (x+2)/(x-1): positive to negative at -2, so a relative maximum
d22 = (x + 2)/(x - 1)
assert d22.subs(x, -3) > 0 and d22.subs(x, 0) < 0
assert sign_change(d22, -2) == MAXI
# q23 x^(2/3)(x - 5): f' = 5(x-2)/(3 x^(1/3)), maximum at x = 0
p = sp.Symbol('p', positive=True)
f23 = p**sp.Rational(5, 3) - 5*p**sp.Rational(2, 3)
assert sp.simplify(sp.diff(f23, p) - 5*(p - 2)/(3*p**sp.Rational(1, 3))) == 0
d23 = 5*(x - 2)/(3*sp.real_root(x, 3))          # the real cube root, valid for x < 0 too
assert d23.subs(x, -1) > 0 and d23.subs(x, 1) < 0
assert sp.solve(sp.Eq(d23, 0), x) == [2]
# q24 and q25 are sign charts; confirm the counted sign changes
assert (1, -1) == MAXI and (-1, -1) != MAXI and (-1, -1) != MINI   # x = -3 max, x = 2 neither
assert (1, 1) != MAXI and (1, 1) != MINI                           # x = 0 is not an extremum

# structural checks
qs = c5_4.QUESTIONS
assert len(qs) == 25, len(qs)
for i, item in enumerate(qs, 1):
    assert len(item["choices"]) == 4, i
    assert len(set(item["choices"])) == 4, i
    assert 0 <= item["ans"] < 4, i
    assert item["why"].strip()
assert len({q["q"] for q in qs}) == 25

print("c5_4: all checks passed")
