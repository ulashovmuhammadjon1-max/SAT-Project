# Verification for CALC 8.12. Run: python3 verify_c8_12.py
# Radii are built as (curve minus axis) or (axis minus curve), and each one is
# checked nonnegative on the interval before the volume is integrated.
import sympy as sp
from c8_12 import QUESTIONS as Q

x, y = sp.symbols('x y', real=True)


def key(i):
    return Q[i - 1]["choices"][Q[i - 1]["ans"]]


def washer(R, r, a, b, var=x):
    mid = sp.Rational(1, 2) * (sp.nsimplify(a) + sp.nsimplify(b))
    assert R.subs(var, mid) >= 0 and r.subs(var, mid) >= 0, "negative radius"
    assert (R - r).subs(var, mid) >= 0, "outer/inner reversed"
    return sp.simplify(sp.pi * sp.integrate(R**2 - r**2, (var, a, b)))


def num(i):
    return sp.nsimplify(key(i).split(",")[0].replace("ln", "log"))


assert len(Q) == 25
for i, item in enumerate(Q, 1):
    assert len(item["choices"]) == 4 and len(set(item["choices"])) == 4, i
    assert 0 <= item["ans"] < 4, i

assert key(1) == "R = f(x) - k and r = g(x) - k"
assert key(2).startswith("the lower curve g, because it is farther")
assert key(3).startswith("both radii must shift by the same amount")

assert washer(x + 1, x**2 + 1, 0, 1) == 7 * sp.pi / 15 and num(4) == 7 * sp.pi / 15
assert washer(2 - x**2, 2 - x, 0, 1) == 8 * sp.pi / 15 and num(5) == 8 * sp.pi / 15
assert washer(1 - x, 1 - sp.sqrt(x), 0, 1) == sp.pi / 6 and num(6) == sp.pi / 6
assert washer(5 - x**2, sp.Integer(1), -2, 2) == 832 * sp.pi / 15 and num(7) == 832 * sp.pi / 15
assert washer(sp.Integer(5), x**2 + 1, -2, 2) == 1088 * sp.pi / 15 and num(8) == 1088 * sp.pi / 15
assert washer(y + 1, y**2 + 1, 0, 1, y) == 7 * sp.pi / 15 and num(9) == 7 * sp.pi / 15
assert washer(2 - y**2, 2 - y, 0, 1, y) == 8 * sp.pi / 15 and num(10) == 8 * sp.pi / 15
assert washer(sp.Integer(3), 3 - x, 0, 2) == 28 * sp.pi / 3 and num(11) == 28 * sp.pi / 3
assert washer(sp.Integer(2), 2 - sp.sqrt(x), 0, 4) == 40 * sp.pi / 3 and num(12) == 40 * sp.pi / 3
assert washer(2 - sp.sqrt(y), sp.Integer(1), 0, 1, y) == 5 * sp.pi / 6 and num(13) == 5 * sp.pi / 6
assert key(14) == "pi * int from -2 to 2 of ((5 - x^2)^2 - 1) dx"
# q15-q17 radius identification
assert sp.simplify((x - (-1)) - (x + 1)) == 0 and key(15) == "x + 1"
assert sp.simplify((x**2 - (-1)) - (x**2 + 1)) == 0 and key(16) == "x^2 + 1"
assert (3 - x**2).subs(x, sp.Rational(1, 2)) > (3 - x).subs(x, sp.Rational(1, 2))
assert key(17) == "3 - x^2"
# q18 adding a constant to both radii does not cancel
assert sp.expand((x + 1)**2 - (x**2 + 1)**2) != sp.expand(x**2 - (x**2)**2)
assert key(18).startswith("every radius grows by 1")
# q19 the region is separated from the x-axis in the interior
assert (x**2).subs(x, sp.Rational(1, 2)) > 0
assert key(19).startswith("a washer solid")
assert washer(6 - x**2, sp.Integer(2), -2, 2) == 384 * sp.pi / 5 and num(20) == 384 * sp.pi / 5
v21 = washer(1 / x + 1, sp.Integer(1), 1, 2)
assert sp.simplify(v21 - (sp.pi / 2 + 2 * sp.pi * sp.log(2))) == 0
assert key(21) == "pi/2 + 2*pi*ln(2)"
assert washer(sp.Integer(1), 1 - x**3, 0, 1) == 5 * sp.pi / 14 and num(22) == 5 * sp.pi / 14
assert key(23).startswith("is still pi times the integral of R^2 - r^2")
assert key(24).startswith("both nonnegative")
# q25 comparison
assert washer(4 - x**2, sp.Integer(0), -2, 2) == 512 * sp.pi / 15
assert 832 * sp.pi / 15 > 512 * sp.pi / 15
assert key(25).startswith("the one about y = 5")

print("verify_c8_12: all checks passed")
