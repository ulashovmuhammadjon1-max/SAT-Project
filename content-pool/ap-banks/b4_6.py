# AP BIOLOGY 4.6 Regulation of Cell Cycle
# CED effective Fall 2025, Unit 4 Cell Communication and Cell Cycle.
# Big Idea 3 Information Storage and Transmission.
# Learning objectives 4.6.A (describe the role of checkpoints in regulating the
# cell cycle) and 4.6.B (describe the effects of disruptions to the cell cycle
# on the cell or organism). Suggested skill 6.E, predict the causes or effects
# of a change in, or disruption to, one or more components in a biological
# system.
#
# Essential knowledge, in the framework's own terms:
#   4.6.A.1  A number of INTERNAL CONTROLS OR CHECKPOINTS regulate PROGRESSION
#            THROUGH THE CELL CYCLE.
#   4.6.A.2  INTERACTIONS BETWEEN CYCLINS AND CYCLIN-DEPENDENT KINASES control
#            the cell cycle.
#   4.6.B.1  DISRUPTIONS to the cell cycle may result in CANCER or APOPTOSIS
#            (programmed cell death).
#
# EXCLUSION STATEMENT OBSERVED, AND IT SHAPES THE WHOLE MODULE. The CED states
# that knowledge of SPECIFIC CYCLIN-CdK PAIRS OR GROWTH FACTORS is beyond the
# scope of the AP Exam, so no item names one. The CED also does NOT name the
# individual checkpoints -- it says only that A NUMBER of internal controls or
# checkpoints regulate progression -- so no key here asserts that a checkpoint
# sits at G1, at G2 or at any other named point. Every checkpoint item is about
# what a checkpoint DOES, which is what EK 4.6.A.1 states.
#
# BOUNDARY WITH 4.5, HELD DELIBERATELY. The stages themselves and what happens
# in each are topic 4.5 and carry no key here; items 17 and 28 chain to EK
# 4.5.A.1.vi and EK 4.5.B.1 and cite them. Apoptosis is also named in EK
# 4.3.A.1 as an outcome of signal transduction; here it enters only as EK
# 4.6.B.1's outcome of a DISRUPTION TO THE CYCLE, which is a different cause
# for the same event.
#
# NO FIGURES ANYWHERE. Cell cycle regulation invites a diagram and the bank
# cannot carry one, so every data item is a table and the question is asked of
# the table.
#
# FIVE choices (A-E). Plain prose, no LaTeX.
TOPIC = ("4.6", "Regulation of Cell Cycle", 4)

_T_CYCLIN = dict(
    headers=["Hours since the start of the cycle",
             "Cyclin concentration (hypothetical, arbitrary units)",
             "Cyclin-dependent kinase activity (hypothetical, arbitrary units)"],
    rows=[["0", "5", "4"],
          ["4", "20", "18"],
          ["8", "60", "55"],
          ["12", "85", "80"],
          ["16", "10", "9"]])

_T_CHECKPOINT = dict(
    headers=["Cell line (hypothetical)",
             "Cells with damaged DNA that halt before dividing (percent)",
             "Cells with damaged DNA that divide anyway (percent)"],
    rows=[["Normal cells", "94", "6"],
          ["Cells lacking a working checkpoint", "8", "92"]])

_T_OUTCOME = dict(
    headers=["Condition of the culture (hypothetical)",
             "Cells dividing under normal control (percent)",
             "Cells dividing without control (percent)",
             "Cells undergoing programmed cell death (percent)"],
    rows=[["Regulation intact", "95", "1", "4"],
          ["Regulation mildly disrupted", "40", "38", "22"],
          ["Regulation severely disrupted", "5", "30", "65"]])

_T_MITOTIC = dict(
    headers=["Culture (hypothetical)",
             "Cells in mitosis out of 500 counted, before treatment",
             "Cells in mitosis out of 500 counted, after treatment"],
    rows=[["Untreated control", "60", "58"],
          ["Treated so that a checkpoint is activated", "62", "5"]])

