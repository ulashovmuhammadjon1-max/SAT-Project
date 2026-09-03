# AP BIOLOGY 3.3 Cellular Energy
# CED effective Fall 2025, Unit 3 Cellular Energetics. Big Idea 2 Energetics.
# Learning objectives 3.3.A (describe the role of energy in living organisms)
# and 3.3.B (explain how shared, conserved, and fundamental processes and
# features support the concept of common ancestry for all organisms).
# Suggested skill 6.C, provide reasoning to justify a claim by connecting
# evidence to biological theories.
#
# Essential knowledge, in the framework's own terms:
#   3.3.A.1     All living systems require an input of energy.
#   3.3.A.2     Life requires a highly ordered system and does not violate the
#               first and second laws of thermodynamics.
#     i.        ENERGY INPUT MUST EXCEED ENERGY LOSS to maintain order and to
#               power cellular processes.
#     ii.       Cellular processes that RELEASE energy may be COUPLED with
#               cellular processes that REQUIRE energy.
#     iii.      SIGNIFICANT LOSS of order or energy flow RESULTS IN DEATH.
#   3.3.A.3     Energy-related pathways in biological systems are SEQUENTIAL to
#               allow for a more CONTROLLED transfer of energy. A PRODUCT of a
#               reaction in a metabolic pathway is typically the REACTANT for
#               the subsequent step.
#   3.3.B.1     Core metabolic pathways (e.g., glycolysis, oxidative
#               phosphorylation) are CONSERVED ACROSS ALL CURRENTLY RECOGNIZED
#               DOMAINS (Archaea, Bacteria, and Eukarya).
#
# EXCLUSION STATEMENT OBSERVED. The CED states that the equation for Gibbs free
# energy is beyond the scope of the AP Exam, so no item here asks for it, names
# it, or requires a sign convention that only that equation supplies.
#
# BOUNDARY WITH 3.4 AND 3.5, HELD DELIBERATELY. Glycolysis and oxidative
# phosphorylation appear here only as the two examples EK 3.3.B.1 itself names
# for a CONSERVED CORE PATHWAY. Nothing in this module asks how either works;
# that is the content of topics 3.4 and 3.5.
#
# Tables are labelled HYPOTHETICAL and every keyed conclusion is recoverable
# from the table itself.
#
# FIVE choices (A-E). Plain prose, no LaTeX.
TOPIC = ("3.3", "Cellular Energy", 3)

_T_BALANCE = dict(
    headers=["Organism (hypothetical)",
             "Energy taken in per day (kilojoules)",
             "Energy lost per day (kilojoules)"],
    rows=[["Organism P", "500", "450"],
          ["Organism Q", "400", "400"],
          ["Organism R", "300", "380"],
          ["Organism S", "620", "500"]])

_T_PATHWAY = dict(
    headers=["Compound in the pathway",
             "Concentration in untreated cells (micromolar)",
             "Concentration in treated cells (micromolar)"],
    rows=[["Compound 1, the starting material", "10", "11"],
          ["Compound 2", "8", "30"],
          ["Compound 3", "6", "1"],
          ["Compound 4, the end product", "5", "0"]])

_T_DOMAINS = dict(
    headers=["Domain", "Species examined",
             "Species carrying out glycolysis",
             "Species carrying out pathway Z"],
    rows=[["Archaea", "40", "40", "0"],
          ["Bacteria", "60", "60", "0"],
          ["Eukarya", "50", "50", "50"]])

_T_COUPLE = dict(
    headers=["Coupled pair in a cell (hypothetical)",
             "Energy released by the first process (kilojoules per mole)",
             "Energy required by the second process (kilojoules per mole)"],
    rows=[["Pair 1", "30", "20"],
          ["Pair 2", "30", "45"],
          ["Pair 3", "50", "31"],
          ["Pair 4", "18", "24"]])

