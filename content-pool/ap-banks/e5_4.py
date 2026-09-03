# AP ENVIRONMENTAL SCIENCE 5.4 Impacts of Agricultural Practices
# CED effective Fall 2026, Unit 5 Land and Water Use. (The CED page heading prints
# "Impact of Agricultural Practices"; the title used here is the one in
# ENV_SCI_topics.json, which the exporter matches on.)
# Enduring understanding EIN-2: when humans use natural resources, they alter natural
# systems.
# Learning objective EIN-2.D: describe agricultural practices that cause environmental
# damage.
# Suggested skill 1.A, describe environmental concepts and processes.
#
# Essential knowledge relied on, in the framework's own words:
#   EIN-2.D.1  Agricultural practices that can cause environmental damage include
#              tilling, slash-and-burn farming, and the use of fertilizers.
#
# SCOPE, AND THE HONEST LIMIT OF ONE SENTENCE. EIN-2.D.1 names three practices and says
# they CAN CAUSE environmental damage. It does not say what damage each one causes. So
# an item that asks a student to attach a named harm to a named practice can only be
# keyed by CHAINING to a framework statement that supplies that harm, and where an item
# does that the chain is written out in the claim:
#
#   tilling            -> STB-1.E.1 makes NO-TILL AGRICULTURE one of the soil
#                         conservation methods whose stated goal is to PREVENT SOIL
#                         EROSION. Tilling is what no-till agriculture omits, so the
#                         damage the framework attaches to tilling is soil erosion.
#   slash-and-burn     -> EIN-2.B.2 states that the cutting and burning of trees
#                         releases carbon dioxide and contributes to climate change.
#   use of fertilizers -> STB-3.F.5 names AGRICULTURAL RUNOFF as an anthropogenic cause
#                         of eutrophication, and STB-3.F.1 defines eutrophication as a
#                         body of water becoming enriched in nutrients.
#
# Nothing beyond those three chains is asserted. In particular no key here claims a
# figure for how fast soil is lost, names a region where slash-and-burn is practised, or
# asserts that any of the three practices is always damaging -- the framework's word is
# CAN.
#
# BOUNDARIES. Eutrophication itself is topic 8.5 and the algal bloom and oxygen sequence
# of STB-3.F.2 is not asked here; this topic uses only the runoff-to-nutrient-enrichment
# link. Soil conservation METHODS are STB-1.E.1 in topic 5.15, and are used here only as
# the contrast that identifies tilling. Irrigation is topic 5.5 and pest control is 5.6,
# so neither is offered as a key to "which practice does the framework name here".
#
# NO FIGURES. Every quantitative item carries a table=; all arithmetic is recomputed in
# verify_e5_4.py from that table alone.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("5.4", "Impacts of Agricultural Practices", 5)

_T_TILL = dict(
    headers=["Plot", "Soil lost in one year (tonnes per hectare)",
             "Soil organic matter after ten seasons (percent by mass)"],
    rows=[["Ploughed before every planting", "18", "1.4"],
          ["Left untilled and sown through the residue", "3", "3.2"]])

_T_FERT_RUNOFF = dict(
    headers=["Treatment", "Fertilizer applied (kilograms per hectare)",
             "Nitrate carried off the plot in runoff (kilograms per hectare)"],
    rows=[["No fertilizer applied", "0", "1"],
          ["Light application", "50", "6"],
          ["Standard application", "100", "14"],
          ["Heavy application", "200", "31"]])

_T_LAKE = dict(
    headers=["Sampling point on the stream",
             "Nitrate concentration in the water (milligrams per litre)"],
    rows=[["Upstream of the farmland", "0.4"],
          ["Beside the farmland", "2.6"],
          ["Downstream of the farmland", "4.1"]])

_T_SLASH = dict(
    headers=["Season since the plot was cleared by cutting and burning",
             "Grain harvested from the plot (tonnes per hectare)"],
    rows=[["First season", "2.4"],
          ["Second season", "1.6"],
          ["Third season", "0.9"],
          ["Fourth season", "0.4"]])

