"""Key audit for AP ENVIRONMENTAL SCIENCE 8.5 Eutrophication.

One (anchor, claim) per item, in module order; the anchor must appear in the
keyed choice and in no distractor. `cg_check.check` is the structural gate and
`es_check` carries the notation gate and the negative control.

WHAT THE KEYS REST ON
---------------------
  STB-3.F.1  eutrophication occurs when a body of water is enriched in
             nutrients -- items 1, 13, 23;
  STB-3.F.2  the nutrient increase causes an algal bloom, microbes digesting
             the dead bloom consume the oxygen, dissolved oxygen falls, and the
             lack of it can cause large die-offs -- items 2, 3, 9, 10, 12, 16,
             19, 22, 25, 28;
  STB-3.F.3  hypoxic waterways are low in dissolved oxygen -- items 4, 14, 17;
  STB-3.F.4  oligotrophic waterways have very low nutrients, stable algae
             populations and high dissolved oxygen -- items 5, 6, 18, 26;
  STB-3.F.5  the anthropogenic causes are agricultural runoff and wastewater
             release -- items 7, 8, 11, 15, 21, 24.
Items 20, 27 and 29 are design items whose keys turn on the same sequence, and
item 30 joins all five statements.

SCOPE, because neighbouring topics touch the same water. The oceanic dead zone
and the oxygen sag curve are keyed in 8.2 under STB-3.B.5 and STB-3.B.6; the
temperature control on dissolved oxygen is keyed in 8.6 under STB-3.G.2. No key
here attributes an oxygen change to temperature, and none re-asks the dead zone
definition.

NOT KEYED: no nutrient limit, no milligrams-per-liter threshold defining
hypoxia, and no named water body. The framework states none, so item 4 and item
17 key only the direction, low in dissolved oxygen.

DATA ITEMS: 3, 6, 8, 10, 12 and 14 carry tables and every keyed reading is
recomputed below from the table alone.

NEGATIVE CONTROL: `python3 verify_e8_5.py --selftest`.
"""
import sys

import cg_check as cg
import es_check as es
import e8_5

NIT = "Nitrate in the lake (milligrams per liter)"
CHL = "Algae measured as chlorophyll (micrograms per liter)"
DO = "Dissolved oxygen (milligrams per liter)"
NUTR = "Total nutrients (micrograms per liter)"
DO_DEEP = "Dissolved oxygen at depth (milligrams per liter)"
NLOAD = "Nitrogen delivered each year (tons)"
DO_DAWN = "Dissolved oxygen before dawn (milligrams per liter)"
DEAD = "Dead fish counted the following morning"
PHOS = "Phosphorus reaching the lake each year (tons)"
CHL_SUM = "Summer algae measured as chlorophyll (micrograms per liter)"
DO_MIN = "Lowest summer dissolved oxygen (milligrams per liter)"
DEPTH = "Depth in a eutrophic lake in late summer (meters)"


def q3(table, item):
    weeks = cg.labels(table)
    nit = cg.col(table, NIT)
    chl = cg.col(table, CHL)
    do = cg.col(table, DO)
    i_nit = nit.index(max(nit))
    i_chl = chl.index(max(chl))
    drops = [do[i] - do[i + 1] for i in range(len(do) - 1)]
    i_drop = drops.index(max(drops))
    assert i_nit < i_chl, f"the nitrate peak ({weeks[i_nit]}) does not precede the algal peak"
    assert i_chl <= i_drop, "the largest oxygen fall does not come at or after the algal peak"
    assert do[0] == max(do) and do[-1] == min(do), "oxygen must start highest and end lowest"
    assert len({i_nit, i_chl}) == 2, "'all peak in the same week' must be false"
    return (f"nitrate peaks at {weeks[i_nit]}, algae at {weeks[i_chl]}, and the largest oxygen "
            f"fall runs from {weeks[i_drop]} to {weeks[i_drop + 1]}, in that order")


