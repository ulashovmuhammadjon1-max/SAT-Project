"""Key audit for AP ENVIRONMENTAL SCIENCE 7.3 Thermal Inversion.

One (anchor, claim) per item, in module order; the anchor must appear in the
keyed choice and in no distractor. `cg_check.check` is the structural gate and
`es_check` carries the notation gate and the negative control.

WHAT THE KEYS REST ON
---------------------
The topic has two essential knowledge statements and every key here rests on
one or both:

  STB-2.C.1  during a thermal inversion the normal temperature gradient is
             altered, as the air temperature at the Earth's surface is cooler
             than the air at higher altitudes;
  STB-2.C.2  thermal inversion traps pollution close to the ground, especially
             smog and particulates.

Items 1, 2, 3, 8, 9, 10, 13, 18, 20, 21 and 28 read a profile or a definition
against STB-2.C.1. Items 4, 6, 15, 22, 23, 25 and 27 rest on STB-2.C.2. Items
5, 7, 11, 12, 14, 16, 17, 19, 24, 26, 29 and 30 join the two.

TWO CONSEQUENCES OF STB-2.C.1 ARE USED AS SUCH, and nothing else is inferred:
if the inversion is the ALTERED case in which the surface is cooler than the
air above, then the ordinary case is the surface warmer than the air above
(items 10, 18, 28), and the inversion has ended when that ordinary ordering
returns (items 12, 24).

WHAT IS NOT CLAIMED. The framework gives no cause for an inversion -- no
valley, no calm clear night, no season -- and no key or stem here supplies one.
It gives no threshold concentration, no duration and no named episode.

DATA ITEMS: 2, 3, 5, 7, 8, 11 and 14 carry tables. Every keyed reading is
recomputed below from the table alone, and the rejected readings are falsified
against the same numbers.

NEGATIVE CONTROL: `python3 verify_e7_3.py --selftest`.
"""
import sys

import cg_check as cg
import es_check as es
import e7_3

HEIGHT = "Height above the ground (meters)"
TEMP = "Air temperature (degrees Celsius)"
SO2 = "Sulfur dioxide (parts per billion)"
GROUND = "Temperature at ground level (degrees Celsius)"
AT400 = "Temperature at 400 meters (degrees Celsius)"
AT300 = "Temperature at 300 meters (degrees Celsius)"
AT200 = "Temperature at 200 meters (degrees Celsius)"
PM_HOUR = "Particulate matter at ground level (micrograms per cubic meter)"
PM_SITE = "Particulates at ground level (micrograms per cubic meter)"
SMOG = "Smog measured at ground level (parts per billion)"
PM_EP = "Particulates measured at ground level (micrograms per cubic meter)"


def _profile(table):
    return list(zip(cg.col(table, HEIGHT), cg.col(table, TEMP)))


def q2(table, item):
    prof = _profile(table)
    assert prof == sorted(prof), "the profile must be listed from the ground upward"
    surface = prof[0][1]
    top_of_rise = max(t for _, t in prof)
    assert prof[1][1] > surface and prof[2][1] > surface, \
        "temperature does not rise above the surface value in the lowest layers"
    assert not all(prof[i][1] > prof[i + 1][1] for i in range(len(prof) - 1)), \
        "'temperature falls throughout' must be false"
    assert len(set(t for _, t in prof)) > 1, "'no change with height' must be false"
    assert prof[-1][1] > surface, "'coldest at the greatest height' must be false"
    return (f"the surface reading is {surface:.0f} degrees, the column rises to "
            f"{top_of_rise:.0f} degrees aloft, and the highest sample is {prof[-1][1]:.0f} "
            "degrees, which is still warmer than the surface")


def q3(table, item):
    prof = _profile(table)
    assert prof == sorted(prof), "the profile must be listed from the ground upward"
    assert all(prof[i][1] > prof[i + 1][1] for i in range(len(prof) - 1)), \
        f"temperature does not fall at every step: {prof}"
    assert prof[0][1] == max(t for _, t in prof), "the surface must hold the warmest air"
    return (f"temperatures run {[t for _, t in prof]} from the ground upward, falling at "
            "every step, so the surface air is the warmest in the column")


