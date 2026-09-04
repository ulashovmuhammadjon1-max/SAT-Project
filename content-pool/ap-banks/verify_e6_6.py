"""Key audit for AP ENVIRONMENTAL SCIENCE 6.6 Nuclear Power.

One (anchor, claim) per item, in module order. The anchor must appear in the
KEYED choice and in no distractor, so an off-by-one key or a reordered choice
list fails here rather than reaching a student.

WHAT THE KEYS REST ON
---------------------
  ENG-3.G.1  fission of Uranium-235 in fuel rods after a neutron strike; the
             heat raises steam, the steam powers a turbine, electricity is
             generated.                  -- items 1, 2, 3, 4, 5, 6, 7
  ENG-3.G.2  radioactivity is the nucleus of a radioactive isotope losing
             energy by emitting radiation.              -- item 8
  ENG-3.G.3  Uranium-235 remains radioactive for a long time, which leads to
             the problems of nuclear waste disposal.    -- items 9, 23
  ENG-3.G.4  nonrenewable; cleaner because no air pollutants; but thermal
             pollution and hazardous solid waste.
                              -- items 10, 11, 12, 13, 17, 18, 25, 26, 27
  ENG-3.H.1  Three Mile Island, Chernobyl and Fukushima; short- and long-term
             impacts.                     -- items 14, 15, 28, 29
  ENG-3.H.2  a half-life can be used to calculate a variety of things,
             including the rate of decay and the radioactivity level at
             specific points in time.     -- items 16, 19, 20, 21, 22, 24
  item 30 reads across all six.

FISSION AND FUSION ARE THE SWAP THIS TOPIC INVITES, and the anchors are written
for it. The framework says FISSION and says the atoms are SPLIT INTO SMALLER
PARTS. Item 1's five options are the four combinations of the two process names
with the two directions, plus combustion, so an anchor naming the process alone
would match a distractor. Every anchor about the mechanism therefore carries the
name and the direction together.

CLEANER AND NONRENEWABLE SIT IN ONE SENTENCE, and dropping either half is the
commonest way to get ENG-3.G.4 wrong. Item 13's anchor carries the
classification and the qualification, and items 25 and 27 carry the fact that
the absence of air pollutants coexists with thermal pollution and hazardous
solid waste.

WHAT IS NOT KEYED. The framework names three accident sites and says the
releases had short- and long-term impacts. It gives no dates, no doses and no
cause for any individual case beyond "accidents or natural disasters", so
nothing here asks for one and the site table is labelled Site 1 to Site 3
rather than with any real place. ENG-3.H.2 says a half-life CAN BE USED to
calculate; the arithmetic items therefore print their own decay record and
compute from it rather than quoting an element's half-life from memory.

DATA ITEMS: 19 to 29, recomputed below from those tables alone.

TWO TABLES SURVIVE A COLUMN REVERSAL on their arithmetic alone. The ratio
between the longest and next-longest half-life is invariant, and so is the fall
at whichever site started highest. Both checks therefore pin their rows BY ROW
LABEL, which a reversal does break.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and every table in turn, and requires each
corruption to raise, BEFORE the real gate runs. It is not behind a flag.
``python3 verify_e6_6.py --selftest`` adds the stronger property that a
REVERSAL ALONE is caught for every table, without e_check's flatten fallback.
"""
import e_check
import cg_check as cg
import e6_6

REMAIN = "Radioactivity remaining (percent of the original)"
TIMES = ["0", "30", "60", "90"]

HALFLIFE = "Half-life (years)"
BYMASS = "Share of the waste by mass (percent)"
IA, IB, IC = "Isotope A", "Isotope B", "Isotope C"

AIR = "Air pollutants released for each unit of electricity (kilograms)"
WASTEHEAT = "Waste heat discharged to the river for each unit of electricity (energy units)"
SOLID = "Hazardous solid waste produced for each unit of electricity (kilograms)"
COALP, NUKE = "Coal plant", "Nuclear plant"

YEAR1 = "Radiation in the soil one year after the release (units)"
YEAR20 = "Radiation in the soil twenty years after the release (units)"
ST1, ST2, ST3 = "Site 1", "Site 2", "Site 3"


