"""sympy verification for CALC 6.6 Applying Properties of Definite Integrals.

A question that only supplies the values of some integrals is checked by
building an explicit function whose integrals really are those values (a step
function is enough) and then letting sp.integrate evaluate the integral the
question asks for.  That way the property being tested is exercised on a real
function instead of being restated as arithmetic.

CONCEPTUAL questions -- no computation, reasoning stated here:
 12  the comparison property: f <= g on [a, b] with a < b gives
     int f <= int g, since int (g - f) is the integral of a non-negative
     function over an interval traversed left to right
 18  there is no product rule for integrals; the other three statements are
     the sum, constant-multiple, and additivity properties
"""
import sympy as sp

from c6_6 import QUESTIONS

x, a, b = sp.symbols('x a b', real=True)
f = sp.Function('f')

CONCEPTUAL = {12, 18}
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


def step(*pieces):
    """step((value, upper), ..., (value, None)) as a sympy Piecewise in x."""
    args = [(v, x < u) for v, u in pieces[:-1]] + [(pieces[-1][0], True)]
    return sp.Piecewise(*args)


# 1: zero-width interval, for an unspecified continuous integrand
assert sp.Integral(f(x), (x, a, a)).doit() == 0
chk(1, sp.Integer(0), [0, None, a, None])

# 2: reversing the limits negates, tested on real integrands
for g_, lo, hi in [(x**2, 1, 4), (sp.sin(x), 0, sp.pi), (sp.exp(x), -1, 2)]:
    assert sp.simplify(sp.integrate(g_, (x, hi, lo)) + sp.integrate(g_, (x, lo, hi))) == 0
key_is(2, "-int from a to b of f(x) dx")

# 3, 4: additivity over adjacent intervals
f34 = step((sp.Rational(8, 5), 5), (sp.Rational(3, 4), None))
assert sp.integrate(f34, (x, 0, 5)) == 8 and sp.integrate(f34, (x, 5, 9)) == 3
chk(3, sp.integrate(f34, (x, 0, 9)), [5, 11, 24, None])
assert sp.integrate(f34, (x, 0, 9)) == 11
chk(4, sp.integrate(f34, (x, 5, 9)), [-3, 3, 19, 88])

# 5: reversed limits
f5 = sp.Integer(2)
assert sp.integrate(f5, (x, 1, 4)) == 6
chk(5, sp.integrate(f5, (x, 4, 1)), [-6, 0, 6, sp.Rational(1, 6)])

# 6: constant multiple
f6 = sp.Rational(5, 4)
assert sp.integrate(f6, (x, 2, 6)) == 5
chk(6, sp.integrate(3 * f6, (x, 2, 6)), [sp.Rational(5, 3), 8, 15, 20])

# 7, 8: linearity with two functions
f7, g7 = sp.Rational(7, 4), sp.Rational(-1, 2)
assert sp.integrate(f7, (x, 0, 4)) == 7 and sp.integrate(g7, (x, 0, 4)) == -2
chk(7, sp.integrate(f7 + g7, (x, 0, 4)), [-14, 5, 9, None])
chk(8, sp.integrate(2 * f7 - 3 * g7, (x, 0, 4)), [8, 11, 20, -42])

# 9: integral of a constant
chk(9, sp.integrate(4, (x, 1, 5)), [4, 9, 16, 20])

# 10: adding a constant to the integrand
f10 = sp.Integer(3)
assert sp.integrate(f10, (x, 2, 5)) == 9
chk(10, sp.integrate(f10 + 2, (x, 2, 5)), [11, 13, 15, 18])

# 11: a negative piece recovered by subtraction
f11 = step((sp.Rational(5, 3), 3), (sp.Rational(-3, 4), None))
assert sp.integrate(f11, (x, 0, 3)) == 5 and sp.integrate(f11, (x, 0, 7)) == 2
chk(11, sp.integrate(f11, (x, 3, 7)), [-3, 3, 7, 10])

# 13: f >= 0 gives a non-negative integral, but not a strictly positive one
assert sp.integrate(sp.Integer(0), (x, 0, 4)) == 0      # kills "strictly positive"
assert sp.integrate(x**2, (x, 0, 4)) > 0
key_is(13, "is greater than or equal to 0")

