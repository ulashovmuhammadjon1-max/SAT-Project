"""Key audit for AP BIOLOGY 5.3 Mendelian Genetics.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on. The
structural gate is ``cg_check.check`` -- written for Comparative Government but
subject-independent: thirty questions, five distinct choices, a key that matches
its anchor, no choice contained in another, a non-empty reason, no option named
by letter, and a recomputation callable for every question carrying a table.

WHAT THIS CANNOT DO. It cannot tell whether the biology is right. There is no
sympy here, so the biology is gated by the CED citation in every claim below and
by the rule in SCIENCE_BRIEF.md that an uncertain question is cut rather than
guessed.

WHAT IT CAN DO, AND DOES. Mendelian genetics is the one part of this course
where the arithmetic is checkable, so this file does not take a single ratio on
trust. ``_cross`` below builds the gametes of each parent from the genotype
string, pairs every gamete with every gamete, and returns exact Fractions over
genotypes; ``_phen_ratio`` collapses those to phenotype classes under complete
dominance. Every ratio, probability and class count asserted by a keyed choice
in items 4, 5, 10, 11, 14, 15, 21, 22, 26, 27 and 30 is recomputed from that
engine rather than from memory, and the seven items carrying tables are
recomputed from the table alone.

NEGATIVE CONTROL. ``negcontrol_b5_7.py`` corrupts each key and each table in
turn and asserts this file then fails. A checker that cannot fail is worse than
none.
"""
from collections import Counter
from fractions import Fraction
from itertools import product

import cg_check as cg
import b5_3

T_MONO = b5_3._T_MONO
T_DIHYBRID = b5_3._T_DIHYBRID
T_PED_REC = b5_3._T_PED_REC
T_PED_DOM = b5_3._T_PED_DOM
T_TESTCROSS = b5_3._T_TESTCROSS
T_THREE = b5_3._T_THREE
T_CHISQ = b5_3._T_CHISQ


# --------------------------------------------------------------- Punnett engine

def _gametes(genotype):
    """Gamete types of a diploid genotype string, with exact probabilities.

    ``"AaBb"`` is read as two genes of two alleles each, so the gametes are
    AB, Ab, aB and ab at one quarter apiece. ``"AA"`` gives one gamete type.
    """
    assert len(genotype) % 2 == 0, f"{genotype!r} is not a whole number of genes"
    genes = [genotype[i:i + 2] for i in range(0, len(genotype), 2)]
    combos = list(product(*genes))
    p = Fraction(1, len(combos))
    out = Counter()
    for combo in combos:
        out["".join(combo)] += p
    return out


def _cross(g1, g2):
    """Offspring genotype frequencies of g1 by g2, as exact Fractions."""
    out = Counter()
    for ga, pa in _gametes(g1).items():
        for gb, pb in _gametes(g2).items():
            geno = "".join("".join(sorted(ga[i] + gb[i], key=str.islower))
                           for i in range(len(ga)))
            out[geno] += pa * pb
    assert sum(out.values()) == 1, "genotype probabilities must sum to one"
    return out


def _phen(genotype):
    """Phenotype class under complete dominance, one entry per gene."""
    genes = [genotype[i:i + 2] for i in range(0, len(genotype), 2)]
    return tuple("dominant" if g[0].isupper() else "recessive" for g in genes)


def _phen_ratio(g1, g2):
    out = Counter()
    for geno, p in _cross(g1, g2).items():
        out[_phen(geno)] += p
    return out


# Recomputations the keyed choices assert. Every one of these is an arithmetic
# claim a reader would otherwise have to take on faith.
_M = _phen_ratio("Aa", "Aa")
assert _M[("dominant",)] == Fraction(3, 4) and _M[("recessive",)] == Fraction(1, 4), \
    f"q10, q28: a monohybrid F2 must be three to one; got {_M}"

_D = _phen_ratio("AaBb", "AaBb")
assert [_D[k] for k in (("dominant", "dominant"), ("dominant", "recessive"),
                        ("recessive", "dominant"), ("recessive", "recessive"))] == \
    [Fraction(9, 16), Fraction(3, 16), Fraction(3, 16), Fraction(1, 16)], \
    f"q11: a dihybrid F2 must be nine to three to three to one; got {_D}"

_G = _cross("AaBb", "AaBb")
assert _G["aabb"] == Fraction(1, 16), f"q4: P(aabb) recomputes to {_G['aabb']}"
assert len(_G) == 9, f"q26: a dihybrid cross must give nine genotypes; got {len(_G)}"
assert len(_phen_ratio("AaBb", "AaBb")) == 4, "q26: four phenotype classes expected"
assert _D[("recessive", "dominant")] == Fraction(3, 16), \
    "q30: recessive at one gene and dominant at the other must be three sixteenths"

