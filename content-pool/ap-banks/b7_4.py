# AP BIOLOGY 7.4 Population Genetics
# CED effective Fall 2025, Unit 7 Natural Selection. Big idea 1 (Evolution).
# Learning objectives 7.4.A, explain how random occurrences affect the genetic
# makeup of a population; 7.4.B, describe the role of random processes in the
# evolution of specific populations; 7.4.C, describe the change in the genetic
# makeup of a population over time. Suggested skill 3.B, STATE THE NULL
# HYPOTHESIS OR PREDICT THE RESULTS of an experiment.
#
# Essential knowledge relied on, in the framework's own words:
#   7.4.A.1     Evolution is ALSO driven by random occurrences.
#   7.4.A.1.i   MUTATION is a random process that ADDS NEW genetic variation to
#               a population.
#   7.4.A.1.ii  GENETIC DRIFT is a change in allele frequencies attributable to
#               a NONSELECTIVE process occurring in SMALL populations.
#   7.4.A.1.iii The BOTTLENECK EFFECT is a type of genetic drift that occurs
#               when a population size is reduced to a small number of
#               individuals for at least one generation.
#   7.4.A.1.iv  The FOUNDER EFFECT is a type of genetic drift that occurs when a
#               population is separated from other members of the population.
#               The frequency of genes and traits will shift based on the genes
#               in this new founder population.
#   7.4.A.1.v   MIGRATION can result in GENE FLOW (the addition or removal of
#               alleles from a population).
#   7.4.B.1     Random processes can lead to changes in allele frequencies in a
#               population.
#   7.4.B.1.i   Mutations result in genetic variation, which provides phenotypes
#               ON WHICH NATURAL SELECTION ACTS.
#   7.4.B.1.ii  Genetic drift can allow a SMALL population to DIVERGE from other
#               populations of the same species.
#   7.4.B.1.iii GENE FLOW between two populations PREVENTS them from diverging
#               into separate species.
#   7.4.C.1     Changes in allele frequencies provide EVIDENCE for the
#               occurrence of evolution in a population.
#
# HARDY-WEINBERG IS NOT ASKED HERE. It is EK 7.5 and belongs to a sibling's
# module, b7_5.py, whose own header records that it leaves drift, the bottleneck
# and founder effects and gene flow to this topic. Nothing in this module uses
# p squared plus 2pq plus q squared, and verify_b7_4.py scans the whole module
# and fails if it does. The arithmetic here is a different and simpler kind: an
# allele frequency COUNTED from copies of the allele, which needs no assumption
# about how the genotypes are distributed. Every such figure is recomputed in
# the verifier, and every table is checked for the property that makes counting
# valid at all -- that the allele copies total twice the number of individuals.
#
# DIVISION OF LABOUR ACROSS 7.1 TO 7.4 is set out in the header of b7_1.py. The
# other three topics are about selection, which is not random; this one is about
# the random occurrences EK 7.4.A.1 says ALSO drive evolution. Where the two
# meet -- EK 7.4.B.1.i, mutation providing the phenotypes selection acts on --
# the item is asked here, because it is this topic's statement. Speciation and
# the mechanisms that maintain reproductive isolation are 7.10's and belong to
# b7_10; the only claim made here about divergence is EK 7.4.B.1.ii's and
# EK 7.4.B.1.iii's own.
#
# ON THE ALLELE LETTERS. The two alleles of a gene are named with letters that
# differ by more than their case -- R and S, M and N -- rather than the
# conventional R and r. The verifier reads a table by its column HEADERS after
# normalizing them, and normalizing lowercases, so "copies of allele R" and
# "copies of allele r" collapse into one key and the two columns silently become
# the same column. The checker caught exactly that here, which is what it is for.
#
# ON FIGURES. No stem refers to a graph. Every data set is a table=.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. Prose notation, no LaTeX.
TOPIC = ("7.4", "Population Genetics", 7)

