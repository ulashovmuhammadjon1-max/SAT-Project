# AP ENVIRONMENTAL SCIENCE 8.4 Human Impacts on Wetlands and Mangroves
# CED effective Fall 2026, Unit 8 Aquatic and Terrestrial Pollution. Enduring
# understanding STB-3. Learning objective STB-3.E: describe the impacts of human
# activity on wetlands and mangroves. Suggested skill 7.B, describe potential responses
# or approaches to environmental problems.
#
# Essential knowledge relied on, in the framework's own words:
#   STB-3.E.1  Wetlands are areas where water covers the soil, either part or all of
#              the time.
#   STB-3.E.2  Wetlands provide a variety of ecological services, including water
#              purification, flood protection, water filtration, and habitat.
#   STB-3.E.3  Threats to wetlands and mangroves include commercial development, dam
#              construction, overfishing, and pollutants from agriculture and
#              industrial waste.
#
# ON MANGROVES, WHICH MATTERS FOR HONESTY HERE. The framework mentions mangroves in
# exactly one place, STB-3.E.3, and only as sharing the same list of threats. It states
# no service, no definition and no distinctive property for them. So no key in this
# module attributes a service to mangroves specifically -- not storm buffering, not
# nursery habitat, not carbon storage -- and every mangrove item keys a threat from
# that list.
#
# ON THE SERVICES. STB-3.E.2 lists water purification, flood protection, water
# filtration, and habitat. The framework prints purification and filtration as separate
# entries and draws no distinction between them, so no item here asks a student to tell
# the two apart.
#
# ON WHAT IS NOT KEYED. No statute, permit, mitigation ratio, area figure or named
# wetland. Every number belongs to the study in its own table and is recomputed in
# verify_e8_4.py.
#
# FIVE choices (A-E). No LaTeX and no non-ASCII.
TOPIC = ("8.4", "Human Impacts on Wetlands and Mangroves", 8)

_T_FILTER = dict(
    headers=["Sampling point along the flow path",
             "Nitrate in the water (milligrams per liter)",
             "Suspended sediment (milligrams per liter)"],
    rows=[["Entering the wetland", "9.0", "150"],
          ["Halfway across the wetland", "5.2", "70"],
          ["Leaving the wetland", "2.1", "25"]])

_T_FLOOD = dict(
    headers=["Catchment", "Wetland remaining in the catchment (percent of original)",
             "Peak river height after a comparable storm (meters)"],
    rows=[["Catchment 1", "90", "2.1"],
          ["Catchment 2", "55", "3.0"],
          ["Catchment 3", "20", "4.2"],
          ["Catchment 4", "5", "5.1"]])

_T_LOSS = dict(
    headers=["Cause of wetland loss recorded in one region",
             "Area lost over 30 years (square kilometers)"],
    rows=[["Commercial development", "420"],
          ["Dam construction and altered river flow", "260"],
          ["Pollutants from agriculture and industrial waste", "180"],
          ["Other recorded causes", "40"]])

_T_HABITAT = dict(
    headers=["Site", "Wetland area remaining (square kilometers)",
             "Waterbird species recorded", "Fish species recorded"],
    rows=[["Site 1", "48", "62", "31"],
          ["Site 2", "26", "45", "24"],
          ["Site 3", "11", "28", "15"],
          ["Site 4", "3", "12", "7"]])

_T_RESTORE = dict(
    headers=["Stage of one restoration project",
             "Wetland area (square kilometers)",
             "Nitrate leaving the site (milligrams per liter)"],
    rows=[["Before restoration", "2", "8.4"],
          ["Three years after restoration", "9", "4.6"],
          ["Eight years after restoration", "14", "2.7"]])

_T_MANGROVE = dict(
    headers=["Coastal section", "Mangrove cleared for development (percent)",
             "Mangrove area remaining (hectares)"],
    rows=[["Section 1", "10", "900"],
          ["Section 2", "35", "650"],
          ["Section 3", "60", "400"],
          ["Section 4", "85", "150"]])

