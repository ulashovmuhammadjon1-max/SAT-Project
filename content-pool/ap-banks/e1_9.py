# AP ENVIRONMENTAL SCIENCE 1.9 Trophic Levels
# CED effective Fall 2026, Unit 1 The Living World: Ecosystems.
# Enduring understanding ENG-1: Energy can be converted from one form to another.
# Learning objective ENG-1.B: explain how energy flows and matter cycles through trophic
# levels. Suggested skill 1.A.
#
# Essential knowledge relied on, in the framework's own words:
#   ENG-1.B.1  All ecosystems depend on a continuous inflow of high-quality energy in
#              order to maintain their structure and function of transferring matter
#              between the environment and organisms via biogeochemical cycles.
#   ENG-1.B.2  Biogeochemical cycles are essential for life and each cycle demonstrates
#              the conservation of matter.
#   ENG-1.B.3  In terrestrial and near-surface marine communities, energy flows from the
#              sun to producers in the lowest trophic levels and then upward to higher
#              trophic levels.
#
# HOW THIS TOPIC IS KEPT DISTINCT FROM 1.10 AND 1.11. The QUANTITY of energy passed
# between levels is ENG-1.C.1, the ten percent rule, and belongs to topic 1.10; nothing
# here tabulates or keys a transfer efficiency. The NAMED categories of consumer --
# herbivore, omnivore, carnivore, detritivore, decomposer -- and the structure of food
# webs are ENG-1.D.1 and ENG-1.D.2 and belong to topic 1.11; nothing here asks a student
# to classify an organism into one of those categories. What is asked here is only what
# ENG-1.B contains: the requirement for a continuous energy inflow, the conservation of
# matter in biogeochemical cycles, and the DIRECTION of energy flow, from the sun to
# producers at the lowest level and then upward.
#
# ON THE SCOPE OF ENG-1.B.3. The framework restricts the sun-to-producers statement to
# terrestrial and near-surface marine communities. Item 27 keys that restriction as a fact
# about the framework's own wording and does not ask about any community outside it.
#
# NO FIGURES ARE REFERENCED. Energy and matter budgets are given as tables.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: export_units.py does not typeset
# Environmental Science.
TOPIC = ("1.9", "Trophic Levels", 1)

_T_DARK = dict(
    headers=["Sealed chamber holding a small ecosystem", "Light supplied each day (hours)",
             "Living mass remaining after six months (percent of the starting mass)"],
    rows=[["Chamber 1", "12", "96"],
          ["Chamber 2", "4", "58"],
          ["Chamber 3", "0", "7"]])

_T_MATTER = dict(
    headers=["Nitrogen budget for one field over a year (kilograms per hectare)", "Amount"],
    rows=[["Nitrogen entering the field", "150"],
          ["Nitrogen leaving the field", "110"],
          ["Increase in nitrogen stored in the field", "40"]])

_T_CARBON = dict(
    headers=["Carbon budget for one woodland over a year (tonnes)", "Amount"],
    rows=[["Carbon taken in from the air by producers", "820"],
          ["Carbon returned to the air by all organisms", "640"],
          ["Increase in carbon held in wood and soil", "180"]])

_T_SHADE = dict(
    headers=["Pond enclosure", "Percent of sunlight allowed to reach the water",
             "Mass of producers after one season (grams per square meter)",
             "Mass of consumers after one season (grams per square meter)"],
    rows=[["Enclosure 1", "100", "310", "42"],
          ["Enclosure 2", "50", "160", "24"],
          ["Enclosure 3", "10", "35", "6"]])

_T_SUNCAP = dict(
    headers=["Site", "Sunlight arriving each year (kilocalories per square meter)",
             "Energy captured by producers each year (kilocalories per square meter)"],
    rows=[["Site 1", "500000", "1200"],
          ["Site 2", "900000", "2600"],
          ["Site 3", "1400000", "4100"]])

_T_WETLAND = dict(
    headers=["Water and dissolved matter for one wetland over a month (tonnes)", "Amount"],
    rows=[["Matter entering in the inflowing stream", "520"],
          ["Matter leaving in the outflowing stream", "455"],
          ["Matter added to the wetland's sediments and living tissue", "65"]])