def _decay(table):
    """The record's times and levels, checked to be evenly spaced and halving."""
    labs = cg.labels(table)
    assert labs == TIMES, f"the record must run 0, 30, 60 and 90 years; got {labs}"
    times = [float(t) for t in labs]
    levels = [cg.cell(table, t, REMAIN) for t in labs]
    steps = [times[i + 1] - times[i] for i in range(3)]
    assert len(set(steps)) == 1, f"the sampling interval must be constant; got {steps}"
    for i in range(3):
        assert abs(levels[i + 1] - levels[i] / 2) < 1e-9, \
            f"the level must halve over each interval; got {levels}"
    return steps[0], times, levels


def q19(table, item):
    step, _, levels = _decay(table)
    assert step == 30, f"the half-life recomputes to {step}, not 30 years"
    for wrong in (60, 90, 15, 50):
        assert step != wrong, f"the {wrong} distractor equals the key"
    return (f"the level runs {levels} percent of the original at intervals of {step:.0f} years, "
            f"halving over each interval, so the half-life is {step:.0f} years")


def q20(table, item):
    step, times, levels = _decay(table)
    n = (60 - times[0]) / step
    assert n == 2, f"the number of half-lives by year sixty recomputes to {n}, not 2"
    assert abs(cg.cell(table, "60", REMAIN) - levels[0] / 4) < 1e-9, \
        "the level at sixty years must be a quarter of the original, which is two halvings"
    for wrong in (1, 3, 4, 60):
        assert n != wrong, f"the {wrong} distractor equals the key"
    return (f"sixty years at a half-life of {step:.0f} years is {n:.0f} halvings, and the level "
            f"has gone from {levels[0]:.0f} to {cg.cell(table, '60', REMAIN)} percent")


def q21(table, item):
    step, times, levels = _decay(table)
    assert times[-1] + step == 120, \
        "one further interval past the record must reach the year the item asks about"
    predicted = levels[-1] / 2
    assert abs(predicted - 6.25) < 1e-9, f"the level recomputes to {predicted}, not 6.25 percent"
    for wrong in (levels[-1], predicted / 2, 50, 0):
        assert abs(predicted - wrong) > 1e-9, f"the {wrong} distractor equals the key"
    return (f"{levels[-1]} percent at ninety years halves once more over the next {step:.0f} "
            f"years to {predicted} percent at one hundred and twenty")


def q22(table, item):
    step, times, levels = _decay(table)
    assert len(levels) >= 3, "a half-life cannot be read off fewer than three points"
    assert step > 0 and all(levels[i] > levels[i + 1] for i in range(3)), \
        f"the record must fall over time for a decay rate to be read; got {levels}"
    assert levels[0] == 100, "the record must start from the whole sample, so levels are readable"
    return (f"the record pairs the times {times} with the levels {levels} percent, from which the "
            f"half-life of {step:.0f} years and the level at any later time both follow")


def q23(table, item):
    lives = {lab: cg.cell(table, lab, HALFLIFE) for lab in cg.labels(table)}
    assert lives[IC] == max(lives.values()), f"the third isotope must be the longest lived; got {lives}"
    assert lives[IC] > 1000 * lives[IB], \
        "the longest lived isotope must outlast the others by orders of magnitude"
    assert lives[IA] == min(lives.values()), "'the first isotope is the longest lived' must be false"
    assert cg.cell(table, IC, BYMASS) == max(cg.col(table, BYMASS)), \
        "'the third isotope is the smallest share of the waste' must be false"
    return (f"the half-lives run {list(lives.values())} years, so the third isotope stays "
            f"radioactive far longer than the others and is also "
            f"{cg.cell(table, IC, BYMASS):.0f} percent of the waste by mass")


