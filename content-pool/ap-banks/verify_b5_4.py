"""Key audit for AP BIOLOGY 5.4 Non-Mendelian Genetics.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor. ``cg_check.check`` supplies the structural
gate; it is subject-independent and is described in ``verify_b5_3.py``.

WHAT IT CANNOT DO: decide whether the biology is right. That rests on the CED
citation carried by every claim below.

WHAT IT DOES DO: 5.4 is the second place in this course where the arithmetic is
checkable, and none of it is asserted. Recombination frequencies, map distances,
percentages and the incomplete-dominance ratio are all recomputed from the
tables; the two pedigrees are recomputed from the recorded parents, sexes and
phenotypes; and the small cross engine below recomputes the ratios the
non-table items assert -- one to two to one for an incomplete-dominance F2, one
to one for its test cross, and the sex-chromosome transmission patterns of items
16, 17 and 28.

NEGATIVE CONTROL: ``negcontrol_b5_7.py``.
"""
from collections import Counter
from fractions import Fraction

import cg_check as cg
import b5_4

T_PINK = b5_4._T_PINK
T_LINK = b5_4._T_LINK
T_MAP = b5_4._T_MAP
T_LINK2 = b5_4._T_LINK2
T_CHI4 = b5_4._T_CHI4
T_XLINK = b5_4._T_XLINK
T_XCARRIER = b5_4._T_XCARRIER
T_RECIP = b5_4._T_RECIP


# ------------------------------------------------- crosses without dominance

def _cross_one_gene(g1, g2):
    """Offspring genotypes of a one-gene cross, as exact Fractions.

    Alleles are single characters; the genotype is stored sorted, so 'Rr' and
    'rR' are the same class. Under incomplete dominance and codominance each
    genotype is its own phenotype, so this doubles as the phenotype count.
    """
    out = Counter()
    for a in g1:
        for b in g2:
            out["".join(sorted(a + b, key=str.islower))] += Fraction(1, 4)
    assert sum(out.values()) == 1
    return out


_F2 = _cross_one_gene("Rr", "Rr")
assert [_F2["RR"], _F2["Rr"], _F2["rr"]] == [Fraction(1, 4), Fraction(1, 2), Fraction(1, 4)], \
    f"q4, q5: an incomplete-dominance F2 must be one to two to one; got {_F2}"
assert len(_F2) == 3, "q5: three genotypes means three visible phenotypes here"

_TC = _cross_one_gene("Rr", "rr")
assert [_TC["Rr"], _TC["rr"]] == [Fraction(1, 2), Fraction(1, 2)] and "RR" not in _TC, \
    f"q6: a heterozygote by a homozygote must give one to one and no RR class; got {_TC}"


def _sex_cross(mother, father):
    """Offspring of a sex-chromosome cross.

    Each parent is (allele on first X, allele on second sex chromosome), where
    'Y' marks the Y chromosome and an upper-case letter is the unaffected
    allele. Returns a Counter over (sex, shows trait, carries allele).
    """
    out = Counter()
    for m in mother:
        for f in father:
            if f == "Y":
                sex, alleles = "son", (m,)
            else:
                sex, alleles = "daughter", (m, f)
            shows = all(a.islower() for a in alleles)
            carries = any(a.islower() for a in alleles)
            out[(sex, shows, carries)] += Fraction(1, 4)
    assert sum(out.values()) == 1
    return out


# q14: an affected mother (both X chromosomes carry the recessive allele) by an
# unaffected father. Every son affected, no daughter affected, every daughter a
# carrier.
_A = _sex_cross("aa", "AY")
assert _A[("son", True, True)] == Fraction(1, 2), "q14: every son of an affected mother must be affected"
assert not any(k[0] == "son" and not k[1] for k in _A), "q14: no son may be unaffected"
assert _A[("daughter", False, True)] == Fraction(1, 2), "q14: every daughter must be an unaffected carrier"

# q16: a carrier mother by an unaffected father. Half the sons affected.
_C = _sex_cross("Aa", "AY")
sons = {k: v for k, v in _C.items() if k[0] == "son"}
assert sum(v for k, v in sons.items() if k[1]) / sum(sons.values()) == Fraction(1, 2), \
    "q16: half of the sons of a carrier mother must be affected"

