# AP BIOLOGY 7.5 Hardy-Weinberg Equilibrium
# CED effective Fall 2025, Unit 7 Natural Selection, Big Idea 1 Evolution.
# Learning objective 7.5.A, describe the conditions under which allele and
# genotype frequencies will change in populations.
# Suggested skills 1.C (explain concepts in applied contexts) and 5.A (perform
# mathematical calculations, including equations in the curriculum, means,
# rates, ratios, percentages and percent changes).
#
# Essential knowledge relied on, in the framework's own terms:
#   7.5.A.1  the Hardy-Weinberg equilibrium is a MODEL for describing and
#            predicting allele frequencies in a NON-EVOLVING population. The
#            conditions for a population or an allele to be in Hardy-Weinberg
#            equilibrium are (i) a large population size, (ii) no migration,
#            (iii) no new mutations, (iv) random mating, (v) no natural
#            selection. "These conditions are never met, but they provide a
#            valuable null hypothesis."
#   7.5.A.2  allele frequencies in a nonevolving population can be calculated
#            from genotype frequencies.
#   Relevant equations printed by the CED for this topic:
#            p squared plus 2pq plus q squared equals 1, and p plus q equals 1,
#            where p is the frequency of allele 1 and q the frequency of
#            allele 2 in the population.
#
# ON THE ARITHMETIC. Every numeric claim in this module is recomputed in
# verify_b7_5.py from the stimulus alone -- from the table for the seven data
# items and from the numbers printed in the stem for the rest. Nothing here
# asks a student to recall a figure, and every calculation is one or two steps
# without a calculator, which is what skill 5.A describes.
#
# DELIBERATE OMISSIONS, to keep off neighbouring topics. Genetic drift, the
# bottleneck effect, the founder effect and gene flow are EK 7.4.A.1 and belong
# to 7.4; this module names a violated CONDITION and stops there. Heterozygote
# advantage is EK 8.7.A.2 and is asked in b8_7. No item here asks whether a
# change in allele frequency is evidence of evolution, which is EK 7.4.C.1.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: this bank is exported
# untypeset, so equations are written out in words.
TOPIC = ("7.5", "Hardy–Weinberg Equilibrium", 7)

_T_COUNTS = dict(
    headers=["Genotype", "Number of individuals"],
    rows=[["FF", "90"],
          ["FS", "60"],
          ["SS", "50"]])

_T_OBS_EXP = dict(
    headers=["Genotype", "Observed number of individuals",
             "Number expected if the population were in Hardy-Weinberg equilibrium"],
    rows=[["MM", "120", "98"],
          ["MN", "40", "84"],
          ["NN", "40", "18"]])

_T_GEN = dict(
    headers=["Generation", "Frequency of allele R", "Frequency of allele W"],
    rows=[["First", "0.80", "0.20"],
          ["Second", "0.72", "0.28"],
          ["Third", "0.65", "0.35"],
          ["Fourth", "0.58", "0.42"]])

_T_FOUR = dict(
    headers=["Population", "Frequency of allele A", "Frequency of allele B",
             "Observed frequency of heterozygotes"],
    rows=[["W", "0.50", "0.50", "0.50"],
          ["X", "0.60", "0.40", "0.48"],
          ["Y", "0.70", "0.30", "0.42"],
          ["Z", "0.90", "0.10", "0.02"]])

