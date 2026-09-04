"""Key audit for AP ENVIRONMENTAL SCIENCE 6.8 Solar Energy.

One (anchor, claim) per item, in module order. The anchor must appear in the
KEYED choice and in no distractor, so an off-by-one key or a reordered choice
list fails here rather than reaching a student.

WHAT THE KEYS REST ON
---------------------
  ENG-3.J.1  Photovoltaic solar cells capture light energy from the sun and
             transform it directly into electrical energy. Their use is limited
             by the availability of sunlight.
                              -- items 1, 2, 8, 14, 15, 17, 18, 19, 20
  ENG-3.J.2  Active solar energy systems use solar energy to heat a liquid
             through mechanical and electric equipment to collect and store the
             energy captured from the sun.   -- items 3, 6, 8, 13, 21
  ENG-3.J.3  Passive solar energy systems absorb heat directly from the sun
             without the use of mechanical and electric equipment, and energy
             cannot be collected or stored.  -- items 4, 5, 6, 7, 13, 21, 22, 23
  ENG-3.K.1  Solar energy systems have low environmental impact and produce
             clean energy, but they can be expensive. Large solar energy farms
             may negatively impact desert ecosystems.
                              -- items 9, 10, 11, 12, 16, 24, 25, 26, 27, 28, 29
  item 30 reads across all four.

ACTIVE AND PASSIVE ARE THE SHARPEST SWAP IN THIS UNIT. The two statements are
built from the same three properties with the values reversed: equipment yes or
no, a liquid heated or heat absorbed directly, energy collected and stored or
not. An anchor reading only "the active system" would match the distractor that
attaches the passive properties to it, so every anchor naming a system carries
the property with the name, and items 6, 7, 13, 21 and 22 carry both clauses.

THREE THINGS ARE CALLED DIRECT here and they are not the same: light transformed
DIRECTLY INTO ELECTRICAL ENERGY in ENG-3.J.1, and heat absorbed DIRECTLY FROM
THE SUN in ENG-3.J.3. Item 8 compares photovoltaic cells with active systems by
what each PRODUCES rather than by that word, and no key treats either sense as
the other.

TWO HEDGES, BOTH KEYED. ENG-3.K.1 says solar systems CAN BE expensive and that
LARGE farms MAY negatively impact DESERT ecosystems. Items 12 and 29 key the
hedges, and no key anywhere states either claim without them -- item 29 in
particular refuses to let a three-plot survey become a universal claim.

DATA ITEMS: 17 to 29, thirteen of them, because the suggested skill for this
topic is 5.C, explain patterns and trends in data to draw conclusions. Every
figure is recomputed below from the item's own table.

THE SUNLIGHT TABLE SURVIVES A COLUMN REVERSAL with its (hours, output) pairs
intact, so all four checks that read it also pin the least and most sunny sites
BY ROW LABEL. Without that, the trend, the rate for each hour, the prediction
and the difference would all be unchanged by a reversal and the checks would
say nothing.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and every table in turn, and requires each
corruption to raise, BEFORE the real gate runs. It is not behind a flag.
``python3 verify_e6_8.py --selftest`` adds the stronger property that a
REVERSAL ALONE is caught for every table, without e_check's flatten fallback.
"""
import e_check
import cg_check as cg
import e6_8

HOURS = "Hours of sunlight in an average day"
OUTPUT = "Electricity the array delivers each day (energy units)"
S1, S2, S3, S4 = "Site 1", "Site 2", "Site 3", "Site 4"

KIT = "Pieces of mechanical and electric equipment fitted"
LITRES = "Heated liquid held for use after dark (litres)"
DELIVERED = "Heat delivered to the house on a sunny day (energy units)"
SYS1, SYS2 = "System 1", "System 2"

BUILD = "Cost to build for each unit of capacity (currency units)"
POLLUTE = "Air pollutants released for each unit of electricity (grams)"
ARRAY, GASPLANT = "Solar array", "Gas plant"

