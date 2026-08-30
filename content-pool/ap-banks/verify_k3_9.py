"""Key audit for AP COMPARATIVE GOVERNMENT 3.9 Challenges from Political and
Social Cleavages.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
This topic has ONE essential knowledge statement:

  LEG-2.B.5  challenges to SECURING STABILITY IN MULTINATIONAL STATES include
             .a CONFLICTING INTERESTS AND COMPETITION AMONG GROUPS AND POLITICAL
             PARTIES, .b PERCEIVED LACK OF GOVERNMENTAL AUTHORITY AND LEGITIMACY,
             .c PRESSURE FOR AUTONOMY/SECESSION, INTERGROUP CONFLICT, TERRORISM and
             CIVIL WAR, and .d ENCROACHMENT OF NEIGHBORING STATES THAT SENSE
             GOVERNMENT WEAKNESS AND VULNERABILITY

THREE INTERNAL, ONE EXTERNAL -- and the external one is CAUSED by the others
being visible. That asymmetry is the statement's most testable feature: a reader
who treats the list as uniformly internal misses the framework's claim that
perceived weakness invites outside pressure. Items 5, 6, 11 and 25 key it.

One sentence cannot carry thirty items, so the rest come from LEG-2.B.2.b (the
range of responses), LEG-2.B.3 (cleavages used to hold power and able to undermine
legitimacy), LEG-2.B.4.a (separatist movements in five course countries),
LEG-1.A.1 (legitimacy as belief), LEG-1.B.3, LEG-1.C.1.b (Iran, Mexico and Nigeria),
LEG-1.C.2, PAU-2.A.2, DEM-1.A.3 and MPA-1.A.3 -- each named in the claim that uses
it.

Topic 1.10 keys LEG-2.B.5's list once, as recall. This module works the four
sub-points one at a time, keys the internal/external split, and puts the list into
a matrix (items 23-25) and a data set (items 20-22, 26-27).

DATA ITEMS
----------
Item 21 asks for a SHARE where the counts point elsewhere, and the row that wins
is the one about PERCEPTION, which is what LEG-1.A.1's definition of legitimacy
would predict. Item 27 is the causal brake: three paired observations are an
association, and a government already unpopular might attract more of these
challenges rather than the reverse.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k3_9

REPORTED = "Number of states reporting it"
FELL = "Number of those states in which the government's approval fell in the same period"
WHAT = "What is reported"
NCHAL = "Number of the framework's four challenges reported"
APPROVAL = "Government approval (percent)"

PARTIES = "Conflicting interests and competition among groups and political parties"
PERCEIVED = "Perceived lack of governmental authority and legitimacy"
AUTONOMY = "Pressure for autonomy or secession"
NEIGHBOR = "Encroachment by a neighboring state"


def _chal(table):
    return {str(r[0]): (cg.cell(table, r[0], REPORTED), cg.cell(table, r[0], FELL)) for r in table["rows"]}


def q20(table, item):
    v = _chal(table)
    assert max(v, key=lambda k: v[k][0]) == PARTIES, f"the most reported challenge is {max(v, key=lambda k: v[k][0])}"
    assert v[PARTIES][0] == 31, f"the keyed count reads {v[PARTIES][0]}"
    stated = {AUTONOMY: 22, PERCEIVED: 18, NEIGHBOR: 6}
    for lab, n in stated.items():
        assert v[lab][0] == n, f"the option for {lab} states {n} but the table gives {v[lab][0]}"
    return f"the four counts are {[v[l][0] for l in v]}, and each option states the true count for a different row"


def q21(table, item):
    v = _chal(table)
    share = {lab: f / n for lab, (n, f) in v.items()}
    assert max(share, key=share.get) == PERCEIVED, f"the largest share belongs to {max(share, key=share.get)}"
    assert v[PERCEIVED] == (18, 17), f"the keyed 17 of 18 reads {v[PERCEIVED]}"
    bigger_counts = [lab for lab, (_, f) in v.items() if f > v[PERCEIVED][1]]
    assert not bigger_counts, "no row may have a larger raw count, but the counts must still not settle it"
    assert v[PARTIES][1] < v[PERCEIVED][1] and share[PARTIES] < 0.5, \
        "the most-reported challenge must have a much smaller share, so count and share come apart"
    assert len(set(share.values())) == 4, "'all four equally' must be false"
    return f"the four shares are {[round(share[l], 2) for l in v]}, with the perception row highest at 17 of 18"


def q22(table, item):
    col = cg.col(table, REPORTED)
    total = sum(col)
    assert total == 77, f"the keyed total recomputes to {total}"
    assert sum(cg.col(table, FELL)) == 48, "the 48 distractor must be the other column's total"
    assert total - 6 == 71, "the 71 distractor must be the total less the smallest row"
    assert 31 + 18 + 6 == 55, "the 55 distractor must be a three-row partial sum"
    assert max(col) == 31, "the 31 distractor must be the largest single row"
    return f"the report column reads {col} and sums to {total:.0f}, with each distractor a wrong column or partial sum"


def _scen(table):
    return {str(r[0]): str(r[1]) for r in table["rows"]}


def q23(table, item):
    v = _scen(table)
    assert "parties" in v["Case 1"] and "budget" in v["Case 1"], f"the keyed row reads {v['Case 1']!r}"
    for lab in ("Case 2", "Case 3", "Case 4"):
        assert "parties" not in v[lab], f"{lab} must not also turn on party competition"
    return "one row alone describes party competition producing deadlock, while the others state the framework's other three challenges"


def q24(table, item):
    v = _scen(table)
    assert "no right to make decisions" in v["Case 2"], f"the keyed row reads {v['Case 2']!r}"
    for lab in ("Case 1", "Case 3", "Case 4"):
        assert "no right" not in v[lab], f"{lab} must not also deny the government's right to decide"
    return "one row alone reports citizens denying the government's right to decide, which is a claim about belief"


def q25(table, item):
    v = _scen(table)
    assert "neighboring state" in v["Case 4"], f"the keyed row reads {v['Case 4']!r}"
    for lab in ("Case 1", "Case 2", "Case 3"):
        assert "neighboring state" not in v[lab], f"{lab} must describe an actor inside the state"
    assert "unable to control its territory" in v["Case 4"], \
        "the keyed row must include the perception of weakness, which is what triggers the framework's external challenge"
    return "one row alone names an actor outside the state, acting on a judgement that the government is weak"


def _stab(table):
    return {lab: (cg.cell(table, lab, NCHAL), cg.cell(table, lab, APPROVAL)) for lab in cg.labels(table)}


def q26(table, item):
    v = _stab(table)
    order = sorted(v, key=lambda k: v[k][0])
    approvals = [v[lab][1] for lab in order]
    assert approvals == sorted(approvals, reverse=True), \
        f"approval must fall as the challenge count rises; got {approvals}"
    assert len(set(approvals)) == 3, "'approval is the same in all three' must be false"
    assert max(v[lab][0] for lab in v) > 2, "'no country records more than two challenges' must be false"
    return f"ordering the rows by challenge count gives approvals {approvals}, falling at every step"


def q27(table, item):
    v = _stab(table)
    assert len(v) == 3, "the objection turns on there being only three paired observations"
    order = sorted(v, key=lambda k: v[k][0])
    approvals = [v[lab][1] for lab in order]
    assert approvals == sorted(approvals, reverse=True), \
        "the columns must genuinely move together, or the objection would be to the reading rather than the inference"
    return "the association is real across all three rows, so what the key rejects is the causal step and not the reading"


CLAIMS = [
 ("securing stability in multinational states",
  "EK LEG-2.B.5 introduces its four items as challenges governments face in securing stability in multinational states, which is why each concerns divisions inside a society rather than the machinery of elections, courts or treaties."),
 ("conflicting interests and competition among groups and political parties",
  "EK LEG-2.B.5.a names conflicting interests and competition among groups and political parties. The rejected options are the framework's other three challenges and one that appears nowhere in the statement."),
 ("perceived lack of governmental authority and legitimacy",
  "EK LEG-2.B.5.b names a perceived lack of governmental authority and legitimacy, and EK LEG-1.A.1 makes legitimacy a matter of whether constituents believe their government has the right to use power as it does. The word 'perceived' places this challenge in the realm of belief."),
 ("intergroup conflict, terrorism, and civil war",
  "EK LEG-2.B.5.c groups pressure for autonomy or secession with intergroup conflict, terrorism and civil war in one item, running from a political demand through to organized violence."),
 ("encroachment of neighboring states that sense government weakness",
  "EK LEG-2.B.5.d is the only one of the four to name an actor outside the state. The other three arise among a state's own groups, parties and citizens."),
 ("may encroach when they sense that the government is weak",
  "EK LEG-2.B.5.d states that encroachment comes from neighboring states that SENSE GOVERNMENT WEAKNESS AND VULNERABILITY, so the external challenge is triggered by the internal ones. That dependence is why the list mixes three internal items with one external."),
 ("conflicting interests and competition among groups and political parties",
  "EK LEG-2.B.5.a names this challenge and EK LEG-2.B.1 states that cleavages affect party systems as well as voting behavior. Deadlock between two group-based parties is that challenge in operation."),
 ("perceived lack of governmental authority and legitimacy",
  "EK LEG-2.B.5.b names a perceived lack of governmental authority and legitimacy, and EK LEG-1.A.1 defines legitimacy as whether constituents believe the government has the right to use power as it does. Denial of that right is the challenge stated directly."),
 ("pressure for secession together with intergroup conflict",
  "EK LEG-2.B.5.c groups pressure for autonomy or secession with intergroup conflict, terrorism and civil war, and the scenario moves along that sequence. EK LEG-2.B.4.a records separatist movements in five of the six course countries."),
 ("encroachment of a neighboring state that senses government weakness",
  "EK LEG-2.B.5.d names encroachment of neighboring states that sense government weakness and vulnerability. The judgement that the government cannot control its territory is the sensed weakness the statement describes."),
 ("three difficulties arising among its own groups",
  "EK LEG-2.B.5.a, .b and .c concern a state's own parties, citizens and movements while EK LEG-2.B.5.d names neighboring states, so three internal and one external is the composition of the framework's list."),
 ("constituents believe the government has the right to use power",
  "EK LEG-1.A.1 defines legitimacy as whether a government's constituents believe it has the right to use power in the way they do, so a shortfall in legitimacy is by definition a matter of perception. EK PAU-1.A.4's sovereignty is a legal standing instead."),
 ("recognition end",
  "EK LEG-2.B.2.b states that state responses range from brute repression to recognition of ethnic and religious minorities and the creation of autonomous regions and/or representation of minorities in governmental institutions. The scenario names the framework's own accommodating measure."),
 ("strengthen legitimacy and hold onto power, and they may also lead to conflict",
  "EK LEG-2.B.3 states both halves in one statement, and EK LEG-1.B.3 adds that serious problems such as social conflicts can undermine legitimacy."),
 ("five",
  "EK LEG-2.B.4.a names China, Iran, Nigeria, Russia and the United Kingdom, five of the six. EK LEG-2.B.5.c makes pressure for autonomy or secession one of the challenges to stability in multinational states, so the two statements bear on each other directly."),
 ("conventional options for participation are ineffective or unavailable",
  "EK DEM-1.A.3 names citizens feeling that more conventional options are ineffective or unavailable among the conditions making violent political behavior more likely, and EK LEG-2.B.5.c places intergroup conflict and terrorism among the challenges to stability."),
 ("Iran, Mexico and Nigeria",
  "EK LEG-1.C.1.b names state responses to separatist group violence, drug trafficking and discrimination based on gender or religious differences in Iran, Mexico and Nigeria. Both the trio of challenges and the trio of countries are the framework's."),
 ("attract more private capital and foreign direct investment",
  "EK LEG-1.C.2 states that state authorities of different regime types attempt to limit the influence of divisive and violent actors to attract more private capital and foreign direct investment and to improve economic growth."),
 ("degree to which power is centralized or decentralized",
  "EK PAU-2.A.2 states that the degree of centralization can change over time and in many cases reflects a state response to internal and external actors including ethnic cleavages and the operations of supranational organizations and other countries."),
 ("in 31 states",
  "EK LEG-2.B.5 names all four of the table's rows as challenges to securing stability in multinational states, so the comparison stays inside the framework's list. Recomputed in q20 above, with each option stating the true count for a different row."),
 ("in 17 of the 18 states reporting it",
  "The question asks for a SHARE, so each row's second figure must be divided by its first. Recomputed in q21 above: the row about PERCEPTION wins, which is what EK LEG-1.A.1's definition of legitimacy as a belief of constituents would lead one to expect, while the most-reported challenge has much the smallest share."),
 ("77",
  "Recomputed in q22 above by summing the report column. Each distractor is the other column's total, the total less a row, a three-row partial sum, or the largest single row."),
 ("refuse to govern together and no budget passes",
  "EK LEG-2.B.5.a names conflicting interests and competition among groups and political parties. Recomputed in q23 above: only one row describes party competition producing deadlock, and the others state the framework's other three challenges."),
 ("deny that the national government has the right to decide for them",
  "EK LEG-2.B.5.b names a perceived lack of governmental authority and legitimacy and EK LEG-1.A.1 defines legitimacy as a belief of constituents. Recomputed in q24 above; the rejected final option confuses legitimacy with EK PAU-1.A.4's sovereignty."),
 ("after judging the government unable to control its territory",
  "EK LEG-2.B.5.d is the only one of the four challenges to name an actor outside the state, and it specifies neighboring states that sense government weakness and vulnerability. Recomputed in q25 above, including that the keyed row states the perception as well as the act."),
 ("the lower its government's approval",
  "EK LEG-2.B.5 lists its four items as obstacles to securing stability and EK LEG-1.B.3 states that serious problems including social conflicts can undermine legitimacy. Recomputed in q26 above: ordering the rows by challenge count makes approval fall at every step."),
 ("three paired observations show an association",
  "EK MPA-1.A.3 states that numerous variables potentially influence political outcomes with no way to isolate and demonstrate which is producing the change, and EK MPA-1.A.4 calls a co-movement an association. Recomputed in q27 above: the columns do move together, so only the causal step fails, and a government already unpopular might attract more of these challenges."),
 ("majority denying that the national government has the right",
  "EK LEG-2.B.5.b names a perceived lack of governmental authority and legitimacy and EK LEG-1.A.1 makes legitimacy a belief of constituents, so the evidence must be about that belief. Legislative deadlock is EK LEG-2.B.5.a's challenge and the remaining options belong to EK LEG-2.B.5.d, EK LEG-2.B.5.c and EK LEG-2.B.2.b."),
 ("taken control of territory after publicly describing the government as unable",
  "EK LEG-2.B.5.d describes encroachment of neighboring states that sense government weakness and vulnerability, so the evidence must show both the encroachment and the perception. A trade agreement, treaty membership, domestic criticism and diplomatic spending show neither."),
 ("can in turn invite encroachment by neighbouring states",
  "EK LEG-2.B.5 lists four challenges, three internal and one external, and makes the external one turn on neighboring states sensing government weakness and vulnerability. The summary keeps that dependence between the internal three and the external one."),
]

cg.check(k3_9, CLAIMS,
         table_checks={20: q20, 21: q21, 22: q22, 23: q23, 24: q24, 25: q25, 26: q26, 27: q27})
