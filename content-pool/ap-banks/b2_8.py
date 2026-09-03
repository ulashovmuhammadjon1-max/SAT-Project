# AP BIOLOGY 2.8 Mechanisms of Transport
# CED effective Fall 2025, Unit 2 Cells. Big Idea 2 Energetics.
# Learning objective 2.8.A: describe the processes that allow ions and other molecules
# to move across membranes. Suggested skill 1.B, explain biological concepts and
# processes.
#
# Essential knowledge relied on -- the topic has exactly one statement:
#   2.8.A.1    Metabolic energy (such as that from ATP) is required for active
#              transport of molecules and ions across the membrane and to establish and
#              maintain electrochemical gradients.
#     i.       Membrane proteins are necessary for active transport.
#     ii.      The sodium-potassium pump and ATPase contribute to the maintenance of
#              the membrane potential.
#
# ON THE CHAINS, because one statement cannot carry thirty questions on its own. Every
# item that reaches outside EK 2.8.A.1 chains to a statement this bank has already used
# and the claim in verify_b2_8.py names it:
#   EK 2.5.A.2  passive transport is net movement down a gradient with NO direct input
#               of metabolic energy -- used for every contrast with active transport;
#   EK 2.5.A.3  active transport requires the direct input of energy and in some cases
#               moves molecules from low concentration to high;
#   EK 2.6.A.1 i  membranes may become polarized by the movement of ions, which is the
#               only other place the framework touches membrane potential;
#   EK 2.6.A.2  facilitated diffusion uses proteins but NO energy input -- the contrast
#               that makes EK 2.8.A.1 i's protein requirement insufficient on its own;
#   EK 2.4.A.2  small nonpolar molecules freely pass, needing neither protein nor energy.
# No item asserts a mechanism for the pump beyond what EK 2.8.A.1 ii states, namely
# that it and ATPase contribute to the maintenance of the membrane potential.
#
# ON NOTATION. The CED prints the pump with ion symbols and charges. Biology is
# exported as prose with no typesetting, so this bank names it in words.
#
# ON THE DATA. Every table is labelled hypothetical, and every keyed conclusion is
# recoverable from the table alone and recomputed in verify_b2_8.py.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: Biology is exported as prose.
TOPIC = ("2.8", "Mechanisms of Transport", 2)

_T_PUMP = dict(
    headers=["Treatment (hypothetical)",
             "Sodium ions pumped out of the cell per minute (arbitrary units)",
             "Magnitude of the membrane potential (millivolts)"],
    rows=[["Untreated cells", "240", "70"],
          ["Cells with ATP synthesis blocked", "8", "12"],
          ["Cells with the pump proteins removed", "4", "10"]])

_T_DECAY = dict(
    headers=["Time after ATP synthesis was blocked (minutes)",
             "Sodium concentration outside the cell (millimolar)",
             "Sodium concentration inside the cell (millimolar)"],
    rows=[["0", "145", "12"],
          ["20", "120", "38"],
          ["40", "95", "62"],
          ["60", "79", "79"]])

_T_PROCESSES = dict(
    headers=["Process (hypothetical)", "Requires a membrane protein",
             "Requires a direct input of metabolic energy"],
    rows=[["Process 1", "yes", "yes"],
          ["Process 2", "yes", "no"],
          ["Process 3", "no", "no"]])

