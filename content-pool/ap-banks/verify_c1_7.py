"""Sympy verification for CALC 1.7.

Every limit named anywhere in the module is recomputed, including the ones that
only appear inside a procedure-choice question's stem or rationale — those are
where a wrong claim would otherwise go unchecked, since the key is a sentence
rather than a number.

Infinite limits are matched against sympy's oo / -oo, and "does not exist" keys
are established by showing the two one-sided limits differ.
"""
import sympy as sp

import c1_7

x = sp.Symbol('x', real=True)
Q = c1_7.QUESTIONS

PROCEDURE = {1, 3, 5, 10, 13, 19, 25}


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


# n, expression, approach point, direction, expected value, key text
FINITE = [
    (2,  (x**2 + 1)/(x + 3),                 2,        '+-', 1,                    "1"),
    (4,  (sp.sqrt(16 + x) - 4)/x,            0,        '+-', sp.Rational(1, 8),    "1/8"),
    (8,  x**2*sp.cos(1/x),                   0,        '+-', 0,                    "0"),
    (9,  (3*x**2 + 1)/(2*x**2 - x),          sp.oo,    '-',  sp.Rational(3, 2),    "3/2"),
    (11, (x**2 - 16)/(x**2 - 3*x - 4),       4,        '+-', sp.Rational(8, 5),    "8/5"),
    (12, sp.sin(5*x)/(2*x),                  0,        '+-', sp.Rational(5, 2),    "5/2"),
    (14, 1/x - 1/(x**2 + x),                 0,        '+-', 1,                    "1"),
    (15, (sp.sqrt(x - 1) - 2)/(x - 5),       5,        '+-', sp.Rational(1, 4),    "1/4"),
    (17, (2*x**3 - x)/(5*x**3 + 4),         -sp.oo,    '+',  sp.Rational(2, 5),    "2/5"),
    (18, (sp.exp(2*x) - 1)/x,                0,        '+-', 2,                    "2"),
    (20, (x**3 - 1)/(x**2 - 1),              1,        '+-', sp.Rational(3, 2),    "3/2"),
    (21, sp.sin(x)/(x - sp.pi),              sp.pi,    '+-', -1,                   "-1"),
    (22, (sp.cos(x) - 1)/x,                  0,        '+-', 0,                    "0"),
    (24, (1 - sp.cos(x))/sp.sin(x),          0,        '+-', 0,                    "0"),
]

INFINITE = [
    (6,  (x + 1)/(x - 3), 3, '+', sp.oo,  "infinity"),
    (7,  (x + 1)/(x - 3), 3, '-', -sp.oo, "-infinity"),
    (16, sp.log(x),       0, '+', -sp.oo, "-infinity"),
]


def main():
    structural()

    for n, expr, at, direction, want, want_text in FINITE:
        got = sp.limit(expr, x, at, direction)
        assert sp.simplify(got - want) == 0, f"q{n}: sympy gives {got}, key claims {want}"
        assert key(n) == want_text, f"q{n}: key text {key(n)!r}"

    for n, expr, at, direction, want, want_text in INFINITE:
        got = sp.limit(expr, x, at, direction)
        assert got == want, f"q{n}: sympy gives {got}, key claims {want}"
        assert key(n) == want_text, f"q{n}: key text {key(n)!r}"

    # q23  (x^2 - 4)/|x - 2| has opposite one-sided limits
    a23 = (x**2 - 4)/sp.Abs(x - 2)
    assert (sp.limit(a23, x, 2, '-'), sp.limit(a23, x, 2, '+')) == (-4, 4)
    assert key(23) == "the limit does not exist"

    # --- claims made inside the procedure-choice items ------------------------

    # q1  substitution is legitimate because the denominator's limit is not 0
    assert sp.limit(x + 3, x, 2, '+-') == 5 != 0
    assert key(1).startswith("Direct substitution")

    # q3  the 0/0 form is real, and cancelling gives 2
    assert ((x**2 - 1)/(x - 1)).subs(x, 1) is sp.nan
    assert sp.limit((x**2 - 1)/(x - 1), x, 1, '+-') == 2
    assert key(3).startswith("factor the numerator")

    # q5  numerator -> 4, denominator -> 0, and the sides really do differ
    assert sp.limit(x + 1, x, 3, '+-') == 4
    assert sp.limit(x - 3, x, 3, '+-') == 0
    assert sp.limit((x + 1)/(x - 3), x, 3, '-') is -sp.oo
    assert sp.limit((x + 1)/(x - 3), x, 3, '+') is sp.oo
    assert key(5).startswith("examine the one-sided limits separately")

    # q10  exactly one of the four choices survives substitution
    candidates = [
        ((x - 4)/(x**2 - 16), 4),
        ((x**2 - 1)/(x - 1), 1),
        ((x**2 + 2)/(x + 3), 1),
        (sp.sin(x)/x, 0),
    ]
    substitutable = [i for i, (e, at) in enumerate(candidates)
                     if e.subs(x, at) is not sp.nan]
    assert substitutable == [2], substitutable
    assert key(10) == "lim as x -> 1 of (x^2 + 2)/(x + 3)"
    assert sp.limit((x**2 + 2)/(x + 3), x, 1, '+-') == sp.Rational(3, 4)

    # q13  |x - 2|/(x - 2): the two sides are 1 and -1 as the rationale says
    a13 = sp.Abs(x - 2)/(x - 2)
    assert (sp.limit(a13, x, 2, '-'), sp.limit(a13, x, 2, '+')) == (-1, 1)
    assert key(13).startswith("rewrite the absolute value piecewise")

    # q19  x sin(1/x) is squeezed to 0 by -|x| and |x|
    assert sp.limit(-sp.Abs(x), x, 0, '+-') == 0 and sp.limit(sp.Abs(x), x, 0, '+-') == 0
    assert sp.limit(x*sp.sin(1/x), x, 0, '+-') == 0
    assert key(19).startswith("The squeeze theorem")

    # q25  the true limit is 2, not the 1 the student reported
    assert sp.limit((x**2 - 1)/(x - 1), x, 1, '+-') == 2
    assert key(25).startswith("0/0 is an indeterminate form")

    print(f"c1_7: 25 questions, {len(FINITE) + len(INFINITE) + 1} limits verified "
          f"with sympy plus the claims inside {len(PROCEDURE)} procedure items. OK")


if __name__ == "__main__":
    main()
