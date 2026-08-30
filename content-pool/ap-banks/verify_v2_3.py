"""Structural gate for AP U.S. Government 2.3 Congressional Behavior.

ANCHORS, GROUNDING and the notation check via usgov_anchor, then usgov_check
with the six data items recomputed from their own tables.

THE TOPIC WHOSE TITLE HIDES ITS CONTENTS
-----------------------------------------
"Congressional Behavior" mentions neither districting nor representational
roles, and both live here: EK 2.3.A.2 is where Baker v. Carr and Shaw v. Reno
attach, and EK 2.3.A.4 is where trustee / delegate / politico lives
(AP_US_GOV_CED.md note 12). The GROUNDING map below is how that coverage is
audited without re-reading thirty items: EK 2.3.A.1 for the partisanship chain,
EK 2.3.A.2 plus the two required cases for districting, EK 2.3.A.3 for divided
government, EK 2.3.A.4 for the three roles.

FOUR DEFINITIONS THAT MUST BE EXACT, AND THE CHECK THAT KEEPS THEM SO
----------------------------------------------------------------------
EK 2.3.A.1 and EK 2.3.A.3 supply four parenthetical definitions -- partisan
voting, polarization, gridlock, divided government -- and every one of them is
a phrase the exam can quote. Three of them sit in the same CED sentence, which
is exactly the condition under which a bank starts using them as synonyms.
_definitions below asserts that each of the four keyed choices still contains
the framework's own distinguishing words, so an edit that softened "no
congressional action" into "difficulty passing legislation" would fail here
rather than quietly teach a looser definition than the exam uses.

THE BOUNDARY ITEM
------------------
EK 2.3.A.3's threshold for divided government is AT LEAST ONE chamber. Item 13
puts a president against an opposing Senate with a friendly House, which is
divided government on the framework's definition and unified government on the
stricter definition students usually carry. That item is the reason this module
exists in the shape it does; if it were removed, nothing else here would catch
the error.
"""
import usgov_anchor as ua
import usgov_check as uc
import v2_3

ANCHORS = {
 1: "voting based on their political party affiliation",
 2: "political attitudes moving toward ideological extremes",
 3: "no congressional action on legislation can be taken due to a lack of consensus",
 4: "distinct and causally ordered",
 5: "Polarized attitudes produce partisan voting",
 6: "failed to be enacted because no consensus could be assembled",
 7: "partially addressed by Supreme Court cases",
 8: "made districting claims justiciable",
 9: "when race was the sole factor",
 10: "Baker held that districting claims may be heard in federal court",
 11: "Baker v. Carr (1962), which held that redistricting did not raise political questions",
 12: "at least one chamber of Congress",
 13: "divided government, because the opposing party controls at least one chamber",
 14: "presidential initiatives and appointments, especially those of a lame duck",
 15: "opponents can hope for a nominee more to their liking",
 16: "a trustee",
 17: "a delegate",
 18: "the politico role, which combines the trustee and delegate conceptions",
 19: "The trustee role, since she rests the vote on her own knowledge",
 20: "Accountability to constituents in each chamber is affected",
 21: "rose across the three periods while the number of major bills enacted fell",
 22: "can lead to gridlock, a situation in which action cannot be taken",
 23: "may both be responding to something else",
 24: "safe districts most often name their own judgement",
 25: "The middle row describes the delegate and the first row describes the trustee",
 26: "sharper electoral accountability",
 27: "an institution it can use against the other",
 28: "conditions no single member controls",
 29: "rejections of presidential nominees occur more often in periods of divided",
 30: "a third conception, the politico",
}

