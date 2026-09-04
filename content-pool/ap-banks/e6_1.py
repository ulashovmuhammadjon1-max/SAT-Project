# AP ENVIRONMENTAL SCIENCE 6.1 Renewable and Nonrenewable Resources
# CED effective Fall 2026, Unit 6 Energy Resources and Consumption.
# Enduring understanding ENG-3: humans use energy from a variety of sources, resulting in
# positive and negative consequences.
# Learning objective ENG-3.A, identify differences between nonrenewable and renewable
# energy sources.
# Suggested skill 1.C, explain environmental concepts, processes, or models in applied
# contexts.
#
# Essential knowledge relied on, in the framework's own words:
#   ENG-3.A.1  Nonrenewable energy sources are those that exist in a fixed amount and
#              involve energy transformation that cannot be easily replaced.
#   ENG-3.A.2  Renewable energy sources are those that can be replenished naturally, at or
#              near the rate of consumption, and reused.
#
# SCOPE, AND THE TRAP THIS TOPIC SETS. The framework gives TWO DEFINITIONS AND NO LIST.
# ENG-3.A.1 and ENG-3.A.2 do not classify a single named source. So a bank of thirty
# items that sorts fuels into two columns would be inventing most of its own keys.
#
# WHAT THE FRAMEWORK DOES CLASSIFY, and the only classifications keyed here:
#   nuclear power  -- ENG-3.G.4, verbatim: "Nuclear power generation is a nonrenewable
#                     energy source."
#   wind energy    -- ENG-3.S.1, verbatim: "Wind energy is a renewable, clean source
#                     of energy."
#   fossil fuels   -- the unit's own Developing Understanding page, which asks "Why are
#                     fossil fuels the most widely used energy resources if they are
#                     nonrenewable?"
# Nothing else is classified anywhere in this module. In particular hydrogen is NOT: the
# framework calls a fuel cell "an alternate to non-renewable fuel sources" (ENG-3.P.1)
# without saying what hydrogen itself is, and biomass, hydroelectricity and geothermal
# energy are never labelled either. Every other item works from the definitions
# themselves, applied to data.
#
# TWO WORDS THAT CARRY THE DEFINITIONS.
#   * ENG-3.A.1 says cannot be EASILY replaced, not cannot be replaced. One item keys it.
#   * ENG-3.A.2 says replenished AT OR NEAR THE RATE OF CONSUMPTION -- a comparison of two
#     rates, not a claim that the source is inexhaustible. Two items key it.
#
# RENEWABLE AND CLEAN ARE TWO CLAIMS, NOT ONE. ENG-3.S.1 calls wind "a renewable, CLEAN
# source", two adjectives; ENG-3.G.4 calls nuclear power nonrenewable AND "a cleaner
# energy source". One item keys that the two properties come apart.
#
# NO FIGURES. Every quantitative item carries a table=; all arithmetic is recomputed in
# verify_e6_1.py from that table alone and is calculator-free.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("6.1", "Renewable and Nonrenewable Resources", 6)

_T_RATES = dict(
    headers=["Energy source studied",
             "Replenished naturally each year (energy units)",
             "Consumed each year (energy units)"],
    rows=[["Source 1", "500", "480"],
          ["Source 2", "900", "870"],
          ["Source 3", "2", "60"],
          ["Source 4", "0", "45"]])

_T_STOCK = dict(
    headers=["Decade of the record",
             "Amount of the deposit remaining (energy units)",
             "Amount added to the deposit during the decade (energy units)"],
    rows=[["First", "800", "0"],
          ["Second", "560", "0"],
          ["Third", "310", "0"],
          ["Fourth", "40", "0"]])

_T_FLOW = dict(
    headers=["Year of the record",
             "Energy taken from the source that year (energy units)",
             "Energy replenished naturally that year (energy units)"],
    rows=[["Year 1", "120", "125"],
          ["Year 5", "140", "142"],
          ["Year 10", "155", "158"]])

_T_MIX = dict(
    headers=["Source of the country's energy",
             "Share of the country's energy (percent)"],
    rows=[["Fossil fuels", "72"],
          ["Nuclear power", "14"],
          ["Wind", "9"],
          ["All other sources together", "5"]])

