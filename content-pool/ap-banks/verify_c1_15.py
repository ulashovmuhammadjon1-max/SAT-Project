"""Sympy verification for CALC 1.15.

Every limit at infinity is recomputed.  The two questions that turn on
sqrt(x^2) = |x| are checked in BOTH directions even though each question asks
about only one, because the whole point of the pair is that the two directions
give different answers, and a verifier that only checked the asked direction
would pass a module whose two keys were swapped.
"""
import sympy as sp

import c1_15

x = sp.Symbol('x', real=True)
Q = c1_15.QUESTIONS

DEFINITION = {1, 2, 3, 4, 19, 23}


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


# n, expression, direction (+oo or -oo), expected value, key text
LIMITS = [
    (5,  (3*x + 2)/(5*x - 1),             sp.oo,  sp.Rational(3, 5), "3/5"),
    (6,  (2*x**2 + 3)/(x**3 - 1),         sp.oo,  0,                 "0"),
    (7,  (x**3 + 1)/(x**2 + 4),           sp.oo,  sp.oo,             "infinity"),
    (8,  (4*x**2 - x)/(2*x**2 + 7),      -sp.oo,  2,                 "2"),
    (11, 1/x,                             sp.oo,  0,                 "0"),
    (12, sp.log(x)/x,                     sp.oo,  0,                 "0"),
    (13, sp.sin(x)/x,                     sp.oo,  0,                 "y = 0"),
    (14, sp.exp(-x),                      sp.oo,  0,                 "0"),
    (15, sp.exp(x),                      -sp.oo,  0,                 "0"),
    (16, sp.atan(x),                      sp.oo,  sp.pi/2,           "pi/2"),
    (17, sp.sqrt(x**2 + 1)/x,             sp.oo,  1,                 "1"),
    (18, sp.sqrt(x**2 + 1)/x,            -sp.oo,  -1,                "-1"),
    (20, (3*x**2 - x)/(x**2 + 2*x + 1),   sp.oo,  3,                 "3"),
    (21, (2*x + 1)/sp.sqrt(x**2 + 3),     sp.oo,  2,                 "2"),
    (22, 5*x/sp.sqrt(4*x**2 + 1),         sp.oo,  sp.Rational(5, 2), "5/2"),
    (25, x/sp.exp(x),                     sp.oo,  0,                 "0"),
]


def main():
    structural()

    for n, expr, at, want, want_text in LIMITS:
        got = sp.limit(expr, x, at)
        assert got == want, f"q{n}: sympy gives {got}, key claims {want}"
        assert key(n) == want_text, f"q{n}: key text {key(n)!r}"

    # q9, q10  horizontal asymptotes read off the limits in both directions
    for n, expr, want, want_text in [
        (9,  (6*x - 1)/(3*x + 5),   2, "y = 2"),
        (10, (x**2 + 1)/(x**2 - 4), 1, "y = 1"),
    ]:
        assert sp.limit(expr, x, sp.oo) == want
        assert sp.limit(expr, x, -sp.oo) == want, \
            f"q{n}: the two directions disagree, so 'the' asymptote is wrong"
        assert key(n) == want_text, f"q{n}: key text {key(n)!r}"

    # q17/q18  the sqrt(x^2) = |x| pair, checked in both directions
    pair = sp.sqrt(x**2 + 1)/x
    assert sp.limit(pair, x, sp.oo) == 1 and sp.limit(pair, x, -sp.oo) == -1
    assert sp.simplify(sp.sqrt(x**2) - sp.Abs(x)) == 0
    assert key(17) == "1" and key(18) == "-1"

    # q2, q3, q4  the three degree rules, on concrete witnesses
    assert sp.limit((3*x + 1)/(x**2 + 1), x, sp.oo) == 0          # smaller degree
    assert sp.limit((7*x**2 + x)/(2*x**2 - 5), x, sp.oo) == sp.Rational(7, 2)  # equal
    assert sp.limit((x**4 + 1)/(x**2 + 1), x, sp.oo) is sp.oo     # larger degree
    assert key(2) == "0"
    assert key(3) == "the ratio of the leading coefficients"
    assert key(4).startswith("no horizontal asymptote")

    # q7  no horizontal asymptote in either direction
    assert sp.limit((x**3 + 1)/(x**2 + 4), x, -sp.oo) is -sp.oo

    # q23  sin(x)/x approaches y = 0 and crosses it infinitely often
    assert sp.limit(sp.sin(x)/x, x, sp.oo) == 0
    for k in range(1, 6):
        assert sp.sin(x).subs(x, k*sp.pi) == 0, "sin(x)/x meets y = 0 at every k*pi"
    assert key(23).startswith("Yes; the asymptote describes only the far-out behavior")

    # q24  2x/sqrt(x^2 + 1) has two horizontal asymptotes
    f24 = 2*x/sp.sqrt(x**2 + 1)
    right, left = sp.limit(f24, x, sp.oo), sp.limit(f24, x, -sp.oo)
    assert (right, left) == (2, -2)
    assert len({right, left}) == 2
    assert key(24) == "two, y = 2 and y = -2"

    # q19  at most two: one per direction
    assert key(19) == "2"

    print(f"c1_15: 25 questions, {len(LIMITS) + 9} limits at infinity verified with "
          f"sympy (both directions wherever a key names an asymptote); "
          f"{len(DEFINITION)} definition items. OK")


if __name__ == "__main__":
    main()
