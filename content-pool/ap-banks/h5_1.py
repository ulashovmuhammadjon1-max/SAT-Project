# AP CHEMISTRY 5.1 Reaction Rates
# CED effective Fall 2024, Unit 5 Kinetics.
# Learning objective 5.1.A: explain the relationship between the rate of a
# chemical reaction and experimental parameters. Suggested skill 6.E, provide
# reasoning to justify a claim using connections between particulate and
# macroscopic scales or levels.
#
# Essential knowledge relied on, in the framework's own words:
#   5.1.A.1  The kinetics of a chemical reaction is defined as the rate at which
#            an amount of reactants is converted to products per unit of time.
#   5.1.A.2  The rates of change of reactant and product concentrations are
#            determined by the stoichiometry in the balanced chemical equation.
#   5.1.A.3  The rate of a reaction is influenced by reactant concentrations,
#            temperature, surface area, catalysts, and other environmental
#            factors.
#
# WHERE THIS TOPIC STOPS, DELIBERATELY. 5.1.A.3 NAMES the factors; it does not
# explain them. The explanation is 5.5's (collisions, energy and orientation),
# 5.6's (the temperature dependence of an elementary rate) and 5.11's
# (catalysis). So no item here keys on "because raising the temperature raises
# the fraction of collisions with sufficient energy" -- that is a 5.5 key. Items
# here key on which parameters influence a rate, and on the stoichiometric
# relationship among the several rates of one reaction, which is 5.1.A.2 and
# belongs to no other topic.
#
# THE RATE LAW IS NOT HERE EITHER. Orders, the rate constant and the initial
# rates method are 5.2. An item in this module may state that doubling a
# concentration changed a measured rate, but no key asserts a power.
#
# NOTATION. Chemistry is not typeset by export_units.py, so the few genuine
# fractions carry hand-written \( ... \) spans and everything else is plain
# text. Concentrations are written "moles per liter" in prose.
TOPIC = ("5.1", "Reaction Rates", 5)

_T_DECOMP = dict(
    headers=["Time (seconds)", "Concentration of N2O5 (moles per liter)"],
    rows=[["0", "0.400"],
          ["100", "0.320"],
          ["200", "0.260"],
          ["300", "0.212"],
          ["400", "0.172"]])

_T_PRODUCT = dict(
    headers=["Time (seconds)", "Moles of O2 collected"],
    rows=[["0", "0.000"],
          ["20", "0.012"],
          ["40", "0.024"],
          ["60", "0.036"],
          ["80", "0.048"]])

_T_FACTORS = dict(
    headers=["Trial", "Form of the calcium carbonate",
             "Temperature (degrees Celsius)",
             "Time for the reaction to finish (seconds)"],
    rows=[["1", "One large lump", "25", "310"],
          ["2", "Coarse chips", "25", "185"],
          ["3", "Fine powder", "25", "62"],
          ["4", "Fine powder", "45", "21"]])

_T_RATIOS = dict(
    headers=["Balanced equation", "Coefficient of the reactant monitored",
             "Coefficient of the product monitored"],
    rows=[["2 N2O5 gives 4 NO2 + O2", "2", "4"],
          ["N2 + 3 H2 gives 2 NH3", "3", "2"],
          ["2 H2O2 gives 2 H2O + O2", "2", "1"]])

_T_CATALYST = dict(
    headers=["Trial", "Catalyst present",
             "Time for half the hydrogen peroxide to decompose (seconds)"],
    rows=[["A", "None", "2400"],
          ["B", "Manganese dioxide", "35"],
          ["C", "Catalase", "4"]])

