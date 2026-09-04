"""Key audit for AP ENVIRONMENTAL SCIENCE 9.1 Stratospheric Ozone Depletion.

One (anchor, claim) per item, in module order; the anchor must appear in the
keyed choice and in no distractor. `cg_check.check` is the structural gate and
`es_check` carries the notation gate and the negative control.

THE LAYER SWAP. This topic is DEPLETED ozone in the STRATOSPHERE, whose human
consequences STB-4.A.3 gives as skin cancer and cataracts. Topic 8.14 is
ELEVATED ozone in the TROPOSPHERE, whose consequences EIN-3.C.4 gives as
respiratory problems and lung function. Items 8, 14 and 17 carry that swap as a
distractor and each anchor below names BOTH the layer and the direction of the
change, so an anchor pinned to "ozone", to "stratosphere" or to "skin cancer"
alone cannot pass.

WHAT THE KEYS REST ON
---------------------
  STB-4.A.1  the stratospheric ozone layer is important to the evolution of life
             on Earth and the continued health and survival of life on Earth --
             items 1, 15, 28;
  STB-4.A.2  depletion is caused by anthropogenic factors such as
             chlorofluorocarbons and natural factors such as the melting of ice
             crystals in the atmosphere at the beginning of the Antarctic
             spring -- items 2, 4, 6, 9, 11, 12, 19, 20, 21, 23, 24, 27;
  STB-4.A.3  a decrease in stratospheric ozone increases the UV rays reaching
             the surface, and exposure to UV rays can lead to skin cancer and
             cataracts in humans -- items 3, 5, 7, 8, 10, 13, 14, 16, 17, 18,
             22, 25, 26.
Items 29 and 30 join all three.

SCOPE. The substitutes for CFCs are keyed in 9.2 under STB-4.B.1 and the
formation of ozone near the ground in 7.2. No key here states either.

NOT KEYED: no treaty, no year, no ozone amount called safe, and no health effect
the framework does not name.

DATA ITEMS: 3, 6, 9, 13, 17 and 21 carry tables and every keyed reading is
recomputed here from the table alone.

NEGATIVE CONTROL: `python3 verify_e9_1.py --selftest`.
"""
import sys

import cg_check as cg
import es_check as es
import e9_1

COL = "Ozone in the column above the site (Dobson units)"
UV = "Ultraviolet radiation measured at the surface (index units)"
EMIT = "Emissions of chlorofluorocarbons (thousands of tons per year)"
SPRING = "Lowest springtime ozone column measured over the pole (Dobson units)"
SEASON_COL = "Ozone column measured (Dobson units)"
UVX = "Average yearly ultraviolet exposure (index units)"
SKIN = "Skin cancer cases per hundred thousand people"
CAT = "Cataract cases per hundred thousand people"
EARLIER = "Value in the earlier record"
LATER = "Value in the later record"
SHARE = "Share of the loss attributed to it (percent)"


