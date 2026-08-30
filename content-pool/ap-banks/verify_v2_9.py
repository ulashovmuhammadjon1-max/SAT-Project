"""Structural gate for AP U.S. Government 2.9 The Role of the Judicial Branch.

ANCHORS, GROUNDING and the notation check via usgov_anchor, then usgov_check
with the six data items recomputed from their own tables.

TWO STATEMENTS THAT PULL IN OPPOSITE DIRECTIONS
------------------------------------------------
EK 2.9.A.1 says courts follow precedent. EK 2.9.A.2 says the Court's changing
composition has led it to reject precedent. Both are in the framework, and a
module that teaches only one of them is wrong in a way that is hard to see:
teach only the first and a student cannot explain any overruling; teach only the
second and precedent looks like decoration. The GROUNDING map below is where the
balance is auditable -- roughly ten items on the doctrine, eight on change, four
on how the two fit together, six on the tables -- and item 27 makes the
reconciliation itself the question.

THE THIRD OPTION STUDENTS DO NOT KNOW ABOUT
--------------------------------------------
EK 2.9.A.1's parenthesis limits stare decisis to cases with SIMILAR FACTS, which
means a court's ordinary move is neither following nor overruling but
DISTINGUISHING -- holding that the facts differ so the precedent does not reach
them. Items 5, 6 and 23 turn on it, and the precedent table is built so
distinctions are the column that actually grows: 58 to 108, against overrulings
that go 3, 6, 11, 9. A student who knows only "follow" and "overrule" reads that
table as a court abandoning precedent, which is the misreading item 23 catches.

_causal_chain below asserts that no key or rationale attributes precedential
change to public opinion, to Congress, or to amendment. EK 2.9.A.2 names one
cause -- ideological changes in composition due to presidential appointments --
and the plausible-sounding substitutes are all false to the framework.
"""
import usgov_anchor as ua
import usgov_check as uc
import v2_9

ANCHORS = {
 1: "courts follow legal precedents when deciding cases with similar facts",
 2: "An important role in judicial decision making",
 3: "predict how a rule will be applied and plan accordingly",
 4: "The facts of the new case must be similar",
 5: "Distinguished the case, which leaves the earlier precedent standing",
 6: "Distinguishing leaves the earlier rule in force for cases like the earlier one",
 7: "must follow the precedent even while disagreeing",
 8: "arranged their affairs in reliance on the rule",
 9: "continues to produce wrong outcomes for as long as it stands",
 10: "the governing precedent, which a court deciding a case with similar facts",
 11: "Ideological changes in the composition of the Court due to presidential appointments",
 12: "Presidential appointments change the Court's composition",
 13: "have led the Court to reject existing precedents",
 14: "appointed by presidents of the party that had supported the earlier rule",
 15: "an appointment is a decision about future law",
 16: "rare relative to the number of cases decided",
 17: "Whether the facts before the court are similar",
 18: "fixing in advance what their duty is",
 19: "keeps that freedom from becoming personal discretion",
 20: "Overruling a precedent, which the framework attributes",
 21: "followed the governing precedent in the large majority of cases",
 22: "That stare decisis plays an important role",
 23: "distinguishing a case leaves the precedent standing",
 24: "and the number of precedents rejected rose across the three periods",
 25: "have led to the rejection of existing precedents",
 26: "records no information about the cases themselves",
 27: "changes in who decides account for the minority of cases",
 28: "even when its current members disagree with the earlier result",
 29: "how often does the court follow it rather than overruling it",
 30: "with no comparable change in the kinds of cases reaching the court",
}

