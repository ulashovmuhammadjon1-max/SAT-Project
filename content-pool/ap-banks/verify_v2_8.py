"""Structural gate for AP U.S. Government 2.8 The Judicial Branch.

ANCHORS, GROUNDING and the notation check via usgov_anchor, then usgov_check
with the six data items recomputed from their own tables.

"RESPECTIVELY" IS THE ENTIRE ESSENTIAL-KNOWLEDGE STATEMENT
------------------------------------------------------------
EK 2.8.A.1 is a pointer rather than a substantive claim: the foundation for the
powers of the judicial branch and the argument for how its independence checks
the other branches are set forth in Article III and Federalist No. 78,
RESPECTIVELY. One word does all the work. Drop it and the statement becomes
"two documents are about the courts," which is true, useless, and what a
paraphrase produces. Items 1, 2, 3 and 25 all turn on the pairing, and
_respectively below asserts that no key in this module attaches the
independence argument to Article III or the foundation to Federalist No. 78.

THE THREE-SOURCE DISTINCTION THIS MODULE IS BUILT TO TEACH
-----------------------------------------------------------
Article III VESTS the judicial power and fixes tenure. Federalist No. 78 ARGUES
that independence is essential under a limited constitution. Marbury v. Madison
ESTABLISHES the principle -- the CED's own verb. Three sources, three different
jobs, and none of the three uses the phrase "judicial review." Item 4 makes
that last point directly, because a student who goes looking for the phrase in
Article III and does not find it usually concludes the principle is
illegitimate rather than that it is structural.

The sources table in items 24 to 26 states the same three-way split as data,
and the checks below read its cells rather than trusting the prose, so a row
edited to say Article III establishes the principle would fail here.
"""
import usgov_anchor as ua
import usgov_check as uc
import v2_8

ANCHORS = {
 1: "Article III of the Constitution",
 2: "Federalist No. 78",
 3: "Article III supplies the foundation for the powers",
 4: "In none of them",
 5: "a principle that the constitutional text does not state in those terms",
 6: "Where the judicial power is vested, and the tenure",
 7: "tenure that does not expire, so a judge need not fear removal",
 8: "the least dangerous, so its independence may safely be secured",
 9: "The principle of judicial review established in Marbury",
 10: "mean nothing unless a body independent of the legislature can enforce them",
 11: "an argument for the practice, not a source of law",
 12: "Article III vests the judicial power, Federalist No. 78 argues",
 13: "exceeds constitutional limits and refuse to give it effect",
 14: "exceeds the authority the Constitution or a statute confers",
 15: "ruled against the executive on a claim of national security",
 16: "Marbury v. Madison (1803), which established that courts may declare",
 17: "can set aside the work of officials the voters chose",
 18: "or the legislature judges its own case",
 19: "removes the incentive to please whoever holds power",
 20: "declined to give the statute effect in cases before it",
 21: "far more state statutes than federal statutes in every period",
 22: "against the states far more often",
 23: "reports no denominator",
 24: "none of the three uses the phrase judicial review",
 25: "The Article III row, which supplies the vesting of the judicial power",
 26: "without appearing in it as a phrase",
 27: "through review of an enacted statute; the president, through review of an executive action",
 28: "requires funds or enforcement action",
 29: "accept the Court's judgments even when they oppose them",
 30: "rule against the government's position",
}

