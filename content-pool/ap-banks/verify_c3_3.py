"""sympy verification for CALC 3.3.

`inv_deriv` does the two steps the formula demands, in order: solve f(a) = b
for a = f^-1(b) over the stated domain, then return 1/f'(a). Nothing is taken
from the answer key, and the function is deliberately not handed the value of
f^-1(b).

It also asserts, for every question where it applies, that f^-1(b) != b -- so
the shortcut 1/f'(b) really does give a different (wrong) number, which is the
distractor those questions offer.

Conceptual questions (1, 12, 16, 22, 25): the formula itself, the misapplied
shortcut, the reflection across y = x, the need for f to be one-to-one, and
the sign of (f^-1)'.
"""
import importlib
import sympy as sp

M = importlib.import_module("c3_3")
x = sp.Symbol("x", real=True)

CONCEPTUAL = {1, 12, 16, 22, 25}
checked = set()
R = sp.Rational

T = {sp.Integer(r[0]): (sp.Rational(r[1]), sp.Rational(r[2])) for r in M.TAB["rows"]}


def check(n, exprs, true_val):
    item = M.QUESTIONS[n - 1]
    assert len(exprs) == 4 == len(item["choices"]), f"q{n}: expected 4 choices"
    diff = sp.simplify(exprs[item["ans"]] - true_val)
    assert diff == 0, f"q{n}: keyed choice {item['ans']} != computed ({diff})"
    for i in range(4):
        for j in range(i + 1, 4):
            assert sp.simplify(exprs[i] - exprs[j]) != 0, f"q{n}: choices {i} and {j} are equal"
    checked.add(n)


def solve_real(f, b, domain):
    """All real a in the domain with f(a) = b.

    Polynomials go through sp.real_roots: solveset returns a ConditionSet for
    a quintic like x^5 + 3x - 1 = 3 and then refuses to be iterated, which is
    exactly the case this topic needs.
    """
    expr = sp.together(f - b)
    poly = expr.as_poly(x)
    if poly is not None:
        cands = list(dict.fromkeys(sp.real_roots(poly)))
    else:
        try:
            cands = [r for r in sp.solveset(sp.Eq(f, b), x, domain) if r.is_real]
        except TypeError:
            # solveset returns a ConditionSet for x + sin(x) = 0 and refuses to
            # be iterated; fall back to scanning the domain for sign changes.
            lo = max(float(domain.inf), -20.0) if domain.inf.is_finite else -20.0
            hi = min(float(domain.sup), 20.0) if domain.sup.is_finite else 20.0
            g = sp.lambdify(x, expr, "math")
            cands, steps = [], 400
            prev_t = lo
            prev_v = g(prev_t)
            for k in range(1, steps + 1):
                t = lo + (hi - lo) * k / steps
                v = g(t)
                if v == 0 or prev_v * v < 0:
                    cands.append(sp.nsimplify(sp.nsolve(expr, x, (prev_t + t) / 2),
                                              rational=False, tolerance=1e-10))
                prev_t, prev_v = t, v
            cands = list(dict.fromkeys(cands))
    out = []
    for r in cands:
        if domain.contains(r) == sp.true or domain.contains(sp.nsimplify(r.evalf())) == sp.true:
            out.append(sp.nsimplify(r))
    return out


def inv_deriv(f, b, domain=sp.S.Reals, expect_distinct=True):
    """(f^-1)'(b): solve f(a) = b for a, then take 1/f'(a)."""
    roots = solve_real(f, b, domain)
    assert len(roots) == 1, f"f(x) = {b} should have one solution in the domain, got {roots}"
    a = roots[0]
    if expect_distinct:
        assert sp.simplify(a - b) != 0, \
            f"f^-1({b}) = {a} equals b, so the 1/f'(b) shortcut would not be tested"
    fp = sp.diff(f, x).subs(x, a)
    assert fp != 0, f"f'({a}) = 0, so the inverse is not differentiable at {b}"
    return sp.simplify(1 / fp)


# --- values stated directly in the stem ------------------------------------
check(2, [R(1, 5), R(1, 3), 3, 5], 1 / sp.Integer(3))
check(3, [R(1, 4), R(1, 2), 2, 4], 1 / R(1, 2))
check(20, [R(1, 7), R(1, 4), 4, 7], 1 / R(1, 4))
check(21, [R(1, 5), R(1, 2), 2, 5], 1 / sp.Integer(5))  # f(1) = 3, so use f'(1) = 5

