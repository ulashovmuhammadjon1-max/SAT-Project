"""sympy verification of every answer in c9_3.py (9.3 parametric arc length).

Run:  python3 verify_c9_3.py
"""
import sympy as sp

import c9_3
from c9_util import Checker, t

C = Checker(c9_3)


def speed(X, Y):
    return sp.simplify(sp.sqrt(sp.diff(X, t)**2 + sp.diff(Y, t)**2))


def length(X, Y, a, b):
    return sp.simplify(sp.integrate(speed(X, Y), (t, a, b)))


# 1 — the formula itself.
C.ck_text(1, "sqrt((dx/dt)^2 + (dy/dt)^2)", "(ds)^2 = (dx)^2 + (dy)^2.")

# 2, 3 — x = t^2, y = t^3 on [0, 2]
X, Y = t**2, t**3
assert sp.simplify(sp.diff(X, t)**2 + sp.diff(Y, t)**2 - (4*t**2 + 9*t**4)) == 0
C.ck_int(2, 0, 2, sp.sqrt(4*t**2 + 9*t**4))
L = length(X, Y, 0, 2)
assert sp.simplify(L - (40**sp.Rational(3, 2) - 8)/27) == 0
C.ck_num(3, L)

# 4 — straight line x = 3t, y = 4t
assert speed(3*t, 4*t) == 5
C.ck(4, length(3*t, 4*t, 0, 2))

# 5, 6 — circles
C.ck(5, length(sp.cos(t), sp.sin(t), 0, sp.pi/2))
C.ck(6, length(3*sp.cos(t), 3*sp.sin(t), 0, 2*sp.pi))

# 7, 8 — x = t, y = t^2 on [0, 1]
X, Y = t, t**2
C.ck_int(7, 0, 1, sp.sqrt(1 + 4*t**2))
L = length(X, Y, 0, 1)
assert abs(sp.N(L) - sp.N(sp.sqrt(5)/2 + sp.log(2 + sp.sqrt(5))/4)) < 1e-12
C.ck_num(8, L)

# 9 — integrand that is a perfect square
tp = sp.Symbol("tp", positive=True)
Xp, Yp = tp**2/2, (2*tp + 1)**sp.Rational(3, 2)/3
sp_speed = sp.sqrt(sp.factor(sp.diff(Xp, tp)**2 + sp.diff(Yp, tp)**2)).simplify()
assert sp.simplify(sp_speed - (tp + 1)) == 0  # the radicand is the square (t + 1)^2
C.ck(9, sp.integrate(tp + 1, (tp, 0, 4)))

# 10, 11 — one arch of the cycloid
X, Y = t - sp.sin(t), 1 - sp.cos(t)
assert sp.simplify(sp.diff(X, t)**2 + sp.diff(Y, t)**2 - (2 - 2*sp.cos(t))) == 0
C.ck_int(10, 0, 2*sp.pi, sp.sqrt(2 - 2*sp.cos(t)))
L = sp.integrate(2*sp.sin(t/2), (t, 0, 2*sp.pi))  # sqrt(2-2cos t) = 2|sin(t/2)| >= 0 here
assert L == 8
C.ck(11, L)

# 12, 13 — conceptual.
C.ck_text(12, "squared before they are added", "the radical acts on the sum of squares.")
C.ck_text(13, "integral from a to b of the particle's speed",
          "speed is exactly sqrt((dx/dt)^2 + (dy/dt)^2).")

# 14, 15 — logarithmic spiral
X, Y = sp.exp(t)*sp.cos(t), sp.exp(t)*sp.sin(t)
assert sp.simplify(speed(X, Y) - sp.sqrt(2)*sp.exp(t)) == 0
C.ck_int(14, 0, 1, sp.sqrt(2)*sp.exp(t))
L = length(X, Y, 0, 1)
assert sp.simplify(L - sp.sqrt(2)*(sp.E - 1)) == 0
C.ck_num(15, L)

# 16, 17 — x = t^3, y = t^2 on [0, 1]
X, Y = t**3, t**2
assert sp.simplify(sp.diff(X, t)**2 + sp.diff(Y, t)**2 - (9*t**4 + 4*t**2)) == 0
C.ck_int(16, 0, 1, sp.sqrt(9*t**4 + 4*t**2))
L = length(X, Y, 0, 1)
assert sp.simplify(L - (13**sp.Rational(3, 2) - 8)/27) == 0
C.ck_num(17, L)

# 18 — the circle traced twice
C.ck(18, length(sp.cos(t), sp.sin(t), 0, 4*sp.pi))

# 19 — solve 5b = 20
b = sp.Symbol("b", positive=True)
assert sp.solve(sp.Eq(sp.integrate(speed(3*t, 4*t), (t, 0, b)), 20), b) == [4]
C.ck(19, 4)

# 20 — same arc, two parametrizations
L1 = length(2*t, 4*t**2, 0, 1)
L2 = length(t, t**2, 0, 2)
assert sp.simplify(L1 - L2) == 0
C.ck_text(20, "same length", "both trace y = x^2 from x = 0 to x = 2 exactly once.")

# 21 — x = sin 2t, y = cos 2t
assert speed(sp.sin(2*t), sp.cos(2*t)) == 2
C.ck(21, length(sp.sin(2*t), sp.cos(2*t), 0, sp.pi/2))

# 22 — x = t^3/3, y = t^2 on [1, 2]
X, Y = t**3/3, t**2
L = length(X, Y, 1, 2)
assert sp.simplify(L - (8**sp.Rational(3, 2) - 5**sp.Rational(3, 2))/3) == 0
C.ck_num(22, L)

# 23 — involute of a circle
X, Y = sp.cos(t) + t*sp.sin(t), sp.sin(t) - t*sp.cos(t)
assert sp.simplify(sp.diff(X, t) - t*sp.cos(t)) == 0
assert sp.simplify(sp.diff(Y, t) - t*sp.sin(t)) == 0
C.ck(23, sp.integrate(t, (t, 0, sp.pi)))  # speed = |t| = t on [0, pi]

# 24 — arc of a circle of radius 5
C.ck(24, length(5*sp.cos(t), 5*sp.sin(t), 0, sp.pi/3))

# 25 — another straight line
C.ck(25, length(4*t + 1, 3*t - 2, 0, 5))

C.finish()
