# AP BIOLOGY 7.9 Phylogeny
# CED effective Fall 2025, Unit 7 Natural Selection, Big Idea 1 Evolution.
# Learning objectives 7.9.A (describe the types of evidence that can be used to
# infer an evolutionary relationship) and 7.9.B (explain how phylogenetic trees
# and cladograms can be used to infer evolutionary relatedness).
# Suggested skill 2.D, represent relationships within biological models,
# including mathematical models, diagrams, flowcharts, and systems.
#
# Essential knowledge relied on, in the framework's own terms:
#   7.9.A.1  phylogenetic trees and cladograms show HYPOTHETICAL evolutionary
#            relationships among lineages THAT CAN BE TESTED.
#   7.9.A.2  phylogenetic trees show the amount of change over time CALIBRATED
#            BY FOSSILS OR A MOLECULAR CLOCK, whereas cladograms do NOT show
#            time scale or the evolutionary difference between groups.
#   7.9.A.3  traits that are either gained or lost during evolution can be used
#            to construct phylogenetic trees and cladograms. THE OUT-GROUP
#            represents the lineage that is LEAST CLOSELY RELATED to the
#            remainder of the organisms in the tree or cladogram.
#              i. shared derived characters can be present in more than one
#                 lineage and indicate common ancestry; these are informative
#                 for the construction of trees and cladograms.
#             ii. molecular data TYPICALLY provide more accurate and reliable
#                 evidence than morphological traits in construction.
#   7.9.B.1  trees and cladograms can be used to illustrate speciation that has
#            occurred. THE NODES on a tree represent the MOST RECENT COMMON
#            ANCESTOR of any two groups or lineages.
#   7.9.B.2  they can be constructed from morphological similarities of LIVING
#            OR FOSSIL species and from DNA and protein sequence similarities.
#   7.9.B.3  they represent HYPOTHESES that are CONSTANTLY BEING REVISED based
#            on evidence.
#
# THE FIGURE PROBLEM, AND WHAT IS DONE ABOUT IT. This topic is about diagrams
# and the bank cannot carry one. SCIENCE_BRIEF.md is explicit that a stem must
# never say "the tree shown", so NOT ONE STEM HERE REFERS TO A DIAGRAM THAT IS
# NOT PRESENT. The data items instead carry the character matrix a cladogram
# would be built FROM, which is the same information in the form skill 2.D
# calls a model, and every question is asked of the matrix. The one table about
# trees and cladograms themselves is a feature-by-diagram table, not a picture.
#
# DELIBERATE OMISSIONS, to keep off neighbouring topics. Counting differences
# between sequences is EK 7.6.B.2 and is asked in b7_6, so no item here keys a
# relationship to a count of sequence differences; the relatedness items here
# turn on shared derived characters, on the out-group and on nodes. Speciation
# itself -- reproductive isolation, allopatry and sympatry, the rate of
# speciation -- is EK 7.10 and is asked in b7_10; the single item here that
# mentions speciation asks only what EK 7.9.B.1 says a diagram can illustrate.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: this bank is exported
# untypeset.
TOPIC = ("7.9", "Phylogeny", 7)

_T_CHARS = dict(
    headers=["Lineage", "Backbone", "Four limbs", "Amniotic egg", "Hair"],
    rows=[["Lineage W", "Absent", "Absent", "Absent", "Absent"],
          ["Lineage X", "Present", "Absent", "Absent", "Absent"],
          ["Lineage Y", "Present", "Present", "Absent", "Absent"],
          ["Lineage Z", "Present", "Present", "Present", "Absent"],
          ["Lineage V", "Present", "Present", "Present", "Present"]])

_T_DIAGRAMS = dict(
    headers=["Information the diagram carries", "Shown by a phylogenetic tree",
             "Shown by a cladogram"],
    rows=[["Proposed branching order of the lineages", "Yes", "Yes"],
          ["A scale of time", "Yes", "No"],
          ["The amount of evolutionary difference between groups", "Yes", "No"]])

