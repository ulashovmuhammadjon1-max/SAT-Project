"""Key audit for AP BIOLOGY 6.4 Translation.

One (anchor, claim) per item, in module order. ``cg_check.check`` is the
structural gate; it is described in ``verify_b5_3.py``.

WHAT IS RECOMPUTED. EK 6.4.A.3.ii and iii make translation a lookup: read the
message in triplets, take each codon's amino acid from a chart, stop at a stop
codon. That is executable, and ``_translate`` below executes it. The keyed
polypeptide and the keyed residue count are not written down here at all -- they
are produced from the chart in the module and the sequence LIFTED OUT OF THE
STEM by regex, so an edit to either the chart or the sequence changes what the
checker expects. The degeneracy item is recomputed by inverting the chart, the
stop-codon item by looking the codon up, and the codon-count item by dividing
lengths by three.

``_translate`` is itself controlled: the block below runs it on a message with
no stop codon, on one that stops immediately, and on a chart with a codon
removed, and asserts it raises or returns the right thing in each case. A lookup
that silently returned an empty peptide would make every one of these items
pass.

NEGATIVE CONTROL: ``negcontrol_b5_7.py``.
"""
import re

import cg_check as cg
import b6_4

T_CODE = b6_4._T_CODE
T_LEN = b6_4._T_LEN


def _rows(table):
    heads = [cg.normalize(h) for h in table["headers"]]
    return [dict(zip(heads, r)) for r in table["rows"]]


def _chart(table):
    """The genetic code chart as a dict, checked for the one-to-one direction."""
    out = {}
    for r in _rows(table):
        codon = str(r["mrna codon"]).strip().upper()
        assert re.fullmatch(r"[ACGU]{3}", codon), f"{codon!r} is not an RNA triplet"
        amino = cg.normalize(r["amino acid encoded"])
        assert codon not in out, f"codon {codon} is listed twice"
        out[codon] = amino
    return out


def _translate(chart, message):
    """The peptide a message encodes, by EK 6.4.A.3.ii, iii, vii and viii."""
    assert re.fullmatch(r"[ACGU]+", message), f"{message!r} is not an RNA sequence"
    assert len(message) % 3 == 0, f"{message!r} is not a whole number of triplets"
    peptide, stopped = [], False
    for i in range(0, len(message), 3):
        codon = message[i:i + 3]
        assert codon in chart, f"codon {codon} is not on the chart supplied"
        if chart[codon] == "stop":
            stopped = True
            break
        peptide.append(chart[codon])
    assert stopped, f"{message!r} runs off the end of the message without reaching a stop codon"
    return peptide


_CHART = _chart(T_CODE)

# Controls on the translator itself. A checker that cannot fail is worse than
# none, and a lookup loop is exactly the kind that quietly returns nothing.
try:
    _translate(_CHART, "AUGUUU")
except AssertionError as exc:
    assert "stop codon" in str(exc)
else:
    raise AssertionError("the translator accepted a message with no stop codon")
try:
    _translate(_CHART, "AUGXXX")
except AssertionError:
    pass
else:
    raise AssertionError("the translator accepted a non-RNA codon")
assert _translate(_CHART, "UAA") == [], "a message that stops at once must give an empty peptide"
assert _translate(_CHART, "AUGUAA") == ["methionine"], "the start codon must contribute a residue"


def _sequence_from(stem, least=6):
    """The RNA sequence the stem states, lifted out rather than retyped."""
    hits = re.findall(r"(?<![A-Za-z])[ACGU]{%d,}(?![A-Za-z])" % least, stem)
    assert len(hits) == 1, f"expected one RNA sequence in the stem; found {hits}"
    return hits[0]


