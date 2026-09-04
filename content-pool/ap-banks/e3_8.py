# AP ENVIRONMENTAL SCIENCE 3.8 Human Population Dynamics
# CED effective Fall 2026, Unit 3 Populations.
# Enduring understanding EIN-1: Human populations change in reaction to a variety of
# factors, including social and cultural factors.
# Learning objective EIN-1.C: explain how human populations experience growth and
# decline. Suggested skill 7.A, describe environmental problems.
#
# Essential knowledge relied on, in the framework's own words:
#   EIN-1.C.1  Human population growth and decline are determined by the rates of birth,
#              death, immigration, and emigration. Birth rates and death rates are
#              affected by factors such as access to education, family planning,
#              healthcare, and nutrition.
#   EIN-1.C.2  Factors limiting global human population include the Earth's carrying
#              capacity and the basic factors that limit human population growth as set
#              forth by Malthusian theory.
#   EIN-1.C.3  Population growth can be affected by both density-independent factors,
#              such as major storms, fires, heat waves, or droughts, and
#              density-dependent factors, such as access to clean water and air, food
#              availability, disease transmission, or territory size.
#   EIN-1.C.4  The rate of natural increase (RNI) is a demographic metric measuring
#              population growth or decline, calculated by subtracting the crude death
#              rate from the crude birth rate, typically expressed as a percentage. One
#              way to estimate the doubling time of a population is by dividing 70 by the
#              annual population growth rate expressed as a percentage.
#
# WHAT THE FRAMEWORK DOES NOT SUPPLY. EIN-1.C.2 names Malthusian theory and says only
# that it sets forth basic factors limiting human population growth. It states none of
# those factors, so NO KEY HERE ASSERTS WHAT MALTHUS ARGUED -- item 4 keys exactly that
# absence. EIN-1.C.4 gives no unit for the crude rates either, so every stem that needs
# them states that they are counted per 1,000 people, and the checks recompute the
# arithmetic from the table alone.
#
# THE ARITHMETIC IS THE ONE REAL GATE THIS TOPIC HAS. Every quantitative key is
# recomputed in verify_e3_8.py from the stimulus: the rate of natural increase as the
# crude birth rate less the crude death rate, the overall change as births less deaths
# plus immigrants less emigrants, and the doubling time as 70 divided by the annual
# growth rate in percent.
#
# THE DISTINCTION MOST WORTH TESTING, and the one items 20 to 22 turn on, is that the
# rate of natural increase uses births and deaths ONLY, while EIN-1.C.1 makes the whole
# change depend on immigration and emigration as well. A population can have a positive
# rate of natural increase and still shrink.
#
# NO FIGURES ARE REFERENCED. Every record is supplied as a table.
#
# BOUNDARIES. Age structure is EIN-1.A (topic 3.6) and total fertility rate EIN-1.B
# (topic 3.7); the four stage model is EIN-1.D (topic 3.9). Carrying capacity, overshoot
# and dieback for populations generally are ERT-3.D and ERT-3.E (topic 3.4); the only
# claim used here is EIN-1.C.2's, that the Earth's carrying capacity is among the factors
# limiting the GLOBAL HUMAN population.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: export_units.py does not typeset
# Environmental Science. Year ranges are written with "to".
TOPIC = ("3.8", "Human Population Dynamics", 3)

_T_RNI = dict(
    headers=["Country", "Crude birth rate per 1,000 people",
             "Crude death rate per 1,000 people"],
    rows=[["Country 1", "34", "9"],
          ["Country 2", "21", "8"],
          ["Country 3", "12", "10"],
          ["Country 4", "9", "14"]])

_T_ZERO = dict(
    headers=["Rate recorded in one country over one year", "Per 1,000 people"],
    rows=[["Crude birth rate", "12"],
          ["Crude death rate", "12"]])

_T_DOUBLE = dict(
    headers=["Country", "Annual population growth rate (percent)"],
    rows=[["Country P", "1.0"],
          ["Country Q", "2.0"],
          ["Country R", "3.5"],
          ["Country S", "0.7"]])

