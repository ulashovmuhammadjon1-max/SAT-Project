"""Key audit for AP ENVIRONMENTAL SCIENCE 8.10 Waste Reduction Methods.

One (anchor, claim) per item, in module order; the anchor must appear in the
keyed choice and in no distractor. `cg_check.check` is the structural gate and
`es_check` carries the notation gate and the negative control.

WHAT THE KEYS REST ON
---------------------
  STB-3.M.1  recycling is a process by which certain solid waste materials are
             processed and converted into new products -- items 1, 11, 22, 26;
  STB-3.M.2  recycling reduces the current global demand on minerals but is
             energy-intensive and can be costly -- items 2, 8, 14, 28, 29;
  STB-3.M.3  composting is organic matter such as food scraps, paper and yard
             waste decomposing, its product usable as fertilizer, with odor and
             rodents as drawbacks -- items 3, 10, 12, 13, 16, 17, 23, 26;
  STB-3.M.4  e-waste can be reduced by recycling and reuse, and its heavy metals
             such as lead and mercury can leach from landfills into groundwater
             if it is not disposed of properly -- items 5, 6, 15, 20, 22, 25;
  STB-3.M.5  landfill mitigation ranges from burning waste for energy to
             restoring habitat on former landfills for use as parks -- items
             7, 18;
  STB-3.M.6  combustion of landfill decomposition gases can turn turbines and
             generate electricity, and the process reduces landfill volume --
             items 9, 19, 24.
Items 4, 21, 27 and 30 join several of them; item 27 is a NOT item whose key is
the ocean dumping of STB-3.L.4, which is a harm rather than a reduction method.

SCOPE. What solid waste is, the landfill and its components, the incineration
trade and the harms of illegal and ocean dumping are keyed in 8.9 under STB-3.K
and STB-3.L. No key here restates one of those as this topic's own content.

NOT KEYED: no recycling rate for a real place, no price, and no energy figure
presented as the framework's. The framework states none of them, so the data
items key only shares, ratios, rank orders and one rate, recomputed below.

DATA ITEMS: 4, 8, 12, 16, 20 and 24 carry tables and every keyed reading is
recomputed here from the table alone. Skill 6.B is a mathematical routine, so
items 4 and 24 ask for a computed value rather than a direction.

NEGATIVE CONTROL: `python3 verify_e8_10.py --selftest`.
"""
import sys

import cg_check as cg
import es_check as es
import e8_10

MASS = "Mass (tons)"
LANDFILLED = "If the material is landfilled"
RECYCLED = "If the material is recycled"
ADDED = "Mass added (kilograms)"
LEFT = "Mass remaining after six months (kilograms)"
ODOR = "Odor complaints filed in one year"
RODENT = "Rodent sightings reported in one year"
LEAD = "Lead in the leachate (micrograms per liter)"
MERC = "Mercury in the leachate (micrograms per liter)"
GAS = "Landfill gas collected (millions of cubic meters)"
KWH = "Electricity generated (thousands of kilowatt hours)"


def q4(table, item):
    parts = cg.labels(table)
    mass = cg.col(table, MASS)
    total = sum(mass)
    divertible = sum(m for p, m in zip(parts, mass) if not p.strip().lower().startswith("everything"))
    assert len(mass) == 3 and divertible < total, \
        f"the table does not separate a divertible share from the rest: {parts}"
    share = 100.0 * divertible / total
    options = [55, 30, 45, 70, 90]
    nearest = min(options, key=lambda o: abs(o - share))
    assert nearest == 55, f"the computed share {share:.1f} percent is not nearest 55"
    assert abs(share - 55) < 2.5, f"the computed share {share:.1f} percent is not about 55"
    return (f"the recyclable and compostable rows total {divertible:.0f} tons of "
            f"{total:.0f}, which is {share:.1f} percent")


