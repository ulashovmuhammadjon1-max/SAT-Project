"""Key audit for AP BIOLOGY 6.3 Transcription and RNA Processing.

One (anchor, claim) per item, in module order. ``cg_check.check`` is the
structural gate; it is described in ``verify_b5_3.py``.

WHAT IS RECOMPUTED. The splicing arithmetic is the checkable part of this topic
and it is not asserted anywhere: ``_splice`` below reads the primary transcript
table, separates introns from exons by their own labels, and returns the mature
length, the excised length and the whole. Both numeric items are keyed to those
returns and every distractor value is checked against them, so an item keyed to
the intron total when it means the exon total cannot ship. The alternative
splicing table is recomputed by parsing the exon numbers out of each version and
intersecting them, and the two processing comparisons are recomputed as
directional effects with the control condition identified from the table rather
than from the stem.

A NOTE ON WHAT IS NOT ASSERTED. The framework does not say that prokaryotes lack
introns, that the poly-A tail is added at the 3 prime end, or which enzyme adds
the cap. None of those is keyed anywhere in this module. The only claim made
about where processing happens is EK 6.3.A.4's own opening words, in eukaryotic
cells.

NEGATIVE CONTROL: ``negcontrol_b5_7.py``.
"""
import re

import cg_check as cg
import b6_3

T_SPLICE = b6_3._T_SPLICE
T_ALT = b6_3._T_ALT
T_TAIL = b6_3._T_TAIL
T_CAP = b6_3._T_CAP


def _rows(table):
    heads = [cg.normalize(h) for h in table["headers"]]
    return [dict(zip(heads, r)) for r in table["rows"]]


def _splice(table):
    """Mature length, excised length and total, from the segment table alone."""
    exons, introns = [], []
    for r in _rows(table):
        label = cg.normalize(r["segment of the primary transcript"])
        n = cg.num(r["length in nucleotides"])
        if label.startswith("exon"):
            exons.append(n)
        elif label.startswith("intron"):
            introns.append(n)
        else:
            raise AssertionError(f"segment {label!r} is neither an exon nor an intron")
    assert exons and introns, "the transcript must contain both exons and introns"
    return sum(exons), sum(introns), sum(exons) + sum(introns)


def q13(table, item):
    mature, excised, total = _splice(table)
    assert mature == 540, f"the exon total recomputes to {mature}, not 540"
    for wrong in (excised, total, max(0, total - mature - 40), total - excised - 230):
        assert wrong != mature, f"a distractor value {wrong} coincides with the key"
    return (f"the exons sum to {mature:.0f} nucleotides, the introns to {excised:.0f}, and the "
            f"whole transcript to {total:.0f}; only the exons are retained")


def q14(table, item):
    mature, excised, total = _splice(table)
    assert excised == 850, f"the intron total recomputes to {excised}, not 850"
    assert excised != mature and excised != total, \
        "the removed total must be distinguishable from the retained and whole totals"
    longest = max(cg.num(r["length in nucleotides"]) for r in _rows(table)
                  if cg.normalize(r["segment of the primary transcript"]).startswith("intron"))
    assert longest != excised, "the single longest intron must not equal the intron total"
    return (f"the two introns sum to {excised:.0f} nucleotides, against {mature:.0f} retained and "
            f"{total:.0f} in the whole transcript; the longest single intron is {longest:.0f}")


_VERSION = re.compile(r"version [0-9]+$")
# The exon list must be exactly "exons N, N and N" and nothing else. A loose
# findall over the cell would happily parse numbers out of a cell that had
# acquired extra text, which is how a table check ends up not reading its table
# at all -- the negative control caught this file doing exactly that.
_EXONS = re.compile(r"exons(?: [0-9]+)+ and [0-9]+$")


def q15(table, item):
    versions = {}
    for r in _rows(table):
        cell = cg.normalize(r["exons retained in that version"])
        assert _EXONS.fullmatch(cell), f"exon list {cell!r} is not of the form 'exons 1 2 and 3'"
        label = cg.normalize(r["mature mrna version recovered"])
        assert _VERSION.fullmatch(label), f"version label {label!r} is not of the form 'version 1'"
        nums = {int(n) for n in re.findall(r"(?<![0-9])[0-9]+(?![0-9])", cell)}
        assert nums, f"no exon numbers parsed from {cell!r}"
        versions[label] = nums
    assert len(versions) >= 3, "the key needs at least three recovered versions"
    assert len(set(map(frozenset, versions.values()))) == len(versions), \
        "the versions must differ from one another, or nothing needs explaining"
    common = set.intersection(*versions.values())
    assert common == {1, 4}, f"the exons present in every version are {sorted(common)}, not 1 and 4"
    for n in (2, 3):
        assert any(n not in v for v in versions.values()), \
            f"exon {n} appears in every version, so it belongs in the common set too"
    return (f"{len(versions)} distinct exon sets were recovered from one gene; the intersection is "
            f"{sorted(common)} and exons 2 and 3 are each absent from one version")


