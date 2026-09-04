# AP ENVIRONMENTAL SCIENCE 3.6 Age Structure Diagrams
# CED effective Fall 2026, Unit 3 Populations.
# Enduring understanding EIN-1: Human populations change in reaction to a variety of
# factors, including social and cultural factors.
# Learning objective EIN-1.A: explain age structure diagrams. Suggested skill 5.C,
# explain patterns and trends in data to draw conclusions.
#
# Essential knowledge relied on, in the framework's own words:
#   EIN-1.A.1  Population growth rates can be interpreted from age structure diagrams by
#              the shape of the structure.
#   EIN-1.A.2  A rapidly growing population will, as a rule, have a higher proportion of
#              younger people compared to stable or declining populations.
#
# THIS TOPIC IS NAMED AFTER A PICTURE AND THE BANK CANNOT CARRY ONE. So no stem here
# points at a figure. Every item that needs an age structure supplies it as a table of
# population by age band -- by sex where the item needs both columns -- and asks the
# question of the rows. The word "diagram" does not appear in a single stem; where the
# framework's own object has to be named it is named inside a choice, never as something
# the student is asked to look at.
#
# WHAT IS DELIBERATELY NOT ASKED. The framework gives no threshold share for "rapidly
# growing", no formula tying a shape to a numerical growth rate, and no doubling time
# read from a structure -- that arithmetic belongs to EIN-1.C.4 and to topic 3.8. So no
# key here converts a shape into a rate; items 7 and 30 refuse exactly that reading. The
# framework's hedge AS A RULE is keyed in item 3 rather than dropped.
#
# BOUNDARIES. Total fertility rate and its determinants are EIN-1.B and belong to topic
# 3.7; birth, death, immigration and emigration rates and the rule of 70 are EIN-1.C and
# belong to 3.8; the four-stage model is EIN-1.D and belongs to 3.9. No key here uses
# any of them.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: export_units.py does not typeset
# Environmental Science. Year and age ranges are written with "to".
TOPIC = ("3.6", "Age Structure Diagrams", 3)

# Three populations, each column a share of that population. Every column totals 100.
_T_THREE = dict(
    headers=["Age band (years)", "Population 1 (percent of its total)",
             "Population 2 (percent of its total)", "Population 3 (percent of its total)"],
    rows=[["0 to 14", "42", "26", "15"],
          ["15 to 29", "26", "24", "17"],
          ["30 to 44", "16", "20", "19"],
          ["45 to 59", "9", "17", "22"],
          ["60 to 74", "5", "10", "18"],
          ["75 and over", "2", "3", "9"]])

# A broad based population, counted by sex. Every younger band is larger than the one
# above it.
_T_BROAD = dict(
    headers=["Age band (years)", "Males (thousands)", "Females (thousands)"],
    rows=[["0 to 9", "980", "940"],
          ["10 to 19", "820", "790"],
          ["20 to 29", "690", "670"],
          ["30 to 39", "560", "550"],
          ["40 to 49", "430", "430"],
          ["50 to 59", "310", "320"],
          ["60 to 69", "190", "210"],
          ["70 and over", "90", "130"]])

# A narrow based population: the youngest bands are the smallest.
_T_NARROW = dict(
    headers=["Age band (years)", "Males (thousands)", "Females (thousands)"],
    rows=[["0 to 9", "210", "200"],
          ["10 to 19", "260", "250"],
          ["20 to 29", "330", "320"],
          ["30 to 39", "390", "380"],
          ["40 to 49", "420", "415"],
          ["50 to 59", "400", "405"],
          ["60 to 69", "350", "370"],
          ["70 and over", "260", "310"]])

# A near vertical population: the younger bands hold nearly equal numbers.
_T_COLUMN = dict(
    headers=["Age band (years)", "Population (thousands)"],
    rows=[["0 to 9", "620"],
          ["10 to 19", "615"],
          ["20 to 29", "625"],
          ["30 to 39", "610"],
          ["40 to 49", "618"],
          ["50 to 59", "600"],
          ["60 to 69", "540"],
          ["70 and over", "410"]])