QUESTIONS = [

 dict(q="How is the kinetics of a chemical reaction defined in this course?",
      choices=[
        "As the rate at which an amount of reactants is converted to products "
        "per unit of time",
        "As the total amount of product a reaction can eventually make",
        "As the energy released or absorbed when the reactants become products",
        "As the ratio of products to reactants once the mixture stops changing",
        "As the temperature at which a reaction first becomes observable"],
      ans=0,
      why="EK 5.1.A.1, near verbatim: the kinetics of a chemical reaction is "
          "defined as the rate at which an amount of reactants is converted to "
          "products per unit of time. How much product forms in the end and how "
          "much energy is exchanged are different questions."),

 dict(q="For the reaction 2 N2O5 → 4 NO2 + O2, nitrogen dioxide appears at 0.080 "
        "moles per liter per second. At what rate is N2O5 disappearing?",
      choices=["0.040 moles per liter per second",
               "0.080 moles per liter per second",
               "0.16 moles per liter per second",
               "0.020 moles per liter per second",
               "0.32 moles per liter per second"],
      ans=0,
      why="EK 5.1.A.2 makes the rates of change of reactant and product "
          "concentrations determined by the stoichiometry in the balanced "
          "equation. Four NO2 appear for every two N2O5 consumed, so the "
          "reactant disappears at half the rate the product appears."),

 dict(q="For the reaction N2 + 3 H2 → 2 NH3, hydrogen is consumed at 0.30 moles "
        "per liter per second. At what rate is ammonia being produced?",
      choices=["0.20 moles per liter per second",
               "0.30 moles per liter per second",
               "0.45 moles per liter per second",
               "0.10 moles per liter per second",
               "0.60 moles per liter per second"],
      ans=0,
      why="EK 5.1.A.2 ties the several rates of one reaction to the coefficients "
          "of the balanced equation. Two ammonia molecules form for every three "
          "hydrogen molecules consumed, so the ammonia rate is two thirds of the "
          "hydrogen rate."),

 dict(q="Which of the following is named in the course framework as a factor "
        "that influences the rate of a reaction?",
      choices=[
        "The surface area of a solid reactant",
        "The molar mass of the product formed",
        "The color of the container in which the reaction is run",
        "The total mass of solvent present, independent of concentration",
        "The number of atoms in the balanced chemical equation"],
      ans=0,
      why="EK 5.1.A.3 lists reactant concentrations, temperature, surface area, "
          "catalysts and other environmental factors as influences on the rate "
          "of a reaction. Surface area is on that list and the other four "
          "options are not."),

 dict(q="The table records the concentration of N2O5 as it decomposes. What is "
        "the average rate at which N2O5 disappeared over the first 100 seconds?",
      table=_T_DECOMP,
      choices=["0.00080 moles per liter per second",
               "0.0080 moles per liter per second",
               "0.080 moles per liter per second",
               "0.00040 moles per liter per second",
               "0.0040 moles per liter per second"],
      ans=0,
      why="EK 5.1.A.1 defines the rate as an amount converted per unit of time, "
          "so an average rate is the change in concentration divided by the "
          "length of the interval it occurred over."),

 dict(q="Using the same table of N2O5 concentrations, how does the average rate "
        "over the last 100 seconds compare with the average rate over the first "
        "100 seconds?",
      table=_T_DECOMP,
      choices=[
        "It is smaller, because less N2O5 disappears in the later interval than "
        "in the earlier one",
        "It is larger, because the reaction has had more time to build up speed",
        "It is the same, because both intervals are 100 seconds long",
        "It is smaller, because the total elapsed time appears in the "
        "denominator",
        "It cannot be compared, because an average rate applies only to the "
        "first interval of an experiment"],
      ans=0,
      why="EK 5.1.A.1 makes a rate an amount converted per unit of time. The two "
          "intervals are equally long, so comparing the rates is comparing the "
          "concentration changes, and the later change is the smaller."),

 dict(q="A student grinds a lump of a solid reactant into a fine powder before "
        "adding it to an acid. What effect does this have, and why?",
      choices=[
        "The reaction goes faster, because surface area is one of the factors "
        "that influences a rate",
        "The reaction goes slower, because the powder packs together and "
        "excludes the acid",
        "The reaction goes at the same rate, because the mass of solid is "
        "unchanged",
        "The reaction produces more product overall, because grinding creates "
        "additional reactant",
        "The reaction goes faster, because grinding raises the concentration of "
        "the acid"],
      ans=0,
      why="EK 5.1.A.3 names surface area among the factors that influence the "
          "rate of a reaction. Grinding changes the surface area without "
          "changing how much reactant is present, so the amount of product "
          "eventually formed is unaffected."),

 dict(q="The table gives the moles of oxygen collected from a decomposition at "
        "several times. What is the average rate of oxygen production over the "
        "whole 80 seconds?",
      table=_T_PRODUCT,
      choices=["0.00060 moles per second", "0.0060 moles per second",
               "0.048 moles per second", "0.00012 moles per second",
               "0.0012 moles per second"],
      ans=0,
      why="EK 5.1.A.1 defines the rate as an amount converted per unit of time, "
          "so the average over an interval is the amount collected divided by "
          "the elapsed time."),

 dict(q="For the reaction 2 H2O2 → 2 H2O + O2, which statement about the three "
        "rates is correct?",
      choices=[
        "Hydrogen peroxide disappears twice as fast as oxygen appears",
        "Hydrogen peroxide disappears at the same rate at which oxygen appears",
        "Oxygen appears twice as fast as hydrogen peroxide disappears",
        "Water appears half as fast as hydrogen peroxide disappears",
        "All three rates are equal, because each species appears once in the "
        "equation"],
      ans=0,
      why="EK 5.1.A.2 makes the rates of change determined by the stoichiometry "
          "in the balanced equation. Two peroxide molecules are consumed and two "
          "water molecules formed for every one oxygen molecule, so the peroxide "
          "and water rates are twice the oxygen rate."),

 dict(q="Two identical flasks of the same reaction mixture are held at 20 degrees "
        "Celsius and 40 degrees Celsius. Which prediction is supported by the "
        "course framework?",
      choices=[
        "The warmer flask reacts faster, because temperature is one of the "
        "factors that influences a rate",
        "The two flasks react at the same rate, because they hold identical "
        "mixtures",
        "The cooler flask reacts faster, because the reactants are more "
        "concentrated when cold",
        "The warmer flask makes more product in total, because heating creates "
        "additional reactant",
        "No prediction is possible, because rate depends only on the balanced "
        "equation"],
      ans=0,
      why="EK 5.1.A.3 lists temperature among the factors that influence the "
          "rate of a reaction. It is a statement about how fast the conversion "
          "occurs, not about how much product the mixture can eventually make."),

 dict(q="The table reports how long a fixed mass of calcium carbonate took to "
        "react completely with excess acid under four sets of conditions. Which "
        "comparison isolates the effect of surface area alone?",
      table=_T_FACTORS,
      choices=[
        "Trials 1, 2 and 3, which differ in the form of the solid while the "
        "temperature is held at the same value",
        "Trials 3 and 4, which differ in temperature while the form of the solid "
        "is held the same",
        "Trials 1 and 4, which differ in both the form of the solid and the "
        "temperature",
        "All four trials together, because each one used the same mass of solid",
        "None of the trials, because time is not a measure of rate"],
      ans=0,
      why="EK 5.1.A.3 names surface area and temperature as separate influences "
          "on a rate. Isolating one requires a set of trials in which only that "
          "factor varies, which the table's temperature column identifies "
          "directly."),

 dict(q="Using the same table of calcium carbonate trials, which pair isolates "
        "the effect of temperature alone, and what does it show?",
      table=_T_FACTORS,
      choices=[
        "Trials 3 and 4, and the warmer trial finished in about a third of the "
        "time",
        "Trials 1 and 2, and the warmer trial finished in about half the time",
        "Trials 2 and 3, and the warmer trial finished in about a third of the "
        "time",
        "Trials 1 and 4, and the warmer trial finished in about a fifteenth of "
        "the time",
        "No pair, because every trial in the table used a different form of the "
        "solid"],
      ans=0,
      why="EK 5.1.A.3 names temperature among the influences on rate. Isolating "
          "it requires two trials whose only difference is temperature, and the "
          "ratio of their completion times measures how large that influence "
          "was."),

 dict(q="For a reaction A + 2 B → 3 C, the rate of change of each species is "
        "measured. Which set of relationships is correct?",
      choices=[
        "B disappears twice as fast as A does, and C appears three times as fast "
        "as A disappears",
        "B disappears half as fast as A does, and C appears a third as fast as A "
        "disappears",
        "All three species change at the same rate, because they take part in "
        "one reaction",
        "A disappears twice as fast as B does, and C appears three times as fast "
        "as B disappears",
        "C appears twice as fast as B disappears, because three is greater than "
        "two"],
      ans=0,
      why="EK 5.1.A.2 makes the rates of change of reactant and product "
          "concentrations determined by the stoichiometry in the balanced "
          "equation, so each rate stands in the ratio of that species' "
          "coefficient to the others."),

 dict(q="The table lists three balanced equations with the coefficients of the "
        "reactant and the product being followed in each. For which equation is "
        "the product formed at exactly twice the rate at which the reactant is "
        "consumed?",
      table=_T_RATIOS,
      choices=[
        "The decomposition of N2O5 to NO2 and O2, in which the coefficients are "
        "two and four",
        "The synthesis of ammonia, in which the coefficients are three and two",
        "The decomposition of hydrogen peroxide, in which the coefficients are "
        "two and one",
        "All three, because in each case a product coefficient exceeds a "
        "reactant coefficient",
        "None of them, because a product can never form faster than a reactant "
        "is consumed"],
      ans=0,
      why="EK 5.1.A.2 makes the rates determined by the stoichiometry, so the "
          "ratio of the two rates is the ratio of the two coefficients. The "
          "table supplies both coefficients for each equation directly."),

 dict(q="A reaction is run twice, once with 0.10 M reactant and once with 0.20 M "
        "reactant, with everything else held the same. The second run is "
        "observed to go faster. Which conclusion is supported?",
      choices=[
        "Reactant concentration influences the rate of this reaction",
        "The reaction must be first order with respect to that reactant",
        "The second run will produce twice as much product in total",
        "The rate constant for the reaction is larger in the second run",
        "The second run must have been carried out at a higher temperature"],
      ans=0,
      why="EK 5.1.A.3 names reactant concentrations among the factors that "
          "influence the rate. Establishing an order requires the quantitative "
          "comparison of 5.2, and the total product depends on the amounts "
          "supplied, not on the speed."),

 dict(q="Why does a rate have units of concentration per unit of time rather than "
        "concentration alone?",
      choices=[
        "Because a rate reports how much conversion occurs in a given interval, "
        "not how much has occurred in total",
        "Because concentration cannot be measured without also measuring time",
        "Because the balanced equation always contains a coefficient with units "
        "of time",
        "Because a reaction that has finished no longer has any concentration to "
        "report",
        "Because time appears in the definition only for reactions that involve "
        "a gas"],
      ans=0,
      why="EK 5.1.A.1 defines kinetics as the rate at which an amount of "
          "reactants is converted to products PER UNIT OF TIME, so the quantity "
          "is a change divided by the interval over which it happened."),

 dict(q="A catalyst is added to a reaction mixture. According to the framework, "
        "what is the effect on the rate?",
      choices=[
        "The rate is influenced, because catalysts are named among the factors "
        "that affect it",
        "The rate is unaffected, because a catalyst is not consumed by the "
        "reaction",
        "The rate falls, because the catalyst occupies space that the reactants "
        "would otherwise use",
        "The rate is unaffected unless the temperature is also raised",
        "The rate is influenced only if the catalyst is a solid with a large "
        "surface area"],
      ans=0,
      why="EK 5.1.A.3 lists catalysts among the factors that influence the rate "
          "of a reaction. That a catalyst is not consumed says nothing about "
          "whether it affects the speed."),

 dict(q="The table reports how long it took for half of a hydrogen peroxide "
        "sample to decompose with and without various catalysts. Which "
        "conclusion is supported?",
      table=_T_CATALYST,
      choices=[
        "The presence of a catalyst influenced the rate, and the two catalysts "
        "did not influence it equally",
        "The presence of a catalyst had no effect, because the same amount of "
        "peroxide decomposed in every trial",
        "Only a solid catalyst can influence the rate, since the shortest time "
        "belongs to a solid",
        "The catalysts changed how much peroxide could decompose, not how "
        "quickly",
        "The three trials cannot be compared, because they used different "
        "catalysts"],
      ans=0,
      why="EK 5.1.A.3 names catalysts among the factors influencing a rate. All "
          "three trials measured the same fraction decomposing, so the times "
          "compare speeds, and they differ from one another as well as from the "
          "uncatalyzed trial."),

 dict(q="For the reaction 4 NH3 + 5 O2 → 4 NO + 6 H2O, oxygen is consumed at 0.25 "
        "moles per liter per second. At what rate is water formed?",
      choices=["0.30 moles per liter per second",
               "0.25 moles per liter per second",
               "0.21 moles per liter per second",
               "0.20 moles per liter per second",
               "0.50 moles per liter per second"],
      ans=0,
      why="EK 5.1.A.2 makes the rates of change determined by the coefficients "
          "of the balanced equation. Six water molecules form for every five "
          "oxygen molecules consumed, so the water rate is six fifths of the "
          "oxygen rate."),

 dict(q="A rate expression for the reaction 2 A → B is sometimes written as "
        r"\( \mathrm{rate} = -\frac{1}{2}\frac{\Delta[\mathrm{A}]}{\Delta t} \). "
        "Why does the expression carry the factor of one half?",
      choices=[
        "So that the single reported rate agrees with the rate of formation of "
        "B, whose coefficient is one",
        "So that the reported rate is always a negative quantity",
        "Because concentration is measured in half-units of moles per liter",
        "Because a reaction with two reactant molecules takes twice as long to "
        "occur",
        "Because the factor converts an average rate into an instantaneous one"],
      ans=0,
      why="EK 5.1.A.2 makes the rates of change of the several species "
          "determined by the stoichiometry, so they are not equal to one "
          "another. Dividing each by its own coefficient gives one number that "
          "describes the reaction rather than one species."),

 dict(q="Which experimental change would be expected to leave the rate of a "
        "reaction between two dissolved species essentially unchanged?",
      choices=[
        "Pouring the same mixture into a wider beaker without changing "
        "concentration or temperature",
        "Warming the mixture by twenty degrees Celsius",
        "Doubling the concentration of one of the dissolved reactants",
        "Adding a catalyst for the reaction",
        "Replacing a lump of a solid reactant with the same mass as a powder"],
      ans=0,
      why="EK 5.1.A.3 names reactant concentrations, temperature, surface area "
          "and catalysts as influences. Changing the shape of the container "
          "alters none of those for a reaction between two dissolved species."),

 dict(q="Over the first 50 seconds of a reaction the concentration of a reactant "
        "falls from 0.500 to 0.350 moles per liter. What is the average rate of "
        "disappearance of that reactant?",
      choices=["0.0030 moles per liter per second",
               "0.030 moles per liter per second",
               "0.150 moles per liter per second",
               "0.0070 moles per liter per second",
               "0.00060 moles per liter per second"],
      ans=0,
      why="EK 5.1.A.1 defines the rate as an amount converted per unit of time, "
          "so the average rate over the interval is the concentration change "
          "divided by the number of seconds it took."),

 dict(q="Two reactions are compared. In the first, a reactant concentration falls "
        "by 0.20 moles per liter in 10 seconds; in the second, by 0.60 moles per "
        "liter in 60 seconds. Which reaction had the larger average rate, and by "
        "what factor?",
      choices=[
        "The first, by a factor of two",
        "The second, by a factor of three",
        "The first, by a factor of three",
        "The second, by a factor of two",
        "Neither, because they had the same average rate"],
      ans=0,
      why="EK 5.1.A.1 makes a rate an amount converted per unit of time, so each "
          "average rate is its own concentration change divided by its own "
          "interval, and the two quotients are then compared."),

 dict(q="A student says that because a reaction is exothermic it must also be "
        "fast. Which response is best?",
      choices=[
        "Energy released and rate are separate questions, and the framework "
        "lists the factors that influence rate without including the energy "
        "change",
        "The student is correct, because releasing energy speeds the conversion "
        "of reactants to products",
        "The student is correct only if the reaction also has a catalyst present",
        "The student is wrong, because exothermic reactions are always the "
        "slower kind",
        "The student is wrong, because rate depends only on the number of atoms "
        "in the equation"],
      ans=0,
      why="EK 5.1.A.1 defines the rate as an amount converted per unit of time "
          "and EK 5.1.A.3 lists what influences it: concentrations, temperature, "
          "surface area, catalysts and other environmental factors. The energy "
          "change of the reaction is not on that list."),

 dict(q="For the reaction 2 SO2 + O2 → 2 SO3, which rate of change is the "
        "smallest in magnitude at any instant?",
      choices=[
        "The rate for O2, whose coefficient is the smallest of the three",
        "The rate for SO2, because it is the species consumed in the larger "
        "amount",
        "The rate for SO3, because a product forms more slowly than a reactant "
        "disappears",
        "All three are equal, because the reaction is a single process",
        "The rate for SO3, whose coefficient is the smallest of the three"],
      ans=0,
      why="EK 5.1.A.2 makes the rates of change determined by the stoichiometry, "
          "so they stand in the ratio of the coefficients. The species with the "
          "smallest coefficient changes concentration most slowly."),

 dict(q="Nitrogen dioxide is produced at 0.24 moles per liter per second in the "
        "reaction 2 N2O5 → 4 NO2 + O2. At what rate is oxygen produced?",
      choices=["0.060 moles per liter per second",
               "0.12 moles per liter per second",
               "0.24 moles per liter per second",
               "0.96 moles per liter per second",
               "0.48 moles per liter per second"],
      ans=0,
      why="EK 5.1.A.2 makes the rates determined by the stoichiometry in the "
          "balanced equation. Four nitrogen dioxide molecules form for every one "
          "oxygen molecule, so oxygen appears at a quarter of the nitrogen "
          "dioxide rate."),

 dict(q="An investigation is designed to measure how the rate of a reaction "
        "depends on temperature. Which design feature is essential?",
      choices=[
        "Every trial uses the same reactant concentrations and the same physical "
        "form of any solid",
        "Every trial is run for the same length of time regardless of when it "
        "finishes",
        "Every trial uses a different catalyst so that a range of rates is "
        "obtained",
        "Every trial uses a different amount of reactant so that the effect is "
        "easier to see",
        "Every trial is stopped as soon as the first product is detected"],
      ans=0,
      why="EK 5.1.A.3 names several separate influences on rate: concentrations, "
          "temperature, surface area and catalysts. Attributing an observed "
          "difference to temperature requires the others to be held constant "
          "across the trials."),

 dict(q="Why can a single reaction be reported as having one rate even though its "
        "several species change concentration at different speeds?",
      choices=[
        "Because each species' rate of change is divided by its own coefficient "
        "from the balanced equation",
        "Because only the slowest-changing species is ever reported",
        "Because the concentrations of all species become equal as the reaction "
        "proceeds",
        "Because the coefficients of a balanced equation are always equal to one "
        "another",
        "Because the rate is defined for the solvent rather than for any "
        "reactant or product"],
      ans=0,
      why="EK 5.1.A.2 makes the rates of change of reactant and product "
          "concentrations determined by the stoichiometry in the balanced "
          "equation. Dividing each measured rate by that species' coefficient "
          "gives one value common to all of them."),

 dict(q="In a reaction between a solid and a solution, which change increases the "
        "amount of solid exposed to the solution without changing how much solid "
        "is present?",
      choices=[
        "Breaking the solid into many smaller pieces of the same total mass",
        "Adding a second, larger piece of the same solid to the vessel",
        "Raising the temperature of the solution by ten degrees Celsius",
        "Diluting the solution with an equal volume of solvent",
        "Stirring the mixture more slowly than before"],
      ans=0,
      why="EK 5.1.A.3 names surface area as a factor that influences the rate. "
          "Dividing a fixed mass into smaller pieces increases the exposed area "
          "while leaving the amount of reactant unchanged, which is what the "
          "question asks to separate."),

 dict(q="A reaction mixture is monitored and the concentration of a product is "
        "found to rise quickly at first and then more slowly, finally becoming "
        "constant. What does the framework's definition of rate imply about the "
        "final part of the curve?",
      choices=[
        "The rate has fallen to zero there, because no further amount is being "
        "converted per unit of time",
        "The rate is at its largest there, because the product concentration is "
        "at its largest",
        "The rate is negative there, because the reaction has begun to run "
        "backward",
        "The rate cannot be defined there, because a rate applies only while a "
        "concentration is changing quickly",
        "The rate is constant but nonzero there, because a constant "
        "concentration means a constant rate"],
      ans=0,
      why="EK 5.1.A.1 defines the rate as the amount converted per unit of time. "
          "If the concentration is no longer changing, the amount converted in "
          "each further interval is zero, and so is the rate that measures it."),
]
