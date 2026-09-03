"""Key audit for AP BIOLOGY 7.11 Variations in Populations.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor, so an off-by-one key stops matching; the
claim states what the key rests on, for a human to audit.

WHAT THE KEYS REST ON
---------------------
Every non-data item is keyed to one of the three parts of EK 7.11.A.1: that the
level of variation in a population affects population dynamics; that the ability
to respond to environmental change is influenced by genetic diversity and that
populations with little of it are at risk of decline or extinction; that
diverse populations are MORE LIKELY to contain individuals that can withstand a
pressure; and that an allele adaptive in one environmental condition may be
deleterious in another because of different selective pressures.

THE HEDGE. EK 7.11.A.1 says MORE LIKELY, not certain. Three items turn on that
word, and no key anywhere in this module upgrades the tendency into a guarantee
or into a prediction that a low-diversity population must decline.

Items 14 to 20 carry a table and every number or comparison their keys state is
RECOMPUTED below from that table alone, through cg_check's header-and-label
accessors. Where the stem names a row, the check locates it by parsing the stem
rather than by trusting a row index.

None of this says whether the biology is right; that is gated by the CLAIMS
text and by the rule in SCIENCE_BRIEF.md that a key must trace to a CED
sentence.

NEGATIVE CONTROL. Moving any key, or changing any table cell the keys depend
on, makes this file raise; confirmed by running exactly that.
"""
import re

import cg_check as cg
import b7_11

QS = b7_11.QUESTIONS
T_DIVERSITY = b7_11._T_DIVERSITY
T_ALLELE = b7_11._T_ALLELE

ALLELES = "Number of distinct alleles detected across ten loci"
SURVIVED = "Percentage of individuals surviving the outbreak"
WITH_T = "Percentage of individuals carrying allele T that survived"
WITHOUT_T = "Percentage of individuals lacking allele T that survived"


def keyed(item):
    return item["choices"][item["ans"]]


def _pops_numbered(table):
    nums = [cg.num(lab) for lab in cg.labels(table)]
    assert nums == list(range(1, len(nums) + 1)), \
        f"population labels are {cg.labels(table)}; they must be numbered from one in row order"


def q14(table, item):
    _pops_numbered(table)
    pairs = sorted(zip(cg.col(table, ALLELES), cg.col(table, SURVIVED)))
    surv = [s for _, s in pairs]
    assert all(b > a for a, b in zip(surv, surv[1:])), \
        f"the key says survival rises with allele number; sorted survival is {surv}"
    return f"sorting the four populations by allele number gives survival {surv}, rising at every step"


def q15(table, item):
    _pops_numbered(table)
    alleles = {lab: cg.cell(table, lab, ALLELES) for lab in cg.labels(table)}
    fewest = min(alleles, key=alleles.get)
    assert sorted(alleles.values())[1] > alleles[fewest], \
        f"the least diverse population must be unique; allele counts are {alleles}"
    surv = {lab: cg.cell(table, lab, SURVIVED) for lab in cg.labels(table)}
    assert min(surv, key=surv.get) == fewest, \
        "the key also notes that the least diverse population survived worst; the table disagrees"
    assert cg.contains_phrase(keyed(item), fewest), \
        f"q15 key {keyed(item)!r} but the least diverse population is {fewest}"
    return f"allele counts {alleles} put {fewest} lowest, and it also records the lowest survival"


def q16(table, item):
    _pops_numbered(table)
    alleles = {lab: cg.cell(table, lab, ALLELES) for lab in cg.labels(table)}
    most, fewest = max(alleles, key=alleles.get), min(alleles, key=alleles.get)
    gap = cg.cell(table, most, SURVIVED) - cg.cell(table, fewest, SURVIVED)
    assert keyed(item) == f"{int(gap)} percentage points", \
        f"q16 key {keyed(item)!r} but the survival gap is {gap}"
    return (f"{most} carries the most alleles and {fewest} the fewest, and their survival "
            f"percentages differ by {int(gap)}")


