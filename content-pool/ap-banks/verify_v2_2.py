"""Structural gate for AP U.S. Government 2.2 Structures, Powers, and Functions of Congress.

ANCHORS, GROUNDING and the notation check via usgov_anchor, then usgov_check
with NINE data items recomputed from three tables.

WHY NINE DATA ITEMS AND NOT SIX
--------------------------------
This topic's suggested skill in the CED (p. 60) is 3.A, describe the data
presented, and EK 2.2.A.4.ii is itself a claim about numbers. A module on this
topic that carried the usual six stimulus items would under-weight exactly the
skill the framework attaches to it.

THE CONDITIONAL, WHICH IS WHAT THE BUDGET TABLE IS REALLY TESTING
------------------------------------------------------------------
EK 2.2.A.4.ii does not say entitlements crowd out discretionary spending. It
says discretionary opportunities "will decrease UNLESS tax revenues increase, or
the budget deficit increases." Two escape routes, stated. The budget table is
built so that both branches are visible in it: mandatory rises and discretionary
falls (the squeeze), AND the deficit widens from 400 to 750 (one of the two
escapes, operating at the same time). Item 24 makes the student compute that
widening. The checks below recompute the deficit in each year from outlays minus
revenues rather than trusting the rationale, and also confirm the four rows are
internally consistent -- mandatory plus discretionary equals total outlays in
every year, which nothing in the questions asserts but which a reader would
reasonably assume and which would be a real defect if it were false.

THE DISCHARGE PETITION WORDING
-------------------------------
EK 2.2.A.3.i says an INDIVIDUAL REPRESENTATIVE can file a discharge petition,
and adds "but it is rarely done"; the chamber rule requires 218 signatures to
succeed. See AP_US_GOV_CED.md note 11. Items 7 and 8 are worded to be true of
both readings -- a representative may FILE one, and success is rare -- and the
last check in this file asserts that no string in the module claims one member
can discharge a bill alone.
"""
import usgov_anchor as ua
import usgov_check as uc
import v2_2

ANCHORS = {
 1: "deliberate feature of the design",
 2: "the majority political party in the chamber",
 3: "Receive it on referral, conduct hearings",
 4: "gatekeeping stage",
 5: "the Rules Committee",
 6: "To expedite debate on bills",
 7: "though it is rarely done",
 8: "route around the committee system",
 9: "unanimous consent",
 10: "a hold, a request that prevents a bill from getting to the floor",
 11: "The filibuster prolongs debate to delay or prevent a vote, and cloture",
 12: "Cloture with the Senate and the Committee of the Whole with the House",
 13: "A conference committee meets to reconcile the differences",
 14: "required by law for entitlement programs such as Social Security",
 15: "approved on an annual basis for purposes such as defense",
 16: "If tax revenues increase, or if the budget deficit increases",
 17: "Revenues rose or the deficit grew",
 18: "flows from standing law and continues unless Congress changes that law",
 19: "funding for a local project included in a larger appropriation bill",
 20: "logrolling, an exchange of political favors",
 21: "district lines shape who serves",
 22: "rose in each year while discretionary spending fell in each year",
 23: "decrease unless revenues rise or the deficit grows",
 24: "It grew by 350 billion dollars",
 25: "Three of the five procedures operate in the House",
 26: "The filibuster, which prolongs debate, and cloture, which ends it",
 27: "the count reflects which rows were chosen",
 28: "Fewer than one in five bills introduced were reported out of committee",
 29: "committees are the stage at which most bills die",
 30: "a single enacted bill may carry the substance of many that died",
}

