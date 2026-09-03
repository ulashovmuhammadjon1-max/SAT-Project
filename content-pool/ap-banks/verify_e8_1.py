"""Key audit for AP ENVIRONMENTAL SCIENCE 8.1 Sources of Pollution.

One (anchor, claim) per item, in module order; the anchor must appear in the
keyed choice and in no distractor. `cg_check.check` is the structural gate and
`es_check` carries the notation gate and the negative control.

WHAT THE KEYS REST ON
---------------------
The topic has two essential knowledge statements:

  STB-3.A.1  a point source refers to a single, identifiable source of a
             pollutant, such as a smokestack or waste discharge pipe;
  STB-3.A.2  nonpoint sources of pollution are diffused and can therefore be
             difficult to identify, such as pesticide spraying or urban runoff.

Items 1, 3, 8, 17, 20, 22 and 28 read a case against STB-3.A.1. Items 2, 4, 6,
7, 10, 14, 15, 18, 24 and 29 read a case against STB-3.A.2. Items 5, 9, 11, 12,
13, 16, 19, 21, 23, 25, 26, 27 and 30 turn on the contrast between the two.

TWO CONSEQUENCES OF THE PAIR ARE USED AS SUCH, and nothing further is inferred:
a source that is single and identifiable can be sampled at that one location
(items 8, 9, 16, 19, 20, 27), and a source that is diffused cannot, which is
what STB-3.A.2's own words "difficult to identify" assert (items 6, 15, 21, 24,
25, 29).

NOT CLAIMED: no statute, permit system, agency, treatment requirement or
numerical limit -- the framework names none in this topic -- and no effect of
any particular pollutant, which belongs to STB-3.B and later.

DATA ITEMS: 5, 7, 8, 10, 12 and 13 carry tables and every keyed reading is
recomputed below from the table alone.

NEGATIVE CONTROL: `python3 verify_e8_1.py --selftest`.
"""
import sys

import cg_check as cg
import es_check as es
import e8_1

LOAD = "Load measured or estimated (tons per year)"
OUTLET = "Can the contribution be measured at a single outlet"
SED = "Suspended sediment in the creek (milligrams per liter)"
PEST = "Pesticide in the creek (micrograms per liter)"
METAL = "Metal concentration (micrograms per liter)"
SHARE = "Share of the sub-basin (percent)"
NITRO = "Nitrogen delivered to the stream (kilograms per year)"
PIPES = "Pollutant released from identified discharge pipes (tons per year)"
OTHER = "Pollutant reaching the bay from all other sources (tons per year)"
SITES = "Number of separate locations releasing the pollutant"


def q5(table, item):
    rows = {r[0]: (r[1], r[2]) for r in table["rows"]}
    loads = dict(zip(cg.labels(table), cg.col(table, LOAD)))
    flag = {k: v[1] for k, v in rows.items()}
    assert set(flag.values()) <= {"yes", "no"}, f"the outlet column is not yes or no: {flag}"
    diffuse = sum(loads[k] for k in loads if flag[k] == "no")
    single = sum(loads[k] for k in loads if flag[k] == "yes")
    assert diffuse > single, f"the diffused total {diffuse} does not exceed {single}"
    assert single > 0, "'only the measurable ones deliver any load' cannot be tested without both"
    assert len(set(loads.values())) > 1, "'equal shares' must be false"
    assert loads["Factory discharge pipe"] != max(loads.values()), \
        "'the factory pipe is the largest single contribution' must be false"
    return (f"the contributions not measurable at one outlet total {diffuse:.0f} tons against "
            f"{single:.0f} for those that are, and the largest single row is "
            f"{max(loads, key=loads.get)}")


