"""Key audit for AP ENVIRONMENTAL SCIENCE 6.7 Energy from Biomass.

One (anchor, claim) per item, in module order. The anchor must appear in the
KEYED choice and in no distractor, so an off-by-one key or a reordered choice
list fails here rather than reaching a student.

WHAT THE KEYS REST ON
---------------------
  ENG-3.I.1  Burning of biomass produces heat for energy at a relatively low
             cost, but it also produces carbon dioxide, carbon monoxide,
             nitrogen oxides, particulates, and volatile organic compounds. The
             overharvesting of trees for fuel also causes deforestation.
                       -- items 1, 2, 3, 4, 9, 10, 11, 13, 15, 19, 20, 21, 22,
                          23, 24, 25, 26
  ENG-3.I.2  Ethanol can be used as a substitute for gasoline. Burning ethanol
             does not introduce additional carbon into the atmosphere via
             combustion, but the energy return on energy investment for ethanol
             is low.   -- items 5, 6, 7, 8, 12, 14, 16, 27, 28, 29
  items 17 and 18 key what the topic does NOT do, and item 30 restates both
  statements.

BOTH STATEMENTS ARE TRADE-OFFS AND THE WORD BUT IS DOING THE WORK. Keeping only
the favourable half is how each is usually misreported, so every scenario item
and both summary items key both halves and their anchors carry both clauses. An
anchor naming the benefit alone would match a distractor that keeps the benefit
and drops or inverts the cost -- items 13, 14, 21 and 30 are written for exactly
that.

THE FIVE SUBSTANCES ARE A CLOSED LIST IN THIS STATEMENT. Sulfur dioxide is not
among them, so item 3 asks which of six is absent from the framework's own list.
That is a question about the sentence, not about what a real furnace emits, and
the claim says so.

THE CARBON CLAIM IS HEDGED TWICE: no ADDITIONAL carbon, and VIA COMBUSTION.
Item 12 keys the correction to a student who drops the hedge, and no key
anywhere states the stronger claim that ethanol is carbon free.

BIOMASS IS NOT CLASSIFIED HERE. The framework labels nuclear power nonrenewable
in ENG-3.G.4 and wind renewable in ENG-3.S.1 and never labels biomass either
way. Item 17 keys that absence; nothing else in the module treats biomass as
classified.

DATA ITEMS: 19 to 29, recomputed below from those tables alone.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and every table in turn, and requires each
corruption to raise, BEFORE the real gate runs. It is not behind a flag.
``python3 verify_e6_7.py --selftest`` adds the stronger property that a
REVERSAL ALONE is caught for every table, without e_check's flatten fallback.
"""
import e_check
import cg_check as cg
import e6_7

GRAMS = "Amount released for each unit of energy (grams)"
CO2 = "Carbon dioxide"
CO = "Carbon monoxide"
NOX = "Nitrogen oxides"
PART = "Particulates"
VOC = "Volatile organic compounds"
FIVE = [CO2, CO, NOX, PART, VOC]

PRICE = "Cost of the fuel for each unit of energy (currency units)"
BIO, GASBOTTLE, GRID = "Biomass gathered locally", "Bottled gas", "Electricity from the grid"

CUT = "Wood cut for fuel each year (thousand tonnes)"
REGROW = "Wood regrowing each year (thousand tonnes)"
FOREST = "Forest area remaining (thousand hectares)"
D1, D2, D3 = "First", "Second", "Third"

DELIVERS = "Energy the fuel delivers (energy units)"
INVESTED = "Energy invested to produce the fuel (energy units)"
ETHANOL, GASOLINE = "Ethanol from a crop", "Gasoline from crude oil"


def _emissions(table):
    labs = cg.labels(table)
    assert labs == FIVE, f"the record must carry the framework's five substances; got {labs}"
    return {lab: cg.cell(table, lab, GRAMS) for lab in FIVE}


def q19(table, item):
    e = _emissions(table)
    assert all(v > 0 for v in e.values()), f"every named substance must be present; got {e}"
    assert e[CO2] == max(e.values()), "carbon dioxide must be the largest by mass in the record"
    assert e[CO2] > 10 * sum(v for k, v in e.items() if k != CO2), \
        "carbon dioxide must dominate the mass, or 'much the largest' is not established"
    assert len(set(e.values())) > 1, "'the five are released in equal amounts' must be false"
    return (f"the record reads {list(e.values())} grams for each unit of energy across the "
            "framework's five substances, all present and carbon dioxide much the largest")


