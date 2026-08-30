"""Verification for AP STATISTICS 1.13, experimental design.

Every key here is a sentence, so nothing goes through ``Checker.check``. What is
mechanically verified instead is the part of this topic that is a *rule* rather
than a definition: the scope of inference.

``scope_of_inference`` encodes the CED's two independent rules --

    random SELECTION  (EK 1.10.E.2) -> the conclusion generalizes to the
                                       population sampled;
    random ASSIGNMENT (EK 1.13.A.7) -> the conclusion may be causal

-- and then checks the four items that span all four combinations against that
table. This is the pair students merge, so the check is deliberately built to
fail if any one of the four keys drifts toward the other rule: a key claiming
causation is required to come from a study with random assignment, and a key
claiming generalization is required to come from one with random selection.

Run: python3 verify_s1_13.py
"""
import s_verify_util as U

import s1_13

c = U.Checker(s1_13)


def scope_of_inference(random_selection, random_assignment):
    """(may generalize to the population, may claim cause and effect)."""
    return bool(random_selection), bool(random_assignment)


def key(qn):
    item = s1_13.QUESTIONS[qn - 1]
    return item["choices"][item["ans"]]


def scope_items_match_the_rules():
    """q19-q22 span all four combinations of selection and assignment."""
    # (question, random selection?, random assignment?)
    items = [
        (19, False, True),   # 200 volunteers, randomly assigned
        (20, True, False),   # 500 randomly selected adults, nothing assigned
        (21, True, True),    # randomly selected AND randomly assigned
        (22, False, False),  # students chose whether to attend
    ]

    # All four combinations must actually be present, or the module is not
    # testing the distinction it claims to test.
    assert {(s, a) for _, s, a in items} == {(True, True), (True, False),
                                             (False, True), (False, False)}, (
        "q19-q22 must cover all four selection/assignment combinations")

    # Each key is pinned by an explicit fragment rather than by sniffing for
    # substrings like "cause". That kind of test is the recurring own-goal in
    # this project -- the first draft of this check asked whether "cause" was in
    # the text and failed on the word "causal", which does not contain it.
    # Explicit fragments say what each key must assert about each of the two
    # rules, and the assertion below is that those fragments agree with the
    # table `scope_of_inference` returns.
    expected = {
        19: dict(causal="causes a better response", general="cannot be generalized"),
        20: dict(causal="no causal conclusion is justified", general="in the national population"),
        21: dict(causal="a causal conclusion", general="generalizes to"),
        22: dict(causal="may explain the difference", general="self-selected"),
    }

    for qn, sel, asg in items:
        may_generalize, may_claim_cause = scope_of_inference(sel, asg)
        text = key(qn).lower()
        want = expected[qn]

        assert want["causal"] in text, (
            f"q{qn}: the key must contain {want['causal']!r} -- got {key(qn)!r}")
        assert want["general"] in text, (
            f"q{qn}: the key must contain {want['general']!r} -- got {key(qn)!r}")

        # Now check those fragments say what the rules require.
        affirms_cause = want["causal"] in ("causes a better response", "a causal conclusion")
        assert affirms_cause == may_claim_cause, (
            f"q{qn}: random assignment is {asg}, so the key must "
            f"{'affirm' if may_claim_cause else 'withhold'} causation")

        affirms_general = want["general"] in ("in the national population", "generalizes to")
        assert affirms_general == may_generalize, (
            f"q{qn}: random selection is {sel}, so the key must "
            f"{'affirm' if may_generalize else 'limit'} the population")

    # q19 and q21 differ ONLY in how the units were obtained, and their keys must
    # differ correspondingly: both claim causation, only q21 generalizes.
    assert "cannot be generalized" in key(19).lower(), "q19: volunteers, so no generalization"
    assert "generalizes to" in key(21).lower(), "q21: random selection, so generalization"

    # q23 asks which change newly permits causation; the key must be the
    # random-assignment option, not the random-selection one.
    k23 = key(23).lower()
    assert "randomly assigning the treatments" in k23, (
        f"q23: the key must be the random-assignment change -- got {key(23)!r}")
    assert "random sampling" not in k23, "q23: random selection must not be the key"


def elements_of_a_good_experiment():
    """q1 is a NOT question; the four real elements must all appear as distractors."""
    item = s1_13.QUESTIONS[0]
    required = ["comparison", "random assignment", "replication", "direct control"]
    distractors = [ch.lower() for i, ch in enumerate(item["choices"]) if i != item["ans"]]
    for element in required:
        assert any(element in d for d in distractors), (
            f"q1: '{element}' is one of the four elements and must appear as a distractor")
    # And the key must be the one that is NOT an element of experimental design.
    assert "random selection" in key(1).lower(), (
        f"q1: the key must be random selection of units -- got {key(1)!r}")


