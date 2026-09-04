# AP ENVIRONMENTAL SCIENCE 8.9 Solid Waste Disposal
# CED effective Fall 2026, Unit 8 Aquatic and Terrestrial Pollution. Enduring
# understanding STB-3. Learning objectives STB-3.K (describe solid waste disposal
# methods) and STB-3.L (describe the effects of solid waste disposal methods). Suggested
# skill 7.D, use data and evidence to support a potential solution.
#
# Essential knowledge relied on, in the framework's own words:
#   STB-3.K.1  Solid waste is any discarded material that is not a liquid or gas. It is
#              generated in domestic, industrial, business, and agricultural sectors.
#   STB-3.K.2  Solid waste is most often disposed of in landfills. Landfills can
#              contaminate groundwater and release harmful gases.
#   STB-3.K.3  Electronic waste, or e-waste, is composed of discarded electronic devices
#              including televisions, cell phones, and computers.
#   STB-3.K.4  A sanitary municipal landfill consists of a bottom liner (plastic or clay),
#              a storm water collection system, a leachate collection system, a cap, and a
#              methane collection system.
#   STB-3.L.1  Factors in landfill decomposition include the composition of the trash and
#              conditions needed for microbial decomposition of the waste.
#   STB-3.L.2  Solid waste can also be disposed of through incineration, where waste is
#              burned at high temperatures. This method significantly reduces the volume
#              of solid waste but releases air pollutants.
#   STB-3.L.3  Some items are not accepted in sanitary landfills and may be disposed of
#              illegally, leading to environmental problems. One example is used rubber
#              tires, which when left in piles can become breeding grounds for mosquitoes
#              that can spread disease.
#   STB-3.L.4  Some countries dispose of their waste by dumping it in the ocean. This
#              practice, along with other sources of plastic, has led to large floating
#              islands of trash in the oceans. Additionally, wildlife can become entangled
#              in the waste, as well as ingest it.
#
# ON SCOPE. Topic 8.10 keys recycling, composting, e-waste reduction and landfill
# mitigation (STB-3.M.1 to STB-3.M.6). Nothing here keys a reduction method; this topic
# keys what solid waste is, where it goes, how a sanitary landfill is built, and what
# each disposal route does. Topic 8.2 keys litter's harm to aquatic wildlife under
# STB-3.B.8; item 23 here rests on STB-3.L.4's own wording about dumped waste.
#
# ON THE FIGURES. The bank carries no images, so every representation is a table and
# every keyed reading is recomputed in verify_e8_9.py from that table alone.
#
# NOT KEYED: no national waste statistic, no landfill lifetime, no emission limit and no
# named site. The framework states none of them.
#
# FIVE choices (A-E). No LaTeX and no non-ASCII.
TOPIC = ("8.9", "Solid Waste Disposal", 8)

_T_SECTORS = dict(
    headers=["Sector generating the waste",
             "Solid waste generated in one region each year (thousands of tons)"],
    rows=[["Domestic", "480"],
          ["Industrial", "1200"],
          ["Business", "350"],
          ["Agricultural", "900"]])

_T_WELLS = dict(
    headers=["Monitoring well", "Position relative to the landfill",
             "Chloride measured in the groundwater (milligrams per liter)"],
    rows=[["Well A", "upgradient of the whole site", "12"],
          ["Well B", "downgradient of the older unlined section", "240"],
          ["Well C", "downgradient of the section with a bottom liner and leachate "
                     "collection", "19"]])

_T_INCIN = dict(
    headers=["Batch of waste sent to the incinerator",
             "Volume of waste before burning (cubic meters)",
             "Volume of ash remaining after burning (cubic meters)",
             "Air pollutants released (kilograms)"],
    rows=[["Batch 1", "1000", "100", "45"],
          ["Batch 2", "800", "88", "36"],
          ["Batch 3", "1200", "108", "54"]])

_T_DECOMP = dict(
    headers=["Material buried in the same landfill",
             "Percent of the material decomposed after five years"],
    rows=[["Food scraps", "92"],
          ["Paper", "55"],
          ["Untreated wood", "20"],
          ["Plastic bottles", "1"],
          ["Glass bottles", "0"]])

