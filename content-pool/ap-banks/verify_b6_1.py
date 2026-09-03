"""Key audit for AP BIOLOGY 6.1 DNA and RNA Structure.

One (anchor, claim) per item, in module order. ``cg_check.check`` is the
structural gate; it is described in ``verify_b5_3.py``.

WHAT IS RECOMPUTED HERE. Base pairing is a rule, and a rule can be applied by a
computer. ``_complement`` below implements EK 6.1.B.1.iii directly and is used
to recompute the two sequence items rather than to trust a hand-written answer;
``_purine`` and ``_pyrimidine`` implement EK 6.1.B.1.i and EK 6.1.B.1.ii and are
used to check the ring-count table and the class assignments. The five data
items are recomputed from their tables, including the two composition
arithmetic items, whose answers follow from the pairing rule and nothing else.

A NOTE ON WHAT IS NOT ASSERTED. The framework does not say how many hydrogen
bonds join a pair, nor that purine-pyrimidine pairing keeps the helix a constant
width. Neither claim is keyed anywhere in this module, and a drafted item that
rested on the second was cut.

NEGATIVE CONTROL: ``negcontrol_b5_7.py``.
"""
import cg_check as cg
import b6_1

T_CHARGAFF = b6_1._T_CHARGAFF
T_CHARG2 = b6_1._T_CHARG2
T_RING = b6_1._T_RING
T_GENOMES = b6_1._T_GENOMES
T_RNA = b6_1._T_RNA

PURINES = {"adenine", "guanine"}
PYRIMIDINES = {"cytosine", "thymine", "uracil"}

# EK 6.1.B.1.iii, written out as a rule rather than as a remembered answer.
_DNA_PAIR = {"adenine": "thymine", "thymine": "adenine",
             "guanine": "cytosine", "cytosine": "guanine"}
_RNA_PAIR = dict(_DNA_PAIR, adenine="uracil", thymine="adenine")


def _complement(seq, rna=False):
    table = _RNA_PAIR if rna else _DNA_PAIR
    return [table[b] for b in seq]


assert PURINES & PYRIMIDINES == set(), "the two base classes must be disjoint"
assert all(_DNA_PAIR[p] in PYRIMIDINES for p in PURINES), \
    "EK 6.1.B.1.iii: every purine must pair with a pyrimidine"
assert all(_DNA_PAIR[p] in PURINES for p in PYRIMIDINES if p != "uracil"), \
    "EK 6.1.B.1.iii: every DNA pyrimidine must pair with a purine"

# q8: the DNA and the RNA partner of one strand, and how many positions differ.
_Q8_SEQ = ["adenine", "guanine", "adenine", "cytosine", "adenine"]
_Q8_DNA = _complement(_Q8_SEQ)
_Q8_RNA = _complement(_Q8_SEQ, rna=True)
_Q8_DIFF = sum(1 for a, b in zip(_Q8_DNA, _Q8_RNA) if a != b)
assert _Q8_DIFF == 3, f"q8: the two partner strands differ at {_Q8_DIFF} positions, not 3"
assert _Q8_DIFF == _Q8_SEQ.count("adenine"), \
    "q8: the positions that differ must be exactly the adenines, which is what the key asserts"
assert all(a == b for a, b in zip(_Q8_DNA, _Q8_RNA)
           if a not in ("thymine", "uracil")), "q8: no non-adenine position may differ"

# q9: the complementary DNA strand, recomputed base by base.
_Q9 = _complement(["guanine", "guanine", "cytosine", "adenine", "guanine"])
assert _Q9 == ["cytosine", "cytosine", "guanine", "thymine", "cytosine"], \
    f"q9: the complement recomputes to {_Q9}"

# q10: the RNA strand pairing with a DNA strand, recomputed base by base.
_Q10 = _complement(["adenine", "cytosine", "adenine", "thymine"], rna=True)
assert _Q10 == ["uracil", "guanine", "uracil", "adenine"], \
    f"q10: the RNA partner recomputes to {_Q10}"
assert "thymine" not in _Q10, "q10: an RNA strand carries uracil, never thymine"

# q11, q26: two purines have no permitted partner between them.
assert _DNA_PAIR["adenine"] != "guanine" and _DNA_PAIR["guanine"] != "adenine", \
    "q11, q26: adenine and guanine must not be a permitted pair"

# q25: 33 percent guanine in a double-stranded molecule leaves 17 percent adenine.
_G = 33.0
_C = _G                      # EK 6.1.B.1.iii pairs guanine with cytosine
_A = (100 - _G - _C) / 2     # the remainder is shared equally by adenine and thymine
assert _A == 17, f"q25: adenine recomputes to {_A}, not 17"