def _paired(table, flag_col, value_col, label_col):
    rows = _rows(table)
    assert len(rows) == 2, "a controlled comparison needs exactly two preparations"
    by_flag = {cg.normalize(r[cg.normalize(flag_col)]): r for r in rows}
    assert set(by_flag) == {"yes", "no"}, f"the two preparations are marked {set(by_flag)}"
    with_it = cg.num(by_flag["yes"][cg.normalize(value_col)])
    without = cg.num(by_flag["no"][cg.normalize(value_col)])
    for v in (with_it, without):
        assert 0 <= v <= 100, f"{value_col!r} holds {v}, which is not a percentage"
    assert by_flag["yes"][cg.normalize(label_col)] != by_flag["no"][cg.normalize(label_col)], \
        "the two rows must be distinguishable preparations"
    return with_it, without


def q16(table, item):
    with_tail, without = _paired(table, "Poly-A tail present",
                                 "Percent of the mRNA still intact after four hours",
                                 "mRNA preparation")
    assert with_tail > without, \
        f"the tailed preparation retained {with_tail} against {without}; the key needs it higher"
    assert with_tail - without > 25, "the difference must be large enough to call an effect"
    return (f"{with_tail:.0f} percent intact with a poly-A tail against {without:.0f} percent "
            f"without, a difference of {with_tail - without:.0f} points in the direction of stability")


def q17(table, item):
    with_cap, without = _paired(table, "GTP cap present",
                                "Percent of transcripts bound by a ribosome within ten minutes",
                                "mRNA preparation")
    assert with_cap > without, \
        f"the capped preparation was bound {with_cap} against {without}; the key needs it higher"
    assert with_cap - without > 25, "the difference must be large enough to call an effect"
    return (f"{with_cap:.0f} percent bound by a ribosome with a GTP cap against {without:.0f} "
            f"percent without, a difference of {with_cap - without:.0f} points in the direction of recognition")