def q8(table, item):
    rows = [str(r[0]).strip().lower() for r in table["rows"]]
    land = cg.col(table, LANDFILLED)
    recy = cg.col(table, RECYCLED)
    ore = [i for i, r in enumerate(rows) if "ore" in r][0]
    energy = [i for i, r in enumerate(rows) if "energy" in r][0]
    cost = [i for i, r in enumerate(rows) if "cost" in r][0]
    assert recy[ore] < 0.5 * land[ore], \
        f"recycling does not cut the ore required: {land[ore]} to {recy[ore]}"
    assert recy[energy] > 2 * land[energy], \
        f"recycling does not use several times the energy: {land[energy]} to {recy[energy]}"
    assert recy[cost] > 2 * land[cost], \
        f"recycling does not cost several times as much: {land[cost]} to {recy[cost]}"
    return (f"ore falls from {land[ore]:.0f} to {recy[ore]:.0f} while energy rises from "
            f"{land[energy]:.0f} to {recy[energy]:.0f} and cost from {land[cost]:.0f} to "
            f"{recy[cost]:.0f}")


def q12(table, item):
    mats = cg.labels(table)
    added = cg.col(table, ADDED)
    left = cg.col(table, LEFT)
    plastic = [i for i, m in enumerate(mats) if "plastic" in m.lower()][0]
    organic = [i for i in range(len(mats)) if i != plastic]
    assert len(organic) == 3, f"there are not three organic rows: {mats}"
    for i in organic:
        assert left[i] < 0.5 * added[i], \
            f"{mats[i]} did not lose most of its mass: {added[i]} to {left[i]}"
    assert left[plastic] == added[plastic], \
        f"the plastic row is not unchanged: {added[plastic]} to {left[plastic]}"
    fracs = [round(left[i] / added[i], 2) for i in organic]
    return (f"the three organic rows retain fractions {fracs} of their starting mass while "
            f"the plastic row retains all {left[plastic]:.0f} kilograms")


def q16(table, item):
    bands = cg.labels(table)
    odor = cg.col(table, ODOR)
    rod = cg.col(table, RODENT)
    assert all(odor[i] > odor[i + 1] for i in range(len(odor) - 1)), \
        f"odor complaints do not fall with distance in row order: {odor}"
    assert all(rod[i] > rod[i + 1] for i in range(len(rod) - 1)), \
        f"rodent reports do not fall with distance in row order: {rod}"
    assert odor[0] == max(odor) and rod[0] == max(rod), \
        "the nearest band is not the highest in both columns"
    assert min(odor) > 0 and min(rod) > 0, "'no reports at any distance' must be false"
    return (f"from {bands[0]} outward the odor counts run {odor} and the rodent counts "
            f"{rod}, both falling with distance")


def q20(table, item):
    cells = cg.labels(table)
    lead = cg.col(table, LEAD)
    merc = cg.col(table, MERC)
    got = [i for i, c in enumerate(cells)
           if "received discarded electronic devices" in c.lower()][0]
    assert lead[got] == max(lead) and merc[got] == max(merc), \
        f"the cell that received devices is not highest in both metals: {lead} {merc}"
    others = [i for i in range(len(cells)) if i != got]
    assert all(lead[got] > 3 * lead[i] for i in others), \
        f"the lead difference is not several fold: {lead}"
    assert all(merc[got] > 3 * merc[i] for i in others), \
        f"the mercury difference is not several fold: {merc}"
    return (f"{cells[got]} reads {lead[got]} lead and {merc[got]} mercury against "
            f"{[lead[i] for i in others]} and {[merc[i] for i in others]} elsewhere")


def q24(table, item):
    gas = cg.col(table, GAS)
    kwh = cg.col(table, KWH)
    rates = [k / g for g, k in zip(gas, kwh)]
    assert max(rates) - min(rates) < 0.02 * max(rates), \
        f"the rate is not the same in every row: {rates}"
    predicted = rates[0] * 10.0
    options = [22500, 2250, 9000, 45000, 180000]
    nearest = min(options, key=lambda o: abs(o - predicted) / o)
    assert nearest == 22500, \
        f"ten million cubic meters predicts {predicted:.0f}, not nearest to 22500"
    return (f"the rate is {rates[0]:.0f} thousand kilowatt hours per million cubic meters "
            f"in every row, so ten million predicts {predicted:.0f}")


