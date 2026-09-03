"""Key audit for AP BIOLOGY 7.9 Phylogeny.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor, so an off-by-one key stops matching; the
claim states what the key rests on, for a human to audit.

WHAT THE KEYS REST ON
---------------------
Items 1 to 18 and 27 to 30 are keyed to sentences the CED prints: EK 7.9.A.1
(hypothetical relationships that can be tested), EK 7.9.A.2 (a tree shows the
amount of change over time calibrated by fossils or a molecular clock; a
cladogram shows neither a time scale nor the evolutionary difference between
groups), EK 7.9.A.3 (traits gained or lost; the out-group is the lineage least
closely related to the remainder; shared derived characters indicate common
ancestry; molecular data TYPICALLY beat morphological traits), EK 7.9.B.1
(nodes are the most recent common ancestor; speciation can be illustrated),
EK 7.9.B.2 (morphological similarities of living or fossil species, and DNA and
protein sequence similarities) and EK 7.9.B.3 (hypotheses constantly revised).

Items 19 to 26 carry a table. THE BANK CANNOT SHOW A DIAGRAM, so no stem here
refers to one: the data items carry the character matrix a cladogram would be
built FROM, and the diagram item is a feature-by-diagram table rather than a
picture. Every claim those keys make about the data -- which lineage shares
nothing, which pair shares most, which character is most widespread, how many
lineages carry a character, which row of the comparison differs between the two
diagram types -- is RECOMPUTED below from the table alone. Where the stem
describes a set of characters, the check reads that set out of the stem text
rather than hard-coding it.

None of this says whether the biology is right; that is gated by the CLAIMS
text and by the rule in SCIENCE_BRIEF.md that a key must trace to a CED
sentence.

NEGATIVE CONTROL. Moving any key, or changing any table cell the keys depend
on, makes this file raise; confirmed by running exactly that.
"""
import itertools
import re

import cg_check as cg
import b7_9

QS = b7_9.QUESTIONS
T_CHARS = b7_9._T_CHARS
T_DIAGRAMS = b7_9._T_DIAGRAMS

TREE_COL = "Shown by a phylogenetic tree"
CLADO_COL = "Shown by a cladogram"
NUMBER_WORDS = ["Zero", "One", "Two", "Three", "Four", "Five", "Six"]


def keyed(item):
    return item["choices"][item["ans"]]


def raw(table, row_label, header):
    j = [cg.normalize(h) for h in table["headers"]].index(cg.normalize(header))
    i = [cg.normalize(lab) for lab in cg.labels(table)].index(cg.normalize(row_label))
    return str(table["rows"][i][j])


def characters(table):
    """The character column headers, which are every header but the row label."""
    return table["headers"][1:]


def present(table, lab):
    """The set of characters recorded as present for one lineage."""
    states = {h: cg.normalize(raw(table, lab, h)) for h in characters(table)}
    for h, v in states.items():
        assert v in ("present", "absent"), f"{lab}/{h} reads {v!r}, not present or absent"
    return {h for h, v in states.items() if v == "present"}


def q19(table, item):
    counts = {lab: len(present(table, lab)) for lab in cg.labels(table)}
    fewest = min(counts, key=counts.get)
    assert counts[fewest] == 0, \
        f"the out-group must share none of the characters; {fewest} has {counts[fewest]}"
    assert sorted(counts.values())[1] > 0, f"more than one lineage shares nothing: {counts}"
    assert cg.contains_phrase(keyed(item), fewest), \
        f"q19 key {keyed(item)!r} but the lineage sharing nothing is {fewest}"
    return f"characters present per lineage are {counts}; only {fewest} shares none with the rest"


def q20(table, item):
    labs = cg.labels(table)
    shared = {pair: len(present(table, pair[0]) & present(table, pair[1]))
              for pair in itertools.combinations(labs, 2)}
    best = max(shared, key=shared.get)
    runner = sorted(shared.values())[-2]
    assert runner < shared[best], f"the greatest number of shared characters is not unique: {shared}"
    for lab in best:
        assert cg.contains_phrase(keyed(item), lab), \
            f"q20 key {keyed(item)!r} does not name {lab}, which is in the best-sharing pair {best}"
    return f"the best-sharing pair is {best} with {shared[best]} characters, ahead of the next pair at {runner}"


