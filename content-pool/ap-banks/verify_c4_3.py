# Verification for CALC 4.3 — Rates of Change in Applied Contexts Other Than Motion.
# Every derivative and every decimal quoted in c4_3.py is recomputed here with sympy,
# including the distractor values, so that no distractor equals the key.
import sympy as sp

import c4_3

t, x, r, p = sp.symbols('t x r p', real=True, positive=True)


def approx(expr, digits=2):
    return round(float(expr), digits)


# q1-q3: P(t) = 500 e^(0.04 t)
P = 500 * sp.exp(sp.Rational(4, 100) * t)
dP = sp.diff(P, t)
assert sp.simplify(dP - 20 * sp.exp(t / 25)) == 0
assert approx(dP.subs(t, 10), 1) == 29.8
assert approx(500 * sp.exp(sp.Rational(2, 5)), 1) == 745.9      # chain-rule-free distractor
assert approx(20 * sp.exp(sp.Rational(4, 100)), 1) == 20.8
avg = (P.subs(t, 10) - P.subs(t, 0)) / 10
assert sp.simplify(avg - 50 * (sp.exp(sp.Rational(2, 5)) - 1)) == 0
assert approx(avg, 1) == 24.6

# q4-q5: V(t) = 100 - 5t + 0.05 t^2
V = 100 - 5 * t + sp.Rational(5, 100) * t**2
dV = sp.diff(V, t)
assert sp.simplify(dV - (-5 + t / 10)) == 0
assert dV.subs(t, 10) == -4
assert sp.solve(dV, t) == [50]

# q6-q7: T(t) = 70 + 30 e^(-0.1 t)
T = 70 + 30 * sp.exp(-t / 10)
dT = sp.diff(T, t)
assert sp.simplify(dT + 3 * sp.exp(-t / 10)) == 0
assert dT.subs(t, 0) == -3
assert approx(dT.subs(t, 10)) == -1.10
assert T.subs(t, 0) == 100

# q8: sphere, dV/dr at r = 2
Vs = sp.Rational(4, 3) * sp.pi * r**3
assert sp.simplify(sp.diff(Vs, r) - 4 * sp.pi * r**2) == 0
assert sp.diff(Vs, r).subs(r, 2) == 16 * sp.pi
assert Vs.subs(r, 2) == sp.Rational(32, 3) * sp.pi          # distractor, not equal to 16pi
assert sp.simplify(16 * sp.pi - sp.Rational(32, 3) * sp.pi) != 0

# q9: circle, dA/dr at r = 5
A = sp.pi * r**2
assert sp.diff(A, r).subs(r, 5) == 10 * sp.pi
assert A.subs(r, 5) == 25 * sp.pi

# q10-q12: revenue, cost, profit
R = 60 * x - sp.Rational(1, 2) * x**2
C = 1000 + 8 * x + sp.Rational(1, 100) * x**2
assert sp.diff(R, x).subs(x, 20) == 40 and R.subs(x, 20) == 1000
assert sp.diff(C, x).subs(x, 300) == 14
assert C.subs(x, 300) == 4300 and sp.nsimplify(C.subs(x, 300) / 300) == sp.Rational(43, 3)
Pr = R - C
assert sp.simplify(sp.diff(Pr, x) - (52 - sp.Rational(102, 100) * x)) == 0
assert sp.nsimplify(sp.diff(Pr, x).subs(x, 20)) == sp.Rational(158, 5)
assert float(sp.Rational(158, 5)) == 31.6

# q13: N(t) = 200 * 2^(t/3)
N = 200 * 2**(t / 3)
dN = sp.diff(N, t)
assert sp.simplify(dN - 200 * 2**(t / 3) * sp.log(2) / 3) == 0
assert sp.simplify(dN.subs(t, 0) - 200 * sp.log(2) / 3) == 0
assert approx(dN.subs(t, 0), 1) == 46.2
assert approx(200 * sp.log(2), 1) == 138.6
assert approx(600 * sp.log(2), 1) == 415.9

# q14: A(t) = 80 e^(-0.03 t)
Ar = 80 * sp.exp(-sp.Rational(3, 100) * t)
dAr = sp.diff(Ar, t)
assert sp.simplify(dAr + sp.Rational(24, 10) * sp.exp(-sp.Rational(3, 100) * t)) == 0
assert approx(dAr.subs(t, 20)) == -1.32

# q15-q16: C(t) = 5t/(t^2+1)
Cd = 5 * t / (t**2 + 1)
dCd = sp.simplify(sp.diff(Cd, t))
assert sp.simplify(dCd - 5 * (1 - t**2) / (t**2 + 1)**2) == 0
assert sp.nsimplify(dCd.subs(t, 2)) == sp.Rational(-3, 5)
assert float(sp.Rational(-3, 5)) == -0.6

# q17: h(t) = 20 - 18 e^(-0.25 t)
h = 20 - 18 * sp.exp(-t / 4)
dh = sp.diff(h, t)
assert sp.simplify(dh - sp.Rational(9, 2) * sp.exp(-t / 4)) == 0
assert approx(dh.subs(t, 4)) == 1.66
assert approx(h.subs(t, 4)) == 13.38

# q21: q(p) = 1200 - 3p^2
qd = 1200 - 3 * p**2
assert sp.diff(qd, p).subs(p, 10) == -60 and qd.subs(p, 10) == 900

# q22: cube
Vc = x**3
assert sp.diff(Vc, x).subs(x, 4) == 48
assert Vc.subs(x, 4) == 64 and (6 * x**2).subs(x, 4) == 96

# q23-q24: R(t) = 40t/(t+4)
Rt = 40 * t / (t + 4)
dRt = sp.simplify(sp.diff(Rt, t))
assert sp.simplify(dRt - 160 / (t + 4)**2) == 0
assert sp.nsimplify(dRt.subs(t, 4)) == sp.Rational(5, 2)
assert Rt.subs(t, 4) == 20
assert sp.limit(dRt, t, sp.oo) == 0 and sp.limit(Rt, t, sp.oo) == 40

# q25: logistic P(t) = 1000/(1 + 9 e^(-0.5 t))
Pl = 1000 / (1 + 9 * sp.exp(-t / 2))
dPl = sp.simplify(sp.diff(Pl, t))
t_half = sp.solve(sp.Eq(Pl, 500), t)[0]
assert sp.simplify(Pl.subs(t, t_half) - 500) == 0
assert sp.simplify(dPl.subs(t, t_half) - 125) == 0
# 125 really is the maximum growth rate of this logistic model
assert sp.simplify(sp.diff(Pl, t, 2).subs(t, t_half)) == 0

# Structure: 25 questions, four distinct choices, in-range key.
assert len(c4_3.QUESTIONS) == 25, len(c4_3.QUESTIONS)
for i, q in enumerate(c4_3.QUESTIONS, 1):
    assert len(q["choices"]) == 4, (i, len(q["choices"]))
    assert len(set(c.strip().lower() for c in q["choices"])) == 4, i
    assert 0 <= q["ans"] < 4, i
    assert "$" not in q["q"] and all("$" not in c for c in q["choices"]), i

print("c4_3: 25 questions, all applied rates verified with sympy, structure OK")
