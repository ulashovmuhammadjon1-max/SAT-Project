# AP ENVIRONMENTAL SCIENCE 1.4 The Carbon Cycle
# CED effective Fall 2026, Unit 1 The Living World: Ecosystems.
# Enduring understanding ERT-1: Ecosystems are the result of biotic and abiotic
# interactions.
# Learning objective ERT-1.D: explain the steps and reservoir interactions in the carbon
# cycle. Suggested skill 2.B, explain relationships between different characteristics of
# environmental concepts, processes, or models represented visually.
#
# Essential knowledge relied on, in the framework's own words:
#   ERT-1.D.1  The carbon cycle is the movement of atoms and molecules containing the
#              element carbon between sources and sinks.
#   ERT-1.D.2  Some of the reservoirs in which carbon compounds occur in the carbon cycle
#              hold those compounds for long periods of time, while some hold them for
#              relatively short periods of time.
#   ERT-1.D.3  Carbon cycles between photosynthesis and cellular respiration in living
#              things.
#   ERT-1.D.4  Plant and animal decomposition have led to the storage of carbon over
#              millions of years. The burning of fossil fuels quickly moves that stored
#              carbon into atmospheric carbon, in the form of carbon dioxide.
#
# HOW THIS TOPIC IS KEPT DISTINCT FROM 1.5, 1.6 AND 1.7. All four cycle topics share the
# phrase "movement of atoms and molecules ... between sources and sinks", so only ONE
# item here (item 1) asks that definition, and it asks it of carbon specifically. The
# reservoir items here turn on ERT-1.D.2, which is about HOW LONG a reservoir holds
# carbon -- a statement the other three cycles do not carry. Which reservoir is LARGEST is
# a nitrogen fact (ERT-1.E.4), a phosphorus fact (ERT-1.F.2) and a water fact (ERT-1.G.2)
# and is asked in those topics, never here. Nothing here touches nitrogen fixation,
# atmospheric absence, or the phases of water.
#
# NO FIGURES ARE REFERENCED. Where a cycle diagram would normally be shown, the fluxes
# and stores are given as a table instead.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: export_units.py does not typeset
# Environmental Science.
TOPIC = ("1.4", "The Carbon Cycle", 1)

_T_RESIDENCE = dict(
    headers=["Carbon reservoir", "Average time a carbon atom stays in the reservoir (years)"],
    rows=[["Sedimentary rock", "100000000"],
          ["Fossil fuel deposits", "300000000"],
          ["Deep ocean water", "1000"],
          ["Soil organic matter", "30"],
          ["Living plant tissue", "12"]])

_T_FLUX = dict(
    headers=["Process", "Carbon moved each year (billions of tonnes)"],
    rows=[["Photosynthesis on land and in the sea", "220"],
          ["Cellular respiration and decomposition", "218"],
          ["Burning of fossil fuels", "9"]])

_T_TREND = dict(
    headers=["Decade", "Mean atmospheric carbon dioxide (parts per million)",
             "Carbon released by fossil fuel burning each year (billions of tonnes)"],
    rows=[["First decade", "317", "2.5"],
          ["Third decade", "339", "5.3"],
          ["Fifth decade", "369", "6.8"],
          ["Seventh decade", "402", "9.4"]])

_T_POOLS = dict(
    headers=["Carbon pool in one forest", "Carbon stored (tonnes per hectare)"],
    rows=[["Living trees", "124"],
          ["Soil organic matter", "95"],
          ["Dead wood on the ground", "18"],
          ["Leaf litter", "7"]])

_T_LEAF = dict(
    headers=["Litter type placed on the forest floor",
             "Percent of the original carbon still present after two years"],
    rows=[["Soft green leaves", "9"],
          ["Tough evergreen needles", "41"],
          ["Woody twigs", "68"],
          ["Whole branches", "84"]])

_T_SEDIMENT = dict(
    headers=["Setting", "Carbon buried in sediment each year (grams per square meter)",
             "Percent of buried carbon still present after one hundred years"],
    rows=[["Well-drained upland soil", "6", "11"],
          ["Waterlogged peat basin", "94", "88"]])

_T_HARVEST = dict(
    headers=["Stand of forest", "Carbon in living wood (tonnes per hectare)",
             "Carbon released to the air in the year measured (tonnes per hectare)"],
    rows=[["Uncut stand", "138", "1"],
          ["Stand cut and burned", "14", "119"]])

