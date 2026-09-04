"""Key audit for AP ENVIRONMENTAL SCIENCE 6.9 Hydroelectric Power.

One (anchor, claim) per item, in module order. The anchor must appear in the
KEYED choice and in no distractor, so an off-by-one key or a reordered choice
list fails here rather than reaching a student.

WHAT THE KEYS REST ON
---------------------
  ENG-3.L.1  Hydroelectric power can be generated in several ways. Dams built
             across rivers collect water in reservoirs. The moving water can be
             used to spin a turbine. Turbines can also be placed in small
             rivers, where the flowing water spins the turbine.
                          -- items 1, 2, 3, 4, 11, 13, 17, 18, 19, 20
  ENG-3.L.2  Tidal energy uses the energy produced by tidal flows to turn a
             turbine.     -- items 1, 5, 11, 13, 27, 28, 29
  ENG-3.M.1  Hydroelectric power does not generate air pollution or waste, but
             construction of the power plants can be expensive, and there may
             be a loss of or change in habitats following the construction of
             dams.        -- items 6, 7, 8, 9, 10, 12, 14, 15, 21, 22, 23, 24,
                             25, 26
  item 16 keys what the topic does NOT do, and item 30 restates all three.

THE HABITAT CLAUSE IS DOUBLY QUALIFIED and every key respects both. It is hedged
with MAY; it offers A LOSS OF OR CHANGE IN habitats rather than a loss alone;
and it is attached to THE CONSTRUCTION OF DAMS rather than to hydroelectric
power in general. Item 8 keys the first two qualifications, item 9 the third,
and item 24 keys that a reach can show a loss and a change at once -- which is
what the framework's own OR allows for.

THE DENIAL IS NARROW. ENG-3.M.1 denies air pollution and waste and grants two
costs in the same sentence, so no key reads it as a claim that hydroelectric
power has no effects at all. Items 12, 21 and 30 carry the reservations
alongside the advantage and their anchors carry both clauses.

HYDROELECTRIC POWER IS NOT CLASSIFIED. The framework labels nuclear power
nonrenewable in ENG-3.G.4 and wind renewable in ENG-3.S.1 and never labels
hydroelectricity either way. Item 16 keys that absence; nothing else treats it
as classified.

DATA ITEMS: 17 to 29, recomputed below from those tables alone.

TWO PLACES WOULD SURVIVE A COLUMN REVERSAL on the arithmetic alone. The tidal
table's (flow, output) pairs are unchanged by one, and so is the total output of
whichever two schemes flood nothing. Those checks therefore pin their rows BY
ROW LABEL as well.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and every table in turn, and requires each
corruption to raise, BEFORE the real gate runs. It is not behind a flag.
``python3 verify_e6_9.py --selftest`` adds the stronger property that a
REVERSAL ALONE is caught for every table, without e_check's flatten fallback.
"""
import e_check
import cg_check as cg
import e6_9

DAMHEIGHT = "Height of the dam built (meters)"
FLOODED = "Land flooded to form a reservoir (hectares)"
YEARLY = "Electricity delivered each year (thousand energy units)"
SC1 = "Scheme 1, a barrier across a large river"
SC2 = "Scheme 2, turbines set in a small river"
SC3 = "Scheme 3, turbines driven by tidal flows"

AIR = "Air pollutants released for each unit of electricity (kilograms)"
SOLID = "Solid waste produced for each unit of electricity (kilograms)"
BUILD = "Cost to build for each unit of capacity (currency units)"
HYDRO, COALP = "Hydroelectric plant", "Coal plant"

CHANNEL = "Flowing river-channel habitat in the reach (hectares)"
STILL = "Still-water habitat in the reach (hectares)"
FISH = "Fish species recorded in the reach"
BEFORE = "Before the barrier was built"
AFTER5 = "Five years after it was built"
AFTER20 = "Twenty years after it was built"

FLOW = "Speed of the tidal flow past the turbine (flow units)"
TIDEOUT = "Electricity the turbine delivers (energy units)"
H1, H2, H3, H4 = "Hour 1", "Hour 2", "Hour 3", "Hour 4"


def _pin_schemes(table):
    """The barrier must be the scheme that has one, by ROW LABEL.

    The total output of whichever two schemes flood nothing is unchanged by a
    column reversal, so without this pin q20's arithmetic would say nothing.
    """
    assert cg.cell(table, SC1, DAMHEIGHT) > 0, "the first scheme must carry a barrier"
    assert cg.cell(table, SC1, FLOODED) > 0, "the first scheme must flood land for a reservoir"
    assert cg.cell(table, SC2, DAMHEIGHT) == 0 and cg.cell(table, SC3, DAMHEIGHT) == 0, \
        "the second and third schemes must carry no barrier"