def q3(table, item):
    col = cg.col(table, COL)
    uv = cg.col(table, UV)
    pairs = sorted(zip(col, uv))
    assert all(pairs[i][1] > pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"ultraviolet radiation does not fall as the ozone column rises: {pairs}"
    assert uv[col.index(max(col))] == min(uv), \
        "'the largest ozone column carried the most ultraviolet' must be false"
    assert len(set(uv)) == len(uv), "'the same at every ozone value' must be false"
    return (f"sorted by ozone column the ultraviolet values run {[u for _, u in pairs]}, "
            "falling at every step as the column thickens")


def q6(table, item):
    periods = cg.labels(table)
    emit = cg.col(table, EMIT)
    ozone = cg.col(table, SPRING)
    assert all(emit[i] < emit[i + 1] for i in range(len(emit) - 1)), \
        f"the emissions do not rise across the periods in row order: {emit}"
    assert all(ozone[i] > ozone[i + 1] for i in range(len(ozone) - 1)), \
        f"the ozone column does not fall across the periods: {ozone}"
    assert ozone[emit.index(max(emit))] == min(ozone), \
        "'the largest emissions gave the largest ozone column' must be false"
    return (f"from {periods[0]} to {periods[-1]} the emissions run {emit} while the "
            f"springtime ozone column runs {ozone}, rising and falling respectively")


def q9(table, item):
    parts = cg.labels(table)
    col = cg.col(table, SEASON_COL)
    spring = [i for i, p in enumerate(parts) if p.strip().lower() == "beginning of spring"]
    assert len(spring) == 1, f"there is no single beginning of spring row: {parts}"
    s = spring[0]
    assert col[s] == min(col), f"the beginning of spring is not the minimum: {col}"
    later = [col[i] for i in range(s + 1, len(col))]
    assert later and all(v > col[s] for v in later), \
        f"the values do not rise again after the beginning of spring: {col}"
    assert len(set(col)) == len(col), "'the same throughout the year' must be false"
    return (f"the beginning of spring carries {col[s]:.0f} Dobson units, the smallest in "
            f"the record {col}, with the later rows rising again")


def q13(table, item):
    regions = cg.labels(table)
    uvx = cg.col(table, UVX)
    skin = cg.col(table, SKIN)
    cat = cg.col(table, CAT)
    order = [r for _, r in sorted(zip(uvx, regions))]
    assert order == [r for _, r in sorted(zip(skin, regions))], \
        f"skin cancer does not follow the ultraviolet order: {uvx} {skin}"
    assert order == [r for _, r in sorted(zip(cat, regions))], \
        f"cataracts do not follow the ultraviolet order: {cat}"
    hi = uvx.index(max(uvx))
    assert skin[hi] == max(skin) and cat[hi] == max(cat), \
        "the most exposed region is not the highest in both conditions"
    return (f"ranking the regions by ultraviolet exposure gives {order}, the same order as "
            "ranking them by skin cancer and by cataracts")


def q17(table, item):
    rows = [str(r[0]).strip().lower() for r in table["rows"]]
    early = cg.col(table, EARLIER)
    late = cg.col(table, LATER)
    strat = [i for i, r in enumerate(rows) if "stratosphere" in r]
    ground = [i for i, r in enumerate(rows) if "near the ground" in r]
    assert len(strat) == 1 and len(ground) == 1, \
        f"the two rows are not one stratospheric and one ground level: {rows}"
    s, g = strat[0], ground[0]
    assert late[s] < early[s], f"the stratospheric row did not fall: {early[s]} to {late[s]}"
    assert late[g] > early[g], f"the ground level row did not rise: {early[g]} to {late[g]}"
    return (f"the stratospheric column falls from {early[s]:.0f} to {late[s]:.0f} while "
            f"the ground level value rises from {early[g]:.0f} to {late[g]:.0f}, opposite "
            "directions in different layers")


def q21(table, item):
    contribs = [str(c).strip().lower() for c in cg.labels(table)]
    share = cg.col(table, SHARE)
    human = [i for i, c in enumerate(contribs) if "chlorofluorocarbons" in c]
    natural = [i for i, c in enumerate(contribs) if "ice crystals" in c]
    assert len(human) == 1 and len(natural) == 1, \
        f"the two contributions named by STB-4.A.2 are not both present: {contribs}"
    assert share[human[0]] > 0 and share[natural[0]] > 0, \
        f"one contribution carries no share: {share}"
    assert abs(sum(share) - 100) < 1e-6, f"the shares do not sum to the whole loss: {share}"
    assert min(share) > 50 * 0 and sum(share) > 50, "the two together must exceed half the loss"
    return (f"the human released contribution is {share[human[0]]:.0f} percent and the "
            f"natural polar contribution {share[natural[0]]:.0f} percent, together the "
            "whole loss")


CLAIMS = [
 ("important to the evolution of life on Earth and to the continued health and survival",
  "STB-4.A.1 verbatim in substance: the stratospheric ozone layer is important to the evolution of life on Earth and the continued health and survival of life on Earth. Breathable oxygen, the surface temperature, heat transport and rainfall belong to other statements."),
 ("Chlorofluorocarbons",
  "STB-4.A.2 names chlorofluorocarbons as its example of an anthropogenic factor causing stratospheric ozone depletion. Fertilizer, asbestos, sewage and waste heat are unit 8 pollutants and are not named here."),
 ("less ozone in the column above the site, the more ultraviolet radiation reached the surface",
  "Recomputed in q3 above: ordering the rows by ozone column gives the reverse of the order by ultraviolet at the surface. STB-4.A.3 states that a decrease in stratospheric ozone increases the ultraviolet rays that reach the surface."),
 ("melting of ice crystals in the atmosphere at the beginning of the Antarctic spring",
  "STB-4.A.2 names that melting as its example of a natural factor. Eruptions, migration, decay and evaporation appear nowhere in this statement."),
 ("increases the ultraviolet rays that reach the surface of the Earth",
  "STB-4.A.3 states that a decrease in stratospheric ozone increases the UV rays that reach the Earth's surface. Each rejected option reverses that, substitutes another quantity, or denies the effect."),
 ("emissions of chlorofluorocarbons rose across the periods, the lowest springtime ozone column fell",
  "Recomputed in q6 above: the emissions column rises at every step in row order while the springtime ozone column falls at every step. STB-4.A.2 names chlorofluorocarbons as an anthropogenic cause of the depletion."),
 ("Skin cancer and cataracts",
  "STB-4.A.3 states that exposure to UV rays can lead to skin cancer and cataracts in humans. Respiratory effects belong to elevated tropospheric ozone under EIN-3.C.4."),
 ("stratosphere, high above the ground, where the ozone is being depleted",
  "STB-4.A.2 and STB-4.A.3 concern depletion of ozone in the stratosphere, while EIN-3.C.4 concerns elevated ozone in the troposphere near the ground. The distractors vary the layer and the direction independently, so the anchor carries both."),
 ("smallest ozone column of the year was measured at the beginning of spring",
  "Recomputed in q9 above: the beginning of spring row is the minimum and the later rows rise again. STB-4.A.2 names processes involving ice crystals in the atmosphere at the beginning of the Antarctic spring among the factors in depletion."),
 ("stands between the Sun and the surface",
  "STB-4.A.3 states that a decrease in stratospheric ozone increases the ultraviolet rays reaching the surface, which places the layer between the source and the ground. The framework makes it neither a source of those rays nor a reflector of heat."),
 ("Sediment washed into rivers from bare farmland",
  "STB-4.A.2 names anthropogenic factors such as chlorofluorocarbons and natural factors such as the melting of ice crystals at the beginning of the Antarctic spring, so sediment, which is STB-3.B.9, is the one option with no role here."),
 ("caused by anthropogenic factors, such as chlorofluorocarbons",
  "STB-4.A.2 identifies chlorofluorocarbons as an anthropogenic cause, so removing them addresses a stated cause. The rejected statements describe why the layer matters, what a decrease does, and what the exposure can lead to."),
 ("highest ultraviolet exposure carries the highest rates of both conditions",
  "Recomputed in q13 above: ranking the regions by ultraviolet exposure gives the same order as ranking them by skin cancer and by cataracts. STB-4.A.3 attaches both conditions to ultraviolet exposure."),
 ("stratosphere is linked to skin cancer and cataracts, while breathing problems are linked to elevated ozone near the ground",
  "STB-4.A.3 attaches skin cancer and cataracts to the increased ultraviolet rays that follow a decrease in stratospheric ozone, while EIN-3.C.4 attaches respiratory problems to elevated tropospheric ozone, so the anchor names both halves of the contrast."),
 ("mattered while life was developing and it continues to matter to life living now",
  "STB-4.A.1 states that the layer is important to the evolution of life on Earth and the continued health and survival of life on Earth, which covers both the past and the present."),
 ("amount of ozone in the column of atmosphere above that site",
  "STB-4.A.2 and STB-4.A.3 concern ozone in the stratosphere, so the overhead column is what shows its depletion. Ozone measured in breathing air is the tropospheric ozone of EIN-3.C.4."),
 ("ozone high in the stratosphere fell while the ozone near the ground rose",
  "Recomputed in q17 above: the stratospheric row falls between the two records and the ground level row rises. STB-4.A.3 concerns a decrease in the stratosphere and EIN-3.C.4 elevated levels near the ground, so the anchor names both layers and both directions."),
 ("overhead ozone column and the ultraviolet radiation at the surface at the same site",
  "STB-4.A.3 links two quantities, so both must be measured together and allowed to vary. Ground level ozone belongs to a different statement entirely."),
 ("ice crystals in the atmosphere melt, which is the natural factor it names",
  "STB-4.A.2 names the melting of ice crystals in the atmosphere at the beginning of the Antarctic spring as its natural factor, so the timing belongs to that process rather than to manufacturing or sunlight."),
 ("Chlorofluorocarbons, paired with the anthropogenic factors",
  "STB-4.A.2 gives chlorofluorocarbons as an example of an anthropogenic factor and the melting of ice crystals as an example of a natural factor, so the framework does divide the causes into two categories."),
 ("Both a contribution from chemicals people released and a contribution from a natural polar process",
  "Recomputed in q21 above: both rows carry a positive share and the two shares sum to the whole loss. STB-4.A.2 names an anthropogenic and a natural factor together."),
 ("higher measured ultraviolet exposure show higher rates of cataracts",
  "STB-4.A.3 states that exposure to UV rays can lead to skin cancer and cataracts in humans, so comparing exposure against the rate of the condition tests it. Elevation, reporting and measurability do not."),
 ("Both kinds of factor contribute to the depletion it describes",
  "STB-4.A.2 gives an example of each kind, which places both within the stated cause of stratospheric ozone depletion. Nothing in the framework subordinates one to the other."),
 ("Chemicals released by human activity that the framework identifies as an anthropogenic cause",
  "STB-4.A.2 names chlorofluorocarbons as an example of the anthropogenic factors causing stratospheric ozone depletion, so they are of human origin rather than natural, mineral, biological or geologic."),
 ("increases the ultraviolet rays reaching the surface, and exposure to those rays can lead to cataracts",
  "STB-4.A.3 joins the increase in ultraviolet rays that follows a decrease in stratospheric ozone to skin cancer and cataracts in humans, which is the chain the report describes."),
 ("Less ultraviolet radiation should reach the surface as the ozone column recovers",
  "STB-4.A.3 states that a decrease in stratospheric ozone increases the ultraviolet rays reaching the surface, so a recovery works in the opposite direction. The framework attaches no temperature or ground level consequence to the column."),
 ("caused only by natural processes",
  "STB-4.A.2 names anthropogenic factors such as chlorofluorocarbons alongside natural factors, so attributing the depletion to natural processes alone contradicts it. The four rejected claims restate STB-4.A.1 to STB-4.A.3."),
 ("continued health and survival of life on Earth, and names skin cancer and cataracts as effects in humans",
  "STB-4.A.1 speaks of life on Earth while STB-4.A.3 names skin cancer and cataracts in humans, so the framework makes a general claim and a specific human one together."),
 ("depleted, more ultraviolet radiation reaches the surface, and exposure to those rays can lead to skin cancer",
  "STB-4.A.2 supplies the depletion and its causes and STB-4.A.3 supplies the increase in ultraviolet rays and the health effects that can follow, in that order. Each rejected sequence reverses the order or the direction."),
 ("depleted by human released chlorofluorocarbons and by a natural polar process",
  "Each clause of the keyed summary is one of STB-4.A.1, STB-4.A.2 and STB-4.A.3. Every rejected summary moves the ozone to the wrong layer, denies a stated cause or effect, reverses the ultraviolet change, or drops the claim about life living now."),
]

TABLE_CHECKS = {3: q3, 6: q6, 9: q9, 13: q13, 17: q17, 21: q21}

es.run(e9_1, CLAIMS, TABLE_CHECKS, sys.argv)
