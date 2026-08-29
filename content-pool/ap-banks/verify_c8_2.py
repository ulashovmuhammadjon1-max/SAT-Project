# Verification for CALC 8.2. Run: python3 verify_c8_2.py
# displacement = int v dt; total distance = int |v| dt, computed by splitting
# at the zeros of v so sympy never has to integrate an Abs symbolically.
import sympy as sp
from c8_2 import QUESTIONS as Q

t = sp.Symbol('t', real=True)


def key(i):
    return Q[i - 1]["choices"][Q[i - 1]["ans"]]


def displacement(v, a, b):
    return sp.simplify(sp.integrate(v, (t, a, b)))


def distance(v, a, b):
    cuts = [r for r in sp.solve(v, t) if r.is_real and a < r < b]
    pts = [a] + sorted(cuts) + [b]
    total = 0
    for lo, hi in zip(pts, pts[1:]):
        total += sp.Abs(sp.integrate(v, (t, lo, hi)))
    return sp.simplify(total)


def num(i):
    return sp.nsimplify(key(i))


assert len(Q) == 25
for i, item in enumerate(Q, 1):
    assert len(item["choices"]) == 4 and len(set(item["choices"])) == 4, i
    assert 0 <= item["ans"] < 4, i

assert key(1) == "int from a to b of v(t) dt"
assert key(2) == "int from a to b of |v(t)| dt"

v1 = t - 3
assert displacement(v1, 0, 5) == sp.Rational(-5, 2) and num(3) == sp.Rational(-5, 2)
assert distance(v1, 0, 5) == sp.Rational(13, 2) and num(4) == sp.Rational(13, 2)

v2 = t**2 - 4
assert displacement(v2, 0, 3) == -3 and num(5) == -3
assert distance(v2, 0, 3) == sp.Rational(23, 3) and num(6) == sp.Rational(23, 3)

v3 = sp.sin(t)
assert displacement(v3, 0, 2 * sp.pi) == 0 and num(7) == 0
assert distance(v3, 0, 2 * sp.pi) == 4 and num(8) == 4

v4 = 4 - 2 * t
assert displacement(v4, 0, 4) == 0 and num(9) == 0
assert distance(v4, 0, 4) == 8 and num(10) == 8

v5 = t**2 - 5 * t + 6
assert displacement(v5, 0, 4) == sp.Rational(16, 3) and num(11) == sp.Rational(16, 3)
assert distance(v5, 0, 4) == sp.Rational(17, 3) and num(12) == sp.Rational(17, 3)
# the three pieces named in the rationale
assert sp.Abs(sp.integrate(v5, (t, 0, 2))) == sp.Rational(14, 3)
assert sp.Abs(sp.integrate(v5, (t, 2, 3))) == sp.Rational(1, 6)
assert sp.Abs(sp.integrate(v5, (t, 3, 4))) == sp.Rational(5, 6)

assert key(13) == "when the velocity does not change sign on the interval"
# and a witness: v = e^t - 1 never changes sign on [0, 2]
v6 = sp.exp(t) - 1
assert distance(v6, 0, 2) == displacement(v6, 0, 2)

s14 = 2 + sp.integrate(3 * t**2, (t, 0, 2))
assert s14 == 10 and num(14) == 10

v15 = 1 + sp.integrate(6 * t, (t, 0, t))
assert sp.simplify(v15 - (3 * t**2 + 1)) == 0
assert key(15) == "v(t) = 3t^2 + 1"

assert key(16) == "the change in velocity from time a to time b"
assert key(17) == "|v(t)|"
assert key(18) == "v(t) < 0"
assert key(19) == "v(t) and a(t) have the same sign"

v20 = 64 + sp.integrate(-32, (t, 0, t))
assert sp.solve(v20, t) == [2] and key(20) == "t = 2 seconds"

assert key(21) == "s(b) - s(a) = int from a to b of v(t) dt"

assert sp.simplify(distance(v6, 0, 2) - (sp.exp(2) - 3)) == 0
assert key(22) == "e^2 - 3"

s23 = 4 + sp.integrate(2 * t - 6, (t, 0, 5))
assert s23 == -1 and num(23) == -1

# q24 average velocity vs average speed
avg_v = displacement(v1, 0, 5) / 5
avg_s = distance(v1, 0, 5) / 5
assert avg_v == sp.Rational(-1, 2) and avg_s == sp.Rational(13, 10)
assert key(24) == "average velocity -0.5 and average speed 1.3"

# q25 the error: |int v| = 2.5, but the real distance is 6.5
assert sp.Abs(displacement(v1, 0, 5)) == sp.Rational(5, 2) != distance(v1, 0, 5)
assert key(25).startswith("the absolute value must be applied to v(t) inside the integral")

print("verify_c8_2: all checks passed")
