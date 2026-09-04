"""Key audit for AP ENVIRONMENTAL SCIENCE 2.6 Adaptations.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor.

WHAT THE KEYS REST ON
---------------------
ERT-2.H.1  Natural selection acts on heritable traits, causing populations to
           adapt to their environment over generations via incremental changes
           at the genetic level.
                 -- items 1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 21,
                    22, 25, 27, 28, 29, 30
ERT-2.H.2  Environmental changes, either sudden or gradual, may threaten a
           species' survival, requiring individuals to alter behaviors, move,
           or perish.
                 -- items 6, 7, 8, 9, 18, 19, 20, 23, 24, 26, 27, 29, 30

ERT-2.H.1 has five parts and each key drawn from it uses one: HERITABLE traits;
the POPULATION rather than the individual; OVER GENERATIONS; INCREMENTAL; AT
THE GENETIC LEVEL. The commonest wrong answer in this area -- that an
individual adapts within its own lifetime -- is ruled out by the statement's
own words, and items 4, 10, 17, 26 and 27 are built on that.

ERT-2.H.2's list of three responses is the framework's own and is exhaustive as
written, so no key adds a fourth and none drops one. Its MAY is a hedge and
item 9 keys it.

WHAT IS DELIBERATELY NOT ASKED. The framework does not define heritable, names
no mechanism of inheritance, gives no rate of adaptation, and never says
adaptation will keep pace with a change. Item 28 asks which description of a
trait fits the framework's own phrase "at the genetic level"; the claim below
says the key rests on that phrase plus the ordinary meaning of the word, and no
item asks a student to classify a borderline case.

DATA ITEMS: 11 to 24 carry tables. Every keyed conclusion is recomputed below
from that table alone, read by column header rather than by index.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and EVERY data table in turn, and requires each
corruption to raise BEFORE the real gate runs. Three of these tables survive a
column reversal -- a reversed pair of co-varying columns still co-varies, and a
reversed set of shares is still a set of shares -- so e_check flattens them
next, and each check fails on the flat table because it needs the values to
differ or to total 100. ``python3 verify_e2_6.py --selftest`` is the same run;
the controls are not behind the flag.
"""
import sys

import cg_check as cg
import e_check
import e2_6

DARK = "Percent of the population that is the dark form"
HERITPCT = "Percent of the trait's variation that is heritable"
CHANGE = "Change in the population mean over twenty generations (percent)"
DEPTH = "Mean beak depth (millimetres)"
YEAR1 = "First year of the study (millimetres)"
YEAR5 = "Fifth year of the study (millimetres)"
COUNT = "Number of individuals"
YEARS = "Time over which it took place (years)"
RISE = "Rise in mean annual temperature (degrees Celsius)"
SURVIVE = "Percent surviving the same dose of one insecticide"
MOVED = "Percent of its individuals that moved to new ground"
ALTERED = "Percent that altered their feeding behaviour"
PERISHED = "Percent that perished"


def _rises(vals):
    return all(vals[i + 1] > vals[i] for i in range(len(vals) - 1))


def _by(table, key_header, *headers):
    keys = cg.col(table, key_header)
    order = sorted(range(len(table["rows"])), key=lambda i: keys[i])
    return [[cg.col(table, h)[i] for i in order] for h in headers]


def q11(table, item):
    pct = cg.col(table, DARK)
    assert _rises(pct), f"the dark form must rise at every generation scored; got {pct}"
    assert pct[0] < 5, "'the dark form appeared in full at the first generation' must be false"
    assert pct[-1] > 50, "'the dark form disappeared' must be false"
    assert len(set(pct)) == len(pct), "'the same share in every generation' must be false"
    return (f"the dark form reads {pct} percent across the generations scored, rising step "
            "by step rather than in one jump")


def q12(table, item):
    pct = cg.col(table, DARK)
    diff = pct[-1] - pct[0]
    assert diff == 89, f"the change must be 89 percentage points; got {diff}"
    assert diff != pct[-1] and diff != pct[0], \
        "the difference must not coincide with either endpoint"
    return (f"the dark form runs {pct[0]:.0f} percent to {pct[-1]:.0f} percent, a change of "
            f"{diff:.0f} percentage points")


def q13(table, item):
    (chg,) = _by(table, HERITPCT, CHANGE)
    assert _rises(chg), f"the change must rise with heritability; got {chg}"
    assert chg[0] == min(chg), \
        "'the least heritable trait changed the most' must be false"
    assert len(set(chg)) == len(chg), "'all four changed by the same amount' must be false"
    assert min(chg) > 0, "'none of the four changed at all' must be false"
    return (f"sorted by the heritable share of their variation the four traits changed "
            f"{chg} percent, strictly increasing")


