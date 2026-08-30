"""Structural gate for AP U.S. Government 2.14 Holding the Bureaucracy Accountable.

ANCHORS, GROUNDING, shape and notation via usgov_anchor, then usgov_check with
NINE data items recomputed from three tables. Nine because this topic's
suggested CED skill (p. 74) is 3.C -- explain patterns and trends in data TO
DRAW CONCLUSIONS -- which needs more than a reading item per table.

TWO OBJECTIVES POINTED AT THE SAME OFFICIALS
----------------------------------------------
LO 2.14.A gives Congress oversight so that ITS legislation is implemented as
intended. LO 2.14.B gives the president the job of aligning the same agencies
with the ADMINISTRATION's goals. They are not two subjects that happen to share
a topic; they are two principals directing one set of officials, which is why
items 18 and 30 are about the collision. The GROUNDING map is where the balance
between the two halves is auditable.

THE TWO HALF-READ SENTENCES THIS FILE GUARDS
----------------------------------------------
EK 2.14.A.1.iii defines the power of the purse as APPROPRIATING OR WITHHOLDING
funds. Withholding is the half that makes it a check rather than routine
budgeting, and _both_halves asserts the keyed definition keeps it.

EK 2.14.B.2 says compliance monitoring ensures funds are used properly AND can
pose a challenge to policy implementation. Two sentences, benefit and cost. A
module that reports only the first teaches that monitoring is free; only the
second, that it is waste. _both_halves asserts both appear, and the monitoring
table is built with two columns so the trade-off is visible as data rather than
asserted in prose: accounting rises 71, 88, 96, 98 while months rise 4, 7, 13,
22 -- gains shrinking, costs growing.

THE CONFOUND IN THE OVERSIGHT TABLE IS THE SAME ONE AS TOPIC 2.5's
--------------------------------------------------------------------
Unified control occupies Years 1 and 2, divided control Years 3 and 4, so party
control and time in office cannot be separated. Item 23 is the item that says
so, and the check asserts the row order, exactly as verify_v2_5.py does. Two
modules in this unit now carry that confound deliberately with an item pointing
at it; a third that carried it silently would be a defect.
"""
import usgov_anchor as ua
import usgov_check as uc
import v2_14

ANCHORS = {
 1: "legislation is implemented as intended",
 2: "Review, monitoring, and supervision of bureaucratic agencies",
 3: "Investigation and committee hearings of bureaucratic activity",
 4: "by appropriating or withholding funds",
 5: "Withholding funds, since the possibility of losing an appropriation",
 6: "exercised through the threat of withholding funds",
 7: "curtail the use of presidential power",
 8: "the instrument through which a president's priorities become action",
 9: "defend the legislature's institutional stake",
 10: "Presidential ideology, authority, and influence",
 11: "affect how agencies carry out the goals of the administration",
 12: "Authority, which includes appointment and the direction of subordinate officials",
 13: "That funds are being used properly and regulations are being followed",
 14: "That it can pose a challenge to policy implementation",
 15: "consume time and staff that would otherwise go to delivering the program",
 16: "both ensures proper use of funds and can challenge implementation",
 17: "Committee hearings, with Congress; compliance monitoring, with the executive branch",
 18: "answers to two principals at once",
 19: "after hearings identified problems, and the changes persisted",
 20: "shifted toward the administration's stated priorities after its appointees took office",
 21: "which suggests oversight intensifies when the opposing party holds a chamber",
 22: "check of executive authorization, curtailing the use of presidential power",
 23: "party control and time in office cannot be separated",
 24: "the gain in accountability shrinks while the delay keeps growing",
 25: "ensures funds are used properly and can pose a challenge to policy implementation",
 26: "two additional points of accounting at the cost of nine additional months",
 27: "the more closely regulatory output matches its priorities",
 28: "exercised through appointments",
 29: "the priority may drive the appointments rather than the reverse",
 30: "toward partly different ends, so accountability runs in two directions",
}

