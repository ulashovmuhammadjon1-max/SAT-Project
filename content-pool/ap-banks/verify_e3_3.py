"""Key audit for AP ENVIRONMENTAL SCIENCE 3.3 Survivorship Curves.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor.

WHAT THE KEYS REST ON
---------------------
ERT-3.C.1  a survivorship curve is a line displaying the relative survival
           rates of a cohort -- a group of individuals of the same age -- in a
           population, from birth to the maximum age reached by any one cohort
           member; there are Type I, Type II, and Type III curves
                        -- items 1, 2, 3, 4, 5, 10, 11, 12, 15, 18, 19, 21,
                           22, 28, 29, 30
ERT-3.C.2  survivorship curves differ for K-selected and r-selected species,
           with K-selected species typically following a Type I or Type II
           curve and r-selected species following a Type III curve
                        -- items 6, 7, 8, 9, 25, 26, 30

THE CONSTRAINT THAT SHAPES THE WHOLE MODULE: THE FRAMEWORK NAMES THE THREE
TYPES AND DESCRIBES THE SHAPE OF NONE OF THEM. Nothing in the course says a
Type I curve means most of a cohort survives to old age or that a Type III
means heavy early loss. So NO ITEM READS A TYPE OFF A COHORT TABLE, and item 10
keys that absence outright.

WHERE A TYPE IS KEYED IT IS REACHED BY A NAMED CHAIN, never by a shape. Items
25 and 26 use ERT-3.B.2 (r-selected: many offspring, short life spans) and
ERT-3.B.1 (K-selected: few offspring, long life spans) to identify the profile
from a table that prints offspring number and maximum age, and then ERT-3.C.2
to assign the curve type. The claims name that chain.

EVERY OTHER DATA ITEM IS ARITHMETIC ON THE PRINTED COHORT -- a share, a
difference, a count at an age, the interval holding the largest loss.

NO FIGURES, AND THIS IS THE TOPIC MOST OFTEN TAUGHT FROM A PICTURE. Not one
stem refers to a curve being shown; the cohort data are in a table= and every
question is asked of the table. ``e_check.no_figure_reference`` enforces it.

DATA ITEMS: 13 to 27 carry tables, recomputed below by column header.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and EVERY data table in turn, and requires each
corruption to raise BEFORE the real gate runs. Two of these checks pick a
maximum that a column reversal happens to leave in place, so each of them also
asserts that the maximum is UNIQUE -- which is what fails when e_check goes on
to flatten the table. ``python3 verify_e3_3.py --selftest`` is the same run;
the controls are not behind the flag.
"""
import sys

import cg_check as cg
import e_check
import e3_3

AGE = "Age class (years)"
CA = "Survivors in cohort A"
CB = "Survivors in cohort B"
CC = "Survivors in cohort C"
MAXAGE = "Maximum age reached by any member (years)"
START = "Survivors at the start of the interval"
END = "Survivors at the end of the interval"
RAGE = "Age (years)"
ALIVE = "Individuals alive"
PCT = "Percent of the original cohort alive"
OFFSPRING = "Offspring produced per reproduction event"
TOPAGE = "Maximum age reached (years)"


def _cohorts(table):
    return {"Cohort A": cg.col(table, CA), "Cohort B": cg.col(table, CB),
            "Cohort C": cg.col(table, CC)}


def q13(table, item):
    coh = _cohorts(table)
    loss = {k: (v[0] - v[1]) / v[0] for k, v in coh.items()}
    worst = max(loss, key=loss.get)
    assert worst == "Cohort C", f"Cohort C must lose the largest first-year share; got {worst}"
    assert list(loss.values()).count(loss[worst]) == 1, \
        "'all three lost the same share' must be false"
    assert min(loss.values()) > 0, "'none of the three lost any members' must be false"
    return (f"the first-year losses are {({k: round(v, 3) for k, v in loss.items()})} of the "
            f"starting cohort, and the largest belongs to {worst}")


def q14(table, item):
    ages = cg.col(table, AGE)
    i = ages.index(8)
    coh = {k: v[i] for k, v in _cohorts(table).items()}
    top = max(coh, key=coh.get)
    assert top == "Cohort A", f"Cohort A must hold the most survivors at age eight; got {top}"
    assert list(coh.values()).count(coh[top]) == 1, \
        "the largest count at that age must be unique, so 'all three are equal' is false"
    assert min(coh.values()) > 0, "'none has any survivors left' must be false"
    return f"at the age class for eight years the three cohorts stand at {coh}"