def _rows(table):
    heads = [cg.normalize(h) for h in table["headers"]]
    return [dict(zip(heads, r)) for r in table["rows"]]


def q14(table, item):
    good, bad = [], []
    for r in _rows(table):
        a, t = cg.num(r["adenine percent"]), cg.num(r["thymine percent"])
        g, c = cg.num(r["guanine percent"]), cg.num(r["cytosine percent"])
        assert a + t + g + c == 100, f"{r['sample']} sums to {a + t + g + c}, not 100"
        (good if (a == t and g == c) else bad).append(cg.normalize(r["sample"]))
    assert good == ["sample 1", "sample 3"], f"the consistent samples are {good}"
    assert bad == ["sample 2", "sample 4"], f"the inconsistent samples are {bad}"
    assert not all(len({cg.num(r[h]) for h in
                        ("adenine percent", "thymine percent", "guanine percent",
                         "cytosine percent")}) == 1 for r in _rows(table)), \
        "'equal amounts of all four bases' must not describe every sample"
    return (f"every sample sums to 100 percent; adenine equals thymine and guanine equals "
            f"cytosine in {good} and in neither of {bad}")


def q15(table, item):
    known = {cg.normalize(r["base"]): r["percent of the bases in the sample"]
             for r in _rows(table)}
    a, t = cg.num(known["adenine"]), cg.num(known["thymine"])
    assert a == t, f"a double-stranded sample needs adenine equal to thymine; got {a} and {t}"
    for base in ("guanine", "cytosine"):
        assert not cg.normalize(known[base]).replace(" ", "").isdigit(), \
            f"{base} must be unmeasured, or the question answers itself"
    cytosine = (100 - a - t) / 2   # EK 6.1.B.1.iii makes guanine and cytosine equal
    assert cytosine == 28, f"cytosine recomputes to {cytosine}, not 28"
    assert cytosine not in (a, 100 - a - t, 50), "a distractor value coincides with the key"
    return (f"adenine {a:.0f} plus thymine {t:.0f} leaves {100 - a - t:.0f} percent to be "
            f"split equally between guanine and cytosine, so cytosine is {cytosine:.0f} percent")


def q17(table, item):
    rings = {cg.normalize(r["nitrogenous base"]):
             cg.num(r["number of rings in the base structure"]) for r in _rows(table)}
    doubles = {b for b, n in rings.items() if n == 2}
    singles = {b for b, n in rings.items() if n == 1}
    assert doubles | singles == set(rings), f"a base has a ring count other than one or two: {rings}"
    assert doubles == PURINES, f"the double-ring bases are {doubles}, not the purines"
    assert singles == PYRIMIDINES, f"the single-ring bases are {singles}, not the pyrimidines"
    return (f"the table gives two rings to {sorted(doubles)} and one to {sorted(singles)}, "
            f"which is exactly the purine and pyrimidine split")


def q18(table, item):
    rows = _rows(table)
    circ = [cg.normalize(r["organism"]) for r in rows
            if cg.normalize(r["chromosome shape"]) == "circular"]
    lin = [cg.normalize(r["organism"]) for r in rows
           if cg.normalize(r["chromosome shape"]) == "linear"]
    assert circ == ["organism w", "organism z"], f"the circular-chromosome organisms are {circ}"
    for name in circ:
        n = cg.num(next(r["number of chromosomes"] for r in rows
                        if cg.normalize(r["organism"]) == name))
        assert n == 1, f"{name} has {n:.0f} chromosomes; the key says a single one"
    for name in lin:
        n = cg.num(next(r["number of chromosomes"] for r in rows
                        if cg.normalize(r["organism"]) == name))
        assert n > 1, f"{name} has {n:.0f} chromosomes; the key needs multiple linear ones"
    plasmid_col = "extra-chromosomal circular dna molecules present"
    withp = [cg.normalize(r["organism"]) for r in rows
             if cg.normalize(r[plasmid_col]) == "yes"]
    assert len(withp) == 1 and withp[0] in circ, \
        "exactly one organism should carry plasmids, so that option picks out one organism only"
    assert set(withp) != set(circ), \
        "plasmids must not coincide with the circular set, or the two criteria cannot be told apart"
    return (f"{circ} each have a single circular chromosome and {lin} have multiple linear ones; "
            f"only {withp} carries extra-chromosomal circular DNA, so that criterion selects differently")


