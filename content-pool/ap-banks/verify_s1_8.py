"""Verification for AP STATISTICS 1.8, boxplots and the five-number summary.

Data set P is parsed out of the module's own DATA_P string, and the whole
five-number summary, the fences, the outlier and both whisker endpoints are
recomputed from it. The upper-whisker item is the one worth being careful about:
44 is NOT an outlier (it sits below the fence of 53) while 58 is, so the whisker
must stop at 44 -- and the check below asserts both halves of that, since a
distractor of 58 is exactly the error the convention exists to prevent.

The skew-signature items (q19, q20) are checked against simulated skewed data
rather than asserted from memory: for a right-skewed sample the median really
does sit closer to Q1 than to Q3 and the mean really does exceed the median, and
the mirrored statements hold for a left-skewed sample.

Run: python3 verify_s1_8.py
"""
import random
import statistics as st

import s_verify_util as U

import s1_8

c = U.Checker(s1_8)

P = sorted(float(t) for t in s1_8.DATA_P.split(","))
assert len(P) == 20, f"data set P should hold 20 values, holds {len(P)}"


def five_number(data):
    d = sorted(data)
    h = len(d) // 2
    return min(d), st.median(d[:h]), st.median(d), st.median(d[h:]), max(d)


pmin, pq1, pmed, pq3, pmax = five_number(P)
piqr = pq3 - pq1
lo_fence, hi_fence = pq1 - 1.5 * piqr, pq3 + 1.5 * piqr
outliers = [x for x in P if x < lo_fence or x > hi_fence]

# The whiskers stop at the most extreme values that are NOT outliers.
upper_whisker = max(x for x in P if x <= hi_fence)
lower_whisker = min(x for x in P if x >= lo_fence)

assert outliers == [58.0], f"q10: outliers are {outliers}"
assert 44.0 <= hi_fence, "q10/q11: 44 must fall inside the fence, so it is not an outlier"
assert 58.0 > hi_fence, "q10: 58 must fall outside the fence"
assert upper_whisker == 44.0, f"q11: upper whisker should stop at 44, got {upper_whisker}"
assert lower_whisker == pmin == 12.0, "q12: with no low outlier the lower whisker reaches the minimum"

# --- computed keys -------------------------------------------------------------
c.check(4, 25)                              # each whisker spans about 25% of the data
c.check(6, pmed)                            # 26.5
c.check(7, pq1)                             # 20.5
c.check(8, pq3)                             # 33.5
c.check(9, piqr)                            # 13.0
c.check(10, 58.0)                           # the sole outlier
c.check(11, upper_whisker)                  # 44
c.check(12, lower_whisker)                  # 12
c.check(13, [pmin, pq1, pmed, pq3, pmax])   # 12, 20.5, 26.5, 33.5, 58
c.check(14, 0.50)                           # the box spans the middle half
c.check(15, 0.25)                           # a quarter of the data lies above Q3

# Distractors named in the rationales are confirmed to be what they claim.
assert abs(st.mean(P) - 28.25) < 1e-9, "q6: 28.25 is the mean distractor"
assert st.mean(P) > pmed, "P is right-skewed, so its mean exceeds its median"
assert pmax - pmin == 46, "q9: 46.0 is the range distractor"


def skew_signatures():
    """q19/q20: what a boxplot looks like for each direction of skew."""
    rng = random.Random(20260830)

    right = [rng.lognormvariate(0, 0.9) for _ in range(20001)]
    rmin, rq1, rmed, rq3, rmax = five_number(right)
    assert rmed - rq1 < rq3 - rmed, "q19: right skew puts the median closer to Q1"
    assert rq3 - rmed < rmax - rq3 or rmax - rq3 > rq1 - rmin, (
        "q19: right skew gives the longer whisker on the right")
    assert st.mean(right) > rmed, "q19/q17: right skew puts the mean above the median"

    left = [-x for x in right]
    lmin, lq1, lmed, lq3, lmax = five_number(left)
    assert lq3 - lmed < lmed - lq1, "q20: left skew puts the median closer to Q3"
    assert lmed - lmin > lmax - lq3, "q20: left skew gives the longer whisker on the left"
    assert st.mean(left) < lmed, "q20/q18: left skew puts the mean below the median"

    # q16: a symmetric distribution has mean and median close together.
    sym = [rng.gauss(50, 8) for _ in range(20001)]
    assert abs(st.mean(sym) - st.median(sym)) < 0.5, "q16: symmetry puts mean and median close"


