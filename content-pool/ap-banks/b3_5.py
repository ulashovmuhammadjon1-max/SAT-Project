# AP BIOLOGY 3.5 Cellular Respiration
# CED effective Fall 2025, Unit 3 Cellular Energetics. Big Idea 2 Energetics.
# Learning objectives 3.5.A (describe the processes and structural features of
# mitochondria that allow organisms to use energy stored in biological
# macromolecules) and 3.5.B (explain how cells obtain energy from biological
# macromolecules in order to power cellular functions).
# Suggested skill 4.A, construct a graph to represent data. The bank cannot
# carry a graph, so every data item here is a TABLE and asks the skill 4.B
# question of it -- identify data points, describe trends, describe
# relationships between variables -- which is what the graphing skill is for.
#
# Essential knowledge, in the framework's own terms:
#   3.5.A.1     cellular respiration uses energy from BIOLOGICAL MACROMOLECULES
#               to synthesize ATP; respiration and fermentation are
#               characteristic of ALL FORMS OF LIFE
#   3.5.A.2     aerobic cellular respiration in eukaryotes is a series of
#               COORDINATED ENZYME-CATALYZED REACTIONS
#   3.5.A.3     the ETC transfers electrons in a series of OXIDATION-REDUCTION
#               reactions that establish an ELECTROCHEMICAL GRADIENT across
#               membranes
#     i.        electrons delivered by NADH and FADH2 move toward the TERMINAL
#               ELECTRON ACCEPTOR, OXYGEN; aerobic prokaryotes use oxygen,
#               ANAEROBIC prokaryotes use OTHER MOLECULES
#     ii.       the gradient runs HIGH OUTSIDE the inner mitochondrial membrane
#               and LOW INSIDE it; FOLDING of the inner membrane INCREASES
#               SURFACE AREA, allowing more ATP to be synthesized; in
#               prokaryotes protons move across the PLASMA MEMBRANE
#     iii.      proton flow back through membrane-bound ATP SYNTHASE by
#               CHEMIOSMOSIS drives ATP formation; this is OXIDATIVE
#               PHOSPHORYLATION
#     iv.       DECOUPLING oxidative phosphorylation from electron transport
#               GENERATES HEAT, which ENDOTHERMIC organisms can use to regulate
#               body temperature
#   3.5.B.1     GLYCOLYSIS releases the energy in glucose to form ATP, NADH and
#               PYRUVATE
#   3.5.B.2     pyruvate is transported FROM THE CYTOSOL TO THE MITOCHONDRION;
#               the Krebs (citric acid) cycle reduces NAD+ to NADH and FAD to
#               FADH2 and releases CARBON DIOXIDE
#   3.5.B.3     the Krebs cycle takes place in the MITOCHONDRIAL MATRIX
#   3.5.B.4     electrons extracted in glycolysis and the Krebs cycle are
#               carried by NADH and FADH2 to the ETC in the INNER MITOCHONDRIAL
#               MEMBRANE
#   3.5.B.5     the pH inside the MITOCHONDRIAL MATRIX is HIGHER than in the
#               INTERMEMBRANE SPACE
#   3.5.B.6     FERMENTATION allows glycolysis to proceed IN THE ABSENCE OF
#               OXYGEN and produces organic molecules such as ALCOHOL and
#               LACTIC ACID
#
# EXCLUSION STATEMENTS OBSERVED. The CED puts beyond scope: memorization of the
# steps of glycolysis and the Krebs cycle, the structures of the molecules and
# the names of the enzymes involved; the full names of the specific electron
# carriers; and the specific steps and intermediates of these pathways. No item
# asks for any of them. ATP synthase is named because EK 3.5.A.3.iii names it
# and the parallel exclusion in topic 3.4 exempts it explicitly.
#
# BOUNDARY WITH 3.4, HELD DELIBERATELY. Both topics carry an electron transport
# chain, a proton gradient, ATP synthase and chemiosmosis. Every item here is
# mitochondrion-specific: the gradient runs the OPPOSITE way (high OUTSIDE the
# inner membrane), the phosphorylation is OXIDATIVE rather than photo-, the
# terminal acceptor is OXYGEN, and glycolysis, pyruvate, the Krebs cycle, the
# matrix, cristae folding, decoupling to heat and fermentation have no
# counterpart in 3.4. The surface-area item is deliberately about the FOLDING
# named in EK 3.5.A.3.ii rather than about compartmentalization, which is
# topic 2.9.
#
# NO FIGURES ANYWHERE. No stem refers to a graph or a diagram; data questions
# carry a table and ask the question of the table.
#
# FIVE choices (A-E). Plain prose, no LaTeX.
TOPIC = ("3.5", "Cellular Respiration", 3)

