"""Sympy verification for CALC 1.4.

Two things are checked for every table question, because a table question can
fail in two independent ways:

  1. the limit the key claims really is the limit of the stated function, and
  2. every number printed in the stem really is that function's value at the
     printed input, rounded as printed.

Check 2 matters more than it looks: a mistyped table entry is invisible to any
check that only recomputes the limit, and it is exactly what would make a
student's reading of the table disagree with the key.  The table entries are
parsed back out of the stem text rather than retyped here, so the stem itself
is what gets verified.

Questions 8, 21 and 24 name no function to recompute (what a finite sample can
establish, comparing four tables, and estimating from a single straddling pair),
so they get the structural check only.  Question 17 is listed with them because
its key is a criticism rather than a value, but the sin(pi/x) trap behind it is
still checked below.
"""
import re

import sympy as sp

import c1_4

x, t = sp.symbols('x t', real=True)
Q = c1_4.QUESTIONS

CONCEPTUAL = {8, 17, 21, 24}


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


def rows(n):
    """Pull the printed x row and f(x) row out of question n's stem."""
    stem = Q[n - 1]["q"]
    m = re.search(r"x = ([-0-9.,\s]+?) with \w+\(x\) = ([-0-9.,\s]+?)\. Based", stem)
    assert m, f"q{n}: could not find the printed table in the stem"
    xs = [sp.Rational(v.strip()) for v in m.group(1).split(",")]
    ys = [v.strip() for v in m.group(2).split(",")]
    return xs, ys


def table_matches(n, expr, var=x):
    """Every printed f(x) entry equals expr(x) rounded to the printed places."""
    xs, ys = rows(n)
    assert len(xs) == len(ys), f"q{n}: {len(xs)} inputs but {len(ys)} outputs"
    for xv, yv in zip(xs, ys):
        places = len(yv.split(".")[1]) if "." in yv else 0
        actual = sp.N(expr.subs(var, xv), 30)
        printed = sp.Rational(yv)
        assert abs(actual - printed) <= sp.Rational(1, 2 * 10**places), \
            f"q{n}: printed {yv} at x = {xv}, but the function gives {actual}"


def pairs(n):
    """Pull loose 'f(a) = b' pairs out of a stem that has no x row / f(x) row."""
    stem = Q[n - 1]["q"]
    return [(sp.Rational(a), sp.Rational(b))
            for a, b in re.findall(
                r"\w+\((-?\d+(?:\.\d+)?)\) = (-?\d+(?:\.\d+)?)", stem)]


def pairs_match(n, expr, var=x, skip=()):
    got = pairs(n)
    assert got, f"q{n}: no f(a) = b pairs found in the stem"
    for xv, yv in got:
        if xv in skip:
            continue
        assert sp.nsimplify(expr.subs(var, xv)) == yv, \
            f"q{n}: stem says {yv} at {xv}, function gives {expr.subs(var, xv)}"


