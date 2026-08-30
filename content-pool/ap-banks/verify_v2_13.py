"""Structural gate for AP U.S. Government 2.13 Discretionary and Rulemaking Authority.

ANCHORS, GROUNDING, the shape check and the notation check via usgov_anchor,
then usgov_check with the six data items recomputed from their own tables.

ONE WORD CARRIES THIS TOPIC: DELEGATED
----------------------------------------
EK 2.13.A.1 says the bureaucracy uses discretionary power AS DELEGATED BY
CONGRESS. Not inherent, not claimed, not conferred by the courts. Everything
else in the topic follows from that single attribution:

  * Congress can narrow, broaden or withdraw the discretion by rewriting the
    statute (item 2), which is why the same agency has wide latitude in one
    field and almost none in another (item 6).
  * A general standard IS a delegation, because it is a decision Congress
    declined to make (items 4 and 5).
  * A regulation must stay inside what the statute authorizes (item 10).

_delegated below asserts that no key attributes agency discretion to Article II,
to the courts, or to the agency itself. Those are the three plausible wrong
sources, and each is a distractor somewhere in the module -- so the check is
scoped to keys and rationales, never to choice lists.

THE SEVEN AGENCIES ARE REQUIRED COURSE CONTENT, NOT EXAMPLES
--------------------------------------------------------------
EK 2.13.A.1 ends with a named list: Homeland Security, Transportation, Veterans
Affairs, Education, EPA, Federal Elections Commission, SEC. Unlike the
illustrative examples elsewhere in this unit, these are inside the essential
knowledge statement, so items may name them. _seven_agencies checks all seven
appear and that item 14, a NOT-question over the list, has four distractors
that really are on it.

A NAMING NOTE, recorded so nobody "fixes" it: the CED writes "Federal Elections
Commission (FEC)". The agency's legal name is the Federal Election Commission,
singular. The module follows the CED because that is the examinable text, and
no item turns on the difference.
"""
import usgov_anchor as ua
import usgov_check as uc
import v2_13

ANCHORS = {
 1: "delegated by Congress",
 2: "narrow it, broaden it, or withdraw it by changing the statute",
 3: "interpret and implement policies",
 4: "the agency must decide what the standard means",
 5: "the statute has already made the decision",
 6: "depends on how specifically the particular statute is written",
 7: "cannot anticipate every situation a statute must cover",
 8: "officials the voters did not choose and cannot remove",
 9: "Through their rulemaking authority, by creating and enforcing regulations",
 10: "must stay within what the statute authorizes",
 11: "includes the means of determining compliance",
 12: "determine what the statute actually requires of anyone",
 13: "can change with the officials exercising the discretion",
 14: "The Federal Reserve Board",
 15: "The Securities and Exchange Commission",
 16: "The Environmental Protection Agency",
 17: "The Federal Elections Commission",
 18: "The Department of Transportation, with standards for commercial vehicle operation",
 19: "Both exercise delegated discretion through rulemaking",
 20: "the president is responsible for how they do it",
 21: "far more regulation than the two setting specific ones",
 22: "its extent varies with how the statute is written",
 23: "measure volume, not significance",
 24: "Most proposed rules survived to become final",
 25: "a proposed rule must survive comment and may be challenged in court",
 26: "may write a narrower rule in the first place",
 27: "then writes rules telling regulated parties what to do about it",
 28: "narrowing the delegation",
 29: "does the statute itself make, and how many does it leave to the agency",
 30: "which exercise it by creating and enforcing regulations",
}

