r"""AP CHEMISTRY 3.6 Deviation from Ideal Gas Law.

CED effective Fall 2024, Unit 3 Properties of Substances and Mixtures.
Learning objective 3.6.A: explain the relationship among non-ideal behaviors of
gases, interparticle forces, and/or volumes.
Suggested skill 6.E, provide reasoning to justify a claim using connections
between particulate and macroscopic scales or levels.

Essential knowledge relied on, in the framework's own words -- there is exactly
one statement in this topic:

  3.6.A.1  The ideal gas law does not explain the actual behavior of real gases.
           Deviations from the ideal gas law may result from interparticle
           attractions among gas molecules, particularly at conditions that are
           close to those resulting in condensation. Deviations may also arise
           from particle volumes, particularly at extremely high pressures.

WHAT THE FRAMEWORK DOES NOT SAY, AND WHY NO KEY HERE SAYS IT. EK 3.6.A.1 names
two SOURCES of deviation and the conditions under which each becomes important.
It says nothing about the DIRECTION of the deviation -- not that a real gas
exerts a pressure below the ideal value, not that it occupies more volume than
predicted. That directional claim is what a textbook adds and what this topic's
sentence withholds, so it appears here only as a distractor, and
verify_h3_6.py refuses any key that states it. The same goes for the hedge: the
framework says deviations MAY result, so no key asserts that a real gas always
deviates.

THE PAIRING THAT MUST NOT SHIP BACKWARDS. Attractions go with conditions close
to those resulting in CONDENSATION; particle volumes go with EXTREMELY HIGH
PRESSURES. Swapping them is the single most likely defect in a topic with one
sentence in it, so verify_h3_6.py parses every key that pairs a cause with a
condition and asserts the pairing runs the framework's way, using named
booleans rather than two tuples read as parallel.

THE TWO-STEP TRACES, stated so a reader can check them. Two items reach past
this topic's single sentence and both cite what they use: EK 3.1.A.2 makes
interactions between polar molecules typically greater than those between
nonpolar molecules of comparable size, which is why the polar gas of a
comparable pair is the one EK 3.6.A.1's first cause bites harder on; and
EK 3.6.A.1's own words attach the second cause to particle VOLUMES, which is
why a gas whose particles occupy more space is the one it bites harder on at
extremely high pressure. Nothing else is imported.

NO FIGURES. Every set of conditions is carried as a table.

ARITHMETIC. Every ranking and every margin asserted by a key is recomputed in
verify_h3_6.py from the table alone.

NOTATION. Plain prose; no math spans are needed in this module.
"""
TOPIC = ("3.6", "Deviation from Ideal Gas Law", 3)

# How close each sample sits to the conditions that would produce condensation,
# given as the gas temperature against the substance's boiling point.
_T_COND = dict(
    headers=["Sample", "Temperature of the gas (K)", "Boiling point of the substance (K)"],
    rows=[["Sample 1", "400", "100"],
          ["Sample 2", "250", "240"],
          ["Sample 3", "600", "90"]])

_T_PRESS = dict(
    headers=["Sample", "Pressure (atm)"],
    rows=[["Sample J", "1.0"],
          ["Sample K", "40"],
          ["Sample L", "900"]])

# Both of EK 3.6.A.1's conditions at once, for the four corner cases.
_T_BOTH = dict(
    headers=["Sample", "Pressure (atm)", "Kelvins above the boiling point"],
    rows=[["Sample P", "1.0", "300"],
          ["Sample Q", "900", "5"],
          ["Sample R", "1.0", "5"],
          ["Sample S", "900", "300"]])

_T_BP = dict(
    headers=["Gas", "Boiling point (K)"],
    rows=[["Gas D", "112"],
          ["Gas E", "240"],
          ["Gas F", "85"]])

_T_SIZE = dict(
    headers=["Gas", "Volume occupied by the particles in one mole (mL)"],
    rows=[["Gas T", "17"],
          ["Gas U", "32"],
          ["Gas V", "64"]])

