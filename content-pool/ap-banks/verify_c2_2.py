"""sympy verification for CALC 2.2.

Each computational question's four choices are transcribed as sympy
expressions in module order; the true value is computed independently, from
the limit definition itself wherever the question asks for it. The check
confirms the keyed choice equals the computed value and that no two choices
are equivalent. Conceptual questions are listed in CONCEPTUAL.
"""
import importlib
import sympy as sp

M = importlib.import_module("c2_2")
x, h, a = sp.symbols("x h a")
xp = sp.Symbol("x", positive=True)
DNE = sp.Symbol("DNE")  # placeholder for the "does not exist" choice

CONCEPTUAL = {1, 2, 3, 4, 12, 13, 20}
checked = set()


def check(n, exprs, true_val):
    item = M.QUESTIONS[n - 1]
    assert len(exprs) == 4 == len(item["choices"]), f"q{n}: expected 4 choices"
    diff = sp.simplify(exprs[item["ans"]] - true_val)
    assert diff == 0, f"q{n}: keyed choice {item['ans']} != computed value ({diff})"
    for i in range(4):
        for j in range(i + 1, 4):
            assert sp.simplify(exprs[i] - exprs[j]) != 0, f"q{n}: choices {i} and {j} are equivalent"
    checked.add(n)


def deriv_def(f, var=x):
    """The derivative straight from the limit definition."""
    return sp.simplify(sp.limit((f.subs(var, var + h) - f) / h, h, 0))


R = sp.Rational

check(5, [2 * x, x, 2, x**2], deriv_def(x**2))
check(6, [3, 5, 3 * x, 3 * x + 5], deriv_def(3 * x + 5))
check(7, [2, 4, 8, 16], deriv_def(x**2).subs(x, 4))
check(8, [5, 32, 80, 160], sp.limit(((2 + h) ** 5 - 32) / h, h, 0))
check(9, [3, R(1, 2), R(1, 3), R(1, 6)], sp.limit((sp.sqrt(9 + h) - 3) / h, h, 0))
check(10, [0, 1, 2, 3], sp.limit((x**3 - 1) / (x - 1), x, 1))
check(11, [-sp.sqrt(3) / 2, sp.sqrt(3) / 2, R(-1, 2), R(1, 2)],
      sp.limit((sp.cos(sp.pi / 3 + h) - sp.cos(sp.pi / 3)) / h, h, 0))
check(14, [-1 / x**2, 1 / x**2, -1 / x, sp.log(x)], deriv_def(1 / x))
check(15, [2 * a - 3, 2 * a, a**2 - 3, 2 * a + 3], deriv_def(x**2 - 3 * x).subs(x, a))
check(16, [2 * x + h, 2 * x, 2 * x + h + 1, 2 * x * h + h**2],
      sp.simplify(((x + h) ** 2 + 1 - (x**2 + 1)) / h))
check(17, [3 * x**2 + 3 * x * h + h**2, 3 * x**2, 3 * x**2 + h**2, x**3 + 3 * x**2 * h],
      sp.simplify(((x + h) ** 3 - x**3) / h))
check(18, [0, 1, sp.E, DNE], sp.limit((sp.exp(h) - 1) / h, h, 0))
check(19, [0, 1, sp.E, sp.log(2)], sp.limit(sp.log(1 + h) / h, h, 0))
check(21, [0, 3, 6, 9], sp.limit(((3 + h) ** 2 - 9) / h, h, 0))
check(24, [1 / (2 * sp.sqrt(xp)), 2 * sp.sqrt(xp), 1 / sp.sqrt(xp), -1 / (2 * sp.sqrt(xp))],
      sp.simplify(sp.limit((sp.sqrt(xp + h) - sp.sqrt(xp)) / h, h, 0)))
check(25, [R(3, 2), 3, 8, 12], sp.limit((x ** R(3, 2) - 8) / (x - 4), x, 4))

# q22 and q23 hold for every differentiable f, so they are verified against
# several unrelated functions with the stated derivative value rather than one.
F22 = [4 * x, 2 * x**2 - 4 * x, x**3 - 8 * x, 4 * x + (x - 2) ** 2 * sp.sin(x)]
for f in F22:
    assert sp.diff(f, x).subs(x, 2) == 4, f"q22 setup: {f} does not have f'(2) = 4"
    assert sp.limit((f.subs(x, 2 + 3 * h) - f.subs(x, 2)) / h, h, 0) == 12, f"q22 fails for {f}"
check(22, [R(4, 3), 3, 4, 12], 12)

F23 = [7 * x, x**7, 7 * sp.log(x), 7 * x + (x - 1) ** 2 * sp.cos(x)]
for f in F23:
    assert sp.diff(f, x).subs(x, 1) == 7, f"q23 setup: {f} does not have f'(1) = 7"
    val = sp.limit((f.subs(x, 1 + h) - f.subs(x, 1 - h)) / (2 * h), h, 0)
    assert sp.simplify(val - 7) == 0, f"q23 fails for {f}"
check(23, [0, R(7, 2), 7, 14], 7)

assert len(M.QUESTIONS) == 25, f"expected 25 questions, found {len(M.QUESTIONS)}"
assert checked | CONCEPTUAL == set(range(1, 26)), \
    f"unaccounted questions: {set(range(1, 26)) - checked - CONCEPTUAL}"
assert not (checked & CONCEPTUAL)
print(f"c2_2: {len(checked)} verified with sympy, {len(CONCEPTUAL)} conceptual, 25 total")
