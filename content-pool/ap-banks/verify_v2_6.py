"""Structural gate for AP U.S. Government 2.6 Expansion of Presidential Power.

ANCHORS, GROUNDING and the notation check via usgov_anchor, then usgov_check
with the six data items recomputed from their own tables.

THE CED SUPPLIES ITS OWN QUOTATION HERE, WHICH IS RARE
-------------------------------------------------------
EK 2.6.A.1 quotes Federalist No. 70 directly: a strong executive is "essential
to the protection of the country against foreign attacks, to the steady
administration of the laws, to the protection of property, and to the security
of liberty." Four items, quoted by the framework, and therefore examinable as a
list. Items 5 and 6 use it -- one asking which is on it, one asking which is
not -- and _four_purposes below asserts that all four still appear somewhere in
the module and that no item smuggles a fifth onto the list.

THE MISREADING THIS MODULE IS BUILT AGAINST
--------------------------------------------
Federalist No. 70 argues for a SINGLE executive against a PLURAL one, and for
energy in that office. It does not argue that the executive should be free of
checks, and the fourth item in the CED's own quoted list -- "the security of
liberty" -- is the internal evidence. Flattening Hamilton into "the president
should be unchecked" is the standard error, and items 3, 7, 9 and 10 each make
that flattening a wrong answer rather than a plausible one.

THE STRENGTH OF EK 2.6.A.2, WHICH IS WEAKER THAN IT LOOKS
----------------------------------------------------------
The framework says the Twenty-Second Amendment's PASSAGE "demonstrates concern
about the expansion of presidential power." It does not say term limits stopped
the expansion, or that the concern was justified. Item 14 keys on exactly that
distinction -- a commentator saying the amendment failed to arrest the growth is
CONSISTENT with the framework -- because the stronger claim is false and is the
one a bank writes by accident.
"""
import usgov_anchor as ua
import usgov_check as uc
import v2_6

ANCHORS = {
 1: "a single executive",
 2: "an executive divided among several officers",
 3: "part of what makes a government good",
 4: "how one person and a group behave",
 5: "The security of liberty",
 6: "The expansion of the president's authority over time",
 7: "does not argue that the executive should be exempt",
 8: "A chain of equivalences",
 9: "the executive is made capable of acting, and the other branches",
 10: "makes no claim about how far its powers would later grow",
 11: "Concern about the expansion of presidential power",
 12: "treats a partial term of more than two years as one of those times",
 13: "the effort itself indicates widespread concern",
 14: "not that it reversed the trend",
 15: "across different eras and under presidents of both parties",
 16: "continue to be debated in the context of contemporary events",
 17: "it treats silence in the law as permission",
 18: "it requires an affirmative grant for every action",
 19: "judicial limit on an executive claim",
 20: "alongside the Twenty-Second Amendment and judicial limits",
 21: "while treaties ratified per year fell below their early republic level",
 22: "in place of one that does",
 23: "measures activity, not authority",
 24: "from seventeen percent to seventy-eight percent",
 25: "an emergency or the internal management of the executive branch",
 26: "range from limited to expansive and continue to be debated",
 27: "delegating broad discretion to the executive branch",
 28: "track the limited and expansive interpretations",
 29: "reaching opposite conclusions from the same fact",
 30: "how far those powers reach remains contested",
}

