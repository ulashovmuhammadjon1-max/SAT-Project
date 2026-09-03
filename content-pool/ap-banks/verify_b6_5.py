"""Key audit for AP BIOLOGY 6.5 Regulation of Gene Expression.

One (anchor, claim) per item, in module order. ``cg_check.check`` is the
structural gate; it is described in ``verify_b5_3.py``.

WHAT IS RECOMPUTED. Nine items carry data and every one of their tables is
recomputed from the table alone. The recurring shape is a fold change between
two conditions, so ``_fold`` is written once and used for the constitutive item,
the inducible item, both operon items and the coordinate regulation item -- and
in each case the check confirms not only the keyed direction but that the
REJECTED reading is false on the same numbers, which is the part a hand-written
key skips. The tissue-specific item is recomputed by counting detections per
protein, the developmental item by confirming the transcription factor precedes
both genes and the two genes appear at different stages, and the dose item by
confirming the enzyme amounts and the phenotypes fall in the same order while
every individual makes some enzyme, since that last fact is what makes presence
alone insufficient.

WHAT IS NOT CLAIMED. The framework says epigenetic modifications are REVERSIBLE;
it does not say the DNA sequence is unchanged, and no key here says so either.
The reversibility is what every epigenetic item turns on, and the contrast drawn
with a mutation is drawn against EK 6.7.A.1's own wording, an alteration in a
DNA sequence.

NEGATIVE CONTROL: ``negcontrol_b5_7.py``.
"""
import re

import cg_check as cg
import b6_5

T_EXPR = b6_5._T_EXPR
T_EPI = b6_5._T_EPI
T_TISSUE = b6_5._T_TISSUE
T_DEV = b6_5._T_DEV
T_AMOUNT = b6_5._T_AMOUNT
T_OPERON_I = b6_5._T_OPERON_I
T_OPERON_R = b6_5._T_OPERON_R
T_COORD = b6_5._T_COORD


def _rows(table):
    heads = [cg.normalize(h) for h in table["headers"]]
    return [dict(zip(heads, r)) for r in table["rows"]]


def _fold(before, after):
    """After divided by before, guarding the zero the data must never contain."""
    assert before > 0, "an expression measurement of zero makes a fold change undefined"
    return after / before


ABSENT = "expression with the sugar absent arbitrary units"
PRESENT = "expression with the sugar present arbitrary units"


def _sugar(table):
    return {cg.normalize(r["gene"]): (cg.num(r[ABSENT]), cg.num(r[PRESENT]))
            for r in _rows(table)}


def q5(table, item):
    d = _sugar(table)
    steady = {g: v for g, v in d.items() if 0.7 < _fold(*v) < 1.4}
    assert len(steady) >= 2, f"more than one gene should be unchanged by the sugar; got {steady}"
    high = {g for g, v in steady.items() if min(v) > 50}
    assert high == {"gene 1"}, f"the unchanged AND substantially expressed gene is {high}"
    # the rejected readings must be false on the same numbers
    assert _fold(*d["gene 2"]) > 10, "the induced gene must not also read as constitutive"
    assert max(d["gene 3"]) < 10, "the barely expressed gene must not read as substantially expressed"
    return (f"fold changes are {({g: round(_fold(*v), 2) for g, v in d.items()})}; only gene 1 is "
            f"both unchanged and expressed above 50 units")


def q6(table, item):
    d = _sugar(table)
    induced = {g for g, v in d.items() if _fold(*v) > 10}
    assert induced == {"gene 2"}, f"the induced gene is {induced}"
    for g in ("gene 1", "gene 3"):
        assert 0.5 < _fold(*d[g]) < 2, f"{g} changes by {_fold(*d[g]):.2f}, which is not 'unchanged'"
    return (f"gene 2 rises by a factor of {_fold(*d['gene 2']):.0f} with the sugar while the other "
            f"two change by less than a factor of two")


