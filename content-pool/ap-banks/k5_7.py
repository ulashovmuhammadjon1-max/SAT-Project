# AP COMPARATIVE GOVERNMENT AND POLITICS 5.7 Impact of Industrialization and
# Economic Development
# CED effective Fall 2026, Unit 5 Political and Economic Changes and Development.
# Enduring understanding LEG-3; learning objective LEG-3.C (explain how rapid
# industrialization and economic development have produced radical changes in
# governmental policies). Suggested skill 5.D, Argumentation (use refutation,
# concession, or rebuttal in responding to opposing or alternate perspectives).
#
# Essential knowledge relied on:
#   LEG-3.C.1  RAPID INDUSTRIALIZATION and INCREASING DEPENDENCE ON ENERGY FROM
#              FOSSIL FUELS have created ENVIRONMENTAL AND POLITICAL PROBLEMS THAT
#              GOVERNMENTS MUST ADDRESS TO PROTECT CITIZENS. Solutions include:
#     .a PHYSICALLY MOVING FACTORIES, IMPLEMENTING GREEN TECHNOLOGIES WITH SUBSIDIES
#        FOR INDUSTRY COMPLIANCE, and INCREASED INFRASTRUCTURE DEVELOPMENT AND
#        ENVIRONMENTAL REGULATION
#     .b PASSING LAWS THAT REQUIRE NATIONWIDE CONVERSION TO HYBRID AND
#        BATTERY-POWERED AUTOS to address AIR POLLUTION PROBLEMS IN MAJOR CITIES FROM
#        AUTO AND INDUSTRIAL EMISSIONS
#     .c DEVELOPING INFRASTRUCTURE AND OTHER MECHANISMS TO RESPOND TO HEALTH CRISES
#        RELATED TO SYSTEMIC POLLUTION
#   LEG-3.C.2  TRADE LIBERALIZATION AFFECTS the GROWTH OF DOMESTIC AND FOREIGN
#              BUSINESS, the AMOUNT OF DIRECT FOREIGN INVESTMENT, FOREIGN EXCHANGE
#              RATES, POPULATION MOVEMENT, and often the QUALITY OF THE ENVIRONMENT.
#              REDUCING TARIFFS MAY LOWER CONSUMER COSTS AT THE EXPENSE OF DOMESTIC
#              INDUSTRY, while INCREASING TARIFFS MAY PROTECT DOMESTIC INDUSTRY
#              AGAINST FOREIGN IMPORTS BUT AT THE EXPENSE OF HIGHER CONSUMER PRICES
#   LEG-3.C.3  governments concerned with BUDGET DEFICITS RESULTING FROM WORLD MARKET
#              FLUCTUATIONS often must adopt AUSTERITY MEASURES, which result in
#              FUNDING CUTS TO STATE PROGRAMS
#
# LEG-3.C.2 IS A SYMMETRICAL TRADE-OFF, AND THAT IS THE TOPIC'S BEST ITEM. The
# framework states a cost on BOTH sides in one sentence: cutting tariffs lowers
# consumer costs AT THE EXPENSE OF domestic industry, and raising them protects
# domestic industry AT THE EXPENSE OF higher consumer prices. Neither direction is
# free, which is exactly what a refutation-and-concession item needs. Items 7, 8,
# 11, 18 and the first table all rest on it, and the table's check requires the two
# columns to move in OPPOSITE directions, since a table where both improved would
# make the key false while the item still looked answerable.
#
# LEG-3.C.1's THREE SOLUTIONS ARE NOT INTERCHANGEABLE. Item .a acts on where
# production happens and how it is regulated, .b is a single nationwide mandate
# aimed at a named problem, and .c is a response AFTER harm has occurred rather
# than prevention of it. Items 12, 13 and 27-29 key those differences.
#
# LEG-3.C.3 SUPPLIES THE CAUSAL CHAIN students shorten: world market fluctuations
# produce budget deficits, deficits produce austerity, austerity produces funding
# cuts to state programs. Items 9, 10, 17, 19 and 20 keep all three links, because
# an answer that starts at austerity has dropped the reason the framework gives.
#
# NOTHING HERE TURNS ON CURRENT EVENTS: no country's tariff schedule, budget,
# emissions rule or programme is asserted. Every table figure is HYPOTHETICAL and
# labelled so.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md.
TOPIC = ("5.7", "Impact of Industrialization and Economic Development", 5)

_T_TRADEOFF = dict(
    headers=["Tariff policy (hypothetical)", "Consumer price index",
             "Domestic manufacturing employment index"],
    rows=[["Tariffs reduced", "86", "79"],
          ["Tariffs unchanged", "100", "100"],
          ["Tariffs increased", "117", "112"]])