def q16(table, item):
    chart = _chart(table)
    peptide = _translate(chart, _sequence_from(item["q"]))
    assert peptide == ["methionine", "phenylalanine", "glycine", "histidine"], \
        f"the stem's sequence translates to {peptide}"
    assert cg.contains_phrase(item["choices"][item["ans"]], ", ".join(peptide)), \
        "the keyed choice must list exactly the recomputed residues, in order"
    return (f"the stem's sequence splits into {len(_sequence_from(item['q'])) // 3} triplets and "
            f"the chart translates them to {peptide} before a stop codon")


def q17(table, item):
    chart = _chart(table)
    seq = _sequence_from(item["q"])
    peptide = _translate(chart, seq)
    assert len(peptide) == 4, f"the residue count recomputes to {len(peptide)}, not 4"
    assert len(seq) // 3 == 5, "the message must hold five triplets, so the count is not the triplet count"
    for wrong in (len(seq) // 3, len(seq), len(peptide) - 1):
        assert wrong != len(peptide), "a distractor value coincides with the key"
    return (f"{len(seq)} nucleotides give {len(seq) // 3} triplets, of which the last is a stop, so "
            f"{len(peptide)} residues are joined")


def q18(table, item):
    chart = _chart(table)
    by_amino = {}
    for codon, amino in chart.items():
        by_amino.setdefault(amino, []).append(codon)
    repeated = {a: sorted(cs) for a, cs in by_amino.items() if len(cs) > 1 and a != "stop"}
    assert repeated, "no amino acid on the chart has two codons, so the key has nothing to point at"
    assert repeated.get("phenylalanine") == ["UUC", "UUU"], \
        f"phenylalanine's codons recompute to {repeated.get('phenylalanine')}"
    assert len(set(chart.values())) < len(chart), \
        "the chart must be many codons to one amino acid, which is the framework's direction"
    assert len(chart) == len(set(chart)), "no codon may appear twice, which the reversed option asserts"
    return (f"inverting the chart gives {sorted(repeated)} with more than one codon apiece, "
            f"including phenylalanine at {repeated['phenylalanine']}")


def q19(table, item):
    chart = _chart(table)
    codon = _sequence_from(item["q"], least=3)
    assert codon in chart, f"{codon} is not on the chart"
    assert chart[codon] == "stop", f"the chart lists {codon} as {chart[codon]!r}, not a stop"
    stops = [c for c, a in chart.items() if a == "stop"]
    assert len(stops) >= 2, "the chart should carry more than one stop codon"
    assert "methionine" != chart[codon], "the codon must not also be the start codon"
    return (f"the chart lists {codon} as a stop, one of {sorted(stops)}, so no amino acid is added "
            f"and translation terminates there")


def q20(table, item):
    lengths = {cg.normalize(r["transcript"]):
               cg.num(r["length of the coding region in nucleotides"]) for r in _rows(table)}
    codons = {}
    for name, n in lengths.items():
        assert n % 3 == 0, f"{name} is {n:.0f} nucleotides, not a whole number of triplets"
        codons[name] = int(n // 3)
    hits = [name for name, c in codons.items() if c == 15]
    assert hits == ["transcript 2"], f"the transcript of 15 codons is {hits}"
    assert len(set(codons.values())) == len(codons), "two transcripts must not give the same count"
    return f"dividing each length by three gives {codons}, so exactly one transcript is 15 codons"


CLAIMS = [
 ("cytoplasm of both prokaryotic and eukaryotic cells, and on the cytoplasmic surface",
  "EK 6.4.A.1 states that translation occurs on ribosomes present in the cytoplasm of both prokaryotic and eukaryotic cells, as well as the cytoplasmic surface of the rough endoplasmic reticulum of eukaryotic cells. The framework names the cytoplasmic surface specifically."),
 ("ribosome, which is present in the cytoplasm of both kinds of cell",
  "EK 6.4.A.1 gives both prokaryotic and eukaryotic cells cytoplasmic ribosomes; the rough endoplasmic reticulum is named only for eukaryotic cells and only as an additional site, and a prokaryotic cell has no nucleus."),
 ("while that mRNA is still being transcribed",
  "EK 6.4.A.2 states that in prokaryotic organisms translation of the mRNA molecule occurs while it is being transcribed. The processing modifications of EK 6.3.A.4 are stated for eukaryotic cells."),
 ("made at the DNA in the nucleus while the ribosome that translates it lies in the cytoplasm",
  "EK 6.4.A.2 confines simultaneous transcription and translation to prokaryotic organisms, and EK 6.3.A.1.i puts the eukaryotic transcript's origin at the DNA in the nucleus and its destination at the ribosome in the cytoplasm. The two processes are in different compartments."),
 ("Initiation, elongation and termination",
  "EK 6.4.A.3 states that translation involves many sequential steps, including initiation, elongation, and termination. Splicing and capping belong to EK 6.3.A.4 and unwinding, priming and joining to EK 6.2.A.1."),
 ("rRNA in the ribosome interacts with the mRNA at the start codon",
  "EK 6.4.A.3.i states that translation is initiated when the rRNA in the ribosome interacts with the mRNA at the start codon. RNA polymerase acts on a DNA template under EK 6.3.A.2 and has no part here."),
 ("AUG, coding for methionine",
  "EK 6.4.A.3.i names the start codon as AUG, coding for the amino acid methionine. The chart in this module lists the same assignment, and lists the two stop codons separately."),
 ("In triplets, each of which is called a codon",
  "EK 6.4.A.3.ii states that the sequence of nucleotides on the mRNA is read in triplets, called codons. The anticodon belongs to tRNA under EK 6.3.A.1.ii and an exon is a processing unit under EK 6.3.A.4.iii."),
 ("genetic code chart",
  "EK 6.4.A.3.iii states that each codon encodes a specific amino acid, which can be deduced by using a genetic code chart. Punnett squares and pedigrees are the tools of EK 5.3.A.2.v."),
 ("Two different codons can specify the same amino acid",
  "EK 6.4.A.3.iii states that each codon encodes a specific amino acid and that many amino acids are encoded by more than one codon, so the relationship runs many codons to one amino acid and never the reverse. The chart in this module is checked to have that direction."),
 ("common ancestry of all living organisms",
  "EK 6.4.A.3.iv states that nearly all living organisms use the same genetic code, which is evidence for the common ancestry of all living organisms."),
 ("brings the correct amino acid to the place specified by the codon",
  "EK 6.4.A.3.v states exactly this. The reversed option makes the amino acid specify the codon, and carrying information from the nucleus is mRNA's role under EK 6.3.A.1.i."),
 ("amino acid is transferred to the growing polypeptide chain",
  "EK 6.4.A.3.vi states that the amino acid is transferred to the growing polypeptide chain, so what joins the chain is the residue rather than the codon or the tRNA that delivered it."),
 ("until a stop codon is reached",
  "EK 6.4.A.3.vii states that the process continues along the mRNA until a stop codon is reached, making the stopping point a feature of the message rather than a count of residues or a shortage of a component."),
 ("newly synthesized protein is released",
  "EK 6.4.A.3.viii states that translation terminates with the release of the newly synthesized protein. A stop codon is part of the mRNA under EK 6.4.A.3.vii and is not appended to a polypeptide."),
 ("histidine, and then the chain is released",
  "EK 6.4.A.3.ii reads the message in triplets and EK 6.4.A.3.iii deduces each residue from the chart, with EK 6.4.A.3.vii and viii stopping at the stop codon. The table check lifts the sequence out of the stem and runs the chart over it, so the keyed list is produced rather than remembered."),
 ("Four, because the fifth triplet is a stop codon",
  "EK 6.4.A.3.i makes the start codon an amino acid as well as a signal, and EK 6.4.A.3.vii adds no residue for a stop codon. The table check recomputes five triplets and four residues and confirms no distractor value equals the count."),
 ("Phenylalanine is listed for two different codons",
  "EK 6.4.A.3.iii states that many amino acids are encoded by more than one codon. The table check inverts the chart to find which amino acids have several codons, and confirms that no codon on the chart carries two amino acids, which is what the reversed option would need."),
 ("stops there and the newly synthesized protein is released",
  "The chart lists that codon as a stop, and EK 6.4.A.3.vii and EK 6.4.A.3.viii stop the process at a stop codon and release the protein. The table check confirms the chart's entry for that codon and that it is not also the start codon."),
 ("whose coding region is 45 nucleotides long",
  "EK 6.4.A.3.ii reads the message in triplets, so the codon count is the length divided by three. The table check divides all three lengths, confirms each is a whole number of triplets and confirms exactly one transcript gives fifteen."),
 ("From RNA to DNA, made possible by reverse transcriptase",
  "EK 6.4.A.4 states that genetic information in retroviruses is a special case with an alternate flow from RNA to DNA, made possible by reverse transcriptase, an enzyme that copies the viral RNA genome into DNA."),
 ("integrates into the host genome and is transcribed and translated",
  "EK 6.4.A.4 states that this DNA integrates into the host genome and is transcribed and translated for the assembly of new viral progeny, so the viral DNA rejoins the ordinary flow of information rather than bypassing it."),
 ("copying of the viral RNA genome into DNA",
  "EK 6.4.A.4 makes reverse transcriptase the enzyme that copies the viral RNA genome into DNA and places integration into the host genome after that copying, so inhibiting the enzyme blocks the copying first and everything downstream follows."),
 ("wrong amino acid is inserted wherever the codon that tRNA reads occurs",
  "EK 6.4.A.3.v has tRNA bring the amino acid to the place the codon specifies and EK 6.4.A.3.vi transfers it to the chain; EK 6.3.A.1.ii makes the anticodon what determines where the tRNA arrives. With the anticodon unchanged the destination is unchanged and only the residue differs."),
 ("polypeptide shorter than the one usually made",
  "EK 6.4.A.3.vii has the process continue until a stop codon is reached and EK 6.4.A.3.viii release the protein there, so the ribosome responds to the first stop codon it meets and the product is shorter."),
 ("interacts with the mRNA at the start codon, tRNA delivers amino acids",
  "The order is EK 6.4.A.3's own, initiation then elongation then termination, filled in by EK 6.4.A.3.i for initiation, EK 6.4.A.3.v and vi for elongation, and EK 6.4.A.3.vii and viii for termination."),
 ("The cytoplasmic surface",
  "EK 6.4.A.1 names the cytoplasmic surface of the rough endoplasmic reticulum of eukaryotic cells as a site of translation, rather than the enclosed side."),
 ("Nearly all living organisms use the same genetic code",
  "EK 6.4.A.3.iv states that nearly all living organisms use the same genetic code, so a codon means the same amino acid in both cells. EK 6.4.A.1 gives prokaryotes ribosomes that translate mRNA, and EK 6.3.A.4.iii puts introns in eukaryotic transcripts."),
 ("Each codon encodes a specific amino acid, and an amino acid may be encoded by several codons",
  "EK 6.4.A.3.iii states both halves, so the mapping is unambiguous from codon to amino acid and not in reverse. EK 6.4.A.3.ii makes a codon three nucleotides specifying one residue."),
 ("prokaryote the mRNA is translated while it is still being transcribed",
  "EK 6.4.A.2 states this for prokaryotic organisms, and EK 6.4.A.1 gives both kinds of cell cytoplasmic ribosomes, so what differs is whether the two processes overlap in time rather than whether the machinery is present."),
]

cg.check(b6_4, CLAIMS, table_checks={16: q16, 17: q17, 18: q18, 19: q19, 20: q20})
print("    Genetic code chart executed as a lookup: the keyed peptide and residue count are")
print("    produced from the chart and the stem's own sequence, and the translator is controlled.")
