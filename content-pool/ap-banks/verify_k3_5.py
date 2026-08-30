"""Key audit for AP COMPARATIVE GOVERNMENT 3.5 Nature and Role of Political
Participation.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
  DEM-1.A.1  participation can be VOLUNTARY OR COERCED, INDIVIDUAL OR GROUP
  DEM-1.A.2  it ranges from REGIME-SUPPORTIVE behavior (INDEPENDENTLY OR UNDER
             STATE DIRECTION) to OPPOSITIONAL behavior seeking to CHANGE
             GOVERNMENTAL POLICIES OR OVERTHROW THE REGIME
  DEM-1.A.3  violent political behavior is more likely WHEN CITIZENS FEEL
             CONVENTIONAL OPTIONS ARE INEFFECTIVE OR UNAVAILABLE
  DEM-1.A.4  formal participation can be ENCOURAGED ACROSS REGIME TYPES to ENHANCE
             LEGITIMACY, GATHER INPUT, ACT AS A SAFETY VALVE, or APPLY A CHECK;
             authoritarian regimes are MORE LIKELY to use it to INTIMIDATE
             OPPOSITION OR GIVE AN ILLUSION OF INFLUENCE, democratic regimes hold
             elections to ALLOW CITIZEN CONTROL OF THE POLICY-MAKING PROCESS
  DEM-1.A.5  REFERENDA let citizens vote DIRECTLY ON POLICY QUESTIONS, used to
             PROMOTE DEMOCRATIC POLICY MAKING, to let a CHIEF EXECUTIVE BYPASS THE
             LEGISLATURE, and to OBLIGE CITIZENS to make difficult and potentially
             unpopular decisions; the UNITED KINGDOM has used them on DEVOLUTION TO
             REGIONAL ASSEMBLIES, on SEPARATION AND THE CREATION OF AN INDEPENDENT
             NATION-STATE, and on WITHDRAWAL FROM THE EUROPEAN UNION

THE STATEMENT STUDENTS HALVE
----------------------------
DEM-1.A.4 says formal participation is encouraged ACROSS REGIME TYPES for four
named purposes, and only then distinguishes what each type is MORE LIKELY to use
it for. Items 7, 10 and 21 key that, and no item lets encouraged voting stand as
evidence of regime type on its own -- item 21's key is the row where every seat is
contested rather than the row with the highest turnout.

DEM-1.A.2's other easily-lost clause is 'either independently or under state
direction': regime-supportive participation is not by itself evidence the state
organized it. Item 3 keys that.

DATA ITEMS
----------
Suggested skill 3.D is Data Analysis, so the module carries three sets (8 items).
The election table separates turnout from contestation, which is what lets items
20 and 21 pull apart. The participation table's two aim columns are DEM-1.A.2's
two ends, and item 25 turns on reading them as PROPORTIONS, where the share aimed
at overthrowing the regime rises as the form becomes less conventional. The
referendum table's three stated reasons are DEM-1.A.5's three reasons, so item 26
cannot be answered by eliminating options that are off the framework's list.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k3_5

TURN = "Turnout at the most recent national election (percent)"
CONTEST = "Share of seats contested by more than one candidate (percent)"
REQ = "Share of voters saying voting is legally or socially required (percent)"
EPS = "Episodes recorded"
POLICY = "Episodes in which participants sought to change a governmental policy"
OVERTHROW = "Episodes in which participants sought to overthrow the regime"
REASON = "Stated reason for holding it"


def _turn(table):
    return {lab: (cg.cell(table, lab, TURN), cg.cell(table, lab, CONTEST), cg.cell(table, lab, REQ))
            for lab in cg.labels(table)}


def q20(table, item):
    v = _turn(table)
    t, c, r = v["Country P"]
    assert t == max(x[0] for x in v.values()), "the keyed row must have the highest turnout"
    assert c == min(x[1] for x in v.values()), "the keyed row must have the fewest contested seats"
    assert r == max(x[2] for x in v.values()), "the keyed row must have the most voters calling voting required"
    assert c < 20 and t > 90, "the combination the key names is a very high turnout with almost no contestation"
    return "one row pairs 93 percent turnout with 11 percent of seats contested and 68 percent calling voting required"


def q21(table, item):
    v = _turn(table)
    t, c, r = v["Country Q"]
    assert c == max(x[1] for x in v.values()) == 100, "the keyed row must have every seat contested"
    assert r == min(x[2] for x in v.values()), "the keyed row must have the fewest voters calling voting required"
    assert t == min(x[0] for x in v.values()), \
        "the keyed row must NOT have the highest turnout, or the item would not separate turnout from contestation"
    return "the keyed row has every seat contested and the lowest turnout, so turnout alone cannot be what identifies it"


def q22(table, item):
    col = cg.col(table, CONTEST)
    gap = max(col) - min(col)
    assert gap == 89, f"the keyed gap recomputes to {gap}"
    assert max(col) - sorted(col)[1] == 26 and sorted(col)[1] - min(col) == 63, \
        "the 26 and 63 distractors must be the other pairwise gaps in the same column"
    turn = cg.col(table, TURN)
    assert max(turn) - min(turn) == 31, "the 31 distractor must be the corresponding gap in the turnout column"
    assert max(col) == 100, "the 100 distractor must be the largest single value read as a difference"
    return f"the contestation column spans {min(col):.0f} to {max(col):.0f}, a gap of {gap:.0f}"


def _part(table):
    return {str(r[0]): (cg.cell(table, r[0], EPS), cg.cell(table, r[0], POLICY), cg.cell(table, r[0], OVERTHROW))
            for r in table["rows"]}


def q23(table, item):
    v = _part(table)
    both = [lab for lab, (_, p, o) in v.items() if p > 0 and o > 0]
    assert both == ["Street protest"], f"exactly one row may record episodes in both aim columns; got {both}"
    assert v["Armed insurgency"][1] == 0, "the least conventional row must record no policy-change episodes"
    assert v["Voting in a national election"][2] == 0, "the most conventional row must record no overthrow episodes"
    return "one row alone records episodes aimed at changing policy AND episodes aimed at overthrowing the regime"


def q24(table, item):
    v = _part(table)
    col = [n for n, _, _ in v.values()]
    total = sum(col)
    assert total == 267, f"the keyed total recomputes to {total}"
    assert sum(p for _, p, _ in v.values()) == 211, "the 211 distractor must be the policy-aim column's total"
    assert total - max(col) == 147, "the 147 distractor must be the total less the largest row"
    assert col[0] + col[1] == 206, "the 206 distractor must be a two-row partial sum"
    assert max(col) == 120, "the 120 distractor must be the largest single row"
    return f"the episode column reads {col} and sums to {total:.0f}, with each distractor another column or a partial sum"


def q25(table, item):
    v = _part(table)
    order = list(v)
    share = [v[lab][2] / v[lab][0] for lab in order]
    assert share == sorted(share), f"the overthrow share must not fall as the form becomes less conventional; got {share}"
    assert share[0] == 0 and share[1] == 0 and share[-1] == 1.0, \
        "the two most conventional rows must be zero and the least conventional entirely overthrow-aimed"
    assert any(o == 0 for _, _, o in v.values()), "'every form includes overthrow episodes' must be false"
    assert any(p > 0 for _, p, _ in v.values()), "'no form includes policy-change episodes' must be false"
    biggest = max(v, key=lambda k: v[k][0])
    assert share[order.index(biggest)] < max(share), \
        "'the form with the most episodes has the largest overthrow share' must be false"
    return f"read as proportions the overthrow shares run {[round(s, 2) for s in share]}, rising as the form becomes less conventional"


def _ref(table):
    return {str(r[0]): str(r[1]) for r in table["rows"]}


def q26(table, item):
    v = _ref(table)
    assert "chief executive" in v["Referendum 2"] and "blocked" in v["Referendum 2"], \
        f"the keyed row reads {v['Referendum 2']!r}"
    assert "devolved" in v["Referendum 1"], "the first row must state the democratic-policy-making reason"
    assert "oblige" in v["Referendum 3"], "the third row must state the difficult-decision reason"
    for lab in ("Referendum 1", "Referendum 3"):
        assert "chief executive" not in v[lab], f"{lab} must not also name the executive's bypass"
    return "all three rows state one of the framework's three reasons, and only one names the executive going around the legislature"


def q27(table, item):
    v = _ref(table)
    assert "devolved to a regional assembly" in v["Referendum 1"], f"the keyed row reads {v['Referendum 1']!r}"
    for lab in ("Referendum 2", "Referendum 3"):
        assert "devol" not in v[lab] and "independent" not in v[lab] and "European" not in v[lab], \
            f"{lab} must not match any of the three United Kingdom subjects"
    return "one row's subject is devolution to a regional assembly, which is the first of the framework's three named subjects"


CLAIMS = [
 ("voluntary or coerced",
  "EK DEM-1.A.1 states that political participation can be voluntary or coerced and may occur at the individual or group level. Both distinctions are offered as available in principle rather than as fixed by regime type."),
 ("supportive of a regime to oppositional behavior",
  "EK DEM-1.A.2 states that participation can range from behavior supportive of a regime to oppositional behavior seeking to change governmental policies or overthrow the regime. The range is defined by aim rather than by legality or by numbers."),
 ("either independently or under state direction",
  "EK DEM-1.A.2 places this phrase inside its description of regime-supportive behavior, so supportive participation is not by itself evidence that the state organized it."),
 ("seeking to change governmental policies, or seeking to overthrow the regime",
  "EK DEM-1.A.2 gives oppositional behavior these two targets: a policy inside the rules, or the rules themselves. EK PAU-1.A.2's distinction between government and regime is the same boundary."),
 ("certain political conditions make it more likely",
  "EK DEM-1.A.3 states that certain political conditions make it more likely that citizens will engage in violent political behavior, and then names one. The claim is about likelihood rather than certainty."),
 ("conventional options for political participation are ineffective or unavailable",
  "EK DEM-1.A.3 names this condition explicitly. Both halves matter, since an option can exist and still be believed useless."),
 ("act as a safety valve",
  "EK DEM-1.A.4 names enhancing legitimacy, gathering input, acting as a safety valve and applying a check on governmental policies as the purposes for which formal participation can be encouraged ACROSS REGIME TYPES."),
 ("intimidate opposition or give an illusion of influence",
  "EK DEM-1.A.4 states that authoritarian regimes are more likely to use citizen participation to intimidate opposition or give an illusion of influence, contrasting that with the use it assigns to democratic regimes in the same sentence."),
 ("allow citizen control of the policy-making process",
  "EK DEM-1.A.4 states that democratic regimes hold elections to allow citizen control of the policy-making process, in contrast with the uses it attributes to authoritarian regimes."),
 ("encouraged across regime types",
  "EK DEM-1.A.4 states that formal political participation can be encouraged across regime types for four named purposes before distinguishing what each type is MORE LIKELY to use it for, and EK DEM-1.B.1 puts the real difference in how open and competitive elections are."),
 ("vote directly on policy questions",
  "EK DEM-1.A.5 states that referenda allow citizens to vote directly on policy questions, and that directness is what separates a referendum from an election of representatives."),
 ("bypass the legislature",
  "EK DEM-1.A.5 names promoting democratic policy making, allowing a chief executive to bypass the legislature, and obliging citizens to make difficult and potentially unpopular decisions as the reasons referenda are used. The framework lists all three without ranking them."),
 ("separation and creation of an independent nation-state",
  "EK DEM-1.A.5 names the devolution of powers to regional assemblies, the separation and creation of an independent nation-state, and withdrawal from the European Union as the subjects on which the United Kingdom has used referenda. EK PAU-1.D.1.e records the devolution reforms separately."),
 ("participation can be coerced",
  "EK DEM-1.A.1 states that political participation can be voluntary or coerced, and a penalty attached to abstention is coercion in the plainest sense. The framework's other distinctions concern level, aim, mechanism and conditions."),
 ("under state direction",
  "EK DEM-1.A.2 describes behavior supportive of a regime occurring either independently or under state direction, and attendance instructed by the state is the second. EK DEM-1.A.1's coerced participation describes the same event on its other axis."),
 ("rather than to overthrow the regime",
  "EK DEM-1.A.2 distinguishes oppositional behavior seeking to change governmental policies from behavior seeking to overthrow the regime, and amending a statute through petitions and legislators is the first. EK PAU-1.A.2's government-regime boundary is the same line."),
 ("allowing a chief executive to bypass the legislature",
  "EK DEM-1.A.5 names this among the reasons referenda are used, and the scenario is that reason exactly. The framework lists it alongside more favorable reasons without endorsing any."),
 ("obliging citizens to make difficult and potentially unpopular decisions",
  "EK DEM-1.A.5 names this among the reasons referenda are used. Putting two unwelcome options to voters transfers the choice rather than the initiative."),
 ("conventional options are ineffective or unavailable",
  "EK DEM-1.A.3 names citizens feeling that more conventional options are ineffective or unavailable among the conditions making violent political behavior more likely, and the scenario supplies both halves, the barred ballot and the ignored petition."),
 ("smallest share of contested seats",
  "EK DEM-1.A.4 states that authoritarian regimes are more likely to use participation to intimidate opposition or give an illusion of influence, and EK DEM-1.B.1 adds that in many such elections there are few if any opposition candidates. Recomputed in q20 above: one row pairs the highest turnout with the least contestation and the most compulsion."),
 ("every seat is contested by more than one candidate",
  "EK DEM-1.A.4 states that democratic regimes hold elections to allow citizen control of the policy-making process, and EK DEM-1.B.1 makes how open and competitive elections are the thing that decides citizens' impact. Recomputed in q21 above: the keyed row has the LOWEST turnout, so turnout alone cannot identify it."),
 ("89 percentage points",
  "Recomputed in q22 above from the contestation column. Every distractor is a real figure from another pair of rows, the turnout column, or a single value read as a difference."),
 ("episodes aimed at changing policy and episodes aimed at overthrowing the regime",
  "EK DEM-1.A.2 gives oppositional behavior two ends, changing governmental policies or overthrowing the regime. Recomputed in q23 above: only one row records episodes in both columns."),
 ("267",
  "Recomputed in q24 above by summing the episode column. Each distractor is another column's total, the total less a row, a two-row partial sum, or the largest single row."),
 ("share of episodes aimed at overthrowing the regime rises",
  "EK DEM-1.A.2 sets out the range from regime-supportive to regime-overthrowing behavior and EK DEM-1.A.3 links violent behavior to conventional options failing. Recomputed in q25 above: read as proportions the overthrow share is zero for the two most conventional forms and rises through the two least conventional."),
 ("settle a question the legislature had blocked",
  "EK DEM-1.A.5 names allowing a chief executive to bypass the legislature among the reasons referenda are used. Recomputed in q26 above: all three rows state one of the framework's three reasons, so the item cannot be answered by eliminating off-list options."),
 ("devolved to a regional assembly",
  "EK DEM-1.A.5 states that the United Kingdom has used referenda on the devolution of powers to regional assemblies, on separation and the creation of an independent nation-state, and on withdrawal from the European Union. Recomputed in q27 above: only one row's subject is among those three."),
 ("direct them into petitions, hearings and elections",
  "EK DEM-1.A.4 names acting as a safety valve among the purposes for which formal participation can be encouraged across regime types, and EK DEM-1.A.3 explains what pressure it releases, since violent behavior becomes more likely when conventional options are felt ineffective or unavailable."),
 ("the range of candidates is fixed in advance",
  "EK DEM-1.A.4 names giving an illusion of influence among the uses authoritarian regimes are more likely to make of participation, and EK DEM-1.B.1 states that in many such elections there are few if any opposition candidates and that governments often intervene to ensure preferred candidates win."),
 ("encouraged across regime types for four named purposes though for different ends",
  "EK DEM-1.A.1 supplies the two axes, EK DEM-1.A.2 the range of aims, EK DEM-1.A.3 the condition for violent behavior, EK DEM-1.A.4 the cross-regime encouragement with its four purposes and regime-specific ends, and EK DEM-1.A.5 the referendum with its three reasons."),
]

cg.check(k3_5, CLAIMS,
         table_checks={20: q20, 21: q21, 22: q22, 23: q23, 24: q24, 25: q25, 26: q26, 27: q27})
