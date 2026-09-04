"""Key audit for AP ENVIRONMENTAL SCIENCE 9.8 Invasive Species.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. ``claim`` states what the key rests on, for a human to audit.

WHAT THE KEYS REST ON
---------------------
  EIN-4.A.1  invasive species can live, and sometimes thrive, outside of their
             normal habitat; they can sometimes be beneficial, but they are
             considered invasive when they threaten native species
                 -- items 1, 2, 3, 9, 10, 11, 12, 13, 15, 17, 18, 20, 27, 28,
                    29, 30
  EIN-4.A.2  invasive species are often generalist, r-selected species and
             therefore may outcompete native species for resources
                 -- items 4, 5, 6, 11, 14, 19, 21, 22, 23, 24, 30
  EIN-4.A.3  invasive species can be controlled through a variety of human
             interventions -- items 7, 8, 11, 16, 25, 26, 30

EIN-4.A.3 NAMES NO INTERVENTION, AND NEITHER DOES ANY KEY HERE. The statement
says only that invasive species can be controlled through a variety of human
interventions, and the framework lists none anywhere in this unit. Item 8 keys
that absence outright, and the control programme in items 25 and 26 is recorded
without a method, so its keyed conclusion is what the intervention did rather
than which method the framework endorses.

THE CRITERION IS THE THREAT TO NATIVE SPECIES. EIN-4.A.1 has three clauses and
they are kept apart: living outside the normal habitat is the setting, being
beneficial is allowed outright, and threatening native species is the criterion.
Items 9, 10, 12, 13, 20, 28 and 29 each turn on one of those separations, and
the benefit table is a full two by two -- beneficial and harmful, beneficial and
harmless, harmful without benefit, neither -- so a student cannot get the item
right by assuming the two properties move together.

THE HEDGES ARE KEPT. OFTEN and MAY in EIN-4.A.2 are keyed in item 6 rather than
hardened, and SOMETIMES in EIN-4.A.1 is what item 10 turns on in both directions:
never beneficial is wrong, and always beneficial overshoots.

BOUNDARIES. What generalist and r-selected mean, and which natives are most
adversely affected, are ERT-3.A and ERT-3.B (topics 3.1 and 3.2); the island
case is ERT-2.E.1 (topic 2.3), and no item here is set on an island. HIPPCO is
EIN-4.C.1 (topic 9.10).

NO FIGURE IS REFERENCED; ``e_check.no_figure_reference`` enforces that on every
run.

DATA ITEMS: 17 to 29 carry tables, each recomputed below from that table alone.

NEGATIVE CONTROLS run on every invocation through ``e_check.run``; ``--selftest``
adds ``es_check.selftest``, which rotates all thirty keys one at a time and
corrupts every cell of every table individually.
"""
import sys

import cg_check as cg
import e_check
import es_check as es

import e9_8

SURVIVAL = "Survival in the new range (percent of individuals in the first year)"
MULTIPLE = "Population after twenty years, as a multiple of the number released"
GROWTH = "Percent change in the introduced population over ten years"
NATIVE_SHARED = "Percent change in the native species sharing its resources"
FOODS = "Number of different food types it eats"
OFFSPRING = "Offspring produced in a year"
AGEFIRST = "Age at first reproduction (months)"
DENSITY = "Density of the introduced species (individuals per hectare)"
SHARE = "Share of the shared food taken by the introduced species (percent)"
NATIVE_DENSITY = "Density of the native species (individuals per hectare)"
YEARS = "Years of intervention completed"
AREA = "Area still occupied by the introduced species (hectares)"
NATIVE_COUNT = "Native species recorded in that area"
CROP = "Crop it pollinates (tonnes each year)"
NATIVE_HABITAT = "Percent change in the native species sharing its habitat"


def _rising(values):
    return all(values[i + 1] > values[i] for i in range(len(values) - 1))


def _falling(values):
    return all(values[i + 1] < values[i] for i in range(len(values) - 1))


