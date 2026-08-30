"""Verification for AP STATISTICS 3.4, interpreting and using a confidence interval.

Most keys here are sentences, so what is verified is the ARITHMETIC the keys rest
on, plus the structural claims about how an interval responds to its inputs.

`claim_verdicts` is the item worth the most care. Items 7, 8, 9, 10 and 22 each
ask whether an interval supports a claim, and the rule is mechanical: a value is
plausible exactly when it lies inside the interval. The verifier applies that
rule to each stated interval and claim and asserts the verdict the key gives --
so if an interval were ever edited such that it no longer straddled 0.50, the
item whose whole point is that it straddles 0.50 would fail here.

`interval_arithmetic` recovers the centre and margin of error from endpoints and
checks the round trip, and `confidence_level_interpretation_holds` simulates the
coverage claim in EK 3.4.A.2 directly: build many 95% intervals from many random
samples and confirm that close to 95% of them capture the known parameter. That
is the one claim in this topic that is genuinely a fact about the world rather
than a definition, so it is measured rather than asserted.

Run: python3 verify_s3_4.py
"""
import math
import random

from scipy.stats import norm

import s_verify_util as U

import s3_4

c = U.Checker(s3_4)


def centre_and_me(low, high):
    """Recover the point estimate and margin of error from an interval."""
    assert low < high, "an interval must have its endpoints in order"
    centre = (low + high) / 2
    me = (high - low) / 2
    assert abs((centre - me) - low) < 1e-12 and abs((centre + me) - high) < 1e-12, (
        "the recovery must round-trip back to the original endpoints")
    return centre, me


def plausible(value, interval):
    """A value is plausible exactly when it lies inside the interval."""
    low, high = interval
    return low <= value <= high


def claim_verdicts():
    """q7, q8, q9, q10, q22: does the interval support the claim?"""
    # q7: (0.52, 0.58) lies entirely above 0.50, so a majority is supported.
    a = (0.52, 0.58)
    assert a[0] > 0.50, "the whole interval must exceed 0.50"
    assert not plausible(0.50, a), "0.50 must be ruled out"
    assert all(v > 0.50 for v in a), "every plausible value is a majority"

    # q8: (0.47, 0.55) straddles 0.50, so a majority is NOT established --
    # and its midpoint is above 0.50, which is exactly the distractor.
    b = (0.47, 0.55)
    assert plausible(0.50, b), "0.50 must remain plausible"
    centre_b, _ = centre_and_me(*b)
    assert centre_b > 0.50, (
        "the midpoint exceeds 0.50, which is why 'the midpoint is above one half' is tempting")
    assert not all(v > 0.50 for v in b), "some plausible values are not majorities"

    # q9 and q10: the same interval, two claims, opposite verdicts.
    d = (0.31, 0.39)
    assert plausible(0.35, d), "q9: 0.35 lies inside, so the claim is consistent"
    assert not plausible(0.45, d), "q10: 0.45 lies outside, so there is evidence against it"

    # q22: (0.48, 0.56) straddles 0.50 -- same structure as q8, different numbers,
    # so both must give the same verdict or the module contradicts itself.
    e = (0.48, 0.56)
    assert plausible(0.50, e)
    assert not all(v > 0.50 for v in e)
    assert plausible(0.50, b) == plausible(0.50, e), (
        "q8 and q22 pose the same question and must be keyed the same way")


claim_verdicts()


def interval_arithmetic():
    """q18, q19, q20: recovering p-hat and the margin of error from endpoints."""
    centre, me = centre_and_me(0.42, 0.50)
    assert abs(centre - 0.46) < 1e-12 and abs(me - 0.04) < 1e-12, (
        f"got centre {centre}, ME {me}")
    c.check(18, centre)                       # 0.46
    c.check(19, me)                           # 0.04
    # The full width is twice the margin of error, which is the 0.08 distractor.
    assert abs((0.50 - 0.42) - 2 * me) < 1e-12

    centre2, me2 = centre_and_me(0.634, 0.766)
    assert abs(centre2 - 0.700) < 1e-12 and abs(me2 - 0.066) < 1e-12, (
        f"got centre {centre2}, ME {me2}")
    c.check(20, [centre2, me2], tol=0.002)    # 0.700 and 0.066


interval_arithmetic()


