"""Key audit for AP BIOLOGY 6.6 Gene Expression and Cell Specialization.

One (anchor, claim) per item, in module order. ``cg_check.check`` is the
structural gate; it is described in ``verify_b5_3.py``.

WHAT IS RECOMPUTED. Six items carry data. Every one is a claim-and-evidence item
in the shape suggested skill 6.B asks for, so what the checks below recompute is
the DIRECTION and SIZE of the effect the keyed claim asserts, together with the
falsity of the opposite claim on the same numbers -- because in a claim item the
opposite claim is always among the choices and a key that merely sounds right is
indistinguishable from one that is right. Two of the checks do more: the
positional item confirms the two positions give results within twenty percent of
each other AND that removing the sequence collapses transcription, since the key
rests on both; and the small RNA item confirms one treatment lowers the mRNA and
the other does not while both lower the protein, which is what makes the keyed
claim about the protein correct and the mRNA-only claim wrong.

WHAT IS NOT CLAIMED. EK 6.6.B.2 says only that certain small RNA molecules have
roles in regulating gene expression. It names no mechanism, and no key here
names one: the small RNA items are keyed to the amount of the gene's product,
which is what the data show.

NEGATIVE CONTROL: ``negcontrol_b5_7.py``.
"""
import cg_check as cg
import b6_6

T_TF = b6_6._T_TF
T_NEG = b6_6._T_NEG
T_POS = b6_6._T_POS
T_CELLS = b6_6._T_CELLS
T_SMALL = b6_6._T_SMALL
T_TFCELL = b6_6._T_TFCELL


def _rows(table):
    heads = [cg.normalize(h) for h in table["headers"]]
    return [dict(zip(heads, r)) for r in table["rows"]]


def _two_way(table, flag_col, value_col):
    """A yes/no pair of conditions and their measurements, checked to be clean."""
    rows = _rows(table)
    assert len(rows) == 2, "a two-condition comparison needs exactly two rows"
    by_flag = {cg.normalize(r[cg.normalize(flag_col)]): cg.num(r[cg.normalize(value_col)])
               for r in rows}
    assert set(by_flag) == {"yes", "no"}, f"the two rows are marked {set(by_flag)}, not yes and no"
    assert all(v >= 0 for v in by_flag.values()), "a negative transcription measurement is not data"
    return by_flag["yes"], by_flag["no"]


def q6(table, item):
    present, absent = _two_way(table, "Transcription factor 1 present",
                               "Transcription of the reporter gene (arbitrary units)")
    assert present > 10 * absent, \
        f"transcription is {present} with the factor and {absent} without; the key needs it to depend on the factor"
    assert absent > 0, "the control must be measurable, so 'no transcription at all' is not the claim"
    return (f"transcription is {present:.0f} units with the factor and {absent:.0f} without, a "
            f"factor of {present / absent:.0f}: required, not inhibitory and not irrelevant")


def q7(table, item):
    added, without = _two_way(table, "Molecule M added",
                              "Transcription of the gene (arbitrary units)")
    assert without > 10 * added, \
        f"transcription is {without} without the molecule and {added} with it; the key needs a fall"
    assert added > 0, "some transcription must remain, so the molecule is not a requirement being removed"
    return (f"transcription falls from {without:.0f} to {added:.0f} units when the molecule is added, "
            f"a factor of {without / added:.0f}: negative, not positive and not neutral")


def q8(table, item):
    rows = _rows(table)
    col = "transcription of the gene arbitrary units"
    pos = "position of the regulatory sequence relative to the transcription start site"
    d = {cg.normalize(r[pos]): cg.num(r[col]) for r in rows}
    up = d["upstream"]
    down = d["downstream"]
    gone = next(v for k, v in d.items() if cg.contains_phrase(k, "removed"))
    assert abs(up - down) / max(up, down) < 0.2, \
        f"upstream {up} and downstream {down} differ too much to say the side makes little difference"
    assert min(up, down) > 5 * gone, \
        f"removing the sequence must collapse transcription; got {gone} against {min(up, down)}"
    assert gone > 0, "some transcription must remain without the sequence, so 'no effect' stays false"
    return (f"upstream {up:.0f} and downstream {down:.0f} are within twenty percent of each other, "
            f"and removing the sequence drops transcription to {gone:.0f}")


