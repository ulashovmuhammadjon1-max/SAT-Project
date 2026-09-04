"""Key audit for AP ENVIRONMENTAL SCIENCE 3.7 Total Fertility Rate.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. ``claim`` states what the key rests on, for a human to audit.

WHAT THE KEYS REST ON
---------------------
  EIN-1.B.1  total fertility rate is affected by the age at which females have
             their first child, educational opportunities for females, access
             to family planning, and government acts and policies
                 -- items 1, 2, 7, 8, 9, 10, 17, 18, 19, 21, 22, 23, 24, 29, 30
  EIN-1.B.2  if fertility rate is at replacement levels, a population is
             considered relatively stable
                 -- items 3, 6, 7, 11, 12, 13, 14, 15, 16, 20, 30
  EIN-1.B.3  factors associated with infant mortality rates include whether
             mothers have access to good healthcare and nutrition, and changes
             in these factors can lead to changes in infant mortality rates
             over time
                 -- items 4, 5, 7, 25, 26, 27, 28, 30

WHAT THE FRAMEWORK DOES NOT SUPPLY, AND HOW THAT IS HANDLED. EIN-1.B.2 says "at
replacement levels" and gives no number; the framework nowhere defines how a
total fertility rate is computed. So the replacement level of 2.1 children per
woman, and the arithmetic converting age specific rates into a total fertility
rate, are STATED IN THE STEM of every item that needs them, and the checks
below recompute that arithmetic from the table alone. The framework's share of
those keys is the interpretation only: at replacement, relatively stable.

EIN-1.B.1 SAYS "AFFECTED BY" AND NAMES NO DIRECTION. So no key here asserts
that more schooling must always lower fertility. Each data item keys the
pattern present IN ITS OWN RECORD, and the framework citation carries only the
claim that the quantity is one it names as affecting fertility.

NO FIGURE IS REFERENCED; ``e_check.no_figure_reference`` enforces that on every
run and its control injects a stem that points at one.

DATA ITEMS: 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25,
27 and 28 carry tables, each recomputed below.

NEGATIVE CONTROLS run on every invocation through ``e_check.run``; ``--selftest``
adds ``es_check.selftest``, which rotates all thirty keys one at a time and
corrupts every cell of every table individually.
"""
import sys

import cg_check as cg
import e_check
import es_check as es

import e3_7

AGEFIRST = "Mean age of mothers at first birth (years)"
SCHOOL = "Percent of girls completing secondary school"
FAMPLAN = "Percent of women with access to family planning services"
TFR = "Total fertility rate (children per woman)"
WOMEN = "Number of women"
CHILDREN = "Total number of children they bore"
BIRTHS = "Births per 1,000 women of that age in one year"
YEARS_SCHOOL = "Mean years of schooling completed by women"
AGEFIRST2 = "Mean age of mothers at first birth (years)"
ACCESS = "Percent of women reporting access to family planning services"
PAYMENT = "Government payment to families for each child (index)"
CARE = "Percent of mothers receiving healthcare during pregnancy"
NUTRITION = "Percent of mothers meeting the recommended nutrition"
DEATHS = "Infant deaths per 1,000 live births"

REPLACEMENT = 2.1  # stated in every stem that uses it; the framework gives no number


def _falls_with(table, driver, response):
    """Sorted by ``driver``, the ``response`` column must fall strictly."""
    pairs = sorted(zip(cg.col(table, driver), cg.col(table, response)))
    assert all(pairs[i + 1][1] < pairs[i][1] for i in range(len(pairs) - 1)), \
        f"sorted by {driver!r} the {response!r} column must fall strictly; got {pairs}"
    return [r for _, r in pairs]


def q8(table, item):
    for driver in (AGEFIRST, SCHOOL, FAMPLAN):
        _falls_with(table, driver, TFR)
    rates = cg.col(table, TFR)
    assert len(set(rates)) == len(rates), "'all four record the same rate' must be false"
    return ("sorted by age at first birth, by schooling and by family planning access in "
            f"turn, the fertility rates read {rates} each time, strictly falling")