PANELS = "Area under solar panels (hectares)"
PLANTS = "Native plant species recorded"
REPTILES = "Reptile species recorded"
P1 = "Plot 1, with no farm"
P2 = "Plot 2, with a small farm"
P3 = "Plot 3, with a large farm"


def _pin_sun(table):
    """The sites must sit on the rows they are keyed to.

    Reversing both numeric columns of this table leaves the (hours, output)
    pairs exactly as they were, so the trend, the rate for each hour, the
    prediction and the extreme difference are all unchanged by a reversal.
    Naming the least and most sunny sites is what a reversal breaks.
    """
    hours = cg.col(table, HOURS)
    assert cg.cell(table, S1, HOURS) == min(hours), "the first site must be the least sunny"
    assert cg.cell(table, S4, HOURS) == max(hours), "the fourth site must be the sunniest"


def q17(table, item):
    _pin_sun(table)
    hours = [cg.cell(table, s, HOURS) for s in (S1, S2, S3, S4)]
    out = [cg.cell(table, s, OUTPUT) for s in (S1, S2, S3, S4)]
    assert all(hours[i] < hours[i + 1] for i in range(3)), f"sunlight must rise; got {hours}"
    assert all(out[i] < out[i + 1] for i in range(3)), f"output must rise with it; got {out}"
    assert min(out) > 0, "'the array delivers nothing at the least sunny site' must be false"
    return (f"sunlight runs {hours} hours a day against output of {out} energy units, the two "
            "rising together across the four sites")


def _rate(table):
    _pin_sun(table)
    rates = [cg.cell(table, s, OUTPUT) / cg.cell(table, s, HOURS) for s in (S1, S2, S3, S4)]
    assert len(set(rates)) == 1, f"the output for each hour must be the same at every site; got {rates}"
    return rates[0]


def q18(table, item):
    rate = _rate(table)
    assert rate == 50, f"the rate recomputes to {rate}, not 50 energy units for each hour"
    for wrong in (cg.cell(table, S1, OUTPUT), 30):
        assert rate != wrong, f"the {wrong} distractor equals the key"
    return (f"output divided by sunlight hours gives {rate:.0f} energy units for each hour at "
            "every one of the four sites")


def q19(table, item):
    rate = _rate(table)
    predicted = rate * 6
    assert predicted == 300, f"the prediction recomputes to {predicted}, not 300 energy units"
    for wrong in (cg.cell(table, S2, OUTPUT), cg.cell(table, S3, OUTPUT),
                  12 * rate, cg.cell(table, S1, OUTPUT)):
        assert predicted != wrong, f"the {wrong} distractor equals the key"
    return (f"six hours at {rate:.0f} energy units for each hour is {predicted:.0f} energy units "
            "a day at the fifth site")


def q20(table, item):
    _pin_sun(table)
    gap = cg.cell(table, S4, OUTPUT) - cg.cell(table, S1, OUTPUT)
    assert gap == 350, f"the gap recomputes to {gap}, not 350 energy units"
    for wrong in (cg.cell(table, S4, OUTPUT),
                  cg.cell(table, S4, OUTPUT) + cg.cell(table, S1, OUTPUT),
                  cg.cell(table, S3, OUTPUT) - cg.cell(table, S2, OUTPUT),
                  cg.cell(table, S2, OUTPUT)):
        assert gap != wrong, f"the {wrong} distractor equals the key"
    return (f"{cg.cell(table, S4, OUTPUT):.0f} minus {cg.cell(table, S1, OUTPUT):.0f} is "
            f"{gap:.0f} energy units more a day at the sunniest site")