GROUNDING = {
 1: "EK 2.13.A.1, verbatim: the bureaucracy 'uses discretionary power as delegated by "
    "Congress.' The word DELEGATED is the topic.",
 2: "EK 2.13.A.1's delegation read for its consequence, the same logic EK 2.11.B.1.i records "
    "for decisions: what legislation created, legislation can modify.",
 3: "EK 2.13.A.1's verbs: agencies use the discretion 'to interpret and implement policies.'",
 4: "EK 2.13.A.1 applied to a general standard, which is a decision Congress declined to make "
    "and therefore one the agency must.",
 5: "EK 2.13.A.1 applied to a specific standard: discretion is what a statute leaves open, so "
    "a statute that fixes the number leaves little.",
 6: "EK 2.13.A.1's delegation as the source: scope varies with the delegating statute rather "
    "than with anything about the agency.",
 7: "EK 2.13.A.1 read with EK 2.12.A.2's specialization criterion: a general legislature hands "
    "technical implementation to a permanent expert staff.",
 8: "EK 2.13.A.1 read for its strongest objection: the more a statute leaves open, the more is "
    "settled by officials no one elected.",
 9: "EK 2.13.A.1's second sentence: 'Through their rulemaking authority, federal bureaucratic "
    "agencies utilize their discretion to create and enforce regulations.'",
 10: "EK 2.13.A.1's delegation bounds the rulemaking: a regulation exceeding the statute is "
     "the fact pattern judicial review addresses (EK 2.8.A.1's Marbury principle).",
 11: "EK 2.13.A.1's 'implement' applied: the means of determining compliance is part of "
     "implementing a requirement, but the delegation still bounds it.",
 12: "EK 2.13.A.1's 'utilize their discretion' -- a discretionary choice about what a general "
     "standard means is a policy choice, which is why rulemaking is policymaking.",
 13: "EK 2.13.A.1's discretion read with EK 2.14.B.1: presidential ideology, authority and "
     "influence affect how agencies carry out the administration's goals.",
 14: "EK 2.13.A.1's list of seven, tested by exclusion. The Federal Reserve is not on it.",
 15: "EK 2.13.A.1.vii, the Securities and Exchange Commission, matched to its subject.",
 16: "EK 2.13.A.1.v, the Environmental Protection Agency, matched to its subject.",
 17: "EK 2.13.A.1.vi, which the CED writes as the Federal Elections Commission, matched to "
     "campaign finance reporting.",
 18: "EK 2.13.A.1.ii, the Department of Transportation; each distractor attaches a subject to "
     "the wrong agency on the same list.",
 19: "EK 2.13.A.1's list mixes departments and independent commissions because the property "
     "the statement is about -- delegated discretionary rulemaking -- is common to both; "
     "EK 2.12.A.1 separately notes the bureaucracy's four kinds of organization.",
 20: "U.S. Constitution Art. II Sec. 3, the Take Care Clause, quoted verbatim, against "
     "EK 2.13.A.1's congressional source. Both are true at once.",
 21: "Data item on a labelled hypothetical; the split between specific and general standards "
     "is recomputed below.",
 22: "EK 2.13.A.1 measured: the specificity of the delegating standard against the volume of "
     "regulation issued under it.",
 23: "Data item, CED skill 3.E: pages are an unweighted measure of output.",
 24: "Data item on a labelled hypothetical; the survival counts are recomputed below.",
 25: "EK 2.13.A.1's discretion shown operating inside a process with a comment stage and a "
     "judicial stage.",
 26: "Data item, CED skill 3.E: a survival rate cannot show the rules an agency chose not to "
     "write because it expected a challenge.",
 27: "EK 2.13.A.1's two verbs in sequence: deciding what a term means, then turning that "
     "meaning into operative requirements.",
 28: "EK 2.13.A.1's delegation as the target of a legislative response; federal courts issue "
     "no advisory opinions and a disapproval resolution changes no authority.",
 29: "EK 2.13.A.1 operationalized: count the decisions the statute does not make.",
 30: "EK 2.13.A.1's two sentences restated in order -- delegation as source, rulemaking as "
     "mechanism, interpretation and implementation as purpose.",
}

STANDARD, PAGES = "Standard the statute set", "Pages of regulation issued"
A, B, C, D = "Statute A", "Statute B", "Statute C", "Statute D"
REMAIN = "Proposed rules remaining"
PROPOSED = "Proposed and published for comment"
REVISED = "Revised after public comment"
FINAL = "Issued as a final rule"
SURVIVED = "Still in force after judicial challenge"


def _std(t, label):
    j = t["headers"].index(STANDARD)
    for row in t["rows"]:
        if row[0] == label:
            return row[j]
    raise KeyError(label)


TABLE_CHECKS = {
 21: [
  ("the two general standards produced 410 and 588 pages against 14 and 62 for the two "
   "specific ones, so every general statute outproduced every specific one",
   lambda t: min(uc.cell(t, s, PAGES) for s in (C, D))
   > max(uc.cell(t, s, PAGES) for s in (A, B))),
  ("the numerical-limit statute produced the FEWEST pages, so that distractor is "
   "reversed",
   lambda t: uc.cell(t, A, PAGES) == min(uc.col(t, PAGES))),
  ("the public-interest statute produced the MOST, so that distractor is reversed too",
   lambda t: uc.cell(t, D, PAGES) == max(uc.col(t, PAGES))),
  ("the four counts span 14 to 588, so 'similar amounts' is false",
   lambda t: max(uc.col(t, PAGES)) > 40 * min(uc.col(t, PAGES))),
  ("regulation RISES as the standard becomes more general, so the last distractor "
   "states the opposite of the table",
   lambda t: uc.col(t, PAGES) == sorted(uc.col(t, PAGES))),
 ],
 22: [
  ("the standard column is categorical and orders from a specific number to an open "
   "phrase, which is what makes the table a measure of the DELEGATION",
   lambda t: "numerical limit" in _std(t, A) and "public interest" in _std(t, D)),
  ("no column reports merit hiring, iron triangles or hearings, so those distractors "
   "cite data the table does not carry",
   lambda t: [h for h in t["headers"][1:]] == [STANDARD, PAGES]),
 ],
 23: [
  ("the standard column and four statutes are present, so two distractors are false on "
   "the table's face",
   lambda t: STANDARD in t["headers"] and len(t["rows"]) == 4),
  ("the page counts are counts rather than percentages and do not sum to 100",
   lambda t: sum(uc.col(t, PAGES)) != 100),
 ],
 24: [
  ("198 of 340 proposed rules became final, a majority, and 181 of those 198 survived "
   "challenge",
   lambda t: uc.cell(t, FINAL, REMAIN) * 2 > uc.cell(t, PROPOSED, REMAIN)
   and uc.cell(t, SURVIVED, REMAIN) * 2 > uc.cell(t, FINAL, REMAIN)),
  ("the comment stage loses 113 rules, more than the judicial stage's 17, so "
   "'judicial challenge removed more' is false",
   lambda t: uc.cell(t, PROPOSED, REMAIN) - uc.cell(t, REVISED, REMAIN) == 113
   and uc.cell(t, FINAL, REMAIN) - uc.cell(t, SURVIVED, REMAIN) == 17),
  ("not every proposed rule became final, so that distractor is false",
   lambda t: uc.cell(t, FINAL, REMAIN) < uc.cell(t, PROPOSED, REMAIN)),
  ("227 rules were revised after comment, so 'no rule was revised' is false",
   lambda t: uc.cell(t, REVISED, REMAIN) == 227),
 ],
 25: [
  ("the process has both a comment stage and a judicial stage, and rules are lost at "
   "each, which is the constraint the key describes",
   lambda t: uc.cell(t, REVISED, REMAIN) < uc.cell(t, PROPOSED, REMAIN)
   and uc.cell(t, SURVIVED, REMAIN) < uc.cell(t, FINAL, REMAIN)),
  ("no stage names Congress, the president or an industry vote, so the four "
   "distractors describe procedures this table does not contain",
   lambda t: not any(k in lab.lower() for lab in uc.labels(t)
                     for k in ("congress", "president", "industry", "vote"))),
 ],
 26: [
  ("the survival rate is high -- 181 of 198, over ninety percent -- which is what "
   "makes the weak-check inference tempting",
   lambda t: uc.cell(t, SURVIVED, REMAIN) / uc.cell(t, FINAL, REMAIN) > 0.9),
  ("four stages and the counts are present, and the column does not sum to 100",
   lambda t: len(t["rows"]) == 4 and sum(uc.col(t, REMAIN)) != 100),
 ],
}


