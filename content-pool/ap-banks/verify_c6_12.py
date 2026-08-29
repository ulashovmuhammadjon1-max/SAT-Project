"""sympy verification for CALC 6.12 Integrating Using Linear Partial Fractions.

Decompositions are reproduced with sp.apart and compared to the keyed choice;
antiderivatives are checked by differentiating back to the integrand (never by
comparing expressions, since correct antiderivatives differ by a constant);
definite integrals are evaluated with sp.integrate.

CONCEPTUAL questions -- no computation, reasoning stated here:
  6  only a proper fraction may be decomposed; an improper one is divided first
 18  the method covers a proper fraction whose denominator splits into distinct
     linear factors
 22  x^3/(x^2 - 1) is improper, so long division comes first (the division
     itself is still checked below)
"""
import sympy as sp

from c6_12 import QUESTIONS

x = sp.Symbol('x', real=True)

CONCEPTUAL = {6, 18, 22}
checked = set()

SAMPLES = (sp.Rational(1, 5), sp.Rational(7, 10), sp.Rational(23, 10),
           sp.Rational(37, 10), sp.Rational(-13, 10))


def is_zero(e, var=x):
    if sp.simplify(e) == 0:
        return True
    vals = []
    for v in SAMPLES:
        try:
            val = complex(sp.N(e.subs(var, v)))
        except TypeError:
            continue
        if val != val:
            continue
        vals.append(abs(val))
    return bool(vals) and max(vals) < 1e-10


def anti(i, integrand, exprs):
    q = QUESTIONS[i - 1]
    assert len(exprs) == len(q["choices"]), f"q{i}: wrong number of expressions"
    key = exprs[q["ans"]]
    assert is_zero(sp.diff(key, x) - integrand), f"q{i}: key is not an antiderivative"
    for j, e in enumerate(exprs):
        if e is None or j == q["ans"]:
            continue
        assert not is_zero(sp.diff(e, x) - integrand), f"q{i}: distractor {j} also works"
    checked.add(i)


def value(i, computed, values):
    q = QUESTIONS[i - 1]
    for p in range(len(values)):
        for r in range(p + 1, len(values)):
            assert sp.simplify(values[p] - values[r]) != 0, f"q{i}: choices {p},{r} equal"
    assert sp.simplify(computed - values[q["ans"]]) == 0, f"q{i}: key mismatch"
    checked.add(i)


def key_is(i, text):
    q = QUESTIONS[i - 1]
    assert q["choices"][q["ans"]] == text, f"q{i}: key is {q['choices'][q['ans']]!r}"
    checked.add(i)


L = lambda e: sp.log(sp.Abs(e))
R = sp.Rational

# 1: the decomposition itself, from sp.apart
d1 = sp.apart(1 / ((x - 1) * (x + 2)), x)
assert sp.simplify(d1 - (R(1, 3) / (x - 1) - R(1, 3) / (x + 2))) == 0
value(1, d1, [R(1, 3) / (x - 1) - R(1, 3) / (x + 2),
              R(1, 3) / (x - 1) + R(1, 3) / (x + 2),
              1 / (x - 1) - 1 / (x + 2),
              R(1, 2) / (x - 1) - R(1, 2) / (x + 2)])

anti(2, 1 / ((x - 1) * (x + 2)),
     [L(x - 1) / 3 - L(x + 2) / 3, L(x - 1) / 3 + L(x + 2) / 3,
      L((x - 1) * (x + 2)), L((x - 1) * (x + 2)) / 3])

d3 = sp.apart(5 / ((x - 3) * (x + 2)), x)
value(3, d3, [1 / (x - 3) - 1 / (x + 2), 1 / (x - 3) + 1 / (x + 2),
              5 / (x - 3) - 5 / (x + 2), R(1, 5) / (x - 3) - R(1, 5) / (x + 2)])

anti(4, 1 / (x**2 - 1),
     [L(x - 1) / 2 - L(x + 1) / 2, L(x - 1) / 2 + L(x + 1) / 2,
      L(x**2 - 1), sp.atan(x)])
anti(5, (x + 7) / ((x - 1) * (x + 3)),
     [2 * L(x - 1) - L(x + 3), L(x - 1) - 2 * L(x + 3),
      2 * L(x - 1) + L(x + 3), L((x - 1) * (x + 3))])

# 7: the setup -- sp.apart really does produce one constant over each factor
d7 = sp.apart(3 * x / ((x - 2) * (x + 5)), x)
assert d7 == R(6, 7) / (x - 2) + R(15, 7) / (x + 5)
key_is(7, "A/(x - 2) + B/(x + 5)")

anti(8, 1 / (x * (x + 1)), [L(x) - L(x + 1), L(x) + L(x + 1),
                            L(x * (x + 1)), -1 / (x * (x + 1))])
