# AP ENVIRONMENTAL SCIENCE 5.7 Meat Production Methods
# CED effective Fall 2026, Unit 5 Land and Water Use.
# Enduring understanding EIN-2: when humans use natural resources, they alter natural
# systems.
# Learning objectives EIN-2.H, identify different methods of meat production; EIN-2.I,
# describe the benefits and drawbacks of different methods of meat production.
# Suggested skill 5.E, explain what the data implies or illustrates about environmental
# issues.
#
# Essential knowledge relied on, in the framework's own words:
#   EIN-2.H.1  Methods of meat production include feedlots and concentrated animal
#              feeding operations (CAFOs), as well as pasture-based systems, such as
#              rotational grazing and free-range grazing.
#   EIN-2.I.1  Meat production requires more land, water, and energy per gram of protein
#              produced than the production of plant-based foods, and it increases
#              nutrient pollution and emissions of greenhouse gases, such as methane. The
#              environmental impacts of meat production vary by the type of livestock
#              raised and production practices used.
#   EIN-2.I.2  CAFOs can be more economically efficient, which lowers costs for
#              consumers. Animals raised in CAFOs are kept in confined spaces and fed
#              grain- and soy-based diets. CAFOs have high concentrations of manure that
#              can contaminate nearby waterways if not properly managed. Routine use of
#              antibiotics in CAFOs can contribute to the global risks of antibiotic
#              resistance.
#   EIN-2.I.3  Free-range or pasture-based grazing systems allow animals to feed on grass
#              or forage for most of their lives. Rotational grazing can improve the
#              sustainability of these systems. Manure delivers nutrients to pasture
#              soils, but runoff and erosion risks remain if animal density is high.
#              These systems require more land, leading to higher consumer costs. Not all
#              free-range systems are antibiotic-free.
#   EIN-2.I.4  Overgrazing occurs when the livestock population exceeds the land's
#              capacity to regenerate vegetation. This results in reduced plant cover,
#              soil erosion, and soil compaction, all of which reduce soil fertility.
#              Overgrazing also reduces biodiversity and lowers carbon storage. Rotational
#              grazing can help prevent or minimize these impacts.
#   EIN-2.I.5  Overgrazing can lead to desertification in arid and semi-arid regions.
#              Implementing restoration efforts, soil conservation measures, and improved
#              grazing practices can help slow or reverse the desertification process.
#   EIN-2.I.6  Less consumption of meat, especially from ruminant livestock such as cattle
#              and sheep, can lower emissions of CO2, CH4, and N2O, conserve freshwater
#              resources, and reduce reliance on antibiotics and growth hormones. Advances
#              in feed quality and the use of precision farming technologies can also
#              mitigate environmental impacts. The magnitude of these benefits depends on
#              the production methods applied and how land no longer used for livestock is
#              subsequently managed.
#
# SCOPE. This topic is unusually well specified, and the framework is careful in three
# places that a careless key would flatten:
#   1. EIN-2.I.1 ends by saying impacts VARY by livestock type and production practices.
#      No key here says every meat is equally damaging.
#   2. EIN-2.I.3 ends by saying NOT ALL free-range systems are antibiotic-free, and puts
#      the runoff and erosion risk on HIGH ANIMAL DENSITY rather than on pasture as such.
#      Two items turn on exactly those qualifications.
#   3. EIN-2.I.6 ends by making the MAGNITUDE of the benefit depend on production methods
#      and on how released land is subsequently managed. That hedge is keyed, not dropped.
# The three greenhouse gases are written out as carbon dioxide, methane and nitrous
# oxide, because export_units.py does not typeset Environmental Science and a subscript
# would reach a student as raw text.
#
# BOUNDARY WITH 5.15. STB-1.E.3 defines rotational grazing as the regular rotation of
# livestock between pastures to avoid overgrazing, and topic 5.15 treats it as a soil
# practice. Here rotational grazing appears only where THIS topic's own statements put
# it: improving the sustainability of pasture systems (EIN-2.I.3) and preventing or
# minimising the impacts of overgrazing (EIN-2.I.4).
#
# NO FIGURES. Every quantitative item carries a table=; all arithmetic is recomputed in
# verify_e5_7.py from that table alone and is calculator-free.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("5.7", "Meat Production Methods", 5)