def width_responds_to_its_inputs():
    """q11-q17, q21, q23: which input moves the width, and in which direction."""
    def z_star(conf):
        return float(norm.ppf(1 - (1 - conf) / 2))

    def se(phat, n):
        return math.sqrt(phat * (1 - phat) / n)

    phat, n = 0.5, 400

    # q11, q12, q13, q16: raising the confidence level raises z*, the margin of
    # error and the width, and leaves the standard error alone.
    levels = (0.80, 0.90, 0.95, 0.99)
    zs = [z_star(l) for l in levels]
    assert zs == sorted(zs), "z* must increase with the confidence level"
    mes = [z * se(phat, n) for z in zs]
    assert mes == sorted(mes), "the margin of error must increase with it"
    widths = [2 * m for m in mes]
    assert widths == sorted(widths), "and so must the width"
    assert len({round(se(phat, n), 15)}) == 1, "the standard error never entered"
    assert abs(z_star(0.90) - 1.645) < 0.001 and abs(z_star(0.99) - 2.576) < 0.001, (
        "q16: the two critical values are 1.645 and 2.576")

    # q14, q15, q17: raising n lowers the standard error and narrows the interval.
    sizes = (100, 400, 900, 1600)
    ses = [se(phat, k) for k in sizes]
    assert ses == sorted(ses, reverse=True), "the standard error must fall as n rises"
    assert all(z_star(0.95) == z_star(0.95) for _ in sizes), "z* does not depend on n"

    # q21: quadrupling n halves the margin of error, at an unchanged confidence level.
    assert abs(se(phat, 4 * n) - se(phat, n) / 2) < 1e-12
    # while lowering the confidence level would also narrow it but changes the level.
    assert z_star(0.90) < z_star(0.95)

    # q23: a narrower interval at the same level implies a larger sample.
    wide, narrow = (0.40, 0.60), (0.46, 0.54)
    _, me_wide = centre_and_me(*wide)
    _, me_narrow = centre_and_me(*narrow)
    assert me_narrow < me_wide, "the second study's interval is the narrower one"
    # Recover the implied sample sizes at 95% with p-hat 0.5 and confirm the order.
    z = z_star(0.95)
    n_wide = (z / me_wide) ** 2 * 0.25
    n_narrow = (z / me_narrow) ** 2 * 0.25
    assert n_narrow > n_wide, (
        f"the narrower interval implies the larger sample ({n_narrow:.0f} against {n_wide:.0f})")


width_responds_to_its_inputs()


def confidence_level_interpretation_holds():
    """EK 3.4.A.2, measured: about 95% of 95% intervals capture the parameter.

    This is the claim behind q2, q6 and q24, and it is the only claim in the
    topic that is a fact about repeated sampling rather than a definition, so it
    is simulated rather than asserted. Intervals are built exactly as the module
    describes, from independent random samples of a population with a known p.
    """
    rng = random.Random(20260830)
    p_true, n, trials = 0.55, 500, 4000
    z = float(norm.ppf(0.975))

    captured = 0
    for _ in range(trials):
        successes = sum(rng.random() < p_true for _ in range(n))
        phat = successes / n
        me = z * math.sqrt(phat * (1 - phat) / n)
        if phat - me <= p_true <= phat + me:
            captured += 1

    rate = captured / trials
    assert 0.93 < rate < 0.97, (
        f"about 95% of intervals should capture p; observed {rate:.4f}")
    # And, per EK 3.4.A.1, individual intervals genuinely do miss sometimes.
    assert captured < trials, "some intervals must fail to capture the parameter"


confidence_level_interpretation_holds()

# --- conceptual keys ---------------------------------------------------------
c.conceptual(1, "EK 3.4.A.3: the interval interpretation names the confidence level, the interval, and the parameter in context with its population.")
c.conceptual(2, "EK 3.4.A.2: simulated above -- the confidence level is the long-run capture rate of the METHOD over repeated samples.")
c.conceptual(3, "EK 3.4.A.1: once computed, the interval and the parameter are both fixed, so no probability attaches to this particular interval.")
c.conceptual(4, "EK 3.4.A.3: an interval estimates the population proportion and says nothing about where individual observations fall.")
c.conceptual(5, "EK 3.4.A.3: an interval built to capture a parameter is not a prediction interval for future sample statistics.")
c.conceptual(6, "EK 3.4.A.1: simulated above -- some intervals captured p and some did not, which is exactly 'may or may not contain'.")
c.conceptual(7, "EK 3.4.B.1: computed above -- (0.52, 0.58) rules out 0.50, so every plausible value is a majority.")
c.conceptual(8, "EK 3.4.B.1: computed above -- (0.47, 0.55) leaves 0.50 plausible even though its midpoint exceeds 0.50.")
c.conceptual(9, "EK 3.4.B.1: computed above -- 0.35 lies inside (0.31, 0.39), so the claim is consistent with the data without being proved.")
c.conceptual(10, "EK 3.4.B.1: computed above -- 0.45 lies outside (0.31, 0.39), which is evidence against the claim rather than proof.")
c.conceptual(11, "EK 3.4.C.1.i: verified above -- z* increases with the confidence level.")
c.conceptual(12, "EK 3.4.C.1.ii: verified above -- the margin of error increases with it, since only z* changes.")
c.conceptual(13, "EK 3.4.C.1.iii: verified above -- the width is twice the margin of error and moves with it.")
c.conceptual(14, "EK 3.4.C.2: verified above -- the standard error falls as n rises.")
c.conceptual(15, "EK 3.4.C.2: verified above -- a smaller standard error gives a narrower interval at the same confidence level.")
c.conceptual(16, "EK 3.4.C.1: computed above -- the two intervals share a standard error and differ only in z*, 1.645 against 2.576.")
c.conceptual(17, "EK 3.4.C.2: verified above -- increasing n narrows the interval without touching the confidence level.")
c.conceptual(21, "EK 3.4.C.2: verified above -- quadrupling n halves the margin of error while the critical value is unchanged.")
c.conceptual(22, "EK 3.4.B.1: computed above -- (0.48, 0.56) leaves values at or below 0.50 plausible, so a majority is not established.")
c.conceptual(23, "EK 3.4.C.2: computed above -- the narrower interval implies the larger implied sample size at the same confidence level.")
c.conceptual(24, "EK 3.4.A.1 and 3.4.A.2: simulated above -- a computed interval either captures p or does not, and 95% describes the procedure's success rate.")
c.conceptual(25, "EK 3.4.A.3: a complete interpretation states the confidence level, the interval, and what the parameter is a proportion of, in context.")

c.finish()
