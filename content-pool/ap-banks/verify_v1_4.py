"""Structural gate for AP U.S. Government 1.4 Challenges of the Articles of Confederation.

Same three parts as the other Unit 1 verifiers -- ANCHORS, GROUNDING (both run
by usgov_anchor.check) and TABLE_CHECKS -- with one difference worth naming.

THIS MODULE HAS A CATEGORICAL TABLE, AND IT IS STILL CHECKED
------------------------------------------------------------
Items 21 to 23 hang off a table whose cells are the words Yes and No, not
numbers, so ``usgov_check.number`` cannot read it and there is no arithmetic to
recompute. The temptation is to write "no arithmetic claim" and move on. That
would leave the table's real content -- which document grants which power --
unguarded, and a single cell flipped from No to Yes would silently make three
questions wrong.

So the claims below read the raw rows instead: every entry in the Articles
column is a denial, every entry in the Constitution column is a grant, the six
row labels are the ones the questions name, and no row mentions an executive.
That is the same discipline as an arithmetic recomputation, applied to a table
that happens to hold words.

Items 24 to 26 use a numeric table, and it is labelled HYPOTHETICAL in the
stem. That is a deliberate choice recorded in the module header: per-state
Confederation requisition receipts could not be verified against a source, and
SOCIAL_BRIEF.md forbids inventing figures and presenting them as history. A
hypothetical confederation makes exactly the same point about a voluntary
revenue system and asserts nothing false about the past.
"""
import usgov_anchor as ua
import usgov_check as uc
import v1_4

ANCHORS = {
 1: "lack of centralized military power",
 2: "executive branch to enforce laws",
 3: "binding judgment",
 4: "regulate commerce among the states",
 5: "but so could the states",
 6: "any power that could not be pointed to in the text",
 7: "single state could block any change",
 8: "unanimous consent of the state legislatures",
 9: "already failed",
 10: "attended to the second requirement and neglected the first",
 11: "cannot be relied on to govern themselves",
 12: "permits powers implied from those enumerated",
 13: "enforces individual rights against state governments",
 14: "lacked both the exclusive power over coinage",
 15: "compliance depended on each state's own choice",
 16: "systematically deny the union the powers",
 17: "assessed the states but could not collect",
 18: "call forth the militia to suppress insurrections",
 19: "Commerce Clause of Article I Section 8",
 20: "organized the western territories",
 21: "denied to the national legislature under the Articles and granted",
 22: "omits any power the Articles granted",
 23: "the table lists legislative powers only",
 24: "smaller share of its assigned amount in each successive year",
 25: "depends on what it expects the others to pay",
 26: "tax individuals directly and an executive able to collect",
 27: "minority of the population the power to block",
 28: "deliberate choice to keep sovereignty in the states",
 29: "powers needed for the tasks the union was actually asked to perform",
 30: "remains at the heart of present-day constitutional issues",
}

