"""Key audit for AP ENVIRONMENTAL SCIENCE 7.4 Atmospheric Particulates.

One (anchor, claim) per item, in module order; the anchor must appear in the
keyed choice and in no distractor. `cg_check.check` is the structural gate and
`es_check` carries the notation gate and the negative control.

THE TITLE. The module's TOPIC string is taken verbatim from
ENV_SCI_topics.json, which reads "Atmospheric Particulates". The CED heading is
"Atmospheric CO2 and Particulates" and its learning objective STB-2.D covers
both, so the module covers both. Flagged for the coordinator rather than
corrected here, because the exported topic code must match the topic list.

WHAT THE KEYS REST ON
---------------------
Items 1, 2, 4, 6, 11, 14, 18, 19, 21, 26 and 28 rest on STB-2.D.1: carbon
dioxide appears naturally in the atmosphere from sources such as respiration,
decomposition, and volcanic eruptions.
Items 7, 8, 9, 10, 17 and 22 rest on STB-2.D.2: there are a variety of natural
sources of particulate matter. That statement names NO natural source, so no
key here requires a student to recall one. Where an item sorts a source, the
stem states whether human activity is involved, and every rejected option is a
source the framework itself attributes to human activity -- coal and fossil
fuel combustion under STB-2.A.1 and STB-2.A.2, and the human-made indoor
pollutants of STB-2.E.5.
Items 3, 5, 12, 13, 15, 16, 20, 23, 24, 25, 27, 29 and 30 rest on suggested
skill 4.C, describe an aspect of a research method, design, and/or measure
used, applied to studies of those sources. Their keys turn on the logic of a
control, of a held-constant condition, or of what a unit reports -- not on a
course fact beyond the two statements above.

WHAT IS NOT CLAIMED. No named volcano, no named region, no global source share,
and no quantity a student would have to remember. The greenhouse behaviour of
carbon dioxide belongs to unit 9 and is not touched here.

DATA ITEMS: 2, 4, 6, 8, 11 and 13 carry tables and each keyed reading is
recomputed below from the table alone.

NEGATIVE CONTROL: `python3 verify_e7_4.py --selftest`.
"""
import sys

import cg_check as cg
import es_check as es
import e7_4

JAR = "Carbon dioxide in the jar after six hours (parts per million)"
CHAMBER = "Carbon dioxide added to the chamber air in 24 hours (parts per million)"
ERUPT = "Carbon dioxide at a downwind station (parts per million above background)"
PM = "Particulate matter measured (micrograms per cubic meter)"
FAR = "Distance to the nearest road or building (kilometers)"
CO2_M = "Average carbon dioxide (parts per million)"
SOIL = "Average soil temperature (degrees Celsius)"
HOURS = "Hours the pump ran"
MASS = "Mass of particles collected (milligrams)"


def q2(table, item):
    vals = dict(zip(cg.labels(table), cg.col(table, JAR)))
    live, stones, air = vals["Jar 1"], vals["Jar 2"], vals["Jar 3"]
    assert live > 4 * max(stones, air), \
        f"the animal jar {live} is not far above the two comparisons {stones} and {air}"
    assert abs(stones - air) < 0.05 * air, "the two comparison jars should stay close together"
    assert live != stones and live != air, "'all three the same' must be false"
    assert stones < live, "'the stones gained the most' must be false"
    assert air < live, "'air alone gained more than the animals' must be false"
    return (f"the jar of animals reads {live:.0f} parts per million against {stones:.0f} "
            f"for stones and {air:.0f} for air alone, more than four times either")


def q4(table, item):
    vals = dict(zip(cg.labels(table), cg.col(table, CHAMBER)))
    live, sterile, empty = vals["Chamber 1"], vals["Chamber 2"], vals["Chamber 3"]
    assert live > 10 * sterile, f"the living chamber {live} is not far above the sterile {sterile}"
    assert live > empty and sterile > empty, "the empty chamber should be the smallest gain"
    assert sterile < live, "'sterilized above untreated' must be false"
    assert len({live, sterile, empty}) == 3, "'equal in all three' must be false"
    return (f"the chamber with decomposers gained {live:.0f} parts per million against "
            f"{sterile:.0f} sterilized and {empty:.0f} empty, more than ten times the sterile gain")