def q14(table, item):
    labs = cg.labels(table)
    chg = dict(zip(labs, cg.col(table, CHANGE)))
    least = min(chg, key=chg.get)
    assert least == "Trait 4", f"Trait 4 must change least; got {least}"
    assert list(chg.values()).count(chg[least]) == 1, "the smallest change must be unique"
    return (f"the four changes are {sorted(chg.values())} percent and the smallest, "
            f"{chg[least]:.0f}, belongs to {least}")


def q15(table, item):
    d = cg.col(table, DEPTH)
    assert _rises(d), f"the mean must rise at every measurement; got {d}"
    steps = [d[i + 1] - d[i] for i in range(len(d) - 1)]
    assert max(steps) < 1.0, f"each step must be small beside the mean itself; got {steps}"
    assert d[-1] < 2 * d[0], "'the mean doubled' must be false"
    assert steps[-1] != sum(steps), \
        "'it changed only between the last two measurements' must be false"
    return (f"the means read {d} millimetres, moving in steps of {[round(s, 2) for s in steps]} "
            "rather than all at once")


def q16(table, item):
    d = cg.col(table, DEPTH)
    diff = d[-1] - d[0]
    assert abs(diff - 1.7) < 1e-6, f"the total change must be 1.7 millimetres; got {diff}"
    assert abs(diff - d[0]) > 1e-6 and abs(diff - d[-1]) > 1e-6, \
        "the change must not coincide with either endpoint"
    return (f"the mean runs {d[0]} to {d[-1]} millimetres, a total change of {diff:.1f}")


def q17(table, item):
    labs = cg.labels(table)
    first = dict(zip(labs, cg.col(table, YEAR1)))
    fifth = dict(zip(labs, cg.col(table, YEAR5)))
    birds = [lab for lab in labs if "marked bird" in lab]
    pop = [lab for lab in labs if "whole population" in lab]
    assert len(birds) == 3 and len(pop) == 1, \
        f"three marked birds and one population mean must be tabulated; got {birds}, {pop}"
    for lab in birds:
        assert abs(first[lab] - fifth[lab]) < 1e-9, \
            f"{lab} must be unchanged between the two years; got {first[lab]} then {fifth[lab]}"
    assert abs(first[pop[0]] - fifth[pop[0]]) > 0.5, \
        f"the population mean must shift; got {first[pop[0]]} then {fifth[pop[0]]}"
    return (f"each marked bird reads the same value in both years while the population mean "
            f"moves {first[pop[0]]} to {fifth[pop[0]]} millimetres")


def q18(table, item):
    n = dict(zip(cg.labels(table), cg.col(table, COUNT)))
    top = max(n, key=n.get)
    assert top.startswith("Altered their behaviour"), \
        f"altering behaviour must be the largest outcome; got {top}"
    assert list(n.values()).count(n[top]) == 1, "'the three were equally common' must be false"
    assert min(n.values()) > 0, "'none of the three was recorded' must be false"
    return f"the three outcomes number {n}, and the largest is {top}"


def q19(table, item):
    n = dict(zip(cg.labels(table), cg.col(table, COUNT)))
    died = [v for k, v in n.items() if k == "Perished"][0]
    total = sum(n.values())
    share = died / total
    assert abs(share - 1 / 3) < 0.03, f"about a third must have perished; got {share}"
    assert abs(share - 0.5) > 0.1 and abs(share - 0.1) > 0.1, \
        "'about a half' and 'about a tenth' must both be false"
    return (f"{died:.0f} of the {total:.0f} individuals followed perished, a share of "
            f"{share:.2f}")


def q20(table, item):
    yrs = cg.col(table, YEARS)
    rise = cg.col(table, RISE)
    assert len(yrs) == 2, f"two changes must be tabulated; got {len(yrs)}"
    assert abs(rise[0] - rise[1]) < 1e-9, f"the two rises must be equal; got {rise}"
    assert max(yrs) / min(yrs) >= 100, \
        f"one change must be far quicker than the other; got {yrs}"
    return (f"both changes raise the mean by {rise[0]:.0f} degrees Celsius, one over "
            f"{min(yrs):.0f} year and the other over {max(yrs):.0f}")


