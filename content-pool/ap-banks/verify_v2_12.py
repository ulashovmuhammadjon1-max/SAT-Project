"""Structural gate for AP U.S. Government 2.12 The Bureaucracy.

ANCHORS, GROUNDING and the notation check via usgov_anchor, then usgov_check
with the six data items recomputed from their own tables.

TWO CED PARENTHETICALS THAT DIFFER ON TWO AXES, NOT ONE
---------------------------------------------------------
EK 2.12.A.1.iv defines an IRON TRIANGLE as an alliance of congressional
committees, bureaucratic agencies and interest groups prominent in specific
policy areas. EK 2.12.A.1.v defines an ISSUE NETWORK as a TEMPORARY coalition
formed to promote a common issue or agenda.

They differ in MEMBERSHIP (three named corners against open) and in DURATION
(standing against temporary). A bank that teaches only the first axis produces
students who classify any three-party coalition as a triangle, which is why
item 9 gives them a temporary coalition containing agencies and outside groups
and item 8 gives them a durable one. _two_axes below asserts that both axes are
stated in the module: the word "temporary" must appear in the issue-network
key, and the three corners must appear in the iron-triangle key.

THE MERIT SYSTEM'S THIRD CRITERION
-----------------------------------
EK 2.12.A.2's list is professionalism, specialization and NEUTRALITY.
Neutrality is the one a patronage system cannot supply and the one that makes
an agency's advice worth having across a change of administration, so items 14
to 18 turn on it. Item 12's fifth distractor keeps two of the three criteria and
substitutes party affiliation -- the thing the merit system is defined against.

The CED also hedges: the civil service PRIMARILY uses a merit system. Item 16
keys on that word and item 23 finds it in the data, because a bank that drops
the hedge teaches that political appointment no longer exists, which would
contradict EK 2.5.A.1's own list of confirmable positions.
"""
import usgov_anchor as ua
import usgov_check as uc
import v2_12

ANCHORS = {
 1: "departments, agencies, commissions, and government corporations",
 2: "Writing and enforcing regulations",
 3: "Issuing fines",
 4: "Testifying before Congress, which serves Congress's oversight power",
 5: "congressional committees, bureaucratic agencies, and interest groups",
 6: "a temporary coalition that forms to promote a common issue",
 7: "three fixed kinds of member and is a standing alliance",
 8: "since the three named corners work together in a specific policy area over time",
 9: "since it is a temporary coalition formed to promote a common issue",
 10: "with little participation from anyone else",
 11: "professionalism, specialization, and neutrality",
 12: "Professionalism, specialization, and neutrality",
 13: "bureaucratic jobs are politically appointed",
 14: "since the standards did not change with the political leadership",
 15: "more likely to report what is true rather than what is wanted",
 16: "particularly senior ones, are still filled by political appointment",
 17: "needs officials who share the administration's priorities",
 18: "Continuity and expertise would be lost every time an administration changed",
 19: "is what a permanent professional bureaucracy supplies",
 20: "requires an organization the clause does not itself describe",
 21: "rose from under a tenth to nearly nine tenths",
 22: "primarily uses a merit system as opposed to political patronage",
 23: "still accounts for eleven percent of positions",
 24: "is not the area imposing the most fines",
 25: "Writing and enforcing regulations, issuing fines, and testifying before Congress",
 26: "counts actions without regard to their scope",
 27: "with the legislative branch; issuing fines, with a regulated party",
 28: "give a statute its operative content",
 29: "consistently support one another's positions over time",
 30: "staffed mainly on merit",
}

