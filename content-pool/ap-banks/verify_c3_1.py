"""sympy verification for CALC 3.1.

Choices are transcribed as sympy expressions in module order and compared
against sp.diff; the composite-function questions read their values from
c3_1.TAB. Every check also confirms the "dropped the inner derivative"
distractor is genuinely different from the key, which is the whole point of
the topic.

Conceptual questions (1, 14): the statement of the chain rule and the missing
factor of 4 in d/dx[sin(4x)] (confirmed below).
"""
import importlib
import sympy as sp

M = importlib.import_module("c3_1")
x = sp.Symbol("x", positive=True)

CONCEPTUAL = {1, 14}
checked = set()
R = sp.Rational

T = {int(r[0]): dict(f=sp.Integer(r[1]), fp=sp.Integer(r[2]),
                     g=sp.Integer(r[3]), gp=sp.Integer(r[4]))
     for r in M.TAB["rows"]}

sin, cos, tan, sec, exp, log, sqrt = sp.sin, sp.cos, sp.tan, sp.sec, sp.exp, sp.log, sp.sqrt


def check(n, exprs, true_val):
    item = M.QUESTIONS[n - 1]
    assert len(exprs) == 4 == len(item["choices"]), f"q{n}: expected 4 choices"
    diff = sp.simplify(exprs[item["ans"]] - true_val)
    assert diff == 0, f"q{n}: keyed choice {item['ans']} != computed ({diff})"
    for i in range(4):
        for j in range(i + 1, 4):
            d = sp.simplify(sp.trigsimp(exprs[i] - exprs[j]))
            assert d != 0, f"q{n}: choices {i} and {j} are the same function"
    checked.add(n)


def d(f):
    return sp.diff(f, x)


check(2, [15 * (3 * x + 1) ** 4, 5 * (3 * x + 1) ** 4, 3 * (3 * x + 1) ** 4,
          15 * (3 * x + 1) ** 5], d((3 * x + 1) ** 5))
check(3, [3 * cos(3 * x), cos(3 * x), 3 * cos(x), -3 * cos(3 * x)], d(sin(3 * x)))
check(4, [2 * exp(2 * x), exp(2 * x), 2 * exp(x), exp(2 * x) / 2], d(exp(2 * x)))
check(5, [1 / x, 5 / x, 1 / (5 * x), log(5) / x], d(log(5 * x)))
check(6, [-2 * x * sin(x**2), -sin(x**2), 2 * x * sin(x**2), -2 * x * cos(x**2)],
      d(cos(x**2)))
check(7, [6 * x * (x**2 + 1) ** 2, 3 * (x**2 + 1) ** 2, 6 * (x**2 + 1) ** 2,
          6 * x * (x**2 + 1) ** 3], d((x**2 + 1) ** 3))
check(8, [2 / sqrt(4 * x + 1), 1 / (2 * sqrt(4 * x + 1)), 4 / sqrt(4 * x + 1),
          2 * sqrt(4 * x + 1)], d(sqrt(4 * x + 1)))
check(9, [2 * x * exp(x**2), exp(x**2), 2 * x * exp(2 * x), x**2 * exp(x**2 - 1)],
      d(exp(x**2)))
check(10, [2 * sec(2 * x) ** 2, sec(2 * x) ** 2, 2 * sec(x) ** 2,
           2 * tan(2 * x) * sec(2 * x)], d(tan(2 * x)))
check(11, [2 * x / (x**2 + 1), 1 / (x**2 + 1), 2 * x / (x**2 + 1) ** 2, 1 / (2 * x)],
      d(log(x**2 + 1)))
check(12, [2 * sin(x) * cos(x), 2 * sin(x), 2 * cos(x), -2 * sin(x) * cos(x)],
      d(sin(x) ** 2))
check(13, [-4 * (2 * x - 5) ** -3, -2 * (2 * x - 5) ** -3, 4 * (2 * x - 5) ** -3,
           -4 * (2 * x - 5) ** -1], d((2 * x - 5) ** -2))
check(17, [cos(x) * exp(sin(x)), exp(sin(x)), exp(cos(x)), sin(x) * exp(sin(x))],
      d(exp(sin(x))))
check(18, [x / sqrt(x**2 + 9), 1 / (2 * sqrt(x**2 + 9)), 2 * x / sqrt(x**2 + 9),
           x / (2 * sqrt(x**2 + 9))], d(sqrt(x**2 + 9)))