def q5(table, item):
    hours = cg.labels(table)
    ground = cg.col(table, GROUND)
    aloft = cg.col(table, AT300)
    pm = cg.col(table, PM_HOUR)
    inverted = [i for i in range(len(hours)) if ground[i] < aloft[i]]
    ordinary = [i for i in range(len(hours)) if ground[i] > aloft[i]]
    assert inverted and ordinary, "the morning must contain both arrangements"
    assert min(pm[i] for i in inverted) > max(pm[i] for i in ordinary), \
        f"the inversion hours do not hold the higher particulate values: {pm}"
    assert len(set(pm)) > 1, "'the same throughout' must be false"
    assert not all(pm[i] < pm[i + 1] for i in range(len(pm) - 1)), \
        "'rise steadily through the period' must be false"
    return (f"the hours {[hours[i] for i in inverted]} have the ground cooler than the air "
            f"aloft and carry particulates {[pm[i] for i in inverted]}, above the "
            f"{[pm[i] for i in ordinary]} recorded once the ordering reverses")


def q7(table, item):
    prof = _profile(table)
    so2 = dict(zip(cg.col(table, HEIGHT), cg.col(table, SO2)))
    cap = 350.0
    below = [v for h, v in so2.items() if h < cap]
    above = [v for h, v in so2.items() if h >= cap]
    assert min(below) > 5 * max(above), \
        f"the layer below {cap:.0f} meters is not far more polluted: {below} against {above}"
    rising = [prof[i][1] < prof[i + 1][1] for i in range(len(prof) - 1)]
    assert all(rising[:3]), "the temperature must still be rising up to the capping level"
    assert not rising[-1], "the temperature must stop rising above the capping level"
    assert max(so2.values()) == so2[min(so2)], "the largest reading must be at the ground"
    return (f"sulfur dioxide runs {below} below {cap:.0f} meters against {above} above it, "
            "and the temperature rises up to that level and falls beyond it")


def q8(table, item):
    ground = dict(zip(cg.labels(table), cg.col(table, GROUND)))
    aloft = dict(zip(cg.labels(table), cg.col(table, AT400)))
    inverted = [c for c in ground if ground[c] < aloft[c]]
    assert inverted == ["City J"], f"the cities meeting the definition are {inverted}"
    assert ground["City K"] > aloft["City K"], "City K must show the ordinary ordering"
    return (f"City J reads {ground['City J']:.0f} degrees at the ground against "
            f"{aloft['City J']:.0f} aloft, while City K reads {ground['City K']:.0f} against "
            f"{aloft['City K']:.0f}, so only City J has the cooler surface")


def q11(table, item):
    sites = cg.labels(table)
    ground = cg.col(table, GROUND)
    aloft = cg.col(table, AT200)
    pm = cg.col(table, PM_SITE)
    inverted = [i for i in range(len(sites)) if ground[i] < aloft[i]]
    ordinary = [i for i in range(len(sites)) if ground[i] > aloft[i]]
    assert len(inverted) == 2 and len(ordinary) == 2, \
        f"expected two sites of each kind, got {inverted} and {ordinary}"
    assert min(pm[i] for i in inverted) > max(pm[i] for i in ordinary), \
        f"the inversion sites do not hold the two largest particulate values: {pm}"
    gaps = [abs(ground[i] - aloft[i]) for i in range(len(sites))]
    assert gaps[pm.index(max(pm))] != min(gaps), \
        "'highest where the difference is smallest' must be false"
    return (f"sites {[sites[i] for i in inverted]} have the ground cooler than the air at "
            f"200 meters and carry {[pm[i] for i in inverted]}, above the "
            f"{[pm[i] for i in ordinary]} at the other two")


def q14(table, item):
    days = cg.labels(table)
    flag = {r[0]: r[1] for r in table["rows"]}
    assert set(flag.values()) <= {"yes", "no"}, f"the inversion column is not yes or no: {flag}"
    smog = dict(zip(days, cg.col(table, SMOG)))
    pm = dict(zip(days, cg.col(table, PM_EP)))
    with_inv = [d for d in days if flag[d] == "yes"]
    without = [d for d in days if flag[d] == "no"]
    assert with_inv and without, "both kinds of day must appear"
    for series, name in ((smog, "smog"), (pm, "particulates")):
        assert min(series[d] for d in with_inv) > max(series[d] for d in without), \
            f"{name} is not higher on every inversion day: {series}"
    return (f"on {with_inv} smog reads {[smog[d] for d in with_inv]} and particulates "
            f"{[pm[d] for d in with_inv]}, both above every value recorded on {without}")


