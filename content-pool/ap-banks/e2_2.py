# AP ENVIRONMENTAL SCIENCE 2.2 Ecosystem Services
# CED effective Fall 2026, Unit 2 The Living World: Biodiversity.
# Enduring understanding ERT-2: ecosystems have structure and diversity that change over
# time.
# Learning objectives ERT-2.B, describe ecosystem services, and ERT-2.C, describe the
# results of human disruptions to ecosystem services. Suggested skill 1.B.
#
# Essential knowledge relied on, in the framework's own words:
#   ERT-2.B.1  There are four categories of ecosystem services: provisioning, regulating,
#              cultural, and supporting.
#   ERT-2.C.1  Anthropogenic activities can disrupt ecosystem services, potentially
#              resulting in economic and ecological consequences.
#
# WHAT THE FRAMEWORK DOES NOT SAY, AND SO IS NOT ASKED. ERT-2.B.1 names the four
# categories and defines none of them. It does not say that pollination is a regulating
# service, that soil formation is a supporting service, or that any one category matters
# more than another. No item here asks a student to sort a named service into one of the
# four categories on the strength of a definition the framework never gives, and in
# particular nothing here turns on the regulating-versus-supporting boundary, which the
# framework supplies no way to draw.
#
# Two items -- 21 and 22 -- do ask which of the four NAMES the framework lists is the one
# whose ordinary English meaning fits a described case. That rests on ERT-2.B.1 for the
# existence and spelling of the four names and on the plain meaning of "provisioning" and
# "cultural" for the match; the claim in verify_e2_2.py says so outright. Both are chosen
# because the ordinary meaning settles them; neither asks about regulating or supporting.
#
# ERT-2.C.1's modal words are load-bearing. It says anthropogenic activities CAN disrupt
# services, POTENTIALLY resulting in economic AND ecological consequences. So no key here
# says a disruption always follows, and no key drops one of the two kinds of consequence.
#
# BOUNDARY WITH 2.5. Natural disruptions to ecosystems are ERT-2.G in topic 2.5. ERT-2.C.1
# is about ANTHROPOGENIC activity, so every disruption keyed here is a human one, and the
# natural cases appear only as rejected options in item 29.
#
# NO FIGURES. Every quantitative item carries a table=, and all of the arithmetic is
# recomputed in verify_e2_2.py from that table alone.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("2.2", "Ecosystem Services", 2)

_T_WETLAND = dict(
    headers=["Stage of the drainage project", "Wetland area remaining (hectares)",
             "Cost of flood damage each year (thousands of dollars)"],
    rows=[["Before drainage", "4000", "200"],
          ["Five years after drainage", "1600", "900"],
          ["Fifteen years after drainage", "300", "2600"]])

_T_POLLINATION = dict(
    headers=["Orchard", "Distance to the nearest natural woodland (kilometres)",
             "Percent of flowers that set fruit"],
    rows=[["Orchard 1", "0.2", "71"],
          ["Orchard 2", "1", "58"],
          ["Orchard 3", "3", "34"],
          ["Orchard 4", "6", "12"]])

_T_MANGROVE = dict(
    headers=["Stretch of coast", "Percent of the mangrove removed before the storm",
             "Cost of property damage from the storm (thousands of dollars)"],
    rows=[["Stretch 1", "0", "40"],
          ["Stretch 2", "25", "150"],
          ["Stretch 3", "60", "520"],
          ["Stretch 4", "95", "1300"]])

_T_CATCHMENT = dict(
    headers=["Catchment", "Forest cover remaining (percent)",
             "Cost of treating the town water supply each year (thousands of dollars)",
             "Fish species recorded in the stream"],
    rows=[["Catchment 1", "90", "30", "22"],
          ["Catchment 2", "60", "90", "17"],
          ["Catchment 3", "30", "240", "9"],
          ["Catchment 4", "5", "610", "3"]])

_T_SOIL = dict(
    headers=["Field", "Years of continuous tillage", "Topsoil depth (centimetres)",
             "Grain harvested (tonnes per hectare)"],
    rows=[["Field 1", "0", "30", "6.0"],
          ["Field 2", "10", "24", "5.2"],
          ["Field 3", "20", "16", "3.9"],
          ["Field 4", "30", "7", "2.1"]])

_T_REEF = dict(
    headers=["Reef site", "Living coral cover (percent)",
             "Visitors booking guided dives each year"],
    rows=[["Site 1", "55", "9000"],
          ["Site 2", "38", "6400"],
          ["Site 3", "20", "3100"],
          ["Site 4", "6", "700"]])

