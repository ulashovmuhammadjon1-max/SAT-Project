"""Key audit for AP ENVIRONMENTAL SCIENCE 8.12 Lethal Dose 50% (LD50).

One (anchor, claim) per item, in module order; the anchor must appear in the
keyed choice and in no distractor. `cg_check.check` is the structural gate and
`es_check` carries the notation gate and the negative control.

WHAT THE KEYS REST ON
---------------------
EIN-3.A.1 is the whole of the framework's content for this topic: lethal dose
50% (LD50) is the dose of a chemical that is lethal to 50% of the population of
a particular species. Every item either states that sentence, reasons from it,
or reads a number out of its own table:

  states it            -- items 1, 2, 20, 23;
  reasons from it      -- items 4, 6, 7, 9, 11, 13, 14, 16, 17, 19, 22, 24, 25,
                          26, 27, 29, 30;
  computed from a table -- items 3, 5, 8, 10, 12, 15, 18, 21, 28.

NOT KEYED, because the framework does not state them: no toxicity threshold, no
regulatory limit, no real chemical's LD50, no route of exposure, no sublethal
effect and no claim that a value transfers between species. Item 9 and item 13
exist precisely to refuse the safety-threshold reading, and item 27 refuses the
reading that an LD50 alone establishes harm in the field.

READABILITY OF THE DOSE TABLES. Every table that asks for an LD50 contains a
row at exactly 50 percent mortality, checked below, so the value asked for is
readable from the rows given rather than interpolated between them. The one
table with no such row is item 12, where the absence is the point and the key
says the value cannot be read.

DATA ITEMS: 3, 5, 8, 10, 12, 15, 18 and 21 carry tables and every keyed reading
is recomputed here from the table alone. Item 28 is arithmetic stated in its own
stem and needs no table.

NEGATIVE CONTROL: `python3 verify_e8_12.py --selftest`.
"""
import sys

import cg_check as cg
import es_check as es
import e8_12

DOSE = "Dose given to each group (milligrams per kilogram of body mass)"
DIED = "Percent of the group that died"
DIED_A = "Percent of species A that died"
DIED_B = "Percent of species B that died"
LD50_COL = "LD50 measured for that species (milligrams per kilogram of body mass)"
MASS = "Body mass of one individual (kilograms)"
YOUNG = "Percent of the young animals that died"
ADULT = "Percent of the adult animals that died"
D10 = "Dose at which 10 percent died (milligrams per kilogram)"
D50 = "Dose at which 50 percent died (milligrams per kilogram)"
D90 = "Dose at which 90 percent died (milligrams per kilogram)"


def _half_dose(dose, pct, label):
    """The single dose whose row records exactly half the group dying."""
    hits = [d for d, p in zip(dose, pct) if p == 50]
    assert len(hits) == 1, (
        f"{label}: {len(hits)} rows record exactly 50 percent mortality, so the LD50 is "
        f"not readable from the rows given: {list(zip(dose, pct))}")
    return hits[0]


def q3(table, item):
    dose = cg.col(table, DOSE)
    pct = cg.col(table, DIED)
    assert all(pct[i] <= pct[i + 1] for i in range(len(pct) - 1)), \
        f"mortality does not rise with dose: {pct}"
    ld50 = _half_dose(dose, pct, "the single species table")
    assert ld50 == 40, f"the row at half mortality is at {ld50}, not 40"
    for other in (20, 80, 160):
        assert other != ld50, f"{other} must not be the half mortality dose"
    return (f"the row recording exactly 50 percent mortality sits at {ld50:.0f} milligrams "
            "per kilogram, so that dose is the LD50 read from the table")


def q5(table, item):
    dose = cg.col(table, DOSE)
    a = cg.col(table, DIED_A)
    b = cg.col(table, DIED_B)
    la = _half_dose(dose, a, "species A")
    lb = _half_dose(dose, b, "species B")
    assert la < lb, f"species A does not reach half mortality first: {la} against {lb}"
    assert lb > 10 * la, f"the two LD50 values are not far apart: {la} and {lb}"
    assert la != max(dose), "'the LD50 for species A is the highest dose' must be false"
    return (f"species A reaches exactly half mortality at {la:.0f} and species B at "
            f"{lb:.0f} milligrams per kilogram, a factor of {lb / la:.0f}")


def q8(table, item):
    names = cg.labels(table)
    vals = cg.col(table, LD50_COL)
    assert len(set(vals)) == len(vals), "'all four equally toxic' must be false"
    lo = names[vals.index(min(vals))]
    hi = names[vals.index(max(vals))]
    assert lo == "Chemical W" and hi == "Chemical Z", \
        f"the smallest and largest values are {lo} and {hi}, not the first and last rows"
    mids = sorted(vals)[1:3]
    assert min(vals) < min(mids), "'the two middle values are the most toxic' must be false"
    return (f"{lo} carries the smallest value {min(vals)} and {hi} the largest "
            f"{max(vals):.0f} milligrams per kilogram")


