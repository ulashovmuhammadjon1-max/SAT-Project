r"""AP CHEMISTRY 2.7 VSEPR and Hybridization.

CED effective Fall 2024, Unit 2 Compound Structure and Properties.
Learning objective 2.7.A: based on the relationship between Lewis diagrams,
VSEPR theory, bond orders and bond polarities, (i) explain structural properties
of molecules and (ii) explain electron properties of molecules.
Suggested skill 6.C, support a claim with evidence from representations or
models at the particulate level.

Essential knowledge relied on, in the framework's own words:

  2.7.A.1  VSEPR theory uses the Coulombic repulsion between electrons as a
           basis for predicting the arrangement of electron pairs around a
           central atom.
  2.7.A.2  Both Lewis diagrams and VSEPR theory must be used for predicting
           electronic and structural properties of many covalently bonded
           molecules and polyatomic ions, including the following:
             i.   Molecular geometry (linear, trigonal planar, tetrahedral,
                  trigonal pyramidal, bent, trigonal bipyramidal, seesaw,
                  T-shaped, octahedral, square pyramidal, square planar)
             ii.  Bond angles
             iii. Relative bond energies based on bond order
             iv.  Relative bond lengths (multiple bonds, effects of atomic
                  radius)
             v.   Presence of a dipole moment
             vi.  Hybridization of valence orbitals for atoms within a molecule
                  or polyatomic ion
  2.7.A.3  The terms "hybridization" and "hybrid atomic orbital" are used to
           describe the arrangement of electrons around a central atom. When the
           central atom is sp hybridized, its ideal bond angles are 180 degrees;
           for sp2 hybridized atoms the bond angles are 120 degrees; and for sp3
           hybridized atoms the bond angles are 109.5 degrees.
  2.7.A.4  Bond formation is associated with overlap between atomic orbitals. In
           multiple bonds, such overlap leads to the formation of both sigma and
           pi bonds. The overlap is stronger in sigma than pi bonds, which is
           reflected in sigma bonds having greater bond energy than pi bonds.
           The presence of a pi bond also prevents the rotation of the bond and
           leads to geometric isomers.

  Exclusion Statements, all three of them, verbatim in substance:
    * An understanding of the derivation and depiction of hybrid orbitals will
      not be assessed. The course DOES include the distinction between sigma and
      pi bonding, the use of VSEPR to explain the shapes of molecules, and the
      sp, sp2 and sp3 nomenclature.
    * Hybridization involving d orbitals will not be assessed. When an atom has
      more than four pairs of electrons surrounding the central atom, students
      are only responsible for the shape of the resulting molecule.
    * Molecular orbital theory will not be assessed: neither molecular orbital
      diagrams, nor filling of molecular orbitals, nor the distinction between
      bonding, nonbonding and antibonding orbitals.

WHAT THIS MODULE KEYS AND WHAT IT REFUSES TO. EK 2.7.A.3 is the one place in
unit 2 where the framework prints a numerical correspondence, so the
hybridization-to-angle mapping carries eleven items and every one of them is
recomputed in verify_h2_7.py against that sentence. The framework does NOT
anywhere state how many regions of electron density give which hybridization,
nor which count of bonding and lone pairs gives which geometry name, so no key
here asserts either. Where an item needs a hybridization it is stated in the
stem, exactly as EK 2.7.A.3 itself supplies one.

The four exclusion statements are keyed as content, not merely obeyed: a student
who knows that d-orbital hybridization and molecular orbital diagrams are off
the exam, and that the sigma/pi distinction and the sp nomenclature are on it,
is better prepared, and those are sentences the CED prints.

NO FIGURES. Nothing here refers to a drawn molecule. Where several central atoms
are compared, their hybridizations are tabulated and the question is asked of
the table.

NOTATION. The hybridization labels are the one place this module needs
typesetting, because a superscript is the difference between two of them:
\( sp^{2} \) and \( sp^{3} \) are hand-written spans, and every choice carries a
following word so that no shorter label is a substring of a longer one. Angles
are written out as "120 degrees" rather than with a degree glyph, which would
print raw outside a span.
"""
TOPIC = ("2.7", "VSEPR and Hybridization", 2)

_T_HYBRID_MIX = dict(
    headers=["Central atom", "Hybridization stated", "Ideal bond angle stated"],
    rows=[["Atom P", r"\( sp \)", "180 degrees"],
          ["Atom Q", r"\( sp^{2} \)", "120 degrees"],
          ["Atom R", r"\( sp^{3} \)", "109.5 degrees"],
          ["Atom S", r"\( sp^{2} \)", "109.5 degrees"]])

