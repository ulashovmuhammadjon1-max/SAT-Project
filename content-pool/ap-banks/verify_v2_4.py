"""Structural gate for AP U.S. Government 2.4 Roles and Powers of the President.

ANCHORS, GROUNDING and the notation check via usgov_anchor, then usgov_check
with NINE data items recomputed from three tables. Nine rather than six because
this topic's suggested CED skill (p. 64) is 3.B, describe patterns and TRENDS
in data, and a trend needs a series rather than a single figure.

THE POCKET VETO, WHICH THIS FILE CHECKS AS A PROPERTY OF THE MODULE
--------------------------------------------------------------------
EK 2.4.A.2.i is one of the CED's flattest factual statements: vetoes "can be
overridden with a 2/3 vote while pocket vetoes CANNOT be overridden with a 2/3
vote" (AP_US_GOV_CED.md note 6). It is also the fact banks most often get
wrong, because the intuition that every veto faces an override vote is strong
and nothing about the phrase "pocket veto" contradicts it.

So _pocket_veto below is not a style check. It reads every string in the module
and fails if any sentence puts an override in the same clause as a pocket veto
without a negation. Item 23 exists for the same reason from the other side: it
makes a student notice that pocket vetoes must be excluded from the DENOMINATOR
of an override rate, which is the arithmetic consequence of the rule and the
place where a bank that knows the rule can still get the numbers wrong.

The veto table is built so that mistake is available: a student who divides
overrides by all vetoes gets 9 of 42 rather than 9 of 31, and both are plausible
numbers. The checks below recompute both, so the distractor is provably a
distractor rather than an alternative reading.

NOTATION, WITH A TWIST WORTH RECORDING
---------------------------------------
The CED itself writes "2/3 vote." Quoting the framework verbatim there would
ship a typeset fraction to students, because export_units.py runs every string
through mathfmt.convert. This module writes "two-thirds" throughout and says so
in its header; ua.notation enforces it. It is the one place so far where the
right thing to do is NOT to copy the CED's wording exactly.
"""
import usgov_anchor as ua
import usgov_check as uc
import v2_4

ANCHORS = {
 1: "Vice-President, the Cabinet, and the Executive Office",
 2: "include both formal and informal powers",
 3: "an executive agreement, an informal foreign policy power",
 4: "Commander in chief, formal; executive agreements, informal",
 5: "but a pocket veto cannot be overridden",
 6: "A pocket veto has occurred, and Congress cannot override it",
 7: "leaves Congress no vote to take",
 8: "formal powers that enable the president to check Congress",
 9: "implied by the vested executive power or delegated by Congress",
 10: "An executive order, which allows the president to manage the federal government",
 11: "informs Congress and the public of the president's interpretation",
 12: "accompanies a bill the president has signed into law; a veto prevents",
 13: "Bargaining and persuasion, informal powers",
 14: "Executive agreements, bargaining and persuasion, signing statements",
 15: "The veto, the pocket veto, the treaty power",
 16: "limited to what existing authority allows",
 17: "The veto, which the course framework classifies as a formal power",
 18: "the treaty power alone requires Senate concurrence",
 19: "Persuasion, an informal power used to build support",
 20: "granted for one purpose can become the basis for far-reaching policy action",
 21: "rose across the three periods, and overrides rose with them",
 22: "nine of thirty-one regular vetoes",
 23: "counts vetoes that were never eligible",
 24: "Three instruments rose across the three years while treaties",
 25: "increasingly on instruments that do not require a Senate vote",
 26: "one treaty may matter more than fifty routine orders",
 27: "both fell in every year, and the two series moved together",
 28: "informal powers enabling the president to secure congressional action",
 29: "nothing about which party controlled Congress",
 30: "instruments that do not require congressional agreement",
}

