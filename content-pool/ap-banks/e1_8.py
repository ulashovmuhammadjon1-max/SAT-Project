# AP ENVIRONMENTAL SCIENCE 1.8 Primary Productivity
# CED effective Fall 2026, Unit 1 The Living World: Ecosystems.
# Enduring understanding ENG-1: Energy can be converted from one form to another.
# Learning objective ENG-1.A: explain how solar energy is acquired and transferred by
# living organisms. Suggested skill 1.A.
#
# Essential knowledge relied on, in the framework's own words:
#   ENG-1.A.1  Primary productivity is the rate at which solar energy (sunlight) is
#              converted into organic compounds via photosynthesis over a unit of time.
#   ENG-1.A.2  Gross primary productivity is the total rate of photosynthesis in a given
#              area.
#   ENG-1.A.3  Net primary productivity is the rate of energy storage by photosynthesizers
#              in a given area, after subtracting the energy lost to respiration.
#   ENG-1.A.4  Productivity is measured in units of energy per unit area per unit time
#              (for example, kilocalories per square meter per year).
#   ENG-1.A.5  Most red light is absorbed in the upper one meter of water, and blue light
#              only penetrates deeper than one hundred meters in the clearest water. This
#              affects photosynthesis in aquatic ecosystems, whose photosynthesizers have
#              adapted mechanisms to address the lack of visible light.
#
# THE ARITHMETIC IS REAL AND IS RECOMPUTED. ENG-1.A.3 makes net primary productivity the
# gross rate less the energy lost to respiration, which is a subtraction. Every item that
# performs it is recomputed from the table alone in verify_e1_8.py, and every quantity is
# chosen so the arithmetic can be done without a calculator.
#
# THE UNITS ARE WRITTEN OUT. ENG-1.A.4's example is printed in the CED as a slash
# expression; export_units.py does not typeset this subject, so it is written here as
# "kilocalories per square meter per year" throughout.
#
# HOW THIS TOPIC IS KEPT DISTINCT FROM 1.9, 1.10 AND 1.11. Nothing here concerns trophic
# levels, the ten percent rule, or food chains; those are ENG-1.B, ENG-1.C and ENG-1.D.
# The light items rest on ENG-1.A.5 and concern light and DEPTH in water, which is not
# the turbidity factor of ERT-1.C.3 asked in topic 1.3.
#
# NO FIGURES ARE REFERENCED. Productivity data are given as tables.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: export_units.py does not typeset
# Environmental Science.
TOPIC = ("1.8", "Primary Productivity", 1)

_T_GPPNPP = dict(
    headers=["Ecosystem", "Gross primary productivity (kilocalories per square meter per year)",
             "Energy lost to respiration (kilocalories per square meter per year)"],
    rows=[["Ecosystem 1", "9000", "6000"],
          ["Ecosystem 2", "5000", "1000"],
          ["Ecosystem 3", "2000", "1200"],
          ["Ecosystem 4", "800", "200"]])

_T_ONEPLOT = dict(
    headers=["Quantity measured in one meadow",
             "Value (kilocalories per square meter per year)"],
    rows=[["Gross primary productivity", "7500"],
          ["Energy lost to respiration by the producers", "2500"]])

_T_LIGHT = dict(
    headers=["Depth in clear ocean water (meters)",
             "Percent of surface red light still present",
             "Percent of surface blue light still present"],
    rows=[["1", "3", "88"],
          ["10", "0", "62"],
          ["50", "0", "27"],
          ["100", "0", "6"]])

_T_AREA = dict(
    headers=["Ecosystem type", "Net primary productivity (kilocalories per square meter per year)",
             "Area of the Earth covered (millions of square kilometers)"],
    rows=[["Open ocean", "500", "332"],
          ["Tropical rainforest", "9000", "17"],
          ["Desert", "300", "42"]])

_T_YEARS = dict(
    headers=["Year in one forest",
             "Gross primary productivity (kilocalories per square meter per year)",
             "Energy lost to respiration (kilocalories per square meter per year)"],
    rows=[["Year 1", "6000", "2000"],
          ["Year 2", "6000", "3000"],
          ["Year 3", "6000", "4500"]])