QUESTIONS = [
 dict(q="Which of the following is one of the conditions that must hold if a population is to be in Hardy-Weinberg equilibrium at a locus?",
   choices=[
     "No migration of individuals into or out of the population",
     "A high rate of new mutations arising at the locus",
     "Steady selection against the homozygous recessive phenotype",
     "Mating restricted to partners that share the same phenotype",
     "A breeding group of only a few dozen individuals"], ans=0,
   why="EK 7.5.A.1 lists exactly five conditions: a large population size, no migration, no new mutations, random mating and no natural selection. The other four options each name the violation of one of those conditions rather than the condition itself."),

 dict(q="The five conditions of the Hardy-Weinberg model are never all satisfied by a real population. Which of the following best explains why biologists still use the model?",
   choices=[
     "It supplies a null expectation, so a gap between predicted and observed frequencies points to a process acting on the population",
     "It proves that a population is not evolving whenever predicted and observed frequencies differ",
     "It allows allele frequencies to be obtained without collecting any data from the population",
     "It describes how quickly natural selection will change a population",
     "It shows that mutation and migration cancel each other out in most populations"], ans=0,
   why="EK 7.5.A.1 states in as many words that the conditions are never met but that they provide a valuable null hypothesis. A null hypothesis is a prediction of what would be seen if nothing were acting, so a departure from it is the signal."),

 dict(q="At a particular locus a large population mates at random and experiences no migration, no new mutations and no natural selection. Over the next several generations the allele frequencies at that locus are expected to",
   choices=[
     "stay the same from one generation to the next",
     "move steadily toward equal frequencies for the two alleles",
     "move toward loss of whichever allele is less common",
     "rise and fall as heterozygotes are removed from the population",
     "become equal to the genotype frequencies"], ans=0,
   why="The population described meets all five conditions of EK 7.5.A.1, and the model those conditions define is a model of a non-evolving population, in which allele frequencies do not change. Nothing in the model drives frequencies toward equality or toward loss."),

 dict(q="A soil fungus kills nearly every seedling that is homozygous recessive at a locus before it can flower, while seedlings of the other two genotypes are unaffected. Which Hardy-Weinberg condition does this population violate?",
   choices=[
     "No natural selection",
     "No new mutations",
     "Random mating",
     "No migration",
     "A large population size"], ans=0,
   why="EK 7.5.A.1 requires that no natural selection act at the locus. Differential survival of one genotype to reproductive age is natural selection, and none of the other four conditions is disturbed by the scenario as described."),

 dict(q="In a wildflower population, insects visit only flowers whose petal colour matches the colour of the flower they last visited, so plants of like colour are pollinated together far more often than expected. Which Hardy-Weinberg condition is violated?",
   choices=[
     "Random mating",
     "No natural selection",
     "No migration",
     "No new mutations",
     "A large population size"], ans=0,
   why="EK 7.5.A.1 requires random mating. Assortative pollination by petal colour means gametes do not combine at random with respect to the locus, even though survival, population size, migration and mutation are untouched."),

 dict(q="A newly formed pond holds twenty-two breeding frogs, and a chance flood drowns eight of them before the breeding season. Which Hardy-Weinberg condition is most directly violated?",
   choices=[
     "A large population size",
     "No new mutations",
     "No migration",
     "Random mating",
     "No natural selection"], ans=0,
   why="EK 7.5.A.1 requires a large population size, because in a small population chance alone shifts allele frequencies between generations. The flood is indiscriminate, so it is not selection, and no individual entered or left the pond."),

 dict(q="Wind carries pollen from a distant field of the same species into a study plot every spring, and seed set in the plot regularly includes offspring sired by that pollen. Which Hardy-Weinberg condition is violated?",
   choices=[
     "No migration",
     "A large population size",
     "Random mating",
     "No new mutations",
     "No natural selection"], ans=0,
   why="EK 7.5.A.1 requires no migration. Pollen arriving from outside adds alleles to the plot from another population, which is movement of alleles into the population regardless of whether any adult plant moves."),

 dict(q="A laboratory colony of beetles is exposed to a chemical that raises the rate at which new alleles appear at a pigment locus roughly tenfold. Which Hardy-Weinberg condition is violated?",
   choices=[
     "No new mutations",
     "No migration",
     "Random mating",
     "No natural selection",
     "A large population size"], ans=0,
   why="EK 7.5.A.1 requires that no new mutations arise. A raised mutation rate at the locus introduces allele copies that were not present in the parental generation, which is exactly the process the condition excludes."),

 dict(q="The Hardy-Weinberg equilibrium is best described as a model for describing and predicting allele frequencies in",
   choices=[
     "a non-evolving population",
     "a population under strong directional selection",
     "any population whose size is increasing",
     "a species that reproduces asexually",
     "a population that has just been founded by a few individuals"], ans=0,
   why="EK 7.5.A.1 states that the Hardy-Weinberg equilibrium is a model for describing and predicting allele frequencies in a non-evolving population. Selection, founding events and asexual reproduction are all outside what the model represents."),

 dict(q="For a locus with two alleles, the expression p plus q equals 1 rests on which assumption?",
   choices=[
     "Every allele copy at the locus is one of the two alleles being counted",
     "The two alleles are equally common in the population",
     "Every individual in the population is heterozygous",
     "The dominant allele is always the more frequent of the two",
     "Mutation continually replaces missing allele copies"], ans=0,
   why="The CED prints p plus q equals 1 for this topic, with p and q defined as the frequencies of allele 1 and allele 2. Frequencies of a complete set of alternatives sum to one, which requires only that no third allele be present, not that the two be equally common."),

 dict(q="In the Hardy-Weinberg equation, the term 2pq gives the expected frequency of",
   choices=[
     "heterozygous individuals",
     "individuals homozygous for the dominant allele",
     "individuals homozygous for the recessive allele",
     "copies of the recessive allele in the gamete pool",
     "individuals that show the dominant phenotype"], ans=0,
   why="The CED prints p squared plus 2pq plus q squared equals 1 for this topic. A heterozygote can be assembled two ways, one allele from each parent in either order, which is why the middle term carries the factor of two."),

 dict(q="A student writes that the three terms of the Hardy-Weinberg equation sum to one. That sum is best interpreted as the statement that",
   choices=[
     "every individual in the population has one of the three possible genotypes",
     "the two alleles are present in equal numbers",
     "the population contains exactly three phenotypes",
     "half of the allele copies are found in heterozygotes",
     "no allele copy is ever lost from the population"], ans=0,
   why="EK 7.5.A.2 treats genotype frequencies as the quantities from which allele frequencies are calculated. For one locus with two alleles there are three genotypes, so their frequencies exhaust the population and must add to one."),

 dict(q="In a population that is in Hardy-Weinberg equilibrium at a locus with two alleles, 16 percent of individuals show the recessive phenotype. What is the frequency of the recessive allele?",
   choices=["0.40", "0.16", "0.32", "0.60", "0.84"], ans=0,
   why="EK 7.5.A.2 with the equation printed for this topic: the recessive phenotype appears only in homozygous recessive individuals, so q squared is 0.16 and q is its square root, 0.40. The other values are the genotype frequency itself, the heterozygote frequency and the two dominant-allele quantities."),

 dict(q="At a locus with two alleles, 16 percent of a population in Hardy-Weinberg equilibrium is homozygous recessive. What proportion of the population is expected to be homozygous dominant?",
   choices=["0.36", "0.48", "0.60", "0.84", "0.16"], ans=0,
   why="From EK 7.5.A.2 and the printed equation, q squared is 0.16 so q is 0.40 and p is 0.60. The homozygous dominant frequency is p squared, which is 0.36. The distractors are the heterozygote frequency, p itself, the whole dominant phenotype and the recessive genotype."),

 dict(q="A population in Hardy-Weinberg equilibrium has a recessive phenotype in 25 percent of its members. What proportion of the population is expected to be heterozygous?",
   choices=["0.50", "0.25", "0.75", "0.13", "0.38"], ans=0,
   why="From EK 7.5.A.2, q squared is 0.25 so q is 0.50 and p is 0.50, giving 2pq equal to 0.50. This is the one allele frequency at which heterozygotes reach their maximum share of the population under the model."),

 dict(q="At a locus in a population in Hardy-Weinberg equilibrium, the frequency of the dominant allele is 0.70. What proportion of individuals is expected to be homozygous recessive?",
   choices=["0.09", "0.30", "0.21", "0.42", "0.49"], ans=0,
   why="Because p plus q equals 1, a p of 0.70 gives a q of 0.30, and the homozygous recessive frequency is q squared, which is 0.09. The distractors are q itself, one of the two cross products, the full heterozygote term and p squared."),

 dict(q="At a locus with two alleles, 9 percent of the individuals in a population in Hardy-Weinberg equilibrium express a recessive trait. The frequency of the dominant allele in this population is",
   choices=["0.70", "0.30", "0.91", "0.09", "0.42"], ans=0,
   why="EK 7.5.A.2 with the printed equation: q squared is 0.09, so q is 0.30 and p is 1 minus 0.30, or 0.70. Subtracting the phenotype frequency from one, which gives 0.91, is the common error the third option represents."),

 dict(q="In a population in Hardy-Weinberg equilibrium, 9 percent of individuals show a recessive trait. What proportion of the population is expected to carry one copy of the recessive allele and one copy of the dominant allele?",
   choices=["0.42", "0.21", "0.49", "0.30", "0.09"], ans=0,
   why="With q squared equal to 0.09, q is 0.30 and p is 0.70, so 2pq is twice 0.70 times 0.30, or 0.42. Halving the correct product and reading p squared instead are the two errors the first distractors capture."),

 dict(q="A population of 400 individuals is in Hardy-Weinberg equilibrium at a locus where the recessive allele has a frequency of 0.10. How many heterozygous individuals are expected?",
   choices=["72", "36", "40", "144", "320"], ans=0,
   why="EK 7.5.A.2 with the printed equation: p is 0.90 and q is 0.10, so 2pq is 0.18, and 0.18 of 400 individuals is 72. Halving that product and using q alone are the errors behind the two nearest values."),

 dict(q="At a locus in a population in Hardy-Weinberg equilibrium the recessive allele has a frequency of 0.20. The expected number of heterozygotes exceeds the expected number of homozygous recessive individuals by a factor of",
   choices=["8 to 1", "4 to 1", "16 to 1", "2 to 1", "1 to 8"], ans=0,
   why="With q equal to 0.20 and p equal to 0.80, the heterozygote term 2pq is 0.32 and the homozygous recessive term q squared is 0.04, and 0.32 divided by 0.04 is 8. The ratio is 2p divided by q, so it grows as the recessive allele becomes rarer."),

 dict(q="A recessive allele has a frequency of 0.10 in a population in Hardy-Weinberg equilibrium. What proportion of all copies of that recessive allele is carried by heterozygous individuals?",
   choices=["0.90", "0.10", "0.18", "0.50", "0.09"], ans=0,
   why="Heterozygotes carry 2pq copies, or 0.18 per individual, and homozygous recessives carry twice q squared, or 0.02, so heterozygotes hold 0.18 of the 0.20 total, which is 0.90. This is why selection against the recessive phenotype removes rare alleles very slowly."),

 dict(q="The table gives the genotype counts at a codominant locus with two alleles in a sample of individuals. What is the frequency of allele F in this sample?",
   table=_T_COUNTS,
   choices=["0.60", "0.45", "0.40", "0.30", "0.75"], ans=0,
   why="EK 7.5.A.2 states that allele frequencies can be calculated from genotype frequencies. Each homozygote contributes two copies and each heterozygote one, so F copies are twice 90 plus 60, out of twice the 200 individuals sampled."),

 dict(q="Using the same table of genotype counts, what is the frequency of allele S in the sample?",
   table=_T_COUNTS,
   choices=["0.40", "0.25", "0.60", "0.50", "0.20"], ans=0,
   why="EK 7.5.A.2. Copies of S number twice 50 plus 60, out of 400 allele copies in 200 individuals. Because the locus carries only two alleles, this also follows from subtracting the frequency of F from one."),

 dict(q="The table compares the observed genotype counts in a sample with the counts expected if the population were in Hardy-Weinberg equilibrium. Which conclusion is best supported?",
   table=_T_OBS_EXP,
   choices=[
     "Heterozygotes are much scarcer than the model predicts, so at least one Hardy-Weinberg condition is not met in this population",
     "The population is in Hardy-Weinberg equilibrium, because the observed and expected totals agree",
     "The sample must have been miscounted, because a population cannot depart from the model",
     "Allele frequencies cannot be calculated for this sample because the genotypes are not in the expected ratio",
     "The observed counts show that a new allele has entered the population"], ans=0,
   why="EK 7.5.A.1 makes the model a null hypothesis, so a clear departure is evidence that one of the five conditions fails. Equal totals are guaranteed by how the expected counts are computed and say nothing, and EK 7.5.A.2 lets allele frequencies be calculated from any genotype counts."),

 dict(q="Using the observed counts in the same table, what is the frequency of allele M in the sample?",
   table=_T_OBS_EXP,
   choices=["0.70", "0.60", "0.30", "0.49", "0.40"], ans=0,
   why="EK 7.5.A.2. Copies of M number twice the 120 homozygotes plus the 40 heterozygotes, out of twice the 200 individuals in the sample. The expected counts are not needed for this calculation and must not be used in place of the observed ones."),

 dict(q="The table gives the frequencies of two alleles at one locus in a population over four generations. Which conclusion is best supported by these data?",
   table=_T_GEN,
   choices=[
     "The frequency of allele W rose in every interval shown, so at least one Hardy-Weinberg condition is not met in this population",
     "The population is in Hardy-Weinberg equilibrium because the two frequencies always sum to one",
     "The data show that allele W is dominant to allele R",
     "The population must be large, because the change from generation to generation is small",
     "Allele R will have disappeared from the population within one more generation"], ans=0,
   why="Under EK 7.5.A.1 the model predicts allele frequencies that do not change, so a directional shift across four generations is a departure from the null expectation. The two frequencies sum to one by definition of a two-allele locus and so carry no information about equilibrium."),

 dict(q="For the first generation shown in that same table, what heterozygote frequency does the Hardy-Weinberg model predict?",
   table=_T_GEN,
   choices=["0.32", "0.16", "0.20", "0.64", "0.04"], ans=0,
   why="EK 7.5.A.2 with the printed equation: the heterozygote term is 2pq, which is twice 0.80 times 0.20, or 0.32. Halving that product, reading q alone and reading p squared account for the three nearest distractors."),

 dict(q="The table gives allele frequencies and the observed heterozygote frequency for four populations. In which population do the observed heterozygotes depart most sharply from the Hardy-Weinberg prediction?",
   table=_T_FOUR,
   choices=["Population Z", "Population W", "Population X", "Population Y", "The four depart from the prediction by the same amount"], ans=0,
   why="EK 7.5.A.2 gives the prediction 2pq for each row, and three of the four observed values match that product exactly while the fourth is far below it. Comparing an observation with the model's own prediction is what makes the model a null hypothesis under EK 7.5.A.1."),

 dict(q="A researcher counts genotypes in a large sample and finds that the counts differ from the Hardy-Weinberg prediction by far more than sampling error can explain. The most defensible interpretation is that",
   choices=[
     "one or more of the model's conditions does not hold for this population at this locus",
     "the alleles at the locus are not inherited",
     "natural selection is acting, and no other explanation is possible",
     "the sample was too small for the model to apply",
     "the frequencies of the two alleles do not sum to one"], ans=0,
   why="EK 7.5.A.1 names five conditions, so rejecting the null expectation implicates the set and not any one member of it. Selection is only one of the five, and the sample was stated to be large."),

 dict(q="For a recessive human disorder, why is the Hardy-Weinberg model useful for estimating how many people carry one copy of the allele?",
   choices=[
     "Carriers cannot be told apart from homozygous dominant individuals by phenotype, but their expected frequency follows from the frequency of affected individuals",
     "The model counts carriers directly without any assumption about mating",
     "Carriers are the only genotype whose frequency the model can predict",
     "The model gives the number of carriers without needing the frequency of the disorder",
     "Carriers always make up half of any population"], ans=0,
   why="EK 7.5.A.2 allows allele frequencies to be obtained from genotype frequencies, and here the only directly countable genotype is the homozygous recessive one. From its frequency q squared the model yields q, then p, then the heterozygote term 2pq."),
]