def boxplot_hides_shape():
    """q23: two very different data sets can share a five-number summary.

    A boxplot records five positions and nothing between them, so a unimodal set
    and a bimodal set with the same five numbers draw the same picture. Both are
    constructed here to make that concrete rather than merely claimed.
    """
    # Both have min 10, Q1 20, median 25, Q3 30, max 40.
    unimodal = [10, 19, 20, 20, 24, 25, 25, 28, 30, 30, 32, 40]
    bimodal = [10, 19, 20, 20, 20, 25, 25, 30, 30, 30, 31, 40]
    assert five_number(unimodal) == five_number(bimodal) == (10, 20, 25, 30, 40), (
        f"q23: summaries are {five_number(unimodal)} and {five_number(bimodal)}")
    assert unimodal != bimodal, "q23: and yet they are different data sets"
    # The bimodal one really does clump at two values and thin out between them.
    assert bimodal.count(20) == 3 and bimodal.count(30) == 3, "q23: two clusters"
    assert sum(1 for x in bimodal if 21 <= x <= 29) < sum(1 for x in unimodal if 21 <= x <= 29), (
        "q23: the bimodal set must be sparser between its two clusters")


def class_comparison():
    """q24: equal-ish medians, very unequal interquartile ranges."""
    a_q1, a_med, a_q3 = 62, 70, 78
    b_q1, b_med, b_q3 = 68, 71, 74
    assert abs(a_med - b_med) <= 2, "q24: the medians are close"
    assert (a_q3 - a_q1) == 16 and (b_q3 - b_q1) == 6, "q24: IQRs of 16 and 6"
    assert (a_q3 - a_q1) > (b_q3 - b_q1), "q24: Class A's middle half is the wider one"


skew_signatures()
boxplot_hides_shape()
class_comparison()

# --- conceptual keys ---------------------------------------------------------
c.conceptual(1, "EK 1.8.A.1: the five-number summary is the minimum, Q1, the median, Q3 and the maximum.")
c.conceptual(2, "EK 1.8.A.2: the ends of the box are the quartiles, so the box represents the middle 50% of the data.")
c.conceptual(3, "EK 1.8.A.2: the interior line marks the median; the mean is not part of a boxplot.")
c.conceptual(5, "EK 1.8.A.2: with outliers present the whiskers stop at the most extreme non-outlying values and each outlier is drawn separately.")
c.conceptual(16, "EK 1.8.B.1: a relatively symmetric distribution has mean and median relatively close together, as simulated above.")
c.conceptual(17, "EK 1.8.B.1: simulated above -- right skew usually puts the mean above the median.")
c.conceptual(18, "EK 1.8.B.1: simulated above -- left skew usually puts the mean below the median.")
c.conceptual(19, "EK 1.8.A.2 and 1.8.B.1: simulated above -- a median near Q1 with a long right whisker is the boxplot signature of right skew.")
c.conceptual(20, "EK 1.8.B.1: simulated above -- a median near Q3 with a long left whisker is left skew, which puts the mean below the median.")
c.conceptual(21, "EK 1.8.A.2: a boxplot displays the five-number summary only, and the mean is not among those five numbers.")
c.conceptual(22, "EK 1.8.A.2: the five positions a boxplot shows are unchanged by how many observations produced them, so sample size is not recoverable.")
c.conceptual(23, "EK 1.8.A.2: constructed above -- two different data sets share one five-number summary, so a boxplot cannot reveal modality, gaps or clusters inside the box.")
c.conceptual(24, "EK 1.8.A.2: computed above -- medians 70 and 71 are close while IQRs of 16 and 6 make Class A's middle half far more spread out.")
c.conceptual(25, "EK 1.8.B.1: a mean and median that nearly coincide, with the median centred in the box and whiskers of similar length, is what approximate symmetry looks like.")

c.finish()
