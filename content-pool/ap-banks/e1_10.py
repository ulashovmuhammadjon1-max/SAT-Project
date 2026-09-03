# AP ENVIRONMENTAL SCIENCE 1.10 Energy Flow and the 10% Rule
# CED effective Fall 2026, Unit 1 The Living World: Ecosystems.
# Enduring understanding ENG-1: Energy can be converted from one form to another.
# Learning objective ENG-1.C: determine how the energy decreases as it flows through
# ecosystems. Suggested skill 6.B, apply appropriate mathematical relationships to solve
# a problem, with work shown.
#
# Essential knowledge relied on, in the framework's own words:
#   ENG-1.C.1  The 10% rule approximates that in the transfer of energy from one trophic
#              level to the next, only about 10% of the energy is passed on.
#   ENG-1.C.2  The loss of energy that occurs when energy moves from lower to higher
#              trophic levels can be explained through the laws of thermodynamics.
#
# THE ARITHMETIC IS THE POINT AND IT IS RECOMPUTED. Every numeric item is recomputed from
# its own stimulus in verify_e1_10.py, and every quantity is a round multiple of a power
# of ten so the work can be done without a calculator, as the AP exam requires. The
# framework's own words are "approximates" and "about", so no item keys an exact figure
# as though the rule were exact; item 13 and item 18 key that qualification itself.
#
# ON THE THERMODYNAMICS. ENG-1.C.2 says the loss CAN BE EXPLAINED THROUGH the laws of
# thermodynamics and states no law. The presupposed content is therefore only the minimum
# that appealing to those laws requires: the energy is not destroyed, and a portion of it
# becomes unavailable to the next level at each transfer. Nothing further is keyed, and
# every item resting on ENG-1.C.2 says so in its claim.
#
# HOW THIS TOPIC IS KEPT DISTINCT FROM 1.8, 1.9 AND 1.11. Gross and net primary
# productivity are ENG-1.A and belong to 1.8; the direction of energy flow and the
# conservation of matter are ENG-1.B and belong to 1.9; the named consumer categories and
# food-web structure are ENG-1.D and belong to 1.11. Everything here is the QUANTITY
# passed between levels and the reason it is not all of it.
#
# NO FIGURES ARE REFERENCED. Energy pyramids appear as tables of level against energy.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: export_units.py does not typeset
# Environmental Science.
TOPIC = ("1.10", "Energy Flow and the 10% Rule", 1)

_T_CHAIN = dict(
    headers=["Trophic level in one grassland",
             "Energy present (kilocalories per square meter per year)"],
    rows=[["Producers", "20000"],
          ["Primary consumers", "2000"],
          ["Secondary consumers", "200"],
          ["Tertiary consumers", "20"]])

_T_TWOCHAINS = dict(
    headers=["Food chain", "Energy at the producers (kilocalories per square meter per year)",
             "Number of transfers from the producers to the top consumer"],
    rows=[["Chain 1", "100000", "2"],
          ["Chain 2", "100000", "4"]])

_T_MEASURED = dict(
    headers=["Transfer measured in one lake",
             "Energy at the lower level (kilocalories per square meter per year)",
             "Energy at the higher level (kilocalories per square meter per year)"],
    rows=[["Transfer 1", "40000", "4000"],
          ["Transfer 2", "4000", "800"],
          ["Transfer 3", "800", "40"]])

_T_MISSING = dict(
    headers=["Trophic level in one estuary",
             "Energy present (kilocalories per square meter per year)"],
    rows=[["Producers", "60000"],
          ["Primary consumers", "6000"],
          ["Secondary consumers", "Not measured"]])

_T_DIET = dict(
    headers=["Way the same field's production is used",
             "Energy reaching people (kilocalories per square meter per year)"],
    rows=[["People eat the crop grown in the field", "8000"],
          ["Crop is fed to cattle and people eat the cattle", "800"]])

_T_PYRAMID = dict(
    headers=["Trophic level in one forest",
             "Energy present (kilocalories per square meter per year)"],
    rows=[["Level 1", "500000"],
          ["Level 2", "50000"],
          ["Level 3", "5000"],
          ["Level 4", "500"],
          ["Level 5", "50"]])

