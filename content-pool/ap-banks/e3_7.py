# AP ENVIRONMENTAL SCIENCE 3.7 Total Fertility Rate
# CED effective Fall 2026, Unit 3 Populations.
# Enduring understanding EIN-1: Human populations change in reaction to a variety of
# factors, including social and cultural factors.
# Learning objective EIN-1.B: explain factors that affect total fertility rate in human
# populations. Suggested skill 5.A, describe patterns or trends in data.
#
# Essential knowledge relied on, in the framework's own words:
#   EIN-1.B.1  Total fertility rate (TFR) is affected by the age at which females have
#              their first child, educational opportunities for females, access to family
#              planning, and government acts and policies.
#   EIN-1.B.2  If fertility rate is at replacement levels, a population is considered
#              relatively stable.
#   EIN-1.B.3  Factors associated with infant mortality rates include whether mothers have
#              access to good healthcare and nutrition. Changes in these factors can lead
#              to changes in infant mortality rates over time.
#
# WHAT THE FRAMEWORK DOES NOT SUPPLY, and what this module therefore supplies in the
# stem instead. EIN-1.B.2 says "at replacement levels" without giving a number, and the
# framework nowhere defines how a total fertility rate is computed. So every item that
# needs either one STATES IT IN ITS OWN STEM -- the replacement level as 2.1 children per
# woman, and the arithmetic for a rate built from age specific rates -- and the verifier
# recomputes the arithmetic from the table alone. The framework's contribution to those
# keys is the interpretation only: at replacement, relatively stable.
#
# NO ITEM CLAIMS A DIRECTION THE FRAMEWORK DOES NOT. EIN-1.B.1 says the four named things
# AFFECT total fertility rate; it does not say which way. So where a table shows fertility
# falling as schooling rises, the keyed conclusion is the pattern IN THAT RECORD, and the
# framework citation is only that the quantity is one it names as affecting fertility.
#
# NO FIGURES ARE REFERENCED. Every record is supplied as a table.
#
# BOUNDARIES. Age structure is EIN-1.A (topic 3.6); crude birth and death rates, the rate
# of natural increase and the rule of 70 are EIN-1.C (topic 3.8); the four stage model is
# EIN-1.D (topic 3.9). No key here uses any of them.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: export_units.py does not typeset
# Environmental Science. Year and age ranges are written with "to".
TOPIC = ("3.7", "Total Fertility Rate", 3)

_T_FACTORS = dict(
    headers=["Country", "Mean age of mothers at first birth (years)",
             "Percent of girls completing secondary school",
             "Percent of women with access to family planning services",
             "Total fertility rate (children per woman)"],
    rows=[["Country 1", "18", "24", "19", "5.6"],
          ["Country 2", "20", "48", "41", "4.1"],
          ["Country 3", "23", "72", "68", "2.7"],
          ["Country 4", "27", "94", "89", "1.6"]])

_T_REPLACEMENT = dict(
    headers=["Country", "Total fertility rate (children per woman)"],
    rows=[["Country A", "1.2"],
          ["Country B", "2.1"],
          ["Country C", "3.6"],
          ["Country D", "1.7"],
          ["Country E", "2.9"]])

_T_COHORT = dict(
    headers=["Group of women who have completed childbearing", "Number of women",
             "Total number of children they bore"],
    rows=[["Group 1", "500", "1,750"],
          ["Group 2", "800", "1,680"],
          ["Group 3", "400", "560"],
          ["Group 4", "1,000", "4,300"]])

_T_ASFR_LOW = dict(
    headers=["Age band of mothers (years)",
             "Births per 1,000 women of that age in one year"],
    rows=[["15 to 19", "40"],
          ["20 to 24", "120"],
          ["25 to 29", "130"],
          ["30 to 34", "80"],
          ["35 to 39", "40"],
          ["40 to 44", "10"]])

_T_ASFR_HIGH = dict(
    headers=["Age band of mothers (years)",
             "Births per 1,000 women of that age in one year"],
    rows=[["15 to 19", "60"],
          ["20 to 24", "170"],
          ["25 to 29", "150"],
          ["30 to 34", "90"],
          ["35 to 39", "50"],
          ["40 to 44", "20"]])