GROUNDING = {
 1: "EK 2.9.A.1's own parenthesis: stare decisis is 'the legal doctrine under which courts "
    "follow legal precedents when deciding cases with similar facts.'",
 2: "EK 2.9.A.1: the doctrine 'plays an important role in judicial decision making,' without "
    "limitation by level of court or type of case.",
 3: "EK 2.9.A.1 read for why the role is important: consistency buys predictability.",
 4: "EK 2.9.A.1's condition, 'with similar facts', which is the threshold for the doctrine "
    "applying at all.",
 5: "EK 2.9.A.1's similar-facts condition seen from the other side: a court finding the facts "
    "unlike declines to apply the precedent without disturbing it.",
 6: "EK 2.9.A.1 against EK 2.9.A.2: distinguishing narrows reach, overruling rejects the rule.",
 7: "EK 2.9.A.1's doctrine applied to a lower court; disagreement is not one of its "
    "exceptions, and only the Supreme Court can reject its own precedent.",
 8: "EK 2.9.A.1's predictability read as reliance, which is what must be weighed against "
    "correcting an error.",
 9: "EK 2.9.A.2's premise stated as a reason rather than a cause: a wrong rule keeps "
    "producing wrong outcomes. Composition explains why courts overrule, not why they should.",
 10: "New York Times Co. v. United States (1971), required case, which the CED attaches to "
     "2.9.A. CED holding: a heavy presumption against prior restraint even in national "
     "security cases -- the governing precedent for the next such case under EK 2.9.A.1.",
 11: "EK 2.9.A.2, verbatim: 'Ideological changes in the composition of the Supreme Court due "
     "to presidential appointments have led to the Court's establishing new or rejecting "
     "existing precedents.'",
 12: "EK 2.9.A.2's causal chain in order: appointments, composition, ideology, precedent.",
 13: "EK 2.9.A.2 applied to a scenario, and compatible with EK 2.9.A.1 rather than a "
     "refutation of it.",
 14: "EK 2.9.A.2 tested by rebuttal, CED skill 5.D: a majority crossing appointing-party lines "
     "is what the composition explanation cannot easily account for.",
 15: "EK 2.9.A.2 with EK 2.5.A.2: composition determines future rules, and judicial "
     "appointments are the president's longest lasting influence.",
 16: "EK 2.9.A.1 and EK 2.9.A.2 held together: an important role plus occasional rejection.",
 17: "EK 2.9.A.1's similar-facts test as the FIRST question, before any question about "
     "whether to overrule.",
 18: "Federalist No. 78 (required document), 'bound down by strict rules and precedents,' "
     "quoted verbatim; the CED attaches Federalist No. 78 to 2.9.A.",
 19: "Federalist No. 78 (required document): independence answers the other branches, "
     "precedent answers the judges themselves. Two objections, one paper.",
 20: "EK 2.9.A.2's overruling as a SCOTUS-comparison item; the non-required case is described "
     "in the stem per CED p. 29 and is not named.",
 21: "Data item on a labelled hypothetical; the dominance of the followed column is "
     "recomputed below.",
 22: "EK 2.9.A.1 measured: the court follows the governing precedent in between about "
     "three quarters and seven eighths of dispositions.",
 23: "EK 2.9.A.1's similar-facts condition read against the data: distinctions grow far more "
     "than overrulings, and a distinction respects the precedent.",
 24: "Data item on a labelled hypothetical; both series' rise is recomputed below.",
 25: "EK 2.9.A.2 measured: turnover in membership paired with rejected precedents.",
 26: "Data item, CED skill 3.E: two series rising together cannot separate composition from a "
     "period in which many precedents were ripe for reconsideration.",
 27: "EK 2.9.A.1 and EK 2.9.A.2 reconciled: the ordinary case and the exception.",
 28: "EK 2.9.A.1's doctrine as a CONSTRAINT: following a rule one would not have adopted is "
     "what makes it a doctrine rather than a preference.",
 29: "EK 2.9.A.1 operationalized: the measure must condition on a precedent actually "
     "governing.",
 30: "EK 2.9.A.2 operationalized: turnover coinciding with the change, and a comparable "
     "caseload, are jointly what rule out the merits explanation.",
}

