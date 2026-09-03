"""Key audit for AP BIOLOGY 8.5 Community Ecology.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor, so an off-by-one key stops matching; the
claim states what the key rests on, for a human to audit.

WHAT THE KEYS REST ON
---------------------
The conceptual items are keyed to EK 8.5.A.1 (structure is composition and
diversity; the printed diversity index with its own definitions of n and N),
EK 8.5.B.1 (a community is interacting populations of different species that
change over time), EK 8.5.B.2 (interactions determine how populations access
energy and matter), EK 8.5.B.3 (relationships characterized by POSITIVE AND
NEGATIVE EFFECTS and modelable; predator and prey, cooperation, trophic
cascades, niche partitioning) and EK 8.5.B.4 (competition, predation, and the
three named symbioses drive population dynamics). The error-bar items are keyed
to suggested skill 5.B.

THE THREE SYMBIOSES ARE NAMED AND NOT DEFINED by the CED. So items 14 to 16
state the effect on each population in the stem and ask which named
relationship that pattern is: the key rests on EK 8.5.B.3's own characterization
by positive and negative effects together with the ordinary meaning of the term
the CED prints, and these claims say that outright rather than citing a
definition the framework does not carry.

THE ARITHMETIC. Every value of the diversity index that a key states is
RECOMPUTED below from the counts in the table alone, using the printed formula.
All three communities hold ten individuals, and the check asserts that before
accepting any index, so every square is exact and the item is calculator-free.
The error-bar items are recomputed from the two interval columns.

NEGATIVE CONTROL. Moving any key, or changing any table cell the keys depend
on, makes this file raise; confirmed by running exactly that.
"""
import re

import cg_check as cg
import b8_5

QS = b8_5.QUESTIONS
T_COMM = b8_5._T_COMM
T_ERROR = b8_5._T_ERROR

MEAN = "Mean number of species recorded per plot"
LOW = "Lower end of the error bar"
HIGH = "Upper end of the error bar"

NUMBER_WORDS = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
                "Eight", "Nine", "Ten"]


def keyed(item):
    return item["choices"][item["ans"]]


def counts(table, lab):
    """The species counts for one community row, in column order."""
    j0 = 1
    row = [cg.num(c) for c in table["rows"][
        [cg.normalize(x) for x in cg.labels(table)].index(cg.normalize(lab))][j0:]]
    return row


def simpson(table, lab):
    c = counts(table, lab)
    total = sum(c)
    assert total > 0, f"{lab} holds no individuals"
    return 1 - sum((x / total) ** 2 for x in c), total


def _same_total(table):
    totals = {lab: sum(counts(table, lab)) for lab in cg.labels(table)}
    assert len(set(totals.values())) == 1, (
        f"every community must hold the same number of individuals for these items to be "
        f"calculator-free and comparable; totals are {totals}"
    )
    return list(totals.values())[0]


def richness(table, lab):
    return sum(1 for x in counts(table, lab) if x > 0)


def q19(table, item):
    _same_total(table)
    named = [lab for lab in cg.labels(table) if cg.contains_phrase(item["q"], lab)]
    assert len(named) == 1, f"the stem names rows {named}; it must name exactly one"
    value, total = simpson(table, named[0])
    assert keyed(item) == f"{value:.2f}", \
        f"q19 key {keyed(item)!r} but the index for {named[0]} is {value}"
    assert abs(value - round(value, 2)) < 1e-9, "the index must be exact to two decimals here"
    return f"{named[0]} holds {counts(table, named[0])} of {int(total)}, giving an index of {value:.2f}"


def q20(table, item):
    _same_total(table)
    idx = {lab: simpson(table, lab)[0] for lab in cg.labels(table)}
    best = max(idx, key=idx.get)
    assert sorted(idx.values())[-2] < idx[best] - 1e-12, \
        f"the largest index must be unique; the values are {idx}"
    assert cg.contains_phrase(keyed(item), best), \
        f"q20 key {keyed(item)!r} but the largest index belongs to {best}"
    shown = {k: round(v, 3) for k, v in idx.items()}
    return f"indices are {shown} and the maximum is {best}"


