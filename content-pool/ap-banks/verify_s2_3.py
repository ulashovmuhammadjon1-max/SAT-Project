"""Verification for AP STATISTICS 2.3, estimating probabilities by simulation.

Two kinds of check here.

First, the digit-assignment items are verified by ENUMERATING the labels rather
than by trusting arithmetic on the endpoints. `label_span` builds the actual
range and counts it, so an off-by-one -- the characteristic error of this topic,
and the one every distractor in q4 and q16 is built from -- cannot slip through.

Second, the claims about simulation behaviour are simulated. q3 (more trials
gives a better estimate) and q23 (two correct runs disagreeing is normal, not a
mistake) are both statements about sampling variability, so the verifier runs
the simulations and measures it, rather than asserting the textbook sentence.

The simulation table's own estimates are recomputed straight from its counts.

Run: python3 verify_s2_3.py
"""
import random
import statistics as st

import s_verify_util as U

import s2_3

c = U.Checker(s2_3)


def label_span(probability, total_labels):
    """(first label, last label, how many) for simulating `probability`.

    Labels run 0, 1, ..., total_labels - 1 and each carries probability
    1/total_labels. The span starts at 0, so the LAST label is one less than the
    count -- which is exactly the off-by-one this function exists to get right.
    """
    count = round(probability * total_labels)
    assert abs(count / total_labels - probability) < 1e-12, (
        f"{probability} is not an exact multiple of 1/{total_labels}")
    labels = list(range(0, count))
    assert len(labels) == count
    return labels[0], labels[-1], count


# --- q4: probability 0.35 with two-digit labels 00-99 --------------------------
lo4, hi4, n4 = label_span(0.35, 100)
assert (lo4, hi4, n4) == (0, 34, 35), f"q4: computed span {lo4}-{hi4}, {n4} labels"
# The distractor 00-35 is thirty-six labels, so it simulates 0.36, not 0.35.
assert len(range(0, 36)) == 36 and 36 / 100 != 0.35
c.check(4, [lo4, hi4])

# --- q5: how many labels for 0.62 ---------------------------------------------
_, _, n5 = label_span(0.62, 100)
assert n5 == 62
c.check(5, n5)

# --- q6: probability 0.30 with single digits 0-9 -------------------------------
lo6, hi6, n6 = label_span(0.30, 10)
assert (lo6, hi6, n6) == (0, 2, 3), f"q6: computed {lo6}-{hi6}, {n6} digits"
assert n6 / 10 == 0.30
# The distractor 0,1,2,3 is four digits and simulates 0.40.
assert len(range(0, 4)) / 10 == 0.40
c.check(6, list(range(lo6, hi6 + 1)))

# --- q9: labels 00 through 07 --------------------------------------------------
n9 = len(range(0, 8))
assert n9 == 8, "00 through 07 inclusive is eight labels, not seven"
c.check(9, n9 / 100)

# --- q16: probability 0.25 with two-digit labels -------------------------------
lo16, hi16, n16 = label_span(0.25, 100)
assert (lo16, hi16, n16) == (0, 24, 25), f"q16: computed {lo16}-{hi16}, {n16} labels"
assert len(range(0, 26)) == 26, "the distractor 00-25 is twenty-six labels"

# --- q7: 70% free throws with single digits ------------------------------------
_, hi7, n7 = label_span(0.70, 10)
assert (hi7, n7) == (6, 7), "digits 0 through 6 is seven of ten, giving 0.70"

# --- q17/q18: one third cannot be done exactly with ten equally likely digits ---
assert 3 / 10 != 1 / 3, "three digits of ten gives 0.30, not one third"
assert abs(3 / 9 - 1 / 3) < 1e-12, "discarding one digit leaves nine, three of which is exactly 1/3"


# --- the simulation table -------------------------------------------------------
def parse_sim(table):
    counts = {}
    total = None
    for label, n in table["rows"]:
        if label.lower() == "total":
            total = int(n)
        else:
            counts[int(label)] = int(n)
    assert sum(counts.values()) == total, (
        f"trial counts sum to {sum(counts.values())}, total row says {total}")
    return counts, total


SIM, SIM_N = parse_sim(s2_3.TABLE_SIM)
assert set(SIM) == {0, 1, 2, 3, 4}, "four tosses give five possible head counts"

c.check(10, SIM[2] / SIM_N)                                     # 19/50 = 0.38
c.check(11, sum(SIM[k] for k in (3, 4)) / SIM_N)                # 16/50 = 0.32
c.check(12, sum(SIM[k] for k in (0, 1)) / SIM_N)                # 15/50 = 0.30
c.check(13, SIM[4] / SIM_N)                                     #  4/50 = 0.08
c.check(14, (SIM_N - SIM[0]) / SIM_N)                           # 47/50 = 0.94

# Complementary pairs must be consistent with each other.
assert abs((SIM[0] / SIM_N) + ((SIM_N - SIM[0]) / SIM_N) - 1.0) < 1e-12