def q17(table, item):
    _pin_schemes(table)
    heights = cg.col(table, DAMHEIGHT)
    assert sum(1 for h in heights if h > 0) == 1, \
        f"exactly one scheme may carry a barrier; got heights {heights}"
    assert cg.cell(table, SC1, FLOODED) == max(cg.col(table, FLOODED)), \
        "the scheme with the barrier must be the one that floods land"
    return (f"only the first scheme carries a barrier, at {cg.cell(table, SC1, DAMHEIGHT):.0f} "
            f"meters, and floods {cg.cell(table, SC1, FLOODED):.0f} hectares, while the other two "
            "carry neither")


def q18(table, item):
    _pin_schemes(table)
    dry = [lab for lab in cg.labels(table) if cg.cell(table, lab, FLOODED) == 0]
    assert dry == [SC2, SC3], f"exactly the second and third schemes must flood nothing; got {dry}"
    for lab in dry:
        assert cg.cell(table, lab, YEARLY) > 0, f"{lab} must still deliver electricity"
    return (f"the flooded areas read {cg.col(table, FLOODED)} hectares, so {dry} flood nothing "
            "and both still deliver electricity")


def q19(table, item):
    _pin_schemes(table)
    gap = cg.cell(table, SC1, YEARLY) - cg.cell(table, SC2, YEARLY)
    assert gap == 860, f"the gap recomputes to {gap}, not 860 thousand energy units"
    for wrong in (cg.cell(table, SC1, YEARLY),
                  cg.cell(table, SC1, YEARLY) + cg.cell(table, SC2, YEARLY),
                  cg.cell(table, SC1, YEARLY) - cg.cell(table, SC3, YEARLY),
                  sum(cg.col(table, YEARLY))):
        assert gap != wrong, f"the {wrong} distractor equals the key"
    return (f"{cg.cell(table, SC1, YEARLY):.0f} minus {cg.cell(table, SC2, YEARLY):.0f} is "
            f"{gap:.0f} thousand energy units more from the scheme with the barrier")


def q20(table, item):
    _pin_schemes(table)
    dry = [lab for lab in cg.labels(table) if cg.cell(table, lab, FLOODED) == 0]
    assert dry == [SC2, SC3], f"the schemes flooding nothing must be the second and third; got {dry}"
    total = sum(cg.cell(table, lab, YEARLY) for lab in dry)
    assert total == 160, f"the total recomputes to {total}, not 160 thousand energy units"
    for wrong in (cg.cell(table, SC1, YEARLY) + cg.cell(table, SC2, YEARLY),
                  sum(cg.col(table, YEARLY)),
                  cg.cell(table, SC3, YEARLY),
                  cg.cell(table, SC1, YEARLY)):
        assert total != wrong, f"the {wrong} distractor equals the key"
    return (f"{cg.cell(table, SC2, YEARLY):.0f} plus {cg.cell(table, SC3, YEARLY):.0f} is "
            f"{total:.0f} thousand energy units from the arrangements that flood no land")


def q21(table, item):
    assert cg.cell(table, HYDRO, AIR) == 0, "the hydroelectric plant must release no air pollutants"
    assert cg.cell(table, HYDRO, SOLID) == 0, "the hydroelectric plant must produce no solid waste"
    assert cg.cell(table, COALP, AIR) > 0 and cg.cell(table, COALP, SOLID) > 0, \
        "the coal plant must release both, or the comparison shows nothing"
    assert cg.cell(table, HYDRO, BUILD) > cg.cell(table, COALP, BUILD), \
        "the hydroelectric plant must be the dearer to build, or the trade-off does not appear"
    return (f"the hydroelectric plant reads {cg.cell(table, HYDRO, AIR):.0f} and "
            f"{cg.cell(table, HYDRO, SOLID):.0f} kilograms against the coal plant's "
            f"{cg.cell(table, COALP, AIR):.0f} and {cg.cell(table, COALP, SOLID)}, while costing "
            f"{cg.cell(table, HYDRO, BUILD):.0f} against {cg.cell(table, COALP, BUILD):.0f} to "
            "build")