def _delegated(module):
    """No key may attribute agency discretion to a source other than Congress."""
    wrong = ("granted directly by article ii", "claimed by each agency",
             "conferred by the federal courts", "reserved to the agencies by the tenth",
             "inherent authority")
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        for label, s in (("key", item["choices"][item["ans"]]), ("why", item["why"])):
            low = s.lower()
            for w in wrong:
                if w in low and not any(n in low for n in ("not ", "rather than", "never")):
                    bad.append(f"q{i} {label}: attributes agency discretion to {w!r}; "
                               "EK 2.13.A.1 says it is delegated by Congress")
    if bad:
        print(f"FAIL {module.__name__} delegated")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} delegated: no key or rationale attributes agency discretion "
          "to Article II, the courts, the Tenth Amendment or the agency itself")


def _seven_agencies(module):
    """All seven of EK 2.13.A.1's named agencies appear; item 14's distractors are real."""
    seven = ("homeland security", "transportation", "veterans affairs", "education",
             "environmental protection agency", "federal elections commission",
             "securities and exchange commission")
    blob = " ".join(it["q"] + " " + it["why"] + " " + " ".join(it["choices"])
                    for it in module.QUESTIONS).lower()
    bad = [f"EK 2.13.A.1 lists {a!r}, which appears nowhere in the module"
           for a in seven if a not in blob]
    q14 = module.QUESTIONS[13]
    if any(a in q14["choices"][q14["ans"]].lower() for a in seven):
        bad.append("q14: the keyed 'not on the list' choice is in fact one of the seven")
    for k, c in enumerate(q14["choices"]):
        if k == q14["ans"]:
            continue
        if not any(a in c.lower() for a in seven):
            bad.append(f"q14: distractor {'ABCDE'[k]} is not one of EK 2.13.A.1's seven, so "
                       "the NOT-question has two defensible keys")
    if bad:
        print(f"FAIL {module.__name__} seven agencies")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} seven agencies: all seven of EK 2.13.A.1's named agencies "
          "appear, and item 14's four distractors are exactly four of them")


ua.shape(v2_13)
ua.check(v2_13, ANCHORS, GROUNDING)
ua.notation(v2_13)
_delegated(v2_13)
_seven_agencies(v2_13)
uc.check(v2_13, TABLE_CHECKS)

# WHAT THE REVIEW FOUND
# ---------------------
# No wrong key. Three stray walrus expressions had been left inside question
# dicts in the source file -- the same defect v2_12 shipped one of, and it
# recurred twice more here before being caught.
#
# That is what moved the check out of a single verifier and into
# usgov_anchor.shape, which every US Government verifier in this bank now runs:
# a question dict may hold exactly q, choices, ans and why, plus an optional
# table, and any other key fails the module. All twenty existing verifiers were
# patched to call it and all twenty still pass, so the check is retroactive as
# well as prospective.
#
# The general lesson is the one this project keeps relearning from the other
# direction. A checker that over-matches trains you to ignore it; a defect that
# no checker looks for trains you to believe a clean run means more than it
# does. Twenty modules passed every content check in this bank while carrying a
# defect no content check could see, because nothing asserted the SHAPE of the
# data -- only its meaning.
