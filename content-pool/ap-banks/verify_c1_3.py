"""Sympy verification for CALC 1.3.

There are no figures in this bank, so each stem describes a graph precisely.
Here every described graph is written down as an explicit function and its
limits are recomputed, which is what makes the descriptions checkable at all.

One-sided limits of piecewise graphs go through branch_limit(): sympy's limit()
ignores `dir` on a Piecewise, so the governing branch is confirmed numerically
on the correct side first and the limit is taken of that branch.
"""
import sympy as sp

import c1_3

x = sp.Symbol('x', real=True)
Q = c1_3.QUESTIONS

# These reason about graphs in general, not one described function.
CONCEPTUAL = {10, 19, 22, 23, 25}


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


def branch_limit(piece, branch, at, direction):
    step = sp.Rational(1, 10)
    for _ in range(6):
        pt = at - step if direction == '-' else at + step
        assert piece.subs(x, pt) == branch.subs(x, pt), \
            f"branch does not govern the {direction} side at {pt}"
        step /= 10
    return sp.limit(branch, x, at, direction)


def main():
    structural()

    # q1, q2  open circle at (2, 3), solid dot at (2, 5): model as x + 1 off 2.
    f12 = sp.Piecewise((5, sp.Eq(x, 2)), (x + 1, True))
    assert branch_limit(f12, x + 1, 2, '-') == 3
    assert branch_limit(f12, x + 1, 2, '+') == 3
    assert key(1) == "3"
    assert f12.subs(x, 2) == 5 and key(2) == "5"

    # q3, q4  jump: left piece ends at the open circle (1, 4), right starts at (1, -1)
    g = sp.Piecewise((3*x + 1, x < 1), (x - 2, True))
    left, right = branch_limit(g, 3*x + 1, 1, '-'), branch_limit(g, x - 2, 1, '+')
    assert (left, right) == (4, -1)
    assert key(3) == "the limit does not exist"
    assert key(4) == "4"

    # q5  the line y = 2x + 1 with the point at x = 4 removed
    assert sp.limit(2*x + 1, x, 4, '+-') == 9
    assert key(5) == "9"

    # q6  the hole in the graph of (x^2 - 16)/(x - 4)
    r = (x**2 - 16)/(x - 4)
    assert sp.simplify(r - (x + 4)) == 0
    assert sp.limit(r, x, 4, '+-') == 8
    assert key(6) == "(4, 8)"

    # q7  1/(x - 3)^2 rises without bound on both sides of x = 3
    a7 = 1/(x - 3)**2
    assert sp.limit(a7, x, 3, '-') is sp.oo and sp.limit(a7, x, 3, '+') is sp.oo
    assert key(7).startswith("the limit does not exist")

    # q8  1/(x + 2) falls on the left of -2 and rises on the right
    a8 = 1/(x + 2)
    assert sp.limit(a8, x, -2, '-') is -sp.oo and sp.limit(a8, x, -2, '+') is sp.oo
    assert key(8) == ("lim as x -> -2^- of k(x) = -infinity and "
                      "lim as x -> -2^+ of k(x) = infinity")

    # q9, q10  parabola on the left, dot at (1, 3), line 2 - x on the right
    f9 = sp.Piecewise((x**2, x < 1), (3, sp.Eq(x, 1)), (2 - x, True))
    assert branch_limit(f9, x**2, 1, '-') == 1
    assert branch_limit(f9, 2 - x, 1, '+') == 1
    assert f9.subs(x, 1) == 3
    assert key(9) == "1"

    # q11  |x| at the corner
    assert sp.limit(sp.Abs(x), x, 0, '+-') == 0
    assert key(11) == "0"

    # q12  step function 1 then 2
    step = sp.Piecewise((1, x < 0), (2, True))
    assert branch_limit(step, sp.Integer(1), 0, '-') == 1
    assert branch_limit(step, sp.Integer(2), 0, '+') == 2
    assert key(12) == "the limit does not exist"

    # q13  an oscillation between -1 and 1 with no limiting height
    osc = sp.limit(sp.sin(1/x), x, 0, '+')
    assert isinstance(osc, sp.AccumBounds) and (osc.min, osc.max) == (-1, 1)
    assert key(13) == "the limit does not exist"

    # q14  an unbroken graph through (5, -2)
    f14 = x - 7
    assert f14.subs(x, 5) == -2 and sp.limit(f14, x, 5, '+-') == -2
    assert key(14) == "-2"

    # q15  flat at height 4 on (6, 8)
    assert sp.limit(sp.Integer(4), x, 7, '+-') == 4
    assert key(15) == "4"

    # q16  a hole at x = -3 sitting at height 7, with nothing plotted there.
    # (x^2 - 9)/(x + 3) equals x - 3 away from -3, so adding 13 puts the hole
    # at height (-3) - 3 + 13 = 7 while leaving p undefined at x = -3.
    p = (x**2 - 9)/(x + 3) + 13
    assert sp.simplify(p - (x + 10)) == 0
    assert sp.limit(p, x, -3, '+-') == 7
    assert p.subs(x, -3) is sp.nan, "the model must be genuinely undefined at -3"
    assert key(16) == "p(-3) is undefined and lim as x -> -3 of p(x) = 7"

    # q17  upper semicircle of radius 2, approached from inside the domain
    semi = sp.sqrt(4 - x**2)
    assert sp.limit(semi, x, 2, '-') == 0
    assert key(17) == "0"

    # q18  1/x^2 at 0
    assert sp.limit(1/x**2, x, 0, '-') is sp.oo and sp.limit(1/x**2, x, 0, '+') is sp.oo
    assert key(18).startswith("The limit does not exist as a finite number")

    # q20, q21  segment to (3, 6) solid, segment from the open circle (3, 1)
    f20 = sp.Piecewise((2*x, x <= 3), (x - 2, True))
    assert branch_limit(f20, x - 2, 3, '+') == 1
    assert branch_limit(f20, 2*x, 3, '-') == 6
    assert f20.subs(x, 3) == 6
    assert key(20) == "1"
    assert key(21) == "the limit does not exist"

    # q24  y = x^2 with (1, 1) replaced by (1, 4)
    f24 = sp.Piecewise((4, sp.Eq(x, 1)), (x**2, True))
    assert branch_limit(f24, x**2, 1, '-') == 1
    assert branch_limit(f24, x**2, 1, '+') == 1
    assert f24.subs(x, 1) == 4
    assert key(24) == "lim as x -> 1 of f(x) = 1 and f(1) = 4"

    checked = set(range(1, 26)) - CONCEPTUAL
    print(f"c1_3: 25 questions, {len(checked)} sympy-verified, "
          f"{len(CONCEPTUAL)} conceptual. OK")


if __name__ == "__main__":
    main()
