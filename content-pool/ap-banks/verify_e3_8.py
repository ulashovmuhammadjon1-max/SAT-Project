"""Key audit for AP ENVIRONMENTAL SCIENCE 3.8 Human Population Dynamics.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. ``claim`` states what the key rests on, for a human to audit.

WHAT THE KEYS REST ON
---------------------
  EIN-1.C.1  human population growth and decline are determined by the rates of
             birth, death, immigration, and emigration; birth and death rates
             are affected by factors such as access to education, family
             planning, healthcare, and nutrition
                 -- items 1, 2, 21, 22, 23, 30
  EIN-1.C.2  factors limiting global human population include the Earth's
             carrying capacity and the basic factors that limit human
             population growth as set forth by Malthusian theory
                 -- items 3, 4, 30
  EIN-1.C.3  growth can be affected by density-independent factors, such as
             major storms, fires, heat waves, or droughts, and
             density-dependent factors, such as access to clean water and air,
             food availability, disease transmission, or territory size
                 -- items 5, 6, 7, 25, 26, 27, 28, 30
  EIN-1.C.4  the rate of natural increase is the crude birth rate less the
             crude death rate, typically expressed as a percentage; one way to
             estimate doubling time is by dividing 70 by the annual population
             growth rate expressed as a percentage
                 -- items 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22,
                    24, 29, 30

WHAT IS DELIBERATELY NOT KEYED. EIN-1.C.2 names Malthusian theory and states
none of the factors it sets forth, so no key here asserts what Malthus argued;
item 4 keys exactly that absence. EIN-1.C.4 gives no unit for the crude rates,
so every stem that needs one states that the rates are counted per 1,000
people, and the checks below convert to a percentage themselves.

THE ARITHMETIC IS THE ONE MACHINE-CHECKABLE GATE THIS TOPIC HAS, and every
quantitative key goes through it: the rate of natural increase as births less
deaths, the overall change as births less deaths plus immigrants less
emigrants, and doubling time as 70 divided by the annual growth rate in
percent. Items 20 to 22 turn on the difference between the first two, since a
population can carry a positive rate of natural increase and still shrink.

DATA ITEMS: 13 to 26 carry tables, each recomputed below from that table alone.

NEGATIVE CONTROLS run on every invocation through ``e_check.run``: a key moved,
an anchor broken, a choice duplicated, a ``why`` thinned, an option named by
letter, a backslash and a year range injected, a stem pointed at a figure, and
every table reversed and then flattened. ``--selftest`` adds
``es_check.selftest``, which rotates all thirty keys one at a time and corrupts
every cell of every table individually.
"""
import sys

import cg_check as cg
import e_check
import es_check as es

import e3_8

CBR = "Crude birth rate per 1,000 people"
CDR = "Crude death rate per 1,000 people"
PER1000 = "Per 1,000 people"
GROWTH = "Annual population growth rate (percent)"
COMPONENT = "People per 1,000 of the population"
EDU = "Percent of adults completing secondary education"
HEALTH = "Percent of people with access to healthcare"
CROWDED = "Percent of the population lost where it was crowded"
SPARSE = "Percent of the population lost where it was sparse"


def _rni_percent(table):
    """Crude birth rate less crude death rate, per 1,000, expressed as a percent."""
    return [(b - d) / 10 for b, d in zip(cg.col(table, CBR), cg.col(table, CDR))]


def _components(table):
    """The four component lines, keyed by their row label."""
    return {lab: v for lab, v in zip(cg.labels(table), cg.col(table, COMPONENT))}


def _doubling(rate):
    return 70 / rate


def q13(table, item):
    labels = cg.labels(table)
    rni = _rni_percent(table)
    declining = [labels[i] for i, r in enumerate(rni) if r < 0]
    assert declining == ["Country 4"], \
        f"exactly Country 4 must return a negative rate of natural increase; got {declining}"
    return (f"subtracting each crude death rate from its crude birth rate gives {rni} "
            f"percent, of which exactly one is negative and it belongs to {declining[0]}")


