"""Verification for CALC 10.11 (Finding Taylor Polynomial Approximations).

Each polynomial key is recomputed from the definition -- sum f^(k)(a)(x-a)^k/k!
built with sp.diff -- and compared to the keyed choice parsed back into a sympy
expression, so the check is on the mathematics and not on the wording.  The
distractors are also parsed and confirmed to be genuinely different
polynomials.

Run: python3 verify_c10_11.py
"""
import re

import sympy as sp
from sympy.parsing.sympy_parser import (implicit_multiplication,
                                        parse_expr,
                                        standard_transformations)

import c10_11

x = sp.Symbol("x")
Q = c10_11.QUESTIONS


def key(i):
    item = Q[i - 1]
    return item["choices"][item["ans"]]


def expect(i, text):
    assert key(i) == text, f"q{i}: key is {key(i)!r}, expected {text!r}"


TRANSFORMS = standard_transformations + (implicit_multiplication,)


def parse(s):
    """Plain-text answer choice -> sympy expression (None if it is prose).

    implicit_multiplication is needed because the modules are written the way a
    textbook writes them ("2 - 3x + 2x^2", "5 + 2(x - 1)"), which is not valid
    Python.  split_symbols is deliberately NOT used: it would tear "pi" apart
    into p*i.
    """
    s = s.replace("^", "**")
    try:
        e = parse_expr(s, local_dict={"x": x, "pi": sp.pi}, transformations=TRANSFORMS)
    except (sp.SympifyError, TypeError, ValueError, SyntaxError, AttributeError):
        return None
    return e if getattr(e, "free_symbols", set()) <= {x} else None


for idx, item in enumerate(Q, 1):
    assert len(item["choices"]) == 4, f"q{idx}: needs exactly four choices"
    assert len(set(item["choices"])) == 4, f"q{idx}: repeated choice text"
    parsed = [p for p in (parse(c) for c in item["choices"]) if p is not None]
    for a in range(len(parsed)):
        for b in range(a + 1, len(parsed)):
            assert sp.simplify(parsed[a] - parsed[b]) != 0, (
                f"q{idx}: two choices are the same expression")


def taylor(f, a, n):
    """The nth-degree Taylor polynomial of f about a, built from the definition."""
    return sum(sp.diff(f, x, k).subs(x, a) / sp.factorial(k) * (x - a) ** k
               for k in range(n + 1))


def matches(i, f, a, n):
    """The keyed choice for question i equals the Taylor polynomial of f."""
    want = sp.expand(taylor(f, a, n))
    got = parse(key(i))
    assert got is not None, f"q{i}: key did not parse"
    assert sp.simplify(sp.expand(got) - want) == 0, f"q{i}: {got} != {want}"


# q1, q2, q3  the definition, its characterizing property, and the name
expect(1, "sum from k=0 to n of f^(k)(a)*(x - a)^k/k!")
# q2  P_n is built so that P_n^(k)(a) = f^(k)(a) for k = 0..n; checked here on
#     e^x about 0 to degree 4.
P = taylor(sp.exp(x), 0, 4)
for k in range(5):
    assert sp.diff(P, x, k).subs(x, 0) == sp.diff(sp.exp(x), x, k).subs(x, 0)
expect(2, "P_n and f agree in value and in their first n derivatives at x = a")
expect(3, "x = 0")

# q4, q5  polynomials assembled from given derivative values
g = sp.Function("g")
P4 = 2 + (-3) * x + sp.Rational(4, 2) * x ** 2
assert sp.simplify(parse(key(4)) - P4) == 0
expect(4, "2 - 3x + 2x^2")
P5 = 5 + 2 * (x - 1) + sp.Rational(-6, 2) * (x - 1) ** 2
assert sp.simplify(parse(key(5)) - P5) == 0
expect(5, "5 + 2(x - 1) - 3(x - 1)^2")

matches(6, sp.exp(x), 0, 3)
expect(6, "1 + x + x^2/2 + x^3/6")
matches(7, sp.cos(x), 0, 4)
expect(7, "1 - x^2/2 + x^4/24")
matches(8, sp.sin(x), 0, 3)
expect(8, "x - x^3/6")
matches(9, sp.log(1 + x), 0, 2)
expect(9, "x - x^2/2")
matches(10, sp.sqrt(x), 4, 2)
assert sp.diff(sp.sqrt(x), x).subs(x, 4) == sp.Rational(1, 4)
assert sp.diff(sp.sqrt(x), x, 2).subs(x, 4) == sp.Rational(-1, 32)
expect(10, "2 + (1/4)(x - 4) - (1/64)(x - 4)^2")

# q11, q12  single coefficients
assert sp.series(sp.exp(x), x, 0, 5).removeO().coeff(x, 4) == sp.Rational(1, 24)
expect(11, "1/24")
assert sp.series(sp.sin(2 * x), x, 0, 5).removeO().coeff(x, 3) == sp.Rational(-4, 3)
expect(12, "-4/3")

# q13, q14, q24  reading a derivative out of a coefficient
assert 5 * sp.factorial(3) == 30
expect(13, "30")
assert 7 * sp.factorial(2) == 14
expect(14, "14")
assert sp.Rational(1, 2) * sp.factorial(4) == 12
expect(24, "12")

# q15  numerical use of P_2 for e^x
P2exp = taylor(sp.exp(x), 0, 2)
assert P2exp.subs(x, sp.Rational(1, 10)) == sp.Rational(1105, 1000)
assert sp.Abs(sp.exp(sp.Rational(1, 10)) - sp.Rational(1105, 1000)) < sp.Rational(1, 1000)
expect(15, "1.105")

matches(16, sp.log(x), 1, 1)
expect(16, "x - 1")
matches(17, 1 / (1 - x), 0, 4)
expect(17, "1 + x + x^2 + x^3 + x^4")
matches(18, sp.exp(2 * x), 0, 2)
expect(18, "1 + 2x + 2x^2")
matches(19, sp.cos(x), sp.pi / 2, 3)
expect(19, "-(x - pi/2) + (x - pi/2)^3/6")
matches(20, x * sp.exp(x), 0, 3)
expect(20, "x + x^2 + x^3/2")

# q21  cos(x^2): the degree-4 polynomial is 1 - x^4/2, and the next term is x^8
matches(21, sp.cos(x ** 2), 0, 4)
s21 = sp.series(sp.cos(x ** 2), x, 0, 9).removeO()
assert s21.coeff(x, 2) == 0 and s21.coeff(x, 4) == sp.Rational(-1, 2)
assert s21.coeff(x, 8) == sp.Rational(1, 24)
expect(21, "1 - x^4/2")

matches(22, 1 / x, 1, 2)
expect(22, "1 - (x - 1) + (x - 1)^2")
matches(23, sp.exp(x) * sp.sin(x), 0, 3)
expect(23, "x + x^2 + x^3/3")

# q25  degree-5 Maclaurin polynomial of sin x: three nonzero terms
p25 = sp.Poly(sp.expand(taylor(sp.sin(x), 0, 5)), x)
assert len([c for c in p25.all_coeffs() if c != 0]) == 3
assert sp.expand(taylor(sp.sin(x), 0, 5)) == x - x ** 3 / 6 + x ** 5 / 120
expect(25, "3")

print("c10_11: all 25 keys verified")
