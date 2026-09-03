"""Key audit for AP BIOLOGY 7.1 Introduction to Natural Selection.

One (anchor, claim) per item, in module order. ``cg_check.check`` is the
structural gate; it is described in ``verify_b5_3.py``.

WHAT IS RECOMPUTED. Six items carry data and each table is recomputed from its
own contents. Two of them are the ones worth naming: the fitness table is
checked to have its highest offspring count and its longest lifespan on
DIFFERENT rows, because if they coincided the item could not distinguish the
framework's measure from the intuitive one and both keys would be defensible;
and the three-phenotype item multiplies survival by offspring per survivor to
get the expected offspring per individual born, which is the only way the
lowest-surviving phenotype comes out highest. The reversal items are checked for
an actual reversal rather than merely a difference, and the rate item is checked
to have equal denominators, since otherwise the two changes could not be
compared without dividing.

THE HEDGE IS CHECKED TOO. EK 7.1.A.2 says individuals with more favorable
phenotypes are MORE LIKELY to survive, not certain to. The scan at the bottom
fails if any keyed choice in this module upgrades that into a guarantee, because
the two items that turn on the distinction would be undermined by a third item
elsewhere asserting the stronger claim.

NEGATIVE CONTROL: ``negcontrol_b5_7.py``.
"""
import cg_check as cg
import b7_1

T_FITNESS = b7_1._T_FITNESS
T_PHENO = b7_1._T_PHENO
T_GEN = b7_1._T_GEN
T_RATE = b7_1._T_RATE
T_THREE = b7_1._T_THREE

# Wordings that would turn EK 7.1.A.2's "more likely" into a guarantee.
OVERCLAIMS = ("certain to survive", "always survives", "guaranteed to survive",
              "will always reproduce", "must survive")


def _rows(table):
    heads = [cg.normalize(h) for h in table["headers"]]
    return [dict(zip(heads, r)) for r in table["rows"]]


def _fitness_rows(table):
    life = "lifespan in years"
    kids = "number of offspring that survived to reproduce"
    d = {cg.normalize(r["individual"]): (cg.num(r[life]), cg.num(r[kids])) for r in _rows(table)}
    assert len(d) >= 4, "the comparison needs at least four individuals"
    return d


def q6(table, item):
    d = _fitness_rows(table)
    most_kids = max(d, key=lambda k: d[k][1])
    longest = max(d, key=lambda k: d[k][0])
    assert most_kids != longest, (
        "the individual with the most offspring must not also be the longest-lived, or the item "
        "cannot distinguish reproductive success from lifespan and both keys are defensible"
    )
    assert d[most_kids][1] == 11, f"the highest offspring count is {d[most_kids][1]}"
    assert len({v[1] for v in d.values()}) == len(d), "two individuals must not tie on offspring"
    return (f"{most_kids} leaves the most offspring at {d[most_kids][1]:.0f} while {longest} lives "
            f"longest at {d[longest][0]:.0f} years, so the two measures point to different individuals")


def q7(table, item):
    d = _fitness_rows(table)
    longest = max(d, key=lambda k: d[k][0])
    fewest = min(d, key=lambda k: d[k][1])
    assert longest == fewest, (
        f"the key says the longest-lived individual left the fewest offspring, but they are "
        f"{longest} and {fewest}"
    )
    return (f"{longest} lives longest at {d[longest][0]:.0f} years and leaves the fewest offspring "
            f"at {d[longest][1]:.0f}, so lifespan and reproductive success come apart here")


def q10(table, item):
    rows = _rows(table)
    series = [(cg.normalize(r["conditions during that generation"]),
               cg.num(r["percent of the population showing the dark form"])) for r in rows]
    conds = [c for c, _ in series]
    assert len(set(conds)) == 2, f"the record must show exactly two sets of conditions; got {set(conds)}"
    first = conds[0]
    switch = conds.index(next(c for c in conds if c != first))
    early = [v for c, v in series[:switch]]
    late = [v for c, v in series[switch:]]
    assert len(early) >= 2 and len(late) >= 2, "each stretch needs at least two generations"
    assert early[-1] > early[0], f"the dark form must rise under the first conditions; got {early}"
    assert late[-1] < late[0], f"the dark form must fall under the second conditions; got {late}"
    assert all(0 <= v <= 100 for _, v in series), "a percentage outside 0 to 100 is not data"
    return (f"under {first!r} the dark form goes {early} and afterwards it goes {late}, so the "
            f"direction reverses exactly where the conditions change")


def q13(table, item):
    cool = "mean number of surviving offspring in the cool years"
    warm = "mean number of surviving offspring in the warm years"
    d = {cg.normalize(r["phenotype"]): (cg.num(r[cool]), cg.num(r[warm])) for r in _rows(table)}
    assert len(d) == 2, "a reversal needs exactly two phenotypes"
    (a, va), (b, vb) = d.items()
    assert (va[0] > vb[0]) != (va[1] > vb[1]), \
        f"the advantage must change hands between the two conditions; got {d}"
    assert min(abs(va[0] - vb[0]), abs(va[1] - vb[1])) > 1, \
        "each difference must be large enough to call an advantage"
    return (f"in the cool years {a} leads {va[0]} to {vb[0]} and in the warm years {b} leads "
            f"{vb[1]} to {va[1]}, so the advantage changes hands")


