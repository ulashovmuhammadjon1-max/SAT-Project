"""Sympy verification for CALC 1.13.

Two checks, one per question family:

  * hole questions — take the limit and confirm it equals the key, then confirm
    that assigning that value actually makes all three continuity conditions
    hold (so the answer is verified to *work*, not merely to be the limit);

  * seam questions — solve the matching equation for the parameter with sympy's
    solveset rather than restating the key's arithmetic, confirm the solution is
    unique, and then substitute it back and check both one-sided limits and the
    function's value agree.

q21's key is that no parameter works; that is checked by showing the solution
set of the seam equation is empty because the one-sided limits differ.
"""
import sympy as sp

import c1_13

x, k, a, b, c = sp.symbols('x k a b c', real=True)
Q = c1_13.QUESTIONS

DEFINITION = {1, 2, 25}


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
    heads = [item["q"][:90].lower() for item in Q]
    assert len(set(heads)) == len(heads), "two stems share their opening 90 characters"


# n, expression, hole location, key text
HOLES = [
    (3,  (x**2 - 16)/(x - 4),                4,  "8"),
    (4,  (x**2 - x - 12)/(x - 4),            4,  "7"),
    (5,  (x**3 - 8)/(x - 2),                 2,  "12"),
    (6,  (x - 2)/(x**2 - 4),                 2,  "1/4"),
    (7,  (x**2 - 5*x + 6)/(x**2 - 4),        2,  "-1/4"),
    (8,  (x**2 + 2*x - 3)/(x**2 - 1),        1,  "2"),
    (9,  (sp.sqrt(x) - 3)/(x - 9),           9,  "1/6"),
    (10, (sp.sqrt(x + 4) - 2)/x,             0,  "1/4"),
    (11, sp.sin(3*x)/x,                      0,  "3"),
    (12, (1 - sp.cos(x))/x,                  0,  "0"),
    (13, (sp.exp(x) - 1)/x,                  0,  "1"),
    (14, sp.tan(x)/x,                        0,  "1"),
]

# n, left branch, right branch, seam, parameter, key text
SEAMS = [
    (15, x**2,        k*x,          2,  k, "2"),
    (16, k*x + 1,     x**2 + 1,     3,  k, "3"),
    (17, 3*x + a,     x**2 + 2,     1,  a, "0"),
    (18, a*x**2,      x + 10,       2,  a, "3"),
    (19, 2*x + b,     x**2,        -1,  b, "3"),
    (20, c*x**2 + 1,  4*x - c,      1,  c, "3/2"),
]


def main():
    structural()

    for n, expr, at, want_text in HOLES:
        lim = sp.limit(expr, x, at, '+-')
        want = sp.nsimplify(want_text)
        assert sp.simplify(lim - want) == 0, f"q{n}: limit is {lim}, key claims {want}"
        assert key(n) == want_text, f"q{n}: key text {key(n)!r}"
        # the hole is real: the formula itself has no value there
        assert expr.subs(x, at) in (sp.nan, sp.zoo), \
            f"q{n}: the expression is already defined at {at}, so there is no hole"
        # and assigning the limit really does produce continuity
        filled = sp.Piecewise((want, sp.Eq(x, at)), (expr, True))
        assert sp.limit(expr, x, at, '-') == want == sp.limit(expr, x, at, '+')
        assert filled.subs(x, at) == want

    for n, left, right, seam, param, want_text in SEAMS:
        lhs = sp.limit(left, x, seam, '-')
        rhs = sp.limit(right, x, seam, '+')
        sols = sp.solveset(sp.Eq(lhs, rhs), param, sp.S.Reals)
        want = sp.nsimplify(want_text)
        assert sols == sp.FiniteSet(want), f"q{n}: solveset gives {sols}, key claims {want}"
        assert key(n) == want_text, f"q{n}: key text {key(n)!r}"
        # substitute back: both sides and the seam value must agree
        assert sp.simplify(lhs.subs(param, want) - rhs.subs(param, want)) == 0

    # q21  |x - 3|/(x - 3): the seam equation has no solution at all
    j = sp.Abs(x - 3)/(x - 3)
    left21, right21 = sp.limit(j, x, 3, '-'), sp.limit(j, x, 3, '+')
    assert (left21, right21) == (-1, 1)
    assert sp.solveset(sp.Eq(left21, right21), k, sp.S.Reals) == sp.S.EmptySet
    assert key(21) == "no value of k makes f continuous at 3"

    # q22, q23  the three-piece function: two seam equations, one linear system
    eq1 = sp.Eq(sp.limit(x**2, x, 1, '-'), (a*x + b).subs(x, 1))       # a + b = 1
    eq2 = sp.Eq(sp.limit(a*x + b, x, 2, '-'), sp.limit(sp.Integer(6), x, 2, '+'))
    sol = sp.solve([eq1, eq2], [a, b], dict=True)
    assert len(sol) == 1, sol
    assert sol[0][a] == 5 and sol[0][b] == -4, sol
    assert key(22) == "5" and key(23) == "-4"
    # substituting back, both seams really close
    a_, b_ = sol[0][a], sol[0][b]
    assert (a_*x + b_).subs(x, 1) == 1 == sp.limit(x**2, x, 1, '-')
    assert (a_*x + b_).subs(x, 2) == 6

    # q24  the symbolic hole: (x^2 - a^2)/(x - a) -> 2a
    asym = sp.Symbol('a_pos', positive=True)
    expr24 = (x**2 - asym**2)/(x - asym)
    assert sp.simplify(sp.cancel(expr24) - (x + asym)) == 0
    assert sp.simplify(sp.limit(expr24, x, asym, '+-') - 2*asym) == 0
    assert key(24) == "2a"

    # q25  after filling the hole the function agrees with x + 1 everywhere
    from sympy.calculus.util import continuous_domain
    assert continuous_domain(x + 1, x, sp.S.Reals) == sp.S.Reals
    assert sp.limit((x**2 - 1)/(x - 1), x, 1, '+-') == 2
    assert key(25).startswith("Yes, because the only discontinuity was the hole")

    print(f"c1_13: 25 questions, {len(HOLES)} holes filled and re-checked, "
          f"{len(SEAMS)} seam equations solved with solveset and substituted back, "
          f"1 unsolvable seam, 1 two-parameter system, 1 symbolic hole. OK")


if __name__ == "__main__":
    main()
