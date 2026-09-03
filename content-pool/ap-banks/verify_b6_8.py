"""Key audit for AP BIOLOGY 6.8 Biotechnology.

One (anchor, claim) per item, in module order. ``cg_check.check`` is the
structural gate; it is described in ``verify_b5_3.py``.

THE FIGURE RULE IS ENFORCED HERE, NOT JUST OBSERVED. SCIENCE_BRIEF.md names 6.8
as one of the two topics that tempt an author into referring to a picture the
bank cannot show, and a gel is the obvious one. The scan at the bottom of this
file fails if any stem contains a phrase that promises a figure -- "the gel
shown", "in the diagram", "the bands above" and their relatives -- and it
carries a positive control so it cannot silently stop matching. It also fails on
any stem that says "gel" while carrying no table, since a gel result with no
data behind it is exactly the defect the brief describes.

WHAT IS RECOMPUTED. The gel calibration is recomputed as a strictly decreasing
relation between length and distance, and the unknown fragment is bracketed by
finding the two references its migration falls between -- not by recalling which
way a gel runs, which would be one of the technique details the CED's exclusion
statement bars. The fingerprint item is recomputed by parsing each sample's
fragment lengths into a set and comparing sets. The amplification item is
recomputed as a doubling series extended to ten cycles. The transformation,
sequence comparison and quantity items are recomputed from their own numbers,
including that the rejected reading is false on the same data.

THE EXCLUSION STATEMENT. "Knowledge of the details of each of these genetic
engineering techniques is beyond the scope of the AP Exam." ``DETAILS`` below
lists the details this topic tempts an author into, and the scan fails if one
appears.

NEGATIVE CONTROL: ``negcontrol_b5_7.py``.
"""
import re

import cg_check as cg
import b6_8

T_GEL = b6_8._T_GEL
T_GEL2 = b6_8._T_GEL2
T_FINGER = b6_8._T_FINGER
T_PCR = b6_8._T_PCR
T_TRANSFORM = b6_8._T_TRANSFORM
T_SEQCOMP = b6_8._T_SEQCOMP
T_AMOUNT = b6_8._T_AMOUNT

# Phrases that promise a picture this bank cannot supply.
FIGURE_PHRASES = ("the gel shown", "gel shown below", "in the diagram", "the diagram shows",
                  "the figure shows", "in the figure", "the bands shown", "shown above",
                  "shown below", "the image", "as illustrated", "the following diagram")
# Technique details the CED's exclusion statement puts beyond the scope.
DETAILS = ("agarose", "taq", "thermocycler", "ethidium", "restriction enzyme",
           "ecori", "buffer", "electrode", "sanger", "dideoxy", "voltage")


def _rows(table):
    heads = [cg.normalize(h) for h in table["headers"]]
    return [dict(zip(heads, r)) for r in table["rows"]]


LEN = "length in base pairs"
DIST = "distance moved through the gel millimeters"


def _calibration(table):
    """Reference fragments as (length, distance), longest first, checked monotonic."""
    refs = []
    for r in _rows(table):
        raw = str(r[LEN]).strip()
        if not re.fullmatch(r"[0-9]+", raw):
            continue                      # the unknown fragment, whose length is not given
        refs.append((float(raw), cg.num(r[DIST])))
    assert len(refs) >= 4, f"a calibration needs at least four references; found {len(refs)}"
    refs.sort()
    dists = [d for _, d in refs]
    assert dists == sorted(dists, reverse=True), \
        f"distance must fall as length rises for the separation to be readable: {refs}"
    assert len(set(dists)) == len(dists), "two references must not have moved the same distance"
    return refs


