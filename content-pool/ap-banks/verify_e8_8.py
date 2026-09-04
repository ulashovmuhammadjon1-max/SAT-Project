"""Key audit for AP ENVIRONMENTAL SCIENCE 8.8 Bioaccumulation and Biomagnification.

One (anchor, claim) per item, in module order; the anchor must appear in the
keyed choice and in no distractor. `cg_check.check` is the structural gate and
`es_check` carries the notation gate and the negative control.

THE SWAP. This topic's characteristic distractor is the other definition:
bioaccumulation stated as a rise across trophic levels, or biomagnification
stated as a build-up inside one organism. Items 1, 2, 10, 14, 16 and 22 all
carry that swap, and each of those anchors below carries BOTH halves of the
distinction -- the process named AND the clause that separates it -- so an
anchor cannot match the swapped option. An anchor pinned only to the term, or
only to the clause, would match both.

WHAT THE KEYS REST ON
---------------------
  STB-3.I.1  bioaccumulation is the selective absorption and concentration of
             elements or compounds by cells in a living organism, most commonly
             fat-soluble compounds -- items 1, 6, 8, 14, 17, 28, 29;
  STB-3.I.2  biomagnification is the increase in concentration of substances
             per unit of body tissue at successively higher trophic levels of a
             food chain or web -- items 2, 3, 9, 13, 16, 19, 20, 22, 23, 27;
  STB-3.J.1  effects include eggshell thinning and developmental deformities in
             top carnivores of the higher trophic levels -- items 5, 11, 12,
             24, 26;
  STB-3.J.2  humans experience harmful effects from biomagnification, including
             issues with the reproductive, nervous and circulatory systems --
             items 7, 18, 21;
  STB-3.J.3  DDT, mercury and PCBs bioaccumulate and have significant
             environmental impacts -- item 4.
Items 10, 25 and 30 join several of them.

SCOPE. The three properties of persistent organic pollutants are keyed in 8.7
under STB-3.H.1 to STB-3.H.3 and methylmercury in 8.2 under STB-3.B.10. Item 26
cites STB-3.H.1 only for the persistence that STB-3.J.1's own wording assumes.

NOT KEYED: no magnification factor for a real ecosystem, no safe intake, no
named place. The framework states none of them, so the data items key only
directions, rank orders and one ratio, each recomputed below.

DATA ITEMS: 3, 6, 9, 12, 15 and 18 carry tables and every keyed reading is
recomputed here from the table alone.

NEGATIVE CONTROL: `python3 verify_e8_8.py --selftest`.
"""
import sys

import cg_check as cg
import es_check as es
import e8_8

PPM_CHAIN = "Concentration of the pollutant (parts per million)"
AGE = "Age of the fish sampled (years)"
PPM_AGE = "Concentration in the fish's fatty tissue (parts per million)"
PPM_EGG = "Concentration in the eggs (parts per million)"
SHELL = "Average eggshell thickness (millimeters)"
CHICKS = "Chicks hatched per nest"
FATSOL = "Concentration of the fat soluble compound (parts per million)"
WATSOL = "Concentration of the water soluble compound (parts per million)"
MEALS = "Meals of predatory fish eaten each month"
HAIR = "Mercury measured in hair (parts per million)"


def q3(table, item):
    steps = cg.labels(table)
    conc = cg.col(table, PPM_CHAIN)
    assert all(conc[i] < conc[i + 1] for i in range(len(conc) - 1)), \
        f"the concentration does not rise at every step in row order: {conc}"
    assert conc[0] == min(conc) and conc[-1] == max(conc), \
        "the water is not the lowest value or the top consumer is not the highest"
    assert len(set(conc)) == len(conc), "'the same at every position' must be false"
    return (f"in row order from {steps[0]} to {steps[-1]} the values run {conc} parts per "
            "million, rising at every step")


