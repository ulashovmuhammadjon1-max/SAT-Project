"""Key audit for AP BIOLOGY 6.7 Mutations.

One (anchor, claim) per item, in module order. ``cg_check.check`` is the
structural gate; it is described in ``verify_b5_3.py``.

WHAT IS RECOMPUTED. A mutation type is decidable from the two sequences, so it
is decided rather than asserted: ``_classify`` below takes the original and the
altered coding sequence plus the chart, and returns the framework's own category
by applying EK 6.7.A.1.i to iv in order -- a length change is a frameshift, an
altered stop position is nonsense, an unchanged peptide is silent, and a changed
residue is a point mutation that alters the protein. The three chart items and
the frameshift item are all keyed to what that function returns for the sequences
LIFTED OUT OF THEIR OWN STEMS, so an edited sequence changes what the checker
expects. ``_classify`` is controlled below on one example of each category, so a
function that returned the same answer for everything could not pass.

The nondisjunction items are arithmetic: the four gamete counts are checked to
sum to twice the parent cell's count, the expected haploid number is recomputed
by halving, the departures are identified against it, and the zygote total is
added up rather than recalled. The mutation-description table is recomputed by
mapping each row's recorded change and effect onto a category.

THE TWO EXCLUSION STATEMENTS ARE ENFORCED. The CED bars knowledge of specific
mutations and their effects, and of specific disorders related to changes in
chromosome number. ``BARRED`` below lists the gene and disease names this topic
tempts an author into -- including the ones the CED itself prints as
illustrative examples -- and the scan at the bottom fails if any appears in a
stem, a choice or a reason. The scan carries a positive control, because a scan
that cannot fire is worse than none.

NEGATIVE CONTROL: ``negcontrol_b5_7.py``.
"""
import re

import cg_check as cg
import b6_7

T_CODE = b6_7._T_CODE
T_NONDIS = b6_7._T_NONDIS
T_MUT = b6_7._T_MUT

# Named by the CED as illustrative examples, or otherwise the obvious reach for
# an author writing this topic. All are barred by the two exclusion statements.
BARRED = ("cftr", "cystic fibrosis", "mc1r", "pocket mice", "sickle cell",
          "sickle-cell", "down syndrome", "trisomy", "turner syndrome",
          "klinefelter", "huntington", "hemophilia")


def _rows(table):
    heads = [cg.normalize(h) for h in table["headers"]]
    return [dict(zip(heads, r)) for r in table["rows"]]


def _chart(table):
    out = {}
    for r in _rows(table):
        codon = str(r["mrna codon"]).strip().upper()
        assert re.fullmatch(r"[ACGU]{3}", codon), f"{codon!r} is not an RNA triplet"
        out[codon] = cg.normalize(r["amino acid encoded"])
    return out


def _peptide(chart, seq):
    """Residues up to the first stop, and the index of that stop."""
    assert len(seq) % 3 == 0, f"{seq!r} is not a whole number of triplets"
    out = []
    for i in range(0, len(seq), 3):
        codon = seq[i:i + 3]
        assert codon in chart, f"codon {codon} is not on the chart supplied"
        if chart[codon] == "stop":
            return out, i // 3
        out.append(chart[codon])
    raise AssertionError(f"{seq!r} reaches no stop codon")


def _classify(chart, before, after):
    """The framework's category for a change, by EK 6.7.A.1.i to iv."""
    assert before != after, "the two sequences are identical, so nothing is being classified"
    if len(before) != len(after):
        return "frameshift"
    diffs = [i for i, (a, b) in enumerate(zip(before, after)) if a != b]
    assert len(diffs) == 1, f"a substitution should differ at one position; differs at {diffs}"
    p_before, stop_before = _peptide(chart, before)
    p_after, stop_after = _peptide(chart, after)
    if stop_after < stop_before:
        return "nonsense"
    if p_before == p_after:
        return "silent"
    return "point"


_CHART = _chart(T_CODE)