def q17(table, item):
    pairs = sorted(zip(cg.col(table, SURVIVAL), cg.col(table, MULTIPLE)))
    multiples = [m for _, m in pairs]
    assert _rising(multiples), \
        f"the eventual multiple must rise with first year survival; got {pairs}"
    assert min(multiples) < 1, \
        f"one species must have fallen below the number released; got {multiples}"
    assert max(multiples) > 100, \
        f"one species must have multiplied many times over; got {multiples}"
    return (f"sorted by first year survival the eventual populations read {multiples} "
            "times the number released, running from below one to several hundred")


def q18(table, item):
    labels = cg.labels(table)
    survival = cg.col(table, SURVIVAL)
    multiple = cg.col(table, MULTIPLE)
    top = max(range(len(multiple)), key=lambda i: multiple[i])
    assert top == max(range(len(survival)), key=lambda i: survival[i]), \
        "the species reaching the largest multiple must also lead on first year survival"
    assert labels[top] == "Species 1", f"that species must be Species 1; got {labels[top]}"
    assert len([m for m in multiple if m == multiple[top]]) == 1, \
        "that largest multiple must be unique, so 'all four thrived alike' is false"
    return (f"{labels[top]} reaches {multiple[top]} times the number released, the largest "
            f"in the record, on the highest first year survival, {survival[top]:.0f} "
            "percent")


def q19(table, item):
    pairs = sorted(zip(cg.col(table, GROWTH), cg.col(table, NATIVE_SHARED)))
    natives = [n for _, n in pairs]
    assert _falling(natives), \
        f"the native change must fall as the introduced growth rises; got {pairs}"
    assert any(n > 0 for n in natives), "'every native species declined' must be false"
    assert any(n < 0 for n in natives), "'every native species increased' must be false"
    return (f"sorted by the growth of the introduced species the native changes read "
            f"{natives} percent, strictly falling and not all of one sign")


def q20(table, item):
    labels = cg.labels(table)
    natives = cg.col(table, NATIVE_SHARED)
    no_threat = [labels[i] for i, n in enumerate(natives) if n >= 0]
    assert no_threat == ["Species 4"], \
        f"exactly Species 4 must show no decline in the native species; got {no_threat}"
    return (f"the native changes read {natives} percent, of which exactly one is not a "
            f"decline, and it belongs to {no_threat[0]}")


def q21(table, item):
    trio = sorted(zip(cg.col(table, FOODS), cg.col(table, OFFSPRING),
                      cg.col(table, AGEFIRST)))
    offspring = [o for _, o, _ in trio]
    ages = [a for _, _, a in trio]
    assert _rising(offspring), f"offspring must rise with the breadth of diet; got {trio}"
    assert _falling(ages), \
        f"the age at first reproduction must fall as the diet broadens; got {trio}"
    assert len(set(cg.col(table, FOODS))) == len(cg.col(table, FOODS)), \
        "'all four eat the same number of food types' must be false"
    assert len(set(ages)) == len(ages), \
        "'all four first reproduce at the same age' must be false"
    return (f"sorted by the number of food types eaten, the offspring read {offspring} a "
            f"year, rising, and the age at first reproduction {ages} months, falling")


def q22(table, item):
    labels = cg.labels(table)
    foods = cg.col(table, FOODS)
    offspring = cg.col(table, OFFSPRING)
    ages = cg.col(table, AGEFIRST)
    top = max(range(len(foods)), key=lambda i: foods[i])
    assert top == max(range(len(offspring)), key=lambda i: offspring[i]), \
        "the broadest diet and the most offspring must fall in the same row"
    assert top == min(range(len(ages)), key=lambda i: ages[i]), \
        "that row must also carry the youngest age at first reproduction"
    assert labels[top] == "Species A", f"that species must be Species A; got {labels[top]}"
    return (f"{labels[top]} eats {foods[top]:.0f} food types, produces "
            f"{offspring[top]:.0f} offspring a year and first breeds at {ages[top]:.0f} "
            "months, leading on all three")


