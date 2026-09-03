"""Key audit for AP ENVIRONMENTAL SCIENCE 5.7 Meat Production Methods.

One (anchor, claim) per item, in module order. The anchor must appear in the
KEYED choice and in no distractor.

WHAT THE KEYS REST ON
---------------------
EIN-2.H.1  feedlots and CAFOs, plus pasture-based systems such as rotational
           and free-range grazing                            -- item 1
EIN-2.I.1  more land, water and energy per gram of protein than plant-based
           food; more nutrient pollution and greenhouse gases such as methane;
           impacts VARY by livestock type and practice   -- items 2, 3, 4, 5, 6
EIN-2.I.2  CAFOs more economically efficient and cheaper for consumers;
           confined spaces and grain- and soy-based diets; high manure
           concentrations that CAN contaminate waterways IF NOT PROPERLY
           MANAGED; routine antibiotics and global resistance risk
                                        -- items 7, 8, 9, 10, 11, 12, 14
EIN-2.I.3  pasture systems: grass or forage for most of life; rotational
           grazing improves sustainability; manure delivers nutrients BUT
           runoff and erosion risks remain IF ANIMAL DENSITY IS HIGH; more land
           and higher consumer costs; NOT ALL free-range systems are
           antibiotic-free                     -- items 13, 14, 15, 16, 17
EIN-2.I.4  overgrazing: livestock exceeding the land's capacity to regenerate
           vegetation; reduced plant cover, soil erosion and compaction, all
           reducing fertility; reduced biodiversity and lowered carbon storage;
           rotational grazing prevents or minimises
                                        -- items 18, 19, 20, 21, 22, 23, 24
EIN-2.I.5  overgrazing can lead to desertification in arid and semi-arid
           regions; restoration, soil conservation and improved grazing can
           slow or reverse it                                -- item 25
EIN-2.I.6  less meat, especially ruminant, lowers carbon dioxide, methane and
           nitrous oxide emissions, conserves fresh water and reduces reliance
           on antibiotics and growth hormones; feed quality and precision
           farming also mitigate; MAGNITUDE depends on production methods and
           on how released land is managed  -- items 26, 27, 28, 29, 30

THREE HEDGES THE FRAMEWORK MAKES AND THIS MODULE KEEPS: impacts vary by
livestock type (item 5), not all free-range systems are antibiotic-free (item
16), and the magnitude of dietary benefits depends on production methods and on
how released land is managed (item 29). Flattening any of the three would make
a key say more than the CED does.

DATA ITEMS: 2, 3, 5, 6, 10, 11, 14, 15, 21, 22, 23, 24 and 27 carry tables,
recomputed below from those tables alone and anchored to named rows.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and every table in turn, and requires each
corruption to raise, BEFORE the real gate runs.
"""
import e_check
import cg_check as cg
import e5_7

LAND_P = "Land used per gram of protein (square meters)"
WATER_P = "Water used per gram of protein (litres)"
ENERGY_P = "Energy used per gram of protein (kilojoules)"
CH4 = "Methane released per kilogram of meat produced (grams)"
LAND_A = "Land needed per animal (hectares)"
PRICE = "Price to the consumer per kilogram of meat (currency units)"
COVER3 = "Plant cover remaining after three seasons (percent of the ground)"
SOIL = "Soil lost in the third season (tonnes per hectare)"
COVER5 = "Plant cover after five seasons (percent of the ground)"
SPECIES = "Number of plant species recorded"
NITRATE = "Nitrate in the stream (milligrams per litre)"
WATER_SAVED = "Freshwater saved (thousand litres)"
GHG_SAVED = "Greenhouse gas emissions avoided (kilograms)"

CAFO = "Concentrated animal feeding operation"
PASTURE = "Free-range pasture system"
UPSTREAM = "Upstream of the animal operation"
STORAGE = "Beside the manure storage"
DOWNSTREAM = "Two kilometers downstream"
ONE_PASTURE = "Animals left on one pasture all season"
ROTATED = "Animals rotated between four pastures"


def q2(table, item):
    for header in (LAND_P, WATER_P, ENERGY_P):
        v = dict(zip(cg.labels(table), cg.col(table, header)))
        assert min(v, key=v.get) == "Beans", \
            f"the plant food must be the smallest on {header}; smallest is {min(v, key=v.get)}"
        assert v["Beef"] > v["Beans"] and v["Pork"] > v["Beans"], \
            f"both meats must exceed the plant food on {header}"
    return ("beans hold the smallest value in all three columns, 0.1 square meters, 0.2 litres "
            "and 20 kilojoules per gram of protein")


