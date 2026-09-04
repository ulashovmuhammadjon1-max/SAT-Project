# AP CHEMISTRY 9.9 Cell Potential and Free Energy
# CED effective Fall 2024, Unit 9 Thermodynamics and Electrochemistry.
# Learning objective 9.9.A: explain whether an electrochemical cell is thermodynamically
# favored, based on its standard cell potential and the constituent half-reactions within
# the cell. Suggested skill 5.F, calculate, estimate, or predict an unknown quantity from
# known quantities by selecting and following a logical computational pathway and attending
# to precision.
#
# Essential knowledge relied on, in the framework's own words:
#   9.9.A.1  Electrochemistry encompasses the study of redox reactions that occur within
#            electrochemical cells. The reactions are either thermodynamically favored
#            (resulting in a positive voltage) or thermodynamically unfavored (resulting in
#            a negative voltage and requiring an externally applied potential for the
#            reaction to proceed).
#   9.9.A.2  The standard cell potential of electrochemical cells can be calculated by
#            identifying the oxidation and reduction half-reactions and their respective
#            standard reduction potentials.
#   9.9.A.3  The standard Gibbs free energy change is proportional to the negative of the
#            cell potential for the redox reaction from which it is constructed. Thus, a
#            cell with a positive standard potential involves a thermodynamically favored
#            reaction, and a cell with a negative standard potential involves a
#            thermodynamically unfavored reaction.
#            EQN: \( \Delta G^\circ = -nFE^\circ \)
#
# Supporting statements used where the framework's own reasoning needs them:
#   EK 9.8.A.3  Oxidation occurs at the anode and reduction at the cathode, which is what
#               lets EK 9.9.A.2's "identify the oxidation and reduction half-reactions" be
#               carried out from a description of the cell.
#   The equation and constant sheet, verbatim: n is the number of moles of electrons and
#   Faraday's constant is 96,485 coulombs per mole of electrons.
#
# THE SIGN IS THE ANSWER IN THIS TOPIC, and it is one character from its opposite. A
# thermodynamically favored cell has a POSITIVE standard cell potential and a NEGATIVE
# standard free energy change; an unfavored cell has both the other way round. Every
# quantitative key below therefore states its value WITH ITS SIGN, every such item offers
# the sign-flipped value as a distractor, and verify_h9_9.py recomputes the arithmetic and
# compares the signed token RAW -- not through a normalizer that drops a leading plus.
#
# THE FIGURE PROBLEM. A cell is normally taught from a drawing and this bank carries no
# images. Every cell below is described in words -- which species is oxidized, which is
# reduced -- or carried as a table of standard reduction potentials, and the question is
# asked of the table. No stem says "shown" or "the diagram", and verify_h9_9.py asserts it.
#
# SCOPE. 9.8 owns the physical components and the naming of the electrodes, so no item here
# turns on which electrode is the anode. 9.10 owns nonstandard conditions, so every
# potential below is a STANDARD one and no item mentions a reaction quotient or the Nernst
# equation. 9.11 owns Faraday's law, so no item computes a charge, a current or a mass; the
# Faraday constant appears here only as the F in the framework's own equation.
#
# NOTATION. export_units.py does not typeset Chemistry. Every span below is hand-written,
# formulas in prose stay plain text, and a signed value in a choice is wrapped in a span so
# that the plus sign survives -- the normalizer used for the containment test drops a bare
# leading plus, which would make "+1.10 V" look contained in "-1.10 V".
TOPIC = ("9.9", "Cell Potential and Free Energy", 9)

_T_SRP = dict(
    headers=["Half-reaction", "Standard reduction potential (V)"],
    rows=[["Ag+ + e- gives Ag(s)", "+0.80"],
          ["Cu2+ + 2 e- gives Cu(s)", "+0.34"],
          ["2 H+ + 2 e- gives H2(g)", "0.00"],
          ["Ni2+ + 2 e- gives Ni(s)", "-0.25"],
          ["Zn2+ + 2 e- gives Zn(s)", "-0.76"],
          ["Mg2+ + 2 e- gives Mg(s)", "-2.37"]])

