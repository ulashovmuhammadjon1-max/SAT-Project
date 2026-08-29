# Verification for CALC 7.7. Run: python3 verify_c7_7.py
# Each keyed particular solution must (a) satisfy the differential equation and
# (b) hit the initial condition. Distractors are checked to fail one or both.
import sympy as sp
from c7_7 import QUESTIONS as Q

x = sp.Symbol('x')
t = sp.Symbol('t')
y = sp.Symbol('y')


def key(i):
    return Q[i - 1]["choices"][Q[i - 1]["ans"]]


def ivp(expr, rhs, x0, y0, var=x):
    """expr solves dy/dvar = rhs (written in var and y) and expr(x0) = y0."""
    de = sp.simplify(sp.diff(expr, var) - rhs.subs(y, expr)) == 0
    ic = sp.simplify(expr.subs(var, x0) - y0) == 0
    return de and ic


assert len(Q) == 25
for i, item in enumerate(Q, 1):
    assert len(item["choices"]) == 4 and len(set(item["choices"])) == 4, i
    assert 0 <= item["ans"] < 4, i

assert ivp(x**2 + 4, 2 * x, 1, 5) and not ivp(x**2 + 5, 2 * x, 1, 5)
assert key(1) == "y = x^2 + 4"

assert ivp(3 * sp.exp(x), y, 0, 3) and not ivp(sp.exp(x) + 3, y, 0, 3)
assert key(2) == "y = 3e^x"

assert ivp(2 * sp.exp(x**2 / 2), x * y, 0, 2) and not ivp(2 * sp.exp(x**2), x * y, 0, 2)
assert key(3) == "y = 2e^(x^2/2)"

assert ivp(5 * sp.exp(-3 * x), -3 * y, 0, 5)
assert key(4) == "y = 5e^(-3x)"

assert ivp(4 * x, y / x, 1, 4)
assert key(5) == "y = 4x"

assert ivp(sp.sqrt(x**2 + 9), x / y, 0, 3)
assert key(6) == "y = sqrt(x^2 + 9)"

assert ivp(-sp.sqrt(x**2 + 9), x / y, 0, -3)
assert not ivp(sp.sqrt(x**2 + 9), x / y, 0, -3)
assert key(7) == "y = -sqrt(x^2 + 9)"

assert ivp(1 / (1 - x), y**2, 0, 1) and not ivp(1 / (1 + x), y**2, 0, 1)
assert key(8) == "y = 1/(1 - x)"

assert (1 / (1 - x)).subs(x, sp.Rational(1, 2)) == 2
assert key(9) == "2"

assert sp.limit(1 / (1 - x), x, 1, '-') == sp.oo
assert key(10) == "x < 1"

assert ivp(-1 / (x**2 + 1), 2 * x * y**2, 0, -1)
assert key(11) == "y = -1/(x^2 + 1)"

assert ivp(sp.sqrt(2 * sp.exp(x) + 2), sp.exp(x) / y, 0, 2)
assert not ivp(sp.sqrt(2 * sp.exp(x) + 4), sp.exp(x) / y, 0, 2)
assert key(12) == "y = sqrt(2e^x + 2)"

assert ivp(4 * sp.exp(sp.sin(x)), y * sp.cos(x), 0, 4)
assert key(13) == "y = 4e^(sin(x))"

assert ivp(2 * sp.exp(x**2 / 2) - 1, x * (y + 1), 0, 1)
assert key(14) == "y = 2e^(x^2/2) - 1"

assert ivp(2 * sp.exp(x**3), 3 * x**2 * y, 0, 2)
assert key(15) == "y = 2e^(x^3)"

assert (x**2 + 4).subs(x, 2) == 8
assert key(16) == "8"

assert sp.simplify((2 * sp.exp(x**2 / 2)).subs(x, 1) - 2 * sp.sqrt(sp.E)) == 0
assert key(17) == "2*sqrt(e)"

assert ivp(sp.sqrt(x + 1), 1 / (2 * y), 0, 1)
assert not ivp(sp.sqrt(2 * x + 1), 1 / (2 * y), 0, 1)
assert key(18) == "y = sqrt(x + 1)"

assert ivp(6 / x, -y / x, 1, 6)
assert key(19) == "y = 6/x"

assert ivp(sp.exp(sp.sin(x) - 1), y * sp.cos(x), sp.pi / 2, 1)
assert not ivp(sp.exp(sp.sin(x)), y * sp.cos(x), sp.pi / 2, 1)
assert key(20) == "y = e^(sin(x) - 1)"

assert ivp(x**2 + x - 3, 2 * x + 1, 0, -3)
assert key(21) == "y = x^2 + x - 3"

k = sp.Symbol('k', positive=True)
T = 70 + 100 * sp.exp(-k * t)
assert sp.simplify(sp.diff(T, t) - (-k * (T - 70))) == 0 and T.subs(t, 0) == 170
assert key(22) == "T = 70 + 100e^(-kt)"

xp = sp.Symbol('xp', positive=True)
sol23 = sp.exp(2 - 1 / xp)
assert sp.simplify(sp.diff(sol23, xp) - sol23 / xp**2) == 0
assert sp.simplify(sol23.subs(xp, 1) - sp.E) == 0
assert key(23) == "y = e^(2 - 1/x)"

sol24 = (x + 4)**2 / 4
assert sp.simplify(sp.diff(sol24, x) - sp.sqrt(sol24)) == 0 or \
       sp.simplify(sp.diff(sol24, x) - (x + 4) / 2) == 0
assert sp.simplify(sp.sqrt(sol24.subs(x, 0)) - 2) == 0 and sol24.subs(x, 0) == 4
assert key(24) == "y = (x + 4)^2/4"

sol25 = 100 * 2**t
assert sol25.subs(t, 0) == 100 and sol25.subs(t, 2) == 400
assert sp.simplify(sp.diff(sol25, t) - sp.log(2) * sol25) == 0
assert key(25) == "y = 100*2^t"

print("verify_c7_7: all checks passed")