CLAIMS = [
 ("information from DNA in the nucleus to the ribosome in the cytoplasm",
  "EK 6.3.A.1.i states exactly this for messenger RNA. Binding an amino acid with an anticodon is tRNA's role under EK 6.3.A.1.ii and being a functional building block of the ribosome is rRNA's under EK 6.3.A.1.iii."),
 ("binds a specific amino acid and carries an anticodon sequence",
  "EK 6.3.A.1.ii states that distinct tRNA molecules bind specific amino acids and have anticodon sequences that base pair with the codons of mRNA. The reversed option is wrong twice over, since a codon belongs to the mRNA and an amino acid is not a sequence."),
 ("functional building blocks of ribosomes",
  "EK 6.3.A.1.iii states that ribosomal RNA molecules are functional building blocks of ribosomes. The template in transcription is a strand of DNA under EK 6.3.A.2, not an RNA molecule."),
 ("structure of the RNA molecule",
  "EK 6.3.A.1 states that the sequence of the RNA bases, together with the structure of the RNA molecule, determines RNA function. Structure is the second determinant the framework names, and length is not among them."),
 ("single template strand, which directs the inclusion of bases",
  "EK 6.3.A.2 states that RNA polymerases use a single template strand of DNA to direct the inclusion of bases in the newly formed RNA molecule. Using both strands would yield two different RNA molecules from one gene."),
 ("Transcription",
  "EK 6.3.A.2 names the process by which RNA polymerase uses a single DNA template strand to direct the inclusion of bases in a new RNA molecule as transcription. Splicing is EK 6.3.A.4.iii's separate modification and translation is EK 6.4.A.3's."),
 ("reading the template in the 3 prime to 5 prime direction",
  "EK 6.3.A.3 states that RNA polymerase synthesizes mRNA in the 5 prime to 3 prime direction by reading the template DNA strand in the 3 prime to 5 prime direction. The two directions are opposite, which rules out both same-direction options."),
 ("3 prime end, because the template is read in the 3 prime to 5 prime direction",
  "EK 6.3.A.3 fixes the reading direction of the template, so reading starts from the end that direction begins at. The direction of synthesis given in the same statement is the opposite one and so cannot locate the template's starting end."),
 ("makes the mRNA more stable",
  "EK 6.3.A.4.i states that the addition of a poly-A tail makes mRNA more stable. Ribosomal recognition is what EK 6.3.A.4.ii assigns to the GTP cap."),
 ("helps with ribosomal recognition",
  "EK 6.3.A.4.ii states that the addition of a GTP cap helps with ribosomal recognition. Stability is what EK 6.3.A.4.i assigns to the poly-A tail."),
 ("introns are excised and the exons are spliced together and retained",
  "EK 6.3.A.4.iii states that the excision of introns, along with the splicing and retention of exons, generates the mature mRNA. The reversed option removes exactly what the framework keeps."),
 ("Different combinations of exons can be retained",
  "EK 6.3.A.4.iii states that this generates different versions of the resulting mature mRNA molecule and names the process alternative splicing. EK 6.3.A.2 allows only one template strand, so no second version can come from the other one."),
 ("540 nucleotides",
  "EK 6.3.A.4.iii retains the spliced exons and excises the introns, so the mature length is the exon total. The table check recomputes the exon total as 540, the intron total as 850 and the whole transcript as 1390, and confirms no distractor value equals the key."),
 ("850 nucleotides, the total length of the introns",
  "EK 6.3.A.4.iii excises the introns while the exons are spliced and retained, so what is removed is the intron total. The table check recomputes it as 850 and confirms it differs from the retained total, the whole transcript and the single longest intron."),
 ("first and fourth exons appear in every version",
  "EK 6.3.A.4.iii states that the excision of introns with the splicing and retention of exons generates different versions of the mature mRNA, which the framework names alternative splicing. The table check parses the exon numbers from each version, confirms the three versions differ, and intersects them."),
 ("survived far better, which is the stability the tail confers",
  "EK 6.3.A.4.i states that the addition of a poly-A tail makes mRNA more stable. The table check identifies the control from the table's own column, confirms the direction of the difference and confirms it is larger than 25 percentage points."),
 ("bound by ribosomes far more often",
  "EK 6.3.A.4.ii states that the addition of a GTP cap helps with ribosomal recognition. The table check identifies the control from the table's own column, confirms the direction of the difference and confirms it is larger than 25 percentage points."),
 ("In eukaryotic cells",
  "EK 6.3.A.4 opens by stating that in eukaryotic cells the mRNA transcript undergoes a series of enzyme-mediated modifications, and the three listed modifications are given for that setting. EK 6.3.A.1.i likewise places the transcript's journey as beginning in a nucleus."),
 ("broken down sooner",
  "EK 6.3.A.4.i states that the addition of a poly-A tail makes mRNA more stable, so removing the modification removes the stability. Recognition is the cap's contribution under EK 6.3.A.4.ii and excision a separate modification under EK 6.3.A.4.iii."),
 ("recognize the transcripts less readily",
  "EK 6.3.A.4.ii states that the addition of a GTP cap helps with ribosomal recognition, so its absence impairs recognition. The direction of reading is fixed by EK 6.3.A.3 and is unrelated to processing."),
 ("excision of that intron",
  "EK 6.3.A.4.iii names the excision of introns, along with the splicing and retention of exons, as the modification producing the mature mRNA, so a retained intron is a failure of that excision. The tail and the cap have the separate roles of EK 6.3.A.4.i and EK 6.3.A.4.ii."),
 ("base pair with the codons of mRNA",
  "EK 6.3.A.1.ii states that tRNA molecules bind specific amino acids and have anticodon sequences that base pair with the codons of mRNA. Altering the anticodon alters which codon the molecule pairs with while leaving the bound amino acid unchanged."),
 ("ribosome, of which ribosomal RNA molecules are functional building blocks",
  "EK 6.3.A.1.iii states that rRNA molecules are functional building blocks of ribosomes, so losing them affects that structure. The anticodon belongs to tRNA under EK 6.3.A.1.ii."),
 ("while copying DNA uses both original strands as templates",
  "EK 6.3.A.2 gives transcription a single template strand and EK 6.2.A.1.ii makes replication semiconservative, with each original strand templating a new complementary strand. Both build their new molecule in the 5 prime to 3 prime direction under EK 6.3.A.3 and EK 6.2.A.1.i, so direction does not separate them."),
 ("Messenger RNA carries the information, transfer RNA brings amino acids",
  "The three roles are stated separately in EK 6.3.A.1.i, EK 6.3.A.1.ii and EK 6.3.A.1.iii, and this option is the only one that assigns each to the molecule the framework assigns it to."),
 ("together with the structure of the molecule, determines RNA function",
  "EK 6.3.A.1 states that the sequence of the RNA bases, together with the structure of the RNA molecule, determines RNA function. Length is not among the determinants the framework names, which is why similar lengths do not imply similar behaviour."),
 ("begins at the DNA in the nucleus and ends at the ribosome in the cytoplasm",
  "EK 6.3.A.1.i states that messenger RNA molecules carry information from DNA in the nucleus to the ribosome in the cytoplasm, and the direction of that journey is part of the statement."),
 ("copies a template strand, the transcript is capped, tailed and spliced",
  "The order follows from the statements: EK 6.3.A.2 makes transcription the copying of a single template strand, EK 6.3.A.4 applies its modifications to the resulting transcript, and EK 6.3.A.1.i has the mature mRNA carry the information to the ribosome. Nothing can be modified before it exists."),
 ("Alternative splicing",
  "EK 6.3.A.4.iii states that the excision of introns with the splicing and retention of exons generates different versions of the resulting mature mRNA and names it alternative splicing. Neither the tail nor the cap changes which bases the mature transcript contains."),
 ("a single strand served as the template",
  "EK 6.3.A.2 states that RNA polymerases use a single template strand of DNA to direct the inclusion of bases in the newly formed RNA molecule, and EK 6.3.A.3 adds that this template is read in the 3 prime to 5 prime direction, which is why the opposite reading direction misstates the framework."),
]

cg.check(b6_3, CLAIMS, table_checks={13: q13, 14: q14, 15: q15, 16: q16, 17: q17})
print("    Splicing arithmetic recomputed from the segment table; alternative splicing")
print("    intersection parsed from the version table; both processing comparisons directional.")
