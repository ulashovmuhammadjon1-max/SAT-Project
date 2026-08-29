# Verification for CALC 4.2 — Straight-Line Motion.
# Every velocity, acceleration, root, extreme value, distance, and sign claim used
# as a key in c4_2.py is recomputed here with sympy.
import sympy as sp

import c4_2

t = sp.Symbol('t', real=True)


def sign_pair(v_expr, a_expr, t0):
    """Return (sign v, sign a) at t0 as +-1/0 so the speeding-up claims are explicit."""
    return sp.sign(v_expr.subs(t, t0)), sp.sign(a_expr.subs(t, t0))


# --- s(t) = t^3 - 6t^2 + 9t : q6-q10, q22 ---
s1 = t**3 - 6 * t**2 + 9 * t
v1, a1 = sp.diff(s1, t), sp.diff(s1, t, 2)
assert sp.expand(v1) == 3 * t**2 - 12 * t + 9
assert sp.expand(a1) == 6 * t - 12
assert sp.solve(v1, t) == [1, 3]
# moving negative exactly on (1, 3)
assert v1.subs(t, sp.Rational(1, 2)) > 0 and v1.subs(t, 2) < 0 and v1.subs(t, 4) > 0
# q9: at t = 2.5, v = -2.25 and a = 3 -> opposite signs -> slowing down
assert sp.nsimplify(v1.subs(t, sp.Rational(5, 2))) == sp.Rational(-9, 4)
assert float(v1.subs(t, sp.Rational(5, 2))) == -2.25
assert a1.subs(t, sp.Rational(5, 2)) == 3
assert sign_pair(v1, a1, sp.Rational(5, 2)) == (-1, 1)
# q10: total distance on [0, 4] with turning points at 1 and 3
pts = [0, 1, 3, 4]
vals = [s1.subs(t, p) for p in pts]
assert vals == [0, 4, 0, 4]
assert sum(abs(vals[i + 1] - vals[i]) for i in range(3)) == 12
# q22: average velocity on [0, 4]
assert sp.nsimplify((s1.subs(t, 4) - s1.subs(t, 0)) / 4) == 1

# --- v(t) = t^2 - 4t + 3 : q11 (speeding up) ---
v2 = t**2 - 4 * t + 3
a2 = sp.diff(v2, t)
assert sp.expand(a2) == 2 * t - 4
for t0, same in [(sp.Rational(1, 2), False), (sp.Rational(3, 2), True),
                 (sp.Rational(5, 2), False), (4, True)]:
    sv, sa = sign_pair(v2, a2, t0)
    assert (sv == sa) == same, (t0, sv, sa)

# --- s(t) = -16t^2 + 64t + 80 : q12-q15 ---
s3 = -16 * t**2 + 64 * t + 80
v3, a3 = sp.diff(s3, t), sp.diff(s3, t, 2)
assert sp.expand(v3) == -32 * t + 64
assert v3.subs(t, 1) == 32 and s3.subs(t, 1) == 128
assert sp.solve(v3, t) == [2]
assert s3.subs(t, 2) == 144
ground = [r for r in sp.solve(s3, t) if r >= 0]
assert ground == [5]
assert v3.subs(t, 5) == -96 and sp.Abs(v3.subs(t, 5)) == 96
assert a3 == -32

# --- s(t) = 2 sin(t) : q16 ---
s4 = 2 * sp.sin(t)
v4, a4 = sp.diff(s4, t), sp.diff(s4, t, 2)
assert sp.simplify(v4.subs(t, 3 * sp.pi / 4) + sp.sqrt(2)) == 0
assert sp.simplify(a4.subs(t, 3 * sp.pi / 4) + sp.sqrt(2)) == 0
assert sign_pair(v4, a4, 3 * sp.pi / 4) == (-1, -1)   # same sign -> speeding up

# --- s(t) = t e^(-t) : q17, q18 ---
s5 = t * sp.exp(-t)
v5, a5 = sp.diff(s5, t), sp.diff(s5, t, 2)
assert sp.simplify(v5 - (1 - t) * sp.exp(-t)) == 0
assert sp.simplify(a5 - (t - 2) * sp.exp(-t)) == 0
assert sign_pair(v5, a5, sp.Rational(3, 2)) == (-1, -1)   # both negative -> speeding up
assert sp.simplify(v5.subs(t, sp.Rational(3, 2)) - (-sp.exp(sp.Rational(-3, 2)) / 2)) == 0

# --- v(t) = (t - 2)^2 : q20, no sign change ---
v6 = (t - 2)**2
assert sp.solve(v6, t) == [2]
assert v6.subs(t, 1) > 0 and v6.subs(t, 3) > 0

# --- v(t) = 4 - t^2 : q22, q23 ---
v7 = 4 - t**2
a7 = sp.diff(v7, t)
assert sign_pair(v7, a7, 1) == (1, -1)    # slowing down on (0, 2)
assert sign_pair(v7, a7, 3) == (-1, -1)   # speeding up for t > 2

# --- s(t) = 2t^3 - 21t^2 + 60t : q24, q25 ---
s8 = 2 * t**3 - 21 * t**2 + 60 * t
v8, a8 = sp.diff(s8, t), sp.diff(s8, t, 2)
assert sp.simplify(v8 - 6 * (t - 2) * (t - 5)) == 0
assert sp.solve(v8, t) == [2, 5]
assert v8.subs(t, 1) > 0 and v8.subs(t, 3) < 0     # positive -> negative at t = 2
assert v8.subs(t, 4) < 0 and v8.subs(t, 6) > 0     # negative -> positive at t = 5
assert sp.expand(a8) == 12 * t - 42
assert sp.solve(a8, t) == [sp.Rational(7, 2)]
assert sign_pair(v8, a8, 3) == (-1, -1)            # speeding up on (2, 3.5)
assert sign_pair(v8, a8, 4) == (-1, 1)             # slowing down on (3.5, 5)

# Structure: 25 questions, four distinct choices, in-range key.
assert len(c4_2.QUESTIONS) == 25, len(c4_2.QUESTIONS)
for i, q in enumerate(c4_2.QUESTIONS, 1):
    assert len(q["choices"]) == 4, (i, len(q["choices"]))
    assert len(set(c.strip().lower() for c in q["choices"])) == 4, i
    assert 0 <= q["ans"] < 4, i
    assert "$" not in q["q"] and all("$" not in c for c in q["choices"]), i

print("c4_2: 25 questions, all motion computations verified with sympy, structure OK")