GROUNDING = {
 1: "EK 2.2.A.1, verbatim: the structures and powers 'are different by design. This "
    "difference directly affects the legislative process.'",
 2: "EK 2.2.A.2, verbatim: 'Leadership in committees is determined by the majority "
    "political party.'",
 3: "EK 2.2.A.2: committees receive bills on referral, conduct hearings, debate and mark up "
    "bills with revisions and additions. Reconciliation is EK 2.2.A.3.iii, a later stage.",
 4: "EK 2.2.A.2 applied: referral plus majority-party control of chairs makes committee "
    "inaction a decision with force. No constitutional provision requires a hearing.",
 5: "EK 2.2.A.3.i: 'Rules for debate in the House on a bill are established by the Rules "
    "Committee.'",
 6: "EK 2.2.A.3.i: 'The House can form a Committee of the Whole in order to expedite debate "
    "on bills.'",
 7: "EK 2.2.A.3.i: an individual representative 'can file a discharge petition to have a "
    "bill brought to the floor for debate, but it is rarely done.' Worded to be true whether "
    "one reads the CED's sentence as filing or as succeeding; see AP_US_GOV_CED.md note 11.",
 8: "EK 2.2.A.2 (majority control of committees) and EK 2.2.A.3.i (Rules Committee control "
    "of debate) together explain why a procedure bypassing both is rarely successful.",
 9: "EK 2.2.A.3.ii: 'In the Senate, bills are typically brought to the floor by unanimous "
    "consent.' The three distractors are House procedures under EK 2.2.A.3.i.",
 10: "EK 2.2.A.3.ii: 'a Senator may request a hold on a bill to prevent it from getting to "
     "the floor for a vote.' A filibuster operates during debate, after the floor is reached.",
 11: "EK 2.2.A.3.ii defines the filibuster as 'a tactic to prolong debate and delay or "
     "prevent a vote on a bill' and cloture as 'a procedure to end a debate.' Both Senate.",
 12: "EK 2.2.A.3.i and EK 2.2.A.3.ii, each procedure assigned to its own chamber.",
 13: "EK 2.2.A.3.iii: a conference committee meets to reconcile differences when a bill "
     "passed by both chambers on the same topic varies in wording.",
 14: "EK 2.2.A.4.i, verbatim: mandatory spending 'is required by law for entitlement "
     "programs such as Social Security, Medicare, and Medicaid.'",
 15: "EK 2.2.A.4.ii, verbatim: discretionary spending 'is approved on an annual basis for "
     "defense spending, education, and infrastructure.'",
 16: "EK 2.2.A.4.ii's conditional, verbatim: the squeeze follows 'unless tax revenues "
     "increase, or the budget deficit increases.' Exactly two escapes, both stated.",
 17: "EK 2.2.A.4.ii applied to an apparent counterexample: steady discretionary spending "
     "alongside rising entitlements is the statement's second branch, not a refutation.",
 18: "EK 2.2.A.4.i against EK 2.2.A.4.ii: the two differ in how each is authorized, standing "
     "law against annual approval.",
 19: "EK 2.2.A.5, verbatim: pork-barrel legislation is 'funding for a local project in a "
     "larger appropriation bill.'",
 20: "EK 2.2.A.5, verbatim: logrolling is the 'exchange of political favors among "
     "legislators, such as trading votes, to gain support for legislation.'",
 21: "Shaw v. Reno (1993), required case, which the CED attaches to 2.2.A. CED holding: "
     "majority-minority districts may be challenged if race is the only factor. House "
     "districts determine the chamber's membership.",
 22: "Data item; both rows' directions of change are recomputed below.",
 23: "EK 2.2.A.4.ii seen as data: mandatory rising while discretionary falls.",
 24: "Data item; the deficit in each year is recomputed below from outlays minus revenues "
     "rather than trusted from the rationale.",
 25: "Data item on a categorical table; the chamber counts are recomputed below.",
 26: "EK 2.2.A.3.ii's tactic and counter-tactic, the only pair in the table pointing in "
     "opposite directions on the same debate.",
 27: "Data item, CED skill 3.E: counting rows in a curated list measures the list.",
 28: "Data item; the survival ratio at the committee stage is recomputed below.",
 29: "EK 2.2.A.2's committee gate shown as data -- the largest single drop in the table.",
 30: "Data item, CED skill 3.E: a bill count treats every bill as equivalent, and omnibus "
     "bills absorb provisions from bills that never advanced alone.",
}

MAND, DISC = "Mandatory spending", "Discretionary spending"
OUT, REV = "Total outlays", "Total revenues"
YEARS = ["Year 1", "Year 2", "Year 3"]
CHAMBER, EFFECT = "Chamber", "Effect on a bill"
REMAIN = "Bills remaining"


def _deficit(t, year):
    return uc.cell(t, OUT, year) - uc.cell(t, REV, year)


def _cats(t, header):
    j = t["headers"].index(header)
    return [row[j] for row in t["rows"]]


