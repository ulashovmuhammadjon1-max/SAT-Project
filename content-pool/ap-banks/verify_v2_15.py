"""Structural gate for AP U.S. Government 2.15 Policy and the Branches of Government.

ANCHORS, GROUNDING, shape and notation via usgov_anchor, then usgov_check with
NINE data items recomputed from three tables. Nine because the suggested CED
skill here (p. 75) is 3.D -- explain what the data IMPLIES OR ILLUSTRATES --
which is a step past description and needs items that ask what a pattern means.

THE THREE-WAY OVERLAP, AND WHY THIS FILE POLICES IT
-----------------------------------------------------
The framework states an access-point claim three times:

    EK 1.6.B.1   separation of powers and checks and balances   -> v1_6
    EK 1.9.A.1   federalism, i.e. levels of government          -> v1_9
    EK 2.15.B.1  the three branches, in a policymaking unit     -> this module

and a constraint claim twice (EK 1.9.A.2 for levels, EK 2.15.B.2 for branches).
All are examinable and none may be tested twice under different topic codes, so
the boundary has to be enforced rather than intended. _branches_not_levels below
fails the module if any key or rationale uses a STATE or LOCAL government as its
additional venue -- that is v1_9's territory. Item 12 turns the three-way
distinction into a question, which is the honest way to handle content that
genuinely does appear three times.

"THE EXTENT TO WHICH" IS THE OTHER HALF OF THE TOPIC
------------------------------------------------------
LO 2.15.A does not ask whether the branches can hold the bureaucracy
accountable. It asks HOW FAR they can, GIVEN THE COMPETING INTERESTS of the
three. That phrasing invites an answer most banks will not write: three
principals pulling one agency in three directions can leave it LESS controlled
than one would, because inconsistent instructions are themselves discretion.
Item 8 keys on exactly that, and _extent asserts that no key in this module
treats overlapping controls as automatically additive.

THE DELAY TABLE IS THE UNIT'S CLOSING ARGUMENT
------------------------------------------------
Items 26 to 28 pair the number of branches contesting a policy with the time it
took to take effect: 6, 14, 29, 47 months. Item 28 asks what that implies about
the relationship between the two EK 2.15.B statements, and the answer is that
the venue and the obstacle are the same institution seen from two sides. That is
the point of stating both claims about one allocation of powers, and it is the
last thing Unit 2 has to say.
"""
import usgov_anchor as ua
import usgov_check as uc
import v2_15

ANCHORS = {
 1: "Formal and informal powers of Congress, the president, and the courts",
 2: "Congress appropriating or withholding an agency's funds",
 3: "publicly pressing an agency to change a policy he cannot lawfully order",
 4: "pressure and bargaining that no formal instrument records",
 5: "The courts, with holding an agency action unlawful; Congress, with the power of the purse",
 6: "their combined pressure is not simply the sum of three controls",
 7: "three principals whose demands do not align",
 8: "can leave it less controlled rather than more",
 9: "so supervision will be contested rather than coordinated",
 10: "whichever branch first identified the departure",
 11: "multiple access points for stakeholders and institutions to influence public policy",
 12: "the branches' distinct functions, the two levels of government",
 13: "the sharing of powers between the three branches",
 14: "That national policymaking is constrained by the sharing of powers",
 15: "the opportunity the structure creates for outside actors",
 16: "added the courts as a venue in which a policy adopted elsewhere can be contested",
 17: "each additional objecting branch adds a place where the policy can be delayed",
 18: "rests on broader agreement and is harder to reverse abruptly",
 19: "may go unaddressed because agreement among three institutions is difficult",
 20: "the executive branch is the only one with both a formal and an informal instrument",
 21: "over the bureaucracy are used to maintain accountability",
 22: "one instrument may matter far more than several others",
 23: "no venue produced change in even half the attempts",
 24: "creates multiple access points for influencing policy",
 25: "an organization able to use several has a better chance",
 26: "from six months to forty-seven",
 27: "constrained by the sharing of powers between the three branches",
 28: "are the places where a policy is delayed",
 29: "how often does the agency end up doing what any of them wanted",
 30: "contested rather than cumulative",
}

