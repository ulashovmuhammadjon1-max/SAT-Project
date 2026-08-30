"""Structural gate for AP U.S. Government 2.11 Checks on the Judicial Branch.

ANCHORS, GROUNDING and the notation check via usgov_anchor, then usgov_check
with the six data items recomputed from their own tables.

ACTIVISM AND RESTRAINT ARE NOT IDEOLOGICAL LABELS, AND THIS FILE CHECKS IT
---------------------------------------------------------------------------
Both of EK 2.11.A.1's definitions are assertions ABOUT JUDICIAL REVIEW.
Activism asserts review ALLOWS courts to overturn precedent or invalidate acts;
restraint asserts review SHOULD BE CONSTRAINED to decisions adhering to
precedent. Neither mentions ideology, neither belongs to a party, and neither
is defined by which side of a case wins.

Outside the framework the two words are used as political epithets, and that
usage is what a bank drifts into without noticing. _not_ideological below fails
the module if any key or rationale attaches either term to a party or to a
political direction. Item 7 makes the correction itself the question, and item
8 is built so the two activist decisions point in OPPOSITE political directions
-- a student who has learned the epithet cannot answer it.

THE FIVE RESTRICTIONS, AND THE TWO THAT GET CONFLATED
-------------------------------------------------------
EK 2.11.B.1 is a closed list of five. Two pairs are routinely collapsed:

  i vs v   Legislation modifying the IMPACT OF A PRIOR DECISION is backward
           looking; legislation REMOVING JURISDICTION over a class of appeals is
           forward looking. Item 18 separates them and item 27 states what each
           can reach.
  iv       Delay by the president or the states is on the list but is NOT A
           LEGAL POWER. It works for the reason Federalist No. 78 gives -- the
           judiciary commands neither the sword nor the purse. Items 16 and 28
           make that explicit rather than letting a student file delay
           alongside statutes and amendments.

_five_restrictions asserts all five appear in the module and that item 22, a
NOT-question over the list, has four distractors that really are on it.
"""
import usgov_anchor as ua
import usgov_check as uc
import v2_11

ANCHORS = {
 1: "ongoing debate over differing interpretations of judicial review",
 2: "allows the courts to overturn current constitutional and case precedent",
 3: "should be constrained to decisions that adhere to current constitutional",
 4: "How far judicial review permits a court to depart",
 5: "both overturned existing precedent and invalidated a legislative act",
 6: "adhered to current precedent rather than departing from it",
 7: "not as positions on any political question",
 8: "One striking down a regulation of business and one striking down a restriction on speech",
 9: "transfers decisions from a body voters chose to one they did not",
 10: "stays in force, and constitutional limits go unenforced",
 11: "cited on both sides of the activism debate",
 12: "Congressional legislation to modify the impact of prior Supreme Court decisions",
 13: "Ratification of a constitutional amendment",
 14: "shift the ideological balance of the court, changing which decisions",
 15: "Delay implementation of the decision",
 16: "It is not a legal power at all",
 17: "removing the Court's jurisdiction over a case",
 18: "The first changes what an existing decision accomplishes",
 19: "modify the impact of a prior Supreme Court decision",
 20: "cannot be undone by statute",
 21: "drew no response at all, and the constitutional amendment route was used least",
 22: "since no row concerns the court's composition",
 23: "a court anticipating a response may decide differently",
 24: "least widely held and the most associated with saying the court has too much power",
 25: "confine departures from precedent to conflicts with the constitutional text",
 26: "pairs with the highest share saying the court has too much power",
 27: "only an amendment can change the effect of a decision interpreting the Constitution",
 28: "The president and states delaying implementation",
 29: "argue publicly about whether a recent decision exceeded the proper scope",
 30: "successfully used one of the listed restrictions to change the outcome",
}

