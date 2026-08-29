"""sympy verification for CALC 2.8.

Choices are transcribed as sympy expressions in module order and compared
against sp.diff. The table-based questions read their values from c2_8.TAB,
so the numbers graded are the numbers a student sees.

Conceptual questions (1, 10, 20): the statement of the product rule, the
counterexample that kills d/dx[fg] = f'g' (checked below), and recognizing the
one product that cannot be simplified before differentiating.
"""
import importlib
import sympy as sp

M = importlib.import_module("c2_8")
x = sp.Symbol("x", positive=True)

CONCEPTUAL = {1, 10, 20}
checked = set()

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

check(2, [2 * x * sin(x) + x**2 * cos(x), 2 * x * cos(x),
          2 * x * sin(x) - x**2 * cos(x), x**2 * cos(x) + 2 * x * cos(x)],
      d(x**2 * sin(x)))
check(3, [exp(x) + x * exp(x), x * exp(x), exp(x), exp(x) - x * exp(x)], d(x * exp(x)))
check(4, [log(x) + 1, 1 / x, log(x) + x, log(x) / x], d(x * log(x)))
check(5, [5 * x**4 + 3 * x**2 - 4 * x, 6 * x**3, 5 * x**4 - 3 * x**2 - 4 * x,
          5 * x**4 + 3 * x**2 + 4 * x], d((x**2 + 1) * (x**3 - 2)))
check(6, [cos(x) ** 2 - sin(x) ** 2, -sin(x) * cos(x),
          cos(x) ** 2 + sin(x) ** 2, sin(x) ** 2 - cos(x) ** 2], d(sin(x) * cos(x)))
check(7, [exp(x) * log(x) + exp(x) / x, exp(x) / x,
          exp(x) * log(x) - exp(x) / x, exp(x) / x + log(x)], d(exp(x) * log(x)))
check(8, [6 * x * exp(x) + 3 * x**2 * exp(x), 6 * x * exp(x), 3 * x**2 * exp(x),
          6 * x * exp(x) - 3 * x**2 * exp(x)], d(3 * x**2 * exp(x)))
check(11, [3 * x**2 * cos(x) - x**3 * sin(x), 3 * x**2 * cos(x) + x**3 * sin(x),
           -3 * x**2 * sin(x), 3 * x**2 * sin(x) - x**3 * cos(x)], d(x**3 * cos(x)))
check(12, [exp(x) / (2 * sqrt(x)) + sqrt(x) * exp(x), exp(x) / (2 * sqrt(x)),
           sqrt(x) * exp(x), exp(x) / (2 * sqrt(x)) - sqrt(x) * exp(x)],
      d(sqrt(x) * exp(x)))
check(13, [4 * x - 5, 2 * x - 6, 2, 4 * x - 6], d((2 * x + 1) * (x - 3)))
check(15, [2 * x * log(x) + x, 2 * x * log(x), 2 / x, 2 * x * log(x) + 1],
      d(x**2 * log(x)))
check(16, [-sp.pi, -1, 0, sp.pi], d(x * sin(x)).subs(x, sp.pi))
check(17, [3 * x**2 + 12 * x + 11, 3 * x**2 + 6 * x + 11, 1, 3 * x**2 + 12 * x + 6],
      d((x + 1) * (x + 2) * (x + 3)))
check(18, [exp(x) * sin(x) + exp(x) * cos(x), exp(x) * cos(x),
           exp(x) * sin(x) - exp(x) * cos(x), exp(x) * cos(x) - exp(x) * sin(x)],
      d(exp(x) * sin(x)))
check(21, [0, 1, 2, sp.E], d(x**2 * exp(x)).subs(x, 0))
check(23, [cos(x) * log(x) + sin(x) / x, cos(x) / x,
           cos(x) * log(x) - sin(x) / x, cos(x) * log(x) + sin(x) * log(x)],
      d(sin(x) * log(x)))

# q24: the tangent line at the origin, built from the derivative.
t24 = d(x * exp(x)).subs(x, 0) * x + 0
check(24, [x, x + 1, sp.Integer(0), sp.E * x], sp.expand(t24))

# --- table questions: the product rule applied to the stored values --------
def prod_rule(a):
    return T[a]["fp"] * T[a]["g"] + T[a]["f"] * T[a]["gp"]


check(9, [-5, 7, 11, 12], prod_rule(2))
check(19, [-2, 3, 18, 20], prod_rule(3))

u = sp.Symbol("u", positive=True)
fu, gu = sp.Function("f"), sp.Function("g")
h14 = sp.diff(u**2 * fu(u), u).subs(
    {sp.Derivative(fu(u), u): T[1]["fp"], fu(u): T[1]["f"], u: 1})
check(14, [-4, 2, 4, 6], h14)

f22 = sp.diff(u * gu(u), u).subs(
    {sp.Derivative(gu(u), u): T[2]["gp"], gu(u): T[2]["g"], u: 2})
check(22, [5, 9, 14, 20], f22)

# q25: horizontal tangents of y = x^2 e^x.
v = sp.Symbol("v", real=True)
z25 = sorted(sp.solve(sp.Eq(sp.diff(v**2 * sp.exp(v), v), 0), v))
assert z25 == [-2, 0], f"q25: {z25}"
assert M.QUESTIONS[24]["ans"] == 0 and M.QUESTIONS[24]["choices"][0] == "x = 0 and x = -2"
checked.add(25)

# q10's counterexample: with f = g = x the false rule gives 1, not 2x.
assert sp.diff(x * x, x) == 2 * x and sp.diff(x, x) * sp.diff(x, x) == 1

assert len(M.QUESTIONS) == 25, f"expected 25 questions, found {len(M.QUESTIONS)}"
assert checked | CONCEPTUAL == set(range(1, 26)), \
    f"unaccounted questions: {set(range(1, 26)) - checked - CONCEPTUAL}"
assert not (checked & CONCEPTUAL)
for i, item in enumerate(M.QUESTIONS, 1):
    assert len(item["choices"]) == 4 == len(set(item["choices"])), f"q{i}: choices"
print(f"c2_8: {len(checked)} verified with sympy, {len(CONCEPTUAL)} conceptual, 25 total")
