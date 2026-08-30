"""Structural gate for AP U.S. Government 1.5 Ratification of the U.S. Constitution.

ANCHORS and GROUNDING via usgov_anchor, then usgov_check with the arithmetic of
the six data items recomputed from their own tables.

THE TWO TABLES ARE OF DIFFERENT KINDS AND ARE CHECKED DIFFERENTLY
------------------------------------------------------------------
Items 21 to 23 use figures that are not data at all in the ordinary sense: the
House seat counts are the numbers written into Article I Section 2 of the
Constitution, and the Senate column is Article I Section 3's two per state.
Nothing about them is an estimate, which is why the limitation item (23) asks
about what a seat count cannot measure -- a chamber's powers -- rather than
about sampling. The checks below confirm the Senate column is constant, that
the House column is not, and that the specific ratio the key names (ten to one,
Virginia against Delaware) is what the table says.

Items 24 to 26 turn on Article V's two thresholds, and every one of them is
recomputed here rather than trusted: two-thirds of 435 is 290, two-thirds of
100 is 67, three-fourths of 50 is 38 after rounding up from 37.5, and the
shortfall of four states that item 25 keys on is 38 minus 34. A threshold
question whose arithmetic is only asserted in the rationale is exactly the
failure this project has paid for before.

ONE NOTATION RULE ENFORCED BY WRITING, NOT BY A CHECK
-----------------------------------------------------
EK 1.5.A.4's first illustration is the September 2001 attacks. It is written
out in words throughout this module and never as the numeric shorthand, because
export_units.py runs every string through mathfmt.convert, which would read the
slash between two digits as a fraction and ship typeset arithmetic to a student.
The last check in this file asserts the shorthand appears nowhere in the module,
so the rule cannot lapse in a later edit.
"""
import re

import usgov_anchor as ua
import usgov_check as uc
import v1_5

ANCHORS = {
 1: "Connecticut Compromise",
 2: "neither side could impose its preference",
 3: "rather than by popular vote or by congressional vote",
 4: "keep the choice from turning on the popularity",
 5: "Representation in the House of Representatives and taxation",
 6: "exceeded what their free population alone would have supported",
 7: "not resolved at all but deferred",
 8: "agreement to add a Bill of Rights",
 9: "two-thirds vote in both houses of Congress or a proposal from two-thirds",
 10: "three-fourths of the states",
 11: "lowered the bar from unanimity",
 12: "even though its officers are chosen in different ways",
 13: "apportioned by population while the Senate represents states equally",
 14: "means and the motive to resist encroachment",
 15: "settled by war rather than by negotiation",
 16: "left that balance unresolved",
 17: "responsibility for security and the individual's claim",
 18: "belong to national authorities, to state authorities, or to individual families",
 19: "left for later argument rather than fixed in 1787",
 20: "did not by itself settle how far those guarantees reach",
 21: "ten times as many House seats as Delaware",
 22: "one chamber varies with population and the other does not vary at all",
 23: "the two chambers hold different powers",
 24: "cleared both congressional thresholds but fell short",
 25: "Four",
 26: "broad but not overwhelming support does not alter the Constitution",
 27: "supermajorities at two separate stages",
 28: "call for a convention to propose amendments",
 29: "what delegates would refuse to accept",
 30: "from surveillance policy to the governance of schools",
}

