"""Key audit for AP BIOLOGY 8.3 Population Ecology.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor, so an off-by-one key stops matching; the
claim states what the key rests on, for a human to audit.

WHAT THE KEYS REST ON
---------------------
The conceptual items are keyed to EK 8.3.A.1 (a population is individuals of
one species interacting with one another and the environment), EK 8.3.A.2 (many
adaptations concern obtaining and using energy and matter; growth dynamics
depend on birth rate, death rate and population size; reproduction WITHOUT
CONSTRAINTS gives exponential growth) and to the two equations the CED prints
for this topic, dN/dt = B minus D and dN/dt = rmax times N, with the CED's own
definitions of dN, dt, B, D, N and rmax. The graphing items are keyed to
suggested skill 4.A.

THE ARITHMETIC IS THE PART A MACHINE CAN SETTLE, and all of it is settled here:

  * ``STEM_MATH`` recomputes items 13 to 16 by PARSING THE NUMBERS OUT OF THE
    STEM, so editing a stem without editing its key fails the check.
  * ``TABLE_CHECKS`` recomputes items 17 to 25 from their table alone, through
    cg_check's header-and-label accessors, locating any row a stem names by
    parsing the stem rather than by trusting a row index.

NO GRAPH IS REFERRED TO ANYWHERE. The suggested skill is graph construction and
the bank cannot show a figure, so the style pass below bars any phrase
promising one, and the growth data live in a table instead.

NEGATIVE CONTROL. Moving any key, changing any table cell the keys depend on,
or changing the first number in any stem the checks read makes this file raise;
confirmed by running exactly that.
"""
import re

import cg_check as cg
import b8_3

QS = b8_3.QUESTIONS
T_BD = b8_3._T_BD
T_EXP = b8_3._T_EXP

BIRTHS = "Births recorded in one year"
DEATHS = "Deaths recorded in one year"
COUNT = "Number of individuals counted"

# No \b anywhere: a digit and a letter are both word characters, so \b is
# silently not a boundary next to either. Explicit lookarounds instead.
_NUM_IN_STEM = re.compile(r"(?<![A-Za-z0-9.])(\d+(?:\.\d+)?)(?![0-9]|\.\d)")


def stem_nums(item):
    return [float(x) for x in _NUM_IN_STEM.findall(item["q"])]


def keyed(item):
    return item["choices"][item["ans"]]


def named_rows(table, item):
    return [lab for lab in cg.labels(table) if cg.contains_phrase(item["q"], lab)]


def _whole(x):
    assert abs(x - round(x)) < 1e-9, f"{x} must be whole for a calculator-free item"
    return int(round(x))


# --------------------------------------------------------- stem arithmetic

def m13(item):
    births, deaths = stem_nums(item)
    change = births - deaths
    assert keyed(item) == f"{_whole(change)} individuals", \
        f"q13 key {keyed(item)!r} but {births} minus {deaths} is {change}"
    return f"births {int(births)} minus deaths {int(deaths)} gives a change of {_whole(change)}"


def m14(item):
    n, r = stem_nums(item)
    added = r * n
    assert keyed(item) == f"{_whole(added)} individuals", \
        f"q14 key {keyed(item)!r} but {r} times {n} is {added}"
    return f"rmax {r} times N {int(n)} gives {_whole(added)} individuals added in the year"


def m15(item):
    n, change = stem_nums(item)
    rate = change / n
    assert keyed(item) == f"{rate:.2f} per individual per year", \
        f"q15 key {keyed(item)!r} but {change} divided by {n} is {rate}"
    return f"a change of {int(change)} over a population of {int(n)} is {rate:.2f} per individual"


def m16(item):
    n, r = stem_nums(item)
    added = r * n
    assert keyed(item) == f"{_whole(added)} individuals", \
        f"q16 key {keyed(item)!r} but {r} times {n} is {added}"
    return f"rmax {r} times N {int(n)} gives {_whole(added)} individuals added in the year"


