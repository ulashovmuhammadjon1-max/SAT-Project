# Verification for CALC 4.5 — Solving Related Rates Problems.
# Each problem is set up as an equation in functions of t, differentiated by sympy,
# and then solved for the unknown rate. Rate symbols are substituted BEFORE point
# values: substituting y(t) -> 12 first would turn Derivative(y(t), t) into
# Derivative(12, t) = 0 and delete the term being solved for.
import sympy as sp

import c4_5

t = sp.Symbol('t', positive=True)
x, y, z, r, h, s, th, P, V = (sp.Function(n)(t) for n in
                              ('x', 'y', 'z', 'r', 'h', 's', 'th', 'P', 'V'))
D = sp.Symbol('D')          # the unknown rate in each problem


def solve_rate(relation, rates, values, unknown=D):
    """Differentiate relation = 0 in t, put in the known/unknown rates, then the point."""
    e = sp.diff(relation, t)
    for d, v in rates:
        e = e.subs(d, v)
    e = e.subs(values)
    sols = sp.solve(sp.Eq(e, 0), unknown)
    assert len(sols) == 1, (relation, sols)
    return sp.simplify(sols[0])


dx, dy, dz, dr, dh, ds, dth, dP, dV = (sp.diff(f, t) for f in
                                       (x, y, z, r, h, s, th, P, V))

# q1: 13-ft ladder, dx/dt = 2, x = 5, y = 12
assert solve_rate(x**2 + y**2 - 169, [(dy, D), (dx, 2)], {x: 5, y: 12}) == sp.Rational(-5, 6)

# q2: same ladder, angle with the ground: 13 cos(theta) = x
theta0 = sp.acos(sp.Rational(5, 13))
assert sp.simplify(sp.sin(theta0) - sp.Rational(12, 13)) == 0
assert solve_rate(13 * sp.cos(th) - x, [(dth, D), (dx, 2)], {th: theta0}) == sp.Rational(-1, 6)

# q3: same ladder, area of the triangle
dA = sp.diff(x * y / 2, t).subs(dy, sp.Rational(-5, 6)).subs(dx, 2).subs({x: 5, y: 12})
assert sp.nsimplify(dA) == sp.Rational(119, 12)

# q4/q5: sphere, dV/dt = 100 at r = 5
Vsph = sp.Rational(4, 3) * sp.pi * r**3
assert solve_rate(Vsph - V, [(dr, D), (dV, 100)], {r: 5}) == 1 / sp.pi
dS = sp.diff(4 * sp.pi * r**2, t).subs(dr, 1 / sp.pi).subs(r, 5)
assert sp.simplify(dS - 40) == 0

# q6: melting snowball, dr/dt = -0.1 at r = 8
dVsnow = sp.diff(Vsph, t).subs(dr, sp.Rational(-1, 10)).subs(r, 8)
assert sp.simplify(dVsnow + sp.Rational(128, 5) * sp.pi) == 0
assert round(float(dVsnow), 1) == -80.4
assert round(float(-sp.Rational(128, 5)), 1) == -25.6      # the pi-less distractor

# q7: ripple, dr/dt = 2 at r = 10
dAr = sp.diff(sp.pi * r**2, t).subs(dr, 2).subs(r, 10)
assert dAr == 40 * sp.pi

# q8: cone tank, r = h/2, dV/dt = 9 at h = 6
Vcone = sp.Rational(1, 3) * sp.pi * (h / 2)**2 * h
assert sp.simplify(Vcone - sp.pi * h**3 / 12) == 0
assert solve_rate(Vcone - V, [(dh, D), (dV, 9)], {h: 6}) == 1 / sp.pi

# q9: sand pile, diameter = height so r = h/2, dV/dt = 10 at h = 4
assert solve_rate(Vcone - V, [(dh, D), (dV, 10)], {h: 4}) == 5 / (2 * sp.pi)

# q10/q11: shadow, person 6 ft, post 15 ft, walking 5 ft/s
# similar triangles: 6/s = 15/(x + s)  ->  6(x + s) = 15 s  ->  s = 2x/3
s_of_x = sp.solve(sp.Eq(6 * (sp.Symbol('X') + sp.Symbol('S')), 15 * sp.Symbol('S')),
                  sp.Symbol('S'))[0]
