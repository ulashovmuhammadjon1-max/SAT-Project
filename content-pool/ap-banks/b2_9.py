# AP BIOLOGY 2.9 Cell Compartmentalization
# CED effective Fall 2025, Unit 2 Cells. Big Idea 2 Energetics.
# Suggested skill 6.E, predict the causes or effects of a change in, or
# disruption to, one or more components in a biological system.
#
# Essential knowledge, in the framework's own terms:
#   2.9.A.1  Membranes and membrane-bound organelles in eukaryotic cells
#            compartmentalize intracellular metabolic processes and specific
#            enzymatic reactions.
#   2.9.B.1  Internal membranes facilitate cellular processes by minimizing
#            competing interactions and by increasing the surface area where
#            reactions can occur.
#
# ONLY TWO ESSENTIAL KNOWLEDGE STATEMENTS carry this topic, so the questions
# are built from the two mechanisms those statements name -- separation of
# incompatible chemistry, and surface area -- worked through the topic's own
# suggested skill (6.E, predict the effect of a disruption). Every key rests
# on one of those two mechanisms, never on organelle trivia: the identity of
# the organelles belongs to topic 2.1 and the prokaryote comparison to 2.10,
# and this module deliberately stays out of both.
#
# Tables are labelled HYPOTHETICAL and every keyed conclusion is recoverable
# from the table itself, which is how the exam's data sets work.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. Plain prose, no LaTeX.
TOPIC = ("2.9", "Cell Compartmentalization", 2)

_T_FRACTION = dict(
    headers=["Cell fraction",
             "Acid hydrolase activity (hypothetical, units per mg protein)",
             "Catalase activity (hypothetical, units per mg protein)"],
    rows=[["Cytosol", "2", "3"],
          ["Fraction I", "180", "5"],
          ["Fraction II", "4", "240"],
          ["Fraction III", "3", "2"]])

_T_AREA = dict(
    headers=["Membrane", "Surface area (hypothetical, square micrometers)"],
    rows=[["Plasma membrane", "1,700"],
          ["Rough endoplasmic reticulum", "30,000"],
          ["Smooth endoplasmic reticulum", "16,000"],
          ["Inner mitochondrial membrane", "39,000"],
          ["Golgi apparatus", "1,300"]])

_T_LEAK = dict(
    headers=["Treatment time (minutes)",
             "Acid hydrolase activity inside the vesicles (hypothetical, units)",
             "Acid hydrolase activity in the surrounding solution (hypothetical, units)"],
    rows=[["0", "200", "0"],
          ["10", "150", "50"],
          ["20", "100", "100"],
          ["30", "40", "160"]])

_T_SA = dict(
    headers=["Mitochondrion (hypothetical)", "Number of cristae",
             "Inner membrane surface area (square micrometers)",
             "ATP produced per minute (arbitrary units)"],
    rows=[["P", "10", "20", "40"],
          ["Q", "20", "40", "80"],
          ["R", "30", "60", "120"]])