def q2(table, item):
    refs = _calibration(table)
    assert all(str(r[LEN]).strip().isdigit() for r in _rows(table)), \
        "every fragment in this table must have a stated length"
    shortest, longest = refs[0], refs[-1]
    assert longest[1] < shortest[1], "the longest fragment must have moved the shortest distance"
    assert shortest[1] > 2 * longest[1], "the difference must be large enough to call a relationship"
    return (f"length rises {shortest[0]:.0f} to {longest[0]:.0f} base pairs while distance falls "
            f"{shortest[1]:.0f} to {longest[1]:.0f} millimeters, strictly, across {len(refs)} fragments")


def q3(table, item):
    refs = _calibration(table)
    unknown = [cg.num(r[DIST]) for r in _rows(table)
               if not re.fullmatch(r"[0-9]+", str(r[LEN]).strip())]
    assert len(unknown) == 1, f"expected exactly one fragment of unstated length; found {len(unknown)}"
    d = unknown[0]
    below = [(L, dist) for L, dist in refs if dist > d]     # shorter fragments, moved further
    above = [(L, dist) for L, dist in refs if dist < d]     # longer fragments, moved less
    assert below and above, f"the unknown at {d} millimeters is not bracketed by the references"
    # the nearest reference on each side, measured by migration distance
    near_below = min(below, key=lambda p: p[1])   # shortest of those that moved further
    near_above = max(above, key=lambda p: p[1])   # longest of those that moved less
    lo, hi = near_below[0], near_above[0]
    assert (lo, hi) == (1000, 2000), f"the unknown brackets to between {lo} and {hi}, not 1000 and 2000"
    return (f"the unknown moved {d:.0f} millimeters, between the {lo:.0f} base pair reference at "
            f"{near_below[1]:.0f} and the {hi:.0f} base pair reference at {near_above[1]:.0f}, "
            f"so its length lies between those two lengths")


def q4(table, item):
    sets = {}
    for r in _rows(table):
        nums = re.findall(r"(?<![0-9])[0-9]+(?![0-9])", r["lengths of the fragments detected in base pairs"])
        assert len(nums) == 3, f"each sample should list three fragment lengths; got {nums}"
        sets[cg.normalize(r["sample"])] = frozenset(int(n) for n in nums)
    evidence = sets["evidence sample"]
    people = {k: v for k, v in sets.items() if k != "evidence sample"}
    matches = sorted(k for k, v in people.items() if v == evidence)
    assert matches == ["person 1"], f"the matching sample is {matches}"
    overlaps = {k: len(v & evidence) for k, v in people.items()}
    assert all(0 < n < 3 for k, n in overlaps.items() if k not in matches), \
        f"each non-matching sample must share some but not all fragments: {overlaps}"
    return (f"the evidence set is {sorted(evidence)}; {matches} matches it exactly and the others "
            f"overlap it at {[(k, n) for k, n in overlaps.items() if k not in matches]}")


def q8(table, item):
    pairs = [(cg.num(r["number of cycles completed"]), cg.num(r["number of copies of the fragment"]))
             for r in _rows(table)]
    for n, c in pairs:
        assert c == 2 ** int(n), f"cycle {n:.0f} records {c:.0f} copies; doubling gives {2 ** int(n)}"
    ten = 2 ** 10
    assert ten == 1024, "the ten-cycle total must recompute to 1024"
    nearest = min([1000, 20, 100, 10000, 40], key=lambda v: abs(v - ten))
    assert nearest == 1000, f"the listed value nearest {ten} is {nearest}"
    return f"the table doubles at every cycle and ten doublings from one copy give {ten}"


def q10(table, item):
    rows = _rows(table)
    col = "number of colonies growing on the selective medium"
    by_flag = {cg.normalize(r["bacteria treated with the foreign dna"]): cg.num(r[col])
               for r in rows}
    assert set(by_flag) == {"yes", "no"}, f"the two plates are marked {set(by_flag)}"
    assert by_flag["yes"] > 0, "the treated plate must show colonies"
    assert by_flag["no"] == 0, \
        "the untreated plate must show none, or the DNA could already have been present"
    return (f"{by_flag['yes']:.0f} colonies on the treated plate and {by_flag['no']:.0f} on the "
            f"untreated one, so growth followed the treatment")


