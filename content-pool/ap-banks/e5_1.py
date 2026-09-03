# AP ENVIRONMENTAL SCIENCE 5.1 The Tragedy of the Commons
# CED effective Fall 2026, Unit 5 Land and Water Use.
# Enduring understanding EIN-2: when humans use natural resources, they alter natural
# systems.
# Learning objective EIN-2.A: explain the concept of the tragedy of the commons.
# Suggested skill 1.B, explain environmental concepts and processes.
#
# Essential knowledge relied on, in the framework's own words:
#   EIN-2.A.1  The tragedy of the commons suggests that individuals will use shared
#              resources in their own self-interest rather than in keeping with the
#              common good, thereby depleting the resources.
#
# SCOPE. One sentence carries this topic, and it has exactly three moving parts: the
# resource is SHARED, each individual acts in SELF-INTEREST rather than for the common
# good, and the consequence is DEPLETION. Every key here turns on one of those three or
# on their combination. The framework proposes no remedy in this topic, names no author
# and no historical case, and does not say the outcome is inevitable -- it says the
# concept SUGGESTS this pattern. No key asserts more than that.
#
# BOUNDARY WITH THE REST OF UNIT 5. Overfishing is EIN-2.J.1 in topic 5.8, overgrazing
# is EIN-2.I.4 in topic 5.7, and aquifer depletion by irrigation is EIN-2.F.7 in topic
# 5.5. Those consequences are not asked here. What is asked here is the DECISION
# STRUCTURE the framework describes: shared access plus private benefit. Settings are
# deliberately spread across woodlots, groundwater, road space, a communal orchard and
# open water so that no single item repeats another topic's ground.
#
# NO FIGURES. Every quantitative item carries a table=; the arithmetic is a difference,
# a total or a per-user share, all calculator-free, and all recomputed in verify_e5_1.py.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("5.1", "The Tragedy of the Commons", 5)

_T_WOODLOT = dict(
    headers=["Year", "Number of households cutting firewood from the shared woodlot",
             "Standing timber remaining in the woodlot (tonnes)"],
    rows=[["Year 1", "12", "980"],
          ["Year 4", "20", "760"],
          ["Year 7", "31", "450"],
          ["Year 10", "44", "160"]])

_T_WELLS = dict(
    headers=["Year", "Number of wells drawing on the shared aquifer",
             "Depth to the water table (meters)"],
    rows=[["Year 1", "18", "22"],
          ["Year 5", "35", "31"],
          ["Year 9", "61", "47"],
          ["Year 13", "88", "68"]])

_T_PAYOFF = dict(
    headers=["Choice made by one herder",
             "Extra income to that herder over the season (units)",
             "Loss of forage spread across all forty herders (units)"],
    rows=[["Add no extra animal", "0", "0"],
          ["Add one extra animal", "40", "40"],
          ["Add four extra animals", "160", "160"]])

_T_OYSTER = dict(
    headers=["Bed", "Access rule",
             "Oysters harvested per hectare in the tenth year (kilograms)"],
    rows=[["Bed 1", "Open to all harvesters", "140"],
          ["Bed 2", "Open to all harvesters", "165"],
          ["Bed 3", "Harvest limited by an enforced quota", "610"],
          ["Bed 4", "Harvest limited by an enforced quota", "580"]])

_T_ORCHARD = dict(
    headers=["Season", "Fruit taken by the village in total (kilograms)",
             "Number of households taking fruit"],
    rows=[["Season 1", "1,200", "10"],
          ["Season 2", "1,600", "20"],
          ["Season 3", "1,800", "40"],
          ["Season 4", "1,600", "80"]])

