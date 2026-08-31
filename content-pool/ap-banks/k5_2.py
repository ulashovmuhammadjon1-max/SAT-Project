# AP COMPARATIVE GOVERNMENT AND POLITICS 5.2 Political Responses to Global
# Market Forces
# CED effective Fall 2026, Unit 5 Political and Economic Changes and Development.
# Enduring understanding IEF-3; learning objective IEF-3.B (compare political
# responses to global market forces). Suggested skill 2.C, Country Comparison.
#
# Essential knowledge relied on:
#   IEF-3.B.1  IN RESPONSE TO MARKET FORCES, course countries CONTINUE TO
#              EXPERIMENT with POLICIES REGARDING PRIVATE OWNERSHIP OF INDUSTRY AND
#              CAPITAL, including:
#     .a SPECIAL ECONOMIC ZONES ALONG THE COAST OF CHINA
#     .b PRIVATIZATION AND INCREASED COMPETITION IN MEXICO'S OIL INDUSTRY (Pemex)
#     .c NIGERIA'S STATE-OWNED NIGERIAN NATIONAL PETROLEUM CORPORATION COLLABORATING
#        WITH FOREIGN COMPANIES IN JOINT VENTURES TO EXTRACT AND PRODUCE OIL
#     .d PUTIN'S RE-NATIONALIZATION OF OIL AND NATURAL GAS INDUSTRIES and IMPOSITION
#        OF FOREIGN INVESTMENT LIMITATIONS
#   IEF-3.B.2  course countries allow VARYING DEGREES OF PRIVATE CONTROL OF NATURAL
#              RESOURCES, with the UNITED KINGDOM ALLOWING THE MOST and CHINA
#              ALLOWING THE LEAST
#   IEF-3.B.3  GOVERNMENTS RESPOND TO GLOBAL MARKET FORCES IN ORDER TO:
#     .a IMPROVE DOMESTIC ECONOMIC CONDITIONS
#     .b RESPOND TO DOMESTIC DEMANDS
#     .c CONTROL OR INFLUENCE DOMESTIC POLITICAL DEBATES TO MAINTAIN OR INCREASE
#        THEIR OWN POWER
#     .d EXTEND NATIONAL INFLUENCE REGIONALLY AND INTERNATIONALLY
#
# THE FOUR EXAMPLES DO NOT POINT THE SAME WAY, and that is the whole point of the
# topic. Two open (coastal special economic zones, privatization and increased
# competition in an oil industry), one is a hybrid (a state-owned corporation
# entering joint ventures with foreign firms while remaining state-owned), and one
# closes (re-nationalization plus limits on foreign investment). A student who has
# learned "globalization means liberalization" has no way to place the fourth.
# IEF-3.B.1's own verb is EXPERIMENT, which is why item 14 keys the absence of a
# single direction and items 11-13 compare pairs running opposite ways.
#
# IEF-3.B.2 IS A SPECTRUM WITH TWO NAMED ENDS, not a list. The framework fixes
# only the endpoints -- the United Kingdom most private control, China least --
# and says the others vary between. Items 6, 7 and 19 key it that way, and the
# module never places a third country on the scale, because the framework does
# not.
#
# IEF-3.B.3.c IS THE MOTIVE STUDENTS DROP. Three of the four reasons are about the
# economy or the public; the third is about the government's own hold on power,
# and it is the one that explains why an authoritarian and a democratic government
# can adopt the same measure for different reasons. Items 9 and 15 key it.
#
# NOTHING HERE TURNS ON CURRENT EVENTS: no price, no output figure, no election,
# no date beyond what the framework itself states. Every table figure is
# HYPOTHETICAL and labelled so.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md.
TOPIC = ("5.2", "Political Responses to Global Market Forces", 5)