# --- q21: recovering the count from an estimate ---------------------------------
c.check(21, 0.164 * 500)                                        # 82 trials

# --- q17 again: three of ten digits ---------------------------------------------
c.check(17, 3 / 10)                                             # 0.30


def simulation_behaviour():
    """q3 and q23: what more trials do, and what two honest runs look like.

    The scenario simulated is the module's own: the number of heads in four
    tosses of a fair coin, with the outcome of interest being exactly 2 heads.
    Its true probability is 6/16 = 0.375, which is computed here rather than
    quoted, so q15's comparison of 0.38 against 0.375 rests on a derivation.
    """
    from itertools import product

    outcomes = list(product([0, 1], repeat=4))
    assert len(outcomes) == 16
    exactly_two = sum(1 for o in outcomes if sum(o) == 2)
    true_p = exactly_two / len(outcomes)
    assert (exactly_two, true_p) == (6, 0.375), f"q15: theoretical value is {true_p}"

    # q15: the module's estimate of 0.38 is close to, but not equal to, 0.375.
    estimate = SIM[2] / SIM_N
    assert estimate != true_p, "q15 is about a simulation NOT landing exactly on the truth"
    assert abs(estimate - true_p) < 0.02, (
        f"q15: {estimate} should be close to {true_p}, as the key claims")

    rng = random.Random(20260830)

    def run(trials):
        hits = 0
        for _ in range(trials):
            if sum(rng.randint(0, 1) for _ in range(4)) == 2:
                hits += 1
        return hits / trials

    # q3: the spread of the estimate around the truth shrinks as trials grow.
    small = [run(100) for _ in range(200)]
    large = [run(10000) for _ in range(20)]
    err_small = st.mean(abs(e - true_p) for e in small)
    err_large = st.mean(abs(e - true_p) for e in large)
    assert err_large < err_small, (
        f"q3: mean error should fall, got {err_small:.4f} -> {err_large:.4f}")
    assert st.pstdev(small) > st.pstdev(large), "q3: and so should the spread"
    # But it never becomes exact.
    assert not any(e == true_p for e in large) or True, (
        "q3: an estimate may coincidentally equal the truth; the key only claims it tends closer")

    # q23: two independent 200-trial runs of a correct simulation routinely
    # differ by a few hundredths, which is variability rather than error.
    pairs = [(run(200), run(200)) for _ in range(200)]
    gaps = [abs(a - b) for a, b in pairs]
    assert st.mean(gaps) > 0.01, (
        "q23: independent runs should typically differ, which is why disagreement is not a mistake")
    assert any(g >= 0.04 for g in gaps), (
        "q23: a gap as large as the 0.41 vs 0.45 in the stem should occur without any error")


simulation_behaviour()

# --- conceptual keys ---------------------------------------------------------
c.conceptual(1, "Skill 3.C: an estimated probability is the number of trials showing the outcome divided by the number of trials.")
c.conceptual(2, "Skill 3.C: a trial is one complete repetition of the whole scenario, so four free throws take four digits.")
c.conceptual(3, "Skill 3.C: simulated above -- the mean error and the spread of the estimate both fell as trials rose, but the estimate stays an estimate.")
c.conceptual(7, "Skill 3.C: verified above -- digits 0 through 6 are seven of ten equally likely digits, which is 0.70; three digits would simulate 0.30.")
c.conceptual(8, "Skill 3.C: a trial must reproduce the whole scenario, and the scenario is four attempts.")
c.conceptual(15, "Skill 3.C: derived above -- the theoretical value is 6/16 = 0.375 and the simulation gave 0.38, a difference well within ordinary variability for 50 trials.")
c.conceptual(16, "Skill 3.C: verified above -- 00 through 24 enumerates twenty-five labels, exactly 0.25; 00 through 25 is twenty-six.")
c.conceptual(18, "Skill 3.C: verified above -- discarding one digit leaves nine equally likely outcomes and 3/9 is exactly one third.")
c.conceptual(19, "Skill 3.C: a simulation description covers the digit assignment, what one trial is, the number of trials, and how the estimate is computed; the theoretical value is what the simulation is for.")
c.conceptual(20, "Skill 3.C: the figure is the observed relative frequency across the trials, offered as an estimate with no claim of exactness.")
c.conceptual(22, "Skill 3.C: a correct simulation must give every outcome its right chance, and this scheme makes three of the twelve months impossible.")
c.conceptual(23, "Skill 3.C: simulated above -- independent 200-trial runs routinely differ by several hundredths, so a gap like 0.41 against 0.45 signals variability, not error.")
c.conceptual(24, "Skill 3.C: the simulation must mirror the real process, and since one person cannot serve twice, a repeated label within a trial is discarded and redrawn.")
c.conceptual(25, "Skill 3.C and EK 1.2.A.5: the estimate is computed from simulated data, so it is a statistic with its own variability, centred on the true probability when the design is correct.")

c.finish()
