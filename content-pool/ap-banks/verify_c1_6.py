"""Sympy verification for CALC 1.6.

Each computational stem's expression is written out here and its limit taken
with dir='+-', so a wrong key or a mistyped expression fails rather than
passing quietly.  Numeric distractors are also compared as numbers, not as
strings, because two differently written choices can be the same value.

Questions 5, 11 and 25 ask which manipulation to use rather than for a value;
q20's key is "the limit does not exist" and is verified by showing the two
one-sided limits differ.
"""
import sympy as sp

import c1_6

x = sp.Symbol('x', real=True)
Q = c1_6.QUESTIONS

TECHNIQUE = {5, 11, 25}


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


def distractors_distinct(n):
    """Choices that name numbers must be pairwise unequal as numbers."""
    vals = []
    for c in Q[n - 1]["choices"]:
        if c.startswith("the limit"):
            continue
        vals.append(sp.nsimplify(c))
    for i in range(len(vals)):
        for j in range(i + 1, len(vals)):
            assert sp.simplify(vals[i] - vals[j]) != 0, \
                f"q{n}: two choices are the same number"


CASES = [
    # n,  expression,                                    at,  value
    (1,  (x**2 - 25)/(x - 5),                            5,   10),
    (2,  (x**2 + x - 6)/(x + 3),                        -3,   -5),
    (3,  (x**2 - 3*x + 2)/(x**2 - 1),                    1,   sp.Rational(-1, 2)),
    (4,  (x - 4)/(x**2 - 16),                            4,   sp.Rational(1, 8)),
    (6,  (sp.sqrt(x + 4) - 2)/x,                         0,   sp.Rational(1, 4)),
    (7,  (x - 9)/(sp.sqrt(x) - 3),                       9,   6),
    (8,  (sp.sqrt(1 + x) - sp.sqrt(1 - x))/x,            0,   1),
    (9,  (1/(x + 3) - sp.Rational(1, 3))/x,              0,   sp.Rational(-1, 9)),
    (10, (1/x - sp.Rational(1, 2))/(x - 2),              2,   sp.Rational(-1, 4)),
    (12, (x**3 - 27)/(x - 3),                            3,   27),
    (13, (x**3 + 8)/(x + 2),                            -2,   12),
    (14, (x**4 - 1)/(x - 1),                             1,   4),
    (15, sp.sin(2*x)/x,                                  0,   2),
    (16, sp.sin(3*x)/sp.sin(5*x),                        0,   sp.Rational(3, 5)),
    (17, (1 - sp.cos(x))/x**2,                           0,   sp.Rational(1, 2)),
    (18, sp.tan(x)/(3*x),                                0,   sp.Rational(1, 3)),
    (19, (2 - sp.sqrt(x))/(4 - x),                       4,   sp.Rational(1, 4)),
    (21, (sp.sqrt(x) - 1)/(x - 1),                       1,   sp.Rational(1, 2)),
    (22, x**2/(1 - sp.cos(x)),                           0,   2),
    (23, (x**2 - 1)/(x**2 + 3*x + 2),                   -1,   -2),
    (24, ((2 + x)**3 - 8)/x,                             0,   12),
]


def main():
    structural()

    for n, expr, at, want in CASES:
        got = sp.limit(expr, x, at, '+-')
        assert sp.simplify(got - want) == 0, f"q{n}: sympy gives {got}, key claims {want}"
        assert sp.simplify(sp.nsimplify(key(n)) - want) == 0, \
            f"q{n}: key text {key(n)!r} does not equal {want}"
        distractors_distinct(n)

    # q20  the absolute value survives every cancellation; the sides disagree
    a20 = (x - 2)/sp.Abs(x - 2)
    left, right = sp.limit(a20, x, 2, '-'), sp.limit(a20, x, 2, '+')
    assert (left, right) == (-1, 1)
    assert key(20) == "the limit does not exist"

    # q5   the cancelled expression agrees with the original away from x = 3
    orig = (x**2 - 9)/(x - 3)
    assert sp.simplify(orig - (x + 3)) == 0
    assert orig.subs(x, 3) is sp.nan and (x + 3).subs(x, 3) == 6
    assert key(5).startswith("the limit depends only on values of x near 3")

    # q11  combining over a common denominator does expose a factor of x
    combined = sp.cancel(sp.together(1/(x + 4) - sp.Rational(1, 4))/x)
    assert sp.simplify(combined - (-1/(4*(x + 4)))) == 0
    assert sp.limit((1/(x + 4) - sp.Rational(1, 4))/x, x, 0, '+-') == sp.Rational(-1, 16)
    assert key(11).startswith("Combine the two fractions")

    # q25  the conjugate really does clear the numerator to x
    conj = sp.simplify((sp.sqrt(x + 25) - 5)*(sp.sqrt(x + 25) + 5))
    assert sp.simplify(conj - x) == 0
    assert sp.limit((sp.sqrt(x + 25) - 5)/x, x, 0, '+-') == sp.Rational(1, 10)
    assert key(25).startswith("multiply the numerator and the denominator")

    print(f"c1_6: 25 questions, {len(CASES) + 1} limits verified with sympy, "
          f"{len(TECHNIQUE)} technique-choice items checked structurally. OK")


if __name__ == "__main__":
    main()