CLAIMS = [
 ("cooler than the air at higher altitudes",
  "STB-2.C.1, near verbatim: during a thermal inversion the normal temperature gradient in the atmosphere is altered as the air temperature at the Earth's surface is cooler than the air at higher altitudes. The rejected options state the ordinary arrangement, a uniform column, or no dependence on height."),
 ("temperature rises with height through the lowest few hundred meters",
  "Recomputed in q2 above from the tabulated profile: the reading at the ground is the coldest in the column and the readings above it are warmer, so the surface air is cooler than the air aloft. That is the altered gradient of STB-2.C.1."),
 ("surface air is warmer than the air above it",
  "Recomputed in q3 above: temperature falls at every step upward and the surface holds the warmest air, so the ordering is the ordinary one rather than the altered gradient of STB-2.C.1. A change with height is not by itself an inversion."),
 ("Smog and particulates",
  "STB-2.C.2, near verbatim: thermal inversion traps pollution close to the ground, especially smog and particulates. Stratospheric chemicals, the indoor pollutants of STB-2.E, the inert constituents of air, and noise under STB-2.J are not what this statement names."),
 ("hours when the ground is cooler than the air at 300 meters",
  "Recomputed in q5 above: the hours whose ground reading is below the reading aloft carry the two largest particulate values, and the values fall once that ordering reverses. STB-2.C.1 defines the ordering and STB-2.C.2 supplies the trapping."),
 ("instead of letting it disperse upward",
  "STB-2.C.2 is a statement about where released pollution goes: it is trapped close to the ground. The concentration near the surface therefore rises because the same releases are confined to a shallower layer, not because new pollutants are created or existing ones made more toxic."),
 ("far higher below 350 meters",
  "Recomputed in q7 above: the three lowest samples carry sulfur dioxide an order of magnitude above the two highest, and the temperature is still rising with height up to that level. The pollution sits in the layer the inversion of STB-2.C.1 caps, which is the trapping of STB-2.C.2."),
 ("Only City J shows the altered gradient",
  "Recomputed in q8 above: City J's ground reading is below its reading at 400 meters and City K's is above. STB-2.C.1 makes the cooler surface the defining condition, so only one of the two cities meets it."),
 ("at the ground and at one or more heights above it",
  "STB-2.C.1 defines the inversion by comparing the temperature at the surface with the temperature at higher altitude, so the comparison requires readings at two or more heights at one time. A surface record alone, a pollutant count, a traffic count or a rainfall total never makes that comparison."),
 ("usually warmer than the air above it",
  "STB-2.C.1 calls the inversion the case in which the NORMAL gradient is ALTERED and describes that altered case as the surface being cooler than the air above. The unaltered case is therefore the reverse, which is the only inference this item makes."),
 ("two sites where the ground is cooler than the air at 200 meters",
  "Recomputed in q11 above: exactly two sites have the ground reading below the reading aloft, and those two carry the two largest particulate values while the two with the ordinary ordering carry the two smallest. STB-2.C.1 and STB-2.C.2 together."),
 ("surface air has warmed above the air aloft",
  "STB-2.C.2 attaches the trapping to the arrangement STB-2.C.1 defines, so when the surface becomes the warmer of the two the defining condition is gone and the releases are no longer confined near the ground. The framework attributes to an inversion no chemical destruction and no change in what sources emit."),
 ("arrangement of air temperature with height",
  "STB-2.C.1 defines a thermal inversion by the temperature of surface air relative to the air above, which is a physical arrangement and not a substance. Its relationship with pollution, under STB-2.C.2, is that it traps what other sources release."),
 ("Both smog and particulates were higher on the days when an inversion was present",
  "Recomputed in q14 above: each inversion day carries larger values in both pollutant columns than either day without one. STB-2.C.2 names smog and particulates as the pollution an inversion especially traps close to the ground."),
 ("air people breathe carries more of them",
  "STB-2.C.2 has the inversion hold smog and particulates close to the ground, which is a rise in what is present at the level where people are. The framework makes no claim that an inversion creates more toxic substances, lowers oxygen, or changes vehicle emission rates."),
 ("temperature at two heights each morning",
  "Suggested skill 2.C together with STB-2.C.1: whether an inversion is present is itself a measurement, requiring temperatures at two heights, and it must be recorded alongside the pollution for the relationship to be tested. Dropping the inversion days or moving the site removes the comparison entirely."),
 ("inversion was present on the first morning and absent on the second",
  "With releases held equal by the stem, the ground-level concentration depends on whether the pollution is confined near the surface, which is what STB-2.C.2 attributes to an inversion. A change of instruments is not a condition of the atmosphere."),
 ("Twenty degrees Celsius at the ground and sixteen degrees Celsius at 500 meters",
  "STB-2.C.1 requires the surface air to be COOLER than the air above for an inversion, so a pair whose ground reading is the warmer of the two rules one out. In each rejected pair the ground reading is the cooler, which is the inversion condition rather than its absence."),
 ("that temperature ordering is the inversion that traps pollution",
  "The reported condition is the altered gradient of STB-2.C.1 and the reported consequence is the trapping of STB-2.C.2. Neither statement is limited to a particular kind of source or to a particular hour of the day."),
 ("temperature increases upward, lying above cooler air at the surface",
  "STB-2.C.1 defines the inversion in terms of temperature alone: surface air cooler than the air at higher altitudes, which on a profile is temperature increasing upward above the cool surface layer. Wind and humidity form no part of the definition."),
 ("smaller releases still mean less pollution trapped",
  "STB-2.C.2 has the inversion trap the pollution that has been released, so the quantity confined depends on the sources. The framework attributes to an inversion no destruction of pollutants and no emission of its own, so the argument that emissions do not matter has no support in it."),
 ("a measurement above the trapped layer misses it",
  "STB-2.C.2 places the trapped pollution close to the ground, so a sampler above that layer is not sampling the air the pollution occupies. Particulates are one of the two kinds of pollution the statement names."),
 ("one of the two kinds of pollution the framework names",
  "STB-2.C.2 names smog and particulates as especially trapped close to the ground during an inversion. It does not make the inversion a condition for smog to form, a source of smog, or a component of clean air."),
 ("arrangement that traps pollution near the ground would be gone",
  "The trapping in STB-2.C.2 belongs to the arrangement STB-2.C.1 defines, in which the surface air is the cooler. Reversing the ordering removes that condition, so pollution released at the surface is no longer held in a shallow layer."),
 ("changes where released pollution goes",
  "STB-2.C.2 is a claim about where pollution ends up -- close to the ground -- while how much enters the air is a matter of the sources identified under STB-2.A. The two are separate and the framework does not merge them."),
 ("on complaint mornings and on comparable mornings without complaints",
  "The claim to be tested is that the ordering defined in STB-2.C.1 is present when the air is worst, so it needs the paired temperature reading on both kinds of morning. Annual complaint totals, yearly average temperature, population and haze color leave that definition untested."),
 ("layer of air where people live and breathe",
  "STB-2.C.2 places the trapped pollution close to the ground, which is where people are, and that is the whole of the health relevance the framework claims for an inversion. It asserts no direct harm from the temperature, no effect on stratospheric ozone, and no change of state of particulates."),
 ("Only the second profile shows the altered gradient",
  "STB-2.C.1 makes the altered gradient the case in which surface air is cooler than the air above, which is the profile that rises from the ground upward. The profile that falls throughout has the warmest air at the surface and is the ordinary arrangement."),
 ("not held close to the ground by the inversion",
  "STB-2.C.2 attributes to an inversion the trapping of pollution close to the ground, so material entering the air above the trapped layer is not subject to that confinement near the plant. An inversion is an arrangement of air temperature and is neither created nor destroyed by a stack."),
 ("normal gradient is altered and pollution, especially smog and particulates, is held close to the ground",
  "The summary joins STB-2.C.1 and STB-2.C.2 in the framework's own order and wording. Each rejected summary reverses the temperature ordering, makes the inversion a source of pollution, sends the pollution upward, or denies the relationship the learning objective is about."),
]

TABLE_CHECKS = {2: q2, 3: q3, 5: q5, 7: q7, 8: q8, 11: q11, 14: q14}

es.run(e7_3, CLAIMS, TABLE_CHECKS, sys.argv)
