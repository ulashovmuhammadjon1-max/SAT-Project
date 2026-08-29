# Verification for CALC 8.11. Run: python3 verify_c8_11.py
import sympy as sp
from c8_11 import QUESTIONS as Q

x, y = sp.symbols('x y', real=True)


def key(i):
    return Q[i - 1]["choices"][Q[i - 1]["ans"]]


def washer(R, r, a, b, var=x):
    mid = sp.Rational(1, 2) * (sp.nsimplify(a) + sp.nsimplify(b))
    assert (R - r).subs(var, mid) >= 0, "outer/inner reversed"
    return sp.simplify(sp.pi * sp.integrate(R**2 - r**2, (var, a, b)))


def num(i):
    return sp.nsimplify(key(i).split(",")[0].replace("ln", "log"))


assert len(Q) == 25
for i, item in enumerate(Q, 1):
    assert len(item["choices"]) == 4 and len(set(item["choices"])) == 4, i
    assert 0 <= item["ans"] < 4, i

assert key(1) == "pi * int of (R(x)^2 - r(x)^2) dx"
R, r = sp.symbols('R r')
assert sp.expand((R - r)**2) != sp.expand(R**2 - r**2)
assert key(2).startswith("the area of a washer is pi*R^2 - pi*r^2")

assert sorted(sp.solve(x - x**2, x)) == [0, 1]
assert washer(x, x**2, 0, 1) == 2 * sp.pi / 15 and num(3) == 2 * sp.pi / 15
assert washer(sp.sqrt(x), x, 0, 1) == sp.pi / 6 and num(4) == sp.pi / 6
assert sorted(sp.solve(4 - x**2, x)) == [-2, 2]
assert washer(sp.Integer(4), x**2, -2, 2) == 256 * sp.pi / 5 and num(5) == 256 * sp.pi / 5
assert washer(sp.Integer(2), 1 / x, 1, 2) == 7 * sp.pi / 2 and num(6) == 7 * sp.pi / 2
assert washer(x**2, x**3, 0, 1) == 2 * sp.pi / 35 and num(7) == 2 * sp.pi / 35
assert washer(y, y**2, 0, 1, y) == 2 * sp.pi / 15 and num(8) == 2 * sp.pi / 15
assert washer(sp.sqrt(y), y, 0, 1, y) == sp.pi / 6 and num(9) == sp.pi / 6
assert key(10).startswith("the distance from the axis of revolution to the farther")
v11 = washer(sp.exp(x), sp.Integer(1), 0, 1)
assert sp.simplify(v11 - sp.pi * (sp.exp(2) - 3) / 2) == 0 and key(11) == "pi*(e^2 - 3)/2"
assert sorted(sp.solve((4 - x**2) - 3, x)) == [-1, 1]
assert washer(4 - x**2, sp.Integer(3), -1, 1) == 136 * sp.pi / 15 and num(12) == 136 * sp.pi / 15
assert key(13) == "pi * int from 0 to 1 of (x^2 - x^4) dx"
assert sorted(sp.solve(2 * x - x**2, x)) == [0, 2]
assert washer(2 * x, x**2, 0, 2) == 64 * sp.pi / 15 and num(14) == 64 * sp.pi / 15
assert washer(sp.Integer(4), y**2, -2, 2, y) == 256 * sp.pi / 5 and num(15) == 256 * sp.pi / 5
assert washer(sp.Integer(1), 1 / x, 1, 3) == 4 * sp.pi / 3 and num(16) == 4 * sp.pi / 3
assert key(17).startswith("the inner radius is 0")
assert washer(sp.Integer(1), sp.sin(x), 0, sp.pi / 2) == sp.pi**2 / 4 and num(18) == sp.pi**2 / 4
assert washer(x, x**3, 0, 1) == 4 * sp.pi / 21 and num(19) == 4 * sp.pi / 21
assert washer(sp.sqrt(x), x**2, 0, 1) == 3 * sp.pi / 10 and num(20) == 3 * sp.pi / 10
assert washer(sp.Integer(2), x, 0, 2) == 16 * sp.pi / 3 and num(21) == 16 * sp.pi / 3
assert key(22).startswith("the two circles that form a washer are concentric")
# q23 reversing the subtraction negates the integral
assert sp.integrate(x**4 - x**2, (x, 0, 1)) == -sp.integrate(x**2 - x**4, (x, 0, 1))
assert key(23) == "the computed volume is the negative of the correct one"
assert key(24) == "cubic inches"
# q25 the y-axis solid is larger
assert sp.pi / 6 > 2 * sp.pi / 15
assert key(25).startswith("the one from revolving about the y-axis")

print("verify_c8_11: all checks passed")
