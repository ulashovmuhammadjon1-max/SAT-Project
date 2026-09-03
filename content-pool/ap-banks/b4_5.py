# AP BIOLOGY 4.5 Cell Cycle
# CED effective Fall 2025, Unit 4 Cell Communication and Cell Cycle.
# Big Idea 3 Information Storage and Transmission.
# Learning objectives 4.5.A (describe the events that occur in the cell cycle)
# and 4.5.B (explain how mitosis results in the transmission of chromosomes
# from one generation of cells to the next).
# Suggested skills 4.B (describe data from a table, including identifying
# specific data points, trends and relationships) and 5.A (perform mathematical
# calculations, including means, rates, ratios, percentages and percent
# changes). Both are data skills, which is why a fifth of this module is
# tables with arithmetic in them.
#
# Essential knowledge, in the framework's own terms:
#   4.5.A.1     the cell cycle is a HIGHLY REGULATED series of events that
#               controls the GROWTH AND REPRODUCTION of eukaryotic cells
#     i.        sequential stages of INTERPHASE (G1, S, G2), MITOSIS and
#               CYTOKINESIS
#     ii.       G1: metabolically active, DUPLICATING ORGANELLES and cytosolic
#               components
#     iii.      S: DNA is in the form of CHROMATIN and REPLICATES to form TWO
#               SISTER CHROMATIDS connected at a CENTROMERE
#     iv.       G2: PROTEIN SYNTHESIS occurs, ATP is produced in large
#               quantities, and CENTROSOMES REPLICATE
#     v.        a cell can enter G0, in which it NO LONGER DIVIDES but CAN
#               REENTER the cell cycle in response to appropriate cues
#     vi.       nondividing cells may EXIT the cell cycle or be HELD at a
#               particular stage
#   4.5.B.1     mitosis ensures the transfer of a COMPLETE GENOME from a parent
#               cell to TWO GENETICALLY IDENTICAL daughter cells in eukaryotes
#     i.        mitosis plays a role in GROWTH, TISSUE REPAIR and ASEXUAL
#               REPRODUCTION
#     ii.       sequential steps PROPHASE, METAPHASE, ANAPHASE, TELOPHASE,
#               alternating with interphase
#     iii.      prophase: sister chromatids CONDENSE, mitotic spindle BEGINS TO
#               FORM, centrosomes MOVE TO OPPOSITE POLES
#     iv.       metaphase: spindle fibers ALIGN CHROMOSOMES ALONG THE EQUATOR
#     v.        anaphase: paired sister chromatids SEPARATE as spindle fibers
#               pull chromatids toward poles
#     vi.       telophase: mitotic spindle BREAKS DOWN, a NEW NUCLEAR ENVELOPE
#               develops, and then the cytoplasm divides
#     vii.      cytokinesis: a CLEAVAGE FURROW forms in ANIMAL cells or a CELL
#               PLATE forms in PLANT cells, giving two new daughter cells
#
# BOUNDARY WITH 4.6 AND 5.1, HELD DELIBERATELY. Checkpoints, cyclins,
# cyclin-dependent kinases and the consequences of disruption (cancer,
# apoptosis) are essential knowledge of topic 4.6 and carry no key here.
# Meiosis, homologous pairs, crossing over and haploid gametes are topics 5.1
# and 5.2. This module is the ordinary cycle and ordinary mitosis, described
# and counted.
#
# NO FIGURES ANYWHERE. The cell cycle tempts a diagram badly and the bank
# cannot carry one, so every data item is a table of counts and the arithmetic
# is done on the table.
#
# FIVE choices (A-E). Plain prose, no LaTeX.
TOPIC = ("4.5", "Cell Cycle", 4)

_T_PHASES = dict(
    headers=["Stage observed", "Cells counted in a sample of 400 (hypothetical)"],
    rows=[["Interphase", "300"],
          ["Prophase", "48"],
          ["Metaphase", "20"],
          ["Anaphase", "12"],
          ["Telophase", "20"]])

_T_DNA = dict(
    headers=["Point in the cell cycle",
             "DNA per cell relative to a cell in G1 (hypothetical)"],
    rows=[["Early G1", "1.0"],
          ["End of S", "2.0"],
          ["G2", "2.0"],
          ["Each daughter cell after cytokinesis", "1.0"]])

_T_TISSUE = dict(
    headers=["Tissue sample (hypothetical)",
             "Cells dividing, out of 500 counted",
             "Cells in G0, out of 500 counted"],
    rows=[["Tissue A", "150", "20"],
          ["Tissue B", "10", "430"],
          ["Tissue C", "60", "300"]])

