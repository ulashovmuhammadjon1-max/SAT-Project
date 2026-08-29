"""sympy verification for CALC 6.1 Exploring Accumulations of Change.

Every computational question is recomputed here from the situation described in
the stem -- by integrating the rate function where one is given -- and checked
against the keyed choice.  The four numeric values behind each question's
choices are also checked pairwise so that no distractor is secretly equal to
the key, and each value is matched back to the text of its own choice so the
list below cannot drift out of step with the module.

CONCEPTUAL questions carry no computation: 1, 2, 11, 12, 16, 20, 22, 25.
"""
import re
import sympy as sp

from c6_1 import QUESTIONS

t = sp.Symbol('t', real=True)

CONCEPTUAL = {1, 2, 11, 12, 16, 20, 22, 25}
checked = set()


def chk(i, computed, values):
    """values: the numeric content of the module's choices, in module order."""
    q = QUESTIONS[i - 1]
    assert len(values) == len(q["choices"]), f"q{i}: wrong number of values"
    for a in range(len(values)):
        for b in range(a + 1, len(values)):
            assert sp.simplify(values[a] - values[b]) != 0, f"q{i}: choices {a},{b} equal"
    # the listed value really is the number printed in that choice
    for v, text in zip(values, q["choices"]):
        m = re.search(r"-?\d+(?:\.\d+)?", text)
        assert m, f"q{i}: no number in {text!r}"
        assert abs(float(m.group()) - float(v)) < 0.011, f"q{i}: {text!r} != {v}"
    assert sp.simplify(computed - values[q["ans"]]) == 0, f"q{i}: key mismatch"
    checked.add(i)


# 3: constant rate 7 gal/min for 15 min
chk(3, sp.integrate(7, (t, 0, 15)), [sp.Rational(15, 7), 22, 105, 210])
# 4: v(t) = 4t on [0, 6]
chk(4, sp.integrate(4 * t, (t, 0, 6)), [24, 72, 144, 216])
# 5: 6 bolts/min on [0, 4], 0 on [4, 9]
rate5 = sp.Piecewise((6, t <= 4), (0, True))
chk(5, sp.integrate(rate5, (t, 0, 9)), [6, 24, 30, 54])
# 6: -3 L/min for 8 min
chk(6, sp.integrate(-3, (t, 0, 8)), [-24, -11, 11, 24])
# 7: v(t) = 12 - 3t, displacement on [0, 4]
chk(7, sp.integrate(12 - 3 * t, (t, 0, 4)), [0, 12, 24, 48])
# 8: same v, displacement on [0, 6]
chk(8, sp.integrate(12 - 3 * t, (t, 0, 6)), [6, 18, 24, 30])
# 9: v(t) = 2t - 8, total distance on [0, 6]
chk(9, sp.integrate(sp.Abs(2 * t - 8), (t, 0, 6)), [4, 12, 16, 20])
# 10: rate rises linearly 2 -> 10 on [0, 4], so rate = 2 + 2t
chk(10, sp.integrate(2 + 2 * t, (t, 0, 4)), [8, 20, 24, 48])
# 13: Q(4) = Q(0) + 18
chk(13, 50 + 18, [18, 32, 68, 72])
# 14: 200 for 3 h then 500 for 2 h
rate14 = sp.Piecewise((200, t <= 3), (500, True))
chk(14, sp.integrate(rate14, (t, 0, 5)), [700, 1000, 1600, 3500])
# 15: 50 mph for 2 h then 30 mph for 1 h
rate15 = sp.Piecewise((50, t <= 2), (30, True))
chk(15, sp.integrate(rate15, (t, 0, 3)), [80, 100, 130, 150])
# 17: 70 + (-2)(4)
chk(17, 70 + sp.integrate(-2, (t, 0, 4)), [60, 62, 68, 78])
# 18: piecewise-linear velocity, total distance on [0, 7] (v >= 0 throughout)
v18 = sp.Piecewise((4 * t, t < 2), (8, t < 5), (8 - 4 * (t - 5), True))
chk(18, sp.integrate(v18, (t, 0, 7)), [24, 32, 40, 56])
# 19: 30 gallons plus a net rate of 2.5 gal/min for 5 min
chk(19, 30 + sp.integrate(4 - sp.Rational(3, 2), (t, 0, 5)),
    [sp.Rational(35, 2), 30, sp.Rational(85, 2), 50])
# 21: 3 in/h for 2 h then 1 in/h; solve for the time giving 8 inches
T = sp.Symbol('T', positive=True)
sol21 = sp.solve(sp.Eq(sp.integrate(3, (t, 0, 2)) + sp.integrate(1, (t, 2, T)), 8), T)
assert sol21 == [4], sol21
chk(21, sol21[0], [3, 4, 5, 6])
# 23: 6 cm^3/s on [0, 5], -2 on [5, 10]
rate23 = sp.Piecewise((6, t <= 5), (-2, True))
chk(23, sp.integrate(rate23, (t, 0, 10)), [10, 20, 30, 40])
# 24: additivity -- the change on [3, 7] is 5 - 12 = -7, a decrease of 7.
# The choices are sentences rather than bare numbers, so the match is on wording.
change_3_to_7 = sp.Integer(5) - sp.Integer(12)
assert change_3_to_7 == -7
assert QUESTIONS[23]["ans"] == 2
assert QUESTIONS[23]["choices"][2] == "The quantity decreased by 7 kilograms."
checked.add(24)

assert checked | CONCEPTUAL == set(range(1, 26)), sorted(set(range(1, 26)) - (checked | CONCEPTUAL))
assert not (checked & CONCEPTUAL)
assert len(QUESTIONS) == 25
for i, q in enumerate(QUESTIONS, 1):
    assert len(q["choices"]) == 4 and len(set(q["choices"])) == 4, f"q{i}: choices"
    assert 0 <= q["ans"] < 4, f"q{i}: ans"
print(f"c6_1: {len(checked)} computational questions verified, "
      f"{len(CONCEPTUAL)} conceptual; all 25 checked for shape.")
