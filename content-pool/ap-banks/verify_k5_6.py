"""Key audit for AP COMPARATIVE GOVERNMENT 5.6 Adaptation of Social Policies.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
Learning objective LEG-3.B, two essential knowledge statements:

  LEG-3.B.1  in response to POLITICAL, CULTURAL AND ECONOMIC CHANGES governments
             create new social policies -- GENDER EQUITY, HEALTH CARE, EDUCATION
             -- represented by .a Iran's gender equity rules for VOTING, THE
             ELECTION OF MAJLES and APPOINTMENT TO CABINET POSITIONS; .b disputes
             in Iran about FEMALE ACCESS TO CERTAIN UNIVERSITY DEGREE PROGRAMS
             and ATTENDANCE AT AND PARTICIPATION IN SPORTING EVENTS; .c VARIED
             ABORTION POLICIES IN MEXICO'S LOCAL AND STATE GOVERNMENTS; .d GENDER
             QUOTAS IN MEXICO; .e UNEQUAL GENDER ACCESS TO EDUCATION IN THE NORTH
             AND SOUTH OF NIGERIA
  LEG-3.B.2  social welfare policies REDUCE POVERTY, INCREASE LITERACY and
             IMPROVE PUBLIC HEALTH, BOTH to improve citizens' lives AND to
             MAINTAIN OR BOLSTER POLITICAL LEGITIMACY

LEG-3.B.2 PUTS TWO PURPOSES IN ONE SENTENCE and joins them with "both ... and",
not "or". That is the item this topic turns on. A student who files welfare
policy as purely humanitarian cannot explain why a government would make delivery
the centerpiece of its case for support, and a student who files it as purely
cynical loses the first half. Items 9, 14, 15, 19 and 20 key the pair, and EK
LEG-1.A.1's definition of legitimacy as what constituents BELIEVE is what makes
the second purpose intelligible rather than merely alleged.

THE FIVE EXAMPLES ARE NOT FIVE COUNTRIES. Two are Iranian, two Mexican, one
Nigerian, and they differ in KIND: rules about holding office (.a), disputes over
access (.b), variation ACROSS LEVELS OF GOVERNMENT (.c), a nomination requirement
(.d), and a gap ACROSS REGIONS (.e). Items 10, 11, 12 and 13 key those
differences, because "which country" is the easy half of a comparison item and
"which kind of policy question" is the half the exam actually asks.

WHAT IS DELIBERATELY NOT ASSERTED: no outcome, statistic, court ruling, election
or current condition of any real country appears anywhere in the module. Each
example is keyed to exactly what its own sentence says. In particular item 5 says
only that abortion policies VARY across Mexico's local and state governments,
which is the framework's entire claim, and NO CONTENT is attributed to any of
those policies. Every table figure is HYPOTHETICAL, labelled so, and attached to
an unnamed country -- including the two-region table, which models the SHAPE of
EK LEG-3.B.1.e's claim without putting a number on a real place.

DATA ITEMS
----------
Items 21-23 read the quota table, 24-26 the welfare-budget table, 27-29 the
two-region table. Item 21's key rests on a contrast between rows WITH the rules
and the row without, so its check tests the quota column as well as the numbers;
item 24's check confirms the budget table's three rows ARE the framework's three
welfare aims. Every arithmetic distractor is verified to be a wrong operation on
the same table.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k5_6

BEFORE = "Seats held by women before the rules (percent)"
AFTER = "Seats held by women after the rules (percent)"
RULES = "Nomination quota rules in force"
BUDGET = "Share of one government's social welfare budget (percent, hypothetical)"
BOYS = "Boys completing secondary school (percent)"
GIRLS = "Girls completing secondary school (percent)"


def _quota(table):
    return {lab: (cg.cell(table, lab, BEFORE), cg.cell(table, lab, AFTER),
                  str(table["rows"][i][3]).lower())
            for i, lab in enumerate(cg.labels(table))}


def q21(table, item):
    v = _quota(table)
    with_rules = [lab for lab in v if v[lab][2] == "yes"]
    without = [lab for lab in v if v[lab][2] == "no"]
    assert len(with_rules) == 2 and len(without) == 1, \
        f"the table must have two rows with the rules and one without; it has {with_rules} and {without}"
    rises = {lab: v[lab][1] - v[lab][0] for lab in v}
    assert min(rises[lab] for lab in with_rules) > max(rises[lab] for lab in without) + 20, \
        f"the quota rows must rise by far more than the row without them; the rises are {rises}"
    assert all(rises[lab] > 0 for lab in v), "'only the row without rules saw any increase' must be false"
    assert len({v[lab][1] for lab in v}) == 3, "'every legislature ended at the same share' must be false"
    return f"the rises are {rises} against quota status {[v[l][2] for l in v]}"


def q22(table, item):
    v = _quota(table)
    rises = {lab: v[lab][1] - v[lab][0] for lab in v}
    top = max(rises.values())
    assert top == 31, f"the largest increase recomputes to {top}"
    assert sorted(rises.values()) == [2, 29, 31], f"the three increases are {sorted(rises.values())}"
    assert max(v[lab][1] for lab in v) == 43, "the 43 distractor must be a final share read as an increase"
    assert v["Legislature 1"][1] - v["Legislature 2"][0] == 26, \
        "the 26 distractor must be a difference taken across two different rows"
    return f"the three increases are {sorted(rises.values())}, the largest of them {top:.0f} percentage points"


def q23(table, item):
    a = cg.col(table, AFTER)
    b = cg.col(table, BEFORE)
    gap = max(a) - min(a)
    assert gap == 24, f"the keyed gap recomputes to {gap}"
    assert max(a) - min(b) == 34, "the 34 distractor must be a difference taken across the two columns"
    assert max(x - y for x, y in zip(a, b)) == 31, "the 31 distractor must be the largest single increase"
    assert max(a) == 43 and min(a) == 19, f"the 43 and 19 distractors must be the later column's extremes; it reads {a}"
    return f"the later column reads {a}, so the largest minus the smallest is {gap:.0f} percentage points"


def q24(table, item):
    aims = [a.lower() for a in cg.labels(table)]
    assert aims == ["reducing poverty", "increasing literacy", "improving public health"], \
        f"the rows must be the framework's three welfare aims; they read {aims}"
    v = {lab: cg.cell(table, lab, BUDGET) for lab in cg.labels(table)}
    top = max(v, key=v.get)
    assert top == "Reducing poverty", f"the largest share belongs to {top}"
    assert v[top] == 46, f"the keyed share reads {v[top]}"
    assert v["Improving public health"] == 33 and v["Increasing literacy"] == 21, \
        "each rejected option must state its own row's true share"
    assert len(set(v.values())) == 3, "'all three equally' must be false"
    return f"the three shares are {[v[l] for l in v]} percent across the framework's three welfare aims"


def q25(table, item):
    c = cg.col(table, BUDGET)
    total = sum(c)
    assert total == 100, f"the keyed sum recomputes to {total}"
    assert total - 21 == 79 and total - 33 == 67 and total - 46 == 54, \
        f"the 79, 67 and 54 distractors must be the sum with each row omitted in turn; the column reads {c}"
    assert max(c) == 46, "the 46 distractor must be the largest single row"
    return f"the budget column reads {c} and sums to {total:.0f}"


def q26(table, item):
    c = cg.col(table, BUDGET)
    diff = max(c) - min(c)
    assert diff == 25, f"the keyed difference recomputes to {diff}"
    pairs = {abs(a - b) for a in c for b in c if a != b}
    assert 13 in pairs and 12 in pairs, f"the 13 and 12 distractors must be the other gaps; gaps are {sorted(pairs)}"
    assert max(c) == 46 and min(c) == 21, f"the 46 and 21 distractors must be the extreme shares; the column reads {c}"
    return f"the budget column reads {c}, so the largest minus the smallest is {diff:.0f} percentage points"


def _reg(table):
    return {lab: (cg.cell(table, lab, BOYS), cg.cell(table, lab, GIRLS)) for lab in cg.labels(table)}


def q27(table, item):
    v = _reg(table)
    gaps = {lab: v[lab][0] - v[lab][1] for lab in v}
    assert gaps["Northern region"] > gaps["Southern region"], f"the gaps read {gaps}"
    assert gaps["Northern region"] > 4 * gaps["Southern region"], \
        f"the northern gap must be far wider, not marginally so; the gaps are {gaps}"
    assert all(g > 0 for g in gaps.values()), "'no gap in either region' and 'girls ahead of boys' must both be false"
    assert v["Northern region"] != v["Southern region"], "'identical figures' must be false"
    return f"the boys-minus-girls gaps are {gaps}, far wider in one region than the other"


def q28(table, item):
    v = _reg(table)
    north = v["Northern region"]
    gap = north[0] - north[1]
    assert gap == 26, f"the keyed gap recomputes to {gap}"
    south = v["Southern region"]
    assert south[0] - south[1] == 5, "the 5 distractor must be the other region's gap"
    assert gap - (south[0] - south[1]) == 21, "the 21 distractor must be the difference between the two gaps"
    assert north == (54, 28), f"the 54 and 28 distractors must be that row's own figures; it reads {north}"
    return f"the northern row reads {north[0]:.0f} against {north[1]:.0f} percent, a gap of {gap:.0f} percentage points"


def q29(table, item):
    v = _reg(table)
    gaps = {lab: v[lab][0] - v[lab][1] for lab in v}
    diff = gaps["Northern region"] - gaps["Southern region"]
    assert diff == 21, f"the keyed difference recomputes to {diff}"
    assert gaps["Northern region"] == 26 and gaps["Southern region"] == 5, \
        f"the 26 and 5 distractors must be the two gaps themselves; they are {gaps}"
    assert v["Southern region"][0] - v["Northern region"][0] == 17, \
        "the 17 distractor must be the difference between the two regions' boys' figures"
    assert v["Southern region"][1] - v["Northern region"][1] == 38, \
        "the 38 distractor must be the difference between the two regions' girls' figures"
    return f"the two gaps are {gaps['Northern region']:.0f} and {gaps['Southern region']:.0f}, differing by {diff:.0f} percentage points"


CLAIMS = [
 ("political, cultural, and economic changes",
  "EK LEG-3.B.1 states that in response to political, cultural, and economic changes governments create new social policies, so the framework locates the prompt in conditions rather than in an instruction from outside."),
 ("gender equity, health care, and education policies",
  "EK LEG-3.B.1 names gender equity, health care, and education policies as the social policies governments create in response to political, cultural, and economic changes."),
 ("voting, the election of the Majles, and appointment to cabinet positions",
  "EK LEG-3.B.1.a associates gender equity rules in Iran with voting, the election of the Majles, and appointment to cabinet positions, all three of which concern choosing or holding office."),
 ("female access to certain university degree programs",
  "EK LEG-3.B.1.b records disputes in Iran about female access to certain university degree programs and about attendance at and participation in sporting events, which are questions of access rather than of office."),
 ("that it varies across local and state governments",
  "EK LEG-3.B.1.c records varied abortion policies in Mexico's local and state governments, so what the framework states is the variation between levels of government, and it states nothing about the content of any of those policies."),
 ("gender quotas",
  "EK LEG-3.B.1.d names gender quotas in Mexico. Every rejected option is one of the framework's Iranian or Nigerian examples."),
 ("unequal gender access to education in the north and south",
  "EK LEG-3.B.1.e records unequal gender access to education in the north and south of Nigeria, which makes it a claim about variation between two regions of a single country."),
 ("reducing poverty, increasing literacy, and improving public health",
  "EK LEG-3.B.2 states that governments implement social welfare policies to reduce poverty, increase literacy, and improve public health."),
 ("both to improve citizens' lives and to maintain or bolster political legitimacy",
  "EK LEG-3.B.2 joins the two purposes with both and and, so neither is offered as an alternative to the other and a policy can serve the public and the regime at once."),
 ("local and state governments",
  "EK LEG-3.B.1.c is the only one of the five examples to locate its variation in local and state governments, which places the difference between levels of government rather than between regions or between countries."),
 ("in the north and south of Nigeria",
  "EK LEG-3.B.1.e states that gender access to education is unequal in the north and south of Nigeria, which is a comparison between two regions of one country rather than between levels of government."),
 ("a nomination quota and policies that differ across levels of government",
  "EK LEG-3.B.1.a and EK LEG-3.B.1.b give Iran rules about voting, the Majles and cabinet appointment together with disputes about university access and sporting events, while EK LEG-3.B.1.d gives Mexico gender quotas and EK LEG-3.B.1.c policies varying across its local and state governments."),
 ("they range across rules for holding office, disputes over access",
  "EK LEG-3.B.1's five examples differ in kind: rules about office, disputes about access, variation across levels of government, a nomination quota, and a gap between two regions."),
 ("legitimacy is a matter of what constituents believe",
  "EK LEG-3.B.2 names both purposes in one sentence and EK LEG-1.A.1 defines legitimacy as whether constituents believe a government has the right to use power in the way it does, which is why visible provision bears on it."),
 ("both to improve citizens' lives and to maintain or bolster political legitimacy",
  "EK LEG-3.B.2 states that governments implement social welfare policies to increase literacy among other aims, both to improve citizens' lives and to maintain or bolster political legitimacy, and the announcement in the scenario pursues both at once."),
 ("gender quotas of the kind the framework records in Mexico",
  "EK LEG-3.B.1.d names gender quotas in Mexico, and a rule requiring parties to nominate candidates of each gender in fixed proportions is what such a quota does."),
 ("disputes about female access to certain university degree programs",
  "EK LEG-3.B.1.b records disputes in Iran about female access to certain university degree programs, which is precisely the question the scenario describes."),
 ("bolsters regime stability by adapting its policies",
  "Enduring understanding LEG-3 states that a government bolsters regime stability by adapting its policies to environmental, political, economic, and cultural conditions, which is why EK LEG-3.B.1 begins from changes and EK LEG-3.B.2 ends at legitimacy."),
 ("made its delivery the centerpiece of its case for public support",
  "EK LEG-3.B.2 states both purposes together, so evidence for the pair has to show the improvement in citizens' lives and the government's use of it, and EK LEG-1.A.1 makes legitimacy turn on what constituents believe about the government's right to use power."),
 ("in one sentence that these policies are implemented both to improve citizens' lives",
  "EK LEG-3.B.2 joins the two purposes with both and and rather than presenting them as alternatives, so the purely humanitarian reading captures one half of the framework's own statement and drops the other."),
 ("with nomination quota rules in force saw much larger increases",
  "EK LEG-3.B.1.d names gender quotas among the social policies governments create in response to political, cultural, and economic changes. Recomputed in q21 above, which reads the quota column as well as the two share columns."),
 ("31 percentage points",
  "Recomputed in q22 above by taking each row's increase and comparing them. The distractors are the increases in the other two rows, a final share read as an increase, and a difference taken across two different rows."),
 ("24 percentage points",
  "Recomputed in q23 above by subtracting the smallest later share from the largest. The distractors are a difference taken across the two columns, the largest single increase, and the later column's two extreme values."),
 ("reducing poverty, at 46 percent",
  "EK LEG-3.B.2 names reducing poverty, increasing literacy, and improving public health as the aims of social welfare policies. Recomputed in q24 above, which also confirms the table's rows are exactly those three aims."),
 ("100",
  "Recomputed in q25 above by summing the budget column. The distractors are the sum with each row omitted in turn and the largest single row."),
 ("25 percentage points",
  "Recomputed in q26 above by subtracting the smallest share from the largest. The distractors are the other two gaps in the column and its two extreme shares read as differences."),
 ("far wider in the northern region",
  "EK LEG-3.B.1.e records unequal gender access to education in the north and south of Nigeria, a claim about a gap that differs between two regions of one country. Recomputed in q27 above, which requires the wider gap to be several times the narrower one."),
 ("26 percentage points",
  "Recomputed in q28 above by subtracting the girls' figure from the boys' figure in that row. The distractors are the other region's gap, the difference between the two gaps, and that row's own two figures."),
 ("21 percentage points",
  "Recomputed in q29 above by taking each region's gap and subtracting the smaller from the larger. The distractors are the two gaps themselves and the differences between the regions' boys' and girls' figures."),
 ("differ in kind and in the level of government that sets them",
  "EK LEG-3.B.1 supplies the prompt, the three policy areas, and five examples differing in kind and in the level of government involved, while EK LEG-3.B.2 supplies the three welfare aims together with both purposes the framework states for them."),
]

cg.check(k5_6, CLAIMS,
         table_checks={21: q21, 22: q22, 23: q23, 24: q24, 25: q25, 26: q26, 27: q27, 28: q28, 29: q29})
