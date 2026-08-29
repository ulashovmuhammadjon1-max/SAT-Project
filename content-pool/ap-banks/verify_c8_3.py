# Verification for CALC 8.3. Run: python3 verify_c8_3.py
import sympy as sp
from c8_3 import QUESTIONS as Q

t = sp.Symbol('t')
x = sp.Symbol('x', positive=True)


def key(i):
    return Q[i - 1]["choices"][Q[i - 1]["ans"]]


assert len(Q) == 25
for i, item in enumerate(Q, 1):
    assert len(item["choices"]) == 4 and len(set(item["choices"])) == 4, i
    assert 0 <= item["ans"] < 4, i

assert key(1).startswith("the number of gallons that flowed in")
assert key(2) == "50 + int from 0 to 10 of r(t) dt"
assert key(3) == "R(b) - R(a)"
# q4 FTC part 1
f = sp.Function('f')
assert sp.diff(sp.Integral(f(t), (t, 0, x)), x).doit() == f(x)
assert key(4) == "f(x)"

# q5
assert sp.integrate(t**2 - 1, (t, 0, 3)) == 6 and key(5) == "6"
assert key(6) == "wherever f(x) > 0"
assert key(7) == "f changes from positive to negative at c"
assert key(8) == "wherever f is increasing"

# q9 net rate (5 + t) - 3
assert sp.integrate((5 + t) - 3, (t, 0, 6)) == 30 and key(9) == "30 gallons"
assert key(10) == "O(t) > I(t)"

# q11 net rate 8 - t peaks the amount at t = 8
net = (10 - t) - 2
assert sp.solve(net, t) == [8]
assert net.subs(t, 7) > 0 and net.subs(t, 9) < 0
assert key(11) == "t = 8"

# q12 bacteria
tot = sp.integrate(100 * sp.exp(sp.Rational(1, 10) * t), (t, 0, 10))
assert sp.simplify(tot - 1000 * (sp.E - 1)) == 0 and round(float(tot)) == 1718
assert key(12) == "1718"

assert sp.integrate(1 / t, (t, 1, sp.E)) == 1 and key(13) == "1"
assert 10 + sp.integrate(6 * t, (t, 0, 4)) == 58 and key(14) == "58 gallons"
assert sp.integrate(3 * t**2 - 12, (t, 0, 4)) == 16 and key(15) == "16"
assert key(16).startswith("the change in the amount of water")
assert key(17) == "meters"

# q18 piecewise accumulation
F4 = sp.integrate(t, (t, 0, 2)) + sp.integrate(2, (t, 2, 4))
assert F4 == 6 and key(18) == "6"

assert key(19) == "the change in population over the ten years"
assert key(20).startswith("the additional cost of increasing production")
assert key(21) == "120 liters of oil over the five hours"
assert key(22).startswith("(1/20) * int from 0 to 20")

# q23 draining 4 gal/min for 10 min from 100 gallons
assert 100 - sp.integrate(4, (t, 0, 10)) == 60
assert key(23).startswith("60 gallons")

# q24 negative integrand
assert sp.integrate(-1, (t, 0, 5)) < 0
assert key(24) == "F is decreasing and F(5) < 0"

assert key(25) == "int from 1 to 4 of (F(t) - S(t)) dt"

print("verify_c8_3: all checks passed")
