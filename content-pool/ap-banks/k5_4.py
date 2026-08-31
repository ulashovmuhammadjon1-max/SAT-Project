# AP COMPARATIVE GOVERNMENT AND POLITICS 5.4 Policies and Economic Liberalization
# CED effective Fall 2026, Unit 5 Political and Economic Changes and Development.
# Enduring understanding IEF-3; learning objectives IEF-3.D (describe economic and
# political liberalization policies) and IEF-3.E (explain the adoption of and
# consequences associated with economic liberalization policies). Suggested skill
# 3.D, Data Analysis (explain what the data implies or illustrates).
#
# Essential knowledge relied on:
#   IEF-3.D.1  ECONOMIC LIBERALIZATION occurs when a STATE REDUCES ITS ECONOMIC ROLE
#              and EMBRACES FREE MARKET MECHANISMS such as ELIMINATING SUBSIDIES AND
#              TARIFFS, PRIVATIZING GOVERNMENT-OWNED INDUSTRIES, and OPENING THE
#              ECONOMY TO FOREIGN DIRECT INVESTMENT
#   IEF-3.E.1  political-economic systems in the course countries can be COMPARED BY
#              MEASURING levels of ECONOMIC DEVELOPMENT, ECONOMIC GROWTH, HUMAN
#              DEVELOPMENT, WEALTH, and INEQUALITY
#   IEF-3.E.2  course countries OF ALL REGIME TYPES adopt economic liberalization
#              policies with the goals of remedying UNDESIRABLE DOMESTIC
#              CIRCUMSTANCES, such as RISING UNEMPLOYMENT and REDUCED PRODUCTIVITY,
#              and UNDESIRABLE EXTERNAL SITUATIONS, such as TRADE DEFICITS WITH OTHER
#              STATES and DECREASING DEMAND FOR RAW MATERIALS like PETROLEUM, NATURAL
#              GAS, and RARE-EARTH METAL
#   IEF-3.E.3  NEOLIBERAL ECONOMIC POLICIES (the REMOVAL OF BARRIERS AND RESTRICTIONS
#              ON WHAT INTERNAL AND EXTERNAL ECONOMIC ACTORS CAN DO) have had MIXED
#              EFFECTS, including REDUCTION IN INFLATION and INCREASES IN NATIONAL
#              INCOME, as well as GROWING INEQUALITY IN WEALTH DISTRIBUTION,
#              PERSISTENT POLITICAL CORRUPTION, and the EXACERBATION OF EXISTING
#              SOCIAL TENSIONS as governments attempt to BALANCE ECONOMIC FREEDOM
#              WITH POLICIES THAT PROMOTE ECONOMIC AND POLITICAL EQUALITY
#   IEF-3.E.4  ECONOMIC PROSPERITY TIED TO LIBERALIZATION POLICIES HAS AFFECTED THE
#              POWER OF RULING POLITICAL PARTIES among course country political
#              systems
#   IEF-3.E.5  while often STIMULATING GROWTH, economic liberalization has
#              CONTRIBUTED TO ENVIRONMENTAL POLLUTION, URBAN SPRAWL, and UNEVEN
#              ECONOMIC DEVELOPMENT, as a result of:
#     .a INCREASED CONSUMPTION AND USE OF AUTOMOBILES AND OTHER ENGINES USING FOSSIL
#        FUELS
#     .b POOR INFRASTRUCTURE AND LACK OF GOVERNMENT REGULATION
#     .c REGIONAL MIGRATION PATTERNS (including EAST/WEST IN CHINA; NORTH/SOUTH IN
#        MEXICO; RURAL/URBAN IN BOTH)
#
# "MIXED EFFECTS" IS THE LOAD-BEARING PHRASE. IEF-3.E.3 puts falling inflation and
# rising national income in the SAME SENTENCE as growing inequality, persistent
# political corruption and worsened social tensions. A student who has learned
# liberalization as either a success story or a failure story cannot answer an
# item that lists both. Items 9, 10, 17 and the second table all require holding
# the two halves together, and the table's check requires two indicators to
# improve AND two to worsen -- a table moving one way would make the key false.
#
# IEF-3.E.2's OTHER LOAD-BEARING PHRASE IS "OF ALL REGIME TYPES". The framework
# does not treat liberalization as something democracies do; it says course
# countries of every regime type adopt these policies, and it splits the reasons
# into domestic circumstances and external situations. Items 4, 5, 6, 19 and 20
# key that split and that universality.
#
# WHAT IS DELIBERATELY NOT ASSERTED: no growth rate, income figure, inflation
# rate, unemployment rate or inequality measure is attributed to any real country
# anywhere in this module. The only country-specific claim made is the one the
# framework itself states in IEF-3.E.5.c -- east/west migration in China and
# north/south migration in Mexico, with rural/urban movement in both -- and it is
# a structural pattern rather than a figure. Every table is HYPOTHETICAL and
# labelled so.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md.
TOPIC = ("5.4", "Policies and Economic Liberalization", 5)

