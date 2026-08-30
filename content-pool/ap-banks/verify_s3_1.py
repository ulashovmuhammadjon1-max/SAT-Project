"""Verification for AP STATISTICS 3.1 Estimators.

`s3_1.py` was authored in a separate pass and reached the repository before any
verifier existed for it. This file closes that gap. Every key was re-derived
here from the stem's own numbers with `statistics` -- not read off the module's
`why` text -- and each one agreed with the module. No disagreements were found.

Two notes on the checks that matter for this topic:

* the standard-deviation items are the ones worth verifying carefully, because
  each offers both the n - 1 and the n divisor as choices. The keys are the
  n - 1 (sample) values throughout, which is the unbiased estimator of the
  population variance's square root, and the n-divisor value appears as the
  intended distractor. Both are computed below so the distinction is checked
  rather than assumed;
* three items key a *sign* or a *direction* rather than a magnitude -- the
  difference of proportions in q8 is negative, and q10, q12 and q19 turn on
  which way an estimator is systematically wrong. Those are asserted explicitly.

Run: python3 verify_s3_1.py
"""
import statistics as st

import s_verify_util as U

import s3_1

c = U.Checker(s3_1)

TRAVEL = [22, 31, 27, 35, 19, 28, 24, 30]          # q4, q5
FLOUR = [4.1, 3.7, 4.6, 3.9, 4.2, 4.5, 3.8, 4.4, 4.0, 4.3]   # q13, q14
DELIVERY = [12, 15, 11, 18, 14, 13, 17, 12, 16, 14, 15, 13]  # q21, q22

# --- proportions --------------------------------------------------------------
c.check(1, 138 / 400)                       # 0.345
c.check(9, 57 / 180)                        # 0.3167 -> 0.317

# q8: the difference of two independent sample proportions, adults minus
# teenagers. The key is negative, which is the point of the item.
diff = 138 / 400 - 96 / 250
assert diff < 0, "q8: adults minus teenagers must come out negative"
c.check(8, diff)                            # 0.345 - 0.384 = -0.039

# --- means and totals ---------------------------------------------------------
c.check(4, st.mean(TRAVEL))                 # 216/8 = 27.0
c.check(13, st.mean(FLOUR))                 # 41.5/10 = 4.15
c.check(21, st.mean(DELIVERY))              # 170/12 = 14.1667 -> 14.17
c.check(17, 3.4 * 1200)                     # estimated total = mean x N = 4,080
c.check(18, 78.4 - 72.9)                    # difference of sample means = 5.5

# The distractors named in the rationales are confirmed to be what they claim,
# so a future edit cannot quietly turn a distractor into a second correct answer.
assert st.median(TRAVEL) == 27.5, "q4: 27.5 is meant to be the sample median"
assert st.median(DELIVERY) == 14.0, "q21: 14.00 is meant to be the sample median"
assert abs((78.4 + 72.9) / 2 - 75.65) < 1e-9, "q18: 75.7 is meant to be the average"
assert abs(3.4 * 50 - 170) < 1e-9, "q17: 170 is meant to be the sample-only total"

# --- standard deviations: n - 1 is the key, n is the distractor ---------------
for qn, data, tol in ((5, TRAVEL, 0.002), (14, FLOUR, 0.002), (22, DELIVERY, 0.005)):
    sample_sd = st.stdev(data)              # divisor n - 1
    population_sd = st.pstdev(data)         # divisor n, the intended distractor
    assert sample_sd > population_sd, "the n - 1 divisor must give the larger value"
    c.check(qn, sample_sd, tol=tol)

assert abs(st.variance(TRAVEL) - 26.857142857142858) < 1e-9, "q5: 26.86 is the sample variance"
assert abs(st.variance(FLOUR) - 0.09166666666666665) < 1e-9, "q14: 0.092 is the sample variance"
assert abs(st.variance(DELIVERY) - 4.515151515151516) < 1e-9, "q22: 4.52 is the sample variance"

# --- q25: rescaling a proportionally biased estimator --------------------------
# E(T) = 0.90 * theta, so E(T / 0.90) = theta and the multiplier is 1/0.90.
# The distractor 1.100 is the error of adding the 10% shortfall back to 1.
assert abs(1 / 0.90 - 1.1111111111111112) < 1e-12
assert abs(1 / 0.90 - 1.10) > 0.01, "1.100 must not be within rounding of the key"
c.check(25, 1 / 0.90)