def q15(table, item):
    ages = cg.col(table, AGE)
    a = cg.col(table, CA)
    share = a[ages.index(6)] / a[ages.index(0)]
    assert abs(share - 0.90) < 1e-9, f"the share must be 0.90; got {share}"
    return (f"the first cohort stands at {a[ages.index(6)]:.0f} of its original "
            f"{a[ages.index(0)]:.0f} at age six, a share of {share:.2f}")


def q16(table, item):
    ages = cg.col(table, AGE)
    c = cg.col(table, CC)
    v = c[ages.index(2)]
    assert v == 28, f"the third cohort must stand at 28 at age two; got {v}"
    assert v != c[ages.index(1)] and v != c[ages.index(4)], \
        "that count must not coincide with the neighbouring age classes"
    return f"the third cohort records {v:.0f} survivors in the age class for two years"


def q17(table, item):
    coh = _cohorts(table)
    steady = []
    for k, v in coh.items():
        ratios = [v[i + 1] / v[i] for i in range(len(v) - 1)]
        if all(0.65 <= r <= 0.75 for r in ratios):
            steady.append(k)
    assert steady == ["Cohort B"], \
        f"exactly Cohort B must fall by a near-constant proportion; got {steady}"
    return ("exactly one cohort's successive counts sit between sixty-five and seventy-five "
            "percent of the count before them at every step")


def q18(table, item):
    labs = cg.labels(table)
    top = dict(zip(labs, cg.col(table, MAXAGE)))
    furthest = max(top, key=top.get)
    assert furthest == "Cohort 1", f"Cohort 1 must reach the greatest age; got {furthest}"
    assert list(top.values()).count(top[furthest]) == 1, \
        "'all three extend equally far' must be false"
    return (f"the maximum ages reached are {top} years, and ERT-3.C.1 ends each curve at "
            f"that age, so the furthest belongs to {furthest}")


def q19(table, item):
    labs = cg.labels(table)
    top = dict(zip(labs, cg.col(table, MAXAGE)))
    shortest = min(top, key=top.get)
    assert shortest == "Cohort 2", f"Cohort 2 must reach the least age; got {shortest}"
    assert list(top.values()).count(top[shortest]) == 1, \
        "the smallest maximum age must be unique"
    return f"the maximum ages reached are {top} years, and the smallest belongs to {shortest}"


def q20(table, item):
    labs = cg.labels(table)
    lost = {lab: s - e for lab, s, e in
            zip(labs, cg.col(table, START), cg.col(table, END))}
    worst = max(lost, key=lost.get)
    assert worst == "Birth to one year", \
        f"the first interval must lose the most individuals; got {worst}"
    assert list(lost.values()).count(lost[worst]) == 1, \
        "'the four intervals lost equal numbers' must be false"
    return f"the four intervals lose {lost} individuals, and the largest loss is in {worst}"


def q21(table, item):
    s = cg.col(table, START)
    e = cg.col(table, END)
    share = (s[0] - e[0]) / s[0]
    assert abs(share - 0.59) < 1e-9, f"the share lost must be 0.59; got {share}"
    assert abs(share - (1 - share)) > 0.05, \
        "the share lost must be distinguishable from the share surviving"
    return (f"the cohort falls {s[0]:.0f} to {e[0]:.0f} over the first interval, a loss of "
            f"{share:.2f} of it")


def q22(table, item):
    alive = cg.col(table, ALIVE)
    pct = cg.col(table, PCT)
    for a, p in zip(alive, pct):
        assert abs(a / alive[0] * 100 - p) < 1e-9, \
            f"{a} of an original {alive[0]} is not {p} percent"
    ratios = [alive[i] / alive[i - 1] * 100 for i in range(1, len(alive))]
    assert any(abs(r - p) > 1e-9 for r, p in zip(ratios, pct[1:])), \
        "the percent column must not also be each count as a share of the one before it"
    return (f"every entry of the percent column equals its count divided by the original "
            f"{alive[0]:.0f}, and it is not the step to step ratio")


def q23(table, item):
    ages = cg.col(table, RAGE)
    pct = cg.col(table, PCT)
    half = [a for a, p in zip(ages, pct) if p <= 50]
    assert half, "'the cohort never fell to half its size' must be false"
    assert half[0] == 5, f"the cohort must reach half at age five; got {half[0]}"
    return (f"the share still alive reads {pct} percent at ages {ages}, and the first entry "
            f"at or below fifty is the one at age {half[0]:.0f}")