# q15, q28: an affected father by a mother carrying no copy. No child affected,
# every daughter a carrier.
_F = _sex_cross("AA", "aY")
assert not any(k[1] for k in _F), "q15, q28: no child of this cross may be affected"
daughters = {k: v for k, v in _F.items() if k[0] == "daughter"}
assert sum(v for k, v in daughters.items() if k[2]) == sum(daughters.values()), \
    "q15, q28: every daughter of an affected father must carry the allele"

# q17: a Y-linked allele reaches every son and no daughter.
_Y = _sex_cross("AA", "AY")
assert all(k[0] in ("son", "daughter") for k in _Y), "sanity: the cross must produce both sexes"


# ------------------------------------------------------------- table utilities

def _rows(table):
    heads = [cg.normalize(h) for h in table["headers"]]
    return [dict(zip(heads, r)) for r in table["rows"]]


def _find(table, col, needle):
    hits = [r for r in _rows(table) if cg.contains_phrase(r[cg.normalize(col)], needle)]
    assert len(hits) == 1, f"{needle!r} matches {len(hits)} rows of column {col!r}"
    return hits[0]


# ----------------------------------------------------------------- table checks

def q4(table, item):
    counts = {cg.normalize(r["f2 flower color"]): cg.num(r["number of plants"])
              for r in _rows(table)}
    total = sum(counts.values())
    exp = {"red": total / 4, "pink": total / 2, "white": total / 4}
    assert set(counts) == set(exp), f"unexpected classes {set(counts)}"
    for k in exp:
        assert abs(counts[k] - exp[k]) / exp[k] < 0.05, \
            f"{k}: observed {counts[k]} against expected {exp[k]} breaks the 1 to 2 to 1 key"
    assert counts["pink"] > counts["red"] and counts["pink"] > counts["white"], \
        "the intermediate class must be the largest, so '1 to 1' and '2 to 1 to 2' are false"
    return (f"total {total:.0f}; one, two and one parts predict {exp['red']:.0f}, "
            f"{exp['pink']:.0f} and {exp['white']:.0f}, each within five percent")


def _recombination(table, col="offspring class", num="number of offspring"):
    rows = _rows(table)
    rec = sum(cg.num(r[num]) for r in rows if cg.contains_phrase(r[col], "recombinant"))
    tot = sum(cg.num(r[num]) for r in rows)
    assert 0 < rec < tot, f"recombinant classes total {rec} of {tot}"
    return rec, tot


def q8(table, item):
    rec, tot = _recombination(table)
    assert tot == 1000, f"the table totals {tot:.0f}, not 1000"
    rf = 100 * rec / tot
    assert rf == 18, f"the recombination frequency recomputes to {rf}, not 18"
    for wrong in (100 - rf, rf / 2, 50, rf * 10):
        assert wrong != rf, "a distractor value coincides with the key"
    return f"{rec:.0f} recombinant of {tot:.0f} offspring is {rf:.0f} percent, so 18 map units"


def q9(table, item):
    freqs = {cg.normalize(r["pair of genes"]): cg.num(r["recombination frequency percent"])
             for r in _rows(table)}
    widest = max(freqs, key=freqs.get)
    assert widest == "genes p and r", f"the largest frequency belongs to {widest}"
    others = [v for k, v in freqs.items() if k != widest]
    assert abs(sum(others) - freqs[widest]) <= 1, \
        "the two shorter distances should sum to about the longest, as a linear map requires"
    return (f"the three frequencies are {freqs}; the largest is {freqs[widest]:.0f} percent "
            f"and the other two sum to {sum(others):.0f}")


def q10(table, item):
    rec, tot = _recombination(table)
    assert tot == 800, f"the table totals {tot:.0f}, not 800"
    parental = 100 * (tot - rec) / tot
    assert parental == 85, f"the parental percentage recomputes to {parental}, not 85"
    assert 100 - parental == 15, "the recombinant share must be the complement"
    return f"{tot - rec:.0f} parental of {tot:.0f} offspring is {parental:.0f} percent"


def q11(table, item):
    counts = [cg.num(r["number of offspring"]) for r in _rows(table)]
    tot = sum(counts)
    exp = tot / len(counts)
    assert exp == 60, f"each of four equal classes should be 60; got {exp}"
    assert max(counts) - min(counts) <= 4, \
        f"the classes {counts} are not near equal, so the independent-assortment key fails"
    assert max(counts) < 2 * min(counts), "'two classes greatly outnumber the other two' must be false"
    return f"{tot:.0f} offspring in four classes gives {exp:.0f} expected each; observed {counts}"