QUESTIONS = [
 dict(q="What do phylogenetic trees and cladograms show?",
   choices=[
     "Hypothetical evolutionary relationships among lineages that can be tested",
     "The exact number of generations separating any two species",
     "Established relationships that no further evidence could revise",
     "The geographic range occupied by each lineage",
     "The order in which species will evolve in the future"], ans=0,
   why="EK 7.9.A.1 states that phylogenetic trees and cladograms show hypothetical evolutionary relationships among lineages that can be tested. Both halves matter: the relationships are proposed rather than settled, and they are open to evidence."),

 dict(q="The framework calls the relationships shown in a phylogenetic tree hypothetical. What does that description imply about them?",
   choices=[
     "They are proposals that evidence can support or overturn",
     "They are guesses for which no evidence can ever be gathered",
     "They are definitions and so cannot be wrong",
     "They apply only to species that are already extinct",
     "They describe what a researcher wishes were true rather than what was observed"], ans=0,
   why="EK 7.9.A.1 pairs the word hypothetical with the clause that the relationships CAN BE TESTED, and EK 7.9.B.3 adds that such diagrams are constantly being revised based on evidence. A hypothesis is testable, which is what separates it both from a definition and from a guess beyond the reach of evidence."),

 dict(q="Which statement best describes the status of a published phylogenetic tree over time?",
   choices=[
     "It is a hypothesis that is constantly revised as new evidence appears",
     "It is fixed once published, because revision would make the diagram useless",
     "It is revised only when the species it contains go extinct",
     "It becomes a definition of the group once it has been published",
     "It can be revised only by the researcher who first published it"], ans=0,
   why="EK 7.9.B.3 states that phylogenetic trees and cladograms represent hypotheses that are constantly being revised based on evidence. Revision in response to evidence is what the framework treats as the normal life of such a diagram."),

 dict(q="Which information does a phylogenetic tree carry that a cladogram does not?",
   choices=[
     "The amount of change over time, calibrated by fossils or a molecular clock",
     "The proposed branching order of the lineages",
     "The identity of the lineages being compared",
     "The characters used to build the diagram",
     "The fact that the relationships shown are hypothetical"], ans=0,
   why="EK 7.9.A.2 states that phylogenetic trees show the amount of change over time calibrated by fossils or a molecular clock, whereas cladograms do not show time scale or the evolutionary difference between groups. Branching order and the hypothetical status belong to both kinds of diagram."),

 dict(q="According to the framework, which of the following does a cladogram NOT show?",
   choices=[
     "A time scale or the evolutionary difference between groups",
     "A proposed pattern of relationship among the lineages included",
     "Which lineages are being compared",
     "A hypothesis open to testing",
     "Groupings based on the characters used to build it"], ans=0,
   why="EK 7.9.A.2 says in as many words that cladograms do not show time scale or the evolutionary difference between groups. Everything else listed is what any such diagram carries under EK 7.9.A.1 and EK 7.9.A.3."),

 dict(q="A researcher needs a diagram that will show how much evolutionary change has accumulated between two groups as well as the order in which lineages branched. Which should the researcher use, and why?",
   choices=[
     "A phylogenetic tree, because it represents the amount of change over time and a cladogram does not",
     "A cladogram, because it represents the amount of change and a tree does not",
     "Either one, because the two carry identical information",
     "Neither, because no diagram can represent branching order",
     "A cladogram, because branching order is shown only there"], ans=0,
   why="EK 7.9.A.2 assigns the amount of change over time to the phylogenetic tree and denies it to the cladogram, while EK 7.9.A.1 gives the proposed relationships to both. Only the tree carries both pieces of information the researcher asks for."),

 dict(q="The amount of change shown on a phylogenetic tree is calibrated by which of the following?",
   choices=[
     "Fossils or a molecular clock",
     "The number of lineages included in the diagram",
     "The geographic distance between the lineages",
     "The number of characters scored for each lineage",
     "The order in which the lineages were discovered"], ans=0,
   why="EK 7.9.A.2 names fossils or a molecular clock as the calibration for the amount of change over time that a phylogenetic tree shows. Without one of those, a diagram carries branching order but no scale."),

 dict(q="Which kinds of trait can be used to construct phylogenetic trees and cladograms?",
   choices=[
     "Traits that are either gained or lost during evolution",
     "Only traits that are gained, since a lost trait leaves no record",
     "Only traits present in every lineage being compared",
     "Only traits that can be measured in living species",
     "Only traits that have no effect on survival"], ans=0,
   why="EK 7.9.A.3 states that traits that are either gained or lost during evolution can be used to construct phylogenetic trees and cladograms. A trait present in every lineage separates none of them, which is why universality is not the criterion."),

 dict(q="What does the out-group represent in a phylogenetic tree or cladogram?",
   choices=[
     "The lineage least closely related to the remainder of the organisms in the diagram",
     "The lineage most closely related to the others in the diagram",
     "The lineage with the greatest number of species",
     "The lineage that is known only from fossils",
     "The lineage in which the greatest amount of change has occurred"], ans=0,
   why="EK 7.9.A.3 states that the out-group represents the lineage that is least closely related to the remainder of the organisms in the phylogenetic tree or cladogram. Number of species, fossil status and amount of change are not what defines the role."),

 dict(q="A cladogram proposes a particular set of relationships among six lineages. Which of the following would count as testing that proposal?",
   choices=[
     "Scoring additional characters or sequences and checking whether the same grouping results",
     "Redrawing the same diagram with the lineages in a different left-to-right order",
     "Counting how many lineages the diagram contains",
     "Asking whether the diagram is easy to read",
     "Adding a time scale to the same diagram without new data"], ans=0,
   why="EK 7.9.A.1 says the relationships shown can be tested, and EK 7.9.B.3 says the diagrams are revised on evidence. A test requires new evidence that could have come out otherwise; rearranging or annotating the existing diagram adds none."),

 dict(q="What do shared derived characters indicate, according to the framework?",
   choices=[
     "Common ancestry of the lineages that share them",
     "That the lineages sharing them occupy the same habitat",
     "That the lineages sharing them are the same species",
     "That the character arose independently in each lineage",
     "The amount of time since the lineages separated"], ans=0,
   why="EK 7.9.A.3 states that shared derived characters can be present in more than one lineage and indicate common ancestry. The statement makes no claim about habitat, species identity or elapsed time, the last of which EK 7.9.A.2 assigns to a calibrated tree."),

 dict(q="Why does the framework describe shared derived characters as informative for the construction of trees and cladograms?",
   choices=[
     "Because a character shared by some lineages and not others groups those lineages together",
     "Because such characters are always easier to measure than other characters",
     "Because they occur in only one lineage at a time",
     "Because they show how long ago each lineage arose",
     "Because they are the only characters that can be lost during evolution"], ans=0,
   why="EK 7.9.A.3 says shared derived characters can be present in more than one lineage, indicate common ancestry, and are informative for construction. Being present in some lineages and absent in others is exactly what divides a set of lineages into groups."),

 dict(q="How does the framework compare molecular data with morphological traits as evidence for constructing a phylogenetic tree or cladogram?",
   choices=[
     "Molecular data typically provide more accurate and reliable evidence than morphological traits",
     "Morphological traits are always more reliable, because they can be seen directly",
     "The two kinds of evidence are equally reliable in every case",
     "Molecular data may be used only for living species",
     "Morphological traits may be used only for fossil species"], ans=0,
   why="EK 7.9.A.3 states that molecular data typically provide more accurate and reliable evidence than morphological traits in the construction of phylogenetic trees or cladograms. EK 7.9.B.2 separately allows morphological data from both living and fossil species, so neither kind of evidence is restricted as the last two options claim."),

 dict(q="The framework says molecular data TYPICALLY provide more accurate and reliable evidence than morphological traits. What does that qualifier allow?",
   choices=[
     "That the comparison is a general tendency, so a particular morphological data set may still be the better evidence",
     "That molecular data are never wrong",
     "That morphological data should never be collected",
     "That the two kinds of data can never be used in the same study",
     "That the comparison holds only for extinct species"], ans=0,
   why="EK 7.9.A.3 writes typically rather than always, and EK 7.9.B.2 continues to name morphological similarities of living or fossil species as a basis for construction. A stated tendency does not license either an absolute or the abandonment of the other data source."),

 dict(q="What does a node on a phylogenetic tree represent?",
   choices=[
     "The most recent common ancestor of any two groups or lineages that meet there",
     "A species alive today that gave rise to the others",
     "The moment at which a character was lost",
     "The out-group of the whole diagram",
     "The total amount of change along a branch"], ans=0,
   why="EK 7.9.B.1 states that the nodes on a tree represent the most recent common ancestor of any two groups or lineages. An ancestor at a node is not one of the tips of the diagram, so it is not a species alive today."),

 dict(q="According to the framework, phylogenetic trees and cladograms can be used to illustrate which of the following?",
   choices=[
     "Speciation that has already occurred",
     "The precise number of species that will exist in the future",
     "The population size of each lineage",
     "The habitat each lineage occupies",
     "The rate at which each lineage reproduces"], ans=0,
   why="EK 7.9.B.1 states that phylogenetic trees and cladograms can be used to illustrate speciation that has occurred. Population size, habitat and reproductive rate are not represented on such a diagram at all."),

 dict(q="From which of the following can phylogenetic trees and cladograms be constructed?",
   choices=[
     "Morphological similarities of living or fossil species and DNA and protein sequence similarities",
     "Morphological similarities of living species only",
     "DNA sequence similarities only",
     "The geographic ranges of the species being compared",
     "The abundance of each species in its habitat"], ans=0,
   why="EK 7.9.B.2 names exactly those sources: morphological similarities of living or fossil species, and DNA and protein sequence similarities. Restricting the list to one source, or replacing it with range or abundance, contradicts the statement."),

 dict(q="Which of the following is NOT named by the framework as a basis for constructing a phylogenetic tree or cladogram?",
   choices=[
     "The number of individuals of each species counted in a survey",
     "Morphological similarities among living species",
     "Morphological similarities among fossil species",
     "DNA sequence similarities",
     "Protein sequence similarities"], ans=0,
   why="EK 7.9.B.2 lists morphological similarities of living or fossil species and DNA and protein sequence similarities. Abundance is a measure of how many individuals are present now, which says nothing about the characters that group lineages together."),

 dict(q="The table records whether each of five lineages possesses four characters. Which lineage would serve as the out-group for the remaining four?",
   table=_T_CHARS,
   choices=["Lineage W", "Lineage X", "Lineage Y", "Lineage Z", "Lineage V"], ans=0,
   why="EK 7.9.A.3 defines the out-group as the lineage least closely related to the remainder. Shared derived characters indicate common ancestry, so the lineage that shares none of the four characters with the others is the one least closely related to them."),

 dict(q="Using the same table of five lineages and four characters, which pair shares the greatest number of characters in the present state?",
   table=_T_CHARS,
   choices=["Lineage Z and Lineage V", "Lineage W and Lineage X", "Lineage X and Lineage Y",
            "Lineage Y and Lineage Z", "Lineage W and Lineage V"], ans=0,
   why="EK 7.9.A.3 makes shared derived characters informative for construction, because a character shared by two lineages and absent from others groups those two together. Counting the characters present in both members of each pair identifies the pair sharing the most."),

 dict(q="In that same character table, which character is present in the greatest number of lineages?",
   table=_T_CHARS,
   choices=["Backbone", "Four limbs", "Amniotic egg", "Hair",
            "All four characters are present in the same number of lineages"], ans=0,
   why="Skill 4.B, identifying specific data points across a table. Reading each character column and counting the lineages in which it is present gives the answer, and a character present in more lineages groups a larger set of them together under EK 7.9.A.3."),

 dict(q="Which character in that table is present in only one of the five lineages?",
   table=_T_CHARS,
   choices=["Hair", "Backbone", "Four limbs", "Amniotic egg",
            "Every character is present in at least two lineages"], ans=0,
   why="Skill 4.B again. A character present in a single lineage is not shared, so under EK 7.9.A.3 it cannot group that lineage with any other, however useful it may be for describing the lineage itself."),

 dict(q="How many of the five lineages in that table possess an amniotic egg?",
   table=_T_CHARS,
   choices=["Two", "One", "Three", "Four", "Five"], ans=0,
   why="Skill 4.B, identifying specific data points. Counting the entries recorded as present in the named character's column gives the number, which is the first step in using that character to group lineages under EK 7.9.A.3."),

 dict(q="A sixth lineage is scored for the same four characters and is found to have a backbone and four limbs but neither of the other two characters. Which lineage in the table has exactly the same set of characters present?",
   table=_T_CHARS,
   choices=["Lineage Y", "Lineage W", "Lineage X", "Lineage Z", "Lineage V"], ans=0,
   why="EK 7.9.A.3 makes shared derived characters the basis for grouping lineages. Matching the described set of present characters against each row of the table finds the lineage whose scored characters agree with it in every column."),

 dict(q="The table compares what a phylogenetic tree and a cladogram each carry. Which rows record information that only one of the two diagrams carries?",
   table=_T_DIAGRAMS,
   choices=[
     "The row for a scale of time and the row for the amount of evolutionary difference",
     "The row for the proposed branching order only",
     "All three rows, since the two diagrams share nothing",
     "None of the rows, since the two diagrams carry the same information",
     "The row for a scale of time only"], ans=0,
   why="EK 7.9.A.2 states that cladograms do not show time scale or the evolutionary difference between groups, while EK 7.9.A.1 gives the proposed relationships to both kinds of diagram. The table check confirms which rows differ between the two columns."),

 dict(q="A student must choose between the two diagrams in that table for a project that requires showing when each branching event occurred. Which choice does the table support?",
   table=_T_DIAGRAMS,
   choices=[
     "The phylogenetic tree, because it is the only one of the two that carries a scale of time",
     "The cladogram, because it is the only one of the two that carries a scale of time",
     "Either diagram, because both carry a scale of time",
     "Neither diagram, because neither carries a scale of time",
     "The cladogram, because it carries the proposed branching order"], ans=0,
   why="EK 7.9.A.2 assigns a time scale to the phylogenetic tree and denies it to the cladogram, and the table records exactly that. Branching order is carried by both and so cannot decide between them."),

 dict(q="Which of the following does a node on a phylogenetic tree NOT represent?",
   choices=[
     "A living species from which the branches above it are descended",
     "The most recent common ancestor of the two lineages that meet there",
     "A point of common ancestry inferred from the evidence used to build the tree",
     "A feature of a diagram that is a hypothesis rather than an observation",
     "A point that a revision of the tree could relocate"], ans=0,
   why="EK 7.9.B.1 identifies a node as the most recent common ancestor of any two groups or lineages, which is an ancestral form and not one of the present-day tips. EK 7.9.A.1 and EK 7.9.B.3 make everything at a node part of a hypothesis open to revision."),

 dict(q="Two research groups publish different trees for the same set of lineages. What should decide between them?",
   choices=[
     "Which tree the available evidence better supports, since each is a hypothesis",
     "Which tree was published first",
     "Which tree contains more lineages",
     "Which tree is simpler to draw",
     "Neither, because two trees for one group cannot both exist"], ans=0,
   why="EK 7.9.A.1 makes these diagrams hypotheses that can be tested and EK 7.9.B.3 makes them subject to constant revision based on evidence. Competing hypotheses about the same lineages are settled by the evidence bearing on them, not by priority or convenience."),

 dict(q="A cladogram built from morphological characters is redrawn after DNA and protein sequence data are added, and two lineages change position. Which statements of the framework does this best illustrate?",
   choices=[
     "That such diagrams are hypotheses revised on evidence, and that molecular data typically provide more accurate and reliable evidence",
     "That morphological characters cannot be used to build a cladogram",
     "That a cladogram cannot be revised once it has been drawn",
     "That the two lineages have changed since the first diagram was drawn",
     "That molecular and morphological data can never be used together"], ans=0,
   why="EK 7.9.B.3 makes revision on evidence the normal case, and EK 7.9.A.3 states that molecular data typically provide more accurate and reliable evidence than morphological traits. EK 7.9.B.2 keeps morphological similarities among the admissible sources, so the second option overstates the point."),

 dict(q="Summarizing this topic, which pair of statements correctly distinguishes a cladogram from a phylogenetic tree?",
   choices=[
     "Both propose a testable pattern of relationship, but only the tree carries a time scale and the amount of evolutionary difference",
     "Both carry a time scale, but only the cladogram proposes a pattern of relationship",
     "Only the cladogram is a hypothesis; the tree is an established result",
     "Only the tree can be built from molecular data; the cladogram requires morphology",
     "The two are alternative names for the same diagram"], ans=0,
   why="EK 7.9.A.1 gives both diagrams the status of testable hypotheses about relationships, and EK 7.9.A.2 gives the time scale and the amount of evolutionary difference to the tree alone. EK 7.9.B.2 allows both to be built from either kind of data."),
]