def q14(table, item):
    labels = cg.labels(table)
    births = cg.col(table, CBR)
    rni = _rni_percent(table)
    top = max(range(len(births)), key=lambda i: births[i])
    assert labels[top] == "Country 1", \
        f"the highest crude birth rate must belong to Country 1; got {labels[top]}"
    assert len([b for b in births if b == births[top]]) == 1, \
        "the highest crude birth rate must be unique"
    assert abs(rni[top] - 2.5) < 1e-9, \
        f"that country's rate of natural increase must be 2.5 percent; got {rni[top]}"
    return (f"{labels[top]} records {births[top]:.0f} births against "
            f"{cg.col(table, CDR)[top]:.0f} deaths per thousand, a difference of "
            f"{births[top] - cg.col(table, CDR)[top]:.0f} per thousand, or {rni[top]} percent")


def q15(table, item):
    labels = cg.labels(table)
    rni = _rni_percent(table)
    closest = min(range(len(rni)), key=lambda i: abs(rni[i]))
    assert labels[closest] == "Country 3", \
        f"the rate closest to zero must belong to Country 3; got {labels[closest]}"
    sizes = [abs(r) for r in rni]
    assert len([s for s in sizes if s == sizes[closest]]) == 1, \
        "that smallest size must be unique, so 'two are tied at zero' is false"
    assert all(s != 0 for s in sizes), "'tied at exactly zero' must be false for every country"
    return (f"the rates of natural increase read {rni} percent, whose single smallest "
            f"size belongs to {labels[closest]}")


def q16(table, item):
    rates = dict(zip(cg.labels(table), cg.col(table, PER1000)))
    birth = rates["Crude birth rate"]
    death = rates["Crude death rate"]
    assert birth == 12 and death == 12, \
        f"both crude rates must stand at 12 per thousand; got {birth} and {death}"
    assert birth - death == 0, "the rate of natural increase must come out at zero"
    return (f"the crude birth rate of {birth:.0f} less the crude death rate of "
            f"{death:.0f} per thousand leaves nothing, so the rate of natural increase "
            "is zero")


def q17(table, item):
    rates = dict(zip(cg.labels(table), cg.col(table, GROWTH)))
    years = _doubling(rates["Country Q"])
    assert abs(years - 35) < 1e-9, f"Country Q must double in about 35 years; got {years}"
    others = {c: _doubling(r) for c, r in rates.items() if c != "Country Q"}
    assert all(abs(y - 35) > 1e-9 for y in others.values()), \
        f"no other country may also return 35 years; got {others}"
    return (f"70 divided by Country Q's growth rate of {rates['Country Q']} percent gives "
            f"{years:.0f} years, and no other country in the record returns that figure")


def q18(table, item):
    rates = dict(zip(cg.labels(table), cg.col(table, GROWTH)))
    times = {c: _doubling(r) for c, r in rates.items()}
    soonest = min(times, key=times.get)
    assert soonest == "Country R", f"the shortest doubling time must be Country R's; got {soonest}"
    assert max(rates, key=rates.get) == soonest, \
        "the shortest doubling time must belong to the largest growth rate"
    assert len(set(times.values())) == len(times), \
        "'all four take the same time' must be false"
    return (f"the doubling times come out at {[round(t, 1) for t in times.values()]} years, "
            f"whose smallest belongs to {soonest}, the country with the largest growth rate")


def q19(table, item):
    rates = dict(zip(cg.labels(table), cg.col(table, GROWTH)))
    slowest = min(rates, key=rates.get)
    assert slowest == "Country S", f"the slowest growing must be Country S; got {slowest}"
    one_percent = [c for c, r in rates.items() if abs(r - 1.0) < 1e-9]
    assert one_percent == ["Country P"], \
        f"exactly Country P must grow at one percent a year; got {one_percent}"
    gap = _doubling(rates[slowest]) - _doubling(1.0)
    assert abs(gap - 30) < 1e-9, f"the difference must be about 30 years; got {gap}"
    assert gap > 0, "the slower growing country must take longer, not less time"
    return (f"70 divided by {rates[slowest]} percent gives "
            f"{_doubling(rates[slowest]):.0f} years against {_doubling(1.0):.0f} years at "
            f"one percent, a difference of {gap:.0f} years")


