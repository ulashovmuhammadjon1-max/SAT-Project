# AP ENVIRONMENTAL SCIENCE 5.3 The Green Revolution
# CED effective Fall 2026, Unit 5 Land and Water Use.
# Enduring understanding EIN-2: when humans use natural resources, they alter natural
# systems.
# Learning objective EIN-2.C: describe changes in agricultural practices.
# Suggested skill 3.B, describe the author's perspective and assumptions.
#
# Essential knowledge relied on, in the framework's own words:
#   EIN-2.C.1  The Green Revolution started a shift to new agricultural strategies and
#              practices in order to increase food production, with both positive and
#              negative results. Some of these strategies and methods are mechanization,
#              genetically modified organisms (GMOs), fertilization, irrigation, and the
#              use of pesticides.
#   EIN-2.C.2  Mechanization of farming can increase profits and efficiency for farms.
#              It can also increase reliance on fossil fuels.
#
# SCOPE. The framework gives a PURPOSE (to increase food production), a VERDICT (both
# positive and negative results), a LIST of five strategies, and then three specific
# consequences of mechanization: profits, efficiency, and increased reliance on fossil
# fuels. It names no country, no crop variety, no scientist and no date. No key here
# requires any of those. The five strategies are keyed as members of the framework's own
# list, never as things a student must rank or attribute to a place.
#
# BOUNDARIES INSIDE UNIT 5. The DAMAGE done by tilling, slash-and-burn farming and
# fertilizers is EIN-2.D.1 in topic 5.4; the methods and losses of irrigation are
# EIN-2.E and EIN-2.F in topic 5.5; resistance to pesticides and the genetic diversity
# cost of engineered crops are EIN-2.G in topic 5.6. This topic asks only what the Green
# Revolution shifted TO and what mechanization does, so no item here keys a consequence
# that belongs to one of those three.
#
# TEXT ANALYSIS. Skill 3.B is about an author's perspective and assumptions, so several
# items carry a short passage from an invented and clearly unattributed source -- a farm
# bulletin, a ministry report -- and ask what its author is assuming. No real document is
# quoted and no real person is named.
#
# NO FIGURES. Every quantitative item carries a table=, and all arithmetic is recomputed
# in verify_e5_3.py from that table alone.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("5.3", "The Green Revolution", 5)

_T_YIELD = dict(
    headers=["Period", "Grain harvested per hectare (tonnes)",
             "Fertilizer applied per hectare (kilograms)"],
    rows=[["Before the shift in practices", "1.0", "10"],
          ["Ten years after the shift", "2.0", "60"],
          ["Twenty years after the shift", "3.0", "150"]])

_T_MECH = dict(
    headers=["Farm", "Hours of human labour per hectare per season",
             "Litres of diesel fuel used per hectare per season"],
    rows=[["Farm using hand tools and animals", "220", "0"],
          ["Farm using tractors and harvesters", "18", "95"]])

_T_PROFIT = dict(
    headers=["Farm", "Area worked in one season (hectares)",
             "Net return over the season (currency units)"],
    rows=[["Farm using hand tools and animals", "6", "3,000"],
          ["Farm using tractors and harvesters", "150", "90,000"]])

_T_ENERGY = dict(
    headers=["Input to the farm",
             "Energy used per hectare per season (megajoules)"],
    rows=[["Diesel for machinery", "3,600"],
          ["Manufacture of the fertilizer applied", "5,400"],
          ["Pumping water for irrigation", "1,800"],
          ["Manufacture of the pesticide applied", "600"]])

_T_TWOFARMS = dict(
    headers=["Region",
             "Grain produced per hectare after the shift (tonnes)",
             "Fossil fuel energy used per hectare after the shift (megajoules)"],
    rows=[["Region A", "1.0", "2,000"],
          ["Region B", "2.0", "6,000"],
          ["Region C", "3.0", "12,000"]])