_T_COMPONENTS = dict(
    headers=["Component recorded over one year", "People per 1,000 of the population"],
    rows=[["Births", "26"],
          ["Deaths", "9"],
          ["Immigrants arriving", "5"],
          ["Emigrants leaving", "12"]])

_T_COMPONENTS2 = dict(
    headers=["Component recorded over one year", "People per 1,000 of the population"],
    rows=[["Births", "14"],
          ["Deaths", "11"],
          ["Immigrants arriving", "2"],
          ["Emigrants leaving", "9"]])

_T_DEMOG = dict(
    headers=["Country", "Percent of adults completing secondary education",
             "Percent of people with access to healthcare",
             "Crude birth rate per 1,000 people", "Crude death rate per 1,000 people"],
    rows=[["Country W", "18", "24", "39", "16"],
          ["Country X", "41", "52", "29", "11"],
          ["Country Y", "68", "77", "19", "9"],
          ["Country Z", "92", "95", "11", "8"]])

_T_DENSITY = dict(
    headers=["Event recorded in one region",
             "Percent of the population lost where it was crowded",
             "Percent of the population lost where it was sparse"],
    rows=[["Event 1", "18", "16"],
          ["Event 2", "42", "9"],
          ["Event 3", "23", "22"],
          ["Event 4", "37", "6"]])

