"""Sympy verification for CALC 1.12.

For each function named in a stem, sympy's continuous_domain is computed over
the reals and compared with the interval the key claims.  That is a stronger
check than recomputing a limit at one point: it catches a key that omits a
break point as well as one that invents an extra restriction.

sympy returns e.g. Union(Interval.open(-oo, 2), Interval.open(2, oo)) for
1/(x - 2), and Interval(5, oo) for sqrt(x - 5) — note the closed left endpoint,
which is exactly the [5, infinity) versus (5, infinity) distinction several
questions turn on.
"""
import sympy as sp
from sympy.calculus.util import continuous_domain

import c1_12

x = sp.Symbol('x', real=True)
R = sp.S.Reals
Q = c1_12.QUESTIONS

DEFINITION = {1, 2, 11, 13, 14, 15}


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


def dom(expr):
    return continuous_domain(expr, x, R)


# n, expression, the domain the key describes, key text
DOMAINS = [
    (3,  3*x**5 - 2*x + 7,       R,
     "all real numbers"),
    (4,  1/(x - 2),              R - sp.FiniteSet(2),
     "(-infinity, 2) and (2, infinity)"),
    (6,  sp.sqrt(x - 5),         sp.Interval(5, sp.oo),
     "[5, infinity)"),
    (7,  sp.sqrt(9 - x**2),      sp.Interval(-3, 3),
     "[-3, 3]"),
    (8,  sp.log(x),              sp.Interval.open(0, sp.oo),
     "(0, infinity)"),
    (10, sp.exp(x),              R,
     "all real numbers"),
    (12, 1/(x**2 + 1),           R,
     "all real numbers"),
    (18, sp.Abs(x),              R,
     "all real numbers"),
    (19, (x**2 - 1)/(x - 1),     R - sp.FiniteSet(1),
     "(-infinity, 1) and (1, infinity)"),
    (20, sp.sqrt(x)/(x - 4),     sp.Union(sp.Interval.Ropen(0, 4),
                                          sp.Interval.open(4, sp.oo)),
     "[0, 4) and (4, infinity)"),
    (21, 1/sp.sqrt(x - 1),       sp.Interval.open(1, sp.oo),
     "(1, infinity)"),
    (22, sp.log(x - 2),          sp.Interval.open(2, sp.oo),
     "(2, infinity)"),
    (24, (x - 3)/(x**2 - 9),     R - sp.FiniteSet(-3, 3),
     "(-infinity, -3) and (-3, 3) and (3, infinity)"),
]


def main():
    structural()

    for n, expr, expected, want_text in DOMAINS:
        got = dom(expr)
        assert got == expected, f"q{n}: continuous_domain is {got}, key describes {expected}"
        assert key(n) == want_text, f"q{n}: key text {key(n)!r}"

    # q5  the break points of (x + 1)/((x - 3)(x + 4))
    breaks5 = R - dom((x + 1)/((x - 3)*(x + 4)))
    assert breaks5 == sp.FiniteSet(-4, 3), breaks5
    assert key(5) == "x = 3 and x = -4"

    # q9  tan(x) breaks exactly at the odd multiples of pi/2.
    # The symbolic form of solveset(cos(x)) varies between sympy versions, so
    # this samples instead: every odd multiple of pi/2 must be a break, and the
    # multiples of pi named by a distractor must not be.
    for k in range(-4, 5):
        odd = (2*k + 1)*sp.pi/2
        assert sp.cos(odd) == 0, f"cos is not 0 at {odd}"
        assert sp.tan(x).subs(x, odd) is sp.zoo, f"tan is finite at {odd}"
        whole = k*sp.pi
        assert sp.tan(x).subs(x, whole) == 0, f"tan should be defined at {whole}"
    assert sp.tan(x).subs(x, 1) not in (sp.zoo, sp.nan)   # an integer is not a break
    assert key(9) == "at every odd multiple of pi/2, where cos(x) = 0"

    # q16  the piecewise seam at 2 matches from both sides
    assert sp.limit(x**2, x, 2, '-') == 4 and sp.limit(sp.Integer(4), x, 2, '+') == 4
    assert (x**2).subs(x, 2) == 4
    assert key(16).startswith("Yes, because the two rules agree at the seam")

    # q17  the piecewise seam at 3 does not
    assert sp.limit(x + 1, x, 3, '-') == 4 and (2*x).subs(x, 3) == 6
    assert key(17) == "No, because the left limit at 3 is 4 while g(3) = 6"

    # q23  sin(x)/(x^2 - 4): only the zeros of the denominator break it
    breaks23 = R - dom(sp.sin(x)/(x**2 - 4))
    assert breaks23 == sp.FiniteSet(-2, 2), breaks23
    assert key(23) == "at x = 2 and x = -2"

    # q25  exactly one of the four choices is continuous on all of [0, 2]
    cands25 = {
        "f(x) = 1/(x - 1)": 1/(x - 1),
        "f(x) = (x^2 - x)/(x - 1)": (x**2 - x)/(x - 1),
        "f(x) = sqrt(4 - x^2)": sp.sqrt(4 - x**2),
        "f(x) = 1/(x - 2)": 1/(x - 2),
    }
    target = sp.Interval(0, 2)
    good = [label for label, e in cands25.items() if target.is_subset(dom(e))]
    assert good == ["f(x) = sqrt(4 - x^2)"], good
    assert key(25) == good[0]

    print(f"c1_12: 25 questions, {len(DOMAINS) + 3} continuous domains computed "
          f"with sympy and matched against the keys, plus 2 piecewise seams; "
          f"{len(DEFINITION)} definition items. OK")


if __name__ == "__main__":
    main()