def q3(table, item):
    base = cg.cell(table, "Beans", LAND_P)
    assert base > 0, "the plant land requirement must be non-zero for a ratio to exist"
    r = cg.cell(table, "Beef", LAND_P) / base
    assert abs(r - 16) < 1e-9, f"the land ratio recomputes to {r}, not 16"
    for wrong in (4, 11, 2, 1):
        assert abs(r - wrong) > 1e-9, f"the {wrong} distractor equals the key"
    return f"1.6 divided by 0.1 is {r:.0f} times as much land per gram of protein"


def q5(table, item):
    v = dict(zip(cg.labels(table), cg.col(table, CH4)))
    assert max(v, key=v.get) == "Cattle", f"the largest release is {max(v, key=v.get)}"
    assert min(v, key=v.get) == "Poultry", f"the smallest release is {min(v, key=v.get)}"
    assert len(set(v.values())) == len(v), "'the same for every livestock' must be false"
    assert min(v.values()) > 0, "'only poultry releases methane' must be false"
    return (f"the four kinds of livestock release {list(v.values())} grams per kilogram, a "
            "range of nearly thirty to one")


def q6(table, item):
    base = cg.cell(table, "Poultry", CH4)
    assert base > 0, "the poultry figure must be non-zero for a ratio to exist"
    r = cg.cell(table, "Cattle", CH4) / base
    assert r == 29, f"the ratio recomputes to {r}, not 29"
    for wrong in (7, 23, 4, 1):
        assert r != wrong, f"the {wrong} distractor equals the key"
    return f"290 divided by 10 is {r:.0f} times as much methane per kilogram of meat"


def q10(table, item):
    up = cg.cell(table, UPSTREAM, NITRATE)
    at = cg.cell(table, STORAGE, NITRATE)
    down = cg.cell(table, DOWNSTREAM, NITRATE)
    assert at > up, f"the reading beside the storage {at} must exceed the upstream {up}"
    assert down > up, f"the downstream reading {down} must remain above the upstream {up}"
    assert down < at, "the downstream reading should be below the peak beside the storage"
    assert up == min(up, at, down), "'the source lies upstream' must be false"
    return (f"the three points read {up}, {at} and {down} milligrams per litre, so the water "
            "gains nitrate at the operation and is still carrying much of it downstream")


def q11(table, item):
    d = cg.cell(table, STORAGE, NITRATE) - cg.cell(table, UPSTREAM, NITRATE)
    assert abs(d - 9.2) < 1e-9, f"the rise recomputes to {d}, not 9.2"
    for wrong in (9.8, 4.8, 4.4, 10.4):
        assert abs(d - wrong) > 1e-9, f"the {wrong} distractor equals the key"
    return f"9.8 minus 0.6 is {d:.1f} milligrams per litre"


def q14(table, item):
    assert cg.cell(table, PASTURE, LAND_A) > cg.cell(table, CAFO, LAND_A), \
        "the pasture system must need the greater land per animal"
    assert cg.cell(table, PASTURE, PRICE) > cg.cell(table, CAFO, PRICE), \
        "the pasture system's meat must cost the consumer more"
    return (f"the pasture system reads {cg.cell(table, PASTURE, LAND_A)} hectares per animal "
            f"against {cg.cell(table, CAFO, LAND_A)}, and "
            f"{cg.cell(table, PASTURE, PRICE):.0f} currency units per kilogram against "
            f"{cg.cell(table, CAFO, PRICE):.0f}")


def q15(table, item):
    base = cg.cell(table, CAFO, LAND_A)
    assert base > 0, "the confined system's land requirement must be non-zero for a ratio"
    r = cg.cell(table, PASTURE, LAND_A) / base
    assert abs(r - 45) < 1e-9, f"the land ratio recomputes to {r}, not 45"
    for wrong in (2, 90, 20, 1):
        assert abs(r - wrong) > 1e-9, f"the {wrong} distractor equals the key"
    return f"0.90 divided by 0.02 is {r:.0f} times as much land per animal"


def q21(table, item):
    cover = cg.col(table, COVER3)
    soil = cg.col(table, SOIL)
    assert cg.cell(table, "1", COVER3) == max(cover), \
        "the lightest stocking rate must keep the most plant cover"
    assert all(cover[i] > cover[i + 1] for i in range(len(cover) - 1)), \
        f"plant cover must fall as stocking rises; got {cover}"
    assert all(soil[i] < soil[i + 1] for i in range(len(soil) - 1)), \
        f"soil loss must rise as stocking rises; got {soil}"
    return (f"plant cover runs {cover} percent while soil lost runs {soil} tonnes per hectare "
            "as the stocking rate rises")


def q22(table, item):
    d = cg.cell(table, "10", SOIL) - cg.cell(table, "1", SOIL)
    assert d == 30, f"the difference recomputes to {d}, not 30"
    for wrong in (31, 27, 18, 32):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"31 minus 1 is {d:.0f} tonnes per hectare more soil lost at the highest stocking rate"