def q18(table, item):
    gens = "number of generations in the period"
    change = "change in the percent of the population showing the trait"
    d = {cg.normalize(r["period"]): (cg.num(r[gens]), cg.num(r[change])) for r in _rows(table)}
    assert len(d) == 2, "the comparison needs exactly two periods"
    (a, va), (b, vb) = d.items()
    assert va[0] == vb[0], \
        f"the two periods must cover the same number of generations to be compared directly; got {d}"
    rates = {k: v[1] / v[0] for k, v in d.items()}
    faster = max(rates, key=rates.get)
    assert faster == "period 2", f"the faster period recomputes to {faster}"
    assert rates[faster] > 3 * min(rates.values()), "the difference must be large enough to call"
    return (f"both periods cover {va[0]:.0f} generations, so the changes {va[1]:.0f} and {vb[1]:.0f} "
            f"give rates {rates}, and the second is {rates[faster] / min(rates.values()):.0f} times the first")


def q19(table, item):
    surv = "percent of individuals surviving to adulthood"
    kids = "mean number of offspring per surviving adult"
    d = {cg.normalize(r["phenotype"]): (cg.num(r[surv]), cg.num(r[kids])) for r in _rows(table)}
    expected = {k: (v[0] / 100) * v[1] for k, v in d.items()}
    best = max(expected, key=expected.get)
    assert best == "phenotype b", f"the highest expected offspring belongs to {best}"
    worst_survival = min(d, key=lambda k: d[k][0])
    assert worst_survival == best, (
        "the key rests on the LOWEST-surviving phenotype coming out highest; if the best survivor "
        "also had the most offspring the item would not need the multiplication"
    )
    assert len(set(expected.values())) == len(expected), "two phenotypes must not tie"
    return (f"survival times offspring per survivor gives {({k: round(v, 2) for k, v in expected.items()})}; "
            f"the phenotype with the lowest survival, {best}, has the highest expected offspring")