def q8(table, item):
    rows = _rows(table)
    assert len(rows) == 3, "reversibility needs a before, a during and an after"
    trio = [(cg.normalize(r["level of the histone modification"]),
             cg.num(r["expression of the gene arbitrary units"])) for r in rows]
    (m1, e1), (m2, e2), (m3, e3) = trio
    assert m1 == m3 and m1 != m2, f"the modification must return to its first level; got {[m1, m2, m3]}"
    assert m2 == "high" and m1 == "low", "the treatment must raise the modification"
    assert e2 < e1 / 5, f"expression must fall sharply under the modification; {e1} to {e2}"
    assert abs(e3 - e1) / e1 < 0.1, f"expression must return; {e1} then {e3}"
    assert e3 > 0, "a deleted gene could not be expressed again, so the final value must be nonzero"
    return (f"the modification goes low, high, low while expression goes {e1:.0f}, {e2:.0f}, "
            f"{e3:.0f}: a sharp fall that reverses")


def q12(table, item):
    cells = ["detected in liver cells", "detected in muscle cells", "detected in nerve cells"]
    counts = {}
    for r in _rows(table):
        vals = [cg.normalize(r[c]) for c in cells]
        assert set(vals) <= {"yes", "no"}, f"unexpected detection value in {vals}"
        counts[cg.normalize(r["protein"])] = vals.count("yes")
    specific = sorted(p for p, n in counts.items() if n == 1)
    everywhere = sorted(p for p, n in counts.items() if n == len(cells))
    assert specific == ["protein q", "protein r"], f"the tissue-specific proteins are {specific}"
    assert everywhere == ["protein s"], f"the ubiquitous proteins are {everywhere}"
    assert all(n > 0 for n in counts.values()), "every protein must be detected somewhere"
    return (f"detection counts are {counts}; {specific} appear in one cell type each and "
            f"{everywhere} in all three")


def q14(table, item):
    rows = _rows(table)
    stages = [(cg.normalize(r["developmental stage"]),
               cg.normalize(r["transcription factor 1 present"]) == "yes",
               cg.normalize(r["gene a expressed"]) == "yes",
               cg.normalize(r["gene b expressed"]) == "yes") for r in rows]
    def first(idx):
        for i, s in enumerate(stages):
            if s[idx]:
                return i
        raise AssertionError(f"column {idx} is never positive, so no sequence can be read")
    tf, a, b = first(1), first(2), first(3)
    assert tf <= a < b, f"the order recomputes to factor {tf}, gene A {a}, gene B {b}"
    assert not stages[0][1] and not stages[0][2] and not stages[0][3], \
        "nothing may be present at the first stage, or the factor does not precede the genes"
    assert a != b, "the two genes must appear at different stages, or the expression is simultaneous"
    return (f"the transcription factor first appears at stage {tf + 1}, gene A at stage {a + 1} and "
            f"gene B at stage {b + 1}: the factor precedes the genes and the genes are sequential")


def q16(table, item):
    rows = _rows(table)
    data = [(cg.num(r["amount of the enzyme produced percent of the typical amount"]),
             cg.normalize(r["observed phenotype"])) for r in rows]
    amounts = [a for a, _ in data]
    assert amounts == sorted(amounts, reverse=True), f"the amounts are not ordered: {amounts}"
    assert len({p for _, p in data}) == len(data), "each individual must show a distinct phenotype"
    assert all(0 < a <= 100 for a in amounts), \
        f"a percent of the typical amount outside 0 to 100 is not data: {amounts}"
    assert amounts[0] == 100, "one individual must sit at the typical amount, or there is no reference"
    assert cg.contains_phrase(data[0][1], "typical"), \
        "the individual at the typical amount must be the one with the typical phenotype"
    assert cg.contains_phrase(data[-1][1], "almost no"), \
        "the individual making least must be the one with least pigment, or the order does not correspond"
    assert amounts[0] / amounts[-1] > 5, "the range of amounts must be wide enough to matter"
    gaps = [x - y for x, y in zip(amounts, amounts[1:])]
    assert all(g >= 20 for g in gaps), \
        f"consecutive amounts {amounts} are too close for a dose correspondence to be readable"
    for r in rows:
        assert re.fullmatch(r"individual [0-9]+", cg.normalize(r["individual"])), \
            f"row label {r['individual']!r} is not of the form 'Individual 1'"
    return (f"all three individuals make some enzyme, in the amounts {amounts}, and their distinct "
            f"phenotypes follow that same order")


