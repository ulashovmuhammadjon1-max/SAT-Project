"""Key audit for AP ENVIRONMENTAL SCIENCE 9.5 Global Climate Change.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. ``claim`` states what the key rests on, for a human to audit.

WHAT THE KEYS REST ON
---------------------
  STB-4.F.1   climate change throughout geologic time, warming and cooling,
              recorded with CO2 data and ice cores -- items 1, 2, 18, 19, 20,
              21, 22, 30
  STB-4.F.2   rising temperatures, melting permafrost and sea ice, rising sea
              levels, displacement of coastal populations -- items 3, 4, 30
  STB-4.F.3   marine ecosystems affected by sea level change, some positively
              (new habitat on flooded shelves) and some negatively (deeper
              communities out of the photic zone) -- items 5, 6, 7, 27, 30
  STB-4.F.4   winds transport heat; climate change MAY change circulation, as
              temperature may impact Hadley cells and the jet stream
                                                      -- items 8, 9, 10, 18, 30
  STB-4.F.5   oceanic currents carry heat worldwide; a change has a big impact
              especially in coastal regions -- items 11, 18, 29, 30
  STB-4.F.6   climate change affects soil through temperature and rainfall,
              impacting viability and potentially increasing erosion
                                                          -- items 12, 13, 28, 30
  STB-4.F.7   polar regions respond faster because their ice and snow reflect
              the most energy back to space, a positive feedback loop
                                                      -- items 14, 18, 23, 24, 30
  STB-4.F.8   as that ice melts, less energy is radiated back and more absorbed,
              warming the poles further -- items 15, 24, 30
  STB-4.F.9   Arctic response time is due to positive feedback loops involving
              melting sea ice and thawing tundra and the subsequent release of
              greenhouse gases like methane -- items 16, 25, 30
  STB-4.F.10  one consequence of losing polar ice and snow is the effect on
              species that depend on it for habitat and food -- items 17, 26, 30

THE FIGURE PROBLEM, AND HOW IT IS SOLVED. This topic is taught from a carbon
dioxide curve and a temperature curve and the bank carries no images. Both are
supplied as tables, and each is sampled finely enough that the feature its own
stem asks about is genuinely readable: the ice core table carries six layers,
including ones both colder and warmer than the present, so the alternation
STB-4.F.1 describes is visible in the rows rather than asserted; the modern
table carries five readings, so "rises at every reading" can be checked step by
step instead of inferred from two endpoints. ``e_check.no_figure_reference``
refuses any stem that points at a picture, on every run.

THE SWAPS. Reflecting energy against absorbing it (items 14, 15, 24), positive
against negative feedback (items 16, 24), and the positive against the negative
marine case (items 6, 7, 27) are the reversals a prepared student falls for, so
each of those anchors carries BOTH clauses rather than the noun alone.

DATA ITEMS: 19 to 29 carry tables, each recomputed below from that table alone.

NEGATIVE CONTROLS run on every invocation through ``e_check.run``; ``--selftest``
adds ``es_check.selftest``, which rotates all thirty keys one at a time and
corrupts every cell of every table individually.
"""
import sys

import cg_check as cg
import e_check
import es_check as es

import e9_5

