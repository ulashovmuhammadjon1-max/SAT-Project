# AP CHEMISTRY 4.5 Stoichiometry
# CED effective Fall 2024, Unit 4 Chemical Reactions.
# Learning objective 4.5.A: explain changes in the amounts of reactants and
# products based on the balanced reaction equation for a chemical process.
# Suggested skill 5.C, explain the relationship between variables within an
# equation when one variable changes.
#
# Essential knowledge relied on, in the framework's own words:
#   4.5.A.1  Because atoms must be conserved during a chemical process, it is
#            possible to calculate product amounts by using known reactant
#            amounts, or to calculate reactant amounts given known product
#            amounts.
#   4.5.A.2  Coefficients of balanced chemical equations contain information
#            regarding the proportionality of the amounts of substances
#            involved in the reaction. These values can be used in chemical
#            calculations involving the mole concept.
#   4.5.A.3  Stoichiometric calculations can be combined with the ideal gas law
#            and calculations involving molarity to quantitatively study gases
#            and solutions.
#
# ON THE ARITHMETIC. Every numerical key is recomputed in verify_h4_5.py from
# the numbers in the stem alone and asserted against the KEYED choice, so a
# moved key or an edited number fails there rather than reaching a student.
# Molar masses and, where a gas volume is wanted, the molar volume at the stated
# conditions are given in the stem, so nothing needs a calculator or a data
# table. That also keeps the gas items inside 4.5.A.3 rather than turning them
# into 3.4 ideal-gas-law items.
#
# NOTATION. Chemistry is not typeset. Formulas and equations are plain text
# (2 H2 + O2 gives 2 H2O). See SCIENCE_BRIEF.md and h_chem_notation.py.
TOPIC = ("4.5", "Stoichiometry", 4)

_T_PROPORTION = dict(
    headers=["Trial", "Moles of N2 consumed", "Moles of H2 consumed",
             "Moles of NH3 produced"],
    rows=[["1", "0.10", "0.30", "0.20"],
          ["2", "0.25", "0.75", "0.50"],
          ["3", "0.40", "1.20", "0.80"]])

_T_LIMITING = dict(
    headers=["Trial", "Moles of Al placed in the flask",
             "Moles of Cl2 placed in the flask", "Moles of AlCl3 formed"],
    rows=[["1", "2.0", "6.0", "2.0"],
          ["2", "4.0", "3.0", "2.0"],
          ["3", "4.0", "6.0", "4.0"]])

_T_MASSES = dict(
    headers=["Substance", "Molar mass (grams per mole)"],
    rows=[["CaCO3", "100."],
          ["CaO", "56.1"],
          ["CO2", "44.0"]])

_T_BURN = dict(
    headers=["Run", "Mass of magnesium burned (grams)",
             "Mass of magnesium oxide collected (grams)"],
    rows=[["1", "2.4", "4.0"],
          ["2", "4.8", "8.0"],
          ["3", "7.2", "12.0"]])

_T_SOLUTIONS = dict(
    headers=["Solution", "Concentration (moles per liter)", "Volume used (liters)"],
    rows=[["Silver nitrate", "0.200", "0.0500"],
          ["Sodium chloride", "0.100", "0.150"]])

_T_GASVOL = dict(
    headers=["Sample", "Moles of gas", "Volume measured (liters)"],
    rows=[["A", "0.500", "12.0"],
          ["B", "1.00", "24.0"],
          ["C", "2.50", "60.0"]])