def q17(table, item):
    d = {cg.normalize(r["pair of species compared"]):
         cg.num(r["number of nucleotide differences found in the same gene"])
         for r in _rows(table)}
    closest = min(d, key=d.get)
    assert closest == "species a and species b", f"the fewest differences belong to {closest}"
    others = sorted(v for k, v in d.items() if k != closest)
    assert others[0] > 3 * d[closest], \
        f"the closest pair must be clearly closest; got {d}"
    assert len(set(d.values())) == len(d), "no two pairs may tie"
    return f"the three counts are {d}; the smallest is {d[closest]:.0f} and the next is {others[0]:.0f}"


def q21(table, item):
    rows = _rows(table)
    col = "amount of the dna fragment detected arbitrary units"
    by_flag = {cg.normalize(r["amplified before measurement"]): cg.num(r[col]) for r in rows}
    assert set(by_flag) == {"yes", "no"}, f"the two samples are marked {set(by_flag)}"
    assert by_flag["yes"] > 100 * by_flag["no"], \
        f"the amplified sample reads {by_flag['yes']} against {by_flag['no']}; the key needs a large rise"
    assert by_flag["no"] > 0, "the unamplified sample must be measurable, not absent"
    return (f"the amount rises from {by_flag['no']:.0f} to {by_flag['yes']:.0f} units after "
            f"amplification, more than a hundredfold")


