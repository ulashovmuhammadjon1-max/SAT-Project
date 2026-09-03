# AP BIOLOGY 7.10 Speciation
# CED effective Fall 2025, Unit 7 Natural Selection, Big Idea 1 Evolution.
# Learning objectives 7.10.A (describe the conditions under which new species
# may arise), 7.10.B (describe the rate of evolution and speciation under
# different ecological conditions) and 7.10.C (explain the processes and
# mechanisms that drive speciation).
# Suggested skills 2.B, explain relationships between characteristics of
# biological models in both theoretical and applied contexts, and 6.E, predict
# the causes or effects of a change in, or disruption to, one or more
# components in a biological system.
#
# Essential knowledge relied on, in the framework's own terms:
#   7.10.A.1  speciation occurs when two populations become REPRODUCTIVELY
#             ISOLATED from each other.
#   7.10.A.2  the BIOLOGICAL SPECIES CONCEPT provides a commonly used
#             definition of a species FOR SEXUALLY REPRODUCING ORGANISMS. It
#             states that species can be defined as a group capable of
#             interbreeding and exchanging genetic information to produce
#             VIABLE, FERTILE offspring.
#   7.10.B.1  PUNCTUATED EQUILIBRIUM is when evolution occurs rapidly after a
#             long period of stasis. GRADUALISM is when evolution occurs slowly
#             over hundreds of thousands or millions of years.
#   7.10.B.2  DIVERGENT EVOLUTION occurs when adaptation to new habitats
#             results in phenotypic diversification. Speciation rates can be
#             especially rapid during times of ADAPTIVE RADIATION as new
#             habitats become available.
#   7.10.B.3  CONVERGENT EVOLUTION occurs when similar selective pressures
#             result in similar phenotypic adaptations in different populations
#             or species.
#   7.10.C.1  SYMPATRIC speciation occurs in populations with GEOGRAPHIC
#             OVERLAP. ALLOPATRIC speciation occurs in populations that are
#             GEOGRAPHICALLY ISOLATED.
#   7.10.C.2  various PRE-ZYGOTIC and POST-ZYGOTIC mechanisms can maintain
#             reproductive isolation and PREVENT GENE FLOW between populations.
#
# ON THE TWO TERMS THE CED USES WITHOUT DEFINING. EK 7.10.C.2 names pre-zygotic
# and post-zygotic mechanisms and does not list any. This module therefore keys
# only on what the two words themselves divide -- whether the barrier acts
# before or after a zygote forms -- and NEVER on the name of a particular
# mechanism, since naming one would be asserting content the framework does not
# print. That is the rule SCIENCE_BRIEF.md sets: if it is not in the CED, it is
# not keyed.
#
# DELIBERATE OMISSIONS. Homologous and vestigial structures are EK 7.6.B.1 and
# are asked in b7_6; the single item here that warns against reading similarity
# as relatedness is keyed to EK 7.10.B.3 on convergent evolution, which is this
# topic's own statement. Reading a cladogram, out-groups and nodes are EK 7.9
# and are asked in b7_9. Gene flow between populations preventing divergence is
# EK 7.4.B.1 and belongs to a sibling's module; the items here concern
# mechanisms that PREVENT gene flow, which is EK 7.10.C.2's own subject.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: this bank is exported
# untypeset.
TOPIC = ("7.10", "Speciation", 7)

_T_CROSS = dict(
    headers=["Pair of populations", "Individuals of the two populations mate",
             "A zygote forms", "Offspring survive to adulthood",
             "Offspring are fertile"],
    rows=[["Pair 1", "Yes", "Yes", "Yes", "Yes"],
          ["Pair 2", "Yes", "Yes", "Yes", "No"],
          ["Pair 3", "Yes", "Yes", "No", "Not applicable"],
          ["Pair 4", "No", "No", "No", "Not applicable"]])

_T_TRAITS = dict(
    headers=["Group of species", "Kind of habitat occupied", "Body form",
             "Most recent common ancestor"],
    rows=[["Group R", "The same kind of habitat", "Very similar", "Distant"],
          ["Group S", "Several different habitats", "Very different", "Recent"]])

