# AP ENVIRONMENTAL SCIENCE 1.5 The Nitrogen Cycle
# CED effective Fall 2026, Unit 1 The Living World: Ecosystems.
# Enduring understanding ERT-1: Ecosystems are the result of biotic and abiotic
# interactions.
# Learning objective ERT-1.E: explain the steps and reservoir interactions in the
# nitrogen cycle. Suggested skill 2.B.
#
# Essential knowledge relied on, in the framework's own words:
#   ERT-1.E.1  The nitrogen cycle is the movement of atoms and molecules containing the
#              element nitrogen between sources and sinks. It involves several steps,
#              including nitrogen fixation, assimilation, ammonification, nitrification,
#              and denitrification. Microorganisms in the soil play an important role in
#              many of these steps.
#   ERT-1.E.2  In nitrogen fixation, atmospheric nitrogen (N2) is converted by certain
#              types of soil bacteria into ammonia (NH3). In the soil, ammonia quickly
#              converts to ammonium (NH4+), which is available for biological uptake.
#   ERT-1.E.3  The availability of nitrogen compounds in the soil is limited by the rate
#              of nitrogen fixation. In many ecosystems, the availability of nitrogen
#              compounds limits primary production by plants and other producers.
#   ERT-1.E.4  The largest reservoir of nitrogen is the atmosphere. Most of the reservoirs
#              in which nitrogen compounds occur in the nitrogen cycle hold those
#              compounds for relatively short periods of time.
#
# WHAT IS DELIBERATELY NOT ASKED. The framework NAMES assimilation, ammonification,
# nitrification and denitrification and DEFINES none of them; only nitrogen fixation is
# defined, in ERT-1.E.2. So no item here asks what any of those four steps does, and no
# item asks a student to put the five steps in an order the framework does not give -- it
# writes "several steps, including", which is a list, not a sequence. The four undefined
# names are used only as members of the list they appear in.
#
# HOW THIS TOPIC IS KEPT DISTINCT FROM 1.4, 1.6 AND 1.7. The sources-and-sinks definition
# is asked in 1.4 for carbon and is NOT re-asked here; the nitrogen items instead turn on
# the list of steps, on the chemistry of fixation, on fixation rate as the limit on
# availability, and on the atmosphere as the largest reservoir. Holding time appears here
# only as ERT-1.E.4's claim that MOST nitrogen reservoirs are short-term, which is a
# different claim from the carbon one in ERT-1.D.2 that reservoirs differ.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: export_units.py does not typeset
# Environmental Science.
TOPIC = ("1.5", "The Nitrogen Cycle", 1)

_T_RESERVOIRS = dict(
    headers=["Nitrogen reservoir", "Nitrogen held (billions of tonnes)"],
    rows=[["Atmosphere", "3900000"],
          ["Soil organic matter", "190"],
          ["Ocean water", "570"],
          ["Living organisms on land", "12"],
          ["Rivers and lakes", "1"]])

_T_HOLDING = dict(
    headers=["Nitrogen reservoir", "Average time nitrogen stays in the reservoir (years)"],
    rows=[["Atmosphere", "10000000"],
          ["Soil ammonium", "0.05"],
          ["Soil nitrate", "0.1"],
          ["Living plant tissue", "3"],
          ["Ocean surface water", "8"]])

_T_ADDED = dict(
    headers=["Plot treatment", "Nitrogen added each year (kilograms per hectare)",
             "Plant mass grown each year (kilograms per hectare)"],
    rows=[["No addition", "0", "1900"],
          ["Low addition", "25", "3100"],
          ["Medium addition", "50", "4400"],
          ["High addition", "100", "5200"]])

_T_STERILE = dict(
    headers=["Soil treatment", "Nitrogen fixed in thirty days (milligrams per kilogram of soil)"],
    rows=[["Untreated soil", "48"],
          ["Soil heated to kill microorganisms", "1"],
          ["Heated soil with microorganisms added back", "44"]])

