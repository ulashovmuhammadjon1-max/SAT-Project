r"""AP CHEMISTRY 3.1 Intermolecular and Interparticle Forces.

CED effective Fall 2024, Unit 3 Properties of Substances and Mixtures.
Learning objective 3.1.A: explain the relationship between the chemical
structures of molecules and the relative strength of their intermolecular
forces when (i) the molecules are of the same chemical species and (ii) the
molecules are of two different chemical species.
Suggested skill 4.D, explain the degree to which a model or representation
describes the connection between particulate-level and macroscopic properties.

Essential knowledge relied on, in the framework's own words:

  3.1.A.1  London dispersion forces are a result of the Coulombic interactions
           between temporary, fluctuating dipoles. London dispersion forces are
           often the strongest net intermolecular force between large molecules.
             iii. The term "London dispersion forces" should not be used
                  synonymously with the term "van der Waals forces."
  3.1.A.2  The dipole moment of a polar molecule leads to additional
           interactions with other chemical species.
             ii. Dipole-dipole interactions are present between polar molecules.
                 The interaction strength depends on the magnitudes of the
                 dipoles and their relative orientation. Interactions between
                 polar molecules are typically greater than those between
                 nonpolar molecules of comparable size because these
                 interactions act in addition to London dispersion forces.
             iii. Ion-dipole forces of attraction are present between ions and
                  polar molecules. These tend to be stronger than dipole-dipole
                  forces.
  3.1.A.3  The relative strength and orientation dependence of dipole-dipole and
           ion-dipole forces can be understood qualitatively by considering the
           sign of the partial charges responsible for the molecular dipole
           moment, and how these partial charges interact with an ion or with an
           adjacent dipole.
  3.1.A.4  Hydrogen bonding is a strong type of intermolecular interaction that
           exists when hydrogen atoms covalently bonded to the highly
           electronegative atoms (N, O, and F) are attracted to the negative end
           of a dipole formed by the electronegative atom (N, O, and F) in a
           different molecule, or a different part of the same molecule.
  3.1.A.5  In large biomolecules, noncovalent interactions may occur between
           different molecules or between different regions of the same large
           biomolecule.

A HOLE IN THE SOURCE, AND WHAT IS DONE ABOUT IT. Three sub-points are absent
from the CED PDF's text layer: 3.1.A.1's sub-points i and ii, and 3.1.A.2's
sub-point i. The page prints 3.1.A.1's lead sentence, then blank space, then a
bare "iii." with the van der Waals warning; and the next page opens with a
sub-point whose numeral is gone, followed by "iii. Ion-dipole". Both pdftotext
modes agree, and the word "polarizability" does not occur anywhere in the whole
dump. This is the same kind of unrecoverable gap SCIENCE_RESUME.md records for
the Biology exocytosis statement, and it is handled the same way: NOTHING here
is keyed to what those sub-points probably said. No item claims that dispersion
forces are present in every substance, that they grow with molar mass or with
polarizability, or that they are the only force between nonpolar molecules --
those are standard teaching, and this source does not contain them.
``no_missing_subpoint_material`` in the verifier asserts that the hole stays
unfilled.

THE ONLY THREE COMPARISONS THE FRAMEWORK MAKES are: ion-dipole TENDS to be
stronger than dipole-dipole; interactions between polar molecules are TYPICALLY
greater than those between nonpolar molecules of comparable size, BECAUSE they
act in addition to London dispersion forces; and dispersion forces are OFTEN the
strongest net force between large molecules. Notice that all three are hedged,
and that hydrogen bonding is never ranked against anything -- EK 3.1.A.4 calls
it "a strong type" and stops. Item 25 keys on exactly that silence, and
``no_unstated_ranking`` asserts no key ranks hydrogen bonding against another
named force.

WHAT IS NOT HERE. Melting points, boiling points and vapor pressures are EK
3.2.A.1 and belong to topic 3.2; solubility and miscibility are EK 3.10.A.1 and
belong to topic 3.10.

NO FIGURES. Interacting species are described in words or tabulated by type.

NOTATION. Plain prose throughout; element symbols in prose stay plain text. No
math spans are needed in this module.
"""
TOPIC = ("3.1", "Intermolecular and Interparticle Forces", 3)