def q22(table, item):
    ratio = cg.cell(table, HYDRO, BUILD) / cg.cell(table, COALP, BUILD)
    assert ratio == 3, f"the ratio recomputes to {ratio}, not 3"
    assert ratio > 1, "'it costs less than the coal plant' must be false"
    for wrong in (2, 8, 30):
        assert ratio != wrong, f"the {wrong} distractor equals the key"
    return (f"{cg.cell(table, HYDRO, BUILD):.0f} divided by "
            f"{cg.cell(table, COALP, BUILD):.0f} is {ratio:.0f} times as much to build for each "
            "unit of capacity")


def _reach(table):
    assert cg.cell(table, BEFORE, STILL) == 0, \
        "the reach must hold no still water before the barrier, or the change is not readable"
    channel = [cg.cell(table, s, CHANNEL) for s in (BEFORE, AFTER5, AFTER20)]
    still = [cg.cell(table, s, STILL) for s in (BEFORE, AFTER5, AFTER20)]
    fish = [cg.cell(table, s, FISH) for s in (BEFORE, AFTER5, AFTER20)]
    return channel, still, fish


def q23(table, item):
    channel, still, fish = _reach(table)
    assert all(channel[i] > channel[i + 1] for i in range(2)), \
        f"the flowing channel habitat must fall; got {channel}"
    assert still[1] > still[0] and still[2] > still[0], \
        f"still water must appear where there was none; got {still}"
    assert all(fish[i] > fish[i + 1] for i in range(2)), f"fish species must fall; got {fish}"
    return (f"flowing channel habitat runs {channel} hectares, still water {still}, and fish "
            f"species {fish}, so the reach both loses habitat and changes in kind")


def q24(table, item):
    channel, still, fish = _reach(table)
    lost = channel[0] - channel[2]
    gained = still[2] - still[0]
    assert lost > 0, "some habitat must be lost, or the loss half of the clause fails"
    assert gained > 0, "some habitat of another kind must appear, or the change half fails"
    assert still[0] == 0, "'no new habitat of any kind appeared' must be false only after the dam"
    assert channel[2] > 0, "the flowing channel must not vanish entirely, or 'change' overstates"
    return (f"{lost:.0f} hectares of flowing channel are lost while {gained:.0f} hectares of "
            "still water appear, which is a loss and a change together")


def q25(table, item):
    channel, _, _ = _reach(table)
    lost = channel[0] - channel[2]
    assert lost == 920, f"the loss recomputes to {lost}, not 920 hectares"
    for wrong in (channel[0] - channel[1], channel[0], channel[1], channel[0] + channel[2]):
        assert lost != wrong, f"the {wrong} distractor equals the key"
    return (f"{channel[0]:.0f} minus {channel[2]:.0f} is {lost:.0f} hectares of flowing "
            "river-channel habitat lost across the survey")


def q26(table, item):
    _, _, fish = _reach(table)
    fall = fish[0] - fish[2]
    assert fall == 11, f"the fall recomputes to {fall}, not 11 species"
    for wrong in (fish[0] - fish[1], fish[1] - fish[2], fish[0], sum(fish)):
        assert fall != wrong, f"the {wrong} distractor equals the key"
    return (f"{fish[0]:.0f} minus {fish[2]:.0f} is {fall:.0f} fish species fewer by the end of "
            "the survey")


def _pin_tide(table):
    """The still hour must be the first, by ROW LABEL.

    Reversing this table's two numeric columns leaves the (flow, output) pairs
    exactly as they were, so the proportionality and the zero-output hour both
    survive a reversal. Naming the hours is what breaks under one.
    """
    assert cg.cell(table, H1, FLOW) == 0, "the first hour must record no flow"
    assert cg.cell(table, H4, FLOW) == max(cg.col(table, FLOW)), \
        "the fourth hour must record the fastest flow"


def q27(table, item):
    _pin_tide(table)
    flow = [cg.cell(table, h, FLOW) for h in (H1, H2, H3, H4)]
    out = [cg.cell(table, h, TIDEOUT) for h in (H1, H2, H3, H4)]
    assert all(flow[i] < flow[i + 1] for i in range(3)), f"the flow must rise; got {flow}"
    assert all(out[i] < out[i + 1] for i in range(3)), f"the output must rise with it; got {out}"
    assert out[0] == 0, "the still hour must deliver nothing"
    return (f"the flow runs {flow} flow units against output of {out} energy units, rising "
            "together from a still hour that delivers nothing")


