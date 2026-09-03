"""Key audit for AP BIOLOGY 5.2 Meiosis and Genetic Diversity.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the keyed choice and in no distractor, so the key
survives the shuffle ``export_units.py`` applies on export.

WHAT THE KEYS REST ON
---------------------
The topic has three essential knowledge statements and every key here is one of
them:

  5.2.A.1  CORRECT SEPARATION of homologous chromosomes in meiosis I and sister
           chromatids in meiosis II gives each gamete a HAPLOID (1n) set that
           comprises an ASSORTMENT OF BOTH MATERNAL AND PATERNAL chromosomes;
           when INCORRECT separation occurs (NONDISJUNCTION), gametes are NO
           LONGER HAPLOID
  5.2.A.2  during PROPHASE I, NON-SISTER CHROMATIDS EXCHANGE GENETIC MATERIAL
           by CROSSING OVER (RECOMBINATION), which INCREASES GENETIC DIVERSITY
           among the resultant gametes
  5.2.A.3  SEXUAL REPRODUCTION increases genetic variation, including CROSSING
           OVER, RANDOM ASSORTMENT during meiosis, and subsequent
           FERTILIZATION of gametes

THE THREE-WAY DISTINCTION IS WHAT THE MODULE TESTS, because the three are
routinely conflated: crossing over changes what a SINGLE CHROMOSOME carries,
random assortment changes WHICH WHOLE CHROMOSOMES a gamete gets, and
nondisjunction changes HOW MANY it gets. Items 22, 24, 25 and 28 turn on
telling them apart, and each offers the other two as distractors.

EXCLUSION STATEMENT OBSERVED. The CED puts the details of sexual reproduction
cycles in various plants and animals beyond the scope of the exam, so no item
asks about any particular organism's life cycle.

BOUNDARY WITH 5.1 AND 5.3. The phases of meiosis belong to topic 5.1; items 3,
9 and 21 cite EK 5.1.A.2.i or EK 5.1.A.2.iii for the phase they name and say
so. Topic 5.3 is not this agent's, and no item here asks for a Punnett square,
a genotype ratio or a map distance -- the recombination table asks only whether
gametes with a new combination appeared, which is what EK 5.2.A.2 asserts
crossing over produces.

Items 11 to 15 carry tables. Every number is HYPOTHETICAL and the stem says so;
each keyed conclusion is recomputed below from the table alone, and the
distractors are shown false against the same numbers. No stem refers to a
figure.

FIVE choices per item (A-E), per SCIENCE_BRIEF.md.
"""
import cg_check as cg
import b5_2

GAMETES = b5_2._T_GAMETES
RECOMBINANT = b5_2._T_RECOMBINANT
ASSORTMENT = b5_2._T_ASSORTMENT
SOURCES = b5_2._T_SOURCES

H_HAPLOID = "Gametes with the haploid number of chromosomes"
H_ANEU = "Gametes with more or fewer chromosomes than the haploid number"
H_PARENTAL = "Gametes carrying a parental combination of the two markers"
H_NEW = "Gametes carrying a combination found in neither parental chromosome"
H_PAIRS = "Homologous pairs in the organism (hypothetical model)"
H_COMBOS = "Different chromosome combinations a gamete could receive from assortment alone"
H_TYPES = "Genetically different offspring types the model produces"


def q11(table, item):
    labs = cg.labels(table)
    hap = dict(zip(labs, cg.col(table, H_HAPLOID)))
    aneu = dict(zip(labs, cg.col(table, H_ANEU)))
    correct = [k for k in labs if "incorrect" not in k.lower()]
    wrong = [k for k in labs if "incorrect" in k.lower()]
    assert len(correct) == 1 and len(wrong) == 1, f"one correct and one incorrect meiosis; got {labs}"
    c, w = correct[0], wrong[0]
    totals = {k: hap[k] + aneu[k] for k in labs}
    assert len(set(totals.values())) == 1, f"both meioses must score the same number of gametes: {totals}"
    assert aneu[c] == 0, "correct separation must produce no gamete off the haploid number"
    assert aneu[w] > 0, "incorrect separation must produce gametes off the haploid number"
    assert hap[c] > hap[w], "'both produced the same proportion of haploid gametes' must be false"
    assert hap[w] > 0, "'neither produced any haploid gamete' must be false"
    return (f"of {totals[c]:.0f} gametes scored each time, correct separation gives {aneu[c]:.0f} off "
            f"the haploid number and incorrect separation gives {aneu[w]:.0f}")


def q12(table, item):
    labs = cg.labels(table)
    par = dict(zip(labs, cg.col(table, H_PARENTAL)))
    new = dict(zip(labs, cg.col(table, H_NEW)))
    totals = {k: par[k] + new[k] for k in labs}
    assert len(set(totals.values())) == 1, f"each pair must be scored over the same sample: {totals}"
    for k in labs:
        assert new[k] > 0, f"{k}: gametes with a new combination must actually appear"
        assert par[k] > new[k], f"{k}: the parental types must remain the majority"
    assert len(set(new.values())) == len(labs), "the two pairs must differ in how often the new type appears"
    return (f"out of {totals[labs[0]]:.0f} gametes scored per pair, new combinations appear "
            f"{[new[k] for k in labs]} times, so an exchange occurred in both pairs at different frequencies")


