"""Key audit for AP ENVIRONMENTAL SCIENCE 6.1 Renewable and Nonrenewable Resources.

One (anchor, claim) per item, in module order. The anchor must appear in the
KEYED choice and in no distractor.

WHAT THE KEYS REST ON
---------------------
  ENG-3.A.1  Nonrenewable energy sources are those that exist in a fixed amount
             and involve energy transformation that cannot be easily replaced.
                              -- items 1, 5, 12, 13, 18, 19, 21, 26, 27, 30
  ENG-3.A.2  Renewable energy sources are those that can be replenished
             naturally, at or near the rate of consumption, and reused.
                       -- items 2, 3, 4, 10, 11, 14, 15, 20, 22, 23, 24, 25, 26, 27, 28, 30

THE ONLY CLASSIFICATIONS KEYED, and where each comes from. The two definitions
classify NO named source, so a module that sorted fuels into two columns would
be inventing its keys. Three classifications are stated by the framework itself
and only these three are used:
  nuclear power  ENG-3.G.4, verbatim "Nuclear power generation is a nonrenewable
                 energy source."                          -- items 6, 9, 16, 17
  wind energy    ENG-3.S.1, verbatim "Wind energy is a renewable, clean source of
                 energy."                                 -- items 7, 9, 16, 17
  fossil fuels   the unit's Developing Understanding page, which asks "Why are
                 fossil fuels the most widely used energy resources if they are
                 nonrenewable?"                        -- items 8, 16, 17, 29
Hydrogen is NOT classified anywhere here: ENG-3.P.1 calls a fuel cell "an
alternate to non-renewable fuel sources" without saying what hydrogen is. Nor
are biomass, hydroelectricity or geothermal energy, which the framework never
labels. Item 16's fourth table row is deliberately left unsorted for that reason.

TWO CHAINS, named in their claims: ENG-3.B.2 (fossil fuels most widely used) and
ENG-3.B.5 (availability, price and governmental regulations influence which
sources people use), both in item 29.

RENEWABLE AND CLEAN ARE TWO CLAIMS. ENG-3.S.1 gives wind both adjectives while
ENG-3.G.4 calls nuclear power nonrenewable AND cleaner. Item 9 keys that they
come apart, and no key anywhere treats them as one property.

DATA ITEMS: 10, 11, 12, 13, 14, 15, 16, 17, 18 and 19, recomputed below from
those tables alone and addressed by row label.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and every table in turn, and requires each
corruption to raise, BEFORE the real gate runs. It is not behind a flag.
"""
import e_check
import cg_check as cg
import e6_1

REPL = "Replenished naturally each year (energy units)"
CONS = "Consumed each year (energy units)"

LEFT = "Amount of the deposit remaining (energy units)"
ADDED = "Amount added to the deposit during the decade (energy units)"

TAKEN = "Energy taken from the source that year (energy units)"
BACK = "Energy replenished naturally that year (energy units)"

SHARE = "Share of the country's energy (percent)"
FOSSIL = "Fossil fuels"
NUCLEAR = "Nuclear power"
WINDROW = "Wind"
OTHER = "All other sources together"

REMAIN = "Amount remaining (energy units)"
USED = "Amount used each year (energy units)"
A, B, C = "Deposit A", "Deposit B", "Deposit C"


def q10(table, item):
    near = [lab for lab in cg.labels(table)
            if cg.cell(table, lab, REPL) >= 0.9 * cg.cell(table, lab, CONS)]
    assert near == ["Source 1", "Source 2"], \
        f"the sources replenished at or near their consumption are {near}, not the first two"
    assert cg.cell(table, "Source 3", CONS) > 10 * cg.cell(table, "Source 3", REPL), \
        "the third source must fall far short of its consumption"
    assert cg.cell(table, "Source 4", REPL) == 0, "the fourth source must not be replenished"
    for lab in ("Source 1", "Source 2"):
        assert cg.cell(table, lab, REPL) > cg.cell(table, lab, CONS), \
            f"{lab} must not be consumed faster than it is replenished"
    return (f"replenishment runs {cg.col(table, REPL)} energy units against consumption of "
            f"{cg.col(table, CONS)}, so {near} keep pace and the others do not")


