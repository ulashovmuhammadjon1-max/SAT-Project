"""sympy verification for CALC 3.6.

Each question's four choices are transcribed as sympy expressions in module
order and compared against sp.diff taken to the stated order -- second, third,
fourth or, for q11, the 101st, which is computed by actually differentiating
101 times rather than by appealing to the period-4 pattern the answer cites.

Conceptual questions (1, 15): the notation d^2y/dx^2 and what f'' measures.
"""
import importlib
import sympy as sp

M = importlib.import_module("c3_6")
x = sp.Symbol("x", positive=True)
t = sp.Symbol("t", real=True)
n, k = sp.symbols("n k")

CONCEPTUAL = {1, 15}
checked = set()
R = sp.Rational
sin, cos, tan, sec, exp, log, sqrt = sp.sin, sp.cos, sp.tan, sp.sec, sp.exp, sp.log, sp.sqrt


def check(num, exprs, true_val):
    item = M.QUESTIONS[num - 1]
    assert len(exprs) == 4 == len(item["choices"]), f"q{num}: expected 4 choices"
    diff = sp.simplify(sp.trigsimp(exprs[item["ans"]] - true_val))
    assert diff == 0, f"q{num}: keyed choice {item['ans']} != computed ({diff})"
    for i in range(4):
        for j in range(i + 1, 4):
            d = sp.simplify(sp.trigsimp(sp.sympify(exprs[i] - exprs[j])))
            assert d != 0, f"q{num}: choices {i} and {j} are the same expression"
    checked.add(num)


def D(f, order, var=x):
    return sp.diff(f, var, order)


check(2, [12 * x**2, 4 * x**3, 24 * x, 12 * x**3], D(x**4, 2))
check(3, [60 * x**2, 20 * x**3, 120 * x, 60 * x**3], D(x**5, 3))
check(4, [-sin(x), sin(x), cos(x), -cos(x)], D(sin(x), 2))
check(5, [-cos(x), cos(x), sin(x), -sin(x)], D(cos(x), 2))
check(6, [4 * exp(2 * x), 2 * exp(2 * x), exp(2 * x), 8 * exp(2 * x)], D(exp(2 * x), 2))
check(7, [-1 / x**2, 1 / x**2, -1 / x, 2 / x**3], D(log(x), 2))
check(8, [18, 29, 32, 36], D(3 * x**3 - 2 * x**2 + x, 2).subs(x, 2))
check(9, [0, 6, 6 * x, 24], D(x**3, 4))
check(10, [sin(x), -sin(x), cos(x), -cos(x)], D(sin(x), 4))
check(13, [2 / x**3, -2 / x**3, 1 / x**2, -1 / x**2], D(1 / x, 2))
check(14, [(x + 2) * exp(x), (x + 1) * exp(x), (x + 3) * exp(x), x * exp(x)],
      D(x * exp(x), 2))
check(16, [-1 / (4 * x ** R(3, 2)), 1 / (4 * x ** R(3, 2)), -1 / (2 * x ** R(3, 2)),
           1 / (2 * sqrt(x))], D(sqrt(x), 2))
check(17, [n * (n - 1) * x ** (n - 2), n * x ** (n - 1), n**2 * x ** (n - 2),
           (n - 1) * x ** (n - 2)], D(x**n, 2))
check(18, [-27 * exp(-3 * x), 27 * exp(-3 * x), -9 * exp(-3 * x), -3 * exp(-3 * x)],
      D(exp(-3 * x), 3))
check(19, [2 * sec(x) ** 2 * tan(x), sec(x) ** 2, 2 * sec(x) * tan(x),
           -2 * sec(x) ** 2 * tan(x)], D(tan(x), 2))
check(21, [48 * (2 * x + 1) ** 2, 12 * (2 * x + 1) ** 2, 24 * (2 * x + 1) ** 2,
           48 * (2 * x + 1) ** 3], D((2 * x + 1) ** 4, 2))
check(23, [(2 - x**2) * sin(x) + 4 * x * cos(x),
           (2 - x**2) * sin(x) - 4 * x * cos(x),
           2 * sin(x) + 4 * x * cos(x),
           -x**2 * sin(x)], D(x**2 * sin(x), 2))
check(25, [2 / x**3, -2 / x**3, -6 / x**4, 1 / x**2], D(log(x), 3))

# q11: differentiate 101 times for real, rather than trusting the cycle.
d101 = sin(x)
for _ in range(101):
    d101 = sp.diff(d101, x)
check(11, [cos(x), sin(x), -sin(x), -cos(x)], d101)

# q12, q24: acceleration is the second derivative of position.
check(12, [-12, -6, 0, 6], D(t**3 - 6 * t**2 + 9 * t, 2, t).subs(t, 1))

z24 = sorted(sp.solve(sp.Eq(D(t**4 - 4 * t**3, 2, t), 0), t))
assert z24 == [0, 2], f"q24: {z24}"
assert M.QUESTIONS[23]["ans"] == 0 and M.QUESTIONS[23]["choices"][0] == "t = 0 and t = 2"
checked.add(24)

# q20: where the second derivative vanishes.
u = sp.Symbol("u", real=True)
z20 = sorted(sp.solve(sp.Eq(D(u**4 - 6 * u**2, 2, u), 0), u))
assert z20 == [-1, 1], f"q20: {z20}"
assert M.QUESTIONS[19]["ans"] == 0 and M.QUESTIONS[19]["choices"][0] == "x = -1 and x = 1"
checked.add(20)

# q22: the nth derivative of e^(kx), verified for several n rather than asserted.
kk = sp.Symbol("k")
for order in range(1, 7):
    assert sp.simplify(sp.diff(sp.exp(kk * x), x, order) - kk**order * sp.exp(kk * x)) == 0
assert M.QUESTIONS[21]["ans"] == 0 and M.QUESTIONS[21]["choices"][0] == "k^n e^(kx)"
checked.add(22)

# q15: f'' is literally the derivative of f'.
g = sp.Function("g")
assert sp.diff(g(x), x, 2) == sp.diff(sp.diff(g(x), x), x)

assert len(M.QUESTIONS) == 25, f"expected 25 questions, found {len(M.QUESTIONS)}"
assert checked | CONCEPTUAL == set(range(1, 26)), \
    f"unaccounted questions: {set(range(1, 26)) - checked - CONCEPTUAL}"
assert not (checked & CONCEPTUAL)
for i, item in enumerate(M.QUESTIONS, 1):
    assert len(item["choices"]) == 4 == len(set(item["choices"])), f"q{i}: choices"
print(f"c3_6: {len(checked)} verified with sympy, {len(CONCEPTUAL)} conceptual, 25 total")