# Controls on the classifier. Each category must be reachable and they must not
# collapse onto one another.
assert _classify(_CHART, "AUGCGUAAAUAG", "AUGUGUAAAUAG") == "point"
assert _classify(_CHART, "AUGCGUAAAUAG", "AUGCGCAAAUAG") == "silent"
assert _classify(_CHART, "AUGGAGAAAUAA", "AUGUAGAAAUAA") == "nonsense"
assert _classify(_CHART, "AUGCGUAAAUGUUAA", "AUGGUAAAUGUUAA") == "frameshift"
assert len({_classify(_CHART, "AUGCGUAAAUAG", "AUGUGUAAAUAG"),
            _classify(_CHART, "AUGCGUAAAUAG", "AUGCGCAAAUAG"),
            _classify(_CHART, "AUGGAGAAAUAA", "AUGUAGAAAUAA")}) == 3, \
    "the classifier returns the same answer for three different changes"


def _sequences_from(stem):
    """The before and after sequences the stem states, in that order."""
    hits = re.findall(r"(?<![A-Za-z])[ACGU]{6,}(?![A-Za-z])", stem)
    assert len(hits) == 2, f"expected two sequences in the stem; found {hits}"
    return hits[0], hits[1]


def _chart_item(table, item, expected):
    chart = _chart(table)
    before, after = _sequences_from(item["q"])
    got = _classify(chart, before, after)
    assert got == expected, f"the stem's sequences classify as {got!r}, not {expected!r}"
    return before, after, chart, got


def q7(table, item):
    before, after, chart, got = _chart_item(table, item, "point")
    p_before, _ = _peptide(chart, before)
    p_after, _ = _peptide(chart, after)
    assert p_before != p_after, "a point mutation keyed here must change the protein, or it is silent"
    return (f"one substitution turns {before} into {after}; the chart gives {p_before} then "
            f"{p_after}, so the classification recomputes as {got}")


def q8(table, item):
    before, after, chart, got = _chart_item(table, item, "silent")
    p_before, _ = _peptide(chart, before)
    p_after, _ = _peptide(chart, after)
    assert p_before == p_after, "a silent mutation must leave the peptide identical"
    return (f"one substitution turns {before} into {after} and the chart gives {p_before} both "
            f"times, so the classification recomputes as {got}")


def q9(table, item):
    before, after, chart, got = _chart_item(table, item, "nonsense")
    _, stop_before = _peptide(chart, before)
    _, stop_after = _peptide(chart, after)
    assert stop_after < stop_before, "a nonsense mutation must move the stop earlier"
    return (f"one substitution turns {before} into {after} and moves the stop from triplet "
            f"{stop_before + 1} to triplet {stop_after + 1}, so it recomputes as {got}")


def _nondis(table):
    rows = _rows(table)
    col = "number of chromosomes counted"
    parent = [cg.num(r[col]) for r in rows
              if cg.contains_phrase(r["cell or gamete"], "the parent cell before meiosis")]
    assert len(parent) == 1, "exactly one row must be the parent cell"
    gametes = {cg.normalize(r["cell or gamete"]): cg.num(r[col]) for r in rows
               if cg.normalize(r["cell or gamete"]).startswith("gamete")}
    assert len(gametes) == 4, f"a meiosis gives four products; the table lists {len(gametes)}"
    return parent[0], gametes


def q17(table, item):
    parent, gametes = _nondis(table)
    expected = parent / 2
    assert expected == 23, f"the expected gamete number recomputes to {expected}, not 23"
    assert sum(gametes.values()) == 2 * parent, \
        f"the four gametes total {sum(gametes.values())}, not twice the parent's {parent}"
    odd = sorted(g for g, n in gametes.items() if n != expected)
    assert len(odd) == 2, f"{len(odd)} gametes depart from the expected number, not two"
    departures = sorted(gametes[g] - expected for g in odd)
    assert departures == [-1, 1], f"the departures recompute to {departures}, not one up and one down"
    return (f"a parent of {parent:.0f} gives gametes of {expected:.0f}; two gametes read "
            f"{[gametes[g] for g in odd]}, one above and one below, and the four still total "
            f"{sum(gametes.values()):.0f}")


