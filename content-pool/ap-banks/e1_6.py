# AP ENVIRONMENTAL SCIENCE 1.6 The Phosphorus Cycle
# CED effective Fall 2026, Unit 1 The Living World: Ecosystems.
# Enduring understanding ERT-1: Ecosystems are the result of biotic and abiotic
# interactions.
# Learning objective ERT-1.F: explain the steps and reservoir interactions in the
# phosphorus cycle. Suggested skill 2.B.
#
# Essential knowledge relied on, in the framework's own words:
#   ERT-1.F.1  The phosphorus cycle is the movement of atoms and molecules containing the
#              element phosphorus between sources and sinks.
#   ERT-1.F.2  The major reservoirs of phosphorus in the phosphorus cycle are rock and
#              ocean sediments that contain phosphorus-bearing minerals. The phosphorus
#              cycle lacks a significant atmospheric component.
#   ERT-1.F.3  Phosphorus is relatively scarce in ecosystems because rocks weather
#              slowly. As a result, phosphorus is often a limiting nutrient for plants
#              and other producers, particularly in freshwater and some terrestrial
#              ecosystems.
#
# HOW THIS TOPIC IS KEPT DISTINCT FROM 1.4, 1.5 AND 1.7. The bare sources-and-sinks
# definition is asked once in the bank, in 1.4, for carbon; it is NOT re-asked here.
# What is asked here instead is what only phosphorus has: rock and ocean sediments as the
# major reservoirs, the ABSENCE of a significant atmospheric component, slow rock
# weathering as the reason for scarcity, and limitation particularly in FRESHWATER and
# some terrestrial ecosystems. The nitrogen-limitation items in 1.5 turn on the rate of
# fixation and are not repeated. The one cross-cycle comparison here (items 6 and 15) is
# the framework's own: ERT-1.F.2 says this cycle lacks an atmospheric component and
# ERT-1.E.4 says the atmosphere is nitrogen's largest reservoir.
#
# NO FIGURES ARE REFERENCED. Fluxes and stores are given as tables.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: export_units.py does not typeset
# Environmental Science.
TOPIC = ("1.6", "The Phosphorus Cycle", 1)

_T_PRESERVOIR = dict(
    headers=["Phosphorus reservoir", "Phosphorus held (billions of tonnes)"],
    rows=[["Rock containing phosphorus-bearing minerals", "4000000"],
          ["Ocean sediments", "840000"],
          ["Soil", "200"],
          ["Ocean water", "90"],
          ["Living organisms", "3"],
          ["Atmosphere", "0.0003"]])

_T_WEATHER = dict(
    headers=["Rock type in a study plot", "Depth of rock weathered in a century (millimeters)",
             "Phosphorus released to the soil in a century (kilograms per hectare)"],
    rows=[["Rock type 1", "2", "6"],
          ["Rock type 2", "7", "19"],
          ["Rock type 3", "14", "41"],
          ["Rock type 4", "31", "88"]])

_T_LAKEADD = dict(
    headers=["Enclosure in one lake", "Nutrient added",
             "Algal mass after four weeks (grams per cubic meter)"],
    rows=[["Enclosure 1", "Nothing", "2.1"],
          ["Enclosure 2", "Nitrogen", "2.4"],
          ["Enclosure 3", "Phosphorus", "11.7"],
          ["Enclosure 4", "Nitrogen and phosphorus", "12.3"]])

_T_TERRA = dict(
    headers=["Grassland plot", "Phosphorus added (kilograms per hectare)",
             "Plant mass grown (kilograms per hectare)"],
    rows=[["Plot 1", "0", "1400"],
          ["Plot 2", "10", "2050"],
          ["Plot 3", "20", "2600"],
          ["Plot 4", "40", "2900"]])

_T_AGE = dict(
    headers=["Age of the land surface (thousands of years)",
             "Phosphorus available in the soil (milligrams per kilogram)"],
    rows=[["3", "84"],
          ["40", "51"],
          ["300", "22"],
          ["2000", "6"]])