GROUNDING = {
 1: "EK 2.3.A.1's own parenthesis: partisan voting is 'when members of Congress vote based "
    "on their political party affiliation.'",
 2: "EK 2.3.A.1's own parenthesis: polarization is 'when political attitudes move toward "
    "ideological extremes.' A distribution of attitudes, not a behavior.",
 3: "EK 2.3.A.1's own parenthesis: gridlock is 'a situation in which no congressional action "
    "on legislation can be taken due to a lack of consensus.'",
 4: "EK 2.3.A.1's causal ordering: partisan voting and polarization 'can lead to' gridlock.",
 5: "EK 2.3.A.1 applied to a scenario, with ideological division upstream and gridlock down.",
 6: "EK 2.3.A.1: gridlock is identified by the ABSENCE OF ACTION, which is what distinguishes "
    "it from the other two terms in the same sentence.",
 7: "EK 2.3.A.2, verbatim: these problems 'have been partially addressed by Supreme Court "
    "cases that opened the door for equal protection challenges to redistricting.' The word "
    "'partially' is the framework's own.",
 8: "Baker v. Carr (1962), required case, which the CED attaches to 2.3.A. CED holding: "
    "'Redistricting did not raise political questions, allowing federal courts to hear cases "
    "challenging redistricting plans.' A rule about justiciability.",
 9: "Shaw v. Reno (1993), required case, which the CED attaches to 2.3.A. CED holding: such "
    "districts 'may be constitutionally challenged by voters IF RACE IS THE ONLY FACTOR used "
    "in creating the district' -- narrower than a ban on considering race.",
 10: "Baker v. Carr against Shaw v. Reno: threshold justiciability against the substantive "
     "standard on the merits.",
 11: "Baker v. Carr (1962), required case, as a SCOTUS comparison; the non-required case's "
     "facts are printed in the stem per CED p. 29.",
 12: "EK 2.3.A.3's own parenthesis: divided government is 'when one party controls the "
     "presidency and the other party controls AT LEAST ONE of the chambers of Congress.'",
 13: "EK 2.3.A.3's threshold tested at its boundary -- one chamber suffices, which is the "
     "definition students most often carry in a stricter form.",
 14: "EK 2.3.A.3: partisanship 'can result in members of Congress voting against presidential "
     "initiatives and appointments, especially those of a lame duck president.'",
 15: "EK 2.3.A.3's lame duck clause, with the mechanism being the expected change in who will "
     "be nominating. U.S. Constitution Art. II Sec. 2 leaves the nomination power intact.",
 16: "EK 2.3.A.4.i: a trustee 'will vote on issues based on their own knowledge and "
     "judgement.'",
 17: "EK 2.3.A.4.ii: a delegate 'sees themselves as an agent of those who elected them and "
     "will vote on issues based on the interests of their constituents.'",
 18: "EK 2.3.A.4.iii: 'A politico uses a combination of these role conceptions.'",
 19: "EK 2.3.A.4.i applied: the explanation given rests the vote on the member's own study "
     "and judgement, which is the trustee conception.",
 20: "EK 2.3.A.4's opening sentence: 'Accountability to constituents in each chamber is "
     "affected by how representatives perceive their roles.'",
 21: "Data item on a labelled hypothetical; both series' directions are recomputed below.",
 22: "EK 2.3.A.1's chain shown as data: party-line voting up, enactments down.",
 23: "Data item, CED skill 3.E: two series moving oppositely support causation in either "
     "direction and a common cause equally well.",
 24: "Data item on a labelled hypothetical; both columns' leading rows are recomputed below.",
 25: "EK 2.3.A.4.i and EK 2.3.A.4.ii located in the table's rows.",
 26: "EK 2.3.A.4's accountability sentence applied: a competitive seat makes accountability "
     "more immediate, which pushes toward the delegate conception.",
 27: "EK 2.3.A.3: elections producing divided government 'can lead to more intense "
     "partisanship,' the mechanism being that each side holds a lever the other must pass.",
 28: "EK 2.3.A.1 (ideological division between parties) and EK 2.3.A.3 (divided government), "
     "neither of which is a choice available to an individual member.",
 29: "EK 2.3.A.3 operationalized: compare party-line votes and nominee rejections across "
     "periods of divided and unified control.",
 30: "EK 2.3.A.4.iii: the politico makes the trustee/delegate pair non-exhaustive.",
}

DIVIDE, BILLS = "Votes dividing the parties (%)", "Major bills enacted"
SAFE, COMP = "Safe district members (%)", "Competitive district members (%)"
OWN, CONST, BOTH = ("Own knowledge and judgement", "The interests of constituents",
                    "A combination of the two")
PERIODS = ["Earliest", "Middle", "Latest"]

