"""Key audit for AP ENVIRONMENTAL SCIENCE 8.11 Sewage Treatment.

One (anchor, claim) per item, in module order; the anchor must appear in the
keyed choice and in no distractor. `cg_check.check` is the structural gate and
`es_check` carries the notation gate and the negative control.

WHAT THE KEYS REST ON
---------------------
  STB-3.N.1  primary treatment is the physical removal of large objects, often
             with screens and grates, followed by the settling of solid waste in
             the bottom of a tank -- items 1, 8, 10, 13, 22;
  STB-3.N.2  secondary treatment is a biological process in which bacteria break
             organic matter into carbon dioxide and inorganic sludge, in a tank
             aerated to increase the rate -- items 2, 6, 7, 12, 14, 18, 23, 25,
             26, 27;
  STB-3.N.3  tertiary treatment is the use of ecological or chemical processes
             to remove any pollutants left after primary and secondary treatment
             -- items 3, 15, 16, 24, 29;
  STB-3.N.4  prior to discharge the treated water is exposed to one or more
             disinfectants, usually chlorine, ozone or UV light, to kill
             bacteria -- items 4, 5, 11, 17, 19, 20, 28.
Items 9, 21 and 30 join all four.

SCOPE. Eutrophication and wastewater release as its cause are keyed in 8.5
under STB-3.F, and dysentery from untreated sewage in 8.14 under EIN-3.C.2. No
key here restates either.

NOT KEYED: no residence time, no discharge limit, no disinfectant dose and no
named plant. The framework states none of them, so the data items key only
directions, rank orders and shares recomputed below.

DATA ITEMS: 4, 8, 12, 16, 20 and 24 carry tables and every keyed reading is
recomputed here from the table alone. Suggested skill 2.A concerns a process
represented visually; the bank carries no images, so each representation is a
table and no stem refers to a diagram.

NEGATIVE CONTROL: `python3 verify_e8_11.py --selftest`.
"""
import sys

import cg_check as cg
import es_check as es
import e8_11

SOLIDS = "Suspended solids (milligrams per liter)"
BOD = "Organic matter measured as oxygen demand (milligrams per liter)"
BACT = "Bacteria (colonies per hundred milliliters)"
REMOVED = "Mass taken out by the screens, grates and settling tank (kilograms)"
REMAIN = "Mass still in the water after primary treatment (kilograms)"
AIR = "Air pumped into the tank (cubic meters per hour)"
BROKEN = "Organic matter broken down in eight hours (percent)"
AFTER2 = "Concentration after secondary treatment (milligrams per liter)"
AFTER3 = "Concentration after tertiary treatment (milligrams per liter)"
BEFORE_D = "Bacteria before the step (colonies per hundred milliliters)"
AFTER_D = "Bacteria after the step (colonies per hundred milliliters)"
STAGES = "Number of treatment stages used before discharge"
NITRO = "Nitrogen remaining in the discharge (milligrams per liter)"

NAMED_DISINFECTANTS = {"chlorine", "ozone", "ultraviolet light"}


def q4(table, item):
    points = cg.labels(table)
    solids = cg.col(table, SOLIDS)
    bod = cg.col(table, BOD)
    bact = cg.col(table, BACT)
    last = len(points) - 1
    assert "disinfection" in points[last].lower(), \
        f"the last row is not the disinfection step: {points[last]}"
    assert solids[0] == max(solids) and bod[0] == max(bod), \
        "the raw sewage row is not the highest in solids and organic matter"
    assert solids[last] < 0.1 * solids[0] and bod[last] < 0.1 * bod[0], \
        f"solids and organic matter do not fall sharply: {solids} {bod}"
    assert min(bact[:last]) > 0.1 * bact[0], \
        f"the bacteria count already collapses before the last step: {bact}"
    assert bact[last] < 0.001 * bact[last - 1], \
        f"the bacteria count does not collapse at the last step: {bact}"
    assert bact[1] > 0.5 * bact[0], \
        "'the bacteria collapse during primary treatment' must be false"
    return (f"solids run {solids} and organic matter {bod}, both falling early, while the "
            f"bacteria run {bact} and only collapse at {points[last]}")


