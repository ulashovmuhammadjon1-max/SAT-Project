# AP ENVIRONMENTAL SCIENCE 5.15 Sustainable Agriculture
# CED effective Fall 2026, Unit 5 Land and Water Use.
# Enduring understanding STB-1: humans can mitigate their impact on land and water
# resources through sustainable use.
# Learning objective STB-1.E, describe sustainable agricultural and food production
# practices.
# Suggested skill 7.E, make a claim that proposes a solution to an environmental problem
# in an applied context.
#
# Essential knowledge relied on, in the framework's own words:
#   STB-1.E.1  The goal of soil conservation is to prevent soil erosion. Different methods
#              of soil conservation include contour plowing, windbreaks, perennial crops,
#              terracing, no-till agriculture, and strip cropping.
#   STB-1.E.2  Strategies to improve soil fertility include crop rotation and the addition
#              of green manure and limestone.
#   STB-1.E.3  Rotational grazing is the regular rotation of livestock between different
#              pastures in order to avoid overgrazing in a particular area.
#
# SCOPE, AND THE ONE THING THIS TOPIC DOES NOT SUPPLY. The framework gives two goals --
# preventing soil erosion, improving soil fertility -- two lists of practices, and one
# definition with its purpose. It gives NO MECHANISM for any practice on either list. It
# does not say that contour plowing works by ploughing across the slope, that windbreaks
# work by slowing wind, or that limestone works on soil acidity. So no key here explains
# HOW a practice works; the practices are keyed by which list they belong to and by what
# a table of measurements shows, and one item keys the absence of any mechanism or
# ranking directly.
#
# THE PRACTICE THAT APPEARS IN TWO STATEMENTS. Crop rotation is a fertility strategy
# under STB-1.E.2 here AND one of the integrated pest management methods under STB-1.C.1
# in topic 5.14. One item keys that, because a student who has met it in only one place
# will treat the other as wrong.
#
# BOUNDARY WITH 5.4 AND 5.7. The DAMAGE done by tilling, slash-and-burn and fertilizer is
# EIN-2.H in topic 5.4, and overgrazing and its results are EIN-2.I in topic 5.7, where
# rotational grazing appears as a prevention. This topic is the practice itself. No table
# here repeats one used there: 5.4 works from ploughed against untilled plots and
# fertilizer runoff, 5.7 from stocking rates and species counts, while the settings here
# are four conservation treatments on one slope, a windbreak trial, an annual against a
# perennial crop, green manure and limestone, a legume rotation, and a pasture rest
# record.
#
# NO FIGURES. Every quantitative item carries a table=; all arithmetic is recomputed in
# verify_e5_15.py from that table alone and is calculator-free.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("5.15", "Sustainable Agriculture", 5)

_T_CONTOUR = dict(
    headers=["Treatment of the field on one hillside",
             "Soil lost in one year (tonnes per hectare)"],
    rows=[["Ploughed up and down the slope, no conservation method", "32"],
          ["Contour plowing", "14"],
          ["Terracing", "6"],
          ["No-till agriculture", "4"]])

_T_WIND = dict(
    headers=["Boundary of the field",
             "Wind speed measured over the field (meters per second)",
             "Soil blown off in one year (tonnes per hectare)"],
    rows=[["Open field with no windbreak", "9", "21"],
          ["Field with a single row of trees", "6", "11"],
          ["Field with a double row of trees", "4", "5"]])

_T_PERENNIAL = dict(
    headers=["Crop grown on the plot",
             "Months of the year the soil holds living roots",
             "Soil lost in one year (tonnes per hectare)"],
    rows=[["Annual crop, replanted each spring", "5", "18"],
          ["Perennial crop, left in the ground", "12", "3"]])

_T_FERTILITY = dict(
    headers=["Treatment of the plot",
             "Soil organic matter after five years (percent)",
             "Yield in the fifth year (tonnes per hectare)"],
    rows=[["No treatment", "1.4", "2.1"],
          ["Green manure ploughed in", "2.9", "3.4"],
          ["Green manure and limestone added", "3.3", "4.0"]])

_T_ROTATE = dict(
    headers=["Sequence grown on the plot",
             "Nitrogen in the soil after six years (kilograms per hectare)",
             "Grain yield in the sixth year (tonnes per hectare)"],
    rows=[["The same grain every year", "38", "1.9"],
          ["Grain rotated with a legume", "96", "3.6"]])

