"""sympy verification for CALC 3.5.

Choices are transcribed as sympy expressions in module order and compared
against sp.diff. Because several questions are deliberately faster by
rewriting than by the quotient rule, the pairwise check compares choices as
functions (a numeric probe first, then sp.simplify) so an unsimplified twin of
the key cannot slip in as a distractor.

Conceptual questions (1, 2, 3, 25) ask which procedure applies; each is
backed below by differentiating the function in question and confirming the
structure the answer claims.
"""
import importlib
import sympy as sp

M = importlib.import_module("c3_5")
x = sp.Symbol("x", positive=True)

CONCEPTUAL = {1, 2, 3, 25}
checked = set()
R = sp.Rational
sin, cos, tan, sec, cot, exp, log, sqrt = (
    sp.sin, sp.cos, sp.tan, sp.sec, sp.cot, sp.exp, sp.log, sp.sqrt)


def check(n, exprs, true_val):
    item = M.QUESTIONS[n - 1]
    assert len(exprs) == 4 == len(item["choices"]), f"q{n}: expected 4 choices"
    diff = sp.simplify(sp.trigsimp(exprs[item["ans"]] - true_val))
    assert diff == 0, f"q{n}: keyed choice {item['ans']} != computed ({diff})"
    for i in range(4):
        for j in range(i + 1, 4):
            d = sp.sympify(exprs[i] - exprs[j])
            probes = [sp.N(d.subs(x, sp.Rational(k, 10))) for k in (3, 7, 11, 23)]
            if all(abs(v) < 1e-9 for v in probes if v.is_real):
                assert sp.simplify(sp.trigsimp(d)) != 0, \
                    f"q{n}: choices {i} and {j} are the same function"
    checked.add(n)


def d(f):
    return sp.diff(f, x)


check(4, [2 * x * sin(3 * x) + 3 * x**2 * cos(3 * x),
          2 * x * sin(3 * x) + x**2 * cos(3 * x),
          6 * x * cos(3 * x), 2 * x * cos(3 * x)], d(x**2 * sin(3 * x)))
check(5, [exp(2 * x) * (2 * cos(x) - sin(x)), exp(2 * x) * (2 * cos(x) + sin(x)),
          exp(2 * x) * (cos(x) - sin(x)), -2 * exp(2 * x) * sin(x)],
      d(exp(2 * x) * cos(x)))
check(6, [6 * x * (x**2 + 1) ** 2 * (x - 1) + (x**2 + 1) ** 3,
          3 * (x**2 + 1) ** 2 * (x - 1) + (x**2 + 1) ** 3,
          6 * x * (x**2 + 1) ** 2 * (x - 1),
          6 * x * (x**2 + 1) ** 2], d((x**2 + 1) ** 3 * (x - 1)))
check(7, [(cos(x) - sin(x)) / exp(x), (cos(x) + sin(x)) / exp(x), cos(x) / exp(x),
          (sin(x) - cos(x)) / exp(x)], d(sin(x) / exp(x)))
check(8, [2 / x + 1, 2 / x, 1 / (x**2 * exp(x)), 2 * x + exp(x)], d(log(x**2 * exp(x))))
check(9, [-1 / (x**2 * sqrt(x**2 + 1)), 1 / (x**2 * sqrt(x**2 + 1)),
          -1 / (x * sqrt(x**2 + 1)), x / sqrt(x**2 + 1)], d(sqrt(x**2 + 1) / x))
check(10, [2 * x * exp(3 * x) + 3 * x**2 * exp(3 * x),
           2 * x * exp(3 * x) + x**2 * exp(3 * x),
           6 * x * exp(3 * x), 2 * x * exp(3 * x)], d(x**2 * exp(3 * x)))
check(11, [2 * x * sec(x**2) ** 2, sec(x**2) ** 2, 2 * x * sec(x) ** 2,
           2 * x * tan(x**2) * sec(x**2)], d(tan(x**2)))
check(12, [3 * log(x) ** 2 / x, 3 * log(x) ** 2, log(x) ** 3 / x,
           3 * log(x) ** 2 * log(x)], d(log(x) ** 3))
check(13, [cot(x), tan(x), 1 / sin(x), -cot(x)], d(log(sin(x))))
check(14, [(sin(x) - x * cos(x)) / sin(x) ** 2, (x * cos(x) - sin(x)) / sin(x) ** 2,
           (sin(x) - x * cos(x)) / sin(x), 1 / cos(x)], d(x / sin(x)))