def q21(table, item):
    counts = {h: sum(1 for lab in cg.labels(table) if h in present(table, lab))
              for h in characters(table)}
    most = max(counts, key=counts.get)
    assert sorted(counts.values())[-2] < counts[most], \
        f"the most widespread character is not unique: {counts}"
    assert cg.contains_phrase(keyed(item), most), \
        f"q21 key {keyed(item)!r} but the most widespread character is {most}"
    return f"characters are present in {counts} lineages respectively; the maximum is {most}"


def q22(table, item):
    counts = {h: sum(1 for lab in cg.labels(table) if h in present(table, lab))
              for h in characters(table)}
    singles = [h for h, n in counts.items() if n == 1]
    assert len(singles) == 1, f"exactly one character must be unique to a lineage; {singles} are"
    assert cg.contains_phrase(keyed(item), singles[0]), \
        f"q22 key {keyed(item)!r} but the character present in one lineage is {singles[0]}"
    return f"character counts are {counts}; only {singles[0]} appears in a single lineage"


def q23(table, item):
    named = [h for h in characters(table) if cg.contains_phrase(item["q"], h)]
    assert len(named) == 1, f"the stem names characters {named}; it must name exactly one"
    n = sum(1 for lab in cg.labels(table) if named[0] in present(table, lab))
    assert keyed(item) == NUMBER_WORDS[n], \
        f"q23 key {keyed(item)!r} but {named[0]} is present in {n} lineages"
    return f"{named[0]} is recorded as present in {n} of the {len(cg.labels(table))} lineages"


def q24(table, item):
    wanted = {h for h in characters(table) if cg.contains_phrase(item["q"], h)}
    assert wanted, "the stem must name the characters the sixth lineage possesses"
    assert wanted != set(characters(table)), \
        "the stem names every character, so the described lineage is not distinguishable"
    matches = [lab for lab in cg.labels(table) if present(table, lab) == wanted]
    assert len(matches) == 1, f"the described character set matches rows {matches}"
    assert cg.contains_phrase(keyed(item), matches[0]), \
        f"q24 key {keyed(item)!r} but the row with exactly {sorted(wanted)} present is {matches[0]}"
    return f"the stem names {sorted(wanted)} as present, which matches {matches[0]} in every column"


def _yes_no(table, lab, header):
    v = cg.normalize(raw(table, lab, header))
    assert v in ("yes", "no"), f"{lab}/{header} reads {v!r}, not yes or no"
    return v == "yes"


def q25(table, item):
    differ = [lab for lab in cg.labels(table)
              if _yes_no(table, lab, TREE_COL) != _yes_no(table, lab, CLADO_COL)]
    same = [lab for lab in cg.labels(table) if lab not in differ]
    assert len(differ) == 2 and len(same) == 1, \
        f"the key names two differing rows and one shared row; got {differ} and {same}"
    for lab in differ:
        # The key must quote at least four consecutive words of the row it
        # names. A shorter match would let "The amount" alone satisfy the
        # check, and a checker that under-matches is worse than none.
        words = cg.normalize(lab).split()
        grams = [" ".join(words[k:k + 4]) for k in range(len(words) - 3)]
        assert any(cg.contains_phrase(keyed(item), g) for g in grams), \
            f"q25 key {keyed(item)!r} quotes no four-word run of the differing row {lab!r}"
    for lab in same:
        words = cg.normalize(lab).split()
        grams = [" ".join(words[k:k + 4]) for k in range(len(words) - 3)]
        assert not any(cg.contains_phrase(keyed(item), g) for g in grams), \
            f"q25 key {keyed(item)!r} also names {lab!r}, which does not differ between the columns"
    return f"rows {differ} differ between the two diagram columns while {same} is the same in both"


def q26(table, item):
    time_rows = [lab for lab in cg.labels(table) if cg.contains_phrase(lab, "a scale of time")]
    assert len(time_rows) == 1, f"exactly one row must record a time scale; got {time_rows}"
    lab = time_rows[0]
    assert _yes_no(table, lab, TREE_COL) and not _yes_no(table, lab, CLADO_COL), \
        "the key requires the tree to carry a time scale and the cladogram not to"
    assert cg.contains_phrase(keyed(item), "phylogenetic tree"), \
        f"q26 key {keyed(item)!r} does not name the diagram the table credits with a time scale"
    return f"the row {lab!r} reads yes for the tree and no for the cladogram"