QUESTIONS = [

 dict(q="Which statement expresses the concept of the tragedy of the commons as the course "
        "framework states it?",
      choices=[
        "Individuals will use shared resources in their own self-interest rather than in "
        "keeping with the common good, and the resources are depleted as a result.",
        "Individuals will refuse to use a shared resource at all until a government "
        "assigns each of them a portion of it.",
        "Shared resources are always used more efficiently than privately held ones "
        "because many people watch over them.",
        "A resource owned by one person is depleted faster than the same resource shared "
        "among many users.",
        "Resources are depleted only when the people using them are unaware that the "
        "resource is limited."],
      ans=0,
      why="EIN-2.A.1 states, near verbatim, that the tragedy of the commons suggests "
          "individuals will use shared resources in their own self-interest rather than in "
          "keeping with the common good, thereby depleting the resources. The rejected "
          "options reverse the direction of the effect or add an ignorance condition the "
          "framework does not state."),

 dict(q="Which feature must a resource have before the concept of the tragedy of the "
        "commons can apply to it?",
      choices=[
        "It must be shared, so that more than one user can draw on it",
        "It must be renewable, so that it grows back after every use",
        "It must be owned outright by a single household",
        "It must be located on land rather than in water",
        "It must be traded on an open market at a published price"],
      ans=0,
      why="EIN-2.A.1 speaks of SHARED resources, and the conflict it describes between "
          "self-interest and the common good has no meaning where a single owner bears the "
          "whole cost of use. The framework attaches no requirement about renewability, "
          "location or price."),

 dict(q="A group of neighbours each draw water from one aquifer that lies beneath all "
        "their land. Each pumps as much as suits their own farm, and the water table falls "
        "year after year. Which part of the framework's concept does the falling water "
        "table represent?",
      choices=[
        "The depletion of the resource that follows from many users each acting in "
        "their own interest",
        "The self-interest of an individual user, considered on its own",
        "The common good, which each user is deliberately protecting",
        "The shared character of the resource, considered on its own",
        "The absence of any connection between individual use and the state of "
        "the resource"],
      ans=0,
      why="EIN-2.A.1 names three things: shared use, self-interested behaviour, and the "
          "depletion that follows. The falling water table is the third of these, the outcome, "
          "rather than the shared character of the aquifer or the motive of any one user."),

 dict(q="A village woodlot is open to every household. The table records the households "
        "cutting there and the timber left standing. Which conclusion is best supported?",
      table=_T_WOODLOT,
      choices=[
        "As more households drew on the shared woodlot, the standing timber fell in "
        "every recorded interval.",
        "As more households drew on the shared woodlot, the standing timber rose in "
        "every recorded interval.",
        "The number of households and the standing timber were unrelated across "
        "the record.",
        "The standing timber fell only after the number of households began to decline.",
        "The standing timber was already zero when the record began, so nothing was "
        "depleted."],
      ans=0,
      why="The households rise from 12 to 44 while the standing timber falls from 980 to 160 "
          "tonnes, with no reversal in either column. EIN-2.A.1 describes exactly this: shared "
          "use in each user's own interest, thereby depleting the resource."),

 dict(q="Using the same woodlot record, how much standing timber was lost between the "
        "first and the last year recorded?",
      table=_T_WOODLOT,
      choices=[
        "820 tonnes",
        "980 tonnes",
        "530 tonnes",
        "160 tonnes",
        "1,140 tonnes"],
      ans=0,
      why="Subtracting the two tabulated figures gives 980 minus 160, which is 820 tonnes. "
          "The rejected values quote one of the two years on its own, pair the wrong years, "
          "or add the two figures instead of differencing them."),

 dict(q="Why does the framework describe the outcome it names as a tragedy rather than as "
        "a mistake?",
      choices=[
        "Each user's decision makes sense for that user even though the combined result "
        "harms everyone who depends on the resource.",
        "Each user knows the decision is wrong for them personally and makes it anyway.",
        "The outcome occurs only where users have miscalculated the size of the resource.",
        "The outcome occurs only where a single user has taken the whole resource by force.",
        "The outcome is impossible to describe in advance, so no one can be blamed for it."],
      ans=0,
      why="EIN-2.A.1 sets self-interest against the common good, which means the individually "
          "sensible choice and the collectively good choice come apart. The framework does not "
          "make the outcome depend on miscalculation, on force, or on the users acting against "
          "their own interest."),

 dict(q="A herder shares a pasture with thirty-nine others. The table shows what one "
        "herder gains and what the group loses for each choice. What does the comparison "
        "explain about the individual herder's incentive?",
      table=_T_PAYOFF,
      choices=[
        "The herder keeps the whole gain but bears only one fortieth of the loss, so "
        "adding animals is attractive to that herder.",
        "The herder keeps the whole gain and also bears the whole loss, so adding animals "
        "is unattractive to that herder.",
        "The herder receives none of the gain but bears the whole loss, so adding animals "
        "is unattractive to that herder.",
        "The gain and the loss are borne by different herders entirely, so no herder is "
        "affected by any other herder's choice.",
        "The table shows no gain from adding animals, so the herder has no reason to "
        "add any."],
      ans=0,
      why="The extra income goes to the one herder while the forage loss of the same size is "
          "spread across all forty, so the herder's share of the cost is a fortieth of the "
          "benefit. That asymmetry is the mechanism behind EIN-2.A.1's claim that individuals "
          "use shared resources in their own self-interest rather than for the common good."),

 dict(q="Using the same herder table, what extra income does one herder receive from adding "
        "four extra animals, and what share of the resulting forage loss falls on that "
        "herder alone?",
      table=_T_PAYOFF,
      choices=[
        "160 units of income and 4 units of the loss",
        "160 units of income and 160 units of the loss",
        "40 units of income and 4 units of the loss",
        "4 units of income and 160 units of the loss",
        "160 units of income and no loss at all"],
      ans=0,
      why="The table gives 160 units of extra income for four extra animals and a forage loss "
          "of 160 units spread across forty herders, and 160 divided by 40 is 4 units falling "
          "on the herder who added the animals. EIN-2.A.1 describes this gap between private "
          "benefit and shared cost."),

 dict(q="Which of the following situations does NOT fit the framework's description of the "
        "tragedy of the commons?",
      choices=[
        "A landowner harvests timber from a woodlot that only that landowner may enter "
        "and replants what is cut.",
        "Many fishing boats work the same stretch of open water and each lands as much "
        "as it can.",
        "Many households pump from one aquifer and each irrigates as much land as it can.",
        "Many herders graze one open pasture and each keeps as many animals as it can "
        "feed there.",
        "Many drivers use one free road and each makes as many trips as suits them."],
      ans=0,
      why="EIN-2.A.1 requires a SHARED resource, so that one user's gain is drawn from "
          "something others also depend on. Where a single owner both takes the whole benefit "
          "and bears the whole cost, the conflict between self-interest and the common good "
          "that the framework describes does not arise."),

 dict(q="A shared aquifer supplies a farming district. The table records the wells drawing "
        "on it and the depth a pump must reach to find water. What does the record show?",
      table=_T_WELLS,
      choices=[
        "The water table fell steadily as the number of wells drawing on the shared "
        "aquifer grew.",
        "The water table rose steadily as the number of wells drawing on the shared "
        "aquifer grew.",
        "The number of wells fell steadily while the water table stayed fixed.",
        "The water table changed only in the final interval recorded.",
        "The record shows no relationship between the number of wells and the depth to "
        "water."],
      ans=0,
      why="The wells rise from 18 to 88 while the depth to water grows from 22 to 68 meters, "
          "and a greater depth to water means less water remains within reach. EIN-2.A.1 "
          "describes shared resources being depleted as individuals draw on them in their "
          "own interest."),

 dict(q="From the same aquifer record, by how many meters did the depth to the water table "
        "increase over the whole period?",
      table=_T_WELLS,
      choices=[
        "46 meters",
        "68 meters",
        "37 meters",
        "21 meters",
        "90 meters"],
      ans=0,
      why="The depth grows from 22 meters to 68 meters, an increase of 46 meters. The rejected "
          "values quote the final depth alone, pair the wrong years, or add the first and last "
          "readings rather than differencing them."),

 dict(q="Four oyster beds of similar size and quality are managed under two different "
        "access rules. Which conclusion do the tenth-year harvests support?",
      table=_T_OYSTER,
      choices=[
        "The beds open to every harvester yielded far less in the tenth year than the "
        "beds under an enforced limit.",
        "The beds open to every harvester yielded far more in the tenth year than the "
        "beds under an enforced limit.",
        "All four beds yielded about the same amount in the tenth year.",
        "The two beds under an enforced limit yielded nothing at all in the tenth year.",
        "Access rules cannot be compared, because each bed had a different rule."],
      ans=0,
      why="The open beds returned 140 and 165 kilograms per hectare against 610 and 580 for "
          "the limited beds, a gap of several times. EIN-2.A.1 attributes depletion to shared "
          "resources used in each individual's own self-interest, and open access is what "
          "makes a resource shared in that sense."),

 dict(q="Which of the following best describes what the framework means by acting in one's "
        "own self-interest rather than in keeping with the common good?",
      choices=[
        "Taking the amount of the resource that is best for oneself, without regard to "
        "what is best for all the users together",
        "Taking the amount of the resource that keeps the total take within what the "
        "resource can support",
        "Refusing to take any of the resource so that others may have more of it",
        "Taking the resource only after every other user has agreed on a total limit",
        "Taking the resource and then compensating every other user for their share"],
      ans=0,
      why="EIN-2.A.1 contrasts the individual's own self-interest with the common good, so the "
          "behaviour it names is choosing by the private benefit alone. The four rejected "
          "options each describe a user who is taking the common good into account, which is "
          "the opposite of the behaviour described."),

 dict(q="A village orchard is open to all. The table records the total fruit taken and the "
        "number of households taking it. What pattern do the data show across the "
        "four seasons?",
      table=_T_ORCHARD,
      choices=[
        "The total taken stopped rising and then fell, even as the number of households "
        "taking fruit continued to double.",
        "The total taken rose in proportion to the number of households in every season.",
        "The total taken and the number of households both fell after the first season.",
        "The number of households stayed fixed while the total taken doubled each season.",
        "The total taken was highest in the season with the most households."],
      ans=0,
      why="The households run 10, 20, 40 and 80 while the totals run 1,200, 1,600, 1,800 and "
          "1,600 kilograms, so the total peaks in the third season and falls in the fourth "
          "despite the largest number of users. EIN-2.A.1 describes shared resources being "
          "depleted by use in each user's own interest."),

 dict(q="Using the same orchard record, what is the average amount of fruit taken per "
        "household in the fourth season?",
      table=_T_ORCHARD,
      choices=[
        "20 kilograms per household",
        "80 kilograms per household",
        "45 kilograms per household",
        "120 kilograms per household",
        "1,600 kilograms per household"],
      ans=0,
      why="Dividing the fourth season total of 1,600 kilograms by the 80 households taking "
          "fruit gives 20 kilograms each. The rejected values come from the wrong season, from "
          "the number of households itself, or from failing to divide at all."),

 dict(q="A student says the tragedy of the commons shows that people are careless. Which "
        "correction follows from the framework's own wording?",
      choices=[
        "The framework describes users acting in their own self-interest, which is "
        "deliberate rather than careless.",
        "The framework describes users who do not know that the resource exists.",
        "The framework describes users who act against their own interest by mistake.",
        "The framework describes users who have agreed in advance to deplete the resource.",
        "The framework describes a natural process in which human decisions play no part."],
      ans=0,
      why="EIN-2.A.1 says individuals use shared resources IN THEIR OWN SELF-INTEREST rather "
          "than in keeping with the common good, which is a description of purposeful choice. "
          "Carelessness, ignorance, error and agreement are all different accounts, and none "
          "of them appears in the statement."),

 dict(q="Which pair of conditions together produce the outcome the framework describes?",
      choices=[
        "Access shared among many users, and each user choosing by their own benefit",
        "Access held by one owner, and that owner choosing by their own benefit",
        "Access shared among many users, and every user choosing by the group's benefit",
        "Access held by one owner, and that owner choosing by the group's benefit",
        "Access shared among many users, and no user drawing on the resource at all"],
      ans=0,
      why="EIN-2.A.1 requires both a shared resource and self-interested use, and states that "
          "the two together deplete the resource. Removing either condition removes the "
          "conflict between individual benefit and common good that the concept rests on."),

 dict(q="An economist argues that a fishery held in common will be fished harder than an "
        "identical fishery owned by one company, even if the company is equally interested "
        "in profit. Which reasoning supports that argument from the framework?",
      choices=[
        "A single owner bears the whole future cost of taking too much today, while a "
        "shared user bears only a fraction of it.",
        "A single owner has no interest in profit, while shared users do.",
        "A shared fishery contains fewer fish at the outset than a privately held one.",
        "A single owner is prevented by law from taking any fish at all.",
        "Shared users always agree on a limit before fishing begins."],
      ans=0,
      why="EIN-2.A.1 turns on the gap between the private benefit of an extra unit taken and "
          "the shared cost of taking it, so concentrating both benefit and cost in one owner "
          "closes that gap. The stem holds the profit motive constant, and the framework "
          "makes no claim about starting stocks or legal prohibitions."),

 dict(q="Which observation would most directly show that a resource is being depleted in the "
        "way the framework describes?",
      choices=[
        "The amount each user is able to take falls year after year while the number of "
        "users rises.",
        "The number of users rises while the amount each user takes stays exactly the same.",
        "The amount each user takes rises while the number of users stays exactly the same.",
        "The resource is fenced and only one household is permitted to enter it.",
        "Users have signed an agreement setting a maximum total take."],
      ans=0,
      why="EIN-2.A.1 links many self-interested users of a shared resource to the depletion of "
          "that resource, so the diagnostic sign is a falling return to each user as the number "
          "of users grows. A fenced single-user resource is not shared, and an agreed maximum "
          "is a case where the common good is being taken into account."),

 dict(q="Which of the following is the clearest example of the shared resource the concept "
        "requires?",
      choices=[
        "A body of groundwater that lies beneath the land of many separate owners",
        "A rain barrel standing beside one house and filled only by that house's roof",
        "A bag of seed purchased by one farmer for that farmer's own field",
        "A tractor owned by one farm and used only on that farm",
        "A greenhouse built on one household's land and locked at night"],
      ans=0,
      why="EIN-2.A.1 applies to shared resources, and groundwater beneath many owners is "
          "drawn on by all of them so that each person's withdrawal reduces what remains for "
          "the rest. The four rejected items are each used and paid for by a single "
          "household."),

 dict(q="Which statement about the framework's claim is accurate?",
      choices=[
        "It says the concept suggests this pattern of use and depletion, not that the "
        "pattern is unavoidable in every case.",
        "It says the pattern occurs in every case where a resource is shared, without "
        "exception.",
        "It says the pattern never occurs where the users know one another.",
        "It says the pattern occurs only where the resource is nonrenewable.",
        "It says the pattern occurs only where the number of users exceeds one hundred."],
      ans=0,
      why="EIN-2.A.1 opens with the words the tragedy of the commons SUGGESTS, which is a "
          "claim about what the concept predicts rather than a guarantee about every shared "
          "resource. The framework attaches no threshold of users, no renewability condition "
          "and no requirement that users be strangers."),

 dict(q="Two districts share a single stretch of river for irrigation. Each district plans "
        "its withdrawals to maximise its own harvest, and by late summer the river runs "
        "too low for either. Which framework concept does the episode illustrate?",
      choices=[
        "The tragedy of the commons, because a shared resource was used in each user's own "
        "interest until it was depleted",
        "A rain shadow, because higher land blocked precipitation from reaching the river",
        "Sustainable yield, because each district took only what the river could replace",
        "The effect of axial tilt, because the shortage appeared in one season of the year",
        "Salinization, because evaporation left salts behind in the irrigated soil"],
      ans=0,
      why="The river is shared, each district chose by its own harvest, and the resource ran "
          "short, which are the three elements of EIN-2.A.1. A rain shadow is ENG-2.B.2, "
          "sustainable yield is STB-1.A.2 and describes the opposite behaviour, and "
          "salinization is EIN-2.F.6."),

 dict(q="If every user of a shared pasture voluntarily limited their herd to the number the "
        "pasture could support indefinitely, what would happen to the framework's "
        "prediction?",
      choices=[
        "The prediction would not be borne out, because the users would be acting in "
        "keeping with the common good rather than only their own interest.",
        "The prediction would still be borne out, because the framework makes depletion "
        "follow from sharing alone.",
        "The prediction would still be borne out, because voluntary limits always fail.",
        "The prediction could not be evaluated, because the framework applies only to "
        "water resources.",
        "The prediction would be strengthened, because limiting a herd increases the "
        "pressure on the pasture."],
      ans=0,
      why="EIN-2.A.1 makes depletion follow from self-interested use of a shared resource, so "
          "removing the self-interested behaviour removes the framework's stated cause. The "
          "framework does not claim that sharing alone depletes a resource, and it is not "
          "restricted to water."),

 dict(q="Which cost of one user's extra withdrawal from a shared resource does that user "
        "actually bear, according to the logic the framework describes?",
      choices=[
        "Only the share of the loss that falls on that user, while the rest falls on the "
        "other users",
        "The whole loss, because every unit taken is taken from that user's own stock",
        "None of the loss, because a shared resource cannot be reduced by use",
        "Twice the loss, because shared resources penalise heavy users",
        "The whole loss in the first year and none of it afterwards"],
      ans=0,
      why="A shared resource is drawn on by many, so a reduction caused by one user is spread "
          "across all of them, and that division of the cost is what makes self-interest point "
          "away from the common good in EIN-2.A.1. The rejected options either concentrate the "
          "whole cost on the one user or deny that use reduces the resource."),

 dict(q="A town council is told that its shared grazing land is showing the pattern the "
        "framework describes. Which piece of evidence would best support that "
        "identification?",
      choices=[
        "The land is open to all townspeople, the number of animals has risen, and the "
        "forage available per animal has fallen.",
        "The land is open to all townspeople and the number of animals has stayed the "
        "same for twenty years.",
        "The land belongs to one family, and the forage available per animal has fallen.",
        "The land is open to all townspeople and the forage available per animal has risen "
        "each year.",
        "The land is open to all townspeople, and no animals have grazed on it for a decade."],
      ans=0,
      why="EIN-2.A.1 requires all three of a shared resource, use that follows each user's own "
          "interest, and depletion, and only the keyed option reports all three. Each rejected "
          "option is missing the shared access, the rising use, or the falling condition of the "
          "resource."),

 dict(q="How does the concept explain a situation in which every user agrees that the "
        "resource is being ruined and yet no user reduces their own take?",
      choices=[
        "Each user's own take is a small part of the total, so restraint by one user costs "
        "that user a great deal and saves the resource very little.",
        "Each user believes the resource is unlimited, so restraint appears pointless "
        "to them.",
        "Each user is legally forbidden to reduce their take.",
        "Each user gains more from restraint than from continued use, so the situation "
        "cannot arise.",
        "Each user is unaware that other users exist."],
      ans=0,
      why="EIN-2.A.1 sets the individual's self-interest against the common good, and the "
          "situation described is exactly that conflict persisting even where the common good "
          "is understood. The rejected options replace the conflict with ignorance, with a "
          "legal barrier, or with an assumption that removes the conflict altogether."),

 dict(q="In the oyster comparison, what is the difference between the average tenth-year "
        "yield of the beds open to all harvesters and the average yield of the beds under "
        "an enforced limit?",
      table=_T_OYSTER,
      choices=[
        "443 kilograms per hectare",
        "152 kilograms per hectare",
        "595 kilograms per hectare",
        "470 kilograms per hectare",
        "748 kilograms per hectare"],
      ans=0,
      why="The open beds average 140 and 165, which is 152.5 kilograms per hectare, and the "
          "limited beds average 610 and 580, which is 595, so the gap is 442.5 and rounds to "
          "443. The rejected values are the two averages themselves, a difference taken "
          "between the wrong pair of beds, or the sum of the two averages."),

 dict(q="Which of the following is the best statement of why the framework places this "
        "concept in a unit about land and water use?",
      choices=[
        "Land and water are commonly shared among many users, so the pattern of "
        "self-interested use and depletion has room to operate there.",
        "Land and water are the only resources that can be owned by a single person.",
        "Land and water are unaffected by human decisions, so no other concept applies "
        "to them.",
        "Land and water cannot be depleted, so the concept serves only as a warning "
        "about other resources.",
        "Land and water are always managed by governments, which removes any role for "
        "individual choice."],
      ans=0,
      why="The enduring understanding EIN-2 states that when humans use natural resources they "
          "alter natural systems, and EIN-2.A.1 applies to shared resources, which pastures, "
          "forests, fisheries and groundwater commonly are. The rejected options deny that "
          "these resources can be depleted or that individuals make choices about them."),

 dict(q="Compare the woodlot record with the aquifer record. What do the two have in common "
        "as illustrations of the concept?",
      table=_T_WELLS,
      choices=[
        "In each, the number of users drawing on one shared stock rose while the stock "
        "available to them fell.",
        "In each, the number of users fell while the stock available to them rose.",
        "In each, the stock available stayed constant while the number of users changed.",
        "In each, a single owner controlled the resource throughout the period recorded.",
        "In each, the resource was replenished faster than it was drawn down."],
      ans=0,
      why="The aquifer record shows wells rising from 18 to 88 as the depth to water grows from "
          "22 to 68 meters, so less water lies within reach as more users draw on it, and the "
          "woodlot record has the same shape. EIN-2.A.1 attributes this joint movement to "
          "shared use in each user's own interest."),

 dict(q="Which summary correctly relates the three elements of the framework's sentence to "
        "one another?",
      choices=[
        "Shared access allows many users in; self-interest governs how much each takes; "
        "depletion is the result of the two together.",
        "Depletion causes users to share the resource; sharing then produces self-interest.",
        "Self-interest causes a resource to become shared; sharing then prevents depletion.",
        "Shared access prevents depletion; self-interest is what restores the resource.",
        "The three elements are independent of one another and never occur in the "
        "same case."],
      ans=0,
      why="EIN-2.A.1 states that individuals will use SHARED resources in their own "
          "SELF-INTEREST rather than in keeping with the common good, THEREBY DEPLETING the "
          "resources, which orders the three as condition, behaviour and consequence. The "
          "rejected summaries reverse that order or deny the connection."),
]