def q11(table, item):
    base = cg.cell(table, "Source 3", REPL)
    assert base > 0, "the third source's replenishment must be non-zero for a ratio to exist"
    ratio = cg.cell(table, "Source 3", CONS) / base
    assert ratio == 30, f"the ratio recomputes to {ratio}, not 30"
    for wrong in (3, 15, 2, 1):
        assert ratio != wrong, f"the {wrong} distractor equals the key"
    return f"60 divided by 2 is {ratio:.0f} times as much consumed as replenished each year"


def q12(table, item):
    v, a = cg.col(table, LEFT), cg.col(table, ADDED)
    assert all(x == 0 for x in a), f"nothing may be added to the deposit; got {a}"
    assert cg.cell(table, "First", LEFT) == max(v), "the first decade must hold the most"
    assert all(v[i] > v[i + 1] for i in range(len(v) - 1)), f"the deposit must fall; got {v}"
    return (f"the deposit runs {v} energy units while the amount added stays at {a} in every "
            "decade")


def q13(table, item):
    d = cg.cell(table, "First", LEFT) - cg.cell(table, "Fourth", LEFT)
    assert d == 760, f"the drawdown recomputes to {d}, not 760"
    for wrong in (cg.cell(table, "First", LEFT),
                  cg.cell(table, "First", LEFT) - cg.cell(table, "Third", LEFT),
                  cg.cell(table, "Third", LEFT) - cg.cell(table, "Fourth", LEFT),
                  cg.cell(table, "Second", LEFT) - cg.cell(table, "Third", LEFT)):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"800 minus 40 is {d:.0f} energy units drawn down across the record"


def q14(table, item):
    t, b = cg.col(table, TAKEN), cg.col(table, BACK)
    for lab in cg.labels(table):
        taken, back = cg.cell(table, lab, TAKEN), cg.cell(table, lab, BACK)
        assert back >= taken, f"{lab}: replenishment {back} must keep up with the {taken} taken"
        assert back < 1.2 * taken, f"{lab}: replenishment {back} must stay NEAR the {taken} taken"
    assert min(b) > 0, "'nothing at all is replenished' must be false"
    # The record must actually vary down the years, or "the amounts change from year to
    # year" could not be rejected -- and a flattened table would satisfy the rate test
    # vacuously, which is exactly what the negative control injects.
    assert cg.cell(table, "Year 1", TAKEN) == min(t), "the first sampled year must take the least"
    assert all(t[i] < t[i + 1] for i in range(len(t) - 1)), f"the take must rise; got {t}"
    assert all(b[i] < b[i + 1] for i in range(len(b) - 1)), f"replenishment must rise; got {b}"
    return (f"the source yields {t} energy units against replenishment of {b}, each pair within "
            "a few units of the other and both rising down the record")


def q15(table, item):
    t, b = cg.col(table, TAKEN), cg.col(table, BACK)
    d = cg.cell(table, "Year 10", TAKEN) - cg.cell(table, "Year 1", TAKEN)
    assert d == 35, f"the rise recomputes to {d}, not 35"
    for wrong in (max(t), max(t) + min(t), max(b) - min(b),
                  cg.cell(table, "Year 5", TAKEN) - cg.cell(table, "Year 1", TAKEN)):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"155 minus 120 is {d:.0f} energy units more taken in the last sampled year"


