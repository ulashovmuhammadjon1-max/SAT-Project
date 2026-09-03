# AP BIOLOGY 7.7 Common Ancestry
# CED effective Fall 2025, Unit 7 Natural Selection, Big Idea 1 Evolution.
# Learning objective 7.7.A, describe structural and functional evidence on
# CELLULAR AND MOLECULAR LEVELS that provides evidence for the common ancestry
# of all eukaryotes.
# Suggested skill 6.E, predict the causes or effects of a change in, or
# disruption to, one or more components in a biological system.
#
# Essential knowledge relied on, in the framework's own terms:
#   7.7.A.1  structural and functional evidence indicates common ancestry of
#            ALL EUKARYOTES. This evidence includes:
#              i. membrane-bound organelles
#             ii. linear chromosomes
#            iii. genes that contain introns
#
# THIS TOPIC HAS ONE ESSENTIAL KNOWLEDGE STATEMENT, and thirty questions on one
# sentence is how the Comparative Government bank produced its repeats. The
# answer used here is the one SOCIAL_DEDUPE.md records for US Government 4.7:
# every item CHAINS 7.7.A.1 to a statement elsewhere in this same CED that says
# what one of the three features IS, so the question is one neither topic can
# ask alone. The statements chained, all quoted from the framework:
#   2.10.A.2  prokaryotes TYPICALLY lack internal membrane-bound organelles but
#             have internal regions with specialized structures and functions
#   2.10.A.3  eukaryotic cells maintain internal membranes that partition the
#             cell into specialized regions
#   2.9.A.1   membranes and membrane-bound organelles in eukaryotic cells
#             compartmentalize intracellular metabolic processes
#   6.1.A.1i  prokaryotic organisms TYPICALLY have circular chromosomes
#   6.1.A.1ii eukaryotic organisms typically have MULTIPLE LINEAR chromosomes
#             comprised of DNA, condensed using histones and associated proteins
#   6.1.A.2   prokaryotes and eukaryotes can contain plasmids, which are
#             extra-chromosomal circular molecules of DNA
#   6.3.A.4iii the excision of introns, along with the splicing and retention of
#             exons, generates different versions of the mature mRNA molecule
#
# WHAT IS DELIBERATELY NOT HERE. Endosymbiosis (EK 2.10.A.1) is the subject of
# b2_10 and is not keyed anywhere in this module; the sibling bank already asks
# it eight ways. The FUNCTION of compartmentalization (EK 2.9.B.1) is b2_9's
# subject and appears here only where the framework's own phrase "structural
# and functional" requires it. Homologous structures, vestigial structures and
# sequence comparison are EK 7.6.B and are asked in b7_6.
#
# The framework's own hedge is preserved throughout: prokaryotes TYPICALLY lack
# membrane-bound organelles and TYPICALLY have circular chromosomes. No item
# here keys an absolute where the CED writes a typical, and no item asserts
# anything about introns in prokaryotes, on which the CED is silent.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: this bank is exported
# untypeset.
TOPIC = ("7.7", "Common Ancestry", 7)

_T_SURVEY = dict(
    headers=["Eukaryotic group surveyed", "Number of species examined",
             "Number found to have membrane-bound organelles",
             "Number found to have linear chromosomes",
             "Number found to have genes that contain introns"],
    rows=[["Group 1", "40", "40", "40", "40"],
          ["Group 2", "25", "25", "25", "25"],
          ["Group 3", "35", "35", "35", "35"]])

_T_CHROM = dict(
    headers=["Cell examined", "Form of the main chromosome",
             "Number of main chromosomes"],
    rows=[["Cell E", "Linear", "8"],
          ["Cell F", "Linear", "14"],
          ["Cell G", "Linear", "23"]])

