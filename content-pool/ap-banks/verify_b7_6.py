"""Key audit for AP BIOLOGY 7.6 Evidence of Evolution.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor, so an off-by-one key stops matching; the
claim states what the key rests on, for a human to audit.

WHAT THE KEYS REST ON
---------------------
Items 1 to 11, 18 to 21 and 26 to 30 are keyed to sentences the CED prints:
EK 7.6.A.1 (the five disciplines), EK 7.6.B.1 (evidence from extant and extinct
organisms; the three fossil dating methods; morphological homologies including
vestigial structures as evidence of common ancestry) and EK 7.6.B.2 (comparison
of DNA nucleotide and protein amino acid sequences as evidence for evolution
and common ancestry).

Items 12 to 17 and 22 to 25 carry a table, and skill 4.B is exactly the skill
of reading one. Every claim those keys make about the numbers is RECOMPUTED
below from the table alone, through cg_check's header-and-label accessors, and
where the stem names a value the check locates the row by parsing that value
out of the stem rather than by trusting a row index. cg_check.check fails a
question that carries a table with no such callable.

None of this says whether the biology is right; that is gated by the CLAIMS
text and by the rule in SCIENCE_BRIEF.md that a key must trace to a CED
sentence.

NEGATIVE CONTROL. Moving any key, changing any table cell or changing the first
number in any stem the checks read makes this file raise; confirmed by running
exactly that before shipping.
"""
import re

import cg_check as cg
import b7_6

QS = b7_6.QUESTIONS
T_LAYERS = b7_6._T_LAYERS
T_ISOTOPE = b7_6._T_ISOTOPE
T_AA = b7_6._T_AA

DEPTH = "Depth below the present surface in metres"
AGE_MY = "Estimated age of the layer in millions of years"
FRACTION = "Fraction of the original isotope still present"
AGE_YR = "Age of the sample in years"
DIFFS = "Number of amino acid differences in a protein of 100 amino acids"

# No \b anywhere: a digit and a letter are both word characters, so \b is
# silently not a boundary next to either. Explicit lookarounds instead.
_NUM_IN_STEM = re.compile(r"(?<![A-Za-z0-9.])(\d+(?:\.\d+)?)(?![0-9]|\.\d)")

_WORD_FRACTION = {"one half": 0.5, "one quarter": 0.25,
                  "one eighth": 0.125, "one sixteenth": 0.0625}


def stem_nums(item):
    return [float(x) for x in _NUM_IN_STEM.findall(item["q"])]


def keyed(item):
    return item["choices"][item["ans"]]


def row_where(table, header, value):
    """The single row label whose named column equals ``value``."""
    hits = [lab for lab in cg.labels(table) if cg.cell(table, lab, header) == value]
    assert len(hits) == 1, f"{value} matches {len(hits)} rows of column {header!r}"
    return hits[0]


def raw(table, row_label, header):
    """A cell as written, found by row label and column header."""
    j = [cg.normalize(h) for h in table["headers"]].index(cg.normalize(header))
    i = [cg.normalize(lab) for lab in cg.labels(table)].index(cg.normalize(row_label))
    return str(table["rows"][i][j])


def q12(table, item):
    ages = {lab: cg.cell(table, lab, AGE_MY) for lab in cg.labels(table)}
    oldest = max(ages, key=ages.get)
    assert cg.contains_phrase(keyed(item), oldest), \
        f"q12 key {keyed(item)!r} but the greatest age belongs to {oldest}"
    assert sorted(ages.values())[-2] < ages[oldest], "the oldest layer must be unique"
    return f"the age column runs {ages} and its maximum is {oldest}"


def q13(table, item):
    deep, shallow = stem_nums(item)
    a = cg.cell(table, row_where(table, DEPTH, deep), AGE_MY)
    b = cg.cell(table, row_where(table, DEPTH, shallow), AGE_MY)
    assert a > b, "the stem names the deeper layer first, which must be the older"
    assert keyed(item) == f"{int(a - b)} million years", \
        f"q13 key {keyed(item)!r} but the ages differ by {a - b}"
    return f"depth {int(deep)} gives age {int(a)} and depth {int(shallow)} gives {int(b)}, a gap of {int(a - b)}"