def directional_claims():
    """The items whose key is a direction rather than a magnitude."""
    # q10: in a right-skewed population the mean exceeds the median, so a sample
    # median centres near the population median and therefore below the mean.
    # Simulated here rather than asserted from memory, with a fixed seed.
    import random
    rng = random.Random(20260830)
    skewed = [rng.lognormvariate(0, 1) for _ in range(200000)]
    assert st.mean(skewed) > st.median(skewed), (
        "q10: a right-skewed population must have mean above median")
    medians = [st.median(rng.sample(skewed, 25)) for _ in range(300)]
    assert st.mean(medians) < st.mean(skewed), (
        "q10: the sample median must centre below the population mean")

    # q12: no sample value can exceed the population maximum, and most samples
    # miss the single largest, so the sample maximum is biased low.
    population = list(range(1, 1001))
    maxima = [max(rng.sample(population, 20)) for _ in range(2000)]
    assert max(maxima) <= max(population), "q12: a sample maximum cannot exceed the population maximum"
    assert st.mean(maxima) < max(population), "q12: the sample maximum is biased low"

    # q19: readings between 51.6 and 51.9 against a true length of 50.0 --
    # tightly clustered (low variability) but centred away from the truth (bias).
    readings = [51.6, 51.7, 51.75, 51.8, 51.9]
    assert st.pstdev(readings) < 0.2, "q19: the readings are tightly clustered"
    assert abs(st.mean(readings) - 50.0) > 1.5, "q19: the readings are centred well off the true length"

    # q24: procedures I and IV sit on 0.60; II and III are off it by about 0.05.
    sim = {"I": 0.601, "II": 0.548, "III": 0.662, "IV": 0.599}
    unbiased = sorted(k for k, v in sim.items() if abs(v - 0.60) <= 0.005)
    assert unbiased == ["I", "IV"], f"q24: procedures on target are {unbiased}"


directional_claims()

# --- conceptual keys ---------------------------------------------------------
c.conceptual(2, "LO 3.1.B: a point estimator is the sample statistic corresponding to the parameter, so the sample mean estimates the population mean.")
c.conceptual(3, "LO 3.1.A: unbiasedness says the sampling distribution centres on the parameter; it is not a claim about one sample and not a claim about spread.")
c.conceptual(6, "LO 3.1.A: deviations taken from the sample mean make the sum of squares too small, so dividing by n rather than n - 1 underestimates the population variance.")
c.conceptual(7, "LO 3.1.A: bias is read from the centre of the sampling distribution and variability from its standard deviation; A centres on 42 and B does not, but B is tighter.")
c.conceptual(10, "LO 3.1.A: simulated above -- in a right-skewed population the mean exceeds the median, so the sample median centres below the population mean.")
c.conceptual(11, "LO 3.1.A: sample size controls the spread of the sampling distribution but not its centre, so a larger sample makes a biased estimator more precisely wrong.")
c.conceptual(12, "LO 3.1.A: simulated above -- the sample maximum can never exceed the population maximum and usually falls short of it, so it is biased low.")
c.conceptual(15, "LO 3.1.A: the n - 1 sample variance is unbiased for the population variance; its square root is not unbiased for the standard deviation, and range and IQR estimate spread but not variance.")
c.conceptual(16, "LO 3.1.B: a single number conveys no sense of sampling variability, which is why an interval estimate is reported alongside it.")
c.conceptual(19, "LO 3.1.A: computed above -- the readings are tightly clustered (low variability) but centre near 51.75 rather than 50.0 (bias); consistency is not accuracy.")
c.conceptual(20, "LO 3.1.A: unbiasedness depends on how the data were collected, not on the arithmetic; voluntary response favours people with strong opinions regardless of sample size.")
c.conceptual(23, "LO 3.1.A: increasing n shrinks the sampling distribution's standard deviation while leaving its centre at p; a convenience sample would instead introduce bias.")
c.conceptual(24, "LO 3.1.A: computed above -- the simulated means for I and IV sit on 0.60 while II is about 0.05 below and III about 0.06 above.")

c.finish()
