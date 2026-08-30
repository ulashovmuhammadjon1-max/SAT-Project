"""Structural gate for AP U.S. Government 2.10 The Court in Action.

ANCHORS, GROUNDING and the notation check via usgov_anchor, then usgov_check
with the six data items recomputed from their own tables.

THE TITLE IS A TRAP AND THIS FILE CHECKS FOR IT
------------------------------------------------
"The Court in Action" sounds like it should cover how cases reach the Court:
certiorari, the rule of four, oral argument, opinion assignment. The framework
covers none of that -- it never mentions certiorari anywhere -- and EK 2.10.A.1
is this topic's ONLY essential-knowledge statement, entirely about LIFE TENURE.
See AP_US_GOV_CED.md note 3.

That makes this the easiest topic in the unit to pollute with off-syllabus
content, because the off-syllabus content is what a teacher would naturally
reach for and what most textbooks put under this heading. _on_syllabus below
fails the module if any key or rationale turns on certiorari, the rule of four,
oral argument or opinion assignment. It is a check against the author's own
instincts rather than against a typo.

EK 2.10.A.1 IS A THREE-LINK CHAIN AND THE VERBS ARE PERMISSIVE
----------------------------------------------------------------
    life tenure ALLOWS the court to function independent of the political
    climate -> as a result the Court CAN deliver controversial or unpopular
    decisions -> which CAN LEAD TO debate about the court's power.

Both hinges are "can". Neither is asserted as inevitable, and item 29 keys on
exactly that: a student who reads ALLOWS as GUARANTEES has misread the only
sentence this topic has. _permissive below asserts no key states either link as
a certainty, and items 27 and 28 attack the first and third links separately,
which is only meaningful because they are separable claims.
"""
import usgov_anchor as ua
import usgov_check as uc
import v2_10

ANCHORS = {
 1: "independent of the current political climate",
 2: "Tenure that does not expire, and a salary that may not be reduced",
 3: "punish the judges financially without removing them",
 4: "has a reason to avoid ruling against the government",
 5: "without risking removal from office",
 6: "impeached by the House and removed on conviction",
 7: "permanence in office is what makes judicial independence possible",
 8: "also lets it persist in an unpopular course indefinitely",
 9: "can deliver controversial or unpopular decisions",
 10: "which no elected body would readily impose on itself",
 11: "struck down a popular federal statute",
 12: "United States v. Lopez (1995), because there too the Court held that Congress had exceeded",
 13: "Baker v. Carr (1962), in which the Court held that federal courts may hear challenges",
 14: "since a popular decision needs no insulation",
 15: "rules against a policy supported by large majorities",
 16: "consistently align with the position of whichever party controls",
 17: "Debate about the court's power",
 18: "that EK 2.10.A.1 says unpopular decisions can provoke",
 19: "attaches a justice's interest to the office",
 20: "shapes the Court's decisions for three decades or more",
 21: "ruled against it far more often than courts whose judges can be",
 22: "secure tenure allows a court to function independent",
 23: "may differ from others in many ways",
 24: "Approval fell by seventeen points and disapproval rose by nineteen",
 25: "since public support is what such debate draws on",
 26: "despite the cost to its public standing",
 27: "vote in line with the preferences of the presidents who appointed them",
 28: "have not been preceded by unusually unpopular decisions",
 29: "which is a claim about what becomes possible rather than about what must occur",
 30: "and does public criticism of a court follow its least popular decisions",
}

