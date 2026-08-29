# Verification for CALC 7.8. Run: python3 verify_c7_8.py
import sympy as sp
from c7_8 import QUESTIONS as Q

t, k = sp.symbols('t k')


def key(i):
    return Q[i - 1]["choices"][Q[i - 1]["ans"]]


def close(a, b, places=2):
    return sp.Abs(sp.nsimplify(a) - b) < sp.Rational(1, 10**places * 2)


assert len(Q) == 25
for i, item in enumerate(Q, 1):
    assert len(item["choices"]) == 4 and len(set(item["choices"])) == 4, i
    assert 0 <= item["ans"] < 4, i

y0 = sp.Symbol('y0', positive=True)
kk = sp.Symbol('kk')
sol = y0 * sp.exp(kk * t)
assert sp.simplify(sp.diff(sol, t) - kk * sol) == 0 and sol.subs(t, 0) == y0
assert key(1) == "y = y0*e^(kt)"

# q2 doubling every 5 years
P = 200 * 2**(t / 5)
assert P.subs(t, 0) == 200 and P.subs(t, 5) == 400 and P.subs(t, 10) == 800
assert key(2) == "P = 200*2^(t/5)"

# q3 three half-lives from 80 g
assert 80 * sp.Rational(1, 2)**3 == 10
assert key(3) == "10 grams"

# q4 k from a 10-year half-life
kr = sp.Symbol('kr', real=True)
k4 = sp.solve(sp.Eq(sp.exp(10 * kr), sp.Rational(1, 2)), kr)
assert len(k4) == 1 and sp.simplify(k4[0] + sp.log(2) / 10) == 0
assert key(4) == "k = -ln(2)/10"

# q5 doubling time for k = 0.07
d5 = sp.log(2) / sp.Rational(7, 100)
assert close(9.9, sp.N(d5), 1)
assert key(5) == "9.9"

# q6 doubling time for k = 0.04
d6 = sp.log(2) / sp.Rational(4, 100)
assert abs(float(d6) - 17.33) < 0.005
assert key(6) == "17.33"

# q7 two half-lives
assert sp.Rational(1, 2)**2 == sp.Rational(1, 4)
assert key(7) == "1/4"

# q8 tripling every 4 hours, 9x
assert sp.solve(sp.Eq(3**(t / 4), 9), t)[0] == 8
assert key(8) == "8 hours"

# q9 y = 50 e^{0.2 t} at t = 10
assert sp.simplify((50 * sp.exp(sp.Rational(1, 5) * t)).subs(t, 10) - 50 * sp.exp(2)) == 0
assert key(9) == "50e^2"

# q10 decay solution
A = 200 * sp.exp(-sp.Rational(1, 20) * t)
assert sp.simplify(sp.diff(A, t) + sp.Rational(1, 20) * A) == 0 and A.subs(t, 0) == 200
assert key(10) == "A = 200e^(-0.05t)"

# q11 relative rate is constant
yf = sp.Function('y')
assert key(11).startswith("its relative rate of change")

# q12 0.9^t = e^{t ln 0.9}
for v in (0, 1, sp.Rational(3, 2), 5):
    assert sp.simplify(sp.Rational(9, 10)**v - sp.exp(v * sp.log(sp.Rational(9, 10)))) == 0
assert float(sp.log(0.9)) < 0
assert key(12) == "k = ln(0.9)"

# q13 100 -> 25 in 8 hours
h = sp.Symbol('h', positive=True)
assert sp.solve(sp.Eq(sp.Rational(1, 2)**(8 / h), sp.Rational(1, 4)), h) == [4]
assert key(13) == "4 hours"

# q14 y(0)=3, y(2)=12
f14 = 3 * 2**t
assert f14.subs(t, 0) == 3 and f14.subs(t, 2) == 12
assert (3 * 4**t).subs(t, 2) != 12
assert key(14) == "y = 3*2^t"

# q15 1000 e^{0.05 t} = 3000
t15 = sp.log(3) / sp.Rational(5, 100)
assert abs(float(t15) - 21.97) < 0.005
assert key(15) == "21.97"

# q16 meaning of k
assert key(16).startswith("the quantity grows at a continuous rate of 3 percent")

# q17 limit of y0 e^{kt}, k < 0
kneg = sp.Symbol('kneg', negative=True)
assert sp.limit(y0 * sp.exp(kneg * t), t, sp.oo) == 0
assert key(17).startswith("y decreases toward 0")

# q18 15 percent continuous loss
assert key(18) == "dA/dt = -0.15A"

# q19 three half-lives
assert sp.Rational(1, 2)**3 == sp.Rational(1, 8)
assert key(19) == "1/8"

# q20 Newton cooling limit is the ambient value
C = sp.Symbol('C')
T = 70 + C * sp.exp(kneg * t)
assert sp.limit(T, t, sp.oo) == 70
assert key(20).startswith("it approaches 70 rather than 0")

# q21 half-life independent of the initial amount
a0 = sp.Symbol('a0', positive=True)
hl = sp.solve(sp.Eq(a0 * sp.exp(kneg * t), a0 / 2), t)[0]
assert a0 not in hl.free_symbols
assert key(21).startswith("they are the same")

# q22 half-life for k = -0.2
h22 = sp.log(2) / sp.Rational(2, 10)
assert abs(float(h22) - 3.47) < 0.005
assert key(22) == "3.47"

# q23 half-life 6 model
A23 = 40 * sp.Rational(1, 2)**(t / 6)
assert A23.subs(t, 0) == 40 and A23.subs(t, 6) == 20 and A23.subs(t, 12) == 10
assert key(23) == "A = 40*(1/2)^(t/6)"

# q24 P(0)=1000, P(3)=8000
P24 = 1000 * 2**t
assert P24.subs(t, 0) == 1000 and P24.subs(t, 3) == 8000
assert (1000 * 2**(t / 3)).subs(t, 3) != 8000
assert key(24) == "P = 1000*2^t"

# q25 the rate is proportional, not constant
assert key(25).startswith("the quantity changes at a rate proportional to its current size")

print("verify_c7_8: all checks passed")
