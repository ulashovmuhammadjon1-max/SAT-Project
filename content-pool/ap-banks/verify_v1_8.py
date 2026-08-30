"""Structural gate for AP U.S. Government 1.8 Constitutional Interpretations of Federalism.

ANCHORS and GROUNDING via usgov_anchor, then usgov_check with the six data
items recomputed from their own tables.

WHAT THE GROUNDING MAP IS DOING IN THIS PARTICULAR TOPIC
---------------------------------------------------------
1.8 is the SCOTUS topic of Unit 1 -- its suggested skill is 2.A, describing the
facts, issue, holding and reasoning of REQUIRED cases -- so most of the keys
here are holdings. A holding stated wrongly is the worst defect this bank can
ship: a student repeats it in an essay and is marked wrong for something the
bank taught them. So every case entry below names the case AND states the
holding in the CED's own words, which AP_US_GOV_CED.md reproduces from p. 30.
Checking this module means reading those entries against that table, and the
entries exist so that check is a five-minute job rather than a re-derivation.

Only five cases appear, because those are the five the CED's cross-reference
table attaches to 1.8.A: McCulloch, Engel, Gideon, Yoder, Lopez. No item names
a case the framework does not attach here, and no item states a holding in any
words but the CED's.

THE DIRECTION TRAP, CHECKED AS DATA
------------------------------------
Four of those five cases expand national power and exactly one, Lopez, limits
it. That one-in-five split is the topic's whole point -- interpretation moves
the boundary in both directions -- and items 21, 22 and 10 all turn on it. It
is therefore recomputed from the table's effect column rather than trusted from
the prose, and the check also confirms the limiting case is the MOST RECENT
row, since a distractor claims it is the oldest.
"""
import usgov_anchor as ua
import usgov_check as uc
import v1_8

ANCHORS = {
 1: "interpretations can influence the extent of those protections",
 2: "changed over time as a result of Supreme Court interpretations",
 3: "extends its protection to any person",
 4: "binding on state criminal proceedings",
 5: "may not adopt a policy the national Constitution forbids",
 6: "compulsory school attendance laws are state laws",
 7: "enforced against a state or its instrumentalities",
 8: "which can influence the extent of the power",
 9: "judicially enforced outer limit",
 10: "held that Congress exceeded its Commerce Clause power",
 11: "when specific actions exceed this constitutional power",
 12: "McCulloch read national power broadly and upheld it",
 13: "substantially affects interstate commerce",
 14: "McCulloch v. Maryland (1819), which established the supremacy",
 15: "Lopez with the Commerce Clause statement",
 16: "upheld a national bank that no clause enumerates",
 17: "invalidated several federal statutes as exceeding",
 18: "enforcer of individual protections against state action",
 19: "falls within one of the powers the Constitution grants",
 20: "grant powers in general terms",
 21: "Four of the five cases expanded national power and one limited it",
 22: "the only case listed whose effect on national power was to limit it",
 23: "not a sample of the Court's decisions",
 24: "national share nearly doubled",
 25: "measure fiscal activity, not constitutional authority",
 26: "upheld national statutes regulating subjects previously left to the states",
 27: "settles what happens when a valid national law conflicts",
 28: "only if it is does the Supremacy Clause resolve the conflict",
 29: "how often and in which direction did the Court's holdings move the boundary",
 30: "the same text can support different boundaries at different times",
}