GROUNDING = {
 1: "EK 2.6.A.1: 'Federalist No. 70 offers justification for a single executive.' Hamilton "
    "argues against a plural executive, which is the second option.",
 2: "EK 2.6.A.1's contrast: one executive against an office divided among several holders.",
 3: "Federalist No. 70 (required document), 'Energy in the executive,' quoted verbatim. The "
    "argument defines good government to include executive energy, not to excuse restraint.",
 4: "Federalist No. 70 (required document), 'Decision, activity, secrecy, and despatch,' "
    "quoted verbatim. CED skill 4.A asks what EVIDENCE a source offers; this one offers a "
    "comparison of one person with a larger number.",
 5: "EK 2.6.A.1's own quotation: essential 'to the protection of the country against foreign "
    "attacks, to the steady administration of the laws, to the protection of property, and "
    "to the security of liberty.'",
 6: "EK 2.6.A.1's quoted list, tested by exclusion. Expansion of the office over time is not "
    "on it, and reading it in is the standard misuse of the paper.",
 7: "EK 2.6.A.1 read against a president's use of it: a justification for unity and energy is "
    "not a justification for exemption from checks, and 'the security of liberty' is on the "
    "framework's own list of what the design serves.",
 8: "Federalist No. 70 (required document), 'A feeble Executive,' quoted verbatim. CED skill "
    "4.A: the reasoning's SHAPE is a chain of restatements.",
 9: "EK 1.6.A.2 (Federalist No. 51 on checks) with EK 2.6.A.1 (Federalist No. 70 on a single "
    "executive): capacity and restraint as two halves of one design.",
 10: "EK 2.6.A.1: the paper is a justification for a design, not a forecast of later growth.",
 11: "EK 2.6.A.2, verbatim: passage of the Twenty-Second Amendment 'demonstrates concern "
     "about the expansion of presidential power.'",
 12: "U.S. Constitution, Twenty-Second Amendment, quoted verbatim including the second clause "
     "that makes a partial term of more than two years count.",
 13: "EK 1.5.A.2's amendment thresholds -- two-thirds to propose, three-fourths to ratify -- "
     "which is why EK 2.6.A.2 can read an amendment as evidence of widespread concern.",
 14: "EK 2.6.A.2 read at its actual strength: the framework claims the passage demonstrates "
     "concern, not that the amendment reversed anything.",
 15: "EK 2.6.A.2 and EK 2.6.A.3 together: a claim that concern RECURS needs evidence "
     "spread across eras and across administrations of both parties, not a single "
     "amendment or a count of executive activity.",
 16: "EK 2.6.A.3, verbatim: perspectives 'ranging from a limited to a more expansive "
     "interpretation and use of power, continue to be debated in the context of contemporary "
     "events.'",
 17: "EK 2.6.A.3's expansive end: legal silence read as permission.",
 18: "EK 2.6.A.3's limited end: an affirmative grant required for every action.",
 19: "New York Times Co. v. United States (1971), required case, which the CED attaches to "
     "2.6.A. CED holding: bolstered freedom of the press, establishing a 'heavy presumption "
     "against prior restraint' even in cases involving national security.",
 20: "EK 2.6.A.3's range implies movement in both directions, so the pair needs one "
     "instrument of expansion and one of constraint.",
 21: "Data item on a labelled hypothetical; every row's direction of change is recomputed "
     "below.",
 22: "EK 2.4.A.2.ii: executive agreements are informal and need no Senate vote; treaties are "
     "formal and do. The table shows one replacing the other.",
 23: "Data item, CED skill 3.E: a tally of actions measures activity, and EK 2.6.A.3's debate "
     "is about authority.",
 24: "Data item on a labelled hypothetical; the spread is recomputed below.",
 25: "Data item; the two majority rows are identified and their common character named.",
 26: "EK 2.6.A.3 measured: the same public taking the expansive side on two questions and the "
     "limited side on two others is the debate the framework describes.",
 27: "EK 2.4.A.2.iv: executive orders rest partly on power DELEGATED BY CONGRESS, so evidence "
     "of broad delegation locates the cause of expansion in the legislature.",
 28: "EK 2.6.A.3 operationalized: examine the arguments made about contested actions rather "
     "than counting presidential activity.",
 29: "EK 2.6.A.3's two ends differ on what statutory silence means -- permission or absence "
     "of authority -- which is why both speakers can cite the same fact.",
 30: "LO 2.6.A itself: how presidents have interpreted and justified their powers, with "
     "EK 2.6.A.3's continuing debate.",
}

EO, EA, TR = ("Executive orders per year", "Executive agreements per year",
              "Treaties ratified per year")