GROUNDING = {
 1: "EK 1.4.A.1.i, verbatim: 'Lack of centralized military power to address Shays' "
    "Rebellion.' Article XIII does contain an amendment process, so that distractor is "
    "false of the document as well as off-point.",
 2: "EK 1.4.A.1.ii: 'Lack of an executive branch to enforce laws, including taxation.' "
    "Congress could assess; nothing could collect.",
 3: "EK 1.4.A.1.iii: 'Lack of a national court system.' Answered by Article III, which "
    "extends the judicial power to controversies between two or more states.",
 4: "EK 1.4.A.1.iv: 'Lack of power to regulate interstate commerce.' Answered by the "
    "Commerce Clause, Art. I Sec. 8.",
 5: "EK 1.4.A.1.v: lack of the EXCLUSIVE power to coin money. The CED's word is "
    "'exclusive'; saying Congress had no coinage power at all misdescribes the Articles.",
 6: "Articles of Confederation (required document), Article II, quoted verbatim. The word "
    "'expressly' is what forecloses implied powers.",
 7: "Articles of Confederation (required document), Article XIII, quoted verbatim. "
    "Confirmation by the legislatures of every state is a unanimity rule.",
 8: "Articles of Confederation Article XIII against U.S. Constitution Article VII, which "
    "set ratification at nine states, and Article V, which replaced unanimity.",
 9: "Federalist No. 10 (required document), the opening catalogue of complaints, quoted "
    "verbatim; the CED attaches Federalist No. 10 to 1.4.A.",
 10: "Federalist No. 51 (required document), 'enable the government to control the "
     "governed... oblige it to control itself,' quoted verbatim; the CED attaches "
     "Federalist No. 51 to 1.4.A. The Articles failed the first requirement.",
 11: "Federalist No. 51 (required document), 'If men were angels,' quoted verbatim; the "
     "sentence argues both for government and for controls on it.",
 12: "McCulloch v. Maryland (1819), required case. CED holding: supremacy of the U.S. "
     "Constitution and federal laws over state laws; the reasoning rests on the Necessary "
     "and Proper Clause, which Article II of the Articles forecloses.",
 13: "McDonald v. Chicago (2010), required case, which the CED attaches to 1.4.A. CED "
     "holding: the Second Amendment right is applicable to the states -- an authority over "
     "a state's treatment of its own residents that the Confederation had in no form.",
 14: "EK 1.4.A.1.v and EK 1.4.A.1.ii together: no exclusive coinage power, and no executive "
     "to enforce whatever Congress did decide.",
 15: "EK 1.4.A.1.ii. A government acting on states rather than individuals must ask; the "
     "Articles did provide for new states and for treaties, so those distractors are false.",
 16: "EK 1.4.A.1 read as a pattern rather than a list of accidents, against the Articles' "
     "Article II sovereignty rule.",
 17: "EK 1.4.A.1.ii applied to a modern scenario: a body that may assess but not enforce "
     "invites every member to hold back.",
 18: "EK 1.4.A.1.i answered by U.S. Constitution Art. I Sec. 8, the powers to raise and "
     "support armies and to call forth the militia to suppress insurrections.",
 19: "EK 1.4.A.1.iv answered by the Commerce Clause. The other four pairings misassign the "
     "clause: Art. III creates courts, Art. II the executive, Art. I Sec. 10 bars state "
     "coinage, Art. V replaces unanimity.",
 20: "EK 1.4.A.1 read for what the Confederation COULD do: organizing the western "
     "territories required no coercion of any state, which is why it succeeded.",
 21: "Data item on a categorical table; the claim is recomputed below from the raw cells, "
     "not from the prose.",
 22: "Data item, CED skill 3.E, explain limitations of the data: rows selected for having "
     "changed will always show change.",
 23: "Data item mapping EK 1.4.A.1's five weaknesses onto the table's rows; four have a row "
     "and the missing branch cannot have one.",
 24: "Data item on a labelled hypothetical confederation; the monotonic decline and each "
     "distractor's falsity are recomputed below.",
 25: "EK 1.4.A.1.ii's mechanism stated as an incentive: a voluntary system rewards holding "
     "back, which is why compliance decays rather than holds steady.",
 26: "EK 1.4.A.1.ii's cure: a power that reaches individuals without a state's cooperation, "
     "which is what U.S. Constitution Art. I Sec. 8 supplies.",
 27: "Articles of Confederation, one vote per state and a nine-state threshold for major "
     "measures, DESCRIBED not quoted; there was no executive branch to hold a veto.",
 28: "EK 1.4.A.1 presents the weaknesses as consequences of provisions, and Article II "
     "states the sovereignty choice they follow from.",
 29: "EK 1.4.A.1's own framing -- 'specific incidents and legal challenges' -- makes the "
     "test of the document what it could not do when called on.",
 30: "EK 1.5.A.4, verbatim in substance: the roles of national government, state powers and "
     "individual rights remain at the heart of present-day constitutional issues; "
     "EK 1.5.A.3 adds that the ratification compromises left matters unresolved.",
}

ART, CON = "Articles of Confederation", "U.S. Constitution"
YEARS = ["Year 1 paid (%)", "Year 2 paid (%)", "Year 3 paid (%)"]


def _powers_col(t, header):
    """The words in a categorical column, in row order."""
    j = t["headers"].index(header)
    return [row[j] for row in t["rows"]]