CLAIMS = [
 ("separates the fragments by size and charge",
  "EK 6.8.A.1.i states that gel electrophoresis is a process that separates DNA fragments by size and charge. Amplifying, sequencing and introducing DNA are the roles EK 6.8.A.1.ii, iv and iii give to the other three techniques."),
 ("the shorter the distance it moved",
  "EK 6.8.A.1.i states that gel electrophoresis separates DNA fragments by size and charge; how the separation ran in this experiment is in the data. The table check confirms distance falls strictly as length rises across all four references, so the relationship is read off rather than recalled."),
 ("Between 1000 and 2000 base pairs",
  "EK 6.8.A.1.i makes gel electrophoresis a separation by size, so references of known length calibrate it. The table check brackets the unknown's migration between the two references it falls between and confirms which lengths those are, without assuming which way the separation runs."),
 ("Person 1",
  "EK 6.8.A.1.iv states that these techniques typically result in a DNA fingerprint allowing the comparison of DNA sequences from various samples, and forensic identification is one of the CED's illustrative examples for EK 6.8.A.1. The table check parses each sample's fragment lengths into a set and confirms exactly one matches the evidence set while the others overlap it only partly."),
 ("amplifies DNA fragments, producing many copies",
  "EK 6.8.A.1.ii states that during the polymerase chain reaction DNA fragments are amplified. Intron removal is a cellular process under EK 6.3.A.4.iii rather than a laboratory technique."),
 ("Denaturing the DNA, annealing primers to the original strand, and extending",
  "EK 6.8.A.1.ii names exactly these three steps as the way fragments are amplified. The rejected options import steps belonging to other techniques or to processes inside a cell."),
 ("a primer can only anneal to a strand that has been separated",
  "EK 6.8.A.1.ii lists the three steps in that order and each supplies what the next requires; EK 6.2.A.1.ii makes a single strand the thing a complementary strand is built on, and extension by definition lengthens something already annealed."),
 ("About 1000 copies",
  "EK 6.8.A.1.ii states that fragments are amplified in the polymerase chain reaction. The table check confirms the recorded counts are the doubling series and recomputes ten doublings from one copy as 1024, then confirms which listed value is nearest it."),
 ("introduces foreign DNA into bacterial cells",
  "EK 6.8.A.1.iii states exactly this for bacterial transformation. The rejected options reverse it or import the roles EK 6.8.A.1.i and iv give to other techniques."),
 ("introduced the foreign DNA into some of the bacterial cells",
  "EK 6.8.A.1.iii states that bacterial transformation introduces foreign DNA into bacterial cells, and skill 6.D asks what a result shows. The table check confirms colonies appeared only on the treated plate, which is what rules out the DNA having already been present."),
 ("order of the nucleotides in a DNA molecule",
  "EK 6.8.A.1.iv states that DNA sequencing technology determines the order of nucleotides in a DNA molecule. Counting copies is what amplification is for and separating by size and charge is EK 6.8.A.1.i's."),
 ("comparison of DNA sequences from various samples",
  "EK 6.8.A.1.iv states that these techniques typically result in a DNA fingerprint that allows for the comparison of DNA sequences from various samples."),
 ("DNA sequencing, which determines the order of nucleotides in a DNA molecule",
  "EK 6.8.A.1.iv assigns the determination of the order of nucleotides to sequencing technology; each of the other three techniques is defined by the framework as doing something else."),
 ("polymerase chain reaction, in which DNA fragments are amplified",
  "EK 6.8.A.1.ii states that DNA fragments are amplified in the polymerase chain reaction, which is the need described. Gene cloning, one of the CED's illustrative examples, likewise propagates fragments."),
 ("Gel electrophoresis, which separates DNA fragments by size and charge",
  "EK 6.8.A.1.i states this, and it is the operation the researcher needs. The other three techniques are defined as amplifying, introducing and reading DNA rather than separating it."),
 ("Bacterial transformation, which introduces foreign DNA into bacterial cells",
  "EK 6.8.A.1.iii states this, and gene cloning allowing propagation of DNA fragments is one of the CED's illustrative examples for EK 6.8.A.1, which depends on the DNA first being introduced."),
 ("Species A and species B",
  "EK 6.8.A.1.iv makes the comparison of DNA sequences from various samples what a fingerprint allows, and phylogenetic analysis from amplified fragments is one of the CED's illustrative examples. The table check confirms one pair has the fewest differences by a factor of more than three, with no tie."),
 ("fingerprint allowing comparison of DNA sequences from various samples",
  "EK 6.8.A.1.iv states this, and forensic identification is one of the CED's illustrative examples for EK 6.8.A.1. Separation and amplification may precede the comparison but neither is what licenses it."),
 ("transgenic animal, which carries DNA introduced from another source",
  "The CED prints among its illustrative examples for EK 6.8.A.1 that genetically modified organisms include transgenic animals. A seasonal coat change is EK 5.5.A.1's plasticity, a spontaneous mutation EK 6.7.B.1's, and differential expression EK 6.6.B.1's."),
 ("reproduced in quantity rather than being used up",
  "Gene cloning allowing propagation of DNA fragments is one of the CED's illustrative examples for EK 6.8.A.1, and to propagate a fragment is to produce more of it. Reading the nucleotide order is EK 6.8.A.1.iv's separate technique."),
 ("polymerase chain reaction, which amplifies DNA fragments",
  "EK 6.8.A.1.ii states that DNA fragments are amplified in the polymerase chain reaction. The table check recomputes a more than hundredfold rise in the amount detected after the treatment, and confirms the unamplified sample was measurable rather than absent."),
 ("starting point from which the new DNA molecule is extended",
  "EK 6.8.A.1.ii places annealing primers to the original strand between denaturing and extending the new DNA molecule, so what the extension step extends is the annealed primer. Separating the strands is the denaturing step of the same statement."),
 ("anneals to a single strand, and denaturing separates the two strands",
  "EK 6.8.A.1.ii names annealing primers to the original strand, and EK 6.2.A.1.ii makes a single strand the thing a complementary strand is built on, which is why denaturing is listed first."),
 ("nothing annealed to the original strand to extend",
  "EK 6.8.A.1.ii makes annealing primers one of the three steps by which fragments are amplified and makes the third step the extension of the new DNA molecule from what was annealed, so with nothing annealed the amplification cannot proceed."),
 ("separated by size and charge, while sequencing produces the order of the nucleotides",
  "EK 6.8.A.1.i assigns separation by size and charge to gel electrophoresis and EK 6.8.A.1.iv assigns the order of nucleotides to sequencing. Each rejected option exchanges the outputs the framework assigns to two techniques."),
 ("Amplify the fragment by the polymerase chain reaction, then determine the order",
  "EK 6.8.A.1.ii increases a scarce fragment, EK 6.8.A.1.iv determines the order of nucleotides, and the same statement makes comparison across samples what the resulting fingerprint allows. Comparing sequences requires the sequences to exist first."),
 ("illustrative uses the CED prints for genetic engineering techniques",
  "The CED prints among its illustrative examples for EK 6.8.A.1 that amplified DNA fragments can be used to identify organisms and perform phylogenetic analysis, and EK 6.8.A.1.iv supplies the comparison of sequences such an analysis rests on."),
 ("Analyze and manipulate DNA and RNA",
  "EK 6.8.A.1 states that genetic engineering techniques can be used to analyze and manipulate DNA and RNA, naming both kinds of activity and both nucleic acids; the four listed techniques are its examples."),
 ("places a fragment among others of known length",
  "EK 6.8.A.1.i confines gel electrophoresis to separating DNA fragments by size and charge, and EK 6.8.A.1.iv assigns the determination of the order of nucleotides to sequencing technology. The framework keeps the two results separate."),
 ("One separates fragments by size and charge, one amplifies fragments",
  "The four roles are stated separately in EK 6.8.A.1.i to iv and this option assigns each technique the role the framework gives it. EK 6.8.A.1 also covers RNA, so the option denying that misreports the scope."),
]

