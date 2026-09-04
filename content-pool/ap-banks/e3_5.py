# AP ENVIRONMENTAL SCIENCE 3.5 Population Growth and Resource Availability
# CED effective Fall 2026, Unit 3 Populations.
# Enduring understanding ERT-3: populations change over time in reaction to a variety of
# factors.
# Learning objective ERT-3.F: explain how resource availability affects population growth.
# Suggested skill 6.B, apply appropriate mathematical relationships to solve a problem.
#
# Essential knowledge relied on, in the framework's own words:
#   ERT-3.F.1  Population growth is limited by environmental factors, especially by the
#              available resources and space.
#   ERT-3.F.2  Resource availability and the total resource base are limited and finite over
#              all scales of time.
#   ERT-3.F.3  When the resources needed by a population for growth are abundant, population
#              growth usually accelerates.
#   ERT-3.F.4  When the resource base of a population shrinks, the increased potential for
#              unequal distribution of resources will ultimately result in increased
#              mortality, decreased fecundity, or both, resulting in population growth
#              declining to, or below, carrying capacity.
#
# THE SUGGESTED SKILL FOR THIS TOPIC IS A MATHEMATICAL ONE, so this module carries fifteen
# data items and every one of them is arithmetic a student can do in a step or two: a
# growth rate as a share of the starting count, a difference between two readings, a
# density, a running total. All of it is recomputed in verify_e3_5.py from the table alone.
#
# ERT-3.F.4 IS A CHAIN OF FOUR LINKS AND EACH IS KEYED SEPARATELY: the resource base
# SHRINKS; the POTENTIAL FOR UNEQUAL DISTRIBUTION rises; that results in INCREASED
# MORTALITY, DECREASED FECUNDITY, OR BOTH; and the result of that is population growth
# DECLINING TO, OR BELOW, CARRYING CAPACITY. Items 7, 8, 9, 10 and 11 take the links one at
# a time, and item 11 turns on TO OR BELOW, which allows the population to end under the
# capacity rather than settling exactly on it.
#
# THE HEDGES: ERT-3.F.3 says growth USUALLY accelerates, and ERT-3.F.4 says increased
# mortality, decreased fecundity, OR BOTH. Items 6 and 10 key those, and no key elsewhere
# hardens either.
#
# BOUNDARY WITH 3.4. Overshoot and the dieback that follows it are ERT-3.D.1 and ERT-3.E.1
# in topic 3.4. This topic is about what resource availability does to the RATE OF GROWTH,
# and item 12 marks the line rather than crossing it.
#
# NO FIGURES. Every quantitative item carries a table=.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("3.5", "Population Growth and Resource Availability", 3)

_T_ACCEL = dict(
    headers=["Period of the record", "Resource supply (index)",
             "Population at the start of the period", "Population at the end of the period"],
    rows=[["Period 1", "2", "500", "540"],
          ["Period 2", "5", "540", "660"],
          ["Period 3", "9", "660", "990"],
          ["Period 4", "14", "990", "1780"]])

_T_SHRINK = dict(
    headers=["Year of the record", "Resource base (index)",
             "Deaths per thousand individuals", "Offspring per female per year"],
    rows=[["Year 1", "100", "40", "3.2"],
          ["Year 5", "72", "65", "2.4"],
          ["Year 9", "41", "110", "1.5"],
          ["Year 13", "18", "180", "0.6"]])

_T_DECLINE = dict(
    headers=["Year of the record", "Population", "Carrying capacity (K)"],
    rows=[["Year 1", "1200", "1400"],
          ["Year 5", "1500", "1400"],
          ["Year 9", "1350", "1400"],
          ["Year 13", "1180", "1400"]])

_T_SPACE = dict(
    headers=["Enclosure", "Floor area available (square metres)",
             "Population the colony reached"],
    rows=[["Enclosure 1", "2", "40"],
          ["Enclosure 2", "6", "118"],
          ["Enclosure 3", "18", "352"],
          ["Enclosure 4", "54", "1060"]])

