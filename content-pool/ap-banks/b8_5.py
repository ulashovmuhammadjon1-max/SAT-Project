# AP BIOLOGY 8.5 Community Ecology
# CED effective Fall 2025, Unit 8 Ecology, Big Idea 2 Energetics.
# Learning objectives 8.5.A (describe the structure of a community according to
# its species composition and diversity) and 8.5.B (explain how interactions
# within and among populations influence community structure).
# Suggested skill 5.B, USE CONFIDENCE INTERVALS AND ERROR BARS to estimate
# whether sample means are statistically different.
#
# Essential knowledge relied on, in the framework's own terms:
#   8.5.A.1  the structure of a community is measured and described in terms of
#            SPECIES COMPOSITION and SPECIES DIVERSITY.
#            RELEVANT EQUATION: Simpson's Diversity Index equals 1 minus the sum
#            over species of the square of n divided by N, where n is the total
#            number of organisms of a particular species and N the total number
#            of organisms of all species.
#   8.5.B.1  communities are groups of INTERACTING POPULATIONS OF DIFFERENT
#            SPECIES that CHANGE OVER TIME based on the interactions between
#            those populations.
#   8.5.B.2  interactions among populations determine HOW THEY ACCESS ENERGY
#            AND MATTER within a community.
#   8.5.B.3  relationships among interacting populations can be characterized by
#            POSITIVE AND NEGATIVE EFFECTS and CAN BE MODELED. Examples include
#            PREDATOR AND PREY INTERACTIONS, COOPERATION, TROPHIC CASCADES, and
#            NICHE PARTITIONING.
#   8.5.B.4  COMPETITION, PREDATION, and SYMBIOSES, INCLUDING PARASITISM,
#            MUTUALISM, AND COMMENSALISM, can drive population dynamics.
#
# ON THE THREE SYMBIOSES. EK 8.5.B.4 names parasitism, mutualism and
# commensalism and defines none of them, exactly as EK 7.10.C.2 names
# pre-zygotic and post-zygotic mechanisms without listing any. What the CED does
# supply is EK 8.5.B.3's statement that relationships among interacting
# populations can be characterized by POSITIVE AND NEGATIVE EFFECTS. Every
# classification item here therefore states the effect on each population in the
# stem and asks which named relationship that pattern is, so the key rests on
# the framework's own characterization plus the ordinary meaning of the term,
# and the verifier's claim says so rather than pretending to a printed
# definition.
#
# ON THE ARITHMETIC. Simpson's index is one of the few things a machine can
# settle in this subject, so every index any key states is RECOMPUTED in
# verify_b8_5.py from the counts in the table alone. All three communities hold
# ten individuals, which keeps every square exact and the whole calculation
# calculator-free.
#
# DELIBERATE OMISSIONS. Ecosystem diversity and resilience, keystone species and
# the collapse that follows their removal are EK 8.6.A and EK 8.6.B and are
# asked in b8_6; NOTHING here mentions a keystone species or the resilience of
# an ecosystem. Genetic diversity within a population is EK 7.11.A.1 and is
# asked in b7_11. Cooperative behaviour raising individual fitness is
# EK 8.1.B.2 and is asked in b8_1; the cooperation item here is keyed to
# EK 8.5.B.3's list of relationships among populations, which is a different
# statement. Trophic levels and energy flow are EK 8.2 and are asked in b8_2.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: this bank is exported
# untypeset, so the equation is written out in words.
TOPIC = ("8.5", "Community Ecology", 8)

_T_COMM = dict(
    headers=["Community sampled", "Individuals of species P", "Individuals of species Q",
             "Individuals of species R", "Individuals of species S"],
    rows=[["Community X", "5", "3", "2", "0"],
          ["Community Y", "8", "1", "1", "0"],
          ["Community Z", "4", "3", "2", "1"]])

