"""Key audit for AP ENVIRONMENTAL SCIENCE 9.9 Endangered Species.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. ``claim`` states what the key rests on, for a human to audit.

WHAT THE KEYS REST ON
---------------------
  EIN-4.B.1  a variety of factors can leave a species threatened with
             extinction, such as being extensively hunted, having limited diet,
             being outcompeted by invasive species, or having specific and
             limited habitat requirements
                 -- items 1, 2, 12, 13, 17, 18, 19, 20, 21, 22, 23, 30
  EIN-4.B.2  not all species will be in danger of extinction from the same
             changes; those able to adapt or to move are less likely to face
             extinction -- items 3, 4, 11, 12, 16, 24, 25, 30
  EIN-4.B.3  selective pressures are any factors that change the behaviors and
             fitness of organisms within an environment -- items 5, 14, 27, 30
  EIN-4.B.4  species compete for resources like territory, food, mates and
             habitat, and this competition may lead to endangerment or
             extinction -- items 6, 7, 10, 12, 26, 30
  EIN-4.B.5  strategies to protect animal populations include criminalizing
             poaching, protecting animal habitats, and legislation
                 -- items 8, 9, 12, 15, 28, 29, 30

THE OVERLAP WITH UNIT 2 AND WITH TOPIC 9.8 IS REAL AND IS HANDLED BY ANGLE.
Habitat loss removing specialists is ERT-2.A.4 (topic 2.1), adaptation by
natural selection is ERT-2.H (topic 2.6), and what an invasive species is, and
that it may outcompete natives, is EIN-4.A (topic 9.8). Every key here rests on
an EIN-4.B statement and asks about EXTINCTION RISK -- which species is
threatened, and what protects it -- rather than about a mechanism another topic
owns. No item defines an invasive species, defines a specialist, or explains
natural selection, and the invasive competitor in items 22 and 23 is followed
only through what happens to the NATIVE population.

THE HEDGES ARE KEPT. EIN-4.B.1's SUCH AS is keyed in item 17 and EIN-4.B.4's MAY
in item 10, so neither the list of factors nor the outcome of competition is
hardened. EIN-4.B.5 ranks none of its three strategies and no key here does
either; items 28 and 29 read their own record instead.

NO FIGURE IS REFERENCED; ``e_check.no_figure_reference`` enforces that on every
run.

DATA ITEMS: 18 to 29 carry tables, each recomputed below from that table alone.

NEGATIVE CONTROLS run on every invocation through ``e_check.run``; ``--selftest``
adds ``es_check.selftest``, which rotates all thirty keys one at a time and
corrupts every cell of every table individually.
"""
import sys

import cg_check as cg
import e_check
import es_check as es

import e9_9

FOODS = "Number of different foods it eats"
HABITATS = "Number of habitat types it can occupy"
DECLINE50 = "Percent decline over fifty years"
TAKEN = "Animals taken by hunters each year"
POPCHANGE = "Percent change in the population over twenty years"
YEARS_SINCE = "Years since the introduced competitor arrived"
REMAINING = "Percent of the native population remaining"
TOLERANCE = "Range of temperatures it can tolerate (degrees Celsius)"
DISPERSAL = "Distance it can disperse in one generation (kilometres)"
DECLINE_WARM = "Percent decline after the same warming"
DECLINING_SHARE = "Share of it secured by the declining species (percent)"
COMPETING_SHARE = "Share of it secured by the competing species (percent)"
BEHAVIOUR = "Percent of animals showing the changed behaviour"
OFFSPRING = "Mean number of surviving offspring per animal"
BAN_YEARS = "Years since poaching was made a crime there"
PROTECTED = "Area of protected habitat (thousands of hectares)"
ANIMAL_CHANGE = "Percent change in the protected animal population"

# EIN-4.B.4's own list, in the framework's order.
RESOURCES = ["Territory", "Food", "Mates", "Habitat"]


def _rising(values):
    return all(values[i + 1] > values[i] for i in range(len(values) - 1))


def _falling(values):
    return all(values[i + 1] < values[i] for i in range(len(values) - 1))


