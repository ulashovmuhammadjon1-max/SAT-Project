"""Key audit for AP ENVIRONMENTAL SCIENCE 6.2 Global Energy Consumption.

One (anchor, claim) per item, in module order. The anchor must appear in the
KEYED choice and in no distractor, so an off-by-one key or a reordered choice
list fails here rather than reaching a student.

WHY THIS FILE EXISTS. The module was left behind by a stopped agent with no
verifier at all -- thirty questions and no gate. Writing the gate found four
real defects, all of them the same family and all now fixed in e6_2.py:

  q3   "It increases" was wholly contained in "It increases only where the
       country has no fossil fuel of its own", so a student who accepts the
       short option has no ground to reject the long one. Rewritten to
       "It changes only where ...".
  q4   the same defect, "It increases" inside "It increases in developed
       countries and decreases in developing ones". Rewritten to "It rises in
       developed countries and falls in developing ones".
  q6, q26, q27  a one-word option ("Price", "Availability", "Governmental
       regulations") beside a compound option that quoted it verbatim. The
       compound options are gone and every option is now a distinct phrase.
  q11  the keyed conclusion opened with a clause that the third option also
       contained word for word, so no anchor drawn from the opening could tell
       them apart. The third option was rewritten to say the same wrong thing
       in different words.

WHAT THE KEYS REST ON
---------------------
  ENG-3.B.1  The use of energy resources is not evenly distributed between
             developed and developing countries.
                                     -- items 1, 8, 9, 10, 22, 24
  ENG-3.B.2  The most widely used sources of energy globally are fossil fuels.
                                     -- items 2, 11, 12
  ENG-3.B.3  As developing countries become more developed, their reliance on
             fossil fuels for energy increases.
                                     -- items 3, 7, 13, 14, 15, 23
  ENG-3.B.4  As the world becomes more industrialized, the demand for energy
             increases.              -- items 4, 7, 13, 16, 17, 25
  ENG-3.B.5  Availability, price, and governmental regulations influence which
             energy sources people use and how they use them.
                                     -- items 5, 6, 18, 19, 20, 21, 26, 27
  items 28, 29 and 30 read across all five, and item 28 keys what the five do
  NOT supply: the framework gives no percentage, no per-person figure, no
  country and no year anywhere in this topic.

WHAT IS DELIBERATELY NOT KEYED. Whether a source is renewable is ENG-3.A in
topic 6.1. Where resources occur, and the geologic history behind it, is
ENG-3.D.1 in topic 6.4. Neither is used as a key here.

THE SUGGESTED SKILL IS 6.C, calculate an accurate numeric answer with
appropriate units, so fourteen of the thirty items are quantitative. Items 8 to
21 carry tables and EVERY figure their keys assert is recomputed below from that
table alone -- a ratio, a per-person amount, a share, a difference in percentage
points. Nothing is taken on the module's word.

TWO TABLES SURVIVE A COLUMN REVERSAL, and the checks are written for it.
Reversing the price column and the households column of the district table
leaves the same (price, share) pairs, so an association-only check could not
fire; the same holds for the difference in item 19. Both checks therefore also
pin the cheapest district by ROW LABEL, which a reversal does break.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and every table in turn, and requires each
corruption to raise, BEFORE the real gate runs. It is not behind a flag.
"""
import e_check
import cg_check as cg
import e6_2

PEOPLE = "People (millions)"
ENERGY = "Energy used in a year (billion energy units)"
DEVED = "Developed countries"
DEVING = "Developing countries"

MIXSHARE = "Share of world energy supply (percent)"
COAL = "Coal"
OIL = "Crude oil and its products"
GAS = "Natural gas"
NUC = "Nuclear power"
OTHERSRC = "All other sources together"

OUTPUT = "Industrial output (index)"
PERPERSON = "Energy used per person (energy units)"
FOSSILSHARE = "Share of that energy from fossil fuels (percent)"
FIRST, SECOND, THIRD, FOURTH = "First", "Second", "Third", "Fourth"

WOUT = "World industrial output (index)"
WDEM = "World energy demand (billion energy units)"

PRICE = "Price of the fuel (currency units per energy unit)"
USING = "Households using that fuel (percent)"
D1, D2, D3 = "District 1", "District 2", "District 3"