def q17(table, item):
    _pops_numbered(table)
    pairs = sorted(zip(cg.col(table, ALLELES), cg.col(table, SURVIVED)))
    surv = [s for _, s in pairs]
    assert all(b > a for a, b in zip(surv, surv[1:])), \
        f"the key says survival rose with allele number across all four; sorted survival is {surv}"
    assert len(cg.labels(table)) == 4, "the key says all four populations"
    lowest_alleles = min(cg.col(table, ALLELES))
    lowest_surv_row = min(cg.labels(table), key=lambda l: cg.cell(table, l, SURVIVED))
    assert cg.cell(table, lowest_surv_row, ALLELES) == lowest_alleles, \
        "a distractor claims the least diverse population survived best; the table must refute it"
    return (f"survival {surv} rises with allele number across all {len(cg.labels(table))} "
            f"populations, and the least diverse population records the lowest survival")


def named_condition(table, item):
    hits = [lab for lab in cg.labels(table) if cg.contains_phrase(item["q"], lab)]
    assert len(hits) == 1, f"the stem names conditions {hits}; it must name exactly one"
    return hits[0]


def q18(table, item):
    better = [lab for lab in cg.labels(table)
              if cg.cell(table, lab, WITH_T) > cg.cell(table, lab, WITHOUT_T)]
    assert len(better) == 1, f"exactly one condition must favour the allele; {better} do"
    assert cg.contains_phrase(keyed(item), better[0]), \
        f"q18 key {keyed(item)!r} but the allele is favoured in {better[0]}"
    return f"carrying the allele raises survival only in {better[0]}"


def q19(table, item):
    lab = named_condition(table, item)
    gap = cg.cell(table, lab, WITHOUT_T) - cg.cell(table, lab, WITH_T)
    assert gap > 0, f"the stem says survival falls below; in {lab} the gap is {gap}"
    assert keyed(item) == f"{int(gap)} percentage points", \
        f"q19 key {keyed(item)!r} but the gap in {lab} is {gap}"
    return f"in {lab} survival runs {int(cg.cell(table, lab, WITH_T))} against {int(cg.cell(table, lab, WITHOUT_T))}, a gap of {int(gap)}"


def q20(table, item):
    signs = {lab: cg.cell(table, lab, WITH_T) - cg.cell(table, lab, WITHOUT_T)
             for lab in cg.labels(table)}
    assert any(v > 0 for v in signs.values()) and any(v < 0 for v in signs.values()), \
        f"the key requires the allele's effect to reverse between conditions; differences are {signs}"
    return f"the allele's survival advantage is {signs}, positive in one condition and negative in the other"


TABLE_CHECKS = {14: q14, 15: q15, 16: q16, 17: q17, 18: q18, 19: q19, 20: q20}