def q24(table, item):
    lives = {lab: cg.cell(table, lab, HALFLIFE) for lab in cg.labels(table)}
    assert lives[IC] == max(lives.values()), "the third isotope must hold the longest half-life"
    ordered = sorted(lives.values(), reverse=True)
    ratio = ordered[0] / ordered[1]
    assert ratio == 10000, f"the ratio recomputes to {ratio}, not 10,000"
    for wrong in (100000, 1000, ordered[1] / ordered[2], 1):
        assert ratio != wrong, f"the {wrong} distractor equals the key"
    return (f"{ordered[0]:.0f} divided by {ordered[1]:.0f} is {ratio:.0f} times as long a "
            "half-life for the longest lived isotope as for the next")


def q25(table, item):
    assert cg.cell(table, NUKE, AIR) == 0, "the nuclear plant must release no air pollutants"
    assert cg.cell(table, COALP, AIR) > 0, "the coal plant must release air pollutants"
    assert cg.cell(table, NUKE, WASTEHEAT) > cg.cell(table, COALP, WASTEHEAT), \
        "the nuclear plant must discharge more waste heat, or thermal pollution goes unshown"
    assert cg.cell(table, NUKE, SOLID) > cg.cell(table, COALP, SOLID), \
        "the nuclear plant must produce more hazardous solid waste"
    return (f"air pollutants are {cg.cell(table, NUKE, AIR)} against "
            f"{cg.cell(table, COALP, AIR)} kilograms, while waste heat is "
            f"{cg.cell(table, NUKE, WASTEHEAT)} against {cg.cell(table, COALP, WASTEHEAT)} and "
            f"hazardous solid waste {cg.cell(table, NUKE, SOLID)} against "
            f"{cg.cell(table, COALP, SOLID)}")


def q26(table, item):
    gap = cg.cell(table, NUKE, WASTEHEAT) - cg.cell(table, COALP, WASTEHEAT)
    assert abs(gap - 0.7) < 1e-9, f"the gap recomputes to {gap}, not 0.7 energy units"
    assert gap > 0, "'the nuclear plant discharges less waste heat' must be false"
    for wrong in (cg.cell(table, NUKE, WASTEHEAT),
                  cg.cell(table, NUKE, WASTEHEAT) + cg.cell(table, COALP, WASTEHEAT),
                  cg.cell(table, COALP, WASTEHEAT)):
        assert abs(gap - wrong) > 1e-9, f"the {wrong} distractor equals the key"
    return (f"{cg.cell(table, NUKE, WASTEHEAT)} minus {cg.cell(table, COALP, WASTEHEAT)} is "
            f"{gap:.1f} energy units more waste heat for each unit of electricity")


def q27(table, item):
    assert cg.cell(table, NUKE, SOLID) > 0, \
        "the record must refute 'no hazardous solid waste' by showing some"
    assert cg.cell(table, NUKE, SOLID) > cg.cell(table, COALP, SOLID), \
        "'it produces less hazardous solid waste than the coal plant' must also be false"
    assert cg.cell(table, NUKE, AIR) == 0, \
        "'it produces no air pollutants' must stand, so only one claim is refuted"
    assert cg.cell(table, NUKE, WASTEHEAT) > 0, \
        "'it discharges waste heat to the river' must stand as well"
    return (f"the nuclear plant produces {cg.cell(table, NUKE, SOLID)} kilograms of hazardous "
            f"solid waste against the coal plant's {cg.cell(table, COALP, SOLID)}, while its air "
            f"pollutant figure stays at {cg.cell(table, NUKE, AIR)}")


def _sites(table):
    early = {lab: cg.cell(table, lab, YEAR1) for lab in cg.labels(table)}
    late = {lab: cg.cell(table, lab, YEAR20) for lab in cg.labels(table)}
    assert early[ST1] == max(early.values()), "the first site must hold the highest early reading"
    return early, late


def q28(table, item):
    early, late = _sites(table)
    assert all(v > 0 for v in early.values()), f"every site must read above zero early; got {early}"
    assert all(v > 0 for v in late.values()), \
        f"every site must still read above zero twenty years later; got {late}"
    for lab in early:
        assert late[lab] < early[lab], f"{lab} must have fallen over the twenty years"
    return (f"the soil reads {list(early.values())} units one year after the releases and still "
            f"{list(late.values())} units twenty years later, so the effect is present at both "
            "timescales")