def q8(table, item):
    mats = cg.labels(table)
    out = cg.col(table, REMOVED)
    left = cg.col(table, REMAIN)
    diss = [i for i, m in enumerate(mats) if "dissolved" in m.lower()][0]
    solid = [i for i in range(len(mats)) if i != diss]
    assert len(solid) == 2, f"there are not two solid material rows: {mats}"
    for i in solid:
        assert out[i] > 10 * left[i], \
            f"{mats[i]} was not almost entirely removed: {out[i]} out, {left[i]} left"
    assert out[diss] == 0 and left[diss] > 0, \
        f"the dissolved organic matter row is not left untouched: {out[diss]} {left[diss]}"
    return (f"the two solid rows were removed at {[out[i] for i in solid]} kilograms "
            f"against {[left[i] for i in solid]} left, while the dissolved organic matter "
            f"had {out[diss]:.0f} removed and {left[diss]:.0f} remaining")


def q12(table, item):
    tanks = cg.labels(table)
    air = cg.col(table, AIR)
    broken = cg.col(table, BROKEN)
    order = [t for _, t in sorted(zip(air, tanks))]
    assert order == [t for _, t in sorted(zip(broken, tanks))], \
        f"the order by air does not match the order by breakdown: {air} {broken}"
    assert broken[air.index(min(air))] == min(broken), \
        "'the tank with no air broke down the largest share' must be false"
    assert len(set(broken)) == len(broken), "'all three the same' must be false"
    return (f"ranking the tanks by air supplied gives {order}, the same order as ranking "
            "them by the share of organic matter broken down")


def q16(table, item):
    subs = cg.labels(table)
    a2 = cg.col(table, AFTER2)
    a3 = cg.col(table, AFTER3)
    for s, x, y in zip(subs, a2, a3):
        assert y < 0.5 * x, f"{s} did not fall substantially: {x} to {y}"
    biggest = a2.index(max(a2))
    assert a3[biggest] < a2[biggest], \
        "'the largest substance after secondary treatment did not fall' must be false"
    fracs = [round(y / x, 2) for x, y in zip(a2, a3)]
    return (f"all {len(subs)} substances fall between the two stages, to fractions "
            f"{fracs} of their earlier values")


def q20(table, item):
    treatments = [t.strip().lower() for t in cg.labels(table)]
    before = cg.col(table, BEFORE_D)
    after = cg.col(table, AFTER_D)
    named = [i for i, t in enumerate(treatments) if t in NAMED_DISINFECTANTS]
    none = [i for i, t in enumerate(treatments) if t.startswith("no disinfectant")]
    assert len(named) == 3, \
        f"the three disinfectants STB-3.N.4 names are not all present: {treatments}"
    assert len(none) == 1, f"there is no untreated row: {treatments}"
    assert len(set(before)) == 1, f"the batches do not share a starting count: {before}"
    for i in named:
        assert after[i] < 0.001 * before[i], \
            f"{treatments[i]} did not cut the count to a tiny fraction: {after[i]}"
    n = none[0]
    assert after[n] > 0.5 * before[n], f"the untreated row changed too much: {after[n]}"
    return (f"from a shared start of {before[0]:.0f}, the three named disinfectants finish "
            f"at {[after[i] for i in named]} while the untreated batch finishes at "
            f"{after[n]:.0f}")


def q24(table, item):
    plants = cg.labels(table)
    stages = cg.col(table, STAGES)
    nitro = cg.col(table, NITRO)
    order = [p for _, p in sorted(zip(stages, plants))]
    assert order == [p for _, p in sorted(zip(nitro, plants), reverse=True)], \
        f"more stages does not mean less nitrogen: {stages} {nitro}"
    assert nitro[stages.index(min(stages))] == max(nitro), \
        "'the plant with the fewest stages discharges the least' must be false"
    assert len(set(nitro)) == len(nitro), "'all three the same' must be false"
    return (f"ranking the plants by number of stages gives {order}, the reverse of the "
            "order by nitrogen remaining")


