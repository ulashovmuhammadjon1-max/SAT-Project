"""Key audit for AP CHEMISTRY 3.8 Representations of Solutions.

One (anchor, claim) per item, in module order.

THE WHOLE TOPIC IS ABOUT PICTURES AND THIS BANK HAS NONE. That is the defect
this file exists to make impossible, so it carries two checks nothing else in
the Chemistry bank needs:

``no_deictic_reference`` bans "above", "below", "as shown" and their relatives
from every student-facing string. A stem that points at a picture the student
cannot see is unanswerable, and pointing words are the only way to do it.

``described_representations_carry_their_numbers`` is the stronger half. Any stem
that says a representation SHOWS something must either carry a ``table=`` or
state the counts in figures. A qualitative stem may stay qualitative; a stem
that asks a student to read a specific drawing must supply that drawing in
words. Both halves are negative-controlled.

WHAT THE KEYS REST ON. EK 3.8.A.1 says particulate representations communicate
the structure and properties of solutions, by illustration of the relative
concentrations of the components and/or drawings that show interactions among
the components. Two exclusion statements attached to it put colligative
properties, and calculations of molality, percent by mass and percent by volume,
outside the exam.

  the sentence itself     1, 2, 7, 8, 9, 12, 13, 16, 17, 18, 19, 28, 30
  the learning objective's two parts                          5, 6
  the exclusion statements                                    3, 4, 11
  relative amounts of the components of a dissolved compound
                          14, 15, 20, 21, 22
  concentration as an amount per depicted volume        23, 24, 25, 26
  EK 3.8.A.1 with EK 3.1.A.3 for the orientation items     10, 27
  the pairing of feature with meaning                         29

THE STOICHIOMETRY IS SUPPLIED BY THE STEM. Every item asking whether a drawing
of a dissolved ionic compound is right states how many cations and anions a
formula unit provides, so nothing here rests on unit 2 or unit 4 knowledge.
``ion_items_state_their_ratio`` asserts that.

THE EXCLUDED MEASURES may be keyed only where the stem frames them as excluded
or as something representations do not communicate;
``excluded_only_when_disowned`` enforces that and asserts they appear somewhere,
so the check cannot pass over an empty set.

NEGATIVE CONTROL: ``python3 verify_h3_8.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h

import h3_8

SOLUTE = "Solute particles drawn"
SOLVENT = "Solvent particles drawn"
CATIONS = "Cations drawn"
ANIONS = "Anions drawn"
BEAKVOL = "Volume represented (mL)"

# Pointing words. Bare "above" and "below" are included deliberately: in this
# module there is nothing legitimate for them to modify, and they are exactly
# how a stem would end up pointing at a picture that is not there.
_DEICTIC = re.compile(
    r"(?<![a-z])(above|below|as shown|shown here|the following diagram|pictured|"
    r"depicted here|this diagram|the image|the picture|see the figure)(?![a-z])", re.I)

# An INSTANCE-referring stem: one that names a particular drawing and asserts
# what it holds. A stem that states a general principle about representations
# ("the more concentrated of two drawings must ...") supplies nothing to read
# and needs no numbers, which is why the trigger is a label or an explicit
# "a drawing shows" rather than the mere words "representation" and "show".
_INSTANCE = re.compile(
    r"(?<![A-Za-z])(?:Representation|Drawing|Beaker)s?\s+(?:[A-Z](?![a-z])|\d)")
_COUNTED = re.compile(
    r"(?<![a-z])(?:a|two|each|the)\s+drawings?\s+(?:of\s[^.]{0,40})?"
    r"(?:shows?|each\s+shows?)(?![a-z])", re.I)
_DIGITS = re.compile(r"\d+")

_EXCLUDED = re.compile(
    r"(?<![A-Za-z])(molality|percent by mass|percent by volume|colligative)(?![A-Za-z])",
    re.I)
_DISOWNED = re.compile(
    r"(?<![a-z])(outside the exam|will not be assessed|not be assessed|"
    r"exclusion statement|is not something the framework says|does not communicate)"
    r"(?![a-z])", re.I)

# Items that ask whether a drawing of a dissolved ionic compound is right.
ION_ITEMS = (14, 15, 20, 21, 22)
_STATED_RATIO = re.compile(
    r"(?<![a-z])provides\s+(\d+)\s+cations?\s+and\s+(\d+)\s+anions?(?![a-z])", re.I)


def _facing(item):
    out = [item["q"], item["why"]] + list(item["choices"])
    t = item.get("table")
    if t:
        out += [str(x) for x in t["headers"]]
        out += [str(c) for r in t["rows"] for c in r]
    return out


def no_deictic_reference(module):
    """Nothing may point at a picture, because there is no picture."""
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in _facing(item):
            hit = _DEICTIC.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: points at something with {hit.group(0)!r}, and "
                f"this bank shows no images -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} figures: no item points at a drawing; every drawing is "
          "described in words or tabulated.")


def described_representations_carry_their_numbers(module):
    """A stem that says a representation shows something must supply what it shows."""
    described, qualitative = [], []
    for i, item in enumerate(module.QUESTIONS, 1):
        stem = item["q"]
        if not (_INSTANCE.search(stem) or _COUNTED.search(stem)):
            qualitative.append(i)
            continue
        described.append(i)
        if item.get("table"):
            continue
        counts = _DIGITS.findall(stem)
        assert len(counts) >= 2, (
            f"{module.TOPIC[0]} q{i}: the stem says a representation shows something but "
            f"carries neither a table nor the counts in figures, so there is nothing for a "
            f"student to read -- {stem[:100]!r}"
        )
    assert len(described) >= 4, (
        f"only {len(described)} stem(s) describe a specific representation, so this check "
        "has almost nothing to read and proves little"
    )
    print(f"OK  {module.TOPIC[0]} descriptions: item(s) {described} put a specific "
          f"representation in front of the student and each supplies it as a table or as "
          f"counts; the remaining {len(qualitative)} item(s) are qualitative.")


def ion_items_state_their_ratio(module):
    """Deciding a formula's dissociation is units 2 and 4; the stem must supply it."""
    for i in ION_ITEMS:
        stem = module.QUESTIONS[i - 1]["q"]
        hit = _STATED_RATIO.search(stem)
        assert hit, (
            f"{module.TOPIC[0]} q{i}: the stem asks whether a drawing shows the right "
            f"relative amounts of ions but never states how many of each a formula unit "
            f"provides -- {stem[:100]!r}"
        )
        a, b = int(hit.group(1)), int(hit.group(2))
        assert a >= 1 and b >= 1, f"{module.TOPIC[0]} q{i}: the stated ratio {a}:{b} is not usable"
    print(f"OK  {module.TOPIC[0]} stoichiometry: all {len(ION_ITEMS)} ion items state the "
          "cation-to-anion ratio in the stem rather than relying on unit 2 or unit 4 "
          "knowledge.")


