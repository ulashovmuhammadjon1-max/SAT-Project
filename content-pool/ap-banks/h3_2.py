r"""AP CHEMISTRY 3.2 Properties of Solids.

CED effective Fall 2024, Unit 3 Properties of Substances and Mixtures.
Learning objective 3.2.A: explain the relationship among the macroscopic
properties of a substance, the particulate-level structure of the substance, and
the interactions between these particles.
Suggested skill 4.C, explain the connection between particulate-level and
macroscopic properties of a substance using models and representations.

Essential knowledge relied on, in the framework's own words:

  3.2.A.1  Many properties of liquids and solids are determined by the strengths
           and types of intermolecular forces present. Because intermolecular
           interactions are overcome completely when a substance vaporizes, the
           vapor pressure and boiling point are directly related to the strength
           of those interactions. Melting points also tend to correlate with
           interaction strength, but because the interactions are only
           rearranged, in melting, the relations can be more subtle.
  3.2.A.2  Particulate-level representations, showing multiple interacting
           chemical species, are a useful means to communicate or understand how
           intermolecular interactions help to establish macroscopic properties.
  3.2.A.3  Due to strong interactions between ions, ionic solids tend to have
           low vapor pressures, high melting points, and high boiling points.
           They tend to be brittle due to the repulsion of like charges caused
           when one layer slides across another layer. They conduct electricity
           only when the ions are mobile, as when the ionic solid is melted
           (i.e., in a molten state) or dissolved in water or another solvent.
  3.2.A.4  In covalent network solids, the atoms are covalently bonded together
           into a three-dimensional network (e.g., diamond) or layers of
           two-dimensional networks (e.g., graphite). These are only formed from
           nonmetals and metalloids: elemental (e.g., diamond, graphite) or
           binary compounds (e.g., silicon dioxide and silicon carbide). Due to
           the strong covalent interactions, covalent solids have high melting
           points. Three-dimensional network solids are also rigid and hard,
           because the covalent bond angles are fixed. However, graphite is soft
           because adjacent layers can slide past each other relatively easily.
  3.2.A.5  Molecular solids are composed of distinct, individual units of
           covalently-bonded molecules attracted to each other through
           relatively weak intermolecular forces. Molecular solids generally
           have a low melting point because of the relatively weak
           intermolecular forces present between the molecules. They do not
           conduct electricity because their valence electrons are tightly held
           within the covalent bonds and the lone pairs of each constituent
           molecule. Molecular solids are sometimes composed of very large
           molecules or polymers.
  3.2.A.6  Metallic solids are good conductors of electricity and heat, due to
           the presence of free valence electrons. They also tend to be malleable
           and ductile, due to the ease with which the metal cores can rearrange
           their structure. In an interstitial alloy, interstitial atoms tend to
           make the lattice more rigid, decreasing malleability and ductility.
           Alloys typically retain a sea of mobile electrons and so remain
           conducting.
  3.2.A.7  In large biomolecules or polymers, noncovalent interactions may occur
           between different molecules or between different regions of the same
           large biomolecule. The functionality and properties of such molecules
           depend strongly on the shape of the molecule, which is largely
           dictated by noncovalent interactions.

WHERE THE FRAMEWORK IS SILENT, THIS MODULE IS SILENT. EK 3.2.A.4 says a great
deal about covalent network solids and says NOTHING about whether they conduct
electricity. Three of the four solid types have a conduction statement and one
does not, and item 30 keys on exactly that silence rather than supplying the
answer a textbook would. ``conduction_claims_match_the_framework`` in the
verifier holds the four statements the CED actually makes and checks every
conduction key against them.

THE MELTING-POINT HEDGE IS THE OTHER THING WORTH KEEPING. EK 3.2.A.1 makes vapor
pressure and boiling point DIRECTLY related to interaction strength because the
interactions are overcome completely on vaporizing, but says melting points only
TEND to correlate, and that because the interactions are merely rearranged in
melting "the relations can be more subtle". Items 1 and 2 are that contrast, and
no key anywhere here treats a melting point as a direct measure of interaction
strength.

NO FIGURES. EK 3.2.A.2 is about particulate representations and this bank cannot
show one, so item 3 asks what such a representation is FOR, which is what the
statement itself says, rather than asking a student to read one.

NOTATION. Plain prose throughout. No math spans are needed in this module.
"""
TOPIC = ("3.2", "Properties of Solids", 3)

_T_SOLIDS = dict(
    headers=["Solid", "Type of solid"],
    rows=[["Solid 1", "ionic"],
          ["Solid 2", "covalent network"],
          ["Solid 3", "molecular"],
          ["Solid 4", "metallic"]])

