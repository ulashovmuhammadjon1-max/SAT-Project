"""sympy verification for CALC 6.5 Interpreting the Behavior of Accumulation
Functions Involving Area.

The two described functions are made concrete:

  SIGNS  f(t) = (t - 3)(t - 7), whose sign pattern on (0, 10) is exactly the
         one in the table;
  AREAS  two different functions with the signed areas in the table -- a step
         function and a piecewise-parabolic one -- so that every answer below
         is confirmed to depend on the areas alone and not on the shape chosen.

CONCEPTUAL questions -- no computation, reasoning stated here:
 14  F'' = f', so f increasing makes F concave up
 15  G'' = g' < 0 where g decreases, so G is concave down
 16  an inflection point of F needs f' to change sign, i.e. f turns around;
     f(c) = 0 or a sign change of f gives an extremum of F instead
"""
import sympy as sp

from c6_5 import QUESTIONS

t, xs = sp.symbols('t x', real=True)

CONCEPTUAL = {14, 15, 16}
checked = set()


def key_is(i, text):
    q = QUESTIONS[i - 1]
    assert q["choices"][q["ans"]] == text, f"q{i}: key is {q['choices'][q['ans']]!r}"
    checked.add(i)


def chk(i, computed, values):
    q = QUESTIONS[i - 1]
    assert len(values) == len(q["choices"]), f"q{i}: wrong number of values"
    assert values[q["ans"]] is not None
    for a in range(len(values)):
        for b in range(a + 1, len(values)):
            if values[a] is None or values[b] is None:
                continue
            assert sp.simplify(values[a] - values[b]) != 0, f"q{i}: choices {a},{b} equal"
    assert sp.simplify(computed - values[q["ans"]]) == 0, f"q{i}: key mismatch"
    checked.add(i)


# ---------------------------------------------------------------- SIGNS -----
fs = (t - 3) * (t - 7)
assert all(fs.subs(t, v) > 0 for v in (0.5, 1, 2.9))
assert all(fs.subs(t, v) < 0 for v in (3.1, 5, 6.9))
assert all(fs.subs(t, v) > 0 for v in (7.1, 8, 9.9))
Fs = sp.integrate(fs, (t, 0, xs))
dFs = sp.diff(Fs, xs)
assert sp.simplify(dFs - fs.subs(t, xs)) == 0
# 1: F increases exactly where f > 0
assert all(dFs.subs(xs, v) > 0 for v in (0.5, 2.9, 7.1, 9.9))
assert all(dFs.subs(xs, v) < 0 for v in (3.1, 5, 6.9))
key_is(1, "0 < x < 3 and 7 < x < 10")
# 2, 3: first-derivative test at the two zeros
assert dFs.subs(xs, 2.9) > 0 > dFs.subs(xs, 3.1)          # local max at 3
assert dFs.subs(xs, 6.9) < 0 < dFs.subs(xs, 7.1)          # local min at 7
assert Fs.subs(xs, 3) > Fs.subs(xs, 2.9) and Fs.subs(xs, 3) > Fs.subs(xs, 3.1)
assert Fs.subs(xs, 7) < Fs.subs(xs, 6.9) and Fs.subs(xs, 7) < Fs.subs(xs, 7.1)
key_is(2, "x = 3")
key_is(3, "x = 7")
# 4: F' = 0 only at 3 and 7
assert sorted(sp.solve(sp.Eq(dFs, 0), xs)) == [3, 7]
key_is(4, "x = 3 and x = 7 only")

# ---------------------------------------------------------------- AREAS -----
step = sp.Piecewise((2, t < 3), (-2, t < 5), (sp.Rational(5, 4), True))
para = sp.Piecewise((sp.Rational(4, 3) * t * (3 - t), t < 3),
                    (-3 * (t - 3) * (5 - t), t < 5),
                    (sp.Rational(15, 32) * (t - 5) * (9 - t), True))
for model in (step, para):
    assert sp.integrate(model, (t, 0, 3)) == 6      # area 6 above the axis
    assert sp.integrate(model, (t, 3, 5)) == -4     # area 4 below the axis
    assert sp.integrate(model, (t, 5, 9)) == 5      # area 5 above the axis
    F = lambda b, m=model: sp.integrate(m, (t, 0, b))
    chk(5, F(3), [-6, 2, 6, 7])
    chk(6, F(5), [-4, 2, 6, 10])
    chk(7, F(9), [3, 7, 11, 15])
    # 8, 9: absolute extrema over the four candidates
    cand = {0: F(0), 3: F(3), 5: F(5), 9: F(9)}
    assert max(cand, key=lambda k: cand[k]) == 9
    assert min(cand, key=lambda k: cand[k]) == 0
    key_is(8, "x = 9")
    key_is(9, "x = 0")
    # 10: F decreasing on [3, 5] only
    assert F(5) < F(3) and F(3) > F(0) and F(9) > F(5)
    key_is(10, "[3, 5]")
    # 21: ordering of F(0), F(5), F(9)
    assert F(0) < F(5) < F(9)
    key_is(21, "F(0) < F(5) < F(9)")
    # 24: f < 0 on (3, 5) makes F decrease there, yet F(4) > 0 -- so "lies
    # below the x-axis" is not forced, while "is decreasing" is
    assert F(4) > 0 and F(sp.Rational(9, 2)) < F(sp.Rational(7, 2))
    key_is(24, "is decreasing")