CO2_CORE = "Carbon dioxide in the trapped air (parts per million)"
TEMP_CORE = "Reconstructed temperature relative to today (degrees Celsius)"
CO2_MODERN = "Atmospheric carbon dioxide (parts per million)"
TEMP_MODERN = "Global temperature relative to the 1900 reading (degrees Celsius)"
WARMING = "Temperature rise since 1900 (degrees Celsius)"
ICE = "Summer sea ice extent (millions of square kilometres)"
REFLECT = "Percent of incoming sunlight reflected back to space by the surface"
SUMMER = "Mean summer surface temperature (degrees Celsius)"
THAWED = "Area of thawed tundra (thousands of square kilometres)"
METHANE = "Methane leaving the thawed ground (thousands of tonnes per year)"
ICEFEED = "Percent of its feeding done from sea ice"
POPCHANGE = "Percent change in its population across the record"
SEALEVEL = "Rise in sea level across the record (centimetres)"
NEWHAB = "New shallow habitat on the flooded shelf (square kilometres)"
LOSTPHOTIC = "Sea floor community carried below the photic zone (square kilometres)"
TEMPRISE = "Rise in mean temperature (degrees Celsius)"
RAINFALL = "Change in yearly rainfall (millimetres)"
EROSION = "Soil lost to erosion (tonnes per hectare each year)"
CURRENT = "Strength of the ocean current reaching one coast (relative index)"
WINTER = "Mean winter temperature of that coastal region (degrees Celsius)"


def _rising(values):
    return all(values[i + 1] > values[i] for i in range(len(values) - 1))


def _falling(values):
    return all(values[i + 1] < values[i] for i in range(len(values) - 1))


def q19(table, item):
    pairs = sorted(zip(cg.col(table, CO2_CORE), cg.col(table, TEMP_CORE)))
    temps = [t for _, t in pairs]
    assert _rising(temps), \
        f"sorted by carbon dioxide the reconstructed temperature must rise strictly; got {pairs}"
    assert any(t < 0 for t in temps), "some layer must be colder than today"
    assert any(t > 0 for t in temps), "some layer must be warmer than today"
    return (f"sorted by trapped carbon dioxide the reconstructed temperatures read {temps} "
            "degrees, strictly rising, with entries on both sides of today's value")


def q20(table, item):
    temps = cg.col(table, TEMP_CORE)
    spread = max(temps) - min(temps)
    assert abs(spread - 10.4) < 1e-9, f"the range must be 10.4 degrees; got {spread}"
    return (f"the reconstructed temperatures run from {min(temps)} to {max(temps)} degrees "
            f"relative to today, a range of {spread:.1f}")


def q21(table, item):
    co2 = cg.col(table, CO2_MODERN)
    temp = cg.col(table, TEMP_MODERN)
    assert _rising(co2), f"carbon dioxide must rise at every reading; got {co2}"
    assert _rising(temp), f"temperature must rise at every reading; got {temp}"
    return (f"in year order the carbon dioxide readings are {co2} parts per million and the "
            f"temperatures {temp} degrees, each rising at every step")


def q22(table, item):
    co2 = cg.col(table, CO2_MODERN)
    pct = (co2[-1] - co2[0]) / co2[0] * 100
    assert abs(pct - 40) < 1e-9, f"the rise must be 40 percent; got {pct}"
    assert pct > 0, "the movement must be a rise"
    return (f"carbon dioxide runs from {co2[0]:.0f} to {co2[-1]:.0f} parts per million, a "
            f"rise of {co2[-1] - co2[0]:.0f}, which is {pct:.0f} percent of the first "
            "reading")


def q23(table, item):
    warming = dict(zip(cg.labels(table), cg.col(table, WARMING)))
    top = max(warming, key=warming.get)
    assert top == "Arctic", f"the largest rise must belong to the Arctic; got {top}"
    assert len([v for v in warming.values() if v == warming[top]]) == 1, \
        "that largest rise must be unique, so 'all four warmed alike' is false"
    gap = warming[top] - warming["Tropics"]
    assert abs(gap - 2.3) < 1e-9, f"the gap over the tropics must be 2.3 degrees; got {gap}"
    return (f"the rises read {list(warming.values())} degrees, whose single largest, "
            f"{warming[top]}, stands {gap:.1f} above the tropical figure of "
            f"{warming['Tropics']}")


