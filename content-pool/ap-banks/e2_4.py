# AP ENVIRONMENTAL SCIENCE 2.4 Ecological Tolerance
# CED effective Fall 2026, Unit 2 The Living World: Biodiversity.
# Enduring understanding ERT-2: ecosystems have structure and diversity that change over
# time.
# Learning objective ERT-2.F: describe ecological tolerance. Suggested skill 3.A, identify
# the author's claim.
#
# Essential knowledge relied on, in the framework's own words:
#   ERT-2.F.1  Ecological tolerance refers to the range of conditions, such as temperature,
#              salinity, flow rate, and sunlight, that an organism can endure before injury
#              or death results.
#   ERT-2.F.2  Ecological tolerance can apply to individuals and to species.
#
# THE STATEMENT HAS FOUR MOVING PARTS AND EVERY KEY USES ONE OF THEM: it is a RANGE rather
# than a single value; the conditions it ranges over are exemplified by temperature,
# salinity, flow rate and sunlight; the edge of the range is marked by INJURY OR DEATH; and
# it applies to individuals as well as to species.
#
# WHAT THE FRAMEWORK DOES NOT SAY, AND SO IS NOT ASKED. It gives no optimal range, no zone
# of stress, no law of the minimum and no claim that any one species tolerates more than
# another. Where a table shows one species enduring a wider range than another, the keyed
# conclusion is a reading OF THAT TABLE, arithmetic on its two limit columns, and the claim
# says so. No item asks a student to predict a limit that is not printed in its own table.
#
# The words WIDE and NARROW are used here only as ordinary descriptions of the size of a
# printed range, never as framework categories.
#
# BOUNDARY WITH 2.6. How populations respond to environmental change over generations is
# ERT-2.H in topic 2.6; nothing here is about natural selection or adaptation, only about
# the range an organism can endure at the time it is measured.
#
# NO FIGURES. Every quantitative item carries a table=, recomputed in verify_e2_4.py from
# that table alone; every computation is a subtraction or a comparison of two printed
# limits.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("2.4", "Ecological Tolerance", 2)

_T_TEMP = dict(
    headers=["Fish species",
             "Lowest water temperature endured without injury (degrees Celsius)",
             "Highest water temperature endured without injury (degrees Celsius)"],
    rows=[["Fish 1", "4", "26"],
          ["Fish 2", "12", "18"],
          ["Fish 3", "2", "31"],
          ["Fish 4", "15", "22"]])

_T_SALINITY = dict(
    headers=["Estuary species", "Lowest salinity endured (parts per thousand)",
             "Highest salinity endured (parts per thousand)"],
    rows=[["Estuary species 1", "0", "12"],
          ["Estuary species 2", "3", "34"],
          ["Estuary species 3", "25", "36"],
          ["Estuary species 4", "18", "28"]])

_T_FLOW = dict(
    headers=["Stream insect", "Lowest flow rate endured (centimetres per second)",
             "Highest flow rate endured (centimetres per second)"],
    rows=[["Insect 1", "5", "80"],
          ["Insect 2", "40", "55"],
          ["Insect 3", "0", "30"],
          ["Insect 4", "60", "120"]])

_T_SUN = dict(
    headers=["Woodland plant", "Lowest daily sunlight endured (hours)",
             "Highest daily sunlight endured (hours)"],
    rows=[["Plant 1", "1", "4"],
          ["Plant 2", "2", "11"],
          ["Plant 3", "1", "13"],
          ["Plant 4", "3", "9"]])

_T_INDIV = dict(
    headers=["Individual taken from one fish species",
             "Highest water temperature it endured without injury (degrees Celsius)"],
    rows=[["Individual 1", "24"],
          ["Individual 2", "27"],
          ["Individual 3", "25"],
          ["Individual 4", "30"],
          ["Individual 5", "26"]])

_T_SURVIVE = dict(
    headers=["Water temperature held in the tank (degrees Celsius)",
             "Percent of the fish surviving thirty days"],
    rows=[["2", "0"],
          ["6", "55"],
          ["14", "100"],
          ["20", "100"],
          ["26", "60"],
          ["32", "0"]])

