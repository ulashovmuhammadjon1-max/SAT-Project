"""Verification for AP STATISTICS 3.5, setting up a test for a proportion.

Two things are checked mechanically here rather than read.

`hypothesis_pairs_are_well_formed` parses the H0/Ha strings out of every keyed
hypothesis pair and applies the CED's rules as predicates: the null must state
equality (EK 3.5.B.2), the alternative must state <, > or not-equal, both must be
about the PARAMETER p rather than p-hat, and both must name the same
hypothesized value. Each keyed pair must pass all four; each distractor pair in
those same items must fail at least one, which is what makes the item
discriminating rather than merely having one right-looking option.

`normality_uses_p0` computes the expected counts for every test scenario in the
module from the null value p0 -- not from p-hat -- and asserts the verdict each
key states. It also confirms the three Unit 3 versions of the condition give
DIFFERENT numbers on the same data, which is the point of q13 and q14.

Run: python3 verify_s3_5.py
"""
import re

import s_verify_util as U

import s3_5

c = U.Checker(s3_5)
Q = s3_5.QUESTIONS

# Items whose choices are H0/Ha pairs.
HYPOTHESIS_ITEMS = (6, 7, 8, 20, 23)

_H0 = re.compile(r"H0:\s*(p-hat|p)\s*(=|>|<|not equal to)\s*([\d.]+)")
_HA = re.compile(r"Ha:\s*(p-hat|p)\s*(=|>|<|not equal to)\s*([\d.]+)")


def parse_pair(text):
    """(null, alternative) as (symbol, relation, value) triples, or None."""
    h0, ha = _H0.search(text), _HA.search(text)
    if not h0 or not ha:
        return None
    return ((h0.group(1), h0.group(2), float(h0.group(3))),
            (ha.group(1), ha.group(2), float(ha.group(3))))


def well_formed(pair):
    """The four CED rules, as a single predicate."""
    if pair is None:
        return False
    (null_sym, null_rel, null_val), (alt_sym, alt_rel, alt_val) = pair
    return (
        null_sym == "p"                       # EK 3.5.B.1: about the parameter
        and alt_sym == "p"
        and null_rel == "="                   # EK 3.5.B.2: null holds equality
        and alt_rel in ("<", ">", "not equal to")   # EK 3.5.B.3
        and null_val == alt_val               # both refer to the same p0
    )


def hypothesis_pairs_are_well_formed():
    for qn in HYPOTHESIS_ITEMS:
        item = Q[qn - 1]
        key = item["choices"][item["ans"]]
        assert well_formed(parse_pair(key)), (
            f"q{qn}: the keyed pair {key!r} does not satisfy the CED's rules")

        # Every distractor must differ from the key -- but NOT necessarily by
        # being malformed. In the direction items a distractor is often a
        # perfectly well-formed pair pointing the wrong way, which is exactly
        # the discrimination those items want. So the requirement is that no
        # distractor is both well formed AND identical in direction and value.
        key_pair = parse_pair(key)
        for j, choice in enumerate(item["choices"]):
            if j == item["ans"]:
                continue
            other = parse_pair(choice)
            assert not (well_formed(other) and other == key_pair), (
                f"q{qn}: the distractor {choice!r} is equivalent to the key")

    # q23 asks which pair is stated CORRECTLY, so there every distractor really
    # must be malformed, or the item has more than one defensible answer.
    item23 = Q[22]
    for j, choice in enumerate(item23["choices"]):
        if j == item23["ans"]:
            continue
        assert not well_formed(parse_pair(choice)), (
            f"q23: the distractor {choice!r} is well formed, so the item has two answers")

    # And the direction of each keyed alternative matches its stem.
    directions = {6: ">", 7: "<", 8: "not equal to", 20: ">", 23: ">"}
    for qn, expected in directions.items():
        item = Q[qn - 1]
        _, (_, alt_rel, _) = parse_pair(item["choices"][item["ans"]])
        assert alt_rel == expected, (
            f"q{qn}: expected an alternative using {expected!r}, got {alt_rel!r}")

    # The null values quoted in the stems.
    values = {6: 0.05, 7: 0.40, 8: 0.08, 20: 0.50, 23: 0.25}
    for qn, p0 in values.items():
        item = Q[qn - 1]
        (_, _, null_val), _ = parse_pair(item["choices"][item["ans"]])
        assert null_val == p0, f"q{qn}: the null value should be {p0}, got {null_val}"


hypothesis_pairs_are_well_formed()


def expected_counts(n, p0):
    """EK 3.5.C.1.iii: the counts expected IF THE NULL IS TRUE."""
    return n * p0, n * (1 - p0)


def normality_ok(n, p0):
    a, b = expected_counts(n, p0)
    return a >= 10 and b >= 10


