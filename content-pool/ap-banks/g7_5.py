# AP HUMAN GEOGRAPHY 7.5 Theories of Development -- 30 questions
# CED Course Framework V.1, Unit 7. Enduring understanding SPS-7,
# "Industrialization, past and present, has facilitated improvements in
# standards of living, but it has also contributed to geographically uneven
# development." Learning objective SPS-7.E, "Explain different theories of
# economic and social development." Suggested skill 1.E, "Explain the
# strengths, weaknesses, and limitations of different geographic models and
# theories in a specified context."
#
# Essential knowledge -- ONE statement, and it is short:
#   SPS-7.E.1  Different theories, such as Rostow's Stages of Economic Growth,
#              Wallerstein's World System Theory, dependency theory, and
#              commodity dependence, help explain spatial variations
#              in development.
#
# THE STATEMENT NAMES FOUR THEORIES AND DESCRIBES NONE OF THEM. That is the
# authoring problem for this topic, and the way it is handled here is the same
# way g7_2 handled least cost theory: the CED requires the theories to be
# explained (SPS-7.E says "explain different theories"), so the module supplies
# the discipline's standard content for each and says so here, rather than
# pretending the CED spelled it out. Every such definition is flagged below.
# Where the CED DOES supply a sentence, it is cited in the item's `why`:
#   - the unit overview, page 121: the theories "are in turn useful in
#     explaining spatial variations in development such as core-periphery
#     relationships"
#   - SPS-7.B.2, which names core, semiperiphery and periphery locations
#   - SPS-7.A.3, which says investors in industry sought out more raw materials
#     and new markets, a factor that contributed to the rise of colonialism and
#     imperialism -- this is the CED's own sentence behind item 23
#   - PSO-5.E.2, which records that some countries have become highly dependent
#     on one or more export commodities
#   - the unit 7 sample activity, page 123, which asks students to compare the
#     four theories and to discuss "how different countries are classified
#     according to the different theories" -- that is the CED licensing the
#     classification items, 9 and 17
#
# ROSTOW'S FIVE STAGES, supplied because the CED names the model without stating
# it. Items 4 to 8 take one each, in order:
#   traditional society          subsistence agriculture, limited technology,
#                                little surplus available to invest
#   preconditions for take-off   transport, banking and commercial agriculture
#                                built up before industry itself grows
#   take-off                     a few leading industries grow rapidly, cities
#                                draw in labour, growth begins to sustain itself
#   drive to maturity            industrial technique spreads beyond those first
#                                sectors and the economy diversifies
#   high mass consumption        services dominate employment and consumer goods
#                                are widely owned
#
# WALLERSTEIN, likewise supplied: one capitalist world economy rather than a set
# of separate national ones, with core, semiperiphery and periphery as positions
# within it. The CED itself names those three words in EK SPS-7.B.2, so the
# vocabulary is on-syllabus even though the theory's content is not written out.
#
# THE ONE-THING-ASKED-TWICE RISK IS REAL HERE. g7_2 q23 and g6_2 q7 BOTH already
# ask what the words core, semiperiphery and periphery refer to, and both key on
# "positions in the world economy". This module therefore does NOT ask that
# question a third time. It asks instead what each tier is CHARACTERIZED BY
# (items 14, 15, 16), what the theory takes as its unit of analysis (13), and
# whether a position is permanent (18) -- none of which either sibling asks.
# Similarly, g5_9 already covers commodity dependence from the agricultural
# side, including the price-volatility risk, so items 25 and 26 here ask what
# makes it an EXPLANATION OF DEVELOPMENT and what it predicts that a stage model
# does not, rather than restating the risk.
#
# SKILL 1.E IS THE TOPIC'S SUGGESTED SKILL and it asks for weaknesses and
# limitations, not only content. Items 11, 12, 19 and 24 are that skill, one
# limitation per theory, and each is a limitation of the theory's REACH rather
# than a claim that the theory is false -- an over-strong criticism would be as
# wrong as no criticism.
#
# WHAT THIS MODULE WILL NOT ASSERT: that any one of the four theories is
# correct, that the CED endorses one of them, or that the framework ranks them.
# SPS-7.E.1 says they HELP EXPLAIN, and item 30 keys on exactly that hedge.
#
# NO REAL COUNTRY IS NAMED ANYWHERE IN THIS MODULE. The three data items carry
# hypothetical records attached to unnamed economies and groups.
#
# SYNONYM CARE. `geo_check` treats {"world system theory", "world-systems
# theory", "core-periphery model"} as one construct and {"stages of economic
# growth", "rostow's model", "modernization model"} as another, so every choice
# list names each theory in exactly one way, using the CED's own wording.
#
# Three items carry a real `table=`. FIVE choices (A-E).
TOPIC = ("7.5", "Theories of Development", 7)

