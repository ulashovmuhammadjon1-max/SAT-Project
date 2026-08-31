"""Key audit for AP COMPARATIVE GOVERNMENT 5.7 Impact of Industrialization and
Economic Development.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
Learning objective LEG-3.C, three essential knowledge statements:

  LEG-3.C.1  RAPID INDUSTRIALIZATION and DEPENDENCE ON FOSSIL FUELS create
             problems governments MUST ADDRESS TO PROTECT CITIZENS; solutions are
             .a MOVING FACTORIES + GREEN TECHNOLOGY SUBSIDIES + INFRASTRUCTURE AND
             REGULATION, .b LAWS REQUIRING NATIONWIDE CONVERSION TO HYBRID AND
             BATTERY-POWERED AUTOS for AIR POLLUTION IN MAJOR CITIES, .c
             INFRASTRUCTURE TO RESPOND TO HEALTH CRISES RELATED TO SYSTEMIC
             POLLUTION
  LEG-3.C.2  TRADE LIBERALIZATION affects business growth, DIRECT FOREIGN
             INVESTMENT, FOREIGN EXCHANGE RATES, POPULATION MOVEMENT and the
             QUALITY OF THE ENVIRONMENT; REDUCING TARIFFS lowers consumer costs AT
             THE EXPENSE OF DOMESTIC INDUSTRY, INCREASING TARIFFS protects
             industry AT THE EXPENSE OF HIGHER CONSUMER PRICES
  LEG-3.C.3  BUDGET DEFICITS RESULTING FROM WORLD MARKET FLUCTUATIONS lead to
             AUSTERITY MEASURES, which result in FUNDING CUTS TO STATE PROGRAMS

LEG-3.C.2 IS A SYMMETRICAL TRADE-OFF and it is the best item this topic offers,
which is why the suggested skill here is refutation and concession. The framework
attaches a cost to EACH direction in a single sentence, so there is no free
option, only two distributions of gain and loss. Items 7, 8, 11, 18 and 21 rest
on it. Item 21's check requires the two columns to move in the SAME direction as
the tariff -- that is, for consumer prices and domestic employment to rise and
fall together -- because a table in which one setting improved both would make
the key false while the item still read as answerable.

LEG-3.C.1's THREE SOLUTIONS ARE NOT INTERCHANGEABLE. The first acts on where
production happens and how it is regulated; the second is one nationwide mandate
about vehicles; the third responds to harm ALREADY DONE rather than preventing
it. Items 12, 13, 27, 28 and 29 key those differences, and item 29 is written so
that the distinction, not the subject matter, decides the answer.

LEG-3.C.3 IS A THREE-LINK CHAIN students shorten to one: world market
fluctuations, then budget deficits, then austerity, then funding cuts. An answer
that begins at austerity has dropped the reason the framework supplies. Items 9,
10, 17, 19 and 20 keep the chain intact, and item 20's supporting finding is
written to contain the external shock, the deficit AND the cuts in that order.

NOTHING HERE TURNS ON CURRENT EVENTS: no country's tariff schedule, budget,
emissions rule, export price or programme is asserted anywhere in the module.
Every table figure is HYPOTHETICAL and labelled so, and both economies are
unnamed.

DATA ITEMS
----------
Items 21-23 read the tariff table, 24-26 the austerity table, 27-29 the measures
table. Every arithmetic distractor is verified below to be a wrong operation on
the same table; the two range items deliberately draw their distractors from the
OTHER column as well as their own, so a student who reads the right rows but the
wrong column still lands on a listed option rather than guessing.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k5_7

PRICE = "Consumer price index"
EMPLOY = "Domestic manufacturing employment index"
FBEFORE = "Funding before the austerity measures (index)"
FAFTER = "Funding after the austerity measures (index)"
DID = "What the government did"


def _trade(table):
    return {lab: (cg.cell(table, lab, PRICE), cg.cell(table, lab, EMPLOY)) for lab in cg.labels(table)}


def q21(table, item):
    v = _trade(table)
    lo, mid, hi = v["Tariffs reduced"], v["Tariffs unchanged"], v["Tariffs increased"]
    assert lo[0] < mid[0] < hi[0], f"consumer prices must rise with the tariff; they read {[lo[0], mid[0], hi[0]]}"
    assert lo[1] < mid[1] < hi[1], f"domestic employment must rise with the tariff; it reads {[lo[1], mid[1], hi[1]]}"
    assert mid == (100, 100), f"the unchanged row must be the base of both indices; it reads {mid}"
    assert not (lo[0] < mid[0] and lo[1] > mid[1]), "no setting may improve both columns, or the trade-off would not hold"
    assert not (hi[1] > mid[1] and hi[0] < mid[0]), "the increased-tariff row must not improve both columns either"
    return (f"across the three settings consumer prices read {[lo[0], mid[0], hi[0]]} and domestic employment "
            f"{[lo[1], mid[1], hi[1]]}, both moving with the tariff so neither setting improves both")


def q22(table, item):
    p, e = cg.col(table, PRICE), cg.col(table, EMPLOY)
    rng = max(p) - min(p)
    assert rng == 31, f"the keyed range recomputes to {rng}"
    assert max(p) - 100 == 17, "the 17 distractor must be the gap between the top two price settings"
    assert 100 - min(p) == 14, "the 14 distractor must be the gap between the bottom two price settings"
    assert max(e) - min(e) == 33, "the 33 distractor must be the other column's range"
    assert 100 - min(e) == 21, "the 21 distractor must be a gap within the other column"
    return f"the price column reads {p}, so its range is {rng:.0f} points"


def q23(table, item):
    p, e = cg.col(table, PRICE), cg.col(table, EMPLOY)
    rng = max(e) - min(e)
    assert rng == 33, f"the keyed range recomputes to {rng}"
    assert max(e) - 100 == 12, "the 12 distractor must be the gap between the top two employment settings"
    assert 100 - min(e) == 21, "the 21 distractor must be the gap between the bottom two employment settings"
    assert max(p) - min(p) == 31, "the 31 distractor must be the other column's range"
    assert max(p) - 100 == 17, "the 17 distractor must be a gap within the other column"
    return f"the employment column reads {e}, so its range is {rng:.0f} points"


def _cuts(table):
    return {lab: cg.cell(table, lab, FBEFORE) - cg.cell(table, lab, FAFTER) for lab in cg.labels(table)}


def q24(table, item):
    before = cg.col(table, FBEFORE)
    assert set(before) == {100}, f"every programme must start from the same base, or the cuts are not comparable; it reads {before}"
    v = _cuts(table)
    top = max(v, key=v.get)
    assert top == "Adult training", f"the largest cut falls on {top}"
    assert v["Adult training"] == 36, f"the keyed cut recomputes to {v['Adult training']}"
    assert v["Public transport"] == 22 and v["Environmental inspection"] == 29, \
        "each rejected option must state its own row's true cut"
    assert all(c > 0 for c in v.values()), "'austerity measures do not reduce funding' must be false"
    assert len(set(v.values())) == 3, "'all three by the same amount' must be false"
    return f"the three cuts are {[v[l] for l in v]} points, the largest of them {v[top]:.0f}"


def q25(table, item):
    v = _cuts(table)
    total = sum(v.values())
    assert total == 87, f"the keyed total recomputes to {total}"
    assert total - v["Public transport"] == 65, "the 65 distractor must be the total with the smallest cut omitted"
    assert total - v["Environmental inspection"] == 58, "the 58 distractor must be the total with the middle cut omitted"
    assert total - v["Adult training"] == 51, "the 51 distractor must be the total with the largest cut omitted"
    assert max(v.values()) == 36, "the 36 distractor must be the largest single cut"
    return f"the three cuts are {[v[l] for l in v]} and sum to {total:.0f} points"


def q26(table, item):
    v = _cuts(table)
    diff = max(v.values()) - min(v.values())
    assert diff == 14, f"the keyed difference recomputes to {diff}"
    others = sorted(v.values())
    assert others[1] - others[0] == 7, "the 7 distractor must be the gap between the other two cuts"
    assert sorted(v.values()) == [22, 29, 36], f"the 36, 29 and 22 distractors must be the cuts themselves; they are {sorted(v.values())}"
    return f"the cuts are {sorted(v.values())}, so the largest minus the smallest is {diff:.0f} points"


def _meas(table):
    return {str(r[0]): str(r[1]).lower() for r in table["rows"]}


def q27(table, item):
    v = _meas(table)
    m = v["Measure 1"]
    for needle in ("relocated factories", "subsidies", "environmental regulation"):
        assert needle in m, f"the keyed measure must contain {needle!r}; it reads {m!r}"
    for k in ("Measure 2", "Measure 3"):
        assert "subsidies" not in v[k], f"{k} must not also pay subsidies for compliance"
    return "one measure alone relocates factories, subsidizes cleaner technology and tightens regulation"


def q28(table, item):
    v = _meas(table)
    m = v["Measure 2"]
    assert "hybrid and battery-powered" in m, f"the keyed measure reads {m!r}"
    assert "whole country" in m, "the keyed measure must be nationwide, as the framework's statement is"
    for k in ("Measure 1", "Measure 3"):
        assert "hybrid" not in v[k], f"{k} must not also mandate hybrid vehicles"
    return "one measure alone requires the whole country to convert to hybrid and battery-powered vehicles"


def q29(table, item):
    v = _meas(table)
    m = v["Measure 3"]
    assert "respond to illness" in m, f"the keyed measure reads {m!r}"
    assert "clinics" in m, "the keyed measure must build the responding infrastructure the framework names"
    for k in ("Measure 1", "Measure 2"):
        assert "illness" not in v[k], f"{k} must act on the source of the pollution rather than on harm already done"
    return "one measure alone answers illness already caused, while the other two act on production and on vehicles"


CLAIMS = [
 ("rapid industrialization and increasing dependence on energy from fossil fuels",
  "EK LEG-3.C.1 states that rapid industrialization and increasing dependence on energy from fossil fuels have created a variety of environmental and political problems that governments must address."),
 ("to protect citizens",
  "EK LEG-3.C.1 states that these are problems governments must address to protect citizens, which places the obligation in the relationship between a government and its own people rather than in an external requirement."),
 ("physically moving factories, implementing green technologies with subsidies",
  "EK LEG-3.C.1.a names physically moving factories, implementing green technologies with subsidies for industry compliance, and engaging in increased infrastructure development and environmental regulation."),
 ("air pollution problems in major cities from auto and industrial emissions",
  "EK LEG-3.C.1.b states that laws requiring nationwide conversion to hybrid and battery-powered autos address air pollution problems in major cities from auto and industrial emissions, naming both the place and the two sources."),
 ("health crises related to systemic pollution",
  "EK LEG-3.C.1.c states that governments develop infrastructure and other mechanisms to respond to health crises related to systemic pollution, which answers harm that has already occurred."),
 ("foreign exchange rates, population movement, and often the quality of the environment",
  "EK LEG-3.C.2 names the growth of domestic and foreign business, the amount of direct foreign investment, foreign exchange rates, population movement, and often the quality of the environment as what trade liberalization affects."),
 ("lower consumer costs come at the expense of domestic industry",
  "EK LEG-3.C.2 states that reducing tariffs may lower consumer costs at the expense of domestic industry, so the gain and the cost fall on different groups inside the same country."),
 ("at the expense of higher consumer prices",
  "EK LEG-3.C.2 states that increasing tariffs may protect domestic industry against foreign imports but at the expense of higher consumer prices, which is the mirror image of the cost of cutting them."),
 ("world market fluctuations",
  "EK LEG-3.C.3 states that governments concerned with budget deficits resulting from world market fluctuations often must adopt austerity measures, so the chain begins outside the government's own decisions."),
 ("funding cuts to state programs",
  "EK LEG-3.C.3 states that austerity measures result in funding cuts to state programs, which is the framework's own statement of what those measures amount to in practice."),
 ("cutting tariffs burdens domestic industry and raising them burdens consumers",
  "EK LEG-3.C.2 attaches a cost to each direction in a single sentence, so the choice is between two distributions of gain and loss rather than between a good option and a bad one."),
 ("a single nationwide requirement about the vehicles people use",
  "EK LEG-3.C.1.a moves factories, subsidizes cleaner technology and tightens regulation, while EK LEG-3.C.1.b passes laws requiring nationwide conversion to hybrid and battery-powered autos, so one reshapes production and the other mandates a change in what is driven."),
 ("responds to harm that has already occurred",
  "EK LEG-3.C.1.c has governments develop infrastructure and other mechanisms to respond to health crises related to systemic pollution, whereas EK LEG-3.C.1.a and EK LEG-3.C.1.b act on the sources of the pollution itself."),
 ("green technologies with subsidies for compliance",
  "EK LEG-3.C.1.a names physically moving factories, implementing green technologies with subsidies for industry compliance, and increased environmental regulation, and the scenario contains all three of those elements."),
 ("passing laws that require nationwide conversion",
  "EK LEG-3.C.1.b names passing laws that require nationwide conversion to hybrid and battery-powered autos to address air pollution problems in major cities, and the scenario states both the mandate and that reason."),
 ("developing infrastructure and other mechanisms to respond to health crises",
  "EK LEG-3.C.1.c names developing infrastructure and other mechanisms to respond to health crises related to systemic pollution, which is what clinics and monitoring in affected districts amount to."),
 ("budget deficits resulting from world market fluctuations",
  "EK LEG-3.C.3 runs from world market fluctuations through budget deficits to austerity measures and then to funding cuts to state programs, and the scenario follows that chain from beginning to end."),
 ("grants that consumer costs may fall",
  "EK LEG-3.C.2 states that reducing tariffs may lower consumer costs at the expense of domestic industry, so the rebuttal concedes the benefit and names the cost the same sentence attaches to it rather than denying the benefit."),
 ("the pressure begins outside the government's own choices",
  "EK LEG-3.C.3 states that governments concerned with budget deficits resulting from world market fluctuations often must adopt austerity measures, which result in funding cuts to state programs, so both the external pressure and the domestic cuts belong to the framework's statement."),
 ("collapsed, the budget fell into deficit the following year",
  "EK LEG-3.C.3 names world market fluctuations as the source of the deficits that lead to austerity measures and funding cuts, so the supporting finding has to contain the external shock, the deficit and the cuts in that order."),
 ("neither setting improves both at once",
  "EK LEG-3.C.2 states that reducing tariffs lowers consumer costs at the expense of domestic industry while increasing them protects industry at the expense of higher consumer prices. Recomputed in q21 above, which requires both columns to move with the tariff so that no setting improves both."),
 ("31 points",
  "Recomputed in q22 above by subtracting the smallest consumer price figure from the largest. The distractors are the two gaps between neighbouring settings, the other column's range, and a gap within that other column."),
 ("33 points",
  "Recomputed in q23 above by subtracting the smallest employment figure from the largest. The distractors are the two gaps between neighbouring settings, the other column's range, and a gap within that other column."),
 ("adult training, cut by 36 points",
  "EK LEG-3.C.3 states that austerity measures result in funding cuts to state programs. Recomputed in q24 above, which also confirms that all three programmes start from the same base so the cuts are comparable."),
 ("87 points",
  "Recomputed in q25 above by adding the three reductions. The distractors are the total with each row omitted in turn and the largest single reduction."),
 ("14 points",
  "Recomputed in q26 above by subtracting the smallest reduction from the largest. The distractors are the gap between the other two reductions and the three reductions themselves read as a difference."),
 ("relocated factories, paid subsidies for cleaner technology",
  "EK LEG-3.C.1.a names physically moving factories, implementing green technologies with subsidies for industry compliance, and increased environmental regulation. Recomputed in q27 above, where one measure alone contains all three."),
 ("requiring the whole country to convert to hybrid and battery-powered vehicles",
  "EK LEG-3.C.1.b names passing laws that require nationwide conversion to hybrid and battery-powered autos. Recomputed in q28 above, where one measure alone is a nationwide vehicle requirement."),
 ("respond to illness caused by long-term pollution",
  "EK LEG-3.C.1.c has governments develop infrastructure and other mechanisms to respond to health crises related to systemic pollution, whereas the other two statements act on where production happens and on what is driven. Recomputed in q29 above."),
 ("trade policy imposes a cost whichever way it moves",
  "EK LEG-3.C.1 supplies the three solutions, EK LEG-3.C.2 the two-sided cost of moving tariffs in either direction, and EK LEG-3.C.3 the chain from world market fluctuations through deficits and austerity to funding cuts to state programs."),
]

cg.check(k5_7, CLAIMS,
         table_checks={21: q21, 22: q22, 23: q23, 24: q24, 25: q25, 26: q26, 27: q27, 28: q28, 29: q29})
