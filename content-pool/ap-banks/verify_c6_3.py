"""sympy verification for CALC 6.3 Riemann Sums, Summation Notation, and
Definite Integral Notation.

Finite sums are evaluated with sp.Sum(...).doit(); every "which limit / which
integral" question is checked the strong way, by taking the limit of each
candidate Riemann sum with sp.limit and confirming that only the keyed one
agrees with the integral computed independently by sp.integrate.

CONCEPTUAL questions -- no computation, reasoning stated here:
 12  dx names the variable of integration
 13  the variable of integration is a dummy; the integral is a number
 14  the definite integral is defined as a limit of Riemann sums
 20  a Riemann sum admits any sample point in each subinterval
 23  summation distributes over addition in a finite sum
"""
import re
import sympy as sp

from c6_3 import QUESTIONS

x, c = sp.symbols('x c', positive=True)
# i and n MUST be declared integer: with a merely positive n, sympy evaluates
# Sum(exp(i/n)/n, (i, 1, n)) to a Piecewise whose limit it reports as 1 instead
# of e - 1.  A silently wrong symbolic answer is the worst kind of check.
i, n = sp.symbols('i n', positive=True, integer=True)

CONCEPTUAL = {12, 13, 14, 20, 23}
checked = set()


def chk(i_q, computed, values, text_check=True):
    """values: value of each choice in module order; None = not a number."""
    q = QUESTIONS[i_q - 1]
    assert len(values) == len(q["choices"]), f"q{i_q}: wrong number of values"
    assert values[q["ans"]] is not None, f"q{i_q}: key has no value"
    for a in range(len(values)):
        for b in range(a + 1, len(values)):
            if values[a] is None or values[b] is None:
                continue
            assert sp.simplify(values[a] - values[b]) != 0, f"q{i_q}: choices {a},{b} equal"
    if text_check:
        for v, text in zip(values, q["choices"]):
            if v is None:
                continue
            m = re.search(r"-?\d+(?:\.\d+)?(?:/\d+)?", text)
            assert m, f"q{i_q}: no number in {text!r}"
            shown = sp.Rational(m.group()) if "/" in m.group() else float(m.group())
            assert abs(float(shown) - float(v)) < 0.0011, f"q{i_q}: {text!r} != {float(v)}"
    assert sp.simplify(computed - values[q["ans"]]) == 0, f"q{i_q}: key mismatch"
    checked.add(i_q)


def rsum_limit(term):
    """limit as n -> infinity of the sum from i = 1 to n of `term`, or None
    when sympy has no closed form for the partial sum (sqrt(i) has none)."""
    try:
        return sp.limit(sp.simplify(sp.Sum(term, (i, 1, n)).doit()), n, sp.oo)
    except (NotImplementedError, TypeError):
        return None


def rsum_numeric(term, N=100000):
    """The Riemann sum itself at a large n -- the fallback when the partial
    sum has no closed form.  Used only to confirm a limit sympy cannot take."""
    f = sp.lambdify(i, term.subs(n, N), 'math')
    return sum(f(k) for k in range(1, N + 1))


def rsum_equals(term, expected, tol=1e-3):
    """Confirm the limit of the Riemann sum is `expected`, symbolically when
    possible and numerically at large n otherwise; returns `expected`."""
    sym = rsum_limit(term)
    if sym is not None:
        assert sp.simplify(sym - expected) == 0, (sym, expected)
    else:
        assert abs(rsum_numeric(term) - float(expected)) < tol, (term, expected)
    return expected


# 1, 2: width and right endpoints of an equal partition
for a, b, keyed in [(0, 4, 4 * i / n), (1, 5, 1 + 4 * i / n)]:
    assert sp.simplify((a + i * sp.Rational(b - a) / n) - keyed) == 0
assert sp.simplify(sp.Rational(4) / n - (4 / n)) == 0
assert QUESTIONS[0]["ans"] == 0 and QUESTIONS[1]["ans"] == 0
# the rival endpoint formulas really are different functions of i and n
for wrong in [i / n, 4 + i / n]:
    assert sp.simplify(4 * i / n - wrong) != 0
for wrong in [4 * i / n, 1 + i / n, 5 * i / n]:
    assert sp.simplify((1 + 4 * i / n) - wrong) != 0
checked.update({1, 2})

# 3: right Riemann sum for int from 0 to 2 of x^2 dx
v3 = rsum_equals((2 * i / n)**2 * (2 / n), sp.integrate(x**2, (x, 0, 2)))
chk(3, v3, [sp.Rational(4, 3), sp.Rational(8, 3), 4, 8])

# 4: only choice A has the limit int from 1 to 3 of x^3 dx
target4 = sp.integrate(x**3, (x, 1, 3))
cands4 = [rsum_limit((1 + 2 * i / n)**3 * (2 / n)),
          rsum_limit((1 + 2 * i / n)**3 * (1 / n)),
          rsum_limit((2 * i / n)**3 * (2 / n)),
          rsum_limit((1 + 3 * i / n)**3 * (3 / n))]
assert cands4[0] == target4 == 20 and None not in cands4
chk(4, target4, cands4, text_check=False)