_T_ERROR = dict(
    headers=["Site sampled", "Mean number of species recorded per plot",
             "Lower end of the error bar", "Upper end of the error bar"],
    rows=[["Site 1", "12", "10", "14"],
          ["Site 2", "13", "11", "15"],
          ["Site 3", "22", "20", "24"]])

QUESTIONS = [
 dict(q="According to the course framework, the structure of a community is measured and described in terms of what?",
   choices=["Species composition and species diversity",
            "The total mass of all individuals present",
            "The age of the habitat the community occupies",
            "The number of individuals of the single most common species",
            "The rate at which the community's populations reproduce"], ans=0,
   why="EK 8.5.A.1 states that the structure of a community is measured and described in terms of species composition and species diversity. Total mass, habitat age and reproductive rate are not what that statement names."),

 dict(q="In the diversity index the framework prints for this topic, what does n represent?",
   choices=["The total number of organisms of a particular species",
            "The total number of organisms of all species",
            "The number of species present in the community",
            "The number of communities being compared",
            "The number of plots sampled"], ans=0,
   why="The CED defines n as the total number of organisms of a particular species and N as the total number of organisms of all species. The two are easy to exchange, which is why both appear as options."),

 dict(q="In the same diversity index, what does N represent?",
   choices=["The total number of organisms of all species",
            "The total number of organisms of a particular species",
            "The number of species present in the community",
            "The number of individuals in the rarest species",
            "The number of sites sampled"], ans=0,
   why="The CED defines N as the total number of organisms of all species in the index for this topic. It is the denominator each species count is divided by before squaring."),

 dict(q="Two communities contain the same number of species and the same total number of individuals, but in one the individuals are spread evenly among the species while in the other a single species holds most of them. Which community has the larger value of the framework's diversity index?",
   choices=[
     "The community in which the individuals are spread evenly among the species",
     "The community in which a single species holds most of the individuals",
     "The two communities must have the same value, because they hold the same number of species",
     "The two communities must have the same value, because they hold the same number of individuals",
     "Neither, because the index cannot be calculated when species counts differ"], ans=0,
   why="The index subtracts from one the sum of the squared proportions. Concentrating individuals into one species makes one proportion large, and squaring a large proportion contributes far more to that sum than squaring several small ones, so the subtracted quantity is larger and the index smaller."),

 dict(q="According to the framework, what are communities?",
   choices=[
     "Groups of interacting populations of different species that change over time based on those interactions",
     "Groups of individuals of a single species",
     "The non-living components of a habitat",
     "All the ecosystems within one biome",
     "Groups of species that never interact with one another"], ans=0,
   why="EK 8.5.B.1 states that communities are groups of interacting populations of different species that change over time based on the interactions between those populations. A group of individuals of one species is a population, which EK 8.3.A.1 defines separately."),

 dict(q="According to the framework, what do interactions among populations determine within a community?",
   choices=["How those populations access energy and matter",
            "The age of the rocks beneath the community",
            "The number of chromosomes each species carries",
            "The total rainfall the habitat receives",
            "Nothing, because populations act independently"], ans=0,
   why="EK 8.5.B.2 states that interactions among populations determine how they access energy and matter within a community. That is the link between community structure and the energy flow of EK 8.2."),

 dict(q="According to the framework, how can relationships among interacting populations be characterized and studied?",
   choices=[
     "By their positive and negative effects, and they can be modeled",
     "Only by counting the individuals of each species",
     "Only by observing them without any attempt to model them",
     "By the age of each population rather than by its effects",
     "They cannot be characterized, because every relationship is unique"], ans=0,
   why="EK 8.5.B.3 states that relationships among interacting populations can be characterized by positive and negative effects and can be modeled. Both halves of that sentence are asserted."),

 dict(q="Which of the following does the framework list as an example of a relationship among interacting populations?",
   choices=["Niche partitioning", "Photosynthesis", "Nitrogen fixation",
            "Genetic drift", "Allopatric speciation"], ans=0,
   why="EK 8.5.B.3 lists predator and prey interactions, cooperation, trophic cascades, and niche partitioning as examples. Photosynthesis and nitrogen fixation belong to EK 8.2's cycles, and drift and allopatry to Unit 7."),

 dict(q="One population consumes individuals of another, and the numbers of the two rise and fall in a related way over successive years. Which of the framework's listed examples does this best illustrate?",
   choices=["A predator and prey interaction", "Niche partitioning", "Cooperation",
            "A trophic cascade", "Commensalism"], ans=0,
   why="EK 8.5.B.3 lists predator and prey interactions among its examples of relationships among interacting populations. One population consuming another, with linked changes in their numbers over time, is that relationship."),

 dict(q="Two populations in a community act together in a way that leaves each of them better able to obtain resources than either would be alone. Which of the framework's listed examples does this best illustrate?",
   choices=["Cooperation", "A predator and prey interaction", "A trophic cascade",
            "Niche partitioning", "Parasitism"], ans=0,
   why="EK 8.5.B.3 lists cooperation among its examples of relationships among interacting populations. The effect on both populations is positive, which is how EK 8.5.B.3 says such relationships are characterized."),

 dict(q="The removal of a predator from a community is followed by a rise in the population it consumed and then by a fall in the populations that population feeds on. Which of the framework's listed examples does this best illustrate?",
   choices=["A trophic cascade", "Niche partitioning", "Cooperation",
            "Commensalism", "Mutualism"], ans=0,
   why="EK 8.5.B.3 lists trophic cascades among its examples of relationships among interacting populations. A change at one level passing down through the levels below it is what the term names."),

 dict(q="Two populations in one community use the same broad resource but concentrate on different parts of it, so that each avoids much of the other's use. Which of the framework's listed examples does this best illustrate?",
   choices=["Niche partitioning", "A trophic cascade", "A predator and prey interaction",
            "Parasitism", "Cooperation"], ans=0,
   why="EK 8.5.B.3 lists niche partitioning among its examples of relationships among interacting populations. Dividing a shared resource so that each population uses a different part of it is what the term names."),

 dict(q="Which list names relationships the framework says can drive population dynamics?",
   choices=[
     "Competition, predation, and symbioses including parasitism, mutualism, and commensalism",
     "Photosynthesis, respiration, decomposition, and combustion",
     "Evaporation, condensation, precipitation, and transpiration",
     "Populations, communities, ecosystems, and biomes",
     "Producers, consumers, and decomposers"], ans=0,
   why="EK 8.5.B.4 states that competition, predation, and symbioses, including parasitism, mutualism, and commensalism, can drive population dynamics. The other lists are the carbon cycle, the hydrologic cycle, the ecological levels of organization and the trophic levels."),

 dict(q="In an interaction between two populations, one population benefits and the other is harmed. Which of the symbioses the framework names does this pattern of effects describe?",
   choices=["Parasitism", "Mutualism", "Commensalism", "Competition", "Cooperation"], ans=0,
   why="EK 8.5.B.3 says relationships among interacting populations can be characterized by positive and negative effects, and EK 8.5.B.4 names parasitism, mutualism and commensalism as symbioses. A positive effect on one population and a negative effect on the other is the pattern the first of those three names."),

 dict(q="In an interaction between two populations, both populations benefit. Which of the symbioses the framework names does this pattern of effects describe?",
   choices=["Mutualism", "Parasitism", "Commensalism", "Predation", "Competition"], ans=0,
   why="EK 8.5.B.3's positive and negative effects applied to EK 8.5.B.4's three named symbioses: a positive effect on both populations is what mutualism names. Predation and competition are listed separately from the symbioses in the same statement."),

 dict(q="Two populations interact, and one of them benefits while the other is neither helped nor harmed. Which of the symbioses the framework names does this pattern of effects describe?",
   choices=["Commensalism", "Mutualism", "Parasitism", "Predation", "A trophic cascade"], ans=0,
   why="EK 8.5.B.3's positive and negative effects applied to EK 8.5.B.4's three named symbioses: a positive effect on one population with no effect on the other is what commensalism names, since the other two involve a benefit or a harm to both."),

 dict(q="Two populations require the same limited resource, and the presence of each reduces the amount available to the other. Which relationship named in the framework does this describe?",
   choices=["Competition", "Mutualism", "Commensalism", "A trophic cascade", "Cooperation"], ans=0,
   why="EK 8.5.B.4 names competition among the relationships that can drive population dynamics, and EK 8.5.B.3 characterizes relationships by their effects. Each population reducing what is available to the other is a negative effect in both directions."),

 dict(q="Which of the following is NOT among the relationships the framework names as able to drive population dynamics?",
   choices=["Nitrogen fixation", "Competition", "Predation", "Parasitism", "Mutualism"], ans=0,
   why="EK 8.5.B.4 names competition, predation, and symbioses including parasitism, mutualism, and commensalism. Nitrogen fixation is a step of the nitrogen cycle in EK 8.2.B.6 and is not a relationship between populations."),

 dict(q="The table gives the number of individuals of each species counted in three sampled communities of ten individuals each. What is the value of the framework's diversity index for Community X?",
   table=_T_COMM,
   choices=["0.62", "0.38", "0.34", "0.70", "0.50"], ans=0,
   why="The framework prints the index as one minus the sum of the squares of each species count divided by the total count. Dividing each of the community's counts by ten, squaring, adding and subtracting from one gives the value; the sum itself, before subtraction, is one of the distractors."),

 dict(q="Using the same three sampled communities, which has the largest value of the framework's diversity index?",
   table=_T_COMM,
   choices=["Community Z", "Community X", "Community Y",
            "All three have the same value", "The index cannot be compared across communities"], ans=0,
   why="EK 8.5.A.1 makes species diversity part of what describes community structure, and the index is the framework's measure of it. Computing the index for each row and comparing the three values identifies the largest."),

 dict(q="Using the same three sampled communities, how many species were recorded in Community Y?",
   table=_T_COMM,
   choices=["Three", "One", "Two", "Four", "Ten"], ans=0,
   why="EK 8.5.A.1 makes species composition part of what describes community structure. Counting the columns in which that row records at least one individual gives the number of species present, which is a different quantity from the number of individuals."),

 dict(q="Two of the sampled communities recorded the same number of species and the same number of individuals, yet their values of the diversity index differ. What accounts for the difference?",
   table=_T_COMM,
   choices=[
     "The individuals are distributed differently among the species in the two communities",
     "One community was sampled over a longer period than the other",
     "One community contains a species the other does not",
     "The index depends only on the number of individuals, which must have been miscounted",
     "The index cannot differ when the number of species is the same"], ans=0,
   why="EK 8.5.A.1 measures community structure by composition and diversity together, and the printed index squares each species' share of the total. Two communities with the same richness and the same total can still differ in how evenly the individuals are spread, and squaring makes that difference count."),

 dict(q="Which community in that table would the framework's index describe as the least diverse, and what feature of its counts explains that?",
   table=_T_COMM,
   choices=[
     "Community Y, because most of its individuals belong to a single species",
     "Community Z, because it contains the largest number of species",
     "Community X, because its counts are the most nearly equal",
     "Community Y, because it contains the fewest individuals in total",
     "All three are equally diverse, because each holds ten individuals"], ans=0,
   why="The printed index subtracts the sum of squared shares from one, and one large share contributes more to that sum than several small ones. The row in which one species holds most of the individuals therefore yields the smallest index; every community in the table holds the same total."),

 dict(q="The table reports the mean number of species recorded per plot at three sites, together with the ends of the error bars around each mean. Which two sites have error bars that overlap?",
   table=_T_ERROR,
   choices=["Site 1 and Site 2", "Site 1 and Site 3", "Site 2 and Site 3",
            "All three sites overlap one another", "No two sites overlap"], ans=0,
   why="Skill 5.B asks a student to use error bars to estimate whether sample means are statistically different. Two intervals overlap when the lower end of one falls below the upper end of the other, which can be read directly from the two columns."),

 dict(q="What does that overlap between two of the sites allow a student to conclude about their mean numbers of species per plot?",
   table=_T_ERROR,
   choices=[
     "The data do not support a claim that the two means are different",
     "The two means are certainly identical",
     "The two means are certainly different",
     "The site with the larger mean must have more species in total",
     "No conclusion of any kind can be drawn from error bars"], ans=0,
   why="Skill 5.B asks whether sample means are statistically different. Overlapping intervals leave the observed difference within the range that sampling alone could produce, which is a failure to establish a difference rather than a demonstration of sameness."),

 dict(q="Which site in that table has a mean number of species per plot that the error bars support treating as different from that of Site 1?",
   table=_T_ERROR,
   choices=["Site 3", "Site 2", "Neither of the other two sites",
            "Both of the other two sites", "Site 1 cannot be compared with any other site"], ans=0,
   why="Skill 5.B asks for an estimate of whether sample means are statistically different. Exactly one of the other sites has an interval that does not overlap the interval around the named site, and non-overlapping intervals support treating the means as different."),

 dict(q="By how many species per plot do the means of Site 1 and Site 3 differ?",
   table=_T_ERROR,
   choices=["10 species per plot", "1 species per plot", "9 species per plot",
            "22 species per plot", "12 species per plot"], ans=0,
   why="Skill 5.A includes differences and skill 5.B settles whether the comparison is meaningful. The two named sites have error bars that do not overlap, so the difference between their means is a difference the data support, and that difference is read from the two means."),

 dict(q="A student reports that two sample means differ and concludes that the underlying communities differ. Under the framework's suggested skill for this topic, what is missing from that reasoning?",
   choices=[
     "An estimate of how much the means could differ by sampling alone, which the error bars provide",
     "A count of the total number of individuals sampled at each site",
     "The name of every species recorded at each site",
     "The age of the habitat at each site",
     "Nothing, because any difference between two means is a real difference"], ans=0,
   why="Skill 5.B asks a student to use confidence intervals and error bars to estimate whether sample means are STATISTICALLY different. Two sample means will almost never be exactly equal, so the size of the difference relative to the uncertainty is what the comparison turns on."),

 dict(q="Why can two communities with the same list of species still be described as having different structure?",
   choices=[
     "Structure is described by species composition and species diversity together, and the diversity of the two can differ",
     "Structure depends only on the list of species, so the description must be an error",
     "Structure depends only on the total number of individuals",
     "Structure depends only on the age of the community",
     "Two communities with the same species always have identical structure"], ans=0,
   why="EK 8.5.A.1 states that the structure of a community is measured and described in terms of species composition AND species diversity. Two communities can share a species list and still differ in how the individuals are distributed, which the printed index measures."),

 dict(q="Taken together, what do the framework's statements about communities assert?",
   choices=[
     "A community is interacting populations of different species whose structure is described by composition and diversity and whose relationships, characterized by positive and negative effects, can drive population dynamics",
     "A community is a group of individuals of one species whose structure is fixed over time",
     "A community's structure is described by the total number of individuals alone",
     "A community's populations do not interact, so no relationship can drive population dynamics",
     "A community's relationships cannot be modeled or characterized in any way"], ans=0,
   why="EK 8.5.A.1 supplies the description of structure, EK 8.5.B.1 the definition and the change over time, EK 8.5.B.3 the characterization by positive and negative effects and the possibility of modelling, and EK 8.5.B.4 the driving of population dynamics. Each distractor contradicts one of those statements."),
]