def q21(table, item):
    assert cg.cell(table, SYS1, KIT) > 0, "the first system must carry mechanical and electric equipment"
    assert cg.cell(table, SYS1, LITRES) > 0, "the first system must store heated liquid"
    assert cg.cell(table, SYS2, KIT) == 0, "the second system must carry no equipment"
    assert cg.cell(table, SYS2, LITRES) == 0, "the second system must store nothing"
    assert cg.cell(table, SYS2, DELIVERED) > 0, \
        "the second system must still deliver heat, or it would not be a solar system at all"
    return (f"the first house carries {cg.cell(table, SYS1, KIT):.0f} pieces of equipment and "
            f"{cg.cell(table, SYS1, LITRES):.0f} litres of stored liquid, the second carries "
            f"{cg.cell(table, SYS2, KIT):.0f} and {cg.cell(table, SYS2, LITRES):.0f} while still "
            f"delivering {cg.cell(table, SYS2, DELIVERED):.0f} energy units of heat")


def q22(table, item):
    assert cg.cell(table, SYS2, KIT) == 0, "the passive house must carry no equipment"
    assert cg.cell(table, SYS2, LITRES) == 0, "the passive house must collect and store nothing"
    assert cg.cell(table, SYS2, DELIVERED) > 0, \
        "the passive house must absorb heat, or the first half of the statement fails"
    assert cg.cell(table, SYS1, LITRES) > 0, \
        "the other house must store something, or 'an active system stores' goes unshown"
    return (f"the second house delivers {cg.cell(table, SYS2, DELIVERED):.0f} energy units of "
            f"heat while holding {cg.cell(table, SYS2, LITRES):.0f} litres and carrying "
            f"{cg.cell(table, SYS2, KIT):.0f} pieces of equipment")


def q23(table, item):
    gap = cg.cell(table, SYS1, DELIVERED) - cg.cell(table, SYS2, DELIVERED)
    assert gap == 200, f"the gap recomputes to {gap}, not 200 energy units"
    assert gap > 0, "the house with the equipment must deliver the more heat"
    for wrong in (cg.cell(table, SYS1, DELIVERED),
                  cg.cell(table, SYS1, DELIVERED) + cg.cell(table, SYS2, DELIVERED),
                  cg.cell(table, SYS1, LITRES),
                  cg.cell(table, SYS2, DELIVERED)):
        assert gap != wrong, f"the {wrong} distractor equals the key"
    return (f"{cg.cell(table, SYS1, DELIVERED):.0f} minus "
            f"{cg.cell(table, SYS2, DELIVERED):.0f} is {gap:.0f} energy units more heat from the "
            "house with the equipment")


def q24(table, item):
    assert cg.cell(table, ARRAY, POLLUTE) == 0, "the array must release no air pollutants"
    assert cg.cell(table, GASPLANT, POLLUTE) > 0, "the gas plant must release some"
    assert cg.cell(table, ARRAY, BUILD) > cg.cell(table, GASPLANT, BUILD), \
        "the array must be the dearer to build, or the trade-off does not appear"
    return (f"the array releases {cg.cell(table, ARRAY, POLLUTE):.0f} grams of air pollutants "
            f"against {cg.cell(table, GASPLANT, POLLUTE):.0f}, and costs "
            f"{cg.cell(table, ARRAY, BUILD):.0f} currency units to build against "
            f"{cg.cell(table, GASPLANT, BUILD):.0f}")


def q25(table, item):
    ratio = cg.cell(table, ARRAY, BUILD) / cg.cell(table, GASPLANT, BUILD)
    assert ratio == 3, f"the ratio recomputes to {ratio}, not 3"
    assert ratio > 1, "'the array is the cheaper of the two' must be false"
    for wrong in (2, 9, 30):
        assert ratio != wrong, f"the {wrong} distractor equals the key"
    return (f"{cg.cell(table, ARRAY, BUILD):.0f} divided by "
            f"{cg.cell(table, GASPLANT, BUILD):.0f} is {ratio:.0f} times as much to build for "
            "each unit of capacity")