def q6(table, item):
    weeks = cg.labels(table)
    flag = {r[0]: r[2] for r in table["rows"]}
    vals = dict(zip(weeks, cg.col(table, ERUPT)))
    assert set(flag.values()) <= {"yes", "no"}, f"the eruption column is not yes or no: {flag}"
    with_e = [w for w in weeks if flag[w] == "yes"]
    without = [w for w in weeks if flag[w] == "no"]
    assert with_e and without, "both kinds of week must appear"
    assert min(vals[w] for w in with_e) > 5 * max(vals[w] for w in without), \
        f"the eruption weeks are not far above the others: {vals}"
    assert len(set(vals.values())) > 1, "'the same in every week' must be false"
    series = [vals[w] for w in weeks]
    assert not all(series[i] < series[i + 1] for i in range(len(series) - 1)), \
        "'rose steadily from first to last' must be false"
    return (f"the eruption weeks read {[vals[w] for w in with_e]} above background against "
            f"{[vals[w] for w in without]} in the other weeks, more than five times larger")


def q8(table, item):
    sites = cg.labels(table)
    far = cg.col(table, FAR)
    pm = cg.col(table, PM)
    remote = sites[far.index(max(far))]
    assert remote == "Remote island station", f"the most remote site is {remote}"
    assert pm[sites.index(remote)] == min(pm), "the remote site does not hold the smallest value"
    assert min(pm) > 0, "'absent from the remote site' must be false"
    assert len(set(pm)) == len(pm), "'identical at all three sites' must be false"
    return (f"the most remote site reads {min(pm):.0f} micrograms per cubic meter, the "
            f"smallest of {pm} and still above zero")


def q11(table, item):
    months = cg.labels(table)
    soil = cg.col(table, SOIL)
    co2 = cg.col(table, CO2_M)
    assert [m for _, m in sorted(zip(soil, months))] == \
           [m for _, m in sorted(zip(co2, months))], "the two rankings differ"
    assert co2[soil.index(max(soil))] == max(co2), "the warmest month does not hold the largest value"
    assert co2[soil.index(min(soil))] == min(co2), "the coldest month does not hold the smallest value"
    assert len(set(co2)) == len(co2), "'the same in every month' must be false"
    return (f"ranking by soil temperature and by carbon dioxide both give "
            f"{[m for _, m in sorted(zip(soil, months))]}, so the warmest month carries the largest value")


def q13(table, item):
    hours = cg.col(table, HOURS)
    mass = cg.col(table, MASS)
    rates = [m / h for h, m in zip(hours, mass)]
    assert max(rates) - min(rates) < 1e-9, f"the mass is not proportional to time: {rates}"
    assert mass[hours.index(min(hours))] == min(mass), \
        "'the shortest run collected the most' must be false"
    assert len(set(mass)) == len(mass), "'the same on every filter' must be false"
    assert mass[hours.index(max(hours))] == max(mass), "'mass falls as time rises' must be false"
    return (f"every filter collected {rates[0]:.2f} milligrams per hour, so mass runs "
            f"{mass} in step with the running times {hours}")


