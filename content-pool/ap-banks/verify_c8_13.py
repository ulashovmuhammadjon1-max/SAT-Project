# Verification for CALC 8.13. Run: python3 verify_c8_13.py
# Arc lengths are integrated from sqrt(1 + (f')^2) directly; the "perfect
# square" cases are checked by confirming the radicand really is a square.
import sympy as sp
from c8_13 import QUESTIONS as Q

x = sp.Symbol('x', positive=True)
t = sp.Symbol('t', positive=True)


def key(i):
    return Q[i - 1]["choices"][Q[i - 1]["ans"]]


def arc(f, a, b, var=x):
    return sp.simplify(sp.integrate(sp.sqrt(1 + sp.diff(f, var)**2), (var, a, b)))


def param_arc(xt, yt, a, b):
    speed = sp.sqrt(sp.diff(xt, t)**2 + sp.diff(yt, t)**2)
    return sp.simplify(sp.integrate(sp.simplify(speed), (t, a, b)))


def num(i):
    return sp.nsimplify(key(i).replace("ln", "log"))


assert len(Q) == 25
for i, item in enumerate(Q, 1):
    assert len(item["choices"]) == 4 and len(set(item["choices"])) == 4, i
    assert 0 <= item["ans"] < 4, i

assert key(1) == "int from a to b of sqrt(1 + (f'(x))^2) dx"
assert key(2) == "int from c to d of sqrt(1 + (g'(y))^2) dy"
assert key(3) == "int from a to b of sqrt((dx/dt)^2 + (dy/dt)^2) dt"
assert key(4) == "sqrt((dx/dt)^2 + (dy/dt)^2)"

assert arc(3 * x + 1, 0, 4) == 4 * sp.sqrt(10) and num(5) == 4 * sp.sqrt(10)
assert arc(sp.Rational(2, 3) * x**sp.Rational(3, 2), 0, 3) == sp.Rational(14, 3)
assert num(6) == sp.Rational(14, 3)
# q7 the radicand is a perfect square
f7 = x**3 / 3 + 1 / (4 * x)
assert sp.simplify(1 + sp.diff(f7, x)**2 - (x**2 + 1 / (4 * x**2))**2) == 0
assert sp.simplify(sp.integrate(x**2 + 1 / (4 * x**2), (x, 1, 2)) - sp.Rational(59, 24)) == 0
assert num(7) == sp.Rational(59, 24)
# q8 sec integral
xa = sp.Symbol('xa')
f8 = sp.log(sp.cos(xa))
assert sp.simplify(1 + sp.diff(f8, xa)**2 - sp.sec(xa)**2) == 0
L8 = sp.integrate(sp.sec(xa), (xa, 0, sp.pi / 4))
assert sp.Abs(sp.N(L8 - sp.log(1 + sp.sqrt(2)))) < sp.Float("1e-25")
assert sp.simplify(sp.diff(sp.log(sp.sec(xa) + sp.tan(xa)), xa) - sp.sec(xa)) == 0
assert sp.simplify(sp.log(sp.sec(xa) + sp.tan(xa)).subs(xa, sp.pi / 4) - sp.log(1 + sp.sqrt(2))) == 0
assert key(8) == "ln(1 + sqrt(2))"
# q9 catenary
f9 = (sp.exp(xa) + sp.exp(-xa)) / 2
assert sp.simplify(1 + sp.diff(f9, xa)**2 - ((sp.exp(xa) + sp.exp(-xa)) / 2)**2) == 0
L9 = sp.integrate((sp.exp(xa) + sp.exp(-xa)) / 2, (xa, 0, 1))
assert sp.simplify(L9 - (sp.E - 1 / sp.E) / 2) == 0
assert key(9) == "(e - 1/e)/2"
# q10
f10 = sp.Rational(2, 3) * (x**2 + 1)**sp.Rational(3, 2)
assert sp.simplify(1 + sp.diff(f10, x)**2 - (2 * x**2 + 1)**2) == 0
assert sp.integrate(2 * x**2 + 1, (x, 0, 1)) == sp.Rational(5, 3) and num(10) == sp.Rational(5, 3)
# q11
L11 = arc(x**sp.Rational(3, 2), 0, 4)
assert sp.simplify(L11 - sp.Rational(8, 27) * (10 * sp.sqrt(10) - 1)) == 0
assert key(11) == "(8/27)*(10*sqrt(10) - 1)"
assert key(12) == "int from 0 to 2 of sqrt(1 + 4x^2) dx"
assert key(13) == "int from 1 to e of sqrt(1 + 1/x^2) dx"
assert param_arc(3 * sp.cos(t), 3 * sp.sin(t), 0, sp.pi) == 3 * sp.pi and num(14) == 3 * sp.pi
L15 = param_arc(t**2, t**3, 0, 1)
assert sp.simplify(L15 - (13 * sp.sqrt(13) - 8) / 27) == 0
assert key(15) == "(13*sqrt(13) - 8)/27"
assert key(16) == "int from a to b of sqrt((x'(t))^2 + (y'(t))^2) dt"
assert key(17) == "int from a to b of |v(t)| dt"
assert key(18).startswith("the curve is at least as long")
assert key(19) == "f' exists and is continuous there"
assert key(20) == "meters"
assert arc(sp.Integer(4), 1, 7) == 6 and num(21) == 6
# q22 dropping the 1 gives the integral of |f'|
assert sp.sqrt(sp.diff(3 * x, x)**2) == 3
assert key(22).startswith("the total variation of f")
assert key(23) == "int from 0 to 1 of sqrt(1 + 4y^2) dy"
assert sp.sqrt(9 + 16) == 5 and 5 * 2 == 10 and num(24) == 10
# q25
f25 = sp.Rational(1, 3) * (x**2 + 2)**sp.Rational(3, 2)
assert sp.simplify(1 + sp.diff(f25, x)**2 - (x**2 + 1)**2) == 0
assert sp.integrate(x**2 + 1, (x, 0, 3)) == 12 and num(25) == 12

print("verify_c8_13: all checks passed")