def q6(table, item):
    lakes = cg.labels(table)
    nutr = cg.col(table, NUTR)
    chl = cg.col(table, CHL)
    do = cg.col(table, DO_DEEP)
    order = [l for _, l in sorted(zip(nutr, lakes))]
    assert order == [l for _, l in sorted(zip(chl, lakes))], "algae do not follow the nutrient order"
    assert order == [l for _, l in sorted(zip(do, lakes), reverse=True)], \
        "dissolved oxygen does not run opposite to the nutrient order"
    assert do[nutr.index(max(nutr))] == min(do), "'the most nutrients gives the most oxygen' must be false"
    assert len(set(chl)) == len(chl), "'the same algae in all four' must be false"
    return (f"ranking by nutrients gives {order}, the same order as by algae and the reverse of "
            "the order by dissolved oxygen")


def q8(table, item):
    basins = cg.labels(table)
    kind = {r[0]: r[1] for r in table["rows"]}
    load = dict(zip(basins, cg.col(table, NLOAD)))
    forest = [b for b in basins if kind[b].startswith("forest")][0]
    crops = [b for b in basins if kind[b].startswith("cropland")]
    both = [b for b in crops if "outfall" in kind[b] and "no outfall" not in kind[b]][0]
    assert load[forest] == min(load.values()), "the forested sub-basin is not the smallest"
    assert min(load[b] for b in crops) > 5 * load[forest], \
        f"the cropland sub-basins are not far above the forested one: {load}"
    assert load[both] == max(load.values()), "the cropland-with-outfall sub-basin is not the largest"
    return (f"the forested sub-basin delivers {load[forest]:.0f} tons against "
            f"{[load[b] for b in crops]} from the cropland sub-basins, the largest being the one "
            "that also receives wastewater")


def q10(table, item):
    nights = cg.labels(table)
    do = dict(zip(nights, cg.col(table, DO_DAWN)))
    dead = dict(zip(nights, cg.col(table, DEAD)))
    order = [n for _, n in sorted(zip(do.values(), nights))]
    assert [dead[n] for n in order] == sorted((dead[n] for n in order), reverse=True), \
        f"fish deaths do not fall as oxygen rises: {dead}"
    assert dead[max(do, key=do.get)] == min(dead.values()), \
        "'the highest oxygen night had the most deaths' must be false"
    assert max(dead.values()) > 0, "'no fish died' must be false"
    assert len(set(dead.values())) == len(dead), "'the same number every night' must be false"
    return (f"ordered from lowest to highest oxygen the death counts run "
            f"{[dead[n] for n in order]}, falling as oxygen rises")


def q12(table, item):
    stages = cg.labels(table)
    phos = dict(zip(stages, cg.col(table, PHOS)))
    chl = dict(zip(stages, cg.col(table, CHL_SUM)))
    do = dict(zip(stages, cg.col(table, DO_MIN)))
    seq = list(stages)
    assert all(phos[seq[i]] > phos[seq[i + 1]] for i in range(len(seq) - 1)), \
        f"phosphorus does not fall across the program: {phos}"
    assert all(chl[seq[i]] > chl[seq[i + 1]] for i in range(len(seq) - 1)), \
        f"the algae do not fall across the program: {chl}"
    assert all(do[seq[i]] < do[seq[i + 1]] for i in range(len(seq) - 1)), \
        f"the oxygen minimum does not rise across the program: {do}"
    return (f"phosphorus runs {[phos[s] for s in seq]} tons and algae {[chl[s] for s in seq]}, both "
            f"falling, while the oxygen minimum runs {[do[s] for s in seq]}, rising")


