# AP CHEMISTRY 6.4 Heat Capacity and Calorimetry
# CED effective Fall 2024, Unit 6 Thermochemistry.
# Learning objective 6.4.A: calculate the heat q absorbed or released by a system
# undergoing heating or cooling based on the amount of the substance, the heat capacity,
# and the change in temperature. Suggested skill 2.D, make observations or collect data
# from representations of laboratory setups or results, while attending to precision where
# appropriate.
#
# Essential knowledge relied on, in the framework's own words:
#   6.4.A.1  The heating of a cool body by a warmer body is an important form of energy
#            transfer between two systems. The amount of heat transferred between two
#            bodies may be quantified by the heat transfer equation: EQN: q = mc(delta T).
#            Calorimetry experiments are used to measure the transfer of heat.
#   6.4.A.2  The first law of thermodynamics states that energy is conserved in chemical
#            and physical processes.
#   6.4.A.3  The transfer of a given amount of thermal energy will not produce the same
#            temperature change in equal masses of matter with differing specific heat
#            capacities.
#   6.4.A.4  Heating a system increases the energy of the system, while cooling a system
#            decreases the energy of the system.
#   6.4.A.5  The specific heat capacity of a substance and the molar heat capacity are
#            both used in energy calculations.
#   6.4.A.6  Chemical systems change their energy through three main processes:
#            heating/cooling, phase transitions, and chemical reactions.
#   6.4.A.7  In calorimetry experiments involving dissolution, temperature changes of the
#            mixture within the calorimeter can be used to determine the direction of
#            energy flow. If the temperature of the mixture increases, thermal energy is
#            released by the dissolution process (exothermic). If the temperature of the
#            mixture decreases, thermal energy is absorbed by the dissolution process
#            (endothermic).
#
# THIS IS THE ARITHMETIC TOPIC OF THE UNIT, and every number below is recomputed in
# verify_h6_4.py from the stimulus alone -- not checked against a stored answer, and never
# by magnitude on its own.
#
# THE SIGN IS WHERE THIS TOPIC LIES TO A STUDENT. q = mc(delta T) carries the sign of the
# temperature change, so cooling gives a negative q, and EK 6.4.A.4 says what that means:
# the system has lost energy. Every keyed choice that reports a quantity of energy for a
# process with a direction says WHICH DIRECTION as well as how much -- "8360 J released",
# never a bare "8360 J" -- and every anchor carries the direction word with the number, so
# a key with the arithmetic right and the sign backwards cannot pass.
#
# THE CONSERVATION STEP IS WRITTEN OUT, NEVER HIDDEN. In a calorimetry experiment the
# energy the mixture gains is the energy the process lost, which is EK 6.4.A.2's first law
# and a change of sign. h6_thermo.heat() returns the heat for the substance whose mass and
# temperature change were measured, and each verifier check negates it explicitly where
# the item asks about the process instead. That negation is the single step most often
# dropped, so it is never done silently.
#
# EVERY DISTRACTOR ON A CALCULATION IS A RECOGNISABLE MISTAKE, not filler: the final
# temperature used in place of the change, the initial temperature used in place of the
# change, the mass left out, the capacity left out, the sign reversed, a reciprocal taken.
# verify_h6_4.py recomputes the ORIGIN of each arithmetic distractor as well as the key,
# so a distractor cannot drift into being accidentally correct and the item cannot
# quietly stop testing what it was written to test.
#
# SCOPE. 6.5 owns the energy of a phase change and its molar enthalpy, and 6.6 owns the
# molar enthalpy of reaction, so no item here multiplies moles by a molar enthalpy or names
# one; EK 6.4.A.6 is used only as the framework uses it, to name the three kinds of
# process. 6.9 owns Hess's law. 6.3 owns the particle-level account of the transfer.
#
# NOTATION. export_units.py does not typeset Chemistry, so \( q = mc\Delta T \) is
# hand-written wherever the equation appears, with a space either side of the span. Units
# are written out in words -- "4.18 J per gram per degree Celsius" -- because a raw degree
# glyph and a slash fraction both reach a student raw.
TOPIC = ("6.4", "Heat Capacity and Calorimetry", 6)

