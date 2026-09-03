"""Key audit for AP ENVIRONMENTAL SCIENCE 5.3 The Green Revolution.

One (anchor, claim) per item, in module order. The anchor must appear in the
KEYED choice and in no distractor.

WHAT THE KEYS REST ON
---------------------
EIN-2.C.1  the Green Revolution started a shift to new agricultural strategies
           and practices in order to increase food production, with both
           positive and negative results; the strategies named are
           mechanization, genetically modified organisms, fertilization,
           irrigation, and the use of pesticides
             -- items 1, 2, 3, 6, 7, 8, 13, 15, 16, 17, 19, 20, 22, 23, 25,
                26, 27
EIN-2.C.2  mechanization of farming can increase profits and efficiency for
           farms, and can also increase reliance on fossil fuels
             -- items 4, 5, 9, 10, 11, 12, 14, 18, 21, 24, 29
both together                            -- items 28, 30

Consequences that belong to neighbouring topics are never keyed here: the
damage done by tilling, slash-and-burn and fertilizers is EIN-2.D.1 (5.4), the
losses and hazards of irrigation are EIN-2.E and EIN-2.F (5.5), and pesticide
resistance and lost crop genetic diversity are EIN-2.G (5.6). Item 26 uses
those four statements as distractors precisely because they are real framework
claims sitting in other topics.

DATA ITEMS: 6, 7, 8, 9, 10, 11, 12, 15, 16, 17, 18 and 27 carry tables. Each
keyed conclusion is recomputed below from that table alone and anchored to a
named row.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and every table in turn, and requires each
corruption to raise, BEFORE the real gate runs.
"""
import e_check
import cg_check as cg
import e5_3

GRAIN = "Grain harvested per hectare (tonnes)"
FERT = "Fertilizer applied per hectare (kilograms)"
LABOUR = "Hours of human labour per hectare per season"
DIESEL = "Litres of diesel fuel used per hectare per season"
AREA = "Area worked in one season (hectares)"
NET = "Net return over the season (currency units)"
ENERGY = "Energy used per hectare per season (megajoules)"
YIELD_R = "Grain produced per hectare after the shift (tonnes)"
FOSSIL = "Fossil fuel energy used per hectare after the shift (megajoules)"

BEFORE = "Before the shift in practices"
TEN = "Ten years after the shift"
TWENTY = "Twenty years after the shift"
HAND = "Farm using hand tools and animals"
MECHANIZED = "Farm using tractors and harvesters"
FERT_MAKE = "Manufacture of the fertilizer applied"


def q6(table, item):
    g = cg.col(table, GRAIN)
    f = cg.col(table, FERT)
    assert cg.cell(table, BEFORE, GRAIN) == min(g), "the pre-shift row must hold the lowest yield"
    assert all(g[i] < g[i + 1] for i in range(len(g) - 1)), f"yield must rise; got {g}"
    assert all(f[i] < f[i + 1] for i in range(len(f) - 1)), f"fertilizer must rise; got {f}"
    return (f"grain runs {g} tonnes per hectare while fertilizer runs {f} kilograms, both "
            "rising with no reversal")


def q7(table, item):
    r = cg.cell(table, TWENTY, GRAIN) / cg.cell(table, BEFORE, GRAIN)
    assert r == 3, f"the yield ratio recomputes to {r}, not 3"
    fr = cg.cell(table, TWENTY, FERT) / cg.cell(table, BEFORE, FERT)
    assert fr != r, "the fertilizer ratio distractor must differ from the key"
    return f"3.0 divided by 1.0 is {r:.0f}, against a fertilizer ratio of {fr:.0f}"


def q8(table, item):
    d = cg.cell(table, TWENTY, FERT) - cg.cell(table, BEFORE, FERT)
    assert d == 140, f"the rise recomputes to {d}, not 140"
    for wrong in (150, 90, 50, 160):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"150 minus 10 is {d:.0f} kilograms per hectare of additional fertilizer"


