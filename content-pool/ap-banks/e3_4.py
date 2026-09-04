# AP ENVIRONMENTAL SCIENCE 3.4 Carrying Capacity
# CED effective Fall 2026, Unit 3 Populations.
# Enduring understanding ERT-3: populations change over time in reaction to a variety of
# factors.
# Learning objectives ERT-3.D, describe carrying capacity, and ERT-3.E, describe the impact
# of carrying capacity on ecosystems. Suggested skill 5.E, explain what the data implies or
# illustrates about environmental issues.
#
# Essential knowledge relied on, in the framework's own words:
#   ERT-3.D.1  When a population exceeds its carrying capacity (carrying capacity can be
#              denoted as K), overshoot occurs. There are environmental impacts of
#              population overshoot, including resource depletion.
#   ERT-3.E.1  A major ecological effect of population overshoot is dieback of the
#              population (often severe to catastrophic) because the lack of available
#              resources leads to famine, disease, and conflict.
#
# WHAT ERT-3.D.1 DOES AND DOES NOT DO. It supplies the SYMBOL K, the CONDITION under which
# overshoot occurs -- a population exceeding its carrying capacity -- and one named
# environmental impact, RESOURCE DEPLETION. It does not define carrying capacity itself. So
# no key here states a definition of carrying capacity; item 11 keys the two things the
# statement does supply, and every distractor there is a claim the framework contradicts or
# never makes, never a true definition dressed up as an error.
#
# ERT-3.E.1's structure is the second half of the topic: the major ecological effect is
# DIEBACK, its severity is hedged as OFTEN SEVERE TO CATASTROPHIC, and its mechanism is the
# LACK OF AVAILABLE RESOURCES leading to FAMINE, DISEASE, AND CONFLICT. Items 5, 9 and 10
# turn on the hedge and on the fact that the three named consequences are alternatives as
# well as companions.
#
# BOUNDARY WITH 3.5. How resource availability limits population growth, and growth
# declining to or below carrying capacity, is ERT-3.F in topic 3.5. Nothing here is about
# the abundance of resources accelerating growth; every item here begins from a population
# that has already exceeded K.
#
# NO FIGURES. Population records are printed in a table= and every quantitative item is
# recomputed in verify_e3_4.py from that table alone.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("3.4", "Carrying Capacity", 3)

_T_OVERSHOOT = dict(
    headers=["Year of the record", "Herd size", "Carrying capacity of the range (K)"],
    rows=[["Year 1", "400", "900"],
          ["Year 4", "760", "900"],
          ["Year 7", "1150", "900"],
          ["Year 10", "1480", "900"],
          ["Year 13", "260", "900"]])

_T_FORAGE = dict(
    headers=["Year of the record", "Herd size",
             "Forage available per animal (kilograms per year)"],
    rows=[["Year 1", "400", "910"],
          ["Year 4", "760", "520"],
          ["Year 7", "1150", "230"],
          ["Year 10", "1480", "70"]])

_T_CAUSES = dict(
    headers=["Cause recorded for deaths during the dieback", "Number of animals"],
    rows=[["Starvation for want of forage", "620"],
          ["Disease", "410"],
          ["Injury in fights over the remaining forage", "190"]])

_T_MAGNITUDE = dict(
    headers=["Stage of the record", "Herd size"],
    rows=[["At the peak of the overshoot", "1480"],
          ["Two years after the peak", "260"]])

_T_TWO_HERDS = dict(
    headers=["Range", "Carrying capacity (K)", "Peak herd size reached",
             "Herd size ten years after the peak"],
    rows=[["Range 1", "900", "880", "870"],
          ["Range 2", "900", "1480", "260"]])

_T_DEPLETION = dict(
    headers=["Range", "Herd size as a percent of the carrying capacity",
             "Percent of the range's plant cover remaining after five years"],
    rows=[["Range A", "60", "96"],
          ["Range B", "95", "88"],
          ["Range C", "140", "54"],
          ["Range D", "180", "23"]])