def q13(table, item):
    pairs = cg.col(table, H_PAIRS)
    combos = cg.col(table, H_COMBOS)
    assert all(b == a + 1 for a, b in zip(pairs, pairs[1:])), f"the pair counts must step by one: {pairs}"
    assert all(b == 2 * a for a, b in zip(combos, combos[1:])), \
        f"each added pair must double the combinations: {combos}"
    assert combos[0] == 2 ** pairs[0], f"the model must start consistently: {combos[0]} for {pairs[0]} pair"
    assert len(set(combos)) == len(combos), "'the same for every organism modeled' must be false"
    assert all(c > 0 for c in combos), "'falls to zero' must be false"
    return (f"combinations run {combos} for {pairs} homologous pairs, doubling at each step, which is "
            f"two raised to the number of pairs")


def _sources(table):
    labs = cg.labels(table)
    types = dict(zip(labs, cg.col(table, H_TYPES)))
    base = [k for k in labs if "nothing" in k.lower()]
    assert len(base) == 1, f"exactly one row must switch nothing off; got {labs}"
    b = base[0]
    removed = [k for k in labs if k != b]
    assert len(removed) == 3, f"three contributors must be removed in turn; got {removed}"
    return b, removed, types


def q14(table, item):
    b, removed, types = _sources(table)
    for k in removed:
        assert types[k] < types[b], f"{k}: switching a contributor off must lower the variety"
    assert types[b] == max(types.values()), "the untouched model must produce the most variety"
    assert len(set(types[k] for k in removed)) == len(removed), \
        "'the three contribute equally' must be false"
    return (f"the untouched model produces {types[b]:.0f} offspring types and the three removals leave "
            f"{[types[k] for k in removed]}, so every removal costs the model variety")


def q15(table, item):
    b, removed, types = _sources(table)
    worst = min(removed, key=lambda k: types[k])
    assert list(types[k] for k in removed).count(types[worst]) == 1, \
        "the most costly removal must be unique"
    assert types[worst] < types[b], "the most costly removal must still be below the untouched model"
    assert types[worst] != max(types[k] for k in removed), \
        "'the removal leaving the most types' must name a different row"
    assert all(types[k] != types[b] for k in removed), \
        "'the removal leaving the number unchanged' must be false"
    return (f"{worst} leaves only {types[worst]:.0f} offspring types against {types[b]:.0f} with "
            f"nothing switched off, the largest loss of the three")


