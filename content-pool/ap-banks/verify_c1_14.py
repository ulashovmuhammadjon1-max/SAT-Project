"""Sympy verification for CALC 1.14.

vertical_asymptotes() finds the candidate break points (the singularities of the
expression) and keeps only those where a one-sided limit is actually infinite.
That distinction is the whole point of this topic: a zero denominator that the
numerator cancels leaves a hole, not an asymptote, and a count that skips this
step gets q9, q11, q21 and q22 wrong.

The counting questions are checked against that function, not against the key's
arithmetic, and the one-sided limit questions are checked directly.
"""
import sympy as sp
from sympy.calculus.util import continuous_domain

import c1_14

x = sp.Symbol('x', real=True)
R = sp.S.Reals
Q = c1_14.QUESTIONS

DEFINITION = {1, 2, 3, 23, 25}


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


def vertical_asymptotes(expr):
    """The points where expr genuinely has a vertical asymptote.

    Every point missing from the continuous domain is a candidate; a candidate
    is kept only when one of its one-sided limits is infinite, which is what
    separates an asymptote from a removable hole.
    """
    missing = R - continuous_domain(expr, x, R)
    if not isinstance(missing, sp.FiniteSet):
        candidates = [p for p in getattr(missing, "args", []) if p.is_number]
    else:
        candidates = list(missing)
    found = []
    for p in candidates:
        if sp.limit(expr, x, p, '-') in (sp.oo, -sp.oo) or \
           sp.limit(expr, x, p, '+') in (sp.oo, -sp.oo):
            found.append(p)
    return sorted(found, key=lambda v: float(v))


# n, expression, point, direction, expected, key text
ONE_SIDED = [
    (4,  1/(x - 4),                4, '+', sp.oo,  "infinity"),
    (5,  1/(x - 4),                4, '-', -sp.oo, "-infinity"),
    (7,  (x + 1)/(x - 2),          2, '+', sp.oo,  "infinity"),
    (8,  (x + 1)/(x - 2),          2, '-', -sp.oo, "-infinity"),
    (12, sp.log(x),                0, '+', -sp.oo, "lim as x -> 0^+ of ln(x) = -infinity"),
    (14, 1/x**3,                   0, '-', -sp.oo, "-infinity"),
    (15, 1/x**3,                   0, '+', sp.oo,  "infinity"),
    (17, (x**2 + 1)/(x - 1),       1, '+', sp.oo,  "infinity"),
    (18, (x - 5)/(x - 2)**2,       2, '-', -sp.oo, "-infinity"),
    (19, (x**2 - 9)/(x - 3)**2,    3, '+', sp.oo,  "infinity"),
    (20, (x**2 - 1)/(x - 1)**3,    1, '-', sp.oo,  "infinity"),
]


def main():
    structural()

    for n, expr, at, direction, want, want_text in ONE_SIDED:
        got = sp.limit(expr, x, at, direction)
        assert got == want, f"q{n}: sympy gives {got}, key claims {want}"
        assert key(n) == want_text, f"q{n}: key text {key(n)!r}"

    # q6  1/(x - 4)^2 is unbounded upward on BOTH sides
    assert sp.limit(1/(x - 4)**2, x, 4, '-') is sp.oo
    assert sp.limit(1/(x - 4)**2, x, 4, '+') is sp.oo
    assert key(6).startswith("Both one-sided limits are infinity")

    # q9  (x^2 - 4)/(x - 2) has a hole at 2, not an asymptote
    assert vertical_asymptotes((x**2 - 4)/(x - 2)) == []
    assert sp.limit((x**2 - 4)/(x - 2), x, 2, '+-') == 4
    assert key(9).startswith("No, because the factor x - 2 cancels")

    # q10, q11  which zeros of the denominator survive
    assert vertical_asymptotes(1/(x**2 - 9)) == [-3, 3]
    assert key(10) == "x = 3 and x = -3"
    assert vertical_asymptotes((x - 3)/(x**2 - 9)) == [-3]
    assert key(11) == "x = -3 only"

    # q13  tan(x): sampled odd multiples of pi/2 are asymptotes, multiples of pi are not
    for k in range(-3, 4):
        assert sp.tan(x).subs(x, (2*k + 1)*sp.pi/2) is sp.zoo
        assert sp.tan(x).subs(x, k*sp.pi) == 0
    assert key(13) == "at every odd multiple of pi/2"

    # q16  exactly one choice has a vertical asymptote at x = 5
    cands16 = {
        "f(x) = (x - 5)/(x^2 - 25)": (x - 5)/(x**2 - 25),
        "f(x) = (x^2 - 25)/(x - 5)": (x**2 - 25)/(x - 5),
        "f(x) = (x + 5)/(x - 5)": (x + 5)/(x - 5),
        "f(x) = x^2 - 25": x**2 - 25,
    }
    at5 = [label for label, e in cands16.items() if 5 in vertical_asymptotes(e)]
    assert at5 == ["f(x) = (x + 5)/(x - 5)"], at5
    assert key(16) == at5[0]

    # q18, q20  the stems claim the same behavior on both sides; check the other side too
    assert sp.limit((x - 5)/(x - 2)**2, x, 2, '+') is -sp.oo
    assert sp.limit((x**2 - 1)/(x - 1)**3, x, 1, '+') is sp.oo

    # q21, q22, q24  counting asymptotes, holes excluded
    counts = [
        (21, (x - 2)/(x**2 - 4),            1, "1"),
        (22, (x**2 - x - 6)/(x**2 - 4),     1, "1"),
        (24, 1/(x - 1) + 1/(x - 2),         2, "2"),
    ]
    for n, expr, want, want_text in counts:
        got = vertical_asymptotes(expr)
        assert len(got) == want, f"q{n}: found asymptotes at {got}, key says {want}"
        assert key(n) == want_text, f"q{n}: key text {key(n)!r}"

    # the holes in q21 and q22 are real holes, which is why the counts are 1 and not 2
    assert sp.limit((x - 2)/(x**2 - 4), x, 2, '+-') == sp.Rational(1, 4)
    assert sp.limit((x**2 - x - 6)/(x**2 - 4), x, -2, '+-') == sp.Rational(5, 4)

    print(f"c1_14: 25 questions, {len(ONE_SIDED) + 2} one-sided limits verified and "
          f"{2 + 3 + 4} asymptote sets computed with holes excluded; "
          f"{len(DEFINITION)} definition items. OK")


if __name__ == "__main__":
    main()
