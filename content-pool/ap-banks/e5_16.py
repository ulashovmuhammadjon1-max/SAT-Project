# AP ENVIRONMENTAL SCIENCE 5.16 Aquaculture
# CED effective Fall 2026, Unit 5 Land and Water Use.
# Enduring understanding STB-1: humans can mitigate their impact on land and water
# resources through sustainable use.
# Learning objective STB-1.F, describe the benefits and drawbacks of aquaculture.
# Suggested skill 7.C, describe disadvantages, advantages, or unintended consequences for
# potential solutions.
#
# Essential knowledge relied on, in the framework's own words:
#   STB-1.F.1  Aquaculture has expanded because it is highly efficient, requires only
#              small areas of water, and requires little fuel.
#   STB-1.F.2  Aquaculture can contaminate wastewater, and fish that escape may compete or
#              breed with wild fish. The density of fish in aquaculture can lead to
#              increases in disease incidences, which can be transmitted to wild fish.
#
# SCOPE. Three reasons for the expansion and three drawbacks, and nothing else. The
# reasons are high efficiency, only small areas of water, and little fuel. The drawbacks
# are contaminated wastewater; escaped fish that may COMPETE OR BREED with wild fish; and
# disease incidences that follow from THE DENSITY OF FISH and can be transmitted to wild
# fish. The framework names no species, no country, no year and no figure, and gives no
# number, so every quantitative item here prints its data in a table and the arithmetic is
# recomputed in verify_e5_16.py from that table alone.
#
# THE HEDGES. STB-1.F.2 says aquaculture CAN contaminate wastewater, that escapees MAY
# compete or breed, and that density CAN lead to increases in disease. Every one is a
# possibility rather than a certainty, and one item keys that. No key here says
# aquaculture always does any of the three.
#
# THE CLAUSE THAT IS EASY TO HALVE. Escapees MAY COMPETE OR BREED with wild fish -- two
# consequences, not one. Competition is ecological and interbreeding is genetic, and a
# student who has met only the first will reject the second. Two items turn on it and
# their anchors carry both verbs.
#
# THE CAUSE THAT IS EASY TO MISPLACE. The framework attributes rising disease to THE
# DENSITY OF FISH IN AQUACULTURE, not to the water, the feed or the species. One item
# keys that, with each distractor putting the cause somewhere else.
#
# BOUNDARY WITH 5.8. Overfishing, the extreme scarcity of some fish species, lessened
# biodiversity in aquatic systems and harm to people who depend on fishing are EIN-2.J.1
# in topic 5.8. None of it is keyed here; aquaculture is the practice, not the shortage
# that motivates it.
#
# NO FIGURES. Every quantitative item carries a table=; all arithmetic is recomputed in
# verify_e5_16.py from that table alone and is calculator-free.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("5.16", "Aquaculture", 5)

_T_INPUTS = dict(
    headers=["Method of producing fish",
             "Water area used per tonne of fish produced (hectares)",
             "Fuel used per tonne of fish produced (litres)"],
    rows=[["Aquaculture in ponds and cages", "0.4", "95"],
          ["Coastal fishing fleet", "60", "475"],
          ["Distant-water fishing fleet", "310", "950"]])

_T_FEED = dict(
    headers=["Animal farmed",
             "Feed eaten per kilogram of body mass gained (kilograms)",
             "Share of the feed converted to edible flesh (percent)"],
    rows=[["Farmed fish", "1.2", "46"],
          ["Farmed poultry", "2.4", "33"],
          ["Farmed cattle", "6.0", "13"]])

_T_WASTE = dict(
    headers=["Water sampled at the fish farm",
             "Nitrogen (milligrams per litre)",
             "Suspended solids (milligrams per litre)"],
    rows=[["Water entering the ponds", "0.9", "6"],
          ["Water leaving the ponds", "7.2", "54"]])

_T_ESCAPE = dict(
    headers=["Year of the survey",
             "Farmed fish that escaped that year (thousands)",
             "Share of the river's spawning fish of farmed origin (percent)"],
    rows=[["Year 1", "4", "2"],
          ["Year 5", "19", "11"],
          ["Year 10", "46", "28"]])

_T_DENSITY = dict(
    headers=["Cage stocked",
             "Stocking density (fish per cubic meter)",
             "Fish showing the disease at harvest (percent)"],
    rows=[["Cage 1", "5", "3"],
          ["Cage 2", "15", "11"],
          ["Cage 3", "30", "26"],
          ["Cage 4", "60", "52"]])

