"""Key audit for AP ENVIRONMENTAL SCIENCE 5.2 Clearcutting.

One (anchor, claim) per item, in module order. The anchor must appear in the
KEYED choice and in no distractor.

WHAT THE KEYS REST ON
---------------------
EIN-2.B.1  clearcutting can be economically advantageous but leads to soil
           erosion, increased soil and stream temperatures, and flooding
             -- items 1, 4, 5, 6, 7, 10, 11, 12, 13, 15, 16, 17, 19, 21, 22,
                23, 24, 26, 29
EIN-2.B.2  forests contain trees that absorb pollutants and store carbon
           dioxide; the cutting and burning of trees releases carbon dioxide
           and contributes to climate change
             -- items 2, 3, 8, 9, 14, 18, 25
both together                            -- items 20, 27, 30

The framework supplies no mechanism for the temperature increase, so item 16
keys the absence of one rather than inventing a cause. Mitigation methods
(reforestation, sustainable harvest, prescribed burn) belong to STB-1.G in
topic 5.17 and are never a key here.

DATA ITEMS: 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 23 and 28 carry tables. Each
keyed conclusion is recomputed below from that table alone, anchored to a named
row so that reversing two columns together cannot leave a check passing.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and every table in turn, and requires each
corruption to raise, BEFORE the real gate runs.
"""
import e_check
import cg_check as cg
import e5_2

SED = "Sediment carried out in streamflow (tonnes per square kilometer per year)"
PEAK = "Peak streamflow after a heavy storm (cubic meters per second)"
SOILT = "Mean summer soil temperature near the surface (degrees Celsius)"
STREAMT = "Mean summer temperature of the stream draining the site (degrees Celsius)"
CARBON = "Carbon stored in living trees (tonnes per hectare)"
VALUE = "Value of the timber removed (currency units per hectare)"
COST = "Cost of the operation (currency units per hectare)"
LOSS = "Sediment leaving the watershed (tonnes per square kilometer per year)"
PM = ("Particulate matter removed from the air by vegetation in one year "
      "(kilograms per hectare)")

UNCUT = "Left uncut"
CUT = "Clearcut two years earlier"
CANOPY = "Under an intact forest canopy"
OPENED = "In an adjacent clearcut area"
MATURE = "Mature forest"
BURNED = "Just after clearcutting and burning"
BEFORE = "The year before the harvest"
YEAR1 = "One year after the harvest"
YEAR8 = "Eight years after the harvest"


def q4(table, item):
    assert cg.cell(table, CUT, SED) > cg.cell(table, UNCUT, SED), \
        "the clearcut watershed must lose more sediment"
    assert cg.cell(table, CUT, PEAK) > cg.cell(table, UNCUT, PEAK), \
        "the clearcut watershed must produce the higher storm peak"
    assert cg.cell(table, CUT, SED) != cg.cell(table, UNCUT, SED), "'the same sediment' must be false"
    return (f"the clearcut watershed reads {cg.cell(table, CUT, SED):.0f} tonnes against "
            f"{cg.cell(table, UNCUT, SED):.0f} and {cg.cell(table, CUT, PEAK):.0f} cubic "
            f"meters per second against {cg.cell(table, UNCUT, PEAK):.0f}, higher on both")


def q5(table, item):
    r = cg.cell(table, CUT, SED) / cg.cell(table, UNCUT, SED)
    assert r == 8, f"the ratio recomputes to {r}, not 8"
    peak_r = cg.cell(table, CUT, PEAK) / cg.cell(table, UNCUT, PEAK)
    assert peak_r != r, "the storm-peak ratio distractor must differ from the key"
    return f"96 divided by 12 is {r:.0f}, against a storm-peak ratio of {peak_r:.0f}"


def q6(table, item):
    assert cg.cell(table, OPENED, SOILT) > cg.cell(table, CANOPY, SOILT), \
        "the clearcut soil must be the warmer of the two"
    assert cg.cell(table, OPENED, STREAMT) > cg.cell(table, CANOPY, STREAMT), \
        "the clearcut stream must be the warmer of the two"
    return (f"the clearcut area reads {cg.cell(table, OPENED, SOILT):.0f} degrees in the soil "
            f"against {cg.cell(table, CANOPY, SOILT):.0f}, and "
            f"{cg.cell(table, OPENED, STREAMT):.0f} in the stream against "
            f"{cg.cell(table, CANOPY, STREAMT):.0f}")