def q9(table, item):
    assert cg.cell(table, MECHANIZED, LABOUR) < cg.cell(table, HAND, LABOUR), \
        "the mechanized farm must use less human labour"
    assert cg.cell(table, MECHANIZED, DIESEL) > cg.cell(table, HAND, DIESEL), \
        "the mechanized farm must use more diesel"
    assert cg.cell(table, HAND, DIESEL) == 0, \
        "the unmechanized farm must show no diesel requirement at all"
    return (f"labour falls from {cg.cell(table, HAND, LABOUR):.0f} hours to "
            f"{cg.cell(table, MECHANIZED, LABOUR):.0f} while diesel rises from none to "
            f"{cg.cell(table, MECHANIZED, DIESEL):.0f} litres per hectare per season")


def q10(table, item):
    d = cg.cell(table, HAND, LABOUR) - cg.cell(table, MECHANIZED, LABOUR)
    assert d == 202, f"the saving recomputes to {d}, not 202"
    for wrong in (220, 18, 95, 238):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"220 minus 18 is {d:.0f} hours of human labour saved per hectare per season"


def q11(table, item):
    assert cg.cell(table, MECHANIZED, AREA) > cg.cell(table, HAND, AREA), \
        "the mechanized farm must work the larger area"
    assert cg.cell(table, MECHANIZED, NET) > cg.cell(table, HAND, NET), \
        "the mechanized farm must return the larger amount"
    assert cg.cell(table, HAND, NET) > 0, "'neither farm returned anything' must be false"
    return (f"the mechanized farm works {cg.cell(table, MECHANIZED, AREA):.0f} hectares against "
            f"{cg.cell(table, HAND, AREA):.0f} and returns "
            f"{cg.cell(table, MECHANIZED, NET):.0f} against {cg.cell(table, HAND, NET):.0f}")


def q12(table, item):
    mech = cg.cell(table, MECHANIZED, NET) / cg.cell(table, MECHANIZED, AREA)
    hand = cg.cell(table, HAND, NET) / cg.cell(table, HAND, AREA)
    assert mech == 600, f"the mechanized per-hectare return recomputes to {mech}, not 600"
    assert hand == 500, f"the unmechanized per-hectare return recomputes to {hand}, not 500"
    assert mech > hand, "the mechanized farm must be the higher of the two per hectare"
    return f"90,000 over 150 is {mech:.0f} per hectare against 3,000 over 6, which is {hand:.0f}"


def q15(table, item):
    e = dict(zip(cg.labels(table), cg.col(table, ENERGY)))
    assert max(e, key=e.get) == FERT_MAKE, f"the largest input is {max(e, key=e.get)}"
    assert len(set(e.values())) == len(e), "'the four inputs were equal' must be false"
    return (f"the four inputs read {list(e.values())} megajoules per hectare per season, "
            "largest for fertilizer manufacture")


def q16(table, item):
    tot = sum(cg.col(table, ENERGY))
    assert tot == 11400, f"the total recomputes to {tot}, not 11,400"
    for wrong in (9000, 5400, 10800, 3600):
        assert tot != wrong, f"the {wrong} distractor equals the key"
    return f"3,600 plus 5,400 plus 1,800 plus 600 is {tot:.0f} megajoules per hectare per season"


