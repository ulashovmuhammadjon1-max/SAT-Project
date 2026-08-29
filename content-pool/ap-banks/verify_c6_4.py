"""sympy verification for CALC 6.4 The Fundamental Theorem of Calculus and
Accumulation Functions.

Each accumulation function is built as sp.Integral with its real limits and
differentiated with .diff(x), so sympy -- not the author -- supplies the
Leibniz chain-rule factor on a variable upper limit and the sign flip on a
variable lower limit.  The other three choices are then checked to be
genuinely different expressions.

CONCEPTUAL questions -- no computation, reasoning stated here:
 13  omitting the factor 2x is exactly the missing chain rule
 17  continuity of the integrand is the hypothesis of the theorem
 18  F' = f exists, so F is differentiable and hence continuous
 22  f > 0 gives h' > 0 (increasing); it says nothing about the sign of h or
     about concavity, which needs f'
 25  the derivative is f(x): no f(a) term, and no free t
"""
import sympy as sp

from c6_4 import QUESTIONS

x, t = sp.symbols('x t', positive=True)
f = sp.Function('f')

CONCEPTUAL = {13, 17, 18, 22, 25}
checked = set()


def chk(i, computed, values):
    """values: the value of each choice, in module order (None = not an expr)."""
    q = QUESTIONS[i - 1]
    assert len(values) == len(q["choices"]), f"q{i}: wrong number of values"
    assert values[q["ans"]] is not None, f"q{i}: key has no value"
    for a in range(len(values)):
        for b in range(a + 1, len(values)):
            if values[a] is None or values[b] is None:
                continue
            assert sp.simplify(values[a] - values[b]) != 0, f"q{i}: choices {a},{b} equal"
    assert sp.simplify(computed - values[q["ans"]]) == 0, f"q{i}: key mismatch"
    checked.add(i)


def D(integrand, lo, hi):
    """d/dx of int from lo to hi of integrand dt, done by sympy."""
    return sp.simplify(sp.Integral(integrand, (t, lo, hi)).diff(x))


# 1: the theorem itself, with an unspecified continuous f
d1 = D(f(t), 1, x)
assert d1 == f(x)
chk(1, d1, [f(x), f(x) - f(1), sp.Derivative(f(x), x).doit(), None])

# 2
chk(2, D(t**2 + 1, 0, x), [x**2 + 1, 2 * x, x**3 / 3 + x, (x**2 + 1) / 3])

# 3: F'(3) = sqrt(3^3 + 1)
d3 = D(sp.sqrt(t**3 + 1), 2, x)
assert sp.simplify(d3 - sp.sqrt(x**3 + 1)) == 0
chk(3, d3.subs(x, 3), [3, sp.sqrt(28), sp.sqrt(28) - 3, 28])

# 4: chain rule on the upper limit
chk(4, D(sp.sin(t), 0, x**2),
    [sp.sin(x**2), 2 * x * sp.sin(x**2), 2 * x * sp.cos(x**2), sp.cos(x**2) - 1])

# 5
chk(5, D(sp.log(t), 1, x**3),
    [sp.log(x**3), 3 * x**2 * sp.log(x**3), 3 * x**2 / x**3,
     x**3 * sp.log(x**3) - x**3])

# 6: variable lower limit flips the sign
chk(6, D(sp.exp(t**2), x, 5),
    [sp.exp(x**2), -sp.exp(x**2), -2 * x * sp.exp(x**2), sp.exp(25) - sp.exp(x**2)])

# 7
chk(7, D(1 / (1 + t**2), 0, x),
    [1 / (1 + x**2), sp.atan(x), -2 * x / (1 + x**2)**2, 2 * x / (1 + x**2)])

# 8: equal limits
val8 = sp.Integral(f(t), (t, 3, 3)).doit()
assert val8 == 0
chk(8, val8, [0, 3, f(3), None])

# 9: variable lower limit and a chain rule together
chk(9, D(sp.cos(t), 2 * x, 5),
    [-2 * sp.cos(2 * x), 2 * sp.cos(2 * x), -sp.cos(2 * x), -2 * sp.sin(2 * x)])

# 10: both limits variable
chk(10, D(1 / t, x**2, x**3),
    [1 / x, 3 / x, 5 / x, sp.log(x**3) - sp.log(x**2)])

# 11: g'(2) = f(2) = 5
g11 = D(f(t), 0, x)
assert g11 == f(x)
chk(11, g11.subs(f(x), 5), [0, 2, 5, 10])

# 12: second derivative
chk(12, sp.diff(D(t**2 - 4, 0, x), x), [2, 2 * x, x**2 - 4, x**3 / 3 - 4 * x])

# 14
chk(14, D(t**2, 0, sp.sin(x)),
    [sp.sin(x)**2 * sp.cos(x), sp.sin(x)**2, sp.sin(x)**3 / 3,
     2 * sp.sin(x) * sp.cos(x)])

# 15: F(3) for F(x) = int from 1 to x of 2t dt
F15 = sp.integrate(2 * t, (t, 1, x))
assert sp.simplify(F15 - (x**2 - 1)) == 0
chk(15, F15.subs(x, 3), [6, 8, 9, 10])

# 16: H'(4), with H(4) itself as the trap distractor
H16 = sp.integrate(3 * t - 1, (t, 0, x))
chk(16, D(3 * t - 1, 0, x).subs(x, 4), [3, 11, 12, H16.subs(x, 4)])
assert H16.subs(x, 4) == 20

# 19
d19 = D(1 / (1 + t**2), 1, x**2)
assert sp.simplify(d19 - 2 * x / (1 + x**4)) == 0
chk(19, d19.subs(x, 1), [0, sp.Rational(1, 2), 1, 2])

# 20
d20 = D(sp.sqrt(1 + t**2), 0, 2 * x)
assert sp.simplify(d20 - 2 * sp.sqrt(1 + 4 * x**2)) == 0
chk(20, d20.subs(x, 1), [sp.sqrt(5) / 2, sp.sqrt(5), 2 * sp.sqrt(5), 4 * sp.sqrt(5)])

# 21: both limits variable
chk(21, D(sp.exp(t), x, x**2),
    [sp.exp(x**2) - sp.exp(x), 2 * x * sp.exp(x**2) - sp.exp(x),
     2 * x * sp.exp(x**2) - 1, sp.exp(x**2) - 1])

# 23: F(6) is the given integral
chk(23, sp.Integer(9), [0, sp.Rational(9, 2), 9, 18])

# 24: the explicit form and the chain-rule form must agree
G24 = sp.integrate(t, (t, 0, x**2))
assert sp.simplify(G24 - x**4 / 2) == 0
assert sp.simplify(sp.diff(G24, x) - 2 * x**3) == 0
assert sp.simplify(D(t, 0, x**2) - 2 * x**3) == 0
assert QUESTIONS[23]["ans"] == 0
checked.add(24)

assert checked | CONCEPTUAL == set(range(1, 26)), sorted(set(range(1, 26)) - (checked | CONCEPTUAL))
assert not (checked & CONCEPTUAL)
assert len(QUESTIONS) == 25
for k, q in enumerate(QUESTIONS, 1):
    assert len(q["choices"]) == 4 and len(set(q["choices"])) == 4, f"q{k}: choices"
    assert 0 <= q["ans"] < 4, f"q{k}: ans"
print(f"c6_4: {len(checked)} computational questions verified, "
      f"{len(CONCEPTUAL)} conceptual; all 25 checked for shape.")
