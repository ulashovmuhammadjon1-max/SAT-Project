# Verification for CALC 7.2. Run: python3 verify_c7_2.py
# Each check substitutes the proposed function into the differential equation
# and confirms the residual simplifies to 0 (and that the distractors do not).
import sympy as sp
from c7_2 import QUESTIONS as Q

x = sp.Symbol('x', positive=True)
t = sp.Symbol('t')


def key(i):
    return Q[i - 1]["choices"][Q[i - 1]["ans"]]


def solves(expr, residual, var=x):
    """residual(y, y', y'') should simplify to 0."""
    return sp.simplify(residual(expr, sp.diff(expr, var), sp.diff(expr, var, 2))) == 0


assert len(Q) == 25
for i, item in enumerate(Q, 1):
    assert len(item["choices"]) == 4 and len(set(item["choices"])) == 4, i
    assert 0 <= item["ans"] < 4, i

# q1  dy/dx = 3y
assert solves(sp.exp(3 * x), lambda y, y1, y2: y1 - 3 * y)
assert not solves(3 * sp.exp(x), lambda y, y1, y2: y1 - 3 * y)
assert not solves(x**3, lambda y, y1, y2: y1 - 3 * y)
assert key(1) == "y = e^(3x)"

# q2  dy/dx = -5y
assert solves(4 * sp.exp(-5 * x), lambda y, y1, y2: y1 + 5 * y)
assert not solves(4 * sp.exp(5 * x), lambda y, y1, y2: y1 + 5 * y)
assert key(2) == "y = 4e^(-5x)"

# q3  y = x^2 + 3
assert sp.diff(x**2 + 3, x) == 2 * x
assert key(3) == "dy/dx = 2x"

# q4  y'' + 9y = 0
assert solves(sp.cos(3 * x), lambda y, y1, y2: y2 + 9 * y)
for bad in (sp.cos(9 * x), sp.exp(3 * x), sp.sin(x / 3)):
    assert not solves(bad, lambda y, y1, y2: y2 + 9 * y)
assert key(4) == "y = cos(3x)"

# q5  which is NOT a solution of y' = y
assert not solves(x * sp.exp(x), lambda y, y1, y2: y1 - y)
for good in (sp.exp(x), 2 * sp.exp(x), -3 * sp.exp(x)):
    assert solves(good, lambda y, y1, y2: y1 - y)
assert key(5) == "y = x*e^x"

# q6  y = 5e^(x^2)
assert solves(5 * sp.exp(x**2), lambda y, y1, y2: y1 - 2 * x * y)
assert key(6) == "dy/dx = 2xy"

# q7  y = 1/x
assert solves(1 / x, lambda y, y1, y2: y1 + y**2)
assert key(7) == "dy/dx = -y^2"

# q8  y = tan x
assert solves(sp.tan(x), lambda y, y1, y2: y1 - (1 + y**2))
assert key(8) == "dy/dx = 1 + y^2"

# q9  y = x ln x
assert solves(x * sp.log(x), lambda y, y1, y2: x * y1 - (y + x))
assert key(9) == "x*dy/dx = y + x"

# q10 y = e^(-x) + 2
assert solves(sp.exp(-x) + 2, lambda y, y1, y2: y1 - (2 - y))
assert key(10) == "dy/dx = 2 - y"

# q11 implicit circle
y = sp.Function('y')
impl = sp.diff(x**2 + y(x)**2 - 25, x)
dydx = sp.solve(impl, sp.Derivative(y(x), x))[0]
assert sp.simplify(dydx + x / y(x)) == 0
assert key(11) == "dy/dx = -x/y"

# q12 y = 3x^2
assert solves(3 * x**2, lambda yy, y1, y2: x * y1 - 2 * yy)
assert key(12) == "x*dy/dx = 2y"

# q13 y = e^(2x) in y'' - 5y' + 6y = 0
assert solves(sp.exp(2 * x), lambda yy, y1, y2: y2 - 5 * y1 + 6 * yy)
assert key(13).startswith("Yes, because 4e^(2x) - 10e^(2x) + 6e^(2x) = 0")

# q14 y'' - y = 0
assert solves(sp.exp(-x), lambda yy, y1, y2: y2 - yy)
for bad in (sp.sin(x), sp.cos(x), x**2):
    assert not solves(bad, lambda yy, y1, y2: y2 - yy)
assert key(14) == "y = e^(-x)"

# q15 y = 2e^(3t) - 1 solves dy/dt = 3y + 3, y(0) = 1
f = 2 * sp.exp(3 * t) - 1
assert sp.simplify(sp.diff(f, t) - (3 * f + 3)) == 0
assert f.subs(t, 0) == 1
assert sp.simplify(sp.diff(f, t) - 3 * f) != 0
assert key(15) == "dy/dt = 3y + 3, y(0) = 1"

# q16 y = e^(kx) in y'' + y' - 6y = 0
roots = sp.solve(sp.Symbol('k')**2 + sp.Symbol('k') - 6, sp.Symbol('k'))
assert set(roots) == {2, -3}
for bad in (3, -2, 6):
    assert bad**2 + bad - 6 != 0
assert key(16) == "k = 2"

# q17 y = x^r in x^2 y'' - 2y = 0
r = sp.Symbol('r')
assert set(sp.solve(r * (r - 1) - 2, r)) == {2, -1}
for bad in (1, -2, 3):
    assert sp.simplify(x**2 * sp.diff(x**bad, x, 2) - 2 * x**bad) != 0
assert key(17) == "r = 2"

# q18 particular solution through (2, 7)
C = sp.Symbol('C')
assert sp.solve(sp.Eq(2**2 + C, 7), C)[0] == 3
assert key(18) == "C = 3"

# q19 y = A x^3 solves dy/dx = 3y/x for every A
A = sp.Symbol('A')
assert sp.simplify(sp.diff(A * x**3, x) - 3 * (A * x**3) / x) == 0
assert key(19) == "every real number A"

# q20 general solution of dy/dx = 4x^3
assert sp.integrate(4 * x**3, x) == x**4
assert key(20) == "y = x^4 + C"

# q21 definition, no computation
assert key(21).startswith("substituting f and its derivatives")

# q22 y = e^(2x) + 5 fails dy/dx = 2y
g = sp.exp(2 * x) + 5
assert sp.simplify(sp.diff(g, x) - 2 * g) == -10
assert key(22).startswith("No, because dy/dx = 2e^(2x)")

# q23 family solving dy/dx = y^2
Cs = sp.Symbol('Cs')
assert sp.simplify(sp.diff(-1 / (x + Cs), x) - (-1 / (x + Cs))**2) == 0
assert sp.simplify(sp.diff(1 / (x + Cs), x) - (1 / (x + Cs))**2) != 0
assert key(23) == "y = -1/(x + C)"

# q24 y = sqrt(x^2 + 4)
assert solves(sp.sqrt(x**2 + 4), lambda yy, y1, y2: y1 - x / yy)
assert key(24) == "dy/dx = x/y"

# q25 y = e^(x^2/2)
assert solves(sp.exp(x**2 / 2), lambda yy, y1, y2: y1 - x * yy)
assert key(25) == "dy/dx = x*y"

print("verify_c7_2: all checks passed")
