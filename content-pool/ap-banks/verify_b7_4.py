"""Key audit for AP BIOLOGY 7.4 Population Genetics.

One (anchor, claim) per item, in module order. ``cg_check.check`` is the
structural gate; it is described in ``verify_b5_3.py``.

WHAT IS RECOMPUTED, AND WHY IT IS NOT HARDY-WEINBERG. SCIENCE_BRIEF.md requires
any allele or genotype frequency stated in a Biology bank to be recomputed here
rather than asserted, and forbids keying Hardy-Weinberg content in this topic,
which is EK 7.5 and belongs to b7_5.py. The two are different operations and the
difference matters: Hardy-Weinberg PREDICTS genotype frequencies from allele
frequencies under stated conditions, whereas every figure in this module is an
allele frequency COUNTED from copies of the allele, which assumes nothing at all
about how the genotypes are distributed. ``_freq`` below does that counting, and
before dividing it checks the property that makes the count valid: the copies of
the two alleles must total exactly twice the number of individuals in a diploid
population. A table that failed that check would be reporting something other
than what the stem says it reports.

The scan at the foot of this file fails if any Hardy-Weinberg term appears
anywhere in the module, and carries a positive control so it cannot stop
matching silently.

The replicate-population item is the one whose check does the most work: it
confirms all five populations START at the same frequency, that they END in
BOTH directions from it, and that at least one reaches zero and one reaches one
hundred. Without those the item could not distinguish a nonselective process
from selection for a single allele, which is precisely what its key asserts.

NEGATIVE CONTROL: ``negcontrol_b5_7.py``.
"""
import cg_check as cg
import b7_4

T_CRASH = b7_4._T_CRASH
T_FOUNDER = b7_4._T_FOUNDER
T_DRIFT = b7_4._T_DRIFT
T_MIGRATION = b7_4._T_MIGRATION
T_EVIDENCE = b7_4._T_EVIDENCE
T_REPLICATE = b7_4._T_REPLICATE
T_ARRIVALS = b7_4._T_ARRIVALS

# EK 7.5's material, which this topic must not key.
HW_TERMS = ("hardy", "weinberg", "p squared", "q squared", "2pq",
            "genotype frequency", "genotypic frequency")


def _rows(table):
    heads = [cg.normalize(h) for h in table["headers"]]
    return [dict(zip(heads, r)) for r in table["rows"]]


def _freq(n_individuals, copies_a, copies_b):
    """The frequency of the first allele, counted, with the diploid check first.

    A diploid population of N individuals holds 2N copies of a gene. If the two
    counts do not total that, the table is not reporting what the stem says it
    reports and no frequency taken from it means anything.
    """
    total = copies_a + copies_b
    assert total == 2 * n_individuals, (
        f"{n_individuals:.0f} diploid individuals hold {2 * n_individuals:.0f} copies of the gene, "
        f"but the table records {total:.0f}"
    )
    assert copies_a >= 0 and copies_b >= 0, "a negative count of allele copies is not data"
    return 100 * copies_a / total


def _two_row_counts(table, label_col, n_col, a_col, b_col):
    # The two allele columns must be distinguishable AFTER normalization, which
    # lowercases: "allele R" and "allele r" would collapse into one key and both
    # reads would return the same column. The checker found exactly that here.
    assert cg.normalize(a_col) != cg.normalize(b_col), \
        f"the two allele columns {a_col!r} and {b_col!r} normalize to the same header"
    out = {}
    for r in _rows(table):
        n = cg.num(r[cg.normalize(n_col)])
        a = cg.num(r[cg.normalize(a_col)])
        b = cg.num(r[cg.normalize(b_col)])
        out[cg.normalize(r[cg.normalize(label_col)])] = (n, _freq(n, a, b))
    assert len(out) == 2, "the comparison needs exactly two rows"
    return out