STEM_MATH = {13: m13, 14: m14, 15: m15, 16: m16}


# -------------------------------------------------------- table arithmetic

def _labels_numbered(table, word):
    letters = [str(lab).split()[-1] for lab in cg.labels(table)]
    assert len(set(letters)) == len(letters), \
        f"{word} labels must be distinct; they read {cg.labels(table)}"


def _change(table, lab):
    return cg.cell(table, lab, BIRTHS) - cg.cell(table, lab, DEATHS)


def q17(table, item):
    _labels_numbered(table, "population")
    named = named_rows(table, item)
    assert len(named) == 1, f"the stem names rows {named}; it must name exactly one"
    change = _change(table, named[0])
    assert change > 0, f"the key states an increase; {named[0]} changes by {change}"
    assert keyed(item) == f"An increase of {_whole(change)} individuals", \
        f"q17 key {keyed(item)!r} but {named[0]} changes by {change}"
    return f"{named[0]} records {int(cg.cell(table, named[0], BIRTHS))} births against {int(cg.cell(table, named[0], DEATHS))} deaths, a change of {_whole(change)}"


def q18(table, item):
    _labels_numbered(table, "population")
    flat = [lab for lab in cg.labels(table) if _change(table, lab) == 0]
    assert len(flat) == 1, f"exactly one population must be unchanged; {flat} are"
    assert cg.contains_phrase(keyed(item), flat[0]), \
        f"q18 key {keyed(item)!r} but the unchanged population is {flat[0]}"
    changes = {lab: _change(table, lab) for lab in cg.labels(table)}
    return f"changes are {changes} and only {flat[0]} comes to zero"


def q19(table, item):
    _labels_numbered(table, "population")
    falling = [lab for lab in cg.labels(table) if _change(table, lab) < 0]
    assert len(falling) == 1, f"exactly one population must decline; {falling} do"
    assert cg.contains_phrase(keyed(item), falling[0]), \
        f"q19 key {keyed(item)!r} but the declining population is {falling[0]}"
    return f"only {falling[0]} records more deaths than births, a change of {_change(table, falling[0])}"


def q20(table, item):
    _labels_numbered(table, "population")
    changes = {lab: _change(table, lab) for lab in cg.labels(table)}
    best = max(changes, key=changes.get)
    assert sorted(changes.values())[-2] < changes[best], \
        f"the largest growth must be unique; the changes are {changes}"
    assert cg.contains_phrase(keyed(item), best), \
        f"q20 key {keyed(item)!r} but the largest growth belongs to {best}"
    most_births = max(cg.labels(table), key=lambda l: cg.cell(table, l, BIRTHS))
    assert most_births != best, \
        "the item is designed so the row with the most births is NOT the fastest grower"
    return f"changes are {changes}; the largest is {best}, while {most_births} records the most births"


def q21(table, item):
    _labels_numbered(table, "population")
    named = named_rows(table, item)
    assert len(named) == 2, f"the stem must name exactly two rows; it names {named}"
    a, b = (_change(table, lab) for lab in named)
    gap = a - b
    assert gap > 0, f"the stem asks by how much the first exceeds the second; the gap is {gap}"
    assert keyed(item) == f"{_whole(gap)} individuals", \
        f"q21 key {keyed(item)!r} but the changes are {a} and {b}"
    return f"{named[0]} changes by {_whole(a)} and {named[1]} by {_whole(b)}, a difference of {_whole(gap)}"


def _years_numbered(table):
    """Year labels must read Year 1 upward in written order: the increments and
    ratios below are read down the column as if it were chronological, and one
    item names two years outright."""
    nums = [cg.num(lab) for lab in cg.labels(table)]
    assert nums == list(range(1, len(nums) + 1)), \
        f"year labels are {cg.labels(table)}; they must be numbered from one in row order"