def q20(table, item):
    e = _emissions(table)
    others = sum(v for k, v in e.items() if k != CO2)
    assert abs(others - 7.2) < 1e-9, f"the total recomputes to {others}, not 7.2 grams"
    for wrong in (e[CO2], sum(e.values()), e[CO], others - e[VOC]):
        assert abs(others - wrong) > 1e-9, f"the {wrong} distractor equals the key"
    return (f"{e[CO]} plus {e[NOX]} plus {e[PART]} plus {e[VOC]} is {others:.1f} grams from the "
            "four substances other than carbon dioxide")


def q21(table, item):
    e = _emissions(table)
    smallest = min(e, key=e.get)
    assert smallest == VOC, f"the smallest emission is {smallest}, not {VOC}"
    assert e[NOX] > e[VOC], "'nitrogen oxides are the smallest' must be false"
    assert e[CO] > e[VOC], "'carbon monoxide is the smallest' must be false"
    assert e[CO2] == max(e.values()), "'carbon dioxide is the smallest' must be false"
    return (f"{smallest} come in at {e[VOC]} grams for each unit of energy, the smallest of "
            f"{list(e.values())}, and the framework's list carries no threshold of size")


def q22(table, item):
    p = {lab: cg.cell(table, lab, PRICE) for lab in cg.labels(table)}
    assert p[BIO] == min(p.values()), f"biomass must be the cheapest in the record; got {p}"
    assert p[BIO] < 0.5 * min(p[GASBOTTLE], p[GRID]), \
        "biomass must be cheaper by enough that 'relatively low' is established"
    return (f"the three fuels cost {list(p.values())} currency units for each unit of energy, so "
            "the locally gathered biomass is the cheapest by a wide margin")


def q23(table, item):
    p = {lab: cg.cell(table, lab, PRICE) for lab in cg.labels(table)}
    assert p[BIO] == min(p.values()), "biomass must be the cheapest for the ratio to be keyed"
    ratio = p[GRID] / p[BIO]
    assert ratio == 9, f"the ratio recomputes to {ratio}, not 9"
    for wrong in (p[GASBOTTLE] / p[BIO], p[GRID] - p[GASBOTTLE],
                  p[GRID] + p[GASBOTTLE], 1):
        assert ratio != wrong, f"the {wrong} distractor equals the key"
    return (f"{p[GRID]:.0f} divided by {p[BIO]:.0f} is {ratio:.0f} times as much for a unit of "
            "energy from the grid as from locally gathered biomass")


def _forest(table):
    cut = [cg.cell(table, d, CUT) for d in (D1, D2, D3)]
    regrow = [cg.cell(table, d, REGROW) for d in (D1, D2, D3)]
    area = [cg.cell(table, d, FOREST) for d in (D1, D2, D3)]
    return cut, regrow, area


def q24(table, item):
    cut, regrow, _ = _forest(table)
    over = [i for i in range(3) if cut[i] > regrow[i]]
    assert over == [1, 2], f"the cutting must first pass the regrowth in the second decade; got {over}"
    assert cut[0] < regrow[0], "the first decade must stay within the regrowth"
    assert len(set(regrow)) == 1, "the regrowth must be steady, or the comparison shifts"
    return (f"cutting runs {cut} thousand tonnes a year against a steady {regrow[0]:.0f} "
            "regrowing, so the second decade is the first in which more is taken than grows back")


def q25(table, item):
    cut, regrow, area = _forest(table)
    assert all(area[i] > area[i + 1] for i in range(2)), f"the forest area must fall; got {area}"
    assert all(cut[i] < cut[i + 1] for i in range(2)), f"the cutting must rise; got {cut}"
    assert cut[-1] > regrow[-1], "the record must end in overharvesting for the claim to apply"
    return (f"the forest area falls {area} thousand hectares over the decades in which cutting "
            f"rises {cut} thousand tonnes a year past a steady {regrow[0]:.0f}")


def q26(table, item):
    _, _, area = _forest(table)
    loss = area[0] - area[2]
    assert loss == 380, f"the loss recomputes to {loss}, not 380 thousand hectares"
    for wrong in (area[0] - area[1], area[1] - area[2], area[2], sum(area)):
        assert loss != wrong, f"the {wrong} distractor equals the key"
    return (f"{area[0]:.0f} minus {area[2]:.0f} is {loss:.0f} thousand hectares of forest lost "
            "across the record")