QUESTIONS = [

 dict(q="Which rates does the framework say determine human population growth and "
        "decline?",
      choices=[
        "The rates of birth, death, immigration and emigration.",
        "The rates of birth and death alone, with movement excluded.",
        "The rates of immigration and emigration alone.",
        "The rate of rainfall and the rate of soil loss.",
        "The rate at which land is cleared and the rate at which it is replanted."],
      ans=0,
      why="EIN-1.C.1 states that human population growth and decline are determined by "
          "the rates of birth, death, immigration, and emigration, which is all four "
          "together rather than either pair on its own."),

 dict(q="What does the framework say affects birth rates and death rates?",
      choices=[
        "Factors such as access to education, family planning, healthcare and nutrition.",
        "Factors such as the elevation of the land and the mineral content of the soil.",
        "Factors such as the number of other species present in the region.",
        "Factors such as the distance of the country from the nearest ocean.",
        "Nothing at all, because the framework treats both rates as fixed."],
      ans=0,
      why="EIN-1.C.1's second sentence states that birth rates and death rates are "
          "affected by factors such as access to education, family planning, healthcare, "
          "and nutrition, and names no geographic factor."),

 dict(q="Which two things does the framework name as factors limiting the global human "
        "population?",
      choices=[
        "The Earth's carrying capacity and the basic limiting factors set forth by "
        "Malthusian theory.",
        "The Earth's carrying capacity and the total area of land under cultivation.",
        "The Earth's rainfall and the number of species it supports.",
        "Malthusian theory and the number of countries in existence.",
        "The rate of immigration and the rate of emigration between countries."],
      ans=0,
      why="EIN-1.C.2 states that factors limiting global human population include the "
          "Earth's carrying capacity and the basic factors that limit human population "
          "growth as set forth by Malthusian theory, and names no others."),

 dict(q="What does the framework itself supply about Malthusian theory?",
      choices=[
        "Only that it sets forth basic factors limiting human population growth; the "
        "statement gives none of those factors.",
        "A full list of the factors the theory sets forth.",
        "A date at which the theory predicts the human population will stop growing.",
        "A figure for the number of people the Earth can support.",
        "A statement that the theory has been shown to be mistaken."],
      ans=0,
      why="EIN-1.C.2 refers to the basic factors that limit human population growth as set "
          "forth by Malthusian theory without stating any of them, giving no list, no "
          "date and no figure, so nothing further can be keyed to that statement."),

 dict(q="Which examples does the framework give of density independent factors?",
      choices=[
        "Major storms, fires, heat waves and droughts.",
        "Food availability, disease transmission and territory size.",
        "Access to clean water, access to clean air and food availability.",
        "Access to education, family planning and healthcare.",
        "Immigration, emigration and the crude birth rate."],
      ans=0,
      why="EIN-1.C.3 names major storms, fires, heat waves, or droughts as its examples of "
          "density independent factors, and gives an entirely different list for density "
          "dependent ones."),

 dict(q="Which examples does the framework give of density dependent factors?",
      choices=[
        "Access to clean water and air, food availability, disease transmission and "
        "territory size.",
        "Major storms, fires, heat waves and droughts.",
        "Access to education, family planning, healthcare and nutrition.",
        "The crude birth rate, the crude death rate and the rate of natural increase.",
        "The Earth's carrying capacity and the theory of Malthus."],
      ans=0,
      why="EIN-1.C.3 names access to clean water and air, food availability, disease "
          "transmission, or territory size as its examples of density dependent factors, "
          "and puts storms, fires, heat waves and droughts in the other category."),

 dict(q="A revision card lists five things and calls all five framework examples of "
        "density independent factors. Which one is not?",
      choices=[
        "A shortage of food.",
        "A major storm.",
        "A fire.",
        "A heat wave.",
        "A drought."],
      ans=0,
      why="EIN-1.C.3 lists major storms, fires, heat waves and droughts as density "
          "independent, and puts food availability in the density dependent list instead."),

 dict(q="How does the framework say the rate of natural increase is calculated?",
      choices=[
        "By subtracting the crude death rate from the crude birth rate.",
        "By subtracting the crude birth rate from the crude death rate.",
        "By adding the crude birth rate to the crude death rate.",
        "By subtracting emigration from immigration.",
        "By dividing the crude birth rate by the crude death rate."],
      ans=0,
      why="EIN-1.C.4 states that the rate of natural increase is calculated by subtracting "
          "the crude death rate from the crude birth rate, which fixes both the operation "
          "and the order of the two rates."),

 dict(q="What does the framework say the rate of natural increase measures?",
      choices=[
        "Population growth or decline.",
        "The total number of people in a population.",
        "The land area a population occupies.",
        "The movement of people across a border.",
        "The share of a population living in cities."],
      ans=0,
      why="EIN-1.C.4 calls the rate of natural increase a demographic metric measuring "
          "population growth or decline, so it reports a change rather than a size, an "
          "area or a movement."),

 dict(q="In what form does the framework say the rate of natural increase is typically "
        "expressed?",
      choices=[
        "As a percentage.",
        "As a count of people.",
        "As a number of years.",
        "As an area of land.",
        "As a ratio of births to deaths."],
      ans=0,
      why="EIN-1.C.4 states that the rate of natural increase is typically expressed as a "
          "percentage, which is why a crude rate counted per thousand people is converted "
          "before it is reported."),

 dict(q="What does the framework give as one way to estimate the doubling time of a "
        "population?",
      choices=[
        "Dividing 70 by the annual population growth rate expressed as a percentage.",
        "Multiplying 70 by the annual population growth rate expressed as a percentage.",
        "Dividing the annual population growth rate by 70.",
        "Subtracting the annual population growth rate from 70.",
        "Dividing 70 by the crude birth rate counted per thousand people."],
      ans=0,
      why="EIN-1.C.4 states that one way to estimate the doubling time of a population is "
          "by dividing 70 by the annual population growth rate expressed as a percentage, "
          "which fixes both the operation and which quantity is the divisor."),

 dict(q="EIN-1.C.4 offers that calculation as ONE WAY to ESTIMATE a doubling time. What "
        "does that wording establish?",
      choices=[
        "An approximation, and one method among others rather than the only one.",
        "An exact result that no other method could improve on.",
        "The only method that exists for finding a doubling time.",
        "A method that applies only to populations that are shrinking.",
        "A method for finding the total size a population will reach."],
      ans=0,
      why="The words ONE WAY and ESTIMATE in EIN-1.C.4 mark the calculation as an "
          "approximation and as one method among others, so nothing in the framework makes "
          "it exact or exclusive."),

 dict(q="Four countries were recorded for their crude birth and death rates. Which one's "
        "population is declining by natural increase?",
      table=_T_RNI,
      choices=[
        "Country 4, whose crude death rate exceeds its crude birth rate.",
        "Country 1, whose crude birth rate exceeds its crude death rate.",
        "Country 2, whose two rates are the closest together.",
        "Country 3, whose crude birth rate is the second lowest.",
        "None of the four, since a crude birth rate is always the larger of the two."],
      ans=0,
      why="EIN-1.C.4 calculates the rate of natural increase by subtracting the crude "
          "death rate from the crude birth rate, and exactly one country in the record "
          "returns a negative result."),

 dict(q="Taking those same crude rates as counts per thousand people, what is the rate of "
        "natural increase of the country with the highest birth rate?",
      table=_T_RNI,
      choices=[
        "2.5 percent.",
        "25 percent.",
        "3.4 percent.",
        "4.3 percent.",
        "0.9 percent."],
      ans=0,
      why="EIN-1.C.4 subtracts the crude death rate from the crude birth rate and states "
          "that the result is typically expressed as a percentage, so a difference counted "
          "per thousand people is converted before it is reported."),

 dict(q="Among those same four countries, which one's rate of natural increase lies "
        "closest to zero?",
      table=_T_RNI,
      choices=[
        "Country 3.",
        "Country 1.",
        "Country 2.",
        "Country 4.",
        "Two of them are tied at exactly zero."],
      ans=0,
      why="Subtracting each crude death rate from its crude birth rate, as EIN-1.C.4 "
          "directs, leaves one country with a difference smaller in size than any other."),

 dict(q="One country's two crude rates over a year were recorded. What does the "
        "framework's metric give for it?",
      table=_T_ZERO,
      choices=[
        "A rate of natural increase of zero, so births and deaths alone leave the "
        "population unchanged.",
        "A rate of natural increase of 12 percent, since both rates are 12.",
        "A rate of natural increase of 24 percent, since the two rates are added.",
        "A rate of natural increase of 1.2 percent, since the difference is divided by "
        "ten.",
        "No rate at all, because the framework's calculation needs immigration figures."],
      ans=0,
      why="EIN-1.C.4 subtracts the crude death rate from the crude birth rate, and two "
          "equal rates leave nothing. The calculation uses those two rates only, so no "
          "migration figure is required for it."),

 dict(q="Four countries were recorded for their yearly growth rates. Using the "
        "framework's estimate, how long will the second of them take to double?",
      table=_T_DOUBLE,
      choices=[
        "About 35 years.",
        "About 70 years.",
        "About 140 years.",
        "About 20 years.",
        "About 2 years."],
      ans=0,
      why="EIN-1.C.4 estimates doubling time by dividing 70 by the annual population "
          "growth rate expressed as a percentage, so a larger growth rate returns a "
          "shorter time."),

 dict(q="Which of those same four countries will double soonest on the framework's "
        "estimate?",
      table=_T_DOUBLE,
      choices=[
        "Country R, which records the largest yearly growth rate.",
        "Country S, which records the smallest yearly growth rate.",
        "Country P, whose growth rate is exactly one percent.",
        "Country Q, whose growth rate is exactly two percent.",
        "All four will take the same time, since the same number is divided each time."],
      ans=0,
      why="EIN-1.C.4 divides 70 by the annual growth rate expressed as a percentage, so "
          "the country with the largest growth rate returns the smallest doubling time."),

 dict(q="Among that same set of four countries, how much longer than the country growing "
        "at exactly one percent a year will the slowest growing one take to double?",
      table=_T_DOUBLE,
      choices=[
        "About 30 years longer.",
        "About 70 years longer.",
        "About 100 years longer.",
        "About 15 years longer.",
        "It will take less time, not more."],
      ans=0,
      why="EIN-1.C.4's estimate is applied to each of the two growth rates and the two "
          "results subtracted, and the smaller growth rate returns the longer doubling "
          "time."),

 dict(q="A country's births, deaths, immigrants and emigrants over one year were recorded "
        "per thousand people. What is its rate of natural increase?",
      table=_T_COMPONENTS,
      choices=[
        "1.7 percent, since only births and deaths enter the calculation.",
        "1.0 percent, since all four components enter the calculation.",
        "2.6 percent, since the births alone give the rate.",
        "3.5 percent, since births and immigrants are added together.",
        "0.7 percent, since immigrants and emigrants give the rate."],
      ans=0,
      why="EIN-1.C.4 calculates the rate of natural increase by subtracting the crude "
          "death rate from the crude birth rate, so the two migration lines take no part "
          "in it even though EIN-1.C.1 makes them part of the overall change."),

 dict(q="Using that same record of four components, by how much did the population change "
        "over the year in all?",
      table=_T_COMPONENTS,
      choices=[
        "It grew by 10 people per thousand, which is 1.0 percent.",
        "It grew by 17 people per thousand, which is 1.7 percent.",
        "It fell by 7 people per thousand, which is 0.7 percent.",
        "It grew by 31 people per thousand, which is 3.1 percent.",
        "It did not change, because the four components cancel exactly."],
      ans=0,
      why="EIN-1.C.1 states that growth and decline are determined by the rates of birth, "
          "death, immigration and emigration together, so all four lines enter the overall "
          "change even though the rate of natural increase uses only two of them."),

 dict(q="A second country's four components over one year were recorded on the same basis. "
        "What does that record establish?",
      table=_T_COMPONENTS2,
      choices=[
        "Its rate of natural increase is positive, yet its population shrank over the "
        "year.",
        "Its rate of natural increase is negative, yet its population grew over the year.",
        "Its rate of natural increase is positive, and its population grew over the year.",
        "Its rate of natural increase is negative, and its population shrank over the "
        "year.",
        "Its rate of natural increase cannot be found without a total population figure."],
      ans=0,
      why="EIN-1.C.4's subtraction of deaths from births leaves a positive figure, while "
          "EIN-1.C.1's fuller account, which adds immigration and subtracts emigration, "
          "leaves a negative one, so the two point opposite ways in this record."),

 dict(q="Four countries were recorded for education, healthcare access and their two crude "
        "rates. What does the record establish?",
      table=_T_DEMOG,
      choices=[
        "Both crude rates fall as education and healthcare access rise.",
        "Both crude rates rise as education and healthcare access rise.",
        "The crude birth rate falls while the crude death rate rises as access rises.",
        "The crude death rate falls while the crude birth rate rises as access rises.",
        "Neither crude rate moves with education or healthcare access in this record."],
      ans=0,
      why="Sorting the countries by education, and then by healthcare access, leaves both "
          "crude rates strictly falling. EIN-1.C.1 names access to education and to "
          "healthcare among the factors affecting birth rates and death rates."),

 dict(q="In that same four country record, which country's rate of natural increase is the "
        "largest?",
      table=_T_DEMOG,
      choices=[
        "Country W, at 2.3 percent.",
        "Country X, at 1.8 percent.",
        "Country Y, at 1.0 percent.",
        "Country Z, at 0.3 percent.",
        "All four are equal, because each crude birth rate exceeds its crude death rate."],
      ans=0,
      why="EIN-1.C.4 subtracts each crude death rate from its crude birth rate and "
          "expresses the result as a percentage, and one country's difference is larger "
          "than any of the others."),

 dict(q="Four events were recorded for the share of the population lost where it was "
        "crowded and where it was sparse. Which events acted in the way the framework "
        "calls density dependent?",
      table=_T_DENSITY,
      choices=[
        "The second and the fourth, whose losses were far heavier where the population was "
        "crowded.",
        "The first and the third, whose losses were far heavier where the population was "
        "crowded.",
        "All four, since every event caused some loss.",
        "None, since the losses were similar at both densities in every event.",
        "The second and the fourth, whose losses were far heavier where the population was "
        "sparse."],
      ans=0,
      why="EIN-1.C.3 distinguishes density dependent from density independent factors, and "
          "in exactly two of these events the loss where the population was crowded is "
          "several times the loss where it was sparse, while in the other two the two "
          "losses are nearly equal."),

 dict(q="In which of those same four events did crowding make the largest difference to "
        "the share of the population lost?",
      table=_T_DENSITY,
      choices=[
        "Event 2.",
        "Event 1.",
        "Event 3.",
        "Event 4.",
        "Crowding made no difference in any of the four events."],
      ans=0,
      why="Subtracting the sparse loss from the crowded loss in each event leaves one "
          "event with the largest gap. EIN-1.C.3 treats a factor whose effect depends on "
          "density as density dependent."),

 dict(q="A hurricane strikes a coastal region and kills a similar share of the people "
        "wherever it passes, crowded districts and empty ones alike. Which of the "
        "framework's categories does that fit?",
      choices=[
        "A density independent factor, of which the framework names major storms as an "
        "example.",
        "A density dependent factor, of which the framework names disease transmission as "
        "an example.",
        "A factor limiting the global human population, as Malthusian theory sets forth.",
        "A component of the rate of natural increase.",
        "A factor affecting the crude birth rate through access to education."],
      ans=0,
      why="EIN-1.C.3 names major storms among its examples of density independent factors, "
          "and an effect that does not change with how crowded the population is is what "
          "that category describes."),

 dict(q="An infectious disease spreads through a city and kills a far larger share of "
        "people in its most crowded districts than in its emptiest ones. Which of the "
        "framework's categories does that fit?",
      choices=[
        "A density dependent factor, of which the framework names disease transmission as "
        "an example.",
        "A density independent factor, of which the framework names heat waves as an "
        "example.",
        "A factor limiting the global human population, as Malthusian theory sets forth.",
        "A component of the rate of natural increase alongside immigration.",
        "A factor affecting the crude birth rate through access to family planning."],
      ans=0,
      why="EIN-1.C.3 names disease transmission among its examples of density dependent "
          "factors, and an effect that grows heavier as the population becomes more "
          "crowded is what that category describes."),

 dict(q="Which single measurement does a demographer need in order to apply EIN-1.C.4's "
        "estimate of doubling time?",
      choices=[
        "The annual population growth rate, expressed as a percentage.",
        "The total number of people in the population.",
        "The crude birth rate alone, counted per thousand people.",
        "The number of immigrants arriving each year.",
        "The land area over which the population is spread."],
      ans=0,
      why="EIN-1.C.4 states that the estimate divides 70 by the annual population growth "
          "rate expressed as a percentage, so that rate is the only quantity the "
          "calculation takes."),

 dict(q="Which single sentence collects what this topic's four statements assert and "
        "nothing further?",
      choices=[
        "Growth and decline are determined by birth, death, immigration and emigration, "
        "with birth and death rates affected by access to education, family planning, "
        "healthcare and nutrition; the Earth's carrying capacity and the basic factors of "
        "Malthusian theory limit the global population; growth is affected by density "
        "independent and density dependent factors; and the rate of natural increase is "
        "the crude birth rate less the crude death rate, with doubling time estimated by "
        "dividing 70 by the annual growth rate in percent.",
        "Growth and decline are determined by birth and death alone; the global population "
        "has no limiting factors; only density independent factors affect growth; and the "
        "rate of natural increase is the crude birth rate added to the crude death rate.",
        "Growth and decline are determined by immigration and emigration alone, and "
        "doubling time is estimated by multiplying 70 by the annual growth rate.",
        "The framework names the factors limiting the global population in full detail, "
        "including every factor Malthusian theory sets forth.",
        "The rate of natural increase measures the total size of a population, and "
        "doubling time is found by dividing the growth rate by 70."],
      ans=0,
      why="EIN-1.C.1 supplies the four determining rates and the factors affecting birth "
          "and death rates, EIN-1.C.2 the two limits on the global population, EIN-1.C.3 "
          "both categories of factor, and EIN-1.C.4 the calculation of the rate of natural "
          "increase and the doubling time estimate."),
]
