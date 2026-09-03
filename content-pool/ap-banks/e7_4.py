# AP ENVIRONMENTAL SCIENCE 7.4 Atmospheric Particulates
# CED effective Fall 2026, Unit 7 Atmospheric Pollution. Enduring understanding STB-2.
# Learning objective STB-2.D: describe natural sources of CO2 and particulates.
# Suggested skill 4.C, describe an aspect of a research method, design, and/or measure
# used.
#
# ON THE TITLE. ENV_SCI_topics.json carries this topic as "Atmospheric Particulates"
# and TOPIC below uses that string verbatim, as the run brief requires. The CED's own
# heading is "Atmospheric CO2 and Particulates" -- the extractor lost the middle of
# the heading where the two-column layout split it -- and the topic's learning
# objective covers both, so this module does too. Flagged for the coordinator.
#
# Essential knowledge relied on, in the framework's own words:
#   STB-2.D.1  CO2 appears naturally in the atmosphere from sources such as
#              respiration, decomposition, and volcanic eruptions.
#   STB-2.D.2  There are a variety of natural sources of particulate matter.
#
# WHAT IS AND IS NOT KEYED. STB-2.D.1 names three natural sources of carbon dioxide
# and STB-2.D.2 asserts only that natural sources of particulate matter are various --
# it names none. So no key in this module asks a student to recognise an unlisted
# natural particulate source from memory. Where an item sorts a source, the stem or
# the table states whether human activity is involved, and the rejected options are
# sources the framework has already named as human: coal combustion and fossil fuel
# combustion under STB-2.A.1 and STB-2.A.2, and the human-made indoor pollutants of
# STB-2.E.5. The one general claim used is STB-2.D.2 itself: particulate matter
# measured where no human activity occurs still has somewhere to have come from.
#
# ON SCOPE. The pollutant effects belong to 7.1, indoor sources to 7.5, and the
# greenhouse behaviour of carbon dioxide to unit 9. This topic keys the NATURAL
# origins and, under skill 4.C, the design and measures of the studies that establish
# them.
#
# FIVE choices (A-E). No LaTeX and no non-ASCII: export_units.py does not typeset
# ENV_SCI.
TOPIC = ("7.4", "Atmospheric Particulates", 7)

_T_REMOTE = dict(
    headers=["Sampling site",
             "Distance to the nearest road or building (kilometers)",
             "Particulate matter measured (micrograms per cubic meter)"],
    rows=[["City center", "0", "42"],
          ["Farm village", "3", "24"],
          ["Remote island station", "300", "9"]])

_T_LITTER = dict(
    headers=["Sealed chamber", "Contents",
             "Carbon dioxide added to the chamber air in 24 hours (parts per million)"],
    rows=[["Chamber 1", "Moist leaf litter with soil organisms", "310"],
          ["Chamber 2", "Leaf litter sterilized before sealing", "15"],
          ["Chamber 3", "Empty, sealed at the same time", "2"]])

_T_ERUPTION = dict(
    headers=["Week of sampling",
             "Carbon dioxide at a downwind station (parts per million above background)",
             "Volcanic eruption reported that week"],
    rows=[["Week 1", "1", "no"],
          ["Week 2", "2", "no"],
          ["Week 3", "46", "yes"],
          ["Week 4", "38", "yes"],
          ["Week 5", "5", "no"]])

_T_RESP = dict(
    headers=["Sealed jar", "Contents",
             "Carbon dioxide in the jar after six hours (parts per million)"],
    rows=[["Jar 1", "Ten crickets in air", "1,900"],
          ["Jar 2", "Ten small stones in air", "420"],
          ["Jar 3", "Air alone", "415"]])

_T_SEASON = dict(
    headers=["Month at a forested monitoring station",
             "Average carbon dioxide (parts per million)",
             "Average soil temperature (degrees Celsius)"],
    rows=[["February", "418", "2"],
          ["May", "424", "11"],
          ["August", "436", "19"],
          ["November", "422", "8"]])

_T_FILTERS = dict(
    headers=["Filter", "Hours the pump ran", "Mass of particles collected (milligrams)"],
    rows=[["Filter 1", "6", "1.8"],
          ["Filter 2", "12", "3.6"],
          ["Filter 3", "24", "7.2"]])