GROUNDING = {
 1: "EK 2.11.A.1, verbatim: political discussion about the Court's power 'is illustrated by "
    "the ongoing debate over differing interpretations of judicial review.'",
 2: "EK 2.11.A.1.i, verbatim: judicial activism 'asserts that judicial review allows the "
    "courts to overturn current Constitutional and case precedent or invalidate legislative "
    "or executive acts.'",
 3: "EK 2.11.A.1.ii, verbatim: judicial restraint 'asserts that judicial review should be "
    "constrained to decisions that adhere to current Constitutional and case precedent.'",
 4: "EK 2.11.A.1.i against EK 2.11.A.1.ii: both are assertions about the REACH of judicial "
    "review, which is what the disagreement is about.",
 5: "EK 2.11.A.1.i applied; the definition names exactly the two moves the decision made, and "
    "attaches the label to what the court did rather than to the outcome's direction.",
 6: "EK 2.11.A.1.ii applied; adhering to precedent is the definition, and private doubts are "
    "not a decision to invalidate.",
 7: "EK 2.11.A.1.i and EK 2.11.A.1.ii, neither of which mentions ideology or party. This is "
    "the topic's central correction.",
 8: "EK 2.11.A.1.i's definition turns on invalidation, not on direction -- which is why the "
    "keyed pair strikes down measures pointing opposite political ways.",
 9: "EK 2.11.A.1.i read for its strongest objection: invalidating the acts of elected "
    "officials moves the decision away from the electorate.",
 10: "EK 2.11.A.1.ii read for its strongest objection: constraining review to existing "
     "precedent makes an erroneous precedent self-perpetuating.",
 11: "Brown v. Board of Education (1954), required case, which the CED attaches to 2.11.A and "
     "2.11.B. CED holding: 'Race-based school segregation violates the Equal Protection "
     "Clause of the Fourteenth Amendment.'",
 12: "EK 2.11.B.1.i, verbatim: 'Congressional legislation to modify the impact of prior "
     "Supreme Court decisions.'",
 13: "EK 2.11.B.1.ii, verbatim: 'Ratification of a Constitutional amendment' -- the only item "
     "that changes the document the Court applies.",
 14: "EK 2.11.B.1.iii, verbatim: appointments and confirmations 'which may shift the "
     "ideological balance of the court'; EK 2.9.A.2 supplies the consequence.",
 15: "EK 2.11.B.1.iv, verbatim: 'The president and states delaying implementation of a Supreme "
     "Court decision.'",
 16: "EK 2.11.B.1.iv distinguished from the other four: delay is non-compliance, effective for "
     "the reason Federalist No. 78 gives -- the judiciary commands neither sword nor purse.",
 17: "EK 2.11.B.1.v, verbatim: 'Enacting legislation to limit the cases the Supreme Court can "
     "hear on appeal by removing the court's jurisdiction over a case.'",
 18: "EK 2.11.B.1.i against EK 2.11.B.1.v: backward-looking against forward-looking, which is "
     "why the framework lists them separately.",
 19: "EK 2.11.B.1.i applied to a statutory interpretation, which a legislature can answer by "
     "rewriting the statute.",
 20: "EK 2.11.B.1.i against EK 2.11.B.1.ii, and the reason for the difference: a statute "
     "cannot override the Constitution (Art. VI), so a constitutional holding needs Art. V.",
 21: "Data item on a labelled hypothetical; the no-response majority and the amendment minimum "
     "are recomputed below.",
 22: "EK 2.11.B.1's five restrictions mapped onto the table's rows; appointments alone have "
     "none, since an appointment responds to no particular decision.",
 23: "Data item, CED skill 3.E: a count of completed responses cannot capture anticipation.",
 24: "Data item on a labelled hypothetical; both the position shares and the second column are "
     "recomputed below.",
 25: "EK 2.11.A.1.ii located in a survey row: the narrowest of the four positions.",
 26: "Data item; the pairing of the most permissive position with the highest concern is "
     "recomputed below, and the rationale marks it as a correlation rather than an explanation.",
 27: "EK 2.11.B.1.i and EK 2.11.B.1.ii and what each can reach, resting on U.S. Constitution "
     "Art. VI's hierarchy.",
 28: "Federalist No. 78 (required document), 'no influence over either the sword or the "
     "purse,' quoted verbatim; the CED attaches Federalist No. 78 to 2.11.A and 2.11.B.",
 29: "LO 2.11.A (debate about the Court's power) against LO 2.11.B (actual limits on it) -- "
     "the two objectives this topic carries, kept separate.",
 30: "LO 2.11.B operationalized: count occasions when a listed restriction was used and "
     "changed the outcome.",
}

