"""sympy verification for CALC 2.1.

For every computational question the four answer choices are transcribed as
sympy expressions in the order they appear in the module, the true value is
computed independently (difference quotients and sp.diff, never re-typed from
the key), and the check confirms:
  * the choice at index `ans` equals the computed value, and
  * the four choices are pairwise non-equivalent, so no distractor is
    accidentally a second correct answer.
Conceptual questions carry no sympy check and are listed in CONCEPTUAL.
"""
import importlib
import sympy as sp

M = importlib.import_module("c2_1")
x, t, h, a, m, b, p, q, c = sp.symbols("x t h a m b p q c")

CONCEPTUAL = {1, 6, 7, 10, 14, 24}
checked = set()


def check(n, exprs, true_val):
    item = M.QUESTIONS[n - 1]
    assert len(exprs) == 4 == len(item["choices"]), f"q{n}: expected 4 choices"
    diff = sp.simplify(sp.expand(exprs[item["ans"]] - true_val))
    assert diff == 0, f"q{n}: keyed choice {item['ans']} != computed value ({diff})"
    for i in range(4):
        for j in range(i + 1, 4):
            assert sp.simplify(exprs[i] - exprs[j]) != 0, f"q{n}: choices {i} and {j} are equivalent"
    checked.add(n)


def aroc(f, var, lo, hi):
    return sp.simplify((f.subs(var, hi) - f.subs(var, lo)) / (hi - lo))


R = sp.Rational

check(2, [2, 5, R(17, 2), 15], aroc(x**2, x, 1, 4))
check(3, [25, 21, 7, -2], aroc(x**3 - 2 * x, x, 0, 3))
check(4, [-1, R(-3, 4), R(-1, 4), R(1, 4)], aroc(1 / x, x, 1, 4))
check(5, [5, 1, R(1, 4), R(1, 5)], aroc(sp.sqrt(x), x, 4, 9))

s1 = t**2 + 3 * t
check(8, [24, 11, 8, 5], aroc(s1, t, 1, 4))
check(9, [2, 4, 5, 8], sp.diff(s1, t).subs(t, 1))

check(11, [3 / sp.log(4), 3 / sp.log(2), 3, 4 / sp.log(4)],
      aroc(sp.exp(x), x, 0, sp.log(4)))
check(12, [2 / sp.pi, 1, sp.pi / 2, 0], aroc(sp.sin(x), x, 0, sp.pi / 2))
check(13, [12, 11, 4, 3], (17 - 5) / sp.Integer(6 - 2))
check(15, [2 + h, 2, h, 2 * h + h**2], aroc(x**2, x, 1, 1 + h))
check(16, [2, R(5, 2), 3, 5],
      sp.solve(sp.Eq(sp.diff(x**2, x).subs(x, c), aroc(x**2, x, 1, 4)), c)[0])
check(17, [16, 12, 4, 0], aroc(x**3, x, -2, 2))
check(18, [80, 9, 8, 7], aroc(200 + 5 * q + R(1, 10) * q**2, q, 10, 20))
check(19, [m, b, m * p + b, (m + b) / 2], aroc(m * x + b, x, p, q))
check(20, [2 / (sp.E**2 - 1), 2, 2 / sp.E**2, 1 / (sp.E**2 - 1)],
      aroc(sp.log(x), x, 1, sp.E**2))
check(21, [-9, 0, 3, 9], aroc(t**3 - 6 * t**2 + 9 * t, t, 0, 3))
check(22, [R(1, 4), R(-1, 4), R(-1, 2), -2], sp.diff(1 / x, x).subs(x, 2))
check(23, [16, 8, 4, 2], (84 - 68) / sp.Integer(7 - 3))
check(25, [2 * a + 3, 2 * a + 1, 2 * a + 5, 4 * a + 6], aroc(x**2 + x, x, a, a + 2))

assert len(M.QUESTIONS) == 25, f"expected 25 questions, found {len(M.QUESTIONS)}"
assert checked | CONCEPTUAL == set(range(1, 26)), \
    f"unaccounted questions: {set(range(1, 26)) - checked - CONCEPTUAL}"
assert not (checked & CONCEPTUAL)
print(f"c2_1: {len(checked)} verified with sympy, {len(CONCEPTUAL)} conceptual, 25 total")
