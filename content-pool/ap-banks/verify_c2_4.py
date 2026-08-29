"""sympy verification for CALC 2.4.

Differentiability at a point is decided here the way the definition decides it:
by computing the one-sided limits of the difference quotient and comparing
them, and by comparing the one-sided limits of f with f(a) for continuity.
Nothing is taken from the answer key.

Conceptual questions (1, 2, 7, 13, 20, 24, 25) state the implication and its
false converse:
  q1  differentiable at a => continuous at a;
  q2  the converse fails, so continuity forces none of the listed consequences;
  q7  the contrapositive: not continuous at a => not differentiable at a;
  q13 the two directions stated together;
  q20 f'(a) exists => lim f(x) = f(a);
  q24 differentiable on an interval => continuous on it, and nothing more;
  q25 a corner is the only listed feature compatible with continuity.
"""
import importlib
import sympy as sp

M = importlib.import_module("c2_4")
x, h = sp.symbols("x h", real=True)

CONCEPTUAL = {1, 2, 7, 13, 20, 24, 25}
checked = set()


def key_is(n, ans, note):
    item = M.QUESTIONS[n - 1]
    assert len(item["choices"]) == 4, f"q{n}: expected 4 choices"
    assert len(set(item["choices"])) == 4, f"q{n}: choices not distinct"
    assert item["ans"] == ans, f"q{n}: key is {item['ans']}, expected {ans} ({note})"
    checked.add(n)


def one_sided_dq(f, a, side):
    """lim of (f(a + h) - f(a))/h as h -> 0 from the given side."""
    return sp.limit((f.subs(x, a + h) - f.subs(x, a)) / h, h, 0, side)


def cbrt(e):
    return sp.real_root(e, 3)


# --- q3: |x| at 0 -- continuous, one-sided derivatives 1 and -1 -------------
f_abs = sp.Abs(x)
assert sp.limit(f_abs, x, 0) == 0 == f_abs.subs(x, 0), "q3: |x| should be continuous at 0"
assert one_sided_dq(f_abs, 0, "+") == 1 and one_sided_dq(f_abs, 0, "-") == -1
key_is(3, 0, "continuous, one-sided slopes 1 and -1 disagree")

# --- q4: x^(1/3) -- vertical tangent, both one-sided slopes +infinity -------
f_cbrt = cbrt(x)
assert sp.limit(f_cbrt, x, 0) == 0, "q4: cube root should be continuous at 0"
assert one_sided_dq(f_cbrt, 0, "+") == sp.oo and one_sided_dq(f_cbrt, 0, "-") == sp.oo
key_is(4, 0, "both one-sided slopes are +infinity: a vertical tangent")

# --- q5: x^(2/3) -- cusp, one-sided slopes +infinity and -infinity ----------
f_23 = cbrt(x) ** 2
assert sp.limit(f_23, x, 0) == 0, "q5: x^(2/3) should be continuous at 0"
assert one_sided_dq(f_23, 0, "+") == sp.oo and one_sided_dq(f_23, 0, "-") == -sp.oo
key_is(5, 0, "one-sided slopes +infinity and -infinity: a cusp")

# --- q6: which is not differentiable at 0 ----------------------------------
for f in (x**2, x**3, sp.sin(x)):
    assert one_sided_dq(f, 0, "+") == one_sided_dq(f, 0, "-"), f"q6: {f} should be smooth at 0"
assert one_sided_dq(f_abs, 0, "+") != one_sided_dq(f_abs, 0, "-")
key_is(6, 3, "|x| is the only one whose one-sided slopes disagree")


def piecewise_at(left, right, a):
    """(continuous?, left slope, right slope) for f = left on x <= a, right on x > a."""
    cont = sp.simplify(left.subs(x, a) - sp.limit(right, x, a, "+")) == 0
    ls = sp.limit((left.subs(x, a + h) - left.subs(x, a)) / h, h, 0, "-")
    rs = sp.limit((right.subs(x, a + h) - left.subs(x, a)) / h, h, 0, "+")
    return cont, ls, rs


cont, ls, rs = piecewise_at(x**2, 2 * x - 1, 1)
assert cont and ls == rs == 2, "q8: should be differentiable with slope 2"
key_is(8, 0, "continuous at 1 and both one-sided slopes equal 2")

cont, _, _ = piecewise_at(x**2, 3 * x - 1, 1)
assert not cont, "q9: should be discontinuous at 1"
key_is(9, 0, "the two pieces give 1 and 2 at x = 1, a jump")

a_s, b_s = sp.symbols("a_s b_s")
sol10 = sp.solve(sp.Eq((x**2).subs(x, 2), (a_s * x + 1).subs(x, 2)), a_s)
assert sol10 == [sp.Rational(3, 2)], f"q10: continuity gives {sol10}"
assert M.QUESTIONS[9]["choices"][M.QUESTIONS[9]["ans"]] == "3/2"
key_is(10, 3, "2a + 1 = 4 gives a = 3/2")