GROUNDING = {
 1: "EK 2.14.A.1, verbatim: oversight exists 'to ensure that legislation is implemented as "
    "intended' -- Congress checking its own statutes, which is what distinguishes it from "
    "presidential direction.",
 2: "EK 2.14.A.1.i: 'Review, monitoring, and supervision of bureaucratic agencies.'",
 3: "EK 2.14.A.1.ii: 'Investigation and committee hearings of bureaucratic activity' -- the "
    "same event EK 2.12.A.1.iii records from the agency's side as testifying.",
 4: "EK 2.14.A.1.iii's own parenthesis: the power of the purse is 'the ability of Congress to "
    "check the bureaucracy by appropriating or withholding funds.'",
 5: "EK 2.14.A.1.iii's second verb. Withholding is what converts an annual appropriation into "
    "leverage; appropriating alone is what any legislature does.",
 6: "EK 2.14.A.1.iii applied: the change was produced by the prospect of a reduction rather "
    "than by a hearing or a rule.",
 7: "EK 2.14.A.2, verbatim: 'As a means to curtail the use of presidential power, "
    "congressional oversight serves as a check of executive authorization.'",
 8: "EK 2.14.A.2 read through EK 2.14.B.1: agencies are the vehicle for the administration's "
    "goals, so limiting their authorization reaches the president indirectly.",
 9: "Federalist No. 51 (required document), 'Ambition must be made to counteract ambition,' "
    "quoted verbatim; the CED attaches Federalist No. 51 to 2.14.A.",
 10: "EK 2.14.B.1, verbatim: 'Presidential ideology, authority, and influence affect how "
     "executive branch agencies carry out the goals of the administration.'",
 11: "EK 2.14.B.1 applied, with EK 2.13.A.1's delegated discretion as the room in which a "
     "change of administration can change an answer the statute left open.",
 12: "EK 2.14.B.1's three levers distinguished: authority is the formal one, and EK 2.4.A.2.iii "
     "classifies persuasion and influence as informal.",
 13: "EK 2.14.B.2, verbatim first sentence: compliance monitoring 'ensures that funds are "
     "being used properly and regulations are being followed.'",
 14: "EK 2.14.B.2, verbatim second sentence: 'Compliance monitoring can pose a challenge to "
     "policy implementation.' The statement has two halves and this is the second.",
 15: "EK 2.14.B.2's second sentence with its mechanism: verification is itself work, done by "
     "the staff and time that would otherwise deliver the program.",
 16: "EK 2.14.B.2's two sentences held together: the disagreement is about where to set a "
     "level, not about which effect is real.",
 17: "EK 2.14.A.1.ii (congressional) against EK 2.14.B.2 (executive) -- the two objectives "
     "assign these instruments to different branches.",
 18: "LO 2.14.A against LO 2.14.B: two branches directing the same agencies at once, which is "
     "why the CED puts them in a single topic.",
 19: "EK 2.14.A.1's stated purpose operationalized: effectiveness is changed implementation, "
     "not a count of hearings.",
 20: "EK 2.14.B.1 operationalized: the claim is about how agencies CARRY OUT goals, so the "
     "evidence must be a change in output rather than in inputs.",
 21: "Data item on a labelled hypothetical; both series are compared across control "
     "conditions below.",
 22: "EK 2.14.A.2 seen as data: oversight rising when the opposing party holds a chamber is "
     "the check on presidential power operating.",
 23: "Data item, CED skill 3.E: unified control occupies Years 1 and 2 and divided control "
     "Years 3 and 4, so control and tenure are perfectly confounded -- the same confound "
     "verify_v2_5.py records, and item 23 is the item that names it.",
 24: "Data item on a labelled hypothetical; the diminishing gains and growing delays are "
     "recomputed below.",
 25: "EK 2.14.B.2's BOTH sentences seen as two columns; a one-column table could not "
     "illustrate the statement.",
 26: "EK 2.14.B.2's trade-off at a specific margin; the step from extensive to very extensive "
     "is recomputed below.",
 27: "Data item on a labelled hypothetical; the monotonic relationship is recomputed below.",
 28: "EK 2.14.B.1's AUTHORITY specifically: appointments are how authority reaches an "
     "agency's decisions.",
 29: "Data item, CED skill 3.E: reverse causation is the live alternative, since an "
     "administration invests appointments where it already has priorities.",
 30: "LO 2.14.A and LO 2.14.B together: accountability running in two directions at once.",
}

CONTROL, HEARINGS, CUTS = ("Party control", "Oversight hearings held",
                           "Agencies whose funds were reduced")
YEARS = ["Year 1", "Year 2", "Year 3", "Year 4"]
ACCT, MONTHS = ("Funds fully accounted for (%)", "Months from award to first service")
LEVELS = ["Minimal", "Moderate", "Extensive", "Very extensive"]
NAGY, MATCH = ("Number of agencies",
               "Regulatory output matching administration priorities (%)")
BANDS = ["Under 25", "25 to 49", "50 to 74", "75 and above"]


def _ctrl(t, year):
    j = t["headers"].index(CONTROL)
    for row in t["rows"]:
        if row[0] == year:
            return row[j]
    raise KeyError(year)


