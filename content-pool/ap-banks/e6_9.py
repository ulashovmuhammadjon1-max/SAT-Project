# AP ENVIRONMENTAL SCIENCE 6.9 Hydroelectric Power
# CED effective Fall 2026, Unit 6 Energy Resources and Consumption.
# Enduring understanding ENG-3: humans use energy from a variety of sources, resulting in
# positive and negative consequences.
# Learning objectives ENG-3.L, describe the use of hydroelectricity in power generation; and
# ENG-3.M, describe the effects of the use of hydroelectricity in power generation on the
# environment.
# Suggested skill 7.F, justify a proposed solution by explaining potential advantages --
# which is why several items here put a scheme to a community and ask what may honestly be
# said for it.
#
# Essential knowledge relied on, in the framework's own words:
#   ENG-3.L.1  Hydroelectric power can be generated in several ways. Dams built across
#              rivers collect water in reservoirs. The moving water can be used to spin a
#              turbine. Turbines can also be placed in small rivers, where the flowing water
#              spins the turbine.
#   ENG-3.L.2  Tidal energy uses the energy produced by tidal flows to turn a turbine.
#   ENG-3.M.1  Hydroelectric power does not generate air pollution or waste, but
#              construction of the power plants can be expensive, and there may be a loss of
#              or change in habitats following the construction of dams.
#
# THREE ARRANGEMENTS, ONE COMMON PART. ENG-3.L.1 says SEVERAL WAYS and then describes a dam
# collecting water in a reservoir, and turbines placed in small rivers; ENG-3.L.2 adds tidal
# flows. In every one of them moving water turns a TURBINE. Two items key what the three
# have in common and one keys the correction to a student who thinks a dam is required.
#
# THE HABITAT CLAUSE IS DOUBLY QUALIFIED, and every key respects both qualifications. The
# framework says THERE MAY BE A LOSS OF OR CHANGE IN HABITATS FOLLOWING THE CONSTRUCTION OF
# DAMS. It is hedged with MAY; it is a loss OR A CHANGE, not only a loss; and it is
# attached to DAMS rather than to hydroelectric power in general, so nothing here hangs it
# on a turbine set in a small river or on a tidal scheme.
#
# NOT AIR POLLUTION OR WASTE, AND NOTHING STRONGER. ENG-3.M.1 denies air pollution and waste
# and grants two costs in the same sentence. No key here reads the denial as a claim that
# hydroelectric power has no effects at all, and the summary items carry the reservations
# alongside the advantage.
#
# HYDROELECTRIC POWER IS NOT CLASSIFIED. The framework labels nuclear power nonrenewable in
# ENG-3.G.4 and wind renewable in ENG-3.S.1, and never labels hydroelectricity either way.
# One item keys that absence and no other item treats it as classified.
#
# NO FIGURES. Every quantitative item carries a table=; all arithmetic is recomputed in
# verify_e6_9.py from that table alone and is calculator-free.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("6.9", "Hydroelectric Power", 6)

_T_SCHEME = dict(
    headers=["Scheme studied",
             "Height of the dam built (meters)",
             "Land flooded to form a reservoir (hectares)",
             "Electricity delivered each year (thousand energy units)"],
    rows=[["Scheme 1, a barrier across a large river", "60", "4,000", "900"],
          ["Scheme 2, turbines set in a small river", "0", "0", "40"],
          ["Scheme 3, turbines driven by tidal flows", "0", "0", "120"]])

_T_EFFECT = dict(
    headers=["Plant compared",
             "Air pollutants released for each unit of electricity (kilograms)",
             "Solid waste produced for each unit of electricity (kilograms)",
             "Cost to build for each unit of capacity (currency units)"],
    rows=[["Hydroelectric plant", "0", "0", "2,400"],
          ["Coal plant", "9", "0.8", "800"]])

_T_HABITAT = dict(
    headers=["Stage of the river survey",
             "Flowing river-channel habitat in the reach (hectares)",
             "Still-water habitat in the reach (hectares)",
             "Fish species recorded in the reach"],
    rows=[["Before the barrier was built", "1,200", "0", "26"],
          ["Five years after it was built", "300", "4,000", "17"],
          ["Twenty years after it was built", "280", "4,000", "15"]])

