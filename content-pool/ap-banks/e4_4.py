# AP ENVIRONMENTAL SCIENCE 4.4 Earth's Atmosphere
# CED effective Fall 2026, Unit 4 Earth Systems and Resources.
# Enduring understanding ERT-4: Earth's systems interact, resulting in a state of balance
# over time.
# Learning objective ERT-4.D: describe the structure and composition of the Earth's
# atmosphere.
# Suggested skill 2.A, describe characteristics of an environmental concept, process, or
# model represented visually.
#
# Essential knowledge relied on, in the framework's own words:
#   ERT-4.D.1  The atmosphere is made up of major gases, each with its own relative
#              abundance.
#   ERT-4.D.2  The layers of the atmosphere are based on temperature gradients and include
#              the troposphere, stratosphere, mesosphere, thermosphere, and exosphere.
#
# TWO SENTENCES ARE THE WHOLE OF THIS TOPIC, and what they DO NOT say governs this module
# as much as what they do:
#   they name no gas, and give no abundance for any gas
#   they give no altitude for any layer
#   they say nothing about which layer lies nearest the surface
#   they say nothing about the DIRECTION in which temperature changes in any layer
#
# So every one of those things enters as a STIMULUS in a table= and the question is a
# reading of the table. No key anywhere in this module states a gas, an abundance, an
# altitude or a direction of temperature change as an assertion of the framework; the
# framework supplies only that the gases have relative abundances and that the layers are
# based on temperature gradients, and each claim in verify_e4_4.py says which of the two is
# doing the work.
#
# WHAT IS KEYED AS FRAMEWORK CONTENT: that the atmosphere is made of major gases; that each
# has its own relative abundance; that the layers are based on TEMPERATURE GRADIENTS and
# not on anything else; and the five names, which the statement gives outright.
#
# NO FIGURES. Skill 2.A concerns a model represented visually and the bank carries no
# images, so the composition and the layer structure are tabulated instead.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("4.4", "Earth’s Atmosphere", 4)

_T_GASES = dict(
    headers=["Gas", "Share of dry air by volume (percent)"],
    rows=[["Nitrogen", "78.08"],
          ["Oxygen", "20.95"],
          ["Argon", "0.93"],
          ["Carbon dioxide", "0.04"]])

_T_LAYERS = dict(
    headers=["Layer", "Altitude at which it begins (kilometers above the surface)",
             "Altitude at which it ends (kilometers above the surface)",
             "Temperature at its lower edge (degrees Celsius)",
             "Temperature at its upper edge (degrees Celsius)"],
    rows=[["Troposphere", "0", "12", "15", "-55"],
          ["Stratosphere", "12", "50", "-55", "0"],
          ["Mesosphere", "50", "85", "0", "-90"],
          ["Thermosphere", "85", "600", "-90", "700"]])