_T_MARGINS = dict(
    headers=["Farming region", "Area of flowering field margins left uncut (hectares)",
             "Wild bee species recorded", "Yield of an insect pollinated crop (tonnes)"],
    rows=[["Region 1", "900", "41", "520"],
          ["Region 2", "640", "33", "470"],
          ["Region 3", "310", "19", "330"],
          ["Region 4", "80", "6", "140"]])

_T_NITROGEN = dict(
    headers=["Condition of the marsh upstream", "Marsh area retained (hectares)",
             "Nitrogen reaching the lake each year (tonnes)"],
    rows=[["Left intact", "1200", "40"],
          ["Half of it cleared", "600", "95"],
          ["All of it cleared", "0", "210"]])

_T_TIMBER = dict(
    headers=["Forest block", "Mature trees left standing (thousands)",
             "Timber harvested from the block each year (cubic metres)"],
    rows=[["Block 1", "400", "9000"],
          ["Block 2", "250", "5600"],
          ["Block 3", "90", "1900"],
          ["Block 4", "20", "400"]])

_T_DUNE = dict(
    headers=["Section of shoreline", "Sand dune volume remaining (percent of the original)",
             "Houses damaged in the same storm"],
    rows=[["Section 1", "100", "2"],
          ["Section 2", "70", "9"],
          ["Section 3", "40", "31"],
          ["Section 4", "10", "88"]])

