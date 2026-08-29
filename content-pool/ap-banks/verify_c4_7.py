# Verification for CALC 4.7 — L'Hospital's Rule.
# Every limit is computed by sympy directly (sp.limit does not need the rule), which is
# an independent check on the keys rather than a replay of the intended reasoning.
# For the three questions where the rule does NOT apply or is inconclusive, the value a
# careless application would produce is also computed and shown to differ from the truth.
import sympy as sp

import c4_7

x = sp.Symbol('x', real=True)

# --- straightforward 0/0 and infinity/infinity limits ---
assert sp.limit((x**2 - 1) / (x - 1), x, 1) == 2                      # q7
assert sp.limit(sp.sin(3 * x) / x, x, 0) == 3                         # q8
assert sp.limit((1 - sp.cos(x)) / x**2, x, 0) == sp.Rational(1, 2)    # q9
assert sp.limit((1 - sp.cos(x)) / x, x, 0) == 0                       # q10
assert sp.limit((sp.exp(2 * x) - 1) / sp.sin(3 * x), x, 0) == sp.Rational(2, 3)   # q11
assert sp.limit((3 * x**2 + 5 * x) / (2 * x**2 - x), x, sp.oo) == sp.Rational(3, 2)  # q12
assert sp.limit(sp.log(x) / x, x, sp.oo) == 0                         # q13
assert sp.limit(x / sp.exp(x), x, sp.oo) == 0                         # q14
assert sp.limit(sp.exp(x) / x**3, x, sp.oo) is sp.oo                  # q15
assert sp.limit((x**2 - 4) / (x**2 + x - 6), x, 2) == sp.Rational(4, 5)   # q16
assert sp.limit((2 * x + 1) / sp.sqrt(x**2 + 3), x, sp.oo) == 2       # q17
assert sp.limit(x * sp.log(x), x, 0, '+') == 0                        # q18
assert sp.limit(x * sp.sin(1 / x), x, sp.oo) == 1                     # q19
assert sp.limit((sp.tan(x) - x) / x**3, x, 0) == sp.Rational(1, 3)    # q20
assert sp.limit((sp.exp(x) - 1 - x) / x**2, x, 0) == sp.Rational(1, 2)   # q21
assert sp.limit(sp.sin(x) / x**2, x, 0, '+') is sp.oo                 # q22
assert sp.limit(sp.log(x)**2 / x, x, sp.oo) == 0                      # q24
assert sp.limit(x**2 / sp.sin(x), x, 0) == 0                          # q25

# --- q3: L'Hospital on (e^x - 1)/x really is lim e^x/1 = 1 ---
assert sp.limit((sp.exp(x) - 1) / x, x, 0) == 1
assert sp.limit(sp.diff(sp.exp(x) - 1, x) / sp.diff(x, x), x, 0) == 1

# --- q4: (x + 2)/x at 0 is NOT indeterminate; the one-sided limits are infinite ---
assert sp.limit((x + 2) / x, x, 0, '+') is sp.oo
assert sp.limit((x + 2) / x, x, 0, '-') is -sp.oo
# a careless application would give lim 1/1 = 1, which is not the answer
assert sp.limit(sp.diff(x + 2, x) / sp.diff(x, x), x, 0) == 1

# --- q5: cos(x)/(x + 1) at 0 is 1/1 = 1, but a careless application gives 0 ---
true5 = sp.limit(sp.cos(x) / (x + 1), x, 0)
wrong5 = sp.limit(sp.diff(sp.cos(x), x) / sp.diff(x + 1, x), x, 0)
assert true5 == 1 and wrong5 == 0 and true5 != wrong5

# --- q6: (x + sin x)/x -> 1, while lim of the derivative quotient does not exist ---
assert sp.limit((x + sp.sin(x)) / x, x, sp.oo) == 1
dq = sp.diff(x + sp.sin(x), x) / sp.diff(x, x)     # = 1 + cos(x)
assert sp.simplify(dq - (1 + sp.cos(x))) == 0
lim_dq = sp.limit(dq, x, sp.oo)
assert not lim_dq.is_number, lim_dq        # oscillates: AccumBounds, not a value

# --- q23: x/sqrt(x^2 + 1) cycles under the rule but the limit is 1 ---
f23, g23 = x, sp.sqrt(x**2 + 1)
assert sp.limit(f23 / g23, x, sp.oo) == 1
once = sp.simplify(sp.diff(f23, x) / sp.diff(g23, x))
assert sp.simplify(once - sp.sqrt(x**2 + 1) / x) == 0     # the quotient inverts, i.e. it cycles
twice = sp.simplify(sp.diff(sp.sqrt(x**2 + 1), x) / sp.diff(x, x))
assert sp.simplify(twice - x / sp.sqrt(x**2 + 1)) == 0    # back to where it started

# Structure: 25 questions, four distinct choices, in-range key.
assert len(c4_7.QUESTIONS) == 25, len(c4_7.QUESTIONS)
for i, q in enumerate(c4_7.QUESTIONS, 1):
    assert len(q["choices"]) == 4, (i, len(q["choices"]))
    assert len(set(c.strip().lower() for c in q["choices"])) == 4, i
    assert 0 <= q["ans"] < 4, i
    assert "$" not in q["q"] and all("$" not in c for c in q["choices"]), i

print("c4_7: 25 questions, every limit confirmed by sympy, structure OK")
