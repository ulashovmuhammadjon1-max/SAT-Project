"""Key audit for AP ENVIRONMENTAL SCIENCE 5.5 Irrigation Methods.

One (anchor, claim) per item, in module order. The anchor must appear in the
KEYED choice and in no distractor.

WHAT THE KEYS REST ON
---------------------
EIN-2.E.1  approximately 70% of human freshwater consumption is agricultural
                                                             -- item 1
EIN-2.E.2  the types of irrigation                           -- item 2
EIN-2.F.1  waterlogging: too much water sitting in the soil raises the water
           table and inhibits oxygen uptake by roots         -- items 3, 17
EIN-2.F.2  furrow: furrows between crop rows, inexpensive, about one third lost
                                       -- items 4, 7, 8, 10, 11, 24, 29, 30
EIN-2.F.3  flood: flooding the field, about 20% lost, can lead to waterlogging
                                                             -- items 15, 28
EIN-2.F.4  spray: pumped through nozzles, more efficient than flood and furrow
           at one quarter or less, more expensive, requires energy
                                                    -- items 12, 13, 25, 30
EIN-2.F.5  drip: perforated hoses to plant roots, most efficient at about 5%,
           expensive and so not often used     -- items 5, 6, 9, 14, 26, 30
EIN-2.F.6  salinization: salts left in the soil after the water evaporates, and
           over time the soil can become toxic to plants -- items 16, 19, 20, 27
EIN-2.F.7  aquifers severely depleted by overuse for irrigation, the Ogallala
           named                                    -- items 21, 22, 23, 27

THE ONE INTERNAL TENSION, AND HOW IT IS HANDLED. EIN-2.F.4 states that spray is
MORE EFFICIENT than flood and furrow, and caps its loss at one quarter or less;
EIN-2.F.3 gives flood about 20%. A spray figure of 25% would satisfy the cap and
contradict the ranking, so every table here uses 15% for spray, which satisfies
both. The check below asserts that ordering explicitly, so a later edit that
reintroduces the contradiction fails the gate.

DATA ITEMS: 1, 6, 7, 8, 9, 10, 17, 18, 19, 20, 21, 22, 24, 25 and 29 carry
tables, recomputed below from those tables alone and anchored to named rows.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and every table in turn, and requires each
corruption to raise, BEFORE the real gate runs. The notation check also fails
on a slash fraction, which is how the framework itself writes 1/3 and 1/4 and
how this module must never write them.
"""
import e_check
import cg_check as cg
import e5_5

SHARE = "Share of human freshwater consumption worldwide (percent)"
PCT = "Water lost to evaporation and runoff (percent of the water applied)"
APPLIED = "Water applied to the field (millimeters)"
DEPTH = "Depth to water in the aquifer (meters)"
IRRIGATED = "Land irrigated from the aquifer (thousand hectares)"
SALT = "Salt in the topsoil (grams per kilogram of soil)"
YIELD = "Crop yield (tonnes per hectare)"
STANDING = "Hours per week the field stands under standing water"
WT = "Depth to the water table beneath the field (meters)"
INSTALL = "Cost to install across one hectare (currency units)"
RUNNING = "Energy needed to run the system for a season (megajoules per hectare)"

DRIP = "Drip irrigation"
FLOOD = "Flood irrigation"
SPRAY = "Spray irrigation"
FURROW = "Furrow irrigation"


def _lost(table, method):
    """Millimeters lost by one method, from the applied depth and the percentage."""
    return cg.cell(table, method, APPLIED) * cg.cell(table, method, PCT) / 100.0


def q1(table, item):
    v = dict(zip(cg.labels(table), cg.col(table, SHARE)))
    assert max(v, key=v.get) == "Agriculture", f"the largest share is {max(v, key=v.get)}"
    assert v["Agriculture"] == 70, f"agriculture reads {v['Agriculture']}, not 70"
    assert abs(sum(v.values()) - 100) < 1e-9, f"the three shares sum to {sum(v.values())}"
    assert len(set(v.values())) == 3, "'the three uses take equal shares' must be false"
    return (f"the tabulated shares are {list(v.values())} percent, summing to 100 with "
            "agriculture much the largest")