_T_FIXRATE = dict(
    headers=["Site", "Nitrogen fixed each year (kilograms per hectare)",
             "Nitrogen available in the soil (kilograms per hectare)"],
    rows=[["Site 1", "3", "9"],
          ["Site 2", "11", "31"],
          ["Site 3", "26", "70"],
          ["Site 4", "48", "128"]])

_T_AMMONIA = dict(
    headers=["Hours after ammonia was added to the soil",
             "Ammonia remaining (milligrams per kilogram)",
             "Ammonium present (milligrams per kilogram)"],
    rows=[["0", "40", "1"],
          ["2", "17", "23"],
          ["6", "4", "35"],
          ["24", "1", "38"]])

_T_LEGUME = dict(
    headers=["Field plot", "Nitrogen in the soil at the start (kilograms per hectare)",
             "Nitrogen in the soil after three seasons (kilograms per hectare)"],
    rows=[["Planted with a nitrogen-fixing crop", "22", "61"],
          ["Planted with a crop that fixes no nitrogen", "22", "17"]])

_T_LIMITING = dict(
    headers=["Nutrient added to a plot", "Plant mass grown (kilograms per hectare)"],
    rows=[["Nothing added", "1800"],
          ["Phosphorus only", "1950"],
          ["Potassium only", "1840"],
          ["Nitrogen only", "4300"]])

