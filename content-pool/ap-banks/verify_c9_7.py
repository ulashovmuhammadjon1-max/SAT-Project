"""sympy verification of every answer in c9_7.py (9.7 polar coordinates and slopes).

Run:  python3 verify_c9_7.py
"""
import sympy as sp

import c9_7
from c9_util import Checker, th

C = Checker(c9_7)


def xy(r):
    """Rectangular coordinate functions of a polar curve r(theta)."""
    return r*sp.cos(th), r*sp.sin(th)


def slope(r):
    X, Y = xy(r)
    return sp.simplify(sp.diff(Y, th)/sp.diff(X, th))


def slope_at(r, v):
    X, Y = xy(r)
    return sp.simplify(sp.diff(Y, th).subs(th, v)/sp.diff(X, th).subs(th, v))


# 1, 2 — conversions
C.ck_pt(1, [2*sp.cos(sp.pi/3), 2*sp.sin(sp.pi/3)])
C.ck_pt(2, [sp.sqrt(1**2 + 1**2), sp.atan2(1, 1)])

# 3 — r = 3 is a circle
X, Y = xy(sp.Integer(3))
assert sp.simplify(X**2 + Y**2 - 9) == 0
C.ck_text(3, "circle of radius 3 centered at the origin", "x^2 + y^2 = 9.")

# 4 — theta = pi/4 is the line y = x
rr = sp.Symbol("rr", real=True)
assert sp.simplify(rr*sp.sin(sp.pi/4) - rr*sp.cos(sp.pi/4)) == 0
C.ck_text(4, "line through the origin with slope 1", "y = x for every r, positive or negative.")

# 5, 6, 15 — the slope formula and the two ways it is misremembered
f = sp.Function("f")
X, Y = f(th)*sp.cos(th), f(th)*sp.sin(th)
formula = (sp.diff(f(th), th)*sp.sin(th) + f(th)*sp.cos(th)) \
    / (sp.diff(f(th), th)*sp.cos(th) - f(th)*sp.sin(th))
assert sp.simplify(sp.diff(Y, th)/sp.diff(X, th) - formula) == 0
assert sp.simplify(sp.diff(X, th) - (sp.diff(f(th), th)*sp.cos(th) - f(th)*sp.sin(th))) == 0
C.ck_text(5, "((dr/dtheta)sin(theta) + r cos(theta))/((dr/dtheta)cos(theta) - r sin(theta))",
          "product rule on x = r cos and y = r sin, then divide.")
assert sp.simplify(slope(th) - sp.diff(th, th)) != 0  # for r = theta, dy/dx is not dr/dtheta
C.ck_text(6, "dr/dtheta measures how the distance from the origin changes",
          "for r = theta, dr/dtheta = 1 but the slope is not 1.")
C.ck_text(15, "(dr/dtheta)cos(theta) - r sin(theta)", "product rule on x = r cos(theta).")

# 7 — circle r = 2
C.ck(7, slope_at(sp.Integer(2), sp.pi/4))

# 8, 9 — the spiral r = theta
C.ck(8, slope(th))
C.ck(9, slope_at(th, sp.pi/2))
assert sp.simplify(slope_at(th, sp.pi/2) + 2/sp.pi) == 0

# 10 — cardioid at theta = pi/2
r = 1 + sp.cos(th)
X, Y = xy(r)
assert sp.diff(X, th).subs(th, sp.pi/2) == -1 and sp.diff(Y, th).subs(th, sp.pi/2) == -1
C.ck(10, slope_at(r, sp.pi/2))

# 11 — r = 2 sin theta at the top of the circle
r = 2*sp.sin(th)
X, Y = xy(r)
assert sp.simplify(sp.diff(Y, th).subs(th, sp.pi/2)) == 0
assert sp.simplify(sp.diff(X, th).subs(th, sp.pi/2)) != 0
C.ck_text(11, "horizontal, because dy/dtheta = 0", "the top point of x^2 + (y-1)^2 = 1.")

# 12 — r = 4 cos theta in rectangular form
r = 4*sp.cos(th)
X, Y = xy(r)
assert sp.simplify(X**2 + Y**2 - 4*X) == 0
C.ck_text(12, "x^2 + y^2 = 4x", "multiply r = 4cos(theta) by r.")

# 13 — r = 2 sec theta
X, Y = xy(2*sp.sec(th))
assert sp.simplify(X - 2) == 0
C.ck_text(13, "vertical line x = 2", "r cos(theta) = 2 is x = 2.")

# 14 — negative r
a = (-2*sp.cos(sp.pi/3), -2*sp.sin(sp.pi/3))
b = (2*sp.cos(4*sp.pi/3), 2*sp.sin(4*sp.pi/3))
assert [sp.simplify(u - v) for u, v in zip(a, b)] == [0, 0]
C.ck_pt(14, [2, 4*sp.pi/3])

# 16 — rectangular to polar in the second quadrant
C.ck_pt(16, [sp.sqrt(9 + 9), sp.atan2(3, -3)])

# 17 — the logarithmic spiral at theta = 0
C.ck(17, slope_at(sp.exp(th), 0))

# 18 — horizontal tangent condition
C.ck_text(18, "dy/dtheta = 0 and dx/dtheta is not 0",
          "the slope (dy/dtheta)/(dx/dtheta) is zero exactly then.")

# 19 — horizontal tangent on the cardioid in (0, pi)
r = 1 + sp.cos(th)
X, Y = xy(r)
sols = [s for s in sp.solve(sp.diff(Y, th), th)
        if s.is_real and 0 < s < sp.pi and sp.simplify(sp.diff(X, th).subs(th, s)) != 0]
assert sols == [sp.pi/3], sols
C.ck(19, sp.pi/3)

# 20 — the rose r = sin(2theta) at theta = pi/4
C.ck(20, slope_at(sp.sin(2*th), sp.pi/4))

# 21 — distance from the origin
C.ck_text(21, "|r|", "a negative r still lies |r| from the origin.")

# 22 — dy/dtheta for r = 3 + 2 sin theta
X, Y = xy(3 + 2*sp.sin(th))
C.ck(22, sp.simplify(sp.diff(Y, th).subs(th, 0)))

# 23 — the defining relations
C.ck_text(23, "x = r cos(theta) and y = r sin(theta)", "the definition of polar coordinates.")

# 24 — the cusp of the cardioid at theta = pi
r = 1 + sp.cos(th)
X, Y = xy(r)
assert sp.simplify(sp.diff(X, th).subs(th, sp.pi)) == 0
assert sp.simplify(sp.diff(Y, th).subs(th, sp.pi)) == 0
C.ck_text(24, "0/0", "both coordinate derivatives vanish at theta = pi.")

# 25 — tangent at the pole for r = sin(3theta)
r = sp.sin(3*th)
assert sp.simplify(r.subs(th, sp.pi/3)) == 0
C.ck(25, sp.simplify(slope_at(r, sp.pi/3)))
assert sp.simplify(slope_at(r, sp.pi/3) - sp.tan(sp.pi/3)) == 0

C.finish()
