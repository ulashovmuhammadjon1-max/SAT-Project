# AP HUMAN GEOGRAPHY 7.6 Trade and the World Economy -- 30 questions
# CED Course Framework V.1, Unit 7. Enduring understanding PSO-7, "Economic and
# social development happen at different times and rates in different places."
# Learning objective PSO-7.A, "Explain causes and geographic consequences of
# recent economic changes such as the increase in international trade,
# deindustrialization, and growing interdependence in the world economy."
# Suggested skill 5.B, "Explain spatial relationships across various geographic
# scales using geographic concepts, processes, models, or theories."
#
# Essential knowledge -- FOUR statements. The CED splits learning objective
# PSO-7.A across two topics: 7.6 carries PSO-7.A.1 to PSO-7.A.4 and 7.7 carries
# PSO-7.A.5 to PSO-7.A.7. This module keeps strictly to the first four, and
# g7_7.py keeps strictly to the last three, so the two do not overlap:
#   PSO-7.A.1  Complementarity and comparative advantage establish the basis
#              for trade.
#   PSO-7.A.2  Neoliberal policies, including free trade agreements, have
#              created new organizations, spatial connections, and trade
#              relationships, such as the EU, World Trade Organization (WTO),
#              Mercosur, and OPEC, that foster greater globalization.
#   PSO-7.A.3  Government initiatives at all scales may affect economic
#              development, including tariffs.
#   PSO-7.A.4  Global financial crises (e.g., debt crises), international
#              lending agencies (e.g., the International Monetary Fund), and
#              strategies of development (e.g., microlending) demonstrate how
#              different economies have become more closely connected, even
#              interdependent.
#
# TERMS THE CED NAMES AND DOES NOT DEFINE, supplied here in the discipline's
# standard sense, the same way g7_2 supplied least cost theory and g7_5 supplied
# Rostow's stages. Every one of these is flagged in its item's `why` as an
# explanation of a term the CED names, never as a quotation:
#   complementarity        one place holds a surplus of something another place
#                          demands, so a flow between them is possible
#   comparative advantage  a place gives up less of other output to produce a
#                          given good than its partner does, so both gain from
#                          specializing even when one is better at everything
#   neoliberal policies    policies reducing government restriction on markets
#                          and cross-border trade -- lowering barriers,
#                          deregulating, privatizing
#   free trade agreement   a treaty under which the signatories lower or remove
#                          the barriers they apply to one another's goods
#   tariff                 a tax a government levies on imported goods
#   debt crisis            a state of affairs in which a borrower cannot meet
#                          obligations already incurred
#
# COMPLEMENTARITY AND COMPARATIVE ADVANTAGE ARE TWO THINGS, NOT ONE. This is
# the distinction the topic most rewards and the one students most often lose.
# Complementarity is a fact about what two places HAVE AND WANT; comparative
# advantage is a fact about the RELATIVE COST of producing something. A pair of
# places can satisfy either without the other. Items 2, 3, 5, 6 and 7 keep them
# apart and item 27's table is built so that one region is better at making both
# goods, because that is the only arrangement in which comparative advantage
# says something absolute advantage does not.
#
# WHAT MAY BE SAID ABOUT THE FOUR NAMED ORGANIZATIONS. The CED names the EU, the
# World Trade Organization, Mercosur and OPEC and says nothing else about any of
# them. This module therefore asserts nothing about what any of them does. Item
# 9 asks which four the framework names and item 10 asks what the framework says
# they do -- foster greater globalization -- and no item anywhere claims a
# membership, a rule, a founding date or a policy.
#
# PSO-7.A.3'S HEDGE IS "MAY AFFECT", NOT "AFFECTS", and item 17 keys on it. The
# statement's other load-bearing phrase is AT ALL SCALES, which is why suggested
# skill 5.B is the topic's skill: items 13, 18 and 20 place an initiative at a
# named scale and ask what changes at the others.
#
# THE MICROLENDING TRAP. g7_4 already carries six items on microloans under
# SPS-7.D.3, including what they are, the chain from loan to living standard,
# and the limits of a programme's own outcome figures. PSO-7.A.4 names
# microlending too, but for a different reason -- it sits in a LIST beside debt
# crises and lending agencies, and the list's point is that connection shows at
# every scale. Item 25 asks about the list's logic and this module says nothing
# about what a microloan is or does, which g7_4 has already covered.
#
# NO CLAIM IS MADE HERE ABOUT ANY NAMED COUNTRY. The three data items carry
# hypothetical records attached to unnamed regions, an unnamed country and
# unnamed economies.
#
# Three items carry a real `table=`. FIVE choices (A-E).
TOPIC = ("7.6", "Trade and the World Economy", 7)

