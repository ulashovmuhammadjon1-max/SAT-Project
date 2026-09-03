# AP BIOLOGY 4.2 Introduction to Signal Transduction
# CED effective Fall 2025, Unit 4 Cell Communication and Cell Cycle.
# Big Idea 3 Information Storage and Transmission.
# Learning objectives 4.2.A (describe the components of a signal transduction
# pathway) and 4.2.B (describe the role of components of a signal transduction
# pathway in producing a cellular response).
# Suggested skill 1.A, describe biological concepts and processes.
#
# Essential knowledge, in the framework's own terms:
#   4.2.A.1     signal transduction pathways LINK SIGNAL RECEPTIONS WITH
#               CELLULAR RESPONSES
#   4.2.A.2     many pathways include PROTEIN MODIFICATIONS and involve
#               PHOSPHORYLATION CASCADES
#   4.2.B.1     signaling begins with the recognition of a chemical messenger,
#               a LIGAND, by a RECEPTOR PROTEIN in a TARGET CELL
#     i.        the LIGAND-BINDING DOMAIN of a receptor recognizes a SPECIFIC
#               chemical messenger, which can be a PEPTIDE (PROTEIN) or a SMALL
#               MOLECULE
#     ii.       G PROTEIN-COUPLED RECEPTORS are an example of a receptor
#               protein in eukaryotes
#     iii.      receptors may be located ON THE SURFACE of a target cell or IN
#               THE CYTOPLASM OR NUCLEUS of the target cell
#   4.2.B.2     signaling cascades RELAY signals from receptors to cell targets,
#               often AMPLIFYING them, resulting in the appropriate responses;
#               responses could include CELL GROWTH, SECRETION OF MOLECULES, or
#               GENE EXPRESSION
#     i.        after the ligand binds, the INTRACELLULAR DOMAIN of the receptor
#               CHANGES SHAPE, initiating transduction
#     ii.       ENZYMES and SECOND MESSENGERS such as CYCLIC AMP relay and
#               amplify the intracellular signal
#     iii.      HORMONES are an example of a signaling messenger that can travel
#               LONG DISTANCES IN THE BLOODSTREAM
#     iv.       binding of ligands to LIGAND-GATED CHANNELS can cause the
#               channel to OPEN OR CLOSE
#
# BOUNDARY WITH 4.1 AND 4.3, HELD DELIBERATELY. Topic 4.1 owns the MODE and
# DISTANCE of communication -- direct contact against chemical signaling, local
# regulators against long-distance signals -- and no key here rests on that
# distinction; the hormone items below are keyed to EK 4.2.B.2.iii's place for
# hormones INSIDE a transduction pathway, not to their range. Topic 4.3 owns
# what a pathway's output does to the cell (altered gene expression, altered
# phenotype, apoptosis) and what MUTATIONS or CHEMICALS do to a pathway, so
# this module contains no mutation item and no inhibitor item at all. The
# suggested skill here is 1.A, DESCRIBE, and the module is written to it.
#
# Tables are labelled HYPOTHETICAL and every keyed conclusion is recoverable
# from the table itself. No stem refers to a figure.
#
# FIVE choices (A-E). Plain prose, no LaTeX.
TOPIC = ("4.2", "Introduction to Signal Transduction", 4)

_T_AMPLIFY = dict(
    headers=["Stage of the signaling cascade",
             "Activated molecules present at that stage (hypothetical)"],
    rows=[["Ligand molecules bound at the surface", "10"],
          ["Receptor proteins activated", "10"],
          ["Relay enzyme molecules activated", "1,000"],
          ["Second messenger molecules produced", "100,000"],
          ["Target enzyme molecules activated", "1,000,000"]])

_T_BINDING = dict(
    headers=["Receptor protein studied",
             "Sites occupied by ligand P (hypothetical, percent)",
             "Sites occupied by ligand Q (hypothetical, percent)"],
    rows=[["Receptor 1", "92", "1"],
          ["Receptor 2", "2", "88"],
          ["Receptor 3", "1", "2"]])

_T_LOCATION = dict(
    headers=["Cell fraction assayed",
             "Receptor for messenger M detected (hypothetical, units)",
             "Receptor for messenger N detected (hypothetical, units)"],
    rows=[["Plasma membrane", "120", "3"],
          ["Cytosol", "4", "95"],
          ["Nucleus", "2", "40"]])

