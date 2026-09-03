# AP ENVIRONMENTAL SCIENCE 7.1 Introduction to Air Pollution
# CED effective Fall 2026, Unit 7 Atmospheric Pollution. Big Idea 4 Sustainability.
# Enduring understanding STB-2: human activities have physical, chemical, and
# biological consequences for the atmosphere.
# Learning objective STB-2.A: identify the sources and effects of air pollutants.
# Suggested skill 4.E, explain modifications to an experimental procedure that will
# alter results.
#
# Essential knowledge relied on, in the framework's own words:
#   STB-2.A.1  Coal combustion releases air pollutants including carbon dioxide,
#              sulfur dioxide, toxic metals, and particulates.
#   STB-2.A.2  The combustion of fossil fuels releases nitrogen oxides into the
#              atmosphere. They lead to the production of ozone, formation of
#              photochemical smog, and convert to nitric acid in the atmosphere,
#              causing acid rain. Other pollutants produced by fossil fuel combustion
#              include carbon monoxide, hydrocarbons, and particulate matter.
#   STB-2.A.3  Air quality can be affected through the release of sulfur dioxide
#              during the burning of fossil fuels, mainly diesel fuels.
#   STB-2.A.4  Through the Clean Air Act, the Environmental Protection Agency (EPA)
#              regulated the use of lead, particularly in fuels, which dramatically
#              decreased the amount of lead in the atmosphere.
#   STB-2.A.5  Air pollutants can be primary or secondary pollutants.
#
# ON PRIMARY AND SECONDARY. STB-2.A.5 names the two categories and does not define
# them. The only definitional content presupposed anywhere in this module is that a
# primary pollutant is released directly into the air by its source and a secondary
# one forms in the atmosphere out of something already released -- which is the
# minimum the framework's own example requires, since STB-2.A.2 has nitrogen oxides
# released by combustion and then LEADING TO ozone and CONVERTING TO nitric acid.
# Where an item asks a student to sort a pollutant into a category, the sorting
# information is given in the stem or the table, never assumed from memory.
#
# ON SCOPE. The mechanism by which photochemical smog forms belongs to topic 7.2,
# the effects of acid deposition to 7.7, indoor sources to 7.5, and control devices
# to 7.6. This topic keys only the sources named in STB-2.A.1 to STB-2.A.4 and the
# primary/secondary distinction of STB-2.A.5.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX and no non-ASCII: export_units.py
# does not typeset ENV_SCI.
TOPIC = ("7.1", "I ntroduction to Air Pollution", 7)

_T_COAL = dict(
    headers=["Pollutant measured in the stack gas",
             "Mass released per gigajoule of heat produced (grams)"],
    rows=[["Carbon dioxide", "94,000"],
          ["Sulfur dioxide", "900"],
          ["Nitrogen oxides", "300"],
          ["Particulate matter", "60"],
          ["Toxic metals", "2"]])

_T_LEAD = dict(
    headers=["Year", "Lead in gasoline sold nationally (grams per liter)",
             "Lead measured in urban air (micrograms per cubic meter)"],
    rows=[["1975", "0.60", "1.20"],
          ["1980", "0.30", "0.60"],
          ["1985", "0.10", "0.20"],
          ["1990", "0.01", "0.05"]])

_T_FUELS = dict(
    headers=["Fuel burned in a delivery fleet",
             "Sulfur dioxide released per 100 liters burned (grams)"],
    rows=[["Diesel", "160"],
          ["Gasoline", "12"],
          ["Compressed natural gas", "1"]])

_T_SORT = dict(
    headers=["Substance measured over a city",
             "Released directly from a tailpipe or smokestack",
             "Formed in the air out of substances already released"],
    rows=[["Sulfur dioxide", "yes", "no"],
          ["Nitrogen oxides", "yes", "no"],
          ["Carbon monoxide", "yes", "no"],
          ["Ozone", "no", "yes"],
          ["Nitric acid", "no", "yes"]])

