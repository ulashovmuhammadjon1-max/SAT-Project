# AP CHEMISTRY 7.1 Introduction to Equilibrium
# CED effective Fall 2024, Unit 7 Equilibrium.
# Learning objective 7.1.A: explain the relationship between the occurrence of a
# reversible chemical or physical process, and the establishment of equilibrium, to
# experimental observations. Suggested skill 6.D, provide reasoning to justify a claim
# using chemical principles or laws, or using mathematical justification.
#
# Essential knowledge relied on, in the framework's own words:
#   7.1.A.1  Many observable processes are reversible. Examples include evaporation and
#            condensation of water, absorption and desorption of a gas, or dissolution
#            and precipitation of a salt. Some important reversible chemical processes
#            include the transfer of protons in acid-base reactions and the transfer of
#            electrons in redox reactions.
#   7.1.A.2  When equilibrium is reached, no observable changes occur in the system.
#            Reactants and products are simultaneously present, and the concentrations or
#            partial pressures of all species remain constant.
#   7.1.A.3  The equilibrium state is dynamic. The forward and reverse processes continue
#            to occur at equal rates, resulting in no net observable change.
#   7.1.A.4  Graphs of concentration, partial pressure, or rate of reaction versus time
#            for simple chemical reactions can be used to understand the establishment of
#            chemical equilibrium.
#
# THE FIGURE PROBLEM. EK 7.1.A.4 makes a GRAPH against time the characteristic
# representation of this topic and this bank cannot show one. Every one of them below is
# therefore given as a TABLE of readings against time, which is exactly what such a graph
# plots and leaves nothing to be read off a picture. No stem says "shown", "the graph" or
# "the figure"; verify_h7_1.py asserts that.
#
# SCOPE, so this topic does not reach into its neighbours. 7.2 owns the argument from the
# RELATIVE sizes of the forward and reverse rates to the direction of net conversion --
# nothing below asks which way a system with unequal rates is moving. 7.3 owns the form of
# the reaction quotient, 7.4 owns computing K from equilibrium concentrations, and 7.5 owns
# what the size of K says. No item here writes or evaluates K at all, and verify_h7_1.py
# asserts that too.
#
# THE MISCONCEPTION THIS TOPIC EXISTS TO KILL. EK 7.1.A.2 says the concentrations remain
# CONSTANT, not that they become EQUAL, and EK 7.1.A.3 says the two processes continue
# rather than stop. Every tabulated equilibrium below is deliberately reached at unequal
# concentrations, and the verifier asserts that, so a student who reads "equal" off this
# module would be contradicted by its own data.
#
# ARITHMETIC. Every time at which equilibrium is first established, and every change in a
# tabulated amount, is recomputed in verify_h7_1.py from the table alone.
#
# NOTATION. export_units.py does not typeset Chemistry, so any \( ... \) span below is
# hand-written. A formula in prose stays plain text (N2O4, CaCO3) and a reaction arrow is
# written as the word "to" so no glyph is left outside a span.
TOPIC = ("7.1", "Introduction to Equilibrium", 7)

_T_TIMECOURSE = dict(
    headers=["Time (min)", "[A] (M)", "[B] (M)"],
    rows=[["0", "1.00", "0"],
          ["2", "0.75", "0.25"],
          ["4", "0.65", "0.35"],
          ["6", "0.60", "0.40"],
          ["8", "0.60", "0.40"],
          ["10", "0.60", "0.40"]])

_T_RATES = dict(
    headers=["Time (s)", "Rate of the forward reaction (M per s)",
             "Rate of the reverse reaction (M per s)"],
    rows=[["0", "0.080", "0"],
          ["10", "0.050", "0.020"],
          ["20", "0.035", "0.035"],
          ["30", "0.035", "0.035"]])

_T_PRESSURES = dict(
    headers=["Time (min)", "Partial pressure of X (atm)", "Partial pressure of Y (atm)"],
    rows=[["0", "2.00", "0"],
          ["5", "1.40", "1.20"],
          ["10", "1.20", "1.60"],
          ["15", "1.20", "1.60"],
          ["20", "1.20", "1.60"]])

_T_VESSELS = dict(
    headers=["Vessel", "[R] at 20 min (M)", "[R] at 30 min (M)", "[R] at 40 min (M)"],
    rows=[["1", "0.40", "0.30", "0.22"],
          ["2", "0.50", "0.50", "0.50"],
          ["3", "0.60", "0.45", "0.38"]])