CLAIMS = [
 ("major mechanism of evolution",
  "EK 7.1.A.1 states that natural selection is a major mechanism of evolution. The framework's word is major rather than only, and EK 7.4.A.1 adds that evolution is also driven by random occurrences."),
 ("Differential survival among the individuals of a population",
  "EK 7.1.A.2 states that competition for limited resources results in differential survival. Nothing in the statement has competition create the phenotypes it acts on."),
 ("more likely to survive and produce more offspring",
  "EK 7.1.A.2 states that individuals with more favorable phenotypes are MORE LIKELY to survive and produce more offspring. The claim is about likelihood, which is the hedge this module preserves throughout."),
 ("passed on to subsequent generations",
  "EK 7.1.A.2 ends by stating that individuals with more favorable phenotypes thus pass on those favorable traits to subsequent generations. Traits are transmitted rather than acquired during a lifetime."),
 ("By reproductive success",
  "EK 7.1.B.1 states that evolutionary fitness is measured by reproductive success. Longevity, size and resource use may correlate with it but none is what the framework names as the measure."),
 ("left 11 surviving offspring",
  "EK 7.1.B.1 makes reproductive success the measure of fitness. The table check confirms the highest offspring count and the longest lifespan belong to different individuals, which is what makes the choice between the two measures a real one, and that no two individuals tie."),
 ("longest-lived individual left the fewest surviving offspring",
  "EK 7.1.B.1. The table check confirms that the longest-lived individual is also the one with the fewest offspring, so the two measures come apart in this population; the key claims nothing about populations in general."),
 ("The rate and the direction of evolution",
  "EK 7.1.B.2 states that biotic and abiotic environments can fluctuate, affecting the rate and direction of evolution. Both are named."),
 ("Different genetic variations can be selected in each generation",
  "EK 7.1.B.2 states this. The environment determines which existing variation is favoured rather than creating variations, which under EK 6.7.B.1.ii arise from mutation."),
 ("rose while the conditions were cool and wet and fell once they became warm and dry",
  "EK 7.1.B.2 states that fluctuating environments affect the direction of evolution and that different variations can be selected in each generation. The table check locates where the conditions change and confirms the trait rises before that point and falls after it."),
 ("resources cannot support every individual",
  "EK 7.1.A.2 states that competition for limited resources results in differential survival, so the limitation is what makes competition possible. The statement does not have limitation create phenotypes."),
 ("statement about probability rather than a guarantee",
  "EK 7.1.A.2 states that individuals with more favorable phenotypes are MORE LIKELY to survive and produce more offspring. The scan at the foot of this file confirms no keyed choice anywhere in the module upgrades that hedge."),
 ("reverses between the two kinds of year",
  "EK 7.1.B.2 states that fluctuating environments affect the rate and direction of evolution and that different variations can be selected in each generation. The table check confirms the advantage genuinely changes hands rather than merely differing in size."),
 ("do not all survive at the same rate",
  "EK 7.1.A.2 pairs differential survival with individuals of more favourable phenotypes being more likely to survive, so the differences concerned are among the individuals of a population."),
 ("abiotic environments can fluctuate",
  "EK 7.1.B.2 states that biotic and abiotic environments can fluctuate, affecting the rate and direction of evolution. Temperature is a non-living feature of the environment."),
 ("biotic environments can fluctuate",
  "EK 7.1.B.2, with a predator as the living part of the environment. EK 7.1.B.1 makes reproductive success rather than escape the measure of fitness."),
 ("how fast the composition of a population changes, and the direction is which variation",
  "EK 7.1.B.2 names both the rate and the direction as things a fluctuating environment affects, so the framework treats them as distinct quantities."),
 ("changed far faster during the second period",
  "EK 7.1.B.2 states that fluctuating environments affect the rate of evolution. The table check confirms both periods cover the same number of generations, which is what allows the two changes to be compared without dividing, and recomputes the ratio between the rates."),
 ("lower survival is more than offset by its much higher offspring number",
  "EK 7.1.B.1 makes reproductive success the measure of fitness. The table check multiplies survival by offspring per survivor for each phenotype and confirms that the phenotype with the LOWEST survival comes out highest, which is what makes the multiplication necessary."),
 ("Zero, because evolutionary fitness is measured by reproductive success",
  "EK 7.1.B.1 states that evolutionary fitness is measured by reproductive success, and EK 7.1.A.2 makes passing traits to subsequent generations the point of surviving and reproducing."),
 ("environment determines which phenotype leaves more offspring, and environments fluctuate",
  "EK 7.1.A.2 speaks of more favorable phenotypes and EK 7.1.B.2 has fluctuating environments change which variation is selected, so favourable is relative to a set of conditions rather than absolute."),
 ("reduction in offspring counts against the trait",
  "EK 7.1.B.1 measures fitness by reproductive success. Survival matters to EK 7.1.A.2 because it leads to producing more offspring, so a trait raising survival while lowering offspring number is judged on the offspring."),
 ("reproductive success of individuals of each phenotype",
  "EK 7.1.B.1 states that evolutionary fitness is measured by reproductive success, so that is what the comparison requires; the other measures are not what the framework names."),
 ("may have been produced by another mechanism as well",
  "EK 7.1.A.1 calls natural selection a major mechanism of evolution and EK 7.4.A.1 states that evolution is also driven by random occurrences, so an observed change does not by itself identify its mechanism."),
 ("conditions fluctuate more, because different genetic variations can be selected in each generation",
  "EK 7.1.B.2 states that fluctuating environments affect the rate and direction of evolution and that different genetic variations can be selected in each generation, so more fluctuation gives more occasions for the favoured variation to change."),
 ("would not be producing differential survival",
  "EK 7.1.A.2 makes competition for LIMITED resources the thing that results in differential survival, so the limitation is part of the causal claim rather than incidental to it."),
 ("what it experiences is the competition that determines whether it does",
  "EK 7.1.A.2 has individuals pass on the favorable traits they carry, and EK 5.3.A.2.iii makes the set of alleles what is inherited. Competition for limited resources is the circumstance deciding which individuals reproduce and is not itself transmitted."),
 ("without yet identifying which mechanism produced the change",
  "EK 7.1.A.1 makes selection a major rather than the only mechanism and EK 7.4.A.1 adds random occurrences, so a change in composition is consistent with more than one mechanism."),
 ("Resources are limited, so individuals compete",
  "The chain is EK 7.1.A.2 taken in order: competition for limited resources gives differential survival, more favourable phenotypes are more likely to survive and produce more offspring, and those traits pass to subsequent generations."),
 ("environments can fluctuate and affect the direction of evolution, and that different genetic variations can be selected",
  "Both halves are EK 7.1.B.2's own clauses, and the second is what makes explicit that the favoured variation can change from one generation to the next."),
]

cg.check(b7_1, CLAIMS, table_checks={6: q6, 7: q7, 10: q10, 13: q13, 18: q18, 19: q19})

# EK 7.1.A.2's hedge, enforced over every keyed choice in the module.
for i, q in enumerate(b7_1.QUESTIONS, 1):
    keyed = q["choices"][q["ans"]]
    for phrase in OVERCLAIMS:
        assert not cg.contains_phrase(keyed, phrase), (
            f"7.1 q{i}: the keyed choice says {phrase!r}, but EK 7.1.A.2 says individuals with more "
            f"favorable phenotypes are MORE LIKELY to survive, not certain to"
        )
for phrase in OVERCLAIMS:
    assert cg.contains_phrase(f"an individual {phrase} in this account", phrase), \
        f"the hedge scan cannot detect {phrase!r} even in a string containing it"
print(f"    Fitness measure separated from lifespan in the data; EK 7.1.A.2's hedge enforced "
      f"across all 30 keyed choices.")
