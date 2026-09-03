# AP BIOLOGY 7.1 Introduction to Natural Selection
# CED effective Fall 2025, Unit 7 Natural Selection. Big idea 1 (Evolution).
# Learning objectives 7.1.A, describe the causes of natural selection, and
# 7.1.B, explain how natural selection affects populations. Suggested skill 2.A,
# describe characteristics of visual representations of biological concepts and
# processes.
#
# Essential knowledge relied on, in the framework's own words:
#   7.1.A.1  Natural selection is a MAJOR MECHANISM of evolution.
#   7.1.A.2  According to Darwin's theory of natural selection, COMPETITION FOR
#            LIMITED RESOURCES results in DIFFERENTIAL SURVIVAL. Individuals
#            with more favorable phenotypes are MORE LIKELY to survive and
#            produce more offspring, thus passing on those favorable traits to
#            subsequent generations.
#   7.1.B.1  Evolutionary fitness is measured by REPRODUCTIVE SUCCESS.
#   7.1.B.2  Biotic and abiotic environments can FLUCTUATE, affecting the RATE
#            AND DIRECTION of evolution. Different genetic variations can be
#            selected in each generation.
#
# ON THE SUGGESTED SKILL. 2.A is describing characteristics of visual
# representations, and this bank cannot carry a picture. The substitute is the
# one SCIENCE_BRIEF.md prescribes: the representation is a TABLE, and the items
# ask what the table shows. Nothing here refers to a graph the student cannot
# see.
#
# DIVISION OF LABOUR ACROSS 7.1 TO 7.4, planned together:
#   7.1  the CAUSES and the DEFINITIONS -- selection as a mechanism of
#        evolution, competition for limited resources giving differential
#        survival, fitness measured by reproductive success, and fluctuating
#        environments changing the rate and direction.
#   7.2  the VARIATION selection acts on -- that selection acts on phenotypic
#        variation, that environments apply selective pressures, that particular
#        variations raise or lower fitness, and that variation in the number and
#        types of molecules within cells contributes to it.
#   7.3  ARTIFICIAL selection, in which humans affect variation in other species.
#   7.4  the RANDOM processes -- mutation, genetic drift, the bottleneck and
#        founder effects, gene flow, and allele frequency change as evidence of
#        evolution.
# The hedge in EK 7.1.A.2 -- MORE LIKELY to survive, not certain to -- is
# preserved, and two items turn on exactly that.
#
# DELIBERATE OMISSIONS. Hardy-Weinberg is EK 7.5 and belongs to a sibling; no
# item here computes an allele frequency. The effect of a population's GENETIC
# DIVERSITY on its resilience is EK 7.11.A.1 and is asked in b7_11.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. Prose notation, no LaTeX.
TOPIC = ("7.1", "Introduction to Natural Selection", 7)

# Four individuals of one population, followed for life.
_T_FITNESS = dict(
    headers=["Individual", "Lifespan in years",
             "Number of offspring that survived to reproduce"],
    rows=[["Individual 1", "9", "2"],
          ["Individual 2", "4", "11"],
          ["Individual 3", "7", "5"],
          ["Individual 4", "11", "1"]])

# Two coat phenotypes of one species, measured across two kinds of year.
_T_PHENO = dict(
    headers=["Phenotype",
             "Mean number of surviving offspring in the cool years",
             "Mean number of surviving offspring in the warm years"],
    rows=[["Thick coat", "4.8", "1.9"],
          ["Thin coat", "1.6", "4.4"]])

# One population followed through five generations of changing conditions.
_T_GEN = dict(
    headers=["Generation", "Conditions during that generation",
             "Percent of the population showing the dark form"],
    rows=[["Generation 1", "Cool and wet", "20"],
          ["Generation 2", "Cool and wet", "31"],
          ["Generation 3", "Warm and dry", "29"],
          ["Generation 4", "Warm and dry", "18"],
          ["Generation 5", "Warm and dry", "11"]])

# The same trait followed through two equally long stretches of time.
_T_RATE = dict(
    headers=["Period", "Number of generations in the period",
             "Change in the percent of the population showing the trait"],
    rows=[["Period 1", "10", "4"],
          ["Period 2", "10", "28"]])