def q29(table, item):
    early, late = _sites(table)
    top = max(early, key=early.get)
    assert top == ST1, f"the site that started highest is {top}, not {ST1}"
    fall = early[top] - late[top]
    assert fall == 290, f"the fall recomputes to {fall}, not 290 units"
    for wrong in (early[top], early[top] + late[top],
                  early[ST2] - late[ST2], early[ST3] - late[ST3]):
        assert fall != wrong, f"the {wrong} distractor equals the key"
    return (f"{early[top]:.0f} minus {late[top]:.0f} is {fall:.0f} units of decline at the site "
            "that started highest")


CLAIMS = [
 ("Fission, in which atoms are split into smaller parts",
  "ENG-3.G.1, near verbatim: NUCLEAR POWER IS GENERATED THROUGH FISSION, WHERE ATOMS OF URANIUM-235 ARE SPLIT INTO SMALLER PARTS. The framework never mentions fusion. The five options are the two process names crossed with the two directions plus combustion, so the anchor carries the name and the direction together."),
 ("Atoms of Uranium-235",
  "ENG-3.G.1 names ATOMS OF URANIUM-235 as what is split, and ENG-3.G.3 returns to Uranium-235 when it explains why nuclear waste is a problem. No other element is named as the fissile material anywhere in this topic."),
 ("In fuel rods",
  "ENG-3.G.1 states that the atoms of Uranium-235 ARE STORED IN FUEL RODS. The turbine and the generator come later in the framework's sequence and take no part in holding the fuel, and the statement gives no other location."),
 ("Being struck by a neutron",
  "ENG-3.G.1 states that the atoms are split into smaller parts AFTER BEING STRUCK BY A NEUTRON. Heat, light, pressure and chemical attack appear nowhere in the framework's account of what triggers fission."),
 ("A large amount of heat, which is used to generate steam",
  "ENG-3.G.1 states that NUCLEAR FISSION RELEASES A LARGE AMOUNT OF HEAT, WHICH IS USED TO GENERATE STEAM. The electricity comes at the end of the sequence rather than at the start, and light captured by cells is photovoltaic solar energy in topic 6.8."),
 ("It powers a turbine, and that generates electricity",
  "ENG-3.G.1 states that the steam POWERS A TURBINE AND GENERATES ELECTRICITY. One rejected option exchanges the turbine for the generator, which is why the anchor carries the part and its effect together."),
 ("the atom splits and releases heat, the heat generates steam, the steam powers a turbine",
  "ENG-3.G.1 gives the whole sequence: a neutron strikes an atom of Uranium-235 stored in a fuel rod, the atom is split into smaller parts, the fission releases a large amount of heat, that heat generates steam, and the steam powers a turbine and generates electricity. Each rejected sequence joins the atoms, exchanges two steps, or makes the reaction a combustion."),
 ("losing energy by emitting radiation",
  "ENG-3.G.2, near verbatim: RADIOACTIVITY OCCURS WHEN THE NUCLEUS OF A RADIOACTIVE ISOTOPE LOSES ENERGY BY EMITTING RADIATION. Splitting after a neutron strike is fission in a separate statement, and the energy goes out of the nucleus rather than into it."),
 ("problems associated with the disposal of nuclear waste",
  "ENG-3.G.3 states that Uranium-235 REMAINS RADIOACTIVE FOR A LONG TIME, WHICH LEADS TO THE PROBLEMS ASSOCIATED WITH THE DISPOSAL OF NUCLEAR WASTE. The statement draws no conclusion about generation, air pollutants, trade or price."),
 ("As nonrenewable",
  "ENG-3.G.4 opens by stating that NUCLEAR POWER GENERATION IS A NONRENEWABLE ENERGY SOURCE. It attaches no condition to that classification, and it does classify the source, so the options declining to classify it are wrong on their face."),
 ("Because it does not produce air pollutants",
  "ENG-3.G.4 states that nuclear power IS CONSIDERED A CLEANER ENERGY SOURCE BECAUSE IT DOES NOT PRODUCE AIR POLLUTANTS. The same sentence goes on to say that it does release thermal pollution and hazardous solid waste, so the rejected reasons contradict the second half of it."),
 ("Thermal pollution and hazardous solid waste",
  "ENG-3.G.4 states that nuclear power DOES RELEASE THERMAL POLLUTION AND HAZARDOUS SOLID WASTE. Air pollutants are what the same sentence says it does not produce, volatile organic compounds belong to fracking in topic 6.5, and carbon dioxide and water are the products of combustion."),
 ("nonrenewable, and it is considered cleaner only in the sense that it produces no air pollutants",
  "ENG-3.G.4 makes both claims in one statement, and cleaner and renewable are separate properties of which only one is granted. One rejected option keeps the qualification and inverts the classification, so the anchor carries both clauses."),
 ("Three Mile Island, Chernobyl, and Fukushima",
  "ENG-3.H.1 names THREE MILE ISLAND, CHERNOBYL, AND FUKUSHIMA as its three cases of accidents or natural disasters leading to a release of radiation. The other places in the rejected lists are associated with chemical or waste incidents and the framework does not name them here."),
 ("short-term and long-term impacts",
  "ENG-3.H.1 states that THESE RELEASES HAVE HAD SHORT- AND LONG-TERM IMPACTS ON THE ENVIRONMENT. Keeping only one of the two timescales drops half the statement, and the framework does describe the impacts rather than passing over them."),
 ("variety of things, including the rate of decay and the radioactivity level",
  "ENG-3.H.2, near verbatim: a half-life CAN BE USED TO CALCULATE A VARIETY OF THINGS, INCLUDING THE RATE OF DECAY AND THE RADIOACTIVITY LEVEL AT SPECIFIC POINTS IN TIME. The word including leaves the list open rather than closing it at one item."),
 ("nonrenewable energy source, without qualification",
  "ENG-3.G.4 states flatly that nuclear power generation is a nonrenewable energy source and makes no exception for reprocessing. The absence of air pollutants is the framework's ground for calling it cleaner, which is a different property from being renewable."),
 ("no air pollutants, but it does release thermal pollution and hazardous solid waste",
  "ENG-3.G.4 grants the absence of air pollutants and then names two things nuclear power does release. Each rejected correction keeps one part of that sentence and drops another, which is the commonest way to misreport it."),
 ("30 years",
  "Recomputed in q19 above: the level runs 100, 50, 25 and 12.5 percent of the original at intervals of thirty years, halving over each. A half-life is the time for the radioactivity to fall by half, and ENG-3.H.2 makes it the quantity such a record yields."),
 ("Two",
  "Recomputed in q20 above: sixty years at a half-life of thirty is two halvings, and the level has fallen from 100 to 25 percent, a quarter. The rejected values count the wrong number of halvings or quote the elapsed years as though they were half-lives."),
 ("6.25 percent",
  "Recomputed in q21 above: the 12.5 percent standing at ninety years halves once more over the next thirty. ENG-3.H.2 states that a half-life can be used to calculate the radioactivity level at specific points in time, which is exactly this step beyond the record."),
 ("half-life can be used to calculate the rate of decay and the radioactivity level",
  "Recomputed in q22 above: the record pairs four times with four falling levels beginning at the whole sample, from which both the half-life and any later level follow. That is what ENG-3.H.2 says a half-life is used for, while the rejected statements concern classification, mechanism, accidents and emissions."),
 ("third isotope, because its half-life is by far the longest",
  "Recomputed in q23 above: half-lives of 7, 70 and 700,000 years, with the longest-lived isotope also half the waste by mass. ENG-3.G.3 ties the problems of disposal to a material remaining radioactive FOR A LONG TIME. One rejected option keeps the isotope and swaps the ground, so the anchor carries both."),
 ("Ten thousand times as long",
  "Recomputed in q24 above: 700,000 divided by 70 years. The rejected values shift the answer by a power of ten, quote the ratio between the two shorter isotopes, or deny that the half-lives differ."),
 ("no air pollutants, but it does discharge more waste heat and more hazardous solid waste",
  "Recomputed in q25 above: 0.0 kilograms of air pollutants against the coal plant's 9.0, with 2.1 energy units of waste heat against 1.4 and 0.45 kilograms of hazardous solid waste against 0.30. ENG-3.G.4 says exactly this, and the anchor carries both halves because dropping either is how the statement is usually misreported."),
 ("0.7 energy units",
  "Recomputed in q26 above: 2.1 minus 1.4 energy units for each unit of electricity. The rejected values quote one plant alone, add the two, or invert the direction the record shows. ENG-3.G.4 names thermal pollution among what nuclear power does release."),
 ("That it produces no hazardous solid waste",
  "Recomputed in q27 above: 0.45 kilograms for each unit of electricity, more than the coal plant's 0.30, so that claim is false while the air pollutant claim stands at 0.0. ENG-3.G.4 names hazardous solid waste among what nuclear power does release."),
 ("short-term and long-term impacts on the environment",
  "Recomputed in q28 above: 400, 260 and 180 units in the soil a year after the releases and still 110, 70 and 40 units twenty years later. ENG-3.H.1 states that such releases have had short- and long-term impacts on the environment."),
 ("By 290 units",
  "Recomputed in q29 above: 400 minus 110 units at the site that started highest, identified by row rather than by position. The rejected values quote the first reading alone, add the two, or take the fall at one of the other two sites."),
 ("cleaner only for want of air pollutants",
  "The keyed summary carries ENG-3.G.1 through G.4 and ENG-3.H.1 and H.2 in the framework's own terms and adds nothing. Each rejected summary joins the atoms instead of splitting them, calls the source renewable or entirely clean, reverses the direction of the energy in radioactivity, or closes a list the framework leaves open."),
]