_T_EDUCATION = dict(
    headers=["Country", "Mean years of schooling completed by women",
             "Total fertility rate (children per woman)"],
    rows=[["Country V", "2.1", "6.2"],
          ["Country W", "4.5", "5.0"],
          ["Country X", "7.0", "3.8"],
          ["Country Y", "10.2", "2.4"],
          ["Country Z", "13.4", "1.5"]])

_T_AGEFIRST = dict(
    headers=["Population", "Mean age of mothers at first birth (years)",
             "Total fertility rate (children per woman)"],
    rows=[["Population 1", "17.8", "6.1"],
          ["Population 2", "20.4", "4.4"],
          ["Population 3", "24.1", "2.6"],
          ["Population 4", "28.6", "1.5"]])

_T_FAMPLAN = dict(
    headers=["District", "Percent of women reporting access to family planning services",
             "Total fertility rate (children per woman)"],
    rows=[["District 1", "12", "6.4"],
          ["District 2", "35", "4.7"],
          ["District 3", "58", "3.1"],
          ["District 4", "81", "1.9"]])

_T_POLICY = dict(
    headers=["Period", "Government payment to families for each child (index)",
             "Total fertility rate (children per woman)"],
    rows=[["The five years before the policy", "0", "1.4"],
          ["The first five years after it", "100", "1.6"],
          ["The second five years after it", "140", "1.9"],
          ["The third five years after it", "150", "2.0"]])

_T_INFANT = dict(
    headers=["Region", "Percent of mothers receiving healthcare during pregnancy",
             "Percent of mothers meeting the recommended nutrition",
             "Infant deaths per 1,000 live births"],
    rows=[["Region 1", "22", "31", "78"],
          ["Region 2", "45", "50", "52"],
          ["Region 3", "71", "74", "27"],
          ["Region 4", "93", "90", "6"]])

_T_INFANT_TIME = dict(
    headers=["Year of the survey",
             "Percent of mothers receiving healthcare during pregnancy",
             "Infant deaths per 1,000 live births"],
    rows=[["1990", "28", "96"],
          ["2000", "44", "71"],
          ["2010", "67", "43"],
          ["2020", "88", "19"]])

