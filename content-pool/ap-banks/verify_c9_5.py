"""sympy verification of every answer in c9_5.py (9.5 integrating vector functions).

Run:  python3 verify_c9_5.py
"""
import sympy as sp

import c9_5
from c9_util import Checker, t

C = Checker(c9_5)


def anti(vec):
    return [sp.integrate(c, t) for c in vec]


def defint(vec, a, b):
    return [sp.simplify(sp.integrate(c, (t, a, b))) for c in vec]


def at(vec, v):
    return [sp.simplify(sp.sympify(c).subs(t, v)) for c in vec]


# 1, 6 — conceptual.
C.ck_text(1, "<int f(t) dt, int g(t) dt>", "antidifferentiation is componentwise.")
C.ck_text(6, "is a vector", "each component contributes its own arbitrary constant.")

# 2, 3 — <2t, 3t^2>
v = [2*t, 3*t**2]
C.ck_vec(2, anti(v))
C.ck_vec(3, defint(v, 0, 1))

# 4, 5 — <cos t, sin t>
v = [sp.cos(t), sp.sin(t)]
C.ck_vec(4, anti(v))
C.ck_vec(5, defint(v, 0, sp.pi/2))

# 7 — <e^t, 1/t>
tp = sp.Symbol("tp", positive=True)
C.ck_vec(7, [sp.exp(t), sp.integrate(1/tp, tp).subs(tp, t)])
assert sp.integrate(1/tp, tp) == sp.log(tp)

# 8 — <sec^2 t, 2t>
C.ck_vec(8, anti([sp.sec(t)**2, 2*t]))

# 9, 10 — definite integrals
C.ck_vec(9, defint([3*t**2, 4*t**3], 0, 2))
C.ck_vec(10, defint([1/t, 1/t**2], 1, 2))

# 11 — antiderivative fixed by r(1) = <2, 5>
v = [3*t**2, 2*t]
pos = [sp.integrate(c, (t, 1, t)) for c in v]
pos = [pos[0] + 2, pos[1] + 5]
assert at(pos, 1) == [2, 5]
C.ck_vec(11, [sp.expand(c) for c in pos])

# 12 — r(0) = <1, -3>, v = <2, 6t>
v = [sp.Integer(2), 6*t]
pos = [sp.integrate(v[0], (t, 0, t)) + 1, sp.integrate(v[1], (t, 0, t)) - 3]
C.ck_vec(12, at(pos, 2))

# 13 — displacement
C.ck_vec(13, defint([t, t**2], 0, 3))

# 14 — displacement vs distance: the two really do differ on an example.
v = [sp.cos(t), sp.sin(t)]
disp = defint(v, 0, 2*sp.pi)
dist = sp.integrate(sp.sqrt(v[0]**2 + v[1]**2), (t, 0, 2*sp.pi))
assert disp == [0, 0] and dist == 2*sp.pi
C.ck_text(14, "displacement vector", "integrating v gives net change in position, not path length.")

# 15, 16, 17 — projectile
acc = [sp.Integer(0), sp.Integer(-32)]
vel = [sp.integrate(acc[0], (t, 0, t)) + 10, sp.integrate(acc[1], (t, 0, t)) + 20]
C.ck_vec(15, vel)
pos = [sp.integrate(vel[0], (t, 0, t)) + 0, sp.expand(sp.integrate(vel[1], (t, 0, t)) + 5)]
C.ck_vec(16, pos)
# 17 — a second projectile, different initial data
vel2 = [sp.integrate(acc[0], (t, 0, t)) + 30, sp.integrate(acc[1], (t, 0, t)) + 40]
pos2 = [sp.integrate(vel2[0], (t, 0, t)) + 0, sp.expand(sp.integrate(vel2[1], (t, 0, t)) + 6)]
C.ck_vec(17, at(pos2, 2))

# 18 — v = <cos t, sin t>, r(0) = <0, 1>
vel = [sp.cos(t), sp.sin(t)]
pos = [sp.integrate(vel[0], (t, 0, t)) + 0, sp.integrate(vel[1], (t, 0, t)) + 1]
assert [sp.simplify(c) for c in pos] == [sp.sin(t), 2 - sp.cos(t)]
C.ck_vec(18, at(pos, sp.pi/2))

# 19 — a = <6t, 12t^2>, v(0) = <1, 2>
acc = [6*t, 12*t**2]
C.ck_vec(19, [sp.integrate(acc[0], (t, 0, t)) + 1, sp.integrate(acc[1], (t, 0, t)) + 2])

# 20 — <sin t, t> on [0, pi]
C.ck_vec(20, defint([sp.sin(t), t], 0, sp.pi))

# 21 — scalar displacement
C.ck(21, sp.integrate(4*t - 8, (t, 0, 3)))
assert sp.integrate(4*t - 8, (t, 0, 3)) == -6

# 22 — solve for the constants from r(2) = <10, 3>
c1, c2 = sp.symbols("c1 c2")
pos = [sp.integrate(4*t, t) + c1, sp.integrate(3*t**2, t) + c2]
sol = sp.solve([sp.Eq(pos[0].subs(t, 2), 10), sp.Eq(pos[1].subs(t, 2), 3)], [c1, c2])
pos = [p.subs(sol) for p in pos]
C.ck_vec(22, at(pos, 0))

# 23 — arctan and exponential antiderivatives
C.ck_vec(23, anti([1/(1 + t**2), sp.exp(2*t)]))

# 24 — odd component integrates to 0
C.ck_vec(24, defint([3*t**2, t], -1, 1))

# 25 — displacement from t = 1 to t = 3
C.ck_vec(25, defint([2*t, sp.Integer(4)], 1, 3))

C.finish()