def q21(table, item):
    named = [lab for lab in cg.labels(table) if cg.contains_phrase(item["q"], lab)]
    assert len(named) == 1, f"the stem names rows {named}; it must name exactly one"
    r = richness(table, named[0])
    assert keyed(item) == NUMBER_WORDS[r], \
        f"q21 key {keyed(item)!r} but {named[0]} records {r} species"
    assert r != sum(counts(table, named[0])), \
        "richness must differ from the number of individuals, or the item tests nothing"
    return f"{named[0]} records {counts(table, named[0])}, which is {r} species among {int(sum(counts(table, named[0])))} individuals"


def q22(table, item):
    _same_total(table)
    labs = cg.labels(table)
    pairs = [(a, b) for i, a in enumerate(labs) for b in labs[i + 1:]
             if richness(table, a) == richness(table, b)
             and abs(simpson(table, a)[0] - simpson(table, b)[0]) > 1e-9]
    assert pairs, "the key requires two rows with equal richness and unequal index; none exist"
    a, b = pairs[0]
    assert counts(table, a) != counts(table, b), \
        "the key attributes the difference to how individuals are distributed; the counts must differ"
    return (f"{a} and {b} both record {richness(table, a)} species out of the same total, "
            f"with counts {counts(table, a)} against {counts(table, b)} and indices "
            f"{simpson(table, a)[0]:.2f} against {simpson(table, b)[0]:.2f}")


def q23(table, item):
    total = _same_total(table)
    idx = {lab: simpson(table, lab)[0] for lab in cg.labels(table)}
    worst = min(idx, key=idx.get)
    assert sorted(idx.values())[1] > idx[worst] + 1e-12, \
        f"the smallest index must be unique; the values are {idx}"
    assert cg.contains_phrase(keyed(item), worst), \
        f"q23 key {keyed(item)!r} but the smallest index belongs to {worst}"
    c = counts(table, worst)
    assert max(c) > total / 2, \
        f"the key says one species holds most of the individuals; {worst} records {c}"
    return f"{worst} has the smallest index and one species holding {int(max(c))} of {int(total)} individuals"


def _sites_numbered(table):
    nums = [cg.num(lab) for lab in cg.labels(table)]
    assert nums == list(range(1, len(nums) + 1)), \
        f"site labels are {cg.labels(table)}; they must be numbered from one in row order"


def _intervals(table):
    out = {}
    for lab in cg.labels(table):
        lo, hi, m = (cg.cell(table, lab, h) for h in (LOW, HIGH, MEAN))
        assert lo < m < hi, f"{lab}: the mean {m} must lie inside its error bar {lo} to {hi}"
        out[lab] = (lo, hi, m)
    return out


def _overlaps(a, b):
    return a[0] <= b[1] and b[0] <= a[1]


def q24(table, item):
    _sites_numbered(table)
    iv = _intervals(table)
    labs = list(iv)
    pairs = [(a, b) for i, a in enumerate(labs) for b in labs[i + 1:] if _overlaps(iv[a], iv[b])]
    assert len(pairs) == 1, f"exactly one overlapping pair is required for this key; found {pairs}"
    for lab in pairs[0]:
        assert cg.contains_phrase(keyed(item), lab), \
            f"q24 key {keyed(item)!r} does not name {lab}, which is in the overlapping pair"
    for lab in labs:
        if lab not in pairs[0]:
            assert not cg.contains_phrase(keyed(item), lab), \
                f"q24 key {keyed(item)!r} also names {lab}, which is not in the overlapping pair"
    return f"intervals are {iv}; the only overlapping pair is {pairs[0]}"


def q25(table, item):
    iv = _intervals(table)
    labs = list(iv)
    pairs = [(a, b) for i, a in enumerate(labs) for b in labs[i + 1:] if _overlaps(iv[a], iv[b])]
    assert len(pairs) == 1, f"the key concerns one overlapping pair; found {pairs}"
    a, b = pairs[0]
    assert iv[a][2] != iv[b][2], \
        "the overlapping pair must have different means, or the item is not about a failure to distinguish them"
    return f"{a} and {b} have different means, {iv[a][2]} and {iv[b][2]}, but overlapping intervals"


def q26(table, item):
    _sites_numbered(table)
    iv = _intervals(table)
    named = [lab for lab in cg.labels(table) if cg.contains_phrase(item["q"], lab)]
    assert len(named) == 1, f"the stem names sites {named}; it must name exactly one"
    apart = [lab for lab in iv if lab != named[0] and not _overlaps(iv[lab], iv[named[0]])]
    assert len(apart) == 1, f"exactly one other site must fail to overlap {named[0]}; {apart} do"
    assert cg.contains_phrase(keyed(item), apart[0]), \
        f"q26 key {keyed(item)!r} but the non-overlapping site is {apart[0]}"
    return f"only {apart[0]} has an interval that does not overlap the interval around {named[0]}"


