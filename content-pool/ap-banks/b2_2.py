# AP BIOLOGY 2.2 Cell Size
# CED effective Fall 2025, Unit 2 Cells. Big Idea 2 Energetics.
# Learning objective 2.2.A: explain the effect of surface area to volume ratios on the
# exchange of materials between cells or organisms and the environment.
# Suggested skills 2.D, represent relationships within biological models, and 5.A,
# perform mathematical calculations including means, rates, ratios and percentages.
#
# Essential knowledge relied on, in the framework's own words:
#   2.2.A.1    Surface area to volume ratios affect the ability of a biological system
#              to obtain necessary nutrients, eliminate waste products, acquire or
#              dissipate thermal energy, and otherwise exchange chemicals and energy
#              with the environment.
#              Illustrative examples: root hairs, guard cells, gut epithelial cells,
#              cilia, stomata.
#   2.2.A.2    The surface area of the plasma membrane must be large enough to
#              adequately exchange materials.
#     i.       The surface area to volume ratio can restrict cell size and shape.
#              Smaller cells typically have a higher surface area to volume ratio as
#              well as a more efficient exchange of materials with the environment than
#              do larger cells.
#     ii.      As cells increase in volume, the surface area to volume ratio decreases
#              and the demand for internal resources increases.
#     iii.     More complex cellular structures, for example membrane folds, are
#              necessary to adequately exchange materials with the environment.
#     iv.      As organisms increase in size, their surface area to volume ratio
#              decreases, affecting properties like rate of heat exchange with the
#              environment. Smaller amounts of mass exchange proportionally more heat
#              with the ambient environment than do larger masses. As mass increases,
#              both the surface area to volume ratio and the rate of heat exchange
#              decrease.
#     v.       There is a relationship between metabolic rate per unit body mass and
#              the size of multicellular organisms; typically, the smaller the
#              organism, the higher the metabolic rate per unit body mass.
#
# ON NOTATION. The CED prints the relevant equations with exponents and a fraction.
# Biology is exported as prose with no typesetting, so every formula this bank needs is
# written out in words IN THE STEM that needs it -- "the volume of a sphere is four
# thirds times pi times the radius cubed" -- and never left to be recalled. The CED
# supplies these equations on the exam's formula sheet for the same reason.
#
# ON THE DATA. Every table is labelled in its stem, every keyed value is recomputed in
# verify_b2_2.py from the dimensions alone, and the surface areas and volumes printed
# in the tables are themselves recomputed from the side lengths, so a mistyped cell
# fails rather than ships.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: Biology is exported as prose.
TOPIC = ("2.2", "Cell Size", 2)

_T_CUBES = dict(
    headers=["Cube", "Length of one side (micrometers)",
             "Surface area (square micrometers)", "Volume (cubic micrometers)"],
    rows=[["Cube A", "1", "6", "1"],
          ["Cube B", "2", "24", "8"],
          ["Cube C", "3", "54", "27"],
          ["Cube D", "6", "216", "216"]])

_T_BOXES = dict(
    headers=["Cell model", "Length, width and height (micrometers)",
             "Surface area (square micrometers)", "Volume (cubic micrometers)"],
    rows=[["Model 1", "4 by 4 by 4", "96", "64"],
          ["Model 2", "8 by 8 by 1", "160", "64"],
          ["Model 3", "16 by 4 by 1", "168", "64"]])

_T_METABOLIC = dict(
    headers=["Animal (hypothetical)", "Body mass (grams)",
             "Metabolic rate per gram of body mass (arbitrary units)"],
    rows=[["Animal 1", "8", "62"],
          ["Animal 2", "60", "31"],
          ["Animal 3", "900", "12"],
          ["Animal 4", "20,000", "5"]])

_T_HEAT = dict(
    headers=["Sphere of tissue (hypothetical)", "Mass (grams)",
             "Heat lost per gram per minute (arbitrary units)"],
    rows=[["Sphere 1", "1", "40"],
          ["Sphere 2", "8", "20"],
          ["Sphere 3", "27", "13"],
          ["Sphere 4", "64", "10"]])

