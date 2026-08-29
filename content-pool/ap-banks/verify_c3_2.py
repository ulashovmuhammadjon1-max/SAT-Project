"""sympy verification for CALC 3.2.

Every dy/dx is recomputed with sp.idiff, sympy's implicit differentiator, and
compared against the transcribed choices; the pairwise check catches the trap
that two algebraically different-looking distractors can be the same rational
function (for example (1 - y)/(1 - x) and (y - 1)/(x - 1)).

Conceptual questions (12, 13): when implicit differentiation is the right
tool, and the missing dy/dx factor -- confirmed below by differentiating
y(x)^2 symbolically.
"""
import importlib
import sympy as sp

M = importlib.import_module("c3_2")
x, y = sp.symbols("x y")
dydx = sp.Symbol("dydx")

CONCEPTUAL = {12, 13}
checked = set()
R = sp.Rational
sin, cos, tan, exp, log = sp.sin, sp.cos, sp.tan, sp.exp, sp.log


def check(n, exprs, true_val):
    item = M.QUESTIONS[n - 1]
    assert len(exprs) == 4 == len(item["choices"]), f"q{n}: expected 4 choices"
    diff = sp.simplify(exprs[item["ans"]] - true_val)
    assert diff == 0, f"q{n}: keyed choice {item['ans']} != computed ({diff})"
    for i in range(4):
        for j in range(i + 1, 4):
            d = sp.simplify(sp.trigsimp(exprs[i] - exprs[j]))
            assert d != 0, f"q{n}: choices {i} and {j} are the same expression"
    checked.add(n)


def imp(eq):
    """dy/dx for the relation eq = 0, from sympy's implicit differentiator."""
    return sp.simplify(sp.idiff(eq, y, x))


def at(expr, px, py):
    return sp.simplify(expr.subs({x: px, y: py}))


# q1: the chain-rule factor, taken from sympy's own derivative of y(x)^2.
yf = sp.Function("y")(x)
d_y2 = sp.diff(yf**2, x).subs({sp.Derivative(yf, x): dydx, yf: y})
check(1, [2 * y * dydx, 2 * y, 2 * dydx, y**2 * dydx], d_y2)

circle = x**2 + y**2 - 25
check(2, [-x / y, x / y, -y / x, -x], imp(circle))
check(3, [R(-4, 3), R(-3, 4), R(3, 4), R(4, 3)], at(imp(circle), 3, 4))
check(4, [-y / x, y / x, -x / y, 1 / x], imp(x * y - 6))
check(5, [-(2 * x + y) / x, (2 * x + y) / x, -(2 * x + y) / y, -2 * x / x],
      imp(x**2 + x * y - 4))
check(6, [2 * x / (3 * y**2), 2 * x / (3 * y), 3 * y**2 / (2 * x), 2 * x / 3],
      imp(y**3 - x**2))
check(7, [1 / cos(y), cos(y), 1 / sin(y), -1 / sin(y)], imp(sin(y) - x))
check(8, [1 / x, exp(y), x * exp(y), log(x)],
      sp.simplify(imp(exp(y) - x).subs(exp(y), x)))
check(9, [-2 * y / x, 2 * y / x, -y / (2 * x), -2 * x * y], imp(x**2 * y - 1))
check(10, [(2 * y - x**2) / (y**2 - 2 * x), (x**2 - 2 * y) / (y**2 - 2 * x),
           (2 * y - x**2) / (y**2 + 2 * x), x**2 / y**2],
      imp(x**3 + y**3 - 6 * x * y))
check(11, [R(-3, 8), R(-3, 4), R(3, 8), R(8, 3)],
      at(imp(x**2 + 4 * y**2 - 25), 3, 2))
check(15, [(y - 1) / (1 - x), (1 - y) / (1 - x), (y - 1) / (1 + x), y / x],
      imp(x + y - x * y))
check(16, [sin(x) / (2 * y), -sin(x) / (2 * y), sin(x) / (2 * y**2), -sin(x) / 2],
      imp(cos(x) + y**2 - 5))
check(19, [2 * x * y, 2 * x / y, 2 * x, y / (2 * x)], imp(log(y) - x**2))
check(20, [-2 * y / (3 * x), 2 * y / (3 * x), -3 * y / (2 * x), -2 * y**3 / (3 * x**2)],
      imp(x**2 * y**3 - 8))
check(21, [-tan(y) / x, tan(y) / x, -sin(y) / x, -1 / (x * cos(y))],
      imp(x * sin(y) - 1))
check(22, [-4, R(-1, 4), R(1, 4), 4], at(imp(x**3 + y**3 - 9), 1, 2))
check(23, [R(-2, 3), 0, R(2, 3), R(4, 9)], at(imp(4 * x**2 + 9 * y**2 - 36), 0, 2))
check(25, [R(-2, 3), R(-1, 3), R(1, 3), R(2, 3)], at(imp(x * y**2 - 12), 3, 2))

# q24: (x - y)^2 = 4 forces dy/dx = 1 away from y = x.
s24 = imp(x**2 - 2 * x * y + y**2 - 4)
assert sp.simplify(s24 - 1) == 0, f"q24: idiff gave {s24}"
check(24, [1, -1, 0, x / y], s24)

# q14: the tangent line at (3, 4), built from the implicit slope.
m14 = at(imp(circle), 3, 4)
line14 = sp.expand(3 * x + 4 * (m14 * (x - 3) + 4))
assert sp.simplify(line14 - 25) == 0, "q14: 3x + 4y should be constant 25 on the tangent"
assert M.QUESTIONS[13]["ans"] == 0 and M.QUESTIONS[13]["choices"][0] == "3x + 4y = 25"
checked.add(14)

# q17, q18: horizontal where dy/dx = 0, vertical where it is undefined.
slope = imp(circle)
horiz = sorted([(px, py) for px in (-5, 0, 5) for py in (-5, 0, 5)
                if px**2 + py**2 == 25 and py != 0 and at(slope, px, py) == 0])
assert horiz == [(0, -5), (0, 5)], f"q17: {horiz}"
assert M.QUESTIONS[16]["ans"] == 0
checked.add(17)

vert = sorted([(px, py) for px in (-5, 0, 5) for py in (-5, 0, 5)
               if px**2 + py**2 == 25 and py == 0])
assert vert == [(-5, 0), (5, 0)], f"q18: {vert}"
assert M.QUESTIONS[17]["ans"] == 0
checked.add(18)

# q13's missing factor, stated as an expression rather than as prose.
assert sp.diff(yf**2, x) != 2 * yf

assert len(M.QUESTIONS) == 25, f"expected 25 questions, found {len(M.QUESTIONS)}"
assert checked | CONCEPTUAL == set(range(1, 26)), \
    f"unaccounted questions: {set(range(1, 26)) - checked - CONCEPTUAL}"
assert not (checked & CONCEPTUAL)
for i, item in enumerate(M.QUESTIONS, 1):
    assert len(item["choices"]) == 4 == len(set(item["choices"])), f"q{i}: choices"
print(f"c3_2: {len(checked)} verified with sympy, {len(CONCEPTUAL)} conceptual, 25 total")