TABLE_CHECKS = {19: q19, 20: q20, 21: q21, 22: q22, 23: q23, 24: q24,
                25: q25, 26: q26, 27: q27, 28: q28, 29: q29}


def _selftest():
    """Reversal alone must be caught for every table, with no flatten fallback.

    Two of these checks compute something a column reversal leaves untouched:
    q24's ratio between the longest and next-longest half-life, and q29's fall
    at whichever site started highest. Both pin their rows by label as well,
    and this control is what proves the pin does the work.
    """
    import copy
    import types

    def run_on(questions):
        mod = types.ModuleType("e6_6_mutant")
        mod.TOPIC = e6_6.TOPIC
        mod.QUESTIONS = questions
        e_check.style(mod)
        e_check.no_figure_reference(mod)
        cg.check(mod, CLAIMS, table_checks=TABLE_CHECKS)

    def must_fail(label, mutate):
        qs = copy.deepcopy(e6_6.QUESTIONS)
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
    must_fail("q19 the halving broken at one interval", edit(19, "60", REMAIN, "30"))
    must_fail("q20 the sixty year level moved off a quarter", edit(20, "60", REMAIN, "40"))
    must_fail("q21 the ninety year level moved, so the next halving changes",
              edit(21, "90", REMAIN, "20"))
    must_fail("q22 the record made to rise rather than decay", edit(22, "30", REMAIN, "150"))
    must_fail("q23 the long lived isotope shortened below the others",
              edit(23, IC, HALFLIFE, "7"))
    must_fail("q24 ratio moved off ten thousand", edit(24, IB, HALFLIFE, "7"))
    must_fail("q25 the nuclear plant given air pollutants", edit(25, NUKE, AIR, "4.0"))
    must_fail("q26 waste heat gap moved off 0.7", edit(26, NUKE, WASTEHEAT, "2.0"))
    must_fail("q27 the nuclear plant's solid waste driven to zero",
              edit(27, NUKE, SOLID, "0.0"))
    must_fail("q28 one site made to read nothing after twenty years",
              edit(28, ST2, YEAR20, "0"))
    must_fail("q29 fall moved off 290 units", edit(29, ST1, YEAR20, "100"))

    print("selftest: the unmodified module must still pass (positive control)")
    run_on(copy.deepcopy(e6_6.QUESTIONS))
    print("all selftest controls raised as required, and the clean module passes.")


if __name__ == "__main__":
    import sys
    if "--selftest" in sys.argv:
        _selftest()

e_check.run(e6_6, CLAIMS, TABLE_CHECKS)