_T_AUSTERITY = dict(
    headers=["State programme", "Funding before the austerity measures (index)",
             "Funding after the austerity measures (index)"],
    rows=[["Public transport", "100", "78"],
          ["Adult training", "100", "64"],
          ["Environmental inspection", "100", "71"]])

_T_SOLUTION = dict(
    headers=["Measure (hypothetical)", "What the government did"],
    rows=[["Measure 1", "Relocated factories away from residential districts, paid subsidies to firms adopting cleaner technology, and tightened environmental regulation"],
          ["Measure 2", "Passed a law requiring the whole country to convert to hybrid and battery-powered vehicles"],
          ["Measure 3", "Built clinics and monitoring networks to respond to illness caused by long-term pollution"]])

QUESTIONS = [
 dict(q="What does the framework identify as having created the environmental and political problems governments must now address?",
   choices=[
     "rapid industrialization and increasing dependence on energy from fossil fuels",
     "the growth of political parties and the widening of the franchise",
     "the transfer of sovereignty to supranational organizations",
     "the reduction of tariffs by international agreement",
     "the migration of people between states"], ans=0,
   why="EK LEG-3.C.1 states that rapid industrialization and increasing dependence on energy from fossil fuels have created a variety of environmental and political problems that governments must address."),
 dict(q="For what reason does the framework say governments must address those problems?",
   choices=[
     "to protect citizens",
     "to satisfy the conditions attached to foreign loans",
     "to comply with the rules of a supranational organization",
     "to attract multinational corporations",
     "to raise tariff revenue"], ans=0,
   why="EK LEG-3.C.1 states that these are problems governments must address to protect citizens, which places the obligation in the relationship between a government and its own people."),
 dict(q="Which set of measures does the framework list as a government solution to those problems?",
   choices=[
     "physically moving factories, implementing green technologies with subsidies for industry compliance, and engaging in increased infrastructure development and environmental regulation",
     "raising tariffs, cutting subsidies, and privatizing state industries",
     "creating special economic zones and inviting foreign investment",
     "reducing the number of registered parties and raising thresholds",
     "adopting gender quotas and expanding literacy programmes"], ans=0,
   why="EK LEG-3.C.1.a names physically moving factories, implementing green technologies with subsidies for industry compliance, and engaging in increased infrastructure development and environmental regulation."),
 dict(q="What does the framework say laws requiring nationwide conversion to hybrid and battery-powered autos are meant to address?",
   choices=[
     "air pollution problems in major cities from auto and industrial emissions",
     "budget deficits caused by world market fluctuations",
     "unequal access to education between regions",
     "the shortage of foreign direct investment",
     "the concentration of wealth in a few hands"], ans=0,
   why="EK LEG-3.C.1.b states that such laws address air pollution problems in major cities from auto and industrial emissions, which names both the place and the two sources of the pollution."),
 dict(q="To what does the framework say governments develop infrastructure and other mechanisms to respond?",
   choices=[
     "health crises related to systemic pollution",
     "shortfalls in tariff revenue",
     "declining demand for raw materials",
     "the demands of supranational organizations",
     "the movement of people between states"], ans=0,
   why="EK LEG-3.C.1.c states that governments develop infrastructure and other mechanisms to respond to health crises related to systemic pollution, which is a response to harm that has already occurred."),
 dict(q="Which set of things does the framework say trade liberalization affects?",
   choices=[
     "the growth of domestic and foreign business, direct foreign investment, foreign exchange rates, population movement, and often the quality of the environment",
     "the number of political parties, the length of terms, and the size of the legislature",
     "the composition of the judiciary and the rules for appointing judges",
     "the boundaries of electoral districts and the registration of candidates",
     "military spending, conscription, and treaty membership"], ans=0,
   why="EK LEG-3.C.2 names the growth of domestic and foreign business, the amount of direct foreign investment, foreign exchange rates, population movement, and often the quality of the environment as what trade liberalization affects."),
 dict(q="According to the framework, what is the cost of reducing tariffs?",
   choices=[
     "lower consumer costs come at the expense of domestic industry",
     "lower consumer costs come at the expense of higher consumer prices",
     "there is no cost, since consumers and industry both gain",
     "domestic industry is protected at the expense of consumers",
     "the cost falls entirely on foreign exporters"], ans=0,
   why="EK LEG-3.C.2 states that reducing tariffs may lower consumer costs at the expense of domestic industry, so the gain and the cost fall on different groups within the same country."),
 dict(q="According to the framework, what is the cost of increasing tariffs?",
   choices=[
     "domestic industry is protected against foreign imports at the expense of higher consumer prices",
     "consumers pay less while domestic industry contracts",
     "there is no cost, since domestic industry is protected",
     "the cost falls entirely on foreign exporters",
     "government revenue falls while consumer prices also fall"], ans=0,
   why="EK LEG-3.C.2 states that increasing tariffs may protect domestic industry against foreign imports but at the expense of higher consumer prices, which is the mirror image of the cost of cutting them."),
 dict(q="What does the framework identify as the source of the budget deficits that lead governments to austerity?",
   choices=[
     "world market fluctuations",
     "the abolition of tariffs by treaty",
     "the growth of the middle class",
     "the imposition of gender quotas",
     "the conversion of vehicle fleets to battery power"], ans=0,
   why="EK LEG-3.C.3 states that governments concerned with budget deficits resulting from world market fluctuations often must adopt austerity measures, so the chain begins outside the country's own decisions."),
 dict(q="What does the framework say austerity measures result in?",
   choices=[
     "funding cuts to state programs",
     "increases in tariff rates",
     "the nationalization of private industry",
     "the creation of new social welfare programmes",
     "the transfer of budget authority to a supranational organization"], ans=0,
   why="EK LEG-3.C.3 states that austerity measures result in funding cuts to state programs, which is the framework's own statement of what the measures amount to in practice."),
 dict(q="A student concludes from the framework that a government can settle its tariff policy without accepting any disadvantage. What is wrong with that conclusion?",
   choices=[
     "the framework attaches a cost to each direction, since cutting tariffs burdens domestic industry and raising them burdens consumers",
     "the framework says tariffs have no effect on either consumers or industry",
     "the framework says only tariff increases have costs",
     "the framework says only tariff reductions have costs",
     "the framework says tariff policy is decided by supranational organizations"], ans=0,
   why="EK LEG-3.C.2 states both costs in one sentence, so the choice is between two distributions of gain and loss rather than between a good option and a bad one."),
 dict(q="How do the first two of the framework's solutions to industrial pollution differ from each other?",
   choices=[
     "one acts on where production takes place and how it is regulated, while the other is a single nationwide requirement about the vehicles people use",
     "one addresses pollution and the other addresses budget deficits",
     "one is a domestic measure and the other is imposed by an international organization",
     "one concerns education policy and the other concerns health care",
     "they are two descriptions of the same measure"], ans=0,
   why="EK LEG-3.C.1.a moves factories, subsidizes cleaner technology and tightens regulation, while EK LEG-3.C.1.b passes laws requiring nationwide conversion to hybrid and battery-powered autos, so one reshapes production and the other mandates a change in what is driven."),
 dict(q="What distinguishes the framework's third solution from its first two?",
   choices=[
     "it responds to harm that has already occurred rather than preventing the pollution",
     "it is the only one that involves government spending",
     "it is the only one that applies nationwide",
     "it is the only one that concerns fossil fuels",
     "it is the only one adopted by democratic governments"], ans=0,
   why="EK LEG-3.C.1.c has governments develop infrastructure and other mechanisms to respond to health crises related to systemic pollution, whereas EK LEG-3.C.1.a and EK LEG-3.C.1.b act on the sources of the pollution itself."),
 dict(q="A government moves several plants out of a crowded district, pays firms to install cleaner equipment, and tightens the rules those firms must meet. Which of the framework's solutions does this match?",
   choices=[
     "physically moving factories, implementing green technologies with subsidies for compliance, and increasing environmental regulation",
     "passing a law requiring nationwide conversion to hybrid and battery-powered autos",
     "developing infrastructure to respond to health crises related to systemic pollution",
     "adopting austerity measures in response to a budget deficit",
     "reducing tariffs to lower consumer costs"], ans=0,
   why="EK LEG-3.C.1.a names physically moving factories, implementing green technologies with subsidies for industry compliance, and increased environmental regulation, and the scenario contains all three."),
 dict(q="A legislature enacts a statute requiring every vehicle sold anywhere in the country to be hybrid or battery-powered, citing the air in its largest cities. Which of the framework's solutions does this match?",
   choices=[
     "passing laws that require nationwide conversion to hybrid and battery-powered autos",
     "physically moving factories away from residential districts",
     "developing infrastructure to respond to health crises related to systemic pollution",
     "adopting austerity measures after a budget deficit",
     "raising tariffs to protect domestic industry"], ans=0,
   why="EK LEG-3.C.1.b names passing laws that require nationwide conversion to hybrid and battery-powered autos to address air pollution problems in major cities from auto and industrial emissions, and the scenario states both the mandate and that reason."),
 dict(q="A government builds clinics and a monitoring network in districts where long-term pollution has made people ill. Which of the framework's solutions does this match?",
   choices=[
     "developing infrastructure and other mechanisms to respond to health crises related to systemic pollution",
     "implementing green technologies with subsidies for industry compliance",
     "passing laws requiring nationwide conversion to hybrid vehicles",
     "adopting austerity measures in response to world market fluctuations",
     "reducing tariffs to lower consumer costs"], ans=0,
   why="EK LEG-3.C.1.c names developing infrastructure and other mechanisms to respond to health crises related to systemic pollution, which is what clinics and monitoring in affected districts are."),
 dict(q="World prices for a country's main export fall sharply, its budget moves into deficit, and it announces reductions in several programmes. Which framework claim does this illustrate?",
   choices=[
     "that governments concerned with budget deficits resulting from world market fluctuations often must adopt austerity measures resulting in funding cuts to state programs",
     "that trade liberalization affects foreign exchange rates and population movement",
     "that rapid industrialization creates environmental problems governments must address",
     "that laws may require nationwide conversion to hybrid vehicles",
     "that reducing tariffs lowers consumer costs at the expense of domestic industry"], ans=0,
   why="EK LEG-3.C.3 runs from world market fluctuations through budget deficits to austerity measures and then to funding cuts to state programs, and the scenario follows that chain from beginning to end."),
 dict(q="A commentator argues that cutting tariffs is simply good policy because prices fall. Which rebuttal is best supported by the framework?",
   choices=[
     "The framework grants that consumer costs may fall and states in the same sentence that this comes at the expense of domestic industry",
     "The framework denies that cutting tariffs lowers consumer costs",
     "The framework states that cutting tariffs raises consumer prices",
     "The framework states that tariffs have no effect on domestic industry",
     "The framework states that tariff policy has no economic effects at all"], ans=0,
   why="EK LEG-3.C.2 states that reducing tariffs may lower consumer costs at the expense of domestic industry, so the rebuttal concedes the benefit and names the cost the same sentence attaches to it."),
 dict(q="A commentator argues that austerity shows a government has chosen to abandon its social commitments. Which reply is best supported by the framework?",
   choices=[
     "The framework presents austerity as something governments concerned with deficits arising from world market fluctuations often must adopt, so the pressure begins outside the government's own choices even though the cuts are its own",
     "The framework states that austerity measures never reduce funding for state programmes",
     "The framework states that budget deficits have no external causes",
     "The framework states that austerity is required by supranational organizations",
     "The framework states that governments are free to ignore budget deficits"], ans=0,
   why="EK LEG-3.C.3 states that governments concerned with budget deficits resulting from world market fluctuations often must adopt austerity measures, which result in funding cuts to state programs, so both the external pressure and the domestic cuts belong to the statement."),
 dict(q="Which finding would most strongly support a claim that a government's spending cuts followed the pattern the framework describes?",
   choices=[
     "Prices for the country's principal export collapsed, the budget fell into deficit the following year, and programme funding was reduced across several ministries",
     "The government reduced programme funding in a year of record export earnings and budget surplus",
     "The government increased programme funding after joining a supranational organization",
     "The government raised tariffs and consumer prices rose",
     "The government relocated several factories away from residential districts"], ans=0,
   why="EK LEG-3.C.3 names world market fluctuations as the source of the deficits that lead to austerity measures and funding cuts to state programs, so the supporting finding must contain the external shock, the deficit and the cuts in that order."),
 dict(q="The table models one hypothetical economy under three tariff settings. Which conclusion does it support?",
   table=_T_TRADEOFF,
   choices=[
     "Consumer prices and domestic manufacturing employment move in the same direction as the tariff, so neither setting improves both at once",
     "Both consumer prices and domestic manufacturing employment improve when tariffs are reduced",
     "Both consumer prices and domestic manufacturing employment improve when tariffs are increased",
     "Tariff settings leave both figures unchanged",
     "Consumer prices fall as tariffs rise"], ans=0,
   why="EK LEG-3.C.2 states that reducing tariffs may lower consumer costs at the expense of domestic industry while increasing tariffs may protect domestic industry at the expense of higher consumer prices, and the table shows both columns rising and falling together with the tariff."),
 dict(q="According to the same table, the range of the consumer price index across the three settings is",
   table=_T_TRADEOFF,
   choices=[
     "31 points",
     "17 points",
     "14 points",
     "33 points",
     "21 points"], ans=0,
   why="Subtracting the smallest consumer price figure from the largest gives the range. The alternatives are the two gaps between neighbouring settings, the range of the other column, and a gap within that other column."),
 dict(q="Using the same table, the range of the domestic manufacturing employment index across the three settings is",
   table=_T_TRADEOFF,
   choices=[
     "33 points",
     "12 points",
     "21 points",
     "31 points",
     "17 points"], ans=0,
   why="Subtracting the smallest employment figure from the largest gives the range. The alternatives are the two gaps between neighbouring settings, the range of the other column, and a gap within that other column."),
 dict(q="The table reports hypothetical funding for three state programmes before and after a package of austerity measures. Which programme was cut by the most?",
   table=_T_AUSTERITY,
   choices=[
     "adult training, cut by 36 points",
     "public transport, cut by 22 points",
     "environmental inspection, cut by 29 points",
     "none of them, since austerity measures do not reduce programme funding",
     "all three by the same amount"], ans=0,
   why="EK LEG-3.C.3 states that austerity measures result in funding cuts to state programs, and subtracting each row's later figure from its earlier one shows which programme lost the most."),
 dict(q="According to the same table of programmes, the total reduction across all three is",
   table=_T_AUSTERITY,
   choices=[
     "87 points",
     "65 points",
     "58 points",
     "51 points",
     "36 points"], ans=0,
   why="Adding the three reductions gives the total. The alternatives are the total with each row omitted in turn and the largest single reduction."),
 dict(q="Using the same table of programmes, the difference between the largest and smallest reductions is",
   table=_T_AUSTERITY,
   choices=[
     "14 points",
     "7 points",
     "36 points",
     "29 points",
     "22 points"], ans=0,
   why="Working out each programme's reduction and subtracting the smallest from the largest gives the answer. The alternatives are the gap between the other two reductions and the three reductions themselves read as a difference."),
 dict(q="The table describes three hypothetical measures. Which one matches EK LEG-3.C.1.a?",
   table=_T_SOLUTION,
   choices=[
     "the measure that relocated factories, paid subsidies for cleaner technology, and tightened environmental regulation",
     "the measure that required the whole country to convert to hybrid and battery-powered vehicles",
     "the measure that built clinics and monitoring networks",
     "none of the three, since that statement names no measures",
     "all three, since each concerns pollution"], ans=0,
   why="EK LEG-3.C.1.a names physically moving factories, implementing green technologies with subsidies for industry compliance, and increased infrastructure development and environmental regulation, and only one measure in the table contains all of those."),
 dict(q="Using the same table of measures, which one matches EK LEG-3.C.1.b?",
   table=_T_SOLUTION,
   choices=[
     "the measure requiring the whole country to convert to hybrid and battery-powered vehicles",
     "the measure that relocated factories and tightened environmental regulation",
     "the measure that built clinics and monitoring networks",
     "none of the three, since that statement names no measures",
     "all three, since each was adopted by a government"], ans=0,
   why="EK LEG-3.C.1.b names passing laws that require nationwide conversion to hybrid and battery-powered autos, and only one measure in the table is a nationwide vehicle requirement."),
 dict(q="Using the same table of measures, which one responds to harm already done rather than to its source?",
   table=_T_SOLUTION,
   choices=[
     "the measure that built clinics and monitoring networks to respond to illness caused by long-term pollution",
     "the measure that relocated factories away from residential districts",
     "the measure requiring conversion to hybrid and battery-powered vehicles",
     "none of the three, since all three prevent pollution",
     "all three, since each follows a period of industrial growth"], ans=0,
   why="EK LEG-3.C.1.c has governments develop infrastructure and other mechanisms to respond to health crises related to systemic pollution, whereas EK LEG-3.C.1.a and EK LEG-3.C.1.b act on where production happens and on what is driven."),
 dict(q="Taking EK LEG-3.C as a whole, which summary is most accurate?",
   choices=[
     "Rapid industrialization and fossil fuel dependence force governments to relocate and regulate production, mandate cleaner vehicles, and treat the illness pollution causes; trade policy imposes a cost whichever way it moves; and world market swings can push a budget into deficit and state programmes into funding cuts",
     "Industrialization creates problems that governments have no means of addressing",
     "Trade liberalization benefits consumers and domestic industry alike",
     "Austerity measures arise only from a government's own spending decisions",
     "Environmental policy is set for governments by supranational organizations"], ans=0,
   why="EK LEG-3.C.1 supplies the three solutions, EK LEG-3.C.2 the two-sided cost of moving tariffs in either direction, and EK LEG-3.C.3 the chain from world market fluctuations through deficits and austerity to funding cuts."),
]
