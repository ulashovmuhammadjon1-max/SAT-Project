"""Key audit for AP BIOLOGY 2.10 Origins of Cell Compartmentalization.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the keyed choice and in no distractor, so a key
survives the choice shuffle ``export_units.py`` applies on the way out. The
claim names the essential knowledge statement the key rests on.

WHAT THE KEYS REST ON
---------------------
The topic has three statements and they carry most of the module:

  2.10.A.1  mitochondria and chloroplasts evolved from once free-living
            prokaryotic cells via endosymbiosis
  2.10.A.2  prokaryotes typically lack internal membrane-bound organelles but
            have internal regions with specialized structures and functions
  2.10.A.3  eukaryotic cells maintain internal membranes that partition the
            cell into specialized regions

Four supporting statements from elsewhere in the same CED are cited where they
are used, never assumed: 2.1.A.1 (ribosomes in all forms of life reflect common
ancestry), 2.1.A.5 and 2.1.A.8 (the double membranes of mitochondrion and
chloroplast), 6.1.A.1.i (prokaryotes typically have circular chromosomes) and
3.4.A.1.ii/iv (photosynthesis first evolved in prokaryotes and prokaryotic
pathways were the foundation of the eukaryotic version).

THE EVIDENCE ITEMS ARE CONDITIONAL ON PURPOSE. The framework asserts the
endosymbiotic origin and does not print the evidence for it. Items 7, 8, 15
and 17 therefore ask what a stated observation would support, so the key is a
piece of reasoning from a cited statement rather than a factual assertion the
CED does not make.

Items 10, 11 and 12 carry tables. Every number is HYPOTHETICAL and the stem
says so; each keyed conclusion is recomputed below from the table alone, and
each distractor is shown false against the same numbers.

FIVE choices per item (A-E), per SCIENCE_BRIEF.md.
"""
import cg_check as cg
import b2_10

CELLS = b2_10._T_CELLS
STRUCT = b2_10._T_STRUCT
SURVEY = b2_10._T_SURVEY

H_ORG = "Types of membrane-bound organelle observed"
H_AREA = "Total internal membrane area (square micrometers)"
H_RIB = "Ribosomes counted (thousands)"

H_MEM = "Membranes surrounding the structure"
H_DIA = "Diameter (micrometers)"
H_DNA = "DNA present within the structure (kilobases)"

H_EXAM = "Species examined"
H_WITHORG = "Species with membrane-bound organelles"
H_WITHREG = "Species with internal regions of specialized function"


def q10(table, item):
    labs = cg.labels(table)
    org = dict(zip(labs, cg.col(table, H_ORG)))
    area = dict(zip(labs, cg.col(table, H_AREA)))
    rib = dict(zip(labs, cg.col(table, H_RIB)))
    zero_org = [k for k in labs if org[k] == 0]
    assert len(zero_org) == 1, f"the key needs exactly one cell with no organelles; got {zero_org}"
    prok = zero_org[0]
    assert area[prok] == 0, "the same cell must also show no internal membrane area"
    assert all(area[k] > 0 for k in labs if k != prok), \
        "every other cell must show internal membrane area"
    # every distractor false on the same numbers
    assert max(area, key=area.get) != prok, "'largest internal membrane area' must not be the prokaryote"
    assert max(rib, key=rib.get) != prok, "'most ribosomes' must not be the prokaryote"
    assert max(org, key=org.get) != prok, "'most organelle types' must not be the prokaryote"
    assert all(rib[k] > 0 for k in labs), \
        "every cell must have ribosomes, so their presence cannot identify anything"
    return (f"{prok} alone shows 0 organelle types and 0 internal membrane area, "
            f"while all three cells carry ribosomes, so ribosome count identifies nothing")


def q11(table, item):
    labs = cg.labels(table)
    mem = dict(zip(labs, cg.col(table, H_MEM)))
    dia = dict(zip(labs, cg.col(table, H_DIA)))
    dna = dict(zip(labs, cg.col(table, H_DNA)))
    two = {k for k in labs if mem[k] == 2}
    withdna = {k for k in labs if dna[k] > 0}
    assert two and two == withdna, \
        f"the double-membrane set {two} must be exactly the DNA-bearing set {withdna}"
    one = {k for k in labs if mem[k] == 1}
    assert one and all(dna[k] == 0 for k in one), \
        "'the one-membrane structures are the ones with DNA' must be false"
    biggest = max(labs, key=lambda k: dia[k])
    assert dna[biggest] != min(dna.values()), \
        "'the largest structure contains the least DNA' must be false"
    assert len(set(mem.values())) > 1, "'every structure has the same number of membranes' must be false"
    ratios = {dna[k] / mem[k] for k in labs}
    assert len(ratios) > 1, "'DNA is proportional to membrane number' must be false"
    return (f"the structures with two membranes are {sorted(two)} and those are exactly the "
            f"structures with DNA present; the largest by diameter is {biggest}, which does not hold the least DNA")


