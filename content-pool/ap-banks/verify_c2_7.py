"""sympy verification for CALC 2.7.

Choices are transcribed as sympy expressions in module order and compared
against sp.diff. Questions 19 and 20 are conceptual: q19 is the dropped minus
sign in d/dx[cos x] (the correct derivative is confirmed below), and q20 is
the domain x > 0 on which ln(x), and therefore its derivative formula, is
defined.
"""
import importlib
import sympy as sp

M = importlib.import_module("c2_7")
x = sp.Symbol("x", positive=True)
h = sp.Symbol("h")
a, b = sp.symbols("a b")

CONCEPTUAL = {19, 20}
checked = set()
R = sp.Rational


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


sin, cos, exp, log = sp.sin, sp.cos, sp.exp, sp.log

check(1, [cos(x), -cos(x), sin(x), -sin(x)], d(sin(x)))
check(2, [-sin(x), sin(x), cos(x), -cos(x)], d(cos(x)))
check(3, [exp(x), x * exp(x - 1), exp(x - 1), exp(x) / x], d(exp(x)))
check(4, [1 / x, log(x), -1 / x**2, x * log(x) - x], d(log(x)))
check(5, [3 * cos(x), 3 * sin(x), -3 * cos(x), cos(x)], d(3 * sin(x)))
check(6, [2 * sin(x), -2 * sin(x), 2 * cos(x), -2 * cos(x)], d(-2 * cos(x)))
check(7, [cos(x) - sin(x), cos(x) + sin(x), sin(x) - cos(x), -sin(x) - cos(x)],
      d(sin(x) + cos(x)))
check(8, [4 * exp(x) - 5 / x, 4 * exp(x) - 5 * x, 4 * x * exp(x - 1) - 5 / x,
          4 * exp(x) + 5 / x], d(4 * exp(x) - 5 * log(x)))
check(9, [2 / x + 2 * x, 2 / x + x**2, 2 * x + 2 * x, 2 * log(x) + 2 * x],
      d(2 * log(x) + x**2))
check(10, [-1, 0, 1, R(1, 2)], d(sin(x)).subs(x, sp.pi / 2))
check(11, [-sp.sqrt(3) / 2, R(-1, 2), R(1, 2), sp.sqrt(3) / 2], d(cos(x)).subs(x, sp.pi / 3))
check(12, [0, 1, sp.E, 1 / sp.E], d(exp(x)).subs(x, 0))
check(13, [R(1, 2), 2, log(2), R(-1, 4)], d(log(x)).subs(x, 2))
check(14, [sp.E + 1, sp.E, 1, sp.E - 1], d(exp(x) + log(x)).subs(x, 1))
check(15, [-1, 0, 1, sp.pi], d(sin(x)).subs(x, 0))
check(21, [0, sp.E, exp(x), 1], d(sp.E))
check(22, [cos(x) / 2 - 3 * exp(x), cos(x) / 2 - 3 * exp(x) + 7, -sin(x) / 2 - 3 * exp(x),
           cos(x) / 2 - 3 * x * exp(x - 1)], d(sin(x) / 2 - 3 * exp(x) + 7))
check(25, [R(-1, 2), R(1, 2), sp.sqrt(2) / 2, sp.sqrt(3) / 2],
      sp.limit((sin(sp.pi / 6 + h) - sin(sp.pi / 6)) / h, h, 0))

# q16, q17: tangent lines, built from the derivative rather than transcribed.
t16 = d(exp(x)).subs(x, 0) * (x - 0) + 1
check(16, [x + 1, x, sp.E * x, x - 1], sp.expand(t16))
t17 = d(log(x)).subs(x, 1) * (x - 1) + 0
check(17, [x - 1, x + 1, x, 1 / x], sp.expand(t17))

# q18, q23: where the tangent has a given slope on [0, 2pi).
u = sp.Symbol("u", real=True)
z18 = sorted(sp.solveset(sp.Eq(sp.diff(sin(u), u), 0), u,
                         sp.Interval.Ropen(0, 2 * sp.pi)))
assert z18 == [sp.pi / 2, 3 * sp.pi / 2], f"q18: {z18}"
assert M.QUESTIONS[17]["ans"] == 0
checked.add(18)

z23 = sorted(sp.solveset(sp.Eq(sp.diff(cos(u), u), 1), u, sp.Interval.Ropen(0, 2 * sp.pi)))
assert z23 == [3 * sp.pi / 2], f"q23: {z23}"
assert M.QUESTIONS[22]["choices"][M.QUESTIONS[22]["ans"]] == "x = 3pi/2"
checked.add(23)

# q24: solve for the two constants.
f24 = a * sin(x) + b * cos(x)
sol24 = sp.solve([sp.Eq(sp.diff(f24, x).subs(x, 0), 3),
                  sp.Eq(sp.diff(f24, x).subs(x, sp.pi / 2), -2)], [a, b])
assert sol24 == {a: 3, b: 2}, f"q24: {sol24}"
assert M.QUESTIONS[23]["ans"] == 0 and M.QUESTIONS[23]["choices"][0] == "a = 3, b = 2"
checked.add(24)

# q19's claim: the derivative of cosine really is -sin, not +sin.
assert sp.diff(cos(x), x) == -sin(x) != sin(x)

assert len(M.QUESTIONS) == 25, f"expected 25 questions, found {len(M.QUESTIONS)}"
assert checked | CONCEPTUAL == set(range(1, 26)), \
    f"unaccounted questions: {set(range(1, 26)) - checked - CONCEPTUAL}"
assert not (checked & CONCEPTUAL)
for i, item in enumerate(M.QUESTIONS, 1):
    assert len(item["choices"]) == 4 == len(set(item["choices"])), f"q{i}: choices"
print(f"c2_7: {len(checked)} verified with sympy, {len(CONCEPTUAL)} conceptual, 25 total")