# One population counted before and immediately after a sharp reduction.
_T_CRASH = dict(
    headers=["Time point", "Number of individuals in the population",
             "Number of copies of allele R", "Number of copies of allele S"],
    rows=[["Before the reduction", "500", "300", "700"],
          ["Immediately after the reduction", "20", "32", "8"]])

# A source population and the small group that separated from it.
_T_FOUNDER = dict(
    headers=["Population", "Number of individuals in the population",
             "Number of copies of allele M", "Number of copies of allele N"],
    rows=[["Source population", "800", "640", "960"],
          ["Newly separated population", "10", "2", "18"]])

# The same allele followed in a small and a large population.
_T_DRIFT = dict(
    headers=["Generation", "Frequency of allele B in the small population (percent)",
             "Frequency of allele B in the large population (percent)"],
    rows=[["Generation 0", "50", "50"],
          ["Generation 5", "38", "51"],
          ["Generation 10", "64", "49"],
          ["Generation 15", "22", "50"],
          ["Generation 20", "0", "50"]])

# Three pairs of populations differing in how many individuals move between them.
_T_MIGRATION = dict(
    headers=["Pair of populations", "Individuals exchanged per generation",
             "Difference in allele frequency after 50 generations (percentage points)"],
    rows=[["Pair 1", "0", "46"],
          ["Pair 2", "2", "9"],
          ["Pair 3", "10", "2"]])

# One population followed across thirty generations.
_T_EVIDENCE = dict(
    headers=["Generation", "Frequency of allele D in the population (percent)"],
    rows=[["Generation 1", "12"],
          ["Generation 10", "19"],
          ["Generation 20", "28"],
          ["Generation 30", "41"]])

# Five small populations started from the same composition and left alone.
_T_REPLICATE = dict(
    headers=["Replicate population", "Frequency of allele E at the start (percent)",
             "Frequency of allele E after 15 generations (percent)"],
    rows=[["Replicate 1", "50", "0"],
          ["Replicate 2", "50", "78"],
          ["Replicate 3", "50", "31"],
          ["Replicate 4", "50", "100"],
          ["Replicate 5", "50", "62"]])

# Two populations, one of which received arrivals from elsewhere.
_T_ARRIVALS = dict(
    headers=["Population", "Individuals arrived from another population",
             "Number of different alleles of the gene present before",
             "Number of different alleles of the gene present after"],
    rows=[["Population 1", "Yes", "2", "4"],
          ["Population 2", "No", "3", "3"]])