SULFUR = "Sulfur permitted in household fuel (percent by mass)"
STILL = "Households still using the high sulfur fuel (percent)"
BEFORE = "Before the regulation"
AFTER2 = "Two years after the regulation"
AFTER5 = "Five years after the regulation"


def _rising(vals):
    return all(vals[i] < vals[i + 1] for i in range(len(vals) - 1))


def _falling(vals):
    return all(vals[i] > vals[i + 1] for i in range(len(vals) - 1))


# ------------------------------------------------------- the two country groups

def q8(table, item):
    """Same total energy, five times the people. That is the unevenness."""
    ed_e, ing_e = cg.cell(table, DEVED, ENERGY), cg.cell(table, DEVING, ENERGY)
    ed_p, ing_p = cg.cell(table, DEVED, PEOPLE), cg.cell(table, DEVING, PEOPLE)
    assert ed_e == ing_e, f"the two totals must be equal; got {ed_e} and {ing_e}"
    assert ing_p == 5 * ed_p, \
        f"the developing group must hold five times the people; got {ing_p} against {ed_p}"
    assert ing_e / ing_p < ed_e / ed_p, \
        "the developing group must use less for each person, or the totals conceal nothing"
    return (f"both groups use {ed_e:.0f} billion energy units while the populations are "
            f"{ed_p:.0f} and {ing_p:.0f} million, so equal totals sit on unequal populations")


def q9(table, item):
    """Energy for each person, developed against developing."""
    ed = cg.cell(table, DEVED, ENERGY) / cg.cell(table, DEVED, PEOPLE)
    ing = cg.cell(table, DEVING, ENERGY) / cg.cell(table, DEVING, PEOPLE)
    ratio = ed / ing
    assert ratio == 5, f"the ratio recomputes to {ratio}, not 5"
    for wrong in (4, 2, 8, 1):
        assert ratio != wrong, f"the {wrong} distractor equals the key"
    return (f"{ed:.1f} energy units for each person against {ing:.1f} is a ratio of "
            f"{ratio:.0f} to one")


def q10(table, item):
    """The developed group's share of people, and its share of energy."""
    ppl = cg.col(table, PEOPLE)
    eng = cg.col(table, ENERGY)
    share_p = cg.cell(table, DEVED, PEOPLE) / sum(ppl)
    share_e = cg.cell(table, DEVED, ENERGY) / sum(eng)
    assert abs(share_p - 1 / 6) < 1e-9, f"the share of people recomputes to {share_p}, not a sixth"
    assert abs(share_e - 1 / 2) < 1e-9, f"the share of energy recomputes to {share_e}, not a half"
    assert share_e > share_p, "the energy share must exceed the population share"
    return (f"{cg.cell(table, DEVED, PEOPLE):.0f} of {sum(ppl):.0f} million people is a sixth, "
            f"and {cg.cell(table, DEVED, ENERGY):.0f} of {sum(eng):.0f} billion units is a half")


# ---------------------------------------------------------- the world's sources

def _fossil_three(table):
    return (cg.cell(table, COAL, MIXSHARE) + cg.cell(table, OIL, MIXSHARE)
            + cg.cell(table, GAS, MIXSHARE))


def q11(table, item):
    """The three fossil fuels must outweigh everything else put together."""
    three = _fossil_three(table)
    rest = cg.cell(table, NUC, MIXSHARE) + cg.cell(table, OTHERSRC, MIXSHARE)
    assert abs(three + rest - 100) < 1e-9, f"the five shares must total 100; got {three + rest}"
    assert three > rest, f"the three fossil fuels must outweigh the rest; got {three} against {rest}"
    assert cg.cell(table, NUC, MIXSHARE) < max(cg.col(table, MIXSHARE)), \
        "'nuclear power supplies the largest part' must be false"
    assert cg.cell(table, COAL, MIXSHARE) <= 50, "'coal alone supplies more than half' must be false"
    assert len(set(cg.col(table, MIXSHARE))) > 1, "'all five supply about the same' must be false"
    return (f"the shares are {cg.col(table, MIXSHARE)} percent, so the three fossil fuels supply "
            f"{three:.0f} against {rest:.0f} from everything else")