COUNT = "Number of decisions"
NONE_ROW = "No response; the decision stood as issued"
LEGIS = "New legislation modifying the decision's effect"
DELAY = "Implementation delayed by officials for more than two years"
JURIS = "Legislation removing the court's jurisdiction over such appeals"
AMEND = "A constitutional amendment ratified"
HELD, TOOMUCH = ("Respondents holding it (%)", "Also say the court has too much power (%)")
TEXTUAL = "Only where the precedent conflicts with the constitutional text"
UNWORK = "Where the precedent has proved unworkable in practice"
WHENEVER = "Whenever a majority of the court believes it was wrongly decided"
NEVER = "Never, under any circumstances"

TABLE_CHECKS = {
 21: [
  ("twenty-nine of fifty drew no response, which is a majority, and the amendment row "
   "is the smallest at one",
   lambda t: uc.cell(t, NONE_ROW, COUNT) == 29
   and sum(uc.col(t, COUNT)) == 50
   and uc.cell(t, NONE_ROW, COUNT) * 2 > sum(uc.col(t, COUNT))
   and uc.cell(t, AMEND, COUNT) == min(uc.col(t, COUNT))),
  ("legislation answered only twelve, so 'a majority answered by new legislation' is "
   "false",
   lambda t: uc.cell(t, LEGIS, COUNT) * 2 < sum(uc.col(t, COUNT))),
  ("delay is not the most common response, so that distractor is false",
   lambda t: uc.cell(t, DELAY, COUNT) < uc.cell(t, NONE_ROW, COUNT)),
  ("a no-response row exists and is the largest, so 'every decision drew some "
   "response' is false on the table's face",
   lambda t: uc.cell(t, NONE_ROW, COUNT) == max(uc.col(t, COUNT))),
 ],
 22: [
  ("four of EK 2.11.B.1's five restrictions have a row -- legislation, delay, "
   "jurisdiction removal, amendment",
   lambda t: all(any(k in lab.lower() for lab in uc.labels(t))
                 for k in ("legislation modifying", "delayed", "jurisdiction",
                           "amendment"))),
  ("no row mentions appointments, confirmations or the court's composition, which is "
   "why the fifth restriction is the answer",
   lambda t: not any(k in lab.lower() for lab in uc.labels(t)
                     for k in ("appoint", "confirm", "composition", "balance"))),
 ],
 23: [
  ("a no-response row IS present, so 'omits decisions that drew no response' is false",
   lambda t: NONE_ROW in uc.labels(t)),
  ("the counts sum to fifty, the number the stem states, so nothing is missing and "
   "the column is counts rather than percentages",
   lambda t: sum(uc.col(t, COUNT)) == 50),
  ("the table has five rows, so 'covers a single decision' is false",
   lambda t: len(t["rows"]) == 5),
 ],
 24: [
  ("the most permissive position is 18 percent -- not the largest -- and carries the "
   "highest figure in the second column at 58",
   lambda t: uc.cell(t, WHENEVER, HELD) == 18
   and uc.cell(t, WHENEVER, HELD) < uc.cell(t, TEXTUAL, HELD)
   and uc.cell(t, WHENEVER, TOOMUCH) == max(uc.col(t, TOOMUCH))),
  ("the never row is the SMALLEST at 9, so 'most widely held' is false",
   lambda t: uc.cell(t, NEVER, HELD) == min(uc.col(t, HELD))),
  ("two positions fall below a quarter, so 'every position above a quarter' is false",
   lambda t: sum(1 for lab in uc.labels(t) if uc.cell(t, lab, HELD) < 25) == 2),
  ("the second column spans 19 to 58, so 'similar levels of concern' is false",
   lambda t: max(uc.col(t, TOOMUCH)) - min(uc.col(t, TOOMUCH)) == 39),
  ("the first column sums to 100, so the positions are a complete distribution",
   lambda t: sum(uc.col(t, HELD)) == 100),
 ],
 25: [
  ("the textual row is the narrowest of the four positions, which is what makes it "
   "the restraint row",
   lambda t: uc.labels(t)[0] == TEXTUAL and uc.cell(t, TEXTUAL, HELD) == 39),
  ("the whenever row is the permissive one and is a different row, so the two are not "
   "the same position",
   lambda t: uc.cell(t, WHENEVER, HELD) != uc.cell(t, TEXTUAL, HELD)),
 ],
 26: [
  ("the most permissive position pairs with the HIGHEST second-column figure, which is "
   "what the commentator claims",
   lambda t: uc.cell(t, WHENEVER, TOOMUCH) == max(uc.col(t, TOOMUCH))),
  ("the second column is NOT identical across positions, so that distractor "
   "misdescribes the table",
   lambda t: len(set(uc.col(t, TOOMUCH))) == 4),
  ("a second measure does exist, so 'the table reports no second measure' is false",
   lambda t: TOOMUCH in t["headers"]),
  ("the permissive position is not the most widely held, so the 'only because' "
   "distractor rests on a false premise",
   lambda t: uc.cell(t, WHENEVER, HELD) < max(uc.col(t, HELD))),
 ],
}