_T_AGE = dict(
    headers=["Carbon-bearing material", "Age of the carbon it contains (years)",
             "Time taken to release that carbon once combustion begins (years)"],
    rows=[["Dried grass in a field fire", "1", "0.01"],
          ["Firewood from a mature tree", "80", "0.01"],
          ["Coal from a deep seam", "300000000", "0.01"]])

QUESTIONS = [

 dict(q="Which statement best defines the carbon cycle as the framework states it?",
      choices=[
        "It is the movement of atoms and molecules containing carbon between sources and "
        "sinks.",
        "It is the creation of new carbon atoms inside living organisms.",
        "It is the destruction of carbon atoms when fuels are burned.",
        "It is the conversion of carbon atoms into nitrogen atoms in the soil.",
        "It is the movement of carbon only within the bodies of living organisms."],
      ans=0,
      why="ERT-1.D.1 states that the carbon cycle is the movement of atoms and molecules "
          "containing the element carbon between sources and sinks. Movement, not "
          "creation or destruction, is what the word cycle carries."),

 dict(q="A student says that burning a fuel destroys the carbon it contained. What is the "
        "best correction?",
      choices=[
        "The carbon is moved into the atmosphere as carbon dioxide rather than destroyed.",
        "The carbon is converted into oxygen atoms rather than destroyed.",
        "The carbon is destroyed, but an equal number of new carbon atoms form in the "
        "soil.",
        "The carbon remains in the fuel deposit and only heat leaves it.",
        "The carbon becomes part of the water cycle instead of the carbon cycle."],
      ans=0,
      why="ERT-1.D.1 describes the cycle as movement between sources and sinks, and "
          "ERT-1.D.4 states specifically that burning fossil fuels moves stored carbon "
          "into atmospheric carbon in the form of carbon dioxide."),

 dict(q="What does the framework say about how long carbon compounds remain in the "
        "reservoirs of the carbon cycle?",
      choices=[
        "Some reservoirs hold them for long periods and some hold them for relatively "
        "short periods.",
        "Every reservoir holds them for the same length of time.",
        "Every reservoir holds them for millions of years.",
        "Every reservoir releases them within a single year.",
        "The length of time cannot differ, because the atoms themselves are identical."],
      ans=0,
      why="ERT-1.D.2 states that some of the reservoirs in which carbon compounds occur "
          "hold those compounds for long periods of time while some hold them for "
          "relatively short periods of time."),

 dict(q="The table gives the average time a carbon atom stays in each of five reservoirs. "
        "Which pairing of reservoir to description is best supported?",
      table=_T_RESIDENCE,
      choices=[
        "Fossil fuel deposits are a long-term store and living plant tissue is a "
        "short-term one.",
        "Living plant tissue is a long-term store and fossil fuel deposits are a "
        "short-term one.",
        "All five reservoirs hold carbon for about the same length of time.",
        "Soil organic matter holds carbon for longer than sedimentary rock does.",
        "Deep ocean water holds carbon for the shortest time of the five."],
      ans=0,
      why="The tabulated residence times differ by more than seven orders of magnitude, "
          "with the two rock and fuel entries far above the rest and living tissue at the "
          "bottom. ERT-1.D.2 is the statement that reservoirs differ in this way."),

 dict(q="Using the same table of residence times, which conclusion about the two "
        "shortest-term reservoirs is best supported?",
      table=_T_RESIDENCE,
      choices=[
        "Carbon held in soil organic matter and in living plant tissue returns to "
        "circulation within decades.",
        "Carbon held in soil organic matter and in living plant tissue returns to "
        "circulation only after millions of years.",
        "Carbon held in soil organic matter stays put longer than carbon in sedimentary "
        "rock.",
        "Carbon held in living plant tissue stays put longer than carbon in deep ocean "
        "water.",
        "Carbon held in fossil fuel deposits returns to circulation faster than carbon in "
        "living tissue."],
      ans=0,
      why="The two smallest tabulated residence times are both measured in tens of years, "
          "which is what makes them the short-period reservoirs ERT-1.D.2 contrasts with "
          "the long-period ones."),

 dict(q="Between which two processes does the framework say carbon cycles in living "
        "things?",
      choices=[
        "Photosynthesis and cellular respiration.",
        "Nitrogen fixation and denitrification.",
        "Evaporation and condensation.",
        "Weathering and sedimentation.",
        "Combustion and precipitation."],
      ans=0,
      why="ERT-1.D.3 states that carbon cycles between photosynthesis and cellular "
          "respiration in living things. The rejected pairs belong to the nitrogen cycle, "
          "the water cycle and rock processes."),

 dict(q="Which process moves carbon from the atmosphere into the organic compounds of "
        "living things?",
      choices=[
        "Photosynthesis.",
        "Cellular respiration.",
        "Combustion of a fossil fuel.",
        "Decomposition of dead tissue.",
        "Burial of sediment on the seafloor."],
      ans=0,
      why="ERT-1.D.3 places photosynthesis and cellular respiration at the two ends of "
          "the living part of the carbon cycle, and ENG-1.A.1 defines primary "
          "productivity as the conversion of solar energy into organic compounds via "
          "photosynthesis, so photosynthesis is the intake step."),

 dict(q="Which process returns carbon from the organic compounds of living things to the "
        "surrounding environment as part of the cycle described in ERT-1.D.3?",
      choices=[
        "Cellular respiration.",
        "Photosynthesis.",
        "Nitrogen fixation.",
        "Condensation of water vapor.",
        "The weathering of phosphorus-bearing rock."],
      ans=0,
      why="ERT-1.D.3 names photosynthesis and cellular respiration as the two processes "
          "between which carbon cycles in living things, and photosynthesis is the "
          "process that builds the organic compounds rather than breaking them down."),

 dict(q="According to the framework, what has led to the storage of carbon over millions "
        "of years?",
      choices=[
        "Plant and animal decomposition.",
        "The burning of fossil fuels.",
        "Nitrogen fixation by soil bacteria.",
        "The evaporation of water from the oceans.",
        "The weathering of phosphorus-bearing rock."],
      ans=0,
      why="ERT-1.D.4 states that plant and animal decomposition have led to the storage "
          "of carbon over millions of years. Combustion is the release step in that same "
          "statement, not the storage step."),

 dict(q="What does the framework say the burning of fossil fuels does to carbon that had "
        "been stored?",
      choices=[
        "It quickly moves that stored carbon into atmospheric carbon in the form of "
        "carbon dioxide.",
        "It slowly moves that stored carbon into the deep ocean over millions of years.",
        "It converts that stored carbon into living plant tissue.",
        "It locks that stored carbon more firmly into the rock it came from.",
        "It removes that carbon from the carbon cycle permanently."],
      ans=0,
      why="ERT-1.D.4 states that the burning of fossil fuels quickly moves stored carbon "
          "into atmospheric carbon, in the form of carbon dioxide. The word quickly is "
          "part of the statement and sets it against the slow storage step."),

 dict(q="The table gives three annual carbon transfers. Which statement is best supported "
        "by these figures?",
      table=_T_FLUX,
      choices=[
        "Photosynthesis and the return processes are close to each other in size, while "
        "fossil fuel burning is a much smaller but additional transfer.",
        "Fossil fuel burning is the largest of the three transfers listed.",
        "Photosynthesis moves less carbon each year than fossil fuel burning does.",
        "Cellular respiration and decomposition move no carbon at all.",
        "All three transfers move the same quantity of carbon each year."],
      ans=0,
      why="The photosynthesis and return figures differ by a small fraction of either, "
          "while the combustion figure is far smaller than both. ERT-1.D.3 pairs the "
          "first two as the living cycle and ERT-1.D.4 adds combustion as a separate "
          "transfer out of long-term storage."),

 dict(q="Atmospheric carbon dioxide and annual fossil fuel emissions were recorded in "
        "four decades, as shown. Which conclusion is best supported?",
      table=_T_TREND,
      choices=[
        "Both quantities rose across the period, which is consistent with combustion "
        "adding stored carbon to the atmosphere.",
        "Atmospheric carbon dioxide rose while fossil fuel emissions fell.",
        "Fossil fuel emissions rose while atmospheric carbon dioxide fell.",
        "Both quantities fell across the period.",
        "Neither quantity changed measurably across the period."],
      ans=0,
      why="Both tabulated columns increase from the first decade to the last. ERT-1.D.4 "
          "states that burning fossil fuels quickly moves stored carbon into atmospheric "
          "carbon in the form of carbon dioxide, which is the direction the data show."),

 dict(q="Carbon stored in four pools of one forest is shown. Which statement is best "
        "supported by the table?",
      table=_T_POOLS,
      choices=[
        "Living trees and soil organic matter together hold more than four fifths of the "
        "carbon in the forest.",
        "Leaf litter holds more carbon than living trees do.",
        "Dead wood on the ground holds the largest share of the forest's carbon.",
        "The four pools each hold about a quarter of the forest's carbon.",
        "Soil organic matter holds no carbon in this forest."],
      ans=0,
      why="Adding the two largest tabulated pools and dividing by the total gives more "
          "than four fifths. ERT-1.D.2 is the framework statement that carbon sits in "
          "reservoirs of different kinds, which is what a pool inventory records."),

 dict(q="Four kinds of plant litter were left on a forest floor and the carbon remaining "
        "after two years was measured, as shown. Which conclusion is best supported?",
      table=_T_LEAF,
      choices=[
        "Softer litter loses its carbon faster, so the same forest holds carbon for "
        "different lengths of time depending on the material.",
        "All four kinds of litter lose their carbon at the same rate.",
        "Whole branches lose their carbon faster than soft green leaves do.",
        "None of the four kinds of litter lost any carbon over the two years.",
        "Tough evergreen needles retained less carbon than soft green leaves did."],
      ans=0,
      why="The percentage still present after two years rises from the softest material "
          "to the woodiest, so the four materials release carbon at different rates. "
          "ERT-1.D.2 is the statement that holding times differ between reservoirs."),

 dict(q="Two settings were compared for carbon burial, as shown. Which conclusion is best "
        "supported?",
      table=_T_SEDIMENT,
      choices=[
        "The waterlogged basin both buries more carbon each year and retains a far larger "
        "share of it, so it acts as the longer-term store.",
        "The well-drained upland soil both buries more carbon each year and retains more "
        "of it.",
        "The two settings bury the same amount of carbon each year.",
        "The waterlogged basin buries more carbon but retains a smaller share of it.",
        "Neither setting retains any buried carbon after one hundred years."],
      ans=0,
      why="The waterlogged basin leads on both tabulated columns, burying more carbon and "
          "keeping a far larger share of it. ERT-1.D.4 attributes long-term carbon "
          "storage to plant and animal decomposition, and ERT-1.D.2 allows reservoirs to "
          "differ in how long they hold it."),

 dict(q="Two forest stands were measured, as shown. Which statement about the cut and "
        "burned stand is best supported?",
      table=_T_HARVEST,
      choices=[
        "Most of the carbon that had been held in living wood was moved to the air in a "
        "single year.",
        "The carbon that had been held in living wood was destroyed rather than moved.",
        "The cut and burned stand released less carbon than the uncut stand did.",
        "The cut and burned stand still holds more carbon in living wood than the uncut "
        "stand does.",
        "The carbon released by the cut and burned stand came from the atmosphere rather "
        "than from the wood."],
      ans=0,
      why="Living wood carbon falls by a large amount while carbon released to the air "
          "rises by a comparable amount in the same stand and year. ERT-1.D.1 makes the "
          "cycle a movement between reservoirs rather than a loss of atoms."),

 dict(q="Three materials were compared for the age of the carbon they contain and how "
        "quickly that carbon is released when burned, as shown. Which conclusion is best "
        "supported?",
      table=_T_AGE,
      choices=[
        "Burning releases carbon in about the same short time whatever its age, so "
        "burning coal returns far older carbon to the air than burning grass does.",
        "Older carbon takes correspondingly longer to release when burned.",
        "The three materials contain carbon of about the same age.",
        "Burning grass returns older carbon to the air than burning coal does.",
        "None of the three materials releases its carbon within a year of ignition."],
      ans=0,
      why="The release-time column is identical across the three rows while the age column "
          "spans hundreds of millions of years. ERT-1.D.4 makes exactly this contrast, "
          "between carbon stored over millions of years and combustion that moves it "
          "quickly."),

 dict(q="Why does the framework treat the burning of fossil fuels differently from the "
        "decay of a fallen leaf, even though both release carbon dioxide?",
      choices=[
        "Because combustion of fossil fuels quickly returns carbon that had been stored "
        "for millions of years, rather than carbon taken up recently.",
        "Because the decay of a leaf releases no carbon at all.",
        "Because combustion of fossil fuels destroys carbon atoms while decay does not.",
        "Because the decay of a leaf takes millions of years to complete.",
        "Because combustion of fossil fuels removes carbon from the cycle permanently."],
      ans=0,
      why="ERT-1.D.4 sets storage over millions of years against a quick return by "
          "combustion, so the distinguishing feature is the age of the carbon and the "
          "speed of its release, not whether carbon dioxide is produced."),

 dict(q="A carbon sink is best described as which of the following?",
      choices=[
        "A place into which carbon moves and is held.",
        "A place from which carbon is released into circulation.",
        "A chemical reaction that destroys carbon atoms.",
        "A measure of how much carbon an organism contains at one instant.",
        "A process that converts carbon atoms into another element."],
      ans=0,
      why="ERT-1.D.1 describes the carbon cycle as movement between sources and sinks, "
          "which pairs a place carbon leaves with a place carbon enters. Nothing in the "
          "framework has carbon atoms destroyed or transmuted."),

 dict(q="A tract of forest is cleared and the wood is burned, and no new trees are "
        "planted. Which change to the local carbon cycle does the framework most directly "
        "support predicting?",
      choices=[
        "Less carbon is taken up by photosynthesis there and more carbon has been moved "
        "into the atmosphere.",
        "More carbon is taken up by photosynthesis there and less carbon is in the "
        "atmosphere.",
        "The carbon that had been in the trees is destroyed and leaves the cycle.",
        "Carbon uptake and carbon release are both unaffected by removing the trees.",
        "The carbon released is stored again within a single year in sedimentary rock."],
      ans=0,
      why="ERT-1.D.3 makes photosynthesis the uptake step of the living carbon cycle, so "
          "removing the photosynthesizers removes the uptake, and ERT-1.D.1 makes the "
          "burning a movement of that carbon into another reservoir rather than a loss."),

 dict(q="Which of the following would count as evidence that a particular reservoir is a "
        "long-term carbon store?",
      choices=[
        "Carbon placed in it is still measurably present after very long spans of time.",
        "It contains a large mass of carbon at the moment it is measured.",
        "It exchanges carbon with the atmosphere many times each year.",
        "The carbon within it is chemically identical to carbon elsewhere.",
        "It lies at a greater depth than the reservoirs around it."],
      ans=0,
      why="ERT-1.D.2 distinguishes reservoirs by how long they hold carbon compounds, so "
          "the evidence that bears on it is retention over time. A large standing mass "
          "and a great depth say nothing about the holding time."),

 dict(q="A student claims that because carbon cycles between photosynthesis and cellular "
        "respiration, the amount of carbon on Earth increases whenever plants grow. What "
        "is the best correction?",
      choices=[
        "Growth moves carbon into plant tissue from elsewhere; it does not add carbon to "
        "the Earth.",
        "Growth does add carbon to the Earth, so the student is correct as stated.",
        "Growth removes carbon from the Earth permanently.",
        "Growth converts carbon atoms into oxygen atoms.",
        "Growth affects only the nitrogen cycle, not the carbon cycle."],
      ans=0,
      why="ERT-1.D.1 defines the cycle as movement of carbon-containing atoms and "
          "molecules between sources and sinks, so an increase in one reservoir is a "
          "transfer out of another rather than the appearance of new carbon."),

 dict(q="Which comparison correctly matches a process from the carbon cycle to the "
        "direction it moves carbon?",
      choices=[
        "Photosynthesis moves carbon out of the atmosphere; combustion of fossil fuels "
        "moves carbon into it.",
        "Photosynthesis moves carbon into the atmosphere; combustion of fossil fuels "
        "moves carbon out of it.",
        "Both photosynthesis and combustion of fossil fuels move carbon out of the "
        "atmosphere.",
        "Both photosynthesis and combustion of fossil fuels move carbon into the "
        "atmosphere.",
        "Neither photosynthesis nor combustion of fossil fuels changes the carbon in the "
        "atmosphere."],
      ans=0,
      why="ERT-1.D.3 makes photosynthesis the step that builds organic compounds, and "
          "ERT-1.D.4 states that burning fossil fuels moves stored carbon into "
          "atmospheric carbon dioxide, so the two run in opposite directions."),

 dict(q="Carbon that has been in a fossil fuel deposit for hundreds of millions of years "
        "is burned and enters the air. Which framework statement does that sequence "
        "illustrate most directly?",
      choices=[
        "Decomposition stored carbon over millions of years and combustion quickly "
        "returns it as carbon dioxide.",
        "Reservoirs of carbon all hold their contents for the same length of time.",
        "Carbon cycles between photosynthesis and cellular respiration in living things.",
        "The carbon cycle is confined to living organisms.",
        "Carbon atoms are created in fossil fuel deposits and destroyed in the air."],
      ans=0,
      why="ERT-1.D.4 contains both halves of the sequence: plant and animal decomposition "
          "led to storage over millions of years, and burning fossil fuels quickly moves "
          "that stored carbon into atmospheric carbon dioxide."),

 dict(q="Two soils hold the same total mass of carbon, but one returns most of its carbon "
        "to the air within a decade while the other holds most of its carbon for "
        "centuries. Which framework statement does this contrast illustrate?",
      choices=[
        "Some reservoirs hold carbon compounds for long periods and some for relatively "
        "short periods.",
        "The carbon cycle is the movement of carbon between sources and sinks.",
        "Carbon cycles between photosynthesis and cellular respiration.",
        "Burning fossil fuels quickly moves stored carbon into the atmosphere.",
        "Plant and animal decomposition stored carbon over millions of years."],
      ans=0,
      why="The two soils are matched on the quantity of carbon and differ only in how "
          "long they keep it, which is precisely the distinction ERT-1.D.2 draws between "
          "long-period and short-period reservoirs."),

 dict(q="An investigator wants to show that a wetland is acting as a carbon sink rather "
        "than a carbon source. Which measurement would be most directly relevant?",
      choices=[
        "Whether more carbon enters the wetland's soils and plants each year than leaves "
        "them.",
        "Whether the wetland contains more plant species than a neighboring field.",
        "Whether the wetland is deeper than a neighboring pond.",
        "Whether the carbon in the wetland is the same element as the carbon in a fuel.",
        "Whether the wetland freezes in winter."],
      ans=0,
      why="ERT-1.D.1 makes a sink a destination in the movement of carbon between sources "
          "and sinks, so the relevant measurement is the balance of carbon entering "
          "against carbon leaving over a period."),

 dict(q="Which of the following pairs a carbon source with a carbon sink correctly?",
      choices=[
        "A burning coal seam is a source and a growing forest is a sink.",
        "A growing forest is a source and a burning coal seam is a sink.",
        "Both a burning coal seam and a growing forest are sources.",
        "Both a burning coal seam and a growing forest are sinks.",
        "Neither a burning coal seam nor a growing forest exchanges carbon with the "
        "atmosphere."],
      ans=0,
      why="ERT-1.D.4 has combustion moving stored carbon into the atmosphere, which makes "
          "it a source, and ERT-1.D.3 has photosynthesis building organic compounds in "
          "growing plants, which makes a growing forest a destination."),

 dict(q="Why does the framework describe the storage of carbon in fossil fuel deposits as "
        "having taken millions of years?",
      choices=[
        "Because that storage arose from the decomposition of plants and animals "
        "accumulating over those spans.",
        "Because carbon atoms take millions of years to form.",
        "Because photosynthesis operates only once every million years.",
        "Because the deposits are burned at the same rate at which they formed.",
        "Because the atmosphere held no carbon dioxide until the deposits formed."],
      ans=0,
      why="ERT-1.D.4 states that plant and animal decomposition have led to the storage "
          "of carbon over millions of years, so the timescale belongs to the accumulation "
          "of decomposed material rather than to any property of the atoms."),

 dict(q="Which statement best explains why moving carbon out of a long-term reservoir "
        "matters for the atmosphere, even though the total amount of carbon on Earth does "
        "not change?",
      choices=[
        "Carbon that was held out of circulation for a very long time is added to a "
        "reservoir that exchanges rapidly, so the amount in that reservoir rises.",
        "Carbon that was held out of circulation is destroyed on release, so the total "
        "falls.",
        "The total amount of carbon on Earth does change, because combustion creates "
        "carbon.",
        "Long-term reservoirs and the atmosphere hold carbon for the same length of time, "
        "so nothing changes.",
        "Carbon released from a long-term reservoir cannot enter the atmosphere."],
      ans=0,
      why="ERT-1.D.1 makes the cycle a redistribution between reservoirs and ERT-1.D.2 "
          "makes those reservoirs differ in holding time, so a transfer from a slow "
          "reservoir to a fast one raises the content of the fast one without changing "
          "the total."),

 dict(q="Which sequence correctly traces one carbon atom through the living part of the "
        "carbon cycle as the framework describes it?",
      choices=[
        "Taken from the air into a plant by photosynthesis, then returned to the air by "
        "cellular respiration.",
        "Taken from the air into a plant by cellular respiration, then returned to the "
        "air by photosynthesis.",
        "Taken from rock into a plant by nitrogen fixation, then returned by "
        "denitrification.",
        "Taken from the ocean into a plant by evaporation, then returned by "
        "precipitation.",
        "Created inside a plant during growth, then destroyed during respiration."],
      ans=0,
      why="ERT-1.D.3 states that carbon cycles between photosynthesis and cellular "
          "respiration in living things, and photosynthesis is the step that builds "
          "organic compounds while respiration is the step that breaks them down."),
]