def q6(table, item):
    age = cg.col(table, AGE)
    conc = cg.col(table, PPM_AGE)
    pairs = sorted(zip(age, conc))
    assert all(pairs[i][1] < pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"the concentration does not rise with age: {pairs}"
    assert conc[age.index(min(age))] == min(conc), \
        "'the youngest fish carries the highest concentration' must be false"
    assert len(set(conc)) == len(conc), "'the same regardless of age' must be false"
    return (f"sorted by age the tissue values run {[c for _, c in pairs]} parts per "
            "million, rising at every step")


def q9(table, item):
    steps = cg.labels(table)
    conc = cg.col(table, PPM_CHAIN.replace("the pollutant", "the pollutant"))
    top, bottom = conc[-1], conc[0]
    assert bottom == min(conc) and top == max(conc), \
        f"the first row is not the smallest or the last row is not the largest: {conc}"
    ratio = top / bottom
    decades = [5, 50, 500, 5000, 50000, 500000]
    nearest = min(decades, key=lambda d: abs(d - ratio) / d)
    assert nearest == 50000, (
        f"the ratio {ratio:.0f} is not nearest to fifty thousand among {decades}")
    assert all(conc[i] < conc[i + 1] for i in range(len(conc) - 1)), \
        f"the chain does not rise at every step: {conc}"
    return (f"{steps[-1]} at {top} over {steps[0]} at {bottom} parts per million is a "
            f"factor of {ratio:.0f}, nearest to fifty thousand")


def q12(table, item):
    regions = cg.labels(table)
    egg = cg.col(table, PPM_EGG)
    shell = cg.col(table, SHELL)
    chicks = cg.col(table, CHICKS)
    order = [r for _, r in sorted(zip(egg, regions))]
    assert order == [r for _, r in sorted(zip(shell, regions), reverse=True)], \
        f"shell thickness does not run opposite to the egg concentration: {egg} {shell}"
    assert order == [r for _, r in sorted(zip(chicks, regions), reverse=True)], \
        f"hatching success does not run opposite to the egg concentration: {chicks}"
    hi = egg.index(max(egg))
    assert shell[hi] == min(shell) and chicks[hi] == min(chicks), \
        "the most contaminated region does not have the thinnest shells and fewest chicks"
    assert len(set(shell)) == len(shell), "'the same thickness everywhere' must be false"
    return (f"ranking the regions by egg concentration gives {order}, the reverse of the "
            "order by shell thickness and by chicks hatched")


def q15(table, item):
    steps = cg.labels(table)
    fat = cg.col(table, FATSOL)
    wat = cg.col(table, WATSOL)
    assert all(fat[i] < fat[i + 1] for i in range(len(fat) - 1)), \
        f"the fat soluble compound does not rise at every step: {fat}"
    assert max(fat) / min(fat) > 100, \
        f"the fat soluble compound does not rise steeply across the chain: {fat}"
    assert max(wat) / min(wat) < 1.2, \
        f"the water soluble compound does not stay near one value: {wat}"
    return (f"across {steps} the fat soluble values run {fat}, a factor of "
            f"{max(fat) / min(fat):.0f}, while the water soluble values stay between "
            f"{min(wat)} and {max(wat)}")


def q18(table, item):
    groups = cg.labels(table)
    meals = cg.col(table, MEALS)
    hair = cg.col(table, HAIR)
    order = [g for _, g in sorted(zip(meals, groups))]
    assert order == [g for _, g in sorted(zip(hair, groups))], \
        f"the order by meals does not match the order by measured mercury: {meals} {hair}"
    assert hair[meals.index(min(meals))] == min(hair), \
        "'the group eating none shows the highest concentration' must be false"
    assert len(set(hair)) == len(hair), "'the same in all four groups' must be false"
    return (f"ranking the groups by meals eaten gives {order}, the same order as ranking "
            "them by the mercury measured")


CLAIMS = [
 ("selective absorption and concentration of elements or compounds by cells inside a single living organism",
  "STB-3.I.1 near verbatim: bioaccumulation is the selective absorption and concentration of elements or compounds by cells in a living organism. The swapped distractor states STB-3.I.2, biomagnification, which is a rise across trophic levels, so the anchor carries both the process and the single-organism clause."),
 ("increase in concentration of substances per unit of body tissue that occurs at successively higher trophic levels",
  "STB-3.I.2 near verbatim: biomagnification is the increase in concentration of substances per unit of body tissue that occurs in successively higher trophic levels of a food chain or in a food web. The swapped distractor states STB-3.I.1."),
 ("rises at every step from the water to the top consumer",
  "Recomputed in q3 above: every row carries a larger value than the row above it, the water is the smallest and the top consumer the largest. STB-3.I.2 describes exactly that increase at successively higher trophic levels."),
 ("DDT, mercury and PCBs",
  "STB-3.J.3 names DDT, mercury and PCBs as substances that bioaccumulate and have significant environmental impacts. Nutrients, greenhouse gases, air pollutants and common ions belong to other statements."),
 ("Eggshell thinning and developmental deformities in top carnivores",
  "STB-3.J.1 verbatim: effects that can occur when a persistent substance is biomagnified include eggshell thinning and developmental deformities in top carnivores of the higher trophic levels. The rejected options reverse the effect or invent one."),
 ("higher the concentration in its fatty tissue, which is accumulation within individual organisms",
  "Recomputed in q6 above: the concentration rises at every step as the age rises, within one population at one trophic level. STB-3.I.1 describes that build-up as absorption and concentration by cells in a living organism."),
 ("The reproductive, nervous and circulatory systems",
  "STB-3.J.2 states that humans also experience harmful effects from biomagnification, including issues with the reproductive, nervous and circulatory systems. The framework names no other systems here and does not exempt humans."),
 ("Fat soluble compounds",
  "STB-3.I.1 states that bioaccumulation most commonly involves fat-soluble compounds. Each rejected option names a property that would work against retention in tissue."),
 ("About 50,000 times higher",
  "Recomputed in q9 above: the top consumer's concentration divided by the concentration in the water is a factor nearest fifty thousand among the decades offered. STB-3.I.2 makes the increase compound from one trophic level to the next."),
 ("Bioaccumulation is a build-up within one organism, while biomagnification is a rise in concentration from each trophic level to the next",
  "STB-3.I.1 places bioaccumulation inside a living organism and STB-3.I.2 places biomagnification across successively higher trophic levels. The distractor is the exact swap, so the anchor carries both halves of the distinction rather than either term alone."),
 ("animals at the top of the chain carry the highest concentrations",
  "STB-3.I.2 makes the concentration increase at successively higher trophic levels and STB-3.J.1 places the eggshell thinning and deformities in top carnivores of the higher trophic levels. The rejected options reverse that gradient."),
 ("thinnest shells and the fewest chicks hatched",
  "Recomputed in q12 above: ranking the regions by the concentration in the eggs gives the reverse of the order by shell thickness and by chicks hatched. STB-3.J.1 names eggshell thinning as an effect in top carnivores."),
 ("Does the concentration of the pollutant per unit of body tissue increase from plankton to small fish to predatory fish",
  "STB-3.I.2 states biomagnification as a measurable increase in concentration per unit of body tissue across successively higher trophic levels, so a question naming those levels and that quantity is answerable by measurement. The rejected options ask for a value judgment or a policy choice."),
 ("Bioaccumulation, because the concentration is building up inside one organism",
  "STB-3.I.1 describes absorption and concentration by cells in a living organism, which is what a record from a single bird shows. The distractor is the swap, so the anchor carries the process name together with the single-organism clause."),
 ("fat soluble compound rises steeply from step to step while the water soluble compound stays near the same value",
  "Recomputed in q15 above: the fat soluble column rises by more than a hundredfold across the chain while the water soluble column stays within a fifth of its own range. STB-3.I.1 makes fat-soluble compounds the common case and STB-3.I.2 supplies the rise across levels."),
 ("Biomagnification, because the concentration per unit of tissue rises at each higher trophic level",
  "STB-3.I.2 defines biomagnification as the increase in concentration per unit of body tissue at successively higher trophic levels, which is what a comparison across three species shows. The distractor is the swap, so the anchor carries both the term and the across-levels clause."),
 ("held in the body's fatty tissue rather than being carried away in watery wastes",
  "STB-3.I.1 states that bioaccumulation most commonly involves fat-soluble compounds absorbed and concentrated by cells, so the compound is retained rather than removed. The rejected options describe removal or destruction."),
 ("more meals of predatory fish a group eats, the higher the concentration",
  "Recomputed in q18 above: ranking the groups by meals eaten gives the same order as ranking them by the mercury measured. STB-3.I.2 places the highest concentrations at higher trophic levels and STB-3.J.2 states that humans experience harmful effects from biomagnification."),
 ("higher concentration per unit of tissue than the smaller fish they eat",
  "STB-3.I.2 requires a comparison across successively higher trophic levels, which only the keyed observation makes. Each rejected observation concerns one organism or one compartment and therefore speaks to STB-3.I.1 or to nothing."),
 ("organisms from several trophic levels of the same food web at the same time",
  "STB-3.I.2 defines biomagnification across trophic levels, so the design must sample several levels of one web and express the result per unit of tissue. A single species, a biomass total, a boat count and a depth survey cannot show a gradient."),
 ("eat organisms from high trophic levels and so take in the concentrations",
  "STB-3.I.2 places the highest concentrations at the higher trophic levels and STB-3.J.2 states that humans also experience harmful effects from biomagnification, including reproductive, nervous and circulatory issues."),
 ("Biomagnification, paired with a rise in concentration from prey to predator",
  "STB-3.I.2 makes biomagnification the increase across successively higher trophic levels, so a prey to predator rise is its observation, while STB-3.I.1 makes bioaccumulation the build-up within an organism. One distractor pairs the same observation with the other term, so the anchor carries the term as well as the observation."),
 ("increase in concentration per unit of body tissue, so body size does not account for it",
  "STB-3.I.2 states the increase as one of concentration per unit of body tissue, which is already corrected for how much tissue an animal carries, so a larger body does not by itself produce the pattern."),
 ("higher concentrations of the compound in their eggs consistently have thinner shells",
  "STB-3.J.1 names eggshell thinning in top carnivores as an effect of a biomagnified persistent substance, so a within-population relationship between the measured concentration and the measured thickness tests the claim. Production totals and nesting habits do not."),
 ("remains intact rather than breaking down is still present to be passed from prey to predator",
  "STB-3.J.1 frames its effects around a persistent substance being biomagnified in a food chain, and STB-3.H.1 states that persistent organic pollutants do not easily break down. A compound that degraded quickly would not remain to climb the chain."),
 ("Concentrations fall at each higher trophic level",
  "STB-3.I.2 states that concentrations increase, not fall, at successively higher trophic levels, so this is the one option the framework denies. The four rejected options restate STB-3.I.1, STB-3.I.2, STB-3.J.3 and STB-3.J.2 correctly."),
 ("held in the same water for longer will show higher tissue concentrations",
  "STB-3.I.1 describes bioaccumulation as absorption and concentration by cells in a living organism, so comparing exposure durations within the same organism tests it directly. The rejected statements state a value, a policy or an unmeasurable comparison."),
 ("Absorption and concentration by the cells of each organism, together with an increase from each trophic level to the next",
  "STB-3.I.1 supplies the uptake and retention inside each organism and STB-3.I.2 supplies the rise from one trophic level to the next, and together they place a top predator far above the water it lives in."),
 ("compared with the concentration in the water or food it takes in",
  "STB-3.I.1 describes bioaccumulation as selective absorption and concentration by cells, so the test is whether the tissue value stands above the value in the surrounding water or food. Flow rate, abundance, temperature and body length do not answer that."),
 ("rises at each higher trophic level, producing eggshell thinning and deformities in top carnivores",
  "Each clause of the keyed summary is one of STB-3.I.1, STB-3.I.2, STB-3.J.1 and STB-3.J.2. Every rejected summary reverses the gradient, denies the effects, or conflates the two processes."),
]

TABLE_CHECKS = {3: q3, 6: q6, 9: q9, 12: q12, 15: q15, 18: q18}

es.run(e8_8, CLAIMS, TABLE_CHECKS, sys.argv)
