"""sympy verification of every answer in c9_1.py (9.1 parametric derivatives).

Run:  python3 verify_c9_1.py
"""
import sympy as sp

import c9_1
from c9_util import Checker, t

C = Checker(c9_1)


def dydx(xt, yt):
    return sp.simplify(sp.diff(yt, t) / sp.diff(xt, t))


# 1 — conceptual: the parametric chain rule.
C.ck_text(1, "(dy/dt)/(dx/dt)",
          "dy/dt = (dy/dx)(dx/dt) by the chain rule.")

# 2, 3 — x = t^2 + 1, y = t^3 - t
X, Y = t**2 + 1, t**3 - t
C.ck(2, dydx(X, Y))
C.ck(3, dydx(X, Y).subs(t, 2))
assert dydx(X, Y).subs(t, 2) == sp.Rational(11, 4)

# 4, 5 — conceptual: horizontal vs vertical tangent conditions.
C.ck_text(4, "g'(c) = 0 and f'(c) is not 0",
          "dy/dx = g'/f' is zero exactly when the numerator vanishes and the denominator does not.")
C.ck_text(5, "f'(c) = 0 and g'(c) is not 0",
          "dy/dx is undefined (vertical tangent) when f' = 0 while g' is nonzero.")

# 6, 7 — x = t^3 - 3t, y = t^2 - 4
X, Y = t**3 - 3*t, t**2 - 4
horiz = [s for s in sp.solve(sp.diff(Y, t), t) if sp.diff(X, t).subs(t, s) != 0]
vert = [s for s in sp.solve(sp.diff(X, t), t) if sp.diff(Y, t).subs(t, s) != 0]
assert horiz == [0], horiz
assert sorted(vert) == [-1, 1], vert
C.ck_text(6, "t = 0 only", "dy/dt = 2t vanishes only at t = 0, where dx/dt = -3.")
C.ck_text(7, "t = 1 and t = -1", "dx/dt = 3t^2 - 3 vanishes at t = 1, -1, where dy/dt = 2t is nonzero.")

# 8, 9 — unit circle
X, Y = sp.cos(t), sp.sin(t)
C.ck(8, dydx(X, Y))
C.ck(9, sp.simplify(dydx(X, Y).subs(t, sp.pi/6)))
assert sp.simplify(dydx(X, Y).subs(t, sp.pi/6) + sp.sqrt(3)) == 0

# 10, 11 — ellipse x = 3cos t, y = 2sin t
X, Y = 3*sp.cos(t), 2*sp.sin(t)
C.ck(10, dydx(X, Y))
assert sp.diff(Y, t).subs(t, sp.pi/2) == 0 and sp.diff(X, t).subs(t, sp.pi/2) == -3
assert (X.subs(t, sp.pi/2), Y.subs(t, sp.pi/2)) == (0, 2)
C.ck_text(11, "(0, 2)", "dy/dt = 2cos t vanishes at t = pi/2, which is the point (0, 2).")

# 12 — exponential parametrization
X, Y = sp.exp(2*t), sp.exp(3*t)
C.ck(12, dydx(X, Y))
assert sp.simplify(dydx(X, Y) - sp.Rational(3, 2)*sp.exp(t)) == 0

# 13 — tangent line to x = t^2, y = t^3 - 3t at t = 2
X, Y = t**2, t**3 - 3*t
assert (X.subs(t, 2), Y.subs(t, 2)) == (4, 2)
assert dydx(X, Y).subs(t, 2) == sp.Rational(9, 4)
C.ck_text(13, "y - 2 = (9/4)(x - 4)", "slope 9/4 at the point (4, 2).")

# 14 — dy/dx as a function of x
X, Y = 2*t + 1, t**2 - t
x = sp.Symbol("x", real=True)
tof = sp.solve(sp.Eq(X, x), t)[0]
C.ck(14, sp.simplify(dydx(X, Y).subs(t, tof)))

# 15 — slope from given rates
C.ck(15, sp.Rational(-6, 4))

# 16, 17 — cycloid
X, Y = t - sp.sin(t), 1 - sp.cos(t)
C.ck(16, dydx(X, Y))
C.ck(17, sp.simplify(dydx(X, Y).subs(t, sp.pi/2)))
assert sp.simplify(dydx(X, Y).subs(t, sp.pi/2)) == 1

# 18 — conceptual: both derivatives zero.
X, Y = t**3, t**2
assert sp.diff(X, t).subs(t, 0) == 0 and sp.diff(Y, t).subs(t, 0) == 0
C.ck_text(18, "0/0",
          "x = t^3, y = t^2 has both derivatives zero at t = 0 and a cusp there, so 0/0 settles nothing.")

# 19 — x = ln t, y = t^2
X, Y = sp.log(t), t**2
C.ck(19, sp.simplify(dydx(X, Y)))

# 20, 21 — x = t^2 - 2t, y = t^3 - 12t
X, Y = t**2 - 2*t, t**3 - 12*t
horiz = [s for s in sp.solve(sp.diff(Y, t), t) if sp.diff(X, t).subs(t, s) != 0]
vert = [s for s in sp.solve(sp.diff(X, t), t) if sp.diff(Y, t).subs(t, s) != 0]
assert sorted(horiz) == [-2, 2] and vert == [1], (horiz, vert)
C.ck_text(20, "t = 2 and t = -2", "dy/dt = 3t^2 - 12 vanishes at t = +/-2 with dx/dt nonzero.")
C.ck_text(21, "t = 1", "dx/dt = 2t - 2 vanishes at t = 1, where dy/dt = -9.")

# 22 — horizontal tangent points of x = t^2, y = t^3 - 3t
X, Y = t**2, t**3 - 3*t
pts = sorted((X.subs(t, s), Y.subs(t, s)) for s in sp.solve(sp.diff(Y, t), t)
             if sp.diff(X, t).subs(t, s) != 0)
assert pts == [(1, -2), (1, 2)], pts
C.ck_text(22, "(1, -2) and (1, 2)", "t = 1 and t = -1 give these two points.")

# 23 — slope at the point (2, 0) on x = t^2 + t, y = t^3 - t
X, Y = t**2 + t, t**3 - t
ts = [s for s in sp.solve(sp.Eq(X, 2), t) if Y.subs(t, s) == 0]
assert ts == [1], ts
C.ck(23, dydx(X, Y).subs(t, 1))
assert dydx(X, Y).subs(t, 1) == sp.Rational(2, 3)

# 24 — x = t^3, y = t^2
X, Y = t**3, t**2
C.ck(24, sp.simplify(dydx(X, Y)))

# 25 — tangent parallel to y = 3x
X, Y = t**2 - 4*t, t**2 + 2*t
sols = [s for s in sp.solve(sp.Eq(dydx(X, Y), 3), t) if sp.diff(X, t).subs(t, s) != 0]
assert sols == [sp.Rational(7, 2)], sols
C.ck(25, sp.Rational(7, 2))

C.finish()
