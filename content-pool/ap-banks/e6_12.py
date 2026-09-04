# AP ENVIRONMENTAL SCIENCE 6.12 Wind Energy
# CED effective Fall 2026, Unit 6 Energy Resources and Consumption.
# Enduring understanding ENG-3: humans use energy from a variety of sources, resulting in
# positive and negative consequences.
# Learning objectives ENG-3.R, describe the use of wind energy in power generation; and
# ENG-3.S, describe the effects of the use of wind energy in power generation on the
# environment.
# Suggested skill 7.B, describe potential responses or approaches to environmental problems
# -- which is why one table trials a measure and asks what it addresses and what it costs.
#
# Essential knowledge relied on, in the framework's own words:
#   ENG-3.R.1  Wind turbines use the kinetic energy of moving air to spin a turbine, which
#              spins a generator, producing electricity.
#   ENG-3.S.1  Wind energy is a renewable, clean source of energy. However, birds and bats
#              may be killed if they fly into the spinning turbine blades.
#
# DELIBERATE SEPARATION FROM e6_1. Topic 6.1 already keys ENG-3.S.1 as a CLASSIFICATION --
# wind is the source the framework calls renewable, set against nuclear power, and one item
# there keys that renewable and clean are two claims rather than one. Nothing here repeats
# that shape. This module works the MECHANISM of ENG-3.R.1, the harm ENG-3.S.1 names, and
# what a response to that harm would have to address. Where the two adjectives appear they
# are asked about emissions and about what a record can and cannot show, not about sorting
# sources into two columns.
#
# THE HARM IS NARROW AND HEDGED. ENG-3.S.1 says BIRDS AND BATS MAY BE KILLED IF THEY FLY
# INTO THE SPINNING TURBINE BLADES. It is hedged with MAY; it names two groups of animals
# and no others; and the mechanism is a collision with the BLADES rather than with the tower
# or with anything else. Three items key those three restrictions and no key overstates any
# of them.
#
# WIND IS THE ONE SOURCE IN THIS UNIT WITH NO COST CLAIM. The framework calls solar
# expensive (ENG-3.K.1), hydroelectric construction expensive (ENG-3.M.1), geothermal access
# prohibitively expensive (ENG-3.O.1) and fuel cell technology expensive (ENG-3.Q.1), and it
# says nothing at all about what wind energy costs. One item keys that absence rather than
# supplying a figure from outside the framework.
#
# NO FIGURES. Every quantitative item carries a table=; all arithmetic is recomputed in
# verify_e6_12.py from that table alone and is calculator-free.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("6.12", "Wind Energy", 6)

_T_SPEED = dict(
    headers=["Site with the same turbine installed",
             "Average wind speed at the hub (speed units)",
             "Electricity the turbine delivers each day (energy units)"],
    rows=[["Site 1", "0", "0"],
          ["Site 2", "4", "240"],
          ["Site 3", "6", "360"],
          ["Site 4", "9", "540"]])

_T_EMIT = dict(
    headers=["Way of generating electricity",
             "Air pollutants released for each unit of electricity (grams)",
             "Carbon dioxide released for each unit of electricity (kilograms)"],
    rows=[["Wind farm", "0", "0"],
          ["Coal plant", "310", "0.95"]])

_T_WILDLIFE = dict(
    headers=["Turbine array studied",
             "Turbines standing in the array",
             "Birds found killed at the array in a year",
             "Bats found killed at the array in a year"],
    rows=[["Array 1", "10", "14", "22"],
          ["Array 2", "40", "56", "88"],
          ["Array 3", "100", "140", "220"]])

_T_MEASURE = dict(
    headers=["Stage of a trial at one array",
             "Birds and bats found killed in a year",
             "Electricity delivered in a year (thousand energy units)"],
    rows=[["Before the measure", "360", "900"],
          ["First year with the measure", "150", "870"],
          ["Second year with the measure", "120", "865"]])

