"""Key audit for AP COMPARATIVE GOVERNMENT 1.9 Sustaining Legitimacy.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
  LEG-1.B.1  legitimacy is maintained through policy effectiveness, political
             efficacy, tradition, charismatic leadership, institutionalized laws
  LEG-1.B.2  peaceful resolution of conflicts, peaceful transfer of power, reduced
             governmental corruption and economic development REINFORCE it
  LEG-1.B.3  an increase in corruption, reduced electoral competition, and serious
             problems such as a poor economy or social conflicts UNDERMINE it
  LEG-1.B.4  devolution can ENHANCE OR WEAKEN legitimacy, with .a benefits and .b
             costs listed in the same statement
  LEG-1.B.5  questions about the integrity of election results ACROSS THE COURSE
             COUNTRIES can lead to protests that MAY weaken legitimacy AND any
             ongoing democratization processes

WHERE THE DEFINITION OF POLITICAL EFFICACY COMES FROM
-----------------------------------------------------
LEG-1.B.1 names political efficacy and the course framework never defines it. It
would therefore have been out of bounds to key a definition -- except that the
CED's own SCORING GUIDELINES for its sample free-response question 2 define it:
acceptable descriptions are "citizens have faith and trust in government and
believe that they can influence politics" and "citizens believe that one's vote
can influence political affairs." Items 2 and 3 key that wording and nothing
beyond it. The same scoring guidelines supply item 28, which accepts that
authoritarian regimes often allow citizens to participate to develop and maintain
a sense of political legitimacy -- consistent with EK DEM-1.A.4.

TWO HEDGES KEYED RATHER THAN SMOOTHED OVER
------------------------------------------
LEG-1.B.4 is two-sided in a single sentence, so items 15 to 19 never let
devolution come out as simply good or simply bad; items 16 and 17 make a student
sort the two halves of the framework's own lists. LEG-1.B.5 says protests MAY
weaken legitimacy, and item 27 is built on that word.

DATA ITEMS
----------
Items 22-24 share a corruption-and-trust table and 25-27 an election-integrity
table, both HYPOTHETICAL and labelled so. Item 24 is the brake: LEG-1.B.2 and
LEG-1.B.3 are claims about CHANGE, so a country whose score is flat supports
neither, however its level ranks.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k1_9

C2010 = "Corruption score, 2010 (0 = highly corrupt, 100 = very clean)"
C2020 = "Corruption score, 2020 (0 = highly corrupt, 100 = very clean)"
TRUST = "Share saying they trust the national government, 2020"
ACC = "Share of citizens saying the count was accurate"
PROT = "Protest events recorded in the following month"
DELTA = "Change in the share saying the government has the right to rule, in percentage points"


def _corr(table):
    return ({lab: cg.cell(table, lab, C2020) - cg.cell(table, lab, C2010) for lab in cg.labels(table)},
            {lab: cg.cell(table, lab, TRUST) for lab in cg.labels(table)})


def q22(table, item):
    d, trust = _corr(table)
    assert d["Country R"] == 21, f"the keyed 21-point rise recomputes to {d['Country R']}"
    assert max(d, key=d.get) == "Country R", "the keyed row must show the largest move toward the clean end"
    assert max(trust, key=trust.get) == "Country R", f"the highest trust figure belongs to {max(trust, key=trust.get)}"
    assert "very clean" in C2020, "the key depends on the header stating that a higher score is cleaner"
    return "one row rises 21 points toward the clean end of the scale and also holds the highest trust figure"


def q23(table, item):
    d, trust = _corr(table)
    assert d["Country S"] == -14, f"the keyed 14-point fall recomputes to {d['Country S']}"
    assert min(d, key=d.get) == "Country S", "the keyed row must show the largest move toward the corrupt end"
    assert min(trust, key=trust.get) == "Country S", f"the lowest trust figure belongs to {min(trust, key=trust.get)}"
    assert all(v < 70 for v in trust.values()), \
        "'every trust figure is below 70' is true, which is why that distractor is tempting and still irrelevant"
    return "one row falls 14 points toward the corrupt end of the scale and also holds the lowest trust figure"


def q24(table, item):
    d, trust = _corr(table)
    assert abs(d["Country T"]) == 1, f"the flat row's change recomputes to {d['Country T']}"
    assert abs(d["Country T"]) == min(abs(v) for v in d.values()), "the flat row must be the one that barely moved"
    assert cg.cell(table, "Country T", C2020) > cg.cell(table, "Country S", C2020), \
        "the first rejected option states a true LEVEL comparison, which is what makes it tempting"
    assert trust["Country T"] != max(trust.values()), \
        "the second rejected option also states a true level fact, that its trust figure is not the highest"
    return "the flat row moves 1 point over the decade while both rejected options state true LEVEL facts, so level and change come apart"


def _prot(table):
    labs = cg.labels(table)
    return (labs,
            {l: cg.cell(table, l, ACC) for l in labs},
            {l: cg.cell(table, l, PROT) for l in labs},
            {l: cg.cell(table, l, DELTA) for l in labs})


def q25(table, item):
    labs, acc, prot, dl = _prot(table)
    order = sorted(labs, key=lambda l: acc[l], reverse=True)
    prots = [prot[l] for l in order]
    deltas = [dl[l] for l in order]
    assert prots == sorted(prots), f"protest counts must rise as acceptance falls; got {prots}"
    assert deltas == sorted(deltas, reverse=True), f"the right-to-rule change must worsen as acceptance falls; got {deltas}"
    assert prot[order[0]] < prot[order[-1]], "'protest heaviest where the count was most accepted' must be false"
    assert any(v > 0 for v in dl.values()), "'a fall after every election' must be false"
    assert any(v < 0 for v in dl.values()), "'a rise after every election' must be false"
    return f"ordering the rows by acceptance gives protest counts {prots} and right-to-rule changes {deltas}"


def q26(table, item):
    vals = cg.col(table, PROT)
    total = sum(vals)
    assert total == 162, f"the keyed total recomputes to {total}"
    for wrong in (158, 116, 50, 112):
        assert wrong != total, f"distractor {wrong} equals the correct total"
    assert 158 == total - min(vals) and 50 == total - max(vals) and 112 == max(vals), \
        "each distractor should be a recognizable partial reading of the same column"
    return f"the protest column reads {vals} and sums to {total:.0f}, with each distractor a partial sum or a single row"


def q27(table, item):
    labs, acc, prot, dl = _prot(table)
    assert max(acc, key=acc.get) == "Election 1", "the keyed row must be the most widely accepted count"
    assert min(prot, key=prot.get) == "Election 1", "the keyed row must have the fewest protest events"
    risers = [l for l, v in dl.items() if v > 0]
    assert risers == ["Election 1"], f"exactly one row may show a rise; got {risers}"
    return "the keyed row is highest on acceptance, lowest on protest, and the only one whose right-to-rule share rises"


CLAIMS = [
 ("policy effectiveness, political efficacy",
  "EK LEG-1.B.1 lists policy effectiveness, political efficacy, tradition, charismatic leadership and institutionalized laws as the processes or factors through which governments maintain legitimacy. The rejected sets are the elements of statehood, territorial structure, electoral arithmetic and the data resources of EK MPA-1.A.8."),
 ("faith and trust in government",
  "The CED's scoring guidelines for its sample free-response question on political efficacy accept 'citizens have faith and trust in government and believe that they can influence politics' and 'citizens believe that one's vote can influence political affairs'. EK LEG-1.B.1 names the term without defining it, so this is the framework's own gloss and the only defensible one."),
 ("political efficacy",
  "EK LEG-1.B.1 names political efficacy among the factors maintaining legitimacy and the CED's scoring guidance glosses it as citizens believing one's vote can influence political affairs. The rejected factors concern a leader's personal appeal, a body of law, continuity, and the manner of a succession."),
 ("charismatic leadership",
  "EK LEG-1.B.1 names charismatic leadership among the factors maintaining legitimacy. Authority attached to a person rather than to an office or a rule is that factor, and institutionalized laws are the framework's contrasting item on the same list."),
 ("institutionalized laws",
  "EK LEG-1.B.1 names institutionalized laws among the factors maintaining legitimacy, and EK PAU-1.A.2 makes rules that endure from government to government the regime rather than the officeholder. Authority attaching to the office is the contrast with charismatic leadership."),
 ("how well the government's policies work",
  "EK LEG-1.B.1 lists policy effectiveness and political efficacy separately, and the CED's scoring guidance glosses efficacy as citizens' faith, trust and belief that they can influence politics. One is a property of what government does and the other of what citizens believe, so a government can be effective without producing efficacy."),
 ("peaceful resolution of conflicts",
  "EK LEG-1.B.2 names peaceful resolution of conflicts, peaceful transfer of power, reduced governmental corruption and economic development as reinforcing legitimacy. The first rejected option is EK LEG-1.B.3's list of what undermines it."),
 ("peaceful transfer of power is named",
  "EK LEG-1.B.2 names peaceful transfer of power among the things that reinforce legitimacy, and EK PAU-1.D.4 describes elections as the relatively peaceful route by which governments change. A transfer accepted by those who lose under the rules is evidence the rules are accepted."),
 ("reduced governmental corruption is named",
  "EK LEG-1.B.2 names reduced governmental corruption among the things that reinforce legitimacy and EK PAU-1.C.3 states that independent judiciaries can reduce corruption while protecting individual liberties and civil rights. The two statements point the same way."),
 ("economic development is named",
  "EK LEG-1.B.2 names economic development among the things that reinforce legitimacy and EK LEG-1.A.2 names economic growth among the sources of legitimacy. Neither makes development sufficient for democratization, which EK PAU-1.C.1 defines separately."),
 ("serious problems such as a poor economy",
  "EK LEG-1.B.3 names an increase in corruption, reduced electoral competition and serious problems such as a poor economy or social conflicts as undermining legitimacy. The first rejected option is EK LEG-1.B.2's reinforcing list, and the rest are aims or instruments of democratization under EK PAU-1.C."),
 ("reduced electoral competition is named",
  "EK LEG-1.B.3 names reduced electoral competition among the things that undermine legitimacy, EK PAU-4.A.3 lists registration and threshold rules among the devices entrenching one party, and EK DEM-2.B.4.a describes candidate exclusion reducing competition and representation. That elections continue does not answer the objection."),
 ("inhibits democratization",
  "EK LEG-1.B.3 names an increase in corruption among the things that undermine legitimacy and EK PAU-1.C.3 states that political corruption inhibits democratization. The framework treats rising corruption as damaging on both fronts at once."),
 ("a poor economy and social conflicts",
  "EK LEG-1.B.3 gives a poor economy and social conflicts as its own examples of the serious problems that can undermine legitimacy. Population, territory, treaty membership, party competition and separated powers appear elsewhere and not under this heading."),
 ("enhance or weaken legitimacy",
  "EK LEG-1.B.4 states that devolution and delegation of power to regional governments can enhance or weaken legitimacy, creating both opportunities and obstacles, and then lists benefits and costs in the same statement. A one-sided reading contradicts the sentence in either direction."),
 ("policy innovation",
  "EK LEG-1.B.4.a lists promoting policy innovation, matching policies to local needs, improving policies through competition, increasing political participation, checking central power and better representation of religious, ethnic and minority groups. Each rejected option comes from EK LEG-1.B.4.b, the costs half of the same statement."),
 ("exacerbating ethnic and local tensions",
  "EK LEG-1.B.4.b lists creating contradictory policies, complicating and slowing implementation, allowing inequality between regions, increasing competition for resources and exacerbating ethnic and local tensions. Each rejected option comes from EK LEG-1.B.4.a, the benefits half of the same statement."),
 ("improvement by competition",
  "EK LEG-1.B.4.a names promoting policy innovation, improving policies through competition and increasing political participation among devolution's benefits, and all three appear in the scenario. EK PAU-2.A.2 allows the degree of centralization to change without altering the constitutional classification."),
 ("exacerbated ethnic and local tensions",
  "EK LEG-1.B.4.b names allowing inequality between regions, increasing competition for resources and exacerbating ethnic and local tensions among devolution's costs, and all three appear in the scenario. EK LEG-1.B.4's opening clause is why one bad case is not a general verdict."),
 ("may weaken legitimacy and any ongoing democratization",
  "EK LEG-1.B.5 states that questions about the integrity of election results across the course countries can lead to protests that may weaken legitimacy and any ongoing democratization processes. The statement names two casualties rather than one, and hedges with 'may'."),
 ("rather than to authoritarian regimes alone",
  "EK LEG-1.B.5 refers to questions about the integrity of election results ACROSS THE COURSE COUNTRIES, the framework's phrase for the whole set of six. This follows the pattern of EK DEM-1.C.2 and EK DEM-1.B.3, which assign a phenomenon to both regime types and differ only in degree."),
 ("rose 21 points toward the clean end",
  "EK LEG-1.B.2 names reduced governmental corruption among the things that reinforce legitimacy, and the column header states that a higher score is cleaner, so a rise is a reduction in corruption. Recomputed in q22 above: one row pairs the largest such rise with the highest trust figure."),
 ("fell 14 points",
  "EK LEG-1.B.3 names an increase in corruption among the things that undermine legitimacy, and on this scale a falling score is rising corruption. Recomputed in q23 above: one row pairs the largest such fall with the lowest trust figure."),
 ("supports neither the claim",
  "EK LEG-1.B.2 and EK LEG-1.B.3 are both claims about CHANGE in corruption, so a country whose score is effectively flat gives neither claim anything to attach to. Recomputed in q24 above, including that the row's level sits above the scale's midpoint, which is the reading the rejected options mistake for a change."),
 ("the more protest followed",
  "EK LEG-1.B.5 states that questions about the integrity of election results can lead to protests that may weaken legitimacy. Recomputed in q25 above: ordering the rows by acceptance makes protest counts rise and the right-to-rule change worsen at every step."),
 ("162",
  "Recomputed in q26 above by summing the protest column. Each distractor is a recognizable partial reading of the same column -- the total less its smallest row, the total less its largest, the first two rows, and the largest row alone."),
 ("rose rather than fell",
  "EK LEG-1.B.5 says such protests MAY weaken legitimacy and any ongoing democratization processes, so the hedge leaves room for an accepted count followed by little protest and no loss. Recomputed in q27 above: one row is highest on acceptance, lowest on protest, and the only one that rises."),
 ("develop and maintain a sense of political legitimacy",
  "The CED's scoring guidelines for its sample turnout question accept that authoritarian regimes often allow citizens to participate to develop and maintain a sense of political legitimacy, and EK DEM-1.A.4 states that formal participation can be encouraged across regime types to enhance legitimacy."),
 ("measured corruption has fallen",
  "EK LEG-1.B.2 names peaceful transfer of power and reduced governmental corruption among the things that reinforce legitimacy, and EK LEG-1.A.1 makes the belief of constituents the thing reinforced. The keyed finding reports two named causes and the belief itself; the rejected findings report none of them."),
 ("affected in either direction by devolution",
  "EK LEG-1.B.1 supplies the processes, EK LEG-1.B.2 the reinforcing developments, EK LEG-1.B.3 the undermining ones, EK LEG-1.B.4 devolution's two-sided effect and EK LEG-1.B.5 the effect of disputed election results. The summary keeps all five rather than reducing them to one mechanism."),
]

cg.check(k1_9, CLAIMS, table_checks={22: q22, 23: q23, 24: q24, 25: q25, 26: q26, 27: q27})
