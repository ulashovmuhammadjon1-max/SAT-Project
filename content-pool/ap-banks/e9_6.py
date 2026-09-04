# AP ENVIRONMENTAL SCIENCE 9.6 Ocean Warming
# CED effective Fall 2026, Unit 9 Global Change.
# Enduring understanding STB-4: Local and regional human activities can have impacts at
# the global level.
# Learning objective STB-4.G: explain the causes and effects of ocean warming. Suggested
# skill 7.A, describe environmental problems.
#
# Essential knowledge relied on, in the framework's own words:
#   STB-4.G.1  Ocean warming is caused by the increase in greenhouse gases in the
#              atmosphere.
#   STB-4.G.2  Ocean warming can affect marine species in a variety of ways, including
#              loss of habitat, and metabolic and reproductive changes.
#   STB-4.G.3  Ocean warming is causing coral bleaching, which occurs when the loss of
#              algae within corals cause the corals to bleach white. Some corals recover
#              and some die.
#
# OCEAN WARMING AND OCEAN ACIDIFICATION ARE DIFFERENT MECHANISMS AND ARE ROUTINELY
# CONFUSED. The framework keeps them apart and so does this module. Warming causes
# BLEACHING, and bleaching is the LOSS OF ALGAE WITHIN THE CORAL (STB-4.G.3).
# Acidification damages coral by making it DIFFICULT TO FORM SHELLS through the loss of
# calcium carbonate (STB-4.H.4), and that belongs to topic 9.7. Item 9 refuses the
# calcium carbonate account of bleaching outright and item 11 states the two mechanisms
# side by side; every anchor on those items carries BOTH clauses -- the process and the
# mechanism -- because a distractor that swaps only the mechanism would otherwise match
# an anchor naming the process alone.
#
# WHAT IS DELIBERATELY NOT ASKED. STB-4.G.1 gives one cause and no chain of steps between
# the atmosphere and the water, so no item asks how the heat gets there. STB-4.G.2 lists
# three ways "in a variety of ways, INCLUDING", so no item treats the three as exhaustive
# -- item 7 keys exactly that. STB-4.G.3 says some corals recover and some die and gives
# no proportion, so no key states how many of either.
#
# NO FIGURES ARE REFERENCED. Every record is supplied as a table.
#
# BOUNDARIES. The greenhouse gases themselves and their potencies are STB-4.C and
# STB-4.D (topic 9.3); the problems an increase in them poses are STB-4.E.1 (topic 9.4);
# rising seas, polar feedback loops and the effects of climate change on ecosystems
# generally are STB-4.F (topic 9.5). No key here uses any of those.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: export_units.py does not typeset
# Environmental Science.
TOPIC = ("9.6", "Ocean Warming", 9)

_T_GHG = dict(
    headers=["Decade of the record",
             "Atmospheric greenhouse gases (carbon dioxide equivalent, parts per million)",
             "Mean temperature of the upper ocean (degrees Celsius)"],
    rows=[["Decade 1", "338", "17.42"],
          ["Decade 2", "356", "17.58"],
          ["Decade 3", "382", "17.79"],
          ["Decade 4", "410", "18.04"]])

_T_SST = dict(
    headers=["Reef", "Mean summer sea surface temperature (degrees Celsius)",
             "Percent of coral colonies bleached white"],
    rows=[["Reef 1", "27.2", "4"],
          ["Reef 2", "28.6", "19"],
          ["Reef 3", "29.8", "48"],
          ["Reef 4", "31.1", "82"]])

_T_FATE = dict(
    headers=["Reef followed after one bleaching event",
             "Percent of the bleached colonies that recovered",
             "Percent of the bleached colonies that died"],
    rows=[["Reef A", "71", "29"],
          ["Reef B", "58", "42"],
          ["Reef C", "34", "66"],
          ["Reef D", "12", "88"]])