QUESTIONS = [

 dict(q="For which two things does the course framework say metabolic energy is required "
        "in this topic?",
      choices=[
        "Active transport of molecules and ions across the membrane, and establishing and "
        "maintaining electrochemical gradients",
        "Passive transport of molecules across the membrane, and abolishing "
        "electrochemical gradients",
        "The synthesis of the phospholipids of the membrane, and the folding of proteins",
        "The free passage of small nonpolar molecules, and the formation of vesicles",
        "The digestion of engulfed material, and the capture of light energy"],
      ans=0,
      why="EK 2.8.A.1 states that metabolic energy is required for active transport of "
          "molecules and ions across the membrane and to establish and maintain "
          "electrochemical gradients. Passive transport is defined in EK 2.5.A.2 as "
          "happening without such an input."),

 dict(q="Which source of metabolic energy does the course framework name in this topic?",
      choices=["ATP", "Sunlight absorbed by the plasma membrane",
               "The concentration gradient itself", "Heat from the environment",
               "The hydrophobic interior of the membrane"],
      ans=0,
      why="EK 2.8.A.1 gives ATP as its example of metabolic energy, in the phrase "
          "metabolic energy such as that from ATP. The framework offers no other source "
          "for active transport in this statement."),

 dict(q="What does the course framework say about membrane proteins and active transport?",
      choices=[
        "Membrane proteins are necessary for active transport.",
        "Membrane proteins prevent active transport from occurring.",
        "Membrane proteins are necessary only for passive transport.",
        "Active transport occurs directly through the hydrophobic interior without "
        "proteins.",
        "Membrane proteins are necessary only when no energy is available."],
      ans=0,
      why="EK 2.8.A.1 i states that membrane proteins are necessary for active transport. "
          "EK 2.4.A.3 separately makes the hydrophobic interior what prevents ions and "
          "polar molecules from crossing directly."),

 dict(q="Which two things does the course framework say contribute to the maintenance of "
        "the membrane potential?",
      choices=[
        "The sodium-potassium pump and ATPase",
        "The cell wall and the glycolipids",
        "Aquaporins and the cholesterol in the membrane",
        "The ribosome and the Golgi complex",
        "The nonpolar hydrocarbon tails and the phosphate regions"],
      ans=0,
      why="EK 2.8.A.1 ii states that the sodium-potassium pump and ATPase contribute to "
          "the maintenance of the membrane potential. Aquaporins carry water under EK "
          "2.6.A.3 and the cell wall is a separate barrier under EK 2.4.B.1."),

 dict(q="According to the course framework, metabolic energy is needed both to establish "
        "an electrochemical gradient and to do what else?",
      choices=[
        "To maintain that gradient once it exists",
        "To abolish that gradient once it exists",
        "To convert that gradient into a cell wall",
        "To prevent any ion from crossing the membrane",
        "To synthesize the ions that make up the gradient"],
      ans=0,
      why="EK 2.8.A.1 states that metabolic energy is required to establish AND maintain "
          "electrochemical gradients. Both verbs are in the same clause, so an energy "
          "supply is needed continuously rather than only at the outset."),

 dict(q="Why does an electrochemical gradient require a continuing supply of energy "
        "rather than a single initial input, on the framework's own terms?",
      choices=[
        "Because the framework says energy is required to maintain the gradient as well "
        "as to establish it",
        "Because the framework says energy is required only to establish the gradient",
        "Because a gradient can only exist while the membrane is impermeable to every "
        "substance",
        "Because the membrane proteins are consumed each time an ion crosses",
        "Because the gradient converts itself into ATP as it decays"],
      ans=0,
      why="EK 2.8.A.1 puts establish and maintain in the same clause about what metabolic "
          "energy is required for. The framework says nothing about proteins being "
          "consumed, and EK 2.4.A.1 makes the membrane selectively rather than completely "
          "impermeable."),

 dict(q="A cell's supply of ATP is destroyed. Which pair of consequences does the course "
        "framework predict?",
      choices=[
        "Active transport stops, and existing electrochemical gradients are no longer "
        "maintained.",
        "Active transport continues, and existing electrochemical gradients become "
        "steeper.",
        "Passive transport stops, and active transport continues unchanged.",
        "The membrane loses its phospholipid framework, and no transport of any kind "
        "occurs.",
        "Nothing changes, because transport across membranes never requires energy."],
      ans=0,
      why="EK 2.8.A.1 makes metabolic energy required both for active transport and to "
          "establish and maintain electrochemical gradients, so removing that energy "
          "reaches both. EK 2.5.A.2 makes passive transport independent of such an "
          "input, which is why it is not the process that stops."),

 dict(q="A drug removes every protein from a cell's plasma membrane while leaving the "
        "phospholipid bilayer and the cell's ATP supply intact. What does the course "
        "framework predict for active transport?",
      choices=[
        "It will stop, because membrane proteins are necessary for active transport.",
        "It will continue, because an intact ATP supply is all that active transport "
        "requires.",
        "It will continue, because active transport occurs through the hydrophobic "
        "interior.",
        "It will speed up, because the proteins had been obstructing the membrane.",
        "It will be replaced by the free passage of ions through the bilayer."],
      ans=0,
      why="EK 2.8.A.1 i states that membrane proteins are necessary for active transport, "
          "so the energy supply alone is not sufficient. EK 2.4.A.3 makes the nonpolar "
          "hydrocarbon tails prevent ions from crossing the interior directly."),

 dict(q="The course framework specifies what metabolic energy is required to move "
        "actively across the membrane. What does it name?",
      choices=[
        "Molecules and ions alike",
        "Molecules only, never ions",
        "Ions only, never molecules",
        "Water only, and only through aquaporins",
        "Only substances that are already more concentrated inside the cell"],
      ans=0,
      why="EK 2.8.A.1 states that metabolic energy is required for active transport of "
          "molecules and ions across the membrane, naming both together. Water through "
          "aquaporins is EK 2.6.A.3's facilitated route, which EK 2.6.A.2 says takes no "
          "energy input at all."),

 dict(q="Both facilitated diffusion and active transport use membrane proteins. What "
        "separates them in the course framework?",
      choices=[
        "Active transport requires metabolic energy and facilitated diffusion occurs with "
        "no energy input.",
        "Facilitated diffusion requires metabolic energy and active transport occurs with "
        "no energy input.",
        "Active transport uses channel proteins and facilitated diffusion uses none.",
        "Facilitated diffusion moves only ions and active transport moves only water.",
        "Nothing separates them; they are two names for one process."],
      ans=0,
      why="EK 2.8.A.1 requires metabolic energy for active transport and EK 2.6.A.2 states "
          "that facilitated diffusion moves substances with no energy input and down the "
          "concentration gradient. Both use proteins, so the protein requirement of EK "
          "2.8.A.1 i cannot be what distinguishes them."),

 dict(q="Which pump does the course framework name in connection with the membrane "
        "potential?",
      choices=["The sodium-potassium pump", "An aquaporin", "A glucose channel",
               "The contractile vacuole", "The Golgi complex"],
      ans=0,
      why="EK 2.8.A.1 ii names the sodium-potassium pump, together with ATPase, as "
          "contributing to the maintenance of the membrane potential. Aquaporins carry "
          "water under EK 2.6.A.3 and the contractile vacuole is an osmoregulation "
          "example under EK 2.7.A.1."),

 dict(q="How does the course framework's statement that membranes may become polarized by "
        "the movement of ions relate to its statement about the membrane potential?",
      choices=[
        "Both concern a difference established across the membrane by ions, which the "
        "pump and ATPase help maintain.",
        "They concern unrelated properties, since polarization involves phospholipids "
        "rather than ions.",
        "Polarization abolishes the membrane potential, which is why energy is needed.",
        "The membrane potential is a property of the cell wall rather than the membrane.",
        "Only plant cells have a membrane potential, while only animal cells become "
        "polarized."],
      ans=0,
      why="EK 2.6.A.1 i states that membranes may become polarized by the movement of ions "
          "across the membrane, and EK 2.8.A.1 ii states that the sodium-potassium pump "
          "and ATPase contribute to the maintenance of the membrane potential. Both "
          "statements concern the same ion-established difference across the membrane."),

 dict(q="The table reports sodium pumping and membrane potential under three conditions. "
        "Which conclusion is best supported?",
      table=_T_PUMP,
      choices=[
        "Both the pumping of sodium and the membrane potential depend on an energy supply "
        "and on the pump proteins.",
        "Sodium pumping depends on the energy supply, but the membrane potential does "
        "not.",
        "The membrane potential depends on the pump proteins, but sodium pumping does "
        "not.",
        "Neither measurement depends on the energy supply or on the pump proteins.",
        "Removing the pump proteins increased both measurements."],
      ans=0,
      why="Both columns fall to a small fraction of their untreated values under either "
          "treatment. EK 2.8.A.1 requires metabolic energy for active transport and EK "
          "2.8.A.1 i makes membrane proteins necessary for it, while EK 2.8.A.1 ii ties "
          "the pump to the maintenance of the membrane potential."),

 dict(q="Which condition in the same table isolates the framework's claim that membrane "
        "proteins are necessary for active transport?",
      table=_T_PUMP,
      choices=[
        "The condition in which the pump proteins were removed while ATP synthesis was "
        "left intact",
        "The condition in which ATP synthesis was blocked while the pump proteins were "
        "left intact",
        "The untreated condition",
        "No condition in the table isolates that claim.",
        "Both treated conditions isolate that claim equally."],
      ans=0,
      why="Isolating the protein requirement of EK 2.8.A.1 i means removing the proteins "
          "while leaving the energy supply available, which is what one of the two "
          "treatments does. Blocking ATP synthesis tests the energy requirement of EK "
          "2.8.A.1 instead."),

 dict(q="Using the same table, about how many times as fast did untreated cells pump "
        "sodium compared with cells whose ATP synthesis was blocked?",
      table=_T_PUMP,
      choices=["About thirty times as fast", "About three times as fast",
               "About half as fast", "About the same", "About three hundred times as "
               "fast"],
      ans=0,
      why="Dividing the untreated pumping rate by the rate with ATP synthesis blocked "
          "gives the comparison directly from the table. It is the quantitative form of "
          "EK 2.8.A.1's claim that metabolic energy is required for active transport."),

 dict(q="The table follows the sodium concentration on each side of a membrane after ATP "
        "synthesis was blocked. Which statement describes what happened?",
      table=_T_DECAY,
      choices=[
        "The difference between the two sides shrank until the concentrations were equal.",
        "The difference between the two sides grew steadily larger.",
        "The difference between the two sides stayed the same throughout.",
        "The outside concentration rose while the inside concentration fell.",
        "Both concentrations fell to zero."],
      ans=0,
      why="The outside concentration falls and the inside rises at every time point until "
          "the two are equal. EK 2.8.A.1 requires metabolic energy to establish and "
          "maintain electrochemical gradients, so removing that energy leaves the "
          "gradient unmaintained."),

 dict(q="What does that time course best demonstrate about the course framework's claim?",
      table=_T_DECAY,
      choices=[
        "That maintaining an electrochemical gradient, and not merely establishing it, "
        "requires metabolic energy",
        "That establishing an electrochemical gradient requires metabolic energy but "
        "maintaining it does not",
        "That an electrochemical gradient forms spontaneously without any energy input",
        "That membrane proteins are unnecessary for active transport",
        "That passive transport requires metabolic energy"],
      ans=0,
      why="The gradient existed at the moment the energy supply was removed and then "
          "decayed, which tests maintenance rather than establishment. EK 2.8.A.1 puts "
          "establish and maintain in the same clause about what metabolic energy is "
          "required for."),

 dict(q="What would the same measurements be expected to show if ATP synthesis had NOT "
        "been blocked, according to the course framework?",
      table=_T_DECAY,
      choices=[
        "The difference between the two sides would have been maintained rather than "
        "decaying to zero.",
        "The difference between the two sides would have decayed to zero even faster.",
        "The outside concentration would have fallen to zero.",
        "The inside concentration would have fallen below the outside concentration "
        "immediately.",
        "No prediction is possible, because the framework says nothing about maintaining "
        "gradients."],
      ans=0,
      why="EK 2.8.A.1 states that metabolic energy is required to establish and maintain "
          "electrochemical gradients, so a cell with that energy available is expected to "
          "hold the gradient it started with. The framework's explicit use of the word "
          "maintain is what makes the prediction available."),

 dict(q="The table records whether three transport processes require a membrane protein "
        "and whether they require a direct input of metabolic energy. Which process is "
        "active transport?",
      table=_T_PROCESSES,
      choices=["Process 1", "Process 2", "Process 3",
               "All three are active transport.",
               "None of them is active transport."],
      ans=0,
      why="EK 2.8.A.1 requires metabolic energy for active transport and EK 2.8.A.1 i "
          "makes membrane proteins necessary for it, so active transport is the row that "
          "answers yes to both. Exactly one row does."),

 dict(q="Among the same three processes, which is consistent with facilitated diffusion?",
      table=_T_PROCESSES,
      choices=["Process 2", "Process 1", "Process 3",
               "All three are consistent with facilitated diffusion.",
               "None of them is consistent with facilitated diffusion."],
      ans=0,
      why="EK 2.6.A.1 requires transport or channel proteins for facilitated diffusion and "
          "EK 2.6.A.2 states that it happens with no energy input, so it is the row that "
          "answers yes to the protein and no to the energy. Exactly one row does."),

 dict(q="Which of the three processes in the table is consistent with the free passage of "
        "a small nonpolar molecule across the membrane?",
      table=_T_PROCESSES,
      choices=["Process 3", "Process 1", "Process 2",
               "All three are consistent with free passage.",
               "None of them is consistent with free passage."],
      ans=0,
      why="EK 2.4.A.2 states that small nonpolar molecules freely pass across the "
          "membrane, needing neither a protein nor an energy input, so the row answering "
          "no to both is the match. Exactly one row does."),

 dict(q="Which observation would best indicate that a cell is carrying out active "
        "transport rather than any other process the framework describes?",
      choices=[
        "A solute accumulates against its concentration gradient, and the accumulation "
        "stops when the cell's ATP supply is removed.",
        "A solute moves down its concentration gradient, and the movement stops when the "
        "cell's ATP supply is removed.",
        "A solute moves down its concentration gradient, and the movement continues when "
        "the cell's ATP supply is removed.",
        "A solute crosses the membrane through an embedded protein.",
        "A solute crosses the membrane faster at a higher external concentration."],
      ans=0,
      why="EK 2.5.A.3 gives active transport the direct input of energy and, in some "
          "cases, movement from low concentration to high, and EK 2.8.A.1 restates the "
          "energy requirement. Crossing through an embedded protein is shared with "
          "facilitated diffusion under EK 2.6.A.1, so it cannot distinguish the two."),

 dict(q="Which process would be expected to continue when a cell can no longer make ATP?",
      choices=[
        "The movement of a small nonpolar molecule down its concentration gradient",
        "The pumping of sodium out of the cell against its gradient",
        "The maintenance of an existing electrochemical gradient",
        "The active transport of ions across the membrane",
        "None of these, because every process listed requires ATP"],
      ans=0,
      why="EK 2.4.A.2 lets small nonpolar molecules freely pass and EK 2.5.A.2 makes such "
          "movement independent of a direct energy input. The other three are exactly "
          "what EK 2.8.A.1 says metabolic energy is required for."),

 dict(q="A student states that supplying a cell with plenty of ATP is enough to guarantee "
        "active transport across its membrane. What is the best correction?",
      choices=[
        "Membrane proteins are also necessary for active transport, so energy alone is "
        "not sufficient.",
        "ATP is not a source of metabolic energy, so supplying it changes nothing.",
        "Active transport requires no energy, so supplying ATP is beside the point.",
        "Active transport requires the membrane to lose its selective permeability "
        "first.",
        "The student is correct, because energy is the only requirement the framework "
        "names."],
      ans=0,
      why="EK 2.8.A.1 names metabolic energy as required and EK 2.8.A.1 i separately "
          "states that membrane proteins are necessary for active transport, so the "
          "framework names two requirements rather than one."),

 dict(q="What role does the course framework assign to ATPase in this topic?",
      choices=[
        "Contributing, along with the sodium-potassium pump, to the maintenance of the "
        "membrane potential",
        "Transporting large quantities of water across the membrane",
        "Forming the structural framework of the plasma membrane",
        "Digesting material the cell has taken in by endocytosis",
        "Preventing ions from crossing the membrane at all"],
      ans=0,
      why="EK 2.8.A.1 ii names the sodium-potassium pump and ATPase together as "
          "contributing to the maintenance of the membrane potential. Water transport "
          "belongs to aquaporins under EK 2.6.A.3 and digestion to lysosomes under EK "
          "2.1.A.6."),

 dict(q="A researcher wants to test whether a particular membrane protein is required for "
        "a cell to move an ion against its concentration gradient. Which comparison is "
        "most informative?",
      choices=[
        "Cells with the protein and otherwise identical cells without it, both supplied "
        "with the same energy source",
        "Cells with the protein supplied with energy and cells with the protein deprived "
        "of energy",
        "Cells with the protein at two different external ion concentrations",
        "Cells without the protein at two different temperatures",
        "Cells with the protein measured at several time points"],
      ans=0,
      why="A requirement claim about the PROTEIN needs the protein to be the only "
          "difference between otherwise identical preparations, with the energy supply "
          "held constant. The second comparison tests the energy requirement of EK "
          "2.8.A.1 rather than the protein requirement of EK 2.8.A.1 i."),

 dict(q="Which statement about the relationship between energy and gradients matches the "
        "course framework?",
      choices=[
        "Metabolic energy is spent to build and hold electrochemical gradients, which "
        "would otherwise not persist.",
        "Electrochemical gradients supply the metabolic energy a cell needs and cost it "
        "nothing.",
        "Electrochemical gradients form only when metabolic energy is unavailable.",
        "Metabolic energy is required to abolish electrochemical gradients rather than to "
        "build them.",
        "Electrochemical gradients and metabolic energy are unrelated in the framework."],
      ans=0,
      why="EK 2.8.A.1 states that metabolic energy is required to establish and maintain "
          "electrochemical gradients. Both verbs point the same way: energy is spent on "
          "the gradient rather than obtained from it in this statement."),

 dict(q="A cell's membrane potential falls toward zero shortly after its energy supply is "
        "interrupted. Which explanation is best supported by the course framework?",
      choices=[
        "The sodium-potassium pump and ATPase, which contribute to maintaining the "
        "membrane potential, require metabolic energy.",
        "The phospholipid bilayer dissolves once the energy supply is interrupted.",
        "The membrane potential is maintained by the cell wall, which is lost without "
        "energy.",
        "Aquaporins stop carrying water, which is what generates the membrane potential.",
        "The membrane potential rises rather than falls when energy is interrupted."],
      ans=0,
      why="EK 2.8.A.1 ii names the sodium-potassium pump and ATPase as contributors to the "
          "maintenance of the membrane potential, and EK 2.8.A.1 makes metabolic energy "
          "required for active transport and for maintaining electrochemical gradients. "
          "Aquaporins carry water under EK 2.6.A.3 and are not tied to the potential."),

 dict(q="Which pair of requirements does the course framework attach to active transport "
        "in this topic?",
      choices=[
        "A direct input of metabolic energy and the presence of membrane proteins",
        "A direct input of metabolic energy and the absence of membrane proteins",
        "The absence of an energy input and the presence of membrane proteins",
        "The absence of both an energy input and membrane proteins",
        "Only the presence of a concentration gradient"],
      ans=0,
      why="EK 2.8.A.1 requires metabolic energy for active transport and EK 2.8.A.1 i "
          "states that membrane proteins are necessary for it, so both requirements come "
          "from the same statement group."),

 dict(q="Which summary of this topic matches the course framework?",
      choices=[
        "Metabolic energy such as that from ATP drives active transport and both "
        "establishes and maintains electrochemical gradients; membrane proteins are "
        "necessary; and the sodium-potassium pump and ATPase help maintain the membrane "
        "potential.",
        "Metabolic energy is needed only to establish gradients; membrane proteins are "
        "unnecessary; and the sodium-potassium pump abolishes the membrane potential.",
        "Metabolic energy drives passive transport; membrane proteins are necessary; and "
        "aquaporins maintain the membrane potential.",
        "Metabolic energy is not required for any transport process; membrane proteins "
        "act alone.",
        "Metabolic energy is required only where a cell wall is present, and the pump "
        "acts only in walled cells."],
      ans=0,
      why="The three parts come from one statement and its two sub-points: EK 2.8.A.1 for "
          "the energy requirement covering active transport and the establishment and "
          "maintenance of electrochemical gradients, EK 2.8.A.1 i for the necessity of "
          "membrane proteins, and EK 2.8.A.1 ii for the pump and ATPase contributing to "
          "the maintenance of the membrane potential."),
]