_T_PFLUX = dict(
    headers=["Route by which phosphorus moves",
             "Phosphorus moved each year (millions of tonnes)"],
    rows=[["Weathering of rock into soil and water", "19"],
          ["Rivers carrying phosphorus to the sea", "21"],
          ["Burial in ocean sediments", "18"],
          ["Carried through the air as dust", "1"]])

_T_TWOLAKES = dict(
    headers=["Lake", "Dissolved phosphorus (micrograms per liter)",
             "Algal mass (grams per cubic meter)"],
    rows=[["Lake 1", "4", "1.2"],
          ["Lake 2", "11", "3.6"],
          ["Lake 3", "29", "9.8"],
          ["Lake 4", "62", "18.4"]])

_T_ATMOS = dict(
    headers=["Element", "Share of the dry atmosphere that is this element in gas form"],
    rows=[["Nitrogen", "About 78 parts in 100"],
          ["Phosphorus", "No measurable share"]])

QUESTIONS = [

 dict(q="What does the framework identify as the major reservoirs of phosphorus?",
      choices=[
        "Rock and ocean sediments that contain phosphorus-bearing minerals.",
        "The atmosphere and the bodies of living organisms.",
        "Fresh water in rivers and lakes.",
        "The tissues of soil bacteria and fungi.",
        "Water vapor and cloud droplets."],
      ans=0,
      why="ERT-1.F.2 states that the major reservoirs of phosphorus in the phosphorus "
          "cycle are rock and ocean sediments that contain phosphorus-bearing minerals."),

 dict(q="Which feature does the framework say the phosphorus cycle lacks?",
      choices=[
        "A significant atmospheric component.",
        "Any movement between sources and sinks.",
        "Any reservoir in rock.",
        "Any connection with living organisms.",
        "Any presence in ocean sediments."],
      ans=0,
      why="ERT-1.F.2 states plainly that the phosphorus cycle lacks a significant "
          "atmospheric component. ERT-1.F.1 and the rest of ERT-1.F.2 supply the "
          "movement, the rock reservoir and the sediment reservoir that the other options "
          "wrongly deny."),

 dict(q="According to the framework, why is phosphorus relatively scarce in ecosystems?",
      choices=[
        "Because the rocks that contain it weather slowly.",
        "Because it escapes rapidly into the atmosphere as a gas.",
        "Because living organisms destroy phosphorus atoms as they grow.",
        "Because no reservoir on Earth contains a large amount of phosphorus.",
        "Because it is converted into nitrogen compounds in the soil."],
      ans=0,
      why="ERT-1.F.3 states that phosphorus is relatively scarce in ecosystems because "
          "rocks weather slowly. The scarcity is a matter of the rate at which the store "
          "is opened, not of the size of the store."),

 dict(q="What consequence does the framework draw from the scarcity of phosphorus in "
        "ecosystems?",
      choices=[
        "Phosphorus is often a limiting nutrient for plants and other producers.",
        "Phosphorus is never taken up by living organisms.",
        "Phosphorus accumulates to high concentrations in the atmosphere.",
        "Phosphorus replaces nitrogen in the tissues of producers.",
        "Phosphorus becomes the largest reservoir in the soil."],
      ans=0,
      why="ERT-1.F.3 states that as a result of that scarcity, phosphorus is often a "
          "limiting nutrient for plants and other producers."),

 dict(q="In which kinds of ecosystem does the framework say phosphorus is particularly "
        "likely to be the limiting nutrient?",
      choices=[
        "Freshwater ecosystems and some terrestrial ecosystems.",
        "Deep ocean ecosystems only.",
        "The upper atmosphere only.",
        "Ecosystems that contain no producers.",
        "Ecosystems in which nitrogen is already abundant in rock."],
      ans=0,
      why="ERT-1.F.3 states that phosphorus is often a limiting nutrient for plants and "
          "other producers, particularly in freshwater and some terrestrial ecosystems."),

 dict(q="The table compares how much of the dry atmosphere each of two elements makes up "
        "in gas form. Which conclusion about the two cycles is best supported by the "
        "table together with the framework?",
      table=_T_ATMOS,
      choices=[
        "The nitrogen cycle has a large atmospheric reservoir while the phosphorus cycle "
        "lacks a significant atmospheric component.",
        "The phosphorus cycle has a large atmospheric reservoir while the nitrogen cycle "
        "lacks a significant atmospheric component.",
        "Both cycles have large atmospheric reservoirs.",
        "Neither cycle has any atmospheric component at all.",
        "The two elements occupy the same share of the atmosphere."],
      ans=0,
      why="ERT-1.E.4 makes the atmosphere the largest reservoir of nitrogen and ERT-1.F.2 "
          "states that the phosphorus cycle lacks a significant atmospheric component, "
          "which is the asymmetry the tabulated shares record."),

 dict(q="The table gives the phosphorus held in six reservoirs. Which conclusion is best "
        "supported?",
      table=_T_PRESERVOIR,
      choices=[
        "Rock and ocean sediments together hold almost all of the phosphorus listed, "
        "while the atmosphere holds a negligible amount.",
        "The atmosphere holds the largest share of the phosphorus listed.",
        "Living organisms hold more phosphorus than ocean sediments do.",
        "The six reservoirs hold roughly equal amounts of phosphorus.",
        "Soil holds more phosphorus than rock does."],
      ans=0,
      why="The two mineral reservoirs sum to essentially the whole tabulated total while "
          "the atmospheric entry is smaller by many orders of magnitude. ERT-1.F.2 names "
          "rock and ocean sediments as the major reservoirs and denies the cycle a "
          "significant atmospheric component."),

 dict(q="Four rock types in one study area were compared, as shown. Which relationship do "
        "the data support?",
      table=_T_WEATHER,
      choices=[
        "Rock that weathers to a greater depth releases more phosphorus to the soil.",
        "Rock that weathers to a greater depth releases less phosphorus to the soil.",
        "The depth weathered has no relationship with the phosphorus released.",
        "The rock weathering least deeply released the most phosphorus.",
        "All four rock types weathered to the same depth."],
      ans=0,
      why="Sorting the rock types by depth weathered leaves the phosphorus released "
          "strictly increasing. ERT-1.F.3 makes the slowness of rock weathering the "
          "reason phosphorus is scarce, so the rate of weathering is what governs supply."),

 dict(q="Four enclosures in one lake received the treatments shown. Which conclusion is "
        "best supported?",
      table=_T_LAKEADD,
      choices=[
        "Phosphorus was limiting algal growth in this lake, since adding it raised algal "
        "mass sharply while adding nitrogen alone did not.",
        "Nitrogen was limiting algal growth in this lake, since adding it raised algal "
        "mass sharply.",
        "Neither nutrient affected algal growth in this lake.",
        "The enclosure receiving nothing grew the most algae.",
        "Adding both nutrients together reduced algal growth below the untreated level."],
      ans=0,
      why="The nitrogen enclosure barely differs from the untreated one while both "
          "enclosures receiving phosphorus rose several-fold. ERT-1.F.3 states that "
          "phosphorus is often the limiting nutrient particularly in freshwater "
          "ecosystems."),

 dict(q="Four grassland plots received different amounts of phosphorus, with the results "
        "shown. Which conclusion is best supported?",
      table=_T_TERRA,
      choices=[
        "Adding phosphorus raised the plant mass grown, which is what is expected where "
        "phosphorus limits producers.",
        "Adding phosphorus lowered the plant mass grown.",
        "Plant mass grown was unaffected by the phosphorus added.",
        "The plot receiving no phosphorus grew the most plant mass.",
        "Only the plot receiving the most phosphorus differed from the untreated plot."],
      ans=0,
      why="Plant mass increases at every step up the phosphorus column. ERT-1.F.3 states "
          "that phosphorus is often a limiting nutrient for plants and other producers, "
          "particularly in freshwater and some terrestrial ecosystems, and grassland is a "
          "terrestrial case."),

 dict(q="Available soil phosphorus was measured on land surfaces of different ages, as "
        "shown. Which conclusion is best supported?",
      table=_T_AGE,
      choices=[
        "Available phosphorus falls as the land surface gets older, which fits a supply "
        "that is opened only slowly and not replaced from the air.",
        "Available phosphorus rises as the land surface gets older.",
        "Available phosphorus is the same on surfaces of every age.",
        "The oldest surface holds the most available phosphorus.",
        "The youngest surface holds the least available phosphorus."],
      ans=0,
      why="Available phosphorus falls steadily with surface age. ERT-1.F.2 gives the "
          "cycle no significant atmospheric component to replenish a soil, and ERT-1.F.3 "
          "makes the rock supply slow to open, so a long-exposed surface has no fast "
          "route to resupply."),

 dict(q="Four routes by which phosphorus moves are shown with their annual quantities. "
        "Which conclusion is best supported?",
      table=_T_PFLUX,
      choices=[
        "The airborne route moves far less phosphorus than the rock, river and sediment "
        "routes do.",
        "The airborne route moves more phosphorus than any other route listed.",
        "All four routes move about the same quantity of phosphorus each year.",
        "Burial in ocean sediments moves no phosphorus at all.",
        "Weathering of rock moves less phosphorus than the airborne route does."],
      ans=0,
      why="The airborne figure is smaller than each of the other three by more than an "
          "order of magnitude. ERT-1.F.2 states that the phosphorus cycle lacks a "
          "significant atmospheric component, which is what a small airborne flux next to "
          "large mineral and water fluxes shows."),

 dict(q="Which of the following is NOT part of the phosphorus cycle as the framework "
        "describes it?",
      choices=[
        "A large reservoir of phosphorus gas in the atmosphere.",
        "Rock containing phosphorus-bearing minerals.",
        "Ocean sediments containing phosphorus-bearing minerals.",
        "The movement of phosphorus-containing molecules between sources and sinks.",
        "The uptake of phosphorus by plants and other producers."],
      ans=0,
      why="ERT-1.F.2 states that the phosphorus cycle lacks a significant atmospheric "
          "component, while ERT-1.F.1 supplies the movement between sources and sinks, "
          "ERT-1.F.2 supplies the two mineral reservoirs, and ERT-1.F.3 makes phosphorus "
          "a nutrient for producers."),

 dict(q="If the rocks of a region began to weather far more rapidly, which change does "
        "the framework most directly support predicting?",
      choices=[
        "More phosphorus would be released into the region's ecosystems.",
        "Less phosphorus would be released into the region's ecosystems.",
        "Phosphorus would begin to enter the region from the atmosphere.",
        "Phosphorus would be destroyed as the rock broke down.",
        "The region's producers would stop taking up phosphorus."],
      ans=0,
      why="ERT-1.F.3 states that phosphorus is relatively scarce because rocks weather "
          "slowly, which makes the weathering rate the gate on supply, so opening that "
          "gate wider lets more phosphorus through."),

 dict(q="A student writes that phosphorus enters ecosystems from the air in the same way "
        "nitrogen does. What is the best correction?",
      choices=[
        "The phosphorus cycle lacks a significant atmospheric component, so its supply "
        "comes from rock and sediments instead.",
        "The nitrogen cycle lacks a significant atmospheric component, so the comparison "
        "is backwards.",
        "Neither element has any reservoir outside living organisms.",
        "Phosphorus enters ecosystems from the air, so the student is correct as stated.",
        "Both elements enter ecosystems only through ocean sediments."],
      ans=0,
      why="ERT-1.F.2 states that the phosphorus cycle lacks a significant atmospheric "
          "component and names rock and ocean sediments as its major reservoirs, while "
          "ERT-1.E.4 makes the atmosphere the largest nitrogen reservoir, so the two "
          "cycles differ exactly here."),

 dict(q="A limnologist wants to find out whether phosphorus limits algal growth in a "
        "lake. Which design would give the most direct evidence?",
      choices=[
        "Add phosphorus to some enclosures in the lake, leave others untreated, and "
        "compare the algal mass grown.",
        "Measure how much phosphorus the lake's rocks contain.",
        "Count the number of fish species in the lake over one summer.",
        "Compare the lake with a lake on another continent.",
        "Measure how deep the lake is at several points."],
      ans=0,
      why="ERT-1.F.3 states that phosphorus is often a limiting nutrient for producers, "
          "particularly in freshwater ecosystems, and a limiting nutrient is tested by "
          "relieving the limit in some units and comparing them against untreated ones."),

 dict(q="Which observation would best support the claim that phosphorus is the nutrient "
        "limiting producers at a site?",
      choices=[
        "Adding phosphorus raises the mass of producers while adding other nutrients "
        "alone does not.",
        "The site contains more phosphorus in its rock than a neighboring site does.",
        "Producers at the site contain phosphorus in their tissues.",
        "The site receives more rainfall than a neighboring site.",
        "The producers at the site belong to more species than at a neighboring site."],
      ans=0,
      why="A limiting nutrient is identified by the response to relieving it, so the "
          "diagnostic comparison is between adding phosphorus and adding something else. "
          "Merely containing phosphorus, or holding it in rock, does not show that its "
          "supply is what constrains growth."),

 dict(q="Why can the supply of phosphorus available to an ecosystem not be raised quickly "
        "by any natural process the framework describes?",
      choices=[
        "Because its major reservoirs are rock and sediments, which release phosphorus "
        "only as they weather, and there is no significant atmospheric route.",
        "Because phosphorus atoms cannot move between reservoirs at all.",
        "Because the atmosphere holds phosphorus but releases it only once a century.",
        "Because producers refuse to take up phosphorus when it is abundant.",
        "Because phosphorus is destroyed as fast as it is released."],
      ans=0,
      why="ERT-1.F.2 places the major reservoirs in rock and ocean sediments and denies "
          "the cycle a significant atmospheric component, and ERT-1.F.3 makes rock "
          "weathering slow, so both of the routes that might act quickly are closed."),

 dict(q="Phosphorus carried by rivers is deposited on the seafloor and buried. Which "
        "framework statement does that describe?",
      choices=[
        "Ocean sediments are one of the major reservoirs of phosphorus.",
        "The phosphorus cycle has a significant atmospheric component.",
        "Phosphorus is abundant in ecosystems because rocks weather quickly.",
        "Phosphorus is never a limiting nutrient for producers.",
        "Living organisms are the major reservoir of phosphorus."],
      ans=0,
      why="ERT-1.F.2 names rock and ocean sediments that contain phosphorus-bearing "
          "minerals as the major reservoirs of the cycle, and burial on the seafloor is "
          "phosphorus arriving at one of them."),

 dict(q="Dissolved phosphorus and algal mass were measured in four lakes, as shown. Which "
        "conclusion is best supported?",
      table=_T_TWOLAKES,
      choices=[
        "Lakes with more dissolved phosphorus carry more algae, which fits phosphorus "
        "acting as a limiting nutrient in fresh water.",
        "Lakes with more dissolved phosphorus carry less algae.",
        "Algal mass is the same in all four lakes.",
        "The lake with the least dissolved phosphorus carries the most algae.",
        "Dissolved phosphorus is the same in all four lakes."],
      ans=0,
      why="Sorting the lakes by dissolved phosphorus leaves algal mass strictly "
          "increasing. ERT-1.F.3 states that phosphorus is often a limiting nutrient for "
          "producers, particularly in freshwater ecosystems."),

 dict(q="An ecosystem sits on a very old land surface whose rock has already been deeply "
        "weathered. Which prediction does the framework support?",
      choices=[
        "Phosphorus is likely to be in short supply there, because the slow rock source "
        "has already given up much of what it held.",
        "Phosphorus is likely to be abundant there, because weathering has been going on "
        "for a long time.",
        "Phosphorus will be resupplied quickly from the atmosphere.",
        "Nitrogen will replace phosphorus in the tissues of the producers.",
        "The producers there will not require phosphorus at all."],
      ans=0,
      why="ERT-1.F.3 attributes phosphorus scarcity to slow rock weathering, and "
          "ERT-1.F.2 gives the cycle no significant atmospheric route, so a long-weathered "
          "surface has neither a fast source nor an aerial resupply."),

 dict(q="A student claims that because rock is abundant everywhere, phosphorus can never "
        "be scarce in an ecosystem. What is the best correction?",
      choices=[
        "The size of the rock store is not the constraint; the slow rate at which rock "
        "weathers is.",
        "Rock contains no phosphorus, so the premise is false.",
        "Phosphorus is scarce because it escapes into the atmosphere.",
        "Phosphorus is never scarce, so the conclusion is right.",
        "Ocean sediments, not rock, are the only reservoir of phosphorus."],
      ans=0,
      why="ERT-1.F.2 grants that rock is a major reservoir, and ERT-1.F.3 states that "
          "phosphorus is relatively scarce in ecosystems BECAUSE rocks weather slowly, so "
          "the constraint is the rate of release rather than the size of the store."),

 dict(q="Which pair of framework statements together explains why phosphorus is often the "
        "nutrient that limits producers?",
      choices=[
        "Its major reservoirs are slowly weathering rock and sediments, and it has no "
        "significant atmospheric route into ecosystems.",
        "Its major reservoir is the atmosphere, and it is released quickly by weathering.",
        "It is created by producers, and it is destroyed by decomposers.",
        "It is abundant in living organisms, and it moves rapidly between them.",
        "It has no reservoirs at all, and it is not required by producers."],
      ans=0,
      why="ERT-1.F.3 gives slow rock weathering as the cause of scarcity and ERT-1.F.2 "
          "denies the cycle a significant atmospheric component, so both of the ways a "
          "supply might be replenished quickly are absent."),

 dict(q="Which of the following is the best evidence that phosphorus moves between "
        "sources and sinks rather than staying in one place?",
      choices=[
        "Phosphorus released from weathering rock is later found in soil, in producers, "
        "and eventually in ocean sediments.",
        "Phosphorus is present in the mineral grains of a rock sample.",
        "Producers contain phosphorus in their tissues at a single moment.",
        "Phosphorus and nitrogen are different elements.",
        "The atmosphere contains no measurable phosphorus gas."],
      ans=0,
      why="ERT-1.F.1 defines the phosphorus cycle as the movement of phosphorus-containing "
          "atoms and molecules between sources and sinks, so tracing the same phosphorus "
          "through successive reservoirs is what shows the movement. A single "
          "measurement at one place shows only a standing amount."),

 dict(q="Two lakes receive the same amount of nitrogen but very different amounts of "
        "phosphorus. Which prediction does the framework most directly support?",
      choices=[
        "The lake receiving more phosphorus is likely to support more producer growth.",
        "The two lakes must support the same producer growth, since nitrogen is equal.",
        "The lake receiving more phosphorus is likely to support less producer growth.",
        "Phosphorus cannot affect producer growth in fresh water.",
        "Producer growth in lakes depends only on the depth of the water."],
      ans=0,
      why="ERT-1.F.3 states that phosphorus is often a limiting nutrient for plants and "
          "other producers, particularly in freshwater ecosystems, so a difference in the "
          "limiting nutrient is expected to show up as a difference in growth."),

 dict(q="Which statement correctly describes where most of the Earth's phosphorus is "
        "held?",
      choices=[
        "In rock and in ocean sediments containing phosphorus-bearing minerals.",
        "In the atmosphere, as a gas.",
        "In the tissues of living organisms.",
        "In the fresh water of rivers and lakes.",
        "In clouds and rainfall."],
      ans=0,
      why="ERT-1.F.2 names rock and ocean sediments that contain phosphorus-bearing "
          "minerals as the major reservoirs of phosphorus and denies the cycle a "
          "significant atmospheric component."),

 dict(q="An ecologist finds that adding phosphorus to a stretch of grassland increases "
        "plant growth, but adding it to a nearby stretch does not. Which reading is most "
        "consistent with the framework?",
      choices=[
        "Phosphorus limits producers in some terrestrial ecosystems but not in all of "
        "them.",
        "Phosphorus limits producers in every terrestrial ecosystem without exception.",
        "Phosphorus never limits producers in terrestrial ecosystems.",
        "The result shows that phosphorus is supplied from the atmosphere.",
        "The result shows that rock weathering has no effect on phosphorus supply."],
      ans=0,
      why="ERT-1.F.3 says phosphorus is often a limiting nutrient, particularly in "
          "freshwater and SOME terrestrial ecosystems. The words often and some are part "
          "of the claim, so a mixed result across two grassland stretches is what the "
          "statement leads one to expect."),

 dict(q="Why does the absence of a significant atmospheric component matter for how "
        "quickly a depleted soil can regain phosphorus?",
      choices=[
        "Because there is no widespread airborne supply that can deliver phosphorus to a "
        "soil that has lost it.",
        "Because the atmosphere would otherwise remove phosphorus from soils.",
        "Because phosphorus in the air would prevent rock from weathering.",
        "Because soils gain all of their phosphorus from rainfall.",
        "Because the atmosphere is the largest phosphorus reservoir."],
      ans=0,
      why="ERT-1.F.2 states that the phosphorus cycle lacks a significant atmospheric "
          "component, so unlike an element with a large atmospheric reservoir, phosphorus "
          "has no aerial route by which a depleted place can be resupplied from a "
          "distance."),

 dict(q="Which comparison of the phosphorus cycle with the nitrogen cycle is supported by "
        "the framework?",
      choices=[
        "Phosphorus has its major reservoirs in rock and sediments, while nitrogen has "
        "its largest reservoir in the atmosphere.",
        "Phosphorus has its largest reservoir in the atmosphere, while nitrogen has its "
        "major reservoirs in rock and sediments.",
        "Both elements have their largest reservoirs in the atmosphere.",
        "Both elements have their major reservoirs in rock and sediments.",
        "Neither element has any major reservoir."],
      ans=0,
      why="ERT-1.F.2 names rock and ocean sediments as the major phosphorus reservoirs "
          "and denies that cycle a significant atmospheric component, while ERT-1.E.4 "
          "states that the largest reservoir of nitrogen is the atmosphere."),

 dict(q="A researcher measures a steady flow of phosphorus out of a watershed in its "
        "river water, with no comparable flow in. Which framework statement does this "
        "most directly illustrate?",
      choices=[
        "Phosphorus moves between sources and sinks, and a watershed can lose it faster "
        "than slow weathering replaces it.",
        "Phosphorus is created within the watershed by its producers.",
        "The atmosphere resupplies the watershed with phosphorus each year.",
        "Phosphorus cannot leave a watershed once it has entered the soil.",
        "Rock weathering supplies phosphorus faster than any river can remove it."],
      ans=0,
      why="ERT-1.F.1 makes the cycle a movement between sources and sinks, and ERT-1.F.3 "
          "makes the rock source slow, so an outflow that exceeds the weathering supply "
          "is exactly the situation those two statements together allow."),
]