def excluded_only_when_disowned(module):
    """Colligative properties and the excluded calculations may be keyed only as excluded."""
    present, keyed = [], []
    for i, item in enumerate(module.QUESTIONS, 1):
        for k, choice in enumerate(item["choices"]):
            if not _EXCLUDED.search(choice):
                continue
            present.append((i, k))
            if k != item["ans"]:
                continue
            assert _DISOWNED.search(item["q"]), (
                f"{module.TOPIC[0]} q{i}: the key states an excluded measure ({choice!r}) "
                f"but the stem does not frame it as excluded or as something a "
                f"representation does not communicate -- stem {item['q'][:80]!r}"
            )
            keyed.append(i)
    assert len(present) >= 3, (
        f"the excluded measures appear only {len(present)} time(s), so this check has almost "
        "nothing to distinguish and proves little"
    )
    print(f"OK  {module.TOPIC[0]} exclusions: the excluded measures appear at {present}, "
          f"keyed only at item(s) {keyed}, where the stem asks what is out of scope.")


SWAP_ITEMS = {
    29: ("numbers of particles drawn communicate concentration",
         "arrangement of solvent around solute particles communicates interactions"),
}


def swap_anchors_carry_both_clauses(module, claims):
    for i, (clause_a, clause_b) in sorted(SWAP_ITEMS.items()):
        anchor = claims[i - 1][0]
        item = module.QUESTIONS[i - 1]
        has_a = cg.contains_phrase(anchor, clause_a)
        has_b = cg.contains_phrase(anchor, clause_b)
        assert has_a and has_b, (
            f"{module.TOPIC[0]} q{i}: the anchor {anchor!r} must name both {clause_a!r} and "
            f"{clause_b!r}; it carries "
            f"{'only the first' if has_a else 'only the second' if has_b else 'neither'}"
        )
        half = [k for k, c in enumerate(item["choices"])
                if k != item["ans"]
                and cg.contains_phrase(c, clause_a) != cg.contains_phrase(c, clause_b)]
        assert half, (
            f"{module.TOPIC[0]} q{i}: no distractor carries exactly one of the two clauses, "
            "so this item is not the half-swap case the check is for"
        )
    print(f"OK  {module.TOPIC[0]} swap guard: {len(SWAP_ITEMS)} anchor(s) carry both halves "
          "of the pairing, with a half-swapped distractor present.")


