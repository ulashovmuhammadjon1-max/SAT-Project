# AP ENVIRONMENTAL SCIENCE 8.1 Sources of Pollution
# CED effective Fall 2026, Unit 8 Aquatic and Terrestrial Pollution. Enduring
# understanding STB-3: human activities, including the use of resources, have physical,
# chemical, and biological consequences for ecosystems.
# Learning objective STB-3.A: identify differences between point and nonpoint sources
# of pollution. Suggested skill 1.A, describe environmental concepts and processes.
#
# Essential knowledge relied on, in the framework's own words:
#   STB-3.A.1  A point source refers to a single, identifiable source of a pollutant,
#              such as a smokestack or waste discharge pipe.
#   STB-3.A.2  Nonpoint sources of pollution are diffused and can therefore be
#              difficult to identify, such as pesticide spraying or urban runoff.
#
# WHAT THE TWO STATEMENTS SUPPORT AND WHAT THEY DO NOT. The framework gives the
# distinction, two examples of each kind, and the reason nonpoint sources are hard to
# identify: they are diffused. Everything keyed here follows from that. Two
# consequences are used as such and are stated so a reader can check them: a source
# that can be identified singly can be measured and traced at its outlet, and a source
# that is diffused cannot, which is what STB-3.A.2's "difficult to identify" means.
#
# NOT KEYED: any statute, permit system, agency, treatment requirement or numerical
# limit. The framework names none in this topic, and the effects of particular
# pollutants belong to 8.2 and later topics rather than here.
#
# FIVE choices (A-E). No LaTeX and no non-ASCII: export_units.py does not typeset
# ENV_SCI.
TOPIC = ("8.1", "Sources of Pollution", 8)

_T_LOADS = dict(
    headers=["Contributor to one river's pollutant load",
             "Load measured or estimated (tons per year)",
             "Can the contribution be measured at a single outlet"],
    rows=[["Factory discharge pipe", "120", "yes"],
          ["Municipal treatment plant outfall", "80", "yes"],
          ["Runoff from farmland across the basin", "260", "no"],
          ["Runoff from streets and parking lots", "140", "no"]])

_T_STORM = dict(
    headers=["Sampling time relative to a rainstorm",
             "Suspended sediment in the creek (milligrams per liter)",
             "Pesticide in the creek (micrograms per liter)"],
    rows=[["Two days before the storm", "12", "0.2"],
          ["During the storm", "310", "4.8"],
          ["Two days after the storm", "35", "0.9"]])

_T_TRACE = dict(
    headers=["Sampling point on the river",
             "Position relative to a factory discharge pipe",
             "Metal concentration (micrograms per liter)"],
    rows=[["Point 1", "500 meters upstream", "2"],
          ["Point 2", "100 meters upstream", "2"],
          ["Point 3", "100 meters downstream", "46"],
          ["Point 4", "2 kilometers downstream", "28"]])

_T_BASIN = dict(
    headers=["Land cover in the sub-basin",
             "Share of the sub-basin (percent)",
             "Nitrogen delivered to the stream (kilograms per year)"],
    rows=[["Cropland", "60", "4,800"],
          ["Pasture", "25", "1,500"],
          ["Forest", "15", "200"]])

_T_PIPES = dict(
    headers=["Year of the permit program",
             "Pollutant released from identified discharge pipes (tons per year)",
             "Pollutant reaching the bay from all other sources (tons per year)"],
    rows=[["Year 1", "900", "700"],
          ["Year 5", "500", "680"],
          ["Year 10", "180", "650"]])

_T_SITES = dict(
    headers=["Suspected contributor to a lake's pollution",
             "Number of separate locations releasing the pollutant"],
    rows=[["Cannery outfall", "1"],
          ["Power plant cooling discharge", "1"],
          ["Lawn treatment across the surrounding suburb", "3,400"]])

