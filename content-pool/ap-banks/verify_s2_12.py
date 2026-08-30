"""Verification for AP STATISTICS 2.12, sampling distributions and the CLT.

The numeric keys are straightforward: standard error is sigma / sqrt(n), and
probabilities follow from standardizing against it. Those are computed twice --
via `norm` with the standard error supplied, and via the z-score -- and the two
must agree.

What is worth more than the arithmetic is `clt_by_simulation`. Items 5, 6, 22,
23 and 24 all rest on the distinction between three different distributions, and
that distinction is a claim about behaviour rather than a formula. So it is
SIMULATED: a strongly right-skewed population is built, and the verifier
confirms, on the same data,

  * the population is skewed (mean well above median);
  * a single large sample from it is still skewed -- which is what q5 and q23
    key, against the common belief that a big sample "becomes normal";
  * the distribution of x-bar across many samples is close to symmetric, centred
    on the population mean, with spread matching sigma / sqrt(n).

If the CLT items were ever re-keyed to the intuitive-but-wrong answer, this
fails. `bias_is_not_fixed_by_n` does the same for q20.

Run: python3 verify_s2_12.py
"""
import math
import random
import statistics as st

from scipy.stats import norm

import s_verify_util as U

import s2_12

c = U.Checker(s2_12)


def se(sigma, n):
    """Standard deviation of the sampling distribution of the sample mean."""
    assert n >= 1
    return sigma / math.sqrt(n)


def p_mean_above(x, mu, sigma, n):
    s = se(sigma, n)
    direct = float(norm.sf(x, mu, s))
    standardized = float(norm.sf((x - mu) / s))
    assert abs(direct - standardized) < 1e-12, "the two routes must agree"
    return direct


def p_mean_below(x, mu, sigma, n):
    return 1.0 - p_mean_above(x, mu, sigma, n)


# --- population mean 70, sigma 12, n = 36 ------------------------------------------
assert se(12, 36) == 2.0
c.check(8, se(12, 36))                                  # 2.00
c.check(9, 70)                                          # the centre is mu, whatever n is
c.check(10, p_mean_above(73, 70, 12, 36), tol=0.005)    # 0.067
c.check(11, p_mean_below(68, 70, 12, 36), tol=0.005)    # 0.159

# The centre does not move with n, which is the point of q9 and q17.
for n in (4, 36, 400, 10000):
    assert se(12, n) != se(12, 36) or n == 36
    # mean of the sampling distribution is mu for every n
    assert abs(float(norm.mean(70, se(12, n))) - 70) < 1e-12

# --- population mean 250, sigma 40, n = 100 ------------------------------------------
assert se(40, 100) == 4.0
c.check(12, se(40, 100))                                # 4.00
between = p_mean_below(255, 250, 40, 100) - p_mean_below(245, 250, 40, 100)
assert abs(between - 0.7887) < 0.001, f"q13: computed {between}"
c.check(13, between, tol=0.005)                         # 0.789

# --- how the spread responds to n ------------------------------------------------------
assert (se(20, 25), se(20, 100)) == (4.0, 2.0)
c.check(14, [se(20, 25), se(20, 100)])                  # 4.00 to 2.00
c.check(15, se(20, 25) / se(20, 100))                   # quadrupling n divides spread by 2

# q16: to halve the spread, n must be multiplied by 4.
factor = 4
assert abs(se(20, 25 * factor) - se(20, 25) / 2) < 1e-12, (
    "multiplying n by 4 must halve the standard error")
assert abs(se(20, 25 * 2) - se(20, 25) / 2) > 1e-6, (
    "doubling n does NOT halve it, which is the distractor")
c.check(16, factor)

# --- population mean 50, sigma 8, n = 64 -------------------------------------------------
assert se(8, 64) == 1.0
c.check(18, p_mean_above(52, 50, 8, 64), tol=0.005)     # 0.023

# --- q25: one observation against a mean of 36 ---------------------------------------------
assert (12.0, se(12, 36)) == (12.0, 2.0), "a single value carries the population's spread of 12"