def q14(table, item):
    depth = cg.col(table, DEPTH)
    do = cg.col(table, DO)
    pairs = sorted(zip(depth, do))
    assert all(pairs[i][1] > pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"oxygen does not fall with depth: {pairs}"
    assert do[depth.index(max(depth))] == min(do), "the deepest sample is not the lowest in oxygen"
    assert do[depth.index(min(depth))] == max(do), "'the shallowest is lowest' must be false"
    return (f"sorted by depth the oxygen values run {[d for _, d in pairs]} milligrams per liter, "
            "falling at every step to the smallest value at the greatest depth")


CLAIMS = [
 ("enriched in nutrients",
  "STB-3.F.1 verbatim: eutrophication occurs when a body of water is enriched in nutrients. Heating belongs to STB-3.G.1, acidification to STB-4.H.1 and sediment to STB-3.B.9."),
 ("microbes digest the algae along with the oxygen in the water",
  "STB-3.F.2 near verbatim: the increase in nutrients causes an algal bloom; when the bloom dies, microbes digest the algae along with the oxygen in the water, lowering dissolved oxygen and causing large die-offs of fish and other aquatic organisms. Each rejected sequence contradicts one of those steps."),
 ("dissolved oxygen fell after the algae had passed their peak",
  "Recomputed in q3 above: the nitrate maximum precedes the algal maximum, and the largest fall in dissolved oxygen comes at or after the algal peak. That order is the sequence STB-3.F.2 describes."),
 ("low in dissolved oxygen",
  "STB-3.F.3 verbatim: hypoxic waterways are those bodies of water that are low in dissolved oxygen. No threshold is stated by the framework and none is keyed here; high oxygen, absent nutrients, warming and acidity are different conditions."),
 ("very low amounts of nutrients, stable algae populations, and high dissolved oxygen",
  "STB-3.F.4 verbatim: compared to eutrophic waterways, oligotrophic waterways have very low amounts of nutrients, stable algae populations, and high dissolved oxygen. Each rejected option reverses at least one of the three."),
 ("least algae and the highest dissolved oxygen",
  "Recomputed in q6 above: ranking the lakes by nutrients gives the same order as by algae and the reverse of the order by dissolved oxygen. That is the contrast STB-3.F.4 draws."),
 ("Agricultural runoff and wastewater release",
  "STB-3.F.5 verbatim: anthropogenic causes of eutrophication are agricultural runoff and wastewater release. Eruptions, fires, thermal discharge, natural erosion and acid deposition belong to other statements."),
 ("the one that also has wastewater outfalls delivers the most",
  "Recomputed in q8 above: the forested sub-basin is smallest by more than a factor of five and the cropland sub-basin that also receives wastewater is largest. Those two land uses are the causes named in STB-3.F.5."),
 ("consume the oxygen in the water as they do so",
  "STB-3.F.2 places the oxygen loss at the microbial digestion of the dead bloom, which is why it follows rather than accompanies the growth. The framework gives no acid, no atmospheric absorption and no cooling role in this sequence."),
 ("lowest dissolved oxygen were followed by the largest numbers of dead fish",
  "Recomputed in q10 above: ordering the nights by dissolved oxygen puts the death counts in the opposite order, with none on the highest-oxygen night. STB-3.F.2 states that the lack of dissolved oxygen can result in large die-offs."),
 ("Anthropogenic causes of eutrophication are agricultural runoff",
  "The item asks which statement names a cause, and STB-3.F.5 is the framework's statement of the anthropogenic causes. The rejected options are STB-3.F.1, STB-3.F.2, STB-3.F.3 and STB-3.F.4, which define a condition or describe a consequence."),
 ("summer algae fell and the lowest summer dissolved oxygen rose",
  "Recomputed in q12 above: phosphorus and algae fall at every stage while the oxygen minimum rises at every stage. That is STB-3.F.2's sequence run backward as the nutrient input is cut."),
 ("in contrast with an oligotrophic waterway's very low nutrients",
  "STB-3.F.1 defines eutrophication as enrichment in nutrients and STB-3.F.4 contrasts eutrophic with oligotrophic waterways. The rejected options describe the oligotrophic case or a process from another topic."),
 ("deepest water sampled is the lowest in oxygen",
  "Recomputed in q14 above: dissolved oxygen falls at every step downward and the deepest sample holds the smallest value. Water low in dissolved oxygen is what STB-3.F.3 calls hypoxic."),
 ("Wastewater release",
  "STB-3.F.5 names wastewater release as one of the two anthropogenic causes of eutrophication, and a discharge from a treatment plant is wastewater. Agricultural runoff is the other; thermal pollution, acid deposition and construction sediment belong to other topics."),
 ("oxygen the fish need is consumed by the microbes",
  "STB-3.F.2 runs from the dying bloom to microbial digestion that consumes the oxygen and then to die-offs, so the deaths are attributed to the lack of dissolved oxygen rather than to any direct action of the algae."),
 ("concentration of dissolved oxygen in the water",
  "STB-3.F.3 defines a hypoxic waterway as one low in dissolved oxygen, so dissolved oxygen is the measurement that identifies the condition. Nutrients, visible algae, temperature and depth are related quantities but not the definition."),
 ("Very low nutrients, a stable algae population, and high dissolved oxygen",
  "STB-3.F.4 attributes exactly those three properties to oligotrophic waterways. Each rejected option pairs the nutrient level with the wrong oxygen level or describes the eutrophic case."),
 ("bloom that follows dies and is digested by microbes",
  "STB-3.F.2 turns the nutrient increase into a bloom, then into oxygen depletion when the bloom dies and is digested, then into die-offs, so the harm arrives through the oxygen. The rejected options deny steps the framework states."),
 ("Nutrient concentrations and dissolved oxygen measured together at several sites",
  "The claim links two quantities from STB-3.F.1 and STB-3.F.2, so the test needs both measured at the same places. A single oxygen reading, nutrients alone, channel width and bridge counts leave one side unmeasured."),
 ("Both deliver nutrients to a body of water",
  "STB-3.F.1 makes eutrophication a matter of nutrient enrichment and STB-3.F.5 names both routes as anthropogenic causes, so both deliver nutrients. Nothing in the framework makes either a remover of nutrients."),
 ("microbes digesting it consumed the dissolved oxygen",
  "The interval between the bloom and the kill is exactly STB-3.F.2's sequence: the bloom dies, microbes digest it and consume the oxygen, and the lack of dissolved oxygen causes large die-offs. No toxicity, starvation, acidity or heating is claimed by the framework."),
 ("Eutrophic describes enrichment in nutrients, while hypoxic describes being low in dissolved oxygen",
  "STB-3.F.1 and STB-3.F.3 define the two terms by different quantities even though STB-3.F.2 connects them. Neither term refers to temperature or salinity."),
 ("smaller algal blooms and less oxygen depletion",
  "STB-3.F.5 makes wastewater release one of the two anthropogenic causes and STB-3.F.2 runs from nutrients to bloom to oxygen depletion, so cutting the nutrient input works backward along that chain."),
 ("need not appear at every place and time",
  "STB-3.F.2 places the fall in dissolved oxygen after the bloom dies and is digested by microbes, making it a stage in a sequence rather than a constant property of nutrient-rich water."),
 ("Oligotrophic, very low amounts of nutrients",
  "STB-3.F.4 gives oligotrophic waterways very low nutrients, stable algae populations and high dissolved oxygen; STB-3.F.3 gives hypoxic waterways low oxygen; STB-3.F.1 makes eutrophication enrichment. Each rejected pairing reverses one of those."),
 ("larger spring nutrient loads are followed by summers with lower oxygen",
  "A year-to-year correspondence between the size of the nutrient input and the depth of the oxygen decline is what tests the sequence in STB-3.F.2. Depth, species counts, units and comparative size test none of it."),
 ("die-offs of fish and other aquatic organisms together",
  "STB-3.F.2's own wording is large die-offs of fish and other aquatic organisms, so the effect is not confined to fish or to any one group."),
 ("nutrients reaching the lake each year and the lowest dissolved oxygen recorded each summer",
  "STB-3.F.1 and STB-3.F.2 make the input and the oxygen minimum the two ends of the process being managed, so tracking both is what shows whether it is working. Visitors, area, boat counts and shoreline length track neither."),
 ("hypoxic water and die-offs, in contrast with oligotrophic water",
  "Each clause of the summary is one of STB-3.F.1 to STB-3.F.5. Every rejected summary reverses the direction of the oxygen change, misattributes the cause, or conflates two of the framework's terms."),
]

TABLE_CHECKS = {3: q3, 6: q6, 8: q8, 10: q10, 12: q12, 14: q14}

es.run(e8_5, CLAIMS, TABLE_CHECKS, sys.argv)