def _operon(table, words):
    """The two conditions of an operon comparison, checked to be a clean pair.

    ``words`` is the pair of opposed terms the two rows must differ by, and the
    rest of the two labels must match. Without that the check reads only the two
    numbers, and the negative control showed it then catching nothing: scaling
    either value left the comparison intact and corrupting a label left the
    keyword in place.
    """
    rows = _rows(table)
    assert len(rows) == 2, "an operon comparison needs exactly two conditions"
    col = "transcription of the group of genes arbitrary units"
    labs = [cg.normalize(r["condition of the culture"]) for r in rows]
    a, b = words
    assert (a in labs[0]) != (a in labs[1]), f"exactly one condition must say {a!r}: {labs}"
    assert (b in labs[0]) != (b in labs[1]), f"exactly one condition must say {b!r}: {labs}"
    assert labs[0].replace(a, "@").replace(b, "@") == labs[1].replace(a, "@").replace(b, "@"), \
        f"the two conditions must be identical apart from {a!r} and {b!r}: {labs}"
    return [(labs[i], cg.num(rows[i][col])) for i in range(2)]


def q21(table, item):
    pairs = _operon(table, ("absent", "present"))
    absent = next(v for c, v in pairs if cg.contains_phrase(c, "absent"))
    present = next(v for c, v in pairs if cg.contains_phrase(c, "present"))
    assert present > 20 * absent, f"transcription {absent} to {present} is not a switch being turned on"
    assert absent > 0, "the low condition should still be measurable, not zero"
    return (f"transcription rises from {absent:.0f} to {present:.0f} units when the nutrient is "
            f"present, a factor of {present / absent:.0f}: switched on, not off")


def q22(table, item):
    pairs = _operon(table, ("scarce", "abundant"))
    scarce = next(v for c, v in pairs if cg.contains_phrase(c, "scarce"))
    abundant = next(v for c, v in pairs if cg.contains_phrase(c, "abundant"))
    assert scarce > 20 * abundant, f"transcription {scarce} to {abundant} is not a switch being turned off"
    assert abundant > 0, "the low condition should still be measurable, not zero"
    return (f"transcription falls from {scarce:.0f} to {abundant:.0f} units when the product is "
            f"abundant, a factor of {scarce / abundant:.0f}: switched off, not on")


def q24(table, item):
    before = "expression before the signal arbitrary units"
    after = "expression two hours after the signal arbitrary units"
    d = {cg.normalize(r["gene"]): (cg.num(r[before]), cg.num(r[after])) for r in _rows(table)}
    risers = sorted(g for g, v in d.items() if _fold(*v) > 5)
    flat = sorted(g for g, v in d.items() if 0.8 < _fold(*v) < 1.25)
    assert len(risers) == 3, f"{len(risers)} genes rise by more than fivefold, not three"
    assert len(flat) == 1 and set(risers) | set(flat) == set(d), \
        f"the four genes must split three and one; got {risers} and {flat}"
    assert not any(_fold(*v) < 0.8 for v in d.values()), "no gene falls, so the falling option is false"
    return (f"{risers} rise by more than a factor of five while {flat} does not move, so the "
            f"coordinated group is three of the four genes")


