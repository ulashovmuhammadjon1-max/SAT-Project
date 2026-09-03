# AP BIOLOGY 4.1 Cell Communication
# CED effective Fall 2025, Unit 4 Cell Communication and Cell Cycle.
# Big Idea 3 Information Storage and Transmission.
# Learning objectives 4.1.A (describe the ways that cells can communicate with
# one another) and 4.1.B (explain how cells communicate with one another over
# short and long distances). Suggested skill 1.B, explain biological concepts
# and processes.
#
# Essential knowledge, in the framework's own terms:
#   4.1.A.1  Cells communicate with one another through DIRECT CONTACT with
#            other cells or FROM A DISTANCE via CHEMICAL SIGNALING.
#   4.1.B.1  Cells communicate over SHORT distances by using LOCAL REGULATORS
#            that target cells IN THE VICINITY of the signal-emitting cell.
#   4.1.B.2  Signals released by ONE CELL TYPE can travel LONG distances to
#            TARGET CELLS OF ANOTHER TYPE.
#
# The CED prints illustrative examples against two of these statements, and
# this module uses them as instances of the category rather than as facts of
# their own:
#   EK 4.1.A.1  immune cells interacting through cell-to-cell contact:
#               antigen-presenting cells (APCs), helper T-cells, killer T-cells
#   EK 4.1.B.1  neurotransmitters; plant immune response; quorum sensing in
#               bacteria; morphogens in embryonic development
#   EK 4.1.B.2  insulin; human growth hormone; thyroid hormones; testosterone;
#               estrogen
# Every key that names an example is keyed to WHICH CATEGORY the CED lists it
# under, never to a mechanism the CED does not print for it.
#
# BOUNDARY WITH 4.2 AND 4.3, HELD DELIBERATELY. Ligands, receptors, the
# ligand-binding domain, G protein-coupled receptors, phosphorylation cascades,
# second messengers such as cyclic AMP, amplification and ligand-gated channels
# are all essential knowledge of topic 4.2, and gene expression changes,
# apoptosis, mutations in pathway components and activating or inhibiting
# chemicals are essential knowledge of topic 4.3. No key in this module rests
# on any of them. What is left to 4.1 is the MODE of communication -- contact
# against chemical -- and the DISTANCE it covers.
#
# Tables are labelled HYPOTHETICAL and every keyed conclusion is recoverable
# from the table itself. No stem refers to a figure.
#
# FIVE choices (A-E). Plain prose, no LaTeX.
TOPIC = ("4.1", "Cell Communication", 4)

_T_DISTANCE = dict(
    headers=["Distance from the releasing cell (micrometers)",
             "Concentration of local regulator R (hypothetical, nanomolar)",
             "Concentration of circulating signal H (hypothetical, nanomolar)"],
    rows=[["10", "40", "5"],
          ["100", "9", "5"],
          ["1,000", "1", "5"],
          ["10,000", "0", "5"]])

_T_TARGET = dict(
    headers=["Cell type exposed to both signals",
             "Response to signal S (hypothetical, arbitrary units)",
             "Response to signal T (hypothetical, arbitrary units)"],
    rows=[["Liver cell", "62", "0"],
          ["Muscle cell", "55", "0"],
          ["Nerve cell", "2", "48"],
          ["Skin cell", "1", "0"]])

_T_CONTACT = dict(
    headers=["Arrangement of the two immune cell populations",
             "Cell-to-cell contacts counted per field",
             "Response measured (hypothetical, arbitrary units)"],
    rows=[["Populations mixed freely", "85", "70"],
          ["Populations separated by a filter that blocks cells but passes molecules", "0", "4"],
          ["Populations mixed with an agent that prevents cells from touching", "6", "8"]])