def q7(table, item):
    times = cg.labels(table)
    sed = dict(zip(times, cg.col(table, SED)))
    pest = dict(zip(times, cg.col(table, PEST)))
    before = "Two days before the storm"
    during = "During the storm"
    after = "Two days after the storm"
    for series, name in ((sed, "sediment"), (pest, "pesticide")):
        assert series[during] > 10 * series[before], f"{name} does not rise sharply during the storm"
        assert series[after] > series[before], f"{name} does not remain above the pre-storm level"
        assert series[before] == min(series.values()), f"the pre-storm {name} is not the smallest"
    return (f"sediment runs {sed[before]:.0f}, {sed[during]:.0f}, {sed[after]:.0f} and pesticide "
            f"{pest[before]}, {pest[during]}, {pest[after]} before, during and after the storm")


def q8(table, item):
    points = cg.labels(table)
    pos = {r[0]: r[1] for r in table["rows"]}
    metal = dict(zip(points, cg.col(table, METAL)))
    up = [p for p in points if "upstream" in pos[p]]
    down = [p for p in points if "downstream" in pos[p]]
    assert len(up) == 2 and len(down) == 2, "two upstream and two downstream points are required"
    assert len(set(metal[p] for p in up)) == 1, f"the upstream values differ: {metal}"
    assert min(metal[p] for p in down) > 10 * max(metal[p] for p in up), \
        f"the downstream values are not far above the upstream: {metal}"
    near = [p for p in down if pos[p].startswith("100 meters")][0]
    far = [p for p in down if p != near][0]
    assert metal[near] > metal[far], "the concentration must not rise with distance downstream"
    assert metal[up[0]] != max(metal.values()), "'highest at the farthest upstream point' must be false"
    return (f"both upstream points read {metal[up[0]]:.0f} while the nearest downstream point reads "
            f"{metal[near]:.0f} and the far one {metal[far]:.0f}, a jump across the pipe")


def q10(table, item):
    covers = cg.labels(table)
    share = dict(zip(covers, cg.col(table, SHARE)))
    nitro = dict(zip(covers, cg.col(table, NITRO)))
    top = max(nitro, key=nitro.get)
    assert top == "Cropland", f"the largest nitrogen delivery belongs to {top}"
    assert max(share, key=share.get) == top, "the largest land cover is not the largest deliverer"
    assert nitro["Forest"] == min(nitro.values()), "'forest delivers the most' must be false"
    assert min(share, key=share.get) != top, \
        "'the smallest share delivers the most' must be false"
    assert len(set(nitro.values())) == len(nitro), "'all the same' must be false"
    return (f"cropland holds {share[top]:.0f} percent of the sub-basin and delivers "
            f"{nitro[top]:.0f} kilograms, the largest of {sorted(nitro.values())}")


def q12(table, item):
    years = cg.labels(table)
    pipes = dict(zip(years, cg.col(table, PIPES)))
    other = dict(zip(years, cg.col(table, OTHER)))
    first, last = years[0], years[-1]
    assert pipes[last] < 0.25 * pipes[first], "the pipe load does not fall sharply"
    assert other[last] > 0.9 * other[first], "the other load should change little"
    assert other[last] > pipes[last], "the remaining pollution should be mostly from other sources"
    assert pipes[last] < pipes[first], "'the pipe load rose' must be false"
    assert not any(abs(pipes[y] - other[y]) < 1e-9 for y in years), "'equal in every year' must be false"
    return (f"the pipe load falls from {pipes[first]:.0f} to {pipes[last]:.0f} tons while the other "
            f"load moves only from {other[first]:.0f} to {other[last]:.0f}")


def q13(table, item):
    rows = dict(zip(cg.labels(table), cg.col(table, SITES)))
    spread = [k for k, v in rows.items() if v > 1]
    single = [k for k, v in rows.items() if v == 1]
    assert len(spread) == 1 and len(single) == 2, f"expected one diffused row: {rows}"
    assert "Lawn treatment" in spread[0], f"the diffused row is {spread[0]}"
    assert rows[spread[0]] > 100 * max(rows[k] for k in single), \
        "the diffused row should involve very many more locations"
    return (f"{spread[0]} releases from {rows[spread[0]]:.0f} locations against one apiece for "
            f"{single}, so only that row is spread across many places")


