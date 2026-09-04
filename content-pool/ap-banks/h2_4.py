r"""AP CHEMISTRY 2.4 Structure of Metals and Alloys.

CED effective Fall 2024, Unit 2 Compound Structure and Properties.
Learning objective 2.4.A: represent a metallic solid and/or alloy using a model
to show essential characteristics of the structure and interactions present in
the substance.
Suggested skill 4.C, explain the connection between particulate-level and
macroscopic properties of a substance using models and representations.

Essential knowledge relied on, in the framework's own words:

  2.4.A.1  Metallic bonding can be represented as an array of positive metal
           ions surrounded by delocalized valence electrons (i.e., a "sea of
           electrons").
  2.4.A.2  Interstitial alloys form between atoms of significantly different
           radii, where the smaller atoms fill the interstitial spaces between
           the larger atoms (e.g., with steel in which carbon occupies the
           interstices in iron).
  2.4.A.3  Substitutional alloys form between atoms of comparable radius, where
           one atom substitutes for the other in the lattice. (e.g., in certain
           brass alloys, other elements, usually zinc, substitute for copper.)

THE ONE DISCRIMINATION THIS TOPIC OWNS is radius: significantly different radii
give an interstitial alloy, comparable radii a substitutional one. That is a
comparison, so twelve items here put real radii in a table and ask the question
of the numbers, and two more state radii in the stem. Every one is recomputed
in verify_h2_4.py from the item's own stimulus, and each classification is made
from the RATIO of the two radii, which is what "comparable" and "significantly
different" are about.

WHAT IS NOT HERE. That metallic solids conduct electricity and heat, that they
are malleable and ductile, and that an interstitial atom makes the lattice more
rigid and so less malleable, are all EK 3.2.A.6 and belong to topic 3.2. No key
here rests on any of them and ``no_macroscopic_property`` in the verifier
asserts it. What 2.4 owns is the STRUCTURE: what the model shows and which kind
of alloy two radii produce.

ON THE CED'S OWN EXAMPLES. The framework names steel (carbon in the interstices
of iron) and brass (zinc substituting for copper) inside the essential
knowledge itself, so both are keyed here, and the tabulated radii for iron,
carbon, copper and zinc are given in the item rather than assumed to be
recalled -- every classification follows from the numbers printed in the table.

NO FIGURES. The bank cannot show a lattice, so candidate models are described
in words or by their tabulated radii and the question is asked of that.

NOTATION. Radii and element names are plain prose. No math spans are needed
anywhere in this module.
"""
TOPIC = ("2.4", "Structure of Metals and Alloys", 2)

_T_PAIRS = dict(
    headers=["Element pair", "Radius of the host atom (picometers)",
             "Radius of the added atom (picometers)"],
    rows=[["Pair 1", "126", "77"],
          ["Pair 2", "128", "134"],
          ["Pair 3", "144", "141"],
          ["Pair 4", "140", "70"]])

_T_ELEMENTS = dict(
    headers=["Species", "Atomic radius (picometers)"],
    rows=[["Host metal M", "140"],
          ["Element A", "135"],
          ["Element B", "70"],
          ["Element C", "144"],
          ["Element D", "132"]])

_T_NAMED = dict(
    headers=["Alloy", "Majority element and its atomic radius (picometers)",
             "Added element and its atomic radius (picometers)"],
    rows=[["Alloy 1", "iron, 126", "carbon, 77"],
          ["Alloy 2", "copper, 128", "zinc, 134"]])

