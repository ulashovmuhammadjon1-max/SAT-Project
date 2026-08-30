"""Structural gate for AP U.S. Government 1.6 Principles of American Government.

ANCHORS and GROUNDING via usgov_anchor, then usgov_check with the six data
items recomputed from their own tables.

THIS TOPIC CARRIES TWO LEARNING OBJECTIVES, AND THE GROUNDING SAYS WHICH
------------------------------------------------------------------------
1.6 is one of the few Unit 1 topics with two objectives: 1.6.A on what
separation of powers and checks and balances ARE, and 1.6.B on what they DO.
Students collapse them, and so do question banks. Every entry in GROUNDING
below names which of the four essential-knowledge statements the key rests on,
so the module's balance across the two objectives is auditable by reading the
map rather than by re-reading thirty questions. As written it is 1.6.A.1 and
1.6.A.2 for the structural items, 1.6.B.1 for the access-point items and
1.6.B.2 for the impeachment items, with the required cases spread across both.

THE CHECKS TABLE IS CATEGORICAL AND IS STILL RECOMPUTED
-------------------------------------------------------
Items 21 to 23 hang off a table of words, not numbers, so there is no
arithmetic in the usual sense. The checks below read the raw branch columns
instead and confirm what the keys claim: that all three branches appear in both
columns, that the legislature restrains the executive on exactly two rows, and
that the appointment row is the only one whose restrained branch is the
judiciary. A single mislabelled row would otherwise break three questions with
nothing to catch it.

THE IMPEACHMENT TABLE IS A LABELLED HYPOTHETICAL, ON PURPOSE
-------------------------------------------------------------
A running count of real federal impeachments would date the module the next
time one occurs, and the figures could not be verified here. The stem says
hypothetical, and the arithmetic the items turn on -- thirteen charges, six
convictions, fewer than half -- is the same lesson EK 1.6.B.2 teaches about the
two-stage design, asserted about nobody real.
"""
import usgov_anchor as ua
import usgov_check as uc
import v1_6

ANCHORS = {
 1: "ensuring no one branch becomes too powerful",
 2: "neither the president nor the courts may do so",
 3: "refuse to confirm a presidential nominee",
 4: "three distinct institutions perform distinct functions",
 5: "out of self-interest, whatever their personal virtue",
 6: "chambers are elected differently and for different terms",
 7: "majority of citizens will act unjustly toward a minority",
 8: "still requires an executive capable of acting decisively",
 9: "unreviewable by another",
 10: "most important check on the other two branches",
 11: "Marbury v. Madison (1803), which established that courts may declare",
 12: "set aside a policy adopted by elected officials",
 13: "review by a body it does not control",
 14: "Withholding or conditioning the appropriations",
 15: "multiple access points for stakeholders and institutions",
 16: "at which an outside interest may try again",
 17: "formally charges an official with abuse of power or misconduct",
 18: "remains in office, because removal requires conviction",
 19: "one charging and the other trying",
 20: "whether officials of another branch remain in office",
 21: "both as a branch that exercises a check and as a branch that is restrained",
 22: "how often each is used",
 23: "Appointment of federal judges, which restrains the judicial branch",
 24: "both the most charges and the most convictions",
 25: "lower bar than removing one",
 26: "resigned or changed course under the threat",
 27: "accepts delay as the price",
 28: "opened an additional access point",
 29: "press the same policy on Congress, the relevant agency and the courts in turn",
 30: "or has one branch's actions gone unreviewed",
}