def q22(table, item):
    _years_numbered(table)
    counts = cg.col(table, COUNT)
    ratios = [b / a for a, b in zip(counts, counts[1:])]
    assert len({round(r, 9) for r in ratios}) == 1, \
        f"a constant multiplying factor is required for this key; the ratios are {ratios}"
    assert abs(ratios[0] - 2.0) < 1e-9, \
        f"the key says the count doubles; the constant factor is {ratios[0]}"
    increments = [b - a for a, b in zip(counts, counts[1:])]
    assert len(set(increments)) > 1, \
        "the nearest distractor claims a constant increase; the increments must not be constant"
    return f"the counts {counts} multiply by {ratios[0]:.0f} at every step while the increments {increments} differ"


def q23(table, item):
    _years_numbered(table)
    named = named_rows(table, item)
    assert len(named) == 2, f"the stem must name exactly two rows; it names {named}"
    a, b = (cg.cell(table, lab, COUNT) for lab in named)
    rise = b - a
    assert rise > 0, f"the stem asks for an increase; the counts are {a} then {b}"
    assert keyed(item) == f"{_whole(rise)} individuals", \
        f"q23 key {keyed(item)!r} but {named[0]} reads {a} and {named[1]} reads {b}"
    return f"{named[0]} reads {int(a)} and {named[1]} reads {int(b)}, an increase of {_whole(rise)}"


def q24(table, item):
    _years_numbered(table)
    counts = cg.col(table, COUNT)
    ratios = [b / a for a, b in zip(counts, counts[1:])]
    increments = [b - a for a, b in zip(counts, counts[1:])]
    assert len({round(r, 9) for r in ratios}) == 1, \
        f"the key rests on a constant multiplying factor; the ratios are {ratios}"
    assert all(y > x for x, y in zip(increments, increments[1:])), \
        f"the key rests on a growing yearly increase; the increments are {increments}"
    return (f"the ratio is a constant {ratios[0]:.0f} while the yearly increments {increments} rise, "
            "so a fixed per capita rate applied to a larger population adds more")


def q25(table, item):
    _years_numbered(table)
    counts = cg.col(table, COUNT)
    ratios = [b / a for a, b in zip(counts, counts[1:])]
    assert len({round(r, 9) for r in ratios}) == 1 and ratios[0] > 1, \
        f"exponential growth requires a constant factor above one; the ratios are {ratios}"
    increments = [b - a for a, b in zip(counts, counts[1:])]
    assert len(set(increments)) > 1, \
        "a distractor claims growth by a constant number per year; the increments must refute it"
    assert counts[-1] > counts[0], "a distractor claims decline; the counts must refute it"
    return f"the counts {counts} rise by a constant factor of {ratios[0]:.0f}, not by a constant amount"


TABLE_CHECKS = {17: q17, 18: q18, 19: q19, 20: q20, 21: q21,
                22: q22, 23: q23, 24: q24, 25: q25}