QUESTIONS = [

 dict(q="What does the framework say happens when a population exceeds its carrying "
        "capacity?",
      choices=[
        "Overshoot occurs.",
        "The carrying capacity rises to meet the population.",
        "The population stops growing at once and holds steady.",
        "Nothing, because a population cannot exceed its carrying capacity.",
        "The population divides into two separate populations."],
      ans=0,
      why="ERT-3.D.1 states that when a population exceeds its carrying capacity, overshoot "
          "occurs. That is the word the framework gives to the condition, and the statement "
          "treats exceeding K as something that does happen."),

 dict(q="What symbol does the framework give for carrying capacity?",
      choices=["The letter K", "The letter r", "The letter N", "The letter B",
               "The framework gives no symbol for it"],
      ans=0,
      why="ERT-3.D.1 states in its own parenthesis that carrying capacity can be denoted as "
          "K. No other letter is offered for it in the statement."),

 dict(q="Which environmental impact of population overshoot does the framework name?",
      choices=["Resource depletion", "A rise in the carrying capacity",
               "An increase in the number of species present",
               "A permanent improvement in habitat quality",
               "A fall in the frequency of natural disruptions"],
      ans=0,
      why="ERT-3.D.1 states that there are environmental impacts of population overshoot, "
          "including resource depletion. Resource depletion is the one impact the statement "
          "names, and the word including leaves room for others without naming them."),

 dict(q="What does the framework identify as a major ecological effect of population "
        "overshoot?",
      choices=[
        "Dieback of the population.",
        "A rise in the population beyond all limits.",
        "A permanent change in the species' reproductive strategy.",
        "The immediate recovery of the depleted resources.",
        "The migration of the whole population to another continent."],
      ans=0,
      why="ERT-3.E.1 states that a major ecological effect of population overshoot is "
          "dieback of the population. Dieback is the framework's own term for what follows "
          "the overshoot."),

 dict(q="How does the framework describe the severity of that dieback?",
      choices=[
        "Often severe to catastrophic.",
        "Always mild and quickly reversed.",
        "Always total, leaving no survivors.",
        "Of a severity the framework does not comment on.",
        "Severe only where humans are present."],
      ans=0,
      why="ERT-3.E.1 describes the dieback, in its own parenthesis, as often severe to "
          "catastrophic. The word often makes that the usual range of severity rather than "
          "a guarantee in every case, and the statement does comment on severity."),

 dict(q="What does the framework give as the reason a dieback follows overshoot?",
      choices=[
        "The lack of available resources.",
        "The arrival of an invasive species.",
        "A change in the population's reproductive strategy.",
        "A fall in the number of predators.",
        "A rise in the carrying capacity of the habitat."],
      ans=0,
      why="ERT-3.E.1 states that the dieback follows BECAUSE the lack of available resources "
          "leads to famine, disease, and conflict. The shortage of resources is the cause "
          "the statement gives."),

 dict(q="Which three consequences of that lack of resources does the framework name?",
      choices=[
        "Famine, disease and conflict.",
        "Famine, migration and predation.",
        "Disease, conflict and mutation.",
        "Famine, disease and a rise in the birth rate.",
        "Conflict, migration and a fall in the carrying capacity."],
      ans=0,
      why="ERT-3.E.1 states that the lack of available resources leads to famine, disease, "
          "and conflict. Each rejected set replaces at least one of those three with "
          "something the statement does not name."),

 dict(q="A revision card lists four consequences of the lack of resources and calls all four "
        "framework consequences. Which one is not?",
      choices=["A rise in the birth rate", "Famine", "Disease", "Conflict",
               "All four are named by the framework"],
      ans=0,
      why="ERT-3.E.1 names famine, disease, and conflict. A rise in the birth rate is not "
          "among them, so a card carrying four items has one too many."),

 dict(q="ERT-3.E.1 says the lack of resources leads to famine, disease, and conflict. What "
        "does the framework's phrasing allow in a particular case?",
      choices=[
        "Any one of the three, or more than one, may be at work.",
        "All three must be at work together or none is.",
        "Exactly one of the three is at work in any case.",
        "None of the three is ever at work without human involvement.",
        "The three occur in a fixed order, famine first."],
      ans=0,
      why="ERT-3.E.1 lists the three as what the lack of resources leads to without "
          "requiring all of them at once or restricting a case to one, and it fixes no order "
          "among them."),

 dict(q="Overshoot, as the framework uses the word, is defined against what quantity?",
      choices=[
        "The population's carrying capacity.",
        "The population's size in the previous year.",
        "The population's biotic potential.",
        "The total area of the habitat.",
        "The number of predators the habitat holds."],
      ans=0,
      why="ERT-3.D.1 states that overshoot occurs when a population EXCEEDS ITS CARRYING "
          "CAPACITY, so carrying capacity is the quantity the population is measured "
          "against. The other quantities appear elsewhere in the framework and not in this "
          "statement."),

 dict(q="Which two things does ERT-3.D.1 state about carrying capacity?",
      choices=[
        "That it can be denoted K, and that a population exceeding it is in overshoot.",
        "That it rises every year, and that a population can never reach it.",
        "That it is the same for every species, and that it cannot be measured.",
        "That it cannot be exceeded, and that it is denoted r.",
        "That it is set by the number of predators, and that it falls when the population "
        "grows."],
      ans=0,
      why="ERT-3.D.1 supplies the symbol K in a parenthesis and states the condition under "
          "which overshoot occurs. Each rejected option asserts something the statement "
          "either contradicts, by saying a population can exceed K, or never mentions at "
          "all."),

 dict(q="A student writes that overshoot is harmless because the population simply returns "
        "to its earlier size. Which part of the framework contradicts that?",
      choices=[
        "The statement that a major ecological effect of overshoot is dieback, often severe "
        "to catastrophic.",
        "The statement that carrying capacity can be denoted K.",
        "The statement that populations change over time in reaction to a variety of "
        "factors.",
        "The statement that overshoot occurs when a population exceeds its carrying "
        "capacity.",
        "Nothing in the framework contradicts it."],
      ans=0,
      why="ERT-3.E.1 attaches a dieback, often severe to catastrophic, to population "
          "overshoot, and ERT-3.D.1 attaches resource depletion to it. A simple return to an "
          "earlier size is neither of those. The rejected options are true statements that "
          "do not bear on severity."),

 dict(q="A herd on one range was counted over thirteen years against the range's carrying "
        "capacity. In which years was the herd in overshoot?",
      table=_T_OVERSHOOT,
      choices=[
        "In the seventh and tenth years",
        "In the first and fourth years",
        "In the thirteenth year alone",
        "In every year of the record",
        "In none of the years of the record"],
      ans=0,
      why="The herd stands at 400, 760, 1,150, 1,480 and 260 against a carrying capacity of "
          "900, so it exceeds 900 in exactly two of the five years. ERT-3.D.1 states that "
          "overshoot occurs when a population exceeds its carrying capacity."),

 dict(q="By how much did that herd exceed the range's carrying capacity at its largest?",
      table=_T_OVERSHOOT,
      choices=["By 580 animals", "By 1,480 animals", "By 900 animals", "By 250 animals",
               "It never exceeded the carrying capacity"],
      ans=0,
      why="The largest herd recorded is 1,480 and the carrying capacity is 900, and 1,480 "
          "less 900 is 580. The rejected values are the two quantities themselves or a "
          "difference between other rows."),

 dict(q="What does that same herd record show happening after the largest count?",
      table=_T_OVERSHOOT,
      choices=[
        "The herd fell below the carrying capacity and below its own starting size.",
        "The herd held steady at its largest size.",
        "The herd settled exactly at the carrying capacity.",
        "The herd rose further above the carrying capacity.",
        "The herd fell but stayed above the carrying capacity."],
      ans=0,
      why="The herd reaches 1,480 and is then recorded at 260, which is below the carrying "
          "capacity of 900 and below the 400 it started at. ERT-3.E.1 states that a major "
          "ecological effect of population overshoot is dieback of the population, often "
          "severe to catastrophic."),

 dict(q="The same range was measured for forage as well as for herd size. What does the "
        "record establish?",
      table=_T_FORAGE,
      choices=[
        "The forage available to each animal fell as the herd grew.",
        "The forage available to each animal rose as the herd grew.",
        "The forage available to each animal was unchanged as the herd grew.",
        "The herd grew because the forage per animal was rising.",
        "The record reports forage but not herd size."],
      ans=0,
      why="Ordered by herd size the forage per animal runs 910, 520, 230 and 70 kilograms a "
          "year, falling at every step. ERT-3.D.1 names resource depletion among the "
          "environmental impacts of population overshoot."),

 dict(q="In that record, how much less forage was available to each animal at the largest "
        "herd size than at the smallest?",
      table=_T_FORAGE,
      choices=["840 kilograms a year", "910 kilograms a year", "70 kilograms a year",
               "290 kilograms a year", "1,080 kilograms a year"],
      ans=0,
      why="Forage per animal runs from 910 kilograms a year at the smallest herd to 70 at "
          "the largest, and 910 less 70 is 840. The rejected values are the two endpoints, a "
          "difference between other rows, or their sum."),

 dict(q="Deaths during one dieback were recorded by cause. What does the record establish?",
      table=_T_CAUSES,
      choices=[
        "All three of the consequences the framework names appear, in different numbers.",
        "Only one of the consequences the framework names appears.",
        "Two of the consequences the framework names appear and the third does not.",
        "The three consequences accounted for equal numbers of deaths.",
        "None of the consequences the framework names appears in the record."],
      ans=0,
      why="The record attributes deaths to starvation for want of forage, to disease and to "
          "injury in fights over the remaining forage, in three different numbers. ERT-3.E.1 "
          "states that the lack of available resources leads to famine, disease, and "
          "conflict."),

 dict(q="Which cause accounted for the most deaths in that dieback?",
      table=_T_CAUSES,
      choices=[
        "Starvation for want of forage", "Disease",
        "Injury in fights over the remaining forage",
        "The three causes were equal", "The record does not say"],
      ans=0,
      why="The three counts are 620, 410 and 190 animals, and the largest belongs to the "
          "first of the causes listed. The comparison is a direct reading of one column."),

 dict(q="A herd was counted at the peak of an overshoot and again two years later. By what "
        "share did it fall?",
      table=_T_MAGNITUDE,
      choices=["By about four fifths", "By about one fifth", "By about one half",
               "By about one tenth", "It did not fall"],
      ans=0,
      why="The herd falls from 1,480 to 260 animals, a loss of 1,220, which is about 82 "
          "percent of the peak. ERT-3.E.1 describes the dieback that follows overshoot as "
          "often severe to catastrophic."),

 dict(q="After that fall, how does the herd's size compare with its size at the peak?",
      table=_T_MAGNITUDE,
      choices=[
        "It is under a fifth of the peak size.",
        "It is about half the peak size.",
        "It is about three quarters of the peak size.",
        "It is larger than the peak size.",
        "It is exactly equal to the peak size."],
      ans=0,
      why="Two hundred and sixty animals out of a peak of 1,480 is under one fifth of it. "
          "ERT-3.E.1's phrase for a dieback of this kind is often severe to catastrophic."),

 dict(q="Two ranges of the same carrying capacity were followed. What does the record "
        "establish?",
      table=_T_TWO_HERDS,
      choices=[
        "Only the herd that rose above the carrying capacity suffered a collapse.",
        "Only the herd that stayed below the carrying capacity suffered a collapse.",
        "Both herds suffered a collapse.",
        "Neither herd suffered a collapse.",
        "The two ranges had different carrying capacities."],
      ans=0,
      why="One herd peaks at 880 against a carrying capacity of 900 and stands at 870 ten "
          "years later; the other peaks at 1,480 and stands at 260. ERT-3.D.1 makes "
          "exceeding the carrying capacity the condition for overshoot and ERT-3.E.1 makes "
          "dieback its major ecological effect."),

 dict(q="Which of those two herds never exceeded its range's carrying capacity?",
      table=_T_TWO_HERDS,
      choices=["The herd on Range 1", "The herd on Range 2", "Both herds exceeded it",
               "Neither herd exceeded it", "The record does not report the capacity"],
      ans=0,
      why="One herd's peak of 880 is below the capacity of 900 while the other's peak of "
          "1,480 is above it. ERT-3.D.1 defines the overshoot condition as the population "
          "exceeding its carrying capacity."),

 dict(q="Four ranges were scored for herd size relative to carrying capacity and for plant "
        "cover remaining. What does the record establish?",
      table=_T_DEPLETION,
      choices=[
        "Less plant cover remained on the ranges whose herds stood higher relative to the "
        "carrying capacity.",
        "More plant cover remained on the ranges whose herds stood higher relative to the "
        "carrying capacity.",
        "The same plant cover remained on all four ranges.",
        "Plant cover and herd size relative to capacity are unrelated across the ranges.",
        "The range with the largest herd relative to capacity kept the most plant cover."],
      ans=0,
      why="Ordered by herd size as a share of carrying capacity the plant cover remaining "
          "runs 96, 88, 54 and 23 percent, falling at every step. ERT-3.D.1 names resource "
          "depletion among the environmental impacts of population overshoot."),

 dict(q="Which of those four ranges carried herds in overshoot?",
      table=_T_DEPLETION,
      choices=[
        "Range C and Range D", "Range A and Range B", "Range D alone",
        "All four ranges", "None of the four ranges"],
      ans=0,
      why="Two of the four herds stand at 140 and 180 percent of the carrying capacity, "
          "which is above it, while the other two stand at 60 and 95 percent, which is "
          "below. ERT-3.D.1 makes exceeding the carrying capacity the condition for "
          "overshoot."),

 dict(q="Which of those ranges lost the most plant cover over the five years?",
      table=_T_DEPLETION,
      choices=["Range D", "Range A", "Range B", "Range C",
               "The four ranges lost the same amount"],
      ans=0,
      why="The plant cover remaining is 96, 88, 54 and 23 percent, so the largest loss "
          "belongs to the range retaining the least, which is also the range whose herd "
          "stands furthest above the carrying capacity."),

 dict(q="A range manager finds the herd standing well above the range's carrying capacity. "
        "What does the framework lead the manager to expect?",
      choices=[
        "Resource depletion, followed by a dieback of the herd.",
        "A rise in the range's carrying capacity to accommodate the herd.",
        "A steady herd at its present size for as long as the range lasts.",
        "An immediate improvement in the forage available to each animal.",
        "No consequence of any kind, since the herd is thriving."],
      ans=0,
      why="ERT-3.D.1 names resource depletion among the environmental impacts of overshoot "
          "and ERT-3.E.1 names dieback as its major ecological effect. Neither statement "
          "offers a rising capacity, a steady herd or an improvement in resources."),

 dict(q="Which observation would best support the claim that a herd's collapse followed from "
        "overshoot as the framework describes it?",
      choices=[
        "Records showing the herd above the range's carrying capacity, forage per animal "
        "falling, and deaths from starvation, disease and fighting.",
        "Records showing the number of predators on the range in each year.",
        "Records showing the herd's average body size in the year of the collapse.",
        "Records showing the age of the oldest animal in the herd.",
        "Records showing the total rainfall over the previous century."],
      ans=0,
      why="ERT-3.D.1 supplies the overshoot condition and resource depletion, and ERT-3.E.1 "
          "supplies the dieback and the famine, disease and conflict behind it. The keyed "
          "records are exactly those three elements; each rejected option measures something "
          "the two statements do not connect to overshoot."),

 dict(q="Which of these does the framework NOT claim about population overshoot?",
      choices=[
        "That the population always returns to exactly its carrying capacity afterwards.",
        "That it occurs when a population exceeds its carrying capacity.",
        "That resource depletion is among its environmental impacts.",
        "That dieback is a major ecological effect of it.",
        "That the lack of available resources leads to famine, disease and conflict."],
      ans=0,
      why="ERT-3.D.1 and ERT-3.E.1 together supply the condition, the depletion, the dieback "
          "and the three consequences. Neither states where the population settles "
          "afterwards, so a promise of an exact return is an addition to the framework."),

 dict(q="Which single sentence collects what this topic's two statements assert and nothing "
        "further?",
      choices=[
        "A population exceeding its carrying capacity, which may be denoted K, is in "
        "overshoot; overshoot depletes resources; and its major ecological effect is a "
        "dieback, often severe to catastrophic, because the lack of resources leads to "
        "famine, disease and conflict.",
        "A population exceeding its carrying capacity is in overshoot; overshoot raises the "
        "carrying capacity; and its major effect is a mild and quickly reversed decline.",
        "A population can never exceed its carrying capacity, which may be denoted K; "
        "overshoot depletes resources; and its major ecological effect is a dieback.",
        "A population exceeding its carrying capacity, which may be denoted K, is in "
        "overshoot; overshoot depletes resources; and its major ecological effect is a "
        "dieback caused by an increase in predators.",
        "A population exceeding its carrying capacity, which may be denoted K, is in "
        "overshoot; overshoot depletes resources; and the population always returns to "
        "exactly its carrying capacity afterwards."],
      ans=0,
      why="ERT-3.D.1 supplies the symbol, the overshoot condition and resource depletion, "
          "and ERT-3.E.1 supplies the dieback, its hedged severity and the famine, disease "
          "and conflict behind it. Each rejected summary denies that K can be exceeded, "
          "softens the dieback, swaps its cause, or adds a promise about where the "
          "population settles."),
]