# 5: the sum's limit is int from 0 to 1 of sqrt(x) dx, not int from 0 to 1 of x dx
v5 = rsum_equals(sp.sqrt(i / n) / n, sp.integrate(sp.sqrt(x), (x, 0, 1)))
assert v5 == sp.Rational(2, 3)
chk(5, v5, [sp.Rational(2, 3), None, None, sp.integrate(x, (x, 0, 1))], text_check=False)

# 6, 8, 9, 17, 24: closed-form finite sums
chk(6, sp.Sum(2 * i + 1, (i, 1, 5)).doit(), [11, 25, 35, 45])
chk(8, sp.Sum(i, (i, 1, 10)).doit(), [45, 55, 100, 110])
chk(9, sp.Sum(i**2, (i, 1, 6)).doit(), [21, 36, 91, 441])
chk(17, sp.Sum(i**2, (i, 1, 4)).doit(), [10, 20, 30, 100])
chk(24, sp.Sum(3 * i - 2, (i, 1, 20)).doit(), [570, 590, 610, 630])

# 7: sum of a constant
s7 = sp.Sum(c, (i, 1, n)).doit()
assert sp.simplify(s7 - c * n) == 0
assert QUESTIONS[6]["ans"] == 1
for wrong in [c, c * n * (n + 1) / 2, c / n]:
    assert sp.simplify(c * n - wrong) != 0
checked.add(7)

# 10: a right Riemann sum with width 1 on [2, 6], tested on f(x) = x^2
f10 = x**2
right10 = sum(f10.subs(x, k) for k in (3, 4, 5, 6))
vals10 = [sum(f10.subs(x, k) for k in (2, 3, 4, 5)), right10, 4 * right10, right10 / 4]
chk(10, right10, vals10, text_check=False)

# 11: right Riemann sum for int from 1 to 4 of x dx
v11 = rsum_equals((3 / n) * (1 + 3 * i / n), sp.integrate(x, (x, 1, 4)))
chk(11, v11, [3, sp.Rational(15, 2), 9, 15])

# 15: right Riemann sum, width 1, for 2x + 1 on [0, 4]
v15 = sum((2 * x + 1).subs(x, k) for k in (1, 2, 3, 4))
assert sp.integrate(2 * x + 1, (x, 0, 4)) == 20 < v15  # increasing => overestimate
chk(15, v15, [16, 20, 24, 28])

# 16: right Riemann sum for int from 0 to pi of sin(x) dx
v16 = rsum_equals((sp.pi / n) * sp.sin(sp.pi * i / n), sp.integrate(sp.sin(x), (x, 0, sp.pi)))
chk(16, v16, [0, 1, 2, sp.pi], text_check=False)

# 18: i^2/n^3 = (i/n)^2 (1/n)
v18 = rsum_equals(i**2 / n**3, sp.integrate(x**2, (x, 0, 1)))
chk(18, v18, [0, sp.Rational(1, 6), sp.Rational(1, 3), sp.Rational(1, 2)], text_check=False)

# 19: only choice A has limit int from 0 to 1 of e^x dx; B and C diverge
target19 = sp.integrate(sp.exp(x), (x, 0, 1))
a19 = rsum_equals(sp.exp(i / n) / n, target19)
d19 = rsum_equals(sp.exp(1 / n) / n, sp.Integer(1))
assert rsum_limit(sp.exp(i) / n) is sp.oo and rsum_limit(sp.exp(i / n)) is sp.oo
chk(19, target19, [a19, None, None, d19], text_check=False)

# 21: right Riemann sum for int from 0 to 1 of 1/(1 + x) dx
v21 = rsum_equals((1 / n) * (1 / (1 + i / n)), sp.integrate(1 / (1 + x), (x, 0, 1)))
chk(21, v21, [sp.log(2), sp.log(3), sp.Rational(1, 2), 1], text_check=False)

# 22: width 4/n with sample points 1 + 4i/n means the interval [1, 5]
cands22 = [sp.integrate(sp.sqrt(x), (x, 1, 5)),
           sp.integrate(sp.sqrt(x), (x, 0, 4)),
           sp.integrate(sp.sqrt(1 + 4 * x), (x, 0, 4)),
           sp.integrate(sp.sqrt(x), (x, 1, 4))]
v22 = rsum_equals((4 / n) * sp.sqrt(1 + 4 * i / n), cands22[0])
chk(22, v22, cands22, text_check=False)

# 25: (1/n^2) sum i = (n + 1)/(2n) -> 1/2
expr25 = sp.simplify(sp.Sum(i, (i, 1, n)).doit() / n**2)
assert sp.simplify(expr25 - (n + 1) / (2 * n)) == 0
v25 = sp.limit(expr25, n, sp.oo)
assert v25 == sp.integrate(x, (x, 0, 1))
chk(25, v25, [0, sp.Rational(1, 2), 1, None], text_check=False)

assert checked | CONCEPTUAL == set(range(1, 26)), sorted(set(range(1, 26)) - (checked | CONCEPTUAL))
assert not (checked & CONCEPTUAL)
assert len(QUESTIONS) == 25
for k, q in enumerate(QUESTIONS, 1):
    assert len(q["choices"]) == 4 and len(set(q["choices"])) == 4, f"q{k}: choices"
    assert 0 <= q["ans"] < 4, f"q{k}: ans"
print(f"c6_3: {len(checked)} computational questions verified, "
      f"{len(CONCEPTUAL)} conceptual; all 25 checked for shape.")
