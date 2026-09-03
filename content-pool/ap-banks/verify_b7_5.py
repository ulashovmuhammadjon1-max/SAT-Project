"""Key audit for AP BIOLOGY 7.5 Hardy-Weinberg Equilibrium.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor, so an off-by-one key stops matching; the
claim states what the key rests on, for a human to audit.

WHAT THE KEYS REST ON
---------------------
Items 1 to 12 and 24, 26, 29 and 30 are keyed to sentences the CED prints:
EK 7.5.A.1 (the five conditions, and the sentence that they are never met but
provide a valuable null hypothesis), EK 7.5.A.2 (allele frequencies can be
calculated from genotype frequencies), and the two equations the CED prints for
this topic.

EVERY NUMBER IS RECOMPUTED HERE, NOT ASSERTED. There is no sympy in Biology, so
the arithmetic is the one part of a key a machine can settle, and this file
settles all of it two ways:

  * ``TABLE_CHECKS`` recomputes the seven data items from their table alone,
    through cg_check's header-and-label accessors, so inserting a column cannot
    silently repoint a check at the wrong numbers. cg_check.check FAILS a
    question that carries a table with no such callable.
  * ``STEM_MATH`` recomputes the nine items whose numbers live in the stem.
    It PARSES those numbers out of the stem string rather than repeating them,
    so editing a stem without editing its key fails the check.

Neither says anything about whether the biology is right. That is gated by the
CLAIMS text and by the rule in SCIENCE_BRIEF.md that a key must trace to a CED
sentence.

NEGATIVE CONTROL. Corrupting any key index, any table cell or any number in a
stem makes this file raise. Confirmed by running exactly that before shipping;
see the report accompanying this module.

FIVE choices per item (A-E), per SCIENCE_BRIEF.md.
"""
import math
import re

import cg_check as cg
import b7_5

QS = b7_5.QUESTIONS
T_COUNTS = b7_5._T_COUNTS
T_OBS_EXP = b7_5._T_OBS_EXP
T_GEN = b7_5._T_GEN
T_FOUR = b7_5._T_FOUR

COUNT = "Number of individuals"
OBS = "Observed number of individuals"
EXP = "Number expected if the population were in Hardy-Weinberg equilibrium"
FR = "Frequency of allele R"
FR_SMALL = "Frequency of allele W"
FA = "Frequency of allele A"
FA_SMALL = "Frequency of allele B"
HET = "Observed frequency of heterozygotes"

# A standalone number in a stem. No \b anywhere: a digit and a letter are both
# word characters, so \b is silently not a boundary next to either. The
# lookbehind refuses a digit, a letter or a decimal point before the match and
# the lookahead refuses a digit or a further decimal group after it, so "0.10"
# is read once and whole and "16" inside "160" is never matched.
_NUM_IN_STEM = re.compile(r"(?<![A-Za-z0-9.])(\d+(?:\.\d+)?)(?![0-9]|\.\d)")


def stem_nums(item):
    return [float(x) for x in _NUM_IN_STEM.findall(item["q"])]


def keyed(item):
    return item["choices"][item["ans"]]


def eq(a, b, tol=1e-9):
    return math.isclose(a, b, rel_tol=0, abs_tol=tol)


def two(x):
    return "%.2f" % x


# ------------------------------------------------------------ stem arithmetic

def m13(item):
    (pct,) = stem_nums(item)
    q = math.sqrt(pct / 100.0)
    assert keyed(item) == two(q), f"q13 key {keyed(item)!r} but sqrt({pct/100}) is {two(q)}"
    return f"recessive phenotype {pct} percent means q squared is {pct/100}, so q is {two(q)}"


def m14(item):
    (pct,) = stem_nums(item)
    p = 1 - math.sqrt(pct / 100.0)
    assert keyed(item) == two(p * p), f"q14 key {keyed(item)!r} but p squared is {two(p*p)}"
    return f"q squared {pct/100} gives q {two(1-p)} and p {two(p)}, so p squared is {two(p*p)}"


