"""sympy verification of every answer in c9_6.py (9.6 motion in the plane).

Run:  python3 verify_c9_6.py
"""
import sympy as sp

import c9_6
from unit9_util import Checker, t

C = Checker(c9_6)
tp = sp.Symbol("tp", positive=True)


def speed(v):
    return sp.sqrt(v[0]**2 + v[1]**2)


def dist(v, a, b):
    return sp.integrate(sp.simplify(speed(v)), (t, a, b))


# 1, 2 — the two definitions the topic turns on.
C.ck_text(1, "sqrt((dx/dt)^2 + (dy/dt)^2)", "speed is the magnitude of velocity, a scalar.")
C.ck_text(2, "int from a to b of sqrt((dx/dt)^2 + (dy/dt)^2) dt",
          "distance travelled is the integral of speed.")

# 3 — constant velocity
C.ck(3, speed([3, 4]))

# 4, 5 — speed from a position function
r = [t**2, t**3]
C.ck(4, sp.simplify(speed([sp.diff(c, t) for c in r]).subs(t, 1)))
r = [t**2, 2*t]
C.ck(5, sp.simplify(speed([sp.diff(c, t) for c in r]).subs(t, 2)))

# 6 — distance at constant speed
C.ck(6, dist([sp.Integer(3), sp.Integer(4)], 0, 2))

# 7 — distance set-up
r = [t**2, 2*t**3]
v = [sp.diff(c, t) for c in r]
assert sp.simplify(v[0]**2 + v[1]**2 - (4*t**2 + 36*t**4)) == 0
C.ck_int(7, 0, 1, sp.sqrt(4*t**2 + 36*t**4))

# 8 — acceleration
C.ck_vec(8, [sp.diff(c, t, 2) for c in [t**3, t**2]])

# 9 — moving left
r = [t**2 - 4*t, t**3]
assert sp.solve(sp.Lt(sp.diff(r[0], t), 0), t).as_set() == sp.Interval.open(-sp.oo, 2)
C.ck_text(9, "t < 2", "dx/dt = 2t - 4 is negative below t = 2.")

# 10 — at rest
v = [t**2 - 1, t - 1]
assert sp.solve(sp.Eq(v[0], 0), t) == [-1, 1] and sp.solve(sp.Eq(v[1], 0), t) == [1]
C.ck_text(10, "t = 1 only", "both components vanish only at t = 1.")

# 11 — unit speed
C.ck(11, dist([sp.cos(t), sp.sin(t)], 0, sp.pi))

# 12 — distance with a reversal
d = sp.integrate(sp.Abs(t - 3), (t, 0, 5))
disp = sp.integrate(t - 3, (t, 0, 5))
assert d == sp.Rational(13, 2) and disp == sp.Rational(-5, 2)
C.ck(12, d)

# 13 — displacement, not distance
disp = [sp.integrate(0, (t, 0, 4)), sp.integrate(2*t - 6, (t, 0, 4))]
assert sp.integrate(sp.Abs(2*t - 6), (t, 0, 4)) == 10  # the distance really is different
C.ck_vec(13, disp)

# 14 — speed on an ellipse
r = [2*sp.cos(t), 3*sp.sin(t)]
C.ck(14, sp.simplify(speed([sp.diff(c, t) for c in r]).subs(t, sp.pi/2)))

# 15 — perfect-square speed
v = [2*tp, sp.sqrt(8*tp + 4)]
sp_speed = sp.sqrt(sp.factor(v[0]**2 + v[1]**2)).simplify()
assert sp.simplify(sp_speed - 2*(tp + 1)) == 0
C.ck(15, sp.integrate(2*(tp + 1), (tp, 0, 3)))

# 16 — minimum speed
v = [2*t, t**2 - 4]
sq = sp.expand(v[0]**2 + v[1]**2)
assert sp.simplify(sq - (t**4 - 4*t**2 + 16)) == 0
crit = [s for s in sp.solve(sp.diff(sq, t), t) if s.is_real and s >= 0]
vals = [sp.sqrt(sq.subs(t, s)) for s in crit] + [sp.sqrt(sq.subs(t, 0)), sp.sqrt(sq.subs(t, 10))]
C.ck(16, sp.simplify(min(vals, key=lambda e: sp.N(e))))
assert sp.simplify(min(vals, key=lambda e: sp.N(e)) - 2*sp.sqrt(3)) == 0

# 17 — magnitude of acceleration
a = [sp.diff(c, t, 2) for c in [t**3, t**2]]
C.ck(17, sp.simplify(speed(a).subs(t, 1)))

# 18 — exponential speed
C.ck(18, dist([3*sp.exp(t), 4*sp.exp(t)], 0, sp.log(2)))

# 19 — speed is nonnegative.
assert speed([-6, 8]) == 10
C.ck_text(19, "speed at t = 2 is 10", "a magnitude cannot be negative.")

# 20 — decimal distance
r = [t**2, 2*t**3]
D = sp.integrate(sp.simplify(sp.sqrt(sp.diff(r[0], t)**2 + sp.diff(r[1], t)**2)).subs(t, tp), (tp, 0, 1))
assert abs(sp.N(D - sp.Rational(2, 27)*(10**sp.Rational(3, 2) - 1))) < 1e-12
C.ck_num(20, D)

# 21 — position from velocity
pos = [1 + sp.integrate(4*t, (t, 0, t)), 2 + sp.integrate(3, (t, 0, t))]
C.ck_vec(21, [c.subs(t, 2) for c in pos])

# 22 — decimal distance with an inverse-hyperbolic antiderivative
D = sp.integrate(2*sp.sqrt(1 + tp**2), (tp, 0, 2))
assert abs(sp.N(D) - sp.N(2*sp.sqrt(5) + sp.log(2 + sp.sqrt(5)))) < 1e-12
C.ck_num(22, D)

# 23 — up and to the left
r = [t**2 - 4*t, t**2 - 2*t]
up = sp.solve(sp.Gt(sp.diff(r[1], t), 0), t).as_set()
left = sp.solve(sp.Lt(sp.diff(r[0], t), 0), t).as_set()
assert (up & left) == sp.Interval.open(1, 2)
C.ck_text(23, "1 < t < 2", "dy/dt > 0 for t > 1 and dx/dt < 0 for t < 2.")

# 24 — speed when crossing the y-axis
r = [t**2 - 4, 3*t]
cross = [s for s in sp.solve(sp.Eq(r[0], 0), t) if s >= 0]
assert cross == [2]
C.ck(24, sp.simplify(speed([sp.diff(c, t) for c in r]).subs(t, 2)))

# 25 — constant speed does not mean zero acceleration.
r = [5*sp.cos(t), 5*sp.sin(t)]
v = [sp.diff(c, t) for c in r]
a = [sp.diff(c, t, 2) for c in r]
assert sp.simplify(speed(v)) == 5 and sp.simplify(speed(a)) == 5
C.ck_text(25, "acceleration may be a nonzero vector",
          "uniform circular motion has constant speed 5 and acceleration of magnitude 5.")

C.finish()