GROUNDING = {
 1: "EK 1.5.A.1.i, verbatim: the Great (Connecticut) Compromise 'created a dual "
    "(bicameral) system of congressional representation.'",
 2: "EK 1.5.A.1's framing of all five items as compromises 'deemed necessary for "
    "ratification' -- design driven by what each side could refuse.",
 3: "EK 1.5.A.1.ii, verbatim: election 'by electors from each state rather than by popular "
    "vote or by congressional vote.' The CED names both rejected alternatives.",
 4: "EK 1.5.A.1.ii read for its logic, the same distribute-across-states logic as the Great "
    "Compromise; U.S. Constitution Art. II Sec. 1 supplies the mechanism.",
 5: "EK 1.5.A.1.iii, verbatim: a formula 'for purposes of representation in the House and "
    "for taxation.' Senate representation is equal and unaffected.",
 6: "EK 1.5.A.1.iii. Adding part of a population to the apportionment base raises the seat "
    "count of the states holding that population.",
 7: "EK 1.5.A.1.iv: 'Postponing until 1808 a decision whether to ban the importation of "
    "enslaved persons' -- a deferral, which is EK 1.5.A.3's unresolved matters in miniature.",
 8: "EK 1.5.A.1.v: the agreement to add a Bill of Rights 'to address concerns of the "
    "Anti-Federalists,' who were outside the Convention.",
 9: "EK 1.5.A.2, verbatim: proposal by 'either a two-thirds vote in both houses or a "
    "proposal from two-thirds of the state legislatures.' U.S. Constitution Art. V.",
 10: "EK 1.5.A.2: 'final ratification determined by three-fourths of the states.'",
 11: "EK 1.5.A.2 against Articles of Confederation Article XIII, which required "
     "confirmation by the legislatures of every state.",
 12: "Federalist No. 39 (required document), the definition of a republic, quoted verbatim; "
     "the CED attaches Federalist No. 39 to 1.5.A. The definition covers direct election, "
     "indirect election and tenure during good behavior.",
 13: "Federalist No. 39 (required document), 'neither a national nor a federal "
     "Constitution, but a composition of both,' quoted verbatim; EK 1.7.A.1 credits "
     "Federalist No. 39 with explaining that the division combines national and state "
     "features.",
 14: "Federalist No. 51 (required document), 'Ambition must be made to counteract "
     "ambition,' quoted verbatim; the CED attaches Federalist No. 51 to 1.5.A.",
 15: "Emancipation Proclamation (required document), quoted verbatim; the CED attaches it "
     "to 1.5.A. Its own words limit it to areas then in rebellion, so it is a war measure "
     "rather than an Article V amendment.",
 16: "EK 1.5.A.3 and EK 1.5.A.4: the compromises left matters unresolved, and the "
     "national/state/individual balance remains at the heart of present-day issues.",
 17: "EK 1.5.A.4.i, the surveillance debate following the September 2001 attacks, written "
     "out in words rather than in the numeric shorthand mathfmt would typeset.",
 18: "EK 1.5.A.4.ii, debates about the role of government in public school education; the "
     "constitutional question is who decides, not what is decided.",
 19: "United States v. Lopez (1995), required case. CED holding: Congress exceeded its power "
     "under the Commerce Clause. A boundary dispute two centuries after ratification.",
 20: "Schenck v. United States (1919), required case. CED holding: speech creating a 'clear "
     "and present danger' was not protected and could be limited. Read against "
     "EK 1.5.A.1.v's Bill of Rights compromise.",
 21: "Data item on U.S. Constitution Art. I Sec. 2 (first House apportionment) and Art. I "
     "Sec. 3 (two senators per state); the ratio is recomputed below.",
 22: "EK 1.5.A.1.i seen in the table: population in one column, equality in the other.",
 23: "Data item, CED skill 3.E. A seat count measures presence, not the powers a chamber "
     "holds, and the Senate's advice and consent role has no House counterpart.",
 24: "Data item on EK 1.5.A.2's thresholds; both congressional thresholds and the state "
     "shortfall are recomputed below.",
 25: "EK 1.5.A.2: three-fourths of 50 rounds up to 38, and 38 minus 34 is 4. Recomputed "
     "below rather than asserted.",
 26: "EK 1.5.A.2 read for its purpose: a three-fourths threshold exists to stop change that "
     "commands a majority but not a consensus. Unanimity was the Articles' rule.",
 27: "EK 1.5.A.2's two stages, two-thirds to propose and three-fourths to ratify, which a "
     "proposal must clear in succession.",
 28: "EK 1.5.A.2's second proposal route, a call from two-thirds of the state legislatures, "
     "which exists so Congress is not the only gateway.",
 29: "EK 1.5.A.1 as a whole: four bargains between positions neither of which could prevail, "
     "and one concession extracted by the document's opponents.",
 30: "EK 1.5.A.3 and EK 1.5.A.4, including both of the CED's own illustrations.",
}

HOUSE, SEN = "Seats in the first House", "Seats in the Senate"
FAV, TOT = "In favor", "Total possible"
H, S, ST = "House of Representatives", "Senate", "State legislatures ratifying"


