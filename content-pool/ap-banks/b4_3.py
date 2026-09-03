# AP BIOLOGY 4.3 Signal Transduction Pathways
# CED effective Fall 2025, Unit 4 Cell Communication and Cell Cycle.
# Big Idea 3 Information Storage and Transmission.
# Learning objectives 4.3.A (describe the different types of cellular responses
# elicited by a signal transduction pathway) and 4.3.B (explain how a change in
# the structure of any signaling molecule affects the activity of the signaling
# pathway). Suggested skill 6.C, provide reasoning to justify a claim by
# connecting evidence to biological theories.
#
# Essential knowledge, in the framework's own terms:
#   4.3.A.1  signal transduction may result in CHANGES IN GENE EXPRESSIONS AND
#            CELL FUNCTION, which may ALTER PHENOTYPE or result in PROGRAMMED
#            CELL DEATH (APOPTOSIS)
#   4.3.B.1  changes in signal transduction pathways can ALTER CELLULAR
#            RESPONSES; MUTATIONS IN ANY DOMAIN of the receptor protein OR IN
#            ANY COMPONENT of the signaling pathway may affect the DOWNSTREAM
#            components by altering the subsequent transduction of the signal
#   4.3.B.2  CHEMICALS that interact with ANY COMPONENT of the signaling pathway
#            may ACTIVATE OR INHIBIT the pathway
#
# The CED prints illustrative examples against both statements, and this module
# uses them as instances of the category rather than as facts of their own:
#   EK 4.3.A.1  chemical messengers used by microbes to communicate with other
#               nearby cells and to regulate specific pathways in response to
#               population density (quorum sensing); epinephrine stimulation of
#               glycogen breakdown in mammals
#   EK 4.3.B.1  cytokines regulating gene expression to allow cell replication
#               and division; mating pheromones in yeast triggering mating gene
#               expression; ethylene levels changing the production of different
#               enzymes and allowing fruits to ripen; HOX genes regulating
#               animal body plans during embryonic development
#
# QUORUM SENSING APPEARS IN TWO TOPICS AND IS ASKED TWO DIFFERENT WAYS. The CED
# lists it under EK 4.1.B.1 (short-distance communication by local regulators)
# and again under EK 4.3.A.1 (regulating SPECIFIC PATHWAYS in response to
# POPULATION DENSITY). Module b4_1 asks the first -- how far the signal travels
# -- and this module asks the second, what the pathway's output regulates.
# Neither key would answer the other question.
#
# BOUNDARY WITH 4.2, HELD DELIBERATELY. The components themselves -- ligand,
# ligand-binding domain, G protein-coupled receptors, receptor location,
# intracellular domain, second messengers, amplification, ligand-gated channels
# -- are essential knowledge of 4.2 and no key here merely names one. This
# module is about what a pathway PRODUCES and what happens when a pathway is
# CHANGED, which is what EK 4.3.A.1, EK 4.3.B.1 and EK 4.3.B.2 state and what
# skill 6.C asks a student to reason about.
#
# Tables are labelled HYPOTHETICAL and every keyed conclusion is recoverable
# from the table itself. No stem refers to a figure.
#
# FIVE choices (A-E). Plain prose, no LaTeX.
TOPIC = ("4.3", "Signal Transduction Pathways", 4)

_T_LINES = dict(
    headers=["Cell line (hypothetical)",
             "Ligand bound by the receptor (percent of normal)",
             "Relay component activated (percent of normal)",
             "Final response measured (percent of normal)"],
    rows=[["Normal cells", "100", "100", "100"],
          ["Line 1", "4", "3", "2"],
          ["Line 2", "98", "5", "3"],
          ["Line 3", "97", "96", "4"]])

_T_DRUG = dict(
    headers=["Treatment of the cells",
             "Ligand supplied (1 means yes, 0 means no)",
             "Response measured (hypothetical, arbitrary units)"],
    rows=[["No drug added", "0", "3"],
          ["No drug added", "1", "80"],
          ["Drug D added", "0", "76"],
          ["Drug E added", "1", "6"]])