_T_WILD = dict(
    headers=["Site sampled",
             "Distance from the fish cages (kilometers)",
             "Wild fish carrying the parasite (percent)"],
    rows=[["Site 1", "1", "38"],
          ["Site 2", "5", "21"],
          ["Site 3", "15", "9"],
          ["Site 4", "40", "3"]])

QUESTIONS = [

 dict(q="Which three reasons does the course framework give for the expansion of "
        "aquaculture?",
      choices=[
        "It is highly efficient, requires only small areas of water, and requires little "
        "fuel",
        "It is highly efficient, requires large areas of water, and requires a great deal of "
        "fuel",
        "It is inefficient, but requires only small areas of water and little fuel",
        "It removes the need to catch any wild fish and eliminates disease in farmed stock",
        "It raises the price of fish and lowers the cost of fishing boats"],
      ans=0,
      why="STB-1.F.1 states that aquaculture has expanded BECAUSE IT IS HIGHLY EFFICIENT, "
          "REQUIRES ONLY SMALL AREAS OF WATER, AND REQUIRES LITTLE FUEL. Each rejected option "
          "reverses one of the three reasons or replaces them with claims the framework never "
          "makes."),

 dict(q="Which of the following is NOT among the reasons the framework gives for the "
        "expansion of aquaculture?",
      choices=[
        "That it eliminates disease among the fish being raised",
        "That it is highly efficient",
        "That it requires only small areas of water",
        "That it requires little fuel",
        "That it is efficient and uses little fuel at once"],
      ans=0,
      why="STB-1.F.1 gives efficiency, small areas of water and little fuel. Far from claiming "
          "that disease is eliminated, STB-1.F.2 states that the density of fish in aquaculture "
          "can lead to INCREASES in disease incidences."),

 dict(q="What does the framework say aquaculture can do to wastewater?",
      choices=[
        "It can contaminate it",
        "It can purify it",
        "It can remove all nitrogen from it",
        "It can reduce the volume of it to nothing",
        "The framework says nothing about wastewater"],
      ans=0,
      why="STB-1.F.2 opens by stating that AQUACULTURE CAN CONTAMINATE WASTEWATER. The rejected "
          "options reverse the effect or deny that the statement exists."),

 dict(q="According to the framework, what may fish that escape from aquaculture do?",
      choices=[
        "Compete or breed with wild fish",
        "Compete with wild fish, but never breed with them",
        "Breed with wild fish, but never compete with them",
        "Return to the farm of their own accord within a season",
        "Die immediately, so that no effect on wild fish is possible"],
      ans=0,
      why="STB-1.F.2 states that fish that escape MAY COMPETE OR BREED WITH WILD FISH, which is "
          "two consequences rather than one: an ecological one and a genetic one. The first two "
          "rejected options each keep one and deny the other."),

 dict(q="To what does the framework attribute increases in disease incidence in aquaculture?",
      choices=[
        "The density of fish in aquaculture",
        "The temperature of the water in aquaculture",
        "The species of fish chosen for aquaculture",
        "The fuel used by the boats that service the cages",
        "The small area of water that aquaculture requires"],
      ans=0,
      why="STB-1.F.2 states that THE DENSITY OF FISH IN AQUACULTURE can lead to increases in "
          "disease incidences. Temperature, species and fuel appear nowhere in the statement, "
          "and the small area of water is one of STB-1.F.1's reasons for the expansion rather "
          "than a cause of disease."),

 dict(q="What further consequence does the framework attach to those disease incidences?",
      choices=[
        "They can be transmitted to wild fish",
        "They can be transmitted to the wastewater but not to any fish",
        "They remain confined to the farm in every case",
        "They reduce the density of fish until the disease disappears",
        "They make the escaped fish unable to breed with wild fish"],
      ans=0,
      why="STB-1.F.2 states that the increases in disease incidences CAN BE TRANSMITTED TO WILD "
          "FISH. The framework does not confine them to the farm, and it separately states that "
          "escapees may breed with wild fish."),

 dict(q="Which of the framework's drawbacks concerns the genetic make-up of a wild "
        "population rather than its numbers?",
      choices=[
        "That escaped farmed fish may breed with wild fish",
        "That escaped farmed fish may compete with wild fish",
        "That aquaculture can contaminate wastewater",
        "That the density of fish can raise disease incidence",
        "That aquaculture requires only small areas of water"],
      ans=0,
      why="Interbreeding mixes farmed and wild stock, which is a change in what the wild "
          "population is rather than in how many there are; STB-1.F.2 names it alongside "
          "competition. Contaminated wastewater and density-driven disease are the statement's "
          "other drawbacks, and small water area is one of STB-1.F.1's benefits."),

 dict(q="Three ways of producing fish are compared in the table. Which reading matches the "
        "framework's reasons for the expansion of aquaculture?",
      table=_T_INPUTS,
      choices=[
        "Aquaculture uses far less water area and far less fuel for each tonne of fish than "
        "either fishing fleet.",
        "Aquaculture uses far more water area and far more fuel for each tonne of fish than "
        "either fishing fleet.",
        "Aquaculture uses less water area but more fuel for each tonne of fish than either "
        "fishing fleet.",
        "The three methods use the same water area for each tonne of fish.",
        "The distant-water fleet uses the least fuel for each tonne of fish."],
      ans=0,
      why="Aquaculture uses 0.4 hectares and 95 litres per tonne against 60 hectares and 475 "
          "litres for the coastal fleet and 310 hectares and 950 litres for the distant-water "
          "fleet. STB-1.F.1 gives only small areas of water and little fuel among its reasons "
          "for the expansion."),

 dict(q="Using the same three methods, how much fuel does the distant-water fleet use for each "
        "tonne of fish compared with aquaculture?",
      table=_T_INPUTS,
      choices=[
        "Ten times as much",
        "Five times as much",
        "Two times as much",
        "Thirteen times as much",
        "The same amount"],
      ans=0,
      why="Dividing the two tabulated figures gives 950 divided by 95, which is 10. The rejected "
          "values compare the coastal fleet with aquaculture, compare the two fleets with each "
          "other, or deny that the methods differ."),

 dict(q="Three farmed animals are compared for how they use their feed. Which reading supports "
        "the framework's first reason for the expansion of aquaculture?",
      table=_T_FEED,
      choices=[
        "Farmed fish need the least feed for each kilogram gained and turn the largest share "
        "of it into edible flesh.",
        "Farmed fish need the most feed for each kilogram gained and turn the smallest share "
        "of it into edible flesh.",
        "Farmed fish need the least feed for each kilogram gained but turn the smallest share "
        "of it into edible flesh.",
        "The three animals need the same feed for each kilogram gained.",
        "Farmed cattle turn the largest share of their feed into edible flesh."],
      ans=0,
      why="Fish need 1.2 kilograms of feed per kilogram gained against 2.4 for poultry and 6.0 "
          "for cattle, and convert 46 percent to edible flesh against 33 and 13. STB-1.F.1's "
          "first reason for the expansion is that aquaculture is HIGHLY EFFICIENT."),

 dict(q="Using the same three animals, how much feed do farmed cattle need for each kilogram "
        "gained compared with farmed fish?",
      table=_T_FEED,
      choices=[
        "Five times as much",
        "Two times as much",
        "Three times as much",
        "Six times as much",
        "The same amount"],
      ans=0,
      why="Dividing the two tabulated figures gives 6.0 divided by 1.2, which is 5. The rejected "
          "values compare poultry with fish, quote the cattle figure alone, or deny that the "
          "animals differ."),

 dict(q="Water was sampled entering and leaving one fish farm's ponds. What do the values "
        "show?",
      table=_T_WASTE,
      choices=[
        "The water leaving the ponds carried far more nitrogen and far more suspended solids "
        "than the water entering them.",
        "The water leaving the ponds carried far less nitrogen and far fewer suspended "
        "solids than the water entering them.",
        "The water leaving carried more nitrogen but fewer suspended solids than the water "
        "entering.",
        "The two samples carried the same nitrogen and the same suspended solids.",
        "The water entering the ponds carried the most nitrogen of the two."],
      ans=0,
      why="Nitrogen rises from 0.9 to 7.2 milligrams per litre and suspended solids from 6 to 54 "
          "across the ponds. STB-1.F.2 states that aquaculture can contaminate wastewater, and "
          "water leaving dirtier than it arrived is that contamination measured."),

 dict(q="Using the same two samples, how much nitrogen did the water leaving the ponds carry "
        "compared with the water entering them?",
      table=_T_WASTE,
      choices=[
        "Eight times as much",
        "Nine times as much",
        "Six times as much",
        "Two times as much",
        "The same amount"],
      ans=0,
      why="Dividing the two tabulated concentrations gives 7.2 divided by 0.9, which is 8. The "
          "rejected values come from the suspended solids column, from the entering "
          "concentration, or from denying that the samples differ."),

 dict(q="Escapes from a river's fish farms were recorded alongside the spawning fish in the "
        "river. Which conclusion is best supported?",
      table=_T_ESCAPE,
      choices=[
        "As more farmed fish escaped, a larger share of the river's spawning fish were of "
        "farmed origin.",
        "As more farmed fish escaped, a smaller share of the river's spawning fish were of "
        "farmed origin.",
        "The share of spawning fish of farmed origin stayed level as escapes rose.",
        "Escapes fell across the ten years while the farmed share of spawners rose.",
        "Escaped farmed fish cannot be detected among a river's spawning fish."],
      ans=0,
      why="Escapes run 4, 19 and 46 thousand while the farmed share of spawners runs 2, 11 and "
          "28 percent. STB-1.F.2 states that fish that escape may compete or breed with wild "
          "fish, and farmed fish appearing among the spawners is the breeding half of that."),

 dict(q="Using the same river, by how much did the share of spawning fish of farmed origin "
        "rise across the ten years?",
      table=_T_ESCAPE,
      choices=[
        "By 26 percentage points",
        "By 28 percentage points",
        "By 30 percentage points",
        "By 42 percentage points",
        "By 11 percentage points"],
      ans=0,
      why="Subtracting the two tabulated shares gives 28 minus 2, which is 26 percentage points. "
          "The rejected values quote the final share alone, add the two, take the rise in the "
          "escapes column, or quote the middle year."),

 dict(q="Four cages stocked at different densities were inspected at harvest. What "
        "relationship do the values show?",
      table=_T_DENSITY,
      choices=[
        "The more densely a cage was stocked, the larger the share of fish showing the "
        "disease.",
        "The more densely a cage was stocked, the smaller the share of fish showing the "
        "disease.",
        "The share of fish showing the disease was the same in all four cages.",
        "The most thinly stocked cage held the largest share of diseased fish.",
        "Stocking density and disease cannot be compared across cages."],
      ans=0,
      why="Density runs 5, 15, 30 and 60 fish per cubic meter against disease shares of 3, 11, "
          "26 and 52 percent. STB-1.F.2 states that THE DENSITY OF FISH IN AQUACULTURE can lead "
          "to increases in disease incidences."),

 dict(q="Using the same four cages, how much larger was the diseased share in the most densely "
        "stocked cage than in the most thinly stocked one?",
      table=_T_DENSITY,
      choices=[
        "49 percentage points larger",
        "52 percentage points larger",
        "55 percentage points larger",
        "26 percentage points larger",
        "3 percentage points larger"],
      ans=0,
      why="Subtracting the two tabulated shares gives 52 minus 3, which is 49 percentage points. "
          "The rejected values quote the densest cage alone, add the two, quote a middle cage, "
          "or quote the thinnest cage alone."),

 dict(q="Wild fish were sampled at four distances from a group of fish cages. Which conclusion "
        "do the values support?",
      table=_T_WILD,
      choices=[
        "The parasite was commonest in the wild fish nearest the cages and rarer with "
        "distance from them.",
        "The parasite was rarest in the wild fish nearest the cages and commoner with "
        "distance from them.",
        "The parasite was equally common in wild fish at all four distances.",
        "The parasite was found only in fish more than forty kilometers from the cages.",
        "A parasite carried by farmed fish cannot appear in wild fish at all."],
      ans=0,
      why="Distances run 1, 5, 15 and 40 kilometers while the share of wild fish carrying the "
          "parasite runs 38, 21, 9 and 3 percent. STB-1.F.2 states that increases in disease "
          "incidences can be TRANSMITTED TO WILD FISH."),

 dict(q="Using the same four sites, how much commoner was the parasite in the wild fish "
        "nearest the cages than in those farthest away?",
      table=_T_WILD,
      choices=[
        "35 percentage points commoner",
        "38 percentage points commoner",
        "41 percentage points commoner",
        "29 percentage points commoner",
        "17 percentage points commoner"],
      ans=0,
      why="Subtracting the two tabulated shares gives 38 minus 3, which is 35 percentage points. "
          "The rejected values quote the nearest site alone, add the two, or compare the nearest "
          "site with one of the two middle sites instead of the farthest."),

 dict(q="A student writes that the framework presents aquaculture purely as a source of harm. "
        "Which correction is required?",
      choices=[
        "The framework also gives three reasons for its expansion: efficiency, small areas "
        "of water, and little fuel",
        "The framework gives no reasons for its expansion, so the student is correct",
        "The framework gives one reason for its expansion, which is that it needs little "
        "fuel",
        "The framework presents aquaculture purely as a benefit and names no drawback",
        "The framework declines to describe aquaculture at all"],
      ans=0,
      why="STB-1.F.1 supplies three reasons for the expansion before STB-1.F.2 supplies the "
          "drawbacks, so the framework carries both sides. Reducing the reasons to one, or "
          "denying the drawbacks, both misreport it."),

 dict(q="A second student writes that escaped farmed fish can only compete with wild fish and "
        "never interbreed. Which correction is required?",
      choices=[
        "The framework says escapees may compete OR BREED with wild fish",
        "The framework says escapees may breed with wild fish but never compete with them",
        "The framework says escapees cannot survive outside the farm",
        "The framework says escapees affect only the wastewater leaving the farm",
        "The framework makes no statement about escaped fish"],
      ans=0,
      why="STB-1.F.2 states that fish that escape MAY COMPETE OR BREED WITH WILD FISH, so both "
          "consequences are inside the statement. Dropping either one, or denying the statement, "
          "departs from the framework."),

 dict(q="A third student writes that the framework blames rising disease on the water quality "
        "in fish farms. Which correction is required?",
      choices=[
        "The framework attributes the rise to the density of fish in aquaculture",
        "The framework attributes the rise to the fuel used by aquaculture",
        "The framework attributes the rise to the small area of water aquaculture uses",
        "The framework attributes the rise to interbreeding with wild fish",
        "The framework attributes the rise to nothing in particular"],
      ans=0,
      why="STB-1.F.2 names THE DENSITY OF FISH IN AQUACULTURE as what can lead to increases in "
          "disease incidences. Fuel and small water area are STB-1.F.1's reasons for the "
          "expansion, and interbreeding is a separate drawback in the same statement."),

 dict(q="Which observation would most directly show the escape drawback the framework names?",
      choices=[
        "Fish of farmed origin found spawning in a river alongside its wild fish",
        "Fish of farmed origin found only inside the farm's own cages",
        "More nitrogen in the water leaving the farm than in the water entering it",
        "A larger share of the caged fish showing disease at higher stocking densities",
        "Less fuel used per tonne of farmed fish than per tonne of fish caught at sea"],
      ans=0,
      why="STB-1.F.2 states that fish that escape may compete or breed with wild fish, and "
          "farmed fish spawning in a wild river is that meeting observed. The rejected "
          "observations report the wastewater drawback, the density drawback, or one of "
          "STB-1.F.1's benefits."),

 dict(q="Which observation would most directly show the wastewater drawback the framework "
        "names?",
      choices=[
        "Water leaving the farm carrying more nitrogen and solids than the water entering it",
        "Water leaving the farm carrying less nitrogen and fewer solids than the water "
        "entering it",
        "Wild fish near the cages carrying a parasite found in the farmed stock",
        "Farmed fish escaping into the river during a storm",
        "A tonne of farmed fish taking less water area to produce than a tonne caught at sea"],
      ans=0,
      why="STB-1.F.2 states that aquaculture CAN CONTAMINATE WASTEWATER, so water leaving dirtier "
          "than it arrived is the direct evidence. The rejected observations report the disease "
          "drawback, the escape drawback, or one of STB-1.F.1's benefits."),

 dict(q="Which pair of measurements would together test the framework's claim about density "
        "and disease?",
      choices=[
        "The number of fish held in each cubic meter of a cage, and the share of its fish "
        "showing disease",
        "The number of fish held in each cubic meter of a cage, and the fuel used to service "
        "it",
        "The share of a cage's fish showing disease, and the price its fish fetch at market",
        "The nitrogen leaving the farm, and the number of fish that escaped last year",
        "The area of water the farm occupies, and the distance to the nearest wild river"],
      ans=0,
      why="STB-1.F.2 ties increases in disease incidences to the DENSITY of fish, so the test "
          "needs a measure of density and a measure of disease. Each rejected pair supplies at "
          "most one of the two, or tests a different drawback altogether."),

 dict(q="Which of the following goes beyond what the framework's two statements actually say?",
      choices=[
        "That aquaculture has replaced wild capture fishing across the world",
        "That aquaculture is highly efficient",
        "That aquaculture requires little fuel",
        "That aquaculture can contaminate wastewater",
        "That escaped fish may breed with wild fish"],
      ans=0,
      why="STB-1.F.1 says aquaculture has EXPANDED and gives three reasons; it says nothing "
          "about replacing capture fishing anywhere. Each rejected option quotes one of the two "
          "statements directly."),

 dict(q="Both of the framework's statements about the drawbacks use hedged wording. What does "
        "that establish?",
      choices=[
        "The framework presents contamination, escape effects and disease as things that can "
        "happen rather than as certainties",
        "The framework presents contamination, escape effects and disease as certainties in "
        "every operation",
        "The framework presents the drawbacks as impossible in practice",
        "The framework presents the reasons for the expansion as uncertain and the drawbacks "
        "as certain",
        "The framework uses no hedged wording anywhere in this topic"],
      ans=0,
      why="STB-1.F.2 says aquaculture CAN contaminate wastewater, that escapees MAY compete or "
          "breed, and that density CAN lead to increases in disease. Each is a possibility, so "
          "reading any of them as a guarantee or as an impossibility departs from the wording."),

 dict(q="A supplier claims that farming fish makes better use of resources than catching them "
        "at sea. Which of the framework's statements bears on that claim?",
      choices=[
        "The one giving efficiency, small areas of water and little fuel as reasons for the "
        "expansion",
        "The one giving contaminated wastewater and escaped fish as drawbacks",
        "The one giving the density of fish as a cause of disease",
        "The one stating that overfishing has led to the extreme scarcity of some fish "
        "species",
        "No statement in the framework bears on the use of resources by aquaculture"],
      ans=0,
      why="STB-1.F.1 gives high efficiency, only small areas of water and little fuel as the "
          "reasons aquaculture has expanded, which are exactly claims about resources. The "
          "drawbacks are a different statement, and the scarcity claim is EIN-2.J.1 in "
          "topic 5.8."),

 dict(q="How do the framework's two statements on this topic stand in relation to each other?",
      choices=[
        "One gives the reasons the practice has expanded; the other gives the drawbacks that "
        "come with it",
        "One gives the drawbacks that come with the practice; the other gives the reasons it "
        "has expanded, in that order",
        "Both give reasons for the expansion, and neither names a drawback",
        "Both give drawbacks, and neither gives a reason for the expansion",
        "The two statements concern different industries and cannot be applied to one farm"],
      ans=0,
      why="STB-1.F.1 supplies efficiency, small water area and little fuel as reasons for the "
          "expansion, and STB-1.F.2 supplies contaminated wastewater, escapees that may compete "
          "or breed, and density-driven disease. Both apply to a single operation, and the swap "
          "of their order is the error worth guarding against."),

 dict(q="Which summary states this topic as the framework does, without adding to it?",
      choices=[
        "Aquaculture has expanded because it is highly efficient and needs only small areas "
        "of water and little fuel; but it can contaminate wastewater, its escapees may "
        "compete or breed with wild fish, and the density of its stock can raise disease "
        "that reaches wild fish.",
        "Aquaculture has expanded because it needs large areas of water and a great deal of "
        "fuel, and it carries no drawbacks worth naming.",
        "Aquaculture eliminates disease in farmed stock and purifies the water that passes "
        "through it.",
        "Aquaculture has expanded for reasons the framework does not give, and its only "
        "drawback is contaminated wastewater.",
        "Aquaculture has replaced wild capture fishing, ending the scarcity of fish species "
        "worldwide."],
      ans=0,
      why="The keyed summary carries STB-1.F.1's three reasons and all three of STB-1.F.2's "
          "drawbacks. Each rejected summary reverses a reason, denies the drawbacks, drops two "
          "of the three, or adds a claim about replacing capture fishing that the framework "
          "never makes."),
]