def _tide_rate(table):
    _pin_tide(table)
    rates = [cg.cell(table, h, TIDEOUT) / cg.cell(table, h, FLOW) for h in (H2, H3, H4)]
    assert len(set(rates)) == 1, f"the output for each flow unit must be constant; got {rates}"
    return rates[0]


def q28(table, item):
    rate = _tide_rate(table)
    assert rate == 20, f"the rate recomputes to {rate}, not 20 energy units for each flow unit"
    for wrong in (cg.cell(table, H2, TIDEOUT), rate / 2, rate * 3):
        assert rate != wrong, f"the {wrong} distractor equals the key"
    return (f"output divided by flow speed gives {rate:.0f} energy units for each flow unit at "
            "every hour in which the tide is moving")


def q29(table, item):
    _pin_tide(table)
    assert cg.cell(table, H1, TIDEOUT) == 0, "the still hour must deliver nothing"
    assert all(cg.cell(table, h, TIDEOUT) > 0 for h in (H2, H3, H4)), \
        "every hour with a flow must deliver something, or the flow is not what drives it"
    rate = _tide_rate(table)
    assert rate > 0, "the output must be proportional to the flow for the explanation to hold"
    return (f"the first hour records a flow of {cg.cell(table, H1, FLOW):.0f} and an output of "
            f"{cg.cell(table, H1, TIDEOUT):.0f}, while every moving hour delivers {rate:.0f} "
            "energy units for each flow unit")


