# Verification for CALC 7.5. Run: python3 verify_c7_5.py
# A generic exact-rational Euler routine recomputes every approximation, and
# the keyed string is compared against it.
import sympy as sp
from c7_5 import QUESTIONS as Q

x, y = sp.symbols('x y')


def key(i):
    return Q[i - 1]["choices"][Q[i - 1]["ans"]]


def euler(f, x0, y0, h, n):
    """Exact rational Euler stepping; f is a sympy expression in x and y."""
    xi, yi = sp.nsimplify(x0), sp.nsimplify(y0)
    hh = sp.nsimplify(h)
    for _ in range(n):
        yi = sp.simplify(yi + hh * f.subs({x: xi, y: yi}))
        xi = xi + hh
    return sp.nsimplify(yi)


def eq(i, value):
    assert sp.nsimplify(key(i)) == sp.nsimplify(value), (i, key(i), value)


assert len(Q) == 25
for i, item in enumerate(Q, 1):
    assert len(item["choices"]) == 4 and len(set(item["choices"])) == 4, i
    assert 0 <= item["ans"] < 4, i

eq(1, euler(x + y, 0, 1, sp.Rational(1, 2), 1))            # 3/2
eq(2, euler(x + y, 0, 1, sp.Rational(1, 2), 2))            # 5/2
eq(3, euler(2 * x, 1, 3, sp.Rational(1, 10), 1))           # 3.2
eq(4, euler(y, 0, 2, sp.Rational(1, 4), 2))                # 3.125
eq(5, euler(x - y, 0, 4, 1, 1))                            # 0
eq(6, euler(x - y, 0, 4, 1, 2))                            # 1
eq(7, euler(x * y, 1, 2, sp.Rational(1, 2), 1))            # 3
eq(8, euler(x * y, 1, 2, sp.Rational(1, 2), 2))            # 5.25
eq(9, sp.Rational(2, 4))                                   # step size
assert key(10).startswith("following the tangent line")
assert key(11) == "y_(n+1) = y_n + h*f(x_n, y_n)"
assert key(12).startswith("an underestimate, because each tangent line lies below")
assert key(13) == "an overestimate"
eq(14, euler(y**2, 0, 1, sp.Rational(1, 10), 2))           # 1.221
eq(15, euler(x + y, 1, 2, sp.Rational(-1, 2), 2))          # 0
# q16 error against the exact solution y = x^2 + 1
approx = euler(2 * x, 0, 1, sp.Rational(1, 2), 2)
exact = (x**2 + 1).subs(x, 1)
assert approx == sp.Rational(3, 2) and exact == 2
eq(16, exact - approx)                                     # 0.5
eq(17, euler(3 - y, 0, 1, sp.Rational(1, 5), 2))           # 1.72
eq(18, euler(1 / x, 1, 0, sp.Rational(1, 2), 2))           # 5/6
eq(19, euler(2 * y - 4, 0, 3, sp.Rational(1, 2), 2))       # 6
eq(20, euler(x**2 - y, 2, 1, sp.Rational(1, 10), 1))       # 1.3
eq(21, euler(y / 2, 0, 4, 1, 3))                           # 13.5
eq(22, euler(x + 2, 1, 5, sp.Rational(1, 4), 1))           # 5.75
eq(23, euler(-2 * x * y, 0, 1, sp.Rational(1, 2), 2))      # 0.5
assert key(24).startswith("it is roughly halved")
# q25 both estimates, and the concavity that ranks them
assert euler(x + y, 0, 1, 1, 1) == 2 and euler(x + y, 0, 1, sp.Rational(1, 2), 2) == sp.Rational(5, 2)
assert (1 + x + y).subs({x: 0, y: 1}) > 0
assert key(25).startswith("the solution is concave up here")

# distractors must not coincide with the key numerically
for i, item in enumerate(Q, 1):
    vals = []
    for c in item["choices"]:
        try:
            vals.append(sp.nsimplify(c))
        except Exception:
            vals = []
            break
    if vals:
        assert len(set(vals)) == 4, i

print("verify_c7_5: all checks passed")
