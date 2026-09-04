# AP CHEMISTRY 6.6 Introduction to Enthalpy of Reaction
# CED effective Fall 2024, Unit 6 Thermochemistry.
# Learning objective 6.6.A: calculate the heat q absorbed or released by a system
# undergoing a chemical reaction in relationship to the amount of the reacting substance in
# moles and the molar enthalpy of reaction. Suggested skill 5.F, calculate, estimate, or
# predict an unknown quantity from known quantities by selecting and following a logical
# computational pathway and attending to precision.
#
# Essential knowledge relied on, in the framework's own words:
#   6.6.A.1  The enthalpy change of a reaction gives the amount of heat energy released
#            (for negative values) or absorbed (for positive values) by a chemical reaction
#            at constant pressure.
#   6.6.A.2  When the products of a reaction are at a different temperature than their
#            surroundings, they exchange energy with the surroundings to reach thermal
#            equilibrium. Thermal energy is transferred to the surroundings as the
#            reactants convert to products in an exothermic reaction. Thermal energy is
#            transferred from the surroundings as the reactants convert to products in an
#            endothermic reaction.
#   6.6.A.3  The chemical potential energy of the products of a reaction is different from
#            that of the reactants because of the breaking and forming of bonds. The energy
#            difference results in a change in the kinetic energy of the particles, which
#            manifests as a temperature change.
#            Exclusion Statement: The technical distinctions between enthalpy and internal
#            energy will not be assessed on the AP Exam. Most reactions studied at the AP
#            level are carried out at constant pressure, where the enthalpy change of the
#            process is equal to the heat (and by extension, the energy) of reaction.
#
# THE SIGN CONVENTION IS THE TOPIC. EK 6.6.A.1 attaches NEGATIVE to released and POSITIVE
# to absorbed, in one sentence, and every other statement in the topic hangs off it. There
# are exactly two ways to get an item here wrong -- pair the sign with the wrong direction,
# or pair the direction with the wrong sign -- so the six items that turn on it are built
# as full two-by-two sets: for the keyed pairing there is always a distractor carrying the
# SAME sign word with the opposite direction, and another carrying the same direction with
# the opposite sign. verify_h6_6.py asserts that structure item by item, so an item cannot
# quietly decay into one answerable from the word "negative" alone.
#
# THE EXCLUSION STATEMENT IS OBEYED, AND ITS SECOND HALF IS USED. The framework says the
# technical distinctions between enthalpy and internal energy will not be assessed, and no
# item here mentions internal energy at all -- not even as a distractor, because choosing
# among options that require the distinction IS assessing it. What the same statement DOES
# license is used: at constant pressure the enthalpy change of the process equals the heat
# of reaction, which is item 28.
#
# THE THREE-LINK CHAIN OF EK 6.6.A.3 is the most distinctive thing in this topic and the
# easiest to state with a link missing: bonds break and form, so the chemical POTENTIAL
# energy of the products differs from the reactants; that difference appears as a change in
# the KINETIC energy of the particles; and that is what a thermometer reads as a
# temperature change. Items 7, 8, 9, 24 and 30 take it one link at a time and then whole,
# and no key here skips from bonds straight to temperature.
#
# SCOPE. 6.7 owns the average bond energies and the calculation built on them, and no item
# here computes an enthalpy from bonds -- the breaking and forming of bonds is named only
# as EK 6.6.A.3 names it, as the REASON the potential energies differ. 6.8 owns the
# standard enthalpies of formation and 6.9 owns Hess's law. 6.4 owns q = mc(delta T).
#
# NOTATION. export_units.py does not typeset Chemistry, so the two spans below are
# hand-written with a space on each side. Molar enthalpies elsewhere are plain text with an
# explicit sign, as "-92 kJ/mol", and every keyed choice that carries a sign also carries
# the word released or absorbed, so the two can never drift apart.
TOPIC = ("6.6", "Introduction to Enthalpy of Reaction", 6)

_T_RXN = dict(
    headers=["Reaction", "Molar enthalpy of reaction (kJ/mol)"],
    rows=[["Reaction A", "-92"],
          ["Reaction B", "+180"],
          ["Reaction C", "-566"],
          ["Reaction D", "+57"],
          ["Reaction E", "-46"]])