def q24(table, item):
    ice = cg.col(table, ICE)
    reflect = cg.col(table, REFLECT)
    temp = cg.col(table, SUMMER)
    assert _falling(ice), f"the sea ice must shrink at every decade; got {ice}"
    assert _falling(reflect), f"the reflected share must fall at every decade; got {reflect}"
    assert _rising(temp), f"the summer temperature must rise at every decade; got {temp}"
    return (f"in decade order the ice extent reads {ice}, the reflected share {reflect} "
            f"percent and the summer temperature {temp} degrees, so as the ice falls the "
            "reflection falls and the temperature rises")


def q25(table, item):
    thawed = cg.col(table, THAWED)
    methane = cg.col(table, METHANE)
    assert _rising(thawed), f"the thawed area must rise at every survey; got {thawed}"
    assert _rising(methane), f"the methane must rise at every survey; got {methane}"
    return (f"in survey order the thawed area reads {thawed} thousand square kilometres "
            f"and the methane {methane} thousand tonnes a year, both rising at every step")


def q26(table, item):
    pairs = sorted(zip(cg.col(table, ICEFEED), cg.col(table, POPCHANGE)))
    changes = [c for _, c in pairs]
    assert _falling(changes), \
        f"the population change must fall as ice dependence rises; got {pairs}"
    assert any(c > 0 for c in changes), "'every species fell in number' must be false"
    assert any(c < 0 for c in changes), "'every species grew in number' must be false"
    return (f"sorted by the share of feeding done from ice, the population changes read "
            f"{changes} percent, strictly falling, and they are not all of one sign")


def q27(table, item):
    trio = sorted(zip(cg.col(table, SEALEVEL), cg.col(table, NEWHAB),
                      cg.col(table, LOSTPHOTIC)))
    new = [n for _, n, _ in trio]
    lost = [l for _, _, l in trio]
    assert _rising(new), f"the new shallow habitat must rise with the sea level; got {trio}"
    assert _rising(lost), f"the area lost from the photic zone must rise too; got {trio}"
    assert all(l > 0 for l in lost), "'every existing community stays where it was' must be false"
    assert all(n > 0 for n in new), "'no new habitat at all' must be false"
    return (f"sorted by the rise in sea level, the new shallow habitat reads {new} and the "
            f"area carried below the photic zone {lost} square kilometres, both rising, so "
            "the same rise does both things at once")


def q28(table, item):
    by_temp = sorted(zip(cg.col(table, TEMPRISE), cg.col(table, EROSION)))
    assert _rising([e for _, e in by_temp]), \
        f"soil loss must rise with the temperature rise; got {by_temp}"
    by_rain = sorted(zip(cg.col(table, RAINFALL), cg.col(table, EROSION)))
    assert _falling([e for _, e in by_rain]), \
        f"soil loss must fall as the rainfall change becomes less negative; got {by_rain}"
    assert all(r < 0 for r in cg.col(table, RAINFALL)), \
        "'rainfall rose on every plot' must be false"
    assert len(set(cg.col(table, EROSION))) == len(cg.col(table, EROSION)), \
        "'every plot lost the same amount of soil' must be false"
    return (f"sorted by the temperature rise the soil lost reads {[e for _, e in by_temp]} "
            f"tonnes per hectare, rising, and sorted by the rainfall change it reads "
            f"{[e for _, e in by_rain]}, so the warmest and driest plots lose the most")


def q29(table, item):
    current = cg.col(table, CURRENT)
    winter = cg.col(table, WINTER)
    assert _falling(current), f"the current must weaken at every period; got {current}"
    assert _falling(winter), f"the coastal winter must cool at every period; got {winter}"
    return (f"in period order the current index reads {current} and the coastal winter "
            f"temperature {winter} degrees, both falling at every step")


