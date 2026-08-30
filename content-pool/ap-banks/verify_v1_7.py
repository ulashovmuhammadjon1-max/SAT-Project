"""Structural gate for AP U.S. Government 1.7 Relationship Between the States and National Government.

ANCHORS and GROUNDING via usgov_anchor, then usgov_check with the six data
items recomputed from their own tables.

WHY EK 1.7.A.5 GETS FIVE ITEMS OF ITS OWN
------------------------------------------
The framework does not merely define the three grant types; it RANKS them, and
the rankings are not deducible from the definitions:

    revenue sharing    almost no restrictions, LEAST USED
    block grants       minimal restrictions,   PREFERRED BY THE STATES
    categorical grants specific categories,    PREFERRED BY THE NATIONAL
                                               GOVERNMENT, MOST COMMONLY USED

The intuitive ordering is backwards -- the most restricted instrument is the
most used one -- so a bank that only tests the definitions leaves the three
claims the exam can actually ask about untested. Items 14 to 18 test them, and
the grant table in items 24 to 26 shows the same ranking as data.

THE POWERS TABLE IS CATEGORICAL AND IS RECOMPUTED ANYWAY
---------------------------------------------------------
Items 21 to 23 use a Yes/No table, so the claims below read the raw columns:
exactly three rows are yes in both columns, exactly one row is the reserved
pattern (no nationally, yes in the states), and the two columns are five and
four rather than equal. That last count is the reason this file exists -- see
the note at the bottom.
"""
import usgov_anchor as ua
import usgov_check as uc
import v1_7

ANCHORS = {
 1: "power is shared between the national and state governments",
 2: "multiple access points for political participation",
 3: "The power to coin money",
 4: "inferred from the Necessary and Proper Clause",
 5: "authorizes means not themselves listed",
 6: "belong to the states because they were not delegated",
 7: "The power to collect taxes",
 8: "None of them",
 9: "Establishing public schools, with the reserved powers",
 10: "chartering a bank is not enumerated",
 11: "judicially enforceable limits",
 12: "United States v. Lopez (1995)",
 13: "enforce constitutional limits on how a state exercises a power",
 14: "Revenue sharing",
 15: "Categorical grants",
 16: "Block grants, which carry minimal restrictions",
 17: "block grants in place of categorical grants",
 18: "a requirement by the national government of the states",
 19: "would not otherwise have chosen in order to remain eligible",
 20: "supreme law of the land",
 21: "Three of the six powers are held by both levels",
 22: "which the states hold and the national government does not",
 23: "counts powers without weighing them",
 24: "most restricted instrument grew as a share",
 25: "most commonly used form of funding and revenue sharing the least used",
 26: "rose by four percentage points while the freest instrument fell",
 27: "in fields the Tenth Amendment reserves to the states",
 28: "House apportioned by population",
 29: "pursue the same goal in Congress, in another state, or in federal court",
 30: "which the framework calls concurrent powers",
}