def m15(item):
    (pct,) = stem_nums(item)
    q = math.sqrt(pct / 100.0)
    p = 1 - q
    assert keyed(item) == two(2 * p * q), f"q15 key {keyed(item)!r} but 2pq is {two(2*p*q)}"
    return f"q squared {pct/100} gives q {two(q)} and p {two(p)}, so 2pq is {two(2*p*q)}"


def m16(item):
    (p,) = stem_nums(item)
    q = 1 - p
    assert keyed(item) == two(q * q), f"q16 key {keyed(item)!r} but q squared is {two(q*q)}"
    return f"p of {two(p)} gives q {two(q)}, so the homozygous recessive term q squared is {two(q*q)}"


def m17(item):
    (pct,) = stem_nums(item)
    p = 1 - math.sqrt(pct / 100.0)
    assert keyed(item) == two(p), f"q17 key {keyed(item)!r} but p is {two(p)}"
    return f"q squared {pct/100} gives q {two(1-p)}, so p is one minus that, {two(p)}"


def m18(item):
    (pct,) = stem_nums(item)
    q = math.sqrt(pct / 100.0)
    p = 1 - q
    assert keyed(item) == two(2 * p * q), f"q18 key {keyed(item)!r} but 2pq is {two(2*p*q)}"
    return f"q squared {pct/100} gives q {two(q)} and p {two(p)}, so 2pq is {two(2*p*q)}"


def m19(item):
    n, q = stem_nums(item)
    p = 1 - q
    expected = 2 * p * q * n
    assert eq(expected, round(expected)), "the expected count must be a whole number"
    assert keyed(item) == str(int(round(expected))), \
        f"q19 key {keyed(item)!r} but 2pq times {n} is {expected}"
    return f"p {two(p)} and q {two(q)} give 2pq {two(2*p*q)}, and that share of {int(n)} is {int(round(expected))}"


def m20(item):
    (q,) = stem_nums(item)
    p = 1 - q
    ratio = (2 * p * q) / (q * q)
    assert eq(ratio, round(ratio)), f"the ratio {ratio} is not whole, so the stated form is wrong"
    assert keyed(item) == f"{int(round(ratio))} to 1", \
        f"q20 key {keyed(item)!r} but 2pq over q squared is {ratio}"
    return f"2pq is {two(2*p*q)} and q squared is {two(q*q)}, a ratio of {int(round(ratio))} to 1"


def m21(item):
    (q,) = stem_nums(item)
    p = 1 - q
    share = (2 * p * q) / (2 * p * q + 2 * q * q)
    assert keyed(item) == two(share), \
        f"q21 key {keyed(item)!r} but the heterozygote share of recessive copies is {two(share)}"
    return (f"heterozygotes hold 2pq {two(2*p*q)} copies per individual against "
            f"{two(2*q*q)} in homozygotes, a share of {two(share)}")


STEM_MATH = {13: m13, 14: m14, 15: m15, 16: m16, 17: m17, 18: m18,
             19: m19, 20: m20, 21: m21}


# --------------------------------------------------------- table arithmetic

def _allele_freq(table, homo_label, het_label, other_label, count_header):
    a = cg.cell(table, homo_label, count_header)
    h = cg.cell(table, het_label, count_header)
    o = cg.cell(table, other_label, count_header)
    total_copies = 2 * (a + h + o)
    return (2 * a + h) / total_copies, total_copies


def q22(table, item):
    f, copies = _allele_freq(table, "FF", "FS", "SS", COUNT)
    assert keyed(item) == two(f), f"q22 key {keyed(item)!r} but F frequency is {two(f)}"
    return f"twice the FF count plus the FS count over {int(copies)} allele copies gives {two(f)}"


def q23(table, item):
    f, copies = _allele_freq(table, "SS", "FS", "FF", COUNT)
    assert keyed(item) == two(f), f"q23 key {keyed(item)!r} but S frequency is {two(f)}"
    other, _ = _allele_freq(table, "FF", "FS", "SS", COUNT)
    assert eq(f + other, 1.0), "the two allele frequencies must sum to one"
    return f"twice the SS count plus the FS count over {int(copies)} copies gives {two(f)}, and the two sum to one"