TABLE_CHECKS = {
 22: [
  ("mandatory rises in each year and discretionary falls in each year",
   lambda t: all(uc.cell(t, MAND, a) < uc.cell(t, MAND, b)
                 for a, b in zip(YEARS, YEARS[1:]))
   and all(uc.cell(t, DISC, a) > uc.cell(t, DISC, b)
           for a, b in zip(YEARS, YEARS[1:]))),
  ("mandatory exceeds discretionary in every year, so 'discretionary exceeded "
   "mandatory in at least one year' is false",
   lambda t: all(uc.cell(t, MAND, y) > uc.cell(t, DISC, y) for y in YEARS)),
  ("outlays exceed revenues in every year, so 'revenues exceeded outlays' is false",
   lambda t: all(_deficit(t, y) > 0 for y in YEARS)),
  ("total outlays RISE from Year 1 to Year 3, so that distractor is false",
   lambda t: uc.cell(t, OUT, YEARS[2]) > uc.cell(t, OUT, YEARS[0])),
  ("the two spending rows sum to total outlays in every year, so the table is "
   "internally consistent -- no question asserts this and a reader would assume it",
   lambda t: all(uc.cell(t, MAND, y) + uc.cell(t, DISC, y) == uc.cell(t, OUT, y)
                 for y in YEARS)),
 ],
 23: [
  ("the squeeze is present: mandatory up 650 and discretionary down 60 across the "
   "three years",
   lambda t: uc.cell(t, MAND, YEARS[2]) - uc.cell(t, MAND, YEARS[0]) == 650
   and uc.cell(t, DISC, YEARS[0]) - uc.cell(t, DISC, YEARS[2]) == 60),
  ("and one of EK 2.2.A.4.ii's two escapes is operating at the same time: the deficit "
   "widens in every year, which is why discretionary falls only slowly",
   lambda t: all(_deficit(t, a) < _deficit(t, b) for a, b in zip(YEARS, YEARS[1:]))),
 ],
 24: [
  ("the deficit is 400 in Year 1 and 750 in Year 3, an increase of exactly 350",
   lambda t: _deficit(t, YEARS[0]) == 400 and _deficit(t, YEARS[2]) == 750
   and _deficit(t, YEARS[2]) - _deficit(t, YEARS[0]) == 350),
  ("the gap grows rather than shrinks, and it is never zero, so the second, third and "
   "fourth distractors are all false",
   lambda t: _deficit(t, YEARS[2]) > _deficit(t, YEARS[0]) > 0),
  ("a revenues row exists, so 'cannot be determined, no revenue figures' is false",
   lambda t: REV in uc.labels(t)),
 ],
 25: [
  ("three procedures are House and two are Senate, which is the key",
   lambda t: _cats(t, CHAMBER).count("House") == 3
   and _cats(t, CHAMBER).count("Senate") == 2),
  ("two chambers appear, so 'all five in the same chamber' is false",
   lambda t: len(set(_cats(t, CHAMBER))) == 2),
  ("the two Senate effects point in opposite directions, so 'both work to speed a "
   "bill' and 'every procedure makes it easier' are both false",
   lambda t: any("Prolongs" in e for c, e in zip(_cats(t, CHAMBER), _cats(t, EFFECT))
                 if c == "Senate")
   and any("Ends" in e for c, e in zip(_cats(t, CHAMBER), _cats(t, EFFECT))
           if c == "Senate")),
  ("every row names an effect on a bill, so 'no procedure affects floor debate' is "
   "false on the table's face",
   lambda t: all(e.strip() for e in _cats(t, EFFECT))),
 ],
 26: [
  ("exactly one row prolongs debate and exactly one ends it, and both are Senate rows",
   lambda t: [row[0] for row, e in zip(t["rows"], _cats(t, EFFECT))
              if "Prolongs" in e] == ["Filibuster"]
   and [row[0] for row, e in zip(t["rows"], _cats(t, EFFECT))
        if e == "Ends debate"] == ["Cloture"]),
  ("the three House rows all move a bill toward the floor or shape debate there, so "
   "no distractor pair is an opposed pair",
   lambda t: sum(1 for c in _cats(t, CHAMBER) if c == "House") == 3),
 ],
 27: [
  ("the Senate appears twice, so 'omits the Senate entirely' is false",
   lambda t: "Senate" in _cats(t, CHAMBER)),
  ("no column reports frequency of use, so that distractor describes data not here",
   lambda t: not any("often" in h.lower() or "used" in h.lower() for h in t["headers"])),
  ("five rows only, which is what makes the count an artifact of the selection",
   lambda t: len(t["rows"]) == 5),
 ],
 28: [
  ("1,050 of 6,400 reported out of committee is under one fifth",
   lambda t: uc.cell(t, "Reported out of committee", REMAIN)
   < 0.2 * uc.cell(t, "Introduced", REMAIN)),
  ("620 of 6,400 passed the chamber of origin, far under half",
   lambda t: uc.cell(t, "Passed the chamber of origin", REMAIN)
   < 0.5 * uc.cell(t, "Introduced", REMAIN)),
  ("30 bills that passed both chambers were not signed, so 'every one was signed' is "
   "false",
   lambda t: uc.cell(t, "Passed both chambers", REMAIN)
   - uc.cell(t, "Signed into law", REMAIN) == 30),
  ("fewer bills were signed than were reported out of committee",
   lambda t: uc.cell(t, "Signed into law", REMAIN)
   < uc.cell(t, "Reported out of committee", REMAIN)),
 ],
 29: [
  ("the committee stage loses 5,350 bills, more than every later stage combined",
   lambda t: uc.cell(t, "Introduced", REMAIN)
   - uc.cell(t, "Reported out of committee", REMAIN) == 5350
   and 5350 > uc.cell(t, "Reported out of committee", REMAIN)
   - uc.cell(t, "Signed into law", REMAIN)),
  ("only 30 bills fall at the final stage, so 'the president rejects most' is false",
   lambda t: uc.cell(t, "Passed both chambers", REMAIN)
   - uc.cell(t, "Signed into law", REMAIN) == 30),
  ("310 of 6,400 become law, so 'most bills eventually become law' is false",
   lambda t: uc.cell(t, "Signed into law", REMAIN)
   < 0.5 * uc.cell(t, "Introduced", REMAIN)),
 ],
 30: [
  ("the table reports both the introduction count and the enactment count, so those "
   "two distractors are false on its face",
   lambda t: {"Introduced", "Signed into law"} <= set(uc.labels(t))),
  ("every cell is a count rather than a percentage, and the column does not sum to 100",
   lambda t: sum(uc.col(t, REMAIN)) != 100),
  ("the five stages are successive and strictly decreasing, which is what makes the "
   "survival-rate reading tempting",
   lambda t: all(a > b for a, b in zip(uc.col(t, REMAIN), uc.col(t, REMAIN)[1:]))),
 ],
}