def q7(table, item):
    d = cg.cell(table, OPENED, SOILT) - cg.cell(table, CANOPY, SOILT)
    assert d == 10, f"the soil difference recomputes to {d}, not 10"
    ds = cg.cell(table, OPENED, STREAMT) - cg.cell(table, CANOPY, STREAMT)
    assert ds != d, "the stream difference must differ from the key"
    return f"24 minus 14 is {d:.0f} degrees Celsius, against a stream difference of {ds:.0f}"


def q8(table, item):
    c = dict(zip(cg.labels(table), cg.col(table, CARBON)))
    assert min(c, key=c.get) == BURNED, f"the smallest store belongs to {min(c, key=c.get)}"
    assert max(c, key=c.get) == MATURE, f"the largest store belongs to {max(c, key=c.get)}"
    assert len(set(c.values())) == 3, "'all three the same' must be false"
    return (f"the tabulated stores are {list(c.values())} tonnes per hectare, smallest just "
            "after cutting and burning and largest in the mature forest")


def q9(table, item):
    d = cg.cell(table, MATURE, CARBON) - cg.cell(table, BURNED, CARBON)
    assert d == 175, f"the difference recomputes to {d}, not 175"
    for wrong in (135, 180, 40, 185):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"180 minus 5 is {d:.0f} tonnes per hectare no longer held in living trees"


def _net(table, lab):
    return cg.cell(table, lab, VALUE) - cg.cell(table, lab, COST)


def q10(table, item):
    clear, sel = _net(table, "Clearcutting"), _net(table, "Cutting selected trees only")
    assert clear > sel, f"clearcutting nets {clear} against {sel}, so it is not the larger"
    assert clear != sel, "'the same amount' must be false"
    assert clear > 0 and sel > 0, "'neither returns anything' must be false"
    return (f"clearcutting nets {clear:.0f} currency units per hectare against {sel:.0f} for "
            "cutting selected trees only")


def q11(table, item):
    n = _net(table, "Clearcutting")
    assert n == 6100, f"the net return recomputes to {n}, not 6,100"
    for wrong in (1100, 7000, 5200, 7900):
        assert n != wrong, f"the {wrong} distractor equals the key"
    return f"7,000 minus 900 is {n:.0f} currency units per hectare"


def q12(table, item):
    vals = cg.col(table, LOSS)
    labs = cg.labels(table)
    assert labs[0] == BEFORE, "the first row must be the pre-harvest year"
    assert vals[1] == max(vals), f"the peak must fall in the first year after harvest; got {vals}"
    assert all(vals[i] > vals[i + 1] for i in range(1, len(vals) - 1)), \
        f"the loss must decline after the peak; got {vals}"
    assert vals[-1] > vals[0], "the last figure must still exceed the pre-harvest level"
    return (f"the record runs {vals} tonnes per square kilometer per year, peaking one year "
            "after the harvest and declining without returning to the pre-harvest figure")


def q13(table, item):
    d = cg.cell(table, YEAR1, LOSS) - cg.cell(table, BEFORE, LOSS)
    assert d == 76, f"the increase recomputes to {d}, not 76"
    for wrong in (88, 49, 13, 100):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"88 minus 12 is {d:.0f} tonnes per square kilometer per year"


def q14(table, item):
    v = dict(zip(cg.labels(table), cg.col(table, PM)))
    assert max(v, key=v.get) == MATURE, f"the largest removal belongs to {max(v, key=v.get)}"
    assert min(v, key=v.get) == "Recently clearcut ground", \
        f"the smallest removal belongs to {min(v, key=v.get)}"
    assert v["Recently clearcut ground"] < 0.2 * v[MATURE], \
        "the clearcut figure must be a small fraction of the forest figure for 'most' to hold"
    assert v["Recently clearcut ground"] < v["Young replanted stand"], \
        "'clearcut ground removes more than a young stand' must be false"
    return (f"the three sites remove {list(v.values())} kilograms per hectare per year, so "
            "clearing removes the large majority of the capacity")