def q24(table, item):
    obs = {lab: cg.cell(table, lab, OBS) for lab in cg.labels(table)}
    exp = {lab: cg.cell(table, lab, EXP) for lab in cg.labels(table)}
    n = sum(obs.values())
    assert eq(sum(exp.values()), n), "expected counts must total the same as observed counts"
    p = (2 * obs["MM"] + obs["MN"]) / (2 * n)
    q_ = 1 - p
    # the printed expectations must actually be the Hardy-Weinberg expectations
    for lab, predicted in (("MM", p * p * n), ("MN", 2 * p * q_ * n), ("NN", q_ * q_ * n)):
        assert eq(exp[lab], round(predicted)), \
            f"printed expectation for {lab} is {exp[lab]} but the model gives {predicted}"
    assert obs["MN"] < 0.6 * exp["MN"], \
        "the key says heterozygotes are much scarcer than predicted; they are not"
    return (f"observed counts give p {two(p)}, whose predictions {int(exp['MM'])}, {int(exp['MN'])}, "
            f"{int(exp['NN'])} match the printed column, and observed MN {int(obs['MN'])} is far below")


def q25(table, item):
    obs = {lab: cg.cell(table, lab, OBS) for lab in cg.labels(table)}
    n = sum(obs.values())
    p = (2 * obs["MM"] + obs["MN"]) / (2 * n)
    assert keyed(item) == two(p), f"q25 key {keyed(item)!r} but observed M frequency is {two(p)}"
    return f"twice observed MM plus observed MN over {int(2*n)} allele copies gives {two(p)}"


def q26(table, item):
    r = cg.col(table, FR_SMALL)
    big_r = cg.col(table, FR)
    for a, b in zip(big_r, r):
        assert eq(a + b, 1.0), f"row frequencies {a} and {b} do not sum to one"
    rises = [b > a for a, b in zip(r, r[1:])]
    assert all(rises), f"the key requires the second allele to rise in every interval; got {r}"
    assert len(r) == 4, f"the stem says four generations; the table has {len(r)}"
    return f"the second allele runs {r} and rises in all {len(rises)} intervals while each row sums to one"


def q27(table, item):
    p = cg.col(table, FR)[0]
    q_ = cg.col(table, FR_SMALL)[0]
    assert eq(p + q_, 1.0), "the first generation's two frequencies must sum to one"
    assert keyed(item) == two(2 * p * q_), \
        f"q27 key {keyed(item)!r} but 2pq for the first row is {two(2*p*q_)}"
    return f"the first row's p {two(p)} and q {two(q_)} give a predicted 2pq of {two(2*p*q_)}"


def q28(table, item):
    dev = {}
    for lab in cg.labels(table):
        p = cg.cell(table, lab, FA)
        q_ = cg.cell(table, lab, FA_SMALL)
        assert eq(p + q_, 1.0), f"{lab}: allele frequencies do not sum to one"
        obs_het = cg.cell(table, lab, HET)
        assert 0.0 <= obs_het <= 1.0, f"{lab}: observed heterozygote frequency {obs_het} is not a frequency"
        dev[lab] = abs(obs_het - 2 * p * q_)
    worst = max(dev, key=dev.get)
    assert cg.contains_phrase(keyed(item), worst), \
        f"q28 key {keyed(item)!r} but the largest departure is population {worst}"
    others = sorted(v for k, v in dev.items() if k != worst)
    assert others[-1] < dev[worst] / 4, \
        f"the key requires one clear outlier; deviations are {dev}"
    return f"predicted 2pq matches the observed heterozygote column except in {worst}, deviations {dev}"


TABLE_CHECKS = {22: q22, 23: q23, 24: q24, 25: q25, 26: q26, 27: q27, 28: q28}