QUESTIONS = [

 dict(q="Which of the following does the framework list among the steps of the nitrogen "
        "cycle?",
      choices=[
        "Nitrogen fixation, assimilation, ammonification, nitrification, and "
        "denitrification.",
        "Evaporation, condensation, precipitation, and runoff.",
        "Photosynthesis, cellular respiration, and combustion.",
        "Weathering, transport, and deposition of parent rock.",
        "Convergence, divergence, and transform motion of plates."],
      ans=0,
      why="ERT-1.E.1 states that the nitrogen cycle involves several steps, including "
          "nitrogen fixation, assimilation, ammonification, nitrification and "
          "denitrification. The rejected lists belong to the water cycle, the carbon "
          "cycle, soil formation and plate tectonics."),

 dict(q="What happens in nitrogen fixation, according to the framework?",
      choices=[
        "Atmospheric nitrogen is converted by certain types of soil bacteria into "
        "ammonia.",
        "Ammonia is converted by plant roots into atmospheric nitrogen.",
        "Nitrogen atoms are created inside the bodies of soil bacteria.",
        "Nitrogen compounds are washed out of the soil into rivers by rainfall.",
        "Atmospheric nitrogen is absorbed directly into plant tissue without any change."],
      ans=0,
      why="ERT-1.E.2 states that in nitrogen fixation, atmospheric nitrogen is converted "
          "by certain types of soil bacteria into ammonia. The conversion runs from the "
          "gas toward ammonia, and it is bacteria that carry it out."),

 dict(q="According to the framework, what becomes of ammonia once it is in the soil?",
      choices=[
        "It quickly converts to ammonium, which is available for biological uptake.",
        "It quickly converts back to atmospheric nitrogen and leaves the soil.",
        "It remains as ammonia indefinitely and is never taken up.",
        "It converts to carbon dioxide, which plants take up.",
        "It converts to phosphate, which plants take up."],
      ans=0,
      why="ERT-1.E.2 states that in the soil, ammonia quickly converts to ammonium, which "
          "is available for biological uptake. Both the speed of the conversion and the "
          "availability of the product are part of that sentence."),

 dict(q="Which nitrogen-containing form does the framework identify as available for "
        "biological uptake?",
      choices=[
        "Ammonium.",
        "Nitrogen gas as it occurs in the atmosphere.",
        "Ammonia only, before any further change.",
        "Elemental nitrogen locked in rock.",
        "Nitrogen dissolved in seawater as a gas."],
      ans=0,
      why="ERT-1.E.2 states that ammonia quickly converts to ammonium in the soil and "
          "that ammonium is available for biological uptake. The framework attaches that "
          "description to no other form."),

 dict(q="What does the framework identify as the limit on how much nitrogen compound is "
        "available in the soil?",
      choices=[
        "The rate of nitrogen fixation.",
        "The total mass of nitrogen in the atmosphere.",
        "The rate at which rock containing nitrogen weathers.",
        "The number of plant species present in the ecosystem.",
        "The rate at which water evaporates from the soil surface."],
      ans=0,
      why="ERT-1.E.3 states that the availability of nitrogen compounds in the soil is "
          "limited by the rate of nitrogen fixation, so it is the rate of that step "
          "rather than the size of the atmospheric store that sets availability."),

 dict(q="In many ecosystems, what does the framework say the availability of nitrogen "
        "compounds limits?",
      choices=[
        "Primary production by plants and other producers.",
        "The number of predator species an ecosystem can hold.",
        "The rate at which water moves through the hydrologic cycle.",
        "The rate at which phosphorus-bearing rock weathers.",
        "The depth to which sunlight penetrates a lake."],
      ans=0,
      why="ERT-1.E.3 states that in many ecosystems the availability of nitrogen "
          "compounds limits primary production by plants and other producers, which is "
          "the specific claim the keyed option restates."),

 dict(q="Which is the largest reservoir of nitrogen, according to the framework?",
      choices=[
        "The atmosphere.",
        "Soil organic matter.",
        "The bodies of living organisms.",
        "Sedimentary rock.",
        "Rivers and lakes."],
      ans=0,
      why="ERT-1.E.4 states plainly that the largest reservoir of nitrogen is the "
          "atmosphere. The framework assigns no such rank to any of the rejected "
          "reservoirs."),

 dict(q="What does the framework say about how long most nitrogen reservoirs hold their "
        "nitrogen compounds?",
      choices=[
        "Most hold them for relatively short periods of time.",
        "Most hold them for millions of years.",
        "All reservoirs hold them for exactly the same length of time.",
        "No reservoir holds them for longer than a single day.",
        "The framework makes no statement about holding times for nitrogen."],
      ans=0,
      why="ERT-1.E.4 states that most of the reservoirs in which nitrogen compounds occur "
          "hold those compounds for relatively short periods of time. The word most is "
          "part of the claim, so it is not a statement about every reservoir."),

 dict(q="What role does the framework assign to microorganisms in the soil within the "
        "nitrogen cycle?",
      choices=[
        "They play an important role in many of the steps of the cycle.",
        "They play no part in the cycle, which is entirely a chemical process.",
        "They are the only reservoir in which nitrogen occurs.",
        "They convert nitrogen atoms into phosphorus atoms.",
        "They take part only in the movement of water through the soil."],
      ans=0,
      why="ERT-1.E.1 states that microorganisms in the soil play an important role in "
          "many of the steps of the nitrogen cycle, and ERT-1.E.2 names certain types of "
          "soil bacteria as the agents of fixation."),

 dict(q="The table gives the amount of nitrogen held in five reservoirs. Which conclusion "
        "is best supported?",
      table=_T_RESERVOIRS,
      choices=[
        "The atmosphere holds far more nitrogen than all the other reservoirs listed put "
        "together.",
        "Ocean water holds more nitrogen than the atmosphere does.",
        "The five reservoirs hold roughly equal amounts of nitrogen.",
        "Living organisms on land hold the largest share of the nitrogen listed.",
        "Rivers and lakes hold more nitrogen than soil organic matter does."],
      ans=0,
      why="The atmospheric figure exceeds the sum of the other four by several orders of "
          "magnitude, which is the quantitative form of the claim in ERT-1.E.4 that the "
          "largest reservoir of nitrogen is the atmosphere."),

 dict(q="Average holding times for five nitrogen reservoirs are shown. Which statement is "
        "best supported by the table?",
      table=_T_HOLDING,
      choices=[
        "Most of the listed reservoirs hold nitrogen for years or less, with the "
        "atmosphere the exception.",
        "Most of the listed reservoirs hold nitrogen for millions of years.",
        "Every listed reservoir holds nitrogen for the same length of time.",
        "Soil ammonium holds nitrogen for longer than the atmosphere does.",
        "Ocean surface water holds nitrogen for the shortest time of the five."],
      ans=0,
      why="Four of the five tabulated holding times are measured in years or fractions of "
          "a year and only one is very long, which is the pattern ERT-1.E.4 describes "
          "when it says most nitrogen reservoirs hold their compounds for relatively "
          "short periods."),

 dict(q="Four plots received different amounts of added nitrogen, with the results shown. "
        "Which conclusion is best supported?",
      table=_T_ADDED,
      choices=[
        "Plant mass grown rises as nitrogen is added, which is what is expected where "
        "nitrogen availability limits production.",
        "Plant mass grown falls as nitrogen is added.",
        "Plant mass grown is unchanged by the amount of nitrogen added.",
        "The plot receiving no nitrogen grew the most plant mass.",
        "Nitrogen addition raised plant mass only in the plot receiving the least "
        "nitrogen."],
      ans=0,
      why="Plant mass increases at every step up the nitrogen addition column. ERT-1.E.3 "
          "states that in many ecosystems the availability of nitrogen compounds limits "
          "primary production by plants and other producers, and a response to addition "
          "is what a limiting nutrient produces."),

 dict(q="Three soil samples were treated as shown and the nitrogen fixed over thirty days "
        "was measured. Which conclusion is best supported?",
      table=_T_STERILE,
      choices=[
        "Fixation depends on living microorganisms, since killing them almost stopped it "
        "and adding them back restored it.",
        "Fixation is a purely chemical process that continues when microorganisms are "
        "killed.",
        "Heating the soil increased the amount of nitrogen fixed.",
        "Adding microorganisms back to the heated soil reduced fixation further.",
        "All three treatments fixed about the same amount of nitrogen."],
      ans=0,
      why="Fixation collapsed when the soil was heated and recovered when microorganisms "
          "were returned, so the living component is what carries it. ERT-1.E.2 names "
          "certain types of soil bacteria as the agents of nitrogen fixation."),

 dict(q="Nitrogen fixation and soil nitrogen availability were measured at four sites, as "
        "shown. Which relationship do these data support?",
      table=_T_FIXRATE,
      choices=[
        "Sites that fix more nitrogen each year also hold more available nitrogen in "
        "their soil.",
        "Sites that fix more nitrogen each year hold less available nitrogen in their "
        "soil.",
        "Available soil nitrogen is the same at every site regardless of fixation.",
        "The site fixing the least nitrogen holds the most available nitrogen.",
        "Fixation is the same at all four sites, so no relationship can be examined."],
      ans=0,
      why="Sorting the sites by the amount of nitrogen fixed leaves available soil "
          "nitrogen strictly increasing. ERT-1.E.3 states that the availability of "
          "nitrogen compounds in the soil is limited by the rate of nitrogen fixation."),

 dict(q="Ammonia was added to a soil sample and both ammonia and ammonium were measured "
        "over the following day, as shown. Which conclusion is best supported?",
      table=_T_AMMONIA,
      choices=[
        "Ammonia was converted to ammonium within hours, which matches the framework's "
        "description of a quick conversion.",
        "Ammonium was converted to ammonia within hours.",
        "Neither compound changed in amount over the day.",
        "Ammonia rose steadily over the day while ammonium fell.",
        "The conversion took many years to complete."],
      ans=0,
      why="Ammonia falls sharply and ammonium rises by a similar amount within the first "
          "hours of the record. ERT-1.E.2 states that in the soil, ammonia quickly "
          "converts to ammonium, which is available for biological uptake."),

 dict(q="Two field plots were followed for three seasons, as shown. Which conclusion is "
        "best supported?",
      table=_T_LEGUME,
      choices=[
        "The plot carrying a nitrogen-fixing crop gained soil nitrogen while the other "
        "plot lost it.",
        "Both plots gained soil nitrogen over the three seasons.",
        "Both plots lost soil nitrogen over the three seasons.",
        "The plot carrying a nitrogen-fixing crop lost soil nitrogen while the other "
        "gained it.",
        "The two plots started with different amounts of soil nitrogen."],
      ans=0,
      why="The two plots began at the same value and moved in opposite directions, with "
          "the fixing crop's plot rising. ERT-1.E.2 identifies fixation as the step that "
          "brings atmospheric nitrogen into a form available in the soil."),

 dict(q="A plot was given each of three nutrients separately, with the results shown. "
        "Which conclusion is best supported?",
      table=_T_LIMITING,
      choices=[
        "Nitrogen was the nutrient limiting production on this plot, since only its "
        "addition produced a large increase.",
        "Phosphorus was the nutrient limiting production on this plot.",
        "Potassium was the nutrient limiting production on this plot.",
        "All three nutrients were equally limiting on this plot.",
        "None of the three nutrients affected production on this plot."],
      ans=0,
      why="Only the nitrogen treatment raised plant mass substantially above the untreated "
          "value; the other two changed it very little. ERT-1.E.3 states that in many "
          "ecosystems the availability of nitrogen compounds limits primary production."),

 dict(q="Which of the following is NOT one of the steps the framework lists for the "
        "nitrogen cycle?",
      choices=[
        "Transpiration.",
        "Nitrogen fixation.",
        "Ammonification.",
        "Nitrification.",
        "Denitrification."],
      ans=0,
      why="ERT-1.E.1 lists nitrogen fixation, assimilation, ammonification, nitrification "
          "and denitrification. The rejected term belongs to the movement of water rather "
          "than to any step of the nitrogen cycle."),

 dict(q="Why can a plant not simply take up the nitrogen it needs from the enormous "
        "supply of nitrogen in the air?",
      choices=[
        "Because the framework makes ammonium, not atmospheric nitrogen, the form "
        "available for biological uptake.",
        "Because the atmosphere contains only a very small amount of nitrogen.",
        "Because plants have no contact with the atmosphere.",
        "Because atmospheric nitrogen is converted to phosphate before uptake.",
        "Because the atmosphere holds nitrogen for only a very short time."],
      ans=0,
      why="ERT-1.E.2 identifies ammonium as the form available for biological uptake and "
          "makes fixation the step that produces it from atmospheric nitrogen, while "
          "ERT-1.E.4 makes the atmosphere the largest reservoir, so size is not the "
          "obstacle."),

 dict(q="If the soil bacteria that carry out nitrogen fixation were eliminated from an "
        "ecosystem, which consequence does the framework most directly support "
        "predicting?",
      choices=[
        "The supply of nitrogen compounds available in the soil would fall, and primary "
        "production could fall with it.",
        "The supply of nitrogen compounds available in the soil would rise, since none "
        "would be consumed.",
        "The atmosphere would lose most of its nitrogen.",
        "Plants would begin absorbing nitrogen gas directly from the air.",
        "Phosphorus would replace nitrogen as a component of plant tissue."],
      ans=0,
      why="ERT-1.E.3 makes the rate of nitrogen fixation the limit on soil nitrogen "
          "availability and makes that availability a limit on primary production in many "
          "ecosystems, so removing the fixers removes the supply at its source."),

 dict(q="A researcher wants to test whether nitrogen availability limits production at a "
        "grassland site. Which design would give the most direct evidence?",
      choices=[
        "Add nitrogen to some plots and nothing to others, and compare the plant mass "
        "grown.",
        "Measure the nitrogen content of the atmosphere above the site over a year.",
        "Count the number of plant species present in a single plot.",
        "Compare the site with a forest on a different continent.",
        "Measure the depth of the soil at several points across the site."],
      ans=0,
      why="ERT-1.E.3 states that the availability of nitrogen compounds limits primary "
          "production in many ecosystems, and the way to test a limiting factor is to "
          "relieve the limit in some plots and compare against untreated ones."),

 dict(q="A student writes that because the atmosphere is the largest nitrogen reservoir, "
        "nitrogen can never be in short supply for plants. What is the best correction?",
      choices=[
        "Availability in the soil is set by the rate of fixation, not by the size of the "
        "atmospheric store.",
        "The atmosphere is in fact a small nitrogen reservoir, so the premise is wrong.",
        "Plants take nitrogen from rock rather than from the soil.",
        "Nitrogen is never limiting in any ecosystem, so the conclusion is right for the "
        "wrong reason.",
        "The atmosphere holds nitrogen for only a very short time, so it empties quickly."],
      ans=0,
      why="ERT-1.E.4 grants the premise that the atmosphere is the largest reservoir, but "
          "ERT-1.E.3 states that soil availability is limited by the rate of nitrogen "
          "fixation, so a large store can sit behind a slow gateway."),

 dict(q="Which sequence correctly follows nitrogen from the air into a form a plant can "
        "take up, as the framework describes it?",
      choices=[
        "Atmospheric nitrogen is converted to ammonia by soil bacteria, and the ammonia "
        "converts to ammonium.",
        "Atmospheric nitrogen is converted to ammonium by soil bacteria, and the ammonium "
        "converts to ammonia.",
        "Ammonium is converted to ammonia by plants, and the ammonia enters the air.",
        "Atmospheric nitrogen dissolves in soil water and is taken up unchanged.",
        "Ammonia forms in the air and falls to the soil, where bacteria convert it to "
        "nitrogen gas."],
      ans=0,
      why="ERT-1.E.2 gives the order directly: atmospheric nitrogen is converted by "
          "certain types of soil bacteria into ammonia, and in the soil ammonia quickly "
          "converts to ammonium, which is available for biological uptake."),

 dict(q="Which observation would best support the claim that microorganisms are essential "
        "to the nitrogen cycle in a particular soil?",
      choices=[
        "Nitrogen transformations in that soil almost cease when its microorganisms are "
        "killed and resume when they are restored.",
        "That soil contains more nitrogen than the soil of a neighboring field.",
        "That soil is darker in color than the soil of a neighboring field.",
        "Plants grown in that soil are taller than plants grown in sand.",
        "That soil holds water for longer than a sandy soil does."],
      ans=0,
      why="ERT-1.E.1 states that microorganisms in the soil play an important role in many "
          "of the steps of the nitrogen cycle, and the way to show that a living agent is "
          "responsible is to remove it and restore it while watching the process."),

 dict(q="Why does the framework describe the availability of nitrogen compounds as a "
        "limit rather than as a guarantee of production?",
      choices=[
        "Because production in many ecosystems cannot exceed what the available nitrogen "
        "supports, whatever else is present.",
        "Because nitrogen compounds destroy plant tissue when they are abundant.",
        "Because nitrogen compounds are the only substance plants require.",
        "Because nitrogen availability determines the number of animal species present.",
        "Because nitrogen availability sets the size of the atmospheric reservoir."],
      ans=0,
      why="ERT-1.E.3 says that in many ecosystems the availability of nitrogen compounds "
          "limits primary production, which is a ceiling on what producers can achieve "
          "rather than a claim that nitrogen alone determines the outcome."),

 dict(q="Which statement correctly pairs a nitrogen reservoir with the framework's claim "
        "about it?",
      choices=[
        "The atmosphere is the largest reservoir, and most other reservoirs hold nitrogen "
        "for relatively short periods.",
        "Soil organic matter is the largest reservoir, and the atmosphere holds nitrogen "
        "briefly.",
        "Living organisms form the largest reservoir, and rock holds nitrogen briefly.",
        "The oceans form the largest reservoir, and the atmosphere holds nitrogen for "
        "millions of years.",
        "Every reservoir is the same size and holds nitrogen for the same time."],
      ans=0,
      why="ERT-1.E.4 makes two claims at once: the largest reservoir of nitrogen is the "
          "atmosphere, and most of the reservoirs in which nitrogen compounds occur hold "
          "them for relatively short periods of time."),

 dict(q="A farmer plants a nitrogen-fixing crop in a depleted field and the soil nitrogen "
        "rises. Which framework statement best accounts for the rise?",
      choices=[
        "Nitrogen fixation converts atmospheric nitrogen into a form that becomes "
        "available in the soil.",
        "Nitrogen compounds are created from nothing by the roots of the crop.",
        "The crop draws nitrogen out of the underlying rock.",
        "The crop converts phosphorus in the soil into nitrogen.",
        "The soil holds nitrogen for millions of years once it arrives."],
      ans=0,
      why="ERT-1.E.2 states that in nitrogen fixation atmospheric nitrogen is converted by "
          "soil bacteria into ammonia, which quickly becomes ammonium available for "
          "biological uptake, and that pathway is the only route the framework gives from "
          "the air into the soil."),

 dict(q="Two soils receive the same quantity of ammonium. In one, plants take it up "
        "rapidly; in the other, most of it is lost within weeks. Which framework claim is "
        "consistent with the second soil?",
      choices=[
        "Most of the reservoirs in which nitrogen compounds occur hold those compounds "
        "for relatively short periods of time.",
        "The largest reservoir of nitrogen is the atmosphere.",
        "Nitrogen fixation converts atmospheric nitrogen into ammonia.",
        "Microorganisms play no role in the nitrogen cycle.",
        "Nitrogen availability never limits primary production."],
      ans=0,
      why="ERT-1.E.4 states that most nitrogen reservoirs hold their compounds for "
          "relatively short periods, so a soil pool that empties within weeks is an "
          "instance of that general claim rather than an anomaly."),

 dict(q="Which comparison correctly distinguishes the role of fixation from the role of "
        "the atmospheric reservoir in the nitrogen cycle?",
      choices=[
        "The atmosphere is where most nitrogen sits; fixation is what makes some of it "
        "available in the soil.",
        "The atmosphere is where nitrogen becomes available; fixation is where most "
        "nitrogen sits.",
        "Both the atmosphere and fixation are reservoirs of nitrogen.",
        "Both the atmosphere and fixation are steps in the movement of nitrogen.",
        "Neither the atmosphere nor fixation has any part in the nitrogen cycle."],
      ans=0,
      why="ERT-1.E.4 makes the atmosphere the largest reservoir and ERT-1.E.2 makes "
          "fixation the conversion of atmospheric nitrogen into ammonia and then "
          "ammonium, so one is a place and the other is a process."),

 dict(q="An ecosystem's producers grow no faster after several wet years, but grow much "
        "faster in the first year after nitrogen-fixing plants colonize the site. What "
        "does this pattern most directly suggest?",
      choices=[
        "Nitrogen availability, rather than water, was limiting primary production at "
        "that site.",
        "Water availability, rather than nitrogen, was limiting primary production at "
        "that site.",
        "Neither water nor nitrogen has any effect on production at that site.",
        "The colonizing plants removed nitrogen from the soil.",
        "The site had no producers before the colonizing plants arrived."],
      ans=0,
      why="Production did not respond to extra water but did respond once a source of "
          "fixed nitrogen appeared, and ERT-1.E.3 states that in many ecosystems the "
          "availability of nitrogen compounds limits primary production by plants and "
          "other producers."),
]