CLAIMS = [
 ("assortment of maternal and paternal chromosomes",
  "EK 5.2.A.1 states that correct separation of homologous chromosomes in meiosis I and sister chromatids in meiosis II ensures each gamete receives a haploid set comprising an assortment of both maternal and paternal chromosomes."),
 ("Nondisjunction, which produces gametes that are no longer haploid",
  "EK 5.2.A.1 states that when incorrect separation occurs, nondisjunction, gametes are no longer haploid. Crossing over and fertilization are named elsewhere for entirely different processes."),
 ("During prophase I, between non-sister chromatids",
  "EK 5.2.A.2 states that during prophase I of meiosis, non-sister chromatids exchange genetic material via crossing over. EK 5.1.A.2.i places synapsis and the possible formation of chiasmata in the same phase."),
 ("increases genetic diversity among the resultant gametes",
  "EK 5.2.A.2 states that crossing over, also called recombination, increases genetic diversity among the resultant gametes."),
 ("random assortment of chromosomes during meiosis, and fertilization of gametes",
  "EK 5.2.A.3 states that sexual reproduction in eukaryotes increases genetic variation, including crossing over, random assortment of chromosomes during meiosis, and subsequent fertilization of gametes."),
 ("independent of the others, so many combinations are possible",
  "EK 5.2.A.3 names random assortment of chromosomes during meiosis among the contributors to variation, and EK 5.2.A.1 describes the resulting haploid set as an assortment of both maternal and paternal chromosomes."),
 ("combines two separately produced gametes",
  "EK 5.2.A.3 names subsequent fertilization of gametes among the ways sexual reproduction in eukaryotes increases genetic variation, alongside crossing over and random assortment."),
 ("Recombination",
  "EK 5.2.A.2 states that non-sister chromatids exchange genetic material via a process called crossing over, giving recombination in parentheses as the alternative name."),
 ("Homologous chromosomes at the first division and sister chromatids at the second",
  "EK 5.2.A.1 speaks of correct separation of the homologous chromosomes in meiosis I and sister chromatids in meiosis II, which EK 5.1.A.2.iii and EK 5.1.A.3.iii state as the events of the two anaphases."),
 ("An assortment of both maternal and paternal chromosomes",
  "EK 5.2.A.1 states that each gamete receives a haploid set of chromosomes that comprises an assortment of both maternal and paternal chromosomes."),
 ("Incorrect separation produced gametes that are no longer haploid",
  "Recomputed in q11 above. EK 5.2.A.1 states that when incorrect separation occurs, nondisjunction, gametes are no longer haploid, and the two rows of the table differ in exactly that respect."),
 ("exchanged between non-sister chromatids during meiosis",
  "Recomputed in q12 above. EK 5.2.A.2 states that non-sister chromatids exchange genetic material via crossing over, and a combination present in neither parental chromosome is what that exchange produces."),
 ("doubles with each additional homologous pair",
  "Recomputed in q13 above. EK 5.2.A.3 names random assortment of chromosomes during meiosis among the contributors to variation, and skill 4.B asks students to describe the relationship between the two columns."),
 ("Each of the three features contributes",
  "Recomputed in q14 above. EK 5.2.A.3 names crossing over, random assortment and fertilization together as ways sexual reproduction increases genetic variation, and every removal in the table lowers the count."),
 ("leaves the fewest genetically different offspring types",
  "Recomputed in q15 above. Skill 4.B asks students to identify specific data points and compare them, and the lowest remaining count marks the removal that cost the model the most variety."),
 ("no longer haploid, because separation was incorrect",
  "EK 5.2.A.1 makes correct separation of homologous chromosomes in meiosis I part of what ensures a haploid set, and states that when incorrect separation occurs, nondisjunction, gametes are no longer haploid."),
 ("lower than it would otherwise be",
  "EK 5.2.A.2 states that crossing over increases genetic diversity among the resultant gametes, so preventing the exchange removes one contribution to that diversity while leaving separation, and therefore ploidy, intact."),
 ("Fertilization of gametes",
  "EK 5.2.A.3 names crossing over, random assortment and subsequent fertilization of gametes as the contributors to variation. Only the last requires two gametes to come together."),
 ("fewer new marker combinations",
  "Skill 3.A asks students to identify or pose a testable question. Only the keyed question can be settled by counting gametes, and it tests EK 5.2.A.2's claim that crossing over increases diversity among the resultant gametes."),
 ("different combinations of whole chromosomes appear among a large sample",
  "Skill 3.A asks for a testable question aligned to the claim. EK 5.2.A.3 makes random assortment a source of variation in which whole chromosomes a gamete receives, so the question must be about how many such combinations appear."),
 ("belong to different members of a homologous pair",
  "EK 5.2.A.2 names non-sister chromatids specifically, and EK 5.1.A.2.i has homologous chromosomes pair up in prophase I, which is what places chromatids of two different chromosomes alongside one another. EK 5.1.A.2.iii keeps sister chromatids attached until the second division."),
 ("Crossing over between non-sister chromatids during prophase I",
  "EK 5.2.A.2 states that non-sister chromatids exchange genetic material via crossing over, increasing genetic diversity among the resultant gametes. Assortment moves whole chromosomes and would not create a new combination within one chromosome."),
 ("species with more pairs can produce more different combinations",
  "EK 5.2.A.3 names random assortment of chromosomes during meiosis as a source of variation and EK 5.2.A.1 makes each haploid set an assortment of maternal and paternal chromosomes, so more independently assorting pairs allow more distinct assortments."),
 ("Incorrect separation during meiosis, which the framework calls nondisjunction",
  "EK 5.2.A.1 states that when incorrect separation occurs, nondisjunction, gametes are no longer haploid. Crossing over and assortment change combinations without changing how many chromosomes a gamete receives."),
 ("marker combinations on one chromosome that neither parental chromosome carried",
  "EK 5.2.A.2 states that non-sister chromatids exchange genetic material via crossing over, which increases genetic diversity among the resultant gametes. A new combination within a single chromosome is the observable signature of that exchange."),
 ("settled independently for each pair",
  "EK 5.2.A.1 says each gamete receives a haploid set comprising an assortment of both maternal and paternal chromosomes, and EK 5.2.A.3 names random assortment of chromosomes during meiosis among the contributors to variation."),
 ("Mitosis of body cells during growth and tissue repair",
  "EK 5.2.A.3 names crossing over, random assortment and fertilization. EK 4.5.B.1 makes mitosis a process producing two genetically IDENTICAL daughter cells, which is the opposite of a source of variation."),
 ("Crossing over creates new combinations within a chromosome",
  "EK 5.2.A.2 has non-sister chromatids EXCHANGE GENETIC MATERIAL, which alters what one chromosome carries, while EK 5.2.A.3's random assortment concerns which whole chromosomes a gamete receives."),
 ("more reliably haploid than normal separation does",
  "EK 5.2.A.1 states that when incorrect separation occurs, nondisjunction, gametes are NO LONGER HAPLOID. The other four options restate EK 5.2.A.2, EK 5.2.A.1 and EK 5.2.A.3 directly."),
 ("independent assortment of chromosomes, and the fusion of two separately produced gametes",
  "EK 5.2.A.3 names crossing over, random assortment of chromosomes during meiosis and subsequent fertilization of gametes, and EK 5.2.A.2 supplies the mechanism of the first of the three."),
]

cg.check(b5_2, CLAIMS, table_checks={11: q11, 12: q12, 13: q13, 14: q14, 15: q15})
