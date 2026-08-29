"""sympy verification for CALC 2.5.

Each computational question's four choices are transcribed as sympy
expressions in module order and the true derivative is computed with sp.diff.
The check confirms the keyed choice equals that derivative and that no two
choices are equivalent (so no distractor is a second correct answer).

Conceptual questions (1, 8, 16): the statement of the power rule, why it does
not apply to 2^x (the variable is in the exponent, so d/dx[2^x] = 2^x ln 2,
confirmed below), and a diagnosed student error.
"""
import importlib
import sympy as sp

M = importlib.import_module("c2_5")
x = sp.Symbol("x", positive=True)  # positive so fractional powers stay real
n = sp.Symbol("n")

CONCEPTUAL = {1, 8, 16}
checked = set()
R = sp.Rational


def check(n_, exprs, true_val):
    item = M.QUESTIONS[n_ - 1]
    assert len(exprs) == 4 == len(item["choices"]), f"q{n_}: expected 4 choices"
    diff = sp.simplify(exprs[item["ans"]] - true_val)
    assert diff == 0, f"q{n_}: keyed choice {item['ans']} != d/dx ({diff})"
    for i in range(4):
        for j in range(i + 1, 4):
            assert sp.simplify(exprs[i] - exprs[j]) != 0, f"q{n_}: choices {i} and {j} are equivalent"
    checked.add(n_)


def d(f):
    return sp.diff(f, x)


check(2, [5 * x**4, 5 * x**5, x**4, x**6 / 6], d(x**5))
check(3, [-3 * x**-4, -3 * x**-2, 3 * x**-4, -x**-2 / 2], d(x**-3))
check(4, [1 / (2 * sp.sqrt(x)), 2 * sp.sqrt(x), 1 / sp.sqrt(x), sp.sqrt(x) / 2], d(sp.sqrt(x)))
check(5, [R(2, 3) * x ** R(-1, 3), R(2, 3) * x ** R(2, 3), R(3, 2) * x ** R(-1, 3),
          R(3, 5) * x ** R(5, 3)], d(x ** R(2, 3)))
check(6, [R(3, 2) * x ** R(1, 2), R(3, 2) * x ** R(3, 2), R(2, 3) * x ** R(1, 2),
          R(1, 2) * x ** R(1, 2)], d(sp.sqrt(x**3)))
check(7, [-4 / x**5, 4 / x**5, -4 / x**3, -1 / (4 * x**3)], d(1 / x**4))
check(9, [512, 1024, 2560, 5120], d(x**10).subs(x, 2))
check(10, [R(-1, 3), R(-1, 9), R(1, 9), R(1, 3)], d(1 / x).subs(x, 3))
check(11, [R(1, 12), R(1, 6), R(2, 3), 2], d(x ** R(1, 3)).subs(x, 8))
check(12, [3, 6, 8, 12], d(x ** R(3, 2)).subs(x, 4))
check(13, [-1 / (2 * x ** R(3, 2)), 1 / (2 * x ** R(3, 2)), -1 / (2 * sp.sqrt(x)),
           -2 / x ** R(3, 2)], d(1 / sp.sqrt(x)))
check(14, [R(5, 2) * x ** R(3, 2), R(5, 2) * x ** R(7, 2), R(2, 7) * x ** R(7, 2),
           R(3, 2) * x ** R(5, 2)], d(x ** R(5, 2)))
check(15, [100 * x**99, 100 * x**100, x**99, x**101 / 101], d(x**100))
check(17, [R(-2, 3) * x ** R(-5, 3), R(2, 3) * x ** R(-5, 3), R(-2, 3) * x ** R(1, 3),
           R(-3, 2) * x ** R(-5, 3)], d(x ** R(-2, 3)))
check(18, [sp.pi * x ** (sp.pi - 1), sp.pi * x**sp.pi, x ** (sp.pi - 1),
           x ** (sp.pi + 1) / (sp.pi + 1)], d(x**sp.pi))
check(19, [6 * x**5, 2 * x**3, 6 * x**6, 5 * x**6], d((x**3) ** 2))
check(20, [6, 8, 12, 24], d(x**3).subs(x, 2))
check(25, [4, R(20, 3), R(40, 3), R(160, 3)], d(x ** R(5, 3)).subs(x, 8))

# q21: the tangent line to y = x^4 at (1, 1), written as four lines in x.
tan21 = sp.diff(x**4, x).subs(x, 1) * (x - 1) + 1
check(21, [4 * x - 3, 4 * x + 1, 4 * x, x + 3], sp.expand(tan21))

# q22: horizontal tangents of y = x^3 are the zeros of its derivative.
zeros22 = sp.solve(sp.Eq(sp.diff(sp.Symbol("u") ** 3, sp.Symbol("u")), 0), sp.Symbol("u"))
assert zeros22 == [0], f"q22: horizontal tangents at {zeros22}"
assert M.QUESTIONS[21]["ans"] == 0 and M.QUESTIONS[21]["choices"][0].startswith("x = 0 only")
checked.add(22)

# q23: x^p is differentiable at 0 only when the derivative (p)x^(p-1) stays
# finite there. Tested with the real cube-root branch so negative x is allowed.
u = sp.Symbol("u", real=True)
h = sp.Symbol("h", real=True)


def diff_at_0(p_num, p_den):
    f = sp.real_root(u, p_den) ** p_num
    lo = sp.limit((f.subs(u, h) - 0) / h, h, 0, "-")
    hi = sp.limit((f.subs(u, h) - 0) / h, h, 0, "+")
    return lo == hi and lo.is_finite


assert diff_at_0(4, 3), "q23: x^(4/3) should be differentiable at 0"
assert not diff_at_0(2, 3), "q23: x^(2/3) should not be"
assert not diff_at_0(1, 3), "q23: x^(1/3) should not be"
assert M.QUESTIONS[22]["ans"] == 0 and M.QUESTIONS[22]["choices"][0] == "p = 4/3"
checked.add(23)

# q24: solve n * 2^(n-1) = 80 over the offered integers.
fits = [k for k in (4, 5, 6, 8) if k * 2 ** (k - 1) == 80]
assert fits == [5], f"q24: {fits}"
assert M.QUESTIONS[23]["choices"][M.QUESTIONS[23]["ans"]] == "5"
checked.add(24)

assert len(M.QUESTIONS) == 25, f"expected 25 questions, found {len(M.QUESTIONS)}"
assert checked | CONCEPTUAL == set(range(1, 26)), \
    f"unaccounted questions: {set(range(1, 26)) - checked - CONCEPTUAL}"
assert not (checked & CONCEPTUAL)
# The conceptual q8 rests on d/dx[2^x] not being x 2^(x-1):
v = sp.Symbol("v")
assert sp.diff(2**v, v) == 2**v * sp.log(2) != v * 2 ** (v - 1)
for i, item in enumerate(M.QUESTIONS, 1):
    assert len(item["choices"]) == 4 == len(set(item["choices"])), f"q{i}: choices"
print(f"c2_5: {len(checked)} verified with sympy, {len(CONCEPTUAL)} conceptual, 25 total")
