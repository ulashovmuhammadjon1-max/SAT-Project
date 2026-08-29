"""sympy verification for CALC 6.9 Integrating Using Substitution.

Indefinite answers are checked by differentiating the keyed antiderivative back
to the integrand and confirming that no distractor does the same (two correct
antiderivatives differ by a constant, so expressions cannot be compared
directly).

Definite answers are checked TWICE: once in x with sp.integrate, and once in u
with the limits converted through the substitution.  Both must agree with the
key.  That is exactly the step the topic is about, so it is the step the
verifier performs rather than assumes.

CONCEPTUAL question -- no computation:
 14  the limits 0 and 2 are x-values; after u = x^2 + 1 they must become 1 and
     5, or the antiderivative must be written back in x first
"""
import sympy as sp

from c6_9 import QUESTIONS

x, u = sp.symbols('x u', real=True)

CONCEPTUAL = {14}
checked = set()

SAMPLES = (sp.Rational(1, 5), sp.Rational(4, 5), sp.Rational(13, 10), sp.Rational(23, 10))


def is_zero(e, var):
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
    return bool(vals) and max(vals) < 1e-12


def anti(i, integrand, exprs, var=x):
    q = QUESTIONS[i - 1]
    assert len(exprs) == len(q["choices"]), f"q{i}: wrong number of expressions"
    key = exprs[q["ans"]]
    assert is_zero(sp.diff(key, var) - integrand, var), f"q{i}: key is not an antiderivative"
    for j, e in enumerate(exprs):
        if e is None or j == q["ans"]:
            continue
        assert not is_zero(sp.diff(e, var) - integrand, var), f"q{i}: distractor {j} also works"
    checked.add(i)


def definite(i, integrand, lo, hi, values, sub=None):
    """values: the value of each choice in module order.  `sub` = (u_of_x,
    integrand_in_u): the same integral after substitution, evaluated between
    the converted limits, which must give the same number."""
    q = QUESTIONS[i - 1]
    val = sp.simplify(sp.integrate(integrand, (x, lo, hi)))
    if sub is not None:
        u_of_x, integrand_u = sub
        lo_u, hi_u = u_of_x.subs(x, lo), u_of_x.subs(x, hi)
        val_u = sp.simplify(sp.integrate(integrand_u, (u, lo_u, hi_u)))
        assert sp.simplify(val - val_u) == 0, f"q{i}: x and u evaluations disagree"
    assert len(values) == len(q["choices"]), f"q{i}: wrong number of values"
    for p in range(len(values)):
        for r in range(p + 1, len(values)):
            assert sp.simplify(values[p] - values[r]) != 0, f"q{i}: choices {p},{r} equal"
    assert sp.simplify(val - values[q["ans"]]) == 0, f"q{i}: key mismatch, integral is {val}"
    checked.add(i)


def key_is(i, text):
    q = QUESTIONS[i - 1]
    assert q["choices"][q["ans"]] == text, f"q{i}: key is {q['choices'][q['ans']]!r}"
    checked.add(i)


E = sp.E

# ------------------------------------------------------- indefinite ---------
anti(1, 2 * x * (x**2 + 1)**3,
     [(x**2 + 1)**4 / 4, (x**2 + 1)**4 / 8, (x**2 + 1)**4, 6 * x**2 * (x**2 + 1)**2])
anti(2, x * (x**2 + 1)**3,
     [(x**2 + 1)**4 / 8, (x**2 + 1)**4 / 4, (x**2 + 1)**4 / 2,
      x**2 * (x**2 + 1)**4 / 8])
anti(4, sp.cos(3 * x),
     [sp.sin(3 * x) / 3, 3 * sp.sin(3 * x), sp.sin(3 * x), -sp.sin(3 * x) / 3])
anti(5, sp.sin(x) * sp.cos(x),
     [sp.sin(x)**2 / 2, sp.sin(x)**2, sp.cos(x)**2 / 2, sp.sin(x) * sp.cos(x)])
anti(6, 2 * x * sp.exp(x**2),
     [sp.exp(x**2), sp.exp(x**2) / 2, 2 * x * sp.exp(x**2), x**2 * sp.exp(x**2)])
anti(7, (2 * x + 1)**5,
     [(2 * x + 1)**6 / 12, (2 * x + 1)**6 / 6, (2 * x + 1)**6 / 2, 10 * (2 * x + 1)**4])
anti(8, 1 / (3 * x + 2),
     [sp.log(sp.Abs(3 * x + 2)) / 3, sp.log(sp.Abs(3 * x + 2)),
      3 * sp.log(sp.Abs(3 * x + 2)), -1 / (3 * (3 * x + 2)**2)])
anti(15, sp.tan(x),
     [-sp.log(sp.Abs(sp.cos(x))), sp.log(sp.Abs(sp.cos(x))), sp.sec(x)**2,
      sp.tan(x)**2 / 2])