def q27(table, item):
    _sites_numbered(table)
    iv = _intervals(table)
    named = [lab for lab in cg.labels(table) if cg.contains_phrase(item["q"], lab)]
    assert len(named) == 2, f"the stem must name exactly two sites; it names {named}"
    a, b = named
    assert not _overlaps(iv[a], iv[b]), \
        f"the key treats the difference as supported, so {a} and {b} must not overlap: {iv[a]}, {iv[b]}"
    gap = abs(iv[a][2] - iv[b][2])
    assert abs(gap - round(gap)) < 1e-9, "the difference must be whole for a calculator-free item"
    assert keyed(item) == f"{int(round(gap))} species per plot", \
        f"q27 key {keyed(item)!r} but the means of {a} and {b} differ by {gap}"
    return f"{a} and {b} have non-overlapping intervals and means differing by {int(round(gap))}"


TABLE_CHECKS = {19: q19, 20: q20, 21: q21, 22: q22, 23: q23,
                24: q24, 25: q25, 26: q26, 27: q27}


CLAIMS = [
 ("Species composition and species diversity",
  "EK 8.5.A.1 states that the structure of a community is measured and described in terms of species composition and species diversity. Total mass, habitat age and reproductive rate appear nowhere in that statement."),
 ("total number of organisms of a particular species",
  "The CED defines n as the total number of organisms of a particular species and N as the total number of organisms of all species, in the diversity index printed for this topic. Exchanging the two is the error the nearest distractor represents."),
 ("total number of organisms of all species",
  "The CED defines N as the total number of organisms of all species in the printed index. It is the denominator each species count is divided by before squaring."),
 ("spread evenly among the species",
  "The printed index subtracts the sum of squared shares from one. Concentrating individuals into one species makes one share large, and squaring a large share contributes far more to that sum than squaring several small ones, so the subtracted quantity is larger and the index smaller. Confirmed numerically against this module's own table in q22 and q23 below."),
 ("interacting populations of different species that change over time",
  "EK 8.5.B.1 states that communities are groups of interacting populations of different species that change over time based on the interactions between those populations. A group of individuals of one species is a population under EK 8.3.A.1."),
 ("How those populations access energy and matter",
  "EK 8.5.B.2 states that interactions among populations determine how they access energy and matter within a community, which is the link between community structure and the energy flow of EK 8.2."),
 ("By their positive and negative effects, and they can be modeled",
  "EK 8.5.B.3 states that relationships among interacting populations can be characterized by positive and negative effects and can be modeled. Both halves of that sentence are asserted together."),
 ("Niche partitioning",
  "EK 8.5.B.3 lists predator and prey interactions, cooperation, trophic cascades and niche partitioning as its examples. Photosynthesis and nitrogen fixation belong to EK 8.2's cycles and the remaining distractors to Unit 7."),
 ("A predator and prey interaction",
  "EK 8.5.B.3 lists predator and prey interactions among its examples of relationships among interacting populations. One population consuming another, with linked changes in numbers over time, is that relationship."),
 ("Cooperation",
  "EK 8.5.B.3 lists cooperation among its examples. The effect on both populations is positive, which is how EK 8.5.B.3 says such relationships are characterized."),
 ("A trophic cascade",
  "EK 8.5.B.3 lists trophic cascades among its examples. A change at one level passing down through the levels below it is what the term names, and the scenario describes exactly that sequence."),
 ("Niche partitioning",
  "EK 8.5.B.3 lists niche partitioning among its examples. Dividing a shared resource so each population uses a different part of it is what the term names."),
 ("Competition, predation, and symbioses including parasitism, mutualism, and commensalism",
  "EK 8.5.B.4 states exactly that list of relationships as able to drive population dynamics. The distractor lists are the carbon cycle, the hydrologic cycle, the ecological levels of organization and the trophic levels."),
 ("Parasitism",
  "EK 8.5.B.3 says relationships can be characterized by positive and negative effects and EK 8.5.B.4 names parasitism, mutualism and commensalism as symbioses without defining them. The stem supplies the effects -- one population helped, the other harmed -- and the key rests on that characterization plus the ordinary meaning of the term the CED prints."),
 ("Mutualism",
  "EK 8.5.B.3's positive and negative effects applied to EK 8.5.B.4's three named symbioses, with the effects stated in the stem: a benefit to both populations. Predation and competition are listed separately from the symbioses in the same statement."),
 ("Commensalism",
  "EK 8.5.B.3's positive and negative effects applied to EK 8.5.B.4's three named symbioses, with the effects stated in the stem: a benefit to one population and no effect on the other, which distinguishes it from the two symbioses that help or harm both."),
 ("Competition",
  "EK 8.5.B.4 names competition among the relationships that can drive population dynamics, and EK 8.5.B.3 characterizes relationships by their effects. Each population reducing what is available to the other is a negative effect in both directions."),
 ("Nitrogen fixation",
  "EK 8.5.B.4 names competition, predation, and symbioses including parasitism, mutualism and commensalism. Nitrogen fixation is a step of the nitrogen cycle in EK 8.2.B.6 and is not a relationship between populations at all."),
 ("0.62",
  "The framework prints the index as one minus the sum of the squares of n over N. The table check above recomputes it from the named row's counts, having first confirmed every community holds the same total, so the squares are exact and the item is calculator-free."),
 ("Community Z",
  "EK 8.5.A.1 makes species diversity part of what describes community structure and the printed index is its measure. The table check above computes the index for every row and confirms the maximum is unique."),
 ("Three",
  "EK 8.5.A.1 makes species composition part of what describes community structure. The table check above counts the columns in which the named row records at least one individual, and confirms that number differs from the number of individuals."),
 ("distributed differently among the species",
  "EK 8.5.A.1 measures structure by composition and diversity together, and the printed index squares each species' share. The table check above confirms two rows share a species count and a total while differing in their counts and in their index."),
 ("because most of its individuals belong to a single species",
  "The printed index subtracts the sum of squared shares from one, and one large share contributes more than several small ones. The table check above confirms the smallest index is unique, belongs to the named row, and that this row has one species holding more than half the individuals."),
 ("Site 1 and Site 2",
  "Skill 5.B asks a student to use error bars to estimate whether sample means are statistically different. The table check above confirms exactly one pair of intervals overlaps and that the key names that pair and no other."),
 ("do not support a claim that the two means are different",
  "Skill 5.B asks whether sample means are STATISTICALLY different. Overlapping intervals leave the observed difference within what sampling alone could produce, which is a failure to establish a difference rather than a demonstration of sameness; the check confirms the two means are not equal."),
 ("Site 3",
  "Skill 5.B asks for an estimate of whether sample means are statistically different. The table check above confirms exactly one other site has an interval that does not overlap the interval around the site the stem names."),
 ("10 species per plot",
  "Skill 5.A includes differences and skill 5.B settles whether the comparison is meaningful. The table check above confirms the two sites the stem names have intervals that do not overlap, and recomputes the difference between their means."),
 ("how much the means could differ by sampling alone",
  "Skill 5.B asks a student to use confidence intervals and error bars to estimate whether sample means are STATISTICALLY different. Two sample means are almost never exactly equal, so the size of the difference against the uncertainty is what settles the comparison."),
 ("composition and species diversity together, and the diversity of the two can differ",
  "EK 8.5.A.1 states that structure is described in terms of species composition AND species diversity. Two communities can share a species list and still differ in how the individuals are distributed, which the printed index measures."),
 ("characterized by positive and negative effects, can drive population dynamics",
  "EK 8.5.A.1 supplies the description of structure, EK 8.5.B.1 the definition and the change over time, EK 8.5.B.3 the characterization by effects and the possibility of modelling, and EK 8.5.B.4 the driving of population dynamics. Each distractor contradicts one of those."),
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

# Error bars are drawn on a chart and the bank cannot show one, so the interval
# ends are given as columns and no stem may promise a picture.
_FIGURE_TALK = re.compile(
    r"(?<![A-Za-z])(the (?:graph|figure|diagram|chart|plot) (?:shown|above|below)|"
    r"in the (?:graph|figure|diagram|chart|plot) (?:shown|above|below)|"
    r"shown in the (?:graph|figure|diagram|chart|plot))(?![A-Za-z])",
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
    cg.check(b8_5, CLAIMS, table_checks=TABLE_CHECKS)
    print(f"    {n_style} notation and figure-reference checks clean.")


main()
