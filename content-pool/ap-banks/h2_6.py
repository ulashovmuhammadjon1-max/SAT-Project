r"""AP CHEMISTRY 2.6 Resonance and Formal Charge.

CED effective Fall 2024, Unit 2 Compound Structure and Properties.
Learning objective 2.6.A: represent a molecule with a Lewis diagram that
accounts for resonance between equivalent structures or that uses formal charge
to select between nonequivalent structures.
Suggested skill 6.C, support a claim with evidence from representations or
models at the particulate level.

Essential knowledge relied on, in the framework's own words:

  2.6.A.1  In cases where more than one equivalent Lewis structure can be
           constructed, resonance must be included as a refinement to the Lewis
           structure. In many such cases, this refinement is needed to provide
           qualitatively accurate predictions of molecular structure and
           properties.
  2.6.A.2  The octet rule and formal charge can be used as criteria for
           determining which of several possible valid Lewis diagrams provides
           the best model for predicting molecular structure and properties.
  2.6.A.3  As with any model, there are limitations to the use of the Lewis
           structure model, particularly in cases with an odd number of valence
           electrons.

THE CED NAMES FORMAL CHARGE BUT NEVER DEFINES IT. EK 2.6.A.2 makes formal
charge a criterion and unit 2's own page says students should practice
"calculating and connecting formal charges in Lewis structures", but no
sentence anywhere in the framework states the arithmetic. Supplying that
definition from memory and then keying answers to it is exactly what
SOCIAL_BRIEF.md forbids. So every calculating item here STATES THE DEFINITION IN
ITS OWN STEM and asks the student to apply it, and ``rule_stated_in_the_stem``
in the verifier asserts that none of them omits it. The key then rests on
arithmetic the item itself supplies, not on a rule the CED does not print.

The same move is used for the one comparison item that ranks candidate
diagrams: EK 2.6.A.2 licenses formal charge as a criterion but does not say
which way the comparison runs, so the item states the comparison it wants and
asks the student to carry it out.

FOURTEEN ITEMS ARE ARITHMETIC and seven more are table items; verify_h2_6.py
recomputes all twenty-one from the item's own stimulus. Item 21 additionally
checks its own answer against the species charge, since the formal charges of a
diagram must sum to the overall charge -- a cross-check the item's numbers
either satisfy or fail.

WHAT IS NOT HERE. Molecular geometry, bond angles and hybridization are EK
2.7.A.2 and 2.7.A.3 and belong to topic 2.7; the verifier asserts no item
mentions them. Constructing a first Lewis diagram at all is 2.5.

NO FIGURES. Every candidate diagram is described by numbers -- electrons in
lone pairs, electrons in bonds, formal charges carried -- and the question is
asked of those numbers.

NOTATION. Formulas stay plain text (NO2, ClO2) and formal charges are written
out as "a formal charge of +1". No math spans are needed in this module.
"""
TOPIC = ("2.6", "Resonance and Formal Charge", 2)

_RULE = ("Taking the formal charge on an atom to be its number of valence electrons, "
         "minus the number of electrons it holds in lone pairs, minus half the number "
         "of electrons it shares in bonds, ")

_T_PARITY_A = dict(
    headers=["Species", "Formula", "Overall charge"],
    rows=[["Nitrogen monoxide", "NO", "neutral"],
          ["Carbon dioxide", "CO2", "neutral"],
          ["Water", "H2O", "neutral"],
          ["Ammonia", "NH3", "neutral"]])

_T_PARITY_B = dict(
    headers=["Species", "Formula", "Overall charge"],
    rows=[["Nitrogen dioxide", "NO2", "neutral"],
          ["Sulfur dioxide", "SO2", "neutral"],
          ["Ozone", "O3", "neutral"],
          ["Methane", "CH4", "neutral"]])

_T_PARITY_C = dict(
    headers=["Species", "Formula", "Overall charge"],
    rows=[["Nitrogen monoxide", "NO", "neutral"],
          ["Chlorine dioxide", "ClO2", "neutral"],
          ["Carbon dioxide", "CO2", "neutral"],
          ["Water", "H2O", "neutral"]])

