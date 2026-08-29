"""sympy verification for CALC 5.11 (solving optimization problems).

Every optimum below is *proved*: the objective is built from the constraint,
the critical number is solved for, and the sign of the second derivative (or
a comparison of candidate values) confirms whether it is a maximum or a
minimum. A stationary point alone is never accepted as an answer.
"""
import sympy as sp

import c5_11

x, r, h, V = sp.symbols('x r h V', positive=True)


def optimum(f, var, want, dom=None):
    """Return the unique critical point in the domain, checking the second
    derivative has the sign matching want ('max' or 'min')."""
    crits = [s for s in sp.solve(sp.diff(f, var), var) if s.is_real]
    if dom is not None:
        crits = [s for s in crits if dom[0] < s < dom[1]]
    assert len(crits) == 1, crits
    c = crits[0]
    d2 = sp.simplify(sp.diff(f, var, 2).subs(var, c))
    assert (sp.N(d2) < 0) if want == 'max' else (sp.N(d2) > 0), (f, d2)
    return c


# q1, q2  rectangle of perimeter 40
A = x*(20 - x)
c = optimum(A, x, 'max')
assert c == 10 and A.subs(x, c) == 100
P = sp.Symbol('P', positive=True)
assert sp.solve(sp.diff(x*(P/2 - x), x), x) == [P/4]        # a square in general
# q3  three-sided fence with 600 feet
A = x*(600 - 2*x)
c = optimum(A, x, 'max')
assert c == 150 and A.subs(x, c) == 45000
# q4  sum 20, maximum product
c = optimum(x*(20 - x), x, 'max')
assert c == 10 and (x*(20 - x)).subs(x, c) == 100
# q5  product 100, minimum sum
S = x + 100/x
c = optimum(S, x, 'min')
assert c == 10 and S.subs(x, c) == 20
# q6  sum 20, minimum sum of squares
f = x**2 + (20 - x)**2
c = optimum(f, x, 'min')
assert c == 10 and f.subs(x, c) == 200
# q7  box from a 12-inch square sheet
Vol = x*(12 - 2*x)**2
assert sp.simplify(sp.diff(Vol, x) - 12*(x - 2)*(x - 6)) == 0
c = optimum(Vol, x, 'max', dom=(0, 6))
assert c == 2 and Vol.subs(x, c) == 128
# q8  can holding 16 pi
hs = sp.solve(sp.Eq(sp.pi*r**2*h, 16*sp.pi), h)[0]
S = sp.simplify(2*sp.pi*r**2 + 2*sp.pi*r*hs)
assert sp.simplify(S - (2*sp.pi*r**2 + 32*sp.pi/r)) == 0
c = optimum(S, r, 'min')
assert c == 2 and hs.subs(r, 2) == 4                         # h = 4 = 2r
# q9  the general result h = 2r
hs = sp.solve(sp.Eq(sp.pi*r**2*h, V), h)[0]
S = sp.simplify(2*sp.pi*r**2 + 2*sp.pi*r*hs)
c = optimum(S, r, 'min')
assert sp.simplify(c**3 - V/(2*sp.pi)) == 0
assert sp.simplify(hs.subs(r, c) - 2*c) == 0
# q10 open box of volume 32
S = x**2 + 128/x
c = optimum(S, x, 'min')
assert c == 4 and S.subs(x, c) == 48
# q11 rectangle under y = 9 - x^2
A = 2*x*(9 - x**2)
c = optimum(A, x, 'max', dom=(0, 3))
assert c == sp.sqrt(3) and sp.simplify(A.subs(x, c)) == 12*sp.sqrt(3)
# q12 rectangle in the circle of radius 5
A = 4*x*sp.sqrt(25 - x**2)
c = optimum(A, x, 'max', dom=(0, 5))
assert sp.simplify(c - 5/sp.sqrt(2)) == 0 and sp.simplify(A.subs(x, c)) == 50
# q13 closest point on y = sqrt(x) to (3, 0)
D = (x - 3)**2 + x
c = optimum(D, x, 'min')
assert c == sp.Rational(5, 2)
# q14 shortest distance from (0, 2) to y = x^2
t = sp.Symbol('t', real=True)
D = t**2 + (t**2 - 2)**2
crits = sorted(sp.solve(sp.diff(D, t), t), key=lambda s: sp.N(s))
assert crits == [-sp.sqrt(6)/2, 0, sp.sqrt(6)/2]
vals = {s: sp.simplify(D.subs(t, s)) for s in crits}
assert vals[0] == 4 and vals[sp.sqrt(6)/2] == sp.Rational(7, 4)
assert min(vals.values(), key=lambda v: sp.N(v)) == sp.Rational(7, 4)
assert sp.simplify(sp.sqrt(sp.Rational(7, 4)) - sp.sqrt(7)/2) == 0
assert sp.simplify((sp.sqrt(6)/2)**2 - sp.Rational(3, 2)) == 0
# q15 wire cut into a square and a circle: minimum area
A = x**2/16 + (60 - x)**2/(4*sp.pi)
c = optimum(A, x, 'min', dom=(0, 60))
assert sp.simplify(c - 240/(sp.pi + 4)) == 0
assert sp.N(A.subs(x, 0)) > sp.N(A.subs(x, c))        # the endpoint is the maximum, not the minimum
# q16, q17 revenue and profit
R = x*(100 - 2*x)
c = optimum(R, x, 'max')
assert c == 25 and R.subs(x, c) == 1250
Pr = sp.expand(R - (20*x + 200))
c = optimum(Pr, x, 'max')
assert c == 20 and Pr.subs(x, c) == 600
# q18 divided pen of area 200
F = 3*x + 400/x
c = optimum(F, x, 'min')
assert sp.simplify(c - 20/sp.sqrt(3)) == 0
assert sp.simplify(F.subs(x, c) - 40*sp.sqrt(3)) == 0
# q19 Norman window of perimeter 30
A = 30*r - 2*r**2 - sp.pi*r**2/2
c = optimum(A, r, 'max')
assert sp.simplify(c - 30/(sp.pi + 4)) == 0
# q20 poster with margins
A = sp.expand((x + 2)*(24/x + 4))
assert sp.simplify(A - (4*x + 48/x + 32)) == 0
c = optimum(A, x, 'min')
assert sp.simplify(c - 2*sp.sqrt(3)) == 0
assert sp.simplify(A.subs(x, c) - (32 + 16*sp.sqrt(3))) == 0
# q21 minimum of x^2 + 16/x
f = x**2 + 16/x
c = optimum(f, x, 'min')
assert c == 2 and f.subs(x, c) == 12
# q22 row-and-walk travel time
T = sp.sqrt(4 + x**2)/3 + (6 - x)/5
c = optimum(T, x, 'min', dom=(0, 6))
assert c == sp.Rational(3, 2)
assert sp.N(T.subs(x, c)) < sp.N(T.subs(x, 0)) and sp.N(T.subs(x, c)) < sp.N(T.subs(x, 6))
# q23 fence against a barn
A = x*(100 - 2*x)
c = optimum(A, x, 'max')
assert c == 25 and A.subs(x, c) == 1250
# q24 x + 2y = 12, maximize xy
prod = x*(12 - x)/2
c = optimum(prod, x, 'max')
assert c == 6 and prod.subs(x, c) == 18

# structural checks
qs = c5_11.QUESTIONS
assert len(qs) == 25, len(qs)
for i, item in enumerate(qs, 1):
    assert len(item["choices"]) == 4, i
    assert len(set(item["choices"])) == 4, i
    assert 0 <= item["ans"] < 4, i
    assert item["why"].strip()
assert len({q["q"] for q in qs}) == 25

print("c5_11: all checks passed")