CLAIMS = [
 ("physical removal of large objects, often with screens and grates",
  "STB-3.N.1 near verbatim: primary treatment is the physical removal of large objects, often through the use of screens and grates, followed by the settling of solid waste in the bottom of a tank. The rejected options state STB-3.N.2, STB-3.N.3 and STB-3.N.4."),
 ("bacteria break down organic matter into carbon dioxide and inorganic sludge that settles",
  "STB-3.N.2 near verbatim: secondary treatment is a biological process in which bacteria break down organic matter into carbon dioxide and inorganic sludge, which settles in the bottom of a tank."),
 ("ecological or chemical processes to remove any pollutants left in the water",
  "STB-3.N.3 verbatim: tertiary treatment is the use of ecological or chemical processes to remove any pollutants left in the water after primary and secondary treatment."),
 ("bacteria count only collapses at the last step",
  "Recomputed in q4 above: solids and organic matter fall to under a tenth of the raw values across the early stages while the bacteria count stays above a tenth of its start until the final row, where it drops by more than a thousandfold. STB-3.N.4 places the disinfectant prior to discharge."),
 ("Chlorine, ozone or ultraviolet light",
  "STB-3.N.4 states that prior to discharge the treated water is exposed to one or more disinfectants, usually chlorine, ozone or UV light, to kill bacteria. The rejected options list nutrients, heavy metals, filter media and gases."),
 ("increase the rate at which the bacteria break down the organic matter",
  "STB-3.N.2 verbatim: the tank is aerated to increase the rate at which the bacteria break down the organic matter. Killing bacteria is STB-3.N.4 and screening is STB-3.N.1."),
 ("Carbon dioxide and inorganic sludge",
  "STB-3.N.2 states that bacteria break down organic matter into carbon dioxide and inorganic sludge. The rejected options name disinfectants from STB-3.N.4, the material of STB-3.N.1, and products the framework does not attribute to this stage."),
 ("rags and the grit were almost entirely taken out",
  "Recomputed in q8 above: the two solid rows carry removed masses more than ten times what remains, while the dissolved organic matter row has nothing removed and a large mass remaining. STB-3.N.1 makes primary treatment physical and STB-3.N.2 assigns organic matter to the bacteria."),
 ("Primary, then secondary, then tertiary, with disinfection prior to discharge",
  "STB-3.N.3 describes tertiary treatment as removing pollutants left after primary and secondary treatment, fixing those three in order, and STB-3.N.4 places the disinfectant step prior to discharge."),
 ("settles in the bottom of a tank after the large objects have been screened out",
  "STB-3.N.1 states that primary treatment is the physical removal of large objects followed by the settling of solid waste in the bottom of a tank. Bacterial breakdown is STB-3.N.2 and disinfection STB-3.N.4."),
 ("kill bacteria before the water is discharged",
  "STB-3.N.4 states that prior to discharge the treated water is exposed to one or more disinfectants to kill bacteria. Settling belongs to STB-3.N.1 and feeding the bacteria would work against the stated purpose."),
 ("greater the share of organic matter broken down in eight hours",
  "Recomputed in q12 above: ranking the tanks by air supplied gives the same order as ranking them by the share broken down, and the tank with no air is lowest. STB-3.N.2 states that the tank is aerated to increase that rate."),
 ("Primary treatment, which physically removes large objects with screens and grates",
  "STB-3.N.1 assigns the physical removal of large objects, often through screens and grates, to primary treatment. The other stages are biological, ecological or chemical, and disinfection targets bacteria."),
 ("Secondary treatment, carried out by bacteria",
  "STB-3.N.2 calls secondary treatment a biological process in which bacteria break down organic matter. STB-3.N.1 is physical, STB-3.N.3 ecological or chemical, and STB-3.N.4 applies a disinfectant."),
 ("different leftover pollutants call for different processes",
  "STB-3.N.3 defines tertiary treatment by the pollutants left in the water after primary and secondary treatment and describes the means as ecological or chemical processes rather than one fixed technique."),
 ("Every substance measured fell substantially between the two stages",
  "Recomputed in q16 above: each substance's later value is under half its earlier value, including the one present in the largest amount. STB-3.N.3 states that tertiary treatment removes any pollutants left after the first two stages."),
 ("disinfection applied prior to discharge",
  "STB-3.N.4 assigns the killing of bacteria to the disinfectant applied prior to discharge, and the other measurements in the stem show the physical and biological stages working."),
 ("Secondary treatment, in which bacteria break the organic matter down",
  "STB-3.N.1 covers the physical removal that has plainly worked and STB-3.N.2 assigns the breakdown of organic matter to the bacteria of secondary treatment, so that is the stage the result points to."),
 ("Powdered lime added to the settling tank",
  "STB-3.N.4 names chlorine, ozone and UV light and states that the water is exposed to one or more of them, so a combination is permitted by the statement. Lime added to a settling tank appears in none of this topic's statements."),
 ("cut the bacteria to a tiny fraction of the starting count",
  "Recomputed in q20 above: the three named disinfectant rows finish below a thousandth of a shared starting count while the untreated row keeps more than half of it. STB-3.N.4 names those three as the usual disinfectants."),
 ("Secondary treatment, paired with bacteria breaking organic matter down in an aerated tank",
  "STB-3.N.2 gives secondary treatment its bacteria and aerated tank, STB-3.N.1 gives primary its screens and settling, STB-3.N.3 gives tertiary its ecological or chemical removal and STB-3.N.4 gives disinfection the killing of bacteria. Each rejected pairing crosses two."),
 ("leaving the dissolved organic matter and the bacteria for the later stages",
  "STB-3.N.1 limits primary treatment to physical removal and settling, STB-3.N.2 assigns organic matter to bacteria in the secondary stage, and STB-3.N.4 assigns bacteria to the disinfectant before discharge."),
 ("organic matter in the water, measured before and after the aerated tank",
  "STB-3.N.2 makes the breakdown of organic matter by bacteria the work of secondary treatment, so a before and after measurement across that tank is the direct test. Screenings belong to STB-3.N.1 and the post-disinfection count to STB-3.N.4."),
 ("more stages a plant uses, the less nitrogen remains",
  "Recomputed in q24 above: ranking the plants by number of stages gives the reverse of the order by nitrogen remaining. STB-3.N.3 states that tertiary treatment removes pollutants left after primary and secondary treatment."),
 ("Living bacteria do the work of breaking the organic matter down",
  "STB-3.N.2 calls secondary treatment a biological process in which bacteria break down organic matter, so the agent is what makes it biological. STB-3.N.1 is physical and STB-3.N.3 ecological or chemical."),
 ("It settles in the bottom of a tank",
  "STB-3.N.2 states that bacteria break organic matter down into carbon dioxide and inorganic sludge, which settles in the bottom of a tank. The framework makes no statement about discharging or converting that sludge."),
 ("run at several different air supply rates",
  "STB-3.N.2 states that the tank is aerated to increase the rate at which the bacteria break down the organic matter, so varying the air and measuring the breakdown is the test. A single condition provides no comparison."),
 ("water that is about to leave the plant, after the other stages have done their work",
  "STB-3.N.4 places the disinfectant prior to discharge and STB-3.N.2 depends on living bacteria doing the breakdown, so disinfecting at the head of the plant would remove the agent of the biological stage."),
 ("Tertiary treatment, using ecological or chemical processes on what is left",
  "STB-3.N.3 states that tertiary treatment is the use of ecological or chemical processes to remove any pollutants left in the water after primary and secondary treatment, which is the situation the stem describes."),
 ("ecological or chemical processes remove what is still left, and a disinfectant kills bacteria",
  "Each clause of the keyed summary is one of STB-3.N.1 through STB-3.N.4 in the order the framework gives them. Every rejected summary reverses the order, denies the biological stage, or assigns a stage the wrong job."),
]

TABLE_CHECKS = {4: q4, 8: q8, 12: q12, 16: q16, 20: q20, 24: q24}

es.run(e8_11, CLAIMS, TABLE_CHECKS, sys.argv)