TABLE_CHECKS = {19: q19, 20: q20, 21: q21, 22: q22, 23: q23, 24: q24, 25: q25, 26: q26}


CLAIMS = [
 ("Hypothetical evolutionary relationships among lineages that can be tested",
  "EK 7.9.A.1, near verbatim: phylogenetic trees and cladograms show hypothetical evolutionary relationships among lineages that can be tested. Both halves matter, since the relationships are proposed rather than settled and are open to evidence."),
 ("proposals that evidence can support or overturn",
  "EK 7.9.A.1 pairs the word hypothetical with the clause that the relationships CAN BE TESTED, and EK 7.9.B.3 adds that the diagrams are constantly revised on evidence. Testability is what separates a hypothesis from a definition and from a guess beyond evidence."),
 ("constantly revised as new evidence appears",
  "EK 7.9.B.3 states that phylogenetic trees and cladograms represent hypotheses that are constantly being revised based on evidence. Revision in response to evidence is the normal life of such a diagram, not a sign that it was worthless."),
 ("amount of change over time, calibrated by fossils or a molecular clock",
  "EK 7.9.A.2 states that phylogenetic trees show the amount of change over time calibrated by fossils or a molecular clock, whereas cladograms show neither a time scale nor the evolutionary difference between groups. Branching order and hypothetical status belong to both."),
 ("time scale or the evolutionary difference between groups",
  "EK 7.9.A.2 says in as many words that cladograms do not show time scale or the evolutionary difference between groups. Everything else listed is what EK 7.9.A.1 and EK 7.9.A.3 give to any such diagram."),
 ("phylogenetic tree, because it represents the amount of change over time",
  "EK 7.9.A.2 assigns the amount of change over time to the tree and denies it to the cladogram, while EK 7.9.A.1 gives the proposed relationships to both. Only the tree supplies both things the researcher asks for."),
 ("Fossils or a molecular clock",
  "EK 7.9.A.2 names fossils or a molecular clock as the calibration for the amount of change over time a phylogenetic tree shows. Without one of those a diagram carries branching order and no scale."),
 ("either gained or lost during evolution",
  "EK 7.9.A.3 states that traits either gained or lost during evolution can be used to construct phylogenetic trees and cladograms. A trait present in every lineage divides none of them, which is why universality is not the criterion."),
 ("least closely related to the remainder",
  "EK 7.9.A.3 states that the out-group represents the lineage least closely related to the remainder of the organisms in the tree or cladogram. Species richness, fossil status and amount of change do not define the role."),
 ("Scoring additional characters or sequences",
  "EK 7.9.A.1 says the relationships shown can be tested and EK 7.9.B.3 says the diagrams are revised on evidence. A test requires evidence that could have come out otherwise, which redrawing or annotating an existing diagram does not supply."),
 ("Common ancestry of the lineages that share them",
  "EK 7.9.A.3 states that shared derived characters can be present in more than one lineage and indicate common ancestry. The statement makes no claim about habitat, species identity or elapsed time, the last of which EK 7.9.A.2 assigns to a calibrated tree."),
 ("shared by some lineages and not others groups those lineages together",
  "EK 7.9.A.3 calls shared derived characters informative for the construction of trees and cladograms. Presence in some lineages and absence in others is precisely what divides a set of lineages into groups."),
 ("typically provide more accurate and reliable evidence",
  "EK 7.9.A.3 states that molecular data typically provide more accurate and reliable evidence than morphological traits in construction. EK 7.9.B.2 separately admits morphological similarities of living OR fossil species, so neither source is restricted as two distractors claim."),
 ("general tendency",
  "EK 7.9.A.3 writes TYPICALLY rather than always, and EK 7.9.B.2 keeps morphological similarities among the admissible sources. A stated tendency licenses neither an absolute nor the abandonment of the other kind of data."),
 ("most recent common ancestor of any two groups or lineages",
  "EK 7.9.B.1 states that the nodes on a tree represent the most recent common ancestor of any two groups or lineages. An ancestor at a node is not one of the diagram's tips, so it is not a species alive today."),
 ("Speciation that has already occurred",
  "EK 7.9.B.1 states that phylogenetic trees and cladograms can be used to illustrate speciation that has occurred. Population size, habitat and reproductive rate are not represented on such a diagram at all."),
 ("living or fossil species and DNA and protein sequence similarities",
  "EK 7.9.B.2 names exactly those sources: morphological similarities of living or fossil species, and DNA and protein sequence similarities. Cutting the list to one source, or replacing it with range or abundance, contradicts the statement."),
 ("number of individuals of each species counted in a survey",
  "EK 7.9.B.2 lists morphological similarities of living or fossil species and DNA and protein sequence similarities, and abundance is not among them. How many individuals are alive now says nothing about the characters that group lineages."),
 ("Lineage W",
  "EK 7.9.A.3 defines the out-group as the lineage least closely related to the remainder, and shared derived characters indicate common ancestry. The table check above confirms exactly one lineage shares none of the scored characters with the others."),
 ("Lineage Z and Lineage V",
  "EK 7.9.A.3 makes shared derived characters informative for construction, because characters shared by two lineages and absent from others group those two together. The table check above computes the shared count for every pair and confirms the maximum is unique."),
 ("Backbone",
  "Skill 4.B, identifying specific data points across a table, applied to EK 7.9.A.3's grouping logic: a character present in more lineages groups a larger set of them. The table check above counts each character column and confirms the maximum is unique."),
 ("Hair",
  "EK 7.9.A.3 makes SHARED derived characters the informative ones. The table check above confirms exactly one character appears in a single lineage, and a character present in only one lineage groups it with nothing."),
 ("Two",
  "Skill 4.B, identifying specific data points. The table check above reads the character column the stem names and counts the lineages recorded as possessing it."),
 ("Lineage Y",
  "EK 7.9.A.3 makes shared derived characters the basis for grouping. The table check above reads the described set of present characters out of the stem and confirms exactly one row of the table matches it in every column."),
 ("scale of time and the row for the amount of evolutionary difference",
  "EK 7.9.A.2 denies the cladogram both a time scale and the evolutionary difference between groups, while EK 7.9.A.1 gives the proposed relationships to both diagrams. The table check above confirms exactly two rows differ between the two columns and one is the same in both."),
 ("phylogenetic tree, because it is the only one of the two that carries a scale of time",
  "EK 7.9.A.2 assigns a time scale to the tree and denies it to the cladogram. The table check above confirms the time row reads yes for the tree and no for the cladogram, and branching order is carried by both and so cannot decide between them."),
 ("A living species from which the branches above it are descended",
  "EK 7.9.B.1 identifies a node as the most recent common ancestor of two groups or lineages, which is an ancestral form rather than one of the present-day tips. EK 7.9.A.1 and EK 7.9.B.3 make everything at a node part of a hypothesis open to revision."),
 ("the available evidence better supports",
  "EK 7.9.A.1 makes these diagrams testable hypotheses and EK 7.9.B.3 makes them subject to constant revision on evidence. Competing hypotheses about the same lineages are settled by evidence, not by priority, size or ease of drawing."),
 ("hypotheses revised on evidence, and that molecular data typically provide more accurate",
  "EK 7.9.B.3 makes revision on evidence the normal case and EK 7.9.A.3 states the molecular advantage as a tendency. EK 7.9.B.2 keeps morphological similarities among the admissible sources, so the option denying them overstates the point."),
 ("only the tree carries a time scale",
  "EK 7.9.A.1 gives both diagrams the status of testable hypotheses about relationships, and EK 7.9.A.2 gives the time scale and the amount of evolutionary difference to the tree alone. EK 7.9.B.2 allows either diagram to be built from either kind of data."),
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

# A stem that promises a picture the bank cannot show is the defect
# SCIENCE_BRIEF.md says this project has already shipped once. Every phrase
# below is barred outright; a data item must carry its own table instead.
_FIGURE_TALK = re.compile(
    r"(?<![A-Za-z])(the (?:tree|cladogram|diagram|graph|figure) (?:shown|above|below)|"
    r"in the (?:tree|cladogram|diagram|figure) (?:shown|above|below)|"
    r"shown in the (?:tree|cladogram|diagram|figure))(?![A-Za-z])",
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
    cg.check(b7_9, CLAIMS, table_checks=TABLE_CHECKS)
    print(f"    {n_style} notation and figure-reference checks clean.")


main()
