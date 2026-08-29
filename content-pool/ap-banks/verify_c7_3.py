# Verification for CALC 7.3. Run: python3 verify_c7_3.py
# Slope values are evaluated with sympy; the verbal-description items are
# checked by testing the property claimed (zero set, sign, symmetry).
import sympy as sp
from c7_3 import QUESTIONS as Q

x, y = sp.symbols('x y')


def key(i):
    return Q[i - 1]["choices"][Q[i - 1]["ans"]]


def slope(expr, px, py):
    return sp.simplify(expr.subs({x: px, y: py}))


assert len(Q) == 25
for i, item in enumerate(Q, 1):
    assert len(item["choices"]) == 4 and len(set(item["choices"])) == 4, i
    assert 0 <= item["ans"] < 4, i

assert slope(2 * x - y, 1, 3) == -1 and key(1) == "-1"
assert slope(x + y, -2, 5) == 3 and key(2) == "3"
assert slope(x * y, 3, -2) == -6 and key(3) == "-6"

# q4 horizontal where y - 1 = 0
assert sp.solve(y - 1, y) == [1] and key(4) == "the horizontal line y = 1"
# q5 horizontal where x^2 - 4 = 0
assert sorted(sp.solve(x**2 - 4, x)) == [-2, 2]
assert key(5) == "the vertical lines x = -2 and x = 2"
# q6 y/x undefined at x = 0
assert sp.limit(sp.Abs(1 / x), x, 0) == sp.oo
assert key(6) == "points on the y-axis, where x = 0"
# q7 slope independent of y
assert sp.diff(x**2 + 1, y) == 0 and sp.diff(y**2 + 1, y) != 0
assert key(7) == "dy/dx = x^2 + 1"
# q8 slope independent of x
assert sp.diff(y**2 - 1, x) == 0 and sp.diff(x**2 - 1, x) != 0
assert key(8) == "dy/dx = y^2 - 1"
# q9
assert sp.solve(x - y, y) == [x] and key(9) == "the points on the line y = x"
# q10
assert sp.diff(sp.Integer(4), x) == 0 and key(10) == "dy/dx = 4"
# q11 xy > 0 in QI and QIII
assert slope(x * y, 2, 3) > 0 and slope(x * y, -2, -3) > 0
assert slope(x * y, -2, 3) < 0 and slope(x * y, 2, -3) < 0
assert key(11) == "the first and third quadrants"
# q12
assert slope(-x / y, 3, 4) == sp.Rational(-3, 4) and key(12) == "-3/4"
# q13 dy/dx = y: zero on x-axis, sign follows y, no x dependence
assert sp.diff(y, x) == 0 and slope(y, 5, 0) == 0 and slope(y, 5, 3) > 0 and slope(y, 5, -3) < 0
assert key(13) == "dy/dx = y"
# q14 dy/dx = -y
assert slope(-y, 5, 3) < 0 and slope(-y, 5, -3) > 0 and sp.diff(-y, x) == 0
assert key(14) == "dy/dx = -y"
# q15 sin(x) zeros
n = sp.Symbol('n', integer=True)
assert sp.sin(sp.pi * n).simplify() == 0 and sp.sin(sp.pi / 2) == 1
assert key(15) == "the vertical lines x = n*pi for every integer n"
# q16 x(y - 2) = 0
assert slope(x * (y - 2), 0, 7) == 0 and slope(x * (y - 2), 5, 2) == 0
assert slope(x * (y - 2), 1, 1) != 0
assert key(16) == "the points on the line y = 2 together with the points on the y-axis"
# q17
assert slope(x + 2 * y, 2, -3) == -4 and key(17) == "-4"
# q18 even in y
assert slope(x + y**2, 1, 2) == slope(x + y**2, 1, -2) == 5
assert slope(x + y, 1, 2) != slope(x + y, 1, -2)
assert slope(x * y, 1, 2) != slope(x * y, 1, -2)
assert key(18) == "dy/dx = x + y^2"
# q19 ln(y) domain
assert sp.log(sp.Rational(1, 2)).is_real and not sp.log(-1).is_real
assert key(19) == "only where y > 0"
# q20 sqrt(9) = 3
assert sp.sqrt(9) == 3 and not sp.sqrt(sp.Integer(-1)).is_real
assert key(20).startswith("slope 3, and the field exists only where x is greater than or equal to 0")
# q21 x^2 + y^2 zero only at origin, grows with distance
assert slope(x**2 + y**2, 0, 0) == 0 and slope(x**2 + y**2, 1, 1) == 2 and slope(x**2 + y**2, 3, 4) == 25
assert key(21) == "dy/dx = x^2 + y^2"
# q22 y^2 never negative
assert sp.Symbol('w', real=True)**2 >= 0
assert (y**2).subs(y, -7) == 49
assert key(22) == "dy/dx = y^2"
# q23 x - 1 sign pattern
assert slope(x - 1, 1, 0) == 0 and slope(x - 1, 0, 0) < 0 and slope(x - 1, 5, 0) > 0
assert key(23).startswith("segments are horizontal along the vertical line x = 1")
# q24 constant slope 2
assert sp.diff(sp.Integer(2), x) == 0
assert key(24).startswith("The right side does not depend on x")
# q25 e^(-x^2) positive and decreasing in |x|
assert sp.exp(-x**2).subs(x, 0) == 1
assert sp.exp(-x**2).subs(x, 3) < sp.exp(-x**2).subs(x, 1)
assert sp.limit(sp.exp(-x**2), x, sp.oo) == 0
assert key(25).startswith("every segment has positive slope, and the segments flatten")

print("verify_c7_3: all checks passed")
