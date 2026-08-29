# Verification for CALC 7.6. Run: python3 verify_c7_6.py
# Each keyed general solution is substituted into its differential equation and
# the residual must simplify to 0. Implicit answers are differentiated with
# sympy.idiff. The named distractors are checked NOT to satisfy the equation.
import sympy as sp
from c7_6 import QUESTIONS as Q

x = sp.Symbol('x', positive=True)
C = sp.Symbol('C', positive=True)
y = sp.Symbol('y', positive=True)


def key(i):
    return Q[i - 1]["choices"][Q[i - 1]["ans"]]


def solves(expr, rhs):
    """expr is y(x); rhs is dy/dx written in x and y."""
    return sp.simplify(sp.diff(expr, x) - rhs.subs(y, expr)) == 0


def implicit_solves(relation, rhs):
    """relation is an expression equal to 0; check idiff gives rhs."""
    return sp.simplify(sp.idiff(relation, y, x) - rhs) == 0


assert len(Q) == 25
for i, item in enumerate(Q, 1):
    assert len(item["choices"]) == 4 and len(set(item["choices"])) == 4, i
    assert 0 <= item["ans"] < 4, i

# q1
assert solves(C * sp.exp(x**2 / 2), x * y) and not solves(C * sp.exp(x**2), x * y)
assert key(1) == "y = C*e^(x^2/2)"
# q2
assert solves(C * x, y / x) and not solves(C * sp.exp(x), y / x)
assert key(2) == "y = Cx"
# q3
assert solves(-1 / (x**2 + C), 2 * x * y**2) and not solves(1 / (x**2 + C), 2 * x * y**2)
assert key(3) == "y = -1/(x^2 + C)"
# q4
assert implicit_solves(y**2 - x**2 - C, x / y)
assert not implicit_solves(y**2 - x**2 / 2 - C, x / y)
assert key(4) == "y^2 = x^2 + C"
# q5
assert solves(C * sp.exp(3 * x), 3 * y)
assert key(5) == "y = C*e^(3x)"
# q6
assert solves(C * sp.exp(-x**2), -2 * x * y)
assert key(6) == "y = C*e^(-x^2)"
# q7
assert implicit_solves(y**2 - x**2 - 2 * x - C, (x + 1) / y)
assert not implicit_solves(y**2 - x**2 - x - C, (x + 1) / y)
assert key(7) == "y^2 = x^2 + 2x + C"
# q8
assert implicit_solves(y**2 - 2 * sp.exp(x) - C, sp.exp(x) / y)
assert key(8) == "y^2 = 2e^x + C"
# q9
assert solves(C * sp.exp(sp.sin(x)), y * sp.cos(x))
assert not solves(C * sp.exp(sp.cos(x)), y * sp.cos(x))
assert key(9) == "y = C*e^(sin(x))"
# q10
assert implicit_solves(y**2 + 2 * sp.cos(x) - C, sp.sin(x) / y)
assert key(10) == "y^2 = -2cos(x) + C"
# q11
assert solves(C * sp.exp(x**4), 4 * x**3 * y)
assert key(11) == "y = C*e^(x^4)"
# q12
assert solves(C * x - 1, (1 + y) / x) and not solves(C * x + 1, (1 + y) / x)
assert key(12) == "y = Cx - 1"
# q13
assert solves(C * sp.exp(x**2 / 2) - 1, x * (y + 1))
assert key(13) == "y = C*e^(x^2/2) - 1"
# q14
assert solves((x + C)**2, 2 * sp.sqrt(y))
assert not solves((2 * x + C)**2, 2 * sp.sqrt(y))
assert key(14) == "y = (x + C)^2"
# q15 separating x^2 y^3
assert sp.simplify(y**-3 * (x**2 * y**3) - x**2) == 0
assert key(15) == "y^(-3) dy = x^2 dx"
# q16 x + y is not a product f(x)g(y)
assert sp.simplify(sp.diff((x + y) / y, y)) != 0  # ratio still depends on y
assert key(16) == "dy/dx = x + y"
# q17 conceptual
assert key(17).startswith("the two constants can be combined")
# q18
k = sp.Symbol('k')
assert sp.simplify(sp.diff(C * sp.exp(k * x), x) - k * (C * sp.exp(k * x))) == 0
assert key(18) == "y = C*e^(kx)"
# q19
assert implicit_solves(y**3 - x**2 - C, 2 * x / (3 * y**2))
assert key(19) == "y^3 = x^2 + C"
# q20
assert solves(sp.tan(x + C), y**2 + 1)
assert key(20) == "y = tan(x + C)"
# q21
assert solves(C * sp.exp(sp.tan(x)), y * sp.sec(x)**2)
assert key(21) == "y = C*e^(tan(x))"
# q22
sol22 = -sp.log(C - x**2 / 2)
assert sp.simplify(sp.diff(sol22, x) - x * sp.exp(sol22)) == 0
assert key(22) == "y = -ln(C - x^2/2)"
# q23
assert implicit_solves(y**2 - x**3 - x - C, (3 * x**2 + 1) / (2 * y))
assert key(23) == "y^2 = x^3 + x + C"
# q24
assert solves(C * sp.exp(2 * x**3), 6 * x**2 * y)
assert not solves(C * sp.exp(6 * x**3), 6 * x**2 * y)
assert key(24) == "y = C*e^(2x^3)"
# q25 the exponentiation error: C*e^(x^2) solves it, e^(x^2) + C does not
assert solves(C * sp.exp(x**2), 2 * x * y)
assert not solves(sp.exp(x**2) + C, 2 * x * y)
assert key(25).startswith("exponentiating both sides gives")

print("verify_c7_6: all checks passed")