def q26(table, item):
    assert cg.cell(table, ARRAY, POLLUTE) == 0, \
        "the array's pollutant figure must be zero for the cleanliness claim to be read off it"
    assert cg.cell(table, GASPLANT, POLLUTE) > 100, \
        "the comparison must be wide enough to be a reading rather than a rounding"
    assert cg.cell(table, ARRAY, BUILD) != cg.cell(table, ARRAY, POLLUTE), \
        "the two columns must be distinguishable, so the wrong one cannot be read for the right"
    return (f"the array releases {cg.cell(table, ARRAY, POLLUTE):.0f} grams of air pollutants for "
            f"each unit of electricity against the gas plant's "
            f"{cg.cell(table, GASPLANT, POLLUTE):.0f}, which is a reading about cleanliness "
            "rather than about cost")


def _desert(table):
    assert cg.cell(table, P1, PANELS) == 0, "the first plot must carry no farm"
    assert cg.cell(table, P3, PANELS) == max(cg.col(table, PANELS)), \
        "the third plot must carry the largest farm"
    plants = [cg.cell(table, p, PLANTS) for p in (P1, P2, P3)]
    reptiles = [cg.cell(table, p, REPTILES) for p in (P1, P2, P3)]
    return plants, reptiles


def q27(table, item):
    plants, reptiles = _desert(table)
    area = [cg.cell(table, p, PANELS) for p in (P1, P2, P3)]
    assert all(area[i] < area[i + 1] for i in range(2)), f"the area under panels must rise; got {area}"
    assert all(plants[i] > plants[i + 1] for i in range(2)), f"plant species must fall; got {plants}"
    assert all(reptiles[i] > reptiles[i + 1] for i in range(2)), \
        f"reptile species must fall; got {reptiles}"
    return (f"the area under panels runs {area} hectares while plant species run {plants} and "
            f"reptile species {reptiles}, the two counts falling as the area rises")


def q28(table, item):
    plants, _ = _desert(table)
    fall = plants[0] - plants[2]
    assert fall == 19, f"the fall recomputes to {fall}, not 19 species"
    for wrong in (plants[0], plants[0] + plants[2], plants[0] - plants[1], plants[1] - plants[2]):
        assert fall != wrong, f"the {wrong} distractor equals the key"
    return (f"{plants[0]:.0f} minus {plants[2]:.0f} is {fall:.0f} native plant species fewer "
            "where the large farm stands")


def q29(table, item):
    plants, reptiles = _desert(table)
    assert plants[0] > plants[2] and reptiles[0] > reptiles[2], \
        "'the counts rise with the area under panels' must be false"
    assert len(plants) == 3, "the survey must be the three plots the item describes"
    assert cg.cell(table, P2, PANELS) < cg.cell(table, P3, PANELS), \
        "the record must distinguish a small farm from a large one, since the claim is about large"
    return (f"three plots, with plant counts {plants} and reptile counts {reptiles}, are "
            "consistent with the framework's hedged claim but are not a universal one")


