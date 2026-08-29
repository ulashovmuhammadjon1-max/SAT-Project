# Verification for CALC 7.1. Run: python3 verify_c7_1.py
import sympy as sp
from c7_1 import QUESTIONS as Q

t, k, M, s, V, S, y = sp.symbols('t k M s V S y', positive=True)


def key(i):
    return Q[i - 1]["choices"][Q[i - 1]["ans"]]


# --- structure -------------------------------------------------------------
assert len(Q) == 25, len(Q)
for i, item in enumerate(Q, 1):
    assert len(item["choices"]) == 4, i
    assert len(set(item["choices"])) == 4, i
    assert 0 <= item["ans"] < 4, i
    assert item["why"].endswith("."), i

# --- q7: y proportional to t forces a constant derivative ------------------
assert sp.diff(k * t, t) == k
assert key(7) == "y = kt, so dy/dt = k is constant"

# --- q8: dy/dt = kt integrates to kt^2/2, NOT to a proportional-to-y model --
assert sp.integrate(k * t, t) == k * t**2 / 2
assert key(8) == "dy/dt = kt"

# --- q13: mixing tank. In 2 lb/gal * 5 gal/min; out (S/200)*5 -------------
rate_in = sp.Integer(2) * 5
rate_out = (S / 200) * 5
assert sp.simplify(rate_in - rate_out - (10 - S / 40)) == 0
assert key(13) == "dS/dt = 10 - S/40"

# --- q19: sphere surface area is proportional to V^(2/3) -------------------
r = sp.Symbol('r', positive=True)
Vol = sp.Rational(4, 3) * sp.pi * r**3
Area = 4 * sp.pi * r**2
r_of_V = sp.solve(sp.Eq(Vol, V), r)[0]
assert sp.simplify(Area.subs(r, r_of_V) / V**sp.Rational(2, 3) - (36 * sp.pi)**sp.Rational(1, 3)) == 0
assert key(19) == "dV/dt = -kV^(2/3)"

# --- q23: cube dissolving. 3s^2 ds/dt = -6k s^2  =>  ds/dt = -2k -----------
dsdt = sp.Symbol('dsdt')
sol = sp.solve(sp.Eq(3 * s**2 * dsdt, -k * 6 * s**2), dsdt)[0]
assert sp.simplify(sol - (-2 * k)) == 0, sol
assert sp.diff(sol, s) == 0  # constant in s
assert key(23).startswith("ds/dt is a negative constant")

# --- q25: k(M - y) is decreasing in y and vanishes at y = M ----------------
expr = k * (M - y)
assert sp.diff(expr, y) == -k
assert expr.subs(y, M) == 0
assert key(25).startswith("The rate of change is largest when y is farthest below M")

# --- q21: logistic factor vanishes at the carrying capacity ---------------
assert (sp.Rational(2, 5) * y * (1 - y / 800)).subs(y, 800) == 0
assert key(21).startswith("A population growing logistically")

# --- q12: net constant rate ------------------------------------------------
assert 7 - 3 == 4
assert key(12) == "dV/dt = 4"

# --- q24: units of k are 1/time -------------------------------------------
assert key(24) == "per hour"

print("verify_c7_1: all checks passed")