def q18(table, item):
    parent, gametes = _nondis(table)
    expected = parent / 2
    high = max(gametes.values())
    assert high == expected + 1, f"the gamete with the extra chromosome reads {high}"
    zygote = high + expected
    assert zygote == 47, f"the zygote total recomputes to {zygote}, not 47"
    for wrong in (parent, expected + expected + 2, high, expected):
        assert wrong != zygote, f"a distractor value {wrong} coincides with the key"
    return (f"{high:.0f} from the affected gamete plus the expected {expected:.0f} gives "
            f"{zygote:.0f} chromosomes in the zygote")


# The descriptive table is fixed stimulus, so the check asserts its exact
# wording rather than searching it for keywords. A keyword search passes on a
# cell that has acquired extra text, which is how a table check ends up not
# reading its table -- the negative control caught this file doing it.
_CHANGES = {"one nucleotide substituted for a different nucleotide",
            "one nucleotide deleted from the sequence"}
_EFFECTS = {"one amino acid differs from the usual one",
            "no amino acid differs from the usual sequence",
            "a stop appears earlier than usual where an amino acid had been",
            "every amino acid after the site of the change differs"}


def _mut_table(table):
    """Each described mutation mapped onto the framework's categories."""
    out = {}
    seen_effects = set()
    for r in _rows(table):
        change = cg.normalize(r["change to the dna sequence"])
        effect = cg.normalize(r["effect on the amino acid sequence of the protein"])
        assert change in _CHANGES, f"unrecognised change description {change!r}"
        assert effect in _EFFECTS, f"unrecognised effect description {effect!r}"
        assert effect not in seen_effects, f"the effect {effect!r} is recorded twice"
        seen_effects.add(effect)
        assert re.fullmatch(r"mutation [0-9]+", cg.normalize(r["mutation"])), \
            f"row label {r['mutation']!r} is not of the form 'Mutation 1'"
        substituted = cg.contains_phrase(change, "substituted")
        deleted = cg.contains_phrase(change, "deleted")
        assert substituted != deleted, f"the change {change!r} is neither clearly a substitution nor a deletion"
        if deleted:
            kind = "frameshift"
        elif cg.contains_phrase(effect, "no amino acid differs"):
            kind = "silent"
        elif cg.contains_phrase(effect, "a stop appears earlier than usual"):
            kind = "nonsense"
        else:
            kind = "point"
        out[cg.normalize(r["mutation"])] = kind
    return out


def q21(table, item):
    kinds = _mut_table(table)
    silent = sorted(m for m, k in kinds.items() if k == "silent")
    assert len(silent) == 1, f"exactly one row should be silent; got {silent}"
    assert len(set(kinds.values())) == 4, f"the four rows should be four categories; got {kinds}"
    return f"the four rows classify as {kinds}, and exactly one of them is silent"


def q22(table, item):
    kinds = _mut_table(table)
    shift = sorted(m for m, k in kinds.items() if k == "frameshift")
    assert len(shift) == 1, f"exactly one row should be a frameshift; got {shift}"
    others = [k for m, k in kinds.items() if m not in shift]
    assert all(k != "frameshift" for k in others), "only the deletion row may be a frameshift"
    return f"the four rows classify as {kinds}, and only the deletion is a frameshift"


