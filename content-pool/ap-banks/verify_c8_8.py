# Verification for CALC 8.8. Run: python3 verify_c8_8.py
# The cross-section area formulas are themselves derived symbolically, then each
# volume is integrated by sympy and compared with the keyed string.
import sympy as sp
from c8_8 import QUESTIONS as Q

x, y = sp.symbols('x y', real=True)
s = sp.Symbol('s', positive=True)

EQUI = sp.sqrt(3) / 4
SEMI = sp.pi / 8          # diameter s
RIGHT_LEG = sp.Rational(1, 2)
RIGHT_HYP = sp.Rational(1, 4)


def key(i):
    return Q[i - 1]["choices"][Q[i - 1]["ans"]]


def vol(area, a, b, var=x):
    return sp.simplify(sp.integrate(area, (var, a, b)))


def num(i):
    return sp.nsimplify(key(i).replace("pi", "pi"))


assert len(Q) == 25
for i, item in enumerate(Q, 1):
    assert len(item["choices"]) == 4 and len(set(item["choices"])) == 4, i
    assert 0 <= item["ans"] < 4, i

# --- the area formulas, derived rather than assumed -----------------------
height = sp.sqrt(s**2 - (s / 2)**2)
assert sp.simplify(sp.Rational(1, 2) * s * height - EQUI * s**2) == 0
assert sp.simplify(sp.Rational(1, 2) * sp.pi * (s / 2)**2 - SEMI * s**2) == 0
leg = s / sp.sqrt(2)                       # isosceles right triangle, hypotenuse s
assert sp.simplify(sp.Rational(1, 2) * leg**2 - RIGHT_HYP * s**2) == 0
assert sp.simplify(sp.Rational(1, 2) * s * s - RIGHT_LEG * s**2) == 0
assert key(1) == "(sqrt(3)/4)*s^2"
assert key(2) == "(pi/8)*s^2"
assert key(3) == "s^2/4"
assert key(4) == "s^2/2"

assert vol(EQUI * (2 * x)**2, 0, 3) == 9 * sp.sqrt(3) and num(5) == 9 * sp.sqrt(3)
assert sp.integrate((1 - x**2)**2, (x, -1, 1)) == sp.Rational(16, 15)
assert vol(SEMI * (1 - x**2)**2, -1, 1) == 2 * sp.pi / 15 and num(6) == 2 * sp.pi / 15
assert vol(EQUI * (2 * sp.sqrt(9 - x**2))**2, -3, 3) == 36 * sp.sqrt(3) and num(7) == 36 * sp.sqrt(3)
assert sorted(sp.solve((2 - x**2) - x**2, x)) == [-1, 1]
assert sp.integrate((2 - 2 * x**2)**2, (x, -1, 1)) == sp.Rational(64, 15)
assert vol(SEMI * (2 - 2 * x**2)**2, -1, 1) == 8 * sp.pi / 15 and num(8) == 8 * sp.pi / 15
assert vol(RIGHT_LEG * (sp.sqrt(x))**2, 0, 16) == 64 and num(9) == 64
assert vol(RIGHT_HYP * x**2, 0, 6) == 18 and num(10) == 18
assert vol(SEMI * (2 - x)**2, 0, 2) == sp.pi / 3 and num(11) == sp.pi / 3
assert vol(SEMI * (2 * sp.sqrt(1 - x**2))**2, -1, 1) == 2 * sp.pi / 3 and num(12) == 2 * sp.pi / 3
assert key(13).startswith("(pi/8) * int")
assert sp.integrate(sp.cos(x)**2, (x, -sp.pi / 2, sp.pi / 2)) == sp.pi / 2
assert vol(EQUI * sp.cos(x)**2, -sp.pi / 2, sp.pi / 2) == sp.sqrt(3) * sp.pi / 8
assert num(14) == sp.sqrt(3) * sp.pi / 8
v15 = vol(SEMI * sp.exp(2 * x)**2, 0, 1)
assert sp.simplify(sp.integrate(sp.exp(4 * x), (x, 0, 1)) - (sp.exp(4) - 1) / 4) == 0
assert sp.simplify(v15 - sp.pi * (sp.exp(4) - 1) / 32) == 0
assert key(15) == "pi*(e^4 - 1)/32"
# q16 radius vs diameter: the wrong formula is 4 times too big
assert sp.simplify((sp.pi / 2 * s**2) / (SEMI * s**2)) == 4
assert key(16).startswith("s is the diameter")
assert key(17) == "(pi/2)*s^2"
assert vol(EQUI * (x**3)**2, 0, 1) == sp.sqrt(3) / 28 and num(18) == sp.sqrt(3) / 28
assert vol(RIGHT_LEG * (4 - y**2)**2, -2, 2, y) == sp.Rational(256, 15)
assert num(19) == sp.Rational(256, 15)
assert vol(EQUI * (1 / x)**2, 1, 4) == 3 * sp.sqrt(3) / 16 and num(20) == 3 * sp.sqrt(3) / 16
assert sp.integrate((4 - x)**2, (x, 0, 4)) == sp.Rational(64, 3)
assert vol(SEMI * (4 - x)**2, 0, 4) == 8 * sp.pi / 3 and num(21) == 8 * sp.pi / 3
# q22 the ratio of semicircular to square cross sections
assert sp.simplify((SEMI * s**2) / s**2 - sp.pi / 8) == 0 and sp.pi / 8 < 1
assert key(22).startswith("the semicircular solid has pi/8")
assert sorted(sp.solve(3 * x - x**2, x)) == [0, 3]
assert sp.integrate((3 * x - x**2)**2, (x, 0, 3)) == sp.Rational(81, 10)
assert vol(EQUI * (3 * x - x**2)**2, 0, 3) == 81 * sp.sqrt(3) / 40
assert num(23) == 81 * sp.sqrt(3) / 40
# q24 triangle of height twice the base
assert sp.simplify(sp.Rational(1, 2) * s * (2 * s) - s**2) == 0
assert vol(x**2, 0, 3) == 9 and num(24) == 9
assert key(25) == "(f(x) - g(x))/2"

print("verify_c8_8: all checks passed")