# ------------------------------------------------------------------ arithmetic

def n8(item):
    p, q = 5.0 / 25.0, 5.0 / 50.0
    assert abs(p - 0.20) < 1e-12 and abs(q - 0.10) < 1e-12, f"the ratios recompute to {p}, {q}"
    assert p > q, "the stated counts must make the first drawing the more concentrated"
    h.shows(item, "Representation P")
    return (f"5 solute among 25 solvent recomputes to {p:g} and 5 among 50 to {q:g}, so the "
            "first drawing is the more concentrated")


def n9(item):
    first, second = 8.0 / 100.0, 8.0 / 200.0
    assert abs(first - 0.08) < 1e-12 and abs(second - 0.04) < 1e-12, (
        f"the concentrations recompute to {first}, {second}"
    )
    assert first > second, "equal counts in a larger depicted volume must be the more dilute"
    h.shows(item, "The first drawing")
    return (f"8 particles in 100 mL recomputes to {first:g} per mL against {second:g} per mL "
            "for the same count in 200 mL")


def n14(item):
    drawn_c, drawn_a = 6.0, 3.0
    stated_c, stated_a = 2.0, 1.0
    matches = abs(drawn_c / drawn_a - stated_c / stated_a) < 1e-12
    assert matches, f"6 to 3 does not reduce to the stated {stated_c:g} to {stated_a:g}"
    h.shows(item, "outnumber the drawn anions two to one")
    return (f"the drawn ratio {drawn_c / drawn_a:g} matches the stated "
            f"{stated_c / stated_a:g}, so the drawing is right")


def n15(item):
    drawn_c, drawn_a = 5.0, 3.0
    stated_c, stated_a = 2.0, 1.0
    matches = abs(drawn_c / drawn_a - stated_c / stated_a) < 1e-12
    assert not matches, (
        f"5 to 3 must NOT match the stated {stated_c:g} to {stated_a:g}, or the item has no "
        "answer"
    )
    assert drawn_c > drawn_a, (
        "the drawing must still show more cations than anions, or the item is answerable "
        "without forming the ratio"
    )
    h.shows(item, "five to three is not the stated two-to-one ratio")
    return (f"the drawn ratio {drawn_c / drawn_a:.4g} misses the stated "
            f"{stated_c / stated_a:g} while still favouring the cation, so only the ratio "
            "settles it")


NUMERIC = {8: n8, 9: n9, 14: n14, 15: n15}


# ----------------------------------------------------------------- table items

def _rep_ratios(table):
    return {lab: cg.cell(table, lab, SOLUTE) / cg.cell(table, lab, SOLVENT)
            for lab in cg.labels(table)}