def main():
    structural()

    # --- questions whose stem prints an x row and an f(x) row ------------------
    printed = {
        1:  ((x**2 - 4)/(x - 2), 4, "4"),
        2:  ((sp.sqrt(x) - 2)/(x - 4), sp.Rational(1, 4), "0.25"),
        3:  (sp.sin(x)/x, 1, "1"),
        4:  ((1 - sp.cos(x))/x, 0, "0"),
        5:  ((1 + x)**(1/x), sp.E, "about 2.718"),
        9:  ((x**3 - 8)/(x - 2), 12, "12"),
        10: (sp.tan(x)/x, 1, "1"),
        11: ((sp.exp(x) - 1)/x, 1, "1"),
        12: ((2**x - 1)/x, sp.log(2), "about 0.693"),
        18: ((sp.sqrt(x + 9) - 3)/x, sp.Rational(1, 6), "1/6"),
        22: ((x - 4)/(sp.sqrt(x) - 2), 4, "4"),
        25: ((sp.cos(x) - 1)/x**2, sp.Rational(-1, 2), "-1/2"),
    }
    at = {1: 2, 2: 4, 3: 0, 4: 0, 5: 0, 9: 2, 10: 0, 11: 0, 12: 0,
          18: 0, 22: 4, 25: 0}
    for n, (expr, want, want_text) in printed.items():
        table_matches(n, expr)
        got = sp.limit(expr, x, at[n], '+-')
        assert sp.simplify(got - want) == 0, f"q{n}: limit is {got}, key claims {want}"
        assert key(n) == want_text, f"q{n}: key text {key(n)!r}"

    # --- questions whose stem lists loose f(a) = b pairs -----------------------
    # q6  jump: 4 - x on the left of 1, 8 - x on the right
    left6, right6 = 4 - x, 8 - x
    for xv, yv in pairs(6):
        expr = left6 if xv < 1 else right6
        assert sp.nsimplify(expr.subs(x, xv)) == yv, f"q6: bad entry at {xv}"
    assert sp.limit(left6, x, 1, '-') == 3 and sp.limit(right6, x, 1, '+') == 7
    assert key(6) == "does not exist"

    # q7, q15, q23  all sample 1/(x - c)
    pairs_match(7, 1/(x - 2))
    assert sp.limit(1/(x - 2), x, 2, '+') is sp.oo
    assert key(7).startswith("does not exist")

    pairs_match(15, 1/(x - 1))
    assert sp.limit(1/(x - 1), x, 1, '+') is sp.oo
    assert key(15).startswith("lim as x -> 1^+ of f(x) does not exist")

    pairs_match(23, 1/(x - 2))
    assert sp.limit(1/(x - 2), x, 2, '-') is -sp.oo
    assert sp.limit(1/(x - 2), x, 2, '+') is sp.oo
    assert key(23).startswith("does not exist")

    # q13  x^2 - 2x + 2 sampled only to the right of 3
    pairs_match(13, x**2 - 2*x + 2)
    assert all(xv > 3 for xv, _ in pairs(13)), "q13 must sample only x > 3"
    assert sp.limit(x**2 - 2*x + 2, x, 3, '+') == 5
    assert key(13) == "lim as x -> 3^+ of f(x) = 5"

    # q14  |x - 5|/(x - 5)
    pairs_match(14, sp.Abs(x - 5)/(x - 5))
    assert sp.limit(sp.Abs(x - 5)/(x - 5), x, 5, '-') == -1
    assert sp.limit(sp.Abs(x - 5)/(x - 5), x, 5, '+') == 1
    assert key(14) == "does not exist"

    # q16  5 + 0.3(x - 3) near 3, with f(3) = 9 assigned separately
    pairs_match(16, 5 + sp.Rational(3, 10)*(x - 3), skip=(3,))
    assert sp.limit(5 + sp.Rational(3, 10)*(x - 3), x, 3, '+-') == 5
    assert key(16) == "5"

    # q19  V(t) = 20 - 2(t - 4)
    volume = 20 - 2*(t - 4)
    for tv, vv in pairs(19):
        assert sp.nsimplify(volume.subs(t, tv)) == vv, f"q19: bad entry at {tv}"
    assert sp.limit(volume, t, 4, '+-') == 20
    assert key(19) == "lim as t -> 4 of V(t) = 20 liters"

    # q20  7 + 2(x - 3) near 3, with f(3) = 1 assigned separately
    pairs_match(20, 7 + 2*(x - 3), skip=(3,))
    assert sp.limit(7 + 2*(x - 3), x, 3, '+-') == 7
    assert key(20) == "lim as x -> 3 of f(x) = 7"

    # q17  the sin(pi/x) trap: the sampled inputs really are all zeros of f,
    # and the true limit really does fail to exist.
    trap = sp.sin(sp.pi/x)
    for xv in [sp.Integer(1), sp.Rational(1, 2), sp.Rational(1, 10),
               sp.Rational(1, 100), sp.Rational(1, 1000)]:
        assert sp.simplify(trap.subs(x, xv)) == 0, f"q17: f({xv}) is not 0"
    osc = sp.limit(trap, x, 0, '+')
    assert isinstance(osc, sp.AccumBounds) and (osc.min, osc.max) == (-1, 1)
    assert "does not exist" in key(17)

    # q21  only choice C has the two sides heading to different numbers
    assert key(21).startswith("f(-0.01) = 4.01")

    checked = set(range(1, 26)) - CONCEPTUAL
    print(f"c1_4: 25 questions, {len(checked)} sympy-verified "
          f"(limit and every printed table entry), "
          f"{len(CONCEPTUAL)} conceptual. OK")


if __name__ == "__main__":
    main()
