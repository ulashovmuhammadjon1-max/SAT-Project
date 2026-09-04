"""Key audit for AP ENVIRONMENTAL SCIENCE 6.4 Distribution of Natural Energy Resources.

One (anchor, claim) per item, in module order. The anchor must appear in the
KEYED choice and in no distractor, so an off-by-one key or a reordered choice
list fails here rather than reaching a student.

WHAT THE KEYS REST ON
---------------------
  ENG-3.D.1  The global distribution of natural energy resources, such as ores,
             coal, crude oil, and gas, is not uniform and depends on regions'
             geologic history.

That is the whole topic: ONE sentence, and every key here comes out of one of
its four parts.

  the subject is the GLOBAL DISTRIBUTION       -- items 1, 8, 13, 17, 19
  the examples are ORES, COAL, CRUDE OIL, GAS,
      offered with SUCH AS                     -- items 3, 4, 5
  the distribution IS NOT UNIFORM              -- items 1, 6, 9, 10, 14, 19,
                                                  20, 21, 22, 23, 27
  it DEPENDS ON REGIONS' GEOLOGIC HISTORY      -- items 2, 11, 12, 15, 24, 25,
                                                  26
  items 7, 16, 18 set it against ENG-3.B.1 and ENG-3.B.5 in topic 6.2, which
  are named in their claims.
  items 28, 29 apply the uneven endowment to what a country can supply itself.
  item 30 restates the whole statement.

THE LIST IS OPEN, and one item keys that. ENG-3.D.1 writes SUCH AS, so ores,
coal, crude oil and gas are examples rather than the category. No key here rules
any resource out of the category; item 4 asks only which of five is not among
the four the statement NAMES, which is a question about the sentence.

WHAT IS DELIBERATELY NOT KEYED. The framework attributes occurrence to geologic
history and stops. It names no mechanism by which particular rocks come to hold
particular fuels, so no key asserts one. Item 24's table pairs a rock type with
an occurrence and the keyed conclusion is only that occurrence tracks the
region's geology rather than its area -- which is ENG-3.D.1's own claim and no
more.

DATA ITEMS: 19 to 29, recomputed below from those tables alone.

THREE CHECKS WOULD SURVIVE A COLUMN REVERSAL on their arithmetic alone, and are
written for it. A leader's share of a total, a ratio between the top two values,
and a sum over the rows that hold nothing are all invariant when a column is
reversed. Those checks therefore also pin the leading and the empty rows BY ROW
LABEL, which a reversal does break.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and every table in turn, and requires each
corruption to raise, BEFORE the real gate runs. It is not behind a flag.
``python3 verify_e6_4.py --selftest`` adds the stronger property that a
REVERSAL ALONE is caught for every table, without e_check's flatten fallback.
"""
import e_check
import cg_check as cg
import e6_4

COALCOL = "Recoverable coal (billion energy units)"
OILCOL = "Recoverable crude oil (billion energy units)"
GASCOL = "Recoverable natural gas (billion energy units)"
R1, R2, R3, R4 = "Region 1", "Region 2", "Region 3", "Region 4"

ROCK = "Rock underlying most of the region"
AREA = "Area of the region (thousand square kilometers)"
RA, RB, RC, RD = "Region A", "Region B", "Region C", "Region D"
MARINE = "Ancient marine sedimentary rock"
VOLCANIC = "Recent volcanic rock"

MADE = "Natural gas produced at home in a year (billion energy units)"
USED = "Natural gas used in a year (billion energy units)"
C1, C2, C3 = "Country 1", "Country 2", "Country 3"


def _pin_region(table):
    """The endowments must sit on the rows they are keyed to.

    A leader's share of the column total, and the ratio between the two largest
    values in a column, are both unchanged when that column is reversed. Naming
    the leading row is what a reversal breaks.
    """
    assert cg.cell(table, R1, COALCOL) == max(cg.col(table, COALCOL)), \
        "the first region must hold the most coal"
    assert cg.cell(table, R2, OILCOL) == max(cg.col(table, OILCOL)), \
        "the second region must hold the most crude oil"


