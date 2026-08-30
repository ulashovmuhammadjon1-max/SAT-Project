"""Structural gate for AP U.S. Government 2.1 Congress: The Senate and the House.

ANCHORS and GROUNDING via usgov_anchor, then usgov_check with the six data
items recomputed from their own tables.

THE FIRST UNIT 2 MODULE, AND ONE THING CHANGES
-----------------------------------------------
Unit 2 is 25 to 36 percent of the exam, the largest unit, and it is full of
numbers a U.S. Government bank naturally wants to write with punctuation: vote
splits, term spans, chamber sizes, dates. usgov_check does not police that;
gov345_check does, for Units 3 to 5, because export_units.py runs every string
through mathfmt.convert and that converter reads BOTH a hyphen and a slash
between two digits as arithmetic. "One-third of the Senate" is safe because the
hyphen sits between letters; "a 5-4 vote" and "the 2024/2025 session" are not.

So this file carries the notation check that verify_v1_5.py introduced, widened
to catch the hyphen as well as the slash, and every Unit 2 module written after
this one should carry it too. It is four lines, it cannot false-positive on
ordinary prose, and it closes the one gap between the Unit 1-2 checker and the
Unit 3-5 one.

WHAT THE TABLES CHECK
----------------------
The chamber table (items 21 to 23) is mixed: two numeric rows and three
categorical. The claims below read whichever kind each row is, and confirm the
pairings the keys depend on -- 435 against 100, two years against six, All
against One third -- so a transposed column would fail here rather than teach a
student that the Senate has 435 members.

The turnover table (items 24 to 26) exists to make EK 2.1.A.3's "continuous
legislative body" visible as data. Its three ratios are recomputed, and so is
the fact that the larger chamber's new-member count falls and then rises, since
a distractor claims a monotonic decline.
"""
import usgov_anchor as ua
import usgov_check as uc
import v2_1

ANCHORS = {
 1: "will of the people is reflected in government by their representatives",
 2: "states equally, while the House is designed to represent the people",
 3: "same two votes as the largest state",
 4: "435 members and the Senate has 100, and the larger size is associated with more formal",
 5: "unstructured debate would consume more time than the chamber has",
 6: "smaller chamber can tolerate unlimited speech",
 7: "attributes the difference to their different membership sizes",
 8: "never stands for election as a whole",
 9: "never far from an election",
 10: "The two-party system",
 11: "but the Senate may amend them once they arrive",
 12: "Conducting oversight of the executive branch, including federal agencies",
 13: "Creating federal courts and their jurisdictions",
 14: "Oversight of the executive branch, including federal agencies in the bureaucracy",
 15: "Passing a federal budget and raising revenue",
 16: "Enacting legislation under the authority of the necessary and proper clause",
 17: "The House, because its seats are apportioned",
 18: "same vote as one representing tens of millions",
 19: "respond to different constituencies on different timetables",
 20: "more restrictive rules governing floor time",
 21: "shorter term and replaces its entire membership",
 22: "Basis of representation, since one chamber is apportioned by population",
 23: "no Senate-specific power",
 24: "at least four times as many new members",
 25: "makes it a continuous body while the larger chamber is entirely renewed",
 26: "does not indicate a high rate of re-election",
 27: "satisfy two differently constituted majorities",
 28: "one district within the state while the senator answers to the state as a whole",
 29: "Granting reprieves and pardons",
 30: "renew their membership on different schedules",
}

