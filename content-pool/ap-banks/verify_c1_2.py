"""Sympy verification for CALC 1.2.

One-sided limits use dir='-' and dir='+'; a two-sided limit is checked with
dir='+-', which raises when the two sides disagree — that raise is itself the
evidence for the "does not exist" keys.
"""
import sympy as sp

import c1_2

x = sp.Symbol('x', real=True)
Q = c1_2.QUESTIONS

CONCEPTUAL = {1, 2, 3, 4, 5, 19, 22, 25}


def key(n):
    item = Q[n - 1]
    return item["choices"][item["ans"]]


def structural():
    assert len(Q) == 25, f"expected 25 questions, found {len(Q)}"
    for i, item in enumerate(Q, 1):
        assert len(item["choices"]) == 4, f"q{i}: needs exactly 4 choices"
        assert len(set(item["choices"])) == 4, f"q{i}: duplicate choice text"
        assert 0 <= item["ans"] < 4, f"q{i}: bad answer index"
    stems = [item["q"] for item in Q]
    assert len(set(stems)) == len(stems), "duplicate stem inside the module"


def two_sided_fails(expr, at):
    """True when the two one-sided limits exist but disagree."""
    left = sp.limit(expr, x, at, '-')
    right = sp.limit(expr, x, at, '+')
    return left != right, left, right


def branch_limit(piece, branch, at, direction):
    """One-sided limit of a Piecewise, taken through its governing branch.

    sympy's limit() ignores `dir` on a Piecewise (it returns the same value on
    both sides of a jump), so the branch that actually governs the approach is
    identified numerically first — the Piecewise is sampled at points marching
    toward `at` from the given side and must agree with `branch` at each — and
    the limit is then taken of that branch alone.
    """
    step = sp.Rational(1, 10)
    for _ in range(6):
        pt = at - step if direction == '-' else at + step
        assert piece.subs(x, pt) == branch.subs(x, pt), \
            f"branch does not govern the {direction} side at {pt}"
        step /= 10
    return sp.limit(branch, x, at, direction)


def main():
    structural()

    # q6
    assert sp.limit((x**2 - 9)/(x - 3), x, 3, '+-') == 6
    assert key(6) == "6"

    # q7, q8, q9  piecewise 2x + 1 (x < 1), 5 - x (x >= 1)
    f = sp.Piecewise((2*x + 1, x < 1), (5 - x, True))
    left = branch_limit(f, 2*x + 1, 1, '-')
    right = branch_limit(f, 5 - x, 1, '+')
    assert left == 3 and key(7) == "3"
    assert right == 4 and key(8) == "4"
    assert left != right, "q9 claims the two-sided limit fails"
    assert key(9) == "does not exist"

    # q10, q11  |x|/x at 0
    assert sp.limit(sp.Abs(x)/x, x, 0, '-') == -1
    assert key(10) == "-1"
    differ, left, right = two_sided_fails(sp.Abs(x)/x, 0)
    assert differ and (left, right) == (-1, 1)
    assert key(11) == "does not exist"

    # q12
    assert sp.limit(x**2 - 5, x, 3, '+-') == 4
    assert key(12) == "4"

    # q13
    assert sp.limit((x**2 + 2*x)/x, x, 0, '+-') == 2
    assert key(13) == "2"

    # q14  piecewise x^2 (x <= 2), 4 (x > 2) — the two sides agree here
    g = sp.Piecewise((x**2, x <= 2), (4, True))
    assert branch_limit(g, x**2, 2, '-') == 4
    assert branch_limit(g, sp.Integer(4), 2, '+') == 4
    assert key(14) == "4"

    # q15, q16
    assert sp.limit(sp.Integer(7), x, 2, '+-') == 7
    assert key(15) == "7"
    assert sp.limit(3*x + 2, x, -1, '+-') == -1
    assert key(16) == "-1"

    # q17  1/x from the right grows without bound
    assert sp.limit(1/x, x, 0, '+') is sp.oo
    assert key(17).startswith("It does not exist")

    # q18  the assigned value f(1) = 7 does not affect the limit
    assert sp.limit((x**2 - 1)/(x - 1), x, 1, '+-') == 2
    assert key(18) == "2"

    # q20  (x - 1)/|x - 1|
    differ, left, right = two_sided_fails((x - 1)/sp.Abs(x - 1), 1)
    assert differ and (left, right) == (-1, 1)
    assert key(20).startswith("The limit does not exist")

    # q21  sin(1/x) oscillates; sympy reports the bounded oscillation directly
    osc = sp.limit(sp.sin(1/x), x, 0, '+')
    assert isinstance(osc, sp.AccumBounds) and (osc.min, osc.max) == (-1, 1)
    assert key(21).startswith("The limit does not exist")

    # q23
    assert sp.limit((x**2 - 4)/(x + 2), x, -2, '+-') == -4
    assert key(23) == "-4"

    # q24  |x - 3|/(x - 3) from the right
    assert sp.limit(sp.Abs(x - 3)/(x - 3), x, 3, '+') == 1
    assert sp.limit(sp.Abs(x - 3)/(x - 3), x, 3, '-') == -1
    assert key(24) == "1"

    checked = set(range(1, 26)) - CONCEPTUAL
    print(f"c1_2: 25 questions, {len(checked)} sympy-verified, "
          f"{len(CONCEPTUAL)} conceptual. OK")


if __name__ == "__main__":
    main()