def q19(table, item):
    out = {}
    for r in _rows(table):
        vals = {b: cg.num(r[f"{b} percent"])
                for b in ("adenine", "uracil", "thymine", "guanine", "cytosine")}
        assert sum(vals.values()) == 100, f"{r['sample']} sums to {sum(vals.values())}"
        out[cg.normalize(r["sample"])] = vals
    rna = [s for s, v in out.items() if v["uracil"] > 0 and v["thymine"] == 0]
    dna = [s for s, v in out.items() if v["thymine"] > 0 and v["uracil"] == 0]
    assert rna == ["sample q"], f"the uracil-bearing sample is {rna}"
    assert sorted(dna) == ["sample p", "sample r"], f"the thymine-bearing samples are {dna}"
    return (f"{rna} contains uracil and no thymine while {sorted(dna)} contain thymine and no "
            f"uracil, and all three sum to 100 percent")


CLAIMS = [
 ("Prokaryotic organisms, which typically have circular chromosomes",
  "EK 6.1.A.1.i states that prokaryotic organisms typically have circular chromosomes, while EK 6.1.A.1.ii gives eukaryotes multiple linear chromosomes. A closed loop with no free ends is circular."),
 ("Multiple linear chromosomes made of DNA and condensed using histones",
  "EK 6.1.A.1.ii states that eukaryotic organisms typically have multiple linear chromosomes comprised of DNA, condensed using histones and associated proteins. Each rejected option alters one of those three features."),
 ("proteins that, with associated proteins, condense",
  "EK 6.1.A.1.ii states that eukaryotic linear chromosomes are condensed using histones and associated proteins, so histones are proteins with a packaging role. The extra-chromosomal circular DNA of EK 6.1.A.2 is a plasmid, a different structure."),
 ("extra-chromosomal circular molecules of DNA",
  "EK 6.1.A.2 states that prokaryotes and eukaryotes can contain plasmids, which are extra-chromosomal circular molecules of DNA. The description in the stem matches that definition term for term."),
 ("lies outside the chromosome",
  "EK 6.1.A.2 defines a plasmid as extra-chromosomal, so the plasmid and the prokaryotic chromosome of EK 6.1.A.1.i share both the circular shape and the DNA composition and differ only in lying inside or outside the chromosome."),
 ("Guanine and adenine, which have a double ring structure",
  "EK 6.1.B.1.i states that the purines, guanine and adenine, have a double ring structure, and EK 6.1.B.1.ii assigns cytosine, thymine and uracil to the single-ring pyrimidines. The class membership is checked against those sets above."),
 ("Cytosine, thymine and uracil",
  "EK 6.1.B.1.ii names cytosine, thymine and uracil as the pyrimidines and gives them a single ring structure; EK 6.1.B.1.i assigns guanine and adenine to the purines instead."),
 ("Three, because only adenine takes a different partner",
  "EK 6.1.B.1.iii gives guanine and cytosine one partner each in both nucleic acids and gives adenine thymine or uracil in RNA. Recomputed above by building both partner strands from the rule and comparing them position by position: they differ at three positions, and those positions are exactly the three adenines."),
 ("Cytosine, cytosine, guanine, thymine, cytosine",
  "EK 6.1.B.1.iii applied base by base. Recomputed above by ``_complement``, which implements the rule rather than recording an answer: the complement of guanine, guanine, cytosine, adenine, guanine is cytosine, cytosine, guanine, thymine, cytosine."),
 ("Uracil, guanine, uracil, adenine",
  "EK 6.1.B.1.iii supplies uracil as adenine's partner in RNA. Recomputed above by the same function in its RNA mode, which also confirms that no thymine appears in an RNA partner strand."),
 ("Both are purines",
  "EK 6.1.B.1.i places guanine and adenine together among the purines and EK 6.1.B.1.iii allows only purine-with-pyrimidine pairs, so the pairing tables above contain no adenine-guanine pair, which is asserted directly."),
 ("as distantly related as a bacterium and a mammal",
  "EK 6.1.B.1 states that specific nucleotide base pairing is conserved through evolution, and EK 6.1.B.1.iii states the same rules for RNA as for DNA. A conserved feature is one retained across lineages."),
 ("carry their genome as RNA",
  "EK 6.1.A.1 states that genetic information is STORED IN AND PASSED TO SUBSEQUENT GENERATIONS through DNA and, in some cases, RNA molecules. The clause is about the heritable genome, which is what an RNA genome is; the rejected options describe roles RNA plays in cells whose genome is DNA."),
 ("Samples 1 and 3",
  "EK 6.1.B.1.iii pairs adenine with thymine and guanine with cytosine, so both equalities must hold in a double-stranded molecule. The table check recomputes which samples satisfy them and confirms that summing to one hundred separates nothing, since all four do."),
 ("28 percent",
  "EK 6.1.B.1.iii makes guanine and cytosine equal in a double-stranded molecule. The table check recomputes 100 minus 22 minus 22 as 56, halves it to 28, and confirms guanine is genuinely unmeasured in the table so the question does not answer itself."),
 ("equal, because every base pair joins one purine to one pyrimidine",
  "EK 6.1.B.1.iii states that purines pair with pyrimidines, so each pair contributes exactly one of each class and the totals match in any double-stranded molecule. Neither the ring counts of EK 6.1.B.1.i nor the number of bases named in each class enters the sum."),
 ("double ring are the purines",
  "EK 6.1.B.1.i gives the purines a double ring and EK 6.1.B.1.ii gives the pyrimidines a single ring. The table check recomputes the two ring groups from the table and confirms they coincide exactly with the framework's purine and pyrimidine sets."),
 ("Organisms W and Z",
  "EK 6.1.A.1.i makes a circular chromosome typical of prokaryotes and EK 6.1.A.1.ii makes multiple linear chromosomes typical of eukaryotes. The table check recomputes which organisms have a single circular chromosome, and confirms that the plasmid column selects a different set, as EK 6.1.A.2 requires since both groups can carry plasmids."),
 ("Sample Q",
  "EK 6.1.B.1.ii lists uracil among the pyrimidines and EK 6.1.B.1.iii identifies it as the base standing in for thymine in RNA. The table check recomputes which sample carries uracil and no thymine and which carry thymine and no uracil."),
 ("not a double-stranded molecule",
  "EK 6.1.B.1.iii pairs adenine with thymine, so in a double-stranded molecule the two percentages must match, and forty against fifteen cannot. EK 6.1.B.1 makes the rules conserved rather than varying by organism or by the shape of the molecule."),
 ("Both prokaryotes and eukaryotes can contain plasmids",
  "EK 6.1.A.2 states that prokaryotes AND eukaryotes can contain plasmids, which are extra-chromosomal circular molecules of DNA. The student's premises about shape and composition are right; the inference fails because the feature is not restricted to one group."),
 ("Specific nucleotide base pairing, which is conserved through evolution",
  "Learning objective 6.1.B asks for the characteristics of DNA that allow it to be used as hereditary material, and the essential knowledge under it is EK 6.1.B.1, exactly this statement. Histones are eukaryote-specific under EK 6.1.A.1.ii and the circular shape is prokaryote-typical."),
 ("Histones and associated proteins",
  "EK 6.1.A.1.ii credits condensation of eukaryotic linear chromosomes to histones and associated proteins. Base pairing under EK 6.1.B.1.iii joins the two strands of the helix and is not what the framework credits with condensing a chromosome."),
 ("through DNA, and through RNA in some cases",
  "EK 6.1.A.1 states that genetic information is stored in and passed to subsequent generations through DNA molecules and, in some cases, RNA molecules. No group is given its own separate storage molecule anywhere in the statement."),
 ("17 percent",
  "EK 6.1.B.1.iii pairs guanine with cytosine and adenine with thymine. Recomputed above: 33 percent guanine implies 33 percent cytosine, leaving 34 percent to be shared equally, so adenine is 17 percent."),
 ("no permitted partners",
  "EK 6.1.B.1.iii states that purines pair with pyrimidines, so two purine strands offer no permitted partner for any base. Asserted directly against the pairing tables above; EK 6.1.B.1.i gives purines a double ring, not a single one."),
 ("One circular chromosome and two plasmids",
  "EK 6.1.A.1.i gives a prokaryote a circular chromosome and EK 6.1.A.2 defines a plasmid as an extra-chromosomal circular molecule of DNA, so the genome-carrying molecule is the chromosome and the ones outside it are plasmids. Histones are proteins under EK 6.1.A.1.ii."),
 ("one permitted partner",
  "EK 6.1.B.1 calls the pairing specific and EK 6.1.B.1.iii states what that means: purines pair with pyrimidines, adenine with thymine or uracil in RNA, and guanine with cytosine. The pairing tables above are single-valued, which is that property."),
 ("conserved through evolution",
  "EK 6.1.B.1 states that specific nucleotide base pairing is conserved through evolution. Finding the same pairs across three distantly related organisms is what that looks like in data; the rejected options concern chromosome shape, plasmids, packaging and the storage molecule."),
 ("condensed using histones and associated proteins, which the framework does not attribute to the bacterium",
  "EK 6.1.A.1.ii attributes condensation using histones and associated proteins to eukaryotic linear chromosomes, and EK 6.1.A.1.i describes the prokaryotic chromosome as circular without that attribution. EK 6.1.A.2 makes plasmids separate DNA molecules rather than packaging."),
]

cg.check(b6_1, CLAIMS, table_checks={14: q14, 15: q15, 17: q17, 18: q18, 19: q19})
print("    Base-pairing rule applied by code: both sequence items and the two composition")
print("    arithmetic items recomputed from EK 6.1.B.1.iii rather than asserted.")
