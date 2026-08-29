"""sympy verification for CALC 6.8 Finding Antiderivatives and Indefinite
Integrals: Basic Rules and Notation.

An antiderivative question cannot be checked by comparing expressions, because
two correct antiderivatives differ by a constant.  Every check below therefore
differentiates: the keyed choice must differentiate back to the integrand, and
no other choice may.  sp.integrate is then asked for the antiderivative
independently and must agree with the key up to a constant.

CONCEPTUAL questions -- no computation, reasoning stated here:
 12  n + 1 is zero when n = -1, so that case needs ln|x|
 20  antiderivatives of one function differ by a constant, so + C names the
     whole family
 25  an indefinite integral is a family of functions, a definite integral is a
     number
"""
import sympy as sp

from c6_8 import QUESTIONS

x, t = sp.symbols('x t', real=True)

CONCEPTUAL = {12, 20, 25}
checked = set()


SAMPLES = (sp.Rational(3, 10), sp.Rational(17, 10), sp.Rational(5, 2),
           sp.Rational(-4, 5), sp.Rational(-31, 10))


def is_zero(e, var):
    """True when e is identically zero.  sp.simplify alone is not enough: the
    derivative of log|x| comes back as sign(x)/Abs(x), whose difference from
    1/x simplifies to a Piecewise rather than to 0, so fall back to sampling
    at points on both sides of the origin."""
    if sp.simplify(e) == 0:
        return True
    vals = []
    for v in SAMPLES:
        try:
            val = complex(sp.N(e.subs(var, v)))
        except TypeError:
            continue
        if val != val:            # NaN: undefined there, no information
            continue
        vals.append(abs(val))
    return bool(vals) and max(vals) < 1e-12


def anti(i, integrand, exprs, var=x):
    """exprs: the antiderivative in each choice, in module order (None = one
    that is not a well-formed expression)."""
    q = QUESTIONS[i - 1]
    assert len(exprs) == len(q["choices"]), f"q{i}: wrong number of expressions"
    key = exprs[q["ans"]]
    assert key is not None, f"q{i}: key has no expression"
    assert is_zero(sp.diff(key, var) - integrand, var), f"q{i}: key is not an antiderivative"
    for j, e in enumerate(exprs):
        if e is None or j == q["ans"]:
            continue
        assert not is_zero(sp.diff(e, var) - integrand, var), f"q{i}: distractor {j} also works"
    # sympy's own antiderivative must differ from the key only by a constant
    F = sp.integrate(integrand, var)
    assert is_zero(sp.diff(F - key, var), var), f"q{i}: disagrees with sp.integrate"
    checked.add(i)


def ivp(i, deriv, x0, y0, exprs, var=x):
    """Initial-value problem: the key must satisfy both the ODE and the point."""
    q = QUESTIONS[i - 1]
    key = exprs[q["ans"]]
    assert is_zero(sp.diff(key, var) - deriv, var), f"q{i}: key has the wrong derivative"
    assert key.subs(var, x0) == y0, f"q{i}: key misses the initial condition"
    for j, e in enumerate(exprs):
        if j == q["ans"]:
            continue
        ok = is_zero(sp.diff(e, var) - deriv, var) and e.subs(var, x0) == y0
        assert not ok, f"q{i}: distractor {j} also works"
    checked.add(i)