CLAIMS = [
 ("Population dynamics",
  "EK 7.11.A.1 states that the level of variation in a population affects population dynamics. The number of loci, the mutation rate and the mode of reproduction are not what the statement connects to the level of variation."),
 ("Its genetic diversity",
  "EK 7.11.A.1 states that the ability of a population to respond to changes in the environment is influenced by genetic diversity. Range, community composition and habitat type appear nowhere in that statement."),
 ("decline or extinction",
  "EK 7.11.A.1 states that species and populations with little genetic diversity are at risk of decline or extinction. No other outcome is attached to low diversity anywhere in the topic."),
 ("more likely to contain individuals that can withstand",
  "EK 7.11.A.1 gives that reason verbatim for the resilience of genetically diverse populations. Diversity concerns the variety of alleles present rather than the number of individuals, which is a separate property."),
 ("selective pressures differ between the two conditions",
  "EK 7.11.A.1 states that alleles adaptive in one environmental condition may be deleterious in another because of different selective pressures. The allele's sequence is unchanged; what changes is what the environment favours."),
 ("harms one plant is likely to harm nearly all of them",
  "EK 7.11.A.1 states that populations with little genetic diversity are at risk of decline or extinction, and that diverse populations are more resilient because they are more likely to contain individuals that can withstand the pressure. Near-identical plants supply few such individuals."),
 ("ability to respond to future environmental change is reduced",
  "EK 7.11.A.1 makes the ability to respond to environmental change depend on genetic diversity and attaches a risk of decline or extinction to having little of it. The statement supplies no mechanism that restores lost variation quickly."),
 ("difference in genetic diversity",
  "EK 7.11.A.1 states that genetically diverse populations are more resilient because they are more likely to contain individuals that can withstand the pressure. Individuals left unaffected by an outbreak are exactly such individuals."),
 ("MORE LIKELY to contain individuals that can withstand the pressure, which is a probability",
  "EK 7.11.A.1 uses the words more likely, which states a tendency rather than a certainty. A pressure that no allele present happens to counter would affect every individual however diverse the population is in other respects."),
 ("large and still carry few distinct alleles",
  "EK 7.11.A.1 attaches the risk of decline or extinction to little GENETIC DIVERSITY, not to small numbers. The two properties can come apart, which is why the statement is written about variation rather than about abundance."),
 ("more distinct alleles suffer smaller losses under the same pressure",
  "Skill 6.C asks for reasoning connecting evidence to a claim. The claim relates a difference in diversity to a difference in outcome, so the evidence must vary diversity and compare outcomes; one case, or two equally diverse populations, leaves the relationship untested."),
 ("far greater genetic diversity suffered equally heavy losses",
  "Skill 6.C cuts both ways. EK 7.11.A.1 predicts that greater diversity makes a population more resilient, so a much more diverse population faring just as badly under the same pressure is the observation that prediction most struggles with."),
 ("raises the chance that some individuals can withstand a future pressure",
  "EK 7.11.A.1 makes resilience follow from being more likely to contain individuals that can withstand the pressure, so raising the number of distinct alleles present raises that likelihood. The statement licenses no guarantee and says nothing about mutation rates."),
 ("the larger the percentage of it that survived",
  "Skill 4.B asks for the relationship between the variables. The table check above sorts the populations by allele number and confirms survival rises at every step, which is the pattern EK 7.11.A.1 predicts."),
 ("Population 1",
  "EK 7.11.A.1 states that populations with little genetic diversity are at risk of decline or extinction. The table check above confirms one population carries the fewest distinct alleles by a clear margin and that the same population records the lowest survival."),
 ("53 percentage points",
  "Skill 5.A includes percentages and percent changes. The table check above identifies the most and least diverse rows by their allele counts and recomputes the difference between their survival percentages."),
 ("rose with the number of distinct alleles across all four populations",
  "Skill 6.C asks for reasoning connecting evidence to a claim. The table check above confirms the co-variation holds across the whole set and, separately, that the least diverse population did NOT survive best, which is what the competing option asserts."),
 ("The cool and wet season",
  "Skill 4.B, identifying and comparing specific data points. The table check above confirms that in exactly one condition the survival of individuals carrying the allele exceeds that of individuals lacking it."),
 ("45 percentage points",
  "Skill 5.A includes percentages. The table check above locates the row the stem names and recomputes the difference between its two survival percentages, confirming the direction the stem states."),
 ("adaptive in one environmental condition may be deleterious in another",
  "EK 7.11.A.1, near verbatim. The table check above confirms the allele's survival advantage is positive in one condition and negative in the other, which is the reversal the statement describes."),
 ("without naming the environmental condition, because its effect reverses",
  "EK 7.11.A.1 makes an allele's adaptive or deleterious character depend on the environmental condition and its selective pressures. An allele whose effect reverses between conditions has no description independent of the condition."),
 ("deleterious now may be the one that allows survival under a different pressure",
  "EK 7.11.A.1 states both that an allele adaptive in one condition may be deleterious in another and that diverse populations are more likely to contain individuals that can withstand a pressure. Variation with no present use is part of the variety the second statement relies on."),
 ("How much genetic diversity each population carries",
  "EK 7.11.A.1 makes the ability to respond to environmental change depend on genetic diversity and makes diverse populations more resilient. The other four properties are connected to resilience by no statement in this topic."),
 ("raised risk of decline should a new pressure arise",
  "EK 7.11.A.1 frames low diversity as a RISK, which is a claim about what happens when a pressure arrives rather than a prediction of decline in every decade. A decade without a new pressure tests the claim in neither direction."),
 ("variety of alleles present among the individuals",
  "EK 7.11.A.1 speaks of the level of variation in a population and of alleles adaptive or deleterious under different conditions, so the variation at issue is variation among alleles. Abundance, community composition and habitat range are separate properties."),
 ("say nothing about a future pressure that no present allele counters",
  "EK 7.11.A.1 ties resilience to the likelihood of containing individuals that can withstand a pressure, and different pressures call on different alleles. A record of surviving particular pressures is evidence about those pressures only."),
 ("nearly every individual is genetically alike",
  "EK 7.11.A.1 makes genetic diversity the property that influences the ability to respond to environmental change. Only one of the listed pairs differs in that property; the rest differ in properties the statement never connects to resilience."),
 ("variation held across a population affects the population's dynamics as a whole",
  "EK 7.11.A.1 states that the LEVEL OF VARIATION IN A POPULATION affects POPULATION DYNAMICS, relating a property of the whole group to an outcome for the whole group. An individual either carries an allele or does not; only a population has a level of variation."),
 ("raises the chance of resistance without assuring it",
  "EK 7.11.A.1 says a diverse population is MORE LIKELY to contain individuals that can withstand the pressure, which leaves room for a pressure none of the alleles present counters. Nothing in the statement supplies alleles on demand."),
 ("low diversity raises the risk of decline, and an allele's value depends on the conditions",
  "The three parts of EK 7.11.A.1 assert exactly those three things. Certainty of extinction and uniform effect across environments are both stronger than anything the statement says."),
]


