r"""AP CHEMISTRY 1.8 Valence Electrons and Ionic Compounds.

CED effective Fall 2024, Unit 1 Atomic Structure and Properties.
Learning objective 1.8.A: explain the relationship between trends in the
reactivity of elements and periodicity.
Suggested skill 4.C, explain the connection between particulate-level and
macroscopic properties of a substance using models and representations.

Essential knowledge relied on, in the framework's own words:

  1.8.A.1  The likelihood that two elements will form a chemical bond is
           determined by the interactions between the valence electrons and
           nuclei of elements.
  1.8.A.2  Elements in the same column of the periodic table tend to form
           analogous compounds.
  1.8.A.3  Typical charges of atoms in ionic compounds are governed by the
           number of valence electrons and predicted by their location on the
           periodic table.

ON CHARGE BALANCE. Several items ask for the formula of an ionic compound built
from two predicted ion charges. EK 1.8.A.3 supplies the charges; the step from
two charges to a formula needs one further premise, that the compound carries
no net charge, and the framework's own statement of it is EK 4.2.A.2 -- "mass
and charge are conserved in chemical reactions". Every such claim cites both
codes rather than treating neutrality as too obvious to source.

ON THE WORD "TYPICAL". EK 1.8.A.3 says TYPICAL charges, and this module keeps
that hedge: no item claims an element can form only one charge, and the two
columns whose behaviour is genuinely variable -- the transition metals -- are
not used for a charge prediction anywhere.

HOW THIS TOPIC IS KEPT DISTINCT FROM 1.7. Topic 1.7 is the trend in a property
across the table. Here the property is put to work: which ion an element forms,
which compounds it forms, and how readily it reacts. Item 17 is the one place
the two touch, and it is deliberately built on a DIFFERENT column and a
different question from either of 1.7's ionization-energy items -- 1.7 asks
what the trend IS, this asks what the trend PREDICTS about reactivity, which is
what LO 1.8.A names and LO 1.7.A does not.

NOTATION. Formulas stay plain text in prose (MgCl2, Al2O3), and ion charges are
written in words ("a charge of plus two") rather than as bare superscripts,
which would print literally outside a math span.
"""
TOPIC = ("1.8", "Valence Electrons and Ionic Compounds", 1)

_T_TYPICAL = dict(
    headers=["Column of the periodic table",
             "Typical charge of the ion formed in an ionic compound"],
    rows=[["Column 1", "+1"], ["Column 2", "+2"], ["Column 13", "+3"],
          ["Column 16", "-2"], ["Column 17", "-1"]])

_T_VALENCE = dict(
    headers=["Element", "Column of the periodic table", "Valence electrons"],
    rows=[["Sodium", "1", "1"], ["Magnesium", "2", "2"], ["Aluminum", "13", "3"],
          ["Sulfur", "16", "6"], ["Chlorine", "17", "7"]])

_T_ANALOG = dict(
    headers=["Element", "Column of the periodic table",
             "Formula of its compound with chlorine"],
    rows=[["Lithium", "1", "LiCl"], ["Sodium", "1", "NaCl"],
          ["Potassium", "1", "KCl"], ["Magnesium", "2", "MgCl2"],
          ["Calcium", "2", "CaCl2"]])

_T_OXIDES = dict(
    headers=["Element", "Column of the periodic table",
             "Formula of its compound with oxygen"],
    rows=[["Lithium", "1", "Li2O"], ["Sodium", "1", "Na2O"],
          ["Magnesium", "2", "MgO"], ["Calcium", "2", "CaO"]])

_T_IE_COL2 = dict(
    headers=["Element (second column, top to bottom)",
             "First ionization energy (kilojoules per mole)"],
    rows=[["Beryllium", "900"], ["Magnesium", "738"], ["Calcium", "590"],
          ["Strontium", "549"]])