_MG = _cross("Aa", "Aa")
assert _MG["AA"] + _MG["Aa"] == Fraction(3, 4), \
    "q5: the two mutually exclusive genotypes carrying A must total three quarters"
assert _MG["aa"] * _MG["aa"] == Fraction(1, 16), \
    "q15: two independent children both aa must be one sixteenth"
assert _MG["Aa"] / (_MG["AA"] + _MG["Aa"]) == Fraction(2, 3), \
    "q21: given the dominant phenotype, heterozygous must be two in three"
assert len(_MG) == 3, f"q27: one gene with two alleles gives three genotypes; got {len(_MG)}"

_T = _phen_ratio("Aa", "aa")
assert _T[("dominant",)] == Fraction(1, 2) and _T[("recessive",)] == Fraction(1, 2), \
    f"q14: a heterozygote by a homozygous recessive must be one to one; got {_T}"

_TD = _phen_ratio("AaBb", "aabb")
assert set(_TD.values()) == {Fraction(1, 4)} and len(_TD) == 4, \
    f"q22: a dihybrid test cross must give four equal classes; got {_TD}"

_F1 = _cross("AA", "aa")
assert list(_F1) == ["Aa"] and _F1["Aa"] == 1, \
    f"q24: a homozygous dominant by homozygous recessive cross gives only heterozygotes; got {_F1}"


# ------------------------------------------------------------- table utilities

def _rows(table):
    """Rows as dicts keyed by normalized header, so a column cannot shift."""
    heads = [cg.normalize(h) for h in table["headers"]]
    return [dict(zip(heads, r)) for r in table["rows"]]


def _count(table, label_col, label, num_col):
    hit = [r for r in _rows(table) if cg.normalize(r[cg.normalize(label_col)]) == cg.normalize(label)]
    assert len(hit) == 1, f"row {label!r} appears {len(hit)} times"
    return cg.num(hit[0][cg.normalize(num_col)])


# ----------------------------------------------------------------- table checks

def q10(table, item):
    tall = _count(table, "F2 phenotype", "Tall", "Number of plants")
    short = _count(table, "F2 phenotype", "Short", "Number of plants")
    ratio = tall / short
    best = min([3.0, 1.0, 9.0, 2.0, 1 / 3], key=lambda c: abs(ratio - c))
    assert best == 3.0, f"the counts give {ratio:.3f} to 1, which is nearest {best}, not 3"
    return f"787 over 277 is {ratio:.2f} to 1, nearer three to one than any other listed ratio"


def q11(table, item):
    obs = {cg.normalize(r["f2 phenotype"]): cg.num(r["number of seeds"]) for r in _rows(table)}
    total = sum(obs.values())
    exp = {"round and yellow": total * 9 / 16, "round and green": total * 3 / 16,
           "wrinkled and yellow": total * 3 / 16, "wrinkled and green": total * 1 / 16}
    assert set(obs) == set(exp), f"unexpected classes {set(obs)}"
    for k in exp:
        assert abs(obs[k] - exp[k]) / exp[k] < 0.12, \
            f"{k}: observed {obs[k]} against expected {exp[k]:.1f} is too far for a 9:3:3:1 key"
    # the equal-classes distractor must be false on the same numbers
    assert max(obs.values()) > 2 * min(obs.values()), "'1 to 1 to 1 to 1' must be false here"
    return (f"total {total:.0f} seeds; nine, three, three and one parts predict "
            f"{exp['round and yellow']:.0f}, {exp['round and green']:.0f}, "
            f"{exp['wrinkled and yellow']:.0f} and {exp['wrinkled and green']:.0f}, each within 12 percent")


def _pedigree(table):
    rows = _rows(table)
    by_id = {cg.normalize(r["individual"]): r for r in rows}
    def aff(r):
        return cg.normalize(r["phenotype"]) == "affected"
    return rows, by_id, aff