def q6(table, item):
    v = dict(zip(cg.labels(table), cg.col(table, PCT)))
    assert min(v, key=v.get) == DRIP, f"the smallest loss belongs to {min(v, key=v.get)}"
    assert v[SPRAY] < v[FLOOD] and v[SPRAY] < v[FURROW], (
        "EIN-2.F.4 makes spray more efficient than flood and furrow, so its tabulated loss "
        f"must be below both; got spray {v[SPRAY]}, flood {v[FLOOD]}, furrow {v[FURROW]}"
    )
    assert v[SPRAY] <= 25, "EIN-2.F.4 caps the spray loss at one quarter or less"
    return (f"the tabulated losses are {list(v.values())} percent, smallest for drip, with "
            "spray below both flood and furrow as the framework requires")


def q7(table, item):
    v = dict(zip(cg.labels(table), cg.col(table, PCT)))
    assert max(v, key=v.get) == FURROW, f"the largest loss belongs to {max(v, key=v.get)}"
    assert abs(v[FURROW] - 100.0 / 3.0) < 2, \
        f"the furrow loss {v[FURROW]} is not about one third"
    return f"the tabulated losses are {list(v.values())} percent, largest for furrow at {v[FURROW]:.0f}"


def q8(table, item):
    lost = _lost(table, FURROW)
    assert abs(lost - 200) <= 5, f"the furrow loss recomputes to {lost} millimeters, not about 200"
    for method, wrong in ((DRIP, 30), (FLOOD, 120), (SPRAY, 90)):
        assert abs(_lost(table, method) - wrong) <= 5, \
            f"the {method} distractor should recompute to about {wrong}"
        assert abs(_lost(table, method) - lost) > 5, f"the {method} distractor equals the key"
    return f"33 percent of 600 millimeters is {lost:.0f}, which rounds to about 200"


def q9(table, item):
    lost = _lost(table, DRIP)
    assert abs(lost - 30) <= 2, f"the drip loss recomputes to {lost} millimeters, not about 30"
    assert abs(_lost(table, FURROW) - lost) > 5, "the furrow distractor equals the key"
    assert abs(_lost(table, FLOOD) - lost) > 5, "the flood distractor equals the key"
    return f"5 percent of 600 millimeters is {lost:.0f} millimeters lost under drip irrigation"


def q10(table, item):
    d = _lost(table, FURROW) - _lost(table, DRIP)
    assert abs(d - 170) <= 5, f"the difference recomputes to {d}, not about 170"
    for wrong in (200, 30, 90, 230):
        assert abs(d - wrong) > 5, f"the {wrong} distractor equals the key"
    return (f"furrow loses {_lost(table, FURROW):.0f} millimeters and drip loses "
            f"{_lost(table, DRIP):.0f}, a difference of {d:.0f}")


def q17(table, item):
    assert cg.cell(table, "Field A", STANDING) == 0, "Field A must be the field never flooded"
    rows = sorted(zip(cg.col(table, STANDING), cg.col(table, WT), cg.col(table, YIELD)))
    assert all(rows[i][1] > rows[i + 1][1] for i in range(len(rows) - 1)), \
        f"the water table must rise toward the surface with standing water; got {rows}"
    assert all(rows[i][2] > rows[i + 1][2] for i in range(len(rows) - 1)), \
        f"the yield must fall as standing water grows; got {rows}"
    return (f"sorted by standing water the depths to the water table are {[r[1] for r in rows]} "
            f"meters and the yields are {[r[2] for r in rows]} tonnes per hectare")