# --- values read from the table --------------------------------------------
def from_table(b):
    hits = [(a, fp) for a, (fa, fp) in T.items() if fa == b]
    assert len(hits) == 1, f"table: f(x) = {b} for {hits}"
    a, fp = hits[0]
    assert a != b, f"table: f^-1({b}) = {a} equals b"
    return sp.simplify(1 / fp)


check(4, [R(1, 5), R(1, 4), 2, 4], from_table(5))
check(13, [R(1, 8), R(1, 2), 2, 8], from_table(8))

# --- questions that require solving for f^-1(b) first -----------------------
check(5, [R(1, 13), R(1, 4), 4, 13], inv_deriv(x**3 + x, 2))
check(6, [R(1, 5), R(1, 2), 2, 5], inv_deriv(x**3 + 2 * x + 1, 1))
check(7, [R(1, 408), R(1, 8), 3, 8], inv_deriv(x**5 + 3 * x - 1, 3))
check(8, [0, 1 / sp.E, 1, sp.E], inv_deriv(sp.exp(x), 1))
check(9, [-1, 0, 1, sp.E], inv_deriv(sp.log(x), 0, sp.Interval.open(0, sp.oo)))
check(10, [R(1, 18), R(1, 6), 6, 18], inv_deriv(x**2, 9, sp.Interval(0, sp.oo)))
check(11, [R(1, 4), 2 * sp.sqrt(2), 4, 8],
      inv_deriv(sp.sqrt(x), 2, sp.Interval.open(0, sp.oo)))
check(15, [R(1, 192), R(1, 12), R(1, 3), 12], inv_deriv(x**3, 8))
check(17, [R(1, 2), 1, 2, sp.sqrt(2)],
      inv_deriv(sp.tan(x), 1, sp.Interval.open(-sp.pi / 2, sp.pi / 2)))
check(19, [R(1, 6), R(1, 3), 3, 6], inv_deriv(x**3 + 3 * x - 4, 0))
check(23, [R(1, 1537), R(1, 25), 2, 25], inv_deriv(2 * x**3 + x - 2, 16))

# q18: here f^-1(0) = 0 genuinely, so the shortcut coincides; flagged explicitly.
check(18, [0, R(1, 2), 1, 2],
      inv_deriv(x + sp.sin(x), 0, sp.Interval(-1, 1), expect_distinct=False))

# q14: the inverse of a line.
inv14 = sp.solve(sp.Eq(2 * sp.Symbol("t") + 3, x), sp.Symbol("t"))[0]
check(14, [R(1, 2), 2, R(-1, 2), 1 / (2 * x + 3)], sp.diff(inv14, x))

# q24: the tangent line to y = f^-1(x) at x = 5, from slope 1/f'(2) = 3 and
# the point (5, f^-1(5)) = (5, 2).
m24 = 1 / R(1, 3)
line24 = m24 * (x - 5) + 2
check(24, [3 * x - 13, x / 3 + R(1, 3), 3 * x - 5, (x - 2) / 3 + 5], sp.expand(line24))

# q12: the shortcut is wrong precisely when f^-1(b) != b -- shown on q5's data.
f5 = x**3 + x
a5 = solve_real(f5, 2, sp.S.Reals)[0]
assert a5 == 1 and 1 / sp.diff(f5, x).subs(x, a5) != 1 / sp.diff(f5, x).subs(x, 2)

# q25: a positive derivative gives a strictly increasing, hence invertible, f,
# and the reciprocal of a positive number is positive.
for f in (sp.exp(x), x**3 + x, x + sp.atan(x)):
    assert sp.diff(f, x).subs(x, 0) > 0 and 1 / sp.diff(f, x).subs(x, 0) > 0

assert len(M.QUESTIONS) == 25, f"expected 25 questions, found {len(M.QUESTIONS)}"
assert checked | CONCEPTUAL == set(range(1, 26)), \
    f"unaccounted questions: {set(range(1, 26)) - checked - CONCEPTUAL}"
assert not (checked & CONCEPTUAL)
for i, item in enumerate(M.QUESTIONS, 1):
    assert len(item["choices"]) == 4 == len(set(item["choices"])), f"q{i}: choices"
print(f"c3_3: {len(checked)} verified with sympy, {len(CONCEPTUAL)} conceptual, 25 total")