def _returns(table):
    return {lab: cg.cell(table, lab, DELIVERS) / cg.cell(table, lab, INVESTED)
            for lab in cg.labels(table)}


def q27(table, item):
    r = _returns(table)
    assert abs(r[ETHANOL] - 1.5) < 1e-9, f"the ethanol return recomputes to {r[ETHANOL]}, not 1.5"
    for wrong in (cg.cell(table, ETHANOL, DELIVERS),
                  cg.cell(table, ETHANOL, INVESTED),
                  1 / r[ETHANOL],
                  r[GASOLINE]):
        assert abs(r[ETHANOL] - wrong) > 1e-9, f"the {wrong} distractor equals the key"
    return (f"{cg.cell(table, ETHANOL, DELIVERS):.0f} delivered over "
            f"{cg.cell(table, ETHANOL, INVESTED):.0f} invested is a return of {r[ETHANOL]}")


def q28(table, item):
    r = _returns(table)
    ratio = r[GASOLINE] / r[ETHANOL]
    assert ratio == 8, f"the ratio recomputes to {ratio}, not 8"
    assert ratio > 1, "'the gasoline return is smaller' must be false"
    for wrong in (2, r[GASOLINE], 80):
        assert ratio != wrong, f"the {wrong} distractor equals the key"
    return (f"the two returns are {r[ETHANOL]} and {r[GASOLINE]}, so the gasoline return is "
            f"{ratio:.0f} times the ethanol return")


def q29(table, item):
    r = _returns(table)
    assert r[ETHANOL] < r[GASOLINE], \
        f"the ethanol return must be the lower of the two; got {r}"
    assert r[ETHANOL] < 2, "the ethanol return must be small enough for 'low' to be read off it"
    assert r[GASOLINE] > 5 * r[ETHANOL], \
        "the comparison must be wide enough that 'low' is a comparison rather than a label"
    return (f"ethanol returns {r[ETHANOL]} units of energy for each unit invested against "
            f"gasoline's {r[GASOLINE]}, which is the comparison the word low rests on")


