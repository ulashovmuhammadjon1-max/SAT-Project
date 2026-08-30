"""Verification for AP STATISTICS 1.6, describing a quantitative distribution.

No key in this topic is a number -- every answer is a shape word, a feature name
or a sentence -- so nothing here goes through ``Checker.check``. That does NOT
make the topic unverifiable. Each distribution is reconstructed from the
module's own frequency table into an actual list of values, and every shape
claim the module keys is then *computed* from that list:

* right skew is confirmed by mean > median, left skew by mean < median;
* the bimodal set is confirmed to have two interior local maxima and three
  values with zero frequency between them -- and its mean is confirmed to land
  inside that empty region, which is what makes q17's key true;
* the uniform set is confirmed to have no frequency standing out from the rest;
* the resistance claim in q20 is confirmed by simulation rather than asserted:
  across many data sets matching the stem's description, replacing the outlier
  with a typical value always moves the mean and standard deviation more than
  the median and interquartile range.

Run: python3 verify_s1_6.py
"""
import random
import statistics as st

import s_verify_util as U

import s1_6

c = U.Checker(s1_6)


def expand(table):
    """Turn a value/frequency table into the list of values it represents."""
    out = []
    for value, freq in table["rows"]:
        out.extend([float(value)] * int(freq))
    return out


def freqs(table):
    return [(float(v), int(f)) for v, f in table["rows"]]


RIGHT = expand(s1_6.TABLE_SKEW_R)
LEFT = expand(s1_6.TABLE_SKEW_L)
BIMODAL = expand(s1_6.TABLE_BIMODAL)
UNIFORM = expand(s1_6.TABLE_UNIFORM)

assert len(RIGHT) == 30 and len(LEFT) == 30, "the two skewed sets should hold 30 values each"
assert len(BIMODAL) == 40, f"the bimodal set should hold 40 values, holds {len(BIMODAL)}"
assert len(UNIFORM) == 42, f"the uniform set should hold 42 values, holds {len(UNIFORM)}"

# --- skew, confirmed by the mean/median relation ------------------------------
r_mean, r_med = st.mean(RIGHT), st.median(RIGHT)
l_mean, l_med = st.mean(LEFT), st.median(LEFT)
assert r_mean > r_med, f"q10/q11: right-skewed set has mean {r_mean} and median {r_med}"
assert l_mean < l_med, f"q12/q13: left-skewed set has mean {l_mean} and median {l_med}"

# The tail is longer on the side the skew is named for: for the right-skewed set
# the distance from the median up to the maximum exceeds the distance down to
# the minimum, and vice versa for the left-skewed set.
assert max(RIGHT) - r_med > r_med - min(RIGHT), "q10: the right tail must be the longer one"
assert l_med - min(LEFT) > max(LEFT) - l_med, "q12: the left tail must be the longer one"

# The two sets are deliberate mirror images of each other on the values 1..8.
assert sorted(f for _, f in freqs(s1_6.TABLE_SKEW_R)) == sorted(
    f for _, f in freqs(s1_6.TABLE_SKEW_L)), "the two skewed tables should mirror each other"
assert abs((9 - r_mean) - l_mean) < 1e-9, "mirrored sets should have mirrored means"

# --- bimodality, the gap, and the mean falling into it ------------------------
bf = freqs(s1_6.TABLE_BIMODAL)
empty = [v for v, f in bf if f == 0]
assert empty == [14.0, 15.0, 16.0], f"q16: the empty values are {empty}"

peaks = [i for i in range(1, len(bf) - 1)
         if bf[i][1] > bf[i - 1][1] and bf[i][1] > bf[i + 1][1]]
assert len(peaks) == 2, f"q15: expected two interior peaks, found {[bf[i][0] for i in peaks]}"
assert [bf[i][0] for i in peaks] == [12.0, 18.0], "q15: the peaks should sit at 12 and 18"

b_mean, b_med = st.mean(BIMODAL), st.median(BIMODAL)
assert min(empty) <= b_mean <= max(empty), (
    f"q17: the mean {b_mean} must land in the empty region {empty}")
assert min(empty) <= b_med <= max(empty), (
    f"q17: the median {b_med} also lands in the empty region -- neither centre describes the data")

# --- approximate uniformity ---------------------------------------------------
uf = [f for _, f in freqs(s1_6.TABLE_UNIFORM)]
assert max(uf) - min(uf) <= 2, f"q18: frequencies {uf} vary too much to call uniform"
assert max(uf) - min(uf) < 0.5 * st.mean(uf), "q18: no frequency should stand out as a peak"
# And it is genuinely not bimodal: no interior value is a strict local maximum
# with a strictly lower neighbour on each side by more than sampling wobble.
assert max(uf) - st.mean(uf) < 2, "q18: no prominent peak"


