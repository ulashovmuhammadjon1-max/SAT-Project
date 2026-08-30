"""Verification for AP STATISTICS 1.3, tabular summaries of one categorical variable.

Every count is read back out of the module's own table objects rather than
retyped here, so the checks below fail if a table is edited and a key is not.
The three tables are first checked for internal consistency (the category counts
must add to the stated total); then every relative frequency, percent, count,
difference and ratio keyed in the module is recomputed from those counts.

Items whose key is prose -- the two claim-evaluation questions and the
recover-the-count question -- cannot go through ``Checker.check``, which is for
numeric choices. Their arithmetic is still computed here, in ``prose_arithmetic``,
and asserted against the value quoted in the key text; only the definitional
items are left as pure reasoning.

Run: python3 verify_s1_3.py
"""
import s_verify_util as U

import s1_3

c = U.Checker(s1_3)


def counts(table):
    """Category -> count, from a module table, excluding the Total row."""
    out = {}
    for label, value in table["rows"]:
        if label.lower() == "total":
            continue
        out[label] = int(value)
    return out


def total(table):
    for label, value in table["rows"]:
        if label.lower() == "total":
            return int(value)
    raise AssertionError("table has no Total row")


A, B, C = s1_3.TABLE_A, s1_3.TABLE_B, s1_3.TABLE_C
a, b, cc = counts(A), counts(B), counts(C)
nA, nB, nC = total(A), total(B), total(C)

# --- the tables must be internally consistent before anything is keyed off them
for name, cnt, n in (("A", a, nA), ("B", b, nB), ("C", cc, nC)):
    assert sum(cnt.values()) == n, (
        f"table {name}: categories sum to {sum(cnt.values())}, total row says {n}")

# --- computed keys -----------------------------------------------------------
c.check(4, a["Soccer"] / nA)                                  # 64/200  = 0.32
c.check(5, a["Tennis"] / nA * 100)                            # 36/200  = 18%
c.check(6, a["Soccer"] - a["Tennis"])                         # 64 - 36 = 28
c.check(7, (a["Soccer"] + a["Basketball"]) / nA)              # 116/200 = 0.58
c.check(8, [13, 12], note="52:48 reduced by the gcd 4")       # ratio Basketball:Swimming
c.check(9, nA - a["Soccer"])                                  # 200 - 64 = 136

c.check(11, b["A"] / nB)                                      # 88/250  = 0.352
c.check(12, b["AB"] / nB * 100)                               # 15/250  = 6%
c.check(13, (b["O"] + b["A"]) / nB)                           # 198/250 = 0.792
c.check(14, nB - b["O"])                                      # 250-110 = 140
c.check(15, b["O"] / b["AB"], tol=0.01)                       # 110/15 ~= 7.3

c.check(17, cc["Car"] / nC * 100)                             # 220/400 = 55%
c.check(18, (cc["Bicycle"] + cc["Walk"]) / nC)                # 84/400  = 0.21
c.check(19, (nC - cc["Car"]) / nC)                            # 180/400 = 0.45
c.check(21, (cc["Car"] - cc["Bus"]) / nC * 100)               # 124/400 = 31%

c.check(23, 45 / (45 + 30 + 25))                              # 45/100  = 0.45

# The reduced ratio in q8 is asserted rather than assumed: 52:48 must reduce to 13:12.
from math import gcd
_g = gcd(a["Basketball"], a["Swimming"])
assert (a["Basketball"] // _g, a["Swimming"] // _g) == (13, 12), "q8 ratio does not reduce to 13:12"


def prose_arithmetic():
    """Arithmetic behind the three questions whose keys are sentences."""
    # q10: the claim is 'fewer than one in five chose Swimming'. Swimming's
    # relative frequency exceeds 0.20, so the claim is false.
    swim = a["Swimming"] / nA
    assert abs(swim - 0.24) < 1e-12, f"q10: Swimming relative frequency is {swim}, key says 0.24"
    assert swim > 0.20, "q10: the key calls the 'fewer than one in five' claim incorrect"

    # q16: 0.148 of 250 donors recovers the type B count of 37.
    assert round(0.148 * nB) == b["B"] == 37, "q16: 0.148 x 250 must recover 37 type B donors"

    # q20: the claim is 'more than a quarter take the bus'. 96/400 = 0.24 < 0.25,
    # so the claim is false -- and it is false by a small margin, which is the point.
    bus = cc["Bus"] / nC
    assert abs(bus - 0.24) < 1e-12, f"q20: bus relative frequency is {bus}, key says 0.24"
    assert bus < 0.25, "q20: the key calls the 'more than a quarter' claim incorrect"
    assert nC // 4 == 100 and cc["Bus"] == 96, "q20: a quarter of 400 is 100 and the bus count is 96"
    return swim, bus


_swim, _bus = prose_arithmetic()

# --- conceptual keys ---------------------------------------------------------
c.conceptual(1, "EK 1.3.A.1: a frequency table shows the number of observational units in each category.")
c.conceptual(2, "EK 1.3.A.2: a relative frequency table shows the proportion of observational units in each category.")
c.conceptual(3, "EK 1.3.A.2: each unit falls in exactly one category, so the proportions account for the whole sample and sum to 1.")
c.conceptual(10, f"EK 1.3.B.2: computed above, Swimming's relative frequency is {_swim}, which exceeds one in five (0.20), so the claim is incorrect.")
c.conceptual(16, "EK 1.3.A.1 and 1.3.A.2: a relative frequency times the total recovers the count, and 0.148 x 250 = 37 as asserted above.")
c.conceptual(20, f"EK 1.3.B.2: computed above, the bus relative frequency is {_bus}, short of the 0.25 the claim requires, so the claim is incorrect.")
c.conceptual(22, "EK 1.3.B.1: percentages, relative frequencies, ratios and proportions all convey the same distributional information in different forms.")
c.conceptual(24, "EK 1.3.B.1: counts are not comparable across groups of different sizes, so relative frequencies are the fair comparison.")
c.conceptual(25, "EK 1.3.A.2: relative frequencies give shares directly, but recovering any count requires the total, which this question withholds.")

c.finish()