CLAIMS = [
 ("Heat for energy at a relatively low cost",
  "ENG-3.I.1, near verbatim: BURNING OF BIOMASS PRODUCES HEAT FOR ENERGY AT A RELATIVELY LOW COST. The word relatively makes it a comparison rather than a claim that the fuel is free, and the statement plainly grants that something useful is produced."),
 ("Carbon dioxide, carbon monoxide, nitrogen oxides, particulates, and volatile organic compounds",
  "ENG-3.I.1 lists exactly those five. Sulfur dioxide, ozone, methane and radon appear nowhere in the list, though some are treated in the atmospheric pollution unit."),
 ("Sulfur dioxide",
  "ENG-3.I.1 names carbon dioxide, carbon monoxide, nitrogen oxides, particulates and volatile organic compounds, and sulfur dioxide is not among them. Every rejected option quotes the statement directly, so the question is about the sentence rather than about what a particular furnace emits."),
 ("Overharvesting of trees for fuel causes deforestation",
  "ENG-3.I.1 ends by stating that THE OVERHARVESTING OF TREES FOR FUEL ALSO CAUSES DEFORESTATION. Groundwater contamination belongs to fracking in topic 6.5, hazardous solid waste to nuclear power in 6.6, and hydrogen sulfide to geothermal energy in 6.10."),
 ("A substitute for gasoline",
  "ENG-3.I.2 opens by stating that ETHANOL CAN BE USED AS A SUBSTITUTE FOR GASOLINE. The statement names no other fuel it replaces and it plainly treats ethanol as something that is burned."),
 ("does not introduce additional carbon into the atmosphere by way of the combustion",
  "ENG-3.I.2 states that BURNING ETHANOL DOES NOT INTRODUCE ADDITIONAL CARBON INTO THE ATMOSPHERE VIA COMBUSTION. The claim is about additional carbon and about the combustion in particular; it does not say carbon is removed and it does not say ethanol is carbon free."),
 ("energy return on energy investment for ethanol is low",
  "ENG-3.I.2 ends by stating exactly that. Sulfur dioxide and transport are not in the statement, and the reservation is made rather than withheld, so the options denying it are wrong on their face."),
 ("energy the fuel delivers against the energy spent producing it",
  "An energy return on energy investment sets energy delivered beside energy invested, which is why ENG-3.I.2 can call it low for ethanol without mentioning money. Price, carbon accounting and land use are separate matters the statement does not raise."),
 ("cheap heat on one side, five named emissions and deforestation on the other",
  "ENG-3.I.1 grants cheap heat and then turns on the word but to five emissions, adding deforestation from overharvesting. Neither half stands alone, and the statement compares biomass with nothing in particular and defines nothing."),
 ("also produces carbon monoxide, nitrogen oxides, particulates and volatile organic compounds",
  "ENG-3.I.1 names five substances and carbon dioxide is only the first of them. Sulfur dioxide is not on the list, and the statement neither replaces carbon dioxide with another product nor denies that it is produced."),
 ("says biomass produces heat at a relatively low cost",
  "ENG-3.I.1 states that burning biomass produces heat for energy AT A RELATIVELY LOW COST. The word relatively keeps it a comparison rather than a claim of free heat, and the statement is about heat rather than electricity."),
 ("burning ethanol introduces no ADDITIONAL carbon by way of the combustion itself",
  "ENG-3.I.2 says burning ethanol DOES NOT INTRODUCE ADDITIONAL CARBON INTO THE ATMOSPHERE VIA COMBUSTION, which is a claim about what the combustion adds rather than a claim that ethanol is carbon free. Reading the hedge away overstates the framework in one direction and reversing it overstates in the other."),
 ("Cheaper heat on one side; five named emissions and the risk of deforestation on the other",
  "ENG-3.I.1 supplies both sides for burning biomass. The low energy return belongs to ethanol in ENG-3.I.2 and habitat loss behind a dam to hydroelectric power in topic 6.9. One rejected option keeps the benefit and attaches the wrong cost, so the anchor carries both sides."),
 ("No additional carbon from the combustion on one side; a low energy return on energy investment",
  "ENG-3.I.2 supplies both sides for ethanol: it substitutes for gasoline and its combustion introduces no additional carbon, but its energy return on energy investment is low. Hydrogen sulfide belongs to geothermal energy, and the cheap heat and deforestation pair belongs to burning biomass, so the anchor carries both sides."),
 ("forest area where wood is being cut for fuel faster than it regrows",
  "ENG-3.I.1 attaches deforestation to the OVERHARVESTING of trees for fuel, so the observation must compare what is taken with what grows back and watch the forest area. Smoke composition, energy return, price and stove counts each bear on a different part of this topic."),
 ("energy the ethanol delivers against the energy invested in producing it",
  "ENG-3.I.2's reservation is that the energy return on energy investment for ethanol is low, which is a ratio of energy out to energy in. Carbon released, price, farmland and particulates each belong to a different claim or a different statement."),
 ("neither; the statements here describe effects rather than assigning a class",
  "ENG-3.I.1 and ENG-3.I.2 describe what burning biomass and ethanol produce and cost, and neither assigns a class. The framework does label nuclear power nonrenewable in ENG-3.G.4 and wind renewable in ENG-3.S.1, which shows it labels a source where it means to."),
 ("about burning biomass bears on the heating choice; the statement about ethanol bears on the transport",
  "ENG-3.I.1 is about burning biomass for heat and the emissions and deforestation that follow, while ENG-3.I.2 makes ethanol a substitute for gasoline, a transport fuel. One rejected option is the pairing exchanged, so the anchor carries both halves."),
 ("All five of the substances the framework names are present, with carbon dioxide much the largest",
  "Recomputed in q19 above: 105 grams of carbon dioxide against 4.2, 0.9, 1.6 and 0.5 grams of the other four for each unit of energy. ENG-3.I.1 names all five, so every one of them appearing is what the statement leads a student to expect."),
 ("7.2 grams",
  "Recomputed in q20 above: 4.2 plus 0.9 plus 1.6 plus 0.5 grams. The rejected values quote carbon dioxide alone, add all five, quote the largest of the four, or drop one of them from the sum."),
 ("Volatile organic compounds, and no, the framework names them whatever the amount",
  "Recomputed in q21 above: 0.5 grams for each unit of energy, the smallest of the five. ENG-3.I.1 lists them alongside the others with no threshold of size, so a list of named products is not a ranking. One rejected option keeps the substance and inverts the verdict, so the anchor carries both."),
 ("produces heat for energy at a relatively low cost",
  "Recomputed in q22 above: 1 currency unit for each unit of energy from locally gathered biomass against 6 for bottled gas and 9 for grid electricity. ENG-3.I.1 states that burning biomass produces heat AT A RELATIVELY LOW COST, and relatively is what a comparison like this establishes."),
 ("Nine times as much",
  "Recomputed in q23 above: 9 divided by 1 currency unit for each unit of energy. The rejected values quote the middle fuel, take the gap between the two dearer fuels, add the prices, or deny that they differ."),
 ("second decade, when 90 thousand tonnes were cut against 55 regrowing",
  "Recomputed in q24 above: cutting of 40, 90 and 150 thousand tonnes a year against a steady 55 regrowing, so the first decade stays within the regrowth and the second is the first that does not. ENG-3.I.1 attaches deforestation to OVERHARVESTING, which is cutting beyond what grows back."),
 ("overharvesting of trees for fuel causes deforestation",
  "Recomputed in q25 above: forest area falling from 900 to 760 to 520 thousand hectares over the same decades in which cutting rises past the steady regrowth. ENG-3.I.1 states this claim and the two columns move exactly as it requires."),
 ("380 thousand hectares",
  "Recomputed in q26 above: 900 minus 520 thousand hectares. The rejected values take one of the two decade-to-decade steps, quote the area remaining, or add the three readings together."),
 ("1.5 units of energy delivered for each unit invested",
  "Recomputed in q27 above: 150 delivered over 100 invested. The rejected values quote one column alone, invert the ratio, or give the figure for the other fuel in the record."),
 ("Eight times as large",
  "Recomputed in q28 above: a return of 12 for gasoline against 1.5 for ethanol. The rejected values quote the gasoline return itself, shift by a power of ten, or invert the comparison the record shows."),
 ("energy return on energy investment for ethanol is low",
  "Recomputed in q29 above: 1.5 units of energy for each unit invested against gasoline's 12. ENG-3.I.2 calls the energy return on energy investment for ethanol low, and a comparison of this width is what the word rests on."),
 ("adds no additional carbon, but its energy return on energy investment is low",
  "The keyed summary carries ENG-3.I.1 and ENG-3.I.2 whole, including the deforestation clause and both halves of each trade-off. Each rejected summary drops the emissions, inverts the cost or the energy return, adds sulfur dioxide to a list that does not carry it, or assigns classes the framework never assigns to either fuel."),
]