_T_HYBRID_OK = dict(
    headers=["Central atom", "Hybridization stated"],
    rows=[["Atom T", r"\( sp^{3} \)"],
          ["Atom U", r"\( sp \)"],
          ["Atom V", r"\( sp^{2} \)"]])

QUESTIONS = [

 dict(q="On what does VSEPR theory base its predictions, according to the framework?",
      choices=[
        "The Coulombic repulsion between electrons",
        "The attraction between the nuclei of neighboring atoms",
        "The difference in mass between the central atom and its neighbors",
        "The temperature at which the molecule is studied",
        "The number of core electrons on the central atom"],
      ans=0,
      why="EK 2.7.A.1, verbatim: VSEPR theory uses the Coulombic repulsion between "
          "electrons as a basis for predicting the arrangement of electron pairs around a "
          "central atom. Nothing about mass or temperature enters that sentence."),

 dict(q="What does VSEPR theory predict, in the framework's own terms?",
      choices=[
        "The arrangement of electron pairs around a central atom",
        "The number of valence electrons each atom contributes",
        "The rate at which a molecule reacts",
        "Which of two atoms is more electronegative",
        "The mass of one mole of the molecule"],
      ans=0,
      why="EK 2.7.A.1 names exactly this as what the theory predicts: the arrangement of "
          "electron pairs around a central atom. Counting the contributed valence "
          "electrons is the Lewis diagram's job under EK 2.5.A.1, before VSEPR is applied."),

 dict(q="Which does the framework say must be used to predict the electronic and "
        "structural properties of a covalently bonded molecule?",
      choices=[
        "Both Lewis diagrams and VSEPR theory",
        "Lewis diagrams alone, since they already show every valence electron",
        "VSEPR theory alone, since it already accounts for repulsion",
        "Neither; such properties can only be measured, never predicted",
        "Coulomb's law alone, applied to the nuclei"],
      ans=0,
      why="EK 2.7.A.2, verbatim: both Lewis diagrams and VSEPR theory must be used for "
          "predicting electronic and structural properties of many covalently bonded "
          "molecules and polyatomic ions. The framework makes neither one sufficient by "
          "itself."),

 dict(q="A central atom is \\( sp \\) hybridized. What does the framework give as its "
        "ideal bond angles?",
      choices=["180 degrees", "120 degrees", "109.5 degrees", "90 degrees", "60 degrees"],
      ans=0,
      why="EK 2.7.A.3 states the correspondence directly: when the central atom is sp "
          "hybridized, its ideal bond angles are 180 degrees. The other two values the "
          "framework prints belong to the other two hybridizations it names."),

 dict(q="A central atom is \\( sp^{2} \\) hybridized. What does the framework give as its "
        "ideal bond angles?",
      choices=["120 degrees", "180 degrees", "109.5 degrees", "90 degrees", "60 degrees"],
      ans=0,
      why="EK 2.7.A.3 states it directly: for sp2 hybridized atoms the bond angles are 120 "
          "degrees. Each rejected value is either one of the other two angles the "
          "framework prints or an angle it never mentions."),

 dict(q="A central atom is \\( sp^{3} \\) hybridized. What does the framework give as its "
        "ideal bond angles?",
      choices=["109.5 degrees", "120 degrees", "180 degrees", "90 degrees", "104.5 degrees"],
      ans=0,
      why="EK 2.7.A.3 states it directly: for sp3 hybridized atoms the bond angles are "
          "109.5 degrees. The framework prints exactly three angles, and the two rejected "
          "values closest to the key are the other two of them."),

 dict(q="The ideal bond angles about a central atom are 109.5 degrees. Which "
        "hybridization does the framework associate with that value?",
      choices=[
        "The central atom is \\( sp^{3} \\) hybridized",
        "The central atom is \\( sp^{2} \\) hybridized",
        "The central atom is \\( sp \\) hybridized",
        "The hybridization cannot be named from a bond angle",
        "The central atom is not hybridized at all"],
      ans=0,
      why="EK 2.7.A.3 pairs 109.5 degrees with sp3 hybridization, and since it assigns a "
          "different angle to each of the three hybridizations it names, the "
          "correspondence runs in both directions for those three."),

 dict(q="The ideal bond angles about a central atom are 180 degrees. Which hybridization "
        "does the framework associate with that value?",
      choices=[
        "The central atom is \\( sp \\) hybridized",
        "The central atom is \\( sp^{2} \\) hybridized",
        "The central atom is \\( sp^{3} \\) hybridized",
        "The hybridization cannot be named from a bond angle",
        "The central atom has no hybrid orbitals"],
      ans=0,
      why="EK 2.7.A.3 pairs 180 degrees with sp hybridization. The three angles the "
          "framework prints are all different, so naming one of them fixes which of the "
          "three hybridizations is meant."),

 dict(q="The ideal bond angles about a central atom are 120 degrees. Which hybridization "
        "does the framework associate with that value?",
      choices=[
        "The central atom is \\( sp^{2} \\) hybridized",
        "The central atom is \\( sp \\) hybridized",
        "The central atom is \\( sp^{3} \\) hybridized",
        "The hybridization cannot be named from a bond angle",
        "The central atom is hybridized only if it carries a lone pair"],
      ans=0,
      why="EK 2.7.A.3 pairs 120 degrees with sp2 hybridization. The framework attaches an "
          "angle to each of the three hybridizations it names, and makes no exception for "
          "whether the atom carries a lone pair."),

 dict(q="Four central atoms are tabulated with a stated hybridization and a stated ideal "
        "bond angle. Which row is inconsistent with the framework?",
      table=_T_HYBRID_MIX,
      choices=["Atom S", "Atom P", "Atom Q", "Atom R",
               "None of them; all four pairings are consistent"],
      ans=0,
      why="EK 2.7.A.3 fixes each of the three pairings: sp with 180 degrees, sp2 with 120 "
          "degrees and sp3 with 109.5 degrees. Exactly one tabulated row pairs a "
          "hybridization with an angle the framework assigns to a different one."),

 dict(q="Three central atoms are tabulated with their hybridizations. Which has the "
        "largest ideal bond angle?",
      table=_T_HYBRID_OK,
      choices=["Atom U", "Atom T", "Atom V",
               "They are equal, since ideal bond angles do not depend on hybridization",
               "It cannot be told without knowing how many lone pairs each atom carries"],
      ans=0,
      why="EK 2.7.A.3 attaches 180, 120 and 109.5 degrees to sp, sp2 and sp3 respectively, "
          "so the tabulated hybridizations are enough to order the angles. The framework "
          "makes the ideal angle a function of the hybridization alone."),

 dict(q="Among those same three tabulated atoms, which has the smallest ideal bond angle?",
      table=_T_HYBRID_OK,
      choices=["Atom T", "Atom U", "Atom V",
               "They are equal, since every central atom has the same ideal angle",
               "It cannot be told without knowing which elements are involved"],
      ans=0,
      why="EK 2.7.A.3 gives sp3 the smallest of the three angles it prints, 109.5 degrees, "
          "against 120 for sp2 and 180 for sp. The elements involved do not enter that "
          "sentence at all."),

 dict(q="What do the terms hybridization and hybrid atomic orbital describe, according to "
        "the framework?",
      choices=[
        "The arrangement of electrons around a central atom",
        "The mass distribution within a molecule",
        "The rate at which a bond forms",
        "The number of protons in the central nucleus",
        "The energy released when a molecule condenses"],
      ans=0,
      why="EK 2.7.A.3 opens by saying that the terms hybridization and hybrid atomic "
          "orbital are used to describe the arrangement of electrons around a central "
          "atom. Nothing about mass, rate or nuclear composition appears in that "
          "statement."),

 dict(q="With what does the framework associate bond formation?",
      choices=[
        "Overlap between atomic orbitals",
        "Complete transfer of an electron from one atom to another",
        "The collision of two nuclei",
        "The delocalization of valence electrons through a solid",
        "The alignment of two permanent dipoles"],
      ans=0,
      why="EK 2.7.A.4, verbatim: bond formation is associated with overlap between atomic "
          "orbitals. Complete transfer describes ionic bonding under EK 2.1.A.4 and "
          "delocalization describes metallic bonding under EK 2.4.A.1, neither of which is "
          "what this statement is about."),

 dict(q="What does the framework say the orbital overlap in a multiple bond produces?",
      choices=[
        "Both sigma and pi bonds",
        "Sigma bonds only, however many pairs are shared",
        "Pi bonds only, since the sigma framework is already complete",
        "Neither kind, since a multiple bond is a single region of overlap",
        "Delocalized electrons shared over the whole molecule"],
      ans=0,
      why="EK 2.7.A.4, verbatim: in multiple bonds, such overlap leads to the formation of "
          "both sigma and pi bonds. The framework does not describe a multiple bond as a "
          "single undifferentiated region."),

 dict(q="How do the bond energies of sigma and pi bonds compare, according to the "
        "framework?",
      choices=[
        "Sigma bonds have greater bond energy than pi bonds",
        "Pi bonds have greater bond energy than sigma bonds",
        "The two are equal, since both arise from orbital overlap",
        "The comparison depends on which elements are bonded",
        "Neither kind has a bond energy, since only whole bonds do"],
      ans=0,
      why="EK 2.7.A.4 states it in those words: the overlap is stronger in sigma than pi "
          "bonds, which is reflected in sigma bonds having greater bond energy than pi "
          "bonds. The framework attaches no dependence on the elements involved to that "
          "comparison."),

 dict(q="What reason does the framework give for the difference in bond energy between "
        "sigma and pi bonds?",
      choices=[
        "The overlap is stronger in sigma bonds than in pi bonds",
        "Sigma bonds join heavier atoms than pi bonds do",
        "Pi bonds contain fewer electrons than sigma bonds do",
        "Sigma bonds form at higher temperatures than pi bonds",
        "Pi bonds are longer than sigma bonds"],
      ans=0,
      why="EK 2.7.A.4 gives the reason and the consequence in one sentence: the overlap is "
          "stronger in sigma than pi bonds, which is REFLECTED IN sigma bonds having "
          "greater bond energy. The framework offers no explanation resting on mass, "
          "temperature or electron count."),

 dict(q="What does the framework say the presence of a pi bond prevents?",
      choices=[
        "Rotation of the bond",
        "Any further bonding to either atom",
        "The molecule from having a dipole moment",
        "The atoms from being of different elements",
        "The bond from having any bond energy at all"],
      ans=0,
      why="EK 2.7.A.4 states it directly: the presence of a pi bond also prevents the "
          "rotation of the bond. The framework attaches no other prohibition to a pi bond "
          "in that sentence."),

 dict(q="What does the framework say follows from a pi bond preventing rotation?",
      choices=[
        "It leads to geometric isomers",
        "It leads to a higher melting point in every case",
        "It leads to the loss of the sigma bond",
        "It leads to a molecule with no dipole moment",
        "It leads to an odd number of valence electrons"],
      ans=0,
      why="EK 2.7.A.4 states the consequence in those words: the presence of a pi bond also "
          "prevents the rotation of the bond and leads to geometric isomers. No other "
          "consequence is attached to it there."),

 dict(q="Which of these does the framework's exclusion statement place outside what the AP "
        "Exam assesses?",
      choices=[
        "The derivation and depiction of hybrid orbitals",
        "The distinction between sigma and pi bonding",
        "The use of VSEPR to explain the shapes of molecules",
        "The sp, sp2 and sp3 nomenclature",
        "The ideal bond angle associated with an sp3 hybridized atom"],
      ans=0,
      why="The exclusion statement attached to LO 2.7.A says an understanding of the "
          "derivation and depiction of hybrid orbitals will not be assessed, and then names "
          "the three things the course DOES include, which are three of the rejected "
          "options; the fourth is EK 2.7.A.3 itself."),

 dict(q="The same exclusion statement names three things the course does include. Which "
        "are they?",
      choices=[
        "The sigma and pi distinction, the use of VSEPR to explain shapes, and the sp, sp2 "
        "and sp3 nomenclature",
        "The derivation of hybrid orbitals, their depiction, and their energies",
        "Molecular orbital diagrams, orbital filling, and antibonding orbitals",
        "Crystal structures, unit cells, and packing arrangements",
        "The masses of the atoms, their radii, and their electron configurations"],
      ans=0,
      why="The exclusion statement lists them in exactly those words: the course includes "
          "the distinction between sigma and pi bonding, the use of VSEPR to explain the "
          "shapes of molecules, and the sp, sp2 and sp3 nomenclature. The other options "
          "name material the framework excludes or assigns to other units."),

 dict(q="An atom has more than four pairs of electrons surrounding it. What does the "
        "framework hold students responsible for in that case?",
      choices=[
        "Only the shape of the resulting molecule",
        "The shape and the hybridization, including the d orbitals involved",
        "Nothing at all; such molecules are entirely outside the course",
        "The molecular orbital diagram of the whole molecule",
        "The exact bond angles, to one decimal place"],
      ans=0,
      why="The exclusion statement says that when an atom has more than four pairs of "
          "electrons surrounding the central atom, students are only responsible for the "
          "shape of the resulting molecule, and the same statement puts hybridization "
          "involving d orbitals outside the exam."),

 dict(q="Which does the framework's exclusion statement about molecular orbital theory "
        "place outside the exam?",
      choices=[
        "The distinction between bonding, nonbonding and antibonding orbitals",
        "The distinction between sigma and pi bonding",
        "The use of VSEPR to explain molecular shapes",
        "The ideal bond angle of an sp2 hybridized atom",
        "The claim that bond formation involves orbital overlap"],
      ans=0,
      why="The exclusion statement says the AP Exam will neither explicitly assess "
          "molecular orbital diagrams, nor filling of molecular orbitals, nor the "
          "distinction between bonding, nonbonding and antibonding orbitals. The sigma and "
          "pi distinction is explicitly INCLUDED by the other exclusion statement."),

 dict(q="Which of the following is among the properties the framework lists as predicted "
        "using Lewis diagrams together with VSEPR theory?",
      choices=[
        "The presence of a dipole moment",
        "The rate at which the molecule reacts",
        "The mass of one mole of the substance",
        "The number of neutrons in each nucleus",
        "The temperature at which the substance boils"],
      ans=0,
      why="EK 2.7.A.2 lists molecular geometry, bond angles, relative bond energies based "
          "on bond order, relative bond lengths, the presence of a dipole moment, and "
          "hybridization of valence orbitals. Reaction rate, molar mass and boiling point "
          "are not on that list."),

 dict(q="Which further property does EK 2.7.A.2's list include?",
      choices=[
        "Relative bond energies based on bond order",
        "The absolute bond energy in kilojoules per mole",
        "The percentage of molecules that are ionized",
        "The number of moles of gas produced on decomposition",
        "The color of the substance in the solid state"],
      ans=0,
      why="EK 2.7.A.2 names relative bond energies BASED ON BOND ORDER as one of the "
          "properties, alongside relative bond lengths, which it qualifies with multiple "
          "bonds and effects of atomic radius. The framework's list is relative "
          "throughout, never absolute."),

 dict(q="Which of the following is NOT among the molecular geometries the framework names?",
      choices=["Trigonal prismatic", "Seesaw", "T-shaped", "Square pyramidal",
               "Trigonal bipyramidal"],
      ans=0,
      why="EK 2.7.A.2 lists the geometries by name: linear, trigonal planar, tetrahedral, "
          "trigonal pyramidal, bent, trigonal bipyramidal, seesaw, T-shaped, octahedral, "
          "square pyramidal and square planar. Four of the options appear on that list and "
          "one does not."),

 dict(q="Hybridization involving which orbitals does the framework place outside the exam?",
      choices=["d orbitals", "s orbitals only", "p orbitals only",
               "The s and p orbitals together", "No orbitals at all are excluded"],
      ans=0,
      why="The exclusion statement says hybridization involving d orbitals will not be "
          "assessed on the AP Exam, while EK 2.7.A.3's sp, sp2 and sp3 nomenclature, built "
          "from s and p orbitals, is exactly what the course does include."),

 dict(q="In ethene, C2H4, each carbon atom is \\( sp^{2} \\) hybridized. According to the "
        "framework, the bond angles about such a carbon are closest to which value?",
      choices=["120 degrees", "90 degrees", "109.5 degrees", "180 degrees", "60 degrees"],
      ans=0,
      why="EK 2.7.A.3 gives 120 degrees as the ideal bond angle for an sp2 hybridized atom, "
          "and the framework's own sample multiple-choice question asks exactly this about "
          "this molecule. The other two angles the framework prints belong to the other two "
          "hybridizations."),

 dict(q="Of the three tabulated central atoms, which two differ in ideal bond angle by "
        "exactly sixty degrees?",
      table=_T_HYBRID_OK,
      choices=["Atom U and Atom V", "Atom T and Atom U", "Atom T and Atom V",
               "No two of them differ by exactly sixty degrees",
               "All three pairs differ by exactly sixty degrees"],
      ans=0,
      why="EK 2.7.A.3 attaches 180, 120 and 109.5 degrees to sp, sp2 and sp3, so the three "
          "pairwise differences follow from the tabulated hybridizations alone. Only one of "
          "those differences is exactly sixty degrees."),

 dict(q="One molecule has an \\( sp \\) hybridized central atom and another has an "
        "\\( sp^{3} \\) hybridized central atom. By how many degrees do their ideal bond "
        "angles differ?",
      choices=["70.5 degrees", "60 degrees", "10.5 degrees", "80 degrees", "45 degrees"],
      ans=0,
      why="EK 2.7.A.3 gives 180 degrees for an sp hybridized atom and 109.5 degrees for an "
          "sp3 hybridized one, and the difference between those two printed values is what "
          "the question asks for. The difference between the other two printed angles is a "
          "rejected value."),
]
