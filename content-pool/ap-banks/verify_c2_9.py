"""sympy verification for CALC 2.9.

Choices are transcribed as sympy expressions in module order and compared
against sp.diff; the table questions read their values from c2_9.TAB.

Conceptual questions (1, 2, 16): the statement of the quotient rule, the
reversed-numerator error (checked below as an exact sign flip), and choosing
the quotient that does not simplify first.
"""
import importlib
import sympy as sp

M = importlib.import_module("c2_9")
x = sp.Symbol("x", positive=True)

CONCEPTUAL = {1, 2, 16}
checked = set()
R = sp.Rational

T = {int(r[0]): dict(f=sp.Integer(r[1]), fp=sp.Integer(r[2]),
                     g=sp.Integer(r[3]), gp=sp.Integer(r[4]))
     for r in M.TAB["rows"]}


def check(n, exprs, true_val):
    item = M.QUESTIONS[n - 1]
    assert len(exprs) == 4 == len(item["choices"]), f"q{n}: expected 4 choices"
    diff = sp.simplify(exprs[item["ans"]] - true_val)
    assert diff == 0, f"q{n}: keyed choice {item['ans']} != computed ({diff})"
    for i in range(4):
        for j in range(i + 1, 4):
            assert sp.simplify(exprs[i] - exprs[j]) != 0, f"q{n}: choices {i} and {j} are equivalent"
    checked.add(n)


def d(f):
    return sp.diff(f, x)


sin, cos, exp, log, sqrt = sp.sin, sp.cos, sp.exp, sp.log, sp.sqrt

check(3, [1 / (x + 1) ** 2, -1 / (x + 1) ** 2, 1 / (x + 1), 1], d(x / (x + 1)))
check(4, [(x**2 - 2 * x) / (x - 1) ** 2, (2 * x - x**2) / (x - 1) ** 2,
          (x**2 - 2 * x) / (x - 1), 2 * x], d(x**2 / (x - 1)))
check(5, [(x * cos(x) - sin(x)) / x**2, (sin(x) - x * cos(x)) / x**2,
          (x * cos(x) - sin(x)) / x, cos(x)], d(sin(x) / x))
check(6, [(x * exp(x) - exp(x)) / x**2, (exp(x) - x * exp(x)) / x**2,
          (x * exp(x) - exp(x)) / x, exp(x)], d(exp(x) / x))
check(7, [(1 - log(x)) / x**2, (log(x) - 1) / x**2, 1 / x**2, (1 - log(x)) / x],
      d(log(x) / x))
check(8, [-17 / (2 * x - 5) ** 2, 17 / (2 * x - 5) ** 2, R(3, 2), -17 / (2 * x - 5)],
      d((3 * x + 1) / (2 * x - 5)))
check(9, [-2 * x / (x**2 + 1) ** 2, 2 * x / (x**2 + 1) ** 2, -2 * x / (x**2 + 1),
          -1 / (2 * x)], d(1 / (x**2 + 1)))
check(10, [-4 * x / (x**2 - 1) ** 2, 4 * x / (x**2 - 1) ** 2, -4 * x / (x**2 - 1), 1],
      d((x**2 + 1) / (x**2 - 1)))
check(12, [(-x * sin(x) - 2 * cos(x)) / x**3, (-x * sin(x) + 2 * cos(x)) / x**3,
           (x * sin(x) - 2 * cos(x)) / x**3, -sin(x) / (2 * x)], d(cos(x) / x**2))
check(13, [R(1, 4), R(1, 2), 1, 2], d(x / (x + 1)).subs(x, 1))
check(14, [-2, 0, 1, 2], d(2 * x / (x**2 + 1)).subs(x, 0))
check(15, [-15 / x**4, 15 / x**4, -15 / x**2, -5 / (3 * x**2)], d(5 / x**3))
check(17, [2 * x + 2, 2 * x + 4, 3 * x**2, 2 * x],
      sp.simplify(d(sp.cancel((x**3 - 8) / (x - 2)))))
check(19, [exp(x) / (1 + exp(x)) ** 2, exp(x) / (1 + exp(x)),
           -exp(x) / (1 + exp(x)) ** 2, 1 / (1 + exp(x)) ** 2], d(exp(x) / (1 + exp(x))))
check(21, [0, 1, 2, R(1, 3)], d(sp.cancel((x**2 - 4) / (x + 2))).subs(x, 1))
check(22, [(1 - x) / (2 * sqrt(x) * (x + 1) ** 2), (x - 1) / (2 * sqrt(x) * (x + 1) ** 2),
           (1 - x) / (2 * sqrt(x) * (x + 1)), 1 / (2 * sqrt(x) * (x + 1) ** 2)],
      d(sqrt(x) / (x + 1)))
check(23, [-1 / x**2 - 4 / x**3, 1 / x**2 + 4 / x**3, -1 / x**2 + 4 / x**3, 1 / (2 * x)],
      d((x + 2) / x**2))

# --- table questions -------------------------------------------------------
def quot(a, top="f", bot="g"):
    t, b = T[a][top], T[a][bot]
    tp, bp = T[a][top + "p"], T[a][bot + "p"]
    return sp.Rational(tp * b - t * bp, b**2)


check(11, [R(-10, 3), R(-10, 9), R(-2, 3), R(10, 3)], quot(2))
check(25, [R(-7, 8), R(5, 8), R(7, 8), R(7, 4)], quot(1))
check(24, [R(-11, 8), R(-7, 8), R(-11, 4), R(11, 8)], quot(3, top="g", bot="f"))

u = sp.Symbol("u", positive=True)
fu = sp.Function("f")
h20 = sp.diff(fu(u) / u**2, u).subs(
    {sp.Derivative(fu(u), u): T[2]["fp"], fu(u): T[2]["f"], u: 2})
check(20, [-2, R(-1, 2), R(1, 2), 2], sp.simplify(h20))

# q18: horizontal tangents of y = x/(x^2 + 1).
v = sp.Symbol("v", real=True)
z18 = sorted(sp.solve(sp.Eq(sp.diff(v / (v**2 + 1), v), 0), v))
assert z18 == [-1, 1], f"q18: {z18}"
assert M.QUESTIONS[17]["ans"] == 0 and M.QUESTIONS[17]["choices"][0] == "x = -1 and x = 1"
checked.add(18)

# q2: reversing the numerator really does negate the derivative.
f, g = sp.Function("f")(x), sp.Function("g")(x)
right = (sp.diff(f, x) * g - f * sp.diff(g, x)) / g**2
wrong = (f * sp.diff(g, x) - sp.diff(f, x) * g) / g**2
assert sp.simplify(wrong + right) == 0, "q2: the reversed form should be the negative"

assert len(M.QUESTIONS) == 25, f"expected 25 questions, found {len(M.QUESTIONS)}"
assert checked | CONCEPTUAL == set(range(1, 26)), \
    f"unaccounted questions: {set(range(1, 26)) - checked - CONCEPTUAL}"
assert not (checked & CONCEPTUAL)
for i, item in enumerate(M.QUESTIONS, 1):
    assert len(item["choices"]) == 4 == len(set(item["choices"])), f"q{i}: choices"
print(f"c2_9: {len(checked)} verified with sympy, {len(CONCEPTUAL)} conceptual, 25 total")