GROUNDING = {
 1: "EK 1.7.A.1, verbatim: federalism is 'the system of government in the United States in "
    "which power is shared between the national and state governments.'",
 2: "Federalist No. 39 (required document), 'neither a national nor a federal Constitution, "
    "but a composition of both,' quoted verbatim; EK 1.7.A.1 credits it with limiting "
    "concentration while allowing multiple access points.",
 3: "EK 1.7.A.2 (exclusive = held by only one level) against EK 1.7.A.4's concurrent "
    "examples. Coinage is denied the states by U.S. Constitution Art. I Sec. 10.",
 4: "EK 1.7.A.2, verbatim: implied powers 'are not specifically written in the Constitution "
    "but are inferred from the Necessary and Proper Clause.'",
 5: "U.S. Constitution Art. I Sec. 8, the Necessary and Proper Clause, quoted verbatim. It "
    "attaches to 'the foregoing Powers,' so it supplies means for enumerated ends.",
 6: "U.S. Constitution, Tenth Amendment, quoted verbatim; EK 1.7.A.3 names it as the source "
    "of reserved powers.",
 7: "EK 1.7.A.4, verbatim: concurrent powers include 'the power to collect taxes, the power "
    "to make and enforce laws and the power to build roads.'",
 8: "EK 1.7.A.4's three examples, all three of them, in one scenario.",
 9: "EK 1.7.A.3. Education is not delegated to the national government and is therefore "
    "reserved; the other four pairings misassign a category.",
 10: "McCulloch v. Maryland (1819), required case. CED holding: supremacy of the U.S. "
     "Constitution and federal laws over state laws; the bank power is implied under "
     "EK 1.7.A.2 because no clause enumerates it.",
 11: "United States v. Lopez (1995), required case. CED holding: Congress exceeded its "
     "power under the Commerce Clause. A boundary, not an abolition of the power.",
 12: "United States v. Lopez (1995), required case, as a SCOTUS comparison; the "
     "non-required case's facts are printed in the stem per CED p. 29.",
 13: "Shaw v. Reno (1993), required case, which the CED attaches to 1.7.A. CED holding: "
     "majority-minority districts may be challenged if race is the only factor.",
 14: "EK 1.7.A.5.i, verbatim: revenue sharing has 'almost no restrictions' and 'is the least "
     "used form of funding.' Both halves are course content.",
 15: "EK 1.7.A.5.iii, verbatim: categorical grants are 'restricted to specific categories of "
     "expenditures, [are] preferred by the national government, and [are] the most commonly "
     "used form of funding.'",
 16: "EK 1.7.A.5.ii, verbatim: block grants carry 'minimal restrictions' and are 'preferred "
     "by the states.'",
 17: "EK 1.7.A.5.ii against EK 1.7.A.5.iii, applied to a scenario; the governor's preference "
     "is the one the framework attributes to the states generally.",
 18: "EK 1.7.A.5.iv, verbatim: mandates are 'requirements by the national government of the "
     "states.' A requirement without funds is none of the three grant types.",
 19: "EK 1.7.A.5 read for its effect: conditions attached to funds direct behavior without "
     "legal compulsion, which is why the formal right to decline does not answer it.",
 20: "U.S. Constitution Art. VI, the Supremacy Clause, and McCulloch v. Maryland's holding "
     "as the CED states it. The Commerce Clause may be the statute's source, not the rule "
     "that resolves the conflict.",
 21: "Data item on a categorical table; the column counts are recomputed below.",
 22: "EK 1.7.A.3's reserved pattern -- not delegated nationally, held by the states -- "
     "identified in a table row and recomputed below.",
 23: "Data item, CED skill 3.E: an unweighted tally treats coinage and road building as "
     "equivalent, which is the flaw in the inference.",
 24: "Data item on a labelled hypothetical; the direction of each instrument's change is "
     "recomputed below.",
 25: "EK 1.7.A.5's ranking shown as data: categorical largest, revenue sharing smallest, in "
     "both years.",
 26: "EK 1.7.A.5's restriction ordering paired with the direction of change; both are "
     "recomputed below.",
 27: "EK 1.7.A.5's instruments reaching EK 1.7.A.3's reserved powers, which is the "
     "framework's own vocabulary for this critique.",
 28: "Federalist No. 39 (required document) as EK 1.7.A.1 uses it: the combination of "
     "national and state features, visible in U.S. Constitution Art. I Sec. 2 and Sec. 3.",
 29: "EK 1.7.A.1's second effect, multiple access points for political participation, which "
     "two levels of government plus courts at each supply.",
 30: "EK 1.7.A.4: concurrent powers are shared between both levels, so overlap is part of "
     "the design rather than a defect in it.",
}

NAT, STA = "Held by the national government", "Held by the state governments"
EARLY, LATE = "Share of funding, earlier year (%)", "Share of funding, later year (%)"
CAT, BLK, REV = "Categorical grants", "Block grants", "Revenue sharing"


def _yes(t, header):
    j = t["headers"].index(header)
    return [row[j] == "Yes" for row in t["rows"]]


def _both(t):
    return sum(1 for a, b in zip(_yes(t, NAT), _yes(t, STA)) if a and b)