def _profile(table):
    """The row with more offspring and the shorter maximum age, and its opposite."""
    labs = cg.labels(table)
    off = dict(zip(labs, cg.col(table, OFFSPRING)))
    age = dict(zip(labs, cg.col(table, TOPAGE)))
    fecund = max(off, key=off.get)
    shortest = min(age, key=age.get)
    assert fecund == shortest, (
        f"one row must be both the more fecund and the shorter lived; got {fecund} and "
        f"{shortest}"
    )
    assert off[fecund] > 100 * min(off.values()), \
        f"the offspring counts must differ by orders of magnitude; got {off}"
    assert age[shortest] * 10 < max(age.values()), \
        f"the maximum ages must differ by an order of magnitude; got {age}"
    other = [lab for lab in labs if lab != fecund][0]
    return fecund, other, off, age


def q24(table, item):
    fecund, other, off, age = _profile(table)
    assert fecund == "Species N", \
        f"Species N must carry the many-offspring, short-lived profile; got {fecund}"
    return (f"{fecund} produces {off[fecund]:.0f} offspring per event and reaches "
            f"{age[fecund]:.0f} years, against {off[other]:.0f} and {age[other]:.0f} for the "
            "other species")


def q25(table, item):
    fecund, other, off, age = _profile(table)
    assert fecund == "Species N", \
        f"the r-selected profile must belong to Species N; got {fecund}"
    return (f"the many-offspring, short-lived row is {fecund}, which ERT-3.B.2 makes the "
            "r-selected profile and ERT-3.C.2 assigns a Type III curve")


def q26(table, item):
    fecund, other, off, age = _profile(table)
    assert other == "Species M", \
        f"the few-offspring, long-lived row must be Species M; got {other}"
    assert off[other] < off[fecund] and age[other] > age[fecund], \
        "that row must have fewer offspring and the longer maximum age"
    return (f"the few-offspring, long-lived row is {other} with {off[other]:.0f} offspring "
            f"and {age[other]:.0f} years, which ERT-3.B.1 makes the K-selected profile")


def q27(table, item):
    s = cg.col(table, START)
    e = cg.col(table, END)
    share = e[-1] / s[0]
    assert abs(share - 0.15) < 1e-9, f"the share still alive must be 0.15; got {share}"
    return (f"the cohort begins at {s[0]:.0f} and ends the last interval at {e[-1]:.0f}, a "
            f"share of {share:.2f}")


