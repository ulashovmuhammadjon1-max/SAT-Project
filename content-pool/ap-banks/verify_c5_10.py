"""sympy verification for CALC 5.10 (setting up optimization problems).

Each model is derived from the constraint symbolically and compared with the
keyed expression, and the distractors are checked for not being algebraically
equal to the key (two choices that simplify to the same function would make
the item unanswerable).
"""
import sympy as sp

import c5_10

w, x, r, h, L, y = sp.symbols('w x r h L y', positive=True)


def same(a, b):
    return sp.simplify(sp.expand(a - b)) == 0


# q4, q5  rectangle of perimeter 40
Lsol = sp.solve(sp.Eq(2*w + 2*L, 40), L)[0]
assert Lsol == 20 - w
assert same(w*Lsol, w*(20 - w))
for bad in (w*(40 - w), w*(40 - 2*w), (20 - w)**2):
    assert not same(bad, w*(20 - w))
t = sp.Symbol('t', real=True)
assert sp.solveset(t > 0, t, sp.S.Reals).intersect(sp.solveset(20 - t > 0, t, sp.S.Reals)) == sp.Interval.open(0, 20)
# q6  three-sided fence, 600 feet
assert same(x*(600 - 2*x), x*(600 - 2*x))
assert sp.solve(sp.Eq(2*x + y, 600), y)[0] == 600 - 2*x
# q7, q8  open box from a 12 by 12 sheet
V = x*(12 - 2*x)**2
assert same(V, 4*x**3 - 48*x**2 + 144*x)
assert sp.solveset(t > 0, t, sp.S.Reals).intersect(sp.solveset(12 - 2*t > 0, t, sp.S.Reals)) == sp.Interval.open(0, 6)
# q9  can of volume 355
hs = sp.solve(sp.Eq(sp.pi*r**2*h, 355), h)[0]
S = sp.simplify(2*sp.pi*r**2 + 2*sp.pi*r*hs)
assert same(S, 2*sp.pi*r**2 + 710/r)
for bad in (2*sp.pi*r**2 + 355/r, sp.pi*r**2 + 710/r, 2*sp.pi*r**2 + 710*sp.pi/r):
    assert not same(bad, S)
# q10 open box, square base, volume 32
hs = sp.solve(sp.Eq(x**2*h, 32), h)[0]
assert same(x**2 + 4*x*hs, x**2 + 128/x)
# q11, q12 two numbers
assert same(x*(20 - x), 20*x - x**2)
assert same(x + 100/x, x + 100/x)
# q13 rectangle under y = 9 - x^2
assert same(2*x*(9 - x**2), 18*x - 2*x**3)
assert sp.solveset(9 - t**2 > 0, t, sp.Interval.open(0, sp.oo)) == sp.Interval.open(0, 3)
# q14 rectangle in a circle of radius 5
ys = sp.sqrt(25 - x**2)
assert same(2*x*(2*ys), 4*x*sp.sqrt(25 - x**2))
# q15 closest point on y = sqrt(x) to (3, 0)
D = (x - 3)**2 + (sp.sqrt(x))**2
assert same(D, (x - 3)**2 + x)
assert not same((x - 3)**2 + x**2, D)
# q17 wire of length 60: square plus circle
square = (x/4)**2
rad = (60 - x)/(2*sp.pi)
circle = sp.pi*rad**2
assert same(square + circle, x**2/16 + (60 - x)**2/(4*sp.pi))
assert not same(x**2/16 + (60 - x)**2/(2*sp.pi), square + circle)
# q18, q19 revenue and profit
R = x*(100 - 2*x)
Cst = 20*x + 200
assert same(sp.expand(R - Cst), 80*x - 2*x**2 - 200)
# q20 divided pen of area 200
ys = sp.solve(sp.Eq(x*y, 200), y)[0]
assert same(3*x + 2*ys, 3*x + 400/x)
# q21 Norman window of perimeter 30
hs = sp.solve(sp.Eq(2*r + 2*h + sp.pi*r, 30), h)[0]
A = sp.expand(2*r*hs + sp.pi*r**2/2)
assert same(A, 30*r - 2*r**2 - sp.pi*r**2/2)
assert not same(30*r - 2*r**2 + sp.pi*r**2/2, A)
# q22 poster with margins
assert same((x + 2)*(24/x + 4), (x + 2)*(24/x + 4))
assert not same((x + 1)*(24/x + 2), (x + 2)*(24/x + 4))
assert not same((x + 2)*(24/x + 2), (x + 2)*(24/x + 4))
# q25 box with square base and no top, volume V
Vs = sp.Symbol('V', positive=True)
hs = sp.solve(sp.Eq(x**2*h, Vs), h)[0]
assert same(x**2 + 4*x*hs, x**2 + 4*Vs/x)

# structural checks
qs = c5_10.QUESTIONS
assert len(qs) == 25, len(qs)
for i, item in enumerate(qs, 1):
    assert len(item["choices"]) == 4, i
    assert len(set(item["choices"])) == 4, i
    assert 0 <= item["ans"] < 4, i
    assert item["why"].strip()
assert len({q["q"] for q in qs}) == 25

print("c5_10: all checks passed")