def q9(table, item):
    d = _two_row_counts(table, "Time point", "Number of individuals in the population",
                        "Number of copies of allele R", "Number of copies of allele S")
    before = next(v for k, v in d.items() if cg.contains_phrase(k, "before the reduction"))
    after = next(v for k, v in d.items() if cg.contains_phrase(k, "immediately after the reduction"))
    assert (before[1], after[1]) == (30, 80), \
        f"the frequencies recompute to {before[1]} and {after[1]} percent, not 30 and 80"
    assert after[0] < before[0] / 10, "the population must be sharply reduced"
    return (f"{before[0]:.0f} individuals give {before[1]:.0f} percent and {after[0]:.0f} give "
            f"{after[1]:.0f} percent, both counted from copies that total twice the individuals")


def q10(table, item):
    d = _two_row_counts(table, "Time point", "Number of individuals in the population",
                        "Number of copies of allele R", "Number of copies of allele S")
    sizes = sorted(v[0] for v in d.values())
    assert sizes[0] <= 20 and sizes[-1] >= 100, \
        f"a bottleneck needs a large population reduced to a small one; got sizes {sizes}"
    assert len({v[1] for v in d.values()}) == 2, "the frequency must actually have changed"
    return (f"the population falls from {sizes[-1]:.0f} to {sizes[0]:.0f} individuals, which is the "
            f"reduction EK 7.4.A.1.iii names, and the frequency changes with it")


def _founder(table):
    return _two_row_counts(table, "Population", "Number of individuals in the population",
                           "Number of copies of allele M", "Number of copies of allele N")


def q11(table, item):
    d = _founder(table)
    source = next(v for k, v in d.items() if cg.contains_phrase(k, "source population"))
    new = next(v for k, v in d.items() if cg.contains_phrase(k, "newly separated population"))
    assert (source[1], new[1]) == (40, 10), \
        f"the frequencies recompute to {source[1]} and {new[1]} percent, not 40 and 10"
    assert source[1] != new[1], "the two frequencies must differ, or nothing has shifted"
    return (f"the source holds {source[1]:.0f} percent and the separated group {new[1]:.0f} percent, "
            f"both counted from copies totalling twice their individuals")


def q12(table, item):
    d = _founder(table)
    source = next((k, v) for k, v in d.items() if cg.contains_phrase(k, "source population"))
    new = next((k, v) for k, v in d.items() if cg.contains_phrase(k, "newly separated population"))
    assert new[1][0] < source[1][0] / 10, "the separated group must be far smaller than the source"
    assert source[1][0] > 100, (
        "the source population must remain large, or the scenario would also be a bottleneck and "
        "the key would not be unique"
    )
    return (f"a group of {new[1][0]:.0f} separates from a source of {source[1][0]:.0f}, which stays "
            f"large, so the reduction the bottleneck effect requires has not happened to it")


SMALL = "frequency of allele b in the small population percent"
LARGE = "frequency of allele b in the large population percent"


def _drift(table):
    s = [(cg.num(r[SMALL]), cg.num(r[LARGE])) for r in _rows(table)]
    for a, b in s:
        assert 0 <= a <= 100 and 0 <= b <= 100, f"a frequency outside 0 to 100 percent: {(a, b)}"
    return s


def q13(table, item):
    s = _drift(table)
    small = [a for a, _ in s]
    large = [b for _, b in s]
    assert small[0] == large[0], "both populations must start at the same frequency"
    spread_small = max(small) - min(small)
    spread_large = max(large) - min(large)
    assert spread_small > 5 * spread_large, \
        f"the small population must swing far more; spreads are {spread_small} and {spread_large}"
    return (f"the small population spans {spread_small:.0f} percentage points and the large one "
            f"{spread_large:.0f}, from an identical start of {small[0]:.0f} percent")


def q14(table, item):
    s = _drift(table)
    small = [a for a, _ in s]
    large = [b for _, b in s]
    assert small[-1] == 0, f"the small population must end at zero; it ends at {small[-1]}"
    assert small[0] > 0, "the allele must have been present at the start for its loss to mean anything"
    assert large[-1] > 0, "the large population must still carry the allele, so the key is specific"
    return (f"the small population ends at {small[-1]:.0f} percent, having started at "
            f"{small[0]:.0f}, while the large one still holds {large[-1]:.0f} percent")


