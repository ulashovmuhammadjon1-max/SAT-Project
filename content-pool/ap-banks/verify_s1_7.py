"""Verification for AP STATISTICS 1.7, summary statistics for one quantitative variable.

The three data sets are parsed straight out of the module's own DATA_J/K/L
strings -- the same strings the student reads in the stem -- so a value edited in
a stem and not in a key fails here rather than reaching a student.

Quartiles are computed by the AP convention the CED describes (EK 1.7.A.5): Q1
is the median of the lower half of the ordered data and Q3 the median of the
upper half. All three data sets have an even n, so each half holds exactly n/2
values and the convention about whether to include the median never arises.

The outlier item is checked under BOTH rules the CED gives (EK 1.7.D.1.i and
1.7.D.1.ii). They are confirmed to agree on data set K -- 62 and nothing else --
so the question has one defensible answer no matter which rule a student applies.

Run: python3 verify_s1_7.py
"""
import statistics as st

import s_verify_util as U

import s1_7

c = U.Checker(s1_7)


def parse(text):
    return sorted(float(t) for t in text.split(","))


J, K, L = parse(s1_7.DATA_J), parse(s1_7.DATA_K), parse(s1_7.DATA_L)
assert (len(J), len(K), len(L)) == (12, 12, 8), "unexpected data set sizes"
for name, d in (("J", J), ("K", K), ("L", L)):
    assert len(d) % 2 == 0, f"data set {name} must have an even n for unambiguous quartiles"


def quartiles(data):
    """(Q1, median, Q3) by the CED's definition, for an even-length data set."""
    d = sorted(data)
    h = len(d) // 2
    return st.median(d[:h]), st.median(d), st.median(d[h:])


jq1, jmed, jq3 = quartiles(J)
kq1, kmed, kq3 = quartiles(K)

# --- data set J ---------------------------------------------------------------
c.check(1, st.mean(J))                     # 176/12 = 14.67
c.check(2, jmed)                           # (13+14)/2 = 13.5
c.check(3, jq1)                            # median of 4,7,8,10,11,13 = 9
c.check(4, jq3)                            # median of 14,16,18,21,24,30 = 19.5
c.check(5, jq3 - jq1)                      # IQR = 10.5
c.check(6, max(J) - min(J))                # range = 26
assert jmed == 13.5 and st.mean(J) != jmed, "q1: 13.50 is the median distractor, not the mean"

# --- data set L: the n - 1 divisor --------------------------------------------
c.check(7, st.stdev(L))                    # sqrt(32/7) = 2.14
c.check(8, st.variance(L))                 # 32/7 = 4.57
assert abs(st.mean(L) - 5.0) < 1e-12, "data set L should have a mean of exactly 5"
assert abs(sum((x - 5.0) ** 2 for x in L) - 32.0) < 1e-12, "squared deviations should total 32"
assert abs(st.pstdev(L) - 2.0) < 1e-12, "q7: 2.00 is the divide-by-n distractor"
assert abs(st.stdev(L) ** 2 - st.variance(L)) < 1e-12, "q8: variance is the square of s"

# --- data set K and the two outlier rules -------------------------------------
kiqr = kq3 - kq1
lower_fence, upper_fence = kq1 - 1.5 * kiqr, kq3 + 1.5 * kiqr
by_iqr = [x for x in K if x < lower_fence or x > upper_fence]

kmean, ksd = st.mean(K), st.stdev(K)
by_sd = [x for x in K if abs(x - kmean) > 2 * ksd]

assert by_iqr == [62.0], f"q12: the 1.5 x IQR rule flags {by_iqr}"
assert by_sd == [62.0], f"the two-standard-deviation rule flags {by_sd}"
assert by_iqr == by_sd, (
    "the two CED outlier rules must agree on this data set, or q12 has no single answer")
assert min(K) > lower_fence, "q12: the minimum 20 must not be a low outlier"

c.check(11, upper_fence)                   # 29.5 + 9 = 38.5
c.check(12, 62.0)                          # the sole outlier
c.check(13, kiqr)                          # 29.5 - 23.5 = 6.0
c.check(14, kmed)                          # (26+27)/2 = 26.5
assert kmean > kmed, "q14: 28.92 is the mean distractor, pulled up by the outlier"
assert max(K) - min(K) == 42, "q13: 42.0 is the range distractor, inflated by the outlier"

# --- q10: zero spread ---------------------------------------------------------
constant = [7.0] * 6
assert st.pstdev(constant) == 0.0, "q10: identical values have standard deviation zero"
c.check(10, st.pstdev(constant))

# --- q17: the quartiles as percentiles ----------------------------------------
# Q1 has about 25% of the ordered data at or below it and Q3 about 75%.
for data, q1, q3 in ((J, jq1, jq3), (K, kq1, kq3)):
    at_or_below_q1 = sum(1 for x in data if x <= q1) / len(data)
    at_or_below_q3 = sum(1 for x in data if x <= q3) / len(data)
    assert abs(at_or_below_q1 - 0.25) <= 0.10, f"Q1 should sit near the 25th percentile, got {at_or_below_q1}"
    assert abs(at_or_below_q3 - 0.75) <= 0.10, f"Q3 should sit near the 75th percentile, got {at_or_below_q3}"