QUESTIONS = [
 dict(q="Natural selection is described in this unit as a major mechanism of evolution. What does the framework add about what else drives evolution?",
   choices=[
     "Evolution is also driven by random occurrences",
     "Evolution is driven by selection alone, with no other contribution",
     "Evolution is driven by the needs of the organisms in a population",
     "Evolution is driven by changes in the genetic code a population uses",
     "Evolution is driven by changes an individual makes to its own phenotype"], ans=0,
   why="EK 7.4.A.1 states that evolution is also driven by random occurrences, which the framework then lists: mutation, genetic drift including its bottleneck and founder forms, and migration producing gene flow. EK 7.1.A.1 calls natural selection a major mechanism rather than the only one, which is what leaves room for these."),
 dict(q="What does the framework say about mutation as a random occurrence?",
   choices=[
     "It is a random process that adds new genetic variation to a population",
     "It is a directed process that adds the variation a population currently needs",
     "It is a random process that removes genetic variation from a population",
     "It is a process that changes allele frequencies without changing any sequence",
     "It occurs only in populations that are already small"], ans=0,
   why="EK 7.4.A.1.i states that mutation is a random process that adds new genetic variation to a population. Both halves matter: the process is random, so it is not directed by need, and its contribution is to add variation rather than to remove it."),
 dict(q="How does the framework define genetic drift?",
   choices=[
     "A change in allele frequencies attributable to a nonselective process occurring in small populations",
     "A change in allele frequencies attributable to selection acting in small populations",
     "A change in allele frequencies attributable to a nonselective process occurring in large populations",
     "A change in the phenotype of an individual attributable to its environment",
     "A change in the genetic code attributable to random mutation"], ans=0,
   why="EK 7.4.A.1.ii states that genetic drift is a change in allele frequencies attributable to a nonselective process occurring in small populations. Both qualifiers are the framework's: the process is nonselective, and the populations concerned are small."),
 dict(q="How does the framework define the bottleneck effect?",
   choices=[
     "A type of genetic drift that occurs when a population size is reduced to a small number of individuals for at least one generation",
     "A type of natural selection that occurs when a population is reduced in size",
     "A type of genetic drift that occurs when a population grows rapidly for at least one generation",
     "A type of gene flow that occurs when individuals migrate away from a population",
     "A type of mutation that occurs when a population is under stress"], ans=0,
   why="EK 7.4.A.1.iii states that the bottleneck effect is a type of genetic drift that occurs when a population size is reduced to a small number of individuals for at least one generation. It is classified as drift, which EK 7.4.A.1.ii makes nonselective, rather than as selection."),
 dict(q="How does the framework define the founder effect?",
   choices=[
     "A type of genetic drift that occurs when a population is separated from other members of the population",
     "A type of genetic drift that occurs when a population is reduced in size by a disaster",
     "A type of natural selection that occurs when a new habitat is colonized",
     "A type of gene flow that occurs when two populations merge",
     "A type of mutation that occurs in the first generation of a new population"], ans=0,
   why="EK 7.4.A.1.iv states that the founder effect is a type of genetic drift that occurs when a population is separated from other members of the population, and adds that the frequency of genes and traits will shift based on the genes in this new founder population. A reduction in size is the bottleneck effect of EK 7.4.A.1.iii instead."),
 dict(q="What does the framework say migration can result in?",
   choices=[
     "Gene flow, which is the addition or removal of alleles from a population",
     "Genetic drift, which is a change in allele frequencies in a small population",
     "Mutation, which adds new genetic variation to a population",
     "Natural selection, which acts on phenotypic variations in a population",
     "A change in the genetic code that the migrating individuals carry"], ans=0,
   why="EK 7.4.A.1.v states that migration can result in gene flow, and the framework defines gene flow in the same breath as the addition or removal of alleles from a population. Drift, mutation and selection are the separate processes of EK 7.4.A.1.ii, EK 7.4.A.1.i and EK 7.2.A.1."),
 dict(q="What distinguishes genetic drift from natural selection, in the framework's terms?",
   choices=[
     "Drift is attributable to a nonselective process, while selection acts on phenotypic variations that differ in fitness",
     "Drift acts on phenotypic variations that differ in fitness, while selection is nonselective",
     "Drift changes allele frequencies, while selection leaves allele frequencies unchanged",
     "Drift occurs in large populations, while selection occurs in small ones",
     "Drift is directed by the needs of the population, while selection is random"], ans=0,
   why="EK 7.4.A.1.ii calls genetic drift a change in allele frequencies attributable to a nonselective process, and EK 7.2.A.1 has natural selection act on phenotypic variations, with EK 7.2.A.3 making some of those variations raise or lower fitness. Whether the differences among individuals matter to the outcome is what separates them."),
 dict(q="What distinguishes the bottleneck effect from the founder effect, as the framework defines them?",
   choices=[
     "A bottleneck is a reduction in the size of an existing population; a founder effect follows a group being separated from the rest of the population",
     "A bottleneck follows a group being separated from the rest of the population; a founder effect is a reduction in size",
     "A bottleneck is a form of selection and a founder effect is a form of drift",
     "A bottleneck occurs in large populations and a founder effect in small ones",
     "A bottleneck adds alleles to a population and a founder effect removes them"], ans=0,
   why="EK 7.4.A.1.iii ties the bottleneck effect to a population size reduced to a small number of individuals for at least one generation, and EK 7.4.A.1.iv ties the founder effect to a population separated from other members of the population. Both are named as types of genetic drift, so the classification is not what separates them."),
 dict(q="The table reports one population counted before and immediately after a sharp reduction in its size. What was the frequency of allele R before the reduction and immediately after it?",
   table=_T_CRASH,
   choices=[
     "30 percent before and 80 percent after",
     "80 percent before and 30 percent after",
     "30 percent before and 30 percent after",
     "60 percent before and 40 percent after",
     "The frequencies cannot be worked out without knowing each individual's genotype"], ans=0,
   why="An allele frequency is the number of copies of that allele divided by the total number of copies of the gene. Before the reduction 300 of the 1000 copies are that allele, which is 30 percent, and afterwards 32 of the 40 copies, which is 80 percent. The genotypes need not be known, because the copies have been counted directly."),
 dict(q="Using the same population, which framework term names what happened to the allele frequency across the reduction?",
   table=_T_CRASH,
   choices=[
     "The bottleneck effect, a type of genetic drift following a population reduced to a small number of individuals",
     "The founder effect, a type of genetic drift following a group separated from the rest of a population",
     "Natural selection, since one allele became far more common than the other",
     "Gene flow, since the number of copies of each allele changed",
     "Mutation, since new alleles must have appeared during the reduction"], ans=0,
   why="EK 7.4.A.1.iii states that the bottleneck effect is a type of genetic drift occurring when a population size is reduced to a small number of individuals for at least one generation, which is what the table records: 500 individuals become 20. No new allele appears and no individual moves between populations, so mutation and gene flow are not what changed."),
 dict(q="The table reports a source population and a small group that separated from it. What was the frequency of allele M in each?",
   table=_T_FOUNDER,
   choices=[
     "40 percent in the source population and 10 percent in the separated group",
     "10 percent in the source population and 40 percent in the separated group",
     "40 percent in both, since the separated group came from the source population",
     "60 percent in the source population and 90 percent in the separated group",
     "The frequencies are equal, because a separated group is a random sample"], ans=0,
   why="An allele frequency is copies of that allele over total copies. The source population holds 640 of 1600 copies, which is 40 percent, and the separated group 2 of 20, which is 10 percent. EK 7.4.A.1.iv states that in the founder effect the frequency of genes and traits will shift based on the genes in the new founder population, which is what the difference shows."),
 dict(q="Which framework term names what the table records about the separated group?",
   table=_T_FOUNDER,
   choices=[
     "The founder effect, a type of genetic drift following the separation of a group from the rest of a population",
     "The bottleneck effect, a type of genetic drift following a reduction in the size of one population",
     "Gene flow, since alleles have moved between two populations",
     "Natural selection, since the allele frequencies of the two groups differ",
     "Mutation, since the separated group contains a different proportion of the allele"], ans=0,
   why="EK 7.4.A.1.iv states that the founder effect is a type of genetic drift that occurs when a population is separated from other members of the population, and that the frequency of genes and traits will shift based on the genes in the new founder population. The source population is not itself reduced here, which is what distinguishes this from the bottleneck effect of EK 7.4.A.1.iii."),
 dict(q="The table follows one allele in a small population and in a large one over twenty generations. What do the data show?",
   table=_T_DRIFT,
   choices=[
     "The frequency swung widely in the small population and barely moved in the large one",
     "The frequency swung widely in the large population and barely moved in the small one",
     "The frequency changed by the same amount in both populations",
     "The frequency rose steadily in both populations",
     "The frequency was unchanged in both populations across the twenty generations"], ans=0,
   why="EK 7.4.A.1.ii attributes genetic drift to a nonselective process occurring in small populations. In the table the small population goes 50, 38, 64, 22 and 0 percent while the large one stays between 49 and 51, which is the size dependence the statement describes."),
 dict(q="Using the same data, what has happened to allele B in the small population by generation 20?",
   table=_T_DRIFT,
   choices=[
     "It has been lost from that population, since its frequency has reached zero",
     "It has become the only allele present in that population, since its frequency has reached zero",
     "It has returned to its starting frequency in that population",
     "It has been lost from the large population as well",
     "It cannot be determined, because a frequency of zero is not a measurement"], ans=0,
   why="A frequency of zero means no copies of that allele remain in the population, which is loss rather than fixation. EK 7.4.A.1.ii makes such a change in allele frequencies in a small population attributable to a nonselective process, and the large population's frequency stays near 50 percent throughout."),
 dict(q="Five small populations were started from the same composition and left alone, with the results in the table. What do these data show about the process acting on them?",
   table=_T_REPLICATE,
   choices=[
     "The frequencies moved in different directions from an identical starting point, which is what a nonselective process produces",
     "The frequencies all moved in the same direction, which is what selection for one allele would produce",
     "The frequencies did not change in any of the five populations",
     "The frequencies all returned to their starting value after fifteen generations",
     "The frequencies changed only in the populations where the allele was rare to begin with"], ans=0,
   why="EK 7.4.A.1.ii defines genetic drift as a change in allele frequencies attributable to a nonselective process occurring in small populations. All five replicates start at 50 percent and end at 0, 78, 31, 100 and 62, so the direction differs between populations that were identical to begin with, which is what distinguishes a nonselective process from selection for one allele."),
 dict(q="What does the framework say mutations result in, and what does that provide?",
   choices=[
     "Genetic variation, which provides phenotypes on which natural selection acts",
     "Genetic variation, which selection then removes before it can be inherited",
     "New phenotypes that are inherited without any change to the DNA",
     "Changes in allele frequency that occur only in small populations",
     "The addition or removal of alleles between two populations"], ans=0,
   why="EK 7.4.B.1.i states that mutations result in genetic variation, which provides phenotypes on which natural selection acts. This is where the random process of EK 7.4.A.1.i meets the nonrandom one of EK 7.2.A.1: mutation supplies the material and selection sorts it."),
 dict(q="What does the framework say genetic drift can allow a small population to do?",
   choices=[
     "Diverge from other populations of the same species",
     "Converge on the composition of other populations of the same species",
     "Acquire new alleles that no population of the species carried before",
     "Resist any change in its allele frequencies",
     "Change the genetic code that it uses"], ans=0,
   why="EK 7.4.B.1.ii states that genetic drift can allow a small population to diverge from other populations of the same species. New alleles come from mutation under EK 7.4.A.1.i, and alleles arriving from elsewhere are gene flow under EK 7.4.A.1.v."),
 dict(q="What does the framework say gene flow between two populations does?",
   choices=[
     "It prevents them from diverging into separate species",
     "It causes them to diverge into separate species",
     "It prevents any change in the allele frequencies of either population",
     "It removes alleles from both populations without adding any",
     "It has no effect on either population's allele frequencies"], ans=0,
   why="EK 7.4.B.1.iii states that gene flow between two populations prevents them from diverging into separate species. EK 7.4.A.1.v defines gene flow as the addition or removal of alleles from a population, so it can change frequencies while keeping the two populations alike."),
 dict(q="Three pairs of populations differing in how many individuals move between them were compared after fifty generations, with the results in the table. What relationship do the data show?",
   table=_T_MIGRATION,
   choices=[
     "The more individuals exchanged per generation, the smaller the difference between the populations",
     "The more individuals exchanged per generation, the larger the difference between the populations",
     "The number exchanged per generation made no difference to how far the populations diverged",
     "The populations exchanging no individuals ended up the most alike",
     "All three pairs ended up equally different after fifty generations"], ans=0,
   why="EK 7.4.B.1.iii states that gene flow between two populations prevents them from diverging into separate species, and EK 7.4.A.1.v makes migration what produces gene flow. In the table the exchanges of 0, 2 and 10 individuals per generation give differences of 46, 9 and 2 percentage points, which fall as the exchange rises."),
 dict(q="What does the framework say a change in allele frequencies provides?",
   choices=[
     "Evidence for the occurrence of evolution in a population",
     "Proof that natural selection rather than a random process was responsible",
     "Evidence that the population's genetic code has changed",
     "Evidence that individuals changed their own phenotypes during their lives",
     "Nothing, since allele frequencies change constantly for no reason"], ans=0,
   why="EK 7.4.C.1 states that changes in allele frequencies provide evidence for the occurrence of evolution in a population. It is evidence that evolution occurred rather than of which mechanism produced it, since EK 7.4.B.1 makes random processes as well as selection able to change frequencies."),
 dict(q="The table follows one allele in a population across thirty generations. What conclusion do these data support?",
   table=_T_EVIDENCE,
   choices=[
     "Evolution has occurred in this population, because its allele frequencies have changed",
     "Evolution has not occurred in this population, because no new allele appeared",
     "Natural selection rather than any random process produced the change",
     "The individuals of this population changed their own allele frequencies during their lives",
     "The population's genetic code changed over the thirty generations"], ans=0,
   why="EK 7.4.C.1 states that changes in allele frequencies provide evidence for the occurrence of evolution in a population, and the recorded frequencies rise from 12 to 41 percent. The data cannot say which mechanism was responsible, because EK 7.4.B.1 allows random processes to change frequencies as well."),
 dict(q="A researcher will follow allele frequencies in several small populations for twenty generations, with no selective pressure applied. Which null hypothesis should the researcher state?",
   choices=[
     "That the allele frequencies of the populations will not change over the twenty generations",
     "That the allele frequencies of the populations will all rise over the twenty generations",
     "That the allele frequencies of the populations will all fall over the twenty generations",
     "That the allele frequencies of the populations will diverge from one another",
     "That natural selection will change the allele frequencies of the populations"], ans=0,
   why="Suggested skill 3.B asks students to state the null hypothesis of an experiment, and a null hypothesis is the statement of no difference or no change that the data may then contradict. The predictions of change, in either direction or between populations, are alternatives to it rather than the null itself."),
 dict(q="A researcher moves individuals between two populations that had been separate for many generations, and predicts what will happen to the difference between their allele frequencies. What should the prediction be?",
   choices=[
     "The difference will shrink, because gene flow between two populations prevents them from diverging",
     "The difference will grow, because gene flow between two populations drives them apart",
     "The difference will be unchanged, because migration does not affect allele frequencies",
     "The difference will shrink only if the two populations are small",
     "The difference cannot be predicted, because migration is a random occurrence"], ans=0,
   why="Suggested skill 3.B asks for a prediction. EK 7.4.A.1.v states that migration can result in gene flow, the addition or removal of alleles from a population, and EK 7.4.B.1.iii states that gene flow between two populations prevents them from diverging, so restoring the exchange should reduce the difference."),
 dict(q="Why does the framework attach genetic drift to small populations in particular?",
   choices=[
     "In a small population a chance event affects a large share of the copies of an allele, so frequencies can move far without any difference in fitness",
     "In a small population selection is stronger, so allele frequencies move further",
     "In a small population mutations occur more often, so new alleles appear faster",
     "In a small population every individual has the same genotype",
     "In a small population migration is impossible, so alleles cannot be added"], ans=0,
   why="EK 7.4.A.1.ii defines genetic drift as a change in allele frequencies attributable to a nonselective process occurring in small populations, and the data in this topic show a small population swinging between 0 and 64 percent while a large one stays near 50. The process is nonselective, so no difference in fitness is involved."),
 dict(q="A storm reduces an island population from several thousand individuals to about thirty for one generation, after which it grows again. Which framework term names what has happened to its allele frequencies?",
   choices=[
     "The bottleneck effect, a type of genetic drift",
     "The founder effect, a type of genetic drift",
     "Gene flow, resulting from migration",
     "Natural selection, resulting from a change in the environment",
     "Mutation, resulting from the stress of the storm"], ans=0,
   why="EK 7.4.A.1.iii states that the bottleneck effect is a type of genetic drift that occurs when a population size is reduced to a small number of individuals for at least one generation, which is exactly the scenario. The survivors are not described as differing in any relevant phenotype, so nothing here is the selection of EK 7.2.A.1."),
 dict(q="A few individuals from a mainland population reach an island and establish a new population there. Which framework term names what happens to the allele frequencies of the new population?",
   choices=[
     "The founder effect, in which the frequency of genes and traits shifts based on the genes in the new population",
     "The bottleneck effect, in which the mainland population is reduced in size",
     "Gene flow, in which alleles are added to the mainland population",
     "Natural selection, in which the island environment favors particular phenotypes",
     "Mutation, in which the founders acquire new alleles on arrival"], ans=0,
   why="EK 7.4.A.1.iv states that the founder effect is a type of genetic drift that occurs when a population is separated from other members of the population, and that the frequency of genes and traits will shift based on the genes in this new founder population. The mainland population is not itself reduced, which is what separates this from the bottleneck effect."),
 dict(q="The table reports two populations, one of which received individuals arriving from elsewhere. What do the data show?",
   table=_T_ARRIVALS,
   choices=[
     "The population that received arrivals gained alleles it had not carried before, while the other population's allele count was unchanged",
     "The population that received arrivals lost alleles it had carried before, while the other population gained some",
     "Both populations gained alleles, whether or not they received arrivals",
     "Neither population's allele count changed, so migration had no effect",
     "The population that received no arrivals gained the most alleles"], ans=0,
   why="EK 7.4.A.1.v states that migration can result in gene flow, which the framework defines as the addition or removal of alleles from a population. In the table the population receiving arrivals goes from two different alleles to four while the other stays at three, so the addition tracks the arrivals."),
 dict(q="A population loses several individuals that emigrate to another population, and the alleles those individuals carried become less common in the population they left. Which framework term covers this?",
   choices=[
     "Gene flow, which the framework defines as the addition or removal of alleles from a population",
     "The founder effect, which requires a group to be separated from the rest of the population",
     "The bottleneck effect, which requires a reduction to a small number of individuals",
     "Mutation, which adds new genetic variation to a population",
     "Natural selection, which acts on phenotypic variations"], ans=0,
   why="EK 7.4.A.1.v states that migration can result in gene flow, and the framework's own definition of gene flow includes the REMOVAL of alleles from a population as well as their addition. The emigrants take their alleles with them, which is removal in that sense."),
 dict(q="Two observations are made of one population: its allele frequencies have changed over fifty generations, and the change was not accompanied by any difference in reproductive success between the phenotypes. What can be concluded?",
   choices=[
     "Evolution has occurred in the population, and a nonselective process is the better explanation of this particular change",
     "Evolution has not occurred, because no difference in reproductive success was found",
     "Natural selection produced the change, since allele frequencies changed",
     "The population's genetic code changed, since its allele frequencies changed",
     "Nothing can be concluded, because allele frequencies change for no reason"], ans=0,
   why="EK 7.4.C.1 states that changes in allele frequencies provide evidence for the occurrence of evolution in a population, so the first observation settles that evolution occurred. EK 7.4.A.1.ii attributes drift to a nonselective process, and EK 7.2.A.3 makes selection a matter of differences in fitness, which the second observation reports as absent."),
 dict(q="Which account of the random occurrences in this topic is consistent with everything the framework states?",
   choices=[
     "Mutation adds new variation, drift changes frequencies nonselectively in small populations, migration adds or removes alleles, and any of these changes is evidence that evolution has occurred",
     "Mutation removes variation, drift acts only in large populations, migration changes nothing, and only selection is evidence of evolution",
     "Mutation is directed by need, drift is a form of selection, migration prevents alleles from moving, and allele frequencies never change",
     "Mutation and drift both act on phenotypes rather than alleles, and migration acts on the genetic code",
     "All three processes drive populations toward the same composition, which is why species remain uniform"], ans=0,
   why="Each clause of the keyed option is one of the framework's own statements: EK 7.4.A.1.i for mutation adding new genetic variation, EK 7.4.A.1.ii for drift as a nonselective process in small populations, EK 7.4.A.1.v for migration adding or removing alleles, and EK 7.4.C.1 for changes in allele frequencies being evidence of evolution."),
]