CLAIMS = [
 ("Several: a barrier across a river collecting water in a reservoir, turbines placed in",
  "ENG-3.L.1 opens by saying hydroelectric power CAN BE GENERATED IN SEVERAL WAYS and then describes dams collecting water in reservoirs and turbines placed in small rivers, while ENG-3.L.2 adds tidal flows turning a turbine. Solar heating belongs to topic 6.8."),
 ("It collects water in a reservoir",
  "ENG-3.L.1 states that DAMS BUILT ACROSS RIVERS COLLECT WATER IN RESERVOIRS. Nothing in the statement gives the barrier a filtering, storing or heating role, and a turbine is still required to generate the electricity."),
 ("To spin a turbine",
  "ENG-3.L.1 states that THE MOVING WATER CAN BE USED TO SPIN A TURBINE. No steam appears anywhere in this topic, and transforming energy directly into electricity is what photovoltaic cells do in topic 6.8."),
 ("In small rivers, where the flowing water spins the turbine",
  "ENG-3.L.1 states that TURBINES CAN ALSO BE PLACED IN SMALL RIVERS, WHERE THE FLOWING WATER SPINS THE TURBINE. Still water spins nothing, and cooling towers and pipelines appear nowhere in this topic."),
 ("The energy produced by tidal flows, to turn a turbine",
  "ENG-3.L.2, near verbatim: TIDAL ENERGY USES THE ENERGY PRODUCED BY TIDAL FLOWS TO TURN A TURBINE. Heating a liquid for storage is an active solar system in topic 6.8, and salinity and ocean heat appear nowhere in the framework's account."),
 ("Air pollution or waste",
  "ENG-3.M.1 opens by stating that HYDROELECTRIC POWER DOES NOT GENERATE AIR POLLUTION OR WASTE. The same sentence grants an expensive construction and a possible loss of or change in habitats, so the denial covers those two things and no more."),
 ("construction can be expensive, and that there may be a loss of or change in habitats",
  "ENG-3.M.1 names exactly two reservations. Hazardous solid waste belongs to nuclear power in topic 6.6 and volatile organic compounds to fracking in topic 6.5, and the framework does make reservations rather than withholding them."),
 ("possible rather than certain, and that it may be a change in habitat rather than only a loss",
  "ENG-3.M.1 hedges with MAY and offers two outcomes, A LOSS OF OR CHANGE IN habitats. One rejected option keeps the hedge and drops the second outcome, so the anchor carries both qualifications."),
 ("To the construction of dams",
  "ENG-3.M.1 puts the habitat clause FOLLOWING THE CONSTRUCTION OF DAMS. The framework describes turbines in small rivers and tidal turbines elsewhere in this topic and attaches no habitat clause to either."),
 ("generates no air pollution and no waste",
  "ENG-3.M.1 grants that hydroelectric power DOES NOT GENERATE AIR POLLUTION OR WASTE, which is the advantage the framework supplies for a proposal like this. It says construction CAN BE EXPENSIVE rather than cheap, and a turbine is required in every arrangement it describes."),
 ("also be placed in small rivers, and tidal flows can turn a turbine without any barrier",
  "ENG-3.L.1 says hydroelectric power can be generated in SEVERAL WAYS and names turbines placed in small rivers, while ENG-3.L.2 adds tidal flows. Neither collects water behind a barrier, and still water spins nothing."),
 ("Construction can be expensive, and habitats may be lost or changed",
  "ENG-3.M.1 grants that there is no air pollution and no waste and then names two drawbacks. Air pollutants and hazardous solid waste are what other sources in this unit release, and the anchor carries both drawbacks because naming one of them alone leaves the statement half reported."),
 ("Moving water turns a turbine in each of them",
  "ENG-3.L.1 has moving water spinning a turbine behind a barrier and flowing water spinning one in a small river, and ENG-3.L.2 has tidal flows turning a turbine. Only one of the three involves a reservoir, no steam appears anywhere, and the sunlight limit belongs to photovoltaic cells in topic 6.8."),
 ("Surveying the habitats and the species of a river reach before a barrier is built",
  "ENG-3.M.1's reservation is a possible LOSS OF OR CHANGE IN HABITATS following the construction of dams, so the observation must compare the same reach before and after. Air pollutants, price, turbine counts and flow speed each bear on a different part of this topic."),
 ("Measuring the air pollutants and the waste leaving the plant",
  "ENG-3.M.1's advantage is that hydroelectric power DOES NOT GENERATE AIR POLLUTION OR WASTE, so measuring both is what tests it. Flooded area and fish counts bear on the habitat reservation and the remaining options on neither claim."),
 ("neither; these statements describe how it works and what it does",
  "ENG-3.L.1, ENG-3.L.2 and ENG-3.M.1 describe arrangements and effects and assign no class. The framework does label nuclear power nonrenewable in ENG-3.G.4 and wind renewable in ENG-3.S.1, which shows that it labels a source where it means to."),
 ("first, which required a 60 meter barrier and flooded 4,000 hectares",
  "Recomputed in q17 above: only one scheme carries a barrier height and a flooded area. ENG-3.L.1 states that DAMS BUILT ACROSS RIVERS COLLECT WATER IN RESERVOIRS, which is the arrangement that scheme has."),
 ("second and third, and yes, the framework describes turbines in small rivers",
  "Recomputed in q18 above: the second and third schemes flood nothing and both still deliver electricity. ENG-3.L.1 names turbines placed in small rivers and ENG-3.L.2 names tidal flows turning a turbine, so both arrangements are the framework's own. One rejected option identifies the same pair and denies that the framework recognises them, so the anchor carries both clauses."),
 ("860 thousand energy units",
  "Recomputed in q19 above: 900 minus 40 thousand energy units a year. The rejected values quote the barrier scheme alone, add that pair, take the gap to the tidal scheme instead, or add all three schemes together."),
 ("160 thousand energy units",
  "Recomputed in q20 above: 40 plus 120 thousand energy units from the two schemes whose flooded area is zero, identified by row. The rejected values add the wrong pair, add all three, or quote one scheme alone."),
 ("hydroelectric plant releases no air pollutants and no solid waste, but costs more to build",
  "Recomputed in q21 above: 0 and 0 kilograms for each unit of electricity against the coal plant's 9 and 0.8, with a build cost of 2,400 currency units against 800. ENG-3.M.1 states that hydroelectric power does not generate air pollution or waste BUT that construction can be expensive, and the anchor carries both halves."),
 ("Three times as much",
  "Recomputed in q22 above: 2,400 divided by 800 currency units for each unit of capacity. The rejected values shift the answer by a power of ten, quote a wrong division, or invert the comparison the record shows."),
 ("may be a loss of or change in habitats following the construction of a barrier",
  "Recomputed in q23 above: flowing channel habitat falling 1,200, 300 and 280 hectares while still water rises from none to 4,000, and fish species falling 26, 17 and 15. ENG-3.M.1 names a possible loss of or change in habitats following the construction of dams."),
 ("Some habitat was lost and the kind of habitat present also changed",
  "Recomputed in q24 above: more than nine hundred hectares of flowing channel lost while 4,000 hectares of still water appear where there was none. ENG-3.M.1 speaks of A LOSS OF OR CHANGE IN HABITATS, and this reach shows both at once."),
 ("920 hectares",
  "Recomputed in q25 above: 1,200 minus 280 hectares of flowing river-channel habitat. The rejected values take the fall to the middle reading, quote the opening area, quote the middle reading itself, or add the first and last readings."),
 ("By 11 species",
  "Recomputed in q26 above: 26 minus 15 fish species across the survey. The rejected values take one of the two steps within the record, quote the opening count, or add the three readings together."),
 ("tidal energy uses the energy produced by tidal flows to turn a turbine",
  "Recomputed in q27 above: nothing delivered while the flow is still, then 40, 80 and 120 energy units as the flow reaches 2, 4 and 6 flow units. ENG-3.L.2 states this claim in exactly those terms."),
 ("20 energy units",
  "Recomputed in q28 above: 40 over 2, 80 over 4 and 120 over 6 all give the same rate. The rejected values quote one hour's output, halve the rate, treble it, or deny an arithmetic the record plainly allows."),
 ("tidal flow past it has stopped, and the framework makes the flow what turns the turbine",
  "Recomputed in q29 above: a flow of zero and an output of zero in the first hour, with every moving hour delivering in proportion to the flow. ENG-3.L.2 makes the energy produced by tidal flows what turns the turbine, so no flow means no output."),
 ("generates no air pollution and no waste, but construction can be expensive",
  "The keyed summary carries ENG-3.L.1, ENG-3.L.2 and ENG-3.M.1 in the framework's own terms, including both reservations and the hedge on the habitat clause. Each rejected summary reduces the arrangements to one, reverses the emissions or the cost, denies the habitat clause, invents steam, or assigns a class the framework never assigns."),
]