cg.check(b6_8, CLAIMS,
         table_checks={2: q2, 3: q3, 4: q4, 8: q8, 10: q10, 17: q17, 21: q21})

# --- the figure rule, enforced rather than trusted
for i, q in enumerate(b6_8.QUESTIONS, 1):
    text = " ".join([q["q"], *q["choices"]])
    for phrase in FIGURE_PHRASES:
        assert not cg.contains_phrase(text, phrase), (
            f"6.8 q{i}: {phrase!r} promises a figure this bank cannot show"
        )
    # A band pattern IS a picture, whatever the sentence around it says.
    for word in ("band", "bands", "lane", "lanes"):
        assert not cg.contains_phrase(text, word), (
            f"6.8 q{i}: {word!r} describes a gel image this bank cannot show; put the fragment "
            f"lengths in a table instead"
        )
    # Naming the technique is fine; reporting a gel RESULT without data is not.
    if cg.contains_phrase(q["q"], "gel") and not q.get("table"):
        for word in ("result", "results", "pattern"):
            assert not cg.contains_phrase(q["q"], word), (
                f"6.8 q{i}: the stem reports a gel {word} but carries no table; a gel result "
                f"must be delivered as data, per SCIENCE_BRIEF.md"
            )

_text = " ".join(" ".join([q["q"], q["why"], *q["choices"]]) for q in b6_8.QUESTIONS)
for word in DETAILS:
    assert not cg.contains_phrase(_text, word), (
        f"6.8: {word!r} appears in the module, but the CED excludes knowledge of the details "
        f"of these genetic engineering techniques from the scope of the exam"
    )

# Positive controls: both scans must be able to fire.
for phrase in FIGURE_PHRASES + ("band", "bands", "lane", "lanes"):
    assert cg.contains_phrase(f"consider {phrase} and answer", phrase), \
        f"the figure scan cannot detect {phrase!r} even in a string containing it"
for word in DETAILS:
    assert cg.contains_phrase(f"a stem mentioning {word} here", word), \
        f"the detail scan cannot detect {word!r} even in a string containing it"
print(f"    Figure rule enforced ({len(FIGURE_PHRASES)} phrases; a stem naming a gel must carry a")
print(f"    table) and the exclusion statement enforced ({len(DETAILS)} technique details scanned).")