def q23(table, item):
    trio = sorted(zip(cg.col(table, DENSITY), cg.col(table, SHARE),
                      cg.col(table, NATIVE_DENSITY)))
    shares = [s for _, s, _ in trio]
    natives = [n for _, _, n in trio]
    assert _rising(shares), f"the share of food taken must rise with density; got {trio}"
    assert _falling(natives), f"the native density must fall as density rises; got {trio}"
    assert len(set(natives)) == len(natives), \
        "'the native species is at the same density everywhere' must be false"
    assert len(set(shares)) == len(shares), \
        "'the same share of food at all four sites' must be false"
    return (f"sorted by the density of the introduced species the share of food taken "
            f"reads {shares} percent, rising, and the native density {natives} per "
            "hectare, falling")


def q24(table, item):
    labels = cg.labels(table)
    density = cg.col(table, DENSITY)
    share = cg.col(table, SHARE)
    natives = cg.col(table, NATIVE_DENSITY)
    worst = min(range(len(natives)), key=lambda i: natives[i])
    assert worst == max(range(len(density)), key=lambda i: density[i]), \
        "the scarcest natives must sit where the introduced species is densest"
    assert worst == max(range(len(share)), key=lambda i: share[i]), \
        "that site must also be where the largest share of the food is taken"
    assert labels[worst] == "Site 4", f"that site must be Site 4; got {labels[worst]}"
    return (f"{labels[worst]} carries the densest introduced population, "
            f"{density[worst]:.0f} per hectare, the largest share of the food, "
            f"{share[worst]:.0f} percent, and the scarcest natives, {natives[worst]:.0f} "
            "per hectare")


def q25(table, item):
    years = cg.col(table, YEARS)
    area = cg.col(table, AREA)
    natives = cg.col(table, NATIVE_COUNT)
    assert _rising(years), f"the stages must run forward in time; got {years}"
    assert _falling(area), f"the area occupied must fall at every stage; got {area}"
    assert _rising(natives), f"the native count must rise at every stage; got {natives}"
    return (f"across {years[0]:.0f} to {years[-1]:.0f} years of intervention the area "
            f"occupied reads {area} hectares, falling, and the native species recorded "
            f"{natives}, rising")


def q26(table, item):
    area = cg.col(table, AREA)
    fall = area[0] - area[-1]
    assert abs(fall - 8700) < 1e-9, f"the area must fall by 8,700 hectares; got {fall}"
    assert fall > 0, "the movement must be a reduction rather than a spread"
    return (f"the area occupied runs from {area[0]:.0f} to {area[-1]:.0f} hectares, a fall "
            f"of {fall:.0f}")


def _benefit_grid(table):
    """(label, brings a benefit, threatens natives) for each row -- named, not indexed."""
    labels = cg.labels(table)
    crop = cg.col(table, CROP)
    native = cg.col(table, NATIVE_HABITAT)
    return [(lab, c > 0, n < 0) for lab, c, n in zip(labels, crop, native)]


def q27(table, item):
    grid = _benefit_grid(table)
    beneficial = [lab for lab, ben, _ in grid if ben]
    harmless = [lab for lab, _, harm in grid if not harm]
    assert len(beneficial) == 2, \
        f"exactly two rows must pollinate a crop; got {beneficial}"
    assert len(harmless) == 2, \
        f"exactly two rows must show no native decline; got {harmless}"
    combos = {(ben, harm) for _, ben, harm in grid}
    assert len(combos) == 4, \
        f"all four combinations of benefit and threat must appear; got {sorted(combos)}"
    both = [lab for lab, ben, harm in grid if ben and harm]
    assert len(both) == 1, f"exactly one row must be both beneficial and a threat; got {both}"
    return (f"the record is a full two by two: {beneficial} pollinate a crop, {harmless} "
            f"show no native decline, and {both} does both at once, so benefit and threat "
            "do not move together")


def q28(table, item):
    grid = _benefit_grid(table)
    both = [lab for lab, ben, harm in grid if ben and harm]
    assert both == ["Species Q"], \
        f"exactly Species Q must pollinate a crop and be a threat; got {both}"
    return (f"{both[0]} is the only row of the record that both pollinates a crop and sits "
            "alongside a fall in the native species")


