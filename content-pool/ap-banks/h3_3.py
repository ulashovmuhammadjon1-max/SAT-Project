r"""AP CHEMISTRY 3.3 Solids, Liquids, and Gases.

CED effective Fall 2024, Unit 3 Properties of Substances and Mixtures.
Learning objective 3.3.A: represent the differences between solid, liquid, and
gas phases using a particulate-level model.
Suggested skill 3.C, represent visually the relationship between the structures
and interactions across multiple levels or scales.

Essential knowledge relied on, in the framework's own words:

  3.3.A.1  Solids can be crystalline, where the particles are arranged in a
           regular three-dimensional structure, or they can be amorphous, where
           the particles do not have a regular, orderly arrangement. In both
           cases, the motion of the individual particles is limited, and the
           particles do not undergo overall translation with respect to each
           other. The structure of the solid is influenced by interparticle
           interactions and the ability of the particles to pack together.
  3.3.A.2  The constituent particles in liquids are in close contact with each
           other, and they are continually moving and colliding. The arrangement
           and movement of particles are influenced by the nature and strength
           of the forces (e.g., polarity, hydrogen bonding, and temperature)
           between the particles.
  3.3.A.3  The solid and liquid phases for a particular substance typically have
           similar molar volume because, in both phases, the constituent
           particles are in close contact at all times.
  3.3.A.4  In the gas phase, the particles are in constant motion. Their
           frequencies of collision and the average spacing between them are
           dependent on temperature, pressure, and volume. Because of this
           constant motion, and minimal effects of forces between particles, a
           gas has neither a definite volume nor a definite shape.

           Exclusion Statement: Understanding/interpreting phase diagrams will
           not be assessed on the AP Exam.

WHAT THE FRAMEWORK SAYS ABOUT EACH PHASE, AND WHAT IT DOES NOT. The three
statements are not parallel: the solid gets an internal distinction
(crystalline against amorphous) that the other two do not; the liquid gets a
list of influences that the solid's structure statement words differently; and
only the gas is told what its collision frequency and spacing depend on.
verify_h3_3.py transcribes the properties the framework attaches to each phase
and checks every phase item against that transcription, so an item asking
"which phase" can only be keyed to a phase the CED actually says it of.

TWO HEDGES ARE KEPT. EK 3.3.A.3 says the solid and liquid molar volumes are
TYPICALLY similar, not always; and EK 3.3.A.4 says forces between gas particles
have MINIMAL effects, not none. Items 26 and 27 are those two hedges, and no
key anywhere states either claim without its qualifier.

THE EXCLUSION STATEMENT is keyed as content in item 13: phase diagrams will not
be assessed, and no item here asks a student to read or interpret one.

NO FIGURES. LO 3.3.A is about particulate-level MODELS and this bank cannot show
one, so items ask what such a model would have to show rather than asking one to
be read, and the comparative items put the phases in a table.

NOTATION. Plain prose throughout. No math spans are needed in this module.
"""
TOPIC = ("3.3", "Solids, Liquids, and Gases", 3)

_T_PHASES = dict(
    headers=["Sample", "Phase"],
    rows=[["Sample 1", "solid"],
          ["Sample 2", "liquid"],
          ["Sample 3", "gas"]])