_T_PROTEIN = dict(
    headers=["Food produced",
             "Land used per gram of protein (square meters)",
             "Water used per gram of protein (litres)",
             "Energy used per gram of protein (kilojoules)"],
    rows=[["Beef", "1.6", "1.1", "220"],
          ["Pork", "0.4", "0.6", "90"],
          ["Beans", "0.1", "0.2", "20"]])

_T_METHANE = dict(
    headers=["Livestock",
             "Methane released per kilogram of meat produced (grams)"],
    rows=[["Cattle", "290"],
          ["Sheep", "230"],
          ["Pigs", "40"],
          ["Poultry", "10"]])

_T_SYSTEMS = dict(
    headers=["Production system",
             "Land needed per animal (hectares)",
             "Price to the consumer per kilogram of meat (currency units)"],
    rows=[["Concentrated animal feeding operation", "0.02", "6"],
          ["Free-range pasture system", "0.90", "14"]])

_T_STOCKING = dict(
    headers=["Stocking rate (animals per hectare)",
             "Plant cover remaining after three seasons (percent of the ground)",
             "Soil lost in the third season (tonnes per hectare)"],
    rows=[["1", "88", "1"],
          ["3", "71", "4"],
          ["6", "42", "13"],
          ["10", "19", "31"]])

_T_ROTATION = dict(
    headers=["Grazing practice on land carrying the same number of animals",
             "Plant cover after five seasons (percent of the ground)",
             "Number of plant species recorded"],
    rows=[["Animals left on one pasture all season", "34", "6"],
          ["Animals rotated between four pastures", "77", "19"]])

_T_MANURE = dict(
    headers=["Site sampled",
             "Nitrate in the stream (milligrams per litre)"],
    rows=[["Upstream of the animal operation", "0.6"],
          ["Beside the manure storage", "9.8"],
          ["Two kilometers downstream", "5.4"]])

_T_DIET = dict(
    headers=["Change made by one household for a year",
             "Freshwater saved (thousand litres)",
             "Greenhouse gas emissions avoided (kilograms)"],
    rows=[["No change", "0", "0"],
          ["Half the beef replaced by beans", "160", "310"],
          ["All the beef replaced by beans", "320", "620"]])

