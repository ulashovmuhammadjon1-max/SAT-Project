# AP ENVIRONMENTAL SCIENCE 5.2 Clearcutting
# CED effective Fall 2026, Unit 5 Land and Water Use.
# Enduring understanding EIN-2: when humans use natural resources, they alter natural
# systems.
# Learning objective EIN-2.B: describe the effect of clearcutting on forests.
# Suggested skill 1.A, describe environmental concepts and processes.
#
# Essential knowledge relied on, in the framework's own words:
#   EIN-2.B.1  Clearcutting can be economically advantageous but leads to soil erosion,
#              increased soil and stream temperatures, and flooding.
#   EIN-2.B.2  Forests contain trees that absorb pollutants and store carbon dioxide.
#              The cutting and burning of trees releases carbon dioxide and contributes
#              to climate change.
#
# SCOPE. The framework names five consequences and one benefit, and nothing else:
# soil erosion, increased SOIL temperature, increased STREAM temperature, flooding,
# and the release of stored carbon dioxide on cutting and burning, against an economic
# advantage. It does not name a species, a region, a rotation length or a percentage.
# Every key here is one of those six, applied to a described case or read off a table
# printed with the question. Nothing asks a student to recall a measured value.
#
# BOUNDARY WITH 5.17 AND 5.9. Reforestation, sustainably harvested wood, reuse and
# prescribed burning are STB-1.G in topic 5.17 and are NOT offered as keys here; this
# topic is the effect of clearcutting, not its mitigation. Overburden, slag and tailings
# belong to mining, EIN-2.L.1 in topic 5.9.
#
# NO FIGURES. Every quantitative item carries a table=. All arithmetic is a difference,
# a ratio of small whole numbers or a total, and all of it is recomputed in
# verify_e5_2.py from the table alone.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("5.2", "Clearcutting", 5)

_T_WATERSHED = dict(
    headers=["Watershed",
             "Sediment carried out in streamflow (tonnes per square kilometer per year)",
             "Peak streamflow after a heavy storm (cubic meters per second)"],
    rows=[["Left uncut", "12", "4"],
          ["Clearcut two years earlier", "96", "12"]])

_T_TEMP = dict(
    headers=["Site",
             "Mean summer soil temperature near the surface (degrees Celsius)",
             "Mean summer temperature of the stream draining the site (degrees Celsius)"],
    rows=[["Under an intact forest canopy", "14", "12"],
          ["In an adjacent clearcut area", "24", "19"]])

_T_CARBON = dict(
    headers=["Condition of the land", "Carbon stored in living trees (tonnes per hectare)"],
    rows=[["Mature forest", "180"],
          ["Ten years after clearcutting", "45"],
          ["Just after clearcutting and burning", "5"]])

_T_MONEY = dict(
    headers=["Harvest method", "Value of the timber removed (currency units per hectare)",
             "Cost of the operation (currency units per hectare)"],
    rows=[["Clearcutting", "7,000", "900"],
          ["Cutting selected trees only", "1,800", "700"]])

_T_EROSION = dict(
    headers=["Time relative to the harvest",
             "Sediment leaving the watershed (tonnes per square kilometer per year)"],
    rows=[["The year before the harvest", "12"],
          ["One year after the harvest", "88"],
          ["Three years after the harvest", "61"],
          ["Eight years after the harvest", "25"]])

_T_POLLUT = dict(
    headers=["Site",
             "Particulate matter removed from the air by vegetation in one year "
             "(kilograms per hectare)"],
    rows=[["Mature forest", "42"],
          ["Young replanted stand", "15"],
          ["Recently clearcut ground", "2"]])