def _not_ideological(module):
    """EK 2.11.A.1 defines activism and restraint without reference to politics."""
    party = ("liberal", "conservative", "democrat", "republican", "left wing",
             "right wing", "progressive judges")
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        for label, s in (("key", item["choices"][item["ans"]]), ("why", item["why"])):
            low = s.lower()
            if "activis" not in low and "restraint" not in low:
                continue
            for word in party:
                if word in low and not any(n in low for n in ("not ", "neither", "any ")):
                    bad.append(f"q{i} {label}: ties activism or restraint to {word!r}; "
                               "EK 2.11.A.1 defines both without reference to ideology")
    if bad:
        print(f"FAIL {module.__name__} not ideological")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} not ideological: no key or rationale ties judicial activism "
          "or restraint to a party or political direction")


def _five_restrictions(module):
    """All five of EK 2.11.B.1 must appear, and item 22's distractors must be real."""
    five = ("legislation to modify the impact", "constitutional amendment",
            "appointments and confirmations", "delaying implementation",
            "removing the court's jurisdiction")
    blob = " ".join(it["q"] + " " + it["why"] + " " + " ".join(it["choices"])
                    for it in module.QUESTIONS).lower()
    bad = [f"EK 2.11.B.1 restriction {r!r} appears nowhere in the module"
           for r in five if r not in blob]
    q22 = module.QUESTIONS[21]
    for k, c in enumerate(q22["choices"]):
        low = c.lower()
        on_list = any(k2 in low for k2 in ("legislation", "amendment", "delay",
                                           "jurisdiction", "appointments"))
        if not on_list:
            bad.append(f"q22: choice {'ABCDE'[k]} names nothing on EK 2.11.B.1's list, so a "
                       "NOT-question over that list has two defensible keys")
    if bad:
        print(f"FAIL {module.__name__} five restrictions")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} five restrictions: all five of EK 2.11.B.1 appear, and every "
          "choice in item 22 names one of them")


ua.check(v2_11, ANCHORS, GROUNDING)
ua.notation(v2_11)
_not_ideological(v2_11)
_five_restrictions(v2_11)
uc.check(v2_11, TABLE_CHECKS)

# WHAT THE REVIEW FOUND
# ---------------------
# No wrong key. Two things are worth recording, and both are about words that
# mean one thing in the CED and something else in ordinary political speech.
#
#   * ACTIVISM and RESTRAINT. Outside the framework these are epithets, and the
#     epithet has a political direction attached: activist judges are the other
#     side's judges. EK 2.11.A.1 defines both purely as assertions about what
#     judicial review permits, with no ideology in either sentence. Item 8 is
#     built to make the difference operative -- its keyed pair contains one
#     decision striking down a business regulation and one striking down a speech
#     restriction, which point opposite political ways and are both activist on
#     the framework's definition. A student carrying the epithet cannot answer
#     it, which is the point.
#   * DELAY. EK 2.11.B.1.iv puts "the president and states delaying
#     implementation" on a list otherwise made of statutes, amendments and
#     appointments. It is the one item that is not an exercise of any granted
#     power -- it is simply non-compliance, and it works for the reason
#     Federalist No. 78 states. Item 16 asks the student to notice that the list
#     is not homogeneous, because filing delay alongside the formal instruments
#     teaches that the Constitution authorizes ignoring a court.