QUESTIONS = [

 dict(q="How does the framework define a point source of pollution?",
      choices=[
        "A single, identifiable source of a pollutant, such as a smokestack or a waste "
        "discharge pipe",
        "Any source that releases pollution during a single day",
        "A source that releases pollution at a single moment and never again",
        "A source that releases only one kind of pollutant",
        "A source located at a single elevation above sea level"],
      ans=0,
      why="The framework defines a point source as a single, identifiable source of a "
          "pollutant and gives a smokestack and a waste discharge pipe as its examples. "
          "The definition is about being one identifiable place, not about the timing, "
          "the number of pollutants, or the elevation."),

 dict(q="How does the framework describe nonpoint sources of pollution?",
      choices=[
        "They are diffused and can therefore be difficult to identify, such as pesticide "
        "spraying or urban runoff",
        "They are concentrated at one outlet and easy to identify",
        "They release pollutants only into the air and never into water",
        "They are always smaller in total than point sources",
        "They occur only in places with no human activity"],
      ans=0,
      why="The framework states that nonpoint sources are diffused and can therefore be "
          "difficult to identify, and gives pesticide spraying and urban runoff as "
          "examples. Being diffused is exactly the opposite of being concentrated at one "
          "identifiable outlet."),

 dict(q="Which of the following is a point source of water pollution?",
      choices=[
        "A pipe discharging treated wastewater into a river at one location",
        "Fertilizer washing off many fields across a watershed after rain",
        "Pesticide drifting from spraying across a large orchard district",
        "Oil dripping from vehicles onto streets throughout a city",
        "Sediment eroding from construction sites scattered across a county"],
      ans=0,
      why="A discharge pipe is one of the framework's own examples of a single, "
          "identifiable source. Each rejected option describes releases spread over many "
          "places, which is what makes a source diffused and hard to identify."),

 dict(q="Which of the following is a nonpoint source of water pollution?",
      choices=[
        "Runoff carrying lawn chemicals from thousands of yards across a suburb",
        "A single outfall from a food processing plant",
        "The exhaust stack of one power station",
        "A leaking valve on one storage tank at one refinery",
        "A single ditch draining one feedlot into a creek"],
      ans=0,
      why="Runoff from thousands of separate yards is diffused across the landscape, "
          "which is the framework's description of a nonpoint source, and urban runoff "
          "is one of its own examples. Each rejected option names one identifiable "
          "release location."),

 dict(q="Contributions to one river's pollutant load are shown.",
      table=_T_LOADS,
      choices=[
        "The two contributions that cannot be measured at a single outlet together "
        "deliver more of the load than the two that can",
        "The two contributions measurable at a single outlet deliver more of the load",
        "All four contributions deliver equal shares of the load",
        "Only the contributions measurable at a single outlet deliver any load at all",
        "The largest single contribution comes from the factory discharge pipe"],
      ans=0,
      why="The two rows marked as not measurable at a single outlet total four hundred "
          "tons against two hundred for the two that are, so the diffused contributions "
          "are the larger share. The framework's nonpoint sources are exactly the ones "
          "that cannot be pinned to one outlet."),

 dict(q="Why does the framework say nonpoint sources can be difficult to identify?",
      choices=[
        "The pollution enters from many places spread across the landscape rather than "
        "from one location",
        "The pollutants they release are invisible while point source pollutants are not",
        "They release pollution only at night",
        "They release smaller quantities than any point source",
        "The pollutants they release cannot be measured by any instrument"],
      ans=0,
      why="The framework's own reason is that nonpoint sources are diffused. Nothing in "
          "the statement turns on visibility, the time of release, the quantity, or "
          "whether an instrument can detect the pollutant once it is in the water."),

 dict(q="Creek measurements taken around one rainstorm are shown.",
      table=_T_STORM,
      choices=[
        "Both sediment and pesticide rose sharply during the storm and remained above "
        "the pre-storm level afterward, a pattern consistent with washoff from across "
        "the landscape",
        "Both measurements fell during the storm",
        "Sediment rose during the storm but pesticide fell",
        "Both measurements were unchanged by the storm",
        "The pre-storm sample carried the highest values of the three"],
      ans=0,
      why="Each column rises by more than an order of magnitude during the storm and is "
          "still above its pre-storm value two days later. A pulse tied to rainfall "
          "rather than to a steady outlet is what diffused sources such as pesticide "
          "spraying and urban runoff produce."),

 dict(q="River measurements around one factory are shown.",
      table=_T_TRACE,
      choices=[
        "The metal concentration is low at both upstream points and much higher "
        "immediately downstream, which identifies the discharge as the source",
        "The metal concentration is highest at the farthest upstream point",
        "The metal concentration is the same at all four points",
        "The metal concentration rises steadily with distance downstream",
        "The measurements cannot distinguish upstream from downstream conditions"],
      ans=0,
      why="Both upstream points carry the same small value and the value jumps more than "
          "twentyfold just below the pipe before falling further downstream. Being "
          "traceable to one identifiable location in this way is what makes the "
          "discharge a point source."),

 dict(q="Which of the following best explains why a point source is usually easier to "
        "monitor than a nonpoint source?",
      choices=[
        "The release passes through one identifiable location, so a sample taken there "
        "captures what that source contributes",
        "A point source always releases less pollution than a nonpoint source",
        "A point source releases pollutants that cannot dissolve in water",
        "A nonpoint source releases pollutants that no instrument can measure",
        "A point source operates only when a nonpoint source is inactive"],
      ans=0,
      why="The framework defines a point source as single and identifiable, which is "
          "what makes one sampling location sufficient, and describes nonpoint sources "
          "as diffused. The comparison is about where the pollution enters, not about "
          "quantity, solubility, or timing."),

 dict(q="Nitrogen delivery from three land covers in one sub-basin is shown.",
      table=_T_BASIN,
      choices=[
        "Cropland delivers the most nitrogen of the three land covers, and the delivery "
        "is spread across the whole area of that land rather than issuing from one point",
        "Forest delivers the most nitrogen of the three land covers",
        "All three land covers deliver the same amount of nitrogen",
        "The land cover with the smallest share of the sub-basin delivers the most "
        "nitrogen",
        "The nitrogen from these land covers enters the stream through a single pipe"],
      ans=0,
      why="Cropland carries both the largest share of the sub-basin and by far the "
          "largest nitrogen delivery in the table. Delivery from a land cover spread "
          "across a basin is diffused rather than issuing from one identifiable outlet."),

 dict(q="A regulator can require a permit for each discharge pipe entering a bay but "
        "finds it far harder to control the pollution carried in by runoff. Which "
        "framework distinction explains the difference?",
      choices=[
        "A discharge pipe is a single, identifiable source, while runoff is diffused and "
        "difficult to identify",
        "A discharge pipe releases pollution while runoff releases only clean water",
        "Runoff is a point source and a discharge pipe is a nonpoint source",
        "Runoff occurs only in rural areas where no rules apply",
        "A discharge pipe releases pollution only during storms"],
      ans=0,
      why="The framework's distinction is exactly this: a point source is single and "
          "identifiable, while nonpoint sources are diffused and therefore difficult to "
          "identify. Reversing the two labels or denying that runoff carries pollution "
          "contradicts the framework's own examples."),

 dict(q="Measurements from a program that limited discharges from identified pipes are "
        "shown.",
      table=_T_PIPES,
      choices=[
        "The load from identified pipes fell sharply while the load from all other "
        "sources changed little, so the remaining pollution comes mostly from sources "
        "that were not addressed",
        "Both the pipe load and the other load fell by the same fraction",
        "The load from other sources fell faster than the load from pipes",
        "The load from identified pipes rose across the program",
        "The two loads were equal in every year of the program"],
      ans=0,
      why="The pipe load falls to a fifth of its starting value while the other load "
          "falls by only a small fraction, so by the final year most of what reaches the "
          "bay comes from sources outside the program. Those are the diffused sources "
          "the framework describes as difficult to identify."),

 dict(q="Suspected contributors to a lake's pollution are listed.",
      table=_T_SITES,
      choices=[
        "The lawn treatment is the diffused contributor, since the pollutant enters from "
        "thousands of separate locations rather than from one",
        "The cannery outfall is the diffused contributor",
        "All three contributors are diffused",
        "None of the three contributors is diffused",
        "The power plant discharge is diffused because it involves cooling water"],
      ans=0,
      why="Two rows name a single release location each and the third names thousands, "
          "and being spread across many locations is what the framework means by "
          "diffused. The nature of the discharge, cooling or otherwise, is not the test."),

 dict(q="Which pair of examples does the framework itself give for nonpoint sources?",
      choices=[
        "Pesticide spraying and urban runoff",
        "A smokestack and a waste discharge pipe",
        "A sewage outfall and a factory drain",
        "A landfill liner and a leachate collection system",
        "A catalytic converter and a vapor recovery nozzle"],
      ans=0,
      why="Pesticide spraying and urban runoff are the framework's own examples of "
          "nonpoint sources. A smokestack and a waste discharge pipe are its examples of "
          "point sources, and the remaining options are landfill components and air "
          "pollution control devices."),

 dict(q="A stream shows the same elevated pollutant concentration at every point along a "
        "twenty kilometer reach with no change at any particular location. Which "
        "conclusion is best supported?",
      choices=[
        "The pollutant is probably entering from diffused sources along the reach rather "
        "than from one identifiable outlet",
        "The pollutant must be entering from a single pipe at the top of the reach",
        "The pollutant cannot be entering the stream at all",
        "The pollutant is entering from a smokestack directly above the stream",
        "The measurements must be mistaken, since pollution always has one source"],
      ans=0,
      why="A single identifiable outlet produces a step change at its location, which is "
          "what these measurements lack. Entry spread along the reach is what the "
          "framework calls diffused, and it is the pattern that fits the data."),

 dict(q="Which of the following would most help an investigator decide whether a "
        "pollutant in a river comes from a point source?",
      choices=[
        "Samples taken immediately upstream and immediately downstream of each suspected "
        "outlet",
        "A single sample taken at the river mouth",
        "The total area of the river basin",
        "The number of people living in the basin",
        "The average rainfall of the basin over the past decade"],
      ans=0,
      why="A point source is single and identifiable, so the test is whether the "
          "concentration steps up across one location. A single sample far downstream, a "
          "basin area, a population count and a rainfall average cannot show that."),

 dict(q="A smokestack releasing pollutants into the air is classified as a point source. "
        "Why does that classification apply even though the pollution disperses widely "
        "after release?",
      choices=[
        "The classification describes where the pollution enters the environment, which "
        "in this case is one identifiable location",
        "The classification describes where the pollution ends up after it disperses",
        "The classification applies only to pollution that does not move",
        "The classification depends on how many people are affected",
        "The classification depends on the quantity released each year"],
      ans=0,
      why="The framework's definition is about the source being single and identifiable, "
          "and it names a smokestack as an example, so what happens to the plume "
          "afterward does not change the classification. Quantity and the number of "
          "people affected are not part of the definition."),

 dict(q="Which statement best describes what makes urban runoff a nonpoint source?",
      choices=[
        "Water picks up pollutants from streets, roofs and yards across the whole built "
        "area before reaching a waterway",
        "Runoff is collected in one pipe before it is released",
        "Runoff contains only one pollutant",
        "Runoff occurs only where there are no buildings",
        "Runoff carries pollution upward into the atmosphere"],
      ans=0,
      why="Urban runoff is one of the framework's own examples of a diffused source, and "
          "it is diffused because the pollution is picked up across the whole developed "
          "surface. Collection in a single pipe would make the release identifiable "
          "instead."),

 dict(q="Two watersheds deliver similar total loads of the same pollutant to a lake. In "
        "one the load comes from three permitted outfalls; in the other it comes from "
        "farmland across the basin. Which difference follows from the framework?",
      choices=[
        "The first load can be traced to identifiable sources while the second is "
        "diffused and harder to attribute",
        "The first load is diffused while the second can be traced to identifiable "
        "sources",
        "Only the first load counts as pollution",
        "Only the second load can be measured in the lake",
        "The two loads must have different chemical compositions"],
      ans=0,
      why="Three outfalls are three single, identifiable sources, while delivery from "
          "farmland across a basin is diffused. The distinction concerns how the "
          "pollution enters, not whether it is pollution, whether it can be measured, or "
          "what it is made of."),

 dict(q="Which observation would best support a claim that a particular pipe is a point "
        "source of a pollutant in a stream?",
      choices=[
        "The concentration is low above the pipe and rises sharply just below it, "
        "consistently across repeated sampling",
        "The concentration is the same above and below the pipe",
        "The pipe is larger than other pipes in the area",
        "The concentration in the stream rises after every rainstorm",
        "The pipe belongs to the largest business in the town"],
      ans=0,
      why="A single identifiable source shows as a step increase across its own "
          "location, repeated across samples. Equal concentrations above and below would "
          "refute the claim, and pipe size, ownership and a rainfall response point "
          "elsewhere."),

 dict(q="An agency reduces the pollutant load a lake receives from every identified "
        "outfall to nearly zero, but the lake remains polluted. Which explanation is "
        "best supported by the framework?",
      choices=[
        "Diffused sources across the surrounding land are still delivering the pollutant",
        "Pollution can only come from identified outfalls, so the measurements must be "
        "wrong",
        "The lake is producing the pollutant on its own",
        "The outfalls must have been nonpoint sources all along",
        "Pollution stops being pollution once outfalls are controlled"],
      ans=0,
      why="The framework recognizes two kinds of source, and controlling the identifiable "
          "ones leaves the diffused ones, which it describes as difficult to identify. "
          "An outfall is by definition a single identifiable location, so it is not a "
          "nonpoint source."),

 dict(q="Which of the following is the clearest example of the framework's smokestack "
        "case applied to water?",
      choices=[
        "A single pipe carrying process water from one plant into a canal",
        "Spray drift from crop dusting over a farming district",
        "Salt washing off many roads after winter treatment",
        "Sediment from erosion across a deforested hillside",
        "Litter blown from many streets into a storm drain network"],
      ans=0,
      why="The framework pairs a smokestack with a waste discharge pipe as its two "
          "examples of a single, identifiable source, so the water analogue is one pipe "
          "from one plant. Every rejected option describes release spread over an area."),

 dict(q="Why can the same pollutant reach a river from both a point source and a "
        "nonpoint source?",
      choices=[
        "The classification describes how the pollutant enters the water, not what the "
        "pollutant is",
        "Each pollutant can only ever have one kind of source",
        "Point sources release different chemicals from those nonpoint sources release",
        "A pollutant changes its identity depending on how it enters the water",
        "Nonpoint sources release only substances that are harmless"],
      ans=0,
      why="The framework's distinction is about the source being single and identifiable "
          "or diffused, which says nothing about the chemical identity of what is "
          "released. The same substance can therefore arrive by either route."),

 dict(q="A study finds that pollutant concentrations in a creek rise sharply only during "
        "and after rainfall and stay low in dry weather. Which source type does this "
        "pattern most suggest?",
      choices=[
        "A diffused source, since rain is what carries pollutants from across the "
        "landscape into the creek",
        "A single discharge pipe operating continuously",
        "A smokestack releasing directly into the creek",
        "A source that releases only in dry weather",
        "No source at all, since the creek is clean between storms"],
      ans=0,
      why="A continuous outlet would raise concentrations in dry weather as well, so the "
          "rainfall dependence points to material carried in from across the surrounding "
          "land, which is the diffused case the framework describes."),

 dict(q="Which of the following best describes why identifying the source type matters "
        "for addressing a pollution problem?",
      choices=[
        "A source that can be identified singly can be addressed at that location, while "
        "a diffused source has to be addressed across the area producing it",
        "Only point sources cause measurable harm",
        "Only nonpoint sources can be reduced",
        "The source type determines which pollutants are dangerous",
        "The source type determines how deep the water body is"],
      ans=0,
      why="The framework's distinction turns on whether the release is single and "
          "identifiable or diffused, which is exactly what determines whether there is "
          "one place to act on. It makes no claim that one type is harmless or "
          "irreducible."),

 dict(q="A student writes that a nonpoint source is simply a small point source. What is "
        "the clearest correction?",
      choices=[
        "A nonpoint source is diffused across many locations rather than being one "
        "location of any size",
        "A nonpoint source is a point source that operates only occasionally",
        "A nonpoint source is a point source located outdoors",
        "A nonpoint source releases the same pollutants as a point source, so the terms "
        "are interchangeable",
        "A nonpoint source is a point source whose owner is unknown"],
      ans=0,
      why="The framework's contrast is between a single identifiable source and a "
          "diffused one, so the difference is the spread of the release rather than its "
          "size, its schedule, its setting or the identity of its owner."),

 dict(q="Which measurement design would best estimate how much of a bay's pollutant load "
        "comes from diffused sources?",
      choices=[
        "Measure the total load reaching the bay and subtract the load measured at every "
        "identified outfall",
        "Measure the load at one outfall and assume it is the whole load",
        "Measure the depth of the bay at several points",
        "Count the number of businesses near the bay",
        "Measure the load reaching a different bay in another region"],
      ans=0,
      why="The diffused contribution is what remains once the identifiable contributions "
          "have been measured and accounted for, which is what the subtraction gives. "
          "Depth, business counts and another bay's load do not bear on this bay's "
          "sources."),

 dict(q="Which of the following pairs correctly matches a source with its type?",
      choices=[
        "A waste discharge pipe, point source",
        "A waste discharge pipe, nonpoint source",
        "Pesticide spraying across a district, point source",
        "Urban runoff from a whole city, point source",
        "A smokestack, nonpoint source"],
      ans=0,
      why="The framework names a waste discharge pipe and a smokestack as point sources "
          "and pesticide spraying and urban runoff as nonpoint sources. Each rejected "
          "pairing reverses one of those four assignments."),

 dict(q="A city argues that it should not be held responsible for the pollution in its "
        "harbor because no single facility can be shown to have released it. How does "
        "the framework bear on that argument?",
      choices=[
        "The framework recognizes diffused sources whose contributions are difficult to "
        "identify, so the absence of one identifiable facility does not mean the "
        "pollution has no human source",
        "The framework recognizes only point sources, so the argument is correct",
        "The framework treats all pollution as natural in origin",
        "The framework holds that pollution without an identified source cannot be "
        "measured",
        "The framework treats urban runoff as a single identifiable source"],
      ans=0,
      why="The framework's second statement exists precisely for pollution that cannot "
          "be traced to one location: nonpoint sources are diffused and therefore "
          "difficult to identify, and urban runoff is its own example of one."),

 dict(q="Which summary best captures the distinction this topic asks students to make?",
      choices=[
        "Pollution entering from one identifiable location is a point source, and "
        "pollution entering from many places across the landscape is a nonpoint source "
        "that is harder to identify",
        "Pollution in water is a point source and pollution in air is a nonpoint source",
        "Pollution that is visible is a point source and pollution that is invisible is "
        "a nonpoint source",
        "Pollution released legally is a point source and pollution released illegally "
        "is a nonpoint source",
        "Pollution from industry is a point source and pollution from any other activity "
        "is a nonpoint source"],
      ans=0,
      why="The framework's two statements distinguish a single, identifiable source from "
          "a diffused one that is difficult to identify, and its examples include both "
          "air and water. Visibility, legality and the sector of the economy are not "
          "part of the distinction."),
]