GROUNDING = {
 1: "EK 2.4.A.1, verbatim: presidents act 'with support from the Vice-President, Cabinet, "
    "and Executive Office of the President.'",
 2: "EK 2.4.A.2, verbatim: 'The powers of the president include both formal and informal "
    "powers.'",
 3: "EK 2.4.A.2.ii: executive agreements are the INFORMAL foreign policy power, against "
    "treaties, which are formal. Absence of Senate ratification is the tell.",
 4: "EK 2.4.A.2.ii sorts commander in chief and treaties as formal, executive agreements as "
    "informal.",
 5: "EK 2.4.A.2.i, verbatim in substance: 'vetoes can be overridden with a 2/3 vote while "
    "pocket vetoes cannot be overridden with a 2/3 vote.' Written here as two-thirds; see "
    "AP_US_GOV_CED.md note 6.",
 6: "EK 2.4.A.2.i applied to the adjournment scenario in which a pocket veto arises.",
 7: "EK 2.4.A.2.i's asymmetry explained procedurally: a returned bill can be voted on again "
    "and a bill dying on adjournment cannot. U.S. Constitution Art. I Sec. 7.",
 8: "EK 2.4.A.2.i classifies BOTH vetoes as formal powers that enable the president to check "
    "Congress; they differ only in whether an override is possible.",
 9: "EK 2.4.A.2.iv, verbatim: executive orders 'allow the president to manage the federal "
    "government and are implied by the president's vested executive power or by power "
    "delegated by Congress.'",
 10: "EK 2.4.A.2.iv applied: a directive to agencies about their own procedures is management "
     "of the federal government.",
 11: "EK 2.4.A.2.v, verbatim: signing statements 'inform Congress and the public of the "
     "president's interpretation of laws passed by Congress and signed by the president.'",
 12: "EK 2.4.A.2.v against EK 2.4.A.2.i: a signing statement attaches to a bill the president "
     "SIGNED; a veto blocks a bill. Opposite outcomes.",
 13: "EK 2.4.A.2.iii: 'Bargaining and persuasion are informal powers that enable the president "
     "to secure congressional action.'",
 14: "EK 2.4.A.2.ii, .iii and .v: the three informal instruments the framework names.",
 15: "EK 2.4.A.2.i and .ii: the four formal instruments the framework names.",
 16: "EK 2.4.A.2.iv: an order resting on vested or delegated authority is bounded by that "
     "authority and available to a successor to undo.",
 17: "U.S. Constitution Art. I Sec. 7, the Presentment Clause, quoted verbatim; EK 2.4.A.2.i "
     "classifies the veto it establishes as a formal power.",
 18: "U.S. Constitution Art. II Sec. 2, quoted verbatim; EK 2.4.A.2.ii lists both as formal "
     "foreign policy powers, and only the treaty power is conditioned on the Senate.",
 19: "Gettysburg Address (required document), Bliss copy, quoted verbatim; the CED attaches "
     "it to 2.4.A. EK 2.4.A.2.iii's persuasion is the power a public appeal exercises.",
 20: "Emancipation Proclamation (required document), which the CED attaches to 2.4.A, read "
     "against EK 2.4.A.2.ii's commander in chief power.",
 21: "Data item; all three series' directions are recomputed below.",
 22: "Data item; the three override shares are recomputed below, with pocket vetoes excluded "
     "from the denominator per EK 2.4.A.2.i.",
 23: "EK 2.4.A.2.i as arithmetic: a veto that cannot be overridden cannot belong in the "
     "denominator of an override rate. Both the right and the wrong ratio are recomputed.",
 24: "Data item; each instrument's direction of change is recomputed below.",
 25: "EK 2.4.A.2.ii and .iv: three of the four rows proceed without a Senate vote and rise, "
     "while the row requiring Senate concurrence falls.",
 26: "Data item, CED skill 3.E: a frequency count treats every use as equivalent.",
 27: "Data item; both series' monotonic decline is recomputed below.",
 28: "EK 2.4.A.2.iii: a president's public standing is the resource persuasion draws on.",
 29: "Data item, CED skill 3.E, read against EK 2.3.A.3: a change in party control would move "
     "both series and the table reports no such variable.",
 30: "EK 2.5.A.3 (policy conflict leads to executive orders and directives to the "
     "bureaucracy) with EK 2.4.A.2.iv. A signing statement accompanies a signed bill and "
     "cannot block one.",
}

REG, OVER, POCK = "Regular vetoes", "Vetoes overridden", "Pocket vetoes"
PERIODS = ["First two years", "Middle two years", "Final two years"]
EO, SS, EA, TR = ("Executive orders", "Signing statements", "Executive agreements",
                  "Treaties submitted to the Senate")
YEARS = ["Year 1", "Year 2", "Year 3"]
APPR, ENACT = "Approval rating (%)", "Proposals enacted (%)"
AYEARS = ["Year 1", "Year 2", "Year 3", "Year 4"]