TABLE_CHECKS = {
 21: [
  ("the party-dividing share rises in every period while enactments fall in every "
   "period, which is the key",
   lambda t: all(uc.cell(t, a, DIVIDE) < uc.cell(t, b, DIVIDE)
                 for a, b in zip(PERIODS, PERIODS[1:]))
   and all(uc.cell(t, a, BILLS) > uc.cell(t, b, BILLS)
           for a, b in zip(PERIODS, PERIODS[1:]))),
  ("the earliest share is 38, below half, so 'exceeded half in every period' is false",
   lambda t: uc.cell(t, "Earliest", DIVIDE) < 50),
  ("fewer bills passed in the latest period than in the earliest, and by more than "
   "half, so both the third and fifth distractors are false",
   lambda t: uc.cell(t, "Latest", BILLS) < uc.cell(t, "Earliest", BILLS) / 2),
 ],
 22: [
  ("the two columns move in opposite directions across all three periods, which is "
   "the EK 2.3.A.1 pattern the key names",
   lambda t: uc.col(t, DIVIDE) == sorted(uc.col(t, DIVIDE))
   and uc.col(t, BILLS) == sorted(uc.col(t, BILLS), reverse=True)),
  ("no column reports party control of the presidency, role conceptions, districting "
   "or committee leadership, so the four distractors cite data not present",
   lambda t: [h for h in t["headers"][1:]] == [DIVIDE, BILLS]),
 ],
 23: [
  ("both series are present across three periods, so the second and third distractors "
   "are false on the table's face",
   lambda t: BILLS in t["headers"] and len(t["rows"]) == 3),
  ("the two series move in OPPOSITE directions, so the fifth distractor misdescribes "
   "the table it is attached to",
   lambda t: (uc.cell(t, "Latest", DIVIDE) > uc.cell(t, "Earliest", DIVIDE))
   != (uc.cell(t, "Latest", BILLS) > uc.cell(t, "Earliest", BILLS))),
  ("the percentage column does not sum to 100 across periods, because each row is a "
   "separate period rather than a share of one whole",
   lambda t: sum(uc.col(t, DIVIDE)) != 100),
 ],
 24: [
  ("own judgement leads the safe column and constituent interests leads the "
   "competitive column, which is the key",
   lambda t: uc.cell(t, OWN, SAFE) == max(uc.col(t, SAFE))
   and uc.cell(t, CONST, COMP) == max(uc.col(t, COMP))),
  ("the combination row is a minority in both groups, so 'a majority in both' is false",
   lambda t: uc.cell(t, BOTH, SAFE) < 50 and uc.cell(t, BOTH, COMP) < 50),
  ("safe district members name their own judgement MORE often than competitive ones, "
   "so that distractor reverses the table",
   lambda t: uc.cell(t, OWN, SAFE) > uc.cell(t, OWN, COMP)),
  ("the two groups differ on constituent interests by 29 points, so 'the same share' "
   "is false",
   lambda t: uc.cell(t, CONST, COMP) - uc.cell(t, CONST, SAFE) == 29),
  ("each column sums to 100, so the survey is a complete distribution",
   lambda t: all(sum(uc.col(t, c)) == 100 for c in (SAFE, COMP))),
 ],
 25: [
  ("the three row labels are the framework's three role conceptions in order: own "
   "judgement, constituent interests, a combination",
   lambda t: uc.labels(t) == [OWN, CONST, BOTH]),
  ("the combination row is the smallest in the competitive column, which is why it is "
   "the third rather than either of the two the key names",
   lambda t: uc.cell(t, BOTH, COMP) == min(uc.col(t, COMP))),
 ],
 26: [
  ("competitive district members choose constituent interests over own judgement by "
   "more than two to one, which is the pattern the key explains",
   lambda t: uc.cell(t, CONST, COMP) > 2 * uc.cell(t, OWN, COMP)),
  ("safe district members go the other way, so the relationship is a contrast between "
   "the two groups rather than a level in one",
   lambda t: uc.cell(t, OWN, SAFE) > uc.cell(t, CONST, SAFE)),
 ],
}


def _definitions(module):
    """The four CED parentheticals must survive verbatim in their keyed choices."""
    required = {
        1: "political party affiliation",
        2: "ideological extremes",
        3: "no congressional action",
        12: "at least one chamber",
    }
    bad = []
    for i, phrase in required.items():
        key = module.QUESTIONS[i - 1]["choices"][module.QUESTIONS[i - 1]["ans"]]
        if phrase not in key:
            bad.append(f"q{i}: the CED's distinguishing phrase {phrase!r} is no longer in "
                       f"the keyed choice {key!r}")
    if bad:
        print(f"FAIL {module.__name__} definitions")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} definitions: partisan voting, polarization, gridlock and "
          "divided government each keep the CED's own distinguishing wording")


ua.check(v2_3, ANCHORS, GROUNDING)
ua.notation(v2_3)
_definitions(v2_3)
uc.check(v2_3, TABLE_CHECKS)

# WHAT THE REVIEW FOUND
# ---------------------
# No wrong key. Two holdings were checked against AP_US_GOV_CED.md rather than
# recalled, and both are stated narrowly on purpose:
#
#   * Baker v. Carr is about JUSTICIABILITY -- whether a federal court may hear
#     a districting claim at all -- and not about equal district populations as
#     a substantive rule. Item 8's distractors include three substantive rules
#     the case did not announce.
#   * Shaw v. Reno applies "if race is the only factor used in creating the
#     district." Item 9 exists because the overstated version -- that any
#     consideration of race is unconstitutional -- is the single most common
#     error about this case, and a bank that repeats it teaches a student to
#     write a false sentence in an FRQ.
#
# The third thing worth recording is item 13. EK 2.3.A.3's threshold for divided
# government is at least ONE chamber, and the version students carry is usually
# both. Nothing else in this module would catch that error, so the item is
# deliberately placed at the boundary rather than at a clear case.