def q9(table, item):
    labels = cg.labels(table)
    ages = cg.col(table, AGEFIRST)
    rates = cg.col(table, TFR)
    youngest = min(range(len(ages)), key=lambda i: ages[i])
    highest = max(range(len(rates)), key=lambda i: rates[i])
    assert youngest == highest, \
        "the youngest mothers and the highest fertility must fall in the same row"
    assert labels[youngest] == "Country 1", \
        f"that row must be Country 1; got {labels[youngest]}"
    assert len([a for a in ages if a == ages[youngest]]) == 1, "the youngest age must be unique"
    assert len([r for r in rates if r == rates[highest]]) == 1, "the highest rate must be unique"
    return (f"the ages at first birth read {ages} years and the fertility rates {rates}, "
            f"whose smallest and largest entries both fall on {labels[youngest]}")


def q10(table, item):
    rates = cg.col(table, TFR)
    spread = max(rates) - min(rates)
    assert abs(spread - 4.0) < 1e-9, f"the spread of fertility rates must be 4.0; got {spread}"
    return (f"the fertility rates read {rates} children per woman, so the largest less the "
            f"smallest is {spread:.1f}")


def q11(table, item):
    labels = cg.labels(table)
    rates = cg.col(table, TFR)
    at_rep = [labels[i] for i, r in enumerate(rates) if abs(r - REPLACEMENT) < 1e-9]
    assert at_rep == ["Country B"], \
        f"exactly Country B must sit at the replacement level of {REPLACEMENT}; got {at_rep}"
    return (f"the rates read {rates} children per woman, of which exactly one equals the "
            f"replacement level of {REPLACEMENT} stated in the stem")


def q12(table, item):
    rates = cg.col(table, TFR)
    below = [r for r in rates if r < REPLACEMENT]
    assert len(below) == 2, f"exactly two rates must lie below {REPLACEMENT}; got {below}"
    assert len(below) != len(rates), "'no country lies below it' must be false"
    return (f"of the rates {rates}, the entries {below} lie strictly below the replacement "
            f"level of {REPLACEMENT} stated in the stem")


def _means(table):
    women = cg.col(table, WOMEN)
    kids = cg.col(table, CHILDREN)
    return [k / w for k, w in zip(kids, women)]


def q13(table, item):
    labels = cg.labels(table)
    means = _means(table)
    at_rep = [labels[i] for i, m in enumerate(means) if abs(m - REPLACEMENT) < 1e-9]
    assert at_rep == ["Group 2"], \
        f"exactly Group 2 must complete childbearing at {REPLACEMENT}; got {at_rep}"
    return (f"children divided by women gives {[round(m, 3) for m in means]} per woman, of "
            f"which exactly one equals the replacement level of {REPLACEMENT}")


def q14(table, item):
    labels = cg.labels(table)
    women = cg.col(table, WOMEN)
    means = _means(table)
    biggest = max(range(len(women)), key=lambda i: women[i])
    assert labels[biggest] == "Group 4", \
        f"the largest group must be Group 4; got {labels[biggest]}"
    assert len([w for w in women if w == women[biggest]]) == 1, "the largest group must be unique"
    assert abs(means[biggest] - 4.3) < 1e-9, \
        f"that group's mean must be 4.3 children per woman; got {means[biggest]}"
    return (f"{labels[biggest]} is the largest group, at {women[biggest]:.0f} women bearing "
            f"{cg.col(table, CHILDREN)[biggest]:.0f} children, a mean of "
            f"{means[biggest]:.1f} per woman")


def _tfr_from_bands(table):
    """Five times the sum of the yearly band rates, divided by one thousand."""
    return 5 * sum(cg.col(table, BIRTHS)) / 1000


def q15(table, item):
    tfr = _tfr_from_bands(table)
    assert abs(tfr - 2.1) < 1e-9, f"the computed rate must be 2.1; got {tfr}"
    return (f"the six band rates total {sum(cg.col(table, BIRTHS)):.0f} per thousand per "
            f"year, which the rule in the stem turns into {tfr:.2f} children per woman")


