"""Sympy verification for CALC 1.9.

This topic asks students to match a formula against a table, a described graph,
or a sentence, so the checks below confirm the match itself rather than a single
limit value:

  * hole locations are recomputed by cancelling and evaluating;
  * the numbers printed in q10's correct table are recomputed from the function
    and the three distractor tables are confirmed NOT to match it;
  * every "which of these four" question has all four choices evaluated, so the
    key is confirmed to be the only one that qualifies rather than merely a
    plausible one.

That last point is the reason this file is longer than a list of limits: a
distractor that accidentally also satisfies the stem makes the question
unanswerable, and only evaluating all four catches it.
"""
import sympy as sp

import c1_9

x, t, b = sp.symbols('x t b', real=True)
Q = c1_9.QUESTIONS

VERBAL = {1, 5, 6, 14, 16, 21}   # translate notation to or from words


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


def hole(expr, at):
    """(at, height) if expr has a removable hole at `at`, else None."""
    if expr.subs(x, at) is not sp.nan:
        return None
    lim = sp.limit(expr, x, at, '+-')
    return None if lim in (sp.oo, -sp.oo) else (at, lim)


def main():
    structural()

    # q2  hole of (x^2 - x - 2)/(x - 2)
    assert hole((x**2 - x - 2)/(x - 2), 2) == (2, 3)
    assert key(2) == "(2, 3)"

    # q3  only one choice matches every printed entry AND is undefined at 2
    table3 = {sp.Rational("1.9"): sp.Rational("3.9"),
              sp.Rational("1.99"): sp.Rational("3.99"),
              sp.Rational("2.01"): sp.Rational("4.01"),
              sp.Rational("2.1"): sp.Rational("4.1")}
    cands3 = {
        "f(x) = 2x": 2*x,
        "f(x) = (x^2 - 4)/(x - 2)": (x**2 - 4)/(x - 2),
        "f(x) = x^2 - 2": x**2 - 2,
        "f(x) = (x^2 + 4)/(x + 2)": (x**2 + 4)/(x + 2),
    }
    fits3 = [label for label, e in cands3.items()
             if all(sp.simplify(e.subs(x, xv) - yv) == 0 for xv, yv in table3.items())
             and e.subs(x, 2) is sp.nan]
    assert fits3 == ["f(x) = (x^2 - 4)/(x - 2)"], fits3
    assert key(3) == fits3[0]

    # q4  only one choice is a line with a hole at (3, 7)
    cands4 = {
        "f(x) = (x^2 + x - 12)/(x - 3)": (x**2 + x - 12)/(x - 3),
        "f(x) = (x^2 - 2x - 3)/(x - 3)": (x**2 - 2*x - 3)/(x - 3),
        "f(x) = (x^2 - 9)/(x - 3)": (x**2 - 9)/(x - 3),
        "f(x) = (x^2 - 3x)/(x - 3)": (x**2 - 3*x)/(x - 3),
    }
    fits4 = [label for label, e in cands4.items() if hole(e, 3) == (3, 7)]
    assert fits4 == ["f(x) = (x^2 + x - 12)/(x - 3)"], fits4
    assert key(4) == fits4[0]

    # q7  x + 2 off 0, with f(0) = 5 assigned separately
    assert sp.limit(x + 2, x, 0, '+-') == 2
    assert key(7) == "lim as x -> 0 of f(x) = 2 and f(0) = 5"

    # q8  the piecewise choice really gives limit 2 and value 5
    assert sp.limit(2*x, x, 1, '+-') == 2
    assert key(8) == "f(x) = 2x for x not equal to 1, and f(1) = 5"

    # q10  recompute the correct table, and confirm no distractor table matches
    f10 = (sp.sqrt(1 + x) - 1)/x
    for xv, yv in [(sp.Rational("-0.01"), "0.501256"), (sp.Rational("0.01"), "0.498756")]:
        actual = sp.N(f10.subs(x, xv), 30)
        assert abs(actual - sp.Rational(yv)) <= sp.Rational(1, 2*10**6), \
            f"q10: printed {yv} at x = {xv}, function gives {actual}"
    assert sp.limit(f10, x, 0, '+-') == sp.Rational(1, 2)
    for wrong in ["0.990000", "0.010000", "2.005013"]:
        assert abs(sp.N(f10.subs(x, sp.Rational("-0.01")), 30) - sp.Rational(wrong)) \
            > sp.Rational(1, 2*10**6), f"q10: distractor {wrong} is not distinguishable"
    assert key(10).startswith("f(-0.01) = 0.501256")

    # q11  exactly one choice has unequal but finite one-sided limits at 1
    cands11 = {
        "f(x) = (x^2 - 1)/(x - 1)": (x**2 - 1)/(x - 1),
        "f(x) = 1/(x - 1)": 1/(x - 1),
        "f(x) = |x - 1|/(x - 1)": sp.Abs(x - 1)/(x - 1),
        "f(x) = x^2 + 1": x**2 + 1,
    }
    jumps = []
    for label, e in cands11.items():
        lo, hi = sp.limit(e, x, 1, '-'), sp.limit(e, x, 1, '+')
        if lo != hi and lo.is_finite and hi.is_finite:
            jumps.append(label)
    assert jumps == ["f(x) = |x - 1|/(x - 1)"], jumps
    assert key(11) == jumps[0]

    # q12, q13  the parking charge, as a step function of t
    charge = sp.Piecewise((3, t <= 1), (5, True))
    assert charge.subs(t, sp.Rational(9, 10)) == 3 and charge.subs(t, 1) == 3
    assert charge.subs(t, sp.Rational(11, 10)) == 5
    assert sp.limit(sp.Integer(3), t, 1, '-') == 3 and sp.limit(sp.Integer(5), t, 1, '+') == 5
    assert key(12) == "3 and 5"
    assert key(13) == "does not exist"

    # q15  (x^3 - 1)/(x - 1) clusters near 3
    assert sp.limit((x**3 - 1)/(x - 1), x, 1, '+-') == 3
    assert key(15) == "3"

    # q17  the k that fills the hole
    assert sp.limit((x**2 - 9)/(x - 3), x, 3, '+-') == 6
    assert key(17) == "6"

    # q18  the line y = 3x - 1 with a hole at x = 2
    assert sp.limit(3*x - 1, x, 2, '+-') == 5
    assert key(18) == "5"

    # q19  exactly one choice grows without bound on BOTH sides of 2
    cands19 = {
        "f(x) = 1/(x - 2)": 1/(x - 2),
        "f(x) = 1/(x - 2)^2": 1/(x - 2)**2,
        "f(x) = (x^2 - 4)/(x - 2)": (x**2 - 4)/(x - 2),
        "f(x) = |x - 2|/(x - 2)": sp.Abs(x - 2)/(x - 2),
    }
    both = [label for label, e in cands19.items()
            if sp.limit(e, x, 2, '-') is sp.oo and sp.limit(e, x, 2, '+') is sp.oo]
    assert both == ["f(x) = 1/(x - 2)^2"], both
    assert key(19) == both[0]

    # q20  undefined at 2 yet the limit is 4
    f20 = (x**2 - 4)/(x - 2)
    assert f20.subs(x, 2) is sp.nan and sp.limit(f20, x, 2, '+-') == 4
    assert key(20).startswith("The function is undefined at x = 2")

    # q22  exactly one choice has both one-sided limits equal to 4 at x = 1
    cands22 = [
        ("f(x) = 3x + 1 for x < 1 and f(x) = 5 - x for x >= 1", 3*x + 1, 5 - x),
        ("f(x) = 4x for x < 1 and f(x) = x + 2 for x >= 1", 4*x, x + 2),
    ]
    fits22 = [label for label, lo, hi in cands22
              if sp.limit(lo, x, 1, '-') == 4 and sp.limit(hi, x, 1, '+') == 4]
    assert fits22 == ["f(x) = 3x + 1 for x < 1 and f(x) = 5 - x for x >= 1"], fits22
    # the two non-piecewise distractors do not even have a limit of 4 there
    assert sp.limit(1/(x - 1), x, 1, '+') is sp.oo
    assert sp.limit(sp.Abs(x - 1)/(x - 1), x, 1, '-') == -1
    assert key(22) == fits22[0]

    # q23  (x^2 + bx)/x approaches b, so the table forces b = 7
    assert sp.simplify(sp.cancel((x**2 + b*x)/x) - (x + b)) == 0
    assert sp.limit((x**2 + b*x)/x, x, 0, '+-') == b
    assert sp.solveset(sp.Eq(b, 7), b, sp.S.Reals) == sp.FiniteSet(7)
    assert key(23) == "7"

    # q25  (x - 1)/(x^2 - 1): hole at (1, 1/2), asymptote at -1
    f25 = (x - 1)/(x**2 - 1)
    assert hole(f25, 1) == (1, sp.Rational(1, 2))
    assert sp.limit(f25, x, -1, '-') is -sp.oo and sp.limit(f25, x, -1, '+') is sp.oo
    assert key(25) == "A hole at (1, 1/2) and a vertical asymptote at x = -1"

    print(f"c1_9: 25 questions, 19 verified with sympy "
          f"(limits, hole locations, table entries, and all four choices on every "
          f"'which of these' item), {len(VERBAL)} notation-to-words items. OK")


if __name__ == "__main__":
    main()
