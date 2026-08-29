"""sympy verification for CALC 6.2 Approximating Areas with Riemann Sums.

The tables are imported from the module itself, so every sum below is computed
from exactly the numbers the student is shown.  Riemann sums over a table are
built by a general routine (unequal widths included) rather than by copying an
arithmetic result, and the sums of formula-defined functions are compared with
the exact integral from sp.integrate.

CONCEPTUAL questions -- no computation, reasoning stated here:
  1  a left sum samples the left endpoint (definition)
  5  increasing f => left sum underestimates (left endpoint is the minimum)
 14  decreasing g => right sum underestimates (right endpoint is the minimum)
 18  concave up => chords lie above the curve => trapezoid overestimates
 19  concave up => the midpoint rectangle equals the area under the tangent
     line at the midpoint, which lies below the curve => underestimate
 20  concave down => chords lie below the curve => trapezoid underestimates
 22  increasing f => right sum is the guaranteed overestimate; midpoint and
     trapezoid depend on concavity instead
 23  for continuous f every choice of sample points has the same limit
 25  h increases then decreases with no partition point at the turn, so the
     left-endpoint errors have both signs and do not have to cancel one way
"""
import re
import sympy as sp

from c6_2 import QUESTIONS, TAB_A, TAB_B, TAB_C, TAB_D

x = sp.Symbol('x', positive=True)

CONCEPTUAL = {1, 5, 14, 18, 19, 20, 22, 23, 25}
checked = set()


def pts(tab):
    return [(sp.Rational(a), sp.Rational(b)) for a, b in tab["rows"]]


def left_sum(tab):
    p = pts(tab)
    return sum((p[i + 1][0] - p[i][0]) * p[i][1] for i in range(len(p) - 1))


def right_sum(tab):
    p = pts(tab)
    return sum((p[i + 1][0] - p[i][0]) * p[i + 1][1] for i in range(len(p) - 1))


def trap_sum(tab):
    p = pts(tab)
    return sum((p[i + 1][0] - p[i][0]) * (p[i][1] + p[i + 1][1]) / 2
               for i in range(len(p) - 1))


def table_lookup(tab, xv):
    for a, b in pts(tab):
        if a == xv:
            return b
    raise KeyError(xv)


def coarse(tab, step):
    """Sub-table keeping only the rows whose x is a multiple of `step`."""
    rows = [r for r in tab["rows"] if sp.Rational(r[0]) % step == 0]
    return dict(headers=tab["headers"], rows=rows)


def midpoint_sum(tab, lo, hi, n):
    """Midpoint sum for a table that carries the midpoints as sample rows."""
    w = sp.Rational(hi - lo, n)
    return sum(w * table_lookup(tab, lo + w * (k + sp.Rational(1, 2)))
               for k in range(n))


def riemann(f, lo, hi, n, kind):
    w = sp.Rational(hi - lo, n)
    off = {"left": 0, "right": 1, "mid": sp.Rational(1, 2)}[kind]
    return sum(w * f.subs(x, lo + w * (k + off)) for k in range(n))


def chk(i, computed, values):
    q = QUESTIONS[i - 1]
    assert len(values) == len(q["choices"]), f"q{i}: wrong number of values"
    for a in range(len(values)):
        for b in range(a + 1, len(values)):
            assert sp.simplify(values[a] - values[b]) != 0, f"q{i}: choices {a},{b} equal"
    for v, text in zip(values, q["choices"]):
        m = re.search(r"-?\d+(?:\.\d+)?", text)
        assert m, f"q{i}: no number in {text!r}"
        assert abs(float(m.group()) - float(v)) < 0.0011, f"q{i}: {text!r} != {float(v)}"
    assert sp.simplify(computed - values[q["ans"]]) == 0, f"q{i}: key mismatch"
    checked.add(i)