CLAIMS = [
 ("Respiration, decomposition, and volcanic eruptions",
  "STB-2.D.1 verbatim: carbon dioxide appears naturally in the atmosphere from sources such as respiration, decomposition, and volcanic eruptions. The rejected lists are the human combustion sources of STB-2.A, manufactured chemicals, the indoor pollutants of STB-2.E, and the smog reaction of STB-2.B.1."),
 ("jar holding living animals gained far more carbon dioxide",
  "Recomputed in q2 above: the jar with organisms reads more than four times either comparison jar, and the two comparisons sit within a few parts per million of each other. Respiration is one of the natural sources named in STB-2.D.1."),
 ("comparison showing what the measurement gives when the proposed source is absent",
  "Suggested skill 4.C, describe an aspect of a research method or design. A control establishes the value the measurement takes with the proposed cause removed, which is what licenses attributing the difference to that cause; it neither supplies the substance nor changes what is measured."),
 ("accumulated where decomposers were present and barely accumulated where they had been killed",
  "Recomputed in q4 above: the chamber with living soil organisms gained more than ten times the sterilized litter and far more than the empty chamber. Decomposition is one of the natural sources named in STB-2.D.1."),
 ("before, during, and after the eruption",
  "Suggested skill 4.C. Attributing a change to an event requires measurements bracketing it, since a single reading during the event has nothing to be compared against. STB-2.D.1 names volcanic eruptions as a natural source, which is the claim such a design would test."),
 ("far higher in the weeks with a reported eruption",
  "Recomputed in q6 above: the two eruption weeks carry values more than five times the largest of the other weeks, and the series does not rise monotonically. STB-2.D.1 names volcanic eruptions among the natural sources of carbon dioxide."),
 ("variety of natural sources of particulate matter",
  "STB-2.D.2 verbatim. The statement asserts that natural sources are various; each rejected option denies either the variety or the natural origin, and the framework asserts neither of those."),
 ("lowest at the most remote site but are still measurable there",
  "Recomputed in q8 above: the site farthest from any road or building holds the smallest of the three values and that value is above zero. STB-2.D.2 accounts for material present where human activity is absent."),
 ("measured in places where no human activity occurs",
  "The claim under test allows only human release, so what refutes it is particulate matter present where people are not, which STB-2.D.2 accounts for. Urban excess, collectability on a filter, hourly variation and particle size are all compatible with the claim and so cannot refute it."),
 ("no people are present",
  "STB-2.D.2 states that natural sources of particulate matter are various, and the stem itself supplies the absence of human activity rather than asking the student to recall an unlisted natural source. Every rejected option is a source the framework attributes to human activity under STB-2.A.1, STB-2.A.2 or STB-2.E.5."),
 ("highest in the month with the warmest soil",
  "Recomputed in q11 above: ranking the months by soil temperature gives the same order as ranking them by carbon dioxide. Decomposition, a natural source named in STB-2.D.1, is the process the soil measurement tracks."),
 ("mass of particles collected from a known volume of air",
  "Suggested skill 4.C, describe a measure used. A concentration is an amount per unit volume, so the measure is the collected particle mass together with the volume of air drawn. Visible haze, an unused filter mass, a vehicle count and an air temperature each measure something else."),
 ("proportional to the time the pump ran",
  "Recomputed in q13 above: every filter collected the same mass per hour, so the collected mass tracks running time exactly. A comparison between runs therefore has to be made per unit time or per volume of air, which is the point of reporting a concentration."),
 ("whether or not people are present",
  "STB-2.D.1 lists respiration, decomposition and volcanic eruptions as natural sources, and those processes proceed independently of human activity. The gas released is the same substance released by combustion, which is why the classification is of the SOURCE rather than of the molecule."),
 ("sampling equipment and the length of the sampling period at both sites",
  "Suggested skill 4.C. A between-site difference is attributable to the air only if the sampling method is the same at both sites, which means the same equipment run for the same period. Staffing, equipment color and the timing of the write-up do not affect what is collected."),
 ("when the decomposers are absent",
  "Suggested skill 4.C applied to STB-2.D.1's decomposition. The control gives the value the measurement takes with the proposed cause removed, which is what makes the remainder attributable to the decomposers; it does not accelerate the process or replace replication."),
 ("has natural sources as well as any distant human ones",
  "STB-2.D.2 states that there are a variety of natural sources of particulate matter, which accounts for a persistent reading where human activity is absent. Nothing in the observation indicates instrument failure, and pollution is not confined to its point of release."),
 ("Decomposition of dead plant material, a natural source",
  "STB-2.D.1 names respiration, decomposition and volcanic eruptions as natural sources of carbon dioxide, while STB-2.A.1 and STB-2.A.2 attribute coal combustion and diesel exhaust to human activity. Each rejected pairing swaps one of those classifications."),
 ("Respiration by the organisms",
  "STB-2.D.1 names respiration as a natural source of carbon dioxide, and respiration is what the organisms present are doing. Plants do not burn fuel, the smog chemistry of STB-2.B.1 requires sunlight, and a thermal inversion under STB-2.C is an arrangement of outdoor air rather than a source."),
 ("accounts for the volume of air sampled",
  "Suggested skill 4.C, describe a measure used. Dividing the collected mass by the volume of air drawn removes the influence of how long the sampler ran, which is what makes two runs comparable; the size of the number and the need for a comparison site are separate matters."),
 ("continues at night in the organisms present",
  "STB-2.D.1 names respiration as a natural source of carbon dioxide and attaches no time of day to it, so it accounts for a rise through the night. Eruptions are not tied to the hour, the framework makes decomposition no daylight process, sunlight chemistry cannot run in the dark, and vegetation burns no fuel."),
 ("how much particulate matter is present in the air at a site",
  "Suggested skill 4.C. A pump and a filter measure the mass of particles in the air drawn through them at one place, so that is the question the method can answer; global source shares, future illness counts, unmeasured history and policy outcomes are outside what the measurement reports."),
 ("single variable is changed between the chambers",
  "Suggested skill 4.C. Holding every condition constant except moisture is what allows a difference in carbon dioxide release to be attributed to moisture; changing two conditions at once, changing the measured quantity, or omitting the measurement each destroys that attribution."),
 ("Repeating the sampling on many days across the year",
  "Suggested skill 4.C. A single day cannot establish whether a value is typical, so repetition across the year is the modification that addresses the limitation. Extra decimal places, an indoor site, a shorter run and an unrecorded remembered value do not."),
 ("mass of particles present in each unit volume",
  "Suggested skill 4.C, describe a measure used. Micrograms per cubic meter reports a mass in a volume and carries no information about particle counts, travel distance, running time, or which sources the particles came from."),
 ("not which processes released it",
  "STB-2.D.1 names several natural sources, all of which release the same gas, so one concentration cannot distinguish among them. The measurement is available at any station and does respond to respiration and decomposition, so the limitation is one of attribution rather than of measurement."),
 ("Simultaneous sampling at a site with heavy human activity and a site with none",
  "Suggested skill 4.C. Isolating a human contribution requires the two settings to be sampled at the same time with the same method, so that the difference reflects the setting; a different instrument, a different indoor or outdoor placement, or no air sampling at all introduces a second difference."),
 ("measured against that background",
  "STB-2.D.1 puts natural carbon dioxide into the same air that human sources release into, so any instrument reads the total. Attributing a change therefore requires the natural background to be accounted for, which is a matter of measurement rather than of the two kinds of gas being separable."),
 ("difference between the two masses",
  "Suggested skill 4.C, describe a measure used. The filter itself has mass, so only the increase during sampling belongs to the collected particles; the pair of weighings says nothing about pump speed or air volume and does not substitute for a comparison site."),
 ("describe how a study measures them",
  "Learning objective STB-2.D asks students to describe natural sources of CO2 and particulates, and suggested skill 4.C asks them to describe an aspect of a research method, design or measure. Named quantities, a global ranking, radiative chemistry and health effects belong to other statements or other topics."),
]

TABLE_CHECKS = {2: q2, 4: q4, 6: q6, 8: q8, 11: q11, 13: q13}

es.run(e7_4, CLAIMS, TABLE_CHECKS, sys.argv)