def _unique_extreme(mapping, want_max, what):
    pick = (max if want_max else min)(mapping, key=mapping.get)
    tied = [k for k, v in mapping.items() if abs(v - mapping[pick]) < 1e-12]
    assert tied == [pick], f"the {what} is not unique: {tied} in {mapping}"
    return pick


def q16(table, item):
    rs = _rep_ratios(table)
    top = _unique_extreme(rs, True, "most concentrated tabulated representation")
    assert top == "Representation 2", f"the most concentrated tabulated row is {top}: {rs}"
    solutes = dict(zip(cg.labels(table), cg.col(table, SOLUTE)))
    solvents = dict(zip(cg.labels(table), cg.col(table, SOLVENT)))
    assert len(set(solvents.values())) > 1, (
        "the tabulated solvent counts must differ somewhere, or the ratio adds nothing to "
        "reading the solute column"
    )
    h.shows(item, top)
    return (f"the tabulated ratios recompute as {rs} from solute counts {solutes} and solvent "
            f"counts {solvents}, with a unique maximum at {top}")


def q17(table, item):
    rs = {lab: round(v, 9) for lab, v in _rep_ratios(table).items()}
    groups = {}
    for lab, v in rs.items():
        groups.setdefault(v, []).append(lab)
    shared = sorted(g for g in groups.values() if len(g) > 1)
    assert shared == [["Representation 3", "Representation 4"]], (
        f"exactly one tabulated pair may share a ratio; the grouping is {groups}"
    )
    pair = shared[0]
    assert (cg.cell(table, pair[0], SOLUTE) != cg.cell(table, pair[1], SOLUTE)
            and cg.cell(table, pair[0], SOLVENT) != cg.cell(table, pair[1], SOLVENT)), (
        "the matching pair must differ in BOTH columns, or the item can be answered without "
        "forming either ratio"
    )
    nums = [str(lab).split()[-1] for lab in pair]
    h.shows(item, f"Representations {nums[0]} and {nums[1]}")
    return (f"the tabulated ratios group as {groups}, with exactly one pair sharing a value "
            "while differing in both columns")


def q18(table, item):
    rs = _rep_ratios(table)
    target = 2.0 * rs["Representation 1"]
    hits = [lab for lab in rs
            if lab != "Representation 1" and abs(rs[lab] - target) < 1e-12]
    assert hits == ["Representation 2"], f"the rows at twice the reference ratio are {hits}: {rs}"
    h.shows(item, hits[0])
    return (f"twice the reference tabulated ratio is {target:g}, matched by exactly one other "
            f"row, {hits[0]}, among {rs}")


def q19(table, item):
    rs = _rep_ratios(table)
    above = sorted(lab for lab, v in rs.items() if v > 0.10 + 1e-12)
    assert above == ["Representation 1", "Representation 2"], (
        f"the rows above one in ten are {above}: {rs}"
    )
    word = {0: "None of them", 1: "Exactly one", 2: "Exactly two", 3: "Exactly three",
            4: "All four"}[len(above)]
    h.shows(item, word)
    return (f"the tabulated ratios recompute as {rs}, of which {len(above)} exceed the stated "
            f"one-in-ten threshold: {above}")


def _ion_pick(table, stem):
    hit = _STATED_RATIO.search(stem)
    assert hit, "the stem must state the cation-to-anion ratio"
    want = int(hit.group(1)) / int(hit.group(2))
    rs = {lab: cg.cell(table, lab, CATIONS) / cg.cell(table, lab, ANIONS)
          for lab in cg.labels(table)}
    hits = sorted(lab for lab, v in rs.items() if abs(v - want) < 1e-9)
    assert len(hits) == 1, (
        f"exactly one tabulated drawing must show the stated ratio {want:g}; {hits} do, "
        f"from {rs}"
    )
    return hits[0], rs, want