GROUNDING = {
 1: "EK 2.10.A.1, verbatim: 'Life tenure for justices allows the court to function independent "
    "of the current political climate.' The first link of three.",
 2: "U.S. Constitution Art. III Sec. 1, quoted verbatim: tenure during good behavior and "
    "compensation that shall not be diminished during continuance in office.",
 3: "U.S. Constitution Art. III Sec. 1's compensation clause read structurally: tenure "
    "protects the office, the salary clause protects its value.",
 4: "EK 2.10.A.1's first link inverted -- a tenure controlled by the party being judged "
    "restores the incentive tenure removes.",
 5: "EK 2.10.A.1's phrase 'independent of the current political climate' as an institutional "
    "condition rather than a claim about a justice's knowledge or beliefs.",
 6: "EK 1.6.B.2 with U.S. Constitution Art. III Sec. 1: tenure runs during good behavior, and "
    "removal follows a House impeachment and a Senate conviction. Difficult, not impossible.",
 7: "Federalist No. 78 (required document), 'permanency in office... the citadel of the public "
    "justice,' quoted verbatim; the CED attaches Federalist No. 78 to 2.10.A.",
 8: "EK 2.10.A.1 read against itself: the insulation that permits an unpopular decision also "
    "removes the electoral correction. CED skill 5.D, rebuttal.",
 9: "EK 2.10.A.1's second link: 'As a result of this independence, the Court can deliver "
    "controversial or unpopular court decisions.'",
 10: "Baker v. Carr (1962), required case, which the CED attaches to 2.10.A. CED holding: "
     "redistricting did not raise political questions, allowing federal courts to hear "
     "challenges to districting plans.",
 11: "United States v. Lopez (1995), required case, which the CED attaches to 2.10.A. CED "
     "holding: Congress exceeded its power under the Commerce Clause.",
 12: "United States v. Lopez (1995) as a SCOTUS comparison, CED skill 2.C; the non-required "
     "case's facts are printed in the stem per CED p. 29 and it is not named.",
 13: "Baker v. Carr (1962) as a SCOTUS comparison, CED skill 2.C; a federal constitutional "
     "limit reaching a state practice.",
 14: "EK 2.10.A.1's phrase 'controversial or unpopular', which locates precisely where "
     "independence is load-bearing.",
 15: "EK 2.10.A.1's second link illustrated; the fourth and fifth distractors illustrate "
     "checks ON the Court, which is EK 2.11.B's subject rather than this one's.",
 16: "EK 2.10.A.1's first link operationalized: independence is measured by whether outcomes "
     "track the government's position.",
 17: "EK 2.10.A.1's third link, verbatim: unpopular decisions 'can lead to debate about the "
     "court's power.' Debate, not any automatic consequence.",
 18: "EK 2.10.A.1's third link illustrated by proposals to restructure a court -- the debate "
     "taking institutional form without any change in authority.",
 19: "Federalist No. 51 (required document), 'Ambition must be made to counteract ambition,' "
     "quoted verbatim; the CED attaches Federalist No. 51 to 2.10.A.",
 20: "EK 2.10.A.1's tenure read against EK 2.5.A.2, the president's longest lasting influence: "
     "the argument is about DURATION.",
 21: "Data item on a labelled hypothetical; the two secure-tenure rows are compared with the "
     "two government-controlled rows below.",
 22: "EK 2.10.A.1's FIRST link measured: tenure rule against rate of ruling against the "
     "government.",
 23: "Data item, CED skill 3.E: a cross-national comparison cannot isolate one institutional "
     "feature from everything else that differs.",
 24: "Data item on a labelled hypothetical; both movements are recomputed below.",
 25: "EK 2.10.A.1's THIRD link measured: what happens to public standing after an unpopular "
     "decision, which is what debate about the court's power draws on.",
 26: "EK 2.10.A.1's second link seen as a price paid: the court issued the decision and lost "
     "seventeen points of approval.",
 27: "EK 2.10.A.1's first link tested by rebuttal, CED skill 5.D: outcomes tracking the "
     "appointing president would show tenure had not produced independence.",
 28: "EK 2.10.A.1's third link tested by rebuttal, and note the framework's CAN LEAD TO -- "
     "occasional exceptions do not refute a permissive claim.",
 29: "EK 2.10.A.1's verbs: ALLOWS and CAN at every hinge. A capacity, not a certainty.",
 30: "EK 2.10.A.1 as a whole: testing a three-link chain means measuring the first and third "
     "links together.",
}

