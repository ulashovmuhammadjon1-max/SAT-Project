# AP CHEMISTRY 6.1 Endothermic and Exothermic Processes
# CED effective Fall 2024, Unit 6 Thermochemistry.
# Learning objective 6.1.A: explain the relationship between experimental observations and
# energy changes associated with a chemical or physical transformation. Suggested skill
# 6.D, provide reasoning to justify a claim using chemical principles or laws, or using
# mathematical justification.
#
# Essential knowledge relied on, in the framework's own words:
#   6.1.A.1  Temperature changes in a system indicate energy changes.
#   6.1.A.2  Energy changes in a system can be described as endothermic and exothermic
#            processes such as the heating or cooling of a substance, phase changes, or
#            chemical transformations.
#   6.1.A.3  When a chemical reaction occurs, the energy of the system either decreases
#            (exothermic reaction), increases (endothermic reaction), or remains the same.
#            For exothermic reactions, the energy lost by the reacting species (system) is
#            gained by the surroundings, as heat transfer from or work done by the system.
#            Likewise, for endothermic reactions, the system gains energy from the
#            surroundings by heat transfer to or work done on the system.
#   6.1.A.4  The formation of a solution may be an exothermic or endothermic process,
#            depending on the relative strengths of intermolecular/interparticle
#            interactions before and after the dissolution process.
#
# THE LEARNING OBJECTIVE IS AN OBSERVATION-TO-ENERGY LINK, so the items are built the way
# the objective is written: a measurement is stated, and the question is what it tells you
# about the energy of the system. Every table below is a set of measured temperatures, and
# verify_h6_1.py subtracts them itself.
#
# THE SWAP THAT MUST NOT SHIP. EK 6.1.A.3 pairs a DECREASE in the energy of the system
# with the word EXOTHERMIC and with energy flowing OUT to the surroundings, and an
# increase with ENDOTHERMIC and energy flowing in. Every one of those three clauses can be
# stated backwards and still read fluently, so every keyed choice that names a direction
# also names where the energy went, and verify_h6_1.py checks the direction word against a
# SIGNED temperature change recomputed from the table -- never against a magnitude.
#
# SCOPE, so that the nine unit 6 topics do not write each other's questions. 6.2 owns the
# energy DIAGRAM as a representation. 6.3 owns the particle-level account -- average
# kinetic energy, collisions, thermal equilibrium -- and no item here explains a transfer
# through collisions. 6.4 owns q = mc(delta T), the specific heat capacity and the
# calorimeter, and NO item here computes a heat. 6.5 owns the molar enthalpy of a phase
# change and 6.6 the molar enthalpy of reaction, so no item here carries a value in
# kJ/mol for a reaction or a phase change, and the word enthalpy does not appear.
# verify_h6_1.py asserts all of that.
#
# ONE CROSSING IS DELIBERATE, and it is recorded here so it is not mistaken for drift.
# Item 22 makes the logical point that EK 6.1.A.1 runs one way only: a temperature change
# indicates an energy change, but the absence of one does not indicate the absence of
# energy transfer, because EK 6.5.A.1 keeps the temperature of a pure substance constant
# through a phase change. That is the only place 6.5's sentence is used, and 6.5 keeps all
# of the arithmetic.
#
# THE INTERACTION TABLE IS NOT BOND ENTHALPY. EK 6.1.A.4 turns on the relative strengths
# of INTERMOLECULAR or interparticle interactions broken and formed on dissolving, which
# is a different quantity from the average covalent bond energies EK 6.7.A.2 uses. The
# table states both amounts for each system, so the comparison is arithmetic rather than
# recall, and 6.7's items are about reactions rather than solutions.
#
# NOTATION. export_units.py does not typeset Chemistry. Nothing here needs a math span:
# temperatures are written as plain numbers and "degrees Celsius" is spelled out, because
# a raw degree glyph reaches a student as a raw degree glyph.
TOPIC = ("6.1", "Endothermic and Exothermic Processes", 6)

