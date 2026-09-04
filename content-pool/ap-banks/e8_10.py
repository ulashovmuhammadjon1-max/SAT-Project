# AP ENVIRONMENTAL SCIENCE 8.10 Waste Reduction Methods
# CED effective Fall 2026, Unit 8 Aquatic and Terrestrial Pollution. Enduring
# understanding STB-3. Learning objective STB-3.M: describe changes to current practices
# that could reduce the amount of generated waste and their associated benefits and
# drawbacks. Suggested skill 6.B, apply appropriate mathematical relationships to solve a
# problem, with work shown.
#
# Essential knowledge relied on, in the framework's own words:
#   STB-3.M.1  Recycling is a process by which certain solid waste materials are
#              processed and converted into new products.
#   STB-3.M.2  Recycling is one way to reduce the current global demand on minerals, but
#              this process is energy-intensive and can be costly.
#   STB-3.M.3  Composting is the process of organic matter such as food scraps, paper,
#              and yard waste decomposing. The product of this decomposition can be used
#              as fertilizer. Drawbacks to composting include odor and rodents.
#   STB-3.M.4  E-waste can be reduced by recycling and reuse. E-wastes may contain
#              hazardous chemicals, including heavy metals such as lead and mercury, which
#              can leach from landfills into groundwater if they are not disposed of
#              properly.
#   STB-3.M.5  Landfill mitigation strategies range from burning waste for energy to
#              restoring habitat on former landfills for use as parks.
#   STB-3.M.6  The combustion of gases produced from decomposition of organic material in
#              landfills can be used to turn turbines and generate electricity. This
#              process reduces landfill volume.
#
# ON SCOPE. Topic 8.9 keys what solid waste is, the landfill and its components, the
# incineration trade and the harms of illegal and ocean dumping (STB-3.K and STB-3.L).
# Nothing here re-asks those; every key rests on a reduction or mitigation practice in
# STB-3.M.
#
# ON THE ARITHMETIC. Suggested skill 6.B is a mathematical routine, so six items carry
# real numbers and verify_e8_10.py recomputes every percentage, ratio and rate from the
# table alone. Nothing is read off a picture; the bank carries no images.
#
# NOT KEYED: no recycling rate for any real place, no price, no energy figure presented
# as the framework's. The framework states none of them.
#
# FIVE choices (A-E). No LaTeX and no non-ASCII.
TOPIC = ("8.10", "Waste Reduction Methods", 8)

_T_DIVERT = dict(
    headers=["Part of one town's yearly waste stream", "Mass (tons)"],
    rows=[["Materials a recycler accepts", "6000"],
          ["Organic matter that could be composted", "5000"],
          ["Everything else", "9000"]])

_T_PROGRAM = dict(
    headers=["Quantity measured for one thousand tons of material",
             "If the material is landfilled", "If the material is recycled"],
    rows=[["Energy used in handling and processing (gigajoules)", "40", "260"],
          ["Cost of handling and processing (thousands of dollars)", "35", "120"],
          ["New mineral ore that must be mined (tons)", "1000", "150"]])

_T_COMPOST = dict(
    headers=["Material added to the compost pile", "Mass added (kilograms)",
             "Mass remaining after six months (kilograms)"],
    rows=[["Food scraps", "400", "140"],
          ["Yard waste", "300", "110"],
          ["Paper", "200", "70"],
          ["Plastic film", "100", "100"]])

_T_ODOR = dict(
    headers=["Distance of the homes from the composting site",
             "Odor complaints filed in one year", "Rodent sightings reported in one year"],
    rows=[["Within 200 meters", "64", "31"],
          ["From 200 to 800 meters", "22", "9"],
          ["More than 800 meters", "3", "1"]])

_T_LEACH = dict(
    headers=["Landfill cell sampled",
             "Lead in the leachate (micrograms per liter)",
             "Mercury in the leachate (micrograms per liter)"],
    rows=[["Cell that received no electronic devices", "2.0", "0.10"],
          ["Cell that received discarded electronic devices", "41.0", "1.9"],
          ["Cell filled after electronic devices were sent to recyclers", "6.0", "0.30"]])