_T_LEVELS = dict(
    headers=["Organism in one grassland", "What it obtains its energy from"],
    rows=[["Organism 1", "Sunlight"],
          ["Organism 2", "Eating Organism 1"],
          ["Organism 3", "Eating Organism 2"],
          ["Organism 4", "Eating Organism 3"]])

_T_INFLOW = dict(
    headers=["Cave pool receiving no sunlight", "Organic matter washed in each month (grams)",
             "Living mass of the pool community (grams)"],
    rows=[["Month 1", "400", "260"],
          ["Month 4", "180", "150"],
          ["Month 7", "40", "48"],
          ["Month 10", "5", "9"]])

QUESTIONS = [

 dict(q="What does the framework say all ecosystems depend on?",
      choices=[
        "A continuous inflow of high-quality energy.",
        "A continuous inflow of new matter from outside the Earth.",
        "The complete absence of any energy loss.",
        "A single pulse of energy at the moment the ecosystem forms.",
        "The presence of at least four trophic levels."],
      ans=0,
      why="ENG-1.B.1 states that all ecosystems depend on a continuous inflow of "
          "high-quality energy. The word continuous is part of the claim, which is what "
          "rules out a single initial pulse."),

 dict(q="According to the framework, what does that continuous inflow of energy allow an "
        "ecosystem to maintain?",
      choices=[
        "Its structure and its function of transferring matter between the environment "
        "and organisms via biogeochemical cycles.",
        "A fixed number of individuals in every population it contains.",
        "A constant temperature everywhere within it.",
        "A supply of new matter created within the ecosystem.",
        "An unchanging list of species over geological time."],
      ans=0,
      why="ENG-1.B.1 states that ecosystems depend on a continuous inflow of high-quality "
          "energy in order to maintain their structure and function of transferring matter "
          "between the environment and organisms via biogeochemical cycles."),

 dict(q="What does the framework say each biogeochemical cycle demonstrates?",
      choices=[
        "The conservation of matter.",
        "The creation of new matter within living organisms.",
        "The destruction of matter as energy is released.",
        "The conversion of matter into energy.",
        "The steady increase of matter in every reservoir."],
      ans=0,
      why="ENG-1.B.2 states that biogeochemical cycles are essential for life and that "
          "each cycle demonstrates the conservation of matter."),

 dict(q="How does the framework describe the importance of biogeochemical cycles?",
      choices=[
        "They are essential for life.",
        "They are useful but not necessary for life.",
        "They occur only in aquatic ecosystems.",
        "They operate only where humans have altered an ecosystem.",
        "They replace the need for an inflow of energy."],
      ans=0,
      why="ENG-1.B.2 states plainly that biogeochemical cycles are essential for life, and "
          "ENG-1.B.1 keeps the inflow of energy as a separate requirement rather than one "
          "the cycles can replace."),

 dict(q="In terrestrial and near-surface marine communities, in which direction does the "
        "framework say energy flows?",
      choices=[
        "From the sun to producers in the lowest trophic levels and then upward to higher "
        "trophic levels.",
        "From the highest trophic levels downward to producers and then to the sun.",
        "From producers to the sun and then to higher trophic levels.",
        "Equally in both directions between every pair of trophic levels.",
        "From the soil upward to producers without any input from the sun."],
      ans=0,
      why="ENG-1.B.3 states that in terrestrial and near-surface marine communities energy "
          "flows from the sun to producers in the lowest trophic levels and then upward to "
          "higher trophic levels."),

 dict(q="Which organisms does the framework place in the lowest trophic levels?",
      choices=[
        "Producers.",
        "The largest predators in the community.",
        "The organisms that eat other organisms.",
        "The organisms with the longest life spans.",
        "The organisms that occupy the greatest area."],
      ans=0,
      why="ENG-1.B.3 states that energy flows from the sun to producers in the lowest "
          "trophic levels and then upward, which places producers at the bottom of the "
          "sequence it describes."),

 dict(q="To which communities does the framework attach its statement about energy flowing "
        "from the sun to producers and then upward?",
      choices=[
        "Terrestrial and near-surface marine communities.",
        "Every community on Earth without exception.",
        "Deep-sea communities only.",
        "Freshwater communities only.",
        "Communities that contain no consumers."],
      ans=0,
      why="ENG-1.B.3 opens with the phrase in terrestrial and near-surface marine "
          "communities, so the scope of the statement is written into the framework's own "
          "wording."),

 dict(q="Three sealed chambers holding small ecosystems received different amounts of "
        "light, as shown. Which conclusion is best supported?",
      table=_T_DARK,
      choices=[
        "The ecosystems that received less energy lost more of their living mass, which "
        "fits a dependence on a continuous inflow of energy.",
        "The ecosystems that received less energy retained more of their living mass.",
        "The amount of light supplied had no effect on the living mass retained.",
        "The chamber receiving no light retained the most living mass.",
        "All three chambers retained about the same living mass."],
      ans=0,
      why="Living mass retained falls at every step down the light column, and the "
          "chamber with no light retained almost none. ENG-1.B.1 states that all "
          "ecosystems depend on a continuous inflow of high-quality energy to maintain "
          "their structure."),

 dict(q="A nitrogen budget for one field is shown. Which statement about the budget is "
        "best supported?",
      table=_T_MATTER,
      choices=[
        "The nitrogen entering equals the nitrogen leaving plus the increase in nitrogen "
        "stored, so none is unaccounted for.",
        "The nitrogen entering is less than the nitrogen leaving, so nitrogen was "
        "destroyed.",
        "The nitrogen leaving equals the nitrogen entering, so nothing was stored.",
        "The increase in stored nitrogen is larger than the nitrogen that entered.",
        "The budget cannot balance, because nitrogen changes chemical form in the soil."],
      ans=0,
      why="Adding the outflow to the change in storage reproduces the inflow exactly. "
          "ENG-1.B.2 states that each biogeochemical cycle demonstrates the conservation "
          "of matter, and a balanced budget is what conservation looks like in data."),

 dict(q="A carbon budget for one woodland is shown. Which statement is best supported?",
      table=_T_CARBON,
      choices=[
        "The carbon taken in is accounted for by the carbon returned plus the carbon added "
        "to wood and soil.",
        "The carbon taken in exceeds everything accounted for, so some carbon was "
        "destroyed.",
        "The carbon returned exceeds the carbon taken in, so the woodland lost carbon over "
        "the year.",
        "No carbon was added to wood and soil over the year.",
        "The woodland created carbon during the year."],
      ans=0,
      why="The return figure plus the increase in storage reproduces the intake exactly. "
          "ENG-1.B.2 states that each biogeochemical cycle demonstrates the conservation "
          "of matter."),

 dict(q="Three pond enclosures received different amounts of sunlight, as shown. Which "
        "conclusion is best supported?",
      table=_T_SHADE,
      choices=[
        "Reducing the sunlight reduced the mass of producers and of consumers together, "
        "which fits energy entering the community through the producers.",
        "Reducing the sunlight reduced the producers but raised the consumers.",
        "Reducing the sunlight raised both producers and consumers.",
        "The enclosure receiving the least sunlight held the most producers.",
        "Consumers were unaffected by the amount of sunlight reaching the water."],
      ans=0,
      why="Both the producer column and the consumer column fall as the sunlight column "
          "falls. ENG-1.B.3 states that energy flows from the sun to producers in the "
          "lowest trophic levels and then upward, so restricting the sun restricts what "
          "reaches the levels above."),

 dict(q="Sunlight arriving and energy captured by producers were measured at three sites, "
        "as shown. Which statement is best supported?",
      table=_T_SUNCAP,
      choices=[
        "Sites receiving more sunlight had producers capturing more energy, though the "
        "captured amount is a small part of what arrived.",
        "Sites receiving more sunlight had producers capturing less energy.",
        "Producers captured all of the sunlight that arrived at each site.",
        "The amount captured was the same at all three sites.",
        "The site receiving the least sunlight captured the most energy."],
      ans=0,
      why="Both columns rise together while the captured column stays a small fraction of "
          "the arriving column at every site. ENG-1.B.3 makes the sun the source that "
          "producers draw on, and ENG-1.B.1 makes the inflow continuous rather than "
          "complete."),

 dict(q="A student writes that energy cycles through an ecosystem in the same way matter "
        "does. What is the best correction?",
      choices=[
        "Matter is cycled through biogeochemical cycles, while energy must be supplied "
        "continuously from outside.",
        "Energy is cycled through biogeochemical cycles, while matter must be supplied "
        "continuously from outside.",
        "Both energy and matter must be supplied continuously from outside.",
        "Both energy and matter are cycled and neither needs an outside supply.",
        "Neither energy nor matter moves through an ecosystem at all."],
      ans=0,
      why="ENG-1.B.2 puts matter in cycles that demonstrate its conservation, while "
          "ENG-1.B.1 makes an ecosystem depend on a CONTINUOUS INFLOW of high-quality "
          "energy, which is not the description of something that cycles."),

 dict(q="Why can an ecosystem sealed away from any outside energy source not maintain its "
        "structure indefinitely?",
      choices=[
        "Because all ecosystems depend on a continuous inflow of high-quality energy.",
        "Because matter is destroyed whenever it passes through an organism.",
        "Because biogeochemical cycles cannot operate without new matter entering.",
        "Because trophic levels reverse direction when energy is scarce.",
        "Because producers convert matter into energy and eventually run out of matter."],
      ans=0,
      why="ENG-1.B.1 states that all ecosystems depend on a continuous inflow of "
          "high-quality energy in order to maintain their structure and function, so "
          "removing the inflow removes what maintains the structure."),

 dict(q="Four organisms in one grassland are described as shown. Which is at the lowest "
        "trophic level?",
      table=_T_LEVELS,
      choices=[
        "Organism 1, which obtains its energy from sunlight.",
        "Organism 2, which obtains its energy by eating Organism 1.",
        "Organism 3, which obtains its energy by eating Organism 2.",
        "Organism 4, which obtains its energy by eating Organism 3.",
        "All four are at the same trophic level, because they share one grassland."],
      ans=0,
      why="ENG-1.B.3 places producers in the lowest trophic levels and has energy flow "
          "from the sun to them and then upward, so the organism drawing its energy "
          "directly from sunlight is the one at the bottom of the sequence."),

 dict(q="Using the same four organisms, which sequence follows the direction in which the "
        "framework says energy flows?",
      table=_T_LEVELS,
      choices=[
        "Sunlight, then Organism 1, then Organism 2, then Organism 3, then Organism 4.",
        "Organism 4, then Organism 3, then Organism 2, then Organism 1, then sunlight.",
        "Organism 1, then sunlight, then Organism 2, then Organism 3, then Organism 4.",
        "Sunlight, then Organism 4, then Organism 3, then Organism 2, then Organism 1.",
        "Organism 2, then Organism 1, then sunlight, then Organism 3, then Organism 4."],
      ans=0,
      why="ENG-1.B.3 states that energy flows from the sun to producers in the lowest "
          "trophic levels and then upward to higher trophic levels, and the table's "
          "feeding relationships fix which organism sits above which."),

 dict(q="A cave pool receives no sunlight and depends on organic matter washed in from "
        "outside. The record is shown. Which conclusion is best supported?",
      table=_T_INFLOW,
      choices=[
        "The living mass of the community fell as the inflow of material fell, which fits "
        "a dependence on a continuous inflow.",
        "The living mass of the community rose as the inflow of material fell.",
        "The living mass of the community was unaffected by the inflow.",
        "The community reached its largest living mass in the month with the smallest "
        "inflow.",
        "The inflow of material was the same in every month recorded."],
      ans=0,
      why="Both columns fall together across the record. ENG-1.B.1 states that all "
          "ecosystems depend on a continuous inflow of high-quality energy in order to "
          "maintain their structure and function."),

 dict(q="Which statement about matter in a biogeochemical cycle is supported by the "
        "framework?",
      choices=[
        "Matter moves between reservoirs and is neither created nor destroyed along the "
        "way.",
        "Matter is created at the start of each cycle and destroyed at its end.",
        "Matter is converted into energy each time it passes through an organism.",
        "Matter accumulates without limit in whichever reservoir it enters first.",
        "Matter leaves the Earth at the end of each cycle."],
      ans=0,
      why="ENG-1.B.2 states that each biogeochemical cycle demonstrates the conservation "
          "of matter, which is precisely the claim that matter is neither created nor "
          "destroyed as it moves."),

 dict(q="A matter budget for a wetland is shown. Which reading of the budget is best "
        "supported?",
      table=_T_WETLAND,
      choices=[
        "Everything that entered is accounted for, either as material that left or as "
        "material retained.",
        "More material left than entered, so some was created inside the wetland.",
        "Less material is accounted for than entered, so some was destroyed inside the "
        "wetland.",
        "Nothing was retained by the wetland during the month.",
        "The wetland retained more material than entered it."],
      ans=0,
      why="The outflow plus the material retained reproduces the inflow exactly. ENG-1.B.2 "
          "states that each biogeochemical cycle demonstrates the conservation of matter, "
          "which is what a closing budget shows."),

 dict(q="What does calling the required energy inflow high-quality most directly "
        "emphasise, given the framework's account?",
      choices=[
        "That an ecosystem needs energy in a usable form supplied from outside, not merely "
        "any energy already present within it.",
        "That an ecosystem needs matter rather than energy.",
        "That an ecosystem needs the same energy to arrive only once.",
        "That an ecosystem can substitute matter for energy when energy is short.",
        "That an ecosystem's energy requirement falls as it grows."],
      ans=0,
      why="ENG-1.B.1 specifies a continuous inflow of high-quality energy as what "
          "maintains an ecosystem's structure and function, so both the continuity and the "
          "quality of the supply are conditions the framework sets on it."),

 dict(q="Which of the following best explains why removing an ecosystem's producers "
        "affects the levels above them?",
      choices=[
        "Energy enters the community at the producers and flows upward from there.",
        "Energy enters the community at the highest trophic level and flows downward.",
        "Producers destroy the matter that higher levels would otherwise use.",
        "Higher trophic levels obtain their energy directly from the sun.",
        "Producers occupy the highest trophic level in the community."],
      ans=0,
      why="ENG-1.B.3 states that energy flows from the sun to producers in the lowest "
          "trophic levels and then upward to higher trophic levels, so the producers are "
          "the point of entry for everything above them."),

 dict(q="Which observation would best support the claim that matter is conserved within an "
        "ecosystem's cycles?",
      choices=[
        "A complete budget for one element, in which the inputs equal the outputs plus the "
        "change in what is stored.",
        "A measurement of how much of one element an ecosystem contains at one instant.",
        "A count of the number of species that contain the element.",
        "A record of how much sunlight the ecosystem receives in a year.",
        "A list of the reservoirs in which the element occurs."],
      ans=0,
      why="ENG-1.B.2 states that each biogeochemical cycle demonstrates the conservation "
          "of matter, and conservation is shown by a budget that closes rather than by a "
          "single standing measurement or an inventory of places."),

 dict(q="Which comparison correctly distinguishes what ENG-1.B.1 requires from what "
        "ENG-1.B.2 asserts?",
      choices=[
        "One requires a continuous supply of energy from outside; the other says matter is "
        "conserved as it cycles.",
        "One requires a continuous supply of matter from outside; the other says energy is "
        "conserved as it cycles.",
        "Both require a continuous supply of matter from outside.",
        "Both say that energy is conserved as it cycles.",
        "Neither concerns energy or matter."],
      ans=0,
      why="ENG-1.B.1 states the dependence on a continuous inflow of high-quality energy, "
          "and ENG-1.B.2 states that each biogeochemical cycle demonstrates the "
          "conservation of matter, so the two statements concern different quantities."),

 dict(q="Two ecosystems are alike in every way except that one receives far more solar "
        "energy each year. Which prediction does the framework support?",
      choices=[
        "The ecosystem receiving more solar energy has more energy entering at its "
        "producers to pass upward.",
        "The ecosystem receiving more solar energy has less energy entering at its "
        "producers.",
        "The two ecosystems must have identical energy inflows, because energy is "
        "conserved.",
        "The ecosystem receiving more solar energy will pass energy downward instead of "
        "upward.",
        "Solar energy has no bearing on what enters an ecosystem's producers."],
      ans=0,
      why="ENG-1.B.3 states that energy flows from the sun to producers in the lowest "
          "trophic levels and then upward, so a larger supply at the source is a larger "
          "supply at the point of entry."),

 dict(q="Why does the framework describe the maintenance of an ecosystem's structure and "
        "the cycling of matter as depending on the same energy inflow?",
      choices=[
        "Because the inflow maintains both the structure and the function of transferring "
        "matter between the environment and organisms.",
        "Because the inflow supplies the matter that the cycles move.",
        "Because matter and energy are the same quantity measured in different units.",
        "Because the cycles create the energy the structure requires.",
        "Because the structure of an ecosystem is unrelated to the matter within it."],
      ans=0,
      why="ENG-1.B.1 places both in one clause: the inflow of high-quality energy is what "
          "maintains an ecosystem's structure AND its function of transferring matter "
          "between the environment and organisms via biogeochemical cycles."),

 dict(q="An ecologist finds that the total mass of one element in a lake is unchanged over "
        "a decade, although large amounts entered and left each year. Which framework "
        "statement does this illustrate?",
      choices=[
        "Each biogeochemical cycle demonstrates the conservation of matter.",
        "All ecosystems depend on a continuous inflow of high-quality energy.",
        "Energy flows from the sun to producers and then upward.",
        "Producers occupy the lowest trophic levels.",
        "Biogeochemical cycles operate only in terrestrial communities."],
      ans=0,
      why="Large flows in and out that leave the standing amount unchanged is a balance of "
          "inputs and outputs, and ENG-1.B.2 states that each biogeochemical cycle "
          "demonstrates the conservation of matter."),

 dict(q="The framework states its account of energy flowing from the sun to producers for "
        "terrestrial and near-surface marine communities. What does that wording indicate?",
      choices=[
        "The statement is asserted for those communities rather than for every community "
        "on Earth.",
        "The statement is asserted for every community on Earth, and the wording is "
        "decorative.",
        "The statement applies only to communities that contain no consumers.",
        "The statement applies only where humans have altered the community.",
        "The statement applies only to communities studied in the last century."],
      ans=0,
      why="ENG-1.B.3 opens with the clause naming terrestrial and near-surface marine "
          "communities, and a clause of that kind states the scope of the sentence that "
          "follows it."),

 dict(q="Which of the following is NOT something the framework claims about ecosystems and "
        "their energy?",
      choices=[
        "That an ecosystem can maintain its structure indefinitely without any energy "
        "entering it.",
        "That all ecosystems depend on a continuous inflow of high-quality energy.",
        "That the inflow maintains an ecosystem's structure and function.",
        "That matter is transferred between the environment and organisms via "
        "biogeochemical cycles.",
        "That energy flows upward from producers to higher trophic levels."],
      ans=0,
      why="ENG-1.B.1 makes the dependence on a continuous inflow universal across "
          "ecosystems, so the keyed statement contradicts it, while each rejected option "
          "restates part of ENG-1.B.1 or ENG-1.B.3."),

 dict(q="An ecosystem's energy inflow is halved and held there for several years. Which "
        "pair of outcomes does the framework most directly support expecting?",
      choices=[
        "Less energy passes upward from the producers, and the ecosystem's structure "
        "becomes harder to maintain.",
        "More energy passes upward from the producers, and the structure becomes easier to "
        "maintain.",
        "The ecosystem begins creating its own energy to compensate.",
        "Matter stops cycling, and energy begins cycling instead.",
        "The direction of energy flow reverses, running from consumers to producers."],
      ans=0,
      why="ENG-1.B.3 puts the producers at the point where energy enters and sends it "
          "upward, and ENG-1.B.1 makes the continuous inflow what maintains an ecosystem's "
          "structure and function, so reducing the inflow acts on both at once."),

 dict(q="Which statement best captures the relationship the framework draws between energy "
        "and matter in an ecosystem?",
      choices=[
        "Energy must keep arriving from outside, while matter is passed around inside and "
        "conserved.",
        "Matter must keep arriving from outside, while energy is passed around inside and "
        "conserved.",
        "Both energy and matter are created inside the ecosystem as needed.",
        "Both energy and matter are destroyed as they pass through organisms.",
        "Energy and matter are unrelated to one another in an ecosystem."],
      ans=0,
      why="ENG-1.B.1 requires a continuous inflow of high-quality energy from outside, "
          "while ENG-1.B.2 states that each biogeochemical cycle demonstrates the "
          "conservation of matter, so the two quantities behave differently."),
]