def q23(table, item):
    assert cg.cell(table, ROTATED, COVER5) > cg.cell(table, ONE_PASTURE, COVER5), \
        "the rotated area must keep the greater plant cover"
    assert cg.cell(table, ROTATED, SPECIES) > cg.cell(table, ONE_PASTURE, SPECIES), \
        "the rotated area must carry the greater number of species"
    return (f"the rotated area reads {cg.cell(table, ROTATED, COVER5):.0f} percent cover and "
            f"{cg.cell(table, ROTATED, SPECIES):.0f} species against "
            f"{cg.cell(table, ONE_PASTURE, COVER5):.0f} percent and "
            f"{cg.cell(table, ONE_PASTURE, SPECIES):.0f} species")


def q24(table, item):
    d = cg.cell(table, ROTATED, SPECIES) - cg.cell(table, ONE_PASTURE, SPECIES)
    assert d == 13, f"the difference recomputes to {d}, not 13"
    for wrong in (19, 6, 25, 43):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"19 minus 6 is {d:.0f} more plant species where the animals were rotated"


def q27(table, item):
    w = cg.col(table, WATER_SAVED)
    g = cg.col(table, GHG_SAVED)
    assert cg.cell(table, "No change", WATER_SAVED) == 0, "the control row must save nothing"
    assert all(w[i] < w[i + 1] for i in range(len(w) - 1)), f"water saved must rise; got {w}"
    assert all(g[i] < g[i + 1] for i in range(len(g) - 1)), f"emissions avoided must rise; got {g}"
    return (f"water saved runs {w} thousand litres and emissions avoided run {g} kilograms as "
            "more of the beef is replaced")