def q12(table, item):
    """The three fossil shares added."""
    three = _fossil_three(table)
    assert three == 80, f"the three fossil shares recompute to {three}, not 80 percent"
    for wrong in (cg.cell(table, COAL, MIXSHARE) + cg.cell(table, OIL, MIXSHARE),
                  three + cg.cell(table, NUC, MIXSHARE),
                  cg.cell(table, COAL, MIXSHARE),
                  cg.cell(table, OTHERSRC, MIXSHARE)):
        assert three != wrong, f"the {wrong} distractor equals the key"
    return (f"{cg.cell(table, COAL, MIXSHARE):.0f} plus {cg.cell(table, OIL, MIXSHARE):.0f} plus "
            f"{cg.cell(table, GAS, MIXSHARE):.0f} is {three:.0f} percent from the three fossil fuels")


# ------------------------------------------------------ one developing country

def q13(table, item):
    """Output, energy per person and the fossil share must all rise together."""
    out = [cg.cell(table, d, OUTPUT) for d in (FIRST, SECOND, THIRD)]
    per = [cg.cell(table, d, PERPERSON) for d in (FIRST, SECOND, THIRD)]
    fos = [cg.cell(table, d, FOSSILSHARE) for d in (FIRST, SECOND, THIRD)]
    assert _rising(out), f"industrial output must rise down the record; got {out}"
    assert _rising(per), f"energy for each person must rise down the record; got {per}"
    assert _rising(fos), f"the fossil fuel share must rise down the record; got {fos}"
    return (f"output runs {out}, energy for each person runs {per} and the fossil share runs "
            f"{fos} percent, all three rising together")


def q14(table, item):
    """The rise in the fossil fuel share, in percentage points."""
    rise = cg.cell(table, THIRD, FOSSILSHARE) - cg.cell(table, FIRST, FOSSILSHARE)
    assert rise == 36, f"the rise recomputes to {rise}, not 36 percentage points"
    for wrong in (cg.cell(table, THIRD, FOSSILSHARE),
                  cg.cell(table, THIRD, FOSSILSHARE) + cg.cell(table, FIRST, FOSSILSHARE),
                  cg.cell(table, SECOND, FOSSILSHARE) - cg.cell(table, FIRST, FOSSILSHARE),
                  cg.cell(table, THIRD, FOSSILSHARE) - cg.cell(table, SECOND, FOSSILSHARE)):
        assert rise != wrong, f"the {wrong} distractor equals the key"
    return (f"{cg.cell(table, THIRD, FOSSILSHARE):.0f} minus "
            f"{cg.cell(table, FIRST, FOSSILSHARE):.0f} is {rise:.0f} percentage points")


def q15(table, item):
    """Energy for each person in the third decade against the first."""
    base = cg.cell(table, FIRST, PERPERSON)
    assert base > 0, "the first decade's figure must be non-zero for a ratio to exist"
    ratio = cg.cell(table, THIRD, PERPERSON) / base
    assert abs(ratio - 5) < 1e-9, f"the ratio recomputes to {ratio}, not 5"
    for wrong in (4, 2, 10, 1):
        assert abs(ratio - wrong) > 1e-9, f"the {wrong} distractor equals the key"
    return (f"{cg.cell(table, THIRD, PERPERSON)} divided by {base} is {ratio:.0f} times as much "
            "energy for each person")


# ------------------------------------------------------------ the world's record

def q16(table, item):
    """Industrialization and demand must move together."""
    out = cg.col(table, WOUT)
    dem = cg.col(table, WDEM)
    assert _rising(out), f"world industrial output must rise; got {out}"
    assert _rising(dem), f"world energy demand must rise; got {dem}"
    assert cg.cell(table, FIRST, WDEM) == min(dem), "the first decade must hold the lowest demand"
    assert cg.cell(table, FOURTH, WDEM) == max(dem), "the fourth decade must hold the highest demand"
    return (f"output runs {out} while demand runs {dem} billion energy units, the two rising "
            "together across the four decades")