_T_EXHAUST = dict(
    headers=["Deposit",
             "Amount remaining (energy units)",
             "Amount used each year (energy units)"],
    rows=[["Deposit A", "600", "30"],
          ["Deposit B", "900", "90"],
          ["Deposit C", "240", "60"]])

QUESTIONS = [

 dict(q="How does the course framework define a nonrenewable energy source?",
      choices=[
        "One that exists in a fixed amount and involves energy transformation that cannot "
        "be easily replaced",
        "One that exists in an unlimited amount but is expensive to obtain",
        "One that releases pollutants when it is used",
        "One that is used mainly in developing countries",
        "One that is replenished naturally at or near the rate of consumption"],
      ans=0,
      why="ENG-3.A.1 states that nonrenewable energy sources are those that EXIST IN A FIXED "
          "AMOUNT and involve energy transformation that CANNOT BE EASILY REPLACED. Pollution, "
          "cost and where a source is used appear nowhere in the definition, and the last option "
          "is the definition of the other kind."),

 dict(q="How does the framework define a renewable energy source?",
      choices=[
        "One that can be replenished naturally, at or near the rate of consumption, and "
        "reused",
        "One that can be replenished naturally, but far more slowly than it is consumed",
        "One that exists in a fixed amount and cannot easily be replaced",
        "One that produces no waste of any kind when it is used",
        "One that costs less than any other source available"],
      ans=0,
      why="ENG-3.A.2 states that renewable energy sources are those that can be REPLENISHED "
          "NATURALLY, AT OR NEAR THE RATE OF CONSUMPTION, AND REUSED. The rate comparison is "
          "part of the definition, and waste and cost are not."),

 dict(q="What does the phrase about the rate of consumption establish in the framework's "
        "definition?",
      choices=[
        "Being replenished is not enough on its own; the replenishment must keep pace with "
        "the use",
        "Being replenished is enough on its own, however slowly it happens",
        "The source must be replenished far faster than it is consumed",
        "The source must be consumed far faster than it is replenished",
        "The rate of consumption has no place in the framework's definition"],
      ans=0,
      why="ENG-3.A.2 requires replenishment AT OR NEAR THE RATE OF CONSUMPTION, which is a "
          "comparison between two rates rather than a claim that any replenishment will do. It "
          "asks for parity, not for a large excess."),

 dict(q="Besides being replenished naturally at or near the rate of consumption, what further "
        "property does the framework's definition of a renewable source name?",
      choices=[
        "That it can be reused",
        "That it can be exported",
        "That it can be stored underground",
        "That it can be taxed",
        "The definition names no further property"],
      ans=0,
      why="ENG-3.A.2 ends its definition with AND REUSED, so being reusable is part of the "
          "statement rather than an addition to it. Export, storage and taxation appear nowhere "
          "in either definition."),

 dict(q="The framework says a nonrenewable source involves energy transformation that cannot "
        "be EASILY replaced. What does the word easily establish?",
      choices=[
        "The framework marks replacement as difficult rather than flatly impossible",
        "The framework marks replacement as impossible in every case",
        "The framework marks replacement as straightforward once the source is exhausted",
        "The framework marks replacement as depending on the price of the source",
        "The framework attaches no qualification to replacement at all"],
      ans=0,
      why="ENG-3.A.1 says the transformation CANNOT BE EASILY REPLACED, and that hedge is part "
          "of the definition. Reading it as an outright impossibility, or dropping it, both "
          "depart from the statement's wording."),

 dict(q="Which energy source does the framework state in so many words to be a nonrenewable "
        "energy source?",
      choices=[
        "Nuclear power generation",
        "Wind energy",
        "Solar energy",
        "Hydroelectric power",
        "Geothermal energy"],
      ans=0,
      why="ENG-3.G.4 states that NUCLEAR POWER GENERATION IS A NONRENEWABLE ENERGY SOURCE, in "
          "those words. The framework labels wind renewable in ENG-3.S.1 and does not label "
          "solar, hydroelectric or geothermal energy either way."),

 dict(q="Which energy source does the framework state in so many words to be a renewable, "
        "clean source of energy?",
      choices=[
        "Wind energy",
        "Nuclear power generation",
        "Coal",
        "Natural gas",
        "Crude oil from tar sands"],
      ans=0,
      why="ENG-3.S.1 states that WIND ENERGY IS A RENEWABLE, CLEAN SOURCE OF ENERGY. ENG-3.G.4 "
          "puts nuclear power on the nonrenewable side, and the framework's unit overview treats "
          "fossil fuels as nonrenewable."),

 dict(q="How does the framework's own unit overview treat fossil fuels in this respect?",
      choices=[
        "As nonrenewable, asking why they are the most widely used energy resources if they "
        "are nonrenewable",
        "As renewable, asking why they are so little used if they are renewable",
        "As neither renewable nor nonrenewable, since the question does not arise",
        "As renewable in developed countries and nonrenewable in developing ones",
        "The unit overview says nothing about fossil fuels"],
      ans=0,
      why="The unit's Developing Understanding page frames the whole unit with the question WHY "
          "ARE FOSSIL FUELS THE MOST WIDELY USED ENERGY RESOURCES IF THEY ARE NONRENEWABLE, so "
          "the framework classifies them as nonrenewable and treats their wide use as the thing "
          "needing explanation. ENG-3.B.2 supplies the wide use."),

 dict(q="The framework calls wind a renewable, clean source and separately calls nuclear power "
        "a cleaner source that is nonrenewable. What does that show about the two properties?",
      choices=[
        "Being renewable and being clean are separate claims, and a source may be one "
        "without the other",
        "Being renewable and being clean are the same claim under two names",
        "Every renewable source is dirty and every nonrenewable source is clean",
        "The framework never describes any source as clean",
        "The framework never describes any source as renewable"],
      ans=0,
      why="ENG-3.S.1 attaches two adjectives to wind, renewable AND clean, while ENG-3.G.4 calls "
          "nuclear power nonrenewable and in the same breath a cleaner energy source because it "
          "does not produce air pollutants. The two properties therefore come apart."),

 dict(q="Four energy sources were measured for how fast they are replenished and how fast they "
        "are used. Which pair meets the framework's rate test for a renewable source?",
      table=_T_RATES,
      choices=[
        "The first two, whose replenishment each year is at or near what is consumed",
        "The last two, whose replenishment each year is at or near what is consumed",
        "All four, since every source is replenished to some degree",
        "None of them, since no source is replenished exactly as fast as it is consumed",
        "The first two, because they are consumed faster than they are replenished"],
      ans=0,
      why="The first two are replenished 500 against 480 consumed and 900 against 870, while the "
          "third is replenished 2 against 60 consumed and the fourth not at all. ENG-3.A.2 asks "
          "for replenishment AT OR NEAR THE RATE OF CONSUMPTION, which the first two meet and "
          "the others do not."),

 dict(q="Using the same four sources, how much more of the third source is consumed each year "
        "than is replenished?",
      table=_T_RATES,
      choices=[
        "Thirty times as much",
        "Three times as much",
        "Fifteen times as much",
        "Two times as much",
        "The same amount"],
      ans=0,
      why="Dividing the two tabulated rates gives 60 divided by 2, which is 30. The rejected "
          "values come from misreading the replenishment column, from halving the answer, or "
          "from denying that the two rates differ."),

 dict(q="One deposit was measured once a decade for forty years. Which of the framework's "
        "definitions do the values fit?",
      table=_T_STOCK,
      choices=[
        "The nonrenewable definition, because nothing is added while the amount remaining "
        "falls decade after decade",
        "The renewable definition, because nothing is added while the amount remaining falls "
        "decade after decade",
        "The renewable definition, because the deposit is replenished at or near the rate of "
        "consumption",
        "The nonrenewable definition, because the amount remaining rises decade after decade",
        "Neither definition, because a deposit cannot be measured over time"],
      ans=0,
      why="The deposit runs 800, 560, 310 and 40 energy units while the amount added stays at "
          "zero in every decade. ENG-3.A.1 defines a nonrenewable source as one existing in a "
          "FIXED AMOUNT, and a stock with no addition is exactly that."),

 dict(q="Using the same deposit, how much of it had been drawn down between the first decade "
        "and the fourth?",
      table=_T_STOCK,
      choices=[
        "760 energy units",
        "800 energy units",
        "490 energy units",
        "270 energy units",
        "250 energy units"],
      ans=0,
      why="Subtracting the two tabulated amounts gives 800 minus 40, which is 760 energy units. "
          "The rejected values quote the opening amount alone or take the fall across one of the "
          "shorter intervals within the record."),

 dict(q="A second source was measured in the same way. Which of the framework's definitions do "
        "these values fit?",
      table=_T_FLOW,
      choices=[
        "The renewable definition, because what is replenished each year stays at or near "
        "what is taken",
        "The nonrenewable definition, because what is replenished each year stays at or near "
        "what is taken",
        "The renewable definition, because far more is taken each year than is replenished",
        "The nonrenewable definition, because nothing at all is replenished",
        "Neither definition, because the amounts change from year to year"],
      ans=0,
      why="The source yields 120, 140 and 155 energy units in the sampled years against "
          "replenishment of 125, 142 and 158. ENG-3.A.2 asks for replenishment AT OR NEAR THE "
          "RATE OF CONSUMPTION, which is what these pairs show."),

 dict(q="Using the same source, by how much did the energy taken from it rise between the "
        "first sampled year and the last?",
      table=_T_FLOW,
      choices=[
        "By 35 energy units",
        "By 155 energy units",
        "By 275 energy units",
        "By 33 energy units",
        "By 20 energy units"],
      ans=0,
      why="Subtracting the two tabulated amounts gives 155 minus 120, which is 35 energy units. "
          "The rejected values quote the final year alone, add the two, take the rise in the "
          "replenishment column, or take one of the shorter intervals."),

 dict(q="A country's energy comes from the sources in the table. Which reading uses only the "
        "classifications the framework itself states?",
      table=_T_MIX,
      choices=[
        "Fossil fuels and nuclear power, which the framework treats as nonrenewable, "
        "together supply the largest part, and wind, which the framework calls renewable, "
        "supplies less than a tenth.",
        "Wind and nuclear power, which the framework treats as nonrenewable, together supply "
        "the largest part, and fossil fuels, which the framework calls renewable, supply "
        "less than a tenth.",
        "The framework classifies every one of the four entries, so all four can be sorted "
        "with confidence.",
        "The framework classifies none of the four entries, so no reading of the table is "
        "possible.",
        "Wind supplies the largest share of the country's energy."],
      ans=0,
      why="ENG-3.G.4 calls nuclear power nonrenewable, the unit overview treats fossil fuels as "
          "nonrenewable, and ENG-3.S.1 calls wind renewable; the fourth row is unnamed by the "
          "framework and is left unsorted. The table reads 72, 14, 9 and 5 percent."),

 dict(q="Using the same country, what share of its energy comes from the two sources the "
        "framework treats as nonrenewable?",
      table=_T_MIX,
      choices=[
        "86 percent",
        "72 percent",
        "95 percent",
        "14 percent",
        "9 percent"],
      ans=0,
      why="Adding the two tabulated shares gives 72 plus 14, which is 86 percent. The rejected "
          "values quote fossil fuels alone, add wind to the pair, quote nuclear power alone, or "
          "quote the wind share."),

 dict(q="Three deposits are compared for what remains and what is used. Which deposit will "
        "last longest at the rates given, and why is that not the largest one?",
      table=_T_EXHAUST,
      choices=[
        "The first deposit, because how long a fixed amount lasts depends on the rate of use "
        "as well as the amount",
        "The second deposit, because it holds the largest amount remaining",
        "The third deposit, because it is used at the highest rate",
        "All three last equally long, because each is a fixed amount",
        "The question cannot be answered without knowing the price of the energy"],
      ans=0,
      why="Deposit A holds 600 units used at 30 a year, which is twenty years; Deposit B holds "
          "900 used at 90, which is ten; Deposit C holds 240 used at 60, which is four. ENG-3.A.1 "
          "makes a nonrenewable source a FIXED AMOUNT, and a fixed amount lasts as long as the "
          "rate of use allows."),

 dict(q="Using the same three deposits, how long will the shortest-lived one last at the rate "
        "given?",
      table=_T_EXHAUST,
      choices=[
        "Four years",
        "Ten years",
        "Twenty years",
        "Two years",
        "Sixty years"],
      ans=0,
      why="Dividing the tabulated amount by the tabulated rate gives 240 divided by 60, which is "
          "4 years. The rejected values give the lives of the other two deposits, halve the "
          "answer, or quote the annual rate as if it were a number of years."),

 dict(q="A student writes that a renewable source is one that will never run out. Which "
        "correction does the framework require?",
      choices=[
        "The definition turns on replenishment keeping pace with consumption, which can fail "
        "if consumption rises",
        "The definition turns on the source being inexhaustible, so the student is correct",
        "The definition turns on the source producing no pollution",
        "The definition turns on the source being cheap to obtain",
        "The framework offers no definition of a renewable source"],
      ans=0,
      why="ENG-3.A.2 defines a renewable source as one replenished naturally AT OR NEAR THE RATE "
          "OF CONSUMPTION, a comparison that can be broken from either side. Nothing in it "
          "promises that a source cannot be exhausted, and cost and pollution are not in it."),

 dict(q="A second student writes that a nonrenewable source is one that can never be replaced "
        "under any circumstances. Which correction does the framework require?",
      choices=[
        "The framework says the energy transformation cannot be EASILY replaced, which is a "
        "weaker claim",
        "The framework says the energy transformation can always be replaced, so the student "
        "has it backwards",
        "The framework says nonrenewable sources are replenished at or near the rate of "
        "consumption",
        "The framework says nonrenewable sources exist in an unlimited amount",
        "The framework says nothing about replacing the energy transformation"],
      ans=0,
      why="ENG-3.A.1 says nonrenewable sources involve energy transformation that CANNOT BE "
          "EASILY REPLACED, which is a statement about difficulty rather than impossibility. The "
          "rejected options reverse the clause or import the other definition."),

 dict(q="Which single observation would bear most directly on whether a source meets the "
        "framework's definition of renewable?",
      choices=[
        "How much of the source is replaced naturally in a year set against how much is used "
        "in that year",
        "How much the source costs for each unit of energy it delivers",
        "How many countries currently obtain energy from the source",
        "How much air pollution the source releases when it is used",
        "How long the source has been in commercial use"],
      ans=0,
      why="ENG-3.A.2 makes the test a comparison between natural replenishment and consumption "
          "over the same period. Cost, popularity, pollution and history are not in the "
          "definition, though the framework discusses them elsewhere."),

 dict(q="Which pair of measurements is the minimum needed to apply the framework's renewable "
        "definition to a source?",
      choices=[
        "The amount replenished naturally in a period, and the amount consumed in the same "
        "period",
        "The amount consumed in a period, and the price paid for it",
        "The amount replenished naturally in a period, and the number of people using the "
        "source",
        "The amount of pollution released, and the amount of waste left behind",
        "The amount remaining in the ground, and the year the source was discovered"],
      ans=0,
      why="ENG-3.A.2 sets replenishment AT OR NEAR THE RATE OF CONSUMPTION, so both sides of "
          "that comparison must be measured over the same period. Each rejected pair supplies at "
          "most one of the two, which is why the anchor spans the pairing."),

 dict(q="A source is replenished naturally, but a survey finds it is being used at many times "
        "the rate at which it is replaced. How does the framework's definition apply?",
      choices=[
        "It fails the renewable definition, because replenishment is not at or near the rate "
        "of consumption",
        "It meets the renewable definition, because it is replenished naturally at all",
        "It meets the renewable definition, because heavy use shows the source is abundant",
        "It fails the renewable definition, because natural replenishment disqualifies a "
        "source",
        "The framework's definition cannot be applied to a source that is replenished at all"],
      ans=0,
      why="ENG-3.A.2 requires replenishment AT OR NEAR THE RATE OF CONSUMPTION, so natural "
          "replenishment far below the rate of use does not satisfy it. The rejected options "
          "drop the rate comparison or invert what natural replenishment means."),

 dict(q="A different source is replenished naturally at very nearly the rate at which it is "
        "used, and what is taken can be used again. How does the framework's definition apply?",
      choices=[
        "It meets the renewable definition on both counts the statement names",
        "It meets the renewable definition on the rate but fails on reuse",
        "It fails the renewable definition, because the rates are not exactly equal",
        "It fails the renewable definition, because reuse is not part of it",
        "The framework gives no definition that such a source could meet"],
      ans=0,
      why="ENG-3.A.2 names two things, replenishment AT OR NEAR the rate of consumption and "
          "reuse, and this source satisfies both. The word near allows the rates to differ "
          "slightly, and reuse is in the statement rather than outside it."),

 dict(q="Which of the following does the framework's pair of definitions NOT settle about an "
        "energy source?",
      choices=[
        "How much pollution it releases and how much it costs",
        "Whether it exists in a fixed amount",
        "Whether its energy transformation can easily be replaced",
        "Whether it is replenished naturally",
        "Whether the replenishment keeps pace with the consumption"],
      ans=0,
      why="ENG-3.A.1 and ENG-3.A.2 speak of fixed amounts, replacement, natural replenishment "
          "and the rate comparison, and of nothing else. Cost and pollution belong to other "
          "statements, so reading them out of these definitions adds to them."),

 dict(q="Which of the two definitions turns on a comparison between two rates, and which on a "
        "fixed quantity?",
      choices=[
        "The renewable definition turns on the rate comparison; the nonrenewable definition "
        "turns on the fixed amount",
        "The nonrenewable definition turns on the rate comparison; the renewable definition "
        "turns on the fixed amount",
        "Both definitions turn on a comparison between two rates",
        "Both definitions turn on a fixed quantity",
        "Neither definition turns on either"],
      ans=0,
      why="ENG-3.A.2 sets replenishment against the rate of consumption, while ENG-3.A.1 opens "
          "with EXIST IN A FIXED AMOUNT. The exact swap of the two is the error worth guarding "
          "against."),

 dict(q="Which finding would count as evidence AGAINST classifying a source as renewable under "
        "the framework's definition?",
      choices=[
        "Consumption has risen year after year while natural replenishment has stayed level",
        "Consumption has fallen year after year while natural replenishment has stayed level",
        "The source releases no air pollution when it is used",
        "The source is used in a larger number of countries each year",
        "The source is cheaper this year than it was last year"],
      ans=0,
      why="ENG-3.A.2's test is replenishment AT OR NEAR THE RATE OF CONSUMPTION, and rising use "
          "against level replenishment pulls the two apart. Falling use moves them together, and "
          "pollution, popularity and price are outside the definition."),

 dict(q="Why does the framework's unit overview treat the wide use of fossil fuels as "
        "something needing explanation?",
      choices=[
        "Because how widely a source is used is a separate question from whether it is "
        "renewable, and the framework answers it with availability, price and regulation",
        "Because a nonrenewable source cannot be used widely, so the observation must be an "
        "error",
        "Because the framework classifies fossil fuels as renewable and expects them to be "
        "used widely",
        "Because the framework holds that only clean sources are used widely",
        "Because the framework gives no account of why any source is used"],
      ans=0,
      why="The unit overview asks why fossil fuels are the most widely used resources if they "
          "are nonrenewable, ENG-3.B.2 records that they are the most widely used, and ENG-3.B.5 "
          "gives availability, price and governmental regulations as what influences which "
          "sources people use."),

 dict(q="Which summary states this topic as the framework does, without adding to it?",
      choices=[
        "A nonrenewable source exists in a fixed amount and involves an energy transformation "
        "that cannot easily be replaced; a renewable source is replenished naturally at or "
        "near the rate of consumption and reused.",
        "A nonrenewable source is replenished naturally at or near the rate of consumption; a "
        "renewable source exists in a fixed amount.",
        "A nonrenewable source is one that pollutes; a renewable source is one that does not.",
        "A renewable source is one that can never be exhausted, whatever the rate at which it "
        "is used.",
        "The framework defines neither kind of source and offers only a list of examples."],
      ans=0,
      why="The keyed summary is ENG-3.A.1 and ENG-3.A.2 with nothing removed and nothing added. "
          "Each rejected summary swaps the two definitions, substitutes pollution for the stated "
          "tests, drops the rate comparison, or denies that definitions are given."),
]
