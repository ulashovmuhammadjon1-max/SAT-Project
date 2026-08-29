"""sympy verification of every answer in c9_9.py (9.9 area between two polar curves).

Run:  python3 verify_c9_9.py
"""
import sympy as sp

import c9_9
from unit9_util import Checker, th

C = Checker(c9_9)


def between(R, r, a, b):
    """(1/2) int (R^2 - r^2) dtheta -- the difference of the SQUARES."""
    return sp.simplify(sp.Rational(1, 2)*sp.integrate(R**2 - r**2, (th, a, b)))


def sector(r, a, b):
    return sp.simplify(sp.Rational(1, 2)*sp.integrate(r**2, (th, a, b)))


def meet(f, g):
    """Intersection angles (mod 2pi, pole excluded) of two polar curves."""
    sols = [s for s in sp.solve(sp.Eq(f, g), th)
            if s.is_real and sp.simplify(f.subs(th, s)) != 0]
    return {sp.simplify(sp.Mod(s, 2*sp.pi)) for s in sols}


def angles(*vals):
    return {sp.simplify(sp.Mod(v, 2*sp.pi)) for v in vals}


# 1, 2 — the formula and the square-of-the-difference error.
C.ck_text(1, "(1/2) int from a to b of (R^2 - r^2) dtheta", "sectors subtract as (1/2)R^2 - (1/2)r^2.")
wrong = sp.Rational(1, 2)*sp.integrate((3 - 1)**2, (th, 0, 2*sp.pi))
right = between(sp.Integer(3), sp.Integer(1), 0, 2*sp.pi)
assert wrong == 4*sp.pi and right == 8*sp.pi
C.ck_text(2, "the difference of the squares is needed", "8pi, not 4pi.")

# 3, 4, 5 — intersection angles
assert meet(sp.Integer(2), 4*sp.cos(th)) == angles(sp.pi/3, -sp.pi/3)
C.ck_text(3, "theta = pi/3 and theta = -pi/3", "cos(theta) = 1/2.")
assert meet(1 + sp.cos(th), sp.Integer(1)) == angles(sp.pi/2, 3*sp.pi/2)
C.ck_text(4, "theta = pi/2 and theta = 3pi/2", "cos(theta) = 0.")
assert meet(sp.sin(th), sp.cos(th)) == angles(sp.pi/4)
C.ck_text(5, "theta = pi/4", "tan(theta) = 1.")

# 6 — an annulus
C.ck(6, between(sp.Integer(3), sp.Integer(1), 0, 2*sp.pi))

# 7, 8 — inside r = 4cos(theta), outside r = 2
R, r = 4*sp.cos(th), sp.Integer(2)
C.ck_int(7, -sp.pi/3, sp.pi/3, R**2 - r**2, coeff=sp.Rational(1, 2))
A = between(R, r, -sp.pi/3, sp.pi/3)
assert sp.simplify(A - (4*sp.pi/3 + 2*sp.sqrt(3))) == 0
C.ck(8, A)

# 9, 10 — inside the cardioid, outside the unit circle
R, r = 1 + sp.cos(th), sp.Integer(1)
C.ck_int(9, -sp.pi/2, sp.pi/2, R**2 - r**2, coeff=sp.Rational(1, 2))
A = between(R, r, -sp.pi/2, sp.pi/2)
assert sp.simplify(A - (2 + sp.pi/4)) == 0
C.ck(10, A)

# 11 — inside the limacon, outside r = 2
C.ck(11, between(2 + sp.cos(th), sp.Integer(2), -sp.pi/2, sp.pi/2))

# 12, 13 — inside both r = 1 and r = 2cos(theta)
inner = 2*(sector(sp.Integer(1), 0, sp.pi/3) + sector(2*sp.cos(th), sp.pi/3, sp.pi/2))
assert sp.simplify(inner - (2*sp.pi/3 - sp.sqrt(3)/2)) == 0
C.ck(12, inner)
C.ck_text(13, "2 times [(1/2) int from 0 to pi/3 of 1 dtheta", "the bounding curve switches at pi/3.")
# the three rejected set-ups really do give something else
assert sp.simplify(between(2*sp.cos(th), sp.Integer(1), 0, sp.pi/2) - inner) != 0
assert sp.simplify(between(2*sp.cos(th), sp.Integer(1), 0, sp.pi/3) - inner) != 0
assert sp.simplify(2*sector(sp.Integer(1), 0, sp.pi/2) - inner) != 0

