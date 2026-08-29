"""sympy verification of every answer in c9_2.py (9.2 parametric second derivatives).

Run:  python3 verify_c9_2.py
"""
import sympy as sp

import c9_2
from c9_util import Checker, t

C = Checker(c9_2)


def d1(X, Y):
    return sp.simplify(sp.diff(Y, t) / sp.diff(X, t))


def d2(X, Y):
    """d^2y/dx^2 = d/dt(dy/dx) / (dx/dt) — the whole point of the topic."""
    return sp.simplify(sp.diff(d1(X, Y), t) / sp.diff(X, t))


# 1, 2 — conceptual statements of the formula and of the classic error.
C.ck_text(1, "divided by dx/dt", "d/dx = (d/dt)/(dx/dt) applied to dy/dx.")
C.ck_text(2, "not a ratio of second t-derivatives",
          "the ratio of second t-derivatives is not d^2y/dx^2, as x = t^2, y = t^3 shows: "
          "6t/2 = 3t, while the true value is 3/(4t).")
X, Y = t**2, t**3
assert sp.simplify(d2(X, Y) - sp.diff(Y, t, 2)/sp.diff(X, t, 2)) != 0

# 3 — the closed form in f and g.
f, g = sp.Function("f"), sp.Function("g")
general = sp.simplify(sp.diff(sp.diff(g(t), t)/sp.diff(f(t), t), t) / sp.diff(f(t), t))
closed = (sp.diff(g(t), t, 2)*sp.diff(f(t), t) - sp.diff(g(t), t)*sp.diff(f(t), t, 2)) \
    / sp.diff(f(t), t)**3
assert sp.simplify(general - closed) == 0
C.ck_text(3, "(g''(t)f'(t) - g'(t)f''(t))/(f'(t))^3", "quotient rule then one more division by f'.")

# 4, 5 — x = t^2, y = t^3
X, Y = t**2, t**3
C.ck(4, d2(X, Y))
C.ck(5, d2(X, Y).subs(t, 1))
assert d2(X, Y).subs(t, 1) == sp.Rational(3, 4)

# 6, 7 — x = t^2 + 1, y = t^3 - t
X, Y = t**2 + 1, t**3 - t
C.ck(6, d2(X, Y))
C.ck(7, d2(X, Y).subs(t, 1))
assert d2(X, Y).subs(t, 1) == 1

# 8 — x = t^3, y = t^2
C.ck(8, d2(t**3, t**2))

# 9 — x = e^t, y = e^(2t)
C.ck(9, d2(sp.exp(t), sp.exp(2*t)))
assert d2(sp.exp(t), sp.exp(2*t)) == 2

# 10 — x = 2t, y = t^2
C.ck(10, d2(2*t, t**2))

# 11 — x = sin t, y = cos t
C.ck(11, d2(sp.sin(t), sp.cos(t)))

# 12 — cycloid
X, Y = t - sp.sin(t), 1 - sp.cos(t)
C.ck(12, sp.simplify(d2(X, Y)))
assert sp.simplify(d2(X, Y) + 1/(1 - sp.cos(t))**2) == 0

# 13 — dy/dx and dx/dt given
slope, dxdt = t**2 + 1, 4*t
C.ck(13, sp.simplify(sp.diff(slope, t)/dxdt))

# 14 — dy/dx = 3t, x = t^2
C.ck(14, sp.simplify(sp.diff(3*t, t)/sp.diff(t**2, t)))

# 15 — dy/dx = t^3, dx/dt = 3, at t = 2
val = sp.simplify(sp.diff(t**3, t)/3)
C.ck(15, val.subs(t, 2))
assert val.subs(t, 2) == 4

# 16 — concavity at t = 1
X, Y = t**2 + 1, t**3 - t
assert d2(X, Y).subs(t, 1) == 1 > 0
C.ck_text(16, "concave up, because d^2y/dx^2 = 1 there", "positive second derivative at t = 1.")

# 17 — x = t^2, y = t^3 at t = -1
C.ck(17, d2(t**2, t**3).subs(t, -1))
assert d2(t**2, t**3).subs(t, -1) == sp.Rational(-3, 4)

# 18 — inflection point of x = 2t, y = t^3 - 3t
X, Y = 2*t, t**3 - 3*t
sec = d2(X, Y)
assert sp.simplify(sec - 3*t/2) == 0
assert sp.solve(sec, t) == [0] and sec.subs(t, -1) < 0 < sec.subs(t, 1)
C.ck_text(18, "t = 0", "d^2y/dx^2 = 3t/2 changes sign at t = 0 only.")

# 19 — the omitted final division
X, Y = t**2 + 1, t**4
assert sp.simplify(d1(X, Y) - 2*t**2) == 0
assert sp.simplify(sp.diff(d1(X, Y), t) - 4*t) == 0
C.ck(19, d2(X, Y))
assert d2(X, Y) == 2

# 20 — x = 3t, y = ln t
C.ck(20, d2(3*t, sp.log(t)))

# 21 — x = t^2, y = ln t
C.ck(21, d2(t**2, sp.log(t)))

# 22 — x = t^2 + t, y = t^3 at t = 1
X, Y = t**2 + t, t**3
C.ck(22, d2(X, Y).subs(t, 1))
assert d2(X, Y).subs(t, 1) == sp.Rational(4, 9)

# 23 — numerical f', f'', g', g''
fp, fpp, gp, gpp = 2, 1, 6, 4
C.ck(23, sp.Rational(gpp*fp - gp*fpp, fp**3))

# 24 — concave up where 3/(4t) > 0
sec = d2(t**2, t**3)
assert sp.solve(sp.Gt(sec, 0), t).as_set() == sp.Interval.open(0, sp.oo)
C.ck_text(24, "t > 0", "3/(4t) > 0 exactly for t > 0.")

# 25 — cycloid concavity sign
X, Y = t - sp.sin(t), 1 - sp.cos(t)
sec = sp.simplify(d2(X, Y))
for v in [sp.Rational(1, 2), 1, 2, 3, 4, 5, 6]:
    assert sec.subs(t, v) < 0
C.ck_text(25, "concave down everywhere", "-1/(1 - cos t)^2 is negative wherever it is defined.")

C.finish()