def q10(table, item):
    liver = "expression in liver cells arbitrary units"
    muscle = "expression in muscle cells arbitrary units"
    d = {cg.normalize(r["gene"]): (cg.num(r[liver]), cg.num(r[muscle])) for r in _rows(table)}
    def ratio(v):
        return max(v) / min(v) if min(v) > 0 else float("inf")
    differ = sorted(g for g, v in d.items() if ratio(v) > 10)
    same = sorted(g for g, v in d.items() if ratio(v) < 1.3)
    assert len(differ) == 2, f"{len(differ)} genes differ by more than tenfold, not two"
    assert len(same) == 1 and set(differ) | set(same) == set(d), \
        f"the three genes must split two and one; got {differ} and {same}"
    return (f"{differ} differ by more than tenfold between the two cell types while {same} reads "
            f"{d[same[0]]}, so the differential expression involves two of the three")


def q12(table, item):
    rows = _rows(table)
    mrna = "amount of the target gene's mrna arbitrary units"
    prot = "amount of the target gene's protein arbitrary units"
    d = {cg.normalize(r["treatment of the cells"]): (cg.num(r[mrna]), cg.num(r[prot]))
         for r in rows}
    control = next(k for k in d if cg.contains_phrase(k, "no small rna supplied"))
    treated = [k for k in d if k != control]
    assert len(treated) == 2, f"expected two small RNA treatments; got {treated}"
    c_mrna, c_prot = d[control]
    for k in treated:
        assert d[k][1] < c_prot / 5, \
            f"{k} leaves the protein at {d[k][1]}, which is not a sharp fall from {c_prot}"
    keeps_mrna = [k for k in treated if d[k][0] > 0.8 * c_mrna]
    drops_mrna = [k for k in treated if d[k][0] < c_mrna / 5]
    assert len(keeps_mrna) == 1 and len(drops_mrna) == 1, \
        f"one treatment should leave the mRNA and one should lower it; got {keeps_mrna} and {drops_mrna}"
    return (f"both treatments drop the protein from {c_prot:.0f} units to under a fifth, while "
            f"{keeps_mrna} leaves the mRNA near {c_mrna:.0f} and {drops_mrna} lowers it")


def q18(table, item):
    rows = _rows(table)
    d = {cg.normalize(r["cell type"]): (cg.normalize(r["transcription factor 2 present"]) == "yes",
                                        cg.normalize(r["target gene expressed"]) == "yes")
         for r in rows}
    assert all(tf == expr for tf, expr in d.values()), \
        f"presence of the factor and expression of the gene do not coincide: {d}"
    withtf = sorted(k for k, v in d.items() if v[0])
    assert 0 < len(withtf) < len(d), \
        "the factor must be present in some cell types and absent in others, or nothing is shown"
    return (f"the factor is present in {withtf} and absent elsewhere, and the target gene is "
            f"expressed in exactly those cell types")


