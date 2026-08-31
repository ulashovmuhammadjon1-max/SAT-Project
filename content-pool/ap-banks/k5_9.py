# AP COMPARATIVE GOVERNMENT AND POLITICS 5.9 Impact of Natural Resources
# CED effective Fall 2026, Unit 5 Political and Economic Changes and Development.
# Enduring understanding LEG-5 (natural resource endowments can have positive and
# negative effects on political stability and economic development); learning
# objective LEG-5.A. Suggested skill 4.C, Source Analysis.
#
# Essential knowledge relied on:
#   LEG-5.A.1  RENTIER STATES (INCLUDING IRAN, NIGERIA, AND RUSSIA) that obtain a
#              SIZABLE PERCENTAGE OF TOTAL GOVERNMENT REVENUE FROM THE EXPORT OF OIL
#              AND GAS or FROM LEASING THE RESOURCE TO FOREIGN COUNTRIES have been
#              ABLE TO RAISE STANDARDS OF LIVING AND FUND GOVERNMENTAL PROGRAMS based
#              on their huge reserves
#   LEG-5.A.2  outcomes related to rentier state status, OFTEN CALLED THE "RESOURCE
#              CURSE" WHEN PETROLEUM IS INVOLVED, include .a LACK OF ECONOMIC
#              DIVERSIFICATION, .b CONCENTRATION OF GOVERNMENTAL RESOURCES ON THE ONE
#              PROFITABLE EXPORT INDUSTRY, .c SEVERE REVENUE FLUCTUATIONS BASED ON
#              WORLD MARKET PRICING, .d OVERVALUATION OF CURRENCY AND TRADE
#              IMBALANCES, .e INCREASING DISPARITY BETWEEN RICH AND POOR, .f A LACK OF
#              INCENTIVE TO MODERNIZE THE ECONOMY OR COOPERATE WITH INTERNATIONAL
#              JUDICIAL BODIES, .g INCREASED GOVERNMENTAL CORRUPTION, .h A LACK OF
#              GOVERNMENTAL ACCOUNTABILITY TO CITIZENS WHEN NOT RELYING ON CITIZENS
#              FOR TAXES, and .i THE ABSENCE OF DEMOCRACY
#   LEG-5.A.3  RESOURCES ARE NATIONALIZED IN CHINA, IRAN, MEXICO, NIGERIA, AND RUSSIA
#              to PROVIDE GOVERNMENT REVENUE, CONSOLIDATE GOVERNMENT CONTROL, and
#              REDUCE POLITICAL INFLUENCE OF FOREIGN GOVERNMENTS AND MULTINATIONAL
#              CORPORATIONS, all of which CAN REINFORCE POLITICAL LEGITIMACY; the
#              DEGREE OF CENTRAL GOVERNMENT CONTROL DIFFERS, as represented by
#     .a the MEXICAN government's decision to ALLOW PRIVATE INVESTMENT IN PEMEX
#     .b the POLITICAL CONTROL EXERCISED BY FOREIGN MULTINATIONAL CORPORATIONS THAT
#        UNDERWRITE NIGERIA'S OIL PRODUCTION
#     .c the HIGH DEGREE OF CENTRALIZED CONTROL over natural resource companies in
#        RUSSIA that HAS RESULTED IN WEALTH CONCENTRATION
#   LEG-5.A.4  PRIVATIZED OWNERSHIP of natural resources DECREASES GOVERNMENT CONTROL,
#              INCREASES WEALTH INEQUALITY, and results in the POTENTIAL LOSS OF
#              SOVEREIGNTY
#
# LEG-5.A.2.h IS THE SHARPEST CLAIM IN THE WHOLE UNIT and the one this module is
# built around. A government funded by selling a resource is not funded by its
# citizens, and the framework states the consequence directly: a lack of
# governmental accountability to citizens WHEN NOT RELYING ON CITIZENS FOR TAXES.
# It is a claim about the direction of dependence, not about wealth, which is why
# item 10, item 19 and the whole first table turn on the SHARE OF REVENUE that
# comes from taxes rather than on how much revenue there is.
#
# THE FRAMEWORK SAYS BOTH GOOD AND BAD, AND ITEM 18 KEYS THAT. LEG-5.A.1 credits
# rentier states with raising standards of living and funding governmental
# programs; LEG-5.A.2 then lists nine adverse outcomes. Enduring understanding
# LEG-5 says resource endowments can have POSITIVE AND NEGATIVE effects, so an
# answer that keeps only one half contradicts the framework's own heading.
#
# THE THREE INSTANCES IN LEG-5.A.3 ARE A SCALE, NOT A LIST. All five named
# countries nationalize, but the DEGREE OF CENTRAL CONTROL differs: private
# investment admitted at one end, foreign corporations exercising political
# control in the middle, high centralization with wealth concentration at the
# other. Items 14-16 and 27-29 key the positions rather than the countries.
#
# NOTHING HERE TURNS ON CURRENT EVENTS: no oil price, production figure, revenue
# share, contract or dispute of any real country is asserted. Every table figure is
# HYPOTHETICAL, labelled so, and attached to unnamed countries or years.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md.
TOPIC = ("5.9", "Impact of Natural Resources", 5)