_T_CARBON_RELEASE = dict(
    headers=["Way the cleared vegetation was treated",
             "Carbon released to the atmosphere in the first year (tonnes per hectare)"],
    rows=[["Cut and burned on the plot", "55"],
          ["Cut and removed as timber", "12"],
          ["Left standing", "0"]])

_T_SEDIMENT = dict(
    headers=["Field", "Times the field was ploughed in the year",
             "Sediment reaching the stream (tonnes per hectare)"],
    rows=[["Field 1", "0", "2"],
          ["Field 2", "1", "7"],
          ["Field 3", "2", "13"],
          ["Field 4", "4", "24"]])

QUESTIONS = [

 dict(q="Which three agricultural practices does the course framework name as practices "
        "that can cause environmental damage?",
      choices=[
        "Tilling, slash-and-burn farming, and the use of fertilizers",
        "Terracing, contour plowing, and the use of windbreaks",
        "Crop rotation, the addition of green manure, and the addition of limestone",
        "Rotational grazing, free-range grazing, and the use of feedlots",
        "Reforestation, prescribed burning, and the removal of affected trees"],
      ans=0,
      why="EIN-2.D.1 states, near verbatim, that agricultural practices that can cause "
          "environmental damage include tilling, slash-and-burn farming, and the use of "
          "fertilizers. The rejected groups are the soil conservation methods of STB-1.E.1, the "
          "fertility strategies of STB-1.E.2, the meat production methods of EIN-2.H.1, and the "
          "forestry methods of STB-1.G."),

 dict(q="A student writes that the framework says tilling ALWAYS damages the environment. "
        "Which correction is needed?",
      choices=[
        "The framework says these practices CAN cause environmental damage, which is "
        "weaker than saying they always do.",
        "The framework says these practices never cause environmental damage.",
        "The framework does not mention tilling among the practices at all.",
        "The framework says only slash-and-burn farming can cause damage.",
        "The framework says the damage occurs only on farms larger than one "
        "hundred hectares."],
      ans=0,
      why="EIN-2.D.1 uses the words CAN CAUSE, which asserts a possibility rather than an "
          "invariable outcome. Tilling is named in the list, no size threshold appears, and the "
          "statement covers all three practices rather than one."),

 dict(q="Two neighbouring plots of the same soil and crop were managed differently. What do "
        "the tabulated results show?",
      table=_T_TILL,
      choices=[
        "The ploughed plot lost more soil in the year and held less organic matter after "
        "ten seasons than the untilled plot.",
        "The ploughed plot lost less soil in the year and held more organic matter after "
        "ten seasons than the untilled plot.",
        "The two plots lost the same amount of soil but differed in organic matter.",
        "The two plots held the same organic matter but differed in soil lost.",
        "The ploughed plot lost more soil but held more organic matter than the "
        "untilled plot."],
      ans=0,
      why="The ploughed plot reads 18 tonnes per hectare of soil lost against 3, and 1.4 "
          "percent organic matter against 3.2. EIN-2.D.1 names tilling among the practices that "
          "can cause environmental damage, and STB-1.E.1 makes no-till agriculture one of the "
          "soil conservation methods whose stated goal is to prevent soil erosion."),

 dict(q="Using the same two plots, how many times as much soil was lost from the ploughed "
        "plot as from the untilled one in a year?",
      table=_T_TILL,
      choices=[
        "Six times as much",
        "Three times as much",
        "Eighteen times as much",
        "Two times as much",
        "The same amount"],
      ans=0,
      why="Dividing the two tabulated losses gives 18 divided by 3, which is 6. The rejected "
          "values quote one of the two losses as if it were the ratio, use the organic matter "
          "figures, or deny that the two differ."),

 dict(q="Why does the framework's treatment of soil conservation help identify what damage "
        "tilling can do?",
      choices=[
        "No-till agriculture is listed as a soil conservation method, and the stated goal "
        "of soil conservation is to prevent soil erosion.",
        "No-till agriculture is listed as a method of pest control, so tilling must "
        "increase pest damage.",
        "No-till agriculture is listed as a method of irrigation, so tilling must "
        "waste water.",
        "No-till agriculture is listed among the strategies of the Green Revolution, so "
        "tilling must lower yields.",
        "The framework never mentions no-till agriculture, so nothing can be inferred "
        "about tilling."],
      ans=0,
      why="STB-1.E.1 states that the goal of soil conservation is to prevent soil erosion and "
          "lists no-till agriculture among the conservation methods. Tilling is exactly what "
          "no-till agriculture omits, so soil erosion is the damage the framework's own "
          "statements attach to it."),

 dict(q="Four plots received different amounts of fertilizer and the nitrate leaving each "
        "in runoff was measured. What relationship do the values show?",
      table=_T_FERT_RUNOFF,
      choices=[
        "Nitrate carried off the plot rose with every increase in the fertilizer applied.",
        "Nitrate carried off the plot fell with every increase in the fertilizer applied.",
        "Nitrate carried off the plot was the same at every application rate.",
        "Nitrate carried off the plot rose only where no fertilizer at all was applied.",
        "The plot receiving the most fertilizer lost the least nitrate in runoff."],
      ans=0,
      why="Sorted by application rate the runoff figures are 1, 6, 14 and 31 kilograms per "
          "hectare, rising without exception. EIN-2.D.1 names the use of fertilizers among the "
          "practices that can cause environmental damage, and STB-3.F.5 names agricultural "
          "runoff as an anthropogenic cause of eutrophication."),

 dict(q="From the same four plots, how much more nitrate leaves the heavily fertilized plot "
        "than the unfertilized one?",
      table=_T_FERT_RUNOFF,
      choices=[
        "30 kilograms per hectare more",
        "31 kilograms per hectare more",
        "25 kilograms per hectare more",
        "17 kilograms per hectare more",
        "32 kilograms per hectare more"],
      ans=0,
      why="Subtracting the two tabulated runoff figures gives 31 minus 1, which is 30 kilograms "
          "per hectare. The rejected values quote the heavy plot alone, pair the wrong "
          "treatments, or add the two figures instead of differencing them."),

 dict(q="A stream was sampled at three points along its length past a fertilized farm. "
        "Which conclusion is best supported?",
      table=_T_LAKE,
      choices=[
        "Nitrate concentration was higher below the farmland than above it, so the "
        "farmland is a source of nitrate to the stream.",
        "Nitrate concentration was lower below the farmland than above it, so the "
        "farmland removes nitrate from the stream.",
        "Nitrate concentration was the same at all three points, so the farmland has "
        "no effect.",
        "Nitrate concentration was highest upstream of the farmland, so the source lies "
        "above the farm.",
        "Nitrate concentration cannot be compared between points on one stream."],
      ans=0,
      why="The concentrations are 0.4, 2.6 and 4.1 milligrams per litre moving downstream past "
          "the farmland, so the water gains nitrate as it passes. STB-3.F.5 names agricultural "
          "runoff as an anthropogenic cause of eutrophication, and STB-3.F.1 defines "
          "eutrophication as a body of water becoming enriched in nutrients."),

 dict(q="Using the same stream, by how much did the nitrate concentration rise between the "
        "upstream point and the downstream point?",
      table=_T_LAKE,
      choices=[
        "3.7 milligrams per litre",
        "4.1 milligrams per litre",
        "2.2 milligrams per litre",
        "1.5 milligrams per litre",
        "4.5 milligrams per litre"],
      ans=0,
      why="Subtracting gives 4.1 minus 0.4, which is 3.7 milligrams per litre. The rejected "
          "values quote the downstream reading alone, pair the wrong points, or add the two "
          "readings rather than differencing them."),

 dict(q="A plot cleared by cutting and burning was cropped for four seasons without "
        "fertilizer. What does the record of harvests show?",
      table=_T_SLASH,
      choices=[
        "The harvest fell in every season after the first.",
        "The harvest rose in every season after the first.",
        "The harvest was the same in all four seasons.",
        "The harvest fell in the second season and then recovered.",
        "The harvest was largest in the fourth season."],
      ans=0,
      why="The tabulated harvests are 2.4, 1.6, 0.9 and 0.4 tonnes per hectare, falling in "
          "every step. EIN-2.D.1 names slash-and-burn farming among the practices that can "
          "cause environmental damage."),

 dict(q="Using the same record, what fraction of the first season's harvest remained by the "
        "fourth season?",
      table=_T_SLASH,
      choices=[
        "One sixth of it",
        "One half of it",
        "One third of it",
        "Two thirds of it",
        "All of it"],
      ans=0,
      why="Dividing the fourth season by the first gives 0.4 over 2.4, which is one sixth. The "
          "rejected fractions correspond to other pairs of seasons or deny that the harvest "
          "changed at all."),

 dict(q="Three ways of dealing with cleared vegetation were compared for the carbon released "
        "in the first year. Which reading is accurate?",
      table=_T_CARBON_RELEASE,
      choices=[
        "Cutting and burning released the most carbon of the three treatments.",
        "Cutting and burning released the least carbon of the three treatments.",
        "Leaving the vegetation standing released the most carbon of the three.",
        "All three treatments released the same amount of carbon.",
        "Cutting and removing the vegetation as timber released more carbon than "
        "burning it."],
      ans=0,
      why="The tabulated releases are 55, 12 and 0 tonnes per hectare, so burning is the "
          "largest. EIN-2.B.2 states that the cutting and burning of trees releases carbon "
          "dioxide and contributes to climate change, which is the harm EIN-2.D.1's mention of "
          "slash-and-burn farming points to."),

 dict(q="Four fields were ploughed different numbers of times in one year. What do the "
        "sediment measurements show?",
      table=_T_SEDIMENT,
      choices=[
        "Sediment reaching the stream rose with each additional ploughing.",
        "Sediment reaching the stream fell with each additional ploughing.",
        "Sediment reaching the stream was the same from all four fields.",
        "The field ploughed most often delivered the least sediment.",
        "Only the field that was never ploughed delivered sediment to the stream."],
      ans=0,
      why="Sorted by number of ploughings the sediment figures are 2, 7, 13 and 24 tonnes per "
          "hectare, rising without exception. EIN-2.D.1 names tilling among the practices that "
          "can cause environmental damage, and STB-1.E.1 puts preventing soil erosion as the "
          "goal that no-till agriculture serves."),

 dict(q="Using the same four fields, how much more sediment reaches the stream from the "
        "field ploughed four times than from the field never ploughed?",
      table=_T_SEDIMENT,
      choices=[
        "22 tonnes per hectare more",
        "24 tonnes per hectare more",
        "17 tonnes per hectare more",
        "11 tonnes per hectare more",
        "26 tonnes per hectare more"],
      ans=0,
      why="Subtracting gives 24 minus 2, which is 22 tonnes per hectare. The rejected values "
          "quote the most-ploughed field alone, pair the wrong fields, or add the two figures "
          "instead of differencing them."),

 dict(q="Which of the following practices is NOT one the framework names in this topic as "
        "capable of causing environmental damage?",
      choices=[
        "Contour plowing",
        "Tilling",
        "Slash-and-burn farming",
        "The use of fertilizers",
        "None of these, because all four are named in this topic"],
      ans=0,
      why="EIN-2.D.1 names tilling, slash-and-burn farming and the use of fertilizers. Contour "
          "plowing appears instead in STB-1.E.1 as one of the soil conservation methods whose "
          "goal is to prevent soil erosion, which places it on the opposite side of "
          "the framework."),

 dict(q="A farm manager proposes to keep yields but reduce the erosion that ploughing "
        "causes. Which change addresses the practice the framework names?",
      choices=[
        "Sowing the crop through the previous season's residue instead of ploughing "
        "the ground",
        "Applying more fertilizer so that the crop grows faster",
        "Clearing an adjacent woodlot by cutting and burning to add land",
        "Watering the field more often during the growing season",
        "Spraying a broader range of pesticides on the crop"],
      ans=0,
      why="EIN-2.D.1 names tilling as the practice at issue, and STB-1.E.1 lists no-till "
          "agriculture among the soil conservation methods whose goal is to prevent soil "
          "erosion. Each rejected option leaves the ploughing in place and changes some other "
          "input, and two of them add a second practice the framework also names as damaging."),

 dict(q="Why does the framework's list in this topic sit inside a unit about land and "
        "water use?",
      choices=[
        "Each named practice is a way of using land, and the enduring understanding states "
        "that human use of natural resources alters natural systems.",
        "Each named practice is a way of generating electricity from land.",
        "Each named practice occurs only on land that has never been farmed before.",
        "Each named practice is required by law in every farming region.",
        "Each named practice affects the atmosphere and never the land or water."],
      ans=0,
      why="The enduring understanding EIN-2 states that when humans use natural resources they "
          "alter natural systems, and tilling, slash-and-burn farming and fertilizer use are "
          "three ways of using farmland. None of them generates electricity, and the "
          "framework attaches no legal requirement or novelty condition to them."),

 dict(q="Which observation would best show that fertilizer use on a farm is producing the "
        "kind of damage the framework has in view?",
      choices=[
        "Nutrient concentrations in the water leaving the farm are much higher than in "
        "the water entering it.",
        "The crop on the farm grows taller than the crop on a neighbouring farm.",
        "The farm's fuel bill has risen since the fertilizer was first applied.",
        "The number of tractors on the farm has increased over the same period.",
        "The soil on the farm has become easier to plough since the fertilizer "
        "was applied."],
      ans=0,
      why="EIN-2.D.1 names the use of fertilizers as a practice that can cause environmental "
          "damage, and STB-3.F.5 makes agricultural runoff a cause of eutrophication, which "
          "STB-3.F.1 defines as nutrient enrichment of a body of water. Taller crops, fuel "
          "costs and machinery counts measure something else."),

 dict(q="A researcher wants to test whether tilling is responsible for soil loss on a farm. "
        "Which comparison isolates the practice?",
      choices=[
        "Two plots of the same soil, slope and crop, one ploughed before planting and "
        "one not",
        "Two plots on different slopes, both ploughed before planting",
        "Two plots growing different crops, one ploughed and one not",
        "One plot measured in a wet year and the same plot measured in a dry year",
        "Two farms in different regions, one that uses fertilizer and one that does not"],
      ans=0,
      why="A test of one practice must vary that practice and hold everything else fixed, so "
          "soil, slope and crop must match while the ploughing differs. Each rejected "
          "comparison changes a second variable or changes a different practice altogether."),

 dict(q="Which statement about slash-and-burn farming follows from the framework's "
        "statements taken together?",
      choices=[
        "Burning the cleared vegetation releases carbon dioxide, which the framework links "
        "to climate change.",
        "Burning the cleared vegetation removes carbon from the carbon cycle permanently.",
        "Burning the cleared vegetation raises the water table beneath the plot.",
        "Burning the cleared vegetation has no atmospheric effect of any kind.",
        "Burning the cleared vegetation is listed by the framework as a soil "
        "conservation method."],
      ans=0,
      why="EIN-2.D.1 names slash-and-burn farming as a practice that can cause environmental "
          "damage, and EIN-2.B.2 states that the cutting and burning of trees releases carbon "
          "dioxide and contributes to climate change. The framework never treats burning as "
          "removing carbon from the cycle or as a conservation method."),

 dict(q="Two extension officers disagree. The first says the framework identifies three "
        "damaging practices and leaves the specific harms to other statements. The second "
        "says the framework spells out a harm for each of the three in the same sentence. "
        "Which evaluation is correct?",
      choices=[
        "The first officer is correct, because the sentence lists the practices and does "
        "not attach a harm to each one.",
        "The second officer is correct, because the sentence names erosion, carbon release "
        "and nutrient runoff in turn.",
        "Both are correct, because the sentence can be read either way.",
        "Neither is correct, because the sentence names no practices at all.",
        "The second officer is correct, because the sentence names a harm only for "
        "fertilizer use."],
      ans=0,
      why="EIN-2.D.1 reads that agricultural practices that CAN CAUSE environmental damage "
          "include tilling, slash-and-burn farming, and the use of fertilizers, and stops "
          "there. The specific harms come from STB-1.E.1, EIN-2.B.2 and STB-3.F.5, which are "
          "separate statements in other topics."),

 dict(q="Using the fertilizer runoff results, what happens to the share of applied fertilizer "
        "that ends up in runoff as the application rate rises from the light to the "
        "heavy treatment?",
      table=_T_FERT_RUNOFF,
      choices=[
        "It rises, from about one part in eight to about one part in six.",
        "It falls, from about one part in six to about one part in eight.",
        "It stays at exactly one part in ten at every rate.",
        "It falls to zero at the heavy application rate.",
        "It cannot be worked out, because the table gives no application rates."],
      ans=0,
      why="The light treatment loses 6 kilograms of the 50 applied, about one part in eight, "
          "and the heavy treatment loses 31 of the 200 applied, about one part in six, so the "
          "share rises. EIN-2.D.1 names the use of fertilizers among the practices that can "
          "cause environmental damage."),

 dict(q="Which of the following best explains why the framework says these practices CAN "
        "cause damage rather than that they DO cause damage?",
      choices=[
        "Whether damage follows depends on how and where a practice is carried out, so the "
        "framework claims a possibility rather than a certainty.",
        "The framework is uncertain whether the practices exist.",
        "The framework expects each practice to be abandoned within a few years.",
        "The framework treats damage as something that occurs only in laboratories.",
        "The framework means that damage occurs but is always reversed within one season."],
      ans=0,
      why="The word CAN in EIN-2.D.1 makes the statement one about what these practices are "
          "capable of producing. The framework does not doubt that the practices exist, does "
          "not predict their abandonment, and says nothing about damage being reversible."),

 dict(q="A district records rising nitrate in its streams and falling soil depth on its "
        "farmland in the same decade. Which pair of practices named in this topic could "
        "account for the two observations?",
      choices=[
        "The use of fertilizers for the nitrate, and tilling for the loss of soil",
        "Tilling for the nitrate, and the use of fertilizers for the loss of soil",
        "Slash-and-burn farming for the nitrate, and irrigation for the loss of soil",
        "Irrigation for the nitrate, and pest control for the loss of soil",
        "Neither observation can be accounted for by any practice in this topic"],
      ans=0,
      why="STB-3.F.5 makes agricultural runoff a source of nutrient enrichment, which points to "
          "the fertilizer named in EIN-2.D.1, and STB-1.E.1 attaches soil erosion to the "
          "absence of no-till practice, which points to tilling. The rejected pairings swap the "
          "two or substitute practices from topics 5.5 and 5.6."),

 dict(q="What does the comparison between a burned plot and a plot whose vegetation was "
        "removed as timber establish about the burning step in particular?",
      table=_T_CARBON_RELEASE,
      choices=[
        "Burning released several times as much carbon in the first year as removing the "
        "same vegetation as timber.",
        "Burning released less carbon in the first year than removing the same vegetation "
        "as timber.",
        "Burning and removing the vegetation released the same carbon in the first year.",
        "Neither treatment released any carbon in the first year.",
        "Only leaving the vegetation standing released carbon in the first year."],
      ans=0,
      why="The tabulated releases are 55 tonnes per hectare for burning against 12 for removal "
          "as timber and 0 for leaving it standing, so burning is more than four times the "
          "removal case. EIN-2.B.2 attributes the release of carbon dioxide to the cutting AND "
          "BURNING of trees."),

 dict(q="Which single measurement would show most directly whether tilling on a hillside is "
        "producing the damage the framework points to?",
      choices=[
        "The mass of soil leaving the hillside each year",
        "The number of times the field is watered each season",
        "The mass of grain harvested from the hillside each year",
        "The number of workers employed on the farm",
        "The price paid for the farm's produce at market"],
      ans=0,
      why="STB-1.E.1 makes preventing soil erosion the goal of the conservation methods that "
          "include no-till agriculture, so the damage attached to tilling is soil leaving the "
          "field. Watering, yield, employment and price each measure something the framework "
          "does not connect to tilling."),

 dict(q="A field trial shows that a plot loses less soil when it is ploughed less often. "
        "Which framework statement does this result bear on most directly?",
      table=_T_SEDIMENT,
      choices=[
        "The statement that tilling is among the practices that can cause "
        "environmental damage",
        "The statement that mechanization can increase reliance on fossil fuels",
        "The statement that eutrophication occurs when a body of water is enriched "
        "in nutrients",
        "The statement that overgrazing can lead to desertification in arid regions",
        "The statement that a rain shadow is land made drier by higher elevation ground"],
      ans=0,
      why="The tabulated sediment figures fall from 24 to 2 tonnes per hectare as ploughings "
          "fall from four to none, which is a result about tilling. EIN-2.D.1 is the statement "
          "that names tilling; the four rejected statements are EIN-2.C.2, STB-3.F.1, EIN-2.I.5 "
          "and ENG-2.B.2, none of which is about ploughing."),

 dict(q="Which of the following correctly distinguishes the practices named in this topic "
        "from the practices named as soil conservation methods?",
      choices=[
        "This topic names practices that can cause damage, while soil conservation names "
        "practices adopted to prevent soil erosion.",
        "This topic names practices adopted to prevent erosion, while soil conservation "
        "names practices that cause damage.",
        "Both sets name the same practices under different headings.",
        "This topic names practices used only on grazing land, while soil conservation "
        "applies only to cropland.",
        "Neither set of practices appears anywhere else in the framework."],
      ans=0,
      why="EIN-2.D.1 introduces its three practices as ones that CAN CAUSE ENVIRONMENTAL "
          "DAMAGE, while STB-1.E.1 states that the GOAL OF SOIL CONSERVATION IS TO PREVENT SOIL "
          "EROSION and then lists its methods. The two lists share no member, and no-till "
          "agriculture is the direct opposite of one of them."),

 dict(q="Which conclusion about the nitrate readings along the stream is NOT supported by "
        "the data?",
      table=_T_LAKE,
      choices=[
        "The nitrate reaching the stream comes from a source upstream of the farmland.",
        "The nitrate concentration is higher beside the farmland than above it.",
        "The nitrate concentration is higher below the farmland than beside it.",
        "The nitrate concentration rises steadily along the stretch that was sampled.",
        "The water above the farmland contains some nitrate already."],
      ans=0,
      why="The readings are 0.4, 2.6 and 4.1 milligrams per litre from upstream to downstream, "
          "so the concentration is lowest above the farmland and rises past it, which is the "
          "opposite of an upstream source. The other four statements each restate part of that "
          "same sequence correctly."),

 dict(q="Which summary states this topic exactly as the framework does, without adding to it?",
      choices=[
        "Tilling, slash-and-burn farming and the use of fertilizers are agricultural "
        "practices that can cause environmental damage.",
        "Tilling, slash-and-burn farming and the use of fertilizers always destroy the "
        "soil, air and water around a farm.",
        "Tilling, irrigation and pest control are the three practices the framework names "
        "as damaging.",
        "Only the use of fertilizers among common farming practices can cause "
        "environmental damage.",
        "No common agricultural practice causes environmental damage, according to "
        "the framework."],
      ans=0,
      why="EIN-2.D.1 states that agricultural practices that can cause environmental damage "
          "include tilling, slash-and-burn farming, and the use of fertilizers. The rejected "
          "summaries strengthen CAN into always, substitute practices from topics 5.5 and 5.6, "
          "shorten the list, or deny it."),
]
