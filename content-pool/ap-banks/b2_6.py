# AP BIOLOGY 2.6 Facilitated Diffusion
# CED effective Fall 2025, Unit 2 Cells. Big Idea 2 Energetics.
# Learning objective 2.6.A: explain how the structure of a molecule affects its ability
# to pass through the plasma membrane.
# Suggested skill 6.E, predict the causes or effects of a change in, or disruption to,
# one or more components in a biological system.
#
# Essential knowledge relied on, in the framework's own words:
#   2.6.A.1    Facilitated diffusion requires transport or channel proteins to enable
#              the movement of charged ions across the membrane.
#     i.       Membranes may become polarized by the movement of ions across the
#              membrane.
#     ii.      Charged ions, including sodium and potassium, require channel proteins
#              to move through the membrane.
#   2.6.A.2    Facilitated diffusion enables the movement of large polar molecules
#              through membranes with no energy input. In this type of diffusion,
#              substances move down the concentration gradient.
#   2.6.A.3    Aquaporins transport large quantities of water across membranes.
#
# ON THE CHAIN TO 2.5. EK 2.6.A.2 says facilitated diffusion happens with NO ENERGY
# INPUT and DOWN THE CONCENTRATION GRADIENT, which are exactly the two clauses EK
# 2.5.A.2 uses to define passive transport. Items that call facilitated diffusion a
# passive process therefore chain those two statements rather than asserting anything
# new, and every such claim in verify_b2_6.py says so.
#
# ON SCOPE. The pumps, ATPases and electrochemical gradients are topic 2.8 and tonicity
# is 2.7. No item here asks about a pump or about water potential. EK 2.6.A.1 i is the
# only place polarization appears in this topic and it is keyed only as far as that
# sentence goes.
#
# ON NOTATION. The CED prints the two ions as chemical symbols with a charge. Biology
# is exported as prose with no typesetting, so this bank names them in words.
#
# ON THE DATA. Every table is labelled hypothetical, and every keyed conclusion is
# recoverable from the table alone and recomputed in verify_b2_6.py.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: Biology is exported as prose.
TOPIC = ("2.6", "Facilitated Diffusion", 2)

_T_CHANNEL = dict(
    headers=["Condition (hypothetical)",
             "Rate of potassium ion movement across the membrane (arbitrary units)",
             "Rate of oxygen movement across the membrane (arbitrary units)"],
    rows=[["Channel proteins present", "320", "95"],
          ["Channel proteins absent", "2", "94"]])

_T_AQUA = dict(
    headers=["Cell line (hypothetical)", "Aquaporins per cell (thousands)",
             "Water crossing the membrane per minute (arbitrary units)"],
    rows=[["Line 1", "0", "6"],
          ["Line 2", "20", "118"],
          ["Line 3", "40", "240"],
          ["Line 4", "60", "352"]])

_T_ENERGY = dict(
    headers=["Treatment (hypothetical)",
             "Rate of glucose entry by facilitated diffusion (arbitrary units)"],
    rows=[["Untreated cells", "210"],
          ["Cells with ATP synthesis blocked", "204"]])

_T_GRAD = dict(
    headers=["Time (minutes)", "Glucose concentration outside the cell (millimolar)",
             "Glucose concentration inside the cell (millimolar)"],
    rows=[["0", "20", "2"],
          ["10", "15", "7"],
          ["20", "12", "10"],
          ["30", "11", "11"]])