QUESTIONS = [

 dict(q="How can metallic bonding be represented, according to the framework?",
      choices=[
        "As an array of positive metal ions surrounded by delocalized valence electrons",
        "As an array of neutral metal atoms, each holding on to its own valence electrons",
        "As alternating positive metal ions and negative nonmetal ions",
        "As separate metal atoms joined in pairs by shared electron pairs",
        "As an array of negative metal ions surrounded by delocalized protons"],
      ans=0,
      why="EK 2.4.A.1, verbatim: metallic bonding can be represented as an array of "
          "positive metal ions surrounded by delocalized valence electrons, a sea of "
          "electrons. The alternating positive and negative ions belong to EK 2.3.A.1's "
          "ionic crystal, not to a metal."),

 dict(q="The framework calls the electrons in a metallic solid a sea of electrons. Which "
        "electrons does that phrase describe?",
      choices=[
        "The valence electrons, which are delocalized rather than associated with any "
        "individual atom",
        "The core electrons, which stay bound to their own nuclei",
        "Electrons that have left the solid entirely and travel in the surrounding air",
        "Electrons shared between exactly two neighboring metal atoms at a time",
        "Electrons transferred permanently from one metal atom to another"],
      ans=0,
      why="EK 2.4.A.1 calls them delocalized VALENCE electrons, and EK 2.1.A.5 says the "
          "same thing in the same words: in a metallic solid the valence electrons from "
          "the metal atoms are considered to be delocalized and not associated with any "
          "individual atom."),

 dict(q="In the model of metallic bonding the framework describes, why are the metal "
        "cores drawn as positive ions?",
      choices=[
        "Because their valence electrons are delocalized through the solid rather than "
        "held by any one core",
        "Because a metal must gain electrons from the surrounding air to form a solid",
        "Because each core has captured an electron from its neighbor",
        "Because the framework treats every metal as an ionic compound",
        "Because the cores repel one another and so must carry like charges"],
      ans=0,
      why="EK 2.4.A.1 represents the solid as positive metal ions surrounded by "
          "delocalized valence electrons, and EK 2.1.A.5 says those valence electrons are "
          "not associated with any individual atom. A core that has given its valence "
          "electrons up to the shared sea is what is left carrying positive charge."),

 dict(q="Under what condition does the framework say an interstitial alloy forms, and "
        "where do the added atoms sit?",
      choices=[
        "Between atoms of significantly different radii, with the smaller atoms filling "
        "the spaces between the larger ones",
        "Between atoms of comparable radius, with the smaller atoms filling the spaces "
        "between the larger ones",
        "Between atoms of significantly different radii, with the smaller atoms taking "
        "the lattice positions of the larger ones",
        "Between atoms of comparable radius, with each atom taking the lattice position "
        "of the other",
        "Between a metal and a nonmetal only, with the nonmetal forming negative ions"],
      ans=0,
      why="EK 2.4.A.2, verbatim: interstitial alloys form between atoms of significantly "
          "different radii, where the smaller atoms fill the interstitial spaces between "
          "the larger atoms. Two rejected options swap in the condition or the placement "
          "belonging to a substitutional alloy under EK 2.4.A.3."),

 dict(q="Under what condition does the framework say a substitutional alloy forms, and "
        "what happens in the lattice?",
      choices=[
        "Between atoms of comparable radius, with one atom substituting for the other in "
        "the lattice",
        "Between atoms of significantly different radii, with one atom substituting for "
        "the other in the lattice",
        "Between atoms of comparable radius, with the added atoms filling the spaces "
        "between lattice positions",
        "Between atoms of any radii, with the added atoms forming a separate layer on the "
        "surface",
        "Between two nonmetals only, with the atoms sharing electron pairs"],
      ans=0,
      why="EK 2.4.A.3, verbatim: substitutional alloys form between atoms of comparable "
          "radius, where one atom substitutes for the other in the lattice. Swapping in "
          "significantly different radii gives EK 2.4.A.2's condition instead."),

 dict(q="The table gives the atomic radii of the two elements in four candidate alloys. "
        "Which pair is most likely to form an interstitial alloy?",
      table=_T_PAIRS,
      choices=["Pair 4", "Pair 1", "Pair 2", "Pair 3",
               "Pair 2, because its added atom is the larger of the two"],
      ans=0,
      why="EK 2.4.A.2 makes significantly different radii the condition for an "
          "interstitial alloy, so the pair whose added atom is smallest relative to its "
          "host is the likeliest. A pair whose added atom is LARGER than the host cannot "
          "fit into a space between host atoms at all."),

 dict(q="Using the same four candidate alloys, which pair is most likely to form a "
        "substitutional alloy?",
      table=_T_PAIRS,
      choices=["Pair 3", "Pair 1", "Pair 2", "Pair 4",
               "Pair 1, because its two radii differ by the largest number of picometers"],
      ans=0,
      why="EK 2.4.A.3 makes comparable radius the condition for substitution, so the pair "
          "whose two radii are nearest to equal is the likeliest. The largest difference "
          "in radii is the condition EK 2.4.A.2 names for the other kind of alloy."),

 dict(q="The framework gives steel as its example of one kind of alloy. What does it say "
        "carbon does in iron?",
      choices=[
        "Carbon occupies the interstices in iron",
        "Carbon substitutes for iron atoms in the lattice",
        "Carbon forms a separate layer on the surface of the iron",
        "Carbon takes electrons from iron to form carbide ions in an ionic array",
        "Carbon replaces the delocalized electrons of the metal"],
      ans=0,
      why="EK 2.4.A.2 gives exactly this example, in these words: steel, in which carbon "
          "occupies the interstices in iron. That is what makes steel the framework's "
          "interstitial case rather than its substitutional one."),

 dict(q="The framework gives brass as its example of the other kind of alloy. What does "
        "it say zinc does in copper?",
      choices=[
        "Zinc substitutes for copper in the lattice",
        "Zinc fills the interstitial spaces between copper atoms",
        "Zinc forms a separate crystal alongside the copper",
        "Zinc gives its valence electrons to copper, forming an ionic array",
        "Zinc removes the delocalized electrons from the copper lattice"],
      ans=0,
      why="EK 2.4.A.3 gives exactly this example: in certain brass alloys, other elements, "
          "usually zinc, substitute for copper. Substitution in the lattice is the "
          "defining feature of the alloy type EK 2.4.A.3 describes."),

 dict(q="A host metal and four candidate additions have the atomic radii shown. Which "
        "added element is most likely to occupy the interstitial spaces in the host "
        "lattice?",
      table=_T_ELEMENTS,
      choices=["Element B", "Element A", "Element C", "Element D",
               "Element C, because its radius is the largest in the table"],
      ans=0,
      why="EK 2.4.A.2 requires significantly different radii for an atom to fill the "
          "spaces between the larger atoms, and one tabulated element is only half the "
          "size of the host while the others are within a few picometers of it. The "
          "largest atom in the table is larger than the host and could not fit in a gap."),

 dict(q="Using those same tabulated radii, which added element is most likely to "
        "substitute for the host atoms in the lattice?",
      table=_T_ELEMENTS,
      choices=["Element C", "Element A", "Element B", "Element D",
               "Element B, because the smallest atom fits a lattice position most easily"],
      ans=0,
      why="EK 2.4.A.3 makes comparable radius the condition for substitution, so the "
          "element whose radius is closest to the host's is the likeliest to take a "
          "lattice position. The smallest atom in the table is the one EK 2.4.A.2 sends "
          "into the interstices instead."),

 dict(q="A student's model of a metallic solid draws neutral metal atoms in an array, "
        "each keeping its own valence electrons in place. Why is that model inconsistent "
        "with the framework?",
      choices=[
        "The framework's model has positive ions and valence electrons delocalized over "
        "the whole array, not held by individual atoms",
        "The framework's model has negative ions surrounded by delocalized protons",
        "The framework's model has each valence electron shared between exactly two "
        "neighboring atoms",
        "The framework's model has no electrons between the metal cores at all",
        "It is consistent; the framework describes a metal as neutral atoms in an array"],
      ans=0,
      why="EK 2.4.A.1 represents metallic bonding as an array of POSITIVE metal ions "
          "surrounded by DELOCALIZED valence electrons, and EK 2.1.A.5 adds that those "
          "electrons are not associated with any individual atom, so localizing them on "
          "their own atoms gives up both halves of the model."),

 dict(q="Two alloys are tabulated with the atomic radii of their component elements. "
        "Which one is the interstitial alloy?",
      table=_T_NAMED,
      choices=["Alloy 1", "Alloy 2",
               "Both, since every alloy contains atoms of different size",
               "Neither, since both pairs of radii are comparable",
               "Alloy 2, because its added atom is larger than its majority atom"],
      ans=0,
      why="EK 2.4.A.2 makes significantly different radii the interstitial condition, and "
          "only one tabulated alloy pairs a majority atom with an added atom far smaller "
          "than it. That alloy is also the steel the framework names as its own example."),

 dict(q="Taking the same two tabulated alloys, which one is the substitutional alloy?",
      table=_T_NAMED,
      choices=["Alloy 2", "Alloy 1",
               "Both, since both contain two kinds of metal atom",
               "Neither, since substitution requires identical radii",
               "Alloy 1, because its added atom is much smaller than its majority atom"],
      ans=0,
      why="EK 2.4.A.3 makes comparable radius the substitutional condition, and only one "
          "tabulated alloy pairs two atoms within a few picometers of each other. That "
          "alloy is the brass the framework names as its own example; identical radii are "
          "not required, only comparable ones."),

 dict(q="Which comparison of atomic radii does the framework associate with an "
        "interstitial alloy?",
      choices=[
        "Radii that are significantly different",
        "Radii that are comparable",
        "Radii that are exactly equal",
        "Radii that are comparable in the majority element and significantly different in "
        "the added element",
        "The comparison of radii does not determine which kind of alloy forms"],
      ans=0,
      why="EK 2.4.A.2 states the condition in those words: interstitial alloys form "
          "between atoms of significantly different radii. EK 2.4.A.3 assigns comparable "
          "radii to the substitutional case, so the two conditions are the framework's "
          "own discriminator between the two kinds of alloy."),

 dict(q="Which comparison of atomic radii does the framework associate with a "
        "substitutional alloy?",
      choices=[
        "Radii that are comparable",
        "Radii that are significantly different",
        "Radii that differ by at least a factor of three",
        "Radii that are equal to within one picometer",
        "Radii play no part; only the number of valence electrons matters"],
      ans=0,
      why="EK 2.4.A.3 states the condition in those words: substitutional alloys form "
          "between atoms of comparable radius. The framework sets no numerical threshold "
          "anywhere, so a stated factor or a stated tolerance is more than it claims."),

 dict(q="Of the four tabulated candidate alloys, how many pair two atoms whose radii are "
        "within ten percent of one another?",
      table=_T_PAIRS,
      choices=["Two", "One", "Three", "Four", "None"],
      ans=0,
      why="EK 2.4.A.3 makes comparable radius the substitutional condition, and comparing "
          "each tabulated added radius with its own host radius sorts the four candidates "
          "into those that are close and those that are not. The framework states no "
          "threshold of its own, so the ten percent here is the item's stated test, not a "
          "rule being recalled."),

 dict(q="Among the four candidate additions tabulated with the host metal, how many have "
        "a radius within ten percent of the host's?",
      table=_T_ELEMENTS,
      choices=["Three", "One", "Two", "Four", "None"],
      ans=0,
      why="EK 2.4.A.3 makes comparable radius the condition for substitution, so counting "
          "the tabulated elements close to the host counts the plausible substitutions. "
          "One tabulated element is only half the host's radius and falls far outside any "
          "such comparison."),

 dict(q="Which statement is NOT part of the framework's model of metallic bonding?",
      choices=[
        "Each valence electron stays paired with one particular metal ion",
        "The metal cores are represented as positive ions",
        "The valence electrons are delocalized",
        "The ions are arranged in an array",
        "The delocalized electrons surround the metal ions"],
      ans=0,
      why="EK 2.4.A.1 represents metallic bonding as an array of positive metal ions "
          "surrounded by delocalized valence electrons, which supports every rejected "
          "statement here. EK 2.1.A.5 rules the remaining one out directly by saying the "
          "valence electrons are not associated with any individual atom."),

 dict(q="Of the tabulated candidate additions, which element's radius differs most from "
        "the host metal's?",
      table=_T_ELEMENTS,
      choices=["Element B", "Element A", "Element C", "Element D",
               "Element C, because it is the only one larger than the host"],
      ans=0,
      why="Comparing each tabulated radius with the host's identifies the one furthest "
          "away, and EK 2.4.A.2 is what makes that comparison worth making, since "
          "significantly different radii are the interstitial condition. Being larger "
          "than the host is not the same as differing from it most."),

 dict(q="In an interstitial alloy, where are the smaller atoms located?",
      choices=[
        "In the interstitial spaces between the larger atoms",
        "At lattice positions vacated by the larger atoms",
        "In a separate region of the solid containing only smaller atoms",
        "Bonded in pairs to individual larger atoms",
        "Outside the solid, adsorbed on its surface"],
      ans=0,
      why="EK 2.4.A.2 places them there in its own words: the smaller atoms fill the "
          "interstitial spaces between the larger atoms. Taking a vacated lattice "
          "position is what EK 2.4.A.3 describes for a substitutional alloy instead."),

 dict(q="In a substitutional alloy, what happens at the lattice positions?",
      choices=[
        "One kind of atom takes the place of the other at those positions",
        "Both kinds of atom leave the lattice positions empty and sit between them",
        "The lattice positions are occupied only by the majority element",
        "The lattice positions hold pairs of atoms rather than single atoms",
        "The lattice positions are filled by delocalized electrons rather than by atoms"],
      ans=0,
      why="EK 2.4.A.3 states it directly: one atom substitutes for the other in the "
          "lattice. Sitting between the lattice positions is EK 2.4.A.2's interstitial "
          "case, and EK 2.4.A.1 puts the delocalized electrons around the ions rather "
          "than at their positions."),

 dict(q="Of the four tabulated candidate alloys, in which pair do the two radii differ by "
        "the smallest number of picometers?",
      table=_T_PAIRS,
      choices=["Pair 3", "Pair 1", "Pair 2", "Pair 4",
               "Pair 4, because its two radii are the smallest in the table"],
      ans=0,
      why="Subtracting the two tabulated radii in each row gives the difference directly, "
          "and EK 2.4.A.3 is what makes the smallest difference interesting, since "
          "comparable radius is the substitutional condition. Having small radii is not "
          "the same as having similar radii."),

 dict(q="Could an atom with a radius less than half that of its host substitute for the "
        "host in the lattice?",
      choices=[
        "No; substitution is the case the framework reserves for atoms of comparable "
        "radius, and an atom that much smaller fills the interstices instead",
        "Yes; any atom smaller than the host can occupy a lattice position",
        "Yes; substitution requires only that the two elements both be metals",
        "No; an atom that much smaller cannot enter the solid at all",
        "It depends only on how many valence electrons the added atom has"],
      ans=0,
      why="EK 2.4.A.3 conditions substitution on comparable radius and EK 2.4.A.2 assigns "
          "significantly different radii to the interstitial case, so the framework sends "
          "an atom half the host's size into the spaces between host atoms rather than "
          "into their positions."),

 dict(q="Reading the tabulated radii of the two named alloys, in which alloy is the added "
        "atom larger relative to the majority atom?",
      table=_T_NAMED,
      choices=["Alloy 2", "Alloy 1",
               "They are the same, since both are alloys of a metal",
               "Neither, since in both the added atom is smaller",
               "Alloy 1, because carbon is the added element in it"],
      ans=0,
      why="Dividing each tabulated added radius by its own majority radius compares the "
          "two alloys directly, and EK 2.4.A.2 and EK 2.4.A.3 are what make that ratio "
          "the quantity that decides which kind of alloy forms. In one alloy the added "
          "atom is in fact the larger of the two."),

 dict(q="How does the framework's model of a metallic solid differ from its model of an "
        "ionic solid?",
      choices=[
        "The metallic model has positive ions in a sea of delocalized valence electrons; "
        "the ionic model has cations and anions arranged together in an array",
        "The metallic model has cations and anions; the ionic model has positive ions in "
        "a sea of electrons",
        "The two models are the same, since both describe an array of ions",
        "The metallic model has neutral atoms; the ionic model has neutral molecules",
        "The metallic model has no charged particles at all"],
      ans=0,
      why="EK 2.4.A.1 gives the metallic model as an array of positive metal ions "
          "surrounded by delocalized valence electrons, while EK 2.3.A.1 gives the ionic "
          "model as cations and anions arranged in a periodic array. The delocalized "
          "electrons are what the ionic model has no counterpart for."),

 dict(q="Setting the host metal aside, which two of the tabulated candidate additions are "
        "closest to each other in radius?",
      table=_T_ELEMENTS,
      choices=[
        "Element A and Element D", "Element A and Element C", "Element C and Element D",
        "Element B and Element A", "Element B and Element C"],
      ans=0,
      why="Comparing the tabulated radii of the candidates with one another, rather than "
          "each with the host, identifies the closest pair. EK 2.4.A.3 is what makes "
          "closeness in radius the property worth measuring, since it is the condition "
          "for one atom to substitute for another."),

 dict(q="Which statement about alloys is NOT supported by the framework?",
      choices=[
        "An alloy must contain equal numbers of the two kinds of atom",
        "An alloy can form between atoms of comparable radius",
        "An alloy can form between atoms of significantly different radii",
        "In one kind of alloy the smaller atoms sit between the larger ones",
        "In one kind of alloy one atom takes the lattice position of another"],
      ans=0,
      why="EK 2.4.A.2 and EK 2.4.A.3 between them support every rejected statement here, "
          "conditioning the two alloy types on significantly different and on comparable "
          "radii respectively. Neither statement says anything about the numbers of the "
          "two kinds of atom, and the framework's own brass example describes zinc as a "
          "substituent rather than as half the solid."),

 dict(q="Two metals whose atoms have radii of 143 picometers and 141 picometers are "
        "melted together and allowed to solidify. Which kind of alloy does the framework "
        "predict, and where do the added atoms sit?",
      choices=[
        "A substitutional alloy, with the added atoms taking lattice positions of the host",
        "An interstitial alloy, with the added atoms in the spaces between host atoms",
        "A substitutional alloy, with the added atoms in the spaces between host atoms",
        "An interstitial alloy, with the added atoms taking lattice positions of the host",
        "No alloy at all, since alloys require atoms of significantly different radii"],
      ans=0,
      why="EK 2.4.A.3 conditions a substitutional alloy on comparable radius and places "
          "the substituting atom in the lattice, and the two radii stated in the problem "
          "differ by little more than one percent. EK 2.4.A.2's interstitial case needs "
          "radii that are significantly different."),

 dict(q="An added element whose atoms have a radius of 62 picometers is combined with a "
        "host metal whose atoms have a radius of 140 picometers. Which kind of alloy does "
        "the framework predict, and where do the added atoms sit?",
      choices=[
        "An interstitial alloy, with the added atoms filling the spaces between host atoms",
        "A substitutional alloy, with the added atoms taking lattice positions of the host",
        "An interstitial alloy, with the added atoms taking lattice positions of the host",
        "A substitutional alloy, with the added atoms filling the spaces between host atoms",
        "No alloy at all, since the added element is not a metal"],
      ans=0,
      why="EK 2.4.A.2 conditions an interstitial alloy on significantly different radii "
          "and places the smaller atoms in the interstitial spaces between the larger "
          "ones, and the added radius stated here is well under half the host's. The "
          "framework's own steel example pairs a nonmetal with a metal, so being a "
          "nonmetal is no bar to forming an alloy."),
]