CLAIMS = [
 ("stretch of DNA that interacts with regulatory proteins to control transcription",
  "EK 6.5.A.1 states exactly this. The sequence is the DNA and the regulatory protein is what interacts with it, so options making the sequence RNA, a protein, or a translated product each reverse part of the definition."),
 ("expressed continually, while an inducible gene is expressed when it is turned on",
  "EK 6.5.A.1 states that some genes are constitutively expressed and others are inducible. Every cell carries the same genes, so presence does not separate them, and EK 6.5.B.1 gives regulated gene groups to both kinds of cell."),
 ("Inducible, because its expression is switched on under a particular condition",
  "EK 6.5.A.1 distinguishes constitutive from inducible expression, and a gene expressed only under a particular condition is the inducible case. Retaining a gene is not expressing it."),
 ("Constitutively expressed, because its transcription does not depend on a particular condition",
  "EK 6.5.A.1. A gene transcribed at a steady rate under every condition is the constitutive case; coordinate regulation under EK 6.5.B.1 concerns groups of genes regulated together rather than a gene expressed in every cell."),
 ("Gene 1",
  "EK 6.5.A.1 makes a constitutively expressed gene one whose expression does not depend on the condition. The table check recomputes the fold change for all three genes and confirms only one is both unchanged and substantially expressed, and that the rejected readings are false on the same numbers."),
 ("Gene 2",
  "EK 6.5.A.1 makes an inducible gene one whose expression is switched on. The table check recomputes the fold changes and confirms exactly one gene changes by more than a factor of ten while the others change by less than a factor of two."),
 ("Reversible modifications of DNA or histones",
  "EK 6.5.A.2 states that epigenetic changes can affect gene expression through reversible modifications of DNA or histones. Reversibility is the framework's own word and is what separates such a change from the alteration of a DNA sequence EK 6.7.A.1 calls a mutation."),
 ("reduces expression of the gene, and its effect is reversible",
  "EK 6.5.A.2. The table check recomputes that the modification goes low, high and low again while expression falls by more than fivefold and returns to within ten percent of its starting value, and that the final value is nonzero, which a deleted gene could not be."),
 ("combination of genes that are expressed and the levels at which they are expressed",
  "EK 6.5.A.3 states both halves, so an account resting on which genes are present, or on levels alone, drops one of them."),
 ("express different combinations of their genes and at different levels",
  "EK 6.5.A.3 makes a cell's phenotype the product of the combination of genes expressed and the levels of expression, so cells sharing a genome can differ in exactly that way. EK 6.4.A.3.iv makes the genetic code shared, and nothing in the framework has a differentiated cell discard genes."),
 ("expression of genes for tissue-specific proteins",
  "EK 6.5.A.3.i states that observable cell differentiation results from the expression of genes for tissue-specific proteins, locating differentiation in what is expressed rather than in genes lost, gained or rewritten."),
 ("Protein Q and protein R",
  "EK 6.5.A.3.i makes a tissue-specific protein one confined to a particular kind of cell. The table check counts detections per protein and confirms that two appear in exactly one cell type each while the third appears in all three."),
 ("Sequential gene expression",
  "EK 6.5.A.3.ii states that induction of transcription factors during development results in sequential gene expression. Intron removal is EK 6.3.A.4.iii's and replication EK 6.2.A.1's."),
 ("transcription factor appears first",
  "EK 6.5.A.3.ii. The table check recomputes the stage at which each of the three first appears and confirms the factor precedes both genes and that the two genes appear at different stages, so the expression is sequential rather than simultaneous."),
 ("function and amount of gene products",
  "EK 6.5.A.3.iii states that the function and amount of gene products determine the phenotype of organisms, and EK 6.5.A.3 names the levels of expression alongside the combination of genes expressed, which presence alone cannot capture."),
 ("amount of the gene product, and not merely whether it is made at all",
  "EK 6.5.A.3.iii. The table check confirms every individual makes some enzyme, so presence cannot separate them, and that the recorded amounts and the distinct phenotypes fall in the same order across a range wider than fivefold."),
 ("Both prokaryotes and eukaryotes",
  "EK 6.5.B.1 states that both prokaryotes and eukaryotes have groups of genes that are coordinately regulated, with operons in EK 6.5.B.1.i and shared transcription factors in EK 6.5.B.1.ii giving each group its mechanism."),
 ("operons in an inducible or a repressible system",
  "EK 6.5.B.1.i states that prokaryotes regulate operons in an inducible or repressible system. Alternative splicing is a processing step under EK 6.3.A.4.iii."),
 ("inducible system, because the presence of the substance switches transcription on",
  "EK 6.5.B.1.i names the two systems and EK 6.5.A.1 defines an inducible gene as one whose expression is switched on, so transcription appearing with the substance is induction. A repressible system is the opposite arrangement."),
 ("repressible system, because abundance of the end product switches transcription off",
  "EK 6.5.B.1.i names inducible and repressible systems for prokaryotic operons; a system switched off by the abundance of a substance is the repressible one. EK 6.5.B.1.ii gives eukaryotes shared transcription factors instead of operons."),
 ("inducible system, because transcription is far higher when the nutrient is present",
  "EK 6.5.B.1.i and EK 6.5.A.1. The table check recomputes the ratio between the two conditions and confirms transcription rises by more than a factor of ten in the presence of the nutrient, which is induction and not repression."),
 ("repressible system, because transcription is far lower when the product is abundant",
  "EK 6.5.B.1.i. The table check recomputes the ratio and confirms transcription falls by more than a factor of ten when the product is abundant, which is the repressible arrangement rather than the inducible one."),
 ("influenced by the same transcription factors",
  "EK 6.5.B.1.ii states that in eukaryotes groups of genes may be influenced by the same transcription factors to coordinately regulate expression. Operons are the prokaryotic arrangement under EK 6.5.B.1.i."),
 ("Three of the four genes rose together",
  "EK 6.5.B.1 and EK 6.5.B.1.ii. The table check recomputes each gene's fold change and confirms exactly three rise by more than a factor of three while the fourth does not move, and that no gene falls, so both the all-four and the falling readings are false."),
 ("rather than the stretch that is transcribed into the product",
  "EK 6.5.A.1 defines regulatory sequences as stretches of DNA that interact with regulatory proteins to control transcription, making them a target for proteins rather than the source of the transcribed product. Both are DNA."),
 ("no longer controlled in the way the interaction provided",
  "EK 6.5.A.1 makes the interaction between regulatory sequence and regulatory protein the source of the control over transcription, so losing the interaction removes that control over the gene concerned and nothing more."),
 ("returns when it is withdrawn, with the modification of histones tracking the change",
  "Suggested skill 6.A asks for a scientific claim and EK 6.5.A.2 requires both parts of one: an effect on gene expression and a modification of DNA or histones that is reversible. A change in the base sequence would be EK 6.7.A.1's mutation instead."),
 ("results in sequential gene expression, and that groups of genes may be influenced by the same transcription factors",
  "EK 6.5.A.3.ii supplies the order in time and EK 6.5.B.1.ii supplies the grouping of the genes that respond to one factor, which is what a fixed order across a set of genes requires."),
 ("same genes but express a different combination of them",
  "EK 6.5.A.3 makes a cell's phenotype the combination of genes expressed and the levels of expression, and EK 6.5.A.3.i attributes observable differentiation to the expression of genes for tissue-specific proteins. Nothing in the framework has a differentiating cell gain or lose genes."),
 ("epigenetic modifications are reversible, and groups of genes can be regulated together in both kinds of cell",
  "Each clause is one of the framework's own statements: EK 6.5.A.1, EK 6.5.A.2 and EK 6.5.B.1. Every rejected option contradicts at least one of the three."),
]

cg.check(b6_5, CLAIMS,
         table_checks={5: q5, 6: q6, 8: q8, 12: q12, 14: q14, 16: q16,
                       21: q21, 22: q22, 24: q24})