QUESTIONS = [

 dict(q="What does the framework say about the ideal gas law and the behavior of real "
        "gases?",
      choices=[
        "The ideal gas law does not explain the actual behavior of real gases",
        "The ideal gas law explains the actual behavior of real gases exactly",
        "The ideal gas law always predicts a pressure lower than the measured one",
        "The ideal gas law applies to real gases only below one atmosphere",
        "The ideal gas law describes real liquids rather than real gases"],
      ans=0,
      why="EK 3.6.A.1 opens with that sentence. It states a limitation without saying which "
          "way a measurement will miss, so a claim about the direction of the miss goes "
          "further than the framework does."),

 dict(q="Which two sources of deviation from the ideal gas law does the framework name?",
      choices=[
        "Interparticle attractions among gas molecules, and particle volumes",
        "The mass of the container, and the number of moles present",
        "The molar mass of the gas, and the value of the gas constant",
        "The shape of the container, and the material it is made of",
        "The colour of the gas, and the wavelength of light used to observe it"],
      ans=0,
      why="EK 3.6.A.1 names exactly those two: deviations may result from interparticle "
          "attractions among gas molecules, and deviations may also arise from particle "
          "volumes. No property of the container appears in the statement at all."),

 dict(q="Under what conditions does the framework say interparticle attractions produce "
        "deviations from the ideal gas law?",
      choices=[
        "At conditions close to those resulting in condensation",
        "At extremely high pressures",
        "At extremely low pressures",
        "At any conditions whatsoever, equally",
        "Only when the gas is a mixture of two or more substances"],
      ans=0,
      why="EK 3.6.A.1 attaches that cause to conditions that are close to those resulting in "
          "condensation. Extremely high pressure is the condition the same sentence attaches "
          "to the OTHER named cause."),

 dict(q="Under what conditions does the framework say particle volumes produce deviations "
        "from the ideal gas law?",
      choices=[
        "At extremely high pressures",
        "At conditions close to those resulting in condensation",
        "At extremely low pressures",
        "At any conditions whatsoever, equally",
        "Only for gases whose molecules carry a dipole moment"],
      ans=0,
      why="EK 3.6.A.1 says deviations may also arise from particle volumes, particularly at "
          "extremely high pressures. Nearness to condensation is the condition the same "
          "sentence attaches to the other named cause."),

 dict(q="A sample of a real gas is cooled and compressed until it is nearly at the point of "
        "condensing. Which named source of deviation does the framework make responsible?",
      choices=[
        "Interparticle attractions among gas molecules",
        "The volumes of the particles themselves",
        "The mass of the gas sample",
        "The volume of the container",
        "The value of the gas constant"],
      ans=0,
      why="EK 3.6.A.1 ties interparticle attractions to conditions that are close to those "
          "resulting in condensation, which is exactly the situation described. Particle "
          "volume is tied by the same sentence to extremely high pressure instead."),

 dict(q="A sample of a real gas is compressed to an extremely high pressure while staying "
        "far above the temperature at which it would condense. Which named source of "
        "deviation does the framework make responsible?",
      choices=[
        "The volumes of the particles themselves",
        "Interparticle attractions among gas molecules",
        "The mass of the container",
        "The number of moles present",
        "The identity of the gas alone"],
      ans=0,
      why="EK 3.6.A.1 says deviations may also arise from particle volumes, particularly at "
          "extremely high pressures. The sample is far from the conditions the same sentence "
          "attaches to interparticle attractions."),

 dict(q="Which of the following does the framework give as a source of deviation from the "
        "ideal gas law?",
      choices=[
        "The volumes of the particles themselves",
        "The material the container is made of",
        "The number of moles of gas present",
        "The molar mass of the gas",
        "The precision of the pressure gauge"],
      ans=0,
      why="EK 3.6.A.1 names particle volumes as one of its two sources. The other four are "
          "quantities the ideal gas law either already contains or never mentions, and none "
          "of them appears in the framework's account of why real gases misbehave."),

 dict(q="The framework says deviations may ALSO arise from particle volumes. What does that "
        "wording indicate?",
      choices=[
        "That particle volume is a second source, separate from interparticle attractions",
        "That particle volume is the same cause as interparticle attractions, renamed",
        "That particle volume matters only when interparticle attractions are absent",
        "That particle volume is the more important of the two under all conditions",
        "That particle volume has been ruled out as a cause"],
      ans=0,
      why="EK 3.6.A.1 introduces interparticle attractions first and then adds particle "
          "volumes with the word also, and it attaches a different set of conditions to each "
          "of them. Two causes with different conditions cannot be one cause renamed."),

 dict(q="The table gives three gas samples with their temperatures and the boiling points of "
        "the substances. Which sample sits closest to the conditions the framework ties to "
        "interparticle attractions?",
      table=_T_COND,
      choices=[
        "Sample 2",
        "Sample 1",
        "Sample 3",
        "All three are equally close",
        "It cannot be decided without the three pressures"],
      ans=0,
      why="EK 3.6.A.1 ties that cause to conditions close to those resulting in condensation, "
          "and a gas is closest to condensing when its temperature sits just above the "
          "boiling point of the substance. The tabulated gap between the two temperatures is "
          "far smaller for one sample than for the others."),

 dict(q="Among the tabulated samples, which is the one where the framework would expect "
        "particle volume to matter most?",
      table=_T_PRESS,
      choices=[
        "Sample L",
        "Sample J",
        "Sample K",
        "All three equally",
        "It cannot be decided without the three temperatures"],
      ans=0,
      why="EK 3.6.A.1 attaches particle volume to extremely high pressures, so among samples "
          "differing only in pressure the one at the highest tabulated pressure is where "
          "that cause is expected to bite hardest."),

 dict(q="Two gases have molecules of comparable size, but one is polar and the other "
        "nonpolar. Near the conditions at which they would condense, which is expected to "
        "deviate more because of interparticle attractions?",
      choices=[
        "The polar gas, because interactions between polar molecules are typically greater "
        "than those between nonpolar molecules of comparable size",
        "The nonpolar gas, because interactions between nonpolar molecules are typically "
        "greater than those between polar molecules of comparable size",
        "The polar gas, because polar molecules occupy more space than nonpolar ones",
        "The nonpolar gas, because nonpolar molecules occupy more space than polar ones",
        "Neither, because the framework ties deviation to pressure alone"],
      ans=0,
      why="EK 3.6.A.1 makes interparticle attractions one of the two sources of deviation, "
          "and EK 3.1.A.2 states that interactions between polar molecules are typically "
          "greater than those between nonpolar molecules of comparable size. Stronger "
          "attractions in the same conditions mean that cause carries further."),

 dict(q="Two gases are held at the same extremely high pressure, and the particles of one "
        "occupy considerably more space than the particles of the other. Which is expected "
        "to deviate more from the ideal gas law?",
      choices=[
        "The gas whose particles occupy more space",
        "The gas whose particles occupy less space",
        "Neither, since particle size is not one of the framework's named causes",
        "The gas with the smaller particles, because they collide more often",
        "It cannot be decided, because the framework ties deviation to temperature alone"],
      ans=0,
      why="EK 3.6.A.1 names particle volumes as a source of deviation and attaches it to "
          "extremely high pressures, which is where both samples sit. The cause is the space "
          "the particles themselves take up, so more of it is more of that cause."),

 dict(q="A student claims that a real gas at one atmosphere and far above its boiling point "
        "behaves almost ideally. Which reasoning supports the claim using the framework's "
        "own account?",
      choices=[
        "Neither named source is in its stated range: the conditions are nowhere near those "
        "producing condensation, and the pressure is nowhere near extremely high",
        "The ideal gas law is exact for every gas, so no support is needed",
        "The gas constant is smaller at low pressure, which cancels the error",
        "Real gases become ideal whenever their molecules are nonpolar",
        "The framework says deviations occur only in mixtures, and this is a pure gas"],
      ans=0,
      why="EK 3.6.A.1 attaches each of its two sources to a stated range of conditions, and "
          "the described sample falls outside both ranges. Justifying the claim means showing "
          "that neither named cause applies, which is the reasoning suggested skill 6.E asks "
          "for."),

 dict(q="A student claims that a gas just above its condensation point will not obey the "
        "ideal gas law well. Which reasoning supports the claim using the framework?",
      choices=[
        "Interparticle attractions are a named source of deviation, and the framework ties "
        "them to conditions close to those resulting in condensation",
        "Particle volumes are a named source of deviation, and the framework ties them to "
        "conditions close to those resulting in condensation",
        "The number of moles changes as a gas approaches condensation",
        "The gas constant takes a different value near a phase change",
        "The ideal gas law contains no temperature term, so it fails whenever temperature "
        "changes"],
      ans=0,
      why="EK 3.6.A.1 names interparticle attractions as a source of deviation and attaches "
          "them to exactly those conditions. The second option names the framework's other "
          "cause but attaches it to the wrong condition, which the same sentence assigns to "
          "extremely high pressure."),

 dict(q="Using the tabulated conditions, for which sample would the framework expect BOTH of "
        "its named sources of deviation to matter?",
      table=_T_BOTH,
      choices=[
        "Sample Q",
        "Sample P",
        "Sample R",
        "Sample S",
        "For none of them, since the two causes never act together"],
      ans=0,
      why="EK 3.6.A.1 attaches one cause to extremely high pressures and the other to "
          "conditions close to condensation, so both apply where the tabulated pressure is "
          "at its highest and the tabulated margin above the boiling point is at its "
          "smallest."),

 dict(q="The framework says deviations MAY result from interparticle attractions. What does "
        "that wording establish?",
      choices=[
        "That the framework names a possible source rather than guaranteeing a deviation",
        "That a real gas always deviates from the ideal gas law by a fixed amount",
        "That interparticle attractions never actually cause a deviation",
        "That the deviation depends on the container rather than on the gas",
        "That the framework is describing liquids rather than gases"],
      ans=0,
      why="EK 3.6.A.1 uses may in both of its causal sentences, which asserts that these are "
          "the sources deviations can come from without promising that any particular sample "
          "will show one. A guarantee of a fixed deviation is a stronger claim than the "
          "sentence makes."),

 dict(q="For which of the tabulated samples would the framework expect NEITHER named source "
        "of deviation to matter much?",
      table=_T_BOTH,
      choices=[
        "Sample P",
        "Sample Q",
        "Sample R",
        "Sample S",
        "For all four equally, since every real gas deviates the same amount"],
      ans=0,
      why="EK 3.6.A.1's two causes need extremely high pressure and nearness to condensation "
          "respectively, so neither is in range where the tabulated pressure is at its "
          "lowest and the tabulated margin above the boiling point is at its largest."),

 dict(q="For which tabulated sample would the framework expect particle volume to matter "
        "while interparticle attractions do not?",
      table=_T_BOTH,
      choices=[
        "Sample S",
        "Sample P",
        "Sample Q",
        "Sample R",
        "For none of them, since the two causes always act together"],
      ans=0,
      why="EK 3.6.A.1 needs an extremely high pressure for the particle-volume cause and "
          "nearness to condensation for the other, so the sample wanted is the one whose "
          "tabulated pressure is high while its tabulated margin above the boiling point is "
          "large."),

 dict(q="For which tabulated sample would the framework expect interparticle attractions to "
        "matter while particle volume does not?",
      table=_T_BOTH,
      choices=[
        "Sample R",
        "Sample P",
        "Sample Q",
        "Sample S",
        "For none of them, since particle volume matters at every pressure"],
      ans=0,
      why="EK 3.6.A.1 needs nearness to condensation for the attraction cause and an "
          "extremely high pressure for the other, so the sample wanted is the one whose "
          "tabulated margin above the boiling point is small while its tabulated pressure is "
          "low."),

 dict(q="What do the framework's two named sources of deviation have in common?",
      choices=[
        "Both are properties of the particles themselves, the forces between them and the "
        "space they take up",
        "Both are properties of the container the gas is held in",
        "Both are measurement errors rather than real effects",
        "Both depend only on the number of moles of gas present",
        "Both apply only to mixtures of two or more gases"],
      ans=0,
      why="EK 3.6.A.1 names interparticle attractions among gas molecules and particle "
          "volumes, and both belong to the particles rather than to the apparatus. Reasoning "
          "from the particulate scale to a macroscopic departure is the connection suggested "
          "skill 6.E asks students to make."),

 dict(q="Three gases are held at the same temperature and pressure. Using the tabulated "
        "boiling points, which is expected to deviate most because of interparticle "
        "attractions?",
      table=_T_BP,
      choices=[
        "Gas E",
        "Gas D",
        "Gas F",
        "All three equally",
        "It cannot be decided without the three molar masses"],
      ans=0,
      why="EK 3.6.A.1 ties that cause to conditions close to those resulting in condensation. "
          "At one shared temperature, the substance with the highest tabulated boiling point "
          "is the one whose conditions sit closest to condensing."),

 dict(q="Three gases are held at the same extremely high pressure. Using the tabulated "
        "particle volumes, which is expected to deviate most from the ideal gas law?",
      table=_T_SIZE,
      choices=[
        "Gas V",
        "Gas T",
        "Gas U",
        "All three equally",
        "It cannot be decided without the three boiling points"],
      ans=0,
      why="EK 3.6.A.1 names particle volumes as a source of deviation and attaches it to "
          "extremely high pressures, which all three samples share. The gas whose particles "
          "occupy the largest tabulated volume therefore carries the most of that cause."),

 dict(q="Which condition does the framework NOT attach to either of its named sources of "
        "deviation?",
      choices=[
        "Extremely low pressure",
        "Extremely high pressure",
        "Conditions close to those resulting in condensation",
        "Conditions under which interparticle attractions act",
        "Conditions under which particle volume is appreciable"],
      ans=0,
      why="EK 3.6.A.1 names extremely high pressures and nearness to condensation, and "
          "attaches nothing to the low-pressure end. That is the end at which neither named "
          "cause is in the range the framework gives it."),

 dict(q="The framework speaks of interparticle attractions among gas molecules. What does "
        "that phrase refer to?",
      choices=[
        "Attractive forces acting between separate gas molecules",
        "The covalent bonds holding each individual molecule together",
        "The attraction of gas molecules to the walls of the container",
        "The force of gravity acting on the gas sample",
        "The repulsion between molecules that keeps a gas expanded"],
      ans=0,
      why="EK 3.6.A.1's phrase is among gas molecules, which places the forces between one "
          "molecule and another rather than inside a molecule. The forces inside a molecule "
          "are the intramolecular ones of topic 2.2, and they hold the molecule together "
          "instead of drawing separate molecules towards each other."),

 dict(q="Which single change to a gas sample would make the particle-volume source of "
        "deviation more important, according to the framework?",
      choices=[
        "Raising the pressure toward extremely high values",
        "Lowering the pressure toward zero",
        "Raising the temperature far above the boiling point",
        "Replacing the container with a larger one at the same pressure",
        "Adding a second gas at a very low pressure"],
      ans=0,
      why="EK 3.6.A.1 attaches particle volume to extremely high pressures, so moving the "
          "sample toward that condition moves it toward the range in which the framework "
          "expects that cause to show. Nothing in the sentence makes the container's size or "
          "the presence of a second gas relevant."),

 dict(q="Which single change to a gas sample would make the interparticle-attraction source "
        "of deviation more important, according to the framework?",
      choices=[
        "Bringing the conditions closer to those that would produce condensation",
        "Moving the conditions further from those that would produce condensation",
        "Raising the temperature far above the boiling point",
        "Enlarging the container at constant temperature",
        "Replacing the gas with one whose molecules are larger"],
      ans=0,
      why="EK 3.6.A.1 attaches interparticle attractions to conditions that are close to "
          "those resulting in condensation, so approaching those conditions is what brings "
          "that cause into its stated range. Warming the sample moves it the other way."),

 dict(q="Why does the framework treat its two sources of deviation separately rather than as "
        "one effect?",
      choices=[
        "Because it attaches a different range of conditions to each of them",
        "Because only one of them is a real effect and the other is hypothetical",
        "Because they act on different gases and never on the same one",
        "Because one applies to pure gases and the other only to mixtures",
        "Because one is a property of the gas and the other a property of the container"],
      ans=0,
      why="EK 3.6.A.1 names interparticle attractions particularly at conditions close to "
          "condensation and particle volumes particularly at extremely high pressures. Two "
          "causes given different ranges of conditions are distinguishable by observation, "
          "which is what makes them separate."),

 dict(q="Which statement puts together everything EK 3.6.A.1 asserts?",
      choices=[
        "The ideal gas law does not explain real gas behavior; interparticle attractions may "
        "cause deviations near conditions producing condensation, and particle volumes may "
        "cause deviations at extremely high pressures",
        "The ideal gas law explains real gas behavior; deviations arise only from "
        "experimental error in the measurement of pressure",
        "The ideal gas law does not explain real gas behavior; the only source of deviation "
        "is the volume of the container",
        "The ideal gas law does not explain real gas behavior; deviations are always larger "
        "at low pressure than at high pressure",
        "The ideal gas law does not explain real gas behavior; deviations depend on the "
        "molar mass of the gas alone"],
      ans=0,
      why="EK 3.6.A.1 has three parts and this option carries all three: the limitation, the "
          "first cause with its conditions, and the second cause with its conditions. Each "
          "rejected option keeps the opening and then replaces one or both causes with "
          "something the sentence does not name."),

 dict(q="Which pairing of a source of deviation with its conditions matches the framework?",
      choices=[
        "Interparticle attractions with conditions producing condensation, and particle "
        "volumes with extremely high pressures",
        "Interparticle attractions with extremely high pressures, and particle volumes with "
        "conditions producing condensation",
        "Both causes with extremely high pressures only",
        "Both causes with conditions producing condensation only",
        "Neither cause is tied to any particular conditions by the framework"],
      ans=0,
      why="EK 3.6.A.1 attaches attractions to conditions that are close to those resulting in "
          "condensation and particle volumes to extremely high pressures. Exchanging the two "
          "conditions keeps both causes and both conditions while making the statement false, "
          "which is why the pairing is stated in full rather than in half."),

 dict(q="Which claim about deviation from the ideal gas law goes beyond what the framework "
        "states?",
      choices=[
        "That a real gas can be relied on to exert less pressure than the ideal gas law "
        "predicts",
        "That interparticle attractions may cause deviations",
        "That particle volumes may cause deviations",
        "That the ideal gas law does not explain the actual behavior of real gases",
        "That nearness to condensation is a condition under which deviations may appear"],
      ans=0,
      why="EK 3.6.A.1 names two causes and the conditions under which each becomes "
          "important, and it stops there. It does not say which way a measured quantity will "
          "depart from the value the equation gives, so a claim about the direction of the "
          "departure is not supported by the sentence. The four rejected statements are each "
          "part of what the sentence does assert."),
]