def q14(table, item):
    pairs = sorted(zip(cg.col(table, DEPTH), cg.col(table, AGE_MY)))
    ages = [a for _, a in pairs]
    assert all(y > x for x, y in zip(ages, ages[1:])), \
        f"the key says age rises with depth at every step; ages by depth are {ages}"
    return f"sorting the four rows by depth gives ages {ages}, rising at every step"


def q15(table, item):
    half_life = stem_nums(item)[0]
    named = [f for f in _WORD_FRACTION if cg.contains_phrase(item["q"], f)]
    assert len(named) == 1, f"the stem names {named}; it must name exactly one fraction"
    lab = row_where_text(table, FRACTION, named[0])
    age = cg.cell(table, lab, AGE_YR)
    order = [cg.normalize(raw(table, l, FRACTION)) for l in cg.labels(table)]
    n_halflives = order.index(cg.normalize(named[0])) + 1
    assert _WORD_FRACTION[named[0]] == 0.5 ** n_halflives, \
        f"{named[0]} is not what remains after {n_halflives} half-lives"
    assert age == half_life * n_halflives, \
        f"row age {age} is not {n_halflives} half-lives of {half_life}"
    assert keyed(item) == f"{int(age)} years", f"q15 key {keyed(item)!r} but the row gives {int(age)}"
    return (f"{named[0]} is the {n_halflives} half-life row, and {n_halflives} times "
            f"{int(half_life)} years is {int(age)} years")


def row_where_text(table, header, text):
    hits = [lab for lab in cg.labels(table)
            if cg.normalize(raw(table, lab, header)) == cg.normalize(text)]
    assert len(hits) == 1, f"{text!r} matches {len(hits)} rows of column {header!r}"
    return hits[0]


def q16(table, item):
    age = stem_nums(item)[0]
    lab = row_where(table, AGE_YR, age)
    n = raw(table, lab, "Number of half-lives elapsed")
    assert cg.contains_phrase(keyed(item), n), \
        f"q16 key {keyed(item)!r} but the row for {age} is labelled {n!r}"
    return f"the age column locates {int(age)} years in the row labelled {n}"


def q17(table, item):
    order = [raw(table, lab, FRACTION) for lab in cg.labels(table)]
    vals = [_WORD_FRACTION[cg.normalize(f)] for f in order]
    assert all(abs(b - a / 2) < 1e-12 for a, b in zip(vals, vals[1:])), \
        f"the key says each entry halves the one above; the column reads {vals}"
    assert vals[-1] > 0, "the key says the amount never reaches zero"
    ages = cg.col(table, AGE_YR)
    step = ages[1] - ages[0]
    assert all(abs((b - a) - step) < 1e-9 for a, b in zip(ages, ages[1:])), \
        "equal half-life intervals must add equal amounts of time"
    return f"the fraction column reads {vals}, each half the one above, over equal steps of {int(step)} years"


def q22(table, item):
    n = stem_nums(item)[0]
    lab = row_where(table, DIFFS, n)
    assert cg.contains_phrase(keyed(item), lab), \
        f"q22 key {keyed(item)!r} but {int(n)} differences belong to {lab}"
    return f"{int(n)} appears once in the difference column, in the row for {lab}"


def q23(table, item):
    d = cg.col(table, DIFFS)
    assert all(y > x for x, y in zip(d, d[1:])), \
        f"the key says the count increases at every step; the column reads {d}"
    return f"the difference column reads {d} in written row order, rising at every step"