TABLE_CHECKS = {
 21: [
  ("every cell in the Articles column is a denial and every cell in the Constitution "
   "column is a grant, which is the key's claim, read from the raw cells",
   lambda t: _powers_col(t, ART) == ["No"] * len(t["rows"])
   and _powers_col(t, CON) == ["Yes"] * len(t["rows"])),
  ("the two columns therefore differ on EVERY row, so 'agree on others' is false",
   lambda t: all(a != b for a, b in zip(_powers_col(t, ART), _powers_col(t, CON)))),
  ("the Articles column grants none of the listed powers, so 'a majority' is false",
   lambda t: _powers_col(t, ART).count("Yes") == 0),
  ("the Constitution column withholds none, so 'at least one withheld' is false",
   lambda t: _powers_col(t, CON).count("No") == 0),
 ],
 22: [
  ("the table has six rows and every one of them is a power the Constitution added, "
   "so nothing in it could show a power the Articles granted or the Constitution "
   "withheld -- which is exactly the limitation the key names",
   lambda t: len(t["rows"]) == 6
   and all(row[t["headers"].index(ART)] == "No"
           and row[t["headers"].index(CON)] == "Yes" for row in t["rows"])),
  ("both documents are named in the headers, so 'covers only one' is false",
   lambda t: ART in t["headers"] and CON in t["headers"]),
  ("no cell holds a number, so 'contains numerical data' is false",
   lambda t: not any(c.strip().lstrip("-").replace(".", "").isdigit()
                     for row in t["rows"] for c in row)),
 ],
 23: [
  ("four of EK 1.4.A.1's five weaknesses have a row of their own -- army, commerce, "
   "courts, exclusive coinage",
   lambda t: all(any(k in row[0] for row in t["rows"])
                 for k in ("army", "commerce among the states",
                           "national court system", "Coin money to the exclusion"))),
  ("no row mentions an executive or a president, so the fifth weakness has none",
   lambda t: not any("executive" in row[0].lower() or "president" in row[0].lower()
                     for row in t["rows"])),
  ("every row label names a power of the LEGISLATURE, which is what the key's "
   "reason turns on",
   lambda t: "national legislature" in t["headers"][0]),
 ],
 24: [
  ("every state's share falls in each successive year, without exception",
   lambda t: all(uc.cell(t, s, YEARS[0]) > uc.cell(t, s, YEARS[1]) > uc.cell(t, s, YEARS[2])
                 for s in uc.labels(t))),
  ("no state increases in any year, so 'at least one increased' is false",
   lambda t: not any(uc.cell(t, s, YEARS[k + 1]) > uc.cell(t, s, YEARS[k])
                     for s in uc.labels(t) for k in (0, 1))),
  ("at least one state is under half in every year, so 'every state above half' fails",
   lambda t: all(min(uc.col(t, y)) < 50 for y in YEARS)),
  ("the Year 1 leader is still the Year 3 leader, so the 'largest becomes smallest' "
   "distractor is false",
   lambda t: uc.labels(t)[uc.col(t, YEARS[0]).index(max(uc.col(t, YEARS[0])))]
   == uc.labels(t)[uc.col(t, YEARS[2]).index(max(uc.col(t, YEARS[2])))]),
  ("the spread between highest and lowest WIDENS, from 53 to 56 points, so the "
   "narrowing distractor is false",
   lambda t: [max(uc.col(t, y)) - min(uc.col(t, y)) for y in YEARS] == [53, 52, 56]),
 ],
 25: [
  ("the decline is monotonic in all five rows, so 'fluctuate randomly' is false",
   lambda t: all(uc.cell(t, s, YEARS[0]) > uc.cell(t, s, YEARS[1]) > uc.cell(t, s, YEARS[2])
                 for s in uc.labels(t))),
  ("no state reaches zero, so 'agreed to stop paying entirely' is false",
   lambda t: min(min(uc.col(t, y)) for y in YEARS) > 0),
  ("at least one state pays two thirds of its share in every year, so 'too high for "
   "any state to meet' is false",
   lambda t: all(max(uc.col(t, y)) >= 66 for y in YEARS)),
  ("the table carries no population column, so the largest-population distractor "
   "cannot be supported by these data at all",
   lambda t: not any("population" in h.lower() for h in t["headers"])),
 ],
 26: [
  ("the mean share collected falls every year, from 52 to 43 to 34 percent, which is "
   "the problem a structural change would have to reverse",
   lambda t: [round(sum(uc.col(t, y)) / len(t["rows"])) for y in YEARS] == [52, 43, 34]),
  ("even the best-complying state pays less each year, so rewarding last year's "
   "payment with a smaller assignment would reward decline",
   lambda t: max(uc.col(t, YEARS[2])) < max(uc.col(t, YEARS[0]))),
 ],
}

ua.check(v1_4, ANCHORS, GROUNDING)
uc.check(v1_4, TABLE_CHECKS)

# WHAT THE REVIEW FOUND
# ---------------------
# No wrong key. One item was rewritten rather than shipped: item 23 originally
# keyed "the military weakness is represented only indirectly," which is a
# judgement about a row rather than a fact about the table, and its own last
# distractor ("fully represented by the row on levying taxes") was closer to the
# truth than the key. It now asks which weakness has NO row, and the answer --
# the absence of an executive branch -- is checked from the row labels below.
#
# One factual trap avoided, and it is the reason item 5 exists: the Articles did
# NOT deny Congress the power to coin money. Congress could coin; so could the
# states. The CED's phrase is the lack of the EXCLUSIVE power, and every
# currency item in this module uses that word.