QUESTIONS = [
 dict(q="Which set of features does the course framework name as the structural and functional evidence for the common ancestry of all eukaryotes?",
   choices=[
     "Membrane-bound organelles, linear chromosomes, and genes that contain introns",
     "A cell wall, a plasma membrane, and ribosomes",
     "Circular chromosomes, plasmids, and an internal region holding the chromosome",
     "Membrane-bound organelles, circular chromosomes, and genes without introns",
     "Plasmids, cell walls, and a single chromosome"], ans=0,
   why="EK 7.7.A.1 lists exactly those three features as the evidence indicating common ancestry of all eukaryotes. A plasma membrane and ribosomes are found in every form of life and so distinguish nothing, and circular chromosomes and plasmids are what EK 6.1.A.1 and EK 6.1.A.2 describe."),

 dict(q="Learning objective 7.7.A asks for evidence of the common ancestry of eukaryotes drawn from which levels of biological organization?",
   choices=["The cellular and molecular levels", "The population and community levels",
            "The ecosystem and biome levels", "The organ and organ system levels",
            "The fossil record alone"], ans=0,
   why="Learning objective 7.7.A specifies structural and functional evidence on cellular and molecular levels. Membrane-bound organelles are a cellular feature and genes containing introns a molecular one, which is why the objective names both."),

 dict(q="All eukaryotes examined so far possess membrane-bound organelles, linear chromosomes, and genes containing introns. What does the framework take that shared possession to indicate?",
   choices=[
     "That all eukaryotes descend from a common ancestor",
     "That all eukaryotes occupy similar habitats",
     "That eukaryotes and prokaryotes are equally closely related to one another",
     "That each eukaryotic lineage acquired the three features independently",
     "That the three features perform the same function in every species"], ans=0,
   why="EK 7.7.A.1 states that this structural and functional evidence indicates common ancestry of all eukaryotes. Inheritance from one ancestor is what explains a feature being present in every descendant without each lineage having to acquire it separately."),

 dict(q="A newly described single-celled organism is found to have a nucleus, mitochondria, and other membrane-bound compartments. Which of the three lines of evidence named for eukaryotic common ancestry does this observation supply?",
   choices=["Membrane-bound organelles", "Linear chromosomes", "Genes that contain introns",
            "The presence of plasmids", "A circular chromosome"], ans=0,
   why="EK 7.7.A.1 lists membrane-bound organelles first among the three. EK 2.10.A.3 describes eukaryotic cells as maintaining internal membranes that partition the cell into specialized regions, which is what the observation reports."),

 dict(q="The framework states that prokaryotes typically lack internal membrane-bound organelles. How does that statement bear on the use of membrane-bound organelles as evidence of eukaryotic common ancestry?",
   choices=[
     "A feature present throughout eukaryotes and typically absent from prokaryotes marks the eukaryotes off as a group with a shared history",
     "It shows that prokaryotes and eukaryotes have no common ancestry of any kind",
     "It shows that membrane-bound organelles arose separately in every eukaryotic lineage",
     "It means membrane-bound organelles cannot be used as evidence, because the statement says only typically",
     "It shows that prokaryotes have no internal organization at all"], ans=0,
   why="EK 2.10.A.2 says prokaryotes typically lack internal membrane-bound organelles but have internal regions with specialized structures and functions, so the second and fifth options misread it. A feature general within one group and not the other is what makes it useful evidence about that group's history under EK 7.7.A.1."),

 dict(q="Prokaryotic organisms typically have circular chromosomes, while eukaryotic organisms typically have multiple linear chromosomes. Which conclusion does the framework draw from the second of these facts?",
   choices=[
     "The linear form of the chromosome is one of the features indicating common ancestry of all eukaryotes",
     "Chromosome form shows that eukaryotes reproduce more rapidly than prokaryotes",
     "Chromosome form is unrelated to evolutionary history",
     "The number of chromosomes is the feature that indicates common ancestry",
     "Circular chromosomes indicate common ancestry of all eukaryotes"], ans=0,
   why="EK 7.7.A.1 names linear chromosomes as the second line of evidence, and EK 6.1.A.1 supplies the contrast, that prokaryotes typically have circular chromosomes and eukaryotes multiple linear ones. The framework names the form, not the number."),

 dict(q="Eukaryotic species differ enormously in how many chromosomes they carry, yet the framework still treats chromosomes as evidence of common ancestry. The reason is that",
   choices=[
     "the feature named as evidence is the linear form of the chromosome, which is shared, and not the number, which is not",
     "chromosome number is the same in all eukaryotes once plasmids are excluded",
     "chromosome number is the only feature the framework names",
     "differences in number are evidence that eukaryotes have no common ancestor",
     "chromosome number cannot be counted reliably in most species"], ans=0,
   why="EK 7.7.A.1 names linear chromosomes, and EK 6.1.A.1 describes eukaryotes as typically having MULTIPLE linear chromosomes without fixing a number. A shared feature is evidence of shared ancestry; a variable one is not, which is why the framework names the form."),

 dict(q="Eukaryotic linear chromosomes are described in the framework as comprised of DNA and condensed using histones and associated proteins. Adding this detail to the evidence for eukaryotic common ancestry does which of the following?",
   choices=[
     "It supplies a further shared molecular feature of the same chromosomes the framework already names",
     "It replaces the linear form as the feature that indicates ancestry",
     "It shows that eukaryotic chromosomes are not really linear",
     "It shows that histones are found in every form of life",
     "It shows that chromosome condensation prevents inheritance"], ans=0,
   why="EK 6.1.A.1 states that eukaryotic linear chromosomes are condensed using histones and associated proteins, so this is a molecular property of the very structure EK 7.7.A.1 names. It adds to the evidence rather than replacing it, and the framework does not claim histones for all life."),

 dict(q="A gene in a newly studied organism contains stretches of sequence that are removed from the transcript, while the remaining stretches are joined together before the message is translated. The removed stretches are",
   choices=["introns", "exons", "plasmids", "histones", "codons"], ans=0,
   why="EK 6.3.A.4 states that the excision of introns, along with the splicing and retention of exons, generates the mature mRNA molecule. So the removed stretches are introns and the retained ones exons, and EK 7.7.A.1 names genes containing introns as evidence of eukaryotic common ancestry."),

 dict(q="Why does the framework treat the presence of genes containing introns as evidence about eukaryotic ancestry rather than as a fact about one species?",
   choices=[
     "The feature is found across eukaryotes, and a feature general to a group is explained by inheritance from the group's ancestor",
     "Introns are the only part of a gene that is inherited",
     "Introns are removed from the transcript, so they cannot vary between species",
     "The presence of introns determines the habitat a species can occupy",
     "Introns are found in every known organism, so they identify no group at all"], ans=0,
   why="EK 7.7.A.1 offers the three features as evidence about ALL eukaryotes, which is a claim about the group. Generality within a group is what an inherited ancestral feature produces, and it is why one species' introns would not by itself be evidence of ancestry."),

 dict(q="Which of the following would most directly challenge the claim that the three named features are shared by all eukaryotes?",
   choices=[
     "A carefully verified eukaryote in which none of the three features is present",
     "A prokaryote that has an internal region with a specialized function",
     "A eukaryote whose chromosome number differs from that of its closest relatives",
     "A eukaryote in which one gene happens to contain no introns",
     "A prokaryote that carries a plasmid"], ans=0,
   why="EK 7.7.A.1 is a claim about all eukaryotes, so only a eukaryote lacking the features bears on it. EK 2.10.A.2 already allows prokaryotes internal specialized regions and EK 6.1.A.2 already allows both groups plasmids, so neither of those observations is a surprise to the framework."),

 dict(q="A eukaryotic lineage is found to have lost one of the three features named as evidence for eukaryotic common ancestry. What is the most defensible response?",
   choices=[
     "Treat the remaining two features as evidence and investigate the loss as a change within the lineage",
     "Conclude that eukaryotes have no common ancestor",
     "Conclude that the lineage is prokaryotic",
     "Discard all three features as evidence for every eukaryote",
     "Conclude that the lineage acquired its other two features independently"], ans=0,
   why="EK 7.7.A.1 offers three lines of evidence rather than one, so the loss of one leaves two standing. Reclassifying the lineage or discarding the framework's evidence entirely both treat a single observation as decisive against a body of converging evidence."),

 dict(q="Which observation about two species would NOT be evidence about their common ancestry under this topic?",
   choices=[
     "The two species are found in the same pond",
     "Both species have chromosomes that are linear rather than circular",
     "Both species have genes interrupted by introns",
     "Both species have compartments bounded by internal membranes",
     "Both species carry the same three cellular and molecular features the framework names"], ans=0,
   why="EK 7.7.A.1 names structural and functional features of the cell and its molecules. Where two species happen to live is a fact about their present environment and can be true of unrelated organisms, so it is not among the evidence this objective describes."),

 dict(q="Which of the following is NOT one of the three features the framework names as evidence for the common ancestry of all eukaryotes?",
   choices=["A plasma membrane surrounding the cell", "Membrane-bound organelles",
            "Linear chromosomes", "Genes that contain introns",
            "Internal membranes partitioning the cell into specialized regions"], ans=0,
   why="EK 7.7.A.1 names membrane-bound organelles, linear chromosomes and genes containing introns. A plasma membrane bounds cells of every kind, so it separates no group from another and appears nowhere in the statement."),

 dict(q="A student proposes using a feature shared by every known form of life as evidence for the common ancestry of eukaryotes specifically. The weakness of this proposal is that",
   choices=[
     "a feature present in every organism cannot distinguish eukaryotes from anything else",
     "features shared by all life are too difficult to measure",
     "the framework does not accept evidence from the molecular level",
     "such a feature would have to have arisen independently in each lineage",
     "the framework accepts only evidence from extinct organisms"], ans=0,
   why="EK 7.7.A.1's three features are offered as evidence about eukaryotes as a group, which requires that they mark that group off. Universality across all life is compatible with any hypothesis about eukaryotes and so discriminates among none of them."),

 dict(q="The framework describes the evidence in this topic as both structural and functional. Which pairing illustrates that description?",
   choices=[
     "The organelle is a structure, and compartmentalizing metabolic processes inside it is what it does",
     "The organelle is a structure, and the chromosome is another structure",
     "Structural evidence comes from living species and functional evidence from fossils",
     "Structural evidence is molecular and functional evidence is ecological",
     "Structure and function are different words for the same evidence"], ans=0,
   why="EK 2.9.A.1 states that membranes and membrane-bound organelles in eukaryotic cells compartmentalize intracellular metabolic processes and specific enzymatic reactions, which is the function of the structure EK 7.7.A.1 names. Naming both is what the objective's phrase requires."),

 dict(q="Which pairing correctly assigns one of the three named features to the cellular level and another to the molecular level?",
   choices=[
     "Membrane-bound organelles are a cellular feature and genes containing introns a molecular one",
     "Membrane-bound organelles are a molecular feature and introns a cellular one",
     "Both membrane-bound organelles and introns are ecological features",
     "Linear chromosomes are an organ-level feature and introns a population-level one",
     "All three named features belong to the same single level"], ans=0,
   why="Learning objective 7.7.A asks for evidence on cellular and molecular levels. An organelle is a component of a cell and an intron a stretch of sequence within a gene, so the two named features sit at those two levels respectively."),

 dict(q="Three groups of eukaryotic species were surveyed for the features named in this topic, with the results in the table. How many species were examined in total?",
   table=_T_SURVEY,
   choices=["100", "40", "75", "60", "120"], ans=0,
   why="Skill 4.B, identifying and combining specific data points. Adding the numbers of species examined across the three groups gives the total, which is the denominator for any statement about how general the features are."),

 dict(q="In that same survey of three eukaryotic groups, what percentage of all the species examined belonged to Group 2?",
   table=_T_SURVEY,
   choices=["25 percent", "35 percent", "40 percent", "75 percent", "60 percent"], ans=0,
   why="Skill 5.A includes percentages. The number of species in the named group is divided by the total examined across all three groups, and both numbers are read directly from the table."),

 dict(q="Which conclusion is best supported by the survey results for those three eukaryotic groups?",
   table=_T_SURVEY,
   choices=[
     "Every species examined carried all three features, which is the pattern inheritance from a shared ancestor predicts",
     "The three features were found in some groups and not others, so they cannot be ancestral",
     "The survey shows that prokaryotes lack all three features",
     "The survey shows how long ago the three groups last shared an ancestor",
     "The three features must have arisen independently in each of the three groups"], ans=0,
   why="EK 7.7.A.1 makes the three features evidence of common ancestry of all eukaryotes, and the counts match the number of species examined in every row and every column. The survey covers no prokaryotes and carries no dates, so neither of those conclusions is available from it."),

 dict(q="The table reports the chromosomes of three eukaryotic cells. Which feature of these cells does the framework name as evidence for the common ancestry of all eukaryotes?",
   table=_T_CHROM,
   choices=["The linear form shared by the chromosomes of all three cells",
            "The number of chromosomes, which differs among the three cells",
            "The fact that all three cells were examined in the same study",
            "The presence of plasmids in all three cells",
            "The circular form of the chromosomes"], ans=0,
   why="EK 7.7.A.1 names linear chromosomes. The table shows one column constant across the three cells and one column varying, and only the constant column reports a shared feature that inheritance from a common ancestor would explain."),

 dict(q="Using the same table of three eukaryotic cells, what does the variation in the second measured column show?",
   table=_T_CHROM,
   choices=[
     "Eukaryotes vary in chromosome number, so that number is not the feature the framework names as evidence",
     "The three cells cannot all be eukaryotic",
     "Chromosome number increases as chromosomes become more linear",
     "The cell with the most chromosomes is the ancestor of the other two",
     "The variation shows that none of the three cells shares ancestry with the others"], ans=0,
   why="EK 6.1.A.1 describes eukaryotes as typically having multiple linear chromosomes without fixing a number, and EK 7.7.A.1 names the linear form rather than the count. A column that varies across the group cannot be the shared feature evidence of shared ancestry rests on."),

 dict(q="A microbiologist wants to test whether a newly isolated microbe shares ancestry with known eukaryotes. Which investigation would bear most directly on that question?",
   choices=[
     "Determining whether the microbe has membrane-bound organelles, linear chromosomes, and genes containing introns",
     "Measuring how quickly the microbe grows in culture at several temperatures",
     "Recording the depth of the water from which the microbe was isolated",
     "Counting how many microbes were present in the original sample",
     "Determining whether the microbe can survive without oxygen"], ans=0,
   why="EK 7.7.A.1 names those three features as the structural and functional evidence indicating common ancestry of eukaryotes, so looking for them is looking for the evidence the objective specifies. Growth rate, depth, abundance and oxygen tolerance are ecological or physiological facts about the isolate."),

 dict(q="A researcher argues that because a prokaryotic cell has internal regions with specialized structures and functions, membrane-bound organelles are worthless as evidence of eukaryotic ancestry. The best reply is that",
   choices=[
     "the framework already grants prokaryotes such regions while distinguishing them from membrane-bound organelles",
     "prokaryotic cells have no internal structure of any kind",
     "the argument is correct, so the framework should drop the first line of evidence",
     "internal regions and membrane-bound organelles are the same thing",
     "only fossil evidence can settle questions of ancestry"], ans=0,
   why="EK 2.10.A.2 says in one sentence that prokaryotes typically lack internal membrane-bound organelles BUT have internal regions with specialized structures and functions, so the observation is part of the framework's own account rather than a counterexample to it."),

 dict(q="Both prokaryotes and eukaryotes can contain plasmids. Why does the framework not list plasmids among the evidence for the common ancestry of eukaryotes?",
   choices=[
     "A feature found in both groups does not mark eukaryotes off as a group with a shared history",
     "Plasmids are not made of DNA",
     "Plasmids are found only in extinct organisms",
     "Plasmids are linear, and the framework names circular structures",
     "Plasmids cannot be observed in living cells"], ans=0,
   why="EK 6.1.A.2 states that prokaryotes and eukaryotes can both contain plasmids, which are extra-chromosomal circular molecules of DNA. EK 7.7.A.1's three features are offered as evidence about eukaryotes specifically, and a feature shared with the other group cannot serve that purpose."),

 dict(q="An organism is found to have linear chromosomes and genes containing introns, but its organelles are too small to resolve with the microscope available. What is the most defensible statement about its ancestry?",
   choices=[
     "Two of the three lines of evidence already point to shared ancestry with other eukaryotes, and the third remains to be examined",
     "No conclusion is possible until all three features have been observed",
     "The organism is a prokaryote, because one feature could not be confirmed",
     "The organism acquired its linear chromosomes independently of other eukaryotes",
     "The two observed features are evidence against shared ancestry"], ans=0,
   why="EK 7.7.A.1 lists three features as evidence, not as a definition requiring all three to be checked. Two present features are evidence and an unexamined third is missing data, which is a different thing from evidence of absence."),

 dict(q="Which statement best describes the status of the claim that all eukaryotes share a common ancestor?",
   choices=[
     "It is a claim supported by structural and functional evidence and open to test by further observation",
     "It is a definition, so no observation could bear on it",
     "It is a claim about which no evidence exists",
     "It is settled by the fossil record alone",
     "It is a value judgement rather than an empirical claim"], ans=0,
   why="EK 7.7.A.1 says the structural and functional evidence INDICATES common ancestry, which is the language of a supported claim rather than of a definition. A claim resting on observations is one further observations can bear on."),

 dict(q="Two cells are compared. One has internal membranes partitioning it into specialized regions; the other has a single interior space bounded only by its plasma membrane. Under the framework's account, which statement about the first cell is best supported?",
   choices=[
     "It shows the organization the framework attributes to eukaryotic cells",
     "It must be older than the second cell",
     "It must reproduce more rapidly than the second cell",
     "It has no chromosomes",
     "It is the direct ancestor of the second cell"], ans=0,
   why="EK 2.10.A.3 states that eukaryotic cells maintain internal membranes that partition the cell into specialized regions, and EK 7.7.A.1 makes membrane-bound organelles the first line of evidence about eukaryotic ancestry. Nothing in either statement licenses a claim about age, reproductive rate or direct descent."),

 dict(q="A student writes that because eukaryotic cells compartmentalize their metabolic processes, compartmentalization must have evolved separately in each eukaryotic lineage. Which flaw does this reasoning contain?",
   choices=[
     "A feature present throughout a group is more simply explained by inheritance from the group's ancestor than by repeated independent origin",
     "Compartmentalization has no function, so it cannot have evolved",
     "Metabolic processes are not compartmentalized in eukaryotic cells",
     "The framework denies that eukaryotic lineages differ from one another",
     "Compartmentalization is found in every form of life"], ans=0,
   why="EK 2.9.A.1 confirms that eukaryotic cells compartmentalize metabolic processes, so the premise stands; the conclusion is what fails. EK 7.7.A.1 treats the same feature as evidence of common ancestry precisely because a single inheritance accounts for its presence throughout the group."),

 dict(q="Taken together, what do membrane-bound organelles, linear chromosomes, and genes containing introns provide?",
   choices=[
     "Three independent lines of structural and functional evidence pointing to one shared eukaryotic ancestor",
     "A single line of evidence stated three ways",
     "Evidence that eukaryotes and prokaryotes are unrelated in every respect",
     "A method for dating when eukaryotes first appeared",
     "A list of the features every living cell possesses"], ans=0,
   why="EK 7.7.A.1 lists three separate features under one claim of common ancestry of all eukaryotes. They are separate observations about different components of the cell, and the statement makes no claim about dates or about all living cells."),
]