def q20(table, item):
    lab, rs, want = _ion_pick(table, item["q"])
    assert lab == "Drawing W", f"the two-to-one tabulated drawing is {lab}: {rs}"
    h.shows(item, lab)
    return (f"the stem states a cation-to-anion ratio of {want:g} and the tabulated ratios "
            f"{rs} match it at exactly one row, {lab}")


def q21(table, item):
    lab, rs, want = _ion_pick(table, item["q"])
    assert lab == "Drawing Z", f"the one-to-three tabulated drawing is {lab}: {rs}"
    h.shows(item, lab)
    return (f"the stem states a cation-to-anion ratio of {want:.4g} and the tabulated ratios "
            f"{rs} match it at exactly one row, {lab}")


def q22(table, item):
    lab, rs, want = _ion_pick(table, item["q"])
    assert lab == "Drawing Y", f"the one-to-one tabulated drawing is {lab}: {rs}"
    h.shows(item, lab)
    return (f"the stem states a cation-to-anion ratio of {want:g} and the tabulated ratios "
            f"{rs} match it at exactly one row, {lab}")


def _densities(table):
    return {lab: cg.cell(table, lab, SOLUTE) / cg.cell(table, lab, BEAKVOL)
            for lab in cg.labels(table)}


def q23(table, item):
    ds = _densities(table)
    top = _unique_extreme(ds, True, "most concentrated tabulated beaker")
    assert top == "Beaker D", f"the most concentrated tabulated beaker is {top}: {ds}"
    solutes = dict(zip(cg.labels(table), cg.col(table, SOLUTE)))
    assert max(solutes, key=solutes.get) == top, (
        "the item is still sound if these agree, but the volumes must differ or the division "
        f"is idle: {solutes} against {ds}"
    )
    vols = dict(zip(cg.labels(table), cg.col(table, BEAKVOL)))
    assert len(set(vols.values())) > 1, "the tabulated volumes must differ"
    h.shows(item, top)
    return (f"the tabulated particles-per-millilitre recompute as {ds} from counts {solutes} "
            f"and volumes {vols}, with a unique maximum at {top}")


def q24(table, item):
    ds = _densities(table)
    low = _unique_extreme(ds, False, "most dilute tabulated beaker")
    assert low == "Beaker B", f"the most dilute tabulated beaker is {low}: {ds}"
    solutes = dict(zip(cg.labels(table), cg.col(table, SOLUTE)))
    fewest = [lab for lab, v in solutes.items() if abs(v - min(solutes.values())) < 1e-12]
    assert len(fewest) > 1 or fewest != [low], (
        "the most dilute row must NOT be identifiable by the particle count alone, or the "
        f"item does not test the division: {solutes} against {ds}"
    )
    h.shows(item, low)
    return (f"the tabulated particles-per-millilitre recompute as {ds}, whose unique minimum "
            f"is at {low}, while the smallest particle count alone points at {fewest}")


def q25(table, item):
    ds = _densities(table)
    target = 2.0 * ds["Beaker A"]
    hits = [lab for lab in ds if lab != "Beaker A" and abs(ds[lab] - target) < 1e-12]
    assert hits == ["Beaker C"], f"the beakers at twice the reference density are {hits}: {ds}"
    h.shows(item, hits[0])
    return (f"twice the reference tabulated density is {target:g} particles per millilitre, "
            f"matched by exactly one other beaker, {hits[0]}, among {ds}")


def q26(table, item):
    ds = _densities(table)
    above = sorted(lab for lab, v in ds.items() if v > ds["Beaker A"] + 1e-12)
    assert above == ["Beaker C", "Beaker D"], f"the beakers above the reference are {above}: {ds}"
    word = {0: "None of them", 1: "Exactly one", 2: "Exactly two", 3: "Exactly three"}[
        len(above)]
    h.shows(item, word)
    return (f"the tabulated densities recompute as {ds}, of which {len(above)} exceed the "
            f"reference beaker's: {above}")