GROUNDING = {
 1: "EK 2.12.A.1, verbatim: the bureaucracy 'is composed of departments, agencies, "
    "commissions, and government corporations.'",
 2: "EK 2.12.A.1.i: 'Writing and enforcing regulations.'",
 3: "EK 2.12.A.1.ii: 'Issuing fines', listed separately from writing regulations.",
 4: "EK 2.12.A.1.iii (testifying before Congress) seen from the other side as EK 2.14.A.1.ii "
    "(investigation and committee hearings of bureaucratic activity).",
 5: "EK 2.12.A.1.iv's parenthesis: iron triangles are 'alliances of congressional committees, "
    "bureaucratic agencies, and interest groups.' Three NAMED corners, not any three actors.",
 6: "EK 2.12.A.1.v's parenthesis: issue networks are 'temporary coalitions that form to "
    "promote a common issue or agenda.'",
 7: "EK 2.12.A.1.iv against EK 2.12.A.1.v on both axes at once: membership and duration.",
 8: "EK 2.12.A.1.iv applied; the actors are the three named corners and the relationship is "
    "durable and policy-specific.",
 9: "EK 2.12.A.1.v applied; the coalition is temporary and contains actors outside the three "
    "corners. Concerning one policy area is true of both concepts and distinguishes neither.",
 10: "EK 2.12.A.1.iv read for its consequence: the three actors with the greatest stake and "
     "information can settle a policy area before it reaches a wider audience.",
 11: "EK 2.12.A.2, verbatim: a merit system 'that prioritizes hiring and promotion based on "
     "professionalism, specialization, and neutrality.'",
 12: "EK 2.12.A.2's closed list of three. The fifth distractor keeps two and substitutes party "
     "affiliation, which is what the merit system is defined against.",
 13: "EK 2.12.A.2, verbatim: political patronage, 'whereby bureaucratic jobs are politically "
     "appointed.'",
 14: "EK 2.12.A.2's third criterion isolated: neutrality is specifically what does not change "
     "when the political leadership does.",
 15: "EK 2.12.A.2's neutrality read for its value, the same institutional logic as Art. III "
     "tenure: remove the incentive to say what the appointing power wants to hear.",
 16: "EK 2.12.A.2's word PRIMARILY, which leaves room for the political appointments "
     "EK 2.5.A.1 lists as subject to Senate confirmation.",
 17: "EK 2.14.B.1: presidential ideology, authority and influence affect how agencies carry "
     "out the administration's goals, and appointees are the mechanism.",
 18: "EK 2.12.A.2's three criteria read as what deep politicization would cost.",
 19: "Federalist No. 70 (required document), 'steady administration of the laws,' quoted "
     "verbatim; the CED attaches Federalist No. 70 to 2.12.A.",
 20: "U.S. Constitution Art. II Sec. 3, the Take Care Clause, quoted verbatim. The duty is the "
     "president's and the text supplies no machinery, which is why EK 2.13.A.1 describes power "
     "DELEGATED by Congress.",
 21: "Data item on a labelled hypothetical; both series are recomputed below.",
 22: "EK 2.12.A.2 seen as data: examination replacing political appointment over time.",
 23: "EK 2.12.A.2's hedge 'primarily' located in the data as a residual eleven percent.",
 24: "Data item on a labelled hypothetical; the column leaders are recomputed below.",
 25: "EK 2.12.A.1.i, ii and iii mapped onto the table's three columns; iv and v are "
     "relationships rather than countable actions, which is why no column reports them.",
 26: "Data item, CED skill 3.E: an unweighted tally treats every action as equivalent.",
 27: "EK 2.12.A.1.ii and iii, each paired with the counterparty it is directed at.",
 28: "EK 2.12.A.1.i with EK 2.13.A.1: writing regulations requires the discretion a statute "
     "leaves open, which is why implementation is not mere execution.",
 29: "EK 2.12.A.1.iv operationalized: look for consistency among the three named corners over "
     "time, not for the size or activity of the agency alone.",
 30: "EK 2.12.A.1's five activities and EK 2.12.A.2's merit system in one sentence.",
}

EXAM, APPT = ("Positions filled by competitive examination (%)",
              "Positions filled by political appointment (%)")
ERAS = ["Early era", "Middle era", "Recent era"]
REGS, FINES, APPEAR = "Regulations issued", "Fines imposed", "Appearances before Congress"
ENV, TRANS, FIN, VET = ("Environment", "Transportation", "Financial regulation",
                        "Veterans affairs")

TABLE_CHECKS = {
 21: [
  ("examination rises from 8 to 89 percent while political appointment falls from 92 "
   "to 11",
   lambda t: uc.cell(t, ERAS[0], EXAM) == 8 and uc.cell(t, ERAS[2], EXAM) == 89
   and uc.cell(t, ERAS[0], APPT) == 92 and uc.cell(t, ERAS[2], APPT) == 11),
  ("political appointment FALLS across the three eras, so that distractor is reversed",
   lambda t: uc.col(t, APPT) == sorted(uc.col(t, APPT), reverse=True)),
  ("appointment holds a majority only in the early era and examination only from the "
   "middle era on, so neither 'in every era' distractor holds",
   lambda t: sum(1 for e in ERAS if uc.cell(t, e, APPT) > 50) == 1
   and sum(1 for e in ERAS if uc.cell(t, e, EXAM) > 50) == 2),
  ("the recent era's two shares are 89 and 11, nowhere near equal",
   lambda t: abs(uc.cell(t, ERAS[2], EXAM) - uc.cell(t, ERAS[2], APPT)) > 50),
  ("each era's two shares sum to 100, so the table is a complete two-way split",
   lambda t: all(uc.cell(t, e, EXAM) + uc.cell(t, e, APPT) == 100 for e in ERAS)),
 ],
 22: [
  ("the two columns are exactly EK 2.12.A.2's contrast: merit examination against "
   "political appointment",
   lambda t: "examination" in EXAM and "political appointment" in APPT),
  ("no column reports regulations, triangles, networks or hearings, so the four "
   "distractors cite activities the table does not measure",
   lambda t: [h for h in t["headers"][1:]] == [EXAM, APPT]),
 ],
 23: [
  ("political appointment survives at eleven percent in the recent era, which is "
   "exactly what the framework's word PRIMARILY leaves room for",
   lambda t: uc.cell(t, ERAS[2], APPT) == 11 and uc.cell(t, ERAS[2], APPT) > 0),
  ("examination's eighty-nine percent is true but is the OTHER half of the same fact, "
   "which is why it is a distractor rather than the key",
   lambda t: uc.cell(t, ERAS[2], EXAM) == 89),
 ],
 24: [
  ("the regulations leader and the fines leader are different rows",
   lambda t: uc.labels(t)[uc.col(t, REGS).index(max(uc.col(t, REGS)))]
   != uc.labels(t)[uc.col(t, FINES).index(max(uc.col(t, FINES)))]),
  ("environment leads regulations and financial regulation leads both fines and "
   "appearances",
   lambda t: uc.cell(t, ENV, REGS) == max(uc.col(t, REGS))
   and uc.cell(t, FIN, FINES) == max(uc.col(t, FINES))
   and uc.cell(t, FIN, APPEAR) == max(uc.col(t, APPEAR))),
  ("veterans affairs imposed 12 fines against 45 regulations, so 'every area imposed "
   "more fines than regulations' is false",
   lambda t: uc.cell(t, VET, FINES) < uc.cell(t, VET, REGS)),
  ("the four areas differ by more than an order of magnitude on fines, so 'similar "
   "rates' is false",
   lambda t: max(uc.col(t, FINES)) > 100 * min(uc.col(t, FINES))),
 ],
 25: [
  ("the three columns are exactly EK 2.12.A.1's first three activities",
   lambda t: [h for h in t["headers"][1:]] == [REGS, FINES, APPEAR]),
  ("no column reports iron triangles or issue networks, which are relationships rather "
   "than countable actions",
   lambda t: not any(k in h.lower() for h in t["headers"]
                     for k in ("triangle", "network"))),
 ],
 26: [
  ("a regulations column and a fines column are both present and four areas are "
   "reported, so three distractors are false on the table's face",
   lambda t: REGS in t["headers"] and FINES in t["headers"] and len(t["rows"]) == 4),
  ("every cell is a count rather than a percentage, and no column sums to 100",
   lambda t: all(sum(uc.col(t, c)) != 100 for c in (REGS, FINES, APPEAR))),
 ],
}