def q18(table, item):
    d = cg.cell(table, "Field A", YIELD) - cg.cell(table, "Field D", YIELD)
    assert abs(d - 3.9) < 1e-9, f"the yield loss recomputes to {d}, not 3.9"
    for wrong in (1.1, 2.4, 0.9, 6.1):
        assert abs(d - wrong) > 1e-9, f"the {wrong} distractor equals the key"
    return f"5.0 minus 1.1 is {d:.1f} tonnes per hectare between the driest and wettest fields"


def q19(table, item):
    assert cg.cell(table, "None", SALT) == min(cg.col(table, SALT)), \
        "the unirrigated row must hold the least salt"
    salt = cg.col(table, SALT)
    yld = cg.col(table, YIELD)
    assert all(salt[i] < salt[i + 1] for i in range(len(salt) - 1)), f"salt must rise; got {salt}"
    assert all(yld[i] > yld[i + 1] for i in range(len(yld) - 1)), f"yield must fall; got {yld}"
    return (f"salt runs {salt} grams per kilogram while the yield runs {yld} tonnes per "
            "hectare, moving in opposite directions with no reversal")


def q20(table, item):
    d = cg.cell(table, "Fifteen", SALT) - cg.cell(table, "None", SALT)
    assert abs(d - 10.0) < 1e-9, f"the rise recomputes to {d}, not 10.0"
    for wrong in (11.0, 7.8, 4.5, 12.0):
        assert abs(d - wrong) > 1e-9, f"the {wrong} distractor equals the key"
    return f"11.0 minus 1.0 is {d:.1f} grams per kilogram of extra salt in the topsoil"


def q21(table, item):
    assert cg.cell(table, "Year 1", DEPTH) == min(cg.col(table, DEPTH)), \
        "the first year must have the shallowest water"
    d = cg.col(table, DEPTH)
    a = cg.col(table, IRRIGATED)
    assert all(d[i] < d[i + 1] for i in range(len(d) - 1)), f"depth must grow; got {d}"
    assert all(a[i] < a[i + 1] for i in range(len(a) - 1)), f"irrigated area must grow; got {a}"
    return (f"the irrigated area runs {a} thousand hectares while the depth to water runs {d} "
            "meters, both rising without a reversal")


def q22(table, item):
    d = cg.cell(table, "Year 30", DEPTH) - cg.cell(table, "Year 1", DEPTH)
    assert d == 46, f"the increase recomputes to {d}, not 46"
    for wrong in (76, 34, 18, 106):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"76 minus 30 is {d:.0f} meters of additional depth to water"


def q24(table, item):
    c = dict(zip(cg.labels(table), cg.col(table, INSTALL)))
    cheapest_two = sorted(c, key=c.get)[:2]
    assert set(cheapest_two) == {FURROW, FLOOD}, f"the two cheapest are {cheapest_two}"
    assert max(c, key=c.get) == DRIP, f"the dearest to install is {max(c, key=c.get)}"
    return (f"the installation costs are {list(c.values())} currency units per hectare, "
            "cheapest for furrow and flood and dearest for drip")


def q25(table, item):
    e = dict(zip(cg.labels(table), cg.col(table, RUNNING)))
    assert e[FURROW] == 0 and e[FLOOD] == 0, "the gravity-fed systems must need no energy"
    assert e[SPRAY] > 0 and e[DRIP] > 0, "the pressurised systems must need energy"
    return (f"the energy column reads {list(e.values())} megajoules per hectare per season, "
            "non-zero only for the two pressurised systems")


def q29(table, item):
    frac_lost = cg.cell(table, FURROW, PCT) / 100.0
    assert 0 < frac_lost < 1, f"the furrow loss fraction {frac_lost} is not a proper fraction"
    applied = 402.0 / (1 - frac_lost)
    assert abs(applied - 600) <= 6, f"the applied depth recomputes to {applied}, not about 600"
    for wrong in (402, 536, 804, 134):
        assert abs(applied - wrong) > 6, f"the {wrong} distractor equals the key"
    return (f"with {frac_lost * 100:.0f} percent lost, 402 millimeters remaining implies about "
            f"{applied:.0f} millimeters applied")