def q19(table, item):
    _pin_region(table)
    coal, oil, gas = cg.col(table, COALCOL), cg.col(table, OILCOL), cg.col(table, GASCOL)
    coal_leader = cg.ranked(table, COALCOL)[0]
    oil_leader = cg.ranked(table, OILCOL)[0]
    gas_leader = cg.ranked(table, GASCOL)[0]
    assert coal_leader != oil_leader, \
        "the region richest in coal must not also be the region richest in crude oil"
    assert len(set(coal)) == len(coal), "'the regions hold equal amounts of coal' must be false"
    assert max(gas) > 0, "'no region holds any appreciable natural gas' must be false"
    assert not (coal_leader == oil_leader == gas_leader), \
        "'one region holds the most of all three' must be false"
    return (f"coal runs {coal}, crude oil runs {oil} and natural gas runs {gas} billion energy "
            f"units, so {coal_leader} leads on coal while {oil_leader} leads on crude oil")


def q20(table, item):
    _pin_region(table)
    coal = cg.col(table, COALCOL)
    share = max(coal) / sum(coal)
    assert abs(share - 0.90) < 1e-9, f"the share recomputes to {share}, not 90 percent"
    for wrong in (0.50, 0.30, 0.09, 0.25):
        assert abs(share - wrong) > 1e-9, f"the {wrong} distractor equals the key"
    return (f"{max(coal):.0f} of the {sum(coal):.0f} billion energy units of coal is "
            f"{share * 100:.0f} percent, held by one of the four regions")


def q21(table, item):
    _pin_region(table)
    coal = sorted(cg.col(table, COALCOL), reverse=True)
    ratio = coal[0] / coal[1]
    assert ratio == 15, f"the ratio recomputes to {ratio}, not 15"
    for wrong in (30, 90, 3, 1):
        assert ratio != wrong, f"the {wrong} distractor equals the key"
    return (f"{coal[0]:.0f} divided by {coal[1]:.0f} is {ratio:.0f} times as much coal in the "
            "richest region as in the next")


def q22(table, item):
    _pin_region(table)
    oil_leader = cg.ranked(table, OILCOL)[0]
    assert oil_leader == R2, f"the crude oil leader is {oil_leader}, not {R2}"
    assert cg.cell(table, R2, COALCOL) < 0.1 * cg.cell(table, R1, COALCOL), \
        "the crude oil leader must hold only a small fraction of the coal leader's coal"
    for lab in cg.labels(table):
        if lab != R2:
            assert cg.cell(table, lab, OILCOL) < cg.cell(table, R2, OILCOL), \
                f"{lab} must not tie or beat the crude oil leader"
    return (f"{oil_leader} holds {cg.cell(table, R2, OILCOL):.0f} billion energy units of crude "
            f"oil, the largest of the four, against {cg.cell(table, R2, COALCOL):.0f} of coal")


def q23(table, item):
    empty = [lab for lab in cg.labels(table) if cg.cell(table, lab, GASCOL) == 0]
    assert empty == [R4], f"exactly the fourth region must hold no natural gas; got {empty}"
    assert max(cg.col(table, GASCOL)) > 0, \
        "'every region holds some natural gas' must be false in one direction only"
    return (f"the natural gas column reads {cg.col(table, GASCOL)} billion energy units, so "
            f"{empty[0]} alone holds none")


def _rocks(table):
    return {r[0]: r[1] for r in table["rows"]}


