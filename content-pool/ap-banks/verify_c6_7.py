"""sympy verification for CALC 6.7 The Fundamental Theorem of Calculus and
Definite Integrals.

Each definite integral is evaluated by sp.integrate, and the antiderivative
quoted in the rationale is checked independently by differentiating it back to
the integrand -- so both halves of the Fundamental Theorem are exercised.

CONCEPTUAL questions -- no computation, reasoning stated here:
  1  the statement F(b) - F(a)
 16  the net change theorem
"""
import sympy as sp

from c6_7 import QUESTIONS

x, t = sp.symbols('x t', real=True)

CONCEPTUAL = {1, 16}
checked = set()


def chk(i, computed, values):
    q = QUESTIONS[i - 1]
    assert len(values) == len(q["choices"]), f"q{i}: wrong number of values"
    assert values[q["ans"]] is not None
    for p in range(len(values)):
        for r in range(p + 1, len(values)):
            if values[p] is None or values[r] is None:
                continue
            assert sp.simplify(values[p] - values[r]) != 0, f"q{i}: choices {p},{r} equal"
    assert sp.simplify(computed - values[q["ans"]]) == 0, f"q{i}: key mismatch"
    checked.add(i)


def key_is(i, text):
    q = QUESTIONS[i - 1]
    assert q["choices"][q["ans"]] == text, f"q{i}: key is {q['choices'][q['ans']]!r}"
    checked.add(i)


def ftc(integrand, F, lo, hi, var=x):
    """Evaluate int lo..hi of `integrand`, checking F is really its antiderivative."""
    assert sp.simplify(sp.diff(F, var) - integrand) == 0, f"{F} is not an antiderivative"
    value = sp.integrate(integrand, (var, lo, hi))
    assert sp.simplify(value - (F.subs(var, hi) - F.subs(var, lo))) == 0
    return sp.simplify(value)


E = sp.E
chk(2, ftc(2 * x, x**2, 0, 3), [3, 6, 9, 18])
chk(3, ftc(3 * x**2, x**3, 1, 4), [21, 45, 63, 64])
chk(4, ftc(x**2 + 1, x**3 / 3 + x, 0, 2),
    [sp.Rational(8, 3), 4, sp.Rational(14, 3), sp.Rational(20, 3)])
chk(5, ftc(1 / x, sp.log(x), 1, E), [0, 1, E - 1, E])
chk(6, ftc(sp.cos(x), sp.sin(x), 0, sp.pi / 2), [-1, 0, 1, sp.pi / 2])
chk(7, ftc(sp.exp(x), sp.exp(x), 0, 1), [1, E - 1, E, E + 1])
chk(8, ftc(2 * x - 3, x**2 - 3 * x, -1, 2), [-6, -2, 2, 6])
chk(9, ftc(sp.sqrt(x), sp.Rational(2, 3) * x**sp.Rational(3, 2), 1, 9),
    [sp.Rational(16, 3), sp.Rational(26, 3), sp.Rational(52, 3), 18])
chk(10, ftc(x - 2, x**2 / 2 - 2 * x, 0, 4), [-4, 0, 4, 8])

# 11: the reversal error -- the two orders differ only in sign
F11 = x**3 / 3
right = sp.integrate(x**2, (x, 1, 3))
wrong = F11.subs(x, 1) - F11.subs(x, 3)
assert right == sp.Rational(26, 3) and wrong == -right
key_is(11, "The limits were subtracted in the wrong order; the correct value is 26/3.")

chk(12, ftc(sp.sin(x), -sp.cos(x), 0, sp.pi), [-2, 0, 1, 2])
chk(13, ftc(sp.Integer(4), 4 * x, 2, 5), [4, 12, 20, 28])
chk(14, ftc(1 / x**2, -1 / x, 1, 2),
    [sp.Rational(-1, 2), sp.Rational(1, 2), sp.log(2), sp.Rational(7, 3)])
chk(15, ftc(3 * t**2, t**3, 0, 2, var=t), [4, 6, 8, 12])

# 17: net change with a known initial value
assert 5 + 7 == 12
chk(17, sp.Integer(12), [2, 7, 12, 35])

chk(18, ftc(x**2, x**3 / 3, -2, 2),
    [0, sp.Rational(8, 3), sp.Rational(16, 3), sp.Rational(32, 3)])
chk(19, ftc(4 * x**3 - 2 * x, x**4 - x**2, 0, 1), [-1, 0, 1, 2])
chk(20, ftc(sp.sec(x)**2, sp.tan(x), 0, sp.pi / 4),
    [0, sp.Rational(1, 2), 1, sp.sqrt(2)])
chk(21, ftc(x**sp.Rational(-2, 3), 3 * x**sp.Rational(1, 3), 1, 8),
    [3, 6, sp.Rational(9, 2), sp.Rational(21, 2)])
chk(22, ftc(sp.exp(2 * x), sp.exp(2 * x) / 2, 0, sp.log(2)),
    [1, sp.Rational(3, 2), 2, 3])

# 23: |x| needs the integral split, which sympy does for us
v23 = sp.integrate(sp.Abs(x), (x, -1, 1))
assert v23 == sp.integrate(-x, (x, -1, 0)) + sp.integrate(x, (x, 0, 1))
chk(23, v23, [0, sp.Rational(1, 2), 1, 2])

chk(24, ftc(t**2 - 4, t**3 / 3 - 4 * t, 0, 3, var=t), [-3, 3, 5, 9])

# 25: 1/x^2 is positive wherever it is defined, so a negative "value" is
# impossible; sympy reports the integral as divergent
assert sp.integrate(1 / x**2, (x, -1, 1)) is sp.oo
assert (-1 / x).subs(x, 1) - (-1 / x).subs(x, -1) == -2   # the bogus computation
key_is(25, "The integrand is not continuous on [-1, 1], so the Fundamental Theorem does not apply.")

assert checked | CONCEPTUAL == set(range(1, 26)), sorted(set(range(1, 26)) - (checked | CONCEPTUAL))
assert not (checked & CONCEPTUAL)
assert len(QUESTIONS) == 25
for k, q in enumerate(QUESTIONS, 1):
    assert len(q["choices"]) == 4 and len(set(q["choices"])) == 4, f"q{k}: choices"
    assert 0 <= q["ans"] < 4, f"q{k}: ans"
print(f"c6_7: {len(checked)} computational questions verified, "
      f"{len(CONCEPTUAL)} conceptual; all 25 checked for shape.")