# SCIENCE_BRIEF.md: Biology is exported untypeset, so a backslash macro or a
# dollar span would reach a student as literal characters, and a
# digit-hyphen-digit run reads as a subtraction. Explicit lookarounds, never \b.
_BANNED = [
    (re.compile(r"\\"), "a backslash: this bank carries no LaTeX"),
    (re.compile(r"\$"), "a dollar-delimited math span"),
    (re.compile(r"(?<![A-Za-z])\d+\s*-\s*\d+(?![A-Za-z])"), "a digit-hyphen-digit range"),
    (re.compile(r"\d\s*/\s*\d"), "a digit-slash-digit fraction"),
]

_FIGURE_TALK = re.compile(
    r"(?<![A-Za-z])(the (?:graph|figure|diagram|chart|curve) (?:shown|above|below)|"
    r"in the (?:graph|figure|diagram|chart|curve) (?:shown|above|below)|"
    r"shown in the (?:graph|figure|diagram|chart|curve))(?![A-Za-z])",
    re.IGNORECASE)


def style():
    hits = 0
    for i, item in enumerate(QS, 1):
        texts = [("stem", item["q"]), ("why", item["why"])]
        texts += [(f"choice {k}", c) for k, c in enumerate(item["choices"])]
        if item.get("table"):
            texts.append(("table", " | ".join(item["table"]["headers"])))
            texts += [("table", " | ".join(str(c) for c in r)) for r in item["table"]["rows"]]
        for where, text in texts:
            for pat, why_bad in _BANNED:
                m = pat.search(text)
                assert not m, f"q{i} {where} contains {m.group(0)!r}, {why_bad}"
                hits += 1
            m = _FIGURE_TALK.search(text)
            assert not m, (
                f"q{i} {where} says {m.group(0)!r}, promising a figure the bank cannot show"
            )
            hits += 1
    return hits


def main():
    n_style = style()
    cg.check(b7_11, CLAIMS, table_checks=TABLE_CHECKS)
    print(f"    {n_style} notation and figure-reference checks clean.")


main()
