"""Sympy verification for CALC 1.1.

Every computational key in c1_1.py is recomputed here from scratch and compared
with the text of the choice the module marks correct.  Conceptual items (the
definitions of average and instantaneous rate of change, the secant/tangent
geometry, the units item and the identification of a difference quotient) carry
no sympy check; they are listed in CONCEPTUAL and only get the structural check.
"""
import sympy as sp

import c1_1

x, h, a, b, t = sp.symbols('x h a b t', real=True)
Q = c1_1.QUESTIONS

CONCEPTUAL = {1, 2, 3, 4, 5, 19, 22, 24}


def key(n):
    """Text of the choice marked correct for question n (1-based)."""
    item = Q[n - 1]
    return item["choices"][item["ans"]]


def structural():
    assert len(Q) == 25, f"expected 25 questions, found {len(Q)}"
    for i, item in enumerate(Q, 1):
        assert len(item["choices"]) == 4, f"q{i}: needs exactly 4 choices"
        assert len(set(item["choices"])) == 4, f"q{i}: duplicate choice text"
        assert 0 <= item["ans"] < 4, f"q{i}: bad answer index"
        assert item["q"].strip() and item["why"].strip(), f"q{i}: empty field"
    stems = [item["q"] for item in Q]
    assert len(set(stems)) == len(stems), "duplicate stem inside the module"


def numeric_choices_distinct(n):
    """Choices that parse as numbers must be pairwise unequal as numbers."""
    vals = []
    for c in Q[n - 1]["choices"]:
        token = c.split()[0]
        try:
            vals.append(sp.nsimplify(token))
        except (sp.SympifyError, ValueError, TypeError):
            return
    for i in range(len(vals)):
        for j in range(i + 1, len(vals)):
            assert sp.simplify(vals[i] - vals[j]) != 0, f"q{n}: choices {i} and {j} are equal"


def avg_rate(f, lo, hi, var=x):
    return sp.simplify((f.subs(var, hi) - f.subs(var, lo)) / (hi - lo))


def main():
    structural()

    # q6  average velocity of s(t) = t^2 + 3t on [1, 4]
    assert avg_rate(t**2 + 3*t, 1, 4, t) == 8
    assert key(6).startswith("8 ")

    # q7  difference quotient of x^2 at x = 2
    assert sp.simplify(((2 + h)**2 - 2**2)/h - (4 + h)) == 0
    assert key(7) == "4 + h"

    # q8  instantaneous rate of x^2 at x = 2
    assert sp.limit(((2 + h)**2 - 4)/h, h, 0) == 4
    assert key(8) == "4"

    # q9  average rate of 1/x on [1, 3]
    assert avg_rate(1/x, 1, 3) == sp.Rational(-1, 3)
    assert sp.nsimplify(key(9)) == sp.Rational(-1, 3)
    numeric_choices_distinct(9)

    # q10 average velocity of 16t^2 on [1, 2]
    assert avg_rate(16*t**2, 1, 2, t) == 48
    assert key(10).startswith("48 ")

    # q11 average velocity of 16t^2 on [1, 1.01]
    assert avg_rate(16*t**2, 1, sp.Rational(101, 100), t) == sp.Rational(804, 25)
    assert sp.Rational(804, 25) == sp.Rational("32.16")
    assert key(11).startswith("32.16 ")

    # q12 recorded positions: (25 - 2)/5
    assert sp.Rational(25 - 2, 5) == sp.Rational("4.6")
    assert key(12).startswith("4.6 ")

    # q13 average rate of x^3 on [-1, 2]
    assert avg_rate(x**3, -1, 2) == 3
    assert key(13) == "3"
    numeric_choices_distinct(13)

    # q14 average rate of sqrt(x) on [4, 9]
    assert avg_rate(sp.sqrt(x), 4, 9) == sp.Rational(1, 5)
    assert sp.nsimplify(key(14)) == sp.Rational(1, 5)
    numeric_choices_distinct(14)

    # q15 average rate of 2^x on [0, 3]
    assert avg_rate(2**x, 0, 3) == sp.Rational(7, 3)
    assert sp.nsimplify(key(15)) == sp.Rational(7, 3)
    numeric_choices_distinct(15)

    # q16 linear function has a constant difference quotient
    assert sp.simplify(avg_rate(3*x + 5, a, b)) == 3
    assert key(16) == "3"

    # q17 average rate of x^2 - 4x on [0, 4]
    assert avg_rate(x**2 - 4*x, 0, 4) == 0
    assert key(17) == "0"

    # q18 limit of the difference quotient of x^2 + 1 at x = 3
    assert sp.limit(((3 + h)**2 + 1 - (3**2 + 1))/h, h, 0) == 6
    assert key(18) == "6"

    # q20 lim ((5 + h)^3 - 125)/h
    assert sp.limit(((5 + h)**3 - 125)/h, h, 0) == 75
    assert key(20) == "75"
    numeric_choices_distinct(20)

    # q21 the tabulated quotients really are 4.1, 4.01, 4.001 and tend to 4
    dq = sp.simplify(((2 + h)**2 - 4)/h)
    for step, want in [(sp.Rational(1, 10), sp.Rational("4.1")),
                       (sp.Rational(1, 100), sp.Rational("4.01")),
                       (sp.Rational(1, 1000), sp.Rational("4.001"))]:
        assert dq.subs(h, step) == want
    assert sp.limit(dq, h, 0) == 4
    assert key(21).endswith("at x = 2 is 4")

    # q23 average rate of x^2 - x on [1, 4]
    assert avg_rate(x**2 - x, 1, 4) == 4
    assert key(23) == "4"
    numeric_choices_distinct(23)

    # q25 average rate of 1/x on [a, b]
    assert sp.simplify(avg_rate(1/x, a, b) - (-1/(a*b))) == 0
    assert key(25) == "-1/(ab)"

    # the distractors of q25 are genuinely different functions of a and b
    alt = {"-1/(ab)": -1/(a*b), "1/(ab)": 1/(a*b),
           "-1/(a + b)": -1/(a + b), "(b - a)/(ab)": (b - a)/(a*b)}
    exprs = list(alt.values())
    for i in range(len(exprs)):
        for j in range(i + 1, len(exprs)):
            assert sp.simplify(exprs[i] - exprs[j]) != 0, "q25 distractors collide"

    # the q24 interval really is the only one with zero net displacement
    s = t**3 - 6*t**2 + 9*t
    disp = {"[0, 1]": (0, 1), "[0, 2]": (0, 2), "[0, 3]": (0, 3), "[1, 2]": (1, 2)}
    zeros = [lab for lab, (lo, hi) in disp.items()
             if sp.simplify(s.subs(t, hi) - s.subs(t, lo)) == 0]
    assert zeros == ["[0, 3]"], zeros
    assert key(24) == "[0, 3]"

    checked = set(range(1, 26)) - CONCEPTUAL
    print(f"c1_1: 25 questions, {len(checked)} sympy-verified, "
          f"{len(CONCEPTUAL)} conceptual. OK")


if __name__ == "__main__":
    main()