QUESTIONS = [

 dict(q="A reversible reaction has been running in a sealed flask for a long time and the "
        "system has reached equilibrium. What does the framework say a person watching the "
        "flask would observe?",
      choices=[
        "No observable changes, because the concentrations of all species remain constant",
        "A steady disappearance of colour, because the reactants are still being consumed",
        "The reactant concentration falling to zero once enough time has passed",
        "The concentrations of reactant and product becoming equal to one another",
        "An observable change every time the forward process occurs"],
      ans=0,
      why="EK 7.1.A.2 states that when equilibrium is reached, no observable changes occur "
          "in the system, that reactants and products are simultaneously present, and that "
          "the concentrations or partial pressures of all species remain constant. Constant "
          "is not the same as equal, and a reactant that fell to zero would not be present "
          "alongside the product."),

 dict(q="Why does the framework describe the equilibrium state as dynamic rather than "
        "static?",
      choices=[
        "The forward and reverse processes continue to occur at equal rates, so there is "
        "no net observable change",
        "The forward and reverse processes both stop once equilibrium is reached",
        "The forward process continues while the reverse process stops",
        "The rates of the two processes keep rising and falling around a common average",
        "The temperature of the system continues to change once equilibrium is reached"],
      ans=0,
      why="EK 7.1.A.3 states that the equilibrium state is dynamic: the forward and reverse "
          "processes continue to occur at equal rates, resulting in no net observable "
          "change. Processes that had stopped would make the state static, which is exactly "
          "the reading the framework's word 'dynamic' rules out."),

 dict(q="Which pair of PHYSICAL processes does the framework offer as an example of a "
        "reversible process?",
      choices=[
        "Evaporation and condensation of water",
        "Combustion and formation of methane",
        "Ionization and neutralization of a strong acid",
        "Melting of a metal and its subsequent oxidation",
        "Diffusion of a gas and its effusion through a pinhole"],
      ans=0,
      why="EK 7.1.A.1 names evaporation and condensation of water, absorption and "
          "desorption of a gas, and dissolution and precipitation of a salt as examples of "
          "reversible processes. Combustion is not among them, and effusion is not the "
          "reverse of diffusion."),

 dict(q="Which CHEMICAL process does the framework single out as an important reversible "
        "process?",
      choices=[
        "The transfer of protons in acid-base reactions",
        "The transfer of energy in a calorimeter",
        "The transfer of a solute across a semipermeable membrane",
        "The transfer of a gas from a cylinder into a balloon",
        "The transfer of heat from a hot body to a cold one"],
      ans=0,
      why="EK 7.1.A.1 says that some important reversible chemical processes include the "
          "transfer of protons in acid-base reactions and the transfer of electrons in "
          "redox reactions. The other transfers listed are physical, and the framework "
          "raises none of them here."),

 dict(q="The table reports concentrations measured at intervals in a sealed vessel. At "
        "which time has the system FIRST reached equilibrium?",
      table=_T_TIMECOURSE,
      choices=["6 minutes", "2 minutes", "4 minutes", "10 minutes", "0 minutes"],
      ans=0,
      why="EK 7.1.A.2 makes constancy of the concentrations the signature of equilibrium, "
          "so the first reading after which nothing changes again is the answer. The "
          "readings are still falling up to that time, and the last reading is merely the "
          "last one taken rather than the first constant one."),

 dict(q="Using the same table of concentrations, what is true of the two concentrations "
        "once the system has settled?",
      table=_T_TIMECOURSE,
      choices=[
        "Both are constant, and they are not equal to each other",
        "Both are constant, and they have become equal to each other",
        "Both are still falling, but too slowly to measure",
        "The reactant concentration is zero and only product remains",
        "They alternate between two values as the two processes take turns"],
      ans=0,
      why="EK 7.1.A.2 requires the concentrations to remain constant and both species to be "
          "present, and the tabulated readings settle at two different constant values. "
          "Nothing in the framework says the concentrations become equal, and reading "
          "'constant' as 'equal' is the standard error this data set is chosen to defeat."),

 dict(q="Using the same table of concentrations, is the substance A completely consumed by "
        "the end of the experiment?",
      table=_T_TIMECOURSE,
      choices=[
        "No, because reactants and products are simultaneously present at equilibrium",
        "Yes, because a reaction runs until its limiting reactant is gone",
        "Yes, because the product concentration stops rising only when A is exhausted",
        "No, because A is a catalyst and is regenerated",
        "It cannot be decided without knowing the volume of the vessel"],
      ans=0,
      why="EK 7.1.A.2 states that reactants and products are simultaneously present at "
          "equilibrium, and the tabulated concentration of A settles at a value above zero "
          "rather than falling to it. A reaction that ran to exhaustion would not be a "
          "reversible one reaching equilibrium."),

 dict(q="The table reports the rates of the forward and reverse reactions in a vessel at "
        "intervals after mixing. What is true of the two rates once equilibrium is "
        "established?",
      table=_T_RATES,
      choices=[
        "They are equal to each other and both are greater than zero",
        "They are equal to each other and both have fallen to zero",
        "The forward rate stays above the reverse rate by a constant amount",
        "The reverse rate rises above the forward rate and stays there",
        "They are equal only at the instant equilibrium is reached and differ afterwards"],
      ans=0,
      why="EK 7.1.A.3 states that the forward and reverse processes continue to occur at "
          "equal rates. The tabulated rates converge on a common nonzero value and stay "
          "there, which is the dynamic state the framework insists on; rates of zero would "
          "describe a system in which nothing is happening at all."),

 dict(q="Using the same table of reaction rates, at which time is equilibrium first "
        "established?",
      table=_T_RATES,
      choices=["20 seconds", "10 seconds", "30 seconds", "0 seconds",
               "Equilibrium is never established in this vessel"],
      ans=0,
      why="EK 7.1.A.3 makes equality of the forward and reverse rates the condition for "
          "equilibrium, so the earliest tabulated time at which the two rates agree is the "
          "answer. At the earlier readings the forward rate still exceeds the reverse one, "
          "and the later reading merely repeats the equality already reached."),

 dict(q="A student says that at equilibrium the forward and reverse reactions have both "
        "stopped, which is why nothing appears to change. What is wrong with this "
        "explanation?",
      choices=[
        "The two processes continue, and it is their equal rates that produce no net change",
        "Nothing is wrong with it, since a system at equilibrium is unchanging",
        "The forward reaction continues but the reverse one genuinely stops",
        "Both reactions continue but at rates that keep changing",
        "The reactions stop only because the reactants have been used up"],
      ans=0,
      why="EK 7.1.A.3 says the equilibrium state is dynamic and that the forward and "
          "reverse processes CONTINUE to occur at equal rates, resulting in no net "
          "observable change. The absence of change is a balance between two ongoing "
          "processes, not the absence of both."),

 dict(q="The table reports partial pressures measured in a rigid vessel in which X(g) "
        "converts reversibly to Y(g). At which time has the system first reached "
        "equilibrium?",
      table=_T_PRESSURES,
      choices=["10 minutes", "5 minutes", "15 minutes", "20 minutes", "0 minutes"],
      ans=0,
      why="EK 7.1.A.2 says that at equilibrium the concentrations OR PARTIAL PRESSURES of "
          "all species remain constant, so the first reading after which the tabulated "
          "pressures stop changing marks it. The earlier readings are still moving and the "
          "later ones only repeat the constant values."),

 dict(q="Using the same table of partial pressures, how much did the partial pressure of X "
        "fall, and how much did that of Y rise, between the start and equilibrium?",
      table=_T_PRESSURES,
      choices=[
        "X fell by 0.80 atm while Y rose by 1.60 atm",
        "X fell by 1.60 atm while Y rose by 0.80 atm",
        "X fell by 0.80 atm and Y rose by the same 0.80 atm",
        "X fell by 2.00 atm while Y rose by 1.60 atm",
        "Neither pressure changed, since the vessel is rigid"],
      ans=0,
      why="EK 7.1.A.4 licenses using readings of partial pressure against time to "
          "understand the establishment of equilibrium, and subtracting the equilibrium "
          "reading from the initial one for each gas gives the two changes directly. The "
          "changes are unequal because two molecules of Y form for each molecule of X "
          "consumed."),

 dict(q="A sealed jar holds a saturated solution of a salt sitting on a bed of undissolved "
        "crystals, and the mass of the crystals has not changed for several days. What is "
        "happening at the particulate level?",
      choices=[
        "Dissolution and precipitation continue at equal rates",
        "Dissolution and precipitation have both stopped",
        "Only precipitation continues, which is why no crystal dissolves",
        "Only dissolution continues, and the crystals are slowly being replaced",
        "The solution has become unsaturated and can dissolve no more solid"],
      ans=0,
      why="EK 7.1.A.1 names dissolution and precipitation of a salt as a reversible "
          "process, and EK 7.1.A.3 makes the equilibrium state dynamic, with both processes "
          "continuing at equal rates and producing no net observable change. A constant "
          "mass is the absence of NET change, not the absence of change."),

 dict(q="Which of the following is the reverse process of the absorption of a gas onto a "
        "surface, in the framework's own list of reversible processes?",
      choices=["Desorption of the gas from the surface",
               "Condensation of the gas to a liquid",
               "Effusion of the gas through a small opening",
               "Combustion of the gas at the surface",
               "Compression of the gas into a smaller volume"],
      ans=0,
      why="EK 7.1.A.1 lists absorption and desorption of a gas as one of its examples of a "
          "reversible process, pairing each named process with its own reverse. "
          "Condensation is paired there with evaporation instead, and the remaining options "
          "are not reverses of adsorption at all."),

 dict(q="A student claims that a reaction has reached equilibrium because the "
        "concentration of the reactant has become equal to the concentration of the "
        "product. How should this claim be evaluated?",
      choices=[
        "It is not sound, because equilibrium requires constant concentrations rather than "
        "equal ones",
        "It is sound, because equal concentrations are the definition of equilibrium",
        "It is sound only if the reaction has a one-to-one stoichiometry",
        "It is not sound, because at equilibrium the product concentration must exceed the "
        "reactant concentration",
        "It cannot be evaluated without the temperature of the system"],
      ans=0,
      why="EK 7.1.A.2 states that the concentrations or partial pressures of all species "
          "REMAIN CONSTANT at equilibrium; it says nothing about their being equal. Two "
          "concentrations can cross and keep changing, so equality at one instant is no "
          "evidence of equilibrium at all."),

 dict(q="Readings of which quantities against time does the framework say can be used to "
        "understand the establishment of chemical equilibrium?",
      choices=[
        "Concentration, partial pressure, or rate of reaction",
        "Temperature, pressure, or volume",
        "Mass, density, or molar mass",
        "Activation energy, enthalpy, or entropy",
        "Only the concentration of the limiting reactant"],
      ans=0,
      why="EK 7.1.A.4 names graphs of concentration, partial pressure, or rate of reaction "
          "versus time for simple chemical reactions as useful for understanding the "
          "establishment of chemical equilibrium. The other quantities listed are not the "
          "ones the framework raises here."),

 dict(q="The table reports the concentration of a reactant R in three vessels at three "
        "times. Which vessel has reached equilibrium by the last reading?",
      table=_T_VESSELS,
      choices=["Vessel 2", "Vessel 1", "Vessel 3", "Vessels 1 and 3", "All three vessels"],
      ans=0,
      why="EK 7.1.A.2 makes constancy of concentration the observable signature of "
          "equilibrium. Only one vessel's three tabulated readings are all the same; in the "
          "other two the concentration is still falling from one reading to the next, so "
          "those systems are still changing."),

 dict(q="Using the same table of three vessels, what does a concentration that is still "
        "falling from one reading to the next indicate?",
      table=_T_VESSELS,
      choices=[
        "The system has not yet reached equilibrium",
        "The system reached equilibrium and has now been disturbed",
        "The system is at equilibrium but the measurements are imprecise",
        "The reverse reaction is faster than the forward reaction",
        "The reactant is being consumed by a side reaction"],
      ans=0,
      why="EK 7.1.A.2 states that at equilibrium the concentrations of all species remain "
          "constant, so a concentration that is still changing shows the system has not yet "
          "got there. Attributing the change to imprecision would explain scatter, not the "
          "steady one-way fall the readings show."),

 dict(q="A flask holds liquid water and water vapour in equilibrium at a fixed "
        "temperature. Which statement best describes the system?",
      choices=[
        "Molecules continue to evaporate and to condense, at equal rates",
        "Evaporation has finished, and only condensation now occurs",
        "The vapour pressure keeps rising because evaporation continues",
        "No molecule crosses the liquid surface once equilibrium is reached",
        "The liquid and the vapour are present in equal amounts"],
      ans=0,
      why="EK 7.1.A.1 gives evaporation and condensation of water as its example of a "
          "reversible process and EK 7.1.A.3 makes the equilibrium state dynamic, with both "
          "continuing at equal rates. Equal RATES is what the framework asserts, not equal "
          "amounts of the two phases."),

 dict(q="Which observation would be the strongest evidence that a reversible reaction in a "
        "sealed vessel has reached equilibrium?",
      choices=[
        "Repeated measurements of every species give the same concentrations over time",
        "The reactant concentration has fallen to half of its initial value",
        "The colour of the mixture has changed since mixing",
        "The forward reaction has been running for more than an hour",
        "A single measurement shows both reactant and product present"],
      ans=0,
      why="EK 7.1.A.2 makes the constancy of the concentrations of ALL species over time "
          "the observable signature of equilibrium. A single reading showing both species, "
          "or any amount of elapsed time, is consistent with a system still on its way "
          "there."),

 dict(q="Why can the forward and reverse rates be equal at equilibrium even though the "
        "concentrations of reactant and product are different?",
      choices=[
        "A rate depends on both the concentration and how readily that species reacts, so "
        "different concentrations can still give equal rates",
        "The rates are equal only when the concentrations are also equal",
        "The reverse reaction has no dependence on concentration at all",
        "The concentrations must in fact be equal, and any difference is measurement error",
        "The two rates are equal by definition and have nothing to do with concentration"],
      ans=0,
      why="EK 7.1.A.2 and EK 7.1.A.3 are asserted together: the concentrations remain "
          "constant at whatever values they have reached, AND the two rates are equal "
          "there. Both can hold at once because a rate is not fixed by concentration alone, "
          "which is why the framework never claims the concentrations must match."),

 dict(q="Using the table of concentrations measured at intervals, what happens to the sum "
        "of the two tabulated concentrations as the reaction proceeds?",
      table=_T_TIMECOURSE,
      choices=[
        "It stays the same at every reading, because each unit of A that reacts produces "
        "one unit of B",
        "It falls steadily, because reactant is consumed faster than product forms",
        "It rises steadily, because product accumulates while reactant remains",
        "It stays the same only after equilibrium has been reached",
        "It cannot be found from the table without the volume of the vessel"],
      ans=0,
      why="Adding the two tabulated values at each time gives the same total throughout, "
          "which is what a one-to-one conversion requires. EK 7.1.A.4 licenses exactly this "
          "kind of reading of concentration against time, and the constancy of the total "
          "holds from the first reading, not only after equilibrium."),

 dict(q="A reversible redox reaction is running in a beaker. Which transfer is the "
        "framework describing when it calls such a process reversible?",
      choices=["The transfer of electrons",
               "The transfer of protons",
               "The transfer of whole atoms between phases",
               "The transfer of thermal energy to the surroundings",
               "The transfer of a precipitate out of solution"],
      ans=0,
      why="EK 7.1.A.1 names the transfer of electrons in redox reactions, alongside the "
          "transfer of protons in acid-base reactions, as an important reversible chemical "
          "process. Proton transfer is the acid-base case the framework lists separately."),

 dict(q="Two students disagree about a sealed vessel whose measured concentrations have "
        "not changed in an hour. One says the reaction is over; the other says it is at "
        "equilibrium. Which reading does the framework support, and why?",
      choices=[
        "At equilibrium, because both reactant and product are present and both processes "
        "continue",
        "The reaction is over, because a completed reaction is what produces unchanging "
        "concentrations",
        "The reaction is over, because the forward rate must have fallen to zero",
        "At equilibrium, because the two concentrations have become equal",
        "Neither, because an hour is not long enough to decide"],
      ans=0,
      why="EK 7.1.A.2 has reactants and products simultaneously present with constant "
          "concentrations, and EK 7.1.A.3 has the two processes continuing at equal rates. "
          "A reaction that was over would have consumed a reactant entirely and would have "
          "no reverse process running."),

 dict(q="Using the table of reaction rates, what is happening to the forward rate and the "
        "reverse rate during the first ten seconds after mixing?",
      table=_T_RATES,
      choices=[
        "The forward rate is falling while the reverse rate is rising",
        "Both rates are rising toward their equilibrium values",
        "Both rates are falling toward their equilibrium values",
        "The forward rate is rising while the reverse rate is falling",
        "Both rates are constant, since the vessel is sealed"],
      ans=0,
      why="Comparing the tabulated readings at the two earliest times gives the direction "
          "of each rate directly. EK 7.1.A.4 licenses reading rate against time in exactly "
          "this way, and EK 7.1.A.3 says where the two are heading: a common value at which "
          "they become equal."),

 dict(q="A sample of solid CaCO3 is sealed in a rigid container and heated until some of "
        "it decomposes to CaO(s) and CO2(g), after which the pressure of CO2 stops "
        "changing. What has the system reached?",
      choices=[
        "Equilibrium, because the partial pressure of a species is no longer changing",
        "Completion, because the pressure can rise no further",
        "Equilibrium, because all of the CaCO3 has decomposed",
        "Neither, because a solid cannot take part in a reversible process",
        "Completion, because the container is rigid and cannot expand"],
      ans=0,
      why="EK 7.1.A.2 says that at equilibrium the concentrations or partial pressures of "
          "all species remain constant, so a partial pressure that has stopped changing is "
          "the observable signature. Solid remains present, which is what distinguishes "
          "this from a reaction that has run out of reactant."),

 dict(q="What does the framework mean by saying that a reversible process produces no NET "
        "observable change at equilibrium?",
      choices=[
        "Change continues in both directions, but the two changes cancel",
        "No change of any kind occurs anywhere in the system",
        "Change occurs, but it is too small to be observed with ordinary instruments",
        "The system changes only when it is disturbed from outside",
        "Observable change occurs, but it repeats on a fixed cycle"],
      ans=0,
      why="EK 7.1.A.3 pairs the phrase with the statement that the forward and reverse "
          "processes CONTINUE at equal rates. The word 'net' is doing the work: two ongoing "
          "changes of equal size in opposite directions leave the observable properties "
          "fixed, which is not the same as nothing happening."),

 dict(q="Which experimental design would allow a student to decide whether a reversible "
        "reaction in solution had reached equilibrium?",
      choices=[
        "Measure the concentration of a species at several times and see whether the value "
        "stops changing",
        "Measure the concentration of a species once and compare it with the initial value",
        "Measure the temperature of the solution at several times",
        "Measure how long the reaction has been running and compare it with a known "
        "reaction",
        "Measure the mass of the whole sealed flask at several times"],
      ans=0,
      why="EK 7.1.A.2 makes constancy of concentration over time the observable signature "
          "of equilibrium and EK 7.1.A.4 names concentration against time as the reading to "
          "take. The mass of a sealed flask is constant whether or not the reaction has "
          "finished, so it distinguishes nothing."),

 dict(q="A reversible reaction is started with reactants only. Which description of the "
        "reverse reaction is correct for the moments just after mixing?",
      choices=[
        "Its rate starts at zero and rises as product accumulates",
        "Its rate starts at its maximum and falls as product accumulates",
        "Its rate is equal to the forward rate from the very first instant",
        "It does not begin at all until the forward reaction has finished",
        "Its rate is constant from the start, since it depends only on temperature"],
      ans=0,
      why="EK 7.1.A.3 has both processes running at equal rates only once equilibrium is "
          "established, and with no product present at the start there is nothing for the "
          "reverse process to consume. EK 7.1.A.4's rate readings against time show the "
          "reverse rate climbing from zero to meet the falling forward rate."),

 dict(q="Which statement about a system at equilibrium is supported by the framework?",
      choices=[
        "Both reactants and products are present, and their amounts are unchanging",
        "Only the products are present, since the forward reaction has won",
        "The amounts of reactant and product are unchanging and equal",
        "The reactants and products are present in the ratio of their coefficients",
        "The system contains whichever species has the faster reaction"],
      ans=0,
      why="EK 7.1.A.2 states in one sentence that reactants and products are simultaneously "
          "present and that the concentrations or partial pressures of all species remain "
          "constant. It makes no claim that the amounts are equal or that they follow the "
          "coefficients of the balanced equation."),

]