def outlier_resistance():
    """q19/q20, by simulation over data sets matching the stem.

    The stem fixes only that eleven values lie between 20 and 26 and the twelfth
    is 83, so the claim is checked over many data sets consistent with that
    description rather than over one hand-picked example. In each, the outlier is
    replaced by a typical value and the four summaries are compared.
    """
    rng = random.Random(20260830)
    for _ in range(2000):
        body = [rng.uniform(20, 26) for _ in range(11)]
        with_outlier = sorted(body + [83.0])
        without = sorted(body + [rng.uniform(20, 26)])

        d_mean = abs(st.mean(with_outlier) - st.mean(without))
        d_sd = abs(st.stdev(with_outlier) - st.stdev(without))
        d_med = abs(st.median(with_outlier) - st.median(without))

        q1a, q3a = st.median(with_outlier[:6]), st.median(with_outlier[6:])
        q1b, q3b = st.median(without[:6]), st.median(without[6:])
        d_iqr = abs((q3a - q1a) - (q3b - q1b))

        assert d_mean > d_med, "q20: the mean must move more than the median"
        assert d_sd > d_iqr, "q20: the standard deviation must move more than the IQR"
        # 83 is the maximum either way, so it is unusually large relative to a
        # body spanning at most six units -- which is what q19 keys.
        assert 83.0 > max(body) + 50, "q19: 83 must stand far away from the body of the data"


outlier_resistance()

# --- conceptual keys ---------------------------------------------------------
c.conceptual(1, "EK 1.6.A.1: a description covers shape, centre, variability and unusual features such as outliers, gaps or clusters, in context.")
c.conceptual(2, "EK 1.6.A.2: right (positive) skew means the tail toward the LARGER values is the longer one.")
c.conceptual(3, "EK 1.6.A.2: left (negative) skew means the tail toward the SMALLER values is the longer one.")
c.conceptual(4, "EK 1.6.A.2: approximate symmetry means the left half is approximately the mirror image of the right half.")
c.conceptual(5, "EK 1.6.A.3: one main peak is unimodal, two prominent peaks is bimodal.")
c.conceptual(6, "EK 1.6.A.3: approximately equal frequencies with no prominent peak is approximately uniform.")
c.conceptual(7, "EK 1.6.A.4: an outlier is a point unusually small or large relative to the rest of the data.")
c.conceptual(8, "EK 1.6.A.5: a gap is a region between two values in which no data were observed.")
c.conceptual(9, "EK 1.6.A.6: clusters are concentrations of values, usually separated by gaps.")
c.conceptual(10, f"EK 1.6.A.2: computed above, this set has mean {r_mean:.3f} above median {r_med} and a longer upper tail, so it is skewed right.")
c.conceptual(11, f"EK 1.6.A.2: computed above, mean {r_mean:.3f} exceeds median {r_med} because the long right tail pulls the mean up.")
c.conceptual(12, f"EK 1.6.A.2: computed above, this set has mean {l_mean:.3f} below median {l_med} and a longer lower tail, so it is skewed left.")
c.conceptual(13, f"EK 1.6.A.2: computed above, mean {l_mean:.3f} falls below median {l_med} because the long left tail pulls the mean down.")
c.conceptual(14, "EK 1.6.A.2: skew is named for the direction of the longer tail, not for where the bulk of the data sits, so the student's rule is backwards.")
c.conceptual(15, "EK 1.6.A.3/1.6.A.5/1.6.A.6: computed above, the frequencies peak at 12 and at 18 with zero observations at 14, 15 and 16 -- two clusters separated by a gap.")
c.conceptual(16, "EK 1.6.A.5: computed above, 14, 15 and 16 are exactly the values with zero frequency, which is the definition of a gap.")
c.conceptual(17, f"EK 1.6.A.1: computed above, the mean is {b_mean} and the median {b_med}, both inside the empty region, so no single centre describes these two clusters.")
c.conceptual(18, "EK 1.6.A.3: computed above, the six frequencies span only 6 to 8 with no prominent peak, which is approximately uniform.")
c.conceptual(19, "EK 1.6.A.4: asserted above, 83 sits more than 50 units above a body of data spanning at most six units, so it is unusually large relative to the rest.")
c.conceptual(20, "EK 1.6.A.1: simulated above over 2,000 data sets matching the stem -- the mean and standard deviation always moved more than the median and IQR.")
c.conceptual(21, "EK 1.6.A.1: spread is variability, the third required element of a description alongside shape and centre.")
c.conceptual(22, "EK 1.6.A.4/1.6.A.5/1.6.A.6: skew, symmetry, modality and uniformity describe shape, while gaps, clusters and outliers are the unusual features named separately.")
c.conceptual(23, "EK 1.6.A.1: the report gives shape (roughly symmetric), centre (5.0 mm), variability (4.7 to 5.3 mm) and unusual features (no outliers), all with units.")
c.conceptual(24, "EK 1.6.A.2: a long left tail drags the mean below the bulk of the data, so the median better represents a typical score; range and standard deviation are not centres at all.")
c.conceptual(25, "EK 1.6.A.2 and 1.6.B.1: right skew means the few very large households stretch the upper tail and pull the mean above the median, so the median is the fairer summary.")

c.finish()