CLAIMS = [
 ("single, identifiable source of a pollutant",
  "STB-3.A.1 verbatim: a point source refers to a single, identifiable source of a pollutant, such as a smokestack or waste discharge pipe. The definition turns on being one identifiable place, not on timing, on the number of pollutants, or on elevation."),
 ("diffused and can therefore be difficult to identify",
  "STB-3.A.2 verbatim: nonpoint sources of pollution are diffused and can therefore be difficult to identify, such as pesticide spraying or urban runoff. Being diffused is the opposite of being concentrated at one identifiable outlet."),
 ("pipe discharging treated wastewater into a river at one location",
  "STB-3.A.1 names a waste discharge pipe as its example of a single, identifiable source. Each rejected option describes release spread across many places, which is STB-3.A.2's diffused case."),
 ("thousands of yards across a suburb",
  "STB-3.A.2 gives urban runoff as an example of a diffused source, and runoff from thousands of separate yards is diffused across the built area. Each rejected option names one identifiable release location, which is STB-3.A.1."),
 ("cannot be measured at a single outlet together deliver more of the load",
  "Recomputed in q5 above: the rows marked as not measurable at one outlet total more than the rows that are, and the factory pipe is not the largest single row. STB-3.A.2's diffused sources are exactly those that cannot be pinned to one outlet."),
 ("from many places spread across the landscape",
  "STB-3.A.2 gives the reason in its own word, diffused. Nothing in the statement turns on visibility, the hour of release, the quantity, or whether an instrument can detect the pollutant once it is in the water."),
 ("consistent with washoff from across the landscape",
  "Recomputed in q7 above: both columns rise by more than a factor of ten during the storm and remain above their pre-storm values afterward. A pulse tied to rainfall rather than to a steady outlet is what the diffused sources of STB-3.A.2, pesticide spraying and urban runoff, produce."),
 ("low at both upstream points and much higher immediately downstream",
  "Recomputed in q8 above: the two upstream points read identically, the value jumps more than tenfold immediately below the pipe, and it declines farther downstream. Being traceable to one location in this way is STB-3.A.1's single, identifiable source."),
 ("passes through one identifiable location",
  "STB-3.A.1 makes a point source single and identifiable, which is why one sampling location captures it, while STB-3.A.2 makes nonpoint sources diffused. The comparison is about where the pollution enters, not about quantity, solubility or timing."),
 ("spread across the whole area of that land rather than issuing from one point",
  "Recomputed in q10 above: cropland holds both the largest share of the sub-basin and by far the largest nitrogen delivery, and forest the smallest. Delivery from a land cover across a basin is the diffused case of STB-3.A.2 rather than an outlet."),
 ("single, identifiable source, while runoff is diffused",
  "STB-3.A.1 and STB-3.A.2 together: one is a single identifiable source and the other is diffused and difficult to identify, with urban runoff as the framework's own example of the latter. Reversing the labels contradicts both statements."),
 ("comes mostly from sources that were not addressed",
  "Recomputed in q12 above: the pipe load falls to under a quarter of its starting value while the other load barely moves, so by the final year the larger part reaching the bay is from sources outside the program. Those are the diffused sources of STB-3.A.2."),
 ("lawn treatment is the diffused contributor",
  "Recomputed in q13 above: two rows name one release location each and the third names thousands. STB-3.A.2 makes being spread across many places the mark of a diffused source; the kind of discharge is not the test."),
 ("Pesticide spraying and urban runoff",
  "STB-3.A.2's own two examples. A smokestack and a waste discharge pipe are STB-3.A.1's examples, and landfill components and air pollution control devices belong to STB-3.K and STB-2.G."),
 ("entering from diffused sources along the reach",
  "A single identifiable source under STB-3.A.1 produces a step change at its own location, which these measurements lack. Entry spread along the reach is what STB-3.A.2 calls diffused."),
 ("immediately upstream and immediately downstream of each suspected outlet",
  "STB-3.A.1's single, identifiable source shows as a step increase across one location, so paired samples on either side of each candidate outlet are the test. A single distant sample, a basin area, a population count and a rainfall average cannot show it."),
 ("where the pollution enters the environment",
  "STB-3.A.1 classifies the SOURCE as single and identifiable and names a smokestack as an example, so dispersal after release does not change the classification. Quantity and the number of people affected form no part of the definition."),
 ("from streets, roofs and yards across the whole built area",
  "Urban runoff is STB-3.A.2's own example of a diffused source, and it is diffused because the pollution is picked up across the developed surface. Collection in one pipe would make the release identifiable, which is STB-3.A.1's case instead."),
 ("traced to identifiable sources while the second is diffused",
  "Three outfalls are three single, identifiable sources under STB-3.A.1, while delivery from farmland across a basin is diffused under STB-3.A.2. The distinction concerns how the pollution enters, not whether it is pollution or what it is made of."),
 ("rises sharply just below it, consistently across repeated sampling",
  "STB-3.A.1's single, identifiable source is exactly what produces a repeated step increase across one location. Equal concentrations above and below would refute the claim, and pipe size, ownership and a rainfall response point elsewhere."),
 ("Diffused sources across the surrounding land are still delivering",
  "The framework recognizes two kinds of source, so controlling every identifiable one leaves the diffused ones that STB-3.A.2 describes as difficult to identify. An outfall is by definition a single identifiable location and so is not a nonpoint source."),
 ("single pipe carrying process water from one plant",
  "STB-3.A.1 pairs a smokestack with a waste discharge pipe as its two examples of a single, identifiable source, so one pipe from one plant is the water analogue. Every rejected option describes release spread over an area."),
 ("how the pollutant enters the water, not what the pollutant is",
  "STB-3.A.1 and STB-3.A.2 classify sources by whether they are single and identifiable or diffused, which says nothing about the chemical identity of what is released. The same substance can therefore arrive by either route."),
 ("rain is what carries pollutants from across the landscape",
  "A continuous outlet under STB-3.A.1 would raise concentrations in dry weather too, so a rainfall-dependent rise points to material carried in from the surrounding land, which is STB-3.A.2's diffused case and its urban runoff example."),
 ("addressed at that location, while a diffused source has to be addressed across the area",
  "STB-3.A.1 and STB-3.A.2 differ precisely in whether there is one identifiable place where the pollution enters. The framework makes no claim that either kind is harmless or irreducible, and the source type says nothing about which pollutants are dangerous."),
 ("diffused across many locations rather than being one location of any size",
  "The framework's contrast is between a single identifiable source and a diffused one, so the difference is the spread of the release rather than its size, its schedule, its setting or the identity of its owner."),
 ("subtract the load measured at every identified outfall",
  "The diffused contribution is what remains once every single, identifiable source under STB-3.A.1 has been measured, which is what the subtraction isolates. Depth, business counts and another bay's load bear on this bay's sources not at all."),
 ("A waste discharge pipe, point source",
  "STB-3.A.1 names a waste discharge pipe and a smokestack as point sources and STB-3.A.2 names pesticide spraying and urban runoff as nonpoint sources. Each rejected pairing reverses one of those four assignments."),
 ("absence of one identifiable facility does not mean the pollution has no human source",
  "STB-3.A.2 exists for exactly this case: nonpoint sources are diffused and therefore difficult to identify, and urban runoff is its own example. The framework does not confine pollution to point sources or treat it as naturally occurring."),
 ("many places across the landscape is a nonpoint source that is harder to identify",
  "The summary states STB-3.A.1 and STB-3.A.2 in the framework's own terms, and its examples span both air and water. Visibility, legality and the sector of the economy are no part of the distinction."),
]

TABLE_CHECKS = {5: q5, 7: q7, 8: q8, 10: q10, 12: q12, 13: q13}

es.run(e8_1, CLAIMS, TABLE_CHECKS, sys.argv)
