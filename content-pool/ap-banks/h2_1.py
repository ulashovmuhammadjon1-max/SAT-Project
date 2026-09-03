r"""AP CHEMISTRY 2.1 Types of Chemical Bonds.

CED effective Fall 2024, Unit 2 Compound Structure and Properties.
Learning objective 2.1.A: explain the relationship between the type of bonding
and the properties of the elements participating in the bond.
Suggested skill 6.A, make a scientific claim.

Essential knowledge relied on, in the framework's own words:

  2.1.A.1  Electronegativity values for the representative elements increase
           going from left to right across a period and decrease going down a
           group. These trends can be understood qualitatively through the
           electronic structure of the atoms, the shell model, and Coulomb's
           law.
  2.1.A.2  Valence electrons shared between atoms of similar electronegativity
           constitute a nonpolar covalent bond. For example, bonds between
           carbon and hydrogen are effectively nonpolar even though carbon is
           slightly more electronegative than hydrogen.
  2.1.A.3  Valence electrons shared between atoms of unequal electronegativity
           constitute a polar covalent bond.
             i.   The atom with a higher electronegativity will develop a
                  partial negative charge relative to the other atom in the
                  bond.
             ii.  In single bonds, greater differences in electronegativity
                  lead to greater bond dipoles.
             iii. All polar bonds have some ionic character, and the difference
                  between ionic and covalent bonding is not distinct but rather
                  a continuum.
  2.1.A.4  The difference in electronegativity is not the only factor in
           determining if a bond should be designated as ionic or covalent.
           Generally, bonds between a metal and nonmetal are ionic, and bonds
           between two nonmetals are covalent. Examination of the properties of
           a compound is the best way to characterize the type of bonding.
  2.1.A.5  In a metallic solid, the valence electrons from the metal atoms are
           considered to be delocalized and not associated with any individual
           atom.

ON THE HEDGES, WHICH ARE THE POINT OF THIS TOPIC. EK 2.1.A.3.iii and EK 2.1.A.4
both say something a bank is tempted to smooth away: bonding is a CONTINUUM,
electronegativity difference is NOT the only factor, and properties are the
best way to characterise a bond. Items 6, 15, 20, 24, 27, 28 and 29 exist to
keep those hedges, and none of the other items contradicts them -- no key here
states a numerical cutoff between ionic and covalent, because the framework
states none.

ON EK 2.1.A.3.ii's OWN QUALIFIER. The framework ties a greater difference to a
greater dipole IN SINGLE BONDS. Every item comparing dipole magnitudes says
"single bond" in the stem.

HOW THIS TOPIC IS KEPT DISTINCT FROM 1.7. Topic 1.7 asks what the
electronegativity trend IS and predicts it from position. Here the trend is a
tool: item 1 states it because EK 2.1.A.1 is one of this topic's own statements,
and every other item uses electronegativity to classify a bond, which is what LO
2.1.A asks and 1.7 never does.

NOTATION. Electronegativity values and formulas are plain prose; partial charges
are written in words ("a partial negative charge"), never as a bare superscript.
"""
TOPIC = ("2.1", "Types of Chemical Bonds", 2)

_T_EN = dict(
    headers=["Element", "Electronegativity"],
    rows=[["Potassium", "0.8"], ["Sodium", "0.9"], ["Magnesium", "1.2"],
          ["Aluminum", "1.5"], ["Hydrogen", "2.1"], ["Phosphorus", "2.1"],
          ["Carbon", "2.5"], ["Sulfur", "2.5"], ["Nitrogen", "3.0"],
          ["Chlorine", "3.0"], ["Oxygen", "3.5"], ["Fluorine", "4.0"]])

_T_BONDS = dict(
    headers=["Single bond", "Electronegativity of the first atom",
             "Electronegativity of the second atom"],
    rows=[["Bond 1: hydrogen to hydrogen", "2.1", "2.1"],
          ["Bond 2: carbon to hydrogen", "2.5", "2.1"],
          ["Bond 3: nitrogen to hydrogen", "3.0", "2.1"],
          ["Bond 4: oxygen to hydrogen", "3.5", "2.1"],
          ["Bond 5: fluorine to hydrogen", "4.0", "2.1"]])