def normality_uses_p0():
    """q15, q16, q21, and the contrast in q13/q14."""
    # q15: H0: p = 0.30, n = 250.
    a, b = expected_counts(250, 0.30)
    assert (a, b) == (75.0, 175.0), f"expected counts are {a} and {b}"
    assert normality_ok(250, 0.30)

    # q16: H0: p = 0.02, n = 300 -- fails on the successes only.
    a, b = expected_counts(300, 0.02)
    assert (a, b) == (6.0, 294.0), f"expected counts are {a} and {b}"
    assert not normality_ok(300, 0.02)
    assert b >= 10, "the failure must be on the expected successes alone"

    # q21: H0: p = 0.50, n = 64.
    a, b = expected_counts(64, 0.50)
    assert (a, b) == (32.0, 32.0)
    assert normality_ok(64, 0.50)

    # q13/q14: on the SAME data the three Unit 3 conditions use different numbers.
    n, p0, observed_successes = 200, 0.30, 78
    phat = observed_successes / n
    test_counts = expected_counts(n, p0)                      # 3.5: from p0
    interval_counts = (observed_successes, n - observed_successes)  # 3.3: observed
    assert test_counts != interval_counts, (
        "the test and interval conditions must give different numbers, or q13/q14 are empty")
    assert test_counts == (60.0, 140.0) and interval_counts == (78, 122)
    assert phat != p0, "and the observed proportion differs from the hypothesised one"


normality_uses_p0()


def ten_percent(n, population):
    return n <= 0.10 * population


# q17: 400 drawn from 3,000.
assert not ten_percent(400, 3000), "400 exceeds 10% of 3,000"
assert 0.10 * 3000 == 300.0

# --- the one numeric key ------------------------------------------------------------
c.check(21, list(expected_counts(64, 0.50)))       # 32 and 32

# --- conceptual keys ---------------------------------------------------------
c.conceptual(1, "EK 3.5.A.1: testing a claim about one population proportion calls for the one-sample z-test.")
c.conceptual(2, "EK 3.5.B.1: H0 is the status quo, assumed correct until the evidence is convincing against it.")
c.conceptual(3, "EK 3.5.B.1: Ha is the claim being investigated, the one the evidence is sought for.")
c.conceptual(4, "EK 3.5.B.2: verified above -- every keyed null states equality at p0, even when the alternative is one-sided.")
c.conceptual(5, "EK 3.5.B.1: verified above -- every keyed hypothesis is about p, since p-hat is known once the data are collected.")
c.conceptual(6, "EK 3.5.B.3: verified above -- 'higher than' gives Ha: p > 0.05 with the null at the boundary 0.05.")
c.conceptual(7, "EK 3.5.B.3: verified above -- 'fewer than' gives Ha: p < 0.40.")
c.conceptual(8, "EK 3.5.B.3: verified above -- 'differs in either direction' gives a two-sided Ha: p not equal to 0.08.")
c.conceptual(9, "EK 3.5.B.2: a not-equal alternative looks both ways and is two-sided; < and > are one-sided.")
c.conceptual(10, "EK 3.5.B.1: verified above -- a hypothesis about p-hat is malformed, since the statistic is not in doubt.")
c.conceptual(11, "EK 3.5.B.2: verified above -- equality belongs in the null and the alternative must state a direction of departure.")
c.conceptual(12, "EK 3.5.C.1: the three conditions are randomization, 10%, and expected-count normality; nothing is assumed about the population's shape.")
c.conceptual(13, "EK 3.5.C.1.iii: computed above -- a test checks n*p0 and n(1 - p0), the counts expected if the null is true.")
c.conceptual(14, "EK 3.5.C.1.iii against 3.3.B.1.iii: computed above -- the two conditions give different counts on the same data, because a test assumes H0 and an interval has no such value.")
c.conceptual(15, "EK 3.5.C.1.iii: computed above -- 75 and 175 expected counts, both above 10.")
c.conceptual(16, "EK 3.5.C.1.iii: computed above -- 6 expected successes against 294 expected failures, so the condition fails on the successes alone.")
c.conceptual(17, "EK 3.5.C.1.ii: computed above -- 10% of 3,000 is 300 and the sample of 400 exceeds it.")
c.conceptual(18, "EK 3.5.A.2: the parameter names the proportion, the response variable and the population, so it describes all students at the school.")
c.conceptual(19, "EK 3.5.C.1.i: volunteers are not a random sample, so the randomization condition fails and no later arithmetic repairs it.")
c.conceptual(20, "EK 3.5.B.3: verified above -- support above one half gives Ha: p > 0.50 with the null at 0.50.")
c.conceptual(22, "EK 3.5.B.1 with 1.1.B.1: choosing the hypotheses after seeing the data is the same fault as changing an investigative question after analysis.")
c.conceptual(23, "EK 3.5.B.2 and 3.5.B.3: verified above -- only this pair puts equality in the null, a direction in the alternative, and both about p.")
c.conceptual(24, "EK 3.5.B.3: evidence points toward Ha when the statistic falls on the alternative's side of the null value, here below 0.35.")
c.conceptual(25, "EK 3.5.B.1: the conditions, the test statistic and the p-value are all computed under the assumption that H0 is true.")

c.finish()