_T_MITO = dict(
    headers=["Addition to the mitochondrial suspension",
             "Oxygen consumed (hypothetical, micromoles per minute)",
             "ATP formed (hypothetical, micromoles per minute)"],
    rows=[["No addition", "20", "55"],
          ["Agent X added", "1", "3"],
          ["Agent Y added", "34", "4"]])

_T_YEAST = dict(
    headers=["Yeast culture condition",
             "Glucose consumed (hypothetical, millimoles)",
             "Carbon dioxide released (hypothetical, millimoles)",
             "Ethanol produced (hypothetical, millimoles)"],
    rows=[["Oxygen supplied throughout", "10", "60", "0"],
          ["No oxygen supplied", "10", "20", "20"]])

_T_PH = dict(
    headers=["Region of the mitochondrion",
             "pH while electron transport is running (hypothetical)",
             "pH after electron transport is blocked (hypothetical)"],
    rows=[["Matrix", "8.0", "7.4"],
          ["Intermembrane space", "7.0", "7.4"]])

QUESTIONS = [
 dict(q="What does the framework say cellular respiration accomplishes for a cell?",
   choices=[
     "It uses energy from biological macromolecules to synthesize ATP",
     "It uses energy from ATP to synthesize biological macromolecules",
     "It uses light energy to synthesize carbohydrates from carbon dioxide",
     "It removes the cell's requirement for an input of energy",
     "It converts ATP directly into heat with no other product"],
   ans=0,
   why="EK 3.5.A.1 states that cellular respiration uses energy from biological macromolecules to synthesize ATP. The reverse direction and the light-driven synthesis belong to other processes in the framework."),

 dict(q="How widely distributed among living things does the framework say respiration and fermentation are?",
   choices=[
     "They are characteristic of all forms of life",
     "They are found only in eukaryotes",
     "They are found only in prokaryotes",
     "They are found only in organisms that lack chloroplasts",
     "They are found only in organisms living without oxygen"],
   ans=0,
   why="EK 3.5.A.1 states that respiration and fermentation are characteristic of all forms of life. That universality is the same kind of observation EK 3.3.B.1 makes about conserved core metabolic pathways."),

 dict(q="How does the framework characterize aerobic cellular respiration in eukaryotes?",
   choices=[
     "As a series of coordinated enzyme-catalyzed reactions that capture energy from biological macromolecules",
     "As a single uncatalyzed reaction that releases all the energy at once",
     "As a process that requires no enzymes because oxygen is present",
     "As a process confined to the cytosol of the cell",
     "As a process that consumes ATP rather than producing it"],
   ans=0,
   why="EK 3.5.A.2 states that aerobic cellular respiration in eukaryotes involves a series of coordinated enzyme-catalyzed reactions that capture energy from biological macromolecules, which is also why EK 3.3.A.3 calls energy pathways sequential."),

 dict(q="What kind of reactions does the electron transport chain carry out, and what do they establish?",
   choices=[
     "A series of oxidation and reduction reactions that establish an electrochemical gradient across a membrane",
     "A series of hydrolysis reactions that break macromolecules into their subunits",
     "A single reaction that converts glucose directly into carbon dioxide",
     "A series of reactions that build carbohydrate from carbon dioxide",
     "A series of reactions that eliminate any concentration difference across a membrane"],
   ans=0,
   why="EK 3.5.A.3 states that the ETC transfers electrons in a series of oxidation-reduction reactions that establish an electrochemical gradient across membranes."),

 dict(q="In aerobic cellular respiration, which molecule is the terminal electron acceptor?",
   choices=[
     "Oxygen",
     "Carbon dioxide",
     "Water",
     "Glucose",
     "Pyruvate"],
   ans=0,
   why="EK 3.5.A.3.i states that electrons delivered by NADH and FADH2 are passed to a series of electron acceptors as they move toward the terminal electron acceptor, oxygen."),

 dict(q="What does the framework say about anaerobic prokaryotes and the end of their electron transport chain?",
   choices=[
     "They use molecules other than oxygen as the terminal electron acceptor",
     "They have no electron transport chain of any kind",
     "They use oxygen but at a much lower concentration than aerobic prokaryotes",
     "They pass their electrons back to the macromolecules the electrons came from",
     "They release their electrons directly into the surrounding medium"],
   ans=0,
   why="EK 3.5.A.3.i states that aerobic prokaryotes use oxygen as a terminal electron acceptor while anaerobic prokaryotes use other molecules. The chain itself is not what they lack."),

 dict(q="Which molecules does the framework name as delivering electrons to the electron transport chain in cellular respiration?",
   choices=[
     "NADH and FADH2",
     "ATP and ADP",
     "NADPH and ATP",
     "Pyruvate and carbon dioxide",
     "Oxygen and water"],
   ans=0,
   why="EK 3.5.A.3.i and EK 3.5.B.4 both name NADH and FADH2 as the carriers that deliver electrons extracted in glycolysis and the Krebs cycle to the electron transport chain. NADPH belongs to photosynthesis under EK 3.4.B.1."),

 dict(q="Where is the proton concentration higher once the electron transport chain has been running in a mitochondrion?",
   choices=[
     "Outside the inner mitochondrial membrane",
     "Inside the inner mitochondrial membrane, in the matrix",
     "In the cytosol surrounding the whole mitochondrion",
     "Equally in both regions, since protons distribute evenly",
     "Inside the thylakoid of the nearest chloroplast"],
   ans=0,
   why="EK 3.5.A.3.ii states that the membrane separates a region of high proton concentration outside the membrane from a region of low proton concentration inside it. This is the opposite sense to the thylakoid gradient of EK 3.4.B.4."),

 dict(q="How do the pH values of the mitochondrial matrix and the intermembrane space compare while electron transport is running?",
   choices=[
     "The pH in the matrix is higher than the pH in the intermembrane space",
     "The pH in the matrix is lower than the pH in the intermembrane space",
     "The two regions have identical pH values at all times",
     "The pH in the matrix is higher only when electron transport has stopped",
     "Neither region has a measurable pH because both are enclosed"],
   ans=0,
   why="EK 3.5.B.5 states that the pH inside the mitochondrial matrix is higher than in the intermembrane space. That is the same fact as EK 3.5.A.3.ii's gradient, since more protons means lower pH."),

 dict(q="What consequence does the framework attach to the folding of the inner mitochondrial membrane?",
   choices=[
     "The increased surface area allows more ATP to be synthesized",
     "The folds make the membrane impermeable to protons",
     "The folds allow the mitochondrion to take in glucose directly",
     "The folds reduce the number of electron transport proteins needed",
     "The folds convert the matrix into a second intermembrane space"],
   ans=0,
   why="EK 3.5.A.3.ii states that the folding of the inner membrane increases the surface area, which allows for more ATP to be synthesized. The statement ties the structural feature directly to the yield."),

 dict(q="In prokaryotes, across which membrane does the passage of electrons move protons?",
   choices=[
     "The plasma membrane",
     "The inner mitochondrial membrane",
     "The thylakoid membrane",
     "The nuclear envelope",
     "The membrane of a lysosome"],
   ans=0,
   why="EK 3.5.A.3.ii states that in prokaryotes the passage of electrons is accompanied by the movement of protons across the plasma membrane. Prokaryotes typically lack the internal membrane-bound organelles named in the other options, per EK 2.10.A.2."),

 dict(q="What name does the framework give to the formation of ATP driven by protons flowing back through ATP synthase in aerobic cellular respiration?",
   choices=[
     "Oxidative phosphorylation",
     "Photophosphorylation",
     "Fermentation",
     "Carbon fixation",
     "Denaturation"],
   ans=0,
   why="EK 3.5.A.3.iii states that the flow of protons back through membrane-bound ATP synthase by chemiosmosis drives the formation of ATP from ADP and inorganic phosphate, and that this is known as oxidative phosphorylation in aerobic cellular respiration."),

 dict(q="What does the framework say results from decoupling oxidative phosphorylation from electron transport, and what use is made of it?",
   choices=[
     "Heat is generated, and endothermic organisms can use it to regulate body temperature",
     "Additional ATP is generated, and organisms use it to power growth",
     "Oxygen is generated, and organisms release it to the surroundings",
     "Glucose is generated, and organisms store it for later use",
     "Nothing is generated, because the two processes cannot be separated"],
   ans=0,
   why="EK 3.5.A.3.iv states that in aerobic cellular respiration, decoupling oxidative phosphorylation from electron transport generates heat, and that this heat can be used by endothermic organisms to regulate body temperature."),

 dict(q="Which three products does the framework say glycolysis forms from glucose?",
   choices=[
     "ATP, NADH, and pyruvate",
     "ATP, NADPH, and carbon dioxide",
     "ATP, FADH2, and oxygen",
     "NADH, oxygen, and lactic acid",
     "Carbon dioxide, water, and ATP"],
   ans=0,
   why="EK 3.5.B.1 states that glycolysis is a biochemical pathway that releases the energy in glucose molecules to form ATP from ADP and inorganic phosphate, NADH from NAD+, and pyruvate."),

 dict(q="Where does pyruvate go after it is formed, according to the framework?",
   choices=[
     "It is transported from the cytosol to the mitochondrion, where oxidation occurs",
     "It is transported from the mitochondrion to the cytosol, where oxidation occurs",
     "It remains in the cytosol, where the Krebs cycle occurs",
     "It is transported into the chloroplast, where carbon fixation occurs",
     "It is released from the cell immediately after it is formed"],
   ans=0,
   why="EK 3.5.B.2 states that pyruvate is transported from the cytosol to the mitochondrion where oxidation occurs. That transport is also what places glycolysis in the cytosol and the Krebs cycle inside the organelle."),

 dict(q="In which part of the mitochondrion does the Krebs cycle take place?",
   choices=[
     "The matrix",
     "The intermembrane space",
     "The outer mitochondrial membrane",
     "The cytosol just outside the organelle",
     "The inner mitochondrial membrane itself"],
   ans=0,
   why="EK 3.5.B.3 states that the Krebs cycle takes place in the mitochondrial matrix. The inner membrane is where EK 3.5.B.4 places the electron transport chain instead."),

 dict(q="Which gas does the framework say is released from organic intermediates during the Krebs cycle?",
   choices=[
     "Carbon dioxide",
     "Oxygen",
     "Nitrogen",
     "Hydrogen",
     "Water vapor"],
   ans=0,
   why="EK 3.5.B.2 and EK 3.5.B.3 both state that carbon dioxide is released during the Krebs cycle. Oxygen is consumed as the terminal electron acceptor under EK 3.5.A.3.i, not released."),

 dict(q="Which coenzyme conversions does the framework attribute to the Krebs cycle?",
   choices=[
     "NAD+ is reduced to NADH and FAD is reduced to FADH2",
     "NADH is oxidized to NAD+ and FADH2 is oxidized to FAD",
     "NADP+ is reduced to NADPH and FAD is oxidized to FADH2",
     "ATP is reduced to ADP and NAD+ is oxidized to NADH",
     "No coenzyme is changed during the Krebs cycle"],
   ans=0,
   why="EK 3.5.B.2 states that the Krebs cycle releases electrons, reducing NAD+ to NADH and FAD to FADH2. The reduced carriers then deliver those electrons to the chain under EK 3.5.B.4."),

 dict(q="Where do NADH and FADH2 deliver the electrons they carry?",
   choices=[
     "To the electron transport chain in the inner mitochondrial membrane",
     "To the electron transport chain in the outer mitochondrial membrane",
     "To the Krebs cycle enzymes in the matrix",
     "To the glycolysis enzymes in the cytosol",
     "To the photosystems in a thylakoid membrane"],
   ans=0,
   why="EK 3.5.B.4 states that electrons extracted in glycolysis and Krebs cycle reactions are transferred by NADH and FADH2 to the electron transport chain in the inner mitochondrial membrane."),

 dict(q="What does the framework say fermentation accomplishes, and what does it produce?",
   choices=[
     "It allows glycolysis to proceed without oxygen and produces organic molecules such as alcohol and lactic acid",
     "It allows the Krebs cycle to proceed without oxygen and produces carbon dioxide only",
     "It allows the electron transport chain to run using carbon dioxide as the terminal acceptor",
     "It converts lactic acid back into glucose in the absence of oxygen",
     "It produces more ATP per glucose molecule than aerobic respiration does"],
   ans=0,
   why="EK 3.5.B.6 states that fermentation allows glycolysis to proceed in the absence of oxygen and produces organic molecules such as alcohol and lactic acid."),

 dict(q="Isolated mitochondria were supplied with substrate and two different agents, with the results shown. Which agent blocks the transfer of electrons to oxygen?",
   table=_T_MITO,
   choices=[
     "The agent that lowers both oxygen consumption and ATP formation",
     "The agent that raises oxygen consumption while ATP formation collapses",
     "Both agents, since both lower ATP formation",
     "Neither agent, since oxygen consumption occurs under every condition",
     "The condition with no addition, since it shows the highest ATP formation"],
   ans=0,
   why="EK 3.5.A.3.i makes oxygen the terminal acceptor, so a block on the chain must stop oxygen being consumed, and EK 3.5.A.3.iii makes ATP formation depend on the gradient the chain builds. Only one of the two agents lowers both measures."),

 dict(q="Using the same mitochondrial results, which agent separates electron transport from ATP formation, and what does the framework predict is produced instead?",
   table=_T_MITO,
   choices=[
     "The agent that raises oxygen consumption while ATP formation collapses, and heat is produced instead",
     "The agent that lowers oxygen consumption along with ATP formation, and heat is produced instead",
     "The agent that raises oxygen consumption while ATP formation collapses, and extra glucose is produced instead",
     "Neither agent, because the two processes cannot be separated",
     "Both agents equally, because both change ATP formation"],
   ans=0,
   why="EK 3.5.A.3.iv states that decoupling oxidative phosphorylation from electron transport generates heat. The signature in the data is electron transport continuing, shown by oxygen consumption, while ATP formation collapses."),

 dict(q="Yeast cultures were grown with and without oxygen, with the results shown. Which culture is carrying out fermentation?",
   table=_T_YEAST,
   choices=[
     "The culture without oxygen, because it is the one producing ethanol",
     "The culture with oxygen, because it is the one producing ethanol",
     "The culture with oxygen, because it releases the most carbon dioxide",
     "Both cultures equally, because both consumed the same amount of glucose",
     "Neither culture, because fermentation produces no measurable product"],
   ans=0,
   why="EK 3.5.B.6 states that fermentation allows glycolysis to proceed in the absence of oxygen and produces organic molecules such as alcohol. Ethanol appearing only in the culture without oxygen is that statement shown as data."),

 dict(q="Using the same yeast results, why does the culture supplied with oxygen release far more carbon dioxide from the same amount of glucose?",
   table=_T_YEAST,
   choices=[
     "Only that culture can run the Krebs cycle, which releases carbon dioxide from organic intermediates",
     "Only that culture can run glycolysis, which releases carbon dioxide from glucose",
     "Carbon dioxide is produced by the electron transport chain acting on oxygen",
     "Carbon dioxide is produced when ethanol is converted back into glucose",
     "The two cultures released the same amount of carbon dioxide from equal glucose"],
   ans=0,
   why="EK 3.5.B.2 and EK 3.5.B.3 place the release of carbon dioxide in the Krebs cycle, and EK 3.5.B.6 limits the oxygen-free culture to glycolysis. Glycolysis forms pyruvate rather than carbon dioxide under EK 3.5.B.1."),

 dict(q="pH was measured in two regions of a mitochondrion under two conditions, with the results shown. Which statement do the data support?",
   table=_T_PH,
   choices=[
     "While electron transport runs, the matrix is less acidic than the intermembrane space, and the difference disappears when transport is blocked",
     "While electron transport runs, the matrix is more acidic than the intermembrane space, and the difference disappears when transport is blocked",
     "The two regions differ in pH whether or not electron transport is running",
     "The two regions have the same pH whether or not electron transport is running",
     "Blocking electron transport makes the difference between the regions larger"],
   ans=0,
   why="EK 3.5.B.5 states that the pH inside the mitochondrial matrix is higher than in the intermembrane space, and EK 3.5.A.3.ii makes electron transport the cause of the gradient, so removing transport should remove the difference."),

 dict(q="In which part of a eukaryotic cell does the framework place glycolysis?",
   choices=[
     "The cytosol",
     "The mitochondrial matrix",
     "The inner mitochondrial membrane",
     "The intermembrane space of the mitochondrion",
     "The stroma of the chloroplast"],
   ans=0,
   why="EK 3.5.B.2 states that pyruvate is transported from the cytosol to the mitochondrion, which places the pathway that produces pyruvate outside the organelle. EK 3.5.B.3 puts the Krebs cycle in the matrix and EK 3.5.B.4 the chain in the inner membrane."),

 dict(q="A muscle cell is working so hard that oxygen cannot reach it fast enough. What is the most reasonable prediction about how it obtains ATP?",
   choices=[
     "It relies on glycolysis supported by fermentation, and organic products such as lactic acid accumulate",
     "It relies on the electron transport chain, using carbon dioxide as the terminal acceptor",
     "It stops making ATP entirely until oxygen is restored",
     "It runs the Krebs cycle faster to compensate for the missing oxygen",
     "It begins carrying out photosynthesis to obtain energy from light"],
   ans=0,
   why="EK 3.5.B.6 states that fermentation allows glycolysis to proceed in the absence of oxygen and produces organic molecules such as lactic acid, and EK 3.5.A.3.i makes oxygen the terminal acceptor the chain needs."),

 dict(q="An endothermic animal in a cold environment increases the proportion of its mitochondrial electron transport that is decoupled from ATP synthesis. What is the most reasonable prediction?",
   choices=[
     "More of the energy from electron transport appears as heat and less as ATP",
     "More of the energy from electron transport appears as ATP and less as heat",
     "Electron transport stops entirely and the animal cools further",
     "The animal begins to consume less oxygen than before",
     "The animal's mitochondria begin carrying out fermentation instead"],
   ans=0,
   why="EK 3.5.A.3.iv states that decoupling oxidative phosphorylation from electron transport generates heat and that endothermic organisms can use that heat to regulate body temperature. More decoupling directs more of the same electron flow to heat."),

 dict(q="Which statement about cellular respiration is NOT supported by the framework?",
   choices=[
     "The proton concentration is higher inside the inner mitochondrial membrane than outside it",
     "The Krebs cycle takes place in the mitochondrial matrix",
     "Oxygen is the terminal electron acceptor in aerobic respiration",
     "Fermentation allows glycolysis to proceed without oxygen",
     "NADH and FADH2 carry electrons to the electron transport chain"],
   ans=0,
   why="EK 3.5.A.3.ii states the gradient in the opposite sense, high outside the membrane and low inside it, and EK 3.5.B.5 says the same thing in pH terms. The other four restate EK 3.5.B.3, EK 3.5.A.3.i, EK 3.5.B.6 and EK 3.5.B.4."),

 dict(q="Taken together, how do glycolysis, the Krebs cycle and the electron transport chain relate to one another in an aerobic eukaryotic cell?",
   choices=[
     "Glycolysis and the Krebs cycle extract electrons that carriers deliver to the chain, which builds the gradient that drives ATP synthesis",
     "The electron transport chain extracts electrons that carriers deliver to glycolysis, which builds the gradient that drives ATP synthesis",
     "The three processes occur independently and none supplies material to another",
     "Glycolysis builds the proton gradient and the Krebs cycle discharges it through ATP synthase",
     "All three occur in the mitochondrial matrix and use oxygen as their starting material"],
   ans=0,
   why="EK 3.5.B.4 states that electrons extracted in glycolysis and Krebs cycle reactions are transferred by NADH and FADH2 to the chain, EK 3.5.A.3.ii makes the chain build the gradient, and EK 3.5.A.3.iii makes proton return through ATP synthase form the ATP."),
]