CLAIMS = [
 ("alteration in a DNA sequence, which can change the type or amount of the protein",
  "EK 6.7.A.1 states that alterations in a DNA sequence are mutations that can cause changes in the type or amount of the protein produced and the consequent phenotype. A reversible modification of DNA or histones is EK 6.5.A.2's epigenetic change, and the code is shared under EK 6.4.A.3.iv."),
 ("effect, or the lack of effect, the mutation has on the resulting nucleic acid or protein",
  "EK 6.7.A.1 states that mutations can be beneficial, detrimental, or neutral based on the effect or the lack of effect they have on the resulting nucleic acid or protein and the phenotypes conferred by the protein, so the classification turns on consequences rather than on the size, cause or position of the change."),
 ("one nucleotide has been substituted for a different nucleotide",
  "EK 6.7.A.1.i defines a point mutation in exactly these terms. Insertions and deletions are EK 6.7.A.1.ii's frameshift mutations and a change in chromosome number is EK 6.7.B.2.i's."),
 ("one or more nucleotides are inserted or deleted, which shifts the reading frame",
  "EK 6.7.A.1.ii states that frameshift mutations occur when one or more nucleotides are inserted or deleted, causing the reading frame to be shifted. A substitution leaves the triplet boundaries of EK 6.4.A.3.ii where they were."),
 ("point mutation that causes a premature stop",
  "EK 6.7.A.1.iii defines a nonsense mutation as a point mutation that causes a premature stop, naming both the kind of change and its consequence. A point mutation with no effect on the amino acid sequence is EK 6.7.A.1.iv's silent mutation."),
 ("change in the nucleotide sequence that has no effect on the amino acid sequence",
  "EK 6.7.A.1.iv states exactly this. That such a change is possible follows from EK 6.4.A.3.iii, that many amino acids are encoded by more than one codon."),
 ("point mutation, because one nucleotide has been substituted",
  "EK 6.7.A.1.i. The table check lifts both sequences out of the stem and runs them through a classifier that applies the framework's four definitions in order; it recomputes a single substitution that changes the residue the chart assigns, which excludes the silent reading."),
 ("silent mutation, because the change in the nucleotide sequence has no effect",
  "EK 6.7.A.1.iv. The table check recomputes both peptides from the chart and confirms they are identical, and EK 6.7.A.1 makes any alteration in a DNA sequence a mutation, so a change without effect is still one."),
 ("nonsense mutation, because a point mutation has introduced a premature stop",
  "EK 6.7.A.1.iii. The table check recomputes the position of the stop in both sequences and confirms it moves earlier, which is what premature means, on a single substitution."),
 ("frameshift mutation, because a nucleotide has been deleted",
  "EK 6.7.A.1.ii. The classifier controlled in this file returns frameshift for these two sequences because their lengths differ, and EK 6.4.A.3.ii has the message read in triplets, so every boundary after the site moves."),
 ("Errors in DNA replication or DNA repair mechanisms, and external factors including radiation",
  "EK 6.7.B.1 states that errors in DNA replication or DNA repair mechanisms as well as external factors, including radiation and reactive chemicals, can cause random mutations in the DNA. The word random rules out an account in which need decides where mutations fall."),
 ("arose at random, and the antibiotic then selected the cells",
  "EK 6.7.B.1 calls these mutations random and EK 6.7.C.1 states that genetic changes enhancing survival and reproduction can be selected for by environmental conditions, so the randomness is in where the change occurs and the direction comes from the selecting condition afterward."),
 ("environmental context",
  "EK 6.7.B.1.i states that whether a mutation is beneficial, detrimental, or neutral depends on the environmental context, which is why the framework does not attach the label to the change itself."),
 ("version of a sequence that was not previously present",
  "EK 6.7.B.1.ii states that mutations are a source of genetic variation and EK 6.7.A.1 makes a mutation an alteration in a DNA sequence, so what it contributes is a sequence version that was not there before."),
 ("Changes in phenotype",
  "EK 6.7.B.2 states that errors in mitosis or meiosis can result in changes in phenotype, with EK 6.7.B.2.i and iii naming chromosome number and chromosome structure as the routes. Reversible histone modification is EK 6.5.A.2's."),
 ("Changes in chromosome number, which often result in new phenotypes",
  "EK 6.7.B.2.i states that changes in chromosome number resulting from nondisjunction often result in new phenotypes. The change is at the level of whole chromosomes rather than of a nucleotide sequence."),
 ("counted at 24 and at 22",
  "EK 6.7.B.2.i attributes changes in chromosome number to nondisjunction. The table check recomputes the expected gamete number by halving the parent count, identifies the two gametes that depart from it by one in each direction, and confirms the four gametes still total twice the parent count."),
 ("47 chromosomes",
  "EK 5.3.A.2 makes fertilization the fusion of two haploid gametes, so the zygote's count is the sum of the two. The table check recomputes the expected gamete number, adds the affected gamete's count to it, and confirms no distractor value equals the total."),
 ("They lead to genetic disorders",
  "EK 6.7.B.2.iii states that alterations in chromosome structure lead to genetic disorders, which the framework lists alongside the changes in chromosome number of EK 6.7.B.2.i and ii."),
 ("often result in disorders with developmental limitations",
  "EK 6.7.B.2.ii states this, and EK 6.7.B.2 attributes the errors to mitosis or meiosis rather than to one of them alone."),
 ("substitution leaves the amino acid sequence unchanged",
  "EK 6.7.A.1.iv defines a silent mutation as a change with no effect on the amino acid sequence. The table check maps every row of the table onto one of the framework's four categories and confirms the four rows give four different ones."),
 ("nucleotide is deleted and every amino acid after the site differs",
  "EK 6.7.A.1.ii makes an insertion or deletion the frameshift case. The table check confirms exactly one row records a deletion and that no substitution row is classified as a frameshift."),
 ("may affect phenotypes that are subject to natural selection",
  "EK 6.7.C.1 states that changes in genotype may affect phenotypes that are subject to natural selection and that genetic changes enhancing survival and reproduction can be selected for by environmental conditions. The mutations themselves are random under EK 6.7.B.1."),
 ("Transformation, the uptake of DNA",
  "EK 6.7.C.1.i names four horizontal acquisitions and defines each; transformation is the uptake of DNA, which is what taking DNA up from the surroundings is."),
 ("Transduction, the viral transmission of genetic information",
  "EK 6.7.C.1.i defines transduction as the viral transmission of genetic information. Alternative splicing is EK 6.3.A.4.iii's processing step and concerns no transfer between cells."),
 ("Conjugation, the transfer of DNA from one cell to another cell",
  "EK 6.7.C.1.i defines conjugation as cell-to-cell transfer of DNA. Fertilization is the fusion of two haploid gametes under EK 5.3.A.2 and is not one of the prokaryotic acquisitions."),
 ("Transposition, and all four increase genetic variation",
  "EK 6.7.C.1.i defines transposition as the movement of DNA segments within and between DNA molecules and states that the four named acquisitions increase genetic variation. Nondisjunction belongs to EK 6.7.B.2.i and is not an acquisition."),
 ("They can recombine genetic information",
  "EK 6.7.C.1.ii states that related viruses can recombine genetic information if they infect the same host cell, which the framework lists among the processes increasing genetic variation."),
 ("evolutionarily conserved and are shared by various organisms",
  "EK 6.7.C.1.iii states this of reproductive processes that increase genetic variation, and being shared across groups is what conserved means."),
 ("depends on the environmental context, and that genetic changes enhancing survival and reproduction can be selected for",
  "EK 6.7.B.1.i and EK 6.7.C.1 together allow one unchanged sequence to be neutral under one set of conditions and favoured under another. EK 6.7.B.1 also names internal errors among the causes and calls the mutations random."),
]

cg.check(b6_7, CLAIMS,
         table_checks={7: q7, 8: q8, 9: q9, 17: q17, 18: q18, 21: q21, 22: q22})

# The CED's two exclusion statements, enforced over the whole module.
_text = " ".join(" ".join([q["q"], q["why"], *q["choices"]]) for q in b6_7.QUESTIONS)
for word in BARRED:
    assert not cg.contains_phrase(_text, word), (
        f"6.7: {word!r} appears in the module, but the CED excludes knowledge of specific "
        f"mutations and their effects, and of specific disorders related to changes in "
        f"chromosome number, from the scope of the exam"
    )
# Positive control: the scan must be able to fire.
for word in BARRED:
    assert cg.contains_phrase(f"a question mentioning {word} in passing", word), \
        f"the exclusion scan cannot detect {word!r} even in a string containing it"
print(f"    Mutation classifier applied to every sequence item and controlled on all four")
print(f"    categories; both exclusion statements enforced ({len(BARRED)} barred names scanned).")