GROUNDING = {
 1: "EK 2.8.A.1.i: Article III supplies 'the foundation for powers of the judicial branch,' "
    "the first half of the framework's 'respectively' pairing.",
 2: "EK 2.8.A.1.ii: Federalist No. 78 supplies 'the argument for how its independence checks "
    "the power of other branches,' the second half of the pairing.",
 3: "EK 2.8.A.1's word 'respectively', which is the whole content of the statement.",
 4: "The phrase 'judicial review' appears in neither Article III nor Federalist No. 78, and "
    "the CED credits the PRINCIPLE to Marbury v. Madison. Structure, not vocabulary.",
 5: "Marbury v. Madison (1803), required case. CED holding: the Court 'established the "
    "principle of judicial review, empowering the Supreme Court to declare an act of the "
    "legislative or executive branch unconstitutional.' Establishing, not applying.",
 6: "U.S. Constitution Art. III Sec. 1, quoted verbatim: the vesting clause and tenure "
    "during good behavior. EK 2.8.A.1.i's foundation.",
 7: "U.S. Constitution Art. III Sec. 1's 'during good Behaviour', which is the structural "
    "source of the independence EK 2.10.A.1 later builds on.",
 8: "Federalist No. 78 (required document), 'neither FORCE nor WILL, but merely judgment,' "
    "quoted verbatim; the premise of the least-dangerous-branch argument.",
 9: "Federalist No. 78 (required document), 'No legislative act... contrary to the "
    "Constitution, can be valid,' quoted verbatim -- the reasoning Marbury later established "
    "as a principle. CED skill 2.B, relating a case to a foundational document.",
 10: "Federalist No. 78 (required document), the 'limited Constitution' passage, quoted "
     "verbatim: written exceptions to legislative authority need an enforcer outside it.",
 11: "EK 2.8.A.1 calls Federalist No. 78 an ARGUMENT; the Federalist papers are essays urging "
     "ratification and carry no legal force. The CED credits Marbury with establishing.",
 12: "EK 2.8.A.1's two assignments plus the CED's statement of the Marbury holding, in order.",
 13: "Marbury's holding as the CED states it, applied to the legislative branch: review "
     "operates on an enacted statute.",
 14: "Marbury's holding applied to the executive branch, which the CED's wording names "
     "explicitly. Removal of a president is impeachment, EK 1.6.B.2.",
 15: "New York Times Co. v. United States (1971), required case, which the CED attaches to "
     "2.8.A. CED holding: a heavy presumption against prior restraint even in national "
     "security cases -- EK 2.8.A.1's independence argument borne out.",
 16: "Marbury v. Madison (1803), required case, as a SCOTUS comparison; the non-required "
     "case's facts are printed in the stem per CED p. 29.",
 17: "U.S. Constitution Art. III Sec. 1's tenure provision read as the source of the "
     "democratic objection: independence is exactly the absence of electoral accountability.",
 18: "Federalist No. 78's 'limited Constitution' argument stated as the affirmative case; the "
     "same paper denies the judiciary any control of the purse.",
 19: "EK 2.8.A.1 places the foundation in a STRUCTURAL provision, and Federalist No. 51's "
     "ambition-counteracting-ambition logic is the same move: design rather than character.",
 20: "Marbury's holding as the CED states it: a court declines to give an unconstitutional "
     "act effect in the cases before it. Repeal belongs to the legislature, amendment to "
     "Art. V.",
 21: "Data item on a labelled hypothetical; both columns are compared period by period below.",
 22: "Marbury's holding names acts of the legislative or executive branch without limiting "
     "the level of government; the table shows review reaching both.",
 23: "Data item, CED skill 3.E: a count with no denominator cannot separate a more assertive "
     "court from a more active legislature.",
 24: "Data item; the three contributions and the three No answers are read from the cells "
     "below.",
 25: "EK 2.8.A.1.i located in a table row: Article III supplies the vesting of the "
     "judicial power and tenure during good behavior, which is the FIRST item of the "
     "framework's respectively pairing.",
 26: "EK 2.8.A.1 read against the absence of the phrase: a principle may rest on a text's "
     "structure without appearing in it as a phrase.",
 27: "Marbury's holding as the CED states it, paired with the instrument each branch "
     "produces.",
 28: "Federalist No. 78 (required document): the judiciary commands neither the sword nor the "
     "purse, so its decisions depend on branches that command both.",
 29: "Federalist No. 78's premise applied: a judgment's effect rests on acceptance by the "
     "branches with force and will.",
 30: "EK 2.8.A.1 operationalized: the check is measured by how often courts rule against the "
     "government where a constitutional limit is asserted.",
}

FED, STATE = "Federal statutes struck down", "State statutes struck down"
PERIODS = ["First period", "Second period", "Third period", "Fourth period"]
SUPPLIES = "What it supplies"
PHRASE = "Does the text use the phrase judicial review?"
ART3, F78, MARB = ("Article III of the Constitution", "Federalist No. 78",
                   "Marbury v. Madison (1803)")


def _cat(t, label, header):
    j = t["headers"].index(header)
    for row in t["rows"]:
        if row[0] == label:
            return row[j]
    raise KeyError(label)


