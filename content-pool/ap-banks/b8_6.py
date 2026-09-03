# AP BIOLOGY 8.6 Biodiversity
# CED effective Fall 2025, Unit 8 Ecology, Big Idea 4 Systems Interactions.
# Learning objectives 8.6.A (describe the relationship between ecosystem
# diversity and its resilience to changes in the environment) and 8.6.B
# (explain how the addition or removal of any component of an ecosystem will
# affect its overall short-term and long-term structure).
# Suggested skill 6.E, PREDICT THE CAUSES OR EFFECTS of a change in, or
# disruption to, one or more components in a biological system.
#
# Essential knowledge relied on, in the framework's own terms:
#   8.6.A.1  NATURAL AND ARTIFICIAL ecosystems with FEWER COMPONENT PARTS, and
#            with LITTLE DIVERSITY AMONG THE PARTS, are OFTEN LESS RESILIENT to
#            changes in the environment.
#   8.6.A.2  KEYSTONE SPECIES, PRODUCERS, and ESSENTIAL ABIOTIC AND BIOTIC
#            FACTORS contribute to MAINTAINING THE DIVERSITY of an ecosystem.
#   8.6.B.1  the effects of keystone species on the ecosystem are
#            DISPROPORTIONATE RELATIVE TO THEIR ABUNDANCE in the ecosystem.
#            When they are removed from the ecosystem, IT OFTEN COLLAPSES.
#
# THE HEDGES ARE PRESERVED. EK 8.6.A.1 says such ecosystems are OFTEN less
# resilient and EK 8.6.B.1 says the ecosystem OFTEN collapses. Neither is a
# guarantee, and three items here turn on exactly that. No key in this module
# upgrades either sentence into a certainty.
#
# DELIBERATE OMISSIONS, because the neighbouring topics are close.
#  * GENETIC diversity within a species or population, and its effect on that
#    population's ability to withstand environmental pressure, is EK 7.11.A.1
#    and is asked in b7_11. Everything here works at the level of an
#    ECOSYSTEM's component parts, which is the level EK 8.6.A.1 works at, and
#    no item here mentions alleles or genetic variation.
#  * Species composition, species diversity and the diversity index are
#    EK 8.5.A.1 and are asked in b8_5, along with competition, predation and
#    the symbioses. NOTHING here computes a diversity index or names a
#    symbiosis; the data items here concern resilience and the disproportionate
#    effect of a keystone species, which are this topic's own statements.
#  * Invasive species, human activity and geological events as disruptions are
#    EK 8.7.B, EK 8.7.C and EK 8.7.D and are asked in b8_7. The disruptions
#    here are the removal or addition of a COMPONENT, which is what learning
#    objective 8.6.B asks about.
#
# ON THE DATA. Both tables are hypothetical and say so, and every number a key
# states is recomputed in verify_b8_6.py from that table alone. The keystone
# table is built so that abundance and effect run in opposite directions, which
# is what EK 8.6.B.1's word DISPROPORTIONATE requires a student to see.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: this bank is exported
# untypeset.
TOPIC = ("8.6", "Biodiversity", 8)

_T_ECO = dict(
    headers=["Hypothetical ecosystem", "Number of component species present",
             "Diversity among the component parts",
             "Percentage change in productivity after the same drought"],
    rows=[["Ecosystem 1", "6", "Low", "-62"],
          ["Ecosystem 2", "14", "Moderate", "-38"],
          ["Ecosystem 3", "31", "High", "-11"]])

_T_KEYSTONE = dict(
    headers=["Species removed in a hypothetical experiment",
             "Percentage of the community's total biomass held by this species",
             "Number of other species whose abundance changed by more than half after the removal"],
    rows=[["Species F", "2", "9"],
          ["Species G", "24", "1"],
          ["Species H", "31", "0"],
          ["Species J", "5", "2"]])

