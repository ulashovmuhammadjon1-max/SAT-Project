"""Plain-text -> sympy helpers shared by the Unit 9 (BC) verify scripts.

The modules are written in the bank's plain-text notation (`3t^2`, `sqrt(...)`,
`int from 0 to 2 of ... dt`).  These helpers parse that notation so every key
can be compared against a value sympy computes independently, and so the four
choices can be checked for pairwise NON-equivalence rather than merely for
being different strings.
"""
import re

import sympy as sp
from sympy.parsing.sympy_parser import (
    convert_xor,
    implicit_multiplication_application,
    parse_expr,
    standard_transformations,
)

TRANSFORMS = standard_transformations + (convert_xor, implicit_multiplication_application)

t, th, x, y, a, b = sp.symbols("t theta x y a b", real=True)

LOCAL = {
    "t": t, "theta": th, "x": x, "y": y, "a": a, "b": b,
    "e": sp.E, "pi": sp.pi,
    "sqrt": sp.sqrt, "ln": sp.log, "log": sp.log, "exp": sp.exp,
    "sin": sp.sin, "cos": sp.cos, "tan": sp.tan,
    "sec": sp.sec, "csc": sp.csc, "cot": sp.cot,
    "arctan": sp.atan, "arcsin": sp.asin, "arccos": sp.acos,
}


def P(s):
    """Parse one plain-text math expression into a sympy expression."""
    return parse_expr(s, local_dict=LOCAL, transformations=TRANSFORMS)


INT_RE = re.compile(
    r"^\s*(?:\(\s*)?(?P<pre>[-+0-9/.()\s*]*?)\s*(?:\)\s*)?"
    r"int\s+from\s+(?P<lo>.+?)\s+to\s+(?P<hi>.+?)\s+of\s+(?P<f>.+?)\s+d(?:t|theta|x)\s*$"
)


def PI_(s):
    """Parse `c int from A to B of f dt` -> (coefficient, lo, hi, integrand)."""
    m = INT_RE.match(s)
    if not m:
        raise ValueError(f"not an integral in bank notation: {s!r}")
    pre = m.group("pre").strip()
    coeff = P(pre) if pre not in ("", "+") else sp.Integer(1)
    if pre == "-":
        coeff = sp.Integer(-1)
    return coeff, P(m.group("lo")), P(m.group("hi")), P(m.group("f"))


def value_of(s):
    """Numeric/symbolic value of a choice: an integral is evaluated, else parsed."""
    try:
        c, lo, hi, f = PI_(s)
    except ValueError:
        return P(s)
    var = th if re.search(r"d\s*theta\s*$", s) else t
    return c * sp.integrate(f, (var, lo, hi))


class Checker:
    """Per-module answer checker.

    ck(i, expected) verifies question i's keyed choice equals `expected` and
    that no other choice is equivalent to it.  ck_int(i, lo, hi, f, c=1)
    does the same for a set-up question whose choices are integrals.
    """

    def __init__(self, module):
        self.M = module
        self.checked = set()

    def _q(self, i):
        return self.M.QUESTIONS[i - 1]

    def _others(self, i):
        q = self._q(i)
        return [c for j, c in enumerate(q["choices"]) if j != q["ans"]]

    def key(self, i):
        q = self._q(i)
        return q["choices"][q["ans"]]

    def ck(self, i, expected, parse=P):
        got = parse(self.key(i))
        assert sp.simplify(got - expected) == 0, f"q{i}: key {self.key(i)!r} != {expected}"
        for c in self._others(i):
            try:
                other = parse(c)
            except Exception:
                continue
            assert sp.simplify(other - expected) != 0, f"q{i}: distractor {c!r} equals the key"
        self.checked.add(i)

    def ck_val(self, i, expected):
        """Like ck but choices may be integrals in bank notation."""
        self.ck(i, expected, parse=value_of)

    def ck_num(self, i, expected, tol=sp.Rational(1, 1000)):
        """Key is a rounded decimal: compare numerically, distractors too."""
        got = P(self.key(i))
        assert abs(sp.N(got - expected)) <= tol, f"q{i}: key {self.key(i)!r} != {sp.N(expected)}"
        for c in self._others(i):
            try:
                other = P(c)
            except Exception:
                continue
            assert abs(sp.N(other - expected)) > tol, f"q{i}: distractor {c!r} equals the key"
        self.checked.add(i)

    def ck_int(self, i, lo, hi, integrand, coeff=1):
        c, l, h, f = PI_(self.key(i))
        assert sp.simplify(c - coeff) == 0, f"q{i}: coefficient {c} != {coeff}"
        assert sp.simplify(l - lo) == 0 and sp.simplify(h - hi) == 0, f"q{i}: limits {l}..{h}"
        assert sp.simplify(f - integrand) == 0, f"q{i}: integrand {f} != {integrand}"
        for other in self._others(i):
            try:
                c2, l2, h2, f2 = PI_(other)
            except ValueError:
                continue
            same = (
                sp.simplify(c2 - coeff) == 0
                and sp.simplify(l2 - lo) == 0
                and sp.simplify(h2 - hi) == 0
                and sp.simplify(f2 - integrand) == 0
            )
            assert not same, f"q{i}: distractor {other!r} matches the key"
        self.checked.add(i)

    def ck_text(self, i, expected_substring, reason):
        """A conceptual question: the key is prose, so pin it by content.

        `reason` documents the mathematics that makes it correct; it is not a
        computation, and the module header says which questions these are.
        """
        assert expected_substring in self.key(i), f"q{i}: key is {self.key(i)!r}"
        assert reason
        self.checked.add(i)

    def distinct(self, i):
        """Pairwise non-equivalence for every choice that parses.

        Integrals are compared as (coefficient, limits, integrand) rather than
        evaluated, so a set-up question is checked without asking sympy for a
        closed form it may not have.
        """
        vals = []
        for c in self._q(i)["choices"]:
            try:
                vals.append((c, sp.Tuple(*PI_(c))))
                continue
            except ValueError:
                pass
            except Exception:
                continue
            try:
                vals.append((c, P(c)))
            except Exception:
                pass
        for j in range(len(vals)):
            for k in range(j + 1, len(vals)):
                a, b_ = vals[j][1], vals[k][1]
                seq = (sp.Tuple, tuple, list)
                if isinstance(a, seq) and isinstance(b_, seq):
                    same = len(a) == len(b_) and all(
                        sp.simplify(u - v) == 0 for u, v in zip(a, b_)
                    )
                elif isinstance(a, seq) or isinstance(b_, seq):
                    same = False
                else:
                    try:
                        same = sp.simplify(a - b_) == 0
                    except TypeError:  # relationals and other non-numeric parses
                        same = a == b_
                assert not same, (
                    f"q{i}: choices {vals[j][0]!r} and {vals[k][0]!r} are equivalent"
                )

    def finish(self, n=25):
        qs = self.M.QUESTIONS
        assert len(qs) == n, f"expected {n} questions, found {len(qs)}"
        for i, q in enumerate(qs, 1):
            assert len(q["choices"]) == 4, f"q{i}: {len(q['choices'])} choices"
            assert len(set(q["choices"])) == 4, f"q{i}: repeated choice string"
            assert 0 <= q["ans"] < 4, f"q{i}: bad answer index"
            assert q["why"].strip(), f"q{i}: no explanation"
            self.distinct(i)
        missing = [i for i in range(1, n + 1) if i not in self.checked]
        assert not missing, f"unchecked questions: {missing}"
        print(f"{self.M.__name__}: {n} questions verified")