QUESTIONS = [
 dict(q="A liver cell digests worn-out proteins with hydrolytic enzymes while simultaneously building new proteins, and the new proteins are not destroyed. Which feature of the cell best accounts for this?",
   choices=[
     "Membrane-bound organelles hold the hydrolytic enzymes in a separate internal compartment",
     "Hydrolytic enzymes and ribosomes share one active site, so only one of them can operate at a time",
     "The cell alternates between digestion and synthesis so that the two never occur on the same day",
     "Newly made proteins are chemically resistant to hydrolysis until they have folded",
     "Hydrolytic enzymes are produced only after every ribosome in the cell has stopped working"],
   ans=0,
   why="EK 2.9.A.1 states that membranes and membrane-bound organelles compartmentalize intracellular metabolic processes and specific enzymatic reactions. Physical separation is what allows chemistry that would otherwise interfere to proceed in one cell at one time."),

 dict(q="Which statement best describes what the internal membranes of a eukaryotic cell accomplish for the reactions those membranes enclose?",
   choices=[
     "They keep competing interactions apart and add surface on which reactions can occur",
     "They supply the activation energy that the enclosed reactions would otherwise lack",
     "They replace the enzymes that the enclosed reactions would otherwise require",
     "They prevent all molecules from entering or leaving the enclosed space",
     "They make the enclosed reactions independent of temperature and pH"],
   ans=0,
   why="EK 2.9.B.1 names exactly two contributions of internal membranes: minimizing competing interactions and increasing the surface area where reactions can occur. Membranes do not supply activation energy, and every organelle exchanges material with the cytosol."),

 dict(q="A cell is treated with a compound that punches holes in lysosomal membranes while leaving every other membrane intact. Which outcome is the best prediction?",
   choices=[
     "Hydrolytic enzymes escape into the cytosol and damage molecules that were previously protected",
     "The lysosomal enzymes stop working because they were manufactured inside the lysosome",
     "The cell increases its rate of protein synthesis to compensate for the missing membrane",
     "The cytosol becomes strongly acidic and the lysosomal enzymes therefore work faster than before",
     "Nothing changes, because hydrolytic enzymes act only on material delivered by vesicles"],
   ans=0,
   why="EK 2.9.A.1 attributes the separation of specific enzymatic reactions to the organelle membrane. Removing that barrier releases the enzymes into a compartment full of the very macromolecules the barrier was keeping them away from, which is the disruption skill 6.E asks students to predict."),

 dict(q="The inner membrane of a mitochondrion is thrown into deep folds rather than lying smooth against the outer membrane. Which consequence of that folding is most directly relevant to the cell's energy yield?",
   choices=[
     "More membrane area is available to hold the proteins that carry out the reactions",
     "The folds make the mitochondrion impermeable to every small molecule",
     "The folds allow the mitochondrion to divide more often than a smooth organelle could",
     "The folds lower the activation energy of every reaction in the matrix",
     "The folds keep the mitochondrion from being recognized by the cytoskeleton"],
   ans=0,
   why="EK 2.9.B.1 names increased surface area for reactions as one of the two contributions internal membranes make. Reactions carried out by membrane-embedded proteins scale with the amount of membrane available to hold them."),

 dict(q="A plant cell mutant produces chloroplasts whose thylakoid membranes are present but greatly reduced in total area, with all other structures normal. What is the most reasonable prediction about that cell?",
   choices=[
     "Fewer of the reactions that depend on membrane-embedded proteins can occur at one time",
     "The chloroplast loses its ability to be separated from the cytosol",
     "The reactions of the chloroplast now occur in the mitochondrion instead",
     "The chloroplast reactions speed up because there is less membrane in the way",
     "The mutant cell can no longer keep any of its enzymes in one place"],
   ans=0,
   why="EK 2.9.B.1 ties internal membrane area to the amount of reaction that can be supported. Reducing the area reduces how much of the membrane-based chemistry can run at once, while leaving the compartment boundary itself intact."),

 dict(q="Researchers separated a cell into fractions and measured two enzyme activities in each fraction, obtaining the results shown. Which conclusion does the table best support?",
   table=_T_FRACTION,
   choices=[
     "Each of the two enzymes is concentrated in a different fraction, so the two occupy different compartments",
     "Both enzymes are concentrated in the same fraction, so the two share one compartment",
     "Neither enzyme is concentrated anywhere, so both are evenly spread through the cytosol",
     "Acid hydrolase activity is highest in the cytosol, so that enzyme is not compartmentalized",
     "Catalase activity is highest in the fraction with the most acid hydrolase activity"],
   ans=0,
   why="The two activities peak in different fractions, which is the observable signature of the separation EK 2.9.A.1 describes. Every alternative reading is false against the same numbers."),

 dict(q="Why does packaging an enzyme and its substrate into a small organelle tend to raise the rate of the reaction they carry out, compared with releasing both into the whole cytosol?",
   choices=[
     "Confining both to a small volume keeps their concentrations high where they meet",
     "Confinement lowers the activation energy the enzyme must overcome",
     "The organelle membrane substitutes for the enzyme's active site",
     "Enzymes are catalytic only when a membrane is touching them",
     "Substrates cannot move at all unless they are inside a membrane"],
   ans=0,
   why="Compartmentalization concentrates participants rather than changing the chemistry. EK 2.9.A.1 places specific enzymatic reactions inside membrane-bound organelles; the enzyme still lowers activation energy, as EK 3.1.A.1 states, whether or not it is enclosed."),

 dict(q="Peroxisomes carry out oxidation reactions that generate hydrogen peroxide, a molecule that damages many cell components. What does enclosing these reactions in an organelle accomplish?",
   choices=[
     "It keeps a reactive product away from molecules it would otherwise attack",
     "It prevents the oxidation reactions from producing hydrogen peroxide at all",
     "It converts hydrogen peroxide into a substrate for protein synthesis",
     "It allows the oxidation reactions to proceed without any enzymes",
     "It stops oxygen from entering the cell in the first place"],
   ans=0,
   why="EK 2.9.B.1 names minimizing competing interactions as a contribution of internal membranes. Segregating a reactive intermediate is that principle applied to a product rather than to an enzyme."),

 dict(q="In a eukaryotic cell the nuclear envelope separates the site where messenger RNA is made from the site where polypeptides are assembled. Which general principle does that arrangement illustrate?",
   choices=[
     "An internal membrane can separate the steps of a process into distinct compartments",
     "An internal membrane supplies the energy needed to join amino acids",
     "An internal membrane guarantees that a process runs in only one direction",
     "An internal membrane eliminates the need for enzymes in the enclosed space",
     "An internal membrane keeps the cell from exchanging material with its surroundings"],
   ans=0,
   why="EK 2.9.A.1 makes compartmentalization of intracellular processes the function of membranes and membrane-bound organelles. The nuclear envelope is that principle applied to two steps of one information pathway."),

 dict(q="A drug prevents newly made hydrolytic enzymes from being sorted into lysosomes, so they are released into the cytosol instead. Which prediction follows most directly from the principle of compartmentalization?",
   choices=[
     "Cytosolic proteins and organelles begin to be broken down inappropriately",
     "The enzymes lose their catalytic activity because they never entered a lysosome",
     "The cell responds by building additional plasma membrane",
     "Lysosomes swell because they have taken in extra enzymes",
     "Protein synthesis continues at exactly the previous rate with no other change"],
   ans=0,
   why="EK 2.9.A.1 makes the compartment the reason a specific enzymatic reaction is confined. A mis-sorted enzyme is still catalytic; what changes is which molecules it now meets, which is the effect skill 6.E asks students to predict."),

 dict(q="A cell doubles the total area of its rough endoplasmic reticulum in response to a demand for secreted protein. Which explanation of the benefit is best supported by the framework?",
   choices=[
     "The added membrane increases the surface where the reactions of protein processing occur",
     "The added membrane raises the temperature at which those reactions occur",
     "The added membrane removes the need for ribosomes",
     "The added membrane makes each protein molecule larger",
     "The added membrane converts the cytosol into an additional compartment"],
   ans=0,
   why="EK 2.9.B.1 names increasing the surface area where reactions can occur as a contribution of internal membranes. Building more of a membrane whose surface hosts the process is the direct application of that statement."),

 dict(q="Which of the following is the best evidence that a particular enzyme is normally confined to a membrane-bound organelle rather than dissolved in the cytosol?",
   choices=[
     "Its activity is recovered almost entirely in one isolated organelle fraction",
     "It has a higher molecular mass than the average cytosolic protein",
     "Its reaction releases more energy than most cytosolic reactions",
     "It is present at the same activity in every fraction of the disrupted cell",
     "It requires a substrate that the cell can synthesize for itself"],
   ans=0,
   why="Compartmentalization is a claim about location, so the evidence has to be a measurement of location. Recovery of activity in one fraction is exactly the observation that separation of enzymatic reactions in EK 2.9.A.1 predicts; mass and energetics say nothing about where an enzyme sits."),

 dict(q="The interior of a lysosome is maintained at a pH well below that of the surrounding cytosol. Which statement best explains why this is possible only in a compartmentalized cell?",
   choices=[
     "A membrane boundary allows one region to hold conditions different from the rest of the cell",
     "Acids are produced only inside organelles and never in the cytosol",
     "Hydrogen ions cannot exist outside a membrane-bound organelle",
     "The cytosol has no buffering capacity of any kind",
     "An organelle sets the pH of the entire cell to match its own interior"],
   ans=0,
   why="EK 2.9.A.1 places metabolic processes inside membrane-bound organelles; distinct local conditions are what a boundary makes possible. Without the boundary the interior and the cytosol would equilibrate and the enzymes tuned to the low pH would work poorly, as EK 3.2.A.1 describes."),

 dict(q="Two metabolic pathways in a eukaryotic cell use the same small intermediate, but one pathway consumes it in the mitochondrial matrix and the other in the cytosol. What does the arrangement allow the cell to do?",
   choices=[
     "Regulate the two pathways separately even though they draw on the same molecule",
     "Run both pathways at the maximum possible rate without any regulation",
     "Convert the shared intermediate into an enzyme when it is not needed",
     "Guarantee that the two pathways always proceed at identical rates",
     "Eliminate the need for the shared intermediate in both pathways"],
   ans=0,
   why="EK 2.9.B.1 names minimizing competing interactions as a purpose of internal membranes. Two pools of one intermediate on opposite sides of a membrane can be drawn down independently, which a single shared pool could not be."),

 dict(q="Golgi processing occurs in a series of separate membrane-bound sacs rather than in one large space. Which advantage of that arrangement follows most directly from the framework?",
   choices=[
     "Different modifying reactions can be kept in different compartments and applied in order",
     "Each sac performs all the modifications at once, so processing takes less time",
     "The sacs prevent any protein from leaving the cell",
     "The sacs remove the need for vesicles to carry material",
     "The sacs make the modifying enzymes unnecessary"],
   ans=0,
   why="EK 2.9.A.1 attributes compartmentalization of specific enzymatic reactions to membrane-bound organelles. Separate sacs are separate compartments, so a set of enzymes can act on a product without the next set acting at the same time."),

 dict(q="Membrane surface areas were measured in a single cell, with the results shown. Which conclusion is supported by these values?",
   table=_T_AREA,
   choices=[
     "The membranes inside the cell together provide far more surface than the plasma membrane does",
     "The plasma membrane provides more surface than all the internal membranes combined",
     "The Golgi apparatus provides the largest single membrane surface in the cell",
     "The rough and smooth endoplasmic reticulum have equal surface areas",
     "The inner mitochondrial membrane provides less surface than the plasma membrane"],
   ans=0,
   why="The internal membranes listed sum to many times the plasma membrane value, which is the quantitative form of the claim in EK 2.9.B.1 that internal membranes increase the surface area where reactions can occur."),

 dict(q="Isolated vesicles containing hydrolytic enzymes were exposed to a membrane-disrupting agent and sampled over time, giving the values shown. Which interpretation do the data support?",
   table=_T_LEAK,
   choices=[
     "Enzyme is leaving the vesicles over time, so the membrane was what confined it",
     "Enzyme is being synthesized inside the vesicles over time",
     "Enzyme activity is being destroyed rather than relocated",
     "The vesicle membrane became less permeable as the treatment continued",
     "Enzyme was never inside the vesicles at any sampling time"],
   ans=0,
   why="Activity falls inside and rises outside while the running total stays put, which is relocation and not synthesis or destruction. That the barrier is what held the enzyme in is the separation claim of EK 2.9.A.1 shown experimentally."),

 dict(q="Which of the following would be the best experimental test of the claim that a certain reaction takes place inside an organelle rather than in the cytosol?",
   choices=[
     "Isolate the organelle and ask whether the reaction still occurs in the isolated fraction",
     "Measure the total rate of the reaction in an intact cell and compare it with a textbook value",
     "Count the number of organelles of that kind in a sample of cells",
     "Measure the mass of the organelle fraction after centrifugation",
     "Determine the amino acid sequence of the enzyme that catalyzes the reaction"],
   ans=0,
   why="Skill 3.C asks for procedures aligned to the question. Only separating the compartment and re-testing distinguishes the two locations; counting organelles or sequencing an enzyme leaves both possibilities alive."),

 dict(q="A researcher argues that compartmentalization allows a eukaryotic cell to hold more kinds of chemistry at once than a cell of the same volume without internal membranes. Which piece of evidence most directly supports that argument?",
   choices=[
     "Enzymes with incompatible requirements are found concentrated in separate organelles",
     "Eukaryotic cells contain more total protein than prokaryotic cells",
     "Eukaryotic cells are on average larger than prokaryotic cells",
     "Enzymes lose activity when they are heated above their optimal temperature",
     "Membranes are composed largely of phospholipids arranged in a bilayer"],
   ans=0,
   why="Skill 6.B asks for evidence connected to the claim. The claim is about incompatible chemistry coexisting, so the supporting observation has to be incompatible enzymes found in separate places, which is EK 2.9.A.1 and EK 2.9.B.1 stated as data."),

 dict(q="Vesicles budding from one organelle and fusing with another are themselves bounded by membrane. What does that membrane accomplish while the vesicle is in transit?",
   choices=[
     "It keeps the cargo separated from the cytosol during the journey",
     "It converts the cargo into a different molecule before delivery",
     "It supplies the energy needed to move the vesicle",
     "It ensures the cargo cannot be delivered to the wrong destination under any circumstance",
     "It allows the cargo to diffuse freely into the cytosol along the way"],
   ans=0,
   why="EK 2.9.A.1 makes the membrane the boundary that compartmentalizes cell contents. A transport vesicle is a temporary compartment, so its cargo remains separated from the cytosol until fusion delivers it."),

 dict(q="A toxin causes the membranes of a cell's organelles to fuse into one continuous space while the plasma membrane stays intact. Which effect on cell metabolism is most likely?",
   choices=[
     "Reactions formerly kept apart now interfere with one another",
     "Metabolism speeds up because substrates now reach every enzyme in the cell",
     "The cell stops taking in material because the plasma membrane is unaffected",
     "The enzymes of the cell are all denatured by the fusion event",
     "Every reaction in the cell now runs at its optimal rate"],
   ans=0,
   why="The predicted effect of removing the boundaries is the loss of what the boundaries provided. EK 2.9.B.1 names minimizing competing interactions, so merging the compartments restores exactly the competition that was being minimized."),

 dict(q="Which observation would most weaken the claim that a certain hydrolytic enzyme is confined to an organelle in healthy cells?",
   choices=[
     "The enzyme's activity is found at the same level in every fraction of a disrupted cell",
     "The enzyme has an optimal pH lower than that of the cytosol",
     "The enzyme is synthesized on ribosomes bound to the endoplasmic reticulum",
     "The enzyme's activity in the organelle fraction is higher than in the whole cell homogenate",
     "The enzyme requires a metal ion for activity"],
   ans=0,
   why="A confinement claim predicts uneven distribution across fractions. An even distribution is the one listed result inconsistent with that prediction; the other observations are compatible with confinement or say nothing about location."),

 dict(q="Mitochondria from three cells were compared, with the results shown. Which relationship do these data support?",
   table=_T_SA,
   choices=[
     "The rate of ATP production rises in step with the inner membrane surface area",
     "The rate of ATP production falls as inner membrane surface area rises",
     "The rate of ATP production is unrelated to the inner membrane surface area",
     "The rate of ATP production is highest in the mitochondrion with the fewest cristae",
     "Every mitochondrion produces the same amount of ATP per minute"],
   ans=0,
   why="The two columns rise together across all three mitochondria, and the ratio of ATP to area is constant. That is the surface area claim of EK 2.9.B.1 expressed as data, which skill 4.B asks students to describe."),

 dict(q="An investigator wants to explain why a particular set of reactions occurs only in one organelle of a eukaryotic cell. Which explanation is consistent with the framework?",
   choices=[
     "The enzymes for those reactions are targeted to that compartment and act where they are delivered",
     "The reactions could occur anywhere but the cell chooses one site at random each generation",
     "The reactions are impossible outside a membrane regardless of which enzymes are present",
     "The reactions require the organelle membrane itself as a substrate",
     "The reactions occur only where the cell's DNA is located"],
   ans=0,
   why="EK 2.9.A.1 attributes the localization of specific enzymatic reactions to compartmentalization by membranes and membrane-bound organelles. A reaction happens where its enzyme is, and the enzyme is where the cell has put it."),

 dict(q="Which statement about compartmentalization is NOT supported by the framework?",
   choices=[
     "Internal membranes make the enclosed reactions independent of the surrounding conditions",
     "Internal membranes increase the surface area available for reactions",
     "Internal membranes reduce interference between incompatible processes",
     "Membrane-bound organelles hold specific enzymatic reactions in defined regions",
     "Compartments allow different regions of one cell to have different chemical conditions"],
   ans=0,
   why="EK 2.9.A.1 and EK 2.9.B.1 support the other four statements. Nothing in the framework claims independence from surrounding conditions, and organelles constantly exchange substrates and products with the cytosol."),

 dict(q="An enzyme that normally works in the acidic interior of a lysosome escapes into the neutral cytosol. What is the most likely immediate effect on that enzyme's activity?",
   choices=[
     "Its activity falls because it is now outside the pH range in which it works best",
     "Its activity rises because the cytosol contains more substrate than the lysosome",
     "Its activity is unchanged because pH has no effect on enzyme structure",
     "Its activity rises because a neutral pH is optimal for every enzyme",
     "Its activity falls to zero permanently because a released enzyme is always destroyed"],
   ans=0,
   why="Compartments hold local conditions, and EK 3.2.A.1 states that pH outside the optimal range for a given enzyme alters the efficiency with which it catalyzes reactions. The immediate change is a drop in efficiency, not necessarily permanent destruction."),

 dict(q="Cell A has extensive internal membranes; cell B is the same size but has almost none. Both are supplied with the same substrates. Which comparison is best justified?",
   choices=[
     "Cell A can support a greater variety of separated reactions at one time",
     "Cell B can support a greater variety of separated reactions at one time",
     "The two cells can support exactly the same set of separated reactions",
     "Cell B has more surface available for membrane-bound reactions",
     "Cell A cannot exchange material with its surroundings"],
   ans=0,
   why="Both mechanisms of EK 2.9.B.1 favor the cell with more internal membrane: more surface for membrane-based reactions and more boundaries to keep competing interactions apart."),

 dict(q="Which of the following best describes the relationship between an organelle's membrane and the enzymes it encloses?",
   choices=[
     "The membrane defines where the enzymes act by controlling what reaches them",
     "The membrane catalyzes the reactions and the enzymes only hold the substrate",
     "The membrane determines the amino acid sequence of the enclosed enzymes",
     "The membrane is consumed each time an enclosed enzyme completes a reaction",
     "The membrane is identical in composition to the enzymes it encloses"],
   ans=0,
   why="EK 2.9.A.1 makes the membrane the compartment boundary, not a catalyst. What the boundary changes is which molecules are present at the enzyme, and that is what confines a specific enzymatic reaction to a region."),

 dict(q="A student claims that a cell with no internal membranes would still be able to run every reaction a compartmentalized cell runs, simply more slowly. What is the strongest objection?",
   choices=[
     "Some pairs of reactions destroy each other's participants and cannot share one space at all",
     "Reactions cannot occur in the absence of a membrane under any conditions",
     "Enzymes are synthesized only inside membrane-bound organelles",
     "A cell without internal membranes cannot import any substrate",
     "Slower reactions release more energy than faster ones"],
   ans=0,
   why="The claim concedes rate but not compatibility, so the objection has to be about compatibility. EK 2.9.B.1 names minimizing competing interactions as a distinct contribution from surface area, and a hydrolytic enzyme meeting the proteins it degrades is a difference in kind rather than in speed."),

 dict(q="Taken together, the two mechanisms the framework assigns to internal membranes are best summarized as which pair?",
   choices=[
     "Keeping incompatible processes apart, and providing more area on which reactions occur",
     "Generating energy, and storing the cell's genetic information",
     "Synthesizing enzymes, and destroying damaged organelles",
     "Blocking all transport, and maintaining a single uniform interior",
     "Replicating the cell's DNA, and dividing the cytoplasm during cytokinesis"],
   ans=0,
   why="EK 2.9.B.1 names precisely these two: internal membranes facilitate cellular processes by minimizing competing interactions and by increasing the surface area where reactions can occur."),
]