FOLLOW, DISTING, OVERRULE = ("Followed the precedent", "Distinguished the case",
                             "Overruled the precedent")
DECADES = ["First", "Second", "Third", "Fourth"]
RECENT, REJECTED = ("Members appointed within the preceding decade", "Precedents rejected")
PERIODS = ["First period", "Second period", "Third period"]

TABLE_CHECKS = {
 21: [
  ("following outnumbers distinctions and overrulings COMBINED in every decade -- by "
   "6.8 to one in the first decade and still 2.8 to one in the fourth, so the ratio "
   "narrows without ever reversing",
   lambda t: all(uc.cell(t, d, FOLLOW)
                 > 2.5 * (uc.cell(t, d, DISTING) + uc.cell(t, d, OVERRULE))
                 for d in DECADES)),
  ("overrulings never approach the followed count, so 'overruled more than it "
   "followed' is false in every decade",
   lambda t: all(uc.cell(t, d, OVERRULE) < uc.cell(t, d, FOLLOW) for d in DECADES)),
  ("the followed count FALLS across the four decades, so 'rose' is false",
   lambda t: uc.cell(t, DECADES[3], FOLLOW) < uc.cell(t, DECADES[0], FOLLOW)),
  ("distinctions occur in every decade and always exceed overrulings, so the last two "
   "distractors are both false",
   lambda t: all(uc.cell(t, d, DISTING) > uc.cell(t, d, OVERRULE) > 0
                 for d in DECADES)),
 ],
 22: [
  ("the followed share runs from 87 percent down to 74 percent of dispositions, so it "
   "is a large majority in every decade -- note 74, not the 80 a careless reading of "
   "the first decade would generalise to",
   lambda t: all(0.73 < uc.cell(t, d, FOLLOW)
                 / (uc.cell(t, d, FOLLOW) + uc.cell(t, d, DISTING)
                    + uc.cell(t, d, OVERRULE)) < 0.88 for d in DECADES)),
  ("overrulings are under 3 percent of dispositions in every decade, far too small to "
   "be the table's story",
   lambda t: all(uc.cell(t, d, OVERRULE)
                 / (uc.cell(t, d, FOLLOW) + uc.cell(t, d, DISTING)
                    + uc.cell(t, d, OVERRULE)) < 0.03 for d in DECADES)),
 ],
 23: [
  ("distinctions rise by 50 while overrulings rise by only 6 -- and overrulings FALL "
   "in the last decade, so 'rose in every decade' is false",
   lambda t: uc.cell(t, DECADES[3], DISTING) - uc.cell(t, DECADES[0], DISTING) == 50
   and uc.cell(t, DECADES[3], OVERRULE) - uc.cell(t, DECADES[0], OVERRULE) == 6
   and uc.cell(t, DECADES[3], OVERRULE) < uc.cell(t, DECADES[2], OVERRULE)),
  ("the followed count falls rather than rises, so that distractor is false too",
   lambda t: uc.cell(t, DECADES[3], FOLLOW) < uc.cell(t, DECADES[0], FOLLOW)),
  ("a distinctions column exists and four decades are reported, so the last two "
   "distractors are false on the table's face",
   lambda t: DISTING in t["headers"] and len(t["rows"]) == 4),
 ],
 24: [
  ("both series rise across all three periods",
   lambda t: uc.col(t, RECENT) == sorted(uc.col(t, RECENT))
   and uc.col(t, REJECTED) == sorted(uc.col(t, REJECTED))
   and len(set(uc.col(t, RECENT))) == 3),
  ("only the third period reaches a majority of a nine member court, so 'a majority in "
   "every period' is false",
   lambda t: sum(1 for p in PERIODS if uc.cell(t, p, RECENT) >= 5) == 1),
  ("rejections differ in every period and none is zero, so the last two distractors "
   "are false",
   lambda t: len(set(uc.col(t, REJECTED))) == 3 and min(uc.col(t, REJECTED)) > 0),
 ],
 25: [
  ("recent appointments and rejections rise together, six against fourteen by the "
   "third period, which is the pairing EK 2.9.A.2 describes",
   lambda t: uc.cell(t, PERIODS[2], RECENT) == 6
   and uc.cell(t, PERIODS[2], REJECTED) == 14),
  ("no column reports how precedent was followed, force, will or judicial review, so "
   "the four distractors name statements the table does not measure",
   lambda t: [h for h in t["headers"][1:]] == [RECENT, REJECTED]),
 ],
 26: [
  ("the two series move in the SAME direction, so the 'opposite directions' distractor "
   "misdescribes the table it is attached to",
   lambda t: (uc.cell(t, PERIODS[2], RECENT) > uc.cell(t, PERIODS[0], RECENT))
   == (uc.cell(t, PERIODS[2], REJECTED) > uc.cell(t, PERIODS[0], REJECTED))),
  ("both columns and three periods are present, and the cells are counts rather than "
   "percentages",
   lambda t: REJECTED in t["headers"] and len(t["rows"]) == 3
   and all(c.isdigit() for row in t["rows"] for c in row[1:])),
  ("nothing in the table describes the cases themselves, which is the gap the key "
   "names",
   lambda t: len(t["headers"]) == 3),
 ],
}