anti(16, sp.log(x) / x,
     [sp.log(x)**2 / 2, sp.log(x)**2, 1 / (2 * x**2), sp.log(sp.Abs(sp.log(x)))])
anti(17, x / (x**2 + 4),
     [sp.log(x**2 + 4) / 2, sp.log(x**2 + 4), sp.atan(x / 2) / 2, None])
anti(18, sp.sec(5 * x)**2,
     [sp.tan(5 * x) / 5, 5 * sp.tan(5 * x), sp.tan(5 * x), sp.sec(5 * x)**3 / 15])
anti(20, x * sp.sqrt(x - 1),
     [sp.Rational(2, 5) * (x - 1)**sp.Rational(5, 2)
      + sp.Rational(2, 3) * (x - 1)**sp.Rational(3, 2),
      sp.Rational(2, 3) * x * (x - 1)**sp.Rational(3, 2),
      sp.Rational(2, 5) * (x - 1)**sp.Rational(5, 2),
      sp.Rational(2, 3) * (x - 1)**sp.Rational(3, 2)
      + sp.Rational(2, 5) * x * (x - 1)**sp.Rational(5, 2)])
anti(23, sp.exp(sp.sin(x)) * sp.cos(x),
     [sp.exp(sp.sin(x)), sp.exp(sp.sin(x)) * sp.sin(x), sp.exp(sp.cos(x)),
      sp.exp(sp.sin(x)) / sp.cos(x)])

# ------------------------------------------- definite, checked in x and u ----
definite(9, 2 * x * (x**2 + 1)**3, 0, 2, [4, 39, 156, sp.Rational(625, 4)],
         sub=(x**2 + 1, u**3))
definite(11, sp.sin(x)**2 * sp.cos(x), 0, sp.pi / 2,
         [sp.Rational(1, 3), sp.Rational(1, 2), sp.Rational(2, 3), 1],
         sub=(sp.sin(x), u**2))
definite(12, x * sp.exp(x**2), 0, 1,
         [(E - 1) / 2, E - 1, E / 2, 2 * (E - 1)], sub=(x**2, sp.exp(u) / 2))
definite(13, (3 * x + 1)**4, 0, 1,
         [sp.Rational(341, 5), sp.Rational(1023, 5), sp.Rational(341, 15),
          sp.Rational(1024, 15)], sub=(3 * x + 1, u**4 / 3))
definite(19, sp.sin(2 * x), 0, sp.pi, [0, 1, 2, sp.Rational(1, 2)],
         sub=(2 * x, sp.sin(u) / 2))
definite(21, x * sp.sqrt(x - 1), 1, 5,
         [sp.Rational(272, 15), sp.Rational(64, 5), sp.Rational(16, 3),
          sp.Rational(128, 15)], sub=(x - 1, (u + 1) * sp.sqrt(u)))
definite(22, x / (x**2 + 1)**2, 0, 1,
         [sp.Rational(1, 4), sp.Rational(1, 2), sp.Rational(1, 8), sp.log(2) / 2],
         sub=(x**2 + 1, 1 / (2 * u**2)))
definite(24, sp.exp(x) / (1 + sp.exp(x)), 0, sp.log(3),
         [sp.log(2), sp.log(3), sp.log(4), sp.Rational(1, 2)],
         sub=(1 + sp.exp(x), 1 / u))

# 3: u = x^2 + 9 really does clear every x, and the rivals do not
assert sp.simplify(sp.integrate(x * sp.sqrt(x**2 + 9), (x, 0, 4))
                   - sp.integrate(sp.sqrt(u) / 2, (u, 9, 25))) == 0
key_is(3, "u = x^2 + 9")

# 10: converted limits for u = x^2 + 1 on [0, 2]
assert ((x**2 + 1).subs(x, 0), (x**2 + 1).subs(x, 2)) == (1, 5)
assert sp.simplify(sp.integrate(x * sp.sqrt(x**2 + 1), (x, 0, 2))
                   - sp.integrate(sp.sqrt(u) / 2, (u, 1, 5))) == 0
key_is(10, "from u = 1 to u = 5")

# 25: du = 3x^2 dx absorbs the entire factor in front
assert sp.simplify(sp.integrate(3 * x**2 * sp.cos(x**3), (x, 0, 2))
                   - sp.integrate(sp.cos(u), (u, 0, 8))) == 0
key_is(25, "int cos(u) du")

assert checked | CONCEPTUAL == set(range(1, 26)), sorted(set(range(1, 26)) - (checked | CONCEPTUAL))
assert not (checked & CONCEPTUAL)
assert len(QUESTIONS) == 25
for k, q in enumerate(QUESTIONS, 1):
    assert len(q["choices"]) == 4 and len(set(q["choices"])) == 4, f"q{k}: choices"
    assert 0 <= q["ans"] < 4, f"q{k}: ans"
print(f"c6_9: {len(checked)} computational questions verified, "
      f"{len(CONCEPTUAL)} conceptual; all 25 checked for shape.")
