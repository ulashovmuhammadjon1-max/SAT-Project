# AP ENVIRONMENTAL SCIENCE 5.5 Irrigation Methods
# CED effective Fall 2026, Unit 5 Land and Water Use.
# Enduring understanding EIN-2: when humans use natural resources, they alter natural
# systems.
# Learning objectives EIN-2.E, describe different methods of irrigation; EIN-2.F,
# describe the benefits and drawbacks of different methods of irrigation.
# Suggested skill 7.C, describe disadvantages, advantages, or unintended consequences
# for potential solutions.
#
# Essential knowledge relied on, in the framework's own words:
#   EIN-2.E.1  On a global scale, approximately 70% of human freshwater consumption is
#              used for agriculture.
#   EIN-2.E.2  Types of irrigation include drip irrigation, flood irrigation, furrow
#              irrigation, drip irrigation, and spray irrigation. (The CED prints drip
#              twice; the four distinct types are drip, flood, furrow and spray.)
#   EIN-2.F.1  Waterlogging occurs when too much water is left to sit in the soil, which
#              raises the water table of groundwater and inhibits plants' ability to
#              absorb oxygen through their roots.
#   EIN-2.F.2  Furrow irrigation involves cutting furrows between crop rows and filling
#              them with water. This system is inexpensive, but about one third of the
#              water is lost to evaporation and runoff.
#   EIN-2.F.3  Flood irrigation involves flooding an agricultural field with water. This
#              system sees about 20% of the water lost to evaporation and runoff. This
#              can also lead to waterlogging of the soil.
#   EIN-2.F.4  Spray irrigation involves pumping ground water into spray nozzles across
#              an agricultural field. This system is more efficient than flood and furrow
#              irrigation, with only one quarter or less of the water lost to evaporation
#              or runoff. However, spray systems are more expensive than flood and furrow
#              irrigation, and also requires energy to run.
#   EIN-2.F.5  Drip irrigation uses perforated hoses to release small amounts of water to
#              plant roots. This system is the most efficient, with only about 5% of
#              water lost to evaporation and runoff. However, this system is expensive
#              and so is not often used.
#   EIN-2.F.6  Salinization occurs when the salts in groundwater remain in the soil after
#              the water evaporates. Over time, salinization can make soil toxic to
#              plants.
#   EIN-2.F.7  Aquifers can be severely depleted if overused for agricultural irrigation,
#              as has happened to the Ogallala Aquifer in the central United States.
#
# ONE INTERNAL TENSION IN THE CED, RESOLVED THE WAY THE CED ITSELF DIRECTS. EIN-2.F.4
# states plainly that spray irrigation is MORE EFFICIENT THAN FLOOD AND FURROW, and then
# caps its loss at "1/4 or less". EIN-2.F.3 gives flood about 20%. A spray figure of 25%
# would satisfy the cap and contradict the ranking, so the tables here use 15% for spray,
# which satisfies both: it is one quarter or less, and it is below flood's 20%. No item
# asks a student to produce a spray percentage from memory.
#
# ON THE FOUR LOSS PERCENTAGES. These are the framework's own numbers, so a key may rest
# on them. Every item that CALCULATES with them nonetheless prints the percentages in a
# table with the question, so the arithmetic is recoverable from the stimulus alone and
# is recomputed in verify_e5_5.py from that table. All of it is one step and
# calculator-free.
#
# NOTATION. The framework writes 1/3 and 1/4; those are written here as "one third" and
# "one quarter", because export_units.py does not typeset Environmental Science and a
# slash fraction would reach a student as raw text. verify_e5_5.py fails on either shape.
#
# BOUNDARIES. The Green Revolution's LIST of strategies, irrigation among them, is
# EIN-2.C.1 in topic 5.3; the tragedy of the commons account of a shared aquifer is
# EIN-2.A.1 in topic 5.1. Neither is keyed here. This topic is the methods and their
# benefits and drawbacks.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("5.5", "Irrigation Methods", 5)