TABLE_CHECKS = {
 21: [
  ("regular vetoes, pocket vetoes and overrides all rise across the three periods",
   lambda t: all(uc.col(t, c) == sorted(uc.col(t, c)) and len(set(uc.col(t, c))) == 3
                 for c in (REG, OVER, POCK))),
  ("regular vetoes exceed pocket vetoes in every period, so that distractor is false",
   lambda t: all(uc.cell(t, p, REG) > uc.cell(t, p, POCK) for p in PERIODS)),
  ("eleven vetoes were overridden in total, so 'no veto was overridden' is false",
   lambda t: sum(uc.col(t, OVER)) == 11),
 ],
 22: [
  ("the final period's override share is nine of thirty-one, about twenty-nine "
   "percent, and it is the largest of the three",
   lambda t: uc.cell(t, PERIODS[2], OVER) == 9
   and uc.cell(t, PERIODS[2], REG) == 31
   and round(100 * 9 / 31) == 29
   and all(uc.cell(t, p, OVER) / uc.cell(t, p, REG)
           < uc.cell(t, PERIODS[2], OVER) / uc.cell(t, PERIODS[2], REG)
           for p in PERIODS[:2])),
  ("the middle period's share really is about twelve percent -- true, and not the "
   "largest, which is what makes it a distractor rather than an error",
   lambda t: round(100 * uc.cell(t, PERIODS[1], OVER) / uc.cell(t, PERIODS[1], REG)) == 12),
  ("the first period had zero overrides, so its share is zero rather than largest",
   lambda t: uc.cell(t, PERIODS[0], OVER) == 0),
  ("an overrides column exists, so 'cannot be determined' is false on the face of it",
   lambda t: OVER in t["headers"]),
 ],
 23: [
  ("the WRONG denominator is available in the table: regular plus pocket vetoes in "
   "the final period is 42, against 31 regular vetoes, so 9 of 42 and 9 of 31 are "
   "both computable and only one is right",
   lambda t: uc.cell(t, PERIODS[2], REG) + uc.cell(t, PERIODS[2], POCK) == 42
   and uc.cell(t, PERIODS[2], REG) == 31),
  ("the two ratios differ materially -- about 21 percent against about 29 -- so the "
   "error is not harmless rounding",
   lambda t: round(100 * 9 / 42) == 21 and round(100 * 9 / 31) == 29),
  ("the table has no column for overrides of pocket vetoes, because there is no such "
   "thing under EK 2.4.A.2.i",
   lambda t: not any("pocket" in h.lower() and "overrid" in h.lower()
                     for h in t["headers"])),
 ],
 24: [
  ("three instruments rise and treaties submitted fall, which is the key",
   lambda t: all(uc.col(t, y) for y in YEARS)
   and all(uc.cell(t, lab, YEARS[0]) < uc.cell(t, lab, YEARS[2])
           for lab in (EO, SS, EA))
   and uc.cell(t, TR, YEARS[0]) > uc.cell(t, TR, YEARS[2])),
  ("executive agreements exceed treaties in every year by more than tenfold, so "
   "'used less often than treaties' is false",
   lambda t: all(uc.cell(t, EA, y) > 10 * uc.cell(t, TR, y) for y in YEARS)),
  ("signing statements are never the largest row, so that distractor is false",
   lambda t: all(uc.cell(t, SS, y) < max(uc.col(t, y)) for y in YEARS)),
  ("executive orders RISE, so 'executive orders fell' is false",
   lambda t: uc.cell(t, EO, YEARS[2]) > uc.cell(t, EO, YEARS[0])),
 ],
 25: [
  ("the three instruments needing no Senate vote all rise while the one requiring "
   "Senate concurrence falls -- the contrast the key rests on",
   lambda t: all(uc.cell(t, lab, YEARS[2]) > uc.cell(t, lab, YEARS[0])
                 for lab in (EO, SS, EA))
   and uc.cell(t, TR, YEARS[2]) < uc.cell(t, TR, YEARS[0])),
  ("no veto row appears, so the veto distractor cites data the table does not carry",
   lambda t: not any("veto" in lab.lower() for lab in uc.labels(t))),
 ],
 26: [
  ("an executive orders row is present and three years are reported, so those two "
   "distractors are false on the table's face",
   lambda t: EO in uc.labels(t) and len(YEARS) == 3),
  ("every cell is a whole count and no column sums to 100, so the percentage "
   "distractor describes a table that is not here",
   lambda t: all(c.isdigit() for row in t["rows"] for c in row[1:])
   and all(sum(uc.col(t, y)) != 100 for y in YEARS)),
 ],
 27: [
  ("both series fall in every year, which is the key",
   lambda t: all(uc.cell(t, a, APPR) > uc.cell(t, b, APPR)
                 for a, b in zip(AYEARS, AYEARS[1:]))
   and all(uc.cell(t, a, ENACT) > uc.cell(t, b, ENACT)
           for a, b in zip(AYEARS, AYEARS[1:]))),
  ("approval falls below half by the third year, so 'above half in every year' is "
   "false",
   lambda t: uc.cell(t, "Year 3", APPR) < 50),
  ("enactment is below approval in every year, so the reverse claim is false",
   lambda t: all(uc.cell(t, y, ENACT) < uc.cell(t, y, APPR) for y in AYEARS)),
 ],
 28: [
  ("the two series fall together across four years, which is the pattern a claim "
   "about persuasion would rest on",
   lambda t: uc.cell(t, "Year 1", APPR) - uc.cell(t, "Year 4", APPR) == 27
   and uc.cell(t, "Year 1", ENACT) - uc.cell(t, "Year 4", ENACT) == 36),
  ("no column reports vetoes, executive orders, signing statements or treaties, so "
   "the four distractors cite instruments the table does not contain",
   lambda t: [h for h in t["headers"][1:]] == [APPR, ENACT]),
 ],
 29: [
  ("the two series move in the SAME direction, so the 'opposite directions' "
   "distractor misdescribes the table it is attached to",
   lambda t: (uc.cell(t, "Year 4", APPR) < uc.cell(t, "Year 1", APPR))
   == (uc.cell(t, "Year 4", ENACT) < uc.cell(t, "Year 1", ENACT))),
  ("four years and both series are present, and both columns are percentages, so "
   "three of the four distractors are false on the table's face",
   lambda t: len(t["rows"]) == 4 and APPR in t["headers"]
   and all("%" in h for h in t["headers"][1:])),
  ("no column reports party control, which is the omission the key names",
   lambda t: not any("part" in h.lower() or "control" in h.lower()
                     for h in t["headers"])),
 ],
}