QUESTIONS = [

 dict(q="Which set of things does the framework name as affecting total fertility rate?",
      choices=[
        "The age at which females have their first child, educational opportunities for "
        "females, access to family planning, and government acts and policies.",
        "The age at which females have their first child, the climate of the region, the "
        "altitude of the land, and the local soil type.",
        "Educational opportunities for females, the number of species in the region, "
        "rainfall, and government acts and policies.",
        "Access to family planning, the mean elevation of the country, its total land "
        "area, and its distance from the equator.",
        "Government acts and policies alone, since the framework names no other factor."],
      ans=0,
      why="EIN-1.B.1 names exactly four things affecting total fertility rate: the age at "
          "which females have their first child, educational opportunities for females, "
          "access to family planning, and government acts and policies."),

 dict(q="A revision card lists five things and calls all five framework factors affecting "
        "total fertility rate. Which one is not?",
      choices=[
        "The mean elevation of the country.",
        "The age at which females have their first child.",
        "Educational opportunities for females.",
        "Access to family planning.",
        "Government acts and policies."],
      ans=0,
      why="EIN-1.B.1 names four factors and elevation is not among them, while each of the "
          "other four appears in the statement word for word."),

 dict(q="What does the framework say about a population whose fertility rate sits at "
        "replacement levels?",
      choices=[
        "It is considered relatively stable.",
        "It is considered to be growing rapidly.",
        "It is considered to be declining rapidly.",
        "It is considered to have no births at all.",
        "It is considered impossible to describe without knowing its land area."],
      ans=0,
      why="EIN-1.B.2 states that if fertility rate is at replacement levels, a population "
          "is considered relatively stable, which is the whole of what the framework "
          "attaches to that condition."),

 dict(q="Which factors does the framework associate with infant mortality rates?",
      choices=[
        "Whether mothers have access to good healthcare and nutrition.",
        "Whether the region receives more than a set amount of rainfall.",
        "Whether the country lies above or below a given latitude.",
        "Whether the population is larger or smaller than its neighbours.",
        "Whether the land is farmed or left uncultivated."],
      ans=0,
      why="EIN-1.B.3 states that factors associated with infant mortality rates include "
          "whether mothers have access to good healthcare and nutrition, and it names no "
          "geographic or agricultural factor."),

 dict(q="According to the framework, what can lead to changes in infant mortality rates "
        "over time?",
      choices=[
        "Changes in whether mothers have access to good healthcare and nutrition.",
        "Changes in the total land area of the country.",
        "Changes in the number of other species living in the region.",
        "Changes in the average elevation at which people live.",
        "Nothing, because infant mortality rates are fixed for each country."],
      ans=0,
      why="EIN-1.B.3 states that changes in the factors it names, access to good "
          "healthcare and nutrition, can lead to changes in infant mortality rates over "
          "time, so the rate is neither fixed nor tied to geography."),

 dict(q="EIN-1.B.2 says a population at replacement level fertility is considered "
        "RELATIVELY stable. What does that wording establish?",
      choices=[
        "A size that holds close to steady rather than one fixed exactly.",
        "A size that is fixed exactly and cannot vary by a single person.",
        "A size that must be falling every year.",
        "A size that must be rising every year.",
        "A statement about the land area rather than about the number of people."],
      ans=0,
      why="The qualifier RELATIVELY in EIN-1.B.2 describes a population held near a steady "
          "size, not one pinned exactly, so small movements are consistent with the "
          "framework's description."),

 dict(q="Which of these does the framework NOT claim in this topic?",
      choices=[
        "Total fertility rate is set by the climate and elevation of the region.",
        "Total fertility rate is affected by the age at which females have their first "
        "child.",
        "A population whose fertility rate is at replacement levels is considered "
        "relatively stable.",
        "Access to good healthcare and nutrition for mothers is associated with infant "
        "mortality rates.",
        "Government acts and policies are among the things that affect total fertility "
        "rate."],
      ans=0,
      why="EIN-1.B.1, EIN-1.B.2 and EIN-1.B.3 supply the four rejected statements between "
          "them. None of the three names climate or elevation, so that pairing is an "
          "addition to the framework."),

 dict(q="Four countries were recorded for three of the things the framework names "
        "alongside their fertility rates. What does the record establish?",
      table=_T_FACTORS,
      choices=[
        "The countries where mothers begin later, more girls finish school and more women "
        "reach family planning services are the countries with the lower fertility rates.",
        "The countries where mothers begin later, more girls finish school and more women "
        "reach family planning services are the countries with the higher fertility "
        "rates.",
        "Fertility rate varies independently of all three of the other columns.",
        "Only the schooling column moves with fertility rate; the other two do not.",
        "All four countries record the same total fertility rate."],
      ans=0,
      why="Sorting the countries by any one of the three columns leaves fertility "
          "strictly falling. EIN-1.B.1 names the age at first birth, educational "
          "opportunities for females and access to family planning among the things that "
          "affect total fertility rate."),

 dict(q="Which of those four countries records both the youngest mothers at first birth "
        "and the highest fertility rate?",
      table=_T_FACTORS,
      choices=[
        "Country 1.",
        "Country 2.",
        "Country 3.",
        "Country 4.",
        "No single country leads on both columns at once."],
      ans=0,
      why="The smallest entry in the age at first birth column and the largest entry in "
          "the fertility column belong to the same row. EIN-1.B.1 names the age at which "
          "females have their first child as one of the factors affecting fertility."),

 dict(q="Across those same four countries, how far apart are the highest and lowest total "
        "fertility rates?",
      table=_T_FACTORS,
      choices=[
        "4.0 children per woman.",
        "5.6 children per woman.",
        "1.6 children per woman.",
        "7.2 children per woman.",
        "2.7 children per woman."],
      ans=0,
      why="The largest and smallest entries in the fertility column are subtracted. "
          "EIN-1.B.1 makes total fertility rate the quantity the other three columns are "
          "said to affect."),

 dict(q="Five countries were recorded for their fertility rates. Taking replacement level "
        "to be 2.1 children per woman, which country does the framework describe as "
        "relatively stable?",
      table=_T_REPLACEMENT,
      choices=[
        "Country B.",
        "Country A.",
        "Country C.",
        "Country D.",
        "Country E."],
      ans=0,
      why="Exactly one of the five rates equals the replacement level given in the stem, "
          "and EIN-1.B.2 states that a population at replacement level fertility is "
          "considered relatively stable."),

 dict(q="Among those same five countries, how many record a fertility rate below the "
        "replacement level of 2.1 children per woman?",
      table=_T_REPLACEMENT,
      choices=[
        "Two of them.",
        "One of them.",
        "Three of them.",
        "Four of them.",
        "No country in the record lies below it."],
      ans=0,
      why="Counting the entries strictly below the replacement level stated in the stem "
          "gives the answer. EIN-1.B.2 makes replacement level the reference against which "
          "a population is judged relatively stable."),

 dict(q="Four groups of women who had completed childbearing were counted alongside the "
        "children they bore. Taking replacement to be 2.1 children per woman, which "
        "group's completed fertility sits at replacement?",
      table=_T_COHORT,
      choices=[
        "Group 2.",
        "Group 1.",
        "Group 3.",
        "Group 4.",
        "No group in the record reaches replacement."],
      ans=0,
      why="Dividing each group's children by its number of women gives its completed "
          "fertility, and exactly one of the four equals the replacement level stated in "
          "the stem. EIN-1.B.2 calls a population at that level relatively stable."),

 dict(q="In that same record of completed childbearing, what is the mean number of "
        "children borne by the women of the largest group?",
      table=_T_COHORT,
      choices=[
        "4.3 children per woman.",
        "3.5 children per woman.",
        "2.1 children per woman.",
        "1.4 children per woman.",
        "4,300 children per woman."],
      ans=0,
      why="The largest group's children are divided by its number of women. The framework "
          "treats total fertility rate as a per woman quantity in EIN-1.B.2, where it is "
          "compared with a replacement level."),

 dict(q="In one population the yearly birth rate of women in each five year age band was "
        "recorded. Its total fertility rate is five times the sum of those yearly rates, "
        "divided by one thousand. What is it?",
      table=_T_ASFR_LOW,
      choices=[
        "2.1 children per woman.",
        "4.2 children per woman.",
        "0.42 children per woman.",
        "420 children per woman.",
        "1.05 children per woman."],
      ans=0,
      why="The six yearly rates are added and the rule given in the stem is applied. "
          "EIN-1.B.2 then supplies the interpretation, since a rate at replacement level "
          "marks a population considered relatively stable."),

 dict(q="A second population's yearly birth rates by age band were recorded on the same "
        "basis. Taking replacement to be 2.1 children per woman, what does its total "
        "fertility rate show?",
      table=_T_ASFR_HIGH,
      choices=[
        "A rate of 2.7 children per woman, which lies above replacement.",
        "A rate of 2.7 children per woman, which lies below replacement.",
        "A rate of 5.4 children per woman, which lies above replacement.",
        "A rate of 1.35 children per woman, which lies below replacement.",
        "A rate of 540 children per woman, which lies above replacement."],
      ans=0,
      why="The six yearly rates are added and the rule stated in the stem applied, giving "
          "a rate larger than the replacement level. EIN-1.B.2 reserves the description "
          "relatively stable for a population at replacement level."),

 dict(q="Five countries were recorded for the schooling their women complete alongside "
        "their fertility rates. What does the record establish?",
      table=_T_EDUCATION,
      choices=[
        "Fertility rate falls at every step as the mean years of schooling rise.",
        "Fertility rate rises at every step as the mean years of schooling rise.",
        "Fertility rate and mean years of schooling vary independently in this record.",
        "The country with the most schooling records the highest fertility rate.",
        "All five countries record the same mean years of schooling."],
      ans=0,
      why="Sorting the five countries by mean years of schooling leaves fertility strictly "
          "falling. EIN-1.B.1 names educational opportunities for females among the things "
          "that affect total fertility rate."),

 dict(q="Across those five countries, how much lower is the fertility rate of the "
        "best schooled than of the least schooled?",
      table=_T_EDUCATION,
      choices=[
        "Lower by 4.7 children per woman.",
        "Lower by 6.2 children per woman.",
        "Lower by 1.5 children per woman.",
        "Lower by 3.8 children per woman.",
        "Lower by 7.7 children per woman."],
      ans=0,
      why="The fertility rates of the rows with the most and the least schooling are "
          "subtracted. EIN-1.B.1 names educational opportunities for females as a factor "
          "affecting total fertility rate."),

 dict(q="Four populations were recorded for the mean age of mothers at first birth "
        "alongside their fertility rates. What does the record establish?",
      table=_T_AGEFIRST,
      choices=[
        "Fertility rate falls at every step as the mean age at first birth rises.",
        "Fertility rate rises at every step as the mean age at first birth rises.",
        "The two columns move independently of one another in this record.",
        "The population with the oldest mothers records the highest fertility rate.",
        "All four populations record the same age at first birth."],
      ans=0,
      why="Sorting the four populations by the mean age at first birth leaves fertility "
          "strictly falling. EIN-1.B.1 names the age at which females have their first "
          "child among the things that affect total fertility rate."),

 dict(q="Taking replacement to be 2.1 children per woman, which of those four populations "
        "records a fertility rate below replacement?",
      table=_T_AGEFIRST,
      choices=[
        "Population 4.",
        "Population 1.",
        "Population 2.",
        "Population 3.",
        "None of the four populations."],
      ans=0,
      why="Exactly one of the four rates lies below the replacement level stated in the "
          "stem. EIN-1.B.2 makes replacement level the reference at which a population is "
          "considered relatively stable."),

 dict(q="Four districts of one country were recorded for reported access to family "
        "planning services alongside their fertility rates. What does the record "
        "establish?",
      table=_T_FAMPLAN,
      choices=[
        "Fertility rate falls at every step as reported access to those services rises.",
        "Fertility rate rises at every step as reported access to those services rises.",
        "Reported access and fertility rate move independently in this record.",
        "The district with the least reported access records the lowest fertility rate.",
        "All four districts record the same fertility rate."],
      ans=0,
      why="Sorting the four districts by reported access leaves fertility strictly "
          "falling. EIN-1.B.1 names access to family planning among the things that "
          "affect total fertility rate."),

 dict(q="A ministry opens clinics offering contraception in districts that previously had "
        "none. Which of the framework's named factors does that measure address?",
      choices=[
        "Access to family planning.",
        "The age at which females have their first child.",
        "Educational opportunities for females.",
        "Whether mothers have access to good nutrition.",
        "The number of other species living in the district."],
      ans=0,
      why="EIN-1.B.1 lists access to family planning as one of the four things affecting "
          "total fertility rate, and opening clinics that provide contraception changes "
          "exactly that access."),

 dict(q="One country was recorded over four periods spanning a change in what it pays "
        "families for each child. What does the record establish?",
      table=_T_POLICY,
      choices=[
        "The fertility rate rose in each successive period as the payment rose.",
        "The fertility rate fell in each successive period as the payment rose.",
        "The fertility rate was unchanged across the four periods.",
        "The payment was unchanged across the four periods.",
        "The fertility rate was highest in the period before the payment began."],
      ans=0,
      why="Reading down the two columns, both rise at every step. EIN-1.B.1 names "
          "government acts and policies among the things that affect total fertility "
          "rate, which is the kind of measure this record follows."),

 dict(q="Which of the framework's named factors does that record of payments to families "
        "bear on most directly?",
      table=_T_POLICY,
      choices=[
        "Government acts and policies.",
        "Access to good healthcare for mothers during pregnancy.",
        "The number of infant deaths per thousand live births.",
        "The mean elevation at which the population lives.",
        "The total land area available for farming."],
      ans=0,
      why="A payment made by a government to families for each child is a government act, "
          "and EIN-1.B.1 names government acts and policies among the four things "
          "affecting total fertility rate."),

 dict(q="Four regions were recorded for mothers' access to healthcare and nutrition "
        "alongside infant deaths. What does the record establish?",
      table=_T_INFANT,
      choices=[
        "Infant deaths per thousand live births fall as both kinds of access rise.",
        "Infant deaths per thousand live births rise as both kinds of access rise.",
        "Infant deaths vary independently of both kinds of access in this record.",
        "Only the nutrition column moves with infant deaths; healthcare access does not.",
        "All four regions record the same number of infant deaths."],
      ans=0,
      why="Sorting the regions by either access column leaves infant deaths strictly "
          "falling. EIN-1.B.3 states that factors associated with infant mortality rates "
          "include whether mothers have access to good healthcare and nutrition."),

 dict(q="A student concludes from EIN-1.B.3 that a country's infant mortality rate cannot "
        "change. What is wrong with that reading?",
      choices=[
        "The framework states that changes in access to healthcare and nutrition can lead "
        "to changes in infant mortality rates over time.",
        "The framework states that infant mortality rates are fixed by the country's "
        "geography.",
        "The framework states that infant mortality rates change only when the total "
        "fertility rate changes.",
        "The framework makes no statement about infant mortality rates at all.",
        "The framework states that infant mortality rates change only where the "
        "population is growing."],
      ans=0,
      why="The second sentence of EIN-1.B.3 says exactly that changes in these factors can "
          "lead to changes in infant mortality rates over time, so the framework treats "
          "the rate as something that moves."),

 dict(q="One country was surveyed four times across thirty years for mothers' access to "
        "care and for infant deaths. What does the record establish?",
      table=_T_INFANT_TIME,
      choices=[
        "Access rose at each survey while infant deaths per thousand live births fell at "
        "each survey.",
        "Access fell at each survey while infant deaths per thousand live births rose at "
        "each survey.",
        "Both access and infant deaths rose at each survey.",
        "Both access and infant deaths fell at each survey.",
        "Neither column changed across the four surveys."],
      ans=0,
      why="Reading down the two columns, one rises at every survey and the other falls. "
          "EIN-1.B.3 states that changes in mothers' access to good healthcare can lead to "
          "changes in infant mortality rates over time."),

 dict(q="Across those thirty years, by how much did infant deaths per thousand live "
        "births change?",
      table=_T_INFANT_TIME,
      choices=[
        "They fell by 77.",
        "They fell by 19.",
        "They fell by 96.",
        "They rose by 77.",
        "They fell by 60."],
      ans=0,
      why="The first and last entries in the infant deaths column are subtracted. "
          "EIN-1.B.3 states that changes in the factors it names can lead to changes in "
          "infant mortality rates over time, which is the movement this record reports."),

 dict(q="Which study would test EIN-1.B.1's claim most directly?",
      choices=[
        "Recording the four things the framework names alongside total fertility rate "
        "across many populations, and looking for movement in fertility as each of them "
        "differs.",
        "Recording total fertility rate in a single population on a single occasion.",
        "Recording the land area and elevation of many countries alongside their fertility "
        "rates.",
        "Recording infant deaths per thousand live births in many countries and nothing "
        "else.",
        "Recording the number of species present in each country alongside its rainfall."],
      ans=0,
      why="EIN-1.B.1 asserts that four named things affect total fertility rate, so the "
          "evidence bearing on it varies those four across populations and watches the "
          "fertility rate, rather than measuring a single case or an unnamed quantity."),

 dict(q="Which single sentence collects what this topic's three statements assert and "
        "nothing further?",
      choices=[
        "Total fertility rate is affected by the age at first birth, educational "
        "opportunities for females, access to family planning and government acts and "
        "policies; a population at replacement level fertility is considered relatively "
        "stable; and mothers' access to healthcare and nutrition is associated with "
        "infant mortality rates, which can change as that access changes.",
        "Total fertility rate is affected by the climate and elevation of a region; a "
        "population at replacement level fertility is considered to be growing; and "
        "infant mortality rates are fixed for each country.",
        "Total fertility rate is affected only by government acts and policies, and "
        "nothing the framework says bears on infant mortality.",
        "A population at replacement level fertility is considered relatively stable, and "
        "the framework names no factor at all that affects total fertility rate.",
        "Mothers' access to healthcare and nutrition sets the total fertility rate "
        "directly, and replacement level fertility marks a declining population."],
      ans=0,
      why="EIN-1.B.1 supplies the four factors, EIN-1.B.2 the replacement level reading, "
          "and EIN-1.B.3 both the factors associated with infant mortality and the "
          "statement that changes in them can change that mortality over time."),
]
