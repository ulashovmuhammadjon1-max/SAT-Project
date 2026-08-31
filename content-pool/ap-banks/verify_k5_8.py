"""Key audit for AP COMPARATIVE GOVERNMENT 5.8 Causes and Effects of Demographic
Change.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
Learning objective LEG-4.A, five essential knowledge statements: LEG-4.A.1's
motivations (GROWING POPULATIONS, CHANGING LAND USE AND VALUES, ECONOMIC
OPPORTUNITIES) and its SIGNIFICANT CHALLENGES TO GOVERNMENTAL RESOURCES;
LEG-4.A.2's four country instances (.a China rural-to-urban and west-to-east,
.b highly skilled people leaving Iran and Nigeria, .c Mexico's southern-to-
northern movement and its north-south development gap, .d positive net migration
into the United Kingdom producing SOCIAL AND POLITICAL TENSIONS); LEG-4.A.3's
four consequences, the last of which CHALLENGES THE GOVERNMENT'S LEGITIMACY;
LEG-4.A.4's health care pressure in the United Kingdom; and LEG-4.A.5's policy
responses reaching into BIRTH RATES and the treatment of RELIGIOUS MINORITIES.

THE SUGGESTED SKILL HERE IS THE LIMITATIONS OF DATA, and it shapes the module.
TWO of the nine data items ask what a table CANNOT establish:

  Item 23. A population table records how many people are in a place, not why the
  number changed, so it cannot separate migration from births and deaths. That
  objection is not a quibble about the table's size or precision -- the three
  rejected objections are deliberately of that weaker kind, because the skill
  being taught is distinguishing a real limitation from a complaint.

  Item 26. A table of arrivals and departures records movement, not motive, so it
  cannot on its own establish EK LEG-4.A.2.b's stated reason for leaving. This is
  the sharper case: the framework DOES make the motive claim, and the point is
  that this data would not be what established it.

A bank that only ever asks what a table shows never teaches the skill the CED
names for this topic, which is why both items are here rather than a ninth
arithmetic item.

WHAT IS DELIBERATELY NOT ASSERTED: no migration figure, population count, health
expenditure, tax rate or election result of any real country. Every table is
HYPOTHETICAL, labelled so, and attached to unnamed regions or occupational
groups. The country-specific claims are exactly the framework's own and all of
them are structural rather than numerical.

DATA ITEMS
----------
Items 21-23 read the population table, 24-26 the occupational table, 27-29 the
aging table. Every arithmetic distractor is verified below to be a wrong
operation on the same table. Item 22's check confirms that one region's change is
NEGATIVE, since the whole point of that item is that a student who adds only the
gains gets a listed wrong answer.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k5_8

START = "Population at the start of the decade (thousands)"
END = "Population at the end of the decade (thousands)"
OUT = "People leaving the country in a year"
IN_ = "People entering the country in a year"
OLD = "People aged 65 and over (percent of the population)"
RATIO = "Working-age people for each person aged 65 and over"
SPEND = "Health spending per person (index)"


def _pop(table):
    return {lab: cg.cell(table, lab, END) - cg.cell(table, lab, START) for lab in cg.labels(table)}


def q21(table, item):
    v = _pop(table)
    top = max(v, key=v.get)
    assert top == "Coastal region", f"the largest gain belongs to {top}"
    assert v["Coastal region"] == 4500, f"the keyed gain recomputes to {v['Coastal region']}"
    assert v["Capital district"] == 1200, "the first rejected option must state its own row's true gain"
    assert v["Interior region"] == -1600, \
        f"the interior row must have LOST 1600, so the option calling it a gain is false; it changed by {v['Interior region']}"
    assert any(c > 0 for c in v.values()), "'every region lost population' must be false"
    assert len(set(v.values())) == 3, "'all three equally' must be false"
    return f"the three changes are {[v[l] for l in v]} thousand, the largest gain {v[top]:.0f}"


def q22(table, item):
    v = _pop(table)
    net = sum(v.values())
    assert net == 4100, f"the keyed net change recomputes to {net}"
    gains = [c for c in v.values() if c > 0]
    assert len(gains) == 2 and sum(gains) == 5700, \
        f"the 5700 distractor must be the gains added with the loss ignored; the gains are {gains}"
    assert max(v.values()) == 4500, "the 4500 distractor must be the largest single gain"
    assert v["Coastal region"] + v["Interior region"] == 2900, \
        "the 2900 distractor must be the two extreme regions netted against each other"
    assert min(gains) == 1200, "the 1200 distractor must be the smallest gain"
    assert any(c < 0 for c in v.values()), \
        "one region must have lost population, or adding only the gains would not be a distinct wrong answer"
    return f"the three changes are {[v[l] for l in v]} thousand and net to {net:.0f}"


def q23(table, item):
    heads = [h.lower() for h in table["headers"]]
    assert not any("migrat" in h or "birth" in h or "death" in h or "reason" in h for h in heads), (
        "the table must contain no column recording migration, births, deaths or reasons, "
        f"or the keyed objection would be false; its headers are {table['headers']}"
    )
    assert len(heads) == 3, f"the table must be a plain start-and-end population count; it has {len(heads)} columns"
    v = _pop(table)
    assert len(v) == 3, "the table must have three regions, so the rejected objection about its size is testable"
    return "the table carries only start and end populations, with no column for migration, births, deaths or reasons"


def _occ(table):
    return {lab: (cg.cell(table, lab, OUT), cg.cell(table, lab, IN_)) for lab in cg.labels(table)}


def q24(table, item):
    v = _occ(table)
    net = {lab: v[lab][0] - v[lab][1] for lab in v}
    top = max(net, key=net.get)
    assert top == "Engineers", f"the largest net loss falls on {top}"
    assert net["Engineers"] == 1560, f"the keyed net loss recomputes to {net['Engineers']}"
    assert net["Physicians"] == 1140, "the first rejected option must state the other skilled group's true net loss"
    assert net["Manual workers"] == -700, \
        f"the manual workers row must be a net GAIN of 700, so the option calling it a loss is false; it is {net['Manual workers']}"
    assert v["Engineers"][0] == 2100 and v["Physicians"][1] != 3200, \
        "the 2100 and 3200 distractors must be raw departure figures rather than net figures"
    return f"the three net figures are {[net[l] for l in net]}, the largest net loss {net[top]:.0f}"


def q25(table, item):
    out, inn = cg.col(table, OUT), cg.col(table, IN_)
    total = sum(out)
    assert total == 6700, f"the keyed total recomputes to {total}"
    assert sum(inn) == 4700, "the 4700 distractor must be the other column's total"
    assert total - min(out) == 5300, "the 5300 distractor must be the total with the smallest group omitted"
    assert sum(sorted(out)[:2]) == 3500, "the 3500 distractor must be the two smallest groups added"
    assert total + sum(inn) == 11400, "the 11400 distractor must be the two columns added together"
    return f"the departure column reads {out} and sums to {total:.0f}"


def q26(table, item):
    heads = [h.lower() for h in table["headers"]]
    assert not any("reason" in h or "why" in h or "motive" in h for h in heads), (
        "the table must contain no column recording a reason, or the keyed objection would be false; "
        f"its headers are {table['headers']}"
    )
    v = _occ(table)
    assert len(v) == 3, "the table must have three occupational groups, so the rejected objection about its size is testable"
    assert all(a > 0 and b > 0 for a, b in v.values()), \
        "both directions must be recorded for every group, so the objection is about motive and not about missing movement"
    return "the table records movement in both directions for every group and carries no column recording a reason"


def q27(table, item):
    old, ratio, spend = cg.col(table, OLD), cg.col(table, RATIO), cg.col(table, SPEND)
    assert old == sorted(old), f"the older share must rise; it reads {old}"
    assert ratio == sorted(ratio, reverse=True), f"the support ratio must fall; it reads {ratio}"
    assert spend == sorted(spend), f"health spending must rise; it reads {spend}"
    assert len(set(spend)) == 3, "'spending unchanged' must be false"
    assert not (old == sorted(old) and ratio == sorted(ratio)), \
        "'all three columns moved in the same direction' must be false, so the support ratio must move against the other two"
    return f"the older share goes {old}, the support ratio {ratio} and spending {spend}"


def q28(table, item):
    old, spend = cg.col(table, OLD), cg.col(table, SPEND)
    rise = old[2] - old[0]
    assert rise == 9, f"the keyed rise recomputes to {rise}"
    assert old[2] - old[1] == 5, "the 5 distractor must be the rise between the second and third years"
    assert old[1] - old[0] == 4, "the 4 distractor must be the rise between the first and second years"
    assert old[2] == 23, "the 23 distractor must be the final share read as a rise"
    assert spend[2] - spend[0] == 61, "the 61 distractor must be the change in the spending column"
    return f"the older-share column reads {old}, so it rises {rise:.0f} percentage points"


def q29(table, item):
    spend, old = cg.col(table, SPEND), cg.col(table, OLD)
    rise = spend[2] - spend[0]
    assert rise == 61, f"the keyed rise recomputes to {rise}"
    assert spend[2] - spend[1] == 33, "the 33 distractor must be the rise between the second and third years"
    assert spend[1] - spend[0] == 28, "the 28 distractor must be the rise between the first and second years"
    assert spend[0] == 100, "the 100 distractor must be the index's own starting value read as a rise"
    assert old[2] - old[0] == 9, "the 9 distractor must be the change in the age column"
    return f"the spending column reads {spend}, so it rises {rise:.0f} points"


CLAIMS = [
 ("growing populations, changing land use and values, and economic opportunities",
  "EK LEG-4.A.1 states that growing populations, changing land use and values, and economic opportunities motivate internal and external population movements."),
 ("significant challenges to governmental resources",
  "EK LEG-4.A.1 states that the corresponding demographic changes pose significant challenges to governmental resources, which is why the topic sits under an enduring understanding about a government's legitimacy."),
 ("preexisting class and regional differences",
  "EK LEG-4.A.2 states that government policies and employment opportunities can draw workers to different geographic regions or influence migration rates, often deepening preexisting class and regional differences and taxing government resources."),
 ("west to east from the interior to the coast",
  "EK LEG-4.A.2.a states that China's shift from agriculture to industry, its special economic zones, its encouragement of foreign direct investment and its reduction of restrictions have led to migration from rural to urban areas and west to east, from the interior to the coast."),
 ("the pursuit of work and educational opportunities abroad",
  "EK LEG-4.A.2.a states that the growing population created by that movement has rising incomes allowing them to pursue work and educational opportunities abroad, which turns an internal movement into an external one."),
 ("perceived as limiting, corrupt, or repressive",
  "EK LEG-4.A.2.b states that highly skilled or well-educated individuals have left home countries such as Iran and Nigeria to escape government policies or practices that are perceived as limiting, corrupt, or repressive."),
 ("maquiladora zones",
  "EK LEG-4.A.2.c names the North American Free Trade Agreement and other economic liberalization policies such as removing agricultural subsidies, maquiladora zones, and foreign direct investment patterns as what prompted migration within Mexico."),
 ("greater economic development in the north than in the south",
  "EK LEG-4.A.2.c states that those changes contributed to greater economic development in the north than in the south, as well as other regional disparities."),
 ("social and political tensions",
  "EK LEG-4.A.2.d states that a positive net migration of immigrants into countries like the United Kingdom has resulted in social and political tensions."),
 ("increased crime stemming from higher population density",
  "EK LEG-4.A.3 lists increased crime from higher population density, the concentration and absence of highly skilled individuals, heavier use of and demand for infrastructure and housing, and the growth of new parties standing against immigration and supranational organizations."),
 ("concentrated in certain areas and absent from others",
  "EK LEG-4.A.3.b names the concentration of highly skilled individuals in certain areas and their absence in other areas as a consequence of shifting migration patterns."),
 ("stand against immigration and supranational organizations",
  "EK LEG-4.A.3.d names the growth of new political parties that stand against immigration and supranational organizations that challenge the government's legitimacy, which is why demographic change falls under an enduring understanding about legitimacy."),
 ("declining working-age population facing increased tax burdens",
  "EK LEG-4.A.4 states that the political leadership of the United Kingdom faces increasing constituent demands to reduce the rising costs of health care, exacerbated by an aging population and a declining working-age population faced with increased tax burdens to fund the universal health care system."),
 ("encouraging or discouraging the birth of children",
  "EK LEG-4.A.5 states that states respond to demographic pressures with actions or policies that influence citizen behavior, including policies encouraging or discouraging the birth of children or actions promoting or discouraging discrimination against religious minorities."),
 ("movement within a country driven by where the work is",
  "EK LEG-4.A.2.a attributes movement within China to economic change and where the work is, while EK LEG-4.A.2.b attributes the departure of highly skilled individuals from countries such as Iran to policies or practices perceived as limiting, corrupt, or repressive."),
 ("driven in each case by where liberalization drew investment and work",
  "EK LEG-4.A.2.a records rural to urban and west to east movement in China following special economic zones and foreign direct investment, and EK LEG-4.A.2.c records rural to urban and southern to northern movement in Mexico following liberalization policies, maquiladora zones and foreign direct investment patterns."),
 ("together with their concentration in certain areas and absence in others",
  "EK LEG-4.A.2.b records highly skilled or well-educated individuals leaving their home countries and EK LEG-4.A.3.b names the resulting concentration of such individuals in certain areas and their absence in others."),
 ("challenge the government's legitimacy",
  "EK LEG-4.A.3.d names the growth of new political parties that stand against immigration and supranational organizations that challenge the government's legitimacy, and the scenario contains all three elements of that statement."),
 ("demands for new and expanded infrastructure and housing",
  "EK LEG-4.A.3.c names increased use of existing infrastructure and housing together with demands for new and expanded infrastructure and housing among the consequences of shifting migration patterns."),
 ("waiting lists lengthened",
  "EK LEG-4.A.1 states that demographic changes pose significant challenges to governmental resources and EK LEG-4.A.2 that such movements tax government resources, so the supporting finding must pair a population change with a strain on provision."),
 ("gained 4500 thousand",
  "EK LEG-4.A.2.a records migration from the interior toward the coast, so the comparison is of the kind the framework describes. Recomputed in q21 above, which also confirms that one region lost population, making the option describing it as a gain false."),
 ("an increase of 4100 thousand",
  "Recomputed in q22 above by adding all three changes including the negative one. The distractors come from adding only the gains, taking the largest single gain, netting only the two extreme regions, and taking the smallest gain."),
 ("not why the numbers changed",
  "EK LEG-4.A.1 names growing populations both as a motivation for movement and as a demographic change in itself, so a population total reflects natural change as well as migration. Recomputed in q23 above, which confirms the table has no column for migration, births, deaths or reasons."),
 ("engineers, with a net loss of 1560",
  "EK LEG-4.A.2.b records highly skilled or well-educated individuals leaving their home countries. Recomputed in q24 above, which also confirms that one group shows a net gain, so the option describing it as a loss is false."),
 ("6700",
  "Recomputed in q25 above by summing the departure column. The distractors are the other column's total, the total with the smallest group omitted, the two smallest groups added, and the two columns added together."),
 ("nothing about their reasons",
  "EK LEG-4.A.2.b's claim is about motive, and a table of arrivals and departures records movement rather than reasons. Recomputed in q26 above, which confirms the table carries no column recording a reason and that both directions are recorded for every group, so the objection is about motive and not about missing data."),
 ("the number of working-age people supporting each of them fell",
  "EK LEG-4.A.4 attributes rising health care costs to an aging population and a declining working-age population. Recomputed in q27 above, where the support ratio moves against the other two columns, which is what makes the rejected option about all three moving together false."),
 ("9 percentage points",
  "Recomputed in q28 above by subtracting the first year's share from the third year's. The distractors are the rises between the other pairs of years, the final share read as a rise, and the change in the spending column."),
 ("61 points",
  "Recomputed in q29 above by subtracting the first year's index from the third year's. The distractors are the rises between the other pairs of years, the index's own starting value, and the change in the age column."),
 ("new parties that challenge a government's legitimacy",
  "EK LEG-4.A.1 supplies the motivations and the strain on governmental resources, EK LEG-4.A.2 the role of policy and the deepening of class and regional differences, EK LEG-4.A.3 the four consequences including the challenge to legitimacy, and EK LEG-4.A.5 the range of state responses."),
]

cg.check(k5_8, CLAIMS,
         table_checks={21: q21, 22: q22, 23: q23, 24: q24, 25: q25, 26: q26, 27: q27, 28: q28, 29: q29})