def q17(table, item):
    """The growth in world demand across the record."""
    growth = cg.cell(table, FOURTH, WDEM) - cg.cell(table, FIRST, WDEM)
    assert growth == 4800, f"the growth recomputes to {growth}, not 4,800 billion energy units"
    for wrong in (cg.cell(table, FOURTH, WDEM),
                  cg.cell(table, FOURTH, WDEM) + cg.cell(table, FIRST, WDEM),
                  cg.cell(table, THIRD, WDEM) - cg.cell(table, FIRST, WDEM),
                  cg.cell(table, FOURTH, WOUT) - cg.cell(table, FIRST, WOUT)):
        assert growth != wrong, f"the {wrong} distractor equals the key"
    return (f"{cg.cell(table, FOURTH, WDEM):.0f} minus {cg.cell(table, FIRST, WDEM):.0f} is "
            f"{growth:.0f} billion energy units of growth")


# ------------------------------------------------------------------ price, rules

def q18(table, item):
    """Use must fall as price rises -- and the record must be read in price order.

    Reversing both numeric columns leaves the (price, share) pairs untouched, so
    an association-only check could not fire. Pinning the cheapest district by
    ROW LABEL is what a reversal breaks.
    """
    price = cg.col(table, PRICE)
    share = cg.col(table, USING)
    assert _rising(price), f"the districts must be listed in rising price order; got {price}"
    assert _falling(share), f"the share using the fuel must fall as price rises; got {share}"
    assert cg.cell(table, D1, PRICE) == min(price), "the first district must be the cheapest"
    assert cg.cell(table, D1, USING) == max(share), \
        "the cheapest district must hold the largest share of users"
    return (f"prices run {price} currency units for each energy unit while the share using the "
            f"fuel runs {share} percent, falling as price rises")


def q19(table, item):
    """The gap in use between the dearest district and the cheapest."""
    price = cg.col(table, PRICE)
    assert cg.cell(table, D1, PRICE) == min(price), "the first district must be the cheapest"
    assert cg.cell(table, D3, PRICE) == max(price), "the third district must be the dearest"
    gap = cg.cell(table, D1, USING) - cg.cell(table, D3, USING)
    assert gap == 59, f"the gap recomputes to {gap}, not 59 percentage points"
    for wrong in (cg.cell(table, D1, USING),
                  cg.cell(table, D1, USING) + cg.cell(table, D3, USING),
                  cg.cell(table, D1, USING) - cg.cell(table, D2, USING),
                  cg.cell(table, D2, USING) - cg.cell(table, D3, USING)):
        assert gap != wrong, f"the {wrong} distractor equals the key"
    return (f"{cg.cell(table, D1, USING):.0f} percent where the fuel costs least minus "
            f"{cg.cell(table, D3, USING):.0f} percent where it costs most is {gap:.0f} "
            "percentage points")


def q20(table, item):
    """Tightening the permitted level and the fall in use must go together."""
    sulfur = [cg.cell(table, s, SULFUR) for s in (BEFORE, AFTER2, AFTER5)]
    users = [cg.cell(table, s, STILL) for s in (BEFORE, AFTER2, AFTER5)]
    assert _falling(sulfur), f"the permitted sulfur must be cut down the record; got {sulfur}"
    assert _falling(users), f"the share still using the fuel must fall; got {users}"
    assert cg.cell(table, BEFORE, SULFUR) == max(sulfur), \
        "the highest permitted level must be the one before the regulation"
    assert cg.cell(table, BEFORE, STILL) == max(users), \
        "the largest share of users must be the one before the regulation"
    return (f"the permitted sulfur runs {sulfur} percent by mass while the share still using the "
            f"fuel runs {users} percent, both falling after the regulation")


def q21(table, item):
    """The fall in use across the five years of the record."""
    fall = cg.cell(table, BEFORE, STILL) - cg.cell(table, AFTER5, STILL)
    assert fall == 52, f"the fall recomputes to {fall}, not 52 percentage points"
    for wrong in (cg.cell(table, BEFORE, STILL),
                  cg.cell(table, BEFORE, STILL) + cg.cell(table, AFTER5, STILL),
                  cg.cell(table, BEFORE, STILL) - cg.cell(table, AFTER2, STILL),
                  cg.cell(table, AFTER2, STILL) - cg.cell(table, AFTER5, STILL)):
        assert fall != wrong, f"the {wrong} distractor equals the key"
    return (f"{cg.cell(table, BEFORE, STILL):.0f} minus {cg.cell(table, AFTER5, STILL):.0f} is "
            f"{fall:.0f} percentage points fewer households on the high sulfur fuel")