_T_GROWTH = dict(
    headers=["Culture (hypothetical)", "Cells present at the start",
             "Cells present after twenty-four hours"],
    rows=[["Culture 1", "2,000", "8,000"],
          ["Culture 2", "2,000", "2,200"],
          ["Culture 3", "2,000", "2,000"]])

QUESTIONS = [
 dict(q="How does the framework describe the cell cycle?",
   choices=[
     "A highly regulated series of events that controls the growth and reproduction of eukaryotic cells",
     "An unregulated sequence that proceeds at the same rate in every cell",
     "A single event in which a cell splits without any preparation",
     "A process confined to prokaryotic cells",
     "A process that occurs only in cells that have stopped growing"],
   ans=0,
   why="EK 4.5.A.1 states that the cell cycle is a highly regulated series of events that controls the growth and reproduction of eukaryotic cells."),

 dict(q="Which sequence of stages does the framework give for the cell cycle?",
   choices=[
     "Interphase, made up of G1, S and G2, then mitosis, then cytokinesis",
     "Mitosis, then cytokinesis, then interphase made up of G1, S and G2",
     "G1, then mitosis, then S, then cytokinesis, then G2",
     "Cytokinesis, then S, then mitosis, then G1 and G2",
     "S alone, since the other stages are optional"],
   ans=0,
   why="EK 4.5.A.1.i states that the cell cycle consists of sequential stages of interphase (G1, S, G2), mitosis, and cytokinesis, in that order."),

 dict(q="What does the framework say a cell is doing during G1?",
   choices=[
     "It is metabolically active and duplicating organelles and cytosolic components",
     "It is replicating its DNA to form sister chromatids",
     "It is replicating its centrosomes in preparation for the spindle",
     "It is dividing its cytoplasm into two daughter cells",
     "It has permanently stopped all metabolic activity"],
   ans=0,
   why="EK 4.5.A.1.ii states that in G1 phase the cell is metabolically active, duplicating organelles and cytosolic components. DNA replication belongs to S and centrosome replication to G2."),

 dict(q="What does the framework say happens during S phase?",
   choices=[
     "DNA in the form of chromatin replicates to form two sister chromatids joined at a centromere",
     "Sister chromatids separate and are pulled toward opposite poles",
     "Organelles and cytosolic components are duplicated but DNA is not",
     "The nuclear envelope re-forms around two sets of chromosomes",
     "The cytoplasm divides to give two daughter cells"],
   ans=0,
   why="EK 4.5.A.1.iii states that in S phase DNA is in the form of chromatin and replicates to form two sister chromatids connected at a centromere."),

 dict(q="What does the framework say happens during G2?",
   choices=[
     "Protein synthesis occurs, large quantities of ATP are produced, and centrosomes replicate",
     "DNA replicates to form sister chromatids",
     "Chromosomes align along the equator of the cell",
     "The cleavage furrow or cell plate forms",
     "The cell permanently withdraws from the cell cycle"],
   ans=0,
   why="EK 4.5.A.1.iv states that in G2 phase protein synthesis occurs, ATP is produced in large quantities, and centrosomes replicate."),

 dict(q="What does the framework say about a cell that has entered G0?",
   choices=[
     "It no longer divides, but it can reenter the cell cycle in response to appropriate cues",
     "It no longer divides and can never reenter the cell cycle",
     "It divides more rapidly than a cell in G1",
     "It has completed mitosis but not cytokinesis",
     "It is in the middle of replicating its DNA"],
   ans=0,
   why="EK 4.5.A.1.v states that a cell can enter a stage, G0, in which it no longer divides, but it can reenter the cell cycle in response to appropriate cues. Both halves are part of the statement."),

 dict(q="What two possibilities does the framework name for nondividing cells?",
   choices=[
     "They may exit the cell cycle or be held at a particular stage in it",
     "They may only exit the cell cycle, never being held within it",
     "They may only be held within the cell cycle, never exiting it",
     "They must complete mitosis before they can stop dividing",
     "They must first replicate their DNA a second time"],
   ans=0,
   why="EK 4.5.A.1.vi states that nondividing cells may exit the cell cycle or be held at a particular stage in the cell cycle, naming both possibilities."),

 dict(q="What does the framework say mitosis ensures?",
   choices=[
     "The transfer of a complete genome from a parent cell to two genetically identical daughter cells",
     "The transfer of half a genome to each of four daughter cells",
     "The transfer of a complete genome to a single daughter cell",
     "The exchange of genetic material between two parent cells",
     "The removal of damaged chromosomes from the parent cell"],
   ans=0,
   why="EK 4.5.B.1 states that mitosis is a process that ensures the transfer of a complete genome from a parent cell to two genetically identical daughter cells in eukaryotes."),

 dict(q="Which roles does the framework assign to mitosis?",
   choices=[
     "Growth, tissue repair, and asexual reproduction",
     "Growth only",
     "Tissue repair only",
     "The formation of gametes for sexual reproduction",
     "The exchange of genetic material between homologous chromosomes"],
   ans=0,
   why="EK 4.5.B.1.i states that mitosis plays a role in growth, tissue repair, and asexual reproduction, naming all three."),

 dict(q="In what order does the framework list the steps of mitosis, and what do they alternate with?",
   choices=[
     "Prophase, metaphase, anaphase, telophase, alternating with interphase",
     "Metaphase, prophase, telophase, anaphase, alternating with interphase",
     "Prophase, anaphase, metaphase, telophase, alternating with cytokinesis",
     "Telophase, anaphase, metaphase, prophase, alternating with G0",
     "Prophase and telophase only, with no other steps"],
   ans=0,
   why="EK 4.5.B.1.ii states that mitosis occurs in sequential steps, prophase, metaphase, anaphase, telophase, and alternates with interphase in the cell cycle."),

 dict(q="What three events does the framework place in prophase?",
   choices=[
     "Sister chromatids condense, the mitotic spindle begins to form, and centrosomes move to opposite poles",
     "Chromosomes align along the equator and spindle fibers attach to them",
     "Sister chromatids separate and are pulled toward the poles",
     "The mitotic spindle breaks down and a new nuclear envelope develops",
     "A cleavage furrow forms in an animal cell or a cell plate in a plant cell"],
   ans=0,
   why="EK 4.5.B.1.iii states that in prophase sister chromatids condense, the mitotic spindle begins to form, and centrosomes move to opposite poles of the cell."),

 dict(q="What does the framework say occurs in metaphase?",
   choices=[
     "Spindle fibers align the chromosomes along the equator of the cell",
     "Spindle fibers pull separated chromatids toward the poles",
     "The centrosomes replicate in preparation for the spindle",
     "The nuclear envelope re-forms around each set of chromosomes",
     "The cytoplasm divides into two daughter cells"],
   ans=0,
   why="EK 4.5.B.1.iv states that in metaphase spindle fibers align chromosomes along the equator of the cell."),

 dict(q="What does the framework say occurs in anaphase?",
   choices=[
     "Paired sister chromatids separate as spindle fibers pull chromatids toward the poles",
     "Paired sister chromatids condense as the spindle begins to form",
     "Chromosomes are aligned along the equator by spindle fibers",
     "A new nuclear envelope develops around each set of chromosomes",
     "DNA replicates to produce sister chromatids"],
   ans=0,
   why="EK 4.5.B.1.v states that in anaphase paired sister chromatids separate as spindle fibers pull chromatids toward poles."),

 dict(q="What does the framework say occurs in telophase?",
   choices=[
     "The mitotic spindle breaks down, a new nuclear envelope develops, and then the cytoplasm divides",
     "The mitotic spindle forms and chromatids begin to condense",
     "Chromosomes are aligned along the equator of the cell",
     "Sister chromatids are pulled apart toward opposite poles",
     "Centrosomes replicate and protein synthesis increases"],
   ans=0,
   why="EK 4.5.B.1.vi states that in telophase the mitotic spindle breaks down, a new nuclear envelope develops, and then the cytoplasm divides."),

 dict(q="How does the framework describe cytokinesis in animal cells compared with plant cells?",
   choices=[
     "A cleavage furrow forms in animal cells and a cell plate forms in plant cells",
     "A cell plate forms in animal cells and a cleavage furrow forms in plant cells",
     "A cleavage furrow forms in both kinds of cell",
     "A cell plate forms in both kinds of cell",
     "Neither kind of cell divides its cytoplasm after mitosis"],
   ans=0,
   why="EK 4.5.B.1.vii states that in cytokinesis a cleavage furrow forms in animal cells or a cell plate forms in plant cells, resulting in two new daughter cells."),

 dict(q="Cells in a tissue sample were classified by stage, with the results shown. What percentage of the counted cells were in interphase?",
   table=_T_PHASES,
   choices=[
     "Seventy-five percent",
     "Fifty percent",
     "Twenty-five percent",
     "Twelve percent",
     "One hundred percent"],
   ans=0,
   why="Skill 5.A asks students to calculate percentages from a table. The interphase count divided by the total of all counts, expressed as a percentage, gives the keyed value and no other option."),

 dict(q="Using the same classified sample, and assuming the whole cell cycle takes twenty hours, about how long does the sample suggest a cell spends in interphase?",
   table=_T_PHASES,
   choices=[
     "About fifteen hours",
     "About ten hours",
     "About five hours",
     "About two hours",
     "About twenty hours"],
   ans=0,
   why="Skill 5.A asks for calculations of ratios and rates. The fraction of cells caught in a stage estimates the fraction of the cycle spent in it, so that fraction of twenty hours gives the keyed value."),

 dict(q="The amount of DNA per cell was measured at four points in the cell cycle, with the results shown. Which interpretation is best supported?",
   table=_T_DNA,
   choices=[
     "The DNA content doubles before division and each daughter cell receives the original amount",
     "The DNA content halves before division and each daughter cell receives twice the original amount",
     "The DNA content is unchanged throughout the whole cell cycle",
     "The DNA content doubles again in each daughter cell immediately after division",
     "The DNA content of a daughter cell is twice that of the parent cell in G1"],
   ans=0,
   why="EK 4.5.A.1.iii states that DNA replicates in S phase to form two sister chromatids, and EK 4.5.B.1 makes mitosis transfer a complete genome to each of two daughter cells. The table shows both events as numbers."),

 dict(q="Three tissues were sampled and their cells classified, with the results shown. Which relationship do the data show?",
   table=_T_TISSUE,
   choices=[
     "The tissue with the most cells in G0 has the fewest dividing cells",
     "The tissue with the most cells in G0 has the most dividing cells",
     "The number of cells in G0 is the same in all three tissues",
     "No tissue in the table contains any cells in G0",
     "Every cell counted in each tissue was found to be dividing"],
   ans=0,
   why="EK 4.5.A.1.v states that a cell in G0 no longer divides, so cells in that stage are not among the dividing ones. Skill 4.B asks students to describe the relationship between the two columns."),

 dict(q="Three cultures were counted at the start and after twenty-four hours, with the results shown. Which culture showed the largest percent increase in cell number?",
   table=_T_GROWTH,
   choices=[
     "The culture that ended with four times as many cells as it began with",
     "The culture that ended with the same number of cells as it began with",
     "The culture that gained two hundred cells over the period",
     "All three cultures increased by the same percentage",
     "None of the cultures increased in cell number at all"],
   ans=0,
   why="Skill 5.A asks for percent changes calculated from a table. Each culture began with the same number, so the largest final count is also the largest percent increase, and only one culture multiplied its number."),

 dict(q="A cell that had been dividing regularly stops dividing but remains alive and metabolically active, and later begins dividing again. What does the framework's account say happened?",
   choices=[
     "The cell entered G0 and later reentered the cell cycle in response to appropriate cues",
     "The cell completed mitosis without cytokinesis and later separated",
     "The cell replicated its DNA twice and later discarded one copy",
     "The cell permanently left the cell cycle and a new cell replaced it",
     "The cell remained in metaphase throughout the interval"],
   ans=0,
   why="EK 4.5.A.1.v states that a cell can enter G0, in which it no longer divides, but can reenter the cell cycle in response to appropriate cues, which is exactly the sequence described."),

 dict(q="At which stage of the cell cycle does the framework place the replication of DNA?",
   choices=[
     "S phase",
     "G1 phase",
     "G2 phase",
     "Metaphase",
     "Cytokinesis"],
   ans=0,
   why="EK 4.5.A.1.iii places DNA replication in S phase, where DNA in the form of chromatin replicates to form two sister chromatids connected at a centromere."),

 dict(q="At which stage of the cell cycle does the framework place the replication of the centrosomes?",
   choices=[
     "G2 phase",
     "S phase",
     "G1 phase",
     "Anaphase",
     "Telophase"],
   ans=0,
   why="EK 4.5.A.1.iv states that in G2 phase protein synthesis occurs, ATP is produced in large quantities, and centrosomes replicate. DNA replication is what belongs to S under EK 4.5.A.1.iii."),

 dict(q="Why does the framework describe the two products of mitosis as genetically identical to one another?",
   choices=[
     "Because mitosis transfers a complete genome from the parent cell to each of them",
     "Because each receives half of the parent cell's genome",
     "Because each exchanges genetic material with the other before separating",
     "Because each replicates its DNA a second time after separating",
     "Because each discards the chromosomes it does not need"],
   ans=0,
   why="EK 4.5.B.1 states that mitosis ensures the transfer of a complete genome from a parent cell to two genetically identical daughter cells. Complete transfer to each is what makes the two identical."),

 dict(q="A plant cell and an animal cell both complete mitosis. What difference does the framework identify in the step that follows?",
   choices=[
     "The plant cell forms a cell plate while the animal cell forms a cleavage furrow",
     "The plant cell forms a cleavage furrow while the animal cell forms a cell plate",
     "The plant cell divides its cytoplasm while the animal cell does not",
     "The animal cell divides its cytoplasm while the plant cell does not",
     "Neither cell divides its cytoplasm, so no daughter cells are produced"],
   ans=0,
   why="EK 4.5.B.1.vii states that in cytokinesis a cleavage furrow forms in animal cells or a cell plate forms in plant cells, resulting in two new daughter cells in both."),

 dict(q="Which stage of mitosis immediately follows the one in which the chromosomes are aligned along the equator of the cell?",
   choices=[
     "The stage in which paired sister chromatids separate and move toward the poles",
     "The stage in which sister chromatids condense and the spindle begins to form",
     "The stage in which the spindle breaks down and a new nuclear envelope develops",
     "The stage in which the centrosomes replicate",
     "The stage in which DNA is replicated from chromatin"],
   ans=0,
   why="EK 4.5.B.1.ii gives the order prophase, metaphase, anaphase, telophase, and EK 4.5.B.1.iv and EK 4.5.B.1.v place alignment at the equator in metaphase and the separation of chromatids in anaphase."),

 dict(q="Sister chromatids are formed at one stage and separated at another. Which pairing does the framework give?",
   choices=[
     "Formed during S phase and separated during anaphase",
     "Formed during anaphase and separated during S phase",
     "Formed during G2 and separated during metaphase",
     "Formed during prophase and separated during telophase",
     "Formed during cytokinesis and separated during G1"],
   ans=0,
   why="EK 4.5.A.1.iii has DNA replicate in S phase to form two sister chromatids joined at a centromere, and EK 4.5.B.1.v has paired sister chromatids separate in anaphase."),

 dict(q="Why can the proportion of cells found in a stage be used to estimate how long a cell spends in that stage?",
   choices=[
     "Because in a large sample of cells cycling continuously, the share caught in a stage reflects the share of the cycle it occupies",
     "Because every stage of the cell cycle lasts exactly the same length of time",
     "Because cells in the longest stage are the easiest ones to count",
     "Because the sample contains only cells that have just entered the cycle",
     "Because the number of cells in a sample changes while it is being counted"],
   ans=0,
   why="EK 4.5.A.1 makes the cycle a sequential series of stages, and skill 5.A asks students to work with ratios. A snapshot of many independently cycling cells distributes them across the stages in proportion to the time each stage takes."),

 dict(q="Which statement about the cell cycle is NOT supported by the framework?",
   choices=[
     "A cell that has entered G0 can never return to the cell cycle",
     "Centrosomes replicate during G2",
     "Mitosis produces two genetically identical daughter cells",
     "Spindle fibers align chromosomes along the equator during metaphase",
     "Nondividing cells may be held at a particular stage of the cell cycle"],
   ans=0,
   why="EK 4.5.A.1.v states that a cell in G0 can reenter the cell cycle in response to appropriate cues. The other four options restate EK 4.5.A.1.iv, EK 4.5.B.1, EK 4.5.B.1.iv and EK 4.5.A.1.vi directly."),

 dict(q="Taken together, what do the framework's statements about the cell cycle and mitosis assert?",
   choices=[
     "That a regulated sequence of interphase, mitosis and cytokinesis delivers a complete genome to each of two identical daughter cells",
     "That an unregulated sequence delivers half a genome to each of four daughter cells",
     "That the cycle consists of mitosis alone, with no preparatory stages",
     "That the daughter cells differ genetically from one another and from the parent",
     "That the cycle occurs only in cells that have permanently stopped growing"],
   ans=0,
   why="EK 4.5.A.1 and EK 4.5.A.1.i give the regulated sequence of interphase, mitosis and cytokinesis, and EK 4.5.B.1 gives the transfer of a complete genome to two genetically identical daughter cells."),
]
