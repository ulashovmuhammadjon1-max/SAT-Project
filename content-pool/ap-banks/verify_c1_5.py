"""Sympy verification for CALC 1.5.

The "given limits" questions are checked by exhibiting concrete functions with
the stated limits and taking the combined limit with sympy, rather than by
restating the law.  That way the check would catch an arithmetic slip in a key
(5 * -2 written as -7, say) instead of merely agreeing with it.

f0 and g0 below approach 5 and -2 at x = 0 without ever being constant, so a
limit law is genuinely being exercised.

Questions 6, 9, 19, 22 and 25 are conceptual (when a law applies, what it fails
to determine, naming the law); q22's two witnesses are checked numerically.
"""
import sympy as sp

import c1_5

x = sp.Symbol('x', real=True)
Q = c1_5.QUESTIONS

CONCEPTUAL = {6, 9, 19, 22, 25}

# Concrete stand-ins: lim f0 = 5 and lim g0 = -2 as x -> 0, neither constant.
f0 = 5 + sp.sin(x)
g0 = -2 + x**2


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
    assert len(set(heads)) == len(heads), \
        "two stems share their opening 90 characters, which the exporter warns on"


def lim0(expr):
    return sp.limit(expr, x, 0, '+-')


def num(text):
    return sp.nsimplify(text)


def main():
    structural()

    assert lim0(f0) == 5 and lim0(g0) == -2, "the stand-in functions are wrong"

    # q1-q5, q7, q8, q11-q13: the laws applied to the stand-ins
    laws = [
        (1,  f0 + g0,                 3),
        (2,  f0 * g0,                 -10),
        (3,  f0 / g0,                 sp.Rational(-5, 2)),
        (4,  3*f0 - 2*g0,             19),
        (5,  f0**2,                   25),
        (7,  sp.sqrt(f0),             sp.sqrt(5)),
        (8,  g0 / f0,                 sp.Rational(-2, 5)),
        (11, -4*f0,                   -20),
        (12, f0 + 3,                  8),
        (13, f0**3,                   125),
    ]
    for n, expr, want in laws:
        got = lim0(expr)
        assert sp.simplify(got - want) == 0, f"q{n}: limit is {got}, expected {want}"
        assert sp.simplify(num(key(n)) - want) == 0, f"q{n}: key text {key(n)!r}"

    # q10  f -> 4, g -> 0: the quotient g/f is fine, f/g (q9) is not
    f10, g10 = 4 + (x - 2), (x - 2)**2
    assert sp.limit(f10, x, 2, '+-') == 4 and sp.limit(g10, x, 2, '+-') == 0
    assert sp.limit(g10/f10, x, 2, '+-') == 0
    assert key(10) == "0"

    # q9  with the same limits, f/g can be made to behave differently, so the
    # law really does determine nothing: one witness blows up, another oscillates.
    assert sp.limit(f10/g10, x, 2, '+-') is sp.oo
    alt = 4 + (x - 2)
    assert sp.limit(alt/(x - 2), x, 2, '-') is -sp.oo
    assert sp.limit(alt/(x - 2), x, 2, '+') is sp.oo
    assert key(9).startswith("The quotient law does not apply")

    # q14-q17  direct evaluation
    direct = [
        (14, 2*x**2 - 5*x + 1,      3, 4,           "4"),
        (15, (x**2 + 3)/(x + 1),    1, 2,           "2"),
        (16, sp.sqrt(2*x + 1),      4, 3,           "3"),
        (17, 3*sp.cos(x) + 2,       0, 5,           "5"),
    ]
    for n, expr, at, want, want_text in direct:
        got = sp.limit(expr, x, at, '+-')
        assert sp.simplify(got - want) == 0, f"q{n}: limit is {got}"
        assert key(n) == want_text, f"q{n}: key text {key(n)!r}"

    # q18  composition through a continuous outer function
    g18 = 3 + (x - 2)          # -> 3 as x -> 2
    f18 = 2*x + 1              # continuous, f18(3) = 7
    assert f18.subs(x, 3) == 7
    assert sp.limit(f18.subs(x, g18), x, 2, '+-') == 7
    assert key(18) == "7"

    # q20  f/g -> 3 and g -> 4 forces f -> 12
    g20 = 4 + x**2
    f20 = 3*g20 + x**3         # so f20/g20 -> 3
    assert sp.limit(f20/g20, x, 0, '+-') == 3 and sp.limit(g20, x, 0, '+-') == 4
    assert sp.limit(f20, x, 0, '+-') == 12
    assert key(20) == "12"

    # q21  (f + g) -> 7 and f -> 3 forces g -> 4
    f21 = 3 + x
    g21 = 4 - x + x**2
    assert sp.limit(f21 + g21, x, 0, '+-') == 7 and sp.limit(f21, x, 0, '+-') == 3
    assert sp.limit(g21, x, 0, '+-') == 4
    assert key(21) == "4"

    # q22  the two witnesses: one sum has a limit, the other does not
    w = sp.Abs(x)/x
    assert sp.limit(w + (-w), x, 0, '+-') == 0
    assert sp.limit(w, x, 0, '-') != sp.limit(w, x, 0, '+')
    assert sp.limit(2*w, x, 0, '-') != sp.limit(2*w, x, 0, '+')
    assert key(22) == "It may exist or may fail to exist, depending on f and g"

    # q23  fg -> 0 with f -> 3 forces g -> 0
    f23 = 3 + x
    g23 = x**2
    assert sp.limit(f23*g23, x, 0, '+-') == 0 and sp.limit(f23, x, 0, '+-') == 3
    assert sp.limit(g23, x, 0, '+-') == 0
    assert key(23) == "0"

    # q24  cube root of a limit of 8
    f24 = 8 + x
    assert sp.limit(sp.real_root(f24, 3), x, 0, '+-') == 2
    assert key(24) == "2"

    # q25  the denominator's limit really is 0, and the true limit is 6
    assert sp.limit(x - 3, x, 3, '+-') == 0
    assert sp.limit((x**2 - 9)/(x - 3), x, 3, '+-') == 6
    assert key(25).startswith("the denominator's limit is 0")

    checked = set(range(1, 26)) - CONCEPTUAL
    print(f"c1_5: 25 questions, {len(checked)} sympy-verified, "
          f"{len(CONCEPTUAL)} conceptual. OK")


if __name__ == "__main__":
    main()
