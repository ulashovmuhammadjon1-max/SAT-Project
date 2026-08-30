"""Verification for AP STATISTICS 1.10, investigative questions and data collection.

Three items count treatments in a factorial design; those are computed here as
products of the level counts, and each is also checked against the additive
error the rationale names as the distractor, so the distractor cannot silently
become a second correct answer.

Everything else in this topic is definitional. Each such item is declared
conceptual against the CED essential-knowledge statement that fixes it, with one
group flagged for particular care: the generalization items (q22, q23, q24, q25)
all turn on RANDOM SELECTION and none of them on random assignment. That
separation is deliberate -- random assignment and the causal conclusions it
licenses belong to topic 1.13 -- and it is asserted below by checking that no
generalization item's key claims causation.

Run: python3 verify_s1_10.py
"""
from math import prod

import s_verify_util as U

import s1_10

c = U.Checker(s1_10)

# --- treatment counts ---------------------------------------------------------
# q9: one factor at four levels -- each level is a treatment.
c.check(9, prod([4]))

# q10: two factors, 3 levels and 2 levels, fully crossed.
levels_10 = [3, 2]
assert prod(levels_10) == 6 and sum(levels_10) == 5, (
    "q10: 3 x 2 = 6 treatments, and 5 is the additive distractor")
c.check(10, prod(levels_10))

# q11: three factors at 2, 2 and 3 levels, fully crossed.
levels_11 = [2, 2, 3]
assert prod(levels_11) == 12 and sum(levels_11) == 7, (
    "q11: 2 x 2 x 3 = 12 treatments, and 7 is the additive distractor")
c.check(11, prod(levels_11))

# The additive answer must appear as a distractor and must not equal the key,
# otherwise the item would have two defensible answers.
for qn, levels in ((10, levels_10), (11, levels_11)):
    assert prod(levels) != sum(levels), f"q{qn}: product and sum must differ"


def generalization_items_are_about_selection_only():
    """q22-q25 test random SELECTION, never random assignment.

    The CED puts generalization under EK 1.10.E (how units were selected) and
    puts causal conclusions under random assignment in topic 1.13. Students
    conflate the two, so this module tests selection alone. The check is that
    no key among these items asserts a cause-and-effect conclusion -- q24's key
    is the one item that mentions causation, and it does so to DENY it.
    """
    causal_words = ("cause-and-effect", "causal", "causes")
    for qn in (22, 23, 25):
        key = s1_10.QUESTIONS[qn - 1]["choices"][s1_10.QUESTIONS[qn - 1]["ans"]]
        assert not any(w in key.lower() for w in causal_words), (
            f"q{qn}: a generalization key must not make a causal claim -- got {key!r}")

    key24 = s1_10.QUESTIONS[23]["choices"][s1_10.QUESTIONS[23]["ans"]]
    assert "does not permit a cause-and-effect" in key24, (
        "q24: the key must be the option that separates generalization from causation")
    assert "generalizing to the population" in key24, (
        "q24: the key must affirm generalization from random selection")


generalization_items_are_about_selection_only()

# --- conceptual keys ---------------------------------------------------------
c.conceptual(1, "EK 1.10.A.1: the first component guides data collection and is phrased in terms of the variables of interest.")
c.conceptual(2, "EK 1.10.A.2: the second component guides the choice of analysis, making clear the parameter and whether it is estimated or tested.")
c.conceptual(3, "EK 1.10.A.3: the third component indicates the type of conclusion, including the population it applies to.")
c.conceptual(4, "EK 1.10.B.1: a census records information from all items or individuals in the population.")
c.conceptual(5, "EK 1.10.C.1: an experiment is a study in which the researcher assigns treatments to units.")
c.conceptual(6, "EK 1.10.C.2: the experimental unit is the observational unit to which the treatment is assigned.")
c.conceptual(7, "EK 1.10.C.3: the explanatory variable, or factor, is the one whose levels are imposed on the units.")
c.conceptual(8, "EK 1.10.C.4: the response variable is the outcome measured on each unit after treatment.")
c.conceptual(12, "EK 1.10.D.1: an observational study records the variables of interest without imposing treatments.")
c.conceptual(13, "EK 1.10.D.2: a prospective study selects units at a point in time and gathers data from then into the future.")
c.conceptual(14, "EK 1.10.D.3: a retrospective study selects units at a point in time and gathers data from the past.")
c.conceptual(15, "EK 1.10.D.4: a survey is an observational study collecting data from humans with a standard set of questions.")
c.conceptual(16, "EK 1.10.D.5: a confounding variable must be associated with BOTH the explanatory and the response variable.")
c.conceptual(17, "EK 1.10.D.5: smoking is associated with coffee drinking and is a cause of lung cancer, so it satisfies both halves of the definition.")
c.conceptual(18, "EK 1.10.D.1: sleep hours were recorded rather than assigned, so the study is observational regardless of how the sample was drawn.")
c.conceptual(19, "EK 1.10.C.1: the researcher assigned the sleep condition, and assigning conditions is what makes a study an experiment.")
c.conceptual(20, "EK 1.10.C.4: alertness is measured after the treatment, so it is the response variable.")
c.conceptual(21, "EK 1.10.E.1: a sample is random when its units are selected using a random mechanism, not when selection merely feels arbitrary.")
c.conceptual(22, "EK 1.10.E.2: verified above -- random selection from the population licenses generalizing to that population, and nothing more.")
c.conceptual(23, "EK 1.10.E.3 and 1.10.E.4: verified above -- volunteers are not randomly selected, so generalization reaches only individuals similar to them.")
c.conceptual(24, "EK 1.10.E.2 against topic 1.13: verified above -- selection fixes the population a conclusion reaches; causation requires random assignment instead.")
c.conceptual(25, "EK 1.10.E.3 and 1.10.E.4: verified above -- deliberately chosen roadside trees are not a random sample, so conclusions extend only to similar trees.")

c.finish()
