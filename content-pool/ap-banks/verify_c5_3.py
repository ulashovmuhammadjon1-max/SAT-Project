"""sympy verification for CALC 5.3 (intervals of increase and decrease).

For each function the derivative's sign set is computed directly with
solveset, so the keyed interval is confirmed rather than sampled.
"""
import sympy as sp

import c5_3

x = sp.Symbol('x', real=True)
R = sp.S.Reals


def pos(f, domain=R):
    return sp.solveset(sp.diff(f, x) > 0, x, domain)


def neg(f, domain=R):
    return sp.solveset(sp.diff(f, x) < 0, x, domain)


oo = sp.oo
O = sp.Interval.open

# q4  x^2 - 4x increasing on (2, inf)
assert pos(x**2 - 4*x) == O(2, oo)
# q5  x^3 - 3x decreasing on (-1, 1)
assert neg(x**3 - 3*x) == O(-1, 1)
# q6  x^3 + 3x^2 - 9x increasing on (-inf, -3) U (1, inf)
assert pos(x**3 + 3*x**2 - 9*x) == sp.Union(O(-oo, -3), O(1, oo))
# q7  x^4 - 4x^3 increasing on (3, inf)
assert pos(x**4 - 4*x**3) == O(3, oo)
# q8  x^5 - 5x decreasing on (-1, 1)
assert neg(x**5 - 5*x) == O(-1, 1)
# q9  x/(x^2+1) increasing on (-1, 1)
assert pos(x/(x**2 + 1)) == O(-1, 1)
# q10 x e^x decreasing on (-inf, -1)
assert neg(x*sp.exp(x)) == O(-oo, -1)
# q11 ln(x) - x increasing on (0, 1)
assert pos(sp.log(x) - x, O(0, oo)) == O(0, 1)
# q12 x^2 e^(-x) increasing on (0, 2)
assert pos(x**2*sp.exp(-x)) == O(0, 2)
# q13 e^(-x^2) decreasing on (0, inf)
assert neg(sp.exp(-x**2)) == O(0, oo)
# q14 sqrt(x) - x decreasing on (1/4, inf)
assert neg(sp.sqrt(x) - x, O(0, oo)) == O(sp.Rational(1, 4), oo)
# q15 x + 1/x increasing on (-inf,-1) U (1, inf)
assert pos(x + 1/x, sp.Complement(R, sp.FiniteSet(0))) == sp.Union(O(-oo, -1), O(1, oo))
# q16 x - 2 sin(x) increasing on (pi/3, 5pi/3)
assert pos(x - 2*sp.sin(x), O(0, 2*sp.pi)) == O(sp.pi/3, 5*sp.pi/3)
# q17 1/x: derivative negative everywhere defined, yet f(-1) < f(1)
assert sp.diff(1/x, x) == -1/x**2
assert (1/x).subs(x, -1) < (1/x).subs(x, 1)
# q18 (x-1)/(x+2): derivative is 3/(x+2)^2 > 0
assert sp.simplify(sp.diff((x - 1)/(x + 2), x) - 3/(x + 2)**2) == 0
# q19 x^2/(x-1) decreasing on (0,1) U (1,2)
f19 = x**2/(x - 1)
assert neg(f19, sp.Complement(R, sp.FiniteSet(1))) == sp.Union(O(0, 1), O(1, 2))
# q20 x^(2/3) increasing on (0, inf)
d20 = sp.Rational(2, 3)*sp.cbrt(x)/x        # = 2/(3 x^(1/3))
assert sp.solveset(d20 > 0, x, sp.Complement(R, sp.FiniteSet(0))) == O(0, oo)
# q21 f' = (x-2)(x+3)^2 positive only on (2, inf)
assert sp.solveset((x - 2)*(x + 3)**2 > 0, x, R) == O(2, oo)
# q22 f' = (x-1)^2 (x-4) negative on (-inf,1) U (1,4)
assert sp.solveset((x - 1)**2*(x - 4) < 0, x, R) == sp.Union(O(-oo, 1), O(1, 4))
# q23 f' = x^2 (x-3)(x+1) positive on (-inf,-1) U (3, inf); of the choices only (3, inf)
s23 = sp.solveset(x**2*(x - 3)*(x + 1) > 0, x, R)
assert s23 == sp.Union(O(-oo, -1), O(3, oo))
assert O(3, oo).is_subset(s23) and not O(-1, 0).is_subset(s23)
assert not O(0, 3).is_subset(s23) and not O(-1, 3).is_subset(s23)
# q25 f' = 6 - 2x with f(1) = 5  ->  f = 6x - x^2, increasing and above 5 on (1, 3)
C = sp.Symbol('C')
f25 = sp.integrate(6 - 2*x, x) + C
C0 = sp.solve(sp.Eq(f25.subs(x, 1), 5), C)[0]
f25 = f25.subs(C, C0)
assert sp.expand(f25) == 6*x - x**2
inc = sp.solveset(sp.diff(f25, x) > 0, x, R)
above = sp.solveset(f25 > 5, x, R)
assert inc.intersect(above) == O(1, 3)

# structural checks
qs = c5_3.QUESTIONS
assert len(qs) == 25, len(qs)
for i, item in enumerate(qs, 1):
    assert len(item["choices"]) == 4, i
    assert len(set(item["choices"])) == 4, i
    assert 0 <= item["ans"] < 4, i
    assert item["why"].strip()
assert len({q["q"] for q in qs}) == 25

print("c5_3: all checks passed")