QUESTIONS = [
 dict(q="Which statement about energy does the framework make about every living system without exception?",
   choices=[
     "It requires an input of energy",
     "It produces more energy than it consumes",
     "It obtains its energy directly from sunlight",
     "It stores all the energy it takes in without loss",
     "It can maintain itself indefinitely with no energy exchange"],
   ans=0,
   why="EK 3.3.A.1 states that all living systems require an input of energy. Nothing in the framework claims that a system creates energy, that every system is photosynthetic, or that energy is stored without loss."),

 dict(q="How does the framework describe the relationship between living systems and the laws of thermodynamics?",
   choices=[
     "Life requires a highly ordered system and does not violate the first and second laws",
     "Life is the one known exception to the second law",
     "Life violates the first law but obeys the second",
     "The laws of thermodynamics apply only to nonliving systems",
     "Life obeys the laws only while an organism is dormant"],
   ans=0,
   why="EK 3.3.A.2 states that life requires a highly ordered system and does not violate the first and second laws of thermodynamics. The framework treats orderliness and thermodynamic law as compatible, not as competing claims."),

 dict(q="What relationship between energy taken in and energy lost does the framework require for an organism to maintain order and power its processes?",
   choices=[
     "Energy input must exceed energy loss",
     "Energy input must exactly equal energy loss",
     "Energy loss must exceed energy input",
     "Energy input and energy loss are unrelated to maintaining order",
     "Energy loss must fall to zero"],
   ans=0,
   why="EK 3.3.A.2.i states that energy input must exceed energy loss to maintain order and to power cellular processes. Equality would leave nothing available for the ordering work the same statement requires."),

 dict(q="The framework says that a cellular process releasing energy may be paired with one requiring energy. What is that arrangement called and what does it accomplish?",
   choices=[
     "Coupling, which lets the energy released by one process drive the other",
     "Denaturation, which lets one process disable the other",
     "Conservation, which lets one process become the other across all domains",
     "Compartmentalization, which lets the two processes occupy separate organelles",
     "Inhibition, which lets one process shut the other down"],
   ans=0,
   why="EK 3.3.A.2.ii states that cellular processes which release energy may be coupled with cellular processes that require energy. The other four terms name mechanisms the framework introduces for entirely different purposes."),

 dict(q="According to the framework, what is the consequence for an organism of a significant loss of order or of energy flow?",
   choices=[
     "Death",
     "A temporary reduction in growth followed by full recovery",
     "A permanent increase in metabolic efficiency",
     "Conversion of the organism into a dormant but living state indefinitely",
     "No consequence, because order is not required for life"],
   ans=0,
   why="EK 3.3.A.2.iii states that significant loss of order or energy flow results in death. The framework treats this as the outcome, not as a recoverable setback."),

 dict(q="Why does the framework describe energy-related pathways in biological systems as sequential?",
   choices=[
     "Because a series of steps allows a more controlled transfer of energy than a single step would",
     "Because a series of steps releases more total energy than a single step would",
     "Because the cell can only build one enzyme at a time",
     "Because a sequence prevents any energy from being lost as heat",
     "Because a sequence removes the need for an input of energy"],
   ans=0,
   why="EK 3.3.A.3 states that energy-related pathways are sequential to allow for a more controlled transfer of energy. Control, not total yield, is the reason the statement gives."),

 dict(q="In a metabolic pathway, what is the usual relationship between one reaction's product and the next reaction?",
   choices=[
     "The product of one reaction is typically the reactant for the following step",
     "The product of one reaction is typically discarded before the following step",
     "Each step draws its reactant directly from outside the cell",
     "Each step produces the same product as every other step",
     "The final product of the pathway is the reactant for the first step"],
   ans=0,
   why="EK 3.3.A.3 states that a product of a reaction in a metabolic pathway is typically the reactant for the subsequent step in the pathway. That linkage is what makes the pathway a sequence rather than a collection of separate reactions."),

 dict(q="Across which groups does the framework say core metabolic pathways are conserved?",
   choices=[
     "Archaea, Bacteria, and Eukarya",
     "Bacteria and Eukarya but not Archaea",
     "Archaea and Bacteria but not Eukarya",
     "Eukarya alone",
     "Only the organisms that carry out photosynthesis"],
   ans=0,
   why="EK 3.3.B.1 states that core metabolic pathways are conserved across all currently recognized domains and names them: Archaea, Bacteria, and Eukarya."),

 dict(q="Which two pathways does the framework give as examples of a conserved core metabolic pathway?",
   choices=[
     "Glycolysis and oxidative phosphorylation",
     "Transcription and translation",
     "Mitosis and meiosis",
     "Diffusion and osmosis",
     "Denaturation and renaturation"],
   ans=0,
   why="EK 3.3.B.1 names glycolysis and oxidative phosphorylation parenthetically as its examples of core metabolic pathways conserved across all currently recognized domains."),

 dict(q="An investigator argues that the presence of the same core metabolic pathway in organisms from all three domains supports common ancestry. What makes that reasoning sound?",
   choices=[
     "A feature shared by all three domains is most simply explained as inherited from an ancestor they share",
     "A feature shared by all three domains must have arisen separately in each of them",
     "A feature found in only one domain is stronger evidence of shared ancestry",
     "Metabolic pathways cannot be compared between domains at all",
     "Shared pathways show that the three domains have identical genomes"],
   ans=0,
   why="Skill 6.C asks for reasoning connecting evidence to a theory. EK 3.3.B.1 supplies the observation of conservation across all three domains, and EK 2.1.A.1 uses the same reasoning for ribosomes, reading a universal feature as reflecting common ancestry."),

 dict(q="A chemical blocks one enzyme in the middle of a sequential metabolic pathway. What is the most reasonable prediction about the compounds in that pathway?",
   choices=[
     "The compound just before the blocked step builds up while later compounds become scarce",
     "Every compound in the pathway builds up equally",
     "The compounds after the blocked step build up while earlier ones become scarce",
     "The pathway is unaffected because the steps operate independently",
     "The pathway reverses direction and runs from its end product backward"],
   ans=0,
   why="EK 3.3.A.3 makes each product the reactant for the following step, so removing one step cuts the supply to everything downstream and leaves the material entering that step with nowhere to go. Skill 6.E asks for exactly this kind of prediction."),

 dict(q="Concentrations of four compounds in a sequential pathway were measured in untreated cells and in cells given an inhibitor, with the results shown. Where in the pathway does the inhibitor act?",
   table=_T_PATHWAY,
   choices=[
     "At the step that converts the last compound to rise into the first compound to fall",
     "At the step that produces the starting material of the pathway",
     "At the final step, which forms the end product",
     "At every step in the pathway equally",
     "Nowhere in this pathway, since the treatment changed nothing"],
   ans=0,
   why="EK 3.3.A.3 makes each product the reactant for the next step, so a block shows as accumulation immediately upstream and depletion downstream. The junction between the accumulating and depleted compounds locates it."),

 dict(q="Daily energy budgets were recorded for four organisms, with the results shown. Which organism cannot maintain its order over the long term?",
   table=_T_BALANCE,
   choices=[
     "The organism whose daily energy loss is greater than its daily energy intake",
     "The organism with the largest daily energy intake",
     "The organism whose intake and loss are equal",
     "The organism with the largest surplus of intake over loss",
     "None of them, because order does not depend on an energy balance"],
   ans=0,
   why="EK 3.3.A.2.i requires energy input to exceed energy loss to maintain order and power cellular processes, and EK 3.3.A.2.iii makes a significant loss of energy flow result in death. Only one organism in the table runs a deficit."),

 dict(q="Using the same daily energy budgets, which organism has the largest surplus available for maintaining order and powering cellular processes?",
   table=_T_BALANCE,
   choices=[
     "The organism whose intake exceeds its loss by the greatest amount",
     "The organism with the smallest daily energy loss",
     "The organism whose intake and loss are equal",
     "The organism with the smallest daily intake",
     "The surplus cannot be determined from intake and loss alone"],
   ans=0,
   why="EK 3.3.A.2.i frames the requirement as input exceeding loss, so the surplus is the difference between the two columns. Skill 5.A asks students to perform exactly this kind of calculation from a table."),

 dict(q="Species from three domains were surveyed for two pathways, with the results shown. Which conclusion do these data support?",
   table=_T_DOMAINS,
   choices=[
     "One of the two pathways is present in every species of all three domains and the other is confined to a single domain",
     "Both pathways are present in every species of all three domains",
     "Neither pathway is present in more than one domain",
     "Both pathways are confined to a single domain",
     "The pathway confined to one domain is present in more species than the universal one"],
   ans=0,
   why="EK 3.3.B.1 says core metabolic pathways are conserved across Archaea, Bacteria, and Eukarya. The table separates a pathway with that distribution from one that lacks it, which is what makes the first a candidate core pathway."),

 dict(q="Four coupled pairs of cellular processes were measured, with the results shown. In which pairs can the energy released by the first process cover the requirement of the second?",
   table=_T_COUPLE,
   choices=[
     "The pairs in which the energy released exceeds the energy required",
     "The pairs in which the energy required exceeds the energy released",
     "All four pairs, since coupling always succeeds",
     "None of the four pairs, since coupling never succeeds",
     "Only the pair with the largest energy release, regardless of the requirement"],
   ans=0,
   why="EK 3.3.A.2.ii allows an energy-releasing process to be coupled to an energy-requiring one, and EK 3.3.A.2.i sets the condition in the same terms: what is supplied must exceed what is needed. The comparison is between the two columns of each row, not between rows."),

 dict(q="Why does maintaining a highly ordered internal state require a continuing input of energy rather than a single initial input?",
   choices=[
     "Because energy is continually lost, so order must be continually restored",
     "Because order is created only at the moment an organism is formed",
     "Because a single large input would violate the first law of thermodynamics",
     "Because the second law does not apply to a system that has already been ordered",
     "Because energy input has no relationship to order once order exists"],
   ans=0,
   why="EK 3.3.A.2.i requires that input exceed loss on an ongoing basis to MAINTAIN order, and EK 3.3.A.2.iii makes the failure of that flow fatal. Ongoing loss is what makes the requirement continuous rather than one-time."),

 dict(q="An organism stops taking in energy but continues to lose energy to its surroundings. Which prediction follows from the framework?",
   choices=[
     "Its order declines and, if the loss continues, it dies",
     "Its order is unaffected because order and energy are separate matters",
     "Its order increases because it is no longer processing incoming material",
     "It enters a state in which the laws of thermodynamics no longer apply",
     "It begins producing its own energy from nothing to compensate"],
   ans=0,
   why="EK 3.3.A.2.i makes maintained order depend on input exceeding loss, and EK 3.3.A.2.iii states that a significant loss of order or energy flow results in death. An intake of zero against continuing loss is that case."),

 dict(q="A student says that because living things become more ordered as they grow, life must be an exception to the second law of thermodynamics. What is the best correction?",
   choices=[
     "An organism maintains its order by taking in more energy than it loses, so no exception is needed",
     "The student is right, and the framework treats life as the one known exception",
     "Living things do not actually become more ordered as they grow",
     "The second law applies only to reactions catalyzed by enzymes",
     "The first law, not the second, is the one that life sets aside"],
   ans=0,
   why="EK 3.3.A.2 states that life requires a highly ordered system and does NOT violate the first and second laws of thermodynamics, and EK 3.3.A.2.i supplies the mechanism as an excess of input over loss."),

 dict(q="Which of these best describes a metabolic pathway as the framework defines it?",
   choices=[
     "A sequence of reactions in which each step supplies the material for the next",
     "A single reaction that converts a starting material directly into a final product",
     "A collection of unrelated reactions that happen to occur in one compartment",
     "A reaction that occurs only in organisms of one domain",
     "A process that requires no enzymes at any step"],
   ans=0,
   why="EK 3.3.A.3 defines the pathway by its linkage: it is sequential, and a product of one reaction is typically the reactant for the subsequent step. That linkage is what separates a pathway from a set of unconnected reactions."),

 dict(q="How does breaking an energy-releasing process into several sequential steps help a cell?",
   choices=[
     "It lets the cell capture energy in stages rather than releasing it all at once",
     "It increases the total amount of energy the process releases",
     "It removes the need for the cell to take in energy from outside",
     "It makes each step independent of the products of the previous step",
     "It converts the process into one that requires no enzymes"],
   ans=0,
   why="EK 3.3.A.3 gives control of the energy transfer as the reason pathways are sequential. Staging does not change the total energy involved, which EK 3.3.A.2 keeps under the first law."),

 dict(q="Which observation would most directly support the claim that a particular pathway is a core metabolic pathway in the framework's sense?",
   choices=[
     "The pathway is found in species from Archaea, Bacteria, and Eukarya alike",
     "The pathway is found in a large number of closely related eukaryotic species",
     "The pathway releases more energy than any other pathway in the cell",
     "The pathway uses enzymes that are unusually efficient",
     "The pathway occurs inside a membrane-bound organelle"],
   ans=0,
   why="Skill 6.C asks for evidence connected to the claim. EK 3.3.B.1 defines the category by distribution across all currently recognized domains, so a broad sample within one domain, a high energy yield or a particular location does not establish it."),

 dict(q="Two cells carry out the same sequential pathway, but one lacks the enzyme for the third of five steps. What difference is expected in the two cells?",
   choices=[
     "Only the cell with all five enzymes forms the pathway's final product",
     "Both cells form the final product, since the missing step can be skipped",
     "Only the cell missing an enzyme forms the final product",
     "Neither cell forms any intermediate compound at all",
     "The cell missing an enzyme forms the final product more quickly"],
   ans=0,
   why="EK 3.3.A.3 makes each product the reactant for the next step, so a missing step severs the sequence and nothing downstream of it is made. Skill 6.E asks for the effect of a disruption to one component of a system."),

 dict(q="An energy-requiring process in a cell proceeds even though it cannot occur on its own. Which explanation does the framework support?",
   choices=[
     "It is coupled to a process that releases energy",
     "It draws energy from the surroundings without any cellular process supplying it",
     "It creates the energy it needs as it proceeds",
     "It occurs because the cell is highly ordered, which removes the energy requirement",
     "It occurs only in organisms of a single domain"],
   ans=0,
   why="EK 3.3.A.2.ii states that cellular processes releasing energy may be coupled with cellular processes that require energy. Coupling is the framework's account of how a process that cannot proceed alone nevertheless proceeds."),

 dict(q="Which statement about cellular energy is NOT supported by the framework?",
   choices=[
     "A living system can maintain its order with no ongoing input of energy",
     "Energy input must exceed energy loss to maintain order",
     "Energy-releasing processes may be coupled to energy-requiring ones",
     "Core metabolic pathways occur in all three currently recognized domains",
     "A product of one step in a pathway is typically the reactant of the next"],
   ans=0,
   why="EK 3.3.A.1 requires an input of energy for all living systems and EK 3.3.A.2.i requires that input to exceed loss. The other four statements restate EK 3.3.A.2.i, EK 3.3.A.2.ii, EK 3.3.B.1 and EK 3.3.A.3 directly."),

 dict(q="An investigator finds that a pathway present in bacteria is absent from every archaeal and eukaryotic species tested. How should that pathway be classified against the framework's category?",
   choices=[
     "Not a conserved core pathway, because conservation is defined across all three domains",
     "A conserved core pathway, because it is present throughout one whole domain",
     "A conserved core pathway, because bacteria are the most numerous organisms",
     "Not a pathway at all, because a pathway must occur in eukaryotes",
     "A conserved core pathway only if it releases energy"],
   ans=0,
   why="EK 3.3.B.1 sets the criterion as conservation across all currently recognized domains, Archaea, Bacteria, and Eukarya. Presence throughout a single domain does not meet a criterion stated across three."),

 dict(q="Using the pathway concentration data, what happens to the compound immediately upstream of the blocked step?",
   table=_T_PATHWAY,
   choices=[
     "Its concentration rises well above the untreated value",
     "Its concentration falls close to zero",
     "Its concentration is unchanged by the treatment",
     "Its concentration falls below that of every other compound",
     "Its concentration cannot be compared between the two conditions"],
   ans=0,
   why="EK 3.3.A.3 makes each compound the reactant for the following step, so blocking that step leaves the compound entering it with no route forward and it accumulates. Skill 4.B asks students to identify the specific data points that show this."),

 dict(q="How does the conservation of core metabolic pathways relate to the framework's treatment of ribosomes, which are found in cells in all forms of life?",
   choices=[
     "Both are shared features read as evidence of descent from a common ancestor",
     "Both are features that arose independently in each lineage",
     "Ribosomes are evidence of ancestry but shared pathways are not",
     "Shared pathways are evidence of ancestry but ribosomes are not",
     "Neither bears on the relationships between organisms"],
   ans=0,
   why="EK 2.1.A.1 says ribosomes are found in cells in all forms of life and reflect the common ancestry in all known life, and EK 3.3.B.1 places core metabolic pathways across all three domains under a learning objective about common ancestry. The reasoning is the same in both cases."),

 dict(q="A dormant seed carries out metabolic processes at an extremely low rate. Which statement about it is consistent with the framework?",
   choices=[
     "It still requires an input of energy, since all living systems do",
     "It requires no energy at all while dormant, since its processes are slow",
     "It has become an exception to the requirement for ordered structure",
     "It obtains energy by reversing the second law of thermodynamics",
     "It maintains order without any relationship between input and loss"],
   ans=0,
   why="EK 3.3.A.1 states that ALL living systems require an input of energy, with no exemption for a low metabolic rate, and EK 3.3.A.2.i keeps the input-exceeds-loss requirement attached to maintaining order."),

 dict(q="Taken together, what do the framework's statements about cellular energy assert about living systems?",
   choices=[
     "They need a continuing energy surplus, run their energy transfers in controlled sequences, and share core pathways across all three domains",
     "They generate their own energy, run each transfer in a single step, and share no pathways between domains",
     "They need energy only during growth, and their pathways are unique to each species",
     "They are exceptions to thermodynamic law and therefore need no energy input",
     "They obtain energy only by coupling, and no pathway occurs in more than one domain"],
   ans=0,
   why="EK 3.3.A.1 and EK 3.3.A.2.i give the surplus requirement, EK 3.3.A.3 gives the sequential and controlled transfer, and EK 3.3.B.1 gives conservation across Archaea, Bacteria, and Eukarya."),
]
