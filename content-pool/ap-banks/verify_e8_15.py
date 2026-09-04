"""Key audit for AP ENVIRONMENTAL SCIENCE 8.15 Pathogens and Infectious Diseases.

One (anchor, claim) per item, in module order; the anchor must appear in the
keyed choice and in no distractor. `cg_check.check` is the structural gate and
`es_check` carries the notation gate and the negative control.

WHAT THE KEYS REST ON
---------------------
  EIN-3.D.1   pathogens adapt to take advantage of new opportunities -- item 1;
  EIN-3.D.2   pathogens occur in many environments regardless of the appearance
              of sanitary conditions -- items 2, 12, 23, 29;
  EIN-3.D.3   as equatorial climate zones spread, pathogens, diseases and
              vectors move into subtropical and temperate areas -- items 3, 8,
              26;
  EIN-3.D.4   low-income areas often lack sanitary waste disposal and have
              contaminated drinking water, creating havens -- items 4, 5, 20,
              27;
  EIN-3.D.5   plague comes from the bite of an infected organism or contact
              with contaminated fluids or tissues -- items 6, 22;
  EIN-3.D.6   tuberculosis attacks the lungs and spreads by breathing in the
              bacteria from an infected person -- items 7, 24, 25, 28;
  EIN-3.D.7   malaria is parasitic, from infected mosquitoes, most often in
              sub-Saharan Africa -- items 9, 17;
  EIN-3.D.8   West Nile virus comes from bites from infected mosquitoes --
              items 10, 17, 19;
  EIN-3.D.9   SARS is a form of pneumonia transferred by inhaling or touching
              infected fluids -- items 11, 25;
  EIN-3.D.10  MERS is a viral respiratory illness transferred from animals to
              humans -- items 13, 18, 25;
  EIN-3.D.11  Zika comes from infected mosquitoes and can be transmitted through
              sexual contact -- items 14, 17, 19;
  EIN-3.D.12  cholera is a bacterial disease contracted from infected water --
              items 15, 21.
Items 16 and 30 join several of them.

SCOPE. Dysentery is keyed in 8.14 under EIN-3.C.2 and is not on this topic's
list, so no key here attributes it to anything. Sewage treatment is keyed in
8.11.

NOT KEYED: no case count for a real outbreak, no incubation period, no
treatment and no vaccine. The framework states none of them, so the data items
key only rank orders, ranges and appearances of a disease where it was absent.

DATA ITEMS: 4, 8, 12, 16, 20 and 24 carry tables and every keyed reading is
recomputed here from the table alone.

NEGATIVE CONTROL: `python3 verify_e8_15.py --selftest`.
"""
import sys

import cg_check as cg
import es_check as es
import e8_15

WASTE = "Households with sanitary waste disposal (percent)"
CLEANW = "Households whose drinking water is free of contamination (percent)"
CHOL = "Cholera cases per ten thousand people each year"
EARLY = "Cases recorded in the earlier decade"
LATE = "Cases recorded in the later decade"
DETECT = "Percent of samples in which the pathogen was detected"
MOSQ = "Infected mosquitoes caught per trap night"
CASES = "New human cases of the mosquito borne disease each month"
INCOME = "Average household income (thousands of currency units)"
DISEASE = "Infectious disease cases per thousand people each year"
HOURS = "Hours per day people share unventilated indoor air"
TB = "Tuberculosis cases per thousand residents each year"


def q4(table, item):
    districts = cg.labels(table)
    waste = cg.col(table, WASTE)
    water = cg.col(table, CLEANW)
    chol = cg.col(table, CHOL)
    order = [d for _, d in sorted(zip(waste, districts))]
    assert order == [d for _, d in sorted(zip(water, districts))], \
        f"the two sanitation columns do not rank the districts alike: {waste} {water}"
    assert order == [d for _, d in sorted(zip(chol, districts), reverse=True)], \
        f"disease does not run opposite to sanitation: {chol}"
    worst = waste.index(min(waste))
    assert chol[worst] == max(chol) and water[worst] == min(water), \
        "the worst served district is not also the most affected"
    assert len(set(chol)) == len(chol), "'the same in all three' must be false"
    return (f"ranking the districts by sanitary waste disposal gives {order}, the same "
            "order as by clean drinking water and the reverse of the order by cholera")