assert sp.simplify(s_of_x - 2 * sp.Symbol('X') / 3) == 0
assert solve_rate(3 * s - 2 * x, [(ds, D), (dx, 5)], {}) == sp.Rational(10, 3)
# tip of shadow is at x + s = 5x/3
assert sp.nsimplify(sp.diff(5 * x / 3, t).subs(dx, 5)) == sp.Rational(25, 3)

# q12: two cars, north 60 and east 80, after one hour
assert solve_rate(z**2 - x**2 - y**2, [(dz, D), (dx, 80), (dy, 60)],
                  {x: 80, y: 60, z: 100}) == 100

# q13: car 30 mi north at 40 mph, truck 40 mi east at 30 mph
assert solve_rate(z**2 - x**2 - y**2, [(dz, D), (dx, 30), (dy, 40)],
                  {x: 40, y: 30, z: 50}) == 48

# q14: kite at constant height 100, horizontal rate 8, string 260
assert sp.sqrt(260**2 - 100**2) == 240
assert solve_rate(z**2 - x**2 - 100**2, [(dz, D), (dx, 8)],
                  {x: 240, z: 260}) == sp.Rational(96, 13)

# q15: rectangular tank 4 by 3, inflow 6
assert solve_rate(12 * h - V, [(dh, D), (dV, 6)], {}) == sp.Rational(1, 2)

# q16: baseball, 90-ft sides, runner 30 ft past first at 25 ft/s
z16 = sp.sqrt(90**2 + 30**2)
assert sp.simplify(z16 - 30 * sp.sqrt(10)) == 0
ans16 = solve_rate(z**2 - 90**2 - x**2, [(dz, D), (dx, 25)], {x: 30, z: z16})
assert sp.simplify(ans16 - 25 / sp.sqrt(10)) == 0
assert round(float(ans16), 2) == 7.91

# q17: balloon rising 10 ft/s, observer 100 ft away, at height 100
ans17 = solve_rate(sp.tan(th) - h / 100, [(dth, D), (dh, 10)], {th: sp.pi / 4})
assert ans17 == sp.Rational(1, 20)

# q18: Boyle's law PV = 600, V = 30, dV/dt = -5
assert solve_rate(P * V - 600, [(dP, D), (dV, -5)], {V: 30, P: 20}) == sp.Rational(10, 3)

# q19: square, ds/dt = 2 at s = 10
assert sp.diff(s**2, t).subs(ds, 2).subs(s, 10) == 40

# q20: cube surface area, ds/dt = 0.5 at s = 4
assert sp.diff(6 * s**2, t).subs(ds, sp.Rational(1, 2)).subs(s, 4) == 24

# q21: trough, width = 3h, length 10, so V = 15 h^2; dV/dt = 12 at h = 0.5
Vtr = 10 * sp.Rational(1, 2) * (3 * h) * h
assert sp.simplify(Vtr - 15 * h**2) == 0
assert solve_rate(Vtr - V, [(dh, D), (dV, 12)], {h: sp.Rational(1, 2)}) == sp.Rational(4, 5)

# q24: both vehicles approaching the intersection
ans24 = solve_rate(z**2 - x**2 - y**2, [(dz, D), (dx, -45), (dy, -60)],
                   {x: sp.Rational(2, 5), y: sp.Rational(3, 10), z: sp.Rational(1, 2)})
assert ans24 == -72

# q25: dV/dt = 20 at the instant the surface area is 100 pi
r25 = [v for v in sp.solve(sp.Eq(4 * sp.pi * sp.Symbol('R', positive=True)**2, 100 * sp.pi),
                           sp.Symbol('R', positive=True)) if v > 0]
assert r25 == [5], r25
assert solve_rate(Vsph - V, [(dr, D), (dV, 20)], {r: 5}) == 1 / (5 * sp.pi)

# Structure: 25 questions, four distinct choices, in-range key.
assert len(c4_5.QUESTIONS) == 25, len(c4_5.QUESTIONS)
for i, q in enumerate(c4_5.QUESTIONS, 1):
    assert len(q["choices"]) == 4, (i, len(q["choices"]))
    assert len(set(c.strip().lower() for c in q["choices"])) == 4, i
    assert 0 <= q["ans"] < 4, i
    assert "$" not in q["q"] and all("$" not in c for c in q["choices"]), i

print("c4_5: 25 questions, every related rate solved by sympy, structure OK")