QUESTIONS = [

 dict(q="What does the framework say the atmosphere is made up of?",
      choices=[
        "Major gases, each with its own relative abundance",
        "A single gas present in the same amount throughout",
        "Liquid water and dust, with no gases involved",
        "Layers of rock differing in density",
        "Nothing that the framework describes"],
      ans=0,
      why="ERT-4.D.1 states that the atmosphere is made up of major gases, each with its "
          "own relative abundance. The statement names more than one gas and gives each a "
          "share of its own."),

 dict(q="What does the framework's phrase RELATIVE ABUNDANCE indicate about those gases?",
      choices=[
        "That they are present in differing amounts, each with its own share of the whole",
        "That they are present in exactly equal amounts",
        "That only one of them is present at any one time",
        "That their amounts cannot be measured",
        "That their amounts are fixed by the temperature of the layer"],
      ans=0,
      why="ERT-4.D.1 gives each major gas its OWN relative abundance, which makes the "
          "abundance a share belonging to that gas rather than a quantity shared equally "
          "among them. The statement neither equalises the shares nor ties them to "
          "temperature."),

 dict(q="On what does the framework say the layers of the atmosphere are based?",
      choices=["Temperature gradients", "Pressure alone", "The abundance of nitrogen",
               "Distance from the equator", "The direction of the prevailing wind"],
      ans=0,
      why="ERT-4.D.2 states that the layers of the atmosphere are based on temperature "
          "gradients, and offers no other basis for them. Relative abundance is what "
          "ERT-4.D.1 attaches to the gases, not to the layers."),

 dict(q="Which layers does the framework name?",
      choices=[
        "The troposphere, stratosphere, mesosphere, thermosphere, and exosphere",
        "The troposphere, stratosphere, mesosphere, and thermosphere, and no fifth layer",
        "The troposphere, stratosphere, and mesosphere, and no fourth layer",
        "The troposphere, stratosphere, mesosphere, thermosphere, and hydrosphere",
        "The lithosphere, hydrosphere, and biosphere"],
      ans=0,
      why="ERT-4.D.2 names the troposphere, stratosphere, mesosphere, thermosphere, and "
          "exosphere. Two rejected options drop one or two of the five, one replaces the "
          "last with the hydrosphere, and one leaves the atmosphere altogether."),

 dict(q="How many layers of the atmosphere does the framework name?",
      choices=["Five", "Two", "Three", "Four", "Seven"],
      ans=0,
      why="ERT-4.D.2 names the troposphere, stratosphere, mesosphere, thermosphere, and "
          "exosphere, which is five names in one list."),

 dict(q="Which of the following is NOT one of the layers the framework names?",
      choices=["The hydrosphere", "The troposphere", "The stratosphere", "The mesosphere",
               "The exosphere"],
      ans=0,
      why="ERT-4.D.2 names the troposphere, stratosphere, mesosphere, thermosphere, and "
          "exosphere. The hydrosphere is not among them and is not a layer of the "
          "atmosphere at all."),

 dict(q="ERT-4.D.2 says the layers INCLUDE the five it names. What does that phrasing "
        "establish?",
      choices=[
        "Those five are the layers the statement supplies, without its asserting that the "
        "atmosphere can be divided in no other way",
        "The statement asserts that no other division of the atmosphere has ever been used",
        "The statement supplies only three of the layers",
        "The statement supplies the layers but not what they are based on",
        "The statement supplies no layers at all"],
      ans=0,
      why="ERT-4.D.2 gives the five names after the word include, which commits the "
          "framework to those five while making no claim about arrangements it does not "
          "discuss. The statement also gives the basis of the layers, so an option denying "
          "that is false as well."),

 dict(q="Which framework statement explains why the atmosphere is treated as layered at "
        "all?",
      choices=[
        "That the layers of the atmosphere are based on temperature gradients",
        "That the atmosphere is made up of major gases, each with its own relative abundance",
        "That global wind patterns result from the most intense solar radiation arriving at "
        "the equator",
        "That soils are generally categorized by horizons",
        "That the characteristics of a watershed include its area and its slope"],
      ans=0,
      why="ERT-4.D.2 states that the layers of the atmosphere are based on temperature "
          "gradients, which is what makes one layer distinguishable from another. The "
          "remaining statements belong to ERT-4.D.1, ERT-4.E.1, ERT-4.B.2 and ERT-4.F.1."),

 dict(q="A student says the layers of the atmosphere are defined by how much oxygen each "
        "one contains. What does the framework say instead?",
      choices=[
        "That the layers are based on temperature gradients, while relative abundance is "
        "what the framework attaches to the gases rather than to the layers",
        "That the layers are based on the abundance of oxygen, exactly as the student says",
        "That the layers are based on the abundance of nitrogen",
        "That the framework supplies no basis at all for the layers",
        "That the layers are based on their distance from the equator"],
      ans=0,
      why="ERT-4.D.2 bases the layers on temperature gradients and ERT-4.D.1 attaches "
          "relative abundance to the major gases. The student has taken a property the "
          "framework gives to one thing and applied it to the other."),

 dict(q="Which of these does the framework's statement about the atmosphere's composition "
        "leave unstated?",
      choices=[
        "Which gas is the most abundant",
        "That the atmosphere is made up of gases",
        "That those gases are described as major ones",
        "That each gas has its own relative abundance",
        "That relative abundance is a property of the gases"],
      ans=0,
      why="ERT-4.D.1 supplies the four rejected options in its own words. It never names a "
          "gas and never gives an abundance, so which gas is most abundant is not something "
          "the statement settles."),

 dict(q="Which of these does the framework's statement about the atmosphere's layers leave "
        "unstated?",
      choices=[
        "The altitude at which each layer begins and ends",
        "That the layers are based on temperature gradients",
        "That the troposphere is one of the layers",
        "That the exosphere is one of the layers",
        "That the mesosphere is one of the layers"],
      ans=0,
      why="ERT-4.D.2 supplies the basis of the layers and the five names, and no altitude "
          "for any of them. Where an altitude is needed it has to come from a measurement "
          "rather than from the statement."),

 dict(q="A researcher rising through the atmosphere records the temperature falling, then "
        "rising, then falling again. Which framework statement does that record bear on?",
      choices=[
        "The statement that the layers are based on temperature gradients, since a change "
        "in the gradient is what marks one layer from the next",
        "The statement that the atmosphere is made up of major gases",
        "The statement that each gas has its own relative abundance",
        "The statement that global wind patterns result from solar radiation arriving at "
        "the equator",
        "No statement in the framework bears on such a record"],
      ans=0,
      why="ERT-4.D.2 states that the layers of the atmosphere are based on temperature "
          "gradients, so a record of how the temperature changes with altitude is a record "
          "of the very thing the layers rest on. The composition statement concerns the "
          "gases rather than the temperature."),

 dict(q="Which measurement would establish the relative abundance of a gas in the "
        "atmosphere?",
      choices=[
        "The share of a sample of air that the gas makes up",
        "The temperature of the air at the height the sample was taken",
        "The altitude at which the sample was taken",
        "The mass of the whole atmosphere",
        "The number of layers lying above the sample"],
      ans=0,
      why="ERT-4.D.1 gives each major gas its own relative abundance, which is a share of "
          "the whole, so a measurement of that share is what establishes it. A temperature "
          "or an altitude bears on ERT-4.D.2 and the layers instead."),

 dict(q="How does this topic's account of the atmosphere differ from the framework's "
        "statement about global wind patterns?",
      choices=[
        "This topic says what the atmosphere is made of and how its layers are defined, "
        "while that statement says what causes the winds moving within it",
        "This topic says what causes the winds moving within the atmosphere, while that "
        "statement says what the atmosphere is made of and how its layers are defined",
        "The two make the same claim in different words",
        "This topic concerns the ocean and that statement concerns the atmosphere",
        "Neither of the two concerns the atmosphere"],
      ans=0,
      why="ERT-4.D.1 and ERT-4.D.2 give the composition of the atmosphere and the basis of "
          "its layers. ERT-4.E.1, in the next topic, states that global wind patterns "
          "primarily result from the most intense solar radiation arriving at the equator. "
          "One describes the thing and the other explains a motion within it."),

 dict(q="Which pairing of a framework term with what it is about is correct?",
      choices=[
        "Relative abundance is about the gases, and a temperature gradient is about the "
        "layers",
        "Relative abundance is about the layers, and a temperature gradient is about the "
        "gases",
        "Both relative abundance and a temperature gradient are about the gases",
        "Both relative abundance and a temperature gradient are about the layers",
        "Neither term is used by the framework in this topic"],
      ans=0,
      why="ERT-4.D.1 attaches relative abundance to the major gases and ERT-4.D.2 bases the "
          "layers on temperature gradients, so each term belongs to one of the two "
          "statements and not to the other."),

 dict(q="Which of these does the framework claim about the layers of the atmosphere?",
      choices=[
        "That they are based on temperature gradients and that five of them are named",
        "That they are based on pressure gradients and that five of them are named",
        "That they are based on temperature gradients and that exactly two of them are named",
        "That they are based on the abundance of the gases and that five of them are named",
        "That the framework names no layers at all"],
      ans=0,
      why="ERT-4.D.2 supplies both halves: the layers are based on temperature gradients, "
          "and the troposphere, stratosphere, mesosphere, thermosphere and exosphere are "
          "named. Each rejected option replaces the basis or the count."),

 dict(q="The composition of dry air was measured for four gases. What does the record "
        "establish?",
      table=_T_GASES,
      choices=[
        "The four gases are present in differing shares, each with a share of its own",
        "The four gases are present in equal shares",
        "Only one of the four gases is present at all",
        "The record reports the gases but not their shares",
        "The shares are the same for every gas except one"],
      ans=0,
      why="The four shares are 78.08, 20.95, 0.93 and 0.04 percent, all different and all "
          "above zero. ERT-4.D.1 states that the atmosphere is made up of major gases, each "
          "with its own relative abundance."),

 dict(q="Which of those four gases makes up the largest share of dry air?",
      table=_T_GASES,
      choices=["Nitrogen", "Oxygen", "Argon", "Carbon dioxide",
               "The four make up equal shares"],
      ans=0,
      why="The largest share in the record is unique and belongs to one of the four gases. "
          "ERT-4.D.1 states that each major gas has its own relative abundance without "
          "saying which is the largest, so the comparison is settled by the measurements."),

 dict(q="Do those four shares account for the whole of dry air, according to the record?",
      table=_T_GASES,
      choices=[
        "Very nearly all of it, since the four shares add to about one hundred percent",
        "About half of it, with the remainder unreported",
        "More than all of it, since the four shares add to more than one hundred percent",
        "About a tenth of it, with the remainder unreported",
        "None of it, since the shares are not measured in percent"],
      ans=0,
      why="Adding 78.08, 20.95, 0.93 and 0.04 gives 100.00 percent. ERT-4.D.1 describes the "
          "gases as having relative abundances, which are shares of one whole."),

 dict(q="About how many times as much nitrogen as oxygen does that record report?",
      table=_T_GASES,
      choices=["About 4 times as much", "About 20 times as much", "About 78 times as much",
               "About the same amount of each", "Less nitrogen than oxygen"],
      ans=0,
      why="The two shares are 78.08 and 20.95 percent, and 78.08 divided by 20.95 is about "
          "3.7. The rejected values are the two shares themselves read as a ratio, or a "
          "comparison the numbers contradict."),

 dict(q="Four layers of the atmosphere were measured for the temperature at each edge. In "
        "which of them does the temperature fall as the altitude rises?",
      table=_T_LAYERS,
      choices=[
        "In the troposphere and in the mesosphere",
        "In the stratosphere and in the thermosphere",
        "In all four of the layers",
        "In none of the four layers",
        "In the troposphere alone"],
      ans=0,
      why="In two of the four layers the temperature at the upper edge is lower than the "
          "temperature at the lower edge, and in the other two it is higher. ERT-4.D.2 "
          "states that the layers of the atmosphere are based on temperature gradients; the "
          "framework gives no direction for any layer, so the direction is read from the "
          "record."),

 dict(q="In which of those same four layers does the temperature rise as the altitude "
        "rises?",
      table=_T_LAYERS,
      choices=[
        "In the stratosphere and in the thermosphere",
        "In the troposphere and in the mesosphere",
        "In all four of the layers",
        "In none of the four layers",
        "In the stratosphere alone"],
      ans=0,
      why="In two of the four layers the temperature at the upper edge is higher than at "
          "the lower edge, and they are not the two in which it falls. ERT-4.D.2 bases the "
          "layers on temperature gradients and gives no direction for any of them, so the "
          "direction is read from the record."),

 dict(q="What happens to the direction of the temperature change from one of those layers "
        "to the next?",
      table=_T_LAYERS,
      choices=[
        "It reverses at every boundary between one layer and the next",
        "It stays the same across every boundary",
        "It reverses at one boundary only",
        "It cannot be told from the record",
        "The temperature does not change within any layer"],
      ans=0,
      why="The temperature falls across the first layer, rises across the second, falls "
          "across the third and rises across the fourth, so the sign of the change is "
          "opposite in every neighbouring pair. ERT-4.D.2 states that the layers of the "
          "atmosphere are based on temperature gradients, and a reversal of the gradient is "
          "what the record shows at each boundary."),

 dict(q="Which of the tabulated layers lies nearest the surface?",
      table=_T_LAYERS,
      choices=["The troposphere", "The stratosphere", "The mesosphere", "The thermosphere",
               "The record does not report altitude"],
      ans=0,
      why="One of the four layers begins at the surface itself and the rest begin above it. "
          "ERT-4.D.2 names the layers without saying which lies lowest, so the ordering is "
          "read from the altitudes in the record."),

 dict(q="Which of the tabulated layers is the thickest?",
      table=_T_LAYERS,
      choices=["The thermosphere", "The troposphere", "The stratosphere", "The mesosphere",
               "The four layers are of equal thickness"],
      ans=0,
      why="Subtracting each layer's lower altitude from its upper one gives thicknesses of "
          "12, 38, 35 and 515 kilometers, and the largest is unique. ERT-4.D.2 gives no "
          "altitude for any layer, so the comparison is settled by the record."),

 dict(q="How do the tabulated layers sit relative to one another in altitude?",
      table=_T_LAYERS,
      choices=[
        "Each one begins at exactly the altitude at which the layer below it ends",
        "Each one begins well above the altitude at which the layer below it ends, leaving "
        "gaps",
        "They overlap one another over most of their extent",
        "They all begin at the surface and differ only in where they end",
        "The record does not report where each layer begins"],
      ans=0,
      why="Every layer's upper altitude equals the lower altitude of the layer above it, so "
          "the four are continuous with no gap and no overlap. ERT-4.D.2 gives no altitudes, "
          "so the arrangement is read from the record."),

 dict(q="Which of the layers the framework names does that record leave out?",
      table=_T_LAYERS,
      choices=["The exosphere", "The troposphere", "The stratosphere", "The mesosphere",
               "The record leaves none of them out"],
      ans=0,
      why="The record carries four layers and ERT-4.D.2 names five, so exactly one of the "
          "framework's names is absent from it. The four present are the four lowest in the "
          "record."),

 dict(q="By how many degrees does the temperature change across the troposphere in that "
        "record?",
      table=_T_LAYERS,
      choices=["By 70 degrees", "By 55 degrees", "By 15 degrees", "By 40 degrees",
               "The record does not report temperature"],
      ans=0,
      why="The troposphere runs from 15 degrees Celsius at its lower edge to minus 55 at "
          "its upper edge, and the difference between them is 70 degrees. The rejected "
          "values are the two edge temperatures themselves and a difference between a "
          "different pair of readings."),

 dict(q="Across which of the tabulated layers does the temperature change by the most "
        "degrees?",
      table=_T_LAYERS,
      choices=["The thermosphere", "The troposphere", "The stratosphere", "The mesosphere",
               "The change is the same across all four"],
      ans=0,
      why="The temperature changes by 70, 55, 90 and 790 degrees across the four layers, "
          "and the largest is unique. ERT-4.D.2 bases the layers on temperature gradients "
          "and gives no size for any of them, so the comparison is settled by the record."),

 dict(q="Which single sentence collects what this topic's two statements assert and nothing "
        "further?",
      choices=[
        "The atmosphere is made up of major gases, each with its own relative abundance, "
        "and its layers are based on temperature gradients and include the troposphere, "
        "stratosphere, mesosphere, thermosphere, and exosphere",
        "The atmosphere is made up of one gas present in a fixed amount, and its layers are "
        "based on temperature gradients and include five named layers",
        "The atmosphere is made up of major gases, each with its own relative abundance, "
        "and its layers are based on the abundance of those gases and include five named "
        "layers",
        "The atmosphere is made up of major gases in equal amounts, and its layers are "
        "based on temperature gradients and include the troposphere, stratosphere, "
        "mesosphere, thermosphere, and exosphere",
        "The atmosphere is made up of major gases, each with its own relative abundance, "
        "and its layers are based on temperature gradients and include the troposphere and "
        "the stratosphere alone"],
      ans=0,
      why="ERT-4.D.1 supplies the major gases and their individual relative abundances and "
          "ERT-4.D.2 supplies the temperature gradients and the five names. Each rejected "
          "summary reduces the gases to one, equalises their abundances, replaces the basis "
          "of the layers, or shortens the list of names."),
]