def q12(table, item):
    labs = cg.labels(table)
    exam = dict(zip(labs, cg.col(table, H_EXAM)))
    org = dict(zip(labs, cg.col(table, H_WITHORG)))
    reg = dict(zip(labs, cg.col(table, H_WITHREG)))
    assert all(reg[k] == exam[k] and exam[k] > 0 for k in labs), \
        "every species surveyed in both groups must show specialized internal regions"
    assert org["Prokaryotes"] == 0, "no prokaryote in the survey may show membrane-bound organelles"
    assert org["Eukaryotes"] == exam["Eukaryotes"], \
        "every eukaryote in the survey must show membrane-bound organelles"
    assert org["Prokaryotes"] < org["Eukaryotes"], \
        "'more prokaryotic than eukaryotic species have organelles' must be false"
    pct_reg = 100 * sum(reg.values()) / sum(exam.values())
    return (f"{pct_reg:.0f} percent of the {sum(exam.values()):.0f} species surveyed show specialized "
            f"internal regions, while organelles appear in {org['Eukaryotes']:.0f} eukaryotes and 0 prokaryotes")


CLAIMS = [
 ("lived independently and came to reside inside another cell",
  "EK 2.10.A.1 states that membrane-bound organelles such as mitochondria and chloroplasts evolved from once free-living prokaryotic cells via endosymbiosis. Infolding, nuclear assembly and viral origin are not the account the framework gives."),
 ("Mitochondria and chloroplasts",
  "EK 2.10.A.1 names these two specifically as the membrane-bound organelles with an endosymbiotic origin. The framework does not extend that claim to lysosomes, the Golgi complex, the nucleus or vesicles."),
 ("typically lack membrane-bound organelles while still having internal regions",
  "EK 2.10.A.2 states that prokaryotes typically lack internal membrane-bound organelles but have internal regions with specialized structures and functions. Both halves of the observation described match that one sentence."),
 ("particular structures and functions are concentrated",
  "EK 2.10.A.2 credits prokaryotes with internal regions of specialized structure and function and EK 2.10.A.3 credits eukaryotes with membrane-partitioned specialized regions. Regional specialization is what the two share; membrane-bound organelles are not."),
 ("Eukaryotic cells maintain internal membranes that partition the cell",
  "EK 2.10.A.3 gives eukaryotes internal membranes that partition the cell into specialized regions, and EK 2.10.A.2 denies prokaryotes internal membrane-bound organelles. EK 2.1.A.1 places ribosomes in all forms of life, which is why the ribosome option fails."),
 ("named as instances, without a claim that every membrane-bound organelle arose the same way",
  "EK 2.10.A.1 introduces mitochondria and chloroplasts with SUCH AS, which offers them as examples rather than an exhaustive list and asserts nothing about organelles it does not name. EK 2.1.A.2's endomembrane system names several other membrane-bound organelles for which the framework makes no endosymbiotic claim."),
 ("prokaryotic organisms typically have circular chromosomes",
  "EK 6.1.A.1.i states that prokaryotic organisms typically have circular chromosomes while eukaryotic organisms typically have multiple linear chromosomes. A circular chromosome inside an organelle therefore points to the prokaryotic ancestry asserted in EK 2.10.A.1."),
 ("expected if one cell had been taken inside another",
  "EK 2.1.A.5 and EK 2.1.A.8 record the double membranes of mitochondrion and chloroplast, and EK 2.10.A.1 gives their origin as uptake of a once free-living cell. An engulfed cell brings its own boundary and gains a second from its host."),
 ("photosynthetic prokaryote becoming an organelle",
  "EK 3.4.A.1.ii places the origin of photosynthesis in prokaryotes and EK 3.4.A.1.iv makes prokaryotic pathways the foundation of the eukaryotic version, which is what EK 2.10.A.1's endosymbiotic origin of the chloroplast would produce."),
 ("no membrane-bound organelle types and no internal membrane area",
  "Recomputed in q10 above. EK 2.10.A.2 makes the absence of membrane-bound organelles the prokaryotic signature, and EK 2.1.A.1 puts ribosomes in all forms of life, so the ribosome column identifies nothing."),
 ("bounded by two membranes are also the ones that contain DNA",
  "Recomputed in q11 above. EK 2.10.A.1 traces mitochondria and chloroplasts to once free-living cells, and a former cell would retain both its own boundary and its own genetic material; in the table those two features coincide exactly."),
 ("only the eukaryotes have membrane-bound organelles",
  "Recomputed in q12 above. EK 2.10.A.2 and EK 2.10.A.3 predict this split precisely: specialized internal regions throughout, membrane-bound organelles in the eukaryotes alone."),
 ("holds broadly while particular prokaryotes may depart",
  "EK 2.10.A.2 is a qualified generalization, in the same form as EK 6.1.A.1.i's statement that prokaryotes typically have circular chromosomes. A qualifier asserts the pattern and leaves room for exceptions, so an absolute reading misstates it."),
 ("descendant as an organelle of the host cell",
  "EK 2.10.A.1 says the organelles evolved FROM once free-living prokaryotic cells, locating independent life in the ancestor. The framework describes the present-day mitochondrion as a membrane-bound organelle of a eukaryotic cell throughout."),
 ("continuous with the endoplasmic reticulum",
  "The endosymbiotic account in EK 2.10.A.1 predicts a structure descended from a cell, carrying its own boundary and its own genetic material. Membrane continuity with the endomembrane system and the absence of genetic material fit an origin by budding instead."),
 ("bounded by their own membranes, so their contents are physically enclosed",
  "EK 2.10.A.3 makes internal membranes the partition in eukaryotes while EK 2.10.A.2 gives prokaryotes regions without membrane-bound organelles. Enclosure by a membrane is a qualitative difference, not a difference of degree."),
 ("genomes of living prokaryotes",
  "Descent is an evolutionary claim, so the informative evidence is a comparison with candidate relatives. EK 2.10.A.1 asserts descent from once free-living prokaryotic cells; volume, copy number, pH and speed bear on none of that."),
 ("descent, not of how the structure works",
  "EK 2.10.A.1 sits under Big Idea 1, Evolution, and asserts a lineage. What a mitochondrion does with energy is treated separately under Big Idea 2, which is why an origin claim is not an energetics claim."),
 ("partitioned into more specialized regions",
  "EK 2.10.A.3 states that eukaryotic cells maintain internal membranes that partition the cell into specialized regions, so more internal membrane means more partitioning. Ancestry and genome size do not follow from how much membrane a cell has built."),
 ("without a surrounding organelle membrane",
  "EK 2.10.A.2 gives prokaryotes internal regions with specialized structures and functions while denying them internal membrane-bound organelles. The keyed description states both halves of that sentence and nothing further."),
 ("confine particular structures and functions to particular internal regions",
  "Skill 6.B asks for evidence that supports the stated claim, and the claim is about internal specialization outside eukaryotes. EK 2.10.A.2 supplies exactly that; cell size, chromosome shape and the outer boundary concern other properties."),
 ("the kind of event by which the chloroplast is said to have arisen",
  "EK 2.10.A.1 gives endosymbiosis as the route by which chloroplasts evolved from once free-living prokaryotic cells, and EK 3.4.A.1.ii places the origin of photosynthesis in prokaryotes. The scenario is that route described as an event."),
 ("requires them to have lived independently first",
  "The wording of EK 2.10.A.1 is the content of the claim: organelles evolved from ONCE FREE-LIVING prokaryotic cells via endosymbiosis. Independent life before uptake is what separates this account from an origin by membrane folding."),
 ("no longer maintain distinct regions with distinct functions",
  "EK 2.10.A.3 makes internal membranes the thing that partitions a eukaryotic cell into specialized regions, so removing them removes the partitioning. Chromosome shape and ribosome presence are governed by other statements and would not change."),
 ("because it descends from one",
  "EK 2.10.A.1 sets the direction of descent: the organelle evolved from a once free-living prokaryotic cell. Resemblance is then inherited, and reversing the direction contradicts the statement outright."),
 ("acquired certain organelles from another lineage",
  "EK 2.10.A.1 attributes mitochondria and chloroplasts specifically to descent from a separate lineage of once free-living prokaryotic cells, which is acquisition across lineages rather than construction from within one."),
 ("Particular functions are associated with particular locations",
  "EK 2.10.A.2 gives prokaryotes internal regions with specialized structures and functions and EK 2.10.A.3 gives eukaryotes membrane-partitioned specialized regions. Localization of function is common to both; membranes, the nuclear envelope and an engulfed ancestor are not."),
 ("while the mitochondrion reflects the merger",
  "EK 2.1.A.1 reads the universality of ribosomes as reflecting the common ancestry of all known life, which is one line of descent. EK 2.10.A.1 describes something different: one lineage of cells taken up into another."),
 ("regions in which particular functions are carried out",
  "Skill 3.A asks for a testable question. Only the keyed question can be answered by looking at cells, and EK 2.10.A.2 is the statement it tests; the others ask what is simpler, more impressive, better or more deserving."),
 ("internal membranes partition the rest of the cell",
  "EK 2.10.A.1 covers the endosymbiotic organelles, EK 2.10.A.3 covers partitioning by internal membranes, and EK 2.10.A.2 denies that prokaryotes are unorganized. Only the keyed pair is consistent with all three."),
]

cg.check(b2_10, CLAIMS, table_checks={10: q10, 11: q11, 12: q12})