QUESTIONS = [

 dict(q="What does the framework say a wind turbine uses?",
      choices=[
        "The kinetic energy of moving air",
        "The heat carried by moving air",
        "The chemical energy stored in the air",
        "The kinetic energy of moving water",
        "The light energy arriving from the sun"],
      ans=0,
      why="ENG-3.R.1 states that WIND TURBINES USE THE KINETIC ENERGY OF MOVING AIR. The energy is "
          "the energy of motion rather than of heat or of chemical bonds, moving water is "
          "hydroelectric power in topic 6.9, and light from the sun is solar energy in 6.8."),

 dict(q="What does the framework say that moving air does first?",
      choices=[
        "It spins a turbine",
        "It spins a generator, with no turbine involved",
        "It is heated so that it expands",
        "It is turned directly into electrical energy",
        "It drives water through a pipe"],
      ans=0,
      why="ENG-3.R.1 states that the kinetic energy of moving air is used TO SPIN A TURBINE. The "
          "generator comes after the turbine in the framework's sequence, and transforming energy "
          "directly into electricity is what photovoltaic cells do in topic 6.8."),

 dict(q="What does the framework say the turbine does?",
      choices=[
        "It spins a generator, which produces the electricity",
        "It produces the electricity itself, with no generator involved",
        "It heats water so that steam can be raised",
        "It stores the energy until the wind drops",
        "It slows the air so that the next turbine can use it"],
      ans=0,
      why="ENG-3.R.1 states that the turbine SPINS A GENERATOR, PRODUCING ELECTRICITY. The turbine "
          "and the generator are separate parts of the framework's sequence and the electricity "
          "comes from the second of them; no steam and no storage appear in this topic."),

 dict(q="Which sequence matches the framework's account of a wind turbine?",
      choices=[
        "Moving air spins a turbine, the turbine spins a generator, and the generator produces "
        "electricity",
        "Moving air spins a generator, the generator spins a turbine, and the turbine produces "
        "electricity",
        "Moving air is heated, the heat raises steam, and the steam spins a turbine",
        "A generator spins a turbine, and the turbine sets the air moving",
        "Moving air is turned directly into electricity, with no turbine and no generator"],
      ans=0,
      why="ENG-3.R.1 gives the whole sequence in one sentence: the kinetic energy of moving air "
          "spins a turbine, which spins a generator, producing electricity. Each rejected sequence "
          "exchanges two of those parts, introduces steam the statement does not have, or removes "
          "the machinery altogether."),

 dict(q="A student writes that the blades of a wind turbine make the electricity themselves. What "
        "correction does the framework require?",
      choices=[
        "The turbine spins a generator, and the generator is what produces the electricity",
        "The turbine produces the electricity and the generator stores it",
        "The moving air produces the electricity before the turbine is reached",
        "The generator spins the turbine, and the turbine produces the electricity",
        "No correction is needed, since the framework treats turbine and generator as one part"],
      ans=0,
      why="ENG-3.R.1 has the turbine spinning A GENERATOR, PRODUCING ELECTRICITY, so the two parts "
          "have different jobs. Nothing in the statement gives the generator a storage role or "
          "reverses the order of the two."),

 dict(q="Which two words does the framework use of wind energy as a source?",
      choices=[
        "Renewable and clean",
        "Renewable and inexpensive",
        "Clean but nonrenewable",
        "Clean and inexhaustible",
        "Renewable and free of any effect on wildlife"],
      ans=0,
      why="ENG-3.S.1 states that WIND ENERGY IS A RENEWABLE, CLEAN SOURCE OF ENERGY, and those are "
          "the two words it uses. The same statement goes on to name a risk to birds and bats, and "
          "the framework says nothing anywhere about what wind energy costs."),

 dict(q="What harm does the framework attach to wind energy?",
      choices=[
        "Birds and bats may be killed if they fly into the spinning turbine blades",
        "Birds and bats may be killed by the air pollutants the turbines release",
        "Fish may be killed as they pass through the turbine",
        "Habitats may be lost or changed following the construction of a dam",
        "The framework attaches no harm to wind energy"],
      ans=0,
      why="ENG-3.S.1 states that BIRDS AND BATS MAY BE KILLED IF THEY FLY INTO THE SPINNING "
          "TURBINE BLADES. The same statement calls wind energy clean, so it releases no air "
          "pollutants; the loss of or change in habitats following the construction of dams is "
          "ENG-3.M.1, in topic 6.9, and the framework names no harm to fish anywhere in this "
          "unit."),

 dict(q="What does the word MAY establish in that clause?",
      choices=[
        "That the deaths are possible rather than certain for any bird or bat that passes",
        "That the deaths are certain for every bird or bat that passes a turbine",
        "That no bird or bat has ever been killed at a turbine",
        "That the risk applies only to birds and not to bats",
        "That the risk applies only where the turbines are offshore"],
      ans=0,
      why="ENG-3.S.1 says birds and bats MAY BE KILLED IF THEY FLY INTO THE SPINNING TURBINE "
          "BLADES, which asserts a possible outcome rather than a certain one. The statement names "
          "both groups of animals and restricts the risk to no particular location."),

 dict(q="Which animals does the framework name in that clause?",
      choices=[
        "Birds and bats",
        "Birds only",
        "Bats only",
        "Birds, bats and insects",
        "Birds, bats and fish"],
      ans=0,
      why="ENG-3.S.1 names BIRDS AND BATS and no other animals. Adding insects or fish to the list "
          "goes beyond the statement, and dropping either of the two named groups leaves it "
          "incomplete."),

 dict(q="With what part of the turbine does the framework say the collision happens?",
      choices=[
        "The spinning blades",
        "The tower supporting the turbine",
        "The generator housing",
        "The cables carrying the electricity away",
        "The framework does not say which part is involved"],
      ans=0,
      why="ENG-3.S.1 says the animals may be killed IF THEY FLY INTO THE SPINNING TURBINE BLADES. "
          "The tower, the housing and the cables appear nowhere in the clause, and the part "
          "involved is named rather than left open."),

 dict(q="A student writes that wind turbines release air pollutants as they generate. What "
        "correction does the framework require?",
      choices=[
        "The framework calls wind energy a clean source, and names only the risk to birds and "
        "bats",
        "The framework calls wind energy a clean source, and names no risk of any kind",
        "The framework calls wind energy a dirty source, so the student is correct",
        "The framework says wind turbines release volatile organic compounds",
        "The framework makes no claim about what wind turbines release"],
      ans=0,
      why="ENG-3.S.1 calls wind energy a RENEWABLE, CLEAN SOURCE OF ENERGY and then names the risk "
          "to birds and bats as the one effect it attaches. Volatile organic compounds belong to "
          "fracking in topic 6.5, and the framework does address what wind energy is like."),

 dict(q="A community wants to reduce the one harm the framework attaches to its wind farm. What "
        "must its measure address?",
      choices=[
        "Collisions of birds and bats with the spinning turbine blades",
        "The air pollutants the turbines release as they generate",
        "The solid waste the turbines produce as they generate",
        "The water the turbines draw from a nearby river",
        "The carbon dioxide released when the turbines are running"],
      ans=0,
      why="ENG-3.S.1 names exactly one effect, and it is birds and bats flying into the spinning "
          "blades. The same statement calls wind energy clean, so there are no air pollutants to "
          "reduce, and no statement in this topic gives a turbine waste, water use or carbon "
          "dioxide in operation."),

 dict(q="Which observation would most directly report the effect the framework names?",
      choices=[
        "Counting the birds and bats found killed at a turbine array over a year",
        "Measuring the air pollutants leaving a turbine array over a year",
        "Measuring the electricity a turbine delivers on a windy day",
        "Recording the cost of building a turbine array",
        "Measuring the wind speed at the hub of each turbine"],
      ans=0,
      why="ENG-3.S.1's effect is that birds and bats may be killed at the spinning blades, so "
          "counting those deaths is what bears on it. Emissions, output, cost and wind speed each "
          "belong to a different claim or to no claim in this topic."),

 dict(q="What does the framework's wind sequence share with its fossil fuel sequence, and what "
        "does it not?",
      choices=[
        "Both end with a turbine spinning a generator; only the fossil fuel sequence burns a "
        "fuel to raise steam first",
        "Both end with a turbine spinning a generator; only the wind sequence burns a fuel to "
        "raise steam first",
        "Both begin by burning a fuel; only the wind sequence ends with a generator",
        "Neither uses a turbine, and both end with a generator",
        "The framework gives no sequence for either of them"],
      ans=0,
      why="ENG-3.R.1 runs moving air, turbine, generator, electricity, while ENG-3.E.2 runs "
          "burning, heat, steam, turbine, generator, electricity. The turbine and generator are "
          "common to both and the combustion and steam belong only to the fossil fuel account."),

 dict(q="Which of the framework's two words for wind energy is a claim about supply, and which "
        "about what is released?",
      choices=[
        "Renewable is the claim about supply; clean is the claim about what is released",
        "Clean is the claim about supply; renewable is the claim about what is released",
        "Both words are claims about supply",
        "Both words are claims about what is released",
        "Neither word is a claim about either"],
      ans=0,
      why="ENG-3.A.2 in topic 6.1 makes a renewable source one replenished naturally at or near "
          "the rate of consumption, which is a claim about supply, while calling a source clean is "
          "a claim about what its use puts out. ENG-3.S.1 applies both words to wind energy in one "
          "sentence."),

 dict(q="What does the framework say about the cost of wind energy?",
      choices=[
        "Nothing; it makes no claim about what wind energy costs",
        "That it is expensive, as it says of solar energy",
        "That its construction can be expensive, as it says of hydroelectric power",
        "That its cost of access can be prohibitively expensive, as it says of geothermal energy",
        "That the technology is expensive, as it says of hydrogen fuel cells"],
      ans=0,
      why="ENG-3.R.1 describes the machinery and ENG-3.S.1 gives two adjectives and one risk, and "
          "neither mentions cost. Each rejected option quotes the cost claim the framework attaches "
          "to a different source in this unit, so a student who transfers one is caught here."),

 dict(q="The same turbine was installed at four sites and its output logged. Which conclusion do "
        "the values support?",
      table=_T_SPEED,
      choices=[
        "The turbine delivers more where the air moves faster, and nothing at all where the air "
        "is still",
        "The turbine delivers more where the air moves faster, and most of all where the air is "
        "still",
        "The turbine delivers the same amount at every site",
        "The output of the turbine is unrelated to the speed of the air",
        "The turbine delivers less where the air moves faster"],
      ans=0,
      why="Wind speed runs 0, 4, 6 and 9 speed units and output runs 0, 240, 360 and 540 energy "
          "units, rising together from nothing at the still site. ENG-3.R.1 makes the KINETIC "
          "ENERGY OF MOVING AIR what drives the turbine, so still air drives nothing."),

 dict(q="Using the same four sites, how much electricity does the turbine deliver for each unit of "
        "wind speed?",
      table=_T_SPEED,
      choices=[
        "60 energy units, the same at every site where the air is moving",
        "40 energy units, the same at every site where the air is moving",
        "240 energy units, which is what the slowest moving site delivers in a whole day",
        "A different amount at each site, falling as the wind rises",
        "The amount for each unit of speed cannot be worked out from the record"],
      ans=0,
      why="Dividing output by wind speed gives 240 over 4, 360 over 6 and 540 over 9, which is 60 "
          "energy units for each speed unit at every moving site. The rejected values pair one "
          "site's output with another site's wind speed, quote a whole day's output as though it "
          "were a rate, or deny an arithmetic the record plainly allows."),

 dict(q="A fifth site with the same turbine averages 7 speed units. What daily output does the "
        "record lead you to expect there?",
      table=_T_SPEED,
      choices=[
        "420 energy units",
        "360 energy units",
        "540 energy units",
        "700 energy units",
        "240 energy units"],
      ans=0,
      why="The record delivers 60 energy units for each unit of wind speed, so seven units gives "
          "420. The rejected values quote a neighbouring site's output, multiply the speed by a "
          "round hundred, or quote the slowest moving site."),

 dict(q="Using the same four sites, how much more does the turbine deliver at the windiest site "
        "than at the slowest site where the air is still moving?",
      table=_T_SPEED,
      choices=[
        "300 energy units",
        "540 energy units",
        "780 energy units",
        "180 energy units",
        "120 energy units"],
      ans=0,
      why="Subtracting the two tabulated outputs gives 540 minus 240, which is 300 energy units. "
          "The rejected values quote the windiest site alone, add the two, or take one of the steps "
          "between adjacent sites."),

 dict(q="A wind farm and a coal plant were compared on what each releases. Which of the "
        "framework's words does the record bear out?",
      table=_T_EMIT,
      choices=[
        "Clean, since the wind farm releases neither air pollutants nor carbon dioxide",
        "Clean, since the wind farm releases more air pollutants than the coal plant",
        "Renewable, since the wind farm releases neither air pollutants nor carbon dioxide",
        "Nonrenewable, since the wind farm releases nothing",
        "Neither word, since the record shows the two releasing the same amounts"],
      ans=0,
      why="The wind farm reads 0 grams of air pollutants and 0 kilograms of carbon dioxide for "
          "each unit of electricity against the coal plant's 310 and 0.95. ENG-3.S.1 calls wind "
          "energy a RENEWABLE, CLEAN SOURCE, and a record of what is released speaks to the second "
          "of those words."),

 dict(q="Using the same comparison, which of the framework's claims does the record leave "
        "untested, and why?",
      table=_T_EMIT,
      choices=[
        "That wind energy is renewable, because a record of what is released says nothing about "
        "whether the source is replenished",
        "That wind energy is clean, because a record of what is released says nothing about "
        "emissions",
        "That birds and bats may be killed at the spinning blades, because the record counts no "
        "animals",
        "That the turbine spins a generator, because the record counts no turbines",
        "None of them; the record tests every claim the framework makes about wind energy"],
      ans=0,
      why="The record carries emissions and nothing else, so it speaks to cleanliness and not to "
          "replenishment, which ENG-3.A.2 in topic 6.1 defines by comparing a rate of "
          "replenishment with a rate of consumption. Two rejected options are true of the record "
          "but are not the claim being asked about, and one misreads what emissions can show."),

 dict(q="Three turbine arrays were monitored for a year. Which of the framework's claims do the "
        "counts support?",
      table=_T_WILDLIFE,
      choices=[
        "That birds and bats may be killed if they fly into the spinning turbine blades",
        "That only birds may be killed if they fly into the spinning turbine blades",
        "That only bats may be killed if they fly into the spinning turbine blades",
        "That wind energy releases air pollutants that kill birds and bats",
        "That no birds or bats are killed at wind turbines"],
      ans=0,
      why="Every array records deaths in both columns, 14 and 22 at the smallest and 140 and 220 "
          "at the largest. ENG-3.S.1 names BIRDS AND BATS together, and the same statement calls "
          "wind energy clean, so no air pollutant is involved."),

 dict(q="Using the same three arrays, how many birds are found killed for each turbine standing?",
      table=_T_WILDLIFE,
      choices=[
        "1.4 birds for each turbine, the same at all three arrays",
        "2.2 birds for each turbine, the same at all three arrays",
        "14 birds for each turbine, the same at all three arrays",
        "A different number at each array, rising with the size of the array",
        "The number for each turbine cannot be worked out from the record"],
      ans=0,
      why="Dividing birds by turbines gives 14 over 10, 56 over 40 and 140 over 100, which is 1.4 "
          "at every array. The rejected values quote the bat rate, quote a whole array's count, or "
          "deny an arithmetic the record plainly allows."),

 dict(q="Using the same three arrays, how many birds and bats together are found killed at the "
        "largest array in a year?",
      table=_T_WILDLIFE,
      choices=[
        "360",
        "140",
        "220",
        "80",
        "110"],
      ans=0,
      why="Adding the two tabulated counts for that array gives 140 plus 220, which is 360. The "
          "rejected values quote one column alone or take the difference between them."),

 dict(q="Using the same three arrays, more bats than birds are found at every array. Does that "
        "change what the framework names?",
      table=_T_WILDLIFE,
      choices=[
        "No, because the framework names birds and bats together without ranking them",
        "Yes, because the framework names bats alone once bats outnumber birds",
        "Yes, because the framework names only the animal found in the larger number",
        "No, because the framework names only birds whatever the counts show",
        "No, because the record shows equal numbers of the two"],
      ans=0,
      why="Bats outnumber birds at each array, 22 against 14, 88 against 56 and 220 against 140. "
          "ENG-3.S.1 names BIRDS AND BATS together and sets no order between them, so which group "
          "is the larger does not alter the statement."),

 dict(q="A measure was trialled at one array and the results recorded. Which of the framework's "
        "concerns does the measure address?",
      table=_T_MEASURE,
      choices=[
        "The killing of birds and bats at the spinning turbine blades",
        "The air pollutants the array releases as it generates",
        "The carbon dioxide the array releases as it generates",
        "The solid waste the array produces as it generates",
        "None of them, since the framework names no concern for wind energy"],
      ans=0,
      why="Deaths fall from 360 to 150 to 120 in a year across the trial, which is the quantity "
          "ENG-3.S.1 names. The same statement calls wind energy clean, so there are no air "
          "pollutants, carbon dioxide or solid waste for a measure to address."),

 dict(q="Using the same trial, by how much did the yearly count of deaths fall?",
      table=_T_MEASURE,
      choices=[
        "By 240",
        "By 360",
        "By 480",
        "By 210",
        "By 30"],
      ans=0,
      why="Subtracting the two tabulated counts gives 360 minus 120, which is 240. The rejected "
          "values quote the opening count, add the two, or take one of the two steps within the "
          "trial."),

 dict(q="Using the same trial, what did the measure cost in electricity delivered over the year?",
      table=_T_MEASURE,
      choices=[
        "35 thousand energy units",
        "30 thousand energy units",
        "900 thousand energy units",
        "865 thousand energy units",
        "Nothing, since the output was unchanged"],
      ans=0,
      why="Subtracting the two tabulated deliveries gives 900 minus 865, which is 35 thousand "
          "energy units. The rejected values take the first year's step alone, quote one reading, "
          "or deny a fall the record shows. The framework names no cost for wind energy, so this "
          "is a figure the trial supplies rather than one the framework does."),

 dict(q="Which summary states this topic as the framework does, without adding to it?",
      choices=[
        "Wind turbines use the kinetic energy of moving air to spin a turbine, which spins a "
        "generator that produces electricity; wind energy is a renewable, clean source, but "
        "birds and bats may be killed if they fly into the spinning blades.",
        "Wind turbines heat air to raise steam for a turbine, and wind energy is a "
        "nonrenewable, clean source with no effect on wildlife.",
        "Wind turbines use the kinetic energy of moving air, and wind energy is renewable and "
        "clean, with no effect the framework names on any animal.",
        "Wind turbines produce electricity in the blades themselves, and the framework calls "
        "wind energy expensive.",
        "Wind energy releases air pollutants that kill birds and bats, and the framework calls "
        "it a nonrenewable source."],
      ans=0,
      why="The keyed summary carries ENG-3.R.1 and ENG-3.S.1 in the framework's own terms, "
          "including both adjectives and the hedged risk to birds and bats. Each rejected summary "
          "introduces steam, reverses the classification, drops the wildlife clause, moves the "
          "electricity into the blades, or adds a cost claim the framework never makes about "
          "wind."),
]
