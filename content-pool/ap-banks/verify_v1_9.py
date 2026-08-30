"""Structural gate for AP U.S. Government 1.9 Federalism in Action.

ANCHORS and GROUNDING via usgov_anchor, then usgov_check with the six data
items recomputed from their own tables.

TWO ESSENTIAL-KNOWLEDGE STATEMENTS, AND THE GROUNDING MAP IS THE BALANCE SHEET
------------------------------------------------------------------------------
This topic has only EK 1.9.A.1 (the allocation of powers creates multiple
access points) and EK 1.9.A.2 (national policymaking is constrained by shared
concurrent powers). They are the same structural fact seen from opposite sides,
and the failure mode for a thirty-item module on two short sentences is that
every question becomes the same question. Reading the GROUNDING column below is
how you check it did not: the access-point items and the constraint items are
separately visible, and item 18 asks the student to tell which of the two a
scenario illustrates.

THE OVERLAP WITH v1_6, WHICH IS DELIBERATE AND BOUNDED
-------------------------------------------------------
EK 1.6.B.1 says almost the same sentence about SEPARATION OF POWERS that
EK 1.9.A.1 says about FEDERALISM. Both are in the framework and both are
examinable, so the two modules must not test the same thing twice. Every
access-point item here turns on a state or local government; the branch version
lives in v1_6. Item 10 makes the distinction itself the question.

A NOTE ON THE MULTIPLE-RESPONSE TABLE
--------------------------------------
The venue table in items 24 to 26 sums to 296 percent, and that is correct: the
stem says respondents could name more than one venue. Item 26 exists because a
student who has learned "percentages sum to one hundred" as a rule rather than
as a property of mutually exclusive categories will call a correct table an
error. The check below asserts the sum is NOT 100, so if anyone later "fixes"
the figures into a distribution, item 26 fails rather than silently becoming
unanswerable.
"""
import usgov_anchor as ua
import usgov_check as uc
import v1_9

ANCHORS = {
 1: "multiple access points for stakeholders and institutions",
 2: "more than one place to pursue the same goal",
 3: "before a state legislature, a state agency and a federal agency",
 4: "Both levels of government hold authority over the subject",
 5: "find some government receptive to it",
 6: "allows multiple access points for political participation",
 7: "without any guarantee that one will succeed",
 8: "overwhelmingly the best funded",
 9: "how many distinct governments each was pressed before",
 10: "across levels of government; the separation of powers multiplies them across branches",
 11: "sharing of concurrent powers with state governments",
 12: "capacity and cooperation of governments it does not control",
 13: "depend on state choices about implementation",
 14: "because a majority of states declined to take the actions",
 15: "in law by the limits of enumerated powers",
 16: "national constitutional standard limits how it may be exercised",
 17: "induce state action in areas where the national government's own authority",
 18: "many states decline to expand the programs it relies on",
 19: "harder for any single change of control to undo",
 20: "failed to be achieved because state governments did not act",
 21: "before any national statute was in force",
 22: "their action can precede national action",
 23: "an order is not by itself evidence that one event produced the other",
 24: "More organizations named a state legislature",
 25: "creates multiple access points for stakeholders to influence policy",
 26: "the shares are not a distribution",
 27: "More venues in which policy can be influenced, and less capacity",
 28: "applies everywhere at once",
 29: "builds a record of results and a coalition",
 30: "speed a policy's adoption somewhere even as it delays adoption everywhere",
}