def linear_transformations():
    """q19-q22: what shifting and scaling do to centre and spread.

    Computed on a real data set rather than asserted, because the whole point of
    these items is that adding a constant and multiplying by one behave
    differently -- shift moves the centre and leaves the spread alone, scale
    moves both.
    """
    base = J
    m0, s0 = st.mean(base), st.stdev(base)

    # q19: add 5 to every value.
    shifted = [x + 5 for x in base]
    assert abs(st.mean(shifted) - (m0 + 5)) < 1e-9, "q19: the mean should rise by exactly 5"
    assert abs(st.stdev(shifted) - s0) < 1e-9, "q19: the standard deviation should not change"

    # q20: multiply every value by 3.
    scaled = [3 * x for x in base]
    assert abs(st.mean(scaled) - 3 * m0) < 1e-9, "q20: the mean should triple"
    assert abs(st.stdev(scaled) - 3 * s0) < 1e-9, "q20: the standard deviation should triple"
    assert abs(st.variance(scaled) - 9 * st.variance(base)) < 1e-9, (
        "q20: the variance is multiplied by 9, which is the distractor")

    # q21: inches to centimetres is a pure scaling by 2.54.
    assert abs(68 * 2.54 - 172.72) < 1e-9, "q21: mean 68 in -> 172.72 cm"
    assert abs(4 * 2.54 - 10.16) < 1e-9, "q21: sd 4 in -> 10.16 cm"

    # q22: Fahrenheit to Celsius is a shift then a scaling. The shift affects the
    # mean only; the scaling affects both.
    assert abs((77 - 32) * 5 / 9 - 25.0) < 1e-9, "q22: mean 77 F -> 25.0 C"
    assert abs(9 * 5 / 9 - 5.0) < 1e-9, "q22: sd 9 F -> 5.0 C, with no subtraction of 32"
    f_data = [70, 74, 77, 80, 84]
    c_data = [(f - 32) * 5 / 9 for f in f_data]
    assert abs(st.mean(c_data) - (st.mean(f_data) - 32) * 5 / 9) < 1e-9
    assert abs(st.stdev(c_data) - st.stdev(f_data) * 5 / 9) < 1e-9, (
        "q22: only the multiplier reaches the standard deviation")


def resistance():
    """q23-q24: the median and IQR barely move when an extreme value is added."""
    body = [20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 33]
    extreme = body[:-1] + [200]
    b1, bmed, b3 = quartiles(body)
    e1, emed, e3 = quartiles(extreme)
    assert abs(emed - bmed) < 1e-9, "the median should be unmoved"
    assert abs((e3 - e1) - (b3 - b1)) < 1e-9, "the IQR should be unmoved"
    assert abs(st.mean(extreme) - st.mean(body)) > 10, "the mean should move a lot"
    assert st.stdev(extreme) > 4 * st.stdev(body), "the standard deviation should inflate"


linear_transformations()
resistance()

# --- conceptual keys ---------------------------------------------------------
c.conceptual(9, "EK 1.7.B.4: the standard deviation is a typical deviation of the data values from their mean, not a difference between two particular values.")
c.conceptual(15, "EK 1.7.D.1.ii: the two-standard-deviation rule is built from the mean and standard deviation, both of which an extreme value inflates, so it measures the outlier with a yardstick the outlier has bent.")
c.conceptual(16, "EK 1.7.A.6: the pth percentile is the value with p% of the ordered data less than or equal to it.")
c.conceptual(17, "EK 1.7.A.6: verified above on both data sets -- about 25% of the ordered data lie at or below Q1 and about 75% at or below Q3, so the quartiles are the 25th and 75th percentiles.")
c.conceptual(18, "EK 1.7.A.6: a percentile is a position within the distribution of scores, not the percent of questions answered correctly.")
c.conceptual(19, "EK 1.7.C.1: verified above -- adding a constant moves every measure of centre by that constant and leaves every distance between values, hence every measure of spread, unchanged.")
c.conceptual(20, "EK 1.7.C.1: verified above -- multiplying by 3 triples both the mean and the standard deviation, while the variance is multiplied by 9.")
c.conceptual(21, "EK 1.7.C.1: verified above -- a pure scaling by 2.54 multiplies both the mean and the standard deviation, giving 172.72 cm and 10.16 cm.")
c.conceptual(22, "EK 1.7.C.1: verified above -- subtracting 32 shifts only the mean, and multiplying by 5/9 scales both, giving 25.0 C and 5.0 C.")
c.conceptual(23, "EK 1.7.F.1: verified above -- the median and IQR are the resistant pair; the mean, standard deviation and range all move when an extreme value is added.")
c.conceptual(24, "EK 1.7.F.1 and 1.7.F.2: strong right skew pulls the mean and inflates the standard deviation and range, so the resistant median and IQR describe a typical price better.")
c.conceptual(25, "EK 1.7.E.1: equal means say the centres match while standard deviations of 12 against 4 say Class A is far more variable; sample sizes are not recoverable from these summaries.")

c.finish()
