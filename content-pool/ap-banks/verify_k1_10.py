"""Key audit for AP COMPARATIVE GOVERNMENT 1.10 Political Stability.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
  LEG-1.C.1  internal actors can BOLSTER OR UNDERMINE regime stability and rule of
             law, represented by .a contrasting methods to combat political
             corruption among the six, .b state responses to separatist group
             violence, drug trafficking and discrimination based on gender or
             religious differences in IRAN, MEXICO and NIGERIA, .c VARIED state
             responses to mass protest movements
  LEG-1.C.2  state authorities OF DIFFERENT REGIME TYPES limit divisive and violent
             actors TO ATTRACT PRIVATE CAPITAL AND FOREIGN DIRECT INVESTMENT and
             improve growth
  LEG-1.C.3  ACROSS THE COURSE COUNTRIES, reform pressure from citizen protest
             groups and civil society can create institutions or policies to
             protect civil liberties, improve transparency, address election
             fairness and media bias, limit corruption, and ensure equality under
             law

Supporting statements: LEG-2.B.2.b (responses ranging from brute repression to
autonomous regions), LEG-2.B.4.a-c (the two country lists and the Nigeria-Mexico
comparison), LEG-2.B.5 (challenges in multinational states), DEM-1.B.4
(authoritarian regimes tolerate mass protest less), PAU-1.C.3, MPA-1.A.3.

THE PAIRING STUDENTS GET BACKWARDS
----------------------------------
LEG-2.B.4.a names China, Iran, Nigeria, Russia and the United Kingdom for
separatist movements; LEG-2.B.4.b names MEXICO AND THE UNITED KINGDOM for groups
demanding autonomy but not independence. The United Kingdom is on both lists and
Mexico only on the second, which is not what a reader guesses from the trio in
LEG-1.C.1.b. Items 10, 11 and 12 key each half separately so the distinction has
to be held rather than approximated (AP_COMP_GOV_CED.md note 14).

TWO GENERALITY CLAUSES KEYED
----------------------------
LEG-1.C.2 opens 'state authorities of different regime types' and LEG-1.C.3 opens
'Across the course countries'. Items 6 and 8 key those clauses, because the
natural assumption -- that limiting violent actors for investment is an
authoritarian habit, or that civil society pressure only works in democracies --
is not the framework's.

DATA ITEMS
----------
Suggested skill 3.D for this topic is Data Analysis. Items 20-22 share a
violence-and-investment table and 23-25 a protest-response table, both
HYPOTHETICAL and labelled so. Item 23 turns on reading each row as a PROPORTION
rather than a count, and item 25 is the causal brake.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k1_10

V2015 = "Recorded incidents of political violence, 2015"
V2020 = "Recorded incidents of political violence, 2020"
FDI = "Net foreign direct investment inflow as a share of GDP, 2020 (percent)"
EPS = "Number of episodes"
NEW = "Episodes followed within two years by a new institution or policy protecting civil liberties"


def _stab(table):
    return ({lab: cg.cell(table, lab, V2020) - cg.cell(table, lab, V2015) for lab in cg.labels(table)},
            {lab: cg.cell(table, lab, FDI) for lab in cg.labels(table)})


def q20(table, item):
    d, fdi = _stab(table)
    assert d["Country U"] == -216, f"the keyed fall of 216 recomputes to {d['Country U']}"
    assert min(d, key=d.get) == "Country U", "the keyed row must show the largest fall in incidents"
    assert max(fdi, key=fdi.get) == "Country U", f"the highest investment share belongs to {max(fdi, key=fdi.get)}"
    assert d["Country W"] == -4, f"the small-fall distractor recomputes to {d['Country W']}"
    assert d["Country V"] > 0, "one row must rise, so 'all three equally' is false"
    return "one row falls by 216 incidents and also holds the highest investment share, so both halves of the claim appear together"


def q21(table, item):
    d, fdi = _stab(table)
    assert cg.cell(table, "Country V", V2015) == 120 and cg.cell(table, "Country V", V2020) == 260, \
        "the keyed choice quotes the two figures, which must match the table"
    assert d["Country V"] == max(d.values()) and d["Country V"] > 0, "only the keyed row may rise"
    assert min(fdi, key=fdi.get) == "Country V", f"the lowest investment share belongs to {min(fdi, key=fdi.get)}"
    assert cg.cell(table, "Country V", V2020) > 2 * cg.cell(table, "Country V", V2015), \
        "'more than doubled' must be true of the keyed row"
    low = min(cg.col(table, V2015)), min(cg.col(table, V2020))
    assert cg.cell(table, "Country W", V2015) == low[0] and cg.cell(table, "Country W", V2020) == low[1], \
        "the rejected 'lowest in both years' option must state a true fact about a different row"
    return "one row rises from 120 to 260, more than double, and also holds the lowest investment share"


def q22(table, item):
    d, _ = _stab(table)
    lab = min(d, key=d.get)
    start = cg.cell(table, lab, V2015)
    pct = -d[lab] / start * 100
    assert abs(pct - 70) < 1.0, f"the proportional fall is {pct:.1f} percent, not close enough to 70"
    remaining = cg.cell(table, lab, V2020) / start * 100
    assert abs(remaining - 30) < 1.0, "the 30 percent distractor must be the REMAINING share, the classic wrong reading"
    other = -d["Country W"] / cg.cell(table, "Country W", V2015) * 100
    assert abs(other - 9) < 1.0, "the 9 percent distractor must be another row's proportional fall"
    assert -d[lab] == 216, "the 216 percent distractor must be the absolute drop misread as a percentage"
    return f"the largest fall is {-d[lab]:.0f} of {start:.0f}, or {pct:.1f} percent, against a remaining share of {remaining:.1f}"


def _resp(table):
    return {str(r[0]): (cg.cell(table, r[0], EPS), cg.cell(table, r[0], NEW)) for r in table["rows"]}


def q23(table, item):
    v = _resp(table)
    share = {lab: k / n for lab, (n, k) in v.items()}
    accommodating = ["Negotiate and concede some demands", "Recognize the group and create a consultative body"]
    other = [lab for lab in v if lab not in accommodating]
    assert min(share[l] for l in accommodating) > 3 * max(share[l] for l in other), \
        f"the accommodating shares must dominate; got {share}"
    assert share["Ban the protest and disperse it"] < share["Negotiate and concede some demands"], \
        "'banned followed more often than negotiated' must be false"
    assert all(k < n for n, k in v.values()), "'every episode' must be false"
    assert any(k > 0 for _, k in v.values()), "'no episode' must be false"
    assert v["Ban the protest and disperse it"][0] > v["Recognize the group and create a consultative body"][0], \
        "'banned fewer than recognized' must be false"
    return f"read as proportions the four rows give {[round(share[l], 2) for l in v]}, separating the accommodating pair sharply"


def q24(table, item):
    n, k = _resp(table)["Ban the protest and disperse it"]
    pct = k / n * 100
    assert pct == 5, f"the keyed 5 percent recomputes to {pct}"
    assert k == 2 and n == 40, "the 2 and 40 distractors must be the raw count and the row total"
    neg_n, neg_k = _resp(table)["Negotiate and concede some demands"]
    assert round(neg_k / neg_n * 100) == 76, "the 76 percent distractor must be another row's share"
    return f"{k:.0f} of {n:.0f} banned episodes is {pct:.0f} percent, while the distractors offer the count, the total and another row's share"


def q25(table, item):
    v = _resp(table)
    assert len(v) == 4, "the objection turns on there being four categories of response"
    share = {lab: k / n for lab, (n, k) in v.items()}
    assert max(share.values()) - min(share.values()) > 0.5, \
        "the association must be real, or the objection would be to the reading rather than to the inference"
    return "the four response categories differ by more than fifty points in proportion, so the association is real and only the causal step fails"


CLAIMS = [
 ("bolster or undermine",
  "EK LEG-1.C.1 states that internal actors can interact with governments to bolster or undermine regime stability and rule of law. The statement is deliberately two-directional, so any reading that permits only one direction contradicts it."),
 ("combat political corruption among the six",
  "EK LEG-1.C.1.a names contrasting methods to combat political corruption among the six course countries as one of three illustrations of internal actors interacting with state authority. Supranational operations and encroachment by neighbors are external actors, treated at EK PAU-2.A.2 and EK LEG-2.B.5.d."),
 ("in Iran, Mexico, and Nigeria",
  "EK LEG-1.C.1.b pairs separatist group violence, drug trafficking, and discrimination based on gender or religious differences with Iran, Mexico and Nigeria. Both halves are the framework's, so substituting a different trio of countries loses the statement's support."),
 ("varied state responses",
  "EK LEG-1.C.1.c names varied state responses to mass protest movements that oppose governmental policies or their equal enforcement. The word 'varied' is the framework's own, and EK LEG-2.B.2.b describes the range along which those responses fall."),
 ("attract more private capital",
  "EK LEG-1.C.2 gives the motive as attracting more private capital and foreign direct investment and improving economic growth, linking internal order to an economic objective rather than an institutional or diplomatic one."),
 ("different regime types",
  "EK LEG-1.C.2 opens with 'state authorities of different regime types', placing the behavior on both sides of the democratic-authoritarian divide. This follows the pattern of EK DEM-1.C.2 and EK DEM-1.B.3, which assign a practice to both types and distinguish them by degree."),
 ("election fairness and media bias",
  "EK LEG-1.C.3 lists protecting civil liberties, improving transparency, addressing election fairness and media bias, limiting corruption and ensuring equality under law as the purposes of institutions created by reform pressure. The economic objectives belong to EK LEG-1.C.2 instead."),
 ("since the statement opens",
  "EK LEG-1.C.3 opens with 'Across the course countries', the framework's phrase for the whole set of six, and EK LEG-1.C.2 uses the parallel 'state authorities of different regime types'. Both statements are deliberately general rather than confined to one regime type."),
 ("brute repression to recognition",
  "EK LEG-2.B.2.b states that state responses can range from brute repression to recognition of ethnic and religious minorities and the creation of autonomous regions and/or representation of minorities in governmental institutions. Both endpoints are the framework's own words."),
 ("China, Iran, Nigeria, Russia",
  "EK LEG-2.B.4.a names China, Iran, Nigeria, Russia and the United Kingdom as the countries where separatist movements have emerged from social cleavages. Mexico is absent from this list, which is why naming every country, or reusing the trio from EK LEG-1.C.1.b, fails."),
 ("Mexico and the United Kingdom",
  "EK LEG-2.B.4.b names Mexico and the United Kingdom as the countries where groups demanding autonomy but not independence have emerged. The five-country list belongs to EK LEG-2.B.4.a and concerns separatist movements."),
 ("the United Kingdom",
  "EK LEG-2.B.4.a's five countries and EK LEG-2.B.4.b's two overlap in exactly one country. Mexico appears only on the second list, which is the half of this pairing a student is most likely to reverse."),
 ("valuing public order more",
  "EK DEM-1.B.4 states that authoritarian regimes tolerate mass political protests and movements less than democratic regimes, valuing public order more than individual liberties and civil rights. EK DEM-1.B.3 adds that both types regulate formal participation, so the difference drawn is one of degree."),
 ("encroachment by neighboring states",
  "EK LEG-2.B.5 lists conflicting interests and competition among groups and parties, perceived lack of governmental authority and legitimacy, pressure for autonomy or secession with intergroup conflict and terrorism, and encroachment of neighboring states that sense weakness. The last is the only external actor on the list."),
 ("contrasting methods to combat political corruption",
  "EK LEG-1.C.1.a names contrasting methods to combat political corruption among the six course countries, and EK PAU-1.C.3 identifies independent judiciaries as able to reduce corruption while protecting individual liberties and civil rights. The scenario is both statements at once."),
 ("civil society coalition works with officials",
  "EK LEG-1.C.1 says internal actors can bolster as well as undermine regime stability and rule of law, and EK LEG-1.C.3 describes civil society pressure producing new institutions that limit corruption. The rejected options are an undermining internal actor and three external actors of the kind EK LEG-2.B.5.d and EK PAU-2.A.2 treat separately."),
 ("intimidate local officials",
  "EK LEG-1.C.1.b names drug trafficking among the challenges to which states respond, and EK LEG-1.C.1 makes such actors capable of undermining regime stability and the rule of law. The rejected options are ordinary politics conducted through institutions, which EK PAU-1.B.1.a treats as the rule of law working."),
 ("divisive and violent actors",
  "EK LEG-1.C.2 states that state authorities of different regime types attempt to limit the influence of divisive and violent actors in their countries to attract more private capital and foreign direct investment and to improve economic growth. The investor signal in the scenario makes that motive explicit."),
 ("improve transparency and limit corruption",
  "EK LEG-1.C.3 names protecting civil liberties, improving transparency, addressing election fairness and media bias, limiting corruption and ensuring equality under law as the purposes of institutions created by reform pressure. Two of those five appear in the scenario."),
 ("fell by 216",
  "EK LEG-1.C.2 pairs limiting the influence of divisive and violent actors with attracting private capital and foreign direct investment. Recomputed in q20 above: one row shows both halves at once, the largest fall in incidents and the largest investment share."),
 ("rose from 120 to 260",
  "EK LEG-1.C.1 makes internal actors capable of undermining regime stability and rule of law and EK LEG-1.C.2 links limiting such actors to attracting capital. Recomputed in q21 above: one row moves against both halves, more than doubling its incidents while holding the lowest investment share."),
 ("70 percent",
  "Recomputed in q22 above: the fall divided by the earlier year's figure. The distractors are the REMAINING share, a halving, another row's proportional fall, and the absolute drop misread as a percentage."),
 ("far more often, in proportion",
  "EK LEG-1.C.1.c states that state responses to mass protest movements vary and EK LEG-1.C.3 that reform pressure can produce new institutions protecting civil liberties. Recomputed in q23 above: read as proportions rather than counts, the two accommodating responses stand more than three times clear of the other two."),
 ("5 percent",
  "Recomputed in q24 above by dividing the banned episodes followed by a new institution by the banned episodes. The distractors offer the raw count, the row total, a misplaced decimal and another row's share."),
 ("association across four categories",
  "EK MPA-1.A.3 states that numerous variables potentially influence political outcomes with no way to isolate and demonstrate which is producing the change, and EK MPA-1.A.4 calls a co-movement an association. Recomputed in q25 above: the association is real, and a state willing to ban a protest may also be disinclined to adopt protections for independent reasons."),
 ("different colonial histories",
  "EK LEG-2.B.4.c states that ethnicity has played a more significant role in Nigeria than in Mexico because of different colonial histories and a greater diversity and politicization of ethnic and religious identities in Nigeria. EK LEG-2.A.1.c does describe ethnic divisions in Mexico, so the claim is comparative rather than a denial."),
 ("statutory powers to audit ministries",
  "EK LEG-1.C.3 requires the creation of new political institutions or policies, so a body with statutory powers satisfies it while an election result, a treaty, an announced target and a speech leave the institutional landscape unchanged."),
 ("acting on society for an economic objective",
  "EK LEG-1.C.2 has state authorities limiting divisive and violent actors to attract capital and improve growth, while EK LEG-1.C.3 has citizen protest groups and civil society producing institutions protecting liberties, transparency, election fairness, anticorruption and equality. Both the direction of pressure and the objective differ."),
 ("framework's own example of recognition",
  "EK LEG-2.B.2.b describes state responses ranging from brute repression to recognition of ethnic and religious minorities and the creation of autonomous regions and/or representation of minorities in governmental institutions, so the scenario names the framework's accommodating endpoint."),
 ("either strengthen or threaten stability",
  "EK LEG-1.C.1 supplies the two-directional influence of internal actors, EK LEG-1.C.2 the cross-regime economic motive for limiting violent actors, and EK LEG-1.C.3 the institutional consequences of reform pressure. The summary keeps all three rather than reducing stability to repression or to outside forces."),
]

cg.check(k1_10, CLAIMS, table_checks={20: q20, 21: q21, 22: q22, 23: q23, 24: q24, 25: q25})