TABLE_CHECKS = {19: q19, 20: q20, 21: q21, 22: q22, 23: q23, 24: q24,
                25: q25, 26: q26, 27: q27, 28: q28, 29: q29}


def _selftest():
    """Reversal alone must be caught for every table, with no flatten fallback."""
    import copy
    import types

    def run_on(questions):
        mod = types.ModuleType("e6_7_mutant")
        mod.TOPIC = e6_7.TOPIC
        mod.QUESTIONS = questions
        e_check.style(mod)
        e_check.no_figure_reference(mod)
        cg.check(mod, CLAIMS, table_checks=TABLE_CHECKS)

    def must_fail(label, mutate):
        qs = copy.deepcopy(e6_7.QUESTIONS)
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
    must_fail("q19 one named substance driven to zero", edit(19, NOX, GRAMS, "0"))
    must_fail("q20 sum of the four moved off 7.2 grams", edit(20, PART, GRAMS, "2.0"))
    must_fail("q21 the smallest emission moved to another row", edit(21, NOX, GRAMS, "0.1"))
    must_fail("q22 biomass made the dearest fuel", edit(22, BIO, PRICE, "12"))
    must_fail("q23 ratio moved off nine", edit(23, GRID, PRICE, "8"))
    must_fail("q24 the first decade put into overharvest", edit(24, D1, CUT, "70"))
    must_fail("q25 the forest area made to grow", edit(25, D3, FOREST, "990"))
    must_fail("q26 loss moved off 380 thousand hectares", edit(26, D3, FOREST, "500"))
    must_fail("q27 ethanol return moved off 1.5", edit(27, ETHANOL, DELIVERS, "200"))
    must_fail("q28 ratio moved off eight", edit(28, GASOLINE, DELIVERS, "900"))
    must_fail("q29 ethanol given the larger return", edit(29, ETHANOL, DELIVERS, "3,000"))

    print("selftest: the unmodified module must still pass (positive control)")
    run_on(copy.deepcopy(e6_7.QUESTIONS))
    print("all selftest controls raised as required, and the clean module passes.")


if __name__ == "__main__":
    import sys
    if "--selftest" in sys.argv:
        _selftest()

e_check.run(e6_7, CLAIMS, TABLE_CHECKS)
