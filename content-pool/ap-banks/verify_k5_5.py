"""Key audit for AP COMPARATIVE GOVERNMENT 5.5 International and Supranational
Organizations.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
Learning objective LEG-3.A, three essential knowledge statements, plus one
statement from Unit 3 used once:

  LEG-3.A.1  INTERNATIONAL organizations (IMF, World Bank) exert influence
             THROUGH PRECONDITIONS FOR FINANCIAL ASSISTANCE; STRUCTURAL
             ADJUSTMENT PROGRAMS require PRIVATIZATION OF STATE-OWNED COMPANIES,
             REDUCED TARIFFS and REDUCED GOVERNMENTAL SUBSIDIES OF DOMESTIC
             INDUSTRIES
  LEG-3.A.2  IMPORT SUBSTITUTION INDUSTRIALIZATION bolsters a country's OWN
             DEVELOPING INDUSTRIES, aiming at REDUCING FOREIGN DEPENDENCY by
             RAISING TARIFFS and ENCOURAGING LOCAL PRODUCTION
  LEG-3.A.3  SUPRANATIONAL organizations (ECOWAS, EU, WTO) have SOVEREIGN POWERS
             OVER THE NATIONAL GOVERNMENTS THAT ARE MEMBER STATES and press
             policymakers TO REDUCE TARIFFS and otherwise liberalize trade
  DEM-1.A.5  the United Kingdom has used referenda to decide questions including
             THEIR WITHDRAWAL FROM THE EUROPEAN UNION

THE TARIFF GOES BOTH WAYS, AND THAT IS THE TOPIC. Two of the three statements
press tariffs DOWN and the third raises them, for a reason the framework also
supplies -- reducing foreign dependency. A student who has filed "international
organizations mean free trade" cannot place import substitution at all. Items 10,
17, 24, 25 and the tariff table all turn on that opposition, and items 24 and 25
are checked to require BOTH the direction of the tariff move AND the stated aim,
so a student cannot get them from the arithmetic alone.

THE TWO MECHANISMS ARE NOT THE SAME, and the learning objective's mention of
national sovereignty depends on the difference. Preconditions for financial
assistance are leverage over a government that wants something; sovereign powers
over member states are authority over a government that has joined. Items 11, 18,
28 and 29 key it, and item 15's source-analysis stem is built so that the
mechanism, not the outcome, decides the answer -- an author complaining that
ministers implement decisions they did not take is describing conditionality,
because a sovereign power would bind whether or not funds were sought.

WHAT IS DELIBERATELY NOT ASSERTED: no course country is placed in any named
organization except where the framework itself does so. The single membership
claim in the module is item 12's, resting on EK DEM-1.A.5, which the CED states
and which concerns a settled past referendum rather than a moving condition.
NIGERIA IS NOT PLACED IN ECOWAS ANYWHERE, although it would be natural to do so,
because the CED names ECOWAS only in a list of supranational organizations and
never states any course country's membership of it. No loan, programme, tariff
schedule or negotiation of any real country appears in the module. Every table
figure is HYPOTHETICAL and labelled so.

DATA ITEMS
----------
Items 21-23 read the conditions table, 24-27 the tariff table, 28-29 the
organization table. Item 21's check confirms the table's three rows ARE the
framework's three structural adjustment requirements, so the comparison cannot
drift outside the statement it tests. Every arithmetic distractor is verified to
be a wrong operation on the same table.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k5_5

ACCEPT = "Borrowing governments accepting it, of 40 receiving assistance (hypothetical)"
TBEFORE = "Average tariff before the programme (percent)"
TAFTER = "Average tariff after the programme (percent)"
AIM = "Stated aim of the programme"
ACTS = "How it acts on the governments it deals with"


def q21(table, item):
    rows = [r.lower() for r in cg.labels(table)]
    assert rows == ["privatization of state-owned companies", "reduced tariffs",
                    "reduced governmental subsidies of domestic industries"], \
        f"the rows must be the framework's three structural adjustment requirements; they read {rows}"
    v = {lab: cg.cell(table, lab, ACCEPT) for lab in cg.labels(table)}
    top = max(v, key=v.get)
    assert top == "Privatization of state-owned companies", f"the most accepted condition is {top}"
    assert v[top] == 35, f"the keyed count reads {v[top]}"
    assert v["Reduced governmental subsidies of domestic industries"] == 29 and v["Reduced tariffs"] == 20, \
        "each rejected option must state its own row's true count"
    assert len(set(v.values())) == 3, "'all three equally' must be false"
    assert max(v.values()) <= 40, "no row may exceed the forty governments the table describes"
    return f"the three counts are {[v[l] for l in v]} of 40, and each option states the true count for a different condition"


def q22(table, item):
    c = cg.col(table, ACCEPT)
    total = sum(c)
    assert total == 84, f"the keyed total recomputes to {total}"
    assert total - min(c) == 64, "the 64 distractor must be the total with the smallest row omitted"
    assert max(c) + min(c) == 55, "the 55 distractor must be the largest and smallest rows added"
    assert total - max(c) == 49, "the 49 distractor must be the total with the largest row omitted"
    assert max(c) == 35, "the 35 distractor must be the largest single row"
    return f"the acceptance column reads {c} and sums to {total:.0f}, with every distractor a wrong sum of the same column"


def q23(table, item):
    c = cg.col(table, ACCEPT)
    diff = max(c) - min(c)
    assert diff == 15, f"the keyed difference recomputes to {diff}"
    pairs = {abs(a - b) for a in c for b in c if a != b}
    assert 6 in pairs and 9 in pairs, f"the 6 and 9 distractors must be the other gaps in that column; gaps are {sorted(pairs)}"
    assert max(c) == 35 and min(c) == 20, f"the 35 and 20 distractors must be the extreme rows; the column reads {c}"
    return f"the acceptance column reads {c}, so the largest minus the smallest is {diff:.0f}"


def _prog(table):
    return {lab: (cg.cell(table, lab, TBEFORE), cg.cell(table, lab, TAFTER),
                  str(table["rows"][i][3]).lower())
            for i, lab in enumerate(cg.labels(table))}


def q24(table, item):
    v = _prog(table)
    p2 = v["Programme 2"]
    assert p2[1] > p2[0], f"the keyed programme must raise the tariff; it reads {p2[0]} then {p2[1]}"
    assert "local production" in p2[2], f"the keyed programme must state the local-production aim; it reads {p2[2]!r}"
    assert "dependence on foreign goods" in p2[2], \
        "the keyed programme must also state the reduction of foreign dependence, which is the framework's stated purpose"
    p1 = v["Programme 1"]
    assert p1[1] < p1[0], "the rejected programme must move the tariff the other way, so direction alone separates them"
    assert "local production" not in p1[2], "the rejected programme must not also state the local-production aim"
    return "one programme raises the tariff and states the local-production aim while the other lowers it and states an external condition"


def q25(table, item):
    v = _prog(table)
    p1 = v["Programme 1"]
    assert p1[1] < p1[0], f"the keyed programme must lower the tariff; it reads {p1[0]} then {p1[1]}"
    assert "external financial assistance" in p1[2], f"the keyed programme must state the assistance condition; it reads {p1[2]!r}"
    p2 = v["Programme 2"]
    assert p2[1] > p2[0] and "external financial assistance" not in p2[2], \
        "the rejected programme must both raise the tariff and give a different aim"
    return "one programme lowers the tariff and gives the conditions attached to external assistance as its reason"


def q26(table, item):
    v = _prog(table)
    p1, p2 = v["Programme 1"], v["Programme 2"]
    fall = p1[0] - p1[1]
    assert fall == 15, f"the keyed fall recomputes to {fall}"
    assert p2[1] - p2[0] == 16, "the 16 distractor must be the change recorded in the other programme"
    assert p1[0] == 24 and p1[1] == 9, f"the 24 and 9 distractors must be that row's own figures; it reads {p1[:2]}"
    assert p2[1] == 27, "the 27 distractor must be a figure from the other row read as a change"
    return f"the first programme's tariff goes from {p1[0]:.0f} to {p1[1]:.0f} percent, a fall of {fall:.0f} percentage points"


def q27(table, item):
    v = _prog(table)
    p1, p2 = v["Programme 1"], v["Programme 2"]
    rise = p2[1] - p2[0]
    assert rise == 16, f"the keyed rise recomputes to {rise}"
    assert p1[0] - p1[1] == 15, "the 15 distractor must be the change recorded in the other programme"
    assert p2[0] == 11 and p2[1] == 27, f"the 11 and 27 distractors must be that row's own figures; it reads {p2[:2]}"
    assert p1[0] == 24, "the 24 distractor must be a figure from the other row read as a change"
    return f"the second programme's tariff goes from {p2[0]:.0f} to {p2[1]:.0f} percent, a rise of {rise:.0f} percentage points"


def _org(table):
    return {str(r[0]): str(r[1]).lower() for r in table["rows"]}


def q28(table, item):
    v = _org(table)
    assert "conditions to the financial assistance" in v["Organization 1"], f"the keyed row reads {v['Organization 1']!r}"
    assert "sovereign powers" not in v["Organization 1"], "the keyed row must not also claim sovereign powers"
    assert "sovereign powers" in v["Organization 2"], "the other row must be the sovereign-powers one, so the two are distinguishable"
    return "one row acts through conditions attached to assistance and the other through sovereign powers over member states"


def q29(table, item):
    v = _org(table)
    assert "sovereign powers over the national governments" in v["Organization 2"], f"the keyed row reads {v['Organization 2']!r}"
    assert "member states" in v["Organization 2"], "the keyed row must name member states, as the framework does"
    assert "conditions" not in v["Organization 2"], "the keyed row must not also act through conditions"
    return "one row alone holds sovereign powers over the national governments that are its member states"


CLAIMS = [
 ("preconditions for financial assistance",
  "EK LEG-3.A.1 states that international organizations like the International Monetary Fund and the World Bank exert great influence through preconditions for financial assistance, so the leverage lies in the terms attached to money a government is seeking."),
 ("structural adjustment programs",
  "EK LEG-3.A.1 states that countries receiving assistance from the International Monetary Fund often must agree to structural adjustment programs, which is the vehicle those preconditions arrive in."),
 ("privatization of state-owned companies, reduced tariffs, and reduced governmental subsidies",
  "EK LEG-3.A.1 names privatization of state-owned companies, reduced tariffs, and reduced governmental subsidies of domestic industries as what structural adjustment programs require."),
 ("reducing foreign dependency",
  "EK LEG-3.A.2 states that some countries pass import substitution industrialization policies aimed at reducing foreign dependency, which is the purpose the framework attaches to the policy."),
 ("raising tariffs and encouraging local production of industrialized products",
  "EK LEG-3.A.2 states that import substitution industrialization works by raising tariffs and encouraging local production of industrialized products, so the barrier at the border and the build-up at home operate together."),
 ("the passing country's own developing industries",
  "EK LEG-3.A.2 opens by stating that these policies are passed to bolster the country's own developing industries, which is why they raise barriers against goods produced elsewhere."),
 ("the Economic Community of West African States, the European Union, and the World Trade Organization",
  "EK LEG-3.A.3 names those three as supranational organizations, while EK LEG-3.A.1 treats the International Monetary Fund and the World Bank separately as international organizations acting through loan conditions."),
 ("sovereign powers",
  "EK LEG-3.A.3 states that supranational organizations have sovereign powers over the national governments that are member states, which is authority over a member rather than leverage exercised through an offer."),
 ("to reduce tariffs and otherwise liberalize trade",
  "EK LEG-3.A.3 states that supranational organizations can apply pressure on policymakers to reduce tariffs and otherwise liberalize trade, which runs in the same direction as the conditions named in EK LEG-3.A.1."),
 ("they move tariffs in the opposite direction",
  "EK LEG-3.A.1 requires reduced tariffs and EK LEG-3.A.3 has supranational organizations pressing to reduce them, while EK LEG-3.A.2 states that import substitution industrialization works by raising them."),
 ("conditions a government accepts in order to receive assistance",
  "EK LEG-3.A.1 describes influence exerted through preconditions for financial assistance while EK LEG-3.A.3 states that supranational organizations have sovereign powers over the national governments that are member states, so one is leverage over a request and the other authority over a member."),
 ("the United Kingdom",
  "EK DEM-1.A.5 states that the United Kingdom has used referenda to decide questions including their withdrawal from the European Union, and EK LEG-3.A.3 names the European Union among the supranational organizations with sovereign powers over member states."),
 ("import substitution industrialization",
  "EK LEG-3.A.2 states that import substitution industrialization policies aim at reducing foreign dependency by raising tariffs and encouraging local production of industrialized products, and the scenario contains both instruments."),
 ("required as a precondition for assistance",
  "EK LEG-3.A.1 states that countries receiving assistance often must agree to structural adjustment programs requiring privatization of state-owned companies, reduced tariffs, and reduced governmental subsidies of domestic industries, and the scenario contains all three."),
 ("great influence through preconditions for financial assistance",
  "EK LEG-3.A.1 states that international organizations exert great influence through preconditions for financial assistance, which is the mechanism the argument describes, whereas the sovereign powers of EK LEG-3.A.3 would bind a member whether or not it was seeking funds."),
 ("import substitution industrialization",
  "EK LEG-3.A.2 states that import substitution industrialization aims at reducing foreign dependency by raising tariffs and encouraging local production of industrialized products, which is precisely the trade-off the argument accepts."),
 ("a policy meant to reduce foreign dependency presses them up",
  "EK LEG-3.A.1 requires reduced tariffs as a condition of assistance and EK LEG-3.A.3 has supranational organizations pressing to reduce tariffs and otherwise liberalize trade, while EK LEG-3.A.2's import substitution industrialization raises them to reduce foreign dependency."),
 ("subject to an authority above it",
  "EK LEG-3.A.3 states that supranational organizations have sovereign powers over the national governments that are member states, and the learning objective for EK LEG-3.A is to explain how such organizations influence domestic policymakers and national sovereignty."),
 ("transferred state-owned companies to private owners, lowered import duties",
  "EK LEG-3.A.1 names privatization of state-owned companies, reduced tariffs, and reduced governmental subsidies of domestic industries as the requirements of a structural adjustment program, so the supporting finding must show all three alongside the assistance."),
 ("exert great influence through preconditions for assistance",
  "EK LEG-3.A.1 attributes great influence to preconditions for financial assistance and EK LEG-3.A.3 attributes sovereign powers over member states together with pressure to reduce tariffs and otherwise liberalize trade."),
 ("privatization of state-owned companies, accepted by 35",
  "EK LEG-3.A.1 names privatization of state-owned companies, reduced tariffs, and reduced governmental subsidies of domestic industries as the requirements of structural adjustment programs. Recomputed in q21 above, which also confirms the table's rows are exactly those three and that each option states its own row truly."),
 ("84",
  "Recomputed in q22 above by summing the acceptance column across the three conditions. The distractors are the total with the smallest row omitted, the largest and smallest rows added, the total with the largest row omitted, and the largest single row."),
 ("15",
  "Recomputed in q23 above by subtracting the smallest row from the largest. The distractors are the other two gaps within the same column and the two extreme rows read as though they were differences."),
 ("raised the average tariff and was aimed at building up local production",
  "EK LEG-3.A.2 states that import substitution industrialization aims at reducing foreign dependency by raising tariffs and encouraging local production of industrialized products. Recomputed in q24 above, which requires the keyed row to show both the tariff rise and the stated aim."),
 ("in order to meet the conditions attached to external financial assistance",
  "EK LEG-3.A.1 names reduced tariffs among the requirements of structural adjustment programs and states that they arrive as preconditions for financial assistance. Recomputed in q25 above, which requires the keyed row to show both the tariff fall and that reason."),
 ("15 percentage points",
  "Recomputed in q26 above by subtracting the later average tariff from the earlier one in that row. The distractors are the change recorded in the other row and individual figures from the table read as changes."),
 ("16 percentage points",
  "Recomputed in q27 above by subtracting the earlier average tariff from the later one in that row. The distractors are the change recorded in the other row and individual figures from the table read as changes."),
 ("attaches conditions to the financial assistance it agrees to provide",
  "EK LEG-3.A.1 states that international organizations like the International Monetary Fund and the World Bank exert great influence through preconditions for financial assistance. Recomputed in q28 above, which confirms only one row acts that way."),
 ("sovereign powers over the national governments that are its member states",
  "EK LEG-3.A.3 states that supranational organizations such as the Economic Community of West African States, the European Union, and the World Trade Organization have sovereign powers over the national governments that are member states. Recomputed in q29 above."),
 ("may raise tariffs instead",
  "EK LEG-3.A.1 supplies the conditionality mechanism and its three requirements, EK LEG-3.A.3 the sovereign powers over member states and the pressure to liberalize trade, and EK LEG-3.A.2 the raising of tariffs to reduce foreign dependency, which runs against the other two."),
]

cg.check(k5_5, CLAIMS,
         table_checks={21: q21, 22: q22, 23: q23, 24: q24, 25: q25, 26: q26, 27: q27, 28: q28, 29: q29})