check(15, [exp(x) * (x - 1) ** 2 / (x**2 + 1) ** 2,
           exp(x) * (x + 1) ** 2 / (x**2 + 1) ** 2,
           exp(x) * (x**2 - 2 * x + 1) / (x**2 + 1),
           exp(x) / (2 * x)], d(exp(x) / (x**2 + 1)))
check(16, [sqrt(x**2 + 1) + x**2 / sqrt(x**2 + 1),
           sqrt(x**2 + 1) + x / sqrt(x**2 + 1),
           sqrt(x**2 + 1) + 2 * x**2 / sqrt(x**2 + 1),
           x**2 / sqrt(x**2 + 1)], d(x * sqrt(x**2 + 1)))
check(17, [-sin(x) * cos(cos(x)), cos(cos(x)), sin(x) * cos(cos(x)), -cos(sin(x))],
      d(sin(cos(x))))
check(18, [R(8, 9), R(4, 9), R(-4, 9), R(-8, 9)], d((x**2 + 1) / (x**2 - 1)).subs(x, 2))
check(19, [2 * x, 3 * x**2 - 1, (3 * x**2 - 1) / x, 2 * x - 1],
      d(sp.cancel((x**3 - x) / x)))
check(20, [exp(x**2) * (2 * x * sin(x) + cos(x)), exp(x**2) * (2 * x * sin(x) - cos(x)),
           exp(x**2) * (sin(x) + cos(x)), 2 * x * exp(x**2) * cos(x)],
      d(exp(x**2) * sin(x)))
check(21, [-2 / (x**2 - 1), 2 / (x**2 - 1), 1 / (x + 1) + 1 / (x - 1),
           (x - 1) / (x + 1)], sp.simplify(d(log(x + 1) - log(x - 1))))
check(22, [sec(2 * x) ** 2 / sqrt(tan(2 * x)), sec(2 * x) ** 2 / (2 * sqrt(tan(2 * x))),
           1 / (2 * sqrt(tan(2 * x))), 2 * sec(2 * x) ** 2 * sqrt(tan(2 * x))],
      d(sqrt(tan(2 * x))))
check(23, [2 * x * log(3 * x) + x, 2 * x * log(3 * x) + 3 * x, 2 * x * log(3 * x),
           2 * x / (3 * x)], d(x**2 * log(3 * x)))
check(24, [-1, 1, 5, 6], d((2 * x + 1) ** 3 * exp(-x)).subs(x, 0))

# --- the conceptual questions, backed by the actual derivatives ------------
# q1: x^2 sin(3x) is a product whose second factor is a composite, so the
# derivative contains both a product-rule sum and an inner factor of 3.
d1 = sp.expand(d(x**2 * sin(3 * x)))
assert d1.has(cos(3 * x)) and d1.coeff(cos(3 * x)) == 3 * x**2

# q2: sin(x^2 + 1) is a lone composite -- one term, carrying the inner 2x.
d2 = d(sin(x**2 + 1))
assert d2 == 2 * x * cos(x**2 + 1) and len(sp.Add.make_args(d2)) == 1

# q3: (x^2 + 1)/(x - 3) does not cancel, so the quotient really is needed.
assert sp.cancel((x**2 + 1) / (x - 3)) == (x**2 + 1) / (x - 3)
assert sp.rem(sp.Poly(x**2 + 1, x), sp.Poly(x - 3, x)) != 0

# q25: rewriting ln(x^5) as 5 ln(x) gives the same derivative, and 5x^4 alone
# is not it.
assert sp.simplify(d(log(x**5)) - d(5 * log(x))) == 0
assert sp.simplify(d(log(x**5)) - 5 / x) == 0 and sp.simplify(d(log(x**5)) - 5 * x**4) != 0

assert len(M.QUESTIONS) == 25, f"expected 25 questions, found {len(M.QUESTIONS)}"
assert checked | CONCEPTUAL == set(range(1, 26)), \
    f"unaccounted questions: {set(range(1, 26)) - checked - CONCEPTUAL}"
assert not (checked & CONCEPTUAL)
for i, item in enumerate(M.QUESTIONS, 1):
    assert len(item["choices"]) == 4 == len(set(item["choices"])), f"q{i}: choices"
print(f"c3_5: {len(checked)} verified with sympy, {len(CONCEPTUAL)} conceptual, 25 total")