def q24(table, item):
    rocks = _rocks(table)
    marine = [lab for lab, rock in rocks.items() if cg.normalize(rock) == cg.normalize(MARINE)]
    volcanic = [lab for lab, rock in rocks.items() if cg.normalize(rock) == cg.normalize(VOLCANIC)]
    assert marine == [RA, RB] and volcanic == [RC, RD], \
        f"the record must pair two regions with each rock; got {marine} and {volcanic}"
    for lab in marine:
        assert cg.cell(table, lab, OILCOL) > 0, f"{lab} must hold crude oil"
    for lab in volcanic:
        assert cg.cell(table, lab, OILCOL) == 0, f"{lab} must hold no crude oil"
    biggest = cg.ranked(table, AREA)[0]
    assert cg.cell(table, biggest, OILCOL) == 0, \
        "the largest region by area must hold no crude oil, or area would track the endowment"
    return (f"the two regions of {MARINE.lower()} hold "
            f"{[cg.cell(table, lab, OILCOL) for lab in marine]} billion energy units while the "
            f"two of {VOLCANIC.lower()} hold none, and the largest region by area is {biggest}")


def q25(table, item):
    rocks = _rocks(table)
    marine = [lab for lab, rock in rocks.items() if cg.normalize(rock) == cg.normalize(MARINE)]
    total = sum(cg.cell(table, lab, OILCOL) for lab in marine)
    assert total == 1050, f"the total recomputes to {total}, not 1,050 billion energy units"
    parts = [cg.cell(table, lab, OILCOL) for lab in marine]
    for wrong in parts + [abs(parts[0] - parts[1]), 0]:
        assert total != wrong, f"the {wrong} distractor equals the key"
    return (f"{parts[0]:.0f} plus {parts[1]:.0f} is {total:.0f} billion energy units of crude oil "
            f"under the {MARINE.lower()}")


def q26(table, item):
    rocks = _rocks(table)
    dry = [lab for lab in cg.labels(table) if cg.cell(table, lab, OILCOL) == 0]
    assert dry == [RC, RD], f"exactly the two volcanic regions must hold no crude oil; got {dry}"
    for lab in dry:
        assert cg.normalize(rocks[lab]) == cg.normalize(VOLCANIC), \
            f"{lab} holds no crude oil but is not one of the volcanic regions"
    total = sum(cg.cell(table, lab, AREA) for lab in dry)
    assert total == 900, f"the area recomputes to {total}, not 900 thousand square kilometers"
    wet = [lab for lab in cg.labels(table) if lab not in dry]
    for wrong in [sum(cg.cell(table, lab, AREA) for lab in wet)] + \
                 [cg.cell(table, lab, AREA) for lab in dry] + [0]:
        assert total != wrong, f"the {wrong} distractor equals the key"
    return (f"the regions holding no crude oil cover "
            f"{[cg.cell(table, lab, AREA) for lab in dry]} thousand square kilometers, "
            f"{total:.0f} between them")


def q27(table, item):
    made = {lab: cg.cell(table, lab, MADE) for lab in cg.labels(table)}
    used = {lab: cg.cell(table, lab, USED) for lab in cg.labels(table)}
    zero = [lab for lab, v in made.items() if v == 0]
    assert zero == [C2], f"exactly the second country must produce none; got {zero}"
    assert used[C2] > 0, "the second country must still use gas, or it would need none"
    assert made[C1] > used[C1], \
        "the first country must produce more than it uses, so 'every country falls short' is false"
    assert 0 < made[C3] < used[C3], \
        "the third country must produce some of what it uses but not all of it"
    return (f"production runs {list(made.values())} against consumption of {list(used.values())} "
            f"billion energy units, so {zero[0]} alone must take all of its gas from outside")


def q28(table, item):
    gap = cg.cell(table, C3, USED) - cg.cell(table, C3, MADE)
    assert gap == 160, f"the shortfall recomputes to {gap}, not 160 billion energy units"
    assert gap > 0, "'it produces more than it uses' must be false for this country"
    for wrong in (cg.cell(table, C3, USED),
                  cg.cell(table, C3, USED) + cg.cell(table, C3, MADE),
                  cg.cell(table, C2, USED)):
        assert gap != wrong, f"the {wrong} distractor equals the key"
    return (f"{cg.cell(table, C3, USED):.0f} minus {cg.cell(table, C3, MADE):.0f} is {gap:.0f} "
            "billion energy units more used than produced")