def _causal_chain(module):
    """EK 2.9.A.2 names one cause. No key may substitute a different one."""
    wrong = ("public opinion", "opinion polls", "congress directed", "constitutional amendment "
             "requiring", "instructions issued by congress")
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        why = item["why"].lower()
        if "reject" not in key and "overrul" not in key and "new precedent" not in key:
            continue
        for w in wrong:
            if w in key:
                bad.append(f"q{i} key: attributes precedential change to {w!r}; EK 2.9.A.2 "
                           "names ideological changes in composition due to presidential "
                           "appointments")
        # The rationale may mention the wrong causes only to reject them.
        for w in wrong:
            if w in why and not any(n in why for n in ("not ", "does not", "rather than")):
                bad.append(f"q{i} why: attributes precedential change to {w!r} without "
                           "rejecting it")
    if bad:
        print(f"FAIL {module.__name__} causal chain")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} causal chain: no key attributes precedential change to "
          "public opinion, Congress or amendment; EK 2.9.A.2's cause is composition")


ua.check(v2_9, ANCHORS, GROUNDING)
ua.notation(v2_9)
_causal_chain(v2_9)
uc.check(v2_9, TABLE_CHECKS)

# WHAT THE REVIEW FOUND
# ---------------------
# No wrong key. The design decision worth recording is the shape of the
# precedent table in items 21 to 23.
#
# It would have been easier to build it with two columns, followed and
# overruled, and the items would still have worked. It has three, because
# EK 2.9.A.1's condition is SIMILAR FACTS and that condition creates a third
# disposition -- distinguishing -- which is the one courts actually reach for
# most often after following. A student who has been taught only "follow" and
# "overrule" looks at a court whose distinctions nearly doubled and concludes it
# has been abandoning precedent, when a distinction is a court respecting a
# precedent and confining it to its facts.
#
# So the table's growing column is distinctions (58 to 108) while overrulings go
# 3, 6, 11 and back down to 9, and item 23 is the item that makes the reader
# notice which column moved. The checks recompute both, including the fall in
# the last decade, so a distractor claiming overrulings rose throughout is
# provably false rather than merely disfavoured.
#
# One rationale corrected by running the checks: item 22's `why` said the court
# follows precedent in "roughly four of every five dispositions." The share runs
# 87, 84, 77 and 74 percent, so four in five is right at the start of the series
# and wrong by the end. It now says between about three quarters and seven
# eighths, and the check asserts both bounds. The same generalise-from-the-first-
# row habit is how a table's opening figure quietly becomes a claim about the
# whole table.