TABLE_CHECKS = {
 21: [
  ("both hearings and funding cuts roughly triple between the unified and divided "
   "years, and every divided year exceeds every unified year on both measures",
   lambda t: min(uc.cell(t, y, HEARINGS) for y in YEARS if _ctrl(t, y) == "Divided")
   > max(uc.cell(t, y, HEARINGS) for y in YEARS if _ctrl(t, y) == "Unified")
   and min(uc.cell(t, y, CUTS) for y in YEARS if _ctrl(t, y) == "Divided")
   > max(uc.cell(t, y, CUTS) for y in YEARS if _ctrl(t, y) == "Unified")),
  ("neither series falls under divided control, so the second and third distractors "
   "are both false",
   lambda t: uc.cell(t, "Year 4", HEARINGS) > uc.cell(t, "Year 1", HEARINGS)
   and uc.cell(t, "Year 4", CUTS) > uc.cell(t, "Year 1", CUTS)),
  ("the four years differ widely on both measures, so 'roughly equal' is false",
   lambda t: max(uc.col(t, HEARINGS)) > 2 * min(uc.col(t, HEARINGS))),
  ("Year 1 holds the LOWEST figures, so 'highest in the first year' is false",
   lambda t: uc.cell(t, "Year 1", HEARINGS) == min(uc.col(t, HEARINGS))
   and uc.cell(t, "Year 1", CUTS) == min(uc.col(t, CUTS))),
 ],
 22: [
  ("the table pairs PARTY CONTROL with oversight activity, which is what makes it a "
   "test of EK 2.14.A.2 rather than of compliance monitoring or the merit system",
   lambda t: CONTROL in t["headers"] and HEARINGS in t["headers"]),
  ("no column reports funds accounted for, appointments or hiring method",
   lambda t: not any(k in h.lower() for h in t["headers"]
                     for k in ("accounted", "appoint", "merit", "examination"))),
 ],
 23: [
  ("the confound is exactly as the key describes: the two unified years are the FIRST "
   "two and the two divided years the LAST two",
   lambda t: [_ctrl(t, y) for y in YEARS] == ["Unified", "Unified", "Divided", "Divided"]),
  ("both series also rise monotonically, which is why time in office explains the "
   "table as well as party control does",
   lambda t: uc.col(t, HEARINGS) == sorted(uc.col(t, HEARINGS))
   and uc.col(t, CUTS) == sorted(uc.col(t, CUTS))),
  ("both control conditions and four years are present, and the cells are counts",
   lambda t: len({_ctrl(t, y) for y in YEARS}) == 2 and len(t["rows"]) == 4),
 ],
 24: [
  ("accounting rises by 17, then 8, then 2 -- diminishing -- while months rise by 3, "
   "then 6, then 9 -- growing. That divergence is the key's whole claim",
   lambda t: [uc.cell(t, b, ACCT) - uc.cell(t, a, ACCT)
              for a, b in zip(LEVELS, LEVELS[1:])] == [17, 8, 2]
   and [uc.cell(t, b, MONTHS) - uc.cell(t, a, MONTHS)
        for a, b in zip(LEVELS, LEVELS[1:])] == [3, 6, 9]),
  ("delay rises rather than falls, so 'both accountability and speed improve' is false",
   lambda t: uc.col(t, MONTHS) == sorted(uc.col(t, MONTHS))),
  ("accounting rises rather than falls, and never reaches 100",
   lambda t: uc.col(t, ACCT) == sorted(uc.col(t, ACCT)) and max(uc.col(t, ACCT)) == 98),
 ],
 25: [
  ("the table has BOTH of EK 2.14.B.2's effects as columns -- accountability and time "
   "to first service -- which is what a one-column table could not show",
   lambda t: [h for h in t["headers"][1:]] == [ACCT, MONTHS]),
  ("the two columns move in the same direction, which is the trade-off rather than a "
   "correlation to celebrate",
   lambda t: uc.col(t, ACCT) == sorted(uc.col(t, ACCT))
   and uc.col(t, MONTHS) == sorted(uc.col(t, MONTHS))),
 ],
 26: [
  ("the final step buys 2 points of accounting for 9 months of delay",
   lambda t: uc.cell(t, LEVELS[3], ACCT) - uc.cell(t, LEVELS[2], ACCT) == 2
   and uc.cell(t, LEVELS[3], MONTHS) - uc.cell(t, LEVELS[2], MONTHS) == 9),
  ("the FIRST step is the cheapest in delay, not the costliest, so that distractor is "
   "reversed",
   lambda t: uc.cell(t, LEVELS[1], MONTHS) - uc.cell(t, LEVELS[0], MONTHS)
   == min(uc.cell(t, b, MONTHS) - uc.cell(t, a, MONTHS)
          for a, b in zip(LEVELS, LEVELS[1:]))),
  ("the accounting gains are unequal, so 'every increase produces an equal gain' is "
   "false, and the highest level is not best on both measures",
   lambda t: len({uc.cell(t, b, ACCT) - uc.cell(t, a, ACCT)
                  for a, b in zip(LEVELS, LEVELS[1:])}) == 3),
 ],
 27: [
  ("matching rises monotonically with the appointment share, 38 to 81",
   lambda t: [uc.cell(t, b, MATCH) for b in BANDS] == sorted(
       [uc.cell(t, b, MATCH) for b in BANDS])
   and uc.cell(t, BANDS[0], MATCH) == 38 and uc.cell(t, BANDS[3], MATCH) == 81),
  ("the largest group is the eleven agencies in the third band, not the top band, so "
   "'most agencies had three quarters or more filled' is false",
   lambda t: uc.cell(t, BANDS[2], NAGY) == max(uc.col(t, NAGY))
   and uc.cell(t, BANDS[3], NAGY) < uc.cell(t, BANDS[2], NAGY)),
  ("no band exceeds 90 percent matching, so that distractor is false",
   lambda t: max(uc.col(t, MATCH)) < 90),
 ],
 28: [
  ("the independent variable is the share of senior positions FILLED BY THE "
   "ADMINISTRATION, which is EK 2.14.B.1's authority reaching an agency",
   lambda t: "senior positions filled by the administration" in t["headers"][0]),
  ("no column reports hearings, appropriations or compliance monitoring, so those "
   "distractors cite data the table does not carry",
   lambda t: not any(k in h.lower() for h in t["headers"]
                     for k in ("hearing", "appropriat", "monitoring", "triangle"))),
 ],
 29: [
  ("all four bands, the agency counts and both percentages are present, so three "
   "distractors are false on the table's face",
   lambda t: len(t["rows"]) == 4 and NAGY in t["headers"] and MATCH in t["headers"]),
  ("the relationship is real and monotonic, so 'shows no relationship' is false -- the "
   "problem is its DIRECTION, not its existence",
   lambda t: uc.cell(t, BANDS[3], MATCH) > uc.cell(t, BANDS[0], MATCH)),
  ("the agency counts sum to 33, so this is a study of many agencies rather than one",
   lambda t: sum(uc.col(t, NAGY)) == 33),
 ],
}


