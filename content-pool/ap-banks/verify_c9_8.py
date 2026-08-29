"""sympy verification of every answer in c9_8.py (9.8 area inside one polar curve).

Run:  python3 verify_c9_8.py
"""
import sympy as sp

import c9_8
from unit9_util import Checker, th

C = Checker(c9_8)


def area(r, a, b):
    """The polar area formula, with the 1/2 and the square both present."""
    return sp.simplify(sp.Rational(1, 2)*sp.integrate(r**2, (th, a, b)))


# 1 — the formula.
C.ck_text(1, "(1/2) int from a to b of r^2 dtheta", "a sector of angle dtheta has area (1/2)r^2 dtheta.")

# 2, 3 — circular sectors
C.ck(2, area(sp.Integer(4), 0, sp.pi/3))
C.ck(3, area(sp.Integer(2), 0, 2*sp.pi))
assert area(sp.Integer(2), 0, 2*sp.pi) == sp.pi*2**2

# 4, 5 — the cardioid
r = 1 + sp.cos(th)
C.ck_int(4, 0, 2*sp.pi, r**2, coeff=sp.Rational(1, 2))
C.ck(5, area(r, 0, 2*sp.pi))
assert area(r, 0, 2*sp.pi) == 3*sp.pi/2

# 6, 7 — r = 2 sin theta is traced once on [0, pi]
r = 2*sp.sin(th)
assert area(r, 0, sp.pi) == sp.pi and area(r, 0, 2*sp.pi) == 2*sp.pi
C.ck_text(6, "0 to pi", "integrating to 2pi doubles the area of this circle.")
C.ck(7, area(r, 0, sp.pi))

# 8, 9, 10 — the four-petal rose
r = sp.cos(2*th)
C.ck_int(8, -sp.pi/4, sp.pi/4, r**2, coeff=sp.Rational(1, 2))
petal = area(r, -sp.pi/4, sp.pi/4)
assert petal == sp.pi/8
C.ck(9, petal)
C.ck(10, 4*petal)

# 11 — one petal of a three-petal rose
r = sp.sin(3*th)
assert sp.solve(sp.Eq(r, 0), th)[0] == 0
C.ck(11, area(r, 0, sp.pi/3))

# 12 — a spiral sector
C.ck(12, area(2*th, 0, sp.pi))

# 13, 14 — the two classic errors
assert sp.integrate(3**2, (th, 0, 2*sp.pi)) == 18*sp.pi          # what the student got
assert area(sp.Integer(3), 0, 2*sp.pi) == 9*sp.pi                # the correct area
C.ck_text(13, "the factor of 1/2 was dropped", "the correct value is half of 18pi.")
r = 1 + sp.cos(th)
assert sp.Rational(1, 2)*sp.integrate(r, (th, 0, 2*sp.pi)) == sp.pi   # unsquared
assert area(r, 0, 2*sp.pi) == 3*sp.pi/2
C.ck_text(14, "r was not squared", "squaring gives 3pi/2, not pi.")

# 15 — exponential spiral
C.ck(15, area(sp.exp(th), 0, 1))

# 16, 17 — cardioid and limacon
C.ck(16, area(1 + sp.sin(th), 0, 2*sp.pi))
C.ck(17, area(2 + sp.cos(th), 0, 2*sp.pi))

# 18, 19 — r = 3 cos theta is traced once on [-pi/2, pi/2]
r = 3*sp.cos(th)
assert area(r, -sp.pi/2, sp.pi/2) == 9*sp.pi/4 == sp.pi*sp.Rational(3, 2)**2
assert area(r, 0, 2*sp.pi) == 9*sp.pi/2
C.ck(18, area(r, -sp.pi/2, sp.pi/2))
C.ck_text(19, "traced twice", "the circle closes at theta = pi and is retraced with r < 0.")

# 20, 21 — the inner loop of a limacon
r = 1 + 2*sp.cos(th)
zeros = sorted(s for s in sp.solve(sp.Eq(r, 0), th) if 0 <= s <= 2*sp.pi)
assert zeros == [2*sp.pi/3, 4*sp.pi/3], zeros
assert sp.simplify(r.subs(th, sp.pi)) == -1  # r is negative between the zeros
C.ck_text(20, "2pi/3 to 4pi/3", "r < 0 exactly between the two zeros of 1 + 2cos(theta).")
inner = area(r, 2*sp.pi/3, 4*sp.pi/3)
assert sp.simplify(inner - (sp.pi - 3*sp.sqrt(3)/2)) == 0
C.ck(21, inner)

# 22 — decimal area of a spiral sector
A = area(th, 0, sp.pi/2)
assert sp.simplify(A - sp.pi**3/48) == 0
C.ck_num(22, A)

# 23 — the symmetric set-up, coefficient 1
r = 1 + sp.cos(th)
C.ck_int(23, 0, sp.pi, r**2, coeff=1)
assert sp.integrate(r**2, (th, 0, sp.pi)) == 3*sp.pi/2 == area(r, 0, 2*sp.pi)

# 24 — squaring removes the radical
C.ck(24, area(sp.sqrt(sp.cos(th)), -sp.pi/2, sp.pi/2))

# 25 — one petal of r = 2cos(3theta)
C.ck(25, area(2*sp.cos(3*th), -sp.pi/6, sp.pi/6))

C.finish()