_T_TIDE = dict(
    headers=["Hour of the tidal cycle recorded",
             "Speed of the tidal flow past the turbine (flow units)",
             "Electricity the turbine delivers (energy units)"],
    rows=[["Hour 1", "0", "0"],
          ["Hour 2", "2", "40"],
          ["Hour 3", "4", "80"],
          ["Hour 4", "6", "120"]])

QUESTIONS = [

 dict(q="How many ways of generating hydroelectric power does the framework describe, and which "
        "are they?",
      choices=[
        "Several: a barrier across a river collecting water in a reservoir, turbines placed in "
        "small rivers, and turbines turned by tidal flows",
        "One only: a barrier across a river collecting water in a reservoir",
        "One only: turbines placed in small rivers",
        "Several, but the framework describes none of them in particular",
        "Two: turbines in small rivers and turbines heated by the sun"],
      ans=0,
      why="ENG-3.L.1 opens by saying hydroelectric power CAN BE GENERATED IN SEVERAL WAYS and then "
          "describes dams collecting water in reservoirs and turbines placed in small rivers, "
          "while ENG-3.L.2 adds tidal flows turning a turbine. Solar heating belongs to topic 6.8."),

 dict(q="What does the framework say a barrier built across a river does?",
      choices=[
        "It collects water in a reservoir",
        "It filters the water before the water reaches the turbine",
        "It stores electricity for use when the river is low",
        "It removes the need for a turbine altogether",
        "It heats the water so that steam can be raised"],
      ans=0,
      why="ENG-3.L.1 states that DAMS BUILT ACROSS RIVERS COLLECT WATER IN RESERVOIRS. Nothing in "
          "the statement gives the barrier a filtering, storing or heating role, and the turbine "
          "is still required to generate the electricity."),

 dict(q="What does the framework say the moving water is used for?",
      choices=[
        "To spin a turbine",
        "To spin a generator with no turbine involved",
        "To raise steam that then spins a turbine",
        "To cool the equipment inside the plant",
        "To be transformed directly into electrical energy"],
      ans=0,
      why="ENG-3.L.1 states that THE MOVING WATER CAN BE USED TO SPIN A TURBINE. No steam appears "
          "anywhere in this topic, and transforming energy directly into electricity is what "
          "photovoltaic cells do in topic 6.8."),

 dict(q="Besides behind a barrier, where does the framework say turbines can be placed?",
      choices=[
        "In small rivers, where the flowing water spins the turbine",
        "In reservoirs, where the still water spins the turbine",
        "In cooling towers, where the falling water spins the turbine",
        "In pipelines, where pumped water spins the turbine",
        "The framework names no other place a turbine can be put"],
      ans=0,
      why="ENG-3.L.1 states that TURBINES CAN ALSO BE PLACED IN SMALL RIVERS, WHERE THE FLOWING "
          "WATER SPINS THE TURBINE. Still water does not spin anything, and cooling towers and "
          "pipelines appear nowhere in this topic."),

 dict(q="What does the framework say tidal energy uses, and to what end?",
      choices=[
        "The energy produced by tidal flows, to turn a turbine",
        "The energy produced by tidal flows, to heat a liquid for storage",
        "The difference in salinity between sea water and river water, to turn a turbine",
        "The heat of the surface ocean, to raise steam for a turbine",
        "The weight of water held behind a barrier, with no turbine involved"],
      ans=0,
      why="ENG-3.L.2 states that TIDAL ENERGY USES THE ENERGY PRODUCED BY TIDAL FLOWS TO TURN A "
          "TURBINE. Heating a liquid for storage is an active solar system in topic 6.8, and "
          "salinity and ocean heat appear nowhere in the framework's account."),

 dict(q="What does the framework say hydroelectric power does NOT generate?",
      choices=[
        "Air pollution or waste",
        "Air pollution, though it does generate waste",
        "Waste, though it does generate air pollution",
        "Any change in the habitats of the river",
        "Any cost to the community that builds it"],
      ans=0,
      why="ENG-3.M.1 opens by stating that HYDROELECTRIC POWER DOES NOT GENERATE AIR POLLUTION OR "
          "WASTE. The same sentence goes on to grant an expensive construction and a possible "
          "loss of or change in habitats, so the denial covers those two things and no more."),

 dict(q="Which two reservations does the framework attach in the same statement?",
      choices=[
        "That construction can be expensive, and that there may be a loss of or change in "
        "habitats after a barrier is built",
        "That construction can be expensive, and that the plant releases hazardous solid waste",
        "That the plant releases air pollutants, and that habitats may be lost or changed",
        "That the plant releases volatile organic compounds, and that construction is cheap",
        "The framework attaches no reservations to hydroelectric power"],
      ans=0,
      why="ENG-3.M.1 names exactly two: CONSTRUCTION OF THE POWER PLANTS CAN BE EXPENSIVE, and "
          "THERE MAY BE A LOSS OF OR CHANGE IN HABITATS FOLLOWING THE CONSTRUCTION OF DAMS. "
          "Hazardous solid waste belongs to nuclear power and volatile organic compounds to "
          "fracking."),

 dict(q="What do the words MAY BE A LOSS OF OR CHANGE IN establish about the habitat "
        "reservation?",
      choices=[
        "That the effect is possible rather than certain, and that it may be a change in habitat "
        "rather than only a loss",
        "That the effect is certain wherever a barrier is built, and is always a total loss of "
        "habitat",
        "That the effect is possible rather than certain, and is always a total loss of habitat",
        "That the effect has never been observed in any river",
        "That the effect applies to turbines placed in small rivers as much as to barriers"],
      ans=0,
      why="ENG-3.M.1 hedges with MAY and offers two outcomes, A LOSS OF OR CHANGE IN habitats. The "
          "clause is also tied to THE CONSTRUCTION OF DAMS rather than to every arrangement, so "
          "extending it to a turbine set in a small river goes beyond the statement."),

 dict(q="To which of the arrangements is the framework's habitat reservation tied?",
      choices=[
        "To the construction of dams",
        "To turbines placed in small rivers",
        "To turbines turned by tidal flows",
        "To every arrangement equally",
        "To no arrangement, since the framework names no habitat effect"],
      ans=0,
      why="ENG-3.M.1 puts the habitat clause FOLLOWING THE CONSTRUCTION OF DAMS. The framework "
          "describes turbines in small rivers and tidal turbines elsewhere in this topic and "
          "attaches no habitat clause to either of them."),

 dict(q="A community is considering turbines set in a small river. Which advantage does the "
        "framework license them to cite?",
      choices=[
        "That hydroelectric power generates no air pollution and no waste",
        "That hydroelectric power is cheap to build",
        "That hydroelectric power creates new habitat wherever it is installed",
        "That hydroelectric power produces electricity without any turbine",
        "That hydroelectric power is unaffected by how much water is flowing"],
      ans=0,
      why="ENG-3.M.1 grants that hydroelectric power DOES NOT GENERATE AIR POLLUTION OR WASTE, "
          "which is the advantage the framework supplies. It says construction CAN BE EXPENSIVE "
          "rather than cheap, and a turbine is required in every arrangement it describes."),

 dict(q="A student writes that every hydroelectric scheme requires a barrier across a river. What "
        "correction does the framework require?",
      choices=[
        "Turbines can also be placed in small rivers, and tidal flows can turn a turbine without "
        "any barrier",
        "Turbines can also be placed in reservoirs, where the still water spins them",
        "Only tidal schemes avoid a barrier; a river scheme always requires one",
        "No correction is needed, since the framework describes only one arrangement",
        "The framework requires a barrier for tidal schemes but not for river schemes"],
      ans=0,
      why="ENG-3.L.1 says hydroelectric power can be generated in SEVERAL WAYS and names turbines "
          "placed in small rivers as one of them, while ENG-3.L.2 adds tidal flows. Neither "
          "involves collecting water behind a barrier, and still water spins nothing."),

 dict(q="A second student writes that the framework treats hydroelectric power as having no "
        "drawbacks. What correction is required?",
      choices=[
        "Construction can be expensive, and habitats may be lost or changed after a barrier is "
        "built",
        "The plant releases air pollutants, which is the drawback the framework names",
        "The plant produces hazardous solid waste, which is the drawback the framework names",
        "The framework names no drawback, so the student is correct",
        "The only drawback the framework names is that the electricity is expensive to sell"],
      ans=0,
      why="ENG-3.M.1 grants that there is no air pollution and no waste and then names two "
          "drawbacks, the cost of construction and a possible loss of or change in habitats. Air "
          "pollutants and hazardous solid waste are what other sources in this unit release."),

 dict(q="What do all three of the arrangements the framework describes have in common?",
      choices=[
        "Moving water turns a turbine in each of them",
        "A reservoir is filled behind a barrier in each of them",
        "Steam is raised before the turbine is reached in each of them",
        "Each of them stores energy for release when demand is high",
        "Each of them depends on the availability of sunlight"],
      ans=0,
      why="ENG-3.L.1 has moving water spinning a turbine behind a barrier and flowing water "
          "spinning a turbine in a small river, and ENG-3.L.2 has tidal flows turning a turbine. "
          "Only one of the three involves a reservoir, no steam appears anywhere, and the "
          "sunlight limit belongs to photovoltaic cells in topic 6.8."),

 dict(q="Which observation would most directly report the framework's habitat reservation?",
      choices=[
        "Surveying the habitats and the species of a river reach before a barrier is built and "
        "again afterwards",
        "Measuring the air pollutants leaving the powerhouse",
        "Recording the cost of the electricity the scheme sells in its first year",
        "Counting the turbines installed in small rivers across a country",
        "Measuring the speed of the tidal flow past a turbine through one cycle"],
      ans=0,
      why="ENG-3.M.1's reservation is a possible LOSS OF OR CHANGE IN HABITATS following the "
          "construction of dams, so the observation must compare the same reach before and after. "
          "Air pollutants, price, turbine counts and flow speed each bear on a different part of "
          "this topic."),

 dict(q="Which observation would most directly report the advantage the framework grants?",
      choices=[
        "Measuring the air pollutants and the waste leaving the plant for each unit of "
        "electricity",
        "Measuring the area flooded behind the barrier",
        "Counting the fish species in the reach below the barrier",
        "Recording how long the plant took to build",
        "Measuring the speed of the water entering the turbine"],
      ans=0,
      why="ENG-3.M.1's advantage is that hydroelectric power DOES NOT GENERATE AIR POLLUTION OR "
          "WASTE, so measuring both is what tests it. Flooded area and fish counts bear on the "
          "habitat reservation and the other two on neither claim."),

 dict(q="Does the framework classify hydroelectric power as a renewable or a nonrenewable energy "
        "source in this topic?",
      choices=[
        "It does neither; these statements describe how it works and what it does",
        "It calls hydroelectric power a renewable source",
        "It calls hydroelectric power a nonrenewable source",
        "It classifies tidal schemes as renewable and barrier schemes as nonrenewable",
        "It classifies barrier schemes as renewable and tidal schemes as nonrenewable"],
      ans=0,
      why="ENG-3.L.1, ENG-3.L.2 and ENG-3.M.1 describe arrangements and effects and assign no "
          "class. The framework does label nuclear power nonrenewable in ENG-3.G.4 and wind "
          "renewable in ENG-3.S.1, which shows that it labels a source where it means to."),

 dict(q="Three schemes were compared on what each required and what each delivered. Which one "
        "matches the framework's description of a barrier collecting water in a reservoir?",
      table=_T_SCHEME,
      choices=[
        "The first, which required a 60 meter barrier and flooded 4,000 hectares",
        "The second, which required no barrier and flooded nothing",
        "The third, which required no barrier and flooded nothing",
        "All three, since each of them collects water in a reservoir",
        "None of them, since the framework describes no scheme with a reservoir"],
      ans=0,
      why="Only the first scheme carries a barrier height and a flooded area, at 60 meters and "
          "4,000 hectares, while the other two carry none. ENG-3.L.1 states that DAMS BUILT ACROSS "
          "RIVERS COLLECT WATER IN RESERVOIRS, which is the arrangement the first scheme has."),

 dict(q="Using the same three schemes, which of them flood no land at all, and does the framework "
        "recognise such arrangements?",
      table=_T_SCHEME,
      choices=[
        "The second and third, and yes, the framework describes turbines in small rivers and "
        "turbines turned by tidal flows",
        "The second and third, but no, the framework describes only schemes with a reservoir",
        "The first and second, and yes, the framework describes turbines in small rivers",
        "Only the third, and yes, the framework describes turbines turned by tidal flows",
        "None of them, since every hydroelectric scheme floods some land"],
      ans=0,
      why="The second and third schemes show a flooded area of zero, and ENG-3.L.1 names turbines "
          "placed in small rivers while ENG-3.L.2 names tidal flows turning a turbine. Neither "
          "arrangement requires water to be collected behind a barrier."),

 dict(q="Using the same three schemes, how much more electricity does the scheme with the barrier "
        "deliver each year than the small river scheme?",
      table=_T_SCHEME,
      choices=[
        "860 thousand energy units",
        "900 thousand energy units",
        "940 thousand energy units",
        "780 thousand energy units",
        "1,060 thousand energy units"],
      ans=0,
      why="Subtracting the two tabulated deliveries gives 900 minus 40, which is 860 thousand "
          "energy units. The rejected values quote the barrier scheme alone, add that pair, take "
          "the gap to the tidal scheme instead, or add all three schemes together."),

 dict(q="Using the same three schemes, how much electricity comes each year from the arrangements "
        "that flood no land?",
      table=_T_SCHEME,
      choices=[
        "160 thousand energy units",
        "940 thousand energy units",
        "1,060 thousand energy units",
        "120 thousand energy units",
        "900 thousand energy units"],
      ans=0,
      why="The two schemes with no flooded area deliver 40 and 120 thousand energy units, which is "
          "160 between them. The rejected values add the wrong pair, add all three, quote the "
          "tidal scheme alone, or quote the barrier scheme, which floods land and so does not "
          "belong to the sum."),

 dict(q="A hydroelectric plant and a coal plant were compared. Which conclusion matches the "
        "framework's statement about hydroelectric power?",
      table=_T_EFFECT,
      choices=[
        "The hydroelectric plant releases no air pollutants and no solid waste, but costs more "
        "to build",
        "The hydroelectric plant releases no air pollutants and no solid waste, and costs less "
        "to build",
        "The hydroelectric plant releases air pollutants but no solid waste, and costs more to "
        "build",
        "The coal plant releases no air pollutants and no solid waste, but costs more to build",
        "The two plants release the same amounts and cost the same to build"],
      ans=0,
      why="The hydroelectric plant shows 0 kilograms of air pollutants and 0 of solid waste "
          "against the coal plant's 9 and 0.8, and costs 2,400 currency units for each unit of "
          "capacity against 800. ENG-3.M.1 states that hydroelectric power does not generate air "
          "pollution or waste BUT that construction can be expensive."),

 dict(q="Using the same two plants, how many times as much does the hydroelectric plant cost to "
        "build for each unit of capacity?",
      table=_T_EFFECT,
      choices=[
        "Three times as much",
        "Two times as much",
        "Eight times as much",
        "Thirty times as much",
        "It costs less than the coal plant"],
      ans=0,
      why="Dividing the two tabulated costs gives 2,400 divided by 800, which is 3. The rejected "
          "values shift the answer by a power of ten, quote a wrong division, or invert the "
          "comparison the record shows."),

 dict(q="A river reach was surveyed before a barrier was built and twice afterwards. Which of the "
        "framework's claims do the values support?",
      table=_T_HABITAT,
      choices=[
        "That there may be a loss of or change in habitats following the construction of a "
        "barrier",
        "That hydroelectric power generates air pollution and waste",
        "That the construction of the plant is inexpensive",
        "That habitats are unaffected by the construction of a barrier",
        "That tidal energy uses the energy produced by tidal flows"],
      ans=0,
      why="Flowing river-channel habitat falls from 1,200 to 300 to 280 hectares while still-water "
          "habitat rises from none to 4,000, and fish species fall from 26 to 17 to 15. ENG-3.M.1 "
          "names a possible LOSS OF OR CHANGE IN HABITATS following the construction of dams."),

 dict(q="Using the same survey, which reading of the two habitat columns matches the framework's "
        "wording most closely?",
      table=_T_HABITAT,
      choices=[
        "Some habitat was lost and the kind of habitat present also changed, which is the loss "
        "or change the framework allows for",
        "Habitat was lost and no new habitat of any kind appeared in the reach",
        "No habitat was lost and only the kind of habitat present changed",
        "Habitat was gained overall, so the framework's reservation does not apply",
        "The two columns show no change of any sort across the survey"],
      ans=0,
      why="Flowing river-channel habitat falls by more than nine hundred hectares while 4,000 "
          "hectares of still water appear where there was none. ENG-3.M.1 speaks of A LOSS OF OR "
          "CHANGE IN HABITATS, and this reach shows both at once."),

 dict(q="Using the same survey, how much flowing river-channel habitat was lost between the first "
        "reading and the last?",
      table=_T_HABITAT,
      choices=[
        "920 hectares",
        "900 hectares",
        "1,200 hectares",
        "300 hectares",
        "1,480 hectares"],
      ans=0,
      why="Subtracting the two tabulated areas gives 1,200 minus 280, which is 920 hectares. The "
          "rejected values take the fall to the middle reading, quote the opening area, quote the "
          "middle reading itself, or add the first and last readings."),

 dict(q="Using the same survey, by how many species did the fish count fall across the record?",
      table=_T_HABITAT,
      choices=[
        "By 11 species",
        "By 9 species",
        "By 2 species",
        "By 26 species",
        "By 41 species"],
      ans=0,
      why="Subtracting the two tabulated counts gives 26 minus 15, which is 11 species. The "
          "rejected values take one of the two steps within the record, quote the opening count, "
          "or add the three readings together."),

 dict(q="A tidal turbine was logged through part of a tidal cycle. Which of the framework's "
        "claims do the values illustrate?",
      table=_T_TIDE,
      choices=[
        "That tidal energy uses the energy produced by tidal flows to turn a turbine",
        "That tidal energy uses the difference in salinity between sea and river water",
        "That tidal energy requires a barrier to be built across the estuary",
        "That hydroelectric power generates air pollution and waste",
        "That construction of a tidal plant is inexpensive"],
      ans=0,
      why="The turbine delivers nothing while the flow is still and 40, 80 and 120 energy units as "
          "the flow reaches 2, 4 and 6 flow units. ENG-3.L.2 states that TIDAL ENERGY USES THE "
          "ENERGY PRODUCED BY TIDAL FLOWS TO TURN A TURBINE."),

 dict(q="Using the same tidal record, how much electricity does the turbine deliver for each unit "
        "of flow speed?",
      table=_T_TIDE,
      choices=[
        "20 energy units",
        "40 energy units",
        "10 energy units",
        "60 energy units",
        "The amount for each unit of flow cannot be worked out from the record"],
      ans=0,
      why="Dividing output by flow speed at each hour with a flow gives 40 over 2, 80 over 4 and "
          "120 over 6, which is 20 energy units for each flow unit throughout. The rejected values "
          "quote one hour's output, halve the rate, treble it, or deny an arithmetic the record "
          "plainly allows."),

 dict(q="Using the same tidal record, why does the turbine deliver nothing in the first hour?",
      table=_T_TIDE,
      choices=[
        "Because the tidal flow past it has stopped, and the framework makes the flow what turns "
        "the turbine",
        "Because the turbine is being repaired at that hour",
        "Because the framework says a turbine needs a reservoir behind it to work",
        "Because tidal turbines deliver electricity only at night",
        "Because the record has not begun and no measurement was taken"],
      ans=0,
      why="The first hour records a flow speed of zero and an output of zero, and every hour with a "
          "flow delivers electricity in proportion to it. ENG-3.L.2 makes the energy produced by "
          "tidal flows what turns the turbine, so no flow means no output."),

 dict(q="Which summary states this topic as the framework does, without adding to it?",
      choices=[
        "Hydroelectric power can be generated in several ways: a barrier across a river "
        "collects water in a reservoir and the moving water spins a turbine, turbines can be "
        "placed in small rivers where the flowing water spins them, and tidal flows can turn a "
        "turbine; the power generates no air pollution and no waste, but construction can be "
        "expensive and habitats may be lost or changed after a barrier is built.",
        "Hydroelectric power can be generated only behind a barrier, and it generates air "
        "pollution and waste but is cheap to build.",
        "Hydroelectric power generates no air pollution and no waste, is cheap to build, and "
        "has no effect on habitats of any kind.",
        "Tidal energy raises steam that spins a turbine, and turbines placed in small rivers "
        "require a reservoir to work.",
        "Hydroelectric power is a renewable energy source, which is what this topic "
        "establishes."],
      ans=0,
      why="The keyed summary carries ENG-3.L.1, ENG-3.L.2 and ENG-3.M.1 in the framework's own "
          "terms, including both reservations and the hedge on the habitat clause. Each rejected "
          "summary reduces the arrangements to one, reverses the emissions or the cost, denies the "
          "habitat clause, invents steam, or assigns a class the framework never assigns."),
]