def q20(table, item):
    c = _components(table)
    rni = (c["Births"] - c["Deaths"]) / 10
    assert abs(rni - 1.7) < 1e-9, f"the rate of natural increase must be 1.7 percent; got {rni}"
    net = (c["Births"] - c["Deaths"] + c["Immigrants arriving"] - c["Emigrants leaving"]) / 10
    assert abs(net - rni) > 1e-9, \
        "the overall change must differ from the rate of natural increase, or the item does not bite"
    return (f"births of {c['Births']:.0f} less deaths of {c['Deaths']:.0f} per thousand "
            f"gives {rni} percent, while the overall change including migration is a "
            f"different figure, {net} percent")


def q21(table, item):
    c = _components(table)
    net_per_thousand = (c["Births"] - c["Deaths"]
                        + c["Immigrants arriving"] - c["Emigrants leaving"])
    assert abs(net_per_thousand - 10) < 1e-9, \
        f"the overall change must be a gain of 10 per thousand; got {net_per_thousand}"
    assert net_per_thousand > 0, "the population must have grown rather than fallen"
    assert abs(net_per_thousand - (c["Births"] - c["Deaths"])) > 1e-9, \
        "the overall change must differ from births less deaths alone"
    return (f"births less deaths plus immigrants less emigrants gives "
            f"{net_per_thousand:.0f} per thousand, or {net_per_thousand / 10} percent, a gain")


def q22(table, item):
    c = _components(table)
    rni = c["Births"] - c["Deaths"]
    net = rni + c["Immigrants arriving"] - c["Emigrants leaving"]
    assert rni > 0, f"the rate of natural increase must be positive; got {rni} per thousand"
    assert net < 0, f"the overall change must be negative; got {net} per thousand"
    return (f"births less deaths gives {rni:.0f} per thousand, a positive rate of natural "
            f"increase, while adding immigrants and subtracting emigrants gives "
            f"{net:.0f} per thousand, a fall")


def q23(table, item):
    for driver in (EDU, HEALTH):
        for rate in (CBR, CDR):
            pairs = sorted(zip(cg.col(table, driver), cg.col(table, rate)))
            assert all(pairs[i + 1][1] < pairs[i][1] for i in range(len(pairs) - 1)), \
                f"sorted by {driver!r} the {rate!r} must fall strictly; got {pairs}"
    return (f"sorted by education and then by healthcare access, the crude birth rates read "
            f"{sorted(cg.col(table, CBR), reverse=True)} and the crude death rates "
            f"{sorted(cg.col(table, CDR), reverse=True)} per thousand, both falling")


def q24(table, item):
    labels = cg.labels(table)
    rni = _rni_percent(table)
    top = max(range(len(rni)), key=lambda i: rni[i])
    assert labels[top] == "Country W", \
        f"the largest rate of natural increase must belong to Country W; got {labels[top]}"
    assert abs(rni[top] - 2.3) < 1e-9, f"that rate must be 2.3 percent; got {rni[top]}"
    assert len(set(rni)) == len(rni), "'all four are equal' must be false"
    return (f"the rates of natural increase read {rni} percent, whose single largest, "
            f"{rni[top]}, belongs to {labels[top]}")


def _dependent(table):
    """Events whose loss where crowded is several times the loss where sparse."""
    labels = cg.labels(table)
    crowded = cg.col(table, CROWDED)
    sparse = cg.col(table, SPARSE)
    return [labels[i] for i in range(len(labels)) if crowded[i] > 2 * sparse[i]]


def q25(table, item):
    dependent = _dependent(table)
    assert dependent == ["Event 2", "Event 4"], \
        f"exactly the second and fourth events must be density dependent; got {dependent}"
    labels = cg.labels(table)
    crowded = cg.col(table, CROWDED)
    sparse = cg.col(table, SPARSE)
    independent = [labels[i] for i in range(len(labels)) if labels[i] not in dependent]
    for i, lab in enumerate(labels):
        if lab in independent:
            assert abs(crowded[i] - sparse[i]) <= 3, \
                f"{lab} must lose a similar share at both densities; got {crowded[i]} and {sparse[i]}"
    assert independent, "'none of the four' must be false"
    return (f"the crowded losses read {crowded} percent against sparse losses of {sparse}, "
            f"so {dependent} lose several times as much where crowded while "
            f"{independent} lose a similar share either way")