QUESTIONS = [
 dict(q="What does the framework say checkpoints do in a eukaryotic cell?",
   choices=[
     "They regulate progression through the cell cycle",
     "They replace the stages of the cell cycle with a single step",
     "They supply the energy the cell cycle requires",
     "They copy the cell's DNA before division",
     "They prevent any cell from ever dividing"],
   ans=0,
   why="EK 4.6.A.1 states that a number of internal controls or checkpoints regulate progression through the cell cycle. Regulating progression is what the statement assigns to them."),

 dict(q="The framework describes checkpoints as internal controls. What does that indicate about where the regulation comes from?",
   choices=[
     "The regulating machinery is part of the cell itself",
     "The regulating machinery is supplied by a neighboring organism",
     "The regulating machinery lies outside the plasma membrane",
     "The regulation is imposed by the physical size of the cell alone",
     "The regulation is applied only by the tissue and never by the cell"],
   ans=0,
   why="EK 4.6.A.1 calls them a number of INTERNAL controls or checkpoints that regulate progression through the cell cycle. The word places the controls within the cell."),

 dict(q="Which molecular interaction does the framework say controls the cell cycle?",
   choices=[
     "Interactions between cyclins and cyclin-dependent kinases",
     "Interactions between hydrolytic enzymes and their substrates",
     "Interactions between ribosomes and messenger RNA",
     "Interactions between chlorophyll and light",
     "Interactions between two sister chromatids at a centromere"],
   ans=0,
   why="EK 4.6.A.2 states that interactions between cyclins and cyclin-dependent kinases control the cell cycle."),

 dict(q="What two outcomes does the framework say disruptions to the cell cycle may produce?",
   choices=[
     "Cancer, or programmed cell death",
     "Cancer only, since a disrupted cell always survives",
     "Programmed cell death only, since a disrupted cell always dies",
     "A permanent increase in the accuracy of cell division",
     "The conversion of the cell into a prokaryotic cell"],
   ans=0,
   why="EK 4.6.B.1 states that disruptions to the cell cycle may result in cancer or apoptosis, which the framework glosses as programmed cell death. Both outcomes are named."),

 dict(q="Which statement best summarizes the framework's account of how the cell cycle is controlled?",
   choices=[
     "Internal checkpoints regulate progression, and cyclin and kinase interactions control the cycle",
     "The cycle is uncontrolled and proceeds at whatever rate conditions allow",
     "The cycle is controlled entirely by signals from other organisms",
     "The cycle is controlled by the amount of DNA a cell contains",
     "The cycle is controlled by the number of organelles a cell has built"],
   ans=0,
   why="EK 4.6.A.1 gives the checkpoints that regulate progression and EK 4.6.A.2 gives the cyclin and cyclin-dependent kinase interactions that control the cycle. Those are the two controls the framework names."),

 dict(q="A cell's checkpoints stop functioning while the rest of its machinery is unaffected. What is the most reasonable prediction?",
   choices=[
     "The cell progresses through the cycle without the checks that would normally regulate it",
     "The cell stops progressing through the cycle immediately and permanently",
     "The cell begins progressing backward through the stages of the cycle",
     "The cell's cyclins are converted into cyclin-dependent kinases",
     "The cell duplicates its checkpoints instead of its chromosomes"],
   ans=0,
   why="EK 4.6.A.1 makes checkpoints the internal controls that regulate progression through the cell cycle, so losing them removes the regulation rather than the progression. Skill 6.E asks for exactly this prediction."),

 dict(q="A mutation prevents a cell from producing a cyclin at the point in the cycle where it would normally accumulate. What is the most reasonable prediction?",
   choices=[
     "The interaction that would control the cycle at that point does not occur, so the cycle does not progress normally",
     "The cycle progresses more quickly because there is one fewer molecule to make",
     "The cell's cyclin-dependent kinases become permanently active instead",
     "The cell replaces the missing cyclin with a hydrolytic enzyme",
     "The cell's DNA replicates twice before the next division"],
   ans=0,
   why="EK 4.6.A.2 states that interactions BETWEEN cyclins and cyclin-dependent kinases control the cell cycle, so removing one partner removes the interaction that provides the control at that point."),

 dict(q="A mutation leaves a cyclin-dependent kinase active at all times rather than only when its partner is present. What is the most reasonable prediction?",
   choices=[
     "The control that depends on the two acting together is lost, so progression is no longer properly regulated",
     "The cell cycle stops because a kinase cannot act without changing",
     "The cell converts the kinase into a cyclin to restore the balance",
     "The cell's checkpoints increase in number to compensate exactly",
     "The cell replicates its DNA without ever entering interphase"],
   ans=0,
   why="EK 4.6.A.2 makes the INTERACTION between cyclins and cyclin-dependent kinases the control, so a kinase acting independently of that interaction is no longer subject to the control the interaction provides."),

 dict(q="A cell's DNA is damaged and its checkpoints are working normally. What does the framework's account predict?",
   choices=[
     "Progression through the cycle is regulated rather than proceeding as though nothing had happened",
     "Progression continues unchanged, because checkpoints act only on undamaged cells",
     "The damaged DNA is converted into cyclin",
     "The cell immediately becomes cancerous",
     "The cell's kinases are removed from it"],
   ans=0,
   why="EK 4.6.A.1 states that internal controls or checkpoints regulate progression through the cell cycle, which is what a control does when a cell is not ready to proceed."),

 dict(q="One possible outcome the framework attaches to a disrupted cell cycle is programmed cell death. What is that outcome called?",
   choices=[
     "Apoptosis",
     "Cytokinesis",
     "Denaturation",
     "Endosymbiosis",
     "Chemiosmosis"],
   ans=0,
   why="EK 4.6.B.1 states that disruptions to the cell cycle may result in cancer or apoptosis, giving programmed cell death as the gloss on that term."),

 dict(q="The other outcome the framework attaches to a disrupted cell cycle is a disease of division. Which is it?",
   choices=[
     "Cancer",
     "Denatured enzymes",
     "Loss of the plasma membrane",
     "Failure of photosynthesis",
     "Loss of the mitochondrion"],
   ans=0,
   why="EK 4.6.B.1 states that disruptions to the cell cycle may result in cancer or apoptosis. Cancer is the first of the two outcomes the statement names."),

 dict(q="Cyclin concentration and kinase activity were measured through one cell cycle, with the results shown. Which conclusion do these data support?",
   table=_T_CYCLIN,
   choices=[
     "Kinase activity rises and falls together with cyclin concentration",
     "Kinase activity falls as cyclin concentration rises",
     "Kinase activity is constant while cyclin concentration changes",
     "Cyclin concentration is constant while kinase activity changes",
     "Neither quantity changes over the course of the cycle"],
   ans=0,
   why="EK 4.6.A.2 states that interactions between cyclins and cyclin-dependent kinases control the cell cycle, and the two columns move together at every time sampled, which is what such an interaction predicts."),

 dict(q="Two cell lines with damaged DNA were compared, with the results shown. What do the data indicate about the checkpoint?",
   table=_T_CHECKPOINT,
   choices=[
     "The checkpoint is what halts damaged cells before they divide",
     "The checkpoint is what causes damaged cells to divide",
     "The checkpoint has no effect on whether damaged cells divide",
     "Both lines halt damaged cells at the same rate",
     "Neither line contains any cells with damaged DNA"],
   ans=0,
   why="EK 4.6.A.1 makes checkpoints the internal controls that regulate progression through the cell cycle. The line lacking a working checkpoint is the one whose damaged cells proceed, which is that regulation shown as data."),

 dict(q="Cultures with intact, mildly disrupted and severely disrupted cell cycle regulation were compared, with the results shown. Which conclusion is best supported?",
   table=_T_OUTCOME,
   choices=[
     "Disrupting regulation raises both uncontrolled division and programmed cell death above their levels in the intact culture",
     "Disrupting regulation raises uncontrolled division while programmed cell death stays at its intact level",
     "Disrupting regulation raises programmed cell death while uncontrolled division stays at its intact level",
     "Disrupting regulation lowers both uncontrolled division and programmed cell death",
     "Disrupting regulation leaves all three measures unchanged"],
   ans=0,
   why="EK 4.6.B.1 states that disruptions to the cell cycle may result in cancer OR apoptosis, so both outcomes are available from one disruption, which is what the three rows of the table show."),

 dict(q="The number of cells in mitosis was counted before and after a treatment, with the results shown. What do the data indicate?",
   table=_T_MITOTIC,
   choices=[
     "The treated cells stopped entering mitosis while the untreated cells continued as before",
     "The untreated cells stopped entering mitosis while the treated cells continued as before",
     "Both cultures stopped entering mitosis after the treatment",
     "Neither culture changed after the treatment",
     "The treated cells entered mitosis more often after the treatment than before"],
   ans=0,
   why="EK 4.6.A.1 makes checkpoints the internal controls that regulate progression through the cell cycle, so activating one should hold cells short of the next stage. Only the treated culture's count falls."),

 dict(q="Why does the framework's account of mitosis make regulation of the cell cycle important?",
   choices=[
     "Because mitosis is supposed to deliver a complete genome to each daughter cell, and unchecked progression puts that outcome at risk",
     "Because mitosis produces four daughter cells that must be counted",
     "Because mitosis requires no energy and so cannot be regulated by energy supply",
     "Because mitosis occurs only in cells that have already left the cell cycle",
     "Because mitosis is the only stage in which a cell is metabolically active"],
   ans=0,
   why="EK 4.5.B.1 makes mitosis the transfer of a complete genome to two genetically identical daughter cells, and EK 4.6.A.1 makes checkpoints the internal controls on progression. Regulation is what protects the outcome mitosis is supposed to produce."),

 dict(q="A cell that is not ready to divide remains at one stage rather than continuing. Which parts of the framework describe that situation?",
   choices=[
     "Nondividing cells may be held at a particular stage, and internal checkpoints regulate progression through the cycle",
     "Nondividing cells must complete the cycle before they can stop, and checkpoints only speed progression",
     "Nondividing cells cannot exist, because every cell divides continuously",
     "Nondividing cells lose their chromosomes and cannot re-enter the cycle",
     "Nondividing cells are always cancerous by definition"],
   ans=0,
   why="EK 4.5.A.1.vi states that nondividing cells may exit the cell cycle or be held at a particular stage in it, and EK 4.6.A.1 makes internal controls or checkpoints what regulates progression."),

 dict(q="A chemical is applied that prevents cyclin-dependent kinase activity throughout a culture. What is the most reasonable prediction?",
   choices=[
     "Progression through the cell cycle is impaired, because the controlling interaction cannot occur",
     "Progression accelerates, because one control has been removed",
     "The cells convert their cyclins into checkpoints",
     "The cells complete mitosis but skip interphase entirely",
     "The cells become immune to any disruption of the cycle"],
   ans=0,
   why="EK 4.6.A.2 states that interactions between cyclins and cyclin-dependent kinases control the cell cycle, so blocking the kinase removes one partner in the interaction that provides the control."),

 dict(q="An investigator wants to justify the claim that a cell line has a defective checkpoint. Which evidence would justify it?",
   choices=[
     "Cells of that line proceed through the cycle under conditions in which normal cells halt",
     "Cells of that line divide at the same rate as normal cells under ordinary conditions",
     "Cells of that line are larger than normal cells",
     "Cells of that line contain cyclins and cyclin-dependent kinases",
     "Cells of that line can be grown in culture for many generations"],
   ans=0,
   why="EK 4.6.A.1 defines a checkpoint by its regulation of progression, so a defect shows as progression where regulation should have prevented it. Every other listed observation is true of normal cells too."),

 dict(q="Two cell lines are compared. One halts under conditions that should stop the cycle and one does not. What does the framework's account say distinguishes them?",
   choices=[
     "The regulation of progression by internal controls is working in one line and not in the other",
     "One line has a cell cycle and the other has none",
     "One line has DNA and the other does not",
     "One line performs mitosis and the other performs cytokinesis",
     "One line is prokaryotic and the other eukaryotic"],
   ans=0,
   why="EK 4.6.A.1 states that a number of internal controls or checkpoints regulate progression through the cell cycle, which is the difference between a line that halts appropriately and one that does not."),

 dict(q="Two cultures receive the same disruption to their cell cycle regulation, and one develops uncontrolled division while the other loses many cells to programmed cell death. How does the framework accommodate both results?",
   choices=[
     "It states that disruptions MAY result in cancer OR apoptosis, so both are available outcomes",
     "It states that every disruption results in cancer, so the second culture must be mistaken",
     "It states that every disruption results in apoptosis, so the first culture must be mistaken",
     "It states that disruptions have no effect, so neither result can occur",
     "It states that the two outcomes cannot arise from the same kind of disruption"],
   ans=0,
   why="EK 4.6.B.1 states that disruptions to the cell cycle may result in cancer or apoptosis, a disjunction that allows either outcome rather than requiring one."),

 dict(q="What does the framework's use of the phrase A NUMBER OF internal controls indicate about how the cycle is regulated?",
   choices=[
     "More than one control acts on progression through the cycle",
     "Exactly one control acts on progression through the cycle",
     "The number of controls is the same in every organism and is stated in the framework",
     "The controls act only once in the lifetime of a cell",
     "The controls act on the cell's genome rather than on the cycle"],
   ans=0,
   why="EK 4.6.A.1 states that A NUMBER OF internal controls or checkpoints regulate progression through the cell cycle. The phrase asserts more than one without committing to a count."),

 dict(q="Cells in a culture continue through the cycle under conditions that would normally hold them short of division. Which description fits the framework's account?",
   choices=[
     "The cycle's regulation has been disrupted, an outcome of which may be cancer",
     "The cycle's regulation has been strengthened, an outcome of which may be cancer",
     "The cells have exited the cycle into a nondividing stage",
     "The cells have replaced their checkpoints with cyclins",
     "The cells have stopped producing cyclin-dependent kinases"],
   ans=0,
   why="EK 4.6.A.1 makes checkpoints the internal controls on progression, and EK 4.6.B.1 states that disruptions to the cell cycle may result in cancer or apoptosis. Progression where regulation should have prevented it is such a disruption."),

 dict(q="A researcher wants to determine whether a treatment halts cells before division. What comparison would settle it?",
   choices=[
     "Counting the proportion of cells in mitosis before and after treatment in both treated and untreated cultures",
     "Counting the total number of cells in the treated culture only",
     "Measuring the size of the treated cells and comparing it with a textbook value",
     "Recording how long the treatment takes to prepare",
     "Determining how many organelles each treated cell contains"],
   ans=0,
   why="EK 4.6.A.1 makes a checkpoint a control on PROGRESSION, so the measurement has to be of progression, and skills 4.B and 5.A make the proportion of cells at a stage the way it is measured. An untreated culture is what shows the change was the treatment's."),

 dict(q="A student claims that every disruption to the cell cycle produces cancer. How does the framework's statement bear on that claim?",
   choices=[
     "It does not support the claim, because it names programmed cell death as an alternative outcome",
     "It supports the claim, because cancer is the only outcome the framework names",
     "It does not support the claim, because the framework denies that disruptions have any outcome",
     "It supports the claim, because apoptosis is a form of cancer",
     "It cannot bear on the claim, because the framework does not mention disruptions"],
   ans=0,
   why="EK 4.6.B.1 states that disruptions to the cell cycle may result in cancer OR apoptosis, so cancer is one of two named outcomes rather than a necessary consequence."),

 dict(q="A cell's cycle regulation is disrupted, and separately its capacity for programmed cell death is disabled. Which outcome named by the framework remains available?",
   choices=[
     "Cancer, since the other named outcome has been removed",
     "Programmed cell death, since the disruption restores it",
     "Neither outcome, since a disrupted cycle has no consequence",
     "Both outcomes equally, since disabling one does not affect its availability",
     "The cell reverts to a normally regulated cycle"],
   ans=0,
   why="EK 4.6.B.1 names cancer and apoptosis as the two outcomes a disruption may produce. Removing the capacity for one leaves the other as the available outcome of that disruption."),

 dict(q="Why does a cyclin concentration that rises and then falls fit the framework's account of how the cycle is controlled?",
   choices=[
     "Because control comes from the interaction between cyclins and their kinases, so a changing amount of cyclin gives control that varies through the cycle",
     "Because the cyclin itself replaces the checkpoints while its concentration is high",
     "Because a falling cyclin concentration converts the cell into a nondividing cell permanently",
     "Because cyclin concentration determines how much DNA a cell contains",
     "Because a constant cyclin concentration would make the cycle run faster"],
   ans=0,
   why="EK 4.6.A.2 states that interactions between cyclins and cyclin-dependent kinases control the cell cycle, so an interaction whose strength varies with cyclin amount supplies control that varies with position in the cycle."),

 dict(q="How does the regulation described in this topic relate to the stages described for the cell cycle itself?",
   choices=[
     "The controls act on progression from one stage of the cycle to the next",
     "The controls replace the stages of the cycle with a single continuous process",
     "The controls act only after cytokinesis has been completed",
     "The controls determine how many chromosomes each stage contains",
     "The controls apply only to cells that have permanently left the cycle"],
   ans=0,
   why="EK 4.6.A.1 states that internal controls or checkpoints regulate PROGRESSION THROUGH the cell cycle, and EK 4.5.A.1.i makes the cycle a sequence of stages, so progression is movement from one stage to the next."),

 dict(q="Which statement about the regulation of the cell cycle is NOT supported by the framework?",
   choices=[
     "A disrupted cell cycle always results in cancer and never in programmed cell death",
     "Internal controls or checkpoints regulate progression through the cell cycle",
     "Interactions between cyclins and cyclin-dependent kinases control the cell cycle",
     "Disruptions to the cell cycle may result in programmed cell death",
     "More than one internal control acts on the cell cycle"],
   ans=0,
   why="EK 4.6.B.1 names cancer OR apoptosis as possible results of a disruption, which rules out the always-and-never reading. The other four options restate EK 4.6.A.1, EK 4.6.A.2 and EK 4.6.B.1."),

 dict(q="Taken together, what do the framework's statements about the regulation of the cell cycle assert?",
   choices=[
     "That internal checkpoints and cyclin and kinase interactions control progression, and that disrupting that control may produce cancer or programmed cell death",
     "That the cycle is unregulated, and that disrupting it has no consequence for the cell",
     "That the cycle is regulated only from outside the cell, and that disruption always kills the cell",
     "That checkpoints act after division rather than before it, and that disruption is always harmless",
     "That cyclins act alone without kinases, and that cancer is the only possible disruption outcome"],
   ans=0,
   why="EK 4.6.A.1 gives the internal controls on progression, EK 4.6.A.2 gives the cyclin and cyclin-dependent kinase interactions, and EK 4.6.B.1 gives cancer or apoptosis as the possible results of a disruption."),
]