_T_GRAZE = dict(
    headers=["Management of the pasture",
             "Days the livestock spend on a pasture before being moved",
             "Days a pasture rests before the livestock return",
             "Grass height when the livestock return (centimeters)"],
    rows=[["Livestock left on one pasture all season", "150", "0", "4"],
          ["Livestock moved between four pastures", "10", "30", "16"]])

QUESTIONS = [

 dict(q="What does the course framework give as the goal of soil conservation?",
      choices=[
        "To prevent soil erosion",
        "To prevent soil from holding water",
        "To raise the amount of fertilizer a crop requires",
        "To increase the number of times a field is ploughed each year",
        "To replace perennial crops with annual ones"],
      ans=0,
      why="STB-1.E.1 opens by stating that THE GOAL OF SOIL CONSERVATION IS TO PREVENT SOIL "
          "EROSION. Improving fertility is the goal of a separate statement, STB-1.E.2, and the "
          "other options name outcomes the framework never sets as a goal."),

 dict(q="Which set of practices does the framework list as methods of soil conservation?",
      choices=[
        "Contour plowing, windbreaks, perennial crops, terracing, no-till agriculture, and "
        "strip cropping",
        "Crop rotation, green manure, limestone, and rotational grazing",
        "Flood irrigation, furrow irrigation, spray irrigation, and drip irrigation",
        "Biocontrol, intercropping, natural predators, and limited chemical control",
        "Clearcutting, prescribed burning, reforestation, and wood reuse"],
      ans=0,
      why="STB-1.E.1 lists contour plowing, windbreaks, perennial crops, terracing, no-till "
          "agriculture, and strip cropping. The rejected lists are STB-1.E.2's fertility "
          "strategies, EIN-2.E.2's irrigation types, STB-1.C.1's pest management methods, and "
          "STB-1.G's forestry methods."),

 dict(q="Which of the following is NOT one of the soil conservation methods the framework "
        "names?",
      choices=[
        "Flood irrigation",
        "Contour plowing",
        "Windbreaks",
        "Terracing",
        "Strip cropping"],
      ans=0,
      why="STB-1.E.1's list is contour plowing, windbreaks, perennial crops, terracing, no-till "
          "agriculture, and strip cropping. Flood irrigation is EIN-2.E.2 and EIN-2.F.3 in the "
          "irrigation topic, where the framework attaches water loss and waterlogging to it "
          "rather than erosion control."),

 dict(q="Which strategies does the framework name for improving soil fertility?",
      choices=[
        "Crop rotation and the addition of green manure and limestone",
        "Contour plowing, terracing, and strip cropping",
        "Windbreaks, perennial crops, and no-till agriculture",
        "Rotational grazing and prescribed burning",
        "Flood irrigation and furrow irrigation"],
      ans=0,
      why="STB-1.E.2 states that strategies to improve soil fertility include CROP ROTATION AND "
          "THE ADDITION OF GREEN MANURE AND LIMESTONE. Every rejected list is drawn from "
          "STB-1.E.1's erosion methods or from other topics altogether."),

 dict(q="Which of the following is NOT one of the fertility strategies the framework names?",
      choices=[
        "Terracing",
        "Rotating the crop from year to year",
        "Ploughing in a green manure crop",
        "Adding limestone to the soil",
        "Applying green manure and limestone in the same season"],
      ans=0,
      why="STB-1.E.2 names crop rotation, green manure and limestone. Terracing sits in "
          "STB-1.E.1, whose stated goal is preventing erosion rather than improving fertility, "
          "and the framework does not move a practice between its two lists."),

 dict(q="How does the framework define rotational grazing?",
      choices=[
        "The regular rotation of livestock between different pastures",
        "The regular rotation of the crops grown on a single pasture",
        "The permanent removal of all livestock from a pasture",
        "The concentration of all livestock on the single best pasture",
        "The rotation of livestock between indoor and outdoor housing"],
      ans=0,
      why="STB-1.E.3 defines rotational grazing as THE REGULAR ROTATION OF LIVESTOCK BETWEEN "
          "DIFFERENT PASTURES. It rotates animals rather than crops, and it moves them rather "
          "than removing or concentrating them."),

 dict(q="What purpose does the framework attach to rotational grazing?",
      choices=[
        "To avoid overgrazing in a particular area",
        "To increase the number of livestock a pasture carries at one time",
        "To prevent the pasture from ever being grazed at all",
        "To improve the fertility of the soil beneath the pasture",
        "To shorten the time each pasture is left to recover"],
      ans=0,
      why="STB-1.E.3 states that livestock are rotated IN ORDER TO AVOID OVERGRAZING IN A "
          "PARTICULAR AREA. Improving fertility is the goal of STB-1.E.2's separate list, and "
          "the rejected options reverse the practice or forbid grazing altogether."),

 dict(q="Which of the following correctly separates the two goals this topic names?",
      choices=[
        "Soil conservation aims at preventing erosion; the second list of strategies aims at "
        "improving fertility",
        "Soil conservation aims at improving fertility; the second list of strategies aims "
        "at preventing erosion",
        "Both lists aim at preventing erosion, and neither concerns fertility",
        "Both lists aim at improving fertility, and neither concerns erosion",
        "The framework gives no goal for either list"],
      ans=0,
      why="STB-1.E.1 states that the goal of soil conservation is to prevent soil erosion, while "
          "STB-1.E.2 introduces its practices as strategies to IMPROVE SOIL FERTILITY. The exact "
          "swap of the two goals is the error worth guarding against."),

 dict(q="Crop rotation appears in this topic and in the framework's topic on integrated pest "
        "management. What does it do in each?",
      choices=[
        "Here it is a strategy to improve soil fertility; there it is one of the methods "
        "that make up integrated pest management",
        "Here it is one of the methods that make up integrated pest management; there it is "
        "a strategy to improve soil fertility",
        "In both places it is a method of preventing soil erosion",
        "In both places it is a way of avoiding overgrazing",
        "The framework mentions crop rotation in only one of the two topics"],
      ans=0,
      why="STB-1.E.2 lists crop rotation among the strategies to improve soil fertility, and "
          "STB-1.C.1 lists it among the biological, physical and limited chemical methods of "
          "integrated pest management. It appears in both statements, in two different roles."),

 dict(q="Four fields on one hillside were farmed differently for a year. What do the values "
        "show?",
      table=_T_CONTOUR,
      choices=[
        "Every field worked under one of the framework's conservation methods lost less soil "
        "than the field worked without one.",
        "Every field worked under one of the framework's conservation methods lost more soil "
        "than the field worked without one.",
        "The four fields lost the same amount of soil.",
        "The field worked without a conservation method lost the least soil of the four.",
        "The amount of soil lost depends only on the size of the field."],
      ans=0,
      why="The untreated field loses 32 tonnes per hectare against 14 under contour plowing, 6 "
          "under terracing and 4 under no-till agriculture. STB-1.E.1 lists all three of those "
          "as soil conservation methods and gives preventing soil erosion as their goal."),

 dict(q="Using the same four fields, how much less soil was lost under the most effective "
        "treatment than with no conservation method at all?",
      table=_T_CONTOUR,
      choices=[
        "28 tonnes per hectare less",
        "32 tonnes per hectare less",
        "36 tonnes per hectare less",
        "18 tonnes per hectare less",
        "10 tonnes per hectare less"],
      ans=0,
      why="Subtracting the two tabulated losses gives 32 minus 4, which is 28 tonnes per "
          "hectare. The rejected values quote the untreated field alone, add the two, compare "
          "the wrong pair of treatments, or take a difference within the treated fields."),

 dict(q="Three otherwise identical fields differed only in the trees along their boundary. "
        "What do the values show?",
      table=_T_WIND,
      choices=[
        "Both the wind speed over the field and the soil blown off it were lower where more "
        "trees stood along the boundary.",
        "Both the wind speed over the field and the soil blown off it were higher where more "
        "trees stood along the boundary.",
        "The wind speed fell with more trees but the soil blown off rose.",
        "The soil blown off fell with more trees but the wind speed rose.",
        "Neither reading differed between the three fields."],
      ans=0,
      why="Wind speed runs 9, 6 and 4 meters per second and soil blown off runs 21, 11 and 5 "
          "tonnes per hectare as the boundary goes from open to a single row to a double row of "
          "trees. STB-1.E.1 lists windbreaks among the soil conservation methods whose goal is "
          "preventing soil erosion."),

 dict(q="Using the same three fields, how much less soil was blown off the best sheltered "
        "field than off the open one?",
      table=_T_WIND,
      choices=[
        "16 tonnes per hectare less",
        "21 tonnes per hectare less",
        "26 tonnes per hectare less",
        "10 tonnes per hectare less",
        "5 tonnes per hectare less"],
      ans=0,
      why="Subtracting the two tabulated losses gives 21 minus 5, which is 16 tonnes per "
          "hectare. The rejected values quote the open field alone, add the two, compare the "
          "wrong pair of fields, or quote the sheltered field alone."),

 dict(q="Two plots of the same soil and slope were sown with crops of different kinds. Which "
        "conclusion do the values support?",
      table=_T_PERENNIAL,
      choices=[
        "The plot holding living roots through the whole year lost far less soil than the "
        "plot replanted each spring.",
        "The plot holding living roots through the whole year lost far more soil than the "
        "plot replanted each spring.",
        "The two plots held living roots for the same number of months.",
        "The two plots lost the same amount of soil.",
        "The plot replanted each spring held living roots for more months of the year."],
      ans=0,
      why="The perennial plot holds roots for 12 months and loses 3 tonnes per hectare, against "
          "5 months and 18 tonnes on the annual plot. STB-1.E.1 lists perennial crops among the "
          "soil conservation methods whose goal is preventing soil erosion."),

 dict(q="Using the same two plots, how much soil did the plot replanted each spring lose "
        "compared with the plot left in the ground?",
      table=_T_PERENNIAL,
      choices=[
        "Six times as much",
        "Three times as much",
        "Fifteen times as much",
        "Two times as much",
        "The same amount"],
      ans=0,
      why="Dividing the two tabulated losses gives 18 divided by 3, which is 6. The rejected "
          "values quote the perennial plot's own loss, take the difference rather than the "
          "ratio, halve the answer, or deny that the plots differ."),

 dict(q="Three plots were given different treatments and measured after five years. Which "
        "reading matches the framework's account of improving fertility?",
      table=_T_FERTILITY,
      choices=[
        "Both the organic matter in the soil and the yield rose with each of the framework's "
        "named additions.",
        "Both the organic matter in the soil and the yield fell with each of the framework's "
        "named additions.",
        "The organic matter rose but the yield fell as the additions were made.",
        "The yield rose but the organic matter fell as the additions were made.",
        "The untreated plot held the most organic matter of the three."],
      ans=0,
      why="Organic matter runs 1.4, 2.9 and 3.3 percent while yield runs 2.1, 3.4 and 4.0 tonnes "
          "per hectare across no treatment, green manure, and green manure with limestone. "
          "STB-1.E.2 names green manure and limestone among the strategies to improve soil "
          "fertility."),

 dict(q="Using the same three plots, how much greater was the fifth-year yield on the plot "
        "given both additions than on the untreated plot?",
      table=_T_FERTILITY,
      choices=[
        "1.9 tonnes per hectare greater",
        "4.0 tonnes per hectare greater",
        "6.1 tonnes per hectare greater",
        "1.3 tonnes per hectare greater",
        "0.6 tonnes per hectare greater"],
      ans=0,
      why="Subtracting the two tabulated yields gives 4.0 minus 2.1, which is 1.9 tonnes per "
          "hectare. The rejected values quote the treated plot alone, add the two, take the "
          "green manure step alone, or take the limestone step alone."),

 dict(q="Two plots were cropped for six years under different sequences. What do the values "
        "show?",
      table=_T_ROTATE,
      choices=[
        "The plot whose grain was rotated with a legume held more nitrogen and yielded more "
        "grain than the plot growing grain every year.",
        "The plot whose grain was rotated with a legume held less nitrogen and yielded less "
        "grain than the plot growing grain every year.",
        "The two plots held the same amount of nitrogen after six years.",
        "The rotated plot held more nitrogen but yielded less grain.",
        "The rotated plot yielded more grain but held less nitrogen."],
      ans=0,
      why="The rotated plot holds 96 kilograms of nitrogen per hectare against 38 and yields 3.6 "
          "tonnes per hectare against 1.9. STB-1.E.2 names crop rotation among the strategies to "
          "improve soil fertility."),

 dict(q="Using the same two plots, how much more nitrogen did the rotated plot hold after six "
        "years?",
      table=_T_ROTATE,
      choices=[
        "58 kilograms per hectare more",
        "96 kilograms per hectare more",
        "134 kilograms per hectare more",
        "38 kilograms per hectare more",
        "1.7 kilograms per hectare more"],
      ans=0,
      why="Subtracting the two tabulated amounts gives 96 minus 38, which is 58 kilograms per "
          "hectare. The rejected values quote one plot alone, add the two, or take the "
          "difference from the yield column instead."),

 dict(q="Two pastures carrying the same livestock were managed differently through one season. "
        "Which reading matches the framework's definition of rotational grazing?",
      table=_T_GRAZE,
      choices=[
        "Moving the livestock between pastures gave each pasture a rest, and the grass was "
        "taller when the livestock returned.",
        "Moving the livestock between pastures gave each pasture no rest, and the grass was "
        "shorter when the livestock returned.",
        "Leaving the livestock on one pasture all season gave that pasture the longer rest.",
        "The two managements gave each pasture the same number of rest days.",
        "The grass was the same height under both managements."],
      ans=0,
      why="Under rotation the livestock spend 10 days on a pasture and it rests 30 before they "
          "return, with the grass at 16 centimeters, against 150 days with no rest and 4 "
          "centimeters. STB-1.E.3 defines rotational grazing as the regular rotation of "
          "livestock between different pastures in order to avoid overgrazing in a "
          "particular area."),

 dict(q="Using the same two pastures, how tall was the grass on the rotated pasture compared "
        "with the pasture grazed all season?",
      table=_T_GRAZE,
      choices=[
        "Four times as tall",
        "Two times as tall",
        "Three times as tall",
        "Twelve times as tall",
        "The same height"],
      ans=0,
      why="Dividing the two tabulated heights gives 16 divided by 4, which is 4. The rejected "
          "values halve the answer, take the difference rather than the ratio, or deny that the "
          "two pastures differ."),

 dict(q="A district reports that soil is washing off its hillsides. Which of this topic's two "
        "lists supplies the response, and on what stated ground?",
      choices=[
        "The soil conservation list, because the framework gives preventing soil erosion as "
        "its goal",
        "The fertility list, because the framework gives preventing soil erosion as its goal",
        "The soil conservation list, because the framework gives improving fertility as its "
        "goal",
        "The fertility list, because the framework gives improving fertility as its goal",
        "Neither list, because the framework attaches no goal to either"],
      ans=0,
      why="STB-1.E.1 states that the goal of soil conservation is to prevent soil erosion, so "
          "soil leaving a hillside is exactly the problem that list addresses. Each rejected "
          "option pairs the wrong list with the goal or denies that goals are stated."),

 dict(q="A second district reports that its soils are yielding less each year although no soil "
        "is being lost. Which of this topic's two lists supplies the response?",
      choices=[
        "The fertility list, whose strategies are crop rotation and the addition of green "
        "manure and limestone",
        "The soil conservation list, whose methods are contour plowing, terracing and the "
        "rest",
        "Neither list, because the framework treats fertility and erosion as one problem",
        "Both lists equally, because the framework gives them the same goal",
        "Neither list, because the framework offers no strategies for fertility"],
      ans=0,
      why="STB-1.E.2 introduces crop rotation, green manure and limestone as STRATEGIES TO "
          "IMPROVE SOIL FERTILITY, which is the district's problem. The conservation list's "
          "stated goal in STB-1.E.1 is preventing erosion, which this district reports it does "
          "not have."),

 dict(q="A student writes that no-till agriculture is one of the framework's strategies for "
        "improving soil fertility. Which correction is required?",
      choices=[
        "No-till agriculture is on the soil conservation list, whose goal is preventing "
        "erosion",
        "No-till agriculture is on the fertility list, and the student is correct",
        "No-till agriculture appears on neither list in this topic",
        "No-till agriculture is the framework's definition of rotational grazing",
        "The framework gives no list of soil conservation methods at all"],
      ans=0,
      why="STB-1.E.1 names no-till agriculture among the soil conservation methods, and states "
          "that the goal of soil conservation is to prevent soil erosion. STB-1.E.2's fertility "
          "strategies are crop rotation, green manure and limestone, and no-till is not "
          "among them."),

 dict(q="A second student writes that rotational grazing means taking livestock off the land "
        "for good. Which correction is required?",
      choices=[
        "The framework describes moving livestock between pastures on a regular cycle, not "
        "removing them",
        "The framework describes removing livestock permanently, and the student is correct",
        "The framework describes moving crops rather than livestock between fields",
        "The framework describes raising the number of livestock on one pasture",
        "The framework offers no definition of rotational grazing"],
      ans=0,
      why="STB-1.E.3 defines rotational grazing as THE REGULAR ROTATION OF LIVESTOCK BETWEEN "
          "DIFFERENT PASTURES in order to avoid overgrazing in a particular area, so the animals "
          "keep grazing and only the place changes. Nothing in the statement removes them or "
          "concentrates them."),

 dict(q="Which observation would most directly show that a soil conservation method had "
        "achieved the goal the framework sets for it?",
      choices=[
        "Less soil left the treated field over the year than left an untreated field",
        "More fertilizer was applied to the treated field over the year",
        "More livestock were carried on the treated field over the year",
        "The treated field was ploughed more often over the year",
        "The treated field was sown with a wider variety of crops over the year"],
      ans=0,
      why="STB-1.E.1 sets the goal of soil conservation as preventing soil erosion, so soil "
          "leaving the field is the quantity that reports success. Fertilizer, livestock, "
          "ploughing frequency and crop variety measure other things."),

 dict(q="Which observation would most directly show that a fertility strategy had achieved the "
        "goal the framework sets for it?",
      choices=[
        "The soil grew more productive over the years the strategy was used",
        "The soil lost less material to the stream over the years the strategy was used",
        "The field was ploughed along the contour rather than up and down the slope",
        "The livestock were moved to a different pasture every month",
        "The field's boundary was planted with a double row of trees"],
      ans=0,
      why="STB-1.E.2 introduces its practices as strategies to IMPROVE SOIL FERTILITY, so a more "
          "productive soil is the outcome that reports success. Each rejected observation "
          "reports an erosion measure or names a practice from the other list."),

 dict(q="Which of the following does the framework's statement about soil conservation NOT "
        "supply?",
      choices=[
        "An explanation of how each method prevents erosion",
        "The goal that soil conservation is meant to achieve",
        "The naming of contour plowing as a method",
        "The naming of terracing as a method",
        "The naming of strip cropping as a method"],
      ans=0,
      why="STB-1.E.1 states a goal and lists six methods, and stops there. It offers no mechanism "
          "for any of them and no ranking among them, so an explanation of how each one works "
          "would be added rather than read. Each rejected option quotes something the statement "
          "does supply."),

 dict(q="How do this topic's three statements stand in relation to one another?",
      choices=[
        "One gives a goal and the methods that serve it, one gives a second goal and its own "
        "strategies, and one defines a grazing practice and the harm it avoids",
        "All three give methods for the same single goal",
        "All three define grazing practices",
        "Two give goals and the third gives neither a practice nor a purpose",
        "The three statements concern three different countries and cannot be applied "
        "together"],
      ans=0,
      why="STB-1.E.1 pairs the goal of preventing erosion with six methods, STB-1.E.2 pairs "
          "improving fertility with three strategies, and STB-1.E.3 defines rotational grazing "
          "and names avoiding overgrazing as its purpose. One farm can apply all three."),

 dict(q="Which summary states this topic as the framework does, without adding to it?",
      choices=[
        "Soil conservation aims to prevent erosion, by contour plowing, windbreaks, "
        "perennial crops, terracing, no-till agriculture and strip cropping; fertility is "
        "improved by crop rotation and by adding green manure and limestone; and rotational "
        "grazing moves livestock between pastures to avoid overgrazing in one area.",
        "Soil conservation aims to improve fertility, by adding green manure and limestone; "
        "and rotational grazing keeps livestock on one pasture all season.",
        "Soil conservation aims to prevent erosion by irrigating fields more often, and "
        "fertility is improved by ploughing more often.",
        "Soil conservation has no stated goal, and the framework lists no strategies for "
        "fertility.",
        "Rotational grazing is the only practice this topic names, and its purpose is to "
        "raise the number of livestock a pasture carries."],
      ans=0,
      why="The keyed summary carries STB-1.E.1's goal and six methods, STB-1.E.2's three "
          "fertility strategies, and STB-1.E.3's definition and purpose. Each rejected summary "
          "swaps the two goals, substitutes practices the framework never names, or denies that "
          "goals and lists are given."),
]