def _need(total, num, den):
    """The smallest whole count clearing a fraction of a total, rounding up."""
    return -((-total * num) // den)


TABLE_CHECKS = {
 21: [
  ("Virginia's House seats are exactly ten times Delaware's, and their Senate seats "
   "are equal, which is the key's whole claim",
   lambda t: uc.cell(t, "Virginia", HOUSE) == 10 * uc.cell(t, "Delaware", HOUSE)
   and uc.cell(t, "Virginia", SEN) == uc.cell(t, "Delaware", SEN)),
  ("the Senate column is constant at 2, so it neither varies with population nor "
   "varies with the House column",
   lambda t: set(uc.col(t, SEN)) == {2.0}),
  ("the House column is NOT constant, so 'every state held the same number' is false",
   lambda t: len(set(uc.col(t, HOUSE))) > 1),
  ("Delaware and Rhode Island together hold 2 House seats against New York's 6, so "
   "that distractor is false",
   lambda t: uc.cell(t, "Delaware", HOUSE) + uc.cell(t, "Rhode Island", HOUSE)
   < uc.cell(t, "New York", HOUSE)),
 ],
 22: [
  ("the House column varies while the Senate column does not, which is the pattern "
   "EK 1.5.A.1.i describes",
   lambda t: len(set(uc.col(t, HOUSE))) > 1 and len(set(uc.col(t, SEN))) == 1),
  ("no column in this table concerns the presidency or the Bill of Rights, so those "
   "distractors describe a table that is not here",
   lambda t: [h for h in t["headers"][1:]] == [HOUSE, SEN]),
 ],
 23: [
  ("the Senate IS in the table, so the 'omits the Senate entirely' distractor is "
   "false on the table's face",
   lambda t: SEN in t["headers"]),
  ("the table lists five states, not all thirteen, so that distractor is false too",
   lambda t: len(t["rows"]) == 5),
  ("no column reports population, so the 'population figures contradict' distractor "
   "refers to data the table does not contain -- which is itself the point of the item",
   lambda t: not any("population" in h.lower() for h in t["headers"])),
 ],
 24: [
  ("the House cleared two-thirds exactly: 290 in favor against 290 required of 435",
   lambda t: uc.cell(t, H, FAV) >= _need(uc.cell(t, H, TOT), 2, 3)
   and _need(uc.cell(t, H, TOT), 2, 3) == 290),
  ("the Senate cleared two-thirds: 68 against 67 required of 100",
   lambda t: uc.cell(t, S, FAV) >= _need(uc.cell(t, S, TOT), 2, 3)
   and _need(uc.cell(t, S, TOT), 2, 3) == 67),
  ("the states fell short of three-fourths: 34 against 38 required of 50",
   lambda t: uc.cell(t, ST, FAV) < _need(uc.cell(t, ST, TOT), 3, 4)
   and _need(uc.cell(t, ST, TOT), 3, 4) == 38),
  ("a MAJORITY of states did approve, which is what makes that distractor tempting "
   "and is not the Article V standard",
   lambda t: uc.cell(t, ST, FAV) > uc.cell(t, ST, TOT) / 2),
 ],
 25: [
  ("the shortfall is exactly four states, which is the keyed number",
   lambda t: _need(uc.cell(t, ST, TOT), 3, 4) - uc.cell(t, ST, FAV) == 4),
  ("none of the other keyed numbers -- one, two, eight, sixteen -- equals the "
   "shortfall, so exactly one option is right",
   lambda t: _need(uc.cell(t, ST, TOT), 3, 4) - uc.cell(t, ST, FAV)
   not in (1, 2, 8, 16)),
 ],
 26: [
  ("state support stands at 68 percent, broad but under the three-fourths bar, which "
   "is the situation the key describes",
   lambda t: 50 < 100 * uc.cell(t, ST, FAV) / uc.cell(t, ST, TOT) < 75),
  ("state legislatures do act in this process, so 'requires no action by state "
   "legislatures' is false of Article V and of the table alike",
   lambda t: ST in uc.labels(t) and uc.cell(t, ST, FAV) > 0),
 ],
}


def _no_numeric_shorthand(module):
    """EK 1.5.A.4.i must never ship as a slash between two digits."""
    hits = []
    for i, item in enumerate(module.QUESTIONS, 1):
        strings = [item["q"], item["why"]] + list(item["choices"])
        t = item.get("table")
        if t:
            strings += list(t["headers"]) + [c for row in t["rows"] for c in row]
        for s in strings:
            m = re.search(r"[0-9]\s*/\s*[0-9]", s)
            if m:
                hits.append(f"q{i}: {m.group(0)!r} would be typeset as a fraction on export")
    if hits:
        print(f"FAIL {module.__name__} notation")
        for h in hits:
            print("  -", h)
        raise SystemExit(1)
    print(f"OK  {module.__name__} notation: no digit/digit run anywhere in the module, so "
          "mathfmt.convert has nothing to read as a fraction")


ua.check(v1_5, ANCHORS, GROUNDING)
_no_numeric_shorthand(v1_5)
uc.check(v1_5, TABLE_CHECKS)

# WHAT THE REVIEW FOUND
# ---------------------
# No wrong key. One factual error in a stem, caught while writing GROUNDING:
# the shared stimulus for items 21 to 23 originally cited "Article I Section 3"
# for the House apportionment. Section 3 is the Senate; the first House's seat
# counts are enumerated in Section 2. The stem, the module header and the
# grounding all now say Section 2 for the House and Section 3 for the Senate.
#
# Worth recording for the next module, because it is the same class of mistake
# the project has hit before: the figures in that table are not survey data and
# not estimates -- they are constitutional text. Getting the citation wrong on a
# table of quoted numbers would have taught a student a false address for a real
# provision, which no arithmetic check would ever have caught.