_T_LOSS = dict(
    headers=["Method of irrigation",
             "Water lost to evaporation and runoff (percent of the water applied)"],
    rows=[["Drip irrigation", "5"],
          ["Flood irrigation", "20"],
          ["Spray irrigation", "15"],
          ["Furrow irrigation", "33"]])

_T_APPLIED = dict(
    headers=["Method of irrigation",
             "Water applied to the field (millimeters)",
             "Water lost to evaporation and runoff (percent of the water applied)"],
    rows=[["Drip irrigation", "600", "5"],
          ["Flood irrigation", "600", "20"],
          ["Spray irrigation", "600", "15"],
          ["Furrow irrigation", "600", "33"]])

_T_SECTORS = dict(
    headers=["Use of fresh water",
             "Share of human freshwater consumption worldwide (percent)"],
    rows=[["Agriculture", "70"],
          ["Industry", "19"],
          ["Households and municipalities", "11"]])

_T_AQUIFER = dict(
    headers=["Year of the record", "Depth to water in the aquifer (meters)",
             "Land irrigated from the aquifer (thousand hectares)"],
    rows=[["Year 1", "30", "400"],
          ["Year 10", "42", "620"],
          ["Year 20", "58", "810"],
          ["Year 30", "76", "900"]])

_T_SALT = dict(
    headers=["Seasons of irrigation with salty groundwater",
             "Salt in the topsoil (grams per kilogram of soil)",
             "Crop yield (tonnes per hectare)"],
    rows=[["None", "1.0", "4.0"],
          ["Five", "3.2", "3.4"],
          ["Ten", "6.5", "2.1"],
          ["Fifteen", "11.0", "0.8"]])

_T_WATERLOG = dict(
    headers=["Field", "Hours per week the field stands under standing water",
             "Depth to the water table beneath the field (meters)",
             "Crop yield (tonnes per hectare)"],
    rows=[["Field A", "0", "3.0", "5.0"],
          ["Field B", "10", "1.2", "4.1"],
          ["Field C", "30", "0.4", "2.6"],
          ["Field D", "60", "0.1", "1.1"]])

_T_INSTALL = dict(
    headers=["Method of irrigation",
             "Cost to install across one hectare (currency units)",
             "Energy needed to run the system for a season (megajoules per hectare)"],
    rows=[["Furrow irrigation", "300", "0"],
          ["Flood irrigation", "400", "0"],
          ["Spray irrigation", "2,100", "1,800"],
          ["Drip irrigation", "4,800", "600"]])

