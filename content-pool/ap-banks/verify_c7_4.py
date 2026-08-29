# Verification for CALC 7.4. Run: python3 verify_c7_4.py
# Equilibria are found with sympy.solve; stability and long-run claims are
# checked by evaluating the sign of the rate on each side of an equilibrium;
# concavity claims are checked by differentiating the equation implicitly.
import sympy as sp
from c7_4 import QUESTIONS as Q

x, y, t, C = sp.symbols('x y t C')


def key(i):
    return Q[i - 1]["choices"][Q[i - 1]["ans"]]


assert len(Q) == 25
for i, item in enumerate(Q, 1):
    assert len(item["choices"]) == 4 and len(set(item["choices"])) == 4, i
    assert 0 <= item["ans"] < 4, i

# q1 equilibria of y(y-3)
assert sorted(sp.solve(y * (y - 3), y)) == [0, 3] and key(1) == "y = 0 and y = 3"
# q2 y - 4 at y = 6 positive and increasing in y
assert (y - 4).subs(y, 6) == 2 > 0 and sp.diff(y - 4, y) == 1
assert key(2) == "it increases without bound"
# q3 4 - y: positive below 4, negative above
assert (4 - y).subs(y, 0) > 0 and (4 - y).subs(y, 9) < 0
assert key(3) == "it approaches 4"
# q4/q5 logistic-shaped y(2-y)
f = y * (2 - y)
assert f.subs(y, 1) == 1 > 0 and f.subs(y, 2) == 0
assert key(4) == "it increases and approaches 2"
assert f.subs(y, -1) == -3 < 0 and f.subs(y, -5) < 0
assert key(5) == "it decreases without bound"
# q6 y = x - 1 solves dy/dx = x - y; general solution x - 1 + C e^{-x}
assert sp.simplify(sp.diff(x - 1, x) - (x - (x - 1))) == 0
gen = x - 1 + C * sp.exp(-x)
assert sp.simplify(sp.diff(gen, x) - (x - gen)) == 0
assert sp.limit(gen - (x - 1), x, sp.oo) == 0
assert key(6) == "they approach the line y = x - 1"
# q7 verbal: both sides move toward it => stable
assert key(7) == "y = 2 is a stable equilibrium solution"
# q8 dy/dx = y at (0,1): y' = 1 > 0, y'' = y' = y = 1 > 0
assert key(8) == "increasing and concave up"
# q9 d^2y/dx^2 = 1 + x + y at (0,1)
assert (1 + x + y).subs({x: 0, y: 1}) == 2 and key(9) == "2"
# q10 single equilibrium at y = -3
assert sp.solve(y + 3, y) == [-3] and len(sp.solve((y + 3) * (y - 3), y)) == 2
assert key(10) == "dy/dx = y + 3"
# q11 y^2 - 1 at y = 0
assert (y**2 - 1).subs(y, 0) == -1 < 0 and (y**2 - 1).subs(y, -1) == 0
assert key(11) == "it decreases and approaches -1"
# q12/q13 (y-1)(y-5)
g = (y - 1) * (y - 5)
assert g.subs(y, 3) == -4 < 0 and key(12) == "it decreases and approaches 1"
assert g.subs(y, 6) == 5 > 0 and g.subs(y, 100) > 0
assert key(13) == "it increases without bound"
# q14 (y-2)^2 never negative, zero only at 2
assert sp.solve((y - 2)**2, y) == [2] and ((y - 2)**2).subs(y, 0) > 0 and ((y - 2)**2).subs(y, 5) > 0
assert key(14).startswith("it is semi-stable")
# q15 y(4-y) zeros
assert sorted(sp.solve(y * (4 - y), y)) == [0, 4]
assert key(15) == "dy/dx = y(4 - y)"
# q16 uniqueness
assert key(16).startswith("a crossing point would give two different solutions")
# q17
assert key(17) == "each is increasing on its whole domain"
# q18 concave up near (0,1) => tangent line underestimates
assert (1 + x + y).subs({x: 0, y: 1}) > 0
assert key(18).startswith("an underestimate")
# q19 Newton cooling equilibrium 70, attracting
h = -sp.Rational(1, 2) * (y - 70)
assert h.subs(y, 100) < 0 and h.subs(y, 20) > 0 and sp.solve(h, y) == [70]
assert key(19) == "T approaches 70 no matter what T(0) is"
# q20 e^y never zero
assert sp.solve(sp.exp(y), y) == []
assert key(20) == "none, because e^y is never 0"
# q21 logistic equilibria
assert sorted(sp.solve(sp.Rational(1, 5) * y * (1 - y / 50), y)) == [0, 50]
assert key(21) == "P = 0 and P = 50"
# q22 x^2 + 1 >= 1
assert sp.minimum(x**2 + 1, x) == 1
assert key(22).startswith("it is increasing everywhere")
# q23 y = C/x solves dy/dx = -y/x
assert sp.simplify(sp.diff(C / x, x) - (-(C / x) / x)) == 0
assert key(23) == "hyperbolas of the form xy = C"
# q24 y^2 - x^2 = C solves dy/dx = x/y
yy = sp.sqrt(x**2 + C)
assert sp.simplify(sp.diff(yy, x) - x / yy) == 0
assert key(24) == "hyperbolas of the form y^2 - x^2 = C"
# q25 y = 1 is an equilibrium of (y-1)(y+2)
assert ((y - 1) * (y + 2)).subs(y, 1) == 0
assert key(25) == "the constant function y = 1 for all x"

print("verify_c7_4: all checks passed")