def q24(table, item):
    length = cg.num(DIFFS.split("protein of")[1])
    named = [lab for lab in cg.labels(table) if cg.contains_phrase(item["q"], lab)]
    assert len(named) == 1, f"the stem names rows {named}; it must name exactly one"
    d = cg.cell(table, named[0], DIFFS)
    pct = (length - d) / length * 100
    assert abs(pct - round(pct)) < 1e-9, "the percentage must be whole for a calculator-free item"
    assert keyed(item) == f"{int(round(pct))} percent", \
        f"q24 key {keyed(item)!r} but {int(length - d)} of {int(length)} identical is {pct} percent"
    return (f"{named[0]} differs at {int(d)} of the {int(length)} positions the header states, "
            f"so {int(round(pct))} percent are identical")


def q25(table, item):
    d = {lab: cg.cell(table, lab, DIFFS) for lab in cg.labels(table)}
    fewest = min(d, key=d.get)
    most = max(d, key=d.get)
    assert fewest != most, "the column must not be constant"
    assert sorted(d.values())[1] > d[fewest], "the smallest count must be unique"
    assert cg.contains_phrase(keyed(item), "fewest"), \
        "the key must turn on the smallest count, not on a named species"
    return f"the difference column runs {d}; its unique minimum is {fewest} and its maximum {most}"


TABLE_CHECKS = {12: q12, 13: q13, 14: q14, 15: q15, 16: q16, 17: q17,
                22: q22, 23: q23, 24: q24, 25: q25}