QUESTIONS = [
 dict(q="What does the framework say the different theories of development do?", choices=[
   "They help explain spatial variations in development",
   "They predict the exact year each country will reach a given income",
   "They rank countries by land area",
   "They describe the physical geography of each world region",
   "They set the development policy every country is required to follow"], ans=0,
   why="EK SPS-7.E.1 states that different theories help explain spatial variations in development. The verb is HELP EXPLAIN, which claims that the theories illuminate a pattern rather than that any of them dictates policy or forecasts a date."),

 dict(q="Which four theories of development does the framework name?", choices=[
   "Rostow's Stages of Economic Growth, Wallerstein's World System Theory, dependency theory, and commodity dependence",
   "The demographic transition model, Malthusian theory, the epidemiological transition, and the gravity model",
   "Von Thunen's model, least cost theory, central place theory, and the rank-size rule",
   "The concentric zone model, the sector model, the multiple nuclei model, and the galactic city model",
   "Environmental determinism, possibilism, cultural ecology, and political ecology"], ans=0,
   why="EK SPS-7.E.1 names exactly these four as its examples of theories that help explain spatial variations in development. The rejected lists are real bodies of theory from other units, which is what makes them plausible and what makes the distinction worth drawing."),

 dict(q="What kind of explanation is Rostow's Stages of Economic Growth?", choices=[
   "A sequence of stages that an economy is held to pass through in order, so a country's level of development is read as its position along one path",
   "A classification of countries by the natural resources found in their territory",
   "An account of where factories choose to locate inside one country",
   "A ranking of countries by the size of their population",
   "An account of how a city arranges its land uses around a centre"], ans=0,
   why="The CED names the model without stating it, and learning objective SPS-7.E requires students to explain it. Its defining feature is the ordered sequence: development is treated as a journey along a single path, which is what makes the model comparable with and opposed to the relational theories named beside it."),

 dict(q="What characterizes the first stage of Rostow's sequence, traditional society?", choices=[
   "Output comes mainly from subsistence agriculture, technology is limited, and little surplus is available to invest",
   "Most employment is in services and consumer goods are widely owned across the population",
   "Growth has become self-sustaining across a wide range of diversified industries",
   "A small number of leading industries are growing rapidly for the first time",
   "Transport and banking are being built up in preparation for industry"], ans=0,
   why="EK SPS-7.E.1 names Rostow's Stages of Economic Growth and learning objective SPS-7.E asks students to explain it. The first stage is defined by the absence of the surplus that later investment requires, which is why the model treats it as the point every economy starts from. The four rejected descriptions are the model's other four stages."),

 dict(q="What happens during the preconditions for take-off, the second stage of Rostow's sequence?", choices=[
   "Transport, banking and commercial agriculture are built up, creating the conditions industry will need before industry itself grows",
   "Consumer durables become widely owned and services dominate employment",
   "Industrial technique spreads across the whole economy and output diversifies",
   "Output falls back to subsistence farming with little surplus",
   "Manufacturing employment reaches its maximum share and then declines"], ans=0,
   why="Learning objective SPS-7.E asks students to explain the theories the CED names. This stage is defined by investment in things that are not themselves industry -- roads, ports, credit, farms selling into markets -- and the sequence matters because industry cannot grow without them already in place."),

 dict(q="What defines the take-off stage in Rostow's sequence?", choices=[
   "A small number of leading industries grow rapidly, cities draw in labour, and growth begins to sustain itself",
   "Every sector of the economy grows at the same rate at the same time",
   "Agriculture disappears entirely from the economy",
   "Household consumption of manufactured goods reaches its highest level",
   "Investment in transport and banking begins for the first time"], ans=0,
   why="Learning objective SPS-7.E asks for an explanation of Rostow's Stages of Economic Growth. Take-off is narrow rather than general: the model's claim is that growth starts in a few sectors and that this is the point at which it stops depending on an outside push, which is also why the stage is the one most often disputed."),

 dict(q="What distinguishes the drive to maturity from the stage before it in Rostow's sequence?", choices=[
   "Industrial technique spreads beyond the first leading sectors, so the economy diversifies and can produce a wide range of goods",
   "The economy returns to relying on a single leading industry",
   "Population growth stops and the workforce contracts",
   "Foreign trade ceases and the economy supplies only itself",
   "Agriculture becomes the largest source of employment again"], ans=0,
   why="Learning objective SPS-7.E asks students to explain the model. The difference between the two stages is breadth rather than speed: take-off concerns a few sectors and maturity concerns their methods reaching the rest of the economy, which is why the model treats maturity as the point at which growth no longer depends on any one industry."),

 dict(q="What characterizes the age of high mass consumption, the last stage of Rostow's sequence?", choices=[
   "Services dominate employment and manufactured consumer goods are widely owned across the population",
   "Most employment is in extraction and most output is exported unprocessed",
   "A small number of industries account for nearly all output",
   "Investment shifts entirely into building roads, ports and banks",
   "Subsistence farming supports the majority of households"], ans=0,
   why="Learning objective SPS-7.E asks for an explanation of the model, and EK SPS-7.B.1 supplies the vocabulary of sectors that the last stage is described in. The stage is defined by what households can buy as much as by what the economy makes, which is why it is named for consumption rather than for production."),

 dict(q="A country's rail network and ports have recently been extended, its farms increasingly sell into markets rather than feeding only the household, and its first large factories have not yet appeared. Which stage of Rostow's sequence does this best describe?", choices=[
   "The preconditions for take-off stage",
   "The traditional society stage",
   "The take-off stage",
   "The drive to maturity stage",
   "The age of high mass consumption"], ans=0,
   why="The unit 7 sample activity asks students to discuss how countries are classified according to the different theories, which is what this case requires. Infrastructure and commercial agriculture are in place while industry is not, and that combination is what the second stage of the model describes rather than the first or the third."),

 dict(q="Where does Rostow's model locate the cause of a country's movement from one stage to the next?", choices=[
   "In conditions inside the country, above all the accumulation and investment of capital in leading sectors",
   "In the country's relationships with the countries it trades with",
   "In the physical size of the country's territory",
   "In the number of neighbouring countries it shares a border with",
   "In the climate zone the country occupies"], ans=0,
   why="Learning objective SPS-7.E asks students to explain different theories, and the theories differ most in where they place the cause. A stage model is internalist: it explains a country's position by what that country has done, which is the assumption dependency theory attacks directly."),

 dict(q="Which is the strongest criticism of Rostow's Stages of Economic Growth as an explanation of spatial variations in development?", choices=[
   "It treats each country as an independent case following the same path, so it cannot account for the effect one country's development has on another's",
   "It denies that any country has ever industrialized",
   "It applies only to countries that have already reached its final stage",
   "It contains no reference to agriculture at any point",
   "It asserts that economic development is impossible"], ans=0,
   why="Suggested skill 1.E for this topic asks students to explain the weaknesses and limitations of a theory in context. EK SPS-7.A.3 records that industrial investors sought raw materials and new markets abroad, which is precisely a case of one country's development acting on another's, and a model of independent national paths has no place to put it."),

 dict(q="A second limitation often raised against a stage model of development concerns the cases the sequence was drawn from. What is that limitation?", choices=[
   "The sequence was generalized from the histories of a small number of countries that industrialized early, which does not establish that later developers face the same conditions",
   "The sequence was generalized from countries that have never industrialized at all",
   "The sequence was generalized from a single year of trade statistics",
   "The sequence names no stages and so cannot be tested",
   "The sequence was generalized from countries chosen at random from every continent"], ans=0,
   why="Suggested skill 1.E asks for the limitations of a model in a specified context. A generalization holds only over the range it was drawn from, and a country industrializing today faces a world that already contains industrialized competitors, which the early cases did not."),

 dict(q="What does Wallerstein's World System Theory take as its unit of analysis?", choices=[
   "A single world economy, within which countries occupy positions, rather than a set of separate national economies each developing on its own",
   "One country at a time, examined in isolation from the others",
   "The individual firm and the supply chain it manages",
   "The city and the rural region immediately surrounding it",
   "The household and the way it allocates its labour"], ans=0,
   why="EK SPS-7.E.1 names the theory and learning objective SPS-7.E requires it to be explained. Choosing the unit of analysis is the theory's first and largest move: if the world economy is one system, a country's development is a fact about its position in that system rather than a fact about the country alone."),

 dict(q="On Wallerstein's account, what characterizes economies in the core?", choices=[
   "Capital-intensive, high-skill and high-wage production, together with the strongest states and the largest share of the profits from world trade",
   "Low-wage extraction of raw materials for processing in other regions",
   "Production of a single agricultural commodity for export",
   "An absence of manufacturing of any kind",
   "Complete self-sufficiency and no participation in world trade"], ans=0,
   why="EK SPS-7.B.2 names core, semiperiphery and periphery locations, and the unit overview says these theories explain spatial variations such as core-periphery relationships. The core is defined by the KIND of production it holds rather than by wealth alone, which is why the definition names skill, capital and the share of the returns together."),

 dict(q="On Wallerstein's account, what characterizes economies in the periphery?", choices=[
   "Low-wage, labour-intensive extraction and production supplying materials and goods that are turned into higher-value products elsewhere",
   "Capital-intensive research and the most profitable stages of production",
   "The largest share of the world's financial services",
   "A refusal to trade with any other region",
   "The highest wages and the most advanced technology in the world economy"], ans=0,
   why="EK SPS-7.B.2 names periphery locations among those that manufacturing factors influence. The definition turns on where in a chain of production the work sits rather than on how much work there is, which is why a peripheral economy can be busy and still capture little of the value."),

 dict(q="What role does the semiperiphery play in Wallerstein's World System Theory?", choices=[
   "An intermediate position that both draws value from the periphery and supplies lower-value production to the core, so the system is not divided into two opposed halves",
   "A position identical to the core in every respect",
   "A position identical to the periphery in every respect",
   "A group of countries that have withdrawn from the world economy",
   "A group of countries with no trade in either direction"], ans=0,
   why="EK SPS-7.B.2 names the semiperiphery alongside the other two, and a three-part division rather than a two-part one is a substantive claim. A tier that is exploited by one side and exploiting on the other has interests pulling both ways, which is what the theory means when it treats the middle tier as stabilizing the whole."),

 dict(q="An economy exports assembled electronics made from components designed and patented elsewhere, has a rapidly growing manufacturing workforce, and is itself a large buyer of unprocessed minerals from poorer neighbours. Which position in Wallerstein's World System Theory does this best fit?", choices=[
   "The semiperiphery, since it stands above the suppliers it buys from and below the economies that design what it assembles",
   "The core, because it exports manufactured goods",
   "The periphery, because it buys minerals from its neighbours",
   "Outside the world economy, because it trades in both directions",
   "The core, because its manufacturing workforce is growing"], ans=0,
   why="The unit 7 sample activity asks students to discuss how countries are classified according to the different theories. Exporting manufactures is not by itself a core characteristic when the design and the patents sit elsewhere, and buying materials from poorer suppliers is not a peripheral one, so the case is defined by holding both relations at once."),

 dict(q="Does Wallerstein's World System Theory hold that a country's position in the system is permanent?", choices=[
   "No, an individual country can move between positions, but the theory holds that the three-tier structure itself persists",
   "Yes, no country has ever changed its position",
   "Yes, because positions are fixed by physical geography",
   "No, and the theory holds that the structure disappears as countries move",
   "The theory makes no claim about position at all"], ans=0,
   why="Learning objective SPS-7.E asks for the theories to be explained, and this is the distinction students most often lose. The claim is about the structure rather than about any occupant of it: movement of countries between tiers is compatible with the tiers themselves remaining, in the same way that mobility between income groups does not abolish the groups."),

 dict(q="Which is a fair limitation to state about the World System Theory as an explanatory tool?", choices=[
   "Its three categories are broad and their boundaries rest on no agreed measure, so placing a particular country is a matter of judgement rather than of calculation",
   "It has no way of describing trade between two countries",
   "It has no way of describing wealthy economies",
   "It denies that any inequality exists between countries",
   "It applies only to countries that do not trade at all"], ans=0,
   why="Suggested skill 1.E asks for the limitations of a theory in a specified context. EK SPS-7.C.1 and EK SPS-7.C.3 supply measured indicators such as gross national income per capita and the Human Development Index, and the contrast is instructive: a category with no threshold cannot be applied the way a measured index can."),

 dict(q="What is the central claim of dependency theory?", choices=[
   "That the poverty of poorer countries is produced and maintained by their relationship with wealthier ones, rather than being an earlier stage those countries have yet to leave",
   "That every country passes through the same sequence of stages in the same order",
   "That a country's level of development follows from its physical resources alone",
   "That poorer countries have never traded with wealthier ones",
   "That differences in wealth between countries have no cause that can be identified"], ans=0,
   why="EK SPS-7.E.1 names dependency theory as one of the theories that help explain spatial variations in development. Its explanation is relational: the same set of connections that makes one place rich is what keeps another poor, so poverty is treated as an outcome of a link rather than as a starting condition."),

 dict(q="Where do dependency theory and Rostow's Stages of Economic Growth disagree most sharply?", choices=[
   "On whether a poor country's condition is an early point on a path everyone travels or a position created by its links with rich countries",
   "On whether countries trade with one another at all",
   "On whether industrialization has ever taken place anywhere",
   "On whether agriculture exists in poorer countries",
   "On whether measures of development can be collected"], ans=0,
   why="EK SPS-7.E.1 names both among the theories that help explain spatial variations in development, and the unit 7 sample activity asks students to compare and contrast them. The disagreement is about the cause rather than about the facts: both accept that countries differ, and they differ over whether the difference is a stage or a relation."),

 dict(q="By what mechanism does dependency theory say the relationship keeps poorer countries poor?", choices=[
   "They supply raw materials and buy finished manufactures, so the stages that add most of the value, and the profits from them, remain in the wealthier countries",
   "They are forbidden by treaty to manufacture anything",
   "They have no ports through which goods could be traded",
   "They produce more manufactured goods than they are able to sell",
   "They receive all of the profits from world trade and then spend them badly"], ans=0,
   why="EK SPS-7.E.1 names dependency theory, and EK PSO-5.E.1 places agricultural products in a global supply chain in which value is added at successive stages. If the later stages are carried out abroad, the earnings from them accrue abroad, which is the mechanism the theory points to rather than any prohibition."),

 dict(q="How does the framework's account of the Industrial Revolution connect to dependency theory?", choices=[
   "Industrial investors sought raw materials and new markets abroad, which contributed to colonialism and imperialism, and the theory treats the trading relationships formed then as the source of present inequality",
   "The framework says industrialization had no effect beyond the countries where it began",
   "The framework says colonialism had ended before industrialization began",
   "The framework says raw materials were never traded across borders",
   "The two accounts concern entirely separate periods and cannot be connected"], ans=0,
   why="EK SPS-7.A.3 states that investors in industry sought out more raw materials and new markets, a factor that contributed to the rise of colonialism and imperialism. That sentence describes the formation of exactly the material-for-manufactures relationship dependency theory takes as its subject, which is why the two topics belong in one unit."),

 dict(q="Which is a fair limitation to state about dependency theory?", choices=[
   "It accounts well for persistent poverty but has more difficulty explaining economies that have moved from supplying materials to exporting manufactures",
   "It has no way of describing a relationship between two countries",
   "It denies that international trade takes place",
   "It contains no account of the colonial period",
   "It applies only to countries that export nothing"], ans=0,
   why="Suggested skill 1.E asks for the limitations of a theory in a specified context. A theory built to explain why a condition persists is under most strain from the cases in which it did not persist, and stating that plainly is what distinguishes a limitation from a rejection."),

 dict(q="What condition does commodity dependence name, and why is it offered as an explanation of development rather than only as a description of trade?", choices=[
   "A large share of export earnings coming from one or a few primary commodities, which explains development because it ties the whole economy's income to prices set outside it",
   "The total quantity of goods a country imports each year, which explains development because imports determine national wealth",
   "The number of trading partners a country deals with, which explains development because partners determine growth",
   "The share of a country's land under cultivation, which explains development because land area determines income",
   "The number of ports a country operates, which explains development because ports determine the volume of trade"], ans=0,
   why="EK PSO-5.E.2 records that some countries have become highly dependent on one or more export commodities, and EK SPS-7.E.1 lists commodity dependence among the theories that help explain spatial variations in development. Concentration is what turns an export pattern into an explanation, because it makes a single external price a fact about the entire economy."),

 dict(q="What does commodity dependence predict about a country's development that a stage model does not?", choices=[
   "That an economy can earn a great deal in a good year and still not build the diversified industry a stage model treats as the next step, because the earnings rest on one price rather than on a broadening base",
   "That every economy will reach its final stage at the same time",
   "That an economy exporting commodities cannot engage in trade",
   "That commodity prices are fixed by international agreement",
   "That an economy with one leading export has no other economic activity"], ans=0,
   why="EK SPS-7.E.1 names both commodity dependence and Rostow's Stages of Economic Growth as theories that help explain spatial variations in development, and the two make different predictions about the same evidence. A stage model reads high earnings as progress along the path, while commodity dependence reads them as a fact about one price that need not broaden the economy at all."),

 dict(q="Four economies are compared in the hypothetical record below. Using the accompanying figures, which conclusion is best supported?",
   table=dict(headers=["Economy", "Export earnings from the largest single commodity (millions of currency units)", "Total export earnings (millions of currency units)", "Fall in total export earnings after that commodity's price fell by one third (%)"],
     rows=[["Economy 1", "3,600", "4,500", "27"],
           ["Economy 2", "900", "4,500", "7"],
           ["Economy 3", "2,700", "5,400", "17"],
           ["Economy 4", "480", "4,800", "3"]]),
   choices=[
   "The share of export earnings coming from one commodity runs from 80 percent down to 10 percent, and the loss each economy suffers from the same price fall tracks that share rather than the size of its export trade",
   "Every economy loses the same proportion of its export earnings when the commodity price falls",
   "The economy earning the smallest share from one commodity suffers the largest fall in total earnings",
   "Total export earnings are identical across all four economies",
   "None of the four economies earns more than half of its export income from a single commodity"], ans=0,
   why="Recomputed from the record: the largest commodity supplies 80, 20, 50 and 10 percent of export earnings, and the losses of 27, 7, 17 and 3 percent are each about a third of that share, while total export earnings of 4,500, 4,500, 5,400 and 4,800 are close together and do not order the losses. EK SPS-7.E.1 names commodity dependence as a theory that helps explain spatial variations in development, and concentration rather than size is what the record shows doing the work."),

 dict(q="The composition of employment in four economies is set out in the hypothetical table below. Using the accompanying figures, which economy is furthest along the sequence Rostow's model describes?",
   table=dict(headers=["Economy", "Employment in the primary sector (%)", "Employment in the secondary sector (%)", "Employment in the tertiary and higher sectors (%)"],
     rows=[["Economy 1", "68", "12", "20"],
           ["Economy 2", "41", "31", "28"],
           ["Economy 3", "22", "34", "44"],
           ["Economy 4", "4", "19", "77"]]),
   choices=[
   "The fourth economy, where only 4 percent of employment remains in the primary sector and 77 percent is in services, which is the composition the model places at its final stage",
   "The first economy, because the largest share of its employment is in the primary sector",
   "The second economy, because its primary and secondary shares are closest to being equal",
   "The third economy, because it has the largest share of employment in the secondary sector",
   "None of them can be compared, because the shares in each row do not add to a whole"], ans=0,
   why="Recomputed from the record: every row adds to 100, and the economy with the smallest primary share is also the one with the largest tertiary share, so the two measures agree on which is furthest along. EK SPS-7.B.1 says the sectors are characterized by distinct development patterns, and the last of Rostow's stages is defined by services dominating employment."),

 dict(q="Trade between two groups of economies in a hypothetical world region is recorded below. Using the accompanying figures, which conclusion is best supported?",
   table=dict(headers=["Direction of flow", "Value (millions of currency units)", "Share of the flow that is unprocessed material (%)", "Share of the flow that is manufactured or high-technology goods (%)"],
     rows=[["Group A to Group B", "1,800", "82", "18"],
           ["Group B to Group A", "1,800", "9", "91"]]),
   choices=[
   "The two flows are equal in value but opposite in composition, with 82 percent of what one group sends being unprocessed material and 91 percent of what the other sends being manufactured, which is the division of roles the relational theories describe",
   "One group sends mostly manufactured goods and receives mostly manufactured goods in return",
   "One group receives nothing at all from the other",
   "The two groups trade goods of the same composition in both directions",
   "One group's exports are worth more than twice as much as the other's"], ans=0,
   why="Recomputed from the record: both flows are 1,800 million currency units, the two shares in each row add to 100, and the compositions are reversed between them. The unit overview says these theories explain spatial variations in development such as core-periphery relationships, and a balanced value of trade carrying an unbalanced composition is what such a relationship looks like in data."),

 dict(q="A student must state what this topic's single essential knowledge statement establishes. Which account is accurate?", choices=[
   "Four named theories are offered as different explanations, and the framework's claim is that they help explain spatial variations in development rather than that any one of them is the settled answer",
   "One theory of development is named and students are required to use it alone",
   "Four theories are named and the framework states that they make identical predictions",
   "Four theories are named and the framework states that none of them explains anything",
   "No theory of development is named anywhere in this topic"], ans=0,
   why="EK SPS-7.E.1 says that DIFFERENT theories, such as the four it lists, HELP EXPLAIN spatial variations in development. Both hedges carry weight: the plural means the framework is not choosing between them, and the verb means each is treated as a partial aid to explanation rather than as a proven law."),
]