# 14, 15 — conceptual
C.ck_text(14, "find the values of theta at which the curves intersect", "they set the limits.")
# the pole: r = sin(theta) reaches it at theta = 0 and r = cos(theta) at theta = pi/2,
# yet sin = cos at neither, so solving f = g misses the shared point.
assert sp.sin(th).subs(th, 0) == 0 and sp.cos(th).subs(th, sp.pi/2) == 0
assert sp.simplify(sp.sin(th).subs(th, 0) - sp.cos(th).subs(th, 0)) != 0
C.ck_text(15, "both curves may pass through the pole at different values of theta",
          "sin and cos each reach the pole, at theta = 0 and pi/2 respectively.")

# 16, 17 — inside r = 2sin(theta), outside r = 1
R, r = 2*sp.sin(th), sp.Integer(1)
assert meet(R, r) == angles(sp.pi/6, 5*sp.pi/6)
A = between(R, r, sp.pi/6, 5*sp.pi/6)
assert sp.simplify(A - (sp.pi/3 + sp.sqrt(3)/2)) == 0
C.ck(16, A)
C.ck_int(17, sp.pi/6, 5*sp.pi/6, R**2 - r**2, coeff=sp.Rational(1, 2))

# 18 — decimal, inside r = 1 + sin(theta) and outside r = 1
A = between(1 + sp.sin(th), sp.Integer(1), 0, sp.pi)
assert sp.simplify(A - (2 + sp.pi/4)) == 0
C.ck_num(18, A)

# 19 — inside both r = 3sin(theta) and r = 3cos(theta)
A = 2*sector(3*sp.sin(th), 0, sp.pi/4)
assert sp.simplify(A - (9*sp.pi/8 - sp.Rational(9, 4))) == 0
C.ck(19, A)

# 20 — inside both r = 1 + cos(theta) and r = 1
A = sector(sp.Integer(1), -sp.pi/2, sp.pi/2) + sector(1 + sp.cos(th), sp.pi/2, 3*sp.pi/2)
assert sp.simplify(A - (5*sp.pi/4 - 2)) == 0
C.ck(20, A)

# 21 — between two circles
C.ck(21, between(sp.Integer(5), sp.Integer(2), 0, 2*sp.pi))

# 22 — one circle entirely inside the other
big = sector(sp.Integer(4), 0, 2*sp.pi)
small = sector(4*sp.cos(th), -sp.pi/2, sp.pi/2)
assert big == 16*sp.pi and small == 4*sp.pi
C.ck(22, big - small)

# 23 — intersection of the cardioid and r = 3cos(theta)
assert meet(1 + sp.cos(th), 3*sp.cos(th)) == angles(sp.pi/3, -sp.pi/3)
C.ck_text(23, "theta = pi/3 and theta = -pi/3", "1 + cos = 3cos gives cos(theta) = 1/2.")

# 24 — inside both r = 2 and r = 4sin(theta)
assert meet(4*sp.sin(th), sp.Integer(2)) == angles(sp.pi/6, 5*sp.pi/6)
A = (sector(4*sp.sin(th), 0, sp.pi/6) + sector(sp.Integer(2), sp.pi/6, 5*sp.pi/6)
     + sector(4*sp.sin(th), 5*sp.pi/6, sp.pi))
assert sp.simplify(A - (8*sp.pi/3 - 2*sp.sqrt(3))) == 0
C.ck(24, A)

# 25 — the condition under which the single-integral formula is valid
C.ck_text(25, "R(theta) >= r(theta) >= 0 throughout", "otherwise the outer curve changes inside the interval.")

C.finish()
