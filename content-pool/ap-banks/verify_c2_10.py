"""sympy verification for CALC 2.10.

Choices are transcribed as sympy expressions in module order and compared
against sp.diff. The pairwise non-equivalence check matters more here than
anywhere else in Unit 2: sec^2(x) - 1, tan^2(x) and sin^2(x)/cos^2(x) are the
same function written three ways, so a careless distractor would silently make
a question unanswerable.

Conceptual questions (5, 15, 21): the quotient-rule derivations of tan and
sec (both re-derived below) and which derivatives carry a minus sign.
"""
import importlib
import sympy as sp

M = importlib.import_module("c2_10")
x = sp.Symbol("x")

CONCEPTUAL = {5, 15, 21}
checked = set()
R = sp.Rational

sin, cos, tan, cot, sec, csc = sp.sin, sp.cos, sp.tan, sp.cot, sp.sec, sp.csc


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


check(1, [sec(x) ** 2, -csc(x) ** 2, sec(x) * tan(x), cot(x)], d(tan(x)))
check(2, [-csc(x) ** 2, csc(x) ** 2, -sec(x) ** 2, -csc(x) * cot(x)], d(cot(x)))
check(3, [sec(x) * tan(x), -sec(x) * tan(x), sec(x) ** 2, csc(x) * cot(x)], d(sec(x)))
check(4, [-csc(x) * cot(x), csc(x) * cot(x), -csc(x) ** 2, -cot(x)], d(csc(x)))
check(6, [3 * sec(x) ** 2, 3 * sec(x) * tan(x), -3 * csc(x) ** 2, sec(x) ** 2],
      d(3 * tan(x)))
check(7, [tan(x) + x * sec(x) ** 2, sec(x) ** 2, tan(x) + sec(x) ** 2, x * sec(x) ** 2],
      d(x * tan(x)))
check(8, [2 * x * sec(x) + x**2 * sec(x) * tan(x), 2 * x * sec(x) * tan(x),
          2 * x * sec(x) - x**2 * sec(x) * tan(x), x**2 * sec(x) * tan(x)],
      d(x**2 * sec(x)))
check(9, [1, sp.sqrt(2), 2, 4], d(tan(x)).subs(x, sp.pi / 4))
check(10, [sp.sqrt(3), 2, 2 * sp.sqrt(3), 4], d(sec(x)).subs(x, sp.pi / 3))
check(11, [-1, 0, 1, 2], d(csc(x)).subs(x, sp.pi / 2))
check(12, [-2, -1, 1, 2], d(cot(x)).subs(x, sp.pi / 4))
check(13, [sec(x) ** 2 - 1, sec(x) ** 2, sec(x) ** 2 + 1, -csc(x) ** 2 - 1],
      d(tan(x) - x))
check(14, [(x * sec(x) * tan(x) - sec(x)) / x**2, (sec(x) - x * sec(x) * tan(x)) / x**2,
           sec(x) * tan(x) / x**2, (x * sec(x) * tan(x) - sec(x)) / x],
      d(sec(x) / x))
check(16, [-5 * csc(x) * cot(x), 5 * csc(x) * cot(x), -5 * csc(x) ** 2,
           -csc(x) * cot(x)], d(5 * csc(x)))
check(17, [(x * sec(x) ** 2 - tan(x)) / x**2, (tan(x) - x * sec(x) ** 2) / x**2,
           sec(x) ** 2, (x * sec(x) ** 2 - tan(x)) / x], d(tan(x) / x))
check(18, [-1, 0, 1, 2], d(tan(x)).subs(x, 0))
check(20, [-csc(x) ** 2 - csc(x) * cot(x), csc(x) ** 2 + csc(x) * cot(x),
           -csc(x) ** 2 + csc(x) * cot(x), -sec(x) ** 2 - sec(x) * tan(x)],
      d(cot(x) + csc(x)))
check(23, [1, sp.sqrt(2), 2, 2 * sp.sqrt(2)], d(sec(x)).subs(x, sp.pi / 4))
check(24, [cot(x) - x * csc(x) ** 2, cot(x) + x * csc(x) ** 2, -csc(x) ** 2,
           cot(x) - csc(x) ** 2], d(x * cot(x)))
check(25, [sec(x) * tan(x) ** 2 + sec(x) ** 3, sec(x) ** 2 * tan(x),
           sec(x) * tan(x) ** 2 - sec(x) ** 3, sec(x) ** 3], d(sec(x) * tan(x)))

# q19: sec^2(x) is never 0, so y = tan(x) has no horizontal tangent.
assert sp.solveset(sp.Eq(d(tan(x)), 0), x, sp.S.Reals) == sp.EmptySet
assert M.QUESTIONS[18]["choices"][M.QUESTIONS[18]["ans"]] == "no value of x"
checked.add(19)

# q22: sec^2(x) = 2 on [0, pi/2).
z22 = sorted(sp.solveset(sp.Eq(d(tan(x)), 2), x, sp.Interval.Ropen(0, sp.pi / 2)))
assert z22 == [sp.pi / 4], f"q22: {z22}"
assert M.QUESTIONS[21]["choices"][M.QUESTIONS[21]["ans"]] == "x = pi/4"
checked.add(22)

# q5 and q21: the two quotient-rule derivations, re-derived rather than asserted.
num_tan = sp.simplify(sp.diff(sin(x), x) * cos(x) - sin(x) * sp.diff(cos(x), x))
assert num_tan == 1, f"q5: numerator simplified to {num_tan}"
assert sp.simplify(d(tan(x)) - sec(x) ** 2) == 0

sec_from_quotient = sp.simplify((sp.diff(1, x) * cos(x) - 1 * sp.diff(cos(x), x)) / cos(x) ** 2)
assert sp.simplify(sec_from_quotient - sin(x) / cos(x) ** 2) == 0
assert sp.simplify(sin(x) / cos(x) ** 2 - sec(x) * tan(x)) == 0, "q21: should equal sec tan"

# q15: exactly cot and csc among the four have negative derivatives at a point
# where every function involved is positive (x = pi/4 lies in the first quadrant).
p = sp.pi / 4
signs = {name: sp.sign(d(f).subs(x, p)) for name, f in
         (("tan", tan(x)), ("cot", cot(x)), ("sec", sec(x)), ("csc", csc(x)))}
assert [k for k, v in signs.items() if v < 0] == ["cot", "csc"], signs

assert len(M.QUESTIONS) == 25, f"expected 25 questions, found {len(M.QUESTIONS)}"
assert checked | CONCEPTUAL == set(range(1, 26)), \
    f"unaccounted questions: {set(range(1, 26)) - checked - CONCEPTUAL}"
assert not (checked & CONCEPTUAL)
for i, item in enumerate(M.QUESTIONS, 1):
    assert len(item["choices"]) == 4 == len(set(item["choices"])), f"q{i}: choices"
print(f"c2_10: {len(checked)} verified with sympy, {len(CONCEPTUAL)} conceptual, 25 total")