GROUNDING = {
 1: "EK 2.1.A.1, verbatim: republicanism, 'the democratic principle that the will of the "
    "people is reflected in government debates and decisions by their representatives,' is "
    "shown in the bicameral structure.",
 2: "EK 2.1.A.1, verbatim: 'The Senate is designed to represent states equally, while the "
    "House is designed to represent the people.'",
 3: "EK 2.1.A.1 applied: equal state representation magnifies a small state's weight in the "
    "Senate relative to its share of the House.",
 4: "EK 2.1.A.2, verbatim: 'Debate in the House, which has 435 members, is more formal than "
    "in the Senate, with 100 members.'",
 5: "EK 2.1.A.2's CAUSAL claim -- different membership sizes INFLUENCE formality -- with the "
    "mechanism being floor time scarce relative to members seeking it.",
 6: "EK 2.1.A.2 applied to the filibuster, which EK 2.2.A.3.ii names as a Senate procedure. "
    "Term length and revenue origination are real differences that do not explain this one.",
 7: "EK 2.1.A.2. The third and fourth distractors each reverse the direction of the "
    "difference the framework states.",
 8: "EK 2.1.A.3, verbatim: 'One-third of the Senate is elected every two years, creating a "
    "continuous legislative body. All House members are elected every two years.'",
 9: "EK 2.1.A.3's term-length differences as one of the two factors affecting interactions "
    "in Congress; U.S. Constitution Art. I Sec. 2 and Sec. 3 supply the terms.",
 10: "EK 2.1.A.3 names exactly two factors: the two-party system and term-length differences.",
 11: "U.S. Constitution Art. I Sec. 7, the Origination Clause, quoted verbatim including its "
     "second half, which preserves the Senate's amending power. EK 2.2.A.3.i records the "
     "rule as a House-specific procedure.",
 12: "EK 2.1.A.4.vii: 'Conducting oversight of the executive branch, including federal "
     "agencies in the bureaucracy.' The distractors are executive functions.",
 13: "EK 2.1.A.4.v: 'Creating federal courts and their jurisdictions.'",
 14: "EK 2.1.A.4.vii applied to a hearing into how a statute was implemented.",
 15: "EK 2.1.A.4.i, which groups passing a federal budget, raising revenue by laying and "
     "collecting taxes, borrowing money and coining money.",
 16: "McCulloch v. Maryland (1819), required case, which the CED attaches to 2.1.A. CED "
     "holding: supremacy of the U.S. Constitution and federal laws over state laws; the bank "
     "power rests on the necessary and proper clause, EK 2.1.A.4.vi.",
 17: "Baker v. Carr (1962), required case, which the CED attaches to 2.1.A. CED holding: "
     "redistricting did not raise political questions. Districts elect the House; senators "
     "are elected statewide.",
 18: "EK 2.1.A.1's design: the Senate represents states equally rather than people equally. "
     "Senators have been popularly elected since the Seventeenth Amendment.",
 19: "EK 2.1.A.1 and EK 2.1.A.3 together: different bases of representation plus different "
     "term lengths mean a majority in one chamber need not be a majority in the other.",
 20: "EK 2.1.A.2 operationalized: compare chamber size against rules governing floor time.",
 21: "Data item; the pairings of size, term and turnover are recomputed below.",
 22: "EK 2.1.A.1 located in a table row: a different basis of apportionment is what lets one "
     "electorate produce two different majorities.",
 23: "Data item, CED skill 3.E. The table lists a House-exclusive power and no Senate-"
     "exclusive one, so any power comparison drawn from it is an artifact of the rows chosen.",
 24: "Data item on a labelled hypothetical; the three ratios are recomputed below.",
 25: "EK 2.1.A.3's 'continuous legislative body' shown as data: a chamber renewing a fraction "
     "of its seats against one renewed entirely.",
 26: "Data item, CED skill 3.E: a raw count of new members confounds turnover with the number "
     "of seats actually contested, and in a staggered chamber most are not.",
 27: "EK 2.1.A.1's republicanism plus the Great Compromise, EK 1.5.A.1.i: agreement between "
     "two differently based chambers is a broader test than agreement within one.",
 28: "EK 2.1.A.1's two bases of representation applied to one state's delegation.",
 29: "EK 2.1.A.4's list of seven, tested by exclusion. Reprieves and pardons are an executive "
     "power under U.S. Constitution Art. II Sec. 2 and appear nowhere on it.",
 30: "EK 2.1.A.1, EK 2.1.A.2 and EK 2.1.A.3 together supply four separate differences, each "
     "stated by the framework itself.",
}

HOUSE, SEN = "House of Representatives", "Senate"
BIG, SMALL = "New members in the larger chamber", "New members in the smaller chamber"


def _row(t, label):
    for row in t["rows"]:
        if row[0] == label:
            return row
    raise KeyError(label)


def _cell(t, label, header):
    return _row(t, label)[t["headers"].index(header)]


