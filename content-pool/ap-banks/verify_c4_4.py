# Verification for CALC 4.4 — Introduction to Related Rates.
# Each relation is differentiated by sympy with the variables declared as functions
# of t, so the chain rule is applied by the CAS rather than assumed by the author.
import sympy as sp

import c4_4

t = sp.Symbol('t', positive=True)
x = sp.Function('x')(t)
y = sp.Function('y')(t)
z = sp.Function('z')(t)
r = sp.Function('r')(t)
h = sp.Function('h')(t)
s = sp.Function('s')(t)
b = sp.Function('b')(t)

dx, dy, dz, dr, dh, ds, db = (sp.diff(f, t) for f in (x, y, z, r, h, s, b))

# q1: x^2 + y^2 = 25
assert sp.simplify(sp.diff(x**2 + y**2 - 25, t) - (2 * x * dx + 2 * y * dy)) == 0

# q2: A = pi r^2
assert sp.simplify(sp.diff(sp.pi * r**2, t) - 2 * sp.pi * r * dr) == 0

# q3: V = (4/3) pi r^3
assert sp.simplify(sp.diff(sp.Rational(4, 3) * sp.pi * r**3, t) - 4 * sp.pi * r**2 * dr) == 0

# q4: V = s^3
assert sp.simplify(sp.diff(s**3, t) - 3 * s**2 * ds) == 0

# q5: A = (1/2) b h
assert sp.simplify(sp.diff(b * h / 2, t) - (b * dh + h * db) / 2) == 0

# q6: xy = 12
assert sp.simplify(sp.diff(x * y - 12, t) - (x * dy + y * dx)) == 0

# q7: d/dt r^3
assert sp.simplify(sp.diff(r**3, t) - 3 * r**2 * dr) == 0

# q11: dA/dt with dr/dt = 2, r = 5
dA = sp.diff(sp.pi * r**2, t).subs({dr: 2, r: 5})
assert dA == 20 * sp.pi

# q12: dV/dt with ds/dt = 1/2, s = 4
dV_cube = sp.diff(s**3, t).subs({ds: sp.Rational(1, 2), s: 4})
assert dV_cube == 24

# q13: x^2 + y^2 = 169 at (5, 12) with dx/dt = 4.
# The unknown rate is swapped for a plain symbol BEFORE the point is substituted:
# substituting y(t) -> 12 first would turn Derivative(y(t), t) into Derivative(12, t) = 0
# and silently delete the very term being solved for.
Dy = sp.Symbol('Dy')
expr13 = sp.diff(x**2 + y**2 - 169, t).subs(dy, Dy).subs(dx, 4).subs({x: 5, y: 12})
sol = sp.solve(sp.Eq(expr13, 0), Dy)
assert sol == [sp.Rational(-5, 3)], sol

# q14: P = 4s, ds/dt = 3
assert sp.diff(4 * s, t).subs(ds, 3) == 12

# q15: C = 2 pi r, dr/dt = 1/2
assert sp.diff(2 * sp.pi * r, t).subs(dr, sp.Rational(1, 2)) == sp.pi

# q16: V = pi r^2 h, both varying
assert sp.simplify(sp.diff(sp.pi * r**2 * h, t) - sp.pi * (2 * r * h * dr + r**2 * dh)) == 0

# q17: r fixed at 3
assert sp.simplify(sp.diff(sp.pi * 9 * h, t) - 9 * sp.pi * dh) == 0

# q18: z^2 = x^2 + y^2
assert sp.simplify(sp.diff(z**2 - x**2 - y**2, t) - (2 * z * dz - 2 * x * dx - 2 * y * dy)) == 0

# q19: y = sqrt(x), dx/dt = 6 at x = 9
assert sp.diff(sp.sqrt(x), t).subs({x: 9, dx: 6}) == 1

# q20: y = sin(x), dx/dt = 3 at x = pi/3
assert sp.diff(sp.sin(x), t).subs({x: sp.pi / 3, dx: 3}) == sp.Rational(3, 2)
assert sp.simplify(sp.sin(sp.pi / 3) * 3 - 3 * sp.sqrt(3) / 2) == 0   # the sin/cos distractor

# q21: cone with r = h/2
V_cone = sp.Rational(1, 3) * sp.pi * (h / 2)**2 * h
assert sp.simplify(V_cone - sp.pi * h**3 / 12) == 0
assert sp.simplify(sp.diff(V_cone, t) - sp.pi * h**2 * dh / 4) == 0

# q22: x^2 y = 8
assert sp.simplify(sp.diff(x**2 * y - 8, t) - (2 * x * y * dx + x**2 * dy)) == 0

# q23: dA/dt = 12, r = 3  ->  dr/dt = 2/pi  (same symbol-first ordering as q13)
Dr = sp.Symbol('Dr')
expr23 = sp.diff(sp.pi * r**2, t).subs(dr, Dr).subs(r, 3)
sol_r = sp.solve(sp.Eq(expr23, 12), Dr)
assert sol_r == [2 / sp.pi], sol_r

# Structure: 25 questions, four distinct choices, in-range key.
assert len(c4_4.QUESTIONS) == 25, len(c4_4.QUESTIONS)
for i, q in enumerate(c4_4.QUESTIONS, 1):
    assert len(q["choices"]) == 4, (i, len(q["choices"]))
    assert len(set(c.strip().lower() for c in q["choices"])) == 4, i
    assert 0 <= q["ans"] < 4, i
    assert "$" not in q["q"] and all("$" not in c for c in q["choices"]), i

print("c4_4: 25 questions, every relation differentiated by sympy, structure OK")
