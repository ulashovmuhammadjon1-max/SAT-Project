"""sympy verification for CALC 5.2 (Extreme Value Theorem, global versus
local extrema, critical points).

Items that only state the Extreme Value Theorem or a definition carry no
computation; every item naming a specific function is confirmed below.
"""
import sympy as sp

import c5_2

x = sp.Symbol('x', real=True)


def zeros_of_derivative(f):
    return sorted([s for s in sp.solve(sp.diff(f, x), x) if s.is_real], key=lambda s: sp.N(s))


# q7  1/x on (0, 1]: unbounded above, minimum 1 at x = 1
assert sp.limit(1/x, x, 0, '+') is sp.oo
assert sp.minimum(1/x, x, sp.Interval(sp.Rational(1, 100), 1)) == 1
# q8  x on (0, 3): infimum and supremum are not attained
assert sp.limit(x, x, 0, '+') == 0 and sp.limit(x, x, 3, '-') == 3
# q9  x^3 - 3x^2
assert zeros_of_derivative(x**3 - 3*x**2) == [0, 2]
# q10 x^4 - 8x^2
assert zeros_of_derivative(x**4 - 8*x**2) == [-2, 0, 2]
# q11 x^(2/3): derivative undefined at 0, never zero
d11 = sp.diff(sp.Pow(x**2, sp.Rational(1, 3)), x)
assert sp.solve(sp.Eq(sp.Rational(2, 3) * x**sp.Rational(-1, 3), 0), x) == []
assert sp.limit(sp.Abs(d11), x, 0) is sp.oo
# q12 |x - 4|: one-sided derivatives disagree at 4
assert sp.diff(4 - x, x) == -1 and sp.diff(x - 4, x) == 1
# q13 x/(x^2 + 1)
f13 = x/(x**2 + 1)
assert sp.simplify(sp.diff(f13, x) - (1 - x**2)/(x**2 + 1)**2) == 0
assert zeros_of_derivative(f13) == [-1, 1]
# q14 x e^(-x)
assert zeros_of_derivative(x*sp.exp(-x)) == [1]
# q15 ln(x)/x
assert zeros_of_derivative(sp.log(x)/x) == [sp.E]
# q16 x/(x - 2): derivative never zero, and 2 is outside the domain
f16 = x/(x - 2)
assert sp.simplify(sp.diff(f16, x) + 2/(x - 2)**2) == 0
assert sp.solve(sp.Eq(sp.diff(f16, x), 0), x) == []
# q17 sin(x) + cos(x) on (0, 2pi)
sols17 = sp.solveset(sp.diff(sp.sin(x) + sp.cos(x), x), x, sp.Interval.open(0, 2*sp.pi))
assert sols17 == sp.FiniteSet(sp.pi/4, 5*sp.pi/4)
# q18 x^2/(x - 1)
f18 = x**2/(x - 1)
assert sp.simplify(sp.diff(f18, x) - (x**2 - 2*x)/(x - 1)**2) == 0
assert zeros_of_derivative(f18) == [0, 2]
# q19 (x - 5)^(1/3): derivative never zero, undefined at 5
d19 = sp.diff(sp.cbrt(x - 5), x)
assert sp.solve(sp.Eq(d19, 0), x) == []
assert sp.limit(sp.Abs(d19), x, 5) is sp.oo
# q20 x^3: f' >= 0 on both sides of 0, so no extremum there
assert sp.diff(x**3, x).subs(x, -1) > 0 and sp.diff(x**3, x).subs(x, 1) > 0
# q21 x^4: f' changes from negative to positive at 0
assert sp.diff(x**4, x).subs(x, -1) < 0 and sp.diff(x**4, x).subs(x, 1) > 0
# q22 the piecewise example: sup is 4 but f(4) = 0, so no maximum is attained
assert sp.limit(x, x, 4, '-') == 4
# q24 3x^5 - 5x^3: three critical numbers, only two with a sign change
f24 = 3*x**5 - 5*x**3
assert zeros_of_derivative(f24) == [-1, 0, 1]
d24 = sp.diff(f24, x)
signs = [sp.sign(d24.subs(x, t)) for t in (-2, sp.Rational(-1, 2), sp.Rational(1, 2), 2)]
assert signs == [1, -1, -1, 1]   # no sign change across x = 0
# q25 x^(2/3) on [-1, 8]
f25 = sp.Pow(x**2, sp.Rational(1, 3))
cands = {t: sp.nsimplify(f25.subs(x, t)) for t in (-1, 0, 8)}
assert cands == {-1: 1, 0: 0, 8: 4}
assert max(cands, key=lambda t: cands[t]) == 8

# structural checks
qs = c5_2.QUESTIONS
assert len(qs) == 25, len(qs)
for i, item in enumerate(qs, 1):
    assert len(item["choices"]) == 4, i
    assert len(set(item["choices"])) == 4, i
    assert 0 <= item["ans"] < 4, i
    assert item["why"].strip()
assert len({q["q"] for q in qs}) == 25

print("c5_2: all checks passed")