def q8(table, item):
    bands = cg.labels(table)
    early = cg.col(table, EARLY)
    late = cg.col(table, LATE)
    temperate = [i for i, b in enumerate(bands) if "temperate" in b.lower()][0]
    sub = [i for i, b in enumerate(bands) if "subtropical" in b.lower()][0]
    assert early[temperate] == 0 and late[temperate] >= 100, \
        f"the temperate band did not go from none to hundreds: {early[temperate]} to {late[temperate]}"
    assert late[sub] > 10 * early[sub], \
        f"the subtropical band did not rise many times over: {early[sub]} to {late[sub]}"
    assert any(e > 0 for i, e in enumerate(early) if i != temperate), \
        "no band other than the temperate one recorded early cases"
    return (f"the temperate band moves from {early[temperate]:.0f} to {late[temperate]:.0f} "
            f"cases and the subtropical band from {early[sub]:.0f} to {late[sub]:.0f}, a "
            f"factor of {late[sub] / early[sub]:.0f}")


def q12(table, item):
    sites = cg.labels(table)
    looks = [str(r[1]).strip().lower() for r in table["rows"]]
    pct = cg.col(table, DETECT)
    assert len(set(looks)) == len(looks), f"the appearance ratings are not distinct: {looks}"
    assert any("clean" in l for l in looks) and any("poorly" in l for l in looks), \
        f"the ratings do not span clean to poorly kept: {looks}"
    assert min(pct) > 0, "the site that looks clean must not be free of the pathogen"
    assert max(pct) < 100, "'detected in every sample' must be false"
    assert max(pct) - min(pct) <= 0.4 * min(pct), \
        f"the detection rates are not broadly similar: {pct}"
    return (f"across sites rated from clean to poorly kept the detection rates are {pct} "
            f"percent, a spread of only {max(pct) - min(pct):.0f} points")


def q16(table, item):
    areas = cg.labels(table)
    mosq = cg.col(table, MOSQ)
    cases = cg.col(table, CASES)
    order = [a for _, a in sorted(zip(mosq, areas))]
    assert order == [a for _, a in sorted(zip(cases, areas))], \
        f"the order by infected mosquitoes does not match the order by cases: {mosq} {cases}"
    assert cases[mosq.index(min(mosq))] == min(cases), \
        "'the area with the fewest mosquitoes recorded the most cases' must be false"
    assert len(set(cases)) == len(cases), "'the same in every area' must be false"
    return (f"ranking the areas by infected mosquitoes caught gives {order}, the same "
            "order as ranking them by new human cases")


def q20(table, item):
    hoods = cg.labels(table)
    inc = cg.col(table, INCOME)
    waste = cg.col(table, WASTE)
    dis = cg.col(table, DISEASE)
    order = [h for _, h in sorted(zip(inc, hoods))]
    assert order == [h for _, h in sorted(zip(waste, hoods))], \
        f"income and sanitation do not run together: {inc} {waste}"
    assert order == [h for _, h in sorted(zip(dis, hoods), reverse=True)], \
        f"disease does not run opposite to income: {dis}"
    poor = inc.index(min(inc))
    assert waste[poor] == min(waste) and dis[poor] == max(dis), \
        "the lowest income neighborhood is not the least served and most affected"
    return (f"ranking the neighborhoods by income gives {order}, the same order as by "
            "sanitary waste disposal and the reverse of the order by disease")


def q24(table, item):
    settings = cg.labels(table)
    hours = cg.col(table, HOURS)
    tb = cg.col(table, TB)
    order = [s for _, s in sorted(zip(hours, settings))]
    assert order == [s for _, s in sorted(zip(tb, settings))], \
        f"the order by shared indoor hours does not match the order by cases: {hours} {tb}"
    assert tb[hours.index(min(hours))] == min(tb), \
        "'the setting with the fewest shared hours has the highest rate' must be false"
    assert len(set(tb)) == len(tb), "'the same rate in every setting' must be false"
    return (f"ranking the settings by hours of shared unventilated air gives {order}, the "
            "same order as ranking them by tuberculosis rate")


