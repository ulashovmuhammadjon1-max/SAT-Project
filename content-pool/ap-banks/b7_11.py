# AP BIOLOGY 7.11 Variations in Populations
# CED effective Fall 2025, Unit 7 Natural Selection, BIG IDEA 4 Systems
# Interactions (not Big Idea 1, unlike the rest of this unit).
# Learning objective 7.11.A, explain how the genetic diversity of a species or
# population affects its ability to withstand environmental pressures.
# Suggested skill 6.C, provide reasoning to justify a claim by connecting
# evidence to biological theories.
#
# Essential knowledge relied on, in the framework's own terms:
#   7.11.A.1  the LEVEL OF VARIATION in a population AFFECTS POPULATION
#             DYNAMICS.
#               i. the ability of a population to respond to changes in the
#                  environment is INFLUENCED BY GENETIC DIVERSITY. Species and
#                  populations with LITTLE genetic diversity are AT RISK OF
#                  DECLINE OR EXTINCTION.
#              ii. genetically diverse populations are MORE RESILIENT to
#                  environmental perturbation BECAUSE THEY ARE MORE LIKELY TO
#                  CONTAIN INDIVIDUALS THAT CAN WITHSTAND the environmental
#                  pressure.
#             iii. alleles that are ADAPTIVE IN ONE environmental condition MAY
#                  BE DELETERIOUS IN ANOTHER because of DIFFERENT SELECTIVE
#                  PRESSURES.
#
# The CED's illustrative examples for EK 7.11.A.1 are California condors,
# black-footed ferrets, prairie chickens, potato blight, corn rust, genetic
# diversity and selective pressures, and antibiotic resistance in bacteria,
# with the parenthetical note that not all individuals in a diverse population
# are susceptible to a disease outbreak. Illustrative examples are not
# assessable content, so no key here depends on knowing one; two scenarios are
# built on the SHAPES those examples describe -- a genetically uniform crop and
# a captive population founded from few individuals -- without naming a species
# or asserting a fact about one.
#
# THE HEDGE IS PRESERVED. EK 7.11.A.1.ii says a diverse population is MORE
# LIKELY to contain individuals that can withstand the pressure. That is a
# statement about probability, and no key in this module upgrades it into a
# guarantee; two items turn on exactly that distinction.
#
# DELIBERATE OMISSIONS. EK 8.6.A.1 makes the same kind of claim about the
# diversity of an ECOSYSTEM's component parts and is asked in b8_6, along with
# keystone species. Everything here is about GENETIC diversity within one
# species or population, which is the level EK 7.11.A.1 works at, and no item
# here mentions ecosystem diversity, keystone species or species richness.
# Small population size as a Hardy-Weinberg condition is EK 7.5.A.1 and is
# asked in b7_5; the single item here that distinguishes population size from
# genetic diversity does so to separate the two, not to restate that condition.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: this bank is exported
# untypeset.
TOPIC = ("7.11", "Variations in Populations", 7)

_T_DIVERSITY = dict(
    headers=["Population", "Number of distinct alleles detected across ten loci",
             "Percentage of individuals surviving the outbreak"],
    rows=[["Population 1", "8", "5"],
          ["Population 2", "15", "22"],
          ["Population 3", "23", "41"],
          ["Population 4", "31", "58"]])

_T_ALLELE = dict(
    headers=["Environmental condition",
             "Percentage of individuals carrying allele T that survived",
             "Percentage of individuals lacking allele T that survived"],
    rows=[["Cool and wet season", "82", "44"],
          ["Hot and dry season", "31", "76"]])

