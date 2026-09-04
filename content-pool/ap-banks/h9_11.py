# AP CHEMISTRY 9.11 Electrolysis and Faraday's Law
# CED effective Fall 2024, Unit 9 Thermodynamics and Electrochemistry.
# Learning objective 9.11.A: calculate the amount of charge flow based on changes in the
# amounts of reactants and products in an electrochemical cell. Suggested skill 5.B,
# identify an appropriate theory, definition, or mathematical relationship to solve a
# problem.
#
# Essential knowledge relied on, in the framework's own words:
#   9.11.A.1  Faraday's laws can be used to determine the stoichiometry of the redox
#             reaction occurring in an electrochemical cell with respect to the following:
#               i.   Number of electrons transferred
#               ii.  Mass of material deposited on or removed from an electrode (as in
#                    electroplating)
#               iii. Current
#               iv.  Time elapsed
#               v.   Charge of ionic species
#             EQN: \( I = \frac{q}{t} \)
#
# Supporting statements used where the framework's own reasoning needs them:
#   The equation and constant sheet, verbatim: Faraday's constant is 96,485 coulombs per one
#   mole of electrons, I is the current in amperes, q the charge in coulombs and t the time
#   in seconds.
#   EK 9.8.A.3  Oxidation occurs at the anode and reduction at the cathode, which is what
#               decides WHICH electrode gains the mass EK 9.11.A.1.ii speaks of and which
#               loses it.
#   EK 9.9.A.1  A thermodynamically unfavored reaction gives a negative voltage and requires
#               an externally applied potential -- the reason an electrolysis needs a supply
#               at all. One item makes that link and states the sign.
#
# THE SIGN IS THE ANSWER IN ONE PLACE HERE, AND IT IS GATED. EK 9.11.A.1.ii names mass
# DEPOSITED ON or REMOVED FROM an electrode, so a mass change in this topic carries a sign,
# and the two electrodes carry opposite ones. Every item that states a signed mass change
# states it with its sign, offers the sign-flipped value as a distractor, and is checked in
# verify_h9_11.py by a RAW token comparison rather than through a normalizer that drops a
# leading plus. The same is done for the negative cell potential of a driven reaction.
#
# EVERY OTHER NUMBER IS A MAGNITUDE, AND EVERY ONE IS RECOMPUTED. Each quantitative stem
# carries its own current, time, charge, half-reaction and molar mass, and verify_h9_11.py
# reads those out of the stem rather than holding a copy of them, then recomputes the key to
# three significant figures. A check that carried its own copy of a stem's numbers would
# keep passing after the stem had been edited.
#
# THE FIGURE PROBLEM. An electrolytic cell is normally taught from a drawing and this bank
# carries no images. Every cell below is described in words -- the electrodes, the solution,
# the external supply -- or carried as a table of half-reactions, currents and times. No
# stem says "shown" or "the diagram", and verify_h9_11.py asserts that.
#
# SCOPE. 9.8 owns the physical components, 9.9 owns the standard cell potential and its
# arithmetic, and 9.10 owns nonstandard conditions. So no item here computes a cell
# potential from reduction potentials, and none mentions a reaction quotient or the Nernst
# equation.
#
# NOTATION. export_units.py does not typeset Chemistry. Every span is hand-written, formulas
# in prose stay plain text, and no number carries a thousands separator except in the
# framework's own quoted value of Faraday's constant -- a separator would otherwise split a
# recomputed value into two tokens.
TOPIC = ("9.11", "Electrolysis and Faraday’s Law", 9)

_T_RUNS = dict(
    headers=["Run", "Current (A)", "Time (s)"],
    rows=[["Run 1", "5.00", "1930"],
          ["Run 2", "2.00", "4825"],
          ["Run 3", "1.00", "1930"],
          ["Run 4", "10.0", "1930"]])

_T_METALS = dict(
    headers=["Half-reaction at the cathode", "Molar mass (g/mol)"],
    rows=[["Ag+(aq) + e- gives Ag(s)", "107.87"],
          ["Cu2+(aq) + 2 e- gives Cu(s)", "63.55"],
          ["Al3+(aq) + 3 e- gives Al(s)", "26.98"],
          ["Zn2+(aq) + 2 e- gives Zn(s)", "65.38"]])