def q21(table, item):
    diff = cg.cell(table, "Generation 10", SURVIVE) - cg.cell(table, "Generation 1", SURVIVE)
    assert diff == 64, f"the rise must be 64 percentage points; got {diff}"
    assert diff != cg.cell(table, "Generation 10", SURVIVE), \
        "the difference must not coincide with the later reading"
    return (f"survival runs {cg.cell(table, 'Generation 1', SURVIVE):.0f} to "
            f"{cg.cell(table, 'Generation 10', SURVIVE):.0f} percent, a rise of {diff:.0f} points")


def q22(table, item):
    labs = cg.labels(table)
    pct = cg.col(table, SURVIVE)
    above = [lab for lab, v in zip(labs, pct) if v > 50]
    assert above, "'no tested generation exceeded one half' must be false"
    assert above[0] == "Generation 10", \
        f"the first generation above one half must be Generation 10; got {above[0]}"
    return (f"the survival figures are {pct} percent and the first above 50 is the one "
            f"recorded at {above[0]}")


def q23(table, item):
    labs = cg.labels(table)
    died = dict(zip(labs, cg.col(table, PERISHED)))
    worst = max(died, key=died.get)
    assert worst == "Population 2", f"Population 2 must lose the largest share; got {worst}"
    assert list(died.values()).count(died[worst]) == 1, \
        "'all three lost the same share' must be false"
    assert min(died.values()) > 0, "'none lost any individuals' must be false"
    return (f"the shares that perished are {died} percent, and the largest belongs to {worst}")


def q24(table, item):
    labs = cg.labels(table)
    triples = {lab: (m, a, p) for lab, m, a, p in
               zip(labs, cg.col(table, MOVED), cg.col(table, ALTERED),
                   cg.col(table, PERISHED))}
    for lab, t in triples.items():
        assert all(v > 0 for v in t), f"{lab} must record all three responses; got {t}"
        assert abs(sum(t) - 100) < 1e-9, f"{lab}'s three shares must total 100; got {t}"
    assert len(set(triples.values())) == len(triples), \
        "'every population divided its individuals equally' must be false"
    return (f"every row records a non-zero share for each of the three responses and totals "
            f"100 percent, and the three rows differ: {triples}")