_T_EWASTE = dict(
    headers=["Item brought to one collection day", "Number of items received"],
    rows=[["Televisions", "120"],
          ["Cell phones", "640"],
          ["Computers", "310"],
          ["Bags of yard clippings", "200"],
          ["Buckets of food scraps", "150"]])

_T_TIRES = dict(
    headers=["Site inspected", "Discarded tires left in the pile",
             "Mosquito larvae counted in a standard sample"],
    rows=[["Site 1", "0", "3"],
          ["Site 2", "40", "55"],
          ["Site 3", "300", "410"],
          ["Site 4", "900", "1180"]])

QUESTIONS = [

 dict(q="How does the framework define solid waste?",
      choices=[
        "Any discarded material that is not a liquid or a gas",
        "Any material that has been buried in a landfill, whatever its state",
        "Any liquid discarded by a household or a factory",
        "Any gas released during the burning of trash",
        "Any material that can be recycled into a new product"],
      ans=0,
      why="STB-3.K.1 states that solid waste is any discarded material that is not a "
          "liquid or gas. The definition turns on the state of the material rather than "
          "on where it ends up or on whether it can be recycled."),

 dict(q="In which sectors does the framework say solid waste is generated?",
      choices=[
        "Domestic, industrial, business and agricultural",
        "Domestic and industrial only",
        "Industrial and agricultural only",
        "Business and domestic only",
        "Only in sectors that operate their own landfills"],
      ans=0,
      why="STB-3.K.1 states that solid waste is generated in domestic, industrial, "
          "business and agricultural sectors. Each rejected option drops at least two of "
          "the four the framework names."),

 dict(q="Solid waste generated in one region is broken down by sector.",
      table=_T_SECTORS,
      choices=[
        "All four sectors the framework names appear here, and the industrial sector "
        "generates the largest amount in this region",
        "Only one of the sectors the framework names appears in this region",
        "The domestic sector generates the largest amount in this region",
        "The four sectors each generate the same amount in this region",
        "The agricultural sector generates the smallest amount in this region"],
      ans=0,
      why="The four row labels are the four sectors STB-3.K.1 names, and the industrial "
          "row carries the largest figure while the business row carries the smallest. "
          "The framework names the sectors without ranking them, so the ranking here "
          "comes from the table alone."),

 dict(q="Where does the framework say solid waste is most often disposed of?",
      choices=[
        "In landfills",
        "In incinerators",
        "In the ocean",
        "In compost piles",
        "In recycling plants"],
      ans=0,
      why="STB-3.K.2 states that solid waste is most often disposed of in landfills. "
          "Incineration and ocean dumping are described in STB-3.L.2 and STB-3.L.4 as "
          "other routes rather than as the most common one."),

 dict(q="Which two problems does the framework attribute to landfills?",
      choices=[
        "They can contaminate groundwater and release harmful gases",
        "They can cool the surrounding air and raise its humidity",
        "They can raise the salinity of nearby seawater and bleach coral",
        "They can thin the eggshells of birds and deform their young",
        "They can deplete stratospheric ozone and raise ultraviolet exposure"],
      ans=0,
      why="STB-3.K.2 states that landfills can contaminate groundwater and release "
          "harmful gases. The rejected options belong to other topics of the course and "
          "are not attributed to landfills anywhere in the framework."),

 dict(q="Groundwater around one landfill was sampled at three wells.",
      table=_T_WELLS,
      choices=[
        "The well below the unlined section is far more contaminated than the well below "
        "the section that has a bottom liner and leachate collection",
        "The well below the lined section is the most contaminated of the three",
        "All three wells carry the same concentration",
        "The upgradient well is the most contaminated of the three",
        "The wells below the landfill are cleaner than the well above it"],
      ans=0,
      why="The well below the unlined section carries a value more than ten times either "
          "of the others, while the well below the lined section is close to the "
          "upgradient value. STB-3.K.2 states that landfills can contaminate groundwater "
          "and STB-3.K.4 lists a bottom liner and a leachate collection system among the "
          "parts of a sanitary municipal landfill."),

 dict(q="Which set of components does the framework list for a sanitary municipal "
        "landfill?",
      choices=[
        "A bottom liner, a storm water collection system, a leachate collection system, a "
        "cap and a methane collection system",
        "A bottom liner and a cap only",
        "A smokestack, a furnace and an ash pit",
        "A settling tank, an aeration basin and a disinfection stage",
        "A conveyor, a shredder and a magnet for separating metals"],
      ans=0,
      why="STB-3.K.4 lists exactly those five components for a sanitary municipal "
          "landfill. The rejected options describe an incinerator, a sewage treatment "
          "plant and a materials recovery line, none of which the framework attributes to "
          "a landfill."),

 dict(q="What does the framework say electronic waste is composed of?",
      choices=[
        "Discarded electronic devices including televisions, cell phones and computers",
        "Discarded food scraps, paper and yard waste",
        "Discarded rubber tires left in piles",
        "Discarded plastic that has reached the open ocean",
        "Discarded liquids from industrial processes"],
      ans=0,
      why="STB-3.K.3 states that electronic waste, or e-waste, is composed of discarded "
          "electronic devices including televisions, cell phones and computers. Food "
          "scraps and yard waste belong to STB-3.M.3, tires to STB-3.L.3 and ocean "
          "plastic to STB-3.L.4."),

 dict(q="Three batches of waste were measured before and after incineration.",
      table=_T_INCIN,
      choices=[
        "The volume remaining after burning is about a tenth of the volume before it in "
        "every batch, and air pollutants were released in every batch",
        "The volume remaining after burning is larger than the volume before it",
        "Burning left the volume unchanged in every batch",
        "No air pollutants were released by any of the three batches",
        "The batch with the largest starting volume left the smallest amount of ash"],
      ans=0,
      why="Dividing each batch's ash volume by its starting volume gives about one tenth "
          "in every case, and every row carries a positive figure for air pollutants "
          "released. STB-3.L.2 states that incineration significantly reduces the volume "
          "of solid waste but releases air pollutants."),

 dict(q="What benefit and what drawback does the framework attach to incineration?",
      choices=[
        "It significantly reduces the volume of solid waste but releases air pollutants",
        "It significantly increases the volume of solid waste but produces no emissions",
        "It removes the need for any disposal site and releases only water vapor",
        "It converts waste into drinking water but consumes large amounts of land",
        "It has no effect on volume and no effect on air quality"],
      ans=0,
      why="STB-3.L.2 states that incineration burns waste at high temperatures, which "
          "significantly reduces the volume of solid waste but releases air pollutants. "
          "Each rejected option denies one half of that trade or invents an outcome."),

 dict(q="Which factors does the framework name as affecting decomposition in a landfill?",
      choices=[
        "The composition of the trash and the conditions needed for microbial "
        "decomposition",
        "The color of the bags the trash is placed in",
        "The distance from the landfill to the nearest city",
        "The number of trucks delivering to the site each day",
        "The height of the fence around the site"],
      ans=0,
      why="STB-3.L.1 states that factors in landfill decomposition include the "
          "composition of the trash and conditions needed for microbial decomposition of "
          "the waste. Bag color, distance, truck counts and fencing appear nowhere in the "
          "framework."),

 dict(q="What example does the framework give of an item that may be disposed of "
        "illegally, and what problem does it name?",
      choices=[
        "Used rubber tires, which when left in piles can become breeding grounds for "
        "mosquitoes that spread disease",
        "Used paper, which when left in piles blocks sunlight from reaching plants",
        "Used glass, which when left in piles raises the temperature of the soil",
        "Used food scraps, which when left in piles produce fertilizer for farmers",
        "Used clothing, which when left in piles absorbs rainfall and prevents flooding"],
      ans=0,
      why="STB-3.L.3 names used rubber tires as an example of an item not accepted in "
          "sanitary landfills that may be disposed of illegally, and states that piles of "
          "them can become breeding grounds for mosquitoes that can spread disease."),

 dict(q="Five materials buried in the same landfill were examined after five years.",
      table=_T_DECOMP,
      choices=[
        "How much a material decomposes depends strongly on what the material is, since "
        "the values run from almost complete decay to almost none",
        "All five materials decomposed to the same extent",
        "The plastic and glass decomposed more completely than the food scraps",
        "None of the five materials decomposed at all",
        "Every material buried in a landfill decomposes completely within five years"],
      ans=0,
      why="The values span nearly the whole range from complete to no decomposition "
          "across five materials in the same landfill, so the material itself is what "
          "differs. STB-3.L.1 names the composition of the trash as a factor in landfill "
          "decomposition."),

 dict(q="What does the framework say has resulted from countries dumping waste in the "
        "ocean, together with other sources of plastic?",
      choices=[
        "Large floating islands of trash in the oceans, with wildlife becoming entangled "
        "in the waste and ingesting it",
        "A permanent rise in the number of fish species in the open ocean",
        "A fall in sea level as the waste displaces water",
        "The complete breakdown of the waste into harmless minerals within a year",
        "A rise in the dissolved oxygen of the surface ocean"],
      ans=0,
      why="STB-3.L.4 states that ocean dumping, along with other sources of plastic, has "
          "led to large floating islands of trash in the oceans, and that wildlife can "
          "become entangled in the waste as well as ingest it."),

 dict(q="Which component of a sanitary municipal landfill is placed to keep liquid from "
        "moving out of the base of the site into the ground below?",
      choices=[
        "The bottom liner of plastic or clay",
        "The cap placed over the top of the site",
        "The methane collection system",
        "The storm water collection system",
        "The fence around the perimeter of the site"],
      ans=0,
      why="STB-3.K.4 lists a bottom liner of plastic or clay among the components of a "
          "sanitary municipal landfill, and it is the component that sits beneath the "
          "waste. STB-3.K.2 states that landfills can contaminate groundwater, which is "
          "the problem a base barrier addresses."),

 dict(q="Which framework statement explains why a sanitary municipal landfill includes a "
        "system for collecting methane?",
      choices=[
        "Landfills can release harmful gases, and a collection system captures gas that "
        "would otherwise escape",
        "Landfills can contaminate groundwater, and methane collection cleans the water",
        "Methane is a liquid and therefore is not solid waste",
        "Methane collection replaces the need for a bottom liner",
        "Methane is added to the landfill to speed the decomposition of glass"],
      ans=0,
      why="STB-3.K.2 states that landfills can release harmful gases and STB-3.K.4 lists "
          "a methane collection system among the components of a sanitary municipal "
          "landfill, so the component matches the stated problem."),

 dict(q="Items received at one collection day are listed.",
      table=_T_EWASTE,
      choices=[
        "The televisions, cell phones and computers together outnumber the remaining items "
        "received",
        "The remaining items outnumber the televisions, cell phones and computers",
        "Every item on the list is electronic waste as the framework describes it",
        "None of the items on the list is electronic waste as the framework describes it",
        "The cell phones alone outnumber all the other items combined"],
      ans=0,
      why="STB-3.K.3 names televisions, cell phones and computers as electronic waste, "
          "and the sum of those three rows exceeds the sum of the two rows of yard "
          "clippings and food scraps. Yard waste and food scraps are the organic material "
          "of STB-3.M.3 rather than electronic devices."),

 dict(q="Which of the following would NOT be solid waste under the framework's "
        "definition?",
      choices=[
        "Used oil drained from an engine and poured into a drum",
        "A broken television set left at the curb",
        "A worn out rubber tire removed from a truck",
        "A cracked glass bottle thrown into a bin",
        "Yard clippings raked up and bagged"],
      ans=0,
      why="STB-3.K.1 defines solid waste as any discarded material that is not a liquid "
          "or gas, and used oil is a liquid. The four rejected items are all discarded "
          "materials in the solid state."),

 dict(q="What is the purpose of the storm water collection system the framework lists for "
        "a sanitary municipal landfill?",
      choices=[
        "To manage the rainfall that runs off the site so it does not carry contamination "
        "away with it",
        "To supply water to the landfill so the waste decomposes faster",
        "To collect the methane produced inside the waste",
        "To replace the leachate collection system when it fails",
        "To cool the waste so that it cannot catch fire"],
      ans=0,
      why="STB-3.K.4 lists a storm water collection system among the components of a "
          "sanitary municipal landfill, and STB-3.K.2 names groundwater contamination as "
          "a landfill problem, so managing water moving through and off the site is what "
          "the component addresses. Methane has its own listed system."),

 dict(q="Why does the framework describe incineration as reducing the volume of waste "
        "rather than eliminating the waste problem?",
      choices=[
        "Burning leaves a much smaller amount of material behind and sends air pollutants "
        "into the atmosphere, so the waste is transformed rather than erased",
        "Burning creates more solid waste than it consumes",
        "Burning converts all of the waste into clean drinking water",
        "Burning has no effect on the amount of material remaining",
        "Burning removes the need for any air quality regulation"],
      ans=0,
      why="STB-3.L.2 states that incineration significantly reduces the volume of solid "
          "waste but releases air pollutants, so it changes the form and location of the "
          "problem rather than removing it."),

 dict(q="Four sites with different numbers of discarded tires were inspected.",
      table=_T_TIRES,
      choices=[
        "The more tires left at a site, the more mosquito larvae were counted there",
        "The more tires left at a site, the fewer mosquito larvae were counted there",
        "The same number of larvae was counted at every site",
        "The site with no tires had the most larvae",
        "The number of tires tells nothing about the larvae counted in these data"],
      ans=0,
      why="Ranking the sites by the number of tires gives the same order as ranking them "
          "by the larvae counted. STB-3.L.3 states that used rubber tires left in piles "
          "can become breeding grounds for mosquitoes that can spread disease."),

 dict(q="A town proposes to line and cap a landfill that currently has neither. Which "
        "evidence would most directly support that proposal?",
      choices=[
        "Groundwater sampled below the unlined part of the site is far more contaminated "
        "than groundwater sampled below a lined part",
        "The town's population has grown over the past decade",
        "The landfill is located beside a highway",
        "The landfill accepts waste from four different sectors",
        "The town owns the land the landfill sits on"],
      ans=0,
      why="STB-3.K.2 names groundwater contamination as a landfill problem and STB-3.K.4 "
          "lists a bottom liner and a cap among the components of a sanitary municipal "
          "landfill, so a measured difference between lined and unlined ground is the "
          "evidence that bears on the proposal."),

 dict(q="Which harms to wildlife does the framework attribute to waste that reaches the "
        "ocean?",
      choices=[
        "Becoming entangled in the waste and ingesting it",
        "Being poisoned by the salt released from the waste",
        "Being deafened by the noise the floating waste makes",
        "Being deprived of sunlight by the waste sinking to the seafloor",
        "Being warmed by heat released from the waste"],
      ans=0,
      why="STB-3.L.4 states that wildlife can become entangled in the waste as well as "
          "ingest it. The framework names no salt, noise, shading or heating effect for "
          "ocean waste in this statement."),

 dict(q="Why does the framework connect illegal disposal to items that sanitary landfills "
        "do not accept?",
      choices=[
        "An item a landfill will not take has to go somewhere, and dumping it outside a "
        "regulated site is what leads to the problems the framework describes",
        "Items that landfills refuse are always harmless wherever they end up",
        "Landfills refuse only items that decompose within a year",
        "Illegal disposal is described as cheaper but otherwise identical to landfilling",
        "The framework states that every item is accepted at a sanitary landfill"],
      ans=0,
      why="STB-3.L.3 states that some items are not accepted in sanitary landfills and "
          "may be disposed of illegally, leading to environmental problems, and gives "
          "tire piles breeding mosquitoes as its example."),

 dict(q="A community finds a landfill contaminant in its wells and asks which part of a "
        "sanitary municipal landfill was most likely missing. Which answer follows from "
        "the framework's list?",
      choices=[
        "The bottom liner together with the leachate collection system, since those are "
        "the parts that keep liquid from moving down out of the waste",
        "The methane collection system, since that is the part that keeps liquid out of "
        "the ground",
        "The cap, since a cap is what stops gas from escaping into the air",
        "The storm water collection system, since that is the part that captures methane",
        "None of the listed parts, since the framework says landfills cannot affect "
        "groundwater"],
      ans=0,
      why="STB-3.K.4 lists a bottom liner and a leachate collection system as separate "
          "components, and STB-3.K.2 states that landfills can contaminate groundwater. "
          "Each rejected option attaches a listed component to the wrong function or "
          "denies the stated problem."),

 dict(q="Two identical loads of the same material are buried in landfills that differ in "
        "moisture and temperature, and they decompose at different rates. Which framework "
        "statement covers that difference?",
      choices=[
        "Factors in landfill decomposition include the conditions needed for microbial "
        "decomposition of the waste",
        "Solid waste is any discarded material that is not a liquid or gas",
        "Incineration significantly reduces the volume of solid waste",
        "Electronic waste is composed of discarded electronic devices",
        "Wildlife can become entangled in waste dumped in the ocean"],
      ans=0,
      why="STB-3.L.1 names both the composition of the trash and the conditions needed "
          "for microbial decomposition as factors, and with the material held constant it "
          "is the conditions that remain. The rejected statements address definitions and "
          "other disposal routes."),

 dict(q="Which pairing of a disposal route with a framework consequence is correct?",
      choices=[
        "Landfilling, paired with the possibility of contaminated groundwater and the "
        "release of harmful gases",
        "Landfilling, paired with the release of large floating islands of trash into the "
        "open ocean",
        "Incineration, paired with an increase in the volume of solid waste",
        "Ocean dumping, paired with the capture of methane for electricity",
        "Incineration, paired with the breeding of mosquitoes in tire piles"],
      ans=0,
      why="STB-3.K.2 attaches groundwater contamination and harmful gas release to "
          "landfills, STB-3.L.2 attaches volume reduction and air pollutants to "
          "incineration, STB-3.L.4 attaches floating trash to ocean dumping and STB-3.L.3 "
          "attaches mosquitoes to tire piles. Each rejected pairing crosses two of those."),

 dict(q="Which measurement would best support a claim that a landfill is releasing gas to "
        "the atmosphere?",
      choices=[
        "The concentration of methane measured in the air at and around the surface of the "
        "site",
        "The number of trucks entering the site each week",
        "The depth of the waste beneath the surface of the site",
        "The chloride concentration in a well downgradient of the site",
        "The area of the site measured from a map"],
      ans=0,
      why="STB-3.K.2 states that landfills can release harmful gases, so a gas measured "
          "in the air is the direct evidence. A well concentration bears on the "
          "groundwater half of that statement, and truck counts, depth and area measure "
          "the site rather than an emission."),

 dict(q="A city must choose between expanding its landfill and building an incinerator. "
        "Which pair of measurements bears most directly on the framework's account of the "
        "two routes?",
      choices=[
        "The volume of waste each route would leave behind and the air pollutants each "
        "would release",
        "The number of employees each route would require and the color of each facility",
        "The distance from the city center to each site and the age of the city's trucks",
        "The number of sectors generating the city's waste and the size of its recycling "
        "bins",
        "The depth of the groundwater beneath each site and the price of scrap metal"],
      ans=0,
      why="STB-3.L.2 states the trade for incineration as a large reduction in volume "
          "against the release of air pollutants, and STB-3.K.2 names groundwater and gas "
          "problems for landfills, so volume left behind and pollutants released are the "
          "quantities the comparison turns on."),

 dict(q="Which summary best captures this topic?",
      choices=[
        "Discarded material that is not a liquid or gas comes from several sectors and "
        "goes most often to landfills, which are built with liners, collection systems and "
        "a cap because they can contaminate groundwater and release gases, while "
        "incineration cuts volume but pollutes the air and illegal dumping and ocean "
        "dumping create their own harms",
        "Solid waste includes liquids and gases and is disposed of almost entirely by "
        "incineration, which releases nothing into the air",
        "Landfills have no effect on groundwater or air, so no engineered components are "
        "needed",
        "Ocean dumping is the framework's recommended disposal method because the waste "
        "breaks down quickly at sea",
        "All materials buried in a landfill decompose at the same rate, so the composition "
        "of the trash does not matter"],
      ans=0,
      why="Each clause of the keyed summary is one of STB-3.K.1 through STB-3.L.4. Every "
          "rejected summary contradicts the definition, denies a stated landfill problem, "
          "recommends a practice the framework describes as harmful, or denies the role "
          "of trash composition."),
]