_T_DISSOLVING = dict(
    headers=["Salt", "Temperature of the water before (degrees Celsius)",
             "Temperature of the solution after (degrees Celsius)"],
    rows=[["Ammonium nitrate", "21.0", "13.4"],
          ["Calcium chloride", "21.0", "31.6"],
          ["Potassium bromide", "21.0", "18.2"],
          ["Lithium chloride", "21.0", "27.5"],
          ["Sodium chloride", "21.0", "20.8"]])

_T_REACTIONS = dict(
    headers=["Mixture", "Temperature of the mixture before (degrees Celsius)",
             "Temperature of the mixture after (degrees Celsius)"],
    rows=[["Mixture V", "22.0", "20.9"],
          ["Mixture W", "22.0", "30.4"],
          ["Mixture X", "22.0", "16.8"],
          ["Mixture Y", "22.0", "22.0"],
          ["Mixture Z", "22.0", "34.9"]])

_T_INTERACTIONS = dict(
    headers=["System",
             "Energy needed to separate the original particles (kJ/mol)",
             "Energy released as the new interactions form (kJ/mol)"],
    rows=[["System P", "780", "812"],
          ["System Q", "640", "598"],
          ["System R", "910", "910"],
          ["System S", "455", "470"],
          ["System T", "300", "268"]])

