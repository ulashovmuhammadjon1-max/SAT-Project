"""Key audit for AP ENVIRONMENTAL SCIENCE 7.1 Introduction to Air Pollution.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. `claim` states what the key rests on, for a human to audit; the
structural gate is `cg_check.check` and the notation gate and negative control
are in `es_check`.

WHAT THE KEYS REST ON
---------------------
Items 1, 2 and 15 rest on STB-2.A.1, the four releases of coal combustion.
Items 3, 4, 20 and 26 rest on STB-2.A.2, the nitrogen oxides released by fossil
fuel combustion and the three consequences the framework attaches to them.
Items 5, 23 and 29 rest on the second sentence of STB-2.A.2, the carbon
monoxide, hydrocarbons and particulate matter.
Items 6, 16, 22, 25 and 27 rest on STB-2.A.3, the sulfur dioxide released when
fossil fuels, mainly diesel fuels, are burned.
Items 7, 8 and 17 rest on STB-2.A.4, the regulation of lead under the Clean Air
Act and the resulting decrease in atmospheric lead.
Items 9, 10, 11, 19 and 28 rest on STB-2.A.5, that air pollutants can be
primary or secondary. The framework names the two categories without defining
them; the only definitional content used here is that a primary pollutant is
released by its source and a secondary one forms in the atmosphere out of what
was released, which is the minimum required by the framework's own example in
STB-2.A.2 of nitrogen oxides LEADING TO ozone and CONVERTING TO nitric acid.
The sorting information a student needs is always in the stem or the table.
Items 12, 18, 24 and 30 rest on the learning objective STB-2.A itself, identify
the sources and effects of air pollutants, and on suggested skill 4.E, explain
modifications to an experimental procedure that will alter results.
Item 21 rests on enduring understanding STB-2, that human activities have
consequences for the atmosphere.

DATA ITEMS: 2, 6, 7, 9, 13 and 14 carry tables, and each keyed conclusion is
recomputed below from that table alone, with the rejected readings falsified
against the same numbers. No item asks a student to recall a measured value.

NEGATIVE CONTROL: `python3 verify_e7_1.py --selftest` rotates every key,
corrupts every table cell in turn, injects each banned notation form, and
requires each to be caught.
"""
import sys

import cg_check as cg
import es_check as es
import e7_1

MASS = "Mass released per gigajoule of heat produced (grams)"
SO2_FUEL = "Sulfur dioxide released per 100 liters burned (grams)"
PB_FUEL = "Lead in gasoline sold nationally (grams per liter)"
PB_AIR = "Lead measured in urban air (micrograms per cubic meter)"
DIRECT = "Released directly from a tailpipe or smokestack"
FORMED = "Formed in the air out of substances already released"
DIST = "Distance from the highway (meters)"
CO = "Carbon monoxide measured (parts per million)"
COAL = "Released by the plant while burning coal (tons per year)"
GAS = "Released by the plant after switching to natural gas (tons per year)"


def q2(table, item):
    vals = dict(zip(cg.labels(table), cg.col(table, MASS)))
    top = max(vals, key=vals.get)
    assert top == "Carbon dioxide", f"the largest release is {top}"
    others = sum(v for k, v in vals.items() if k != "Carbon dioxide")
    assert vals["Carbon dioxide"] > 10 * others, \
        "carbon dioxide is not by far the largest release"
    assert min(vals, key=vals.get) == "Toxic metals", \
        "the metals must be the smallest release, so 'metals dominate' is false"
    assert len(vals) > 1, "a single-pollutant reading must be false on this table"
    return (f"carbon dioxide at {vals['Carbon dioxide']:.0f} grams exceeds ten times the "
            f"sum of the other four, {others:.0f}, and the metals are the smallest entry")


def q6(table, item):
    vals = dict(zip(cg.labels(table), cg.col(table, SO2_FUEL)))
    top = max(vals, key=vals.get)
    assert top == "Diesel", f"the largest release is {top}, not diesel"
    rest = sorted(v for k, v in vals.items() if k != "Diesel")
    assert vals["Diesel"] > 10 * rest[-1], "diesel is not far above the next fuel"
    assert vals["Gasoline"] < vals["Diesel"], "'gasoline above diesel' must be false"
    assert min(vals, key=vals.get) == "Compressed natural gas", \
        "'natural gas is the largest source' must be false"
    return (f"diesel at {vals['Diesel']:.0f} grams is more than ten times the next fuel, "
            f"{rest[-1]:.0f}, so the equal-amounts and gasoline-above-diesel readings fail")