_T_SPECTRUM = dict(
    headers=["Country (hypothetical)",
             "Natural resource output produced by privately owned firms (percent)",
             "Limits on foreign investment in the resource sector"],
    rows=[["Country A", "91", "None"],
          ["Country B", "62", "Some"],
          ["Country C", "28", "Extensive"],
          ["Country D", "4", "Extensive"]])

_T_EPISODE = dict(
    headers=["Episode (hypothetical)", "What the government did"],
    rows=[["Episode 1", "Opened designated coastal areas to foreign investment on special terms"],
          ["Episode 2", "Allowed private investment in the national oil company and admitted competitors to the industry"],
          ["Episode 3", "Kept the national petroleum corporation in state hands while entering joint ventures with foreign firms to extract and produce oil"],
          ["Episode 4", "Returned oil and natural gas firms to state ownership and imposed limits on foreign investment"]])

_T_MOTIVE = dict(
    headers=["Government statement (hypothetical)", "Reason given for the policy"],
    rows=[["Statement 1", "To raise output and employment at home"],
          ["Statement 2", "To answer petitions submitted by citizens and associations"],
          ["Statement 3", "To shape how the measure is argued about at home and secure the government's own position"],
          ["Statement 4", "To increase the country's weight within its region and beyond it"]])

QUESTIONS = [
 dict(q="According to the framework, what do the course countries continue to experiment with in response to market forces?",
   choices=[
     "policies regarding private ownership of industry and capital",
     "the number of chambers in their legislatures",
     "the length of their executives' terms",
     "the rules governing party registration",
     "the composition of their high courts"], ans=0,
   why="EK IEF-3.B.1 states that in response to market forces course countries continue to experiment with policies regarding private ownership of industry and capital, and the word experiment signals that these policies are unsettled rather than fixed."),
 dict(q="Which policy does the framework record along the coast of China?",
   choices=[
     "special economic zones",
     "the re-nationalization of natural gas firms",
     "the privatization of the national oil company",
     "joint ventures between a state petroleum corporation and foreign firms",
     "a ban on all foreign investment"], ans=0,
   why="EK IEF-3.B.1.a names special economic zones along the coast of China as one of the experiments with policies regarding private ownership of industry and capital. The rejected policies are the framework's Russian, Mexican and Nigerian examples."),
 dict(q="What does the framework record in Mexico's oil industry?",
   choices=[
     "privatization and increased competition",
     "the creation of special economic zones",
     "re-nationalization and limits on foreign investment",
     "the abolition of the national oil company",
     "a prohibition on joint ventures with foreign firms"], ans=0,
   why="EK IEF-3.B.1.b names privatization and increased competition in Mexico's oil industry, and EK LEG-5.A.3.a records the same country's decision to allow private investment in that company."),
 dict(q="How does the framework describe the arrangement involving Nigeria's national petroleum corporation?",
   choices=[
     "a state-owned corporation collaborating with foreign companies in joint ventures to extract and produce oil",
     "a fully privatized corporation competing with foreign firms",
     "a corporation barred from any dealings with foreign firms",
     "a corporation returned to state ownership after being privatized",
     "a corporation operating only inside special economic zones"], ans=0,
   why="EK IEF-3.B.1.c states that Nigeria's state-owned Nigerian National Petroleum Corporation collaborates with foreign companies in joint ventures to extract and produce oil, so the corporation stays in state hands while foreign firms take part."),
 dict(q="Which pair of measures does the framework record in Russia?",
   choices=[
     "the re-nationalization of oil and natural gas industries together with the imposition of foreign investment limitations",
     "the privatization of oil and gas industries together with the removal of investment limits",
     "the creation of coastal special economic zones together with tax concessions",
     "the sale of a national petroleum corporation together with the admission of competitors",
     "joint ventures with foreign firms together with the transfer of ownership to them"], ans=0,
   why="EK IEF-3.B.1.d names the re-nationalization of oil and natural gas industries and the imposition of foreign investment limitations together, so the two measures run in the same direction and both reduce private and foreign control."),
 dict(q="Which course country does the framework place at the end of its spectrum allowing the most private control of natural resources?",
   choices=[
     "the United Kingdom",
     "China",
     "Russia",
     "Nigeria",
     "Iran"], ans=0,
   why="EK IEF-3.B.2 states that course countries allow varying degrees of private control of natural resources, with the United Kingdom allowing the most private control."),
 dict(q="At the opposite end of that same spectrum, which country allows the least private control of natural resources?",
   choices=[
     "China",
     "the United Kingdom",
     "Mexico",
     "Nigeria",
     "Russia"], ans=0,
   why="EK IEF-3.B.2 states that course countries allow varying degrees of private control of natural resources, with China allowing the least private control."),
 dict(q="Which set of purposes does the framework give for governments' responses to global market forces?",
   choices=[
     "improving domestic economic conditions, responding to domestic demands, controlling or influencing domestic political debates to maintain or increase their own power, and extending national influence regionally and internationally",
     "reducing the number of political parties, lengthening legislative terms, and appointing regional governors",
     "joining supranational organizations, adopting a common currency, and abolishing tariffs",
     "increasing the size of the armed forces, extending conscription, and expanding intelligence services",
     "widening the franchise, holding referendums, and creating an independent electoral commission"], ans=0,
   why="EK IEF-3.B.3 names exactly those four purposes. Two of them concern the economy and the public, one concerns the government's own hold on power, and one concerns the country's standing abroad."),
 dict(q="Which of the framework's stated purposes concerns the government's own hold on power rather than economic conditions?",
   choices=[
     "controlling or influencing domestic political debates to maintain or increase their own power",
     "improving domestic economic conditions",
     "responding to domestic demands",
     "extending national influence regionally and internationally",
     "experimenting with policies on private ownership"], ans=0,
   why="EK IEF-3.B.3.c states that governments respond to global market forces in order to control or influence domestic political debates to maintain or increase their own power, which is the only one of the four purposes stated in terms of the government's own position."),
 dict(q="Which of the framework's stated purposes looks outward beyond the country's borders?",
   choices=[
     "extending national influence regionally and internationally",
     "improving domestic economic conditions",
     "responding to domestic demands",
     "controlling domestic political debates",
     "allowing private control of natural resources"], ans=0,
   why="EK IEF-3.B.3.d states that governments respond to global market forces in order to extend national influence regionally and internationally, and it is the only one of the four purposes directed outside the country."),
 dict(q="Which comparison of the framework's Mexican and Russian examples is accurate?",
   choices=[
     "One admitted private investment and competitors into an oil industry, while the other returned oil and gas firms to state ownership and restricted foreign investment",
     "Both admitted private investment into their oil industries",
     "Both returned their energy industries to state ownership",
     "One abolished its national oil company and the other created one",
     "Neither country's energy policy is described by the framework"], ans=0,
   why="EK IEF-3.B.1.b names privatization and increased competition in Mexico's oil industry while EK IEF-3.B.1.d names the re-nationalization of oil and natural gas industries and the imposition of foreign investment limitations in Russia, so the two experiments run in opposite directions."),
 dict(q="Which comparison of the framework's Chinese and Russian examples is accurate?",
   choices=[
     "One created zones on its coast where foreign investment is admitted on special terms, while the other imposed limits on foreign investment",
     "Both created coastal zones open to foreign investment",
     "Both imposed limits on foreign investment",
     "One privatized its energy industry and the other created special economic zones",
     "Neither has changed its treatment of foreign investment"], ans=0,
   why="EK IEF-3.B.1.a names special economic zones along the coast of China and EK IEF-3.B.1.d names the imposition of foreign investment limitations in Russia, so one example widens the opening to foreign capital and the other narrows it."),
 dict(q="Which comparison of the framework's Nigerian and Mexican examples is accurate?",
   choices=[
     "In one the national petroleum corporation remains state-owned while working with foreign firms, whereas in the other private investment and competitors were admitted into the oil industry itself",
     "Both fully privatized their national oil companies",
     "Both kept their oil industries closed to foreign participation",
     "Both re-nationalized their oil industries",
     "Neither allows foreign firms any role in oil production"], ans=0,
   why="EK IEF-3.B.1.c keeps Nigeria's corporation state-owned while it collaborates with foreign companies in joint ventures, and EK IEF-3.B.1.b records privatization and increased competition in Mexico's oil industry, so foreign participation without a transfer of ownership is different from opening the industry to private owners."),
 dict(q="Taken together, what do the four examples in EK IEF-3.B.1 show about the direction of policy on private ownership across the course countries?",
   choices=[
     "there is no single direction: some measures widen private and foreign participation while at least one reverses it",
     "every course country has moved steadily toward private ownership",
     "every course country has moved steadily away from private ownership",
     "no course country has changed its policy on private ownership",
     "policy on private ownership is set by international financial organizations rather than by governments"], ans=0,
   why="EK IEF-3.B.1 introduces its examples with the verb experiment, and the four it gives include coastal zones open to foreign investment and privatization on one side and re-nationalization with foreign investment limitations on the other."),
 dict(q="A government facing pressure from world markets adopts a measure and its ministers argue for it chiefly in terms of quieting criticism and keeping the governing party's position secure. Which of the framework's purposes does this match?",
   choices=[
     "controlling or influencing domestic political debates to maintain or increase their own power",
     "improving domestic economic conditions",
     "responding to domestic demands",
     "extending national influence regionally and internationally",
     "allowing varying degrees of private control of natural resources"], ans=0,
   why="EK IEF-3.B.3.c states that governments respond to global market forces in order to control or influence domestic political debates to maintain or increase their own power, and an argument pitched at criticism and the government's own security is that purpose stated openly."),
 dict(q="A government designates several coastal districts in which foreign firms may invest under terms available nowhere else in the country. Which framework example does this match?",
   choices=[
     "special economic zones along a coast",
     "the re-nationalization of energy industries",
     "joint ventures between a state corporation and foreign firms",
     "privatization of a national oil company",
     "the imposition of limits on foreign investment"], ans=0,
   why="EK IEF-3.B.1.a names special economic zones along the coast of China among the experiments with policies regarding private ownership of industry and capital, and a coastal district with investment terms unavailable elsewhere is what such a zone is."),
 dict(q="A government takes energy firms that had passed into private hands back under state ownership and caps the stake foreign investors may hold. Which framework example does this match?",
   choices=[
     "re-nationalization of oil and natural gas industries together with foreign investment limitations",
     "privatization and increased competition in an oil industry",
     "special economic zones opened along a coast",
     "a state corporation entering joint ventures with foreign firms",
     "the removal of all restrictions on private ownership"], ans=0,
   why="EK IEF-3.B.1.d names the re-nationalization of oil and natural gas industries and the imposition of foreign investment limitations as a single example, and the scenario contains both halves of it."),
 dict(q="A national petroleum corporation signs agreements under which foreign companies help extract and produce oil, while the corporation itself remains owned by the state. Which framework example does this match?",
   choices=[
     "a state-owned petroleum corporation collaborating with foreign companies in joint ventures",
     "the privatization of a national oil company",
     "the re-nationalization of an energy industry",
     "the creation of coastal special economic zones",
     "a prohibition on foreign participation in oil production"], ans=0,
   why="EK IEF-3.B.1.c describes Nigeria's state-owned Nigerian National Petroleum Corporation collaborating with foreign companies in joint ventures to extract and produce oil, which keeps ownership with the state while admitting foreign participation."),
 dict(q="How is EK IEF-3.B.2 best understood?",
   choices=[
     "as a spectrum whose two ends the framework names, with the other course countries lying somewhere between them",
     "as a division of the course countries into two groups of three",
     "as a claim that all six course countries treat natural resources alike",
     "as a ranking of all six course countries from first to sixth",
     "as a claim that no country allows any private control of natural resources"], ans=0,
   why="EK IEF-3.B.2 states that course countries allow varying degrees of private control of natural resources and names only the two extremes, the United Kingdom allowing the most and China the least, so it fixes endpoints rather than a full ordering."),
 dict(q="Which finding would most strongly support a claim that a government's response to global market forces was aimed at extending its influence beyond its own borders?",
   choices=[
     "The measures were introduced alongside new energy supply agreements with neighboring states and a bid for a larger role in a regional organization",
     "The measures were introduced after a domestic petition campaign",
     "The measures were justified by ministers as a way to reduce unemployment at home",
     "The measures were accompanied by restrictions on domestic media coverage of the debate",
     "The measures reduced the number of state-owned firms"], ans=0,
   why="EK IEF-3.B.3.d states that governments respond to global market forces in order to extend national influence regionally and internationally, so the supporting evidence has to point outside the country, while the rejected findings point to EK IEF-3.B.3.b, EK IEF-3.B.3.a and EK IEF-3.B.3.c instead."),
 dict(q="The table gives hypothetical figures on private ownership in four countries' resource sectors. Which row sits at the end of the framework's spectrum where private control of natural resources is greatest?",
   table=_T_SPECTRUM,
   choices=[
     "Country A, where privately owned firms produce 91 percent of resource output and no limits are placed on foreign investment",
     "Country B, where privately owned firms produce 62 percent of resource output",
     "Country C, where extensive limits are placed on foreign investment",
     "Country D, where privately owned firms produce 4 percent of resource output",
     "None of them, since degrees of private control cannot be compared"], ans=0,
   why="EK IEF-3.B.2 states that course countries allow varying degrees of private control of natural resources, with one end of the spectrum allowing the most, and the matching row shows both the largest private share and no restriction on foreign capital."),
 dict(q="Using the same table, which row sits at the opposite end of that spectrum?",
   table=_T_SPECTRUM,
   choices=[
     "Country D, where privately owned firms produce only 4 percent of resource output and foreign investment is extensively limited",
     "Country C, where privately owned firms produce 28 percent of resource output",
     "Country B, where some limits are placed on foreign investment",
     "Country A, where no limits are placed on foreign investment",
     "None of them, since every country in the table allows some private production"], ans=0,
   why="EK IEF-3.B.2 names an end of its spectrum at which the least private control of natural resources is allowed, and the matching row combines the smallest private share with extensive limits on foreign investment."),
 dict(q="According to the same table, the gap between the largest and smallest shares of resource output produced by privately owned firms is",
   table=_T_SPECTRUM,
   choices=[
     "87 percentage points",
     "63 percentage points",
     "34 percentage points",
     "24 percentage points",
     "91 percentage points"], ans=0,
   why="Subtracting the smallest figure in that column from the largest gives the gap. The alternatives are the gaps between other pairs in the same column and the largest single figure read as though it were a gap."),
 dict(q="The table describes four hypothetical policy episodes. Which one corresponds to the framework's Chinese example?",
   table=_T_EPISODE,
   choices=[
     "the episode in which designated coastal areas were opened to foreign investment on special terms",
     "the episode in which private investment was admitted into the national oil company",
     "the episode in which a state petroleum corporation entered joint ventures with foreign firms",
     "the episode in which energy firms were returned to state ownership",
     "none of the four, since the framework gives no example for that country"], ans=0,
   why="EK IEF-3.B.1.a names special economic zones along the coast of China, and only one episode describes designated coastal areas opened to foreign investment on terms unavailable elsewhere."),
 dict(q="Using the same table of episodes, which one corresponds to the framework's Mexican example?",
   table=_T_EPISODE,
   choices=[
     "the episode in which private investment was allowed into the national oil company and competitors were admitted to the industry",
     "the episode in which coastal areas were opened to foreign investment",
     "the episode in which a state petroleum corporation kept its ownership while working with foreign firms",
     "the episode in which oil and gas firms were returned to state ownership",
     "none of the four, since the framework gives no example for that country"], ans=0,
   why="EK IEF-3.B.1.b names privatization and increased competition in Mexico's oil industry, so the matching episode has to show both private investment entering the national company and competitors entering the industry."),
 dict(q="Using the same table of episodes, which one corresponds to the framework's Nigerian example?",
   table=_T_EPISODE,
   choices=[
     "the episode in which the national petroleum corporation stayed in state hands while entering joint ventures with foreign firms",
     "the episode in which coastal areas were opened to foreign investment",
     "the episode in which private investment was admitted into the national oil company",
     "the episode in which energy firms were returned to state ownership",
     "none of the four, since the framework gives no example for that country"], ans=0,
   why="EK IEF-3.B.1.c states that Nigeria's state-owned Nigerian National Petroleum Corporation collaborates with foreign companies in joint ventures to extract and produce oil, so the matching episode keeps state ownership and adds foreign partners."),
 dict(q="Using the same table of episodes, which one runs in the opposite direction from the other three?",
   table=_T_EPISODE,
   choices=[
     "the episode in which oil and natural gas firms were returned to state ownership and limits were imposed on foreign investment",
     "the episode in which coastal areas were opened to foreign investment on special terms",
     "the episode in which private investment was allowed into a national oil company",
     "the episode in which a state corporation entered joint ventures with foreign firms",
     "none of them, since all four widen private participation"], ans=0,
   why="EK IEF-3.B.1's other three examples each admit private or foreign participation, while EK IEF-3.B.1.d withdraws it, which is why the framework describes the course countries as experimenting rather than converging."),
 dict(q="The table gives four hypothetical statements of a government's reasons for a policy. Which one matches the framework's purpose concerning the government's own power?",
   table=_T_MOTIVE,
   choices=[
     "the statement about shaping how the measure is argued about at home and securing the government's own position",
     "the statement about raising output and employment at home",
     "the statement about answering petitions from citizens and associations",
     "the statement about increasing the country's weight in its region and beyond",
     "none of the four, since the framework gives no such purpose"], ans=0,
   why="EK IEF-3.B.3.c states that governments respond to global market forces in order to control or influence domestic political debates to maintain or increase their own power, and only one statement in the table names both the debate and the government's own position."),
 dict(q="Using the same table of statements, which one matches the framework's purpose of responding to domestic demands?",
   table=_T_MOTIVE,
   choices=[
     "the statement about answering petitions submitted by citizens and associations",
     "the statement about raising output and employment at home",
     "the statement about shaping how the measure is argued about at home",
     "the statement about increasing the country's weight beyond its borders",
     "none of the four, since the framework gives no such purpose"], ans=0,
   why="EK IEF-3.B.3.b states that governments respond to global market forces in order to respond to domestic demands, and a statement about answering petitions from citizens and associations is a demand arriving from the public rather than an economic aim or a matter of the government's standing."),
 dict(q="Taking EK IEF-3.B as a whole, which summary is most accurate?",
   choices=[
     "Course countries keep experimenting with private ownership of industry and capital, some opening and at least one closing, they allow different degrees of private control over natural resources, and their reasons range from economic conditions and public demands to the government's own power and its standing abroad",
     "Course countries have converged on a single policy toward private ownership",
     "Course countries respond to market forces only for economic reasons",
     "Course countries all allow the same degree of private control over natural resources",
     "Course countries no longer make their own decisions about private ownership"], ans=0,
   why="EK IEF-3.B.1 supplies the four experiments running in different directions, EK IEF-3.B.2 the spectrum of private control over natural resources with its two named ends, and EK IEF-3.B.3 the four purposes, two economic or public and two about power and standing."),
]