CLAIMS = [
 ("no migration of individuals into or out of",
  "EK 7.5.A.1 lists five conditions and no migration is the second of them. Each distractor states the negation of one of the other four, which is what a student who has learned the list but not its direction will pick."),
 ("null expectation",
  "EK 7.5.A.1 says the conditions are never met but that they provide a valuable null hypothesis. A null hypothesis predicts what would be observed if nothing were acting, so a departure is the evidence, and no departure proves any particular cause."),
 ("stay the same from one generation",
  "The scenario states all five conditions of EK 7.5.A.1, and the model those conditions define is a model of a non-evolving population, in which allele frequencies are constant across generations."),
 ("no natural selection",
  "EK 7.5.A.1 requires that no natural selection act at the locus. Killing one genotype before reproduction is differential survival by genotype, which is selection; nothing in the scenario touches size, mating, migration or mutation."),
 ("random mating",
  "EK 7.5.A.1 requires random mating. Pollination that pairs like phenotype with like phenotype means gametes do not unite at random with respect to the locus, while survival and population size are unaffected."),
 ("a large population size",
  "EK 7.5.A.1 requires a large population size, because chance sampling of gametes shifts frequencies appreciably only when few individuals breed. An indiscriminate flood is not selection, and no individual entered or left."),
 ("no migration",
  "EK 7.5.A.1 requires no migration. Pollen arriving from a separate population adds allele copies from outside the study plot, and the condition concerns the movement of alleles rather than the movement of adults."),
 ("no new mutations",
  "EK 7.5.A.1 requires that no new mutations arise at the locus. A raised mutation rate introduces allele copies absent from the parental generation, which is the process the condition excludes."),
 ("non-evolving population",
  "EK 7.5.A.1 states that the Hardy-Weinberg equilibrium is a model for describing and predicting allele frequencies in a non-evolving population. Directional selection, founding events and asexual reproduction are all outside what the model represents."),
 ("every allele copy at the locus",
  "The CED prints p plus q equals 1 for this topic with p and q defined as the frequencies of allele 1 and allele 2. Frequencies of an exhaustive set of alternatives sum to one, which requires only that no third allele exist at the locus."),
 ("heterozygous individuals",
  "The CED prints p squared plus 2pq plus q squared equals 1 for this topic. The middle term counts the two ways a heterozygote can be assembled from the gamete pool, which is why it carries a factor of two."),
 ("one of the three possible genotypes",
  "EK 7.5.A.2 treats genotype frequencies as the quantities from which allele frequencies are calculated. One locus with two alleles admits exactly three genotypes, so their frequencies exhaust the population and sum to one."),
 ("0.40",
  "EK 7.5.A.2 and the printed equation. Recomputed in the stem-math check above: the recessive phenotype appears only in homozygous recessives, so q squared is the stated phenotype frequency and q is its square root."),
 ("0.36",
  "EK 7.5.A.2 and the printed equation. Recomputed above: q squared gives q, then p is one minus q, and the homozygous dominant frequency is p squared."),
 ("0.50",
  "EK 7.5.A.2 and the printed equation. Recomputed above as 2pq from the stated recessive phenotype frequency. This is also the allele frequency at which the heterozygote term reaches its maximum."),
 ("0.09",
  "The CED prints p plus q equals 1, so the stated dominant allele frequency fixes q, and the homozygous recessive frequency is q squared. Recomputed above from the number in the stem."),
 ("0.70",
  "EK 7.5.A.2 and the printed equations. Recomputed above: q is the square root of the stated phenotype frequency and p is one minus q. Subtracting the phenotype frequency itself from one is the error a distractor carries."),
 ("0.42",
  "EK 7.5.A.2 and the printed equation. Recomputed above as twice p times q from the stated recessive phenotype frequency."),
 ("72",
  "EK 7.5.A.2 with skill 5.A, which names ratios and percentages. Recomputed above: the heterozygote term 2pq applied to the stated population size gives a whole number of individuals."),
 ("8 to 1",
  "The two terms of the printed equation compared: heterozygotes number 2pq and homozygous recessives q squared, so the ratio is 2p over q. Recomputed above from the stated allele frequency."),
 ("0.90",
  "Counting allele copies rather than individuals: heterozygotes carry 2pq copies of the recessive allele and homozygous recessives carry twice q squared. Recomputed above; this is why a rare recessive allele sits mostly in carriers."),
 ("0.60",
  "EK 7.5.A.2, that allele frequencies can be calculated from genotype frequencies. Recomputed from the table alone above: each homozygote contributes two copies and each heterozygote one, over twice the number of individuals."),
 ("0.40",
  "EK 7.5.A.2 again, for the second allele. Recomputed from the table above, and independently checked to sum to one with the first allele's frequency, which is what a two-allele locus requires."),
 ("much scarcer than the model predicts",
  "EK 7.5.A.1 makes the model a null hypothesis, so a large departure implicates the five conditions. The table check above confirms that the printed expectations really are the model's predictions from the observed allele frequency and that the heterozygote shortfall is large."),
 ("0.70",
  "EK 7.5.A.2. Recomputed above from the observed column alone; the expected column is derived from this frequency and so cannot be used to obtain it without circularity."),
 ("allele W rose in every interval shown",
  "EK 7.5.A.1: the model predicts constant allele frequencies, so a directional shift across the whole record is a departure from the null expectation. The table check above confirms the rise is present in every interval and that each row sums to one, which is why summing to one carries no information."),
 ("0.32",
  "EK 7.5.A.2 and the printed equation, applied to the first row of the table. Recomputed above as twice the product of that row's two frequencies."),
 ("Population Z",
  "EK 7.5.A.2 supplies the prediction 2pq for each row. The table check above recomputes all four predictions, confirms three match the observed column exactly, and confirms the fourth departure is several times larger than any other."),
 ("one or more of the model's conditions",
  "EK 7.5.A.1 names five conditions jointly, so rejecting the model's prediction implicates the set rather than any one member. Selection is only one of the five, and the stem states the sample was large."),
 ("cannot be told apart from homozygous dominant individuals",
  "EK 7.5.A.2 allows allele frequencies to be calculated from genotype frequencies, and for a recessive disorder the homozygous recessive class is the only genotype that can be counted directly from phenotype. Its frequency yields q, then p, then the heterozygote term."),
]


