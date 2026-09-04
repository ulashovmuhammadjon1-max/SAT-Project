"""Key audit for AP ENVIRONMENTAL SCIENCE 8.7 Persistent Organic Pollutants (POPs).

One (anchor, claim) per item, in module order; the anchor must appear in the
keyed choice and in no distractor. `cg_check.check` is the structural gate and
`es_check` carries the notation gate and the negative control.

WHAT THE KEYS REST ON
---------------------
  STB-3.H.1  POPs do not easily break down in the environment because they are
             synthetic, carbon based molecules, such as DDT and PCBs -- items
             1, 3, 4, 11, 12, 13, 14, 16, 17, 23, 24, 28;
  STB-3.H.2  POPs can be toxic to organisms because they are soluble in fat,
             which allows them to accumulate in organisms' fatty tissues --
             items 2, 6, 8, 10, 15, 18, 21, 26;
  STB-3.H.3  POPs can travel over long distances via wind and water before
             being redeposited -- items 5, 7, 9, 19, 20, 22, 29.
Items 25 and 30 join all three statements.

SCOPE. Bioaccumulation and biomagnification are defined in 8.8 under STB-3.I.1
and STB-3.I.2 and their effects under STB-3.J.1 to STB-3.J.3; no key here
defines either term or asserts a rise in concentration across trophic levels.
Methylmercury is keyed in 8.2 under STB-3.B.10 and is not a synthetic carbon
based molecule, so it appears nowhere here.

NOT KEYED: no half-life figure for a real compound, no treaty, and no
concentration described as safe or unsafe. The framework states none of them,
so the data items key only directions, rank orders and comparisons the tables
themselves carry.

DATA ITEMS: 3, 6, 9, 12, 15 and 18 carry tables and every keyed reading is
recomputed here from the table alone.

NEGATIVE CONTROL: `python3 verify_e8_7.py --selftest`.
"""
import sys

import cg_check as cg
import es_check as es
import e8_7

DAYS = "Days for half of the amount applied to break down"
FATPCT = "Fat content of the tissue (percent by mass)"
CONC_TISSUE = "Concentration of the pollutant (parts per million)"
DIST = "Distance from the nearest area of use (kilometers)"
SOIL = "Concentration in surface soil (nanograms per gram)"
POP_PPB = "Concentration of the persistent organic pollutant (parts per billion)"
OTHER_PPB = "Concentration of the readily broken down pesticide (parts per billion)"
YEARS = "Years since both compounds stopped being used"
FATTY = "Concentration in fatty tissue (parts per million)"
MUSCLE = "Concentration in muscle (parts per million)"
WATSOL = "Solubility in water (milligrams per liter)"
FATSOL = "Solubility in fat (units of the same scale)"
INFAT = "Concentration measured in animal fat (parts per million)"


def q3(table, item):
    names = cg.labels(table)
    kind = [str(r[1]).strip().lower() for r in table["rows"]]
    days = cg.col(table, DAYS)
    synth = [i for i, k in enumerate(kind) if k == "synthetic and carbon based"]
    quick = [i for i, k in enumerate(kind) if k == "readily broken down by soil microbes"]
    assert len(synth) == 2 and len(quick) == 2, \
        f"the two described groups are not both present as written: {kind}"
    assert min(days[i] for i in synth) > 10 * max(days[i] for i in quick), \
        f"the synthetic carbon based rows do not last far longer: {days}"
    assert min(days[i] for i in synth) >= 1000, \
        f"the synthetic carbon based rows are not measured in thousands of days: {days}"
    assert max(days[i] for i in quick) < 100, \
        f"the readily broken down rows are not gone within about a month: {days}"
    assert days.index(min(days)) in quick, \
        "'the fastest to break down is a synthetic carbon based one' must be false"
    assert len(set(days)) == len(days), "'about the same time for all four' must be false"
    return (f"the synthetic carbon based rows {[names[i] for i in synth]} take "
            f"{[days[i] for i in synth]} days against {[days[i] for i in quick]} for the "
            "readily broken down rows")


def q6(table, item):
    tissues = cg.labels(table)
    fat = cg.col(table, FATPCT)
    conc = cg.col(table, CONC_TISSUE)
    order = [t for _, t in sorted(zip(fat, tissues))]
    assert order == [t for _, t in sorted(zip(conc, tissues))], \
        f"the order by fat content does not match the order by concentration: {fat} {conc}"
    assert conc[fat.index(max(fat))] == max(conc), "the fattiest tissue is not the highest"
    assert conc[fat.index(min(fat))] == min(conc), "the leanest tissue is not the lowest"
    assert len(set(conc)) == len(conc), "'the same in every tissue' must be false"
    return (f"ranking the tissues by fat content gives {order}, the same order as ranking "
            "them by pollutant concentration")