_T_DEPTHPROD = dict(
    headers=["Depth band in a lake (meters)",
             "Net primary productivity (kilocalories per square meter per year)"],
    rows=[["0 to 5", "1800"],
          ["5 to 20", "900"],
          ["20 to 50", "120"],
          ["50 to 80", "5"]])

_T_HARVEST = dict(
    headers=["Grassland plot", "Energy in plant tissue at the start of the year "
                               "(kilocalories per square meter)",
             "Energy in plant tissue at the end of the year (kilocalories per square meter)"],
    rows=[["Plot 1", "400", "1600"],
          ["Plot 2", "400", "900"]])

_T_PIGMENT = dict(
    headers=["Alga", "Depth at which it is most abundant (meters)",
             "Color of light its pigments absorb best"],
    rows=[["Alga 1", "1", "Red"],
          ["Alga 2", "40", "Blue"]])

QUESTIONS = [

 dict(q="Which statement best defines primary productivity as the framework states it?",
      choices=[
        "It is the rate at which solar energy is converted into organic compounds by "
        "photosynthesis over a unit of time.",
        "It is the total mass of organic compounds present in an ecosystem at one "
        "instant.",
        "It is the rate at which organic compounds are broken down by consumers.",
        "It is the amount of sunlight that strikes an ecosystem in a year.",
        "It is the number of producer species living in a given area."],
      ans=0,
      why="ENG-1.A.1 states that primary productivity is the rate at which solar energy "
          "is converted into organic compounds via photosynthesis over a unit of time. It "
          "is a rate, not a standing quantity, and the conversion is by photosynthesis."),

 dict(q="What does the framework mean by gross primary productivity?",
      choices=[
        "The total rate of photosynthesis in a given area.",
        "The rate of photosynthesis remaining after respiration is subtracted.",
        "The total mass of producers living in a given area.",
        "The rate at which consumers eat producers in a given area.",
        "The total sunlight falling on a given area."],
      ans=0,
      why="ENG-1.A.2 states that gross primary productivity is the total rate of "
          "photosynthesis in a given area. The subtraction of respiration belongs to net "
          "primary productivity under ENG-1.A.3, not to the gross figure."),

 dict(q="What does the framework mean by net primary productivity?",
      choices=[
        "The rate of energy storage by photosynthesizers in a given area after "
        "subtracting the energy lost to respiration.",
        "The total rate of photosynthesis in a given area before any subtraction.",
        "The rate at which energy is lost to respiration in a given area.",
        "The total energy contained in an ecosystem at one instant.",
        "The rate at which sunlight arrives at a given area."],
      ans=0,
      why="ENG-1.A.3 states that net primary productivity is the rate of energy storage by "
          "photosynthesizers in a given area, after subtracting the energy lost to "
          "respiration."),

 dict(q="In what kind of units does the framework say productivity is measured?",
      choices=[
        "Energy per unit area per unit time.",
        "Energy per unit area only.",
        "Mass per organism only.",
        "Energy per organism per unit time.",
        "Area per unit time."],
      ans=0,
      why="ENG-1.A.4 states that productivity is measured in units of energy per unit area "
          "per unit time, and gives kilocalories per square meter per year as its example."),

 dict(q="The table gives gross primary productivity and respiration for four ecosystems. "
        "Which ecosystem has the highest net primary productivity?",
      table=_T_GPPNPP,
      choices=[
        "Ecosystem 2, at four thousand kilocalories per square meter per year.",
        "Ecosystem 1, at nine thousand kilocalories per square meter per year.",
        "Ecosystem 1, at three thousand kilocalories per square meter per year.",
        "Ecosystem 3, at eight hundred kilocalories per square meter per year.",
        "Ecosystem 4, at six hundred kilocalories per square meter per year."],
      ans=0,
      why="ENG-1.A.3 makes net primary productivity the gross rate less the energy lost to "
          "respiration, so each ecosystem's net value is the difference of its two "
          "tabulated columns, and the largest of those differences identifies the answer."),

 dict(q="Using the same table, which ecosystem loses the largest share of its gross "
        "primary productivity to respiration?",
      table=_T_GPPNPP,
      choices=[
        "Ecosystem 1, which loses two thirds of its gross productivity.",
        "Ecosystem 2, which loses one fifth of its gross productivity.",
        "Ecosystem 3, which loses one tenth of its gross productivity.",
        "Ecosystem 4, which loses three quarters of its gross productivity.",
        "All four lose the same share of their gross productivity."],
      ans=0,
      why="The share lost is respiration divided by gross primary productivity, computed "
          "for each row of the table. ENG-1.A.2 and ENG-1.A.3 make those two columns the "
          "gross rate and the loss subtracted from it."),

 dict(q="One meadow was measured as shown. What is its net primary productivity?",
      table=_T_ONEPLOT,
      choices=[
        "Five thousand kilocalories per square meter per year.",
        "Ten thousand kilocalories per square meter per year.",
        "Two thousand five hundred kilocalories per square meter per year.",
        "Seven thousand five hundred kilocalories per square meter per year.",
        "Three kilocalories per square meter per year."],
      ans=0,
      why="ENG-1.A.3 defines net primary productivity as the rate of energy storage after "
          "subtracting the energy lost to respiration, so the answer is the difference "
          "between the two tabulated values rather than their sum or their ratio."),

 dict(q="Which relationship between gross and net primary productivity does the framework "
        "support?",
      choices=[
        "Net primary productivity is smaller than gross primary productivity whenever "
        "producers respire at all.",
        "Net primary productivity is larger than gross primary productivity whenever "
        "producers respire at all.",
        "Net and gross primary productivity are always equal.",
        "Net primary productivity is gross primary productivity plus the energy lost to "
        "respiration.",
        "Gross primary productivity is net primary productivity minus the energy lost to "
        "respiration."],
      ans=0,
      why="ENG-1.A.3 obtains the net figure by subtracting the energy lost to respiration "
          "from the gross rate of ENG-1.A.2, so any respiration at all makes the net "
          "figure the smaller of the two."),

 dict(q="What does the framework say about red light in water?",
      choices=[
        "Most of it is absorbed in the upper one meter.",
        "It penetrates deeper than any other color of light.",
        "It reaches beyond one hundred meters in the clearest water.",
        "It is not absorbed by water at any depth.",
        "It is the only color of light that reaches aquatic photosynthesizers."],
      ans=0,
      why="ENG-1.A.5 states that most red light is absorbed in the upper one meter of "
          "water, which is what distinguishes it from blue light in the same sentence."),

 dict(q="What does the framework say about blue light in water?",
      choices=[
        "It penetrates deeper than one hundred meters only in the clearest water.",
        "It penetrates deeper than one hundred meters in all water.",
        "It is absorbed within the upper one meter of all water.",
        "It never reaches any aquatic photosynthesizer.",
        "It penetrates the same depth as red light."],
      ans=0,
      why="ENG-1.A.5 states that blue light only penetrates deeper than one hundred meters "
          "in the clearest water, so both the depth and the qualification about clarity "
          "are part of the claim."),

 dict(q="What consequence does the framework draw from the way light behaves in water?",
      choices=[
        "It affects photosynthesis in aquatic ecosystems, whose photosynthesizers have "
        "adapted mechanisms to address the lack of visible light.",
        "It prevents photosynthesis from occurring anywhere in water.",
        "It makes aquatic photosynthesis independent of depth.",
        "It causes aquatic photosynthesizers to stop using light altogether.",
        "It makes red light the deepest-penetrating color in every water body."],
      ans=0,
      why="ENG-1.A.5 states that the behavior of red and blue light in water affects "
          "photosynthesis in aquatic ecosystems, whose photosynthesizers have adapted "
          "mechanisms to address the lack of visible light."),

 dict(q="The table shows how much of each color of surface light remains at four depths "
        "in clear ocean water. Which conclusion is best supported?",
      table=_T_LIGHT,
      choices=[
        "Red light is essentially gone within the first few meters, while blue light "
        "persists to far greater depth.",
        "Blue light is essentially gone within the first few meters, while red light "
        "persists to far greater depth.",
        "Both colors persist equally at all four depths.",
        "Red light is still present at one hundred meters in the same proportion as at "
        "one meter.",
        "Neither color is present at any depth below one meter."],
      ans=0,
      why="The red column falls to zero by ten meters while the blue column is still "
          "measurable at one hundred meters. ENG-1.A.5 states that most red light is "
          "absorbed in the upper one meter and that blue light penetrates deeper than one "
          "hundred meters only in the clearest water."),

 dict(q="Three ecosystem types are compared as shown. Which statement about the open "
        "ocean is best supported?",
      table=_T_AREA,
      choices=[
        "It has a low net primary productivity per square meter but covers by far the "
        "largest area of the three.",
        "It has the highest net primary productivity per square meter of the three.",
        "It covers the smallest area of the three.",
        "It has both the highest productivity per square meter and the largest area.",
        "It has the same productivity per square meter as tropical rainforest."],
      ans=0,
      why="The open ocean carries the lower of the two productivity extremes per square "
          "meter yet the largest tabulated area. ENG-1.A.4 makes productivity a rate per "
          "unit area, so a rate per unit area and a total for a whole ecosystem type are "
          "different quantities."),

 dict(q="Using the same table, which ecosystem type delivers the largest total net primary "
        "productivity across all the area it covers?",
      table=_T_AREA,
      choices=[
        "The open ocean, because its area is large enough to outweigh its low rate per "
        "square meter.",
        "Tropical rainforest, because its rate per square meter is the highest.",
        "Desert, because it covers more area than tropical rainforest.",
        "All three deliver the same total, because rate and area trade off exactly.",
        "The total cannot be compared, because productivity is a rate."],
      ans=0,
      why="Multiplying each tabulated rate by its tabulated area gives a total for each "
          "type, and the products are what the comparison rests on. ENG-1.A.4 makes "
          "productivity energy per unit area per unit time, so a total requires the area "
          "as well as the rate."),

 dict(q="Gross primary productivity and respiration were followed in one forest over three "
        "years, as shown. What happened to net primary productivity?",
      table=_T_YEARS,
      choices=[
        "It fell each year, because respiration rose while gross primary productivity "
        "stayed the same.",
        "It rose each year, because respiration rose while gross primary productivity "
        "stayed the same.",
        "It stayed the same each year, because gross primary productivity did not change.",
        "It fell each year, because gross primary productivity fell.",
        "It cannot be determined, because net primary productivity was not measured "
        "directly."],
      ans=0,
      why="ENG-1.A.3 makes the net figure the gross rate less the energy lost to "
          "respiration, so with the gross column constant and the respiration column "
          "rising, the difference must shrink each year."),

 dict(q="Net primary productivity was measured in four depth bands of one lake, as shown. "
        "Which conclusion is best supported?",
      table=_T_DEPTHPROD,
      choices=[
        "Productivity falls steeply with depth, which is consistent with less visible "
        "light reaching the deeper water.",
        "Productivity rises steeply with depth.",
        "Productivity is the same in every depth band.",
        "The deepest band is the most productive of the four.",
        "The shallowest band is the least productive of the four."],
      ans=0,
      why="Productivity falls at every step down the depth column. ENG-1.A.5 states that "
          "light is absorbed with depth in water and that this affects photosynthesis in "
          "aquatic ecosystems."),

 dict(q="Two grassland plots were measured at the start and end of one year, as shown. "
        "Which statement about their net primary productivity is best supported?",
      table=_T_HARVEST,
      choices=[
        "The plot whose plant tissue gained more energy over the year had the higher net "
        "primary productivity.",
        "The plot whose plant tissue gained less energy over the year had the higher net "
        "primary productivity.",
        "The two plots had the same net primary productivity, because they started with "
        "the same energy.",
        "Neither plot had any net primary productivity, because both retained some "
        "starting tissue.",
        "Net primary productivity cannot be compared without knowing the number of "
        "species present."],
      ans=0,
      why="ENG-1.A.3 makes net primary productivity the rate of energy storage by "
          "photosynthesizers after respiration is subtracted, so energy actually "
          "accumulated in plant tissue over a year is what that rate produces."),

 dict(q="A student writes that net primary productivity equals gross primary productivity "
        "plus the energy lost to respiration. What is the best correction?",
      choices=[
        "The energy lost to respiration is subtracted from the gross figure, not added to "
        "it.",
        "The energy lost to respiration is added to the net figure to give the gross "
        "figure, so the student has it right.",
        "Gross primary productivity already excludes respiration, so no operation is "
        "needed.",
        "Net primary productivity is a mass and gross primary productivity is a rate, so "
        "they cannot be combined.",
        "Respiration has no effect on either figure."],
      ans=0,
      why="ENG-1.A.3 states that net primary productivity is the rate of energy storage "
          "AFTER SUBTRACTING the energy lost to respiration, so the student has reversed "
          "the operation."),

 dict(q="Which of the following is a valid set of units for productivity as the framework "
        "describes it?",
      choices=[
        "Kilocalories per square meter per year.",
        "Kilocalories only.",
        "Square meters per year.",
        "Kilocalories per organism.",
        "Years per square meter."],
      ans=0,
      why="ENG-1.A.4 states that productivity is measured in units of energy per unit area "
          "per unit time and gives kilocalories per square meter per year as its own "
          "example. Each rejected option drops the area, the time, or the energy."),

 dict(q="Why is a single figure for the total energy stored in an ecosystem's plants NOT "
        "a measure of primary productivity?",
      choices=[
        "Because productivity is a rate over a unit of time and area, not a standing "
        "amount.",
        "Because plants do not store energy at all.",
        "Because energy stored in plants is measured in units of area.",
        "Because productivity concerns consumers rather than producers.",
        "Because the total energy of an ecosystem never changes."],
      ans=0,
      why="ENG-1.A.1 defines primary productivity as a RATE over a unit of time, and "
          "ENG-1.A.4 requires units of energy per unit area per unit time, so a quantity "
          "with no time in it is a different measurement."),

 dict(q="Two algae from one lake were studied, as shown. Which conclusion is best "
        "supported by the table together with the framework?",
      table=_T_PIGMENT,
      choices=[
        "The alga living deeper absorbs best the color that penetrates deeper into water.",
        "The alga living deeper absorbs best the color that is absorbed in the upper one "
        "meter.",
        "The two algae absorb the same color of light.",
        "The alga living nearest the surface absorbs best the color that penetrates "
        "deepest.",
        "Neither alga uses visible light for photosynthesis."],
      ans=0,
      why="ENG-1.A.5 states that most red light is absorbed in the upper one meter while "
          "blue light penetrates far deeper, and it attributes adapted mechanisms to "
          "aquatic photosynthesizers, so the deeper alga is matched to the deeper-reaching "
          "color."),

 dict(q="Why do the framework's statements about light imply that photosynthesis in deep "
        "water is difficult?",
      choices=[
        "Because visible light is progressively absorbed with depth, leaving little of it "
        "available to photosynthesizers there.",
        "Because water becomes too cold for photosynthesis below one meter.",
        "Because carbon dioxide is absent from deep water.",
        "Because photosynthesizers cannot live below one meter of water.",
        "Because red light is the only color that reaches deep water."],
      ans=0,
      why="ENG-1.A.5 states that most red light is absorbed in the upper one meter and "
          "that blue light reaches beyond one hundred meters only in the clearest water, "
          "then says this affects photosynthesis in aquatic ecosystems because of the lack "
          "of visible light."),

 dict(q="An ecosystem's gross primary productivity doubles while the energy its producers "
        "lose to respiration stays the same. What happens to net primary productivity?",
      choices=[
        "It rises, because a larger gross figure is reduced by the same subtraction.",
        "It falls, because a larger gross figure means more respiration.",
        "It stays the same, because respiration did not change.",
        "It cannot change, because net primary productivity depends only on respiration.",
        "It becomes equal to gross primary productivity."],
      ans=0,
      why="ENG-1.A.3 makes the net figure the gross rate less the energy lost to "
          "respiration, so raising the first term while holding the second constant raises "
          "the difference."),

 dict(q="Which of the following would be the most direct way to estimate the net primary "
        "productivity of a grassland plot over one growing season?",
      choices=[
        "Measure the energy stored in the plot's plant tissue at the beginning and end of "
        "the season and take the difference.",
        "Measure the total sunlight falling on the plot over the season.",
        "Count the number of plant species growing on the plot.",
        "Measure the area of the plot at the beginning and end of the season.",
        "Measure the mass of animals living on the plot at the end of the season."],
      ans=0,
      why="ENG-1.A.3 defines net primary productivity as the rate of energy storage by "
          "photosynthesizers after respiration is subtracted, so the energy that has "
          "actually accumulated in plant tissue over a known period is the quantity "
          "sought."),

 dict(q="Which statement correctly distinguishes what gross primary productivity measures "
        "from what net primary productivity measures?",
      choices=[
        "Gross measures the total rate of photosynthesis; net measures the rate of energy "
        "storage left after respiration.",
        "Gross measures the rate of energy storage left after respiration; net measures "
        "the total rate of photosynthesis.",
        "Gross measures a mass of tissue; net measures a rate of photosynthesis.",
        "Gross measures the sunlight arriving; net measures the sunlight reflected.",
        "Gross and net measure the same quantity in different units."],
      ans=0,
      why="ENG-1.A.2 defines gross primary productivity as the total rate of "
          "photosynthesis in a given area and ENG-1.A.3 defines net primary productivity "
          "as the rate of energy storage after subtracting the energy lost to respiration."),

 dict(q="Two lakes have the same surface area and the same sunlight, but one is far "
        "clearer than the other. Which prediction does the framework support?",
      choices=[
        "Photosynthesis can occur at greater depth in the clearer lake, because light "
        "penetrates further there.",
        "Photosynthesis can occur at greater depth in the murkier lake.",
        "Photosynthesis occurs to the same depth in both lakes, because the sunlight is "
        "the same.",
        "Photosynthesis cannot occur at any depth in either lake.",
        "Red light will reach deeper than blue light in the clearer lake."],
      ans=0,
      why="ENG-1.A.5 states that blue light penetrates deeper than one hundred meters only "
          "in the CLEAREST water, which makes clarity the condition on how far light "
          "reaches and therefore on the depth at which photosynthesis is possible."),

 dict(q="Which observation would best support the framework's claim that aquatic "
        "photosynthesizers have adapted mechanisms to address the lack of visible light?",
      choices=[
        "Photosynthesizers living at depth use pigments that capture the colors of light "
        "still present there.",
        "Photosynthesizers living at depth are larger than those at the surface.",
        "Photosynthesizers living at depth are found in both fresh and salt water.",
        "Photosynthesizers living at depth reproduce more slowly than those at the "
        "surface.",
        "Photosynthesizers living at depth contain the same amount of water as those at "
        "the surface."],
      ans=0,
      why="ENG-1.A.5 attributes adapted mechanisms specifically to the lack of visible "
          "light, so the evidence that bears on it is a feature that lets an organism use "
          "the light that remains. Size, salinity tolerance and reproductive rate address "
          "other problems."),

 dict(q="An ecologist reports a value of two thousand kilocalories per square meter per "
        "year for a forest. What has been measured?",
      choices=[
        "A rate of energy conversion or storage per unit area, which is what productivity "
        "is.",
        "The total energy in the forest at one instant.",
        "The area of the forest.",
        "The number of years the forest has existed.",
        "The mass of animals the forest supports."],
      ans=0,
      why="ENG-1.A.4 states that productivity is measured in units of energy per unit area "
          "per unit time, and the reported value carries exactly those three parts, so it "
          "is a productivity figure rather than a standing total."),

 dict(q="Why does the framework describe primary productivity as involving solar energy "
        "specifically?",
      choices=[
        "Because it is defined as the rate at which sunlight is converted into organic "
        "compounds by photosynthesis.",
        "Because sunlight is the only form of energy in an ecosystem.",
        "Because sunlight is stored directly in animal tissue without change.",
        "Because sunlight is measured in the same units as productivity.",
        "Because photosynthesis releases sunlight into the ecosystem."],
      ans=0,
      why="ENG-1.A.1 defines primary productivity as the rate at which solar energy is "
          "converted into organic compounds via photosynthesis over a unit of time, so "
          "sunlight is the input the definition names."),

 dict(q="Two ecosystems have the same gross primary productivity, but one stores far more "
        "energy in new plant tissue each year. Which explanation does the framework "
        "support?",
      choices=[
        "The ecosystem storing less energy loses more of its gross productivity to "
        "respiration.",
        "The ecosystem storing less energy receives less sunlight, even though its gross "
        "productivity is equal.",
        "The ecosystem storing more energy has a lower gross primary productivity than "
        "reported.",
        "Gross primary productivity cannot be equal if storage differs, so the "
        "measurements must be wrong.",
        "Respiration raises the energy stored, so the ecosystem storing more must respire "
        "more."],
      ans=0,
      why="ENG-1.A.3 makes stored energy the gross rate less the energy lost to "
          "respiration, so with the gross figures equal the difference in storage must "
          "come from the subtraction."),
]
