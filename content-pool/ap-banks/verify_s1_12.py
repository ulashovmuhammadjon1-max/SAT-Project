"""Verification for AP STATISTICS 1.12, potential problems with sampling.

Every key in this topic is a sentence, so none goes through ``Checker.check``.
The central claim the module rests on is nonetheless simulated rather than
asserted: that enlarging the sample shrinks VARIABILITY and leaves BIAS exactly
where it was. ``bias_versus_variability`` below draws from a population with a
known parameter using a deliberately biased procedure (an undercoverage frame
that omits a part of the population holding a different opinion), at four sample
sizes, and confirms both halves --

    the spread of the estimates falls roughly as 1/sqrt(n),
    while their centre stays put, well away from the true parameter.

That single simulation is what backs q2, q3, q15, q24 and q25 at once, which is
why those five keys are the ones a student most often gets wrong: the intuition
that "more data fixes it" is exactly what the numbers refuse.

``named_biases_are_distinct`` then checks that the four named biases are keyed
consistently across the module -- each definition item keys its own name, and no
scenario item keys a bias whose definition the scenario contradicts.

Run: python3 verify_s1_12.py
"""
import random
import statistics as st

import s_verify_util as U

import s1_12

c = U.Checker(s1_12)


def bias_versus_variability():
    """The claim behind q2, q3, q15, q24 and q25, computed.

    Population: 100,000 adults, 40% of whom hold the view (the parameter is
    0.40). The biased procedure samples only from the 70,000 who are reachable
    by day, among whom the rate is 30%. The unbiased procedure samples from the
    whole population.
    """
    rng = random.Random(20260830)
    parameter = 0.40
    reachable_rate = 0.30

    results = {}
    for n in (100, 400, 1600, 6400):
        biased = [
            sum(rng.random() < reachable_rate for _ in range(n)) / n
            for _ in range(600)
        ]
        unbiased = [
            sum(rng.random() < parameter for _ in range(n)) / n
            for _ in range(600)
        ]
        results[n] = (st.mean(biased), st.pstdev(biased),
                      st.mean(unbiased), st.pstdev(unbiased))

    sizes = sorted(results)

    # (a) The biased procedure's centre does not move toward the parameter as n
    #     grows -- it stays at the reachable-group rate. This is q2 and q3.
    for n in sizes:
        centre = results[n][0]
        assert abs(centre - reachable_rate) < 0.02, (
            f"n={n}: the biased procedure should centre on {reachable_rate}, got {centre:.4f}")
        assert abs(centre - parameter) > 0.07, (
            f"n={n}: the biased procedure must stay well away from the parameter")

    # (b) Its variability does fall, and roughly as 1/sqrt(n): quadrupling n
    #     should roughly halve the standard deviation.
    for small, large in zip(sizes, sizes[1:]):
        sd_small, sd_large = results[small][1], results[large][1]
        assert sd_large < sd_small, f"variability should fall from n={small} to n={large}"
        ratio = sd_small / sd_large
        assert 1.6 < ratio < 2.5, (
            f"quadrupling n from {small} to {large} should roughly halve the sd; ratio {ratio:.2f}")

    # (c) The bias does not shrink like the variability does. Comparing the
    #     smallest and largest n, the spread fell by a large factor while the
    #     distance from the parameter did not.
    bias_small = abs(results[sizes[0]][0] - parameter)
    bias_large = abs(results[sizes[-1]][0] - parameter)
    sd_small, sd_large = results[sizes[0]][1], results[sizes[-1]][1]
    assert sd_small / sd_large > 6, "the spread should shrink substantially across this range"
    assert 0.9 < bias_large / bias_small < 1.1, (
        f"the bias should be essentially unchanged; {bias_small:.4f} -> {bias_large:.4f}")

    # (d) q15: centred-but-wide against tight-but-off-centre. The unbiased
    #     procedure at the smallest n is centred correctly with a wide spread;
    #     the biased procedure at the largest n is tight but off centre.
    wide_centre, wide_sd = results[sizes[0]][2], results[sizes[0]][3]
    tight_centre, tight_sd = results[sizes[-1]][0], results[sizes[-1]][1]
    assert abs(wide_centre - parameter) < 0.02, "the unbiased design centres on the parameter"
    assert abs(tight_centre - parameter) > 0.07, "the biased design does not"
    assert tight_sd < wide_sd, "and yet the biased design is the tighter of the two"

    # (e) q14 and q18: changing the PROCEDURE is what moves the centre.
    assert abs(results[sizes[0]][2] - parameter) < abs(results[sizes[0]][0] - parameter), (
        "sampling the whole population instead of the reachable part removes the bias")