COURTS, AGAINST = "Number of courts", "Decisions against the government (%)"
SECURE = ["Tenure until a fixed retirement age", "Single long term, not renewable"]
CONTROLLED = ["Fixed term, renewable by the government",
              "Term at the pleasure of the government"]
BEFORE, AFTER = "Before the decision (%)", "After the decision (%)"
APP, DIS, NOOP = "Approve of the court", "Disapprove of the court", "No opinion"

TABLE_CHECKS = {
 21: [
  ("every secure-tenure row exceeds every government-controlled row, by at least "
   "twenty points",
   lambda t: min(uc.cell(t, r, AGAINST) for r in SECURE)
   - max(uc.cell(t, r, AGAINST) for r in CONTROLLED) >= 20),
  ("the at-pleasure row is the LOWEST, not the highest, so that distractor reverses "
   "the table",
   lambda t: uc.cell(t, CONTROLLED[1], AGAINST) == min(uc.col(t, AGAINST))),
  ("the four rates span 4 to 34 percent, so 'similar rates' is false",
   lambda t: max(uc.col(t, AGAINST)) - min(uc.col(t, AGAINST)) == 30),
  ("the largest group is the six courts with tenure to a retirement age, not the "
   "renewable-term group",
   lambda t: uc.cell(t, SECURE[0], COURTS) == max(uc.col(t, COURTS))
   and uc.cell(t, SECURE[0], COURTS) > uc.cell(t, CONTROLLED[0], COURTS)),
  ("two rows exceed a fifth, so 'no group above a fifth' is false",
   lambda t: sum(1 for r in uc.labels(t) if uc.cell(t, r, AGAINST) > 20) == 2),
 ],
 22: [
  ("the table pairs a TENURE RULE with an outcome, which is what makes it a test of "
   "EK 2.10.A.1's first link rather than of the second or third",
   lambda t: "Tenure rule" == t["headers"][0] and AGAINST in t["headers"]),
  ("no column reports precedent, popularity or public criticism, so the distractors "
   "naming those claims cite data the table does not carry",
   lambda t: not any(k in h.lower() for h in t["headers"]
                     for k in ("precedent", "popular", "criticism"))),
 ],
 23: [
  ("all four tenure groups and both columns are present, so three distractors are "
   "false on the table's face",
   lambda t: len(t["rows"]) == 4 and COURTS in t["headers"] and AGAINST in t["headers"]),
  ("the groups DO differ, by thirty points between the extremes, so 'shows no "
   "difference' is false",
   lambda t: max(uc.col(t, AGAINST)) > min(uc.col(t, AGAINST))),
  ("the outcome column is a percentage, so 'counts rather than percentages' is false",
   lambda t: "%" in AGAINST),
 ],
 24: [
  ("approval falls seventeen points and disapproval rises nineteen",
   lambda t: uc.cell(t, APP, BEFORE) - uc.cell(t, APP, AFTER) == 17
   and uc.cell(t, DIS, AFTER) - uc.cell(t, DIS, BEFORE) == 19),
  ("disapproval RISES, so 'both fell' is false",
   lambda t: uc.cell(t, DIS, AFTER) > uc.cell(t, DIS, BEFORE)),
  ("approval ends below half, so 'a majority still approved' is false",
   lambda t: uc.cell(t, APP, AFTER) < 50),
  ("the no-opinion share falls by two points, so 'rose sharply' is false",
   lambda t: uc.cell(t, NOOP, AFTER) < uc.cell(t, NOOP, BEFORE)),
  ("approval led disapproval by thirty-one points beforehand, so 'disapproval "
   "exceeded approval before' is false",
   lambda t: uc.cell(t, APP, BEFORE) - uc.cell(t, DIS, BEFORE) == 31),
  ("both columns sum to 100, so each is a complete distribution",
   lambda t: all(sum(uc.col(t, c)) == 100 for c in (BEFORE, AFTER))),
 ],
 25: [
  ("the table measures public standing BEFORE and AFTER a decision, which is the "
   "third link, and reports nothing about tenure, which is the first",
   lambda t: [h for h in t["headers"][1:]] == [BEFORE, AFTER]
   and not any("tenure" in h.lower() for h in t["headers"])),
  ("the movement is large enough to be the subject of debate: a net swing of "
   "thirty-six points between approval and disapproval",
   lambda t: (uc.cell(t, APP, BEFORE) - uc.cell(t, APP, AFTER))
   + (uc.cell(t, DIS, AFTER) - uc.cell(t, DIS, BEFORE)) == 36),
 ],
 26: [
  ("approval fell rather than rose, so the 'expected approval to rise' distractor is "
   "contradicted by the table",
   lambda t: uc.cell(t, APP, AFTER) < uc.cell(t, APP, BEFORE)),
  ("the standing changed substantially, so 'unaffected' is false",
   lambda t: abs(uc.cell(t, APP, AFTER) - uc.cell(t, APP, BEFORE)) > 10),
  ("the table records only two moments and no reversal or loss of office, so the last "
   "two distractors describe events outside these data entirely",
   lambda t: len(t["headers"]) == 3),
 ],
}