ERAS = ["Early republic", "Late nineteenth century", "Mid twentieth century",
        "Recent decades"]
ALONE, CONG = "Should be able to act alone (%)", "Should require Congress (%)"
ATTACK, LONG = "Responding to a sudden armed attack", "Committing troops to a long conflict"
REORG, PROGRAM = "Reorganizing an executive agency", "Creating a new federal program"

TABLE_CHECKS = {
 21: [
  ("executive agreements grow more than any other row, from 1 to 215, and treaties "
   "end BELOW their early republic level, 3 against 4",
   lambda t: uc.cell(t, ERAS[3], EA) - uc.cell(t, ERAS[0], EA)
   > max(uc.cell(t, ERAS[3], c) - uc.cell(t, ERAS[0], c) for c in (EO, TR))
   and uc.cell(t, ERAS[3], TR) < uc.cell(t, ERAS[0], TR)),
  ("executive orders FALL in the last era, so 'all three grew steadily' is false",
   lambda t: uc.cell(t, ERAS[3], EO) < uc.cell(t, ERAS[2], EO)),
  ("agreements outgrow treaties by a wide margin, so that distractor is reversed",
   lambda t: uc.cell(t, ERAS[3], EA) > 50 * uc.cell(t, ERAS[3], TR)),
  ("executive orders are not the largest instrument in the last two eras, so 'most "
   "used in every era' is false",
   lambda t: uc.cell(t, ERAS[2], EO) < uc.cell(t, ERAS[2], EA)),
  ("agreements exceed treaties in the two most recent eras and NOT in the two "
   "earliest -- two of four, which is enough to falsify 'less often than treaties "
   "in every era' and is the count the rationale originally got wrong",
   lambda t: sum(1 for e in ERAS if uc.cell(t, e, EA) > uc.cell(t, e, TR)) == 2
   and uc.cell(t, ERAS[1], EA) < uc.cell(t, ERAS[1], TR)),
 ],
 22: [
  ("the instrument needing no Senate vote rises while the one requiring it falls, "
   "which is the substitution the key describes",
   lambda t: uc.cell(t, ERAS[3], EA) > uc.cell(t, ERAS[0], EA)
   and uc.cell(t, ERAS[3], TR) < uc.cell(t, ERAS[0], TR)),
  ("executive orders remain in the dozens per year in both recent eras, so "
   "'abandoned executive orders' is false",
   lambda t: min(uc.cell(t, ERAS[2], EO), uc.cell(t, ERAS[3], EO)) > 30),
 ],
 23: [
  ("all three instruments and four eras are present, so two of the distractors are "
   "false on the table's face",
   lambda t: {EO, EA, TR} <= set(t["headers"]) and len(t["rows"]) == 4),
  ("every cell is a whole count rather than a percentage",
   lambda t: all(c.isdigit() for row in t["rows"] for c in row[1:])),
 ],
 24: [
  ("the four acting-alone figures span 17 to 78, a spread of 61 points",
   lambda t: min(uc.col(t, ALONE)) == 17 and max(uc.col(t, ALONE)) == 78
   and max(uc.col(t, ALONE)) - min(uc.col(t, ALONE)) == 61),
  ("two situations draw a majority for acting alone and two draw a majority against, "
   "so neither 'a majority in every situation' distractor holds",
   lambda t: sum(1 for lab in uc.labels(t) if uc.cell(t, lab, ALONE) > 50) == 2),
  ("support is highest for the armed attack and LOWEST for creating a program, so "
   "that distractor is reversed",
   lambda t: uc.cell(t, ATTACK, ALONE) == max(uc.col(t, ALONE))
   and uc.cell(t, PROGRAM, ALONE) == min(uc.col(t, ALONE))),
  ("every row's two figures sum to 100, so each is a complete two-way split",
   lambda t: all(uc.cell(t, lab, ALONE) + uc.cell(t, lab, CONG) == 100
                 for lab in uc.labels(t))),
 ],
 25: [
  ("the two majority rows are the armed attack and the agency reorganization, exactly "
   "the pair the key characterizes",
   lambda t: [lab for lab in uc.labels(t) if uc.cell(t, lab, ALONE) > 50]
   == [ATTACK, REORG]),
  ("the two minority rows are the long conflict and the new program, so the "
   "distractors describing military commitment or new programs fit the OTHER pair",
   lambda t: [lab for lab in uc.labels(t) if uc.cell(t, lab, ALONE) < 50]
   == [LONG, PROGRAM]),
 ],
 26: [
  ("the public takes the expansive side on two situations and the limited side on "
   "two, which is EK 2.6.A.3's debate measured rather than resolved",
   lambda t: sum(1 for lab in uc.labels(t) if uc.cell(t, lab, ALONE) > 50) == 2
   and sum(1 for lab in uc.labels(t) if uc.cell(t, lab, CONG) > 50) == 2),
  ("no row concerns term limits, appointments, vetoes or Federalist No. 70, so the "
   "four distractors cite statements these data do not measure",
   lambda t: not any(k in lab.lower() for lab in uc.labels(t)
                     for k in ("term", "nominee", "veto", "confirm"))),
 ],
}


