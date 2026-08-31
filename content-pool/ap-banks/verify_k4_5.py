"""Key audit for AP COMPARATIVE GOVERNMENT 4.5 Impact of Social Movements and
Interest Groups.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
Learning objective IEF-2.A, five essential knowledge statements, under enduring
understanding IEF-2 (strong and varied citizen organizations and movements
FOSTER AND ARE REINFORCED BY democratization -- a two-way claim, keyed at item
14).

  IEF-2.A.1  social movements: LARGE GROUPS PUSHING COLLECTIVELY for SIGNIFICANT
             political or social change
  IEF-2.A.2  interest groups EXPLICITLY ORGANIZED for a SPECIFIC interest or
             policy issue; social movements are MULTIPLE GROUPS AND INDIVIDUALS
             advocating BROAD social change
  IEF-2.A.3  four pressures, then five country instances .a-.e
  IEF-2.A.4  grassroots movements exert power UP FROM THE LOCAL LEVEL
  IEF-2.A.5  limited hierarchies are HARD TO SUPPRESS, BUT can leave a movement
             unable to MOBILIZE SUPPORT or NEGOTIATE with government

IEF-2.A.5 IS A CONCESSION SENTENCE and it is the reason the suggested skill for
this topic is argumentation by refutation, concession and rebuttal. One
structural feature -- few leadership levels -- is stated as a protection against
suppression and, in the same sentence, as an obstacle to mobilizing and
negotiating. A student who keeps only the first clause treats leaderlessness as
costless. Items 12, 13, 19, 20 and the whole first table hold both clauses at
once, and the rebuttal in item 20 is deliberately NOT "the advantage is false"
but "the advantage and the cost have the same cause", which is what the sentence
actually says.

IEF-2.A.2 IS THE DEFINITION PAIR THAT GETS COLLAPSED into "an interest group is
small and a movement is big". The framework's contrast is not size: it is how
EXPLICITLY ORGANIZED the body is and how BROAD its aim. Items 3, 17 and 18 key
both axes, and item 3's distractors are all single-axis or off-axis readings.

WHAT THE MODULE DELIBERATELY DOES NOT ASSERT: IEF-2.A.3 names four pressures and
then five examples, but it does not pair each example with one pressure. The
module therefore pairs an example with a pressure only where the example's own
sentence states the substance -- the Green Movement's protest of election
corruption against "conduct fair and transparent elections" (items 27, 4), and
the Niger Delta movements' protest over the extraction and DISTRIBUTION of oil
against "redistribute revenues from key exports such as oil" (items 28, 6). The
Chiapas and Boko Haram examples are keyed only to what their own sentences say.
An "indigenous civil rights" pairing is NOT made anywhere, because the framework
does not make it.

Table figures are HYPOTHETICAL and every table is labelled so; the third table's
demands are worded as IEF-2.A.3 words its four pressures.

DATA ITEMS
----------
Items 21-23 read the hierarchy table, 24-26 the stage table, 27-28 the demands
table. Item 21's key asserts TWO things about one row, so the check confirms that
row holds both the minimum of one column and the minimum of another, and that the
two columns move together across all three rows -- one row in isolation would not
establish the framework's claim. Item 24's key asserts an ORDER and a TREND, so
the check reads the level names as well as the counts. Every arithmetic
distractor is verified to be a wrong operation on the same table.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k4_5

LEVELS = "Formal leadership levels"
ARREST = "Participants arrested as a share of all participants (percent)"
DEALS = "Formal agreements negotiated with government representatives"

STAGE_LEVEL = "Highest level at which the movement was active"
GROUPS = "Local groups taking part"
GOVTS = "Governments responding publicly"


def _sup(table):
    return {lab: (cg.cell(table, lab, LEVELS), cg.cell(table, lab, ARREST), cg.cell(table, lab, DEALS))
            for lab in cg.labels(table)}


def q21(table, item):
    v = _sup(table)
    flat = min(v, key=lambda k: v[k][0])
    assert flat == "Movement 1", f"the fewest leadership levels belong to {flat}"
    assert v[flat][1] == min(v[k][1] for k in v), \
        f"the flattest movement must have the lowest arrest share; it has {v[flat][1]}"
    assert v[flat][2] == min(v[k][2] for k in v), \
        f"the flattest movement must have the fewest negotiated agreements; it has {v[flat][2]}"
    order = sorted(v, key=lambda k: v[k][0])
    assert [v[k][1] for k in order] == sorted(v[k][1] for k in v), \
        "the arrest share must rise with leadership levels across all three rows"
    assert [v[k][2] for k in order] == sorted(v[k][2] for k in v), \
        "negotiated agreements must rise with leadership levels across all three rows"
    assert len({v[k][1] for k in v}) == 3 and len({v[k][2] for k in v}) == 3, \
        "'no relationship' must be false, so no two rows may tie in either column"
    return (f"ordering the rows by leadership levels {[v[k][0] for k in order]} gives arrest shares "
            f"{[v[k][1] for k in order]} and agreements {[v[k][2] for k in order]}, both rising together")


def q22(table, item):
    deals, arrests, levels = cg.col(table, DEALS), cg.col(table, ARREST), cg.col(table, LEVELS)
    total = sum(deals)
    assert total == 8, f"the keyed total recomputes to {total}"
    assert sum(arrests) == 37, "the 37 distractor must be the arrest column's total"
    assert sum(levels) == 10, "the 10 distractor must be the leadership column's total"
    assert max(deals) == 6, "the 6 distractor must be the largest single row of the keyed column"
    assert total + sum(arrests) == 45, "the 45 distractor must be two columns added together"
    return f"the agreements column reads {deals} and sums to {total:.0f}, with every distractor a wrong sum of the same table"


def q23(table, item):
    a = cg.col(table, ARREST)
    gap = max(a) - min(a)
    assert gap == 17, f"the keyed gap recomputes to {gap}"
    pairs = sorted({abs(x - y) for x in a for y in a if x != y})
    assert 9 in pairs and 8 in pairs, f"the 9 and 8 distractors must be the other gaps in that column; gaps are {pairs}"
    assert max(a) == 21 and min(a) == 4, \
        f"the 21 and 4 distractors must be the column's extreme values read as differences; the column reads {a}"
    return f"the arrest column reads {a}, so the largest minus the smallest is {gap:.0f} percentage points"


def _stage(table):
    return [(str(r[0]), str(r[1]), cg.num(r[2]), cg.num(r[3])) for r in table["rows"]]


def q24(table, item):
    v = _stage(table)
    names = [row[1].lower() for row in v]
    assert names == ["local", "regional", "national", "international"], \
        f"the stages must run local, regional, national, international; they read {names}"
    groups = [row[2] for row in v]
    assert groups == sorted(groups), f"participation must rise at every stage; it reads {groups}"
    assert len(set(groups)) == 4, "'remained local' and 'fell as it widened' must both be false"
    assert groups[0] == min(groups), "the movement must start from its smallest footprint"
    return f"the stages run {names} while local groups taking part go {groups}, rising at every step"


def q25(table, item):
    g, gov = cg.col(table, GROUPS), cg.col(table, GOVTS)
    total = sum(g)
    assert total == 300, f"the keyed total recomputes to {total}"
    assert total + sum(gov) == 306, "the 306 distractor must be the two columns added together"
    assert g[0] + g[-1] == 154, "the 154 distractor must be the first and last stages added"
    assert max(g) == 149, "the 149 distractor must be the largest single stage"
    assert total - min(g) == 295, "the 295 distractor must be the total with the smallest stage omitted"
    return f"the participation column reads {g} and sums to {total:.0f}, with every distractor a wrong sum of the same table"


def q26(table, item):
    g = cg.col(table, GROUPS)
    rise = g[2] - g[0]
    assert rise == 107, f"the keyed increase recomputes to {rise}"
    assert g[3] - g[0] == 144, "the 144 distractor must be the increase to the fourth stage"
    assert g[2] - g[1] == 78, "the 78 distractor must be the increase between the second and third stages"
    assert g[3] - g[2] == 37, "the 37 distractor must be the increase between the third and fourth stages"
    assert g[2] == 112, "the 112 distractor must be a raw stage figure read as an increase"
    return f"the participation column reads {g}, so the rise from the first stage to the third is {rise:.0f}"


def _demands(table):
    return {str(r[0]): str(r[1]) for r in table["rows"]}


def q27(table, item):
    v = _demands(table)
    assert "election" in v["Movement W"].lower(), f"the keyed row reads {v['Movement W']!r}"
    for lab in ("Movement X", "Movement Y", "Movement Z"):
        assert "election" not in v[lab].lower(), f"{lab} must not also name an election"
    assert "transparent" in v["Movement W"].lower(), \
        "the keyed row must use the framework's own wording about fair and transparent elections"
    return "one row alone demands the fair and transparent conduct of an election, the framework's own wording"


def q28(table, item):
    v = _demands(table)
    assert "oil" in v["Movement X"].lower(), f"the keyed row reads {v['Movement X']!r}"
    for lab in ("Movement W", "Movement Y", "Movement Z"):
        assert "oil" not in v[lab].lower(), f"{lab} must not also name oil"
    assert "redistribution" in v["Movement X"].lower(), \
        "the keyed row must state redistribution, which is what the framework's pressure names"
    assert len(set(v.values())) == 4, "the four demands must be distinct, or more than one row would answer"
    return "one row alone demands redistribution of oil export revenues, which is the framework's own pressure"


CLAIMS = [
 ("pushing collectively for significant political or social change",
  "EK IEF-2.A.1 states that social movements involve large groups of people pushing collectively for significant political or social change, so both the collective action and the significance of the aim belong to the definition."),
 ("explicitly organized to represent and advocate for a specific interest",
  "EK IEF-2.A.2 states that interest groups are explicitly organized to represent and advocate for a specific interest or policy issue, so the deliberate organization and the narrowness of the aim are both part of the definition."),
 ("how explicitly they are organized, and how broad the change they seek",
  "EK IEF-2.A.2 contrasts a body explicitly organized around a specific interest or policy issue with multiple groups and individuals advocating for broad social change, which sets two axes rather than one and neither of them is size."),
 ("corruption in the 2009 election",
  "EK IEF-2.A.3.a states that the Green Movement in Iran protested corruption in the 2009 election. Each rejected object of protest belongs to one of the framework's other four country examples."),
 ("negative impact of the North American Free Trade Agreement",
  "EK IEF-2.A.3.b states that the Zapatistas or Chiapas uprising in Mexico arose in response to socioeconomic inequality and the negative impact of the North American Free Trade Agreement."),
 ("unjust methods of extraction and distribution of oil",
  "EK IEF-2.A.3.c states that the Movement for the Emancipation of the Niger Delta and the Movement for the Survival of the Ogoni People emerged to advocate for the rights of an ethnic minority or to protest against unjust methods of extraction and distribution of oil in the Niger Delta region."),
 ("Nigeria",
  "EK IEF-2.A.3.c introduces its examples with the parenthetical that movements in Nigeria are often militant, and no other country's movements carry that description anywhere in the framework."),
 ("establish an Islamic state in northern Nigeria",
  "EK IEF-2.A.3.d states that the Boko Haram movement is attempting to establish an Islamic state in northern Nigeria. Each rejected aim belongs to one of the framework's other four examples."),
 ("State Duma's passage of legislation against same-sex couples",
  "EK IEF-2.A.3.e records domestic protests over the Russian State Duma's passage of legislation against same-sex couples, which makes the object of protest an act of the national legislature rather than an election or an economic policy."),
 ("redistributing revenues from key exports such as oil",
  "EK IEF-2.A.3 names promoting indigenous civil rights, redistributing revenues from key exports such as oil, conducting fair and transparent elections, and ensuring fair treatment of citizens of different sexual orientations as the pressures social movements have placed on states, before listing its five country examples."),
 ("up from the local level",
  "EK IEF-2.A.4 states that grassroots social movements exert their power up from the local level to the regional, national, or international level, so power runs upward from where participants live rather than downward from a headquarters."),
 ("difficult for state-run military or law enforcement to suppress",
  "EK IEF-2.A.5 states that with limited organizational hierarchies such movements are difficult for state-run military or law enforcement to suppress, since there is no command structure for the state to remove."),
 ("attracting and mobilizing support among fellow citizens",
  "EK IEF-2.A.5 states that some social movements have difficulty in attracting and mobilizing support among fellow citizens or in negotiating with governmental representatives, which is the concession the same sentence attaches to the advantage it has just granted."),
 ("foster democratization and are in turn reinforced by it",
  "Enduring understanding IEF-2 states that strong and varied citizen organizations and movements foster and are reinforced by democratization, which makes the relationship mutual rather than running in one direction only."),
 ("corruption in the conduct of an election",
  "EK IEF-2.A.3.a names the Green Movement as protesting corruption in the 2009 election while EK IEF-2.A.3.e records protests over the State Duma's passage of legislation against same-sex couples, so one targets an electoral process and the other a legislative act."),
 ("worsened by a trade agreement",
  "EK IEF-2.A.3.c names protest against unjust methods of extraction and distribution of oil in the Niger Delta region and EK IEF-2.A.3.b names socioeconomic inequality and the negative impact of the North American Free Trade Agreement, and EK IEF-2.A.3 lists redistribution of revenues from key exports among the pressures movements apply."),
 ("since it is explicitly organized around one policy issue",
  "EK IEF-2.A.2 defines interest groups as explicitly organized to represent and advocate for a specific interest or policy issue, which a permanent staff working on a single bill satisfies, while a social movement is multiple groups and individuals pursuing broad social change."),
 ("multiple groups and individuals are advocating for broad social change",
  "EK IEF-2.A.2 states that social movements represent multiple groups and individuals advocating for broad social change and EK IEF-2.A.1 adds that they involve large groups pushing collectively, which is what separates them from a body organized around one policy issue."),
 ("hard to suppress but can also leave it unable to mobilize support",
  "EK IEF-2.A.5 states the advantage and the cost in a single sentence, and the scenario exhibits both at once: the movement survives repeated attempts to break it up and yet neither grows nor reaches agreement with governmental representatives."),
 ("the advantage is not free",
  "EK IEF-2.A.5 concedes that limited hierarchies frustrate suppression and in the same sentence states that they can hinder mobilizing fellow citizens and negotiating with governmental representatives, so the rebuttal is that both follow from one structural feature rather than that the advantage is untrue."),
 ("the lowest share of participants arrested and the fewest agreements",
  "EK IEF-2.A.5 states that limited organizational hierarchies make a movement hard to suppress but can leave it unable to negotiate with governmental representatives. Recomputed in q21 above, where both columns rise with leadership levels across all three rows, so the claim rests on the pattern and not on one row."),
 ("8",
  "Recomputed in q22 above by summing the negotiated-agreements column. The distractors are the arrest column's total, the leadership column's total, the largest single row, and two columns added together."),
 ("17 percentage points",
  "Recomputed in q23 above by subtracting the smallest arrest share from the largest. The distractors are the other two gaps in that column and its two extreme values read as though they were differences."),
 ("with more local groups taking part at each stage",
  "EK IEF-2.A.4 states that grassroots social movements exert their power up from the local level to the regional, national, or international level. Recomputed in q24 above, which reads the stage names as well as the counts, since the key asserts both an order and a trend."),
 ("300",
  "Recomputed in q25 above by summing the participation column across the four stages. The distractors are the two columns added together, the first and last stages added, the largest single stage, and the total with the smallest stage left out."),
 ("107",
  "Recomputed in q26 above by subtracting the first stage's figure from the third stage's. The distractors are the increases across three other pairs of stages and a raw stage figure read as an increase."),
 ("fair and transparent conduct of a disputed national election",
  "EK IEF-2.A.3.a states that the Green Movement in Iran protested corruption in the 2009 election, and EK IEF-2.A.3 names conducting fair and transparent elections among the four pressures. Recomputed in q27 above, where one row alone concerns an election."),
 ("redistribution of the revenues earned from oil exports",
  "EK IEF-2.A.3.c states that the Nigerian movements it names protest against unjust methods of extraction and distribution of oil in the Niger Delta region, and EK IEF-2.A.3 names redistributing revenues from key exports such as oil among the four pressures. Recomputed in q28 above, where one row alone concerns oil."),
 ("began with meetings in a handful of towns",
  "EK IEF-2.A.4 states that grassroots social movements exert their power up from the local level to the regional, national, or international level, so the supporting evidence must show power moving upward from where participants live rather than downward from a headquarters or outward from a governing party."),
 ("a loose structure both protects them and limits them",
  "EK IEF-2.A.2 supplies the distinction between the two kinds of body, EK IEF-2.A.3 the four pressures and five country instances, EK IEF-2.A.4 the upward direction of grassroots power, and EK IEF-2.A.5 both the protection and the limitation that follow from limited hierarchy."),
]

cg.check(k4_5, CLAIMS,
         table_checks={21: q21, 22: q22, 23: q23, 24: q24, 25: q25, 26: q26, 27: q27, 28: q28})
