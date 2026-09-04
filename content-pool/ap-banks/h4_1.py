# AP CHEMISTRY 4.1 Introduction for Reactions
# CED effective Fall 2024, Unit 4 Chemical Reactions.
# Learning objective 4.1.A: identify evidence of chemical and physical changes
# in matter. Suggested skill 2.B, formulate a hypothesis or predict the results
# of an experiment.
#
# Essential knowledge relied on, in the framework's own words:
#   4.1.A.1  A physical change occurs when a substance undergoes a change in
#            properties but not a change in composition. Changes in the phase of
#            a substance (solid, liquid, gas) or formation/separation of
#            mixtures of substances are common physical changes.
#   4.1.A.2  A chemical change occurs when substances are transformed into new
#            substances, typically with different compositions. Production of
#            heat or light, formation of a gas, formation of a precipitate,
#            and/or color change provide possible evidence that a chemical
#            change has occurred.
#
# THE ONE MOVE THIS TOPIC OWNS: COMPOSITION IS THE CRITERION, THE OBSERVATIONS
# ARE ONLY EVIDENCE. 4.1.A.1 and 4.1.A.2 both define their change by what
# happens to composition; the four observations in 4.1.A.2 are introduced with
# the words "possible evidence". So a large share of this module turns on the
# gap between the two -- a gas appears when water boils, a color fades when a
# solution is diluted, and neither is a chemical change.
#
# WHAT IS NOT HERE. Topic 4.4 classifies the same two kinds of process by BONDS
# and intermolecular interactions, and h4_4.py owns that framing along with the
# argued case of dissolving a salt. Nothing in this module keys on bond
# breaking, on ion-dipole interactions, or on the dissolution argument. Writing
# an equation for a change is 4.2 and particulate pictures of one are 4.3.
#
# NOTATION. Chemistry is not typeset and this topic needs no mathematics, so
# every formula is written in prose: H2O, CaCO3, N2. Reaction arrows are written
# as the word "gives", since a raw arrow glyph reaches the student literally.
TOPIC = ("4.1", "Introduction for Reactions", 4)

_T_EVIDENCE = dict(
    headers=["Observation recorded by the student",
             "Kind of observation it is"],
    rows=[["The mixture became hot and glowed briefly",
           "Production of heat or light"],
          ["A solid appeared when two clear solutions were combined",
           "Formation of a precipitate"],
          ["The liquid went from colorless to deep blue",
           "Color change"],
          ["The sample was poured from a beaker into a flask",
           "Transfer between containers"]])

_T_COMPOSITION = dict(
    headers=["Process", "Substances present before", "Substances present after"],
    rows=[["P1", "H2O(l)", "H2O(s)"],
          ["P2", "N2(g), H2(g)", "NH3(g)"],
          ["P3", "I2(s)", "I2(g)"],
          ["P4", "CaCO3(s)", "CaO(s), CO2(g)"]])

_T_SECOND = dict(
    headers=["Observation recorded by the student",
             "Kind of observation it is"],
    rows=[["Bubbles of gas rose steadily from the reacting mixture",
           "Formation of a gas"],
          ["The clear solution turned bright orange",
           "Color change"],
          ["The flask felt noticeably warm afterwards",
           "Production of heat or light"],
          ["The mass of the sealed flask was unchanged",
           "Conservation of mass"]])