_T_COUNTRIES = dict(
    headers=["Country", "Percent of population under 15",
             "Percent of population 65 and over",
             "Annual population growth rate (percent)"],
    rows=[["Country 1", "44", "3", "2.8"],
          ["Country 2", "31", "6", "1.7"],
          ["Country 3", "19", "16", "0.4"],
          ["Country 4", "13", "23", "-0.3"]])

# Two populations of identical total size, 7,600 thousand each.
_T_PAIR = dict(
    headers=["Age band (years)", "Population A (thousands)", "Population B (thousands)"],
    rows=[["0 to 14", "3400", "1500"],
          ["15 to 44", "2600", "3100"],
          ["45 to 64", "1200", "2400"],
          ["65 and over", "400", "600"]])

_T_OVERTIME = dict(
    headers=["Year of the count", "Percent of population under 15",
             "Percent of population 65 and over"],
    rows=[["1980", "45", "3"],
          ["2000", "38", "5"],
          ["2020", "29", "9"],
          ["2040 projected", "21", "14"]])

_T_REGIONS = dict(
    headers=["Region", "Percent of population under 15",
             "Percent of population 15 to 64", "Percent of population 65 and over"],
    rows=[["Region 1", "38", "58", "4"],
          ["Region 2", "30", "62", "8"],
          ["Region 3", "22", "65", "13"],
          ["Region 4", "16", "63", "21"]])