_T_GAS = dict(
    headers=["Year of the landfill gas project",
             "Landfill gas collected (millions of cubic meters)",
             "Electricity generated (thousands of kilowatt hours)"],
    rows=[["Year 1", "4.0", "9000"],
          ["Year 3", "6.5", "14625"],
          ["Year 5", "8.0", "18000"]])

QUESTIONS = [

 dict(q="How does the framework define recycling?",
      choices=[
        "A process by which certain solid waste materials are processed and converted into "
        "new products",
        "A process by which organic matter is allowed to decompose into a soil additive",
        "A process by which waste is burned at high temperatures to reduce its volume",
        "A process by which waste is buried beneath a liner and a cap",
        "A process by which a used item is passed on and used again as it is"],
      ans=0,
      why="STB-3.M.1 states that recycling is a process by which certain solid waste "
          "materials are processed and converted into new products. Decomposition is "
          "composting under STB-3.M.3, burning is incineration under STB-3.L.2, and "
          "burial is landfilling under STB-3.K.2."),

 dict(q="What benefit and what drawbacks does the framework attach to recycling?",
      choices=[
        "It reduces the current global demand on minerals, but the process is energy "
        "intensive and can be costly",
        "It reduces the demand on minerals at no cost and with no energy required",
        "It increases the demand on minerals but saves energy",
        "It has no effect on mineral demand and no effect on cost",
        "It reduces odor and rodent problems but raises the demand on minerals"],
      ans=0,
      why="STB-3.M.2 states that recycling is one way to reduce the current global demand "
          "on minerals, but that this process is energy-intensive and can be costly. Odor "
          "and rodents are the drawbacks STB-3.M.3 attaches to composting instead."),

 dict(q="How does the framework describe composting and its drawbacks?",
      choices=[
        "Organic matter such as food scraps, paper and yard waste decomposing, with odor "
        "and rodents as drawbacks",
        "Metal and glass being melted and reformed, with high energy use as the drawback",
        "Electronic devices being taken apart for their metals, with toxic dust as the "
        "drawback",
        "Waste being burned to generate electricity, with air pollutants as the drawback",
        "Waste being buried under a cap, with methane release as the drawback"],
      ans=0,
      why="STB-3.M.3 describes composting as the process of organic matter such as food "
          "scraps, paper and yard waste decomposing and names odor and rodents as "
          "drawbacks. The rejected options describe recycling, e-waste handling, "
          "incineration and landfilling."),

 dict(q="One town's yearly waste stream is broken down as shown. What share of the total "
        "could be handled by recycling and composting together?",
      table=_T_DIVERT,
      choices=[
        "About 55 percent of the total",
        "About 30 percent of the total",
        "About 45 percent of the total",
        "About 70 percent of the total",
        "About 90 percent of the total"],
      ans=0,
      why="Adding the recyclable and compostable rows and dividing by the sum of all "
          "three rows gives a little over half the stream. STB-3.M.1 makes recycling a "
          "route for solid waste materials and STB-3.M.3 makes composting a route for "
          "organic matter."),

 dict(q="By what two practices does the framework say electronic waste can be reduced?",
      choices=[
        "Recycling and reuse",
        "Incineration and ocean disposal",
        "Composting and land application",
        "Burial in an unlined cell and capping",
        "Grinding and discharge to a sewer"],
      ans=0,
      why="STB-3.M.4 states that e-waste can be reduced by recycling and reuse. The "
          "rejected options are disposal routes described elsewhere in the unit rather "
          "than reduction practices for electronic devices."),

 dict(q="What hazard does the framework attach to electronic waste that is not disposed "
        "of properly?",
      choices=[
        "It may contain heavy metals such as lead and mercury that can leach from "
        "landfills into groundwater",
        "It may contain nutrients that cause algal blooms in the air above a landfill",
        "It may contain organic matter that produces fertilizer inside a landfill",
        "It may raise the temperature of a landfill until the waste ignites",
        "It may attract rodents that spread the devices to other sites"],
      ans=0,
      why="STB-3.M.4 states that e-wastes may contain hazardous chemicals, including heavy "
          "metals such as lead and mercury, which can leach from landfills into "
          "groundwater if they are not disposed of properly."),

 dict(q="What range of landfill mitigation strategies does the framework describe?",
      choices=[
        "From burning waste for energy to restoring habitat on former landfills for use as "
        "parks",
        "From dumping waste at sea to leaving tires in open piles",
        "From lining a landfill to closing every landfill permanently",
        "From composting food scraps to grinding glass into sand",
        "From reducing packaging to raising the price of collection"],
      ans=0,
      why="STB-3.M.5 states that landfill mitigation strategies range from burning waste "
          "for energy to restoring habitat on former landfills for use as parks. Ocean "
          "dumping and illegal tire piles are the harms of STB-3.L.4 and STB-3.L.3 rather "
          "than mitigation strategies."),

 dict(q="Handling one thousand tons of material by two routes is compared.",
      table=_T_PROGRAM,
      choices=[
        "Recycling cuts the ore that must be mined to a small fraction of the landfill "
        "case while using several times the energy and costing several times as much",
        "Recycling cuts the ore that must be mined and also uses less energy and costs "
        "less",
        "Recycling increases the ore that must be mined while saving energy",
        "The two routes require the same energy, the same cost and the same amount of ore",
        "Recycling costs less but requires far more ore to be mined"],
      ans=0,
      why="The ore row falls to a small fraction under recycling while the energy and cost "
          "rows are several times larger. That is exactly the trade STB-3.M.2 states: a "
          "reduction in the global demand on minerals from a process that is energy "
          "intensive and can be costly."),

 dict(q="What does the framework say can be done with the gases produced by the "
        "decomposition of organic material in a landfill?",
      choices=[
        "Their combustion can be used to turn turbines and generate electricity, which "
        "also reduces landfill volume",
        "They can be condensed into a liquid fertilizer for farmland",
        "They can be pumped into groundwater to neutralize contamination",
        "They can be sold as a raw material for making new electronic devices",
        "They can be used to cool the landfill and slow decomposition"],
      ans=0,
      why="STB-3.M.6 states that the combustion of gases produced from decomposition of "
          "organic material in landfills can be used to turn turbines and generate "
          "electricity, and that this process reduces landfill volume."),

 dict(q="What does the framework say the product of composting can be used for?",
      choices=[
        "As fertilizer",
        "As a fuel burned to generate electricity",
        "As a liner beneath a landfill",
        "As a raw material for making new electronic devices",
        "As a disinfectant for treated wastewater"],
      ans=0,
      why="STB-3.M.3 states that the product of the decomposition of organic matter can "
          "be used as fertilizer. Burning for electricity is STB-3.M.6, a liner is a "
          "landfill component under STB-3.K.4, and disinfection belongs to sewage "
          "treatment."),

 dict(q="Why does the framework say recycling reduces the global demand on minerals?",
      choices=[
        "Materials already in circulation are processed into new products, so less new "
        "material has to be obtained",
        "Recycling destroys minerals so that no one can use them",
        "Recycling converts minerals into organic matter",
        "Recycling raises the price of minerals until demand disappears",
        "Recycling has no relationship to mineral demand at all"],
      ans=0,
      why="STB-3.M.1 makes recycling the processing and conversion of solid waste "
          "materials into new products, and STB-3.M.2 states that this is one way to "
          "reduce the current global demand on minerals, so the recovered material stands "
          "in for material that would otherwise be extracted."),

 dict(q="Four materials were added to one compost pile and weighed again six months later.",
      table=_T_COMPOST,
      choices=[
        "The three organic materials each lost most of their mass while the plastic film "
        "lost none of its own",
        "The plastic film lost more of its mass than any of the other materials",
        "All four materials lost about the same share of their mass",
        "None of the four materials lost any mass",
        "The organic materials gained mass while the plastic film lost mass"],
      ans=0,
      why="Each of the three organic rows retains only a fraction of the mass it started "
          "with, while the plastic row is unchanged. STB-3.M.3 describes composting as "
          "organic matter such as food scraps, paper and yard waste decomposing, and "
          "plastic film is not organic matter of that kind."),

 dict(q="Which set of materials does the framework name as the organic matter that "
        "composting handles?",
      choices=[
        "Food scraps, paper and yard waste",
        "Televisions, cell phones and computers",
        "Aluminum cans, glass bottles and steel",
        "Used rubber tires and scrap vehicles",
        "Concrete rubble and broken brick"],
      ans=0,
      why="STB-3.M.3 names food scraps, paper and yard waste as the organic matter that "
          "decomposes in composting. Electronic devices are STB-3.M.4, tires are "
          "STB-3.L.3, and metals and rubble are not named in this statement."),

 dict(q="A student argues that a town should recycle everything because recycling costs "
        "nothing and uses no energy. What is the clearest correction from the framework?",
      choices=[
        "The framework describes recycling as energy intensive and potentially costly even "
        "while it reduces the demand on minerals",
        "The framework describes recycling as free but as raising the demand on minerals",
        "The framework describes recycling as impossible for any material",
        "The framework describes recycling as producing fertilizer rather than new products",
        "The framework describes recycling as the same process as composting"],
      ans=0,
      why="STB-3.M.2 pairs the reduction in global mineral demand with the statement that "
          "the process is energy-intensive and can be costly, so the benefit comes with a "
          "stated price rather than without one."),

 dict(q="Why does the framework insist that electronic waste be disposed of properly "
        "rather than sent to an ordinary landfill?",
      choices=[
        "Heavy metals such as lead and mercury in the devices can leach into groundwater "
        "if they are not handled properly",
        "Electronic devices decompose too quickly and fill a landfill with gas",
        "Electronic devices attract rodents and produce odor",
        "Electronic devices raise the temperature of a landfill",
        "Electronic devices cannot be recycled or reused at all"],
      ans=0,
      why="STB-3.M.4 states that e-wastes may contain hazardous chemicals, including heavy "
          "metals such as lead and mercury, which can leach from landfills into "
          "groundwater if they are not disposed of properly, and that e-waste can be "
          "reduced by recycling and reuse."),

 dict(q="Reports from homes at different distances from a composting site are shown.",
      table=_T_ODOR,
      choices=[
        "Both the odor complaints and the rodent reports are highest for the homes closest "
        "to the site and fall with distance",
        "Both kinds of report are highest for the homes farthest from the site",
        "The odor complaints fall with distance while the rodent reports rise with it",
        "The reports are the same at every distance from the site",
        "No odor complaints or rodent reports were filed at any distance"],
      ans=0,
      why="Both columns fall at each step away from the site and are largest for the "
          "nearest homes. STB-3.M.3 names odor and rodents as the drawbacks of "
          "composting."),

 dict(q="Which of the following is a drawback the framework attaches to composting rather "
        "than to another practice?",
      choices=[
        "Odor and rodents around the site",
        "Air pollutants released from a stack",
        "Groundwater contaminated by heavy metals",
        "A high energy requirement for reprocessing materials",
        "Wildlife entangled in floating debris"],
      ans=0,
      why="STB-3.M.3 names odor and rodents as drawbacks to composting. Stack emissions "
          "belong to incineration under STB-3.L.2, heavy metal leaching to e-waste under "
          "STB-3.M.4, high energy use to recycling under STB-3.M.2 and entanglement to "
          "ocean waste under STB-3.L.4."),

 dict(q="A closed landfill is capped, planted and opened to the public with trails and "
        "playing fields. Which framework statement does this illustrate?",
      choices=[
        "Landfill mitigation strategies include restoring habitat on former landfills for "
        "use as parks",
        "Recycling converts solid waste materials into new products",
        "Composting produces a material that can be used as fertilizer",
        "E-waste can be reduced by recycling and reuse",
        "Incineration significantly reduces the volume of solid waste"],
      ans=0,
      why="STB-3.M.5 states that landfill mitigation strategies range from burning waste "
          "for energy to restoring habitat on former landfills for use as parks, and a "
          "closed landfill reopened as a park is the second end of that range."),

 dict(q="A landfill operator wants both to generate power and to reduce the volume of "
        "waste in the site. Which framework practice does that?",
      choices=[
        "Collecting the gases produced by decomposition and burning them to turn turbines",
        "Adding fresh organic matter to the site each week",
        "Composting the food scraps that arrive at the site",
        "Sending the site's electronic devices to a recycler",
        "Replacing the site's bottom liner with a thicker one"],
      ans=0,
      why="STB-3.M.6 states that the combustion of gases produced from decomposition of "
          "organic material in landfills can be used to turn turbines and generate "
          "electricity and that this process reduces landfill volume, which is both "
          "outcomes the operator wants."),

 dict(q="Leachate from three landfill cells was analyzed.",
      table=_T_LEACH,
      choices=[
        "The cell that received discarded electronic devices carries far more lead and "
        "mercury in its leachate than either of the other two cells",
        "The cell that received no electronic devices carries the most lead and mercury",
        "All three cells carry the same amount of lead and mercury",
        "The cell filled after devices were sent to recyclers carries the most mercury",
        "Lead is highest in one cell while mercury is highest in a different cell"],
      ans=0,
      why="The row for the cell that received devices carries the largest value in both "
          "columns, several times either of the others. STB-3.M.4 states that e-wastes may "
          "contain heavy metals such as lead and mercury that can leach from landfills "
          "into groundwater if they are not disposed of properly."),

 dict(q="Which pairing of a practice with the framework's own account of it is correct?",
      choices=[
        "Composting, paired with a product that can be used as fertilizer and with odor "
        "and rodents as drawbacks",
        "Composting, paired with a reduction in the global demand on minerals and with a "
        "high energy requirement",
        "Recycling, paired with a product that can be used as fertilizer",
        "Landfill gas combustion, paired with an increase in the volume of the landfill",
        "Reuse of electronic devices, paired with the release of lead and mercury into "
        "groundwater"],
      ans=0,
      why="STB-3.M.3 gives composting a product usable as fertilizer and names odor and "
          "rodents as drawbacks, while STB-3.M.2 gives the mineral and energy trade to "
          "recycling and STB-3.M.6 has gas combustion reduce landfill volume. Each "
          "rejected pairing crosses two of those statements."),

 dict(q="How does reusing an electronic device differ from recycling it, as the framework "
        "presents the two?",
      choices=[
        "Reuse keeps the device in service as it is, while recycling processes materials "
        "and converts them into new products",
        "Reuse processes the materials into new products, while recycling keeps the device "
        "in service",
        "The framework treats the two words as names for the same practice",
        "Reuse is a disposal method and recycling is a mitigation strategy",
        "Reuse applies only to organic matter and recycling only to metals"],
      ans=0,
      why="STB-3.M.4 names recycling and reuse as two ways to reduce e-waste and "
          "STB-3.M.1 defines recycling as processing solid waste materials and converting "
          "them into new products, so reuse is the practice that does not require that "
          "conversion."),

 dict(q="A city is deciding whether to add a composting program. Which pair of "
        "measurements would best let it weigh the framework's stated benefit against the "
        "framework's stated drawbacks?",
      choices=[
        "The mass of organic waste diverted from the landfill and the number of odor and "
        "rodent complaints from nearby homes",
        "The number of trucks in the city fleet and the price of fuel",
        "The area of the city and the number of its residents",
        "The depth of the landfill and the age of its liner",
        "The number of electronic devices collected and the price of scrap metal"],
      ans=0,
      why="STB-3.M.3 gives composting a usable product from diverted organic matter and "
          "names odor and rodents as its drawbacks, so the diverted mass and the "
          "complaints are the two sides of that trade. Fleet size, city size, landfill "
          "depth and scrap prices measure neither."),

 dict(q="Gas collected and electricity generated at one landfill are shown. Using the same "
        "rate, about how much electricity would ten million cubic meters of collected gas "
        "generate?",
      table=_T_GAS,
      choices=[
        "About 22,500 thousand kilowatt hours",
        "About 2,250 thousand kilowatt hours",
        "About 9,000 thousand kilowatt hours",
        "About 45,000 thousand kilowatt hours",
        "About 180,000 thousand kilowatt hours"],
      ans=0,
      why="Dividing the electricity generated by the gas collected gives the same rate in "
          "each row, and multiplying that rate by ten million cubic meters gives the keyed "
          "figure. STB-3.M.6 states that the combustion of landfill gases can be used to "
          "turn turbines and generate electricity."),

 dict(q="Which evidence would most directly support a claim that sending electronic "
        "devices to recyclers protects groundwater?",
      choices=[
        "Leachate from landfill cells that received the devices carries more lead and "
        "mercury than leachate from cells filled after the devices were diverted",
        "The number of devices collected at recycling events has risen each year",
        "Recycling a device costs less than manufacturing a new one",
        "The devices contain parts made in several different countries",
        "The landfill has been in operation for more than thirty years"],
      ans=0,
      why="STB-3.M.4 states that heavy metals such as lead and mercury in e-waste can "
          "leach from landfills into groundwater if the waste is not disposed of properly, "
          "so a measured difference in leachate between cells with and without the devices "
          "is the evidence that bears on the claim."),

 dict(q="Why does the framework describe composting as a decomposition process rather "
        "than as a manufacturing process?",
      choices=[
        "Organic matter is broken down by decay into a material usable as fertilizer, "
        "rather than being processed into a new product",
        "Organic matter is melted and reformed into a new product",
        "Organic matter is burned at high temperatures and reduced to ash",
        "Organic matter is buried beneath a liner where nothing changes",
        "Organic matter is dissolved in water and discharged to a sewer"],
      ans=0,
      why="STB-3.M.3 describes composting as the process of organic matter decomposing "
          "and gives fertilizer as the use of the product, while STB-3.M.1 reserves "
          "processing into new products for recycling."),

 dict(q="Which of the following is NOT a waste reduction or mitigation practice the "
        "framework describes in this topic?",
      choices=[
        "Dumping waste into the ocean so that it leaves the land",
        "Converting certain solid waste materials into new products",
        "Letting food scraps and yard waste decompose into fertilizer",
        "Recycling and reusing discarded electronic devices",
        "Restoring habitat on a former landfill for use as a park"],
      ans=0,
      why="STB-3.L.4 describes ocean dumping as a practice that has produced large "
          "floating islands of trash and entangled wildlife, not as a reduction method. "
          "The four rejected options restate STB-3.M.1, STB-3.M.3, STB-3.M.4 and "
          "STB-3.M.5."),

 dict(q="Which study would best test the framework's claim that recycling reduces the "
        "demand on minerals?",
      choices=[
        "Comparing the tons of new ore required to make a product from recycled material "
        "with the tons required to make the same product from new material",
        "Counting the number of bins a city distributes to households",
        "Measuring the odor around a composting site",
        "Recording the number of electronic devices sold in a year",
        "Measuring the volume of gas collected from a landfill"],
      ans=0,
      why="STB-3.M.2 states that recycling is one way to reduce the current global demand "
          "on minerals, so the comparison must be of the new material each route requires. "
          "Bin counts, odor, device sales and gas volumes test other statements or none."),

 dict(q="A region wants to cut the mining it depends on but has a limited energy budget. "
        "Which framework tension does that situation illustrate?",
      choices=[
        "Recycling lowers the demand on minerals but is itself energy intensive and can be "
        "costly",
        "Composting lowers the demand on minerals but produces odor and rodents",
        "Landfilling lowers the demand on minerals but releases air pollutants",
        "Reuse lowers the demand on minerals but requires more mining than recycling",
        "Burning landfill gas lowers the demand on minerals but increases landfill volume"],
      ans=0,
      why="STB-3.M.2 pairs the reduction in global mineral demand with the fact that the "
          "process is energy-intensive and can be costly. Odor and rodents belong to "
          "composting under STB-3.M.3, and STB-3.M.6 has gas combustion reduce rather than "
          "increase landfill volume."),

 dict(q="Which summary best captures this topic?",
      choices=[
        "Recycling converts waste materials into new products and lowers mineral demand at "
        "the price of energy and cost, composting turns organic matter into fertilizer at "
        "the price of odor and rodents, electronic waste is reduced by recycling and reuse "
        "so its lead and mercury stay out of groundwater, and landfill mitigation runs "
        "from burning gas for electricity to reopening closed sites as parks",
        "Every reduction method described in this topic is free of cost and free of "
        "drawbacks",
        "Composting and recycling are the same process applied to different materials",
        "Electronic waste is best handled by burial in an unlined cell",
        "Burning landfill gas increases the volume of a landfill and generates no "
        "electricity"],
      ans=0,
      why="Each clause of the keyed summary is one of STB-3.M.1 through STB-3.M.6. Every "
          "rejected summary denies a stated drawback, conflates two practices, recommends "
          "a practice the framework warns against, or reverses a stated outcome."),
]