CLAIMS = [
 ("adapt to take advantage of new opportunities to infect and spread",
  "EIN-3.D.1 verbatim: pathogens adapt to take advantage of new opportunities to infect and spread through human populations. Each rejected option denies that adaptation or the spread it allows."),
 ("regardless of how sanitary the conditions appear",
  "EIN-3.D.2 states that specific pathogens can occur in many environments regardless of the appearance of sanitary conditions, so appearance is not a reliable guide to presence."),
 ("spread into subtropical and temperate areas where the disease has not previously been known",
  "EIN-3.D.3 states that as equatorial-type climate zones spread north and south into what are currently subtropical and temperate climate zones, pathogens, infectious diseases and any associated vectors are spreading into these areas where the disease has not previously been known to occur."),
 ("least sanitary waste disposal and the most contaminated drinking water carries by far the most disease",
  "Recomputed in q4 above: the two sanitation columns rank the districts alike and the disease column runs opposite to both. EIN-3.D.4 makes poor waste disposal and contaminated water a haven for disease and EIN-3.D.12 makes cholera waterborne."),
 ("creates havens and opportunities for infectious disease to spread",
  "EIN-3.D.4 states that poverty-stricken, low-income areas often lack sanitary waste disposal and have contaminated drinking water supplies, leading to havens and opportunities for the spread of infectious diseases."),
 ("bite of an infected organism, or through contact with contaminated fluids or tissues",
  "EIN-3.D.5 states that plague is transferred to humans via the bite of an infected organism or through contact with contaminated fluids or tissues. The rejected routes belong to EIN-3.D.6, EIN-3.D.12, the mosquito borne diseases and EIN-3.D.10."),
 ("bacterial infection that typically attacks the lungs, spread by breathing in the bacteria",
  "EIN-3.D.6 states that tuberculosis is a bacterial infection that typically attacks the lungs, spread by breathing in the bacteria from the bodily fluids of an infected person. The rejected descriptions are malaria, MERS, cholera and plague."),
 ("recorded no cases in the earlier decade recorded hundreds in the later one",
  "Recomputed in q8 above: the temperate row moves from zero to at least a hundred cases and the subtropical row rises more than tenfold. EIN-3.D.3 describes exactly that movement into areas where the disease was not previously known."),
 ("parasitic disease caused by bites from infected mosquitoes, most often found in sub-Saharan Africa",
  "EIN-3.D.7 states that malaria is a parasitic disease caused by bites from infected mosquitoes and is most often found in sub-Saharan Africa. The rejected descriptions are cholera, MERS, tuberculosis and SARS."),
 ("By bites from infected mosquitoes",
  "EIN-3.D.8 states that West Nile virus is transmitted to humans via bites from infected mosquitoes. Water, air, animal tissues and food are the routes the framework gives for other diseases on this list."),
 ("form of pneumonia transferred by inhaling or touching infected fluids",
  "EIN-3.D.9 states that severe acute respiratory syndrome is a form of pneumonia transferred by inhaling or touching infected fluids. The rejected descriptions belong to malaria, cholera, plague and Zika."),
 ("detected at broadly similar rates at all three sites",
  "Recomputed in q12 above: the three detection percentages differ by less than forty percent of the smallest, across ratings spanning clean to poorly kept, and none is zero or complete. EIN-3.D.2 is the statement that appearance is no guide."),
 ("viral respiratory illness that is transferred from animals to humans",
  "EIN-3.D.10 states that Middle East Respiratory Syndrome is a viral respiratory illness that is transferred from animals to humans. Tuberculosis, malaria, cholera and plague have different descriptions."),
 ("Bites from infected mosquitoes, and transmission through sexual contact",
  "EIN-3.D.11 states that Zika is a virus caused by bites from infected mosquitoes and that it can be transmitted through sexual contact, so the framework gives this disease two routes."),
 ("bacterial disease that is contracted from infected water",
  "EIN-3.D.12 states that cholera is a bacterial disease that is contracted from infected water. The rejected descriptions belong to MERS, malaria, tuberculosis and SARS."),
 ("caught the most infected mosquitoes recorded the most new human cases",
  "Recomputed in q16 above: ranking the areas by infected mosquitoes caught gives the same order as ranking them by new human cases. EIN-3.D.7, EIN-3.D.8 and EIN-3.D.11 attribute malaria, West Nile virus and Zika to bites from infected mosquitoes."),
 ("Malaria, West Nile virus and Zika",
  "EIN-3.D.7, EIN-3.D.8 and EIN-3.D.11 each give bites from infected mosquitoes. Cholera is waterborne, tuberculosis and SARS spread from infected people, plague comes from an infected organism and MERS from animals."),
 ("Middle East Respiratory Syndrome",
  "EIN-3.D.10 states that MERS is a viral respiratory illness transferred from animals to humans. Cholera comes from infected water, tuberculosis and SARS from an infected person, and Zika from mosquitoes or sexual contact."),
 ("Zika, which can also be transmitted through sexual contact",
  "EIN-3.D.11 gives Zika two routes, bites from infected mosquitoes and sexual contact, while EIN-3.D.7 and EIN-3.D.8 give malaria and West Nile virus only the mosquito route."),
 ("lowest income has the least sanitary waste disposal and the most infectious disease",
  "Recomputed in q20 above: ranking the neighborhoods by income gives the same order as by sanitation coverage and the reverse of the order by disease. EIN-3.D.4 makes low-income areas havens through poor waste disposal and contaminated water."),
 ("Cholera",
  "EIN-3.D.12 states that cholera is a bacterial disease contracted from infected water. Malaria and West Nile virus come from mosquitoes, tuberculosis from breathing infected droplets, and MERS from animals."),
 ("Plague can be transferred through contact with contaminated fluids or tissues",
  "EIN-3.D.5 states that plague is transferred to humans via the bite of an infected organism or through contact with contaminated fluids or tissues, which covers handling an infected animal. The rejected statements name water, human droplets and mosquitoes."),
 ("occur in many environments regardless of the appearance of sanitary conditions",
  "EIN-3.D.2 states that specific pathogens can occur in many environments regardless of the appearance of sanitary conditions, which is exactly the inference the officer draws from appearance."),
 ("more hours people share unventilated indoor air, the higher the tuberculosis rate",
  "Recomputed in q24 above: ranking the settings by hours of shared unventilated air gives the same order as ranking them by case rate. EIN-3.D.6 states that tuberculosis spreads by breathing in the bacteria from an infected person."),
 ("Tuberculosis, severe acute respiratory syndrome and Middle East Respiratory Syndrome",
  "EIN-3.D.6 calls tuberculosis an infection that typically attacks the lungs, EIN-3.D.9 calls SARS a form of pneumonia, and EIN-3.D.10 calls MERS a viral respiratory illness. The rejected sets mix in waterborne and mosquito borne diseases."),
 ("vectors are spreading into areas where the disease has not previously been known to occur as equatorial climate zones expand",
  "EIN-3.D.3 states that as equatorial-type climate zones spread north and south, pathogens, infectious diseases and any associated vectors are spreading into these areas where the disease has not previously been known to occur."),
 ("often lack sanitary waste disposal and have contaminated drinking water, which gives pathogens opportunities",
  "EIN-3.D.4 attributes the havens and opportunities to the lack of sanitary waste disposal and to contaminated drinking water supplies rather than to any other feature of those areas."),
 ("Tuberculosis, paired with breathing in bacteria from the bodily fluids of an infected person",
  "EIN-3.D.6 gives tuberculosis its airborne route from an infected person, EIN-3.D.12 gives cholera water, EIN-3.D.7 gives malaria mosquitoes, EIN-3.D.11 gives Zika mosquitoes and sexual contact, and EIN-3.D.5 gives plague an infected organism. Each rejected pairing crosses two."),
 ("site which appears sanitary is reliably free of pathogens",
  "EIN-3.D.2 states the opposite, that specific pathogens can occur in many environments regardless of the appearance of sanitary conditions, so this is the option the framework denies. The four rejected options restate EIN-3.D.1, EIN-3.D.3, EIN-3.D.4 and EIN-3.D.10."),
 ("poor sanitation and contaminated water give them havens",
  "Each clause of the keyed summary is one of EIN-3.D.1 through EIN-3.D.12. Every rejected summary denies the appearance statement, collapses every route into one, denies the role of sanitation, or denies animal to human transfer."),
]

TABLE_CHECKS = {4: q4, 8: q8, 12: q12, 16: q16, 20: q20, 24: q24}

es.run(e8_15, CLAIMS, TABLE_CHECKS, sys.argv)