_T_FATE = dict(
    headers=["What becomes of the energy at one trophic level in a year",
             "Energy (kilocalories per square meter per year)"],
    rows=[["Passed on to the next trophic level", "500"],
          ["Released as heat during respiration", "3600"],
          ["Left in material that is never eaten", "900"]])

QUESTIONS = [

 dict(q="What does the ten percent rule approximate, according to the framework?",
      choices=[
        "That only about a tenth of the energy at one trophic level is passed on to the "
        "next.",
        "That about ten times as much energy is present at each higher trophic level.",
        "That exactly a tenth of the energy at one trophic level is passed on, with no "
        "variation.",
        "That about a tenth of the energy at one trophic level is destroyed at each "
        "transfer.",
        "That about ten trophic levels are present in every ecosystem."],
      ans=0,
      why="ENG-1.C.1 states that the ten percent rule approximates that in the transfer of "
          "energy from one trophic level to the next, only about ten percent of the energy "
          "is passed on. The words approximates and about make it a rule of thumb rather "
          "than an exact law."),

 dict(q="How does the framework say the loss of energy between trophic levels can be "
        "explained?",
      choices=[
        "Through the laws of thermodynamics.",
        "Through the laws of supply and demand.",
        "Through the conservation of species richness.",
        "Through the rate of nitrogen fixation.",
        "Through the distribution of biomes."],
      ans=0,
      why="ENG-1.C.2 states that the loss of energy that occurs when energy moves from "
          "lower to higher trophic levels can be explained through the laws of "
          "thermodynamics."),

 dict(q="Producers in a meadow store fifty thousand kilocalories per square meter per "
        "year. Using the ten percent rule, about how much energy is available to the "
        "primary consumers?",
      choices=[
        "About five thousand kilocalories per square meter per year.",
        "About five hundred thousand kilocalories per square meter per year.",
        "About five hundred kilocalories per square meter per year.",
        "About fifty kilocalories per square meter per year.",
        "About forty-five thousand kilocalories per square meter per year."],
      ans=0,
      why="ENG-1.C.1 passes about a tenth of the energy to the next level, so one step up "
          "from fifty thousand gives about five thousand. Multiplying instead of dividing, "
          "or taking two steps instead of one, produces the rejected values."),

 dict(q="For the same meadow, about how much energy is available to the secondary "
        "consumers, two transfers above the producers?",
      choices=[
        "About five hundred kilocalories per square meter per year.",
        "About five thousand kilocalories per square meter per year.",
        "About fifty kilocalories per square meter per year.",
        "About five kilocalories per square meter per year.",
        "About five million kilocalories per square meter per year."],
      ans=0,
      why="ENG-1.C.1 applies once per transfer, so two transfers take about a tenth of a "
          "tenth. Starting from fifty thousand that leaves about five hundred, while one "
          "transfer alone would leave about five thousand."),

 dict(q="Producers in a pond store one hundred thousand kilocalories per square meter per "
        "year. Using the ten percent rule, about how much energy reaches the tertiary "
        "consumers, three transfers above the producers?",
      choices=[
        "About one hundred kilocalories per square meter per year.",
        "About one thousand kilocalories per square meter per year.",
        "About ten kilocalories per square meter per year.",
        "About ten thousand kilocalories per square meter per year.",
        "About one hundred thousand kilocalories per square meter per year."],
      ans=0,
      why="ENG-1.C.1 passes about a tenth at each of the three transfers, so the producers' "
          "figure is divided by ten three times. Stopping one transfer short or going one "
          "too far produces the two nearest rejected values."),

 dict(q="Using the ten percent rule, about what share of the energy at one trophic level "
        "does NOT reach the next level?",
      choices=[
        "About ninety percent.",
        "About ten percent.",
        "About fifty percent.",
        "None of it, because all energy is passed on.",
        "All of it, because no energy is passed on."],
      ans=0,
      why="ENG-1.C.1 has about ten percent of the energy passed on, so the remainder, "
          "about ninety percent, is what does not reach the next level."),

 dict(q="A top consumer receives about thirty kilocalories per square meter per year, "
        "three transfers above the producers. Using the ten percent rule, about how much "
        "energy did the producers hold?",
      choices=[
        "About thirty thousand kilocalories per square meter per year.",
        "About three thousand kilocalories per square meter per year.",
        "About three hundred thousand kilocalories per square meter per year.",
        "About three hundred kilocalories per square meter per year.",
        "About three kilocalories per square meter per year."],
      ans=0,
      why="Working backwards through the rule multiplies by ten once for each transfer, so "
          "three transfers below thirty gives about thirty thousand. Two transfers or four "
          "transfers produce the nearest rejected values."),

 dict(q="Energy at four trophic levels of one grassland is shown. Which statement is best "
        "supported?",
      table=_T_CHAIN,
      choices=[
        "Each level holds about a tenth of the energy of the level below it, which matches "
        "the ten percent rule.",
        "Each level holds about ten times the energy of the level below it.",
        "Each level holds about the same energy as the level below it.",
        "The highest level holds the most energy of the four.",
        "The energy falls by a fixed number of kilocalories at each step rather than by a "
        "fixed share."],
      ans=0,
      why="Dividing each tabulated value by the one below it gives about a tenth at every "
          "step. ENG-1.C.1 approximates exactly that share for the transfer from one "
          "trophic level to the next."),

 dict(q="Using the same grassland table, about how much energy is lost between the "
        "producers and the primary consumers?",
      table=_T_CHAIN,
      choices=[
        "About eighteen thousand kilocalories per square meter per year.",
        "About two thousand kilocalories per square meter per year.",
        "About twenty thousand kilocalories per square meter per year.",
        "About two hundred kilocalories per square meter per year.",
        "No energy is lost between those two levels."],
      ans=0,
      why="The energy lost is the difference between the two tabulated levels, not the "
          "amount that arrives. ENG-1.C.1 makes the passed-on share about a tenth, so the "
          "difference is about nine tenths of the lower level's figure."),

 dict(q="Two food chains start from producers holding the same energy, as shown. Which "
        "conclusion is best supported?",
      table=_T_TWOCHAINS,
      choices=[
        "The top consumer of the chain with fewer transfers has far more energy available "
        "to it.",
        "The top consumer of the chain with more transfers has far more energy available "
        "to it.",
        "The two top consumers have the same energy available, because the producers are "
        "equal.",
        "The chain with more transfers loses no energy at any step.",
        "The number of transfers has no bearing on the energy reaching the top."],
      ans=0,
      why="ENG-1.C.1 removes about nine tenths of the energy at each transfer, so with the "
          "producers equal, two extra transfers reduce the energy reaching the top by about "
          "a factor of a hundred."),

 dict(q="Three energy transfers measured in one lake are shown. Which transfer passed on "
        "the largest share of the energy available to it?",
      table=_T_MEASURED,
      choices=[
        "Transfer 2, which passed on about a fifth.",
        "Transfer 1, which passed on about a tenth.",
        "Transfer 3, which passed on about a twentieth.",
        "All three passed on the same share.",
        "Transfer 3, which passed on about half."],
      ans=0,
      why="The share passed on is the higher-level figure divided by the lower-level "
          "figure, computed for each row. ENG-1.C.1 calls ten percent an approximation, so "
          "measured transfers may sit above or below it."),

 dict(q="An estuary was measured as shown. Using the ten percent rule, about how much "
        "energy would be expected at the secondary consumers?",
      table=_T_MISSING,
      choices=[
        "About six hundred kilocalories per square meter per year.",
        "About six thousand kilocalories per square meter per year.",
        "About sixty kilocalories per square meter per year.",
        "About sixty thousand kilocalories per square meter per year.",
        "About six kilocalories per square meter per year."],
      ans=0,
      why="The tabulated levels already fall by a factor of ten from producers to primary "
          "consumers, and ENG-1.C.1 applies the same approximation to the next transfer, so "
          "the missing value is about a tenth of the primary consumers' figure."),

 dict(q="The same field's production was used in two ways, as shown. Which explanation of "
        "the difference is best supported?",
      table=_T_DIET,
      choices=[
        "Adding a trophic level between the crop and people removes about nine tenths of "
        "the energy.",
        "Adding a trophic level between the crop and people removes about a tenth of the "
        "energy.",
        "Cattle create additional energy that people can then use.",
        "The two ways deliver the same energy, so the table must be in error.",
        "Feeding the crop to cattle raises the energy reaching people about tenfold."],
      ans=0,
      why="The tabulated energy reaching people falls by a factor of ten when an extra "
          "transfer is inserted, and ENG-1.C.1 approximates that only about a tenth of the "
          "energy is passed on at each transfer."),

 dict(q="Why does the framework describe the ten percent figure as an approximation?",
      choices=[
        "Because the framework's own wording is that the rule approximates that only about "
        "ten percent is passed on.",
        "Because the true figure is always exactly ten percent in every ecosystem.",
        "Because the figure applies only to the transfer from producers to primary "
        "consumers.",
        "Because the figure applies only to aquatic ecosystems.",
        "Because the figure describes matter rather than energy."],
      ans=0,
      why="ENG-1.C.1 uses the words approximates and about, which is what makes the rule a "
          "working estimate for any transfer from one trophic level to the next rather "
          "than an exact quantity."),

 dict(q="A student says the energy that does not reach the next trophic level has been "
        "destroyed. What is the best correction?",
      choices=[
        "It has not been destroyed; it has become unavailable to the next level, which is "
        "what the laws of thermodynamics account for.",
        "It has been destroyed, and the laws of thermodynamics describe that destruction.",
        "It has been converted into matter at the next trophic level.",
        "It has been passed to a lower trophic level instead.",
        "It has been returned unchanged to the sun."],
      ans=0,
      why="ENG-1.C.2 states that the loss of energy between trophic levels can be explained "
          "through the laws of thermodynamics, and the minimum that appeal requires is "
          "that the energy is not destroyed but becomes unavailable to the level above."),

 dict(q="What becomes of the energy at one trophic level in the year shown? Which "
        "conclusion is best supported?",
      table=_T_FATE,
      choices=[
        "Only a small fraction of the energy at that level is passed on, and most of it "
        "leaves by other routes.",
        "Most of the energy at that level is passed on to the next level.",
        "All of the energy at that level is passed on to the next level.",
        "None of the energy at that level leaves as heat.",
        "The energy passed on exceeds the energy released as heat."],
      ans=0,
      why="The passed-on entry is a small share of the tabulated total while the other two "
          "routes take most of it. ENG-1.C.1 approximates that only about ten percent is "
          "passed on at each transfer."),

 dict(q="Five trophic levels in one forest are shown. About how many times smaller is the "
        "energy at Level 4 than the energy at Level 1?",
      table=_T_PYRAMID,
      choices=[
        "About one thousand times smaller.",
        "About one hundred times smaller.",
        "About ten times smaller.",
        "About ten thousand times smaller.",
        "The two levels hold about the same energy."],
      ans=0,
      why="Three transfers separate the two levels, and ENG-1.C.1 passes about a tenth at "
          "each, so the ratio is about a tenth cubed. The tabulated values reproduce that "
          "ratio directly."),

 dict(q="Using the same forest table, which level is the first to hold less than one "
        "hundred kilocalories per square meter per year?",
      table=_T_PYRAMID,
      choices=[
        "Level 5.",
        "Level 4.",
        "Level 3.",
        "Level 2.",
        "No level in the table holds less than that."],
      ans=0,
      why="Reading down the tabulated energy column and comparing each value against one "
          "hundred identifies the first level below it. ENG-1.C.1 is the reason the values "
          "fall so quickly from one level to the next."),

 dict(q="Two ecologists measure the transfer from producers to primary consumers in "
        "different ecosystems and obtain fourteen percent and seven percent. What does the "
        "framework support concluding?",
      choices=[
        "Both results are consistent with the rule, because it approximates about ten "
        "percent rather than fixing an exact value.",
        "Both results must be errors, because the rule fixes the transfer at exactly ten "
        "percent.",
        "Only the fourteen percent result is consistent with the rule.",
        "Only the seven percent result is consistent with the rule.",
        "Neither result concerns energy transfer between trophic levels."],
      ans=0,
      why="ENG-1.C.1 says the rule APPROXIMATES that ABOUT ten percent is passed on, so "
          "measured values scattered around a tenth are what the framework's own wording "
          "leads one to expect."),

 dict(q="Why does the ten percent rule imply that food chains cannot have very many "
        "levels?",
      choices=[
        "Because about nine tenths of the energy is removed at each transfer, so little "
        "remains after a few steps.",
        "Because each level requires ten times the energy of the level below it.",
        "Because energy is destroyed after a fixed number of transfers.",
        "Because the number of levels is fixed by the number of species present.",
        "Because energy stops moving upward once three levels are present."],
      ans=0,
      why="ENG-1.C.1 passes on only about a tenth at each transfer, so the energy available "
          "falls by about a factor of ten per step and reaches a level too small to "
          "support another consumer within a few steps."),

 dict(q="A grassland's producers hold eight hundred thousand kilocalories per square meter "
        "per year. Using the ten percent rule, about how much energy reaches the level two "
        "transfers above them?",
      choices=[
        "About eight thousand kilocalories per square meter per year.",
        "About eighty thousand kilocalories per square meter per year.",
        "About eight hundred kilocalories per square meter per year.",
        "About eighty kilocalories per square meter per year.",
        "About eight million kilocalories per square meter per year."],
      ans=0,
      why="ENG-1.C.1 applies once per transfer, so two transfers divide the producers' "
          "figure by ten twice. One transfer or three transfers produce the two nearest "
          "rejected values."),

 dict(q="Which set of units is appropriate for an answer giving the energy available at a "
        "trophic level in a given area each year?",
      choices=[
        "Kilocalories per square meter per year.",
        "Kilocalories alone.",
        "Square meters per year.",
        "Kilocalories per organism.",
        "Percent per year."],
      ans=0,
      why="Energy at a trophic level in a stated area over a stated period carries an "
          "energy unit, an area unit and a time unit together, which is the same form "
          "ENG-1.A.4 gives for productivity."),

 dict(q="Which observation would best support the claim that the loss between trophic "
        "levels is a matter of energy becoming unavailable rather than disappearing?",
      choices=[
        "The energy passed on, the energy released as heat and the energy left uneaten "
        "together account for all the energy at the lower level.",
        "The energy at each level is smaller than the energy at the level below it.",
        "The number of organisms falls at each higher trophic level.",
        "The organisms at higher levels are larger than those at lower levels.",
        "The ecosystem receives sunlight throughout the year."],
      ans=0,
      why="ENG-1.C.2 attributes the loss to what the laws of thermodynamics explain, and "
          "the minimum that appeal requires is that the energy is accounted for rather than "
          "destroyed, which is what a closing energy budget shows."),

 dict(q="A pond's primary consumers hold nine hundred kilocalories per square meter per "
        "year. Using the ten percent rule, about how much energy did the producers hold?",
      choices=[
        "About nine thousand kilocalories per square meter per year.",
        "About ninety kilocalories per square meter per year.",
        "About ninety thousand kilocalories per square meter per year.",
        "About nine hundred kilocalories per square meter per year.",
        "About nine kilocalories per square meter per year."],
      ans=0,
      why="Working backwards through one transfer multiplies by ten, since ENG-1.C.1 passes "
          "on about a tenth going upward. Going the wrong way, or applying two transfers, "
          "produces the nearest rejected values."),

 dict(q="Two ecosystems have producers holding the same energy, but one supports four "
        "trophic levels and the other supports three. Which statement does the framework "
        "support?",
      choices=[
        "The energy available at the top of the four-level ecosystem is about a tenth of "
        "that at the top of the three-level one.",
        "The energy available at the top of the four-level ecosystem is about ten times "
        "that at the top of the three-level one.",
        "The two top levels hold the same energy, because the producers are equal.",
        "The four-level ecosystem loses no energy at its extra transfer.",
        "The three-level ecosystem must have more productive producers."],
      ans=0,
      why="With equal producers the two chains differ by one transfer, and ENG-1.C.1 passes "
          "on about a tenth at a transfer, so the longer chain's top level holds about a "
          "tenth of what the shorter chain's top level holds."),

 dict(q="Which of the following best states what the ten percent rule does NOT claim?",
      choices=[
        "That the same exact fraction is transferred at every step in every ecosystem.",
        "That only about a tenth of the energy moves to the next trophic level.",
        "That energy decreases as it moves to higher trophic levels.",
        "That the rule is an approximation.",
        "That the transfer concerned is from one trophic level to the next."],
      ans=0,
      why="ENG-1.C.1 uses the words approximates and about, so exactness is precisely what "
          "the statement withholds, while each rejected option restates part of what it "
          "does assert."),

 dict(q="An ecosystem's producers double the energy they store, and the number of trophic "
        "levels is unchanged. Using the ten percent rule, what happens to the energy "
        "available at the top level?",
      choices=[
        "It roughly doubles, because the same fraction is passed on at each unchanged "
        "transfer.",
        "It is unchanged, because the rule fixes the top level's energy.",
        "It roughly halves, because more energy is lost at each transfer.",
        "It rises tenfold, because the rule multiplies by ten.",
        "It cannot be predicted, because the rule applies only to producers."],
      ans=0,
      why="ENG-1.C.1 makes each transfer pass on about a fixed fraction, so multiplying the "
          "starting energy by a factor multiplies the energy at every level above by the "
          "same factor."),

 dict(q="Which statement correctly relates the ten percent rule to the laws of "
        "thermodynamics as the framework presents them?",
      choices=[
        "The rule describes how much energy is passed on; the laws of thermodynamics are "
        "what explain why so little is.",
        "The laws of thermodynamics describe how much energy is passed on; the rule "
        "explains why.",
        "The rule and the laws of thermodynamics both describe the movement of matter.",
        "The rule contradicts the laws of thermodynamics.",
        "Neither the rule nor the laws of thermodynamics concerns energy transfer between "
        "trophic levels."],
      ans=0,
      why="ENG-1.C.1 supplies the quantity, about ten percent passed on, and ENG-1.C.2 "
          "states that the loss of energy moving from lower to higher trophic levels can be "
          "explained through the laws of thermodynamics."),

 dict(q="Using the lake transfers measured earlier, which transfer fell furthest below the "
        "share the ten percent rule approximates?",
      table=_T_MEASURED,
      choices=[
        "Transfer 3, which passed on about a twentieth.",
        "Transfer 1, which passed on about a fifth.",
        "Transfer 2, which passed on about a hundredth.",
        "All three fell equally far below a tenth.",
        "None of the three fell below a tenth."],
      ans=0,
      why="Dividing each higher-level figure by its lower-level figure gives the share "
          "actually passed on, and the smallest of those shares is the one furthest below "
          "the tenth that ENG-1.C.1 approximates."),

 dict(q="Why is it a mistake to conclude from the ten percent rule that ecosystems waste "
        "ninety percent of their energy?",
      choices=[
        "Because the energy not passed on is used by the organisms at that level and "
        "released in forms the next level cannot use.",
        "Because the energy not passed on is destroyed rather than wasted.",
        "Because no energy is actually lost between trophic levels.",
        "Because the rule concerns matter rather than energy.",
        "Because the rule applies only to producers and not to consumers."],
      ans=0,
      why="ENG-1.C.2 explains the loss through the laws of thermodynamics, and the minimum "
          "that appeal requires is that the energy is accounted for rather than destroyed; "
          "it leaves the chain because it becomes unavailable, not because it vanishes."),
]
