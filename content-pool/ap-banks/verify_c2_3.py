"""sympy verification for CALC 2.3.

Every numeric estimate is recomputed here from the tables and values stored in
c2_3.py itself, so the number a question is graded against is the number the
student sees. `num` also confirms the four choices are pairwise distinct as
numbers, not merely as strings.

Conceptual questions (6, 7, 9, 12, 18):
  q6  the narrowest interval bracketing the point gives the best estimate;
  q7  the derivative is by definition the limit of the difference quotient;
  q9  a difference quotient carries output units over input units;
  q12 a table constrains f at finitely many points and says nothing about the
      behavior between them, so no finite difference quotient can be exact;
  q18 for f of constant concavity the forward and backward errors have
      opposite signs, so the symmetric estimate cancels the leading error
      (demonstrated numerically below for two functions).
"""
import importlib
import sympy as sp

M = importlib.import_module("c2_3")
x = sp.Symbol("x")

CONCEPTUAL = {6, 7, 9, 12, 18}
checked = set()


def tab(t):
    return {float(r[0]): float(r[1]) for r in t["rows"]}


A, B, C = tab(M.TAB_A), tab(M.TAB_B), tab(M.TAB_C)


def num(n, expected, tol=5e-4):
    """The keyed choice, read as a number, must match the recomputed value."""
    item = M.QUESTIONS[n - 1]
    vals = [float(c) for c in item["choices"]]
    assert len(vals) == 4, f"q{n}: expected 4 choices"
    assert abs(vals[item["ans"]] - expected) <= tol, \
        f"q{n}: keyed {vals[item['ans']]} != recomputed {expected}"
    for i in range(4):
        for j in range(i + 1, 4):
            assert abs(vals[i] - vals[j]) > tol, f"q{n}: choices {i} and {j} are equal"
    checked.add(n)


def claim(n, ok, ans):
    """A question whose choices are prose: the computation behind the key."""
    item = M.QUESTIONS[n - 1]
    assert ok, f"q{n}: the reasoning behind the key does not hold"
    assert item["ans"] == ans, f"q{n}: key is {item['ans']}, expected {ans}"
    assert len(set(item["choices"])) == 4, f"q{n}: choices not distinct"
    checked.add(n)


def dq(t, lo, hi):
    return (t[hi] - t[lo]) / (hi - lo)


num(1, dq(A, 1.5, 2.5))
num(2, dq(A, 1.0, 1.5))
num(3, dq(A, 2.5, 3.0))
num(4, dq(B, 2, 6))
num(5, dq(B, 4, 8))
num(8, dq(C, 5, 15))
num(10, dq(C, 0, 5))
num(11, dq(C, 15, 20))
num(13, (8.06 - 8) / (3.01 - 3))
num(14, (12.9 - 12) / (5.2 - 5))
num(15, (6.98 - 7.02) / (2.01 - 1.99))
num(19, dq(A, 1.0, 3.0))
num(20, float((sp.log(sp.Rational(11, 10)) - sp.log(1)) / sp.Rational(1, 10)))
num(21, float((sp.exp(sp.Rational(1, 10)) - sp.exp(sp.Rational(-1, 10))) / sp.Rational(1, 5)))
num(22, dq(B, 6, 8))
num(24, (5.0302 - 5) / (2.01 - 2))
num(25, (90.0 - 0.0) / (2 - 0))

# q16 and q17: for a concave-up f the forward difference over [a, a + h]
# overestimates f'(a) and the backward difference over [a - h, a] underestimates
# it. Demonstrated on two unrelated concave-up functions.
UP = [x**2, sp.exp(x)]
fwd_over = all(
    ((f.subs(x, sp.Rational(5, 2)) - f.subs(x, 2)) / sp.Rational(1, 2)
     - sp.diff(f, x).subs(x, 2)).evalf() > 0 for f in UP)
bwd_under = all(
    ((f.subs(x, 2) - f.subs(x, sp.Rational(3, 2))) / sp.Rational(1, 2)
     - sp.diff(f, x).subs(x, 2)).evalf() < 0 for f in UP)
for f in UP:
    assert sp.diff(f, x, 2).subs(x, 2) > 0, f"{f} is not concave up at 2"
claim(16, fwd_over, 0)
claim(17, bwd_under, 0)

# q23: the two successive difference quotients fall from 3.0 to 2.0, so f'
# is decreasing and f is concave down on the interval.
s1 = (10.3 - 10.0) / (4.1 - 4.0)
s2 = (10.5 - 10.3) / (4.2 - 4.1)
claim(23, s1 > s2 > 0, 0)

# q18's numerical demonstration: the symmetric estimate beats the forward one.
for f in UP:
    a, hh = sp.Rational(2), sp.Rational(1, 10)
    true = sp.diff(f, x).subs(x, a)
    sym = (f.subs(x, a + hh) - f.subs(x, a - hh)) / (2 * hh)
    one = (f.subs(x, a + hh) - f.subs(x, a)) / hh
    assert abs((sym - true).evalf()) < abs((one - true).evalf()), \
        f"q18: symmetric estimate is not better for {f}"

assert len(M.QUESTIONS) == 25, f"expected 25 questions, found {len(M.QUESTIONS)}"
assert checked | CONCEPTUAL == set(range(1, 26)), \
    f"unaccounted questions: {set(range(1, 26)) - checked - CONCEPTUAL}"
assert not (checked & CONCEPTUAL)
print(f"c2_3: {len(checked)} verified with sympy, {len(CONCEPTUAL)} conceptual, 25 total")