GROUNDING = {
 1: "EK 2.15.A.1, verbatim: 'Formal and informal powers of Congress, the president, and the "
    "courts over the bureaucracy are used to maintain its accountability.' Three branches, "
    "two kinds of power.",
 2: "EK 2.14.A.1.iii's power of the purse as a FORMAL power -- an authority the Constitution "
    "and statute confer, which is what the formal/informal line turns on.",
 3: "EK 2.4.A.2.iii's bargaining and persuasion as INFORMAL: influence exercised without any "
    "authority to command.",
 4: "EK 2.15.A.1 names both kinds because an account limited to statutes and court orders "
    "would miss most of the interaction.",
 5: "EK 2.15.A.1's three branches, each matched to an instrument it actually holds: judicial "
    "review, the appropriation power, appointment, hearings.",
 6: "LO 2.15.A's own phrase, 'given the competing interests of Congress, the president, and "
    "the federal courts', which is why the objective asks about EXTENT.",
 7: "EK 2.15.A.1 with LO 2.15.A: all three branches' powers reach the same agency at once, "
    "and their demands need not align.",
 8: "LO 2.15.A's 'extent to which' answered honestly: inconsistent instructions are themselves "
    "discretion, so overlapping controls are not additive.",
 9: "Federalist No. 51 (required document), 'Ambition must be made to counteract ambition,' "
    "quoted verbatim; the CED attaches Federalist No. 51 to 2.15.A. Madison's mechanism "
    "predicts contested rather than coordinated supervision.",
 10: "LO 2.15.A operationalized: effectiveness measured by corrected departures, with "
     "'whichever branch' addressing the competing-interests qualification directly.",
 11: "EK 2.15.B.1, verbatim: 'The allocation of powers among the three branches of government "
     "creates multiple access points for stakeholders and institutions to influence public "
     "policy.'",
 12: "EK 1.6.B.1, EK 1.9.A.1 and EK 2.15.B.1 distinguished -- branches' functions, levels of "
     "government, and the branches' joint role in policymaking. Three sentences, three "
     "multipliers, all examinable.",
 13: "EK 2.15.B.2, verbatim: 'National policymaking is constrained by the sharing of powers "
     "between the three branches.'",
 14: "EK 2.15.B.2 illustrated: an objective blocked in one branch, attempted in another, "
     "stopped by a third.",
 15: "EK 2.15.B.1 against EK 2.15.B.2: opportunity and constraint from one allocation of "
     "powers, the same pair EK 1.9.A.1 and EK 1.9.A.2 make about federalism.",
 16: "Marbury v. Madison (1803), required case, which the CED attaches to 2.15.B. CED "
     "holding: judicial review, empowering the Court to declare an act of the legislative or "
     "executive branch unconstitutional -- which makes the courts both a venue and an obstacle.",
 17: "EK 2.15.B.2's mechanism: shared powers mean action requires agreement, so each objecting "
     "branch adds a place to be stopped.",
 18: "EK 2.15.B.2 defended, via Federalist No. 51's logic: a policy satisfying three separately "
     "constituted institutions rests on a broader coalition.",
 19: "EK 2.15.B.2 attacked: the cost of delay when a timely response is needed.",
 20: "Data item on a categorical table; the branch and formality columns are recomputed below.",
 21: "EK 2.15.A.1 seen as data: three branches and both kinds of power in two columns.",
 22: "Data item, CED skill 3.E: counting rows in a curated list measures the list, and one "
     "holding can reach further than several hearings.",
 23: "Data item on a labelled hypothetical; both columns' leaders and the ceiling on success "
     "are recomputed below.",
 24: "EK 2.15.B.1 measured -- and note all four venues are NATIONAL institutions, which is "
     "what makes this the branches version rather than EK 1.9.A.1's federalism version.",
 25: "EK 2.15.B.1 stated as an implication, CED skill 3.D: low per-venue success is precisely "
     "what makes multiple access points valuable.",
 26: "Data item on a labelled hypothetical; the monotonic rise in delay is recomputed below.",
 27: "EK 2.15.B.2 measured: median time to take effect rising with each contesting branch.",
 28: "EK 2.15.B.1 and EK 2.15.B.2 as one fact, CED skill 3.D: a branch that contests a policy "
     "is a branch someone reached.",
 29: "LO 2.15.A operationalized at its hardest point -- condition on the branches disagreeing, "
     "then look at the outcome.",
 30: "LO 2.15.A's contribution to topics 2.12 through 2.14: the instruments described "
     "separately all operate at once on the same agency.",
}

BRANCH, KIND = "Branch", "Formal or informal"
USING, CHANGE = "Organizations using it (%)", "Produced some change (%)"
COMMENTS, STAFF = "Comments filed with the agency", "Congressional committee staff"
LEADERSHIP, COURT = "The agency's political leadership", "Litigation in federal court"
NPOL, MONTHS = "Number of policies", "Median months to take effect"
CONTEST = ["None", "One", "Two", "Three"]