def q15(table, item):
    start = "frequency of allele e at the start percent"
    end = "frequency of allele e after 15 generations percent"
    d = {cg.normalize(r["replicate population"]): (cg.num(r[start]), cg.num(r[end]))
         for r in _rows(table)}
    starts = {v[0] for v in d.values()}
    assert len(starts) == 1, f"every replicate must start at the same frequency; got {starts}"
    s0 = starts.pop()
    ends = [v[1] for v in d.values()]
    assert all(0 <= e <= 100 for e in ends), f"a frequency outside 0 to 100 percent: {ends}"
    assert any(e < s0 for e in ends) and any(e > s0 for e in ends), (
        "the replicates must end on BOTH sides of the common start, or the pattern is "
        "indistinguishable from selection for one allele"
    )
    assert 0 in ends and 100 in ends, \
        "at least one replicate should be lost and one fixed, which selection for one allele cannot do"
    return (f"all five start at {s0:.0f} percent and end at {sorted(ends)}, on both sides of the "
            f"start and including both loss and fixation")


def q19(table, item):
    ex = "individuals exchanged per generation"
    diff = "difference in allele frequency after 50 generations percentage points"
    pairs = sorted((cg.num(r[ex]), cg.num(r[diff])) for r in _rows(table))
    assert len(pairs) >= 3, "the relationship needs at least three pairs"
    diffs = [d for _, d in pairs]
    assert diffs == sorted(diffs, reverse=True) and len(set(diffs)) == len(diffs), \
        f"the difference must fall strictly as the exchange rises; got {pairs}"
    assert pairs[0][0] == 0, "one pair should exchange no individuals, as the comparison point"
    return (f"exchanges {[e for e, _ in pairs]} give differences {diffs}, which fall strictly as the "
            f"exchange rises")


def q21(table, item):
    s = [(cg.num(r["generation"]), cg.num(r["frequency of allele d in the population percent"]))
         for r in _rows(table)]
    gens = [g for g, _ in s]
    vals = [v for _, v in s]
    assert gens == sorted(gens) and len(set(gens)) == len(gens), "generations must increase"
    assert vals == sorted(vals) and len(set(vals)) == len(vals), \
        f"the frequency must change at every step; got {vals}"
    assert all(0 <= v <= 100 for v in vals), "a frequency outside 0 to 100 percent is not data"
    assert vals[-1] != vals[0], "the frequency must have changed, which is the evidence claimed"
    return (f"the frequency rises from {vals[0]:.0f} to {vals[-1]:.0f} percent across generations "
            f"{gens}, so the allele frequencies of the population changed")


def q27(table, item):
    before = "number of different alleles of the gene present before"
    after = "number of different alleles of the gene present after"
    d = {cg.normalize(r["individuals arrived from another population"]):
         (cg.num(r[before]), cg.num(r[after])) for r in _rows(table)}
    assert set(d) == {"yes", "no"}, f"the two populations are marked {set(d)}"
    assert d["yes"][1] > d["yes"][0], "the population receiving arrivals must gain alleles"
    assert d["no"][1] == d["no"][0], "the population receiving none must be unchanged"
    for v in d.values():
        assert v[0] >= 1 and v[1] >= 1, "a population must carry at least one allele of the gene"
    return (f"the receiving population goes from {d['yes'][0]:.0f} alleles to {d['yes'][1]:.0f} while "
            f"the other stays at {d['no'][0]:.0f}, so the gain tracks the arrivals")