def clt_by_simulation():
    """q5, q6, q22, q23, q24: three different distributions, one data set."""
    rng = random.Random(20260830)

    # A strongly right-skewed population.
    population = [rng.expovariate(1 / 40.0) for _ in range(400000)]
    pop_mean = st.mean(population)
    pop_sd = st.pstdev(population)
    assert pop_mean > st.median(population) * 1.2, (
        "the population must be clearly right-skewed for these items to mean anything")

    # q5 / q23: one large sample still looks like the population.
    one_sample = rng.sample(population, 200)
    assert st.mean(one_sample) > st.median(one_sample) * 1.15, (
        "a single sample of 200 from a skewed population is still visibly skewed")

    # q6 / q22 / q24: the sampling distribution of x-bar is near-symmetric,
    # centred at mu, with spread sigma / sqrt(n).
    n = 100
    means = [st.mean(rng.sample(population, n)) for _ in range(3000)]
    assert abs(st.mean(means) - pop_mean) < 0.05 * pop_sd / math.sqrt(n) * 10, (
        "the sampling distribution must centre on the population mean")
    assert abs(st.pstdev(means) - se(pop_sd, n)) < 0.1 * se(pop_sd, n), (
        f"spread {st.pstdev(means):.4f} should match sigma/sqrt(n) = {se(pop_sd, n):.4f}")
    # Near-symmetry: the mean and median of the sampling distribution nearly coincide,
    # whereas for the population they are far apart.
    skew_pop = (pop_mean - st.median(population)) / pop_sd
    skew_samp = (st.mean(means) - st.median(means)) / st.pstdev(means)
    assert abs(skew_samp) < abs(skew_pop) / 3, (
        f"the sampling distribution must be far more symmetric than the population "
        f"({skew_samp:.4f} against {skew_pop:.4f})")

    # And the spread ordering q24 keys: the sampling distribution is the tightest.
    assert st.pstdev(means) < st.pstdev(one_sample), (
        "the sampling distribution of x-bar has smaller spread than the sample")
    assert st.pstdev(means) < pop_sd, "and smaller than the population"


def bias_is_not_fixed_by_n():
    """q20: a larger sample narrows the sampling distribution but does not recentre it."""
    rng = random.Random(20260830)
    true_mu = 50.0
    # A biased procedure: it systematically samples values shifted by +6.
    for n in (100, 10000):
        means = [st.mean([rng.gauss(true_mu + 6, 10) for _ in range(n)]) for _ in range(200)]
        centre, spread = st.mean(means), st.pstdev(means)
        assert abs(centre - (true_mu + 6)) < 0.5, (
            f"n={n}: the centre stays at the biased value, got {centre:.3f}")
        assert abs(centre - true_mu) > 5, f"n={n}: it never approaches the true mean"
        if n == 100:
            wide = spread
        else:
            assert spread < wide / 5, "the spread must shrink substantially with n"


clt_by_simulation()
bias_is_not_fixed_by_n()

# --- conceptual keys ---------------------------------------------------------
c.conceptual(1, "Skill 4.C: a sampling distribution is the distribution of a statistic over all samples of a given size, not of the values in one sample.")
c.conceptual(2, "Skill 4.C: verified above -- the sampling distribution of x-bar centres on mu for every n, so x-bar is unbiased.")
c.conceptual(3, "Skill 4.C: verified above -- the standard deviation of x-bar is sigma over the square root of n.")
c.conceptual(4, "Skill 4.C: the CLT concerns the sampling distribution of x-bar and says nothing about the population or about the data inside one sample.")
c.conceptual(5, "Skill 4.C: simulated above -- a single sample of 200 from a right-skewed population is still visibly skewed.")
c.conceptual(6, "Skill 4.C: simulated above -- the distribution of x-bar over many samples of 100 is near-symmetric and centred on the population mean.")
c.conceptual(7, "Skill 4.C: sampling from a normal population gives an exactly normal sampling distribution at any n; the CLT is only needed otherwise.")
c.conceptual(17, "Skill 4.C: verified above -- x-bar is unbiased at every n, so a larger sample reduces spread rather than correcting the centre.")
c.conceptual(19, "Skill 4.C: simulated above -- an average of n observations varies less than a single observation, by a factor of the square root of n.")
c.conceptual(20, "Skill 4.C: simulated above -- raising n from 100 to 10,000 shrank the spread more than fivefold while the centre stayed 6 units off the truth.")
c.conceptual(21, "EK 1.2.A.4 with Skill 4.C: mu is a fixed population value, while x-bar, s and p-hat vary from sample to sample.")
c.conceptual(22, "Skill 4.C: simulated above -- the sampling distribution is far more symmetric than the skewed population it came from.")
c.conceptual(23, "Skill 4.C: simulated above -- sample size normalizes the distribution of x-bar, not the values inside a single sample.")
c.conceptual(24, "Skill 4.C: simulated above -- the sampling distribution of x-bar had smaller spread than both the sample and the population.")
c.conceptual(25, "Skill 4.C: computed above -- a single observation carries spread 12 while the mean of 36 carries spread 2, so the mean clusters far more tightly around 70.")

c.finish()