def q18(table, item):
    for driver in (FOODS, HABITATS):
        pairs = sorted(zip(cg.col(table, driver), cg.col(table, DECLINE50)))
        assert _falling([d for _, d in pairs]), \
            f"sorted by {driver!r} the decline must fall strictly; got {pairs}"
    declines = cg.col(table, DECLINE50)
    assert len(set(declines)) == len(declines), \
        "'every species declined by the same amount' must be false"
    return (f"sorted by the breadth of diet and then by the number of habitat types, the "
            f"declines read {sorted(declines, reverse=True)} percent, falling both times")


def q19(table, item):
    labels = cg.labels(table)
    foods = cg.col(table, FOODS)
    habitats = cg.col(table, HABITATS)
    declines = cg.col(table, DECLINE50)
    worst = min(range(len(foods)), key=lambda i: foods[i])
    assert worst == min(range(len(habitats)), key=lambda i: habitats[i]), \
        "the narrowest diet and the fewest habitat types must fall in the same row"
    assert worst == max(range(len(declines)), key=lambda i: declines[i]), \
        "that row must also carry the largest decline"
    assert labels[worst] == "Species 1", f"that species must be Species 1; got {labels[worst]}"
    return (f"{labels[worst]} eats {foods[worst]:.0f} food and occupies "
            f"{habitats[worst]:.0f} habitat type, the fewest of each, and has declined "
            f"{declines[worst]:.0f} percent, the most")


def q20(table, item):
    pairs = sorted(zip(cg.col(table, TAKEN), cg.col(table, POPCHANGE)))
    changes = [c for _, c in pairs]
    assert _falling(changes), \
        f"the population change must fall as the numbers taken rise; got {pairs}"
    assert any(c > 0 for c in changes), "'every species fell in number' must be false"
    assert any(c < 0 for c in changes), "'every species rose in number' must be false"
    return (f"sorted by the numbers hunters take, the population changes read {changes} "
            "percent, strictly falling and not all of one sign")


def q21(table, item):
    labels = cg.labels(table)
    taken = cg.col(table, TAKEN)
    changes = cg.col(table, POPCHANGE)
    rose = [labels[i] for i, c in enumerate(changes) if c > 0]
    assert rose == ["Species D"], f"exactly Species D must have risen; got {rose}"
    i = labels.index("Species D")
    assert taken[i] == min(taken), \
        "the species that did not fall must be the one taken in the smallest numbers"
    return (f"the population changes read {changes} percent, of which exactly one is a "
            f"rise, and it belongs to the species taken in the smallest numbers, "
            f"{taken[i]:.0f} a year")


def q22(table, item):
    years = cg.col(table, YEARS_SINCE)
    remaining = cg.col(table, REMAINING)
    assert _rising(years), f"the stages must run forward in time; got {years}"
    assert _falling(remaining), \
        f"the share of the native population remaining must fall at every stage; got {remaining}"
    return (f"in stage order the years since the competitor arrived read {years} and the "
            f"share of the native population remaining {remaining} percent, falling "
            "throughout")


def q23(table, item):
    labels = cg.labels(table)
    years = cg.col(table, YEARS_SINCE)
    remaining = cg.col(table, REMAINING)
    worst = min(range(len(remaining)), key=lambda i: remaining[i])
    assert worst == max(range(len(years)), key=lambda i: years[i]), \
        "the smallest surviving share must sit at the longest time since arrival"
    assert labels[worst] == "Stage 4", f"that stage must be Stage 4; got {labels[worst]}"
    assert len(set(remaining)) == len(remaining), \
        "'the native population is the same size at every stage' must be false"
    return (f"{labels[worst]} carries the longest presence, {years[worst]:.0f} years, and "
            f"the smallest surviving share, {remaining[worst]:.0f} percent")


def q24(table, item):
    for driver in (TOLERANCE, DISPERSAL):
        pairs = sorted(zip(cg.col(table, driver), cg.col(table, DECLINE_WARM)))
        assert _falling([d for _, d in pairs]), \
            f"sorted by {driver!r} the decline must fall strictly; got {pairs}"
    declines = cg.col(table, DECLINE_WARM)
    assert len(set(declines)) == len(declines), \
        "the four declines must differ, or 'the same change endangered all alike' is not refuted"
    return (f"sorted by the range of conditions tolerated and then by dispersal distance, "
            f"the declines read {sorted(declines, reverse=True)} percent, falling both "
            "times and all four different")


