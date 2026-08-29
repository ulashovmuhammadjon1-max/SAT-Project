"""Sympy verification for CALC 1.8.

Two kinds of check, matching the two kinds of question:

  * a formula is given -> take the limit directly with sympy;
  * only bounds are given -> confirm the two bounds share a limit (that is what
    licenses the squeeze conclusion), and where the stem asserts the bounds hold
    for *every* real x, confirm with sympy that the inequality really is true
    everywhere, so the hypothesis handed to the student is not itself false.

That second check is the one worth having: a bounds question whose stated
sandwich is impossible would look perfectly reasonable to a reader.
"""
import sympy as sp

import c1_8

x = sp.Symbol('x', real=True)
Q = c1_8.QUESTIONS

STATEMENT = {1, 2, 3, 4, 5}


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


def sandwich_valid_near(lower, upper, at, radius=sp.Rational(1, 2)):
    """No x within `radius` of `at` has upper(x) < lower(x).

    A bounds question whose sandwich crosses is unanswerable — no function can
    satisfy the stated hypothesis — and it reads perfectly plausibly, so this
    is checked rather than eyeballed.  An earlier draft of q10 paired
    2x - 1 with x^2 - 2x + 2, whose gap (x - 1)(x - 3) is negative for every x
    just to the right of 1; this check is what found it.
    """
    bad = sp.solveset(sp.Lt(upper - lower, 0), x, sp.S.Reals)
    window = sp.Interval(at - radius, at + radius)
    return sp.Intersection(bad, window) == sp.S.EmptySet


# n, expression, approach point, direction, value, key text
DIRECT = [
    (6,  x**2*sp.sin(1/x),            0,     '+-', 0, "0"),
    (7,  x*sp.cos(1/x),               0,     '+-', 0, "0"),
    (8,  x**4*sp.cos(2/x),            0,     '+-', 0, "0"),
    (12, sp.sqrt(x)*sp.sin(1/x),      0,     '+',  0, "0"),
    (13, sp.sin(x)/x,                 sp.oo, '-',  0, "0"),
    (14, sp.cos(x)/x**2,              sp.oo, '-',  0, "0"),
    (15, x**2*(3 + sp.sin(1/x)),      0,     '+-', 0, "0"),
    (19, x**3*sp.cos(1/x**2),         0,     '+-', 0, "0"),
    (20, (x - 2)**2*sp.sin(1/(x - 2)), 2,    '+-', 0, "0"),
    (23, (2*x + sp.sin(x))/x,         sp.oo, '-',  2, "2"),
]

# n, lower bound, upper bound, approach point, common limit, key text
BOUNDS = [
    (9,  3*x,                   x**3 + 2,          1, 3, "3"),
    (10, 2*x - 1,               x**2,              1, 1, "1"),
    (16, 5 - 2*sp.Abs(x - 3),   5 + 2*sp.Abs(x - 3), 3, 5, "5"),
    (17, -x**2,                 x**2,              0, 0, "0"),
    (25, 2*x,                   x**2 + 1,          1, 2, "2"),
]


def main():
    structural()

    for n, expr, at, direction, want, want_text in DIRECT:
        got = sp.limit(expr, x, at, direction)
        assert sp.simplify(got - want) == 0, f"q{n}: sympy gives {got}, key claims {want}"
        assert key(n) == want_text, f"q{n}: key text {key(n)!r}"

    for n, lower, upper, at, want, want_text in BOUNDS:
        lo = sp.limit(lower, x, at, '+-')
        hi = sp.limit(upper, x, at, '+-')
        assert lo == hi == want, f"q{n}: bounds tend to {lo} and {hi}, key claims {want}"
        assert key(n) == want_text, f"q{n}: key text {key(n)!r}"
        assert sandwich_valid_near(lower, upper, at), \
            f"q{n}: the stated bounds cross near x = {at}, so no function satisfies them"

    # q16, q17 and q25 assert their sandwich for EVERY real x, so the inequality
    # has to hold everywhere, not merely near the point.
    for n, lower, upper in [(16, 5 - 2*sp.Abs(x - 3), 5 + 2*sp.Abs(x - 3)),
                            (17, -x**2, x**2),
                            (25, 2*x, x**2 + 1)]:
        gap = sp.simplify(upper - lower)
        assert sp.solveset(sp.Lt(gap, 0), x, sp.S.Reals) == sp.S.EmptySet, \
            f"q{n}: the stated bounds cross somewhere, so no function can satisfy them"

    # q25's bounds meet only at x = 1, which is what makes the question work
    assert sp.solveset(sp.Eq(x**2 + 1, 2*x), x, sp.S.Reals) == sp.FiniteSet(1)

    # q11  the stated sandwich for sin(x)/x has a common limit of 1
    assert sp.limit(1 - x**2/6, x, 0, '+-') == 1
    assert sp.limit(sp.sin(x)/x, x, 0, '+-') == 1
    assert key(11) == "lim as x -> 0 of sin(x)/x = 1"

    # q18  -x^2 <= f <= x^2 pins f(0) as well as the limit
    assert (-x**2).subs(x, 0) == 0 and (x**2).subs(x, 0) == 0
    assert key(18) == "f(0) = 0 and lim as x -> 0 of f(x) = 0"

    # q21  the squeeze conclusion ignores f(4); constant bounds make that concrete
    assert sp.limit(7 - sp.Abs(x - 4), x, 4, '+-') == 7
    assert sp.limit(7 + sp.Abs(x - 4), x, 4, '+-') == 7
    assert key(21) == "7"

    # q22  sin(1/x) has no shrinking factor and genuinely has no limit at 0,
    # while the other three choices are all squeezed to 0.
    osc = sp.limit(sp.sin(1/x), x, 0, '+')
    assert isinstance(osc, sp.AccumBounds) and (osc.min, osc.max) == (-1, 1)
    for other in [x**2*sp.sin(1/x), x*sp.cos(1/x), x**3*sp.sin(1/x)]:
        assert sp.limit(other, x, 0, '+-') == 0
    assert key(22) == "sin(1/x)"

    # q24  e^(sin(1/x)) is bounded by 1/e and e, so x^2 times it is squeezed
    for bound in [x**2/sp.E, sp.E*x**2]:
        assert sp.limit(bound, x, 0, '+-') == 0
    assert sp.limit(x**2*sp.exp(sp.sin(1/x)), x, 0, '+-') == 0
    assert key(24) == "0"

    # q5  the correct sandwich for x^2 sin(1/x): the gap is nonnegative both ways
    assert sp.solveset(sp.Lt(x**2 - (-x**2), 0), x, sp.S.Reals) == sp.S.EmptySet
    assert key(5) == "-x^2 <= x^2 sin(1/x) <= x^2"

    print(f"c1_8: 25 questions, {len(DIRECT)} limits taken directly, "
          f"{len(BOUNDS)} bound pairs checked for a common limit, "
          f"3 sandwiches checked for consistency, {len(STATEMENT)} statement items. OK")


if __name__ == "__main__":
    main()
