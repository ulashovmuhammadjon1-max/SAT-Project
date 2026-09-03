# AP BIOLOGY 2.7 Tonicity and Osmoregulation
# CED effective Fall 2025, Unit 2 Cells. Big Idea 2 Energetics.
# Learning objectives 2.7.A, explain how concentration gradients affect the movement of
# molecules across membranes, and 2.7.B, explain how osmoregulatory mechanisms
# contribute to the health and survival of organisms.
# Suggested skill 4.A, construct a graph to represent the data.
#
# Essential knowledge relied on, in the framework's own words:
#   2.7.A.1    External environments can be hypotonic, hypertonic, or isotonic to
#              internal environments of cells. Movement of water can also be described
#              as moving from hypotonic to hypertonic regions. Water moves by osmosis
#              from regions of high water potential to regions of low water potential.
#              RELEVANT EQUATION -- water potential is the sum of the pressure
#              potential and the solute potential.
#              Illustrative examples: the contractile vacuole in protists, the central
#              vacuole in plant cells.
#   2.7.B.1    Growth and homeostasis are maintained by the constant movement of
#              molecules across membranes.
#   2.7.B.2    Osmoregulation maintains water balance and allows organisms to control
#              their internal solute composition and water potential. Water moves from
#              regions of low osmolarity or solute concentration to regions of high
#              osmolarity or solute concentration.
#              RELEVANT EQUATION -- the solute potential of a solution is the negative
#              of the ionization constant times the molar concentration times the
#              pressure constant times the temperature in Kelvin, where the pressure
#              constant is 0.0831 liter bars per mole per Kelvin and the temperature in
#              Kelvin is the temperature in degrees Celsius plus 273.
#
# ON NOTATION. The CED prints both equations with Greek symbols and subscripts.
# Biology is exported as prose with no typesetting, so this bank writes both equations
# out in words, IN THE STEM of every item that needs one. Nothing is left to be
# recalled: the exam supplies these equations on its formula sheet for the same reason.
#
# ON SCOPE. The transport mechanisms themselves are topics 2.5, 2.6 and 2.8. This topic
# is tonicity, water potential and osmoregulation.
#
# ON THE DATA. Every table is labelled hypothetical, and every keyed value is
# recomputed in verify_b2_7.py from the tabulated inputs and the equation above.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: Biology is exported as prose.
TOPIC = ("2.7", "Tonicity and Osmoregulation", 2)

_T_WATERPOT = dict(
    headers=["Solution (hypothetical)", "Ionization constant of the solute",
             "Molar concentration (moles per liter)", "Temperature (degrees Celsius)"],
    rows=[["Solution 1", "1", "0.2", "27"],
          ["Solution 2", "2", "0.1", "27"],
          ["Solution 3", "1", "0.5", "27"],
          ["Solution 4", "2", "0.3", "27"]])

_T_TONICITY = dict(
    headers=["Cell (hypothetical)", "Solute concentration inside the cell (millimolar)",
             "Solute concentration of the surrounding solution (millimolar)"],
    rows=[["Cell A", "300", "150"],
          ["Cell B", "300", "450"],
          ["Cell C", "300", "300"]])

_T_CONTRACTILE = dict(
    headers=["External solution (hypothetical)",
             "Solute concentration of the solution (millimolar)",
             "Contractions of the contractile vacuole per minute"],
    rows=[["Solution P", "5", "22"],
          ["Solution Q", "50", "11"],
          ["Solution R", "150", "3"]])