def _four_purposes(module):
    """EK 2.6.A.1's quoted four-part list must be complete and unpadded."""
    four = ["protection of the country against foreign attacks",
            "steady administration of the laws",
            "protection of property",
            "security of liberty"]
    blob = " ".join(item["q"] + " " + item["why"] + " " + " ".join(item["choices"])
                    for item in module.QUESTIONS).lower()
    missing = [p for p in four if p not in blob]
    bad = [f"EK 2.6.A.1's quoted purpose {p!r} appears nowhere in the module"
           for p in missing]
    # Item 6 asks which is NOT on the list; its key must not be one of the four.
    q6 = module.QUESTIONS[5]
    if any(p in q6["choices"][q6["ans"]].lower() for p in four):
        bad.append("q6: the keyed 'not on the list' choice is in fact one of the four")
    for k, c in enumerate(q6["choices"]):
        if k == q6["ans"]:
            continue
        if not any(p in c.lower() for p in four):
            bad.append(f"q6: distractor {'ABCDE'[k]} is not one of EK 2.6.A.1's four, so "
                       "the item has two defensible keys")
    if bad:
        print(f"FAIL {module.__name__} four purposes")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} four purposes: all four of EK 2.6.A.1's quoted purposes "
          "appear, and item 6's four distractors are exactly those four")


ua.shape(v2_6)
ua.check(v2_6, ANCHORS, GROUNDING)
ua.notation(v2_6)
_four_purposes(v2_6)
uc.check(v2_6, TABLE_CHECKS)

# WHAT THE REVIEW FOUND
# ---------------------
# No wrong key. The check worth explaining is _four_purposes, and specifically
# its second half. Item 6 asks which option is NOT among the four purposes the
# CED quotes from Federalist No. 70. An item of that shape is only sound if
# every distractor really is on the list -- otherwise there are two defensible
# keys and the student who knows the material best is the one most likely to
# hesitate. So the check does not merely confirm the key is off the list; it
# confirms all four distractors are on it. A NOT-question is the one question
# type where the distractors have to be verified as carefully as the key.
#
# The second thing recorded here rather than assumed: Taft's and Theodore
# Roosevelt's writings are ILLUSTRATIVE EXAMPLES in the CED (p. 66), not
# required documents. Their competing views of the office are the obvious
# material for a topic about interpretations of presidential power, and this
# module deliberately does not use them by name -- no item requires having read
# either, and the limited/expansive range is taught through EK 2.6.A.3's own
# wording instead.
#
# One wrong number in a rationale, caught by the arithmetic: item 21's `why`
# said executive agreements "overtake treaties from the late nineteenth century
# onward." They do not -- that era is 6 agreements against 9 treaties. Agreements
# lead in the two most recent eras only, two of four, which is still more than
# enough to falsify the distractor claiming they were always fewer. The keyed
# choice never depended on the wrong count; the sentence explaining it did.