CLAIMS = [
 ("not evenly distributed between them",
  "ENG-3.B.1, near verbatim: the use of energy resources IS NOT EVENLY DISTRIBUTED between developed and developing countries. The rejected options reverse the claim, narrow it to regions within a group, or deny that the framework makes it."),
 ("Fossil fuels",
  "ENG-3.B.2, near verbatim: THE MOST WIDELY USED SOURCES OF ENERGY GLOBALLY ARE FOSSIL FUELS. Nuclear, wind, solar, hydroelectric power and biomass are each named elsewhere in the unit but none of them is given this position."),
 ("It increases",
  "ENG-3.B.3, near verbatim: AS DEVELOPING COUNTRIES BECOME MORE DEVELOPED, THEIR RELIANCE ON FOSSIL FUELS FOR ENERGY INCREASES. The direction is upward, which is the opposite of what many students expect, and the framework attaches no condition to it."),
 ("It increases",
  "ENG-3.B.4, near verbatim: AS THE WORLD BECOMES MORE INDUSTRIALIZED, THE DEMAND FOR ENERGY INCREASES. The statement is about the world as a whole and it carries no efficiency offset and no split between the two groups of countries."),
 ("price, and governmental regulations",
  "ENG-3.B.5 names AVAILABILITY, PRICE, AND GOVERNMENTAL REGULATIONS and nothing else. Climate, population growth, rainfall, soil type, equipment age and distance to a coast appear nowhere in the statement."),
 ("climate of the region",
  "ENG-3.B.5's three influences are availability, price and governmental regulations, so climate is not among them. Two rejected options restate governmental regulation in different words, one restates availability and one restates price, so all four are things the statement does name."),
 ("reliance on fossil fuels rises as it develops; the other says the world's total demand for energy rises",
  "ENG-3.B.3 is about DEVELOPING COUNTRIES and their RELIANCE ON FOSSIL FUELS; ENG-3.B.4 is about THE WORLD and its TOTAL DEMAND FOR ENERGY. Different subject and different quantity. One rejected option is the exact swap of the two directions, so the anchor carries both clauses rather than either alone."),
 ("not evenly distributed, since the two groups use the same total energy",
  "Recomputed in q8 above: 4,000 billion energy units each, over 1,000 million people against 5,000 million. ENG-3.B.1 states that use is NOT EVENLY DISTRIBUTED between developed and developing countries. One rejected option reaches the same verdict from a false reading of the table, so the anchor carries the ground as well as the verdict."),
 ("Five times as much",
  "Recomputed in q9 above: 4.0 energy units for each person against 0.8. ENG-3.B.1's unevenness is exactly this ratio. The rejected values misdivide one of the two rows or deny that the groups differ."),
 ("A sixth of the people, using half",
  "Recomputed in q10 above: 1,000 of 6,000 million people is a sixth and 4,000 of 8,000 billion energy units is a half. The gap between those two fractions is what ENG-3.B.1 calls uneven distribution."),
 ("natural gas together supply the largest part",
  "Recomputed in q11 above: 26, 31 and 23 percent against 4 from nuclear power and 16 from everything else. ENG-3.B.2 states that the most widely used sources of energy globally are fossil fuels."),
 ("80 percent",
  "Recomputed in q12 above: 26 plus 31 plus 23 percent. The rejected values leave out natural gas, add nuclear power to the three, quote coal alone, or quote the unclassified remainder."),
 ("energy demand rises with industrialization, and that reliance on fossil fuels rises",
  "Recomputed in q13 above: output 20, 55 and 110, energy for each person 0.6, 1.4 and 3.0, fossil share 38, 57 and 74 percent, all rising together. ENG-3.B.4 has demand rising with industrialization and ENG-3.B.3 has reliance on fossil fuels rising as a developing country develops. One rejected option keeps the first direction and inverts the second, so the anchor carries both."),
 ("36 percentage points",
  "Recomputed in q14 above: 74 minus 38 percent. The rejected values quote the final share alone, add the two, or take one of the two decade-to-decade steps inside the record."),
 ("Five times as much",
  "Recomputed in q15 above: 3.0 divided by 0.6 energy units for each person. The rejected values come from the middle decade, from the industrial output column, or from denying that the decades differ."),
 ("demand for energy increases as the world becomes more industrialized",
  "Recomputed in q16 above: output 100, 150, 210 and 300 against demand 3,000, 4,200, 5,700 and 7,800 billion energy units, rising together. ENG-3.B.4 states this trend in so many words."),
 ("4,800 billion energy units",
  "Recomputed in q17 above: 7,800 minus 3,000 billion energy units. The rejected values quote the final decade alone, add the two, take a shorter interval, or take the rise in the industrial output column."),
 ("Price, since the share of households using the fuel falls",
  "Recomputed in q18 above: prices of 2, 5 and 9 currency units for each energy unit against household shares of 78, 46 and 19 percent. ENG-3.B.5 names PRICE among the three influences. One rejected option gives the same influence with the direction inverted and another gives the right direction under the wrong influence, so the anchor carries both halves."),
 ("59 percentage points",
  "Recomputed in q19 above: 78 percent where the fuel costs least minus 19 percent where it costs most. The rejected values quote the cheapest district alone, add the two, or take one of the two steps between adjacent districts."),
 ("Governmental regulations, since fewer households used the high sulfur fuel",
  "Recomputed in q20 above: permitted sulfur cut from 5.0 to 2.0 to 1.0 percent by mass while the share still using the fuel falls from 64 to 35 to 12 percent. ENG-3.B.5 names GOVERNMENTAL REGULATIONS among the three influences. One rejected option inverts the direction and another swaps the influence, so the anchor carries both halves."),
 ("52 percentage points",
  "Recomputed in q21 above: 64 minus 12 percent. The rejected values quote the opening share alone, add the two, or take one of the two steps within the record."),
 ("not evenly distributed between developed and developing countries",
  "ENG-3.B.1 is a flat denial of even distribution between developed and developing countries, so the student's sentence has to be reversed rather than qualified. The rejected corrections accept the claim, narrow it, or deny that the framework speaks to the question."),
 ("reliance INCREASING as a developing country",
  "ENG-3.B.3 states that AS DEVELOPING COUNTRIES BECOME MORE DEVELOPED, THEIR RELIANCE ON FOSSIL FUELS FOR ENERGY INCREASES. The direction is the whole content of the statement, which is why inverting it is the mistake worth naming."),
 ("for each person in developed countries set beside energy used for each person",
  "ENG-3.B.1 is about how use is distributed between the two groups, and a comparison for each person is what exposes it while totals alone can conceal it. Price, counts of available sources and dates of first use are outside the statement."),
 ("over the same decades in which world industrial output rose",
  "ENG-3.B.4 ties rising demand for energy to the world becoming more industrialized, so the two quantities must move together and both must be measured for the world. One rejected option reports ENG-3.B.3 instead, which is a statement about a developing country's fuel mix rather than about world demand."),
 ("Governmental regulations",
  "ENG-3.B.5 names availability, price and GOVERNMENTAL REGULATIONS as the three influences on which energy sources people use, and a national prohibition is a governmental regulation. Nothing in the case turns on what the fuel costs, on how much of it lies nearby, or on the weather."),
 ("The price of the fuel",
  "ENG-3.B.5 names availability, PRICE and governmental regulations, and a doubling of the cost for each unit of energy is a change in price. No rule was made, no supply disappeared, and equipment age is not one of the three."),
 ("figure for how much more energy a developed country uses",
  "ENG-3.B.1 through B.5 give directions and lists and not one number: no percentage, no per-person figure, no country and no year appears in any of them. Each rejected option quotes a claim the five statements do make."),
 ("two describe how use changes as countries and the world develop",
  "ENG-3.B.1 and B.2 describe the present pattern of use, B.3 and B.4 describe change over time in a developing country and in the world, and B.5 names availability, price and governmental regulations as the influences on the choice of source."),
 ("reliance on fossil fuels rises as a developing country develops; demand rises as the world industrializes",
  "The keyed summary carries all five of ENG-3.B.1 to B.5 in the framework's own directions and adds nothing. Each rejected summary reverses a direction, substitutes influences the framework never names, or claims figures the framework does not give."),
]