QUESTIONS = [

 dict(q="From what does the framework say population growth rates can be interpreted?",
      choices=[
        "From the shape of a population's age structure.",
        "From the total number of individuals a population contains.",
        "From the land area over which a population is spread.",
        "From the number of other species living alongside the population.",
        "From the yearly rainfall the region receives."],
      ans=0,
      why="EIN-1.A.1 states that population growth rates can be interpreted from age "
          "structure diagrams by the shape of the structure, so it is the shape and not a "
          "total, an area or a rainfall figure that carries the information."),

 dict(q="What does the framework say a rapidly growing population will have, as a rule?",
      choices=[
        "A higher proportion of younger people than a stable or declining population.",
        "A lower proportion of younger people than a stable or declining population.",
        "Exactly the same proportion of younger people as a declining population.",
        "A higher proportion of people over sixty than a stable population has.",
        "No people at all below the age of fifteen."],
      ans=0,
      why="EIN-1.A.2 states that a rapidly growing population will, as a rule, have a "
          "higher proportion of younger people compared to stable or declining "
          "populations, which fixes both the direction and the comparison."),

 dict(q="EIN-1.A.2 says a rapidly growing population will, AS A RULE, have a higher "
        "proportion of younger people. What does that wording establish?",
      choices=[
        "A general tendency that need not hold in every single case.",
        "A law that holds without exception in every population ever counted.",
        "A claim about one named country and no other.",
        "A prediction about the total size a population will reach.",
        "A statement that applies only to populations already in decline."],
      ans=0,
      why="The hedge AS A RULE in EIN-1.A.2 states a tendency rather than a universal "
          "law, so a single population that departs from the pattern would not "
          "contradict the framework's statement."),

 dict(q="With which kinds of population does EIN-1.A.2 compare a rapidly growing one?",
      choices=[
        "With stable populations and with declining populations.",
        "With other rapidly growing populations only.",
        "With populations of other species in the same region.",
        "With populations living in a different climate zone.",
        "With the same population as it was one century earlier."],
      ans=0,
      why="EIN-1.A.2 names the comparison explicitly: a rapidly growing population is set "
          "against stable or declining populations, and against nothing else."),

 dict(q="A student writes that a count of a population by age band reports only how many "
        "people there are. What is the clearest correction from the framework?",
      choices=[
        "The shape of the structure also allows the population's growth rate to be "
        "interpreted.",
        "The count reports the total only, and nothing whatever about growth.",
        "The count reports the land area the population occupies.",
        "The count reports how many other species share the region.",
        "The count reports the rainfall the region receives each year."],
      ans=0,
      why="EIN-1.A.1 states that population growth rates can be interpreted from age "
          "structure diagrams by the shape of the structure, so the same counts carry "
          "more than a total."),

 dict(q="Two populations hold the same number of people, but a much larger share of one "
        "of them is under fifteen. Which expectation does the framework support?",
      choices=[
        "The population with the larger share under fifteen is the more rapidly growing "
        "of the two.",
        "The population with the smaller share under fifteen is the more rapidly growing "
        "of the two.",
        "The two must be growing at the same rate, because their totals match.",
        "Neither can be growing at all, because the totals are equal.",
        "The share under fifteen bears on nothing that the framework discusses."],
      ans=0,
      why="EIN-1.A.2 attaches a higher proportion of younger people to the rapidly "
          "growing population, and the two populations here differ in exactly that "
          "proportion while their totals do not."),

 dict(q="Which of these does the framework NOT claim in this topic?",
      choices=[
        "The exact number of years a population will take to double can be read off its "
        "age structure.",
        "Population growth rates can be interpreted from the shape of an age structure.",
        "A rapidly growing population, as a rule, holds a higher proportion of younger "
        "people.",
        "Stable populations are among those the rapidly growing case is compared with.",
        "Declining populations are among those the rapidly growing case is compared "
        "with."],
      ans=0,
      why="EIN-1.A.1 and EIN-1.A.2 supply the four rejected statements between them. "
          "Neither gives any arithmetic converting a shape into a rate or a number of "
          "years, so a doubling time is an addition to the framework."),

 dict(q="Three populations were counted by age band, each column giving the share of "
        "that population falling in the band. Which one is growing most rapidly, on the "
        "framework's reading?",
      table=_T_THREE,
      choices=[
        "Population 1, which holds much the largest share of its people in the youngest "
        "band.",
        "Population 3, which holds the largest share of its people in the oldest bands.",
        "Population 2, whose shares are the most nearly equal across the bands.",
        "Population 3, because a small share in the youngest band marks rapid growth.",
        "All three are growing equally, because every column totals one hundred."],
      ans=0,
      why="EIN-1.A.2 attaches a higher proportion of younger people to the rapidly "
          "growing population, and one of the three columns carries a far larger share in "
          "the youngest band than either of the others."),

 dict(q="Among those same three populations, which one holds more people aged sixty and "
        "over than under fifteen?",
      table=_T_THREE,
      choices=[
        "Population 3.",
        "Population 1.",
        "Population 2.",
        "Both the first and the second population.",
        "None of the three populations."],
      ans=0,
      why="Adding the two oldest bands and comparing them with the youngest band leaves "
          "exactly one column with more people at the top than at the bottom, which "
          "EIN-1.A.2 associates with a stable or declining rather than a growing case."),

 dict(q="Taking the population with the largest share under fifteen and the one with the "
        "smallest, how far apart are those two shares?",
      table=_T_THREE,
      choices=[
        "27 percentage points.",
        "42 percentage points.",
        "15 percentage points.",
        "57 percentage points.",
        "9 percentage points."],
      ans=0,
      why="The largest and smallest entries in the youngest band are read from the table "
          "and subtracted. EIN-1.A.2 makes that share the quantity a comparison of growth "
          "rests on."),

 dict(q="One population was counted by age band and by sex. What does that record "
        "establish about its shape?",
      table=_T_BROAD,
      choices=[
        "Each younger band holds more people than the band above it, which is the broad "
        "based shape of a rapidly growing population.",
        "Each younger band holds fewer people than the band above it, which is the narrow "
        "based shape of a declining population.",
        "The bands hold nearly equal numbers throughout, which is the near vertical shape "
        "of a stable population.",
        "The oldest band holds more people than any other band in the record.",
        "Males and females were counted over entirely different age bands."],
      ans=0,
      why="Reading down the two columns, every band holds more people than the band above "
          "it. EIN-1.A.2 attaches a higher proportion of younger people to a rapidly "
          "growing population, which is what that shape reports."),

 dict(q="In that same broad based population, how many people are counted in the youngest "
        "band?",
      table=_T_BROAD,
      choices=[
        "1,920 thousand.",
        "980 thousand.",
        "940 thousand.",
        "1,610 thousand.",
        "2,040 thousand."],
      ans=0,
      why="The two entries in the youngest band are added. The framework's reading in "
          "EIN-1.A.1 rests on the shape of the whole structure, so both sexes are counted "
          "into each band."),

 dict(q="How many people in that same broad based population are below the age of twenty?",
      table=_T_BROAD,
      choices=[
        "3,530 thousand.",
        "1,920 thousand.",
        "1,610 thousand.",
        "4,530 thousand.",
        "2,760 thousand."],
      ans=0,
      why="The four entries in the two youngest bands are added. EIN-1.A.2 makes the "
          "size of the young part of a population the quantity that distinguishes a "
          "rapidly growing case."),

 dict(q="A second population was counted by age band and by sex. What does its record "
        "establish?",
      table=_T_NARROW,
      choices=[
        "The youngest bands hold fewer people than the middle bands, which is the narrow "
        "based shape of a stable or declining population.",
        "The youngest bands hold more people than the middle bands, which is the broad "
        "based shape of a rapidly growing population.",
        "Every band in the record holds the same number of people as every other.",
        "The record holds no people at all above the age of fifty.",
        "The record counts males only and reports no females."],
      ans=0,
      why="The youngest bands in this record are the smallest and the middle bands the "
          "largest. EIN-1.A.2 ties a higher proportion of younger people to rapid growth, "
          "so the absence of that proportion points the other way."),

 dict(q="Which age band holds the most people in that second, narrow based population?",
      table=_T_NARROW,
      choices=[
        "The 40 to 49 band.",
        "The 0 to 9 band.",
        "The 20 to 29 band.",
        "The 50 to 59 band.",
        "The 70 and over band."],
      ans=0,
      why="Adding the two columns band by band gives a single largest total, and it does "
          "not fall in the youngest band. EIN-1.A.1 makes the position of the widest part "
          "of the structure part of its shape."),

 dict(q="A third population was counted in a single column by age band. What does its "
        "record establish?",
      table=_T_COLUMN,
      choices=[
        "The younger bands hold nearly equal numbers, which is the near vertical shape of "
        "a population neither growing rapidly nor falling away sharply.",
        "The younger bands hold far more people than the middle bands, which is the broad "
        "based shape of rapid growth.",
        "The younger bands hold far fewer people than the middle bands, which is a narrow "
        "based shape.",
        "The population holds nobody under the age of twenty.",
        "The oldest band is the largest band in the record."],
      ans=0,
      why="The six youngest bands differ from one another by only a few percent, so the "
          "structure is close to vertical. EIN-1.A.2 attaches the larger young share to "
          "the rapidly growing case, and this record does not carry one."),

 dict(q="Four countries were recorded for the share of their people under fifteen, the "
        "share sixty five and over, and the yearly growth rate. What does the record "
        "establish?",
      table=_T_COUNTRIES,
      choices=[
        "The countries carrying larger shares under fifteen also carry the higher growth "
        "rates.",
        "The countries carrying larger shares under fifteen carry the lower growth rates.",
        "The share under fifteen and the growth rate vary independently of one another.",
        "The country with the largest share sixty five and over carries the highest growth "
        "rate.",
        "All four countries are recorded as growing at the same yearly rate."],
      ans=0,
      why="Sorting the four countries by the share under fifteen leaves the growth rate "
          "strictly increasing. EIN-1.A.2 is the framework statement that connects a "
          "larger young share with more rapid growth."),

 dict(q="Which of those four countries is shrinking rather than growing?",
      table=_T_COUNTRIES,
      choices=[
        "Country 4, whose yearly growth rate is the only one below zero.",
        "Country 1, whose yearly growth rate is the largest of the four.",
        "Country 2, which lies in the middle of the four.",
        "Country 3, whose growth rate is small but above zero.",
        "None of the four, because every growth rate recorded is above zero."],
      ans=0,
      why="Exactly one growth rate in the record lies below zero, and it belongs to the "
          "country with the smallest share under fifteen and the largest share sixty five "
          "and over, which is the structure EIN-1.A.2 sets against rapid growth."),

 dict(q="Which of those four countries carries the age structure the framework associates "
        "with the most rapid growth?",
      table=_T_COUNTRIES,
      choices=[
        "Country 1, which holds the largest share of its people under fifteen.",
        "Country 2, which holds the second largest share under fifteen.",
        "Country 3, whose two shares are closest to equal.",
        "Country 4, which holds the largest share sixty five and over.",
        "The structures given cannot be ranked for growth at all."],
      ans=0,
      why="EIN-1.A.2 attaches a higher proportion of younger people to a rapidly growing "
          "population, and one country in this record holds a larger share under fifteen "
          "than any of the others."),

 dict(q="Two populations of identical total size were counted by broad age band. What "
        "does the record establish?",
      table=_T_PAIR,
      choices=[
        "Population A holds more than twice as many people under fifteen as Population B, "
        "although the two totals are equal.",
        "Population B holds more than twice as many people under fifteen as Population A, "
        "although the two totals are equal.",
        "The two populations hold the same number of people under fifteen.",
        "Population A is the larger of the two populations overall.",
        "Population B is the larger of the two populations overall."],
      ans=0,
      why="Adding the four bands of each column gives the same total, while the youngest "
          "band of one column is more than twice the other. EIN-1.A.2 makes that "
          "proportion, and not the total, the quantity bearing on growth."),

 dict(q="On the framework's reading, which of those two equally sized populations is "
        "growing more rapidly?",
      table=_T_PAIR,
      choices=[
        "Population A, because a higher proportion of its people are young.",
        "Population B, because a higher proportion of its people are young.",
        "Neither, because two populations of the same total size must grow alike.",
        "Population B, because it holds more people in the two middle bands.",
        "It cannot be judged at all, since the two totals are equal."],
      ans=0,
      why="EIN-1.A.2 states that a rapidly growing population will as a rule hold a "
          "higher proportion of younger people, and the two columns differ in exactly "
          "that proportion while their totals are the same."),

 dict(q="One population was counted four times over sixty years for its share under "
        "fifteen and its share sixty five and over. What does the record establish?",
      table=_T_OVERTIME,
      choices=[
        "The share under fifteen falls at every count while the share sixty five and over "
        "rises at every count.",
        "The share under fifteen rises at every count while the share sixty five and over "
        "falls at every count.",
        "Both shares rise across the four counts.",
        "Both shares fall across the four counts.",
        "Neither share changes across the four counts."],
      ans=0,
      why="Reading down the two columns, one falls at each successive count and the other "
          "rises. EIN-1.A.1 makes such a change in the shape of the structure the thing a "
          "growth rate is interpreted from."),

 dict(q="What does that sixty year record indicate about the population's growth, on the "
        "framework's reading?",
      table=_T_OVERTIME,
      choices=[
        "Its structure is moving away from the shape of a rapidly growing population.",
        "Its structure is moving toward the shape of a rapidly growing population.",
        "Its structure is unchanged across the four counts.",
        "Its structure carries no information about growth at any of the counts.",
        "Its structure indicates that the population already holds nobody under fifteen."],
      ans=0,
      why="The young share falls and the old share rises across the record. EIN-1.A.2 "
          "attaches the larger young share to the rapidly growing case, so a structure "
          "losing that share is moving away from it."),

 dict(q="Across that sixty year record, how far did the share of the population under "
        "fifteen move?",
      table=_T_OVERTIME,
      choices=[
        "A fall of 24 percentage points.",
        "A rise of 24 percentage points.",
        "A fall of 11 percentage points.",
        "A fall of 66 percentage points.",
        "No change at all."],
      ans=0,
      why="The first and last entries in the under fifteen column are subtracted. "
          "EIN-1.A.2 makes that share the quantity by which a growing population is "
          "distinguished from a stable or declining one."),

 dict(q="Which study would allow a population's growth rate to be interpreted in the way "
        "the framework describes?",
      choices=[
        "Counting the people in each age band and comparing the shape of the resulting "
        "structure with structures of known growing and declining populations.",
        "Counting only the total number of people in the population.",
        "Measuring the land area over which the population is spread.",
        "Counting the number of other species present in the region.",
        "Recording the region's yearly rainfall over several decades."],
      ans=0,
      why="EIN-1.A.1 makes the shape of the age structure the thing a growth rate is "
          "interpreted from, so a study has to build that structure and read its shape "
          "rather than record a single total or an unrelated quantity."),

 dict(q="A country reports that forty four percent of its people are under fifteen and "
        "three percent are sixty five and over. Which description follows from the "
        "framework?",
      choices=[
        "A broad based structure, of the kind a rapidly growing population has as a rule.",
        "A narrow based structure, of the kind a declining population has.",
        "A near vertical structure, of the kind a stable population has.",
        "A structure that carries no information about the population's growth.",
        "A structure indicating that the population has already stopped growing."],
      ans=0,
      why="EIN-1.A.2 states that a rapidly growing population will as a rule have a "
          "higher proportion of younger people, and a country with well over a third of "
          "its people under fifteen carries exactly that proportion."),

 dict(q="EIN-1.A.2 compares the PROPORTION of younger people between populations. Which "
        "quantity is that?",
      choices=[
        "The share of the whole population that falls in the younger age bands.",
        "The number of younger people, whatever the size of the population.",
        "The number of younger people minus the number of older people.",
        "The number of births recorded in the population each year.",
        "The age reached by the oldest person in the population."],
      ans=0,
      why="A proportion is a part expressed against the whole, which is what allows "
          "EIN-1.A.2 to compare a rapidly growing population with a stable or declining "
          "one whose total size may be quite different."),

 dict(q="Which pair of quantities does EIN-1.A.1 connect to one another?",
      choices=[
        "The shape of a population's age structure and the population's growth rate.",
        "The shape of a population's age structure and the land area it occupies.",
        "The total size of a population and the rainfall of its region.",
        "The number of species in a region and the growth rate of one of them.",
        "The age of the oldest person and the total size of the population."],
      ans=0,
      why="EIN-1.A.1 states that population growth rates can be interpreted from age "
          "structure diagrams by the shape of the structure, which puts those two "
          "quantities and no others in the same sentence."),

 dict(q="Four regions of one country were recorded by broad age band. Which region's "
        "structure most resembles that of a rapidly growing population?",
      table=_T_REGIONS,
      choices=[
        "Region 1, which holds the largest share under fifteen and the smallest share "
        "sixty five and over.",
        "Region 2, whose share under fifteen is the second largest of the four.",
        "Region 3, whose three shares are the most evenly spread.",
        "Region 4, which holds the largest share sixty five and over.",
        "All four regions carry the same structure, since each set of shares totals one "
        "hundred."],
      ans=0,
      why="EIN-1.A.2 attaches a higher proportion of younger people to a rapidly growing "
          "population. One region in this record leads on the young share and trails on "
          "the old share, so both columns point to the same region."),

 dict(q="Which single sentence collects what this topic's two statements assert and "
        "nothing further?",
      choices=[
        "Population growth rates can be interpreted from the shape of a population's age "
        "structure, and a rapidly growing population as a rule holds a higher proportion "
        "of younger people than a stable or declining one.",
        "Population growth rates can be interpreted from the shape of a population's age "
        "structure, and a rapidly growing population as a rule holds a lower proportion "
        "of younger people than a stable or declining one.",
        "Growth rates cannot be interpreted from an age structure at all, because the "
        "shape carries no information about them.",
        "The shape of an age structure gives the exact number of years a population will "
        "take to double in size.",
        "Only the total size of a population indicates whether it is growing, and its age "
        "bands add nothing."],
      ans=0,
      why="EIN-1.A.1 supplies the first clause and EIN-1.A.2 the second, including its "
          "direction and its comparison with stable and declining populations. Neither "
          "statement offers a doubling time or denies that the shape is informative."),
]