CLAIMS = [
 ("transform it directly into electrical energy",
  "ENG-3.J.1, near verbatim: PHOTOVOLTAIC SOLAR CELLS CAPTURE LIGHT ENERGY FROM THE SUN AND TRANSFORM IT DIRECTLY INTO ELECTRICAL ENERGY. Heating a liquid is what an active system does in ENG-3.J.2 and absorbing heat without equipment is a passive system in ENG-3.J.3."),
 ("The availability of sunlight",
  "ENG-3.J.1 states that THEIR USE IS LIMITED BY THE AVAILABILITY OF SUNLIGHT. Water for cooling, equipment and desert land appear nowhere in that clause, and the limit is stated rather than withheld."),
 ("Heat a liquid, through mechanical and electric equipment, so the energy can be collected",
  "ENG-3.J.2, near verbatim: active systems USE SOLAR ENERGY TO HEAT A LIQUID THROUGH MECHANICAL AND ELECTRIC EQUIPMENT TO COLLECT AND STORE THE ENERGY. Doing it without equipment and without collection or storage is the passive system of ENG-3.J.3, so the anchor carries the liquid, the equipment and the storage together."),
 ("absorbs heat directly from the sun without the use of mechanical and electric equipment",
  "ENG-3.J.3, near verbatim. One rejected option is the same sentence with the equipment put back in, so the anchor carries the absence of equipment as well as the absorption."),
 ("Collect or store the energy it absorbs",
  "ENG-3.J.3 ends by stating that ENERGY CANNOT BE COLLECTED OR STORED in a passive system. The same statement says it does absorb heat directly from the sun, so the options denying that it works at all contradict it."),
 ("active system uses mechanical and electric equipment and can collect and store the energy; the passive system uses none",
  "ENG-3.J.2 gives the active system equipment and the ability to collect and store, while ENG-3.J.3 gives the passive system neither. One rejected option is the exact swap, so the anchor carries both halves."),
 ("Passive, because it absorbs heat directly from the sun without mechanical and electric equipment",
  "ENG-3.J.3 describes exactly this arrangement: heat absorbed directly with no mechanical or electric equipment and no collection or storage. One rejected option keeps the ground and attaches it to the active system, so the anchor carries the name and the ground together."),
 ("cells produce electrical energy, while the active system heats a liquid",
  "ENG-3.J.1 has photovoltaic cells transforming light directly into ELECTRICAL ENERGY while ENG-3.J.2 has an active system heating A LIQUID. Each statement names its own output and the two are different, which is why the comparison is made on the outputs rather than on the word direct."),
 ("low environmental impact and produce clean energy",
  "ENG-3.K.1 opens by stating that SOLAR ENERGY SYSTEMS HAVE LOW ENVIRONMENTAL IMPACT AND PRODUCE CLEAN ENERGY. The same statement goes on to name an impact on desert ecosystems, so low impact is not the same as none."),
 ("That they can be expensive",
  "ENG-3.K.1 states that solar energy systems CAN BE EXPENSIVE. Hazardous solid waste and thermal pollution belong to nuclear power in topic 6.6 and volatile organic compounds to fracking in topic 6.5."),
 ("may negatively impact desert ecosystems",
  "ENG-3.K.1 ends by stating that LARGE SOLAR ENERGY FARMS MAY NEGATIVELY IMPACT DESERT ECOSYSTEMS. The claim is hedged with may, it names desert ecosystems rather than wetlands, and it is made rather than withheld."),
 ("possible rather than certain",
  "ENG-3.K.1 says solar systems CAN BE expensive and that large farms MAY negatively impact desert ecosystems, which asserts possibility in both cases. Neither hedge touches the claim that the energy produced is clean, which the same sentence states flatly."),
 ("passive system the energy cannot be collected or stored; it is an active system that collects",
  "ENG-3.J.3 denies collection and storage to a passive system while ENG-3.J.2 gives both to an active one. One rejected correction is the exact swap of the two, which is why both halves have to be stated."),
 ("cells transform light directly into electrical energy; heating a liquid is what an active system does",
  "ENG-3.J.1 has the cells transforming light directly into electrical energy and ENG-3.J.2 gives the heated liquid to an active system. Absorbing heat directly is the passive system, and no statement in this topic gives solar energy a turbine."),
 ("use of photovoltaic cells is limited by the availability of sunlight",
  "ENG-3.J.1 names THE AVAILABILITY OF SUNLIGHT as the limit on photovoltaic cells, which is precisely what a persistently cloudy region lacks. The rejected statements concern cleanliness, deserts and the two kinds of heating system."),
 ("Surveying desert plots with and without a large farm",
  "ENG-3.K.1 restricts the claim to LARGE SOLAR ENERGY FARMS and to DESERT ECOSYSTEMS, so the observation must compare desert land with and without such a farm. Output, storage temperature, cost and ownership each bear on a different statement."),
 ("delivers more where there is more sunlight",
  "Recomputed in q17 above: 3, 5, 8 and 10 hours of sunlight a day against 150, 250, 400 and 500 energy units of output, rising together, with the least and most sunny sites identified by row. ENG-3.J.1 states that the use of photovoltaic cells is LIMITED BY THE AVAILABILITY OF SUNLIGHT."),
 ("50 energy units, the same at every site",
  "Recomputed in q18 above: 150 over 3, 250 over 5, 400 over 8 and 500 over 10 all give the same rate. The rejected values quote a whole day's output, divide the wrong way round, or deny an arithmetic the record plainly allows."),
 ("300 energy units",
  "Recomputed in q19 above: six hours at 50 energy units for each hour. The rejected values quote a neighbouring site's output, double the hours instead of multiplying by the rate, or quote the least sunny site."),
 ("350 energy units",
  "Recomputed in q20 above: 500 minus 150 energy units, with the two extreme sites identified by row rather than by position. The rejected values quote the sunniest site alone, add the two, or take a step between adjacent sites."),
 ("first is active, because it has mechanical and electric equipment and stores heated liquid",
  "Recomputed in q21 above: 6 pieces of equipment and 400 litres held after dark at the first house, none of either at the second, which still delivers 300 energy units of heat. ENG-3.J.2 gives equipment and storage to the active system and ENG-3.J.3 denies both to the passive one. One rejected option is the exact swap, so the anchor carries both."),
 ("passive system absorbs heat directly from the sun but cannot collect or store it",
  "Recomputed in q22 above: the second house delivers heat while holding no liquid and carrying no equipment. ENG-3.J.3 says exactly this. One rejected option keeps the system and inverts the storage clause and another keeps the storage clause and swaps the system, so the anchor carries both."),
 ("200 energy units",
  "Recomputed in q23 above: 500 minus 300 energy units of heat on a sunny day. The rejected values quote one house alone, add the two, or read the litres of stored liquid as though they were energy units."),
 ("clean energy but is the more expensive to build",
  "Recomputed in q24 above: 0 grams of air pollutants for each unit of electricity against 310, and 2,700 currency units to build for each unit of capacity against 900. ENG-3.K.1 states that solar energy systems produce clean energy BUT CAN BE EXPENSIVE, and the anchor carries both halves of that trade-off."),
 ("Three times as much",
  "Recomputed in q25 above: 2,700 divided by 900 currency units for each unit of capacity. The rejected values shift the answer by a power of ten, quote a wrong division, or invert the comparison the record shows."),
 ("solar energy systems produce clean energy",
  "Recomputed in q26 above: 0 grams of air pollutants for each unit of electricity against the gas plant's 310, which is a reading about what is released rather than about cost, deserts, sunlight or storage. ENG-3.K.1 states that solar energy systems PRODUCE CLEAN ENERGY."),
 ("large solar energy farms may negatively impact desert ecosystems",
  "Recomputed in q27 above: native plant species falling 34, 27, 15 and reptile species 11, 8, 4 as the area under panels rises from none to 120 to 900 hectares. ENG-3.K.1 states this claim in exactly those terms."),
 ("By 19 species",
  "Recomputed in q28 above: 34 minus 15 native plant species between the undisturbed plot and the one under the large farm. The rejected values quote the undisturbed plot alone, add the two, or take a step between adjacent plots."),
 ("hedged and is about large farms in desert ecosystems",
  "Recomputed in q29 above: three plots whose counts do fall, which is consistent with the framework without establishing more than it claims. ENG-3.K.1 says large solar energy farms MAY negatively impact DESERT ecosystems, a hedged claim restricted to a size and a habitat."),
 ("passive systems absorb heat directly with no such equipment and cannot collect or store it",
  "The keyed summary carries ENG-3.J.1, J.2, J.3 and K.1 in the framework's own terms, including both hedges. Each rejected summary exchanges the active and passive properties, drops the sunlight limit, denies the desert clause, reverses the environmental verdict, or claims figures the framework never supplies."),
]

