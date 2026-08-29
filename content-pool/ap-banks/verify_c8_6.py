# Verification for CALC 8.6. Run: python3 verify_c8_6.py
# Crossings are solved for, then each piece is integrated in the correct order
# and the absolute values are summed.
import sympy as sp
from c8_6 import QUESTIONS as Q

x = sp.Symbol('x', real=True)


def key(i):
    return Q[i - 1]["choices"][Q[i - 1]["ans"]]


def split_area(f, g, a, b):
    cuts = sorted({r for r in sp.solve(sp.Eq(f, g), x) if r.is_real and a < r < b})
    pts = [sp.nsimplify(a)] + list(cuts) + [sp.nsimplify(b)]
    total = 0
    for lo, hi in zip(pts, pts[1:]):
        total += sp.Abs(sp.integrate(f - g, (x, lo, hi)))
    return sp.simplify(total)


def num(i):
    return sp.nsimplify(key(i))


assert len(Q) == 25
for i, item in enumerate(Q, 1):
    assert len(item["choices"]) == 4 and len(set(item["choices"])) == 4, i
    assert 0 <= item["ans"] < 4, i

assert key(1).startswith("the curve that is on top changes")
assert key(2) == "int from a to b of |f(x) - g(x)| dx"
assert key(3) == "solving f(x) = g(x)"
assert key(4).startswith("evaluate both functions at a test point")
assert key(5) == "4"

assert sorted(sp.solve(x**3 - x, x)) == [-1, 0, 1]
assert split_area(x**3, x, -1, 1) == sp.Rational(1, 2) and num(6) == sp.Rational(1, 2)
assert split_area(x**3 - x, sp.Integer(0), -1, 1) == sp.Rational(1, 2) and num(7) == sp.Rational(1, 2)
assert sorted(sp.solve(x**3 - 4 * x, x)) == [-2, 0, 2]
assert split_area(x**3, 4 * x, -2, 2) == 8 and num(8) == 8
assert sorted(sp.solve(x**2 - x**4, x)) == [-1, 0, 1]
assert split_area(x**2, x**4, -1, 1) == sp.Rational(4, 15) and num(9) == sp.Rational(4, 15)
assert split_area(x, x**5, -1, 1) == sp.Rational(2, 3) and num(10) == sp.Rational(2, 3)
a11 = split_area(sp.sin(x), sp.cos(x), 0, sp.pi)
assert sp.simplify(a11 - 2 * sp.sqrt(2)) == 0 and key(11) == "2*sqrt(2)"
assert split_area(sp.sin(x), sp.Integer(0), 0, 2 * sp.pi) == 4 and num(12) == 4
assert split_area(sp.cos(x), sp.Integer(0), 0, 2 * sp.pi) == 4 and num(13) == 4
assert split_area(x**3 - 4 * x, sp.Integer(0), -2, 2) == 8 and num(14) == 8
assert split_area(sp.Abs(x), x**2, -1, 1) == sp.Rational(1, 3) and num(15) == sp.Rational(1, 3)
assert split_area(sp.sin(2 * x), sp.Integer(0), 0, sp.pi) == 2 and num(16) == 2
assert sorted(sp.solve(x**4 - 4 * x**2, x)) == [-2, 0, 2]
assert split_area(x**4 - 4 * x**2, sp.Integer(0), -2, 2) == sp.Rational(128, 15)
assert num(17) == sp.Rational(128, 15)
# q18 x^3 vs x^2 on [-1, 2]: they meet at 0 and 1 but only swap order at 1
assert sorted(sp.solve(x**3 - x**2, x)) == [0, 1]
assert (x**3 - x**2).subs(x, sp.Rational(-1, 2)) < 0
assert (x**3 - x**2).subs(x, sp.Rational(1, 2)) < 0
assert (x**3 - x**2).subs(x, sp.Rational(3, 2)) > 0
assert split_area(x**3, x**2, -1, 2) == sp.Rational(25, 12) and num(18) == sp.Rational(25, 12)
assert sp.integrate(x**2 - x**3, (x, -1, 1)) == sp.Rational(2, 3)
assert sp.integrate(x**3 - x**2, (x, 1, 2)) == sp.Rational(17, 12)
# q19
assert sorted(sp.solve(2 * x - (x**3 + x**2), x)) == [-2, 0, 1]
assert split_area(2 * x, x**3 + x**2, -2, 1) == sp.Rational(37, 12) and num(19) == sp.Rational(37, 12)
assert sp.Abs(sp.integrate(2 * x - x**3 - x**2, (x, -2, 0))) == sp.Rational(8, 3)
assert sp.Abs(sp.integrate(2 * x - x**3 - x**2, (x, 0, 1))) == sp.Rational(5, 12)
# q20 the cancellation error
assert sp.integrate(x - x**3, (x, -1, 1)) == 0
assert key(20).startswith("the curves cross at x = 0, so the two halves cancel")
# q21 odd symmetry
assert sp.Abs(sp.integrate(x**3 - x, (x, -1, 0))) == sp.Abs(sp.integrate(x - x**3, (x, 0, 1)))
assert key(21).startswith("both x^3 and x are odd")
# q22 only two meeting points
assert sorted(sp.solve((x**2 - 1) - (1 - x**2), x)) == [-1, 1]
assert key(22).startswith("no, because the curves meet only at x = -1 and x = 1")
assert sp.integrate(x - x**3, (x, 0, 1)) == sp.Rational(1, 4) and num(23) == sp.Rational(1, 4)
assert key(24).startswith("int from -1 to 0 of (x^3 - x) dx")
# q25 tangency: a double root, so no enclosed region
assert sp.solve(x**2 - (2 * x - 1), x) == [1]
assert sp.factor(x**2 - 2 * x + 1) == (x - 1)**2
assert key(25).startswith("0, because a single point of tangency")

print("verify_c8_6: all checks passed")