QUESTIONS = [

 dict(q="Which list gives the categories of ecosystem services that the course framework "
        "names?",
      choices=[
        "Provisioning, regulating, cultural and supporting.",
        "Provisioning, regulating, cultural and economic.",
        "Producing, regulating, recreational and supporting.",
        "Provisioning, purifying, cultural and structural.",
        "Regulating, supporting, aesthetic and monetary."],
      ans=0,
      why="ERT-2.B.1 states that there are four categories of ecosystem services: "
          "provisioning, regulating, cultural, and supporting. Each rejected list swaps at "
          "least one of those four names for a term the framework does not use."),

 dict(q="How many categories of ecosystem services does the framework recognise?",
      choices=["Four", "Two", "Three", "Five", "Nine"],
      ans=0,
      why="ERT-2.B.1 states outright that there are four categories of ecosystem services, "
          "and it then names exactly four of them."),

 dict(q="A revision sheet lists five headings and says all five are framework categories "
        "of ecosystem services. Which heading is not one of them?",
      choices=[
        "Regenerating services",
        "Provisioning services",
        "Regulating services",
        "Cultural services",
        "Supporting services"],
      ans=0,
      why="ERT-2.B.1 names provisioning, regulating, cultural and supporting. Regenerating "
          "is not among the four names the framework gives, so it is the heading the "
          "framework does not recognise."),

 dict(q="A student writes that ecosystem services fall into three categories: "
        "provisioning, regulating and cultural. What is wrong with that answer?",
      choices=[
        "The framework names a fourth category, supporting.",
        "The framework names only two categories, so one of the three is invented.",
        "The framework replaces cultural with economic in its own list.",
        "The framework treats provisioning and regulating as a single category.",
        "The framework gives no categories at all, so any list is wrong."],
      ans=0,
      why="ERT-2.B.1 gives four categories, and the three the student lists are the first "
          "three of them. The one left out is supporting, so the answer is short by exactly "
          "one of the framework's own names."),

 dict(q="What kind of activity does the framework identify as able to disrupt ecosystem "
        "services?",
      choices=[
        "Anthropogenic activities, which are those caused by humans.",
        "Only the activities of invasive species newly arrived in a region.",
        "Only volcanic and seismic activity within the Earth.",
        "Only activities that take place inside protected reserves.",
        "Only the seasonal activity of migrating wildlife."],
      ans=0,
      why="ERT-2.C.1 states that anthropogenic activities can disrupt ecosystem services. "
          "Anthropogenic means human caused, which is the population of activities the "
          "statement is about."),

 dict(q="According to the framework, what may follow when anthropogenic activity disrupts "
        "ecosystem services?",
      choices=[
        "Economic and ecological consequences.",
        "Economic consequences but never ecological ones.",
        "Ecological consequences but never economic ones.",
        "Political and military consequences.",
        "Genetic and evolutionary consequences only."],
      ans=0,
      why="ERT-2.C.1 states that anthropogenic activities can disrupt ecosystem services, "
          "potentially resulting in economic and ecological consequences. The statement "
          "names both kinds together and excludes neither."),

 dict(q="ERT-2.C.1 says anthropogenic activities CAN disrupt ecosystem services, "
        "POTENTIALLY resulting in consequences. What do those two words establish?",
      choices=[
        "That disruption and its consequences are possible outcomes rather than guaranteed "
        "ones.",
        "That disruption follows from every human activity without exception.",
        "That consequences appear only after a fixed number of years.",
        "That the framework is uncertain whether humans affect ecosystems at all.",
        "That only economic consequences are possible, ecological ones being ruled out."],
      ans=0,
      why="ERT-2.C.1 is written with can and potentially, which assert possibility rather "
          "than necessity. A single case in which no consequence was measured therefore "
          "does not contradict the statement, and neither does the statement promise that "
          "every human activity disrupts something."),

 dict(q="A valley marsh was drained in stages. What does the table establish about the "
        "cost of flood damage?",
      table=_T_WETLAND,
      choices=[
        "It rose at every stage while the wetland area fell, which is an economic "
        "consequence.",
        "It fell at every stage while the wetland area fell.",
        "It stayed the same throughout the project.",
        "It rose only after the wetland area had recovered.",
        "It cannot be compared across the stages because the units differ."],
      ans=0,
      why="The wetland area runs 4000, 1600 and 300 hectares while the yearly flood damage "
          "cost runs 200, 900 and 2600 thousands of dollars, so one falls at every stage "
          "and the other rises. ERT-2.C.1 names economic consequences as one of the two "
          "kinds that anthropogenic disruption can bring."),

 dict(q="Using the same drainage record, by roughly what factor did the yearly cost of "
        "flood damage change from before drainage to fifteen years after it?",
      table=_T_WETLAND,
      choices=[
        "It rose about thirteenfold",
        "It rose about fourfold",
        "It fell to about one thirteenth",
        "It rose by about one quarter",
        "It did not change"],
      ans=0,
      why="The cost goes from 200 to 2600 thousands of dollars, and 2600 divided by 200 is "
          "13. ERT-2.C.1 records economic consequences as a possible result of "
          "anthropogenic disruption, and the size of the change is read from the record "
          "rather than assumed."),

 dict(q="Four orchards of the same crop lie at different distances from natural woodland. "
        "What relationship does the table establish?",
      table=_T_POLLINATION,
      choices=[
        "The further an orchard lies from natural woodland, the smaller the percent of its "
        "flowers that set fruit.",
        "The further an orchard lies from natural woodland, the larger the percent of its "
        "flowers that set fruit.",
        "Distance from woodland and fruit set are unrelated across the four orchards.",
        "All four orchards set the same percent of their flowers.",
        "The orchard furthest from woodland set the largest percent of its flowers."],
      ans=0,
      why="Ordered by distance the four orchards set 71, 58, 34 and 12 percent of their "
          "flowers, which falls at every step. ERT-2.B.1 establishes that ecosystems supply "
          "services and ERT-2.C.1 that human land use can disrupt them, and the record here "
          "measures one such service across a gradient of separation."),

 dict(q="Four stretches of the same coast lost different amounts of mangrove before one "
        "storm crossed all of them. What does the table establish?",
      table=_T_MANGROVE,
      choices=[
        "Property damage from the storm was larger where more of the mangrove had been "
        "removed.",
        "Property damage from the storm was larger where less of the mangrove had been "
        "removed.",
        "Property damage was the same on all four stretches.",
        "Property damage was determined only by the strength of the storm, which the record "
        "reports.",
        "The stretch with no mangrove removed suffered the greatest property damage."],
      ans=0,
      why="Ordered by the percent of mangrove removed, the damage runs 40, 150, 520 and "
          "1300 thousands of dollars, rising at every step. ERT-2.C.1 attaches economic "
          "consequences to anthropogenic disruption of ecosystem services, and the storm "
          "was the same event on all four stretches."),

 dict(q="Four catchments differ in how much forest they retain. What do the two right hand "
        "columns of the table establish together?",
      table=_T_CATCHMENT,
      choices=[
        "As forest cover falls, treatment cost rises and stream fish species fall, so the "
        "record carries an economic and an ecological consequence together.",
        "As forest cover falls, treatment cost rises and stream fish species also rise.",
        "As forest cover falls, treatment cost falls and stream fish species rise.",
        "Treatment cost and fish species are unchanged across the four catchments.",
        "Only an economic consequence appears, because fish species were not counted."],
      ans=0,
      why="Ordered from the most forested catchment to the least, treatment cost runs 30, "
          "90, 240 and 610 thousands of dollars while fish species run 22, 17, 9 and 3. "
          "ERT-2.C.1 names economic and ecological consequences together, and one column "
          "here measures each."),

 dict(q="In which of the four catchments is the cost of water treatment highest and the "
        "count of stream fish species lowest?",
      table=_T_CATCHMENT,
      choices=["Catchment 4", "Catchment 1", "Catchment 2", "Catchment 3",
               "No single catchment holds both extremes"],
      ans=0,
      why="The highest treatment cost, 610 thousands of dollars, and the lowest fish "
          "species count, 3, fall in the same row, which is also the row with the least "
          "forest left. ERT-2.C.1 allows the two kinds of consequence to appear together."),

 dict(q="Four fields of the same soil type have been tilled continuously for different "
        "lengths of time. What does the table establish?",
      table=_T_SOIL,
      choices=[
        "Both topsoil depth and grain harvested fall as the years of tillage increase.",
        "Topsoil depth falls while grain harvested rises as the years of tillage increase.",
        "Topsoil depth rises while grain harvested falls as the years of tillage increase.",
        "Neither topsoil depth nor grain harvested changes with the years of tillage.",
        "Grain harvested is highest in the field tilled longest."],
      ans=0,
      why="Ordered by years of tillage, topsoil runs 30, 24, 16 and 7 centimetres and the "
          "harvest runs 6.0, 5.2, 3.9 and 2.1 tonnes per hectare, so both fall. ERT-2.C.1 "
          "records that anthropogenic activity can disrupt ecosystem services with economic "
          "and ecological consequences, and the two columns here move together."),

 dict(q="Four reef sites differ in how much living coral they retain. What does the table "
        "establish about visitors booking guided dives?",
      table=_T_REEF,
      choices=[
        "Fewer visitors book dives where less living coral remains.",
        "More visitors book dives where less living coral remains.",
        "The same number of visitors book dives at every site.",
        "Visitor numbers depend on the size of the reef, which the record gives.",
        "The site with the least coral attracts the most visitors."],
      ans=0,
      why="Ordered by living coral cover the visitor counts run 9000, 6400, 3100 and 700, "
          "falling as the coral falls. ERT-2.B.1 names cultural services among the four "
          "categories and ERT-2.C.1 attaches economic consequences to disruption, and a "
          "paid booking is money changing hands."),

 dict(q="Four farming regions left different areas of flowering field margin uncut. What "
        "does the table establish?",
      table=_T_MARGINS,
      choices=[
        "Both the count of wild bee species and the crop yield fall as the margin area "
        "falls.",
        "The count of wild bee species falls while the crop yield rises as the margin area "
        "falls.",
        "The count of wild bee species rises while the crop yield falls as the margin area "
        "falls.",
        "Neither the bee species count nor the crop yield changes with margin area.",
        "The region with the smallest margin area records the most bee species."],
      ans=0,
      why="Ordered by margin area the bee species run 41, 33, 19 and 6 and the yield runs "
          "520, 470, 330 and 140 tonnes, so both fall together. ERT-2.C.1 names ecological "
          "and economic consequences of anthropogenic disruption side by side."),

 dict(q="Using the same regional record, which column reports an ecological consequence and "
        "which reports an economic one?",
      table=_T_MARGINS,
      choices=[
        "The fall in wild bee species is the ecological consequence and the fall in crop "
        "yield the economic one.",
        "The fall in wild bee species is the economic consequence and the fall in crop yield "
        "the ecological one.",
        "Both columns report ecological consequences and neither reports an economic one.",
        "Both columns report economic consequences and neither reports an ecological one.",
        "Neither column reports a consequence, because only the margin area was managed."],
      ans=0,
      why="A count of species present is a measure of the living system, while a harvest "
          "sold by weight is a measure of production. ERT-2.C.1 pairs ecological with "
          "economic consequences, and the two columns supply one of each for the same set "
          "of regions."),

 dict(q="A marsh upstream of a lake was cleared in two steps. What does the table "
        "establish?",
      table=_T_NITROGEN,
      choices=[
        "Nitrogen reaching the lake rose as the retained marsh area fell.",
        "Nitrogen reaching the lake fell as the retained marsh area fell.",
        "Nitrogen reaching the lake was unchanged by the clearing.",
        "Nitrogen reaching the lake was highest while the marsh was intact.",
        "The record shows nothing, because the lake was not measured before the clearing."],
      ans=0,
      why="The retained marsh runs 1200, 600 and 0 hectares while the nitrogen load runs "
          "40, 95 and 210 tonnes a year, so the load rises as the marsh goes. ERT-2.C.1 "
          "states that anthropogenic activities can disrupt ecosystem services, and the "
          "clearing is such an activity."),

 dict(q="Four blocks of one forest hold different numbers of mature trees. What does the "
        "table establish about the timber taken from them?",
      table=_T_TIMBER,
      choices=[
        "Less timber is taken each year from blocks holding fewer mature trees.",
        "More timber is taken each year from blocks holding fewer mature trees.",
        "The same timber volume is taken from every block.",
        "Timber taken depends only on the age of the trees, which the record gives.",
        "The block with the fewest mature trees yields the most timber."],
      ans=0,
      why="Ordered by mature trees standing, the annual harvest runs 9000, 5600, 1900 and "
          "400 cubic metres, falling with the trees. ERT-2.B.1 names provisioning among the "
          "four categories of ecosystem services, and harvested timber is a good the system "
          "supplies."),

 dict(q="Four sections of one shoreline retain different amounts of their sand dunes. What "
        "does the table establish about the same storm?",
      table=_T_DUNE,
      choices=[
        "More houses were damaged on sections retaining less of their dune volume.",
        "More houses were damaged on sections retaining more of their dune volume.",
        "The same number of houses was damaged on every section.",
        "House damage depended on the number of houses built, which the record gives.",
        "The section with its dunes intact suffered the most damage."],
      ans=0,
      why="Ordered by dune volume remaining, the houses damaged run 2, 9, 31 and 88, rising "
          "as the dunes go. ERT-2.C.1 attaches economic consequences to anthropogenic "
          "disruption of ecosystem services, and the storm was one event across all four "
          "sections."),

 dict(q="Which of the four category names the framework lists is the one whose ordinary "
        "meaning is the supplying of goods that people take from an ecosystem, such as "
        "timber and fish?",
      choices=["Provisioning", "Regulating", "Cultural", "Supporting", "Restoring"],
      ans=0,
      why="ERT-2.B.1 supplies the four names and defines none of them, so the match rests "
          "on the ordinary meaning of the word the framework chose. To provision is to "
          "supply, and one of the five options is not a framework category at all."),

 dict(q="A community values a grove for its ceremonies, its stories and the walking people "
        "do there, rather than for anything harvested from it. Which of the four category "
        "names the framework lists fits that kind of value by its ordinary meaning?",
      choices=["Cultural", "Provisioning", "Regulating", "Supporting", "Commercial"],
      ans=0,
      why="ERT-2.B.1 supplies the four names and defines none of them, so the match rests "
          "on the ordinary meaning of the word the framework chose. Ceremony, story and "
          "recreation are matters of culture, and one of the five options is not a framework "
          "category at all."),

 dict(q="What does the framework say about which of its categories of ecosystem services "
        "matters most?",
      choices=[
        "It names the four categories without ranking them.",
        "It ranks provisioning first because people depend on food and timber.",
        "It ranks supporting first because the other three rest on it.",
        "It ranks cultural last because it cannot be measured in money.",
        "It ranks regulating first because it prevents damage from storms."],
      ans=0,
      why="ERT-2.B.1 states that there are four categories and lists them. It attaches no "
          "order of importance to the four, so any ranking is an addition to the framework "
          "rather than a reading of it."),

 dict(q="A researcher claims that clearing a marsh disrupted an ecosystem service and that "
        "the disruption carried an economic consequence. Which observation would most "
        "directly support the claim?",
      choices=[
        "The cost of treating the town water supply before and after the clearing, together "
        "with the same record for a comparable marsh left intact.",
        "The number of people who said they liked the marsh before it was cleared.",
        "A list of the plant species that grew in the marsh at the time of clearing.",
        "The total area of marsh remaining in the country as a whole.",
        "The cost of the machinery used to carry out the clearing."],
      ans=0,
      why="ERT-2.C.1 links anthropogenic disruption to economic consequences, so the "
          "evidence has to be a cost that changed with the clearing, and a comparable "
          "uncleared marsh is what separates the clearing from whatever else changed over "
          "the same years."),

 dict(q="Which of these outcomes is an ecological consequence rather than an economic one?",
      choices=[
        "The number of fish species living in a stream falls after the catchment is "
        "cleared.",
        "A town pays more each year to treat its drinking water.",
        "Insurance premiums along a stretch of coast rise after a storm.",
        "A fishing port employs fewer people than it did twenty years ago.",
        "A crop is sold for a lower price than in the previous season."],
      ans=0,
      why="ERT-2.C.1 names economic and ecological consequences as two kinds. A count of "
          "species present is a property of the living system, while each rejected option "
          "is a sum of money or a count of jobs."),

 dict(q="Which of these outcomes is an economic consequence rather than an ecological one?",
      choices=[
        "A town pays more each year to treat the water it draws from a cleared catchment.",
        "The number of amphibian species breeding in a pond falls by half.",
        "A wetland plant community is replaced by grasses after drainage.",
        "Fewer wild bees are recorded in a farming region than a decade earlier.",
        "A stream loses the shade that once kept its water cool."],
      ans=0,
      why="ERT-2.C.1 names economic and ecological consequences as two kinds. A recurring "
          "payment is money changing hands, while each rejected option describes a change "
          "in the living system itself."),

 dict(q="A student argues that because one river diversion produced no measurable rise in "
        "costs, ERT-2.C.1 must be wrong. How should that argument be answered?",
      choices=[
        "The statement says consequences potentially follow, so a case with no measured cost "
        "does not contradict it.",
        "The statement says consequences always follow, so the measurement must have been "
        "made incorrectly.",
        "The statement applies only to wetlands, so a river diversion falls outside it.",
        "The statement is about ecological consequences only, so costs are irrelevant to "
        "it.",
        "The statement concerns natural disruptions, so a diversion built by people falls "
        "outside it."],
      ans=0,
      why="ERT-2.C.1 is written with can and potentially, which assert that disruption and "
          "its consequences are possible rather than certain. A single case without a "
          "measured consequence is consistent with a claim of possibility."),

 dict(q="Which of these is an anthropogenic activity of the kind ERT-2.C.1 is about?",
      choices=[
        "Draining a marsh to build houses on it.",
        "A volcanic eruption burying a valley in ash.",
        "A lightning strike starting a fire in an uninhabited range.",
        "A hurricane flattening a stand of coastal forest.",
        "A landslide following heavy rain on a steep slope."],
      ans=0,
      why="Anthropogenic means human caused, and ERT-2.C.1 is a statement about "
          "anthropogenic activities. Each rejected option is a natural event, which the "
          "framework treats separately under natural disruptions to ecosystems."),

 dict(q="Two accounts of the same river basin are offered. Which one stays within what the "
        "framework asserts?",
      choices=[
        "Human activity in the basin can disrupt ecosystem services, and that disruption "
        "may carry consequences both for the economy and for the living system.",
        "Human activity in the basin always destroys ecosystem services, and the "
        "consequences are always economic.",
        "Human activity in the basin can disrupt ecosystem services, but the framework "
        "attaches no consequences to that disruption.",
        "Only natural events can disrupt ecosystem services in the basin, so human activity "
        "is not at issue.",
        "Human activity in the basin can disrupt ecosystem services, and the framework "
        "ranks the ecological consequences above the economic ones."],
      ans=0,
      why="ERT-2.C.1 states that anthropogenic activities can disrupt ecosystem services, "
          "potentially resulting in economic and ecological consequences. Each rejected "
          "account hardens can into always, drops one of the two kinds of consequence, "
          "denies the human role, or adds a ranking the framework does not give."),

 dict(q="Which single sentence collects what the framework asserts across both of this "
        "topic's statements?",
      choices=[
        "There are four categories of ecosystem services, and anthropogenic activities can "
        "disrupt them, potentially with economic and ecological consequences.",
        "There are four categories of ecosystem services, and only natural events disrupt "
        "them, always with economic consequences.",
        "There are two categories of ecosystem services, and anthropogenic activities always "
        "disrupt them.",
        "There are four categories of ecosystem services, and the framework ranks them by "
        "the money each is worth.",
        "There are four categories of ecosystem services, and human activity affects only "
        "the provisioning category."],
      ans=0,
      why="ERT-2.B.1 supplies the count and the four names and ERT-2.C.1 supplies the "
          "anthropogenic cause and the pair of possible consequences. Each rejected summary "
          "changes the count, hardens a possibility into a certainty, removes the human "
          "cause, or adds a ranking or a restriction the framework does not state."),
]