# 14: odd integrand over a symmetric interval
chk(14, sp.integrate(x**3, (x, -2, 2)), [-8, 0, 4, 8])

# 15: even integrand over a symmetric interval
for even, A in [(x**2, 2), (sp.cos(x), 1), (sp.Abs(x), 3)]:
    k = sp.integrate(even, (x, 0, A))
    assert sp.simplify(sp.integrate(even, (x, -A, A)) - 2 * k) == 0
key_is(15, "2k")

# 16: bounding the integrand bounds the integral, and the bounds are attained
lo16 = sp.integrate(sp.Integer(2), (x, 1, 7))
hi16 = sp.integrate(sp.Integer(5), (x, 1, 7))
assert (lo16, hi16) == (12, 30)
mid16 = sp.integrate(2 + 3 * (x - 1) / 6, (x, 1, 7))
assert lo16 <= mid16 <= hi16
key_is(16, "12 <= I <= 30")

# 17: dividing the integrand by 2
f17 = sp.Rational(10, 6)
assert sp.integrate(f17, (x, 0, 6)) == 10
chk(17, sp.integrate(f17 / 2, (x, 0, 6)), [2, 5, 10, 20])

# 19: additivity then reversal
f19 = step((2, 3), (sp.Rational(6, 5), None))
assert sp.integrate(f19, (x, 1, 3)) == 4 and sp.integrate(f19, (x, 3, 8)) == 6
chk(19, sp.integrate(f19, (x, 8, 1)), [-10, -2, 2, 10])

# 20: equal limits with a nontrivial integrand
chk(20, sp.integrate(x**3 + 2 * x, (x, 5, 5)), [0, 135, 150, 175])

# 21: subtraction then reversal
f21 = step((sp.Rational(3, 2), 2), (1, None))
assert sp.integrate(f21, (x, 0, 2)) == 3 and sp.integrate(f21, (x, 0, 6)) == 7
chk(21, sp.integrate(f21, (x, 6, 2)), [-10, -4, 4, 10])

# 22: odd term vanishes, constant term does not
chk(22, sp.integrate(x**3 + 4, (x, -3, 3)), [0, 12, 24, 51])

# 23: linearity with a constant term
f23 = sp.Rational(5, 3)
assert sp.integrate(f23, (x, 1, 4)) == 5
chk(23, sp.integrate(2 * f23 - 1, (x, 1, 4)), [4, 7, 9, 10])

# 24: two pairs with the same separate integrals but different int f*g,
#     while the other three choices agree across the pair
fA, gA = sp.Rational(9, 4), sp.Integer(1)
fB, gB = step((sp.Rational(9, 2), 2), (0, None)), step((0, 2), (2, None))
for u, v in [(fA, gA), (fB, gB)]:
    assert sp.integrate(u, (x, 0, 4)) == 9 and sp.integrate(v, (x, 0, 4)) == 4
    assert sp.integrate(u - v, (x, 0, 4)) == 5
    assert sp.integrate(5 * u, (x, 0, 4)) == 45
    assert sp.integrate(v, (x, 4, 0)) == -4
assert sp.integrate(fA * gA, (x, 0, 4)) == 9 and sp.integrate(fB * gB, (x, 0, 4)) == 0
key_is(24, "int from 0 to 4 of f(x) g(x) dx")

# 25: 0 <= f <= 3 on [0, 4] caps the integral at 12; 0, 5, and 12 are attainable
assert sp.integrate(sp.Integer(0), (x, 0, 4)) == 0
assert sp.integrate(sp.Rational(5, 4), (x, 0, 4)) == 5
assert sp.integrate(sp.Integer(3), (x, 0, 4)) == 12
assert 15 > 12
key_is(25, "15")

assert checked | CONCEPTUAL == set(range(1, 26)), sorted(set(range(1, 26)) - (checked | CONCEPTUAL))
assert not (checked & CONCEPTUAL)
assert len(QUESTIONS) == 25
for k, q in enumerate(QUESTIONS, 1):
    assert len(q["choices"]) == 4 and len(set(q["choices"])) == 4, f"q{k}: choices"
    assert 0 <= q["ans"] < 4, f"q{k}: ans"
print(f"c6_6: {len(checked)} computational questions verified, "
      f"{len(CONCEPTUAL)} conceptual; all 25 checked for shape.")