TABLE_CHECKS = {17: q17, 18: q18, 19: q19, 20: q20, 21: q21, 22: q22, 23: q23,
                24: q24, 25: q25, 26: q26, 27: q27, 28: q28, 29: q29}


def _selftest():
    """Reversal alone must be caught for every table, with no flatten fallback."""
    import copy
    import types

    def run_on(questions):
        mod = types.ModuleType("e6_9_mutant")
        mod.TOPIC = e6_9.TOPIC
        mod.QUESTIONS = questions
        e_check.style(mod)
        e_check.no_figure_reference(mod)
        cg.check(mod, CLAIMS, table_checks=TABLE_CHECKS)

    def must_fail(label, mutate):
        qs = copy.deepcopy(e6_9.QUESTIONS)
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

    # The positive control runs FIRST here, not last. It was written last, and
    # while it was last a real defect hid behind it: q21's anchor also matched a
    # distractor, so EVERY control after q21 raised on that anchor rather than
    # on its own mutation and reported "control OK" while proving nothing. A
    # control that fires for the wrong reason is the same failure as one that
    # cannot fire. Establishing the clean pass before any mutation makes that
    # impossible.
    print("selftest: the unmodified module must pass before any mutation is tried")
    run_on(copy.deepcopy(e6_9.QUESTIONS))

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
    must_fail("q17 a second scheme given a barrier", edit(17, SC2, DAMHEIGHT, "20"))
    must_fail("q18 one of the two flood-free schemes given a reservoir",
              edit(18, SC3, FLOODED, "500"))
    must_fail("q19 gap moved off 860", edit(19, SC2, YEARLY, "100"))
    must_fail("q20 total moved off 160", edit(20, SC3, YEARLY, "200"))
    must_fail("q21 the hydroelectric plant given solid waste", edit(21, HYDRO, SOLID, "0.4"))
    must_fail("q22 ratio moved off three", edit(22, HYDRO, BUILD, "3,200"))
    must_fail("q23 the fish count made to recover", edit(23, AFTER20, FISH, "30"))
    must_fail("q24 the still water removed, so no change of kind occurs",
              edit(24, AFTER20, STILL, "0"))
    must_fail("q25 loss moved off 920 hectares", edit(25, AFTER20, CHANNEL, "300"))
    must_fail("q26 fall moved off 11 species", edit(26, AFTER20, FISH, "16"))
    must_fail("q27 the still hour given an output", edit(27, H1, TIDEOUT, "30"))
    must_fail("q28 the rate made to differ between hours", edit(28, H3, TIDEOUT, "90"))
    must_fail("q29 a moving hour left with no output", edit(29, H2, TIDEOUT, "0"))

    print("selftest: the unmodified module must still pass (positive control)")
    run_on(copy.deepcopy(e6_9.QUESTIONS))
    print("all selftest controls raised as required, and the clean module passes.")


if __name__ == "__main__":
    import sys
    if "--selftest" in sys.argv:
        _selftest()

e_check.run(e6_9, CLAIMS, TABLE_CHECKS)