# --- the monotonicity the conceptual questions 5 and 14 rely on -------------
assert all(pts(TAB_A)[i][1] < pts(TAB_A)[i + 1][1] for i in range(len(TAB_A["rows"]) - 1))
assert all(pts(TAB_C)[i][1] > pts(TAB_C)[i + 1][1] for i in range(len(TAB_C["rows"]) - 1))

# --- TAB_A, four unequal subintervals --------------------------------------
A_L, A_R, A_T = left_sum(TAB_A), right_sum(TAB_A), trap_sum(TAB_A)
assert A_T == (A_L + A_R) / 2
chk(2, A_L, [95, 110, 125, 168])
chk(3, A_R, [95, 110, 125, 168])
chk(4, A_T, [95, 110, 125, 220])

# --- TAB_B, width 1 (n = 6) and width 2 (n = 3) ----------------------------
chk(6, left_sum(TAB_B), [46, sp.Rational(105, 2), 59, 62])
chk(7, right_sum(TAB_B), [46, sp.Rational(105, 2), 59, 62])
chk(8, midpoint_sum(TAB_B, 0, 6, 3), [40, 52, 53, 66])
chk(9, trap_sum(TAB_B), [46, sp.Rational(105, 2), 53, 59])
B3 = coarse(TAB_B, 2)
assert [r[0] for r in B3["rows"]] == ["0", "2", "4", "6"]
chk(10, trap_sum(B3), [40, 52, 53, 66])

# --- TAB_C, three unequal subintervals -------------------------------------
C_L, C_R, C_T = left_sum(TAB_C), right_sum(TAB_C), trap_sum(TAB_C)
assert C_T == (C_L + C_R) / 2
chk(11, C_L, [89, sp.Rational(227, 2), 138, 170])
chk(12, C_R, [89, sp.Rational(227, 2), 138, 170])
chk(13, C_T, [89, sp.Rational(227, 2), 138, 227])

# --- x^2 on [0, 4]; the exact integral is 64/3, between the midpoint and
#     trapezoidal values, as it must be for a concave-up function ------------
exact = sp.integrate(x**2, (x, 0, 4))
assert exact == sp.Rational(64, 3)
chk(15, riemann(x**2, 0, 4, 4, "right"), [14, 21, 22, 30])
chk(16, riemann(x**2, 0, 4, 4, "left"), [14, 21, 22, 30])
chk(17, riemann(x**2, 0, 4, 4, "mid"), [14, 21, 22, 30])
trap_x2 = (riemann(x**2, 0, 4, 4, "left") + riemann(x**2, 0, 4, 4, "right")) / 2
assert trap_x2 == 22 and riemann(x**2, 0, 4, 4, "mid") < exact < trap_x2

# --- 1/x on [1, 3] ---------------------------------------------------------
r21 = riemann(1 / x, 1, 3, 4, "right")
l21 = riemann(1 / x, 1, 3, 4, "left")
assert r21 == sp.Rational(19, 20)
chk(21, r21, [sp.Rational(19, 20), (r21 + l21) / 2, l21, sp.Rational(19, 10)])
assert abs(float((r21 + l21) / 2) - 1.117) < 0.001 and abs(float(l21) - 1.283) < 0.001

# --- TAB_D, midpoint with two subintervals of width 20 ---------------------
D_mid = midpoint_sum(TAB_D, 0, 40, 2)
chk(24, D_mid, [660, 835, 880, 1010])
assert left_sum(TAB_D) == 660 and right_sum(TAB_D) == 1010 and trap_sum(TAB_D) == 835

assert checked | CONCEPTUAL == set(range(1, 26)), sorted(set(range(1, 26)) - (checked | CONCEPTUAL))
assert not (checked & CONCEPTUAL)
assert len(QUESTIONS) == 25
for i, q in enumerate(QUESTIONS, 1):
    assert len(q["choices"]) == 4 and len(set(q["choices"])) == 4, f"q{i}: choices"
    assert 0 <= q["ans"] < 4, f"q{i}: ans"
print(f"c6_2: {len(checked)} computational questions verified, "
      f"{len(CONCEPTUAL)} conceptual; all 25 checked for shape.")