CLAIMS = [
 ("Agriculture, at about 70 percent",
  "Recomputed in q1 above: shares of 70, 19 and 11 percent summing to 100. EIN-2.E.1 states that on a global scale, approximately 70 percent of human freshwater consumption is used for agriculture."),
 ("Drip, flood, furrow, and spray",
  "EIN-2.E.2 lists drip irrigation, flood irrigation, furrow irrigation and spray irrigation. The rejected sets are STB-1.E.1's soil conservation methods, EIN-2.H.1's meat production methods, STB-1.C.1's integrated pest management methods, and STB-1.B.1's urban runoff methods."),
 ("prevents roots from taking up oxygen",
  "EIN-2.F.1, near verbatim: waterlogging occurs when too much water is left to sit in the soil, which raises the water table of groundwater and inhibits plants' ability to absorb oxygen through their roots. Salt left behind after evaporation is salinization, EIN-2.F.6."),
 ("Furrow irrigation",
  "EIN-2.F.2 states that furrow irrigation involves cutting furrows between crop rows and filling them with water. Drip uses perforated hoses, spray uses nozzles, and flooding covers the whole field."),
 ("Drip irrigation",
  "EIN-2.F.5 states that drip irrigation uses perforated hoses to release small amounts of water to plant roots. The other three are described by furrows, flooding and spray nozzles in EIN-2.F.2, EIN-2.F.3 and EIN-2.F.4."),
 ("Drip irrigation which loses the smallest",
  "Recomputed in q6 above, which also asserts that the tabulated spray loss sits below flood and furrow as EIN-2.F.4 requires. EIN-2.F.5 states that drip irrigation is the most efficient system, with only about 5 percent of water lost."),
 ("Furrow irrigation at about one third",
  "Recomputed in q7 above: the largest tabulated loss is furrow's, at about a third. EIN-2.F.2 states that about one third of the water is lost to evaporation and runoff under furrow irrigation."),
 ("About 200 millimeters",
  "Recomputed in q8 above: 33 percent of 600 millimeters. The rejected values are the same table's losses for drip, flood and spray, and the water that remains rather than the water lost."),
 ("About 30 millimeters",
  "Recomputed in q9 above: 5 percent of 600 millimeters, the figure EIN-2.F.5 attaches to drip irrigation. The rejected values double it, quote other methods, or give the water that remains."),
 ("About 170 millimeters more",
  "Recomputed in q10 above: about 200 millimeters lost under furrow against about 30 under drip. The rejected values quote one loss alone, use the spray loss, or add the two."),
 ("set against its large water loss",
  "EIN-2.F.2 states that furrow irrigation is inexpensive, BUT about one third of the water is lost to evaporation and runoff, which is a cheapness set against a loss. EIN-2.F.5 reserves the smallest loss for drip irrigation."),
 ("one quarter or less",
  "EIN-2.F.4 states that spray irrigation is more efficient than flood and furrow irrigation, with only one quarter or less of the water lost. EIN-2.F.5 gives the most efficient place to drip irrigation instead."),
 ("requires energy to run",
  "EIN-2.F.4 states that spray systems are more expensive than flood and furrow irrigation and also require energy to run. The framework attaches no field size limit to the method."),
 ("It is expensive",
  "EIN-2.F.5 states that drip irrigation is the most efficient, HOWEVER this system is expensive and so is not often used. Waterlogging belongs to flood irrigation in EIN-2.F.3."),
 ("Flood irrigation",
  "EIN-2.F.3 states that flood irrigation involves flooding an agricultural field with water, sees about 20 percent lost, and can also lead to waterlogging of the soil. EIN-2.F.1 defines waterlogging as too much water left to sit in the soil."),
 ("left in the soil after the water evaporates",
  "EIN-2.F.6, near verbatim: salinization occurs when the salts in groundwater remain in the soil after the water evaporates, and over time salinization can make soil toxic to plants. The rejected option about a raised water table restates waterlogging instead."),
 ("closer the water table lies to the surface",
  "Recomputed in q17 above: standing water of 0, 10, 30 and 60 hours per week against water table depths of 3.0, 1.2, 0.4 and 0.1 meters and yields of 5.0, 4.1, 2.6 and 1.1 tonnes per hectare. EIN-2.F.1 states that waterlogging raises the water table and inhibits oxygen uptake by roots."),
 ("3.9 tonnes per hectare",
  "Recomputed in q18 above: 5.0 minus 1.1 tonnes per hectare. The rejected values quote one yield alone, pair the wrong fields, or add the two."),
 ("while the yield fell season",
  "Recomputed in q19 above: salt of 1.0, 3.2, 6.5 and 11.0 grams per kilogram against yields of 4.0, 3.4, 2.1 and 0.8 tonnes per hectare. EIN-2.F.6 states that over time salinization can make soil toxic to plants."),
 ("10.0 grams per kilogram",
  "Recomputed in q20 above: 11.0 minus 1.0 grams per kilogram. The rejected values quote the final reading alone, pair the wrong seasons, or add the two."),
 ("had to be reached at greater depth",
  "Recomputed in q21 above: irrigated area from 400 to 900 thousand hectares while the depth to water grows from 30 to 76 meters. EIN-2.F.7 states that aquifers can be severely depleted if overused for agricultural irrigation."),
 ("46 meters",
  "Recomputed in q22 above: 76 minus 30 meters. The rejected values quote the final depth alone, pair the wrong years, or add the two."),
 ("Ogallala Aquifer",
  "EIN-2.F.7 states that aquifers can be severely depleted if overused for agricultural irrigation, as has happened to the Ogallala Aquifer in the central United States. That is the only aquifer the statement names, so it is assessable content rather than an illustrative example."),
 ("furrow and flood and the most expensive is drip",
  "Recomputed in q24 above: 300, 400, 2,100 and 4,800 currency units per hectare. EIN-2.F.2 calls furrow inexpensive, EIN-2.F.4 makes spray dearer than flood and furrow, and EIN-2.F.5 calls drip expensive and therefore not often used."),
 ("Spray and drip require energy",
  "Recomputed in q25 above: the energy column is non-zero only for the two pressurised systems. EIN-2.F.4 states that spray systems also require energy to run."),
 ("with only about 5 percent",
  "EIN-2.F.5 states that drip irrigation is the most efficient, with only about 5 percent of water lost, however this system is expensive and so is not often used. The stem removes the expense objection, leaving the efficiency claim standing."),
 ("severe depletion of an aquifer",
  "EIN-2.F.6 attaches salinization to salts left after irrigation water evaporates and EIN-2.F.7 attaches severe depletion to aquifers overused for agricultural irrigation, and neither is tied to one delivery method. The rejected pairs belong to EIN-2.D.1, EIN-2.B.2, EIN-2.G, EIN-2.B.1 and EIN-2.M."),
 ("Waterlogging raises the water table, and salinization",
  "EIN-2.F.1 makes a raised water table the mark of waterlogging and EIN-2.F.3 states that flood irrigation can lead to waterlogging; EIN-2.F.6 makes salt left behind after evaporation the mark of salinization. The rejected first option swaps the two definitions."),
 ("600 millimeters",
  "Recomputed in q29 above: with a third lost, two thirds of what is applied remains, and 402 millimeters remaining implies about 600 applied. The rejected values assume no loss, use another method's loss, or double the amount remaining."),
 ("Drip loses least, then spray",
  "EIN-2.F.5 gives drip about 5 percent, EIN-2.F.4 places spray above flood and furrow in efficiency at one quarter or less, EIN-2.F.3 gives flood about 20 percent, and EIN-2.F.2 gives furrow about one third. That is the framework's own ranking."),
]

TABLE_CHECKS = {1: q1, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10, 17: q17, 18: q18, 19: q19,
                20: q20, 21: q21, 22: q22, 24: q24, 25: q25, 29: q29}

e_check.run(e5_5, CLAIMS, TABLE_CHECKS)
