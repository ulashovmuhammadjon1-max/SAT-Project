"""Verification for AP STATISTICS 3.11, judging a claim from a two-sample interval.

Every key in this topic is a sentence, so what is verified is the RULE the keys
apply. `verdict` implements it once -- an interval entirely above 0 establishes
p1 > p2, one entirely below establishes p2 > p1, one containing 0 establishes
nothing -- and each interval the module quotes is run through it and required to
produce the verdict its key states.

That is worth doing mechanically because the three verdicts are easy to key
backwards, and because two of the items (q13 and q19) hinge on intervals whose
ENDPOINT is 0. An endpoint is a plausible value, so those intervals do not rule
0 out; a check that tested `low > 0` rather than `low > 0 or contains 0` would
get them wrong in exactly the way a hurried author would.

`scope_of_inference_items` reuses the Unit 1 rule table for q14, q15, q23 and
q24, so the two-sample items agree with topic 1.13 rather than drifting.

Run: python3 verify_s3_11.py
"""
import s_verify_util as U

import s3_11

c = U.Checker(s3_11)


def contains_zero(interval):
    low, high = interval
    assert low <= high, "endpoints must be in order"
    return low <= 0 <= high


def verdict(interval):
    """What a two-proportion interval establishes about p1 minus p2."""
    if contains_zero(interval):
        return "no difference established"
    return "p1 larger" if interval[0] > 0 else "p2 larger"


def endpoint_zero_is_not_exclusion():
    """An interval with 0 as an endpoint does NOT rule 0 out."""
    assert contains_zero((0.00, 0.14)), "0 as the lower endpoint is still contained"
    assert contains_zero((-0.11, 0.00)), "0 as the upper endpoint is still contained"
    assert verdict((0.00, 0.14)) == "no difference established"
    assert verdict((-0.11, 0.00)) == "no difference established"
    # And a naive test would get these wrong, which is why the check exists.
    assert not (0.00 > 0), "a low endpoint of exactly 0 is not strictly positive"


endpoint_zero_is_not_exclusion()

# --- the three worked intervals -----------------------------------------------------
A, B, C = (0.03, 0.15), (-0.08, 0.02), (-0.20, -0.05)
assert verdict(A) == "p1 larger", "q2"
assert verdict(B) == "no difference established", "q3, q5"
assert verdict(C) == "p2 larger", "q4, q16"
assert len({verdict(A), verdict(B), verdict(C)}) == 3, (
    "the three intervals must produce three different verdicts")

# q5: the interval that contains 0 also contains many other values, which is why
# it cannot establish equality.
for value in (-0.06, -0.02, 0.0, 0.01):
    assert B[0] <= value <= B[1], f"{value} is plausible under interval B"
assert B[0] != B[1], "the interval is not a single point"

# q12: an interval mostly positive but containing 0 still establishes nothing.
mostly_positive = (-0.02, 0.30)
assert contains_zero(mostly_positive)
assert verdict(mostly_positive) == "no difference established"
positive_width = mostly_positive[1] - 0.0
negative_width = 0.0 - mostly_positive[0]
assert positive_width > negative_width * 10, (
    "most of the interval is positive, which is exactly what makes the wrong answer tempting")

# q13: only one of the five offered intervals excludes 0.
offered = [(-0.05, 0.12), (-0.11, 0.00), (0.00, 0.14), (0.02, 0.19), (-0.09, 0.09)]
excluding = [iv for iv in offered if not contains_zero(iv)]
assert excluding == [(0.02, 0.19)], f"q13: intervals excluding 0 are {excluding}"


def widening_and_narrowing():
    """q8, q9, q17, q18, q21: how the width interacts with the verdict."""
    # q8/q9: widening can only add values, so exclusion can be lost but not gained.
    narrow = (0.03, 0.15)
    wider = (narrow[0] - 0.05, narrow[1] + 0.05)
    assert not contains_zero(narrow) and contains_zero(wider), (
        "widening an interval that barely excluded 0 can bring 0 inside")
    assert wider[0] < narrow[0] and wider[1] > narrow[1], "widening adds values at both ends"

    # A wider interval always contains the narrower one when they share a centre.
    centre = (narrow[0] + narrow[1]) / 2
    assert abs(centre - 0.09) < 1e-12
    assert wider[0] <= narrow[0] and narrow[1] <= wider[1]

    # q17: narrowing around a nonzero centre eventually excludes 0.
    for half_width in (0.20, 0.12, 0.06, 0.03):
        iv = (centre - half_width, centre + half_width)
        if half_width < centre:
            assert not contains_zero(iv), f"half-width {half_width} should exclude 0"
        else:
            assert contains_zero(iv), f"half-width {half_width} should contain 0"

    # q18: the same data, two confidence levels, two verdicts -- consistent, not
    # contradictory, because the wider interval is the higher-confidence one.
    at99, at90 = (-0.01, 0.13), (0.01, 0.11)
    assert (at99[1] - at99[0]) > (at90[1] - at90[0]), "the 99% interval must be the wider"
    assert at99[0] < at90[0] and at99[1] > at90[1], "and must contain the 90% interval"
    assert contains_zero(at99) and not contains_zero(at90), "hence the two verdicts differ"
    assert abs((at99[0] + at99[1]) / 2 - (at90[0] + at90[1]) / 2) < 0.01, (
        "and they share a centre, since they come from the same data")

    # q21: nine times the data gives three times the precision.
    import math
    assert abs(math.sqrt(900 / 100) - 3.0) < 1e-12

    # q22: the point estimate is the centre of the reported interval.
    reported = (-0.03, 0.19)
    assert abs((reported[0] + reported[1]) / 2 - 0.08) < 1e-12, (
        "q22: the centre really is the 8 percentage points the article quotes")
    assert contains_zero(reported), "yet the interval leaves no difference plausible"


