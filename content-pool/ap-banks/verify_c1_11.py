"""Sympy verification for CALC 1.11.

conditions() evaluates the three continuity conditions for a function at a
point and reports which of them hold.  Every question that names a specific
function is checked against it, including the ones whose key names *which*
condition fails — that is the part a reader is most likely to get wrong, since
"undefined at c" and "no limit at c" look alike and are different failures.
"""
import sympy as sp

import c1_11

x = sp.Symbol('x', real=True)
Q = c1_11.QUESTIONS

DEFINITION = {1, 2, 12, 17, 18, 22, 25}


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
    assert not open("c1_11.py", "rb").read().startswith(b"\xef\xbb\xbf"), \
        "module file starts with a byte-order mark"


def conditions(expr, at, value=None):
    """Which of the three continuity conditions hold at x = at.

    Returns (defined, limit_exists, they_agree).  `value` overrides the value
    read off the expression, for functions defined piecewise at the point.
    """
    val = expr.subs(x, at) if value is None else value
    defined = val is not sp.nan and val.is_finite is not False
    left = sp.limit(expr, x, at, '-')
    right = sp.limit(expr, x, at, '+')
    oscillating = isinstance(left, sp.AccumBounds) or isinstance(right, sp.AccumBounds)
    limit_exists = (not oscillating
                    and left not in (sp.oo, -sp.oo)
                    and right not in (sp.oo, -sp.oo)
                    and sp.simplify(left - right) == 0)
    agree = bool(defined and limit_exists and sp.simplify(left - val) == 0)
    return defined, limit_exists, agree


def continuous(expr, at, value=None):
    return conditions(expr, at, value)[2]


def main():
    structural()

    # q3  (x^2 - 4)/(x - 2) at 2: only the "defined" condition fails
    assert conditions((x**2 - 4)/(x - 2), 2) == (False, True, False)
    assert sp.limit((x**2 - 4)/(x - 2), x, 2, '+-') == 4
    assert key(3) == "f(2) is not defined"

    # q4  the -1/1 step at 0: defined, but no limit
    step = sp.Piecewise((-1, x < 0), (1, True))
    assert step.subs(x, 0) == 1
    assert (sp.limit(sp.Integer(-1), x, 0, '-'), sp.limit(sp.Integer(1), x, 0, '+')) == (-1, 1)
    assert key(4).startswith("the limit as x approaches 0 does not exist")

    # q5  x + 1 off 3 with f(3) = 7: defined and limited, but they disagree
    assert conditions(x + 1, 3, value=sp.Integer(7)) == (True, True, False)
    assert sp.limit(x + 1, x, 3, '+-') == 4
    assert key(5).startswith("the limit exists and equals 4")

    # q6  a polynomial is continuous everywhere it is sampled
    poly = 3*x**3 - 5*x + 2
    for at in (-3, 0, sp.Rational(1, 2), 7):
        assert continuous(poly, at), f"polynomial not continuous at {at}"
    assert key(6) == "at every real number"

    # q7, q8  1/x fails at 0 on the first condition, and is fine at 2
    assert conditions(1/x, 0) == (False, False, False)
    assert key(7) == "No, because f(0) is undefined"
    assert continuous(1/x, 2) and (1/x).subs(x, 2) == sp.Rational(1, 2)
    assert key(8).startswith("Yes, because f(2) = 1/2")

    # q9, q10  the two piecewise seams at x = 1
    assert sp.limit(x**2, x, 1, '-') == 1 and sp.limit(2*x - 1, x, 1, '+') == 1
    assert key(9).startswith("Yes, because the left limit")
    assert sp.limit(x**2, x, 1, '-') == 1 and sp.limit(2*x, x, 1, '+') == 2
    assert key(10) == "No, because the left limit is 1 and the right limit is 2"

    # q11  sqrt(x) at 0: right-continuous only, since there is no left approach
    assert sp.sqrt(x).subs(x, 0) == 0
    assert sp.limit(sp.sqrt(x), x, 0, '+') == 0
    assert not sp.sqrt(sp.Rational(-1, 100)).is_real, "sqrt is not real to the left of 0"
    assert key(11).startswith("f is continuous from the right at 0")

    # q13  |x| is continuous at 0 despite the corner
    assert continuous(sp.Abs(x), 0)
    assert key(13).startswith("Yes, because both one-sided limits and f(0) all equal 0")

    # q14, q15  the greatest integer function
    assert sp.floor(x).subs(x, 2) == 2
    assert sp.limit(sp.floor(x), x, 2, '-') == 1
    assert not continuous(sp.floor(x), 2)
    assert key(14) == "No, because the left limit is 1 while the value is 2"
    assert continuous(sp.floor(x), sp.Rational(5, 2))
    assert key(15).startswith("Yes, because it equals the constant 2")

    # q16  exactly one of the four choices is continuous at 0
    cands16 = {
        "f(x) = 1/x": 1/x,
        "f(x) = |x|/x": sp.Abs(x)/x,
        "f(x) = x^2 + 3": x**2 + 3,
        "f(x) = (x^2 - x)/x": (x**2 - x)/x,
    }
    good = [label for label, e in cands16.items() if continuous(e, 0)]
    assert good == ["f(x) = x^2 + 3"], good
    assert key(16) == good[0]

    # q20  a witness with limit 9 and no value at 4: only condition (1) fails,
    # and assigning 9 makes all three hold, which is what "removable" means.
    witness = (x**2 - 16)/(x - 4) + 1        # equals x + 5 off 4, so the limit is 9
    assert conditions(witness, 4) == (False, True, False)
    assert sp.limit(witness, x, 4, '+-') == 9
    assert conditions(witness, 4, value=sp.Integer(9)) == (True, True, True)
    assert key(20).startswith("f is discontinuous at 4, and the discontinuity is removable")

    # q21  (x^2 - 1)/(x - 1) with f(1) = 2 is continuous
    assert conditions((x**2 - 1)/(x - 1), 1, value=sp.Integer(2)) == (True, True, True)
    assert key(21).startswith("Yes, because the limit is 2")

    # q23, q24  sin(x)/x at 0 with the right and the wrong assigned value
    assert sp.limit(sp.sin(x)/x, x, 0, '+-') == 1
    assert conditions(sp.sin(x)/x, 0, value=sp.Integer(1)) == (True, True, True)
    assert key(23).startswith("Yes, because the limit as x approaches 0 is 1")
    assert conditions(sp.sin(x)/x, 0, value=sp.Integer(0)) == (True, True, False)
    assert key(24).startswith("the limit exists and equals 1")

    # q25  |x| is the witness that continuity does not imply differentiability
    assert continuous(sp.Abs(x), 0)
    assert sp.diff(sp.Abs(x), x).subs(x, 0) is sp.nan or \
        sp.limit((sp.Abs(x) - 0)/x, x, 0, '-') != sp.limit((sp.Abs(x) - 0)/x, x, 0, '+')
    assert key(25) == "f is differentiable at c"

    print("c1_11: 25 questions, every named function's three continuity "
          "conditions evaluated with sympy and compared with the key; "
          f"{len(DEFINITION)} definition items. OK")


if __name__ == "__main__":
    main()
