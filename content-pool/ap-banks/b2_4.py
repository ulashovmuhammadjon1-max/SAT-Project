# AP BIOLOGY 2.4 Membrane Permeability
# CED effective Fall 2025, Unit 2 Cells. Big Idea 2 Energetics.
# Learning objectives 2.4.A, explain how the structure of biological membranes
# influences selective permeability, and 2.4.B, describe the role of the cell wall in
# maintaining cell structure and function.
# Suggested skill 5.D, use data to evaluate a hypothesis or prediction, including
# rejecting or failing to reject the null hypothesis.
#
# Essential knowledge relied on, in the framework's own words:
#   2.4.A.1    Plasma membranes separate the internal environment of the cell from the
#              external environment. Selective permeability is the result of the plasma
#              membrane having a hydrophobic interior.
#   2.4.A.2    Small nonpolar molecules, including nitrogen, oxygen, and carbon
#              dioxide, freely pass across the membrane. Hydrophilic substances, such
#              as large polar molecules and ions, move across the membrane through
#              embedded channels and transport proteins.
#   2.4.A.3    The nonpolar hydrocarbon tails of phospholipids prevent the movement of
#              ions and polar molecules across the membrane. Small polar, uncharged
#              molecules, like water or ammonia, pass through the membrane in small
#              amounts.
#   2.4.B.1    Cell walls of Bacteria, Archaea, Fungi, and plants provide a structural
#              boundary as well as a permeability barrier for some substances to the
#              internal or external cellular environments and protection from osmotic
#              lysis.
#
# ON SCOPE. This topic is WHAT CAN CROSS and why. The named transport mechanisms are
# topics 2.5, 2.6 and 2.8 and tonicity is 2.7; no item here asks for the name of a
# transport process or for the direction of a gradient. Items that mention channels or
# transport proteins do so only because EK 2.4.A.2 names them as the route hydrophilic
# substances take.
#
# ON NOTATION. The CED prints the gases and the small polar molecules as chemical
# formulas. Biology is exported as prose with no typesetting, so this bank names them
# in words throughout.
#
# ON THE DATA. Every table is labelled hypothetical in its stem, and every keyed
# conclusion is recoverable from the table alone and recomputed in verify_b2_4.py.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: Biology is exported as prose.
TOPIC = ("2.4", "Membrane Permeability", 2)

_T_PERM = dict(
    headers=["Substance", "Chemical description",
             "Rate of movement across a protein-free artificial phospholipid bilayer "
             "(arbitrary units)"],
    rows=[["Oxygen", "small nonpolar", "9,600"],
          ["Carbon dioxide", "small nonpolar", "4,500"],
          ["Water", "small polar and uncharged", "62"],
          ["Glucose", "large polar", "0.4"],
          ["Sodium ion", "charged", "0.0002"]])

_T_NULL_SOLUTE = dict(
    headers=["Treatment (hypothetical)",
             "Mean amount of a large polar solute entering the cells in ten minutes "
             "(arbitrary units)"],
    rows=[["Transport proteins functional", "148"],
          ["Transport proteins blocked", "6"]])

_T_NULL_OXYGEN = dict(
    headers=["Treatment (hypothetical)",
             "Mean amount of oxygen entering the cells in ten minutes (arbitrary units)"],
    rows=[["Transport proteins functional", "96"],
          ["Transport proteins blocked", "94"]])

_T_WALL = dict(
    headers=["Preparation (hypothetical)", "Treatment of the cell wall",
             "Percentage of cells that burst in distilled water within twenty minutes"],
    rows=[["Preparation 1", "wall left intact", "2"],
          ["Preparation 2", "wall enzymatically removed", "87"]])