_T_CALOR = dict(
    headers=["Trial", "Mass of solution (g)", "Temperature before (degrees Celsius)",
             "Temperature after (degrees Celsius)"],
    rows=[["Trial 1", "100.0", "22.0", "28.0"],
          ["Trial 2", "100.0", "22.0", "17.0"],
          ["Trial 3", "200.0", "20.0", "23.0"],
          ["Trial 4", "50.0", "25.0", "25.0"],
          ["Trial 5", "100.0", "22.0", "31.0"]])

_T_C = dict(
    headers=["Substance", "Specific heat capacity (J per gram per degree Celsius)"],
    rows=[["Water", "4.18"],
          ["Aluminum", "0.900"],
          ["Iron", "0.449"],
          ["Copper", "0.385"],
          ["Lead", "0.128"]])

QUESTIONS = [

 dict(q="Which equation does the framework give for the amount of heat transferred "
        "between two bodies?",
      choices=[
        "\\( q = mc\\Delta T \\) , the mass times the specific heat capacity times the "
        "temperature change",
        "\\( q = m\\Delta T \\) , the mass times the temperature change",
        "\\( q = c\\Delta T \\) , the specific heat capacity times the temperature change",
        "\\( q = mc \\) , the mass times the specific heat capacity",
        "\\( q = m/c \\) , the mass divided by the specific heat capacity"],
      ans=0,
      why="EK 6.4.A.1 gives the heat transfer equation as q equals m times c times the "
          "change in temperature, so all three quantities appear and the temperature "
          "enters as a CHANGE rather than as a value."),

 dict(q="What does the framework say calorimetry experiments are used to do?",
      choices=[
        "Measure the transfer of heat",
        "Measure the mass of a reacting substance",
        "Separate a mixture into its components",
        "Determine the formula of a compound",
        "Measure how quickly a reaction reaches completion"],
      ans=0,
      why="EK 6.4.A.1 closes by stating that calorimetry experiments are used to measure "
          "the transfer of heat, which is what the heat transfer equation in the same "
          "statement quantifies."),

 dict(q="What does the first law of thermodynamics state, in the framework's words?",
      choices=[
        "Energy is conserved in chemical and physical processes",
        "Energy always moves from a system to its surroundings",
        "The energy of a system is always increasing",
        "Energy can be created when a chemical reaction occurs",
        "The energy of a system depends only on its temperature"],
      ans=0,
      why="EK 6.4.A.2 states that the first law of thermodynamics says energy is conserved "
          "in chemical and physical processes, which is what lets the energy a calorimeter "
          "mixture gains be counted as the energy the process lost."),

 dict(q="What does the framework say heating a system does to its energy, and what does "
        "cooling do?",
      choices=[
        "Heating increases the energy of the system and cooling decreases it",
        "Heating decreases the energy of the system and cooling increases it",
        "Both heating and cooling increase the energy of the system",
        "Both heating and cooling leave the energy of the system unchanged",
        "Neither changes the energy of the system unless a reaction occurs"],
      ans=0,
      why="EK 6.4.A.4 states that heating a system increases the energy of the system, "
          "while cooling a system decreases the energy of the system, which is what the "
          "sign of q in the heat transfer equation reports."),

 dict(q="Which two quantities does the framework say are both used in energy "
        "calculations?",
      choices=[
        "The specific heat capacity of a substance and the molar heat capacity",
        "The specific heat capacity and the density",
        "The molar heat capacity and the molar mass",
        "The specific heat capacity and the boiling point",
        "The molar heat capacity and the volume"],
      ans=0,
      why="EK 6.4.A.5 states that the specific heat capacity of a substance and the molar "
          "heat capacity are both used in energy calculations, one taken per gram and the "
          "other per mole."),

 dict(q="Through which three main processes does the framework say chemical systems change "
        "their energy?",
      choices=[
        "Heating or cooling, phase transitions, and chemical reactions",
        "Heating or cooling, dissolution, and filtration",
        "Phase transitions, chemical reactions, and changes in pressure",
        "Chemical reactions, changes in volume, and changes in mass",
        "Heating or cooling, changes in pressure, and changes in concentration"],
      ans=0,
      why="EK 6.4.A.6 names exactly these three: heating and cooling, phase transitions, "
          "and chemical reactions. The other processes listed are not among the three the "
          "framework gives."),

 dict(q="Equal masses of two substances with different specific heat capacities each "
        "receive the same amount of thermal energy. What does the framework say about "
        "their temperature changes?",
      choices=[
        "They will not be the same",
        "They will be the same, since the energy transferred was the same",
        "They will be the same, since the masses were the same",
        "The substance with the larger specific heat capacity will change more",
        "Neither will change temperature at all"],
      ans=0,
      why="EK 6.4.A.3 states that the transfer of a given amount of thermal energy will "
          "not produce the same temperature change in equal masses of matter with "
          "differing specific heat capacities, which the heat transfer equation makes "
          "arithmetic."),

 dict(q="A 50.0 g sample of water, whose specific heat capacity is 4.18 J per gram per "
        "degree Celsius, is warmed by 10.0 degrees Celsius. How much energy did the water "
        "absorb?",
      choices=[
        "2090 J absorbed",
        "2090 J released",
        "209 J absorbed",
        "41.8 J absorbed",
        "500 J absorbed"],
      ans=0,
      why="EK 6.4.A.1's equation multiplies the mass, the specific heat capacity and the "
          "temperature change, and EK 6.4.A.4 makes a warming system one whose energy has "
          "increased, so the sample took the energy in."),

 dict(q="A 100.0 g sample of water, whose specific heat capacity is 4.18 J per gram per "
        "degree Celsius, cools from 60.0 to 40.0 degrees Celsius. What is the energy "
        "change of the water?",
      choices=[
        "8360 J released",
        "8360 J absorbed",
        "16720 J released",
        "4180 J released",
        "418 J released"],
      ans=0,
      why="EK 6.4.A.1's equation takes the temperature change as the final value less the "
          "initial one, which is negative here, and EK 6.4.A.4 makes a cooling system one "
          "whose energy has decreased, so the water gave the energy up."),

 dict(q="4180 J of energy are transferred to a 100.0 g sample of water whose specific "
        "heat capacity is 4.18 J per gram per degree Celsius. By how much does its "
        "temperature change?",
      choices=[
        "It rises by 10.0 degrees Celsius",
        "It falls by 10.0 degrees Celsius",
        "It rises by 41.8 degrees Celsius",
        "It rises by 1000 degrees Celsius",
        "It rises by 20.0 degrees Celsius"],
      ans=0,
      why="Rearranging EK 6.4.A.1's equation divides the energy by the mass and the "
          "specific heat capacity, and EK 6.4.A.4 makes energy transferred INTO a system "
          "a warming rather than a cooling."),

 dict(q="A sample of water whose specific heat capacity is 4.18 J per gram per degree "
        "Celsius absorbs 8360 J and its temperature rises by 20.0 degrees Celsius. What "
        "is the mass of the sample?",
      choices=[
        "100.0 g",
        "50.0 g",
        "200.0 g",
        "418 g",
        "2000 g"],
      ans=0,
      why="Rearranging EK 6.4.A.1's equation divides the energy by the specific heat "
          "capacity and by the temperature change, which leaves the mass of the sample "
          "that was heated."),

 dict(q="A 50.0 g sample of a metal absorbs 500 J and its temperature rises by 25.0 "
        "degrees Celsius. What is the specific heat capacity of the metal?",
      choices=[
        "0.400 J per gram per degree Celsius",
        "0.0400 J per gram per degree Celsius",
        "2.50 J per gram per degree Celsius",
        "10.0 J per gram per degree Celsius",
        "20.0 J per gram per degree Celsius"],
      ans=0,
      why="Rearranging EK 6.4.A.1's equation divides the energy by the mass and by the "
          "temperature change, and EK 6.4.A.5 makes that per-gram quantity the specific "
          "heat capacity."),

 dict(q="The molar heat capacity of a substance is 75.3 J per mole per degree Celsius. "
        "How much energy is needed to warm 2.00 mol of it by 10.0 degrees Celsius?",
      choices=[
        "1506 J",
        "753 J",
        "376.5 J",
        "150.6 J",
        "15060 J"],
      ans=0,
      why="EK 6.4.A.5 puts the molar heat capacity to work in energy calculations in the "
          "same way as the specific heat capacity, with the amount taken in moles rather "
          "than in grams, so the amount, the capacity and the temperature change "
          "multiply."),

 dict(q="A hot metal block is dropped into water inside a calorimeter, and the water is "
        "found to have absorbed 2090 J. How much energy did the block lose, and why?",
      choices=[
        "2090 J lost, because energy is conserved in physical processes",
        "2090 J gained, because the block and the water both finish warmer than the water "
        "began",
        "1045 J lost, because the energy is shared equally between the block and the water",
        "4180 J lost, because the block must supply the water twice over",
        "It cannot be found without the mass of the block"],
      ans=0,
      why="EK 6.4.A.2 states the first law of thermodynamics, that energy is conserved in "
          "chemical and physical processes, so the energy the water gained is the energy "
          "the block gave up."),

 dict(q="During a calorimetry experiment on a dissolution, the temperature of the mixture "
        "increases. What does the framework say has happened?",
      choices=[
        "Thermal energy was released by the dissolution, which is therefore exothermic",
        "Thermal energy was absorbed by the dissolution, which is therefore endothermic",
        "Thermal energy was released by the dissolution, which is therefore endothermic",
        "Thermal energy was absorbed by the dissolution, which is therefore exothermic",
        "No energy was exchanged, since the calorimeter is insulated"],
      ans=0,
      why="EK 6.4.A.7 states that if the temperature of the mixture increases, thermal "
          "energy is released by the dissolution process, and names that case exothermic. "
          "Both halves of the key come from the one sentence."),

 dict(q="During a calorimetry experiment on a different dissolution, the temperature of "
        "the mixture decreases. What does the framework say has happened?",
      choices=[
        "Thermal energy was absorbed by the dissolution, which is therefore endothermic",
        "Thermal energy was released by the dissolution, which is therefore exothermic",
        "Thermal energy was absorbed by the dissolution, which is therefore exothermic",
        "Thermal energy was released by the dissolution, which is therefore endothermic",
        "The calorimeter must have leaked, since a dissolution cannot cool a mixture"],
      ans=0,
      why="EK 6.4.A.7 states that if the temperature of the mixture decreases, thermal "
          "energy is absorbed by the dissolution process, and names that case endothermic."),

 dict(q="Five dissolutions were carried out in a calorimeter and the mixture's mass and "
        "temperatures recorded. Taking the specific heat capacity of every mixture as 4.18 "
        "J per gram per degree Celsius, which trial's dissolution is endothermic?",
      table=_T_CALOR,
      choices=[
        "Trial 2",
        "Trial 1",
        "Trial 3",
        "Trial 4",
        "Trial 5"],
      ans=0,
      why="EK 6.4.A.7 makes a fall in the temperature of the mixture the sign that thermal "
          "energy was absorbed by the dissolution, which is the endothermic case, so the "
          "one trial whose mixture cooled is the answer."),

 dict(q="Among those same five trials, in which did the dissolution release the most "
        "energy to the mixture?",
      table=_T_CALOR,
      choices=[
        "Trial 5",
        "Trial 1",
        "Trial 3",
        "Trial 2",
        "Trial 4"],
      ans=0,
      why="EK 6.4.A.1's equation gives the energy the mixture took up from its mass, its "
          "specific heat capacity and its temperature change, and EK 6.4.A.7 makes a "
          "warming mixture one that received energy from the dissolution."),

 dict(q="Which two of those trials transferred the same quantity of energy to the "
        "mixture, despite differing in both mass and temperature change?",
      table=_T_CALOR,
      choices=[
        "Trial 1 and Trial 3",
        "Trial 1 and Trial 5",
        "Trial 3 and Trial 5",
        "Trial 2 and Trial 4",
        "Trial 2 and Trial 3"],
      ans=0,
      why="EK 6.4.A.1's equation multiplies the mass by the specific heat capacity and by "
          "the temperature change, so a smaller change in a larger mass can deliver the "
          "same quantity of energy as a larger change in a smaller one."),

 dict(q="How much energy did the mixture in Trial 1 absorb?",
      table=_T_CALOR,
      choices=[
        "2508 J",
        "11704 J",
        "9196 J",
        "25.08 J",
        "418 J"],
      ans=0,
      why="EK 6.4.A.1's equation takes the mass of the mixture, its specific heat "
          "capacity, and the CHANGE in temperature rather than either recorded "
          "temperature on its own."),

 dict(q="A 10.0 g sample of each of five substances absorbs 100 J. In which does the "
        "temperature rise by the most?",
      table=_T_C,
      choices=[
        "Lead",
        "Copper",
        "Iron",
        "Aluminum",
        "Water"],
      ans=0,
      why="EK 6.4.A.3 states that a given amount of thermal energy will not produce the "
          "same temperature change in equal masses of substances with differing specific "
          "heat capacities, and rearranging EK 6.4.A.1's equation divides by the capacity, "
          "so the smallest capacity gives the largest rise."),

 dict(q="Among those same five substances, each 10.0 g and each absorbing 100 J, in which "
        "does the temperature rise by the least?",
      table=_T_C,
      choices=[
        "Water",
        "Aluminum",
        "Iron",
        "Copper",
        "Lead"],
      ans=0,
      why="EK 6.4.A.1's equation divides the energy by the mass and by the specific heat "
          "capacity to give the temperature change, so the largest tabulated capacity "
          "gives the smallest rise."),

 dict(q="Which of those five substances needs the most energy to raise one gram of it by "
        "one degree Celsius?",
      table=_T_C,
      choices=[
        "Water",
        "Aluminum",
        "Iron",
        "Copper",
        "Lead"],
      ans=0,
      why="EK 6.4.A.5 makes the specific heat capacity the energy per gram per degree, so "
          "the substance with the largest tabulated value is the one that takes the most "
          "for the same gram and the same degree."),

 dict(q="A 10.0 g sample of each substance absorbs 100 J. Which two of them show the most "
        "nearly equal temperature rises?",
      table=_T_C,
      choices=[
        "Iron and copper",
        "Water and aluminum",
        "Aluminum and iron",
        "Copper and lead",
        "Water and lead"],
      ans=0,
      why="EK 6.4.A.3 makes the temperature changes differ because the capacities differ, "
          "and dividing the same energy by each tabulated capacity gives five rises whose "
          "closest pair can be found by comparing them."),

 dict(q="A metal railing and a swimming pool stand in the same sunlight. Why does the "
        "railing become hot to the touch long before the water does?",
      choices=[
        "Water has a much larger specific heat capacity, so the same energy per gram "
        "produces a much smaller temperature change",
        "Water has a much smaller specific heat capacity, so the same energy per gram "
        "produces a much smaller temperature change",
        "The railing absorbs energy and the water reflects all of it",
        "Water cannot absorb energy from sunlight at all",
        "The railing has a larger specific heat capacity than the water"],
      ans=0,
      why="EK 6.4.A.3 states that the same thermal energy will not produce the same "
          "temperature change in equal masses of substances with differing specific heat "
          "capacities, and EK 6.4.A.1's equation divides by the capacity, so the larger "
          "capacity gives the smaller change."),

 dict(q="Which three quantities must be known to calculate the heat absorbed or released "
        "by a substance being heated or cooled?",
      choices=[
        "The mass, the specific heat capacity, and the change in temperature",
        "The mass, the specific heat capacity, and the final temperature",
        "The volume, the density, and the change in temperature",
        "The mass, the molar mass, and the final temperature",
        "The specific heat capacity, the change in temperature, and the pressure"],
      ans=0,
      why="EK 6.4.A.1's equation is q equals m times c times the change in temperature, "
          "and it is the CHANGE that enters rather than either temperature alone, which "
          "is what the learning objective's phrase change in temperature names."),

 dict(q="A student applies the heat transfer equation to a sample of water that has cooled "
        "and obtains a negative value for q. What does the sign mean?",
      choices=[
        "The water lost energy, since cooling a system decreases its energy",
        "The water gained energy, since cooling a system increases its energy",
        "The student has made an arithmetic error, since q is never negative",
        "The mass must have been entered as a negative number",
        "The specific heat capacity of water must be negative"],
      ans=0,
      why="EK 6.4.A.1's equation carries the sign of the temperature change, which is "
          "negative for cooling, and EK 6.4.A.4 states that cooling a system decreases the "
          "energy of the system."),

 dict(q="In a calorimetry experiment on a dissolution, what is measured directly and what "
        "is deduced from it?",
      choices=[
        "The temperature change of the mixture is measured, and the direction of energy "
        "flow is deduced from it",
        "The direction of energy flow is measured, and the temperature change is deduced "
        "from it",
        "The mass of the salt is measured, and the temperature change is deduced from it",
        "The energy of the salt is measured directly by the calorimeter",
        "Nothing is measured, since the direction of energy flow is known in advance"],
      ans=0,
      why="EK 6.4.A.7 states that temperature changes of the mixture within the "
          "calorimeter can be used to determine the direction of energy flow, so the "
          "thermometer supplies the measurement and the direction is the conclusion drawn "
          "from it."),

 dict(q="A reaction carried out inside a calorimeter releases 5.0 kJ. Where does that "
        "energy go?",
      choices=[
        "It is gained by the mixture and the calorimeter, because energy is conserved",
        "It is destroyed, because a calorimeter is a closed container",
        "It is stored in the products of the reaction",
        "It leaves the calorimeter as light rather than as heat",
        "It cannot be accounted for without knowing the mass of the products"],
      ans=0,
      why="EK 6.4.A.2 states that energy is conserved in chemical and physical processes, "
          "and EK 6.4.A.1 makes the calorimeter the apparatus in which the transfer of "
          "that heat is measured, so what the reaction releases the surroundings inside "
          "the calorimeter take up."),

 dict(q="A student has the molar heat capacity of a substance but knows the amount of "
        "sample only as a mass in grams. What must be done before the energy calculation?",
      choices=[
        "Convert the mass to an amount in moles, since a molar heat capacity is taken per "
        "mole",
        "Convert the molar heat capacity to a temperature, since the two are equivalent",
        "Nothing, since a molar heat capacity may be multiplied by a mass in grams",
        "Convert the mass to a volume, since heat capacities are taken per unit volume",
        "Nothing, since the mass cancels out of the calculation"],
      ans=0,
      why="EK 6.4.A.5 states that the specific heat capacity and the molar heat capacity "
          "are both used in energy calculations, one per gram and the other per mole, so "
          "the amount supplied has to match the capacity being used."),
]