GROUNDING = {
 1: "EK 1.9.A.1, verbatim: the allocation of powers 'creates multiple access points for "
    "stakeholders and institutions to influence public policy.'",
 2: "EK 1.9.A.1 applied: a defeat in Congress followed by wins in state legislatures is the "
    "structure operating.",
 3: "EK 1.9.A.1, CED skill 5.B. The claim is about the number of venues, so the evidence "
    "must show one actor using several.",
 4: "EK 1.9.A.1 read alongside EK 1.7.A.4's concurrent powers -- the strategy works because "
    "both levels hold authority over the subject.",
 5: "Federalist No. 10 (required document), 'Extend the sphere,' quoted verbatim; the CED "
    "attaches Federalist No. 10 to 1.9.A. Many interests plus many governments means a "
    "coalition beaten in one arena may prevail in another.",
 6: "Federalist No. 39 (required document), 'neither a national nor a federal Constitution,' "
    "quoted verbatim; EK 1.7.A.1 credits it with allowing multiple access points while "
    "limiting concentration, which EK 1.9.A.1 restates for policymaking.",
 7: "EK 1.9.A.1: access points are opportunities to influence, not entitlements to win.",
 8: "EK 1.9.A.1 tested by rebuttal, CED skill 5.D. Multiple venues favor whoever can afford "
    "to use several at once.",
 9: "EK 1.9.A.1 operationalized: count venues per proposal, not trust, budgets or output.",
 10: "EK 1.9.A.1 (levels) against EK 1.6.B.1 (branches). Both statements are in the "
     "framework and they operate on different axes.",
 11: "EK 1.9.A.2, verbatim: 'National policymaking is constrained by the sharing of "
     "concurrent powers with state governments.'",
 12: "EK 1.9.A.2 applied to cooperative implementation: a statute enforced by state officials "
     "is only as effective as those officials.",
 13: "EK 1.9.A.2: shared authority means state decisions shape what a national policy becomes "
     "in practice, which is why uniform statutes give uneven results.",
 14: "EK 1.9.A.2, CED skill 5.B: a constraint is an unmet objective traceable to state "
     "choices, not a long debate or a thick rulebook.",
 15: "United States v. Lopez (1995), required case, which the CED attaches to 1.9.A. CED "
     "holding: Congress exceeded its power under the Commerce Clause. A legal constraint "
     "alongside EK 1.9.A.2's practical one; a court invalidating is not a state nullifying.",
 16: "Shaw v. Reno (1993), required case, which the CED attaches to 1.9.A. CED holding: "
     "majority-minority districts may be challenged if race is the only factor. A state "
     "power bounded by a national standard.",
 17: "EK 1.7.A.5's grant instruments used to answer EK 1.9.A.2's constraint: conditions "
     "induce where command may exceed an enumerated power, and a state refusing the money "
     "is not bound.",
 18: "EK 1.9.A.2 against EK 1.9.A.1 -- the item exists to make a student sort the two, since "
     "the four distractors are all access-point scenarios.",
 19: "EK 1.9.A.1 and EK 1.9.A.2 together: a policy that had to win at more than one level "
     "rests on a broader coalition. No legal bar to repeal is claimed.",
 20: "EK 1.9.A.2 operationalized: connect unmet national objectives to state inaction.",
 21: "Data item on a labelled hypothetical; the majority threshold and the monotonic rise "
     "are recomputed below.",
 22: "EK 1.9.A.1 shown as a sequence -- state action preceding national action -- recomputed "
     "from the table's own ordering.",
 23: "Data item, CED skill 3.E: a time-ordered table shows sequence, and sequence alone does "
     "not establish causation.",
 24: "Data item on a labelled hypothetical multiple-response survey; the column maximum is "
     "recomputed below.",
 25: "EK 1.9.A.1 measured: six venues across levels and branches, each named by a "
     "substantial share of organizations.",
 26: "Data item, CED skill 3.E. Overlapping categories do not sum to one hundred, and the "
     "stem says so; the check below asserts the sum is not a distribution.",
 27: "EK 1.9.A.1 and EK 1.9.A.2 stated together, pointing in opposite directions from the "
     "same division of authority.",
 28: "EK 1.9.A.1's mirror image: access points produce uneven coverage, which is the real "
     "advantage of the national route. The fourth option contradicts EK 1.9.A.2.",
 29: "EK 1.9.A.1 used sequentially: state wins produce evidence and allies for a later "
     "national campaign.",
 30: "EK 1.9.A.1 and EK 1.9.A.2 together; reducing the topic to delay drops half of what the "
     "framework says.",
}

STATES, NATL = "States that had adopted the policy", "National statute in force"
NAMED = "Organizations naming it (%)"


def _col(t, header):
    j = t["headers"].index(header)
    return [row[j] for row in t["rows"]]