GROUNDING = {
 1: "EK 1.8.A.1, verbatim: the Fourteenth Amendment's Due Process and Equal Protection "
    "Clauses give the national government power to enforce protections for any person "
    "against the states, 'but Supreme Court interpretations can influence the extent.'",
 2: "LO 1.8.A itself: explain how the balance of power has changed OVER TIME based on "
    "interpretations of the Supreme Court -- change, not the original allocation.",
 3: "U.S. Constitution, Fourteenth Amendment Section 1, quoted verbatim. It restrains the "
    "STATES and protects 'any person,' which is what EK 1.8.A.1 rests on.",
 4: "Gideon v. Wainwright (1963), required case. CED holding: 'The Sixth Amendment's right "
    "to an attorney extends procedural due process protections to felony defendants in "
    "state courts.'",
 5: "Engel v. Vitale (1962), required case. CED holding: 'School sponsorship of religious "
    "activities violates the Establishment Clause of the First Amendment.'",
 6: "Wisconsin v. Yoder (1972), required case. CED holding: 'Compelling Amish students to "
    "attend school past the eighth grade violates the Free Exercise Clause of the First "
    "Amendment.' The compelling law is a STATE law.",
 7: "Engel, Gideon and Yoder together, all three required cases, sharing EK 1.8.A.1's "
    "structure: a national guarantee enforced against state action.",
 8: "U.S. Constitution Art. I Sec. 8, the Commerce Clause, quoted verbatim, with "
    "EK 1.8.A.2's qualification that interpretation sets the extent.",
 9: "United States v. Lopez (1995), required case. CED holding: 'Congress exceeded its "
    "power under the Commerce Clause when it made possession of a gun in a school zone a "
    "federal crime.'",
 10: "Lopez as the counterexample to a one-directional account of judicial interpretation; "
     "it is the only one of the five 1.8.A cases that contracts national power.",
 11: "U.S. Constitution Art. VI, the Supremacy Clause, quoted verbatim, with EK 1.8.A.4's "
     "qualification. 'In Pursuance thereof' is why an ultra vires federal act is not supreme.",
 12: "McCulloch v. Maryland (1819) against United States v. Lopez (1995), both required "
     "cases, CED holdings as stated: supremacy of federal law over state law after "
     "upholding an implied power, against Congress exceeding its Commerce Clause power.",
 13: "United States v. Lopez (1995), required case, as a SCOTUS comparison; the "
     "non-required case's facts are printed in the stem per CED p. 29.",
 14: "McCulloch v. Maryland (1819), required case, as a SCOTUS comparison. CED holding: "
     "'established supremacy of the U.S. Constitution and federal laws over state laws.'",
 15: "Each required case matched to the essential-knowledge statement its holding turns on; "
     "Lopez to EK 1.8.A.2, the Commerce Clause statement.",
 16: "McCulloch v. Maryland (1819), required case, illustrating EK 1.8.A.3: no clause "
     "enumerates a power to charter a bank, so the authority is Necessary and Proper.",
 17: "EK 1.8.A as a whole: the balance is tied to judicial interpretation, so evidence of a "
     "shift toward the states must be holdings limiting national power.",
 18: "EK 1.8.A.1. Before the Fourteenth Amendment the Bill of Rights was read as restraining "
     "the national government; after it, national enforcement runs against the states.",
 19: "U.S. Constitution, Tenth Amendment: powers 'not delegated' are reserved, so the "
     "delegated-powers question is logically first. This is why Lopez turns on the Commerce "
     "Clause rather than on the Tenth Amendment.",
 20: "EK 1.8.A.1 through EK 1.8.A.4 share one form -- a general grant plus an interpretive "
     "qualification -- which is what makes change over time possible without amendment.",
 21: "Data item; the effect column's four-to-one split and the date of the limiting case are "
     "both recomputed below.",
 22: "Data item; the Lopez row is the only one marked Limited, recomputed below.",
 23: "Data item, CED skill 3.E: a curated list of required cases carries no information "
     "about the Court's base rates.",
 24: "Data item on a labelled hypothetical; every row's direction of change is recomputed "
     "below.",
 25: "Data item, CED skill 3.E, read against LO 1.8.A: the objective locates change in "
     "judicial interpretation, and spending shares are not constitutional authority.",
 26: "EK 1.8.A.2 and EK 1.8.A.3: the link between a fiscal pattern and the federal balance "
     "has to run through decisions upholding national regulation in state fields.",
 27: "EK 1.8.A.3 (a grant of power) against EK 1.8.A.4 (precedence in a conflict). McCulloch "
     "applies both, in that order.",
 28: "U.S. Constitution Art. VI's 'in Pursuance thereof' and EK 1.8.A.4's qualification: a "
     "statute outside a granted power has no precedence to assert.",
 29: "LO 1.8.A operationalized -- direction and extent of movement in holdings, not counts "
     "of opinions or justices.",
 30: "EK 1.8.A.1 through EK 1.8.A.4, all four of which state that interpretation influences "
     "how far a granted power extends.",
}

EFFECT, PROV = "Effect on national power", "Provision at issue"
LOPEZ = "United States v. Lopez (1995)"
NATL, STATE, LOCAL = "National", "State", "Local"
P1, P2, P3 = "Period 1 (%)", "Period 2 (%)", "Period 3 (%)"


def _cats(t, header):
    j = t["headers"].index(header)
    return [row[j] for row in t["rows"]]