TABLE_CHECKS = {17: q17, 18: q18, 19: q19, 20: q20, 21: q21, 22: q22, 23: q23,
                24: q24, 25: q25, 26: q26, 27: q27, 28: q28, 29: q29}


def _selftest():
    """Reversal alone must be caught for every table, with no flatten fallback.

    The sunlight table is the case that needs this: reversing both of its
    columns leaves the (hours, output) pairs untouched, so the trend, the rate
    for each hour, the prediction and the extreme difference all survive. All
    four of its checks pin the least and most sunny sites by row label, and this
    control is what proves the pin does the work.
    """
    import copy
    import types

    def run_on(questions):
        mod = types.ModuleType("e6_8_mutant")
        mod.TOPIC = e6_8.TOPIC
        mod.QUESTIONS = questions
        e_check.style(mod)
        e_check.no_figure_reference(mod)
        cg.check(mod, CLAIMS, table_checks=TABLE_CHECKS)

    def must_fail(label, mutate):
        qs = copy.deepcopy(e6_8.QUESTIONS)
        mutate(qs)
        try:
            run_on(qs)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:88]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def reverse_columns(table):
        t = copy.deepcopy(table)
        for j in range(1, len(t["headers"])):
            vals = [r[j] for r in t["rows"]]
            try:
                [cg.num(v) for v in vals]
            except AssertionError:
                continue
            for r, v in zip(t["rows"], reversed(vals)):
                r[j] = v
        return t

    print("selftest: reversal alone must be caught for every table")
    for i in sorted(TABLE_CHECKS):
        must_fail(f"q{i} table columns reversed (no flatten fallback)",
                  lambda qs, i=i: qs[i - 1].__setitem__(
                      "table", reverse_columns(qs[i - 1]["table"])))

    def edit(qi, row_label, header, value):
        def mutate(qs):
            t = copy.deepcopy(qs[qi - 1]["table"])
            j = [cg.normalize(h) for h in t["headers"]].index(cg.normalize(header))
            for r in t["rows"]:
                if cg.normalize(r[0]) == cg.normalize(row_label):
                    r[j] = value
            qs[qi - 1]["table"] = t
        return mutate

    print("selftest: one cell at a time, against the keyed number")
    must_fail("q17 the trend broken at one site", edit(17, S3, OUTPUT, "100"))
    must_fail("q18 the rate made to differ between sites", edit(18, S2, OUTPUT, "260"))
    must_fail("q19 the rate moved so the prediction changes", edit(19, S1, OUTPUT, "150.5"))
    must_fail("q20 gap moved off 350 energy units", edit(20, S4, OUTPUT, "550"))
    must_fail("q21 the equipped house stripped of its equipment", edit(21, SYS1, KIT, "0"))
    must_fail("q22 the passive house given a storage tank", edit(22, SYS2, LITRES, "250"))
    must_fail("q23 gap moved off 200 energy units", edit(23, SYS2, DELIVERED, "250"))
    must_fail("q24 the array given air pollutants", edit(24, ARRAY, POLLUTE, "120"))
    must_fail("q25 ratio moved off three", edit(25, ARRAY, BUILD, "3,600"))
    must_fail("q26 the array's pollutant figure lifted off zero",
              edit(26, ARRAY, POLLUTE, "40"))
    must_fail("q27 the largest farm given the richest plant count",
              edit(27, P3, PLANTS, "40"))
    must_fail("q28 fall moved off 19 species", edit(28, P3, PLANTS, "20"))
    must_fail("q29 the two farms made the same size", edit(29, P2, PANELS, "900"))

    print("selftest: the unmodified module must still pass (positive control)")
    run_on(copy.deepcopy(e6_8.QUESTIONS))
    print("all selftest controls raised as required, and the clean module passes.")


if __name__ == "__main__":
    import sys
    if "--selftest" in sys.argv:
        _selftest()

e_check.run(e6_8, CLAIMS, TABLE_CHECKS)
