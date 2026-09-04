r"""AP CHEMISTRY 3.7 Solutions and Mixtures.

CED effective Fall 2024, Unit 3 Properties of Substances and Mixtures.
Learning objective 3.7.A: calculate the number of solute particles, volume, or
molarity of solutions.
Suggested skill 5.F, calculate, estimate, or predict an unknown quantity from
known quantities by selecting and following a logical computational pathway and
attending to precision.

Essential knowledge relied on, in the framework's own words:

  3.7.A.1  Solutions, also sometimes called homogeneous mixtures, can be solids,
           liquids, or gases. In a solution, the macroscopic properties do not
           vary throughout the sample. In a heterogeneous mixture, the
           macroscopic properties depend on location in the mixture.
  3.7.A.2  Solution composition can be expressed in a variety of ways; molarity
           is the most common method used in the laboratory.
           EQN: M = n(solute) / L(solution)

THE EXCLUSIONS, which belong to topic 3.8 and are exam-wide. Colligative
properties will not be assessed, and calculations of molality, percent by mass
and percent by volume for solutions will not be assessed. So nothing here asks
for one. They appear only as DISTRACTORS in the two items about how composition
can be expressed -- a student should meet the names and learn that molarity is
the one the framework calls the laboratory's usual measure -- and
verify_h3_7.py asserts that no stem asks for one and no key states one, while
also asserting they are offered somewhere so the check is not idle.

THE DILUTION PREMISE IS STATED, NOT ASSUMED. The CED gives M = moles of solute
over liters of solution and asks for volume, molarity or solute particles to be
calculated. It does not separately state that adding water leaves the amount of
solute alone, so every dilution stem below SAYS SO in its own words -- water is
added and no solute is added or removed -- and the arithmetic then follows from
EK 3.7.A.2 alone. Item 14 keys that premise on its own.

THE DENOMINATOR IS THE SOLUTION, NOT THE SOLVENT. That is the single most
common wrong reading of EK 3.7.A.2's equation, so item 15 asks it directly, a
distractor in item 6 puts the solvent in the denominator, and verify_h3_7.py
refuses any key that divides by a volume of solvent.

NO FIGURES. Every set of solution data is carried as a table.

ARITHMETIC. Every number a key asserts is recomputed in verify_h3_7.py from the
stimulus alone, and most checks recompute the specific wrong turn a distractor
represents -- inverting the ratio, dividing by millilitres, or reporting the
concentration before the dilution instead of after it.

NOTATION. export_units.py does not typeset Chemistry, so the spans below are
hand-written. Unit words stay plain text.
"""
TOPIC = ("3.7", "Solutions and Mixtures", 3)

_T_SOL = dict(
    headers=["Solution", "Moles of solute", "Volume of solution (L)"],
    rows=[["Solution 1", "0.20", "2.0"],
          ["Solution 2", "0.60", "1.5"],
          ["Solution 3", "0.10", "0.50"],
          ["Solution 4", "0.40", "4.0"]])