QUESTIONS = [

 dict(q="The table divides human freshwater consumption worldwide among three uses. Which "
        "use takes the largest share, and at what figure?",
      table=_T_SECTORS,
      choices=[
        "Agriculture, at about 70 percent, which is the share the framework gives it",
        "Industry, at about 70 percent, which is the share the framework gives it",
        "Households and municipalities, at about 70 percent, which is the share the "
        "framework gives them",
        "Agriculture, at about 19 percent, which is the share the framework gives it",
        "The three uses take equal shares, so none of them dominates"],
      ans=0,
      why="The tabulated shares are 70, 19 and 11 percent, so agriculture is much the largest "
          "and the three sum to 100. EIN-2.E.1 states that on a global scale, approximately "
          "70 percent of human freshwater consumption is used for agriculture."),

 dict(q="Which set of methods does the framework list as types of irrigation?",
      choices=[
        "Drip, flood, furrow, and spray",
        "Terracing, contour plowing, strip cropping, and windbreaks",
        "Feedlots, rotational grazing, and free-range grazing",
        "Biocontrol, intercropping, crop rotation, and natural predators",
        "Permeable pavement, tree planting, and building up rather than out"],
      ans=0,
      why="EIN-2.E.2 lists drip irrigation, flood irrigation, furrow irrigation and spray "
          "irrigation. The rejected sets are the soil conservation methods of STB-1.E.1, the "
          "meat production methods of EIN-2.H.1, the integrated pest management methods of "
          "STB-1.C.1, and the urban runoff methods of STB-1.B.1."),

 dict(q="What does the framework say waterlogging is?",
      choices=[
        "Too much water left sitting in the soil, which raises the water table and "
        "prevents roots from taking up oxygen",
        "Too little water reaching the soil, which leaves roots unable to take up "
        "nutrients",
        "Salt left behind in the soil when irrigation water evaporates",
        "The loss of irrigation water to evaporation before it reaches the root zone",
        "The compaction of soil beneath the wheels of heavy farm machinery"],
      ans=0,
      why="EIN-2.F.1 states that waterlogging occurs when too much water is left to sit in the "
          "soil, which raises the water table of groundwater and inhibits plants' ability to "
          "absorb oxygen through their roots. Salt left behind after evaporation is "
          "salinization, EIN-2.F.6."),

 dict(q="Which method involves cutting channels between the crop rows and filling them "
        "with water?",
      choices=[
        "Furrow irrigation",
        "Drip irrigation",
        "Spray irrigation",
        "Flood irrigation",
        "None of these, because the framework describes no method of this kind"],
      ans=0,
      why="EIN-2.F.2 states that furrow irrigation involves cutting furrows between crop rows "
          "and filling them with water. Drip uses perforated hoses, spray uses nozzles, and "
          "flooding covers the whole field rather than channels between rows."),

 dict(q="Which method uses perforated hoses to release small amounts of water directly to "
        "plant roots?",
      choices=[
        "Drip irrigation",
        "Furrow irrigation",
        "Spray irrigation",
        "Flood irrigation",
        "All four methods do this equally"],
      ans=0,
      why="EIN-2.F.5 states that drip irrigation uses perforated hoses to release small amounts "
          "of water to plant roots. The other three methods are described in EIN-2.F.2, "
          "EIN-2.F.3 and EIN-2.F.4 by furrows, flooding and spray nozzles."),

 dict(q="The table gives the share of applied water lost to evaporation and runoff under "
        "four methods. Which method is the most efficient, as the framework describes it?",
      table=_T_LOSS,
      choices=[
        "Drip irrigation, which loses the smallest share of the water applied",
        "Furrow irrigation, which loses the smallest share of the water applied",
        "Flood irrigation, which loses the smallest share of the water applied",
        "Spray irrigation, which loses the smallest share of the water applied",
        "All four are equally efficient, since each loses some water"],
      ans=0,
      why="The tabulated losses are 5, 15, 20 and 33 percent, and drip is the smallest. "
          "EIN-2.F.5 states that drip irrigation is the most efficient system, with only about "
          "5 percent of water lost to evaporation and runoff."),

 dict(q="Using the same table of losses, which method loses the largest share of the water "
        "applied to it?",
      table=_T_LOSS,
      choices=[
        "Furrow irrigation, at about one third of the water applied",
        "Flood irrigation, at about one third of the water applied",
        "Spray irrigation, at about one third of the water applied",
        "Drip irrigation, at about one third of the water applied",
        "The four methods lose the same share of the water applied"],
      ans=0,
      why="The tabulated losses are 5, 15, 20 and 33 percent, and 33 percent is furrow "
          "irrigation. EIN-2.F.2 states that about one third of the water is lost to "
          "evaporation and runoff under furrow irrigation."),

 dict(q="A field is given 600 millimeters of water by furrow irrigation. Using the table, "
        "about how much of it is lost to evaporation and runoff?",
      table=_T_APPLIED,
      choices=[
        "About 200 millimeters",
        "About 30 millimeters",
        "About 120 millimeters",
        "About 90 millimeters",
        "About 400 millimeters"],
      ans=0,
      why="A third of 600 millimeters is 200 millimeters, which matches the 33 percent the "
          "table gives for furrow irrigation. The rejected values are the losses the same "
          "table implies for drip, flood and spray, and the water that remains rather than "
          "the water lost."),

 dict(q="The same field is given 600 millimeters of water by drip irrigation instead. Using "
        "the table, about how much is lost to evaporation and runoff?",
      table=_T_APPLIED,
      choices=[
        "About 30 millimeters",
        "About 60 millimeters",
        "About 120 millimeters",
        "About 200 millimeters",
        "About 570 millimeters remaining"],
      ans=0,
      why="Five percent of 600 millimeters is 30 millimeters, which is the figure the table "
          "gives for drip irrigation. The rejected values double the correct answer, quote the "
          "flood and furrow losses, or give the water that remains."),

 dict(q="Using the same applied depths, how much more water is lost under furrow irrigation "
        "than under drip irrigation on this field?",
      table=_T_APPLIED,
      choices=[
        "About 170 millimeters more",
        "About 200 millimeters more",
        "About 30 millimeters more",
        "About 90 millimeters more",
        "About 230 millimeters more"],
      ans=0,
      why="Furrow loses 200 millimeters of the 600 applied and drip loses 30, so the difference "
          "is 170 millimeters. The rejected values quote one of the two losses alone, use the "
          "spray loss, or add the two losses instead of differencing them."),

 dict(q="Which statement correctly reports what the framework says about the cost of "
        "furrow irrigation?",
      choices=[
        "It is inexpensive, and that is the advantage set against its large water loss.",
        "It is the most expensive of the four methods, which is why it is rarely used.",
        "It costs the same as drip irrigation but wastes less water.",
        "The framework makes no statement about the cost of furrow irrigation.",
        "It is inexpensive, and it also loses the least water of the four methods."],
      ans=0,
      why="EIN-2.F.2 states that furrow irrigation is inexpensive, but about one third of the "
          "water is lost to evaporation and runoff, so cheapness is set against the loss. "
          "EIN-2.F.5 reserves the smallest loss for drip irrigation."),

 dict(q="What does the framework say about the efficiency of spray irrigation compared with "
        "flood and furrow?",
      choices=[
        "It is more efficient than both, losing only one quarter or less of the "
        "water applied.",
        "It is less efficient than both, losing more than one third of the water applied.",
        "It is exactly as efficient as flood irrigation and less efficient than furrow.",
        "It is the most efficient of all four methods described.",
        "The framework offers no comparison between spray and the other methods."],
      ans=0,
      why="EIN-2.F.4 states that spray irrigation is more efficient than flood and furrow "
          "irrigation, with only one quarter or less of the water lost. EIN-2.F.5 gives the "
          "most efficient place to drip irrigation instead."),

 dict(q="What drawbacks does the framework attach to spray irrigation?",
      choices=[
        "It is more expensive than flood and furrow irrigation and requires energy to run.",
        "It is cheaper than flood and furrow irrigation but loses more water than either.",
        "It cannot be used on any field larger than one hectare.",
        "It causes salinization but never waterlogging.",
        "It has no drawbacks, according to the framework."],
      ans=0,
      why="EIN-2.F.4 states that spray systems are more expensive than flood and furrow "
          "irrigation and also require energy to run. The framework attaches no field size "
          "limit to the method and does record drawbacks, so the last option is wrong."),

 dict(q="What does the framework give as the reason drip irrigation is not often used, "
        "despite being the most efficient?",
      choices=[
        "It is expensive.",
        "It loses more water than flood irrigation.",
        "It cannot deliver water to plant roots.",
        "It causes waterlogging of the soil.",
        "It requires more energy than any other method."],
      ans=0,
      why="EIN-2.F.5 states that drip irrigation is the most efficient, with only about 5 "
          "percent of water lost, HOWEVER this system is expensive and so is not often used. "
          "The framework attributes waterlogging to flood irrigation in EIN-2.F.3."),

 dict(q="Which method does the framework say can lead to waterlogging of the soil?",
      choices=[
        "Flood irrigation",
        "Drip irrigation",
        "Spray irrigation",
        "Furrow irrigation",
        "None of the four, since waterlogging has no connection to irrigation"],
      ans=0,
      why="EIN-2.F.3 states that flood irrigation involves flooding an agricultural field with "
          "water, sees about 20 percent of the water lost, and can also lead to waterlogging of "
          "the soil. EIN-2.F.1 defines waterlogging as too much water left to sit in the soil."),

 dict(q="What does the framework say salinization is, and what does it do over time?",
      choices=[
        "Salts from groundwater are left in the soil after the water evaporates, and over "
        "time this can make the soil toxic to plants.",
        "Salts are washed out of the soil by irrigation water, and over time this leaves "
        "the soil short of nutrients.",
        "Water sits in the soil and raises the water table, and over time this stops roots "
        "taking up oxygen.",
        "Salts are added deliberately to the soil to control weeds, and over time this "
        "raises yields.",
        "Salt spray from the ocean settles on coastal fields, and over time this "
        "raises yields."],
      ans=0,
      why="EIN-2.F.6 states that salinization occurs when the salts in groundwater remain in "
          "the soil after the water evaporates, and that over time salinization can make soil "
          "toxic to plants. The third option restates waterlogging, EIN-2.F.1."),

 dict(q="Four fields differ in how long they stand under water each week. What do the "
        "values show?",
      table=_T_WATERLOG,
      choices=[
        "The longer a field stands under water, the closer the water table lies to the "
        "surface and the lower the yield.",
        "The longer a field stands under water, the deeper the water table lies and the "
        "higher the yield.",
        "Standing water has no effect on either the water table or the yield in these data.",
        "The field standing under water longest has both the deepest water table and the "
        "highest yield.",
        "The water table depth varies but the yield is the same in all four fields."],
      ans=0,
      why="Standing water runs 0, 10, 30 and 60 hours per week while the depth to the water "
          "table runs 3.0, 1.2, 0.4 and 0.1 meters and the yield runs 5.0, 4.1, 2.6 and 1.1 "
          "tonnes per hectare. EIN-2.F.1 states that waterlogging raises the water table and "
          "inhibits plants' ability to absorb oxygen through their roots."),

 dict(q="Using the same four fields, how much yield is lost between the field that never "
        "stands under water and the field that stands under water longest?",
      table=_T_WATERLOG,
      choices=[
        "3.9 tonnes per hectare",
        "1.1 tonnes per hectare",
        "2.4 tonnes per hectare",
        "0.9 tonnes per hectare",
        "6.1 tonnes per hectare"],
      ans=0,
      why="Subtracting the two tabulated yields gives 5.0 minus 1.1, which is 3.9 tonnes per "
          "hectare. The rejected values quote one yield alone, pair the wrong fields, or add "
          "the two yields instead of differencing them."),

 dict(q="A field has been irrigated with salty groundwater for several seasons. What do the "
        "tabulated results show?",
      table=_T_SALT,
      choices=[
        "Salt in the topsoil rose season after season while the yield fell season "
        "after season.",
        "Salt in the topsoil fell season after season while the yield rose season "
        "after season.",
        "Salt in the topsoil rose while the yield stayed the same throughout.",
        "Salt in the topsoil stayed the same while the yield fell throughout.",
        "Salt in the topsoil and the yield both rose season after season."],
      ans=0,
      why="Salt runs 1.0, 3.2, 6.5 and 11.0 grams per kilogram while the yield runs 4.0, 3.4, "
          "2.1 and 0.8 tonnes per hectare, moving in opposite directions with no reversal. "
          "EIN-2.F.6 states that over time salinization can make soil toxic to plants."),

 dict(q="Using the same record, by how much did the salt in the topsoil rise over "
        "fifteen seasons?",
      table=_T_SALT,
      choices=[
        "10.0 grams per kilogram",
        "11.0 grams per kilogram",
        "7.8 grams per kilogram",
        "4.5 grams per kilogram",
        "12.0 grams per kilogram"],
      ans=0,
      why="Subtracting gives 11.0 minus 1.0, which is 10.0 grams per kilogram. The rejected "
          "values quote the final reading alone, pair the wrong seasons, or add the first and "
          "last readings instead of differencing them."),

 dict(q="An aquifer under a farming region was monitored for thirty years. What do the "
        "values show?",
      table=_T_AQUIFER,
      choices=[
        "As more land was irrigated from the aquifer, the water within it had to be "
        "reached at greater depth.",
        "As more land was irrigated from the aquifer, the water within it rose closer to "
        "the surface.",
        "The area irrigated fell over the period while the water level stayed the same.",
        "The depth to water changed only in the last interval recorded.",
        "The depth to water and the area irrigated are unrelated across this record."],
      ans=0,
      why="The irrigated area rises from 400 to 900 thousand hectares while the depth to water "
          "grows from 30 to 76 meters, both without a reversal. EIN-2.F.7 states that aquifers "
          "can be severely depleted if overused for agricultural irrigation."),

 dict(q="From the same aquifer record, by how many meters did the depth to water increase "
        "over the thirty years?",
      table=_T_AQUIFER,
      choices=[
        "46 meters",
        "76 meters",
        "34 meters",
        "18 meters",
        "106 meters"],
      ans=0,
      why="Subtracting gives 76 minus 30, which is 46 meters. The rejected values quote the "
          "final depth alone, pair the wrong years, or add the first and last readings rather "
          "than differencing them."),

 dict(q="Which aquifer does the framework name as one that has been severely depleted by "
        "overuse for agricultural irrigation?",
      choices=[
        "The Ogallala Aquifer in the central United States",
        "An aquifer beneath the Nile delta",
        "An aquifer beneath the North China Plain",
        "An aquifer beneath the Australian interior",
        "The framework names no aquifer at all"],
      ans=0,
      why="EIN-2.F.7 states that aquifers can be severely depleted if overused for agricultural "
          "irrigation, as has happened to the Ogallala Aquifer in the central United States. "
          "That is the only aquifer the statement names."),

 dict(q="Installation costs and running energy for the four methods are compared in the "
        "table. Which reading matches what the framework says about cost?",
      table=_T_INSTALL,
      choices=[
        "The two cheapest systems to install are furrow and flood, and the most expensive "
        "is drip.",
        "The two cheapest systems to install are spray and drip, and the most expensive "
        "is furrow.",
        "All four systems cost the same to install.",
        "Drip is the cheapest system to install, which is why it is used most widely.",
        "Spray is the cheapest system to install and needs no energy to run."],
      ans=0,
      why="The tabulated installation costs are 300, 400, 2,100 and 4,800 currency units per "
          "hectare, so furrow and flood are cheapest and drip is dearest. EIN-2.F.2 calls "
          "furrow inexpensive, EIN-2.F.4 makes spray more expensive than flood and furrow, and "
          "EIN-2.F.5 calls drip expensive and therefore not often used."),

 dict(q="Using the same installation table, which methods require energy to run, and what "
        "does that match in the framework?",
      table=_T_INSTALL,
      choices=[
        "Spray and drip require energy, which matches the framework's statement that spray "
        "systems require energy to run.",
        "Furrow and flood require energy, which matches the framework's statement that "
        "spray systems require energy to run.",
        "All four methods require the same energy, so the framework's statement does "
        "not apply.",
        "No method requires energy, so the framework's statement is contradicted.",
        "Only furrow requires energy, which matches the framework's statement about "
        "furrow irrigation."],
      ans=0,
      why="The energy column reads 0, 0, 1,800 and 600 megajoules per hectare per season, so "
          "the two pressurised systems need energy and the two gravity-fed ones do not. "
          "EIN-2.F.4 states that spray systems also require energy to run."),

 dict(q="A grower on a small, high-value plot can afford a large capital outlay and wants "
        "the least possible water loss. Which method does the framework's own description "
        "point to, and why?",
      choices=[
        "Drip irrigation, because it is the most efficient, with only about 5 percent of "
        "the water lost, and its drawback is its expense",
        "Furrow irrigation, because it is the most efficient, and its drawback is "
        "its expense",
        "Flood irrigation, because it is the most efficient, and its drawback is "
        "its expense",
        "Spray irrigation, because it is the most efficient of the four described",
        "Any of the four, because the framework reports the same loss for each"],
      ans=0,
      why="EIN-2.F.5 states that drip irrigation is the most efficient, with only about 5 "
          "percent of water lost, however this system is expensive and so is not often used. "
          "The stem removes the expense objection, which leaves the efficiency claim standing."),

 dict(q="Which pair of problems does the framework attach to irrigation practice itself, "
        "rather than to the delivery method a farm chooses?",
      choices=[
        "Salinization of the soil and severe depletion of an aquifer",
        "Soil erosion by ploughing and the release of carbon dioxide by burning",
        "Loss of crop genetic diversity and resistance in pest species",
        "Increased soil temperature and increased stream temperature",
        "Urban sprawl and the spread of impervious surfaces"],
      ans=0,
      why="EIN-2.F.6 attaches salinization to salts left in the soil after irrigation water "
          "evaporates and EIN-2.F.7 attaches severe depletion to aquifers overused for "
          "agricultural irrigation, and neither is tied to one delivery method. The rejected "
          "pairs belong to EIN-2.D.1 and EIN-2.B.2, EIN-2.G, EIN-2.B.1 and EIN-2.M."),

 dict(q="A district irrigating by flooding reports both a rising water table and salt "
        "crusts appearing on the soil surface. Which two framework statements account for "
        "the two reports?",
      choices=[
        "Waterlogging raises the water table, and salinization leaves salts behind when "
        "irrigation water evaporates.",
        "Salinization raises the water table, and waterlogging leaves salts behind when "
        "irrigation water evaporates.",
        "Both reports are explained by the statement that flood irrigation loses about 20 "
        "percent of its water.",
        "Both reports are explained by the statement that drip irrigation is expensive.",
        "Neither report corresponds to any statement in this topic."],
      ans=0,
      why="EIN-2.F.1 makes a raised water table the mark of waterlogging, and EIN-2.F.3 states "
          "that flood irrigation can lead to waterlogging; EIN-2.F.6 makes salt left behind "
          "after evaporation the mark of salinization. The second option swaps the two "
          "definitions."),

 dict(q="Using the four loss percentages, how much water must be applied by furrow "
        "irrigation for 402 millimeters to remain on the field after evaporation "
        "and runoff?",
      table=_T_LOSS,
      choices=[
        "600 millimeters",
        "402 millimeters",
        "536 millimeters",
        "804 millimeters",
        "134 millimeters"],
      ans=0,
      why="Furrow loses 33 percent, so 67 percent of what is applied remains, and 67 percent of "
          "600 millimeters is 402 millimeters. The rejected values assume no loss at all, use "
          "another method's loss, or double the amount that remains."),

 dict(q="Which summary of this topic keeps the framework's ordering of the four methods by "
        "water lost, from least to most?",
      choices=[
        "Drip loses least, then spray, then flood, then furrow loses most.",
        "Furrow loses least, then flood, then spray, then drip loses most.",
        "Spray loses least, then drip, then furrow, then flood loses most.",
        "Flood loses least, then furrow, then drip, then spray loses most.",
        "The four methods lose the same share, so no ordering exists."],
      ans=0,
      why="EIN-2.F.5 gives drip the smallest loss at about 5 percent, EIN-2.F.4 places spray "
          "above flood and furrow in efficiency at one quarter or less, EIN-2.F.3 gives flood "
          "about 20 percent, and EIN-2.F.2 gives furrow about one third. Reading the "
          "framework's own ranking puts drip first, spray second and furrow last."),
]