_T_PAIRS = dict(
    headers=["Pair", "First species", "Second species"],
    rows=[["Pair 1", "an ion", "a polar molecule"],
          ["Pair 2", "a polar molecule", "a polar molecule"],
          ["Pair 3", "a nonpolar molecule", "a nonpolar molecule"],
          ["Pair 4", "an ion", "an ion"]])

_T_SIZE = dict(
    headers=["Substance", "Polarity of its molecules", "Molecular size"],
    rows=[["Substance J", "polar", "comparable to that of Substance K"],
          ["Substance K", "nonpolar", "comparable to that of Substance J"]])

QUESTIONS = [

 dict(q="What does the framework say London dispersion forces result from?",
      choices=[
        "Coulombic interactions between temporary, fluctuating dipoles",
        "Coulombic interactions between the permanent dipoles of polar molecules",
        "The sharing of valence electrons between two molecules",
        "The transfer of an electron from one molecule to another",
        "The overlap of atomic orbitals on neighboring molecules"],
      ans=0,
      why="EK 3.1.A.1, verbatim: London dispersion forces are a result of the Coulombic "
          "interactions between temporary, fluctuating dipoles. The dipole moment of a "
          "polar molecule is what EK 3.1.A.2 treats separately, and sharing or "
          "transferring electrons is bonding rather than an intermolecular force."),

 dict(q="What does the framework say about London dispersion forces between large "
        "molecules?",
      choices=[
        "They are often the strongest net intermolecular force between such molecules",
        "They are always negligible compared with every other intermolecular force",
        "They are absent, since large molecules interact only through their dipoles",
        "They are always exactly equal to the dipole-dipole interaction",
        "They act only between molecules of two different chemical species"],
      ans=0,
      why="EK 3.1.A.1 states it in those words: London dispersion forces are OFTEN the "
          "strongest net intermolecular force between large molecules. The framework "
          "hedges with often rather than always, and makes no claim that they vanish for "
          "any class of molecule."),

 dict(q="What does the framework say about the terms London dispersion forces and van der "
        "Waals forces?",
      choices=[
        "The two terms should not be used synonymously",
        "The two terms mean exactly the same thing and may be interchanged",
        "The term van der Waals forces should replace London dispersion forces entirely",
        "Neither term should be used in the course",
        "The two terms differ only in the language they come from"],
      ans=0,
      why="EK 3.1.A.1's third sub-point says exactly this: the term London dispersion "
          "forces should not be used synonymously with the term van der Waals forces. "
          "Treating them as interchangeable is the usage the framework specifically warns "
          "against."),

 dict(q="What does the framework say the dipole moment of a polar molecule leads to?",
      choices=[
        "Additional interactions with other chemical species",
        "The complete loss of any dispersion interaction",
        "A covalent bond to any neighboring molecule",
        "An equal and opposite dipole in every neighbor",
        "The molecule becoming an ion"],
      ans=0,
      why="EK 3.1.A.2, verbatim: the dipole moment of a polar molecule leads to additional "
          "interactions with other chemical species. The word additional is the point: the "
          "dipole adds interactions rather than replacing what was already there."),

 dict(q="Between which species does the framework say dipole-dipole interactions are "
        "present?",
      choices=[
        "Between polar molecules",
        "Between nonpolar molecules",
        "Between ions and nonpolar molecules",
        "Between the atoms within a single molecule",
        "Between any two molecules whatever their structure"],
      ans=0,
      why="EK 3.1.A.2's second sub-point states it directly: dipole-dipole interactions are "
          "present between polar molecules. Interactions within a single molecule are "
          "intramolecular and belong to topic 2.2, not to this one."),

 dict(q="On what does the framework say the strength of a dipole-dipole interaction "
        "depends?",
      choices=[
        "On the magnitudes of the dipoles and on their relative orientation",
        "On the magnitudes of the dipoles alone, orientation being irrelevant",
        "On their relative orientation alone, the magnitudes being irrelevant",
        "On the masses of the two molecules",
        "On the number of atoms in each molecule"],
      ans=0,
      why="EK 3.1.A.2's second sub-point names both: the interaction strength depends on "
          "the magnitudes of the dipoles and their relative orientation. Dropping either "
          "half is what makes two of the rejected options wrong."),

 dict(q="The framework says interactions between polar molecules are typically greater "
        "than those between nonpolar molecules of comparable size. What reason does it "
        "give?",
      choices=[
        "Because these interactions act in addition to London dispersion forces",
        "Because London dispersion forces are absent between polar molecules",
        "Because polar molecules are always the larger of the two",
        "Because polar molecules carry a full charge rather than a partial one",
        "Because nonpolar molecules have no electrons available to interact"],
      ans=0,
      why="EK 3.1.A.2's second sub-point gives the reason in those words: because these "
          "interactions act IN ADDITION TO London dispersion forces. That is an addition "
          "rather than a substitution, which is what the second rejected option gets "
          "backwards."),

 dict(q="Between which species does the framework say ion-dipole forces of attraction are "
        "present?",
      choices=[
        "Between ions and polar molecules",
        "Between ions and nonpolar molecules",
        "Between two polar molecules",
        "Between two ions of opposite charge",
        "Between the two ends of a single polar molecule"],
      ans=0,
      why="EK 3.1.A.2's third sub-point states it directly: ion-dipole forces of attraction "
          "are present between ions and polar molecules. The attraction between two ions is "
          "EK 2.2.A.3's Coulombic case and is not called an ion-dipole force."),

 dict(q="How does the framework compare ion-dipole forces with dipole-dipole forces?",
      choices=[
        "Ion-dipole forces tend to be the stronger of the two",
        "Dipole-dipole forces tend to be the stronger of the two",
        "The two are always exactly equal in strength",
        "The comparison depends entirely on temperature",
        "The framework makes no comparison between them"],
      ans=0,
      why="EK 3.1.A.2's third sub-point says ion-dipole forces tend to be stronger than "
          "dipole-dipole forces. The framework does make this comparison, and it hedges it "
          "with tend rather than stating it as invariable."),

 dict(q="How does the framework say the relative strength and orientation dependence of "
        "dipole-dipole and ion-dipole forces can be understood?",
      choices=[
        "Qualitatively, by considering the sign of the partial charges responsible for the "
        "molecular dipole moment",
        "Quantitatively, by calculating the interaction energy in kilojoules per mole",
        "By measuring the boiling point of each substance involved",
        "By counting the valence electrons on the central atom",
        "By writing the electron configuration of every atom present"],
      ans=0,
      why="EK 3.1.A.3 says the relative strength and orientation dependence can be "
          "understood QUALITATIVELY by considering the sign of the partial charges "
          "responsible for the molecular dipole moment. The framework asks for a "
          "qualitative account here rather than a calculated energy."),

 dict(q="To which atoms must a hydrogen be covalently bonded for the framework's "
        "definition of hydrogen bonding to apply?",
      choices=[
        "Nitrogen, oxygen or fluorine",
        "Carbon, nitrogen or oxygen",
        "Any nonmetal at all",
        "Chlorine, bromine or iodine",
        "Any atom more electronegative than hydrogen"],
      ans=0,
      why="EK 3.1.A.4 names the three atoms explicitly, twice: hydrogen atoms covalently "
          "bonded to the highly electronegative atoms N, O and F. The framework's "
          "definition is a list of three elements rather than a general rule about "
          "electronegativity."),

 dict(q="In the framework's definition of hydrogen bonding, what is the hydrogen atom "
        "attracted to?",
      choices=[
        "The negative end of a dipole formed by a nitrogen, oxygen or fluorine atom",
        "The positive end of a dipole formed by a nitrogen, oxygen or fluorine atom",
        "The nucleus of a neighboring hydrogen atom",
        "A free electron travelling between the molecules",
        "The delocalized electrons of a metallic solid"],
      ans=0,
      why="EK 3.1.A.4 states it in those words: the hydrogen atoms are attracted to the "
          "NEGATIVE end of a dipole formed by the electronegative atom N, O or F. A "
          "hydrogen carrying a partial positive charge is drawn to the negative end, so "
          "swapping the sign reverses the interaction."),

 dict(q="Where does the framework say the electronegative atom attracting the hydrogen may "
        "be found?",
      choices=[
        "In a different molecule, or in a different part of the same molecule",
        "In a different molecule only",
        "In the same molecule only",
        "In a neighboring ionic solid only",
        "In the surrounding solvent only"],
      ans=0,
      why="EK 3.1.A.4 allows both cases in its own sentence: in a different molecule, or a "
          "different part of the same molecule. Restricting the definition to either case "
          "alone drops half of what the framework states."),

 dict(q="How does the framework describe hydrogen bonding?",
      choices=[
        "As a strong type of intermolecular interaction",
        "As a type of covalent bond between two molecules",
        "As a weak form of ionic bonding",
        "As the transfer of a hydrogen nucleus between molecules",
        "As a form of metallic bonding involving hydrogen"],
      ans=0,
      why="EK 3.1.A.4 opens by calling hydrogen bonding a strong type of INTERMOLECULAR "
          "interaction, which places it among the forces between molecules rather than "
          "among the bonds within them. The hydrogen involved stays covalently bonded to "
          "its own N, O or F."),

 dict(q="What does the framework say about noncovalent interactions in large biomolecules?",
      choices=[
        "They may occur between different molecules or between different regions of the "
        "same large biomolecule",
        "They occur only between two separate biomolecules",
        "They occur only within a single biomolecule",
        "They do not occur in biomolecules, which are held together by covalent bonds alone",
        "They occur only when the biomolecule carries an overall charge"],
      ans=0,
      why="EK 3.1.A.5 states both cases: in large biomolecules, noncovalent interactions "
          "may occur between different molecules or between different regions of the same "
          "large biomolecule. Restricting it to either case alone drops half the "
          "statement."),

 dict(q="Four pairs of interacting species are tabulated by type. In which pair does the "
        "framework say ion-dipole forces are present?",
      table=_T_PAIRS,
      choices=["Pair 1", "Pair 2", "Pair 3", "Pair 4",
               "In none of them, since ion-dipole forces act only within a molecule"],
      ans=0,
      why="EK 3.1.A.2's third sub-point places ion-dipole forces between ions and polar "
          "molecules, and exactly one tabulated pair puts an ion with a polar molecule. Two "
          "ions together are EK 2.2.A.3's case rather than an ion-dipole one."),

 dict(q="Using the same four tabulated pairs, in which does the framework say dipole-dipole "
        "interactions are present?",
      table=_T_PAIRS,
      choices=["Pair 2", "Pair 1", "Pair 3", "Pair 4",
               "In all four, since every species has some dipole"],
      ans=0,
      why="EK 3.1.A.2's second sub-point places dipole-dipole interactions between polar "
          "molecules, and exactly one tabulated pair puts two polar molecules together. A "
          "pair containing an ion or a nonpolar molecule is not the case that sub-point "
          "describes."),

 dict(q="Of the two tabulated pairs for which the framework names a force, which does it "
        "say tends to have the stronger interaction?",
      table=_T_PAIRS,
      choices=["Pair 1", "Pair 2", "Pair 3", "Pair 4",
               "The framework makes no comparison between the two"],
      ans=0,
      why="EK 3.1.A.2's third sub-point says ion-dipole forces tend to be stronger than "
          "dipole-dipole forces, so the pair carrying the ion-dipole force is the stronger "
          "of the two named cases. This is one of the few comparisons the framework "
          "actually makes."),

 dict(q="For how many of the four tabulated pairs does the framework name neither a "
        "dipole-dipole nor an ion-dipole force?",
      table=_T_PAIRS,
      choices=["Exactly two", "Exactly one", "Exactly three", "All four", "None of them"],
      ans=0,
      why="EK 3.1.A.2 places dipole-dipole interactions between polar molecules and "
          "ion-dipole forces between ions and polar molecules, so a pair with no polar "
          "molecule in it falls under neither sub-point. Counting the tabulated pairs on "
          "that test gives the answer."),

 dict(q="Two substances of comparable molecular size are tabulated, one polar and one "
        "nonpolar. Which has the greater interactions between its own molecules, and why?",
      table=_T_SIZE,
      choices=[
        "The polar one, because dipole-dipole interactions act in addition to London "
        "dispersion forces",
        "The nonpolar one, because dispersion forces replace the weaker dipole-dipole "
        "interactions",
        "The polar one, because a dipole moment removes the need for dispersion forces",
        "They are equal, because the two substances are of comparable size",
        "The nonpolar one, because polar molecules repel one another"],
      ans=0,
      why="EK 3.1.A.2's second sub-point states both the comparison and its reason: "
          "interactions between polar molecules are typically greater than those between "
          "nonpolar molecules of comparable size BECAUSE these interactions act in addition "
          "to London dispersion forces. Comparable size is the condition that makes the "
          "comparison fair rather than the reason the two are equal."),

 dict(q="Two polar molecules of the same kind interact, and the strength of the "
        "interaction changes as the molecules turn relative to one another. Which part of "
        "the framework accounts for that?",
      choices=[
        "That dipole-dipole interaction strength depends on the relative orientation of "
        "the dipoles",
        "That dipole-dipole interaction strength depends only on the magnitudes of the "
        "dipoles",
        "That London dispersion forces arise from temporary, fluctuating dipoles",
        "That ion-dipole forces tend to be stronger than dipole-dipole forces",
        "That hydrogen bonding requires nitrogen, oxygen or fluorine"],
      ans=0,
      why="EK 3.1.A.2's second sub-point names relative orientation alongside the "
          "magnitudes of the dipoles as what the interaction strength depends on, and EK "
          "3.1.A.3 makes that orientation dependence something to be understood "
          "qualitatively from the partial charges."),

 dict(q="EK 3.1.A.3 asks how the partial charges are to be considered. What does it say "
        "they interact with?",
      choices=[
        "With an ion, or with an adjacent dipole",
        "With the nucleus of the nearest atom",
        "With the delocalized electrons of a metal",
        "With the covalent bonds inside the same molecule",
        "With the walls of the container"],
      ans=0,
      why="EK 3.1.A.3 names both: how these partial charges interact with an ion or with an "
          "adjacent dipole. Those two cases correspond exactly to the ion-dipole and "
          "dipole-dipole forces the same statement is about."),

 dict(q="A molecule contains hydrogen atoms covalently bonded to carbon and nothing else. "
        "Does the framework's definition of hydrogen bonding reach it?",
      choices=[
        "No, because the definition names hydrogen bonded to nitrogen, oxygen or fluorine",
        "Yes, because carbon is more electronegative than hydrogen",
        "Yes, because any covalently bonded hydrogen can hydrogen bond",
        "No, because hydrogen bonding requires an ion to be present",
        "Yes, but only if the molecule is large"],
      ans=0,
      why="EK 3.1.A.4 defines hydrogen bonding for hydrogen atoms covalently bonded to the "
          "highly electronegative atoms N, O and F, and names no other element. That "
          "carbon is somewhat more electronegative than hydrogen, which EK 2.1.A.2 itself "
          "notes, does not put it on the framework's list."),

 dict(q="Learning objective 3.1.A names two cases in which the relationship between "
        "chemical structure and intermolecular force strength is to be explained. What are "
        "they?",
      choices=[
        "When the molecules are of the same chemical species, and when they are of two "
        "different chemical species",
        "When the molecules are polar, and when they are nonpolar",
        "When the substance is a solid, and when it is a liquid",
        "When the molecules are large, and when they are small",
        "When the temperature is high, and when it is low"],
      ans=0,
      why="LO 3.1.A states the two cases in exactly those words, as its sub-points i and "
          "ii. The distinction the objective draws is between one species interacting with "
          "itself and two different species interacting with each other."),

 dict(q="Which comparison does the framework NOT make?",
      choices=[
        "Whether hydrogen bonding is stronger or weaker than an ion-dipole force",
        "Whether ion-dipole forces tend to be stronger than dipole-dipole forces",
        "Whether interactions between polar molecules are typically greater than those "
        "between nonpolar molecules of comparable size",
        "Whether London dispersion forces are often the strongest net force between large "
        "molecules",
        "Whether dipole-dipole strength depends on the relative orientation of the dipoles"],
      ans=0,
      why="EK 3.1.A.4 calls hydrogen bonding a strong type of intermolecular interaction "
          "and stops there, ranking it against nothing. The other four statements are each "
          "made explicitly, in EK 3.1.A.2's two sub-points and in EK 3.1.A.1."),

 dict(q="EK 3.1.A.2 says a polar molecule's dipole moment leads to ADDITIONAL "
        "interactions. Additional to what, in the framework's own account?",
      choices=[
        "To the London dispersion forces that the same statement says these interactions "
        "act in addition to",
        "To the covalent bonds within the molecule",
        "To the ionic attractions between cations and anions",
        "To the delocalized electrons of a metallic solid",
        "To nothing; the word additional is used loosely"],
      ans=0,
      why="EK 3.1.A.2's second sub-point spells out what the addition is to: these "
          "interactions act in addition to London dispersion forces. Covalent bonds are "
          "intramolecular and belong to unit 2, so they are not what an intermolecular "
          "force is added to."),

 dict(q="What distinguishes the dipoles behind London dispersion forces from the dipole "
        "moment of a polar molecule, in the framework's wording?",
      choices=[
        "They are temporary and fluctuating",
        "They are larger in magnitude",
        "They arise only in molecules containing nitrogen, oxygen or fluorine",
        "They point in a fixed direction relative to the molecular framework",
        "They carry a full charge rather than a partial one"],
      ans=0,
      why="EK 3.1.A.1 describes the dipoles responsible for dispersion forces as temporary "
          "and fluctuating, while EK 3.1.A.2 speaks of the dipole moment OF a polar "
          "molecule as a property of that molecule. Those two words are the distinction the "
          "framework draws."),

 dict(q="A single large biomolecule folds so that two of its own regions come close "
        "together. Does the framework allow a noncovalent interaction between them?",
      choices=[
        "Yes, since it allows such interactions between different regions of the same "
        "large biomolecule",
        "No, since noncovalent interactions require two separate molecules",
        "No, since a folded molecule has no dipoles",
        "Yes, but only if the two regions carry full charges",
        "Yes, but only between two different biomolecules of the same kind"],
      ans=0,
      why="EK 3.1.A.5 states it directly: in large biomolecules, noncovalent interactions "
          "may occur between different molecules or between different regions of the same "
          "large biomolecule. EK 3.1.A.4 makes the same allowance for hydrogen bonding "
          "within one molecule."),

 dict(q="The framework says ion-dipole forces TEND to be stronger than dipole-dipole "
        "forces. What does that wording rule out?",
      choices=[
        "Treating the comparison as holding without exception in every case",
        "Treating ion-dipole forces as generally the stronger of the two",
        "Treating dipole-dipole interactions as present between polar molecules",
        "Treating ion-dipole forces as present between ions and polar molecules",
        "Treating the two kinds of force as different from each other"],
      ans=0,
      why="EK 3.1.A.2's third sub-point says these TEND to be stronger, which asserts a "
          "general tendency rather than an exceptionless rule. The other statements are "
          "each part of what the same sub-point does assert."),

 dict(q="Which statement about intermolecular forces is NOT supported by the framework?",
      choices=[
        "London dispersion forces and van der Waals forces are two names for the same thing",
        "London dispersion forces result from Coulombic interactions between temporary, "
        "fluctuating dipoles",
        "Ion-dipole forces are present between ions and polar molecules",
        "Hydrogen bonding can occur between different parts of one molecule",
        "Dipole-dipole interaction strength depends on the relative orientation of the "
        "dipoles"],
      ans=0,
      why="EK 3.1.A.1's third sub-point says the term London dispersion forces should NOT "
          "be used synonymously with the term van der Waals forces, which contradicts the "
          "keyed statement directly. The other four are each stated in EK 3.1.A.1, 3.1.A.2 "
          "or 3.1.A.4."),
]