QUESTIONS = [
 dict(q="According to the course framework, what does the level of variation in a population affect?",
   choices=["Population dynamics", "The number of loci in the genome",
            "The rate at which mutations occur", "The geographic range the species can be described in",
            "Whether the species reproduces sexually or asexually"], ans=0,
   why="EK 7.11.A.1 states that the level of variation in a population affects population dynamics. The number of loci, the mutation rate and the mode of reproduction are properties the statement does not connect to the level of variation."),

 dict(q="What does the framework say influences a population's ability to respond to changes in its environment?",
   choices=["Its genetic diversity", "The total area of its geographic range",
            "The number of species in the same habitat", "The age of the rocks in which its fossils occur",
            "Whether its habitat is terrestrial or aquatic"], ans=0,
   why="EK 7.11.A.1 states that the ability of a population to respond to changes in the environment is influenced by genetic diversity. Range, community composition and habitat type are not what that statement names."),

 dict(q="According to the framework, species and populations with little genetic diversity are at risk of",
   choices=["decline or extinction", "an increased mutation rate",
            "becoming a new species within one generation", "losing the ability to reproduce sexually",
            "expanding rapidly into new habitats"], ans=0,
   why="EK 7.11.A.1 states that species and populations with little genetic diversity are at risk of decline or extinction. The other outcomes are not consequences the statement attaches to low diversity."),

 dict(q="Why does the framework say genetically diverse populations are more resilient to environmental perturbation?",
   choices=[
     "They are more likely to contain individuals that can withstand the environmental pressure",
     "They contain more individuals in total than less diverse populations",
     "Their individuals each carry more copies of every allele",
     "Their mutation rate rises when the environment changes",
     "They occupy a larger geographic range than less diverse populations"], ans=0,
   why="EK 7.11.A.1 gives that reason in as many words: genetically diverse populations are more resilient because they are more likely to contain individuals that can withstand the environmental pressure. Diversity is about the variety of alleles present, not about how many individuals there are."),

 dict(q="According to the framework, why may an allele that is adaptive in one environmental condition be deleterious in another?",
   choices=[
     "Because the selective pressures differ between the two conditions",
     "Because the allele changes its sequence when the environment changes",
     "Because alleles are adaptive only in the environment in which they first arose",
     "Because deleterious alleles are removed from every population within a generation",
     "Because an allele has the same effect in every environment"], ans=0,
   why="EK 7.11.A.1 states that alleles adaptive in one environmental condition may be deleterious in another because of different selective pressures. The allele itself does not change; what changes is what the environment favours."),

 dict(q="A grower plants a large field with a single crop variety in which every plant is genetically nearly identical. Which risk does the framework's account identify?",
   choices=[
     "A pressure that harms one plant is likely to harm nearly all of them, so the planting is at risk of collapse",
     "The plants will mutate more rapidly than a diverse planting would",
     "The plants will be unable to reproduce at all",
     "The planting will use more water than a diverse planting would",
     "The planting will be immune to any new disease, because all plants are alike"], ans=0,
   why="EK 7.11.A.1 states that populations with little genetic diversity are at risk of decline or extinction, and that diverse populations are more resilient because they are more likely to contain individuals that can withstand the pressure. Near-identical plants offer few such individuals."),

 dict(q="A captive breeding programme is founded from a very small number of surviving individuals, and the resulting population carries far fewer distinct alleles than the original wild population did. What does the framework's account predict about this population?",
   choices=[
     "Its ability to respond to future environmental change is reduced, so it is at greater risk of decline",
     "It will respond to environmental change more quickly than the wild population did",
     "Its mutation rate will rise to replace the missing alleles within a generation",
     "It will be unaffected, because the number of individuals is what matters",
     "It will automatically regain the missing alleles once released"], ans=0,
   why="EK 7.11.A.1 states that the ability to respond to environmental change is influenced by genetic diversity and that populations with little of it are at risk of decline or extinction. Nothing in the statement supplies a mechanism that restores the missing variation quickly."),

 dict(q="A disease sweeps through two populations of the same species. In one population every individual is affected; in the other, a substantial minority is unaffected. Which difference between the populations does the framework's account point to?",
   choices=[
     "A difference in genetic diversity, since a diverse population is more likely to contain individuals that can withstand the pressure",
     "A difference in the total number of individuals present",
     "A difference in the age of the two populations",
     "A difference in how quickly the two populations mutate in response to the disease",
     "A difference in the number of species sharing their habitat"], ans=0,
   why="EK 7.11.A.1 states that genetically diverse populations are more resilient to environmental perturbation because they are more likely to contain individuals that can withstand the pressure. Individuals unaffected by an outbreak are precisely such individuals."),

 dict(q="A student claims that a genetically diverse population is guaranteed to survive any environmental change. How does this claim depart from the framework's statement?",
   choices=[
     "The framework says such a population is MORE LIKELY to contain individuals that can withstand the pressure, which is a probability rather than a guarantee",
     "The framework says diverse populations are less resilient than uniform ones",
     "The framework says genetic diversity has no effect on resilience",
     "The framework says only the number of individuals matters",
     "The framework says environmental change never threatens any population"], ans=0,
   why="EK 7.11.A.1 uses the words more likely, which states a tendency and not a certainty. A pressure that no allele in the population happens to counter would still affect every individual, however diverse the population is in other respects."),

 dict(q="Which of the following is the best reason that a large population can still be at risk of decline under the framework's account?",
   choices=[
     "A population can be large and still carry few distinct alleles, so numbers and genetic diversity are not the same thing",
     "Large populations always mutate more slowly than small ones",
     "A large population cannot respond to any environmental change",
     "Genetic diversity rises automatically with population size",
     "Numbers of individuals are the only thing the framework considers"], ans=0,
   why="EK 7.11.A.1 attaches the risk of decline or extinction to LITTLE GENETIC DIVERSITY rather than to small numbers. The two properties can come apart, which is why the statement is written about variation rather than about abundance."),

 dict(q="Which observation would best support the claim that genetic diversity influences a population's ability to withstand an environmental pressure?",
   choices=[
     "Populations measured to carry more distinct alleles suffer smaller losses under the same pressure",
     "A single population with many alleles survives one pressure",
     "Two populations with equal diversity suffer equal losses",
     "A population's size increases in a year when no pressure occurs",
     "A population with few alleles occupies a smaller range than one with many"], ans=0,
   why="Skill 6.C asks for reasoning that connects evidence to a claim. The claim relates a difference in diversity to a difference in outcome, so the evidence must vary the diversity and compare the outcomes; a single case and a comparison of equals both leave the relationship untested."),

 dict(q="Which observation would most weaken the claim that a particular population's losses were due to its low genetic diversity?",
   choices=[
     "A neighbouring population with far greater genetic diversity suffered equally heavy losses from the same pressure",
     "The population in question carried fewer distinct alleles than any other measured",
     "The pressure was severe in the year the losses occurred",
     "The population had declined in size in previous years as well",
     "The pressure has affected other species in the same habitat"], ans=0,
   why="Skill 6.C asks for reasoning connecting evidence to a claim, which cuts both ways. EK 7.11.A.1 predicts that greater diversity makes a population more resilient, so a diverse population faring just as badly under the same pressure is the observation that prediction most struggles with."),

 dict(q="A conservation manager can add individuals from a separate wild population to a small, genetically uniform population. Which justification for doing so follows from the framework's account?",
   choices=[
     "Adding distinct alleles raises the chance that some individuals can withstand a future pressure",
     "Adding individuals raises the mutation rate of the population",
     "Adding individuals guarantees that the population will not decline",
     "Adding individuals removes the deleterious alleles already present",
     "Adding individuals makes every future environmental change favourable"], ans=0,
   why="EK 7.11.A.1 states that diverse populations are more resilient because they are more likely to contain individuals that can withstand the pressure. Raising the number of distinct alleles present is what raises that likelihood; nothing in the statement licenses a guarantee."),

 dict(q="The table reports the number of distinct alleles detected in each of four populations of one species and how each fared in the same outbreak. What relationship do the two measured variables show?",
   table=_T_DIVERSITY,
   choices=[
     "The more distinct alleles a population carries, the larger the percentage of it that survived",
     "The more distinct alleles a population carries, the smaller the percentage of it that survived",
     "The two variables are unrelated across these populations",
     "Survival was the same in all four populations",
     "Survival rose with allele number only in the two least diverse populations"], ans=0,
   why="Skill 4.B asks for the relationship between the variables. Reading the populations in order of allele number, the survival percentage rises without exception, which is the pattern EK 7.11.A.1 predicts."),

 dict(q="Which population in that same table does the framework's account identify as at the greatest risk of decline?",
   table=_T_DIVERSITY,
   choices=["Population 1", "Population 2", "Population 3", "Population 4",
            "All four are at equal risk, because they belong to one species"], ans=0,
   why="EK 7.11.A.1 states that species and populations with little genetic diversity are at risk of decline or extinction. The population carrying the fewest distinct alleles is the one the statement singles out, and its survival in the outbreak was also the lowest recorded."),

 dict(q="Using the same four populations, by how many percentage points does survival in the most diverse population exceed survival in the least diverse one?",
   table=_T_DIVERSITY,
   choices=["53 percentage points", "58 percentage points", "5 percentage points",
            "41 percentage points", "23 percentage points"], ans=0,
   why="Skill 5.A includes percentages and percent changes. The two rows are located by the number of distinct alleles they report, and the answer is the difference between their survival percentages."),

 dict(q="Which statement best uses the data from those four populations to justify the claim that genetic diversity influences a population's ability to respond to environmental change?",
   table=_T_DIVERSITY,
   choices=[
     "Survival rose with the number of distinct alleles across all four populations, which is the pattern the claim predicts",
     "One population survived the outbreak, which shows that diversity is not needed",
     "The four populations belong to one species, which shows that diversity does not vary",
     "The outbreak affected every population, so diversity made no difference",
     "The population with the fewest alleles survived best, which is the pattern the claim predicts"], ans=0,
   why="Skill 6.C asks for reasoning that connects evidence to a claim. EK 7.11.A.1 predicts that more diversity makes a population better able to withstand a pressure, so the justification must point to the co-variation across the whole set rather than to a single population."),

 dict(q="The table reports how individuals carrying allele T and individuals lacking it fared under two different environmental conditions. In which condition is carrying allele T associated with higher survival?",
   table=_T_ALLELE,
   choices=["The cool and wet season", "The hot and dry season",
            "Both conditions equally", "Neither condition",
            "The table does not report survival for individuals carrying allele T"], ans=0,
   why="Skill 4.B, identifying specific data points and comparing them. In exactly one row the survival of individuals carrying the allele exceeds that of individuals lacking it, and that row's condition is the answer."),

 dict(q="In the hot and dry season recorded in that same table, by how many percentage points does survival of individuals carrying allele T fall below survival of those lacking it?",
   table=_T_ALLELE,
   choices=["45 percentage points", "38 percentage points", "31 percentage points",
            "76 percentage points", "107 percentage points"], ans=0,
   why="Skill 5.A includes percentages. The stem names one row, and the answer is the difference between the two survival percentages recorded in it."),

 dict(q="Which statement of the framework do the survival data for allele T in the two conditions most directly illustrate?",
   table=_T_ALLELE,
   choices=[
     "An allele adaptive in one environmental condition may be deleterious in another because of different selective pressures",
     "Populations with little genetic diversity are at risk of decline or extinction",
     "Genetically diverse populations are more likely to contain individuals that can withstand a pressure",
     "The level of variation in a population has no effect on population dynamics",
     "An allele has the same effect on survival in every environment"], ans=0,
   why="EK 7.11.A.1 states that alleles adaptive in one environmental condition may be deleterious in another because of different selective pressures. The table shows the same allele associated with higher survival in one condition and lower survival in the other, which is that statement."),

 dict(q="What follows from the data on allele T about whether it should be described as a beneficial allele for the species?",
   choices=[
     "It cannot be described as beneficial without naming the environmental condition, because its effect reverses between conditions",
     "It is beneficial, because it raised survival in one of the two conditions measured",
     "It is deleterious, because it lowered survival in one of the two conditions measured",
     "It is neutral, because the two effects are of similar size",
     "No description is possible, because survival cannot be measured"], ans=0,
   why="EK 7.11.A.1 makes the adaptive or deleterious character of an allele depend on the environmental condition and the selective pressures it imposes. An allele whose effect reverses between conditions has no single description independent of the condition."),

 dict(q="Why does an allele that is deleterious under present conditions still contribute to a population's resilience under the framework's account?",
   choices=[
     "Conditions can change, and an allele deleterious now may be the one that allows survival under a different pressure",
     "Deleterious alleles raise the mutation rate of the population",
     "Deleterious alleles are the only alleles that can be inherited",
     "A deleterious allele becomes beneficial as soon as it becomes common",
     "Deleterious alleles have no effect on survival in any condition"], ans=0,
   why="EK 7.11.A.1 states both that alleles adaptive in one condition may be deleterious in another and that diverse populations are more likely to contain individuals that can withstand a pressure. Variation that looks useless under present conditions is part of the variety the second statement relies on."),

 dict(q="Two populations of one species face a new pressure. Which piece of information would best predict which population will lose fewer individuals?",
   choices=[
     "How much genetic diversity each population carries",
     "Which population occupies the larger area",
     "Which population was described by biologists first",
     "Which population has the longer generation time",
     "How many other species share each population's habitat"], ans=0,
   why="EK 7.11.A.1 states that the ability of a population to respond to changes in the environment is influenced by genetic diversity and that diverse populations are more resilient. The other four properties are not connected to resilience by any statement in this topic."),

 dict(q="A population is described as having lost most of its genetic diversity, yet it has not declined in numbers over the past decade. Which conclusion is best supported?",
   choices=[
     "It faces a raised risk of decline should a new pressure arise, which the last decade has not tested",
     "The framework's claim about genetic diversity is refuted by this population",
     "Genetic diversity has no effect on any population",
     "The population must in fact be highly diverse",
     "The population will certainly decline within the next decade"], ans=0,
   why="EK 7.11.A.1 frames low diversity as a RISK, which is a claim about what happens when a pressure arrives rather than a prediction of decline in every decade. A period without a new pressure does not test the claim in either direction."),

 dict(q="Which of the following best describes what genetic diversity means for a population, as the framework uses the term?",
   choices=[
     "The variety of alleles present among the individuals that make up the population",
     "The number of individuals the population contains",
     "The number of species living alongside the population",
     "The variety of habitats the population occupies",
     "The number of generations the population has existed"], ans=0,
   why="EK 7.11.A.1 speaks of the level of variation in a population and of alleles that are adaptive or deleterious under different conditions, so the variation at issue is variation among alleles. Abundance, community composition and habitat range are separate properties."),

 dict(q="A researcher argues that because every individual in a population survived the last three environmental changes, the population's genetic diversity is irrelevant to its future. Which flaw does this reasoning contain?",
   choices=[
     "Past pressures that the population happened to withstand say nothing about a future pressure that no present allele counters",
     "Survival of every individual proves that the population has no genetic diversity",
     "The framework denies that populations ever survive environmental change",
     "Genetic diversity is relevant only to populations that have already declined",
     "Three changes are more than enough to establish a general claim"], ans=0,
   why="EK 7.11.A.1 ties resilience to the likelihood of containing individuals that can withstand a pressure, and different pressures call on different alleles. A record of surviving particular pressures is evidence about those pressures and not about the next one."),

 dict(q="Under the framework's account, which pair of populations of one species would be expected to differ most in their ability to withstand a novel pressure?",
   choices=[
     "One in which many distinct alleles are present and one in which nearly every individual is genetically alike",
     "One with a long generation time and one with a short generation time",
     "One occupying a coastal habitat and one occupying an inland habitat",
     "One that has been studied for many years and one recently discovered",
     "One that reproduces in spring and one that reproduces in autumn"], ans=0,
   why="EK 7.11.A.1 makes genetic diversity the property that influences the ability to respond to environmental change. Only the first pair differs in that property; the other four differ in properties the statement does not connect to resilience."),

 dict(q="Why does the framework place this topic under the theme of systems interactions rather than treating variation as a property of individuals?",
   choices=[
     "The claim is about how the variation held across a population affects the population's dynamics as a whole",
     "The claim applies only to individuals and not to populations",
     "Variation cannot be measured in an individual organism",
     "Populations are the only biological systems that exist",
     "The theme determines which alleles are adaptive"], ans=0,
   why="EK 7.11.A.1 states that the LEVEL OF VARIATION IN A POPULATION affects POPULATION DYNAMICS, which relates a property of the whole group to an outcome for the whole group. An individual either carries an allele or does not; only a population has a level of variation."),

 dict(q="A pressure arrives that no allele present in a genetically diverse population happens to counter. What does the framework's account predict?",
   choices=[
     "The population may still suffer heavy losses, because diversity raises the chance of resistance without assuring it",
     "The population will be unaffected, because diverse populations always survive",
     "The population will immediately generate a new allele that counters the pressure",
     "The population's diversity will rise as a result of the pressure",
     "The pressure will affect only the individuals carrying the rarest alleles"], ans=0,
   why="EK 7.11.A.1 says a diverse population is MORE LIKELY to contain individuals that can withstand the pressure, which leaves room for a pressure that none of the alleles present happens to counter. Nothing in the statement supplies alleles on demand."),

 dict(q="Taken together, what do the framework's statements about variation in populations assert?",
   choices=[
     "Genetic diversity influences how a population responds to environmental change, low diversity raises the risk of decline, and an allele's value depends on the conditions",
     "Genetic diversity determines the number of individuals a population contains",
     "Genetic diversity has the same effect on every population regardless of the pressure",
     "An allele is either beneficial or deleterious in all environments alike",
     "Populations with low genetic diversity are certain to become extinct"], ans=0,
   why="The three parts of EK 7.11.A.1 assert exactly those three things: diversity influences the ability to respond, little diversity brings a risk of decline or extinction, and an allele adaptive in one condition may be deleterious in another. Certainty and uniformity across environments are both stronger than what is stated."),
]
