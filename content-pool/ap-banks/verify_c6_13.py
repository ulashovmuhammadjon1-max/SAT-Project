"""sympy verification for CALC 6.13 Evaluating Improper Integrals.

Every improper integral is evaluated the way the topic demands: integrate over
a finite interval whose endpoint is a symbol, then take the limit with
sp.limit.  Divergence is established the same way -- the limit is +-infinity --
rather than by trusting a single sp.integrate call on an infinite interval.
Where sympy can also do the improper integral directly, the two answers are
cross-checked against each other.

CONCEPTUAL questions -- no computation, reasoning stated here:
  1  the limit definition of an integral over an infinite interval
 11  infinity cannot be substituted into an antiderivative; the limit is what
     gives the symbol meaning
 17  improper means an infinite interval or an unbounded integrand
 23  the comparison test: bounded and increasing accumulation converges
"""
import sympy as sp

from c6_13 import QUESTIONS

x = sp.Symbol('x', positive=True)
b = sp.Symbol('b', positive=True)
a = sp.Symbol('a', positive=True)

CONCEPTUAL = {1, 11, 17, 23}
checked = set()
DIVERGES = object()


def tail(f, lo, var=x):
    """lim as b -> infinity of int from lo to b."""
    return sp.limit(sp.integrate(f, (var, lo, b)), b, sp.oo)


def head(f, hi, var=x):
    """lim as a -> 0+ of int from a to hi (an unbounded integrand at 0)."""
    return sp.limit(sp.integrate(f, (var, a, hi)), a, 0, '+')


def value(i, computed, values):
    """values: the number in each choice, in module order; DIVERGES for the
    'the integral diverges' choice."""
    q = QUESTIONS[i - 1]
    assert len(values) == len(q["choices"]), f"q{i}: wrong number of values"
    nums = [v for v in values if v is not DIVERGES and v is not None]
    for p in range(len(nums)):
        for r in range(p + 1, len(nums)):
            assert sp.simplify(nums[p] - nums[r]) != 0, f"q{i}: two choices are equal"
    key = values[q["ans"]]
    if key is DIVERGES:
        assert computed in (sp.oo, -sp.oo) or computed.has(sp.oo), \
            f"q{i}: keyed as divergent but sympy found {computed}"
    else:
        assert computed not in (sp.oo, -sp.oo), f"q{i}: diverges, but a number is keyed"
        assert sp.simplify(computed - key) == 0, f"q{i}: key mismatch, value is {computed}"
    checked.add(i)


def key_is(i, text):
    q = QUESTIONS[i - 1]
    assert q["choices"][q["ans"]] == text, f"q{i}: key is {q['choices'][q['ans']]!r}"
    checked.add(i)


D = DIVERGES
R = sp.Rational
E = sp.E

# --- infinite intervals ----------------------------------------------------
v2 = tail(1 / x**2, 1)
assert v2 == sp.integrate(1 / x**2, (x, 1, sp.oo))
value(2, v2, [1, R(1, 2), 2, D])

v3 = tail(1 / x, 1)
assert v3 is sp.oo
value(3, v3, [D, 0, 1, sp.log(2)])

value(4, tail(1 / x**3, 1), [R(1, 2), R(1, 3), 1, D])

# 5: the p-test, checked on both sides of p = 1
for p in (R(3, 2), 2, 5):
    assert tail(x**(-p), 1).is_finite
for p in (R(1, 2), 1):
    assert tail(x**(-p), 1) is sp.oo
key_is(5, "p > 1")

v8 = tail(sp.exp(-x), 0)
assert v8 == sp.integrate(sp.exp(-x), (x, 0, sp.oo))
value(8, v8, [1, 0, E, D])
value(9, tail(sp.exp(-2 * x), 0), [R(1, 2), 1, 2, D])