QUESTIONS = [

 dict(q="What does the course framework say a plasma membrane does for a cell?",
      choices=[
        "It separates the internal environment of the cell from the external "
        "environment.",
        "It synthesizes the proteins the cell needs from messenger RNA sequences.",
        "It stores the cell's hereditary information as a sequence of nucleotides.",
        "It supplies the cell with all of the energy it uses.",
        "It digests material the cell has taken in from outside."],
      ans=0,
      why="EK 2.4.A.1 opens by stating that plasma membranes separate the internal "
          "environment of the cell from the external environment. The rejected options "
          "are the functions the framework assigns to ribosomes, nucleic acids and "
          "lysosomes in EK 2.1.A.1, EK 1.6.A.1 and EK 2.1.A.6."),

 dict(q="What does the course framework identify as the source of a plasma membrane's "
        "selective permeability?",
      choices=[
        "The membrane having a hydrophobic interior",
        "The membrane having a hydrophilic interior",
        "The number of embedded proteins the membrane contains",
        "The presence of a cell wall outside the membrane",
        "The total surface area of the membrane"],
      ans=0,
      why="EK 2.4.A.1 states that selective permeability is the result of the plasma "
          "membrane having a hydrophobic interior. A hydrophilic interior would be the "
          "opposite claim, and the cell wall is treated separately in EK 2.4.B.1."),

 dict(q="Which group of substances does the course framework say freely passes across the "
        "membrane?",
      choices=[
        "Small nonpolar molecules such as nitrogen, oxygen and carbon dioxide",
        "Large polar molecules such as glucose",
        "Charged ions such as sodium and potassium",
        "Any molecule small enough to fit between two phospholipids",
        "Only molecules that carry a phosphate group"],
      ans=0,
      why="EK 2.4.A.2 states that small nonpolar molecules, including nitrogen, oxygen, "
          "and carbon dioxide, freely pass across the membrane. Large polar molecules and "
          "ions are placed in the second half of the same statement as substances that "
          "need embedded channels and transport proteins."),

 dict(q="By what route does the course framework say hydrophilic substances cross the "
        "membrane?",
      choices=[
        "Through embedded channels and transport proteins",
        "Directly through the hydrophobic interior of the bilayer",
        "Through gaps that open between neighbouring phospholipids",
        "Through the cell wall, which admits them selectively",
        "They do not cross the membrane by any route."],
      ans=0,
      why="EK 2.4.A.2 states that hydrophilic substances, such as large polar molecules "
          "and ions, move across the membrane through embedded channels and transport "
          "proteins. EK 2.4.A.3 explicitly denies the direct route by saying the nonpolar "
          "hydrocarbon tails prevent the movement of ions and polar molecules."),

 dict(q="Which part of the membrane does the course framework credit with preventing the "
        "movement of ions and polar molecules?",
      choices=[
        "The nonpolar hydrocarbon tails of the phospholipids",
        "The polar phosphate regions of the phospholipids",
        "The carbohydrate chains of the glycolipids",
        "The cell wall surrounding the membrane",
        "The embedded transport proteins"],
      ans=0,
      why="EK 2.4.A.3 states that the nonpolar hydrocarbon tails of phospholipids prevent "
          "the movement of ions and polar molecules across the membrane. The embedded "
          "transport proteins are what EK 2.4.A.2 offers as the route those substances "
          "take instead, so they permit rather than prevent."),

 dict(q="What does the course framework say about small polar, uncharged molecules such "
        "as water and ammonia?",
      choices=[
        "They pass through the membrane in small amounts.",
        "They pass through the membrane as freely as small nonpolar molecules do.",
        "They cannot cross the membrane at all under any circumstances.",
        "They cross only through the cell wall.",
        "They cross only when the membrane loses its hydrophobic interior."],
      ans=0,
      why="EK 2.4.A.3 states that small polar, uncharged molecules, like water or "
          "ammonia, pass through the membrane in small amounts. That is a middle case "
          "between the free passage EK 2.4.A.2 grants small nonpolar molecules and the "
          "prevention EK 2.4.A.3 applies to ions and polar molecules."),

 dict(q="Which groups of organisms does the course framework name as having cell walls?",
      choices=[
        "Bacteria, Archaea, Fungi and plants",
        "Animals, Fungi and plants",
        "Bacteria and animals only",
        "Plants only",
        "All organisms without exception"],
      ans=0,
      why="EK 2.4.B.1 names the cell walls of Bacteria, Archaea, Fungi, and plants. "
          "Animals are not on that list, so any option including them or extending the "
          "list to all organisms overstates it."),

 dict(q="What does the course framework say a cell wall provides?",
      choices=[
        "A structural boundary, a permeability barrier for some substances, and "
        "protection from osmotic lysis",
        "A hydrophobic interior that produces selective permeability",
        "The embedded channels through which ions cross into the cell",
        "The site at which aerobic cellular respiration takes place",
        "A store of hydrolytic enzymes used to digest material"],
      ans=0,
      why="EK 2.4.B.1 states that cell walls provide a structural boundary as well as a "
          "permeability barrier for some substances and protection from osmotic lysis. "
          "The hydrophobic interior belongs to the plasma membrane under EK 2.4.A.1 and "
          "the channels to the membrane's embedded proteins under EK 2.4.A.2."),

 dict(q="The table gives the rate at which five substances cross a protein-free "
        "artificial phospholipid bilayer. Which substance crossed most readily, and what "
        "is its chemical description?",
      table=_T_PERM,
      choices=[
        "Oxygen, which is small and nonpolar",
        "Water, which is small, polar and uncharged",
        "Glucose, which is large and polar",
        "The sodium ion, which is charged",
        "Carbon dioxide, which is large and polar"],
      ans=0,
      why="The largest rate in the table belongs to a substance the same row describes as "
          "small and nonpolar, which is the category EK 2.4.A.2 says freely passes across "
          "the membrane. The final option misdescribes a substance the table calls small "
          "and nonpolar."),

 dict(q="Among the same five substances, which crossed the protein-free bilayer least "
        "readily?",
      table=_T_PERM,
      choices=["The sodium ion", "Glucose", "Water", "Oxygen", "Carbon dioxide"],
      ans=0,
      why="The smallest rate in the table belongs to the row the table describes as "
          "charged. EK 2.4.A.3 states that the nonpolar hydrocarbon tails of "
          "phospholipids prevent the movement of ions across the membrane, which is why "
          "the charged substance is last."),

 dict(q="Where does water fall among the five substances in the table, and how does that "
        "fit the course framework?",
      table=_T_PERM,
      choices=[
        "Below the small nonpolar molecules but above the large polar molecule and the "
        "ion, which matches passage in small amounts",
        "Above every other substance in the table, which matches free passage",
        "Below every other substance in the table, which matches complete exclusion",
        "Equal to the small nonpolar molecules, which matches free passage",
        "Equal to the charged ion, which matches complete exclusion"],
      ans=0,
      why="The tabulated rate for water lies between the two small nonpolar rows and the "
          "large polar and charged rows. EK 2.4.A.3 states that small polar, uncharged "
          "molecules pass through the membrane in small amounts, which is exactly an "
          "intermediate position."),

 dict(q="Which two substances in the table would most need embedded channels or transport "
        "proteins in order to enter a real cell at a useful rate?",
      table=_T_PERM,
      choices=[
        "Glucose and the sodium ion",
        "Oxygen and carbon dioxide",
        "Water and oxygen",
        "Carbon dioxide and glucose",
        "None of them, because all five crossed the artificial bilayer"],
      ans=0,
      why="EK 2.4.A.2 assigns embedded channels and transport proteins to hydrophilic "
          "substances such as large polar molecules and ions, and the table's two lowest "
          "rates belong to exactly the rows it describes as large polar and as charged. A "
          "measurable rate is not the same as a useful one, which is why the final option "
          "fails."),

 dict(q="Using the same measurements, about how many times as fast did oxygen cross the "
        "artificial bilayer compared with carbon dioxide?",
      table=_T_PERM,
      choices=["About twice as fast", "About half as fast", "About ten times as fast",
               "About a hundred times as fast", "At almost exactly the same rate"],
      ans=0,
      why="Dividing the oxygen rate by the carbon dioxide rate gives the comparison "
          "directly from the table. Both rows are described as small and nonpolar, which "
          "is why they sit far above the other three under EK 2.4.A.2 even though they "
          "differ from each other."),

 dict(q="Cells were tested for the entry of a large polar solute with their transport "
        "proteins functional and with those proteins blocked, with the results in the "
        "table. What should be concluded about the null hypothesis that blocking the "
        "proteins makes no difference to the entry of this solute?",
      table=_T_NULL_SOLUTE,
      choices=[
        "It should be rejected, because entry fell to a small fraction of its untreated "
        "value.",
        "It should not be rejected, because entry fell to a small fraction of its "
        "untreated value.",
        "It should be rejected, because entry rose when the proteins were blocked.",
        "It should not be rejected, because the two treatments gave nearly the same "
        "result.",
        "No conclusion is possible, because a null hypothesis cannot be tested with two "
        "treatments."],
      ans=0,
      why="The two tabulated means differ by more than an order of magnitude in the "
          "direction the blocking predicts, so the no-difference hypothesis does not "
          "survive. EK 2.4.A.2 assigns hydrophilic substances such as large polar "
          "molecules to embedded channels and transport proteins, which is the mechanism "
          "the result supports."),

 dict(q="In the same investigation, what does the null hypothesis actually assert?",
      table=_T_NULL_SOLUTE,
      choices=[
        "That the treatment has no effect on the amount of solute entering the cells",
        "That the treatment increases the amount of solute entering the cells",
        "That the treatment decreases the amount of solute entering the cells",
        "That the solute cannot enter the cells under any treatment",
        "That the solute enters the cells only through the hydrophobic interior"],
      ans=0,
      why="A null hypothesis is the statement of no effect, which the data are then used "
          "to reject or fail to reject. Asserting an increase or a decrease is the "
          "alternative rather than the null, and the last option states a mechanism EK "
          "2.4.A.3 denies for a polar solute."),

 dict(q="The same cells were tested for the entry of oxygen with transport proteins "
        "functional and with those proteins blocked, with the results in the second "
        "table. What should be concluded?",
      table=_T_NULL_OXYGEN,
      choices=[
        "The null hypothesis of no effect should not be rejected, which fits oxygen "
        "crossing the membrane without transport proteins.",
        "The null hypothesis of no effect should be rejected, which fits oxygen requiring "
        "transport proteins.",
        "The null hypothesis of no effect should be rejected, which fits oxygen being "
        "excluded by the hydrophobic interior.",
        "The null hypothesis of no effect should not be rejected, which fits oxygen "
        "requiring transport proteins.",
        "No conclusion is possible, because oxygen is a gas."],
      ans=0,
      why="The two tabulated means are close, so the no-effect hypothesis survives this "
          "test. EK 2.4.A.2 states that small nonpolar molecules including oxygen freely "
          "pass across the membrane, so a treatment that blocks transport proteins is not "
          "expected to change oxygen entry."),

 dict(q="Two preparations of walled cells, one with its walls left intact and one with "
        "its walls removed, were placed in distilled water, with the results in the "
        "table. Which conclusion is best supported?",
      table=_T_WALL,
      choices=[
        "The cell wall protects cells from bursting in distilled water.",
        "The cell wall causes cells to burst in distilled water.",
        "The cell wall had no measurable effect on whether cells burst.",
        "Both preparations burst at nearly the same rate.",
        "Removing the wall prevented water from entering the cells."],
      ans=0,
      why="Far more cells burst once the wall had been removed than with the wall intact. "
          "EK 2.4.B.1 states that cell walls provide protection from osmotic lysis, which "
          "is exactly the protection the data record."),

 dict(q="An artificial membrane is modified so that its interior becomes even more "
        "strongly hydrophobic. Which prediction follows most directly from the course "
        "framework?",
      choices=[
        "Ions and polar molecules will cross it even less readily than before.",
        "Ions and polar molecules will cross it more readily than before.",
        "Small nonpolar molecules will stop crossing it entirely.",
        "The membrane will lose its selective permeability altogether.",
        "The membrane will begin to admit every substance equally."],
      ans=0,
      why="EK 2.4.A.1 makes the hydrophobic interior the source of selective "
          "permeability, and EK 2.4.A.3 makes the nonpolar hydrocarbon tails what prevents "
          "the movement of ions and polar molecules. Strengthening that interior "
          "therefore sharpens the exclusion rather than removing it."),

 dict(q="Why can a charged ion not simply diffuse through the middle of a phospholipid "
        "bilayer?",
      choices=[
        "The interior is made of nonpolar hydrocarbon tails, which prevent the movement "
        "of ions.",
        "The interior is made of polar phosphate groups, which repel the ion's charge.",
        "The interior is occupied by transport proteins that block the way.",
        "The interior is filled with water, which the ion cannot displace.",
        "The interior carries a cell wall that admits only nonpolar substances."],
      ans=0,
      why="EK 2.4.A.3 states that the nonpolar hydrocarbon tails of phospholipids prevent "
          "the movement of ions and polar molecules across the membrane, and EK 2.3.A.1 "
          "places those tails in the interior. The phosphate regions face the aqueous "
          "environments rather than the interior."),

 dict(q="Why can oxygen cross a phospholipid bilayer without any protein assistance?",
      choices=[
        "It is a small nonpolar molecule, and the framework says such molecules freely "
        "pass across the membrane.",
        "It is a small polar molecule, and the framework says such molecules freely pass "
        "across the membrane.",
        "It is charged, and charged substances are drawn through the hydrophobic "
        "interior.",
        "It is large, and large molecules push the phospholipids apart as they pass.",
        "It passes through the cell wall rather than through the membrane."],
      ans=0,
      why="EK 2.4.A.2 states that small nonpolar molecules, including nitrogen, oxygen, "
          "and carbon dioxide, freely pass across the membrane. Small polar uncharged "
          "molecules are the separate case EK 2.4.A.3 limits to small amounts."),

 dict(q="A student states that a plasma membrane is impermeable to every substance. What "
        "is the best correction?",
      choices=[
        "The membrane is selectively permeable: small nonpolar molecules pass freely and "
        "hydrophilic substances cross through embedded proteins.",
        "The membrane is freely permeable to every substance, so nothing is excluded.",
        "The membrane admits only charged substances and excludes everything else.",
        "The membrane admits substances only where the cell wall has been removed.",
        "The student is correct, because the hydrophobic interior excludes everything."],
      ans=0,
      why="EK 2.4.A.1 calls the property selective permeability rather than "
          "impermeability, and EK 2.4.A.2 supplies both halves of the selection: free "
          "passage for small nonpolar molecules and passage through embedded channels and "
          "transport proteins for hydrophilic substances."),

 dict(q="Water is polar, yet the course framework does not group it with the substances "
        "that require embedded channels. How does the framework treat it?",
      choices=[
        "As a small polar, uncharged molecule that passes through the membrane in small "
        "amounts",
        "As a small nonpolar molecule that passes across the membrane freely",
        "As a large polar molecule that must use embedded channels and transport "
        "proteins",
        "As a charged substance that the hydrocarbon tails exclude completely",
        "As a substance that crosses only through the cell wall"],
      ans=0,
      why="EK 2.4.A.3 places small polar, uncharged molecules like water and ammonia in a "
          "category of their own that passes through the membrane in small amounts, "
          "distinct from the free passage of EK 2.4.A.2's small nonpolar molecules and "
          "from the prevention EK 2.4.A.3 applies to ions and polar molecules."),

 dict(q="Glucose and oxygen are both uncharged, yet the course framework treats them very "
        "differently. What accounts for the difference?",
      choices=[
        "Glucose is a large polar molecule and so needs embedded proteins, while oxygen "
        "is small and nonpolar and passes freely.",
        "Glucose is small and nonpolar and passes freely, while oxygen is a large polar "
        "molecule and needs embedded proteins.",
        "Glucose carries a charge and oxygen does not, so only glucose is excluded.",
        "Glucose is excluded by the cell wall and oxygen is not.",
        "There is no difference in how the framework treats them."],
      ans=0,
      why="EK 2.4.A.2 divides the two cases by size and polarity rather than by charge: "
          "small nonpolar molecules freely pass, while hydrophilic substances such as "
          "large polar molecules move through embedded channels and transport proteins."),

 dict(q="Which structure named in the course framework lies outside the plasma membrane "
        "and acts as a permeability barrier for some substances?",
      choices=["The cell wall", "The nuclear envelope", "The Golgi complex",
               "The mitochondrial inner membrane", "The ribosome"],
      ans=0,
      why="EK 2.4.B.1 states that cell walls provide a structural boundary as well as a "
          "permeability barrier for some substances to the internal or external cellular "
          "environments. The rejected structures are internal components treated in EK "
          "2.1.A.1 to EK 2.1.A.5."),

 dict(q="A walled bacterium has its cell wall removed and is then placed in distilled "
        "water. Which outcome does the course framework support as a prediction?",
      choices=[
        "It becomes more likely to burst, because the wall's protection from osmotic "
        "lysis has been removed.",
        "It becomes less likely to burst, because the wall had been trapping water "
        "inside.",
        "It becomes unable to take up any substance at all.",
        "Its plasma membrane loses its hydrophobic interior.",
        "Nothing changes, because the wall has no role in resisting bursting."],
      ans=0,
      why="EK 2.4.B.1 names protection from osmotic lysis among the roles of the cell "
          "walls of Bacteria, Archaea, Fungi, and plants, so removing the wall removes "
          "that protection. Nothing in EK 2.4.A.1 to EK 2.4.A.3 makes the membrane's own "
          "properties depend on the wall."),

 dict(q="A researcher wants to test whether a substance can cross a membrane without the "
        "help of any protein. Which design is best?",
      choices=[
        "Measure the movement of the substance across an artificial bilayer made only of "
        "phospholipids.",
        "Measure the movement of the substance across a living cell membrane containing "
        "its usual proteins.",
        "Measure the movement of the substance across an isolated cell wall.",
        "Measure the concentration of the substance inside a cell at a single moment.",
        "Measure the surface area of the membrane before and after adding the "
        "substance."],
      ans=0,
      why="The claim under test is about the bilayer alone, so the preparation must "
          "exclude the embedded channels and transport proteins EK 2.4.A.2 names as the "
          "alternative route. A living membrane confounds the two routes, and a cell wall "
          "is a different barrier under EK 2.4.B.1."),

 dict(q="By which route would ammonia be expected to enter a cell, according to the "
        "course framework?",
      choices=[
        "Directly through the membrane, in small amounts, as a small polar uncharged "
        "molecule",
        "Directly through the membrane, freely, as a small nonpolar molecule",
        "Through embedded channels and transport proteins, as a charged ion",
        "Through the cell wall, which selects for small molecules",
        "It cannot enter a cell at all."],
      ans=0,
      why="EK 2.4.A.3 names ammonia alongside water as a small polar, uncharged molecule "
          "that passes through the membrane in small amounts. It is neither in EK "
          "2.4.A.2's free-passage category nor among the ions that statement routes "
          "through proteins."),

 dict(q="An artificial membrane is built from molecules that are polar along their "
        "entire length, so the membrane has no hydrophobic interior at all. Which "
        "prediction follows most directly from the course framework?",
      choices=[
        "It will lose its selective permeability, because that property is stated to "
        "result from having a hydrophobic interior.",
        "It will keep its selective permeability, because selectivity depends on the "
        "embedded proteins rather than on the interior.",
        "It will become impermeable to every substance, including small nonpolar "
        "molecules.",
        "It will admit ions but exclude small nonpolar molecules.",
        "It will behave exactly as before, because the interior plays no part in what "
        "crosses."],
      ans=0,
      why="EK 2.4.A.1 states that selective permeability is the result of the plasma "
          "membrane having a hydrophobic interior, so removing that interior removes the "
          "stated cause of the property. EK 2.4.A.2 and EK 2.4.A.3 make the interior what "
          "sorts substances, not what blocks all of them."),

 dict(q="A membrane is found to admit nitrogen and carbon dioxide readily, water in small "
        "amounts, and sodium ions only where particular proteins are present. Which term "
        "best describes this behaviour?",
      choices=["Selective permeability", "Complete impermeability",
               "Free permeability to all substances", "Osmotic lysis",
               "Structural boundary formation"],
      ans=0,
      why="EK 2.4.A.1 names selective permeability as the property that results from the "
          "membrane's hydrophobic interior, and the three behaviours described are exactly "
          "the three cases EK 2.4.A.2 and EK 2.4.A.3 lay out. Osmotic lysis and structural "
          "boundary formation belong to the cell wall statement, EK 2.4.B.1."),

 dict(q="Which summary correctly sorts substances by how the course framework says they "
        "cross a plasma membrane?",
      choices=[
        "Small nonpolar molecules pass freely; small polar uncharged molecules pass in "
        "small amounts; large polar molecules and ions use embedded proteins.",
        "Small nonpolar molecules use embedded proteins; small polar uncharged molecules "
        "pass freely; large polar molecules and ions pass in small amounts.",
        "All three groups pass freely, since the membrane is permeable to everything.",
        "All three groups use embedded proteins, since nothing crosses the hydrophobic "
        "interior.",
        "Large polar molecules pass freely; ions pass in small amounts; small nonpolar "
        "molecules are excluded."],
      ans=0,
      why="The three cases come straight from two statements: EK 2.4.A.2 gives free "
          "passage to small nonpolar molecules and embedded channels and transport "
          "proteins to hydrophilic substances such as large polar molecules and ions, and "
          "EK 2.4.A.3 gives small polar uncharged molecules passage in small amounts."),
]