QUESTIONS = [

 dict(q="What does the course framework say Faraday's laws can be used to determine?",
      choices=[
        "The stoichiometry of the redox reaction occurring in an electrochemical cell",
        "The rate at which the redox reaction reaches equilibrium",
        "The standard reduction potential of each half-reaction",
        "The temperature at which a cell reaction becomes favored",
        "The number of half-cells a working cell must contain"],
      ans=0,
      why="EK 9.11.A.1 states that Faraday's laws can be used to determine the stoichiometry "
          "of the redox reaction occurring in an electrochemical cell, and then lists the "
          "five quantities that stoichiometry connects. A reduction potential is EK 9.9.A.2's "
          "material and a rate is Unit 5's."),

 dict(q="Which set of quantities does the framework list as what Faraday's laws relate?",
      choices=[
        "Number of electrons transferred, mass deposited or removed, current, time elapsed, "
        "and charge of the ionic species",
        "Number of electrons transferred, cell potential, temperature, pressure, and time "
        "elapsed",
        "Mass deposited or removed, cell potential, current, volume of solution, and "
        "temperature",
        "Current, time elapsed, reaction quotient, equilibrium constant, and charge of the "
        "ionic species",
        "Number of half-cells, mass of each electrode, current, time elapsed, and "
        "temperature"],
      ans=0,
      why="EK 9.11.A.1 lists exactly five things: the number of electrons transferred, the "
          "mass of material deposited on or removed from an electrode as in electroplating, "
          "the current, the time elapsed, and the charge of the ionic species. Neither the "
          "temperature nor the cell potential is among them."),

 dict(q="Which equation does the framework attach to this topic?",
      choices=[
        "\\( I = \\frac{q}{t} \\)",
        "\\( I = qt \\)",
        "\\( I = \\frac{t}{q} \\)",
        "\\( q = \\frac{I}{t} \\)",
        "\\( I = \\frac{q}{nF} \\)"],
      ans=0,
      why="EK 9.11.A.1's EQN gives the current as the charge divided by the time elapsed, "
          "which is what lets two of the five quantities it lists be exchanged for the "
          "third. Faraday's constant enters at the next step, converting a charge into moles "
          "of electrons, rather than in this equation."),

 dict(q="What does the framework's equation and constant sheet give as Faraday's constant?",
      choices=[
        "96,485 coulombs per one mole of electrons",
        "96,485 coulombs per one electron",
        "96,485 moles of electrons per coulomb",
        "96,485 joules per volt",
        "96,485 amperes per second"],
      ans=0,
      why="The equation and constant sheet states Faraday's constant as 96,485 coulombs per "
          "one mole of electrons, which is the conversion between a charge in coulombs and "
          "the number of electrons transferred that EK 9.11.A.1 lists first."),

 dict(q="A cell is operated at a steady current of 1.50 A for 2000 s. How much charge passes "
        "through it?",
      choices=["3000 C", "1330 C", "750 C", "300 C", "It cannot be found without the "
               "identity of the metal"],
      ans=0,
      why="EK 9.11.A.1's equation gives the current as the charge over the time elapsed, so "
          "the charge is the current multiplied by the time. Dividing the time by the "
          "current instead is the error behind the second value offered, and the identity of "
          "the metal enters only when a mass is wanted."),

 dict(q="An electrolysis passes 5790 C of charge at a steady current of 3.00 A. For how long "
        "did it run?",
      choices=["1930 s", "17400 s", "579 s", "300 s",
               "It cannot be found without the number of electrons transferred"],
      ans=0,
      why="Rearranging EK 9.11.A.1's equation gives the time elapsed as the charge divided by "
          "the current. Multiplying the two instead gives the largest value offered, and the "
          "number of electrons per ion is needed only to go on to an amount of substance."),

 dict(q="A different electrolysis passes 9650 C of charge in 1930 s. What steady current did "
        "it draw?",
      choices=["5.00 A", "0.200 A", "1.93 A", "9650 A",
               "It cannot be found without the molar mass of the product"],
      ans=0,
      why="EK 9.11.A.1's equation gives the current directly as the charge divided by the "
          "time elapsed. Inverting that quotient gives the second value offered, and the "
          "molar mass is needed only when the question asks for a mass."),

 dict(q="How many moles of electrons are carried by 48250 C of charge?",
      choices=["0.500 mol", "2.00 mol", "0.0500 mol", "5.00 mol",
               "It cannot be found without the current"],
      ans=0,
      why="The equation and constant sheet gives Faraday's constant as 96,485 coulombs per "
          "one mole of electrons, so dividing a charge by that constant returns the number "
          "of electrons transferred that EK 9.11.A.1 lists first. The current is not needed, "
          "because the charge is already known."),

 dict(q="How much charge is carried by 0.100 mol of electrons?",
      choices=["9650 C", "965 C", "96500 C", "1930 C",
               "It cannot be found without the time elapsed"],
      ans=0,
      why="Multiplying a number of moles of electrons by Faraday's constant returns the "
          "charge in coulombs, which is the same conversion read the other way. The time "
          "elapsed matters only for the current, under EK 9.11.A.1's equation."),

 dict(q="In the half-reaction Cu2+(aq) + 2 e- gives Cu(s), a charge of 9650 C is passed "
        "through a copper(II) solution. What mass of copper is deposited, given that the "
        "molar mass of copper is 63.55 g/mol?",
      choices=["3.18 g", "6.36 g", "1.59 g", "63.6 g",
               "It cannot be found without the current"],
      ans=0,
      why="The charge gives the moles of electrons through Faraday's constant, the "
          "half-reaction's two electrons per ion give the moles of copper, and the molar "
          "mass gives the mass. Forgetting to divide by the two electrons doubles the answer, "
          "which is what EK 9.11.A.1's fifth item, the charge of the ionic species, exists to "
          "prevent."),

 dict(q="A charge of 9650 C is passed through a silver solution in which Ag+(aq) + e- gives "
        "Ag(s). What mass of silver is deposited, given that the molar mass of silver is "
        "107.87 g/mol?",
      choices=["10.8 g", "5.39 g", "21.6 g", "108 g",
               "It cannot be found without the time elapsed"],
      ans=0,
      why="One electron per silver ion means the moles of silver equal the moles of "
          "electrons, so the same charge deposits twice as many moles here as it does for a "
          "two-electron ion. This is EK 9.11.A.1's fifth item, the charge of the ionic "
          "species, doing its work."),

 dict(q="A charge of 28950 C is passed through an aluminium solution in which Al3+(aq) + 3 "
        "e- gives Al(s). What mass of aluminium is deposited, given that the molar mass of "
        "aluminium is 26.98 g/mol?",
      choices=["2.70 g", "8.09 g", "0.899 g", "26.98 g",
               "It cannot be found without the current"],
      ans=0,
      why="The charge gives 0.300 mol of electrons through Faraday's constant, and the "
          "half-reaction's three electrons per ion give a third of that in moles of "
          "aluminium. Skipping the division by three triples the answer."),

 dict(q="An electrolysis transfers 0.400 mol of electrons through a solution in which "
        "Ni2+(aq) + 2 e- gives Ni(s). How many moles of nickel are deposited?",
      choices=["0.200 mol", "0.400 mol", "0.800 mol", "0.100 mol",
               "It cannot be found without the molar mass of nickel"],
      ans=0,
      why="EK 9.11.A.1's fifth item is the charge of the ionic species, and the "
          "half-reaction's two electrons per nickel ion make the moles of metal half the "
          "moles of electrons. The molar mass is needed only to turn that amount into a mass."),

 dict(q="The same charge is passed separately through a solution of a 1+ ion and a solution "
        "of a 3+ ion of the same element. How do the amounts of metal deposited compare?",
      choices=[
        "Three times as many moles are deposited from the 1+ solution",
        "Three times as many moles are deposited from the 3+ solution",
        "The same number of moles is deposited from each",
        "Nine times as many moles are deposited from the 1+ solution",
        "The comparison depends on the current rather than on the charge"],
      ans=0,
      why="EK 9.11.A.1's fifth item is the charge of the ionic species, and a 3+ ion needs "
          "three electrons where a 1+ ion needs one, so the same number of electrons "
          "discharges three times as many of the singly charged ions. The current does not "
          "enter, since the charge passed is what has been fixed."),

 dict(q="How long must a current of 5.00 A run to deposit 0.0500 mol of copper from a "
        "solution in which Cu2+(aq) + 2 e- gives Cu(s)?",
      choices=["1930 s", "965 s", "3860 s", "48200 s",
               "It cannot be found without the molar mass of copper"],
      ans=0,
      why="The two electrons per copper ion turn the amount of metal into moles of electrons, "
          "Faraday's constant turns that into a charge, and EK 9.11.A.1's equation turns the "
          "charge and the current into a time. The molar mass is not needed, because the "
          "amount is already given in moles."),

 dict(q="What steady current would deposit 0.100 mol of silver in 1930 s from a solution in "
        "which Ag+(aq) + e- gives Ag(s)?",
      choices=["5.00 A", "10.0 A", "2.50 A", "1.00 A",
               "It cannot be found without the molar mass of silver"],
      ans=0,
      why="One electron per silver ion makes the moles of electrons equal to the moles of "
          "silver, Faraday's constant converts that into a charge, and EK 9.11.A.1's equation "
          "divides the charge by the time elapsed to give the current."),

 dict(q="Copper is plated onto one electrode from a solution in which Cu2+(aq) + 2 e- "
        "gives Cu(s), while copper dissolves from the other electrode, and 9650 C is passed. "
        "Taking the molar mass of copper as 63.55 g/mol, what are the two changes in "
        "electrode mass?",
      choices=[
        "The change is \\( +3.18 \\) g at the cathode and \\( -3.18 \\) g at the anode",
        "The change is \\( -3.18 \\) g at the cathode and \\( +3.18 \\) g at the anode",
        "The change is \\( +1.59 \\) g at the cathode and \\( -1.59 \\) g at the anode",
        "The change is \\( +6.36 \\) g at the cathode and \\( -6.36 \\) g at the anode",
        "The change is \\( +3.18 \\) g at each of the two electrodes"],
      ans=0,
      why="EK 9.11.A.1's second item is the mass of material deposited ON or removed FROM an "
          "electrode, so the two changes are equal in size and opposite in sign. EK 9.8.A.3 "
          "settles which is which: reduction at the cathode deposits the metal and oxidation "
          "at the anode dissolves it. The two electrons per copper ion fix the size."),

 dict(q="During an electroplating run, which electrode gains mass and which loses it?",
      choices=[
        "The cathode gains mass, because reduction deposits metal there, and the anode loses "
        "mass, because oxidation dissolves it",
        "The anode gains mass, because reduction deposits metal there, and the cathode loses "
        "mass, because oxidation dissolves it",
        "Both electrodes gain mass, because metal is deposited at each of them",
        "Both electrodes lose mass, because current carries metal into the solution",
        "Neither changes in mass, because the metal only moves through the solution"],
      ans=0,
      why="EK 9.11.A.1's second item names both a deposit and a removal, and EK 9.8.A.3 "
          "assigns reduction to the cathode and oxidation to the anode. Metal ions gaining "
          "electrons build up on the cathode while metal atoms losing them leave the anode, "
          "so one electrode gains exactly what the other loses."),

 dict(q="The table gives the current and the time for four electrolysis runs. How much charge "
        "passed in run 1?",
      table=_T_RUNS,
      choices=["9650 C", "386 C", "1930 C", "19300 C",
               "It cannot be found without the metal being deposited"],
      ans=0,
      why="EK 9.11.A.1's equation makes the charge the product of the tabulated current and "
          "the tabulated time elapsed. Dividing the two instead gives the smallest value "
          "offered, and the identity of the metal matters only once a mass is wanted."),

 dict(q="Using the same four runs, which passed the greatest charge?",
      table=_T_RUNS,
      choices=["Run 4", "Run 1", "Run 2", "Run 3", "Runs 1 and 2 equally"],
      ans=0,
      why="EK 9.11.A.1's equation makes the charge the product of the tabulated current and "
          "time, so neither column decides the comparison on its own. One tabulated row gives "
          "a larger product than any other."),

 dict(q="Using the same four runs, which passed the smallest charge?",
      table=_T_RUNS,
      choices=["Run 3", "Run 1", "Run 2", "Run 4", "Runs 1 and 3 equally"],
      ans=0,
      why="Multiplying each tabulated current by its tabulated time gives one row a smaller "
          "product than any other. A long run at a small current can still pass less charge "
          "than a short run at a large one, which is what EK 9.11.A.1's equation says."),

 dict(q="Among the same four runs, which two passed equal quantities of charge?",
      table=_T_RUNS,
      choices=["Runs 1 and 2", "Runs 1 and 3", "Runs 2 and 4", "Runs 3 and 4",
               "No two of them passed equal charge"],
      ans=0,
      why="EK 9.11.A.1's equation lets a large current for a short time pass the same charge "
          "as a small current for a long time. Exactly one pair of tabulated rows gives the "
          "same product of current and time elapsed."),

 dict(q="How many moles of electrons were transferred in run 4 of the table?",
      table=_T_RUNS,
      choices=["0.200 mol", "0.100 mol", "0.0200 mol", "2.00 mol",
               "It cannot be found without the ionic charge of the metal"],
      ans=0,
      why="The tabulated current and time give the charge through EK 9.11.A.1's equation, and "
          "Faraday's constant turns that charge into the number of electrons transferred, "
          "which EK 9.11.A.1 lists first. The ionic charge is needed only for the step from "
          "electrons to moles of metal."),

 dict(q="The table gives four cathode half-reactions and the molar masses of the metals. If "
        "9650 C is passed through each solution in turn, which metal is deposited in the "
        "greatest MASS?",
      table=_T_METALS,
      choices=["Silver", "Copper", "Aluminium", "Zinc",
               "All four are deposited in equal masses"],
      ans=0,
      why="The same charge gives the same moles of electrons in every case, and each "
          "tabulated half-reaction then fixes the moles of metal, which the tabulated molar "
          "mass turns into a mass. The metal needing the fewest electrons per ion and having "
          "the largest molar mass wins on both counts."),

 dict(q="Using the same four half-reactions and the same charge of 9650 C, which metal is "
        "deposited in the smallest mass?",
      table=_T_METALS,
      choices=["Aluminium", "Copper", "Silver", "Zinc",
               "All four are deposited in equal masses"],
      ans=0,
      why="The metal needing the most electrons per ion and having the smallest tabulated "
          "molar mass is deposited in the least mass for a fixed charge. Both of EK "
          "9.11.A.1's later items, the charge of the ionic species and the mass deposited, "
          "are at work in the comparison."),

 dict(q="Using the same table, what mass of zinc is deposited by 9650 C of charge?",
      table=_T_METALS,
      choices=["3.27 g", "6.54 g", "1.63 g", "65.4 g",
               "It cannot be found without the current"],
      ans=0,
      why="Faraday's constant turns the charge into moles of electrons, the tabulated "
          "half-reaction's two electrons per ion halve that to give moles of zinc, and the "
          "tabulated molar mass turns it into a mass. The current is not needed once the "
          "charge is known."),

 dict(q="Using the same table, how many moles of aluminium are deposited by 9650 C of charge?",
      table=_T_METALS,
      choices=["0.0333 mol", "0.100 mol", "0.300 mol", "0.0500 mol",
               "It cannot be found without the time elapsed"],
      ans=0,
      why="The charge gives the moles of electrons through Faraday's constant, and the "
          "tabulated half-reaction's three electrons per aluminium ion divide that by three. "
          "The time elapsed would be needed only to find the current."),

 dict(q="Using the same table, which two metals are deposited in equal NUMBERS OF MOLES "
        "when the same charge of 9650 C is passed through each solution?",
      table=_T_METALS,
      choices=["Copper and zinc", "Silver and copper", "Silver and aluminium",
               "Aluminium and zinc", "No two of them"],
      ans=0,
      why="For a fixed charge the moles of metal depend only on the electrons per ion in the "
          "tabulated half-reaction, which is EK 9.11.A.1's fifth item. Exactly two of the "
          "tabulated half-reactions call for the same number of electrons per ion, and their "
          "differing molar masses then give different masses."),

 dict(q="An electrolysis has to be driven by an external power supply, and the magnitude of "
        "the standard cell potential of the reaction being driven is 1.23 V. What is that "
        "standard cell potential?",
      choices=[
        "\\( -1.23 \\) V, because a reaction requiring an external supply is thermodynamically "
        "unfavored",
        "\\( +1.23 \\) V, because a reaction requiring an external supply is thermodynamically "
        "favored",
        "\\( +1.23 \\) V, because every electrolysis delivers energy to the circuit",
        "\\( -0.62 \\) V, because the potential is shared between the two electrodes",
        "Zero, because the external supply sets the potential instead"],
      ans=0,
      why="EK 9.9.A.1 says a thermodynamically unfavored reaction results in a negative "
          "voltage and requires an externally applied potential for the reaction to proceed, "
          "which is exactly the situation an electrolysis describes. The magnitude is given, "
          "so only the sign is in question, and the framework fixes it."),

 dict(q="Which sequence correctly gets from a current and a time to a mass of metal "
        "deposited?",
      choices=[
        "Multiply the current by the time, divide by Faraday's constant, divide by the "
        "electrons per ion, then multiply by the molar mass",
        "Multiply the current by the time, multiply by Faraday's constant, divide by the "
        "electrons per ion, then multiply by the molar mass",
        "Divide the current by the time, divide by Faraday's constant, multiply by the "
        "electrons per ion, then multiply by the molar mass",
        "Multiply the current by the time, divide by Faraday's constant, multiply by the "
        "electrons per ion, then divide by the molar mass",
        "Multiply the current by the molar mass, then divide by Faraday's constant and by "
        "the time"],
      ans=0,
      why="EK 9.11.A.1's equation supplies the first step, Faraday's constant the second, the "
          "charge of the ionic species the third and the molar mass the last, which is the "
          "chain of the five quantities the statement lists. Multiplying by Faraday's "
          "constant instead of dividing would turn a charge into a far larger number rather "
          "than into moles of electrons."),

]