GROUNDING = {
 1: "EK 1.6.A.1, verbatim: the separate powers 'allow each branch to check and balance "
    "the power of the other branches, ensuring no one branch becomes too powerful.'",
 2: "EK 1.6.A.1 read for the distinction the CED keeps across two objectives: separation "
    "assigns a function to a branch; a check is power over another branch's exercise.",
 3: "EK 1.6.A.1, the same distinction from the other side. Advice and consent (U.S. "
    "Constitution Art. II Sec. 2) is one branch acting on another's decision.",
 4: "EK 1.6.A.1: the sequence contains both shapes, distinct functions and a judicial "
    "restraint on an executive action.",
 5: "Federalist No. 51 (required document), 'the necessary constitutional means and "
    "personal motives to resist encroachments,' quoted verbatim; EK 1.6.A.2.",
 6: "Federalist No. 51 (required document), 'the legislative authority necessarily "
    "predominates... divide the legislature into different branches,' quoted verbatim. "
    "The remedy is bicameralism, U.S. Constitution Art. I Sec. 1.",
 7: "Federalist No. 51 (required document), 'guard one part of the society against the "
    "injustice of the other part,' quoted verbatim. EK 1.6.A.2 names abuses BY MAJORITIES "
    "as what these provisions control.",
 8: "Federalist No. 70 (required document), 'Energy in the executive,' quoted verbatim; "
    "the CED attaches Federalist No. 70 to 1.6.A. Hamilton argues against a PLURAL "
    "executive, which is why that option is his position's opposite.",
 9: "EK 1.6.A.1. The objection is to the absence of review by another branch, which is "
    "the defining feature of a check.",
 10: "Marbury v. Madison (1803), required case. CED holding: judicial review, empowering "
     "the Court to declare an act of the legislative or executive branch unconstitutional.",
 11: "Marbury v. Madison (1803), required case, as a SCOTUS comparison; the non-required "
     "case's facts are printed in the stem per CED p. 29.",
 12: "Engel v. Vitale (1962), required case, which the CED attaches to 1.6.A. CED holding: "
     "school sponsorship of religious activities violates the Establishment Clause.",
 13: "EK 1.6.A.1 applied to U.S. Constitution Art. II Sec. 2's advice and consent: the "
     "president decides and another branch reviews.",
 14: "EK 1.6.A.1 and the appropriations power, U.S. Constitution Art. I Sec. 9. The removal "
     "distractor is false under EK 1.6.B.2, which requires a Senate conviction.",
 15: "EK 1.6.B.1, verbatim: the structure 'creates multiple access points for stakeholders "
     "and institutions to influence public policy.'",
 16: "EK 1.6.B.1 applied to a scenario: one interest using three access points in turn.",
 17: "EK 1.6.B.2, verbatim: impeachment is the process in which 'the House formally charges "
     "an official with abuse of power or misconduct.'",
 18: "EK 1.6.B.2: removal follows only 'if the official is convicted in a Senate impeachment "
     "trial.' An acquittal leaves the charge without effect on tenure.",
 19: "EK 1.6.B.2's two-chamber division, House charging and Senate trying; impeachment is a "
     "political process requiring no prior criminal conviction.",
 20: "EK 1.6.B.2 classified against EK 1.6.A.1: impeachment reaches officers of the other "
     "branches, so it is a check rather than a separation.",
 21: "Data item on a categorical table of five checks; the claim is recomputed below from "
     "the raw branch columns.",
 22: "Data item, CED skill 3.E. Formal authority counted is not effective power exercised.",
 23: "Data item read against U.S. Constitution Art. III Sec. 1, judges holding office during "
     "good behavior, which makes the judiciary the branch furthest from the electorate.",
 24: "Data item on a labelled hypothetical; the row maxima are recomputed below.",
 25: "EK 1.6.B.2's two-stage design shown arithmetically: six convictions on thirteen "
     "charges is fewer than half.",
 26: "Data item, CED skill 3.E: a count of completed proceedings cannot capture deterrence.",
 27: "EK 1.6.A.2: Federalist No. 51 explains how these provisions control potential abuses "
     "by majorities, so obstruction is the mechanism rather than a defect.",
 28: "Baker v. Carr (1962), required case, which the CED attaches to 1.6.B. CED holding: "
     "redistricting did not raise political questions, allowing federal courts to hear such "
     "cases -- an access point added, which is EK 1.6.B.1.",
 29: "EK 1.6.B.1 against EK 1.6.A.1: access points concern OUTSIDE actors; the four "
     "distractors are all institutions restraining one another.",
 30: "EK 1.6.A.1's stated purpose, that no one branch becomes too powerful, turned into a "
     "test: whether the checks are actually being exercised.",
}

EXER, REST = "Branch that exercises it", "Branch it restrains"
CHARGED, CONVICTED = "Charged by the lower chamber", "Convicted by the upper chamber"


def _cats(t, header):
    j = t["headers"].index(header)
    return [row[j] for row in t["rows"]]


