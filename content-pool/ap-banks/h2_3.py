r"""AP CHEMISTRY 2.3 Structure of Ionic Solids.

CED effective Fall 2024, Unit 2 Compound Structure and Properties.
Learning objective 2.3.A: represent an ionic solid with a particulate model
that is consistent with Coulomb's law and the properties of the constituent
ions.
Suggested skill 4.C, explain the connection between particulate-level and
macroscopic properties of a substance using models and representations.

Essential knowledge relied on, in the framework's own words:

  2.3.A.1  The cations and anions in an ionic crystal are arranged in a
           systematic, periodic 3-D array that maximizes the attractive forces
           among cations and anions while minimizing the repulsive forces.

           Exclusion Statement: Knowledge of specific crystal structures is not
           essential to an understanding of the learning objective and will not
           be assessed on the AP Exam.

THIS TOPIC HAS EXACTLY ONE ESSENTIAL KNOWLEDGE SENTENCE, which is the whole
difficulty of writing thirty items for it. The honest way to get thirty is not
to restate that sentence thirty times but to put it to work: LO 2.3.A itself
requires the model to be consistent with COULOMB'S LAW and with THE PROPERTIES
OF THE CONSTITUENT IONS, and EK 2.2.A.3 states what Coulomb's law says about
cations and anions. So fourteen items here are data items over tabulated ion
charges, ion radii and interionic distances, each asking a different question
of the numbers, and one is a stem-numeric comparison. Every one of those is
recomputed in verify_h2_3.py from the table or the stem alone.

THE EXCLUSION STATEMENT IS GATED, NOT JUST OBEYED. No item names a crystal
structure, a unit cell, a coordination number or a packing efficiency;
``no_named_lattice`` in the verifier asserts it, so the exclusion cannot quietly
be broken by a later edit.

WHAT IS NOT HERE. The macroscopic properties of ionic solids -- low vapor
pressure, high melting point, brittleness, conduction only when molten or
dissolved -- are EK 3.2.A.3 and belong to topic 3.2, so no key here rests on
them; ``no_macroscopic_property`` asserts that too. Which ions an element forms
and the formula that results are EK 1.8.A.3 and belong to topic 1.8. What is
left, and what this topic owns, is the ARRANGEMENT and why it is the
arrangement it is.

NO FIGURES. The bank cannot show a picture of a lattice, so the two model
items describe candidate models by their nearest neighbours in a table and ask
the question of the table.

NOTATION. Charges and distances are plain prose; formulas in prose stay plain
text (NaCl, MgO). No math spans are needed anywhere in this module.
"""
TOPIC = ("2.3", "Structure of Ionic Solids", 2)

_T_MODELS = dict(
    headers=["Proposed particulate model", "Nearest neighbors of each cation",
             "Nearest neighbors of each anion"],
    rows=[["Model 1", "anions only", "cations only"],
          ["Model 2", "cations only", "anions only"],
          ["Model 3", "a mixture of cations and anions in random positions",
           "a mixture of cations and anions in random positions"],
          ["Model 4", "anions only",
           "a mixture of cations and anions in random positions"]])

_T_CHARGE_DIST = dict(
    headers=["Ionic compound", "Charge on the cation", "Charge on the anion",
             "Distance between neighboring ion centers (picometers)"],
    rows=[["Compound W", "+1", "-1", "280"],
          ["Compound X", "+2", "-2", "290"],
          ["Compound Y", "+1", "-1", "230"],
          ["Compound Z", "+2", "-1", "260"]])

_T_DISTANCE_ONLY = dict(
    headers=["Ionic compound", "Charge on the cation", "Charge on the anion",
             "Distance between neighboring ion centers (picometers)"],
    rows=[["Compound J", "+1", "-1", "231"],
          ["Compound K", "+1", "-1", "282"],
          ["Compound L", "+1", "-1", "298"],
          ["Compound M", "+1", "-1", "323"]])

_T_CHARGE_ONLY = dict(
    headers=["Ionic compound", "Charge on the cation", "Charge on the anion",
             "Distance between neighboring ion centers (picometers)"],
    rows=[["Compound Q", "+1", "-1", "250"],
          ["Compound R", "+2", "-1", "250"],
          ["Compound S", "+2", "-2", "250"],
          ["Compound T", "+3", "-2", "250"]])