CLAIMS = [
 ("Individual organisms of the same species",
  "EK 8.3.A.1 states that populations comprise individual organisms of the same species that interact with one another and with the environment in complex ways. Organisms of many species in one place are a community, a separate level in EK 8.2.B.1."),
 ("Obtaining and using energy and matter in a particular environment",
  "EK 8.3.A.2 states that many adaptations in organisms are related to obtaining and using energy and matter in a particular environment, which is what links the adaptations of individuals to the dynamics of their population."),
 ("Birth rate, death rate, and population size",
  "EK 8.3.A.2 states that population growth dynamics depend on birth rate, death rate, and population size. All three appear in the two equations the CED prints for this topic."),
 ("change in population size per unit of time",
  "The CED defines dN as the change in population size and dt as the change in time, so their quotient is the change in population size per unit time. N alone is the population size and rmax the maximum per capita growth rate."),
 ("The birth rate and the death rate",
  "The CED defines B as the birth rate and D as the death rate in the equation dN/dt = B minus D. Population size is N and the maximum per capita growth rate is rmax, both defined in the other printed equation."),
 ("is positive, so the population is growing",
  "The CED prints dN/dt = B minus D, so a birth rate exceeding a death rate makes that difference positive, and a positive change in population size per unit time is growth."),
 ("is zero, so its size is not changing",
  "The CED prints dN/dt = B minus D, and equal rates make the difference zero. A zero change does not mean nothing is happening, only that births and deaths offset each other."),
 ("is negative, so the population is shrinking",
  "The CED prints dN/dt = B minus D, so a death rate exceeding a birth rate makes that difference negative, and a negative change in population size per unit time is a decline."),
 ("Exponential growth of the population",
  "EK 8.3.A.2 states that reproduction without constraints results in the exponential growth of a population, and prints dN/dt = rmax times N for that case."),
 ("maximum per capita growth rate of the population",
  "The CED defines rmax as the maximum per capita growth rate of population. Per capita means per individual, which is why the equation multiplies it by N to give a total rate of change."),
 ("the same per capita rate is applied to more individuals",
  "The CED prints dN/dt = rmax times N, a product. Holding one factor fixed and raising the other raises the product, which is why exponential growth adds more individuals per unit time as the population grows."),
 ("measured for each individual, while the change per unit time counts the whole population",
  "The CED defines rmax as a per capita rate and dN as the change in population size, and its equation multiplies the first by N to obtain the second. Two populations can share a per capita rate and add very different numbers of individuals."),
 ("75 individuals",
  "The CED prints dN/dt = B minus D. Recomputed in the stem-math check above from the two counts the stem states; adding them instead is the error the largest distractor carries."),
 ("20 individuals",
  "The CED prints dN/dt = rmax times N for reproduction without constraints. Recomputed above from the population size and per capita rate the stem states."),
 ("0.15 per individual per year",
  "The CED's exponential equation makes the change in population size per unit time the product of the per capita rate and the population size, so dividing the change by the size recovers the rate. Recomputed above from the stem's two numbers."),
 ("10 individuals",
  "The CED prints dN/dt = rmax times N. Recomputed above: the per capita rate multiplied by the population size gives the number added over the year."),
 ("An increase of 75 individuals",
  "The CED prints dN/dt = B minus D. The table check above locates the row the stem names, recomputes births minus deaths, and confirms the sign matches the increase the key states."),
 ("Population B",
  "The CED prints dN/dt = B minus D, so equal counts give a change of zero. The table check above confirms exactly one row comes to zero; equal counts do not mean no births and no deaths occurred."),
 ("Population C",
  "The CED prints dN/dt = B minus D, so deaths exceeding births give a negative change. The table check above confirms exactly one row records more deaths than births."),
 ("Population A",
  "The CED prints dN/dt = B minus D, so the largest growth is the largest excess of births over deaths. The table check above confirms the maximum is unique AND that the row with the most births is a different row, which is what the item tests."),
 ("15 individuals",
  "Skill 5.A includes differences. The table check above recomputes each named row's change as births minus deaths and takes the difference between the two changes."),
 ("It doubles",
  "Skill 4.B calls for describing the trend. The table check above confirms the ratio between successive counts is the same at every step and equals two, and separately that the yearly increments are NOT constant, which is what the nearest distractor claims."),
 ("200 individuals",
  "Skill 4.B includes identifying specific data points and skill 5.A the arithmetic. The table check above locates the two rows the stem names and subtracts the earlier count from the later."),
 ("same per capita rate applied to a larger population adds more individuals",
  "The CED prints dN/dt = rmax times N. The table check above confirms the multiplying factor is constant, so the per capita rate is constant, while the yearly increments rise at every step; a rising increment under a fixed rate is exactly the product growing with N."),
 ("Exponential growth",
  "EK 8.3.A.2 states that reproduction without constraints results in exponential growth and prints dN/dt = rmax times N. The table check above confirms a constant multiplying factor above one and refutes both the constant-increase and the decline distractors from the same numbers."),
 ("A line graph, because the counts are made at successive times",
  "Skill 4.A asks for the type of graph appropriate for the data. Counts recorded at successive times form a series whose change between times is the point, and a line graph is the form that shows it."),
 ("Labels including appropriate units, with a scale chosen so the data fit",
  "Skill 4.A lists axis labeling including appropriate units and legend, and scaling, among the components a graph should include. A trend line is listed separately and only where appropriate, so it does not replace labelling."),
 ("during a period in which nothing is restraining reproduction",
  "EK 8.3.A.2 states that reproduction WITHOUT CONSTRAINTS results in exponential growth. The qualifying phrase is part of the statement, so the equation is offered for the unconstrained case rather than as a description of every population."),
 ("larger population adds more individuals per unit time",
  "The CED prints dN/dt = rmax times N. With rmax equal for both populations the change per unit time is proportional to N, so the larger population adds more individuals even though each individual contributes the same."),
 ("The first requires a birth rate and a death rate; the second requires a per capita rate and a population size",
  "The CED prints dN/dt = B minus D with B the birth rate and D the death rate, and dN/dt = rmax times N with rmax the maximum per capita growth rate and N the population size. One distractor exchanges the two sets of inputs."),
]