# Three phenotypes, each scored for survival and for offspring per survivor.
_T_THREE = dict(
    headers=["Phenotype", "Percent of individuals surviving to adulthood",
             "Mean number of offspring per surviving adult"],
    rows=[["Phenotype A", "80", "1.0"],
          ["Phenotype B", "40", "5.0"],
          ["Phenotype C", "60", "2.0"]])

QUESTIONS = [
 dict(q="How does the framework describe the place of natural selection among the processes that produce evolution?",
   choices=[
     "It is a major mechanism of evolution",
     "It is the only mechanism of evolution",
     "It is a minor mechanism that rarely affects populations",
     "It is a consequence of evolution rather than a mechanism of it",
     "It is a mechanism of development within an individual rather than of evolution"], ans=0,
   why="EK 7.1.A.1 states that natural selection is a major mechanism of evolution. The framework's word is major rather than only, and EK 7.4.A.1 goes on to state that evolution is also driven by random occurrences, so selection is one important mechanism among more than one."),
 dict(q="According to Darwin's theory as the framework states it, what does competition for limited resources result in?",
   choices=[
     "Differential survival among the individuals of a population",
     "Equal survival among the individuals of a population",
     "The appearance of new favorable phenotypes in the individuals that need them",
     "The removal of all variation from the population within one generation",
     "An increase in the resources available to the population"], ans=0,
   why="EK 7.1.A.2 states that according to Darwin's theory of natural selection, competition for limited resources results in differential survival. Differential means that individuals do not all fare alike, and nothing in the statement has competition create the phenotypes it acts on."),
 dict(q="What does the framework say about individuals with more favorable phenotypes?",
   choices=[
     "They are more likely to survive and produce more offspring",
     "They are certain to survive and produce more offspring",
     "They survive at the same rate as other individuals but produce fewer offspring",
     "They acquire their favorable phenotypes in response to competition",
     "They are the only individuals of the population that reproduce at all"], ans=0,
   why="EK 7.1.A.2 states that individuals with more favorable phenotypes are MORE LIKELY to survive and produce more offspring. The framework's claim is about likelihood rather than certainty, and it says nothing about other individuals failing to reproduce entirely."),
 dict(q="What does the framework say is the consequence of more favorable phenotypes surviving and producing more offspring?",
   choices=[
     "Those favorable traits are passed on to subsequent generations",
     "Those favorable traits disappear from the population within a generation",
     "The individuals that survive acquire additional favorable traits during their lives",
     "The resources available to the population increase in each generation",
     "Every individual of the next generation shows the identical phenotype"], ans=0,
   why="EK 7.1.A.2 ends by stating that individuals with more favorable phenotypes thus pass on those favorable traits to subsequent generations. Traits are transmitted rather than acquired during a lifetime, and the statement makes no claim that the next generation is uniform."),
 dict(q="How is evolutionary fitness measured, according to the framework?",
   choices=[
     "By reproductive success",
     "By the length of an individual's life",
     "By an individual's size relative to others of its species",
     "By the number of resources an individual consumes",
     "By the number of genes an individual carries"], ans=0,
   why="EK 7.1.B.1 states that evolutionary fitness is measured by reproductive success. Longevity, size and resource consumption may each contribute to reproductive success in a given case, but the framework names only the outcome, offspring produced, as the measure."),
 dict(q="Four individuals of one population were followed for their whole lives, with the results in the table. Which individual had the greatest evolutionary fitness?",
   table=_T_FITNESS,
   choices=[
     "The individual that left 11 surviving offspring",
     "The individual that lived 11 years",
     "The individual that lived 9 years",
     "The individual that lived 7 years and left 5 surviving offspring",
     "All four had equal fitness, since all four survived to reproduce"], ans=0,
   why="EK 7.1.B.1 states that evolutionary fitness is measured by reproductive success, so the individual leaving the most surviving offspring has the greatest fitness. In the table the highest offspring count and the longest lifespan belong to different individuals, which is what makes the choice between the two measures a real one."),
 dict(q="Using the same data, what does the record of the longest-lived individual show about the relationship between lifespan and fitness?",
   table=_T_FITNESS,
   choices=[
     "The longest-lived individual left the fewest surviving offspring, so a long life does not by itself confer high fitness",
     "The longest-lived individual left the most surviving offspring, so a long life confers high fitness",
     "The longest-lived individual left the average number of surviving offspring, so lifespan and fitness are unrelated in every population",
     "Lifespan is the framework's measure of fitness, so the longest-lived individual is the fittest",
     "No comparison can be made, because fitness cannot be measured in a single generation"], ans=0,
   why="EK 7.1.B.1 makes reproductive success the measure of evolutionary fitness. In this population the individual with the longest recorded lifespan has the lowest offspring count, which shows directly that the two do not have to move together; the data do not license a general claim about every population."),
 dict(q="What does the framework say fluctuating biotic and abiotic environments affect?",
   choices=[
     "The rate and the direction of evolution",
     "The rate of evolution but never its direction",
     "The direction of evolution but never its rate",
     "The number of genes present in each individual",
     "Nothing, because evolution proceeds at a constant rate in all conditions"], ans=0,
   why="EK 7.1.B.2 states that biotic and abiotic environments can fluctuate, affecting the rate and direction of evolution. Both are named, and the same statement adds that different genetic variations can be selected in each generation."),
 dict(q="What does the framework say can happen from one generation to the next as environments fluctuate?",
   choices=[
     "Different genetic variations can be selected in each generation",
     "The same genetic variation is selected in every generation once selection has begun",
     "Selection stops entirely until the environment becomes stable again",
     "New genetic variations are created by the environment in each generation",
     "Every genetic variation present is removed from the population each generation"], ans=0,
   why="EK 7.1.B.2 states that different genetic variations can be selected in each generation. The environment determines which existing variation is favoured rather than creating variations, which under EK 6.7.B.1.ii arise from mutation."),
 dict(q="One population was followed through five generations while conditions changed, as recorded in the table. What do the data show about the direction of change?",
   table=_T_GEN,
   choices=[
     "The dark form rose while the conditions were cool and wet and fell once they became warm and dry",
     "The dark form fell while the conditions were cool and wet and rose once they became warm and dry",
     "The dark form rose steadily across all five generations regardless of conditions",
     "The dark form remained unchanged across all five generations",
     "The dark form changed at random, since the conditions were the same in every generation"], ans=0,
   why="EK 7.1.B.2 states that fluctuating environments affect the rate and direction of evolution and that different genetic variations can be selected in each generation. In the table the dark form goes from 20 to 31 percent while the conditions are cool and wet, and from 29 down to 11 percent after the conditions change, so the direction reverses when the conditions do."),
 dict(q="Why does Darwin's theory as the framework states it require resources to be limited?",
   choices=[
     "Competition arises because the resources cannot support every individual, and that competition is what produces differential survival",
     "Limited resources cause the favorable phenotypes to appear in the individuals that need them",
     "Limited resources prevent any individual from reproducing, which is what selection requires",
     "Limited resources make every individual equally likely to survive",
     "Limited resources are not part of the theory, which rests on differences in lifespan alone"], ans=0,
   why="EK 7.1.A.2 states that competition for limited resources results in differential survival. If resources were unlimited there would be nothing to compete for and no differential survival to follow from the competition; the statement does not have limitation create phenotypes."),
 dict(q="A student says that natural selection guarantees that the individual with the most favorable phenotype in a population will survive. How should this be corrected?",
   choices=[
     "The framework says such an individual is more likely to survive and reproduce, which is a statement about probability rather than a guarantee",
     "The framework says such an individual is certain to survive, so the student is correct",
     "The framework says such an individual is less likely to survive, so the student has the direction reversed",
     "The framework makes no claim about survival at all, only about the number of genes an individual carries",
     "The framework says survival is determined entirely by chance, so phenotype is irrelevant"], ans=0,
   why="EK 7.1.A.2 states that individuals with more favorable phenotypes are MORE LIKELY to survive and produce more offspring. An individual with a favourable phenotype can still meet an accident, and the framework's wording is what protects the claim from that objection."),
 dict(q="Two coat phenotypes were compared across two kinds of year, with the results in the table. What do the data show?",
   table=_T_PHENO,
   choices=[
     "Which phenotype leaves more offspring reverses between the two kinds of year",
     "The same phenotype leaves more offspring in both kinds of year",
     "Neither phenotype leaves more offspring than the other in either kind of year",
     "The thick coat phenotype leaves more offspring in both kinds of year",
     "The thin coat phenotype leaves more offspring in both kinds of year"], ans=0,
   why="EK 7.1.B.2 states that fluctuating biotic and abiotic environments affect the rate and direction of evolution and that different genetic variations can be selected in each generation. In the cool years the thick coat leaves 4.8 offspring against 1.6, and in the warm years the thin coat leaves 4.4 against 1.9, so the advantage changes hands."),
 dict(q="What does differential survival mean, in the framework's sense?",
   choices=[
     "That the individuals of a population do not all survive at the same rate",
     "That every individual of a population survives for a different length of time but all reproduce equally",
     "That survival differs between species rather than within a population",
     "That an individual's chance of survival changes during its own lifetime",
     "That survival is the same for all individuals but reproduction differs"], ans=0,
   why="EK 7.1.A.2 states that competition for limited resources results in differential survival, and pairs that with individuals of more favourable phenotypes being more likely to survive. The differences the statement concerns are among the individuals of a population, which is the level at which the favourable phenotypes differ."),
 dict(q="A change in temperature over several generations alters which of two variations leaves more offspring in a population. Which part of the framework does this illustrate?",
   choices=[
     "That abiotic environments can fluctuate, affecting the rate and direction of evolution",
     "That biotic environments can fluctuate, since temperature is a living component of the environment",
     "That competition for limited resources creates new phenotypes",
     "That evolutionary fitness is measured by an individual's lifespan",
     "That natural selection is the only mechanism of evolution"], ans=0,
   why="EK 7.1.B.2 states that biotic and abiotic environments can fluctuate, affecting the rate and direction of evolution. Temperature is a non-living feature of the environment and so is abiotic; EK 7.1.A.1 also makes selection a major rather than the only mechanism."),
 dict(q="A new predator arrives in a habitat and the variation that leaves the most offspring changes as a result. Which part of the framework does this illustrate?",
   choices=[
     "That biotic environments can fluctuate, affecting the rate and direction of evolution",
     "That abiotic environments can fluctuate, since a predator is a non-living component",
     "That evolutionary fitness is measured by the number of predators an individual escapes",
     "That favorable phenotypes appear in response to the arrival of a predator",
     "That competition for limited resources has no effect once a predator is present"], ans=0,
   why="EK 7.1.B.2 states that biotic and abiotic environments can fluctuate, affecting the rate and direction of evolution. A predator is a living part of the environment and so is biotic, and EK 7.1.B.1 makes reproductive success rather than escape the measure of fitness."),
 dict(q="What is the difference between the rate of evolution and the direction of evolution, both of which the framework says a fluctuating environment can affect?",
   choices=[
     "The rate is how fast the composition of a population changes, and the direction is which variation is becoming more common",
     "The rate is which variation is becoming more common, and the direction is how fast the change occurs",
     "The rate applies to abiotic changes and the direction to biotic changes",
     "The rate applies to individuals and the direction to whole species",
     "There is no difference, since the framework uses the two words interchangeably"], ans=0,
   why="EK 7.1.B.2 names both the rate and the direction as things a fluctuating environment affects, so they must be distinct. How quickly a population changes and which way it is changing are separate quantities, and the same statement's clause about different variations being selected in each generation is about direction."),
 dict(q="The same trait was followed through two equally long periods, as reported in the table. What do the data show?",
   table=_T_RATE,
   choices=[
     "The trait changed far faster during the second period than during the first",
     "The trait changed far faster during the first period than during the second",
     "The trait changed at the same rate during both periods",
     "The trait changed in opposite directions during the two periods",
     "No comparison of rates is possible, because the two periods lasted different numbers of generations"], ans=0,
   why="EK 7.1.B.2 states that fluctuating environments affect the rate of evolution, and a rate is a change divided by the time it took. Both periods cover ten generations, so their changes of 4 and 28 percentage points can be compared directly and the second is seven times the first."),
 dict(q="Three phenotypes were scored for survival to adulthood and for offspring per surviving adult, as reported in the table. Which phenotype has the greatest reproductive success per individual born?",
   table=_T_THREE,
   choices=[
     "Phenotype B, whose lower survival is more than offset by its much higher offspring number",
     "Phenotype A, whose survival to adulthood is the highest of the three",
     "Phenotype C, whose two values are both intermediate",
     "Phenotype A and phenotype C equally, since both survive better than phenotype B",
     "The three cannot be compared, because survival and offspring number are different quantities"], ans=0,
   why="EK 7.1.B.1 makes reproductive success the measure of evolutionary fitness, and the offspring expected per individual born is the survival proportion multiplied by the offspring per survivor. That gives 0.8, 2.0 and 1.2 for the three phenotypes, so the phenotype with the lowest survival has the highest expected number of offspring."),
 dict(q="An individual survives longer than any other member of its population but produces no offspring. What is its evolutionary fitness?",
   choices=[
     "Zero, because evolutionary fitness is measured by reproductive success",
     "The highest in the population, because it survived longest",
     "Average, because survival and reproduction count equally",
     "Undefined, because fitness applies only to whole populations",
     "The highest in the population, because it used the most resources"], ans=0,
   why="EK 7.1.B.1 states that evolutionary fitness is measured by reproductive success. An individual that leaves no offspring contributes nothing to subsequent generations, which is what EK 7.1.A.2 makes the point of surviving and reproducing."),
 dict(q="Why does the framework describe a phenotype as more favorable rather than as simply better?",
   choices=[
     "Because the environment determines which phenotype leaves more offspring, and environments fluctuate",
     "Because a phenotype is favorable only if it makes an individual larger than others",
     "Because no phenotype ever affects an individual's chance of leaving offspring",
     "Because a phenotype is favorable only if it appears in every member of the population",
     "Because favorable phenotypes are created by the environment when they are needed"], ans=0,
   why="EK 7.1.A.2 speaks of more favorable phenotypes and EK 7.1.B.2 states that fluctuating environments affect the rate and direction of evolution, with different genetic variations selected in each generation. A phenotype is therefore favourable relative to a set of conditions rather than in itself."),
 dict(q="A trait improves an individual's chance of surviving to adulthood but greatly reduces the number of offspring it goes on to produce. How does the framework's measure of fitness treat this trait?",
   choices=[
     "Fitness is measured by reproductive success, so the reduction in offspring counts against the trait",
     "Fitness is measured by survival, so the improvement in survival is decisive",
     "Fitness is measured by the sum of years lived and offspring produced, so the two cancel",
     "Fitness cannot be assessed for a trait with effects in two directions",
     "Fitness is measured by the trait's frequency, so no measurement of the individual is needed"], ans=0,
   why="EK 7.1.B.1 states that evolutionary fitness is measured by reproductive success, which is the offspring an individual leaves. Survival matters to the framework because EK 7.1.A.2 has it lead to producing more offspring, so a trait that raises survival while lowering offspring number is judged on the offspring."),
 dict(q="A researcher wants to compare the evolutionary fitness of two phenotypes in a population. What must be measured?",
   choices=[
     "The reproductive success of individuals of each phenotype",
     "The average lifespan of individuals of each phenotype",
     "The average body size of individuals of each phenotype",
     "The number of resources each phenotype consumes",
     "The number of genes carried by individuals of each phenotype"], ans=0,
   why="EK 7.1.B.1 states that evolutionary fitness is measured by reproductive success, so that is the quantity the comparison requires. The other measures might correlate with it in a particular population but none of them is what the framework names as the measure."),
 dict(q="What follows from natural selection being a major mechanism of evolution rather than the only one?",
   choices=[
     "A change in a population's composition may have been produced by another mechanism as well as by selection",
     "Every change in a population's composition must have been produced by selection",
     "Selection acts only on populations too small to change in any other way",
     "Selection cannot produce any change in a population's composition",
     "Evolution occurs only when selection and every other mechanism act together"], ans=0,
   why="EK 7.1.A.1 calls natural selection a major mechanism of evolution, and EK 7.4.A.1 states that evolution is also driven by random occurrences. More than one mechanism is therefore available, so observing a change does not by itself identify which produced it."),
 dict(q="Two populations of one species live in habitats that differ in how much their conditions vary from year to year. In which population would the framework expect the direction of evolution to change more often?",
   choices=[
     "The population whose conditions fluctuate more, because different genetic variations can be selected in each generation",
     "The population whose conditions fluctuate less, because stable conditions change the direction of selection",
     "Neither, because the direction of evolution is fixed once selection begins",
     "Neither, because the framework attributes direction to chance alone",
     "The population whose conditions fluctuate less, because it has more time to respond"], ans=0,
   why="EK 7.1.B.2 states that biotic and abiotic environments can fluctuate, affecting the rate and direction of evolution, and that different genetic variations can be selected in each generation. More fluctuation gives more occasions for the favoured variation to change."),
 dict(q="In a population living where resources are abundant enough for every individual, what does Darwin's theory as the framework states it predict about differential survival from competition?",
   choices=[
     "Competition for those resources would not be producing differential survival, since the theory ties the two together",
     "Competition would produce even stronger differential survival, since there is more to compete for",
     "Differential survival would occur but reproduction would stop",
     "The population would acquire new favorable phenotypes to use the surplus",
     "Every individual would produce exactly the same number of offspring in every generation"], ans=0,
   why="EK 7.1.A.2 states that competition for LIMITED resources results in differential survival, so the limitation is part of the causal claim. The statement addresses what competition for limited resources produces and does not claim that this is the only thing that could ever differentiate survival."),
 dict(q="Which statement correctly separates what an individual inherits from what it experiences, as the framework describes natural selection?",
   choices=[
     "An individual inherits its phenotype's basis and passes those traits on if it reproduces; what it experiences is the competition that determines whether it does",
     "An individual acquires its phenotype from the competition it experiences and passes that acquired phenotype on",
     "An individual inherits the competition it will face and acquires its traits during its lifetime",
     "An individual neither inherits nor acquires a phenotype, since phenotype is a property of populations",
     "An individual passes on the experiences of its lifetime rather than the traits it inherited"], ans=0,
   why="EK 7.1.A.2 has individuals with more favorable phenotypes pass on those favorable traits to subsequent generations, and EK 5.3.A.2.iii makes what is inherited the set of alleles. Competition for limited resources is the circumstance that decides which individuals reproduce; it is not itself transmitted."),
 dict(q="A biologist observes that a particular variation became more common in a population over ten generations. What does the framework allow the biologist to conclude from this observation alone?",
   choices=[
     "That the composition of the population changed, without yet identifying which mechanism produced the change",
     "That natural selection produced the change, since selection is a mechanism of evolution",
     "That the environment fluctuated during those ten generations",
     "That the individuals with that variation lived longer than the others",
     "That the variation arose by mutation during those ten generations"], ans=0,
   why="EK 7.1.A.1 makes natural selection a major mechanism of evolution rather than the only one, and EK 7.4.A.1 adds that evolution is also driven by random occurrences. A change in composition is therefore consistent with more than one mechanism, and EK 7.1.B.1 makes reproductive success rather than lifespan the relevant measure in any case."),
 dict(q="Which chain of claims matches the framework's account of natural selection?",
   choices=[
     "Resources are limited, so individuals compete; competition gives differential survival; individuals with more favorable phenotypes are more likely to survive and produce more offspring; those traits pass to later generations",
     "Individuals acquire favorable phenotypes; those phenotypes make resources unlimited; every individual then survives and reproduces equally",
     "Individuals inherit favorable phenotypes; those individuals live longer but leave no more offspring; the population is unchanged",
     "Resources are unlimited, so individuals do not compete; differential survival occurs anyway; traits pass to later generations",
     "Environments fluctuate; the fluctuation creates new phenotypes; those phenotypes are then inherited"], ans=0,
   why="The chain is EK 7.1.A.2 taken in order: competition for limited resources results in differential survival, individuals with more favorable phenotypes are more likely to survive and produce more offspring, and those favorable traits are thus passed on to subsequent generations. Each rejected chain breaks one of those links."),
 dict(q="Which pair of framework statements together explains why a variation that is favored in one generation may not be favored in the next?",
   choices=[
     "That biotic and abiotic environments can fluctuate and affect the direction of evolution, and that different genetic variations can be selected in each generation",
     "That natural selection is a major mechanism of evolution, and that fitness is measured by reproductive success",
     "That competition is for limited resources, and that individuals are certain to survive if their phenotype is favorable",
     "That environments create the variations they favor, and that those variations are inherited",
     "That evolution proceeds at a constant rate, and that its direction never changes"], ans=0,
   why="EK 7.1.B.2 contains both halves: biotic and abiotic environments can fluctuate, affecting the rate and direction of evolution, and different genetic variations can be selected in each generation. The second clause is what makes the change of favoured variation between generations explicit."),
]