CLAIMS = [
 ("Heritable traits",
  "ERT-2.H.1 states that natural selection acts on heritable traits. Heritable is the framework's own restriction on which traits are involved."),
 ("Populations to adapt to their environment over generations",
  "ERT-2.H.1 states that natural selection causes POPULATIONS to adapt to their environment OVER GENERATIONS. Both the level and the timescale are the statement's own words."),
 ("Incremental changes at the genetic level",
  "ERT-2.H.1 states that populations adapt over generations via incremental changes at the genetic level. Incremental and genetic are both the framework's words."),
 ("The population, across generations",
  "ERT-2.H.1 names the population as what adapts and generations as the interval, so an individual within one lifetime is neither the unit nor the timescale the statement gives."),
 ("restricts natural selection to heritable traits",
  "ERT-2.H.1 acts on HERITABLE traits, so a trait that is not passed on falls outside the statement. The rejected options remove that restriction or replace it with one the framework does not state."),
 ("may threaten the species' survival",
  "ERT-2.H.2 states that environmental changes may threaten a species' survival. The word may makes the threat possible rather than certain, and no other outcome is asserted."),
 ("Alter their behaviours, move, or perish",
  "ERT-2.H.2, near verbatim: environmental changes may threaten a species' survival, requiring individuals to alter behaviors, move, or perish. Each rejected set drops one of the three or adds something the statement does not name."),
 ("Both sudden and gradual change",
  "ERT-2.H.2 opens with environmental changes, either sudden or gradual, so both paces are inside the statement and neither is singled out."),
 ("possible outcome rather than a certain one",
  "ERT-2.H.2 is written with may, which asserts possibility rather than necessity, so a species that came through a change unharmed does not contradict it."),
 ("Across generations, rather than within a single lifetime",
  "ERT-2.H.1 places the adaptation of a population OVER GENERATIONS, an interval longer than one individual's life, and it does state an interval."),
 ("rose in the population step by step",
  "Recomputed in q11 above: the dark form rises at every generation scored, from below 5 percent to above 50, without a jump. ERT-2.H.1 describes adaptation as incremental changes at the genetic level over generations."),
 ("Eighty-nine points",
  "Recomputed in q12 above: 91 percent less 2 percent is 89 percentage points, which is neither of the two endpoints. The rejected values are the endpoints or differences between other pairs of rows."),
 ("more heritable changed more over the generations",
  "Recomputed in q13 above: sorted by the heritable share of their variation the four traits' changes are strictly increasing. ERT-2.H.1 states that natural selection acts on heritable traits, which is the property this record varies."),
 ("Trait 4",
  "Recomputed in q14 above: the smallest change belongs to the trait whose variation is least heritable, and it is unique. ERT-2.H.1 makes heritable variation what natural selection acts on."),
 ("shifted a little at each measurement",
  "Recomputed in q15 above: the mean rises at every measurement in steps small beside the mean itself, and it neither doubles nor moves only at the end. ERT-2.H.1 describes adaptation as INCREMENTAL change over generations."),
 ("1.7 millimetres",
  "Recomputed in q16 above: 10.9 less 9.2 millimetres is 1.7, which is neither endpoint nor a single step. The rejected values are those other quantities."),
 ("kept the beak depth it started with while the population mean shifted",
  "Recomputed in q17 above: each marked bird reads the same value in both years while the population mean moves. ERT-2.H.1 makes the POPULATION the thing that adapts, over generations, rather than the individual within its own life."),
 ("Altering their behaviour and feeding on other prey",
  "Recomputed in q18 above: the three counts are 410, 260 and 330 and the largest is unique. ERT-2.H.2 names altering behaviours, moving and perishing as the three things individuals may be required to do."),
 ("About one third",
  "Recomputed in q19 above: 330 of 1,000 individuals perished. Perishing is one of the three outcomes ERT-2.H.2 names, and the share is arithmetic on the table."),
 ("same size arrived suddenly in one case and gradually in the other",
  "Recomputed in q20 above: both changes raise the mean by the same amount, one over a single year and one over three hundred. ERT-2.H.2 covers environmental changes that are either sudden or gradual."),
 ("Sixty-four points",
  "Recomputed in q21 above: 68 percent less 4 percent is 64 percentage points. ERT-2.H.1 places such a change across generations rather than within one individual's life."),
 ("The tenth generation tested",
  "Recomputed in q22 above: the survival figures are 4, 12, 35, 68 and 92 percent and the first above 50 is the fourth entry. The reading is a search along one column in the order tested."),
 ("Population 2",
  "Recomputed in q23 above: the largest share perishing is 80 percent and it is unique. ERT-2.H.2 names perishing as one of the three things a threatened individual may be required to do."),
 ("All three of the framework's responses occurred in every population",
  "Recomputed in q24 above: every row records a non-zero share for moving, for altering feeding behaviour and for perishing, the three shares total 100 percent, and the three rows differ from one another. ERT-2.H.2 names exactly those three responses."),
 ("variation is passed to offspring, and the population mean shifts",
  "ERT-2.H.1 requires heritable traits, a population and a change over generations. Each rejected set is missing the heritability, the variation, or the generational shift."),
 ("alter their behaviour, some move, and some perish",
  "ERT-2.H.2 states that environmental change may require individuals to alter behaviors, move, or perish. Each rejected set swaps one of the three for something the statement does not name, and one attributes a genetic change to an individual, which ERT-2.H.1 places in the population across generations."),
 ("alters its own genes in response to the environment",
  "ERT-2.H.1 places the genetic change in the population and spreads it over generations, and ERT-2.H.2 gives individuals three responses of which changing their own genes is not one. The four rejected options are the statements' own words."),
 ("so that a change in it is a change at the genetic level",
  "ERT-2.H.1 acts on HERITABLE traits and locates the changes AT THE GENETIC LEVEL, so the trait it is about is one carried from parents to offspring. A learned skill, an injury and a difference in feeding are not carried that way, and a trait with no variation offers nothing to select between."),
 ("any adaptation appears in the population over generations",
  "ERT-2.H.2 supplies the possible threat and the three individual responses, and ERT-2.H.1 supplies adaptation of the population over generations by incremental genetic change. Each rejected account hardens may into certainty, moves the genetic change into the individual, replaces incremental with a jump, or promises that adaptation will succeed."),
 ("incremental genetic change, while environmental change, sudden or gradual",
  "ERT-2.H.1 supplies heritable traits, the population, the generations and the incremental genetic change; ERT-2.H.2 supplies the two paces of change, the possible threat and the three responses. Each rejected summary moves adaptation into the individual or the ecosystem, replaces incremental with a jump, narrows the pace, or drops two of the three responses."),
]

TABLE_CHECKS = {11: q11, 12: q12, 13: q13, 14: q14, 15: q15, 16: q16, 17: q17,
                18: q18, 19: q19, 20: q20, 21: q21, 22: q22, 23: q23, 24: q24}

if "--selftest" in sys.argv:
    print("note: e_check.run negative-controls every gate on every run; "
          "--selftest is the same run, not a separate one.")

e_check.run(e2_6, CLAIMS, TABLE_CHECKS)
