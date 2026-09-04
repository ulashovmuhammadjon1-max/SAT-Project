# AP ENVIRONMENTAL SCIENCE 3.9 Demographic Transition
# CED effective Fall 2026, Unit 3 Populations.
# Enduring understanding EIN-1: Human populations change in reaction to a variety of
# factors, including social and cultural factors.
# Learning objective EIN-1.D: define the demographic transition. Suggested skill 1.C,
# explain environmental concepts, processes, or models in applied contexts.
#
# Essential knowledge relied on, in the framework's own words:
#   EIN-1.D.1  The demographic transition refers to the transition from high to lower
#              birth and death rates in a country or region as development occurs and
#              that country moves from a pre-industrial to an industrialized economic
#              system. This transition is typically demonstrated through a four-stage
#              demographic transition model (DTM).
#   EIN-1.D.2  Characteristics of developing countries include higher infant mortality
#              rates and more children in the workforce than developed countries.
#
# THE FRAMEWORK NAMES THE FOUR STAGE MODEL AND DESCRIBES NONE OF ITS STAGES. It says
# only that the transition runs from high to lower birth AND death rates as a country
# develops, and that a four stage model is the usual way of demonstrating it. So NO KEY
# HERE STATES WHAT HAPPENS IN STAGE 1, 2, 3 OR 4 -- item 7 keys exactly that absence, and
# item 28 refuses the reading that every country passes through the stages at one pace.
# Where an item reads a country's rates it keys the movement the record shows, which is
# the movement EIN-1.D.1 describes, and never a stage number.
#
# THE SWAP IS THE DANGER IN THIS TOPIC. High to lower against low to higher, and
# developing against developed, are the two reversals a prepared student falls for. Every
# anchor on such an item carries BOTH clauses -- the direction and the thing that moves --
# never one alone. An anchor of "birth and death rates" would match the swapped
# distractor exactly as well as the key.
#
# NO FIGURES ARE REFERENCED. The demographic transition model is normally taught from a
# picture and the bank cannot carry one, so every record is supplied as a table of rates
# and the question is asked of the rows.
#
# BOUNDARIES. Age structure is EIN-1.A (topic 3.6), total fertility rate and the factors
# associated with infant mortality are EIN-1.B (topic 3.7), and the rate of natural
# increase, the doubling time estimate and the density dependent and independent factors
# are EIN-1.C (topic 3.8). No key here computes a rate of natural increase or a doubling
# time, and the infant mortality claim used here is EIN-1.D.2's comparison between
# developing and developed countries, not EIN-1.B.3's list of associated factors.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: export_units.py does not typeset
# Environmental Science. Age ranges are written with "to".
TOPIC = ("3.9", "Demographic Transition", 3)

_T_TRANSITION = dict(
    headers=["Period of the record", "Crude birth rate per 1,000 people",
             "Crude death rate per 1,000 people"],
    rows=[["Period 1", "44", "38"],
          ["Period 2", "43", "26"],
          ["Period 3", "36", "16"],
          ["Period 4", "24", "11"],
          ["Period 5", "13", "9"]])

_T_FOUR = dict(
    headers=["Country", "Crude birth rate per 1,000 people",
             "Crude death rate per 1,000 people"],
    rows=[["Country 1", "45", "38"],
          ["Country 2", "41", "17"],
          ["Country 3", "27", "10"],
          ["Country 4", "11", "9"]])

_T_ECONOMY = dict(
    headers=["Region", "Percent of the workforce employed in industry and services",
             "Crude birth rate per 1,000 people", "Crude death rate per 1,000 people"],
    rows=[["Region 1", "12", "46", "33"],
          ["Region 2", "34", "35", "18"],
          ["Region 3", "61", "22", "11"],
          ["Region 4", "88", "12", "8"]])

_T_DEVELOPING = dict(
    headers=["Country", "Infant deaths per 1,000 live births",
             "Percent of children aged 10 to 14 who are in the workforce"],
    rows=[["Country A", "68", "24"],
          ["Country B", "51", "17"],
          ["Country C", "19", "5"],
          ["Country D", "4", "1"]])

_T_PAIR = dict(
    headers=["Measure recorded in the same year", "Country M", "Country N"],
    rows=[["Infant deaths per 1,000 live births", "62", "5"],
          ["Percent of children aged 10 to 14 who are in the workforce", "21", "1"]])

