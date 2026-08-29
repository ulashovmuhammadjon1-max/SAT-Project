"""sympy verification for CALC 5.5 (the candidates test).

Each item is checked the way the test is actually run: build the candidate
list (critical numbers inside the interval plus both endpoints), evaluate f
at each, and confirm the keyed maximum or minimum is the extreme value.
"""
import sympy as sp

import c5_5

x = sp.Symbol('x', real=True)


def candidates(f, a, b, extra=()):
    crit = [s for s in sp.solve(sp.diff(f, x), x) if s.is_real and a <= s <= b]
    pts = sorted(set([sp.nsimplify(a), sp.nsimplify(b)] + list(crit) + [sp.nsimplify(e) for e in extra]),
                 key=lambda t: sp.N(t))
    return {t: sp.simplify(f.subs(x, t)) for t in pts}


def top(vals):
    return max(vals.values(), key=lambda v: sp.N(v))


def bot(vals):
    return min(vals.values(), key=lambda v: sp.N(v))


# q4, q5  x^3 - 3x on [-2, 3]
v = candidates(x**3 - 3*x, -2, 3)
assert v == {-2: -2, -1: 2, 1: -2, 3: 18}
assert top(v) == 18 and bot(v) == -2
assert [t for t, y in v.items() if y == -2] == [-2, 1]      # the minimum is attained twice
# q6  x^3 - 3x^2 on [-1, 4]
v = candidates(x**3 - 3*x**2, -1, 4)
assert v == {-1: -4, 0: 0, 2: -4, 4: 16} and top(v) == 16
# q7  x^4 - 8x^2 + 3 on [-1, 3]
v = candidates(x**4 - 8*x**2 + 3, -1, 3)
assert v == {-1: -4, 0: 3, 2: -13, 3: 12} and bot(v) == -13
# q8, q9  2x^3 - 3x^2 - 12x + 5 on [-2, 3]
v = candidates(2*x**3 - 3*x**2 - 12*x + 5, -2, 3)
assert v == {-2: 1, -1: 12, 2: -15, 3: -4}
assert top(v) == 12 and bot(v) == -15
# q10 x + 4/x on [1, 4]
v = candidates(x + 4/x, 1, 4)
assert v == {1: 5, 2: 4, 4: 5} and bot(v) == 4
# q11 x e^(-x) on [0, 3]
v = candidates(x*sp.exp(-x), 0, 3)
assert set(v) == {0, 1, 3} and top(v) == sp.exp(-1)
assert sp.N(3*sp.exp(-3)) < sp.N(sp.exp(-1))
# q12 sin + cos on [0, pi]
v = candidates(sp.sin(x) + sp.cos(x), 0, sp.pi)
assert top(v) == sp.sqrt(2) and bot(v) == -1
# q13 x^(2/3) on [-8, 1]; critical number 0 comes from f' being undefined
f13 = sp.Pow(x**2, sp.Rational(1, 3))
v13 = {t: sp.nsimplify(f13.subs(x, t)) for t in (-8, 0, 1)}
assert v13 == {-8: 4, 0: 0, 1: 1} and top(v13) == 4
# q14 ln(x)/x on [1, e^2]
v = candidates(sp.log(x)/x, 1, sp.E**2)
assert top(v) == sp.exp(-1)
assert sp.N(2*sp.exp(-2)) < sp.N(sp.exp(-1))
# q15 x sqrt(4 - x^2) on [-2, 2]
v = candidates(x*sp.sqrt(4 - x**2), -2, 2)
assert top(v) == 2 and bot(v) == -2
# q16 1/(x^2 + 1) on [-1, 2]
v = candidates(1/(x**2 + 1), -1, 2)
assert v == {-1: sp.Rational(1, 2), 0: 1, 2: sp.Rational(1, 5)}
assert bot(v) == sp.Rational(1, 5)
# q17 x^3 on [-2, 1]: extremes at the endpoints
v = candidates(x**3, -2, 1)
assert v == {-2: -8, 0: 0, 1: 1} and top(v) == 1 and bot(v) == -8
# q18 |x - 3| on [0, 5]
f18 = sp.Abs(x - 3)
v18 = {t: f18.subs(x, t) for t in (0, 3, 5)}
assert v18 == {0: 3, 3: 0, 5: 2} and max(v18.values()) == 3
# q19 x^4 - 2x^2 on [0, 2]
v = candidates(x**4 - 2*x**2, 0, 2)
assert v == {0: 0, 1: -1, 2: 8} and bot(v) == -1
# q20 cos on [0, 3pi/2]
v = candidates(sp.cos(x), 0, 3*sp.pi/2)
assert bot(v) == -1 and v[sp.pi] == -1
# q21 e^x - x on [-1, 2]
v = candidates(sp.exp(x) - x, -1, 2)
assert set(v) == {-1, 0, 2}
assert top(v) == sp.exp(2) - 2
assert sp.N(sp.exp(-1) + 1) < sp.N(sp.exp(2) - 2)
# q22 x/(x^2 + 4) on [0, 4]
v = candidates(x/(x**2 + 4), 0, 4)
assert v == {0: 0, 2: sp.Rational(1, 4), 4: sp.Rational(1, 5)}
assert top(v) == sp.Rational(1, 4)
# q23 (x - 1)^(2/3) on [0, 9]
f23 = sp.Pow((x - 1)**2, sp.Rational(1, 3))
v23 = {t: sp.nsimplify(f23.subs(x, t)) for t in (0, 1, 9)}
assert v23 == {0: 1, 1: 0, 9: 4} and max(v23.values()) == 4
# q24 3x^(4/3) - 12x^(1/3) on [-1, 8]
r = sp.real_root(x, 3)
f24 = 3*r**4 - 12*r
p = sp.Symbol('p', positive=True)
assert sp.simplify(sp.diff(3*p**sp.Rational(4, 3) - 12*p**sp.Rational(1, 3), p)
                   - 4*(p - 1)/p**sp.Rational(2, 3)) == 0
v24 = {t: sp.nsimplify(f24.subs(x, t)) for t in (-1, 0, 1, 8)}
assert v24 == {-1: 15, 0: 0, 1: -9, 8: 24}
assert max(v24.values()) == 24 and min(v24.values()) == -9

# structural checks
qs = c5_5.QUESTIONS
assert len(qs) == 25, len(qs)
for i, item in enumerate(qs, 1):
    assert len(item["choices"]) == 4, i
    assert len(set(item["choices"])) == 4, i
    assert 0 <= item["ans"] < 4, i
    assert item["why"].strip()
assert len({q["q"] for q in qs}) == 25

print("c5_5: all checks passed")
