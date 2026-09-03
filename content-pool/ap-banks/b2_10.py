# AP BIOLOGY 2.10 Origins of Cell Compartmentalization
# CED effective Fall 2025, Unit 2 Cells. Big Idea 1 Evolution.
# Learning objective 2.10.A, describe similarities and/or differences in
# compartmentalization between prokaryotic and eukaryotic cells.
# Suggested skill 6.B, support a claim with evidence from biological
# principles, concepts, processes, and data.
#
# Essential knowledge, in the framework's own terms:
#   2.10.A.1  Membrane-bound organelles such as mitochondria and chloroplasts
#             evolved from once free-living prokaryotic cells via endosymbiosis.
#   2.10.A.2  Prokaryotes typically lack internal membrane-bound organelles but
#             have internal regions with specialized structures and functions.
#   2.10.A.3  Eukaryotic cells maintain internal membranes that partition the
#             cell into specialized regions.
#
# Supporting statements cited where used, from elsewhere in the same CED:
#   2.1.A.1   ribosomes are non-membrane subcellular structures found in cells
#             in all forms of life and reflect the common ancestry of all
#             known life
#   2.1.A.5   mitochondria have a double membrane
#   2.1.A.8   chloroplasts contain a double membrane
#   6.1.A.1.i prokaryotic organisms typically have circular chromosomes
#   3.4.A.1.ii-iv  photosynthesis first evolved in prokaryotic organisms, and
#             prokaryotic photosynthetic pathways were the foundation of
#             eukaryotic photosynthesis
#
# WHAT THIS MODULE DELIBERATELY DOES NOT ASSERT. The framework states the
# endosymbiotic origin as a conclusion and does not print the evidence for it.
# Items that ask about evidence are therefore written CONDITIONALLY -- "an
# investigator reports X; which claim does that support" -- so the key is a
# piece of reasoning traceable to 2.10.A.1 and the cited supporting statement,
# not an unsourced factual assertion.
#
# Topic 2.9 covers what compartments DO inside a eukaryotic cell; this module
# stays on origin and on the prokaryote-eukaryote comparison, and every use of
# 2.10.A.3 is in that comparative frame.
#
# FIVE choices (A-E). Plain prose, no LaTeX.
TOPIC = ("2.10", "Origins of Cell Compartmentalization", 2)

_T_CELLS = dict(
    headers=["Cell (hypothetical)",
             "Types of membrane-bound organelle observed",
             "Total internal membrane area (square micrometers)",
             "Ribosomes counted (thousands)"],
    rows=[["Cell 1", "0", "0", "15"],
          ["Cell 2", "6", "3,200", "210"],
          ["Cell 3", "8", "4,800", "260"]])

_T_STRUCT = dict(
    headers=["Structure (hypothetical measurements)",
             "Membranes surrounding the structure",
             "Diameter (micrometers)",
             "DNA present within the structure (kilobases)"],
    rows=[["Mitochondrion", "2", "1.0", "16"],
          ["Chloroplast", "2", "5.0", "150"],
          ["Lysosome", "1", "0.5", "0"],
          ["Transport vesicle", "1", "0.1", "0"]])

_T_SURVEY = dict(
    headers=["Group surveyed (hypothetical)",
             "Species examined",
             "Species with membrane-bound organelles",
             "Species with internal regions of specialized function"],
    rows=[["Prokaryotes", "120", "0", "120"],
          ["Eukaryotes", "80", "80", "80"]])

