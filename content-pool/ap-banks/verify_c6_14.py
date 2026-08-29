"""sympy verification for CALC 6.14 Selecting Techniques for Antidifferentiation.

Computational answers are checked by differentiating the keyed antiderivative
back to the integrand and confirming that no distractor does the same.  Each
"which technique" question is checked by actually performing the named
technique -- the substitution, the by-parts formula, sp.apart, or sp.div -- and
confirming it produces an antiderivative of the integrand, so the key is
justified by a computation rather than by an assertion about method.

CONCEPTUAL question -- no computation:
 24  in int x e^x dx neither factor is the derivative of the inside of the
     other, which is what rules substitution out; the other three integrands
     are checked below to be substitution cases
"""
import sympy as sp

from c6_14 import QUESTIONS

x = sp.Symbol('x', positive=True)
u = sp.Symbol('u', positive=True)

CONCEPTUAL = {24}
checked = set()

SAMPLES = (sp.Rational(1, 5), sp.Rational(4, 5), sp.Rational(13, 10), sp.Rational(23, 10))


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


def is_sub_form(integrand, u_of_x, h):
    """True when integrand = h(u(x)) * u'(x) -- the exact shape a substitution
    needs.  An earlier version of this helper asked only whether the quotient
    integrand/u'(x) could be rewritten without x, which is true for almost any
    invertible u and so accepted everything; a checker that over-matches is
    worse than no checker."""
    return is_zero(sp.simplify(integrand - h(u_of_x) * sp.diff(u_of_x, x)))


L = lambda e: sp.log(sp.Abs(e))
R = sp.Rational
E = sp.E

# --- 1-6: choosing the technique, each justified by carrying it out ---------
# 1: x cos(x^2) = h(u) u' with u = x^2 and h(U) = cos(U)/2
assert is_sub_form(x * sp.cos(x**2), x**2, lambda U: sp.cos(U) / 2)
assert is_zero(sp.diff(sp.sin(x**2) / 2, x) - x * sp.cos(x**2))
key_is(1, "substitution with u = x^2")

# 2: parts with u = x reproduces the antiderivative, and x cos(x) is not of
# the form h(cos x) * (cos x)' -- the sine that substitution would need is absent
v2 = sp.integrate(sp.cos(x), x)
by2 = x * v2 - sp.integrate(v2 * sp.diff(x, x), x)
assert is_zero(sp.diff(by2, x) - x * sp.cos(x))
assert not is_sub_form(x * sp.cos(x), sp.cos(x), lambda U: U)
assert not is_sub_form(x * sp.cos(x), sp.cos(x), lambda U: -U)
key_is(2, "integration by parts with u = x")

# 3: the denominator factors, so sp.apart gives two linear pieces
d3 = sp.apart((x + 2) / (x**2 - 9), x)
assert sp.factor(x**2 - 9) == (x - 3) * (x + 3) and len(d3.args) == 2
key_is(3, "partial fractions, since the denominator factors as (x - 3)(x + 3)")

# 4: improper, so long division comes first
q4, r4 = sp.div(sp.Poly(x**2 + 3, x), sp.Poly(x + 1, x))
assert q4.as_expr() == x - 1 and r4.as_expr() == 4
key_is(4, "long division, since the numerator has the higher degree")

# 5: the denominator is irreducible, and completing the square gives arctan
assert sp.discriminant(x**2 + 6 * x + 10, x) < 0
assert sp.expand((x + 3)**2 + 1 - (x**2 + 6 * x + 10)) == 0
assert is_zero(sp.diff(sp.atan(x + 3), x) - 1 / (x**2 + 6 * x + 10))
key_is(5, "completing the square, since the denominator has no real roots")

# 6: the numerator is the derivative of the denominator
assert sp.simplify(sp.diff(x**2 + 1, x) - 2 * x) == 0
assert is_zero(sp.diff(sp.log(x**2 + 1), x) - 2 * x / (x**2 + 1))
key_is(6, "substitution with u = x^2 + 1")

# --- computations ----------------------------------------------------------
anti(7, x**2 * sp.sin(x**3),
     [-sp.cos(x**3) / 3, sp.cos(x**3) / 3, -sp.cos(x**3), -x**3 * sp.cos(x**3) / 3])
anti(8, x**2 * sp.sin(x),
     [-x**2 * sp.cos(x) + 2 * x * sp.sin(x) + 2 * sp.cos(x),
      -x**2 * sp.cos(x) + 2 * x * sp.sin(x) - 2 * sp.cos(x),
      -x**2 * sp.cos(x) - 2 * x * sp.sin(x) - 2 * sp.cos(x),
      -sp.cos(x**3) / 3])
anti(9, (x**3 - 1) / x**2,
     [x**2 / 2 + 1 / x, x**2 / 2 - 1 / x, x**2 / 2 - L(x), None])
anti(10, 1 / (x**2 + 9),
     [sp.atan(x / 3) / 3, sp.atan(x / 3), sp.atan(x / 3) / 9,
      sp.log(x**2 + 9) / 3])
