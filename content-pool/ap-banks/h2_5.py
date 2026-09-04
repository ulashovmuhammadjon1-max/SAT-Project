r"""AP CHEMISTRY 2.5 Lewis Diagrams.

CED effective Fall 2024, Unit 2 Compound Structure and Properties.
Learning objective 2.5.A: represent a molecule with a Lewis diagram.
Suggested skill 3.B, represent chemical substances or phenomena with
appropriate diagrams or models.

Essential knowledge relied on, in the framework's own words:

  2.5.A.1  Lewis diagrams can be constructed according to an established set of
           principles.

THE PROBLEM WITH THIS TOPIC, STATED PLAINLY. That is the WHOLE essential
knowledge for 2.5 -- one sentence, and it names none of the principles. It
would be easy to fill the gap from a textbook, and SOCIAL_BRIEF.md forbids
exactly that. Two things in the CED itself keep this module honest:

  * Unit 2's own "Preparing for the AP Exam" page (CED p. 41) states what
    students must be able to do and what they get wrong: "students must be
    able to construct Lewis structures and make predictions or claims based on
    them ... Mistakes include: using the incorrect number of valence
    electrons, violating the octet rule". So counting the available valence
    electrons and the octet rule are the framework's own named principles for
    this task, and two items key on exactly those two mistakes.
  * EK 1.5.A.3 defines valence electrons, EK 1.5.A.1 makes an ion's charge the
    imbalance between its electrons and its nucleus, and EK 2.1.A.2 makes a
    bond a SHARED pair of valence electrons. Those three sentences are enough
    to license every count in this module.

So twenty-two of the thirty items are arithmetic: the total number of valence
electrons available to a diagram, or the number of lone pairs left once the
stated bonds have taken their share. verify_h2_5.py recomputes every one of
them from the formula and the bonding written in the item's own stem -- never
from a remembered structure. No key here asserts a principle the CED does not
name.

WHAT IS NOT HERE. Resonance and formal charge are EK 2.6.A.1 and 2.6.A.2 and
belong to topic 2.6; molecular geometry, bond angles and hybridization are EK
2.7.A.2 and 2.7.A.3 and belong to topic 2.7. The verifier asserts that no item
mentions resonance, formal charge or hybridization at all, and that exactly one
item mentions molecular geometry -- item 21, whose key is that a Lewis diagram
by itself does NOT fix the geometry, which is EK 2.7.A.2's own statement that
both must be used.

NO FIGURES. The bank cannot show a Lewis diagram, so every item states the
formula, the overall charge and, where it matters, the bonding in words, and
asks a question that can be answered from that description alone. Nothing here
says "the diagram shown".

NOTATION. Formulas stay plain text (CH4, SO4) and charges are written out as
"an overall charge of 2-". No math spans are needed anywhere in this module.
"""
TOPIC = ("2.5", "Lewis Diagrams", 2)

_T_SPECIES = dict(
    headers=["Species", "Formula", "Overall charge"],
    rows=[["Methane", "CH4", "neutral"],
          ["Carbon dioxide", "CO2", "neutral"],
          ["Nitrate ion", "NO3", "1-"],
          ["Sulfate ion", "SO4", "2-"]])