TABLE_CHECKS = {16: q16, 17: q17, 18: q18, 19: q19, 20: q20, 21: q21, 22: q22,
                23: q23, 24: q24, 25: q25, 26: q26}


CLAIMS = [
 ("The structure and properties of solutions",
  "EK 3.8.A.1 opens by saying particulate representations of solutions communicate the structure and properties of solutions."),
 ("illustrating the relative concentrations of the components, and by drawings that show interactions among the components",
  "EK 3.8.A.1 names exactly those two means, and both are things a particle-scale picture can carry."),
 ("Colligative properties",
  "One of the exclusion statements attached to EK 3.8.A.1 says colligative properties will not be assessed on the AP Exam; the rejected options are named in the statement itself as this topic's content."),
 ("Calculations of molality, percent by mass, and percent by volume for solutions",
  "The second exclusion statement attached to EK 3.8.A.1 names those three specifically, and pointedly not molarity, which learning objective 3.7.A requires."),
 ("Represent interactions between components",
  "Learning objective 3.8.A's first part, backed by EK 3.8.A.1's mention of drawings that show interactions among the components."),
 ("Represent concentrations of components",
  "Learning objective 3.8.A's second part, backed by EK 3.8.A.1's mention of illustration of the relative concentrations of the components."),
 ("more solute particles in the same depicted volume",
  "EK 3.8.A.1 makes illustration of relative concentrations one of the two things such a drawing does, and at a fixed depicted volume that is carried by how many solute particles appear."),
 ("Representation P",
  "EK 3.8.A.1's relative concentration is formed within each drawing. Recomputed in n8 from the stated counts."),
 ("The first drawing",
  "EK 3.8.A.1's concentration is an amount per volume, so equal counts in a larger depicted volume are the more dilute. Recomputed in n9."),
 ("Drawings that show interactions among the components",
  "EK 3.8.A.1 names that as one of its two means, and EK 3.1.A.3 makes the orientation of a solvent dipole toward an ion the qualitative content of such an interaction."),
 ("The percent by mass of the solute",
  "EK 3.8.A.1 names structure, properties, relative concentrations and interactions, and an exclusion statement attached to it puts calculations of percent by mass outside the exam."),
 ("shows how the components' amounts compare with one another",
  "EK 3.8.A.1's phrase is the RELATIVE concentrations of the components in the solution, which is a comparison among the things drawn rather than a measured value."),
 ("may illustrate relative concentrations, show interactions, or do both",
  "EK 3.8.A.1 joins its two means with and/or, which permits either alone as well as the two together."),
 ("outnumber the drawn anions two to one",
  "EK 3.8.A.1 makes the relative amounts of the components the drawing's content and the stem supplies the ratio. Recomputed in n14."),
 ("five to three is not the stated two-to-one ratio",
  "The stem supplies the ratio the drawing must match. Recomputed in n15, which also checks the drawing still shows more cations than anions, so only the ratio settles it."),
 ("Representation 2",
  "EK 3.8.A.1's relative concentration formed within each tabulated row. q16 recomputes all four and checks the maximum is unique."),
 ("Representations 3 and 4",
  "A ratio can agree while both counts differ. q17 recomputes all four, checks exactly one pair matches, and checks that pair differs in both columns."),
 ("Representation 2",
  "Twice a ratio is still a ratio. q18 recomputes the reference row, doubles it, and checks exactly one other row matches."),
 ("Exactly two",
  "EK 3.8.A.1's relative concentration compared with a stated threshold row by row. Recomputed in q19."),
 ("Drawing W",
  "EK 3.8.A.1 makes matching the stated relative amounts the drawing's job. q20 reads the ratio out of the stem and checks exactly one tabulated row shows it."),
 ("Drawing Z",
  "The same check with a different stated ratio, read out of the stem by the same code. Recomputed in q21."),
 ("Drawing Y",
  "The same check with a one-to-one stated ratio. Recomputed in q22."),
 ("Beaker D",
  "Concentration is an amount per volume, so the tabulated count is divided by the tabulated volume. q23 recomputes all four and checks the volumes differ so the division does real work."),
 ("Beaker B",
  "The same division read the other way. q24 recomputes all four and checks the answer is NOT the row with the fewest particles, so the item cannot be got right by reading one column."),
 ("Beaker C",
  "Twice a concentration is twice an amount per volume, which doubling the particle count alone would not give if the volume doubled too. Recomputed in q25."),
 ("Exactly two",
  "Each tabulated density compared with the reference row's. Recomputed in q26."),
 ("partially negative ends turned toward a cation",
  "EK 3.8.A.1 names drawings that show interactions, and EK 3.1.A.3 says the orientation dependence of ion-dipole forces is understood from the sign of the partial charges and how they interact with an ion; a cation is positive, so the negative end faces it."),
 ("fewer solute particles for the same number of solvent particles",
  "EK 3.8.A.1 has the drawing carry the relative concentrations of the components, and the dilute member of a pair carries less solute for the same solvent."),
 ("The relative numbers of particles drawn communicate concentration, and the arrangement of solvent around solute particles communicates interactions",
  "EK 3.8.A.1 pairs illustration of relative concentrations with how much of each component is present, and drawings that show interactions with how the components act on one another. The pairing is stated in full because exchanging the two keeps every word and makes it false."),
 ("communicate the structure and properties of solutions, by illustrating relative concentrations of the components and by showing interactions among them",
  "EK 3.8.A.1's three parts in one statement: what is communicated, and the two means by which it is communicated."),
]