_T_FINITE = dict(
    headers=["Decade of the record", "Stock of the resource at the start (thousand tonnes)",
             "Amount used during the decade (thousand tonnes)"],
    rows=[["First", "900", "150"],
          ["Second", "750", "220"],
          ["Third", "530", "310"],
          ["Fourth", "220", "220"]])

_T_ABUNDANT = dict(
    headers=["Population", "Resource supply relative to need (percent)",
             "Annual growth rate (percent)"],
    rows=[["Population 1", "210", "6.4"],
          ["Population 2", "150", "4.1"],
          ["Population 3", "95", "0.7"],
          ["Population 4", "60", "-2.3"]])

_T_UNEQUAL = dict(
    headers=["Stage of the shortage",
             "Share of the food taken by the largest quarter of the herd (percent)",
             "Deaths per thousand individuals"],
    rows=[["Before the shortage", "28", "30"],
          ["Early in the shortage", "46", "75"],
          ["Late in the shortage", "71", "190"]])

QUESTIONS = [

 dict(q="What does the framework say limits population growth?",
      choices=[
        "Environmental factors, especially the available resources and space.",
        "The reproductive strategy of the species alone.",
        "The number of predators present, and nothing else.",
        "The age structure of the population alone.",
        "Nothing, since population growth is unlimited."],
      ans=0,
      why="ERT-3.F.1 states that population growth is limited by environmental factors, "
          "especially by the available resources and space. Both the general category and "
          "the two the statement singles out are its own words."),

 dict(q="Which two environmental factors does ERT-3.F.1 single out with the word "
        "ESPECIALLY?",
      choices=[
        "The available resources and space.",
        "Temperature and rainfall.",
        "Predation and disease.",
        "Salinity and sunlight.",
        "Soil depth and slope."],
      ans=0,
      why="ERT-3.F.1 names environmental factors in general and then singles out the "
          "available resources and space. The rejected pairs are conditions the framework "
          "discusses elsewhere but does not name here."),

 dict(q="What does the framework say about resource availability and the total resource "
        "base?",
      choices=[
        "They are limited and finite over all scales of time.",
        "They are limited in the short term but unlimited in the long term.",
        "They are unlimited in the short term but limited in the long term.",
        "They are unlimited over every scale of time.",
        "The framework makes no claim about them."],
      ans=0,
      why="ERT-3.F.2 states that resource availability and the total resource base are "
          "limited and finite over all scales of time. The phrase over all scales of time "
          "leaves no interval on which they are unlimited."),

 dict(q="What does ERT-3.F.2's phrase OVER ALL SCALES OF TIME rule out?",
      choices=[
        "Any interval, however long or short, on which resources could be treated as "
        "unlimited.",
        "Any measurement of resources over an interval shorter than a decade.",
        "Any comparison between two different resources.",
        "Any resource that can be renewed by natural processes.",
        "Any claim that resources vary from place to place."],
      ans=0,
      why="ERT-3.F.2 applies the words limited and finite over all scales of time, so no "
          "timescale is exempted. It says nothing about measurement intervals, comparisons, "
          "renewal or spatial variation."),

 dict(q="What does the framework say usually happens when the resources a population needs "
        "for growth are abundant?",
      choices=[
        "Population growth usually accelerates.",
        "Population growth usually slows.",
        "Population growth usually stops altogether.",
        "The population usually splits into smaller groups.",
        "The carrying capacity usually falls."],
      ans=0,
      why="ERT-3.F.3 states that when the resources needed by a population for growth are "
          "abundant, population growth usually accelerates. Acceleration is the direction "
          "the statement gives."),

 dict(q="ERT-3.F.3 says growth USUALLY accelerates when resources are abundant. What does "
        "that word establish?",
      choices=[
        "That acceleration is the usual result rather than one guaranteed in every case.",
        "That acceleration happens in every case without exception.",
        "That acceleration happens only in populations that have never been studied.",
        "That acceleration happens only after the resources have run out.",
        "That the framework is unsure whether resources affect growth."],
      ans=0,
      why="The statement is written with usually, which asserts what commonly happens "
          "rather than a rule without exceptions, while still committing the framework to "
          "the direction of the effect."),

 dict(q="According to ERT-3.F.4, what increases when the resource base of a population "
        "shrinks?",
      choices=[
        "The potential for unequal distribution of resources.",
        "The total resource base itself.",
        "The number of offspring each female produces.",
        "The carrying capacity of the habitat.",
        "The equality with which resources are shared."],
      ans=0,
      why="ERT-3.F.4 states that when the resource base shrinks, the increased potential for "
          "unequal distribution of resources will ultimately have consequences. The rising "
          "quantity is that potential for unequal distribution."),

 dict(q="What does ERT-3.F.4 say that increased potential for unequal distribution "
        "ultimately results in?",
      choices=[
        "Increased mortality, decreased fecundity, or both.",
        "Decreased mortality and increased fecundity.",
        "Increased mortality and increased fecundity together.",
        "A rise in the carrying capacity of the habitat.",
        "No change in the population at all."],
      ans=0,
      why="ERT-3.F.4 states that it will ultimately result in increased mortality, decreased "
          "fecundity, or both. Both named changes work against the population, and each "
          "rejected option reverses at least one direction."),

 dict(q="And what does ERT-3.F.4 say results from that increased mortality or decreased "
        "fecundity?",
      choices=[
        "Population growth declining to, or below, carrying capacity.",
        "Population growth rising above carrying capacity.",
        "Population growth holding at exactly its earlier rate.",
        "The carrying capacity declining to meet the population.",
        "The resource base returning to its earlier level."],
      ans=0,
      why="ERT-3.F.4 ends by stating that the result is population growth declining to, or "
          "below, carrying capacity. The population's growth is what declines, and it is "
          "measured against the carrying capacity."),

 dict(q="ERT-3.F.4 says increased mortality, decreased fecundity, OR BOTH. What does that "
        "phrasing allow in a particular case?",
      choices=[
        "Either change alone, or the two together.",
        "Only the two together, never one alone.",
        "Only one of the two, never both.",
        "Neither of the two, in most cases.",
        "The two in a fixed order, mortality first."],
      ans=0,
      why="The phrase or both admits each change on its own and admits them together, and "
          "the statement fixes no order between them."),

 dict(q="ERT-3.F.4 says growth declines TO, OR BELOW, carrying capacity. What does that "
        "allow?",
      choices=[
        "That the population may end up under the carrying capacity, not only exactly at it.",
        "That the population always settles exactly at the carrying capacity.",
        "That the population always ends above the carrying capacity.",
        "That the carrying capacity always rises to meet the population.",
        "That the population is never measured against the carrying capacity at all."],
      ans=0,
      why="The framework writes to, OR BELOW, which admits both landing points. A promise of "
          "settling exactly at the capacity is stronger than the statement, and the other "
          "options reverse it."),

 dict(q="How does this topic's claim differ from the framework's separate statement that "
        "overshoot is followed by a dieback?",
      choices=[
        "This topic is about how resource availability changes the rate of population "
        "growth, while that statement is about what follows a population exceeding its "
        "carrying capacity.",
        "This topic is about what follows a population exceeding its carrying capacity, "
        "while that statement is about how resource availability changes the rate of growth.",
        "The two make the same claim in different words.",
        "This topic concerns human populations and that statement concerns wildlife.",
        "This topic concerns a single generation and that statement concerns geological "
        "time."],
      ans=0,
      why="ERT-3.F.1 to ERT-3.F.4 concern the limits on growth and what abundance or "
          "shortage does to its rate. ERT-3.D.1 and ERT-3.E.1, in the carrying capacity "
          "topic, concern the overshoot condition and the dieback that follows it. The two "
          "begin at different points."),

 dict(q="One population was followed through four periods of differing resource supply. What "
        "does the record establish?",
      table=_T_ACCEL,
      choices=[
        "The population added more individuals in each successive period as the resource "
        "supply rose.",
        "The population added fewer individuals in each successive period as the resource "
        "supply rose.",
        "The population added the same number of individuals in every period.",
        "The population lost individuals in the periods of highest resource supply.",
        "The resource supply and the population change are unrelated in the record."],
      ans=0,
      why="The four periods add 40, 120, 330 and 790 individuals as the resource supply "
          "index runs 2, 5, 9 and 14. ERT-3.F.3 states that when the resources needed for "
          "growth are abundant, population growth usually accelerates."),

 dict(q="By what percent did that population grow during the fourth period?",
      table=_T_ACCEL,
      choices=["About 80 percent", "About 50 percent", "About 22 percent",
               "About 8 percent", "It did not grow"],
      ans=0,
      why="The population runs from 990 to 1,780 in that period, a gain of 790, and 790 "
          "divided by 990 is about 0.80. The rejected values are the growth rates of the "
          "other three periods."),

 dict(q="In which of those four periods did the population add the fewest individuals?",
      table=_T_ACCEL,
      choices=["Period 1", "Period 2", "Period 3", "Period 4",
               "All four periods added the same number"],
      ans=0,
      why="The four periods add 40, 120, 330 and 790 individuals, and the smallest gain "
          "belongs to the period of lowest resource supply. ERT-3.F.3 ties an accelerating "
          "growth to abundant resources."),

 dict(q="One population was followed as its resource base shrank. What do the two right hand "
        "columns establish?",
      table=_T_SHRINK,
      choices=[
        "Deaths rose and offspring per female fell as the resource base shrank.",
        "Deaths fell and offspring per female rose as the resource base shrank.",
        "Both deaths and offspring per female rose as the resource base shrank.",
        "Both deaths and offspring per female fell as the resource base shrank.",
        "Neither quantity changed as the resource base shrank."],
      ans=0,
      why="As the resource base index runs 100, 72, 41 and 18, deaths per thousand run 40, "
          "65, 110 and 180 while offspring per female run 3.2, 2.4, 1.5 and 0.6. ERT-3.F.4 "
          "states that a shrinking resource base ultimately results in increased mortality, "
          "decreased fecundity, or both, and here it is both."),

 dict(q="By how much did the death rate in that population change between the first and the "
        "last year of the record?",
      table=_T_SHRINK,
      choices=[
        "It rose by 140 per thousand", "It rose by 180 per thousand",
        "It fell by 140 per thousand", "It rose by 40 per thousand", "It did not change"],
      ans=0,
      why="Deaths per thousand run from 40 in the first year to 180 in the last, and 180 "
          "less 40 is 140. ERT-3.F.4 names increased mortality as one of the two results of "
          "a shrinking resource base."),

 dict(q="And by how much did the number of offspring per female change over the same years?",
      table=_T_SHRINK,
      choices=[
        "It fell by 2.6", "It rose by 2.6", "It fell by 3.2", "It fell by 0.6",
        "It did not change"],
      ans=0,
      why="Offspring per female run from 3.2 in the first year to 0.6 in the last, and 3.2 "
          "less 0.6 is 2.6. ERT-3.F.4 names decreased fecundity as the other of the two "
          "results of a shrinking resource base."),

 dict(q="One population was counted against its habitat's carrying capacity over thirteen "
        "years. What does the record establish?",
      table=_T_DECLINE,
      choices=[
        "The population rose above the carrying capacity and then declined to below it.",
        "The population stayed above the carrying capacity throughout.",
        "The population stayed below the carrying capacity throughout.",
        "The population settled exactly at the carrying capacity.",
        "The carrying capacity rose to meet the population."],
      ans=0,
      why="The population runs 1,200, 1,500, 1,350 and 1,180 against a constant carrying "
          "capacity of 1,400, so it passes above the capacity and finishes below it and "
          "below where it began. ERT-3.F.4 ends with population growth declining to, or "
          "below, carrying capacity."),

 dict(q="In which year of that record does the population stand furthest below the carrying "
        "capacity?",
      table=_T_DECLINE,
      choices=["The thirteenth year", "The first year", "The fifth year", "The ninth year",
               "The population is never below the carrying capacity"],
      ans=0,
      why="The shortfalls against the capacity of 1,400 are 200, none, 50 and 220 "
          "individuals. The largest belongs to the last year recorded, which is what "
          "ERT-3.F.4's phrase declining to, or BELOW, carrying capacity allows."),

 dict(q="Four colonies of one species were kept in enclosures of different floor area. What "
        "does the record establish?",
      table=_T_SPACE,
      choices=[
        "The colonies in larger enclosures reached larger populations.",
        "The colonies in larger enclosures reached smaller populations.",
        "Every colony reached the same population.",
        "Floor area and the population reached are unrelated in the record.",
        "The colony in the smallest enclosure reached the largest population."],
      ans=0,
      why="Ordered by floor area the populations reached run 40, 118, 352 and 1,060, rising "
          "at every step. ERT-3.F.1 states that population growth is limited by environmental "
          "factors, especially by the available resources and SPACE."),

 dict(q="What quantity is roughly the same across all four of those enclosures?",
      table=_T_SPACE,
      choices=[
        "The population reached for each square metre of floor, at about twenty.",
        "The population reached for each square metre of floor, at about two.",
        "The total population reached, at about four hundred.",
        "The floor area available, at about twenty square metres.",
        "Nothing in the record is roughly constant across the four."],
      ans=0,
      why="Dividing each population reached by its floor area gives 20, about 19.7, about "
          "19.6 and about 19.6 individuals per square metre. ERT-3.F.1 names space among the "
          "environmental factors that limit population growth, and a constant density is "
          "what limiting by space looks like in numbers."),

 dict(q="A resource stock was recorded over four decades of use. What does the record "
        "establish?",
      table=_T_FINITE,
      choices=[
        "The stock fell in every decade and was exhausted by the end of the record.",
        "The stock rose in every decade despite the use made of it.",
        "The stock was unchanged across the four decades.",
        "The stock fell in the first two decades and recovered in the last two.",
        "The record reports use but not the stock remaining."],
      ans=0,
      why="The stock at the start of each decade runs 900, 750, 530 and 220 thousand tonnes "
          "while 150, 220, 310 and 220 are used, and the last decade's use equals what was "
          "left. ERT-3.F.2 states that resource availability and the total resource base are "
          "limited and finite over all scales of time."),

 dict(q="How much of that resource was used in total across the four decades?",
      table=_T_FINITE,
      choices=[
        "900 thousand tonnes, the whole of the opening stock",
        "530 thousand tonnes, rather less than the opening stock",
        "220 thousand tonnes, the amount used in the last decade",
        "1,800 thousand tonnes, twice the opening stock",
        "The total cannot be formed from the record"],
      ans=0,
      why="Adding 150, 220, 310 and 220 gives 900 thousand tonnes, which is exactly the "
          "stock standing at the start of the first decade. ERT-3.F.2 describes the total "
          "resource base as limited and finite."),

 dict(q="Four populations were recorded for the resources available to them relative to what "
        "they need, and for their growth rates. What does the record establish?",
      table=_T_ABUNDANT,
      choices=[
        "The populations with more resources relative to need grew faster.",
        "The populations with more resources relative to need grew more slowly.",
        "All four populations grew at the same rate.",
        "None of the four populations grew at all.",
        "The population with the least resources relative to need grew fastest."],
      ans=0,
      why="Ordered by resource supply relative to need the growth rates run minus 2.3, 0.7, "
          "4.1 and 6.4 percent a year, rising at every step. ERT-3.F.3 states that when the "
          "resources needed for growth are abundant, population growth usually accelerates."),

 dict(q="Which of those four populations was shrinking rather than growing?",
      table=_T_ABUNDANT,
      choices=["Population 4 alone", "Population 1 alone", "Population 3 alone",
               "All four populations", "None of the four populations"],
      ans=0,
      why="One of the four records a growth rate of minus 2.3 percent a year while the other "
          "three are positive, and it is also the one whose resources fall furthest short of "
          "its needs. ERT-3.F.1 makes available resources a limit on population growth."),

 dict(q="A herd was followed through a shortage, with the share of the food taken by its "
        "largest quarter recorded alongside its death rate. What does the record establish?",
      table=_T_UNEQUAL,
      choices=[
        "As the food was shared more unequally, the death rate rose.",
        "As the food was shared more unequally, the death rate fell.",
        "As the food was shared more equally, the death rate rose.",
        "The share taken by the largest quarter did not change during the shortage.",
        "The death rate did not change during the shortage."],
      ans=0,
      why="The share taken by the largest quarter runs 28, 46 and 71 percent while deaths "
          "per thousand run 30, 75 and 190. ERT-3.F.4 states that a shrinking resource base "
          "brings an increased potential for unequal distribution of resources, which "
          "ultimately results in increased mortality, decreased fecundity, or both."),

 dict(q="Which set of measurements would test ERT-3.F.4's chain most directly?",
      choices=[
        "The size of the resource base, how evenly it is shared, the death rate, the "
        "offspring per female, and the population against its carrying capacity.",
        "The size of the resource base alone, recorded once.",
        "The number of predators and the number of competitors in the habitat.",
        "The average body size of the individuals in the population.",
        "The total area of the habitat in each year."],
      ans=0,
      why="ERT-3.F.4 runs from a shrinking resource base, through the potential for unequal "
          "distribution, to increased mortality or decreased fecundity, to growth declining "
          "to or below carrying capacity. Only the keyed set measures every link; each "
          "rejected option measures at most one thing the statement does not connect."),

 dict(q="Which of these does the framework NOT claim in this topic?",
      choices=[
        "That the resource base grows to match a population that needs more of it.",
        "That population growth is limited by environmental factors, especially resources "
        "and space.",
        "That resource availability is limited and finite over all scales of time.",
        "That abundant resources usually accelerate population growth.",
        "That a shrinking resource base ultimately raises mortality, lowers fecundity, or "
        "both."],
      ans=0,
      why="ERT-3.F.1 to ERT-3.F.4 supply the four rejected statements in their own words. "
          "None of them offers a resource base that grows to meet demand, and ERT-3.F.2 "
          "rules it out by calling the base limited and finite over all scales of time."),

 dict(q="Which single sentence collects what this topic's four statements assert and nothing "
        "further?",
      choices=[
        "Growth is limited by environmental factors, especially resources and space; "
        "resources are limited and finite over all scales of time; abundance usually "
        "accelerates growth; and a shrinking base raises the potential for unequal "
        "distribution, which raises mortality, lowers fecundity, or both, until growth "
        "declines to or below carrying capacity.",
        "Growth is limited only by predation; resources are unlimited over long timescales; "
        "abundance always accelerates growth; and a shrinking base lowers mortality and "
        "raises fecundity.",
        "Growth is limited by environmental factors, especially resources and space; "
        "resources are limited and finite over all scales of time; abundance usually slows "
        "growth; and a shrinking base raises mortality, lowers fecundity, or both.",
        "Growth is limited by environmental factors, especially resources and space; "
        "resources are limited in the short term only; abundance usually accelerates growth; "
        "and a shrinking base leaves growth unchanged.",
        "Growth is limited by environmental factors, especially resources and space; "
        "resources are limited and finite over all scales of time; abundance usually "
        "accelerates growth; and a shrinking base drives growth to settle exactly at "
        "carrying capacity and never below it."],
      ans=0,
      why="ERT-3.F.1 supplies the limit and the two factors, ERT-3.F.2 the finiteness over "
          "all scales of time, ERT-3.F.3 the hedged acceleration, and ERT-3.F.4 the whole "
          "chain ending in growth declining TO OR BELOW carrying capacity. Each rejected "
          "summary removes a limit, reverses a direction, exempts a timescale, or forbids "
          "the population to fall below the capacity."),
]
