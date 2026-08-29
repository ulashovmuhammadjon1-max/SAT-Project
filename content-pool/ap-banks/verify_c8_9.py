# Verification for CALC 8.9. Run: python3 verify_c8_9.py
import sympy as sp
from c8_9 import QUESTIONS as Q

x, y = sp.symbols('x y', real=True)


def key(i):
    return Q[i - 1]["choices"][Q[i - 1]["ans"]]


def disc(radius, a, b, var=x):
    return sp.simplify(sp.pi * sp.integrate(radius**2, (var, a, b)))


def num(i):
    return sp.nsimplify(key(i).split(",")[0].replace("ln", "log"))


assert len(Q) == 25
for i, item in enumerate(Q, 1):
    assert len(item["choices"]) == 4 and len(set(item["choices"])) == 4, i
    assert 0 <= item["ans"] < 4, i

assert key(1) == "pi * int from a to b of f(x)^2 dx"
assert key(2).startswith("pi * int of (the radius as a function of y)^2 dy")
assert key(3).startswith("the distance from the x-axis to the curve")

assert disc(x, 0, 3) == 9 * sp.pi and num(4) == 9 * sp.pi
assert disc(sp.sqrt(x), 0, 4) == 8 * sp.pi and num(5) == 8 * sp.pi
assert disc(x**2, 0, 2) == 32 * sp.pi / 5 and num(6) == 32 * sp.pi / 5
assert disc(1 / x, 1, 3) == 2 * sp.pi / 3 and num(7) == 2 * sp.pi / 3
v8 = disc(sp.exp(x), 0, 1)
assert sp.simplify(v8 - sp.pi * (sp.exp(2) - 1) / 2) == 0 and key(8) == "pi*(e^2 - 1)/2"
assert disc(sp.sin(x), 0, sp.pi) == sp.pi**2 / 2 and num(9) == sp.pi**2 / 2
assert disc(y**2, 0, 2, y) == 32 * sp.pi / 5 and num(10) == 32 * sp.pi / 5
assert disc(sp.sqrt(y), 0, 4, y) == 8 * sp.pi and num(11) == 8 * sp.pi
assert disc(2 * x + 1, 0, 2) == 62 * sp.pi / 3 and num(12) == 62 * sp.pi / 3
# q13 sphere of radius 3
assert disc(sp.sqrt(9 - x**2), -3, 3) == 36 * sp.pi
assert sp.simplify(sp.Rational(4, 3) * sp.pi * 3**3 - 36 * sp.pi) == 0
assert key(13).startswith("36*pi, a sphere of radius 3")
# q14 cone of radius 6, height 3
assert disc(2 * x, 0, 3) == 36 * sp.pi
assert sp.simplify(sp.Rational(1, 3) * sp.pi * 6**2 * 3 - 36 * sp.pi) == 0
assert key(14).startswith("36*pi, a cone of radius 6 and height 3")
assert key(15) == "pi * int from 0 to 4 of x dx"
assert key(16).startswith("the area of a disc is pi times the radius SQUARED")
assert disc(x**3, 0, 1) == sp.pi / 7 and num(17) == sp.pi / 7
assert disc(4 - x**2, -2, 2) == 512 * sp.pi / 15 and num(18) == 512 * sp.pi / 15
assert disc(sp.cos(x), 0, sp.pi / 2) == sp.pi**2 / 4 and num(19) == sp.pi**2 / 4
assert disc(1 - y**2, -1, 1, y) == 16 * sp.pi / 15 and num(20) == 16 * sp.pi / 15
# q21 cylinder
assert disc(sp.Integer(2), 0, 5) == 20 * sp.pi and num(21) == 20 * sp.pi
assert key(22) == "cubic meters"
xp = sp.Symbol('xp', positive=True)
v23 = sp.pi * sp.integrate(xp**sp.Rational(2, 3), (xp, 0, 8))
assert sp.simplify(v23 - 96 * sp.pi / 5) == 0 and num(23) == 96 * sp.pi / 5
assert disc(sp.sqrt(y), 0, 1, y) == sp.pi / 2 and num(24) == sp.pi / 2
assert key(25).startswith("discs perpendicular to the x-axis have thickness dx")

print("verify_c8_9: all checks passed")