def q16(table, item):
    named_nonrenewable = cg.cell(table, FOSSIL, SHARE) + cg.cell(table, NUCLEAR, SHARE)
    assert named_nonrenewable > cg.cell(table, WINDROW, SHARE), \
        "the two nonrenewable rows must supply more than the wind row"
    assert cg.cell(table, WINDROW, SHARE) < 10, "the wind share must be less than a tenth"
    assert cg.cell(table, FOSSIL, SHARE) == max(cg.col(table, SHARE)), \
        "'wind supplies the largest share' must be false"
    assert cg.cell(table, OTHER, SHARE) > 0, \
        "the unclassified row must carry a share, so that leaving it unsorted matters"
    return (f"the shares are {cg.col(table, SHARE)} percent, so the two rows the framework calls "
            f"nonrenewable supply {named_nonrenewable:.0f} against wind's "
            f"{cg.cell(table, WINDROW, SHARE):.0f}, with "
            f"{cg.cell(table, OTHER, SHARE):.0f} percent the framework does not classify")


def q17(table, item):
    total = cg.cell(table, FOSSIL, SHARE) + cg.cell(table, NUCLEAR, SHARE)
    assert total == 86, f"the share recomputes to {total}, not 86 percent"
    for wrong in (cg.cell(table, FOSSIL, SHARE),
                  total + cg.cell(table, WINDROW, SHARE),
                  cg.cell(table, NUCLEAR, SHARE), cg.cell(table, WINDROW, SHARE)):
        assert total != wrong, f"the {wrong} percent distractor equals the key"
    return f"72 plus 14 is {total:.0f} percent from the two sources the framework calls nonrenewable"


def q18(table, item):
    lives = {lab: cg.cell(table, lab, REMAIN) / cg.cell(table, lab, USED)
             for lab in cg.labels(table)}
    longest = max(lives, key=lives.get)
    biggest = max(cg.labels(table), key=lambda lab: cg.cell(table, lab, REMAIN))
    assert longest == A, f"the longest-lived deposit is {longest}, not {A}"
    assert biggest == B, f"the largest deposit is {biggest}, not {B}"
    assert longest != biggest, "the longest-lived and the largest must differ for this item"
    assert len(set(lives.values())) == len(lives), "'all three last equally long' must be false"
    return (f"the three lives recompute to {({k: round(v) for k, v in lives.items()})} years, so "
            f"{longest} outlasts the larger {biggest}")


def q19(table, item):
    lives = {lab: cg.cell(table, lab, REMAIN) / cg.cell(table, lab, USED)
             for lab in cg.labels(table)}
    shortest = min(lives, key=lives.get)
    assert shortest == C, f"the shortest-lived deposit is {shortest}, not {C}"
    assert lives[C] == 4, f"its life recomputes to {lives[C]}, not 4 years"
    for wrong in (lives[A], lives[B], 2, cg.cell(table, C, USED)):
        assert lives[C] != wrong, f"the {wrong} distractor equals the key"
    return f"240 divided by 60 is {lives[C]:.0f} years for the shortest-lived deposit"


