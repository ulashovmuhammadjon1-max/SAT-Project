"""Key audit for AP COMPARATIVE GOVERNMENT 5.4 Policies and Economic
Liberalization.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
Learning objectives IEF-3.D and IEF-3.E, six essential knowledge statements:

  IEF-3.D.1  economic liberalization = the STATE REDUCING ITS ECONOMIC ROLE and
             embracing free market mechanisms: ELIMINATING SUBSIDIES AND TARIFFS,
             PRIVATIZING GOVERNMENT-OWNED INDUSTRIES, OPENING THE ECONOMY TO FDI
  IEF-3.E.1  five comparison measures: ECONOMIC DEVELOPMENT, ECONOMIC GROWTH,
             HUMAN DEVELOPMENT, WEALTH, INEQUALITY
  IEF-3.E.2  countries OF ALL REGIME TYPES adopt it, for DOMESTIC circumstances
             (rising unemployment, reduced productivity) and EXTERNAL situations
             (trade deficits, decreasing demand for petroleum, natural gas and
             rare-earth metal)
  IEF-3.E.3  neoliberal policies = REMOVAL OF BARRIERS ON INTERNAL AND EXTERNAL
             ACTORS; MIXED EFFECTS -- lower inflation and higher national income
             WITH growing inequality, persistent corruption and worsened social
             tensions, as governments balance ECONOMIC FREEDOM against POLICIES
             PROMOTING ECONOMIC AND POLITICAL EQUALITY
  IEF-3.E.4  prosperity tied to liberalization HAS AFFECTED THE POWER OF RULING
             POLITICAL PARTIES
  IEF-3.E.5  it has contributed to POLLUTION, URBAN SPRAWL and UNEVEN DEVELOPMENT
             through .a fossil-fuel engines, .b poor infrastructure and lack of
             regulation, .c regional migration (east/west in China, north/south
             in Mexico, rural/urban in both)

"MIXED EFFECTS" IS THE LOAD-BEARING PHRASE OF THE TOPIC. IEF-3.E.3 puts falling
inflation and rising national income in the SAME SENTENCE as growing inequality,
persistent political corruption and worsened social tensions. A student who has
filed liberalization as a success story or as a failure story cannot answer an
item that lists both, which is why items 9, 10, 17 and 24 all require holding the
two halves at once. Item 24's check demands that TWO indicators improve and TWO
worsen in the table; a table moving one way would make the key false while the
item still looked answerable.

IEF-3.E.2's SECOND LOAD-BEARING PHRASE IS "OF ALL REGIME TYPES". The framework
does not present liberalization as something democracies do. Items 4 and 20 key
that, and item 20's scenario deliberately pairs an authoritarian regime with a
democracy doing the same thing.

WHAT IS DELIBERATELY NOT ASSERTED: no growth rate, income level, inflation rate,
unemployment rate or inequality measure is attributed to any real country
anywhere in this module -- this is the unit SOCIAL_BRIEF.md warns is most exposed
to going stale. The only country-specific claim is IEF-3.E.5.c's own, keyed at
item 16: east/west migration in China, north/south in Mexico, rural/urban in
both. That is a structural pattern, not a figure. Every table is HYPOTHETICAL and
labelled so, and every country in one is unnamed.

DATA ITEMS
----------
Items 21-23 read the comparison table, 24-26 the before-and-after table, 27-29
the migration table. Items 21 and 22 each assert a COMBINATION of two measures,
so each check confirms the keyed row holds the relevant extreme in BOTH columns
and that no other row does. Every arithmetic distractor is verified to be a wrong
operation on the same table.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k5_4

INCOME = "National income per person (index)"
GROWTH = "Annual economic growth (percent)"
HDI = "Human development index"
TOP10 = "Share of income held by the richest tenth (percent)"

BEFORE = "Before the reforms"
AFTER = "Ten years after the reforms"

NET = "Net movement of people over a decade, in thousands (hypothetical)"


def _meas(table):
    return {lab: (cg.cell(table, lab, INCOME), cg.cell(table, lab, GROWTH),
                  cg.cell(table, lab, HDI), cg.cell(table, lab, TOP10))
            for lab in cg.labels(table)}


def q21(table, item):
    v = _meas(table)
    assert max(v, key=lambda k: v[k][2]) == "Country A", "the keyed row must hold the highest human development"
    assert min(v, key=lambda k: v[k][1]) == "Country A", "the keyed row must also hold the slowest growth"
    assert v["Country A"][2] == 0.92 and v["Country A"][1] == 1.4, f"the keyed row reads {v['Country A']}"
    assert v["Country B"][2] == 0.74 and v["Country B"][1] == 6.8, "the first rejected option must state its own row truly"
    assert v["Country C"][2] == 0.55 and v["Country C"][1] == 3.1, "the second rejected option must state its own row truly"
    assert len({v[k][2] for k in v}) == 3 and len({v[k][1] for k in v}) == 3, "'all three equally' must be false"
    return (f"human development reads {[v[k][2] for k in v]} against growth {[v[k][1] for k in v]}, "
            "so one row alone is highest on the first and lowest on the second")


def q22(table, item):
    v = _meas(table)
    assert max(v, key=lambda k: v[k][1]) == "Country B", "the keyed row must hold the fastest growth"
    assert max(v, key=lambda k: v[k][3]) == "Country B", "the keyed row must also hold the largest top-tenth share"
    assert v["Country B"][1] == 6.8 and v["Country B"][3] == 41, f"the keyed row reads {v['Country B']}"
    assert v["Country A"][1] == 1.4 and v["Country C"][3] == 33, "each rejected option must state its own row truly"
    assert min(v[k][3] for k in v) > 0, "'no inequality anywhere' must be false"
    return (f"growth reads {[v[k][1] for k in v]} against top-tenth shares {[v[k][3] for k in v]}, "
            "so one row alone is highest on both")


def q23(table, item):
    t = cg.col(table, TOP10)
    diff = max(t) - min(t)
    assert diff == 17, f"the keyed difference recomputes to {diff}"
    pairs = {abs(a - b) for a in t for b in t if a != b}
    assert 8 in pairs and 9 in pairs, f"the 8 and 9 distractors must be the other gaps in that column; gaps are {sorted(pairs)}"
    assert max(t) == 41 and min(t) == 24, f"the 41 and 24 distractors must be the column's extremes; it reads {t}"
    return f"the top-tenth column reads {t}, so the largest minus the smallest is {diff:.0f} percentage points"


def _mix(table):
    return {lab: (cg.cell(table, lab, BEFORE), cg.cell(table, lab, AFTER)) for lab in cg.labels(table)}


def q24(table, item):
    v = _mix(table)
    infl = "Annual inflation (percent)"
    inc = "National income index"
    top = "Share of income held by the richest tenth (percent)"
    corr = "Recorded cases of official corruption"
    assert v[infl][1] < v[infl][0], f"inflation must fall; it reads {v[infl]}"
    assert v[inc][1] > v[inc][0], f"national income must rise; it reads {v[inc]}"
    assert v[top][1] > v[top][0], f"income concentration must rise; it reads {v[top]}"
    assert v[corr][1] > v[corr][0], f"recorded corruption must rise; it reads {v[corr]}"
    improved = [lab for lab in v if lab == infl and v[lab][1] < v[lab][0]] + [lab for lab in v if lab == inc and v[lab][1] > v[lab][0]]
    worsened = [lab for lab in (top, corr) if v[lab][1] > v[lab][0]]
    assert len(improved) == 2 and len(worsened) == 2, \
        "exactly two indicators must move favorably and two unfavorably, or 'mixed' would not be the reading"
    for lab in v:
        assert v[lab][0] != v[lab][1], f"{lab} must change, so 'none of the indicators changed' is false"
    return (f"inflation goes {v[infl]}, national income {v[inc]}, the top tenth's share {v[top]} and recorded "
            "corruption " + str(v[corr]) + ", two moving each way")


def q25(table, item):
    v = _mix(table)
    infl = v["Annual inflation (percent)"]
    fall = infl[0] - infl[1]
    assert fall == 22, f"the keyed fall recomputes to {fall}"
    assert infl[1] == 6 and infl[0] == 28, f"the 6 and 28 distractors must be the row's own two figures; it reads {infl}"
    top = v["Share of income held by the richest tenth (percent)"]
    assert top[1] - top[0] == 13, "the 13 distractor must be the change in the top-tenth row"
    inc = v["National income index"]
    assert inc[1] - inc[0] == 49, "the 49 distractor must be the change in the national income row"
    return f"the inflation row goes from {infl[0]:.0f} to {infl[1]:.0f} percent, a fall of {fall:.0f} percentage points"


def q26(table, item):
    v = _mix(table)
    top = v["Share of income held by the richest tenth (percent)"]
    rise = top[1] - top[0]
    assert rise == 13, f"the keyed rise recomputes to {rise}"
    infl = v["Annual inflation (percent)"]
    assert infl[0] - infl[1] == 22, "the 22 distractor must be the change in the inflation row"
    assert top[1] == 44 and top[0] == 31, f"the 44 and 31 distractors must be the row's own two figures; it reads {top}"
    corr = v["Recorded cases of official corruption"]
    assert corr[1] - corr[0] == 55, "the 55 distractor must be the change in the corruption row"
    return f"the top-tenth row goes from {top[0]:.0f} to {top[1]:.0f} percent, a rise of {rise:.0f} percentage points"


def q27(table, item):
    v = {lab: cg.cell(table, lab, NET) for lab in cg.labels(table)}
    top = max(v, key=v.get)
    assert top == "Rural areas to urban areas", f"the largest flow is {top}"
    assert v[top] == 9600, f"the keyed flow reads {v[top]}"
    assert v["Urban areas to rural areas"] == min(v.values()), \
        "the reverse flow must be the smallest, or the rejected option naming it as dominant would be arguable"
    assert len(set(v.values())) == 4, "no two flows may tie, or more than one option could be defended"
    return f"the four flows are {[v[l] for l in v]} thousand, and the rural-to-urban flow is the largest"


def q28(table, item):
    c = cg.col(table, NET)
    total = sum(c)
    assert total == 16300, f"the keyed total recomputes to {total}"
    assert total - min(c) == 15600, "the 15600 distractor must be the total with the smallest row omitted"
    assert sum(sorted(c)[-2:]) == 13800, "the 13800 distractor must be the two largest rows added"
    assert max(c) == 9600, "the 9600 distractor must be the largest single row"
    assert total - max(c) == 6700, "the 6700 distractor must be the total with the largest row omitted"
    return f"the movement column reads {c} and sums to {total:.0f} thousand"


def q29(table, item):
    v = {lab: cg.cell(table, lab, NET) for lab in cg.labels(table)}
    into, out = v["Rural areas to urban areas"], v["Urban areas to rural areas"]
    net = into - out
    assert net == 8900, f"the keyed net gain recomputes to {net}"
    assert into + out == 10300, "the 10300 distractor must be the two flows added instead of subtracted"
    assert into == 9600 and out == 700, f"the 9600 and 700 distractors must be the two flows themselves; they read {into}, {out}"
    assert v["Interior regions to coastal regions"] - v["Southern regions to northern regions"] == 2400, \
        "the 2400 distractor must be the gap between the two rows that do not concern the urban areas"
    return f"movement into the urban areas is {into:.0f} thousand against {out:.0f} thousand out, a net gain of {net:.0f} thousand"


CLAIMS = [
 ("reducing its economic role and embracing free market mechanisms",
  "EK IEF-3.D.1 states that economic liberalization occurs when a state reduces its economic role and embraces free market mechanisms, so the definition is about the state stepping back rather than about any political change."),
 ("eliminating subsidies and tariffs, privatizing government-owned industries",
  "EK IEF-3.D.1 names eliminating subsidies and tariffs, privatizing government-owned industries, and opening the economy to foreign direct investment as the free market mechanisms a liberalizing state embraces."),
 ("levels of economic development, economic growth, human development, wealth, and inequality",
  "EK IEF-3.E.1 states that political-economic systems in the course countries can be compared by measuring levels of economic development, economic growth, human development, wealth, and inequality."),
 ("course countries of all regime types",
  "EK IEF-3.E.2 states that course countries of all regime types adopt economic liberalization policies, so the framework treats liberalization as a response available to any regime rather than as the mark of one kind."),
 ("rising unemployment and reduced productivity",
  "EK IEF-3.E.2 names rising unemployment and reduced productivity as the undesirable domestic circumstances that economic liberalization policies aim to remedy."),
 ("trade deficits with other states and decreasing demand for raw materials",
  "EK IEF-3.E.2 names trade deficits with other states and decreasing demand for raw materials as the undesirable external situations, distinguishing them from the domestic circumstances in the same statement."),
 ("petroleum, natural gas, and rare-earth metal",
  "EK IEF-3.E.2 names petroleum, natural gas, and rare-earth metal as the raw materials whose decreasing demand counts as an undesirable external situation."),
 ("removal of barriers and restrictions on what internal and external economic actors can do",
  "EK IEF-3.E.3 defines neoliberal economic policies as the removal of barriers and restrictions on what internal and external economic actors can do, which covers domestic and foreign actors alike."),
 ("reduction in inflation and increases in national income",
  "EK IEF-3.E.3 names reduction in inflation and increases in national income among the effects of neoliberal economic policies and lists them in the same sentence as the unfavorable effects, which is what makes the record mixed."),
 ("growing inequality in wealth distribution, persistent political corruption",
  "EK IEF-3.E.3 names growing inequality in wealth distribution, persistent political corruption, and the exacerbation of existing social tensions among the effects of neoliberal economic policies."),
 ("balancing economic freedom with policies that promote economic and political equality",
  "EK IEF-3.E.3 states that existing social tensions are exacerbated as governments attempt to balance economic freedom with policies that promote economic and political equality, which is the trade-off the statement itself identifies."),
 ("the power of ruling political parties",
  "EK IEF-3.E.4 states that economic prosperity tied to liberalization policies has affected the power of ruling political parties among course country political systems, tying an economic outcome to a party's hold on office."),
 ("environmental pollution, urban sprawl, and uneven economic development",
  "EK IEF-3.E.5 states that while often stimulating growth, economic liberalization has contributed to environmental pollution, urban sprawl, and uneven economic development in course countries."),
 ("automobiles and other engines using fossil fuels",
  "EK IEF-3.E.5.a names increased consumption and use of automobiles and other engines using fossil fuels, the one of its three causes stated in terms of what people use rather than of policy or of movement."),
 ("poor infrastructure and lack of government regulation",
  "EK IEF-3.E.5.b names poor infrastructure and lack of government regulation, the one of the three causes stated as a shortfall on the government's own side rather than as private behavior."),
 ("east and west in China, north and south in Mexico",
  "EK IEF-3.E.5.c names regional migration patterns including east and west in China, north and south in Mexico, and rural to urban movement in both, so two country-specific axes are joined by one pattern common to the two."),
 ("in the same statement",
  "EK IEF-3.E.3 lists reduction in inflation and increases in national income together with growing inequality in wealth distribution, persistent political corruption and the exacerbation of social tensions, so the mixture is in the framework's own record rather than in disagreement about it."),
 ("the state is reducing its economic role",
  "EK IEF-3.D.1 names eliminating subsidies, privatizing government-owned industries, and opening the economy to foreign direct investment as the mechanisms of economic liberalization, and the scenario contains one instance of each."),
 ("an undesirable external situation, namely a trade deficit",
  "EK IEF-3.E.2 names trade deficits with other states among the undesirable external situations that liberalization policies aim to remedy, and separates those from the domestic circumstances of unemployment and reduced productivity."),
 ("course countries of all regime types adopt economic liberalization policies",
  "EK IEF-3.E.2 states that course countries of all regime types adopt economic liberalization policies to remedy undesirable domestic circumstances and undesirable external situations, so regime type is not what decides whether they are adopted."),
 ("human development index of 0.92 and annual growth of 1.4 percent",
  "EK IEF-3.E.1 names economic growth and human development as separate measures for comparing political-economic systems, so a country can rank high on one and low on the other. Recomputed in q21 above, where one row alone holds the highest of the first and the lowest of the second."),
 ("the richest tenth holding 41 percent of income",
  "EK IEF-3.E.1 names growth and inequality among the comparison measures and EK IEF-3.E.3 records growing inequality in wealth distribution alongside increases in national income, so the two can rise together. Recomputed in q22 above, where one row alone is highest on both."),
 ("17 percentage points",
  "Recomputed in q23 above by subtracting the smallest top-tenth share from the largest. The distractors are the other two gaps in that column and its two extreme values read as though they were differences."),
 ("while income concentration at the top and recorded corruption both increased",
  "EK IEF-3.E.3 states that neoliberal economic policies have had mixed effects, joining reduction in inflation and increases in national income to growing inequality and persistent political corruption. Recomputed in q24 above, which requires exactly two indicators to move each way."),
 ("22 percentage points",
  "Recomputed in q25 above by subtracting the later inflation figure from the earlier one. The distractors are the two inflation figures themselves and the changes recorded in two other rows of the same table."),
 ("13 percentage points",
  "Recomputed in q26 above by subtracting the earlier top-tenth share from the later one. The distractors are the change in the inflation row, the two shares themselves, and the change in the corruption row."),
 ("movement from rural areas to urban areas",
  "EK IEF-3.E.5.c names regional migration patterns including rural to urban movement among the causes of environmental pollution, urban sprawl, and uneven economic development. Recomputed in q27 above, where that flow is the largest and no two flows tie."),
 ("16300 thousand",
  "Recomputed in q28 above by summing the movement column across the four directions. The distractors are the total with the smallest row omitted, the two largest rows added, the largest single row, and the total with the largest row omitted."),
 ("8900 thousand",
  "Recomputed in q29 above by subtracting movement out of the urban areas from movement into them. The distractors are the two flows added instead of subtracted, each flow on its own, and the gap between the two rows that do not concern the urban areas."),
 ("joining lower inflation and higher income to greater inequality",
  "EK IEF-3.D.1 supplies the definition and its three mechanisms, EK IEF-3.E.2 the universality across regime types and the split between domestic and external goals, EK IEF-3.E.3 the mixed effects, EK IEF-3.E.4 the bearing on ruling parties' power, and EK IEF-3.E.5 the pollution, sprawl and uneven development."),
]

cg.check(k5_4, CLAIMS,
         table_checks={21: q21, 22: q22, 23: q23, 24: q24, 25: q25, 26: q26, 27: q27, 28: q28, 29: q29})
