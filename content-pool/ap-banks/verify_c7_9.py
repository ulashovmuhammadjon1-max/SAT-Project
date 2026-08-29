# Verification for CALC 7.9. Run: python3 verify_c7_9.py
# Carrying capacities come from sp.solve, the fastest-growth population from
# maximizing the logistic rate, and the long-run values from sp.limit.
import sympy as sp
from c7_9 import QUESTIONS as Q

P, t = sp.symbols('P t', positive=True)
k, K, A = sp.symbols('k K A', positive=True)


def key(i):
    return Q[i - 1]["choices"][Q[i - 1]["ans"]]


def peak(rate):
    """Population at which the logistic rate is maximal, and that maximum."""
    crit = sp.solve(sp.diff(rate, P), P)
    crit = [c for c in crit if c.is_real and c > 0]
    assert len(crit) == 1, crit
    return crit[0], sp.simplify(rate.subs(P, crit[0]))


assert len(Q) == 25
for i, item in enumerate(Q, 1):
    assert len(item["choices"]) == 4 and len(set(item["choices"])) == 4, i
    assert 0 <= item["ans"] < 4, i

# q1-q3  dP/dt = 0.5 P (1 - P/200)
r1 = sp.Rational(1, 2) * P * (1 - P / 200)
Pr = sp.Symbol('Pr', real=True)
assert sorted(sp.solve(sp.Rational(1, 2) * Pr * (1 - Pr / 200), Pr)) == [0, 200]
assert key(1) == "200"
p1, m1 = peak(r1)
assert p1 == 100 and m1 == 25
assert key(2) == "100"
assert key(3) == "25"

# q4-q6  dP/dt = 0.03 P (500 - P)
r2 = sp.Rational(3, 100) * P * (500 - P)
assert sorted(sp.solve(Pr * (500 - Pr), Pr)) == [0, 500]
assert key(4) == "500"
p2, m2 = peak(r2)
assert p2 == 250 and m2 == 1875
assert key(5) == "250"
assert key(6) == "1875"

# q7/q8 long-run behavior of the logistic solution
gen = K / (1 + A * sp.exp(-k * t))
assert sp.limit(gen, t, sp.oo) == K
assert key(7) == "K"
rate = k * P * (1 - P / K)
assert rate.subs({k: 1, K: 100}).subs(P, 200) < 0     # above K the rate is negative
assert key(8) == "it decreases toward K"

# q9 inflection at K/2: the second derivative of the solution vanishes there
kk, KK = sp.Rational(1, 2), sp.Integer(200)
sol = KK / (1 + 3 * sp.exp(-kk * t))
infl = sp.solve(sp.diff(sol, t, 2), t)
infl = [s for s in infl if s.is_real]
assert len(infl) == 1
assert sp.simplify(sol.subs(t, infl[0]) - KK / 2) == 0
assert key(9) == "P = K/2, half the carrying capacity"

# q10 equilibria
assert sorted(sp.solve(Pr * (1 - Pr / 100), Pr)) == [0, 100]
assert key(10) == "P = 0 and P = K"

# q11 the general solution really solves the equation
kx, Kx, Ax = sp.symbols('kx Kx Ax', positive=True)
g = Kx / (1 + Ax * sp.exp(-kx * t))
assert sp.simplify(sp.diff(g, t) - kx * g * (1 - g / Kx)) == 0
assert key(11) == "P = K/(1 + A*e^(-kt))"

# q12-q14  P = 800/(1 + 7 e^{-0.2 t})
p14 = 800 / (1 + 7 * sp.exp(-sp.Rational(1, 5) * t))
assert sp.limit(p14, t, sp.oo) == 800 and key(12) == "800"
assert p14.subs(t, 0) == 100 and key(13) == "100"
tstar = sp.solve(sp.Eq(p14, 400), t)
tstar = [s for s in tstar if s.is_real][0]
assert abs(float(tstar) - 9.73) < 0.005
assert sp.simplify(tstar - sp.log(7) / sp.Rational(1, 5)) == 0
assert key(14) == "9.73"

# q15  2P - 0.01P^2 = 2P(1 - P/200)
assert sp.simplify(2 * P - sp.Rational(1, 100) * P**2 - 2 * P * (1 - P / 200)) == 0
assert key(15) == "dP/dt = 2P - 0.01P^2"

# q16 small P behaves exponentially
assert sp.limit(rate / (k * P), P, 0) == 1
assert key(16).startswith("exponential, since the factor")

# q17 concave up below K/2: check the sign of the second derivative
assert sp.diff(sol, t, 2).subs(t, infl[0] - 1) > 0
assert sp.diff(sol, t, 2).subs(t, infl[0] + 1) < 0
assert key(17) == "while P is below K/2"

# q18 P(0) = K is the equilibrium solution
assert rate.subs(P, K) == 0
assert key(18) == "the constant function P = K"

# q19 long run of 0.1 y (1 - y/50)
assert sorted(sp.solve(Pr * (1 - Pr / 50), Pr)) == [0, 50]
assert key(19) == "50"

# q20 rate at P = 30 for 0.4 P (1 - P/60)
assert (sp.Rational(2, 5) * P * (1 - P / 60)).subs(P, 30) == 6
assert key(20) == "6"

# q21 maximum rate kK/4
pg, mg = peak(rate)
assert sp.simplify(pg - K / 2) == 0 and sp.simplify(mg - k * K / 4) == 0
assert key(21) == "kK/4"

# q22 rate is 0 at P = K
assert rate.subs(P, K) == 0 and rate.subs({k: 1, K: 100}).subs(P, 50) > 0
assert key(22).startswith("at the carrying capacity the growth rate is 0")

# q23  P = 1200/(1 + 3 e^{-0.5 t}), fastest at P = 600
p23 = 1200 / (1 + 3 * sp.exp(-sp.Rational(1, 2) * t))
t23 = [s for s in sp.solve(sp.Eq(p23, 600), t) if s.is_real][0]
assert abs(float(t23) - 2.20) < 0.005
assert key(23) == "2.20"

# q24 max of 0.02 P (1000 - P)
p24, m24 = peak(sp.Rational(1, 50) * P * (1000 - P))
assert p24 == 500 and m24 == 5000
assert key(24) == "5000"

# q25 rate at 900 is positive but smaller than at 500 (K = 1000)
r25 = P * (1 - P / 1000)
assert r25.subs(P, 900) > 0 and r25.subs(P, 900) < r25.subs(P, 500)
assert key(25).startswith("it is still increasing, but more slowly")

print("verify_c7_9: all checks passed")