QUESTIONS = [

 dict(q="How does the framework describe a crystalline solid?",
      choices=[
        "Its particles are arranged in a regular three-dimensional structure",
        "Its particles have no regular, orderly arrangement",
        "Its particles are in constant motion through the whole sample",
        "Its particles are far apart and rarely collide",
        "Its particles translate freely with respect to one another"],
      ans=0,
      why="EK 3.3.A.1 defines it in those words: solids can be crystalline, where the "
          "particles are arranged in a regular three-dimensional structure. The absence of "
          "a regular arrangement is what the same sentence calls amorphous instead."),

 dict(q="How does the framework describe an amorphous solid?",
      choices=[
        "Its particles do not have a regular, orderly arrangement",
        "Its particles are arranged in a regular three-dimensional structure",
        "It has no particles in contact with one another",
        "Its particles undergo overall translation with respect to each other",
        "It has neither a definite volume nor a definite shape"],
      ans=0,
      why="EK 3.3.A.1 defines it in those words: they can be amorphous, where the particles "
          "do not have a regular, orderly arrangement. Having neither a definite volume nor "
          "a definite shape is what EK 3.3.A.4 says of a gas, not of any solid."),

 dict(q="What does the framework say is true of the particles in BOTH crystalline and "
        "amorphous solids?",
      choices=[
        "The motion of the individual particles is limited, and they do not undergo overall "
        "translation with respect to each other",
        "The particles are motionless and do not vibrate at all",
        "The particles move freely past one another while staying in contact",
        "The particles are arranged in a regular three-dimensional structure",
        "The particles are far apart and interact only on collision"],
      ans=0,
      why="EK 3.3.A.1 says exactly this of both cases: in BOTH cases, the motion of the "
          "individual particles is limited, and the particles do not undergo overall "
          "translation with respect to each other. Limited motion is not the same as no "
          "motion, which the framework nowhere claims."),

 dict(q="What does the framework say influences the structure of a solid?",
      choices=[
        "Interparticle interactions and the ability of the particles to pack together",
        "The pressure of the surrounding atmosphere alone",
        "The volume of the container the solid is held in",
        "The frequency with which the particles collide",
        "The mass of one mole of the substance"],
      ans=0,
      why="EK 3.3.A.1 names both influences in its own words. Collision frequency is what "
          "EK 3.3.A.4 discusses for a gas, and the container's volume matters for a gas "
          "rather than for a solid, since only a gas has no definite volume."),

 dict(q="How does the framework describe the constituent particles in a liquid?",
      choices=[
        "In close contact with each other, and continually moving and colliding",
        "In close contact with each other, and held motionless in fixed positions",
        "Far apart from each other, and continually moving and colliding",
        "Arranged in a regular three-dimensional structure",
        "Unable to undergo any translation with respect to each other"],
      ans=0,
      why="EK 3.3.A.2 states both halves: the constituent particles in liquids are in close "
          "contact with each other, and they are continually moving and colliding. Each "
          "rejected option keeps one half and swaps the other for a solid's or a gas's "
          "description."),

 dict(q="What does the framework say influences the arrangement and movement of particles "
        "in a liquid?",
      choices=[
        "The nature and strength of the forces between the particles",
        "The shape of the container alone",
        "The number of moles of liquid present",
        "The regularity of the three-dimensional structure",
        "The frequency of collisions with the container walls"],
      ans=0,
      why="EK 3.3.A.2 states it in those words: the arrangement and movement of particles "
          "are influenced by the nature and strength of the forces between the particles. "
          "Both the nature and the strength are named, so neither alone is the whole "
          "answer."),

 dict(q="Which examples does the framework give of what influences the arrangement and "
        "movement of particles in a liquid?",
      choices=[
        "Polarity, hydrogen bonding, and temperature",
        "Mass, density, and color",
        "Container shape, container material, and container volume",
        "Atomic number, mass number, and isotopic abundance",
        "Crystalline structure, amorphous structure, and packing efficiency"],
      ans=0,
      why="EK 3.3.A.2 lists those three in parentheses as its own examples. Packing "
          "together is what EK 3.3.A.1 names for the structure of a solid, which is a "
          "different statement about a different phase."),

 dict(q="What does the framework say about the molar volumes of the solid and liquid "
        "phases of one substance?",
      choices=[
        "They typically have similar molar volume",
        "They typically differ by a factor of about a thousand",
        "The solid always has the larger molar volume",
        "The liquid always has the larger molar volume",
        "The framework makes no comparison between them"],
      ans=0,
      why="EK 3.3.A.3 states it directly: the solid and liquid phases for a particular "
          "substance typically have similar molar volume. The framework does make the "
          "comparison, and it hedges it with typically rather than stating it without "
          "exception."),

 dict(q="What reason does the framework give for the solid and liquid phases having "
        "similar molar volume?",
      choices=[
        "In both phases the constituent particles are in close contact at all times",
        "In both phases the particles are arranged in a regular three-dimensional structure",
        "In both phases the particles are motionless",
        "In both phases the particles are far apart",
        "In both phases the particles undergo overall translation"],
      ans=0,
      why="EK 3.3.A.3 gives the reason in its own words: because, in both phases, the "
          "constituent particles are in close contact at all times. A regular structure is "
          "only one of the two kinds of solid EK 3.3.A.1 allows, so it cannot be what both "
          "phases share."),

 dict(q="How does the framework describe the particles in the gas phase?",
      choices=[
        "They are in constant motion",
        "Their motion is limited and they do not translate with respect to each other",
        "They are in close contact at all times",
        "They are arranged in a regular three-dimensional structure",
        "They move only when the temperature is raised"],
      ans=0,
      why="EK 3.3.A.4 opens with it: in the gas phase, the particles are in constant "
          "motion. Limited motion without overall translation is EK 3.3.A.1's description "
          "of a solid, and close contact at all times is EK 3.3.A.3's of the condensed "
          "phases."),

 dict(q="On what does the framework say the collision frequency and average spacing of gas "
        "particles depend?",
      choices=[
        "On temperature, pressure, and volume",
        "On temperature alone",
        "On the mass of the container",
        "On the regularity of the particles' arrangement",
        "On the strength of the forces between the particles"],
      ans=0,
      why="EK 3.3.A.4 names all three: their frequencies of collision and the average "
          "spacing between them are dependent on temperature, pressure, and volume. The "
          "same statement makes the effects of forces between gas particles minimal rather "
          "than what the spacing depends on."),

 dict(q="What reason does the framework give for a gas having neither a definite volume "
        "nor a definite shape?",
      choices=[
        "The constant motion of its particles, together with minimal effects of forces "
        "between them",
        "The strong forces between its particles",
        "The regular three-dimensional arrangement of its particles",
        "The close contact of its particles at all times",
        "The limited motion of its individual particles"],
      ans=0,
      why="EK 3.3.A.4 gives both parts of the reason in one clause: because of this "
          "constant motion, and minimal effects of forces between particles, a gas has "
          "neither a definite volume nor a definite shape. Each rejected option offers a "
          "property the framework attributes to a condensed phase instead."),

 dict(q="What does the framework's exclusion statement for this topic place outside the "
        "exam?",
      choices=[
        "Understanding and interpreting phase diagrams",
        "The distinction between crystalline and amorphous solids",
        "The comparison of solid and liquid molar volumes",
        "The dependence of gas particle spacing on temperature",
        "The description of a liquid's particles as continually colliding"],
      ans=0,
      why="The exclusion statement attached to EK 3.3.A.4 says understanding and "
          "interpreting phase diagrams will not be assessed on the AP Exam. The four "
          "rejected options are each stated as required content in EK 3.3.A.1 through "
          "3.3.A.4."),

 dict(q="Which internal distinction does the framework draw within one phase and not "
        "within the others?",
      choices=[
        "Solids may be crystalline or amorphous",
        "Liquids may be crystalline or amorphous",
        "Gases may be crystalline or amorphous",
        "Liquids may be polar or nonpolar",
        "Gases may be definite or indefinite in volume"],
      ans=0,
      why="EK 3.3.A.1 divides solids into crystalline and amorphous cases, and neither EK "
          "3.3.A.2 nor EK 3.3.A.4 draws any such division within the liquid or the gas "
          "phase. The distinction is about the regularity of the arrangement, which "
          "presupposes an arrangement of the kind only a solid has."),

 dict(q="EK 3.3.A.1 says the particles in a solid do not undergo overall translation with "
        "respect to each other. What does that leave room for?",
      choices=[
        "Limited motion of the individual particles",
        "No motion of any kind whatsoever",
        "Free movement of particles past one another",
        "Particles leaving the sample entirely",
        "Particles rearranging into a regular structure from an amorphous one"],
      ans=0,
      why="EK 3.3.A.1 pairs the two claims in one sentence: the motion of the individual "
          "particles is LIMITED, and the particles do not undergo overall translation with "
          "respect to each other. Limited motion is asserted, so a claim of no motion at "
          "all goes beyond the statement."),

 dict(q="Three samples are tabulated by phase. In which does the framework say the "
        "particles do not undergo overall translation with respect to each other?",
      table=_T_PHASES,
      choices=["Sample 1", "Sample 2", "Sample 3",
               "In all three, since particles always keep their relative positions",
               "In none of them, since particles are always in motion"],
      ans=0,
      why="EK 3.3.A.1 makes that claim of solids, in both the crystalline and the amorphous "
          "case. EK 3.3.A.2 has a liquid's particles continually moving and colliding and "
          "EK 3.3.A.4 has a gas's in constant motion, so neither carries the claim."),

 dict(q="Using the same tabulated samples, in which does the framework say the particles "
        "are in close contact and continually moving and colliding?",
      table=_T_PHASES,
      choices=["Sample 2", "Sample 1", "Sample 3",
               "In all three, since particles collide in every phase",
               "In none of them, since close contact prevents collision"],
      ans=0,
      why="EK 3.3.A.2 says exactly that of liquids. A solid's particles have limited motion "
          "under EK 3.3.A.1, and a gas's are not described as being in close contact "
          "anywhere in EK 3.3.A.4."),

 dict(q="Of the tabulated samples, which does the framework say has neither a definite "
        "volume nor a definite shape?",
      table=_T_PHASES,
      choices=["Sample 3", "Sample 1", "Sample 2",
               "All three, since volume and shape always depend on the container",
               "None of them; the framework does not discuss volume or shape"],
      ans=0,
      why="EK 3.3.A.4 makes that claim of the gas phase, and gives the reason as the "
          "particles' constant motion together with minimal effects of forces between "
          "them. No such claim is made of either condensed phase."),

 dict(q="For which of the tabulated samples does the framework say the molar volumes are "
        "typically similar?",
      table=_T_PHASES,
      choices=[
        "For Sample 1 and Sample 2",
        "For Sample 1 and Sample 3",
        "For Sample 2 and Sample 3",
        "For all three samples equally",
        "For none of them; the framework compares no molar volumes"],
      ans=0,
      why="EK 3.3.A.3 compares the solid and liquid phases of one substance and says they "
          "typically have similar molar volume, because in both the particles are in close "
          "contact at all times. The gas phase is not part of that comparison."),

 dict(q="In which of the tabulated samples does the framework say the motion of the "
        "individual particles is limited?",
      table=_T_PHASES,
      choices=["Sample 1", "Sample 2", "Sample 3",
               "In all three, since motion is limited by the container in every case",
               "In none of them; the framework never limits particle motion"],
      ans=0,
      why="EK 3.3.A.1 says the motion of the individual particles is limited in solids, in "
          "both the crystalline and the amorphous case. Continual movement and constant "
          "motion are what EK 3.3.A.2 and EK 3.3.A.4 say of the other two phases."),

 dict(q="Of the tabulated samples, in which does the framework say the particles are in "
        "constant motion?",
      table=_T_PHASES,
      choices=["Sample 3", "Sample 1", "Sample 2",
               "In all three, since every particle is always moving",
               "In none of them; the framework describes no phase that way"],
      ans=0,
      why="EK 3.3.A.4 opens by saying that in the gas phase the particles are in constant "
          "motion. EK 3.3.A.2's liquid particles are continually moving and colliding, "
          "which is a separate statement about a different phase, and EK 3.3.A.1's solid "
          "particles have limited motion."),

 dict(q="For how many of the tabulated samples does the framework say the particles are in "
        "close contact?",
      table=_T_PHASES,
      choices=["Exactly two", "Exactly one", "All three", "None of them",
               "The framework never uses the phrase close contact"],
      ans=0,
      why="EK 3.3.A.2 puts a liquid's particles in close contact with each other, and EK "
          "3.3.A.3 says that in BOTH the solid and liquid phases the constituent particles "
          "are in close contact at all times. Nothing of the kind is said of a gas."),

 dict(q="For which tabulated sample does the framework say the collision frequency and "
        "average particle spacing depend on temperature, pressure and volume?",
      table=_T_PHASES,
      choices=["Sample 3", "Sample 1", "Sample 2",
               "For all three, since every phase responds to those three variables",
               "For none of them; the framework names no such dependence"],
      ans=0,
      why="EK 3.3.A.4 attaches that dependence to the gas phase specifically. The framework "
          "names influences on the other two phases in different terms: interparticle "
          "interactions and packing for a solid, and the nature and strength of the forces "
          "for a liquid."),

 dict(q="Which tabulated sample does the framework say may be either crystalline or "
        "amorphous?",
      table=_T_PHASES,
      choices=["Sample 1", "Sample 2", "Sample 3",
               "All three, since any phase can be ordered or disordered",
               "None of them; the framework does not use those terms"],
      ans=0,
      why="EK 3.3.A.1 divides solids into crystalline and amorphous cases and draws no such "
          "division within either of the other phases. The distinction concerns the "
          "regularity of an arrangement, which the framework attributes only to a solid."),

 dict(q="For which tabulated sample does the framework name polarity and hydrogen bonding "
        "among the influences on its particles?",
      table=_T_PHASES,
      choices=["Sample 2", "Sample 1", "Sample 3",
               "For all three, since intermolecular forces act in every phase",
               "For none of them; those terms belong to unit 2 alone"],
      ans=0,
      why="EK 3.3.A.2 gives polarity, hydrogen bonding and temperature as its examples of "
          "what influences the arrangement and movement of particles in a liquid. EK "
          "3.3.A.1 words the solid's influences differently, as interparticle interactions "
          "and the ability to pack together."),

 dict(q="EK 3.3.A.3 says the solid and liquid molar volumes are TYPICALLY similar. What "
        "does that wording rule out?",
      choices=[
        "Treating the similarity as holding for every substance without exception",
        "Treating the two molar volumes as similar in general",
        "Treating the particles as being in close contact in both phases",
        "Treating molar volume as a property worth comparing",
        "Treating the solid and liquid as phases of one substance"],
      ans=0,
      why="EK 3.3.A.3's word is typically, which asserts a general pattern rather than an "
          "exceptionless rule. The four rejected statements are each part of what the "
          "sentence does assert."),

 dict(q="EK 3.3.A.4 refers to MINIMAL effects of forces between gas particles. What does "
        "that wording avoid claiming?",
      choices=[
        "That there are no forces between gas particles at all",
        "That the effects of those forces are small",
        "That gas particles are in constant motion",
        "That a gas has no definite shape",
        "That collision frequency depends on temperature"],
      ans=0,
      why="EK 3.3.A.4 says minimal effects rather than none, so the statement leaves the "
          "forces in existence while making their effects small. Topic 3.6 then treats the "
          "deviations that arise when those effects are not negligible, which would be "
          "impossible if the framework had denied the forces here."),

 dict(q="A student compares a liquid with a gas. Which phase does the framework describe "
        "as having its particles in close contact?",
      choices=[
        "The liquid, whose particles the framework places in close contact with each other",
        "The gas, whose particles the framework places in close contact with each other",
        "Both, since particles touch in every phase",
        "Neither, since the framework describes contact only for solids",
        "It depends on the temperature, which the framework leaves open"],
      ans=0,
      why="EK 3.3.A.2 puts a liquid's constituent particles in close contact with each "
          "other, while EK 3.3.A.4 describes a gas by the average spacing between its "
          "particles and by the minimal effects of forces between them, which is the "
          "opposite picture."),

 dict(q="EK 3.3.A.3's comparison of molar volumes covers which phases?",
      choices=[
        "The solid and liquid phases of a particular substance",
        "The solid and gas phases of a particular substance",
        "The liquid and gas phases of a particular substance",
        "All three phases of a particular substance",
        "The same phase of two different substances"],
      ans=0,
      why="EK 3.3.A.3 names the solid and liquid phases FOR A PARTICULAR SUBSTANCE, and "
          "gives as its reason that in both of those phases the particles are in close "
          "contact at all times. The gas phase does not enter that statement."),

 dict(q="Which statement about the phases is NOT supported by the framework?",
      choices=[
        "The particles of a solid are completely motionless",
        "The particles of a solid do not undergo overall translation with respect to each "
        "other",
        "The particles of a liquid are continually moving and colliding",
        "The particles of a gas are in constant motion",
        "A solid may be crystalline or amorphous"],
      ans=0,
      why="EK 3.3.A.1 says the motion of the individual particles in a solid is LIMITED, "
          "which asserts motion rather than denying it, so complete motionlessness "
          "contradicts the statement. The four rejected options are each stated in EK "
          "3.3.A.1, 3.3.A.2 or 3.3.A.4."),
]
