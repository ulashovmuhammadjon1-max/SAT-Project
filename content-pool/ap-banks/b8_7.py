# AP BIOLOGY 8.7 Disruptions in Ecosystems
# CED effective Fall 2025, Unit 8 Ecology. Big Idea 1 Evolution for LO 8.7.A
# and Big Idea 4 Systems Interactions for LO 8.7.B, 8.7.C and 8.7.D.
# Learning objectives 8.7.A (explain the interaction between the environment
# and random or preexisting variations in populations), 8.7.B (explain how
# invasive species affect ecosystem dynamics), 8.7.C (describe human activities
# that lead to changes in ecosystem structure and dynamics) and 8.7.D (explain
# how geological and meteorological activity leads to changes in ecosystem
# structure and dynamics).
# Suggested skill 5.D, USE DATA TO EVALUATE A HYPOTHESIS OR PREDICTION,
# including rejecting or failing to reject the null hypothesis.
#
# Essential knowledge relied on, in the framework's own terms:
#   8.7.A.1  an ADAPTATION is a GENETIC VARIATION that is FAVORED BY SELECTION
#            and MANIFESTS AS A TRAIT that provides an ADVANTAGE to an organism
#            IN A PARTICULAR ENVIRONMENT.
#   8.7.A.2  HETEROZYGOTE ADVANTAGE is when the HETEROZYGOUS GENOTYPE HAS A
#            HIGHER RELATIVE FITNESS than either the homozygous dominant or the
#            homozygous recessive genotype.
#   8.7.A.3  MUTATIONS ARE NOT DIRECTED BY SPECIFIC ENVIRONMENTAL PRESSURES.
#   8.7.B.1  the INTENTIONAL OR UNINTENTIONAL introduction of an invasive
#            species can allow the species to EXPLOIT A NEW NICHE FREE OF
#            PREDATORS OR COMPETITORS or to OUTCOMPETE NATIVE SPECIES FOR
#            RESOURCES.
#   8.7.C.1  HUMAN IMPACT ACCELERATES CHANGES AT LOCAL AND GLOBAL LEVELS. These
#            activities can drive changes in ecosystems, such as the following,
#            that cause extinctions to occur: (i) BIOMAGNIFICATION,
#            (ii) EUTROPHICATION.
#   8.7.D.1  GEOLOGICAL AND METEOROLOGICAL EVENTS AFFECT HABITAT CHANGE AND
#            ECOSYSTEM DISTRIBUTION. BIOGEOGRAPHICAL STUDIES illustrate these
#            changes.
#
# WHAT THE CED LISTS AND WHAT IT DOES NOT. EK 8.7.C.1 names exactly two changes,
# biomagnification and eutrophication, and its illustrative examples -- Kudzu,
# zebra mussels, Dutch elm disease, potato blight, global climate change,
# logging, urbanization, monocropping, El Nino, continental drift, the meteor
# impact on dinosaurs -- are not assessable content. So no key here depends on
# recognising a named species or event, and no key adds a third item to the
# framework's list of two.
#
# DELIBERATE OMISSIONS, because two neighbours are close.
#  * EK 7.11.A.1 (an allele adaptive in one condition may be deleterious in
#    another) is asked in b7_11, so no item here turns on an allele's effect
#    reversing between environments. The adaptation items here ask what the
#    DEFINITION in EK 8.7.A.1 requires.
#  * Genetic drift, mutation as a source of variation and gene flow are
#    EK 7.4.A.1 and belong to a sibling's module; the single item here on
#    mutation is keyed to EK 8.7.A.3's own sentence about direction.
#  * Keystone species and ecosystem resilience are EK 8.6 and are asked in
#    b8_6; the disruptions here are invasive species, human activity and
#    geological or meteorological events, which are this topic's own subjects.
#
# ON THE DATA. All three tables are hypothetical and say so, and every number a
# key states is recomputed in verify_b8_7.py from that table alone. The
# suggested skill for this topic is evaluating a hypothesis against data, so
# three items ask what the data license and what they do not.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: this bank is exported
# untypeset.
TOPIC = ("8.7", "Disruptions in Ecosystems", 8)