def q7(table, item):
    fuel = cg.col(table, PB_FUEL)
    air = cg.col(table, PB_AIR)
    years = cg.labels(table)
    assert years == sorted(years), f"the record must run forward in time, got {years}"
    for series, name in ((fuel, "fuel"), (air, "air")):
        assert all(series[i] > series[i + 1] for i in range(len(series) - 1)), \
            f"the {name} column does not fall in every interval: {series}"
        assert series[0] > 10 * series[-1], f"the {name} column does not fall dramatically"
    assert air[-1] > 0, "'fell to zero' must be false, so the last air value must be positive"
    return (f"fuel lead runs {fuel} and air lead runs {air}; both fall in every interval "
            "by more than a factor of ten, and the final air value is above zero")


def q9(table, item):
    rows = {r[0]: r[1:] for r in table["rows"]}
    heads = table["headers"][1:]
    for label, cells in rows.items():
        assert set(cells) <= {"yes", "no"}, f"{label} has a cell that is not yes or no"
        assert cells.count("yes") == 1, f"{label} must be marked in exactly one column"
    j_direct = heads.index(DIRECT)
    j_formed = heads.index(FORMED)
    secondary = [lab for lab, cells in rows.items() if cells[j_formed] == "yes"]
    primary = [lab for lab, cells in rows.items() if cells[j_direct] == "yes"]
    assert secondary == ["Ozone", "Nitric acid"], f"the formed-in-air rows are {secondary}"
    for lab in ("Sulfur dioxide", "Nitrogen oxides", "Carbon monoxide"):
        assert lab in primary, f"{lab} must be marked as released directly"
    return (f"the table marks {secondary} as formed in the air and {primary} as released "
            "directly, so ozone is the only keyed option in the formed group")