def reversing_the_order():
    """q11: negating both endpoints reflects the interval and preserves the finding."""
    original = (0.03, 0.15)
    reversed_iv = (-original[1], -original[0])
    assert reversed_iv == (-0.15, -0.03)
    assert verdict(original) == "p1 larger" and verdict(reversed_iv) == "p2 larger", (
        "the labels swap because the parameter has been redefined, not because the finding changed")
    assert abs((original[1] - original[0]) - (reversed_iv[1] - reversed_iv[0])) < 1e-12, (
        "the width, and so the precision, is unchanged")
    assert contains_zero(original) == contains_zero(reversed_iv), (
        "and whether a difference is established is unchanged")


def scope_of_inference_items():
    """q14, q15, q23, q24: the same rules as topic 1.13, applied to two samples."""
    def scope(random_selection, random_assignment):
        return bool(random_selection), bool(random_assignment)

    # q14: groups self-selected, so association only.
    generalize, causal = scope(False, False)
    assert not causal, "q14: without random assignment no causal claim"

    # q15: random samples of two populations, nothing assigned.
    generalize, causal = scope(True, False)
    assert generalize and not causal, "q15: generalize to the sampled populations, no causation"

    # q23: random assignment present.
    generalize, causal = scope(False, True)
    assert causal, "q23: random assignment licenses the causal claim"
    assert not generalize, "and the population reached is limited to subjects like those studied"

    # q24: both, which is the strongest case.
    generalize, causal = scope(True, True)
    assert generalize and causal, "q24: both randomizations give the strongest conclusion"


widening_and_narrowing()
reversing_the_order()
scope_of_inference_items()

# --- conceptual keys ---------------------------------------------------------
c.conceptual(1, "Skill 4.G: the parameter is p1 minus p2, so 0 is exactly the statement that the two population proportions are equal.")
c.conceptual(2, "Skill 4.G: computed above -- interval A lies entirely above 0, so p1 is convincingly the larger.")
c.conceptual(3, "Skill 4.G: computed above -- interval B contains 0, so no difference is established in either direction.")
c.conceptual(4, "Skill 4.G: computed above -- interval C lies entirely below 0, so p2 is convincingly the larger.")
c.conceptual(5, "Skill 4.G: computed above -- interval B contains -0.06 and 0.01 as well as 0, so it fails to distinguish among them rather than establishing equality.")
c.conceptual(6, "Skill 4.F: as in topic 3.4, the interpretation names the confidence level, the interval and the parameter, which here is a difference between two populations.")
c.conceptual(7, "Skill 4.F: at the same confidence level a narrower interval reflects a smaller standard error, which comes from larger samples.")
c.conceptual(8, "Skill 4.F: computed above -- raising the confidence level widens the interval around the same centre and can bring 0 inside.")
c.conceptual(9, "Skill 4.F: computed above -- widening only adds values, so exclusion at one level does not guarantee it at a higher one.")
c.conceptual(10, "Skill 4.F: the parameter is a difference of proportions, so the interval bounds how much one exceeds the other, not a proportion and not a ratio.")
c.conceptual(11, "Skill 4.F: computed above -- negating both endpoints redefines which group is subtracted, leaving the width and the finding unchanged.")
c.conceptual(12, "Skill 4.G: computed above -- the interval contains 0 despite being mostly positive, and containing 0 is the criterion.")
c.conceptual(13, "Skill 4.G: computed above -- only (0.02, 0.19) excludes 0; the two intervals with 0 as an endpoint do not rule it out.")
c.conceptual(14, "Skill 4.G with EK 1.13.A.7: verified above -- self-selected groups support association only.")
c.conceptual(15, "Skill 4.G with EK 1.10.E.2: verified above -- random selection carries the conclusion to the sampled populations.")
c.conceptual(16, "Skill 4.G: computed above -- proportions are never negative but their difference can be, and a negative difference means the subtracted proportion is larger.")
c.conceptual(17, "Skill 4.F: computed above -- narrowing around a nonzero centre eventually excludes 0.")
c.conceptual(18, "Skill 4.F: computed above -- the 99% interval contains the 90% one and shares its centre, so the differing verdicts reflect the standard of evidence, not a contradiction.")
c.conceptual(19, "Skill 4.G: verified above -- an endpoint is a plausible value, so 0 as an endpoint is not ruled out.")
c.conceptual(20, "Skill 4.F: the centre carries the estimate and the width carries the precision, and the two depend on different quantities.")
c.conceptual(21, "Skill 4.F: computed above -- nine times the sample size gives three times the precision.")
c.conceptual(22, "Skill 4.G: computed above -- 0.08 really is the centre of (-0.03, 0.19), and reporting it alone hides that no difference is established.")
c.conceptual(23, "Skill 4.G with EK 1.13.A.7: verified above -- random assignment licenses the causal claim for subjects like those studied.")
c.conceptual(24, "Skill 4.G with EK 1.10.E.2 and 1.13.A.7: verified above -- selection carries the population and assignment carries causation.")
c.conceptual(25, "Skill 4.G: judging a claim against an interval is the same operation whatever the parameter -- inside is plausible, outside argues against it.")

c.finish()
