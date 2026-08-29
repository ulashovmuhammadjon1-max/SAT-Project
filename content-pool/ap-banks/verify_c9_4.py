"""sympy verification of every answer in c9_4.py (9.4 vector-valued functions).

Run:  python3 verify_c9_4.py
"""
import sympy as sp

import c9_4
from unit9_util import Checker, t

C = Checker(c9_4)


def d(vec, n=1):
    return [sp.diff(c, t, n) for c in vec]


def at(vec, v):
    return [sp.simplify(c.subs(t, v)) for c in vec]


# 1 — the componentwise definition.
C.ck_text(1, "<f'(t), g'(t)>", "derivatives of vector functions are taken component by component.")

# 2, 3 — r = <t^2, t^3>
r = [t**2, t**3]
C.ck_vec(2, d(r))
C.ck_vec(3, at(d(r), 1))

# 4 — <sin t, cos t>
C.ck_vec(4, d([sp.sin(t), sp.cos(t)]))

# 5 — <e^(2t), ln t>
C.ck_vec(5, d([sp.exp(2*t), sp.log(t)]))

# 6 — second derivative
C.ck_vec(6, d([t**3, t**2], 2))

# 7 — conceptual: r' is tangent.
C.ck_text(7, "is tangent to the curve", "the difference quotient's limit lies along the curve.")

# 8 — r = <3t^2 - t, t^4>
C.ck_vec(8, at(d([3*t**2 - t, t**4]), 1))

# 9 — dy/dx from the components
r = [t**2 + 1, t**3]
slope = sp.simplify(sp.diff(r[1], t)/sp.diff(r[0], t))
C.ck(9, slope.subs(t, 2))
assert slope.subs(t, 2) == 3

# 10 — chain rule in both components
C.ck_vec(10, d([sp.cos(2*t), sp.sin(3*t)]))

# 11 — magnitude of r'(1)
v = at(d([t**2, 2*t]), 1)
C.ck(11, sp.sqrt(v[0]**2 + v[1]**2))
assert sp.simplify(sp.sqrt(v[0]**2 + v[1]**2) - 2*sp.sqrt(2)) == 0

# 12 — conceptual: magnitude is a scalar.
C.ck_text(12, "|r'(t)|", "a magnitude is a number; r'(t), r''(t) and a difference of positions are vectors.")

# 13 — unit tangent vector
v = at(d([t, t**2]), 1)
mag = sp.sqrt(v[0]**2 + v[1]**2)
C.ck_vec(13, [c/mag for c in v])

# 14 — <tan t, sec t>
C.ck_vec(14, d([sp.tan(t), sp.sec(t)]))

# 15 — zero vector
r = [t**3, t**2]
zeros = sp.solve([sp.diff(c, t) for c in r], t)
assert sp.solve(sp.Eq(sp.diff(r[0], t), 0), t) == [0]
assert sp.solve(sp.Eq(sp.diff(r[1], t), 0), t) == [0]
C.ck_text(15, "t = 0", "3t^2 and 2t vanish together only at t = 0.")

# 16 — chain rule with inner 2t
C.ck_vec(16, d([sp.sin(t**2), sp.cos(t**2)]))

# 17 — log and arctangent
C.ck_vec(17, [sp.simplify(c) for c in d([sp.log(t**2 + 1), sp.atan(t)])])

# 18, 19 — horizontal and vertical tangent vectors
r = [t**2, t**3 - 3*t]
horiz = [s for s in sp.solve(sp.diff(r[1], t), t) if sp.diff(r[0], t).subs(t, s) != 0]
vert = [s for s in sp.solve(sp.diff(r[0], t), t) if sp.diff(r[1], t).subs(t, s) != 0]
assert sorted(horiz) == [-1, 1] and vert == [0], (horiz, vert)
C.ck_text(18, "t = 1 and t = -1", "the y-component of r' vanishes at t = +/-1 with 2t nonzero.")
C.ck_text(19, "t = 0", "the x-component 2t vanishes at t = 0, where the y-component is -3.")

# 20 — r' parallel to <1, 1>
r = [t**2, t**3]
sols = [s for s in sp.solve(sp.Eq(sp.diff(r[1], t), sp.diff(r[0], t)), t) if s > 0]
assert sols == [sp.Rational(2, 3)], sols
C.ck(20, sp.Rational(2, 3))

# 21 — second derivative of <t^4, e^t>
C.ck_vec(21, d([t**4, sp.exp(t)], 2))

# 22 — product rule in both components
C.ck_vec(22, [sp.simplify(c) for c in d([t*sp.exp(t), t**2*sp.exp(t)])])

# 23 — slope 6
r = [t**2, t**3]
slope = sp.simplify(sp.diff(r[1], t)/sp.diff(r[0], t))
assert sp.solve(sp.Eq(slope, 6), t) == [4]
C.ck(23, 4)

# 24 — the limit definition.
h = sp.Symbol("h")
r = [t**2, sp.sin(t)]
for comp in r:  # the componentwise difference quotient reproduces the derivative
    assert sp.simplify(sp.limit((comp.subs(t, t + h) - comp)/h, h, 0) - sp.diff(comp, t)) == 0
# taking the magnitude first gives a different object (a number, and here a different one)
mag_quot = sp.limit(sp.sqrt(((t + h)**2 - t**2)**2 + (sp.sin(t + h) - sp.sin(t))**2)/h, h, 0)
assert sp.simplify(mag_quot - 2*t) != 0
C.ck_text(24, "(r(t + h) - r(t))/h", "the vector difference quotient, not its magnitude.")

# 25 — r'(4) for <sqrt(t), 1/t>
C.ck_vec(25, at(d([sp.sqrt(t), 1/t]), 4))

C.finish()
