r"""AP CHEMISTRY 2.2 Intramolecular Force and Potential Energy.

CED effective Fall 2024, Unit 2 Compound Structure and Properties.
Learning objective 2.2.A: represent the relationship between potential energy
and distance between atoms, based on factors that influence the interaction
strength.
Suggested skill 3.A, represent chemical phenomena using appropriate graphing
techniques, including correct scale and units.

Essential knowledge relied on, in the framework's own words:

  2.2.A.1  A graph of potential energy versus the distance between atoms
           (internuclear distance) is a useful representation for describing
           the interactions between atoms. Such graphs illustrate both the
           equilibrium bond length (the separation between atoms at which the
           potential energy is lowest) and the bond energy (the energy required
           to separate the atoms).
  2.2.A.2  In a covalent bond, the bond length is influenced by both the size
           of the atom's core and the bond order (i.e., single, double,
           triple). Bonds with a higher order are shorter and have larger bond
           energies.
  2.2.A.3  Coulomb's law can be used to understand the strength of interactions
           between cations and anions.
             i.  Because the interaction strength is proportional to the charge
                 on each ion, larger charges lead to stronger interactions.
             ii. Because the interaction strength increases as the distance
                 between the centers of the ions (nuclei) decreases, smaller
                 ions lead to stronger interactions.

ON THE GRAPH, WHICH IS THIS TOPIC'S WHOLE PROBLEM. EK 2.2.A.1 is a statement
about a GRAPH, and SCIENCE_BRIEF.md forbids referring to a picture the bank
cannot show. Every potential energy curve here is therefore printed as a table
of internuclear distance against potential energy, and each item asks its
question of that table -- where the minimum lies, how deep it is, what happens
on either side of it. No stem says "the graph shows". Item 6 is the suggested
skill 3.A item and asks which axes and units such a graph would need, which is
a question about how to build the representation rather than about reading one.

HOW COULOMB'S LAW HERE DIFFERS FROM 1.5's. EK 1.5.A.2 applies Coulomb's law to
an electron and a nucleus inside one atom; EK 2.2.A.3 applies it to CATIONS AND
ANIONS. Every Coulombic item in this module is about two ions, and every
Coulombic item in 1.5 is about a subshell of one atom. Neither module trespasses
on the other.

ON THE DATA. Bond lengths and bond energies are of realistic magnitude, but no
item turns on recalling one: every key follows from comparisons WITHIN the
item's own table.

NOTATION. Energies and distances are plain prose with units written out.
Negative values are written with a hyphen inside the table cells, which the
notation gate permits because a cell is not prose.
"""
TOPIC = ("2.2", "Intramolecular Force and Potential Energy", 2)

_T_CURVE = dict(
    headers=["Internuclear distance (picometers)",
             "Potential energy (kilojoules per mole)"],
    rows=[["40", "220"], ["60", "-100"], ["74", "-436"], ["90", "-390"],
          ["120", "-250"], ["200", "-60"], ["400", "0"]])

_T_CURVE_B = dict(
    headers=["Internuclear distance (picometers)",
             "Potential energy (kilojoules per mole)"],
    rows=[["80", "150"], ["110", "-200"], ["127", "-431"], ["150", "-360"],
          ["200", "-180"], ["350", "-20"], ["600", "0"]])

_T_ORDER = dict(
    headers=["Bond", "Bond order", "Bond length (picometers)",
             "Bond energy (kilojoules per mole)"],
    rows=[["Carbon to carbon, single", "1", "154", "348"],
          ["Carbon to carbon, double", "2", "134", "614"],
          ["Carbon to carbon, triple", "3", "120", "839"]])

_T_CORE = dict(
    headers=["Bond", "Bond order", "Bond length (picometers)"],
    rows=[["Hydrogen to fluorine", "1", "92"],
          ["Hydrogen to chlorine", "1", "127"],
          ["Hydrogen to bromine", "1", "141"],
          ["Hydrogen to iodine", "1", "161"]])

_T_IONS = dict(
    headers=["Ion pair", "Charge on the cation", "Charge on the anion",
             "Distance between the ion centers (picometers)"],
    rows=[["Pair 1", "+1", "-1", "280"], ["Pair 2", "+2", "-2", "280"],
          ["Pair 3", "+1", "-1", "200"], ["Pair 4", "+2", "-1", "240"]])

