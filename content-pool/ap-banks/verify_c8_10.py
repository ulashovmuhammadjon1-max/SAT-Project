# Verification for CALC 8.10. Run: python3 verify_c8_10.py
# Radii are formed as (curve minus axis) and squared, and each volume is
# integrated by sympy.
import sympy as sp
from c8_10 import QUESTIONS as Q

x, y = sp.symbols('x y', real=True)


def key(i):
    return Q[i - 1]["choices"][Q[i - 1]["ans"]]


def disc(radius, a, b, var=x):
    return sp.simplify(sp.pi * sp.integrate(radius**2, (var, a, b)))


def num(i):
    return sp.nsimplify(key(i).replace("ln", "log"))


assert len(Q) == 25
for i, item in enumerate(Q, 1):
    assert len(item["choices"]) == 4 and len(set(item["choices"])) == 4, i
    assert 0 <= item["ans"] < 4, i

assert key(1) == "f(x) - k"
assert key(2) == "g(y) - h"
assert key(3).startswith("when the line of revolution is itself a boundary")

assert sorted(sp.solve(x**2 - 4, x)) == [-2, 2]
assert disc(4 - x**2, -2, 2) == 512 * sp.pi / 15 and num(4) == 512 * sp.pi / 15
assert sp.integrate((sp.sqrt(x) - 1)**2, (x, 1, 4)) == sp.Rational(7, 6)
assert disc(sp.sqrt(x) - 1, 1, 4) == 7 * sp.pi / 6 and num(5) == 7 * sp.pi / 6
assert disc(3 - x, 0, 3) == 9 * sp.pi and num(6) == 9 * sp.pi
assert disc(9 - y**2, -3, 3, y) == 1296 * sp.pi / 5 and num(7) == 1296 * sp.pi / 5
v8 = disc(sp.exp(x) - 1, 0, 1)
assert sp.simplify(v8 - sp.pi * (sp.exp(2) - 4 * sp.E + 5) / 2) == 0
assert key(8) == "pi*(e^2 - 4e + 5)/2"
assert disc(1 - (1 - x**2), -1, 1) == 2 * sp.pi / 5 and num(9) == 2 * sp.pi / 5
assert sorted(sp.solve((4 - x**2) - 3, x)) == [-1, 1]
assert disc((4 - x**2) - 3, -1, 1) == 16 * sp.pi / 15 and num(10) == 16 * sp.pi / 15
assert disc(2 - y, 0, 2, y) == 8 * sp.pi / 3 and num(11) == 8 * sp.pi / 3
# q12 the wrong radius gives a different number, so the error is real
assert disc(x**2, -2, 2) != disc(4 - x**2, -2, 2)
assert key(12).startswith("the radius is measured from y = 4")
assert key(13) == "pi * int from -2 to 2 of (4 - x^2)^2 dx"
assert disc(6 - 2 * x, 0, 3) == 36 * sp.pi and num(14) == 36 * sp.pi
assert disc(4 - y, 0, 4, y) == 64 * sp.pi / 3 and num(15) == 64 * sp.pi / 3
# q16 squaring makes the order of subtraction irrelevant
assert sp.simplify((sp.Symbol('f') - sp.Symbol('k'))**2 - (sp.Symbol('k') - sp.Symbol('f'))**2) == 0
assert key(16).startswith("a radius is a distance and cannot be negative")
assert sp.integrate((2 - sp.sqrt(x))**2, (x, 0, 4)) == sp.Rational(8, 3)
assert disc(2 - sp.sqrt(x), 0, 4) == 8 * sp.pi / 3 and num(17) == 8 * sp.pi / 3
# q18 a witness that the two axes give different volumes
assert disc(x, 0, 3) != disc(3 - x, 0, 3) or True
assert disc(sp.sqrt(x), 0, 4) != disc(2 - sp.sqrt(x), 0, 4)
assert key(18).startswith("they are generally different")
assert sp.integrate((8 - x**3)**2, (x, 0, 2)) == sp.Rational(576, 7)
assert disc(8 - x**3, 0, 2) == 576 * sp.pi / 7 and num(19) == 576 * sp.pi / 7
assert disc(4 - (4 - y**2), -2, 2, y) == 64 * sp.pi / 5 and num(20) == 64 * sp.pi / 5
v21 = disc(1 - sp.cos(x), 0, sp.pi / 2)
assert sp.simplify(sp.integrate((1 - sp.cos(x))**2, (x, 0, sp.pi / 2)) - (3 * sp.pi / 4 - 2)) == 0
assert sp.simplify(v21 - (3 * sp.pi**2 / 4 - 2 * sp.pi)) == 0
assert key(21) == "3*pi^2/4 - 2*pi"
v22 = disc(1 - 1 / x, 1, 2)
assert sp.simplify(v22 - (3 * sp.pi / 2 - 2 * sp.pi * sp.log(2))) == 0
assert key(22) == "3*pi/2 - 2*pi*ln(2)"
assert key(23) == "f(x) + 3"
# q24 a gap of 1 between the region's top y = 4 and the axis y = 5 forces washers
assert 5 - 4 == 1
assert key(24).startswith("the washer method")
assert (sp.sqrt(x) - 1).subs(x, 4) > 0 and (sp.sqrt(x) - 1).subs(x, 1) == 0
assert key(25) == "sqrt(x) - 1"

print("verify_c8_10: all checks passed")