def q29(table, item):
    surpluses = {lab: cg.cell(table, lab, MADE) - cg.cell(table, lab, USED)
                 for lab in cg.labels(table)}
    positive = [lab for lab, v in surpluses.items() if v > 0]
    assert positive == [C1], f"exactly the first country must run a surplus; got {positive}"
    assert surpluses[C1] == 180, \
        f"the surplus recomputes to {surpluses[C1]}, not 180 billion energy units"
    for wrong in (cg.cell(table, C1, MADE) + cg.cell(table, C1, USED),
                  -surpluses[C3]):
        assert surpluses[C1] != wrong, f"the {wrong} distractor equals the key"
    return (f"{cg.cell(table, C1, MADE):.0f} minus {cg.cell(table, C1, USED):.0f} is "
            f"{surpluses[C1]:.0f} billion energy units of surplus, and no other country has one")


CLAIMS = [
 ("That it is not uniform",
  "ENG-3.D.1, near verbatim: the global distribution of natural energy resources IS NOT UNIFORM. The rejected options reverse the claim, restrict it to a scale the statement does not use, or deny that the framework speaks to the question."),
 ("The geologic history of the regions",
  "ENG-3.D.1 states that the distribution DEPENDS ON REGIONS' GEOLOGIC HISTORY. Population, consumption, wealth and government policy are each treated elsewhere in this unit and none of them appears in this statement."),
 ("Ores, coal, crude oil, and gas",
  "ENG-3.D.1 names ORES, COAL, CRUDE OIL, AND GAS as its examples. The rejected lists are drawn from other topics of this unit, which treat sunlight, wind, flowing water, biomass and hydrogen in statements of their own."),
 ("Flowing water in rivers",
  "ENG-3.D.1's four named examples are ores, coal, crude oil and gas. Flowing water belongs to the framework's statements about hydroelectric power in topic 6.9, and every rejected option quotes this statement directly."),
 ("examples of natural energy resources rather than a complete list",
  "The words SUCH AS mark a list as illustrative, so ENG-3.D.1 offers its four resources as examples and leaves the category open. The statement sets no order among them and does not claim that they occur together."),
 ("Some regions hold far more of a given resource than other regions do",
  "ENG-3.D.1 denies uniformity, which is a claim that the amounts differ from region to region. It does not say the amounts are equal, that they are everywhere negligible, that a resource sits in one region only, or that an endowment changes by year."),
 ("where natural energy resources occur; the other is about how energy use is spread",
  "ENG-3.D.1 is about occurrence and rests on geologic history; ENG-3.B.1 in topic 6.2 is about the distribution of energy USE between developed and developing countries. One rejected option is the pairing with the second half exchanged, so the anchor carries both clauses."),
 ("Where the world's natural energy resources are found",
  "ENG-3.D.1 sits under the learning objective identify where natural energy resources occur, so it answers a question about location. Consumption is ENG-3.B, cleanliness of a fuel is ENG-3.C.4, and whether a source is renewable is ENG-3.A in topic 6.1."),
 ("coal is not uniformly distributed, and nothing about the region's other resources",
  "ENG-3.D.1 asserts an uneven distribution depending on geologic history and says nothing about any one region's full endowment, its trade, or how its history compares with a neighbour's. A single absence is an instance of the unevenness and no more."),
 ("not uniform and depends on geologic history",
  "Two adjoining areas differing sharply in what they hold is the unevenness ENG-3.D.1 describes, and the statement attributes such differences to the regions' geologic history. The rejected options quote statements about energy use rather than about occurrence."),
 ("because the framework makes occurrence depend on the geologic history of regions",
  "ENG-3.D.1 states that the distribution DEPENDS ON REGIONS' GEOLOGIC HISTORY, which is an account in terms of how the rocks of a place came to be. Consumption, climate and wealth are not part of the statement, and the framework does give an account rather than withholding one."),
 ("because its people consume a great deal of energy",
  "ENG-3.D.1 makes occurrence depend on geologic history, so explaining an endowment by the level of consumption reverses cause and effect and imports a statement about use into a statement about occurrence. Every rejected option restates the framework's own account."),
 ("recoverable amount of one resource measured in each of several regions",
  "ENG-3.D.1 is a claim about how much of a resource occurs in one place against another, so measuring the endowment region by region is what tests it. Consumption for each person, price, fuel mix and years of regulation belong to other statements in this unit."),
 ("the global distribution is NOT uniform",
  "ENG-3.D.1 denies uniformity in so many words, so the student's sentence has to be reversed rather than qualified. The rejected corrections accept the sentence, narrow the claim to a scale the statement does not use, or deny that the framework addresses it."),
 ("makes occurrence depend on the geologic history of the region",
  "ENG-3.D.1 attributes the pattern to REGIONS' GEOLOGIC HISTORY. Consumption is the subject of ENG-3.B in topic 6.2 and is a consequence of what people do rather than a cause of what lies underground."),
 ("availability, price and governmental regulations influence which energy sources people use",
  "ENG-3.B.5 names availability among the three influences on which energy sources people use, and what a region holds is what is available there. The rejected statements classify or describe particular sources without bearing on the choice between them."),
 ("ores, coal, crude oil and gas among them, is not uniform and depends on the geologic history",
  "The keyed sentence carries all four parts of ENG-3.D.1: the subject, the four examples offered as examples, the denial of uniformity and the dependence on geologic history. Each rejected version swaps the explanation, reverses the uniformity claim, closes the open list, or denies that the claim can be made."),
 ("may hold a great deal of a resource and use little energy",
  "ENG-3.D.1 and ENG-3.B.1 are separate statements with separate subjects, so nothing in the framework ties a region's endowment to its consumption. Geologic history is offered as the explanation of occurrence only, and the framework does address consumption at length elsewhere in this unit."),
 ("unevenly distributed, and the region richest in one is not the region richest in another",
  "Recomputed in q19 above: coal 900, 30, 60 and 10, crude oil 40, 720, 10 and 30, natural gas 60, 500, 40 and 0 billion energy units, with the coal leader and the crude oil leader in different rows. ENG-3.D.1 states that the distribution of such resources is not uniform."),
 ("90 percent",
  "Recomputed in q20 above: 900 of the 1,000 billion energy units of coal in the record. The rejected values assume an even split between two or four regions, drop a power of ten, or take a quarter."),
 ("Fifteen times as much",
  "Recomputed in q21 above: 900 divided by 60 billion energy units, the two largest coal endowments. The rejected values divide by the wrong row, drop a power of ten, or deny that the amounts differ."),
 ("second region, with 720 billion energy units of crude oil against 30 of coal",
  "Recomputed in q22 above: the largest crude oil endowment of the four sits in the region holding a small fraction of the coal leader's coal. That a region can lead in one resource and trail in another is what ENG-3.D.1's denial of uniformity amounts to."),
 ("The fourth region",
  "Recomputed in q23 above: the natural gas column reads 60, 500, 40 and 0 billion energy units, so exactly one region holds none. An endowment of nothing beside a neighbour's 500 is the sharpest form of the unevenness ENG-3.D.1 describes."),
 ("occurs in the regions with one kind of rock and not in the others, while the area",
  "Recomputed in q24 above: 600 and 450 billion energy units of crude oil under the ancient marine sedimentary rock, none under the recent volcanic rock, and the largest region by area holding none. ENG-3.D.1 makes occurrence depend on the geologic history of regions rather than on their size."),
 ("1,050 billion energy units",
  "Recomputed in q25 above: 600 plus 450 billion energy units. The rejected values quote one region alone, take the difference between the two, or deny an occurrence the record plainly shows."),
 ("900 thousand square kilometers",
  "Recomputed in q26 above: the two regions holding no crude oil cover 600 and 300 thousand square kilometers, and both are the volcanic ones. The rejected values quote one of those regions alone or add the two that do hold crude oil."),
 ("second country, which produces none and uses 180 billion energy units",
  "Recomputed in q27 above: production of 300, 0 and 40 billion energy units against consumption of 120, 180 and 200. Only one country produces nothing at all, and ENG-3.D.1's uneven endowment is what puts countries in such different positions."),
 ("160 billion energy units",
  "Recomputed in q28 above: 200 minus 40 billion energy units. The rejected values quote that country's consumption alone, add the two amounts, quote another country's consumption, or invert the direction the record shows."),
 ("The first country, by 180 billion energy units",
  "Recomputed in q29 above: 300 produced against 120 used, and no other country in the record runs a surplus. The rejected values add the two amounts instead of subtracting them or attach the surplus to a country that does not have one."),
 ("is not uniform, and it depends on the geologic history of regions",
  "The keyed summary carries ENG-3.D.1 whole: the subject, the four examples, the denial of uniformity and the dependence on geologic history. Each rejected summary reverses the uniformity claim, swaps the explanation, closes a list the framework leaves open, or claims figures the framework never supplies."),
]