QUESTIONS = [

 dict(q="Why does the framework say that vapor pressure and boiling point are directly "
        "related to the strength of a substance's intermolecular interactions?",
      choices=[
        "Because those interactions are overcome completely when the substance vaporizes",
        "Because those interactions are merely rearranged when the substance vaporizes",
        "Because vaporizing breaks the covalent bonds within each molecule",
        "Because vapor pressure is measured at the melting point",
        "Because a vapor has stronger interactions than the liquid it came from"],
      ans=0,
      why="EK 3.2.A.1 gives the reason in those words: because intermolecular interactions "
          "are overcome completely when a substance vaporizes, the vapor pressure and "
          "boiling point are directly related to the strength of those interactions. "
          "Rearrangement rather than complete removal is what the same statement says "
          "happens in melting."),

 dict(q="What does the framework say about how melting points relate to interaction "
        "strength?",
      choices=[
        "They tend to correlate with it, but the relations can be more subtle because the "
        "interactions are only rearranged in melting",
        "They are directly related to it, exactly as boiling points are",
        "They are unrelated to it, since melting does not involve intermolecular forces",
        "They are inversely related to it, so stronger interactions give lower melting "
        "points",
        "They can be predicted only from the mass of the substance"],
      ans=0,
      why="EK 3.2.A.1 hedges melting points deliberately: they also TEND to correlate with "
          "interaction strength, but because the interactions are only rearranged in "
          "melting, the relations can be more subtle. The direct relation is reserved for "
          "vapor pressure and boiling point in the same statement."),

 dict(q="What does the framework say particulate-level representations are useful for?",
      choices=[
        "Communicating or understanding how intermolecular interactions help to establish "
        "macroscopic properties",
        "Measuring the boiling point of a substance to within a degree",
        "Counting the number of molecules in a macroscopic sample",
        "Replacing the need to know what interactions are present",
        "Determining the mass of one mole of the substance"],
      ans=0,
      why="EK 3.2.A.2 states the purpose in those words, and specifies that such "
          "representations show MULTIPLE interacting chemical species. The statement is "
          "about communication and understanding rather than about measurement."),

 dict(q="What does the framework say ionic solids tend to have, and why?",
      choices=[
        "Low vapor pressures, high melting points and high boiling points, due to strong "
        "interactions between ions",
        "High vapor pressures, low melting points and low boiling points, due to weak "
        "interactions between ions",
        "Low vapor pressures and low melting points, due to the mobility of the ions",
        "High melting points but also high vapor pressures, due to the size of the ions",
        "Properties that cannot be generalized, since every ionic solid differs"],
      ans=0,
      why="EK 3.2.A.3 states it in exactly those terms: due to strong interactions between "
          "ions, ionic solids tend to have low vapor pressures, high melting points, and "
          "high boiling points. A low vapor pressure and a high boiling point go together "
          "under EK 3.2.A.1, since both follow from strong interactions."),

 dict(q="What reason does the framework give for ionic solids tending to be brittle?",
      choices=[
        "The repulsion of like charges caused when one layer slides across another",
        "The complete absence of any attraction between the ions",
        "The ease with which the ions rearrange their positions",
        "The presence of free valence electrons between the ions",
        "The weakness of the interactions holding the ions together"],
      ans=0,
      why="EK 3.2.A.3 gives that reason in its own words: they tend to be brittle due to "
          "the repulsion of like charges caused when one layer slides across another layer. "
          "Ease of rearrangement is what EK 3.2.A.6 attributes to metallic solids, and it "
          "produces the opposite property."),

 dict(q="Under what conditions does the framework say an ionic solid conducts electricity?",
      choices=[
        "Only when the ions are mobile, as when it is melted or dissolved",
        "At all times, since it is built from charged particles",
        "Only when it is in the solid state, since the array holds the ions in place",
        "Only when it is cooled below its melting point",
        "Never, under any conditions"],
      ans=0,
      why="EK 3.2.A.3 states the condition precisely: they conduct electricity only when "
          "the ions are mobile, as when the ionic solid is melted, that is in a molten "
          "state, or dissolved in water or another solvent. Mobility of the ions is what "
          "the conduction depends on."),

 dict(q="How does the framework describe the bonding arrangement in a covalent network "
        "solid?",
      choices=[
        "The atoms are covalently bonded into a three-dimensional network or into layers "
        "of two-dimensional networks",
        "The atoms are held in discrete molecules attracted by weak forces",
        "Positive cores sit in a sea of delocalized valence electrons",
        "Cations and anions alternate through a periodic array",
        "Neutral atoms are stacked without any bonding between them"],
      ans=0,
      why="EK 3.2.A.4 names both arrangements, with diamond as its example of the "
          "three-dimensional case and graphite of the layered one. The other options "
          "describe molecular, metallic and ionic solids under EK 3.2.A.5, 3.2.A.6 and "
          "3.2.A.3 respectively."),

 dict(q="From which elements does the framework say covalent network solids are formed?",
      choices=[
        "Only from nonmetals and metalloids",
        "Only from metals",
        "From a metal together with a nonmetal",
        "From any elements at all",
        "Only from elements in the same group of the periodic table"],
      ans=0,
      why="EK 3.2.A.4 states the restriction directly: these are only formed from nonmetals "
          "and metalloids. A metal with a nonmetal is EK 2.1.A.4's generalization for ionic "
          "bonding, which produces a different kind of solid."),

 dict(q="What kinds of substance does the framework say covalent network solids can be?",
      choices=[
        "Elemental, or binary compounds",
        "Elemental only",
        "Binary compounds only",
        "Compounds of three or more elements only",
        "Mixtures of two or more separate solids"],
      ans=0,
      why="EK 3.2.A.4 gives both, with its own examples: elemental, as diamond and "
          "graphite, or binary compounds, as silicon dioxide and silicon carbide. "
          "Restricting the class to either case alone drops half of what the framework "
          "states."),

 dict(q="What reason does the framework give for covalent network solids having high "
        "melting points?",
      choices=[
        "The strong covalent interactions holding the network together",
        "The weak intermolecular forces between the layers",
        "The mobility of the valence electrons through the network",
        "The repulsion between like charges within the network",
        "The large mass of each atom in the network"],
      ans=0,
      why="EK 3.2.A.4 gives the reason in those words: due to the strong covalent "
          "interactions, covalent solids have high melting points. Weak intermolecular "
          "forces are what EK 3.2.A.5 makes responsible for the LOW melting points of "
          "molecular solids."),

 dict(q="Why does the framework say three-dimensional network solids are rigid and hard?",
      choices=[
        "Because the covalent bond angles are fixed",
        "Because their layers can slide past one another easily",
        "Because their valence electrons are free to move",
        "Because their ions repel one another when a layer slides",
        "Because they are held together by weak intermolecular forces"],
      ans=0,
      why="EK 3.2.A.4 gives exactly that reason: three-dimensional network solids are also "
          "rigid and hard, because the covalent bond angles are fixed. Sliding layers are "
          "what the same statement uses to explain the opposite property in graphite."),

 dict(q="What reason does the framework give for graphite being soft?",
      choices=[
        "Adjacent layers can slide past each other relatively easily",
        "Its covalent bonds are weaker than those in other network solids",
        "It contains no covalent bonds at all",
        "Its bond angles are free to change within each layer",
        "It is held together only by ion-dipole forces"],
      ans=0,
      why="EK 3.2.A.4 states it directly: however, graphite is soft because adjacent layers "
          "can slide past each other relatively easily. The framework attributes the "
          "softness to the arrangement of the layers rather than to any weakness in the "
          "covalent bonds themselves."),

 dict(q="How does the framework describe what a molecular solid is composed of?",
      choices=[
        "Distinct, individual units of covalently bonded molecules attracted to each other "
        "through relatively weak intermolecular forces",
        "A continuous covalent network extending through the whole solid",
        "Cations and anions in a periodic three-dimensional array",
        "Positive cores surrounded by delocalized valence electrons",
        "Individual atoms held together by ion-dipole forces"],
      ans=0,
      why="EK 3.2.A.5 states it in those words. The word DISTINCT is what separates a "
          "molecular solid from EK 3.2.A.4's covalent network, where the covalent bonding "
          "runs through the whole solid rather than stopping at the edge of a molecule."),

 dict(q="What reason does the framework give for molecular solids generally having a low "
        "melting point?",
      choices=[
        "The relatively weak intermolecular forces present between the molecules",
        "The weakness of the covalent bonds within each molecule",
        "The mobility of their valence electrons",
        "The repulsion between the molecules",
        "The small mass of each molecule"],
      ans=0,
      why="EK 3.2.A.5 gives that reason directly: molecular solids generally have a low "
          "melting point because of the relatively weak intermolecular forces present "
          "between the molecules. The bonds WITHIN each molecule are covalent and are not "
          "what melting overcomes."),

 dict(q="Why does the framework say molecular solids do not conduct electricity?",
      choices=[
        "Their valence electrons are tightly held within the covalent bonds and the lone "
        "pairs of each molecule",
        "Their molecules carry no electrons at all",
        "Their ions are held immobile in a rigid array",
        "Their valence electrons are delocalized over the whole solid",
        "Their molecules are too large to move"],
      ans=0,
      why="EK 3.2.A.5 gives that reason in its own words. Immobile ions are EK 3.2.A.3's "
          "explanation for an ionic solid, and delocalized valence electrons are EK "
          "3.2.A.6's reason why a metallic solid DOES conduct."),

 dict(q="What does the framework add about the size of the units in a molecular solid?",
      choices=[
        "Molecular solids are sometimes composed of very large molecules or polymers",
        "Molecular solids are always composed of very small molecules",
        "Molecular solids contain no molecules, only atoms",
        "Molecular solids contain molecules all of exactly the same size",
        "Molecular solids are composed of molecules too small to be represented"],
      ans=0,
      why="EK 3.2.A.5 closes with exactly that sentence, which keeps polymers inside the "
          "molecular category rather than treating a large molecule as a network solid. EK "
          "3.2.A.7 then treats the noncovalent interactions of such large molecules."),

 dict(q="What reason does the framework give for metallic solids being good conductors of "
        "electricity and heat?",
      choices=[
        "The presence of free valence electrons",
        "The mobility of the metal ions through the solid",
        "The fixed covalent bond angles within the lattice",
        "The repulsion of like charges when one layer slides",
        "The weakness of the interactions between the metal cores"],
      ans=0,
      why="EK 3.2.A.6 gives that reason directly: metallic solids are good conductors of "
          "electricity and heat, due to the presence of free valence electrons, which is "
          "the sea of electrons EK 2.4.A.1 describes. The ions themselves stay in place."),

 dict(q="What reason does the framework give for metallic solids tending to be malleable "
        "and ductile?",
      choices=[
        "The ease with which the metal cores can rearrange their structure",
        "The repulsion of like charges when one layer slides across another",
        "The fixed covalent bond angles between the metal cores",
        "The absence of any electrons between the metal cores",
        "The high melting points that metals generally have"],
      ans=0,
      why="EK 3.2.A.6 gives that reason in those words. Repulsion of like charges on "
          "sliding is EK 3.2.A.3's explanation for brittleness in ionic solids, which is "
          "the opposite behavior."),

 dict(q="What does the framework say interstitial atoms do to an alloy's lattice?",
      choices=[
        "They tend to make it more rigid, decreasing malleability and ductility",
        "They tend to make it less rigid, increasing malleability and ductility",
        "They remove the free valence electrons, so the alloy stops conducting",
        "They leave the mechanical properties of the lattice unchanged",
        "They convert the metallic bonding into ionic bonding"],
      ans=0,
      why="EK 3.2.A.6 states it directly: in an interstitial alloy, interstitial atoms tend "
          "to make the lattice more rigid, decreasing malleability and ductility. The same "
          "statement goes on to say the alloy nevertheless remains conducting."),

 dict(q="What does the framework say about the electrical conduction of alloys?",
      choices=[
        "They typically retain a sea of mobile electrons and so remain conducting",
        "They lose their mobile electrons and stop conducting",
        "They conduct only when melted, as ionic solids do",
        "They conduct only if both components are metals",
        "They conduct better than either pure component in every case"],
      ans=0,
      why="EK 3.2.A.6 closes with exactly that: alloys typically retain a sea of mobile "
          "electrons and so remain conducting. Conducting only when molten is EK 3.2.A.3's "
          "description of an ionic solid, not of an alloy."),

 dict(q="What does the framework say the functionality and properties of a large "
        "biomolecule depend on?",
      choices=[
        "Strongly on the shape of the molecule, which is largely dictated by noncovalent "
        "interactions",
        "Only on the covalent bonds within the molecule, its shape being irrelevant",
        "Only on the total mass of the molecule",
        "On the number of ions dissolved around it",
        "On the temperature alone"],
      ans=0,
      why="EK 3.2.A.7 states it in those words: the functionality and properties of such "
          "molecules depend strongly on the shape of the molecule, which is largely "
          "dictated by noncovalent interactions. The noncovalent interactions reach the "
          "properties through the shape."),

 dict(q="What does the framework say determines many properties of liquids and solids?",
      choices=[
        "The strengths and types of intermolecular forces present",
        "The strengths of the intermolecular forces alone, their type being irrelevant",
        "The types of intermolecular force alone, their strength being irrelevant",
        "The number of atoms in each molecule",
        "The container the substance is held in"],
      ans=0,
      why="EK 3.2.A.1 opens by naming both: many properties of liquids and solids are "
          "determined by the strengths AND TYPES of intermolecular forces present. Dropping "
          "either half is what makes two of the rejected options wrong."),

 dict(q="Four solids are tabulated by type. Which one does the framework describe as a "
        "good conductor of electricity in the solid state?",
      table=_T_SOLIDS,
      choices=["Solid 4", "Solid 1", "Solid 2", "Solid 3",
               "None of them, since no solid conducts electricity"],
      ans=0,
      why="EK 3.2.A.6 says metallic solids are good conductors of electricity and heat, due "
          "to free valence electrons. Of the four tabulated types, that statement is made "
          "about exactly one, and EK 3.2.A.3 and EK 3.2.A.5 describe the other two "
          "conduction cases differently."),

 dict(q="Using the same four tabulated solids, which does the framework say conducts "
        "electricity only when it is melted or dissolved?",
      table=_T_SOLIDS,
      choices=["Solid 1", "Solid 2", "Solid 3", "Solid 4",
               "All four, since conduction always requires mobile particles"],
      ans=0,
      why="EK 3.2.A.3 says an ionic solid conducts electricity only when the ions are "
          "mobile, as when it is melted or dissolved in water or another solvent. That "
          "condition is attached to exactly one of the tabulated types."),

 dict(q="Among those tabulated solids, which does the framework say does not conduct "
        "electricity?",
      table=_T_SOLIDS,
      choices=["Solid 3", "Solid 1", "Solid 2", "Solid 4",
               "None of them, since every solid conducts to some degree"],
      ans=0,
      why="EK 3.2.A.5 says molecular solids do not conduct electricity, because their "
          "valence electrons are tightly held within the covalent bonds and lone pairs of "
          "each molecule. That flat statement is made about exactly one tabulated type."),

 dict(q="Of the four tabulated solids, which does the framework say generally has a low "
        "melting point?",
      table=_T_SOLIDS,
      choices=["Solid 3", "Solid 1", "Solid 2", "Solid 4",
               "None of them; the framework gives no melting point for any type"],
      ans=0,
      why="EK 3.2.A.5 says molecular solids generally have a low melting point because of "
          "the relatively weak intermolecular forces between the molecules. EK 3.2.A.3 and "
          "EK 3.2.A.4 assign high melting points to two of the other tabulated types."),

 dict(q="For how many of the four tabulated types does the framework state a HIGH melting "
        "point?",
      table=_T_SOLIDS,
      choices=["Exactly two", "Exactly one", "Exactly three", "All four", "None of them"],
      ans=0,
      why="EK 3.2.A.3 gives ionic solids high melting points and EK 3.2.A.4 gives covalent "
          "network solids high melting points, while EK 3.2.A.5 gives molecular solids a "
          "low one and EK 3.2.A.6 states no melting point for metallic solids at all."),

 dict(q="Which of the tabulated solids does the framework describe as tending to be "
        "brittle?",
      table=_T_SOLIDS,
      choices=["Solid 1", "Solid 2", "Solid 3", "Solid 4",
               "None of them; brittleness is not a property the framework discusses"],
      ans=0,
      why="EK 3.2.A.3 says ionic solids tend to be brittle due to the repulsion of like "
          "charges caused when one layer slides across another layer. Brittleness is "
          "attached to exactly one of the tabulated types."),

 dict(q="Which of the tabulated solids does the framework describe as tending to be "
        "malleable and ductile?",
      table=_T_SOLIDS,
      choices=["Solid 4", "Solid 1", "Solid 2", "Solid 3",
               "None of them; malleability is not a property the framework discusses"],
      ans=0,
      why="EK 3.2.A.6 says metallic solids tend to be malleable and ductile, due to the "
          "ease with which the metal cores can rearrange their structure. That property is "
          "attached to exactly one of the tabulated types, and EK 3.2.A.3 attaches the "
          "opposite behavior to another."),

 dict(q="For which of the tabulated types does the framework make no statement at all "
        "about electrical conduction?",
      table=_T_SOLIDS,
      choices=["Solid 2", "Solid 1", "Solid 3", "Solid 4",
               "For none of them; every type has a conduction statement"],
      ans=0,
      why="EK 3.2.A.3 states when an ionic solid conducts, EK 3.2.A.5 states that a "
          "molecular solid does not, and EK 3.2.A.6 states that a metallic solid does, but "
          "EK 3.2.A.4 says nothing whatever about conduction in a covalent network solid, "
          "even while describing its bonding, melting point, rigidity and hardness at "
          "length."),
]