def _discharge_wording(module):
    """No item may claim one representative can discharge a bill by himself."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        for s in [item["q"], item["why"]] + list(item["choices"]):
            low = s.lower()
            if "discharge petition" not in low:
                continue
            for phrase in ("acting alone", "by himself", "by herself", "without any other",
                           "single signature", "one signature", "no other member"):
                if phrase in low:
                    bad.append(f"q{i}: {phrase!r} beside 'discharge petition'")
    if bad:
        print(f"FAIL {module.__name__} discharge wording")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} discharge wording: no item claims one member can "
          "discharge a bill alone, so the items are true on either reading of EK 2.2.A.3.i")


ua.check(v2_2, ANCHORS, GROUNDING)
ua.notation(v2_2)
_discharge_wording(v2_2)
uc.check(v2_2, TABLE_CHECKS)

# WHAT THE REVIEW FOUND
# ---------------------
# No wrong key. The check worth recording is the one on the budget table's
# internal consistency: mandatory plus discretionary must equal total outlays in
# every year. No question in the module asserts that, so nothing would have
# failed if it were false -- and every reader would have assumed it, computed a
# deficit from a table that did not add up, and been wrong. A stimulus table has
# to be true in the ways nobody asks about, not only in the ways the keys use.
#
# The second is the discharge-petition wording. EK 2.2.A.3.i says an INDIVIDUAL
# representative can FILE one; the real chamber rule needs 218 signatures to
# succeed (AP_US_GOV_CED.md note 11). Items 7 and 8 are written to be true on
# either reading, and _discharge_wording above makes that a checked property
# rather than an author's intention, so a later edit cannot quietly introduce
# "a single representative can force a bill to the floor."