def q23(table, item):
    before, eight = cg.cell(table, BEFORE, LOSS), cg.cell(table, YEAR8, LOSS)
    peak = max(cg.col(table, LOSS))
    assert eight > before, f"the eighth-year figure {eight} must exceed the pre-harvest {before}"
    assert 1.5 < eight / before < 3.0, f"the ratio {eight / before} is not 'about twice'"
    assert eight < peak, "the eighth-year figure must be below the peak"
    return (f"{eight:.0f} tonnes eight years afterward against {before:.0f} before the harvest "
            f"and a peak of {peak:.0f}")


def q28(table, item):
    r = cg.cell(table, MATURE, PM) / cg.cell(table, "Recently clearcut ground", PM)
    assert r == 21, f"the ratio recomputes to {r}, not 21"
    for wrong in (3, 42, 7, 2):
        assert r != wrong, f"the {wrong} distractor equals the key"
    return f"42 divided by 2 is {r:.0f} times as much particulate matter removed"


CLAIMS = [
 ("increased soil and stream temperatures",
  "EIN-2.B.1, near verbatim: clearcutting can be economically advantageous but leads to soil erosion, increased soil and stream temperatures, and flooding. The rejected options reverse the direction of the temperature and water effects or deny any effect."),
 ("absorb pollutants and store carbon dioxide",
  "EIN-2.B.2, near verbatim: forests contain trees that absorb pollutants and store carbon dioxide. The rejected options drop one of the two functions or reverse the direction of the exchange."),
 ("contributing to climate change",
  "EIN-2.B.2 states that the cutting and burning of trees releases carbon dioxide and contributes to climate change. None of the rejected pathways is named by the framework, and the last denies the release the statement asserts."),
 ("more sediment and produced a higher storm peak",
  "Recomputed in q4 above: 96 tonnes per square kilometer against 12, and 12 cubic meters per second against 4. EIN-2.B.1 names soil erosion and flooding among the consequences of clearcutting, and these two measurements are the field expression of each."),
 ("Eight times as much",
  "Recomputed in q5 above: 96 divided by 12. The rejected values are the storm-peak ratio and the raw sediment figures taken as ratios."),
 ("Both the soil and the stream were warmer",
  "Recomputed in q6 above: 24 degrees Celsius in the clearcut soil against 14, and 19 in its stream against 12. EIN-2.B.1 names increased soil AND stream temperatures together."),
 ("10 degrees",
  "Recomputed in q7 above: 24 minus 14 degrees Celsius in the soil, against a stream difference of 7. The rejected values are that stream difference, one reading alone, or the sum."),
 ("just after clearcutting and burning holds the least",
  "Recomputed in q8 above: 180, 45 and 5 tonnes per hectare. EIN-2.B.2 states that forests store carbon dioxide and that cutting and burning trees releases it."),
 ("175",
  "Recomputed in q9 above: 180 minus 5 tonnes per hectare. The rejected values pair the wrong parcels, quote a total alone, or add the two figures."),
 ("Clearcutting returns more",
  "Recomputed in q10 above: 6,100 currency units per hectare against 1,100 once each operation's cost is taken off. EIN-2.B.1 opens by saying clearcutting can be economically advantageous, and this is that advantage in numbers."),
 ("6,100",
  "Recomputed in q11 above: 7,000 minus 900 currency units per hectare. The rejected values are the other method's net, the gross value alone, a wrong pairing, and the sum."),
 ("rose sharply after the harvest",
  "Recomputed in q12 above: 12 tonnes before the harvest, then 88, 61 and 25 afterward, peaking in the first year and still above the pre-harvest figure in the eighth. EIN-2.B.1 names soil erosion as an effect of clearcutting."),
 ("76",
  "Recomputed in q13 above: 88 minus 12 tonnes per square kilometer per year. The rejected values quote one year alone, pair the wrong years, or add them."),
 ("removes most of the site's capacity",
  "Recomputed in q14 above: 42, 15 and 2 kilograms per hectare per year, so clearing leaves under a twentieth of the mature forest's removal. EIN-2.B.2 states that forests contain trees that absorb pollutants."),
 ("grants the economic advantage",
  "EIN-2.B.1 is built as a concession followed by a list: clearcutting CAN BE economically advantageous BUT leads to soil erosion, increased soil and stream temperatures, and flooding. The framework grants the benefit and denies that it is the whole account."),
 ("without attaching a further mechanism",
  "EIN-2.B.1 lists increased soil and stream temperatures as results of clearcutting and supplies no mechanism, so the defensible answer reports the consequence without inventing a cause. The rejected options invent one, reverse the causal order, or deny the stated effect."),
 ("and the summer temperature of the stream",
  "EIN-2.B.1 names soil erosion and increased stream temperature as two separate consequences, and sediment yield and stream temperature measure one each. The rejected pairs measure economics, forest composition or site geography instead."),
 ("already entered the atmosphere",
  "EIN-2.B.2 states that trees store carbon dioxide and that cutting and burning releases it and contributes to climate change, so the release occurs whatever is planted afterward. The rejected options contradict one half or the other of that statement."),
 ("higher peak flow",
  "EIN-2.B.1 names flooding among the consequences of clearcutting, and a larger peak flow for a storm of the same size is what flooding looks like as a measurement. Soil temperature and sediment are the framework's other effects rather than this one."),
 ("does to air quality",
  "EIN-2.B.1 gives erosion, warmer soils and streams, and flooding, all at the harvested site, while EIN-2.B.2 gives pollutant absorption, carbon storage and release. The two cover different consequences of the same act, and the framework attaches neither to a latitude."),
 ("Both soil erosion and increased stream temperature",
  "EIN-2.B.1 names soil erosion and increased stream temperatures in one sentence as effects of clearcutting, and muddier and warmer water downstream are those two effects observed. Mining wastes are EIN-2.L.1 in a different topic."),
 ("at a lower cost per unit removed",
  "EIN-2.B.1 says clearcutting CAN BE economically advantageous and then lists the harms separately, so the advantage is the yield and cost of the harvest itself. Each rejected option names one of the harms the same sentence sets against it."),
 ("still about twice its pre-harvest level",
  "Recomputed in q23 above: 25 tonnes per square kilometer per year eight years after the harvest against 12 before it and a peak of 88. EIN-2.B.1 names soil erosion without putting a limit on how long it persists."),
 ("the stream below it will run warmer",
  "EIN-2.B.1 names soil erosion and increased stream temperature together as consequences of clearcutting, so both move the same way on the cleared hillside. Every rejected option reverses at least one of the two."),
 ("would otherwise be in the atmosphere",
  "EIN-2.B.2 states that forests contain trees that absorb pollutants and store carbon dioxide, and that cutting and burning releases it, which places the standing forest on the storing side. The framework names no mineral pathway."),
 ("mass of sediment carried out of the watershed",
  "Soil erosion is the movement of soil off the site, so the measurement that captures it is the sediment carried away in the water leaving the watershed. The rejected measurements record the harvest, the economy or the regional climate."),
 ("not confined to the site",
  "EIN-2.B.1 places erosion and the temperature increases at the harvested ground and its stream, while EIN-2.B.2 ends with carbon dioxide contributing to climate change, which is not a site-scale outcome."),
 ("Twenty-one times as much",
  "Recomputed in q28 above: 42 divided by 2 kilograms per hectare per year. The rejected values come from the mature forest figure alone, from the young stand comparison, or from the clearcut figure taken as the ratio."),
 ("increases soil temperature rather than",
  "EIN-2.B.1 lists INCREASED soil and stream temperatures among the effects of clearcutting, so the direction in the student's sentence is the wrong one. The framework does address soil temperature and does not split the two temperature effects apart."),
 ("the trees were holding",
  "EIN-2.B.1 concedes the economic advantage and lists erosion, increased soil and stream temperatures and flooding, and EIN-2.B.2 adds the release of stored carbon dioxide on cutting and burning. The keyed sentence carries all five items and the concession."),
]

TABLE_CHECKS = {4: q4, 5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10, 11: q11, 12: q12,
                13: q13, 14: q14, 23: q23, 28: q28}

e_check.run(e5_2, CLAIMS, TABLE_CHECKS)