# SCIENCE_BRIEF.md: Biology is exported untypeset, so a backslash macro or a
# dollar span would reach a student as literal characters, and a
# digit-hyphen-digit run reads as a subtraction. Explicit lookarounds, never \b.
_BANNED = [
    (re.compile(r"\\"), "a backslash: this bank carries no LaTeX"),
    (re.compile(r"\$"), "a dollar-delimited math span"),
    (re.compile(r"(?<![A-Za-z])\d+\s*-\s*\d+(?![A-Za-z])"), "a digit-hyphen-digit range"),
    (re.compile(r"\d\s*/\s*\d"), "a digit-slash-digit fraction"),
]

# This topic's suggested skill is graph construction, which is exactly the
# temptation SCIENCE_BRIEF.md warns about: a stem that says "the growth curve
# shown" promises a figure the bank cannot display. Every such phrase is barred.
_FIGURE_TALK = re.compile(
    r"(?<![A-Za-z])(the (?:graph|curve|figure|diagram|chart|plot) (?:shown|above|below)|"
    r"in the (?:graph|curve|figure|diagram|chart|plot) (?:shown|above|below)|"
    r"shown in the (?:graph|curve|figure|diagram|chart|plot))(?![A-Za-z])",
    re.IGNORECASE)


def style():
    hits = 0
    for i, item in enumerate(QS, 1):
        texts = [("stem", item["q"]), ("why", item["why"])]
        texts += [(f"choice {k}", c) for k, c in enumerate(item["choices"])]
        if item.get("table"):
            texts.append(("table", " | ".join(item["table"]["headers"])))
            texts += [("table", " | ".join(str(c) for c in r)) for r in item["table"]["rows"]]
        for where, text in texts:
            for pat, why_bad in _BANNED:
                m = pat.search(text)
                assert not m, f"q{i} {where} contains {m.group(0)!r}, {why_bad}"
                hits += 1
            m = _FIGURE_TALK.search(text)
            assert not m, (
                f"q{i} {where} says {m.group(0)!r}, promising a figure the bank cannot show"
            )
            hits += 1
    return hits


def main():
    n_style = style()
    notes = []
    for i, fn in sorted(STEM_MATH.items()):
        item = QS[i - 1]
        assert "table" not in item, f"q{i} has a table; it belongs in TABLE_CHECKS"
        notes.append(f"  q{i:>2}: {fn(item)}")
    cg.check(b8_3, CLAIMS, table_checks=TABLE_CHECKS)
    print(f"    {n_style} notation and figure-reference checks clean.")
    print(f"    {len(STEM_MATH)} stem calculation(s) recomputed from the stem text:")
    print("\n".join(notes))


main()