def q10(table, item):
    species = cg.labels(table)
    ld50 = cg.col(table, LD50_COL)
    mass = cg.col(table, MASS)
    dose = ld50[0] * mass[0]
    options = [60, 20, 6.7, 600, 3]
    nearest = min(options, key=lambda o: abs(o - dose) / o)
    assert nearest == 60, f"{species[0]} gives {dose:.1f} milligrams, not nearest to 60"
    assert abs(dose - 60) < 1e-6, f"the product is {dose}, not exactly 60"
    return (f"{species[0]} at {ld50[0]:.0f} milligrams per kilogram and {mass[0]} "
            f"kilograms gives {dose:.0f} milligrams for one individual")


def q12(table, item):
    dose = cg.col(table, DOSE)
    pct = cg.col(table, DIED)
    assert max(pct) < 50, \
        f"some dose tested did reach half mortality, so the key would be wrong: {pct}"
    assert pct[dose.index(max(dose))] == max(pct), \
        "the highest dose does not produce the most deaths"
    assert min(pct) == 0, "'no dose produced zero deaths' would change the item"
    return (f"the largest mortality recorded is {max(pct):.0f} percent at the highest dose "
            f"{max(dose)}, so no row reaches the half mortality the LD50 requires")


def q15(table, item):
    dose = cg.col(table, DOSE)
    young = cg.col(table, YOUNG)
    adult = cg.col(table, ADULT)
    ly = _half_dose(dose, young, "the young animals")
    la = _half_dose(dose, adult, "the adult animals")
    assert ly < la, f"the young do not reach half mortality first: {ly} against {la}"
    assert la > 3 * ly, f"the two doses are not far apart: {ly} and {la}"
    return (f"the young reach exactly half mortality at {ly:.0f} and the adults at "
            f"{la:.0f} milligrams per kilogram")


def q18(table, item):
    chems = cg.labels(table)
    d10 = cg.col(table, D10)
    d50 = cg.col(table, D50)
    d90 = cg.col(table, D90)
    assert len(chems) == 2, f"the table does not compare exactly two chemicals: {chems}"
    for name, a, b, c in zip(chems, d10, d50, d90):
        assert a < b < c, f"{name}: the three doses are not in increasing order"
    ratio = d50[1] / d50[0]
    assert abs(ratio - 10) < 0.5, \
        f"the fifty percent doses differ by a factor of {ratio:.2f}, not ten"
    return (f"{chems[1]} reaches half mortality at {d50[1]:.0f} against {d50[0]:.0f} for "
            f"{chems[0]}, a factor of {ratio:.0f}")


def q21(table, item):
    dose = cg.col(table, DOSE)
    pct = cg.col(table, DIED)
    assert all(pct[i] <= pct[i + 1] for i in range(len(pct) - 1)), \
        f"mortality does not rise with dose: {pct}"
    ld50 = _half_dose(dose, pct, "the closely spaced table")
    assert ld50 == 100, f"the row at half mortality is at {ld50}, not 100"
    return (f"a row records exactly 50 percent mortality at {ld50:.0f} milligrams per "
            "kilogram, so no interpolation between rows is needed")