def q17(table, item):
    pairs = sorted(zip(cg.col(table, YIELD_R), cg.col(table, FOSSIL)))
    assert cg.cell(table, "Region A", YIELD_R) == min(cg.col(table, YIELD_R)), \
        "Region A must be the lowest-yielding region"
    assert all(pairs[i][1] < pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"fossil fuel energy must rise with yield; got {pairs}"
    assert len(set(cg.col(table, FOSSIL))) > 1, "'the same energy everywhere' must be false"
    return (f"sorted by yield the fossil fuel energies are {[e for _, e in pairs]} megajoules "
            "per hectare, rising without exception")


def q18(table, item):
    y = dict(zip(cg.labels(table), cg.col(table, YIELD_R)))
    lowest = min(y, key=y.get)
    assert lowest == "Region A", f"the lowest-yielding region is {lowest}"
    per = cg.cell(table, lowest, FOSSIL) / cg.cell(table, lowest, YIELD_R)
    assert per == 2000, f"the energy per tonne recomputes to {per}, not 2,000"
    for wrong in (3000, 4000, 6000, 1000):
        assert per != wrong, f"the {wrong} distractor equals the key"
    return f"2,000 megajoules divided by 1.0 tonne is {per:.0f} megajoules per tonne"


def q27(table, item):
    first = cg.cell(table, BEFORE, FERT) / cg.cell(table, BEFORE, GRAIN)
    last = cg.cell(table, TWENTY, FERT) / cg.cell(table, TWENTY, GRAIN)
    assert first == 10, f"the opening ratio recomputes to {first}, not 10"
    assert last == 50, f"the closing ratio recomputes to {last}, not 50"
    assert last > first, "the fertilizer needed per tonne must rise across the period"
    return (f"10 over 1.0 is {first:.0f} kilograms per tonne and 150 over 3.0 is {last:.0f}, "
            "so more fertilizer was needed for each tonne at the end")


CLAIMS = [
 ("intended to increase food production",
  "EIN-2.C.1 states that the Green Revolution started a shift to new agricultural strategies and practices in order to increase food production. The rejected options reverse that purpose or describe a programme the framework does not mention."),
 ("genetically modified organisms, fertilization",
  "EIN-2.C.1 names mechanization, genetically modified organisms, fertilization, irrigation, and the use of pesticides. The rejected groups are the soil conservation methods of STB-1.E.1, the forestry methods of STB-1.G, the meat production methods of EIN-2.H.1, and the urban runoff methods of STB-1.B.1."),
 ("both positive and negative",
  "EIN-2.C.1 states that the shift was made in order to increase food production, WITH BOTH POSITIVE AND NEGATIVE RESULTS. The framework therefore refuses both one-sided readings and does not treat the outcome as unmeasured."),
 ("Increase profits and efficiency",
  "EIN-2.C.2, near verbatim: mechanization of farming can increase profits and efficiency for farms. Each rejected option drops or reverses one half of that pairing."),
 ("increase a farm's reliance on fossil fuels",
  "EIN-2.C.2 states that mechanization can also increase reliance on fossil fuels. Genetic diversity belongs to EIN-2.G.2 and the water table to EIN-2.F.1, and the framework nowhere makes machinery a substitute for fertilizer."),
 ("rose alongside it",
  "Recomputed in q6 above: grain 1.0, 2.0 and 3.0 tonnes per hectare against fertilizer 10, 60 and 150 kilograms. EIN-2.C.1 names fertilization among the strategies of a shift undertaken in order to increase food production."),
 ("Three times as much",
  "Recomputed in q7 above: 3.0 divided by 1.0. The rejected values come from the ten-year row, from the fertilizer ratio, or from denying the yields differ."),
 ("A rise of 140 kilograms",
  "Recomputed in q8 above: 150 minus 10 kilograms per hectare. The rejected values quote the final figure alone, pair the wrong rows, or add the two figures."),
 ("introducing a fuel requirement",
  "Recomputed in q9 above: labour falls from 220 hours to 18 while diesel rises from none to 95 litres per hectare per season. EIN-2.C.2 names both sides, the efficiency gain and the increased reliance on fossil fuels."),
 ("202 hours",
  "Recomputed in q10 above: 220 minus 18 hours per hectare per season. The rejected values are the two labour figures themselves, the diesel figure, and their sum."),
 ("returned far more over the season",
  "Recomputed in q11 above: 150 hectares against 6 and 90,000 currency units against 3,000. EIN-2.C.2 states that mechanization can increase profits and efficiency for farms."),
 ("which is more than the 500",
  "Recomputed in q12 above: 90,000 over 150 is 600 currency units per hectare against 3,000 over 6, which is 500. The rejected options reverse the comparison or read a whole-season total as a per-hectare figure."),
 ("the only result worth counting",
  "The author moves from a single measured gain to the word unqualified, which requires that nothing else counts. EIN-2.C.1 states that the shift produced BOTH positive and negative results, so the framework denies the assumption the author needs."),
 ("since mechanization can increase reliance on fossil fuels",
  "EIN-2.C.2 affirms the profit and efficiency half of the quoted sentence and then adds increased reliance on fossil fuels, which is a change in what the farms consume. Only the final clause is at odds with the framework."),
 ("manufacture of the fertilizer applied",
  "Recomputed in q15 above: 3,600, 5,400, 1,800 and 600 megajoules per hectare per season, largest for fertilizer manufacture. Fertilization, irrigation, mechanization and pesticide use are four of the five strategies EIN-2.C.1 lists."),
 ("11,400",
  "Recomputed in q16 above by adding the four tabulated categories. The rejected values omit one or more categories or quote a single row."),
 ("also used more fossil fuel energy",
  "Recomputed in q17 above: sorted by yield, the fossil fuel energies rise from 2,000 to 6,000 to 12,000 megajoules per hectare. EIN-2.C.1 records both positive and negative results, and EIN-2.C.2 names increased fossil fuel reliance as one of them."),
 ("2,000 megajoules per tonne",
  "Recomputed in q18 above: 2,000 megajoules divided by 1.0 tonne in the lowest-yielding region. The rejected values are the other regions' figures per tonne and a halved quotient."),
 ("To increase food production",
  "EIN-2.C.1 states that the shift was made IN ORDER TO INCREASE FOOD PRODUCTION. Reducing cultivated area, lowering fertilizer use and restoring soil are not purposes the framework assigns, and machinery is one of the strategies rather than something the shift removed."),
 ("soil conservation method rather than",
  "EIN-2.C.1 names mechanization, genetically modified organisms, fertilization, irrigation and the use of pesticides, and contour plowing is not among them; STB-1.E.1 places it under soil conservation. The framework does supply a list, so denying that is wrong on its face."),
 ("Output per hour of human labour",
  "EIN-2.C.2 makes two claims, one about efficiency and one about fossil fuel reliance, so a test needs one measurement of each. Output per hour of labour measures efficiency and fuel per hectare measures fossil fuel reliance."),
 ("among the methods adopted",
  "EIN-2.C.1 places genetically modified organisms in its list of strategies and methods alongside mechanization, fertilization, irrigation and the use of pesticides, and that list is introduced as the means by which food production was to be increased."),
 ("because the framework records negative as well as positive",
  "EIN-2.C.1 states that the shift produced BOTH positive AND negative results, so a yield gain does not by itself establish that nothing was lost. The framework does record the purpose of increasing food production, so denying any yield change misreads it."),
 ("therefore buys fuel every season",
  "EIN-2.C.2 states that mechanization can increase reliance on fossil fuels, and substituting diesel machinery for animal power is that increase. The rejected options reduce fuel use or describe practices the framework places elsewhere in the unit."),
 ("says the shift produced both positive and negative results",
  "EIN-2.C.1 contains the phrase with both positive and negative results, which is a two-sided verdict on its face. The framework also names five strategies and gives the purpose as increasing food production."),
 ("Mechanization, which can raise profits",
  "EIN-2.C.2 is the framework's second statement in this topic and it is about mechanization alone. The other four claims offered are real framework statements but they sit in EIN-2.F.1, EIN-2.G.1 and EIN-2.G.2, in topics 5.5 and 5.6."),
 ("rose from 10 kilograms per tonne to 50",
  "Recomputed in q27 above: 10 over 1.0 tonne at the start and 150 over 3.0 tonnes at the end. EIN-2.C.1 records both positive and negative results from the shift, and this is one of each in the same data."),
 ("takes one of those strategies",
  "EIN-2.C.1 introduces the shift, its purpose, its mixed results and its five strategies; EIN-2.C.2 then develops mechanization, one member of that list, into profits, efficiency and fossil fuel reliance. The second elaborates the first."),
 ("fuel energy the farm consumes for each tonne",
  "EIN-2.C.2 names increased reliance on fossil fuels as the consequence in question, and fuel energy per tonne of output measures that reliance against the yield the cooperative wants to keep. Labour hours, price, area and machine count each leave one aim unmeasured."),
 ("with mixed results",
  "EIN-2.C.1 supplies the purpose, the mixed verdict and the list of strategies, and EIN-2.C.2 supplies mechanization's profits, efficiency and fossil fuel reliance. Each rejected summary reverses the purpose, drops the negative results, or adds a condition the framework does not state."),
]

TABLE_CHECKS = {6: q6, 7: q7, 8: q8, 9: q9, 10: q10, 11: q11, 12: q12, 15: q15,
                16: q16, 17: q17, 18: q18, 27: q27}

e_check.run(e5_3, CLAIMS, TABLE_CHECKS)