_T_PAIRS = dict(
    headers=["Pair of elements", "Electronegativity of the first element",
             "Electronegativity of the second element"],
    rows=[["Carbon and sulfur", "2.5", "2.5"],
          ["Phosphorus and chlorine", "2.1", "3.0"],
          ["Sodium and fluorine", "0.9", "4.0"],
          ["Carbon and oxygen", "2.5", "3.5"]])

_T_PROPERTIES = dict(
    headers=["Substance", "Melting point (degrees Celsius)",
             "Conducts electricity when melted"],
    rows=[["Substance R", "801", "yes"], ["Substance S", "-114", "no"],
          ["Substance T", "1,291", "yes"], ["Substance U", "-23", "no"]])

_T_ROWS = dict(
    headers=["Element", "Row of the periodic table", "Column of the periodic table",
             "Metal or nonmetal"],
    rows=[["Element A", "3", "1", "metal"], ["Element B", "3", "17", "nonmetal"],
          ["Element C", "2", "16", "nonmetal"], ["Element D", "4", "2", "metal"]])

QUESTIONS = [

 dict(q="How do electronegativity values of the representative elements vary with "
        "position in the periodic table?",
      choices=[
        "They increase from left to right across a period and decrease down a group.",
        "They decrease from left to right across a period and increase down a group.",
        "They increase both across a period and down a group.",
        "They decrease both across a period and down a group.",
        "They are the same for every representative element, since all share the same "
        "kind of valence shell."],
      ans=0,
      why="EK 2.1.A.1, near verbatim: electronegativity values for the representative "
          "elements increase going from left to right across a period and decrease "
          "going down a group. The framework adds that the trends are understood "
          "through electronic structure, the shell model and Coulomb's law."),

 dict(q="Valence electrons are shared between two atoms whose electronegativities are "
        "very similar. What kind of bond is that?",
      choices=["A nonpolar covalent bond", "A polar covalent bond",
               "An ionic bond", "A metallic bond",
               "No bond at all, because similar atoms do not attract each other"],
      ans=0,
      why="EK 2.1.A.2, near verbatim: valence electrons shared between atoms of similar "
          "electronegativity constitute a nonpolar covalent bond. Sharing is what makes "
          "it covalent and similarity is what makes it nonpolar."),

 dict(q="Valence electrons are shared between two atoms whose electronegativities are "
        "unequal. What kind of bond is that, and where does the partial negative charge "
        "sit?",
      choices=[
        "A polar covalent bond, with the partial negative charge on the atom of higher "
        "electronegativity.",
        "A polar covalent bond, with the partial negative charge on the atom of lower "
        "electronegativity.",
        "A nonpolar covalent bond, with no partial charges anywhere.",
        "An ionic bond, with a full negative charge on the atom of higher "
        "electronegativity.",
        "A metallic bond, with the charge delocalized over both atoms."],
      ans=0,
      why="EK 2.1.A.3 makes shared valence electrons between atoms of unequal "
          "electronegativity a polar covalent bond, and EK 2.1.A.3.i puts the partial "
          "negative charge on the atom with the higher electronegativity. The charges "
          "are partial rather than full, which is what separates this from an ionic "
          "bond."),

 dict(q="Using the tabulated electronegativities, which single bond has the largest "
        "bond dipole?",
      table=_T_BONDS,
      choices=["Bond 5", "Bond 1", "Bond 2", "Bond 3", "Bond 4"],
      ans=0,
      why="EK 2.1.A.3.ii states that in single bonds, greater differences in "
          "electronegativity lead to greater bond dipoles, so the largest difference "
          "between the two tabulated values marks the largest dipole."),

 dict(q="Using the same table, which single bond is nonpolar?",
      table=_T_BONDS,
      choices=["Bond 1", "Bond 2", "Bond 3", "Bond 4", "Bond 5"],
      ans=0,
      why="EK 2.1.A.2 makes a bond between atoms of similar electronegativity nonpolar "
          "covalent, and one tabulated pair has no difference at all between its two "
          "values. Every other row shows some difference and so some dipole."),

 dict(q="The framework says that bonds between carbon and hydrogen are effectively "
        "nonpolar even though carbon is slightly more electronegative than hydrogen. "
        "What does that example illustrate?",
      choices=[
        "That a small difference in electronegativity produces a bond that is treated "
        "as nonpolar covalent.",
        "That carbon and hydrogen have exactly equal electronegativity values.",
        "That a bond can be nonpolar only when the two atoms are of the same element.",
        "That carbon and hydrogen form an ionic bond with each other.",
        "That electronegativity differences have no effect on bond polarity."],
      ans=0,
      why="EK 2.1.A.2 gives exactly this example and states that the bonds are "
          "effectively nonpolar EVEN THOUGH carbon is slightly more electronegative, "
          "which is a statement that a small difference is treated as no difference "
          "rather than that no difference exists."),

 dict(q="Which statement about the relationship between ionic and covalent bonding does "
        "the framework make?",
      choices=[
        "All polar bonds have some ionic character, and the difference between ionic "
        "and covalent bonding is a continuum rather than a sharp division.",
        "A bond is either fully ionic or fully covalent, with nothing in between.",
        "All covalent bonds are nonpolar, and all polar bonds are ionic.",
        "Ionic bonding occurs only between two metals, and covalent bonding only "
        "between two nonmetals.",
        "Any bond with an electronegativity difference above a fixed value is ionic and "
        "any bond below it is covalent."],
      ans=0,
      why="EK 2.1.A.3.iii, near verbatim: all polar bonds have some ionic character, and "
          "the difference between ionic and covalent bonding is not distinct but rather "
          "a continuum. The framework states no numerical cutoff anywhere, which is what "
          "the last rejected option invents."),

 dict(q="A bond forms between a metal and a nonmetal. What does the framework say about "
        "its likely designation?",
      choices=[
        "It is generally ionic, though the electronegativity difference is not the only "
        "factor involved.",
        "It is always ionic, and the electronegativity difference settles the matter "
        "completely.",
        "It is generally covalent, because both atoms contribute valence electrons.",
        "It is generally metallic, because one of the two atoms is a metal.",
        "Its designation cannot be estimated at all without measuring the compound's "
        "properties."],
      ans=0,
      why="EK 2.1.A.4 states that generally, bonds between a metal and nonmetal are "
          "ionic, and in the same breath that the difference in electronegativity is "
          "not the only factor in determining the designation. Both halves have to be "
          "kept, which is what rules out the two options that make the rule absolute."),

 dict(q="According to the framework, what is the best way to characterize the type of "
        "bonding in a compound?",
      choices=[
        "Examination of the properties of the compound.",
        "Calculation of the difference in electronegativity between the two elements.",
        "Comparison of the masses of the two elements involved.",
        "Counting the number of valence electrons each element started with.",
        "Determining which element was discovered first."],
      ans=0,
      why="EK 2.1.A.4, near verbatim: examination of the properties of a compound is the "
          "best way to characterize the type of bonding. The framework offers the "
          "electronegativity difference as a useful indicator in the same statement and "
          "explicitly denies that it is the only factor."),

 dict(q="How does the framework describe the valence electrons in a metallic solid?",
      choices=[
        "As delocalized, and not associated with any individual atom.",
        "As localized in pairs between neighboring atoms.",
        "As transferred completely from one atom to another.",
        "As confined to the core of each atom.",
        "As absent, since metal atoms have no valence electrons."],
      ans=0,
      why="EK 2.1.A.5, near verbatim: in a metallic solid, the valence electrons from "
          "the metal atoms are considered to be delocalized and not associated with any "
          "individual atom. A localized shared pair is a covalent bond and a complete "
          "transfer is an ionic one."),

 dict(q="Using the tabulated electronegativities, which pair of elements would form the "
        "bond with the greatest ionic character?",
      table=_T_PAIRS,
      choices=["Sodium and fluorine", "Carbon and sulfur",
               "Phosphorus and chlorine", "Carbon and oxygen",
               "All four pairs are equal, because each involves two different elements"],
      ans=0,
      why="EK 2.1.A.3.iii places ionic and covalent bonding on a continuum with all "
          "polar bonds having some ionic character, and EK 2.1.A.3.ii ties a larger "
          "electronegativity difference to a larger bond dipole. The tabulated pair "
          "with the largest difference therefore sits farthest toward the ionic end."),

 dict(q="Using the same table, which pair of elements would form a nonpolar covalent "
        "bond?",
      table=_T_PAIRS,
      choices=["Carbon and sulfur", "Phosphorus and chlorine",
               "Sodium and fluorine", "Carbon and oxygen",
               "None of them, because a nonpolar bond requires two atoms of the same "
               "element"],
      ans=0,
      why="EK 2.1.A.2 makes shared valence electrons between atoms of SIMILAR "
          "electronegativity a nonpolar covalent bond, and one tabulated pair shows no "
          "difference at all. The framework's own carbon-to-hydrogen example shows that "
          "two different elements can bond nonpolarly."),

 dict(q="In a single bond between two different atoms, what happens to the bond dipole "
        "as the difference in electronegativity between the atoms grows?",
      choices=["The bond dipole grows as well.", "The bond dipole shrinks.",
               "The bond dipole is unaffected, since only the shared pair matters.",
               "The bond dipole first grows and then shrinks.",
               "The bond dipole disappears entirely once the difference is large."],
      ans=0,
      why="EK 2.1.A.3.ii, near verbatim: in single bonds, greater differences in "
          "electronegativity lead to greater bond dipoles. The framework attaches the "
          "claim specifically to single bonds, which is why the stem specifies one."),

 dict(q="Four substances were tested with the results in the table. Which substance's "
        "properties point most clearly to ionic bonding?",
      table=_T_PROPERTIES,
      choices=[
        "Substance T, which has the highest melting point and conducts when melted.",
        "Substance S, which has the lowest melting point and does not conduct when "
        "melted.",
        "Substance U, which does not conduct when melted.",
        "Substance R, because it has the lowest melting point of the conducting "
        "substances.",
        "None of them, because bonding type cannot be judged from properties."],
      ans=0,
      why="EK 2.1.A.4 states that examination of the properties of a compound is the "
          "best way to characterize the type of bonding, and EK 3.2.A.3 supplies what "
          "ionic solids look like: high melting points and conduction when melted. The "
          "keyed substance has the highest tabulated melting point among those that "
          "conduct."),

 dict(q="Two students disagree. The first says that any bond whose electronegativity "
        "difference exceeds a particular number is ionic and any bond below it is "
        "covalent. The second says the two kinds of bonding shade into one another. "
        "Which position does the framework support, and why?",
      choices=[
        "The second, because the difference between ionic and covalent bonding is "
        "described as a continuum rather than a sharp division.",
        "The first, because the framework sets the dividing value at exactly one and "
        "seven tenths.",
        "The first, because every bond must be classified as one or the other for a "
        "formula to be written.",
        "The second, because electronegativity differences cannot be measured at all.",
        "Neither, because the framework treats all bonds as ionic."],
      ans=0,
      why="EK 2.1.A.3.iii states that all polar bonds have some ionic character and that "
          "the difference between ionic and covalent bonding is not distinct but rather "
          "a continuum. The framework prints no dividing value, and EK 2.1.A.4 adds that "
          "the electronegativity difference is not the only factor in any case."),

 dict(q="In a bond between hydrogen and chlorine, which atom carries the partial "
        "negative charge, and why?",
      table=_T_EN,
      choices=[
        "Chlorine, because its tabulated electronegativity is the higher of the two.",
        "Hydrogen, because its tabulated electronegativity is the lower of the two.",
        "Chlorine, because it is the heavier of the two atoms.",
        "Hydrogen, because it has only one electron to contribute.",
        "Neither, because the two atoms share the electrons equally."],
      ans=0,
      why="EK 2.1.A.3.i states that the atom with a higher electronegativity will develop "
          "a partial negative charge relative to the other atom in the bond, and the "
          "tabulated values settle which atom that is. Mass and electron count do not "
          "enter the framework's statement."),

 dict(q="Which claim about bonding is best supported by the tabulated electronegativity "
        "values alone?",
      table=_T_EN,
      choices=[
        "A bond between potassium and fluorine would be more polar than a bond between "
        "carbon and sulfur.",
        "A bond between potassium and fluorine would be less polar than a bond between "
        "carbon and sulfur.",
        "A bond between carbon and sulfur would carry a full negative charge on carbon.",
        "Every bond in the table would be ionic, since all the elements differ.",
        "No claim about polarity can be supported by electronegativity values."],
      ans=0,
      why="Suggested skill 6.A asks for a claim the evidence supports. EK 2.1.A.3.ii ties "
          "a larger electronegativity difference to a larger dipole, and the tabulated "
          "values give the first pair a large difference and the second none at all. A "
          "FULL charge would make the bond ionic rather than polar covalent."),

 dict(q="What does it mean to say that a polar covalent bond has some ionic character?",
      choices=[
        "The shared electrons are pulled toward one atom, giving partial charges that "
        "resemble a small version of the complete transfer in an ionic bond.",
        "The bond is half of an ionic bond and half of a covalent bond, in equal parts.",
        "The two atoms have exchanged an electron completely, as in an ionic compound.",
        "The bond will break into ions whenever the compound is heated.",
        "The bond contains a metal atom, since only metals produce ionic character."],
      ans=0,
      why="EK 2.1.A.3.iii states that all polar bonds have some ionic character and that "
          "the two kinds of bonding form a continuum, and EK 2.1.A.3.i describes the "
          "partial charges that arise from unequal sharing. A complete transfer would "
          "place the bond at the ionic end rather than partway along."),

 dict(q="Two atoms of the same element share a pair of valence electrons. What kind of "
        "bond results, and what is the electronegativity difference?",
      choices=[
        "A nonpolar covalent bond, with an electronegativity difference of zero.",
        "A polar covalent bond, with a small electronegativity difference.",
        "An ionic bond, with a large electronegativity difference.",
        "A metallic bond, with the electrons delocalized over both atoms.",
        "No bond, because two identical atoms cannot share electrons."],
      ans=0,
      why="Two atoms of one element have identical electronegativities, and EK 2.1.A.2 "
          "makes shared valence electrons between atoms of similar electronegativity a "
          "nonpolar covalent bond. Zero difference is the limiting case of similarity."),

 dict(q="Using the table of element positions, which pairing would be expected to "
        "produce a bond generally designated as covalent?",
      table=_T_ROWS,
      choices=[
        "Element B with element C, because both are nonmetals.",
        "Element A with element B, because one is a metal and one a nonmetal.",
        "Element A with element D, because both are metals.",
        "Element D with element C, because one is a metal and one a nonmetal.",
        "None of these pairings, because covalent bonding requires two atoms of the "
        "same element."],
      ans=0,
      why="EK 2.1.A.4 states that generally, bonds between a metal and nonmetal are "
          "ionic and bonds between two nonmetals are covalent. The tabulated metal or "
          "nonmetal column is what settles each pairing, and EK 2.1.A.3 makes covalent "
          "bonds between different elements ordinary rather than impossible."),

 dict(q="Two metals are combined. According to the framework's description of a metallic "
        "solid, what happens to their valence electrons?",
      table=_T_ROWS,
      choices=[
        "They become delocalized and are not associated with any individual atom.",
        "They are transferred completely from one metal to the other.",
        "They form localized shared pairs between adjacent atoms.",
        "They remain bound to their own atoms and take no part in the bonding.",
        "They are lost from the solid entirely."],
      ans=0,
      why="EK 2.1.A.5, near verbatim: in a metallic solid, the valence electrons from "
          "the metal atoms are considered to be delocalized and not associated with any "
          "individual atom. A complete transfer would make the substance ionic and a "
          "localized pair would make it covalent."),

 dict(q="Why does a bond between two elements taken from opposite sides of a period tend "
        "to be more polar than one between two elements taken from adjacent columns?",
      choices=[
        "Because electronegativity rises steadily across a period, so elements farther "
        "apart differ more, and a greater difference means a greater bond dipole.",
        "Because elements on opposite sides of a period have very different masses.",
        "Because elements on opposite sides of a period occupy different shells.",
        "Because adjacent elements cannot form bonds with each other at all.",
        "Because electronegativity falls across a period, so the far pair is closer in "
        "value."],
      ans=0,
      why="EK 2.1.A.1 gives the rise in electronegativity across a period and EK "
          "2.1.A.3.ii makes a greater difference a greater bond dipole in a single bond. "
          "Elements in one period occupy the same valence shell, which is what makes the "
          "shell-based rejected option false."),

 dict(q="Using the tabulated single bonds, rank the bond dipoles from smallest to "
        "largest.",
      table=_T_BONDS,
      choices=[
        "Bond 1, then Bond 2, then Bond 3, then Bond 4, then Bond 5.",
        "Bond 5, then Bond 4, then Bond 3, then Bond 2, then Bond 1.",
        "Bond 2, then Bond 1, then Bond 3, then Bond 5, then Bond 4.",
        "Bond 3, then Bond 1, then Bond 2, then Bond 4, then Bond 5.",
        "The five dipoles are equal, since every bond in the table involves hydrogen."],
      ans=0,
      why="EK 2.1.A.3.ii makes the dipole of a single bond grow with the difference in "
          "electronegativity, so the ranking follows the tabulated differences. Sharing "
          "one atom in common is what makes the comparison clean, not what makes the "
          "dipoles equal."),

 dict(q="An analyst measures a compound's melting point and its ability to conduct "
        "electricity when melted, and uses those results to decide how the compound is "
        "bonded. Which statement about that approach is correct?",
      table=_T_PROPERTIES,
      choices=[
        "It is the approach the framework calls best, since examining a compound's "
        "properties is the best way to characterize its bonding.",
        "It is unreliable, since only an electronegativity difference can determine "
        "bonding type.",
        "It is unnecessary, since the positions of the elements in the periodic table "
        "settle the matter completely.",
        "It is invalid, since melting point depends only on the mass of the compound.",
        "It is circular, since bonding type is defined as whatever the properties turn "
        "out to be."],
      ans=0,
      why="EK 2.1.A.4 states outright that examination of the properties of a compound "
          "is the best way to characterize the type of bonding, and in the same "
          "statement that the electronegativity difference is not the only factor. The "
          "periodic table gives a general expectation rather than a settled answer."),

 dict(q="A compound of two nonmetals is found to have a large electronegativity "
        "difference between its two elements. Which description of its bonding is most "
        "consistent with the framework?",
      choices=[
        "Strongly polar covalent, lying toward the ionic end of the continuum without "
        "being fully ionic.",
        "Purely ionic, since a large difference guarantees complete transfer.",
        "Purely nonpolar covalent, since two nonmetals always share equally.",
        "Metallic, since a large difference produces delocalized electrons.",
        "Impossible to place, since the framework offers no way to describe intermediate "
        "cases."],
      ans=0,
      why="EK 2.1.A.4 makes bonds between two nonmetals generally covalent while denying "
          "that the electronegativity difference settles the designation on its own, and "
          "EK 2.1.A.3.iii supplies the continuum along which such a bond sits. The "
          "framework describes intermediate cases explicitly."),

 dict(q="Which experimental observation would give the strongest reason to revise a "
        "prediction, based on electronegativity difference alone, that a particular "
        "compound is ionic?",
      table=_T_PROPERTIES,
      choices=[
        "The compound melts far below room temperature and does not conduct electricity "
        "when melted.",
        "The compound is a solid at room temperature.",
        "The compound contains two elements rather than three.",
        "The compound has a larger molar mass than a known ionic compound.",
        "Nothing could give such a reason, since the electronegativity difference is "
        "decisive."],
      ans=0,
      why="EK 2.1.A.4 makes examination of properties the best way to characterize "
          "bonding and denies that the electronegativity difference is the only factor, "
          "so a property that ionic compounds do not show is exactly the evidence that "
          "would force a revision. EK 3.2.A.3 supplies the properties in question."),

 dict(q="A student writes that in a polar covalent bond the more electronegative atom "
        "gains a full negative charge. Which correction is appropriate?",
      choices=[
        "The charge is partial rather than full, because the electrons are shared "
        "unequally rather than transferred.",
        "The charge is full but positive rather than negative.",
        "The charge sits on the less electronegative atom instead.",
        "There is no charge of any kind, since covalent bonds involve sharing.",
        "The student is correct, since a polar bond is simply an ionic bond by another "
        "name."],
      ans=0,
      why="EK 2.1.A.3 defines a polar covalent bond as SHARED valence electrons between "
          "atoms of unequal electronegativity, and EK 2.1.A.3.i calls the resulting "
          "charge partial. EK 2.1.A.3.iii places such a bond partway along the continuum "
          "toward ionic rather than at its end."),

 dict(q="Using the tabulated electronegativities, which of the following single bonds "
        "would be expected to have a dipole closest in size to that of a bond between "
        "carbon and oxygen?",
      table=_T_EN,
      choices=[
        "A bond between nitrogen and hydrogen.",
        "A bond between hydrogen and phosphorus.",
        "A bond between sodium and fluorine.",
        "A bond between carbon and sulfur.",
        "A bond between potassium and fluorine."],
      ans=0,
      why="EK 2.1.A.3.ii makes the size of a single bond's dipole follow the difference "
          "in electronegativity, so the closest match is the pair whose tabulated "
          "difference is nearest. Two of the rejected pairs have no difference or a very "
          "large one."),

 dict(q="What role does the shell model play in the framework's account of "
        "electronegativity?",
      choices=[
        "It is one of the ideas through which the periodic trends in electronegativity "
        "are understood qualitatively, alongside electronic structure and Coulomb's law.",
        "It defines electronegativity as the number of shells an atom has.",
        "It replaces electronegativity entirely for bonds between two nonmetals.",
        "It applies only to metallic solids, where the valence electrons are "
        "delocalized.",
        "It plays no part, since electronegativity is a purely experimental quantity "
        "with no model behind it."],
      ans=0,
      why="EK 2.1.A.1 states that the electronegativity trends can be understood "
          "qualitatively through the electronic structure of the atoms, the shell model, "
          "and Coulomb's law. That is an explanatory role rather than a definition, and "
          "it is not restricted to any one class of substance."),

 dict(q="Which observation about a solid would be best explained by the framework's "
        "model of metallic bonding?",
      choices=[
        "Electrons move through the solid without belonging to any one atom.",
        "Each atom holds its electrons in localized pairs with a single neighbor.",
        "The solid is made of separate positive and negative ions in fixed positions.",
        "The solid contains discrete molecules held together only weakly.",
        "The solid contains no valence electrons at all."],
      ans=0,
      why="EK 2.1.A.5 states that in a metallic solid the valence electrons from the "
          "metal atoms are considered to be delocalized and not associated with any "
          "individual atom, which is exactly what an observation of electrons not "
          "belonging to any one atom would show."),
]