TABLE_CHECKS = {
 21: [
  ("state statutes exceed federal statutes in every period, by at least four to one",
   lambda t: all(uc.cell(t, p, STATE) >= 4 * uc.cell(t, p, FED) for p in PERIODS)),
  ("both counts FALL in the fourth period, so 'both rose in every period' is false",
   lambda t: uc.cell(t, PERIODS[3], FED) < uc.cell(t, PERIODS[2], FED)
   and uc.cell(t, PERIODS[3], STATE) < uc.cell(t, PERIODS[2], STATE)),
  ("federal statutes are struck down in every period, so 'no federal statutes' is "
   "false",
   lambda t: min(uc.col(t, FED)) > 0),
  ("the state peak is the THIRD period, not the fourth",
   lambda t: uc.cell(t, PERIODS[2], STATE) == max(uc.col(t, STATE))),
 ],
 22: [
  ("both columns are non-zero in every period, so review reaches both levels",
   lambda t: min(uc.col(t, FED)) > 0 and min(uc.col(t, STATE)) > 0),
  ("the two columns are never equal, so 'exercised equally against the two levels' is "
   "false",
   lambda t: all(uc.cell(t, p, FED) != uc.cell(t, p, STATE) for p in PERIODS)),
 ],
 23: [
  ("both columns and four periods are present, so three distractors are false on the "
   "table's face",
   lambda t: {FED, STATE} <= set(t["headers"]) and len(t["rows"]) == 4),
  ("every cell is a whole count rather than a percentage, and no column sums to 100",
   lambda t: all(c.isdigit() for row in t["rows"] for c in row[1:])
   and sum(uc.col(t, FED)) != 100 and sum(uc.col(t, STATE)) != 100),
  ("nothing in the table reports how many statutes were enacted, which is the missing "
   "denominator the key names",
   lambda t: not any("enact" in h.lower() or "total" in h.lower() for h in t["headers"])),
 ],
 24: [
  ("the three contributions are three different things, which is the key's first "
   "clause",
   lambda t: len({_cat(t, lab, SUPPLIES) for lab in uc.labels(t)}) == 3),
  ("all three rows answer No to the phrase question, which is the key's second clause",
   lambda t: [_cat(t, lab, PHRASE) for lab in uc.labels(t)] == ["No", "No", "No"]),
  ("the Marbury row, not the Article III row, is the one that establishes the "
   "principle",
   lambda t: "establishment of the principle" in _cat(t, MARB, SUPPLIES)
   and "establish" not in _cat(t, ART3, SUPPLIES)),
 ],
 25: [
  ("the Article III row supplies the vesting and the tenure, which is EK 2.8.A.1.i",
   lambda t: "vesting of the judicial power" in _cat(t, ART3, SUPPLIES)
   and "good behavior" in _cat(t, ART3, SUPPLIES)),
  ("the Federalist No. 78 row supplies the independence argument, which is "
   "EK 2.8.A.1.ii and NOT what item 25 asks for",
   lambda t: "independent judiciary checks" in _cat(t, F78, SUPPLIES)),
 ],
 26: [
  ("no row claims any source uses the phrase, so the student's premise is right and "
   "only the inference is wrong -- which is what the key addresses",
   lambda t: "Yes" not in [_cat(t, lab, PHRASE) for lab in uc.labels(t)]),
  ("Federalist No. 78 is listed as a source of an ARGUMENT, not as part of the "
   "Constitution, so that distractor contradicts the table",
   lambda t: "argument" in _cat(t, F78, SUPPLIES).lower()),
 ],
}


def _respectively(module):
    """EK 2.8.A.1's pairing must never be reversed in a key or a rationale."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        for label, s in (("key", item["choices"][item["ans"]]), ("why", item["why"])):
            low = s.lower()
            if "article iii" in low and "argument for" in low and "federalist" not in low:
                bad.append(f"q{i} {label}: attaches the independence ARGUMENT to Article III; "
                           "EK 2.8.A.1 assigns it to Federalist No. 78")
            if ("federalist no. 78" in low and "foundation for the powers" in low
                    and "article iii" not in low):
                bad.append(f"q{i} {label}: attaches the FOUNDATION to Federalist No. 78; "
                           "EK 2.8.A.1 assigns it to Article III")
            if "federalist no. 78" in low and "part of the constitution" in low:
                bad.append(f"q{i} {label}: treats Federalist No. 78 as law")
    if bad:
        print(f"FAIL {module.__name__} respectively")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} respectively: no key or rationale reverses EK 2.8.A.1's "
          "pairing of Article III with the foundation and Federalist No. 78 with the "
          "independence argument")


ua.check(v2_8, ANCHORS, GROUNDING)
ua.notation(v2_8)
_respectively(v2_8)
uc.check(v2_8, TABLE_CHECKS)

# WHAT THE REVIEW FOUND
# ---------------------
# No wrong key. The thing worth recording is what item 4 is for.
#
# The phrase "judicial review" appears in none of the three sources this topic
# rests on -- not Article III, not Federalist No. 78, not the CED's statement of
# the Marbury holding, which says the Court ESTABLISHED the principle rather
# than that it named it. A student who goes looking for the phrase in the
# constitutional text and does not find it reaches one of two conclusions: that
# the principle is structural, or that it is illegitimate. Which one they reach
# depends on whether anyone told them the phrase was never there.
#
# So the module says it outright rather than leaving it to inference, and the
# sources table in items 24 to 26 states it as data with a column that reads No
# three times. The checks read that column rather than the prose, so a row
# edited to claim Article III uses the phrase, or establishes the principle,
# fails this file rather than teaching a student something false about the text.