def _pocket_veto(module):
    """No KEY and no RATIONALE may assert that a pocket veto can be overridden.

    Scoped to the keyed choice and the `why`, deliberately. A distractor whose
    whole job is to state the falsehood -- item 5's "Both a regular veto and a
    pocket veto can be overridden" -- must be allowed to say it, and so must a
    stem describing a student's wrong calculation. An earlier version of this
    function read every string in the module and reported eight findings, every
    one of them a correct distractor doing its job. That is the over-matching
    checker this project keeps re-inventing: it would have trained the next
    reader to skim past real output. What must never state the falsehood is the
    text a student is told is TRUE.
    """
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        for label, s in (("key", item["choices"][item["ans"]]), ("why", item["why"])):
            for clause in s.replace(";", ".").replace(",", ".").split("."):
                low = clause.lower()
                if "pocket veto" not in low or "overrid" not in low:
                    continue
                if any(n in low for n in ("cannot", "can not", "never", "not ",
                                          "no ", "excluded", "ineligible")):
                    continue
                bad.append(f"q{i} {label}: {clause.strip()!r} asserts a pocket veto "
                           "override with no negation")
    if bad:
        print(f"FAIL {module.__name__} pocket veto")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} pocket veto: no key and no rationale states or implies "
          "that a pocket veto can be overridden, per EK 2.4.A.2.i")


ua.check(v2_4, ANCHORS, GROUNDING)
ua.notation(v2_4)
_pocket_veto(v2_4)
uc.check(v2_4, TABLE_CHECKS)

# WHAT THE REVIEW FOUND
# ---------------------
# No wrong key. Two decisions worth recording, both of which are the module
# departing from what looks like the obvious thing to do:
#
#   * The CED writes "2/3 vote." This module writes "two-thirds" everywhere, and
#     ua.notation enforces it, because export_units.py would typeset the CED's
#     own notation as a fraction. It is the first place in this bank where
#     quoting the framework verbatim would have been the wrong call.
#   * Item 23 is an arithmetic item about a rule, not about a table. A bank can
#     state EK 2.4.A.2.i correctly in prose and still compute an override rate
#     with pocket vetoes in the denominator, and the veto table is built so both
#     denominators are available: 9 of 42 gives 21 percent, 9 of 31 gives 29.
#     The checks recompute both, so the wrong reading is provably wrong rather
#     than merely disfavoured.
#
# And one own-goal, caught and fixed here rather than shipped: the first version
# of _pocket_veto read EVERY string in the module and reported eight findings --
# all eight of them correct distractors doing exactly their job, plus a stem
# describing a student's wrong calculation. It is the same over-matching checker
# this project has now built several times (\bpi, LETTER_REF, the shared-span
# detector). The function is now scoped to the keyed choice and the rationale,
# which is the only text a student is told is true, and the docstring records
# why so nobody widens it again.