# ------------------------------------------------- explicit integrands ------
F11 = sp.integrate(t - 4, (t, 0, xs))
chk(11, F11, [xs**2 / 2 - 4 * xs, xs**2 / 2 - 4 * xs + 8, xs - 4, xs**2 - 4 * xs])
crit12 = sp.solve(sp.Eq(sp.diff(F11, xs), 0), xs)
assert crit12 == [4] and sp.diff(F11, xs, 2).subs(xs, 4) > 0
chk(12, sp.Integer(crit12[0]), [0, 2, 4, 8])
chk(13, F11.subs(xs, 6), [-8, -6, 2, 6])

# 17: f > 0 forces F increasing, but F(x) < 0 for x < 0 (take f = 1)
F17 = sp.integrate(sp.Integer(1), (t, 0, xs))
assert sp.diff(F17, xs) > 0 and F17.subs(xs, -2) < 0
key_is(17, "F is increasing on the whole real line")

# 18, 19: F(x) = int from 2 to x of (t - 1)(t - 5) dt
f18 = (t - 1) * (t - 5)
F18 = sp.integrate(f18, (t, 2, xs))
d18 = sp.diff(F18, xs)
assert d18.subs(xs, 0) > 0 > d18.subs(xs, 2)              # local max at x = 1
assert sorted(sp.solve(sp.Eq(d18, 0), xs)) == [1, 5]
chk(18, sp.Integer(1), [1, 2, 3, 5])
infl = sp.solve(sp.Eq(sp.diff(F18, xs, 2), 0), xs)
assert infl == [3] and sp.diff(F18, xs, 2).subs(xs, 2) < 0 < sp.diff(F18, xs, 2).subs(xs, 4)
chk(19, sp.Integer(infl[0]), [1, 3, 5, 2])

# 20: F(x) = 1 - cos(x) on [0, 2pi]
F20 = sp.integrate(sp.sin(t), (t, 0, xs))
assert sp.simplify(F20 - (1 - sp.cos(xs))) == 0
vals20 = [F20.subs(xs, v) for v in (0, sp.pi / 2, sp.pi, 3 * sp.pi / 2, 2 * sp.pi)]
assert max(vals20) == 2
chk(20, sp.Integer(2), [0, 1, 2, sp.pi])

# 22: F(x) = int from 0 to x of (t^2 - 9) dt
F22 = sp.integrate(t**2 - 9, (t, 0, xs))
d22 = sp.diff(F22, xs)
assert d22.subs(xs, -4) > 0 > d22.subs(xs, 0)             # local max at x = -3
chk(22, sp.Integer(-3), [-3, 0, 3, 9])

# 23: absolute minimum of int from 1 to x of (t - 3) dt on [0, 5]
F23 = sp.integrate(t - 3, (t, 1, xs))
cands23 = {v: F23.subs(xs, v) for v in (0, 3, 5)}
assert min(cands23.values()) == -2 and cands23[3] == -2
chk(23, sp.Integer(-2), [-2, sp.Rational(-3, 2), 0, 2])

# 25: F'(3) = 0 without a sign change, so no extremum
F25 = sp.integrate((t - 3)**2, (t, 0, xs))
d25 = sp.diff(F25, xs)
assert d25.subs(xs, 3) == 0 and d25.subs(xs, 2) > 0 and d25.subs(xs, 4) > 0
assert F25.subs(xs, 2) < F25.subs(xs, 3) < F25.subs(xs, 4)
key_is(25, "F has a horizontal tangent at x = 3 but no extremum there.")

assert checked | CONCEPTUAL == set(range(1, 26)), sorted(set(range(1, 26)) - (checked | CONCEPTUAL))
assert not (checked & CONCEPTUAL)
assert len(QUESTIONS) == 25
for k, q in enumerate(QUESTIONS, 1):
    assert len(q["choices"]) == 4 and len(set(q["choices"])) == 4, f"q{k}: choices"
    assert 0 <= q["ans"] < 4, f"q{k}: ans"
print(f"c6_5: {len(checked)} computational questions verified, "
      f"{len(CONCEPTUAL)} conceptual; all 25 checked for shape.")