_T_HET = dict(
    headers=["Genotype at the locus studied",
             "Relative fitness measured in one hypothetical environment"],
    rows=[["Homozygous dominant", "0.80"],
          ["Heterozygous", "1.00"],
          ["Homozygous recessive", "0.35"]])

_T_INVASIVE = dict(
    headers=["Year of the survey",
             "Individuals of the introduced species counted per plot",
             "Native species recorded per plot"],
    rows=[["Year 1", "4", "12"],
          ["Year 2", "60", "9"],
          ["Year 3", "210", "5"],
          ["Year 4", "480", "2"]])

_T_BIOMAG = dict(
    headers=["Trophic level sampled",
             "Concentration of a persistent compound in tissue, in parts per million"],
    rows=[["Producers", "0.04"],
          ["Primary consumers", "0.4"],
          ["Secondary consumers", "4"],
          ["Tertiary consumers", "40"]])

QUESTIONS = [
 dict(q="According to the course framework, what is an adaptation?",
   choices=[
     "A genetic variation favored by selection that manifests as a trait providing an advantage in a particular environment",
     "Any change an organism makes during its lifetime to suit its surroundings",
     "A trait that appears in response to an environmental pressure that requires it",
     "Any difference between two individuals of the same species",
     "A change in the number of individuals in a population"], ans=0,
   why="EK 8.7.A.1 gives that definition in as many words. Every part of it does work: the variation must be genetic, it must be favored by selection, and the advantage it confers is relative to a particular environment."),

 dict(q="An individual becomes better able to withstand a stress during its own lifetime, but the change is not heritable. Why is this not an adaptation under the framework's definition?",
   choices=[
     "The definition requires a genetic variation, and this change is not one",
     "The definition requires the change to be harmful",
     "The definition applies only to populations that are declining",
     "The definition requires the change to occur in every individual at once",
     "The definition applies only to organisms known from fossils"], ans=0,
   why="EK 8.7.A.1 defines an adaptation as a GENETIC VARIATION favored by selection that manifests as a trait. A change that is not heritable cannot be favored by selection across generations, which is what the definition requires."),

 dict(q="Which two conditions does the framework's definition require before a genetic variation counts as an adaptation?",
   choices=[
     "It must be favored by selection and must manifest as a trait that provides an advantage",
     "It must be common in the population and must be recently arisen",
     "It must be rare in the population and must be dominant",
     "It must be harmful in one environment and beneficial in another",
     "It must be present in every individual of the species"], ans=0,
   why="EK 8.7.A.1 states that an adaptation is a genetic variation FAVORED BY SELECTION that MANIFESTS AS A TRAIT providing an advantage in a particular environment. Frequency, dominance and age of the variation are not part of the definition."),

 dict(q="According to the framework, what is heterozygote advantage?",
   choices=[
     "When the heterozygous genotype has a higher relative fitness than either homozygous genotype",
     "When the homozygous dominant genotype has the highest relative fitness",
     "When the homozygous recessive genotype has the highest relative fitness",
     "When all three genotypes have equal relative fitness",
     "When the heterozygous genotype is the most common in the population"], ans=0,
   why="EK 8.7.A.2 states that heterozygote advantage is when the heterozygous genotype has a higher relative fitness than either the homozygous dominant or the homozygous recessive genotype. It is a claim about fitness, not about frequency."),

 dict(q="A population is described as showing heterozygote advantage at a locus. What follows about the relative fitness of the three genotypes?",
   choices=[
     "The heterozygote's relative fitness exceeds that of both homozygotes",
     "The heterozygote's relative fitness lies between those of the two homozygotes",
     "The two homozygotes have equal relative fitness",
     "The homozygous recessive genotype has the highest relative fitness",
     "Relative fitness cannot be compared among genotypes"], ans=0,
   why="EK 8.7.A.2 requires the heterozygous genotype to have a higher relative fitness than EITHER homozygote, so it must exceed both. The statement says nothing about how the two homozygotes compare with each other."),

 dict(q="According to the framework, what is true of mutations?",
   choices=[
     "They are not directed by specific environmental pressures",
     "They arise only when an environmental pressure requires them",
     "They always increase the fitness of the organism carrying them",
     "They occur only in populations that are already declining",
     "They are directed by the needs of the individual organism"], ans=0,
   why="EK 8.7.A.3 states that mutations are not directed by specific environmental pressures. The remaining options each assert some form of direction by need, which is exactly what that sentence denies."),

 dict(q="A population meets a new environmental pressure. Which prediction does the framework's statement about mutation rule out?",
   choices=[
     "That the pressure will cause the mutations needed to withstand it to arise",
     "That some individuals may already carry variation that helps them withstand it",
     "That selection may act on whatever variation is present",
     "That the frequency of a helpful variant may rise over generations",
     "That the population may decline if no helpful variation is present"], ans=0,
   why="EK 8.7.A.3 states that mutations are not directed by specific environmental pressures, which rules out the pressure producing the mutation that answers it. Selection acting on variation that is already present is a different claim and is not excluded."),

 dict(q="What does the framework's statement that mutations are not directed by environmental pressures NOT deny?",
   choices=[
     "That selection can favour a variation that happens to be advantageous under a pressure",
     "That an environment can call forth the variation it requires",
     "That mutation rates rise in exactly the genes a pressure concerns",
     "That organisms can choose which mutations to acquire",
     "That an environmental pressure determines which mutation occurs"], ans=0,
   why="EK 8.7.A.3 denies direction of mutation by pressure; it says nothing against selection, which EK 8.7.A.1 makes the process that favours advantageous variation. The four distractors are all restatements of the direction the sentence rules out."),

 dict(q="According to the framework, how may an invasive species be introduced to an ecosystem?",
   choices=["Intentionally or unintentionally", "Only intentionally",
            "Only unintentionally", "Only by geological events",
            "Only by the movement of native species"], ans=0,
   why="EK 8.7.B.1 states that the INTENTIONAL OR UNINTENTIONAL introduction of an invasive species can allow it to exploit a new niche or outcompete native species. Both routes are named in the same sentence."),

 dict(q="According to the framework, what may the introduction of an invasive species allow that species to do?",
   choices=[
     "Exploit a new niche free of predators or competitors, or outcompete native species for resources",
     "Increase the number of native species present",
     "Restore an ecosystem that has already collapsed",
     "Prevent all further change in the ecosystem",
     "Direct the mutations that arise in native populations"], ans=0,
   why="EK 8.7.B.1 names exactly those two possibilities: exploiting a new niche free of predators or competitors, and outcompeting native species for resources. Nothing in the statement suggests an increase in native species or a restoration."),

 dict(q="An introduced species spreads rapidly in a new range where nothing consumes it and no established species uses the same resources. Which part of the framework's account of invasive species does this illustrate?",
   choices=[
     "Exploiting a new niche free of predators or competitors",
     "Outcompeting native species for resources",
     "Accelerating change at local and global levels through human activity",
     "Biomagnification of a persistent compound",
     "Habitat change caused by a geological event"], ans=0,
   why="EK 8.7.B.1 names two routes, and the scenario describes the first: a niche free of predators or competitors. Outcompeting native species would require the species to be taking resources from established populations, which the scenario excludes."),

 dict(q="According to the framework, what does human impact do to changes in ecosystems?",
   choices=["It accelerates changes at local and global levels",
            "It slows changes at every level", "It affects only local changes",
            "It affects only global changes", "It has no measurable effect on ecosystems"], ans=0,
   why="EK 8.7.C.1 states that human impact accelerates changes at local and global levels. Both scales are named, so any option restricting the claim to one of them contradicts the sentence."),

 dict(q="Which of the following changes in ecosystems does the framework name as driven by human activities and able to cause extinctions?",
   choices=["Biomagnification", "Continental drift", "Heterozygote advantage",
            "Speciation", "Genetic drift"], ans=0,
   why="EK 8.7.C.1 names biomagnification and eutrophication as the two such changes. Continental drift is a geological event under EK 8.7.D.1, and the remaining options are Unit 7 processes."),

 dict(q="Besides biomagnification, which change does the framework name among human activities that can drive extinctions?",
   choices=["Eutrophication", "Punctuated equilibrium", "Nitrogen fixation",
            "Convergent evolution", "Adaptive radiation"], ans=0,
   why="EK 8.7.C.1 lists exactly two such changes, biomagnification and eutrophication. Nitrogen fixation is a step of the nitrogen cycle in EK 8.2.B.6 and the rest are evolutionary processes from Unit 7."),

 dict(q="How many changes driven by human activities does the framework list as causing extinctions to occur?",
   choices=["Two", "One", "Three", "Four", "Five"], ans=0,
   why="EK 8.7.C.1 introduces its list with the words such as the following and then prints two items, biomagnification and eutrophication. The list is what the framework supplies, and no key in this topic may add to it."),

 dict(q="According to the framework, what do geological and meteorological events affect?",
   choices=["Habitat change and ecosystem distribution",
            "The direction in which mutations arise",
            "The definition of an adaptation",
            "The relative fitness of a heterozygous genotype only",
            "Nothing, since ecosystems are unaffected by physical events"], ans=0,
   why="EK 8.7.D.1 states that geological and meteorological events affect habitat change and ecosystem distribution. Directing mutation is what EK 8.7.A.3 explicitly denies of any environmental pressure."),

 dict(q="According to the framework, what kind of study illustrates the changes that geological and meteorological events bring about?",
   choices=["Biogeographical studies", "Studies of relative fitness in one population",
            "Studies of mutation rates in the laboratory",
            "Studies of the number of chromosomes in a species",
            "Studies of a single individual over its lifetime"], ans=0,
   why="EK 8.7.D.1 states that biogeographical studies illustrate these changes. Biogeography concerns where organisms are found, which is the aspect of an ecosystem that habitat change and shifting distribution alter."),

 dict(q="Under the framework's suggested skill for this topic, what is the role of a null hypothesis when data are used to evaluate a prediction?",
   choices=[
     "It states what would be observed if the proposed effect were absent, so the data are judged against it",
     "It states the result the investigator expects to find",
     "It is the conclusion that follows once the data are collected",
     "It is a prediction that no data could bear on",
     "It is the same statement as the prediction being tested"], ans=0,
   why="Skill 5.D asks a student to use data to evaluate a hypothesis or prediction, including rejecting or failing to reject the null hypothesis. A null hypothesis is the no-effect expectation the observations are compared against, which is why it is not the investigator's own prediction."),

 dict(q="The table reports the relative fitness of three genotypes at one locus in a hypothetical environment. Do these data show heterozygote advantage, and why?",
   table=_T_HET,
   choices=[
     "Yes, because the heterozygote's relative fitness exceeds that of both homozygotes",
     "No, because the heterozygote's relative fitness lies between the two homozygotes",
     "No, because relative fitness cannot be compared across genotypes",
     "Yes, because the homozygous recessive genotype has the lowest relative fitness",
     "No, because the two homozygotes differ from each other"], ans=0,
   why="EK 8.7.A.2 defines heterozygote advantage as the heterozygous genotype having a higher relative fitness than either homozygote. The table's three values are compared directly, and a difference between the two homozygotes is beside the point."),

 dict(q="Which genotype in that table has the highest relative fitness in the environment studied?",
   table=_T_HET,
   choices=["The heterozygous genotype", "The homozygous dominant genotype",
            "The homozygous recessive genotype", "All three are equal",
            "The table does not report relative fitness"], ans=0,
   why="Skill 4.B, identifying a specific data point. Reading down the relative fitness column and taking the largest value identifies the genotype, which is the comparison EK 8.7.A.2 turns on."),

 dict(q="By how much does the relative fitness of the heterozygous genotype exceed that of the homozygous dominant genotype in that table?",
   table=_T_HET,
   choices=["0.20", "0.65", "0.35", "0.45", "0.80"], ans=0,
   why="Skill 5.A includes differences. The two rows named by the stem each report a relative fitness, and the answer is the difference between them; the difference from the other homozygote is one of the distractors."),

 dict(q="The table reports four yearly surveys of plots into which a species was introduced. What pattern do the two counted variables show?",
   table=_T_INVASIVE,
   choices=[
     "The introduced species rose in every year while the number of native species fell in every year",
     "Both counts rose in every year",
     "Both counts fell in every year",
     "The introduced species fell while the native species rose",
     "Neither count changed over the four years"], ans=0,
   why="Skill 4.B asks for the trend and the relationship between variables. Reading the two columns down the years, one rises at every step and the other falls at every step."),

 dict(q="In which year of that survey were the most individuals of the introduced species counted per plot?",
   table=_T_INVASIVE,
   choices=["Year 4", "Year 1", "Year 2", "Year 3",
            "The counts were equal in every year"], ans=0,
   why="Skill 4.B, identifying a specific data point. The largest entry in the column for the introduced species belongs to one year, and that year also records the fewest native species."),

 dict(q="A null hypothesis is stated for that survey: the introduced species has no effect on the number of native species per plot. What do these data support?",
   table=_T_INVASIVE,
   choices=[
     "Rejecting the null hypothesis, because native species fell steadily as the introduced species rose",
     "Failing to reject the null hypothesis, because the two counts changed together",
     "Accepting the null hypothesis as proven",
     "Neither rejecting nor evaluating it, because counts cannot be compared",
     "Rejecting the null hypothesis, because the introduced species itself increased"], ans=0,
   why="Skill 5.D asks a student to use data to evaluate a hypothesis, including rejecting or failing to reject the null. A steady fall in native species alongside a steady rise in the introduced species is the opposite of what no effect predicts; a rise in the introduced species alone would say nothing about the natives."),

 dict(q="What does the framework's account of invasive species suggest is happening in those plots?",
   table=_T_INVASIVE,
   choices=[
     "The introduced species may be outcompeting native species for resources",
     "The introduced species is restoring the plots to their original condition",
     "Human activity has slowed the rate of change in the plots",
     "A geological event has changed the distribution of the ecosystem",
     "The native species are directing mutations in the introduced species"], ans=0,
   why="EK 8.7.B.1 states that an introduced invasive species may exploit a new niche free of predators or competitors or outcompete native species for resources. Native species falling as the introduced species rises fits the second of those two; EK 8.7.A.3 rules out the last option outright."),

 dict(q="The table reports the concentration of a persistent compound measured in tissue at four trophic levels of a hypothetical ecosystem. At which level is the concentration highest?",
   table=_T_BIOMAG,
   choices=["Tertiary consumers", "Producers", "Primary consumers",
            "Secondary consumers", "The concentration is the same at every level"], ans=0,
   why="Skill 4.B, identifying a specific data point. Reading down the concentration column and taking the largest value identifies the level, which is the topmost level the table samples."),

 dict(q="By what factor does the concentration in that table rise from each trophic level to the one above it?",
   table=_T_BIOMAG,
   choices=["10 times", "4 times", "40 times", "100 times", "0.1 times"], ans=0,
   why="Skill 5.A includes ratios. Dividing each level's concentration by the level below it gives the same factor at every step, which is what makes a single number the right description of these data."),

 dict(q="Which of the changes the framework names as driven by human activities do those concentration data illustrate?",
   table=_T_BIOMAG,
   choices=["Biomagnification", "Eutrophication", "Heterozygote advantage",
            "The introduction of an invasive species", "A meteorological event"], ans=0,
   why="EK 8.7.C.1 names biomagnification and eutrophication as changes driven by human activities that can cause extinctions. A persistent compound rising in concentration at each successive trophic level is what the first of those two names."),

 dict(q="A second survey finds no difference in native species counts between plots with and without an introduced species. Under the framework's suggested skill, what is the correct description of that result?",
   choices=[
     "The data fail to reject the null hypothesis of no effect, which is not the same as proving there is none",
     "The data prove that the introduced species has no effect",
     "The data reject the null hypothesis of no effect",
     "The data show that the introduced species benefits the native species",
     "The data cannot bear on the question at all"], ans=0,
   why="Skill 5.D names rejecting or FAILING TO REJECT the null hypothesis as the two outcomes. Failing to reject is a statement about what the data establish, and it leaves open that an effect exists but was not detected by this survey."),

 dict(q="Taken together, what kinds of disruption to ecosystems does this topic identify?",
   choices=[
     "The introduction of invasive species, human activities such as biomagnification and eutrophication, and geological and meteorological events",
     "Only the introduction of invasive species",
     "Only human activities",
     "Only geological and meteorological events",
     "Only changes that are directed by the needs of the organisms affected"], ans=0,
   why="EK 8.7.B.1 supplies invasive species, EK 8.7.C.1 human impact with its two named changes, and EK 8.7.D.1 geological and meteorological events. EK 8.7.A.3 separately rules out any account in which the changes are directed by what organisms need."),
]
