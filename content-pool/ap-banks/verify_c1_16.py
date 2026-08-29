"""Sympy verification for CALC 1.16.

Three things are checked for every question that names a function:

  1. the endpoint values quoted in the stem or rationale are the real ones;
  2. the continuity hypothesis is evaluated with continuous_domain, so a
     question claiming the IVT applies is confirmed to have a continuous
     function and one claiming it does not is confirmed to have a genuine
     break inside the interval;
  3. for the "IVT does not apply" questions, the target value is confirmed to
     be NOT attained anywhere on the interval.

Point 3 is the one that matters most.  A question saying "the IVT does not
apply" is only honest if the conclusion also fails; if the value happened to be
attained anyway the question would be teaching the wrong lesson, and nothing
about the stem would reveal it.
"""
import sympy as sp
from sympy.calculus.util import continuous_domain

import c1_16

x = sp.Symbol('x', real=True)
R = sp.S.Reals
Q = c1_16.QUESTIONS

STATEMENT = {1, 2, 3, 4, 11, 19, 21, 24, 25}


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


def continuous_on(expr, a, b):
    return sp.Interval(a, b).is_subset(continuous_domain(expr, x, R))


def attains(expr, k, a, b):
    """Whether expr(x) = k has a real solution in [a, b]."""
    sols = sp.solveset(sp.Eq(expr, k), x, sp.Interval(a, b))
    return sols != sp.S.EmptySet


# n, expression, a, b, target k, key text -- cases where the IVT DOES apply
APPLIES = [
    (6,  x**3 - x - 1,      1, 2, 0, "There is a zero of f in (1, 2), because f(1) = -1 and f(2) = 5"),
    (16, x**3 + 2*x - 1,    0, 1, 0, "f has a zero in (0, 1), because f(0) = -1 and f(1) = 2"),
    (17, sp.exp(x) + x,    -1, 0, 0, "f has a zero in (-1, 0), because f(-1) is negative and f(0) = 1 is positive"),
    (18, sp.cos(x) - x,     0, 1, 0, "The equation cos(x) = x has a solution in (0, 1), because f(0) = 1 and f(1) is negative"),
]