_T_SWITCH = dict(
    headers=["Pollutant", "Released by the plant while burning coal (tons per year)",
             "Released by the plant after switching to natural gas (tons per year)"],
    rows=[["Sulfur dioxide", "4,000", "4"],
          ["Particulate matter", "600", "30"],
          ["Nitrogen oxides", "1,200", "500"],
          ["Carbon dioxide", "3,000,000", "1,700,000"]])

_T_SITES = dict(
    headers=["Sampling site", "Distance from the highway (meters)",
             "Carbon monoxide measured (parts per million)"],
    rows=[["Site 1", "10", "6.0"],
          ["Site 2", "100", "3.0"],
          ["Site 3", "500", "1.5"],
          ["Site 4", "2,000", "0.5"]])

QUESTIONS = [

 dict(q="A power station burns coal to raise steam. Which of the following best "
        "identifies air pollutants that the framework attributes to coal combustion?",
      choices=[
        "Carbon dioxide, sulfur dioxide, toxic metals, and particulates",
        "Helium, argon, and neon released from the mineral matter in the fuel",
        "Chlorofluorocarbons used as the working fluid inside the boiler",
        "Radon gas driven out of the bedrock beneath the station",
        "Pollen and fungal spores drawn in through the air intake"],
      ans=0,
      why="Coal combustion is the source the framework attaches to carbon dioxide, "
          "sulfur dioxide, toxic metals and particulates. The noble gases are "
          "unreactive and are not combustion products, radon comes out of rock rather "
          "than out of a fuel, and pollen and spores are biological material that "
          "burning does not create."),

 dict(q="An engineer measures what leaves the stack of a coal-fired boiler. The "
        "measurements are given below.",
      table=_T_COAL,
      choices=[
        "Carbon dioxide is released in by far the greatest mass, but the sulfur "
        "dioxide, particulates, and metals released with it are pollutants as well",
        "Only the substance released in the greatest mass counts as an air pollutant",
        "The metals are released in the greatest mass and therefore dominate the "
        "pollution problem at this plant",
        "Because particulates are measured in grams they cannot be harmful",
        "The table shows that burning coal releases a single pollutant"],
      ans=0,
      why="The measured masses fall from carbon dioxide down to the metals, so the "
          "largest release is the carbon dioxide, and the framework lists sulfur "
          "dioxide, toxic metals and particulates alongside it as pollutants that "
          "coal combustion also releases. Mass released is not the same as harm done."),

 dict(q="Nitrogen oxides enter the atmosphere when fossil fuels are burned. Which of "
        "the following lists consequences the framework attaches to those nitrogen "
        "oxides?",
      choices=[
        "The production of ozone, the formation of photochemical smog, and conversion "
        "to nitric acid that causes acid rain",
        "The destruction of soil bacteria and the loss of nitrogen from farmland",
        "A drop in atmospheric oxygen that makes breathing difficult at sea level",
        "The chilling of the lower atmosphere and the onset of an ice age",
        "The direct thinning of the ozone layer over the poles"],
      ans=0,
      why="Nitrogen oxides released by combustion lead to ozone production, to the "
          "formation of photochemical smog, and to nitric acid that falls as acid "
          "rain. Nothing in the framework has them consuming atmospheric oxygen, "
          "cooling the lower atmosphere, or thinning stratospheric ozone."),

 dict(q="Rainfall collected downwind of a highway corridor is measured and found to "
        "contain nitric acid. Which pathway does the framework give for the formation "
        "of that acid?",
      choices=[
        "Nitrogen oxides released by fuel combustion convert to nitric acid in the "
        "atmosphere",
        "Nitric acid is manufactured in vehicle engines and leaves the tailpipe as it is",
        "Carbon monoxide from vehicles reacts with rainwater to make nitric acid",
        "Nitrogen gas in the air dissolves in rain and becomes acidic without any "
        "combustion",
        "Particulate matter dissolves in cloud droplets and releases nitrogen"],
      ans=0,
      why="The framework has combustion release nitrogen oxides, which then convert "
          "to nitric acid in the atmosphere and cause acid rain. The acid is therefore "
          "formed after release rather than emitted ready-made, and carbon monoxide "
          "and nitrogen gas are not its source."),

 dict(q="Besides nitrogen oxides, which group of pollutants does the framework "
        "identify as produced by fossil fuel combustion?",
      choices=[
        "Carbon monoxide, hydrocarbons, and particulate matter",
        "Chlorofluorocarbons, hydrofluorocarbons, and halons",
        "Radon, mold spores, and dust mites",
        "Asbestos fibers and formaldehyde released from insulation",
        "Nitrogen gas, argon, and water vapor in their ordinary proportions"],
      ans=0,
      why="Carbon monoxide, hydrocarbons and particulate matter are the three the "
          "framework names as other products of fossil fuel combustion. Halogenated "
          "refrigerants are manufactured chemicals rather than combustion products, "
          "and the remaining options list indoor or naturally occurring materials."),

 dict(q="A city compares the sulfur dioxide released by three fuels used in its "
        "delivery fleets.",
      table=_T_FUELS,
      choices=[
        "Diesel releases far more sulfur dioxide per hundred liters than the other two "
        "fuels, which matches the framework's statement about sulfur dioxide and diesel",
        "The three fuels release sulfur dioxide in nearly equal amounts",
        "Compressed natural gas is the largest single source of sulfur dioxide here",
        "Gasoline releases more sulfur dioxide per hundred liters than diesel does",
        "Sulfur dioxide is a secondary pollutant, so no fuel can release it directly"],
      ans=0,
      why="The measured releases place diesel far above gasoline and compressed "
          "natural gas, and the framework states that sulfur dioxide affecting air "
          "quality comes from burning fossil fuels, mainly diesel fuels. Sulfur "
          "dioxide leaves the exhaust already formed, so it is released directly."),

 dict(q="A national record of lead in fuel and lead in air is shown.",
      table=_T_LEAD,
      choices=[
        "Lead in the air fell as lead in gasoline fell, which is what regulating lead "
        "in fuels would be expected to produce",
        "Lead in the air rose while lead in gasoline fell",
        "Lead in gasoline fell but lead in the air stayed at the same level throughout",
        "The two columns move in opposite directions in every interval",
        "Lead in the air fell to zero within the period shown"],
      ans=0,
      why="Both columns fall in every interval of the record, and the framework "
          "credits the regulation of lead under the Clean Air Act, particularly in "
          "fuels, with dramatically decreasing atmospheric lead. The final air "
          "measurement is small but is not zero."),

 dict(q="Which agency and which law does the framework credit with the regulation of "
        "lead that reduced the amount of lead in the atmosphere?",
      choices=[
        "The Environmental Protection Agency acting through the Clean Air Act",
        "The Environmental Protection Agency acting through a ban on coal mining",
        "A voluntary agreement among refiners with no legislation behind it",
        "An international treaty on stratospheric ozone",
        "State highway departments setting speed limits"],
      ans=0,
      why="The framework attributes the regulation of lead, particularly in fuels, to "
          "the Environmental Protection Agency acting through the Clean Air Act, and "
          "attributes the dramatic decline in atmospheric lead to that regulation. No "
          "voluntary scheme, ozone treaty or speed limit is given that role."),

 dict(q="Air pollutants are sorted into two categories. Measurements over one city "
        "are shown.",
      table=_T_SORT,
      choices=[
        "Ozone, because the table shows it forming in the air rather than leaving a "
        "tailpipe or smokestack",
        "Sulfur dioxide, because it is measured at high concentrations",
        "Carbon monoxide, because it is a gas rather than a particle",
        "Nitrogen oxides, because they are released by combustion",
        "Every substance in the table, because all of them are measured over the city"],
      ans=0,
      why="A secondary pollutant is one formed in the atmosphere out of material "
          "already released, and the table marks ozone and nitric acid that way while "
          "marking the other three as released directly. Being a gas, being abundant, "
          "or simply being present over the city does not sort a pollutant into "
          "either category."),

 dict(q="Which statement best captures the difference the framework draws between "
        "primary and secondary air pollutants?",
      choices=[
        "A primary pollutant is released into the air by its source, while a secondary "
        "pollutant forms in the atmosphere out of substances already released",
        "A primary pollutant is always more harmful than a secondary pollutant",
        "A primary pollutant is a gas and a secondary pollutant is a particle",
        "A primary pollutant comes from nature and a secondary pollutant comes from "
        "human activity",
        "A primary pollutant is regulated by law and a secondary pollutant is not"],
      ans=0,
      why="The framework's own example is nitrogen oxides, which are released by "
          "combustion and then lead to ozone and convert to nitric acid in the "
          "atmosphere, so the categories turn on where the substance is formed. "
          "Harm, physical state, origin and legal status vary independently of that."),

 dict(q="A student claims that every pollutant in urban air must have come straight "
        "out of an exhaust pipe or a chimney. Which observation most directly "
        "challenges the claim?",
      choices=[
        "Some pollutants are formed in the atmosphere from substances that were "
        "released earlier",
        "Some exhaust pipes release more pollution than others",
        "Air pollution is worse in some seasons than in others",
        "Air pollution can travel a long way from where it was released",
        "Some pollutants are gases and others are particles"],
      ans=0,
      why="The claim allows only direct release, so the observation that refutes it is "
          "the existence of pollutants formed after release, which is what the "
          "framework's secondary category holds. Differences in amount, season, "
          "distance travelled and physical state are all consistent with the claim."),

 dict(q="A team plans to test whether traffic on a nearby highway raises carbon "
        "monoxide in the air. They intend to sample at one site beside the highway. "
        "Which modification to the procedure would most improve the conclusion they "
        "can draw?",
      choices=[
        "Sample at several distances from the highway during the same hours",
        "Sample at the same single site but use a more expensive instrument",
        "Sample only on days when traffic is heaviest",
        "Report the highest single reading rather than the average of the readings",
        "Move the single site closer to the highway edge"],
      ans=0,
      why="A claim that the highway is the source needs a comparison across distance "
          "from it, with the time of day held constant. A better instrument, a "
          "restricted set of days, a maximum in place of an average, or a site moved "
          "nearer all leave the study with nothing to compare against."),

 dict(q="Results from a redesigned carbon monoxide study are shown.",
      table=_T_SITES,
      choices=[
        "Carbon monoxide falls steadily with distance from the highway, which is "
        "consistent with the traffic being its source",
        "Carbon monoxide rises with distance from the highway",
        "Carbon monoxide is the same at every distance measured",
        "The site farthest from the highway recorded the highest concentration",
        "The measurements show that carbon monoxide is formed in the air rather than "
        "released"],
      ans=0,
      why="The concentrations fall at every step away from the road, which is the "
          "pattern expected if the road is the source, and the framework lists carbon "
          "monoxide among the pollutants produced by fossil fuel combustion. The "
          "table cannot show where a substance was formed, only where it was measured."),

 dict(q="A plant switches from coal to natural gas and keeps its output of "
        "electricity the same. Emissions before and after are shown.",
      table=_T_SWITCH,
      choices=[
        "Sulfur dioxide falls by the largest fraction of its original amount",
        "Carbon dioxide falls by the largest fraction of its original amount",
        "Nitrogen oxides fall by the largest fraction of their original amount",
        "Particulate matter falls by the largest fraction of its original amount",
        "All four pollutants fall by the same fraction of their original amounts"],
      ans=0,
      why="Sulfur dioxide falls from four thousand tons to four, a thousandfold "
          "reduction, while particulates fall to a twentieth, nitrogen oxides to less "
          "than half, and carbon dioxide by little more than a third. The fractions "
          "are therefore plainly unequal, and the largest belongs to sulfur dioxide."),

 dict(q="Which of the following is the best reason that burning coal is treated as a "
        "source of several different air pollutants rather than only one?",
      choices=[
        "The fuel contains carbon, sulfur, and metallic impurities, and combustion "
        "releases products of all of them along with unburned solid particles",
        "Coal is burned in larger quantities than any other substance on Earth",
        "Coal is always burned outdoors, so its products spread widely",
        "Every fuel releases exactly the same mixture of pollutants when burned",
        "Coal releases pollutants only after it has been buried in a landfill"],
      ans=0,
      why="The framework's list for coal combustion covers carbon dioxide, sulfur "
          "dioxide, toxic metals and particulates, which are products of different "
          "constituents of the same fuel. Quantity burned, where it is burned, and "
          "disposal after use do not explain a mixture of products."),

 dict(q="A monitoring station records elevated sulfur dioxide on days when a nearby "
        "coal-fired plant is running at full load and low sulfur dioxide when the "
        "plant is shut for maintenance. Which conclusion does this pattern best "
        "support?",
      choices=[
        "The plant is a source of the sulfur dioxide measured at the station",
        "Sulfur dioxide is formed in the atmosphere rather than released",
        "The station is measuring particulate matter instead of a gas",
        "Sulfur dioxide has no effect on air quality",
        "The plant is the only possible source of sulfur dioxide anywhere in the region"],
      ans=0,
      why="The pollutant rises and falls with the operation of one identified source, "
          "which supports that source contributing to the measured concentration. It "
          "does not show that no other source exists, does not change what is being "
          "measured, and does not bear on whether air quality is affected."),

 dict(q="Which of the following best describes why regulating lead in fuels was an "
        "effective way to reduce lead in the air?",
      choices=[
        "Fuel was burned in enormous quantities in ordinary vehicles, so the lead it "
        "carried was released into the air wherever those vehicles went",
        "Lead is a gas at ordinary temperatures and so escapes from any container",
        "Lead in fuel is the only form of lead that exists",
        "Lead becomes harmless once it has left an engine",
        "Regulating fuel removed lead from paints and pipes as well"],
      ans=0,
      why="The framework singles out fuels as the use of lead that the Environmental "
          "Protection Agency regulated and credits that regulation with a dramatic "
          "decrease in atmospheric lead, which follows from the very large number of "
          "engines burning that fuel. Lead is a metal, exists in many other uses, and "
          "does not become harmless on release."),

 dict(q="An investigator wants to know whether the particulate matter over a "
        "neighborhood comes mainly from a highway or from a nearby industrial plant. "
        "Which modification to a single-site sampling plan would best allow the two "
        "sources to be separated?",
      choices=[
        "Add sampling sites on the far side of each source and record the wind "
        "direction with every sample",
        "Sample for a longer time at the original site",
        "Sample at the original site only when the wind is calm",
        "Replace the particulate sampler with a carbon monoxide sampler",
        "Report the results as a single yearly average"],
      ans=0,
      why="Separating two sources requires measurements positioned around both and a "
          "record of which way the air was moving when each sample was taken. Longer "
          "sampling, calm days only, a different pollutant, or a single average all "
          "discard the information that distinguishes the sources."),

 dict(q="Ozone measured in the air over a city is described as a secondary pollutant. "
        "Which statement follows from that classification?",
      choices=[
        "The ozone was produced in the atmosphere from pollutants that had been "
        "released there",
        "The ozone was released from vehicle tailpipes in the form measured",
        "The ozone drifted down from the stratosphere without any human involvement",
        "The ozone must be harmless because it was not released directly",
        "The ozone must have come from a single identifiable smokestack"],
      ans=0,
      why="A secondary pollutant is one formed in the atmosphere out of material "
          "already released, and the framework has nitrogen oxides from combustion "
          "leading to the production of ozone. The classification says nothing about "
          "how harmful the ozone is or where any single stack stands."),

 dict(q="Two claims are made about fossil fuel combustion. The first is that it "
        "releases nitrogen oxides. The second is that it contributes to acid rain. "
        "Which statement best explains how both can be true at once?",
      choices=[
        "The nitrogen oxides released convert to nitric acid in the atmosphere, so one "
        "release leads to the other effect",
        "The two claims describe unrelated processes that happen to occur together",
        "Acid rain is released directly from the exhaust of vehicles as an acid",
        "Nitrogen oxides neutralize acids, so the second claim must be mistaken",
        "Acid rain forms only from natural sources, so combustion is irrelevant"],
      ans=0,
      why="The framework links them explicitly: combustion releases nitrogen oxides, "
          "and those oxides convert to nitric acid in the atmosphere, causing acid "
          "rain. The link is a chemical conversion after release rather than a "
          "coincidence, a direct emission of acid, or a neutralization."),

 dict(q="A student says that any substance found in the air counts as an air "
        "pollutant. Which of the following is the strongest objection?",
      choices=[
        "The ordinary components of clean air are present everywhere and are not "
        "released by human activity in a way that damages air quality",
        "Air pollutants are always invisible, and many substances in the air can be seen",
        "Only substances regulated by name in a statute are pollutants",
        "Only substances released indoors can be pollutants",
        "Substances present in small amounts cannot be pollutants"],
      ans=0,
      why="The framework treats air pollution as the consequence of human activities "
          "for the atmosphere and identifies pollutants by their sources and effects, "
          "which excludes the ordinary constituents of clean air. Visibility, listing "
          "in a statute, indoor origin and small concentration are not the test."),

 dict(q="Which single change to a fleet would be expected to produce the largest "
        "reduction in the sulfur dioxide it releases, according to the sources the "
        "framework names?",
      choices=[
        "Replacing diesel vehicles with vehicles that do not burn diesel fuel",
        "Repainting the vehicles a lighter color to reduce heat absorption",
        "Reducing the weight carried by each vehicle by a small amount",
        "Fitting quieter exhaust systems to the existing diesel vehicles",
        "Washing the vehicles more often to remove accumulated soot"],
      ans=0,
      why="The framework attributes the sulfur dioxide that affects air quality to the "
          "burning of fossil fuels, mainly diesel fuels, so removing diesel combustion "
          "removes that source. Paint, small load reductions, exhaust noise and "
          "washing do not change the sulfur burned."),

 dict(q="Carbon monoxide is measured at a busy intersection. Which of the following "
        "best identifies its source there, according to the framework?",
      choices=[
        "It is one of the pollutants produced by the combustion of fossil fuels",
        "It is formed in the atmosphere from ozone and sunlight",
        "It is released by the decay of asphalt in the roadway",
        "It is a naturally occurring component of clean air at that concentration",
        "It is produced by the corrosion of metal in vehicle bodies"],
      ans=0,
      why="The framework lists carbon monoxide, hydrocarbons and particulate matter "
          "among the pollutants produced by fossil fuel combustion, which is what "
          "vehicles at an intersection are doing. It gives no atmospheric formation "
          "route, no pavement source and no corrosion source for carbon monoxide."),

 dict(q="A researcher measuring particulates beside a road places the sampler at "
        "ground level in a sheltered alcove out of the wind. A colleague argues the "
        "results will misrepresent the air over the road. Which modification best "
        "addresses that objection?",
      choices=[
        "Move the sampler into the open air at a standard height away from the shelter",
        "Leave the sampler where it is but run it for twice as long",
        "Leave the sampler where it is and multiply every reading by two",
        "Move the sampler indoors so that conditions are constant",
        "Take readings only on days with no traffic"],
      ans=0,
      why="A sheltered alcove is not exposed to the air being described, so the fix is "
          "to sample the air in question under standard conditions. Longer runs and "
          "scaled readings preserve the same bias, an indoor site measures different "
          "air, and no-traffic days remove the source under study."),

 dict(q="Which of the following best explains why sulfur dioxide and particulate "
        "matter are both attributed to coal combustion even though one is a gas and "
        "one is solid material?",
      choices=[
        "Both leave the furnace with the exhaust stream, one as a gaseous product of "
        "the sulfur in the fuel and one as solid material carried up by the hot gases",
        "Solid particles are simply sulfur dioxide that has cooled and frozen",
        "Both are formed in the atmosphere long after the exhaust has dispersed",
        "The two are the same substance measured by two different instruments",
        "Only the gas is a pollutant, and the particles are counted for convenience"],
      ans=0,
      why="The framework lists both among the releases of coal combustion, and the "
          "difference in physical state reflects different constituents of the same "
          "fuel and the same exhaust stream. Neither is a frozen form of the other, "
          "neither is formed only after dispersal, and both are named as pollutants."),

 dict(q="A city council is told that reducing nitrogen oxide emissions would address "
        "more than one air quality problem at once. Which of the following best "
        "supports that statement?",
      choices=[
        "Nitrogen oxides lead to ozone production and to photochemical smog, and they "
        "convert to the nitric acid that falls as acid rain",
        "Nitrogen oxides are the only pollutant released by vehicles",
        "Nitrogen oxides remove particulate matter from the air as they disperse",
        "Nitrogen oxides are heavier than air and settle out near their source",
        "Nitrogen oxides are secondary pollutants and so are easy to control"],
      ans=0,
      why="The framework attaches three separate consequences to the nitrogen oxides "
          "released by combustion, so one reduction reaches all three. Vehicles "
          "release other pollutants as well, and the framework gives nitrogen oxides "
          "no scrubbing effect, no settling behavior, and no secondary status."),

 dict(q="Two neighborhoods report different air quality. One sits beside a rail yard "
        "where diesel locomotives idle; the other sits beside a park. Which "
        "measurement would best test the claim that the rail yard is affecting local "
        "air quality?",
      choices=[
        "Sulfur dioxide measured in both neighborhoods over the same period",
        "The number of trees counted in each neighborhood",
        "The population of each neighborhood",
        "The age of the houses in each neighborhood",
        "The number of complaints filed by residents of each neighborhood"],
      ans=0,
      why="The framework attributes the sulfur dioxide that affects air quality to "
          "burning fossil fuels, mainly diesel fuels, so a paired measurement of that "
          "pollutant tests the claim directly. Trees, population, housing age and "
          "complaints measure something other than the air."),

 dict(q="Which of the following would be classified as a primary pollutant on the "
        "framework's distinction?",
      choices=[
        "Sulfur dioxide leaving a smokestack in the form in which it is measured",
        "Ozone produced over a city during the day",
        "Nitric acid falling in rain downwind of a highway",
        "A haze that appears only after several hours of sunlight",
        "An acid formed in cloud droplets from a released gas"],
      ans=0,
      why="A primary pollutant is released by its source in the form in which it is "
          "found, which describes sulfur dioxide leaving a stack. Ozone, nitric acid, "
          "a haze that develops over hours and an acid formed in cloud droplets are "
          "all produced in the atmosphere after release."),

 dict(q="An air quality report notes that a region's problems come from many sources "
        "rather than one. Which pair of statements from the framework best supports "
        "that description?",
      choices=[
        "Coal combustion releases carbon dioxide, sulfur dioxide, toxic metals, and "
        "particulates, and fossil fuel combustion also releases nitrogen oxides, "
        "carbon monoxide, and hydrocarbons",
        "Air pollutants can be primary or secondary, and secondary pollutants are "
        "always more abundant",
        "Lead was regulated in fuels, and lead is the only regulated pollutant",
        "Sulfur dioxide comes mainly from diesel fuels, and diesel is the only fossil "
        "fuel burned",
        "Nitrogen oxides convert to nitric acid, and nitric acid converts back to "
        "nitrogen oxides"],
      ans=0,
      why="The two source statements together cover several fuels and several "
          "pollutants, which is what a many-source description needs. Each other "
          "option pairs a framework statement with an assertion the framework does not "
          "make, about abundance, exclusivity of regulation, a single fuel, or a "
          "reverse conversion."),

 dict(q="A student is asked to explain what it means to identify the source and the "
        "effect of an air pollutant. Which response is best?",
      choices=[
        "Naming the activity that puts the substance into the air and naming the harm "
        "it does once it is there",
        "Naming the instrument used to measure it and the units of that measurement",
        "Naming the country in which it was first detected and the year",
        "Naming the season in which it is most abundant and the temperature that day",
        "Naming its chemical formula and its molecular mass"],
      ans=0,
      why="The learning objective asks for sources and effects, so the source is the "
          "activity releasing the pollutant and the effect is what it does after "
          "release. Instruments, dates, seasons and formulas describe the substance or "
          "the measurement rather than the source or the effect."),
]