def _on_syllabus(module):
    """2.10 is about life tenure. Certiorari and friends are off-syllabus here."""
    off = ("certiorari", "rule of four", "writ of cert", "oral argument",
           "opinion assignment", "docket")
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        blob = (item["q"] + " " + item["why"] + " "
                + " ".join(item["choices"])).lower()
        for term in off:
            if term in blob:
                bad.append(f"q{i}: mentions {term!r}; the framework never discusses it and "
                           "EK 2.10.A.1 is entirely about life tenure "
                           "(AP_US_GOV_CED.md note 3)")
    if bad:
        print(f"FAIL {module.__name__} on syllabus")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} on syllabus: no item turns on certiorari, the rule of four, "
          "oral argument or opinion assignment, none of which the CED contains")


def _permissive(module):
    """EK 2.10.A.1's hinges are ALLOWS and CAN. No key may state them as certainties."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        if "life tenure" not in key and "tenure" not in key:
            continue
        for word in ("guarantees", "ensures that the court will", "always rules",
                     "must rule independently"):
            if word in key:
                bad.append(f"q{i} key: states EK 2.10.A.1's permissive claim as a certainty "
                           f"({word!r}); the framework's verb is ALLOWS")
    if bad:
        print(f"FAIL {module.__name__} permissive")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} permissive: no key states life tenure as guaranteeing "
          "independence; EK 2.10.A.1 says ALLOWS and CAN at every hinge")


ua.shape(v2_10)
ua.check(v2_10, ANCHORS, GROUNDING)
ua.notation(v2_10)
_on_syllabus(v2_10)
_permissive(v2_10)
uc.check(v2_10, TABLE_CHECKS)

# WHAT THE REVIEW FOUND
# ---------------------
# No wrong key. The check worth explaining is _on_syllabus, which is unlike
# every other check in this bank: it does not guard against an error, it guards
# against the author knowing too much.
#
# "The Court in Action" is a heading under which every textbook puts the
# certiorari process, the rule of four, oral argument and opinion assignment.
# The CED puts none of it there. The framework does not mention certiorari
# anywhere at all, and this topic has exactly one essential-knowledge statement,
# about life tenure (AP_US_GOV_CED.md note 3). An item about how four justices
# vote to grant review would look completely at home in this module and would be
# off-syllabus -- a student who got it wrong would have been failed by the bank,
# and a student who got it right would have learned nothing the exam tests.
#
# So the check names the four temptations explicitly and fails the module if any
# of them appears. It exists because the mistake it prevents is one a
# well-informed author makes and a poorly-informed one never would.
