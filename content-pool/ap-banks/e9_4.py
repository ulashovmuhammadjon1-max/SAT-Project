# AP ENVIRONMENTAL SCIENCE 9.4 Increases in the Greenhouse Gases
# CED effective Fall 2026, Unit 9 Global Change. Enduring understanding STB-4, local and
# regional human activities can have impacts at the global level. Learning objective
# STB-4.E: identify the threats to human health and the environment posed by an increase
# in greenhouse gases. Suggested skill 2.C, explain how environmental concepts and
# processes represented visually relate to broader environmental issues.
#
# Essential knowledge relied on, in the framework's own words:
#   STB-4.E.1  Global climate change, caused by excess greenhouse gases in the atmosphere,
#              can lead to a variety of environmental problems including rising sea levels
#              resulting from melting ice sheets and ocean water expansion, and disease
#              vectors spreading from the tropics toward the poles. These problems can
#              lead to changes in population dynamics and population movements in
#              response.
#
# THAT SENTENCE IS THE WHOLE OF THIS TOPIC'S CONTENT, and it contains five separable
# claims that the thirty items key and nothing else:
#   (a) the cause is EXCESS greenhouse gases in the atmosphere;
#   (b) the problems are a VARIETY, of which it names some;
#   (c) sea levels rise from TWO stated contributions, melting ice sheets AND the
#       expansion of ocean water;
#   (d) disease vectors spread FROM THE TROPICS TOWARD THE POLES, that direction and no
#       other;
#   (e) these problems can lead to changes in POPULATION DYNAMICS and POPULATION
#       MOVEMENTS in response.
#
# ON SCOPE. Topic 9.3 keys which gases are greenhouse gases and how their potencies
# compare (STB-4.C, STB-4.D); topic 9.5 keys the effects of climate change on ecosystems
# (STB-4.F), including melting permafrost and sea ice and the polar feedback loops; topic
# 9.6 keys ocean warming and topic 9.7 ocean acidification. No key here states any of
# those. Where an item needs the identity of a greenhouse gas it cites STB-4.C.1, and
# says so in verify_e9_4.py.
#
# ON THE FIGURES. Suggested skill 2.C concerns concepts represented visually and the bank
# carries no images, so every representation is a table and every keyed reading, sum,
# difference and percentage is recomputed in verify_e9_4.py from that table alone.
#
# NOT KEYED: no projected sea level, no temperature target, no named country or island,
# no date, and no disease named as spreading. The framework states none of them.
#
# FIVE choices (A-E). No LaTeX and no non-ASCII. Year ranges are written with the word
# "to", never with a hyphen.
TOPIC = ("9.4", "Increases in the Greenhouse Gases", 9)

_T_CONC = dict(
    headers=["Year of the record", "Carbon dioxide (parts per million)",
             "Methane (parts per billion)", "Nitrous oxide (parts per billion)"],
    rows=[["1900", "296", "900", "285"],
          ["1950", "311", "1150", "289"],
          ["2000", "369", "1750", "316"],
          ["2020", "414", "1880", "333"]])

_T_PCT = dict(
    headers=["Greenhouse gas", "Concentration in the earlier record (parts per billion)",
             "Concentration in the later record (parts per billion)"],
    rows=[["Carbon dioxide", "296000", "414000"],
          ["Methane", "900", "1880"],
          ["Nitrous oxide", "285", "333"]])

_T_SEA = dict(
    headers=["Period of the record",
             "Contribution from melting ice sheets (millimeters per year)",
             "Contribution from the expansion of ocean water (millimeters per year)",
             "Total rise in sea level (millimeters per year)"],
    rows=[["Period 1", "0.50", "0.80", "1.3"],
          ["Period 2", "1.1", "1.2", "2.3"],
          ["Period 3", "2.2", "1.6", "3.8"]])

_T_VECTOR = dict(
    headers=["Decade of the survey",
             "Northernmost latitude at which the disease vector was found (degrees)"],
    rows=[["Decade 1", "32"],
          ["Decade 2", "35"],
          ["Decade 3", "39"],
          ["Decade 4", "44"]])