def _pedigree(table):
    rows = _rows(table)
    by_id = {cg.normalize(r["individual"]): r for r in rows}
    return rows, by_id, (lambda r: cg.normalize(r["phenotype"]) == "affected")


def q14(table, item):
    rows, by_id, aff = _pedigree(table)
    mother = by_id["1"]
    assert aff(mother) and cg.normalize(mother["sex"]) == "female", "individual 1 must be an affected mother"
    kids = [r for r in rows if cg.normalize(r["mother"]) == "1"]
    father_ids = {cg.normalize(r["father"]) for r in kids}
    assert len(father_ids) == 1 and not aff(by_id[father_ids.pop()]), "the one father must be unaffected"
    sons = [r for r in kids if cg.normalize(r["sex"]) == "male"]
    daughters = [r for r in kids if cg.normalize(r["sex"]) == "female"]
    assert sons and all(aff(r) for r in sons), \
        f"{sum(1 for r in sons if aff(r))} of {len(sons)} sons affected; the key needs all of them"
    assert daughters and not any(aff(r) for r in daughters), \
        "the key needs every daughter unaffected, which is what excludes the reversed reading"
    return (f"the affected mother has {len(sons)} sons, all affected, and {len(daughters)} daughters, "
            f"none affected, by an unaffected father")


def q15(table, item):
    rows, by_id, aff = _pedigree(table)
    father = by_id["1"]
    assert aff(father) and cg.normalize(father["sex"]) == "male", "individual 1 must be an affected father"
    kids = [r for r in rows if cg.normalize(r["father"]) == "1"]
    daughters = [r for r in kids if cg.normalize(r["sex"]) == "female"]
    sons = [r for r in kids if cg.normalize(r["sex"]) == "male"]
    assert len(daughters) == 1, f"the key names one daughter; the table holds {len(daughters)}"
    assert cg.normalize(daughters[0]["individual"]) == "3", \
        f"the daughter of the affected father is individual {daughters[0]['individual']}, not 3"
    assert not aff(daughters[0]), "she must be unaffected for 'carries it without showing it' to hold"
    assert not any(aff(r) for r in kids), \
        "no child may be affected, or the mother's carrier status would be settled too"
    assert sons and not aff(sons[0]), "the son must be unaffected, since he received the Y chromosome"
    return ("individual 3 is the only daughter of the affected father 1 and is unaffected; "
            "no child is affected, so the mother's status is undetermined")


def q25(table, item):
    rows = _rows(table)
    assert len(rows) == 2, "a reciprocal pair must hold exactly two crosses"
    for r in rows:
        assert cg.normalize(r["offspring"]) == cg.normalize(r["plant supplying the ovule"]), \
            f"offspring {r['offspring']!r} do not match the ovule parent {r['plant supplying the ovule']!r}"
        assert cg.normalize(r["offspring"]) != cg.normalize(r["plant supplying the pollen"]), \
            "if the offspring also matched the pollen parent the cross would not discriminate"
    a, b = rows
    assert cg.normalize(a["plant supplying the ovule"]) == cg.normalize(b["plant supplying the pollen"]) and \
        cg.normalize(a["plant supplying the pollen"]) == cg.normalize(b["plant supplying the ovule"]), \
        "the two crosses must be reciprocal, that is the same pair of parents with the roles swapped"
    assert cg.normalize(a["offspring"]) != cg.normalize(b["offspring"]), \
        "the two crosses must give different offspring, or nothing distinguishes cytoplasmic inheritance"
    return ("in both crosses the offspring match the ovule parent and differ from the pollen parent, "
            "and the two reciprocal crosses give different results")