QUESTIONS = [
 dict(q="According to the framework, mitochondria and chloroplasts arose by which evolutionary route?",
   choices=[
     "They descend from prokaryotic cells that once lived independently and came to reside inside another cell",
     "They formed when the plasma membrane of an ancestral eukaryote folded inward and pinched off",
     "They were assembled from proteins encoded entirely by the nuclear genome of the first eukaryote",
     "They arose independently in every eukaryotic lineage after those lineages had already diverged",
     "They developed from viruses that infected an early eukaryotic cell and were never released"],
   ans=0,
   why="EK 2.10.A.1 states that membrane-bound organelles such as mitochondria and chloroplasts evolved from once free-living prokaryotic cells via endosymbiosis. The other routes are not the account the framework gives."),

 dict(q="Which pair of organelles does the framework name as having an endosymbiotic origin?",
   choices=[
     "Mitochondria and chloroplasts",
     "Lysosomes and peroxisomes",
     "The Golgi complex and the endoplasmic reticulum",
     "The nucleus and the nuclear envelope",
     "Transport vesicles and vacuoles"],
   ans=0,
   why="EK 2.10.A.1 names mitochondria and chloroplasts specifically as the membrane-bound organelles that evolved from once free-living prokaryotic cells. The framework does not extend the claim to the other structures listed."),

 dict(q="A microbiologist examines a cell and finds no membrane-bound organelles, yet finds a region where the chromosome is concentrated and other regions where particular reactions occur. How should this cell be classified and why?",
   choices=[
     "Prokaryotic, because prokaryotes typically lack membrane-bound organelles while still having internal regions of specialized function",
     "Prokaryotic, because prokaryotic cells have no internal organization of any kind",
     "Eukaryotic, because any region of specialized function must be an organelle",
     "Eukaryotic, because only eukaryotes concentrate their chromosome in one region",
     "Neither, because a cell with regions of specialized function but no organelles cannot exist"],
   ans=0,
   why="EK 2.10.A.2 states that prokaryotes typically lack internal membrane-bound organelles but have internal regions with specialized structures and functions. Both halves of the observation match that statement."),

 dict(q="Which statement best captures a similarity between prokaryotic and eukaryotic cells with respect to internal organization?",
   choices=[
     "Both have internal regions in which particular structures and functions are concentrated",
     "Both partition their interiors using membrane-bound organelles",
     "Both keep every enzyme uniformly distributed through the cytosol",
     "Both use a nuclear envelope to separate the chromosome from the cytosol",
     "Both arose when a free-living cell was taken up by a larger cell"],
   ans=0,
   why="EK 2.10.A.2 credits prokaryotes with internal regions of specialized structure and function, and EK 2.10.A.3 credits eukaryotes with internal membranes that partition the cell into specialized regions. Regional specialization is the shared feature; membrane-bound organelles are not."),

 dict(q="Which statement best captures a difference between prokaryotic and eukaryotic cells with respect to internal organization?",
   choices=[
     "Eukaryotic cells maintain internal membranes that partition the cell, and prokaryotes typically do not",
     "Prokaryotic cells contain more kinds of membrane-bound organelle than eukaryotic cells",
     "Only prokaryotic cells concentrate particular functions in particular regions",
     "Only eukaryotic cells contain ribosomes",
     "Only prokaryotic cells are surrounded by a plasma membrane"],
   ans=0,
   why="EK 2.10.A.3 gives eukaryotes internal membranes that partition the cell into specialized regions, and EK 2.10.A.2 says prokaryotes typically lack internal membrane-bound organelles. EK 2.1.A.1 places ribosomes in all forms of life, which is why the ribosome option fails."),

 dict(q="Ribosomes are found in cells of every known form of life. What does the framework take that distribution to indicate?",
   choices=[
     "It reflects the common ancestry of all known life",
     "It shows that ribosomes evolved separately in each lineage",
     "It shows that ribosomes are membrane-bound organelles",
     "It shows that every cell type carries out photosynthesis",
     "It shows that ribosomes arose by endosymbiosis in the same way mitochondria did"],
   ans=0,
   why="EK 2.1.A.1 states that ribosomes are non-membrane subcellular structures found in cells in all forms of life and reflect the common ancestry in all known life. Universality is read as inheritance from a shared ancestor, not as repeated invention."),

 dict(q="An investigator reports that a mitochondrion contains its own circular molecule of DNA. Which claim does that observation most directly support, and on what reasoning?",
   choices=[
     "That the organelle descends from a prokaryotic cell, because prokaryotic organisms typically have circular chromosomes",
     "That the organelle synthesizes the entire proteome of the cell, because DNA encodes protein",
     "That the organelle is a recent invention of eukaryotes, because eukaryotic chromosomes are linear",
     "That the organelle can leave the cell and resume independent life at any time",
     "That the organelle is not surrounded by a membrane, because DNA cannot cross a membrane"],
   ans=0,
   why="EK 6.1.A.1.i states that prokaryotic organisms typically have circular chromosomes while eukaryotic organisms typically have multiple linear chromosomes. A circular chromosome inside the organelle therefore points to the prokaryotic ancestry asserted in EK 2.10.A.1."),

 dict(q="Both the mitochondrion and the chloroplast are bounded by two membranes rather than one. Why is that feature often cited in support of an endosymbiotic origin?",
   choices=[
     "An extra outer boundary is what would be expected if one cell had been taken inside another",
     "Two membranes prove that the organelle cannot exchange material with the cytosol",
     "Two membranes are found around every organelle in a eukaryotic cell",
     "Two membranes are needed for any organelle that contains enzymes",
     "Two membranes show that the organelle formed after the nucleus did"],
   ans=0,
   why="EK 2.1.A.5 and EK 2.1.A.8 record the double membrane of mitochondria and chloroplasts, and EK 2.10.A.1 gives their origin as a once free-living cell taken up by another. An engulfed cell would bring its own boundary and acquire a second one from its host."),

 dict(q="The framework states that photosynthesis first evolved in prokaryotic organisms and that prokaryotic photosynthetic pathways were the foundation of eukaryotic photosynthesis. How does that fit the origin of the chloroplast?",
   choices=[
     "It is consistent with a photosynthetic prokaryote becoming an organelle inside a eukaryotic cell",
     "It shows that eukaryotes invented photosynthesis and later passed it to prokaryotes",
     "It shows that chloroplasts and mitochondria have unrelated origins from one another",
     "It shows that the chloroplast arose by infolding of the eukaryotic plasma membrane",
     "It shows that photosynthesis requires a nucleus in order to occur"],
   ans=0,
   why="EK 3.4.A.1.ii and EK 3.4.A.1.iv put photosynthesis first in prokaryotes and make prokaryotic pathways the foundation of the eukaryotic version, which is exactly what EK 2.10.A.1's endosymbiotic origin of the chloroplast would produce."),

 dict(q="Three cells were examined with the results shown. Which cell is prokaryotic, and what in the data identifies it?",
   table=_T_CELLS,
   choices=[
     "The cell with no membrane-bound organelle types and no internal membrane area",
     "The cell with the largest internal membrane area, because organelles crowd out the cytosol",
     "The cell with the most ribosomes, because ribosomes replace organelles in prokaryotes",
     "The cell with the most types of membrane-bound organelle",
     "None of them, because every cell in the table contains ribosomes"],
   ans=0,
   why="EK 2.10.A.2 says prokaryotes typically lack internal membrane-bound organelles, so the identifying column is the organelle count and not the ribosome count. EK 2.1.A.1 puts ribosomes in all forms of life, which is why their presence identifies nothing."),

 dict(q="Structures from a eukaryotic cell were measured with the results shown. Which pattern in these data is most consistent with an endosymbiotic origin for some of them?",
   table=_T_STRUCT,
   choices=[
     "The structures bounded by two membranes are also the ones that contain DNA",
     "The structures bounded by one membrane are also the ones that contain DNA",
     "The largest structure in the table contains the least DNA",
     "Every structure listed is bounded by the same number of membranes",
     "The amount of DNA present is proportional to the number of membranes for all four structures"],
   ans=0,
   why="EK 2.10.A.1 traces mitochondria and chloroplasts to once free-living prokaryotic cells. A former cell would be expected to retain both its own boundary and its own genetic material, and in the table those two features occur in the same two structures and in no others."),

 dict(q="A survey of two groups of organisms produced the results shown. Which conclusion do these data support?",
   table=_T_SURVEY,
   choices=[
     "Every species surveyed has internal regions of specialized function, but only the eukaryotes have membrane-bound organelles",
     "Every species surveyed has membrane-bound organelles, but only the eukaryotes have specialized regions",
     "Neither group shows any internal specialization of function",
     "More prokaryotic than eukaryotic species were found to have membrane-bound organelles",
     "The two groups are indistinguishable on both measures reported"],
   ans=0,
   why="EK 2.10.A.2 and EK 2.10.A.3 predict precisely this split: specialized internal regions in both groups, membrane-bound organelles in the eukaryotes only. The numbers in the table show that split exactly."),

 dict(q="The framework says prokaryotes TYPICALLY lack internal membrane-bound organelles. What does the qualifier allow for?",
   choices=[
     "That the generalization holds broadly while particular prokaryotes may depart from it",
     "That no prokaryote has ever been examined closely enough to say",
     "That every prokaryote possesses at least one membrane-bound organelle",
     "That the statement applies only to prokaryotes living inside other cells",
     "That prokaryotes lose their organelles when they are cultured in a laboratory"],
   ans=0,
   why="EK 2.10.A.2 is written as a generalization with a qualifier, in the same way EK 6.1.A.1.i says prokaryotes typically have circular chromosomes. A qualified generalization asserts the pattern and leaves room for exceptions, which is why an absolute reading of it is wrong."),

 dict(q="A student claims that because a mitochondrion descends from a free-living cell, a mitochondrion removed from a cell should be able to grow and reproduce on its own in culture. What is the best response?",
   choices=[
     "The ancestor was free-living, but the framework describes the descendant as an organelle of the host cell",
     "The claim is correct, because endosymbiosis leaves the engulfed cell entirely unchanged",
     "The claim is correct, because organelles with two membranes are self-sufficient",
     "The claim fails because mitochondria were never derived from cells at all",
     "The claim fails because a mitochondrion contains no proteins of its own"],
   ans=0,
   why="EK 2.10.A.1 says the organelles evolved FROM once free-living prokaryotic cells; the phrase locates independent life in the ancestor. The present-day structure is described throughout the framework as a membrane-bound organelle of a eukaryotic cell."),

 dict(q="Which observation, if made, would most weaken the claim that a particular organelle arose by endosymbiosis?",
   choices=[
     "The organelle is bounded by a single membrane continuous with the endoplasmic reticulum and contains no genetic material",
     "The organelle is bounded by two membranes",
     "The organelle contains ribosomes",
     "The organelle carries out reactions that release energy",
     "The organelle is found in every eukaryotic cell examined"],
   ans=0,
   why="The endosymbiotic account in EK 2.10.A.1 predicts a structure descended from a cell, which would carry both its own boundary and its own genetic material. Continuity with the endomembrane system and the absence of genetic material fit an origin by membrane budding instead."),

 dict(q="How does the internal organization of a eukaryotic cell differ in kind, not merely in degree, from that of a prokaryotic cell?",
   choices=[
     "The eukaryotic regions are bounded by their own membranes, so their contents are physically enclosed",
     "The eukaryotic regions are larger but are bounded in exactly the same way",
     "The prokaryotic regions are bounded by membranes and the eukaryotic ones are not",
     "The eukaryotic cell has fewer regions of specialized function",
     "Only the prokaryotic cell keeps its genetic material in a defined region"],
   ans=0,
   why="EK 2.10.A.3 makes internal MEMBRANES the partition in eukaryotes, while EK 2.10.A.2 gives prokaryotes regions without membrane-bound organelles. Enclosure by a membrane is the qualitative difference between the two arrangements."),

 dict(q="An investigator wants to test whether a newly discovered organelle descends from a free-living cell. Which line of evidence would be most informative?",
   choices=[
     "Comparing genetic material found inside the organelle with the genomes of living prokaryotes",
     "Measuring the total volume the organelle occupies within the cell",
     "Counting how many copies of the organelle a typical cell contains",
     "Determining the pH of the cytosol surrounding the organelle",
     "Measuring how quickly the organelle moves through the cytoplasm"],
   ans=0,
   why="Descent is an evolutionary claim, so the informative comparison is with candidate relatives. EK 2.10.A.1 asserts descent from once free-living prokaryotic cells, and sequence comparison is what could place the organelle among them; volume and speed bear on neither."),

 dict(q="Which of these best explains why the endosymbiotic origin of organelles is placed under the framework's evolution theme rather than its energetics theme?",
   choices=[
     "It is an account of how a structure came to exist through descent, not of how the structure works",
     "It concerns only organisms that no longer exist",
     "It describes a chemical reaction rather than a cell structure",
     "It applies to prokaryotes but not to eukaryotes",
     "It is a claim about energy transfer between two cells"],
   ans=0,
   why="EK 2.10.A.1 sits under Big Idea 1, Evolution, and asserts a lineage: organelles evolved from once free-living prokaryotic cells. What the mitochondrion does with energy is a separate matter treated under Big Idea 2."),

 dict(q="Two eukaryotic cells of equal volume are compared. Cell X has extensive internal membranes; cell Y has almost none. On the framework's account, what has cell X gained relative to cell Y?",
   choices=[
     "A cell interior partitioned into more specialized regions",
     "A prokaryotic ancestry that cell Y lacks",
     "The ability to survive without a plasma membrane",
     "Freedom from the need for enzymes in its reactions",
     "A larger genome than cell Y"],
   ans=0,
   why="EK 2.10.A.3 states that eukaryotic cells maintain internal membranes that partition the cell into specialized regions. More internal membrane means more partitioning; ancestry and genome size are unrelated to how much membrane a cell has built."),

 dict(q="Which of these describes an internal region of a prokaryotic cell in terms the framework supports?",
   choices=[
     "A region where a particular structure is located and a particular function is carried out, without a surrounding organelle membrane",
     "A region enclosed by its own membrane and separated from the cytosol",
     "A region occupied by a nucleus containing linear chromosomes",
     "A region formed by the engulfment of another prokaryotic cell",
     "A region in which no reactions of any kind take place"],
   ans=0,
   why="EK 2.10.A.2 gives prokaryotes internal regions with specialized structures and functions while denying them internal membrane-bound organelles. The keyed description states both halves of that sentence and no more."),

 dict(q="An argument holds that compartmentalization is not unique to eukaryotes. Which piece of evidence best supports that argument?",
   choices=[
     "Prokaryotic cells confine particular structures and functions to particular internal regions",
     "Prokaryotic cells are on average smaller than eukaryotic cells",
     "Prokaryotic cells have circular chromosomes",
     "Eukaryotic cells contain mitochondria",
     "Both cell types are enclosed by a plasma membrane"],
   ans=0,
   why="Skill 6.B asks for evidence that supports the stated claim. The claim is about internal specialization, and EK 2.10.A.2 supplies exactly that for prokaryotes; cell size, chromosome shape and the outer boundary are about other properties."),

 dict(q="Suppose a large prokaryotic cell took up a smaller photosynthetic prokaryote that continued to carry out photosynthesis inside it. On the framework's account, what would this arrangement represent?",
   choices=[
     "The kind of event by which the chloroplast is said to have arisen",
     "The formation of a new endomembrane system by inward folding",
     "The conversion of a prokaryote into a virus",
     "The loss of photosynthesis from both cells involved",
     "The origin of the ribosome as a subcellular structure"],
   ans=0,
   why="EK 2.10.A.1 gives endosymbiosis as the route by which chloroplasts evolved from once free-living prokaryotic cells, and EK 3.4.A.1.ii places the origin of photosynthesis in prokaryotes. The scenario is that route stated as an event."),

 dict(q="Why does the framework describe the ancestors of mitochondria and chloroplasts as once free-living rather than as always organelles?",
   choices=[
     "Because the claim is that independently living cells became organelles, which requires them to have lived independently first",
     "Because organelles are defined as structures that have never been alive",
     "Because free-living cells cannot contain DNA",
     "Because a cell must lose its membrane before it can become an organelle",
     "Because only eukaryotic cells have ever lived independently"],
   ans=0,
   why="EK 2.10.A.1's wording is the content of the claim: organelles evolved from once free-living prokaryotic cells via endosymbiosis. Independent life before uptake is what distinguishes this account from an origin by membrane folding."),

 dict(q="A eukaryotic cell loses the internal membranes that separate its specialized regions but keeps its plasma membrane. Which change is the most reasonable prediction?",
   choices=[
     "The cell can no longer maintain distinct regions with distinct functions",
     "The cell becomes prokaryotic and acquires a circular chromosome",
     "The cell gains additional membrane-bound organelles to compensate",
     "The cell's exchange with its surroundings stops entirely",
     "The cell's ribosomes disappear because they need internal membranes"],
   ans=0,
   why="EK 2.10.A.3 makes internal membranes the thing that partitions the eukaryotic cell into specialized regions, so removing them removes the partitioning. Chromosome shape and ribosome presence are governed by other statements and would not follow."),

 dict(q="Which comparison between a prokaryotic cell and a mitochondrion is consistent with the framework's account of the organelle's origin?",
   choices=[
     "The mitochondrion resembles a prokaryotic cell because it descends from one",
     "The mitochondrion resembles a prokaryotic cell because prokaryotes descend from mitochondria",
     "The mitochondrion resembles a prokaryotic cell only by coincidence, since the two are unrelated",
     "The mitochondrion cannot resemble a prokaryotic cell because it lies inside a eukaryote",
     "The mitochondrion resembles a prokaryotic cell because both were made by a virus"],
   ans=0,
   why="EK 2.10.A.1 sets the direction of descent: the organelle evolved from a once free-living prokaryotic cell. Resemblance is then inheritance, and reversing the direction contradicts the statement."),

 dict(q="What role does the framework's evolution theme give to endosymbiosis in explaining eukaryotic complexity?",
   choices=[
     "It accounts for how a eukaryotic cell acquired certain organelles from another lineage of cells",
     "It accounts for how every organelle in the cell was assembled from nuclear gene products",
     "It accounts for how prokaryotes came to lack internal membranes",
     "It accounts for how enzymes lower the activation energy of reactions",
     "It accounts for how a cell divides its cytoplasm during cytokinesis"],
   ans=0,
   why="EK 2.10.A.1 attributes specific organelles, mitochondria and chloroplasts, to descent from a separate lineage of once free-living prokaryotic cells. That is an acquisition across lineages rather than a construction from within one."),

 dict(q="Which statement about compartmentalization is supported by the framework for BOTH prokaryotic and eukaryotic cells?",
   choices=[
     "Particular functions are associated with particular locations inside the cell",
     "Every specialized function is enclosed by its own membrane",
     "The chromosome is enclosed within a nuclear envelope",
     "The cell contains organelles derived from engulfed cells",
     "Internal membranes fold to increase surface area for reactions"],
   ans=0,
   why="EK 2.10.A.2 gives prokaryotes internal regions with specialized structures and functions and EK 2.10.A.3 gives eukaryotes membrane-partitioned specialized regions. Localization of function is common to both; the membrane, the envelope and the engulfed ancestor belong to the eukaryotic case only."),

 dict(q="A textbook figure labels the boundary of a mitochondrion with two arrows and the boundary of a lysosome with one. Which inference about origins is best supported?",
   choices=[
     "The mitochondrion's second boundary fits an origin by uptake into another cell, which the lysosome's boundary does not require",
     "The lysosome must also have arisen by endosymbiosis but has lost one of its membranes",
     "The number of boundaries shows which organelle is older",
     "Both organelles must have arisen by inward folding of the plasma membrane",
     "The mitochondrion must have arisen by the fusion of two lysosomes"],
   ans=0,
   why="EK 2.1.A.5 records the mitochondrion's double membrane and EK 2.10.A.1 gives its endosymbiotic origin; an engulfed cell would supply one boundary and the host the other. A single-membrane organelle needs no such account."),

 dict(q="Which question about a newly described organelle is testable in the way the framework's origin claim was made testable?",
   choices=[
     "Does the genetic material inside the organelle group with any lineage of living prokaryotes?",
     "Should the organelle be regarded as the most important structure in the cell?",
     "Is the organelle beautiful when viewed under an electron microscope?",
     "Would the cell be better off without the organelle?",
     "Does the organelle deserve to be given a new name?"],
   ans=0,
   why="Skill 3.A asks for a testable question. Only the keyed question can be settled by evidence, and it addresses the relationship EK 2.10.A.1 asserts between organelles and once free-living prokaryotic cells; the rest ask for judgements no observation settles."),

 dict(q="Summarizing the topic, which pair of statements is the framework's account of where a eukaryotic cell's compartments came from?",
   choices=[
     "Some organelles descend from engulfed free-living prokaryotes, and internal membranes partition the rest of the cell into specialized regions",
     "All organelles descend from engulfed free-living prokaryotes, and prokaryotes have no internal organization",
     "No organelle descends from a free-living cell, and internal membranes are absent from eukaryotes",
     "All compartments arose after the first eukaryotes had evolved multicellularity",
     "Compartments are found only in cells that carry out photosynthesis"],
   ans=0,
   why="EK 2.10.A.1 covers the endosymbiotic organelles and EK 2.10.A.3 covers the partitioning by internal membranes, while EK 2.10.A.2 denies that prokaryotes are unorganized. Only the keyed pair states all three correctly."),
]