QUESTIONS = [
 dict(q="According to the framework, what are the two ways cells communicate with one another?",
   choices=[
     "Through direct contact with other cells, or from a distance by chemical signaling",
     "Through direct contact only, since chemical signals cannot leave a cell",
     "By chemical signaling only, since cells never touch one another",
     "By exchanging whole organelles or by exchanging whole chromosomes",
     "By altering the temperature or the pH of the surrounding tissue"],
   ans=0,
   why="EK 4.1.A.1 states that cells communicate with one another through direct contact with other cells or from a distance via chemical signaling. Those two routes are the whole of the statement."),

 dict(q="What does the framework call the molecules cells use to communicate over short distances, and which cells do those molecules act on?",
   choices=[
     "Local regulators, which target cells in the vicinity of the signal-emitting cell",
     "Local regulators, which target cells throughout the whole organism",
     "Circulating hormones, which target cells in the vicinity of the signal-emitting cell",
     "Structural proteins, which hold neighboring cells physically together",
     "Digestive enzymes, which break down the cells nearest the source"],
   ans=0,
   why="EK 4.1.B.1 states that cells communicate over short distances by using local regulators that target cells in the vicinity of the signal-emitting cell. Both the name and the range are given in that sentence."),

 dict(q="What does the framework say about signals that travel long distances?",
   choices=[
     "Signals released by one cell type can travel long distances to target cells of another type",
     "Signals released by one cell type can travel long distances only to cells of the same type",
     "Long-distance signals act on every cell they reach without exception",
     "Long-distance signals must be delivered by direct contact between cells",
     "No signal can travel further than the cells immediately adjacent to its source"],
   ans=0,
   why="EK 4.1.B.2 states that signals released by one cell type can travel long distances to target cells of another type. Both the crossing of cell types and the distance are part of that statement."),

 dict(q="A neurotransmitter released by one nerve cell acts on a cell immediately across a narrow gap. Under which of the framework's categories does that fall?",
   choices=[
     "Communication over a short distance using a local regulator",
     "Communication over a long distance using a circulating signal",
     "Communication by direct physical contact between the two cells",
     "Communication by the exchange of genetic material",
     "Communication that requires no signal molecule at all"],
   ans=0,
   why="The CED lists neurotransmitters as an illustrative example of EK 4.1.B.1, which covers communication over short distances by local regulators that target cells in the vicinity of the signal-emitting cell."),

 dict(q="Insulin is released by cells of one tissue and acts on cells of other tissues elsewhere in the body. Under which of the framework's categories does that fall?",
   choices=[
     "Communication over a long distance to target cells of another type",
     "Communication over a short distance by a local regulator",
     "Communication by direct physical contact between the two cells",
     "Communication that occurs only within a single cell",
     "Communication that requires the two cells to be touching"],
   ans=0,
   why="The CED lists insulin as an illustrative example of EK 4.1.B.2, which covers signals released by one cell type that travel long distances to target cells of another type."),

 dict(q="An antigen-presenting cell and a helper T-cell interact by touching one another. Under which of the framework's categories does that interaction fall?",
   choices=[
     "Communication through direct contact between cells",
     "Communication over a short distance using a local regulator",
     "Communication over a long distance using a circulating signal",
     "Communication that requires no interaction between the two cells",
     "Communication carried out entirely inside one of the two cells"],
   ans=0,
   why="The CED lists immune cells interacting through cell-to-cell contact, naming antigen-presenting cells, helper T-cells and killer T-cells, as an illustrative example of EK 4.1.A.1's direct-contact route."),

 dict(q="Bacteria release a molecule that accumulates as the population grows, and the bacteria alter their behavior once enough of it is present nearby. Which of the framework's categories does this illustrate?",
   choices=[
     "Short-distance communication in which a released molecule acts on cells in the vicinity",
     "Long-distance communication in which a hormone reaches a distant organ",
     "Direct contact communication in which the cells must be touching",
     "Communication in which no molecule is released by any cell",
     "Communication that occurs only between cells of two different species"],
   ans=0,
   why="The CED lists quorum sensing in bacteria as an illustrative example of EK 4.1.B.1, which covers short-distance communication by local regulators targeting cells in the vicinity of the signal-emitting cell."),

 dict(q="During embryonic development, a molecule released from one region acts on nearby cells and helps determine what those cells become. Which of the framework's categories does this illustrate?",
   choices=[
     "Short-distance communication by a molecule acting on cells near its source",
     "Long-distance communication by a molecule carried to a distant organ",
     "Direct contact communication requiring the cells to touch",
     "Communication in which the responding cells release the molecule themselves",
     "Communication that requires no released molecule at all"],
   ans=0,
   why="The CED lists morphogens in embryonic development as an illustrative example of EK 4.1.B.1, which covers communication over short distances by local regulators targeting cells in the vicinity."),

 dict(q="A plant attacked at one leaf releases molecules that prepare neighboring cells to resist the attacker. Which of the framework's categories does this illustrate?",
   choices=[
     "Short-distance communication by molecules acting on cells near the source",
     "Direct contact communication in which the attacked cell touches each neighbor",
     "Long-distance communication in which the molecule crosses to another organism",
     "Communication that requires an animal nervous system",
     "Communication in which no molecule leaves the attacked cell"],
   ans=0,
   why="The CED lists the plant immune response as an illustrative example of EK 4.1.B.1, which covers short-distance communication by local regulators that target cells in the vicinity of the signal-emitting cell."),

 dict(q="Thyroid hormones are released by one gland and act on cells throughout the body. Which of the framework's categories does that illustrate?",
   choices=[
     "Long-distance communication reaching target cells of another type",
     "Short-distance communication by a local regulator",
     "Direct contact between the gland and every responding cell",
     "Communication that occurs only among cells of the gland itself",
     "Communication that does not involve a released molecule"],
   ans=0,
   why="The CED lists thyroid hormones as an illustrative example of EK 4.1.B.2, which covers signals released by one cell type travelling long distances to target cells of another type."),

 dict(q="Which pair below sets one of the framework's long-distance signals beside one of its short-distance local regulators?",
   choices=[
     "Estrogen and neurotransmitters",
     "Insulin and thyroid hormones",
     "Neurotransmitters and morphogens",
     "Testosterone and human growth hormone",
     "Quorum sensing molecules and the plant immune response"],
   ans=0,
   why="The CED lists estrogen among the illustrative examples of EK 4.1.B.2, long-distance signals reaching target cells of another type, and neurotransmitters among those of EK 4.1.B.1, local regulators acting on cells in the vicinity. Each of the other four pairs draws both of its members from the same one of those two lists."),

 dict(q="Human growth hormone is released by cells in one part of the body and produces effects in tissues far from its source. Which statement about it follows from the framework?",
   choices=[
     "It is a long-distance signal reaching target cells of another type",
     "It is a local regulator restricted to the vicinity of its source",
     "It acts only on the cells that released it",
     "It acts only when the releasing and responding cells are touching",
     "It acts on every cell in the body without distinction"],
   ans=0,
   why="The CED lists human growth hormone among the illustrative examples of EK 4.1.B.2, which covers signals released by one cell type that travel long distances to target cells of another type."),

 dict(q="Killer T-cells act on the cells they destroy by touching them. Which of the framework's two communication routes does that use?",
   choices=[
     "Direct contact with other cells",
     "Chemical signaling over a long distance",
     "Chemical signaling over a short distance",
     "Neither route, because destroying a cell is not communication",
     "Both routes at once, since contact requires a circulating hormone"],
   ans=0,
   why="The CED lists killer T-cells among the immune cells that interact through cell-to-cell contact, its illustrative example of the direct-contact route named in EK 4.1.A.1."),

 dict(q="What is the essential difference between the two kinds of chemical signaling the framework distinguishes?",
   choices=[
     "How far the signal travels before it reaches the cells it acts on",
     "Whether the signal is a molecule or a physical force",
     "Whether the releasing cell is alive at the time of release",
     "Whether the signal is released inside or outside an organelle",
     "Whether the responding cell is larger or smaller than the releasing cell"],
   ans=0,
   why="EK 4.1.B.1 and EK 4.1.B.2 are distinguished by range: local regulators act on cells in the vicinity of the signal-emitting cell, while long-distance signals travel to target cells of another type elsewhere."),

 dict(q="Concentrations of two signal molecules were measured at increasing distances from a releasing cell, with the results shown. Which molecule is behaving as a local regulator?",
   table=_T_DISTANCE,
   choices=[
     "The molecule whose concentration falls sharply with distance from the releasing cell",
     "The molecule whose concentration is the same at every distance measured",
     "The molecule present at the lowest concentration nearest the releasing cell",
     "Both molecules equally, since both were detected near the releasing cell",
     "Neither molecule, since a local regulator cannot be measured"],
   ans=0,
   why="EK 4.1.B.1 defines a local regulator as targeting cells in the vicinity of the signal-emitting cell, so its concentration must be high near the source and negligible away from it. Only one of the two columns behaves that way."),

 dict(q="Using the same concentration measurements, which molecule is behaving as a long-distance signal?",
   table=_T_DISTANCE,
   choices=[
     "The molecule held at the same concentration at every distance measured",
     "The molecule whose concentration falls to zero far from the releasing cell",
     "The molecule at the highest concentration closest to the releasing cell",
     "Neither molecule, since long distances were not tested",
     "Both molecules, since both were detected somewhere in the measurements"],
   ans=0,
   why="EK 4.1.B.2 describes signals that travel long distances to target cells of another type, which requires the signal to be present far from its source. Only one of the two columns holds its concentration across the full range measured."),

 dict(q="Four cell types were exposed to the same two signals, with the results shown. Which conclusion is best supported?",
   table=_T_TARGET,
   choices=[
     "Each signal produces a response in some cell types and not in others",
     "Each signal produces a response in every cell type exposed to it",
     "Neither signal produces a response in any cell type",
     "The two signals produce a response in exactly the same cell types",
     "Only the cell type that released each signal responds to it"],
   ans=0,
   why="EK 4.1.B.2 describes signals travelling to TARGET cells of another type, which implies that some exposed cells are targets and others are not. The table shows each signal acting on a different subset of the four cell types."),

 dict(q="Two immune cell populations were combined in three arrangements and the response was measured, with the results shown. What do the data indicate about the communication involved?",
   table=_T_CONTACT,
   choices=[
     "A strong response requires the cells to touch, since arrangements that prevent contact give little response",
     "A strong response occurs whenever molecules can pass between the populations, whether or not the cells touch",
     "A strong response occurs only when the cells are kept apart by a filter",
     "The response is the same in all three arrangements",
     "The response is greatest in the arrangement with the fewest cell-to-cell contacts"],
   ans=0,
   why="EK 4.1.A.1 names direct contact as one of the two communication routes, and the CED's illustrative example is immune cells interacting through cell-to-cell contact. A filter that passes molecules but blocks cells separates the two routes."),

 dict(q="An agent is added that prevents an antigen-presenting cell from touching a helper T-cell but does not affect either cell otherwise. What is the most reasonable prediction?",
   choices=[
     "The interaction that depends on direct contact does not occur",
     "The interaction occurs normally, because contact is not required for it",
     "The two cells begin communicating by releasing a hormone instead",
     "Both cells are destroyed immediately by the loss of contact",
     "The interaction becomes stronger because the cells are free to move"],
   ans=0,
   why="EK 4.1.A.1 makes direct contact one of the two routes of cell communication, and the CED's illustrative example places this immune interaction in that route. Removing contact removes the route the interaction uses."),

 dict(q="The same signal molecule is released by a cell into a narrow space between two cells in one tissue and into the circulation in another tissue. What difference does the framework's account predict?",
   choices=[
     "In one case it acts on cells in the vicinity and in the other it can reach cells far away",
     "In both cases it can act only on cells in the vicinity",
     "In both cases it can act only on cells far away",
     "In neither case can it act on any cell, since a molecule cannot serve two roles",
     "In one case it acts by direct contact and in the other by direct contact as well"],
   ans=0,
   why="EK 4.1.B.1 and EK 4.1.B.2 are statements about how far a released signal travels, not about the identity of the molecule, so where a signal is released determines the range over which it can act."),

 dict(q="Why does chemical signaling allow cells to communicate that could never communicate by the other route the framework names?",
   choices=[
     "A released molecule can cross a space, while direct contact requires the cells to meet",
     "A released molecule carries no information, while direct contact does",
     "A released molecule can act only on the cell that released it",
     "Direct contact can occur across any distance at all",
     "Direct contact is the only route available to cells of different types"],
   ans=0,
   why="EK 4.1.A.1 separates communication through direct contact from communication FROM A DISTANCE via chemical signaling, and EK 4.1.B.2 extends the second route to target cells of another type far from the source."),

 dict(q="An investigator claims that a newly identified molecule is a local regulator rather than a long-distance signal. Which finding would best support that claim?",
   choices=[
     "The molecule is detectable only within a short distance of the cells that release it",
     "The molecule is a protein rather than a small molecule",
     "The molecule is released in large amounts by many kinds of cell",
     "The molecule produces a strong effect on the cells it acts on",
     "The molecule is produced continuously rather than in bursts"],
   ans=0,
   why="EK 4.1.B.1 defines a local regulator by its range, targeting cells in the vicinity of the signal-emitting cell. Only a measurement of range distinguishes it from EK 4.1.B.2's long-distance signal; size, amount and potency do not."),

 dict(q="Cells in one region of a developing embryo become different from cells in a neighboring region even though both began alike. Which of the framework's routes best accounts for this?",
   choices=[
     "A molecule released nearby reaches one region strongly and the other weakly",
     "A hormone in the circulation reaches both regions at exactly the same concentration",
     "The two regions are physically identical and no communication occurred",
     "Each cell decided independently with no signal from any other cell",
     "The two regions exchanged whole chromosomes with one another"],
   ans=0,
   why="EK 4.1.B.1 gives short-distance communication by local regulators targeting cells in the vicinity of the source, and the CED lists morphogens in embryonic development as its illustrative example. A signal at equal concentration everywhere could not distinguish two regions."),

 dict(q="Which statement about cell communication is NOT supported by the framework?",
   choices=[
     "Every signal a cell releases reaches every other cell in the organism",
     "Cells can communicate through direct contact with other cells",
     "Local regulators target cells in the vicinity of the signal-emitting cell",
     "Some signals travel long distances to target cells of another type",
     "Chemical signaling allows communication between cells that are not touching"],
   ans=0,
   why="EK 4.1.B.1 confines local regulators to the vicinity of the emitting cell and EK 4.1.B.2 speaks of TARGET cells, so no statement in the framework makes every signal universal. The other four restate EK 4.1.A.1, EK 4.1.B.1 and EK 4.1.B.2."),

 dict(q="Which arrangement is an example of the direct contact route rather than the chemical signaling route?",
   choices=[
     "Two immune cells that must touch one another for the interaction to occur",
     "A gland releasing a hormone that travels through the circulation",
     "A nerve cell releasing a molecule into a narrow gap next to another cell",
     "A bacterium releasing a molecule that accumulates as its population grows",
     "A plant cell releasing molecules that prepare neighboring cells for attack"],
   ans=0,
   why="EK 4.1.A.1 separates direct contact from chemical signaling, and the CED's illustrative example of contact is immune cells interacting cell-to-cell. The other four options are all illustrative examples of the chemical route, in EK 4.1.B.1 or EK 4.1.B.2."),

 dict(q="A hormone released by cells in one organ produces an effect in a different organ. Which parts of the framework's description does that scenario satisfy?",
   choices=[
     "A signal released by one cell type travelling a long distance to target cells of another type",
     "A local regulator acting on cells in the vicinity of the releasing cell",
     "Direct contact between the cells of the two organs",
     "A signal acting only on cells identical to the ones that released it",
     "A signal that acts without ever leaving the releasing cell"],
   ans=0,
   why="EK 4.1.B.2 states that signals released by one cell type can travel long distances to target cells of another type, which names both features of the scenario: the crossing of cell types and the distance."),

 dict(q="Two tissues are separated by a barrier that molecules can cross but cells cannot. Which kinds of communication remain possible between them?",
   choices=[
     "Chemical signaling remains possible while direct contact does not",
     "Direct contact remains possible while chemical signaling does not",
     "Both kinds remain possible because the barrier is permeable",
     "Neither kind remains possible because the tissues are separated",
     "Only communication between cells of the same type remains possible"],
   ans=0,
   why="EK 4.1.A.1 names two routes, direct contact and chemical signaling from a distance. A barrier that passes molecules but not cells removes exactly one of the two."),

 dict(q="Why does the framework describe long-distance signals as acting on target cells rather than simply on distant cells?",
   choices=[
     "Because a signal that reaches many cells produces its effect in only some of them",
     "Because a signal reaches only one cell in the entire organism",
     "Because distant cells are all of the same type as the releasing cell",
     "Because a signal loses its identity as it travels and becomes a different molecule",
     "Because the responding cells travel to meet the signal at its source"],
   ans=0,
   why="EK 4.1.B.2 says signals travel to TARGET cells of another type, a phrase that distinguishes the cells that respond from the cells a circulating signal merely passes. Being reached and being a target are not the same thing."),

 dict(q="A researcher wants to determine whether a response between two cell populations requires contact. Which comparison would settle it?",
   choices=[
     "Mixed populations against populations separated by a barrier that passes molecules but not cells",
     "Mixed populations against populations kept in separate flasks with no shared medium",
     "One population alone against the other population alone",
     "Mixed populations at two different temperatures",
     "Mixed populations measured after two different lengths of time"],
   ans=0,
   why="EK 4.1.A.1 names contact and chemical signaling as the two routes, so a design that removes contact while leaving molecular exchange intact isolates one route. Separate flasks remove both routes at once and settle nothing."),

 dict(q="Taken together, how does the framework organize the ways cells communicate?",
   choices=[
     "By whether the cells touch, and if they do not, by how far the released signal travels",
     "By whether the cells belong to the same organism, and if they do, by their size",
     "By whether the signal is a protein, and if it is, by how quickly it is made",
     "By whether the responding cell divides afterward, and if it does, by how often",
     "By whether the cells are prokaryotic, since eukaryotes do not communicate"],
   ans=0,
   why="EK 4.1.A.1 draws the first distinction between direct contact and chemical signaling from a distance, and EK 4.1.B.1 and EK 4.1.B.2 divide the chemical route by range into local regulators and long-distance signals."),
]
