# Verification for CALC 8.5. Run: python3 verify_c8_5.py
import sympy as sp
from c8_5 import QUESTIONS as Q

y = sp.Symbol('y', real=True)
x = sp.Symbol('x', real=True)


def key(i):
    return Q[i - 1]["choices"][Q[i - 1]["ans"]]


def area(right, left, c, d):
    mid = sp.Rational(1, 2) * (sp.nsimplify(c) + sp.nsimplify(d))
    assert (right - left).subs(y, mid) >= 0, "right/left reversed"
    return sp.simplify(sp.integrate(right - left, (y, c, d)))


def meet(f, g):
    return sorted([r for r in sp.solve(f - g, y) if r.is_real])


def num(i):
    return sp.nsimplify(key(i).replace("ln", "log"))


assert len(Q) == 25
for i, item in enumerate(Q, 1):
    assert len(item["choices"]) == 4 and len(set(item["choices"])) == 4, i
    assert 0 <= item["ans"] < 4, i

assert key(1) == "int from c to d of (f(y) - g(y)) dy"
assert key(2).startswith("the right-hand x-value minus the left-hand x-value")
assert key(3).startswith("the left and right boundaries")

assert meet(y**2, sp.Integer(4)) == [-2, 2]
assert area(sp.Integer(4), y**2, -2, 2) == sp.Rational(32, 3) and num(4) == sp.Rational(32, 3)
assert meet(y**2, y) == [0, 1]
assert area(y, y**2, 0, 1) == sp.Rational(1, 6) and num(5) == sp.Rational(1, 6)
assert area(y, y**3, 0, 1) == sp.Rational(1, 4) and num(6) == sp.Rational(1, 4)
# q7 the same region either way
assert area(sp.Integer(4), y**2, 0, 2) == sp.Rational(16, 3)
assert sp.integrate(sp.sqrt(x), (x, 0, 4)) == sp.Rational(16, 3)
assert num(7) == sp.Rational(16, 3)
assert area(sp.sqrt(y), y / 2, 0, 4) == sp.Rational(4, 3) and num(8) == sp.Rational(4, 3)
assert meet(y**2, y + 2) == [-1, 2]
assert area(y + 2, y**2, -1, 2) == sp.Rational(9, 2) and num(9) == sp.Rational(9, 2)
assert meet(y**2, 2 - y**2) == [-1, 1]
assert area(2 - y**2, y**2, -1, 1) == sp.Rational(8, 3) and num(10) == sp.Rational(8, 3)
assert meet(4 * y - y**2, sp.Integer(0)) == [0, 4]
assert area(4 * y - y**2, sp.Integer(0), 0, 4) == sp.Rational(32, 3) and num(11) == sp.Rational(32, 3)
assert sp.simplify(area(sp.exp(y), sp.Integer(0), 0, 1) - (sp.E - 1)) == 0 and key(12) == "e - 1"
assert area(sp.sin(y), sp.Integer(0), 0, sp.pi) == 2 and num(13) == 2
assert meet(y**2, 8 - y**2) == [-2, 2]
assert area(8 - y**2, y**2, -2, 2) == sp.Rational(64, 3) and num(14) == sp.Rational(64, 3)
assert sp.solve(sp.Eq(y, 2 * x + 1), x) == [(y - 1) / 2] and key(15) == "x = (y - 1)/2"
yp = sp.Symbol('yp', nonnegative=True)
xp = sp.Symbol('xp', nonnegative=True)
sols16 = sp.solve(sp.Eq(yp, xp**2), xp)
assert sp.sqrt(yp) in sols16
for v in (0, 1, 4, 9):                       # the nonnegative branch is the right one
    assert sp.sqrt(sp.Integer(v))**2 == v
assert key(16) == "x = sqrt(y)"
# q17 same region both ways
assert area(sp.Integer(2), sp.sqrt(y), 0, 4) == sp.Rational(8, 3)
assert sp.integrate(x**2, (x, 0, 2)) == sp.Rational(8, 3)
assert num(17) == sp.Rational(8, 3)
assert meet(y**2 - 4, sp.Integer(0)) == [-2, 2]
assert (0 - (y**2 - 4)).subs(y, 0) > 0
assert key(18) == "int from -2 to 2 of (4 - y^2) dy"
assert key(19).startswith("with horizontal slices the integrand must be right minus left")
assert meet(2 * y, y**2) == [0, 2]
assert area(2 * y, y**2, 0, 2) == sp.Rational(4, 3) and num(20) == sp.Rational(4, 3)
assert sp.simplify(area(1 / y, sp.Integer(0), 1, 2) - sp.log(2)) == 0 and key(21) == "ln(2)"
assert area(y**2, y**4, 0, 1) == sp.Rational(2, 15) and num(22) == sp.Rational(2, 15)
assert meet(y**2, y + 6) == [-2, 3]
assert key(23) == "from y = -2 to y = 3"
assert area(y + 6, y**2, -2, 3) == sp.Rational(125, 6) and num(24) == sp.Rational(125, 6)
# q25 both orientations give 1/6
assert sp.integrate(x - x**2, (x, 0, 1)) == sp.Rational(1, 6)
assert sp.integrate(sp.sqrt(y) - y, (y, 0, 1)) == sp.Rational(1, 6)
assert key(25).startswith("it can be computed either way")

print("verify_c8_5: all checks passed")