QUESTIONS = [

 dict(q="What does the framework say about how Lewis diagrams are constructed?",
      choices=[
        "They can be constructed according to an established set of principles",
        "They can be constructed only by measuring a molecule experimentally first",
        "They are constructed differently for every molecule, with no shared rules",
        "They are constructed by writing the electron configuration of each atom in full",
        "They cannot be constructed for any species carrying an overall charge"],
      ans=0,
      why="EK 2.5.A.1, verbatim: Lewis diagrams can be constructed according to an "
          "established set of principles. That the principles are established and shared "
          "is the whole content of the statement, so a claim that each molecule needs its "
          "own rules contradicts it directly."),

 dict(q="Which electrons does a Lewis diagram of a molecule display?",
      choices=[
        "The valence electrons, shown either in bonds between atoms or as lone pairs",
        "Every electron in every atom, core electrons included",
        "Only the electrons that have been transferred from one atom to another",
        "Only the core electrons, since the valence electrons are delocalized",
        "The protons in each nucleus, one dot for each"],
      ans=0,
      why="EK 1.5.A.3 separates core electrons from valence electrons, and EK 2.1.A.2 "
          "describes a covalent bond as valence electrons SHARED between atoms, so a "
          "diagram of the bonding is a diagram of the valence electrons. Nothing in the "
          "framework has a Lewis diagram display a nucleus."),

 dict(q="A Lewis diagram is to be drawn for methane, whose formula is CH4 and which is "
        "neutral overall. How many valence electrons are available to the diagram?",
      choices=["8", "4", "10", "12", "16"],
      ans=0,
      why="EK 1.5.A.3 makes the valence electrons the outer electrons of each atom, and "
          "the periodic table supplies four for carbon and one for each hydrogen. Unit 2's "
          "own list of common mistakes puts using the incorrect number of valence "
          "electrons first, which is why the count is the first step."),

 dict(q="In a Lewis diagram, how many of the available valence electrons does one single "
        "bond between two atoms account for?",
      choices=["Two", "One", "Three", "Four", "Eight"],
      ans=0,
      why="EK 2.1.A.2 describes a covalent bond as valence electrons SHARED between atoms, "
          "and EK 2.2.A.2 treats a single bond as bond order one against a double bond's "
          "order two, so a single bond is one shared pair. A count that treats a bond as "
          "one electron loses half the electrons in the diagram."),

 dict(q="A Lewis diagram is to be drawn for carbon dioxide, whose formula is CO2 and "
        "which is neutral overall. How many valence electrons are available?",
      choices=["16", "12", "18", "20", "22"],
      ans=0,
      why="EK 1.5.A.3 makes the count the sum of the valence electrons of the atoms "
          "present, four for carbon and six for each oxygen from their positions in the "
          "periodic table. Unit 2's own list of mistakes names an incorrect valence "
          "electron count as the first thing to get wrong."),

 dict(q="When a Lewis diagram is drawn for an ion rather than a neutral molecule, how is "
        "the count of available valence electrons adjusted?",
      choices=[
        "One electron is added for each unit of negative charge and one removed for each "
        "unit of positive charge",
        "One electron is removed for each unit of negative charge and one added for each "
        "unit of positive charge",
        "The count is unchanged, since the charge sits on the nucleus rather than on the "
        "electrons",
        "The whole count is multiplied by the size of the charge",
        "One proton is added or removed instead, leaving the electron count alone"],
      ans=0,
      why="EK 1.5.A.1 makes an atom negatively charged electrons around a positively "
          "charged nucleus, so an overall negative charge is a surplus of electrons over "
          "protons and an overall positive charge is a deficit. The nucleus is not what "
          "changes when an ion forms from an atom."),

 dict(q="A Lewis diagram is to be drawn for the nitrate ion, whose formula is NO3 and "
        "which carries an overall charge of 1-. How many valence electrons are available?",
      choices=["24", "23", "22", "26", "18"],
      ans=0,
      why="EK 1.5.A.3 gives five valence electrons for nitrogen and six for each oxygen "
          "from the periodic table, and EK 1.5.A.1 makes a single negative charge one "
          "extra electron. Forgetting to add that electron gives one of the rejected "
          "counts."),

 dict(q="A Lewis diagram is to be drawn for the ammonium ion, whose formula is NH4 and "
        "which carries an overall charge of 1+. How many valence electrons are available?",
      choices=["8", "9", "10", "7", "12"],
      ans=0,
      why="EK 1.5.A.3 gives five valence electrons for nitrogen and one for each hydrogen, "
          "and EK 1.5.A.1 makes a single positive charge one electron fewer than the "
          "neutral collection of atoms would have. Adding an electron instead of removing "
          "one gives a rejected count."),

 dict(q="Unit 2 of the framework lists the mistakes students make when constructing Lewis "
        "structures. Which of the following does it name?",
      choices=[
        "Using the incorrect number of valence electrons",
        "Drawing the atoms in the wrong order of atomic mass",
        "Using the incorrect number of protons",
        "Writing the electron configuration with subscripts rather than superscripts",
        "Failing to state the temperature at which the diagram applies"],
      ans=0,
      why="The framework's own Preparing for the AP Exam page for unit 2 lists the "
          "mistakes in these words: using the incorrect number of valence electrons, "
          "violating the octet rule, or confusing molecular geometry with bond angles. "
          "The count of protons is not something a Lewis diagram displays at all."),

 dict(q="A Lewis diagram is to be drawn for sulfur dioxide, whose formula is SO2 and "
        "which is neutral overall. How many valence electrons are available?",
      choices=["18", "16", "20", "12", "24"],
      ans=0,
      why="EK 1.5.A.3 makes the count the sum over the atoms present, six valence "
          "electrons for sulfur and six for each oxygen from their column of the periodic "
          "table. Counting sulfur as though it were carbon gives one of the rejected "
          "totals."),

 dict(q="In the accepted Lewis diagram for carbon dioxide, whose formula is CO2 and which "
        "is neutral overall, the central carbon atom is joined to each of the two oxygen "
        "atoms by a double bond. How many lone pairs does the finished diagram carry?",
      choices=["4", "2", "6", "8", "0"],
      ans=0,
      why="The available count follows from EK 1.5.A.3 and the periodic table, and EK "
          "2.1.A.2 makes each shared pair two of those electrons, so a double bond takes "
          "four. Whatever the bonds do not take remains as lone pairs, and the remainder "
          "here divides into that many pairs."),

 dict(q="In the accepted Lewis diagram for ammonia, whose formula is NH3 and which is "
        "neutral overall, the central nitrogen atom is joined to each of the three "
        "hydrogen atoms by a single bond. How many lone pairs does the diagram carry?",
      choices=["1", "0", "2", "3", "4"],
      ans=0,
      why="EK 1.5.A.3 and the periodic table give the available count, and EK 2.1.A.2 "
          "makes each single bond one shared pair, so three bonds take six electrons. What "
          "is left over is the diagram's lone pair count."),

 dict(q="Four species are tabulated with their formulas and overall charges. Which has "
        "the largest number of valence electrons available to its Lewis diagram?",
      table=_T_SPECIES,
      choices=["Sulfate ion", "Methane", "Carbon dioxide", "Nitrate ion",
               "Whichever species has the most atoms in its formula"],
      ans=0,
      why="EK 1.5.A.3 makes the total the sum of the atoms' valence electrons and EK "
          "1.5.A.1 makes each unit of negative charge one more electron, so the totals are "
          "computed row by row from the tabulated formula and charge. The number of atoms "
          "is not what sets the total, since different atoms contribute different numbers."),

 dict(q="A Lewis diagram is to be drawn for the carbonate ion, whose formula is CO3 and "
        "which carries an overall charge of 2-. How many valence electrons are available?",
      choices=["24", "22", "20", "26", "18"],
      ans=0,
      why="EK 1.5.A.3 gives four valence electrons for carbon and six for each oxygen from "
          "the periodic table, and EK 1.5.A.1 makes a charge of two minus two extra "
          "electrons. Neglecting the charge entirely gives one of the rejected counts."),

 dict(q="Besides an incorrect count of valence electrons, which further mistake does the "
        "framework name in connection with Lewis structures?",
      choices=[
        "Violating the octet rule",
        "Placing the heaviest atom at the center",
        "Drawing lone pairs as lines rather than as dots",
        "Using a periodic table rather than a table of atomic masses",
        "Assuming that every bond in a molecule has the same length"],
      ans=0,
      why="Unit 2's Preparing for the AP Exam page names violating the octet rule in "
          "exactly those words, alongside an incorrect valence electron count, and EK "
          "2.6.A.2 confirms the octet rule as a criterion the course uses. Which atom sits "
          "at the center is not among the mistakes the framework lists."),

 dict(q="A Lewis diagram is to be drawn for ethene, whose formula is C2H4 and which is "
        "neutral overall. How many valence electrons are available?",
      choices=["12", "10", "14", "16", "8"],
      ans=0,
      why="EK 1.5.A.3 makes the total the sum over the atoms present, four valence "
          "electrons for each carbon and one for each hydrogen. This is the molecule the "
          "framework's own sample multiple-choice question uses, and its diagram must "
          "account for exactly this many electrons."),

 dict(q="In the accepted Lewis diagram for methane, whose formula is CH4 and which is "
        "neutral overall, the central carbon atom is joined to each of the four hydrogen "
        "atoms by a single bond. How many lone pairs does the diagram carry?",
      choices=["0", "1", "2", "4", "8"],
      ans=0,
      why="EK 1.5.A.3 and the periodic table give the available count and EK 2.1.A.2 makes "
          "each single bond one shared pair, so the four bonds account for eight "
          "electrons. Nothing is left over, so the diagram carries no lone pair at all."),

 dict(q="Among the four tabulated species, which has the smallest number of valence "
        "electrons available to its Lewis diagram?",
      table=_T_SPECIES,
      choices=["Methane", "Carbon dioxide", "Nitrate ion", "Sulfate ion",
               "Whichever species carries the largest negative charge, since charge removes electrons"],
      ans=0,
      why="EK 1.5.A.3 makes the total the sum of the atoms' valence electrons, computed "
          "here row by row from the tabulated formulas. EK 1.5.A.1 makes a NEGATIVE charge "
          "a surplus of electrons rather than a deficit, so the doubly charged anion gains "
          "electrons rather than losing them."),

 dict(q="A Lewis diagram is to be drawn for carbon tetrachloride, whose formula is CCl4 "
        "and which is neutral overall. How many valence electrons are available?",
      choices=["32", "28", "20", "36", "40"],
      ans=0,
      why="EK 1.5.A.3 gives four valence electrons for carbon and seven for each chlorine "
          "from their columns of the periodic table. Forgetting the carbon altogether, or "
          "allowing every atom an octet from the start, gives two of the rejected totals."),

 dict(q="In the accepted Lewis diagram for nitrogen gas, whose formula is N2 and which is "
        "neutral overall, the two nitrogen atoms are joined by a triple bond. How many "
        "lone pairs does the diagram carry?",
      choices=["2", "1", "3", "4", "0"],
      ans=0,
      why="EK 1.5.A.3 and the periodic table give five valence electrons for each nitrogen, "
          "and EK 2.1.A.2 with EK 2.2.A.2 makes a triple bond three shared pairs. What the "
          "bond does not take is left as lone pairs, one on each atom."),

 dict(q="EK 2.7.A.2 states that both Lewis diagrams and VSEPR theory must be used to "
        "predict the structural properties of a molecule. What follows about a Lewis "
        "diagram on its own?",
      choices=[
        "It does not by itself settle the molecular geometry, which needs VSEPR theory as "
        "well",
        "It settles the molecular geometry completely, and VSEPR theory adds nothing",
        "It settles nothing at all about the molecule, since only VSEPR theory is used",
        "It settles the molecular geometry for neutral molecules but not for ions",
        "It settles the molecular geometry only when the molecule has no lone pairs"],
      ans=0,
      why="EK 2.7.A.2 says BOTH Lewis diagrams and VSEPR theory must be used for "
          "predicting electronic and structural properties, so neither is sufficient by "
          "itself. The framework draws no distinction there between ions and neutral "
          "molecules, nor between molecules with and without lone pairs."),

 dict(q="A Lewis diagram is to be drawn for phosphorus trichloride, whose formula is PCl3 "
        "and which is neutral overall. How many valence electrons are available?",
      choices=["26", "24", "20", "28", "32"],
      ans=0,
      why="EK 1.5.A.3 gives five valence electrons for phosphorus and seven for each "
          "chlorine from their columns of the periodic table. Treating phosphorus as "
          "though it had four valence electrons gives one of the rejected totals."),

 dict(q="In the accepted Lewis diagram for water, whose formula is H2O and which is "
        "neutral overall, the central oxygen atom is joined to each of the two hydrogen "
        "atoms by a single bond. How many lone pairs does the diagram carry?",
      choices=["2", "1", "3", "0", "4"],
      ans=0,
      why="EK 1.5.A.3 and the periodic table give six valence electrons for oxygen and one "
          "for each hydrogen, and EK 2.1.A.2 makes each single bond one shared pair, so "
          "the two bonds take four electrons. The remainder divides into that many lone "
          "pairs, all of them on the oxygen."),

 dict(q="Of the tabulated species, which has exactly twice as many valence electrons "
        "available as methane does?",
      table=_T_SPECIES,
      choices=["Carbon dioxide", "Nitrate ion", "Sulfate ion",
               "None of them, since no two totals are related that simply",
               "All three of the others, since each is larger than methane"],
      ans=0,
      why="EK 1.5.A.3 makes each total the sum of the atoms' valence electrons and EK "
          "1.5.A.1 adjusts for the tabulated charge, so the four totals can be compared "
          "directly. Exactly one of them is double the smallest, which is a fact about the "
          "computed numbers rather than about which species is larger."),

 dict(q="A Lewis diagram is to be drawn for hydrogen cyanide, whose formula is HCN and "
        "which is neutral overall. How many valence electrons are available?",
      choices=["10", "8", "12", "14", "9"],
      ans=0,
      why="EK 1.5.A.3 gives one valence electron for hydrogen, four for carbon and five "
          "for nitrogen from their positions in the periodic table. The total is what any "
          "acceptable diagram of the molecule has to account for exactly."),

 dict(q="What must be true of the valence electrons counted at the start of a Lewis "
        "diagram, once the diagram is finished?",
      choices=[
        "Every one of them appears in the diagram, either in a bond or as part of a lone "
        "pair",
        "Some of them may be left out, since only bonding electrons are drawn",
        "More may be drawn than were counted, if the octets require it",
        "Exactly half of them appear, since electrons are shared in pairs",
        "None of them appear individually; only the total is written beside the diagram"],
      ans=0,
      why="Unit 2's own list of mistakes names using the incorrect number of valence "
          "electrons, which presupposes that the finished diagram accounts for the counted "
          "electrons exactly. EK 2.1.A.2 makes the bonding electrons shared pairs, so the "
          "electrons not in bonds are the ones left as lone pairs."),

 dict(q="A Lewis diagram is to be drawn for ammonia, whose formula is NH3 and which is "
        "neutral overall. How many valence electrons are available?",
      choices=["8", "6", "10", "5", "11"],
      ans=0,
      why="EK 1.5.A.3 gives five valence electrons for nitrogen and one for each hydrogen "
          "from the periodic table. Counting only the nitrogen, or only the bonds that "
          "will be drawn, gives one of the rejected totals."),

 dict(q="How many of the four tabulated species have more than twenty valence electrons "
        "available to their Lewis diagrams?",
      table=_T_SPECIES,
      choices=["Exactly two", "Exactly one", "Exactly three", "All four", "None of them"],
      ans=0,
      why="EK 1.5.A.3 and EK 1.5.A.1 fix each total from the tabulated formula and charge, "
          "so the four totals can be computed and counted against the threshold the stem "
          "states. The threshold is the item's own test rather than any rule of the "
          "framework's."),

 dict(q="A Lewis diagram is to be drawn for the sulfate ion, whose formula is SO4 and "
        "which carries an overall charge of 2-. How many valence electrons are available?",
      choices=["32", "30", "28", "34", "24"],
      ans=0,
      why="EK 1.5.A.3 gives six valence electrons for sulfur and six for each oxygen from "
          "their column of the periodic table, and EK 1.5.A.1 makes a charge of two minus "
          "two extra electrons. Leaving the charge out gives one of the rejected counts."),

 dict(q="A student draws a Lewis diagram for sulfur dioxide, whose formula is SO2 and "
        "which is neutral overall, and the finished diagram shows 20 electrons in all. "
        "What has gone wrong?",
      choices=[
        "The diagram shows more valence electrons than the species actually has available",
        "The diagram shows fewer valence electrons than the species actually has available",
        "The diagram shows the right number of electrons but too few atoms",
        "Nothing has gone wrong; the number of electrons drawn is not fixed",
        "The diagram has counted the protons of each atom rather than its electrons"],
      ans=0,
      why="EK 1.5.A.3 and the periodic table fix the number of valence electrons the "
          "species brings, and unit 2's own list of mistakes names using the incorrect "
          "number of valence electrons as the first of them. Comparing the drawn total "
          "with the available total shows which direction the error runs in."),
]
