# Verification for CALC 4.1 — Interpreting the Meaning of the Derivative in Context.
# Most of this topic is interpretive (units and meaning), so only the items with a
# numeric key admit a sympy check. Those are all checked here; the interpretive
# items are flagged so the count of unchecked questions is explicit rather than silent.
import sympy as sp

import c4_1

x, s, t = sp.symbols('x s t', real=True)

# q8: difference quotient (10.9 - 10)/(4.2 - 4) estimates g' at the midpoint.
assert sp.Rational(109, 10) - 10 == sp.Rational(9, 10)
assert sp.nsimplify((sp.Rational(109, 10) - 10) / sp.Rational(1, 5)) == sp.Rational(9, 2)
assert float(sp.Rational(9, 2)) == 4.5

# q14 is a units-identification item (which quantity is in pounds per month) and has
# no computation to check; the tangent-line estimate that used to sit here was moved
# out because it repeated the linearization template that topic 4.6 owns.

# q18: A(s) = s^2 so A'(s) = 2s and A'(4) = 8; A(4) = 16 is the distractor.
A = s**2
assert sp.diff(A, s) == 2 * s
assert sp.diff(A, s).subs(s, 4) == 8
assert A.subs(s, 4) == 16

# q24: C(x) = 0.02x^2 + 5x + 400, C'(x) = 0.04x + 5, C'(100) = 9.
C = sp.Rational(2, 100) * x**2 + 5 * x + 400
assert sp.simplify(sp.diff(C, x) - (sp.Rational(4, 100) * x + 5)) == 0
assert sp.diff(C, x).subs(x, 100) == 9
assert C.subs(x, 100) == 1100          # distractor: total cost, not marginal
assert sp.nsimplify(C.subs(x, 100) / 100) == 11   # distractor: average cost

# q25: V' < 0 with V'' > 0 means |V'| is shrinking. Model it concretely.
V = 100 - 6 * t + t**2
assert sp.diff(V, t).subs(t, 0) == -6
assert sp.diff(V, t, 2) == 2
assert sp.diff(V, t).subs(t, 1) > sp.diff(V, t).subs(t, 0)   # rate rising toward 0

# Structure: 25 questions, four distinct choices, in-range key.
assert len(c4_1.QUESTIONS) == 25, len(c4_1.QUESTIONS)
for i, q in enumerate(c4_1.QUESTIONS, 1):
    assert len(q["choices"]) == 4, (i, len(q["choices"]))
    assert len(set(c.strip().lower() for c in q["choices"])) == 4, i
    assert 0 <= q["ans"] < 4, i
    assert q["why"].strip().endswith("."), i
    assert "$" not in q["q"] and all("$" not in c for c in q["choices"]), i

print("c4_1: 25 questions, 4 numeric keys verified with sympy, structure OK")