def _two_axes(module):
    """Both distinguishing axes must be stated where the two concepts are keyed."""
    bad = []
    triangle_key = module.QUESTIONS[4]["choices"][module.QUESTIONS[4]["ans"]].lower()
    network_key = module.QUESTIONS[5]["choices"][module.QUESTIONS[5]["ans"]].lower()
    for corner in ("congressional committees", "bureaucratic agencies", "interest groups"):
        if corner not in triangle_key:
            bad.append(f"q5: the iron-triangle key omits EK 2.12.A.1.iv's corner {corner!r}")
    if "temporary" not in network_key:
        bad.append("q6: the issue-network key omits EK 2.12.A.1.v's word 'temporary', which "
                   "is the duration axis and half of what distinguishes the two concepts")
    both = module.QUESTIONS[6]["choices"][module.QUESTIONS[6]["ans"]].lower()
    if "temporary" not in both or "three" not in both:
        bad.append("q7: the key that contrasts the two concepts must state BOTH axes, "
                   "membership and duration")
    if bad:
        print(f"FAIL {module.__name__} two axes")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} two axes: the iron-triangle key names all three of "
          "EK 2.12.A.1.iv's corners, the issue-network key keeps 'temporary', and the "
          "contrast item states both membership and duration")


def _merit_criteria(module):
    """EK 2.12.A.2's three criteria are a closed list, and party affiliation is not on it."""
    q = module.QUESTIONS[11]
    key = q["choices"][q["ans"]].lower()
    bad = []
    for c in ("professionalism", "specialization", "neutrality"):
        if c not in key:
            bad.append(f"q12: the keyed list omits EK 2.12.A.2's criterion {c!r}")
    for word in ("party", "loyalty", "patronage"):
        if word in key:
            bad.append(f"q12: the keyed list includes {word!r}, which EK 2.12.A.2 names as "
                       "the CONTRAST to the merit system rather than as one of its criteria")
    if bad:
        print(f"FAIL {module.__name__} merit criteria")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} merit criteria: the keyed list is exactly EK 2.12.A.2's "
          "professionalism, specialization and neutrality, with nothing added")


ua.check(v2_12, ANCHORS, GROUNDING)
ua.notation(v2_12)
_two_axes(v2_12)
_merit_criteria(v2_12)
uc.check(v2_12, TABLE_CHECKS)

# WHAT THE REVIEW FOUND
# ---------------------
# No wrong key. One defect in the source file itself, caught by running it: a
# stray walrus expression had been left inside item 29's dict, between `ans` and
# `why`. Python accepted it -- it evaluated to an empty string bound to an unused
# name -- so the module imported cleanly and every structural check passed. It
# would have shipped as dead code inside a live question.
#
# Worth recording because it is a failure mode this bank had not seen before:
# every other defect found in these twenty modules was a wrong number or a
# misstated claim, things a reader or a recomputation catches. This one was
# syntactically valid, semantically inert, and invisible to all of it. The only
# reason it surfaced is that the module is run, not just read -- which is an
# argument for the verifier existing at all, independent of anything it checks.