def q29(table, item):
    grid = _benefit_grid(table)
    neither = [lab for lab, ben, harm in grid if not ben and not harm]
    assert neither == ["Species S"], \
        f"exactly Species S must pollinate no crop and pose no threat; got {neither}"
    return (f"{neither[0]} is the only row of the record that pollinates no crop and sits "
            "alongside no fall in the native species")


CLAIMS = [
 ("live, and sometimes thrive, outside of their normal habitat",
  "EIN-4.A.1, near verbatim: invasive species are species that can live, and sometimes thrive, outside of their normal habitat."),
 ("When it threatens native species",
  "EIN-4.A.1 states that invasive species can sometimes be beneficial, but that they are considered invasive when they threaten native species, which makes the threat the criterion rather than the move, the benefit or the abundance."),
 ("Beneficial",
  "EIN-4.A.1 states outright that invasive species can sometimes be beneficial, before adding the criterion that they are considered invasive when they threaten native species."),
 ("Generalist, r-selected species",
  "EIN-4.A.2, near verbatim: invasive species are often generalist, r-selected species. The rejected option is that pairing reversed on both terms."),
 ("They may outcompete native species for resources",
  "EIN-4.A.2 states that invasive species are often generalist, r-selected species and therefore may outcompete native species for resources, which puts the competitive advantage on the introduced side. The anchor carries the direction because the rejected option reverses it."),
 ("tendency and a possibility rather than a rule holding in every case",
  "The hedges OFTEN and MAY in EIN-4.A.2 mark the profile as usual rather than universal and the outcompeting as possible rather than certain, so neither is a rule and neither is dismissed."),
 ("controlled through a variety of human interventions",
  "EIN-4.A.3, near verbatim: invasive species can be controlled through a variety of human interventions, which is the whole of what the framework says about control in this topic."),
 ("names no particular one",
  "EIN-4.A.3 refers to a variety of human interventions and lists none of them anywhere in this unit, so no particular control method can be keyed to the framework. This item keys that absence rather than filling it."),
 ("reserves the label for species that threaten native species",
  "EIN-4.A.1 opens with the ability to live outside the normal habitat and then makes the label turn on threatening native species, so living elsewhere is the setting rather than the criterion."),
 ("can sometimes be beneficial",
  "EIN-4.A.1 states that invasive species can sometimes be beneficial, so a claim that they never are contradicts the statement while a claim that they always are overshoots the word SOMETIMES."),
 ("cannot be controlled once it is established",
  "EIN-4.A.3 states the opposite, that invasive species can be controlled through a variety of human interventions, and the three other rejected options restate EIN-4.A.1 and EIN-4.A.2."),
 ("the criterion for calling it invasive, a threat to native species, has not been met",
  "EIN-4.A.1 makes threatening native species the condition under which a species is considered invasive, and this account reports a wide spread outside the normal habitat without that threat."),
 ("the benefit it brings does not exempt it",
  "EIN-4.A.1 allows that invasive species can sometimes be beneficial and still makes them considered invasive when they threaten native species, so the two clauses stand together rather than cancelling one another."),
 ("often generalist and r-selected and therefore may outcompete native species",
  "EIN-4.A.2 states the profile and the consequence in a single sentence joined by THEREFORE, which is what connects the kind of species to its effect on natives."),
 ("declining alongside the spread of the introduced species",
  "EIN-4.A.1 makes the threat to native species the condition under which a species is considered invasive, so evidence of that threat bears on the criterion while evidence of survival, diet, reproduction or benefit does not."),
 ("before and during a programme of human intervention",
  "EIN-4.A.3 asserts that invasive species can be controlled through human interventions, so the evidence bearing on it follows what an intervention does to the species rather than describing its diet, its reproduction or its origin."),
 ("Some merely persisted in the new range while others multiplied many times over",
  "Recomputed in q17 above: sorting the species by first year survival leaves the eventual multiple strictly rising, from below one to several hundred times the number released. EIN-4.A.1 distinguishes living outside the normal habitat from thriving there."),
 ("Species 1, whose population reached the largest multiple",
  "Recomputed in q18 above: the largest and uniquely largest multiple belongs to the species with the highest first year survival. EIN-4.A.1's word THRIVE is what that row illustrates."),
 ("grew most are the ones alongside the largest native declines",
  "Recomputed in q19 above: sorting the introduced species by their growth leaves the change in the native species strictly falling, and the native changes are not all of one sign. EIN-4.A.2 states that invasive species may outcompete native species for resources."),
 ("Species 4, the only one alongside which the native species did not decline",
  "Recomputed in q20 above: exactly one row shows no decline in the native species sharing its resources. EIN-4.A.1 makes a species considered invasive when it threatens native species, which that row does not do."),
 ("widest range of foods also produce the most offspring and breed youngest",
  "Recomputed in q21 above: sorting the species by the number of food types they eat leaves the offspring count rising and the age at first reproduction falling, with no ties. EIN-4.A.2 states that invasive species are often generalist, r-selected species."),
 ("Species A, which eats the widest range of foods",
  "Recomputed in q22 above: the broadest diet, the largest offspring count and the youngest age at first reproduction all fall in the same row. EIN-4.A.2 attaches that generalist, r-selected profile to invasive species."),
 ("denser it takes a larger share of the food and the native species is scarcer",
  "Recomputed in q23 above: sorting the sites by the density of the introduced species leaves the share of food it takes rising and the native density falling. EIN-4.A.2 states that invasive species may outcompete native species for resources. The anchor carries both directions because the rejected option reverses both."),
 ("Site 4, where the introduced species is densest",
  "Recomputed in q24 above: the scarcest natives, the densest introduced population and the largest share of the food all fall in the same row, which is the pattern EIN-4.A.2's outcompeting describes."),
 ("area occupied by the introduced species fell and the native species recorded rose",
  "Recomputed in q25 above: across the stages the area occupied falls at every step and the native count rises at every step. EIN-4.A.3 states that invasive species can be controlled through a variety of human interventions; the record follows one such programme without naming its method."),
 ("By 8,700 hectares",
  "Recomputed in q26 above: the first and last entries of the area column differ by 8,700 hectares, downward. EIN-4.A.3 is the statement that a human intervention can bring such a reduction about."),
 ("brings a benefit and is nevertheless accompanied by a heavy decline",
  "Recomputed in q27 above: the record is a full two by two -- two rows pollinate a crop, two show no native decline, and all four combinations of the two properties appear, with exactly one row both beneficial and a threat. EIN-4.A.1 keeps the benefit and the criterion separate, which is why the two properties need not move together."),
 ("Species Q, which pollinates a crop and is accompanied by a heavy native decline",
  "Recomputed in q28 above: exactly one row both pollinates a crop and sits alongside a fall in the native species. EIN-4.A.1 makes the threat the criterion and allows the benefit at the same time."),
 ("Species S, which pollinates no crop and is accompanied by no native decline",
  "Recomputed in q29 above: exactly one row pollinates no crop and sits alongside no fall in the native species, so it meets neither the benefit nor EIN-4.A.1's criterion."),
 ("often generalist, r-selected species and may therefore outcompete natives for resources; and they can be controlled",
  "EIN-4.A.1 supplies the definition, the possible benefit and the criterion, EIN-4.A.2 the usual profile and the possible outcompeting, and EIN-4.A.3 the control through a variety of human interventions. Each rejected summary reverses a clause, drops the criterion, claims the framework names the interventions, or hardens a hedge into a rule."),
]

TABLE_CHECKS = {17: q17, 18: q18, 19: q19, 20: q20, 21: q21, 22: q22, 23: q23,
                24: q24, 25: q25, 26: q26, 27: q27, 28: q28, 29: q29}

if "--selftest" in sys.argv:
    es.selftest(e9_8, CLAIMS, TABLE_CHECKS)

e_check.run(e9_8, CLAIMS, TABLE_CHECKS)