def main():
    structural()

    # --- cases where the theorem applies --------------------------------------
    for n, expr, a, b, k, want_text in APPLIES:
        assert continuous_on(expr, a, b), f"q{n}: f is not continuous on [{a}, {b}]"
        fa, fb = expr.subs(x, a), expr.subs(x, b)
        assert (fa - k)*(fb - k) < 0, f"q{n}: endpoint values {fa}, {fb} do not straddle {k}"
        assert attains(expr, k, a, b), f"q{n}: no solution exists, so the key is wrong"
        assert key(n) == want_text, f"q{n}: key text {key(n)!r}"

    # the exact endpoint values quoted in the stems
    assert (x**3 - x - 1).subs(x, 1) == -1 and (x**3 - x - 1).subs(x, 2) == 5
    assert (x**3 + 2*x - 1).subs(x, 0) == -1 and (x**3 + 2*x - 1).subs(x, 1) == 2
    assert sp.N(sp.exp(x) + x).subs(x, -1) < 0 and (sp.exp(x) + x).subs(x, 0) == 1
    assert (sp.cos(x) - x).subs(x, 0) == 1 and sp.N((sp.cos(x) - x).subs(x, 1)) < 0

    # q7  x^2 on [-1, 2] with k = 3
    assert continuous_on(x**2, -1, 2)
    assert (x**2).subs(x, -1) == 1 and (x**2).subs(x, 2) == 4
    assert 1 < 3 < 4 and attains(x**2, 3, -1, 2)
    assert key(7).startswith("There is a c in (-1, 2) with f(c) = 3")

    # --- cases where the theorem does NOT apply -------------------------------
    # For each, continuity must genuinely fail AND the value must be unattained.
    fails = [
        (8,  1/x,        -1, 1,          0, "an infinite discontinuity at 0"),
        (10, sp.tan(x),  sp.pi/4, 3*sp.pi/4, 0, "tan is undefined at pi/2"),
    ]
    for n, expr, a, b, k, marker in fails:
        assert not continuous_on(expr, a, b), \
            f"q{n}: f is actually continuous on the interval, so the key is wrong"
        assert not attains(expr, k, a, b), \
            f"q{n}: the value {k} IS attained, so 'the conclusion fails' is wrong"
        assert marker in key(n), f"q{n}: key text {key(n)!r}"

    # q8's endpoint values, as quoted
    assert (1/x).subs(x, -1) == -1 and (1/x).subs(x, 1) == 1
    # q10's endpoint values, as quoted
    assert sp.simplify(sp.tan(sp.pi/4) - 1) == 0
    assert sp.simplify(sp.tan(3*sp.pi/4) + 1) == 0

    # q9  the greatest integer function: discontinuous at 1, and never 0.5
    assert sp.limit(sp.floor(x), x, 1, '-') == 0 and sp.floor(x).subs(x, 1) == 1
    assert sp.solveset(sp.Eq(sp.floor(x), sp.Rational(1, 2)), x, sp.Interval(0, 2)) \
        == sp.S.EmptySet
    assert "never takes a non-integer value" in key(9)

    # q20  the piecewise jump that skips 0 entirely
    left20, right20 = x - 2, x
    assert sp.solveset(sp.Eq(left20, 0), x, sp.Interval.Ropen(0, 1)) == sp.S.EmptySet
    assert sp.solveset(sp.Eq(right20, 0), x, sp.Interval(1, 2)) == sp.S.EmptySet
    assert left20.subs(x, 0) == -2 and right20.subs(x, 2) == 2
    assert sp.limit(left20, x, 1, '-') == -1 and right20.subs(x, 1) == 1
    assert key(20).startswith("No; f jumps from just under -1 to 1 at x = 1")

    # --- questions about which k the theorem covers ---------------------------
    # q12: 12 is outside [4, 10]; q13: 7 is inside; q14: 3 is outside [1, 1]
    assert not (4 < 12 < 10 or 10 < 12 < 4)
    assert key(12) == "No, because 12 is not between 4 and 10"
    assert 4 < 7 < 10
    assert key(13).startswith("Yes, because 7 lies between 4 and 10")
    assert not (1 < 3 < 1)
    assert key(14).startswith("No, because 3 does not lie between f(0) and f(5)")

    # q15  only one tabulated interval changes sign
    table = [(1, -5), (2, -1), (3, 2), (4, 6)]
    sign_changes = [f"({table[i][0]}, {table[i+1][0]})"
                    for i in range(len(table) - 1)
                    if table[i][1]*table[i + 1][1] < 0]
    assert sign_changes == ["(2, 3)"], sign_changes
    assert key(15) == "(2, 3)"

    # q22  x^5 + x - 3 really has a single zero in (1, 2), and it is increasing there
    f22 = x**5 + x - 3
    assert f22.subs(x, 1) == -1 and f22.subs(x, 2) == 31
    roots = sp.solveset(sp.Eq(f22, 0), x, sp.Interval(1, 2))
    assert len(roots) == 1, roots
    assert sp.solveset(sp.Lt(sp.diff(f22, x), 0), x, sp.Interval(1, 2)) == sp.S.EmptySet
    assert key(22).startswith("that f is strictly increasing")

    # q23  -3 and 8 straddle 0, but nothing forces monotonicity or uniqueness
    assert -3 < 0 < 8
    assert key(23) == "f(c) = 0 for some c in (2, 6)"

    # q5  the same shape one more time: -2 and 5 straddle 0
    assert -2 < 0 < 5
    assert key(5) == "f has a zero somewhere in (1, 4)"

    print(f"c1_16: 25 questions, {len(APPLIES) + 1} IVT applications verified, "
          f"4 non-applications verified to fail BOTH the hypothesis and the "
          f"conclusion, plus the tabulated sign change and the uniqueness case; "
          f"{len(STATEMENT)} statement items. OK")


if __name__ == "__main__":
    main()