_T_ALGAE = dict(
    headers=["Coral colony",
             "Algae remaining within the coral tissue (percent of the original)",
             "Percent of the colony that appears white"],
    rows=[["Colony 1", "94", "5"],
          ["Colony 2", "68", "31"],
          ["Colony 3", "35", "67"],
          ["Colony 4", "8", "93"]])

_T_METABOLIC = dict(
    headers=["Water temperature (degrees Celsius)",
             "Oxygen consumed by one fish (milligrams per hour)",
             "Eggs produced by one female in the season"],
    rows=[["18", "42", "1,800"],
          ["21", "58", "1,450"],
          ["24", "79", "980"],
          ["27", "104", "410"]])

_T_HABITAT = dict(
    headers=["Species", "Warmest water it can occupy (degrees Celsius)",
             "Percent of its former range still cool enough for it"],
    rows=[["Species 1", "22", "18"],
          ["Species 2", "25", "43"],
          ["Species 3", "28", "71"],
          ["Species 4", "31", "94"]])

QUESTIONS = [

 dict(q="What does the framework give as the cause of ocean warming?",
      choices=[
        "The increase in greenhouse gases in the atmosphere.",
        "The decrease in the pH of seawater.",
        "The loss of algae from within corals.",
        "The melting of sea ice at the poles.",
        "The rise in sea level along the continental shelves."],
      ans=0,
      why="STB-4.G.1 states that ocean warming is caused by the increase in greenhouse "
          "gases in the atmosphere. A fall in seawater pH is the subject of a separate "
          "statement about acidification, and the loss of algae is what bleaching is, not "
          "what warms the ocean."),

 dict(q="In which ways does the framework say ocean warming can affect marine species?",
      choices=[
        "Loss of habitat, and metabolic and reproductive changes.",
        "Loss of habitat only, with no change to any body process.",
        "Metabolic changes only, with no loss of habitat.",
        "Reproductive changes only, with no loss of habitat.",
        "A change in the salinity of the water the species occupy."],
      ans=0,
      why="STB-4.G.2 states that ocean warming can affect marine species in a variety of "
          "ways, including loss of habitat, and metabolic and reproductive changes, which "
          "is the set the keyed option names in full."),

 dict(q="A revision card lists four effects on marine species and calls all four framework "
        "effects of ocean warming. Which one is not?",
      choices=[
        "A change in the salinity of the water they occupy.",
        "Loss of habitat.",
        "Metabolic changes.",
        "Reproductive changes.",
        "Changes in the rate at which their bodies use energy."],
      ans=0,
      why="STB-4.G.2 names loss of habitat and metabolic and reproductive changes, which "
          "the four rejected options restate in one wording or another. Salinity appears "
          "nowhere in this topic's statements."),

 dict(q="What does the framework say ocean warming is causing to corals?",
      choices=[
        "Coral bleaching.",
        "Coral reproduction to accelerate.",
        "Corals to grow thicker skeletons.",
        "Corals to move into deeper water.",
        "Corals to take on more algae than before."],
      ans=0,
      why="STB-4.G.3 states that ocean warming is causing coral bleaching, and it "
          "attributes no other change in corals to warming."),

 dict(q="What does the framework say coral bleaching occurs when?",
      choices=[
        "The loss of algae from within the corals causes the corals to bleach white.",
        "The loss of calcium carbonate from the corals makes it difficult for them to form "
        "shells.",
        "The corals take in extra algae and darken as a result.",
        "The corals are buried by sediment washed off the land.",
        "The corals are lifted above the surface by a fall in sea level."],
      ans=0,
      why="STB-4.G.3 states that coral bleaching occurs when the loss of algae within "
          "corals causes the corals to bleach white. The calcium carbonate account belongs "
          "to the framework's separate statement about ocean acidification, which is a "
          "different mechanism from warming."),

 dict(q="What does the framework say about the fate of corals that have bleached?",
      choices=[
        "Some recover and some die.",
        "All of them recover.",
        "All of them die.",
        "None is affected either way.",
        "They recover only if the water becomes more acidic."],
      ans=0,
      why="STB-4.G.3 ends by stating that some corals recover and some die, so the "
          "framework commits to neither outcome for all of them."),

 dict(q="STB-4.G.2 says ocean warming can affect marine species in A VARIETY OF WAYS, "
        "INCLUDING three that it names. What does that wording establish?",
      choices=[
        "The three named ways are examples rather than a complete list.",
        "The three named ways are the only ways that exist.",
        "The three named ways apply to one species only.",
        "The three named ways are ruled out by the framework.",
        "Ocean warming affects marine species in no way at all."],
      ans=0,
      why="The phrase A VARIETY OF WAYS, INCLUDING in STB-4.G.2 marks the three named "
          "effects as instances rather than an exhaustive set, so the framework neither "
          "closes the list nor narrows it to one species."),

 dict(q="A student writes that every coral which bleaches goes on to die. What is the "
        "clearest correction from the framework?",
      choices=[
        "The framework states that some bleached corals recover and some die.",
        "The framework states that every bleached coral recovers.",
        "The framework states that bleaching is not caused by warming at all.",
        "The framework states that bleached corals die only where the water is deep.",
        "The framework gives the exact share of bleached corals that die."],
      ans=0,
      why="STB-4.G.3 states that some corals recover and some die, so the student's claim "
          "closes an outcome the framework leaves open, and the framework supplies no "
          "share for either outcome."),

 dict(q="A student writes that coral bleaching is corals losing their calcium carbonate "
        "and so failing to form shells. What is the clearest correction from the "
        "framework?",
      choices=[
        "Bleaching is the loss of algae within the corals; the difficulty in forming "
        "shells through the loss of calcium carbonate is what the framework attributes to "
        "acidification.",
        "Bleaching is the loss of calcium carbonate; the loss of algae is what the "
        "framework attributes to acidification.",
        "Bleaching and the difficulty in forming shells are the same process under two "
        "names.",
        "Bleaching is caused by a fall in the pH of seawater rather than by warming.",
        "The framework gives no mechanism for bleaching at all."],
      ans=0,
      why="STB-4.G.3 defines bleaching as the loss of algae within corals under ocean "
          "warming, while STB-4.H.4 attributes the difficulty in forming shells, through "
          "the loss of calcium carbonate, to ocean acidification. The two are separate "
          "processes with separate causes in the framework."),

 dict(q="Which of these does the framework NOT claim in this topic?",
      choices=[
        "Ocean warming is caused by a fall in the pH of seawater.",
        "Ocean warming is caused by the increase in greenhouse gases in the atmosphere.",
        "Ocean warming can lead to loss of habitat for marine species.",
        "Ocean warming can lead to metabolic and reproductive changes in marine species.",
        "Ocean warming is causing coral bleaching."],
      ans=0,
      why="STB-4.G.1, STB-4.G.2 and STB-4.G.3 supply the four rejected statements between "
          "them. STB-4.G.1 names the increase in atmospheric greenhouse gases as the "
          "cause, and a fall in pH belongs to the framework's separate account of "
          "acidification."),

 dict(q="How does the framework separate the way ocean warming damages coral from the way "
        "ocean acidification does?",
      choices=[
        "Warming causes bleaching through the loss of algae; acidification makes it "
        "difficult to form shells through the loss of calcium carbonate.",
        "Warming makes it difficult to form shells through the loss of calcium carbonate; "
        "acidification causes bleaching through the loss of algae.",
        "Both damage coral by the same mechanism, so the framework draws no distinction.",
        "Warming damages coral while acidification does not affect it at all.",
        "Acidification damages coral while warming does not affect it at all."],
      ans=0,
      why="STB-4.G.3 attributes bleaching, the loss of algae within corals, to ocean "
          "warming, and STB-4.H.4 attributes the difficulty in forming shells, through the "
          "loss of calcium carbonate, to ocean acidification. Each process has its own "
          "mechanism in the framework."),

 dict(q="A monitoring programme reports that atmospheric greenhouse gases have risen "
        "steadily over fifty years. Which framework statement connects that report to the "
        "ocean?",
      choices=[
        "The one stating that ocean warming is caused by the increase in greenhouse gases "
        "in the atmosphere.",
        "The one stating that bleaching occurs when corals lose the algae within them.",
        "The one stating that some bleached corals recover and some die.",
        "The one stating that warming can bring metabolic changes in marine species.",
        "No statement in this topic connects the atmosphere to the ocean."],
      ans=0,
      why="STB-4.G.1 is the statement that names an atmospheric change as the cause of "
          "ocean warming, and it is the only one in this topic that reaches from the "
          "atmosphere to the water."),

 dict(q="Which observations would test STB-4.G.1's claim most directly?",
      choices=[
        "Records of atmospheric greenhouse gases and of ocean temperature over the same "
        "years.",
        "Records of ocean temperature alone over many years.",
        "Records of atmospheric greenhouse gases alone over many years.",
        "A single measurement of ocean temperature on one day.",
        "Records of the number of coral species present at one reef."],
      ans=0,
      why="STB-4.G.1 asserts a cause running from atmospheric greenhouse gases to ocean "
          "warming, so the evidence bearing on it follows both quantities over the same "
          "period rather than either one alone."),

 dict(q="As the water around them warms, the females of one fish species produce far fewer "
        "eggs each season. Which of the framework's named effects is that?",
      choices=[
        "A reproductive change.",
        "A metabolic change.",
        "A loss of habitat.",
        "A case of coral bleaching.",
        "A change in the salinity of the water."],
      ans=0,
      why="STB-4.G.2 names reproductive changes among the ways ocean warming can affect "
          "marine species, and a fall in the eggs produced each season is a change in "
          "reproduction rather than in habitat or in body chemistry."),

 dict(q="As the water around it warms, one fish uses oxygen and energy at a markedly "
        "higher rate. Which of the framework's named effects is that?",
      choices=[
        "A metabolic change.",
        "A reproductive change.",
        "A loss of habitat.",
        "A case of coral bleaching.",
        "A change in the acidity of the water."],
      ans=0,
      why="STB-4.G.2 names metabolic changes among the ways ocean warming can affect "
          "marine species, and a change in the rate at which an animal uses oxygen and "
          "energy is a change in metabolism."),

 dict(q="A cold water species finds that most of the sea it once occupied is now too warm "
        "for it. Which of the framework's named effects is that?",
      choices=[
        "A loss of habitat.",
        "A metabolic change.",
        "A reproductive change.",
        "A case of coral bleaching.",
        "A rise in the pH of the water."],
      ans=0,
      why="STB-4.G.2 names loss of habitat among the ways ocean warming can affect marine "
          "species, and water that has become too warm to occupy is habitat lost rather "
          "than a change within the animal."),

 dict(q="Atmospheric greenhouse gases and the temperature of the upper ocean were recorded "
        "over four decades. What does the record establish?",
      table=_T_GHG,
      choices=[
        "Both rise at every successive decade.",
        "Both fall at every successive decade.",
        "The greenhouse gases rise while the ocean temperature falls.",
        "The ocean temperature rises while the greenhouse gases fall.",
        "Neither column changes across the four decades."],
      ans=0,
      why="Reading down both columns in decade order, each entry exceeds the one before "
          "it. STB-4.G.1 states that ocean warming is caused by the increase in greenhouse "
          "gases in the atmosphere, and this record follows both quantities together."),

 dict(q="Across those same four decades, by how much did the upper ocean warm?",
      table=_T_GHG,
      choices=[
        "By 0.62 degrees Celsius.",
        "By 0.16 degrees Celsius.",
        "By 0.25 degrees Celsius.",
        "By 1.04 degrees Celsius.",
        "By 18.04 degrees Celsius."],
      ans=0,
      why="The first and last entries in the ocean temperature column are subtracted. "
          "STB-4.G.1 makes that warming the effect whose cause the framework attributes to "
          "the rise in atmospheric greenhouse gases."),

 dict(q="Four reefs were recorded for their summer sea surface temperature and for the "
        "share of colonies bleached white. What does the record establish?",
      table=_T_SST,
      choices=[
        "The warmer the reef, the larger the share of its colonies bleached white.",
        "The warmer the reef, the smaller the share of its colonies bleached white.",
        "Temperature and bleaching are unrelated across these four reefs.",
        "Every reef in the record shows the same share bleached.",
        "The coolest reef shows the largest share bleached."],
      ans=0,
      why="Sorting the reefs by summer sea surface temperature leaves the share bleached "
          "strictly increasing. STB-4.G.3 states that ocean warming is causing coral "
          "bleaching."),

 dict(q="Which of those four reefs carries both the warmest summer water and the largest "
        "share of bleached colonies?",
      table=_T_SST,
      choices=[
        "Reef 4.",
        "Reef 1.",
        "Reef 2.",
        "Reef 3.",
        "No single reef leads on both columns."],
      ans=0,
      why="The largest entry in the temperature column and the largest entry in the "
          "bleaching column fall in the same row. STB-4.G.3 attributes coral bleaching to "
          "ocean warming."),

 dict(q="How much warmer is the summer water of that most bleached reef than of the least "
        "bleached one?",
      table=_T_SST,
      choices=[
        "3.9 degrees Celsius warmer.",
        "1.3 degrees Celsius warmer.",
        "2.5 degrees Celsius warmer.",
        "27.2 degrees Celsius warmer.",
        "78 degrees Celsius warmer."],
      ans=0,
      why="The summer temperatures of the reefs with the largest and smallest bleached "
          "shares are subtracted. STB-4.G.3 ties bleaching to ocean warming, which is what "
          "makes that temperature gap the relevant comparison."),

 dict(q="Four reefs were followed after a bleaching event, with the fate of the bleached "
        "colonies recorded. What does the record establish?",
      table=_T_FATE,
      choices=[
        "At every reef some of the bleached colonies recovered and some died.",
        "At every reef all of the bleached colonies recovered.",
        "At every reef all of the bleached colonies died.",
        "At two of the reefs none of the bleached colonies died.",
        "At two of the reefs none of the bleached colonies recovered."],
      ans=0,
      why="Both columns carry an entry above zero at every reef, and the two shares total "
          "the whole of the bleached colonies. STB-4.G.3 states that some corals recover "
          "and some die."),

 dict(q="Which of those four reefs lost the largest share of its bleached colonies?",
      table=_T_FATE,
      choices=[
        "Reef D.",
        "Reef A.",
        "Reef B.",
        "Reef C.",
        "All four lost the same share."],
      ans=0,
      why="The largest entry in the column recording deaths belongs to one reef alone. "
          "STB-4.G.3 states that some corals recover and some die without giving a share "
          "for either, so the shares have to be read from the record."),

 dict(q="Four coral colonies were recorded for the algae remaining within their tissue and "
        "for how white they appear. What does the record establish?",
      table=_T_ALGAE,
      choices=[
        "The colonies that have lost the most algae are the colonies that appear whitest.",
        "The colonies that have lost the most algae are the colonies that appear least "
        "white.",
        "The algae remaining and the whiteness are unrelated across these colonies.",
        "Every colony in the record retains the same share of its algae.",
        "The colony retaining the most algae appears the whitest."],
      ans=0,
      why="Sorting the colonies by the algae remaining leaves the share appearing white "
          "strictly falling. STB-4.G.3 states that bleaching occurs when the loss of algae "
          "within corals causes the corals to bleach white."),

 dict(q="Which of those four colonies has kept most of its algae and appears least white?",
      table=_T_ALGAE,
      choices=[
        "Colony 1.",
        "Colony 2.",
        "Colony 3.",
        "Colony 4.",
        "No single colony leads on one column and trails on the other."],
      ans=0,
      why="The largest entry in the algae column and the smallest entry in the whiteness "
          "column fall in the same row, which is the pairing STB-4.G.3's account of "
          "bleaching predicts."),

 dict(q="One fish species was held at four water temperatures and measured for oxygen use "
        "and for eggs produced. What does the record establish?",
      table=_T_METABOLIC,
      choices=[
        "As the water warms the fish uses more oxygen and the females produce fewer eggs.",
        "As the water warms the fish uses less oxygen and the females produce more eggs.",
        "As the water warms both the oxygen used and the eggs produced rise.",
        "As the water warms both the oxygen used and the eggs produced fall.",
        "Neither measurement changes with the temperature of the water."],
      ans=0,
      why="Reading down the columns in order of rising temperature, the oxygen used rises "
          "at every step while the eggs produced fall at every step. STB-4.G.2 names both "
          "metabolic and reproductive changes among the effects of ocean warming on marine "
          "species."),

 dict(q="Across the range of temperatures in that same experiment, by how much did the "
        "eggs produced by one female fall?",
      table=_T_METABOLIC,
      choices=[
        "By 1,390 eggs.",
        "By 410 eggs.",
        "By 1,800 eggs.",
        "By 820 eggs.",
        "By 2,210 eggs."],
      ans=0,
      why="The entries at the coolest and warmest temperatures in the egg column are "
          "subtracted. STB-4.G.2 names reproductive changes among the effects of ocean "
          "warming on marine species."),

 dict(q="Four species were recorded for the warmest water they can occupy and for how much "
        "of their former range is still cool enough. What does the record establish?",
      table=_T_HABITAT,
      choices=[
        "The species that can bear the least warmth have kept the least of their former "
        "range.",
        "The species that can bear the least warmth have kept the most of their former "
        "range.",
        "The warmest water a species can bear is unrelated to how much range it has kept.",
        "Every species in the record has kept the same share of its former range.",
        "Every species in the record has kept all of its former range."],
      ans=0,
      why="Sorting the species by the warmest water they can occupy leaves the share of "
          "range still cool enough strictly increasing. STB-4.G.2 names loss of habitat "
          "among the ways ocean warming can affect marine species."),

 dict(q="Which of those four species has kept the smallest share of its former range?",
      table=_T_HABITAT,
      choices=[
        "Species 1, which can bear the least warmth of the four.",
        "Species 4, which can bear the most warmth of the four.",
        "Species 2, which stands second from the bottom on both columns.",
        "Species 3, which stands third on both columns.",
        "All four have kept the same share of their former range."],
      ans=0,
      why="The smallest entry in the range column and the smallest entry in the "
          "temperature tolerance column fall in the same row. STB-4.G.2 names loss of "
          "habitat among the effects of ocean warming on marine species."),

 dict(q="Which single sentence collects what this topic's three statements assert and "
        "nothing further?",
      choices=[
        "Ocean warming is caused by the increase in atmospheric greenhouse gases; it can "
        "affect marine species in a variety of ways, including loss of habitat and "
        "metabolic and reproductive changes; and it is causing coral bleaching, the loss "
        "of algae within corals, after which some corals recover and some die.",
        "Ocean warming is caused by a fall in the pH of seawater; it affects marine "
        "species only through loss of habitat; and it is causing corals to lose their "
        "calcium carbonate, after which all of them die.",
        "Ocean warming has no named cause in the framework, and its only recorded effect "
        "is on corals.",
        "Ocean warming affects marine species in exactly three ways and in no others, and "
        "every bleached coral recovers.",
        "Ocean warming makes it difficult for corals to form shells, while acidification "
        "causes them to lose the algae within them."],
      ans=0,
      why="STB-4.G.1 supplies the cause, STB-4.G.2 the three named kinds of effect within "
          "a variety of ways, and STB-4.G.3 the bleaching, its mechanism in the loss of "
          "algae, and the split outcome afterwards. The calcium carbonate mechanism "
          "belongs to the framework's separate statement on acidification."),
]