anti(9, 1 / (x**2 - 4),
     [L(x - 2) / 4 - L(x + 2) / 4, L(x - 2) / 4 + L(x + 2) / 4,
      L(x - 2) / 2 - L(x + 2) / 2, sp.atan(x / 2) / 2])

value(10, sp.simplify(sp.integrate(1 / (x * (x - 1)), (x, 2, 3))),
      [sp.log(R(4, 3)), sp.log(R(3, 2)), sp.log(2), sp.log(R(3, 4))])

anti(11, (3 * x + 11) / ((x - 3) * (x + 2)),
     [4 * L(x - 3) - L(x + 2), L(x - 3) - 4 * L(x + 2),
      4 * L(x - 3) + L(x + 2), 3 * L((x - 3) * (x + 2))])
anti(12, 1 / (x * (1 - x)), [L(x) - L(1 - x), L(x) + L(1 - x),
                             -L(x * (1 - x)), L(1 - x) - L(x)])

value(13, sp.simplify(sp.integrate(1 / ((x + 1) * (x + 2)), (x, 0, 1))),
      [sp.log(R(4, 3)), sp.log(R(3, 2)), sp.log(R(2, 3)), sp.log(2)])

# 14: improper, so divide first
quot, rem = sp.div(sp.Poly(x**2, x), sp.Poly(x**2 - 1, x))
assert quot.as_expr() == 1 and rem.as_expr() == 1
anti(14, x**2 / (x**2 - 1),
     [x + L(x - 1) / 2 - L(x + 1) / 2, L(x - 1) / 2 - L(x + 1) / 2,
      x + L(x**2 - 1), x - L(x - 1) / 2 + L(x + 1) / 2])

anti(15, 4 * x / (x**2 - 4),
     [2 * L(x - 2) + 2 * L(x + 2), 2 * L(x - 2) - 2 * L(x + 2),
      4 * L(x**2 - 4), L(x - 2) + L(x + 2)])

# 16: the coefficient A
A16 = sp.apart((2 * x + 3) / ((x + 1) * (x - 4)), x).coeff(1 / (x + 1))
assert sp.simplify(A16 - R(-1, 5)) == 0
value(16, A16, [R(-1, 5), R(1, 5), R(11, 5), R(-11, 5)])

anti(17, 6 / ((x - 1) * (x + 5)),
     [L(x - 1) - L(x + 5), L(x - 1) + L(x + 5),
      6 * L(x - 1) - 6 * L(x + 5), L(sp.Abs((x - 1) / (x + 5))) / 6])

value(19, sp.simplify(sp.integrate(1 / (x**2 - 4), (x, 3, 4))),
      [sp.log(R(5, 3)) / 4, sp.log(R(3, 5)) / 4, sp.log(R(5, 3)) / 2,
       sp.log(R(5, 3))])

assert sp.factor(x**2 - x - 6) == (x - 3) * (x + 2)
anti(20, (x + 1) / (x**2 - x - 6),
     [4 * L(x - 3) / 5 + L(x + 2) / 5, L(x - 3) / 5 + 4 * L(x + 2) / 5,
      4 * L(x - 3) / 5 - L(x + 2) / 5, L(x**2 - x - 6)])
anti(21, 2 / (x**2 + x),
     [2 * L(x) - 2 * L(x + 1), 2 * L(x) + 2 * L(x + 1),
      L(x) - L(x + 1), 2 * L(x**2 + x)])

# 22: the division that must come first
q22, r22 = sp.div(sp.Poly(x**3, x), sp.Poly(x**2 - 1, x))
assert q22.as_expr() == x and r22.as_expr() == x

value(23, sp.simplify(sp.integrate(1 / (x * (x + 2)), (x, 1, 2))),
      [sp.log(R(3, 2)) / 2, sp.log(R(2, 3)) / 2, sp.log(R(3, 2)),
       sp.log(R(4, 3)) / 2])

d24 = sp.apart(7 / ((x - 2) * (x + 5)), x)
assert sp.simplify(d24 - (1 / (x - 2) - 1 / (x + 5))) == 0
key_is(24, "A = 1 and B = -1")

anti(25, (5 * x - 2) / (x**2 - 4),
     [2 * L(x - 2) + 3 * L(x + 2), 3 * L(x - 2) + 2 * L(x + 2),
      2 * L(x - 2) - 3 * L(x + 2),
      5 * L(x**2 - 4) - 2 * sp.atan(x / 2)])

assert checked | CONCEPTUAL == set(range(1, 26)), sorted(set(range(1, 26)) - (checked | CONCEPTUAL))
assert not (checked & CONCEPTUAL)
assert len(QUESTIONS) == 25
for k, q in enumerate(QUESTIONS, 1):
    assert len(q["choices"]) == 4 and len(set(q["choices"])) == 4, f"q{k}: choices"
    assert 0 <= q["ans"] < 4, f"q{k}: ans"
print(f"c6_12: {len(checked)} computational questions verified, "
      f"{len(CONCEPTUAL)} conceptual; all 25 checked for shape.")
