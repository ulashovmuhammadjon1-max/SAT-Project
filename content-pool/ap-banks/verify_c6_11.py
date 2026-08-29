"""sympy verification for CALC 6.11 Integrating Using Integration by Parts.

Two independent checks per computational question:

  * the keyed antiderivative differentiates back to the integrand, and no
    distractor does (correct antiderivatives can differ by a constant, so the
    comparison is always made on derivatives);
  * the by-parts calculation itself is carried out symbolically -- u*v minus
    sp.integrate(v * du) -- and must agree with the key up to a constant.

CONCEPTUAL questions -- no computation, reasoning stated here:
  1  the formula int u dv = uv - int v du, from integrating the product rule
 12  LIATE orders the factors by how much differentiating them simplifies
 24  substitution needs a factor that is the derivative of another factor's
     inside; x and e^x are not related that way
"""
import sympy as sp

from c6_11 import QUESTIONS

x = sp.Symbol('x', positive=True)     # positive so ln(x) is real in the checks

CONCEPTUAL = {1, 12, 24}
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


def anti(i, integrand, exprs, parts=None):
    """parts = (u, dv): also perform the by-parts computation and compare."""
    q = QUESTIONS[i - 1]
    assert len(exprs) == len(q["choices"]), f"q{i}: wrong number of expressions"
    key = exprs[q["ans"]]
    assert is_zero(sp.diff(key, x) - integrand), f"q{i}: key is not an antiderivative"
    for j, e in enumerate(exprs):
        if e is None or j == q["ans"]:
            continue
        assert not is_zero(sp.diff(e, x) - integrand), f"q{i}: distractor {j} also works"
    if parts is not None:
        u, dv = parts
        assert is_zero(u * dv - integrand), f"q{i}: u*dv is not the integrand"
        v = sp.integrate(dv, x)
        by_parts = u * v - sp.integrate(v * sp.diff(u, x), x)
        assert is_zero(sp.diff(by_parts - key, x)), f"q{i}: by-parts disagrees with the key"
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


E, ex, lg = sp.E, sp.exp, sp.log

anti(2, x * ex(x), [x * ex(x) - ex(x), x * ex(x) + ex(x), x**2 * ex(x) / 2, ex(x)],
     parts=(x, ex(x)))
anti(3, x * sp.cos(x),
     [x * sp.sin(x) + sp.cos(x), x * sp.sin(x) - sp.cos(x),
      -x * sp.sin(x) + sp.cos(x), x**2 * sp.sin(x) / 2], parts=(x, sp.cos(x)))
anti(4, x * sp.sin(x),
     [-x * sp.cos(x) + sp.sin(x), x * sp.cos(x) - sp.sin(x),
      -x * sp.cos(x) - sp.sin(x), x * sp.sin(x) + sp.cos(x)], parts=(x, sp.sin(x)))
anti(5, lg(x), [x * lg(x) - x, x * lg(x) + x, 1 / x, lg(x)**2 / 2],
     parts=(lg(x), sp.Integer(1)))

# 6: u = ln(x), dv = x dx is the choice that clears the logarithm
v6 = sp.integrate(x, x)
by6 = lg(x) * v6 - sp.integrate(v6 * sp.diff(lg(x), x), x)
assert is_zero(sp.diff(by6, x) - x * lg(x))
key_is(6, "u = ln(x), dv = x dx")

anti(7, x * lg(x),
     [x**2 * lg(x) / 2 - x**2 / 4, x**2 * lg(x) / 2 - x**2 / 2,
      x**2 * lg(x) / 2 + x**2 / 4, x * lg(x) - x], parts=(lg(x), x))
anti(8, x * ex(2 * x),
     [x * ex(2 * x) / 2 - ex(2 * x) / 4, x * ex(2 * x) / 2 - ex(2 * x) / 2,
      x * ex(2 * x) / 2 + ex(2 * x) / 4, x * ex(2 * x) - ex(2 * x) / 2],
     parts=(x, ex(2 * x)))
anti(9, x**2 * ex(x),
     [x**2 * ex(x) - 2 * x * ex(x) + 2 * ex(x),
      x**2 * ex(x) - 2 * x * ex(x) - 2 * ex(x),
      x**2 * ex(x) + 2 * x * ex(x) + 2 * ex(x), x**3 * ex(x) / 3],
     parts=(x**2, ex(x)))