check(19, [128, 256, 512, 1024], d((x**2 + 3) ** 4).subs(x, 1))
check(20, [-tan(x), tan(x), 1 / cos(x), -1 / cos(x)], d(log(cos(x))))
check(21, [6 * sin(3 * x) * cos(3 * x), 2 * sin(3 * x) * cos(3 * x), 6 * sin(3 * x),
           2 * sin(3 * x)], d(sin(3 * x) ** 2))
check(22, [(6 * x - 1) * exp(3 * x**2 - x), exp(3 * x**2 - x),
           (6 * x - 1) * exp(6 * x - 1), (3 * x**2 - x) * exp(3 * x**2 - x - 1)],
      d(exp(3 * x**2 - x)))
check(23, [-6 * cos(2 * x) ** 2 * sin(2 * x), 3 * cos(2 * x) ** 2,
           -3 * cos(2 * x) ** 2 * sin(2 * x), 6 * cos(2 * x) ** 2 * sin(2 * x)],
      d(cos(2 * x) ** 3))
check(25, [R(3, 5), R(4, 5), R(5, 4), 4], d(sqrt(x**2 + 9)).subs(x, 4))

# --- composite questions from the table ------------------------------------
# Rather than asserting the chain-rule formula, build actual polynomials that
# hit the table's values and slopes at x = 2 and x = 3, then let sympy
# differentiate the real composites f(g(x)) and g(f(x)).
u = sp.Symbol("u")


def fit(conditions):
    """Lowest-degree polynomial matching the given (point, value, slope) data."""
    n = 2 * len(conditions)
    coeffs = sp.symbols(f"a0:{n}")
    p = sum(c * u**i for i, c in enumerate(coeffs))
    eqs = []
    for pt, val, slope in conditions:
        eqs.append(sp.Eq(p.subs(u, pt), val))
        eqs.append(sp.Eq(sp.diff(p, u).subs(u, pt), slope))
    sol = sp.solve(eqs, coeffs, dict=True)[0]
    return sp.expand(p.subs(sol))


F = fit([(2, T[2]["f"], T[2]["fp"]), (3, T[3]["f"], T[3]["fp"])])
G = fit([(2, T[2]["g"], T[2]["gp"]), (3, T[3]["g"], T[3]["gp"])])
for pt in (2, 3):
    assert F.subs(u, pt) == T[pt]["f"] and sp.diff(F, u).subs(u, pt) == T[pt]["fp"]
    assert G.subs(u, pt) == T[pt]["g"] and sp.diff(G, u).subs(u, pt) == T[pt]["gp"]

h15 = sp.diff(F.subs(u, G), u).subs(u, 2)
check(15, [5, 12, 20, 30], h15)
k16 = sp.diff(G.subs(u, F), u).subs(u, 2)
check(16, [24, 18, 12, 6], k16)
assert h15 != k16, "q15 and q16 should differ: composition order matters"

# q24: h(x) = f(x^3) with f'(8) = 2, checked against two unrelated such f.
for f24 in (2 * u, u**2 / 8, 2 * u + (u - 8) ** 2 * sp.cos(u)):
    assert sp.simplify(sp.diff(f24, u).subs(u, 8) - 2) == 0, f"q24 setup: {f24}"
    val = sp.diff(f24.subs(u, u**3), u).subs(u, 2)
    assert sp.simplify(val - 24) == 0, f"q24: got {val} for {f24}"
check(24, [2, 6, 12, 24], 24)

# q14: the missing factor really is 4.
assert sp.diff(sin(4 * x), x) == 4 * cos(4 * x) != cos(4 * x)

assert len(M.QUESTIONS) == 25, f"expected 25 questions, found {len(M.QUESTIONS)}"
assert checked | CONCEPTUAL == set(range(1, 26)), \
    f"unaccounted questions: {set(range(1, 26)) - checked - CONCEPTUAL}"
assert not (checked & CONCEPTUAL)
for i, item in enumerate(M.QUESTIONS, 1):
    assert len(item["choices"]) == 4 == len(set(item["choices"])), f"q{i}: choices"
print(f"c3_1: {len(checked)} verified with sympy, {len(CONCEPTUAL)} conceptual, 25 total")
