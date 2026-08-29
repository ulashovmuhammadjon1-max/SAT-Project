"""sympy verification for CALC 2.6.

Choices are transcribed as sympy expressions in module order and compared
against sp.diff; the pairwise check rules out a distractor that is a second
correct answer. Questions 2, 3 and 25 are conceptual (the statements of the
constant-multiple and sum/difference rules, and the fact that there is no
product rule of the form f' g'); q25's claim is falsified by example below.
"""
import importlib
import sympy as sp

M = importlib.import_module("c2_6")
x = sp.Symbol("x", positive=True)
a, b, c, k = sp.symbols("a b c k")

CONCEPTUAL = {2, 3, 25}
checked = set()
R = sp.Rational


def check(n, exprs, true_val):
    item = M.QUESTIONS[n - 1]
    assert len(exprs) == 4 == len(item["choices"]), f"q{n}: expected 4 choices"
    diff = sp.simplify(exprs[item["ans"]] - true_val)
    assert diff == 0, f"q{n}: keyed choice {item['ans']} != d/dx ({diff})"
    for i in range(4):
        for j in range(i + 1, 4):
            assert sp.simplify(exprs[i] - exprs[j]) != 0, f"q{n}: choices {i} and {j} are equivalent"
    checked.add(n)


def d(f):
    return sp.diff(f, x)


check(1, [0, 1, 7, 7 * x], d(sp.Integer(7)))
check(4, [6 * x + 5, 6 * x**2 + 5, 6 * x + 5 - 4, 3 * x**2 + 5], d(3 * x**2 + 5 * x - 4))
check(5, [12 * x**2 - 2, 12 * x**2 - 2 * x, 12 * x**3 - 2, 4 * x**2 - 2], d(4 * x**3 - 2 * x))
check(6, [5 / (2 * sp.sqrt(x)), 5 * sp.sqrt(x) / 2, 1 / (2 * sp.sqrt(x)), 10 * sp.sqrt(x)],
      d(5 * sp.sqrt(x)))
check(7, [2 * x**3 + 3 / x**2, 2 * x**3 - 3 / x**2, 2 * x**3 + 3 / x, 4 * x**3 + 3 / x**2],
      d(x**4 / 2 - 3 / x))
check(8, [4 * x, 6 * x**2 - 1, 4 * x - 1, 2 * x], d(sp.simplify((2 * x**3 - x) / x)))
check(9, [3 * x**2 - 2 * x + 3, 2 * x, 3 * x**2 + 3, 2 * x**2 - 2 * x + 3],
      d((x**2 + 3) * (x - 1)))
check(10, [12, 24, 30, 36], d(6 * x**5 - 3 * x**2 + 9).subs(x, 1))
check(11, [13, 24, 25, 49], d(2 * x**3 + x).subs(x, 2))
check(13, [4, 5, 9, 20], 5 * 4)
check(15, [0, sp.pi**2, 2 * sp.pi, 2 * sp.pi * x], d(sp.pi**2))
check(16, [2 * x / 3 - 6 / x**3, 2 * x / 3 + 6 / x**3, 2 * x / 3 - 6 / x, x / 3 - 6 / x**3],
      d(x**2 / 3 + 3 / x**2))
check(17, [-6, 0, 6, 12], d(2 * x**3 - 6 * x).subs(x, 1))
check(19, [2 * x + 2, 2 * x, 2 * (x + 1) ** 2, x**2 + 2 * x], d((x + 1) ** 2))
check(20, [2 * a * x + b, 2 * a * x + b + c, a * x + b, 2 * a * x], d(a * x**2 + b * x + c))
check(23, [1 / sp.sqrt(x) + 3 / (2 * x ** R(3, 2)),
           1 / sp.sqrt(x) - 3 / (2 * x ** R(3, 2)),
           2 / sp.sqrt(x) + 3 / (2 * x ** R(3, 2)),
           1 / (2 * sp.sqrt(x)) + 3 / (2 * x ** R(3, 2))],
      d(2 * sp.sqrt(x) - 3 / sp.sqrt(x)))

# q12: a linear combination of two derivative values.
f, g = sp.Function("f"), sp.Function("g")
comb = sp.diff(3 * f(x) - 2 * g(x), x).subs(
    {sp.Derivative(f(x), x): 5, sp.Derivative(g(x), x): -2})
check(12, [7, 11, 19, 23], comb)

# q14: adding a constant leaves the derivative alone.
assert sp.diff(f(x) + 7, x) == sp.diff(f(x), x), "q14: constant should drop out"
assert M.QUESTIONS[13]["ans"] == 0 and M.QUESTIONS[13]["choices"][0] == "f'(x)"
checked.add(14)

# q18 and q24: sets of x where the derivative vanishes.
u = sp.Symbol("u", real=True)
z18 = sorted(sp.solve(sp.Eq(sp.diff(u**3 - 3 * u, u), 0), u))
assert z18 == [-1, 1], f"q18: {z18}"
assert M.QUESTIONS[17]["ans"] == 0 and M.QUESTIONS[17]["choices"][0] == "x = -1 and x = 1"
checked.add(18)

z24 = sorted(sp.solve(sp.Eq(sp.diff(u**3 - 6 * u**2 + 9 * u + 1, u), 0), u))
assert z24 == [1, 3], f"q24: {z24}"
assert M.QUESTIONS[23]["ans"] == 0 and M.QUESTIONS[23]["choices"][0] == "x = 1 and x = 3"
checked.add(24)

# q21 and q22: solve for the constants.
k21 = sp.solve(sp.Eq(sp.diff(x**3 + k * x, x).subs(x, 1), 7), k)
assert k21 == [4], f"q21: {k21}"
assert M.QUESTIONS[20]["choices"][M.QUESTIONS[20]["ans"]] == "4"
checked.add(21)

sol22 = sp.solve([sp.Eq((a * x**2 + b * x).subs(x, 1), 3),
                  sp.Eq(sp.diff(a * x**2 + b * x, x).subs(x, 1), 5)], [a, b])
assert sol22 == {a: 2, b: 1}, f"q22: {sol22}"
assert M.QUESTIONS[21]["ans"] == 0 and M.QUESTIONS[21]["choices"][0] == "a = 2, b = 1"
checked.add(22)

# q25's false rule, killed by a single example: with f = g = x,
# d/dx[x * x] = 2x, while f'(x) g'(x) = 1.
assert sp.diff(x * x, x) != sp.diff(x, x) * sp.diff(x, x)

assert len(M.QUESTIONS) == 25, f"expected 25 questions, found {len(M.QUESTIONS)}"
assert checked | CONCEPTUAL == set(range(1, 26)), \
    f"unaccounted questions: {set(range(1, 26)) - checked - CONCEPTUAL}"
assert not (checked & CONCEPTUAL)
for i, item in enumerate(M.QUESTIONS, 1):
    assert len(item["choices"]) == 4 == len(set(item["choices"])), f"q{i}: choices"
print(f"c2_6: {len(checked)} verified with sympy, {len(CONCEPTUAL)} conceptual, 25 total")