def q13(table, item):
    pairs = sorted(zip(cg.col(table, DIST), cg.col(table, CO)))
    assert all(pairs[i][1] > pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"carbon monoxide does not fall with distance: {pairs}"
    assert pairs[-1][1] < pairs[0][1], "the farthest site must not hold the highest value"
    assert len(set(v for _, v in pairs)) == len(pairs), "'same at every distance' must be false"
    return (f"sorted by distance the concentrations are {[v for _, v in pairs]}, strictly "
            "decreasing, so the rising, equal and farthest-highest readings are all false")


def q14(table, item):
    before = dict(zip(cg.labels(table), cg.col(table, COAL)))
    after = dict(zip(cg.labels(table), cg.col(table, GAS)))
    frac = {k: (before[k] - after[k]) / before[k] for k in before}
    best = max(frac, key=frac.get)
    assert best == "Sulfur dioxide", f"the largest fractional fall belongs to {best}"
    rest = [v for k, v in frac.items() if k != "Sulfur dioxide"]
    assert all(v < frac["Sulfur dioxide"] for v in rest), "another pollutant ties or beats it"
    assert len(set(round(v, 6) for v in frac.values())) > 1, \
        "'all fall by the same fraction' must be false"
    return ("the fractional reductions are " +
            ", ".join(f"{k} {frac[k]:.3f}" for k in frac) +
            ", so sulfur dioxide falls by the largest fraction and no two are equal")


CLAIMS = [
 ("toxic metals, and particulates",
  "STB-2.A.1, near verbatim: coal combustion releases air pollutants including carbon dioxide, sulfur dioxide, toxic metals, and particulates. The rejected options name noble gases, a manufactured refrigerant, a gas released from bedrock, and biological material, none of which the framework attributes to burning coal."),
 ("by far the greatest mass",
  "Recomputed in q2 above from the tabulated masses. STB-2.A.1 lists sulfur dioxide, toxic metals and particulates alongside carbon dioxide, so the smaller releases are pollutants too, which is why a single-pollutant or a metals-dominate reading fails."),
 ("conversion to nitric acid that causes acid rain",
  "STB-2.A.2, near verbatim: nitrogen oxides released by fossil fuel combustion lead to the production of ozone, the formation of photochemical smog, and convert to nitric acid in the atmosphere, causing acid rain. The framework gives them no role in depleting stratospheric ozone or in cooling the lower atmosphere."),
 ("convert to nitric acid in the atmosphere",
  "STB-2.A.2 places the conversion in the atmosphere, after release, so the acid is not emitted ready-made from an engine. Carbon monoxide and unreactive nitrogen gas are not given as sources of nitric acid anywhere in the framework."),
 ("Carbon monoxide, hydrocarbons, and particulate matter",
  "STB-2.A.2, second sentence, near verbatim: other pollutants produced by fossil fuel combustion include carbon monoxide, hydrocarbons, and particulate matter. Chlorofluorocarbons and halons are manufactured chemicals, and radon, mold, asbestos and formaldehyde are indoor pollutants under STB-2.E."),
 ("far more sulfur dioxide per hundred liters",
  "Recomputed in q6 above: diesel exceeds ten times the next fuel in the table. STB-2.A.3 states that air quality can be affected through the release of sulfur dioxide during the burning of fossil fuels, mainly diesel fuels, and sulfur dioxide leaves the exhaust already formed."),
 ("fell as lead in gasoline fell",
  "Recomputed in q7 above: both columns fall in every interval by more than a factor of ten and the final air value is above zero. STB-2.A.4 credits the regulation of lead, particularly in fuels, with dramatically decreasing atmospheric lead."),
 ("acting through the Clean Air Act",
  "STB-2.A.4 names the Environmental Protection Agency and the Clean Air Act as the agency and the law under which the use of lead, particularly in fuels, was regulated. No voluntary agreement, ozone treaty or speed limit is given that role."),
 ("forming in the air rather than leaving a tailpipe",
  "Recomputed in q9 above from the two marked columns. STB-2.A.5 states that air pollutants can be primary or secondary, and the category a substance falls into turns on where it is formed rather than on its concentration, its physical state, or its mere presence."),
 ("forms in the atmosphere out of substances already released",
  "STB-2.A.5 names the two categories, and STB-2.A.2 supplies the framework's own worked example: nitrogen oxides are released and then lead to ozone and convert to nitric acid. So the distinction is where the substance forms, not how harmful it is, what state it is in, or whether it is regulated."),
 ("formed in the atmosphere from substances that were released earlier",
  "The claim under test allows only direct release, so what refutes it is the existence of the secondary category named in STB-2.A.5. Differences in amount, season, distance travelled and physical state are all compatible with every pollutant having been released directly."),
 ("several distances from the highway during the same hours",
  "Suggested skill 4.E, explain modifications to an experimental procedure that will alter results. A source claim needs a comparison across distance with time of day held constant; a more sensitive instrument, a restricted set of days, a maximum in place of a mean, or a site moved nearer leave nothing to compare."),
 ("falls steadily with distance from the highway",
  "Recomputed in q13 above: sorted by distance the concentrations decrease at every step, so the rising, constant and farthest-highest readings are false on the same numbers. STB-2.A.2 places carbon monoxide among the products of fossil fuel combustion."),
 ("Sulfur dioxide falls by the largest fraction",
  "Recomputed in q14 above: the fractional reductions are computed for all four pollutants and sulfur dioxide's is the largest, with no two equal. STB-2.A.1 and STB-2.A.3 both tie sulfur dioxide to the burning of the sulfur-bearing fuel."),
 ("products of all of them along with unburned solid particles",
  "STB-2.A.1 lists four different releases from one fuel, which follows from the fuel containing carbon, sulfur and metallic impurities and from solid material being carried up in the exhaust. Quantity burned, location of burning and later disposal do not explain a mixture of products."),
 ("a source of the sulfur dioxide measured at the station",
  "STB-2.A.3 attributes sulfur dioxide affecting air quality to the burning of fossil fuels. A pollutant that rises and falls with the operation of one identified source supports that source contributing, but a single correlation cannot establish that no other source exists."),
 ("wherever those vehicles went",
  "STB-2.A.4 singles out fuels as the regulated use of lead and credits the regulation with a dramatic decrease in atmospheric lead, which follows from that fuel being burned in very many engines spread across the country. Lead is a metal with many other uses and does not become harmless on release."),
 ("record the wind direction with every sample",
  "Suggested skill 4.E. Separating two candidate sources requires sampling positioned around both and a record of the air movement at the time of each sample; longer runs, calm days only, a different pollutant, or a single annual average all discard exactly the information that distinguishes them."),
 ("produced in the atmosphere from pollutants that had been released",
  "STB-2.A.5 with the example in STB-2.A.2, where nitrogen oxides released by combustion lead to the production of ozone. The classification describes where the ozone was formed and carries no implication about its harmfulness or about any single smokestack."),
 ("one release leads to the other effect",
  "STB-2.A.2 links them directly: combustion releases nitrogen oxides, which convert to nitric acid in the atmosphere, causing acid rain. The link is a chemical conversion after release rather than a coincidence, a direct emission of acid, or a neutralization."),
 ("ordinary components of clean air",
  "Enduring understanding STB-2 makes air pollution a consequence of human activities for the atmosphere, and STB-2.A identifies pollutants by their sources and effects. That excludes the ordinary constituents of clean air, and it does not make visibility, statutory listing, indoor origin or small concentration the test."),
 ("vehicles that do not burn diesel fuel",
  "STB-2.A.3 attributes the sulfur dioxide that affects air quality to burning fossil fuels, mainly diesel fuels, so removing diesel combustion removes the source the framework names. Paint color, small load reductions, exhaust noise and washing do not change the sulfur burned."),
 ("one of the pollutants produced by the combustion of fossil fuels",
  "STB-2.A.2 lists carbon monoxide among the pollutants produced by fossil fuel combustion, which is what vehicles at an intersection are doing. The framework gives carbon monoxide no atmospheric formation route, no pavement source and no corrosion source."),
 ("standard height away from the shelter",
  "Suggested skill 4.E. A sampler in a sheltered alcove is not exposed to the air the study is about, so the modification that changes the result is to sample that air under standard conditions; longer runs and scaled readings preserve the same bias."),
 ("solid material carried up by the hot gases",
  "STB-2.A.1 lists both sulfur dioxide and particulates among the releases of coal combustion, and the difference in physical state reflects different constituents of the same fuel leaving in the same exhaust stream. Neither is a frozen form of the other and both are named as pollutants."),
 ("lead to ozone production and to photochemical smog",
  "STB-2.A.2 attaches three separate consequences to the nitrogen oxides released by combustion, so a single reduction reaches all three. The framework gives nitrogen oxides no scrubbing effect on particulates, no settling behavior, and no secondary-pollutant status."),
 ("measured in both neighborhoods over the same period",
  "STB-2.A.3 makes sulfur dioxide the pollutant tied to diesel combustion, so measuring it in the exposed and the comparison neighborhood over the same period is the measurement that tests the claim. Tree counts, population, housing age and complaint counts measure something other than the air."),
 ("in the form in which it is measured",
  "STB-2.A.5 with STB-2.A.2. A primary pollutant is released by its source in the form in which it is found, which is sulfur dioxide leaving a stack; ozone, nitric acid, a haze that develops over hours and an acid formed in cloud droplets are all produced in the atmosphere after release."),
 ("carbon monoxide, and hydrocarbons",
  "STB-2.A.1 and STB-2.A.2 together name several fuels and several pollutants, which is what a many-source description rests on. Each rejected pairing attaches to a framework statement an assertion the framework does not make, about abundance, exclusive regulation, a single fuel, or a reverse conversion."),
 ("the harm it does once it is there",
  "Learning objective STB-2.A asks students to identify the sources and effects of air pollutants, so the source is the activity that releases the substance and the effect is what it does after release. An instrument, a date, a season or a chemical formula answers a different question."),
]

TABLE_CHECKS = {2: q2, 6: q6, 7: q7, 9: q9, 13: q13, 14: q14}

es.run(e7_1, CLAIMS, TABLE_CHECKS, sys.argv)