CLAIMS = [
 ("geographical, geological, physical",
  "EK 7.6.A.1 names geographical, geological, physical, biochemical and mathematical data as the evidence supporting evolution. Every distractor names one real line of evidence and excludes the rest, which is the error the statement is written against."),
 ("Geographical data",
  "EK 7.6.A.1 lists geographical data among the disciplines. Recording which related species occur on which islands and mainland is a statement about where organisms are, which is geographical whatever the organisms are made of."),
 ("Geological data",
  "EK 7.6.A.1 lists geological data, and EK 7.6.B.1 makes the age of the rocks where a fossil is found one of the three named dating methods. The sequence of layers is what is being read here."),
 ("Biochemical data",
  "EK 7.6.A.1 lists biochemical data and EK 7.6.B.2 names protein amino acid sequence comparison specifically as evidence for evolution and common ancestry."),
 ("Mathematical data",
  "EK 7.6.A.1 lists mathematical data among the five disciplines. Constructing a quantitative prediction and testing it against measurement is the mathematical contribution, independent of what is being measured."),
 ("different sources of error",
  "EK 7.6.A.1 names five separate disciplines rather than one authoritative source. Rock dating, sequence comparison and species distribution each fail in their own way, so agreement among them is not explained by any single method's weakness."),
 ("organisms known only as fossils",
  "EK 7.6.B.1 states that molecular, morphological and genetic evidence from extant AND extinct organisms adds to our understanding of evolution. The statement names both groups, so any option restricting it to one is wrong."),
 ("the age of the rocks in which the fossil is found",
  "EK 7.6.B.1 lists three fossil dating methods and this is the first of them. Body size and modern species counts date nothing, and sequence comparison belongs to EK 7.6.B.2 as evidence of ancestry rather than as a date."),
 ("the rate at which the isotope decays",
  "EK 7.6.B.1 names the rate of decay of isotopes, including carbon-14, as a dating method. A known decay rate is what converts a measured remaining fraction into an elapsed time; without it the measurement fixes nothing."),
 ("Geographical data",
  "EK 7.6.B.1 lists exactly three fossil dating methods, of which geographical data is the third alongside the age of the rocks and the rate of isotope decay. Vestigial structures and sequences are evidence of ancestry in this same topic, not dating methods."),
 ("fail in different ways",
  "EK 7.6.B.1 offers a variety of dating methods rather than one, which is what makes cross-checking possible at all. Two methods with unrelated failure modes agreeing is evidence about the date; repeating one measurement is not."),
 ("layer 4",
  "EK 7.6.B.1's first dating method, the age of the rock in which the fossil is found. The table check above reads the age column and confirms the greatest age is unique and belongs to the keyed layer."),
 ("48 million years",
  "Skill 4.B, identifying specific data points and relating two variables. The table check above locates both rows by the depths the stem names and recomputes the difference between their ages."),
 ("the greater its estimated age",
  "Skill 4.B asks for the relationship between the variables. The table check above sorts the rows by depth and confirms the age rises at every step, which is what allows surrounding rock to date a fossil under EK 7.6.B.1."),
 ("12000 years",
  "EK 7.6.B.1 names the rate of isotope decay as a dating method. The table check above finds the row for the fraction the stem names, confirms that fraction is what remains after that many half-lives, and confirms the row's age is that many half-lives of the stated length."),
 ("Four",
  "Skill 4.B, identifying a specific data point. The table check above locates the stated age in the age column and reads the number of half-lives from the same row."),
 ("half of the entry above it",
  "The defining property of a half-life, which is what makes EK 7.6.B.1's decay method a clock. The table check above confirms each fraction is half the one above and that equal half-life steps add equal amounts of time."),
 ("common ancestry",
  "EK 7.6.B.1 states that morphological homologies, including vestigial structures, provide evidence of common ancestry. Homology is a claim about shared origin, not about what a structure is currently used for."),
 ("a morphological homology",
  "EK 7.6.B.1. The same bones in the same relative positions serving different uses is the pattern that descent with modification from a shared ancestor predicts, and that shared function does not."),
 ("a vestigial structure",
  "EK 7.6.B.1 names vestigial structures among the morphological homologies that provide evidence of common ancestry. A reduced version of a relative's working structure is what retention from a shared ancestor looks like."),
 ("DNA nucleotide sequences and of protein amino acid sequences",
  "EK 7.6.B.2 names exactly this comparison as providing evidence for evolution and common ancestry. The other options describe measurements the framework does not identify as evidence of ancestry."),
 ("Species T",
  "Skill 4.B, identifying a specific data point. The table check above locates the number of differences the stem names and confirms it appears in exactly one row."),
 ("increases at every step",
  "Skill 4.B asks for the trend before any interpretation of it. The table check above confirms each count exceeds the one above it in written row order."),
 ("88 percent",
  "Skill 5.A includes percentages. The table check above takes the protein length from the column header, subtracts that row's difference count and confirms the remainder as a whole percentage."),
 ("fewest positions",
  "EK 7.6.B.2 makes sequence comparison evidence for common ancestry. Differences accumulate after two lineages separate, so the smallest count corresponds to the shortest separate history; the table carries no calibration, so it cannot support a date."),
 ("present in an ancestor shared by all of them",
  "EK 7.6.B.2 makes such a comparison evidence for evolution and common ancestry. The presence of one recognisable version of the same protein in every species compared is explained by inheritance from a single ancestor."),
 ("independent line of evidence",
  "EK 7.6.A.1 makes biochemical data one of several disciplines and EK 7.6.B.2 names sequence comparison among them. A line of evidence is not discarded for disagreeing with appearance; that is what having several disciplines is for."),
 ("no time scale unless it is calibrated",
  "EK 7.6.B.2 licenses an inference to common ancestry and not to a date, while EK 7.6.B.1 puts dating with rock ages and isotope decay. Converting a count of differences into years needs the dating evidence the conclusion did not use."),
 ("nucleotide sequences of a gene shared by the same species",
  "EK 7.6.A.1 treats the disciplines as separate sources of evidence. Remeasuring the same morphological characters more carefully is not independent of those characters; a molecular comparison under EK 7.6.B.2 is."),
 ("descend from shared ancestors",
  "This is what learning objective 7.6.B asks students to explain, and what EK 7.6.B.1 and EK 7.6.B.2 assert jointly: geological, morphological and molecular data are evidence that organisms have changed over time and share ancestry. No statement in the topic claims a uniform rate of change."),
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
    return hits


def main():
    n_style = style()
    cg.check(b7_6, CLAIMS, table_checks=TABLE_CHECKS)
    print(f"    {n_style} notation checks clean (no LaTeX, no ranges, no slash fractions).")


main()