def q25(table, item):
    labels = cg.labels(table)
    tolerance = cg.col(table, TOLERANCE)
    dispersal = cg.col(table, DISPERSAL)
    declines = cg.col(table, DECLINE_WARM)
    best = min(range(len(declines)), key=lambda i: declines[i])
    assert best == max(range(len(tolerance)), key=lambda i: tolerance[i]), \
        "the smallest decline must belong to the widest tolerance"
    assert best == max(range(len(dispersal)), key=lambda i: dispersal[i]), \
        "it must also belong to the greatest dispersal distance"
    assert labels[best] == "Species Z", f"that species must be Species Z; got {labels[best]}"
    return (f"{labels[best]} tolerates {tolerance[best]:.0f} degrees of range and disperses "
            f"{dispersal[best]:.0f} kilometres, the widest and furthest, and has declined "
            f"{declines[best]:.0f} percent, the least")


def q26(table, item):
    labels = cg.labels(table)
    assert labels == RESOURCES, \
        f"the record must cover exactly the resources the framework names; got {labels}"
    declining = cg.col(table, DECLINING_SHARE)
    competing = cg.col(table, COMPETING_SHARE)
    for lab, d, c in zip(labels, declining, competing):
        assert d < c, f"the declining species must secure the smaller share of {lab}; got {d} and {c}"
    assert not any(d > c for d, c in zip(declining, competing)), \
        "'the declining species secured the larger share of the food' must be false"
    return (f"across {labels} the declining species secures {declining} percent against the "
            f"competitor's {competing}, the smaller share in every case")


def q27(table, item):
    behaviour = cg.col(table, BEHAVIOUR)
    offspring = cg.col(table, OFFSPRING)
    assert _rising(behaviour), \
        f"the share showing the changed behaviour must rise at every stage; got {behaviour}"
    assert _falling(offspring), \
        f"the surviving offspring must fall at every stage; got {offspring}"
    # Named booleans, so the two halves of EIN-4.B.3 cannot be read off parallel
    # lists in the wrong order -- the inverted check this project has already paid for.
    behaviour_changed = behaviour[-1] != behaviour[0]
    fitness_changed = offspring[-1] != offspring[0]
    assert behaviour_changed and fitness_changed, \
        "the factor must change both the behaviour and the fitness for it to be a selective pressure"
    return (f"in stage order the share showing the changed behaviour reads {behaviour} "
            f"percent, rising, and the surviving offspring {offspring}, falling, so both "
            "behaviour and fitness moved")


def q28(table, item):
    for driver in (BAN_YEARS, PROTECTED):
        pairs = sorted(zip(cg.col(table, driver), cg.col(table, ANIMAL_CHANGE)))
        assert _rising([c for _, c in pairs]), \
            f"sorted by {driver!r} the population change must rise strictly; got {pairs}"
    changes = cg.col(table, ANIMAL_CHANGE)
    assert any(c > 0 for c in changes), "'every country shows a fall' must be false"
    assert any(c < 0 for c in changes), "'every country shows a rise' must be false"
    return (f"sorted by the years since poaching was criminalized and then by the protected "
            f"area, the population changes read {sorted(changes)} percent, rising both "
            "times and not all of one sign")


def q29(table, item):
    labels = cg.labels(table)
    years = cg.col(table, BAN_YEARS)
    area = cg.col(table, PROTECTED)
    changes = cg.col(table, ANIMAL_CHANGE)
    best = max(range(len(changes)), key=lambda i: changes[i])
    assert best == max(range(len(years)), key=lambda i: years[i]), \
        "the largest rise must belong to the longest standing ban"
    assert best == max(range(len(area)), key=lambda i: area[i]), \
        "it must also belong to the largest protected area"
    assert labels[best] == "Country 4", f"that country must be Country 4; got {labels[best]}"
    assert len(set(changes)) == len(changes), "'all four record the same change' must be false"
    return (f"{labels[best]} has banned poaching for {years[best]:.0f} years and protects "
            f"{area[best]:.0f} thousand hectares, the most of each, and records the largest "
            f"rise, {changes[best]:.0f} percent")