def _cats(t, header):
    j = t["headers"].index(header)
    return [row[j] for row in t["rows"]]


TABLE_CHECKS = {
 20: [
  ("all three branches appear, and the executive is the only branch with both a "
   "formal and an informal instrument listed",
   lambda t: {"Legislative", "Executive", "Judicial"} == set(_cats(t, BRANCH))
   and {k for b, k in zip(_cats(t, BRANCH), _cats(t, KIND)) if b == "Executive"}
   == {"Formal", "Informal"}
   and all({k for b, k in zip(_cats(t, BRANCH), _cats(t, KIND)) if b == other}
           == {"Formal"} for other in ("Legislative", "Judicial"))),
  ("two rows are informal, so 'only formal instruments appear' and 'every instrument "
   "is informal' are both false",
   lambda t: _cats(t, KIND).count("Informal") == 2),
  ("the judiciary has ONE row, fewer than either other branch, so 'the most "
   "instruments' is false",
   lambda t: _cats(t, BRANCH).count("Judicial") == 1
   and _cats(t, BRANCH).count("Judicial") < _cats(t, BRANCH).count("Legislative")),
  ("the legislature has two FORMAL rows, so 'no formal instrument listed' is false",
   lambda t: sum(1 for b, k in zip(_cats(t, BRANCH), _cats(t, KIND))
                 if b == "Legislative" and k == "Formal") == 2),
 ],
 21: [
  ("the table's two columns are exactly EK 2.15.A.1's two dimensions, branch and "
   "formality",
   lambda t: [h for h in t["headers"][1:]] == [BRANCH, KIND]),
  ("no row concerns delegated discretion, hiring, iron triangles or compliance "
   "monitoring, so those distractors cite content the table does not carry",
   lambda t: not any(k in row[0].lower() for row in t["rows"]
                     for k in ("merit", "triangle", "compliance", "delegat"))),
 ],
 22: [
  ("the judicial row IS present, so 'omits the judicial branch' is false",
   lambda t: "Judicial" in _cats(t, BRANCH)),
  ("no column reports how often an instrument is used, so that distractor describes "
   "data not here",
   lambda t: not any("often" in h.lower() or "used" in h.lower() for h in t["headers"])),
  ("six rows across three branches, which is what makes any count an artifact of the "
   "selection",
   lambda t: len(t["rows"]) == 6),
 ],
 23: [
  ("agency comments lead BOTH columns, at 84 percent used and 37 percent producing "
   "change, and 37 is the ceiling -- under half",
   lambda t: uc.cell(t, COMMENTS, USING) == max(uc.col(t, USING))
   and uc.cell(t, COMMENTS, CHANGE) == max(uc.col(t, CHANGE))
   and max(uc.col(t, CHANGE)) < 50),
  ("litigation is the LEAST used and the LEAST effective, so both distractors naming "
   "it are false",
   lambda t: uc.cell(t, COURT, USING) == min(uc.col(t, USING))
   and uc.cell(t, COURT, CHANGE) == min(uc.col(t, CHANGE))),
  ("the four usage shares span 38 to 84, so 'similar shares' is false",
   lambda t: max(uc.col(t, USING)) - min(uc.col(t, USING)) == 46),
 ],
 24: [
  ("all four venues are NATIONAL -- an agency, congressional staff, the "
   "administration and a federal court -- which is what makes this the "
   "three-branches version rather than the federalism version",
   lambda t: not any(k in lab.lower() for lab in uc.labels(t)
                     for k in ("state", "local", "governor", "city"))),
  ("the venues span the executive, legislative and judicial branches",
   lambda t: {COMMENTS, LEADERSHIP} <= set(uc.labels(t))
   and STAFF in uc.labels(t) and COURT in uc.labels(t)),
 ],
 25: [
  ("no venue succeeds in as many as two fifths of attempts, which is what makes "
   "using several worth more than using one",
   lambda t: max(uc.col(t, CHANGE)) < 40),
  ("the usage column sums to 235 percent, so organizations plainly used more than one "
   "venue and the shares are not a distribution",
   lambda t: sum(uc.col(t, USING)) == 235 and sum(uc.col(t, USING)) != 100),
  ("the most used venue IS the most effective, which is true and does not make the "
   "others worthless -- the reason that distractor is tempting",
   lambda t: uc.cell(t, COMMENTS, USING) == max(uc.col(t, USING))
   and uc.cell(t, COMMENTS, CHANGE) == max(uc.col(t, CHANGE))),
 ],
 26: [
  ("the median rises with every additional contesting branch: 6, 14, 29, 47 months",
   lambda t: [uc.cell(t, c, MONTHS) for c in CONTEST] == [6, 14, 29, 47]),
  ("only five of seventy-eight policies were contested by all three, so 'most "
   "policies' is false",
   lambda t: uc.cell(t, "Three", NPOL) == 5 and sum(uc.col(t, NPOL)) == 78),
  ("the medians span 6 to 47 months, so 'similar regardless' is false and the longest "
   "exceeds two years",
   lambda t: max(uc.col(t, MONTHS)) > 24),
 ],
 27: [
  ("the independent variable is the NUMBER OF BRANCHES contesting, which is what makes "
   "the table a measure of EK 2.15.B.2's shared-powers constraint",
   lambda t: "Branches actively contesting" in t["headers"][0]),
  ("the increments grow -- 8, 15, 18 months -- so each additional branch costs more "
   "than the last",
   lambda t: [uc.cell(t, b, MONTHS) - uc.cell(t, a, MONTHS)
              for a, b in zip(CONTEST, CONTEST[1:])] == [8, 15, 18]),
 ],
 28: [
  ("every level of contestation appears, from none to three, so the table shows the "
   "whole range rather than only the contested cases",
   lambda t: [c for c in _cats(t, NPOL)] and uc.labels(t) == CONTEST),
  ("policies contested by nobody are the second largest group, so contestation is not "
   "universal and the venue/obstacle identity is a claim about the same institutions "
   "rather than about all policies",
   lambda t: uc.cell(t, "None", NPOL) == 24
   and uc.cell(t, "One", NPOL) == max(uc.col(t, NPOL))),
 ],
}