QUESTIONS = [

 dict(q="Which set of outcomes does the course framework attribute to clearcutting?",
      choices=[
        "Soil erosion, increased soil and stream temperatures, and flooding",
        "Soil erosion, decreased soil and stream temperatures, and drought",
        "Increased soil fertility, cooler streams, and reduced runoff",
        "Increased groundwater salinity, cooler soils, and reduced sediment loads",
        "No measurable change to soil, water or temperature at the harvested site"],
      ans=0,
      why="EIN-2.B.1 states that clearcutting can be economically advantageous but leads to "
          "soil erosion, increased soil and stream temperatures, and flooding. The rejected "
          "options reverse the direction of the temperature and water effects or deny that any "
          "effect occurs."),

 dict(q="According to the framework, what do the trees in a forest do that bears on air "
        "quality and on the atmosphere?",
      choices=[
        "They absorb pollutants and store carbon dioxide",
        "They release pollutants and consume oxygen from the air",
        "They absorb pollutants but release carbon dioxide continuously",
        "They store carbon dioxide but have no effect on any pollutant",
        "They neither absorb pollutants nor store carbon dioxide"],
      ans=0,
      why="EIN-2.B.2 states that forests contain trees that absorb pollutants and store carbon "
          "dioxide. The rejected options drop one of the two functions or reverse the "
          "direction of the exchange."),

 dict(q="What does the framework say happens to the carbon held in a forest when the trees "
        "are cut and burned?",
      choices=[
        "It is released as carbon dioxide, contributing to climate change",
        "It remains locked in the soil indefinitely and never reaches the atmosphere",
        "It is converted into nitrogen compounds that fertilise the remaining ground",
        "It is absorbed by the surrounding streams and carried out to sea",
        "It has no atmospheric effect, because burning removes carbon from the "
        "carbon cycle"],
      ans=0,
      why="EIN-2.B.2 states that the cutting and burning of trees releases carbon dioxide and "
          "contributes to climate change. None of the rejected pathways is named by the "
          "framework, and the last denies the release the statement asserts."),

 dict(q="Two neighbouring watersheds were compared, one left uncut and one clearcut two "
        "years earlier. Which conclusion do the values support?",
      table=_T_WATERSHED,
      choices=[
        "The clearcut watershed lost more sediment and produced a higher storm peak than "
        "the uncut one.",
        "The clearcut watershed lost less sediment and produced a lower storm peak than "
        "the uncut one.",
        "The two watersheds lost the same amount of sediment but differed in storm peak.",
        "The two watersheds produced the same storm peak but differed in sediment loss.",
        "The clearcut watershed lost more sediment but produced a lower storm peak than "
        "the uncut one."],
      ans=0,
      why="The clearcut watershed reads 96 tonnes per square kilometer against 12, and 12 "
          "cubic meters per second against 4, so both figures are higher. EIN-2.B.1 names soil "
          "erosion and flooding among the consequences of clearcutting, and these two "
          "measurements are the field expression of each."),

 dict(q="Using the same two watersheds, how many times as much sediment left the clearcut "
        "watershed as left the uncut one?",
      table=_T_WATERSHED,
      choices=[
        "Eight times as much",
        "Three times as much",
        "Twelve times as much",
        "Ninety-six times as much",
        "The same amount"],
      ans=0,
      why="Dividing the two tabulated figures gives 96 divided by 12, which is 8. The rejected "
          "values come from the storm-peak ratio, from one of the two sediment figures taken "
          "as the ratio, or from denying that the two differ."),

 dict(q="Soil and stream temperatures were measured under an intact canopy and in an "
        "adjacent clearcut area. What do the paired values show?",
      table=_T_TEMP,
      choices=[
        "Both the soil and the stream were warmer in the clearcut area than under "
        "the canopy.",
        "Both the soil and the stream were cooler in the clearcut area than under "
        "the canopy.",
        "The soil was warmer in the clearcut area but the stream was cooler there.",
        "The stream was warmer in the clearcut area but the soil was cooler there.",
        "Neither the soil nor the stream differed between the two sites."],
      ans=0,
      why="The clearcut area reads 24 degrees Celsius in the soil against 14, and 19 degrees "
          "in the stream against 12, so both are higher. EIN-2.B.1 names increased soil AND "
          "stream temperatures together among the effects of clearcutting."),

 dict(q="From the same pair of sites, by how much did the mean summer soil temperature "
        "differ between them?",
      table=_T_TEMP,
      choices=[
        "10 degrees Celsius",
        "7 degrees Celsius",
        "24 degrees Celsius",
        "5 degrees Celsius",
        "38 degrees Celsius"],
      ans=0,
      why="Subtracting the two tabulated soil temperatures gives 24 minus 14, which is 10 "
          "degrees Celsius. The rejected values are the stream difference, one of the two soil "
          "readings alone, or the sum of the pair."),

 dict(q="Carbon stored in living trees was measured on three parcels of the same forest "
        "type. Which reading of the values is accurate?",
      table=_T_CARBON,
      choices=[
        "The parcel just after clearcutting and burning holds the least carbon in living "
        "trees of the three.",
        "The parcel just after clearcutting and burning holds the most carbon in living "
        "trees of the three.",
        "All three parcels hold the same carbon in living trees.",
        "The parcel ten years after clearcutting holds more carbon than the mature forest.",
        "The mature forest holds the least carbon in living trees of the three."],
      ans=0,
      why="The tabulated figures are 180, 45 and 5 tonnes per hectare, so the just-cut and "
          "burned parcel holds the smallest amount. EIN-2.B.2 states that forests store carbon "
          "dioxide and that cutting and burning trees releases it."),

 dict(q="Using the same three parcels, how much of the mature forest's stored carbon per "
        "hectare is no longer held in living trees just after clearcutting and burning?",
      table=_T_CARBON,
      choices=[
        "175 tonnes per hectare",
        "135 tonnes per hectare",
        "180 tonnes per hectare",
        "40 tonnes per hectare",
        "185 tonnes per hectare"],
      ans=0,
      why="Subtracting the two tabulated figures gives 180 minus 5, which is 175 tonnes per "
          "hectare. The rejected values pair the wrong parcels, quote the mature forest total "
          "alone, or add the two figures instead of differencing them."),

 dict(q="A landowner compares two ways of taking timber from one hectare. Using the table, "
        "which method returns more once the cost of the operation is taken off, and what "
        "does that illustrate?",
      table=_T_MONEY,
      choices=[
        "Clearcutting returns more, which illustrates the economic advantage the framework "
        "attributes to it.",
        "Cutting selected trees returns more, which illustrates the economic advantage the "
        "framework attributes to clearcutting.",
        "The two methods return the same amount, so the framework's economic claim does "
        "not apply.",
        "Clearcutting returns less, which contradicts the framework's economic claim.",
        "Neither method returns anything once costs are taken off."],
      ans=0,
      why="Clearcutting returns 7,000 less 900, which is 6,100 currency units per hectare, "
          "against 1,800 less 700, which is 1,100. EIN-2.B.1 opens by saying clearcutting can "
          "be economically advantageous, and this is that advantage in numbers."),

 dict(q="From the same comparison, what is the net return per hectare from clearcutting?",
      table=_T_MONEY,
      choices=[
        "6,100 currency units",
        "1,100 currency units",
        "7,000 currency units",
        "5,200 currency units",
        "7,900 currency units"],
      ans=0,
      why="Taking the cost from the value of the timber gives 7,000 minus 900, which is 6,100 "
          "currency units per hectare. The rejected values are the other method's net return, "
          "the gross value alone, a difference taken between the wrong pair of figures, and "
          "the sum of value and cost."),

 dict(q="Sediment leaving one watershed was recorded before a clearcut and at three times "
        "afterward. What pattern do the values show?",
      table=_T_EROSION,
      choices=[
        "Sediment loss rose sharply after the harvest and then fell back toward, but not "
        "to, its pre-harvest level.",
        "Sediment loss fell sharply after the harvest and then rose back toward its "
        "pre-harvest level.",
        "Sediment loss was unchanged by the harvest at every time recorded.",
        "Sediment loss rose after the harvest and continued rising at every later "
        "measurement.",
        "Sediment loss returned exactly to its pre-harvest level within one year."],
      ans=0,
      why="The record runs 12 tonnes before the harvest, then 88, 61 and 25 afterward, so the "
          "loss rises sevenfold and then declines while remaining above the pre-harvest figure "
          "eight years later. EIN-2.B.1 names soil erosion as an effect of clearcutting."),

 dict(q="Using the same record, how much greater was the sediment loss one year after the "
        "harvest than in the year before it?",
      table=_T_EROSION,
      choices=[
        "76 tonnes per square kilometer per year",
        "88 tonnes per square kilometer per year",
        "49 tonnes per square kilometer per year",
        "13 tonnes per square kilometer per year",
        "100 tonnes per square kilometer per year"],
      ans=0,
      why="Subtracting gives 88 minus 12, which is 76 tonnes per square kilometer per year. "
          "The rejected values quote the post-harvest figure alone, pair the wrong years, or "
          "add the two figures rather than differencing them."),

 dict(q="Particulate matter removed from the air by vegetation was measured at three sites. "
        "Which conclusion follows, using the framework?",
      table=_T_POLLUT,
      choices=[
        "Removing the mature forest removes most of the site's capacity to take pollutants "
        "out of the air.",
        "Removing the mature forest increases the site's capacity to take pollutants out "
        "of the air.",
        "The three sites remove the same amount of particulate matter each year.",
        "Recently clearcut ground removes more particulate matter than a young "
        "replanted stand.",
        "Vegetation has no role in removing particulate matter from the air."],
      ans=0,
      why="The tabulated figures are 42, 15 and 2 kilograms per hectare per year, so the "
          "recently clearcut ground removes about one twentieth of what the mature forest "
          "removes. EIN-2.B.2 states that forests contain trees that absorb pollutants."),

 dict(q="A forester says that clearcutting has only economic consequences and no "
        "environmental ones. How does the framework answer that claim?",
      choices=[
        "It grants the economic advantage and then names soil erosion, warmer soils and "
        "streams, and flooding as consequences.",
        "It denies that clearcutting has any economic advantage at all.",
        "It agrees that the consequences of clearcutting are entirely economic.",
        "It states that the environmental consequences appear only where the trees are "
        "burned rather than removed.",
        "It states that the environmental consequences fall only on the atmosphere and "
        "never on soil or water."],
      ans=0,
      why="EIN-2.B.1 is built as a concession followed by a list: clearcutting CAN BE "
          "economically advantageous BUT leads to soil erosion, increased soil and stream "
          "temperatures, and flooding. The framework therefore grants the benefit and denies "
          "that it is the whole story."),

 dict(q="Why does removing the canopy raise the temperature of the soil beneath it and of "
        "the stream draining it, in the framework's account?",
      choices=[
        "The framework states the increase as a consequence of clearcutting without "
        "attaching a further mechanism to it.",
        "The framework states that cutting trees releases heat stored in their wood.",
        "The framework states that the removal of trees raises the temperature of the "
        "whole atmosphere within a day.",
        "The framework states that warmer soil is what causes trees to be cut down.",
        "The framework denies that soil and stream temperatures change after cutting."],
      ans=0,
      why="EIN-2.B.1 lists increased soil and stream temperatures among the results of "
          "clearcutting and supplies no mechanism, so the defensible answer is the one that "
          "reports the consequence without inventing a cause. The rejected options invent a "
          "mechanism, reverse the causal order, or deny the stated effect."),

 dict(q="Which pair of measurements from a cleared site would together provide the "
        "strongest evidence for two different consequences named in the framework?",
      choices=[
        "Sediment carried out of the watershed each year, and the summer temperature of "
        "the stream that drains it",
        "The market price of timber, and the wages paid to the harvesting crew",
        "The number of tree species present, and the age of the oldest remaining tree",
        "The distance to the nearest road, and the slope of the ground",
        "The depth of the winter snowpack, and the direction of the prevailing wind"],
      ans=0,
      why="EIN-2.B.1 names soil erosion and increased stream temperature as two separate "
          "consequences, and sediment yield and stream temperature are direct measurements of "
          "each. The rejected pairs measure economics, forest composition or site geography "
          "rather than the framework's named effects."),

 dict(q="An analyst argues that because young trees are replanted immediately, clearcutting "
        "has no effect on the carbon held on the site. What does the framework's own "
        "statement establish against that argument?",
      choices=[
        "Cutting and burning trees releases carbon dioxide, so the carbon the standing "
        "trees held has already entered the atmosphere.",
        "Replanting is impossible after a clearcut, so no carbon can be recovered.",
        "Trees do not store carbon dioxide in the first place, so nothing is released.",
        "The carbon released by cutting is immediately re-absorbed by the soil.",
        "Carbon dioxide released by cutting does not contribute to climate change."],
      ans=0,
      why="EIN-2.B.2 states that forests contain trees that store carbon dioxide and that the "
          "cutting and burning of trees releases carbon dioxide and contributes to climate "
          "change, so the release happens whatever is planted afterward. The other options "
          "contradict one half or the other of that statement."),

 dict(q="Which observation would be the clearest single sign of the flooding consequence the "
        "framework names?",
      choices=[
        "A higher peak flow in the stream after the same size of storm than the same "
        "watershed produced before the harvest",
        "A lower peak flow in the stream after the same size of storm than before "
        "the harvest",
        "A rise in the number of days per year with no rain at all",
        "A rise in the average temperature of the soil during the summer",
        "A fall in the amount of sediment leaving the watershed"],
      ans=0,
      why="EIN-2.B.1 names flooding among the consequences of clearcutting, and a larger peak "
          "flow for the same storm is what flooding looks like as a measurement. Soil "
          "temperature and sediment are the framework's other two effects rather than this "
          "one, and the remaining options point the wrong way."),

 dict(q="Which statement correctly describes the relationship between the two essential "
        "knowledge statements in this topic?",
      choices=[
        "One lists the effects of clearcutting on soil and water at the site; the other "
        "adds what the loss of the trees does to air quality and to the atmosphere.",
        "The two statements list the same effects using different words.",
        "One denies that clearcutting has environmental effects and the other affirms it.",
        "One applies only to tropical forests and the other only to temperate forests.",
        "The two statements describe different land uses and cannot be applied to the "
        "same harvest."],
      ans=0,
      why="EIN-2.B.1 gives erosion, warmer soils and streams, and flooding, all at the "
          "harvested site, while EIN-2.B.2 gives pollutant absorption, carbon storage and the "
          "release of carbon dioxide on cutting and burning. The two cover different "
          "consequences of the same act, and the framework attaches neither to a "
          "particular latitude."),

 dict(q="A town downstream of a large clearcut complains of muddier water and warmer water "
        "in the same summer. How does the framework account for both complaints at once?",
      choices=[
        "Both soil erosion and increased stream temperature are listed as consequences of "
        "clearcutting.",
        "Only soil erosion is a listed consequence, so the warmer water must have "
        "another cause.",
        "Only increased stream temperature is a listed consequence, so the muddier water "
        "must have another cause.",
        "Neither is a listed consequence, so the complaints are unrelated to the harvest.",
        "Both complaints are listed consequences of mining rather than of clearcutting."],
      ans=0,
      why="EIN-2.B.1 names soil erosion and increased stream temperatures in the same sentence "
          "as effects of clearcutting, and muddier water and warmer water are those two "
          "effects observed downstream. Mining wastes are EIN-2.L.1 in a different topic."),

 dict(q="Which of the following would count as the economic advantage the framework "
        "concedes to clearcutting?",
      choices=[
        "A larger volume of timber taken from a hectare in one operation, at a lower cost "
        "per unit removed",
        "A larger volume of sediment carried out of the watershed in the first year "
        "after harvest",
        "A larger increase in the summer temperature of the stream draining the site",
        "A larger release of stored carbon dioxide to the atmosphere",
        "A larger peak streamflow after a storm of a given size"],
      ans=0,
      why="EIN-2.B.1 says clearcutting CAN BE economically advantageous and then lists the "
          "harms separately, so the advantage is the yield and cost of the harvest itself. "
          "Each rejected option names one of the harms the same sentence sets against "
          "that advantage."),

 dict(q="Using the sediment record over time, what does the eighth-year figure show about "
        "how long the erosion effect lasts?",
      table=_T_EROSION,
      choices=[
        "Sediment loss was still about twice its pre-harvest level eight years afterward.",
        "Sediment loss had returned exactly to its pre-harvest level eight years afterward.",
        "Sediment loss was still at its peak eight years afterward.",
        "Sediment loss had fallen below its pre-harvest level eight years afterward.",
        "Sediment loss eight years afterward cannot be compared with the pre-harvest "
        "figure."],
      ans=0,
      why="The eighth-year figure is 25 tonnes per square kilometer per year against 12 before "
          "the harvest, which is slightly more than double and well below the peak of 88. "
          "EIN-2.B.1 names soil erosion as a consequence of clearcutting without putting a "
          "limit on how long it persists."),

 dict(q="Two hillsides are identical except that one is clearcut and the other keeps its "
        "trees. Which prediction follows from the framework for the cleared hillside?",
      choices=[
        "More soil will be carried off it, and the stream below it will run warmer.",
        "Less soil will be carried off it, and the stream below it will run cooler.",
        "The same amount of soil will be carried off it, but the stream will run cooler.",
        "More soil will be carried off it, but the stream below it will run cooler.",
        "Neither the soil nor the stream will differ from the wooded hillside."],
      ans=0,
      why="EIN-2.B.1 names soil erosion and increased stream temperature together as "
          "consequences of clearcutting, so both move in the same direction on the cleared "
          "hillside. Every rejected option reverses at least one of the two."),

 dict(q="What role does the framework give forests in the movement of carbon, before any "
        "cutting takes place?",
      choices=[
        "They store carbon dioxide, holding carbon that would otherwise be in "
        "the atmosphere.",
        "They release carbon dioxide steadily, adding to what is in the atmosphere.",
        "They convert carbon dioxide into a mineral that is buried permanently in "
        "the bedrock.",
        "They have no role, since carbon storage happens only in the ocean.",
        "They store carbon only in years when they are not growing."],
      ans=0,
      why="EIN-2.B.2 states that forests contain trees that absorb pollutants and store carbon "
          "dioxide, and that cutting and burning releases it, which places the standing forest "
          "on the storing side. The framework names no mineral pathway and does not reserve "
          "storage to the ocean."),

 dict(q="A regional agency wants one measurement that will show whether a recent clearcut is "
        "producing the erosion effect the framework names. Which should it choose?",
      choices=[
        "The mass of sediment carried out of the watershed in streamflow each year",
        "The number of stems per hectare remaining after the harvest",
        "The market value of the timber that was removed",
        "The mean annual air temperature of the region",
        "The number of vehicles using the logging road each week"],
      ans=0,
      why="Soil erosion is the movement of soil off the site, so the measurement that captures "
          "it is the sediment carried away in the water leaving the watershed. The rejected "
          "measurements record the harvest, the economy or the regional climate rather than "
          "the effect EIN-2.B.1 names."),

 dict(q="Which of the following correctly separates what happens at the harvested site from "
        "what happens beyond it, according to the framework?",
      choices=[
        "Soil erosion and warmer soil occur at the site, while released carbon dioxide "
        "contributes to a change that is not confined to the site.",
        "Soil erosion occurs beyond the site, while released carbon dioxide stays "
        "at the site.",
        "Every effect the framework names is confined to the harvested hectare.",
        "Every effect the framework names occurs only outside the harvested hectare.",
        "The framework does not distinguish effects at all."],
      ans=0,
      why="EIN-2.B.1 places erosion and the temperature increases at the harvested ground and "
          "its stream, while EIN-2.B.2 ends with carbon dioxide contributing to climate change, "
          "which is not a site-scale outcome. The rejected options collapse or invert "
          "that distinction."),

 dict(q="Using the pollutant removal values, how many times as much particulate matter does "
        "a hectare of mature forest remove each year as a hectare of recently "
        "clearcut ground?",
      table=_T_POLLUT,
      choices=[
        "Twenty-one times as much",
        "Three times as much",
        "Forty-two times as much",
        "Seven times as much",
        "Two times as much"],
      ans=0,
      why="Dividing the two tabulated figures gives 42 divided by 2, which is 21. The rejected "
          "values come from the mature forest figure alone, from the young stand comparison, "
          "or from the clearcut figure taken as the ratio."),

 dict(q="A student writes that clearcutting cools the soil because the trees no longer "
        "shelter it. Which correction does the framework require?",
      choices=[
        "The framework states that clearcutting increases soil temperature rather than "
        "lowering it.",
        "The framework states that clearcutting leaves soil temperature unchanged.",
        "The framework states that clearcutting cools the soil but warms the stream.",
        "The framework makes no statement about soil temperature after clearcutting.",
        "The framework states that soil temperature depends only on latitude."],
      ans=0,
      why="EIN-2.B.1 lists INCREASED soil and stream temperatures among the effects of "
          "clearcutting, so the direction in the student's sentence is the wrong one. The "
          "framework does address soil temperature and does not split the two temperature "
          "effects apart."),

 dict(q="Which single sentence best summarises the whole of this topic as the framework "
        "presents it?",
      choices=[
        "Clearcutting pays, but it erodes soil, warms soils and streams, brings flooding, "
        "and releases the carbon dioxide the trees were holding.",
        "Clearcutting pays and has no drawbacks beyond the cost of replanting.",
        "Clearcutting does not pay and has no environmental consequences either.",
        "Clearcutting cools the site and reduces the sediment leaving it, at "
        "considerable cost.",
        "Clearcutting affects only the atmosphere and leaves the site itself unchanged."],
      ans=0,
      why="EIN-2.B.1 concedes the economic advantage and lists erosion, increased soil and "
          "stream temperatures and flooding, and EIN-2.B.2 adds the release of stored carbon "
          "dioxide on cutting and burning. The keyed sentence carries all five items and the "
          "concession; each rejected sentence drops or reverses part of that."),
]