def q12(table, item):
    rows, by_id, aff = _pedigree(table)
    # recessive: an affected child of two unaffected parents
    recessive = [r for r in rows
                 if aff(r) and cg.normalize(r["mother"]) in by_id
                 and cg.normalize(r["father"]) in by_id
                 and not aff(by_id[cg.normalize(r["mother"])])
                 and not aff(by_id[cg.normalize(r["father"])])]
    assert recessive, "no affected child of two unaffected parents: the recessive key fails"
    # not X-linked recessive: an affected daughter whose father is unaffected
    daughters = [r for r in recessive
                 if cg.normalize(r["sex"]) == "female"
                 and not aff(by_id[cg.normalize(r["father"])])]
    assert daughters, "no affected daughter of an unaffected father: X-linked recessive is not excluded"
    sexes = {cg.normalize(r["sex"]) for r in rows if aff(r)}
    assert sexes == {"male", "female"}, f"affected individuals are only {sexes}, so 'both sexes' fails"
    # the dominant distractor must be false
    assert not all(
        aff(by_id[cg.normalize(r["mother"])]) or aff(by_id[cg.normalize(r["father"])])
        for r in rows if aff(r) and cg.normalize(r["mother"]) in by_id), \
        "'every affected individual has an affected parent' must be false here"
    ids = ", ".join(sorted(cg.normalize(r["individual"]) for r in recessive))
    return (f"affected individuals {ids} have two unaffected parents, so the allele is recessive; "
            f"an affected daughter of an unaffected father excludes X-linked recessive")


def q13(table, item):
    rows, by_id, aff = _pedigree(table)
    # dominant: two affected parents with an unaffected child
    dom = [r for r in rows
           if not aff(r) and cg.normalize(r["mother"]) in by_id
           and cg.normalize(r["father"]) in by_id
           and aff(by_id[cg.normalize(r["mother"])])
           and aff(by_id[cg.normalize(r["father"])])]
    assert dom, "no unaffected child of two affected parents: the dominant key fails"
    # not X-linked dominant: an affected father with an unaffected daughter
    xd = [r for r in rows
          if cg.normalize(r["sex"]) == "female" and not aff(r)
          and cg.normalize(r["father"]) in by_id
          and aff(by_id[cg.normalize(r["father"])])]
    assert xd, "no unaffected daughter of an affected father: X-linked dominant is not excluded"
    # the recessive distractor must be false: every affected non-founder has an affected parent
    for r in rows:
        if aff(r) and cg.normalize(r["mother"]) in by_id:
            assert aff(by_id[cg.normalize(r["mother"])]) or aff(by_id[cg.normalize(r["father"])]), \
                f"individual {r['individual']} is affected with two unaffected parents, which breaks the dominant key"
    return ("two affected parents have an unaffected child, so the allele is dominant and both are "
            "heterozygous; an unaffected daughter of an affected father excludes X-linked dominant")


def q16(table, item):
    obs = [cg.num(r["observed number"]) for r in _rows(table)]
    total = sum(obs)
    exp = [total * p / 16 for p in (9, 3, 3, 1)]
    assert exp == [180, 60, 60, 20], f"expected counts recompute to {exp}, not 180/60/60/20"
    assert obs != exp, "the observed counts must differ from the expected ones"
    assert [total / 4] * 4 != exp, "the equal-classes distractor must be false"
    return f"total {total:.0f} over sixteen parts is 20 per part, giving expected {exp}"


def q19(table, item):
    rows = _rows(table)
    by_cross = {cg.normalize(r["cross"]): r for r in rows}
    def tall(k):
        return cg.num(by_cross[k]["tall offspring"])
    def short(k):
        return cg.num(by_cross[k]["short offspring"])
    assert cg.contains_phrase(by_cross["cross 2"]["parent phenotypes"], "tall by short"), \
        "cross 2 must be a tall parent by a short parent"
    assert short("cross 2") > 0, "cross 2 must produce short offspring for the key to hold"
    assert short("cross 1") == 0, "cross 1 must produce no short offspring"
    assert cg.contains_phrase(by_cross["cross 3"]["parent phenotypes"], "tall by tall"), \
        "cross 3 must not be a tall by short cross"
    return (f"cross 2 is tall by short and yields {short('cross 2'):.0f} short offspring, "
            f"while cross 1 yields none; only cross 2 is a tall by short cross revealing a recessive allele")


def q20(table, item):
    purple = _count(table, "Offspring phenotype", "Purple flowers", "Number of plants")
    white = _count(table, "Offspring phenotype", "White flowers", "Number of plants")
    total = purple + white
    assert total == 200, f"the stem says 200 offspring; the table totals {total:.0f}"
    assert purple == 98, f"the purple count is {purple:.0f}"
    for wrong in (total, white, total / 4, total * 3 / 4):
        assert wrong != purple, f"a distractor value {wrong} coincides with the key"
    return f"{purple:.0f} purple of {total:.0f} total; only the purple offspring received a dominant allele"