CLAIMS = [
 ("extensively hunted, having a limited diet, being outcompeted by invasive species",
  "EIN-4.B.1, near verbatim: a variety of factors can lead to a species becoming threatened with extinction, such as being extensively hunted, having limited diet, being outcompeted by invasive species, or having specific and limited habitat requirements. The anchor carries three of the four because one rejected option reverses each of them in turn."),
 ("unusually long life span",
  "EIN-4.B.1 names four factors, each of which the four rejected options restates. Life span appears nowhere in this topic's statements."),
 ("Not all of them will be in danger of extinction",
  "EIN-4.B.2 opens by stating that not all species will be in danger of extinction when exposed to the same changes in their ecosystem, so one change does not carry one risk for every species present."),
 ("able to adapt to changes in their environment, or able to move to a new environment",
  "EIN-4.B.2 states that species able to adapt to changes in their environment or able to move to a new environment are less likely to face extinction, naming both routes to a lower risk. The anchor carries both because the rejected option negates both."),
 ("change the behaviours and fitness of organisms within an environment",
  "EIN-4.B.3, near verbatim: selective pressures are any factors that change the behaviors and fitness of organisms within an environment, which puts both the behaviour and the fitness in the definition."),
 ("Territory, food, mates and habitat",
  "EIN-4.B.4 states that species in a given ecosystem compete for resources like territory, food, mates, and habitat, which is the set the keyed option names in full."),
 ("Endangerment or extinction",
  "EIN-4.B.4 states that competition for those resources may lead to endangerment or extinction, and attaches no other outcome to it."),
 ("Criminalizing poaching, protecting animal habitats, and legislation",
  "EIN-4.B.5, near verbatim: strategies to protect animal populations include criminalizing poaching, protecting animal habitats, and legislation."),
 ("Introducing a competitor to reduce the protected animal's numbers",
  "EIN-4.B.5 names criminalizing poaching, protecting animal habitats and legislation, which the four rejected options restate in one wording or another. Introducing a competitor appears nowhere among them."),
 ("possible outcome of competition rather than one that always follows",
  "The word MAY in EIN-4.B.4 marks endangerment or extinction as a possible consequence of competition rather than a certain one, so the framework neither guarantees it nor excludes it."),
 ("Not all species will be in danger of extinction when exposed to the same changes",
  "EIN-4.B.2 opens with exactly that denial and explains it by pointing to the species able to adapt or to move, which are less likely to face extinction."),
 ("broad diet is more likely to become threatened than one with a limited diet",
  "EIN-4.B.1 names having limited diet, not a broad one, among the factors leading to a species becoming threatened, so the keyed option reverses the framework. The four rejected options restate EIN-4.B.1, EIN-4.B.2, EIN-4.B.4 and EIN-4.B.5."),
 ("limited diet, and having specific and limited habitat requirements",
  "EIN-4.B.1 names having limited diet and having specific and limited habitat requirements among its four factors, and the bird described carries both at once."),
 ("factor changing both the behaviours and the fitness of organisms",
  "EIN-4.B.3 defines selective pressures as any factors that change the behaviors and fitness of organisms within an environment, and the account reports a change in both. The anchor carries the direction because one rejected option keeps the label and negates the change."),
 ("Criminalizing poaching, and legislation",
  "EIN-4.B.5 names criminalizing poaching and legislation among the strategies to protect animal populations, and a law making the killing of an animal a crime is both at once."),
 ("several species of the same ecosystem fared after one and the same change",
  "EIN-4.B.2 asserts that species differ in their danger from the same change and that the ability to adapt or to move lowers it, so the evidence bearing on it compares several species under one change and measures those two abilities."),
 ("examples of a variety of factors rather than a closed list",
  "EIN-4.B.1 opens with a variety of factors and then offers four SUCH AS examples, so the list is illustrative rather than exhaustive and none of the four is dismissed."),
 ("fewest foods and the fewest habitat types declined the most",
  "Recomputed in q18 above: sorting the species by the breadth of diet, and then by the number of habitat types, leaves the decline strictly falling each time, and the four declines differ. EIN-4.B.1 names limited diet and specific and limited habitat requirements among its factors."),
 ("Species 1, which eats the fewest foods and occupies the fewest habitat types",
  "Recomputed in q19 above: the narrowest diet, the fewest habitat types and the largest decline all fall in the same row. EIN-4.B.1 names both of those properties among the factors leading to a species becoming threatened."),
 ("taken in the largest numbers fell the furthest",
  "Recomputed in q20 above: sorting the species by the numbers hunters take leaves the population change strictly falling, and the changes are not all of one sign. EIN-4.B.1 names being extensively hunted among its factors."),
 ("Species D, from which hunters take the smallest number",
  "Recomputed in q21 above: exactly one row shows a rise rather than a fall, and it is the species taken in the smallest numbers. EIN-4.B.1 names extensive hunting among the factors leading to a species becoming threatened."),
 ("the less of the native population remained",
  "Recomputed in q22 above: in stage order the years since the competitor arrived rise at every step while the share of the native population remaining falls at every step. EIN-4.B.1 names being outcompeted by invasive species among its factors."),
 ("Stage 4, at which the competitor had been present longest",
  "Recomputed in q23 above: the smallest surviving share and the longest presence fall in the same row, and the four shares differ. EIN-4.B.1 names being outcompeted by invasive species among the factors leading to a species becoming threatened."),
 ("move further fell least, so the same change did not endanger all four alike",
  "Recomputed in q24 above: sorting by the range of conditions tolerated, and then by dispersal distance, leaves the decline strictly falling each time, and the four declines differ. EIN-4.B.2 states both that the same change does not endanger every species alike and that the ability to adapt or to move lowers the risk. The anchor carries both clauses because the rejected option reverses both."),
 ("Species Z, which bears the widest range of conditions and disperses furthest",
  "Recomputed in q25 above: the widest tolerance, the greatest dispersal and the smallest decline all fall in the same row. EIN-4.B.2 states that species able to adapt or to move are less likely to face extinction."),
 ("smaller share than its competitor of every resource recorded",
  "Recomputed in q26 above: the record covers exactly territory, food, mates and habitat, the resources EIN-4.B.4 names, and in every row the declining species' share is the smaller. That statement adds that such competition may lead to endangerment or extinction."),
 ("changed both the behaviour of the animals and the number of young they raise",
  "Recomputed in q27 above: the share showing the changed behaviour rises at every stage while the surviving offspring fall at every stage, so both moved. EIN-4.B.3 defines selective pressures as any factors that change the behaviors and fitness of organisms within an environment."),
 ("criminalized poaching for longer and protect more habitat record the better outcomes",
  "Recomputed in q28 above: sorting by the years since poaching was criminalized, and then by the protected area, leaves the change in the animal population strictly rising each time, and the changes are not all of one sign. EIN-4.B.5 names both measures among the strategies to protect animal populations."),
 ("Country 4, which has criminalized poaching longest and protects the most habitat",
  "Recomputed in q29 above: the largest rise, the longest standing ban and the largest protected area all fall in the same row, and the four changes differ. EIN-4.B.5 names both measures among its strategies."),
 ("selective pressures are factors changing behaviour and fitness",
  "EIN-4.B.1 supplies the four illustrative factors, EIN-4.B.2 the difference in danger and the two things that lower it, EIN-4.B.3 the definition of a selective pressure, EIN-4.B.4 the resources competed for and the possible outcome, and EIN-4.B.5 the three strategies. Each rejected summary drops a statement, reverses one, or hardens a hedge."),
]

TABLE_CHECKS = {18: q18, 19: q19, 20: q20, 21: q21, 22: q22, 23: q23, 24: q24,
                25: q25, 26: q26, 27: q27, 28: q28, 29: q29}

if "--selftest" in sys.argv:
    es.selftest(e9_9, CLAIMS, TABLE_CHECKS)

e_check.run(e9_9, CLAIMS, TABLE_CHECKS)