QUESTIONS = [

 dict(q="Which statement gives the framework's criterion for a physical change?",
      choices=[
        "A substance undergoes a change in properties but not a change in "
        "composition",
        "A substance undergoes a change in composition but not a change in "
        "properties",
        "A substance is transformed into new substances that have new "
        "compositions",
        "A substance gives off heat or light to its surroundings",
        "A substance is broken down into the elements it contains"],
      ans=0,
      why="EK 4.1.A.1, near verbatim: a physical change occurs when a substance "
          "undergoes a change in properties but not a change in composition. "
          "Composition, not appearance, is what the framework makes decisive."),

 dict(q="Which statement gives the framework's criterion for a chemical change?",
      choices=[
        "Substances are transformed into new substances, typically with "
        "different compositions",
        "Substances change phase while keeping the compositions they started "
        "with",
        "Substances are mixed together without any of their identities changing",
        "The temperature of a sample changes while its identity stays the same",
        "A sample is divided into smaller portions of the same substance"],
      ans=0,
      why="EK 4.1.A.2, near verbatim: a chemical change occurs when substances "
          "are transformed into new substances, typically with different "
          "compositions. Mixing and phase change leave composition alone under "
          "EK 4.1.A.1."),

 dict(q="Which of the following does the framework name as a common physical "
        "change?",
      choices=[
        "A change in the phase of a substance among solid, liquid and gas",
        "The appearance of a precipitate when two solutions are combined",
        "The production of light by a burning sample",
        "The conversion of reactants into products of new composition",
        "The release of a gas by a reacting mixture"],
      ans=0,
      why="EK 4.1.A.1 lists changes in the phase of a substance among solid, "
          "liquid and gas as common physical changes. The other four are the "
          "observations EK 4.1.A.2 offers as possible evidence of a CHEMICAL "
          "change."),

 dict(q="A chemist combines powdered sulfur with iron filings and later "
        "separates the two with a magnet. How does the framework classify these "
        "two operations?",
      choices=[
        "Both are physical changes, because forming and separating a mixture "
        "leaves each substance's composition alone",
        "Both are chemical changes, because two substances were brought into "
        "contact",
        "Forming the mixture is chemical and separating it is physical",
        "Forming the mixture is physical and separating it is chemical",
        "Neither is a change of any kind, because nothing was heated"],
      ans=0,
      why="EK 4.1.A.1 names formation and separation of mixtures of substances "
          "as common physical changes, and EK 4.1.A.1's criterion is that "
          "composition is unaltered, which is exactly what a magnet exploits."),

 dict(q="Which observation appears on the framework's list of possible evidence "
        "that a chemical change has occurred?",
      choices=[
        "The formation of a precipitate",
        "The melting of a solid to a liquid",
        "The separation of a mixture into its components",
        "The compression of a gas into a smaller volume",
        "The stirring of a solid until it is evenly distributed"],
      ans=0,
      why="EK 4.1.A.2 lists production of heat or light, formation of a gas, "
          "formation of a precipitate, and color change as possible evidence of "
          "a chemical change. Melting and separating a mixture are the physical "
          "changes of EK 4.1.A.1."),

 dict(q="Which of the following is NOT among the observations the framework "
        "offers as possible evidence that a chemical change has occurred?",
      choices=[
        "A change in the phase of the substance",
        "The production of heat or light",
        "The formation of a gas",
        "The formation of a precipitate",
        "A change in color"],
      ans=0,
      why="EK 4.1.A.2's list is production of heat or light, formation of a gas, "
          "formation of a precipitate, and color change. A phase change is on EK "
          "4.1.A.1's list of common PHYSICAL changes instead."),

 dict(q="A student says that because bubbles of gas appear when water is "
        "boiled, boiling must be a chemical change. What is wrong with the "
        "reasoning?",
      choices=[
        "The formation of a gas is only possible evidence of a chemical change, "
        "and the boiling water keeps the composition it started with",
        "The formation of a gas is never associated with a chemical change",
        "Bubbles in boiling water are air rather than a substance of any kind",
        "The reasoning is correct, because gas formation settles the question",
        "The reasoning fails only because water was not heated strongly enough"],
      ans=0,
      why="EK 4.1.A.2 introduces its four observations as POSSIBLE evidence "
          "rather than proof, and EK 4.1.A.1 makes a change of phase a physical "
          "change because the composition of the water is the same before and "
          "after."),

 dict(q="The table records four observations from one experiment and states "
        "what kind of observation each is. How many of them fall among the "
        "kinds the framework offers as possible evidence of a chemical change?",
      table=_T_EVIDENCE,
      choices=[
        "Three of them",
        "All four of them",
        "Two of them",
        "Exactly one of them",
        "None of them"],
      ans=0,
      why="EK 4.1.A.2 names production of heat or light, formation of a gas, "
          "formation of a precipitate, and color change. Counting the tabulated "
          "kinds against that list is what settles the number."),

 dict(q="A strip of magnesium is ignited. It burns with a brilliant white "
        "light and leaves behind a crumbly white powder that will not burn "
        "again. Which conclusion does the framework support?",
      choices=[
        "A chemical change occurred, because a new substance of different "
        "composition was formed and light was produced",
        "A physical change occurred, because the metal only changed its "
        "appearance",
        "A physical change occurred, because the white powder is magnesium in a "
        "different phase",
        "No change occurred, because the mass of the sample can be accounted for",
        "A chemical change occurred, but only because the sample was heated"],
      ans=0,
      why="EK 4.1.A.2 makes transformation into a new substance of different "
          "composition the criterion, and offers production of heat or light as "
          "possible evidence. The white powder does not behave as magnesium "
          "does, so it is not the same substance."),

 dict(q="Liquid nitrogen poured into an open dish boils away vigorously to "
        "nitrogen gas. How should the process be classified?",
      choices=[
        "A physical change, because the nitrogen has the same composition as a "
        "gas that it had as a liquid",
        "A chemical change, because a gas was formed",
        "A chemical change, because the sample disappeared from the dish",
        "A physical change, because nitrogen is an element and elements cannot "
        "react",
        "It cannot be classified without knowing the temperature of the room"],
      ans=0,
      why="EK 4.1.A.1 makes a change in the phase of a substance a common "
          "physical change, since properties change while composition does not. "
          "EK 4.1.A.2 offers gas formation as possible evidence only."),

 dict(q="Sand stirred into water is poured through filter paper, and dry sand "
        "is recovered on the paper while clear water passes through. What kind "
        "of change is the filtration?",
      choices=[
        "A physical change, because separating a mixture leaves the composition "
        "of each component unaltered",
        "A chemical change, because the sand and the water were parted from one "
        "another",
        "A chemical change, because the water that passed through is clear "
        "rather than cloudy",
        "A physical change, but only because no heat was applied",
        "Neither, because a separation is a procedure rather than a change"],
      ans=0,
      why="EK 4.1.A.1 names formation and separation of mixtures of substances "
          "among common physical changes, and the sand recovered has the same "
          "composition as the sand added."),

 dict(q="A mixture of ethanol and water is heated in a still and the ethanol "
        "collects first in a cooled receiver. Which statement about the "
        "distillation is correct?",
      choices=[
        "It is a physical change, because it separates a mixture without "
        "altering the composition of either substance",
        "It is a chemical change, because the ethanol was converted to a vapor "
        "and back again",
        "It is a chemical change, because the receiver holds a substance the "
        "still did not contain at the start",
        "It is a physical change only if the ethanol is collected without any "
        "water",
        "It is neither, because two phase changes cancel one another"],
      ans=0,
      why="EK 4.1.A.1 lists both phase changes and the separation of mixtures "
          "as common physical changes, and the collected ethanol has the "
          "composition it had in the flask."),

 dict(q="Table sugar stirred into warm water disappears, and evaporating the "
        "water afterwards returns sugar that tastes and behaves as it did "
        "before. What does the recovery establish?",
      choices=[
        "That dissolving formed a mixture without changing the composition of "
        "the sugar, which the framework treats as a physical change",
        "That dissolving destroyed the sugar and evaporation created it again",
        "That dissolving is a chemical change because the sugar became "
        "invisible",
        "That the water and the sugar exchanged compositions and then exchanged "
        "them back",
        "That no change of any kind took place at any stage"],
      ans=0,
      why="EK 4.1.A.1 makes formation of a mixture a common physical change and "
          "defines a physical change as a change in properties without a change "
          "in composition. Recovering unaltered sugar is evidence its "
          "composition survived."),

 dict(q="A student plans to test whether heating a white solid produces a "
        "chemical change. Which prediction, if borne out, would count under the "
        "framework as possible evidence that it did?",
      choices=[
        "A gas will be given off and the residue will be a different color from "
        "the original solid",
        "The solid will occupy a slightly larger volume once it is warm",
        "The solid will feel warmer than it did before it was heated",
        "The mass of the closed apparatus will stay the same throughout",
        "The solid will look the same at the end as it did at the start"],
      ans=0,
      why="EK 4.1.A.2 offers formation of a gas and color change among the "
          "observations that provide possible evidence of a chemical change. "
          "Warming and expansion accompany heating whatever kind of change "
          "occurs."),

 dict(q="Water is added to a small volume of concentrated blue copper sulfate "
        "solution and the color becomes much paler. Does the color change "
        "establish a chemical change?",
      choices=[
        "No, because color change is only possible evidence, and dilution "
        "spreads the same dissolved substance through more water",
        "Yes, because color change is on the framework's list of evidence",
        "Yes, because the pale solution is a substance the flask did not "
        "contain before",
        "No, because color change is never associated with a chemical change",
        "It cannot be judged without measuring the temperature of the solution"],
      ans=0,
      why="EK 4.1.A.2 offers color change as POSSIBLE evidence, not as proof. "
          "The dissolved substance keeps its composition, so EK 4.1.A.1 makes "
          "the dilution a physical change."),

 dict(q="Solid carbon dioxide left in a warm room shrinks steadily and a cold "
        "fog forms above it, with no liquid ever appearing. What kind of change "
        "is this, and why?",
      choices=[
        "Physical, because the carbon dioxide has passed from solid to gas "
        "without any change in its composition",
        "Chemical, because a gas was formed where none was present before",
        "Chemical, because the solid vanished entirely",
        "Physical, because carbon dioxide is a compound rather than an element",
        "Chemical, because the fog is a substance different from the solid"],
      ans=0,
      why="EK 4.1.A.1 makes a change in the phase of a substance a common "
          "physical change. EK 4.1.A.2 offers gas formation as possible "
          "evidence only, and here the gas has the composition of the solid it "
          "came from."),

 dict(q="The table gives the substances present before and after each of four "
        "processes. In which processes does the composition of the material "
        "change?",
      table=_T_COMPOSITION,
      choices=[
        "P2 and P4",
        "P1 and P3",
        "All four processes",
        "Only P1",
        "Only P3"],
      ans=0,
      why="EK 4.1.A.2 makes transformation into new substances the mark of a "
          "chemical change, while EK 4.1.A.1 makes a change of phase leave "
          "composition alone. Comparing the tabulated formulas before and after "
          "is what identifies the two."),

 dict(q="Steam released onto a cold window condenses and the window becomes "
        "warm. Why does the warming fail to establish that a chemical change "
        "occurred?",
      choices=[
        "Because energy release is only possible evidence, and a phase change "
        "releases energy while leaving the composition of the water alone",
        "Because a chemical change never releases energy to its surroundings",
        "Because the window is too cold for a chemical change to occur on it",
        "Because water is a compound and compounds cannot undergo chemical "
        "change",
        "Because the released energy would have to be measured before any "
        "conclusion is possible"],
      ans=0,
      why="EK 4.1.A.2 offers production of heat among its possible evidence, "
          "not as a sufficient test. EK 4.1.A.1 classes the condensation as a "
          "phase change, and the condensed water has the composition the steam "
          "had."),

 dict(q="Two samples are compared. The first is the same substance before and "
        "after treatment; the second contains substances not present at the "
        "start. Which sample underwent a chemical change, and on what grounds?",
      choices=[
        "The second, because a chemical change is a transformation into new "
        "substances of different composition",
        "The first, because the treatment altered its properties",
        "Both, because every treatment alters a sample in some way",
        "Neither, until an observation such as a color change is also reported",
        "It cannot be decided from composition alone"],
      ans=0,
      why="EK 4.1.A.2 makes transformation into new substances the definition of "
          "a chemical change and EK 4.1.A.1 makes unaltered composition the mark "
          "of a physical one, so composition alone settles the classification."),

 dict(q="Which wording matches the framework's statement about the composition "
        "of the substances a chemical change produces?",
      choices=[
        "New substances are formed, typically with compositions different from "
        "the original substances",
        "New substances are formed, always with exactly the same composition as "
        "the original substances",
        "The original substances are kept, but their properties are exchanged",
        "The original substances are divided, leaving smaller portions of the "
        "same material",
        "New substances are formed only when a precipitate can be seen"],
      ans=0,
      why="EK 4.1.A.2 reads that substances are transformed into new substances, "
          "typically with different compositions. The word typically is the "
          "framework's own hedge and does not license the claim that the "
          "composition is unchanged."),

 dict(q="A reaction is carried out and none of the framework's four listed "
        "observations is seen. What may the student conclude?",
      choices=[
        "Nothing decisive, because those observations are offered as possible "
        "evidence rather than as a requirement of every chemical change",
        "That no chemical change occurred, because the list is exhaustive",
        "That a physical change must have occurred instead",
        "That the sample was too small for any change to take place",
        "That a chemical change certainly occurred but was too slow to see"],
      ans=0,
      why="EK 4.1.A.2 says the four observations PROVIDE POSSIBLE EVIDENCE that "
          "a chemical change has occurred. That wording makes them indicators "
          "rather than a checklist a genuine chemical change must satisfy."),

 dict(q="A pure liquid is frozen solid and then melted back to a liquid with "
        "the same boiling point as before. What has been demonstrated about its "
        "composition?",
      choices=[
        "That the composition was unaltered throughout, which makes both steps "
        "physical changes",
        "That the composition changed on freezing and changed back on melting",
        "That the composition of a solid is always different from that of a "
        "liquid",
        "That the substance must have been a mixture rather than a pure "
        "substance",
        "That freezing is physical while melting is chemical"],
      ans=0,
      why="EK 4.1.A.1 makes changes in the phase of a substance common physical "
          "changes, in which properties change but composition does not, and "
          "the recovered boiling point is evidence the substance is what it was."),

 dict(q="A drop of black ink is placed on filter paper and water carries the "
        "dyes it contains into separate colored bands. Which classification does "
        "the framework support?",
      choices=[
        "A physical change, because the separation of a mixture leaves each dye "
        "with the composition it had in the ink",
        "A chemical change, because colors appeared that the ink did not show",
        "A chemical change, because the water reacted with each dye in turn",
        "A physical change, because color change is never evidence of anything",
        "Neither, because only the paper was altered"],
      ans=0,
      why="EK 4.1.A.1 names separation of mixtures of substances among common "
          "physical changes. The bands are the dyes that were in the ink all "
          "along, so no substance of new composition was made."),

 dict(q="A copper wire is drawn out until it is half its original diameter and "
        "several times its original length. What has changed, in the "
        "framework's terms?",
      choices=[
        "Its properties have changed while its composition has not, so the "
        "change is physical",
        "Its composition has changed while its properties have not, so the "
        "change is chemical",
        "Both its properties and its composition have changed",
        "Neither its properties nor its composition has changed",
        "Its composition has changed because the sample is now longer"],
      ans=0,
      why="EK 4.1.A.1 defines a physical change as a change in properties "
          "without a change in composition. Drawing the wire alters its "
          "dimensions and stiffness while every part of it is still copper."),

 dict(q="A student wants an observation that would support the hypothesis that "
        "heating two powders together produces a chemical change. Which planned "
        "observation is the strongest under the framework?",
      choices=[
        "Watching for a glow and for a residue whose color differs from either "
        "starting powder",
        "Watching for the mixture to become warm while the burner is lit",
        "Watching for the powders to become more finely divided as they are "
        "stirred",
        "Watching for the total mass of the sealed tube to stay constant",
        "Watching for the mixture to spread evenly across the bottom of the tube"],
      ans=0,
      why="EK 4.1.A.2 offers production of heat or light and color change among "
          "the observations that provide possible evidence of a chemical "
          "change; warming under a lit burner and even mixing accompany any "
          "heating."),

 dict(q="Colorless ammonia gas and colorless hydrogen chloride gas meet in a "
        "tube and a white solid forms on the glass between them. What is the "
        "best justification that a chemical change occurred?",
      choices=[
        "A solid of a composition different from either gas has appeared where "
        "only gases were present",
        "The two gases were both colorless before they met",
        "The solid appeared partway along the tube rather than at one end",
        "Gases are always converted to solids by chemical change",
        "The tube became slightly warm as the solid formed"],
      ans=0,
      why="EK 4.1.A.2 makes transformation into new substances of different "
          "composition the criterion for a chemical change. A solid is neither "
          "of the gases and cannot be either of them in another phase, since "
          "both were present at the same temperature."),

 dict(q="Water freezes to ice, which is rigid and much harder than the liquid "
        "it came from. Why does the framework still call this a physical "
        "change?",
      choices=[
        "Because a change in properties without a change in composition is "
        "exactly what a physical change is",
        "Because the change in properties is too small to matter",
        "Because ice and liquid water have different compositions but the same "
        "properties",
        "Because freezing releases no energy at all",
        "Because a change is physical only when nothing observable happens"],
      ans=0,
      why="EK 4.1.A.1 defines a physical change as a change in properties but "
          "not a change in composition, and names phase changes as common "
          "examples. A dramatic change in hardness is a change in properties, "
          "which the definition allows."),

 dict(q="The table records four observations from a second experiment. Which of "
        "the tabulated observations falls OUTSIDE the framework's list of "
        "possible evidence for a chemical change?",
      table=_T_SECOND,
      choices=[
        "The report that the mass of the sealed flask was unchanged",
        "The steady rise of bubbles from the reacting mixture",
        "The turning of the clear solution to bright orange",
        "The warmth of the flask afterwards",
        "All four fall outside the framework's list"],
      ans=0,
      why="EK 4.1.A.2 lists production of heat or light, formation of a gas, "
          "formation of a precipitate, and color change. Constant mass is a "
          "consequence of conservation stated in EK 4.2.A.2 and is not on that "
          "list of evidence."),

 dict(q="Why does the framework define the two kinds of change by composition "
        "rather than by how dramatic the change looks?",
      choices=[
        "Because a change can be spectacular and leave composition alone, while "
        "an unremarkable one can produce new substances",
        "Because appearance cannot be recorded reliably by any student",
        "Because composition is the only property a substance has",
        "Because a chemical change is always more dramatic than a physical one",
        "Because the framework has no interest in what a student observes"],
      ans=0,
      why="EK 4.1.A.1 and EK 4.1.A.2 both turn on composition, while EK "
          "4.1.A.2's four observations are offered only as possible evidence. "
          "Boiling nitrogen and a quiet precipitation are the two directions in "
          "which appearance and composition come apart."),

 dict(q="Two students are asked what evidence would let them decide between a "
        "physical and a chemical change. Whose plan is the better one under the "
        "framework?",
      choices=[
        "The student who proposes to test whether the material recovered at the "
        "end behaves as the starting material did",
        "The student who proposes to record how bright the change looked",
        "The student who proposes to time how long the change took",
        "The student who proposes to measure the volume of the container before "
        "and after",
        "The student who proposes to repeat the change at a higher temperature"],
      ans=0,
      why="EK 4.1.A.1 makes unchanged composition the mark of a physical change "
          "and EK 4.1.A.2 makes new substances the mark of a chemical one, so a "
          "test of whether the recovered material is the starting material "
          "addresses the criterion itself rather than the evidence for it."),
]