_T_FORMULAS = dict(
    headers=["Proposed compound", "Formula proposed",
             "Column of the metal", "Column of the nonmetal"],
    rows=[["Compound 1", "NaCl", "1", "17"], ["Compound 2", "MgO", "2", "16"],
          ["Compound 3", "KO", "1", "16"], ["Compound 4", "CaBr2", "2", "17"]])

QUESTIONS = [

 dict(q="According to the framework, what determines the likelihood that two elements "
        "will form a chemical bond with each other?",
      choices=[
        "The interactions between the valence electrons and the nuclei of the two "
        "elements.",
        "The relative masses of the two elements, since heavier atoms bond more readily.",
        "The number of neutrons each nucleus contains.",
        "Whether the two elements were discovered in the same century.",
        "The number of core electrons the two elements have in common."],
      ans=0,
      why="EK 1.8.A.1, near verbatim: the likelihood that two elements will form a "
          "chemical bond is determined by the interactions between the valence "
          "electrons and nuclei of elements. Mass and neutron count play no part in "
          "that statement."),

 dict(q="Two elements lie in the same column of the periodic table. What does the "
        "framework say about the compounds they form?",
      choices=[
        "They tend to form analogous compounds, with the same kind of formula.",
        "They tend to form compounds with each other rather than with other elements.",
        "They tend to form compounds of identical mass.",
        "They tend to form no compounds at all, because their properties are "
        "duplicated.",
        "They tend to form compounds whose formulas are unrelated, because their masses "
        "differ."],
      ans=0,
      why="EK 1.8.A.2, near verbatim: elements in the same column of the periodic table "
          "tend to form analogous compounds. Analogous means the same pattern of "
          "formula, which is a statement about composition rather than about mass."),

 dict(q="An element in the first column of the periodic table forms an ion in an ionic "
        "compound. What is its typical charge, and what governs it?",
      table=_T_TYPICAL,
      choices=[
        "A charge of plus one, governed by its single valence electron.",
        "A charge of minus one, governed by its single valence electron.",
        "A charge of plus one, governed by its single core electron.",
        "A charge of plus seven, governed by the number of protons in its nucleus.",
        "A charge that cannot be predicted, since charge depends on the other element "
        "in the compound."],
      ans=0,
      why="EK 1.8.A.3 states that typical charges of atoms in ionic compounds are "
          "governed by the number of valence electrons and predicted by location on the "
          "periodic table, and the tabulated charge for this column is the positive one. "
          "Core electrons are the inner electrons under EK 1.5.A.3 and are not what is "
          "lost."),

 dict(q="Using the tabulated typical charges, what is the charge of the ion an element "
        "of the sixteenth column forms in an ionic compound?",
      table=_T_TYPICAL,
      choices=["A charge of minus two", "A charge of plus two",
               "A charge of minus six", "A charge of plus six",
               "A charge of minus one"],
      ans=0,
      why="EK 1.8.A.3 makes the typical charge predictable from position, and the table "
          "records it for this column directly. An element of this column has six "
          "valence electrons and reaches a filled outer subshell by gaining two rather "
          "than by losing six."),

 dict(q="The table lists the number of valence electrons for five elements. Which "
        "element would be expected to form an ion carrying a charge of plus three?",
      table=_T_VALENCE,
      choices=["Aluminum", "Sodium", "Magnesium", "Sulfur", "Chlorine"],
      ans=0,
      why="EK 1.8.A.3 makes the typical charge governed by the number of valence "
          "electrons, so an element that loses all three of its valence electrons is "
          "left with a charge of plus three. The tabulated valence counts fix which "
          "element that is."),

 dict(q="A metal from the second column of the periodic table combines with a nonmetal "
        "from the seventeenth column. Using the tabulated typical charges, what is the "
        "formula of the ionic compound, written with the metal first?",
      table=_T_TYPICAL,
      choices=["One metal atom to two nonmetal atoms", "One metal atom to one nonmetal "
               "atom", "Two metal atoms to one nonmetal atom",
               "Two metal atoms to three nonmetal atoms",
               "One metal atom to three nonmetal atoms"],
      ans=0,
      why="EK 1.8.A.3 supplies the two charges from position in the table, and EK "
          "4.2.A.2's conservation of charge requires the compound to carry no net "
          "charge, so one ion of charge plus two needs two ions of charge minus one to "
          "balance it."),

 dict(q="Sodium forms the compound NaBr with bromine. Using periodicity, what compound "
        "would potassium, which lies directly below sodium, be expected to form with "
        "bromine?",
      choices=["KBr, one potassium ion for each bromide ion",
               "KBr2, one potassium ion for every two bromide ions",
               "K2Br, two potassium ions for each bromide ion",
               "K3Br, three potassium ions for each bromide ion",
               "KBr3, one potassium ion for every three bromide ions"],
      ans=0,
      why="EK 1.8.A.2 states that elements in the same column tend to form analogous "
          "compounds, so an element directly below another should form a compound of "
          "the same pattern with the same partner. EK 1.8.A.3 agrees, since both "
          "elements have the same number of valence electrons and so the same typical "
          "charge."),

 dict(q="Why can the typical charge of an atom in an ionic compound be predicted from "
        "the element's location on the periodic table?",
      choices=[
        "Because location fixes the number of valence electrons, and the typical charge "
        "is governed by that number.",
        "Because location fixes the number of neutrons, and neutrons set the charge.",
        "Because location fixes the atomic mass, and heavier atoms carry larger charges.",
        "Because location fixes the number of core electrons, which are the electrons "
        "transferred.",
        "Because charges were assigned to the columns by convention when the table was "
        "drawn up."],
      ans=0,
      why="EK 1.8.A.3 states that typical charges are governed by the number of valence "
          "electrons and predicted by location on the periodic table, and EK 1.7.A.1 "
          "supplies the link between the two by tracing the columns to repeating "
          "ground-state configurations. Core electrons are the inner ones under EK "
          "1.5.A.3."),

 dict(q="Aluminum lies in the thirteenth column and oxygen in the sixteenth. Using the "
        "tabulated typical charges, what is the formula of the ionic compound they "
        "form?",
      table=_T_TYPICAL,
      choices=["Al2O3", "Al3O2", "AlO", "Al2O5", "Al4O5"],
      ans=0,
      why="EK 1.8.A.3 gives the charges as plus three and minus two from the tabulated "
          "columns, and EK 4.2.A.2's conservation of charge requires them to balance, "
          "which two of the first and three of the second do. Reversing the two "
          "subscripts gives one of the rejected formulas."),

 dict(q="Which pairing of elements is most likely to produce an ionic compound, "
        "according to the way the framework describes bond formation?",
      table=_T_VALENCE,
      choices=[
        "An element with one valence electron together with an element with seven "
        "valence electrons.",
        "Two elements that each have one valence electron.",
        "Two elements that each have seven valence electrons.",
        "An element with one valence electron together with an element that has the "
        "same number of core electrons.",
        "Two elements chosen so that their nuclei have the same number of neutrons."],
      ans=0,
      why="EK 1.8.A.1 makes the likelihood of a bond depend on the interactions between "
          "the valence electrons and nuclei of the two elements, and EK 1.8.A.3 ties the "
          "typical ionic charges to those valence counts. One element that readily gives "
          "up a single electron and one that readily takes a single electron is the "
          "pairing those two statements favor."),

 dict(q="The table gives the formulas of the chlorine compounds of five elements. "
        "Rubidium lies directly below potassium in the first column. What formula would "
        "you expect for its compound with chlorine?",
      table=_T_ANALOG,
      choices=["RbCl, one rubidium ion for each chloride ion",
               "RbCl2, one rubidium ion for every two chloride ions",
               "Rb2Cl, two rubidium ions for each chloride ion",
               "Rb3Cl, three rubidium ions for each chloride ion",
               "RbCl3, one rubidium ion for every three chloride ions"],
      ans=0,
      why="EK 1.8.A.2 states that elements in the same column tend to form analogous "
          "compounds, and every tabulated element of that column forms a compound of the "
          "same one-to-one pattern with chlorine. The tabulated second-column elements "
          "form a different pattern, which is why the column matters."),

 dict(q="Using the same table, what feature of the data most directly supports the claim "
        "that elements of one column form analogous compounds?",
      table=_T_ANALOG,
      choices=[
        "Every element of the first column forms a one-to-one compound with chlorine, "
        "while every element of the second column forms a one-to-two compound.",
        "Every element in the table forms a compound with chlorine, whatever its column.",
        "The formulas contain different numbers of atoms in every case.",
        "The elements of the first column form compounds with more chlorine atoms than "
        "the elements of the second column do.",
        "Each element forms a compound whose mass matches that of the others in its "
        "column."],
      ans=0,
      why="EK 1.8.A.2's claim is about the PATTERN of a formula recurring within a "
          "column, so the support is that the pattern is constant inside each column and "
          "differs between them. That every element forms some compound with chlorine is "
          "true of the whole table and so distinguishes nothing."),

 dict(q="The table gives the formulas of the oxygen compounds of four elements. Which "
        "statement is best supported?",
      table=_T_OXIDES,
      choices=[
        "The first-column elements need two atoms for each oxygen atom, while the "
        "second-column elements need only one, which matches their typical ionic charges.",
        "The first-column elements need one atom for each oxygen atom, and the "
        "second-column elements need two.",
        "All four elements form compounds of the same pattern with oxygen.",
        "The pattern of the formula depends on the mass of the element rather than on "
        "its column.",
        "No pattern can be drawn, because four elements are too few."],
      ans=0,
      why="The tabulated formulas differ by column and agree within a column, which is "
          "what EK 1.8.A.2 predicts, and EK 1.8.A.3 supplies the reason: an ion of "
          "charge plus one needs two of itself to balance a charge of minus two, while "
          "an ion of charge plus two balances it alone."),

 dict(q="An element has seven valence electrons. What charge does it typically carry in "
        "an ionic compound, and why?",
      choices=[
        "A charge of minus one, because gaining a single electron completes its outer "
        "subshell.",
        "A charge of plus seven, because it loses all seven valence electrons.",
        "A charge of minus seven, because it gains seven more electrons.",
        "A charge of plus one, because it loses a single valence electron.",
        "No charge at all, because seven is an odd number of electrons."],
      ans=0,
      why="EK 1.8.A.3 makes the typical charge governed by the number of valence "
          "electrons, and EK 1.7.A.1 makes a completely filled shell or subshell the "
          "recurring feature that the pattern of configurations produces. Gaining one "
          "electron is a far smaller change than losing seven."),

 dict(q="The table lists the first ionization energies of the elements of the second "
        "column of the periodic table. Which element would be expected to lose its "
        "valence electrons most readily, and what does that imply about its reactivity "
        "as a metal?",
      table=_T_IE_COL2,
      choices=[
        "Strontium, and it should be the most reactive of the four as a metal.",
        "Beryllium, and it should be the most reactive of the four as a metal.",
        "Strontium, and it should be the least reactive of the four as a metal.",
        "Beryllium, and it should be the least reactive of the four, though it loses its "
        "electrons most readily.",
        "All four are equally reactive, since all four have two valence electrons."],
      ans=0,
      why="The tabulated ionization energies fall down the column, so the last element "
          "gives up its valence electrons for the least energy. LO 1.8.A concerns the "
          "relationship between reactivity and periodicity, and EK 1.8.A.1 makes bond "
          "formation depend on the interaction between valence electrons and nuclei, "
          "which is exactly what ionization energy measures."),

 dict(q="Which of the following formulas is inconsistent with the typical ionic charges "
        "predicted from the columns given?",
      table=_T_FORMULAS,
      choices=["Compound 3", "Compound 1", "Compound 2", "Compound 4",
               "All four are consistent with the typical charges"],
      ans=0,
      why="EK 1.8.A.3 fixes each ion's typical charge from its column, and EK 4.2.A.2 "
          "requires the compound to carry no net charge. Three of the tabulated "
          "formulas balance on those charges and one does not, since an ion of charge "
          "plus one cannot balance an ion of charge minus two on its own."),

 dict(q="Two elements of the first column of the periodic table are compared. Which "
        "statement about their chemistry follows from periodicity?",
      choices=[
        "Both form ions of the same charge and compounds of the same pattern, because "
        "both have the same number of valence electrons.",
        "They form ions of different charges, because their nuclei contain different "
        "numbers of protons.",
        "They form compounds of the same pattern only if their masses are similar.",
        "They form ions of opposite charge, since one lies above the other.",
        "Nothing can be said, since the two elements are different substances."],
      ans=0,
      why="EK 1.8.A.2 states that elements in the same column tend to form analogous "
          "compounds, and EK 1.8.A.3 traces the typical charge to the number of valence "
          "electrons, which EK 1.7.A.1's repeating configurations make identical down a "
          "column. Differing proton counts change how tightly the electrons are held, "
          "not how many there are."),

 dict(q="Magnesium forms the compound MgS with sulfur. Which element would be expected "
        "to form a compound of the same pattern with sulfur?",
      table=_T_ANALOG,
      choices=["Calcium, which lies in the same column as magnesium",
               "Sodium, which lies one column to the left of magnesium",
               "Aluminum, which lies to the right of magnesium",
               "Chlorine, which is a nonmetal like sulfur",
               "No other element, since each compound is unique to its elements"],
      ans=0,
      why="EK 1.8.A.2 makes elements of one COLUMN the ones that form analogous "
          "compounds, so the element to look for is the one sharing magnesium's column "
          "in the table. Sharing a row, or being a nonmetal like the partner, is a "
          "different relationship entirely."),

 dict(q="An atom of an element in the second column loses both its valence electrons. "
        "What is the charge of the resulting ion, and how does its electron count "
        "compare with that of the neutral atom?",
      choices=[
        "A charge of plus two, with two fewer electrons than the neutral atom.",
        "A charge of minus two, with two more electrons than the neutral atom.",
        "A charge of plus two, with two more electrons than the neutral atom.",
        "A charge of plus two, with two fewer protons than the neutral atom.",
        "No charge, because losing electrons removes charge from the atom."],
      ans=0,
      why="EK 1.5.A.1 gives the electron a negative charge, so removing two leaves a net "
          "charge of plus two, and EK 1.8.A.3 makes that the typical charge for an "
          "element of this column. Losing electrons cannot change the number of protons, "
          "which sit in the nucleus."),

 dict(q="Why is it useful to know an element's column when predicting the formula of an "
        "ionic compound it forms, rather than knowing its atomic mass?",
      choices=[
        "Because the column determines the number of valence electrons, and the typical "
        "ionic charge is governed by that number rather than by mass.",
        "Because the column determines the number of neutrons, which sets the charge.",
        "Because the atomic mass is different for every sample of an element.",
        "Because atomic mass has no measurable value for most elements.",
        "Because the column determines the number of core electrons, which are the ones "
        "transferred in an ionic compound."],
      ans=0,
      why="EK 1.8.A.3 states that typical charges are governed by the number of valence "
          "electrons and predicted by location on the periodic table, and EK 1.7.A.1 "
          "makes a column a repeating configuration pattern. Atomic mass is a real, "
          "measurable quantity that simply does not enter the prediction."),

 dict(q="A student proposes that the compound formed between an element of the first "
        "column and an element of the sixteenth column should have a one-to-one formula. "
        "Using the tabulated typical charges, evaluate the proposal.",
      table=_T_TYPICAL,
      choices=[
        "It is wrong, because one ion of charge plus one cannot balance one ion of "
        "charge minus two; two of the first are needed.",
        "It is wrong, because one ion of charge plus two cannot balance one ion of "
        "charge minus one.",
        "It is right, because every ionic compound has a one-to-one formula.",
        "It is right, because the two columns are on opposite sides of the table.",
        "It cannot be evaluated, because typical charges apply only to metals."],
      ans=0,
      why="EK 1.8.A.3 supplies the two charges from the tabulated columns and EK 4.2.A.2 "
          "requires the compound to be electrically balanced, so the numbers of the two "
          "ions must be in the inverse ratio of their charges. The framework assigns "
          "typical charges to nonmetals as readily as to metals."),

 dict(q="How does the number of valence electrons an atom has connect a particulate-level "
        "feature to something that can be observed about a substance?",
      choices=[
        "It sets the typical charge of the ion the atom forms, which fixes the ratio in "
        "which the elements combine and so the formula of the compound that results.",
        "It sets the mass of the atom, which fixes the density of the substance.",
        "It sets the number of neutrons, which fixes the melting point of the substance.",
        "It sets the color of the substance directly, with no intermediate step.",
        "It has no observable consequence, since electrons cannot be seen."],
      ans=0,
      why="Suggested skill 4.C asks for the connection between the particulate level and "
          "what can be observed. EK 1.8.A.3 runs from valence electron count to typical "
          "ionic charge, and EK 4.2.A.2's charge balance then fixes the combining ratio, "
          "which is what an analyst measures as a formula."),

 dict(q="Two elements are described: the first has one valence electron and a low first "
        "ionization energy; the second has seven valence electrons. Which prediction "
        "about the pair follows from the framework?",
      choices=[
        "They are likely to form a compound, with the first supplying an electron to the "
        "second.",
        "They are unlikely to form any compound, because their valence counts differ so "
        "widely.",
        "They are likely to form a compound, with the second supplying an electron to "
        "the first.",
        "They will form a compound only if their nuclei contain the same number of "
        "neutrons.",
        "No prediction is possible without knowing the masses of the two elements."],
      ans=0,
      why="EK 1.8.A.1 makes bond formation depend on the interactions between the "
          "valence electrons and the nuclei of the two elements. A low ionization energy "
          "means the single valence electron is loosely held, and EK 1.8.A.3 makes an "
          "element with seven valence electrons one that typically takes an electron, so "
          "the transfer runs one way and not the other."),

 dict(q="Which observation would count as evidence AGAINST the claim that elements in "
        "one column of the periodic table tend to form analogous compounds?",
      choices=[
        "Two elements of the same column form compounds with chlorine whose formulas "
        "have different combining ratios.",
        "Two elements of the same column form compounds with chlorine whose masses "
        "differ.",
        "Two elements of the same column have different numbers of protons.",
        "Two elements of the same column have different atomic radii.",
        "Two elements of the same column occupy different rows."],
      ans=0,
      why="EK 1.8.A.2's claim is about the pattern of the formula recurring within a "
          "column, so only a difference in that pattern bears on it. Differing masses, "
          "proton counts, radii and rows are all expected of column-mates and are "
          "consistent with the claim rather than against it."),

 dict(q="An element of the seventeenth column and an element of the second column form "
        "an ionic compound. In one formula unit, what is the ratio of the number of "
        "seventeenth-column ions to second-column ions?",
      table=_T_TYPICAL,
      choices=["Two to one", "One to two", "One to one", "Three to one",
               "One to three"],
      ans=0,
      why="EK 1.8.A.3 gives the two tabulated charges as minus one and plus two, and EK "
          "4.2.A.2's charge balance requires the ions to appear in the inverse ratio of "
          "the magnitudes of their charges. Stating the ratio the other way round gives "
          "the nearest rejected option."),

 dict(q="Using the tabulated valence electron counts, which two elements would be "
        "expected to combine in a ratio of one metal ion to two nonmetal ions?",
      table=_T_VALENCE,
      choices=["Magnesium and chlorine", "Sodium and chlorine",
               "Sodium and sulfur", "Aluminum and chlorine",
               "Magnesium and sulfur"],
      ans=0,
      why="EK 1.8.A.3 turns the tabulated valence counts into typical charges, and EK "
          "4.2.A.2's charge balance makes the combining ratio the inverse ratio of the "
          "charge magnitudes. A charge of plus two against a charge of minus one is the "
          "only pairing in the table that gives one to two; two of the rejected pairings "
          "balance one to one and the others give two to one and one to three."),

 dict(q="Why do the elements of the first column become more reactive as metals going "
        "down the column?",
      choices=[
        "Their single valence electron lies farther from the nucleus and is more "
        "shielded, so it is given up more easily.",
        "They gain valence electrons going down the column, so there is more to give up.",
        "Their nuclei contain fewer protons going down the column, so the electron is "
        "held less tightly.",
        "Their atoms become smaller going down the column, which frees the valence "
        "electron.",
        "They are not more reactive going down the column; reactivity is the same "
        "throughout."],
      ans=0,
      why="LO 1.8.A concerns the relationship between reactivity trends and periodicity. "
          "EK 1.7.A.2 explains the fall in ionization energy down a column through "
          "distance and shielding, and EK 1.8.A.1 makes bond formation turn on the "
          "interaction between the valence electrons and the nuclei. Every element of "
          "the column has one valence electron and a growing proton count."),

 dict(q="A newly studied element is found to sit directly below calcium in the second "
        "column of the periodic table. Which prediction about it is best supported?",
      table=_T_ANALOG,
      choices=[
        "It should form a compound with chlorine in a one-to-two ratio, as the other "
        "second-column elements in the table do.",
        "It should form a compound with chlorine in a one-to-one ratio, since it is a "
        "metal.",
        "It should form no compound with chlorine, since it lies below every element "
        "listed.",
        "It should form a compound with chlorine in a two-to-one ratio, since it is "
        "heavier than calcium.",
        "No prediction is possible until the compound has been prepared and analyzed."],
      ans=0,
      why="EK 1.8.A.2 states that elements in the same column tend to form analogous "
          "compounds, and both tabulated members of that column form the same "
          "one-to-two pattern with chlorine. EK 1.7.A.3 separately licenses using "
          "periodicity to predict a property in the absence of data."),

 dict(q="A student says that because an element of the sixteenth column has six valence "
        "electrons, it will typically form an ion of charge plus six. Which evaluation "
        "is correct?",
      table=_T_TYPICAL,
      choices=[
        "The claim is wrong: the tabulated typical charge for that column is negative, "
        "because gaining two electrons is a much smaller change than losing six.",
        "The claim is right: the typical charge equals the number of valence electrons.",
        "The claim is wrong: the tabulated typical charge for that column is plus two.",
        "The claim is wrong, because elements of that column form no ions at all.",
        "The claim cannot be evaluated, because typical charges are not predictable from "
        "position."],
      ans=0,
      why="EK 1.8.A.3 makes the typical charge governed by the valence count and "
          "predicted by location, and the tabulated charge for that column is negative. "
          "EK 1.7.A.1's completely filled shells and subshells are why the small change "
          "is the one that happens."),

 dict(q="An ionic compound is analyzed and found to contain two atoms of a metal for "
        "every three atoms of a nonmetal. Using typical charges, which combination of "
        "columns is consistent with that ratio?",
      table=_T_TYPICAL,
      choices=[
        "A metal of the thirteenth column with a nonmetal of the sixteenth column.",
        "A metal of the first column with a nonmetal of the seventeenth column.",
        "A metal of the second column with a nonmetal of the seventeenth column.",
        "A metal of the first column with a nonmetal of the sixteenth column.",
        "A metal of the second column with a nonmetal of the sixteenth column."],
      ans=0,
      why="EK 1.8.A.3 gives each column its typical charge and EK 4.2.A.2's charge "
          "balance makes the combining ratio the inverse ratio of the charge "
          "magnitudes, so a two-to-three ratio requires charges of magnitude three and "
          "two. Only one of the tabulated pairings supplies those."),
]