TABLE_CHECKS = {
 21: [
  ("the larger chamber has the shorter term and renews entirely, which is the key: "
   "435 against 100, two years against six, All against One third",
   lambda t: int(_cell(t, "Number of members", HOUSE))
   > int(_cell(t, "Number of members", SEN))
   and int(_cell(t, "Length of a term in years", HOUSE))
   < int(_cell(t, "Length of a term in years", SEN))
   and _cell(t, "Share of the chamber elected every two years", HOUSE) == "All"
   and _cell(t, "Share of the chamber elected every two years", SEN) == "One third"),
  ("the two chambers do NOT replace the same share, so that distractor is false",
   lambda t: _cell(t, "Share of the chamber elected every two years", HOUSE)
   != _cell(t, "Share of the chamber elected every two years", SEN)),
  ("the bases of representation differ, so 'both represent states equally' is false",
   lambda t: _cell(t, "Basis of representation", HOUSE)
   != _cell(t, "Basis of representation", SEN)),
  ("revenue bills originate in exactly one chamber, so 'either chamber' is false",
   lambda t: (_cell(t, "Chamber in which revenue bills must originate", HOUSE),
              _cell(t, "Chamber in which revenue bills must originate", SEN))
   == ("Yes", "No")),
 ],
 22: [
  ("the basis-of-representation row is the only one naming population against state "
   "equality, which is the mechanism the key describes",
   lambda t: "Population" in _cell(t, "Basis of representation", HOUSE)
   and "Equal" in _cell(t, "Basis of representation", SEN)),
  ("the four distractor rows all differ between the chambers too -- each is a true "
   "difference that does not by itself change which coalition holds a majority",
   lambda t: sum(1 for row in t["rows"] if row[1] != row[2]) == 5),
 ],
 23: [
  ("the table names a power exclusive to the House and none exclusive to the Senate, "
   "which is exactly the selection problem the key identifies",
   lambda t: any("revenue bills" in row[0] for row in t["rows"])
   and not any(k in row[0].lower() for row in t["rows"]
               for k in ("confirm", "ratif", "treaty", "appointment"))),
  ("the Senate column and the membership row are both present, so those two "
   "distractors are false on the table's face",
   lambda t: SEN in t["headers"]
   and _cell(t, "Number of members", SEN) == "100"),
  ("five rows and five differences, so 'identical in every respect' is false",
   lambda t: len(t["rows"]) == 5 and all(row[1] != row[2] for row in t["rows"])),
 ],
 24: [
  ("in every election the larger chamber seats at least four times as many new "
   "members as the smaller one -- the ratios are 6.9, 4.4 and 8.9, so FIVE would be "
   "false at the second election",
   lambda t: all(uc.cell(t, e, BIG) >= 4 * uc.cell(t, e, SMALL)
                 for e in uc.labels(t))),
  ("the smaller chamber never exceeds the larger, so that distractor is false",
   lambda t: all(uc.cell(t, e, SMALL) < uc.cell(t, e, BIG) for e in uc.labels(t))),
  ("the larger chamber's count FALLS then RISES, so 'declined at every election' is "
   "false -- 62, 48, 71",
   lambda t: uc.col(t, BIG) == [62, 48, 71]),
  ("the two chambers are never equal, and neither is ever zero",
   lambda t: all(uc.cell(t, e, BIG) != uc.cell(t, e, SMALL) for e in uc.labels(t))
   and min(uc.col(t, BIG) + uc.col(t, SMALL)) > 0),
 ],
 25: [
  ("the smaller chamber's counts stay in single or low double digits while the larger "
   "chamber's run from 48 to 71, which is the fraction-against-whole pattern",
   lambda t: max(uc.col(t, SMALL)) < min(uc.col(t, BIG))),
  ("no column in this table reports terms, rules of debate or bill origination, so "
   "the four distractors cite facts these data do not contain",
   lambda t: [h for h in t["headers"][1:]] == [BIG, SMALL]),
 ],
 26: [
  ("the smaller chamber's counts are small in absolute terms, which is what makes the "
   "popularity inference tempting and the staggering explanation necessary",
   lambda t: max(uc.col(t, SMALL)) <= 11),
  ("both chambers appear and three elections are reported, so those two distractors "
   "are false on the table's face",
   lambda t: BIG in t["headers"] and len(t["rows"]) == 3),
  ("every cell is a whole count rather than a percentage",
   lambda t: all(c.isdigit() for row in t["rows"] for c in row[1:])),
 ],
}


ua.shape(v2_1)
ua.check(v2_1, ANCHORS, GROUNDING)
ua.notation(v2_1)
uc.check(v2_1, TABLE_CHECKS)

# WHAT THE REVIEW FOUND
# ---------------------
# No wrong key. Two things were caught while writing the grounding:
#
#   * The module's TOPIC tuple was written with the unit as an arithmetic
#     expression rather than the literal 2. usgov_check would have accepted it,
#     since it evaluates to 2, but export_units.py writes that value into every
#     question's unit field and a stray expression there is a defect waiting for
#     the next person who edits the line. It is now the literal.
#   * Item 3's distractor "The Senate has more members than the House" needed
#     the rationale to say so explicitly, because a student who confuses the two
#     chamber sizes gets several later items wrong in the same direction. The
#     rationale now states which chamber is smaller rather than leaving it.
#
# And one real defect, caught by the arithmetic rather than by reading: item 24's
# key claimed the larger chamber seated "at least five times as many" new members
# in every election. The three ratios are 62 to 9, 48 to 11 and 71 to 8 -- about
# 6.9, 4.4 and 8.9 -- so the middle election falsifies FIVE while FOUR holds
# everywhere. The key now says four, and the check recomputes all three ratios.
# The keyed choice was still the best of the five options as originally written,
# which is exactly what makes this kind of near-miss dangerous: nothing about the
# item looks wrong until the number is actually divided.