TABLE_CHECKS = {8: q8, 9: q9, 10: q10, 11: q11, 12: q12, 13: q13, 14: q14,
                15: q15, 16: q16, 17: q17, 18: q18, 19: q19, 20: q20, 21: q21}


def _selftest():
    """Controls beyond the shared ones, aimed at what is bespoke here.

    ``e_check.run`` already corrupts a key, an anchor, a choice, a ``why``, the
    notation and a figure reference, and it corrupts every table by REVERSING
    its numeric columns and, only if that is not caught, by FLATTENING them.
    The flatten fallback is what would let a weak check pass quietly, so this
    selftest asserts the stronger property: reversal ALONE must be caught for
    every one of the fourteen tables.

    That matters here specifically. Reversing both numeric columns of the
    district table leaves the (price, share) pairs exactly as they were, so a
    check written only on the association between the two columns cannot fire,
    and neither can the difference in item 19. Both checks pin the cheapest
    district by row label for that reason, and this control is what proves the
    pin does the work.

    Then each keyed number is attacked one cell at a time, because a check that
    recomputes a difference correctly but never compares it against the keyed
    value would survive everything above.
    """
    import copy
    import types

    def run_on(questions):
        mod = types.ModuleType("e6_2_mutant")
        mod.TOPIC = e6_2.TOPIC
        mod.QUESTIONS = questions
        e_check.style(mod)
        e_check.no_figure_reference(mod)
        cg.check(mod, CLAIMS, table_checks=TABLE_CHECKS)

    def must_fail(label, mutate):
        qs = copy.deepcopy(e6_2.QUESTIONS)
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
            for r, v in zip(t["rows"], reversed(vals)):
                r[j] = v
        return t

    print("selftest: reversal alone must be caught for every table")
    for i in sorted(TABLE_CHECKS):
        must_fail(f"q{i} table columns reversed (no flatten fallback)",
                  lambda qs, i=i: qs[i - 1].__setitem__("table", reverse_columns(qs[i - 1]["table"])))

    print("selftest: one cell at a time, against the keyed number")

    def edit(qi, row_label, header, value):
        def mutate(qs):
            t = copy.deepcopy(qs[qi - 1]["table"])
            j = [cg.normalize(h) for h in t["headers"]].index(cg.normalize(header))
            for r in t["rows"]:
                if cg.normalize(r[0]) == cg.normalize(row_label):
                    r[j] = value
            qs[qi - 1]["table"] = t
        return mutate

    # q9 keys "five times as much": make the two groups equal for each person.
    must_fail("q9 per-person ratio driven to one",
              edit(9, DEVING, PEOPLE, "1,000"))
    # q12 keys 80 percent: move three points from gas to nuclear power.
    must_fail("q12 fossil total moved off 80 percent",
              edit(12, GAS, MIXSHARE, "20"))
    # q14 keys 36 percentage points: change the opening share.
    must_fail("q14 rise moved off 36 percentage points",
              edit(14, FIRST, FOSSILSHARE, "40"))
    # q17 keys 4,800 billion: change the closing demand.
    must_fail("q17 growth moved off 4,800 billion energy units",
              edit(17, FOURTH, WDEM, "8,000"))
    # q19 keys 59 percentage points, and the pairing must survive: swap the
    # share of the cheapest district for the share of the dearest, which leaves
    # both columns' multisets untouched.
    def swap_district_shares(qs):
        t = copy.deepcopy(qs[18]["table"])
        j = [cg.normalize(h) for h in t["headers"]].index(cg.normalize(USING))
        t["rows"][0][j], t["rows"][2][j] = t["rows"][2][j], t["rows"][0][j]
        qs[18]["table"] = t
    must_fail("q19 cheapest and dearest districts' shares swapped", swap_district_shares)
    # q21 keys 52 percentage points: change the closing share.
    must_fail("q21 fall moved off 52 percentage points",
              edit(21, AFTER5, STILL, "20"))

    print("selftest: the unmodified module must still pass (positive control)")
    run_on(copy.deepcopy(e6_2.QUESTIONS))
    print("all selftest controls raised as required, and the clean module passes.")


if __name__ == "__main__":
    import sys
    if "--selftest" in sys.argv:
        _selftest()

e_check.run(e6_2, CLAIMS, TABLE_CHECKS)