_T_MEASURE = dict(
    headers=["Country (hypothetical)", "National income per person (index)",
             "Annual economic growth (percent)", "Human development index",
             "Share of income held by the richest tenth (percent)"],
    rows=[["Country A", "100", "1.4", "0.92", "24"],
          ["Country B", "46", "6.8", "0.74", "41"],
          ["Country C", "19", "3.1", "0.55", "33"]])

_T_MIXED = dict(
    headers=["Indicator (hypothetical)", "Before the reforms", "Ten years after the reforms"],
    rows=[["Annual inflation (percent)", "28", "6"],
          ["National income index", "100", "149"],
          ["Share of income held by the richest tenth (percent)", "31", "44"],
          ["Recorded cases of official corruption", "210", "265"]])

_T_MIGRATION = dict(
    headers=["Direction of movement", "Net movement of people over a decade, in thousands (hypothetical)"],
    rows=[["Interior regions to coastal regions", "4200"],
          ["Southern regions to northern regions", "1800"],
          ["Rural areas to urban areas", "9600"],
          ["Urban areas to rural areas", "700"]])

QUESTIONS = [
 dict(q="How does the framework define economic liberalization?",
   choices=[
     "a state reducing its economic role and embracing free market mechanisms",
     "a state taking ownership of its largest industries",
     "a state raising tariffs to protect domestic producers",
     "a state widening the franchise and legalizing opposition parties",
     "a state joining a supranational organization with sovereign powers"], ans=0,
   why="EK IEF-3.D.1 states that economic liberalization occurs when a state reduces its economic role and embraces free market mechanisms, so the definition is about the state stepping back rather than about a political change."),
 dict(q="Which measures does the framework name as examples of the free market mechanisms economic liberalization embraces?",
   choices=[
     "eliminating subsidies and tariffs, privatizing government-owned industries, and opening the economy to foreign direct investment",
     "nationalizing energy firms, raising tariffs, and capping foreign ownership",
     "expanding the civil service, increasing subsidies, and fixing prices",
     "extending term limits, appointing governors, and raising thresholds",
     "creating ethnic quotas, gender quotas, and regional assemblies"], ans=0,
   why="EK IEF-3.D.1 names eliminating subsidies and tariffs, privatizing government-owned industries, and opening the economy to foreign direct investment as the free market mechanisms a liberalizing state embraces."),
 dict(q="Which set of measures does the framework give for comparing the political-economic systems of the course countries?",
   choices=[
     "levels of economic development, economic growth, human development, wealth, and inequality",
     "population, land area, coastline, and climate",
     "the number of parties, the length of terms, and the size of the legislature",
     "tariff rates, exchange rates, and interest rates alone",
     "military spending, treaty membership, and diplomatic recognition"], ans=0,
   why="EK IEF-3.E.1 states that political-economic systems in the course countries can be compared by measuring levels of economic development, economic growth, human development, wealth, and inequality."),
 dict(q="Which course countries does the framework say adopt economic liberalization policies?",
   choices=[
     "course countries of all regime types",
     "only the democracies among them",
     "only the authoritarian regimes among them",
     "only those that are members of supranational organizations",
     "only those without significant natural resources"], ans=0,
   why="EK IEF-3.E.2 states that course countries of all regime types adopt economic liberalization policies, so the framework treats liberalization as a response available to any regime rather than as a mark of one."),
 dict(q="Which undesirable domestic circumstances does the framework name as goals for economic liberalization to remedy?",
   choices=[
     "rising unemployment and reduced productivity",
     "falling birth rates and rising emigration",
     "a shortage of political parties and low turnout",
     "an independent judiciary and a free press",
     "an aging population and rising health care costs"], ans=0,
   why="EK IEF-3.E.2 names rising unemployment and reduced productivity as the undesirable domestic circumstances liberalization policies aim to remedy."),
 dict(q="Which undesirable external situations does the framework name as goals for economic liberalization to remedy?",
   choices=[
     "trade deficits with other states and decreasing demand for raw materials",
     "the loss of diplomatic recognition and expulsion from treaties",
     "rising unemployment and reduced productivity at home",
     "an increase in foreign direct investment",
     "the growth of a domestic middle class"], ans=0,
   why="EK IEF-3.E.2 names trade deficits with other states and decreasing demand for raw materials as the undesirable external situations, and distinguishes them from the domestic circumstances named in the same statement."),
 dict(q="Which raw materials does the framework name when it refers to decreasing demand?",
   choices=[
     "petroleum, natural gas, and rare-earth metal",
     "wheat, maize, and rice",
     "timber, rubber, and cotton",
     "gold, silver, and diamonds",
     "fish, coffee, and cocoa"], ans=0,
   why="EK IEF-3.E.2 names petroleum, natural gas, and rare-earth metal as the raw materials whose decreasing demand is an undesirable external situation."),
 dict(q="What does the framework say neoliberal economic policies refer to?",
   choices=[
     "the removal of barriers and restrictions on what internal and external economic actors can do",
     "the transfer of economic policy to an international organization",
     "the nationalization of industries deemed strategic",
     "the negotiation of wages by state-sanctioned peak associations",
     "the setting of prices by a central planning ministry"], ans=0,
   why="EK IEF-3.E.3 defines neoliberal economic policies as the removal of barriers and restrictions on what internal and external economic actors can do, so the definition covers domestic and foreign actors alike."),
 dict(q="Which effects does the framework list on the favorable side of the mixed record of neoliberal economic policies?",
   choices=[
     "reduction in inflation and increases in national income",
     "reduction in inequality and the elimination of corruption",
     "an end to social tensions and a rise in political participation",
     "a fall in unemployment and an end to trade deficits",
     "cleaner air and slower urban growth"], ans=0,
   why="EK IEF-3.E.3 names reduction in inflation and increases in national income among the effects of neoliberal economic policies, and lists them alongside the unfavorable ones in the same sentence."),
 dict(q="Which effects does the framework list on the unfavorable side of that same record?",
   choices=[
     "growing inequality in wealth distribution, persistent political corruption, and the exacerbation of existing social tensions",
     "rising inflation, falling national income, and shrinking trade",
     "the disappearance of private industry and the end of foreign investment",
     "the loss of diplomatic recognition and expulsion from treaties",
     "falling productivity and rising unemployment in every case"], ans=0,
   why="EK IEF-3.E.3 names growing inequality in wealth distribution, persistent political corruption, and the exacerbation of existing social tensions among the effects of neoliberal economic policies."),
 dict(q="What balance does the framework say governments attempt as those tensions worsen?",
   choices=[
     "balancing economic freedom with policies that promote economic and political equality",
     "balancing the budget against the level of foreign borrowing",
     "balancing exports against imports in every sector",
     "balancing the powers of the legislature against those of the executive",
     "balancing regional against national representation in the legislature"], ans=0,
   why="EK IEF-3.E.3 states that existing social tensions are exacerbated as governments attempt to balance economic freedom with policies that promote economic and political equality, which is the trade-off the statement identifies."),
 dict(q="What does the framework say economic prosperity tied to liberalization policies has affected?",
   choices=[
     "the power of ruling political parties",
     "the boundaries between states",
     "the number of chambers in legislatures",
     "the tenure of judges",
     "the recognition of states by other states"], ans=0,
   why="EK IEF-3.E.4 states that economic prosperity tied to liberalization policies has affected the power of ruling political parties among course country political systems, which links an economic outcome to a party's hold on office."),
 dict(q="Alongside stimulating growth, what does the framework say economic liberalization has contributed to?",
   choices=[
     "environmental pollution, urban sprawl, and uneven economic development",
     "the abolition of private property and the end of trade",
     "the disappearance of regional differences within countries",
     "a fall in the use of automobiles and other fossil fuel engines",
     "the equalization of incomes across regions"], ans=0,
   why="EK IEF-3.E.5 states that while often stimulating growth, economic liberalization has contributed to environmental pollution, urban sprawl, and uneven economic development in course countries."),
 dict(q="Which of the causes the framework gives for those consequences concerns what people consume and use?",
   choices=[
     "increased consumption and use of automobiles and other engines using fossil fuels",
     "poor infrastructure and lack of government regulation",
     "regional migration patterns within countries",
     "the elimination of subsidies and tariffs",
     "the privatization of government-owned industries"], ans=0,
   why="EK IEF-3.E.5.a names increased consumption and use of automobiles and other engines using fossil fuels, which is the one of the three causes stated in terms of what people use rather than of policy or movement."),
 dict(q="Which of those causes concerns what governments have failed to build or to do?",
   choices=[
     "poor infrastructure and lack of government regulation",
     "increased use of automobiles and other fossil fuel engines",
     "regional migration patterns within countries",
     "growing inequality in wealth distribution",
     "decreasing demand for raw materials"], ans=0,
   why="EK IEF-3.E.5.b names poor infrastructure and lack of government regulation, which is the one of the three causes stated as a shortfall on the government's own side."),
 dict(q="Which regional migration patterns does the framework name in connection with uneven economic development?",
   choices=[
     "east and west in China, north and south in Mexico, and rural to urban in both",
     "north and south in China and east and west in Mexico",
     "coastal to interior movement in every course country",
     "movement between the six course countries",
     "urban to rural movement in China and Mexico"], ans=0,
   why="EK IEF-3.E.5.c names regional migration patterns including east and west in China, north and south in Mexico, and rural to urban movement in both, so two country-specific axes are joined by one common to both."),
 dict(q="Why does the framework describe the effects of neoliberal economic policies as mixed rather than as good or bad?",
   choices=[
     "because it records improvements in inflation and national income alongside worsening inequality, persistent corruption, and sharper social tensions in the same statement",
     "because different countries have adopted different policies",
     "because the effects have not yet been measured",
     "because economists disagree about how to define them",
     "because the effects appear only after a long delay"], ans=0,
   why="EK IEF-3.E.3 lists reduction in inflation and increases in national income together with growing inequality in wealth distribution, persistent political corruption, and the exacerbation of social tensions, so the mixture is in the record itself."),
 dict(q="A government abolishes fuel subsidies, sells its state-owned airline, and lifts the ceiling on foreign ownership in several industries. Which framework concept does this best illustrate?",
   choices=[
     "economic liberalization, since the state is reducing its economic role and embracing free market mechanisms",
     "corporatism, since the state is dealing with economic sectors",
     "import substitution, since domestic industry is affected",
     "re-nationalization, since ownership is changing hands",
     "austerity, since the budget is involved"], ans=0,
   why="EK IEF-3.D.1 names eliminating subsidies, privatizing government-owned industries, and opening the economy to foreign direct investment as the mechanisms of economic liberalization, and the scenario contains one of each."),
 dict(q="Ministers explain a package of liberalizing measures by pointing to a persistent shortfall in what the country sells abroad against what it buys. Which of the framework's goals does this match?",
   choices=[
     "remedying an undesirable external situation, namely a trade deficit with other states",
     "remedying an undesirable domestic circumstance, namely rising unemployment",
     "remedying an undesirable domestic circumstance, namely reduced productivity",
     "balancing economic freedom against policies promoting equality",
     "responding to a decline in the power of a ruling political party"], ans=0,
   why="EK IEF-3.E.2 names trade deficits with other states among the undesirable external situations liberalization policies aim to remedy, and distinguishes them from the domestic circumstances listed in the same statement."),
 dict(q="An authoritarian regime and a democracy in the same decade both cut tariffs, sell state firms, and court foreign investors. Which framework claim does this best support?",
   choices=[
     "that course countries of all regime types adopt economic liberalization policies",
     "that liberalization occurs only where a legislature is independent",
     "that liberalization requires membership in a supranational organization",
     "that liberalization is always imposed by foreign governments",
     "that liberalization is confined to states without natural resources"], ans=0,
   why="EK IEF-3.E.2 states that course countries of all regime types adopt economic liberalization policies with the goals of remedying undesirable domestic circumstances and undesirable external situations, so regime type is not what decides whether the policies are adopted."),
 dict(q="The table reports hypothetical figures on the measures the framework uses to compare political-economic systems. Which country combines the highest human development with the slowest growth?",
   table=_T_MEASURE,
   choices=[
     "Country A, with a human development index of 0.92 and annual growth of 1.4 percent",
     "Country B, with a human development index of 0.74 and annual growth of 6.8 percent",
     "Country C, with a human development index of 0.55 and annual growth of 3.1 percent",
     "None of them, since human development and growth cannot be compared",
     "All three equally, since each reports both figures"], ans=0,
   why="EK IEF-3.E.1 names economic growth and human development as two separate measures for comparing political-economic systems, so a country can rank high on one and low on the other, which is what one row of the table shows."),
 dict(q="Using the same table, which country combines the fastest growth with the greatest concentration of income at the top?",
   table=_T_MEASURE,
   choices=[
     "Country B, growing at 6.8 percent a year with the richest tenth holding 41 percent of income",
     "Country A, growing at 1.4 percent a year",
     "Country C, where the richest tenth holds 33 percent of income",
     "None of them, since growth and inequality never occur together",
     "All three, since each records some inequality"], ans=0,
   why="EK IEF-3.E.1 names economic growth and inequality among the measures for comparing systems and EK IEF-3.E.3 records growing inequality in wealth distribution alongside increases in national income, so the two can rise together, as one row of the table shows."),
 dict(q="According to the same table, the difference between the largest and smallest shares of income held by the richest tenth is",
   table=_T_MEASURE,
   choices=[
     "17 percentage points",
     "8 percentage points",
     "9 percentage points",
     "41 percentage points",
     "24 percentage points"], ans=0,
   why="Subtracting the smallest figure in that column from the largest gives the difference. The alternatives are the other gaps in the same column and its two extreme values read as though they were differences."),
 dict(q="The table compares four hypothetical indicators before and after a package of liberalizing reforms. Which conclusion does it support?",
   table=_T_MIXED,
   choices=[
     "Inflation fell and national income rose, while income concentration at the top and recorded corruption both increased",
     "Every indicator improved after the reforms",
     "Every indicator worsened after the reforms",
     "Inflation rose while national income fell",
     "None of the indicators changed after the reforms"], ans=0,
   why="EK IEF-3.E.3 states that neoliberal economic policies have had mixed effects, including reduction in inflation and increases in national income as well as growing inequality in wealth distribution and persistent political corruption, and the table shows two indicators moving each way."),
 dict(q="According to the same table of indicators, the fall in annual inflation is",
   table=_T_MIXED,
   choices=[
     "22 percentage points",
     "6 percentage points",
     "28 percentage points",
     "13 percentage points",
     "49 percentage points"], ans=0,
   why="Subtracting the later inflation figure from the earlier one gives the fall. The alternatives are the two inflation figures themselves and the changes recorded in the other rows."),
 dict(q="Using the same table of indicators, the rise in the share of income held by the richest tenth is",
   table=_T_MIXED,
   choices=[
     "13 percentage points",
     "22 percentage points",
     "44 percentage points",
     "31 percentage points",
     "55 percentage points"], ans=0,
   why="Subtracting the earlier share from the later one gives the rise. The alternatives are the change in the inflation row, the two shares themselves, and the change recorded in the corruption row."),
 dict(q="The table reports hypothetical net movements of people within one country over a decade. Which movement is the largest, and which framework claim does it bear on?",
   table=_T_MIGRATION,
   choices=[
     "movement from rural areas to urban areas, which the framework names among the regional migration patterns behind uneven economic development",
     "movement from urban areas to rural areas, which the framework names as the dominant pattern",
     "movement from southern regions to northern regions, which the framework says exceeds all others",
     "movement from interior regions to coastal regions, which the framework says is the only pattern that matters",
     "none of them, since the framework names no migration patterns"], ans=0,
   why="EK IEF-3.E.5.c names regional migration patterns including rural to urban movement among the causes of environmental pollution, urban sprawl, and uneven economic development, and the table's largest flow is that one."),
 dict(q="According to the same table of movements, the total net movement recorded across all four directions is",
   table=_T_MIGRATION,
   choices=[
     "16300 thousand",
     "15600 thousand",
     "13800 thousand",
     "9600 thousand",
     "6700 thousand"], ans=0,
   why="Adding the column across the four rows gives the total. The alternatives are the total with the smallest row omitted, the two largest rows added, the largest single row, and the total with the largest row omitted."),
 dict(q="Using the same table of movements, the net gain of the urban areas once movement in both directions is taken into account is",
   table=_T_MIGRATION,
   choices=[
     "8900 thousand",
     "10300 thousand",
     "9600 thousand",
     "2400 thousand",
     "700 thousand"], ans=0,
   why="Subtracting the movement out of the urban areas from the movement into them gives the net gain. The alternatives are the two flows added instead of subtracted, each flow on its own, and the gap between two unrelated rows."),
 dict(q="Taking EK IEF-3.D and EK IEF-3.E together, which summary is most accurate?",
   choices=[
     "Liberalization means the state stepping back through subsidy and tariff cuts, privatization, and openness to foreign investment; countries of every regime type adopt it for domestic and external reasons; and its record is mixed, joining lower inflation and higher income to greater inequality, corruption, pollution, sprawl, and uneven regional development",
     "Liberalization means the state expanding its ownership of industry, and only democracies attempt it",
     "Liberalization has had uniformly favorable effects across the course countries",
     "Liberalization has had uniformly unfavorable effects across the course countries",
     "Liberalization affects economic conditions but has no bearing on political power"], ans=0,
   why="EK IEF-3.D.1 supplies the definition and its three mechanisms, EK IEF-3.E.2 the universality across regime types and the split between domestic and external goals, EK IEF-3.E.3 the mixed effects, EK IEF-3.E.4 the bearing on ruling parties' power, and EK IEF-3.E.5 the pollution, sprawl and uneven development."),
]