QUESTIONS = [
 dict(q="According to the course framework, speciation occurs when",
   choices=[
     "two populations become reproductively isolated from each other",
     "two populations come to occupy the same habitat",
     "a population increases beyond the resources available to it",
     "individuals in a population differ in phenotype",
     "a population's allele frequencies remain constant across generations"], ans=0,
   why="EK 7.10.A.1 states in as many words that speciation occurs when two populations become reproductively isolated from each other. Phenotypic variation and population growth occur constantly within a single species and do not by themselves divide one."),

 dict(q="Under the biological species concept, a species is defined as a group capable of",
   choices=[
     "interbreeding and exchanging genetic information to produce viable, fertile offspring",
     "surviving in the same habitat as one another",
     "producing any offspring at all, whether or not those offspring survive",
     "sharing a recent common ancestor with one another",
     "resembling one another closely in body form"], ans=0,
   why="EK 7.10.A.2 gives exactly that definition. Both adjectives carry weight: offspring must be viable, meaning they survive, and fertile, meaning they can themselves reproduce, so producing any offspring at all is not enough."),

 dict(q="To which organisms does the framework say the biological species concept applies?",
   choices=[
     "Sexually reproducing organisms",
     "All organisms without exception",
     "Only organisms known from fossils",
     "Only organisms that reproduce asexually",
     "Only organisms that occupy overlapping ranges"], ans=0,
   why="EK 7.10.A.2 introduces the biological species concept as a commonly used definition of a species FOR SEXUALLY REPRODUCING ORGANISMS. The definition turns on interbreeding, which an asexual lineage does not do."),

 dict(q="Two populations mate in the wild and produce healthy offspring, but every one of those offspring is sterile. Under the biological species concept, the two populations are",
   choices=[
     "separate species, because the offspring are not fertile",
     "one species, because offspring are produced",
     "one species, because the offspring are healthy",
     "separate species, because the two populations occupy different habitats",
     "impossible to classify, because the concept applies only to fossils"], ans=0,
   why="EK 7.10.A.2 requires that interbreeding produce viable AND FERTILE offspring. Sterile offspring cannot pass genetic information on, so the two populations do not exchange genetic information across generations even though a mating occurs."),

 dict(q="Which of the following describes punctuated equilibrium as the framework defines it?",
   choices=[
     "Evolution occurring rapidly after a long period of stasis",
     "Evolution occurring slowly over hundreds of thousands or millions of years",
     "Evolution occurring at exactly the same rate in every lineage",
     "Evolution ceasing entirely once a species is well adapted",
     "Evolution occurring only in populations that are geographically isolated"], ans=0,
   why="EK 7.10.B.1 defines punctuated equilibrium as evolution occurring rapidly after a long period of stasis, and gradualism as evolution occurring slowly over hundreds of thousands or millions of years. The second option is the definition of the other term."),

 dict(q="Which of the following describes gradualism as the framework defines it?",
   choices=[
     "Evolution occurring slowly over hundreds of thousands or millions of years",
     "Evolution occurring rapidly after a long period of stasis",
     "Evolution occurring only when a new habitat becomes available",
     "Evolution occurring only in populations with geographic overlap",
     "Evolution occurring at a rate that cannot be estimated"], ans=0,
   why="EK 7.10.B.1 defines gradualism as evolution occurring slowly over hundreds of thousands or millions of years. The first distractor is the framework's definition of punctuated equilibrium, which is the contrasting pattern in the same statement."),

 dict(q="A lineage shows little change through a long run of the fossil record and then changes markedly over a comparatively short interval. Which pattern of evolutionary rate does this best illustrate?",
   choices=["Punctuated equilibrium", "Gradualism", "Convergent evolution",
            "Allopatric speciation", "Sympatric speciation"], ans=0,
   why="EK 7.10.B.1 defines punctuated equilibrium as rapid evolution after a long period of stasis, which is the sequence the record describes. The other four options name a different rate or a different process altogether."),

 dict(q="A second lineage shows small, steady change from one level of the fossil record to the next across millions of years. Which pattern of evolutionary rate does this best illustrate?",
   choices=["Gradualism", "Punctuated equilibrium", "Adaptive radiation",
            "Convergent evolution", "Reproductive isolation"], ans=0,
   why="EK 7.10.B.1 defines gradualism as evolution occurring slowly over hundreds of thousands or millions of years, which is what a steady small change across such an interval describes. No stasis interrupted by rapid change is reported."),

 dict(q="According to the framework, divergent evolution occurs when",
   choices=[
     "adaptation to new habitats results in phenotypic diversification",
     "similar selective pressures produce similar adaptations in different species",
     "two populations that have separated come back together and interbreed",
     "a population remains unchanged for a long period",
     "the same phenotype appears in every population of a species"], ans=0,
   why="EK 7.10.B.2 states that divergent evolution occurs when adaptation to new habitats results in phenotypic diversification. The first distractor is the framework's definition of convergent evolution in EK 7.10.B.3."),

 dict(q="Under what circumstances does the framework say speciation rates can be especially rapid?",
   choices=[
     "During times of adaptive radiation, as new habitats become available",
     "During long periods in which the environment does not change",
     "Whenever two populations occupy exactly the same habitat",
     "Whenever a population's size is held constant",
     "Only when the fossil record is complete"], ans=0,
   why="EK 7.10.B.2 states that speciation rates can be especially rapid during times of adaptive radiation as new habitats become available. New habitats are what allow adaptation to diversify phenotypes, which is the same statement's account of divergent evolution."),

 dict(q="According to the framework, convergent evolution occurs when",
   choices=[
     "similar selective pressures result in similar phenotypic adaptations in different populations or species",
     "adaptation to new habitats results in phenotypic diversification",
     "two populations become geographically isolated from one another",
     "a lineage remains unchanged over a long period of the fossil record",
     "a population's offspring are viable but not fertile"], ans=0,
   why="EK 7.10.B.3 states that convergent evolution occurs when similar selective pressures result in similar phenotypic adaptations in different populations or species. The first distractor is EK 7.10.B.2's definition of divergent evolution."),

 dict(q="Two species that are not closely related occupy deserts on separate continents and have independently come to store water in thickened stems. Which process does this best illustrate?",
   choices=["Convergent evolution", "Divergent evolution", "Adaptive radiation",
            "Punctuated equilibrium", "Sympatric speciation"], ans=0,
   why="EK 7.10.B.3 defines convergent evolution as similar selective pressures producing similar phenotypic adaptations in different populations or species. Separate continents and distant relationship rule out a shared adaptation inherited from a recent ancestor."),

 dict(q="A single lineage colonizes a chain of islands offering many previously unoccupied habitats, and its descendants come to differ markedly in body size and feeding structures. Which pair of processes does this best illustrate?",
   choices=[
     "Divergent evolution during an adaptive radiation",
     "Convergent evolution during a period of stasis",
     "Punctuated equilibrium without any change in habitat",
     "Reproductive isolation without any phenotypic change",
     "Gradualism in a single unchanging habitat"], ans=0,
   why="EK 7.10.B.2 states both halves: divergent evolution occurs when adaptation to new habitats results in phenotypic diversification, and speciation rates can be especially rapid during adaptive radiation as new habitats become available."),

 dict(q="According to the framework, allopatric speciation occurs in populations that are",
   choices=["geographically isolated", "geographically overlapping",
            "identical in phenotype", "unable to produce any offspring at all",
            "increasing in size"], ans=0,
   why="EK 7.10.C.1 states that allopatric speciation occurs in populations that are geographically isolated, and that sympatric speciation occurs in populations with geographic overlap. The two terms are distinguished by geography alone in this statement."),

 dict(q="According to the framework, sympatric speciation occurs in populations that",
   choices=["have geographic overlap", "are separated by a physical barrier",
            "occupy separate continents", "have already become separate species",
            "reproduce only asexually"], ans=0,
   why="EK 7.10.C.1 states that sympatric speciation occurs in populations with geographic overlap. Populations that already form separate species are the outcome of speciation rather than its starting condition."),

 dict(q="A river changes course and divides a population of ground-dwelling insects into two groups that no longer meet. If the two groups become separate species, the process is best described as",
   choices=["allopatric speciation", "sympatric speciation", "convergent evolution",
            "punctuated equilibrium", "adaptive radiation"], ans=0,
   why="EK 7.10.C.1 assigns speciation in geographically isolated populations to allopatry. A physical barrier that keeps the groups from meeting is geographic isolation, whatever the eventual rate of change turns out to be."),

 dict(q="Two groups of an insect species live in the same orchard, but one group feeds and mates on one kind of tree and the other on a different kind, so the two rarely meet at breeding time. If these groups become separate species, the process is best described as",
   choices=["sympatric speciation", "allopatric speciation", "convergent evolution",
            "gradualism", "an adaptive radiation onto new continents"], ans=0,
   why="EK 7.10.C.1 assigns speciation in populations with geographic overlap to sympatry. Both groups occupy the same orchard, so their ranges overlap even though their use of that range differs."),

 dict(q="What do the framework's pre-zygotic and post-zygotic mechanisms accomplish?",
   choices=[
     "They maintain reproductive isolation and prevent gene flow between populations",
     "They increase the rate at which alleles move between populations",
     "They guarantee that two populations will remain a single species",
     "They convert asexual reproduction into sexual reproduction",
     "They determine which of two populations is the older"], ans=0,
   why="EK 7.10.C.2 states that various pre-zygotic and post-zygotic mechanisms can maintain reproductive isolation and prevent gene flow between populations. Preventing gene flow is the opposite of the first distractor's claim."),

 dict(q="What distinguishes a pre-zygotic isolating mechanism from a post-zygotic one?",
   choices=[
     "Whether the barrier acts before or after a zygote is formed",
     "Whether the two populations occupy overlapping ranges",
     "Whether the two populations resemble each other in body form",
     "Whether the change occurred rapidly or slowly",
     "Whether the populations are known from fossils or from living specimens"], ans=0,
   why="EK 7.10.C.2 names the two categories without listing particular mechanisms, and the two names divide the possibilities at the formation of the zygote. Geography, appearance and rate are the subjects of EK 7.10.C.1, EK 7.10.B.3 and EK 7.10.B.1 respectively."),

 dict(q="The table records what happens when individuals of four pairs of populations encounter one another. Which pair would be considered a single species under the biological species concept?",
   table=_T_CROSS,
   choices=["Pair 1", "Pair 2", "Pair 3", "Pair 4",
            "None of the four pairs, because all four produced some result"], ans=0,
   why="EK 7.10.A.2 requires interbreeding that produces viable, fertile offspring. Only one row of the table records mating, a zygote, offspring that survive to adulthood, and offspring that are themselves fertile."),

 dict(q="In which pair recorded in that table do offspring survive to adulthood but prove unable to reproduce?",
   table=_T_CROSS,
   choices=["Pair 2", "Pair 1", "Pair 3", "Pair 4",
            "No pair shows that combination of outcomes"], ans=0,
   why="Skill 4.B, identifying specific data points across a table. Exactly one row records offspring surviving to adulthood together with an entry showing those offspring are not fertile, which under EK 7.10.A.2 makes the two populations separate species."),

 dict(q="For which pairs in that same table does the barrier to reproduction act only after a zygote has formed?",
   table=_T_CROSS,
   choices=["Pair 2 and Pair 3", "Pair 1 and Pair 2", "Pair 3 and Pair 4",
            "Pair 1 and Pair 4", "All four pairs"], ans=0,
   why="EK 7.10.C.2 divides isolating mechanisms into pre-zygotic and post-zygotic, and the two names divide them at the formation of the zygote. The rows that record a zygote forming but the offspring failing to survive or to reproduce are the post-zygotic cases."),

 dict(q="In which pair recorded in that table does the barrier act before a zygote can form?",
   table=_T_CROSS,
   choices=["Pair 4", "Pair 1", "Pair 2", "Pair 3",
            "In every pair the barrier acts before a zygote forms"], ans=0,
   why="EK 7.10.C.2 names pre-zygotic mechanisms, which by the term's own division act before a zygote is formed. Exactly one row records that the individuals do not mate at all, so no zygote is available for a later barrier to act on."),

 dict(q="The table summarizes two groups of species, their habitats, their body forms, and how recently each group's members shared a common ancestor. Which process does the first group's combination of features best illustrate?",
   table=_T_TRAITS,
   choices=["Convergent evolution", "Divergent evolution", "Adaptive radiation",
            "Allopatric speciation", "Punctuated equilibrium"], ans=0,
   why="EK 7.10.B.3 defines convergent evolution as similar selective pressures producing similar phenotypic adaptations in different populations or species. A group whose members occupy the same kind of habitat and resemble one another despite a distant common ancestor is that pattern."),

 dict(q="Using the same summary of two groups, which process does the second group's combination of features best illustrate?",
   table=_T_TRAITS,
   choices=["Divergent evolution", "Convergent evolution", "Gradualism",
            "Sympatric speciation", "Reproductive isolation without phenotypic change"], ans=0,
   why="EK 7.10.B.2 defines divergent evolution as adaptation to new habitats resulting in phenotypic diversification. A group whose members share a recent ancestor, occupy several different habitats and differ markedly in form is that pattern."),

 dict(q="Which column of that two-group summary does the most to distinguish the two processes from one another?",
   table=_T_TRAITS,
   choices=[
     "The column recording how recently the members of the group shared a common ancestor",
     "The column recording the kind of habitat occupied",
     "The column recording body form",
     "The column giving the name of each group",
     "No column distinguishes them, because the two processes cannot be told apart"], ans=0,
   why="EK 7.10.B.2 and EK 7.10.B.3 differ in what produces the observed similarity or difference: shared recent ancestry with new habitats in one case, shared selective pressure without close relationship in the other. Habitat and body form each vary between the groups too, but ancestry is what settles which explanation applies."),

 dict(q="Two populations long separated by a mountain range are reunited when a pass opens, and they interbreed freely and produce fertile offspring in every generation thereafter. What follows under the framework's account?",
   choices=[
     "They had not become reproductively isolated, so speciation had not been completed",
     "They must be separate species, because they were separated for a long time",
     "They must be separate species, because they occupy overlapping ranges",
     "Speciation is now certain to occur within one generation",
     "The biological species concept cannot be applied to them"], ans=0,
   why="EK 7.10.A.1 makes reproductive isolation the condition for speciation and EK 7.10.A.2 makes the production of viable, fertile offspring the test of a single species. Time spent apart is not itself the criterion; what happens on contact is."),

 dict(q="A volcanic eruption creates a large area of new and varied habitat that is quickly colonized by one species from the surrounding region. Which outcome does the framework's account make most likely over subsequent generations?",
   choices=[
     "Phenotypic diversification among the descendants, with speciation possibly proceeding rapidly",
     "A long period of stasis in which no phenotypic change occurs",
     "Convergence of the colonists on the phenotype of an unrelated species",
     "An immediate return of the colonists to their original range",
     "A halt to all evolutionary change until the habitat stops changing"], ans=0,
   why="EK 7.10.B.2 states that divergent evolution occurs when adaptation to new habitats results in phenotypic diversification, and that speciation rates can be especially rapid during adaptive radiation as new habitats become available. The scenario is new habitat becoming available."),

 dict(q="Why is a close resemblance in body form between two species weak evidence on its own that they are closely related?",
   choices=[
     "Similar selective pressures can produce similar adaptations in species that are not closely related",
     "Body form cannot be measured accurately in any species",
     "Closely related species never resemble one another",
     "Resemblance is evidence only when the species occupy different habitats",
     "Body form changes only during periods of stasis"], ans=0,
   why="EK 7.10.B.3 states that convergent evolution occurs when similar selective pressures result in similar phenotypic adaptations in different populations or species. Resemblance therefore has two possible explanations, and the observation alone does not choose between them."),

 dict(q="Which pairing of the framework's terms correctly matches a process with the condition that defines it?",
   choices=[
     "Allopatric speciation with geographic isolation, and sympatric speciation with geographic overlap",
     "Allopatric speciation with geographic overlap, and sympatric speciation with geographic isolation",
     "Punctuated equilibrium with slow change over millions of years, and gradualism with rapid change after stasis",
     "Convergent evolution with adaptation to new habitats, and divergent evolution with similar selective pressures",
     "Reproductive isolation with the merging of two populations into one species"], ans=0,
   why="EK 7.10.C.1 assigns geographic isolation to allopatry and geographic overlap to sympatry. Each remaining option reverses a pair of the framework's definitions, from EK 7.10.B.1, EK 7.10.B.2 and EK 7.10.B.3 respectively, or contradicts EK 7.10.A.1."),
]