CLAIMS = [
 ("Feedlots and concentrated animal feeding operations",
  "EIN-2.H.1 states that methods of meat production include feedlots and concentrated animal feeding operations, as well as pasture-based systems such as rotational grazing and free-range grazing. The rejected sets are EIN-2.E.2's irrigation types, STB-1.E.1's conservation methods, STB-1.C.1's IPM methods and STB-1.G's forestry methods."),
 ("takes more land, water and energy per gram of protein",
  "Recomputed in q2 above: the plant food holds the smallest value in all three columns. EIN-2.I.1 states that meat production requires more land, water, and energy per gram of protein produced than the production of plant-based foods."),
 ("Sixteen times as much",
  "Recomputed in q3 above: 1.6 divided by 0.1 square meters per gram of protein. The rejected values come from the pork comparison, from the water column, or from denying the two differ."),
 ("Increased nutrient pollution and increased emissions",
  "EIN-2.I.1 states that meat production increases nutrient pollution and emissions of greenhouse gases, such as methane. Each rejected option reverses one or both directions."),
 ("varies by the type of livestock raised",
  "Recomputed in q5 above: releases of 290, 230, 40 and 10 grams per kilogram across four kinds of livestock. EIN-2.I.1 ends by stating that the environmental impacts of meat production VARY by the type of livestock raised and production practices used."),
 ("Twenty-nine times as much",
  "Recomputed in q6 above: 290 divided by 10 grams per kilogram. The rejected values come from other pairs in the same table."),
 ("more economically efficient, which lowers costs",
  "EIN-2.I.2 states that CAFOs can be more economically efficient, which lowers costs for consumers. The same statement puts these animals on grain- and soy-based diets, so the grass condition offered elsewhere is not the framework's claim."),
 ("confined spaces and fed grain- and soy-based diets",
  "EIN-2.I.2 states that animals raised in CAFOs are kept in confined spaces and fed grain- and soy-based diets. Feeding on grass or forage for most of life is EIN-2.I.3's description of pasture systems."),
 ("if it is not properly managed",
  "EIN-2.I.2 states that CAFOs have high concentrations of manure that CAN contaminate nearby waterways IF NOT PROPERLY MANAGED, which is a conditional rather than an inevitability. EIN-2.I.3 also discusses manure on pasture."),
 ("consistent with manure reaching the water",
  "Recomputed in q10 above: 0.6, 9.8 and 5.4 milligrams per litre from upstream past the storage to downstream. EIN-2.I.2 states that high concentrations of manure can contaminate nearby waterways if not properly managed."),
 ("9.2 milligrams per litre",
  "Recomputed in q11 above: 9.8 minus 0.6 milligrams per litre. The rejected values quote the peak alone, pair the wrong points, or add the two."),
 ("global risks of antibiotic resistance",
  "EIN-2.I.2 states that routine use of antibiotics in CAFOs can contribute to the global risks of antibiotic resistance. Loss of crop genetic diversity is EIN-2.G.2 and a rising water table is EIN-2.F.1."),
 ("Grass or forage for most of their lives",
  "EIN-2.I.3 states that free-range or pasture-based grazing systems allow animals to feed on grass or forage for most of their lives. Grain- and soy-based diets belong to CAFOs in EIN-2.I.2."),
 ("far more land per animal and its meat costs the consumer more",
  "Recomputed in q14 above: 0.90 hectares per animal against 0.02, and 14 currency units per kilogram against 6. EIN-2.I.3 states that pasture systems require more land, leading to higher consumer costs, and EIN-2.I.2 makes CAFOs cheaper for consumers."),
 ("Forty-five times as much",
  "Recomputed in q15 above: 0.90 divided by 0.02 hectares per animal. The rejected values come from the price column or from misplacing a decimal."),
 ("not all free-range systems are antibiotic-free",
  "EIN-2.I.3 ends with exactly that sentence, which denies the guarantee without asserting the opposite. The framework attaches routine antibiotic use to CAFOs in EIN-2.I.2 but does not rank the two systems on antibiotic use."),
 ("but runoff and erosion risks remain if animal density is high",
  "EIN-2.I.3 states that manure delivers nutrients to pasture soils, BUT runoff and erosion risks remain IF ANIMAL DENSITY IS HIGH. The framework grants the benefit and makes the risk conditional on density."),
 ("exceeding the land's capacity to regenerate vegetation",
  "EIN-2.I.4, near verbatim: overgrazing occurs when the livestock population exceeds the land's capacity to regenerate vegetation. Rotation between pastures is what the same statement offers to prevent it."),
 ("all of which reduce soil fertility",
  "EIN-2.I.4 states that overgrazing results in reduced plant cover, soil erosion, and soil compaction, ALL OF WHICH REDUCE SOIL FERTILITY. Each rejected option reverses at least one result or the fertility outcome."),
 ("reduces biodiversity and lowers carbon storage",
  "EIN-2.I.4 states that overgrazing also reduces biodiversity and lowers carbon storage. Each rejected option reverses one or both directions."),
 ("plant cover remaining fell and the soil lost rose",
  "Recomputed in q21 above: plant cover of 88, 71, 42 and 19 percent against soil losses of 1, 4, 13 and 31 tonnes per hectare. EIN-2.I.4 states that overgrazing results in reduced plant cover and soil erosion."),
 ("30 tonnes per hectare more",
  "Recomputed in q22 above: 31 minus 1 tonnes per hectare. The rejected values quote the highest loss alone, pair the wrong rates, or add the two."),
 ("more plant cover and more plant species",
  "Recomputed in q23 above: 77 percent cover and 19 species against 34 percent and 6 species with animal numbers held equal. EIN-2.I.4 states that rotational grazing can help prevent or minimize the impacts of overgrazing, which include reduced plant cover and reduced biodiversity."),
 ("13 more species",
  "Recomputed in q24 above: 19 minus 6 plant species. The rejected values quote one count alone, add the two, or take the difference from the plant cover column."),
 ("Desertification, which restoration efforts",
  "EIN-2.I.5 states that overgrazing can lead to desertification in arid and semi-arid regions, and that restoration efforts, soil conservation measures and improved grazing practices can help slow or reverse the process. Waterlogging and salinization are EIN-2.F.1 and EIN-2.F.6."),
 ("Ruminant livestock such as cattle and sheep",
  "EIN-2.I.6 states that less consumption of meat, ESPECIALLY FROM RUMINANT LIVESTOCK SUCH AS CATTLE AND SHEEP, can lower emissions of carbon dioxide, methane and nitrous oxide. The framework does name a category."),
 ("saved more fresh water and avoided more greenhouse",
  "Recomputed in q27 above: 0, 160 and 320 thousand litres saved and 0, 310 and 620 kilograms of emissions avoided as more beef is replaced. EIN-2.I.6 states that less meat consumption can lower those emissions and conserve freshwater resources."),
 ("reliance on antibiotics and growth hormones",
  "EIN-2.I.6 states that less meat consumption can lower emissions, conserve freshwater resources, AND reduce reliance on antibiotics and growth hormones. The framework does name that third benefit."),
 ("how land no longer used for livestock is subsequently managed",
  "EIN-2.I.6 ends by stating that the magnitude of these benefits depends on the production methods applied and how land no longer used for livestock is subsequently managed. That hedge is the framework's own and is not dropped here."),
 ("feed quality and the use of precision farming",
  "EIN-2.I.6 states that advances in feed quality and the use of precision farming technologies can also mitigate environmental impacts. Raising the stocking rate is what EIN-2.I.4 defines as the route to overgrazing."),
]

TABLE_CHECKS = {2: q2, 3: q3, 5: q5, 6: q6, 10: q10, 11: q11, 14: q14, 15: q15,
                21: q21, 22: q22, 23: q23, 24: q24, 27: q27}

e_check.run(e5_7, CLAIMS, TABLE_CHECKS)