_T_RADII = dict(
    headers=["Ionic solid", "Radius of the cation (picometers)",
             "Radius of the anion (picometers)"],
    rows=[["Sample 1", "102", "133"],
          ["Sample 2", "102", "181"],
          ["Sample 3", "102", "196"],
          ["Sample 4", "102", "220"]])

QUESTIONS = [

 dict(q="How does the framework describe the arrangement of cations and anions in an "
        "ionic crystal?",
      choices=[
        "As a systematic, periodic three-dimensional array",
        "As a random three-dimensional packing with no repeating pattern",
        "As a single flat layer that repeats in two directions only",
        "As separate pairs of one cation and one anion, each pair held apart from the "
        "others",
        "As a fixed frame of anions through which the cations move freely"],
      ans=0,
      why="EK 2.3.A.1, verbatim in substance: the cations and anions in an ionic crystal "
          "are arranged in a systematic, periodic 3-D array. Each rejected option drops "
          "one of the three words the framework uses, and the last describes mobile ions, "
          "which the framework reserves for a molten or dissolved ionic solid."),

 dict(q="What does that arrangement accomplish, according to the framework?",
      choices=[
        "It maximizes the attractive forces among cations and anions while minimizing the "
        "repulsive forces",
        "It maximizes the repulsive forces, which is what holds the ions apart at fixed "
        "positions",
        "It makes the attractive and repulsive forces exactly equal, so that neither one "
        "dominates",
        "It minimizes the attractive forces and the repulsive forces together",
        "It maximizes the attractions between ions carrying the same sign of charge"],
      ans=0,
      why="EK 2.3.A.1, verbatim: the array maximizes the attractive forces among cations "
          "and anions while minimizing the repulsive forces. The two halves of that "
          "sentence point in the same direction rather than balancing against each other, "
          "which is what the rejected options get wrong."),

 dict(q="Four proposed particulate models of an ionic solid are summarized by what sits "
        "next to each ion. Which model is consistent with EK 2.3.A.1?",
      table=_T_MODELS,
      choices=["Model 1", "Model 2", "Model 3", "Model 4",
               "None of the four, since a periodic array cannot be summarized by naming "
               "nearest neighbors"],
      ans=0,
      why="EK 2.3.A.1 has the array maximize attraction among cations and anions while "
          "minimizing repulsion, and the only tabulated model that surrounds every cation "
          "with anions and every anion with cations is the one that does both at once. A "
          "model that surrounds a cation with cations raises exactly the repulsion the "
          "framework says the array minimizes."),

 dict(q="The table lists four ionic compounds with the charges on their ions and the "
        "distance between neighboring ion centers. In which compound is the interaction "
        "between neighboring ions strongest?",
      table=_T_CHARGE_DIST,
      choices=["Compound X", "Compound W", "Compound Y", "Compound Z",
               "They are all equal, because every compound is an ionic solid"],
      ans=0,
      why="LO 2.3.A requires the model of an ionic solid to be consistent with Coulomb's "
          "law, and EK 2.2.A.3 makes the strength grow with the charge on each ion and "
          "fall as the distance between ion centers grows. Both columns must be taken "
          "together: the largest charges here sit at very nearly the largest separation, "
          "and the charges still win."),

 dict(q="A particulate model of an ionic solid is required to be consistent with which "
        "two things?",
      choices=[
        "Coulomb's law and the properties of the constituent ions",
        "The ideal gas law and the temperature at which the solid was formed",
        "The mass of each ion and the measured density of the solid",
        "Coulomb's law alone, since the identities of the ions do not affect the "
        "arrangement",
        "The number of moles of solid present and the shape of its container"],
      ans=0,
      why="LO 2.3.A states the requirement in exactly those terms: represent an ionic "
          "solid with a particulate model that is consistent with Coulomb's law and the "
          "properties of the constituent ions. Dropping the second half is what makes one "
          "rejected option wrong, and the ideal gas law belongs to gases under EK 3.4.A.1."),

 dict(q="Four ionic compounds carry identical ion charges and differ only in the distance "
        "between neighboring ion centers. In which is the interaction strongest?",
      table=_T_DISTANCE_ONLY,
      choices=["Compound J", "Compound K", "Compound L", "Compound M",
               "They are all equal, since every tabulated charge is the same"],
      ans=0,
      why="EK 2.2.A.3.ii states that the interaction strength increases as the distance "
          "between the centers of the ions decreases, and the tabulated charges are "
          "identical, so the smallest separation gives the strongest interaction. LO "
          "2.3.A is what brings Coulomb's law to bear on the array in the first place."),

 dict(q="In the array the framework describes, what sits next to a given cation?",
      choices=[
        "Anions, since surrounding each cation with oppositely charged ions is what "
        "maximizes attraction and minimizes repulsion",
        "Other cations, packed as closely together as their sizes allow",
        "A mixture of cations and anions in no particular order",
        "Nothing else; each cation is paired with one anion and isolated from the rest",
        "Delocalized valence electrons shared among all the ions in the solid"],
      ans=0,
      why="EK 2.3.A.1 says the array maximizes attraction among cations and anions while "
          "minimizing repulsion, and placing anions around a cation is what does both. "
          "The delocalized electron option is EK 2.4.A.1's model of a metallic solid, not "
          "of an ionic one."),

 dict(q="Four ionic compounds have neighboring ion centers the same distance apart and "
        "differ only in the charges their ions carry. In which is the interaction "
        "strongest?",
      table=_T_CHARGE_ONLY,
      choices=["Compound T", "Compound Q", "Compound R", "Compound S",
               "They are all equal, since every tabulated separation is the same"],
      ans=0,
      why="EK 2.2.A.3.i states that the interaction strength is proportional to the charge "
          "on each ion, so with the separations tabulated as equal the largest product of "
          "the two charges gives the strongest interaction. LO 2.3.A is what requires the "
          "ionic model to answer to Coulomb's law."),

 dict(q="A student's model of an ionic solid places each cation in contact with several "
        "other cations and each anion in contact with several other anions. Why is that "
        "model inconsistent with the framework?",
      choices=[
        "It puts ions of like charge next to one another, which raises exactly the "
        "repulsive forces the array is described as minimizing",
        "It shows a three-dimensional array, whereas the framework describes a "
        "two-dimensional one",
        "It shows the ions touching, whereas the framework requires a gap between every "
        "pair of ions",
        "It shows equal numbers of cations and anions, which no ionic solid contains",
        "It is consistent, because Coulomb's law applies only to isolated pairs of ions"],
      ans=0,
      why="EK 2.3.A.1 says the array minimizes the repulsive forces, and the repulsions in "
          "an ionic solid are between ions of like charge, so an arrangement that makes "
          "like charges nearest neighbors works against the arrangement the framework "
          "describes."),

 dict(q="Four ionic solids are built from the same cation and from anions of different "
        "size, as the table records. Assuming every ion carries a single charge, in which "
        "solid is the interaction between neighboring ions strongest?",
      table=_T_RADII,
      choices=["Sample 1", "Sample 2", "Sample 3", "Sample 4",
               "They are all equal, since the cation is the same in every solid"],
      ans=0,
      why="The distance between neighboring ion centers is the sum of the two radii, so "
          "the solid with the smallest anion has the smallest separation. EK 2.2.A.3.ii "
          "then makes that the strongest interaction, and LO 2.3.A requires the model to "
          "reflect the properties of the constituent ions, of which radius is one."),

 dict(q="Two regions deep inside one crystal of an ionic solid are examined. What does "
        "the framework's description predict about the arrangement of ions in the two "
        "regions?",
      choices=[
        "The same arrangement is found in both, because the array is periodic throughout "
        "the solid",
        "The arrangements differ, because the ions settle into random positions as the "
        "solid forms",
        "The arrangement is orderly near the surface and disordered deeper inside",
        "The arrangement matches only if the two regions lie in the same flat layer",
        "No prediction is possible, because the framework describes only one cation and "
        "one anion"],
      ans=0,
      why="EK 2.3.A.1 calls the array systematic and periodic, and a periodic arrangement "
          "is one that repeats, so the same local arrangement recurs throughout the "
          "crystal rather than varying from place to place."),

 dict(q="Using the same four compounds tabulated with their charges and separations, in "
        "which is the interaction between neighboring ions weakest?",
      table=_T_CHARGE_DIST,
      choices=["Compound W", "Compound X", "Compound Y", "Compound Z",
               "Compound X, because it has the largest separation"],
      ans=0,
      why="EK 2.2.A.3 makes the strength rise with the charges and fall with the "
          "separation, so the weakest is the compound that combines the smallest charge "
          "product with a large separation. Ranking on separation alone points at the "
          "compound with the largest charges instead, which is why that reasoning is "
          "rejected."),

 dict(q="Two ionic solids are built from ions of about the same size. In the first the "
        "ions carry charges of one unit; in the second they carry two. What follows from "
        "Coulomb's law?",
      choices=[
        "The interactions in the second solid are stronger, because strength is "
        "proportional to the charge on each ion",
        "The interactions in the second solid are weaker, because larger charges repel "
        "more strongly",
        "The interactions are equal, because the ions are the same size",
        "The interactions in the second solid are stronger, but only because larger "
        "charges make ions smaller",
        "No comparison is possible without knowing the masses of the ions"],
      ans=0,
      why="EK 2.2.A.3.i states that because the interaction strength is proportional to "
          "the charge on each ion, larger charges lead to stronger interactions, and LO "
          "2.3.A brings that law to the ionic array. Size is stipulated equal, so charge "
          "is the only variable left."),

 dict(q="Among the four compounds that share their ion charges and differ only in "
        "separation, in which is the interaction weakest?",
      table=_T_DISTANCE_ONLY,
      choices=["Compound M", "Compound J", "Compound K", "Compound L",
               "Compound J, because the smallest separation gives the weakest interaction"],
      ans=0,
      why="EK 2.2.A.3.ii states that the interaction strength increases as the distance "
          "between ion centers decreases, so the largest tabulated separation gives the "
          "weakest interaction. The rejected option that names the smallest separation "
          "reverses the framework's sentence."),

 dict(q="A model shows an ionic solid as a collection of separate cation-anion pairs, "
        "each pair well away from every other pair. What does the framework describe "
        "instead?",
      choices=[
        "One continuous array in which every ion has oppositely charged neighbors on all "
        "sides",
        "The same separate pairs, but arranged so that they all lie in one plane",
        "The same separate pairs, but each containing two cations for every anion",
        "The same separate pairs, but free to slide past one another as in a liquid",
        "Nothing different; a formula unit is a separate particle within the solid"],
      ans=0,
      why="EK 2.3.A.1 describes a systematic, periodic three-dimensional ARRAY that "
          "maximizes attraction among cations and anions, which is a single extended "
          "arrangement rather than a set of isolated pairs; isolating each pair would "
          "give up most of the attractions the array is described as maximizing."),

 dict(q="Of the four compounds whose separations are all tabulated as equal, in which is "
        "the interaction between neighboring ions weakest?",
      table=_T_CHARGE_ONLY,
      choices=["Compound Q", "Compound R", "Compound S", "Compound T",
               "Compound T, because the largest charges give the weakest interaction"],
      ans=0,
      why="EK 2.2.A.3.i makes the strength proportional to the charge on each ion, so with "
          "every tabulated separation equal the smallest product of charges gives the "
          "weakest interaction. The rejected option that names the largest charges "
          "reverses the proportionality."),

 dict(q="Two ionic solids are built from ions carrying the same charges, but the ions in "
        "the first are noticeably smaller. Which solid has the stronger interactions "
        "between neighboring ions?",
      choices=[
        "The first, because smaller ions bring the ion centers closer together",
        "The second, because larger ions have more electrons to attract the cation",
        "The second, because a greater distance between centers strengthens the attraction",
        "Neither; ion size has no place in Coulomb's law",
        "The first, but only because smaller ions must carry larger charges"],
      ans=0,
      why="EK 2.2.A.3.ii states that because the interaction strength increases as the "
          "distance between the centers of the ions decreases, smaller ions lead to "
          "stronger interactions. The charges are stipulated equal, so the separation set "
          "by the ionic radii is what varies."),

 dict(q="Taking the same four solids built from one cation and anions of differing size, "
        "in which is the interaction between neighboring ions weakest?",
      table=_T_RADII,
      choices=["Sample 4", "Sample 1", "Sample 2", "Sample 3",
               "Sample 1, because the smallest anion gives the weakest interaction"],
      ans=0,
      why="Adding the two tabulated radii gives the distance between neighboring ion "
          "centers, and EK 2.2.A.3.ii makes the largest such distance the weakest "
          "interaction. LO 2.3.A is what requires the model of the solid to answer to the "
          "properties of the ions it is built from."),

 dict(q="A student draws every ion in an ionic solid as a circle of the same size and "
        "marks no charges on the drawing. Which requirement of the learning objective "
        "does the drawing fail to meet?",
      choices=[
        "That the model be consistent with the properties of the constituent ions, which "
        "include their charges and their relative sizes",
        "That the model show the ions in continuous random motion",
        "That the model be drawn in two dimensions rather than three",
        "That the model state how many moles of each ion the sample contains",
        "None of them, since the framework requires only that the ions alternate"],
      ans=0,
      why="LO 2.3.A requires a particulate model that is consistent with Coulomb's law and "
          "with the properties of the constituent ions; a drawing showing neither charge "
          "nor relative size carries none of those properties. Continuous random motion is "
          "EK 3.3.A.4's description of a gas, not of a solid array."),

 dict(q="Returning once more to the four compounds tabulated with both their charges and "
        "their separations, which has the second strongest interaction?",
      table=_T_CHARGE_DIST,
      choices=["Compound Z", "Compound W", "Compound X", "Compound Y",
               "The second strongest cannot be identified without the ionic radii"],
      ans=0,
      why="EK 2.2.A.3 makes both the charge product and the separation matter, so ranking "
          "all four requires combining the two columns rather than sorting on either. The "
          "separations are given directly, so no radius is needed to place the compounds "
          "in order."),

 dict(q="Why is a single flat sheet of alternating cations and anions an incomplete model "
        "of an ionic solid?",
      choices=[
        "Because the framework describes the array as three-dimensional, so a sheet leaves "
        "out the oppositely charged neighbors above and below each ion",
        "Because a flat sheet cannot alternate cations and anions at all",
        "Because the framework describes the array as one-dimensional",
        "Because a flat sheet would maximize repulsion rather than attraction",
        "It is not incomplete; the framework describes the array as a single sheet"],
      ans=0,
      why="EK 2.3.A.1 specifies a three-dimensional array, and a sheet supplies neighbors "
          "in only two directions, so it omits attractions the framework says the "
          "arrangement maximizes. A sheet can alternate charges perfectly well, which is "
          "why the second option fails."),

 dict(q="In the four tabulated solids built from a single cation, what is the only "
        "quantity that changes the distance between neighboring ion centers?",
      table=_T_RADII,
      choices=[
        "The radius of the anion",
        "The radius of the cation",
        "The charge on the cation",
        "The number of ions in the sample",
        "Nothing in the table; the distance is the same in all four solids"],
      ans=0,
      why="The tabulated cation radius is identical in all four rows while the anion radius "
          "varies, and the distance between neighboring ion centers is the sum of the two, "
          "so only the anion radius can move it. EK 2.2.A.3.ii is what makes that distance "
          "worth isolating."),

 dict(q="Which question about an ionic solid can be answered from the framework's "
        "description of the array alone?",
      choices=[
        "Why an arrangement that surrounds each ion with oppositely charged neighbors is "
        "favored over a random one",
        "Which named crystal structure a particular ionic compound adopts",
        "How many ions lie within one unit cell of a named lattice",
        "What fraction of the volume of a named lattice is occupied by ions",
        "How many nearest neighbors surround an ion in a named lattice"],
      ans=0,
      why="EK 2.3.A.1 states that the array maximizes attraction among cations and anions "
          "while minimizing repulsion, which is enough to say why alternation is favored. "
          "The topic's exclusion statement puts knowledge of specific crystal structures "
          "outside what is assessed, and every rejected option asks for exactly that."),

 dict(q="Of those four compounds tabulated with charges and separations, which comparison "
        "isolates the effect of the distance between ion centers?",
      table=_T_CHARGE_DIST,
      choices=[
        "Compound W against Compound Y, which carry the same charges at different "
        "separations",
        "Compound W against Compound X, which differ in charge and in separation",
        "Compound X against Compound Z, which differ in charge and in separation",
        "Compound Y against Compound Z, which differ in charge and in separation",
        "No tabulated comparison isolates distance, since every pair differs in charge"],
      ans=0,
      why="Isolating one variable means holding the other fixed, and exactly one tabulated "
          "pair shares its charges while differing in separation. EK 2.2.A.3 makes both "
          "quantities relevant, which is why an uncontrolled comparison cannot attribute "
          "a difference to either one."),

 dict(q="An ionic solid built from small, highly charged ions is compared with one built "
        "from large, singly charged ions. What does Coulomb's law predict about the "
        "interactions in the two arrays?",
      choices=[
        "Stronger in the first, because a larger charge and a smaller separation both "
        "raise the interaction strength",
        "Weaker in the first, because small ions present less surface for contact",
        "Equal, because the arrangement of the array is what fixes the strength",
        "Stronger in the first, but only on account of the charges, since size has no "
        "place in Coulomb's law",
        "Weaker in the first, because a higher charge raises repulsion more than "
        "attraction"],
      ans=0,
      why="EK 2.2.A.3.i and 2.2.A.3.ii each state one half of the answer, that larger "
          "charges strengthen the interaction and that smaller ions do as well by bringing "
          "the centers closer, and here the two point the same way rather than opposing "
          "each other."),

 dict(q="Among the compounds whose tabulated separations are equal, which has an "
        "interaction exactly twice as strong as that in Compound Q?",
      table=_T_CHARGE_ONLY,
      choices=["Compound R", "Compound S", "Compound T",
               "None of them, because doubling a charge quadruples the interaction",
               "All of them, because each carries a larger charge than Compound Q"],
      ans=0,
      why="EK 2.2.A.3.i makes the strength proportional to the charge on each ion, so at a "
          "fixed separation the ratio of two interactions is the ratio of the products of "
          "their charges, and exactly one tabulated compound gives a product twice that of "
          "the reference compound."),

 dict(q="Which feature of a drawn particulate model most directly reflects the "
        "requirement that the model be consistent with Coulomb's law?",
      choices=[
        "Oppositely charged ions drawn as near neighbors, with like charges kept farther "
        "apart",
        "Every ion drawn as a circle of the same diameter",
        "The ions drawn in constant motion past one another",
        "A count of ions in the drawing equal to Avogadro's number",
        "An equal number of cations and anions in every drawing, whatever their charges"],
      ans=0,
      why="Coulomb's law under EK 2.2.A.3 makes attraction between opposite charges "
          "stronger at shorter distances and repulsion between like charges stronger at "
          "shorter distances, so a drawing answers to it by placing unlike charges close "
          "and like charges far. EK 2.3.A.1 is the arrangement that results."),

 dict(q="Which statement describes how the interaction strength varies across the four "
        "compounds that share their ion charges?",
      table=_T_DISTANCE_ONLY,
      choices=[
        "It weakens steadily as the separation between ion centers grows",
        "It strengthens steadily as the separation between ion centers grows",
        "It is identical in all four, because every compound carries the same charges",
        "It weakens at first and then strengthens again at the largest separation",
        "No pattern can be stated, because the ionic radii are not tabulated"],
      ans=0,
      why="EK 2.2.A.3.ii states that the interaction strength increases as the distance "
          "between the centers of the ions decreases, so with the charges held equal the "
          "strength falls monotonically as the tabulated separation rises. The separations "
          "are given directly, so the radii are not needed."),

 dict(q="Which statement about an ionic crystal is NOT supported by the framework's "
        "description of its structure?",
      choices=[
        "Each formula unit exists inside the solid as a separate molecule",
        "The arrangement of the ions repeats throughout the crystal",
        "The arrangement extends in three dimensions",
        "The arrangement keeps ions of like charge from being nearest neighbors",
        "The arrangement can be understood using Coulomb's law"],
      ans=0,
      why="EK 2.3.A.1 describes a systematic, periodic three-dimensional array maximizing "
          "attraction among cations and anions, and LO 2.3.A adds consistency with "
          "Coulomb's law, which supports each of the rejected statements. Nothing in the "
          "framework describes a separate molecular unit inside that array."),

 dict(q="Sodium chloride is built from ions carrying charges of +1 and -1, and magnesium "
        "oxide from ions carrying +2 and -2. The distance between neighboring ion centers "
        "is nearly the same in the two solids. By roughly what factor is the Coulombic "
        "interaction in magnesium oxide larger?",
      choices=["About four times", "About twice", "About half",
               "About sixteen times", "About the same, since the separations match"],
      ans=0,
      why="EK 2.2.A.3.i makes the interaction strength proportional to the charge on each "
          "ion, so doubling both charges multiplies the product of the charges by two "
          "twice over while the separation, stipulated to be nearly equal, contributes "
          "nothing. LO 2.3.A is what puts Coulomb's law to work on the ionic array."),
]