QUESTIONS = [

 dict(q="Which set of methods does the course framework identify as methods of "
        "meat production?",
      choices=[
        "Feedlots and concentrated animal feeding operations, together with pasture-based "
        "systems such as rotational and free-range grazing",
        "Drip, flood, furrow, and spray systems",
        "Terracing, contour plowing, and strip cropping",
        "Biocontrol, intercropping, and crop rotation",
        "Reforestation, prescribed burning, and the removal of affected trees"],
      ans=0,
      why="EIN-2.H.1 states that methods of meat production include feedlots and concentrated "
          "animal feeding operations, as well as pasture-based systems, such as rotational "
          "grazing and free-range grazing. The rejected sets are the irrigation types of "
          "EIN-2.E.2, the soil conservation methods of STB-1.E.1, the integrated pest "
          "management methods of STB-1.C.1, and the forestry methods of STB-1.G."),

 dict(q="Land, water and energy used per gram of protein are compared for three foods in "
        "the table. Which conclusion does the framework support?",
      table=_T_PROTEIN,
      choices=[
        "Producing meat takes more land, water and energy per gram of protein than "
        "producing a plant-based food.",
        "Producing meat takes less land, water and energy per gram of protein than "
        "producing a plant-based food.",
        "Producing meat takes more land but less water and energy per gram of protein "
        "than producing a plant-based food.",
        "The three foods take the same land, water and energy per gram of protein.",
        "The comparison cannot be made, because protein from meat and protein from plants "
        "are different substances."],
      ans=0,
      why="Beans read 0.1 square meters, 0.2 litres and 20 kilojoules per gram of protein "
          "against 1.6, 1.1 and 220 for beef and 0.4, 0.6 and 90 for pork, so the plant food "
          "is the smallest on all three counts. EIN-2.I.1 states that meat production requires "
          "more land, water, and energy per gram of protein produced than the production of "
          "plant-based foods."),

 dict(q="Using the same three foods, how many times as much land per gram of protein does "
        "beef take as beans?",
      table=_T_PROTEIN,
      choices=[
        "Sixteen times as much",
        "Four times as much",
        "Eleven times as much",
        "Two times as much",
        "The same amount"],
      ans=0,
      why="Dividing the two tabulated land figures gives 1.6 divided by 0.1, which is 16. The "
          "rejected values come from the pork comparison, from the water column, or from "
          "denying that the two differ."),

 dict(q="Besides land, water and energy, what two further environmental effects does the "
        "framework attribute to meat production?",
      choices=[
        "Increased nutrient pollution and increased emissions of greenhouse gases such "
        "as methane",
        "Increased nutrient pollution and a fall in greenhouse gas emissions",
        "Reduced nutrient pollution and increased emissions of greenhouse gases",
        "Reduced nutrient pollution and reduced emissions of greenhouse gases",
        "No further effects, since land, water and energy exhaust the framework's account"],
      ans=0,
      why="EIN-2.I.1 states that meat production increases nutrient pollution and emissions of "
          "greenhouse gases, such as methane. Each rejected option reverses one or both "
          "directions, or denies that the framework names anything further."),

 dict(q="Methane released per kilogram of meat is compared across four kinds of livestock. "
        "What does the comparison illustrate about the framework's claim?",
      table=_T_METHANE,
      choices=[
        "The environmental impact of meat production varies by the type of "
        "livestock raised.",
        "The environmental impact of meat production is the same for every type of "
        "livestock raised.",
        "Only poultry production releases any methane at all.",
        "Methane release per kilogram is highest for poultry and lowest for cattle.",
        "Methane release cannot be compared between kinds of livestock."],
      ans=0,
      why="The tabulated releases are 290, 230, 40 and 10 grams per kilogram of meat, a range "
          "of nearly thirty to one across four kinds of livestock. EIN-2.I.1 ends by stating "
          "that the environmental impacts of meat production VARY by the type of livestock "
          "raised and production practices used."),

 dict(q="Using the same methane values, how many times as much methane is released per "
        "kilogram of cattle meat as per kilogram of poultry meat?",
      table=_T_METHANE,
      choices=[
        "Twenty-nine times as much",
        "Seven times as much",
        "Twenty-three times as much",
        "Four times as much",
        "The same amount"],
      ans=0,
      why="Dividing the two tabulated values gives 290 divided by 10, which is 29. The rejected "
          "values come from other pairs of livestock in the same table or deny that "
          "the two differ."),

 dict(q="What economic effect does the framework attribute to concentrated animal "
        "feeding operations?",
      choices=[
        "They can be more economically efficient, which lowers costs for consumers.",
        "They are less economically efficient, which raises costs for consumers.",
        "They are more economically efficient, but consumer costs rise all the same.",
        "They have no effect on the cost of meat to consumers.",
        "They lower costs only where the animals are fed on grass."],
      ans=0,
      why="EIN-2.I.2 states that CAFOs can be more economically efficient, which lowers costs "
          "for consumers. EIN-2.I.2 also states that animals in CAFOs are fed grain- and "
          "soy-based diets, so the grass condition in the last option is not the "
          "framework's claim."),

 dict(q="How does the framework describe the conditions and feeding of animals raised in "
        "concentrated animal feeding operations?",
      choices=[
        "Kept in confined spaces and fed grain- and soy-based diets",
        "Kept on open pasture and fed grass or forage for most of their lives",
        "Kept in confined spaces and fed grass or forage for most of their lives",
        "Kept on open pasture and fed grain- and soy-based diets",
        "The framework does not describe how the animals are kept or fed"],
      ans=0,
      why="EIN-2.I.2 states that animals raised in CAFOs are kept in confined spaces and fed "
          "grain- and soy-based diets. Feeding on grass or forage for most of their lives is "
          "EIN-2.I.3's description of free-range and pasture-based systems instead."),

 dict(q="What does the framework say about manure in concentrated animal "
        "feeding operations?",
      choices=[
        "They hold high concentrations of it, which can contaminate nearby waterways if "
        "it is not properly managed.",
        "They hold high concentrations of it, which always contaminates nearby waterways "
        "whatever is done.",
        "They hold no manure, because the animals are fed a grain- and soy-based diet.",
        "They hold high concentrations of it, which the framework says cannot reach "
        "any waterway.",
        "The framework discusses manure only in pasture-based systems."],
      ans=0,
      why="EIN-2.I.2 states that CAFOs have high concentrations of manure that CAN contaminate "
          "nearby waterways IF NOT PROPERLY MANAGED, which is a conditional rather than an "
          "inevitability. EIN-2.I.3 also discusses manure on pasture, so the last option "
          "is wrong."),

 dict(q="A stream running past an animal operation was sampled at three points. Which "
        "conclusion is best supported?",
      table=_T_MANURE,
      choices=[
        "Nitrate rose sharply beside the operation and remained elevated downstream, "
        "which is consistent with manure reaching the water.",
        "Nitrate fell sharply beside the operation, which is consistent with manure being "
        "removed from the water.",
        "Nitrate was the same at all three points, so the operation had no effect.",
        "Nitrate was highest upstream, so the source lies above the operation.",
        "Nitrate readings from one stream cannot be compared with one another."],
      ans=0,
      why="The readings are 0.6, 9.8 and 5.4 milligrams per litre from upstream to beside the "
          "storage to downstream, so the water gains nitrate at the operation and is still "
          "carrying much of it two kilometers on. EIN-2.I.2 states that high concentrations of "
          "manure can contaminate nearby waterways if not properly managed."),

 dict(q="Using the same stream, by how much did the nitrate concentration rise between the "
        "upstream point and the point beside the manure storage?",
      table=_T_MANURE,
      choices=[
        "9.2 milligrams per litre",
        "9.8 milligrams per litre",
        "4.8 milligrams per litre",
        "4.4 milligrams per litre",
        "10.4 milligrams per litre"],
      ans=0,
      why="Subtracting gives 9.8 minus 0.6, which is 9.2 milligrams per litre. The rejected "
          "values quote the peak reading alone, pair the wrong points, or add the two readings "
          "rather than differencing them."),

 dict(q="What risk does the framework attach to the routine use of antibiotics in "
        "concentrated animal feeding operations?",
      choices=[
        "It can contribute to the global risks of antibiotic resistance.",
        "It can contribute to the loss of genetic diversity in the crop fed to the animals.",
        "It can raise the water table beneath the operation.",
        "It can lower the price of meat without any further consequence.",
        "The framework attaches no risk to it."],
      ans=0,
      why="EIN-2.I.2 states that routine use of antibiotics in CAFOs can contribute to the "
          "global risks of antibiotic resistance. Loss of crop genetic diversity is EIN-2.G.2 "
          "and a rising water table is EIN-2.F.1, both in other topics."),

 dict(q="How does the framework describe what animals in free-range or pasture-based "
        "grazing systems eat?",
      choices=[
        "Grass or forage for most of their lives",
        "Grain- and soy-based diets for most of their lives",
        "Grass for the first month only and grain thereafter",
        "Nothing, because these systems supply no feed at all",
        "The framework does not describe what these animals eat"],
      ans=0,
      why="EIN-2.I.3 states that free-range or pasture-based grazing systems allow animals to "
          "feed on grass or forage for most of their lives. Grain- and soy-based diets belong "
          "to CAFOs in EIN-2.I.2."),

 dict(q="Two production systems are compared in the table. Which reading matches the "
        "framework's account?",
      table=_T_SYSTEMS,
      choices=[
        "The pasture system needs far more land per animal and its meat costs the consumer "
        "more, which is what the framework says of these systems.",
        "The pasture system needs far less land per animal and its meat costs the consumer "
        "less, which is what the framework says of these systems.",
        "The two systems need the same land per animal but differ in consumer price.",
        "The two systems charge the same consumer price but differ in land per animal.",
        "The pasture system needs far more land per animal but its meat costs the consumer "
        "less than meat from the other system."],
      ans=0,
      why="The pasture system reads 0.90 hectares per animal against 0.02, and 14 currency "
          "units per kilogram against 6. EIN-2.I.3 states that these systems require more land, "
          "leading to higher consumer costs, and EIN-2.I.2 states that CAFOs can be more "
          "economically efficient, which lowers costs for consumers."),

 dict(q="Using the same two systems, how many times as much land per animal does the "
        "pasture system need?",
      table=_T_SYSTEMS,
      choices=[
        "Forty-five times as much",
        "Two times as much",
        "Ninety times as much",
        "Twenty times as much",
        "The same amount"],
      ans=0,
      why="Dividing the two tabulated land requirements gives 0.90 divided by 0.02, which is "
          "45. The rejected values come from the price column, from misplacing a decimal, or "
          "from denying that the two differ."),

 dict(q="A student writes that meat from a free-range system is guaranteed to be produced "
        "without antibiotics. Which correction does the framework require?",
      choices=[
        "The framework states that not all free-range systems are antibiotic-free.",
        "The framework states that all free-range systems are antibiotic-free.",
        "The framework states that antibiotics are used only in free-range systems.",
        "The framework makes no statement about antibiotics in free-range systems.",
        "The framework states that free-range systems use more antibiotics than "
        "confined systems."],
      ans=0,
      why="EIN-2.I.3 ends with the sentence that not all free-range systems are "
          "antibiotic-free, which denies the guarantee without asserting the opposite. The "
          "framework attaches routine antibiotic use to CAFOs in EIN-2.I.2 but does not rank "
          "the two systems."),

 dict(q="What does the framework say about manure in a pasture-based system, and what "
        "condition does it attach?",
      choices=[
        "Manure delivers nutrients to pasture soils, but runoff and erosion risks remain "
        "if animal density is high.",
        "Manure delivers nutrients to pasture soils, and no runoff or erosion risk remains "
        "at any animal density.",
        "Manure removes nutrients from pasture soils, and runoff risks remain at any "
        "animal density.",
        "Manure has no effect on pasture soils in the framework's account.",
        "Manure delivers nutrients only where the animals are kept in confined spaces."],
      ans=0,
      why="EIN-2.I.3 states that manure delivers nutrients to pasture soils, BUT runoff and "
          "erosion risks remain IF ANIMAL DENSITY IS HIGH. The framework therefore grants the "
          "benefit and makes the risk conditional on density rather than unconditional "
          "or absent."),

 dict(q="What does the framework say overgrazing is?",
      choices=[
        "The livestock population exceeding the land's capacity to regenerate vegetation",
        "The livestock population falling below the number the land could support",
        "The rotation of livestock between pastures during a single season",
        "The confinement of livestock in a small space and their feeding on grain",
        "The loss of vegetation to fire rather than to animals"],
      ans=0,
      why="EIN-2.I.4 states that overgrazing occurs when the livestock population exceeds the "
          "land's capacity to regenerate vegetation. Rotation between pastures is the practice "
          "EIN-2.I.4 offers to prevent it, and confinement with grain feeding is EIN-2.I.2's "
          "description of CAFOs."),

 dict(q="Which set of results does the framework attribute to overgrazing?",
      choices=[
        "Reduced plant cover, soil erosion and soil compaction, all of which reduce "
        "soil fertility",
        "Increased plant cover, deeper soil and looser soil, all of which raise "
        "soil fertility",
        "Reduced plant cover and looser soil, which together raise soil fertility",
        "Increased plant cover and soil erosion, which together leave fertility unchanged",
        "No change to plant cover, soil or fertility"],
      ans=0,
      why="EIN-2.I.4 states that overgrazing results in reduced plant cover, soil erosion, and "
          "soil compaction, ALL OF WHICH REDUCE SOIL FERTILITY. Each rejected option reverses "
          "at least one of the three results or the fertility outcome."),

 dict(q="What two further consequences of overgrazing does the framework name beyond the "
        "effects on soil?",
      choices=[
        "It reduces biodiversity and lowers carbon storage.",
        "It raises biodiversity and raises carbon storage.",
        "It reduces biodiversity but raises carbon storage.",
        "It raises biodiversity but lowers carbon storage.",
        "It has no consequences beyond the effects on soil."],
      ans=0,
      why="EIN-2.I.4 states that overgrazing also reduces biodiversity and lowers carbon "
          "storage. Each rejected option reverses one or both directions, or denies that the "
          "framework names anything further."),

 dict(q="Four paddocks were stocked at different rates and measured after three seasons. "
        "What do the values show?",
      table=_T_STOCKING,
      choices=[
        "As the stocking rate rose, the plant cover remaining fell and the soil lost rose.",
        "As the stocking rate rose, the plant cover remaining rose and the soil lost fell.",
        "Plant cover and soil loss were unchanged across the four stocking rates.",
        "The most heavily stocked paddock kept the most plant cover of the four.",
        "The most lightly stocked paddock lost the most soil of the four."],
      ans=0,
      why="Plant cover runs 88, 71, 42 and 19 percent while soil lost runs 1, 4, 13 and 31 "
          "tonnes per hectare as the stocking rate rises. EIN-2.I.4 states that overgrazing "
          "results in reduced plant cover and soil erosion."),

 dict(q="Using the same four paddocks, how much more soil was lost at the highest stocking "
        "rate than at the lowest?",
      table=_T_STOCKING,
      choices=[
        "30 tonnes per hectare more",
        "31 tonnes per hectare more",
        "27 tonnes per hectare more",
        "18 tonnes per hectare more",
        "32 tonnes per hectare more"],
      ans=0,
      why="Subtracting gives 31 minus 1, which is 30 tonnes per hectare. The rejected values "
          "quote the highest loss alone, pair the wrong rates, or add the two "
          "figures instead of differencing them."),

 dict(q="Two areas carrying the same number of animals were managed differently for five "
        "seasons. What does the comparison support?",
      table=_T_ROTATION,
      choices=[
        "Rotating the animals between pastures left more plant cover and more plant "
        "species than leaving them on one pasture.",
        "Rotating the animals between pastures left less plant cover and fewer plant "
        "species than leaving them on one pasture.",
        "The two managements left the same plant cover and the same number of species.",
        "Rotating the animals left more plant cover but fewer plant species.",
        "Rotating the animals left fewer plant species but the same plant cover."],
      ans=0,
      why="The rotated area reads 77 percent plant cover and 19 species against 34 percent and "
          "6 species, with the animal numbers held equal by the stem. EIN-2.I.4 states that "
          "rotational grazing can help prevent or minimize the impacts of overgrazing, which "
          "include reduced plant cover and reduced biodiversity."),

 dict(q="Using the same two managements, how many more plant species were recorded where "
        "the animals were rotated?",
      table=_T_ROTATION,
      choices=[
        "13 more species",
        "19 more species",
        "6 more species",
        "25 more species",
        "43 more species"],
      ans=0,
      why="Subtracting the two tabulated species counts gives 19 minus 6, which is 13. The "
          "rejected values quote one count alone, add the two counts, or take the difference "
          "from the plant cover column instead."),

 dict(q="What does the framework say overgrazing can lead to in arid and semi-arid regions, "
        "and what can be done about it?",
      choices=[
        "Desertification, which restoration efforts, soil conservation measures and "
        "improved grazing practices can help slow or reverse",
        "Desertification, which the framework says nothing can slow or reverse",
        "Waterlogging, which restoration efforts can help slow or reverse",
        "Salinization, which improved grazing practices can help slow or reverse",
        "Eutrophication, which soil conservation measures can help slow or reverse"],
      ans=0,
      why="EIN-2.I.5 states that overgrazing can lead to desertification in arid and semi-arid "
          "regions, and that implementing restoration efforts, soil conservation measures, and "
          "improved grazing practices can help slow or reverse the process. Waterlogging and "
          "salinization are EIN-2.F.1 and EIN-2.F.6, and eutrophication is STB-3.F.1."),

 dict(q="Which livestock does the framework single out when it says that eating less meat "
        "can lower emissions?",
      choices=[
        "Ruminant livestock such as cattle and sheep",
        "Poultry such as chickens and turkeys",
        "Farmed fish such as salmon and carp",
        "Pigs raised in confined spaces",
        "The framework singles out no kind of livestock"],
      ans=0,
      why="EIN-2.I.6 states that less consumption of meat, ESPECIALLY FROM RUMINANT LIVESTOCK "
          "SUCH AS CATTLE AND SHEEP, can lower emissions of carbon dioxide, methane and nitrous "
          "oxide. The framework does name a category, so the last option is wrong on its face."),

 dict(q="A household changed its diet for a year and the savings were estimated. What do "
        "the values support?",
      table=_T_DIET,
      choices=[
        "Replacing more of the beef saved more fresh water and avoided more greenhouse "
        "gas emissions.",
        "Replacing more of the beef saved less fresh water and avoided fewer greenhouse "
        "gas emissions.",
        "The two changes saved the same amount of fresh water as making no change.",
        "Replacing all the beef saved fresh water but avoided no greenhouse "
        "gas emissions.",
        "Replacing half the beef saved more fresh water than replacing all of it."],
      ans=0,
      why="The savings run 0, 160 and 320 thousand litres of fresh water and 0, 310 and 620 "
          "kilograms of emissions avoided as more of the beef is replaced. EIN-2.I.6 states "
          "that less consumption of meat can lower emissions of carbon dioxide, methane and "
          "nitrous oxide and conserve freshwater resources."),

 dict(q="Besides lowering emissions and conserving fresh water, what further benefit does "
        "the framework attach to eating less meat?",
      choices=[
        "Reduced reliance on antibiotics and growth hormones",
        "Reduced reliance on irrigation for every crop grown",
        "Increased genetic diversity of every crop grown",
        "Reduced soil compaction in every region of the world",
        "The framework names no further benefit"],
      ans=0,
      why="EIN-2.I.6 states that less meat consumption can lower emissions of carbon dioxide, "
          "methane and nitrous oxide, conserve freshwater resources, AND reduce reliance on "
          "antibiotics and growth hormones. The framework does name that third benefit, so the "
          "last option is wrong on its face."),

 dict(q="What qualification does the framework place on the size of the benefits from "
        "eating less meat?",
      choices=[
        "Their magnitude depends on the production methods applied and on how land no "
        "longer used for livestock is subsequently managed.",
        "Their magnitude is fixed and identical wherever the change is made.",
        "Their magnitude depends only on the number of people who make the change.",
        "Their magnitude depends only on the price of meat in the region.",
        "The framework places no qualification on the size of the benefits."],
      ans=0,
      why="EIN-2.I.6 ends by stating that the magnitude of these benefits depends on the "
          "production methods applied and how land no longer used for livestock is "
          "subsequently managed. The framework does qualify the claim, so the last option "
          "is wrong on its face."),

 dict(q="What does the framework offer, besides eating less meat, as a way of reducing the "
        "environmental impact of meat production?",
      choices=[
        "Advances in feed quality and the use of precision farming technologies",
        "A ban on all pasture-based grazing systems",
        "A move from poultry production to cattle production",
        "An increase in the stocking rate on every pasture",
        "The framework offers nothing besides eating less meat"],
      ans=0,
      why="EIN-2.I.6 states that advances in feed quality and the use of precision farming "
          "technologies can also mitigate environmental impacts. Raising the stocking rate is "
          "what EIN-2.I.4 defines as the route to overgrazing, and the framework offers no ban "
          "and no move toward the higher-emitting livestock."),
]