def _both_halves(module):
    """Two CED sentences with two halves each must keep both halves."""
    bad = []
    purse = module.QUESTIONS[3]["choices"][module.QUESTIONS[3]["ans"]].lower()
    for verb in ("appropriating", "withholding"):
        if verb not in purse:
            bad.append(f"q4: the power-of-the-purse key omits EK 2.14.A.1.iii's verb {verb!r}; "
                       "withholding is the half that makes it a check")
    blob = " ".join(it["q"] + " " + it["why"] + " " + " ".join(it["choices"])
                    for it in module.QUESTIONS).lower()
    for half in ("funds are being used properly", "challenge to policy implementation"):
        if half not in blob:
            bad.append(f"EK 2.14.B.2's half {half!r} appears nowhere in the module; the "
                       "statement has a benefit and a cost and both are examinable")
    if bad:
        print(f"FAIL {module.__name__} both halves")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} both halves: the power of the purse keeps both appropriating "
          "and withholding, and compliance monitoring keeps both its assurance and its cost")


ua.shape(v2_14)
ua.check(v2_14, ANCHORS, GROUNDING)
ua.notation(v2_14)
_both_halves(v2_14)
uc.check(v2_14, TABLE_CHECKS)

# WHAT THE REVIEW FOUND
# ---------------------
# No wrong key. The design decision worth recording is the monitoring table.
#
# EK 2.14.B.2 is two sentences: compliance monitoring ENSURES funds are used
# properly, and it CAN POSE A CHALLENGE to implementation. A table with one
# column can only illustrate one of them, and whichever one it showed would
# teach half the statement -- monitoring as free, or monitoring as waste.
#
# So the table carries two columns that move together, and the numbers are
# chosen so the trade-off has a shape rather than merely a direction: accounting
# gains shrink (17, 8, 2) while delays grow (3, 6, 9). That makes item 26
# possible, which asks what the last step actually buys -- two points of
# accounting for nine months -- and turns a statement a student could recite
# into a decision they have to reason about. The checks recompute both
# difference series, so an edit that flattened either one would break the item
# rather than quietly making it a matter of opinion.