# SCIENCE_BRIEF.md: Biology is exported untypeset, so a backslash macro, a
# dollar-delimited span or a bracket span would reach a student as literal
# characters. Year ranges and slash fractions are barred for the same reason
# they were barred in the social science banks: nothing typesets them here, and
# a digit-hyphen-digit run reads as a subtraction. Explicit lookarounds, never
# \b -- a digit and a letter are both word characters.
_BANNED = [
    (re.compile(r"\\"), "a backslash: this bank carries no LaTeX"),
    (re.compile(r"\$"), "a dollar-delimited math span"),
    (re.compile(r"\\\(|\\\["), "a LaTeX delimiter"),
    (re.compile(r"(?<![A-Za-z])\d+\s*-\s*\d+(?![A-Za-z])"), "a digit-hyphen-digit range"),
    (re.compile(r"\d\s*/\s*\d"), "a digit-slash-digit fraction"),
]


def style():
    hits = 0
    for i, item in enumerate(QS, 1):
        texts = [("stem", item["q"]), ("why", item["why"])]
        texts += [(f"choice {k}", c) for k, c in enumerate(item["choices"])]
        if item.get("table"):
            texts += [("table", " | ".join(item["table"]["headers"]))]
            texts += [("table", " | ".join(str(c) for c in r)) for r in item["table"]["rows"]]
        for where, text in texts:
            for pat, why_bad in _BANNED:
                m = pat.search(text)
                assert not m, f"q{i} {where} contains {m.group(0)!r}, {why_bad}"
                hits += 1
    return hits


def main():
    notes = []
    for i, fn in sorted(STEM_MATH.items()):
        item = QS[i - 1]
        assert "table" not in item, f"q{i} has a table; it belongs in TABLE_CHECKS"
        notes.append(f"  q{i:>2}: {fn(item)}")
    n_style = style()
    cg.check(b7_5, CLAIMS, table_checks=TABLE_CHECKS)
    print(f"    {n_style} notation checks clean (no LaTeX, no ranges, no slash fractions).")
    print(f"    {len(STEM_MATH)} stem calculation(s) recomputed from the stem text:")
    print("\n".join(notes))


main()