QUESTIONS = [

 dict(q="Which three terms does the course framework use to describe an external "
        "environment relative to the internal environment of a cell?",
      choices=[
        "Hypotonic, hypertonic and isotonic",
        "Hydrophilic, hydrophobic and amphipathic",
        "Passive, active and facilitated",
        "Saturated, unsaturated and polyunsaturated",
        "Linear, branched and helical"],
      ans=0,
      why="EK 2.7.A.1 states that external environments can be hypotonic, hypertonic, or "
          "isotonic to internal environments of cells. The rejected sets belong to EK "
          "2.3.A.2, EK 2.5, EK 1.5.A.1 and EK 1.4.A.1 and describe other properties."),

 dict(q="Movement of water can be described as moving between which regions, according to "
        "the course framework?",
      choices=[
        "From hypotonic regions to hypertonic regions",
        "From hypertonic regions to hypotonic regions",
        "From isotonic regions to hypotonic regions",
        "Always into the cell, whatever the surrounding solution",
        "Always out of the cell, whatever the surrounding solution"],
      ans=0,
      why="EK 2.7.A.1 states that movement of water can also be described as moving from "
          "hypotonic to hypertonic regions. The framework gives no fixed direction "
          "relative to the cell, only relative to the two regions' tonicity."),

 dict(q="In terms of water potential, in which direction does water move by osmosis?",
      choices=[
        "From regions of high water potential to regions of low water potential",
        "From regions of low water potential to regions of high water potential",
        "In whichever direction the cell's energy supply drives it",
        "From regions of high pressure potential to regions of low solute potential",
        "Water potential does not determine the direction of osmosis."],
      ans=0,
      why="EK 2.7.A.1 states that water moves by osmosis from regions of high water "
          "potential to regions of low water potential. Osmosis is not driven by the "
          "cell's energy supply in this statement, and the fourth option compares two "
          "different quantities."),

 dict(q="In terms of solute concentration, in which direction does water move, according "
        "to the course framework?",
      choices=[
        "From regions of low solute concentration to regions of high solute "
        "concentration",
        "From regions of high solute concentration to regions of low solute "
        "concentration",
        "Water moves only when the two solute concentrations are equal.",
        "Water moves in the direction that raises the solute concentration difference.",
        "Solute concentration has no bearing on the movement of water."],
      ans=0,
      why="EK 2.7.B.2 states that water moves from regions of low osmolarity or solute "
          "concentration to regions of high osmolarity or solute concentration. That is "
          "the same movement EK 2.7.A.1 describes as hypotonic to hypertonic, expressed in "
          "terms of solute rather than tonicity."),

 dict(q="The water potential of a solution is calculated from which two quantities?",
      choices=[
        "The pressure potential and the solute potential, added together",
        "The pressure potential and the solute potential, multiplied together",
        "The solute potential and the temperature, added together",
        "The molar concentration and the ionization constant, added together",
        "The pressure potential alone"],
      ans=0,
      why="The relevant equation printed with EK 2.7.A.1 gives water potential as the sum "
          "of the pressure potential and the solute potential. The other quantities named "
          "are the inputs to the separate solute potential equation printed with EK "
          "2.7.B.2."),

 dict(q="The solute potential of a solution is the negative of the ionization constant "
        "times the molar concentration times the pressure constant times the temperature "
        "in Kelvin. Which quantity is NOT an input to that calculation?",
      choices=[
        "The pressure potential of the solution",
        "The ionization constant of the solute",
        "The molar concentration of the solution",
        "The temperature in Kelvin",
        "The pressure constant"],
      ans=0,
      why="The equation printed with EK 2.7.B.2 takes the ionization constant, the molar "
          "concentration, the pressure constant and the temperature in Kelvin. The "
          "pressure potential enters the separate water potential equation printed with "
          "EK 2.7.A.1, where it is added to the solute potential."),

 dict(q="A solution is held at 27 degrees Celsius. What temperature should be used in the "
        "solute potential equation, which requires the temperature in Kelvin?",
      choices=["300", "27", "273", "246", "327"],
      ans=0,
      why="The equation printed with EK 2.7.B.2 defines the temperature in Kelvin as the "
          "temperature in degrees Celsius plus 273. Using the Celsius value unchanged, or "
          "subtracting instead of adding, are the two standard slips this item is built "
          "to catch."),

 dict(q="What does the course framework say osmoregulation does?",
      choices=[
        "It maintains water balance and allows organisms to control their internal solute "
        "composition and water potential.",
        "It supplies the energy an organism needs to move solutes against a gradient.",
        "It builds the phospholipids from which membranes are assembled.",
        "It prevents any movement of water across an organism's membranes.",
        "It converts solute potential into pressure potential."],
      ans=0,
      why="EK 2.7.B.2 states that osmoregulation maintains water balance and allows "
          "organisms to control their internal solute composition and water potential. "
          "Preventing all water movement would contradict EK 2.7.B.1's constant movement "
          "of molecules across membranes."),

 dict(q="According to the course framework, what maintains growth and homeostasis?",
      choices=[
        "The constant movement of molecules across membranes",
        "The complete absence of movement of molecules across membranes",
        "The rigidity of the cell wall alone",
        "The number of ribosomes a cell contains",
        "The removal of every concentration gradient"],
      ans=0,
      why="EK 2.7.B.1 states that growth and homeostasis are maintained by the constant "
          "movement of molecules across membranes. Removing every gradient would remove "
          "what EK 2.5.A.1 makes selective permeability able to establish."),

 dict(q="Which two structures does the course framework offer as illustrative examples "
        "when it discusses tonicity and the movement of water?",
      choices=[
        "The contractile vacuole in protists and the central vacuole in plant cells",
        "The ribosome and the Golgi complex",
        "The mitochondrion and the chloroplast",
        "The rough endoplasmic reticulum and the lysosome",
        "The nuclear envelope and the plasma membrane"],
      ans=0,
      why="The illustrative examples printed with EK 2.7.A.1 are the contractile vacuole "
          "in protists and the central vacuole in plant cells. The rejected pairs are "
          "organelles from EK 2.1.A.1 to EK 2.1.A.8, which the framework attaches to a "
          "different topic."),

 dict(q="The table gives the ionization constant, molar concentration and temperature of "
        "four solutions. Taking the solute potential as the negative of the ionization "
        "constant times the molar concentration times 0.0831 liter bars per mole per "
        "Kelvin times the temperature in Kelvin, which solution has the LOWEST solute "
        "potential?",
      table=_T_WATERPOT,
      choices=["Solution 4", "Solution 1", "Solution 2", "Solution 3",
               "All four have the same solute potential."],
      ans=0,
      why="Every row is at the same temperature, so the solute potential is set by the "
          "ionization constant multiplied by the molar concentration, and the largest "
          "such product gives the most negative value. Lowest means most negative, which "
          "is where the largest product lands."),

 dict(q="Using the same four solutions and the same equation, which two have solute "
        "potentials equal to each other?",
      table=_T_WATERPOT,
      choices=[
        "Solution 1 and Solution 2",
        "Solution 1 and Solution 3",
        "Solution 2 and Solution 3",
        "Solution 3 and Solution 4",
        "No two of them are equal."],
      ans=0,
      why="At a common temperature the solute potential depends on the product of the "
          "ionization constant and the molar concentration, and exactly one pair of rows "
          "shares that product. A solute that dissociates into two particles at half the "
          "concentration gives the same value as one that does not dissociate."),

 dict(q="Using the same equation and the values in the table, what is the solute "
        "potential of the solution whose molar concentration is 0.5 and whose ionization "
        "constant is 1?",
      table=_T_WATERPOT,
      choices=["About negative 12.5 bars", "About negative 4.2 bars",
               "About negative 25.0 bars", "About negative 0.5 bars",
               "About positive 12.5 bars"],
      ans=0,
      why="Multiplying the ionization constant, the molar concentration, the pressure "
          "constant of 0.0831 and the temperature of 300 Kelvin and then taking the "
          "negative gives the answer. The positive option ignores the minus sign the "
          "equation begins with, which is what makes every solute potential zero or "
          "negative."),

 dict(q="One of the solutions in the table is placed in an open beaker, where the "
        "pressure potential is zero. Given that water potential is the sum of the "
        "pressure potential and the solute potential, what is the water potential of the "
        "solution with an ionization constant of 1 and a molar concentration of 0.2?",
      table=_T_WATERPOT,
      choices=["About negative 5.0 bars", "About positive 5.0 bars", "Zero bars",
               "About negative 10.0 bars",
               "It cannot be determined without the pressure potential."],
      ans=0,
      why="With a pressure potential of zero the sum reduces to the solute potential "
          "alone, and the stem supplies the pressure potential, so the final option is "
          "false. The solute potential itself follows from the equation and the row's own "
          "values."),

 dict(q="Two of the solutions in the table are placed in open beakers, where the pressure "
        "potential is zero, and are separated by a membrane permeable only to water. In "
        "which direction does water move between the solution with an ionization constant "
        "of 1 and a concentration of 0.2 and the solution with an ionization constant of "
        "2 and a concentration of 0.3?",
      table=_T_WATERPOT,
      choices=[
        "From the first solution to the second, because the first has the higher water "
        "potential",
        "From the second solution to the first, because the second has the higher water "
        "potential",
        "In neither direction, because the two water potentials are equal",
        "From the second solution to the first, because the second has more solute",
        "The direction cannot be determined without knowing the pressure potentials."],
      ans=0,
      why="EK 2.7.A.1 states that water moves by osmosis from regions of high water "
          "potential to regions of low water potential. With the pressure potential zero "
          "in both beakers each water potential equals its own solute potential, and the "
          "less negative of the two is the higher. The stem supplies the pressure "
          "potentials, so the final option is false."),

 dict(q="The table gives the solute concentration inside three cells and in the solution "
        "surrounding each. Which cell is surrounded by a hypotonic solution?",
      table=_T_TONICITY,
      choices=["Cell A", "Cell B", "Cell C",
               "All three are surrounded by hypotonic solutions.",
               "None of them is surrounded by a hypotonic solution."],
      ans=0,
      why="A hypotonic external environment is one with a lower solute concentration than "
          "the cell's interior, and exactly one row of the table records that. EK 2.7.A.1 "
          "names hypotonic, hypertonic and isotonic as the three possible relations."),

 dict(q="Among the same three cells, which is surrounded by a hypertonic solution?",
      table=_T_TONICITY,
      choices=["Cell B", "Cell A", "Cell C",
               "All three are surrounded by hypertonic solutions.",
               "None of them is surrounded by a hypertonic solution."],
      ans=0,
      why="A hypertonic external environment has a higher solute concentration than the "
          "cell's interior, and exactly one row of the table records that. The three "
          "relations EK 2.7.A.1 names are mutually exclusive, so only one row can qualify."),

 dict(q="Which of the three cells in the table sits in an isotonic solution?",
      table=_T_TONICITY,
      choices=["Cell C", "Cell A", "Cell B",
               "All three sit in isotonic solutions.",
               "None of them sits in an isotonic solution."],
      ans=0,
      why="An isotonic external environment has the same solute concentration as the "
          "cell's interior, and exactly one row of the table records equal values. EK "
          "2.7.A.1 names isotonic as one of the three possible relations."),

 dict(q="Into which of the three cells in the table would water move by osmosis?",
      table=_T_TONICITY,
      choices=["Cell A", "Cell B", "Cell C", "All three", "None of them"],
      ans=0,
      why="EK 2.7.B.2 states that water moves from regions of low solute concentration to "
          "regions of high solute concentration, so water enters the cell whose interior "
          "is the more concentrated of the pair. Exactly one row of the table is "
          "arranged that way."),

 dict(q="Which of the three cells in the table would lose water to its surroundings?",
      table=_T_TONICITY,
      choices=["Cell B", "Cell A", "Cell C", "All three", "None of them"],
      ans=0,
      why="EK 2.7.A.1 describes water as moving from hypotonic to hypertonic regions, so "
          "a cell loses water when the solution around it is the more concentrated of the "
          "pair. Exactly one row of the table is arranged that way."),

 dict(q="A protist was placed in three external solutions of different solute "
        "concentration and its contractile vacuole contractions were counted, with the "
        "results in the table. Which conclusion is best supported?",
      table=_T_CONTRACTILE,
      choices=[
        "The more dilute the surrounding solution, the more often the contractile vacuole "
        "contracted.",
        "The more dilute the surrounding solution, the less often the contractile vacuole "
        "contracted.",
        "The contraction rate was the same in all three solutions.",
        "The contractile vacuole contracted only in the most concentrated solution.",
        "Contraction rate was unrelated to the surrounding solute concentration."],
      ans=0,
      why="Contractions fall at every step as the external solute concentration rises "
          "across the three solutions. EK 2.7.B.2 makes water move toward the more "
          "concentrated region, so a dilute environment sends more water into the cell "
          "for the vacuole, which EK 2.7.A.1 offers as an illustrative example, to expel."),

 dict(q="Using the same data, what would you predict for the same protist placed in a "
        "solution at 250 millimolar?",
      table=_T_CONTRACTILE,
      choices=[
        "Fewer contractions per minute than in any of the three solutions tested",
        "More contractions per minute than in any of the three solutions tested",
        "Exactly the same number of contractions as in the most dilute solution",
        "No contractions at all, because contraction requires a hypertonic environment",
        "The prediction cannot be made, because contraction rate does not depend on the "
        "surroundings."],
      ans=0,
      why="The tabulated contraction rate falls at every step as the external "
          "concentration rises, and the new solution is more concentrated than any row "
          "shown, so the trend extrapolates below the lowest value. EK 2.7.B.2 supplies "
          "the reason the trend continues rather than reversing."),

 dict(q="Why does the pressure potential of a solution in an open beaker count as zero "
        "when its water potential is calculated?",
      choices=[
        "Because there is no physical pressure applied to the solution beyond the "
        "surroundings, so only the solute potential contributes",
        "Because the solute potential is always zero in an open beaker",
        "Because water potential is defined without a pressure term",
        "Because pressure potential applies only to solutions containing an ionizing "
        "solute",
        "Because the pressure potential and the solute potential always cancel"],
      ans=0,
      why="The equation printed with EK 2.7.A.1 makes water potential the sum of the "
          "pressure potential and the solute potential, so a pressure potential of zero "
          "leaves the solute potential as the whole value. The solute potential is not "
          "zero unless the solution contains no solute."),

 dict(q="Why is the solute potential of a solution containing dissolved solute never a "
        "positive number?",
      choices=[
        "The equation begins with a minus sign, and the ionization constant, "
        "concentration, pressure constant and Kelvin temperature are all positive.",
        "The equation begins with a plus sign, but the Kelvin temperature is negative.",
        "The ionization constant is negative for every solute.",
        "The molar concentration is negative whenever solute is present.",
        "The pressure constant is negative."],
      ans=0,
      why="The equation printed with EK 2.7.B.2 takes the negative of a product of four "
          "quantities, each of which is positive for a real solution, so the result is "
          "zero when there is no solute and negative otherwise. None of the individual "
          "inputs is itself negative."),

 dict(q="Solute is added to a solution in an open beaker while the temperature is held "
        "constant. What happens to its water potential?",
      choices=[
        "It falls, because a larger concentration makes the solute potential more "
        "negative.",
        "It rises, because a larger concentration makes the solute potential more "
        "positive.",
        "It stays the same, because water potential depends only on the pressure "
        "potential.",
        "It falls, because the pressure potential becomes negative.",
        "It cannot change unless the temperature also changes."],
      ans=0,
      why="The equation printed with EK 2.7.B.2 makes the solute potential proportional to "
          "the molar concentration with a minus sign in front, and the equation printed "
          "with EK 2.7.A.1 adds that solute potential to a pressure potential of zero in "
          "an open beaker."),

 dict(q="An animal cell with no cell wall is placed in a strongly hypertonic solution. "
        "Which outcome is predicted by the course framework?",
      choices=[
        "Water leaves the cell, because water moves toward the region of higher solute "
        "concentration.",
        "Water enters the cell, because water moves toward the region of lower solute "
        "concentration.",
        "No water moves, because an animal cell has no cell wall.",
        "The cell bursts, because a hypertonic solution drives water inward.",
        "The cell synthesizes additional solute until the two sides are equal."],
      ans=0,
      why="EK 2.7.B.2 states that water moves from regions of low solute concentration to "
          "regions of high solute concentration, and EK 2.7.A.1 describes the same "
          "movement as running from hypotonic toward hypertonic. A hypertonic exterior "
          "therefore draws water out."),

 dict(q="An animal cell with no cell wall is placed in a strongly hypotonic solution. "
        "Which risk does the course framework identify for such a cell?",
      choices=[
        "Water enters the cell and it may undergo osmotic lysis, a risk a cell wall would "
        "guard against.",
        "Water leaves the cell and it may shrink, a risk a cell wall would guard against.",
        "No water moves, because a hypotonic solution has the same water potential as the "
        "cell.",
        "The cell wall of the animal cell prevents any change in volume.",
        "The cell converts the excess water into solute."],
      ans=0,
      why="EK 2.7.A.1 sends water from hypotonic toward hypertonic regions, so a "
          "hypotonic exterior drives water in, and EK 2.4.B.1 names protection from "
          "osmotic lysis among the roles of the cell walls of Bacteria, Archaea, Fungi and "
          "plants, which an animal cell does not have."),

 dict(q="Why is there no net movement of water between a cell and an isotonic solution?",
      choices=[
        "The solute concentrations on the two sides are equal, so there is no difference "
        "in water potential to drive net movement.",
        "The solute concentrations on the two sides are equal, so water molecules stop "
        "moving altogether.",
        "An isotonic solution contains no solute at all.",
        "An isotonic solution has a positive water potential, which blocks osmosis.",
        "Water can only cross a membrane when a direct energy input is supplied."],
      ans=0,
      why="EK 2.7.A.1 drives osmosis by a difference in water potential and EK 2.7.B.2 by "
          "a difference in solute concentration, so equal concentrations leave no net "
          "direction. EK 2.7.B.1's constant movement of molecules across membranes is "
          "what rules out the claim that movement stops altogether."),

 dict(q="A protist living in fresh water is moved to a solution much closer in solute "
        "concentration to its own interior. What would the course framework predict for "
        "its contractile vacuole?",
      choices=[
        "It will need to expel less water, because less water now enters the cell by "
        "osmosis.",
        "It will need to expel more water, because more water now enters the cell by "
        "osmosis.",
        "It will need to expel the same amount of water, because osmoregulation is "
        "constant.",
        "It will begin to take water in rather than expel it, because the solution is "
        "hypertonic.",
        "It will stop functioning, because osmoregulation is only needed in hypertonic "
        "surroundings."],
      ans=0,
      why="EK 2.7.B.2 makes water move toward the more concentrated region, so narrowing "
          "the difference reduces the inward flow. EK 2.7.B.2 also states that "
          "osmoregulation maintains water balance, and EK 2.7.A.1 offers the contractile "
          "vacuole of protists as its illustrative example."),

 dict(q="Which summary correctly links the framework's three descriptions of the same "
        "movement of water?",
      choices=[
        "Water moves from hypotonic to hypertonic regions, from low solute concentration "
        "to high, and from high water potential to low.",
        "Water moves from hypertonic to hypotonic regions, from high solute concentration "
        "to low, and from low water potential to high.",
        "Water moves from hypotonic to hypertonic regions, from high solute concentration "
        "to low, and from high water potential to low.",
        "Water moves from hypertonic to hypotonic regions, from low solute concentration "
        "to high, and from high water potential to low.",
        "The three descriptions contradict one another and cannot all be correct."],
      ans=0,
      why="EK 2.7.A.1 supplies the first and third descriptions and EK 2.7.B.2 the second, "
          "and all three name the same movement: toward the more concentrated, lower "
          "water potential side. Each rejected option reverses one or two of the three."),
]