CLAIMS = [
 ("exists in a fixed amount and involves energy transformation that cannot be easily replaced",
  "ENG-3.A.1, near verbatim: nonrenewable energy sources are those that EXIST IN A FIXED AMOUNT and involve energy transformation that CANNOT BE EASILY REPLACED. Pollution, cost and where a source is used appear nowhere in it, and one distractor is the other definition."),
 ("replenished naturally, at or near the rate of consumption, and reused",
  "ENG-3.A.2, near verbatim: renewable energy sources are those that can be REPLENISHED NATURALLY, AT OR NEAR THE RATE OF CONSUMPTION, AND REUSED. One distractor keeps natural replenishment and drops the rate test, so the anchor carries the whole clause."),
 ("replenishment must keep pace with the use",
  "ENG-3.A.2 requires replenishment AT OR NEAR THE RATE OF CONSUMPTION, a comparison between two rates rather than a claim that any replenishment will do. It asks for parity, not for a large excess in either direction."),
 ("That it can be reused",
  "ENG-3.A.2 ends its definition with AND REUSED, so reusability is part of the statement. Export, storage and taxation appear in neither definition, and the framework does supply a further property, so the last option is wrong on its face."),
 ("marks replacement as difficult rather than flatly impossible",
  "ENG-3.A.1 says the energy transformation CANNOT BE EASILY REPLACED, and that hedge is part of the definition. Reading it as an outright impossibility, or dropping it, both depart from the wording."),
 ("Nuclear power generation",
  "ENG-3.G.4 states in so many words that NUCLEAR POWER GENERATION IS A NONRENEWABLE ENERGY SOURCE. ENG-3.S.1 puts wind on the renewable side, and the framework never labels solar, hydroelectric or geothermal energy either way, which is why they are the rejected options."),
 ("Wind energy",
  "ENG-3.S.1 states in so many words that WIND ENERGY IS A RENEWABLE, CLEAN SOURCE OF ENERGY. ENG-3.G.4 puts nuclear power on the nonrenewable side and the unit overview treats fossil fuels as nonrenewable."),
 ("nonrenewable, asking why they are the most widely used energy resources",
  "The unit's Developing Understanding page frames the whole unit with the question WHY ARE FOSSIL FUELS THE MOST WIDELY USED ENERGY RESOURCES IF THEY ARE NONRENEWABLE, so the framework classifies them as nonrenewable and treats the wide use as what needs explaining. ENG-3.B.2 supplies the wide use."),
 ("separate claims, and a source may be one without the other",
  "ENG-3.S.1 gives wind two adjectives, renewable AND clean, while ENG-3.G.4 calls nuclear power nonrenewable and in the same statement a cleaner energy source because it produces no air pollutants. The two properties therefore come apart."),
 ("first two, whose replenishment each year is at or near what is consumed",
  "Recomputed in q10 above: 500 against 480 and 900 against 870, beside 2 against 60 and nothing against 45. ENG-3.A.2 asks for replenishment AT OR NEAR THE RATE OF CONSUMPTION. One distractor names the same pair for the opposite reason, so the anchor carries the ground as well as the pair."),
 ("Thirty times as much",
  "Recomputed in q11 above: 60 consumed against 2 replenished. The rejected values come from misreading the replenishment column, from halving the answer, or from denying that the two rates differ."),
 ("nonrenewable definition, because nothing is added while the amount remaining falls",
  "Recomputed in q12 above: 800, 560, 310 and 40 energy units with nothing added in any decade. ENG-3.A.1 defines a nonrenewable source as one existing in a FIXED AMOUNT. One distractor pairs the same reading with the other definition, so the anchor carries both halves."),
 ("760 energy units",
  "Recomputed in q13 above: 800 minus 40 energy units. The rejected values quote the opening amount alone or take the fall across one of the shorter intervals inside the record."),
 ("renewable definition, because what is replenished each year stays at or near what is taken",
  "Recomputed in q14 above: 120, 140 and 155 energy units taken against 125, 142 and 158 replenished. ENG-3.A.2 asks for replenishment AT OR NEAR THE RATE OF CONSUMPTION. One distractor pairs the same reading with the other definition, so the anchor carries both halves."),
 ("By 35 energy units",
  "Recomputed in q15 above: 155 minus 120 energy units. The rejected values quote the final year alone, add the two, take the rise in the replenishment column, or take a shorter interval."),
 ("which the framework treats as nonrenewable, together supply the largest part, and wind",
  "ENG-3.G.4 calls nuclear power nonrenewable, the unit overview treats fossil fuels as nonrenewable, and ENG-3.S.1 calls wind renewable; the fourth row is unnamed by the framework and is left unsorted. Recomputed in q16 above from shares of 72, 14, 9 and 5 percent."),
 ("86 percent",
  "Recomputed in q17 above: 72 plus 14 percent. The rejected values quote fossil fuels alone, add the wind share to the pair, quote nuclear power alone, or quote wind alone."),
 ("first deposit, because how long a fixed amount lasts depends on the rate of use",
  "Recomputed in q18 above: 600 units at 30 a year is twenty years, 900 at 90 is ten, and 240 at 60 is four, so the largest deposit is not the longest-lived. ENG-3.A.1 makes a nonrenewable source a FIXED AMOUNT, and a fixed amount lasts as long as the rate of use allows."),
 ("Four years",
  "Recomputed in q19 above: 240 divided by 60 energy units a year. The rejected values give the lives of the other two deposits, halve the answer, or quote the annual rate as though it were a number of years."),
 ("replenishment keeping pace with consumption, which can fail if consumption rises",
  "ENG-3.A.2 defines a renewable source as one replenished naturally AT OR NEAR THE RATE OF CONSUMPTION, a comparison that can be broken from either side. Nothing in it promises that a source cannot be exhausted, and cost and pollution are not in it."),
 ("cannot be EASILY replaced, which is a weaker claim",
  "ENG-3.A.1 says the energy transformation CANNOT BE EASILY REPLACED, a statement about difficulty rather than impossibility. The rejected options reverse the clause or import the other definition."),
 ("replaced naturally in a year set against how much is used",
  "ENG-3.A.2 makes the test a comparison between natural replenishment and consumption over the same period. Cost, popularity, pollution and length of service are not in either definition, though the framework treats them elsewhere."),
 ("replenished naturally in a period, and the amount consumed in the same period",
  "ENG-3.A.2 sets replenishment AT OR NEAR THE RATE OF CONSUMPTION, so both sides must be measured over the same period. Each rejected pair supplies at most one of the two, which is why the anchor spans the pairing."),
 ("fails the renewable definition, because replenishment is not at or near the rate",
  "ENG-3.A.2 requires replenishment AT OR NEAR THE RATE OF CONSUMPTION, so natural replenishment far below the rate of use does not satisfy it. The rejected options drop the rate comparison or invert what natural replenishment means."),
 ("meets the renewable definition on both counts",
  "ENG-3.A.2 names two things, replenishment AT OR NEAR the rate of consumption and reuse, and this source satisfies both. The word near allows the two rates to differ slightly, and reuse is inside the statement rather than outside it."),
 ("How much pollution it releases and how much it costs",
  "ENG-3.A.1 and ENG-3.A.2 speak of fixed amounts, replacement, natural replenishment and the rate comparison, and of nothing else. Cost and pollution belong to other statements, so reading them out of these definitions adds to them; every rejected option quotes one of the four things the definitions do settle."),
 ("renewable definition turns on the rate comparison; the nonrenewable definition turns on the fixed amount",
  "ENG-3.A.2 sets replenishment against the rate of consumption while ENG-3.A.1 opens with EXIST IN A FIXED AMOUNT. One distractor is the exact swap, so the anchor carries both halves."),
 ("Consumption has risen year after year while natural replenishment has stayed level",
  "ENG-3.A.2's test is replenishment AT OR NEAR THE RATE OF CONSUMPTION, and rising use against level replenishment pulls the two apart. Falling use moves them together, and pollution, popularity and price sit outside the definition."),
 ("separate question from whether it is renewable, and the framework answers it with availability, price",
  "The unit overview asks why fossil fuels are the most widely used resources IF THEY ARE NONRENEWABLE, ENG-3.B.2 records that they are the most widely used, and ENG-3.B.5 names availability, price and governmental regulations as what influences which sources people use."),
 ("fixed amount and involves an energy transformation that cannot easily be replaced; a renewable source",
  "The keyed summary is ENG-3.A.1 and ENG-3.A.2 with nothing removed and nothing added. Each rejected summary swaps the two definitions, substitutes pollution for the stated tests, drops the rate comparison, or denies that definitions are given."),
]

TABLE_CHECKS = {10: q10, 11: q11, 12: q12, 13: q13, 14: q14, 15: q15, 16: q16,
                17: q17, 18: q18, 19: q19}

e_check.run(e6_1, CLAIMS, TABLE_CHECKS)