_T_MOVEMENT = dict(
    headers=["Low lying coastal district",
             "Share of the district's land lost to the sea (percent)",
             "People who left the district over the same period"],
    rows=[["District 1", "2.0", "400"],
          ["District 2", "9.0", "3100"],
          ["District 3", "21", "11800"]])

_T_EMISS = dict(
    headers=["Period of the record",
             "Greenhouse gases released each year (billions of tons of carbon dioxide "
             "equivalent)",
             "Carbon dioxide measured in the atmosphere (parts per million)"],
    rows=[["Period 1", "6.0", "325"],
          ["Period 2", "22", "355"],
          ["Period 3", "38", "390"],
          ["Period 4", "50", "415"]])

QUESTIONS = [

 dict(q="What does the framework give as the cause of the global climate change described "
        "in this topic?",
      choices=[
        "Excess greenhouse gases in the atmosphere",
        "A decrease in stratospheric ozone",
        "An increase in ozone near the ground",
        "Untreated sewage entering streams and rivers",
        "A natural cycle unrelated to any gas in the atmosphere"],
      ans=0,
      why="STB-4.E.1 states that global climate change is caused by excess greenhouse gases "
          "in the atmosphere. Stratospheric ozone depletion is STB-4.A.2, ground level "
          "ozone is EIN-3.C.4, and sewage is EIN-3.C.2."),

 dict(q="Which environmental problems does the framework name as ones global climate change "
        "can lead to?",
      choices=[
        "Rising sea levels, and disease vectors spreading from the tropics toward the poles",
        "Falling sea levels, and disease vectors retreating toward the equator",
        "The depletion of stratospheric ozone and an increase in ultraviolet radiation",
        "The eutrophication of lakes and the death of fish from low oxygen",
        "The accumulation of solid waste in landfills and the release of methane from them"],
      ans=0,
      why="STB-4.E.1 names rising sea levels and disease vectors spreading from the tropics "
          "toward the poles among the variety of environmental problems. Ozone depletion, "
          "eutrophication and landfill gas belong to other statements in the course."),

 dict(q="Atmospheric concentrations of three gases were recorded across four years.",
      table=_T_CONC,
      choices=[
        "All three gases rose at every step across the record",
        "All three gases fell at every step across the record",
        "Only one of the three gases rose across the record",
        "The three gases were unchanged across the record",
        "The gases rose at first and then returned to their starting values"],
      ans=0,
      why="Each of the three columns carries a larger value in every later row than in the "
          "row above it. STB-4.C.1 names carbon dioxide, methane and nitrous oxide among "
          "the principal greenhouse gases, and STB-4.E.1 attributes global climate change "
          "to excess greenhouse gases in the atmosphere."),

 dict(q="What two contributions to rising sea levels does the framework name?",
      choices=[
        "Melting ice sheets and the expansion of ocean water",
        "Melting ice sheets and increased rainfall over the ocean",
        "The expansion of ocean water and the sinking of the seafloor",
        "Increased river flow and the melting of sea ice alone",
        "The movement of populations toward the coast"],
      ans=0,
      why="STB-4.E.1 states that rising sea levels result from melting ice sheets and ocean "
          "water expansion. Rainfall, seafloor movement, river flow and human movement are "
          "not given as contributions in that statement."),

 dict(q="In which direction does the framework say disease vectors are spreading?",
      choices=[
        "From the tropics toward the poles",
        "From the poles toward the tropics",
        "From the coasts toward the interior of continents",
        "From high elevations down toward sea level",
        "In no particular direction at all"],
      ans=0,
      why="STB-4.E.1 states that disease vectors are spreading from the tropics toward the "
          "poles. Each rejected option reverses that direction or substitutes a different "
          "axis."),

 dict(q="What further consequences does the framework say these environmental problems can "
        "lead to?",
      choices=[
        "Changes in population dynamics and population movements in response",
        "A permanent increase in the number of species in every ecosystem",
        "The complete recovery of the stratospheric ozone layer",
        "A reduction in the amount of greenhouse gas in the atmosphere",
        "No further consequences of any kind"],
      ans=0,
      why="STB-4.E.1 states that these problems can lead to changes in population dynamics "
          "and population movements in response. The rejected options attribute outcomes "
          "the framework does not."),

 dict(q="Two records of the same three gases are compared. Which gas rose by the largest "
        "percentage?",
      table=_T_PCT,
      choices=[
        "Methane, which rose by more than one hundred percent",
        "Carbon dioxide, which rose by more than one hundred percent",
        "Nitrous oxide, which rose by more than one hundred percent",
        "Carbon dioxide, because its concentration is the largest in both records",
        "All three gases rose by the same percentage"],
      ans=0,
      why="Dividing each gas's increase by its earlier value gives the percentage rise, and "
          "the largest belongs to methane, which more than doubles. The largest "
          "concentration is not the largest percentage change, and STB-4.C.1 names all "
          "three among the principal greenhouse gases."),

 dict(q="Which of the following is NOT among the problems the framework names in this "
        "statement?",
      choices=[
        "An increase in the ultraviolet radiation reaching the Earth's surface",
        "Rising sea levels",
        "Melting ice sheets",
        "The expansion of ocean water",
        "Disease vectors spreading from the tropics toward the poles"],
      ans=0,
      why="STB-4.E.1 names rising sea levels from melting ice sheets and ocean water "
          "expansion, and disease vectors spreading poleward. Increased ultraviolet "
          "radiation belongs to STB-4.A.3, which concerns stratospheric ozone rather than "
          "greenhouse gases."),

 dict(q="Why does the framework list the expansion of ocean water separately from melting "
        "ice sheets as a contribution to rising sea levels?",
      choices=[
        "They are two different contributions to the same rise, one adding water and the "
        "other changing the volume the same water occupies",
        "They are two names for the same process",
        "The expansion of ocean water lowers sea level while melting raises it",
        "Melting ice sheets lower sea level while expansion raises it",
        "Neither contribution actually affects sea level"],
      ans=0,
      why="STB-4.E.1 names both melting ice sheets and ocean water expansion as sources of "
          "the rise, so the framework treats them as two contributions rather than as one "
          "or as offsetting effects."),

 dict(q="A coastal government plans for flooding of low lying land. Which framework "
        "problem does that planning respond to?",
      choices=[
        "Rising sea levels resulting from melting ice sheets and the expansion of ocean "
        "water",
        "Disease vectors spreading from the tropics toward the poles",
        "The depletion of stratospheric ozone by chlorofluorocarbons",
        "The eutrophication of coastal waters by agricultural runoff",
        "The accumulation of solid waste in coastal landfills"],
      ans=0,
      why="STB-4.E.1 names rising sea levels, resulting from melting ice sheets and ocean "
          "water expansion, among the environmental problems global climate change can lead "
          "to. The rejected options belong to other statements."),

 dict(q="Contributions to sea level rise were measured over three periods.",
      table=_T_SEA,
      choices=[
        "Both named contributions grew across the periods, and in each period the two "
        "together account for the whole rise",
        "Only one of the two named contributions grew across the periods",
        "The total rise fell across the three periods",
        "The two contributions together account for less than half of the total rise",
        "Neither contribution changed across the three periods"],
      ans=0,
      why="Both contribution columns rise at every step and in each row the two add to the "
          "total. STB-4.E.1 names melting ice sheets and ocean water expansion as the "
          "sources of the rise in sea level."),

 dict(q="Which of the framework's named problems bears most directly on human health?",
      choices=[
        "Disease vectors spreading from the tropics toward the poles",
        "The expansion of ocean water",
        "The melting of ice sheets",
        "The rise in sea level itself",
        "Changes in population dynamics"],
      ans=0,
      why="STB-4.E.1 names disease vectors spreading from the tropics toward the poles "
          "among the problems, and a vector carries disease to people. The other items in "
          "the statement concern the level of the sea and the movement of populations."),

 dict(q="How do changes in population dynamics differ from population movements in the "
        "framework's statement?",
      choices=[
        "One concerns changes within populations while the other concerns populations "
        "relocating in response",
        "One concerns the sea and the other concerns the atmosphere",
        "They are two names for the same change",
        "One concerns only human populations and the other only animal populations",
        "Neither is mentioned by the framework in this statement"],
      ans=0,
      why="STB-4.E.1 states that these problems can lead to changes in population dynamics "
          "and population movements in response, naming two outcomes rather than one, and "
          "does not restrict either to a particular kind of population."),

 dict(q="Which evidence would best support the framework's claim about the direction "
        "disease vectors are spreading?",
      choices=[
        "Repeated surveys showing the vector's range limit moving away from the tropics "
        "over successive decades",
        "A single survey of where the vector is found today",
        "A count of how many people live within the vector's present range",
        "A record of the price of insect control in one country",
        "A measurement of the sea level at the vector's range limit"],
      ans=0,
      why="STB-4.E.1 asserts a movement from the tropics toward the poles, so repeated "
          "surveys of the range limit over time are what test it. A single survey shows no "
          "movement, and population, price and sea level measure other things."),

 dict(q="Surveys of a disease vector's range limit were made over four decades.",
      table=_T_VECTOR,
      choices=[
        "The vector's range limit moved steadily farther from the equator across the four "
        "decades",
        "The vector's range limit moved steadily closer to the equator",
        "The vector's range limit did not change across the four decades",
        "The vector's range limit moved away from the equator and then back toward it",
        "The vector was found at the same latitude in the first and last decades"],
      ans=0,
      why="The recorded latitude rises at every step across the record, which is movement "
          "away from the equator. STB-4.E.1 states that disease vectors are spreading from "
          "the tropics toward the poles."),

 dict(q="Why does the framework say excess greenhouse gases rather than simply greenhouse "
        "gases?",
      choices=[
        "The gases are present in the atmosphere in any case, and it is the amount beyond "
        "that which the framework connects to global climate change",
        "The framework means that greenhouse gases exist only when they are in excess",
        "The framework means that greenhouse gases are always harmful in any quantity",
        "The framework means that only one greenhouse gas is ever in excess",
        "The framework uses the word to mean that the gases are harmless"],
      ans=0,
      why="STB-4.E.1 attributes global climate change to excess greenhouse gases in the "
          "atmosphere, while STB-4.C.3 states that the greenhouse effect results in the "
          "surface temperature necessary for life, so the framework distinguishes the "
          "presence of the gases from an excess of them."),

 dict(q="Which pairing of a framework problem with its stated mechanism is correct?",
      choices=[
        "Rising sea levels, paired with melting ice sheets and the expansion of ocean water",
        "Rising sea levels, paired with disease vectors moving toward the poles",
        "Disease vectors moving toward the poles, paired with the expansion of ocean water",
        "Population movements, paired with the depletion of stratospheric ozone",
        "Melting ice sheets, paired with an increase in ultraviolet radiation"],
      ans=0,
      why="STB-4.E.1 attributes the rise in sea level to melting ice sheets and ocean water "
          "expansion and names the poleward spread of disease vectors as a separate "
          "problem. Ultraviolet radiation belongs to STB-4.A.3."),

 dict(q="A temperate region records the first local transmission of a disease that had "
        "previously occurred only in the tropics. Which framework statement covers that?",
      choices=[
        "Disease vectors are spreading from the tropics toward the poles as a consequence "
        "of global climate change",
        "Rising sea levels result from melting ice sheets and the expansion of ocean water",
        "Excess greenhouse gases have no consequences for human populations",
        "Population movements occur only in response to sea level rise",
        "Stratospheric ozone depletion increases the ultraviolet radiation at the surface"],
      ans=0,
      why="STB-4.E.1 names disease vectors spreading from the tropics toward the poles "
          "among the problems that global climate change can lead to, which is the arrival "
          "the stem describes."),

 dict(q="Three low lying coastal districts were compared.",
      table=_T_MOVEMENT,
      choices=[
        "The districts that lost the most land also lost the most people",
        "The districts that lost the most land lost the fewest people",
        "The three districts lost the same number of people",
        "No district lost any people over the period",
        "Land lost and people leaving are unrelated across these districts"],
      ans=0,
      why="Ranking the districts by the share of land lost gives the same order as ranking "
          "them by the number of people who left. STB-4.E.1 states that these problems can "
          "lead to changes in population dynamics and population movements in response."),

 dict(q="Which set of measurements would show how much each named contribution adds to a "
        "rise in sea level?",
      choices=[
        "The rise attributable to melting ice sheets and the rise attributable to the "
        "expansion of ocean water, measured separately",
        "The total rise in sea level alone",
        "The concentration of carbon dioxide in the atmosphere alone",
        "The number of people living on the coast",
        "The latitude at which a disease vector is found"],
      ans=0,
      why="STB-4.E.1 names two contributions to the rise, so separating them is what shows "
          "how much each adds. A total alone cannot be divided, and the remaining options "
          "measure other quantities in the statement or outside it."),

 dict(q="Why does the framework describe population movements as occurring in response?",
      choices=[
        "They follow from the environmental problems it lists rather than causing them",
        "They cause the environmental problems it lists",
        "They occur before any environmental problem appears",
        "They are unrelated to the environmental problems it lists",
        "They are the only consequence the framework names"],
      ans=0,
      why="STB-4.E.1 states that these problems can lead to changes in population dynamics "
          "and population movements in response, which places the movements after the "
          "problems in the chain and alongside the changes in dynamics."),

 dict(q="Which observation would most strengthen the claim that a coastline's flooding "
        "comes from the process the framework describes?",
      choices=[
        "Sea level measured along that coast has risen over decades in step with measured "
        "ice sheet loss and ocean warming",
        "The coast has been inhabited for a long time",
        "The coast faces the open ocean rather than a bay",
        "More people live on the coast now than in the past",
        "The coastal district has been renamed since the last survey"],
      ans=0,
      why="STB-4.E.1 attributes rising sea levels to melting ice sheets and the expansion "
          "of ocean water, so a record tying the local rise to those two is what supports "
          "the claim. Settlement history, orientation, population and naming do not."),

 dict(q="Emissions and atmospheric concentration were recorded over four periods.",
      table=_T_EMISS,
      choices=[
        "Both the yearly release of greenhouse gases and the concentration measured in the "
        "atmosphere rose across the periods",
        "The yearly release rose while the concentration measured in the atmosphere fell",
        "Both quantities fell across the periods",
        "The yearly release fell while the concentration rose",
        "Neither quantity changed across the periods"],
      ans=0,
      why="Both columns rise at every step across the record. STB-4.E.1 attributes global "
          "climate change to excess greenhouse gases in the atmosphere, and the two columns "
          "are the release and the resulting amount present."),

 dict(q="What does the framework's phrase about a variety of environmental problems "
        "indicate?",
      choices=[
        "The problems it goes on to name are examples rather than a complete list",
        "Exactly two problems can result and no others",
        "The problems it names are the only ones that can result",
        "No problem can result from excess greenhouse gases",
        "The problems it names are unrelated to greenhouse gases"],
      ans=0,
      why="STB-4.E.1 says that global climate change can lead to a variety of environmental "
          "problems including the ones it then names, and the word including marks them as "
          "examples."),

 dict(q="A low lying island community faces losing habitable land to the sea. Which chain "
        "does the framework's statement describe for that community?",
      choices=[
        "Excess greenhouse gases lead to global climate change, which raises sea levels, "
        "which can lead to population movements in response",
        "Population movements lead to global climate change, which raises sea levels",
        "Rising sea levels lead to excess greenhouse gases, which lead to climate change",
        "Global climate change lowers sea levels, which leads to population movements",
        "Excess greenhouse gases lead directly to population movements with no problem in "
        "between"],
      ans=0,
      why="STB-4.E.1 runs from excess greenhouse gases to global climate change, then to "
          "rising sea levels among other problems, and then to changes in population "
          "dynamics and population movements in response, in that order."),

 dict(q="In the framework's statement, which item is the cause and which is a consequence?",
      choices=[
        "Excess greenhouse gases are the cause and rising sea levels are a consequence",
        "Rising sea levels are the cause and excess greenhouse gases are a consequence",
        "Population movements are the cause and global climate change is a consequence",
        "Disease vectors are the cause and excess greenhouse gases are a consequence",
        "The framework identifies no cause and no consequence"],
      ans=0,
      why="STB-4.E.1 states that global climate change is caused by excess greenhouse gases "
          "in the atmosphere and can lead to problems including rising sea levels, so the "
          "gases stand at the causal end and the sea level rise at the consequence end."),

 dict(q="A student is asked to relate a table of rising greenhouse gas concentrations to a "
        "broader environmental issue. Which connection does the framework support?",
      choices=[
        "Rising concentrations of these gases are the excess the framework connects to "
        "global climate change and the problems that follow from it",
        "Rising concentrations of these gases are the cause of stratospheric ozone "
        "depletion",
        "Rising concentrations of these gases lower the temperature at the surface",
        "Rising concentrations of these gases have no connection to any environmental issue",
        "Rising concentrations of these gases are caused by population movements"],
      ans=0,
      why="STB-4.C.1 identifies the principal greenhouse gases and STB-4.E.1 attributes "
          "global climate change and the problems that follow to excess greenhouse gases in "
          "the atmosphere, which is the connection the task calls for."),

 dict(q="Which outcome does the framework NOT attribute to global climate change in this "
        "statement?",
      choices=[
        "An increase in the cases of skin cancer and cataracts",
        "Rising sea levels",
        "Disease vectors spreading toward the poles",
        "Changes in population dynamics",
        "Population movements in response"],
      ans=0,
      why="STB-4.A.3 attributes skin cancer and cataracts to the increased ultraviolet rays "
          "that follow stratospheric ozone depletion, not to greenhouse gases. The four "
          "rejected options are named in STB-4.E.1."),

 dict(q="Why does the framework name melting ice sheets specifically among the "
        "contributions to rising sea levels?",
      choices=[
        "Water held on land as ice adds to the ocean when it melts, which is one of the two "
        "contributions the statement gives",
        "Melting ice sheets are the only contribution the statement gives",
        "Melting ice sheets reduce the volume of the ocean",
        "Melting ice sheets are named as a consequence of rising sea levels rather than a "
        "cause",
        "Melting ice sheets are named as a cause of disease vectors spreading"],
      ans=0,
      why="STB-4.E.1 states that rising sea levels result from melting ice sheets and ocean "
          "water expansion, so the melting is one of two named contributions rather than "
          "the only one, a reducer of the ocean, or a consequence."),

 dict(q="Which summary best captures this topic?",
      choices=[
        "Excess greenhouse gases cause global climate change, which can lead to a variety "
        "of problems including sea levels rising from melting ice sheets and the expansion "
        "of ocean water and disease vectors spreading from the tropics toward the poles, "
        "and those problems can change population dynamics and drive population movements",
        "Excess greenhouse gases cause stratospheric ozone depletion, which raises "
        "ultraviolet radiation at the surface",
        "Global climate change lowers sea levels and drives disease vectors toward the "
        "equator",
        "The problems the framework names have no effect on human populations",
        "Sea level rise is caused only by increased rainfall over the ocean"],
      ans=0,
      why="Every clause of the keyed summary is part of STB-4.E.1. Each rejected summary "
          "substitutes ozone depletion for climate change, reverses the direction of the "
          "sea level or vector change, denies the population consequences, or replaces the "
          "two named contributions with one the framework does not give."),
]