def _branches_not_levels(module):
    """EK 2.15.B is about BRANCHES. Levels of government belong to v1_9."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        if "access point" not in key and "venue" not in key:
            continue
        for word in ("state legislature", "state government", "local government",
                     "another state", "state agency"):
            if word in key:
                bad.append(f"q{i} key: uses {word!r} as an additional venue; that is "
                           "EK 1.9.A.1's federalism version, which v1_9 owns")
    if bad:
        print(f"FAIL {module.__name__} branches not levels")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} branches not levels: no access-point key uses a state or "
          "local government as its venue, so EK 2.15.B.1 is not tested as EK 1.9.A.1")


def _extent(module):
    """LO 2.15.A asks HOW FAR, given competing interests. No key may assume additivity."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        for phrase in ("guarantee tighter control", "guarantees tighter control",
                       "three controls are better than one",
                       "combined pressure is simply the sum"):
            if phrase in key:
                bad.append(f"q{i} key: treats overlapping controls as additive; LO 2.15.A "
                           "asks about the EXTENT of accountability given competing interests")
    q8 = module.QUESTIONS[7]
    if "less controlled" not in q8["choices"][q8["ans"]].lower():
        bad.append("q8: the item that carries LO 2.15.A's hardest conclusion -- that "
                   "conflicting controls can leave an agency LESS controlled -- no longer "
                   "states it")
    if bad:
        print(f"FAIL {module.__name__} extent")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} extent: no key treats three overlapping controls as "
          "additive, and item 8 still states LO 2.15.A's harder conclusion")


ua.shape(v2_15)
ua.check(v2_15, ANCHORS, GROUNDING)
ua.notation(v2_15)
_branches_not_levels(v2_15)
_extent(v2_15)
uc.check(v2_15, TABLE_CHECKS)

# WHAT THE REVIEW FOUND
# ---------------------
# No wrong key. One item was cut rather than fixed: the module was written with
# thirty-one questions, and the one removed asked a student to identify an
# organization moving from an agency to a congressional committee to a federal
# court as an illustration of multiple access points. It was correct and it was
# redundant -- item 12 already makes the three-way distinction among EK 1.6.B.1,
# EK 1.9.A.1 and EK 2.15.B.1 the question, and the venues table in items 23 to
# 25 shows the same movement as data. Thirty is the exporter's requirement, and
# the right item to lose is the one whose work is done twice elsewhere.
#
# The other thing worth recording is _branches_not_levels. This bank now states
# the access-point claim in three modules because the framework states it in
# three essential-knowledge statements, and the only thing stopping three
# modules from becoming three copies of one module is that each is pinned to a
# different multiplier. v1_9 already carries the mirror-image note. A check that
# reads the KEYS for state and local venues is a crude instrument, but it fails
# loudly the moment someone writes a federalism item under a branches code,
# which is exactly the drift that would otherwise be invisible until a student
# saw the same question twice.