TABLE_CHECKS = {19: q19, 20: q20, 21: q21, 22: q22, 23: q23, 24: q24,
                25: q25, 26: q26, 27: q27, 28: q28, 29: q29}


def _selftest():
    """Reversal alone must be caught for every table, with no flatten fallback.

    Three of these checks compute something a column reversal leaves untouched:
    q20's leader share of a total, q21's ratio between the two largest values,
    and q26's area summed over the rows holding nothing. All three therefore
    pin their rows by label as well, and this control is what proves the pin
    does the work rather than the arithmetic.
    """
    import copy
    import types

    def run_on(questions):
        mod = types.ModuleType("e6_4_mutant")
        mod.TOPIC = e6_4.TOPIC
        mod.QUESTIONS = questions
        e_check.style(mod)
        e_check.no_figure_reference(mod)
        cg.check(mod, CLAIMS, table_checks=TABLE_CHECKS)

    def must_fail(label, mutate):
        qs = copy.deepcopy(e6_4.QUESTIONS)
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
    must_fail("q19 coal and crude oil leaders brought into the same row",
              edit(19, R2, OILCOL, "20"))
    must_fail("q20 leader share moved off 90 percent", edit(20, R3, COALCOL, "160"))
    must_fail("q21 ratio moved off fifteen", edit(21, R3, COALCOL, "90"))
    must_fail("q23 the empty region given some natural gas", edit(23, R4, GASCOL, "5"))
    must_fail("q24 a volcanic region given crude oil", edit(24, RC, OILCOL, "500"))
    must_fail("q25 marine total moved off 1,050", edit(25, RB, OILCOL, "400"))
    must_fail("q26 a marine region emptied of crude oil", edit(26, RB, OILCOL, "0"))
    must_fail("q27 the importer given a domestic supply", edit(27, C2, MADE, "20"))
    must_fail("q28 shortfall moved off 160", edit(28, C3, MADE, "60"))
    must_fail("q29 the surplus country pushed into deficit", edit(29, C1, USED, "400"))

    print("selftest: the unmodified module must still pass (positive control)")
    run_on(copy.deepcopy(e6_4.QUESTIONS))
    print("all selftest controls raised as required, and the clean module passes.")


if __name__ == "__main__":
    import sys
    if "--selftest" in sys.argv:
        _selftest()

e_check.run(e6_4, CLAIMS, TABLE_CHECKS)