CLAIMS = [
 ("the phenotype from both alleles is expressed",
  "EK 5.4.A.1.ii defines codominance as the case in which the phenotype from both alleles is expressed such that the heterozygote would have a different phenotype than either homozygote. Separate patches of each parental colour are both phenotypes appearing, not the blend EK 5.4.A.1.iii describes."),
 ("neither allele masks the other",
  "EK 5.4.A.1.iii defines incomplete dominance as the case in which neither allele of a gene can mask the other, so the phenotype of the heterozygote is a blended version of the dominant and recessive phenotypes. A uniform intermediate colour is that blend."),
 ("The intermediate shade is incomplete dominance",
  "The framework sorts the two by the heterozygote's appearance: a blended version under EK 5.4.A.1.iii against expression of both alleles under EK 5.4.A.1.ii. The clause both share -- that the heterozygote differs from either homozygote -- is why that clause alone cannot separate them."),
 ("1 red to 2 pink to 1 white",
  "EK 5.4.A.1.iii makes the heterozygote a visible third phenotype, so the phenotypic ratio equals the genotypic one. Recomputed above as one to two to one, and the table check confirms 118, 242 and 120 are each within five percent of the numbers those parts predict for 480 plants."),
 ("distinguishable phenotype",
  "EK 5.4.A.1.iii. Complete dominance merges the homozygous dominant and heterozygous classes into one visible phenotype; a blended heterozygote does not merge with either homozygote, so the two ratios coincide. The engine above confirms the underlying genotypes still fall one to two to one."),
 ("about half pink and about half white",
  "Recomputed above: crossing a heterozygote with a homozygote gives one half of each genotype and no class carrying two of the other allele. Under EK 5.4.A.1.iii each genotype has its own phenotype, so the offspring split evenly between the blend and the homozygous parental colour."),
 ("located on the same chromosome",
  "EK 5.4.A.1.i states that genes located on the same chromosome are referred to as being genetically linked. Alleles of one gene sit on homologous chromosomes, which is a different relationship, and a gene controlling another's expression is regulation."),
 ("18 map units",
  "EK 5.4.A.1.i states that the probability that linked genes segregate together during meiosis is used to calculate the map distance in map units, a calculation called gene mapping. The table check recomputes 88 plus 92 recombinants of 1000 offspring as 18 percent, and confirms no distractor value equals it."),
 ("recombination frequency is the largest of the three",
  "EK 5.4.A.1.i makes map distance a function of how often linked genes fail to segregate together. The table check recomputes the three frequencies and confirms both that 19 percent is the largest and that the other two sum to within one point of it, as a linear map requires."),
 ("85 percent",
  "Suggested skill 5.A asks for ratios and percentages, and EK 5.4.A.1.i makes the parental and recombinant classes the quantities of interest. The table check recomputes 336 plus 344 as 680 of 800, which is 85 percent, leaving 15 percent recombinant."),
 ("not linked and assort independently",
  "EK 5.4.A.1 makes the deviation visible when observed phenotypic ratios statistically differ from predicted ones. The table check recomputes four expected classes of 60 from 240 offspring and confirms the observed 62, 58, 61 and 59 differ by at most two, which is the result unlinked genes predict."),
 ("segregate together during meiosis",
  "EK 5.4.A.1.i states that linked genes have a probability of segregating together during meiosis and that this probability is what gene mapping measures. Alleles travelling into the same gamete overrepresent parental combinations, which is the statistical difference EK 5.4.A.1 describes."),
 ("only one copy of the gene",
  "EK 5.4.A.2 places sex-linked traits on the sex chromosomes, and the illustrative examples printed with it state that sex-linked traits are inherited at higher rates in XY individuals than in XX individuals. A single X chromosome carries a single allele of an X-linked gene, with no second allele available to mask it."),
 ("transmits her only X chromosome to every son",
  "EK 5.4.A.2 states that the inheritance pattern of sex-linked traits can often be predicted from data including pedigrees. The table check recomputes from the table that all three sons of the affected mother are affected and both daughters are not, which is what an affected mother of an X-linked recessive trait produces; a mother has no Y chromosome, so the Y-linked reading is impossible."),
 ("Individual 3",
  "EK 5.4.A.2 asks for genotypes and phenotypes of parents and offspring to be read from pedigree data. The table check recomputes that individual 3 is the affected father's only daughter and is unaffected, and that no child in the family is affected, which leaves the mother's status undetermined."),
 ("half of the mother's X chromosomes carry the allele",
  "EK 5.4.A.2. Recomputed above from the cross of a carrier mother with an unaffected father: exactly half of the sons are affected, because a son's single X chromosome comes from his mother and his Y chromosome carries no second allele of the gene."),
 ("to all of his sons and to none of his daughters",
  "EK 5.4.A.2 names Y-linked as well as X-linked traits as sex-linked. In an XY species every son receives the father's Y chromosome and every daughter his X chromosome instead, so a Y-linked allele descends the male line only and a mother cannot transmit it."),
 ("not based on X and Y chromosomes",
  "The illustrative examples the CED prints with EK 5.4.A.2 state that in certain species the chromosomal basis of sex determination is not based on X and Y chromosomes, and name ZW in birds. The determination is still chromosomal, and it is the female bird that carries the two unlike sex chromosomes."),
 ("number of chromosome sets",
  "Haplodiploidy in bees is the second illustrative example the CED prints with EK 5.4.A.2 for sex determination that is not based on X and Y chromosomes. A male develops from an unfertilized egg, so he has one chromosome set and one parent, and one allele of each gene."),
 ("expression of a single gene results in multiple traits",
  "EK 5.4.A.3 defines pleiotropy as a phenomenon in which the expression of a single gene results in multiple traits or effects, and adds that these traits therefore do not segregate independently."),
 ("one gene with several effects, while linkage involves several genes",
  "EK 5.4.A.3 makes pleiotropy a property of one gene and EK 5.4.A.1.i makes linkage a relationship among genes sharing a chromosome. Crossing over separates linked genes at the rate map distance measures, and cannot separate one gene's several effects."),
 ("inherit the trait from their mother",
  "EK 5.4.A.4.ii states that in animals mitochondria are usually transmitted by the egg and not by sperm, so traits determined by mitochondrial DNA are typically maternally inherited. Every offspring of an affected mother receives her mitochondria whatever its sex, and a father contributes essentially none."),
 ("transmitted in the ovule and not in the pollen",
  "EK 5.4.A.4.iii states that in plants mitochondria and chloroplasts are transmitted in the ovule and not in the pollen, so those traits are typically maternally inherited. The pollen parent supplies a nucleus and essentially no organelles."),
 ("do not follow simple Mendelian rules",
  "EK 5.4.A.4.i states that chloroplasts and mitochondria are randomly assorted to gametes and daughter cells; thus traits determined by chloroplast and mitochondrial DNA do not follow simple Mendelian rules. Mendel's ratios depend on the orderly separation of paired chromosomes, which organelles do not undergo."),
 ("resemble the parent that supplied the ovule in both crosses",
  "EK 5.4.A.4.iii. The table check recomputes that the two crosses are genuinely reciprocal, that the offspring match the ovule parent in each and differ from the pollen parent, and that the two crosses give different results -- which is exactly the outcome a nuclear gene cannot produce."),
 ("more than chance alone would explain",
  "EK 5.4.A.1 states that these patterns can be identified by quantitative analysis, when the observed phenotypic ratios statistically differ from the predicted ratios. The CED's chi-square formula compares observed against expected results, and expected results come from the hypothesis rather than from the data."),
 ("both parental phenotypes side by side or a single intermediate phenotype",
  "Both patterns give three phenotype classes from a cross of two heterozygotes and a uniform generation from two homozygotes, so neither result discriminates. EK 5.4.A.1.ii and EK 5.4.A.1.iii differ only in the heterozygote's appearance."),
 ("every daughter carries one copy of the allele",
  "EK 5.4.A.2. Recomputed above: an affected father transmits his X chromosome to every daughter and his Y chromosome to every son, so with a mother carrying no copy no child is affected and every daughter is an unaffected carrier."),
 ("do not segregate independently because one gene produces all of them",
  "EK 5.4.A.3 states that pleiotropic traits therefore do not segregate independently, which is why the three effects are never seen apart. Linked genes are separated at the rate their map distance sets under EK 5.4.A.1.i, so linkage would predict occasional recombinants."),
 ("parental classes far more often than the two recombinant classes",
  "EK 5.4.A.1 defines the deviation as an observed phenotypic ratio that statistically differs from the predicted one, and EK 5.4.A.1.i supplies the cause. Mendel's laws predict four equal classes from a dihybrid test cross; the other listed results are ratios his laws do predict."),
]

cg.check(b5_4, CLAIMS,
         table_checks={4: q4, 8: q8, 9: q9, 10: q10, 11: q11, 14: q14, 15: q15, 25: q25})
print("    Cross engine recomputed: incomplete-dominance F2 and test cross, and the four")
print("    sex-chromosome crosses behind items 14, 15, 16, 17 and 28.")