def _extra_mutations():
    def deictic_creeps_in(mod, cl):
        mod.QUESTIONS[15]["q"] = ("Which of the representations shown above is the most "
                                  "concentrated?")
        no_deictic_reference(mod)

    def bare_pointing_word(mod, cl):
        mod.QUESTIONS[0]["q"] = mod.QUESTIONS[0]["q"] + " Use the drawing below to decide."
        no_deictic_reference(mod)

    def described_drawing_loses_its_numbers(mod, cl):
        mod.QUESTIONS[7]["q"] = ("Representation P shows some solute particles among many "
                                 "solvent particles, and Representation Q shows the same "
                                 "solute among more solvent. Which is more concentrated?")
        described_representations_carry_their_numbers(mod)

    def no_stem_describes_a_representation(mod, cl):
        # A control on the CONTROL: strip every label and every "a drawing
        # shows", and nothing is left referring to a particular drawing, so the
        # check would read nothing and pass over an empty set.
        for item in mod.QUESTIONS:
            q = _INSTANCE.sub("one such view", item["q"])
            item["q"] = _COUNTED.sub("one such view indicates", q)
        described_representations_carry_their_numbers(mod)

    def ion_stem_drops_its_ratio(mod, cl):
        mod.QUESTIONS[19]["q"] = ("For a dissolved ionic compound, which tabulated drawing "
                                  "represents its solution correctly?")
        ion_items_state_their_ratio(mod)

    def excluded_measure_keyed_plainly(mod, cl):
        # The excluded measure keyed under a stem that does NOT disown it.
        ch = list(mod.QUESTIONS[0]["choices"])
        ch[0] = "The percent by mass of every component"
        mod.QUESTIONS[0]["choices"] = ch
        cl[0] = ("The percent by mass of every component", cl[0][1])
        excluded_only_when_disowned(mod)

    def disowning_stem_rewritten(mod, cl):
        mod.QUESTIONS[10]["q"] = ("Which of the following does a particulate representation "
                                  "of a solution communicate?")
        excluded_only_when_disowned(mod)

    def excluded_measures_removed(mod, cl):
        for item in mod.QUESTIONS:
            item["choices"] = [_EXCLUDED.sub("mole fraction", c) for c in item["choices"]]
        excluded_only_when_disowned(mod)

    def pairing_anchor_halved(mod, cl):
        cl[28] = ("numbers of particles drawn communicate concentration", cl[28][1])
        swap_anchors_carry_both_clauses(mod, cl)

    def rep_table_ties(mod, cl):
        mod.QUESTIONS[15]["table"] = dict(
            headers=h3_8._T_REP["headers"],
            rows=[["Representation 1", "8", "20"], ["Representation 2", "8", "20"],
                  ["Representation 3", "2", "20"], ["Representation 4", "4", "40"]])

    def rep_table_solvents_flattened(mod, cl):
        # Every drawing given the same solvent count: the ratio adds nothing to
        # reading the solute column, so the item no longer tests what it claims.
        mod.QUESTIONS[15]["table"] = dict(
            headers=h3_8._T_REP["headers"],
            rows=[["Representation 1", "4", "20"], ["Representation 2", "8", "20"],
                  ["Representation 3", "2", "20"], ["Representation 4", "6", "20"]])

    def second_matching_rep_pair(mod, cl):
        mod.QUESTIONS[16]["table"] = dict(
            headers=h3_8._T_REP["headers"],
            rows=[["Representation 1", "4", "20"], ["Representation 2", "8", "40"],
                  ["Representation 3", "2", "20"], ["Representation 4", "4", "40"]])

    def ion_table_gains_a_second_match(mod, cl):
        mod.QUESTIONS[19]["table"] = dict(
            headers=h3_8._T_IONS["headers"],
            rows=[["Drawing W", "6", "3"], ["Drawing X", "4", "2"],
                  ["Drawing Y", "4", "4"], ["Drawing Z", "2", "6"]])

    def beaker_dilute_readable_from_one_column(mod, cl):
        # The most dilute beaker made also the one with the fewest particles: the
        # item can then be answered without dividing by the volume at all.
        mod.QUESTIONS[23]["table"] = dict(
            headers=h3_8._T_CONC["headers"],
            rows=[["Beaker A", "100", "10"], ["Beaker B", "100", "4"],
                  ["Beaker C", "100", "20"], ["Beaker D", "200", "60"]])

    def beaker_volumes_changed(mod, cl):
        mod.QUESTIONS[24]["table"] = dict(
            headers=h3_8._T_CONC["headers"],
            rows=[["Beaker A", "100", "10"], ["Beaker B", "200", "10"],
                  ["Beaker C", "200", "20"], ["Beaker D", "200", "60"]])

    return [
        ("a stem pointing at representations shown somewhere", deictic_creeps_in),
        ("a bare pointing word added to a stem", bare_pointing_word),
        ("a described drawing stripped of its counts", described_drawing_loses_its_numbers),
        ("no stem left describing a specific drawing, so that check would read nothing",
         no_stem_describes_a_representation),
        ("an ion item stripped of the ratio its stem must supply", ion_stem_drops_its_ratio),
        ("an excluded measure keyed under a stem that does not disown it",
         excluded_measure_keyed_plainly),
        ("the disowning stem rewritten so the excluded key becomes an assertion",
         disowning_stem_rewritten),
        ("every excluded measure removed, so that check would run over an empty set",
         excluded_measures_removed),
        ("the pairing anchor cut to one clause", pairing_anchor_halved),
        ("two tabulated representations tied for the highest ratio", rep_table_ties),
        ("every tabulated solvent count made equal, so the ratio does no work",
         rep_table_solvents_flattened),
        ("a second tabulated pair made to share a ratio", second_matching_rep_pair),
        ("a second tabulated drawing made to show the stated ion ratio",
         ion_table_gains_a_second_match),
        ("the most dilute beaker made readable from the particle count alone",
         beaker_dilute_readable_from_one_column),
        ("a tabulated beaker volume changed under the twice-the-concentration key",
         beaker_volumes_changed),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h3_8, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

no_deictic_reference(h3_8)
described_representations_carry_their_numbers(h3_8)
ion_items_state_their_ratio(h3_8)
excluded_only_when_disowned(h3_8)
swap_anchors_carry_both_clauses(h3_8, CLAIMS)
h.run(h3_8, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
