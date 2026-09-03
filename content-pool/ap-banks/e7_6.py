# AP ENVIRONMENTAL SCIENCE 7.6 Reduction of Air Pollutants
# CED effective Fall 2026, Unit 7 Atmospheric Pollution. Enduring understanding STB-2.
# Learning objective STB-2.G: explain how air pollutants can be reduced at the source.
# Suggested skill 7.D, use data and evidence to support a potential solution.
#
# Essential knowledge relied on, in the framework's own words:
#   STB-2.G.1  Methods to reduce air pollutants include regulatory practices,
#              conservation practices, and alternative fuels.
#   STB-2.G.2  A vapor recovery nozzle is an air pollution control device on a gasoline
#              pump that prevents fumes from escaping into the atmosphere when fueling
#              a motor vehicle.
#   STB-2.G.3  A catalytic converter is an air pollution control device for internal
#              combustion engines that converts pollutants (CO, NOx, and hydrocarbons)
#              in exhaust into less harmful molecules (CO2, N2, O2, and H2O).
#   STB-2.G.4  Wet and dry scrubbers are air pollution control devices that remove
#              particulates and/or gases from industrial exhaust streams.
#   STB-2.G.5  Methods to reduce air pollution from coal-burning power plants include
#              scrubbers and electrostatic precipitators.
#
# ON SCOPE. Topic 7.1 keys the sources of the pollutants and 7.2 keys the two
# reductions that lower photochemical smog; this topic keys the DEVICES and the three
# categories of method, and the evidence that would support choosing one. No item here
# re-asks which pollutants a source releases.
#
# ON WHAT THE FRAMEWORK DOES NOT SAY. It gives no removal efficiency, no cost, no
# statutory limit, and no mechanism for an electrostatic precipitator beyond naming it
# as a method for coal-burning power plants. So every efficiency and cost in this
# module is stated in the stem or the table as the data of that question, never keyed
# as a fact to be recalled, and no key asserts how a precipitator works internally.
#
# Formulas appear only where the framework prints them, as plain text: CO, NOx, CO2,
# N2, O2, H2O. ENV_SCI is not typeset, so nothing here carries a math span.
#
# FIVE choices (A-E). No LaTeX and no non-ASCII.
TOPIC = ("7.6", "Reduction of Air Pollutants", 7)

_T_CONVERTER = dict(
    headers=["Pollutant measured in the exhaust",
             "Without a catalytic converter (grams per kilometer)",
             "With a catalytic converter (grams per kilometer)"],
    rows=[["Carbon monoxide", "12.0", "1.2"],
          ["Hydrocarbons", "1.6", "0.2"],
          ["Nitrogen oxides", "1.8", "0.3"],
          ["Carbon dioxide", "180", "184"]])

_T_SCRUB = dict(
    headers=["Coal plant", "Control equipment fitted",
             "Sulfur dioxide released (tons per year)",
             "Particulates released (tons per year)"],
    rows=[["Plant 1", "none", "5,000", "700"],
          ["Plant 2", "scrubber only", "600", "660"],
          ["Plant 3", "electrostatic precipitator only", "4,800", "40"],
          ["Plant 4", "scrubber and precipitator", "550", "35"]])

_T_NOZZLE = dict(
    headers=["Filling station", "Vapor recovery nozzles fitted",
             "Hydrocarbon vapor escaping per 1,000 liters dispensed (grams)"],
    rows=[["Station 1", "no", "1,300"],
          ["Station 2", "no", "1,150"],
          ["Station 3", "yes", "180"],
          ["Station 4", "yes", "140"]])

_T_METHODS = dict(
    headers=["Proposed measure for one city",
             "Category of method",
             "Modeled fall in city-wide pollutant releases (percent)"],
    rows=[["A limit on the sulfur content of fuel sold", "regulatory practice", "18"],
          ["A campaign to reduce unnecessary vehicle trips", "conservation practice", "7"],
          ["A switch of the bus fleet to an alternative fuel", "alternative fuel", "11"]])

_T_FUELSWAP = dict(
    headers=["Fuel used by a fleet of buses",
             "Sulfur dioxide released per 1,000 kilometers (grams)",
             "Particulates released per 1,000 kilometers (grams)"],
    rows=[["High-sulfur diesel", "900", "260"],
          ["Low-sulfur diesel", "90", "150"],
          ["Compressed natural gas", "6", "20"]])