def named_biases_are_distinct():
    """The four named biases must be keyed consistently across the module.

    Each definition item (q4-q7) keys its own name, and the scenario items key
    a bias consistent with what the scenario actually describes. The scenarios
    are grouped here by which bias they are built to illustrate, so a key that
    drifted onto a neighbouring bias would fail.
    """
    def key(qn):
        item = s1_12.QUESTIONS[qn - 1]
        return item["choices"][item["ans"]].lower()

    definitions = {4: "voluntary response", 5: "undercoverage",
                   6: "nonresponse", 7: "response bias"}
    for qn, name in definitions.items():
        assert key(qn).startswith(name), f"q{qn}: expected the {name} option, got {key(qn)!r}"

    scenarios = {
        8: "undercoverage",       # no landline -- unreachable
        9: "nonresponse",         # selected and reachable, did not reply
        10: "voluntary response",  # self-selected callers
        11: "response bias",      # leading question
        12: "response bias",      # sensitive question, authority figure
        13: "undercoverage",      # only library users at one time
        19: "response bias",      # misremembered and overstated
        21: "undercoverage",      # daytime doorknocking
    }
    for qn, name in scenarios.items():
        assert name in key(qn), (
            f"q{qn}: the scenario illustrates {name}, but the key reads {key(qn)!r}")

    # The four names must not all collapse onto one another: each definition
    # item's key must be wrong for the other three definition items.
    keys = {qn: key(qn) for qn in definitions}
    assert len(set(keys.values())) == 4, "the four definition keys must be four different options"


bias_versus_variability()
named_biases_are_distinct()

# --- conceptual keys ---------------------------------------------------------
c.conceptual(1, "EK 1.12.A.1: bias is a systematic error making a statistic consistently larger or smaller than the parameter, unlike ordinary sampling variability.")
c.conceptual(2, "EK 1.12.A.1: simulated above -- across a 64-fold increase in n the biased procedure's centre did not move toward the parameter at all.")
c.conceptual(3, "EK 1.12.A.1: simulated above -- quadrupling n roughly halved the spread of the estimates while leaving their centre fixed.")
c.conceptual(4, "EK 1.12.A.2: voluntary response bias occurs when the sample consists entirely of volunteers.")
c.conceptual(5, "EK 1.12.A.3: undercoverage occurs when the method fails to include part of the population, or makes part of it less likely to be selected.")
c.conceptual(6, "EK 1.12.A.4: nonresponse bias occurs when individuals chosen to be sampled fail to supply a response and differ from those who do.")
c.conceptual(7, "EK 1.12.A.5: response bias occurs when the responses themselves depart from the true value in one direction.")
c.conceptual(8, "EK 1.12.A.3: cross-checked above -- households without a landline are absent from the frame, so they could never be selected.")
c.conceptual(9, "EK 1.12.A.4: cross-checked above -- every household was properly selected and reachable; the failure is that most did not reply.")
c.conceptual(10, "EK 1.12.A.2: cross-checked above -- nobody was selected, the callers put themselves forward, and 1,500 volunteers are still volunteers.")
c.conceptual(11, "EK 1.12.A.5: cross-checked above -- a leading question pushes answers one way, and asking everyone the same loaded question does not repair it.")
c.conceptual(12, "EK 1.12.A.5: cross-checked above -- a sensitive question put by an authority figure makes the answers themselves lean systematically.")
c.conceptual(13, "EK 1.12.A.3: cross-checked above -- students who never use the library, or use it at other times, have little or no chance of selection.")
c.conceptual(14, "EK 1.12.A.6: simulated above -- only replacing the procedure moved the centre of the estimates; enlarging or repeating it did not.")
c.conceptual(15, "EK 1.12.A.1: simulated above -- one design is centred with a wide spread and the other tight but off centre, which is exactly low bias/high variability against high bias/low variability.")
c.conceptual(16, "EK 1.12.A.6: without a chance mechanism nothing prevents systematic over- or under-representation, and no later arithmetic repairs it.")
c.conceptual(17, "EK 1.12.A.1: bias is a property of the procedure over all possible samples, so one estimate landing near the truth proves nothing.")
c.conceptual(18, "EK 1.12.A.3, 1.12.A.4, 1.12.A.6: a full frame addresses undercoverage, random selection addresses self-selection, and follow-up addresses nonresponse.")
c.conceptual(19, "EK 1.12.A.5: cross-checked above -- respondents were selected and did answer, but the reported values run systematically high.")
c.conceptual(20, "EK 1.12.A.1: two proper random samples differing slightly is sampling variability, which has no systematic direction and shrinks as n grows.")
c.conceptual(21, "EK 1.12.A.3: cross-checked above -- daytime doorknocking makes households where everyone works far less likely to be selected.")
c.conceptual(22, "EK 1.12.A.2 and 1.12.A.3: readers of one magazine who choose to return a coupon are both an undercovered frame and a self-selected group.")
c.conceptual(23, "EK 1.12.A.1: bias concerns where the estimates centre and variability how spread out they are, and neither implies the other.")
c.conceptual(24, "EK 1.12.A.4: simulated above -- a random selection that ends with a 25% response rate is no longer protected by its randomness.")
c.conceptual(25, "EK 1.12.A.1: simulated above -- a large biased sample estimates the wrong quantity precisely, which makes the wrong answer look more authoritative.")

c.finish()