sol11 = sp.solve([sp.Eq(1, a_s + b_s), sp.Eq(sp.diff(x**3, x).subs(x, 1), a_s)], [a_s, b_s])
assert sol11 == {a_s: 3, b_s: -2}, f"q11: {sol11}"
key_is(11, 0, "a = 3 and b = -2")

assert (one_sided_dq(f_abs, 0, "+"), one_sided_dq(f_abs, 0, "-")) == (1, -1)
key_is(12, 0, "the one-sided difference quotients are 1 and -1")

# --- q14: a step function -- flat pieces, but a jump -----------------------
# sympy's limit() of a Piecewise does not respect the branch condition here
# (it returns 2 from the left), so the one-sided limits are taken from the
# branch formulas themselves, which is what the definition uses.
left_piece, right_piece = sp.Integer(1), sp.Integer(2)
assert sp.diff(left_piece, x) == 0 and sp.diff(right_piece, x) == 0, "q14: pieces are flat"
assert sp.limit(left_piece, x, 0, "-") != right_piece.subs(x, 0), "q14: should jump at 0"
key_is(14, 0, "the jump at 0 rules out a derivative even though each piece is flat")

# --- q15, q16, q17: corners of absolute-value functions --------------------
for expr, corners in ((sp.Abs(x - 3), [3]), (sp.Abs(x**2 - 4), [-2, 2])):
    inner = expr.args[0]
    found = sorted(sp.solve(sp.Eq(inner, 0), x))
    assert found == sorted(corners), f"corners of {expr}: {found}"
    for c in found:
        assert one_sided_dq(expr, c, "+") != one_sided_dq(expr, c, "-"), f"{expr} at {c}"
key_is(15, 0, "the single corner is at x = 3")
key_is(16, 0, "corners at x = -2 and x = 2")

f17 = sp.Abs(x - 1) + sp.Abs(x + 2)
bad17 = [c for c in (-2, 1) if one_sided_dq(f17, c, "+") != one_sided_dq(f17, c, "-")]
assert len(bad17) == 2, f"q17: found {bad17}"
assert M.QUESTIONS[16]["choices"][M.QUESTIONS[16]["ans"]] == "2"
key_is(17, 2, "two corners, at x = -2 and x = 1")

# --- q18, q19: the oscillating pair ---------------------------------------
assert sp.limit(h**2 * sp.sin(1 / h) / h, h, 0) == 0, "q18: f'(0) should be 0"
key_is(18, 0, "the difference quotient h sin(1/h) is squeezed to 0")

assert sp.limit(h * sp.sin(1 / h), h, 0) == 0, "q19: g should be continuous at 0"
osc = sp.limit(sp.sin(1 / h), h, 0)
assert isinstance(osc, sp.AccumBounds), f"q19: expected an oscillating limit, got {osc}"
key_is(19, 0, "continuous, but the difference quotient sin(1/h) has no limit")

# --- q21, q22: vertical tangent versus cusp versus corner ------------------
f21 = sp.sqrt(sp.Abs(x))
assert sp.limit(f21, x, 0) == 0
assert one_sided_dq(f21, 0, "+") == sp.oo and one_sided_dq(f21, 0, "-") == -sp.oo
key_is(21, 0, "continuous, but the one-sided slopes are +infinity and -infinity")

assert one_sided_dq(cbrt(x), 0, "+") == one_sided_dq(cbrt(x), 0, "-") == sp.oo
assert one_sided_dq(f_abs, 0, "+") != one_sided_dq(f_abs, 0, "-")
assert one_sided_dq(x**2, 0, "+") == one_sided_dq(x**2, 0, "-") == 0
assert one_sided_dq(cbrt(x) ** 4, 0, "+") == one_sided_dq(cbrt(x) ** 4, 0, "-") == 0
key_is(22, 0, "only x^(1/3) has both one-sided slopes equal to +infinity")

sol23 = sp.solve([sp.Eq(a_s * 4, 2 + b_s), sp.Eq(4 * a_s, 1)], [a_s, b_s])
assert sol23 == {a_s: sp.Rational(1, 4), b_s: -1}, f"q23: {sol23}"
key_is(23, 0, "a = 1/4 and b = -1")

assert len(M.QUESTIONS) == 25, f"expected 25 questions, found {len(M.QUESTIONS)}"
assert checked | CONCEPTUAL == set(range(1, 26)), \
    f"unaccounted questions: {set(range(1, 26)) - checked - CONCEPTUAL}"
assert not (checked & CONCEPTUAL)
for i, item in enumerate(M.QUESTIONS, 1):
    assert len(item["choices"]) == 4 == len(set(item["choices"])), f"q{i}: choices"
print(f"c2_4: {len(checked)} verified with sympy, {len(CONCEPTUAL)} conceptual, 25 total")