_T_UPGRADE = dict(
    headers=["Year of the upgrade program",
             "Share of the vehicle fleet fitted with catalytic converters (percent)",
             "Carbon monoxide measured downtown (parts per million)"],
    rows=[["Year 1", "10", "9.0"],
          ["Year 3", "35", "6.4"],
          ["Year 5", "70", "3.8"],
          ["Year 7", "95", "2.2"]])

QUESTIONS = [

 dict(q="Which three kinds of method does the framework give for reducing air "
        "pollutants?",
      choices=[
        "Regulatory practices, conservation practices, and alternative fuels",
        "Taxation, migration, and urbanization",
        "Dilution, dispersion, and burial",
        "Reforestation, irrigation, and terracing",
        "Primary treatment, secondary treatment, and tertiary treatment"],
      ans=0,
      why="The framework states that methods to reduce air pollutants include "
          "regulatory practices, conservation practices, and alternative fuels. The "
          "other groupings belong to different parts of the course, and dilution and "
          "burial are not offered as methods of reduction at all."),

 dict(q="What does a vapor recovery nozzle do?",
      choices=[
        "It prevents fumes from escaping into the atmosphere while a motor vehicle is "
        "being fueled",
        "It converts exhaust gases leaving an engine into less harmful molecules",
        "It removes particulates from an industrial exhaust stream",
        "It filters the air entering a building through its ventilation system",
        "It reduces the sulfur content of the fuel as it is pumped"],
      ans=0,
      why="The framework defines a vapor recovery nozzle as an air pollution control "
          "device on a gasoline pump that prevents fumes from escaping into the "
          "atmosphere when fueling a motor vehicle. Converting exhaust and removing "
          "particulates are the jobs of other devices it names."),

 dict(q="A catalytic converter is fitted to an internal combustion engine. Which "
        "conversion does the framework attribute to it?",
      choices=[
        "Carbon monoxide, nitrogen oxides, and hydrocarbons into carbon dioxide, "
        "nitrogen, oxygen, and water",
        "Carbon dioxide into carbon monoxide and free carbon",
        "Sulfur dioxide into sulfuric acid collected as a liquid",
        "Particulate matter into a gas that leaves the tailpipe",
        "Nitrogen in the air into ammonia used as a fuel"],
      ans=0,
      why="The framework states that a catalytic converter converts the pollutants CO, "
          "NOx, and hydrocarbons in exhaust into the less harmful molecules CO2, N2, O2, "
          "and H2O. The rejected conversions run the wrong way or involve substances the "
          "framework does not assign to this device."),

 dict(q="Exhaust measurements from one vehicle model are shown.",
      table=_T_CONVERTER,
      choices=[
        "Carbon monoxide, hydrocarbons, and nitrogen oxides all fall sharply with the "
        "converter fitted, while carbon dioxide does not fall",
        "All four measured substances fall sharply with the converter fitted",
        "The three pollutants rise with the converter fitted",
        "Only carbon monoxide changes when the converter is fitted",
        "Carbon dioxide falls by the largest amount of the four"],
      ans=0,
      why="The three pollutants the framework names each drop by most of their "
          "uncontrolled value, while the carbon dioxide reading is slightly higher "
          "rather than lower. That is consistent with a device that converts those "
          "pollutants into carbon dioxide, nitrogen, oxygen and water."),

 dict(q="Wet and dry scrubbers are described by the framework as air pollution control "
        "devices. What do they do?",
      choices=[
        "They remove particulates and gases from industrial exhaust streams",
        "They increase the temperature of an industrial exhaust stream",
        "They prevent fuel vapors from escaping at a filling station",
        "They convert engine exhaust into less harmful molecules",
        "They monitor the concentration of pollutants without removing any"],
      ans=0,
      why="The framework states that wet and dry scrubbers remove particulates and gases "
          "from industrial exhaust streams. Fuel vapor capture belongs to the vapor "
          "recovery nozzle and exhaust conversion to the catalytic converter, and a "
          "monitor is not a control device."),

 dict(q="Which methods does the framework name for reducing air pollution from "
        "coal-burning power plants?",
      choices=[
        "Scrubbers and electrostatic precipitators",
        "Vapor recovery nozzles and catalytic converters",
        "Thermal inversions and atmospheric mixing",
        "Indoor ventilation systems and air filters",
        "Reforestation of the land around the plant"],
      ans=0,
      why="The framework names scrubbers and electrostatic precipitators as methods to "
          "reduce air pollution from coal-burning power plants. Vapor recovery nozzles "
          "belong to gasoline pumps and catalytic converters to internal combustion "
          "engines."),

 dict(q="Emissions from four coal plants of similar size are shown.",
      table=_T_SCRUB,
      choices=[
        "The plant with both devices is lowest in both pollutants, while each single "
        "device lowers one pollutant much more than the other",
        "Each single device lowers both pollutants equally",
        "The plant with no control equipment is lowest in both pollutants",
        "Fitting both devices raises the sulfur dioxide above the uncontrolled plant",
        "None of the control equipment changes either measurement"],
      ans=0,
      why="The plant with both devices carries the smallest value in each column, while "
          "the scrubber-only plant is far lower in sulfur dioxide than in particulates "
          "and the precipitator-only plant the reverse. Both devices are among those the "
          "framework names for coal-burning power plants."),

 dict(q="Vapor measurements at four filling stations are shown.",
      table=_T_NOZZLE,
      choices=[
        "The stations fitted with vapor recovery nozzles lose far less hydrocarbon vapor "
        "per volume dispensed than the stations without them",
        "The stations fitted with the nozzles lose more vapor per volume dispensed",
        "Vapor loss per volume dispensed is the same at all four stations",
        "Only one of the fitted stations differs from the unfitted stations",
        "The measurements show that vapor cannot escape from a fuel pump"],
      ans=0,
      why="Both fitted stations lose less than a fifth of what either unfitted station "
          "loses per volume dispensed. The framework describes the vapor recovery nozzle "
          "as a device that prevents fumes from escaping into the atmosphere when a "
          "vehicle is fueled."),

 dict(q="A city considers three measures. Their modeled effects are shown.",
      table=_T_METHODS,
      choices=[
        "The three measures illustrate the framework's three categories of method, and "
        "the regulatory measure is modeled to achieve the largest reduction here",
        "All three measures fall into the same category of method",
        "The conservation measure is modeled to achieve the largest reduction",
        "The alternative fuel measure is modeled to achieve no reduction at all",
        "The three measures are modeled to achieve identical reductions"],
      ans=0,
      why="The table labels one measure in each of the three categories the framework "
          "names, and the regulatory measure carries the largest modeled reduction of "
          "the three. The other readings contradict the labels or the numbers in the "
          "same table."),

 dict(q="Which of the following is best described as a conservation practice for "
        "reducing air pollutants?",
      choices=[
        "Reducing the number of vehicle trips taken so that less fuel is burned",
        "Setting a legal limit on the sulfur content of fuel",
        "Requiring every new vehicle to carry a catalytic converter",
        "Fitting a scrubber to the exhaust stream of a factory",
        "Replacing a diesel bus fleet with buses that run on a different fuel"],
      ans=0,
      why="A conservation practice reduces the activity that releases the pollutant, "
          "which is what fewer trips does. A legal limit and an equipment requirement "
          "are regulatory practices, a scrubber is a control device, and changing the "
          "fuel is the alternative fuel category."),

 dict(q="Why does the framework treat a catalytic converter as reducing pollution even "
        "though the exhaust still leaves the tailpipe?",
      choices=[
        "It converts the pollutants in the exhaust into less harmful molecules before "
        "they leave",
        "It stores the exhaust permanently inside the vehicle",
        "It prevents the engine from burning any fuel",
        "It cools the exhaust so that the pollutants become invisible",
        "It measures the pollutants so that the driver can avoid releasing them"],
      ans=0,
      why="The framework describes the converter as converting CO, NOx and hydrocarbons "
          "into CO2, N2, O2 and H2O, so what leaves is a different mixture rather than "
          "the same one. It does not store exhaust, stop combustion, or merely measure."),

 dict(q="Downtown measurements taken during a fleet upgrade program are shown.",
      table=_T_UPGRADE,
      choices=[
        "Carbon monoxide downtown fell as the share of the fleet fitted with catalytic "
        "converters rose",
        "Carbon monoxide downtown rose as the fitted share rose",
        "Carbon monoxide downtown was unchanged throughout the program",
        "The fitted share fell over the course of the program",
        "The two measurements are unrelated in these data"],
      ans=0,
      why="The fitted share rises at every step of the record while the measured carbon "
          "monoxide falls at every step. Carbon monoxide is one of the pollutants the "
          "framework has the catalytic converter convert into less harmful molecules."),

 dict(q="A factory releases both particulates and a corrosive gas in its exhaust stream. "
        "Which control device does the framework describe as suited to that exhaust?",
      choices=[
        "A scrubber, which removes particulates and gases from industrial exhaust streams",
        "A vapor recovery nozzle, which is fitted to a gasoline pump",
        "A catalytic converter, which is fitted to an internal combustion engine",
        "A thermal inversion, which holds pollution near the ground",
        "A ventilation fan, which moves indoor air outdoors"],
      ans=0,
      why="The framework assigns the removal of particulates and gases from industrial "
          "exhaust streams to wet and dry scrubbers. The nozzle and the converter are "
          "defined for a fuel pump and an engine, an inversion is an atmospheric "
          "condition, and a fan relocates air rather than cleaning it."),

 dict(q="Emissions from a bus fleet running on three different fuels are shown.",
      table=_T_FUELSWAP,
      choices=[
        "Switching from high-sulfur diesel to either of the other fuels lowers both "
        "pollutants, and compressed natural gas is lowest in both",
        "Switching fuels lowers the sulfur dioxide but raises the particulates",
        "High-sulfur diesel is lowest in both pollutants",
        "The three fuels produce identical emissions",
        "Compressed natural gas is lowest in sulfur dioxide but highest in particulates"],
      ans=0,
      why="Both alternatives carry smaller values than high-sulfur diesel in each "
          "column, and compressed natural gas carries the smallest value in both. "
          "Alternative fuels are one of the three categories of method the framework "
          "names."),

 dict(q="Which piece of evidence would best support a proposal to require vapor recovery "
        "nozzles at every filling station in a region?",
      choices=[
        "Measurements showing that stations already using the nozzles release far less "
        "fuel vapor per volume dispensed than stations without them",
        "Measurements showing that stations using the nozzles sell more fuel than other "
        "stations",
        "Measurements showing that the nozzles are the same color as the existing ones",
        "Measurements showing that fuel vapor is heavier than air",
        "Measurements showing that vehicles fueled at those stations travel farther"],
      ans=0,
      why="Suggested skill 7.D asks for data supporting a solution, and the data that "
          "support this one are a measured difference in the vapor released with and "
          "without the device. Sales volume, appearance, vapor density and vehicle range "
          "do not measure the release the nozzle is meant to prevent."),

 dict(q="Which measure is best described as a regulatory practice?",
      choices=[
        "A law setting a maximum allowable release of a pollutant from new vehicles",
        "A household choosing to walk instead of drive on short journeys",
        "A power plant voluntarily installing a scrubber",
        "A bus company switching to a fuel that releases less sulfur dioxide",
        "A driver keeping tires inflated to reduce fuel use"],
      ans=0,
      why="A regulatory practice is a rule imposed by law, which is what a maximum "
          "allowable release is. Walking, keeping tires inflated and a voluntary "
          "installation are choices rather than rules, and changing fuel is the "
          "alternative fuel category."),

 dict(q="An analyst argues that fitting catalytic converters to a city's vehicles cannot "
        "reduce the pollutants the framework attributes to them, because the vehicles "
        "still run. Which response is best supported?",
      choices=[
        "The converter changes what leaves the tailpipe, so the same amount of driving "
        "releases less carbon monoxide, fewer nitrogen oxides and fewer hydrocarbons",
        "The converter stops the engine from running, so no pollutants are released at all",
        "The converter has no effect until driving is also reduced",
        "The converter releases the same pollutants in a different order",
        "The converter works only on vehicles that burn no fuel"],
      ans=0,
      why="The framework describes the converter as converting the pollutants in exhaust "
          "into less harmful molecules, which is a change in what is released rather "
          "than in how much driving occurs. It is defined for internal combustion "
          "engines, so it applies precisely to vehicles that do burn fuel."),

 dict(q="Which comparison would best show whether a newly installed scrubber is working "
        "as intended at a factory?",
      choices=[
        "Measurements of the exhaust stream before and after the scrubber was installed, "
        "with production held steady",
        "Measurements of the exhaust stream only after the scrubber was installed",
        "The number of workers employed at the factory in each year",
        "The purchase price of the scrubber compared with other equipment",
        "The concentration of pollutants measured in a city fifty kilometers away"],
      ans=0,
      why="Suggested skill 7.D. Attributing a change to the device requires readings "
          "from before and after it was fitted with the activity held constant, so the "
          "difference cannot be a change in output. A single later reading, employment, "
          "price and a distant city all leave the comparison unmade."),

 dict(q="Why does the framework describe pollution control devices as reducing "
        "pollutants at the source?",
      choices=[
        "Each device acts on the exhaust or vapor where it is produced, before it enters "
        "the wider atmosphere",
        "Each device collects pollution after it has spread across a region",
        "Each device converts outdoor pollution into indoor pollution",
        "Each device works only once the pollution has reached ground level",
        "Each device removes pollution that was released in an earlier year"],
      ans=0,
      why="The vapor recovery nozzle acts at the pump, the catalytic converter in the "
          "engine's exhaust and the scrubber in the industrial exhaust stream, so each "
          "acts before release into the atmosphere. None of them retrieves pollution "
          "already dispersed."),

 dict(q="A region reports that its sulfur dioxide releases fell after two changes: coal "
        "plants fitted scrubbers, and a law lowered the sulfur content allowed in fuel. "
        "Which description of the two changes is accurate?",
      choices=[
        "One is a control device fitted to an exhaust stream and the other is a "
        "regulatory practice",
        "Both are conservation practices",
        "Both are alternative fuels",
        "One is a conservation practice and the other is a control device fitted to an "
        "engine",
        "Neither is among the methods the framework names"],
      ans=0,
      why="A scrubber is one of the control devices the framework names for industrial "
          "and coal plant exhaust, and a legal limit on fuel composition is a regulatory "
          "practice, one of its three categories of method. Neither reduces the activity "
          "itself, so neither is a conservation practice."),

 dict(q="Which of the following best explains why a device that removes particulates "
        "from a coal plant's exhaust may leave its sulfur dioxide release almost "
        "unchanged?",
      choices=[
        "A device that captures solid particles from the stream does not by itself "
        "remove a gas from it",
        "Sulfur dioxide is not released by coal plants at all",
        "Sulfur dioxide is destroyed by any device placed in an exhaust stream",
        "Particulates and sulfur dioxide are the same substance measured differently",
        "A device can only remove one pollutant per plant by law"],
      ans=0,
      why="The framework distinguishes devices by what they remove, giving scrubbers the "
          "removal of particulates and gases and naming precipitators separately among "
          "the methods for coal plants. A device aimed at solid particles therefore need "
          "not affect a gas in the same stream."),

 dict(q="A city wants evidence that a proposed switch of its bus fleet to an alternative "
        "fuel would reduce air pollutants. Which evidence is most relevant?",
      choices=[
        "Measured releases per kilometer travelled for buses running on the current fuel "
        "and on the proposed fuel",
        "The number of passengers each bus can carry",
        "The color and age of the buses in the current fleet",
        "The distance from the bus depot to the city center",
        "The number of bus routes the city operates"],
      ans=0,
      why="Suggested skill 7.D. Comparing releases per kilometer for the two fuels is "
          "what shows whether the switch reduces pollution for the same amount of "
          "service. Capacity, appearance, depot location and route count do not measure "
          "any release."),

 dict(q="Which statement best describes the relationship between the three categories of "
        "method and the specific devices the framework names?",
      choices=[
        "The devices are particular ways of carrying out the broader methods, and a "
        "regulation can require a device to be used",
        "The devices and the methods are alternatives that cannot be combined",
        "The devices apply only to indoor air and the methods only to outdoor air",
        "The methods apply only to coal plants and the devices only to vehicles",
        "The devices replace the need for any regulatory or conservation practice"],
      ans=0,
      why="The framework lists regulatory practices, conservation practices and "
          "alternative fuels as methods, and separately names devices for pumps, engines "
          "and industrial exhaust. A rule requiring a device is a regulatory practice "
          "carried out through a device, so the two are not exclusive."),

 dict(q="Which observation would most weaken a claim that a filling station's vapor "
        "recovery nozzles are reducing hydrocarbon releases?",
      choices=[
        "Vapor escaping per volume of fuel dispensed is the same as at nearby stations "
        "without the nozzles",
        "The station dispenses more fuel than nearby stations",
        "The station is located farther from the city center than the others",
        "The nozzles were installed more recently than those at other stations",
        "The station sells a different brand of fuel from the others"],
      ans=0,
      why="The device is meant to prevent fumes escaping during fueling, so the finding "
          "that undermines the claim is an escape rate no lower than at stations without "
          "it. Volume dispensed, location, installation date and fuel brand say nothing "
          "about the escape per volume."),

 dict(q="Why is it useful to express a control device's effect as the release per "
        "kilometer travelled or per volume dispensed rather than as a total for the "
        "year?",
      choices=[
        "A rate per unit of activity allows two situations with different amounts of "
        "activity to be compared fairly",
        "A rate is always a smaller number and therefore easier to report",
        "A total cannot be measured once a device is fitted",
        "A rate removes the need to measure the pollutant at all",
        "A total is only valid for gases and a rate only for particles"],
      ans=0,
      why="Suggested skill 7.D. A yearly total confounds how clean each unit of activity "
          "is with how much activity took place, so the rate is what isolates the "
          "device's effect. The size of the number and the physical state of the "
          "pollutant are irrelevant to that."),

 dict(q="A power plant fits both a scrubber and an electrostatic precipitator. Which "
        "expectation follows from the framework's treatment of coal plant methods?",
      choices=[
        "Both devices are among the methods named for reducing air pollution from "
        "coal-burning power plants, so the plant addresses more than one pollutant",
        "The two devices cancel each other out and neither works",
        "Only the device fitted first can have any effect",
        "The plant no longer needs to burn coal to generate electricity",
        "The plant will release no pollutants of any kind"],
      ans=0,
      why="The framework names scrubbers and electrostatic precipitators together as "
          "methods for coal-burning power plants, and scrubbers are separately described "
          "as removing particulates and gases. Nothing in the framework has one device "
          "disable another or make the fuel unnecessary."),

 dict(q="A student proposes reducing a city's air pollution by building taller "
        "smokestacks. How does this compare with the methods the framework names?",
      choices=[
        "It changes where the pollution goes rather than reducing the amount released, "
        "so it is not one of the reduction methods the framework gives",
        "It is a conservation practice, because it conserves the height of the plant",
        "It is a regulatory practice, because stack height can be regulated",
        "It is an alternative fuel, because it changes how the fuel burns",
        "It is a control device, because it is attached to the exhaust stream"],
      ans=0,
      why="The framework's methods and devices either reduce the activity, change the "
          "fuel, require a change by rule, or remove and convert pollutants before "
          "release. A taller stack does none of those, since the same material still "
          "enters the atmosphere."),

 dict(q="Which pair of measurements would best support a claim that a city's catalytic "
        "converter program is responsible for a fall in carbon monoxide?",
      choices=[
        "The share of the fleet fitted with converters and the measured carbon monoxide, "
        "both recorded over the same years",
        "The share of the fleet fitted with converters and the number of vehicles sold "
        "nationally",
        "The measured carbon monoxide and the average price of fuel in another country",
        "The number of converters manufactured and the population of the city",
        "The measured carbon monoxide in one year and the fleet share in a different "
        "decade"],
      ans=0,
      why="Suggested skill 7.D. Linking the program to the outcome requires both "
          "quantities over the same period, so that the change in one can be set beside "
          "the change in the other. National sales, foreign fuel prices, manufacturing "
          "counts and mismatched periods break that link."),

 dict(q="Why does the framework describe the molecules a catalytic converter produces as "
        "less harmful rather than as harmless?",
      choices=[
        "The products include carbon dioxide, which the course treats as a pollutant of "
        "concern in its own right",
        "The products are the same pollutants that entered the converter",
        "The products are radioactive and decay over time",
        "The products cannot be measured with ordinary instruments",
        "The products are removed from the exhaust and stored in the vehicle"],
      ans=0,
      why="The framework's own wording is less harmful molecules, and the list of "
          "products it gives includes CO2, which appears throughout the course as an "
          "atmospheric pollutant. The products are not the original pollutants, are not "
          "radioactive, and are not retained in the vehicle."),

 dict(q="Which summary best captures how the framework organizes the reduction of air "
        "pollutants?",
      choices=[
        "Three broad kinds of method, together with named devices that capture vapor at "
        "the pump, convert exhaust in an engine, and remove particulates and gases from "
        "industrial streams",
        "A single method that applies equally to every source of air pollution",
        "A list of devices with no broader categories of method behind them",
        "A set of methods that apply only after pollution has entered the atmosphere",
        "A requirement that all combustion be stopped in order to reduce pollution"],
      ans=0,
      why="The framework gives regulatory practices, conservation practices and "
          "alternative fuels as the three kinds of method, and separately defines the "
          "vapor recovery nozzle, the catalytic converter, scrubbers and electrostatic "
          "precipitators. Both halves of that structure are needed, and both act before "
          "release rather than after it."),
]