QUESTIONS = [

 dict(q="What does the course framework say ecological tolerance refers to?",
      choices=[
        "The range of conditions an organism can endure before injury or death results.",
        "The single condition at which an organism grows fastest.",
        "The number of different habitats in which an organism has been recorded.",
        "The length of time an organism can survive without food.",
        "The proportion of an organism's offspring that reach maturity."],
      ans=0,
      why="ERT-2.F.1 states that ecological tolerance refers to the range of conditions "
          "that an organism can endure before injury or death results. It is a range with "
          "an endpoint at each end, not a single best value or a count of anything."),

 dict(q="Which set of conditions does the framework give as its examples of what ecological "
        "tolerance ranges over?",
      choices=[
        "Temperature, salinity, flow rate and sunlight.",
        "Temperature, altitude, wind speed and soil colour.",
        "Salinity, soil nitrogen, day length and predation.",
        "Flow rate, rainfall, air pressure and humidity.",
        "Sunlight, latitude, tree height and fire frequency."],
      ans=0,
      why="ERT-2.F.1 names temperature, salinity, flow rate and sunlight as the conditions "
          "it gives as examples. Every rejected set replaces at least one of the four with "
          "something the statement does not list."),

 dict(q="A study sheet lists five conditions and calls all five framework examples of what "
        "ecological tolerance ranges over. Which one is not?",
      choices=["Soil nitrogen content", "Temperature", "Salinity", "Flow rate", "Sunlight"],
      ans=0,
      why="ERT-2.F.1 gives temperature, salinity, flow rate and sunlight as its examples. "
          "Soil nitrogen content is not among the four the statement names."),

 dict(q="What outcome does the framework use to mark the edge of an organism's tolerance "
        "range?",
      choices=[
        "Injury or death.",
        "A fall in growth rate to half its usual value.",
        "A move to a different habitat.",
        "A failure to reproduce in that season.",
        "A change in the organism's colour or behaviour."],
      ans=0,
      why="ERT-2.F.1 defines the range as the conditions an organism can endure BEFORE "
          "INJURY OR DEATH RESULTS, so injury or death is the framework's own marker for "
          "the end of the range. It names no other threshold."),

 dict(q="What does the framework say ecological tolerance can apply to?",
      choices=[
        "Individuals and species alike.",
        "Species only, never a single organism.",
        "Individuals only, never a whole species.",
        "Whole ecosystems rather than the organisms in them.",
        "Only the populations living at the edge of a range."],
      ans=0,
      why="ERT-2.F.2 states that ecological tolerance can apply to individuals and to "
          "species. Both levels are named, and neither is excluded."),

 dict(q="A student writes that ecological tolerance is a property of a species and of "
        "nothing smaller. Which correction does the framework support?",
      choices=[
        "It can be a property of a single individual as well.",
        "It can be a property of an ecosystem but not of a species.",
        "It can be a property of a food web rather than of any organism.",
        "It can be a property of a habitat rather than of what lives there.",
        "It can be a property of a season rather than of an organism."],
      ans=0,
      why="ERT-2.F.2 states that ecological tolerance can apply to individuals and to "
          "species, so restricting it to the species level drops half of what the statement "
          "says."),

 dict(q="Why is a single temperature reading not enough to report an organism's ecological "
        "tolerance for temperature?",
      choices=[
        "Because tolerance is a range, which needs a limit at each end.",
        "Because temperature is not one of the conditions the framework names.",
        "Because tolerance is measured in units of time rather than temperature.",
        "Because tolerance applies to ecosystems and not to organisms.",
        "Because a reading taken once cannot be trusted at all."],
      ans=0,
      why="ERT-2.F.1 defines ecological tolerance as a RANGE of conditions, and a range is "
          "fixed by two endpoints. One reading names neither end, and temperature is in "
          "fact one of the four conditions the statement gives as examples."),

 dict(q="Four fish species were held at a series of water temperatures. Which endures the "
        "widest range of temperature?",
      table=_T_TEMP,
      choices=["Fish 3", "Fish 1", "Fish 2", "Fish 4",
               "All four endure the same width of range"],
      ans=0,
      why="The ranges are 26 less 4, 18 less 12, 31 less 2 and 22 less 15, which are 22, 6, "
          "29 and 7 degrees. The widest belongs to the species whose limits are 2 and 31. "
          "ERT-2.F.1 makes ecological tolerance a range between two limits, which is what "
          "these subtractions measure."),

 dict(q="How wide is the temperature range endured by the first of the four fish species?",
      table=_T_TEMP,
      choices=["Twenty-two degrees Celsius", "Four degrees Celsius",
               "Twenty-six degrees Celsius", "Thirty degrees Celsius",
               "Fifteen degrees Celsius"],
      ans=0,
      why="That species endures water from 4 to 26 degrees Celsius, and 26 less 4 is 22. "
          "ERT-2.F.1 defines the tolerance as the range between the limits, so the width is "
          "the difference of the two printed values."),

 dict(q="A tank is held at 30 degrees Celsius. Which of the four fish species is the only "
        "one that could endure it without injury?",
      table=_T_TEMP,
      choices=["Fish 3", "Fish 1", "Fish 2", "Fish 4", "None of the four could endure it"],
      ans=0,
      why="Enduring 30 degrees requires a lower limit at or below 30 and an upper limit at "
          "or above it, and only the species whose limits are 2 and 31 satisfies both. "
          "ERT-2.F.1 makes injury the outcome once a condition passes the end of the range."),

 dict(q="Which of the four fish species endures the narrowest range of water temperature?",
      table=_T_TEMP,
      choices=["Fish 2", "Fish 1", "Fish 3", "Fish 4",
               "The record does not allow the ranges to be compared"],
      ans=0,
      why="The four ranges are 22, 6, 29 and 7 degrees, so the smallest belongs to the "
          "species whose limits are 12 and 18. Both limits are printed for every species, "
          "so the comparison is available."),

 dict(q="Four estuary species were tested across a series of salinities. Which endures the "
        "widest range of salinity?",
      table=_T_SALINITY,
      choices=["Estuary species 2", "Estuary species 1", "Estuary species 3",
               "Estuary species 4", "All four endure the same width of range"],
      ans=0,
      why="The ranges are 12 less 0, 34 less 3, 36 less 25 and 28 less 18, which are 12, "
          "31, 11 and 10 parts per thousand. The widest belongs to the species whose limits "
          "are 3 and 34. ERT-2.F.1 names salinity among the conditions tolerance ranges "
          "over."),

 dict(q="An animal is carried from water at 5 parts per thousand to water at 32 parts per "
        "thousand. Which of the four estuary species could endure both?",
      table=_T_SALINITY,
      choices=["Estuary species 2", "Estuary species 1", "Estuary species 3",
               "Estuary species 4", "Every one of the four could endure both"],
      ans=0,
      why="Enduring both requires a lower limit at or below 5 and an upper limit at or "
          "above 32, and only the species whose limits are 3 and 34 satisfies both. "
          "ERT-2.F.1 makes injury or death the result of passing either end of the range."),

 dict(q="How wide is the salinity range endured by the third of the four estuary species?",
      table=_T_SALINITY,
      choices=["Eleven parts per thousand", "Twenty-five parts per thousand",
               "Thirty-six parts per thousand", "Sixty-one parts per thousand",
               "Thirty-one parts per thousand"],
      ans=0,
      why="That species endures salinity from 25 to 36 parts per thousand, and 36 less 25 "
          "is 11. The width of a range is the difference between its two limits, which is "
          "what ERT-2.F.1's definition makes the quantity of interest."),

 dict(q="Four stream insects were tested across a series of current speeds. Which endures "
        "the narrowest range of flow rate?",
      table=_T_FLOW,
      choices=["Insect 2", "Insect 1", "Insect 3", "Insect 4",
               "All four endure the same width of range"],
      ans=0,
      why="The ranges are 80 less 5, 55 less 40, 30 less 0 and 120 less 60, which are 75, "
          "15, 30 and 60 centimetres per second. The narrowest belongs to the insect whose "
          "limits are 40 and 55. ERT-2.F.1 names flow rate among its example conditions."),

 dict(q="A reach of stream runs at 100 centimetres per second. Which of the four insects "
        "could live there without injury?",
      table=_T_FLOW,
      choices=["Insect 4", "Insect 1", "Insect 2", "Insect 3",
               "None of the four could live there"],
      ans=0,
      why="Enduring that current requires a lower limit at or below 100 and an upper limit "
          "at or above it, and only the insect whose limits are 60 and 120 satisfies both. "
          "ERT-2.F.1 sets injury as the consequence of passing either end."),

 dict(q="Four woodland plants were grown under a series of daily sunlight hours. Which "
        "endures the widest range?",
      table=_T_SUN,
      choices=["Plant 3", "Plant 1", "Plant 2", "Plant 4",
               "All four endure the same width of range"],
      ans=0,
      why="The ranges are 4 less 1, 11 less 2, 13 less 1 and 9 less 3, which are 3, 9, 12 "
          "and 6 hours. The widest belongs to the plant whose limits are 1 and 13. "
          "ERT-2.F.1 names sunlight among the conditions ecological tolerance ranges over."),

 dict(q="A clearing receives 10 hours of direct sunlight a day. Which of the four woodland "
        "plants could endure it?",
      table=_T_SUN,
      choices=[
        "The second and the third plant only",
        "The first and the fourth plant only",
        "The third plant alone",
        "All four plants",
        "None of the four plants"],
      ans=0,
      why="Enduring 10 hours requires a lower limit at or below 10 and an upper limit at or "
          "above it. The plants with limits of 2 and 11, and of 1 and 13, satisfy both; the "
          "plant reaching only 4 hours and the plant reaching only 9 do not."),

 dict(q="Five individuals taken from one fish species were tested separately. What do their "
        "upper limits establish?",
      table=_T_INDIV,
      choices=[
        "Individuals of one species can differ in the temperature they endure.",
        "Every individual of one species endures exactly the same temperature.",
        "Ecological tolerance cannot be measured on a single individual.",
        "The five individuals must belong to five different species.",
        "The upper limit falls as an individual grows older."],
      ans=0,
      why="The five upper limits are 24, 27, 25, 30 and 26 degrees Celsius, so they are not "
          "all the same. ERT-2.F.2 states that ecological tolerance can apply to "
          "individuals as well as to species, which is what makes a per individual limit a "
          "meaningful measurement."),

 dict(q="Across those five individuals, how far apart are the highest and the lowest upper "
        "limit?",
      table=_T_INDIV,
      choices=["Six degrees Celsius", "Two degrees Celsius", "Thirty degrees Celsius",
               "Twenty-four degrees Celsius", "Fifty-four degrees Celsius"],
      ans=0,
      why="The highest of the five limits is 30 degrees Celsius and the lowest is 24, and "
          "30 less 24 is 6. ERT-2.F.2 allows tolerance to be a property of an individual, "
          "so a spread between individuals is a quantity that can be reported."),

 dict(q="One fish species was held for thirty days at each of six temperatures. What does "
        "the survival record establish?",
      table=_T_SURVIVE,
      choices=[
        "Survival is complete only over a middle band of temperatures and reaches zero at "
        "both the cold and the warm end.",
        "Survival is complete at the coldest temperature tested and falls steadily as the "
        "water warms.",
        "Survival is complete at the warmest temperature tested and falls steadily as the "
        "water cools.",
        "Survival is the same at every temperature tested.",
        "Survival reaches zero only at the warm end of the series."],
      ans=0,
      why="Survival reads 0, 55, 100, 100, 60 and 0 percent as the water warms from 2 to 32 "
          "degrees Celsius, so it is complete in the middle and nil at both extremes. "
          "ERT-2.F.1 makes tolerance a range bounded at each end by injury or death."),

 dict(q="At which of the tested temperatures did every fish survive the thirty days?",
      table=_T_SURVIVE,
      choices=[
        "At 14 and at 20 degrees Celsius",
        "At 2 and at 32 degrees Celsius",
        "At 6 and at 26 degrees Celsius",
        "At every temperature tested",
        "At none of the temperatures tested"],
      ans=0,
      why="Two of the six rows record 100 percent surviving, and they are the two middle "
          "temperatures. The coldest and the warmest rows record none surviving, which "
          "ERT-2.F.1 identifies as the outcome beyond the ends of the range."),

 dict(q="Which observation would report a species' ecological tolerance for salinity as the "
        "framework defines it?",
      choices=[
        "The lowest and the highest salinity at which individuals survive without injury.",
        "The salinity at which the species grows fastest.",
        "The average salinity of the estuaries where the species has been found.",
        "The number of estuaries in which the species has been recorded.",
        "The salinity of the water on the day the species was first described."],
      ans=0,
      why="ERT-2.F.1 defines ecological tolerance as the RANGE of conditions endured before "
          "injury or death, so the report has to name both ends of that range. A fastest "
          "growth point, an average, a count and a single day's reading each name something "
          "else."),

 dict(q="A researcher claims a stream insect endures a wide range of flow rates. Which "
        "study would test the claim most directly?",
      choices=[
        "Holding insects at a series of flow rates and recording the rates at which injury "
        "first appears at the slow end and at the fast end.",
        "Recording the flow rate of the one stream in which the insect is most abundant.",
        "Counting how many other insect species live in the same stream.",
        "Measuring how fast the insect swims in still water.",
        "Recording the water temperature of every stream in which the insect occurs."],
      ans=0,
      why="ERT-2.F.1 makes ecological tolerance a range ending in injury or death, so a "
          "direct test has to locate both endpoints. One stream's flow rate, a species "
          "count, a swimming speed and a temperature record locate neither."),

 dict(q="Two individuals of one plant species are found to wilt at different soil "
        "temperatures. What does the framework allow a student to conclude?",
      choices=[
        "Ecological tolerance can apply to individuals, so two individuals may have "
        "different limits.",
        "Ecological tolerance applies only to species, so one of the two measurements must "
        "be an error.",
        "The two individuals must belong to different species.",
        "Ecological tolerance changes only when a species evolves, so neither result is "
        "usable.",
        "The framework gives no way to describe a limit for a plant."],
      ans=0,
      why="ERT-2.F.2 states that ecological tolerance can apply to individuals and to "
          "species. A difference between two individuals is therefore an ordinary result "
          "rather than a contradiction or an error."),

 dict(q="An author writes: below 3 degrees Celsius the larvae die, between 3 and 24 degrees "
        "they feed and grow, and above 24 degrees they are damaged. What claim is the "
        "author making?",
      choices=[
        "That the larvae's ecological tolerance for temperature is bounded at both ends.",
        "That the larvae have no upper limit for temperature.",
        "That the larvae grow fastest at 24 degrees Celsius.",
        "That temperature has no effect on the larvae between the two limits.",
        "That the larvae's tolerance applies to the species but not to any individual."],
      ans=0,
      why="The passage names a temperature below which the larvae die and one above which "
          "they are damaged, which is exactly the shape ERT-2.F.1 gives ecological "
          "tolerance: a range whose ends are marked by injury or death. The author states "
          "no growth maximum and denies no upper limit."),

 dict(q="Which of these does the framework NOT assert about ecological tolerance?",
      choices=[
        "That every species endures a range of the same width.",
        "That it is a range rather than a single value.",
        "That it can be reported for an individual.",
        "That its ends are marked by injury or death.",
        "That temperature is one of the conditions it can range over."],
      ans=0,
      why="ERT-2.F.1 supplies the range, the examples and the endpoint of injury or death, "
          "and ERT-2.F.2 supplies the individual level. Neither statement compares the "
          "widths of different species' ranges, so a claim that all are equal is an "
          "addition rather than a reading."),

 dict(q="A stream insect survives only between two closely spaced current speeds and is "
        "injured outside them. Which description uses the framework's term correctly?",
      choices=[
        "It has a narrow ecological tolerance for flow rate.",
        "It has a narrow ecological tolerance for salinity.",
        "It has no ecological tolerance at all.",
        "It has an ecological tolerance that applies to the stream rather than to the "
        "insect.",
        "It has an ecological tolerance measured in individuals per square metre."],
      ans=0,
      why="ERT-2.F.1 names flow rate among the conditions ecological tolerance ranges over, "
          "and describes the range as bounded by injury or death. Narrow is an ordinary "
          "description of the size of that range; the condition being tolerated here is "
          "current speed rather than salt, and the tolerance belongs to the organism."),

 dict(q="Two accounts of a fish's temperature limits are offered. Which stays within what "
        "the framework asserts?",
      choices=[
        "The fish endures water between two temperatures, and outside them injury or death "
        "results; the same range can be reported for one fish or for the species.",
        "The fish endures water below one temperature only, and above it the fish simply "
        "moves elsewhere.",
        "The fish endures every temperature, and the range describes only how fast it "
        "grows.",
        "The fish endures water between two temperatures, but the range can be reported "
        "only for the species and never for one fish.",
        "The fish endures water between two temperatures, and outside them the species "
        "evolves a new limit within one generation."],
      ans=0,
      why="ERT-2.F.1 supplies the range and the injury or death that marks its ends, and "
          "ERT-2.F.2 supplies both levels of application. Each rejected account drops one "
          "end of the range, replaces injury with movement or with growth rate, forbids the "
          "individual level, or adds an evolutionary claim the statement does not make."),

 dict(q="Which single sentence collects what this topic's two statements assert and nothing "
        "further?",
      choices=[
        "Ecological tolerance is the range of conditions, such as temperature, salinity, "
        "flow rate and sunlight, that an organism endures before injury or death, and it "
        "can be reported for an individual or for a species.",
        "Ecological tolerance is the single condition at which an organism does best, and it "
        "can be reported for an individual or for a species.",
        "Ecological tolerance is the range of conditions an organism endures before injury "
        "or death, and it can be reported only for a whole species.",
        "Ecological tolerance is the range of conditions an organism prefers, and every "
        "species has a range of the same width.",
        "Ecological tolerance is the range of temperatures an organism endures, and no "
        "other condition is covered by the term."],
      ans=0,
      why="ERT-2.F.1 supplies the range, the four example conditions and the injury or "
          "death that ends it; ERT-2.F.2 supplies the two levels it can apply to. Each "
          "rejected summary replaces the range with an optimum, forbids the individual "
          "level, adds an equal-width claim, or narrows the conditions to temperature "
          "alone."),
]
