# AP ENVIRONMENTAL SCIENCE 5.9 Impacts of Mining
# CED effective Fall 2026, Unit 5 Land and Water Use.
# Enduring understanding EIN-2: when humans use natural resources, they alter natural
# systems.
# Learning objectives EIN-2.K, describe natural resource extraction through mining;
# EIN-2.L, describe ecological and economic impacts of natural resource extraction
# through mining.
# Suggested skill 7.E, make a claim that proposes a solution to an environmental problem
# in an applied context.
#
# Essential knowledge relied on, in the framework's own words:
#   EIN-2.K.1  As the more accessible ores are mined to depletion, mining operations are
#              forced to access lower grade ores. Accessing these ores requires increased
#              use of resources that can cause increased waste and pollution.
#   EIN-2.K.2  Surface mining is the removal of large portions of soil and rock, called
#              overburden, in order to access the ore underneath. An example is strip
#              mining, which removes the vegetation from an area, making the area more
#              susceptible to erosion.
#   EIN-2.L.1  Mining wastes include the soil and rocks that are moved to gain access to
#              the ore and the waste, called slag and tailings that remain when the
#              minerals have been removed from the ore. Mining helps to provide low cost
#              energy and material necessary to make products. The mining of coal can
#              destroy habitats, contaminate ground water, and release dust particles and
#              methane.
#   EIN-2.L.2  As coal reserves get smaller, due to a lack of easily accessible reserves,
#              it becomes necessary to access coal through subsurface mining, which is
#              very expensive.
#
# SCOPE. The framework supplies four vocabulary terms -- overburden, strip mining, slag
# and tailings -- one economic benefit, one economic trend, and a named list of coal
# mining harms: destroyed habitats, contaminated ground water, dust particles and
# methane. It names no mine, no metal, no company and no country, and it gives no
# figures. Every quantitative item here therefore prints its data in a table and the
# arithmetic is recomputed in verify_e5_9.py from that table alone.
#
# THE ONE THING NOT TO OVERSTATE. EIN-2.L.1 is not a condemnation: it states in the same
# breath that MINING HELPS TO PROVIDE LOW COST ENERGY AND MATERIAL NECESSARY TO MAKE
# PRODUCTS. Two items key that benefit, and no item here says the framework treats mining
# as harm alone.
#
# BOUNDARY WITH UNIT 6. The combustion of coal, the steam cycle and fracking are ENG-3.E
# and ENG-3.F in topic 6.5, and the distribution of coal and ores by geologic history is
# ENG-3.D.1 in topic 6.4. This topic is the EXTRACTION and its wastes, not the burning
# and not the geography.
#
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("5.9", "Impacts of Mining", 5)

_T_GRADE = dict(
    headers=["Ore worked",
             "Metal in the ore (kilograms per tonne of rock)",
             "Rock that must be moved for one tonne of metal (tonnes)",
             "Energy used per tonne of metal (gigajoules)"],
    rows=[["High grade ore, mined first", "20", "50", "30"],
          ["Medium grade ore", "5", "200", "90"],
          ["Low grade ore, mined last", "2", "500", "210"]])

_T_STRIP = dict(
    headers=["Condition of the ground",
             "Vegetation cover (percent of the ground)",
             "Soil lost in one year (tonnes per hectare)"],
    rows=[["Undisturbed before mining", "92", "2"],
          ["Stripped of vegetation and overburden", "4", "58"],
          ["Replanted ten years after mining", "61", "9"]])

_T_WASTE = dict(
    headers=["Material leaving the mine in one year",
             "Mass (thousand tonnes)"],
    rows=[["Overburden moved to reach the ore", "780"],
          ["Tailings left after the minerals were removed", "190"],
          ["Slag left after smelting", "26"],
          ["Metal sold", "4"]])

_T_WELLS = dict(
    headers=["Well sampled",
             "Distance from the coal mine (kilometers)",
             "Sulfate in the well water (milligrams per litre)"],
    rows=[["Well 1", "1", "610"],
          ["Well 2", "3", "340"],
          ["Well 3", "8", "120"],
          ["Well 4", "20", "35"]])

_T_COST = dict(
    headers=["Method of reaching the coal",
             "Cost per tonne of coal produced (currency units)",
             "Depth of the coal worked (meters)"],
    rows=[["Surface mining of a shallow seam", "18", "30"],
          ["Subsurface mining of a deep seam", "74", "400"]])