_T_EXPRESSION = dict(
    headers=["Gene measured",
             "Expression without the signal (hypothetical, arbitrary units)",
             "Expression with the signal (hypothetical, arbitrary units)"],
    rows=[["Gene 1", "5", "140"],
          ["Gene 2", "90", "88"],
          ["Gene 3", "120", "6"]])

_T_APOPTOSIS = dict(
    headers=["Condition of the cell culture",
             "Cells still alive after two days (hypothetical, percent)",
             "Cells that underwent programmed cell death (hypothetical, percent)"],
    rows=[["Survival signal supplied", "96", "4"],
          ["Survival signal withheld", "29", "71"],
          ["Survival signal withheld, pathway switched on by a drug", "94", "6"]])

QUESTIONS = [
 dict(q="According to the framework, what may signal transduction result in within a cell?",
   choices=[
     "Changes in gene expression and in cell function",
     "Changes in the cell's genome sequence itself",
     "Replacement of the cell's plasma membrane",
     "Conversion of the cell into a cell of a different species",
     "Removal of every receptor the cell possesses"],
   ans=0,
   why="EK 4.3.A.1 states that signal transduction may result in changes in gene expressions and cell function. A change in what genes are expressed is not a change in the sequence of the genome."),

 dict(q="What two further outcomes does the framework say those changes may lead to?",
   choices=[
     "An altered phenotype, or programmed cell death",
     "An altered phenotype only, since a cell cannot be instructed to die",
     "Programmed cell death only, since phenotype is fixed at fertilization",
     "A change in the organism's species, or a change in its habitat",
     "An increase in the number of chromosomes, or a loss of the nucleus"],
   ans=0,
   why="EK 4.3.A.1 states that the changes in gene expression and cell function may alter phenotype or result in programmed cell death, which the framework names apoptosis."),

 dict(q="What does the framework mean by apoptosis?",
   choices=[
     "Programmed cell death",
     "Uncontrolled cell division",
     "The binding of a ligand to its receptor",
     "The amplification of a signal inside a cell",
     "The fusion of two cells into one"],
   ans=0,
   why="EK 4.3.A.1 names apoptosis in parentheses as programmed cell death, one of the outcomes signal transduction may produce."),

 dict(q="According to the framework, which parts of a receptor protein can carry a mutation that affects the pathway?",
   choices=[
     "Any domain of the receptor protein",
     "Only the ligand-binding domain",
     "Only the intracellular domain",
     "No domain, since receptor mutations have no effect",
     "Only a domain that lies outside the cell"],
   ans=0,
   why="EK 4.3.B.1 states that mutations in ANY DOMAIN of the receptor protein may affect the downstream components by altering the subsequent transduction of the signal."),

 dict(q="Beyond the receptor, where else does the framework say a mutation can change the transduction of a signal?",
   choices=[
     "In any component of the signaling pathway",
     "Only in the ligand released by the signaling cell",
     "Only in components that lie outside the target cell",
     "Nowhere, because only receptors matter to a pathway",
     "Only in the final response the cell produces"],
   ans=0,
   why="EK 4.3.B.1 states that mutations in any domain of the receptor protein OR IN ANY COMPONENT of the signaling pathway may affect the downstream components by altering the subsequent transduction of the signal."),

 dict(q="What does the framework say chemicals that interact with a component of a signaling pathway may do?",
   choices=[
     "Activate the pathway or inhibit it",
     "Activate the pathway but never inhibit it",
     "Inhibit the pathway but never activate it",
     "Convert the pathway into a different pathway entirely",
     "Have no effect, since only mutations can change a pathway"],
   ans=0,
   why="EK 4.3.B.2 states that chemicals that interact with any component of the signaling pathway may activate or inhibit the pathway. Both directions are named."),

 dict(q="Epinephrine acting in mammals stimulates the breakdown of stored glycogen. Which of the framework's categories does that illustrate?",
   choices=[
     "A signal transduction pathway producing a change in cell function",
     "A signal transduction pathway producing programmed cell death",
     "A mutation in a receptor protein altering transduction",
     "A chemical inhibiting a signaling pathway",
     "A receptor being synthesized in response to a ligand"],
   ans=0,
   why="The CED lists epinephrine stimulation of glycogen breakdown in mammals as an illustrative example of EK 4.3.A.1, which covers signal transduction resulting in changes in gene expression and cell function."),

 dict(q="Microbes release chemical messengers and, once the population is dense enough, switch on particular pathways. Which part of the framework does that illustrate?",
   choices=[
     "Signal transduction regulating specific pathways in response to population density",
     "A mutation in a receptor protein altering the transduction of a signal",
     "A chemical inhibiting the pathway of a neighboring cell",
     "Programmed cell death triggered by the loss of a signal",
     "A receptor changing its location from the surface to the nucleus"],
   ans=0,
   why="The CED lists the use of chemical messengers by microbes to regulate specific pathways in response to population density, quorum sensing, as an illustrative example of EK 4.3.A.1's account of the responses a pathway elicits."),

 dict(q="Cytokines act on cells to regulate gene expression in a way that permits cell replication and division. Which part of the framework does that illustrate?",
   choices=[
     "A signaling molecule whose pathway regulates gene expression",
     "A signaling molecule that acts without any receptor",
     "A mutation that removes a receptor's ligand-binding domain",
     "A chemical that inhibits every pathway it touches",
     "A pathway whose only possible output is programmed cell death"],
   ans=0,
   why="The CED lists cytokines regulating gene expression to allow for cell replication and division as an illustrative example under EK 4.3.B.1, and EK 4.3.A.1 makes changes in gene expression one of the results of signal transduction."),

 dict(q="Mating pheromones in yeast cause the expression of mating genes. Which of the framework's statements does that support?",
   choices=[
     "That signal transduction may result in changes in gene expression",
     "That signal transduction always results in programmed cell death",
     "That a signaling pathway can operate with no signaling molecule",
     "That gene expression cannot be changed by an external signal",
     "That only animals use signal transduction pathways"],
   ans=0,
   why="The CED lists mating pheromones in yeast triggering mating gene expression among the illustrative examples for EK 4.3.B.1, and EK 4.3.A.1 states that signal transduction may result in changes in gene expressions."),

 dict(q="Ethylene levels change which enzymes a plant produces, and fruits ripen as a result. Which of the framework's statements does that illustrate?",
   choices=[
     "That a signal can change gene expression and cell function, altering the phenotype",
     "That a signal can only act on cells of the same type that released it",
     "That signals act by physically breaking down the cells they reach",
     "That a signal must be a protein in order to change gene expression",
     "That ripening occurs independently of any signaling pathway"],
   ans=0,
   why="The CED lists ethylene levels causing changes in the production of different enzymes and allowing fruits to ripen among the illustrative examples for EK 4.3.B.1, and EK 4.3.A.1 makes altered phenotype one of the possible outcomes."),

 dict(q="HOX genes regulate animal body plans during embryonic development. Which part of the framework does that illustrate?",
   choices=[
     "Regulated gene expression shaping the phenotype of a developing organism",
     "A receptor protein binding a small molecule at the cell surface",
     "A chemical added from outside that inhibits a signaling pathway",
     "Programmed cell death removing every cell of an embryo",
     "A mutation that has no effect on any downstream component"],
   ans=0,
   why="The CED lists HOX genes regulating animal body plans during embryonic development among the illustrative examples for EK 4.3.B.1, and EK 4.3.A.1 makes an altered phenotype one of the outcomes of changed gene expression."),

 dict(q="Three mutant cell lines were compared with normal cells at three points along one pathway, with the results shown. Which line carries a defect at the receptor itself?",
   table=_T_LINES,
   choices=[
     "The line in which ligand binding is already reduced along with everything downstream",
     "The line in which ligand binding is normal but the relay component is not activated",
     "The line in which ligand binding and relay activation are both normal",
     "The normal cell line, since it shows full activity at every point",
     "None of the lines, since a receptor defect cannot be detected this way"],
   ans=0,
   why="EK 4.3.B.1 states that a mutation may affect the DOWNSTREAM components by altering the subsequent transduction of the signal, so the earliest step that departs from normal locates the lesion. Only one line fails at the binding step itself."),

 dict(q="Using the same three mutant lines, which line carries a defect downstream of the relay component?",
   table=_T_LINES,
   choices=[
     "The line in which ligand binding and relay activation are both normal but the response is not",
     "The line in which ligand binding is already reduced",
     "The line in which the relay component fails to be activated",
     "The normal cell line, since its response is unchanged",
     "None of the lines, because a downstream defect would also lower ligand binding"],
   ans=0,
   why="EK 4.3.B.1 makes a mutation affect the components DOWNSTREAM of it, leaving earlier steps intact, so a line with normal binding and normal relay but a failed response has its lesion after the relay."),

 dict(q="Cells were treated with two drugs and tested with and without the pathway's ligand, with the results shown. What do the data indicate about the two drugs?",
   table=_T_DRUG,
   choices=[
     "One drug activates the pathway without the ligand and the other inhibits it despite the ligand",
     "Both drugs activate the pathway without the ligand",
     "Both drugs inhibit the pathway despite the ligand",
     "Neither drug changes the response in any condition tested",
     "Both drugs act only when the ligand is also supplied"],
   ans=0,
   why="EK 4.3.B.2 states that chemicals interacting with any component of the signaling pathway may activate or inhibit the pathway. The table shows one of each against the untreated conditions."),

 dict(q="Expression of three genes was measured with and without a signal, with the results shown. Which conclusion is best supported?",
   table=_T_EXPRESSION,
   choices=[
     "The signal raises expression of one gene, lowers another, and leaves a third unchanged",
     "The signal raises expression of all three genes",
     "The signal lowers expression of all three genes",
     "The signal leaves all three genes unchanged",
     "The signal changes expression of every gene by the same amount"],
   ans=0,
   why="EK 4.3.A.1 states that signal transduction may result in changes in gene expressions, without requiring that every gene move in the same direction. The table shows one gene up, one down and one unmoved."),

 dict(q="Cells were cultured with a survival signal, without it, and without it but with a drug that switches the pathway on, with the results shown. Which conclusion is best supported?",
   table=_T_APOPTOSIS,
   choices=[
     "Losing the signal triggers programmed cell death, and switching the pathway on prevents it",
     "Losing the signal prevents programmed cell death",
     "Switching the pathway on triggers programmed cell death",
     "Programmed cell death occurs at the same rate in all three conditions",
     "Programmed cell death occurs only when the survival signal is supplied"],
   ans=0,
   why="EK 4.3.A.1 makes programmed cell death one of the outcomes signal transduction may produce, and EK 4.3.B.2 allows a chemical to activate a pathway. The drug substituting for the missing signal is what shows the pathway is what carries the effect."),

 dict(q="A mutation changes the ligand-binding domain of a receptor so that it no longer recognizes its messenger. What is the most reasonable prediction?",
   choices=[
     "The whole pathway downstream of the receptor is not activated by that messenger",
     "The pathway is activated more strongly than before",
     "Only the receptor is affected, and the response occurs normally",
     "The messenger is destroyed as soon as it reaches the cell",
     "The cell begins expressing the messenger instead of responding to it"],
   ans=0,
   why="EK 4.3.B.1 states that mutations in any domain of the receptor protein may affect the downstream components by altering the subsequent transduction of the signal. A signal never received cannot be transduced."),

 dict(q="A chemical is applied to cells and the pathway's response appears even though no messenger is present. What does the framework's account say has happened?",
   choices=[
     "The chemical has interacted with a component of the pathway and activated it",
     "The chemical has become a receptor for a messenger that is not there",
     "The chemical has inhibited the pathway, which is why a response appeared",
     "The chemical has removed the pathway from the cell entirely",
     "The chemical has caused the cell to synthesize the messenger outside itself"],
   ans=0,
   why="EK 4.3.B.2 states that chemicals interacting with any component of the signaling pathway may activate or inhibit the pathway. A response with no messenger present is the activating case."),

 dict(q="A chemical is applied to cells and the response disappears even though the messenger is present and still binds the receptor normally. Which explanation fits the framework?",
   choices=[
     "The chemical is inhibiting a component of the pathway downstream of the receptor",
     "The chemical is inhibiting the binding of the messenger to the receptor",
     "The chemical has mutated the gene encoding the receptor",
     "The chemical has become the pathway's messenger",
     "The chemical has increased the amount of messenger the cell receives"],
   ans=0,
   why="EK 4.3.B.2 allows a chemical to interact with ANY component of a pathway, and EK 4.3.B.1 makes a change at one point affect the components downstream of it. Binding that is still normal places the block after the receptor."),

 dict(q="An investigator wants to justify the claim that a drug acts on the receptor rather than further along the pathway. Which evidence would justify it?",
   choices=[
     "Ligand binding is reduced in treated cells while the pathway can still be switched on downstream of the receptor",
     "The response is reduced in treated cells, with nothing else measured",
     "The drug is a small molecule rather than a protein",
     "The drug is effective at low concentration",
     "The cells continue to grow normally while treated"],
   ans=0,
   why="Skill 6.C asks for reasoning that connects evidence to a claim. EK 4.3.B.1 makes a lesion affect everything downstream of it, so distinguishing a receptor lesion from a later one requires measuring at more than one point in the pathway."),

 dict(q="Cells that depend on a continuous survival signal lose that signal. Which outcome does the framework identify as possible?",
   choices=[
     "The cells undergo programmed cell death",
     "The cells become permanently unable to die",
     "The cells convert into cells of another tissue type",
     "The cells lose their genomes but continue functioning",
     "The cells begin producing the survival signal for other cells"],
   ans=0,
   why="EK 4.3.A.1 states that signal transduction may result in changes in gene expression and cell function which may alter phenotype or result in programmed cell death, which the framework names apoptosis."),

 dict(q="Two genetically identical plants are grown, and one is exposed to a ripening signal. The exposed plant's fruit softens and changes color while the other's does not. How does the framework describe this difference?",
   choices=[
     "A signal has changed gene expression and cell function, altering the phenotype",
     "A signal has changed the DNA sequence of the exposed plant",
     "A signal has caused programmed cell death throughout the exposed plant",
     "The two plants must differ in genotype after all",
     "The difference cannot involve signal transduction because the plants are identical"],
   ans=0,
   why="EK 4.3.A.1 states that signal transduction may result in changes in gene expressions and cell function, which may alter phenotype. Identical genotypes differing in phenotype after a signal is exactly that case."),

 dict(q="Why can a mutation in a component far along a pathway still change the cell's response, even though the receptor works perfectly?",
   choices=[
     "Because each component passes the signal to those downstream of it, so a break anywhere below the receptor stops the relay",
     "Because a mutation anywhere in a cell destroys all of its receptors",
     "Because the receptor cannot function unless every downstream component is intact",
     "Because the ligand is consumed by the downstream components",
     "Because a mutation changes the identity of the messenger outside the cell"],
   ans=0,
   why="EK 4.3.B.1 states that mutations in any component of the signaling pathway may affect the downstream components by altering the subsequent transduction of the signal, and EK 4.2.B.2 makes the cascade a relay from receptor to cell targets."),

 dict(q="How would an activating chemical and an inhibiting chemical be distinguished experimentally?",
   choices=[
     "By whether the response appears without the messenger or fails to appear with it",
     "By whether the chemical is larger or smaller than the messenger",
     "By whether the chemical is applied before or after the cells are counted",
     "By whether the chemical is dissolved in water or in another solvent",
     "By whether the cells are growing quickly or slowly at the time"],
   ans=0,
   why="EK 4.3.B.2 states that chemicals interacting with a pathway may activate or inhibit it, so the discriminating test is what the response does in the presence and absence of the messenger."),

 dict(q="An investigator argues that a single altered signaling pathway can change a whole visible trait of an organism. Which reasoning connects that claim to the framework?",
   choices=[
     "A pathway can change gene expression and cell function, and the framework names altered phenotype as a possible outcome",
     "A pathway can change the organism's DNA sequence, which changes the trait",
     "A pathway can only cause programmed cell death, which is not a visible trait",
     "A pathway acts on a single cell only, so a whole trait cannot be affected",
     "A trait can change only if every pathway in the organism is altered at once"],
   ans=0,
   why="Skill 6.C asks for reasoning connecting evidence to a theory. EK 4.3.A.1 supplies exactly that chain: transduction changes gene expression and cell function, and those changes may alter phenotype."),

 dict(q="A researcher wants to determine whether a cell's failure to respond is caused by a defective receptor or by a defective component further along. What comparison would settle it?",
   choices=[
     "Measuring both the binding of the messenger and the activity of a component downstream of the receptor",
     "Measuring only the final response of the cell",
     "Counting the number of cells present in each culture",
     "Comparing the size of the cells with and without the messenger",
     "Measuring how long the messenger takes to reach the cells"],
   ans=0,
   why="EK 4.3.B.1 makes a lesion affect the components downstream of it while leaving earlier steps intact, so only measurements at two or more points along the pathway can locate it. The final response alone is changed by a lesion anywhere."),

 dict(q="A mutation disables one component that lies at a point where a pathway divides into two branches, each leading to a different response. What is the most reasonable prediction?",
   choices=[
     "Both responses downstream of that component are affected",
     "Neither response is affected because the pathway branches",
     "Only the response reached by the shorter branch is affected",
     "The receptor loses the ability to bind its messenger",
     "The cell begins responding to a different messenger instead"],
   ans=0,
   why="EK 4.3.B.1 states that a mutation in any component may affect the DOWNSTREAM components by altering the subsequent transduction of the signal, and both branches lie downstream of the disabled component."),

 dict(q="Which statement about signal transduction pathways is NOT supported by the framework?",
   choices=[
     "Only a mutation in the ligand-binding domain of a receptor can change a cellular response",
     "Signal transduction may result in changes in gene expression",
     "Signal transduction may result in programmed cell death",
     "Chemicals may activate or inhibit a signaling pathway",
     "A mutation in a component of a pathway may affect components downstream of it"],
   ans=0,
   why="EK 4.3.B.1 extends the effect to mutations in ANY domain of the receptor and in ANY component of the pathway. The other four options restate EK 4.3.A.1, EK 4.3.A.1, EK 4.3.B.2 and EK 4.3.B.1 directly."),

 dict(q="Taken together, what do the framework's statements about signal transduction pathways assert?",
   choices=[
     "That a pathway's output can change gene expression, cell function, phenotype or survival, and that a change anywhere in the pathway can alter that output",
     "That a pathway's output is fixed and cannot be changed by mutation or by chemicals",
     "That only chemicals, and never mutations, can alter a pathway's output",
     "That only mutations, and never chemicals, can alter a pathway's output",
     "That a pathway's only possible output is programmed cell death"],
   ans=0,
   why="EK 4.3.A.1 gives the range of outputs, EK 4.3.B.1 makes a mutation anywhere in the pathway alter the downstream transduction, and EK 4.3.B.2 adds chemicals that may activate or inhibit it."),
]