def q16(table, item):
    tfr = _tfr_from_bands(table)
    assert abs(tfr - 2.7) < 1e-9, f"the computed rate must be 2.7; got {tfr}"
    assert tfr > REPLACEMENT, \
        f"that rate must lie above the replacement level of {REPLACEMENT}; got {tfr}"
    return (f"the six band rates total {sum(cg.col(table, BIRTHS)):.0f} per thousand per "
            f"year, which the rule in the stem turns into {tfr:.2f} children per woman, "
            f"above the replacement level of {REPLACEMENT}")


def q17(table, item):
    rates = _falls_with(table, YEARS_SCHOOL, TFR)
    schooling = cg.col(table, YEARS_SCHOOL)
    assert len(set(schooling)) == len(schooling), \
        "'all five record the same schooling' must be false"
    return (f"sorted by mean years of schooling the fertility rates read {rates}, strictly "
            "falling across the five countries")


def q18(table, item):
    pairs = sorted(zip(cg.col(table, YEARS_SCHOOL), cg.col(table, TFR)))
    drop = pairs[0][1] - pairs[-1][1]
    assert abs(drop - 4.7) < 1e-9, \
        f"the best schooled must sit 4.7 children per woman below the least schooled; got {drop}"
    assert drop > 0, "the movement must be downward"
    return (f"the least schooled country records {pairs[0][1]} and the best schooled "
            f"{pairs[-1][1]} children per woman, a difference of {drop:.1f}")


def q19(table, item):
    rates = _falls_with(table, AGEFIRST2, TFR)
    ages = cg.col(table, AGEFIRST2)
    assert len(set(ages)) == len(ages), "'all four record the same age' must be false"
    return (f"sorted by mean age at first birth the fertility rates read {rates}, strictly "
            "falling across the four populations")


def q20(table, item):
    labels = cg.labels(table)
    rates = cg.col(table, TFR)
    below = [labels[i] for i, r in enumerate(rates) if r < REPLACEMENT]
    assert below == ["Population 4"], \
        f"exactly Population 4 must lie below {REPLACEMENT}; got {below}"
    return (f"the rates read {rates} children per woman, of which exactly one lies below "
            f"the replacement level of {REPLACEMENT} stated in the stem")


def q21(table, item):
    rates = _falls_with(table, ACCESS, TFR)
    access = dict(zip(cg.labels(table), cg.col(table, ACCESS)))
    tfr = dict(zip(cg.labels(table), cg.col(table, TFR)))
    least = min(access, key=access.get)
    assert tfr[least] == max(tfr.values()), \
        "the district with the least access must hold the highest rather than the lowest rate"
    return (f"sorted by reported access the fertility rates read {rates}, strictly falling "
            "across the four districts")


def q23(table, item):
    pay = cg.col(table, PAYMENT)
    rates = cg.col(table, TFR)
    assert all(pay[i + 1] > pay[i] for i in range(len(pay) - 1)), \
        f"the payment must rise at every period; got {pay}"
    assert all(rates[i + 1] > rates[i] for i in range(len(rates) - 1)), \
        f"the fertility rate must rise at every period; got {rates}"
    assert rates[0] == min(rates), "'the rate was highest before the payment began' must be false"
    return (f"in period order the payment index reads {pay} and the fertility rate "
            f"{rates}, both rising at every step")


def q24(table, item):
    pay = cg.col(table, PAYMENT)
    rates = cg.col(table, TFR)
    assert pay[0] == 0, f"the first period must precede the payment; got {pay[0]}"
    assert pay[-1] == max(pay), "the payment must stand at its highest in the last period"
    assert rates[-1] > rates[0], "the fertility rate must end above where it began"
    return (f"the record runs from no payment at a rate of {rates[0]} to a payment index of "
            f"{pay[-1]:.0f} at a rate of {rates[-1]}, which is a government act")


def q25(table, item):
    for driver in (CARE, NUTRITION):
        pairs = sorted(zip(cg.col(table, driver), cg.col(table, DEATHS)))
        assert all(pairs[i + 1][1] < pairs[i][1] for i in range(len(pairs) - 1)), \
            f"sorted by {driver!r} the infant deaths must fall strictly; got {pairs}"
    deaths = cg.col(table, DEATHS)
    assert len(set(deaths)) == len(deaths), "'all four record the same deaths' must be false"
    return (f"sorted by healthcare access and then by nutrition, the infant deaths read "
            f"{sorted(deaths, reverse=True)} per thousand live births, falling both times")