_T_RENT = dict(
    headers=["Country (hypothetical)", "Government revenue from oil and gas exports (percent of the total)",
             "Government revenue from taxes on citizens and domestic firms (percent of the total)",
             "Index of government responsiveness to citizen complaints"],
    rows=[["Country A", "78", "14", "31"],
          ["Country B", "41", "46", "58"],
          ["Country C", "6", "81", "84"]])

_T_PRICE = dict(
    headers=["Year (hypothetical)", "World price index for the country's main export",
             "Government revenue index", "Spending on state programmes (index)"],
    rows=[["Year 1", "100", "100", "100"],
          ["Year 2", "152", "141", "128"],
          ["Year 3", "61", "72", "81"]])

_T_CONTROL = dict(
    headers=["Arrangement (hypothetical)", "How the resource sector is controlled"],
    rows=[["Arrangement 1", "The state company remains in place, but private investors have been admitted to it"],
          ["Arrangement 2", "Foreign multinational corporations underwrite production and exercise political influence"],
          ["Arrangement 3", "Resource companies are held under a high degree of centralized control, and wealth has become concentrated"]])

QUESTIONS = [
 dict(q="How does the framework define a rentier state?",
   choices=[
     "one that obtains a sizable percentage of total government revenue from exporting oil and gas or from leasing the resource to foreign countries",
     "one that obtains most of its revenue from taxes on its citizens",
     "one that has privatized its natural resource industries",
     "one that borrows from international financial organizations",
     "one that belongs to a supranational organization with sovereign powers"], ans=0,
   why="EK LEG-5.A.1 defines rentier states as those that obtain a sizable percentage of total government revenue from the export of oil and gas or from leasing the resource to foreign countries, so the defining feature is where the revenue comes from."),
 dict(q="Which course countries does the framework include among rentier states?",
   choices=[
     "Iran, Nigeria, and Russia",
     "China, Mexico, and the United Kingdom",
     "the United Kingdom, Iran, and China",
     "Mexico, Nigeria, and the United Kingdom",
     "China, Russia, and Mexico"], ans=0,
   why="EK LEG-5.A.1 names Iran, Nigeria, and Russia among rentier states, which are the three course countries whose governments draw a sizable share of revenue from oil and gas."),
 dict(q="What does the framework say rentier states have been able to do on the strength of their reserves?",
   choices=[
     "raise standards of living and fund governmental programs",
     "eliminate inequality between rich and poor",
     "diversify their economies away from a single export",
     "dispense with government revenue altogether",
     "avoid all fluctuations in revenue"], ans=0,
   why="EK LEG-5.A.1 states that rentier states have been able to raise standards of living and fund governmental programs based on their huge reserves, which is the favorable half of the framework's account."),
 dict(q="What term does the framework say the outcomes of rentier state status are often given when petroleum is involved?",
   choices=[
     "the resource curse",
     "structural adjustment",
     "import substitution",
     "economic liberalization",
     "corporatism"], ans=0,
   why="EK LEG-5.A.2 states that the political and economic outcomes related to rentier state status are often referred to as the resource curse when petroleum is involved."),
 dict(q="Which pair of outcomes does the framework list concerning the shape of a rentier state's economy?",
   choices=[
     "a lack of economic diversification, and the concentration of governmental resources on the one profitable export industry",
     "a broadening of industry across many sectors, and the retreat of the state from the economy",
     "a fall in the price of the export, and a rise in tax revenue",
     "the privatization of every state-owned company, and the removal of tariffs",
     "the expansion of the judiciary, and the strengthening of the legislature"], ans=0,
   why="EK LEG-5.A.2.a names a lack of economic diversification and EK LEG-5.A.2.b the concentration of governmental resources on developing the one profitable export industry to the exclusion of other types of industries."),
 dict(q="What does the framework say produces severe revenue fluctuations in a rentier state?",
   choices=[
     "world market pricing",
     "changes in the country's tax rates",
     "the decisions of a supranational organization",
     "the size of the working-age population",
     "the number of parties in the legislature"], ans=0,
   why="EK LEG-5.A.2.c names severe revenue fluctuations based on world market pricing among the outcomes related to rentier state status, so the instability comes from a price set outside the country."),
 dict(q="Which monetary and trade outcome does the framework associate with rentier state status?",
   choices=[
     "the overvaluation of currency and trade imbalances",
     "the undervaluation of currency and balanced trade",
     "the adoption of a common currency with neighbouring states",
     "the abolition of a national currency",
     "the elimination of all tariffs"], ans=0,
   why="EK LEG-5.A.2.d names the overvaluation of currency and trade imbalances among the outcomes related to rentier state status."),
 dict(q="What does the framework say happens to the distance between rich and poor in a rentier state?",
   choices=[
     "the disparity between rich and poor increases",
     "the disparity between rich and poor disappears",
     "incomes converge across regions",
     "wealth is distributed equally by the state",
     "the framework makes no claim about it"], ans=0,
   why="EK LEG-5.A.2.e names the increasing disparity between rich and poor among the outcomes related to rentier state status."),
 dict(q="Which two things does the framework say a rentier state lacks the incentive to do?",
   choices=[
     "modernize the economy, and cooperate with international judicial bodies",
     "collect any revenue at all, and maintain armed forces",
     "hold elections, and appoint a cabinet",
     "join international financial organizations, and sign treaties",
     "export its resource, and lease it to foreign countries"], ans=0,
   why="EK LEG-5.A.2.f names a lack of incentive to modernize the economy or cooperate with international judicial bodies among the outcomes related to rentier state status."),
 dict(q="On the framework's account, why does a rentier government tend to be less accountable to its citizens?",
   choices=[
     "because it is not relying on citizens for taxes",
     "because its citizens are wealthier than in other states",
     "because international lenders forbid it to consult them",
     "because its constitution contains no provision for elections",
     "because its population is too widely dispersed to consult"], ans=0,
   why="EK LEG-5.A.2.h names a lack of governmental accountability to citizens when not relying on citizens for taxes, so the framework's claim is about the direction of dependence rather than about how rich a country is."),
 dict(q="Which two further outcomes does the framework list for rentier states?",
   choices=[
     "increased governmental corruption, and the absence of democracy",
     "reduced governmental corruption, and the consolidation of democracy",
     "the strengthening of the judiciary, and the widening of the franchise",
     "the growth of interest groups, and the weakening of parties",
     "an end to trade imbalances, and a stable currency"], ans=0,
   why="EK LEG-5.A.2.g names increased governmental corruption and EK LEG-5.A.2.i the absence of democracy among the outcomes related to rentier state status."),
 dict(q="In which course countries does the framework say resources are nationalized?",
   choices=[
     "China, Iran, Mexico, Nigeria, and Russia",
     "all six course countries",
     "Iran, Nigeria, and Russia only",
     "the United Kingdom, Mexico, and China",
     "none of the course countries"], ans=0,
   why="EK LEG-5.A.3 states that resources are nationalized in China, Iran, Mexico, Nigeria, and Russia, which is five of the six course countries, and EK IEF-3.B.2 places the sixth at the end of the spectrum allowing the most private control."),
 dict(q="For what purposes does the framework say resources are nationalized?",
   choices=[
     "to provide government revenue, consolidate government control, and reduce the political influence of foreign governments and multinational corporations",
     "to satisfy the conditions attached to external financial assistance",
     "to comply with the rules of a supranational organization",
     "to increase the number of private firms in the sector",
     "to reduce a government's revenue from exports"], ans=0,
   why="EK LEG-5.A.3 names providing government revenue, consolidating government control, and reducing the political influence of foreign governments and multinational corporations as the purposes, adding that all of these can reinforce political legitimacy."),
 dict(q="Which decision does the framework give as an instance of a lower degree of central control over a nationalized resource?",
   choices=[
     "the Mexican government's decision to allow private investment in its national oil company",
     "the imposition of a high degree of centralized control over resource companies",
     "the exclusion of all foreign firms from oil production",
     "the transfer of the resource sector to a supranational organization",
     "the abolition of the national oil company"], ans=0,
   why="EK LEG-5.A.3.a gives the Mexican government's decision to allow private investment in Pemex as one of the ways the degree of central government control differs among the states that nationalize resources."),
 dict(q="What does the framework record about the foreign multinational corporations that underwrite Nigeria's oil production?",
   choices=[
     "that they exercise political control",
     "that they hold no influence over policy",
     "that they own the country's resource reserves outright",
     "that they are barred from the sector",
     "that they are owned by the national government"], ans=0,
   why="EK LEG-5.A.3.b names the political control exercised by foreign multinational corporations that underwrite Nigeria's oil production as one of the ways the degree of central government control differs."),
 dict(q="What result does the framework attribute to the high degree of centralized control over natural resource companies in Russia?",
   choices=[
     "wealth concentration",
     "the equalization of incomes",
     "the withdrawal of the state from the sector",
     "the transfer of ownership to foreign firms",
     "the elimination of government revenue from the sector"], ans=0,
   why="EK LEG-5.A.3.c states that the high degree of centralized control over natural resource companies in Russia has resulted in wealth concentration."),
 dict(q="What three effects does the framework attribute to privatized ownership of natural resources?",
   choices=[
     "decreased government control, increased wealth inequality, and the potential loss of sovereignty",
     "increased government control, reduced inequality, and strengthened sovereignty",
     "higher tax revenue, lower corruption, and greater economic diversification",
     "the elimination of trade imbalances and the stabilization of the currency",
     "the transfer of resource revenue to an international organization"], ans=0,
   why="EK LEG-5.A.4 states that privatized ownership of natural resources decreases government control, increases wealth inequality, and results in the potential loss of sovereignty."),
 dict(q="A student says the framework treats a large resource endowment as simply an advantage. What is wrong with that reading?",
   choices=[
     "the framework credits rentier states with raising living standards and funding programmes and then lists nine adverse political and economic outcomes, and its enduring understanding says such endowments have positive and negative effects",
     "the framework says resource endowments have no effect on political stability",
     "the framework lists only adverse outcomes and no benefits",
     "the framework treats resource endowments as a matter for international organizations",
     "the framework says only privatized resources have any effect"], ans=0,
   why="EK LEG-5.A.1 states the benefits and EK LEG-5.A.2 lists the outcomes often called the resource curse, while enduring understanding LEG-5 states that natural resource endowments can have positive and negative effects on political stability and economic development."),
 dict(q="A writer argues that a government which never has to ask its people for money has little reason to answer to them. Which framework claim does this argument rest on?",
   choices=[
     "that rentier states show a lack of governmental accountability to citizens when not relying on citizens for taxes",
     "that rentier states suffer severe revenue fluctuations based on world market pricing",
     "that privatized ownership decreases government control",
     "that nationalization can reinforce political legitimacy",
     "that resource wealth raises standards of living"], ans=0,
   why="EK LEG-5.A.2.h names a lack of governmental accountability to citizens when not relying on citizens for taxes, which is exactly the link between the source of revenue and the obligation to answer that the argument makes."),
 dict(q="Another writer warns that selling long-term rights over a country's minerals to foreign firms may leave decisions about its territory in other hands. Which framework claim does this warning rest on?",
   choices=[
     "that privatized ownership of natural resources decreases government control and results in the potential loss of sovereignty",
     "that nationalization provides government revenue and consolidates government control",
     "that rentier states lack economic diversification",
     "that world market pricing causes severe revenue fluctuations",
     "that resource wealth raises standards of living"], ans=0,
   why="EK LEG-5.A.4 states that privatized ownership of natural resources decreases government control, increases wealth inequality, and results in the potential loss of sovereignty."),
 dict(q="The table reports hypothetical revenue sources and a responsiveness measure for three countries. Which conclusion does it support?",
   table=_T_RENT,
   choices=[
     "The larger the share of revenue drawn from oil and gas, the smaller the share drawn from taxes on citizens and the lower the recorded responsiveness",
     "The larger the share of revenue drawn from oil and gas, the higher the recorded responsiveness",
     "The share of revenue drawn from taxes bears no relationship to responsiveness",
     "All three countries record the same responsiveness",
     "No country in the table draws revenue from taxes on citizens"], ans=0,
   why="EK LEG-5.A.2.h names a lack of governmental accountability to citizens when not relying on citizens for taxes, and reading the rows in order of their oil and gas share shows the tax share and the responsiveness measure both falling as it rises."),
 dict(q="According to the same table, the difference between the highest and lowest recorded responsiveness is",
   table=_T_RENT,
   choices=[
     "53 points",
     "26 points",
     "27 points",
     "84 points",
     "31 points"], ans=0,
   why="Subtracting the smallest figure in that column from the largest gives the difference. The alternatives are the other two gaps in the same column and its two extreme values read as though they were differences."),
 dict(q="Using the same table, the difference between the highest and lowest shares of revenue drawn from oil and gas is",
   table=_T_RENT,
   choices=[
     "72 percentage points",
     "37 percentage points",
     "35 percentage points",
     "78 percentage points",
     "6 percentage points"], ans=0,
   why="Subtracting the smallest figure in that column from the largest gives the difference. The alternatives are the other two gaps in the same column and its two extreme values read as though they were differences."),
 dict(q="The table follows one hypothetical resource exporter over three years. Which conclusion does it support?",
   table=_T_PRICE,
   choices=[
     "Government revenue and programme spending rose when the world price rose and fell when it fell, swinging far below the starting level in the last year",
     "Government revenue was steady while the world price swung",
     "Programme spending rose in every year regardless of the world price",
     "The world price fell in every year of the period",
     "The three columns moved in opposite directions to one another"], ans=0,
   why="EK LEG-5.A.2.c names severe revenue fluctuations based on world market pricing among the outcomes of rentier state status, and the table's three columns rise together and then fall together with the price."),
 dict(q="According to the same table of years, the range of the world price index across the period is",
   table=_T_PRICE,
   choices=[
     "91 points",
     "52 points",
     "39 points",
     "152 points",
     "69 points"], ans=0,
   why="Subtracting the smallest world price figure from the largest gives the range. The alternatives are the two gaps against the starting year, the largest single figure read as a range, and the range of the revenue column."),
 dict(q="Using the same table of years, the range of the government revenue index across the period is",
   table=_T_PRICE,
   choices=[
     "69 points",
     "41 points",
     "28 points",
     "141 points",
     "91 points"], ans=0,
   why="Subtracting the smallest revenue figure from the largest gives the range. The alternatives are the two gaps against the starting year, the largest single figure read as a range, and the range of the world price column."),
 dict(q="The table describes three hypothetical arrangements for a nationalized resource sector. Which one matches EK LEG-5.A.3.a?",
   table=_T_CONTROL,
   choices=[
     "the arrangement in which the state company remains but private investors have been admitted to it",
     "the arrangement in which foreign corporations underwrite production and exercise political influence",
     "the arrangement in which resource companies are held under a high degree of centralized control",
     "none of the three, since that statement describes no arrangement",
     "all three, since each involves a state resource sector"], ans=0,
   why="EK LEG-5.A.3.a gives the Mexican government's decision to allow private investment in Pemex as an instance of how the degree of central government control differs, and only one arrangement admits private investors to a state company."),
 dict(q="Using the same table of arrangements, which one matches EK LEG-5.A.3.b?",
   table=_T_CONTROL,
   choices=[
     "the arrangement in which foreign multinational corporations underwrite production and exercise political influence",
     "the arrangement in which private investors have been admitted to the state company",
     "the arrangement in which resource companies are held under a high degree of centralized control",
     "none of the three, since that statement describes no arrangement",
     "all three, since each involves foreign firms"], ans=0,
   why="EK LEG-5.A.3.b names the political control exercised by foreign multinational corporations that underwrite Nigeria's oil production, and only one arrangement in the table gives foreign corporations both roles."),
 dict(q="Using the same table of arrangements, which one leaves the central government with the greatest control, and what does the framework record as accompanying it?",
   table=_T_CONTROL,
   choices=[
     "the arrangement holding resource companies under a high degree of centralized control, which the framework associates with wealth concentration",
     "the arrangement admitting private investors to the state company, which the framework associates with wealth concentration",
     "the arrangement in which foreign corporations underwrite production, which the framework associates with an equal distribution of wealth",
     "none of the three, since the framework records no difference in the degree of control",
     "all three equally, since each keeps the resource nationalized"], ans=0,
   why="EK LEG-5.A.3.c states that the high degree of centralized control over natural resource companies in Russia has resulted in wealth concentration, and EK LEG-5.A.3 introduces the three instances as showing that the degree of central government control differs."),
 dict(q="Taking EK LEG-5.A as a whole, which summary is most accurate?",
   choices=[
     "Resource revenue lets a government raise living standards and fund programmes while exposing it to price swings, narrowing its economy, widening inequality, and loosening its need to answer to taxpayers; nationalization can shore up its legitimacy and its control, in degrees that differ from one state to another, and privatization trades that control away",
     "Resource wealth is an unqualified advantage for the states that hold it",
     "Resource wealth is an unqualified disadvantage for the states that hold it",
     "Every state that nationalizes its resources exercises the same degree of control over them",
     "Privatized ownership of natural resources leaves a government's control unchanged"], ans=0,
   why="EK LEG-5.A.1 supplies the benefits, EK LEG-5.A.2 the nine adverse outcomes including the accountability claim, EK LEG-5.A.3 the purposes of nationalization and the differing degrees of control, and EK LEG-5.A.4 the effects of privatized ownership."),
]