CLAIMS = [
 ("periods of warming and of cooling",
  "STB-4.F.1, near verbatim: the Earth has undergone climate change throughout geologic time, with major shifts in global temperatures causing periods of warming and cooling. Both directions are in the statement, which is what the rejected options drop."),
 ("Carbon dioxide data and ice cores",
  "STB-4.F.1 states that those major shifts are recorded with CO2 data and ice cores, which is the whole of the evidence the statement names."),
 ("melting permafrost and sea ice, rising sea levels",
  "STB-4.F.2, near verbatim: effects of climate change include rising temperatures, melting permafrost and sea ice, rising sea levels, and displacement of coastal populations."),
 ("hours of daylight at each latitude",
  "STB-4.F.2 names four effects, each of which the four rejected options restates. Hours of daylight appear nowhere in the statement."),
 ("Some are affected positively and some negatively",
  "STB-4.F.3 states that marine ecosystems are affected by changes in sea level, some positively and some negatively, and supplies an example on each side."),
 ("Newly created habitats on now flooded continental shelves",
  "STB-4.F.3 gives newly created habitats on now-flooded continental shelves as its example of a positive effect, and keeps the photic zone case for the negative side."),
 ("no longer lie within the photic zone",
  "STB-4.F.3 gives deeper communities that may no longer be in the photic zone of seawater as its negative example. The soil and polar species cases belong to STB-4.F.6 and STB-4.F.10 instead."),
 ("help transport heat throughout the Earth",
  "STB-4.F.4, near verbatim: winds generated by atmospheric circulation help transport heat throughout the Earth, which is a movement of heat rather than a removal or a blockage of it."),
 ("Hadley cells and the jet stream",
  "STB-4.F.4 states that temperature changes may impact Hadley cells and the jet stream, and names no other feature of circulation."),
 ("possibility the framework raises rather than an outcome it guarantees",
  "The word MAY in STB-4.F.4 marks the change in circulation patterns as possible, so the framework neither promises it nor rules it out."),
 ("a change has a big impact especially in coastal regions",
  "STB-4.F.5 states that oceanic currents, or the ocean conveyor belt, carry heat throughout the world, and that when these currents change it can have a big impact on global climate, especially in coastal regions. The anchor carries the coastal clause because one rejected option keeps the first half and reverses the second."),
 ("Changes in temperature and in rainfall",
  "STB-4.F.6 states that climate change can affect soil through changes in temperature and rainfall, and names no other route to the soil."),
 ("potentially increase erosion",
  "STB-4.F.6 states that those changes can impact soil's viability and potentially increase erosion, so the direction of the erosion claim is upward and it is hedged with POTENTIALLY."),
 ("reflect the most energy back out to space",
  "STB-4.F.7 states that the polar regions show faster response times because ice and snow in these regions reflect the most energy back out to space, leading to a positive feedback loop. The anchor names reflection, which is the half the swapped distractor inverts."),
 ("Less solar energy is radiated back into space and more is absorbed",
  "STB-4.F.8, near verbatim: as the Earth warms this ice and snow melts, meaning less solar energy is radiated back into space and instead is absorbed by the Earth's surface, which in turn causes more warming of the polar regions. The anchor carries both clauses because the rejected option swaps them."),
 ("Positive feedback loops involving melting sea ice and thawing tundra",
  "STB-4.F.9 states that global climate change response time in the Arctic is due to positive feedback loops involving melting sea ice and thawing tundra, and the subsequent release of greenhouse gases like methane. The anchor carries the sign of the loop and the two processes, because the rejected option reverses all three."),
 ("species that depend on the ice for habitat and food",
  "STB-4.F.10 names as one consequence of the loss of ice and snow in polar regions the effect on species that depend on the ice for habitat and food."),
 ("unchanging until human activity began",
  "STB-4.F.1 states that the Earth has undergone climate change throughout geologic time with periods of both warming and cooling, so a claim that the climate held steady until recently contradicts the framework. The four rejected options restate STB-4.F.1, STB-4.F.4, STB-4.F.5 and STB-4.F.7."),
 ("move together across the layers, and the record holds layers both colder and warmer than today",
  "Recomputed in q19 above: sorting the six layers by trapped carbon dioxide leaves the reconstructed temperature strictly rising, and the temperature column carries entries on both sides of today's value. STB-4.F.1 makes CO2 data and ice cores the record of those warming and cooling periods."),
 ("10.4 degrees Celsius",
  "Recomputed in q20 above: the warmest and coldest reconstructed layers differ by 10.4 degrees. STB-4.F.1 describes major shifts in global temperatures across geologic time, and this is the size of one such range."),
 ("Both rise at every successive reading",
  "Recomputed in q21 above: in year order each carbon dioxide reading and each temperature reading exceeds the one before it. STB-4.F.1 makes carbon dioxide data one of the two records by which shifts in global temperature are traced."),
 ("By 40 percent",
  "Recomputed in q22 above: the carbon dioxide column rises by 118 parts per million from a first reading of 295, which is 40 percent of it."),
 ("The Arctic, by 2.3 degrees Celsius more than the tropics",
  "Recomputed in q23 above: the largest and uniquely largest rise belongs to the Arctic and stands 2.3 degrees above the tropical figure. STB-4.F.7 states that the Earth's polar regions are showing faster response times to global climate change. The anchor names the region and the size together, because one rejected option reverses the two regions."),
 ("less sunlight is reflected and the surface grows warmer, which is a positive feedback loop",
  "Recomputed in q24 above: in decade order the ice extent and the reflected share both fall while the summer temperature rises. STB-4.F.7 and STB-4.F.8 describe exactly that chain, in which melting ice reflects less energy so more is absorbed and the region warms further. The anchor carries direction and sign, because the rejected option inverts both."),
 ("rises as the thawed area rises",
  "Recomputed in q25 above: in survey order the thawed area and the methane leaving it both rise at every step. STB-4.F.9 attributes the Arctic's response time to feedback loops involving thawing tundra and the subsequent release of greenhouse gases like methane."),
 ("feed most from the ice are the species whose populations fell most",
  "Recomputed in q26 above: sorting the species by the share of feeding done from ice leaves the population change strictly falling, and the changes are not all of one sign. STB-4.F.10 names the effect on species that depend on the ice for habitat and food."),
 ("both creates new shallow habitat and carries other communities below the photic zone",
  "Recomputed in q27 above: sorting the sites by the rise in sea level leaves both the new shallow habitat and the area carried below the photic zone strictly rising, and neither is zero anywhere. STB-4.F.3 gives exactly those two as its positive and negative examples."),
 ("lost most rainfall are the plots that lost most soil",
  "Recomputed in q28 above: soil loss rises with the temperature rise and falls as the rainfall change becomes less negative, and every plot's rainfall change is negative. STB-4.F.6 states that climate change can affect soil through changes in temperature and rainfall and potentially increase erosion."),
 ("As the current weakens, the coastal region grows colder",
  "Recomputed in q29 above: in period order the current index and the coastal winter temperature fall together. STB-4.F.5 states that oceanic currents carry heat throughout the world and that a change in them can have a big impact especially in coastal regions."),
 ("affects marine ecosystems both positively and negatively",
  "STB-4.F.1 supplies the geologic record and its evidence, STB-4.F.2 the four named effects, STB-4.F.3 the two directions for marine ecosystems, STB-4.F.4 and STB-4.F.5 the winds and currents that carry heat, STB-4.F.6 the soil, and STB-4.F.7 through STB-4.F.10 the polar feedback loops and the species that depend on ice. Each rejected summary denies the geologic record, reverses a direction, narrows the topic to one statement, or promises a certainty the framework hedges."),
]

TABLE_CHECKS = {19: q19, 20: q20, 21: q21, 22: q22, 23: q23, 24: q24, 25: q25,
                26: q26, 27: q27, 28: q28, 29: q29}

if "--selftest" in sys.argv:
    es.selftest(e9_5, CLAIMS, TABLE_CHECKS)

e_check.run(e9_5, CLAIMS, TABLE_CHECKS)
