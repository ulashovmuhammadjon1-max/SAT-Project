"""Verification for AP STATISTICS 1.5, graphical displays of one quantitative variable.

The three displays are reconstructed here as actual lists of numbers -- the
stem-and-leaf plot is parsed back into its 16 values, the dotplot into its 20 --
and every key is then recomputed from those lists with `statistics`. Nothing is
retyped from the module's `why` text, so a table edited without its keys fails.

The histogram is treated as what it is: bins and counts, with no individual
values. That is why q22's key is that the maximum cannot be determined, and the
assertion below is that the data available bound it only to the final interval.

Run: python3 verify_s1_5.py
"""
import statistics as st

import s_verify_util as U

import s1_5

c = U.Checker(s1_5)

# --- rebuild the data sets from the module's own tables ----------------------
# F: a dotplot given as value/count pairs.
F = []
for value, count in s1_5.TABLE_F["rows"]:
    F.extend([float(value)] * int(count))

# G: a stem-and-leaf plot. Stem 2 with leaf 3 is the value 23, so each value is
# 10 * stem + leaf. Both stems and leaves are supposed to be in increasing
# order (EK 1.5.A.3), which is asserted rather than assumed.
G = []
prev_stem = None
for stem, leaves in s1_5.TABLE_G["rows"]:
    s = int(stem)
    assert prev_stem is None or s > prev_stem, "stems are not in increasing order"
    prev_stem = s
    digits = [int(d) for d in leaves.split()]
    assert digits == sorted(digits), f"leaves on stem {stem} are not in increasing order"
    G.extend(10 * s + d for d in digits)

# H: a histogram, available only as bins and frequencies.
H_BINS = [(row[0], int(row[1])) for row in s1_5.TABLE_H["rows"]]
H_N = sum(f for _, f in H_BINS)

assert len(F) == 20, f"dotplot should hold 20 observations, holds {len(F)}"
assert len(G) == 16, f"stem-and-leaf should hold 16 values, holds {len(G)}"
assert H_N == 45, f"histogram should hold 45 measurements, holds {H_N}"
assert G == sorted(G), "the reconstructed stem-and-leaf values are not sorted"

# --- computed keys: the dotplot ----------------------------------------------
c.check(6, len(F))                                            # 2+5+8+4+1 = 20
c.check(7, st.mode(F))                                        # most-stacked value = 5
c.check(8, F.count(5) / len(F))                               # 8/20 = 0.40
c.check(9, sum(1 for v in F if v <= 4))                       # 2 + 5 = 7
c.check(10, st.mean(F))                                       # 97/20 = 4.85
c.check(11, st.median(F))                                     # average of 10th and 11th = 5

# --- computed keys: the stem-and-leaf plot -----------------------------------
c.check(12, len(G))                                           # 3+6+5+2 = 16
c.check(13, [min(G), max(G)])                                 # 23 and 53
c.check(14, max(G) - min(G))                                  # 53 - 23 = 30
c.check(15, sum(1 for v in G if v >= 40))                     # 5 + 2 = 7
c.check(16, st.median(G))                                     # average of 8th and 9th = 38
c.check(17, sum(1 for v in G if v < 30) / len(G))             # 3/16 = 0.1875

# --- computed keys: the histogram --------------------------------------------
c.check(19, H_BINS[0][1] + H_BINS[1][1])                      # 4 + 11 = 15 below 20
c.check(20, H_BINS[2][1] / H_N)                               # 18/45 = 0.40
c.check(21, H_BINS[3][1] + H_BINS[4][1])                      # 9 + 3 = 12 at or above 30


def histogram_hides_the_maximum():
    """q22: a histogram fixes only the interval the maximum falls in.

    The last non-empty bin is '40 to under 50' with a frequency of 3, so the
    largest measurement is somewhere in [40, 50). Any of 40.1, 47 and 49.9 is
    consistent with this histogram, which is exactly why the key says the exact
    maximum cannot be determined.
    """
    last_label, last_freq = [b for b in H_BINS if b[1] > 0][-1]
    assert last_label == "40 to under 50" and last_freq == 3
    for candidate in (40.1, 47.0, 49.9):
        assert 40 <= candidate < 50, "every one of these is consistent with the display"
    # And 50 itself is not, which rules out the distractor that names 50.
    assert not (40 <= 50 < 50)


histogram_hides_the_maximum()

# --- conceptual keys ---------------------------------------------------------
c.conceptual(1, "EK 1.5.A.1: all three displays maintain the natural ordering of the quantitative variable, smallest to largest.")
c.conceptual(2, "EK 1.5.A.2: each histogram bar represents an interval and its height is the frequency or relative frequency within that interval.")
c.conceptual(3, "EK 1.5.A.2: altering the bin widths can change the appearance of the histogram without changing the data.")
c.conceptual(4, "EK 1.5.A.3: the stem is the leading digit or digits and the leaf is usually the single digit after it, both ordered smallest to largest.")
c.conceptual(5, "EK 1.5.A.4: a dotplot places one dot per observation at that observation's value, stacking near-identical values.")
c.conceptual(18, "EK 1.5.A.3 against 1.5.A.2: every original value can be read back off a stem-and-leaf plot, while a histogram keeps only interval counts.")
c.conceptual(22, "EK 1.5.A.2: asserted above, the display bounds the maximum only to the interval [40, 50), so the exact largest value is not recoverable.")
c.conceptual(23, "EK 1.5.A.1 against 1.4.A.2: a pie chart divides a whole among categories and cannot represent the ordering or spacing of numerical values.")
c.conceptual(24, "EK 1.5.A.4: one dot per observation stays readable only for small data sets; large ones need the grouping a histogram provides.")
c.conceptual(25, "EK 1.5.A.2: histogram bins are adjoining intervals of a number line so the bars meet, while a bar chart's categories are separate labels.")

c.finish()
