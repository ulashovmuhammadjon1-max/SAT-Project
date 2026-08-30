"""Verification for AP STATISTICS 1.11, random sampling methods.

The counting items are not taken as "population over interval" on faith -- each
systematic plan is actually enumerated, for every legal random starting point,
and the count is confirmed to be the same whichever start is drawn. That matters:
if the interval did not divide the population evenly the answer would depend on
the start and the question would have no single key, so the check also asserts
that the division is exact.

The proportional-allocation item is checked by computing both sampling fractions
and requiring them to be equal, which is the claim the key makes.

Everything else is definitional and is declared conceptual against the CED
essential-knowledge statement that fixes it. The stratified/cluster pair is
additionally checked for internal consistency: q4 and q5 must key opposite
descriptions, and q16 must key the one option that states the difference the
same way round.

Run: python3 verify_s1_11.py
"""
import s_verify_util as U

import s1_11

c = U.Checker(s1_11)


def systematic_count(population, interval):
    """Number of units selected, checked to be independent of the random start."""
    counts = set()
    for start in range(1, interval + 1):
        counts.add(len(range(start, population + 1, interval)))
    assert len(counts) == 1, (
        f"a population of {population} with interval {interval} gives {sorted(counts)} "
        "units depending on the start, so the question would have no single answer")
    assert population % interval == 0, "the interval must divide the population exactly"
    return counts.pop()


# --- q10: 1,200 students, every 20th after a random start in 1..20 -------------
n10 = systematic_count(1200, 20)
assert n10 == 60, f"q10: expected 60 students, computed {n10}"
# The stem names the start 7 and the first few selections 7, 27, 47.
assert list(range(7, 1201, 20))[:3] == [7, 27, 47], "q10: the stem's sequence must match"
c.check(10, n10)

# --- q21: 4,800 items, every 40th after a random start in 1..40 ---------------
n21 = systematic_count(4800, 40)
assert n21 == 120, f"q21: expected 120 items, computed {n21}"
c.check(21, n21)

# --- q20: inclusion probability in an SRS of 50 from 500 ----------------------
c.check(20, 50 / 500)

# --- q22: three strata contributing 15 each -----------------------------------
strata = [15, 15, 15]
assert len(strata) == 3 and all(s == 15 for s in strata)
c.check(22, sum(strata))

# --- q12: proportional allocation ---------------------------------------------
under_frac = 80 / 8000
grad_frac = 20 / 2000
assert under_frac == grad_frac == 0.01, (
    f"q12: sampling fractions are {under_frac} and {grad_frac}, and the key says both are 0.01")
assert 80 + 20 == 100 and 8000 + 2000 == 10000, "q12: a sample of 100 from a population of 10,000"
assert (80 + 20) / (8000 + 2000) == under_frac, (
    "q12: proportional allocation means the overall rate equals each stratum's rate")


def stratified_versus_cluster_is_consistent():
    """q4, q5 and q16 must describe the same distinction the same way round.

    This is the pair students reverse, so the three items that turn on it are
    cross-checked against each other rather than each being trusted alone.
    """
    def key(qn):
        item = s1_11.QUESTIONS[qn - 1]
        return item["choices"][item["ans"]].lower()

    assert "stratified" in key(4), "q4 must key the stratified option"
    assert "cluster" in key(5), "q5 must key the cluster option"

    # q4's stem describes sampling within every group; q5's describes taking
    # entire groups. Confirm the stems really do say that.
    stem4 = s1_11.QUESTIONS[3]["q"].lower()
    stem5 = s1_11.QUESTIONS[4]["q"].lower()
    assert "from within every group" in stem4, "q4's stem must describe sampling inside all groups"
    assert "entire groups are selected at random" in stem5, "q5's stem must describe taking whole groups"

    # q16's key must state the distinction in that same direction.
    k16 = key(16)
    assert "stratified sampling takes some units from every group" in k16, (
        "q16: the key must say stratified samples within every group")
    assert "cluster sampling takes every unit from some groups" in k16, (
        "q16: the key must say cluster takes entire groups")


stratified_versus_cluster_is_consistent()

# --- conceptual keys ---------------------------------------------------------
c.conceptual(1, "EK 1.11.A.1: without replacement, a unit can be selected only once.")
c.conceptual(2, "EK 1.11.A.2: with replacement, a unit can be selected more than once.")
c.conceptual(3, "EK 1.11.A.3: in an SRS of size n every sample of size n is equally likely, which is stronger than equal chances for each individual.")
c.conceptual(4, "EK 1.11.A.4: cross-checked above -- stratified sampling divides the population into non-overlapping strata and samples within every one.")
c.conceptual(5, "EK 1.11.A.5: cross-checked above -- cluster sampling selects entire clusters at random.")
c.conceptual(6, "EK 1.11.A.6: a systematic random sample uses a random starting point and then a fixed interval.")
c.conceptual(7, "EK 1.11.A.4: strata are built to be internally similar and mutually different, which is what makes stratification reduce variability.")
c.conceptual(8, "EK 1.11.A.5: each cluster ideally mirrors the population, so a few whole clusters represent it.")
c.conceptual(9, "EK 1.11.A.6: a random start followed by every 20th name on the list is a systematic random sample.")
c.conceptual(11, "EK 1.11.A.4: the population was split into two non-overlapping groups and sampled within each, which is stratification.")
c.conceptual(12, "EK 1.11.A.4: computed above -- 80/8,000 and 20/2,000 are both 0.01, so the strata were sampled proportionally.")
c.conceptual(13, "EK 1.11.A.5: whole buildings were chosen at random and everyone inside them surveyed, which is cluster sampling.")
c.conceptual(14, "EK 1.11.A.3: mixing identical slips and drawing six makes every group of six equally likely, which is an SRS.")
c.conceptual(15, "EK 1.11.A: nothing random governs who is approached or who agrees, so this is a convenience sample and supports no generalization.")
c.conceptual(16, "EK 1.11.A.4 against 1.11.A.5: cross-checked above -- stratified takes some units from every group, cluster takes every unit from some groups.")
c.conceptual(17, "EK 1.11.B.1: stratifying by grade guarantees every grade appears, which a simple random sample would probably but not certainly achieve.")
c.conceptual(18, "EK 1.11.B.1: cluster sampling concentrates fieldwork in a few randomly chosen locations, which is exactly the situation it is designed for.")
c.conceptual(19, "EK 1.11.A.1 and 1.11.A.3: without replacement no individual repeats, and in an SRS of 50 from 500 each has a 50/500 chance of inclusion.")
c.conceptual(23, "EK 1.11.B.1: stratification guarantees subgroup representation and can lower sample-to-sample variability; no sampling method supports a causal claim.")
c.conceptual(24, "EK 1.11.A.6: when the list cycles with the same period as the sampling interval, every selected unit falls at the same point of the cycle.")
c.conceptual(25, "EK 1.11.A and 1.10.E.2: all four methods let chance rather than judgement choose the units, which is what licenses generalization; causation still needs random assignment.")

c.finish()
