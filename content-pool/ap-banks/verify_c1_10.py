"""Sympy verification for CALC 1.10.

classify() derives the type of a discontinuity from the two one-sided limits and
the function's value, and every classification key in the module is compared
against what classify() returns.  Nothing here restates the label the module
already claims — the label is the thing under test.

The classification rules used are the standard ones:
    infinite   at least one one-sided limit is +/- infinity
    jump       both one-sided limits are finite but unequal
    removable  the two-sided limit exists but the value is missing or different
    continuous the two-sided limit exists and equals f(c)
    oscillating neither one-sided limit exists at all
"""
import sympy as sp

import c1_10

x = sp.Symbol('x', real=True)
Q = c1_10.QUESTIONS

DEFINITION = {1, 2, 3, 17, 23}


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


def classify(expr, at, value=None):
    """Type of the discontinuity of expr at x = at, decided from limits."""
    left = sp.limit(expr, x, at, '-')
    right = sp.limit(expr, x, at, '+')
    if isinstance(left, sp.AccumBounds) or isinstance(right, sp.AccumBounds):
        return "oscillating"
    if left in (sp.oo, -sp.oo) or right in (sp.oo, -sp.oo):
        return "infinite"
    if sp.simplify(left - right) != 0:
        return "jump"
    actual = expr.subs(x, at) if value is None else value
    if actual is sp.nan or sp.simplify(actual - left) != 0:
        return "removable"
    return "not a discontinuity"


# n, expression, point, assigned value (None = read it off the expression), key
CASES = [
    (4,  (x**2 - 4)/(x - 2),               2,  None, "removable"),
    (5,  1/(x - 3),                        3,  None, "infinite"),
    (6,  sp.Abs(x)/x,                      0,  None, "jump"),
    (7,  (x - 1)/(x**2 - 1),               1,  None, "removable"),
    (8,  (x - 1)/(x**2 - 1),              -1,  None, "infinite"),
    (12, sp.tan(x),                        sp.pi/2, None, "infinite"),
    (13, 1/x**2,                           0,  None, "infinite"),
    (15, (x**2 - 9)/(x**2 - 3*x),          3,  None, "removable"),
    (16, (x**2 - 9)/(x**2 - 3*x),          0,  None, "infinite"),
    (20, (x + 2)/(x**2 - 4),              -2,  None, "removable"),
    (21, (x**2 - 5*x + 6)/(x**2 - 4),      2,  None, "removable"),
    (22, (x**2 - 5*x + 6)/(x**2 - 4),     -2,  None, "infinite"),
    (24, sp.Abs(x - 1)/(x**2 - 1),         1,  None, "jump"),
]


def main():
    structural()

    for n, expr, at, value, want in CASES:
        got = classify(expr, at, value)
        assert got == want, f"q{n}: classify says {got}, key says {want}"
        assert key(n) == want, f"q{n}: key text {key(n)!r}"

    # q9  piecewise x^2 (x < 2), x + 3 (x >= 2): a jump of 4 -> 5
    assert sp.limit(x**2, x, 2, '-') == 4 and sp.limit(x + 3, x, 2, '+') == 5
    assert key(9) == "jump"

    # q10  x + 1 off 3 with f(3) = 7: limit 4, value 7
    assert classify(x + 1, 3, value=sp.Integer(7)) == "removable"
    assert key(10) == "removable"

    # q11  the value that removes the hole in (x^2 - x - 6)/(x - 3)
    assert sp.limit((x**2 - x - 6)/(x - 3), x, 3, '+-') == 5
    assert key(11) == "5"

    # q14  sin(1/x) fits none of the three categories
    assert classify(sp.sin(1/x), 0, value=sp.Integer(0)) == "oscillating"
    assert key(14).startswith("none of removable, jump, or infinite")

    # q18  exactly one of the four choices jumps at 0
    cands18 = {
        "f(x) = x^2/x": (x**2/x, None),
        "f(x) = 1/x": (1/x, None),
        "f(x) = x/|x|": (x/sp.Abs(x), None),
        "f(x) = x sin(1/x) with f(0) = 0": (x*sp.sin(1/x), sp.Integer(0)),
    }
    jumps = [label for label, (e, v) in cands18.items() if classify(e, 0, v) == "jump"]
    assert jumps == ["f(x) = x/|x|"], jumps
    assert key(18) == jumps[0]

    # q19  the greatest integer function steps by 1 at each integer
    floor_left = sp.limit(sp.floor(x), x, 3, '-')
    floor_right = sp.limit(sp.floor(x), x, 3, '+')
    assert (floor_left, floor_right) == (2, 3)
    assert key(19) == "jump"

    # q25  (x^2 - 1)/(x^3 - x) reduces to 1/x: two removable, one infinite
    f25 = (x**2 - 1)/(x**3 - x)
    assert sp.simplify(sp.cancel(f25) - 1/x) == 0
    kinds = {at: classify(f25, at) for at in (-1, 0, 1)}
    assert kinds == {-1: "removable", 0: "infinite", 1: "removable"}, kinds
    assert sum(1 for v in kinds.values() if v == "removable") == 2
    assert key(25) == "2"

    print(f"c1_10: 25 questions, {len(CASES) + 7} classifications derived from "
          f"one-sided limits and compared with the keys, "
          f"{len(DEFINITION)} definition items. OK")


if __name__ == "__main__":
    main()