value(10, sp.integrate(x * ex(x), (x, 0, 1)), [1, E - 1, E, 2 * E - 1])
value(11, sp.integrate(x * sp.sin(x), (x, 0, sp.pi)),
      [sp.pi, 2 * sp.pi, 0, sp.pi / 2])

anti(13, sp.atan(x),
     [x * sp.atan(x) - lg(1 + x**2) / 2, x * sp.atan(x) + lg(1 + x**2) / 2,
      sp.atan(x)**2 / 2, 1 / (1 + x**2)], parts=(sp.atan(x), sp.Integer(1)))
anti(14, x * sp.sec(x)**2,
     [x * sp.tan(x) + lg(sp.Abs(sp.cos(x))), x * sp.tan(x) - lg(sp.Abs(sp.cos(x))),
      x * sp.tan(x) - sp.tan(x)**2 / 2, x**2 * sp.tan(x) / 2])
anti(15, x**2 * lg(x),
     [x**3 * lg(x) / 3 - x**3 / 9, x**3 * lg(x) / 3 - x**3 / 3,
      x**3 * lg(x) / 3 + x**3 / 9, x**3 / (3 * lg(x))], parts=(lg(x), x**2))
anti(16, ex(x) * sp.sin(x),
     [ex(x) * (sp.sin(x) - sp.cos(x)) / 2, ex(x) * (sp.sin(x) + sp.cos(x)) / 2,
      ex(x) * sp.sin(x) - ex(x) * sp.cos(x), -ex(x) * sp.cos(x)])

value(17, sp.integrate(lg(x), (x, 1, E)), [1, E - 1, E, E - 2])

# 18: u = x^2, dv = e^x dx -- the choice that lowers the polynomial's degree
v18 = sp.integrate(ex(x), x)
by18 = x**2 * v18 - sp.integrate(v18 * sp.diff(x**2, x), x)
assert is_zero(sp.diff(by18, x) - x**2 * ex(x))
key_is(18, "u = x^2 and dv = e^x dx")

anti(19, (x + 1) * ex(x),
     [x * ex(x), (x + 1) * ex(x), (x + 2) * ex(x), x**2 * ex(x) / 2 + x * ex(x)],
     parts=(x + 1, ex(x)))
anti(20, x * sp.sqrt(x + 1),
     [sp.Rational(2, 3) * x * (x + 1)**sp.Rational(3, 2)
      - sp.Rational(4, 15) * (x + 1)**sp.Rational(5, 2),
      sp.Rational(2, 3) * x * (x + 1)**sp.Rational(3, 2)
      + sp.Rational(4, 15) * (x + 1)**sp.Rational(5, 2),
      sp.Rational(2, 3) * (x + 1)**sp.Rational(3, 2),
      x**2 * (x + 1)**sp.Rational(3, 2) / 3], parts=(x, sp.sqrt(x + 1)))

value(21, sp.simplify(sp.integrate(sp.atan(x), (x, 0, 1))),
      [sp.pi / 4 - lg(2) / 2, sp.pi / 4 + lg(2) / 2, sp.pi / 4, lg(2) / 2])

anti(22, x**3 * ex(x**2),
     [(x**2 - 1) * ex(x**2) / 2, (x**2 + 1) * ex(x**2) / 2,
      x**2 * ex(x**2) / 2, x**4 * ex(x**2) / 4])
anti(23, lg(x) / x**2,
     [-lg(x) / x - 1 / x, -lg(x) / x + 1 / x, lg(x) / x + 1 / x,
      lg(x)**2 / (2 * x)], parts=(lg(x), x**-2))
anti(25, ex(x) * sp.cos(x),
     [ex(x) * (sp.sin(x) + sp.cos(x)) / 2, ex(x) * (sp.sin(x) - sp.cos(x)) / 2,
      ex(x) * sp.sin(x), ex(x) * sp.cos(x) / 2])

assert checked | CONCEPTUAL == set(range(1, 26)), sorted(set(range(1, 26)) - (checked | CONCEPTUAL))
assert not (checked & CONCEPTUAL)
assert len(QUESTIONS) == 25
for k, q in enumerate(QUESTIONS, 1):
    assert len(q["choices"]) == 4 and len(set(q["choices"])) == 4, f"q{k}: choices"
    assert 0 <= q["ans"] < 4, f"q{k}: ans"
print(f"c6_11: {len(checked)} computational questions verified, "
      f"{len(CONCEPTUAL)} conceptual; all 25 checked for shape.")