TABLE_CHECKS = {
 21: [
  ("a majority of the fifty states had adopted before any national statute was in "
   "force: 26 in Year 9 with the statute column still No",
   lambda t: uc.cell(t, "Year 9", STATES) > 25
   and _col(t, NATL)[[r[0] for r in t["rows"]].index("Year 9")] == "No"),
  ("the national statute appears only in the LAST row, so it did not precede state "
   "adoption",
   lambda t: _col(t, NATL) == ["No", "No", "No", "Yes"]),
  ("adoption rises in every interval, so 'fell between Year 5 and Year 9' is false",
   lambda t: all(a < b for a, b in zip(uc.col(t, STATES), uc.col(t, STATES)[1:]))),
  ("thirty-eight states had adopted by Year 13, well over half, so 'fewer than half' "
   "is false",
   lambda t: uc.cell(t, "Year 13", STATES) == 38),
 ],
 22: [
  ("state adoption precedes the national statute in three of the four rows, which is "
   "the sequence the key describes",
   lambda t: sum(1 for s, n in zip(uc.col(t, STATES), _col(t, NATL))
                 if s > 0 and n == "No") == 3),
  ("the table never shows a national statute without prior state adoption, so "
   "'national policy always precedes state policy' is false of these data",
   lambda t: not any(n == "Yes" and s == 0
                     for s, n in zip(uc.col(t, STATES), _col(t, NATL)))),
 ],
 23: [
  ("the table reports four distinct years, so 'covers a single year' is false",
   lambda t: len({row[0] for row in t["rows"]}) == 4),
  ("the table does carry a count of adopting states and the statute's status, so those "
   "two distractors are false on its face",
   lambda t: STATES in t["headers"] and NATL in t["headers"]),
  ("the counts run to 38 of 50, which is many states rather than one, so 'only one "
   "state' is false",
   lambda t: max(uc.col(t, STATES)) > 1),
 ],
 24: [
  ("the state legislature row is the column maximum at 71 percent, ahead of Congress",
   lambda t: uc.cell(t, "A state legislature", NAMED) == max(uc.col(t, NAMED))
   and uc.cell(t, "A state legislature", NAMED) > uc.cell(t, "Congress", NAMED)),
  ("three federal venues are each named by at least a third of organizations, so "
   "'fewer than half named any federal venue' is false",
   lambda t: max(uc.cell(t, v, NAMED)
                 for v in ("A federal agency", "Congress", "A federal court")) > 50),
  ("the six shares are all different, so the venues do not divide evenly",
   lambda t: len(set(uc.col(t, NAMED))) == 6),
 ],
 25: [
  ("six venues appear, spanning state, federal and local government and both the "
   "legislative and the judicial branch, which is what makes it an access-point table",
   lambda t: len(t["rows"]) == 6
   and any("state" in v.lower() for v in uc.labels(t))
   and any("federal" in v.lower() for v in uc.labels(t))
   and any("local" in v.lower() for v in uc.labels(t))),
  ("courts are named LESS often than legislatures, so the 'prefer courts' distractor "
   "is contradicted by the table",
   lambda t: uc.cell(t, "A federal court", NAMED)
   < uc.cell(t, "A state legislature", NAMED)),
 ],
 26: [
  ("the column sums to 296, which is NOT a distribution -- exactly what the key says, "
   "and the check that stops anyone later normalising the figures to 100",
   lambda t: sum(uc.col(t, NAMED)) == 296 and sum(uc.col(t, NAMED)) != 100),
  ("no single row exceeds 100, so no individual figure is itself impossible",
   lambda t: max(uc.col(t, NAMED)) <= 100),
  ("dividing the sum by six would give about 49, which is not 100 either, so the "
   "'divide by six' distractor does not rescue the arithmetic",
   lambda t: round(sum(uc.col(t, NAMED)) / len(t["rows"])) != 100),
 ],
}

ua.check(v1_9, ANCHORS, GROUNDING)
uc.check(v1_9, TABLE_CHECKS)

# WHAT THE REVIEW FOUND
# ---------------------
# No wrong key. The thing worth recording is what was checked rather than what
# was found: this topic has only two essential-knowledge sentences, and the risk
# in a thirty-item module on two sentences is thirty rewordings of one question.
# Reading the GROUNDING map above is the audit -- roughly ten items rest on
# EK 1.9.A.1, ten on EK 1.9.A.2, two on the required cases, six on the tables,
# and item 18 makes distinguishing the two statements the question itself.
#
# The second deliberate check was against v1_6, which owns the nearly identical
# access-point sentence at EK 1.6.B.1 about separation of powers. No item here
# uses a second BRANCH of the national government as its additional venue; every
# one uses a state or local government. Item 10 turns that boundary into an item
# rather than leaving it as an author's private convention.