CLAIMS = [
 ("relative survival rates of a cohort in a population",
  "ERT-3.C.1, near verbatim: a survivorship curve is a line that displays the relative survival rates of a cohort in a population. It is about one cohort's survival, not population size, births, limits or averages."),
 ("A group of individuals of the same age",
  "ERT-3.C.1 defines a cohort in its own parenthesis as a group of individuals of the same age. Shared species, habitat and size are not the criterion."),
 ("maximum age reached by any one cohort member",
  "ERT-3.C.1 runs the curve from birth to the maximum age reached by any one cohort member, so the end of the axis is set by the longest lived member rather than by an average or a life stage."),
 ("Type I, Type II and Type III",
  "ERT-3.C.1 closes by stating that there are Type I, Type II, and Type III curves, which is three types with those names."),
 ("The Type IV curve",
  "ERT-3.C.1 names Type I, Type II and Type III. A fourth type is not among them."),
 ("Type I or Type II curves",
  "ERT-3.C.2 states that K-selected species typically follow a Type I or Type II curve, which is two types rather than one, and not the type it gives to r-selected species."),
 ("Type III curves",
  "ERT-3.C.2 states that r-selected species follow a Type III curve, which is not either of the two types it offers K-selected species."),
 # Both halves, because the distractor is the SWAP.
 ("Type I or Type II curve, and r-selected species follow a Type III",
  "ERT-3.C.2 states that survivorship curves differ for K-selected and r-selected species, with K-selected species typically following a Type I or Type II curve and r-selected species following a Type III curve."),
 ("usual for K-selected species rather than universal",
  "ERT-3.C.2 is written with TYPICALLY, which asserts what usually holds rather than a rule without exceptions, so a K-selected species whose curve is neither Type I nor Type II is not a contradiction."),
 ("names the three types without describing the shape",
  "ERT-3.C.1 states that there are Type I, Type II, and Type III curves and stops there, and ERT-3.C.2 attaches types to reproductive strategies without describing any shape. No shape, formula, count or age is given anywhere in the two statements. This is why no item in this module reads a type off a cohort table."),
 ("follows a cohort, which is a group of individuals of the same age",
  "ERT-3.C.1 makes the curve a display of the relative survival rates of a COHORT, defined as a group of individuals of the same age, so the measurement follows one such group rather than sampling every age at one moment."),
 ("Relative survival rates",
  "ERT-3.C.1 states that a survivorship curve displays the relative survival rates of a cohort. Births, biomass, species counts and habitat change are not what the line displays."),
 ("Cohort C",
  "Recomputed in q13 above: the three first-year losses are 1, 30 and 94 percent of the starting cohort, and the largest is unique. The comparison is arithmetic on two rows of each column."),
 ("Cohort A",
  "Recomputed in q14 above: at the age class for eight years the three cohorts stand at 700, 168 and 2, and the largest is unique. The comparison is a direct reading of one row."),
 ("Ninety percent",
  "Recomputed in q15 above: 900 of an original 1,000 is 90 percent. ERT-3.C.1 makes the curve a display of RELATIVE survival rates, which is what a share of the original cohort is."),
 ("Twenty-eight",
  "Recomputed in q16 above: that cohort records 28 survivors in the age class for two years, and the value differs from its neighbours. The rejected values are its counts at other ages or another cohort's count."),
 ("Cohort B",
  "Recomputed in q17 above: exactly one cohort's successive counts sit between sixty-five and seventy-five percent of the count before them at every step. This is a set of divisions on the columns, not a claim about any curve's shape."),
 ("That of Cohort 1",
  "Recomputed in q18 above: the maximum ages reached are 62, 3 and 19 years and the largest is unique. ERT-3.C.1 ends a survivorship curve at the maximum age reached by any one cohort member."),
 ("That of Cohort 2",
  "Recomputed in q19 above: the smallest maximum age reached is 3 years and it is unique, so it sets the shortest axis under ERT-3.C.1's definition."),
 ("Birth to one year",
  "Recomputed in q20 above: the four intervals lose 590, 80, 50 and 130 individuals and the largest is unique. The comparison is a subtraction carried out row by row."),
 ("Fifty-nine percent",
  "Recomputed in q21 above: the cohort falls from 1,000 to 410, a loss of 590, which is 59 percent of it. ERT-3.C.1 makes relative survival the quantity of interest and a share lost is its complement."),
 ("each count expressed as a share of the original cohort",
  "Recomputed in q22 above: every percent equals its count divided by the 2,000 alive at age zero, and it is not the step to step ratio. ERT-3.C.1 makes a survivorship curve a display of RELATIVE survival rates, which is exactly this ratio."),
 ("By age five",
  "Recomputed in q23 above: the share still alive first reaches fifty percent at the third age recorded and is above half at every earlier one. The reading is a search along one column."),
 # Both clauses, because two distractors keep one half and swap the other.
 ("Species N, which has many offspring and the shorter maximum age",
  "NAMED CHAIN: ERT-3.B.2 gives r-selected species many offspring and short life spans, and q24 above recomputes that one row alone has both, by orders of magnitude. The rejected options attach the wrong traits to a species or the wrong species to the traits."),
 ("Type III",
  "NAMED CHAIN, recomputed in q25 above: the row with many offspring and the shorter maximum age is the r-selected profile of ERT-3.B.2, and ERT-3.C.2 states that r-selected species follow a Type III curve. The type is reached through those two statements, never from a shape the framework does not describe."),
 ("Type I or a Type II",
  "NAMED CHAIN, recomputed in q26 above: the other row has few offspring and the longer maximum age, which is the K-selected profile of ERT-3.B.1, and ERT-3.C.2 states that K-selected species typically follow a Type I or Type II curve. Two types are offered, not one."),
 ("Fifteen percent",
  "Recomputed in q27 above: 150 of an original 1,000 is 15 percent. The share is arithmetic on the first and last entries of the two columns."),
 ("Marking every chick hatched in one season",
  "ERT-3.C.1 defines the curve as a display of the relative survival rates of a cohort, a group of individuals of the same age, from birth onward, so only a group hatched together and followed through time is such a cohort."),
 ("relative survival of one cohort, not the size of the whole population",
  "ERT-3.C.1 makes the curve a display of the relative survival rates of a cohort from birth to the maximum age any member reaches. A population's total size includes individuals of every age and every birth year, which is not what the line follows."),
 ("K-selected species typically follow Type I or Type II while r-selected species follow Type III",
  "ERT-3.C.1 supplies the definition, the cohort, the span and the three type names, and ERT-3.C.2 the pairing with the two reproductive strategies. Each rejected summary changes what the line displays, changes the end of the span, adds a fourth type, reverses the pairing, denies it, or claims a description of the shapes the framework never gives."),
]

TABLE_CHECKS = {13: q13, 14: q14, 15: q15, 16: q16, 17: q17, 18: q18, 19: q19,
                20: q20, 21: q21, 22: q22, 23: q23, 24: q24, 25: q25, 26: q26,
                27: q27}

if "--selftest" in sys.argv:
    print("note: e_check.run negative-controls every gate on every run; "
          "--selftest is the same run, not a separate one.")

e_check.run(e3_3, CLAIMS, TABLE_CHECKS)
