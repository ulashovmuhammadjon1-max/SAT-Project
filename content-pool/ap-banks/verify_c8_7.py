# Verification for CALC 8.7. Run: python3 verify_c8_7.py
import sympy as sp
from c8_7 import QUESTIONS as Q

x, y = sp.symbols('x y', real=True)


def key(i):
    return Q[i - 1]["choices"][Q[i - 1]["ans"]]


def vol(area, a, b, var=x):
    return sp.simplify(sp.integrate(area, (var, a, b)))


def num(i):
    return sp.nsimplify(key(i).replace("ln", "log"))


assert len(Q) == 25
for i, item in enumerate(Q, 1):
    assert len(item["choices"]) == 4 and len(set(item["choices"])) == 4, i
    assert 0 <= item["ans"] < 4, i

assert key(1) == "int from a to b of A(x) dx"
assert key(2).startswith("with respect to x")
assert key(3) == "(f(x) - g(x))^2"

assert vol(x**2, 0, 4) == sp.Rational(64, 3) and num(4) == sp.Rational(64, 3)
assert vol(sp.sqrt(x)**2, 0, 4) == 8 and num(5) == 8
assert vol((4 - x**2)**2, -2, 2) == sp.Rational(512, 15) and num(6) == sp.Rational(512, 15)
assert vol((x - x**2)**2, 0, 1) == sp.Rational(1, 30) and num(7) == sp.Rational(1, 30)
assert vol(2 * (x - x**2)**2, 0, 1) == sp.Rational(1, 15) and num(8) == sp.Rational(1, 15)
assert vol((2 * sp.sqrt(4 - x**2))**2, -2, 2) == sp.Rational(128, 3) and num(9) == sp.Rational(128, 3)
v10 = vol(sp.exp(x)**2, 0, 1)
assert sp.simplify(v10 - (sp.exp(2) - 1) / 2) == 0 and key(10) == "(e^2 - 1)/2"
assert vol(y**2, 0, 3, y) == 9 and num(11) == 9
assert vol(3 * x**2, 0, 2) == 8 and num(12) == 8
# q13 diagonal: area is d^2/2
assert vol(x**2 / 2, 0, 2) == sp.Rational(4, 3) and num(13) == sp.Rational(4, 3)
assert key(14) == "int from -2 to 2 of (4 - x^2)^2 dx"
assert vol((2 - x)**2, 0, 2) == sp.Rational(8, 3) and num(15) == sp.Rational(8, 3)
assert vol(sp.sin(x)**2, 0, sp.pi) == sp.pi / 2 and key(16) == "pi/2"
assert vol(5 * (4 - x**2), -2, 2) == sp.Rational(160, 3) and num(17) == sp.Rational(160, 3)
assert sp.integrate(4 - x**2, (x, -2, 2)) == sp.Rational(32, 3)
assert key(18) == "cubic centimeters"
assert key(19).startswith("pi belongs to circular cross sections")
assert vol(2 * (x - x**2), 0, 1) == sp.Rational(1, 3) and num(20) == sp.Rational(1, 3)
assert vol((1 / x)**2, 1, 3) == sp.Rational(2, 3) and num(21) == sp.Rational(2, 3)
assert sorted(sp.solve(2 * x - x**2, x)) == [0, 2]
assert vol((2 * x - x**2)**2, 0, 2) == sp.Rational(16, 15) and num(22) == sp.Rational(16, 15)
assert vol(sp.sqrt(y)**2, 0, 4, y) == 8 and num(23) == 8
assert vol((6 - 2 * x)**2, 0, 3) == 36 and num(24) == 36
# q25 diagonal-to-area relation
d = sp.Symbol('d', positive=True)
assert sp.simplify((d / sp.sqrt(2))**2 - d**2 / 2) == 0
assert key(25) == "half the square of the segment length"

print("verify_c8_7: all checks passed")