_T_DUST = dict(
    headers=["Distance from the coal mine (kilometers)",
             "Dust particles in the air (micrograms per cubic meter)",
             "Methane in the air above the workings (parts per million)"],
    rows=[["At the workings", "180", "24"],
          ["Two", "90", "8"],
          ["Ten", "22", "2"]])

QUESTIONS = [

 dict(q="What does the course framework say happens as the more accessible ores are mined "
        "to depletion?",
      choices=[
        "Mining operations are forced to access lower grade ores",
        "Mining operations switch to ores of higher grade than before",
        "Mining operations stop, because no further ore can be reached",
        "Mining operations use less energy per tonne of metal than before",
        "Mining operations produce less waste per tonne of metal than before"],
      ans=0,
      why="EIN-2.K.1 states that as the more accessible ores are mined to depletion, mining "
          "operations are forced to access lower grade ores. The same statement adds that "
          "accessing them requires increased use of resources, so the energy and waste options "
          "point the wrong way."),

 dict(q="What consequence does the framework attach to working lower grade ores?",
      choices=[
        "Increased use of resources, which can cause increased waste and pollution",
        "Decreased use of resources, which reduces waste and pollution",
        "Increased use of resources, but with no change in waste or pollution",
        "No change in resource use, but a large fall in waste and pollution",
        "The framework attaches no consequence to working lower grade ores"],
      ans=0,
      why="EIN-2.K.1 states that accessing lower grade ores requires increased use of resources "
          "that can cause increased waste and pollution. Each rejected option reverses a "
          "direction, breaks the link between the two, or denies the statement exists."),

 dict(q="Three ore grades from one deposit are compared in the table. What do the values "
        "show about working a lower grade ore?",
      table=_T_GRADE,
      choices=[
        "More rock must be moved and more energy used for each tonne of metal obtained.",
        "Less rock must be moved and less energy used for each tonne of metal obtained.",
        "More rock must be moved but less energy used for each tonne of metal obtained.",
        "The rock moved and the energy used per tonne of metal are the same at "
        "every grade.",
        "The lowest grade ore yields the most metal per tonne of rock."],
      ans=0,
      why="As the metal content falls from 20 to 5 to 2 kilograms per tonne, the rock moved "
          "rises from 50 to 200 to 500 tonnes and the energy from 30 to 90 to 210 gigajoules "
          "per tonne of metal. EIN-2.K.1 states that accessing lower grade ores requires "
          "increased use of resources that can cause increased waste and pollution."),

 dict(q="Using the same three ore grades, how many times as much rock must be moved for a "
        "tonne of metal from the lowest grade ore as from the highest grade ore?",
      table=_T_GRADE,
      choices=[
        "Ten times as much",
        "Four times as much",
        "Seven times as much",
        "Two and a half times as much",
        "The same amount"],
      ans=0,
      why="Dividing the two tabulated masses gives 500 divided by 50, which is 10. The rejected "
          "values come from the middle grade, from the energy column, or from denying that the "
          "two differ."),

 dict(q="From the same comparison, how much more energy is needed for a tonne of metal from "
        "the lowest grade ore than from the highest grade ore?",
      table=_T_GRADE,
      choices=[
        "180 gigajoules more",
        "210 gigajoules more",
        "120 gigajoules more",
        "60 gigajoules more",
        "240 gigajoules more"],
      ans=0,
      why="Subtracting the two tabulated energies gives 210 minus 30, which is 180 gigajoules "
          "per tonne of metal. The rejected values quote the low grade figure alone, pair the "
          "wrong grades, or add the two rather than differencing them."),

 dict(q="What does the framework call the soil and rock removed in order to reach the ore "
        "beneath it?",
      choices=[
        "Overburden",
        "Tailings",
        "Slag",
        "Sediment",
        "Aggregate"],
      ans=0,
      why="EIN-2.K.2 states that surface mining is the removal of large portions of soil and "
          "rock, called overburden, in order to access the ore underneath. EIN-2.L.1 reserves "
          "the words slag and tailings for what remains after the minerals have been removed "
          "from the ore."),

 dict(q="What does the framework call the waste that remains once the minerals have been "
        "removed from the ore?",
      choices=[
        "Slag and tailings",
        "Overburden and topsoil",
        "Sediment and silt",
        "Peat and lignite",
        "Aggregate and gravel"],
      ans=0,
      why="EIN-2.L.1 states that mining wastes include the soil and rocks moved to gain access "
          "to the ore AND the waste, called slag and tailings, that remains when the minerals "
          "have been removed from the ore. Overburden is what is moved to reach the ore, under "
          "EIN-2.K.2, and peat and lignite are fuels in ENG-3.C."),

 dict(q="How does the framework describe strip mining?",
      choices=[
        "A form of surface mining that removes the vegetation from an area, making it more "
        "susceptible to erosion",
        "A form of subsurface mining that reaches coal through shafts sunk from "
        "the surface",
        "A method of returning overburden to a worked area once the ore has been removed",
        "A method of separating minerals from the ore after it has been brought "
        "to the surface",
        "A method of preventing erosion by leaving the vegetation in place"],
      ans=0,
      why="EIN-2.K.2 gives strip mining as an example of surface mining and states that it "
          "removes the vegetation from an area, making the area more susceptible to erosion. "
          "The rejected options describe subsurface mining, restoration, processing, or the "
          "opposite of what the statement says."),

 dict(q="A site was measured before mining, immediately after stripping, and ten years "
        "after replanting. What do the values show?",
      table=_T_STRIP,
      choices=[
        "Removing the vegetation cut the cover sharply and multiplied the soil lost, and "
        "replanting recovered part of both.",
        "Removing the vegetation raised the cover and reduced the soil lost, and "
        "replanting reversed both changes.",
        "Removing the vegetation left the cover and the soil lost unchanged.",
        "Replanting returned the site exactly to its condition before mining.",
        "The stripped site lost less soil than the undisturbed site."],
      ans=0,
      why="Cover runs 92, 4 and 61 percent while soil lost runs 2, 58 and 9 tonnes per hectare, "
          "so stripping cut the cover and raised the loss many times over and replanting "
          "recovered part but not all of each. EIN-2.K.2 states that strip mining removes the "
          "vegetation from an area, making the area more susceptible to erosion."),

 dict(q="Using the same site, how many times as much soil was lost in the year after "
        "stripping as in the year before mining?",
      table=_T_STRIP,
      choices=[
        "Twenty-nine times as much",
        "Four times as much",
        "Six times as much",
        "Twenty-three times as much",
        "The same amount"],
      ans=0,
      why="Dividing the two tabulated losses gives 58 divided by 2, which is 29. The rejected "
          "values come from the replanted row, from the difference rather than the ratio, or "
          "from denying that the two differ."),

 dict(q="Materials leaving one mine in a year are listed in the table. Which conclusion is "
        "best supported?",
      table=_T_WASTE,
      choices=[
        "The overburden moved to reach the ore is the largest single mass leaving the "
        "operation, and far larger than the metal sold.",
        "The metal sold is the largest single mass leaving the operation.",
        "The slag left after smelting is the largest single mass leaving the operation.",
        "All four materials leave the operation in about equal masses.",
        "No waste material leaves the operation at all."],
      ans=0,
      why="The tabulated masses are 780, 190, 26 and 4 thousand tonnes, so the overburden is "
          "much the largest and the metal sold much the smallest. EIN-2.L.1 states that mining "
          "wastes include the soil and rocks moved to gain access to the ore as well as the "
          "slag and tailings left afterwards."),

 dict(q="Using the same mine, what total mass of waste leaves the operation in a year, "
        "counting overburden, tailings and slag?",
      table=_T_WASTE,
      choices=[
        "996 thousand tonnes",
        "1,000 thousand tonnes",
        "970 thousand tonnes",
        "216 thousand tonnes",
        "780 thousand tonnes"],
      ans=0,
      why="Adding the three waste rows gives 780 plus 190 plus 26, which is 996 thousand "
          "tonnes. The rejected values include the metal sold, omit the slag, count only the "
          "two smaller wastes, or quote the overburden alone."),

 dict(q="Which economic benefit does the framework attribute to mining?",
      choices=[
        "It helps to provide low cost energy and material necessary to make products.",
        "It removes the need for any energy source other than coal.",
        "It guarantees that the price of every mineral will fall each year.",
        "It provides employment but no material of any kind.",
        "The framework attributes no benefit to mining."],
      ans=0,
      why="EIN-2.L.1 states, in the same statement as the list of wastes, that mining helps to "
          "provide low cost energy and material necessary to make products. The framework does "
          "record a benefit, so the last option is wrong on its face."),

 dict(q="Which set of harms does the framework attach specifically to the mining of coal?",
      choices=[
        "Destroyed habitats, contaminated ground water, and the release of dust particles "
        "and methane",
        "Destroyed habitats, salinized soil, and the release of nitrous oxide",
        "Waterlogged soil, eutrophic lakes, and the release of ozone",
        "Desertified rangeland, acidified oceans, and the release of chlorine",
        "The framework attaches no harms to coal mining in particular"],
      ans=0,
      why="EIN-2.L.1 states that the mining of coal can destroy habitats, contaminate ground "
          "water, and release dust particles and methane. Salinization is EIN-2.F.6, "
          "waterlogging EIN-2.F.1, eutrophication STB-3.F.1 and desertification EIN-2.I.5, all "
          "in other topics."),

 dict(q="Four wells at different distances from a coal mine were sampled. What does the "
        "pattern support?",
      table=_T_WELLS,
      choices=[
        "Sulfate concentration falls with distance from the mine, which is consistent with "
        "the mine as the source.",
        "Sulfate concentration rises with distance from the mine, which is consistent with "
        "the mine as the source.",
        "Sulfate concentration is the same at every distance, so the mine cannot be "
        "the source.",
        "The well nearest the mine has the lowest sulfate concentration of the four.",
        "Sulfate concentration in well water cannot be compared between wells."],
      ans=0,
      why="Distances run 1, 3, 8 and 20 kilometers while sulfate runs 610, 340, 120 and 35 "
          "milligrams per litre, falling steadily away from the mine. EIN-2.L.1 states that the "
          "mining of coal can contaminate ground water."),

 dict(q="Using the same wells, how much higher is the sulfate concentration nearest the mine "
        "than at the most distant well?",
      table=_T_WELLS,
      choices=[
        "575 milligrams per litre higher",
        "610 milligrams per litre higher",
        "490 milligrams per litre higher",
        "305 milligrams per litre higher",
        "645 milligrams per litre higher"],
      ans=0,
      why="Subtracting the two tabulated concentrations gives 610 minus 35, which is 575 "
          "milligrams per litre. The rejected values quote the nearest well alone, pair the "
          "wrong wells, or add the two readings instead of differencing them."),

 dict(q="Air was sampled at three distances from a coal mine. Which conclusion do the "
        "values support?",
      table=_T_DUST,
      choices=[
        "Both dust particles and methane are most concentrated at the workings and fall "
        "away with distance.",
        "Both dust particles and methane are least concentrated at the workings and rise "
        "with distance.",
        "Dust particles fall away with distance but methane rises with distance.",
        "Methane falls away with distance but dust particles rise with distance.",
        "Neither dust particles nor methane varies with distance from the workings."],
      ans=0,
      why="Dust runs 180, 90 and 22 micrograms per cubic meter and methane runs 24, 8 and 2 "
          "parts per million as distance increases, so both fall together. EIN-2.L.1 states "
          "that the mining of coal can release dust particles and methane."),

 dict(q="What does the framework say happens as coal reserves get smaller for lack of "
        "easily accessible reserves?",
      choices=[
        "It becomes necessary to access coal through subsurface mining, which is "
        "very expensive.",
        "It becomes necessary to access coal through surface mining, which is very cheap.",
        "It becomes impossible to reach any further coal at any cost.",
        "The cost of reaching coal falls, because the remaining seams lie nearer "
        "the surface.",
        "The framework makes no statement about how the cost of reaching coal changes."],
      ans=0,
      why="EIN-2.L.2 states that as coal reserves get smaller, due to a lack of easily "
          "accessible reserves, it becomes necessary to access coal through subsurface mining, "
          "which is very expensive. The rejected options reverse the method, the direction of "
          "the cost, or deny the statement."),

 dict(q="Two ways of reaching coal are compared in the table. Which reading matches the "
        "framework's statement?",
      table=_T_COST,
      choices=[
        "Reaching the deeper seam costs far more per tonne than working the shallow one, "
        "which is the expense the framework attaches to subsurface mining.",
        "Reaching the deeper seam costs far less per tonne than working the shallow one, "
        "which is the saving the framework attaches to subsurface mining.",
        "The two methods cost the same per tonne, so the framework's statement "
        "does not apply.",
        "The shallow seam lies deeper than the seam reached by subsurface mining.",
        "Neither method produces any coal, so the costs cannot be compared."],
      ans=0,
      why="The deep seam costs 74 currency units per tonne against 18 for the shallow one, and "
          "lies at 400 meters against 30. EIN-2.L.2 states that as easily accessible reserves "
          "run short it becomes necessary to access coal through subsurface mining, which is "
          "very expensive."),

 dict(q="Using the same two methods, how many times as much does a tonne of coal cost from "
        "the deep seam as from the shallow one, to the nearest whole number?",
      table=_T_COST,
      choices=[
        "About four times as much",
        "About two times as much",
        "About thirteen times as much",
        "About seven times as much",
        "About the same"],
      ans=0,
      why="Dividing the two tabulated costs gives 74 divided by 18, which is about 4.1 and "
          "rounds to about four. The rejected values come from the depth column, from halving "
          "rather than dividing, or from denying that the two differ."),

 dict(q="A student writes that the framework treats mining purely as a source of harm. Which "
        "correction is required?",
      choices=[
        "The same statement that lists mining wastes also says mining helps to provide low "
        "cost energy and material necessary to make products.",
        "The framework lists no wastes at all, so there is no harm to balance.",
        "The framework says mining provides material but denies that it provides "
        "low cost energy.",
        "The framework says mining provides energy but denies that it produces any waste.",
        "The framework says the harms of mining fall only on the workers."],
      ans=0,
      why="EIN-2.L.1 begins with the wastes and then states that mining helps to provide low "
          "cost energy and material necessary to make products, so both sides sit in one "
          "sentence. The framework does list wastes and does name both energy and material."),

 dict(q="Which pair of measurements would best show the effect the framework attaches to "
        "working progressively lower grade ores?",
      choices=[
        "The metal recovered from each tonne of rock, and the waste rock produced for each "
        "tonne of metal",
        "The metal recovered from each tonne of rock, and the number of workers at the mine",
        "The waste rock produced for each tonne of metal, and the distance to the "
        "nearest town",
        "The market price of the metal, and the age of the mining equipment",
        "The rainfall over the mine site, and the direction of the prevailing wind"],
      ans=0,
      why="EIN-2.K.1 links falling ore grade to increased use of resources and increased waste, "
          "so the test needs a measure of grade and a measure of waste per unit of product. The "
          "rejected pairs measure at most one of the two."),

 dict(q="A mining company proposes to reduce the erosion its operation causes. Which action "
        "addresses the mechanism the framework names for strip mining?",
      choices=[
        "Restoring vegetation cover on the stripped ground as soon as the ore has "
        "been removed",
        "Increasing the depth of overburden removed before the ore is reached",
        "Working a lower grade ore so that more rock is moved each year",
        "Smelting the ore on site so that more slag is produced",
        "Extending the working face over a larger area of ground each season"],
      ans=0,
      why="EIN-2.K.2 states that strip mining removes the vegetation from an area, making the "
          "area more susceptible to erosion, so returning the vegetation addresses the stated "
          "cause. Each rejected action removes more ground cover, moves more rock, or produces "
          "more waste."),

 dict(q="Which of the following correctly distinguishes overburden from tailings?",
      choices=[
        "Overburden is moved to reach the ore; tailings are what remains once the minerals "
        "have been taken out of the ore.",
        "Tailings are moved to reach the ore; overburden is what remains once the minerals "
        "have been taken out of the ore.",
        "Both are moved to reach the ore, and neither remains after processing.",
        "Both remain after processing, and neither is moved to reach the ore.",
        "Overburden is a fuel and tailings are a metal."],
      ans=0,
      why="EIN-2.K.2 defines overburden as the soil and rock removed in order to access the ore "
          "underneath, and EIN-2.L.1 defines slag and tailings as the waste that remains when "
          "the minerals have been removed from the ore. The two sit at opposite ends of the "
          "same operation."),

 dict(q="Using the ore grade comparison, how much metal is obtained from a tonne of the "
        "medium grade ore, and how does that compare with the high grade ore?",
      table=_T_GRADE,
      choices=[
        "5 kilograms per tonne, which is one quarter of the high grade figure",
        "5 kilograms per tonne, which is four times the high grade figure",
        "20 kilograms per tonne, which is the same as the high grade figure",
        "2 kilograms per tonne, which is one tenth of the high grade figure",
        "200 kilograms per tonne, which is ten times the high grade figure"],
      ans=0,
      why="The table gives 5 kilograms per tonne for the medium grade against 20 for the high "
          "grade, and 5 is a quarter of 20. The rejected options invert the comparison, quote "
          "another row, or read the rock-moved column as a metal content."),

 dict(q="Which observation would most strongly support a claim that a coal mine is "
        "contaminating the ground water near it?",
      choices=[
        "Wells nearer the mine carry much higher concentrations of a mine-related substance "
        "than wells farther away.",
        "Wells nearer the mine carry the same concentrations as wells farther away.",
        "The mine employs more people than any other business in the district.",
        "The mine produces more coal in winter than in summer.",
        "The coal from the mine is sold at a lower price than coal from other mines."],
      ans=0,
      why="EIN-2.L.1 states that the mining of coal can contaminate ground water, and a "
          "concentration gradient falling away from the mine is what a local source looks like "
          "in well data. Employment, seasonal output and price say nothing about the water."),

 dict(q="A district is told that its remaining coal can be reached only by working seams far "
        "below the surface. What does the framework predict about the coal from those "
        "seams?",
      choices=[
        "It will be very expensive to produce, because subsurface mining is what the "
        "framework calls very expensive.",
        "It will be cheaper to produce than the coal already taken from shallow seams.",
        "It will be produced at the same cost as the coal already taken.",
        "It cannot be produced at all, because the framework says deep coal is unreachable.",
        "It will be produced without any waste rock, because no overburden is removed."],
      ans=0,
      why="EIN-2.L.2 states that as easily accessible reserves run short it becomes necessary to "
          "access coal through subsurface mining, WHICH IS VERY EXPENSIVE. The framework says "
          "the deep coal is reached, not that it is unreachable."),

 dict(q="Using the record of the stripped and replanted site, what does the replanted row "
        "show about the recovery of the ground?",
      table=_T_STRIP,
      choices=[
        "Cover had returned to most but not all of its original level, and soil loss had "
        "fallen but remained above its original level.",
        "Cover and soil loss had both returned exactly to their original levels.",
        "Cover had returned to its original level but soil loss remained at its "
        "stripped level.",
        "Cover remained at its stripped level while soil loss returned to its "
        "original level.",
        "Cover and soil loss were both worse ten years after replanting than "
        "immediately after stripping."],
      ans=0,
      why="Ten years after replanting the cover reads 61 percent against 92 before mining and 4 "
          "when stripped, and the soil lost reads 9 tonnes per hectare against 2 before mining "
          "and 58 when stripped. Both are partway back rather than fully restored, which is "
          "what EIN-2.K.2's susceptibility to erosion leads a student to check."),

 dict(q="Which statement best relates the two learning objectives of this topic to "
        "each other?",
      choices=[
        "The first describes how ore is reached and what that requires; the second "
        "describes what the operation leaves behind and what it is worth.",
        "The first describes what the operation leaves behind; the second describes how "
        "ore is reached.",
        "Both describe only the wastes, and neither mentions any benefit.",
        "Both describe only the benefits, and neither mentions any waste.",
        "The two objectives describe different industries and cannot be applied to "
        "one mine."],
      ans=0,
      why="EIN-2.K covers extraction, with falling ore grade in EIN-2.K.1 and surface mining and "
          "overburden in EIN-2.K.2, while EIN-2.L covers ecological and economic impacts, with "
          "slag and tailings, the low cost energy and material, and the coal mining harms. The "
          "second objective carries both a cost and a benefit."),

 dict(q="Which summary states this topic as the framework does, without adding to it?",
      choices=[
        "Falling ore grades force more rock and energy per tonne of metal; surface mining "
        "strips overburden and vegetation; the wastes are overburden, slag and tailings; "
        "mining supplies low cost energy and materials; and deep coal is very expensive.",
        "Falling ore grades reduce the rock and energy needed per tonne of metal, and "
        "mining produces no waste worth naming.",
        "Surface mining leaves vegetation in place, and the only waste from mining is the "
        "metal that is not sold.",
        "Mining has no economic value, and the coal that remains is cheap to reach.",
        "Mining affects only the atmosphere and never the ground or the water."],
      ans=0,
      why="The keyed summary carries EIN-2.K.1's falling grades and rising resource use, "
          "EIN-2.K.2's overburden and stripped vegetation, EIN-2.L.1's wastes and its low cost "
          "energy and material, and EIN-2.L.2's expensive subsurface mining. Each rejected "
          "summary reverses a direction or drops a whole statement."),
]