QUESTIONS = [

 dict(q="What does the framework say the demographic transition refers to?",
      choices=[
        "The transition from high to lower birth and death rates in a country or region as "
        "development occurs.",
        "The transition from low to higher birth and death rates in a country or region as "
        "development occurs.",
        "The transition from high to lower birth rates only, with death rates unchanged.",
        "The transition from high to lower death rates only, with birth rates unchanged.",
        "The movement of people from one country to another as development occurs."],
      ans=0,
      why="EIN-1.D.1 states that the demographic transition refers to the transition from "
          "high to lower birth and death rates in a country or region as development "
          "occurs, which fixes the direction and puts both rates in the statement."),

 dict(q="What economic change does the framework attach to the demographic transition?",
      choices=[
        "A country moving from a pre-industrial to an industrialized economic system.",
        "A country moving from an industrialized to a pre-industrial economic system.",
        "A country enlarging its land area through settlement.",
        "A country raising the number of species it protects.",
        "A country changing the language of its schools."],
      ans=0,
      why="EIN-1.D.1 places the transition where development occurs and the country moves "
          "from a pre-industrial to an industrialized economic system, and it names that "
          "direction of change and no other."),

 dict(q="Through what does the framework say the demographic transition is typically "
        "demonstrated?",
      choices=[
        "A four stage demographic transition model.",
        "A three stage demographic transition model.",
        "A five stage demographic transition model.",
        "A single equation relating births to deaths.",
        "A survey of the ages of every person in a country."],
      ans=0,
      why="EIN-1.D.1's second sentence states that the transition is typically "
          "demonstrated through a four stage demographic transition model, so the number "
          "of stages is the framework's own."),

 dict(q="How many stages does the model the framework names contain?",
      choices=[
        "Four.",
        "Two.",
        "Three.",
        "Five.",
        "Six."],
      ans=0,
      why="EIN-1.D.1 calls it a four stage demographic transition model, so the count is "
          "stated in the framework rather than inferred."),

 dict(q="Which rates does the framework say move during the demographic transition?",
      choices=[
        "Birth rates and death rates together.",
        "Birth rates alone.",
        "Death rates alone.",
        "Immigration rates alone.",
        "Emigration rates alone."],
      ans=0,
      why="EIN-1.D.1 describes a transition from high to lower birth and death rates, "
          "naming both, and mentions neither immigration nor emigration in this "
          "statement."),

 dict(q="EIN-1.D.1 says the transition is TYPICALLY demonstrated through a four stage "
        "model. What does that wording establish?",
      choices=[
        "That the four stage model is the usual way of showing it, not the only possible "
        "way.",
        "That the four stage model is the only representation that exists.",
        "That the model applies to only one country in the world.",
        "That the transition itself has no stages of any kind.",
        "That the model shows something other than the demographic transition."],
      ans=0,
      why="The hedge TYPICALLY in EIN-1.D.1 marks the four stage model as the usual "
          "representation rather than the only one, so the framework asserts neither "
          "exclusivity nor the absence of the model."),

 dict(q="What does the framework itself state about what happens within each of the four "
        "stages?",
      choices=[
        "Nothing; it names the model and describes only the transition as a whole.",
        "It gives the birth rate and the death rate typical of each of the four stages.",
        "It gives the number of years each of the four stages lasts.",
        "It states which stage every country in the world currently occupies.",
        "It states that the fourth stage always ends in population decline."],
      ans=0,
      why="EIN-1.D.1 names the four stage demographic transition model and describes the "
          "transition as a movement from high to lower birth and death rates as "
          "development occurs. It supplies no rates, no durations, no country list and no "
          "outcome for any individual stage."),

 dict(q="Which characteristics does the framework attribute to developing countries?",
      choices=[
        "Higher infant mortality rates and more children in the workforce than developed "
        "countries.",
        "Lower infant mortality rates and fewer children in the workforce than developed "
        "countries.",
        "Higher infant mortality rates and fewer children in the workforce than developed "
        "countries.",
        "Lower infant mortality rates and more children in the workforce than developed "
        "countries.",
        "A larger land area and a greater number of species than developed countries."],
      ans=0,
      why="EIN-1.D.2 states that characteristics of developing countries include higher "
          "infant mortality rates and more children in the workforce than developed "
          "countries, so both halves point the same way."),

 dict(q="A revision card lists five things and calls all five framework characteristics "
        "of developing countries. Which one is not?",
      choices=[
        "A larger land area than developed countries.",
        "Higher infant mortality rates than developed countries.",
        "More children in the workforce than developed countries.",
        "Infant mortality rates that exceed those of developed countries.",
        "A greater share of children working than in developed countries."],
      ans=0,
      why="EIN-1.D.2 names higher infant mortality rates and more children in the "
          "workforce, each of which the four rejected options restates. Land area appears "
          "in neither of this topic's statements."),

 dict(q="A student writes that the demographic transition is a fall in birth rates while "
        "death rates stay where they were. What is the clearest correction?",
      choices=[
        "The framework describes both birth rates and death rates moving from high to "
        "lower.",
        "The framework describes death rates rising while birth rates fall.",
        "The framework describes birth rates rising while death rates fall.",
        "The framework describes neither rate as moving at all.",
        "The framework describes immigration replacing both rates."],
      ans=0,
      why="EIN-1.D.1 puts birth and death rates together in one movement from high to "
          "lower as development occurs, so leaving death rates out drops half of what the "
          "statement says."),

 dict(q="A student writes that the demographic transition runs from low birth and death "
        "rates to high ones. What is the clearest correction?",
      choices=[
        "The framework describes the transition running from high rates to lower ones.",
        "The framework describes the transition running from low rates to higher ones, so "
        "the student is right.",
        "The framework describes the transition as leaving both rates unchanged.",
        "The framework describes the transition as concerning migration rather than "
        "births and deaths.",
        "The framework gives no direction for the transition at all."],
      ans=0,
      why="EIN-1.D.1 states the direction explicitly, from high to lower birth and death "
          "rates, so the reversed reading contradicts the statement rather than "
          "restating it."),

 dict(q="Which comparison does EIN-1.D.2 draw?",
      choices=[
        "Developing countries set against developed countries.",
        "One developed country set against another developed country.",
        "One region of a country set against another region of the same country.",
        "A country today set against the same country a century earlier.",
        "Countries set against the species living within them."],
      ans=0,
      why="EIN-1.D.2 states its two characteristics of developing countries explicitly in "
          "comparison with developed countries, which is the only comparison it makes."),

 dict(q="One country's two crude rates were recorded over five successive periods. What "
        "does the record establish?",
      table=_T_TRANSITION,
      choices=[
        "Both rates end far lower than they began, which is the movement the framework "
        "describes.",
        "Both rates end far higher than they began, which is the movement the framework "
        "describes.",
        "The birth rate falls while the death rate rises across the record.",
        "The death rate falls while the birth rate rises across the record.",
        "Neither rate changes appreciably across the five periods."],
      ans=0,
      why="Reading down both columns, each rate ends far below where it started. EIN-1.D.1 "
          "describes the demographic transition as a movement from high to lower birth and "
          "death rates as development occurs."),

 dict(q="Across those same five periods, by how much did the crude birth rate fall?",
      table=_T_TRANSITION,
      choices=[
        "By 31 per thousand people.",
        "By 29 per thousand people.",
        "By 44 per thousand people.",
        "By 13 per thousand people.",
        "By 12 per thousand people."],
      ans=0,
      why="The first and last entries in the crude birth rate column are subtracted. "
          "EIN-1.D.1 makes a movement from high to lower birth rates one half of what the "
          "demographic transition describes."),

 dict(q="Over the same five periods, by how much did the crude death rate fall?",
      table=_T_TRANSITION,
      choices=[
        "By 29 per thousand people.",
        "By 31 per thousand people.",
        "By 38 per thousand people.",
        "By 9 per thousand people.",
        "By 12 per thousand people."],
      ans=0,
      why="The first and last entries in the crude death rate column are subtracted. "
          "EIN-1.D.1 makes a movement from high to lower death rates the other half of "
          "what the demographic transition describes."),

 dict(q="Between the first and second of those periods, which of the two rates fell "
        "further?",
      table=_T_TRANSITION,
      choices=[
        "The death rate, which fell by 12 per thousand against the birth rate's 1.",
        "The birth rate, which fell by 12 per thousand against the death rate's 1.",
        "Both fell by the same amount between those two periods.",
        "Neither fell between those two periods.",
        "The birth rate fell while the death rate rose between those two periods."],
      ans=0,
      why="The two columns are read across the first two rows and the changes compared. "
          "EIN-1.D.1 describes the overall movement from high to lower birth and death "
          "rates and says nothing about which of the two moves first, so the order here is "
          "a property of this record rather than a framework claim."),

 dict(q="Four countries were recorded for their crude birth and death rates in the same "
        "year. What does the record establish?",
      table=_T_FOUR,
      choices=[
        "The four stand at different points, with both rates highest in one country and "
        "both lowest in another.",
        "The four stand at the same point, since every country records a birth rate above "
        "its death rate.",
        "The country with the highest birth rate also records the lowest death rate.",
        "The country with the lowest birth rate also records the highest death rate.",
        "Every one of the four records the same crude death rate."],
      ans=0,
      why="Sorting the countries by either rate puts them in the same order, with one "
          "country leading on both and another trailing on both. EIN-1.D.1 describes the "
          "transition as a movement from high to lower birth and death rates, so countries "
          "part way along it stand at different points."),

 dict(q="Which of those four countries records the pattern of a country that has not yet "
        "made the movement the framework describes?",
      table=_T_FOUR,
      choices=[
        "Country 1, whose birth rate and death rate are both the highest in the record.",
        "Country 4, whose birth rate and death rate are both the lowest in the record.",
        "Country 2, whose death rate has fallen well below its birth rate.",
        "Country 3, whose two rates lie in the middle of the record.",
        "None of the four, because every country records some births and some deaths."],
      ans=0,
      why="EIN-1.D.1 describes the transition as running from high to lower birth and "
          "death rates, so a country still carrying the highest of both has not yet made "
          "that movement."),

 dict(q="And which of those four countries records the pattern of a country at the far "
        "end of that movement?",
      table=_T_FOUR,
      choices=[
        "Country 4, whose birth rate and death rate are both the lowest in the record.",
        "Country 1, whose birth rate and death rate are both the highest in the record.",
        "Country 2, whose birth rate is the second highest in the record.",
        "Country 3, whose death rate is the second lowest in the record.",
        "None of the four, because the framework gives no rates for any stage."],
      ans=0,
      why="EIN-1.D.1 describes the transition as running from high to lower birth and "
          "death rates, so a country carrying the lowest of both stands at the far end of "
          "that movement."),

 dict(q="Four regions were recorded for the share of their workforce in industry and "
        "services alongside their two crude rates. What does the record establish?",
      table=_T_ECONOMY,
      choices=[
        "Both crude rates fall as the share of the workforce in industry and services "
        "rises.",
        "Both crude rates rise as the share of the workforce in industry and services "
        "rises.",
        "The crude birth rate falls while the crude death rate rises as that share rises.",
        "The crude death rate falls while the crude birth rate rises as that share rises.",
        "Neither crude rate moves with that share in this record."],
      ans=0,
      why="Sorting the regions by the share of the workforce in industry and services "
          "leaves both crude rates strictly falling. EIN-1.D.1 ties the transition from "
          "high to lower birth and death rates to a country moving from a pre-industrial "
          "to an industrialized economic system."),

 dict(q="Which of those four regions has the least industrialized economy and the highest "
        "pair of crude rates?",
      table=_T_ECONOMY,
      choices=[
        "Region 1.",
        "Region 2.",
        "Region 3.",
        "Region 4.",
        "No single region leads on all three columns at once."],
      ans=0,
      why="The smallest entry in the industry and services column and the largest entries "
          "in both rate columns fall in the same row. EIN-1.D.1 places the movement from "
          "high to lower rates alongside the move to an industrialized economic system."),

 dict(q="Four countries were recorded for infant deaths and for children in the workforce. "
        "What does the record establish?",
      table=_T_DEVELOPING,
      choices=[
        "The countries with higher infant mortality also have more children in the "
        "workforce.",
        "The countries with higher infant mortality have fewer children in the workforce.",
        "Infant mortality and children in the workforce vary independently here.",
        "Every country records the same infant mortality rate.",
        "Every country records the same share of children in the workforce."],
      ans=0,
      why="Sorting the countries by infant deaths leaves the share of children in the "
          "workforce strictly falling in step. EIN-1.D.2 names higher infant mortality "
          "rates and more children in the workforce together as characteristics of "
          "developing countries."),

 dict(q="Which of those four countries carries both of EIN-1.D.2's characteristics most "
        "strongly?",
      table=_T_DEVELOPING,
      choices=[
        "Country A, which leads the record on infant deaths and on children working.",
        "Country D, which trails the record on infant deaths and on children working.",
        "Country B, which stands second on both columns.",
        "Country C, which stands third on both columns.",
        "No country leads on both columns at once."],
      ans=0,
      why="The largest entry in the infant deaths column and the largest entry in the "
          "children working column fall in the same row. EIN-1.D.2 names both as "
          "characteristics of developing countries relative to developed ones."),

 dict(q="In that same four country record, how many times the lowest infant mortality is "
        "the highest?",
      table=_T_DEVELOPING,
      choices=[
        "Seventeen times.",
        "Four times.",
        "Nineteen times.",
        "Sixty eight times.",
        "Seventy two times."],
      ans=0,
      why="The largest entry in the infant deaths column is divided by the smallest. "
          "EIN-1.D.2 makes higher infant mortality one of the characteristics separating "
          "developing from developed countries."),

 dict(q="Two countries were compared on the two measures the framework names. Which of "
        "them carries the characteristics EIN-1.D.2 attributes to developing countries?",
      table=_T_PAIR,
      choices=[
        "Country M, which records the higher figure on both measures.",
        "Country N, which records the lower figure on both measures.",
        "Country M, which records the lower figure on both measures.",
        "Country N, which records the higher figure on both measures.",
        "Neither, because the two measures point in opposite directions."],
      ans=0,
      why="EIN-1.D.2 attributes higher infant mortality rates and more children in the "
          "workforce to developing countries, and one of the two columns stands higher on "
          "both measures."),

 dict(q="A country's economy moves from farming to manufacturing over several decades, and "
        "over the same decades both its birth rate and its death rate fall a long way. "
        "Which framework statement covers that account?",
      choices=[
        "The one describing a transition from high to lower birth and death rates as a "
        "country moves from a pre-industrial to an industrialized economic system.",
        "The one describing higher infant mortality rates in developing countries.",
        "The one describing more children in the workforce in developing countries.",
        "The one describing the number of stages in the model.",
        "No statement in this topic covers an account of that kind."],
      ans=0,
      why="EIN-1.D.1 joins exactly those two things: the movement of both rates from high "
          "to lower, and the country's move from a pre-industrial to an industrialized "
          "economic system."),

 dict(q="Which observations would show a region making the movement the framework "
        "describes?",
      choices=[
        "Records of both the birth rate and the death rate falling over time as the "
        "economy industrializes.",
        "A single record of the birth rate on one occasion.",
        "A single record of the death rate on one occasion.",
        "Records of the region's land area over several decades.",
        "Records of the number of species present in the region."],
      ans=0,
      why="EIN-1.D.1 describes a movement of both rates from high to lower as development "
          "occurs, so the evidence bearing on it follows both rates over time alongside "
          "the change in the economy, rather than either rate once."),

 dict(q="A student concludes from EIN-1.D.1 that every country passes through the four "
        "stages at the same pace. Why does that go beyond the framework?",
      choices=[
        "The statement says only that a four stage model typically demonstrates the "
        "transition; it makes no claim about pace or about every country.",
        "The statement says that every country passes through the stages at the same pace, "
        "so the student is right.",
        "The statement says that no country passes through more than two stages.",
        "The statement gives the number of years each stage takes in a developed country.",
        "The statement denies that a four stage model exists."],
      ans=0,
      why="EIN-1.D.1 names the four stage model as the typical way of demonstrating the "
          "transition and states nothing about how fast any country moves through it or "
          "whether every country does."),

 dict(q="Which of these does the framework NOT claim in this topic?",
      choices=[
        "Developing countries hold larger total populations than developed countries.",
        "The demographic transition runs from high to lower birth and death rates.",
        "The transition accompanies a move from a pre-industrial to an industrialized "
        "economic system.",
        "The transition is typically demonstrated through a four stage model.",
        "Developing countries have higher infant mortality rates than developed "
        "countries."],
      ans=0,
      why="EIN-1.D.1 and EIN-1.D.2 supply the four rejected statements between them. "
          "Neither says anything about the total size of a developing country's "
          "population, so that comparison is an addition to the framework."),

 dict(q="Which single sentence collects what this topic's two statements assert and "
        "nothing further?",
      choices=[
        "The demographic transition is the movement from high to lower birth and death "
        "rates as a country develops from a pre-industrial to an industrialized economy, "
        "typically demonstrated through a four stage model, and developing countries are "
        "characterised by higher infant mortality and more children in the workforce than "
        "developed ones.",
        "The demographic transition is the movement from low to higher birth and death "
        "rates as a country develops from an industrialized to a pre-industrial economy, "
        "typically demonstrated through a four stage model, and developing countries are "
        "characterised by lower infant mortality and fewer children in the workforce.",
        "The demographic transition concerns death rates only, is demonstrated through a "
        "three stage model, and says nothing about developing countries.",
        "The demographic transition is the movement of people between countries as "
        "development occurs, and developing countries differ from developed ones only in "
        "land area.",
        "The framework describes the birth rate and the death rate in each of the four "
        "stages and gives the number of years each stage lasts."],
      ans=0,
      why="EIN-1.D.1 supplies the direction of the transition, the economic change it "
          "accompanies and the four stage model, and EIN-1.D.2 supplies both "
          "characteristics of developing countries. No further detail about the stages "
          "appears in either statement."),
]