def q27(table, item):
    care = cg.col(table, CARE)
    deaths = cg.col(table, DEATHS)
    assert all(care[i + 1] > care[i] for i in range(len(care) - 1)), \
        f"access must rise at every survey; got {care}"
    assert all(deaths[i + 1] < deaths[i] for i in range(len(deaths) - 1)), \
        f"infant deaths must fall at every survey; got {deaths}"
    return (f"in survey order the access column reads {care} percent, rising throughout, "
            f"while the infant deaths read {deaths}, falling throughout")


def q28(table, item):
    deaths = cg.col(table, DEATHS)
    drop = deaths[0] - deaths[-1]
    assert abs(drop - 77) < 1e-9, f"the fall must be 77 per thousand; got {drop}"
    assert drop > 0, "the movement must be a fall rather than a rise"
    return (f"infant deaths run from {deaths[0]:.0f} to {deaths[-1]:.0f} per thousand live "
            f"births, a fall of {drop:.0f}")


CLAIMS = [
 ("educational opportunities for females, access to family planning",
  "EIN-1.B.1, near verbatim: total fertility rate is affected by the age at which females have their first child, educational opportunities for females, access to family planning, and government acts and policies. The rejected sets each replace at least one of those four with a geographic or ecological quantity the statement never names."),
 ("mean elevation of the country",
  "EIN-1.B.1 names four factors and elevation is not among them, while each of the four rejected options appears in the statement word for word."),
 ("considered relatively stable",
  "EIN-1.B.2, near verbatim: if fertility rate is at replacement levels, a population is considered relatively stable. The framework attaches no other description to that condition."),
 ("access to good healthcare and nutrition",
  "EIN-1.B.3, near verbatim: factors associated with infant mortality rates include whether mothers have access to good healthcare and nutrition. No geographic or agricultural factor is named."),
 ("Changes in whether mothers have access",
  "EIN-1.B.3's second sentence states that changes in these factors can lead to changes in infant mortality rates over time, so the rate is neither fixed nor tied to land area or elevation."),
 ("holds close to steady rather than one fixed exactly",
  "EIN-1.B.2 qualifies its claim with RELATIVELY stable, which describes a population held near a steady size rather than one pinned exactly, so small movements do not contradict it."),
 ("set by the climate and elevation of the region",
  "EIN-1.B.1, EIN-1.B.2 and EIN-1.B.3 supply the four rejected statements between them, and none of the three names climate or elevation. That pairing is an addition to the framework."),
 ("are the countries with the lower fertility rates",
  "Recomputed in q8 above: sorting by the age at first birth, by schooling and by family planning access in turn each leaves fertility strictly falling. EIN-1.B.1 names all three among the things that affect total fertility rate."),
 ("Country 1",
  "Recomputed in q9 above: the uniquely smallest age at first birth and the uniquely largest fertility rate fall in the same row. EIN-1.B.1 names the age at which females have their first child as a factor affecting fertility."),
 ("4.0 children per woman",
  "Recomputed in q10 above: the largest and smallest fertility rates differ by 4.0. EIN-1.B.1 makes total fertility rate the quantity the other columns are said to affect."),
 ("Country B",
  "Recomputed in q11 above: exactly one of the five rates equals the replacement level of 2.1 stated in the stem. EIN-1.B.2 states that a population at replacement level fertility is considered relatively stable."),
 ("Two of them",
  "Recomputed in q12 above: exactly two of the five rates lie strictly below the replacement level stated in the stem, and not all five do. EIN-1.B.2 makes replacement level the reference for relative stability."),
 ("Group 2",
  "Recomputed in q13 above: dividing children by women gives exactly one group at the replacement level stated in the stem. EIN-1.B.2 calls a population at that level relatively stable."),
 ("4.3 children per woman",
  "Recomputed in q14 above: the uniquely largest group's children divided by its women give 4.3. EIN-1.B.2 treats fertility as a per woman quantity by comparing it with a replacement level."),
 ("2.1 children per woman",
  "Recomputed in q15 above: the six band rates total 420 per thousand per year, which the rule stated in the stem turns into 2.1 children per woman. EIN-1.B.2 supplies the reading of a rate at replacement level."),
 ("2.7 children per woman, which lies above replacement",
  "Recomputed in q16 above: the six band rates total 540 per thousand per year, giving 2.7 children per woman, above the replacement level stated in the stem. EIN-1.B.2 reserves relative stability for a population at replacement."),
 ("falls at every step as the mean years of schooling rise",
  "Recomputed in q17 above: sorting by mean years of schooling leaves fertility strictly falling. EIN-1.B.1 names educational opportunities for females among the things affecting total fertility rate."),
 ("Lower by 4.7 children per woman",
  "Recomputed in q18 above: the best schooled and least schooled rows differ by 4.7 children per woman, downward. EIN-1.B.1 names educational opportunities for females as a factor affecting fertility."),
 ("falls at every step as the mean age at first birth rises",
  "Recomputed in q19 above: sorting by the mean age at first birth leaves fertility strictly falling. EIN-1.B.1 names the age at which females have their first child among the things affecting fertility."),
 ("Population 4",
  "Recomputed in q20 above: exactly one of the four rates lies below the replacement level stated in the stem. EIN-1.B.2 makes replacement level the reference at which a population is considered relatively stable."),
 ("falls at every step as reported access to those services rises",
  "Recomputed in q21 above: sorting by reported access leaves fertility strictly falling, and the district with the least access carries the highest rather than the lowest rate. EIN-1.B.1 names access to family planning as a factor affecting fertility."),
 ("Access to family planning",
  "EIN-1.B.1 lists access to family planning among the four things affecting total fertility rate, and opening clinics that provide contraception changes exactly that access rather than schooling, age at first birth or nutrition."),
 ("rose in each successive period as the payment rose",
  "Recomputed in q23 above: in period order both the payment index and the fertility rate rise at every step, and the rate is at its lowest before the payment began. EIN-1.B.1 names government acts and policies among the things affecting fertility."),
 ("Government acts and policies",
  "Recomputed in q24 above: the record runs from no payment to the largest payment, with fertility ending above where it began. A payment made by a government to families for each child is a government act, which EIN-1.B.1 names as a factor affecting total fertility rate."),
 ("fall as both kinds of access rise",
  "Recomputed in q25 above: sorting by healthcare access and then by nutrition each leaves infant deaths strictly falling. EIN-1.B.3 names both as factors associated with infant mortality rates."),
 ("changes in access to healthcare and nutrition can lead to changes in infant mortality rates",
  "EIN-1.B.3's second sentence states exactly that, so the framework treats infant mortality as something that moves rather than as a fixed property of a country."),
 ("Access rose at each survey while infant deaths",
  "Recomputed in q27 above: in survey order the access column rises at every step and the infant deaths fall at every step. EIN-1.B.3 states that changes in mothers' access to good healthcare can lead to changes in infant mortality over time."),
 ("They fell by 77",
  "Recomputed in q28 above: the first and last entries of the infant deaths column differ by 77 per thousand live births, downward. EIN-1.B.3 makes such a movement over time the thing changes in access can lead to."),
 ("looking for movement in fertility as each of them differs",
  "EIN-1.B.1 asserts that four named things affect total fertility rate, so the evidence bearing on it varies those four across populations and watches the fertility rate, rather than measuring a single case or a quantity the statement never names."),
 ("considered relatively stable; and mothers' access to healthcare",
  "EIN-1.B.1 supplies the four factors, EIN-1.B.2 the replacement level reading, and EIN-1.B.3 both the factors associated with infant mortality and the statement that changes in them can change that mortality over time. Every rejected summary swaps a factor, reverses the replacement reading, or fixes infant mortality."),
]

TABLE_CHECKS = {8: q8, 9: q9, 10: q10, 11: q11, 12: q12, 13: q13, 14: q14,
                15: q15, 16: q16, 17: q17, 18: q18, 19: q19, 20: q20, 21: q21,
                23: q23, 24: q24, 25: q25, 27: q27, 28: q28}

if "--selftest" in sys.argv:
    es.selftest(e3_7, CLAIMS, TABLE_CHECKS)

e_check.run(e3_7, CLAIMS, TABLE_CHECKS)