TABLE_CHECKS = {
 21: [
  ("exactly three of the six rows are held by both levels, and the other three by one "
   "level only, which is the key's claim",
   lambda t: len(t["rows"]) == 6 and _both(t) == 3
   and sum(1 for a, b in zip(_yes(t, NAT), _yes(t, STA)) if a != b) == 3),
  ("not every row is held by both, and not every row is held nationally, so those two "
   "distractors are false",
   lambda t: _both(t) < len(t["rows"]) and not all(_yes(t, NAT))),
  ("exactly one row is held by the states alone, so 'no power held by the states "
   "alone' is false",
   lambda t: sum(1 for a, b in zip(_yes(t, NAT), _yes(t, STA)) if b and not a) == 1),
  ("the national column carries FIVE yes entries and the state column FOUR, so the "
   "states do not hold more -- the count the rationale originally got wrong",
   lambda t: sum(_yes(t, NAT)) == 5 and sum(_yes(t, STA)) == 4),
 ],
 22: [
  ("exactly one row shows EK 1.7.A.3's reserved pattern, and it is public schools",
   lambda t: [row[0] for row, a, b in zip(t["rows"], _yes(t, NAT), _yes(t, STA))
              if b and not a] == ["Establish public schools"]),
  ("each of the four distractor rows is either national-only or held by both, so none "
   "of them is a reserved power",
   lambda t: all(a for row, a, b in zip(t["rows"], _yes(t, NAT), _yes(t, STA))
                 if row[0] != "Establish public schools")),
 ],
 23: [
  ("the state column IS present, so 'omits the state governments entirely' is false",
   lambda t: STA in t["headers"]),
  ("three rows differ between the two columns, so 'no row in which the levels differ' "
   "is false",
   lambda t: sum(1 for a, b in zip(_yes(t, NAT), _yes(t, STA)) if a != b) == 3),
  ("six rows is nowhere near every power in the Constitution, so that distractor "
   "cannot stand",
   lambda t: len(t["rows"]) == 6),
 ],
 24: [
  ("categorical grants rise while block grants and revenue sharing both fall",
   lambda t: uc.cell(t, CAT, LATE) > uc.cell(t, CAT, EARLY)
   and uc.cell(t, BLK, LATE) < uc.cell(t, BLK, EARLY)
   and uc.cell(t, REV, LATE) < uc.cell(t, REV, EARLY)),
  ("two of the three fall, so 'every instrument increased' is false",
   lambda t: sum(1 for lab in uc.labels(t)
                 if uc.cell(t, lab, LATE) < uc.cell(t, lab, EARLY)) == 2),
  ("block grants never reach a majority, and revenue sharing is the smallest in the "
   "earlier year rather than the largest",
   lambda t: max(uc.cell(t, BLK, c) for c in (EARLY, LATE)) < 50
   and uc.cell(t, REV, EARLY) == min(uc.col(t, EARLY))),
  ("each year's shares sum to 100, so 'less than half of national funding' is false",
   lambda t: all(sum(uc.col(t, c)) == 100 for c in (EARLY, LATE))),
 ],
 25: [
  ("categorical grants are the largest and revenue sharing the smallest in BOTH years, "
   "which is EK 1.7.A.5's ranking shown as data",
   lambda t: all(uc.cell(t, CAT, c) == max(uc.col(t, c))
                 and uc.cell(t, REV, c) == min(uc.col(t, c)) for c in (EARLY, LATE))),
  ("mandates do not appear in the table at all, so that distractor cannot be supported "
   "by these data",
   lambda t: "Mandates" not in uc.labels(t)),
 ],
 26: [
  ("the most restricted instrument rises by exactly four points and the least "
   "restricted falls to six percent, which is the keyed pairing",
   lambda t: uc.cell(t, CAT, LATE) - uc.cell(t, CAT, EARLY) == 4
   and uc.cell(t, REV, LATE) == 6),
  ("revenue sharing does change by fewer points than categorical grants -- true of the "
   "table, and silent on discretion, which is why it is a distractor",
   lambda t: abs(uc.cell(t, REV, LATE) - uc.cell(t, REV, EARLY))
   < abs(uc.cell(t, CAT, LATE) - uc.cell(t, CAT, EARLY))),
  ("block grants do exceed revenue sharing in both years -- also true, also silent",
   lambda t: all(uc.cell(t, BLK, c) > uc.cell(t, REV, c) for c in (EARLY, LATE))),
 ],
}

ua.shape(v1_7)
ua.check(v1_7, ANCHORS, GROUNDING)
uc.check(v1_7, TABLE_CHECKS)

# WHAT THE REVIEW FOUND
# ---------------------
# No wrong key. One wrong number in a rationale, and it is the same failure mode
# as the one v1_2 shipped: item 21's `why` originally read "Both levels hold five
# of the six, so neither column is larger." The national column carries five yes
# entries and the state column four. The keyed choice was right either way -- the
# claim it makes is about how many rows are shared -- but the sentence explaining
# it asserted a false count about the table sitting directly above it.
#
# It is now stated correctly, and the last check on item 21 recomputes both
# column totals, so the pair 5 and 4 cannot drift again. The general rule this
# keeps proving: a number that appears only in prose is a number nothing is
# checking, and in a bank with no sympy that is where the errors live.