_T_CELLS = dict(
    headers=["Cell", "Moles of electrons transferred", "Standard cell potential (V)"],
    rows=[["Cell 1", "2", "+1.10"],
          ["Cell 2", "1", "-0.44"],
          ["Cell 3", "2", "+0.46"],
          ["Cell 4", "4", "-0.20"]])

QUESTIONS = [

 dict(q="According to the course framework, what are the two possibilities for a redox "
        "reaction occurring within an electrochemical cell?",
      choices=[
        "It is thermodynamically favored, giving a positive voltage, or thermodynamically "
        "unfavored, giving a negative voltage",
        "It is thermodynamically favored, giving a negative voltage, or thermodynamically "
        "unfavored, giving a positive voltage",
        "It is thermodynamically favored in one direction and equally favored in the other",
        "It gives a positive voltage in a galvanic cell and no voltage in any other cell",
        "It gives a voltage whose sign depends on which electrode the measurement starts "
        "from"],
      ans=0,
      why="EK 9.9.A.1 says the reactions are either thermodynamically favored, resulting in "
          "a positive voltage, or thermodynamically unfavored, resulting in a negative "
          "voltage. The pairing of the sign with the verdict is the statement itself, not a "
          "convention a student may choose."),

 dict(q="What does the framework say a thermodynamically unfavored cell reaction requires "
        "before it will proceed?",
      choices=[
        "An externally applied potential",
        "A higher temperature than the standard one",
        "A larger quantity of the reactants",
        "A catalyst at one of the electrodes",
        "Nothing further, since every cell reaction proceeds on its own"],
      ans=0,
      why="EK 9.9.A.1 attaches to the unfavored case the words requiring an externally "
          "applied potential for the reaction to proceed, and EK 9.8.A.2 makes such a cell "
          "the electrolytic one. Neither more reactant nor a catalyst changes whether a "
          "reaction is favored."),

 dict(q="How does the framework say the standard cell potential of an electrochemical cell "
        "can be calculated?",
      choices=[
        "By identifying the oxidation and reduction half-reactions and their respective "
        "standard reduction potentials",
        "By adding the two standard reduction potentials together",
        "By multiplying each standard reduction potential by the number of electrons it "
        "carries",
        "By measuring the mass lost at one electrode over a known time",
        "By dividing the standard free energy change by the temperature"],
      ans=0,
      why="EK 9.9.A.2 states that the standard cell potential can be calculated by "
          "identifying the oxidation and reduction half-reactions and their respective "
          "standard reduction potentials. The potential of a half-reaction is not weighted "
          "by the number of electrons, which is why n appears in the free energy equation "
          "and not in the potential."),

 dict(q="Which equation does the framework give relating the standard free energy change to "
        "the standard cell potential?",
      choices=[
        "\\( \\Delta G^\\circ = -nFE^\\circ \\)",
        "\\( \\Delta G^\\circ = nFE^\\circ \\)",
        "\\( \\Delta G^\\circ = -RTE^\\circ \\)",
        "\\( \\Delta G^\\circ = -nF\\ln E^\\circ \\)",
        "\\( E^\\circ = -nF\\Delta G^\\circ \\)"],
      ans=0,
      why="EK 9.9.A.3 gives the equation with the negative sign in front, which is what "
          "makes the free energy change proportional to the NEGATIVE of the cell potential. "
          "Dropping that sign would make a favored cell come out with a positive free energy "
          "change, contradicting the same statement's own conclusion."),

 dict(q="A cell is measured to have a positive standard cell potential. What follows about "
        "the reaction?",
      choices=[
        "It is thermodynamically favored, with a negative standard free energy change",
        "It is thermodynamically unfavored, with a negative standard free energy change",
        "It is thermodynamically favored, with a positive standard free energy change",
        "It is thermodynamically unfavored, with a positive standard free energy change",
        "Nothing follows until the number of electrons transferred is known"],
      ans=0,
      why="EK 9.9.A.3 says a cell with a positive standard potential involves a "
          "thermodynamically favored reaction, and its equation carries a negative sign, so "
          "a positive potential gives a free energy change below zero. The number of "
          "electrons scales the size of that change but cannot alter its sign."),

 dict(q="A different cell is measured to have a negative standard cell potential. What "
        "follows about the reaction?",
      choices=[
        "It is thermodynamically unfavored, with a positive standard free energy change",
        "It is thermodynamically favored, with a positive standard free energy change",
        "It is thermodynamically unfavored, with a negative standard free energy change",
        "It is thermodynamically favored, with a negative standard free energy change",
        "Nothing follows, since a potential cannot be negative"],
      ans=0,
      why="EK 9.9.A.3 says a cell with a negative standard potential involves a "
          "thermodynamically unfavored reaction, and the negative sign in its equation turns "
          "a negative potential into a free energy change above zero. EK 9.9.A.1 adds that "
          "such a reaction needs an externally applied potential."),

 dict(q="A cell is built from a zinc electrode in zinc nitrate solution and a copper "
        "electrode in copper(II) nitrate solution, joined by a salt bridge, and zinc is "
        "oxidized while copper(II) ion is reduced. Using the table, what is the standard "
        "cell potential?",
      table=_T_SRP,
      choices=["\\( +1.10 \\) V", "\\( -1.10 \\) V", "\\( +0.42 \\) V", "\\( -0.42 \\) V",
               "\\( +1.86 \\) V"],
      ans=0,
      why="EK 9.9.A.2 says to identify the oxidation and reduction half-reactions and their "
          "respective standard reduction potentials. The reduced species supplies the "
          "cathode potential and the oxidized species the anode potential, and the standard "
          "cell potential is the first less the second. Adding the two tabulated values "
          "instead of subtracting them is what produces the other magnitude offered."),

 dict(q="Another cell is assembled in which copper metal is oxidized and silver ion is "
        "reduced. Using the same table, what is the standard cell potential?",
      table=_T_SRP,
      choices=["\\( +0.46 \\) V", "\\( -0.46 \\) V", "\\( +1.14 \\) V", "\\( -1.14 \\) V",
               "\\( +0.23 \\) V"],
      ans=0,
      why="EK 9.9.A.2's procedure again: the tabulated reduction potential of the species "
          "that is reduced, less the tabulated reduction potential of the species that is "
          "oxidized. Halving the result for the one electron of the silver half-reaction is "
          "the error the smallest value represents; a potential is not divided by n."),

 dict(q="A third cell is assembled in which magnesium metal is oxidized and nickel(II) ion "
        "is reduced. Using the same table, what is the standard cell potential?",
      table=_T_SRP,
      choices=["\\( +2.12 \\) V", "\\( -2.12 \\) V", "\\( +2.62 \\) V", "\\( -2.62 \\) V",
               "\\( +1.06 \\) V"],
      ans=0,
      why="EK 9.9.A.2 fixes the arithmetic: the tabulated potential of the reduced species "
          "less that of the oxidized one. Adding the two tabulated magnitudes rather than "
          "subtracting the signed values is what gives the larger of the two magnitudes "
          "offered here."),

 dict(q="Of all the cells that could be assembled from the tabulated half-reactions, which "
        "pairing gives the largest standard cell potential?",
      table=_T_SRP,
      choices=[
        "Magnesium is oxidized and silver ion is reduced",
        "Silver is oxidized and magnesium ion is reduced",
        "Zinc is oxidized and silver ion is reduced",
        "Magnesium is oxidized and zinc ion is reduced",
        "Magnesium is oxidized and hydrogen ion is reduced"],
      ans=0,
      why="EK 9.9.A.2 makes the standard cell potential the reduction potential of the "
          "cathode less that of the anode, so it is largest when the species reduced has the "
          "highest tabulated potential and the species oxidized the lowest. Reversing that "
          "pairing gives the most negative potential rather than the largest."),

 dict(q="A cell is set up so that copper metal is oxidized and zinc ion is reduced. Using "
        "the same table, what is the standard cell potential, and what follows?",
      table=_T_SRP,
      choices=[
        "\\( -1.10 \\) V, so the reaction is thermodynamically unfavored",
        "\\( +1.10 \\) V, so the reaction is thermodynamically favored",
        "\\( -0.42 \\) V, so the reaction is thermodynamically unfavored",
        "\\( +0.42 \\) V, so the reaction is thermodynamically favored",
        "\\( -2.20 \\) V, so the reaction is thermodynamically unfavored"],
      ans=0,
      why="Running the cell of the first calculation backwards exchanges which tabulated "
          "potential is subtracted from which, so EK 9.9.A.2's arithmetic returns the same "
          "magnitude with the opposite sign. EK 9.9.A.3 then makes a negative standard "
          "potential the mark of a thermodynamically unfavored reaction, which EK 9.9.A.1 "
          "says needs an externally applied potential."),

 dict(q="A cell has a standard cell potential of +1.10 V and transfers 2 moles of electrons "
        "for each mole of reaction. Taking Faraday's constant as 96,485 coulombs per mole of "
        "electrons, what is the standard free energy change?",
      choices=[
        "\\( -212 \\) kJ/mol, thermodynamically favored",
        "\\( +212 \\) kJ/mol, thermodynamically unfavored",
        "\\( -106 \\) kJ/mol, thermodynamically favored",
        "\\( -424 \\) kJ/mol, thermodynamically favored",
        "Zero, since the cell is at standard conditions"],
      ans=0,
      why="EK 9.9.A.3's equation multiplies the moles of electrons, Faraday's constant and "
          "the standard cell potential, and puts a negative sign in front. A positive "
          "potential therefore gives a free energy change below zero, which is the "
          "thermodynamically favored case the same statement names. Omitting the factor of "
          "n halves the magnitude."),

 dict(q="A silver cell transfers 1 mole of electrons for each mole of reaction and has a "
        "standard cell potential of +0.80 V. What is its standard free energy change?",
      choices=[
        "\\( -77.2 \\) kJ/mol, thermodynamically favored",
        "\\( +77.2 \\) kJ/mol, thermodynamically unfavored",
        "\\( -154 \\) kJ/mol, thermodynamically favored",
        "\\( -38.6 \\) kJ/mol, thermodynamically favored",
        "Zero, since only one mole of electrons is transferred"],
      ans=0,
      why="EK 9.9.A.3's equation with one mole of electrons gives Faraday's constant times "
          "the potential, with the negative sign in front. Using two moles of electrons "
          "where the reaction transfers one is the error behind the doubled magnitude, and "
          "the sign follows from the equation rather than from the size of n."),

 dict(q="An electrolytic process has a standard cell potential of -0.50 V and transfers 2 "
        "moles of electrons for each mole of reaction. What is its standard free energy "
        "change?",
      choices=[
        "\\( +96.5 \\) kJ/mol, thermodynamically unfavored",
        "\\( -96.5 \\) kJ/mol, thermodynamically favored",
        "\\( +193 \\) kJ/mol, thermodynamically unfavored",
        "\\( +48.2 \\) kJ/mol, thermodynamically unfavored",
        "Zero, since the potential is negative"],
      ans=0,
      why="The negative sign in EK 9.9.A.3's equation turns a negative standard potential "
          "into a positive standard free energy change, which is exactly the "
          "thermodynamically unfavored case that statement names and EK 9.9.A.1 says needs "
          "an externally applied potential."),

 dict(q="A fuel-cell reaction transfers 4 moles of electrons for each mole of reaction and "
        "has a standard cell potential of +0.40 V. What is its standard free energy change?",
      choices=[
        "\\( -154 \\) kJ/mol, thermodynamically favored",
        "\\( +154 \\) kJ/mol, thermodynamically unfavored",
        "\\( -38.6 \\) kJ/mol, thermodynamically favored",
        "\\( -617 \\) kJ/mol, thermodynamically favored",
        "Zero, since the potential is below one volt"],
      ans=0,
      why="EK 9.9.A.3's equation scales with the moles of electrons as well as the "
          "potential, so four moles of electrons at a modest potential still give a large "
          "negative change. Dividing by n instead of multiplying by it produces the smallest "
          "magnitude offered."),

 dict(q="A reaction has a standard free energy change of -193 kJ/mol and transfers 2 moles "
        "of electrons for each mole of reaction. What is its standard cell potential?",
      choices=[
        "\\( +1.00 \\) V, so the cell is thermodynamically favored",
        "\\( -1.00 \\) V, so the cell is thermodynamically unfavored",
        "\\( +2.00 \\) V, so the cell is thermodynamically favored",
        "\\( +0.50 \\) V, so the cell is thermodynamically favored",
        "\\( -2.00 \\) V, so the cell is thermodynamically unfavored"],
      ans=0,
      why="Rearranging EK 9.9.A.3's equation divides the free energy change by the moles of "
          "electrons and by Faraday's constant and changes the sign, so a negative free "
          "energy change gives a positive potential. Forgetting to divide by the moles of "
          "electrons doubles the answer."),

 dict(q="Another reaction has a standard free energy change of +96.5 kJ/mol and transfers 1 "
        "mole of electrons for each mole of reaction. What is its standard cell potential?",
      choices=[
        "\\( -1.00 \\) V, so the cell is thermodynamically unfavored",
        "\\( +1.00 \\) V, so the cell is thermodynamically favored",
        "\\( -0.50 \\) V, so the cell is thermodynamically unfavored",
        "\\( -2.00 \\) V, so the cell is thermodynamically unfavored",
        "\\( +0.50 \\) V, so the cell is thermodynamically favored"],
      ans=0,
      why="The same rearrangement of EK 9.9.A.3's equation carries the sign the other way: a "
          "free energy change above zero gives a potential below zero. EK 9.9.A.1 then "
          "requires an externally applied potential before this reaction will proceed."),

 dict(q="A cell whose standard cell potential is +1.10 V has a standard free energy change "
        "of -212 kJ/mol. How many moles of electrons does the reaction transfer?",
      choices=["2 moles of electrons", "1 mole of electrons", "3 moles of electrons",
               "4 moles of electrons", "6 moles of electrons"],
      ans=0,
      why="EK 9.9.A.3's equation contains only n, Faraday's constant and the potential, so "
          "knowing the free energy change and the potential fixes n. Dividing the magnitude "
          "of the free energy change by the product of Faraday's constant and the potential "
          "returns a whole number of moles of electrons."),

 dict(q="Two cells each have a standard cell potential of +0.50 V, but the first transfers 2 "
        "moles of electrons for each mole of reaction while the second transfers 4 moles of "
        "electrons. What is the standard free energy change of the second cell?",
      choices=[
        "\\( -193 \\) kJ/mol, twice as large in magnitude as the first cell's",
        "\\( +193 \\) kJ/mol, twice as large in magnitude as the first cell's",
        "\\( -96.5 \\) kJ/mol, the same as the first cell's",
        "\\( -386 \\) kJ/mol, four times as large in magnitude as the first cell's",
        "Zero, since the two cells have the same potential"],
      ans=0,
      why="EK 9.9.A.3's equation is proportional to the moles of electrons as well as to the "
          "potential, so doubling n at a fixed potential doubles the magnitude of the free "
          "energy change while leaving its sign alone. Equal potentials do not imply equal "
          "free energy changes, which is why the framework states the relationship as a "
          "proportionality rather than an identity."),

 dict(q="What does the framework mean by saying the standard free energy change is "
        "proportional to the NEGATIVE of the cell potential?",
      choices=[
        "The two quantities always carry opposite signs, and the size of one fixes the size "
        "of the other",
        "The two quantities always carry the same sign, and the size of one fixes the size "
        "of the other",
        "The free energy change is the cell potential subtracted from zero, in the same "
        "units",
        "The free energy change falls as the cell potential falls",
        "The free energy change is unrelated to the cell potential unless the cell is "
        "galvanic"],
      ans=0,
      why="EK 9.9.A.3 puts a negative sign in front of a product of positive quantities, so "
          "the free energy change and the potential can never share a sign. That is exactly "
          "why the same statement can conclude that a positive potential marks a favored "
          "reaction and a negative potential an unfavored one."),

 dict(q="The table gives the moles of electrons transferred and the standard cell potential "
        "for four cells. Which of them are thermodynamically favored?",
      table=_T_CELLS,
      choices=["Cells 1 and 3", "Cells 2 and 4", "Cells 1 and 2", "Cells 3 and 4",
               "All four cells"],
      ans=0,
      why="EK 9.9.A.3 makes a cell with a positive standard potential thermodynamically "
          "favored, and exactly two of the tabulated potentials are above zero. The moles of "
          "electrons scale the free energy change but have no bearing on which side of zero "
          "it falls."),

 dict(q="Using the same four cells, which of them require an externally applied potential "
        "before their reactions will proceed?",
      table=_T_CELLS,
      choices=["Cells 2 and 4", "Cells 1 and 3", "Cells 1 and 4", "Cells 2 and 3",
               "None of the four"],
      ans=0,
      why="EK 9.9.A.1 attaches the requirement of an externally applied potential to the "
          "thermodynamically unfavored case, which EK 9.9.A.3 identifies by a negative "
          "standard cell potential. Exactly two of the tabulated potentials are below zero."),

 dict(q="Among the same four cells, which has the most negative standard free energy change?",
      table=_T_CELLS,
      choices=["Cell 1", "Cell 3", "Cell 2", "Cell 4", "Cells 1 and 3 equally"],
      ans=0,
      why="EK 9.9.A.3's equation makes the magnitude the product of the moles of electrons, "
          "Faraday's constant and the potential, so the comparison is settled by the product "
          "of the two tabulated columns rather than by the potential alone. One tabulated "
          "row gives the largest such product among the cells with a positive potential."),

 dict(q="What is the standard free energy change of cell 3 in the table?",
      table=_T_CELLS,
      choices=[
        "\\( -88.8 \\) kJ/mol, thermodynamically favored",
        "\\( +88.8 \\) kJ/mol, thermodynamically unfavored",
        "\\( -44.4 \\) kJ/mol, thermodynamically favored",
        "\\( -178 \\) kJ/mol, thermodynamically favored",
        "Zero, since the potential is below half a volt"],
      ans=0,
      why="EK 9.9.A.3's equation applied to that row's tabulated moles of electrons and "
          "tabulated potential, with the negative sign in front. Reading the row for a "
          "single mole of electrons instead of the tabulated number halves the magnitude."),

 dict(q="A cell is found to have a standard cell potential of exactly zero. What is its "
        "standard free energy change?",
      choices=[
        "Zero, since the equation multiplies the potential by the other factors",
        "Zero, since every standard free energy change is zero at standard conditions",
        "Negative, since the reaction is still favored",
        "Positive, since the reaction is still unfavored",
        "It cannot be found without the number of moles of electrons"],
      ans=0,
      why="EK 9.9.A.3's equation is a product in which the potential is one factor, so a "
          "potential of zero makes the whole expression zero whatever the moles of electrons "
          "are. The framework's two named cases are a positive potential and a negative one, "
          "so this cell is neither favored nor unfavored."),

 dict(q="Two cells are compared, one with a standard cell potential of +0.20 V and one with "
        "+1.50 V. What can be said about them?",
      choices=[
        "Both are thermodynamically favored, and the second has the more negative free "
        "energy change for a given number of electrons",
        "Both are thermodynamically favored, and the first has the more negative free energy "
        "change for a given number of electrons",
        "Only the second is thermodynamically favored, since the first potential is small",
        "Only the first is thermodynamically favored, since a small potential is more easily "
        "reached",
        "Neither can be judged without knowing which electrode is the anode"],
      ans=0,
      why="EK 9.9.A.3 makes any positive standard potential the mark of a thermodynamically "
          "favored reaction, with no threshold attached, and its equation makes the free "
          "energy change more negative as the potential grows at fixed n. Size is a separate "
          "question from sign."),

 dict(q="What role does n play in the framework's equation for the standard free energy "
        "change?",
      choices=[
        "It is the number of moles of electrons transferred in the reaction",
        "It is the number of half-cells in the electrochemical cell",
        "It is the number of moles of the limiting reactant",
        "It is the number of electrons in the valence shell of the metal",
        "It is the number of volts the cell delivers"],
      ans=0,
      why="The framework's equation and constant sheet defines n as the number of moles of "
          "electrons, and EK 9.9.A.3 uses it as the factor by which the free energy change "
          "exceeds Faraday's constant times the potential. It is not a property of the "
          "apparatus or of the metal."),

 dict(q="What quantity does Faraday's constant carry in the framework's equation?",
      choices=[
        "The charge on one mole of electrons, 96,485 coulombs",
        "The charge on one electron, expressed in coulombs",
        "The energy released per volt of cell potential",
        "The number of electrons in one mole of any substance",
        "The potential of the standard hydrogen half-reaction"],
      ans=0,
      why="The framework's equation and constant sheet gives Faraday's constant as 96,485 "
          "coulombs per one mole of electrons, which is what turns the moles of electrons in "
          "EK 9.9.A.3's equation into a charge, and that charge times a potential into an "
          "energy."),

 dict(q="A student is asked to judge whether a cell is thermodynamically favored and is "
        "given only the two half-reactions and their standard reduction potentials. Is that "
        "enough?",
      choices=[
        "Yes, because the standard cell potential follows from them and its sign settles the "
        "question",
        "No, because the number of moles of electrons must also be known",
        "No, because the free energy change must be measured separately",
        "Yes, but only if the two potentials are both positive",
        "No, because the temperature must also be known"],
      ans=0,
      why="EK 9.9.A.2 says the standard cell potential is calculated from the half-reactions "
          "and their respective standard reduction potentials, and EK 9.9.A.3 makes the sign "
          "of that potential decide the favorability. The moles of electrons affect the size "
          "of the free energy change but never its sign, since the other factors are "
          "positive."),

 dict(q="Which set of three statements about one cell is consistent with the framework?",
      choices=[
        "A positive standard cell potential, a negative standard free energy change, and a "
        "thermodynamically favored reaction",
        "A positive standard cell potential, a positive standard free energy change, and a "
        "thermodynamically favored reaction",
        "A negative standard cell potential, a negative standard free energy change, and a "
        "thermodynamically favored reaction",
        "A negative standard cell potential, a positive standard free energy change, and a "
        "thermodynamically favored reaction",
        "A positive standard cell potential, a negative standard free energy change, and a "
        "thermodynamically unfavored reaction"],
      ans=0,
      why="EK 9.9.A.3 ties all three together in one sentence: the free energy change is "
          "proportional to the negative of the cell potential, so a cell with a positive "
          "standard potential involves a thermodynamically favored reaction. Any set that "
          "gives the two quantities the same sign, or attaches the wrong verdict to them, "
          "contradicts that statement."),

]