QUESTIONS = [

 dict(q="What does the course framework say the Green Revolution started?",
      choices=[
        "A shift to new agricultural strategies and practices intended to increase "
        "food production",
        "A shift away from farming and toward the collection of wild foods",
        "A shift to smaller farms worked entirely by hand in order to protect soil",
        "A programme to remove all fertilizer and pesticide use from world agriculture",
        "A treaty limiting the total area of land that could be brought into cultivation"],
      ans=0,
      why="EIN-2.C.1 states that the Green Revolution started a shift to new agricultural "
          "strategies and practices in order to increase food production. The rejected options "
          "reverse the purpose or describe a programme the framework does not mention."),

 dict(q="Which group of methods does the framework list among the strategies of that shift?",
      choices=[
        "Mechanization, genetically modified organisms, fertilization, irrigation, and "
        "the use of pesticides",
        "Terracing, windbreaks, perennial crops, and strip cropping",
        "Reforestation, prescribed burning, and the removal of affected trees",
        "Rotational grazing, free-range grazing, and the use of feedlots",
        "Permeable pavement, tree planting, and increased use of public transportation"],
      ans=0,
      why="EIN-2.C.1 names mechanization, genetically modified organisms, fertilization, "
          "irrigation, and the use of pesticides. The rejected groups are the soil conservation "
          "methods of STB-1.E.1, the forestry methods of STB-1.G, the meat production methods "
          "of EIN-2.H.1, and the urban runoff methods of STB-1.B.1."),

 dict(q="How does the framework characterise the results of the Green Revolution?",
      choices=[
        "As both positive and negative",
        "As entirely positive, with no drawbacks recorded",
        "As entirely negative, with no benefit recorded",
        "As unknown, because the results have never been measured",
        "As identical to the results of leaving the practices unchanged"],
      ans=0,
      why="EIN-2.C.1 states that the shift was made in order to increase food production, with "
          "both positive and negative results. The framework therefore refuses both of the "
          "one-sided readings and does not treat the outcome as unmeasured."),

 dict(q="According to the framework, what can mechanization of farming do for a farm's "
        "finances and operations?",
      choices=[
        "Increase profits and efficiency",
        "Increase profits while reducing efficiency",
        "Increase efficiency while reducing profits",
        "Reduce both profits and efficiency",
        "Leave profits and efficiency exactly as they were"],
      ans=0,
      why="EIN-2.C.2 states that mechanization of farming can increase profits and efficiency "
          "for farms. Each rejected option drops or reverses one half of that pairing."),

 dict(q="What further consequence of mechanization does the framework name?",
      choices=[
        "It can increase a farm's reliance on fossil fuels.",
        "It can eliminate a farm's need for any energy input at all.",
        "It can increase the genetic diversity of the crop grown.",
        "It can raise the water table beneath the farm.",
        "It can remove the need for fertilizer on the farm."],
      ans=0,
      why="EIN-2.C.2 states that mechanization can also increase reliance on fossil fuels. "
          "Genetic diversity belongs to EIN-2.G.2, the water table to EIN-2.F.1, and the "
          "framework nowhere makes machinery a substitute for fertilizer."),

 dict(q="A district recorded the values in the table across a period when new practices "
        "were adopted. Which reading is accurate?",
      table=_T_YIELD,
      choices=[
        "Grain harvested per hectare rose, and the fertilizer applied per hectare rose "
        "alongside it.",
        "Grain harvested per hectare rose while the fertilizer applied per hectare fell.",
        "Grain harvested per hectare fell while the fertilizer applied per hectare rose.",
        "Both grain harvested and fertilizer applied per hectare stayed the same.",
        "Fertilizer applied per hectare rose only after grain harvested per hectare had "
        "begun to fall."],
      ans=0,
      why="Grain runs 1.0, 2.0 and 3.0 tonnes per hectare while fertilizer runs 10, 60 and 150 "
          "kilograms, both rising with no reversal. EIN-2.C.1 names fertilization among the "
          "strategies of a shift undertaken in order to increase food production."),

 dict(q="Using the same district record, how many times as much grain per hectare was "
        "harvested twenty years after the shift as before it?",
      table=_T_YIELD,
      choices=[
        "Three times as much",
        "Two times as much",
        "Fourteen times as much",
        "Six times as much",
        "The same amount"],
      ans=0,
      why="Dividing the two tabulated yields gives 3.0 divided by 1.0, which is 3. The rejected "
          "values come from the ten-year row, from the fertilizer ratio, or from denying that "
          "the yields differ."),

 dict(q="From the same record, by how many kilograms per hectare did fertilizer use rise "
        "across the whole period?",
      table=_T_YIELD,
      choices=[
        "A rise of 140 kilograms per hectare",
        "A rise of 150 kilograms per hectare",
        "A rise of 90 kilograms per hectare",
        "A rise of 50 kilograms per hectare",
        "A rise of 160 kilograms per hectare"],
      ans=0,
      why="Subtracting the first and last tabulated values gives 150 minus 10, which is 140 "
          "kilograms per hectare. The rejected values quote the final figure alone, pair the "
          "wrong rows, or add the first and last instead of differencing them."),

 dict(q="Two farms of the same size and crop are compared in the table. What do the two "
        "columns together illustrate about mechanization?",
      table=_T_MECH,
      choices=[
        "It cuts the human labour a hectare needs while introducing a fuel requirement "
        "that was not there before.",
        "It cuts both the human labour and the fuel a hectare needs.",
        "It raises both the human labour and the fuel a hectare needs.",
        "It raises the human labour a hectare needs while cutting the fuel it needs.",
        "It leaves both the human labour and the fuel a hectare needs unchanged."],
      ans=0,
      why="Labour falls from 220 hours to 18 while diesel rises from none to 95 litres per "
          "hectare per season. EIN-2.C.2 names both sides of that trade when it says "
          "mechanization can increase efficiency and can also increase reliance on fossil fuels."),

 dict(q="Using the same two farms, how many hours of human labour per hectare does the "
        "mechanized farm save in a season?",
      table=_T_MECH,
      choices=[
        "202 hours",
        "220 hours",
        "18 hours",
        "95 hours",
        "238 hours"],
      ans=0,
      why="Subtracting the two tabulated labour figures gives 220 minus 18, which is 202 hours "
          "per hectare per season. The rejected values are the two labour figures themselves, "
          "the diesel figure, and the sum of the two labour figures."),

 dict(q="Two farms are compared by area worked and by net return over one season. What does "
        "the comparison support, given the framework?",
      table=_T_PROFIT,
      choices=[
        "The mechanized farm worked far more land and returned far more over the season, "
        "which is the profit and efficiency the framework attributes to mechanization.",
        "The mechanized farm worked far more land but returned less over the season, which "
        "contradicts the framework.",
        "The two farms worked the same area and returned the same amount, so mechanization "
        "made no difference.",
        "The unmechanized farm worked more land, which is the efficiency the framework "
        "attributes to mechanization.",
        "Neither farm returned anything over the season, so no comparison is possible."],
      ans=0,
      why="The mechanized farm worked 150 hectares against 6 and returned 90,000 currency units "
          "against 3,000. EIN-2.C.2 states that mechanization of farming can increase profits "
          "and efficiency for farms, and both tabulated columns move that way."),

 dict(q="Using the same two farms, what is the net return per hectare on the mechanized "
        "farm, and how does it compare with the other farm?",
      table=_T_PROFIT,
      choices=[
        "600 currency units per hectare, which is more than the 500 on the "
        "unmechanized farm",
        "600 currency units per hectare, which is less than the 500 on the "
        "unmechanized farm",
        "500 currency units per hectare, which equals the return on the unmechanized farm",
        "90,000 currency units per hectare, which is the whole season's return",
        "150 currency units per hectare, which is the area worked"],
      ans=0,
      why="Dividing gives 90,000 over 150, which is 600 currency units per hectare, against "
          "3,000 over 6, which is 500. The rejected options reverse the comparison, treat the "
          "whole-season return as a per-hectare figure, or quote the area as if it "
          "were a return."),

 dict(q="A farm bulletin states: \"Every hectare we bring under the new methods produces "
        "more grain than it did before, so the new methods are an unqualified improvement "
        "on the old ones.\" Which assumption is the author making?",
      choices=[
        "That output per hectare is the only result worth counting when the two methods "
        "are compared",
        "That output per hectare has fallen under the new methods",
        "That the old methods used more fertilizer than the new ones",
        "That the new methods are used on only a small share of the land",
        "That grain is less valuable than the crops it replaced"],
      ans=0,
      why="The author moves from a single measured gain to the word unqualified, which requires "
          "that nothing else counts. EIN-2.C.1 states that the shift produced BOTH positive and "
          "negative results, so the framework itself denies the assumption the author needs."),

 dict(q="A ministry report states: \"Mechanization has raised our farms' output per worker "
        "and their profits, and it has done so without any change in what the farms "
        "consume.\" Which part of that sentence does the framework contradict?",
      choices=[
        "The claim that nothing the farms consume has changed, since mechanization can "
        "increase reliance on fossil fuels",
        "The claim that output per worker has risen, since mechanization cannot raise "
        "efficiency",
        "The claim that profits have risen, since mechanization cannot raise profits",
        "The whole sentence, since the framework says mechanization has no measurable "
        "effects",
        "None of the sentence, since the framework agrees with every part of it"],
      ans=0,
      why="EIN-2.C.2 affirms the profit and efficiency half of the sentence and then adds that "
          "mechanization can also increase reliance on fossil fuels, which is a change in what "
          "the farms consume. Only the final clause is at odds with the framework."),

 dict(q="Energy inputs on one mechanized and irrigated farm were totalled by category. "
        "Which input accounted for the largest share?",
      table=_T_ENERGY,
      choices=[
        "The manufacture of the fertilizer applied",
        "The diesel burned by the machinery",
        "The pumping of water for irrigation",
        "The manufacture of the pesticide applied",
        "The four inputs were equal"],
      ans=0,
      why="The tabulated values are 3,600, 5,400, 1,800 and 600 megajoules per hectare per "
          "season, so fertilizer manufacture is the largest. Fertilization, irrigation, "
          "mechanization and pesticide use are four of the five strategies EIN-2.C.1 lists."),

 dict(q="Using the same energy accounting, what total energy is used per hectare per season "
        "across all four inputs?",
      table=_T_ENERGY,
      choices=[
        "11,400 megajoules",
        "9,000 megajoules",
        "5,400 megajoules",
        "10,800 megajoules",
        "3,600 megajoules"],
      ans=0,
      why="Adding the four tabulated values gives 3,600 plus 5,400 plus 1,800 plus 600, which "
          "is 11,400 megajoules per hectare per season. The rejected values omit one or more of "
          "the categories or quote a single row."),

 dict(q="Three regions adopted the new practices to different degrees. What relationship do "
        "the values show?",
      table=_T_TWOFARMS,
      choices=[
        "Regions producing more grain per hectare also used more fossil fuel energy "
        "per hectare.",
        "Regions producing more grain per hectare used less fossil fuel energy per hectare.",
        "Grain production per hectare and fossil fuel energy per hectare are unrelated in "
        "these data.",
        "All three regions used the same fossil fuel energy per hectare.",
        "The region producing the least grain per hectare used the most fossil fuel "
        "energy per hectare."],
      ans=0,
      why="Grain runs 1.0, 2.0 and 3.0 tonnes per hectare while fossil fuel energy runs 2,000, "
          "6,000 and 12,000 megajoules, rising together with no reversal. EIN-2.C.1 records "
          "both positive and negative results, and EIN-2.C.2 names increased reliance on fossil "
          "fuels as one of them."),

 dict(q="Using the same three regions, how much fossil fuel energy is used per tonne of "
        "grain in the region producing the least grain per hectare?",
      table=_T_TWOFARMS,
      choices=[
        "2,000 megajoules per tonne",
        "3,000 megajoules per tonne",
        "4,000 megajoules per tonne",
        "6,000 megajoules per tonne",
        "1,000 megajoules per tonne"],
      ans=0,
      why="Dividing that region's 2,000 megajoules by its 1.0 tonne gives 2,000 megajoules per "
          "tonne. The rejected values are the other two regions' figures per tonne, another "
          "region's energy total, and half the correct quotient."),

 dict(q="Which of the following is the best statement of the PURPOSE the framework "
        "attributes to the shift in practices?",
      choices=[
        "To increase food production",
        "To reduce the total area of land under cultivation",
        "To lower the amount of fertilizer used per hectare",
        "To restore soil that earlier farming had eroded",
        "To end the use of machinery on farms"],
      ans=0,
      why="EIN-2.C.1 states that the shift was made IN ORDER TO INCREASE FOOD PRODUCTION. "
          "Reducing cultivated area, lowering fertilizer use and restoring soil are not the "
          "purposes the framework assigns, and machinery is one of the strategies rather than "
          "something the shift removed."),

 dict(q="A student lists four practices of the Green Revolution and includes contour "
        "plowing among them. Which correction follows from the framework?",
      choices=[
        "Contour plowing is a soil conservation method rather than one of the strategies "
        "the framework lists for this shift.",
        "Contour plowing belongs on the list, because the framework names it among "
        "the strategies.",
        "Contour plowing is a method of meat production rather than of crop farming.",
        "Contour plowing is a method of pest control rather than a farming practice.",
        "The framework lists no strategies at all, so no correction is possible."],
      ans=0,
      why="EIN-2.C.1 names mechanization, genetically modified organisms, fertilization, "
          "irrigation, and the use of pesticides, and contour plowing is not among them; "
          "STB-1.E.1 lists it under soil conservation instead. The framework does supply a "
          "list, so the last option is wrong on its face."),

 dict(q="Which pair of measurements would together best test the framework's claim that "
        "mechanization increases both efficiency and reliance on fossil fuels?",
      choices=[
        "Output per hour of human labour, and litres of fuel burned per hectare",
        "Output per hectare, and the number of crop species grown on the farm",
        "The price of grain at market, and the distance to the nearest town",
        "The number of tractors owned, and the age of the farm's owner",
        "The depth of the topsoil, and the number of rainy days in the season"],
      ans=0,
      why="EIN-2.C.2 makes two claims, one about efficiency and one about fossil fuel reliance, "
          "so the test needs one measurement of each. Output per hour of labour is efficiency "
          "and fuel per hectare is fossil fuel reliance; the rejected pairs measure neither or "
          "only one."),

 dict(q="Why does the framework describe genetically modified organisms as a strategy of the "
        "shift rather than as a result of it?",
      choices=[
        "The framework lists them among the methods adopted in order to increase "
        "food production.",
        "The framework lists them among the negative results the shift produced.",
        "The framework lists them among the soil conservation practices.",
        "The framework does not mention genetically modified organisms in this topic "
        "at all.",
        "The framework lists them as a consequence of increased mechanization."],
      ans=0,
      why="EIN-2.C.1 places genetically modified organisms in its list of strategies and "
          "methods, alongside mechanization, fertilization, irrigation and the use of "
          "pesticides, and that list is introduced as the means by which food production was "
          "to be increased."),

 dict(q="An advisory note states: \"Because the new practices raised yields, no farmer who "
        "adopts them can be worse off in any respect.\" How does the framework bear on "
        "this reasoning?",
      choices=[
        "It undercuts the reasoning, because the framework records negative as well as "
        "positive results from the shift.",
        "It supports the reasoning, because the framework records only positive results "
        "from the shift.",
        "It is silent on the reasoning, because the framework makes no claim about results.",
        "It undercuts the reasoning, because the framework denies that yields rose at all.",
        "It supports the reasoning, because the framework says higher yields remove every "
        "other consideration."],
      ans=0,
      why="EIN-2.C.1 states that the shift produced BOTH positive AND negative results, so a "
          "yield gain does not by itself establish that nothing was lost. The framework does "
          "record the purpose of increasing food production, so the option denying any "
          "yield change misreads it."),

 dict(q="Which of the following describes an increase in reliance on fossil fuels of exactly "
        "the kind the framework attaches to mechanization?",
      choices=[
        "A farm that replaces animal-drawn implements with diesel machinery and therefore "
        "buys fuel every season",
        "A farm that replaces diesel machinery with animal-drawn implements and therefore "
        "buys no fuel",
        "A farm that plants a wider mixture of crop varieties in the same field",
        "A farm that lines its irrigation channels to reduce seepage",
        "A farm that leaves a strip of land uncultivated along a stream"],
      ans=0,
      why="EIN-2.C.2 states that mechanization can increase reliance on fossil fuels, and "
          "substituting diesel machinery for animal power is that increase. The rejected "
          "options reduce fuel use or describe practices the framework places elsewhere in "
          "the unit."),

 dict(q="A regional planner argues that the framework's account of the Green Revolution is "
        "one-sided in favour of the new practices. Which feature of the framework's own "
        "wording answers that argument?",
      choices=[
        "It says the shift produced both positive and negative results.",
        "It says the shift produced only positive results.",
        "It says the shift produced only negative results.",
        "It refuses to name any of the strategies involved in the shift.",
        "It says the shift had no effect on food production."],
      ans=0,
      why="EIN-2.C.1 contains the phrase WITH BOTH POSITIVE AND NEGATIVE RESULTS, which is "
          "exactly a two-sided verdict. The framework also names five strategies and gives the "
          "purpose as increasing food production, so the remaining options misdescribe it."),

 dict(q="Which of the five listed strategies does the framework single out for a further "
        "statement of its own, and what does that statement add?",
      choices=[
        "Mechanization, which can raise profits and efficiency and can also raise reliance "
        "on fossil fuels",
        "Irrigation, which can raise the water table and inhibit root function",
        "The use of pesticides, which can lead to resistance through artificial selection",
        "Genetically modified organisms, which can reduce the genetic diversity of a crop",
        "Fertilization, which can add nutrients to nearby waterways"],
      ans=0,
      why="EIN-2.C.2 is the framework's second statement in this topic and it is about "
          "mechanization alone. The other four claims are real framework statements but they "
          "belong to EIN-2.F.1, EIN-2.G.1, EIN-2.G.2 and other topics rather than to 5.3."),

 dict(q="Using the district record of yields and fertilizer, what happened to the amount of "
        "fertilizer needed for each tonne of grain across the period?",
      table=_T_YIELD,
      choices=[
        "It rose from 10 kilograms per tonne to 50 kilograms per tonne.",
        "It fell from 50 kilograms per tonne to 10 kilograms per tonne.",
        "It stayed at 10 kilograms per tonne throughout the period.",
        "It rose from 10 kilograms per tonne to 30 kilograms per tonne.",
        "It cannot be worked out, because the table reports no yields."],
      ans=0,
      why="Dividing fertilizer by yield gives 10 over 1.0, which is 10, and 150 over 3.0, "
          "which is 50 kilograms per tonne, so more fertilizer was needed per tonne at "
          "the end. EIN-2.C.1 records both positive and negative results from the shift, and "
          "this reading is one of each in the same data."),

 dict(q="Which statement correctly relates the two essential knowledge statements of "
        "this topic?",
      choices=[
        "The first describes the shift and lists its strategies; the second takes one of "
        "those strategies and states what it does for and to a farm.",
        "The first and the second describe two different shifts that happened in "
        "different centuries.",
        "The second contradicts the first by removing mechanization from the list "
        "of strategies.",
        "The two statements describe the same consequences in different words.",
        "The second concerns forestry rather than farming and does not connect to "
        "the first."],
      ans=0,
      why="EIN-2.C.1 introduces the shift, its purpose, its mixed results and its five "
          "strategies, and EIN-2.C.2 then develops mechanization, one member of that list, into "
          "profits, efficiency and fossil fuel reliance. The second therefore elaborates the "
          "first rather than contradicting or repeating it."),

 dict(q="A cooperative wants to keep the yield gains of the new practices while reducing the "
        "fossil fuel reliance the framework warns of. Which measurement should it watch to "
        "know whether it is succeeding on the second aim?",
      choices=[
        "The fuel energy the farm consumes for each tonne of grain it produces",
        "The number of hours its workers spend in the field each season",
        "The market price its grain fetches at the end of the season",
        "The number of hectares it holds title to",
        "The number of different machines parked in its yard"],
      ans=0,
      why="EIN-2.C.2 names increased reliance on fossil fuels as the consequence in question, "
          "and fuel energy per tonne of output is that reliance measured against the yield the "
          "cooperative wants to keep. Labour hours, price, area and machine count each leave "
          "one of the two aims unmeasured."),

 dict(q="Which summary of this topic keeps every element the framework states and adds "
        "nothing?",
      choices=[
        "New practices were adopted to raise food production, with mixed results, and "
        "mechanization in particular raised profits and efficiency while raising reliance "
        "on fossil fuels.",
        "New practices were adopted to lower food production, with uniformly good results, "
        "and mechanization lowered profits.",
        "New practices were adopted to raise food production and succeeded without any "
        "drawback, and mechanization had no effect on fuel use.",
        "New practices were abandoned in order to protect soil, and mechanization was "
        "removed from farms.",
        "New practices raised food production only in countries that already had "
        "machinery, and had no other consequences."],
      ans=0,
      why="EIN-2.C.1 supplies the purpose, the mixed verdict and the list of strategies, and "
          "EIN-2.C.2 supplies mechanization's profits, efficiency and fossil fuel reliance. The "
          "keyed summary carries all of that; each rejected summary reverses the purpose, drops "
          "the negative results, or adds a condition the framework does not state."),
]