TABLE_CHECKS = {
 21: [
  ("all three branches appear in BOTH branch columns, which is the key's claim",
   lambda t: {"Executive", "Legislative", "Judicial"} <= set(_cats(t, EXER))
   and {"Executive", "Legislative", "Judicial"} <= set(_cats(t, REST))),
  ("the executive exercises two of the five checks, so 'only as restrained' is false",
   lambda t: _cats(t, EXER).count("Executive") == 2),
  ("the judiciary exercises exactly one, fewer than either other branch, so 'more "
   "than either other branch' is false",
   lambda t: _cats(t, EXER).count("Judicial") == 1
   and _cats(t, EXER).count("Judicial") < _cats(t, EXER).count("Legislative")),
  ("two listed checks DO run from the legislative to the executive, the override and "
   "confirmation, so that distractor is false",
   lambda t: sum(1 for e, r in zip(_cats(t, EXER), _cats(t, REST))
                 if e == "Legislative" and r == "Executive") == 2),
  ("the five checks are not exercised by five different branches, since there are "
   "only three, so the last distractor is impossible on its face",
   lambda t: len(set(_cats(t, EXER))) < len(t["rows"])),
 ],
 22: [
  ("the judiciary IS in the table, so 'omits the judicial branch entirely' is false",
   lambda t: "Judicial" in _cats(t, EXER) or "Judicial" in _cats(t, REST)),
  ("no cell holds a number, so the 'numerical scores' distractor is false",
   lambda t: not any(c.strip().isdigit() for row in t["rows"] for c in row)),
  ("the table lists five checks, which is nowhere near every check the Constitution "
   "contains, so 'lists every check' is false and the item's own key stands",
   lambda t: len(t["rows"]) == 5),
 ],
 23: [
  ("exactly one listed check restrains the judiciary, and it is the appointment row",
   lambda t: _cats(t, REST).count("Judicial") == 1
   and t["rows"][_cats(t, REST).index("Judicial")][0] == "Appointment of federal judges"),
  ("each of the four distractors names a row whose restrained branch is elected, "
   "legislative or executive, not judicial",
   lambda t: all(r in ("Legislative", "Executive")
                 for row, r in zip(t["rows"], _cats(t, REST))
                 if row[0] != "Appointment of federal judges")),
 ],
 24: [
  ("the judge row holds the maximum of both columns, which is the key's claim",
   lambda t: uc.cell(t, "Federal judge", CHARGED) == max(uc.col(t, CHARGED))
   and uc.cell(t, "Federal judge", CONVICTED) == max(uc.col(t, CONVICTED))),
  ("no row has convictions equal to charges, so 'every official convicted' and "
   "'equal in every category' are both false",
   lambda t: all(uc.cell(t, lab, CONVICTED) < uc.cell(t, lab, CHARGED)
                 for lab in uc.labels(t))),
  ("two rows do show convictions, so 'no category shows a conviction' is false",
   lambda t: sum(1 for lab in uc.labels(t) if uc.cell(t, lab, CONVICTED) > 0) == 2),
  ("chief executives were convicted zero times against the cabinet's one, so that "
   "distractor is false",
   lambda t: uc.cell(t, "Chief executive", CONVICTED)
   < uc.cell(t, "Cabinet secretary", CONVICTED)),
 ],
 25: [
  ("thirteen charged, six convicted -- fewer than half, which is the keyed claim",
   lambda t: sum(uc.col(t, CHARGED)) == 13 and sum(uc.col(t, CONVICTED)) == 6
   and sum(uc.col(t, CONVICTED)) * 2 < sum(uc.col(t, CHARGED))),
  ("the upper chamber does not convict whenever the lower charges -- two categories "
   "convicted nobody at all",
   lambda t: sum(1 for lab in uc.labels(t) if uc.cell(t, lab, CONVICTED) == 0) == 2),
  ("four types of official appear, so 'only the chief executive can be charged' is "
   "false on the table's face",
   lambda t: len(uc.labels(t)) == 4),
 ],
 26: [
  ("both chambers are named in the headers, so 'omits the upper chamber' is false",
   lambda t: any("upper chamber" in h for h in t["headers"])
   and any("lower chamber" in h for h in t["headers"])),
  ("every cell is a whole count rather than a percentage, so the 'percentages do not "
   "sum to one hundred' distractor describes a table that is not here",
   lambda t: all(c.isdigit() for row in t["rows"] for c in row[1:])
   and sum(uc.col(t, CHARGED)) != 100),
  ("four types of official appear, so 'officials of only one type' is false",
   lambda t: len(uc.labels(t)) == 4),
 ],
}

ua.shape(v1_6)
ua.check(v1_6, ANCHORS, GROUNDING)
uc.check(v1_6, TABLE_CHECKS)

# WHAT THE REVIEW FOUND
# ---------------------
# No wrong key, and no item in this module says an official was "impeached and
# removed" as though those were one act. That was checked deliberately rather
# than incidentally: EK 1.6.B.2 defines impeachment as the House's CHARGE and
# removal as conviction in a Senate trial, and the collapsed phrasing is the
# single most common error on this topic. Items 17 to 20 and the hypothetical
# table in 24 to 26 all keep the two stages apart, and item 18's key exists
# precisely to make a student who has collapsed them get the question wrong.