QUESTIONS = [
 dict(q="According to the course framework, which ecosystems are often less resilient to changes in the environment?",
   choices=[
     "Those with fewer component parts and little diversity among the parts",
     "Those with many component parts and great diversity among the parts",
     "Those that contain at least one producer",
     "Those that occupy the largest area",
     "Those that have existed for the longest time"], ans=0,
   why="EK 8.6.A.1 states that natural and artificial ecosystems with fewer component parts, and with little diversity among the parts, are often less resilient to changes in the environment. Area and age are not what the statement names."),

 dict(q="EK 8.6.A.1 says such ecosystems are OFTEN less resilient. What does that qualifier allow?",
   choices=[
     "That lower diversity usually reduces resilience without guaranteeing it in every case",
     "That lower diversity always reduces resilience",
     "That diversity has no effect on resilience",
     "That resilience cannot be observed",
     "That only artificial ecosystems are affected"], ans=0,
   why="EK 8.6.A.1 writes OFTEN rather than always. A stated tendency describes the usual case and leaves room for exceptions, so an absolute reading overstates the sentence."),

 dict(q="To which ecosystems does the framework's statement about component parts and resilience apply?",
   choices=["Both natural and artificial ecosystems", "Natural ecosystems only",
            "Artificial ecosystems only", "Only ecosystems containing keystone species",
            "Only ecosystems that have already collapsed"], ans=0,
   why="EK 8.6.A.1 opens by naming natural AND artificial ecosystems, so the claim is not restricted to either kind. A planted stand and an undisturbed wood are covered by the same sentence."),

 dict(q="According to the framework, what contributes to maintaining the diversity of an ecosystem?",
   choices=[
     "Keystone species, producers, and essential abiotic and biotic factors",
     "Keystone species alone",
     "Producers alone",
     "Abiotic factors alone, since living components cannot maintain diversity",
     "The total area of the ecosystem"], ans=0,
   why="EK 8.6.A.2 names keystone species, producers, and essential abiotic and biotic factors as contributing to maintaining the diversity of an ecosystem. Each distractor keeps one part of that list and discards the rest."),

 dict(q="Which of the following is NOT among the contributors to maintaining ecosystem diversity that the framework names?",
   choices=["The age of the rocks underlying the ecosystem", "Keystone species",
            "Producers", "Essential abiotic factors", "Essential biotic factors"], ans=0,
   why="EK 8.6.A.2 names keystone species, producers, and essential abiotic and biotic factors. The age of the underlying rock is a dating consideration under EK 7.6.B.1 and appears nowhere in this topic."),

 dict(q="According to the framework, how do the effects of a keystone species on its ecosystem compare with its abundance there?",
   choices=[
     "The effects are disproportionate relative to its abundance",
     "The effects are proportional to its abundance",
     "The effects are always smaller than its abundance would suggest",
     "A keystone species is always the most abundant species present",
     "A keystone species has no measurable effect on its ecosystem"], ans=0,
   why="EK 8.6.B.1 states that the effects of keystone species on the ecosystem are disproportionate relative to their abundance in the ecosystem. Disproportionate means out of proportion, which is why proportionality is the error the nearest distractor carries."),

 dict(q="According to the framework, what often happens to an ecosystem when a keystone species is removed from it?",
   choices=["It often collapses", "It becomes more diverse", "It is unaffected",
            "It gains additional component parts", "It becomes more resilient to further change"], ans=0,
   why="EK 8.6.B.1 states that when keystone species are removed from the ecosystem, it often collapses. That is the consequence the statement attaches to their removal."),

 dict(q="EK 8.6.B.1 says the ecosystem OFTEN collapses when a keystone species is removed. What does that qualifier allow?",
   choices=[
     "That collapse is the usual outcome without being certain in every case",
     "That collapse is certain in every case",
     "That collapse never occurs",
     "That collapse occurs only in artificial ecosystems",
     "That collapse occurs only when the species removed is the most abundant"], ans=0,
   why="EK 8.6.B.1 writes OFTEN rather than always, which states a strong tendency and leaves room for cases in which the ecosystem does not collapse. No key in this topic may treat the outcome as guaranteed."),

 dict(q="A species makes up a very small share of the biomass of its community, yet removing it changes the abundance of many other species. This pattern is best described in the framework's terms as",
   choices=[
     "an effect disproportionate relative to the species' abundance",
     "an effect proportional to the species' abundance",
     "evidence that the species is the community's most abundant",
     "evidence that the community has no producers",
     "evidence that the community's diversity cannot be measured"], ans=0,
   why="EK 8.6.B.1 states that the effects of keystone species on the ecosystem are disproportionate relative to their abundance. A large effect from a species of small abundance is exactly that mismatch."),

 dict(q="A student concludes that the keystone species of an ecosystem must be the species with the greatest biomass there. Which statement of the framework does this conclusion contradict?",
   choices=[
     "That the effects of keystone species are disproportionate relative to their abundance",
     "That producers contribute to maintaining the diversity of an ecosystem",
     "That ecosystems with fewer component parts are often less resilient",
     "That both natural and artificial ecosystems are covered by the claim",
     "That essential abiotic factors contribute to maintaining diversity"], ans=0,
   why="EK 8.6.B.1 defines the keystone role by a mismatch between effect and abundance, so identifying it with the greatest abundance removes the very feature the statement names. Nothing in the framework ties the role to biomass rank."),

 dict(q="A component species is removed from an ecosystem, and over the following seasons several other populations change sharply in abundance. Which statement of the framework does this outcome illustrate?",
   choices=[
     "The addition or removal of a component of an ecosystem affects its overall structure",
     "Removal of a component has no effect on the remaining components",
     "Diversity among the parts has no bearing on how an ecosystem responds",
     "Only the removal of an abiotic factor can change an ecosystem",
     "The ecosystem's structure is fixed once it is established"], ans=0,
   why="Learning objective 8.6.B asks students to explain how the addition or removal of any component of an ecosystem will affect its overall short-term and long-term structure, and EK 8.6.B.1 gives the keystone case as the most extreme version of it."),

 dict(q="Producers are removed from a hypothetical ecosystem while every other component is left in place. What does the framework's account predict?",
   choices=[
     "The ecosystem's diversity is no longer maintained, because producers are named among its contributors",
     "The ecosystem becomes more diverse, because competition is reduced",
     "Nothing changes, because producers are only one component",
     "Only abiotic factors are affected",
     "The remaining species become keystone species"], ans=0,
   why="EK 8.6.A.2 names producers among the contributors to maintaining the diversity of an ecosystem, and skill 6.E asks for the predicted effect of a disruption to one or more components. Removing a named contributor removes its contribution."),

 dict(q="Two hypothetical ecosystems face the same environmental change. One holds many component species with great diversity among them; the other holds few, with little diversity. Which prediction does the framework's account support?",
   choices=[
     "The ecosystem with few, similar parts is more likely to be the less resilient of the two",
     "The ecosystem with many diverse parts is more likely to be the less resilient of the two",
     "The two will respond identically, because the change is the same",
     "Neither ecosystem can respond to environmental change",
     "The larger ecosystem will always recover first regardless of its parts"], ans=0,
   why="EK 8.6.A.1 states that ecosystems with fewer component parts and little diversity among the parts are often less resilient to changes in the environment. Skill 6.E asks for the prediction that follows, and the word often makes it a likelihood rather than a certainty."),

 dict(q="A planted stand is established that contains one crop species and very few other organisms. What does the framework's account predict about how it will respond to a new environmental stress?",
   choices=[
     "It is likely to be less resilient than a comparable ecosystem with more and more varied parts",
     "It is likely to be more resilient, because it has fewer parts to disturb",
     "It cannot be compared with a natural ecosystem under this statement",
     "It will be unaffected by any environmental stress",
     "It will gain component parts automatically in response to the stress"], ans=0,
   why="EK 8.6.A.1 covers artificial as well as natural ecosystems and attaches lower resilience to having fewer component parts and little diversity among them. A stand of one species with few other organisms is that description at the ecosystem level."),

 dict(q="An essential abiotic factor of an ecosystem is disrupted. Under the framework's account, what is the most defensible prediction?",
   choices=[
     "The diversity of the ecosystem is likely to be affected, because such factors are named among its contributors",
     "Only the abiotic components will be affected, since biotic parts are independent",
     "The ecosystem will gain diversity, because a constraint has been removed",
     "Nothing will change, because only species affect diversity",
     "The most abundant species will automatically become a keystone species"], ans=0,
   why="EK 8.6.A.2 names essential abiotic AND biotic factors among the contributors to maintaining the diversity of an ecosystem, so the two are not independent in the statement's own terms. Skill 6.E asks for the effect of a disruption to a component."),

 dict(q="Which observation about a species would best support the claim that it is a keystone species in its ecosystem?",
   choices=[
     "It makes up a small share of the community's biomass, and its removal changes many other populations",
     "It makes up the largest share of the community's biomass",
     "It is the species most recently added to the ecosystem",
     "It occupies the largest area within the ecosystem",
     "Its own population size changes the most from year to year"], ans=0,
   why="EK 8.6.B.1 makes the keystone role a mismatch between effect and abundance, so evidence for it must pair a small abundance with a large effect. Biomass rank, area and variability alone say nothing about the effect of removal."),

 dict(q="What would most weaken the claim that a particular species is the keystone species of its ecosystem?",
   choices=[
     "Its removal from comparable plots leaves the other populations almost unchanged",
     "It makes up only a small share of the community's biomass",
     "It interacts with several other species",
     "It is a producer rather than a consumer",
     "It has been present in the ecosystem for many years"], ans=0,
   why="EK 8.6.B.1 rests the keystone role on a large effect out of proportion to abundance. An observed removal that changes little removes the effect half of that claim, whereas a small abundance is consistent with the role rather than against it."),

 dict(q="Components are added to a simplified ecosystem so that it comes to hold more species and more variety among them. What does the framework's account predict about its resilience?",
   choices=[
     "It is likely to become more resilient to changes in the environment",
     "It is likely to become less resilient, because more parts can fail",
     "Its resilience will not change, because only the original parts matter",
     "It will collapse, because any addition is a disruption",
     "It will become an artificial ecosystem and so fall outside the statement"], ans=0,
   why="EK 8.6.A.1 attaches lower resilience to having fewer component parts and little diversity among them, so moving away from that condition moves away from the associated fragility. EK 8.6.A.1 covers artificial ecosystems too, so the last option misreads the statement."),

 dict(q="Why does the framework treat the removal of a keystone species as a more severe disruption than the removal of a similarly rare species that is not keystone?",
   choices=[
     "Because the keystone species' effects are out of proportion to its abundance, so its loss removes more than its share of the ecosystem's structure",
     "Because the keystone species is always more abundant than the other",
     "Because rare species can never be removed from an ecosystem",
     "Because only keystone species are producers",
     "Because the two removals are in fact equally severe"], ans=0,
   why="EK 8.6.B.1 states that the effects of keystone species are disproportionate relative to their abundance and that the ecosystem often collapses when they are removed. Rarity is shared by both species in the comparison; the disproportion is not."),

 dict(q="The table reports three hypothetical ecosystems, the number of component species in each, the diversity among those parts, and how each fared under the same drought. What relationship do these data show?",
   table=_T_ECO,
   choices=[
     "The ecosystems with more and more varied parts lost less productivity",
     "The ecosystems with more and more varied parts lost more productivity",
     "The loss of productivity was the same in all three ecosystems",
     "The number of component species and the loss are unrelated in these data",
     "Only the ecosystem with the fewest parts gained productivity"], ans=0,
   why="Skill 4.B asks for the relationship between the variables. Reading the rows in order of the number of component species, the loss of productivity shrinks without exception, which is the pattern EK 8.6.A.1 describes."),

 dict(q="Which of the three ecosystems in that table does the framework's account identify as the least resilient to this change?",
   table=_T_ECO,
   choices=["Ecosystem 1", "Ecosystem 2", "Ecosystem 3",
            "All three were equally resilient", "Resilience cannot be judged from these data"], ans=0,
   why="EK 8.6.A.1 states that ecosystems with fewer component parts and little diversity among the parts are often less resilient. The row with the fewest species and the lowest diversity is also the row that lost the most productivity."),

 dict(q="By how many percentage points did the loss of productivity in the least diverse ecosystem exceed the loss in the most diverse one?",
   table=_T_ECO,
   choices=["51 percentage points", "62 percentage points", "11 percentage points",
            "73 percentage points", "27 percentage points"], ans=0,
   why="Skill 5.A includes percentages and percent changes. The two rows are identified by the number of component species they report, and the answer is the difference in the size of their recorded losses."),

 dict(q="Which column of that three-ecosystem table would have to be added to test whether the drought itself was equally severe in all three places?",
   table=_T_ECO,
   choices=[
     "A record of the severity of the drought at each ecosystem",
     "A record of the number of component species before the drought",
     "A record of the percentage change in productivity",
     "A record of the diversity among the parts",
     "No further column is needed, because the comparison is already complete"], ans=0,
   why="Skill 6.E asks for a prediction about the effect of a disruption, and a comparison across ecosystems only isolates the effect of their structure if the disruption itself was comparable. Three of the options name columns the table already carries."),

 dict(q="What does the framework's statement about resilience allow a student to conclude from those three ecosystems, and what does it not?",
   table=_T_ECO,
   choices=[
     "The pattern matches the framework's expectation, but the word often means a further case could depart from it",
     "The pattern proves that low diversity always causes a large loss",
     "The pattern shows that diversity has no effect on resilience",
     "The pattern shows that the drought was more severe where diversity was high",
     "No pattern is present in the data at all"], ans=0,
   why="EK 8.6.A.1 says such ecosystems are OFTEN less resilient, which is a tendency rather than a law. Three consistent cases match the expectation without converting the hedge into a certainty."),

 dict(q="The table reports four species removed one at a time from a hypothetical community, the share of total biomass each held, and how many other species changed sharply in abundance afterwards. Which species best fits the framework's description of a keystone species?",
   table=_T_KEYSTONE,
   choices=["Species F", "Species G", "Species H", "Species J",
            "None of the four, because a keystone species must be the most abundant"], ans=0,
   why="EK 8.6.B.1 states that the effects of keystone species are disproportionate relative to their abundance. The row combining the smallest share of biomass with much the largest number of species affected is the one that mismatch picks out."),

 dict(q="Which species in that removal experiment held the largest share of the community's biomass, and what did its removal show?",
   table=_T_KEYSTONE,
   choices=[
     "Species H, whose removal changed the abundance of no other species",
     "Species F, whose removal changed the abundance of many other species",
     "Species G, whose removal changed the abundance of no other species",
     "Species J, whose removal changed the abundance of many other species",
     "Species H, whose removal changed the abundance of many other species"], ans=0,
   why="EK 8.6.B.1 makes the keystone role a mismatch between effect and abundance, and the table is built to separate the two. The row with the largest biomass share records the smallest number of other species affected."),

 dict(q="After Species F was removed, how many other species changed in abundance by more than half?",
   table=_T_KEYSTONE,
   choices=["Nine", "One", "Two", "Zero", "Four"], ans=0,
   why="Skill 4.B, identifying a specific data point. The row the stem names records the number directly, and it is the largest such number in the table."),

 dict(q="Species G held how many times the share of biomass that Species F held?",
   table=_T_KEYSTONE,
   choices=["12 times", "9 times", "2 times", "24 times", "22 times"], ans=0,
   why="Skill 5.A includes ratios. Dividing the biomass share of the first named species by that of the second gives the factor, and the same pair runs the other way on the number of species affected."),

 dict(q="Which conclusion do the results of that removal experiment best support?",
   table=_T_KEYSTONE,
   choices=[
     "The effect of a species on its community need not be proportional to how abundant it is",
     "The effect of a species on its community is always proportional to how abundant it is",
     "Only the most abundant species affect their communities",
     "Removing any species changes the same number of other species",
     "The number of species affected cannot be counted"], ans=0,
   why="EK 8.6.B.1 states that the effects of keystone species are disproportionate relative to their abundance. The table records the smallest biomass share with the largest effect and the largest share with none, which is that disproportion measured directly."),

 dict(q="Taken together, what do the framework's statements about biodiversity assert?",
   choices=[
     "Ecosystems with fewer and less varied parts are often less resilient, several named components maintain diversity, and a keystone species has effects out of proportion to its abundance",
     "Ecosystems with more parts are always less resilient, and abundance determines a species' effect",
     "Only artificial ecosystems lose resilience, and keystone species have no measurable effects",
     "Diversity is maintained by abundance alone, and removal of any species collapses an ecosystem",
     "Resilience and diversity are unrelated to one another"], ans=0,
   why="EK 8.6.A.1 supplies the resilience claim with its hedge, EK 8.6.A.2 the list of contributors to maintaining diversity, and EK 8.6.B.1 the disproportionate effect of keystone species. Each distractor contradicts one of those three sentences."),
]