QUESTIONS = [

 dict(q="Hydrogen and oxygen react according to 2 H2 + O2 → 2 H2O. A vessel is "
        "charged with 6.0 mol of H2 and more than enough O2, and all of the H2 "
        "reacts. How many moles of H2O are produced?",
      choices=["6.0 mol", "3.0 mol", "12 mol", "1.5 mol", "0.50 mol"],
      ans=0,
      why="EK 4.5.A.2 makes the coefficients of the balanced equation the "
          "proportionality between amounts. The coefficients of H2 and H2O are "
          "both 2, so the two amounts are equal and 6.0 mol of H2 yields 6.0 mol "
          "of H2O."),

 dict(q="Nitrogen and hydrogen combine according to N2 + 3 H2 → 2 NH3. If 0.60 "
        "mol of N2 reacts completely with excess H2, how many moles of NH3 form?",
      choices=["1.2 mol", "0.60 mol", "0.30 mol", "1.8 mol", "2.0 mol"],
      ans=0,
      why="EK 4.5.A.2: the coefficients give the proportionality of the amounts. "
          "Two moles of NH3 form for every one mole of N2 consumed, so 0.60 mol "
          "of N2 gives twice that amount of NH3."),

 dict(q="Aluminum reacts with chlorine according to 2 Al + 3 Cl2 → 2 AlCl3. A "
        "flask is charged with 4.0 mol of Al and 3.0 mol of Cl2 and the reaction "
        "proceeds until one reactant is used up. How many moles of AlCl3 form?",
      choices=["2.0 mol", "4.0 mol", "3.0 mol", "6.0 mol", "1.5 mol"],
      ans=0,
      why="EK 4.5.A.2: the coefficients set the proportionality. The Al on hand "
          "could make 4.0 mol of AlCl3 and the Cl2 on hand only 2.0 mol, so Cl2 "
          "runs out first and fixes the amount of product at 2.0 mol."),

 dict(q="Calcium carbonate decomposes on strong heating according to CaCO3 → CaO "
        "+ CO2. A 50.0 g sample of CaCO3 decomposes completely. Using the molar "
        "masses in the table, what mass of CO2 is released?",
      table=_T_MASSES,
      choices=["22.0 g", "44.0 g", "50.0 g", "28.0 g", "11.0 g"],
      ans=0,
      why="EK 4.5.A.1 and 4.5.A.2: 50.0 g of CaCO3 is 0.500 mol at 100. grams "
          "per mole, the coefficients make the CO2 amount equal to the CaCO3 "
          "amount, and 0.500 mol of CO2 at 44.0 grams per mole has a mass of "
          "22.0 g."),

 dict(q="A student needs the number of moles of HCl in 0.100 L of a solution "
        "labeled 0.500 M HCl. What is that amount?",
      choices=["0.0500 mol", "5.00 mol", "0.200 mol", "0.500 mol", "2.00 mol"],
      ans=0,
      why="EK 4.5.A.3 allows stoichiometric calculations to be combined with "
          "calculations involving molarity. Molarity is moles per liter, so the "
          "amount is the concentration multiplied by the volume in liters."),

 dict(q="Under the conditions of an experiment, one mole of any gas occupies "
        "24.0 L. What volume is occupied by 0.25 mol of oxygen gas under the "
        "same conditions?",
      choices=["6.0 L", "96 L", "24.0 L", "1.5 L", "12.0 L"],
      ans=0,
      why="EK 4.5.A.3 allows stoichiometric calculations to be combined with the "
          "ideal gas law. At fixed temperature and pressure the volume is "
          "proportional to the amount of gas, so a quarter of a mole occupies a "
          "quarter of the stated molar volume."),

 dict(q="Why is it possible to calculate the amount of a product from a known "
        "amount of a reactant?",
      choices=[
        "Because atoms are conserved during a chemical process, so the atoms in "
        "the products must be exactly those supplied by the reactants",
        "Because the mass of a product is always equal to the mass of the "
        "reactant that formed it",
        "Because every chemical process converts one mole of reactant into one "
        "mole of product",
        "Because the amount of product depends only on how long the reaction is "
        "allowed to run",
        "Because reactants and products always occupy the same volume under the "
        "same conditions"],
      ans=0,
      why="EK 4.5.A.1, near verbatim: because atoms must be conserved during a "
          "chemical process, it is possible to calculate product amounts using "
          "known reactant amounts, or reactant amounts given known product "
          "amounts."),

 dict(q="What information about a reaction is carried by the coefficients of its "
        "balanced chemical equation?",
      choices=[
        "The proportionality of the amounts of the substances involved, usable "
        "in calculations with the mole concept",
        "The masses in grams of each substance that must be weighed out before "
        "the reaction can begin",
        "The order of the reaction with respect to each reactant, which sets how "
        "fast the reaction runs",
        "The relative volumes that each substance occupies whether it is a "
        "solid, a liquid, or a gas",
        "The number of atoms of each element present in one gram of each "
        "substance"],
      ans=0,
      why="EK 4.5.A.2, near verbatim: coefficients of balanced chemical "
          "equations contain information regarding the proportionality of the "
          "amounts of substances involved in the reaction, and these values can "
          "be used in chemical calculations involving the mole concept."),

 dict(q="The table records three trials of the reaction N2 + 3 H2 → 2 NH3. Which "
        "statement is supported by the tabulated amounts?",
      table=_T_PROPORTION,
      choices=[
        "In every trial the amount of H2 consumed is three times the amount of "
        "N2 consumed, matching the coefficients",
        "In every trial the amounts of N2 and H2 consumed are equal, showing "
        "that coefficients do not affect amounts",
        "The amount of NH3 produced is equal to the amount of H2 consumed in "
        "each trial",
        "The amount of NH3 produced falls as the amount of N2 consumed rises",
        "The three trials contradict one another, because they consume "
        "different amounts of N2"],
      ans=0,
      why="EK 4.5.A.2 makes the coefficients the proportionality between "
          "amounts. Each row of the table shows the hydrogen amount at three "
          "times the nitrogen amount and the ammonia amount at twice it, which "
          "is the ratio 1 to 3 to 2 written in the equation."),

 dict(q="Propane burns according to C3H8 + 5 O2 → 3 CO2 + 4 H2O. If 2.0 mol of "
        "C3H8 burns completely in excess oxygen, how many moles of CO2 form?",
      choices=["6.0 mol", "2.0 mol", "8.0 mol", "10. mol", "0.67 mol"],
      ans=0,
      why="EK 4.5.A.2: the coefficients give the proportionality. Three moles of "
          "CO2 form per mole of C3H8 burned, so 2.0 mol of propane produces "
          "three times that amount of carbon dioxide."),

 dict(q="Aluminum and chlorine are combined as in 2 Al + 3 Cl2 → 2 AlCl3, "
        "starting from 4.0 mol of Al and 3.0 mol of Cl2. After the reaction has "
        "gone as far as it can, how much of the reactant in excess remains?",
      choices=["2.0 mol of Al", "1.0 mol of Al", "2.0 mol of Cl2",
               "1.0 mol of Cl2", "None of either reactant remains"],
      ans=0,
      why="EK 4.5.A.2: 3.0 mol of Cl2 is consumed entirely and, by the two to "
          "three ratio in the equation, consumes 2.0 mol of Al. That leaves the "
          "difference between the 4.0 mol supplied and the 2.0 mol used."),

 dict(q="A student titrates hydrochloric acid with sodium hydroxide, which react "
        "according to HCl + NaOH → NaCl + H2O. Exactly 25.0 mL of 0.200 M NaOH "
        "is required. How many moles of HCl were present?",
      choices=["0.00500 mol", "0.0200 mol", "0.0500 mol", "0.250 mol",
               "0.00250 mol"],
      ans=0,
      why="EK 4.5.A.3 combines stoichiometry with molarity calculations. The "
          "base supplies 0.200 moles per liter times 0.0250 L, and the "
          "coefficients make the acid and base amounts equal at the point where "
          "the acid is exactly consumed."),

 dict(q="Zinc reacts with hydrochloric acid according to Zn + 2 HCl → ZnCl2 + H2. "
        "A student reacts 0.10 mol of zinc with excess acid and collects the "
        "hydrogen under conditions where one mole of gas occupies 24.0 L. What "
        "volume of hydrogen is collected?",
      choices=["2.4 L", "4.8 L", "1.2 L", "24.0 L", "0.24 L"],
      ans=0,
      why="EK 4.5.A.3 combines stoichiometry with the ideal gas law. The "
          "coefficients make one mole of H2 form per mole of Zn, so 0.10 mol of "
          "gas is collected, and that amount occupies a tenth of the stated "
          "molar volume."),

 dict(q="The table gives the results of three runs in which magnesium was burned "
        "completely in oxygen. What do these data illustrate about the "
        "relationship between reactant and product amounts?",
      table=_T_BURN,
      choices=[
        "The mass of oxide collected is a fixed multiple of the mass of "
        "magnesium burned, because the ratio is set by the balanced equation",
        "The mass of oxide collected equals the mass of magnesium burned, "
        "because mass is conserved in a chemical process",
        "The mass of oxide collected grows faster than the mass of magnesium "
        "burned, because oxygen accumulates from run to run",
        "The three runs are inconsistent, because a larger sample should give "
        "proportionally less product",
        "No relationship can be found without knowing how long each run lasted"],
      ans=0,
      why="EK 4.5.A.1 and 4.5.A.2: atoms are conserved and the coefficients fix "
          "the proportion, so each run collects the same multiple of the "
          "magnesium mass. The oxide is heavier than the metal because it also "
          "contains the oxygen that combined with it."),

 dict(q="Iron(III) oxide is reduced by carbon monoxide according to Fe2O3 + 3 CO "
        "→ 2 Fe + 3 CO2. How many moles of CO are required to consume 0.50 mol "
        "of Fe2O3 completely?",
      choices=["1.5 mol", "0.50 mol", "3.0 mol", "1.0 mol", "0.17 mol"],
      ans=0,
      why="EK 4.5.A.2: the coefficients give the proportionality between "
          "amounts. Three moles of CO are consumed per mole of Fe2O3, so half a "
          "mole of the oxide requires three halves of a mole of carbon monoxide."),

 dict(q="A reaction produces 8.8 g of CO2 from the complete combustion of "
        "propane, C3H8 + 5 O2 → 3 CO2 + 4 H2O. Taking the molar mass of CO2 as "
        "44.0 grams per mole, how many moles of propane were burned?",
      choices=["0.067 mol", "0.20 mol", "0.60 mol", "8.80 mol", "0.30 mol"],
      ans=0,
      why="EK 4.5.A.1 allows reactant amounts to be calculated from known "
          "product amounts. The mass of CO2 corresponds to 0.20 mol, and the "
          "coefficients put three moles of CO2 with every one mole of propane, "
          "so the propane amount is a third of that."),

 dict(q="Silver nitrate solution and sodium chloride solution are mixed and react "
        "according to AgNO3 + NaCl → AgCl + NaNO3. Using the concentrations and "
        "volumes in the table, which reactant limits the amount of AgCl formed?",
      table=_T_SOLUTIONS,
      choices=[
        "Silver nitrate, because it supplies 0.0100 mol against 0.0150 mol of "
        "sodium chloride and the two react in a one to one ratio",
        "Sodium chloride, because its volume is the larger of the two",
        "Silver nitrate, because its concentration is the larger of the two",
        "Sodium chloride, because it supplies fewer moles than the silver "
        "nitrate does",
        "Neither, because the two solutions supply equal numbers of moles"],
      ans=0,
      why="EK 4.5.A.3 combines stoichiometry with molarity. Multiplying each "
          "concentration by its own volume gives the amount supplied, and with a "
          "one to one coefficient ratio the smaller of the two amounts is what "
          "runs out first."),

 dict(q="Sulfur dioxide is oxidized according to 2 SO2 + O2 → 2 SO3. A student "
        "doubles the amount of O2 while holding the amount of SO2 fixed, and the "
        "O2 was already present in excess. What happens to the amount of SO3 "
        "formed?",
      choices=[
        "It does not change, because the SO2 was already the reactant that runs "
        "out first",
        "It doubles, because doubling any reactant doubles the product",
        "It is halved, because the excess oxygen dilutes the sulfur dioxide",
        "It quadruples, because the coefficient of SO2 is two",
        "It cannot be predicted without knowing the temperature of the vessel"],
      ans=0,
      why="EK 4.5.A.2 makes the amount of product proportional to the amount of "
          "the reactant that is entirely consumed. Adding more of a reactant "
          "that was already in excess leaves that limit untouched, so the "
          "product amount is unchanged."),

 dict(q="Which statement correctly describes what a balanced chemical equation "
        "does NOT tell you directly?",
      choices=[
        "The mass in grams of each substance, which requires the molar masses in "
        "addition to the coefficients",
        "The proportion in which the substances are consumed and produced",
        "The number of moles of a product formed per mole of a reactant "
        "consumed",
        "The identity of each reactant and each product in the process",
        "The relative numbers of atoms of each element on the two sides"],
      ans=0,
      why="EK 4.5.A.2 restricts what the coefficients carry to the "
          "proportionality of the amounts, usable with the mole concept. "
          "Converting an amount to a mass needs the molar mass of that "
          "substance, which the equation does not supply."),

 dict(q="Ammonia burns according to 4 NH3 + 5 O2 → 4 NO + 6 H2O. A vessel holds "
        "1.0 mol of NH3 and 1.0 mol of O2. Which reactant is consumed first?",
      choices=[
        "Oxygen, because 1.0 mol of NH3 would require 1.25 mol of O2 and only "
        "1.0 mol is available",
        "Ammonia, because its coefficient in the equation is smaller than that "
        "of oxygen",
        "Ammonia, because the two gases are present in equal amounts and "
        "ammonia is listed first",
        "Neither, because the two gases are present in equal amounts and will "
        "run out together",
        "Oxygen, because oxygen is always the reactant consumed first in a "
        "combustion process"],
      ans=0,
      why="EK 4.5.A.2: the coefficients set the required proportion at five "
          "moles of O2 per four moles of NH3. Reacting all the ammonia would "
          "need more oxygen than the vessel holds, so the oxygen is exhausted "
          "while ammonia is left over."),

 dict(q="A 0.150 mol sample of a gas is collected and found to occupy 3.60 L. "
        "What volume would 0.500 mol of the same gas occupy at the same "
        "temperature and pressure?",
      choices=["12.0 L", "1.08 L", "3.60 L", "24.0 L", "0.75 L"],
      ans=0,
      why="EK 4.5.A.3 allows stoichiometric reasoning to be combined with the "
          "ideal gas law. At fixed temperature and pressure the volume is "
          "proportional to the amount, and the sample occupies 24.0 L per mole, "
          "so the larger amount occupies that multiple."),

 dict(q="The table lists the measured volumes of three gas samples at the same "
        "temperature and pressure. A fourth sample of the same gas is found to "
        "occupy 36.0 L. What amount of gas does it contain?",
      table=_T_GASVOL,
      choices=["1.50 mol", "0.750 mol", "3.60 mol", "36.0 mol", "0.150 mol"],
      ans=0,
      why="EK 4.5.A.3 combines stoichiometry with the ideal gas law. Every row "
          "in the table gives the same 24.0 L per mole, so dividing the new "
          "volume by that constant gives the amount in the fourth sample."),

 dict(q="Solid sodium hydrogen carbonate decomposes according to 2 NaHCO3 → "
        "Na2CO3 + H2O + CO2. If 0.40 mol of NaHCO3 decomposes completely, what "
        "total amount of gaseous products is released?",
      choices=["0.40 mol", "0.20 mol", "0.80 mol", "0.10 mol", "1.20 mol"],
      ans=0,
      why="EK 4.5.A.2: the coefficients put one mole each of H2O and CO2 with "
          "every two moles of NaHCO3. Decomposing 0.40 mol therefore gives 0.20 "
          "mol of each gas, and the two together make the stated total."),

 dict(q="A chemist wants 0.30 mol of AlCl3 from the reaction 2 Al + 3 Cl2 → 2 "
        "AlCl3, with chlorine in excess. What amount of aluminum is required?",
      choices=["0.30 mol", "0.45 mol", "0.15 mol", "0.60 mol", "0.90 mol"],
      ans=0,
      why="EK 4.5.A.1 allows a reactant amount to be calculated from a desired "
          "product amount. The coefficients of Al and AlCl3 are both two, so "
          "the two amounts are equal."),

 dict(q="Two students disagree about a reaction in which 10.0 g of a solid "
        "reacts with 5.0 g of a gas to give a single solid product. One says the "
        "product must weigh 15.0 g and the other says it must weigh 10.0 g. "
        "Which claim is correct, and why?",
      choices=[
        "15.0 g, because every atom in both reactants is present in the single "
        "product and atoms are conserved",
        "10.0 g, because only the solid reactant contributes mass to a solid "
        "product",
        "12.5 g, because a gas adds only half of its mass to a solid product",
        "10.0 g, because the gas escapes once it has caused the reaction to "
        "occur",
        "Neither, because the mass of a product cannot be predicted from the "
        "masses of the reactants"],
      ans=0,
      why="EK 4.5.A.1 rests on the conservation of atoms during a chemical "
          "process. Nothing else is formed here, so every atom supplied by the "
          "two reactants ends up in the one product and the masses add."),

 dict(q="Which of the following is required, in addition to the balanced "
        "equation, to convert a measured volume of a reactant solution into the "
        "mass of a product?",
      choices=[
        "The concentration of the solution and the molar mass of the product",
        "The temperature of the solution and the density of the product",
        "The rate constant for the reaction and the order with respect to the "
        "reactant",
        "The volume of the product and the pressure at which it is collected",
        "Nothing further, because the balanced equation converts volumes to "
        "masses directly"],
      ans=0,
      why="EK 4.5.A.3 allows stoichiometry to be combined with molarity "
          "calculations, and the concentration is what turns a solution volume "
          "into an amount. Turning that amount into a mass then requires the "
          "molar mass of the product."),

 dict(q="The table lists three trials of the reaction 2 Al + 3 Cl2 → 2 AlCl3. "
        "In which trial is aluminum the reactant that limits the product, with "
        "chlorine left over at the end?",
      table=_T_LIMITING,
      choices=[
        "Trial 1, in which the chlorine supplied is more than the three halves "
        "of the aluminum amount that the equation requires",
        "Trial 2, in which more aluminum than chlorine was placed in the flask",
        "Trial 3, in which the largest amount of product was formed",
        "Both Trial 2 and Trial 3, because both were charged with 4.0 mol of "
        "aluminum",
        "None of the trials, because chlorine has the larger coefficient and "
        "must always run out first"],
      ans=0,
      why="EK 4.5.A.2: the equation requires three moles of Cl2 per two moles of "
          "Al. Comparing each row's chlorine against three halves of its "
          "aluminum shows which reactant is short, and the product column "
          "confirms the amount that reactant allows."),

 dict(q="Copper reacts with silver nitrate solution according to Cu + 2 AgNO3 → "
        "Cu(NO3)2 + 2 Ag. If 0.030 mol of silver is deposited, what amount of "
        "copper was consumed?",
      choices=["0.015 mol", "0.030 mol", "0.060 mol", "0.0075 mol", "0.12 mol"],
      ans=0,
      why="EK 4.5.A.1 allows a reactant amount to be calculated from a known "
          "product amount, and EK 4.5.A.2 supplies the ratio: two moles of "
          "silver are deposited per mole of copper consumed, so the copper "
          "amount is half the silver amount."),

 dict(q="Exactly 0.0400 mol of a solid acid is dissolved and the solution is made "
        "up to 0.200 L. What is the concentration of the resulting solution?",
      choices=["0.200 M", "0.00800 M", "5.00 M", "0.0400 M", "2.00 M"],
      ans=0,
      why="EK 4.5.A.3 brings molarity into stoichiometric work, and molarity is "
          "defined as the amount of solute divided by the volume of solution in "
          "liters, which is what the two given quantities supply directly."),

 dict(q="An experiment is repeated with every reactant amount tripled and nothing "
        "else changed. Assuming the same reactant is still the one that runs out "
        "first, how does the amount of product compare with the original?",
      choices=[
        "It is three times as large, because the amounts are proportional to the "
        "amount of the reactant that is consumed entirely",
        "It is nine times as large, because tripling two reactants multiplies "
        "their effects",
        "It is unchanged, because the ratio of the reactants is the same as "
        "before",
        "It is one third as large, because a more crowded vessel converts less "
        "of each reactant",
        "It cannot be predicted, because a balanced equation applies to only one "
        "set of amounts"],
      ans=0,
      why="EK 4.5.A.2 makes the coefficients a statement of proportionality "
          "rather than of fixed amounts. Scaling every amount by the same factor "
          "leaves the limiting reactant unchanged and scales the product by that "
          "same factor."),
]