def q9(table, item):
    sites = cg.labels(table)
    dist = cg.col(table, DIST)
    used = [str(r[2]).strip().lower() for r in table["rows"]]
    conc = cg.col(table, SOIL)
    assert all(c > 0 for c in conc), f"not every site carries a measurable amount: {conc}"
    never = [i for i, u in enumerate(used) if u == "no"]
    assert len(never) >= 3, f"fewer than three sites are marked as never treated: {used}"
    assert max(dist[i] for i in never) >= 1000, \
        "no untreated site is thousands of kilometers away"
    pairs = sorted(zip(dist, conc))
    assert all(pairs[i][1] > pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"the concentration does not fall as distance rises: {pairs}"
    return (f"every site carries a measurable residue, {len(never)} of them marked as "
            f"never treated, and sorted by distance the values run {[c for _, c in pairs]}")


def q12(table, item):
    years = cg.col(table, YEARS)
    pop = cg.col(table, POP_PPB)
    other = cg.col(table, OTHER_PPB)
    start = years.index(min(years))
    last = years.index(max(years))
    assert pop[start] == other[start], "the two compounds do not start from the same value"
    assert pop[last] > 0.5 * pop[start], \
        f"the persistent compound is not still above half its start: {pop}"
    assert other[last] < 0.01 * other[start], \
        f"the readily broken down compound has not nearly disappeared: {other}"
    assert all(pop[i] > other[i] for i in range(1, len(years))), \
        "the persistent compound is not the higher of the two after year zero"
    return (f"after {years[last]:.0f} years the persistent compound is at {pop[last]} "
            f"parts per billion against {other[last]} for the other, from a shared start "
            f"of {pop[start]}")


def q15(table, item):
    animals = cg.labels(table)
    fatty = cg.col(table, FATTY)
    muscle = cg.col(table, MUSCLE)
    for a, f, m in zip(animals, fatty, muscle):
        assert f > 5 * m, f"{a}: fatty tissue {f} is not many times muscle {m}"
    ratios = [round(f / m, 1) for f, m in zip(fatty, muscle)]
    return (f"in all {len(animals)} animals the fatty tissue value exceeds the muscle "
            f"value, by factors of {ratios}")


def q18(table, item):
    comps = cg.labels(table)
    wat = cg.col(table, WATSOL)
    fat = cg.col(table, FATSOL)
    infat = cg.col(table, INFAT)
    order = [c for _, c in sorted(zip(fat, comps))]
    assert order == [c for _, c in sorted(zip(infat, comps))], \
        f"the order by fat solubility does not match the order in animal fat: {fat} {infat}"
    assert order == [c for _, c in sorted(zip(wat, comps), reverse=True)], \
        f"the order by fat solubility is not the reverse of the order by water solubility: {wat}"
    assert infat[fat.index(min(fat))] == min(infat), \
        "'the least fat soluble is found at the highest concentration' must be false"
    assert len(set(infat)) == len(infat), "'the same concentration for all four' must be false"
    return (f"ranking by solubility in fat gives {order}, the same order as the "
            "concentration in animal fat and the reverse of the order by water solubility")


CLAIMS = [
 ("synthetic, carbon based molecules",
  "STB-3.H.1 verbatim: persistent organic pollutants do not easily break down in the environment because they are synthetic, carbon based molecules. Mineral salts, heavy metals from mining (STB-3.B.7) and atmospheric gases belong to other statements."),
 ("soluble in fat, which allows them to accumulate in the fatty tissues",
  "STB-3.H.2 verbatim: POPs can be toxic to organisms because they are soluble in fat, which allows them to accumulate in organisms' fatty tissues. Each rejected option substitutes a route that would remove rather than store the compound."),
 ("took far longer to break down by half",
  "Recomputed in q3 above: both rows described as synthetic and carbon based carry breakdown times more than ten times those of the readily broken down rows. STB-3.H.1 gives that as the reason these compounds are called persistent."),
 ("DDT and PCBs",
  "STB-3.H.1 names DDT and PCBs as its examples. Lead and cadmium are heavy metals under STB-3.B.7, nitrate and phosphate are nutrients under STB-3.F, and the remaining pairs are greenhouse gases and acid precursors from units 7 and 9."),
 ("travel over long distances by wind and water before being redeposited",
  "STB-3.H.3 verbatim: POPs can travel over long distances via wind and water before being redeposited. Every rejected option denies or narrows that movement."),
 ("highest fat content carries by far the highest concentration",
  "Recomputed in q6 above: ranking the tissues by fat content gives the same order as ranking them by pollutant concentration, with the fattiest highest and the leanest lowest. STB-3.H.2 supplies the reason."),
 ("can travel over long distances by wind and water before being redeposited",
  "STB-3.H.3 is the framework's statement about movement, and long distance transport followed by redeposition is what places a compound where it was never used. STB-3.H.1 and STB-3.H.2 explain persistence and storage instead."),
 ("dissolves in fat far better than in the watery fluids of the body",
  "STB-3.H.2 attributes accumulation to solubility in fat, so fatty tissue rather than a watery compartment is where the compound collects. The framework makes no claim that blood cannot be sampled or that it destroys the compound."),
 ("including sites thousands of kilometers away where it was never applied",
  "Recomputed in q9 above: every row carries a measurable residue, three of them marked as never treated and one of those five thousand kilometers away, with concentrations falling as distance rises. That is the transport and redeposition of STB-3.H.3."),
 ("attributes their toxicity to solubility in fat",
  "STB-3.H.2 gives fat solubility as the reason for the toxicity and STB-3.H.1 gives resistance to breakdown as the reason for the persistence. STB-3.H.3 allows water to carry them, but that is transport rather than the source of the toxicity."),
 ("length of time the compound remains in soil or water before it breaks down",
  "STB-3.H.1 makes resistance to breaking down in the environment the defining property, so time until breakdown is the measurement that tests membership in the class. Price, color, sales and packaging test none of the three statements."),
 ("still at more than half its starting concentration after twenty years",
  "Recomputed in q12 above: from a shared starting value the persistent column is still above half after twenty years while the other has fallen below one hundredth of its start. STB-3.H.1 is the reason."),
 ("molecules already released do not easily break down",
  "STB-3.H.1 states that these compounds do not easily break down in the environment, so a stock already released remains after new input stops. The framework describes them as synthetic rather than naturally produced."),
 ("break down quickly once released into soil or water",
  "STB-3.H.1 states the opposite, that these compounds do not easily break down in the environment. The four rejected options restate STB-3.H.1, STB-3.H.2 and STB-3.H.3 correctly, so the keyed option is the one property the framework denies."),
 ("concentration in fatty tissue is many times the concentration in muscle",
  "Recomputed in q15 above: every animal's fatty tissue value exceeds its muscle value by more than a factor of five. STB-3.H.2 attributes that to solubility in fat."),
 ("resist breaking down and therefore remain in the environment for a long time",
  "STB-3.H.1 defines the class by the fact that these compounds do not easily break down in the environment, so the name refers to the fate of the molecule rather than to a pattern of release or of use."),
 ("fails the property that defines the class",
  "STB-3.H.1 makes not easily breaking down the defining behavior and gives being synthetic and carbon based as its reason, so a compound that degrades within two weeks does not show the property the class is named for."),
 ("dissolve best in fat and least in water",
  "Recomputed in q18 above: ranking by solubility in fat gives the same order as the concentration found in animal fat and the reverse of the order by water solubility. STB-3.H.2 makes fat solubility the reason for accumulation."),
 ("Wind and water",
  "STB-3.H.3 names wind and water as the routes by which these pollutants travel long distances before being redeposited. The framework names no other transport route for them."),
 ("settle there, far from where they were released",
  "STB-3.H.3 pairs long distance travel with redeposition, which is how a compound comes to be measured far from its release. Destruction in transit would contradict the persistence of STB-3.H.1."),
 ("held in fatty tissue instead of being carried out in watery wastes",
  "STB-3.H.2 states that solubility in fat allows these compounds to accumulate in organisms' fatty tissues, which is a matter of where the compound is held rather than of how fast it is destroyed."),
 ("with wind or current records connecting them to areas of use",
  "STB-3.H.3 asserts movement followed by redeposition, so detection at distant sites together with a transport pathway is the test. Source measurements, production totals and storage conditions test none of it."),
 ("manufactured rather than produced by natural processes",
  "STB-3.H.1 describes these molecules as synthetic and carbon based and gives that origin as the reason they do not easily break down. Natural production, decay products and mined minerals are different origins."),
 ("Resistance to breakdown, so the compound remains in the environment long after",
  "STB-3.H.1 makes resistance to breakdown the reason these compounds persist. Each rejected pairing takes a property from STB-3.H.1 to STB-3.H.3 and attaches the opposite consequence."),
 ("resists breakdown and travels long distances by wind and water",
  "STB-3.H.1 supplies the persistence, STB-3.H.3 the long distance transport and redeposition, and STB-3.H.2 the accumulation in fatty tissue, which together account for a residue in a country with no history of use."),
 ("against the concentration measured in a low fat tissue of the same animal",
  "STB-3.H.2 predicts that the compound collects in fatty tissue, so a within-animal comparison between a fatty and a low fat tissue is what tests it. A single value, a sample size, a travel distance and a body mass do not."),
 ("describe the kind of molecule that resists breaking down",
  "STB-3.H.1 gives synthetic and carbon based together as the reason these compounds do not easily break down. The framework makes no claim that carbon based molecules are alive, water soluble, natural, or removed by photosynthesis."),
 ("do not easily break down in the environment",
  "A residue still measurable in sediment laid down decades ago is the persistence stated in STB-3.H.1. Fat solubility (STB-3.H.2) and transport (STB-3.H.3) do not explain survival in a buried layer."),
 ("freshly fallen snow sampled at the remote region",
  "STB-3.H.3 names wind as one of the two transport routes, so sampling air and fresh deposition at the receiving end and matching it to upwind releases tests that pathway. A single soil sample cannot distinguish a route."),
 ("their fat solubility lets them accumulate in fatty tissues",
  "Each clause of the keyed summary is one of STB-3.H.1, STB-3.H.2 and STB-3.H.3. Every rejected summary denies the persistence, the transport, or the accumulation in fatty tissue."),
]

TABLE_CHECKS = {3: q3, 6: q6, 9: q9, 12: q12, 15: q15, 18: q18}

es.run(e8_7, CLAIMS, TABLE_CHECKS, sys.argv)