_T_CANDIDATES = dict(
    headers=["Candidate Lewis diagram",
             "Number of atoms carrying a nonzero formal charge",
             "Largest formal charge magnitude on any one atom"],
    rows=[["Diagram 1", "0", "0"],
          ["Diagram 2", "2", "1"],
          ["Diagram 3", "3", "2"],
          ["Diagram 4", "2", "3"]])

QUESTIONS = [

 dict(q="More than one equivalent Lewis structure can be constructed for a species. What "
        "does the framework require?",
      choices=[
        "That resonance be included as a refinement to the Lewis structure",
        "That the structure with the fewest bonds be chosen and the others discarded",
        "That the species be represented without any Lewis structure at all",
        "That the two structures be shown as belonging to two different compounds",
        "That the atoms be rearranged until only one structure can be drawn"],
      ans=0,
      why="EK 2.6.A.1, verbatim: in cases where more than one equivalent Lewis structure "
          "can be constructed, resonance must be included as a refinement to the Lewis "
          "structure. The framework refines the representation rather than discarding one "
          "of the equivalent structures."),

 dict(q="Why does the framework say that refinement is needed in many such cases?",
      choices=[
        "To provide qualitatively accurate predictions of molecular structure and "
        "properties",
        "To make the molecule easier to draw with fewer lines",
        "To make the total number of valence electrons come out even",
        "To allow the molecule to be assigned a single bond angle",
        "To remove the need to count valence electrons at all"],
      ans=0,
      why="EK 2.6.A.1 gives the reason in exactly those words: in many such cases this "
          "refinement is needed to provide qualitatively accurate predictions of molecular "
          "structure and properties. Ease of drawing is not a reason the framework offers "
          "anywhere."),

 dict(q="In one proposed Lewis diagram of a polyatomic ion, a nitrogen atom has 0 "
        "electrons in lone pairs and 8 electrons in bonds. " + _RULE +
        "what formal charge does that nitrogen carry?",
      choices=["A formal charge of +1", "A formal charge of 0", "A formal charge of -1",
               "A formal charge of +3", "A formal charge of -3"],
      ans=0,
      why="EK 2.6.A.2 makes formal charge a criterion for choosing among valid Lewis "
          "diagrams, and the arithmetic the stem states is applied to the nitrogen's five "
          "valence electrons. Halving the bonding electrons is the step that separates the "
          "keyed value from the rejected ones."),

 dict(q="Several valid Lewis diagrams can be drawn for one species. Which two criteria "
        "does the framework name for deciding among them?",
      choices=[
        "The octet rule and formal charge",
        "The octet rule and the molar mass of the species",
        "Formal charge and the temperature of the sample",
        "Electronegativity and the number of atoms in the species",
        "The number of lone pairs and the color of the substance"],
      ans=0,
      why="EK 2.6.A.2, verbatim: the octet rule and formal charge can be used as criteria "
          "for determining which of several possible valid Lewis diagrams provides the "
          "best model. No other property appears in that sentence."),

 dict(q="A candidate Lewis diagram places an oxygen atom with 4 electrons in lone pairs "
        "and 4 electrons in bonds. " + _RULE +
        "what formal charge does that oxygen carry?",
      choices=["A formal charge of 0", "A formal charge of +1", "A formal charge of -1",
               "A formal charge of +2", "A formal charge of -2"],
      ans=0,
      why="EK 2.6.A.2 makes formal charge a criterion for selecting among valid diagrams, "
          "and the stem's own arithmetic is applied to the oxygen's six valence electrons. "
          "Forgetting to halve the bonding electrons gives one of the rejected values."),

 dict(q="Four neutral species are tabulated with their formulas. In which one is the "
        "total number of valence electrons odd?",
      table=_T_PARITY_A,
      choices=["Nitrogen monoxide", "Carbon dioxide", "Water", "Ammonia",
               "In none of them, since a molecule cannot have an odd electron count"],
      ans=0,
      why="EK 2.6.A.3 singles out species with an odd number of valence electrons as the "
          "case where the Lewis model's limitations show, so the count has to be done "
          "before the limitation can be recognized. Summing each tabulated formula's "
          "valence electrons finds the odd one."),

 dict(q="Another candidate diagram gives an oxygen atom 6 electrons in lone pairs and 2 "
        "electrons in bonds. " + _RULE +
        "what formal charge does that oxygen carry?",
      choices=["A formal charge of -1", "A formal charge of 0", "A formal charge of +1",
               "A formal charge of -2", "A formal charge of +2"],
      ans=0,
      why="EK 2.6.A.2 makes formal charge one of the criteria for choosing among valid "
          "diagrams, and the stem's arithmetic applied to oxygen's six valence electrons "
          "leaves the atom with more electrons than it brought. A sign error gives the "
          "mirror-image rejected value."),

 dict(q="What are the octet rule and formal charge used to determine, according to the "
        "framework?",
      choices=[
        "Which of several possible valid Lewis diagrams provides the best model for "
        "predicting molecular structure and properties",
        "Whether a species can exist at all",
        "How many grams of a substance will react",
        "The temperature at which a molecule decomposes",
        "Which of two elements is more electronegative"],
      ans=0,
      why="EK 2.6.A.2 states the purpose in exactly those words. The criteria choose "
          "between diagrams already known to be valid, rather than deciding whether the "
          "species exists or predicting anything about a reacting quantity."),

 dict(q="A carbon atom in a proposed diagram has 0 electrons in lone pairs and 8 "
        "electrons in bonds. " + _RULE +
        "what formal charge does that carbon carry?",
      choices=["A formal charge of 0", "A formal charge of +1", "A formal charge of -1",
               "A formal charge of +4", "A formal charge of -4"],
      ans=0,
      why="EK 2.6.A.2 makes formal charge a criterion among valid diagrams, and the stem's "
          "arithmetic applied to carbon's four valence electrons leaves it exactly as it "
          "began. Neglecting to halve the bonding electrons produces the largest rejected "
          "value."),

 dict(q="What does the framework say about the limitations of the Lewis structure model?",
      choices=[
        "As with any model there are limitations, particularly for species with an odd "
        "number of valence electrons",
        "There are no limitations, since every species has a valid Lewis structure",
        "The limitations arise only for species containing metals",
        "The limitations arise only at high temperature",
        "The limitations arise only for species carrying an overall charge"],
      ans=0,
      why="EK 2.6.A.3, verbatim: as with any model, there are limitations to the use of "
          "the Lewis structure model, particularly in cases with an odd number of valence "
          "electrons. The framework names no other class of species there."),

 dict(q="A sulfur atom in one candidate diagram has 2 electrons in lone pairs and 6 "
        "electrons in bonds. " + _RULE +
        "what formal charge does that sulfur carry?",
      choices=["A formal charge of +1", "A formal charge of 0", "A formal charge of -1",
               "A formal charge of +2", "A formal charge of -2"],
      ans=0,
      why="EK 2.6.A.2 makes formal charge a criterion for choosing among valid diagrams, "
          "and the stem's arithmetic applied to sulfur's six valence electrons leaves it "
          "one electron short of what it brought. Treating sulfur as though it had four "
          "valence electrons gives a rejected value."),

 dict(q="Four candidate Lewis diagrams for one species are summarized in the table. If "
        "the preferred diagram is the one whose atoms carry formal charges closest to "
        "zero, which is preferred?",
      table=_T_CANDIDATES,
      choices=["Diagram 1", "Diagram 2", "Diagram 3", "Diagram 4",
               "No diagram can be preferred, since all four are valid"],
      ans=0,
      why="EK 2.6.A.2 licenses formal charge as a criterion for determining which valid "
          "diagram provides the best model, and the stem states the direction the "
          "comparison runs. One tabulated diagram carries no nonzero formal charge at all, "
          "so it wins on both tabulated columns at once."),

 dict(q="In a further candidate, an oxygen atom has 2 electrons in lone pairs and 6 "
        "electrons in bonds. " + _RULE +
        "what formal charge does that oxygen carry?",
      choices=["A formal charge of +1", "A formal charge of 0", "A formal charge of -1",
               "A formal charge of +2", "A formal charge of -2"],
      ans=0,
      why="EK 2.6.A.2 makes formal charge a criterion among valid diagrams, and the stem's "
          "arithmetic applied to oxygen's six valence electrons leaves it one electron "
          "short. This is the arrangement that makes an oxygen atom positively charged "
          "formally, which is what makes such a diagram worth comparing against others."),

 dict(q="Two valid Lewis diagrams for a species are NOT equivalent to one another. Which "
        "part of the framework applies?",
      choices=[
        "The octet rule and formal charge, used as criteria to select the better diagram",
        "Resonance, which must be included as a refinement whenever two diagrams exist",
        "Neither; a species with two valid diagrams has no acceptable representation",
        "The requirement that the two diagrams be averaged atom by atom",
        "The requirement that the diagram with the larger number of atoms be chosen"],
      ans=0,
      why="EK 2.6.A.1 conditions resonance on more than one EQUIVALENT structure, so it "
          "does not reach this case; EK 2.6.A.2 supplies the octet rule and formal charge "
          "as the criteria for choosing among several possible valid diagrams. Learning "
          "objective 2.6.A puts the two cases side by side in exactly this way."),

 dict(q="A nitrogen atom in one candidate has 2 electrons in lone pairs and 6 electrons "
        "in bonds. " + _RULE + "what formal charge does that nitrogen carry?",
      choices=["A formal charge of 0", "A formal charge of +1", "A formal charge of -1",
               "A formal charge of +2", "A formal charge of -2"],
      ans=0,
      why="EK 2.6.A.2 makes formal charge a criterion among valid diagrams, and the stem's "
          "arithmetic applied to nitrogen's five valence electrons returns exactly what it "
          "brought. Neglecting the lone pair entirely gives one of the rejected values."),

 dict(q="Of these four neutral species, tabulated with their formulas, which has an odd "
        "total number of valence electrons?",
      table=_T_PARITY_B,
      choices=["Nitrogen dioxide", "Sulfur dioxide", "Ozone", "Methane",
               "All four, since every species with three atoms has an odd count"],
      ans=0,
      why="EK 2.6.A.3 names an odd number of valence electrons as the case where the Lewis "
          "model's limitations are clearest, and the count is done by summing the valence "
          "electrons of the atoms in each tabulated formula. The number of atoms does not "
          "by itself decide the parity."),

 dict(q="A chlorine atom in a proposed diagram has 0 electrons in lone pairs and 8 "
        "electrons in bonds. " + _RULE +
        "what formal charge does that chlorine carry?",
      choices=["A formal charge of +3", "A formal charge of +1", "A formal charge of 0",
               "A formal charge of -1", "A formal charge of -3"],
      ans=0,
      why="EK 2.6.A.2 makes formal charge a criterion among valid diagrams, and the stem's "
          "arithmetic applied to chlorine's seven valence electrons gives a large positive "
          "value. A diagram assigning a formal charge this far from zero is exactly the "
          "kind the criterion is meant to weigh against."),

 dict(q="The framework introduces the limitations of the Lewis model with the phrase as "
        "with any model. What does that phrase indicate?",
      choices=[
        "That having limitations is expected of models generally, not a defect peculiar to "
        "this one",
        "That the Lewis model has more limitations than any other model in the course",
        "That the Lewis model should not be used at all",
        "That every model fails specifically for odd numbers of valence electrons",
        "That the limitations apply only when a model is used outside chemistry"],
      ans=0,
      why="EK 2.6.A.3 opens with as with any model, which places the Lewis structure model "
          "among models in general rather than singling it out, while still naming the odd "
          "valence electron count as where its limitations particularly show. The "
          "framework does not extend that particular failure to every model."),

 dict(q="In another candidate, a carbon atom has 2 electrons in lone pairs and 6 electrons "
        "in bonds. " + _RULE + "what formal charge does that carbon carry?",
      choices=["A formal charge of -1", "A formal charge of 0", "A formal charge of +1",
               "A formal charge of -2", "A formal charge of +2"],
      ans=0,
      why="EK 2.6.A.2 makes formal charge a criterion among valid diagrams, and the stem's "
          "arithmetic applied to carbon's four valence electrons leaves it holding one "
          "electron more than it brought. Dropping the lone pair from the calculation "
          "gives one of the rejected values."),

 dict(q="Using the same four tabulated candidate diagrams, which places the largest single "
        "formal charge on one atom?",
      table=_T_CANDIDATES,
      choices=["Diagram 4", "Diagram 1", "Diagram 2", "Diagram 3",
               "Diagram 3, because it has the most atoms carrying a nonzero formal charge"],
      ans=0,
      why="The two tabulated columns measure different things: how many atoms carry a "
          "nonzero formal charge, and how large the largest one is. The diagram with the "
          "most charged atoms is not the one with the largest single charge, which is why "
          "EK 2.6.A.2's criterion has to be applied to the quantity actually asked about."),

 dict(q="In one Lewis diagram of the nitrite ion, whose formula is NO2 and which carries "
        "an overall charge of 1-, the nitrogen atom has 2 electrons in lone pairs and 6 "
        "electrons in bonds, one oxygen atom has 4 electrons in lone pairs and 4 electrons "
        "in bonds, and the other oxygen atom has 6 electrons in lone pairs and 2 electrons "
        "in bonds. " + _RULE + "what do the three formal charges add up to?",
      choices=["A sum of -1", "A sum of 0", "A sum of +1", "A sum of -2",
               "A sum of +2"],
      ans=0,
      why="EK 2.6.A.2 makes formal charge a criterion among valid diagrams, and applying "
          "the stem's arithmetic atom by atom and adding the results gives the total. That "
          "total has to come out equal to the ion's own overall charge, which is what "
          "makes the sum a check on the diagram rather than a separate fact."),

 dict(q="EK 2.6.A.1 says the resonance refinement is needed in MANY such cases. What does "
        "that wording rule out?",
      choices=[
        "Claiming that the refinement is needed in every case where equivalent structures "
        "exist",
        "Claiming that resonance must be included when equivalent structures exist",
        "Claiming that the refinement improves predictions of structure and properties",
        "Claiming that more than one equivalent structure can sometimes be drawn",
        "Claiming that a Lewis structure can be refined at all"],
      ans=0,
      why="EK 2.6.A.1 makes the inclusion of resonance unconditional but hedges its "
          "necessity for accurate prediction with in many such cases, so a universal claim "
          "about the prediction goes beyond the sentence. The other statements are each "
          "part of what the sentence asserts."),

 dict(q="A nitrogen atom in a further candidate has 4 electrons in lone pairs and 4 "
        "electrons in bonds. " + _RULE + "what formal charge does that nitrogen carry?",
      choices=["A formal charge of -1", "A formal charge of 0", "A formal charge of +1",
               "A formal charge of -2", "A formal charge of +2"],
      ans=0,
      why="EK 2.6.A.2 makes formal charge a criterion among valid diagrams, and the stem's "
          "arithmetic applied to nitrogen's five valence electrons leaves it one electron "
          "to the good. Counting the bonding electrons in full rather than halving them "
          "gives a rejected value."),

 dict(q="Among those four tabulated candidates, which spreads nonzero formal charge over "
        "the greatest number of atoms?",
      table=_T_CANDIDATES,
      choices=["Diagram 3", "Diagram 1", "Diagram 2", "Diagram 4",
               "Diagram 4, because it carries the largest single formal charge"],
      ans=0,
      why="One tabulated column counts the atoms carrying a nonzero formal charge and the "
          "other measures the largest single value, and they do not point at the same "
          "diagram. EK 2.6.A.2 makes formal charge a criterion but leaves which of these "
          "quantities to compare to the question being asked."),

 dict(q="Nitrogen dioxide, whose formula is NO2 and which is neutral overall, brings an "
        "odd number of valence electrons to its Lewis diagram. What follows?",
      choices=[
        "At least one electron must be left unpaired, which is the limitation the "
        "framework names",
        "The diagram must simply use one electron fewer, rounding the count down",
        "The species cannot exist, since electrons occur only in pairs",
        "The diagram must show the extra electron outside the molecule",
        "Nothing follows; an odd count and an even count are handled identically"],
      ans=0,
      why="Summing the valence electrons of the atoms in the formula gives an odd total, "
          "and an odd number cannot be divided entirely into pairs, so some electron is "
          "left unpaired. EK 2.6.A.3 names exactly this case as where the limitations of "
          "the Lewis structure model particularly show."),

 dict(q="In yet another candidate, a phosphorus atom has 2 electrons in lone pairs and 6 "
        "electrons in bonds. " + _RULE + "what formal charge does that phosphorus carry?",
      choices=["A formal charge of 0", "A formal charge of +1", "A formal charge of -1",
               "A formal charge of +2", "A formal charge of -2"],
      ans=0,
      why="EK 2.6.A.2 makes formal charge a criterion among valid diagrams, and the stem's "
          "arithmetic applied to phosphorus's five valence electrons returns exactly what "
          "it brought. Phosphorus and nitrogen share a column of the periodic table, so "
          "the same numbers give the same result for either."),

 dict(q="How many of these four tabulated neutral species have an odd total number of "
        "valence electrons?",
      table=_T_PARITY_C,
      choices=["Exactly two", "Exactly one", "Exactly three", "All four", "None of them"],
      ans=0,
      why="EK 2.6.A.3 makes an odd valence electron count the case where the Lewis model's "
          "limitations particularly show, so the parity of each tabulated formula has to "
          "be worked out and counted. Summing the atoms' valence electrons row by row "
          "settles it."),

 dict(q="Of the four tabulated candidate diagrams, how many place a formal charge of "
        "magnitude two or more on some atom?",
      table=_T_CANDIDATES,
      choices=["Exactly two", "Exactly one", "Exactly three", "All four", "None of them"],
      ans=0,
      why="The tabulated column giving the largest formal charge magnitude on any one atom "
          "is what the threshold applies to, and counting the rows that reach it answers "
          "the question. EK 2.6.A.2 is what makes formal charge worth measuring across "
          "candidate diagrams in the first place."),

 dict(q="A final candidate gives a carbon atom 4 electrons in lone pairs and 4 electrons "
        "in bonds. " + _RULE + "what formal charge does that carbon carry?",
      choices=["A formal charge of -2", "A formal charge of -1", "A formal charge of 0",
               "A formal charge of +1", "A formal charge of +2"],
      ans=0,
      why="EK 2.6.A.2 makes formal charge a criterion among valid diagrams, and the stem's "
          "arithmetic applied to carbon's four valence electrons leaves it two electrons to "
          "the good. A diagram assigning a charge this far from zero is what the criterion "
          "exists to weigh against."),

 dict(q="Which statement about the Lewis structure model is NOT supported by the "
        "framework?",
      choices=[
        "The model applies without limitation to every species",
        "The model has limitations, as any model does",
        "Its limitations show particularly for odd numbers of valence electrons",
        "Formal charge can be used to choose among several valid diagrams",
        "Resonance must be included when more than one equivalent structure can be drawn"],
      ans=0,
      why="EK 2.6.A.3 states that there are limitations to the use of the Lewis structure "
          "model, so a claim of no limitations contradicts it directly. EK 2.6.A.1 and EK "
          "2.6.A.2 supply the remaining statements between them."),
]