anti(11, sp.exp(3 * x + 1),
     [sp.exp(3 * x + 1) / 3, sp.exp(3 * x + 1), 3 * sp.exp(3 * x + 1),
      sp.exp(3 * x + 1) / (3 * x + 1)])
anti(12, sp.sin(x)**3 * sp.cos(x),
     [sp.sin(x)**4 / 4, sp.sin(x)**4, sp.cos(x)**4 / 4, -sp.sin(x)**4 / 4])
anti(13, 1 / (x**2 - 9),
     [L(x - 3) / 6 - L(x + 3) / 6, L(x - 3) / 6 + L(x + 3) / 6,
      sp.atan(x / 3) / 3, L(x**2 - 9) / 6])
anti(14, (2 * x + 3) / (x**2 + 3 * x + 1),
     [L(x**2 + 3 * x + 1), L(x**2 + 3 * x + 1) / 2, 2 * L(x**2 + 3 * x + 1),
      sp.atan(x**2 + 3 * x + 1)])
anti(15, x / (x**2 + 1)**3,
     [-1 / (4 * (x**2 + 1)**2), -1 / (2 * (x**2 + 1)**2),
      1 / (4 * (x**2 + 1)**2), sp.log((x**2 + 1)**3) / 2])
anti(16, sp.sqrt(x) * (x + 1),
     [R(2, 5) * x**R(5, 2) + R(2, 3) * x**R(3, 2),
      R(2, 3) * x**R(3, 2) * (x**2 / 2 + x),
      R(2, 5) * x**R(5, 2) + R(2, 3) * x**R(1, 2),
      R(2, 7) * x**R(7, 2) + R(2, 3) * x**R(3, 2)])
anti(17, sp.log(2 * x),
     [x * sp.log(2 * x) - x, x * sp.log(2 * x) + x, sp.log(2 * x) / x,
      x * sp.log(2 * x) / 2 - x])

# 18: the half-angle identity is the "technique" here
assert sp.simplify(sp.cos(x)**2 - (1 + sp.cos(2 * x)) / 2) == 0
anti(18, sp.cos(x)**2,
     [x / 2 + sp.sin(2 * x) / 4, sp.cos(x)**3 / 3, x / 2 - sp.sin(2 * x) / 4,
      sp.sin(x)**2 / 2])

value(19, sp.simplify(sp.integrate(x / (x + 1), (x, 0, 1))),
      [1 - sp.log(2), 1 + sp.log(2), sp.log(2), R(1, 2)])

anti(20, (3 * x**2 + 2 * x) / (x**3 + x**2),
     [L(x**3 + x**2), L(x**3 + x**2) / 3, 3 * L(x**3 + x**2), L(3 * x**2 + 2 * x)])
anti(21, x / sp.sqrt(x + 4),
     [R(2, 3) * (x + 4)**R(3, 2) - 8 * sp.sqrt(x + 4),
      R(2, 3) * (x + 4)**R(3, 2) + 8 * sp.sqrt(x + 4),
      2 * x * sp.sqrt(x + 4), R(2, 3) * (x + 4)**R(3, 2)])
anti(22, x / (1 + x**4),
     [sp.atan(x**2) / 2, sp.atan(x**2), sp.log(1 + x**4) / 2, sp.atan(x) / 2])

value(23, sp.simplify(sp.integrate(sp.sin(x) * sp.exp(sp.cos(x)), (x, 0, sp.pi / 2))),
      [E - 1, 1 - E, E, 1])

# 24: each rival is exactly h(u(x)) u'(x) for an elementary h, so substitution
# handles it; x e^x has no such shape with either natural inner function
assert is_sub_form(x * sp.exp(x**2), x**2, lambda U: sp.exp(U) / 2)
assert is_sub_form((2 * x + 1) / (x**2 + x), x**2 + x, lambda U: 1 / U)
assert is_sub_form(sp.cos(x) * sp.sin(x), sp.sin(x), lambda U: U)
for h in (lambda U: U, lambda U: sp.log(U), lambda U: 1 / U):
    assert not is_sub_form(x * sp.exp(x), x**2, h)

anti(25, x**2 / (x**3 + 1),
     [L(x**3 + 1) / 3, L(x**3 + 1), 3 * L(x**3 + 1), x**3 / (3 * (x**3 + 1))])

assert checked | CONCEPTUAL == set(range(1, 26)), sorted(set(range(1, 26)) - (checked | CONCEPTUAL))
assert not (checked & CONCEPTUAL)
assert len(QUESTIONS) == 25
for k, q in enumerate(QUESTIONS, 1):
    assert len(q["choices"]) == 4 and len(set(q["choices"])) == 4, f"q{k}: choices"
    assert 0 <= q["ans"] < 4, f"q{k}: ans"
print(f"c6_14: {len(checked)} computational questions verified, "
      f"{len(CONCEPTUAL)} conceptual; all 25 checked for shape.")