QUESTIONS = [

 dict(q="Which of the following does the framework name as natural sources of carbon "
        "dioxide in the atmosphere?",
      choices=[
        "Respiration, decomposition, and volcanic eruptions",
        "Coal combustion, diesel engines, and industrial furnaces",
        "Refrigeration equipment, aerosol propellants, and foam blowing",
        "Radon decay, asbestos wear, and mold growth indoors",
        "Photochemical reactions between nitrogen oxides and sunlight"],
      ans=0,
      why="The framework states that carbon dioxide appears naturally in the atmosphere "
          "from sources such as respiration, decomposition, and volcanic eruptions. The "
          "rejected lists are human combustion sources, manufactured chemicals, indoor "
          "pollutants, and the reaction that forms photochemical smog."),

 dict(q="A class seals three jars for six hours and measures the carbon dioxide in each.",
      table=_T_RESP,
      choices=[
        "The jar holding living animals gained far more carbon dioxide than either jar "
        "without them, which is what respiration would produce",
        "All three jars gained the same amount of carbon dioxide",
        "The jar of stones gained the most carbon dioxide of the three",
        "The jar of air alone gained more carbon dioxide than the jar of animals",
        "The results show that carbon dioxide can only come from burning fuel"],
      ans=0,
      why="Only the jar with living animals rises far above the starting concentration, "
          "while the jar of stones and the jar of air alone stay near it. Respiration is "
          "one of the natural sources of carbon dioxide the framework names."),

 dict(q="A class investigating respiration seals one jar containing live crickets, one "
        "containing stones, and one containing air alone, and measures the carbon "
        "dioxide in each after six hours. What is the purpose of the jar holding air "
        "alone?",
      choices=[
        "It provides a comparison showing what the measurement gives when the proposed "
        "source is absent",
        "It doubles the amount of carbon dioxide available to the animals",
        "It removes the need to measure the other jars",
        "It measures the temperature rather than the carbon dioxide",
        "It shows that the jars leak at a constant rate"],
      ans=0,
      why="A comparison with the proposed source removed is what allows a rise in the "
          "other jars to be attributed to that source. It does not supply carbon "
          "dioxide, replace the other measurements, change the quantity measured, or "
          "establish a leak rate."),

 dict(q="Three sealed chambers are compared over 24 hours.",
      table=_T_LITTER,
      choices=[
        "Carbon dioxide accumulated where decomposers were present and barely "
        "accumulated where they had been killed, which supports decomposition as the "
        "source",
        "Carbon dioxide accumulated equally in all three chambers",
        "The empty chamber accumulated the most carbon dioxide",
        "The sterilized litter accumulated more carbon dioxide than the untreated litter",
        "The results show that leaf litter cannot release carbon dioxide under any "
        "conditions"],
      ans=0,
      why="The chamber with living soil organisms gained about twenty times as much "
          "carbon dioxide as the sterilized litter and far more than the empty chamber, "
          "so the gain tracks the presence of decomposers. Decomposition is one of the "
          "natural sources of carbon dioxide the framework names."),

 dict(q="Which measurement from a monitoring station would give the strongest evidence "
        "that a particular volcanic eruption raised carbon dioxide at that station?",
      choices=[
        "Carbon dioxide measured at the station before, during, and after the eruption",
        "Carbon dioxide measured at the station only during the eruption",
        "The height of the volcano and the age of its last eruption",
        "The number of people living near the volcano",
        "The average carbon dioxide of the whole atmosphere for that decade"],
      ans=0,
      why="Attributing a rise to an event requires readings from before and after it as "
          "well as during, so that the change can be seen. A single reading during the "
          "eruption has nothing to be compared with, and the other options measure "
          "something other than the station's air."),

 dict(q="Weekly measurements at a station downwind of a volcano are shown.",
      table=_T_ERUPTION,
      choices=[
        "Carbon dioxide above background was far higher in the weeks with a reported "
        "eruption than in the weeks without one",
        "Carbon dioxide above background was higher in the weeks without an eruption",
        "Carbon dioxide above background was the same in every week",
        "Carbon dioxide above background rose steadily from the first week to the last",
        "The eruption weeks cannot be compared with the other weeks in these data"],
      ans=0,
      why="The two weeks marked as eruption weeks carry the two largest values and the "
          "three other weeks are all small, so the rise coincides with the eruptions. "
          "Volcanic eruptions are among the natural sources of carbon dioxide the "
          "framework names."),

 dict(q="Which statement does the framework make about natural sources of particulate "
        "matter?",
      choices=[
        "There are a variety of natural sources of particulate matter",
        "All particulate matter in the atmosphere comes from human activity",
        "Particulate matter has exactly one natural source",
        "Particulate matter is produced only by combustion",
        "Particulate matter exists only indoors"],
      ans=0,
      why="The framework states that there are a variety of natural sources of "
          "particulate matter, which is a claim about their number and diversity. The "
          "rejected options each deny that variety or deny natural origin altogether."),

 dict(q="Particulate measurements from three sites on the same day are shown.",
      table=_T_REMOTE,
      choices=[
        "Particulates are lowest at the most remote site but are still measurable there, "
        "which is consistent with natural sources existing alongside human ones",
        "Particulates are absent from the most remote site",
        "Particulates are highest at the most remote site",
        "Particulates are identical at all three sites",
        "The results show that particulates have no human sources"],
      ans=0,
      why="The remote station records the smallest of the three values, but the value is "
          "not zero, so some particulate matter is present far from roads and buildings. "
          "The framework states that particulate matter has a variety of natural "
          "sources, which is what a nonzero remote reading is consistent with."),

 dict(q="A student claims that any particulate matter in the air must have been released "
        "by people. Which observation most directly challenges the claim?",
      choices=[
        "Particulate matter is measured in places where no human activity occurs",
        "Particulate matter is measured in cities at higher concentrations than in the "
        "countryside",
        "Particulate matter can be collected on a filter",
        "Particulate matter varies from hour to hour at a single site",
        "Particulate matter is smaller than the particles in ordinary sand"],
      ans=0,
      why="The claim allows only human release, so what refutes it is particulate matter "
          "present where people are not, which the framework accounts for by stating "
          "that natural sources of particulate matter are various. Urban excess, "
          "collectability, hourly variation and particle size are all compatible with "
          "the claim."),

 dict(q="Which of the following would be counted as a natural source of particulate "
        "matter?",
      choices=[
        "Soil lifted into the air by strong wind across bare ground where no people are "
        "present",
        "Fly ash carried up the stack of a coal-fired power station",
        "Soot released from the exhaust of a diesel engine",
        "Fibers shed by asbestos insulation inside a building",
        "Smoke drawn into a room from burning tobacco"],
      ans=0,
      why="The described process involves no human activity, and the framework states "
          "that natural sources of particulate matter are various. Each rejected option "
          "is a source the framework itself attributes to human activity, either to fuel "
          "combustion or to human-made indoor materials."),

 dict(q="Monthly measurements at a forested station are shown.",
      table=_T_SEASON,
      choices=[
        "Carbon dioxide is highest in the month with the warmest soil and lowest in the "
        "month with the coldest soil",
        "Carbon dioxide is highest in the month with the coldest soil",
        "Carbon dioxide is the same in every month",
        "Carbon dioxide falls as the soil warms",
        "Soil temperature and carbon dioxide have no relationship in these data"],
      ans=0,
      why="Ranking the four months by soil temperature gives the same order as ranking "
          "them by carbon dioxide, so the highest reading belongs to the warmest month "
          "and the lowest to the coldest. Decomposition in soil is one of the natural "
          "sources of carbon dioxide the framework names."),

 dict(q="A researcher wants to describe how much particulate matter is in the air at a "
        "site. Which measure is appropriate?",
      choices=[
        "The mass of particles collected from a known volume of air",
        "The number of days on which haze was visible from the site",
        "The mass of the filter before any air has passed through it",
        "The number of vehicles that passed the site during the sampling period",
        "The temperature of the air at the time of sampling"],
      ans=0,
      why="A concentration is an amount in a given volume, so the measure is the mass of "
          "particles collected per volume of air drawn through the sampler. Visible haze "
          "days, an unused filter mass, a vehicle count and an air temperature each "
          "measure something else."),

 dict(q="Three filters are run for different lengths of time at the same site with the "
        "same pump.",
      table=_T_FILTERS,
      choices=[
        "The mass collected is proportional to the time the pump ran, so the mass alone "
        "cannot be compared between filters unless the running time is taken into account",
        "The mass collected is the same on every filter regardless of running time",
        "The filter run for the shortest time collected the most mass",
        "The mass collected falls as the running time rises",
        "The results show that the pump collected nothing at all"],
      ans=0,
      why="Doubling the running time doubles the mass collected in each step of the "
          "table, so mass by itself reflects how long the pump ran as much as how dirty "
          "the air was. A comparison between filters therefore has to be made per unit "
          "of time or per volume of air."),

 dict(q="Why does the framework describe carbon dioxide as appearing naturally in the "
        "atmosphere even though burning fossil fuels also releases it?",
      choices=[
        "Processes such as respiration, decomposition, and volcanic eruptions release "
        "carbon dioxide whether or not people are present",
        "Carbon dioxide released by fuel combustion is a different substance from the "
        "carbon dioxide released by living things",
        "Carbon dioxide is only natural when its concentration is low",
        "Carbon dioxide appears naturally only in the stratosphere",
        "Carbon dioxide from natural sources cannot be measured"],
      ans=0,
      why="The framework lists respiration, decomposition and volcanic eruptions as "
          "natural sources, and those processes occur independently of human activity. "
          "The same substance is released by combustion as well, which is why sorting "
          "the SOURCE rather than the substance is the point."),

 dict(q="An investigator plans to compare particulate concentrations at a roadside site "
        "and a remote site. Which aspect of the design most needs to be held constant "
        "for the comparison to be fair?",
      choices=[
        "The sampling equipment and the length of the sampling period at both sites",
        "The number of researchers present at each site",
        "The color of the filter holders used at each site",
        "The day of the week on which the results are written up",
        "The order in which the two sets of results are reported"],
      ans=0,
      why="A difference between sites can only be attributed to the air if the way the "
          "air is sampled is the same at both, which means the same equipment run for "
          "the same period. Staffing, equipment color, and how or when results are "
          "written up do not affect what the samplers collect."),

 dict(q="Which of the following best describes what a control chamber contributes to a "
        "decomposition experiment?",
      choices=[
        "It shows how much carbon dioxide accumulates when the decomposers are absent, "
        "so the rest can be attributed to them",
        "It increases the rate at which the litter decomposes",
        "It measures the mass of the litter rather than the gas",
        "It guarantees that the experiment will produce a large result",
        "It replaces the need to repeat the experiment"],
      ans=0,
      why="The control establishes the value the measurement takes with the proposed "
          "cause removed, which is what makes the difference attributable to that cause. "
          "It does not speed up the process, change what is measured, or remove the need "
          "for replication."),

 dict(q="A monitoring station far from any city records a small but steady concentration "
        "of particulate matter throughout the year. Which conclusion is best supported?",
      choices=[
        "Particulate matter reaching that station has natural sources as well as any "
        "distant human ones",
        "The station's instruments must be faulty, since no people are nearby",
        "All the particulate matter at the station was released by the station itself",
        "Particulate matter cannot travel away from where it is released",
        "The station is measuring carbon dioxide rather than particles"],
      ans=0,
      why="The framework states that there are a variety of natural sources of "
          "particulate matter, which accounts for a persistent reading where human "
          "activity is absent. Nothing in the observation suggests instrument failure, "
          "and pollution is not confined to its point of release."),

 dict(q="Which pairing of a source with its classification is consistent with the "
        "framework?",
      choices=[
        "Decomposition of dead plant material, a natural source of carbon dioxide",
        "Combustion of coal in a power station, a natural source of carbon dioxide",
        "Respiration by animals, a human-made source of carbon dioxide",
        "Volcanic eruption, a human-made source of carbon dioxide",
        "Diesel exhaust, a natural source of particulate matter"],
      ans=0,
      why="The framework names respiration, decomposition and volcanic eruptions as "
          "natural sources of carbon dioxide, and it attributes coal combustion and "
          "diesel exhaust to human activity in the earlier air pollution statements. "
          "Each rejected pairing swaps one of those classifications."),

 dict(q="A study measures carbon dioxide inside a greenhouse full of plants and animals "
        "at night and finds that it rises. Which natural source best accounts for the "
        "rise?",
      choices=[
        "Respiration by the organisms in the greenhouse",
        "A volcanic eruption inside the greenhouse",
        "Combustion of fossil fuel by the plants",
        "Photochemical smog forming in the dark",
        "Thermal inversion trapping carbon dioxide inside the glass"],
      ans=0,
      why="Respiration is one of the natural sources of carbon dioxide the framework "
          "names, and it is the process the organisms present are carrying out. Plants "
          "do not burn fuel, smog requires sunlight, and an inversion is an arrangement "
          "of outdoor air rather than a source."),

 dict(q="What is the clearest reason to report particulate results as a concentration "
        "rather than as a total mass collected?",
      choices=[
        "A concentration accounts for the volume of air sampled, so results from "
        "different sampling runs can be compared",
        "A concentration is always a larger number than a total mass",
        "A total mass cannot be measured with a balance",
        "A concentration removes the need for a control site",
        "A total mass is only meaningful for gases, not for particles"],
      ans=0,
      why="Dividing by the volume of air drawn through the sampler removes the influence "
          "of how long the pump ran, which is what makes two runs comparable. The size "
          "of the number, the ability to weigh a filter, and the need for a comparison "
          "site are separate matters."),

 dict(q="A team reports that carbon dioxide at a rural station rises every night and "
        "falls every day. Which natural process named by the framework is most "
        "consistent with a nightly rise?",
      choices=[
        "Respiration, which continues at night in the organisms present",
        "Volcanic eruption, which occurs only after dark",
        "Decomposition, which stops entirely during daylight",
        "Photochemical reactions, which require sunlight",
        "Fossil fuel combustion by the vegetation around the station"],
      ans=0,
      why="Respiration is a natural source of carbon dioxide the framework names, and it "
          "does not stop at night. Eruptions are not tied to the hour, the framework does "
          "not make decomposition daylight-dependent, sunlight-driven chemistry cannot "
          "run in the dark, and vegetation does not burn fuel."),

 dict(q="Which question could a study of natural particulate sources actually answer "
        "with the measurements described in this topic?",
      choices=[
        "How much particulate matter is present in the air at a site where no human "
        "activity occurs",
        "Which single natural source produces the majority of the world's particulate "
        "matter",
        "How many people will become ill from particulates in the next decade",
        "Whether particulate matter existed before there were instruments to measure it",
        "Which government policy would remove all particulate matter from the air"],
      ans=0,
      why="A sampler measures how much particulate matter is present in the air it "
          "draws, which is a question about concentration at a place. Global source "
          "shares, future illness counts, unmeasured history and policy outcomes are not "
          "answered by a filter and a pump."),

 dict(q="Two chambers of leaf litter are prepared identically, but one is kept moist and "
        "one is kept dry. Which aspect of the research design does this comparison "
        "represent?",
      choices=[
        "A single variable is changed between the chambers so that its effect on carbon "
        "dioxide release can be described",
        "Two variables are changed at once so that the experiment finishes sooner",
        "The measurement is changed from carbon dioxide to temperature",
        "The chambers are used as a substitute for a control",
        "The design removes the need to measure either chamber"],
      ans=0,
      why="Holding everything constant except moisture is what allows a difference in "
          "carbon dioxide release to be attributed to moisture. Changing more than one "
          "condition, changing what is measured, or omitting the measurement would all "
          "destroy that attribution."),

 dict(q="Which of the following would most improve a one-day study that reported "
        "particulate concentrations at a remote site?",
      choices=[
        "Repeating the sampling on many days across the year at the same site",
        "Reporting the single day's result to more decimal places",
        "Moving the sampler indoors for the day",
        "Sampling for a shorter period on the same day",
        "Comparing the result with a value remembered from another study"],
      ans=0,
      why="A single day cannot show whether a value is typical, so repeated sampling "
          "across the year is what strengthens the claim. Extra decimal places, an "
          "indoor site, a shorter run and an unrecorded comparison value do not address "
          "the limitation."),

 dict(q="A report states that a station recorded 9 micrograms of particulate matter per "
        "cubic meter of air. Which aspect of the measurement does the unit convey?",
      choices=[
        "The mass of particles present in each unit volume of the air sampled",
        "The number of particles counted, regardless of their size",
        "The distance the particles travelled before reaching the sampler",
        "The length of time the sampler was running",
        "The proportion of the particles that came from natural sources"],
      ans=0,
      why="Micrograms per cubic meter is a mass in a volume, so it reports how much "
          "particle mass the sampled air contained. It carries no information about "
          "particle counts, travel distance, running time or the origin of the particles."),

 dict(q="A student proposes to identify the natural sources of the carbon dioxide at a "
        "station by measuring only the total concentration there. What is the main "
        "limitation?",
      choices=[
        "A total concentration says how much is present but not which processes released "
        "it",
        "A total concentration cannot be measured at a rural station",
        "A total concentration is measured in the wrong units for a gas",
        "A total concentration changes only when there is an eruption",
        "A total concentration is unaffected by respiration or decomposition"],
      ans=0,
      why="The framework names several natural sources, all releasing the same gas, so a "
          "single concentration cannot distinguish among them. It can be measured "
          "anywhere and it does respond to respiration and decomposition, which is why "
          "the ambiguity is about attribution rather than about the measurement itself."),

 dict(q="Which comparison would best show whether human activity adds particulate matter "
        "to air that already contains some from natural sources?",
      choices=[
        "Simultaneous sampling at a site with heavy human activity and a site with none, "
        "using the same equipment",
        "Sampling at the site with heavy human activity on two different days",
        "Sampling at the remote site with a more sensitive instrument than the urban site",
        "Counting the vehicles at the urban site without sampling the air",
        "Sampling the urban site indoors and the remote site outdoors"],
      ans=0,
      why="Isolating the human contribution requires the two settings to be sampled at "
          "the same time with the same method, so that the difference reflects the "
          "setting. Different instruments, different indoor and outdoor placements, or "
          "no air sampling at all would each introduce a second difference."),

 dict(q="Why is it useful to know that carbon dioxide has natural sources when studying "
        "the effects of human emissions?",
      choices=[
        "Because a measured concentration includes carbon dioxide from natural sources, "
        "so a change attributed to human activity has to be measured against that "
        "background",
        "Because natural sources make human emissions harmless",
        "Because natural sources release a different gas that is easier to measure",
        "Because natural sources only operate where humans are absent",
        "Because natural carbon dioxide cannot mix with carbon dioxide from combustion"],
      ans=0,
      why="Respiration, decomposition and eruptions put carbon dioxide into the same air "
          "that human sources do, so any instrument reads the total. Attributing a "
          "change therefore requires the natural background to be accounted for, not "
          "that the two kinds of carbon dioxide are separable substances."),

 dict(q="In a study of particulates, why might a researcher weigh the filter both before "
        "and after sampling?",
      choices=[
        "The difference between the two masses is the mass of particles the filter "
        "collected",
        "The two weighings check that the pump ran at a constant speed",
        "The first weighing measures the air and the second measures the filter",
        "The two weighings together give the volume of air sampled",
        "Weighing twice removes the need to run a control site"],
      ans=0,
      why="A filter has a mass of its own, so only the increase during sampling belongs "
          "to the collected particles. The weighings say nothing about pump speed or air "
          "volume, and they do not substitute for a comparison site."),

 dict(q="Which statement best summarizes what this topic asks a student to be able to do?",
      choices=[
        "Describe the natural sources of carbon dioxide and of particulate matter, and "
        "describe how a study measures them",
        "Calculate the mass of carbon dioxide released by a named volcano in a named year",
        "Rank every natural source of particulate matter by the amount it releases "
        "worldwide",
        "Explain the chemistry by which carbon dioxide absorbs radiation",
        "List the diseases caused by exposure to particulate matter"],
      ans=0,
      why="The learning objective is to describe natural sources of carbon dioxide and "
          "particulates, and the suggested skill is to describe an aspect of a research "
          "method, design or measure. Named quantities, a global ranking, radiative "
          "chemistry and health effects belong to other statements or to other topics."),
]