CLAIMS = [
 ("RNA polymerase and transcription factors",
  "EK 6.6.A.1 states that RNA polymerase and transcription factors bind to promoter or enhancer DNA sequences to initiate transcription. DNA polymerase and ligase belong to replication under EK 6.2.A.1 and the named RNA types to translation under EK 6.3.A.1."),
 ("Either upstream or downstream",
  "EK 6.6.A.1 states that these sequences can be upstream or downstream of the transcription start site, so the framework confines a regulatory sequence to neither side, and they are DNA rather than part of the transcript."),
 ("consistent with the framework, which allows these sequences on either side",
  "EK 6.6.A.1 permits promoter or enhancer sequences upstream or downstream of the transcription start site, so a downstream location is not grounds for doubting the result. The framework assigns no side to either kind of sequence."),
 ("binding to DNA and blocking transcription",
  "EK 6.6.A.2 states that negative regulatory molecules inhibit gene expression by binding to DNA and blocking transcription, naming both the target and the step, so moving the action to the transcript or the finished protein changes the statement."),
 ("binds a promoter or enhancer to initiate transcription, while the negative regulatory molecule binds DNA to block it",
  "EK 6.6.A.1 has transcription factors initiate transcription at promoter or enhancer sequences and EK 6.6.A.2 has negative regulatory molecules bind DNA and block it, so the difference is the direction of the effect rather than the kind of target."),
 ("depends on the presence of transcription factor 1",
  "EK 6.6.A.1 makes transcription factors participants in initiating transcription, and skill 6.B asks for the claim the data support. The table check recomputes a more than tenfold fall in the factor's absence and confirms the control is nonzero, so the inhibitory, neutral and all-or-nothing readings are all false."),
 ("negative regulator of this gene",
  "EK 6.6.A.2 states that negative regulatory molecules inhibit gene expression by binding to DNA and blocking transcription. The table check recomputes a more than tenfold fall on adding the molecule and confirms transcription still occurs without it, so the molecule is not a requirement for transcription."),
 ("increases transcription from either side",
  "EK 6.6.A.1 states that promoter or enhancer sequences can be upstream or downstream of the transcription start site. The table check confirms the two positions differ by less than twenty percent and that removing the sequence drops transcription more than fivefold, which is both halves of the key."),
 ("Differential gene expression, which influences cell products and functions",
  "EK 6.6.B.1 states exactly this. Base pairing is conserved under EK 6.1.B.1 and the genetic code shared under EK 6.4.A.3.iv, neither of which regulation alters."),
 ("Two of the three genes are expressed very differently",
  "EK 6.6.B.1 makes differential gene expression the result of regulation. The table check recomputes the ratio between the two cell types for each gene and confirms exactly two exceed tenfold while the third is within thirty percent, so the all-three reading is false on the same numbers."),
 ("Certain small RNA molecules have roles in regulating gene expression",
  "EK 6.6.B.2 states exactly this. The rejected options assign small RNAs the roles the framework gives to the DNA template in EK 6.3.A.2, to rRNA in EK 6.3.A.1.iii and to tRNA in EK 6.3.A.1.ii."),
 ("Both small RNA molecules reduce the amount of the target gene's protein",
  "EK 6.6.B.2 states that certain small RNA molecules have roles in regulating gene expression. The table check confirms both treatments drop the protein below a fifth of the control while exactly one of them also lowers the mRNA, which is what makes the mRNA-only reading false."),
 ("no longer initiated at its usual rate",
  "EK 6.6.A.1 makes initiation depend on molecules binding promoter or enhancer sequences, so a promoter that cannot be bound cannot serve that function. Nothing in the framework allows translation without a transcript or alters the shared code of EK 6.4.A.3.iv."),
 ("transcribed at a much lower rate",
  "EK 6.6.A.1 names transcription factors alongside RNA polymerase as the molecules that bind promoter or enhancer sequences to initiate transcription, so losing one lowers initiation of its targets. Blocking is EK 6.6.A.2's role for a different class of molecule."),
 ("Removing the segment sharply reduces transcription of that gene",
  "EK 6.6.A.1 makes a regulatory sequence one that molecules bind in order to initiate transcription, so the supporting evidence is a change in that gene's transcription when the segment is altered. Position cannot support the claim because EK 6.6.A.1 allows either side."),
 ("reduces transcription, and the protein is found bound to the gene's DNA",
  "EK 6.6.A.2 names two things a negative regulatory molecule does, inhibit expression and bind DNA, so the supporting evidence has to show both. Evidence of an increase supports the opposite claim."),
 ("results in differential gene expression, which in turn influences cell products and functions",
  "EK 6.6.B.1 states the direction of the account: regulation gives differential expression, which influences cell products and functions. The reversed option makes the outcome the cause, and EK 6.4.A.3.iv makes the code shared."),
 ("expressed in exactly the cell types in which transcription factor 2 is present",
  "EK 6.6.A.1 has transcription factors initiate transcription and EK 6.6.B.1 makes differential expression the result. The table check confirms presence and expression coincide in every row and that the factor is present in some cell types and absent in others."),
 ("molecule that binds, and the sequence is the stretch of DNA it binds to",
  "EK 6.6.A.1 places RNA polymerase and transcription factors on the binding side and the promoter or enhancer on the DNA side; EK 6.5.A.1 makes the same division for regulatory proteins and regulatory sequences."),
 ("differ in which regulatory molecules are present",
  "EK 6.6.A.1 and EK 6.6.A.2 make transcription depend on which molecules are present to bind the gene's DNA, and EK 6.6.B.1 makes the resulting differential expression the source of the differences between cells."),
 ("certain small RNA molecules have roles in regulating gene expression",
  "EK 6.6.B.2 states this as a claim about the regulation of expression rather than about sequence, and the stem states the gene itself is unchanged. Delivering amino acids is tRNA's role under EK 6.3.A.1.ii."),
 ("negative regulatory molecule, which inhibits expression by binding DNA",
  "EK 6.6.A.2 requires both a fall in transcription and binding to DNA, and the observation supplies both. An enhancer is a DNA sequence rather than a molecule that binds DNA under EK 6.6.A.1."),
 ("falls sharply, because the sequence that molecules bind in order to initiate it is gone",
  "EK 6.6.A.1 makes initiation depend on molecules binding a promoter or enhancer, so deleting the promoter removes what initiation depends on. Blocking is EK 6.6.A.2's role for negative regulatory molecules, not a promoter's."),
 ("binding an enhancer initiates transcription, while a negative regulatory molecule binding DNA blocks it",
  "EK 6.6.A.1 and EK 6.6.A.2 assign opposite directions to the two kinds of molecule, and both act at the DNA before any transcript exists."),
 ("Regulatory molecules act on a gene's DNA, transcription of that gene changes",
  "EK 6.6.A.1 and EK 6.6.A.2 place regulatory molecules on the DNA affecting transcription, and EK 6.6.B.1 carries that through to cell products and functions. EK 6.5.A.3.iii makes the amount of the product part of what sets the phenotype."),
 ("act from either side of the transcription start site",
  "EK 6.6.A.1 states that promoter or enhancer sequences can be upstream or downstream of the transcription start site, so one sequence working from both positions is what the framework describes. The sequence is DNA, not part of the transcript."),
 ("expressed at very different levels in the two cell types that share a genome",
  "Skill 6.B asks for evidence supporting a claim and EK 6.6.B.1 makes differential gene expression the thing to demonstrate. A shared chromosome number, code, size or organelle is common ground rather than the difference the claim is about."),
 ("transcription factor acting at a promoter or enhancer",
  "EK 6.6.A.1 states that RNA polymerase and transcription factors bind promoter or enhancer DNA sequences to initiate transcription, and both observations fit it. A negative regulatory molecule under EK 6.6.A.2 would accompany transcription being blocked, and a protein is not an RNA molecule."),
 ("determines which of the cell's genes are expressed",
  "EK 6.6.B.1 states that gene regulation results in differential gene expression and influences cell products and functions, placing the effect on expression rather than on the genes themselves. A change in a base sequence is EK 6.7.A.1's mutation."),
 ("other molecules bind DNA to block it, certain small RNA molecules regulate expression",
  "Each clause of the keyed option is one of the framework's own statements: EK 6.6.A.1 for the binding molecules and the two positions, EK 6.6.A.2 for negative regulatory molecules, EK 6.6.B.2 for small RNAs, and EK 6.6.B.1 for differential expression influencing cell products and functions."),
]

cg.check(b6_6, CLAIMS, table_checks={6: q6, 7: q7, 8: q8, 10: q10, 12: q12, 18: q18})