QUESTIONS = [

 dict(q="What other name does the framework give to a solution?",
      choices=[
        "A homogeneous mixture",
        "A heterogeneous mixture",
        "A pure substance",
        "A suspension of one phase in another",
        "A compound of fixed formula"],
      ans=0,
      why="EK 3.7.A.1 opens by saying that solutions are also sometimes called homogeneous "
          "mixtures. A mixture is not a compound, and the heterogeneous case is the one the "
          "same sentence contrasts with a solution."),

 dict(q="In which physical states does the framework say a solution can exist?",
      choices=[
        "As a solid, a liquid or a gas",
        "As a liquid only",
        "As a liquid or a gas but never a solid",
        "As a solid or a liquid but never a gas",
        "As a gas only"],
      ans=0,
      why="EK 3.7.A.1 states that solutions can be solids, liquids, or gases. The idea that a "
          "solution must be a liquid is a habit of laboratory work rather than anything the "
          "framework says."),

 dict(q="What does the framework say about the macroscopic properties of a solution?",
      choices=[
        "They do not vary throughout the sample",
        "They depend on location within the sample",
        "They vary only near the walls of the container",
        "They cannot be measured without separating the components",
        "They are the same as those of the pure solvent"],
      ans=0,
      why="EK 3.7.A.1 states that in a solution the macroscopic properties do not vary "
          "throughout the sample. Dependence on location is what the very next sentence "
          "assigns to a heterogeneous mixture instead."),

 dict(q="What does the framework say about the macroscopic properties of a heterogeneous "
        "mixture?",
      choices=[
        "They depend on location in the mixture",
        "They do not vary throughout the sample",
        "They are always identical to those of a solution of the same components",
        "They cannot be measured at all",
        "They depend only on the total mass of the mixture"],
      ans=0,
      why="EK 3.7.A.1 states that in a heterogeneous mixture the macroscopic properties "
          "depend on location in the mixture. Uniformity throughout the sample is what the "
          "preceding sentence assigns to a solution."),

 dict(q="Which method of expressing solution composition does the framework name as the most "
        "common one used in the laboratory?",
      choices=[
        "Molarity",
        "Molality",
        "Percent by mass",
        "Percent by volume",
        "Mole fraction"],
      ans=0,
      why="EK 3.7.A.2 says that solution composition can be expressed in a variety of ways "
          "and that molarity is the most common method used in the laboratory. The other "
          "names are real ways of expressing composition, but the framework does not give "
          "any of them that standing."),

 dict(q="Which equation does the framework give for molarity?",
      choices=[
        "\\( M = \\frac{n_{\\mathrm{solute}}}{L_{\\mathrm{solution}}} \\)",
        "\\( M = \\frac{L_{\\mathrm{solution}}}{n_{\\mathrm{solute}}} \\)",
        "\\( M = n_{\\mathrm{solute}} \\times L_{\\mathrm{solution}} \\)",
        "\\( M = \\frac{n_{\\mathrm{solute}}}{L_{\\mathrm{solvent}}} \\)",
        "\\( M = n_{\\mathrm{solute}} - L_{\\mathrm{solution}} \\)"],
      ans=0,
      why="EK 3.7.A.2 gives molarity as the moles of solute divided by the litres of "
          "SOLUTION. The volume below the line is the volume the finished solution occupies, "
          "not the volume of solvent that was poured in before the solute dissolved."),

 dict(q="A solution contains 0.50 mol of solute in a total volume of 2.0 L. What is its "
        "molarity?",
      choices=[
        "0.25 M",
        "4.0 M",
        "1.0 M",
        "0.50 M",
        "2.5 M"],
      ans=0,
      why="EK 3.7.A.2's equation divides the moles of solute by the litres of solution. "
          "Dividing the volume by the moles instead inverts the ratio and gives a number "
          "larger than one, which is one of the values offered."),

 dict(q="How many moles of solute are present in 0.500 L of a 0.20 M solution?",
      choices=[
        "0.10 mol",
        "0.40 mol",
        "0.25 mol",
        "0.020 mol",
        "5.0 mol"],
      ans=0,
      why="EK 3.7.A.2's equation rearranged multiplies the molarity by the litres of "
          "solution. Dividing the molarity by the volume instead is the wrong turn one of "
          "the other values represents."),

 dict(q="What volume of a 3.0 M solution contains 0.60 mol of solute?",
      choices=[
        "0.20 L",
        "1.8 L",
        "5.0 L",
        "2.0 L",
        "0.50 L"],
      ans=0,
      why="EK 3.7.A.2's equation rearranged divides the moles of solute by the molarity. "
          "Multiplying the two instead, or dividing the molarity by the moles, gives two of "
          "the other values offered."),

 dict(q="A solution is made by dissolving 0.10 mol of solute and diluting to a total volume "
        "of 250 mL. What is the molarity?",
      choices=[
        "0.40 M",
        "0.00040 M",
        "2500 M",
        "25 M",
        "4.0 M"],
      ans=0,
      why="EK 3.7.A.2's equation takes litres below the line, so the volume must be converted "
          "before it is used. Dividing the moles by the volume in millilitres without "
          "converting gives a value a thousand times too small, which is one of the numbers "
          "offered, and attending to that conversion is part of suggested skill 5.F."),

 dict(q="A 25.0 mL portion of a 2.00 M solution is transferred to a flask and water is added "
        "until the total volume is 100.0 mL. No solute is added or removed. What is the "
        "molarity of the diluted solution?",
      choices=[
        "0.500 M",
        "8.00 M",
        "2.00 M",
        "0.250 M",
        "0.0500 M"],
      ans=0,
      why="The amount of solute is stated to be unchanged, so EK 3.7.A.2's equation is "
          "applied twice: the moles present are found from the original molarity and volume, "
          "then divided by the new volume. Multiplying by the volume ratio the other way "
          "round gives a concentration larger than the original, which cannot happen when "
          "only water is added."),

 dict(q="What volume of a 6.0 M stock solution is needed to prepare 250 mL of a 0.30 M "
        "solution, if the only other thing added is water?",
      choices=[
        "12.5 mL",
        "5.0 mL",
        "500 mL",
        "1.25 mL",
        "125 mL"],
      ans=0,
      why="EK 3.7.A.2's equation gives the moles the finished solution must contain, and the "
          "same equation applied to the stock gives the volume of stock holding that many "
          "moles. All of the solute has to come from the stock, since water carries none."),

 dict(q="Water is added to a solution until its volume is exactly doubled, with no solute "
        "added or removed. What happens to the molarity?",
      choices=[
        "It is halved",
        "It doubles",
        "It is unchanged",
        "It quadruples",
        "It falls to one quarter"],
      ans=0,
      why="EK 3.7.A.2's equation keeps the moles of solute above the line unchanged while "
          "the litres of solution below the line double, and doubling a denominator halves "
          "the quotient."),

 dict(q="Water is added to a solution and nothing else is added or removed. What happens to "
        "the number of moles of solute present?",
      choices=[
        "It is unchanged",
        "It doubles",
        "It is halved",
        "It rises in proportion to the volume added",
        "It falls in proportion to the volume added"],
      ans=0,
      why="Water contributes solvent and no solute, so the quantity above the line in "
          "EK 3.7.A.2's equation cannot change. This is the premise every dilution "
          "calculation rests on, which is why each dilution stem in this topic states it "
          "explicitly rather than leaving it to be assumed."),

 dict(q="Which volume belongs in the denominator of the framework's molarity equation?",
      choices=[
        "The volume of the solution",
        "The volume of the solvent used",
        "The volume of the solute alone",
        "The volume of the container holding the solution",
        "The volume of solvent and solute measured separately and added together"],
      ans=0,
      why="EK 3.7.A.2 writes molarity as moles of solute per litre of SOLUTION. The finished "
          "solution's volume is not in general the sum of the separate volumes, so the two "
          "readings do not give the same number and only one of them is the framework's."),

 dict(q="Which of the tabulated solutions is the most concentrated?",
      table=_T_SOL,
      choices=[
        "Solution 2",
        "Solution 1",
        "Solution 3",
        "Solution 4",
        "All four are equally concentrated"],
      ans=0,
      why="EK 3.7.A.2's equation gives each tabulated row a molarity from its own moles and "
          "volume. The largest amount of solute does not by itself settle the question, "
          "since the volumes differ too, so each ratio has to be formed before they are "
          "compared."),

 dict(q="What is the molarity of Solution 3 in the table?",
      table=_T_SOL,
      choices=[
        "0.20 M",
        "0.050 M",
        "5.0 M",
        "0.10 M",
        "0.60 M"],
      ans=0,
      why="EK 3.7.A.2's equation divides the tabulated moles of solute by the tabulated "
          "litres of solution for that row alone."),

 dict(q="Which two of the tabulated solutions have the same molarity as each other?",
      table=_T_SOL,
      choices=[
        "Solutions 1 and 4",
        "Solutions 1 and 2",
        "Solutions 2 and 3",
        "Solutions 3 and 4",
        "No two of them share a molarity"],
      ans=0,
      why="EK 3.7.A.2's equation gives each row its own ratio, and two rows can share a "
          "molarity while differing in both the moles present and the volume, which is "
          "exactly what one pair in the table does."),

 dict(q="Two samples are drawn from different parts of the same solution. How do their "
        "macroscopic properties compare?",
      choices=[
        "They are the same, because in a solution the macroscopic properties do not vary "
        "throughout the sample",
        "They may differ, because in a solution the macroscopic properties depend on "
        "location",
        "They are the same, but only if the solution has been stirred immediately before "
        "sampling",
        "They may differ, because the solute settles toward the bottom of any solution",
        "The comparison cannot be made without knowing the molarity"],
      ans=0,
      why="EK 3.7.A.1 states that in a solution the macroscopic properties do not vary "
          "throughout the sample, which is the whole content of calling it homogeneous. The "
          "framework makes that a property of being a solution, not a consequence of recent "
          "stirring."),

 dict(q="Two samples are drawn from different parts of the same heterogeneous mixture. How "
        "do their macroscopic properties compare?",
      choices=[
        "They may differ, because in a heterogeneous mixture the macroscopic properties "
        "depend on location in the mixture",
        "They are the same, because in a heterogeneous mixture the macroscopic properties do "
        "not vary throughout the sample",
        "They may differ, because a heterogeneous mixture has no macroscopic properties at "
        "all",
        "They are the same, because every mixture is uniform once it has been prepared",
        "The comparison cannot be made without knowing the number of components"],
      ans=0,
      why="EK 3.7.A.1 states that in a heterogeneous mixture the macroscopic properties "
          "depend on location in the mixture, which is what makes where you sample matter. "
          "Uniformity throughout is the property the same sentence gives to a solution."),

 dict(q="A metal alloy is uniform in composition at every point. Does the framework allow it "
        "to be called a solution?",
      choices=[
        "Yes, because the framework says solutions can be solids",
        "No, because a solution must be a liquid",
        "No, because a solution must contain a solvent that was originally a liquid",
        "Yes, but only if it can be melted without decomposing",
        "The framework does not say what physical states a solution may have"],
      ans=0,
      why="EK 3.7.A.1 says solutions can be solids, liquids, or gases, and it defines the "
          "solution case by macroscopic properties that do not vary throughout the sample. A "
          "uniform solid meets both parts of that description."),

 dict(q="A mixture of several gases has the same composition at every point in its "
        "container. How does the framework classify it?",
      choices=[
        "As a solution, since a solution is a homogeneous mixture and may be a gas",
        "As a heterogeneous mixture, since it contains more than one substance",
        "As a pure substance, since its properties are uniform",
        "As a compound, since the gases are mixed in fixed proportions",
        "The framework does not classify mixtures of gases"],
      ans=0,
      why="EK 3.7.A.1 calls solutions homogeneous mixtures, allows them to be gases, and "
          "makes uniformity of the macroscopic properties throughout the sample the "
          "distinguishing feature. Containing more than one substance is what makes it a "
          "mixture rather than a pure substance."),

 dict(q="How many moles of solute are contained in 0.75 L of a 0.40 M solution?",
      choices=[
        "0.30 mol",
        "0.53 mol",
        "1.9 mol",
        "3.0 mol",
        "0.19 mol"],
      ans=0,
      why="EK 3.7.A.2's equation rearranged multiplies the molarity by the litres of "
          "solution, which is the calculation of the number of solute particles that "
          "learning objective 3.7.A names."),

 dict(q="A student dissolves 0.10 mol of solute and dilutes to 500 mL, then transfers the "
        "whole solution to a larger flask and adds water until the volume is 2.00 L. What is "
        "the final molarity?",
      choices=[
        "0.050 M",
        "0.20 M",
        "0.025 M",
        "0.40 M",
        "5.0 M"],
      ans=0,
      why="The whole solution is transferred and only water is added, so all of the original "
          "solute is still present and EK 3.7.A.2's equation is applied once to the final "
          "volume. The concentration the solution had at the intermediate volume is one of "
          "the other values offered."),

 dict(q="Which of these actions changes the molarity of a solution?",
      choices=[
        "Adding more solvent to the solution",
        "Dividing the solution between two beakers",
        "Stirring the solution thoroughly",
        "Pouring the solution into a container of a different shape",
        "Relabelling the container the solution is stored in"],
      ans=0,
      why="EK 3.7.A.2 makes molarity a ratio of moles of solute to litres of solution, so "
          "only a change to one of those two quantities can move it. Dividing a solution or "
          "changing its container changes the amount in each vessel and the shape of the "
          "sample without changing that ratio, since EK 3.7.A.1 makes the properties of a "
          "solution uniform throughout."),

 dict(q="Exactly half of a solution is poured into a second beaker. What happens in that "
        "second beaker compared with the original solution?",
      choices=[
        "The molarity is unchanged and the number of moles of solute is halved",
        "The molarity is halved and the number of moles of solute is unchanged",
        "Both the molarity and the number of moles of solute are halved",
        "Both the molarity and the number of moles of solute are unchanged",
        "The molarity doubles and the number of moles of solute is halved"],
      ans=0,
      why="EK 3.7.A.1 makes the macroscopic properties of a solution the same throughout, so "
          "half the volume carries half the solute and EK 3.7.A.2's ratio of the two is "
          "unmoved. The amount and the concentration are different quantities and only one "
          "of them depends on how much you take."),

 dict(q="How many of the tabulated solutions are more concentrated than 0.15 M?",
      table=_T_SOL,
      choices=[
        "Exactly two",
        "Exactly one",
        "Exactly three",
        "All four",
        "None of them"],
      ans=0,
      why="EK 3.7.A.2's equation is applied to each tabulated row in turn and the resulting "
          "molarities are compared with the stated threshold. Two of the four rows carry "
          "more solute per litre than that and two do not."),

 dict(q="A volume is measured as 250. mL. What is that volume in litres, as the framework's "
        "molarity equation requires?",
      choices=[
        "0.250 L",
        "2.50 L",
        "2500 L",
        "25.0 L",
        "0.0250 L"],
      ans=0,
      why="A litre is a thousand millilitres, so the numerical value is divided by a "
          "thousand and the three significant figures of the measurement are carried "
          "through. Following the conversion carefully is exactly what suggested skill 5.F "
          "asks for."),

 dict(q="The framework says solution composition can be expressed in a variety of ways. What "
        "standing does it give molarity among them?",
      choices=[
        "Molarity is the most common method used in the laboratory",
        "Molarity is the only method by which composition may be expressed",
        "Molality is the most common method used in the laboratory",
        "Percent by mass is the most common method used in the laboratory",
        "The framework ranks none of the methods against the others"],
      ans=0,
      why="EK 3.7.A.2 says composition can be expressed in a variety of ways and then names "
          "molarity as the most common method used in the laboratory. That is a statement "
          "about ordinary practice, not a claim that the other ways do not exist."),

 dict(q="In words, what does the framework's molarity equation say?",
      choices=[
        "Moles of solute divided by litres of solution",
        "Litres of solution divided by moles of solute",
        "Moles of solute divided by litres of solvent",
        "Moles of solute multiplied by litres of solution",
        "Grams of solute divided by litres of solution"],
      ans=0,
      why="EK 3.7.A.2 writes molarity with the moles of solute above the line and the litres "
          "of solution below it. Grams are a mass rather than an amount, and the solvent's "
          "volume is not the solution's volume once the solute has dissolved."),
]