QUESTIONS = [

 dict(q="A student measures the temperature of a system before and after a "
        "transformation and finds that it has changed. According to the framework, what "
        "does that observation indicate?",
      choices=[
        "That the energy of the system has changed",
        "That the mass of the system has changed",
        "That a gas must have been produced",
        "That the system has reached equilibrium",
        "That the transformation is complete"],
      ans=0,
      why="EK 6.1.A.1 states that temperature changes in a system indicate energy "
          "changes. Nothing in the framework ties a temperature change to a change in "
          "mass, to the production of a gas, or to the state of completion."),

 dict(q="Which kinds of process does the framework say can be described as endothermic "
        "or exothermic?",
      choices=[
        "The heating or cooling of a substance, a phase change, or a chemical "
        "transformation",
        "A chemical transformation and nothing else",
        "A phase change and nothing else",
        "Only a process that changes the mass of the system",
        "Only a process carried out in a sealed container"],
      ans=0,
      why="EK 6.1.A.2 states that energy changes in a system can be described as "
          "endothermic and exothermic processes such as the heating or cooling of a "
          "substance, phase changes, or chemical transformations. All three are named."),

 dict(q="When a chemical reaction occurs, what are the possibilities the framework "
        "allows for the energy of the system?",
      choices=[
        "It decreases, it increases, or it remains the same",
        "It always decreases",
        "It always increases",
        "It decreases only when a gas is produced",
        "It changes only when work is done on the system"],
      ans=0,
      why="EK 6.1.A.3 opens by stating that when a chemical reaction occurs, the energy "
          "of the system either decreases, increases, or remains the same. The third "
          "possibility is stated as plainly as the first two."),

 dict(q="A reaction occurs in which the energy of the system decreases. What is such a "
        "reaction called, and what becomes of the energy?",
      choices=[
        "Exothermic, and the energy lost by the reacting species is gained by the "
        "surroundings",
        "Endothermic, and the energy lost by the reacting species is gained by the "
        "surroundings",
        "Exothermic, and the energy is destroyed rather than transferred",
        "Endothermic, and the system takes the energy from the surroundings",
        "Exothermic, and the surroundings lose an equal amount of energy to the system"],
      ans=0,
      why="EK 6.1.A.3 names a reaction in which the energy of the system decreases an "
          "exothermic reaction, and states that the energy lost by the reacting species, "
          "which is the system, is gained by the surroundings."),

 dict(q="A reaction occurs in which the energy of the system increases. What is such a "
        "reaction called, and where does the energy come from?",
      choices=[
        "Endothermic, and the system gains the energy from the surroundings",
        "Exothermic, and the system gains the energy from the surroundings",
        "Endothermic, and the energy is created within the system",
        "Exothermic, and the surroundings gain the energy from the system",
        "Endothermic, and the surroundings gain an equal amount of energy as well"],
      ans=0,
      why="EK 6.1.A.3 names a reaction in which the energy of the system increases an "
          "endothermic reaction, and states that the system gains energy from the "
          "surroundings by heat transfer to or work done on the system."),

 dict(q="By what routes does the framework say energy passes between a reacting system "
        "and its surroundings?",
      choices=[
        "By heat transfer and by work",
        "By heat transfer alone",
        "By work alone",
        "By a transfer of mass between the two",
        "By a change in the temperature of the surroundings alone"],
      ans=0,
      why="EK 6.1.A.3 names both routes twice over: for exothermic reactions the energy "
          "is gained by the surroundings as heat transfer from or work done by the "
          "system, and for endothermic reactions by heat transfer to or work done on it."),

 dict(q="Is the formation of a solution an endothermic process or an exothermic one?",
      choices=[
        "Either is possible, and which one occurs depends on the relative strengths of "
        "the interactions before and after dissolution",
        "Always exothermic, because forming a solution releases energy",
        "Always endothermic, because the original particles must be separated",
        "Always exothermic when the solvent is water",
        "Neither, because dissolving is a physical rather than a chemical change"],
      ans=0,
      why="EK 6.1.A.4 states that the formation of a solution may be an exothermic or "
          "endothermic process, depending on the relative strengths of the "
          "intermolecular or interparticle interactions before and after the dissolution "
          "process. Neither outcome is the rule."),

 dict(q="A salt dissolves in water and the solution becomes colder. What does that "
        "observation say about the interactions involved?",
      choices=[
        "The new interactions formed release less energy than separating the original "
        "particles required, so the dissolution is endothermic",
        "The new interactions formed release more energy than separating the original "
        "particles required, so the dissolution is exothermic",
        "The dissolution is endothermic because separating the original particles is the "
        "only step in which energy is involved at all",
        "No interactions were broken, since the salt simply spread through the water",
        "The water molecules stopped interacting with one another"],
      ans=0,
      why="EK 6.1.A.4 makes the direction depend on the relative strengths of the "
          "interactions before and after dissolution, and EK 6.1.A.1 makes the fall in "
          "temperature a sign that the system took energy from the water around it."),

 dict(q="A different salt dissolves in water and the solution becomes warmer. What does "
        "that observation say about the interactions involved?",
      choices=[
        "The new interactions formed release more energy than separating the original "
        "particles required, so the dissolution is exothermic",
        "The new interactions formed release less energy than separating the original "
        "particles required, so the dissolution is endothermic",
        "The dissolution is exothermic because forming any new interaction always gives "
        "back more than breaking the old ones costs",
        "The water gained mass and therefore gained energy",
        "The original particles were already separated before mixing"],
      ans=0,
      why="EK 6.1.A.4 makes the direction depend on the relative strengths of the "
          "interactions before and after dissolution, and EK 6.1.A.3 has the energy lost "
          "by an exothermic system gained by the surroundings, which is the water here."),

 dict(q="Equal amounts of five salts were each dissolved in the same volume of water at "
        "the same starting temperature. For which salt does the dissolution release the "
        "most energy to the water?",
      table=_T_DISSOLVING,
      choices=[
        "Calcium chloride",
        "Lithium chloride",
        "Ammonium nitrate",
        "Potassium bromide",
        "Sodium chloride"],
      ans=0,
      why="EK 6.1.A.3 has the energy lost by an exothermic system gained by the "
          "surroundings, and EK 6.1.A.1 makes a rise in the water's temperature the sign "
          "of that gain, so the largest rise marks the largest release."),

 dict(q="Using the same set of measurements, for which salt does the dissolution take "
        "the most energy from the water?",
      table=_T_DISSOLVING,
      choices=[
        "Ammonium nitrate",
        "Potassium bromide",
        "Sodium chloride",
        "Calcium chloride",
        "Lithium chloride"],
      ans=0,
      why="EK 6.1.A.3 has an endothermic system gain energy from its surroundings, and "
          "EK 6.1.A.1 makes the fall in the water's temperature the sign of that loss, so "
          "the largest fall marks the largest amount taken."),

 dict(q="Which two of the tabulated dissolutions are exothermic processes?",
      table=_T_DISSOLVING,
      choices=[
        "Calcium chloride and lithium chloride",
        "Ammonium nitrate and potassium bromide",
        "Potassium bromide and sodium chloride",
        "Calcium chloride and ammonium nitrate",
        "Lithium chloride and sodium chloride"],
      ans=0,
      why="EK 6.1.A.3 makes a process exothermic when the system loses energy to its "
          "surroundings, and EK 6.1.A.1 makes the warming of the water the observation "
          "that reports it, so the two solutions whose temperature rose are the pair."),

 dict(q="Which tabulated dissolution is endothermic but changes the temperature of the "
        "water least?",
      table=_T_DISSOLVING,
      choices=[
        "Sodium chloride",
        "Potassium bromide",
        "Ammonium nitrate",
        "Calcium chloride",
        "Lithium chloride"],
      ans=0,
      why="EK 6.1.A.1 ties the size of the temperature change to the size of the energy "
          "change, so among the dissolutions whose solutions cooled, the smallest fall is "
          "the smallest energy transfer."),

 dict(q="Five reaction mixtures were prepared at the same starting temperature and their "
        "temperatures measured again once each reaction had finished. In which mixture "
        "did the reacting species take the most energy from the surroundings?",
      table=_T_REACTIONS,
      choices=[
        "Mixture X",
        "Mixture V",
        "Mixture Y",
        "Mixture W",
        "Mixture Z"],
      ans=0,
      why="EK 6.1.A.3 has an endothermic system gain energy from the surroundings, and "
          "EK 6.1.A.1 makes the cooling of the mixture the observation of that gain, so "
          "the largest fall in temperature marks the largest transfer inward."),

 dict(q="Using the same five mixtures, in which one did the reaction release the most "
        "energy to the surroundings?",
      table=_T_REACTIONS,
      choices=[
        "Mixture Z",
        "Mixture W",
        "Mixture V",
        "Mixture X",
        "Mixture Y"],
      ans=0,
      why="EK 6.1.A.3 has the energy lost by an exothermic system gained by the "
          "surroundings, and EK 6.1.A.1 makes the warming of the mixture the observation "
          "of that, so the largest rise marks the largest release."),

 dict(q="In which of the five mixtures is the energy of the reacting system, so far as "
        "the measurements show, unchanged?",
      table=_T_REACTIONS,
      choices=[
        "Mixture Y",
        "Mixture V",
        "Mixture W",
        "Mixture X",
        "Mixture Z"],
      ans=0,
      why="EK 6.1.A.3 allows a reaction in which the energy of the system remains the "
          "same, and EK 6.1.A.1 makes a temperature change the indicator of an energy "
          "change, so the mixture that did not change temperature is the one."),

 dict(q="A student claims that only chemical reactions can be called endothermic or "
        "exothermic. What is wrong with the claim?",
      choices=[
        "The heating or cooling of a substance and phase changes are also described that "
        "way",
        "Nothing, since the two words apply only to reactions",
        "The two words apply only to processes carried out in a calorimeter",
        "The two words apply only to processes that change the temperature of a solution",
        "The two words apply only to processes that produce a gas"],
      ans=0,
      why="EK 6.1.A.2 lists the heating or cooling of a substance and phase changes "
          "alongside chemical transformations as the processes that energy changes in a "
          "system can be described as endothermic or exothermic."),

 dict(q="Steam condenses on a cold window pane and the pane becomes warmer. What does "
        "that observation indicate about the condensation?",
      choices=[
        "It is exothermic, because energy has passed from the condensing water to the "
        "pane around it",
        "It is endothermic, because energy has passed from the condensing water to the "
        "pane around it",
        "It is exothermic, because the pane has given energy to the condensing water",
        "It is endothermic, because the pane has given energy to the condensing water",
        "Neither, because a phase change is not an energy change"],
      ans=0,
      why="EK 6.1.A.2 counts a phase change among the processes described as endothermic "
          "or exothermic, and EK 6.1.A.3 has the energy lost by an exothermic system "
          "gained by the surroundings, which the warming of the pane reports under EK "
          "6.1.A.1."),

 dict(q="A volatile liquid evaporates from a person's skin and the skin feels cool. What "
        "does that observation indicate about the evaporation?",
      choices=[
        "It is endothermic, because the evaporating liquid has taken energy from the skin",
        "It is exothermic, because the evaporating liquid has taken energy from the skin",
        "It is endothermic, because the skin has taken energy from the evaporating liquid",
        "It is exothermic, because the skin has taken energy from the evaporating liquid",
        "Neither, because evaporation removes matter rather than energy"],
      ans=0,
      why="EK 6.1.A.2 counts a phase change among the processes described as endothermic "
          "or exothermic, and EK 6.1.A.3 has an endothermic system gain energy from its "
          "surroundings, which the cooling of the skin reports under EK 6.1.A.1."),

 dict(q="Can a chemical reaction occur without the energy of the system changing at all?",
      choices=[
        "Yes, since the framework lists remaining the same alongside decreasing and "
        "increasing",
        "No, since every reaction breaks and forms bonds and so must change the energy",
        "No, since every reaction changes the temperature of its surroundings",
        "Only if the reaction is carried out in a sealed container",
        "Only if no products are formed"],
      ans=0,
      why="EK 6.1.A.3 states three possibilities when a chemical reaction occurs: the "
          "energy of the system decreases, increases, or remains the same. The third is "
          "part of the statement, not an omission from it."),

 dict(q="A reaction in a cylinder pushes a piston outward, and no energy leaves the "
        "cylinder as heat. Has the system lost energy to its surroundings?",
      choices=[
        "Yes, because work done by the system is a route by which energy reaches the "
        "surroundings",
        "No, because energy leaves a system only by heat transfer",
        "No, because pushing a piston is a mechanical effect rather than an energy change",
        "Yes, but only if the cylinder also becomes cooler",
        "It cannot be decided without knowing the mass of the piston"],
      ans=0,
      why="EK 6.1.A.3 states that for exothermic reactions the energy lost by the system "
          "is gained by the surroundings as heat transfer FROM or work done BY the "
          "system, so work is named as a route in the framework's own sentence."),

 dict(q="While a pure substance melts, its temperature does not change. Does that mean "
        "no energy is being transferred?",
      choices=[
        "No, because the temperature of a pure substance stays constant through a phase "
        "change even while energy is transferred",
        "Yes, because an unchanged temperature always means an unchanged energy",
        "Yes, because melting is a physical rather than a chemical change",
        "No, because the temperature is in fact rising too slowly to measure",
        "It cannot be decided without knowing the mass of the substance"],
      ans=0,
      why="EK 6.1.A.1 says a temperature change indicates an energy change; it does not "
          "say the reverse. EK 6.5.A.1 states that the temperature of a pure substance "
          "remains constant during a phase change, so energy can be transferred with the "
          "thermometer standing still."),

 dict(q="Breaking the inner pouch of a cold pack lets a salt dissolve in water, and the "
        "pack becomes cold to the touch. How should the dissolution be described?",
      choices=[
        "Endothermic, because the dissolving salt and water take energy from their "
        "surroundings",
        "Exothermic, because the dissolving salt and water take energy from their "
        "surroundings",
        "Endothermic, because the surroundings take energy from the dissolving salt and "
        "water",
        "Exothermic, because the surroundings take energy from the dissolving salt and "
        "water",
        "Neither, because the cooling is caused by the pouch breaking rather than by the "
        "dissolution"],
      ans=0,
      why="EK 6.1.A.4 allows the formation of a solution to be endothermic, and EK "
          "6.1.A.3 has an endothermic system gain energy from its surroundings, which is "
          "what the hand feels as cold under EK 6.1.A.1."),

 dict(q="Five salts were dissolved in water, and for each the energy needed to separate "
        "the original particles and the energy released as the new interactions form were "
        "determined. Which dissolution is exothermic and releases the most energy "
        "overall?",
      table=_T_INTERACTIONS,
      choices=[
        "System P",
        "System S",
        "System Q",
        "System T",
        "System R"],
      ans=0,
      why="EK 6.1.A.4 makes the direction of the energy change depend on the relative "
          "strengths of the interactions before and after dissolution, so the system "
          "whose tabulated release exceeds its tabulated requirement by the most releases "
          "the most."),

 dict(q="Among the same five systems, which dissolution is endothermic and takes the "
        "most energy from the surroundings?",
      table=_T_INTERACTIONS,
      choices=[
        "System Q",
        "System T",
        "System P",
        "System S",
        "System R"],
      ans=0,
      why="EK 6.1.A.4 makes the comparison of the two amounts decide the direction, and "
          "EK 6.1.A.3 has an endothermic system gain energy from its surroundings, so the "
          "largest shortfall is the largest amount taken in."),

 dict(q="Among the same five systems, in which one does forming the solution leave the "
        "energy of the system unchanged?",
      table=_T_INTERACTIONS,
      choices=[
        "System R",
        "System P",
        "System Q",
        "System S",
        "System T"],
      ans=0,
      why="EK 6.1.A.4 compares the strengths of the interactions before and after "
          "dissolution, so when the tabulated energy released exactly matches the "
          "tabulated energy required, neither an increase nor a decrease is left."),

 dict(q="A reaction is carried out in a beaker of water, and the water is used to follow "
        "the energy change. In the framework's terms, what is the system?",
      choices=[
        "The reacting species",
        "The water in the beaker",
        "The beaker itself",
        "The thermometer",
        "The room in which the experiment is done"],
      ans=0,
      why="EK 6.1.A.3 writes of the energy lost by the reacting species and then names "
          "them, in parentheses, as the system. The water is what gains that energy, "
          "which makes it part of the surroundings rather than the system."),

 dict(q="One student says an exothermic reaction lost energy and another says its "
        "surroundings gained energy. Can both be right?",
      choices=[
        "Yes, because the energy lost by the reacting species is the energy gained by the "
        "surroundings",
        "No, because energy cannot both be lost and be gained",
        "No, because only the system's account of the energy is meaningful",
        "Yes, but only when the reaction is carried out in a sealed container",
        "Yes, but only when no work is done"],
      ans=0,
      why="EK 6.1.A.3 states that for exothermic reactions the energy lost by the "
          "reacting species, the system, is gained by the surroundings. The two "
          "descriptions are the same transfer counted from opposite sides."),

 dict(q="Water in a beaker is warmed on a hotplate. Taking the water as the system, how "
        "should the heating be described?",
      choices=[
        "Endothermic, because the water gains energy from its surroundings",
        "Exothermic, because the water gains energy from its surroundings",
        "Endothermic, because the water loses energy to its surroundings",
        "Exothermic, because the water loses energy to its surroundings",
        "Neither, because only chemical changes can be described that way"],
      ans=0,
      why="EK 6.1.A.2 names the heating or cooling of a substance among the processes "
          "described as endothermic or exothermic, and the water here gains energy from "
          "the hotplate, which EK 6.1.A.1 reports as its rising temperature."),

 dict(q="A student wants to decide whether a reaction run in aqueous solution is "
        "exothermic, without computing anything. Which single observation settles it?",
      choices=[
        "Whether the temperature of the solution rises or falls",
        "Whether a precipitate appears in the solution",
        "Whether a gas is given off during the reaction",
        "Whether the color of the solution changes",
        "Whether the reaction finishes quickly or slowly"],
      ans=0,
      why="EK 6.1.A.1 makes a temperature change the indicator of an energy change, and "
          "EK 6.1.A.3 has the surroundings gain the energy an exothermic system loses, so "
          "the direction the solution's temperature moves reports the direction of the "
          "transfer."),
]