CLAIMS = [
 ("processed and converted into new products",
  "STB-3.M.1 verbatim: recycling is a process by which certain solid waste materials are processed and converted into new products. Decomposition is STB-3.M.3, burning STB-3.L.2 and burial STB-3.K.2."),
 ("reduces the current global demand on minerals, but the process is energy intensive",
  "STB-3.M.2 verbatim: recycling is one way to reduce the current global demand on minerals, but this process is energy-intensive and can be costly. Odor and rodents belong to composting under STB-3.M.3."),
 ("food scraps, paper and yard waste decomposing, with odor and rodents as drawbacks",
  "STB-3.M.3 describes composting as the process of organic matter such as food scraps, paper and yard waste decomposing and names odor and rodents as its drawbacks. The rejected options describe recycling, e-waste handling, incineration and landfilling."),
 ("About 55 percent of the total",
  "Recomputed in q4 above: the recyclable and compostable rows sum to fifty-five percent of the three-row total, nearest the keyed option and within two and a half points of it. STB-3.M.1 covers the first route and STB-3.M.3 the second."),
 ("Recycling and reuse",
  "STB-3.M.4 states that e-waste can be reduced by recycling and reuse. The rejected options are disposal routes from elsewhere in the unit rather than reduction practices for electronic devices."),
 ("heavy metals such as lead and mercury that can leach from landfills into groundwater",
  "STB-3.M.4 verbatim: e-wastes may contain hazardous chemicals, including heavy metals such as lead and mercury, which can leach from landfills into groundwater if they are not disposed of properly."),
 ("From burning waste for energy to restoring habitat on former landfills",
  "STB-3.M.5 verbatim: landfill mitigation strategies range from burning waste for energy to restoring habitat on former landfills for use as parks. Ocean dumping and tire piles are the harms of STB-3.L.4 and STB-3.L.3."),
 ("cuts the ore that must be mined to a small fraction",
  "Recomputed in q8 above: the ore row falls to less than half under recycling while the energy and cost rows are more than double. That is the trade STB-3.M.2 states."),
 ("turn turbines and generate electricity, which also reduces landfill volume",
  "STB-3.M.6 verbatim: the combustion of gases produced from decomposition of organic material in landfills can be used to turn turbines and generate electricity, and this process reduces landfill volume."),
 ("As fertilizer",
  "STB-3.M.3 states that the product of the decomposition of organic matter can be used as fertilizer. Burning for electricity is STB-3.M.6 and a liner is a landfill component under STB-3.K.4."),
 ("so less new material has to be obtained",
  "STB-3.M.1 makes recycling the processing and conversion of solid waste materials into new products and STB-3.M.2 states that this reduces the current global demand on minerals, so recovered material stands in for extracted material."),
 ("three organic materials each lost most of their mass while the plastic film lost none",
  "Recomputed in q12 above: each organic row retains less than half the mass it started with while the plastic row is unchanged. STB-3.M.3 names food scraps, paper and yard waste as the organic matter that decomposes."),
 ("Food scraps, paper and yard waste",
  "STB-3.M.3 names food scraps, paper and yard waste as the organic matter composting handles. Electronic devices are STB-3.M.4 and tires STB-3.L.3."),
 ("energy intensive and potentially costly even while it reduces the demand on minerals",
  "STB-3.M.2 pairs the reduction in global mineral demand with the statement that the process is energy-intensive and can be costly, so the benefit is stated together with its price."),
 ("Heavy metals such as lead and mercury in the devices can leach into groundwater",
  "STB-3.M.4 states that e-wastes may contain heavy metals such as lead and mercury which can leach from landfills into groundwater if they are not disposed of properly, and names recycling and reuse as the reductions."),
 ("highest for the homes closest to the site and fall with distance",
  "Recomputed in q16 above: both columns fall at every step away from the site and are largest for the nearest band, and neither is zero anywhere. STB-3.M.3 names odor and rodents as composting's drawbacks."),
 ("Odor and rodents around the site",
  "STB-3.M.3 names odor and rodents as drawbacks to composting. Stack emissions are STB-3.L.2, heavy metal leaching STB-3.M.4, high energy use STB-3.M.2 and entanglement STB-3.L.4."),
 ("restoring habitat on former landfills for use as parks",
  "STB-3.M.5 states that landfill mitigation strategies range from burning waste for energy to restoring habitat on former landfills for use as parks, and a closed landfill reopened for public use is the second end of that range."),
 ("Collecting the gases produced by decomposition and burning them to turn turbines",
  "STB-3.M.6 states that the combustion of landfill decomposition gases can turn turbines and generate electricity and that the process reduces landfill volume, which is both of the outcomes named in the stem."),
 ("received discarded electronic devices carries far more lead and mercury",
  "Recomputed in q20 above: the cell that received the devices is highest in both metals by more than a factor of three over either other cell. STB-3.M.4 states that e-waste heavy metals can leach from landfills into groundwater."),
 ("Composting, paired with a product that can be used as fertilizer",
  "STB-3.M.3 gives composting a product usable as fertilizer and names odor and rodents as drawbacks, STB-3.M.2 gives the mineral and energy trade to recycling, and STB-3.M.6 has gas combustion reduce landfill volume. Each rejected pairing crosses two of those."),
 ("keeps the device in service as it is, while recycling processes materials",
  "STB-3.M.4 names recycling and reuse as two ways to reduce e-waste and STB-3.M.1 defines recycling as processing materials and converting them into new products, so reuse is the practice that does not require that conversion."),
 ("organic waste diverted from the landfill and the number of odor and rodent complaints",
  "STB-3.M.3 gives composting a usable product from diverted organic matter and names odor and rodents as its drawbacks, so those two quantities are the two sides of the trade. Fleet size, city size, landfill depth and scrap prices measure neither."),
 ("About 22,500 thousand kilowatt hours",
  "Recomputed in q24 above: the electricity divided by the gas collected is the same rate in all three rows, and that rate applied to ten million cubic meters gives the keyed figure. STB-3.M.6 states that burning landfill gas generates electricity."),
 ("carries more lead and mercury than leachate from cells filled after the devices were diverted",
  "STB-3.M.4 states that heavy metals in e-waste can leach from landfills into groundwater if the waste is not disposed of properly, so a measured leachate difference between cells with and without the devices is what bears on the claim."),
 ("broken down by decay into a material usable as fertilizer",
  "STB-3.M.3 describes composting as organic matter decomposing and gives fertilizer as the use of the product, while STB-3.M.1 reserves processing into new products for recycling."),
 ("Dumping waste into the ocean",
  "STB-3.L.4 describes ocean dumping as a practice that has produced large floating islands of trash and entangled wildlife, not as a reduction method, so it is the option this topic does not contain. The four rejected options restate STB-3.M.1, STB-3.M.3, STB-3.M.4 and STB-3.M.5."),
 ("tons of new ore required to make a product from recycled material",
  "STB-3.M.2 states that recycling is one way to reduce the current global demand on minerals, so the comparison must be of the new material each route requires. Bin counts, odor, device sales and gas volumes test other statements or none."),
 ("Recycling lowers the demand on minerals but is itself energy intensive",
  "STB-3.M.2 pairs the reduction in global mineral demand with the fact that the process is energy-intensive and can be costly. Odor and rodents belong to STB-3.M.3, and STB-3.M.6 has gas combustion reduce rather than increase landfill volume."),
 ("landfill mitigation runs from burning gas for electricity to reopening closed sites as parks",
  "Each clause of the keyed summary is one of STB-3.M.1 through STB-3.M.6. Every rejected summary denies a stated drawback, conflates two practices, recommends a practice the framework warns against, or reverses a stated outcome."),
]

TABLE_CHECKS = {4: q4, 8: q8, 12: q12, 16: q16, 20: q20, 24: q24}

es.run(e8_10, CLAIMS, TABLE_CHECKS, sys.argv)