QUESTIONS = [
 dict(q="What does the framework say establishes the basis for trade?", choices=[
   "Complementarity and comparative advantage",
   "Population size and land area",
   "Distance and the number of shared borders",
   "Climate and soil quality alone",
   "The age of a country's trading ports"], ans=0,
   why="EK PSO-7.A.1 states that complementarity and comparative advantage establish the basis for trade. Two conditions are named rather than one, and each answers a different question about why a flow between two places exists at all."),

 dict(q="What does complementarity between two places mean?", choices=[
   "One place holds a surplus of something the other place demands, so a flow between them is possible",
   "The two places produce exactly the same goods in the same quantities",
   "The two places are the same distance from a third market",
   "The two places have populations of similar size",
   "Neither place produces anything the other lacks"], ans=0,
   why="EK PSO-7.A.1 names complementarity as one of the two things establishing the basis for trade, and the CED does not define it. It is a matching of a surplus on one side to a demand on the other, which is a fact about what each place has and wants rather than about how cheaply either can produce."),

 dict(q="What does comparative advantage mean?", choices=[
   "A place gives up less of its other output to produce a given good than its partner does, so specializing and trading leaves both better off",
   "A place produces more of every good than its partner does",
   "A place has the largest total economy among its trading partners",
   "A place charges the lowest tariff on imported goods",
   "A place is closer to the market than any of its competitors"], ans=0,
   why="EK PSO-7.A.1 names comparative advantage as the second basis for trade, and the CED does not define it. The comparison is between what a place gives up to make one thing rather than another, which is why it is a statement about relative cost rather than about total output."),

 dict(q="Why can two places both gain from trade even when one of them can produce every good more efficiently than the other?", choices=[
   "Because what each place gives up to make a given good still differs, so each can specialize where its own sacrifice is smaller",
   "Because the more efficient place is required to trade by international law",
   "Because trade always benefits the less efficient partner only",
   "Because efficiency has no bearing on what a place produces",
   "Because the two places must produce identical goods"], ans=0,
   why="EK PSO-7.A.1 names comparative advantage rather than absolute output as a basis for trade. Producing one thing means not producing another with the same workers and land, and that forgone alternative can be smaller in the less productive place, which is exactly the case where the concept does work that a comparison of totals cannot."),

 dict(q="An inland region has more timber than its own builders can use, and a neighbouring region with almost no forest is building rapidly. Which of the framework's two bases for trade does this most directly illustrate?", choices=[
   "Complementarity, since a surplus in one place meets a demand in the other",
   "Comparative advantage, since one region gives up less to produce timber",
   "Neither, since the two regions share a border",
   "Both equally, since any trade illustrates both at once",
   "Neither, since timber is a raw material rather than a manufactured good"], ans=0,
   why="EK PSO-7.A.1 names complementarity and comparative advantage as two separate bases. The case states only what each region has and what each region needs, and says nothing about what either gives up to produce timber, so it supplies the first condition and not the second."),

 dict(q="Two regions can each produce both wheat and machinery, but one gives up much more machinery to grow a tonne of wheat than the other does. Which of the framework's two bases for trade does this most directly illustrate?", choices=[
   "Comparative advantage, since the amount of other output forgone differs between them",
   "Complementarity, since one region has a surplus the other demands",
   "Neither, since both regions can produce both goods",
   "Both equally, since two goods are involved",
   "Neither, since no surplus has been stated"], ans=0,
   why="EK PSO-7.A.1 names both bases and the case is stated entirely in terms of what is forgone. No surplus or unmet demand appears anywhere in it, so the condition it supplies is the one about relative cost rather than the one about matching a surplus to a want."),

 dict(q="Why does the framework name TWO bases for trade rather than one?", choices=[
   "They answer different questions, one about what each place has and wants and one about what each place gives up to produce it, and a pair of places can satisfy either without the other",
   "The two terms mean the same thing and are given twice for emphasis",
   "One applies to goods and the other applies only to services",
   "One applies within countries and the other only between continents",
   "The framework names two because trade requires exactly two parties"], ans=0,
   why="EK PSO-7.A.1 puts complementarity and comparative advantage in one sentence as joint conditions. Two places can hold matching surpluses and wants while neither has any cost advantage, and two places can have differing relative costs while neither produces a surplus of anything the other lacks."),

 dict(q="What do neoliberal policies do, in the sense the framework uses the term?", choices=[
   "They reduce government restriction on markets and on trade across borders, so that flows are governed less by state decision and more by market outcome",
   "They increase the number of goods a government produces directly",
   "They fix the prices at which goods may cross a border",
   "They require every country to trade only with its neighbours",
   "They prohibit governments from signing treaties of any kind"], ans=0,
   why="EK PSO-7.A.2 names neoliberal policies, INCLUDING FREE TRADE AGREEMENTS, as what created the new organizations and relationships it lists, and the CED does not define the term. A free trade agreement is an instance of the wider policy of lowering the barriers a state maintains, which is what makes the CED's word 'including' accurate."),

 dict(q="Which organizations does the framework name as examples of what neoliberal policies created?", choices=[
   "The EU, the World Trade Organization, Mercosur, and OPEC",
   "The United Nations, NATO, the World Health Organization, and the International Court of Justice",
   "Primary, secondary, tertiary, and quaternary sectors",
   "Tariffs, subsidies, quotas, and embargoes",
   "Core, semiperiphery, periphery, and the world economy"], ans=0,
   why="EK PSO-7.A.2 names exactly these four as examples of the new organizations, spatial connections and trade relationships created by neoliberal policies. The other lists are real, but they are bodies with other purposes, categories of employment, instruments of trade policy, and positions in the world economy respectively."),

 dict(q="What does the framework say the new organizations and trade relationships it names do?", choices=[
   "They foster greater globalization",
   "They guarantee equal levels of development among their members",
   "They eliminate all economic difference between countries",
   "They prevent any government from setting a tariff",
   "They replace the governments of the countries that join them"], ans=0,
   why="EK PSO-7.A.2 says these organizations, connections and relationships FOSTER GREATER GLOBALIZATION. The verb claims that they encourage a process already under way, which is a weaker and more defensible claim than that they equalize development or supersede governments."),

 dict(q="What is a free trade agreement, as the framework uses the term?", choices=[
   "A treaty under which the signatories lower or remove the barriers each applies to the others' goods",
   "A treaty under which the signatories agree to raise their barriers together",
   "A treaty in which one country agrees to buy a fixed quantity from another",
   "A treaty that sets a single price for a commodity worldwide",
   "A treaty that transfers a territory from one state to another"], ans=0,
   why="EK PSO-7.A.2 names free trade agreements as an instance of neoliberal policies, and the CED does not define them. The defining feature is reciprocal reduction of barriers, which is what makes such an agreement a neoliberal instrument rather than simply any commercial treaty."),

 dict(q="The framework says neoliberal policies created new organizations, new spatial connections, and new trade relationships. What is the difference among the three?", choices=[
   "An organization is a body with members and rules, a spatial connection is a route or flow that now exists between places, and a trade relationship is an ongoing pattern of exchange between particular partners",
   "The three terms all name the same thing in different words",
   "All three refer to treaties signed between governments",
   "All three refer to physical infrastructure such as ports and railways",
   "All three refer to categories of manufactured goods"], ans=0,
   why="EK PSO-7.A.2 lists organizations, spatial connections and trade relationships as three separate products of the same policies. Only the first has members; the second is a fact about geography, since a flow runs between places; and the third can persist without any treaty behind it."),

 dict(q="A group of neighbouring countries signs an agreement removing tariffs on one another's goods. Using the framework's emphasis on scale, what should a geographer expect to change below the level of that agreement?", choices=[
   "Producers in each member country face competition from the others, so which places specialize in which goods can shift within every member as well as between them",
   "Nothing changes below the level of the agreement, since it binds only governments",
   "Only the total volume of world trade changes, and nothing within any member",
   "Every producer in every member country becomes equally competitive",
   "Local production disappears entirely in all member countries"], ans=0,
   why="Suggested skill 5.B for this topic asks students to explain spatial relationships across various geographic scales. EK PSO-7.A.2 says such agreements create new spatial connections, and a connection made at the supranational scale reaches the local one because it changes which producers a local firm is now competing against."),

 dict(q="By what mechanism does lowering trade barriers foster greater globalization?", choices=[
   "Removing a cost that applied only to goods crossing a border makes distant suppliers and customers viable where they were not, so the range over which producers and buyers interact widens",
   "It increases the number of countries that exist in the world",
   "It shortens the physical distance between trading partners",
   "It requires every producer to sell abroad rather than at home",
   "It makes transport free for goods moving between countries"], ans=0,
   why="EK PSO-7.A.2 says neoliberal policies including free trade agreements foster greater globalization. A barrier at a border is a cost that falls on distance-crossing exchange specifically, so lifting it changes which of those exchanges are worth making without changing any physical distance."),

 dict(q="What is a tariff?", choices=[
   "A tax a government levies on goods imported into its territory",
   "A payment a government makes to its own producers",
   "A legal limit on the quantity of a good that may be imported",
   "A ban on trading a good with a particular country",
   "A charge levied on goods moving between two regions of the same country"], ans=0,
   why="EK PSO-7.A.3 names tariffs as an example of a government initiative that may affect economic development, and the CED does not define the term. A tariff is a tax on imports specifically, which distinguishes it from a subsidy paid to producers and from a quota, which limits quantity rather than adding cost."),

 dict(q="At what scales does the framework say government initiatives may affect economic development?", choices=[
   "At all scales",
   "At the national scale only",
   "At the local scale only",
   "At the supranational scale only",
   "At no scale, since development is determined by markets"], ans=0,
   why="EK PSO-7.A.3 states that government initiatives AT ALL SCALES may affect economic development, including tariffs. That phrase is why suggested skill 5.B, on explaining spatial relationships across various geographic scales, is the skill attached to this topic."),

 dict(q="The framework says government initiatives MAY affect economic development. What does that wording claim, and what does it not claim?", choices=[
   "It claims that such initiatives are capable of affecting development without claiming that every initiative does, or that the effect is always the one intended",
   "It claims that every government initiative raises the level of development",
   "It claims that government initiatives never affect development",
   "It claims that only tariffs among government initiatives have any effect",
   "It claims that the effect of an initiative can be predicted exactly in advance"], ans=0,
   why="EK PSO-7.A.3 says government initiatives at all scales MAY affect economic development. A modal claim asserts possibility rather than regularity, which is the honest form for a statement covering everything from a municipal incentive to a national tariff."),

 dict(q="Which set of examples best shows government initiatives operating at three different scales?", choices=[
   "A municipal authority servicing land for an industrial park, a national government setting a tariff, and a group of states signing a trade agreement together",
   "Three separate national governments each setting a tariff in the same year",
   "One national government setting three different tariffs on three goods",
   "Three municipal authorities each granting the same local incentive",
   "A single trade agreement signed by a single state with itself"], ans=0,
   why="EK PSO-7.A.3 says government initiatives at ALL SCALES may affect economic development, and suggested skill 5.B asks for spatial relationships explained across scales. Only one of these sets varies the scale at which the decision is taken rather than varying how many decisions of one kind are counted."),

 dict(q="A government raises a tariff on imported steel. Who inside that country bears the cost, and who gains?", choices=[
   "Buyers of steel pay more, whether they import it or buy it at home, while producers of steel inside the country face a competitor made more expensive",
   "Only foreign producers bear any cost and nobody inside the country is affected",
   "Only domestic steel producers bear the cost, and buyers are unaffected",
   "Nobody bears a cost, because a tariff is paid by the exporting government",
   "Every party inside the country gains and none loses"], ans=0,
   why="EK PSO-7.A.3 names tariffs among the government initiatives that may affect economic development. A tax on the imported version raises what buyers pay for the import and lets the domestic version be sold at a higher price than before, so the effect falls inside the country as well as outside it."),

 dict(q="Why does the phrase AT ALL SCALES matter to how a student analyses a government initiative?", choices=[
   "Because an initiative taken at one scale produces effects at the others, so an account confined to the scale of the decision misses most of what happened",
   "Because initiatives at different scales never interact with one another",
   "Because only the largest scale is worth analysing",
   "Because the scale of an initiative determines whether it is legal",
   "Because every initiative must be taken at every scale simultaneously"], ans=0,
   why="EK PSO-7.A.3 says government initiatives at all scales may affect economic development, and suggested skill 5.B asks students to explain spatial relationships across various geographic scales. A national tariff changes what a local factory pays for materials, so the decision and its consequences sit at different levels."),

 dict(q="What three kinds of thing does the framework name as demonstrating how closely economies have become connected?", choices=[
   "Global financial crises, international lending agencies, and strategies of development",
   "Tariffs, quotas, and embargoes",
   "Primary, secondary, and tertiary employment",
   "Core, semiperiphery, and periphery positions",
   "Complementarity, comparative advantage, and neoliberal policy"], ans=0,
   why="EK PSO-7.A.4 names global financial crises, international lending agencies and strategies of development as the three, and offers debt crises, the International Monetary Fund and microlending as its examples of each. The rejected lists are drawn from the other statements of this unit."),

 dict(q="What is a debt crisis, the framework's example of a global financial crisis?", choices=[
   "A situation in which a borrower cannot meet obligations it has already incurred, so lenders and other borrowers are exposed in turn",
   "A situation in which a country has borrowed nothing at all",
   "A situation in which a lender refuses to make any new loans anywhere",
   "A situation in which the price of one commodity falls sharply",
   "A situation in which two countries dispute the border between them"], ans=0,
   why="EK PSO-7.A.4 offers debt crises as its example of a global financial crisis and does not define them. The reason the CED can call such a crisis GLOBAL is that a debt is a relationship: a borrower who cannot pay is also a lender's unpaid asset, which is how the difficulty travels."),

 dict(q="What is an international lending agency, the second kind of thing the framework names?", choices=[
   "A body that lends to states and often attaches conditions to what it lends, with the International Monetary Fund as the framework's example",
   "A private bank that lends only to households",
   "A body that sets the tariffs its members may charge",
   "A body that owns and operates factories in several countries",
   "A body that measures development but makes no loans"], ans=0,
   why="EK PSO-7.A.4 names international lending agencies and gives the International Monetary Fund as its example. The statement's point is what such a body demonstrates rather than what it decides, and lending across borders is itself one of the connections the statement is about."),

 dict(q="Why does a financial crisis that begins in one economy reach economies far from it?", choices=[
   "Lending, investment and trade tie the balance sheets and the order books of distant economies together, so a loss in one place is a loss to holders and suppliers in many others",
   "Because financial crises spread through physical contact between neighbouring territories",
   "Because every country uses the same currency",
   "Because a crisis in one economy causes crises to begin independently elsewhere",
   "Because international agreements require all countries to enter a crisis together"], ans=0,
   why="EK PSO-7.A.4 says global financial crises demonstrate how different economies have become more closely connected, even interdependent. The connection is the mechanism as well as the lesson: an unpaid debt or a cancelled order is somebody else's missing income, and the chain does not stop at a border."),

 dict(q="Why does the framework list a strategy such as microlending alongside global financial crises and international lending agencies?", choices=[
   "Because all three are cases of finance crossing a boundary, and putting a household-scale instrument beside a world-scale crisis shows the same connectedness reaching every scale",
   "Because all three are the same size and reach the same number of people",
   "Because all three are managed by the same organization",
   "Because microlending is the cause of global financial crises",
   "Because the framework treats the three as alternatives, only one of which is real"], ans=0,
   why="EK PSO-7.A.4 puts all three in one sentence and says they DEMONSTRATE how different economies have become more closely connected. The list is deliberately mixed in scale, which is the same point suggested skill 5.B makes about spatial relationships across various geographic scales."),

 dict(q="The framework says economies have become more closely connected, EVEN INTERDEPENDENT. What does the second word add to the first?", choices=[
   "Connection means the economies affect one another, while interdependence means each now relies on the others in a way it cannot easily undo",
   "The two words mean the same thing and the second is used for emphasis",
   "Interdependence means the economies no longer trade with one another",
   "Interdependence means one economy controls all the others",
   "Interdependence describes a weaker relationship than connection"], ans=0,
   why="EK PSO-7.A.4 says the three cases demonstrate that economies have become more closely connected, EVEN INTERDEPENDENT. The escalation is the point: influence running between two economies is a weaker claim than reliance running both ways, and only the second makes withdrawal costly."),

 dict(q="Two regions are compared in the hypothetical record below. Using the accompanying figures, which conclusion is best supported?",
   table=dict(headers=["Region", "Units of cloth one worker can make in a day", "Units of grain one worker can make in a day"],
     rows=[["Region 1", "8", "6"],
           ["Region 2", "3", "4"]]),
   choices=[
   "Region 1 makes more of both goods, yet Region 2 gives up 0.75 units of cloth for each unit of grain while Region 1 gives up 1.33, so Region 2 holds the comparative advantage in grain and both can gain from specializing",
   "Region 1 makes more of both goods, so there is no basis for trade between them",
   "Region 2 makes more grain per worker than Region 1 does",
   "The two regions give up the same amount of cloth for each unit of grain",
   "Region 1 holds the comparative advantage in both goods because it produces more of both"], ans=0,
   why="Recomputed from the record: Region 1 out-produces Region 2 in both goods, but a unit of grain costs Region 1 eight sixths of a unit of cloth, which is 1.33, and costs Region 2 three quarters of a unit, which is 0.75. EK PSO-7.A.1 names comparative advantage rather than absolute output as a basis for trade, and this is the arrangement in which the two answers differ."),

 dict(q="One country's steel trade before and after a tariff change is recorded in the hypothetical table below. Using the accompanying figures, which conclusion is best supported?",
   table=dict(headers=["Record", "Tariff on imported steel (%)", "Imported steel (thousands of tonnes)", "Steel made inside the country (thousands of tonnes)", "Average price paid by domestic buyers (currency units per tonne)"],
     rows=[["Before the change", "0", "900", "600", "480"],
           ["After the change", "25", "500", "760", "560"]]),
   choices=[
   "Imports fell by about 44 percent while steel made inside the country rose by about 27 percent, and the price domestic buyers paid rose by about 17 percent, so the initiative moved production inward at the buyers' expense",
   "Imports and domestic production both fell after the tariff was imposed",
   "The price paid by domestic buyers was unchanged by the tariff",
   "Domestic production rose by enough to leave the total quantity of steel available unchanged",
   "Imports rose after the tariff was imposed"], ans=0,
   why="Recomputed from the record: imports fall from 900 to 500 thousand tonnes, domestic output rises from 600 to 760, and the average price rises from 480 to 560 currency units, so the quantity replaced domestically is smaller than the quantity of imports lost. EK PSO-7.A.3 says government initiatives at all scales MAY affect economic development, and a record showing a gain and a cost together is what that hedged claim looks like."),

 dict(q="Four economies and their exposure to a single trading partner are set out in the hypothetical record below. Using the accompanying figures, which conclusion is best supported?",
   table=dict(headers=["Economy", "Share of exports going to one partner economy (%)", "Fall in that partner's imports during a downturn (%)", "Fall in this economy's total export earnings (%)"],
     rows=[["Economy 1", "62", "20", "12"],
           ["Economy 2", "35", "20", "7"],
           ["Economy 3", "15", "20", "3"],
           ["Economy 4", "8", "20", "2"]]),
   choices=[
   "One partner's downturn is identical for all four, yet the loss it inflicts runs from about 12 percent down to about 2 percent in step with how much of each economy's trade that partner takes",
   "The downturn costs each economy the same share of its export earnings",
   "The economy sending the smallest share to that partner suffers the largest loss",
   "The four economies send equal shares of their exports to that partner",
   "None of the four economies loses any export earnings from the downturn"], ans=0,
   why="Recomputed from the record: the partner's imports fall by 20 percent in every case, and each economy's loss is that fall applied to its own exposure, giving about 12, 7, 3 and 2 percent. EK PSO-7.A.4 says economies have become more closely connected, EVEN INTERDEPENDENT, and exposure rather than the size of the shock is what decides how far the connection carries."),

 dict(q="A student must state what this topic's four essential knowledge statements establish together. Which account is accurate?", choices=[
   "Complementarity and comparative advantage give trade its basis, neoliberal policies including free trade agreements built organizations and relationships that foster globalization, government initiatives at every scale may affect development, and crises, lending agencies and development strategies show how interdependent economies have become",
   "Trade rests on comparative advantage alone, and no government initiative has any effect on development",
   "Neoliberal policies created organizations that ended all differences in development between countries",
   "Government initiatives determine development completely, and trade plays no part",
   "Economies are connected but not interdependent, and no crisis in one reaches another"], ans=0,
   why="EK PSO-7.A.1 supplies the basis for trade, EK PSO-7.A.2 the organizations and relationships and what they foster, EK PSO-7.A.3 the government initiatives with their hedge, and EK PSO-7.A.4 the interdependence. Each rejected summary either drops one of the four statements or strengthens a hedged claim into one the framework does not make."),
]