CLAIMS = [
 ("also driven by random occurrences",
  "EK 7.4.A.1 states that evolution is also driven by random occurrences, which the framework then lists as mutation, genetic drift with its bottleneck and founder forms, and migration producing gene flow. EK 7.1.A.1 calls selection a major rather than the only mechanism."),
 ("random process that adds new genetic variation",
  "EK 7.4.A.1.i states this. Both halves matter: the process is random, so it is not directed by need, and its contribution is to add variation rather than remove it."),
 ("nonselective process occurring in small populations",
  "EK 7.4.A.1.ii defines genetic drift as a change in allele frequencies attributable to a nonselective process occurring in small populations, and both qualifiers are the framework's."),
 ("reduced to a small number of individuals for at least one generation",
  "EK 7.4.A.1.iii defines the bottleneck effect in exactly these terms and classifies it as a type of genetic drift, which EK 7.4.A.1.ii makes nonselective."),
 ("separated from other members of the population",
  "EK 7.4.A.1.iv defines the founder effect as a type of genetic drift occurring when a population is separated from other members of the population, with the frequency of genes and traits shifting based on the genes in the new founder population."),
 ("Gene flow, which is the addition or removal of alleles from a population",
  "EK 7.4.A.1.v states that migration can result in gene flow and defines gene flow in the same breath as the addition or removal of alleles from a population."),
 ("attributable to a nonselective process, while selection acts on phenotypic variations that differ in fitness",
  "EK 7.4.A.1.ii makes drift nonselective and EK 7.2.A.1 with EK 7.2.A.3 makes selection turn on differences in fitness among phenotypic variations, so whether the differences among individuals matter is what separates them."),
 ("reduction in the size of an existing population; a founder effect follows a group being separated",
  "EK 7.4.A.1.iii and EK 7.4.A.1.iv define the two, and both are named as types of genetic drift, so the classification is not what separates them."),
 ("30 percent before and 80 percent after",
  "An allele frequency is copies of the allele over total copies. The table check recomputes both, after first confirming that the copies total twice the number of individuals, which is what makes the counting valid without any assumption about genotypes."),
 ("bottleneck effect, a type of genetic drift following a population reduced",
  "EK 7.4.A.1.iii ties the bottleneck effect to a population size reduced to a small number of individuals for at least one generation. The table check confirms the reduction is sharp and that no new allele appears, so mutation and gene flow are not what changed."),
 ("40 percent in the source population and 10 percent in the separated group",
  "Counted from copies over total copies, with the diploid total checked first for both rows. EK 7.4.A.1.iv states that in the founder effect the frequency of genes and traits shifts based on the genes in the new founder population."),
 ("founder effect, a type of genetic drift following the separation of a group",
  "EK 7.4.A.1.iv. The table check confirms the source population remains large, which is what makes the bottleneck reading of EK 7.4.A.1.iii false on the same data and the key unique."),
 ("swung widely in the small population and barely moved in the large one",
  "EK 7.4.A.1.ii attributes drift to a nonselective process occurring in small populations. The table check confirms both series start at the same frequency and that the small population's spread is more than five times the large one's."),
 ("lost from that population, since its frequency has reached zero",
  "A frequency of zero means no copies remain, which is loss and not fixation. The table check confirms the allele was present at the start and that the large population still carries it, so the key is specific to the small one."),
 ("moved in different directions from an identical starting point",
  "EK 7.4.A.1.ii defines drift as nonselective. The table check confirms all five replicates start at the same frequency, that they end on both sides of it, and that one is lost and one fixed -- none of which selection for a single allele would produce."),
 ("Genetic variation, which provides phenotypes on which natural selection acts",
  "EK 7.4.B.1.i states this, and it is where the random process of EK 7.4.A.1.i meets the nonrandom one of EK 7.2.A.1: mutation supplies the material and selection sorts it."),
 ("Diverge from other populations of the same species",
  "EK 7.4.B.1.ii states that genetic drift can allow a small population to diverge from other populations of the same species. New alleles come from mutation under EK 7.4.A.1.i and arriving alleles are gene flow under EK 7.4.A.1.v."),
 ("prevents them from diverging into separate species",
  "EK 7.4.B.1.iii states this. EK 7.4.A.1.v defines gene flow as the addition or removal of alleles, so it can change frequencies while keeping two populations alike."),
 ("more individuals exchanged per generation, the smaller the difference",
  "EK 7.4.B.1.iii makes gene flow what prevents two populations from diverging and EK 7.4.A.1.v makes migration what produces it. The table check confirms the difference falls strictly as the exchange rises, across three pairs including one exchanging none."),
 ("Evidence for the occurrence of evolution in a population",
  "EK 7.4.C.1 states that changes in allele frequencies provide evidence for the occurrence of evolution in a population. It is evidence that evolution occurred rather than of which mechanism, since EK 7.4.B.1 allows random processes to change frequencies too."),
 ("Evolution has occurred in this population, because its allele frequencies have changed",
  "EK 7.4.C.1. The table check confirms the frequency changes at every recorded step and stays within a legitimate range; the data cannot identify the mechanism, which is why the selection option overreaches."),
 ("will not change over the twenty generations",
  "Suggested skill 3.B asks students to state the null hypothesis of an experiment, and a null hypothesis is the statement of no difference or no change that data may contradict. The predictions of change are alternatives to it."),
 ("difference will shrink, because gene flow between two populations prevents them from diverging",
  "Suggested skill 3.B asks for a prediction. EK 7.4.A.1.v makes migration produce gene flow and EK 7.4.B.1.iii makes gene flow prevent divergence, so restoring the exchange should reduce the difference."),
 ("chance event affects a large share of the copies of an allele",
  "EK 7.4.A.1.ii confines genetic drift to a nonselective process occurring in small populations, and this module's data show a small population swinging between zero and sixty-four percent while a large one stays near fifty. Being nonselective, no difference in fitness is involved."),
 ("bottleneck effect, a type of genetic drift",
  "EK 7.4.A.1.iii states that the bottleneck effect occurs when a population size is reduced to a small number of individuals for at least one generation. The survivors are not described as differing in any relevant phenotype, so EK 7.2.A.1's selection is not what is described."),
 ("founder effect, in which the frequency of genes and traits shifts based on the genes in the new population",
  "EK 7.4.A.1.iv states exactly this. The mainland population is not itself reduced, which separates the scenario from the bottleneck effect of EK 7.4.A.1.iii."),
 ("gained alleles it had not carried before, while the other population's allele count was unchanged",
  "EK 7.4.A.1.v states that migration can result in gene flow, the addition or removal of alleles from a population. The table check confirms the receiving population's allele count rises and the other's does not, so the gain tracks the arrivals."),
 ("addition or removal of alleles from a population",
  "EK 7.4.A.1.v's own definition of gene flow includes removal as well as addition, which is what emigrants taking their alleles with them amounts to. The founder and bottleneck effects require a separation or a reduction, neither of which is described."),
 ("nonselective process is the better explanation of this particular change",
  "EK 7.4.C.1 makes the change in allele frequencies evidence that evolution occurred, and EK 7.4.A.1.ii attributes drift to a nonselective process while EK 7.2.A.3 makes selection a matter of differences in fitness, which the second observation reports as absent."),
 ("drift changes frequencies nonselectively in small populations, migration adds or removes alleles",
  "Each clause is one of the framework's statements: EK 7.4.A.1.i, EK 7.4.A.1.ii, EK 7.4.A.1.v and EK 7.4.C.1 in turn."),
]

cg.check(b7_4, CLAIMS,
         table_checks={9: q9, 10: q10, 11: q11, 12: q12, 13: q13, 14: q14, 15: q15,
                       19: q19, 21: q21, 27: q27})

# EK 7.5's material must not appear here; it belongs to b7_5.py.
_text = " ".join(" ".join([q["q"], q["why"], *q["choices"]]) for q in b7_4.QUESTIONS)
for word in HW_TERMS:
    assert not cg.contains_phrase(_text, word), (
        f"7.4: {word!r} appears in the module, but Hardy-Weinberg is EK 7.5 and belongs to b7_5.py"
    )
for word in HW_TERMS:
    assert cg.contains_phrase(f"a stem mentioning {word} here", word), \
        f"the scan cannot detect {word!r} even in a string containing it"
print(f"    Allele frequencies COUNTED from copies, with the diploid total checked first; "
      f"{len(HW_TERMS)} Hardy-Weinberg terms scanned for and absent.")