QUESTIONS = [

 dict(q="According to the course framework, surface area to volume ratios affect a "
        "biological system's ability to do which of the following?",
      choices=[
        "Obtain necessary nutrients, eliminate waste products, and acquire or dissipate "
        "thermal energy",
        "Copy its hereditary information before it divides",
        "Synthesize proteins according to messenger RNA sequences",
        "Fold and chemically modify newly synthesized proteins",
        "Store nutrients and water in a large central vacuole"],
      ans=0,
      why="EK 2.2.A.1 states that surface area to volume ratios affect the ability of a "
          "biological system to obtain necessary nutrients, eliminate waste products, "
          "acquire or dissipate thermal energy, and otherwise exchange chemicals and "
          "energy with the environment. The rejected options are organelle functions from "
          "EK 2.1.A.1, EK 2.1.A.4 and EK 2.1.A.7 i."),

 dict(q="What requirement does the course framework place on the surface area of the "
        "plasma membrane?",
      choices=[
        "It must be large enough to adequately exchange materials.",
        "It must be small enough to limit the loss of internal materials.",
        "It must be exactly equal to the volume of the cell.",
        "It must increase in proportion to the cube of the cell's diameter.",
        "It must remain constant no matter how the cell's volume changes."],
      ans=0,
      why="EK 2.2.A.2 states that the surface area of the plasma membrane must be large "
          "enough to adequately exchange materials. Surface area and volume are measured "
          "in different units, so requiring them to be equal is not a claim the framework "
          "makes or could make."),

 dict(q="How do smaller cells compare with larger cells, according to the course "
        "framework?",
      choices=[
        "They typically have a higher surface area to volume ratio and exchange materials "
        "with the environment more efficiently.",
        "They typically have a lower surface area to volume ratio and exchange materials "
        "more efficiently.",
        "They typically have a higher surface area to volume ratio but exchange materials "
        "less efficiently.",
        "They typically have the same surface area to volume ratio, since ratios do not "
        "depend on size.",
        "They typically have a lower surface area to volume ratio and exchange materials "
        "less efficiently."],
      ans=0,
      why="EK 2.2.A.2 i states that smaller cells typically have a higher surface area to "
          "volume ratio as well as a more efficient exchange of materials with the "
          "environment than do larger cells. Both halves move together in that sentence, "
          "so the options that split them contradict it."),

 dict(q="What does the course framework say happens as cells increase in volume?",
      choices=[
        "The surface area to volume ratio decreases and the demand for internal resources "
        "increases.",
        "The surface area to volume ratio increases and the demand for internal resources "
        "decreases.",
        "Both the surface area to volume ratio and the demand for internal resources "
        "increase.",
        "Both the surface area to volume ratio and the demand for internal resources "
        "decrease.",
        "Neither the surface area to volume ratio nor the demand for internal resources "
        "changes."],
      ans=0,
      why="EK 2.2.A.2 ii states that as cells increase in volume the surface area to "
          "volume ratio decreases and the demand for internal resources increases. The "
          "two move in opposite directions, which is what makes large size a problem for "
          "exchange."),

 dict(q="What example does the course framework give of a more complex cellular structure "
        "that is necessary for adequate exchange with the environment?",
      choices=["Membrane folds", "A double helix", "A peptide bond",
               "A saturated fatty acid tail", "A ribosome"],
      ans=0,
      why="EK 2.2.A.2 iii states that more complex cellular structures, for example "
          "membrane folds, are necessary to adequately exchange materials with the "
          "environment. The rejected options are structures the framework introduces in "
          "Unit 1 and in EK 2.1.A.1, none of them offered as an exchange structure."),

 dict(q="As organisms increase in size, which property does the course framework say is "
        "affected by their falling surface area to volume ratio?",
      choices=[
        "The rate of heat exchange with the environment",
        "The sequence of amino acids in their proteins",
        "The number of nitrogenous bases in their DNA",
        "The kind of bond joining one monomer to the next",
        "The number of membranes surrounding their mitochondria"],
      ans=0,
      why="EK 2.2.A.2 iv states that as organisms increase in size their surface area to "
          "volume ratio decreases, affecting properties like rate of heat exchange with "
          "the environment. The rejected options name molecular features the framework "
          "never makes a function of body size."),

 dict(q="How do small and large masses compare in the heat they exchange with the "
        "surrounding environment?",
      choices=[
        "Smaller amounts of mass exchange proportionally more heat than larger masses do.",
        "Smaller amounts of mass exchange proportionally less heat than larger masses do.",
        "Small and large masses exchange heat at the same proportional rate.",
        "Larger masses exchange heat proportionally more because they contain more "
        "material.",
        "Mass has no bearing on the rate of heat exchange with the environment."],
      ans=0,
      why="EK 2.2.A.2 iv states that smaller amounts of mass exchange proportionally more "
          "heat with the ambient environment than do larger masses, and that as mass "
          "increases both the surface area to volume ratio and the rate of heat exchange "
          "decrease."),

 dict(q="What relationship does the course framework describe between the size of a "
        "multicellular organism and its metabolic rate per unit body mass?",
      choices=[
        "Typically, the smaller the organism, the higher the metabolic rate per unit body "
        "mass.",
        "Typically, the smaller the organism, the lower the metabolic rate per unit body "
        "mass.",
        "Metabolic rate per unit body mass is the same in organisms of every size.",
        "Metabolic rate per unit body mass depends only on the organism's diet, not its "
        "size.",
        "Typically, the larger the organism, the higher the metabolic rate per unit body "
        "mass."],
      ans=0,
      why="EK 2.2.A.2 v states that there is a relationship between metabolic rate per "
          "unit body mass and the size of multicellular organisms, and that typically the "
          "smaller the organism, the higher the metabolic rate per unit body mass."),

 dict(q="Which of the following is offered by the course framework as an illustrative "
        "example of surface area to volume ratios and exchanges?",
      choices=["Root hairs", "Lysosomes", "Peptide bonds", "Nitrogenous bases",
               "The Golgi complex"],
      ans=0,
      why="The illustrative examples printed with EK 2.2.A.1 are root hairs, guard cells "
          "and gut epithelial cells, together with cilia and stomata. Lysosomes and the "
          "Golgi are organelles under EK 2.1.A.6 and EK 2.1.A.4, and the other two are "
          "Unit 1 molecular features."),

 dict(q="The table gives the side length, surface area and volume of four cubes. Which "
        "cube has the greatest surface area to volume ratio?",
      table=_T_CUBES,
      choices=["Cube A", "Cube B", "Cube C", "Cube D",
               "All four cubes have the same ratio."],
      ans=0,
      why="Dividing the surface area column by the volume column gives the ratio for each "
          "cube, and the smallest cube gives the largest value. EK 2.2.A.2 i is the "
          "general statement that smaller means a higher surface area to volume ratio."),

 dict(q="For the cube in the table whose sides are 3 micrometers long, what is the "
        "surface area to volume ratio?",
      table=_T_CUBES,
      choices=["2 to 1", "1 to 2", "3 to 1", "6 to 1", "27 to 54"],
      ans=0,
      why="Dividing that row's surface area by its volume gives the ratio directly from "
          "the table. The inverted option is volume over surface area and the 6 to 1 "
          "option is the ratio of the smallest cube in the same table."),

 dict(q="What happens to the surface area to volume ratio of a cube as the length of its "
        "side increases, according to the values in the table?",
      table=_T_CUBES,
      choices=[
        "It decreases as the side length increases.",
        "It increases as the side length increases.",
        "It stays the same at every side length.",
        "It increases and then decreases as the side length increases.",
        "It cannot be determined from the values shown."],
      ans=0,
      why="Computing surface area over volume for each of the four rows gives a strictly "
          "falling sequence as the side length rises. That is the arithmetic behind EK "
          "2.2.A.2 ii, which states that the ratio decreases as cells increase in volume."),

 dict(q="If each cube in the table were a model of a cell, which would exchange materials "
        "with its environment most efficiently for each unit of its volume?",
      table=_T_CUBES,
      choices=["Cube A", "Cube B", "Cube C", "Cube D",
               "All four would exchange equally efficiently."],
      ans=0,
      why="EK 2.2.A.2 i ties a higher surface area to volume ratio to a more efficient "
          "exchange of materials with the environment, and the ratio computed from the "
          "table is largest for the smallest cube. The four ratios differ, so the option "
          "saying all are equal is false."),

 dict(q="The table describes three box-shaped cell models that all enclose the same "
        "volume. Which model has the greatest surface area to volume ratio?",
      table=_T_BOXES,
      choices=["Model 3", "Model 1", "Model 2",
               "All three have the same ratio, because their volumes are equal.",
               "The ratios cannot be compared, because the shapes differ."],
      ans=0,
      why="With the volume column identical across the three rows, the largest surface "
          "area is also the largest ratio. Equal volume therefore does not force equal "
          "ratio, which is the point EK 2.2.A.2 i makes when it says the ratio can "
          "restrict cell shape as well as cell size."),

 dict(q="What do the three box-shaped models in the table show about the effect of shape "
        "on exchange with the environment?",
      table=_T_BOXES,
      choices=[
        "Flattening or elongating a cell raises its surface area to volume ratio without "
        "changing its volume.",
        "Flattening or elongating a cell lowers its surface area to volume ratio without "
        "changing its volume.",
        "Shape has no effect on the surface area to volume ratio once volume is fixed.",
        "Only a cube shape can achieve a high surface area to volume ratio.",
        "Changing shape necessarily changes the volume enclosed."],
      ans=0,
      why="All three rows enclose the same volume, and the flatter and longer models "
          "carry larger surface areas and therefore larger ratios. EK 2.2.A.2 i states "
          "that the surface area to volume ratio can restrict cell size and shape, which "
          "is why shape is a variable at all."),

 dict(q="A spherical cell has a radius of 3 micrometers. Taking the surface area of a "
        "sphere as four times pi times the radius squared, and the volume as four thirds "
        "times pi times the radius cubed, what is its surface area to volume ratio?",
      choices=["1 to 1", "3 to 1", "1 to 3", "4 to 3", "9 to 1"],
      ans=0,
      why="Dividing the surface area expression by the volume expression cancels pi and "
          "leaves three divided by the radius, which for a radius of 3 micrometers is 1. "
          "The 3 to 1 option is that expression with the radius omitted."),

 dict(q="A cube-shaped cell model doubles the length of every side. What happens to its "
        "surface area, its volume, and its surface area to volume ratio?",
      choices=[
        "Surface area is multiplied by four, volume by eight, and the ratio is halved.",
        "Surface area is multiplied by eight, volume by four, and the ratio is doubled.",
        "Surface area, volume and the ratio are all doubled.",
        "Surface area is multiplied by two, volume by four, and the ratio is halved.",
        "Surface area and volume both double, so the ratio is unchanged."],
      ans=0,
      why="Surface area of a cube goes with the square of the side and volume with the "
          "cube of the side, so doubling the side multiplies them by four and by eight "
          "and divides the ratio by two. That arithmetic is what EK 2.2.A.2 ii states "
          "qualitatively when it says the ratio decreases as volume increases."),

 dict(q="Four hypothetical animals of different sizes were measured for metabolic rate "
        "per gram of body mass, with the results in the table. Which conclusion is best "
        "supported?",
      table=_T_METABOLIC,
      choices=[
        "The smaller the animal, the higher its metabolic rate per gram of body mass.",
        "The smaller the animal, the lower its metabolic rate per gram of body mass.",
        "Metabolic rate per gram of body mass was the same in all four animals.",
        "Metabolic rate per gram of body mass rose and then fell as body mass increased.",
        "Body mass and metabolic rate per gram were unrelated in these animals."],
      ans=0,
      why="Ranking the four rows by body mass gives the reverse of the ranking by "
          "metabolic rate per gram. EK 2.2.A.2 v states that typically the smaller the "
          "organism, the higher the metabolic rate per unit body mass."),

 dict(q="Using the same measurements, how many times as great is the metabolic rate per "
        "gram of the lightest animal compared with the heaviest?",
      table=_T_METABOLIC,
      choices=["About twelve times as great", "About twice as great",
               "About half as great", "About sixty times as great",
               "Almost exactly the same"],
      ans=0,
      why="Dividing the metabolic rate per gram of the lightest row by that of the "
          "heaviest gives the comparison directly from the table. The sixty option is the "
          "lightest animal's rate reported on its own rather than as a ratio."),

 dict(q="Four spheres of tissue differing only in mass were measured for heat lost per "
        "gram per minute, with the results in the table. Which conclusion is best "
        "supported?",
      table=_T_HEAT,
      choices=[
        "As mass increased, the heat lost per gram per minute decreased.",
        "As mass increased, the heat lost per gram per minute increased.",
        "Heat lost per gram per minute was the same at every mass.",
        "The heaviest sphere lost the most heat per gram per minute.",
        "Mass and heat loss per gram were unrelated in these spheres."],
      ans=0,
      why="Heat lost per gram falls at every step as mass rises across the four spheres. "
          "EK 2.2.A.2 iv states that as mass increases both the surface area to volume "
          "ratio and the rate of heat exchange decrease."),

 dict(q="A fifth sphere of tissue with a mass of 125 grams is prepared under the same "
        "conditions as those in the heat table. What is the best prediction for its heat "
        "loss per gram per minute?",
      table=_T_HEAT,
      choices=[
        "Lower than the value recorded for any sphere in the table",
        "Higher than the value recorded for any sphere in the table",
        "Equal to the value recorded for the lightest sphere",
        "Between the values recorded for the two lightest spheres",
        "Impossible to predict, because heat loss does not depend on mass"],
      ans=0,
      why="The tabulated values fall at every step as mass rises, and the new sphere is "
          "heavier than every row shown, so the trend extrapolates below the smallest "
          "value. EK 2.2.A.2 iv supplies the reason the trend is expected to continue "
          "rather than reverse."),

 dict(q="A cell grows so that its volume increases substantially while its shape stays "
        "the same. Which pair of consequences does the course framework predict?",
      choices=[
        "Its surface area to volume ratio falls, and its demand for internal resources "
        "rises.",
        "Its surface area to volume ratio rises, and its demand for internal resources "
        "falls.",
        "Its surface area to volume ratio and its demand for internal resources both "
        "rise.",
        "Its surface area to volume ratio and its demand for internal resources both "
        "fall.",
        "Neither its surface area to volume ratio nor its demand for internal resources "
        "changes."],
      ans=0,
      why="EK 2.2.A.2 ii states that as cells increase in volume the surface area to "
          "volume ratio decreases and the demand for internal resources increases. Those "
          "are the two halves of one sentence, and they move in opposite directions."),

 dict(q="Why does a very large cell have difficulty supplying its interior, according to "
        "the course framework?",
      choices=[
        "Its membrane surface area has not kept pace with its volume, so exchange with "
        "the environment is inadequate for the amount of interior it must supply.",
        "Its membrane surface area has grown faster than its volume, so materials leave "
        "faster than they enter.",
        "Large cells contain no plasma membrane through which exchange could occur.",
        "Large cells have a higher surface area to volume ratio than small ones and so "
        "lose materials too quickly.",
        "Large cells cannot carry out any exchange with the environment at all."],
      ans=0,
      why="EK 2.2.A.2 requires the plasma membrane's surface area to be large enough to "
          "adequately exchange materials, and EK 2.2.A.2 ii states that the ratio falls "
          "and the demand for internal resources rises as volume grows. Larger cells have "
          "a lower ratio, not a higher one, under EK 2.2.A.2 i."),

 dict(q="Which change would most increase a cell's capacity to exchange materials with "
        "its environment without a comparable increase in its volume?",
      choices=[
        "Adding folds to its plasma membrane",
        "Increasing the length of every side by the same factor",
        "Filling more of its interior with stored material",
        "Reducing the number of proteins embedded in its membrane",
        "Becoming more nearly spherical while keeping the same volume"],
      ans=0,
      why="EK 2.2.A.2 iii names membrane folds as an example of the more complex cellular "
          "structures necessary to adequately exchange materials with the environment. "
          "Scaling every side up raises volume faster than surface area under EK 2.2.A.2 "
          "ii, and a sphere is the shape with the least surface area for a given volume."),

 dict(q="Two animals of the same shape but very different masses are placed in the same "
        "cold room. Which prediction follows from the course framework?",
      choices=[
        "The smaller animal will lose proportionally more heat to the room than the "
        "larger one.",
        "The larger animal will lose proportionally more heat to the room than the "
        "smaller one.",
        "Both will lose heat at the same proportional rate, since the room is the same.",
        "Neither will exchange heat with the room, because heat exchange depends only on "
        "diet.",
        "The smaller animal will gain heat from the room while the larger loses it."],
      ans=0,
      why="EK 2.2.A.2 iv states that smaller amounts of mass exchange proportionally more "
          "heat with the ambient environment than do larger masses, and that as mass "
          "increases both the surface area to volume ratio and the rate of heat exchange "
          "decrease."),

 dict(q="Two cells enclose exactly the same volume, but one is a compact sphere and the "
        "other is long and thin. Which statement about them is best supported?",
      choices=[
        "The long thin cell has the greater surface area to volume ratio and can exchange "
        "materials more efficiently.",
        "The compact spherical cell has the greater surface area to volume ratio and can "
        "exchange materials more efficiently.",
        "Their surface area to volume ratios must be equal, because their volumes are "
        "equal.",
        "Their surface area to volume ratios cannot be compared unless their masses are "
        "also equal.",
        "Neither cell can exchange materials, because exchange depends on volume alone."],
      ans=0,
      why="EK 2.2.A.2 i states that the surface area to volume ratio can restrict cell "
          "size and shape and ties a higher ratio to more efficient exchange. Equal "
          "volumes do not force equal ratios, as the three equal-volume box models in "
          "this topic's own data show."),

 dict(q="A student wants to test the claim that smaller objects exchange materials with "
        "their surroundings more efficiently. Which design is best?",
      choices=[
        "Soak cubes of the same material cut to several different side lengths in the "
        "same solution for the same time, then measure how far the solution penetrated as "
        "a fraction of each cube.",
        "Soak cubes of several different materials, each a different size, in different "
        "solutions for different times.",
        "Soak a single large cube in a solution and report whether the solution reached "
        "its centre.",
        "Weigh cubes of several different side lengths without placing any of them in "
        "solution.",
        "Measure the surface area of several cubes and calculate their volumes without "
        "any soaking step."],
      ans=0,
      why="The claim is about the effect of size, so size must be the only difference "
          "between the treatments while material, solution and time are held constant, "
          "and the outcome must be measured relative to each object's own size. A single "
          "object supplies no comparison, and calculating ratios alone tests no exchange."),

 dict(q="A student states that a larger cell must have a higher surface area to volume "
        "ratio because it has more membrane in total. What is the best correction?",
      choices=[
        "The ratio compares surface area with volume, and volume grows faster than "
        "surface area as a cell enlarges, so the ratio falls.",
        "The ratio compares surface area with volume, and surface area grows faster than "
        "volume as a cell enlarges, so the ratio rises.",
        "A larger cell has less membrane in total, which is why its ratio falls.",
        "The ratio does not depend on the size of the cell at all.",
        "The student is correct, because more membrane always means a higher ratio."],
      ans=0,
      why="Having more membrane in total is consistent with having less membrane per unit "
          "of volume, which is what the ratio measures. EK 2.2.A.2 ii states that as "
          "cells increase in volume the surface area to volume ratio decreases, and the "
          "cube arithmetic in this topic shows why."),

 dict(q="A cube-shaped cell model has sides 4 micrometers long. Taking the surface area "
        "of a cube as six times the side length squared and the volume as the side length "
        "cubed, what is its surface area to volume ratio?",
      choices=["1.5 to 1", "1 to 1.5", "4 to 1", "6 to 1", "2 to 1"],
      ans=0,
      why="Dividing six times the side squared by the side cubed leaves six divided by "
          "the side length, which for a side of 4 micrometers is 1.5. The 6 to 1 option "
          "is that expression with the side length omitted, which is the ratio only for a "
          "side of 1 micrometer."),

 dict(q="Which statement best expresses why the course framework treats the surface area "
        "to volume ratio as a limit on how large a cell can be?",
      choices=[
        "The ratio can restrict cell size and shape, because the membrane must stay large "
        "enough relative to the interior it serves.",
        "The ratio can restrict cell size and shape, because a cell's volume cannot "
        "exceed its surface area.",
        "The ratio sets no limit on size, since a cell can always add more membrane "
        "folds.",
        "The ratio limits only the shape of a cell and never its size.",
        "The ratio limits only the size of an organism and never the size of a cell."],
      ans=0,
      why="EK 2.2.A.2 i states that the surface area to volume ratio can restrict cell "
          "size and shape, and EK 2.2.A.2 requires the plasma membrane's surface area to "
          "be large enough to adequately exchange materials. Comparing a volume with an "
          "area as if they were the same kind of quantity is not a claim the framework "
          "makes."),
]