TABLE_CHECKS = {
 21: [
  ("the effect column reads Expanded four times and Limited once, which is the key",
   lambda t: _cats(t, EFFECT).count("Expanded") == 4
   and _cats(t, EFFECT).count("Limited") == 1),
  ("the one limiting case is the LAST row, the most recent, not the oldest -- which is "
   "what makes that distractor tempting and false",
   lambda t: _cats(t, EFFECT).index("Limited") == len(t["rows"]) - 1
   and t["rows"][-1][0] == LOPEZ),
  ("three of the five rows name a Bill of Rights provision, so 'no case involved one' "
   "is false",
   lambda t: sum(1 for p in _cats(t, PROV) if "Amendment" in p) == 3),
  ("only one row names the Commerce Clause, so 'every case turned on it' is false",
   lambda t: sum(1 for p in _cats(t, PROV) if "Commerce Clause" in p) == 1),
 ],
 22: [
  ("exactly one row is marked Limited and it is the Lopez row",
   lambda t: [row[0] for row, e in zip(t["rows"], _cats(t, EFFECT))
              if e == "Limited"] == [LOPEZ]),
  ("all four distractor rows are marked Expanded, so each is a true statement about "
   "state involvement in a case the NATIONAL rule won",
   lambda t: all(e == "Expanded" for row, e in zip(t["rows"], _cats(t, EFFECT))
                 if row[0] != LOPEZ)),
 ],
 23: [
  ("the table does contain an effect column and a provision column, so those two "
   "distractors are false on its face",
   lambda t: EFFECT in t["headers"] and PROV in t["headers"]),
  ("the cases span 1819 to 1995, so 'only the twentieth century' is false",
   lambda t: "1819" in t["rows"][0][0] and "1995" in t["rows"][-1][0]),
  ("five rows is the whole table, which is what makes the base-rate inference "
   "impossible and the key correct",
   lambda t: len(t["rows"]) == 5),
 ],
 24: [
  ("the national share nearly doubles while both other levels decline in every period",
   lambda t: uc.cell(t, NATL, P3) > 1.9 * uc.cell(t, NATL, P1)
   and uc.cell(t, STATE, P1) > uc.cell(t, STATE, P2) > uc.cell(t, STATE, P3)
   and uc.cell(t, LOCAL, P1) > uc.cell(t, LOCAL, P2) > uc.cell(t, LOCAL, P3)),
  ("two of the three levels fall, so 'all three increased' is false",
   lambda t: sum(1 for lab in uc.labels(t)
                 if uc.cell(t, lab, P3) < uc.cell(t, lab, P1)) == 2),
  ("local leads in Period 1 only, so 'largest share in every period' is false",
   lambda t: uc.cell(t, LOCAL, P1) == max(uc.col(t, P1))
   and uc.cell(t, LOCAL, P2) < max(uc.col(t, P2))),
  ("the local share falls 24 points against the state's 4, so 'state fell more "
   "sharply' is false",
   lambda t: (uc.cell(t, LOCAL, P1) - uc.cell(t, LOCAL, P3)) == 24
   and (uc.cell(t, STATE, P1) - uc.cell(t, STATE, P3)) == 4),
  ("the national share is 30 in Period 1, below half, so 'exceeded half in every "
   "period' is false",
   lambda t: uc.cell(t, NATL, P1) < 50),
  ("each period sums to 100, so the shares are a complete distribution",
   lambda t: all(sum(uc.col(t, c)) == 100 for c in (P1, P2, P3))),
 ],
 25: [
  ("the national row IS present, so 'omits the national government' is false",
   lambda t: NATL in uc.labels(t)),
  ("three periods are reported, so 'covers only one period' is false",
   lambda t: len([h for h in t["headers"] if h.startswith("Period")]) == 3),
  ("every column sums to 100, so these are shares rather than dollar amounts",
   lambda t: all(sum(uc.col(t, c)) == 100 for c in (P1, P2, P3))),
  ("every row changes across the three periods, so 'shows no change' is false",
   lambda t: all(len({uc.cell(t, lab, c) for c in (P1, P2, P3)}) > 1
                 for lab in uc.labels(t))),
 ],
 26: [
  ("the shift to be explained is real and large: the national share rises 28 points "
   "while local falls 24",
   lambda t: uc.cell(t, NATL, P3) - uc.cell(t, NATL, P1) == 28
   and uc.cell(t, LOCAL, P1) - uc.cell(t, LOCAL, P3) == 24),
  ("nothing in the table reports population, employment or total spending, so the "
   "three distractors that cite them are outside these data entirely",
   lambda t: not any(k in h.lower() for h in t["headers"]
                     for k in ("population", "employ", "total"))),
 ],
}

ua.shape(v1_8)
ua.check(v1_8, ANCHORS, GROUNDING)
uc.check(v1_8, TABLE_CHECKS)

# WHAT THE REVIEW FOUND
# ---------------------
# No wrong key and no misstated holding. Every one of the five required cases in
# this module states its holding in the CED's own words, and each was checked
# against AP_US_GOV_CED.md's reproduction of the required-case table rather than
# from memory. Two things that check caught before they became defects:
#
#   * No case outside the CED's 1.8.A list appears. Marbury and Baker v. Carr
#     both belong to Unit 1 and would have read naturally in an interpretation
#     topic, but the framework attaches them to 1.6, not here.
#   * The Yoder item names the STATE as the government whose authority was
#     limited. Compulsory attendance is a state law, and an item that let a
#     student infer a federal statute was struck down would have taught the
#     wrong lesson about which level the case constrains.