# 10: the lower limit runs to -infinity
c = sp.Symbol('c', negative=True)
v10 = sp.limit(sp.integrate(sp.exp(x), (x, c, 0)), c, -sp.oo)
value(10, v10, [1, 0, -1, D])

value(12, tail(1 / sp.sqrt(x), 1), [D, 2, 1, R(1, 2)])
value(13, tail(1 / x**4, 2), [R(1, 24), R(1, 12), R(1, 3), D])

# 15, 16: arctangent tails
v16 = tail(1 / (1 + x**2), 0)
assert v16 == sp.pi / 2
value(16, v16, [sp.pi / 2, sp.pi, 1, D])
v15 = v16 + sp.limit(sp.integrate(1 / (1 + x**2), (x, c, 0)), c, -sp.oo)
assert v15 == sp.integrate(1 / (1 + x**2), (x, -sp.oo, sp.oo))
value(15, v15, [sp.pi, sp.pi / 2, 2 * sp.pi, D])

u = sp.Symbol('u', positive=True)
v18 = tail(1 / (x * sp.log(x)**2), E)
assert v18 == tail(1 / u**2, 1, var=u)          # the substitution u = ln x
value(18, v18, [1, R(1, 2), E, D])

value(21, tail(x * sp.exp(-x**2), 1), [1 / (2 * E), 1 / E, 2 / E, D])
value(22, tail(x**R(-3, 2), 1), [2, 1, R(3, 2), D])
value(24, tail(x * sp.exp(-x), 0), [1, 0, R(1, 2), D])

# --- unbounded integrands --------------------------------------------------
v6 = head(1 / sp.sqrt(x), 1)
assert v6 == sp.integrate(1 / sp.sqrt(x), (x, 0, 1))
value(6, v6, [2, 1, R(1, 2), D])

v7 = head(1 / x, 1)
assert v7 is sp.oo
value(7, v7, [D, 0, 1, -1])

v14 = head(1 / x**2, 1)
assert v14 is sp.oo
value(14, v14, [D, 1, -1, 2])

# 19: the discontinuity sits inside [0, 3]; the left piece alone diverges
s = sp.Symbol('s', positive=True)
left19 = sp.limit(sp.integrate(1 / (x - 1)**2, (x, 0, 1 - s)), s, 0, '+')
assert left19 is sp.oo
naive19 = (-1 / (x - 1)).subs(x, 3) - (-1 / (x - 1)).subs(x, 0)
assert naive19 == R(-3, 2)                      # the tidy wrong answer
value(19, left19, [D, R(-3, 2), R(3, 2), R(1, 2)])

v20 = head(sp.log(x), 1)
assert v20 == sp.integrate(sp.log(x), (x, 0, 1))
value(20, v20, [-1, 1, 0, D])

# 25: both halves of int from -1 to 1 of 1/x dx diverge -- to +infinity on the
# right of 0 and to -infinity on its left, so they cannot cancel
w = sp.Symbol('w', real=True)
neg = sp.Symbol('neg', negative=True)
right25 = sp.limit(sp.integrate(1 / w, (w, s, 1)), s, 0, '+')
left25 = sp.limit(sp.integrate(1 / w, (w, -1, neg)), neg, 0, '-')
assert right25 is sp.oo and left25 is -sp.oo
key_is(25, "The integrand is unbounded at x = 0, so the integral must be split there, and each piece diverges")

assert checked | CONCEPTUAL == set(range(1, 26)), sorted(set(range(1, 26)) - (checked | CONCEPTUAL))
assert not (checked & CONCEPTUAL)
assert len(QUESTIONS) == 25
for k, q in enumerate(QUESTIONS, 1):
    assert len(q["choices"]) == 4 and len(set(q["choices"])) == 4, f"q{k}: choices"
    assert 0 <= q["ans"] < 4, f"q{k}: ans"
print(f"c6_13: {len(checked)} computational questions verified, "
      f"{len(CONCEPTUAL)} conceptual; all 25 checked for shape.")
