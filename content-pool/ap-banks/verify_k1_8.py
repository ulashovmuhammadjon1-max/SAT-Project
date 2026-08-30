"""Key audit for AP COMPARATIVE GOVERNMENT 1.8 Political Legitimacy.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
  LEG-1.A.1  legitimacy is whether a government's constituents BELIEVE their
             government has the right to use power in the way they do; legitimacy
             confers authority on and can increase the power of a regime and
             government
  LEG-1.A.2  sources of legitimacy for BOTH democratic and authoritarian regimes
             can include popular elections and constitutional provisions; other
             sources are nationalism, tradition, governmental effectiveness,
             economic growth, ideology, religious heritage and organizations, and
             the dominant political party's endorsement

Country illustrations are held to PAU-1.D.1.b and PAU-3.G.1.b (Iran's theocracy
and its judiciary's religious function), PAU-4.A.2 (China's single governing
party maintaining centralism and order), PAU-3.C.2.f (the ceremonial monarch),
DEM-1.C.5 (Russia's contested but limited elections), PAU-1.D.1.c and DEM-2.B.4.b
(Mexico and Nigeria). The data items also lean on DEM-1.A.4 and MPA-1.A.3.

THE CONFLATION THIS MODULE IS BUILT TO PREVENT
----------------------------------------------
Legitimacy is a BELIEF held by a government's own constituents. It is not
sovereignty (PAU-1.A.4, a legal standing), not international recognition
(PAU-1.A.2, other states' acceptance), and not turnout (a behavior, which
DEM-1.A.4 says can be encouraged across regime types to give an illusion of
influence). A student who merges any of these can answer most of the topic
wrongly in a consistent way, so items 3, 4, 20, 22 and 29 key each separation on
its own rather than leaving it implicit.

A second framework position keyed rather than assumed: LEG-1.A.2 makes popular
elections a source of legitimacy for AUTHORITARIAN regimes too. Item 17 turns on
that, since the intuition that an uncompetitive election contributes nothing is
not the framework's.

DATA ITEMS
----------
Suggested skill 3.C for this topic is Data Analysis, so the module carries three
quantitative sets -- belief against turnout, sources named in two countries, and
growth against belief over four years -- rather than the usual one or two. All
figures are HYPOTHETICAL and labelled so in the stems. Item 27 is the causal
brake: the columns really do move together, and what fails is the inference.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k1_8

A2010 = "Share agreeing the government has the right to use power as it does, 2010"
A2020 = "Share agreeing the government has the right to use power as it does, 2020"
TURN = "Share reporting that they voted at the last national election"
CP = "Country P (hypothetical, percent)"
CQ = "Country Q (hypothetical, percent)"
GROWTH = "Annual economic growth (hypothetical, percent)"
AGREE = "Share agreeing the government has the right to use power as it does (percent)"


def q20(table, item):
    heads = [h.lower() for h in table["headers"]]
    assert any("agreeing" in h and "right to use power" in h for h in heads), \
        "the table must carry a belief column for the key to name"
    assert any("voted" in h for h in heads), "the table must also carry a turnout column, or the item has no distractor"
    assert A2010 != TURN and A2020 != TURN, "belief and turnout must be separate columns"
    return "the table carries two belief columns and one turnout column, so the item asks which kind of quantity the definition names"


def q21(table, item):
    d = {lab: cg.cell(table, lab, A2020) - cg.cell(table, lab, A2010) for lab in cg.labels(table)}
    assert d["Country L"] == -13, f"the keyed 13-point fall recomputes to {d['Country L']}"
    assert d["Country M"] == 6 and d["Country N"] == -4, f"the other two changes recompute to {d}"
    assert min(d.values()) == d["Country L"], "the keyed row must show the largest fall"
    assert any(v > 0 for v in d.values()), "'no country's figure fell' must be false, and one row must in fact rise"
    cross = cg.cell(table, "Country N", TURN) - cg.cell(table, "Country N", A2010)
    assert cross == 44, "the 44-point distractor must be a cross-column reading rather than a change over time"
    return "the three changes are -13, +6 and -4 points; the 44 offered against them is turnout minus an agreement figure"


def q22(table, item):
    turn = {lab: cg.cell(table, lab, TURN) for lab in cg.labels(table)}
    a10 = {lab: cg.cell(table, lab, A2010) for lab in cg.labels(table)}
    a20 = {lab: cg.cell(table, lab, A2020) for lab in cg.labels(table)}
    top = max(turn, key=turn.get)
    assert top == "Country N", f"the highest turnout belongs to {top}"
    assert min(a10, key=a10.get) == top and min(a20, key=a20.get) == top, \
        "the same row must hold the lowest agreement figure in BOTH years, as the stem says"
    return "one row holds the highest turnout at 83 and the lowest agreement in both years, 39 and 35"


def _cols(table):
    return ({str(r[0]): cg.cell(table, r[0], CP) for r in table["rows"]},
            {str(r[0]): cg.cell(table, r[0], CQ) for r in table["rows"]})


def q23(table, item):
    p, q = _cols(table)
    assert sum(p.values()) == 100 and sum(q.values()) == 100, \
        f"the columns sum to {sum(p.values())} and {sum(q.values())}, not 100"
    assert max(p, key=p.get) != max(q, key=q.get), \
        "the key requires the leading source to differ between the two countries"
    for col, name in ((p, "first"), (q, "second")):
        assert sum(1 for v in col.values() if v >= 10) >= 3, \
            f"the {name} column must spread across several sources for 'several' to be true"
    return "both columns sum to 100 and spread over at least three sources each, and the leading row differs between them"


def q24(table, item):
    p, q = _cols(table)
    gaps = {lab: abs(p[lab] - q[lab]) for lab in p}
    assert gaps["Free elections"] == 39, f"the keyed 39-point gap recomputes to {gaps['Free elections']}"
    assert max(gaps, key=gaps.get) == "Free elections", f"the largest gap belongs to {max(gaps, key=gaps.get)}"
    stated = {"Religious heritage": 26, "Economic growth": 19,
              "Constitutional provisions": 9, "The governing party's endorsement": 3}
    for lab, v in stated.items():
        assert gaps[lab] == v, f"the distractor for {lab} states {v} but the table gives {gaps[lab]}"
    return f"the five gaps recompute to {sorted(gaps.values(), reverse=True)}, and each distractor states a true gap for the wrong row"


def q25(table, item):
    p, q = _cols(table)
    assert q["Free elections"] < 10, "the student's premise requires elections to be rarely named in that column"
    top2 = sorted(q, key=q.get, reverse=True)[:2]
    assert sum(q[lab] for lab in top2) > 50, \
        "the objection requires two other sources to carry most of that column"
    assert set(top2) == {"Economic growth", "Religious heritage"}, f"the two leading rows are {top2}"
    return "elections are named by 7 percent in that column while two other named sources carry 64 percent between them"


def q26(table, item):
    g = cg.col(table, GROWTH)
    a = cg.col(table, AGREE)
    assert g == [6.1, 2.3, -1.4, 3.0], f"the growth column reads {g}"
    assert a == [72, 64, 51, 57], f"the agreement column reads {a}"
    steps = [(g[i + 1] - g[i], a[i + 1] - a[i]) for i in range(len(g) - 1)]
    for dg, da in steps:
        assert (dg > 0) == (da > 0), f"a step moves the two columns in opposite directions: {dg}, {da}"
    assert any(x < 0 for x in g), "'growth was positive in every year' must be false"
    assert max(a) != a[g.index(min(g))], "'agreement highest when growth lowest' must be false"
    return "the two columns move in the same direction at every one of the three steps, including the recovery"


def q27(table, item):
    g, a = cg.col(table, GROWTH), cg.col(table, AGREE)
    assert len(g) == 4, "the objection turns on there being only four paired observations"
    steps = [(g[i + 1] - g[i], a[i + 1] - a[i]) for i in range(3)]
    assert all((dg > 0) == (da > 0) for dg, da in steps), \
        "the columns must genuinely move together, or the objection would be to the reading rather than to the inference"
    return "the association is real across all four years, so what the key rejects is the causal step and not the reading"


CLAIMS = [
 ("constituents believe",
  "EK LEG-1.A.1 defines legitimacy as whether a government's constituents believe their government has the right to use power in the way they do. The rejected options are EK PAU-1.A.4's sovereignty, EK PAU-1.A.2's international recognition, a behavioral measure, and EK PAU-1.A.2's regime."),
 ("confers authority on them",
  "EK LEG-1.A.1 states that legitimacy confers authority on and can increase the power of a regime and government, which is why EK PAU-1.D.2 can say democratic regimes maintain sovereignty using less power. Belief does part of the work coercion would otherwise have to do."),
 ("belief held by a government's own constituents",
  "EK LEG-1.A.1 locates legitimacy in what constituents believe and EK PAU-1.A.4 locates sovereignty in independent legal authority free of outside interference. A state can hold the second while its government struggles for the first."),
 ("international recognition an element of statehood",
  "EK PAU-1.A.2 makes international recognition an element of statehood while EK LEG-1.A.1 makes legitimacy a matter of what a government's own constituents believe. Recognition by outsiders cannot supply a belief held by insiders, so the two come apart exactly as the scenario describes."),
 ("for both democratic and authoritarian regimes",
  "EK LEG-1.A.2 states that sources of legitimacy for both democratic and authoritarian regimes can include popular elections as well as constitutional provisions. Because the framework makes these available to both, holding an election is not itself evidence that a regime is democratic."),
 ("religious heritage and organizations",
  "EK LEG-1.A.2 lists nationalism, tradition, governmental effectiveness, economic growth, ideology, religious heritage and organizations, and the dominant political party's endorsement as the further sources. The rejected lists are elements of statehood, territorial structure, institutional design and electoral statistics."),
 ("nationalism",
  "EK LEG-1.A.2 names nationalism among the sources of legitimacy. An appeal to a shared national identity and history, rather than to a founding text, a custom, a growth rate or a party's approval, is that source and no other on the list."),
 ("tradition",
  "EK LEG-1.A.2 names tradition among the sources of legitimacy, and EK PAU-3.C.2.f describes the United Kingdom's monarch serving ceremonially as head of state, an office whose claim rests on continuity rather than on election, doctrine or performance."),
 ("governmental effectiveness",
  "EK LEG-1.A.2 names governmental effectiveness among the sources of legitimacy and EK LEG-1.B.1 repeats policy effectiveness among the things through which governments maintain it. What is credited in the scenario is performance rather than identity, faith, custom or a text."),
 ("economic growth",
  "EK LEG-1.A.2 names economic growth among the sources of legitimacy and EK LEG-1.B.3 adds that serious problems such as a poor economy can undermine it. A source that rises and falls with incomes is that one; the others do not move with the business cycle."),
 ("ideology",
  "EK LEG-1.A.2 names ideology among the sources of legitimacy, and EK PAU-4.A.2 describes rules reserving governing power to one party in order to maintain the values of centralism and order, which is a doctrine functioning in exactly this way."),
 ("religious heritage and organizations",
  "EK LEG-1.A.2 names religious heritage and organizations among the sources of legitimacy, and EK PAU-1.D.1.b gives a theocracy based on Islamic Sharia law as the framework's instance of religion supplying the basis of rule. The claim runs through the religious code rather than through custom or performance."),
 ("dominant political party's endorsement",
  "EK LEG-1.A.2 names the dominant political party's endorsement among the sources of legitimacy and EK PAU-4.A.2 describes a system in which only one party may control governing power. What confers the right to rule there is the party's choice rather than a vote, a text, an identity or a growth rate."),
 ("religious heritage and organizations",
  "EK PAU-1.D.1.b describes Iran's transition to a theocracy based on Islamic Sharia law and EK PAU-3.G.1.b adds that the judiciary's major function is to ensure the legal system rests on religious law. EK LEG-1.A.2 names religious heritage and organizations as the corresponding source of legitimacy."),
 ("ideology and the dominant political party's endorsement",
  "EK PAU-4.A.2 states that China's rules allow only the Communist Party of China to control governing power in order to maintain the values of centralism and order, pairing a doctrine with a party's exclusive endorsement. EK LEG-1.A.2 names both among the sources of legitimacy."),
 ("tradition operating as a source of legitimacy",
  "EK PAU-3.C.2.f has the monarch serving ceremonially as head of state while formally appointing the leader of the largest Commons party, so two claims to authority stand side by side. EK LEG-1.A.2 names tradition among the sources and allows a regime to draw on more than one at once."),
 ("available to authoritarian as well as democratic regimes",
  "EK LEG-1.A.2 states that popular elections can be a source of legitimacy for both democratic and authoritarian regimes, and EK DEM-1.C.5 describes Russia holding contested elections with limited competitiveness. What an election contributes to legitimacy is a separate question from what it shows about regime type."),
 ("popular elections and constitutional provisions",
  "EK LEG-1.A.2 names popular elections and constitutional provisions as sources available to both regime types, EK PAU-1.D.1.c records both transitions to multiparty republics, and EK DEM-2.B.4.b records the independent election commissions created during them. Those institutions are the two sources in operation."),
 ("which sources are relied on",
  "EK LEG-1.A.2 lists popular elections and religious heritage and organizations among the sources without ranking them, and EK LEG-1.A.1 makes legitimacy a matter of what constituents believe. Which source a government leans on is therefore a different question from whether it has legitimacy."),
 ("share agreeing the government has the right to use power as it does",
  "EK LEG-1.A.1 makes legitimacy a belief about the government's right to use power, which is not a behavior. Recomputed in q20 above: the table carries belief columns and a turnout column separately, and participation is treated by the framework under EK DEM-1.A and EK DEM-1.B instead."),
 ("by 13 percentage points",
  "Recomputed in q21 above: the three changes are a 13-point fall, a 6-point rise and a 4-point fall. The 44 offered against them is turnout minus an agreement figure, a comparison across columns that measure different things."),
 ("does not by itself establish",
  "EK LEG-1.A.1 makes legitimacy a belief about the right to use power, while EK DEM-1.A.4 notes that formal participation can be encouraged across regime types, including to give an illusion of influence. Recomputed in q22 above: one row pairs the highest turnout with the lowest agreement in both years."),
 ("the leading source differs between them",
  "EK LEG-1.A.2's list supplies every row of the table, and the framework allows a regime to draw on several sources at once. Recomputed in q23 above: both columns sum to 100 and spread across at least three sources, with different rows leading."),
 ("39 percentage points",
  "Recomputed in q24 above from the absolute difference in each row. Every alternative states the correct gap for a different row, so the item turns on comparing the five differences rather than computing one."),
 ("several sources besides elections",
  "EK LEG-1.A.2 names nationalism, tradition, governmental effectiveness, economic growth, ideology, religious heritage and organizations, and a dominant party's endorsement alongside elections and constitutional provisions. Recomputed in q25 above: two of those rows carry 64 percent of that column between them."),
 ("rose in the year growth recovered",
  "EK LEG-1.A.2 names economic growth among the sources of legitimacy and EK LEG-1.B.3 says a poor economy can undermine it. Recomputed in q26 above: the two columns move in the same direction at every step, including the recovery."),
 ("isolated and demonstrated with certainty",
  "EK MPA-1.A.3 states that numerous variables potentially influence political outcomes with no way to isolate and demonstrate which is producing the change, and EK MPA-1.A.4 calls a co-movement an association. Recomputed in q27 above: the columns do move together, so the failure is in the causal step."),
 ("no right to make the decisions",
  "EK LEG-1.A.1 makes legitimacy a matter of whether constituents believe the government has the right to use power in the way it does, so evidence about it must be evidence about that belief. Seat losses, foreign criticism, reorganization and a leadership change are each compatible with that belief holding."),
 ("constituted by the belief rather than by the performance",
  "EK LEG-1.A.1 defines legitimacy as the belief of a government's constituents while EK LEG-1.A.2 lists governmental effectiveness as one possible SOURCE of that belief. A source can be present without producing the belief, which is how equal performance and unequal legitimacy coexist."),
 ("available to democratic and authoritarian regimes alike",
  "EK LEG-1.A.1 supplies the definition and the consequence that legitimacy confers authority and can increase a regime's power, and EK LEG-1.A.2 supplies the plural sources and their availability to both regime types. The summary keeps all three parts."),
]

cg.check(k1_8, CLAIMS,
         table_checks={20: q20, 21: q21, 22: q22, 23: q23, 24: q24, 25: q25, 26: q26, 27: q27})