_T_IONIC_SIZE = dict(
    headers=["Ion pair", "Charge on the cation", "Charge on the anion",
             "Distance between the ion centers (picometers)"],
    rows=[["Pair A", "+1", "-1", "230"], ["Pair B", "+1", "-1", "280"],
          ["Pair C", "+1", "-1", "310"], ["Pair D", "+1", "-1", "350"]])

_T_MINIMA = dict(
    headers=["Diatomic molecule", "Distance at the lowest potential energy (picometers)",
             "Lowest potential energy reached (kilojoules per mole)"],
    rows=[["Molecule J", "74", "-436"], ["Molecule K", "121", "-498"],
          ["Molecule L", "142", "-159"], ["Molecule M", "110", "-945"]])

QUESTIONS = [

 dict(q="A graph of potential energy against the distance between two atoms is drawn. "
        "Which two quantities does such a representation display?",
      choices=[
        "The equilibrium bond length and the bond energy.",
        "The mass of each atom and the total mass of the molecule.",
        "The number of valence electrons on each atom and the bond order.",
        "The electronegativity of each atom and the bond dipole.",
        "The temperature of the sample and its rate of reaction."],
      ans=0,
      why="EK 2.2.A.1, near verbatim: such graphs illustrate both the equilibrium bond "
          "length, the separation at which the potential energy is lowest, and the bond "
          "energy, the energy required to separate the atoms. Nothing in the framework "
          "reads a mass or a temperature off that representation."),

 dict(q="The table records the potential energy of a pair of atoms at several "
        "internuclear distances. What is the equilibrium bond length?",
      table=_T_CURVE,
      choices=["74 picometers", "40 picometers", "120 picometers",
               "400 picometers", "436 picometers"],
      ans=0,
      why="EK 2.2.A.1 defines the equilibrium bond length as the separation between "
          "atoms at which the potential energy is lowest, so the answer is read off the "
          "tabulated distance holding the smallest energy value. Reading the energy "
          "itself as a distance gives one of the rejected values."),

 dict(q="Using the same table, what is the bond energy of this bond?",
      table=_T_CURVE,
      choices=["436 kilojoules per mole", "74 kilojoules per mole",
               "220 kilojoules per mole", "250 kilojoules per mole",
               "656 kilojoules per mole"],
      ans=0,
      why="EK 2.2.A.1 defines the bond energy as the energy required to separate the "
          "atoms, which is the depth of the tabulated minimum below the value at large "
          "separation. That reference value is zero in this table, so the bond energy is "
          "the magnitude of the lowest energy reached."),

 dict(q="Using the same table, what happens to the potential energy as the two atoms "
        "are pushed closer together than the equilibrium bond length?",
      table=_T_CURVE,
      choices=[
        "It rises steeply, eventually becoming positive.",
        "It falls further, becoming more negative without limit.",
        "It stays at its lowest value, since that value is a minimum.",
        "It rises to exactly zero and remains there.",
        "It cannot be determined, because the graph applies only to separations larger "
        "than the bond length."],
      ans=0,
      why="EK 2.2.A.1 calls the equilibrium bond length the separation at which the "
          "potential energy is LOWEST, so on either side of it the energy must be higher, "
          "and the tabulated values at the two shortest distances rise and then turn "
          "positive."),

 dict(q="Using the same table, what happens to the potential energy as the two atoms are "
        "pulled far apart?",
      table=_T_CURVE,
      choices=[
        "It rises toward zero, the value for two separated atoms.",
        "It falls toward the value at the equilibrium bond length.",
        "It becomes large and positive without limit.",
        "It stays at its minimum value however far apart the atoms are moved.",
        "It oscillates between positive and negative values."],
      ans=0,
      why="EK 2.2.A.1 makes the bond energy the energy required to SEPARATE the atoms, "
          "which means the curve must climb from its minimum toward the value for atoms "
          "that no longer interact. The tabulated values do exactly that, reaching zero "
          "at the largest separation."),

 dict(q="A student is asked to draw the representation EK 2.2.A.1 describes for a "
        "diatomic molecule. Which pair of axes and units is appropriate?",
      choices=[
        "Internuclear distance in picometers on the horizontal axis and potential energy "
        "in kilojoules per mole on the vertical axis.",
        "Time in seconds on the horizontal axis and potential energy in kilojoules per "
        "mole on the vertical axis.",
        "Internuclear distance in picometers on the horizontal axis and mass in grams on "
        "the vertical axis.",
        "Temperature in kelvin on the horizontal axis and bond order on the vertical "
        "axis.",
        "Bond energy in kilojoules per mole on both axes, so that the two can be "
        "compared."],
      ans=0,
      why="Suggested skill 3.A asks for an appropriate graph with correct scale and "
          "units, and EK 2.2.A.1 names the two quantities as potential energy and the "
          "distance between atoms. Only one pairing plots those two against each other "
          "in units each quantity is actually measured in."),

 dict(q="What does the framework say about how bond order affects the length and energy "
        "of a covalent bond?",
      choices=[
        "Bonds with a higher order are shorter and have larger bond energies.",
        "Bonds with a higher order are longer and have larger bond energies.",
        "Bonds with a higher order are shorter and have smaller bond energies.",
        "Bonds with a higher order are longer and have smaller bond energies.",
        "Bond order affects neither length nor energy, only the number of shared "
        "electrons."],
      ans=0,
      why="EK 2.2.A.2, near verbatim: bonds with a higher order are shorter and have "
          "larger bond energies. The framework also names the size of the atom's core as "
          "the other influence on bond length."),

 dict(q="The table gives data for three carbon-to-carbon bonds. What relationship do the "
        "data show between bond order, bond length and bond energy?",
      table=_T_ORDER,
      choices=[
        "As bond order rises, the bond gets shorter and its energy gets larger.",
        "As bond order rises, the bond gets longer and its energy gets larger.",
        "As bond order rises, the bond gets shorter and its energy gets smaller.",
        "Bond order is related to bond length but not to bond energy.",
        "The three bonds have the same length and energy, since all are between carbon "
        "atoms."],
      ans=0,
      why="The tabulated lengths fall and the tabulated energies rise as the tabulated "
          "bond order increases, which is exactly the relationship EK 2.2.A.2 states. "
          "That both quantities are involved is what rules out the option separating "
          "them."),

 dict(q="The table gives four single bonds between hydrogen and a different partner "
        "atom. Since every bond order is the same, what accounts for the differences in "
        "bond length?",
      table=_T_CORE,
      choices=[
        "The size of the partner atom's core, which is the other influence the framework "
        "names on bond length.",
        "The bond order, which the table shows to be different for each bond.",
        "The number of hydrogen atoms in each molecule, which differs.",
        "The temperature at which each bond length was measured.",
        "Nothing accounts for it, since bonds of the same order must have the same "
        "length."],
      ans=0,
      why="EK 2.2.A.2 names two influences on the length of a covalent bond, the size of "
          "the atom's core and the bond order, and the tabulated bond order is identical "
          "for all four rows, so the remaining influence is the one that varies."),

 dict(q="Coulomb's law is applied to the interaction between a cation and an anion. What "
        "happens to the strength of that interaction if the charge on the cation is "
        "doubled while the distance between the ion centers is unchanged?",
      choices=["It becomes stronger.", "It becomes weaker.",
               "It is unchanged, since only distance matters.",
               "It becomes stronger only if the anion's charge is also doubled.",
               "It falls to zero, since a doubled charge cancels the anion's charge."],
      ans=0,
      why="EK 2.2.A.3.i states that because the interaction strength is proportional to "
          "the charge on each ion, larger charges lead to stronger interactions. That is "
          "a statement about EACH ion separately, so raising one charge is enough."),

 dict(q="Two ionic compounds are compared. In the first, the ions are small; in the "
        "second, the ions are larger but carry the same charges. Which interaction is "
        "stronger, and why?",
      choices=[
        "The first, because a smaller distance between ion centers means a stronger "
        "interaction.",
        "The second, because larger ions carry more electrons and so attract more "
        "strongly.",
        "The first, because smaller ions carry larger charges.",
        "The second, because a larger distance between ion centers allows a stronger "
        "interaction.",
        "The two are equal, because the charges are the same."],
      ans=0,
      why="EK 2.2.A.3.ii states that because the interaction strength increases as the "
          "distance between the centers of the ions decreases, smaller ions lead to "
          "stronger interactions. The charges are stipulated equal, so distance is the "
          "only variable left."),

 dict(q="Four cation and anion pairs are described in the table. In which pair is the "
        "Coulombic interaction the strongest?",
      table=_T_IONS,
      choices=["Pair 2", "Pair 1", "Pair 3", "Pair 4",
               "Pairs 2 and 3 are equally strong and stronger than the others"],
      ans=0,
      why="EK 2.2.A.3 makes the strength grow with the charge on each ion and fall as the "
          "distance between the ion centers grows, so both columns have to be taken "
          "together. Choosing on charge alone or on distance alone points at a different "
          "row."),

 dict(q="Four cation and anion pairs carry identical charges but differ in the distance "
        "between their ion centers, as shown. In which pair is the interaction the "
        "weakest?",
      table=_T_IONIC_SIZE,
      choices=["Pair D", "Pair A", "Pair B", "Pair C",
               "All four are equal, because all four carry the same charges"],
      ans=0,
      why="EK 2.2.A.3.ii states that the interaction strength increases as the distance "
          "between the ion centers decreases, so with the charges held equal the largest "
          "tabulated distance gives the weakest interaction."),

 dict(q="Four diatomic molecules were studied and the position and depth of the minimum "
        "in each potential energy curve recorded. Which molecule has the strongest bond?",
      table=_T_MINIMA,
      choices=["Molecule M", "Molecule J", "Molecule K", "Molecule L",
               "Molecule J, because its minimum lies at the shortest distance"],
      ans=0,
      why="EK 2.2.A.1 makes the bond energy the energy required to separate the atoms, "
          "which is the depth of the minimum, so the deepest tabulated minimum marks the "
          "strongest bond. The shortest bond in this table is not the strongest one, "
          "which is what the last rejected option assumes."),

 dict(q="Using the same table, which molecule has the shortest bond?",
      table=_T_MINIMA,
      choices=["Molecule J", "Molecule K", "Molecule L", "Molecule M",
               "Molecule M, because it has the deepest minimum"],
      ans=0,
      why="EK 2.2.A.1 defines the equilibrium bond length as the separation at which the "
          "potential energy is lowest, so the answer is the smallest tabulated distance. "
          "Because the deepest minimum belongs to a different molecule, depth cannot be "
          "used as a proxy here."),

 dict(q="Why is the potential energy of two bonded atoms lower at the equilibrium bond "
        "length than at any other separation?",
      choices=[
        "Because that separation is where the net attraction and repulsion between the "
        "two atoms balance most favorably, which is what makes it the minimum of the "
        "curve.",
        "Because the atoms stop moving entirely at that separation.",
        "Because the two nuclei touch at that separation.",
        "Because the bond order changes at that separation.",
        "Because potential energy is defined to be zero at that separation."],
      ans=0,
      why="EK 2.2.A.1 identifies the equilibrium bond length as the separation at which "
          "the potential energy is lowest, and a minimum in the curve is by definition "
          "where the energy is lower than on either side. The framework sets the zero of "
          "the scale at large separation, not at the minimum."),

 dict(q="A second potential energy curve is tabulated below for a different diatomic "
        "molecule. Compared with the first table, is this bond longer or shorter, and "
        "stronger or weaker?",
      table=_T_CURVE_B,
      choices=[
        "Longer and very slightly weaker, since its minimum lies at a greater distance "
        "and is very slightly shallower.",
        "Shorter and stronger, since its minimum lies at a smaller distance and is "
        "deeper.",
        "Longer and stronger, since a greater bond length always means a stronger bond.",
        "Shorter and weaker, since its minimum lies at a smaller distance and is "
        "shallower.",
        "Identical in both respects, since both curves reach zero at large separation."],
      ans=0,
      why="EK 2.2.A.1 makes the position of the minimum the bond length and its depth the "
          "bond energy, so the two curves are compared on those two readings. Reaching "
          "the same value at large separation is what makes the depths comparable, not "
          "what makes them equal."),

 dict(q="Two covalent bonds join the same two elements, but one is a single bond and the "
        "other a double bond. Which statement about them is correct?",
      choices=[
        "The double bond is shorter and requires more energy to break.",
        "The double bond is longer and requires more energy to break.",
        "The double bond is shorter and requires less energy to break.",
        "The two bonds have the same length, since the atoms are the same.",
        "The two bonds have the same energy, since the atoms are the same."],
      ans=0,
      why="EK 2.2.A.2 states that bonds with a higher order are shorter and have larger "
          "bond energies, and it names bond order as an influence on length alongside "
          "the size of the atom's core. Holding the two elements fixed leaves bond order "
          "as the variable."),

 dict(q="Using the tabulated carbon-to-carbon data, by roughly what factor does the bond "
        "energy grow when the bond order rises from one to three?",
      table=_T_ORDER,
      choices=["About two and a half times", "About one and a half times",
               "About five times", "It does not grow; it falls by about half",
               "It stays the same"],
      ans=0,
      why="The two tabulated bond energies are compared directly as a ratio, and EK "
          "2.2.A.2's claim that higher-order bonds have larger bond energies is what "
          "makes the direction of the change expected rather than surprising."),

 dict(q="Using the tabulated carbon-to-carbon data, by roughly how much does the bond "
        "shorten when the bond order rises from one to three?",
      table=_T_ORDER,
      choices=["By about 34 picometers", "By about 20 picometers",
               "By about 120 picometers", "By about 274 picometers",
               "It does not shorten; it lengthens by about 34 picometers"],
      ans=0,
      why="The difference between the two tabulated bond lengths is read off directly, "
          "and EK 2.2.A.2's statement that higher-order bonds are shorter fixes the "
          "direction. Adding the two lengths rather than subtracting them gives one of "
          "the rejected values."),

 dict(q="An ionic compound made of doubly charged ions is compared with one made of "
        "singly charged ions of about the same size. Which is expected to have the "
        "stronger interaction between its ions, and why?",
      table=_T_IONS,
      choices=[
        "The compound with doubly charged ions, because interaction strength is "
        "proportional to the charge on each ion.",
        "The compound with singly charged ions, because smaller charges sit closer "
        "together.",
        "The two are equal, because the ion centers are the same distance apart.",
        "The compound with singly charged ions, because a smaller charge is spread over "
        "a smaller volume.",
        "Neither, because Coulomb's law applies only to atoms rather than to ions."],
      ans=0,
      why="EK 2.2.A.3.i states that because the interaction strength is proportional to "
          "the charge on each ion, larger charges lead to stronger interactions, and EK "
          "2.2.A.3 makes Coulomb's law the right tool for cation-anion interactions "
          "specifically. Equal distances leave charge as the only variable."),

 dict(q="What does the value of the potential energy at very large internuclear "
        "distances represent?",
      table=_T_CURVE,
      choices=[
        "The energy of two atoms that are no longer interacting, which is the reference "
        "the bond energy is measured against.",
        "The bond energy of the molecule, read directly.",
        "The equilibrium bond length, expressed as an energy.",
        "The energy required to push the two atoms together.",
        "The energy of a single atom on its own."],
      ans=0,
      why="EK 2.2.A.1 makes the bond energy the energy required to SEPARATE the atoms, so "
          "the value the curve approaches when the atoms are far apart is the state that "
          "separation reaches, and the depth of the minimum below it is the bond energy."),

 dict(q="Two ion pairs carry the same charges. The first has ion centers 200 picometers "
        "apart and the second 400 picometers apart. How do the interaction strengths "
        "compare?",
      choices=[
        "The first is stronger, and by more than a factor of two, since the strength "
        "depends on the square of the distance.",
        "The first is stronger, by exactly a factor of two.",
        "The second is stronger, by a factor of two.",
        "The two are equal, since the charges are the same.",
        "The comparison cannot be made without knowing the masses of the ions."],
      ans=0,
      why="EK 2.2.A.3.ii states that the interaction strength increases as the distance "
          "between the ion centers decreases, and EK 1.5.A.2 gives Coulomb's law with the "
          "separation squared in the denominator, so halving the distance more than "
          "doubles the strength. Mass does not appear in the relationship."),

 dict(q="A student claims that the bond energy of a molecule can be read straight off "
        "the potential energy curve as the value at the minimum, without reference to "
        "any other point. Using the tabulated curve, evaluate the claim.",
      table=_T_CURVE,
      choices=[
        "It happens to work here only because the curve reaches zero at large "
        "separation; the bond energy is the depth of the minimum BELOW that value.",
        "It is correct in general, because the minimum is always the bond energy.",
        "It is wrong, because the bond energy is the value at the shortest tabulated "
        "distance.",
        "It is wrong, because the bond energy is the distance at which the minimum "
        "occurs.",
        "It cannot be evaluated, because bond energy is not shown on such a curve at "
        "all."],
      ans=0,
      why="EK 2.2.A.1 defines the bond energy as the energy required to separate the "
          "atoms, which is a DIFFERENCE between the minimum and the separated-atom "
          "value. The two coincide numerically only when the separated-atom value has "
          "been set to zero, as it is in this table."),

 dict(q="Two bonds have the same bond order but join atoms of different size. What does "
        "the framework predict about their lengths?",
      table=_T_CORE,
      choices=[
        "The bond involving the larger atomic core will be the longer of the two.",
        "The two bonds will have the same length, since bond order is the only "
        "influence.",
        "The bond involving the larger atomic core will be the shorter of the two.",
        "The lengths will depend on the electronegativity difference rather than on "
        "size.",
        "No prediction is possible without measuring both bonds."],
      ans=0,
      why="EK 2.2.A.2 names both the size of the atom's core and the bond order as "
          "influences on bond length, so with the order held fixed the core size is what "
          "remains, and the tabulated lengths rise with the size of the partner atom."),

 dict(q="Why does the framework describe a potential energy curve as a useful "
        "representation of the interaction between two atoms?",
      choices=[
        "Because a single curve displays both the separation the atoms settle at and the "
        "energy needed to pull them apart.",
        "Because it shows how the mass of the molecule changes with separation.",
        "Because it replaces the need to know which elements are involved.",
        "Because it gives the rate at which the bond forms.",
        "Because it shows the number of electrons shared in the bond directly."],
      ans=0,
      why="EK 2.2.A.1 states that such graphs illustrate both the equilibrium bond length "
          "and the bond energy, which is exactly the pair of readings the keyed option "
          "names. Rates, masses and electron counts are read from other kinds of "
          "evidence."),

 dict(q="Using the tabulated ion pairs, which comparison correctly isolates the effect of "
        "charge alone?",
      table=_T_IONS,
      choices=[
        "Pair 1 against Pair 2, which have the same ion separation but different charges.",
        "Pair 1 against Pair 3, which have the same charges but different separations.",
        "Pair 3 against Pair 4, which differ in both charge and separation.",
        "Pair 2 against Pair 4, which differ in both charge and separation.",
        "No comparison in the table isolates charge, because every row differs in both "
        "respects."],
      ans=0,
      why="Isolating one variable means holding the other fixed, and exactly one pairing "
          "in the table shares a separation while differing in charge. EK 2.2.A.3 makes "
          "both quantities relevant, which is why a controlled comparison is needed to "
          "attribute an effect to either."),

 dict(q="For a given pair of atoms, what happens to the equilibrium bond length as the "
        "bond order increases from single to double to triple?",
      table=_T_ORDER,
      choices=[
        "It decreases at each step, and the bond energy rises at each step.",
        "It increases at each step, and the bond energy falls at each step.",
        "It decreases at each step, and the bond energy falls at each step.",
        "It stays constant, since the atoms are unchanged.",
        "It decreases from single to double and then increases from double to triple."],
      ans=0,
      why="EK 2.2.A.2 states that bonds with a higher order are shorter and have larger "
          "bond energies, and the tabulated values fall and rise respectively at every "
          "step. The atoms being unchanged is what makes bond order the variable rather "
          "than what makes the lengths equal."),

 dict(q="Two ionic compounds are compared. The first is built from a doubly charged "
        "cation and a doubly charged anion; the second from a singly charged cation and "
        "a singly charged anion at a slightly smaller separation. What does the framework "
        "allow you to say?",
      table=_T_IONS,
      choices=[
        "Both charge and separation affect the interaction, so the comparison requires "
        "weighing the larger charges against the smaller separation.",
        "The second must be stronger, because separation always outweighs charge.",
        "The first must be stronger, because charge always outweighs separation.",
        "Neither can be compared, because Coulomb's law applies only when charges are "
        "equal.",
        "The two must be equal, because one factor favors each compound."],
      ans=0,
      why="EK 2.2.A.3 makes the interaction strength depend on the charge on each ion and "
          "on the distance between the ion centers, and it ranks neither factor above the "
          "other. When the two point in opposite directions the framework licenses no "
          "shortcut, only the combined comparison."),

 dict(q="A potential energy curve for a pair of atoms never dips below zero at any "
        "separation. What does that indicate?",
      choices=[
        "No stable bond forms between them, since there is no separation at which the "
        "atoms are lower in energy than when apart.",
        "A very strong bond forms, since the energy stays high.",
        "The bond order must be three, since higher orders raise the energy.",
        "The equilibrium bond length is zero.",
        "The two atoms must be identical, since identical atoms give no minimum."],
      ans=0,
      why="EK 2.2.A.1 makes the equilibrium bond length the separation at which the "
          "potential energy is lowest and the bond energy the energy required to separate "
          "the atoms, so a curve with no minimum below the separated-atom value offers no "
          "separation the atoms would settle at and no energy to be recovered by pulling "
          "them apart."),
]
