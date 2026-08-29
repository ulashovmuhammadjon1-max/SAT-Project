# Verification for CALC 8.4. Run: python3 verify_c8_4.py
# Intersections are solved for, the ordering of the curves is checked at an
# interior point, and each area is integrated by sympy.
import sympy as sp
from c8_4 import QUESTIONS as Q

x = sp.Symbol('x', real=True)


def key(i):
    return Q[i - 1]["choices"][Q[i - 1]["ans"]]


def area(top, bottom, a, b):
    mid = sp.Rational(1, 2) * (sp.nsimplify(a) + sp.nsimplify(b))
    assert (top - bottom).subs(x, mid) >= 0, "top/bottom reversed"
    return sp.simplify(sp.integrate(top - bottom, (x, a, b)))


def crossings(f, g):
    return sorted([r for r in sp.solve(f - g, x) if r.is_real])


def num(i):
    return sp.nsimplify(key(i).replace("ln", "log"))


assert len(Q) == 25
for i, item in enumerate(Q, 1):
    assert len(item["choices"]) == 4 and len(set(item["choices"])) == 4, i
    assert 0 <= item["ans"] < 4, i

assert key(1) == "int from a to b of (f(x) - g(x)) dx"
assert area(x, x**2, 0, 1) == sp.Rational(1, 6) and num(2) == sp.Rational(1, 6)
assert crossings(4 - x**2, sp.Integer(0)) == [-2, 2]
assert area(4 - x**2, sp.Integer(0), -2, 2) == sp.Rational(32, 3) and num(3) == sp.Rational(32, 3)
assert area(x, x**3, 0, 1) == sp.Rational(1, 4) and num(4) == sp.Rational(1, 4)
assert crossings(2 * x, x**2) == [0, 2]
assert area(2 * x, x**2, 0, 2) == sp.Rational(4, 3) and num(5) == sp.Rational(4, 3)
assert area(sp.sqrt(x), x, 0, 1) == sp.Rational(1, 6) and num(6) == sp.Rational(1, 6)
assert sp.simplify(area(sp.exp(x), sp.Integer(1), 0, 1) - (sp.E - 2)) == 0 and key(7) == "e - 2"
assert sp.simplify(area(sp.cos(x), sp.sin(x), 0, sp.pi / 4) - (sp.sqrt(2) - 1)) == 0
assert key(8) == "sqrt(2) - 1"
assert key(9).startswith("the top function value minus the bottom")
assert crossings(8 - x**2, x**2) == [-2, 2]
assert area(8 - x**2, x**2, -2, 2) == sp.Rational(64, 3) and num(10) == sp.Rational(64, 3)
assert crossings(3 * x, x**2 + 2) == [1, 2]
assert area(3 * x, x**2 + 2, 1, 2) == sp.Rational(1, 6) and num(11) == sp.Rational(1, 6)
a12 = area(1 / x, 1 / x**2, 1, 2)
assert sp.simplify(a12 - (sp.log(2) - sp.Rational(1, 2))) == 0 and key(12) == "ln(2) - 1/2"
assert area(x**3, x, -1, 0) == sp.Rational(1, 4) and num(13) == sp.Rational(1, 4)
assert crossings(x + 2, x**2) == [-1, 2]
assert area(x + 2, x**2, -1, 2) == sp.Rational(9, 2) and num(14) == sp.Rational(9, 2)
# q15 area under |cos| on [0, pi]
a15 = sp.integrate(sp.cos(x), (x, 0, sp.pi / 2)) - sp.integrate(sp.cos(x), (x, sp.pi / 2, sp.pi))
assert a15 == 2 and num(15) == 2
assert crossings(sp.Integer(9), x**2) == [-3, 3]
assert area(sp.Integer(9), x**2, -3, 3) == 36 and num(16) == 36
assert area(x**2, -x**2, 0, 1) == sp.Rational(2, 3) and num(17) == sp.Rational(2, 3)
assert [r for r in crossings(4 * x, x**3) if r >= 0] == [0, 2]
assert area(4 * x, x**3, 0, 2) == 4 and num(18) == 4
assert area(sp.log(x), sp.Integer(0), 1, sp.E) == 1 and num(19) == 1
assert crossings(x**2 - 2 * x, sp.Integer(0)) == [0, 2]
assert area(sp.Integer(0), x**2 - 2 * x, 0, 2) == sp.Rational(4, 3) and num(20) == sp.Rational(4, 3)
# q21 reversed order gives the negative
assert sp.integrate(x**2 - x, (x, 0, 1)) == sp.Rational(-1, 6)
assert key(21).startswith("the subtraction is backwards")
a22 = sp.simplify(sp.integrate(2**x, (x, 0, 2)) - sp.integrate(x, (x, 0, 2)))
assert sp.simplify(a22 - (3 / sp.log(2) - 2)) == 0 and key(22) == "3/ln(2) - 2"
assert crossings(6 - x**2, x) == [-3, 2]
assert (6 - x**2 - x).subs(x, 0) > 0
assert key(23) == "int from -3 to 2 of (6 - x^2 - x) dx"
a24 = sp.integrate(sp.sin(x), (x, 0, sp.pi)) - sp.integrate(sp.sin(x), (x, sp.pi, 2 * sp.pi))
assert a24 == 4 and num(24) == 4
assert crossings(x**3, x) == [-1, 0, 1]
assert (x**3 - x).subs(x, sp.Rational(-1, 2)) > 0 and (x**3 - x).subs(x, sp.Rational(1, 2)) < 0
assert key(25).startswith("the curves cross at x = -1, 0, and 1")

print("verify_c8_4: all checks passed")
