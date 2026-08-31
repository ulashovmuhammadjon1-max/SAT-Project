"""Key audit for AP COMPARATIVE GOVERNMENT 4.4 Role of Political Party Systems.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
Learning objective PAU-4.B, two essential knowledge statements. PAU-4.B.1 opens
with three dimensions of variation -- RULES GOVERNING ELECTIONS, PARTY STRUCTURE
and LAWS REGULATING POLITICAL PARTIES -- and then gives eight country instances,
.a through .h. PAU-4.B.2 states that party systems vary in how they AFFECT AND
ARE AFFECTED BY citizen participation.

The eight country instances are the module's factual spine and every one of them
is keyed once as recall (items 2-3 China, 4 Iran, 5-6 Mexico, 7 Nigeria, 8-9
Russia, 10-11 the United Kingdom) before being used again in comparison and
application. Nothing about a country is asserted that is not in one of those
eight sentences.

THE TWO ITEMS MOST LIKELY TO BE GOT WRONG, and why the keys are what they are:

  Item 12 pairs PAU-4.B.1.g with PAU-4.B.1.h, which look contradictory: the same
  rule both diminishes minor-party representation and lets regional parties win
  seats. They are not contradictory because the rule is constant and the parties
  differ. Only the leading candidate in a district takes it, so support spread
  evenly across many districts converts into nothing while the same quantity of
  support concentrated in one region converts into the seats there. The key
  states that mechanism; every distractor invents an exemption the framework
  does not grant.

  Item 8 keys PAU-4.B.1.e's ELIMINATION AND THEN REINSTATEMENT. A student who
  has learned only that Russian rules restrict competition reads a reinstatement
  as another restriction. The framework says the change affected regional
  parties AND the representation of independent candidates, and single-member
  districts are the only route by which either wins, so removing the districts
  cut both and restoring them brought both back. Items 20-22 put that on data.

Item 16 keys PAU-4.B.1.b's phrase QUESTIONABLE LINKAGE TO CONSTITUENTS, which is
the only place in the eight statements where the framework itself doubts that a
party system carries citizens into policy -- the exact thing PAU-4.B is about.

TABLE FIGURES ARE HYPOTHETICAL and the module labels every table so. No number
in any table is asserted about a real country; the tables model the mechanisms
the framework describes, and the country identification in items 23 and 27 rests
on the SHAPE of the distribution, not on the specific figures.

DATA ITEMS
----------
Items 20-22 read the district-rule table, 23-26 the seat-share table, 27-28 the
quota table. Every arithmetic claim is recomputed below and every distractor is
checked to be a WRONG operation on the same table -- a distractor nobody can
derive teaches nothing. Item 20's key is a JOINT movement in two columns, so the
check verifies both fall and both recover; a table where only one column moved
would make the key half true. Item 27's key is a claim about three separate
comparisons, so the check recomputes the gap between seat share and population
share for every row both before and after, and requires it to narrow in all
three -- "every region" is not established by checking one.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k4_4

BIG1 = "Seats held by the largest party (percent)"
BIG2 = "Seats held by the second largest party (percent)"
NPARTY = "Number of parties holding at least one seat"

RULES = "Rules for filling the seats"
REGIONAL = "Seats won by regional parties"
INDEP = "Seats won by independent candidates"

POP = "Share of the national population (percent)"
BEFORE = "Share of federal legislative seats before quota rules (percent)"
AFTER = "Share of federal legislative seats after quota rules (percent)"


def _smd(table):
    return {lab: (str(table["rows"][i][1]),
                  cg.cell(table, lab, REGIONAL),
                  cg.cell(table, lab, INDEP))
            for i, lab in enumerate(cg.labels(table))}


def q20(table, item):
    v = _smd(table)
    e1, e2, e3 = v["Election 1"], v["Election 2"], v["Election 3"]
    assert "single-member district" in e1[0] and "single-member district" in e3[0], \
        "the first and third elections must be the ones using single-member districts"
    assert "single-member district" not in e2[0] and "party list" in e2[0], \
        f"the middle election must be the list-only one; its rule reads {e2[0]!r}"
    assert e1[1] > e2[1] < e3[1], f"regional-party seats must fall then recover; got {[e1[1], e2[1], e3[1]]}"
    assert e1[2] > e2[2] < e3[2], f"independent seats must fall then recover; got {[e1[2], e2[2], e3[2]]}"
    assert e2[2] == 0, "the list-only election must return no independents at all, since a list has no independents"
    assert e1[1] != e2[1] and e1[2] != e2[2], "'unaffected' must be false for both columns"
    return (f"regional-party seats go {[e1[1], e2[1], e3[1]]} and independents {[e1[2], e2[2], e3[2]]}, "
            "so both columns fall when the districts are removed and recover when they return")


def q21(table, item):
    ind = cg.col(table, INDEP)
    reg = cg.col(table, REGIONAL)
    total = sum(ind)
    assert total == 21, f"the keyed total recomputes to {total}"
    assert sum(reg) == 35, "the 35 distractor must be the other column's total"
    assert max(ind) == 12 and sorted(ind)[-2] == 9, \
        f"the 12 and 9 distractors must be the two nonzero rows of the keyed column; the column reads {ind}"
    assert total + sum(reg) == 56, "the 56 distractor must be the two columns added together"
    return f"the independent-candidate column reads {ind} and sums to {total:.0f}, with every distractor a wrong sum of the same table"


def q22(table, item):
    reg = cg.col(table, REGIONAL)
    ind = cg.col(table, INDEP)
    fall = reg[0] - reg[1]
    assert fall == 16, f"the keyed fall recomputes to {fall}"
    assert ind[0] - ind[1] == 12, "the 12 distractor must be the corresponding fall in the other column"
    assert reg[2] - reg[1] == 13, "the 13 distractor must be the change between the second and third elections"
    assert reg[2] == 15, "the 15 distractor must be the third election's own figure read as a change"
    assert reg[0] == 18, "the 18 distractor must be the first election's own figure read as a change"
    return f"the regional-party column reads {reg}, so the fall from the first election to the second is {fall:.0f} seats"


def _seats(table):
    return {lab: (cg.cell(table, lab, BIG1), cg.cell(table, lab, BIG2), cg.cell(table, lab, NPARTY))
            for lab in cg.labels(table)}


def q23(table, item):
    v = _seats(table)
    l1, l2, l3 = v["Legislature 1"], v["Legislature 2"], v["Legislature 3"]
    assert l1[0] + l1[1] >= 80, f"the keyed row's top two must dominate; they hold {l1[0] + l1[1]}"
    assert abs(l1[0] - l1[1]) <= 10, "the keyed row's top two must both be large, not one dominant party"
    assert l1[2] == 9, f"the keyed option says seven other parties also hold seats, so the row must seat 9; it seats {l1[2]}"
    assert l2[0] >= 70, f"the rejected dominant row must hold nearly three-quarters; it holds {l2[0]}"
    assert l3[0] + l3[1] < 60, f"the rejected fragmented row's top two must hold under three-fifths; they hold {l3[0] + l3[1]}"
    assert len({v[k][0] for k in v}) == 3, "'all three equally' must be false"
    return (f"the top-two shares are {[v[k][0] + v[k][1] for k in v]} percent against seated-party counts "
            f"{[v[k][2] for k in v]}, so one row alone shows two large parties with a tail behind them")


def q24(table, item):
    v = _seats(table)
    pair = {lab: v[lab][0] + v[lab][1] for lab in v}
    assert pair["Legislature 1"] == 86, f"the keyed combined share recomputes to {pair['Legislature 1']}"
    assert pair["Legislature 2"] == 83, "the 83 distractor must be another row's combined share"
    assert pair["Legislature 3"] == 58, "the 58 distractor must be the third row's combined share"
    assert v["Legislature 1"] == (46, 40, 9), f"the 46 and 40 distractors must be the keyed row's own two figures; it reads {v['Legislature 1']}"
    return f"the three combined top-two shares are {[pair[k] for k in pair]} percent, and the keyed row's is {pair['Legislature 1']:.0f}"


def q25(table, item):
    v = _seats(table)
    gap = v["Legislature 2"][0] - v["Legislature 3"][0]
    assert gap == 43, f"the keyed gap recomputes to {gap}"
    assert v["Legislature 2"][0] - v["Legislature 1"][0] == 28, "the 28 distractor must be another gap in the same column"
    assert v["Legislature 1"][0] - v["Legislature 3"][0] == 15, "the 15 distractor must be the remaining gap in that column"
    assert v["Legislature 2"][0] - v["Legislature 2"][1] == 65, \
        "the 65 distractor must be the gap between the second row's own two parties"
    assert max(v[k][0] for k in v) == 74, "the 74 distractor must be the largest single figure read as a gap"
    return f"the largest-party column reads {[v[k][0] for k in v]}, so the gap between the second and third rows is {gap:.0f} points"


def q26(table, item):
    v = _seats(table)
    l2 = v["Legislature 2"]
    assert l2[0] == max(v[k][0] for k in v), "the keyed row must hold the largest share in the column"
    assert l2[0] == 74 and l2[1] == 9, f"the keyed row reads {l2[0]}, {l2[1]}"
    assert l2[0] > 8 * l2[1], "the keyed row's leader must dwarf its runner-up, or the contest is not one-sided"
    assert abs(v["Legislature 1"][0] - v["Legislature 1"][1]) <= 10, \
        "the rejected close-contest row must indeed be close"
    assert v["Legislature 3"][2] == 12, f"the rejected twelve-party option must state that row truly; it reads {v['Legislature 3'][2]}"
    return f"the leader holds {l2[0]:.0f} percent against a runner-up on {l2[1]:.0f}, more than eight times as many seats"


def _quota(table):
    return {lab: (cg.cell(table, lab, POP), cg.cell(table, lab, BEFORE), cg.cell(table, lab, AFTER))
            for lab in cg.labels(table)}


def q27(table, item):
    v = _quota(table)
    for lab, (pop, before, after) in v.items():
        assert abs(after - pop) < abs(before - pop), (
            f"{lab} must end closer to its population share: it was {abs(before - pop)} away and is now {abs(after - pop)}"
        )
        assert before != after, f"{lab}'s seat share must actually change, or 'unchanged' would be defensible"
    assert sum(v[k][1] for k in v) == 100 and sum(v[k][2] for k in v) == 100, \
        "both seat columns must total 100 percent, or the rows are not a whole chamber"
    assert sum(v[k][0] for k in v) == 100, "the population column must total 100 percent"
    assert len({v[k][2] for k in v}) == 3, "'an equal share for every region' must be false"
    return ("before the rules the three seat shares sit "
            f"{[abs(v[k][1] - v[k][0]) for k in v]} points from their populations and after them "
            f"{[abs(v[k][2] - v[k][0]) for k in v]}, so every row narrows")


def q28(table, item):
    v = _quota(table)
    fell = [lab for lab in v if v[lab][2] < v[lab][1]]
    assert fell == ["Region 1"], f"exactly one row's seat share may fall; these fell: {fell}"
    drop = v["Region 1"][1] - v["Region 1"][2]
    assert drop == 14, f"the keyed fall recomputes to {drop}"
    assert v["Region 1"][1] - v["Region 1"][0] == 16, \
        "the 16 distractor must be that row's gap from its own population share"
    assert v["Region 3"][2] - v["Region 3"][1] == 12, "the 12 distractor must be the third row's rise"
    assert v["Region 2"][2] - v["Region 2"][1] == 2, "the 2 distractor must be the second row's rise"
    assert abs(v["Region 2"][1] - v["Region 2"][0]) == 3, \
        "the 3 distractor must be the second row's original gap from its population share"
    return f"only the first row falls, from {v['Region 1'][1]:.0f} to {v['Region 1'][2]:.0f} percent, a fall of {drop:.0f} points"


CLAIMS = [
 ("rules governing elections, party structure, and laws regulating political parties",
  "EK PAU-4.B.1 states that party systems vary across the course countries in terms of rules governing elections, party structure, and laws regulating political parties, and the eight country instances that follow are grouped under those three headings."),
 ("the government and the military",
  "EK PAU-4.B.1.a states that in China one party, the Communist Party of China, has controlled the government and the military since 1949. The framework names the military alongside the government, which is what separates this from ordinary party government."),
 ("fill minor political offices",
  "EK PAU-4.B.1.a states that minor parties have limited power to fill minor political offices, so their existence sits alongside one party's control of the government and the military rather than qualifying it."),
 ("loosely formed political alliances",
  "EK PAU-4.B.1.b states that Iran lacks formal political party structures and that parties operate as loosely formed political alliances with questionable linkage to constituents."),
 ("Party of the Democratic Revolution",
  "EK PAU-4.B.1.c states that Mexico's multiparty system is dominated by the National Action Party, the Party of the Democratic Revolution and the Institutional Revolutionary Party. The rejected sets are the framework's leading parties in Nigeria, the United Kingdom and China."),
 ("coalitions to nominate candidates for any particular election",
  "EK PAU-4.B.1.c states that parties are allowed to form coalitions to nominate candidates for any particular election, so the phrase any particular election permits a coalition assembled contest by contest."),
 ("multiple parties operating alongside ethnic quotas",
  "EK PAU-4.B.1.d states that in Nigeria multiple parties with ethnic quotas affect representation in the country's federal legislature, so party competition and an ethnic allocation rule operate at the same time."),
 ("regional parties and independent candidates",
  "EK PAU-4.B.1.e states that the elimination and then reinstatement of single-member districts has affected regional parties and the representation of independent candidates, both of which depend on carrying a particular district rather than on a share of a national list."),
 ("changing threshold rules",
  "EK PAU-4.B.1.e states that diminished representation of smaller parties in Russia occurs because of changing threshold rules, and smaller parties are the ones nearest the line a raised threshold draws."),
 ("Labour and Conservative",
  "EK PAU-4.B.1.f states that in the United Kingdom two large parties, Labour and Conservative, dominate the House of Commons. The rejected pairs are the framework's leading parties in Mexico and Nigeria."),
 ("they diminish minor-party representation",
  "EK PAU-4.B.1.g states that single-member district plurality elections in the United Kingdom diminish minor-party representation, because a party finishing second in every district converts none of its votes into seats."),
 ("concentrated in one region can carry the districts there",
  "EK PAU-4.B.1.g and EK PAU-4.B.1.h are both about single-member districts, so the difference must lie in the parties rather than the rule, and EK DEM-2.B.2's plurality rule supplies the mechanism, since only the leading candidate in a district converts votes into a seat."),
 ("vary in how they affect and are affected by citizen participation",
  "EK PAU-4.B.2 states that party systems across the course countries vary in how they affect and are affected by citizen participation, which makes the relationship run in both directions."),
 ("lacks formal party structures altogether",
  "EK PAU-4.B.1.a describes a party that has controlled the government and military since 1949 with minor parties confined to minor offices, while EK PAU-4.B.1.b states that Iran lacks formal political party structures. A durable party monopoly and the absence of formal parties are different arrangements."),
 ("ethnic quotas shape who is represented in the federal legislature",
  "EK PAU-4.B.1.c gives Mexico three dominant parties permitted to form coalitions to nominate candidates for any particular election, and EK PAU-4.B.1.d gives Nigeria multiple parties whose ethnic quotas affect federal legislative representation."),
 ("questionable linkage to constituents",
  "EK PAU-4.B.1.b is the only one of the eight country statements to describe linkage to constituents as questionable, and EK PAU-4.B is about how party systems link citizen participation to policy making, so that phrase is the framework's own judgement on linkage."),
 ("form coalitions to nominate candidates for any particular election",
  "EK PAU-4.B.1.c states that Mexican parties may form coalitions to nominate candidates for any particular election, and the words any particular election are what allow a coalition lasting one contest."),
 ("ethnic quotas affecting federal legislative representation",
  "EK PAU-4.B.1.d is the framework's only case of an ethnic allocation rule operating on the composition of a legislature, stating that multiple parties with ethnic quotas affect representation in Nigeria's federal legislature."),
 ("competitive election rules and still have parties that are loose alliances",
  "EK PAU-4.B.1 names rules governing elections and party structure as two separate dimensions, and EK PAU-4.B.1.a and EK PAU-4.B.1.b show them coming apart, since a durably organized governing party and the absence of formal party structures both coexist with elections being held."),
 ("both recovered when the districts returned",
  "EK PAU-4.B.1.e states that the elimination and then reinstatement of single-member districts has affected regional parties and the representation of independent candidates. Recomputed in q20 above, where both columns fall with the districts and rise again with them."),
 ("21",
  "Recomputed in q21 above by summing the independent-candidate column across the three elections. The distractors are the other column's total, each of the two nonzero rows on its own, and the two columns added together."),
 ("16 seats",
  "Recomputed in q22 above by subtracting the second election's regional-party figure from the first. The distractors are the same fall in the other column, the later change, and the first and third elections' own figures read as changes."),
 ("seven other parties still hold seats",
  "EK PAU-4.B.1.f states that two large parties dominate the House of Commons and EK PAU-4.B.1.h that single-member districts allow regional parties to win legislative seats, so the matching distribution is two dominant parties with a tail behind them. Recomputed in q23 above."),
 ("86 percent",
  "Recomputed in q24 above by adding that row's two seat shares. The distractors are the combined shares of the other two rows and each of the keyed row's own two figures."),
 ("43 percentage points",
  "Recomputed in q25 above by subtracting the smaller largest-party share from the larger. The distractors are the other two gaps in that column, the gap between one row's own two parties, and the largest single figure read as a gap."),
 ("74 percent of the seats and the next party holds 9 percent",
  "EK PAU-4.A.1 places dominant party systems at one end of the framework's range of party systems. Recomputed in q26 above: the leading party holds more than eight times the runner-up's seats, which is that end shown in data rather than a close contest."),
 ("moved closer to its share of the national population",
  "EK PAU-4.B.1.d states that ethnic quotas affect representation in Nigeria's federal legislature. Recomputed in q27 above for all three rows, both before and after, so the claim about every region is established row by row rather than from one case."),
 ("the first region, by 14 percentage points",
  "Recomputed in q28 above; only one row's seat share is lower after the rules than before. The distractors are that row's gap from its own population share, the rises in the other two rows, and another row's original gap."),
 ("vary in how they affect and are affected by citizen participation",
  "EK PAU-4.B.2 states that party systems vary in how they affect and are affected by citizen participation, and EK PAU-4.B.1.b's questionable linkage to constituents is the framework's own instance of the weaker case."),
 ("how far a citizen's participation reaches into policy making",
  "EK PAU-4.B.1 names three dimensions of variation and gives eight country instances of them, and EK PAU-4.B.2 states that party systems vary in how they affect and are affected by citizen participation, which is the link the learning objective asks about."),
]

cg.check(k4_4, CLAIMS,
         table_checks={20: q20, 21: q21, 22: q22, 23: q23, 24: q24, 25: q25, 26: q26, 27: q27, 28: q28})