CLAIMS = [
 ("lethal to half of the population of a particular species",
  "EIN-3.A.1 verbatim in substance: lethal dose 50% is the dose of a chemical that is lethal to 50% of the population of a particular species. Each rejected option changes the fraction, reverses the meaning, or measures something other than a dose."),
 ("percentage of the exposed population that the dose kills",
  "EIN-3.A.1 defines the measure as the dose lethal to 50 percent of the population, so the number in the name is a share of the population rather than a property of the chemical or of the study."),
 ("is 40 milligrams per kilogram of body mass",
  "Recomputed in q3 above: exactly one row records 50 percent mortality and its dose is the keyed value, so the LD50 is read from the rows given rather than interpolated. EIN-3.A.1 supplies the definition."),
 ("belongs to the species it was measured in",
  "EIN-3.A.1 defines the LD50 as lethal to 50 percent of the population of a particular species, which ties the value to the species tested. The framework offers no rule for carrying it to another species."),
 ("far more toxic to species A",
  "Recomputed in q5 above: each species has exactly one row at 50 percent mortality, and the dose for the first is more than ten times smaller than the dose for the second. EIN-3.A.1 makes the smaller such dose the mark of greater toxicity to that species."),
 ("smaller dose is enough to kill half the population",
  "EIN-3.A.1 makes the LD50 the dose lethal to half the population, so a smaller value means less of the chemical reaches that outcome. Persistence, the number of systems affected and absorption rate are different quantities."),
 ("range of doses and find the dose at which half the group dies",
  "EIN-3.A.1 defines the LD50 as a dose associated with half a population dying, so the method must expose groups at several doses and locate that dose. A single individual yields no percentage."),
 ("smallest listed value is the most toxic to this species",
  "Recomputed in q8 above: the four values are distinct and the smallest and largest belong to the first and last rows. EIN-3.A.1 makes each value the dose at which half the population dies, so the smallest marks the greatest toxicity."),
 ("dose below which the chemical produces no effect of any kind",
  "EIN-3.A.1 defines the LD50 only as the dose lethal to 50 percent of the population of a particular species and says nothing about doses below it, so this is the one option that misstates the measure. The four rejected statements follow from the definition."),
 ("about 60 milligrams of the chemical",
  "Recomputed in q10 above: the first row's dose per kilogram multiplied by that individual's body mass gives exactly the keyed figure. EIN-3.A.1 defines that dose as the one lethal to half the population of the species."),
 ("how much of the chemical an organism receives",
  "EIN-3.A.1 makes the LD50 a dose of a chemical lethal to half a population, so the quantity is what reaches the organisms. Production, persistence, transport and solubility belong to other topics."),
 ("cannot be read from these data because no dose tested killed as many as half",
  "Recomputed in q12 above: the largest mortality in the table is below fifty percent, so no row records the outcome EIN-3.A.1 defines and the dose that would lies above every dose tested. Naming a tested dose would assert what the data do not show."),
 ("says nothing about what smaller doses do",
  "EIN-3.A.1 defines the LD50 as the dose lethal to 50 percent of the population and states nothing about lower doses, so treating it as a safety threshold reads into the definition something it does not contain."),
 ("Both values were measured on the same species",
  "EIN-3.A.1 ties the value to a particular species, so two values are comparable when they belong to the same species. Year, manufacturer, price and place of publication bear on none of the definition."),
 ("Half the young animals died at a dose far smaller",
  "Recomputed in q15 above: each group has exactly one row at 50 percent mortality and the dose for the young animals is more than three times smaller. EIN-3.A.1 defines that dose as the LD50 for the population tested."),
 ("property of the population tested under the conditions of the test",
  "EIN-3.A.1 defines the LD50 in terms of the population of a particular species that is exposed, so it is measured from that population rather than fixed by the chemical alone or chosen by the researchers."),
 ("not known in advance, so a range of doses is needed to find it",
  "EIN-3.A.1 defines the LD50 as a particular point on the relationship between dose and mortality, and locating that point requires observing mortality at more than one dose."),
 ("ten times larger for the second chemical than for the first",
  "Recomputed in q18 above: the second chemical's fifty percent dose divided by the first chemical's is ten. EIN-3.A.1 defines that column as the LD50 for the species tested."),
 ("does not by itself give the dose that kills half a fish population",
  "EIN-3.A.1 defines the LD50 as the dose lethal to 50 percent of the population of a particular species, so a value measured in one species is a statement about that species. The framework offers no conversion."),
 ("lethal to half of the exposed population of one species, paired with the name",
  "EIN-3.A.1 states that lethal dose 50% is the dose of a chemical that is lethal to 50% of the population of a particular species. The rejected pairings attach the name to complete lethality, fat solubility, persistence and transport, which belong to other statements."),
 ("is 100 milligrams per kilogram of body mass",
  "Recomputed in q21 above: one row records exactly 50 percent mortality and its dose is the keyed value, so no interpolation between the closely spaced rows is required."),
 ("requires a group to measure",
  "EIN-3.A.1 defines the LD50 in terms of 50 percent of the population of a particular species, and a percentage of a population cannot be observed in a single organism."),
 ("the LD50 for the beetle population tested",
  "EIN-3.A.1 defines the LD50 as the dose lethal to 50 percent of the population of a particular species, which is exactly what the team observed. The rejected statements extend the result beyond that species or describe a different quantity."),
 ("The species whose population was exposed",
  "EIN-3.A.1 defines the LD50 as belonging to a particular species, so the species is part of the reported value. Storage, staffing, timing and report length bear on none of the definition."),
 ("much smaller dose of the first chemical than of the second",
  "EIN-3.A.1 makes the LD50 the dose lethal to half the population of a species, so a smaller such dose means the outcome is reached with less material. Persistence, production, solubility and history are different properties."),
 ("separately for each species and compare the two doses",
  "EIN-3.A.1 ties the value to a particular species, so a comparison requires it to be measured in each. Assuming it carries over, counting individuals and timing persistence do not produce a comparable pair of doses."),
 ("not how much of the chemical the wild animals are actually receiving",
  "EIN-3.A.1 defines a dose associated with half a population dying, so applying it to a wild population also requires knowing the dose those animals receive. The definition says nothing about field exposure."),
 ("thousand times as much of the second chemical",
  "EIN-3.A.1 makes each value the dose lethal to half the population, and the larger value divided by the smaller gives the factor between them, which the stem's own two numbers fix. The comparison concerns the dose needed rather than any other property."),
 ("smaller than the dose reported",
  "EIN-3.A.1 defines the LD50 as the dose at which half the population dies, and the reported dose already exceeds that level of mortality, so the fifty percent point lies at a smaller dose. The framework provides no formula relating the two."),
 ("a value measured in one species does not transfer to another",
  "The keyed summary states EIN-3.A.1 together with the two consequences that follow directly from it. Every rejected summary turns the value into a safety threshold, an absorbed fraction, a species-independent constant, or a duration."),
]

TABLE_CHECKS = {3: q3, 5: q5, 8: q8, 10: q10, 12: q12, 15: q15, 18: q18, 21: q21}

es.run(e8_12, CLAIMS, TABLE_CHECKS, sys.argv)