QUESTIONS = [

 dict(q="How does the framework define a wetland?",
      choices=[
        "An area where water covers the soil, either part or all of the time",
        "An area that is permanently underwater and never dries",
        "An area of open ocean within sight of the shore",
        "An area of dry land that receives more rain than average",
        "An area where groundwater lies more than fifty meters below the surface"],
      ans=0,
      why="The framework defines a wetland as an area where water covers the soil, "
          "either part or all of the time. Permanent inundation is only one of the two "
          "cases it allows, and open ocean, dry land and deep groundwater are none of "
          "them."),

 dict(q="Which ecological services does the framework attribute to wetlands?",
      choices=[
        "Water purification, flood protection, water filtration, and habitat",
        "Electricity generation, mineral extraction, and shipping access",
        "Timber production and grazing land",
        "Radon removal from the atmosphere",
        "Reduction of noise from urban transportation"],
      ans=0,
      why="Those four are the ecological services the framework lists for wetlands. The "
          "rejected options are economic uses or effects belonging to other parts of the "
          "course rather than services the framework attributes to wetlands."),

 dict(q="Which threats to wetlands and mangroves does the framework name?",
      choices=[
        "Commercial development, dam construction, overfishing, and pollutants from "
        "agriculture and industrial waste",
        "Stratospheric ozone depletion and increased ultraviolet radiation",
        "Thermal inversions trapping smog above the coast",
        "Noise from shipping and construction",
        "The natural succession of forest into grassland"],
      ans=0,
      why="Those four are exactly the threats the framework lists for wetlands and "
          "mangroves. Ozone depletion, thermal inversion, noise and succession are "
          "treated in other topics and are not named as threats here."),

 dict(q="Water is sampled as it moves through a wetland.",
      table=_T_FILTER,
      choices=[
        "Both nitrate and suspended sediment are lower where the water leaves the wetland "
        "than where it enters",
        "Both measurements are higher where the water leaves the wetland",
        "Nitrate falls across the wetland but sediment rises",
        "Neither measurement changes across the wetland",
        "The measurements are highest halfway across the wetland"],
      ans=0,
      why="Each column falls at every step from the inflow to the outflow, so the water "
          "leaves carrying less of both. Water purification and water filtration are "
          "among the ecological services the framework attributes to wetlands."),

 dict(q="Catchments with different amounts of remaining wetland are compared after "
        "comparable storms.",
      table=_T_FLOOD,
      choices=[
        "The catchments retaining more wetland recorded lower peak river heights",
        "The catchments retaining more wetland recorded higher peak river heights",
        "Peak river height was the same in all four catchments",
        "The catchment with the least wetland recorded the lowest peak",
        "Wetland area and peak river height are unrelated in these data"],
      ans=0,
      why="Ordering the catchments by remaining wetland puts the peak river heights in "
          "the opposite order, so more wetland goes with a lower peak. Flood protection "
          "is one of the ecological services the framework lists for wetlands."),

 dict(q="Recorded causes of wetland loss in one region are shown.",
      table=_T_LOSS,
      choices=[
        "Commercial development accounts for more of the recorded loss than any other "
        "single cause listed",
        "Pollutants from agriculture and industrial waste account for more of the loss "
        "than any other cause listed",
        "The four causes account for equal areas of loss",
        "Dam construction accounts for the smallest area of the causes listed",
        "None of the causes listed appears in the framework's list of threats"],
      ans=0,
      why="The largest area in the table belongs to commercial development, and the "
          "other named rows are smaller. Commercial development, dam construction and "
          "pollutants from agriculture and industrial waste are three of the four "
          "threats the framework lists."),

 dict(q="Which of the following is the clearest example of the habitat service the "
        "framework attributes to wetlands?",
      choices=[
        "The wetland supports populations of birds, fish and other animals that live and "
        "breed there",
        "The wetland stores water that is later pumped for irrigation",
        "The wetland provides a route for boats to reach the sea",
        "The wetland yields peat that is dug and burned as fuel",
        "The wetland reflects sunlight back to space"],
      ans=0,
      why="Habitat is one of the four ecological services the framework lists, and "
          "habitat means the place where organisms live. Water supply for irrigation, "
          "navigation, fuel extraction and reflection are not among the services it "
          "names."),

 dict(q="Bird and fish counts are compared across sites with different amounts of "
        "remaining wetland.",
      table=_T_HABITAT,
      choices=[
        "Both the number of waterbird species and the number of fish species fall as the "
        "remaining wetland area falls",
        "Both counts rise as the remaining wetland area falls",
        "The site with the least wetland records the most species of both kinds",
        "The two counts are the same at all four sites",
        "Wetland area is related to the bird count but not to the fish count"],
      ans=0,
      why="Both species counts decrease at every step as the remaining area decreases. "
          "Habitat is one of the ecological services the framework attributes to "
          "wetlands, so a loss of area is expected to bear on the species a wetland "
          "supports."),

 dict(q="A developer proposes to drain a wetland and build on the site. Which framework "
        "threat does the proposal represent?",
      choices=[
        "Commercial development",
        "Dam construction",
        "Overfishing",
        "Pollutants from agriculture",
        "Industrial waste discharged upstream"],
      ans=0,
      why="Draining a wetland to build on the site is commercial development, which is "
          "the first threat in the framework's list. The other options are the remaining "
          "threats it names and describe different activities."),

 dict(q="A dam upstream of a coastal wetland changes the amount and timing of the fresh "
        "water and sediment reaching it. Which framework threat does this illustrate?",
      choices=[
        "Dam construction",
        "Commercial development of the wetland itself",
        "Overfishing within the wetland",
        "Noise pollution from transportation",
        "Thermal pollution from a power station"],
      ans=0,
      why="Dam construction is one of the four threats to wetlands and mangroves the "
          "framework names. Building on the wetland and removing too many fish are "
          "separate items in the same list, and the last two options belong to other "
          "topics."),

 dict(q="Which response to wetland loss follows most directly from the services the "
        "framework attributes to wetlands?",
      choices=[
        "Restoring drained areas so that water again covers the soil and the site can "
        "filter water, hold floodwater and provide habitat",
        "Replacing the wetland with a paved surface that drains quickly",
        "Deepening the channel so that water passes through the area faster",
        "Filling the wetland and planting a lawn",
        "Building a wall around the wetland so that no water can enter it"],
      ans=0,
      why="Suggested skill 7.B. The services the framework names depend on water "
          "covering the soil, so restoring that condition is what could restore them. "
          "Paving, deepening, filling and excluding water all remove the condition the "
          "definition requires."),

 dict(q="A restoration project is monitored over eight years.",
      table=_T_RESTORE,
      choices=[
        "As the restored area grew, the nitrate leaving the site fell",
        "As the restored area grew, the nitrate leaving the site rose",
        "The restored area shrank over the eight years",
        "The nitrate leaving the site was unchanged throughout",
        "The largest nitrate value was recorded eight years after restoration"],
      ans=0,
      why="The area increases at every stage while the nitrate leaving the site "
          "decreases at every stage. Water purification and filtration are among the "
          "services the framework attributes to wetlands."),

 dict(q="Coastal sections with different amounts of mangrove clearing are compared.",
      table=_T_MANGROVE,
      choices=[
        "The sections where more mangrove was cleared for development retain less "
        "mangrove area",
        "The sections where more mangrove was cleared retain more mangrove area",
        "All four sections retain the same mangrove area",
        "The section with the most clearing retains the largest area",
        "Clearing and remaining area are unrelated in these data"],
      ans=0,
      why="Ordering the sections by the share cleared puts the remaining area in the "
          "opposite order. Commercial development is one of the threats the framework "
          "names for wetlands and mangroves alike."),

 dict(q="Why does the framework's definition of a wetland allow for areas that are dry "
        "for part of the year?",
      choices=[
        "The definition covers areas where water covers the soil either part or all of "
        "the time",
        "The definition requires water to be present continuously",
        "The definition applies only to coastal areas",
        "The definition applies only to areas with trees",
        "The definition depends on the depth of the water rather than its presence"],
      ans=0,
      why="The framework's own wording is either part or all of the time, so seasonal "
          "inundation falls inside the definition. Depth, tree cover and coastal position "
          "are not part of it."),

 dict(q="Which of the following would most directly reduce the threat the framework "
        "describes as pollutants from agriculture reaching a wetland?",
      choices=[
        "Reducing the fertilizer and pesticide carried in runoff from the fields draining "
        "into the wetland",
        "Increasing the number of boats using the wetland",
        "Deepening the drainage ditches that carry runoff into the wetland",
        "Removing the vegetation between the fields and the wetland",
        "Building housing at the edge of the wetland"],
      ans=0,
      why="Suggested skill 7.B. The threat named is pollutants from agriculture, so the "
          "response that addresses it is a reduction in what the runoff carries. The "
          "other options increase traffic, speed delivery of runoff, or add a second "
          "threat from the same list."),

 dict(q="A town relies on a wetland to slow and store water during storms. Which "
        "framework service does that use depend on?",
      choices=[
        "Flood protection",
        "Water purification",
        "Habitat",
        "Water filtration",
        "Timber production"],
      ans=0,
      why="Slowing and storing storm water is flood protection, which the framework "
          "lists among the ecological services wetlands provide. Purification, filtration "
          "and habitat are the other services in that list, and timber production is not "
          "in it at all."),

 dict(q="Which of the following best explains why removing a wetland can raise flood "
        "peaks downstream even though the wetland itself produced no water?",
      choices=[
        "The wetland had been providing flood protection by holding water that now moves "
        "downstream instead",
        "The wetland had been generating rainfall over the catchment",
        "The wetland had been pumping water back into the ground below the river",
        "The wetland had been raising the temperature of the water",
        "The wetland had been adding sediment to the river channel"],
      ans=0,
      why="Flood protection is one of the ecological services the framework attributes "
          "to wetlands, so losing the wetland removes that service. The framework does "
          "not have wetlands generate rain, pump water underground, warm water, or "
          "supply sediment."),

 dict(q="Which of the following pairs a framework threat with a matching response?",
      choices=[
        "Overfishing, and limiting the catch taken from the wetland",
        "Overfishing, and draining part of the wetland for building",
        "Dam construction, and deepening the shipping channel through the wetland",
        "Commercial development, and increasing fertilizer use upstream",
        "Industrial waste, and clearing the mangroves along the shore"],
      ans=0,
      why="Suggested skill 7.B. Overfishing is one of the framework's four threats, and "
          "limiting the catch addresses that threat directly. Every rejected pairing "
          "answers a threat with another item from the same list of threats."),

 dict(q="Why does the framework treat commercial development and dam construction as "
        "threats even though neither releases a pollutant into the wetland?",
      choices=[
        "Both are named as threats to wetlands and mangroves alongside the pollutants, so "
        "a wetland can be lost or altered without being contaminated",
        "Both release pollutants that the framework does not name",
        "Neither is actually a threat according to the framework",
        "Both threaten only mangroves and never wetlands",
        "Both are responses to environmental problems rather than threats"],
      ans=0,
      why="The framework's list contains commercial development, dam construction, "
          "overfishing, and pollutants from agriculture and industrial waste together, so "
          "physical loss and alteration sit alongside contamination as threats to the "
          "same systems."),

 dict(q="An area is flooded for three months each spring and dry for the rest of the "
        "year. How does the framework's definition classify it?",
      choices=[
        "As a wetland, since water covers the soil for part of the time",
        "As a wetland only if the flooding lasts all year",
        "As open water rather than a wetland",
        "As dry land, since it is dry for most of the year",
        "The definition cannot be applied without knowing the depth of the water"],
      ans=0,
      why="The framework's definition covers areas where water covers the soil either "
          "part or all of the time, so seasonal flooding qualifies. The definition sets "
          "no minimum duration and mentions no depth."),

 dict(q="A proposal would convert part of a mangrove shoreline to ponds and buildings. "
        "Which framework statement bears most directly on the proposal?",
      choices=[
        "Threats to wetlands and mangroves include commercial development",
        "Wetlands provide water purification and filtration",
        "Wetlands are areas where water covers the soil part or all of the time",
        "Oceanic dead zones are caused by increased nutrient pollution",
        "Heavy metals from industry can reach groundwater"],
      ans=0,
      why="The framework names mangroves only in its list of threats, and converting "
          "mangrove shoreline to ponds and buildings is commercial development, the "
          "first threat in that list. The service and definition statements are written "
          "about wetlands, and the last two options belong to other topics."),

 dict(q="Which measurement would best show that a wetland is providing the water "
        "purification and filtration services the framework describes?",
      choices=[
        "Concentrations of pollutants measured in the water entering the wetland and in "
        "the water leaving it",
        "The number of visitors to the wetland each year",
        "The area of the wetland in square kilometers",
        "The number of bird species recorded in the wetland",
        "The depth of the water at the center of the wetland"],
      ans=0,
      why="Purification and filtration are changes to the water as it passes through, so "
          "the paired inflow and outflow measurement is what shows them. Visitors, area, "
          "bird counts and depth measure something other than the change in water "
          "quality."),

 dict(q="Which of the following would be evidence that overfishing is affecting a "
        "wetland, as opposed to another threat on the framework's list?",
      choices=[
        "Catch records showing many more fish removed each year than in the past, "
        "alongside falling fish numbers, while the wetland area is unchanged",
        "Records showing that new buildings now cover part of the wetland",
        "Records showing that a dam has changed the water reaching the wetland",
        "Measurements showing high fertilizer concentrations in the inflowing water",
        "Photographs showing the wetland is smaller than it once was"],
      ans=0,
      why="Overfishing is the removal of too many fish, so the evidence for it concerns "
          "the catch and the fish population with the habitat unchanged. Each rejected "
          "option is evidence for one of the framework's other three threats."),

 dict(q="A restoration plan proposes to reconnect a drained wetland to its river and "
        "allow it to flood again. Which framework idea best justifies the plan?",
      choices=[
        "Wetlands are areas where water covers the soil, and they provide purification, "
        "flood protection, filtration and habitat",
        "Wetlands are threatened only by pollutants, so restoring water flow is "
        "irrelevant",
        "Wetlands provide no ecological services once they have been drained for any "
        "length of time",
        "Wetlands can be replaced by any body of open water",
        "Wetlands are defined by their vegetation rather than by the presence of water"],
      ans=0,
      why="Suggested skill 7.B. Restoring the flooding restores the condition in the "
          "framework's definition, and the services it lists belong to wetlands so "
          "defined. The framework does not limit the threats to pollutants or make the "
          "services unrecoverable."),

 dict(q="A landowner argues that a wetland has no value because nothing is grown or "
        "built on it. Which framework statement most directly answers the argument?",
      choices=[
        "Wetlands provide ecological services including water purification, flood "
        "protection, water filtration, and habitat",
        "Wetlands are areas where water covers the soil part or all of the time",
        "Threats to wetlands include dam construction",
        "Litter in aquatic ecosystems creates choking hazards for wildlife",
        "Heavy metals from mining can reach the groundwater"],
      ans=0,
      why="The argument is about value, and the framework's answer is the list of "
          "ecological services wetlands provide. The definition and the threat list "
          "describe what a wetland is and what endangers it rather than what it does."),

 dict(q="Two adjacent catchments lose wetland at different rates. Which measurement "
        "would best test whether the loss is affecting water quality downstream?",
      choices=[
        "Pollutant concentrations measured downstream in both catchments over the same "
        "period, alongside the wetland area remaining in each",
        "The number of residents in each catchment",
        "The height of the tallest building in each catchment",
        "The number of roads crossing each catchment",
        "The average summer temperature of each catchment"],
      ans=0,
      why="Testing the effect requires the outcome and the wetland area to be measured "
          "together across the two catchments over the same period. Population, building "
          "height, road counts and temperature measure neither the wetland nor the water "
          "quality."),

 dict(q="Which statement best describes the relationship between the framework's "
        "definition of a wetland and the services it lists?",
      choices=[
        "The services are provided by areas where water covers the soil, so losing that "
        "condition puts the services at risk",
        "The services are provided only where water is present all year",
        "The services are unrelated to whether water covers the soil",
        "The services are provided by dry land as readily as by wetland",
        "The services depend on the wetland being open to boat traffic"],
      ans=0,
      why="The framework defines wetlands by water covering the soil part or all of the "
          "time and attributes the services to wetlands so defined, which ties the "
          "services to that condition. It does not require year-round water or make the "
          "services independent of it."),

 dict(q="A regional plan proposes to protect remaining wetlands and mangroves by "
        "addressing the framework's list of threats. Which set of measures matches that "
        "list most completely?",
      choices=[
        "Limits on building in wetland areas, review of dam projects, limits on fishing, "
        "and controls on agricultural and industrial pollutants",
        "Limits on building only",
        "Controls on agricultural pollutants only",
        "A ban on all boat traffic and nothing further",
        "A program of tree planting on dry hillsides"],
      ans=0,
      why="Suggested skill 7.B. The framework's threats are commercial development, dam "
          "construction, overfishing, and pollutants from agriculture and industrial "
          "waste, and only the keyed set addresses all four. The rejected options address "
          "one threat, none, or something outside the list."),

 dict(q="Why is the framework's habitat service difficult to replace once a wetland is "
        "filled and built upon?",
      choices=[
        "The service depends on the wetland condition itself, which is removed when the "
        "area is filled",
        "The service depends on the number of buildings in the area",
        "The service is provided equally well by paved surfaces",
        "The service is unrelated to the presence of water",
        "The service returns automatically once building work is complete"],
      ans=0,
      why="The framework attributes habitat, along with the other services, to wetlands, "
          "which it defines by water covering the soil. Filling the area removes that "
          "condition, and the framework gives no substitute that provides the service "
          "without it."),

 dict(q="Which summary best captures this topic?",
      choices=[
        "Wetlands are areas where water covers the soil part or all of the time and "
        "provide purification, flood protection, filtration and habitat, and they and "
        "mangroves are threatened by development, dams, overfishing and pollutants from "
        "agriculture and industry",
        "Wetlands are permanently flooded areas with no ecological value that are "
        "threatened only by pollution",
        "Wetlands are dry areas that occasionally flood and provide only habitat",
        "Mangroves provide services that wetlands do not, and neither faces any threat "
        "from development",
        "Wetlands and mangroves are threatened only by natural processes rather than by "
        "human activity"],
      ans=0,
      why="Each clause of the keyed summary is one of the framework's three statements "
          "for this topic. Every rejected summary denies the definition, the list of "
          "services, or the list of threats."),
]