CLAIMS = [
 ("half of the gametes carry each allele",
  "EK 5.3.A.1 states the law of segregation and EK 5.3.A.2 makes fertilization the fusion of two HAPLOID gametes. A haploid gamete carries one allele of the gene, and a heterozygote's two alleles separate into equal numbers of gametes; the Punnett engine above builds every ratio in this module on that premise."),
 ("carried on different chromosomes",
  "EK 5.3.A.1 is explicit: Mendel's laws of segregation and independent assortment can be applied to genes that are on different chromosomes. Genes on one chromosome are genetically linked, which the framework treats under EK 5.4.A.1.i as a deviation from the predicted ratios."),
 ("creating new combinations of alleles",
  "EK 5.3.A.2 states that fertilization restores the diploid number AND increases genetic variation in populations by creating new combinations of alleles in the zygote. New combinations, not new alleles, is the framework's wording."),
 ("probability of bb are multiplied",
  "The CED's laws of probability give P(A and B) = P(A) x P(B) for independent events, and EK 5.3.A.1 makes the two genes independent here. Recomputed above from the full sixteen-way cross: the aabb class is exactly one sixteenth."),
 ("mutually exclusive genotypes",
  "The CED's laws of probability give P(A or B) = P(A) + P(B) for mutually exclusive events. Recomputed above: the homozygous dominant quarter plus the heterozygous half is exactly three quarters of the offspring."),
 ("observable expression of the trait",
  "EK 5.3.A.2.iv defines the phenotype as the observable expression of the inherited traits and EK 5.3.A.2.iii defines the genotype as the set of alleles inherited. The visible coat colour is the first and the allele pair is the second."),
 ("heterozygous for flower color",
  "EK 5.3.A.2.iii states that a genotype can be homozygous or heterozygous FOR EACH GENE, so the two terms are assigned gene by gene and one individual can be both, at different genes."),
 ("must be homozygous recessive",
  "EK 5.3.A.2.ii names the test cross among the crosses used to determine whether alleles are dominant or recessive. An individual showing the recessive phenotype carries two recessive alleles by EK 5.3.A.2.iii, so it contributes only recessive alleles and every offspring reports the other parent's contribution directly."),
 ("half of its gametes carried the recessive allele",
  "EK 5.3.A.2.ii, applied through the segregation law of EK 5.3.A.1. The recessive parent's contribution is fixed, so the offspring phenotype ratio equals the gamete ratio of the unknown parent; the engine above confirms a heterozygote by a homozygous recessive gives one to one."),
 ("3 tall plants to 1 short plant",
  "EK 5.3.A.2.ii names the monohybrid cross and EK 5.3.A.2.i licenses the probability analysis. The engine recomputes three quarters dominant for a heterozygote by heterozygote cross, and the table check shows 787 to 277 is nearer three to one than to any other listed ratio."),
 ("9 round yellow to 3 round green",
  "EK 5.3.A.1 permits independent assortment for genes on different chromosomes. The engine recomputes the four classes at nine, three, three and one sixteenths, and the table check shows each observed count lies within twelve percent of the number those proportions predict for 556 seeds."),
 ("two unaffected parents have affected children of both sexes",
  "EK 5.3.A.2.v states that patterns of inheritance and whether an allele is dominant or recessive can often be predicted from data including pedigrees. The table check recomputes both halves of the key: an affected child of two unaffected parents forces a recessive allele, and an affected daughter of an unaffected father excludes an X-linked recessive allele."),
 ("affected father has an unaffected daughter",
  "EK 5.3.A.2.v again. The table check recomputes that two affected parents have an unaffected child, which requires a dominant allele carried heterozygously, and that an affected father has an unaffected daughter, which excludes X-linked dominance because a father transmits his single X chromosome to every daughter."),
 ("and half show the recessive phenotype",
  "EK 5.3.A.2.v names Punnett squares as the tool for predicting genotypes and phenotypes of offspring. Recomputed above: a heterozygote crossed to a homozygous recessive gives exactly one half of each phenotype."),
 ("the probability for each child is one quarter and the two are multiplied",
  "EK 5.3.A.2.i licenses applying the rules of probability, and the CED's equation for independent events multiplies them. Recomputed above: one quarter squared is one sixteenth, and successive fertilizations are separate events."),
 ("180, 60, 60 and 20",
  "The CED's chi-square formula takes expected results from the null hypothesis rather than from the data. The table check recomputes 320 over sixteen parts as 20 per part, giving 180, 60, 60 and 20, and confirms the observed counts differ from those."),
 ("critical value of 3.84",
  "The CED's chi-square table states that degrees of freedom equal the number of distinct possible outcomes minus one, and prints 3.84 in the p = 0.05 row of the one degree of freedom column. Two phenotype classes give one degree of freedom; 6.63 is the p = 0.01 entry in that same column."),
 ("larger than chance alone comfortably explains",
  "The CED's chi-square table gives 3.84 at one degree of freedom and p = 0.05. A statistic above the critical value rejects the null hypothesis of agreement between observed and expected; the table is indexed by degrees of freedom, not by sample size."),
 ("crossed to a short parent produced short offspring",
  "EK 5.3.A.2.ii names the test cross. The table check recomputes that only the second cross pairs a tall parent with a short parent AND yields short offspring, which requires the tall parent to have supplied a recessive allele."),
 ("since exactly the purple offspring received it",
  "The white parent is homozygous recessive by EK 5.3.A.2.iii and supplies only a recessive allele, so purple offspring are exactly those that received a dominant allele from the other parent. The table check recomputes the count as 98 of 200 and confirms no distractor value coincides with it."),
 ("one homozygous dominant class and two heterozygous classes",
  "EK 5.3.A.2.i licenses the probability analysis. Recomputed above: conditioning the one to two to one genotype distribution on showing the dominant phenotype removes the homozygous recessive quarter and leaves two in three heterozygous."),
 ("1 dominant for both traits to 1 dominant for the first only",
  "EK 5.3.A.1 permits independent assortment and EK 5.3.A.2.v names the Punnett square. Recomputed above: a dihybrid crossed to a doubly homozygous recessive individual gives four phenotype classes at exactly one quarter each."),
 ("each parent carries one copy without showing the trait",
  "EK 5.3.A.2.iii allows a genotype to be heterozygous and EK 5.3.A.2.iv makes the phenotype the observable expression, so a heterozygote for a recessive allele transmits it while showing the dominant phenotype. EK 5.3.A.2.v states that dominance can be read from pedigree data of exactly this shape."),
 ("heterozygous and all show the dominant phenotype",
  "EK 5.3.A.2 makes fertilization the fusion of two haploid gametes. Recomputed above: a homozygous dominant parent supplies only a dominant allele and a homozygous recessive parent only a recessive allele, so every zygote is heterozygous, and by EK 5.3.A.2.iv they share one observable expression."),
 ("two genotypic classes are counted as one phenotypic class",
  "EK 5.3.A.2.iii and EK 5.3.A.2.iv separate the set of alleles from the observable expression. Recomputed above: the genotypes fall one to two to one while the phenotypes fall three to one, because complete dominance makes two of the genotype classes look alike."),
 ("nine genotypes and four phenotypes",
  "EK 5.3.A.1 permits treating the two genes independently, and the CED's multiplication rule then combines their counts. Recomputed above from the full cross: nine distinct genotypes and four phenotype classes. Sixteen is the number of Punnett square boxes, many of which repeat a genotype."),
 ("heterozygous, or homozygous for the recessive allele",
  "EK 5.3.A.2.iii states that an organism's genotype is the set of alleles inherited for a gene and can be homozygous or heterozygous. Recomputed above: a diploid gene with two available alleles admits exactly three genotypes, since a set does not record which parent supplied which allele."),
 ("small samples deviate from it by chance",
  "EK 5.3.A.2.i applies the rules of probability to the passing of single-gene traits. A probability governs each independent fertilization rather than allotting outcomes within a batch, and the engine's three quarters is the long-run expectation the counts approach."),
 ("One parent is in fact homozygous recessive",
  "Suggested skill 6.E asks students to predict the effect of a change to a component of a biological system, and EK 5.3.A.2.v makes the cross type readable from the offspring ratio. Recomputed above: replacing one heterozygous parent with a homozygous recessive one turns the cross into a test cross yielding one to one."),
 ("one quarter is multiplied by three quarters",
  "EK 5.3.A.1 permits independent treatment of genes on different chromosomes and the CED's equation multiplies independent probabilities. Recomputed above: the class recessive at one gene and dominant at the other is exactly three sixteenths of the offspring."),
]

cg.check(b5_3, CLAIMS,
         table_checks={10: q10, 11: q11, 12: q12, 13: q13, 16: q16, 19: q19, 20: q20})
print("    Punnett engine recomputed: monohybrid, dihybrid, test cross, dihybrid test cross,")
print("    conditional heterozygosity, genotype and phenotype class counts.")