def blocking_and_matched_pairs():
    """q12, q14, q15, q17: blocking, its special case, and its sampling analogue."""
    assert "grouped by similar values of an extraneous variable" in key(12), (
        "q12: blocking groups units before assignment")
    k14 = key(14).lower()
    assert "randomized block design with exactly two treatments" in k14, (
        "q14: matched pairs is a randomized block design with two treatments")
    assert "matched pairs" in key(15).lower(), "q15: twins in pairs is a matched pairs design"
    # q17: blocking and stratifying are analogous in grouping-then-randomizing,
    # and the key must NOT claim blocking permits causation (q13's distractor).
    k17 = key(17).lower()
    assert "before randomization" in k17 and "reduce variability" in k17, (
        "q17: the analogy is grouping before randomizing to reduce variability")

    # Neither q13 nor q17 may key the option that credits blocking or stratifying
    # with licensing causation. The test is on that specific claim, not on the
    # word "cause": q13's correct key legitimately contains "caused by the
    # blocking variable", and an earlier draft of this check rejected it for that.
    causal_licence = "cause-and-effect conclusion possible"
    for qn in (13, 17):
        assert causal_licence not in key(qn).lower(), (
            f"q{qn}: blocking and stratifying sharpen comparisons; they do not license causation")
        offered = [ch for ch in s1_13.QUESTIONS[qn - 1]["choices"]
                   if causal_licence in ch.lower()]
        for ch in offered:
            assert ch != key(qn), f"q{qn}: the causal-licence option must be a distractor"


scope_items_match_the_rules()
elements_of_a_good_experiment()
blocking_and_matched_pairs()

# --- conceptual keys ---------------------------------------------------------
c.conceptual(1, "EK 1.13.A.1: cross-checked above -- comparison, random assignment, replication and direct control are the four elements; random selection is a sampling matter.")
c.conceptual(2, "EK 1.13.A.2: a control group is a set of units created for comparison, possibly receiving a placebo or a different treatment.")
c.conceptual(3, "EK 1.13.A.3: the placebo effect is the difference between the average response to a placebo and to no treatment.")
c.conceptual(4, "EK 1.13.A.4: in a single-blind study the participants do not know their treatment but the interacting researchers do.")
c.conceptual(5, "EK 1.13.A.5: in a double-blind study neither the participants nor the interacting research team know the assignment.")
c.conceptual(6, "EK 1.13.A.6: an extraneous variable affects the response but is not an explanatory variable under study.")
c.conceptual(7, "EK 1.13.A.7: random assignment exists to make the treatment groups as similar as possible with respect to extraneous variation.")
c.conceptual(8, "EK 1.13.A.9: replication within an experiment means more than one experimental unit per treatment.")
c.conceptual(9, "EK 1.13.A.10: direct control keeps the settings of an extraneous variable the same from unit to unit.")
c.conceptual(10, "EK 1.13.A.8: a confounding variable is related to the explanatory variable so that their effects on the response cannot be separated.")
c.conceptual(11, "EK 1.13.B.1: in a completely randomized design treatments are assigned completely at random, and the group sizes need not be equal.")
c.conceptual(12, "EK 1.13.B.2: cross-checked above -- units are grouped into blocks by an extraneous variable first, then randomized within each block.")
c.conceptual(13, "EK 1.13.B.3: cross-checked above -- blocking separates the blocking variable's variation from the rest, giving more precise treatment comparisons.")
c.conceptual(14, "EK 1.13.B.4: cross-checked above -- matched pairs is a randomized block design with two treatments and blocks of size two.")
c.conceptual(15, "EK 1.13.B.4: cross-checked above -- twins form matched pairs and the two treatments are randomized within each pair.")
c.conceptual(16, "EK 1.13.B.2 and 1.13.B.3: variety is a known extraneous source of variation, so blocking on it removes that variation from the fertilizer comparison.")
c.conceptual(17, "EK 1.13.B.2 against 1.11.A.4: cross-checked above -- both group units before randomizing to reduce variability, one inside an experiment and one inside a sampling plan.")
c.conceptual(18, "EK 1.13.A.5: double-blinding removes the systematic influence of beliefs about the assignment, held by participants and by the staff who interact with them.")
c.conceptual(19, "EK 1.13.A.7 with 1.10.E.4: cross-checked above -- random assignment gives causation, volunteers restrict the conclusion to individuals like them.")
c.conceptual(20, "EK 1.10.E.2 without 1.13.A.7: cross-checked above -- random selection generalizes the association, but with nothing assigned no causal claim follows.")
c.conceptual(21, "EK 1.10.E.2 with 1.13.A.7: cross-checked above -- both randomizations are present, so both the generalization and the causal conclusion are available.")
c.conceptual(22, "EK 1.13.A.8: cross-checked above -- self-selection leaves motivation confounded with attendance, so no causal claim about the session is available.")
c.conceptual(23, "EK 1.13.A.7: cross-checked above -- only random assignment balances extraneous variables across groups; the other changes touch precision or generalizability.")
c.conceptual(24, "EK 1.13.A.9: five units per treatment is still replication, but unit-to-unit variation then swamps a real treatment difference far more easily than with 25.")
c.conceptual(25, "EK 1.13.A.1.i: with a single group there is nothing to compare against, so improvement cannot be separated from a placebo effect or natural recovery.")

c.finish()