_T_CHANNEL = dict(
    headers=["Condition of the membrane preparation",
             "Ligand supplied (hypothetical, micromolar)",
             "Ion flow through the channel (hypothetical, arbitrary units)"],
    rows=[["No ligand supplied", "0", "2"],
          ["Low ligand supplied", "1", "28"],
          ["High ligand supplied", "10", "95"]])

QUESTIONS = [
 dict(q="What does the framework say a signal transduction pathway does?",
   choices=[
     "It links the reception of a signal to a cellular response",
     "It links two receptors together so that neither can bind a signal",
     "It replaces the need for a cell to receive any signal",
     "It converts a cellular response back into the original signal",
     "It moves a signal from one organism to another"],
   ans=0,
   why="EK 4.2.A.1 states that signal transduction pathways link signal receptions with cellular responses. Reception at one end and response at the other are what the pathway connects."),

 dict(q="What kinds of molecular events does the framework say many signal transduction pathways include?",
   choices=[
     "Protein modifications, including phosphorylation cascades",
     "Replication of the cell's chromosomes",
     "Digestion of the receptor by hydrolytic enzymes",
     "Synthesis of new plasma membrane around the signal",
     "Conversion of the ligand into a nucleic acid"],
   ans=0,
   why="EK 4.2.A.2 states that many signal transduction pathways include protein modifications and involve phosphorylation cascades."),

 dict(q="What does the framework call the chemical messenger that a receptor protein recognizes?",
   choices=[
     "A ligand",
     "A second messenger",
     "A phosphorylation cascade",
     "An allosteric site",
     "A target cell"],
   ans=0,
   why="EK 4.2.B.1 states that signaling begins with the recognition of a chemical messenger, a ligand, by a receptor protein in a target cell. A second messenger acts later, inside the cell, under EK 4.2.B.2.ii."),

 dict(q="Which part of a receptor protein recognizes the chemical messenger, and how selective is that recognition?",
   choices=[
     "The ligand-binding domain, which recognizes a specific chemical messenger",
     "The ligand-binding domain, which recognizes any chemical messenger it encounters",
     "The intracellular domain, which recognizes a specific chemical messenger",
     "The whole receptor at once, with no particular region responsible",
     "A separate protein that carries the messenger to the receptor"],
   ans=0,
   why="EK 4.2.B.1.i states that the ligand-binding domain of a receptor recognizes a specific chemical messenger. Both the region and the selectivity are given in that sentence; the intracellular domain acts later under EK 4.2.B.2.i."),

 dict(q="What kinds of molecule does the framework say a ligand can be?",
   choices=[
     "A peptide, meaning a protein, or a small molecule",
     "A protein only, since receptors recognize only proteins",
     "A small molecule only, since a protein is too large to be recognized",
     "A nucleic acid only",
     "A phospholipid only"],
   ans=0,
   why="EK 4.2.B.1.i states that the specific chemical messenger a ligand-binding domain recognizes can be a peptide, which the framework glosses as a protein, or a small molecule."),

 dict(q="Which of these does the framework give as an example of a receptor protein in eukaryotes?",
   choices=[
     "G protein-coupled receptors",
     "Ribosomes",
     "ATP synthase",
     "Hydrolytic enzymes of the lysosome",
     "The nuclear envelope"],
   ans=0,
   why="EK 4.2.B.1.ii names G protein-coupled receptors as an example of a receptor protein in eukaryotes. The other structures are introduced elsewhere in the framework for other purposes."),

 dict(q="Where does the framework say receptors may be located in a target cell?",
   choices=[
     "On the cell surface, or in the cytoplasm or nucleus",
     "On the cell surface only",
     "In the nucleus only",
     "In the cytoplasm only, never at the surface or in the nucleus",
     "Outside the cell entirely, floating in the surrounding fluid"],
   ans=0,
   why="EK 4.2.B.1.iii states that receptors may be located on the surface of a target cell or in the cytoplasm or nucleus of the target cell. All three locations are named."),

 dict(q="What does the framework say signaling cascades do between the receptor and the cell's targets?",
   choices=[
     "They relay the signal onward and often amplify it",
     "They relay the signal onward and always weaken it",
     "They hold the signal at the receptor until the ligand is released",
     "They convert the signal back into a ligand outside the cell",
     "They prevent the receptor from producing any response"],
   ans=0,
   why="EK 4.2.B.2 states that signaling cascades relay signals from receptors to cell targets, often amplifying the incoming signals, resulting in the appropriate responses by the cell."),

 dict(q="Which cellular responses does the framework name as possible outcomes of a signaling cascade?",
   choices=[
     "Cell growth, secretion of molecules, or gene expression",
     "Cell growth only",
     "Secretion of molecules only",
     "Replication of the ligand and its release from the cell",
     "Loss of the plasma membrane and merging with a neighboring cell"],
   ans=0,
   why="EK 4.2.B.2 states that responses could include cell growth, secretion of molecules, or gene expression. All three are named together in that sentence."),

 dict(q="According to the framework, what happens to a receptor protein immediately after its ligand binds?",
   choices=[
     "Its intracellular domain changes shape, initiating transduction of the signal",
     "Its intracellular domain is removed from the cell",
     "Its ligand-binding domain is converted into a second messenger",
     "The whole receptor leaves the membrane and enters the nucleus",
     "The receptor is broken down before any signal can be passed on"],
   ans=0,
   why="EK 4.2.B.2.i states that after the ligand binds, the intracellular domain of a receptor protein changes shape, initiating transduction of the signal."),

 dict(q="What role does the framework give to enzymes and to second messengers such as cyclic AMP?",
   choices=[
     "They relay and amplify the intracellular signal",
     "They bind the ligand outside the cell before the receptor does",
     "They replace the receptor once the ligand has bound",
     "They carry the signal out of the cell to a neighboring cell",
     "They end the signal by destroying the receptor"],
   ans=0,
   why="EK 4.2.B.2.ii states that enzymes and second messengers such as cyclic AMP relay and amplify the intracellular signal. Both jobs are named in that sentence."),

 dict(q="How does the framework describe hormones within its account of signaling?",
   choices=[
     "As an example of a signaling messenger that can travel long distances in the bloodstream",
     "As an example of a second messenger produced inside the target cell",
     "As an example of a receptor protein found only at the cell surface",
     "As an example of an enzyme that phosphorylates other proteins",
     "As an example of a channel that opens when a ligand binds"],
   ans=0,
   why="EK 4.2.B.2.iii states that hormones are an example of a signaling messenger that can travel long distances in the bloodstream. Second messengers, receptors, enzymes and channels are separate components in the same set of statements."),

 dict(q="What does the framework say can happen when a ligand binds to a ligand-gated channel?",
   choices=[
     "The channel can be caused to open or to close",
     "The channel is permanently destroyed",
     "The channel is converted into a receptor of a different kind",
     "The channel leaves the membrane and enters the nucleus",
     "The channel begins synthesizing the ligand it just bound"],
   ans=0,
   why="EK 4.2.B.2.iv states that the binding of ligands to ligand-gated channels can cause the channel to open or close. Both directions are part of the statement."),

 dict(q="What does it mean for a signaling cascade to amplify an incoming signal?",
   choices=[
     "A small number of bound signal molecules leads to a much larger number of activated molecules inside the cell",
     "The signal molecule itself grows larger as it passes through the cell",
     "The cell releases more of the same signal molecule than it received",
     "The receptor binds the same ligand repeatedly without releasing it",
     "The response occurs sooner than it otherwise would but at the same size"],
   ans=0,
   why="EK 4.2.B.2 states that signaling cascades relay signals from receptors to cell targets, OFTEN AMPLIFYING the incoming signals, and EK 4.2.B.2.ii assigns that amplification to enzymes and second messengers acting inside the cell."),

 dict(q="The numbers of activated molecules at successive stages of one cascade were counted, with the results shown. Which conclusion do these data support?",
   table=_T_AMPLIFY,
   choices=[
     "The number of activated molecules grows at successive stages, so the signal is amplified",
     "The number of activated molecules falls at successive stages, so the signal is weakened",
     "The number of activated molecules is the same at every stage",
     "The largest number of molecules is found at the stage where ligand binds",
     "Amplification occurs only between the ligand and the receptor"],
   ans=0,
   why="EK 4.2.B.2 states that cascades often amplify the incoming signals and EK 4.2.B.2.ii names enzymes and second messengers as what does the amplifying. A rising count from stage to stage is that statement expressed as data."),

 dict(q="Two chemical messengers were offered to three receptor proteins, with the results shown. Which property of receptors do the data illustrate?",
   table=_T_BINDING,
   choices=[
     "A receptor's binding domain recognizes a specific messenger rather than any messenger",
     "A receptor's binding domain recognizes every messenger it encounters equally",
     "The three receptors are interchangeable with one another",
     "Neither messenger is recognized by any of the three receptors",
     "Both messengers are recognized equally well by the same receptor"],
   ans=0,
   why="EK 4.2.B.1.i states that the ligand-binding domain of a receptor recognizes a SPECIFIC chemical messenger. Each receptor in the table binds at most one of the two messengers offered."),

 dict(q="Cell fractions were assayed for the receptors of two messengers, with the results shown. What do the data indicate about where receptors are found?",
   table=_T_LOCATION,
   choices=[
     "One messenger's receptor is found at the cell surface and the other's inside the cell",
     "Both messengers' receptors are found only at the cell surface",
     "Both messengers' receptors are found only inside the cell",
     "Neither messenger's receptor is found in any fraction assayed",
     "Both messengers share a single receptor found in one fraction"],
   ans=0,
   why="EK 4.2.B.1.iii states that receptors may be located on the surface of a target cell or in the cytoplasm or nucleus, so both distributions in the table are consistent with the framework and the two messengers differ in which one they use."),

 dict(q="A membrane preparation containing a ligand-gated channel was supplied with increasing amounts of its ligand, with the results shown. What do the data indicate?",
   table=_T_CHANNEL,
   choices=[
     "Ion flow rises as ligand is supplied, so binding of the ligand opens the channel",
     "Ion flow falls as ligand is supplied, so binding of the ligand closes the channel",
     "Ion flow is unchanged by the amount of ligand supplied",
     "Ion flow is greatest when no ligand is supplied",
     "Ion flow occurs only when the ligand is absent from the preparation"],
   ans=0,
   why="EK 4.2.B.2.iv states that the binding of ligands to ligand-gated channels can cause the channel to open or close. Flow rising with ligand supplied is the opening case shown as data."),

 dict(q="A receptor for a particular messenger is found in the nucleus of its target cell rather than at the cell surface. How does that fit the framework?",
   choices=[
     "It is consistent, because receptors may be located in the nucleus of a target cell",
     "It is inconsistent, because every receptor must sit in the plasma membrane",
     "It is inconsistent, because a receptor in the nucleus could not be a protein",
     "It is consistent only if the messenger is a second messenger",
     "It is consistent only if the cell has no plasma membrane"],
   ans=0,
   why="EK 4.2.B.1.iii states that receptors may be located on the surface of a target cell or in the cytoplasm or nucleus of the target cell, so a nuclear location is one of the three the framework names."),

 dict(q="A molecule released by one cell is recognized by a protein in a second cell, and a response follows. Which term does the framework apply to each of the two molecules?",
   choices=[
     "The released molecule is the ligand and the recognizing protein is the receptor",
     "The released molecule is the receptor and the recognizing protein is the ligand",
     "Both molecules are ligands, since both take part in signaling",
     "Both molecules are receptors, since both are in contact with the signal",
     "Neither term applies until a response has been completed"],
   ans=0,
   why="EK 4.2.B.1 states that signaling begins with the recognition of a chemical messenger, a ligand, by a receptor protein in a target cell. The molecule recognized is the ligand and the protein doing the recognizing is the receptor."),

 dict(q="In what order do the framework's components of signaling act on the way from a messenger outside the cell to a response?",
   choices=[
     "A ligand is recognized by a receptor, a cascade relays the signal, and the cell responds",
     "A cascade relays a signal, a ligand is recognized by a receptor, and the cell responds",
     "The cell responds, a receptor recognizes a ligand, and a cascade relays the signal",
     "A receptor recognizes a response, a ligand relays it, and a cascade is produced",
     "A ligand is produced by the cascade and then recognized by the response"],
   ans=0,
   why="EK 4.2.B.1 places recognition of the ligand by the receptor at the start, EK 4.2.B.2 puts the relaying cascade between receptor and cell target, and EK 4.2.A.1 makes the linking of reception to response the pathway's function."),

 dict(q="Two cells are exposed to the same chemical messenger, and only one of them responds. Which explanation is supported by the framework?",
   choices=[
     "Only the responding cell has a receptor whose binding domain recognizes that messenger",
     "Only the responding cell was close enough for the messenger to reach it",
     "The messenger changed into a different molecule before reaching the second cell",
     "The second cell has more receptors than it can use at one time",
     "The second cell has already completed its response and cannot respond again"],
   ans=0,
   why="EK 4.2.B.1 makes signaling begin with recognition by a receptor protein in a TARGET cell, and EK 4.2.B.1.i makes the ligand-binding domain recognize a specific messenger. A cell without the matching receptor is not a target."),

 dict(q="What is the relationship between the enzymes and second messengers of a pathway and the receptor that begins it?",
   choices=[
     "They act after the receptor, carrying and enlarging the signal it has started",
     "They act before the receptor, delivering the ligand to its binding domain",
     "They replace the receptor so that the ligand is no longer needed",
     "They are the same molecules as the receptor under a different name",
     "They act outside the cell while the receptor acts inside it"],
   ans=0,
   why="EK 4.2.B.2.i places the shape change of the receptor's intracellular domain at the start of transduction, and EK 4.2.B.2.ii has enzymes and second messengers such as cyclic AMP relay and amplify the intracellular signal that follows."),

 dict(q="What does it mean to say that a cascade RELAYS a signal?",
   choices=[
     "Each component passes the signal to the next, carrying it from the receptor to the cell's targets",
     "Each component destroys the signal so that the next must generate it again",
     "The signal is carried backward from the cell's targets to the receptor",
     "The signal is held unchanged at the receptor until the response is complete",
     "The signal is passed out of the cell and back in again at each step"],
   ans=0,
   why="EK 4.2.B.2 states that signaling cascades relay signals from receptors to cell targets, resulting in the appropriate responses by the cell. Relaying is passing the signal along that route."),

 dict(q="A signaling messenger is carried in the bloodstream from the cells that release it to its target cells. What does the framework call such a messenger?",
   choices=[
     "A hormone",
     "A second messenger",
     "A ligand-gated channel",
     "A phosphorylation cascade",
     "An intracellular domain"],
   ans=0,
   why="EK 4.2.B.2.iii states that hormones are an example of a signaling messenger that can travel long distances in the bloodstream. The other four terms name components that act at or inside the target cell."),

 dict(q="A receptor recognizes a messenger that is a short chain of amino acids. Is that consistent with the framework's account of ligands?",
   choices=[
     "Yes, because the framework allows a ligand to be a peptide as well as a small molecule",
     "No, because the framework restricts ligands to small molecules",
     "No, because a chain of amino acids can only be a receptor",
     "Yes, but only if the receptor is located in the nucleus",
     "Yes, but only if the messenger is produced inside the target cell"],
   ans=0,
   why="EK 4.2.B.1.i states that the specific chemical messenger recognized by a ligand-binding domain can be a peptide, which the framework glosses as a protein, or a small molecule."),

 dict(q="A eukaryotic cell surface protein binds an external messenger and begins a transduction pathway. Which of the framework's named examples does this fit?",
   choices=[
     "A G protein-coupled receptor",
     "A second messenger such as cyclic AMP",
     "A hormone travelling in the bloodstream",
     "A phosphorylation cascade",
     "The intracellular domain acting alone"],
   ans=0,
   why="EK 4.2.B.1.ii names G protein-coupled receptors as an example of a receptor protein in eukaryotes, and EK 4.2.B.1 makes the receptor the component that recognizes the external messenger."),

 dict(q="A cell responds to a signal by beginning to make a protein it was not making before. Which of the framework's listed responses is that?",
   choices=[
     "Gene expression",
     "Secretion of molecules",
     "Cell growth",
     "Recognition of the ligand",
     "Relay of the signal"],
   ans=0,
   why="EK 4.2.B.2 lists cell growth, secretion of molecules and gene expression as possible responses. Making a protein that was not previously made is the third of those; recognition and relay are earlier steps, not responses."),

 dict(q="Which statement about signal transduction is NOT supported by the framework?",
   choices=[
     "Every receptor protein is located in the plasma membrane of its target cell",
     "The ligand-binding domain recognizes a specific chemical messenger",
     "Cascades often amplify the incoming signal",
     "Cyclic AMP is an example of a second messenger",
     "Binding of a ligand can open or close a ligand-gated channel"],
   ans=0,
   why="EK 4.2.B.1.iii allows receptors on the surface or in the cytoplasm or nucleus, so a plasma membrane location is not universal. The other four restate EK 4.2.B.1.i, EK 4.2.B.2, EK 4.2.B.2.ii and EK 4.2.B.2.iv."),

 dict(q="Taken together, what are the components the framework assigns to a signal transduction pathway, from outside the cell inward?",
   choices=[
     "A chemical messenger, a receptor protein that recognizes it, a relaying and amplifying cascade, and a cellular response",
     "A cellular response, a relaying cascade, a receptor protein, and a chemical messenger produced last",
     "A receptor protein alone, since no other component is required",
     "A chemical messenger and a cellular response, with nothing between them",
     "A phosphorylation cascade that both recognizes the messenger and carries out the response"],
   ans=0,
   why="EK 4.2.B.1 gives the messenger and the receptor, EK 4.2.B.2 gives the relaying and often amplifying cascade and the response, and EK 4.2.A.1 states that the pathway links reception to response."),
]