def q26(table, item):
    labels = cg.labels(table)
    gaps = [c - s for c, s in zip(cg.col(table, CROWDED), cg.col(table, SPARSE))]
    top = max(range(len(gaps)), key=lambda i: gaps[i])
    assert labels[top] == "Event 2", f"the largest gap must be Event 2's; got {labels[top]}"
    assert len([g for g in gaps if g == gaps[top]]) == 1, "that largest gap must be unique"
    assert all(g != 0 for g in gaps), "'crowding made no difference in any event' must be false"
    return (f"the crowded loss less the sparse loss reads {gaps} percentage points, whose "
            f"single largest belongs to {labels[top]}")


CLAIMS = [
 ("rates of birth, death, immigration and emigration",
  "EIN-1.C.1, near verbatim: human population growth and decline are determined by the rates of birth, death, immigration, and emigration. Each rejected option drops at least one of the four or replaces them with quantities the statement never names."),
 ("access to education, family planning, healthcare and nutrition",
  "EIN-1.C.1's second sentence states that birth rates and death rates are affected by factors such as access to education, family planning, healthcare, and nutrition, and names no geographic factor and no fixed rate."),
 ("carrying capacity and the basic limiting factors set forth by Malthusian theory",
  "EIN-1.C.2, near verbatim: factors limiting global human population include the Earth's carrying capacity and the basic factors that limit human population growth as set forth by Malthusian theory."),
 ("the statement gives none of those factors",
  "EIN-1.C.2 refers to the basic factors set forth by Malthusian theory without stating any of them, and supplies no date, no figure for how many people the Earth can support, and no verdict on the theory. Nothing further can be keyed to it."),
 ("Major storms, fires, heat waves and droughts",
  "EIN-1.C.3 names major storms, fires, heat waves, or droughts as its examples of density-independent factors, and gives a separate list for the density-dependent ones."),
 ("clean water and air, food availability, disease transmission and territory size",
  "EIN-1.C.3 names access to clean water and air, food availability, disease transmission, or territory size as its examples of density-dependent factors."),
 ("A shortage of food",
  "EIN-1.C.3 lists major storms, fires, heat waves and droughts as density-independent and places food availability in the density-dependent list, so a food shortage is the item that does not belong."),
 ("subtracting the crude death rate from the crude birth rate",
  "EIN-1.C.4, near verbatim: the rate of natural increase is calculated by subtracting the crude death rate from the crude birth rate. The rejected options reverse the order, add instead of subtract, divide, or use the migration rates."),
 ("Population growth or decline",
  "EIN-1.C.4 calls the rate of natural increase a demographic metric measuring population growth or decline, so it reports a change rather than a size, an area or a movement."),
 ("As a percentage",
  "EIN-1.C.4 states that the rate of natural increase is typically expressed as a percentage, which is why a difference counted per thousand people is converted before it is reported."),
 ("Dividing 70 by the annual population growth rate expressed as a percentage",
  "EIN-1.C.4, near verbatim: one way to estimate the doubling time of a population is by dividing 70 by the annual population growth rate expressed as a percentage. The rejected options invert the division, multiply, subtract, or substitute the crude birth rate for the growth rate."),
 ("one method among others rather than the only one",
  "EIN-1.C.4's wording, ONE WAY to ESTIMATE, marks the calculation as an approximation and as one method among others, so the framework makes it neither exact nor exclusive."),
 ("Country 4, whose crude death rate exceeds its crude birth rate",
  "Recomputed in q13 above: exactly one country returns a negative figure when the crude death rate is subtracted from the crude birth rate, as EIN-1.C.4 directs. The anchor carries both the country and the direction, because the rejected option puts the same two rates the other way round."),
 ("2.5 percent",
  "Recomputed in q14 above: the country with the uniquely highest crude birth rate records 34 against 9 per thousand, a difference of 25 per thousand. EIN-1.C.4 subtracts the death rate from the birth rate and expresses the result as a percentage."),
 ("Country 3",
  "Recomputed in q15 above: subtracting each crude death rate from its crude birth rate leaves one country with a difference smaller in size than any other, and none at exactly zero. EIN-1.C.4 supplies the subtraction."),
 ("rate of natural increase of zero",
  "Recomputed in q16 above: both crude rates stand at 12 per thousand, so EIN-1.C.4's subtraction leaves nothing. The calculation uses those two rates only, so no migration figure is needed for it."),
 ("About 35 years",
  "Recomputed in q17 above: 70 divided by that country's growth rate of 2.0 percent gives 35 years, and no other country in the record returns that figure. EIN-1.C.4 supplies the estimate."),
 ("Country R, which records the largest yearly growth rate",
  "Recomputed in q18 above: the shortest doubling time belongs to the largest growth rate, since EIN-1.C.4 divides the same number, 70, by that rate."),
 ("About 30 years longer",
  "Recomputed in q19 above: 70 divided by 0.7 percent gives 100 years against 70 years at one percent. EIN-1.C.4's estimate returns a longer doubling time for a smaller growth rate."),
 ("1.7 percent, since only births and deaths enter the calculation",
  "Recomputed in q20 above: births less deaths gives 17 per thousand, or 1.7 percent, and that figure differs from the overall change. EIN-1.C.4 defines the rate of natural increase from those two rates alone."),
 ("grew by 10 people per thousand",
  "Recomputed in q21 above: births less deaths plus immigrants less emigrants gives a gain of 10 per thousand, which differs from births less deaths alone. EIN-1.C.1 makes all four rates determine growth and decline."),
 ("rate of natural increase is positive, yet its population shrank",
  "Recomputed in q22 above: births less deaths is positive while births less deaths plus immigrants less emigrants is negative. EIN-1.C.4 defines the first quantity and EIN-1.C.1 the second, and this record separates them."),
 ("Both crude rates fall as education and healthcare access rise",
  "Recomputed in q23 above: sorting by education and then by healthcare access leaves both crude rates strictly falling. EIN-1.C.1 names access to education and to healthcare among the factors affecting birth rates and death rates."),
 ("Country W, at 2.3 percent",
  "Recomputed in q24 above: subtracting each crude death rate from its crude birth rate and expressing the result as a percentage leaves one country above all the others, and the four are not equal."),
 ("second and the fourth, whose losses were far heavier where the population was crowded",
  "Recomputed in q25 above: exactly two events lose several times as much where the population is crowded, while the other two lose within three percentage points of the same share at either density. EIN-1.C.3 draws exactly that distinction. The anchor carries both the pair and the direction, because one rejected option names the same pair with crowded and sparse swapped."),
 ("Event 2",
  "Recomputed in q26 above: subtracting the sparse loss from the crowded loss leaves one event with a uniquely largest gap, and no event has a gap of zero. EIN-1.C.3 treats a factor whose effect changes with density as density dependent."),
 ("density independent factor, of which the framework names major storms",
  "EIN-1.C.3 names major storms among its examples of density-independent factors, and an effect that does not change with how crowded the population is is what that category describes."),
 ("density dependent factor, of which the framework names disease transmission",
  "EIN-1.C.3 names disease transmission among its examples of density-dependent factors, and an effect that grows heavier as the population becomes more crowded is what that category describes."),
 ("annual population growth rate, expressed as a percentage",
  "EIN-1.C.4 states that the estimate divides 70 by the annual population growth rate expressed as a percentage, so that rate is the only quantity the calculation takes."),
 ("crude birth rate less the crude death rate, with doubling time estimated",
  "EIN-1.C.1 supplies the four determining rates and the factors affecting birth and death rates, EIN-1.C.2 the two named limits on the global population, EIN-1.C.3 both categories of factor, and EIN-1.C.4 the calculation and the doubling time estimate. Each rejected summary drops a rate, denies a limit, reverses an operation, or claims a detail about Malthusian theory the framework never gives."),
]

TABLE_CHECKS = {13: q13, 14: q14, 15: q15, 16: q16, 17: q17, 18: q18, 19: q19,
                20: q20, 21: q21, 22: q22, 23: q23, 24: q24, 25: q25, 26: q26}

if "--selftest" in sys.argv:
    es.selftest(e3_8, CLAIMS, TABLE_CHECKS)

e_check.run(e3_8, CLAIMS, TABLE_CHECKS)