anti(1, x**5, [x**6 / 6, 5 * x**4, x**6, x**4 / 4])
anti(2, 3 * x**2, [x**3, 3 * x**3, 6 * x, x**3 / 3])
anti(3, 1 / x, [sp.log(sp.Abs(x)), -1 / x**2, None, 1 / (2 * x**2)])
anti(4, sp.exp(x), [sp.exp(x), sp.exp(x) / x, x * sp.exp(x - 1), None])
anti(5, sp.cos(x), [sp.sin(x), -sp.sin(x), -sp.cos(x), sp.tan(x)])
anti(6, sp.sin(x), [-sp.cos(x), sp.cos(x), -sp.sin(x), sp.sec(x)])
anti(7, sp.sec(x)**2, [sp.tan(x), sp.sec(x) * sp.tan(x), sp.sec(x)**3 / 3, 2 * sp.sec(x)])
anti(8, x**-2, [-1 / x, -2 / x**3, x**-1, sp.log(sp.Abs(x**2))])
anti(9, sp.sqrt(x), [sp.Rational(2, 3) * x**sp.Rational(3, 2),
                     sp.Rational(3, 2) * x**sp.Rational(3, 2),
                     sp.Rational(1, 2) * x**sp.Rational(-1, 2),
                     x**sp.Rational(3, 2)])
anti(10, 4 * x**3 - 6 * x + 5,
     [x**4 - 3 * x**2 + 5 * x, x**4 - 6 * x**2 + 5 * x, 12 * x**2 - 6,
      4 * x**4 - 3 * x**2 + 5 * x])
anti(11, 1 / (1 + x**2),
     [sp.atan(x), sp.log(1 + x**2), -1 / (1 + x**2)**2, sp.asin(x)])
anti(13, sp.Integer(5), [5 * x, sp.Integer(5), x, 5 * x**2 / 2])
anti(14, 2 / x, [2 * sp.log(sp.Abs(x)), sp.log(sp.Abs(2 * x)), -2 / x**2, 2 / x**2])
anti(15, sp.exp(3 * x),
     [sp.exp(3 * x) / 3, sp.exp(3 * x), 3 * sp.exp(3 * x), sp.exp(3 * x) / x])
anti(18, x * (x + 2), [x**3 / 3 + x**2, x**3 / 3 + 2 * x**2,
                       x**2 * (x**2 / 2 + 2 * x) / 2, (x**2 / 2) * (x**2 / 2 + 2 * x)])
anti(19, sp.sec(x) * sp.tan(x),
     [sp.sec(x), sp.tan(x), sp.sec(x)**2 / 2, sp.sec(x) * sp.tan(x)])
anti(21, 1 / sp.sqrt(x), [2 * sp.sqrt(x), sp.sqrt(x) / 2,
                          -1 / (2 * x**sp.Rational(3, 2)), sp.log(sp.Abs(sp.sqrt(x)))])
anti(23, 3 / x**4, [-1 / x**3, -3 / x**3, 3 / x**3, -12 / x**5])
anti(24, 2 * sp.cos(x) - 3 * sp.sin(x),
     [2 * sp.sin(x) + 3 * sp.cos(x), 2 * sp.sin(x) - 3 * sp.cos(x),
      -2 * sp.sin(x) + 3 * sp.cos(x), -2 * sp.sin(x) - 3 * sp.cos(x)])

ivp(16, 2 * x, 1, 5, [x**2 + 4, x**2 + 5, x**2 - 4, 2 * x**2 + 3])
ivp(17, 6 * x**2, 0, -2, [2 * x**3 - 2, 2 * x**3 + 2, 6 * x**3 - 2, 12 * x - 2])
ivp(22, 4 * t + 1, 0, 3, [2 * t**2 + t + 3, 2 * t**2 + t,
                          4 * t**2 + t + 3, 2 * t**2 + 3 * t + 1], var=t)

assert checked | CONCEPTUAL == set(range(1, 26)), sorted(set(range(1, 26)) - (checked | CONCEPTUAL))
assert not (checked & CONCEPTUAL)
assert len(QUESTIONS) == 25
for k, q in enumerate(QUESTIONS, 1):
    assert len(q["choices"]) == 4 and len(set(q["choices"])) == 4, f"q{k}: choices"
    assert 0 <= q["ans"] < 4, f"q{k}: ans"
print(f"c6_8: {len(checked)} computational questions verified, "
      f"{len(CONCEPTUAL)} conceptual; all 25 checked for shape.")