QUESTIONS = [

 dict(q="A chemical reaction has an enthalpy change of \\( \\Delta H = -92\\ "
        "\\mathrm{kJ/mol} \\) . What does the negative value report?",
      choices=[
        "That heat is released, since a negative enthalpy change reports energy given out",
        "That heat is absorbed, since a negative enthalpy change reports energy taken in",
        "That heat is released, since a positive enthalpy change reports energy given out",
        "That the reaction reaches completion quickly",
        "That the reaction is carried out at constant volume"],
      ans=0,
      why="EK 6.6.A.1 states that the enthalpy change of a reaction gives the amount of "
          "heat energy released for negative values, so the sign and the direction are "
          "fixed together in the framework's own sentence."),

 dict(q="A different reaction has an enthalpy change of \\( \\Delta H = +57\\ "
        "\\mathrm{kJ/mol} \\) . What does the positive value report?",
      choices=[
        "That heat is absorbed, since a positive enthalpy change reports energy taken in",
        "That heat is released, since a positive enthalpy change reports energy given out",
        "That heat is absorbed, since a negative enthalpy change reports energy taken in",
        "That the reaction produces more product than reactant",
        "That the reaction cannot occur at ordinary temperatures"],
      ans=0,
      why="EK 6.6.A.1 states that the enthalpy change gives the amount of heat energy "
          "absorbed for positive values, which is the second half of the same sentence "
          "that assigns released to negative values."),

 dict(q="Under what condition does the framework say the enthalpy change of a reaction "
        "gives the heat energy released or absorbed?",
      choices=[
        "At constant pressure",
        "At constant volume",
        "At constant temperature",
        "Only when the reaction is exothermic",
        "Only when no gas is produced"],
      ans=0,
      why="EK 6.6.A.1 ends with the words at constant pressure, and the framework's own "
          "exclusion note adds that most reactions studied at this level are carried out "
          "that way."),

 dict(q="In an exothermic reaction, which way does the framework say thermal energy is "
        "transferred as the reactants convert to products?",
      choices=[
        "To the surroundings",
        "From the surroundings",
        "Neither way, since the energy stays within the products",
        "Into the products, which retain it rather than passing it on",
        "In whichever direction the temperature of the room determines"],
      ans=0,
      why="EK 6.6.A.2 states that thermal energy is transferred to the surroundings as the "
          "reactants convert to products in an exothermic reaction."),

 dict(q="In an endothermic reaction, which way does the framework say thermal energy is "
        "transferred as the reactants convert to products?",
      choices=[
        "From the surroundings",
        "To the surroundings",
        "Neither way, since the reactants supply their own energy",
        "Out of the products and into the unreacted reactants",
        "In whichever direction the pressure determines"],
      ans=0,
      why="EK 6.6.A.2 states that thermal energy is transferred from the surroundings as "
          "the reactants convert to products in an endothermic reaction, which is the "
          "mirror of the exothermic case in the same statement."),

 dict(q="The products of a reaction end up at a different temperature from their "
        "surroundings. What does the framework say happens then, and why?",
      choices=[
        "They exchange energy with the surroundings, in order to reach thermal equilibrium",
        "They exchange matter with the surroundings, in order to reach thermal equilibrium",
        "They keep their temperature, since a product's temperature is fixed by the "
        "reaction",
        "They return to the reactants until the temperatures agree",
        "They exchange energy only if the reaction was exothermic"],
      ans=0,
      why="EK 6.6.A.2 opens by stating that when the products of a reaction are at a "
          "different temperature than their surroundings, they exchange energy with the "
          "surroundings to reach thermal equilibrium."),

 dict(q="Why does the framework say the chemical potential energy of the products of a "
        "reaction differs from that of the reactants?",
      choices=[
        "Because of the breaking and forming of bonds",
        "Because the products are always at a higher temperature",
        "Because the number of particles always changes during a reaction",
        "Because the products occupy a different volume",
        "Because energy is created as the reaction proceeds"],
      ans=0,
      why="EK 6.6.A.3 states that the chemical potential energy of the products of a "
          "reaction is different from that of the reactants because of the breaking and "
          "forming of bonds."),

 dict(q="According to the framework, what does that difference in chemical potential "
        "energy result in?",
      choices=[
        "A change in the kinetic energy of the particles",
        "A change in the mass of the particles",
        "A change in the number of particles",
        "A change in the pressure of the surroundings only",
        "No further change of any kind"],
      ans=0,
      why="EK 6.6.A.3 states that the energy difference results in a change in the kinetic "
          "energy of the particles, which is the middle link between the bonds and the "
          "thermometer."),

 dict(q="How does that change in the kinetic energy of the particles show itself?",
      choices=[
        "As a temperature change",
        "As a change in the color of the mixture",
        "As a change in the volume of the mixture",
        "As a change in the mass of the mixture",
        "It does not show itself in any measurable way"],
      ans=0,
      why="EK 6.6.A.3 closes by stating that the change in the kinetic energy of the "
          "particles manifests as a temperature change, which is what makes the enthalpy "
          "change observable at all."),

 dict(q="On which two quantities does the learning objective say the heat absorbed or "
        "released by a reacting system depends?",
      choices=[
        "The amount of the reacting substance in moles and the molar enthalpy of reaction",
        "The mass of the reacting substance and its specific heat capacity",
        "The molar enthalpy of reaction and the temperature of the surroundings",
        "The amount of the reacting substance in moles and the temperature change",
        "The pressure and the volume of the reacting system"],
      ans=0,
      why="Learning objective 6.6.A names exactly these two, the amount of the reacting "
          "substance in moles and the molar enthalpy of reaction, whose product is the "
          "heat q for the change."),

 dict(q="A reaction has a molar enthalpy of reaction of -46 kJ/mol. How much energy is "
        "involved when 3.00 mol of it takes place?",
      choices=[
        "138 kJ released",
        "138 kJ absorbed",
        "46 kJ released",
        "15.3 kJ released",
        "49 kJ released"],
      ans=0,
      why="Learning objective 6.6.A multiplies the amount in moles by the molar enthalpy of "
          "reaction, and EK 6.6.A.1 makes a negative value a release of heat, so the energy "
          "leaves the reacting system."),

 dict(q="A reaction of 2.00 mol releases 150 kJ of heat. What is the molar enthalpy of "
        "reaction?",
      choices=[
        "-75 kJ/mol, a negative value because the reaction released the energy",
        "-75 kJ/mol, a negative value because the reaction absorbed the energy",
        "+75 kJ/mol, a positive value because the reaction released the energy",
        "-300 kJ/mol, a negative value because the reaction released the energy",
        "-150 kJ/mol, a negative value because the reaction released the energy"],
      ans=0,
      why="Learning objective 6.6.A makes the heat the amount in moles times the molar "
          "enthalpy of reaction, so dividing by the amount returns the molar value, and EK "
          "6.6.A.1 makes a release of heat a negative enthalpy change."),

 dict(q="A reaction whose molar enthalpy of reaction is -92 kJ/mol releases 276 kJ. What "
        "amount of reaction took place?",
      choices=[
        "3.00 mol",
        "0.333 mol",
        "25392 mol",
        "184 mol",
        "92.0 mol"],
      ans=0,
      why="Learning objective 6.6.A makes the heat the amount in moles times the molar "
          "enthalpy of reaction, so dividing the energy released by the size of the molar "
          "enthalpy returns the amount that reacted."),

 dict(q="The molar enthalpies of reaction of five reactions have been measured. Which "
        "reaction releases the most energy per mole?",
      table=_T_RXN,
      choices=[
        "Reaction C",
        "Reaction A",
        "Reaction E",
        "Reaction B",
        "Reaction D"],
      ans=0,
      why="EK 6.6.A.1 makes a negative enthalpy change a release of heat and its size the "
          "amount released, so the most negative tabulated value marks the largest release "
          "per mole."),

 dict(q="Among those same five reactions, which absorbs the most energy per mole?",
      table=_T_RXN,
      choices=[
        "Reaction B",
        "Reaction D",
        "Reaction C",
        "Reaction A",
        "Reaction E"],
      ans=0,
      why="EK 6.6.A.1 makes a positive enthalpy change an absorption of heat and its size "
          "the amount absorbed, so the most positive tabulated value marks the largest "
          "absorption per mole."),

 dict(q="Which two of those five reactions are endothermic?",
      table=_T_RXN,
      choices=[
        "Reaction B and Reaction D",
        "Reaction A and Reaction E",
        "Reaction A and Reaction C",
        "Reaction C and Reaction E",
        "Reaction B and Reaction C"],
      ans=0,
      why="EK 6.6.A.1 assigns positive enthalpy changes to heat absorbed, and EK 6.6.A.2 "
          "calls a reaction that takes thermal energy from the surroundings endothermic, "
          "so the tabulated reactions with positive values are the pair."),

 dict(q="How much energy is involved when 2.00 mol of Reaction A takes place?",
      table=_T_RXN,
      choices=[
        "184 kJ released",
        "184 kJ absorbed",
        "92 kJ released",
        "46 kJ released",
        "94 kJ released"],
      ans=0,
      why="Learning objective 6.6.A multiplies the amount in moles by the tabulated molar "
          "enthalpy of reaction, and EK 6.6.A.1 makes that negative value a release of "
          "heat."),

 dict(q="How much energy is involved when 0.500 mol of Reaction D takes place?",
      table=_T_RXN,
      choices=[
        "28.5 kJ absorbed",
        "28.5 kJ released",
        "57 kJ absorbed",
        "114 kJ absorbed",
        "57.5 kJ absorbed"],
      ans=0,
      why="Learning objective 6.6.A multiplies the amount in moles by the tabulated molar "
          "enthalpy of reaction, and EK 6.6.A.1 makes that positive value an absorption of "
          "heat."),

 dict(q="Which of those five reactions transfers the least energy per mole, in either "
        "direction?",
      table=_T_RXN,
      choices=[
        "Reaction E",
        "Reaction D",
        "Reaction A",
        "Reaction B",
        "Reaction C"],
      ans=0,
      why="EK 6.6.A.1 makes the SIZE of the enthalpy change the amount of heat released or "
          "absorbed, with the sign giving only the direction, so the tabulated value "
          "closest to zero marks the smallest transfer."),

 dict(q="A reaction has a molar enthalpy of reaction of +57 kJ/mol. Does its flask warm or "
        "cool as the reaction proceeds?",
      choices=[
        "It cools, because a positive enthalpy change means energy is absorbed from the "
        "surroundings",
        "It warms, because a positive enthalpy change means energy is released to the "
        "surroundings",
        "It cools, because a negative enthalpy change means energy is absorbed from the "
        "surroundings",
        "It neither warms nor cools, since the enthalpy change concerns only the reactants",
        "It warms, because every reaction warms its surroundings as it proceeds"],
      ans=0,
      why="EK 6.6.A.1 makes a positive enthalpy change an absorption of heat, and EK "
          "6.6.A.2 has thermal energy transferred FROM the surroundings in an endothermic "
          "reaction, which leaves them cooler."),

 dict(q="A reaction flask becomes hot to the touch as the reaction proceeds. What is the "
        "sign of the enthalpy change, and why?",
      choices=[
        "Negative, because heat was released to the surroundings",
        "Negative, because heat was absorbed from the surroundings",
        "Positive, because heat was released to the surroundings",
        "Positive, because heat was absorbed from the surroundings",
        "It cannot be decided from a temperature change alone"],
      ans=0,
      why="EK 6.6.A.2 sends thermal energy to the surroundings in an exothermic reaction, "
          "which is what warms the flask, and EK 6.6.A.1 attaches negative values to heat "
          "released."),

 dict(q="Two reactions have molar enthalpies of reaction of -100 kJ/mol and +100 kJ/mol. "
        "What do they have in common, and how do they differ?",
      choices=[
        "They transfer the same amount of energy per mole, in opposite directions",
        "They transfer the same amount of energy per mole, in the same direction",
        "They transfer different amounts of energy per mole, in opposite directions",
        "They transfer no energy at all, since the two values cancel",
        "They cannot be compared, since one is negative"],
      ans=0,
      why="EK 6.6.A.1 makes the size of the enthalpy change the amount of heat and its "
          "sign the direction, so equal sizes with opposite signs are equal transfers "
          "running opposite ways."),

 dict(q="A chemist doubles the amount of reactant used. What happens to the heat "
        "transferred, and to the molar enthalpy of reaction?",
      choices=[
        "The heat transferred doubles and the molar enthalpy of reaction is unchanged",
        "Both the heat transferred and the molar enthalpy of reaction double",
        "The heat transferred is unchanged and the molar enthalpy of reaction doubles",
        "Neither changes, since the reaction is the same reaction",
        "The heat transferred doubles and the molar enthalpy of reaction is halved"],
      ans=0,
      why="Learning objective 6.6.A makes the heat the amount in moles times the molar "
          "enthalpy of reaction, so the amount is what scales; the molar enthalpy is a "
          "property of the reaction itself and is stated per mole."),

 dict(q="Put the framework's account of a reaction's temperature change in order, from "
        "first to last.",
      choices=[
        "Bonds break and form, the chemical potential energy changes, the kinetic energy "
        "of the particles changes, and a temperature change is observed",
        "The temperature changes, the kinetic energy of the particles changes, the "
        "chemical potential energy changes, and bonds break and form",
        "Bonds break and form, the kinetic energy of the particles changes, the chemical "
        "potential energy changes, and a temperature change is observed",
        "The chemical potential energy changes, bonds break and form, a temperature change "
        "is observed, and the kinetic energy of the particles changes",
        "Bonds break and form and a temperature change is observed, with no change in "
        "energy of any other kind"],
      ans=0,
      why="EK 6.6.A.3 runs in exactly this order: the breaking and forming of bonds makes "
          "the products' chemical potential energy differ from the reactants', that "
          "difference results in a change in the kinetic energy of the particles, and that "
          "manifests as a temperature change."),

 dict(q="A reaction is carried out and the surroundings show no temperature change at all. "
        "What does that suggest about the enthalpy change of the reaction?",
      choices=[
        "That it is close to zero, since the enthalpy change gives the heat released or "
        "absorbed",
        "That it is large and negative, since no change means no loss",
        "That it is large and positive, since no change means no gain",
        "That the reaction did not occur, since every reaction changes the temperature",
        "Nothing at all, since the enthalpy change and the temperature are unconnected"],
      ans=0,
      why="EK 6.6.A.1 makes the enthalpy change the amount of heat released or absorbed, "
          "and EK 6.6.A.3 makes a temperature change how that energy difference shows "
          "itself, so an unmoved thermometer reports little heat either way."),

 dict(q="A reaction has a molar enthalpy of reaction of +180 kJ/mol. How much energy is "
        "involved when 0.250 mol of it takes place?",
      choices=[
        "45.0 kJ absorbed",
        "45.0 kJ released",
        "180 kJ absorbed",
        "720 kJ absorbed",
        "180.25 kJ absorbed"],
      ans=0,
      why="Learning objective 6.6.A multiplies the amount in moles by the molar enthalpy of "
          "reaction, and EK 6.6.A.1 makes a positive value an absorption of heat, so the "
          "energy enters the reacting system."),

 dict(q="A student says that a reaction with a large positive enthalpy change releases a "
        "great deal of energy. What is wrong with the claim?",
      choices=[
        "A positive enthalpy change reports energy taken in by the reaction",
        "A positive enthalpy change reports energy given out by the reaction",
        "A negative enthalpy change reports energy taken in by the reaction",
        "Nothing; a large enthalpy change of either sign means a great deal of energy "
        "leaves the reacting system",
        "The size of the enthalpy change says nothing about how much energy is transferred"],
      ans=0,
      why="EK 6.6.A.1 assigns released to negative values and absorbed to positive values, "
          "so a large positive enthalpy change reports a large absorption; the size is "
          "right in the claim and the direction is not."),

 dict(q="At the level of this course, what is the enthalpy change of a reaction taken to "
        "be equal to?",
      choices=[
        "The heat of the reaction, since these reactions are carried out at constant "
        "pressure",
        "The heat of the reaction, since these reactions are carried out at constant volume",
        "The temperature change of the surroundings",
        "The amount of the reacting substance in moles",
        "The kinetic energy of the reactant particles"],
      ans=0,
      why="EK 6.6.A.1 gives the enthalpy change as the heat released or absorbed at "
          "constant pressure, and the framework's own note adds that most reactions studied "
          "at this level are carried out at constant pressure, where the enthalpy change of "
          "the process equals the heat of reaction."),

 dict(q="The products of a reaction are formed hotter than the surroundings. What does the "
        "framework say happens next, and how does it end?",
      choices=[
        "They transfer energy to the surroundings until thermal equilibrium is reached",
        "They transfer energy from the surroundings until thermal equilibrium is reached",
        "They stay hotter than the surroundings indefinitely",
        "They convert back into the reactants until the temperatures agree",
        "They transfer energy to the surroundings until they are colder than the "
        "surroundings"],
      ans=0,
      why="EK 6.6.A.2 states that when the products of a reaction are at a different "
          "temperature than their surroundings they exchange energy with the surroundings "
          "to reach thermal equilibrium, and hotter products are the ones giving energy up."),

 dict(q="How does the framework connect what happens to the bonds in a reaction with what "
        "a thermometer in the mixture reads?",
      choices=[
        "Breaking and forming bonds changes the chemical potential energy, the difference "
        "appears as kinetic energy of the particles, and that is read as a temperature "
        "change",
        "Breaking and forming bonds changes the kinetic energy of the particles, the "
        "difference appears as chemical potential energy, and that is read as a "
        "temperature change",
        "Breaking and forming bonds changes the temperature directly, with no change in "
        "any other form of energy",
        "Breaking and forming bonds changes the number of particles, and a thermometer "
        "reads that as a temperature change",
        "Breaking and forming bonds has no effect a thermometer can read"],
      ans=0,
      why="EK 6.6.A.3 states the chain in this order: the bonds make the products' "
          "chemical potential energy differ from the reactants', the energy difference "
          "results in a change in the kinetic energy of the particles, and that manifests "
          "as a temperature change."),
]