QUESTIONS = [

 dict(q="What does the course framework say facilitated diffusion requires in order to "
        "move charged ions across a membrane?",
      choices=[
        "Transport or channel proteins",
        "A direct input of metabolic energy",
        "The removal of the membrane's hydrophobic interior",
        "The formation of new vesicles at the membrane",
        "The presence of a cell wall outside the membrane"],
      ans=0,
      why="EK 2.6.A.1 states that facilitated diffusion requires transport or channel "
          "proteins to enable the movement of charged ions across the membrane. EK "
          "2.6.A.2 separately says the process happens with no energy input, so the "
          "energy option contradicts the same statement group."),

 dict(q="Which charged ions does the course framework name as requiring channel proteins "
        "to move through the membrane?",
      choices=["Sodium and potassium", "Oxygen and nitrogen", "Water and ammonia",
               "Glucose and starch", "Carbon dioxide and oxygen"],
      ans=0,
      why="EK 2.6.A.1 ii states that charged ions, including sodium and potassium, "
          "require channel proteins to move through the membrane. Oxygen, nitrogen and "
          "carbon dioxide are the small nonpolar molecules EK 2.4.A.2 says pass freely, "
          "and water and ammonia are EK 2.4.A.3's small polar uncharged case."),

 dict(q="What does the course framework say may happen to a membrane as a result of ions "
        "moving across it?",
      choices=[
        "The membrane may become polarized.",
        "The membrane may lose its phospholipids.",
        "The membrane may become freely permeable to every substance.",
        "The membrane may fold in on itself to form vesicles.",
        "The membrane may become a cell wall."],
      ans=0,
      why="EK 2.6.A.1 i states that membranes may become polarized by the movement of "
          "ions across the membrane. Vesicle formation belongs to endocytosis under EK "
          "2.5.B.1 i, and nothing in this topic makes a membrane freely permeable."),

 dict(q="What does the course framework say facilitated diffusion does for large polar "
        "molecules?",
      choices=[
        "It enables their movement through membranes with no energy input.",
        "It enables their movement through membranes using a direct energy input.",
        "It prevents their movement through membranes entirely.",
        "It converts them into small nonpolar molecules first.",
        "It moves them only inside newly formed vesicles."],
      ans=0,
      why="EK 2.6.A.2 states that facilitated diffusion enables the movement of large "
          "polar molecules through membranes with no energy input. A direct energy input "
          "is what EK 2.5.A.3 assigns to active transport instead."),

 dict(q="In which direction do substances move during facilitated diffusion?",
      choices=[
        "Down the concentration gradient",
        "Up the concentration gradient",
        "In whichever direction the cell's energy supply pushes them",
        "Always into the cell, regardless of concentration",
        "Always out of the cell, regardless of concentration"],
      ans=0,
      why="EK 2.6.A.2 states that in this type of diffusion substances move down the "
          "concentration gradient. Movement up a gradient is what EK 2.5.A.3 reserves for "
          "the energy-requiring case."),

 dict(q="What does the course framework say aquaporins do?",
      choices=[
        "They transport large quantities of water across membranes.",
        "They transport large quantities of sodium and potassium across membranes.",
        "They synthesize water inside the cell.",
        "They prevent water from crossing the membrane at all.",
        "They form the structural framework of the membrane."],
      ans=0,
      why="EK 2.6.A.3 states that aquaporins transport large quantities of water across "
          "membranes. Sodium and potassium are the ions EK 2.6.A.1 ii routes through "
          "channel proteins, and the membrane's framework is phospholipid under EK "
          "2.3.B.1."),

 dict(q="Why does a charged ion need a channel protein rather than crossing the bilayer "
        "directly?",
      choices=[
        "The nonpolar hydrocarbon tails in the membrane interior prevent the movement of "
        "ions.",
        "The polar phosphate regions at the membrane surface prevent the movement of "
        "ions.",
        "Ions are too large to fit between two phospholipid molecules.",
        "Ions can only move when a direct energy input is supplied.",
        "Ions are repelled by the carbohydrate chains of the glycolipids."],
      ans=0,
      why="EK 2.4.A.3 states that the nonpolar hydrocarbon tails of phospholipids prevent "
          "the movement of ions and polar molecules across the membrane, which is why EK "
          "2.6.A.1 ii routes charged ions through channel proteins instead. The phosphate "
          "regions face the aqueous environments rather than the interior."),

 dict(q="On the course framework's own definitions, is facilitated diffusion a passive or "
        "an active process, and why?",
      choices=[
        "Passive, because it occurs with no energy input and moves substances down the "
        "concentration gradient",
        "Active, because it requires proteins embedded in the membrane",
        "Active, because it occurs with no energy input",
        "Passive, because it moves substances up the concentration gradient",
        "Neither, because the framework's passive and active categories do not apply to "
        "diffusion"],
      ans=0,
      why="EK 2.6.A.2 gives facilitated diffusion both of the clauses EK 2.5.A.2 uses to "
          "define passive transport: no energy input, and movement down the concentration "
          "gradient. Requiring a protein is not what EK 2.5.A.3 makes a process active; a "
          "direct input of energy is."),

 dict(q="How does facilitated diffusion differ from the process the framework calls "
        "active transport?",
      choices=[
        "Facilitated diffusion needs no energy input and follows the gradient, while "
        "active transport takes a direct energy input and can run against it.",
        "Facilitated diffusion takes a direct energy input and runs against the gradient, "
        "while active transport needs no energy input.",
        "Facilitated diffusion uses membrane proteins and active transport does not.",
        "Facilitated diffusion moves only ions and active transport moves only water.",
        "There is no difference between the two processes."],
      ans=0,
      why="EK 2.6.A.2 gives facilitated diffusion no energy input and movement down the "
          "gradient, while EK 2.5.A.3 gives active transport a direct input of energy and "
          "in some cases movement from low concentration to high. Both processes use "
          "membrane proteins, so that is not what separates them."),

 dict(q="A compound blocks every channel protein in a cell's membrane. Which prediction "
        "follows most directly from the course framework?",
      choices=[
        "The movement of charged ions such as sodium and potassium across the membrane "
        "will fall sharply.",
        "The movement of small nonpolar molecules such as oxygen will fall sharply.",
        "The membrane will lose its phospholipid framework.",
        "The cell will begin to move ions up their concentration gradient instead.",
        "Nothing will change, because ions cross the membrane without proteins."],
      ans=0,
      why="EK 2.6.A.1 ii states that charged ions, including sodium and potassium, "
          "require channel proteins to move through the membrane, so blocking those "
          "proteins removes the route. Small nonpolar molecules pass freely under EK "
          "2.4.A.2 and do not use that route."),

 dict(q="A cell's aquaporins are all blocked. Which outcome does the course framework "
        "support as a prediction?",
      choices=[
        "The cell will no longer move large quantities of water across its membrane "
        "quickly.",
        "The cell will move water across its membrane more quickly than before.",
        "The cell will lose its ability to move sodium and potassium.",
        "The cell will begin to synthesize water internally instead.",
        "The membrane will become impermeable to every substance."],
      ans=0,
      why="EK 2.6.A.3 states that aquaporins transport large quantities of water across "
          "membranes, so blocking them removes the high-volume route. EK 2.4.A.3 still "
          "allows water, as a small polar uncharged molecule, to pass in small amounts, "
          "which is why the prediction is about quantity rather than about total "
          "exclusion."),

 dict(q="A cell's ability to make usable energy is destroyed. What does the course "
        "framework predict for facilitated diffusion?",
      choices=[
        "It will continue, because it occurs with no energy input.",
        "It will stop, because it requires a direct energy input.",
        "It will reverse direction, moving substances up their gradients.",
        "It will continue only for small nonpolar molecules.",
        "It will be replaced by endocytosis."],
      ans=0,
      why="EK 2.6.A.2 states that facilitated diffusion enables the movement of large "
          "polar molecules through membranes with no energy input, so a loss of usable "
          "energy does not remove the driver. Movement up a gradient is EK 2.5.A.3's "
          "energy-requiring case."),

 dict(q="The table compares the movement of two substances across a membrane with and "
        "without channel proteins. Which conclusion is best supported?",
      table=_T_CHANNEL,
      choices=[
        "Potassium ion movement depends on the channel proteins while oxygen movement "
        "does not.",
        "Oxygen movement depends on the channel proteins while potassium ion movement "
        "does not.",
        "Both substances depend equally on the channel proteins.",
        "Neither substance depends on the channel proteins.",
        "Removing the channel proteins increased the movement of both substances."],
      ans=0,
      why="Potassium ion movement falls to a tiny fraction of its original rate when the "
          "channel proteins are removed while oxygen movement is essentially unchanged. "
          "EK 2.6.A.1 ii requires channel proteins for charged ions and EK 2.4.A.2 lets "
          "small nonpolar molecules pass freely."),

 dict(q="Using the same measurements, which substance's movement is essentially "
        "unaffected by removing the channel proteins, and why does the framework expect "
        "that?",
      table=_T_CHANNEL,
      choices=[
        "Oxygen, because small nonpolar molecules freely pass across the membrane",
        "Oxygen, because it is a charged ion that uses a separate route",
        "The potassium ion, because small nonpolar molecules freely pass across the "
        "membrane",
        "The potassium ion, because aquaporins carry it instead",
        "Both substances, because neither uses a membrane protein"],
      ans=0,
      why="The oxygen rate barely changes between the two conditions in the table, and EK "
          "2.4.A.2 states that small nonpolar molecules including oxygen freely pass "
          "across the membrane. Oxygen is not an ion and aquaporins carry water under EK "
          "2.6.A.3, not potassium."),

 dict(q="Four cell lines differing in the number of aquaporins per cell were measured for "
        "water movement, with the results in the table. Which conclusion is best "
        "supported?",
      table=_T_AQUA,
      choices=[
        "Water movement increased as the number of aquaporins increased.",
        "Water movement decreased as the number of aquaporins increased.",
        "Water movement was unrelated to the number of aquaporins.",
        "Water movement was greatest in the line with no aquaporins.",
        "Water movement was the same in all four lines."],
      ans=0,
      why="Water movement rises at every step as the aquaporin count rises across the "
          "four lines. EK 2.6.A.3 states that aquaporins transport large quantities of "
          "water across membranes, which is the relationship the data record."),

 dict(q="Using the same four lines, how does the amount of water crossing per aquaporin "
        "behave as the number of aquaporins rises?",
      table=_T_AQUA,
      choices=[
        "It stays roughly constant, so the total rises in proportion to the number of "
        "aquaporins.",
        "It roughly doubles at each step, so the total rises faster than the number of "
        "aquaporins.",
        "It roughly halves at each step, so the total rises more slowly than the number "
        "of aquaporins.",
        "It falls to zero once the number of aquaporins exceeds twenty thousand.",
        "It cannot be calculated from the values given."],
      ans=0,
      why="Dividing the water movement by the aquaporin count gives nearly the same value "
          "for each line that has aquaporins, so the total scales with the count. That is "
          "what makes the aquaporins the route responsible under EK 2.6.A.3 rather than "
          "an incidental correlate."),

 dict(q="One line in the aquaporin table has no aquaporins at all yet still shows some "
        "water crossing its membrane. Which explanation fits the course framework?",
      table=_T_AQUA,
      choices=[
        "Water is a small polar uncharged molecule and passes through the membrane in "
        "small amounts without aquaporins.",
        "Water is a small nonpolar molecule and passes freely without aquaporins.",
        "Water is a charged ion and passes through channel proteins instead.",
        "The measurement must be an error, because water cannot cross without "
        "aquaporins.",
        "The line must contain aquaporins that were not counted."],
      ans=0,
      why="EK 2.4.A.3 states that small polar, uncharged molecules like water pass "
          "through the membrane in small amounts, and the tabulated value for that line "
          "is small next to every line with aquaporins. EK 2.6.A.3 makes aquaporins the "
          "route for LARGE quantities, not the only route of any kind."),

 dict(q="Glucose entry by facilitated diffusion was measured with and without ATP "
        "synthesis blocked, with the results in the table. Which conclusion is best "
        "supported?",
      table=_T_ENERGY,
      choices=[
        "Facilitated diffusion of glucose proceeds without a direct energy input.",
        "Facilitated diffusion of glucose requires a direct energy input.",
        "Blocking ATP synthesis stopped glucose entry entirely.",
        "Blocking ATP synthesis more than doubled glucose entry.",
        "The result shows that glucose crosses the membrane without any protein."],
      ans=0,
      why="The two rates differ by only a few percent, so removing the energy supply did "
          "not remove the driver. EK 2.6.A.2 states that facilitated diffusion enables "
          "movement through membranes with no energy input, and EK 2.6.A.1 still requires "
          "a protein, which this measurement does not test."),

 dict(q="The table follows the glucose concentration on each side of a membrane over half "
        "an hour while glucose enters by facilitated diffusion. Which statement describes "
        "the net movement?",
      table=_T_GRAD,
      choices=[
        "Glucose moved from the side where it was more concentrated toward the side where "
        "it was less concentrated.",
        "Glucose moved from the side where it was less concentrated toward the side where "
        "it was more concentrated.",
        "Glucose moved in both directions at equal rates from the start.",
        "Glucose concentration rose on both sides of the membrane.",
        "Glucose concentration fell on both sides of the membrane."],
      ans=0,
      why="The outside concentration falls while the inside concentration rises across "
          "the four time points, so the net movement runs from the more concentrated side "
          "to the less concentrated one. EK 2.6.A.2 states that in this type of diffusion "
          "substances move down the concentration gradient."),

 dict(q="What has happened by the last time point in the same table, and what does it "
        "imply about further net movement?",
      table=_T_GRAD,
      choices=[
        "The two concentrations have become equal, so there is no longer a gradient to "
        "drive net movement.",
        "The inside concentration has risen above the outside concentration, which shows "
        "an energy input was supplied.",
        "The outside concentration has fallen to zero, so no glucose remains to move.",
        "The two concentrations are still far apart, so net movement is unchanged.",
        "The measurement cannot be interpreted without knowing the number of transport "
        "proteins."],
      ans=0,
      why="The last row records the same value on both sides. EK 2.6.A.2 makes movement "
          "in this process follow the concentration gradient, so once the gradient is "
          "gone there is nothing left to drive net movement; going beyond equality would "
          "require the energy input EK 2.5.A.3 describes."),

 dict(q="Which two kinds of substance does the course framework place in the care of "
        "facilitated diffusion?",
      choices=[
        "Charged ions and large polar molecules",
        "Small nonpolar molecules and charged ions",
        "Small nonpolar molecules and large polar molecules",
        "Only water",
        "Only substances moving up their concentration gradients"],
      ans=0,
      why="EK 2.6.A.1 assigns charged ions to transport or channel proteins and EK "
          "2.6.A.2 assigns large polar molecules to the same process. Small nonpolar "
          "molecules cross freely under EK 2.4.A.2 and need no facilitation."),

 dict(q="Which substance would be expected NOT to depend on facilitated diffusion to "
        "cross a plasma membrane?",
      choices=["Carbon dioxide", "The sodium ion", "The potassium ion",
               "A large polar sugar molecule", "A large charged molecule"],
      ans=0,
      why="EK 2.4.A.2 states that small nonpolar molecules including carbon dioxide "
          "freely pass across the membrane, so no protein is needed. EK 2.6.A.1 ii and EK "
          "2.6.A.2 place ions and large polar molecules in the facilitated category."),

 dict(q="According to the course framework, what may cause a membrane to become "
        "polarized?",
      choices=[
        "The movement of ions across the membrane",
        "The movement of small nonpolar molecules across the membrane",
        "The movement of water through aquaporins",
        "The folding of the membrane into vesicles",
        "The loss of the membrane's embedded proteins"],
      ans=0,
      why="EK 2.6.A.1 i states that membranes may become polarized by the movement of "
          "ions across the membrane. The framework attaches polarization to no other "
          "movement in this topic, and water and small nonpolar molecules carry no "
          "charge."),

 dict(q="Which statement about the proteins involved in facilitated diffusion is accurate "
        "on the framework's own terms?",
      choices=[
        "They enable movement across the membrane, but their involvement does not make "
        "the process require energy.",
        "They enable movement across the membrane, and their involvement is what makes "
        "the process require energy.",
        "They prevent movement across the membrane and must be removed for diffusion to "
        "occur.",
        "They are needed only for small nonpolar molecules.",
        "They move substances only against the concentration gradient."],
      ans=0,
      why="EK 2.6.A.1 requires transport or channel proteins and EK 2.6.A.2 states in the "
          "same breath that the process happens with no energy input and down the "
          "concentration gradient. Needing a protein and needing energy are therefore "
          "separate matters in the framework."),

 dict(q="A student states that facilitated diffusion is a kind of active transport "
        "because it uses membrane proteins. What is the best correction?",
      choices=[
        "What makes a process active is a direct input of energy, and facilitated "
        "diffusion occurs with no energy input.",
        "What makes a process active is the use of membrane proteins, so the student is "
        "correct.",
        "Facilitated diffusion moves substances up their concentration gradients, which "
        "is what makes it active.",
        "Active transport does not use membrane proteins at all, which is the student's "
        "error.",
        "Facilitated diffusion is neither passive nor active, because it applies only to "
        "water."],
      ans=0,
      why="EK 2.5.A.3 defines active transport by the direct input of energy, and EK "
          "2.6.A.2 states that facilitated diffusion occurs with no energy input and down "
          "the concentration gradient. Membrane proteins are used in both, so their "
          "presence cannot be what distinguishes them."),

 dict(q="How does the role of aquaporins relate to the framework's earlier statement that "
        "water passes through the membrane in small amounts?",
      choices=[
        "Water can cross in small amounts without help, and aquaporins are what allow "
        "large quantities to cross.",
        "Water cannot cross at all without aquaporins, so the earlier statement applies "
        "only to ammonia.",
        "Aquaporins reduce the amount of water that crosses, which is why the amount is "
        "small.",
        "Aquaporins carry water only against its concentration gradient.",
        "Aquaporins and the earlier statement describe two different substances."],
      ans=0,
      why="EK 2.4.A.3 allows water, as a small polar uncharged molecule, to pass through "
          "the membrane in small amounts, and EK 2.6.A.3 states that aquaporins transport "
          "large quantities of water across membranes. The two statements describe the "
          "same substance at two different scales."),

 dict(q="A tissue must move very large volumes of water across its cell membranes "
        "rapidly. Which feature would be most useful, and on what grounds?",
      choices=[
        "Many aquaporins, because the framework assigns the transport of large quantities "
        "of water to them",
        "Many channel proteins for sodium, because the framework assigns water transport "
        "to them",
        "A thicker hydrophobic interior, because it speeds the passage of polar "
        "molecules",
        "Fewer embedded proteins, because proteins slow the passage of water",
        "A cell wall, because it admits water selectively"],
      ans=0,
      why="EK 2.6.A.3 states that aquaporins transport large quantities of water across "
          "membranes. EK 2.6.A.1 ii assigns sodium channels to ions rather than water, and "
          "EK 2.4.A.3 makes the hydrophobic interior what restricts polar molecules rather "
          "than what speeds them."),

 dict(q="A researcher wants to show that a particular membrane protein is required for a "
        "solute to enter a cell. Which comparison is most informative?",
      choices=[
        "Entry of the solute into cells with the protein present and into otherwise "
        "identical cells lacking it",
        "Entry of the solute into cells with the protein present, measured at several "
        "different times",
        "Entry of two different solutes into cells with the protein present",
        "Entry of the solute into cells with the protein present and into cells of a "
        "different species lacking many proteins",
        "The total number of proteins in the membrane before and after the solute is "
        "added"],
      ans=0,
      why="A requirement claim needs the protein to be the only difference between "
          "otherwise identical preparations, which is what the keyed comparison supplies. "
          "Comparing across species or across solutes changes more than one thing at once, "
          "and a time course with the protein always present has no contrast at all."),

 dict(q="Which observation would best distinguish facilitated diffusion of a substance "
        "from its free passage through the bilayer?",
      choices=[
        "Movement of the substance falls sharply when its membrane proteins are blocked, "
        "even though no energy supply has been removed.",
        "Movement of the substance falls sharply when the cell's energy supply is "
        "removed, even though its membrane proteins are intact.",
        "Movement of the substance follows the concentration gradient.",
        "Movement of the substance occurs across an intact plasma membrane.",
        "Movement of the substance is faster at a higher temperature."],
      ans=0,
      why="EK 2.6.A.1 makes the protein requirement the distinctive feature of facilitated "
          "diffusion, while EK 2.6.A.2 shares the no-energy and down-the-gradient features "
          "with the free passage EK 2.4.A.2 grants small nonpolar molecules. Sensitivity "
          "to losing energy would point instead to EK 2.5.A.3's active case."),

 dict(q="Which summary of facilitated diffusion matches the course framework?",
      choices=[
        "It uses transport or channel proteins, needs no energy input, moves substances "
        "down the concentration gradient, and includes the aquaporin route for water.",
        "It uses transport or channel proteins, needs a direct energy input, and moves "
        "substances up the concentration gradient.",
        "It needs no proteins, no energy input, and moves substances down the "
        "concentration gradient.",
        "It uses transport or channel proteins, needs no energy input, and moves "
        "substances up the concentration gradient.",
        "It applies only to small nonpolar molecules and requires no proteins."],
      ans=0,
      why="The four parts come from three statements: EK 2.6.A.1 for the protein "
          "requirement, EK 2.6.A.2 for no energy input and movement down the gradient, and "
          "EK 2.6.A.3 for aquaporins carrying large quantities of water."),
]
