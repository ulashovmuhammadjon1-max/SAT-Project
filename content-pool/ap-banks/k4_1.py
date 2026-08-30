# AP COMPARATIVE GOVERNMENT AND POLITICS 4.1 Electoral Systems and Rules
# Unit 4, Party and Electoral Systems and Citizen Organizations (13-18% of the
# multiple-choice section). Enduring understanding DEM-2: the rules of electoral
# systems reflect party and legislative control and level of democratization.
# Learning objective DEM-2.A: describe electoral systems and election rules
# among course countries.
#
# Essential knowledge relied on, and nothing outside it:
#   DEM-2.A.1   in some regimes electoral rules allow competitive selection of
#               representatives, while in others rules are frequently changed to
#               advance different political interests
#     .a China   the National People's Congress selects members INDIRECTLY
#               through a series of local and regional elections
#     .b Iran    Majles members directly elected in single-member and
#               multimember districts, sometimes requiring a second round;
#               candidates vetted by the Guardian Council; the legislative body
#               lacks formal political party structures; a small number of the
#               290 seats are reserved for non-Muslim minorities (Christians,
#               Jews, Zoroastrians)
#     .c Mexico  Chamber of Deputies: 300 directly elected in single-member
#               districts by plurality plus 200 by proportional representation
#               party list; Chamber of Senators: 96 elected in three-seat
#               constituencies and 32 by proportional representation; gender
#               quotas in the party list system have helped increase female
#               representation
#     .d Nigeria House of Representatives directly elected in single-member
#               districts, the number from each state based on population size;
#               the Senate has three members directly elected from each of the
#               36 states; two major parties have alternated control of the
#               National Assembly
#     .e Russia  State Duma returned to a system with half the representatives
#               directly elected from single-member districts and half chosen
#               through proportional representation with a threshold
#     .f UK      House of Commons members directly elected under single-member
#               district, first-past-the-post rules
#   DEM-2.A.2   proportional representation relies on multimember districts that
#               promote multiparty systems
#
# Every arithmetic figure used in a table comes from those bullets (300/200,
# 96/32, 290, 36 states x 3 senators). Where a table needs vote totals the stem
# says the district is hypothetical, because the CED prints no election returns
# and inventing them would be presenting fiction as fact.
#
# FIVE choices (A-E), matching the real AP Comparative exam.
TOPIC = ("4.1", "Electoral Systems and Rules", 4)
QUESTIONS = [
 dict(q="Which of the following accurately compares how members of the United Kingdom's House of Commons and Mexico's Chamber of Deputies are elected?", choices=[
   "Every seat in the House of Commons is filled in a single-member district, whereas the Chamber of Deputies fills some seats in single-member districts and the rest from proportional representation party lists.",
   "Both chambers fill every seat from national party lists using proportional representation.",
   "The House of Commons uses proportional representation, while every seat in the Chamber of Deputies is won by plurality in a single-member district.",
   "Members of both chambers are chosen indirectly by regional assemblies rather than by voters.",
   "Members of both chambers are appointed by the head of government on the advice of an independent commission."], ans=0,
   why="EK DEM-2.A.1.f gives the Commons a pure single-member district, first-past-the-post system, while EK DEM-2.A.1.c gives the Chamber of Deputies a mixed system of 300 single-member district seats and 200 party-list seats, so the difference is that Mexico's chamber is mixed and the British one is not."),
 dict(q="Members of China's National People's Congress reach the national legislature by which route?", choices=[
   "They are selected indirectly through a series of local and regional elections.",
   "They are elected directly nationwide under first-past-the-post rules.",
   "They are elected from a single national party list using proportional representation with a threshold.",
   "They are nominated by the eight minor parties and confirmed by the head of state.",
   "They are chosen by lot from among members of provincial people's congresses."], ans=0,
   why="EK DEM-2.A.1.a states that the National People's Congress selects members indirectly through a series of local and regional elections, so no voter casts a ballot for a national deputy."),
 dict(q="Iran's Majles is elected in single-member and multimember districts, and its candidates are screened before they may appear on the ballot. Which of the following does this arrangement best illustrate?", choices=[
   "Direct election of a legislature can coexist with rules that restrict which candidates voters are permitted to choose among.",
   "A legislature elected in districts cannot also reserve seats for religious minorities.",
   "Multimember districts require that seats be distributed among competing political parties in proportion to their votes.",
   "A legislature whose candidates are screened must be selected indirectly rather than by voters.",
   "Screening candidates before an election guarantees that the winner holds an absolute majority of the national vote."], ans=0,
   why="EK DEM-2.A.1.b has Majles members directly elected in districts and also has their candidacies vetted by the Guardian Council, so direct election and restricted ballot access are present in the same system; the vetting limits the choice set rather than the method of election."),
 dict(table=dict(headers=["Method of election", "Seats"],
   rows=[["Single-member district plurality", "300"], ["Proportional representation party list", "200"]]),
   q="The table shows how the seats in Mexico's Chamber of Deputies are filled. According to the table, the share of the chamber chosen by proportional representation is", choices=[
   "20 percent",
   "30 percent",
   "40 percent",
   "50 percent",
   "60 percent"], ans=2,
   why="The table's two rows total 500 seats and 200 of them are party-list seats, so the proportional share is 200 divided by 500, or 40 percent; the figures are those of EK DEM-2.A.1.c."),
 dict(table=dict(headers=["Feature of Nigeria's Senate", "Number"],
   rows=[["States", "36"], ["Senators directly elected from each state", "3"]]),
   q="According to the table, the number of directly elected members of Nigeria's Senate is", choices=[
   "36",
   "39",
   "72",
   "108",
   "144"], ans=3,
   why="Three senators from each of 36 states is 108 members, and EK DEM-2.A.1.d specifies that the three are directly elected from each state, so the chamber's size follows from equal state representation rather than from population."),
 dict(q="Changes to State Duma elections in Russia returned the chamber to a system in which", choices=[
   "half the deputies are elected in single-member districts and half through proportional representation with a threshold",
   "all deputies are elected in single-member districts under first-past-the-post rules",
   "all deputies are elected from one national party list with no threshold",
   "deputies are appointed by regional governors and regional legislatures",
   "deputies are selected indirectly by a series of local and regional elections"], ans=0,
   why="EK DEM-2.A.1.e describes the restored mixed system: half the representatives directly elected from single-member districts, half chosen by proportional representation with a threshold. Appointment by regional bodies describes the Federation Council, not the Duma."),
 dict(q="Proportional representation tends to produce multiparty legislatures principally because", choices=[
   "it relies on multimember districts, so a party that finishes behind the leader can still win seats",
   "it requires every winning candidate to obtain an absolute majority of the votes cast",
   "it forbids parties from forming coalitions to nominate candidates",
   "it gives each district a single representative who is accountable to local voters",
   "it allows an electoral commission to add members to the legislature after the count"], ans=0,
   why="EK DEM-2.A.2 states that proportional representation relies on multimember districts that promote multiparty systems; because a district returns several members, finishing second or third still yields representation, which is exactly what a single-member plurality contest denies."),
 dict(q="Which of the following is an accurate difference between legislative elections in Iran and in the United Kingdom?", choices=[
   "Candidates for Iran's Majles are vetted by a religious body before the ballot is set, whereas candidates for the House of Commons face no comparable vetting body.",
   "Iran's Majles is filled entirely by proportional representation, whereas the House of Commons is filled in single-member districts.",
   "Members of the House of Commons are chosen indirectly by regional bodies, whereas Majles members are elected directly.",
   "Both chambers set aside seats for recognized religious minorities.",
   "Neither chamber's members are elected directly by voters."], ans=0,
   why="EK DEM-2.A.1.b names the Guardian Council's vetting of Majles candidates, and EK DEM-2.A.1.f describes the Commons as directly elected under first-past-the-post with no such screening body, so ballot access rather than the method of counting is where the two systems part."),
 dict(q="The United Kingdom fills the House of Commons through single-member district plurality contests. A recurring consequence of these rules is that", choices=[
   "minor parties win a smaller share of seats than their share of the national vote",
   "seats are allocated to each party in proportion to its national vote share",
   "minor parties are guaranteed seats once they cross a national threshold",
   "each district is represented by several members drawn from different parties",
   "a new election must be held whenever no party wins an absolute majority of votes"], ans=0,
   why="EK PAU-4.B.1.g states that single-member district plurality elections in the United Kingdom diminish minor-party representation: the leading candidate takes the whole district, so votes spread thinly across many districts convert into few seats."),
 dict(table=dict(headers=["Party", "Votes"],
   rows=[["Party W", "41,000"], ["Party X", "33,000"], ["Party Y", "18,000"], ["Party Z", "8,000"]]),
   q="The table shows the votes cast in one hypothetical single-member district. Under the rules used to elect the United Kingdom's House of Commons, which of the following describes the outcome?", choices=[
   "Party W takes the district's one seat with 41 percent of the votes cast, and the other 59 percent elect no one there.",
   "Party W and Party X divide the seat, because together they won a majority of the votes.",
   "Party Y receives a seat because it cleared the threshold required for list seats.",
   "No one is elected, because no candidate won an absolute majority, so a second round is held.",
   "Each party receives a share of the district's seats in proportion to the votes it won."], ans=0,
   why="The four parties polled 100,000 votes and Party W polled 41,000 of them, which is 41 percent; first-past-the-post awards the single seat to the leading candidate regardless of whether that is a majority, which is why 59 percent of this district's votes elect nobody."),
 dict(q="Mexico's Chamber of Senators is filled by", choices=[
   "election in three-seat constituencies together with an additional group of members chosen by proportional representation",
   "single-member district plurality contests alone",
   "appointment by the president from a list approved by the Chamber of Deputies",
   "indirect selection by the legislature of each state",
   "one national party list with no district contests at all"], ans=0,
   why="EK DEM-2.A.1.c gives the Chamber of Senators 96 members elected in three-seat constituencies and 32 elected by proportional representation, so it mixes multimember district contests with a list component."),
 dict(q="Gender quotas applied to Mexico's party lists are best understood as an electoral rule that", choices=[
   "constrains whom parties may nominate and has helped raise the number of women serving in the legislature",
   "reserves a fixed bloc of seats for recognized religious minorities",
   "requires a presidential candidate to win a quarter of the vote in two-thirds of the states",
   "prohibits parties from forming coalitions to nominate candidates",
   "replaces the proportional representation tier with additional single-member districts"], ans=0,
   why="EK DEM-2.A.1.c credits gender quotas in the party list system with helping to increase female representation in the legislature; a quota operates on the composition of the list, which is a rule about nomination rather than about counting votes."),
 dict(table=dict(headers=["Country", "Chamber", "How members are chosen"],
   rows=[["China", "National People's Congress", "Indirectly, through a series of local and regional elections"],
         ["Russia", "State Duma", "Half in single-member districts, half by proportional representation with a threshold"],
         ["United Kingdom", "House of Commons", "Directly, in single-member districts under first-past-the-post rules"]]),
   q="According to the table, which of the following conclusions is best supported?", choices=[
   "One of the three chambers is filled without any direct election of its members, and the other two are filled at least partly by direct election in districts.",
   "All three chambers fill at least some seats by proportional representation.",
   "Two of the three chambers are filled entirely by single-member district plurality contests.",
   "None of the three chambers uses single-member districts.",
   "Each of the three chambers applies a threshold to list seats."], ans=0,
   why="Exactly one row, China's, says the members are chosen indirectly, and the other two rows both name single-member districts, so the count in the table supports the first statement and refutes the claims that all three or none of the three use a given method."),
 dict(q="Seats in Nigeria's House of Representatives are distributed among the states according to", choices=[
   "population size, so a more populous state elects more representatives",
   "an equal allocation to every state, as in the Senate",
   "the number of registered political parties active in the state",
   "the share of the national vote each party wins, using list seats",
   "appointment by each state's governor"], ans=0,
   why="EK DEM-2.A.1.d states that the number of representatives elected from each state is based on population size, in contrast with the Senate, where each of the 36 states returns the same three members."),
 dict(q="Which of the following accurately compares the two chambers of Nigeria's National Assembly?", choices=[
   "Every state sends the same number of senators, whereas House seats are apportioned according to population.",
   "Every state sends the same number of representatives, whereas Senate seats are apportioned according to population.",
   "Both chambers apportion seats according to population.",
   "Both chambers give each state an identical number of members.",
   "Both chambers are filled by proportional representation from national party lists."], ans=0,
   why="EK DEM-2.A.1.d pairs three directly elected senators from each of the 36 states with House seats whose number per state is based on population size, so the Senate weights states equally and the House weights people."),
 dict(q="A regime rewrites its ballot access and party registration rules shortly before each national election, each time in ways that favor the governing party. This pattern is characteristic of systems in which", choices=[
   "election rules are changed frequently in order to advance particular political interests rather than to permit competitive selection of representatives",
   "an independent commission has insulated electoral administration from partisan control",
   "proportional representation guarantees minor parties a share of the seats",
   "the legislature is chosen indirectly rather than by voters",
   "candidates must be vetted for their religious qualifications before standing"], ans=0,
   why="EK DEM-2.A.1 draws exactly this contrast: in some regimes electoral rules are structured for the competitive selection of representatives, while in others rules are frequently changed to advance different political interests, and frequent self-serving revision is the mark of the second."),
 dict(q="Which pair fills every seat in the chamber named entirely through single-member district contests?", choices=[
   "The United Kingdom's House of Commons and Nigeria's House of Representatives",
   "Mexico's Chamber of Deputies and Russia's State Duma",
   "China's National People's Congress and Iran's Majles",
   "Russia's State Duma and Nigeria's Senate",
   "Iran's Majles and Mexico's Chamber of Senators"], ans=0,
   why="EK DEM-2.A.1.f and DEM-2.A.1.d put every Commons seat and every House of Representatives seat in a single-member district; Mexico's Deputies and Russia's Duma are mixed systems, Nigeria's Senate uses three-member states, Iran's Majles uses multimember districts as well as single-member ones, and China's congress is indirect."),
 dict(q="Mexico's Chamber of Deputies and Russia's State Duma resemble each other in that both", choices=[
   "combine single-member district seats with seats awarded by proportional representation",
   "are filled entirely from a single national party list",
   "reserve a bloc of seats for recognized religious minorities",
   "are selected indirectly by subnational legislatures",
   "give every subnational unit an identical number of members"], ans=0,
   why="EK DEM-2.A.1.c gives Mexico's lower chamber 300 district seats plus 200 list seats and EK DEM-2.A.1.e gives the Duma an equal split between district and list seats, so both are mixed systems even though the countries' regime types differ."),
 dict(q="The threshold applied to the proportional representation half of Russia's State Duma elections most directly determines", choices=[
   "whether a party whose vote share falls below the required level receives any list seats",
   "how many members each region sends to the Federation Council",
   "how many candidates an electoral vetting body may reject",
   "whether the president may appoint envoys to the federal districts",
   "how House seats are apportioned among states by population"], ans=0,
   why="EK DEM-2.A.1.e specifies proportional representation with a threshold, and a threshold is a minimum vote share below which a list receives nothing, so it operates on small parties' access to list seats and on nothing else in the list."),
 dict(q="Iran's Majles differs from Mexico's Congress of the Union in that Iran's legislative body", choices=[
   "lacks formal political party structures, so its members are not organized into competing parties within the chamber",
   "is chosen indirectly by provincial councils rather than by voters",
   "awards all of its seats through proportional representation",
   "is appointed in its entirety by the head of state",
   "sets aside half of its seats for women"], ans=0,
   why="EK DEM-2.A.1.b states that Iran's legislative body lacks formal political party structures, whereas EK PAU-4.B.1.c describes a Mexican multiparty system in which parties may even form coalitions to nominate candidates."),
 dict(table=dict(headers=["Chamber", "Seats filled in districts", "Seats filled by proportional representation"],
   rows=[["Chamber of Deputies", "300", "200"], ["Chamber of Senators", "96", "32"]]),
   q="According to the table, the total membership of Mexico's Congress of the Union is", choices=[
   "500",
   "596",
   "628",
   "632",
   "700"], ans=2,
   why="The Chamber of Deputies totals 300 plus 200, or 500 members, and the Chamber of Senators totals 96 plus 32, or 128, so the two chambers together seat 628 legislators."),
 dict(table=dict(headers=["Chamber", "Seats filled in districts", "Seats filled by proportional representation"],
   rows=[["Chamber of Deputies", "300", "200"], ["Chamber of Senators", "96", "32"]]),
   q="Using the same table, which chamber of Mexico's Congress of the Union relies more heavily on proportional representation, and by how much?", choices=[
   "The Chamber of Deputies, where 200 of 500 seats are filled by proportional representation, against 32 of 128 in the Chamber of Senators",
   "The Chamber of Senators, where 32 of 128 seats are filled by proportional representation, against 200 of 500 in the Chamber of Deputies",
   "The two chambers rely on proportional representation to exactly the same degree",
   "The Chamber of Deputies, because all 500 of its seats are filled from party lists",
   "The Chamber of Senators, because none of the Chamber of Deputies' seats come from party lists"], ans=0,
   why="Two hundred of the 500 deputies, or 40 percent, hold list seats, against 32 of the 128 senators, or 25 percent, so the lower chamber is the more proportional of the two, and neither chamber is filled wholly one way."),
 dict(q="Iran sets aside a small number of Majles seats for recognized non-Muslim minorities, and Mexico applies gender quotas to its party lists. Both rules are examples of", choices=[
   "electoral rules adopted to change which groups end up represented in the legislature",
   "rules that govern how the head of government is selected",
   "thresholds designed to reduce the number of parties in the legislature",
   "federal rules dividing authority between national and subnational governments",
   "measures that convert a directly elected chamber into an indirectly selected one"], ans=0,
   why="EK DEM-2.A.1.b reserves seats for Christians, Jews, and Zoroastrians and EK DEM-2.A.1.c credits gender quotas with raising female representation, and EK DEM-2.B.6 states the general point that election rule changes affect the representation of different religious, ethnic, and socioeconomic groups."),
 dict(q="The indirect selection of China's National People's Congress most directly limits", choices=[
   "the ability of ordinary voters to reward or remove a national legislator at the ballot box",
   "the number of political parties permitted to exist in the country",
   "the total number of members the legislature may seat",
   "the frequency with which the legislature is permitted to meet",
   "the use of districts of any kind in local elections"], ans=0,
   why="EK DEM-2.A.1.a routes selection through a series of local and regional elections, so the voters who choose a national deputy are themselves officeholders rather than the general electorate, and the direct electoral sanction disappears. The limit on parties in China comes from a separate rule, EK PAU-4.A.2, not from the method of selection."),
 dict(q="A country abandons single-member district plurality elections and adopts proportional representation in multimember districts. Based on the framework, the most likely consequence is", choices=[
   "an increase in the number of parties holding seats in the legislature",
   "a reduction in the number of parties, because votes concentrate on the leader in each district",
   "the abolition of districts, since proportional representation must be conducted nationwide",
   "a change from direct election of the legislature to indirect selection",
   "the replacement of the legislature's elected members with appointed members"], ans=0,
   why="EK DEM-2.A.2 states that proportional representation relies on multimember districts that promote multiparty systems, and EK DEM-2.B.2 states that single-member plurality tends to promote two-party systems, so moving from the second to the first should raise, not lower, the number of parties winning seats. Proportional representation does not abolish districts; it makes them larger."),
 dict(q="Which of the following accurately compares how China's National People's Congress and Russia's State Duma are filled?", choices=[
   "The National People's Congress is filled indirectly through lower-level elections, whereas half the State Duma is elected directly in single-member districts.",
   "Both chambers are filled indirectly by subnational legislatures.",
   "Both chambers are filled entirely by proportional representation with a threshold.",
   "The National People's Congress is elected directly in single-member districts, whereas the State Duma is chosen indirectly.",
   "The National People's Congress reserves seats for religious minorities, whereas the State Duma reserves seats for regional parties."], ans=0,
   why="EK DEM-2.A.1.a makes the Chinese congress indirect while EK DEM-2.A.1.e makes half the Duma directly elected from single-member districts, so the two authoritarian-leaning systems differ in whether voters choose national legislators at all."),
 dict(q="Why might a country choose multimember districts rather than single-member districts for its legislature?", choices=[
   "Because several representatives are returned from one district, groups that are not the largest in that district can still win representation there.",
   "Because a multimember district guarantees that the winning candidate holds an absolute majority of the district's votes.",
   "Because a multimember district ties each representative to one constituency and so strengthens constituency service.",
   "Because multimember districts raise the effective threshold and so reduce the number of parties.",
   "Because multimember districts allow the executive to appoint the members it prefers."], ans=0,
   why="EK DEM-2.A.2 links multimember districts to proportional representation and to multiparty systems; the mechanism is that a district returning several members can seat more than the leading party. The single representative per district and its strong constituency accountability belong to EK DEM-2.B.2, which describes the opposite design."),
 dict(q="Which statement about the national legislatures of the six course countries is accurate?", choices=[
   "Members of the United Kingdom's House of Commons and of Nigeria's House of Representatives are directly elected, whereas members of China's National People's Congress are selected indirectly.",
   "Members of every one of the six national legislatures are directly elected by voters.",
   "None of the six countries fills any legislative seat through proportional representation.",
   "Only the United Kingdom uses districts of any kind to fill its legislature.",
   "Every one of the six countries reserves legislative seats for religious minorities."], ans=0,
   why="EK DEM-2.A.1.f and DEM-2.A.1.d have both chambers named here directly elected in single-member districts, while EK DEM-2.A.1.a makes China's congress indirect; Mexico and Russia both use list seats, and only Iran, under EK DEM-2.A.1.b, reserves seats for religious minorities."),
 dict(q="Two major parties have alternated control of Nigeria's National Assembly. Considered alongside the rules for electing that legislature, this pattern is most consistent with the expectation that", choices=[
   "single-member district contests tend to concentrate legislative strength in a small number of parties",
   "proportional representation with a low threshold tends to fragment a legislature among many parties",
   "indirectly selected legislatures produce frequent turnover between parties",
   "reserved seats for minorities determine which party controls a legislature",
   "gender quotas determine which party controls a legislature"], ans=0,
   why="EK DEM-2.A.1.d records the alternation of two major parties in a chamber whose members are elected in single-member districts, and EK DEM-2.B.2 states that single-member district plurality systems tend to promote two-party systems, so the observed pattern matches the rule's predicted effect."),
 dict(q="A political scientist argues that a country's electoral rules reveal how far its regime has democratized. Which piece of evidence would best support that argument?", choices=[
   "A regime that screens candidates for ideological loyalty before they may stand produces legislatures with far less competition than a regime whose ballot access is administered by an independent commission.",
   "Two countries with the same electoral rules have legislatures of different sizes.",
   "A country's legislature meets more often than its neighbor's legislature does.",
   "A country's largest party has a longer official name than its rivals' names.",
   "Two countries hold their legislative elections in the same month of the year."], ans=0,
   why="EK DEM-2.A.1 ties the structure of electoral rules to whether representatives are competitively selected, and EK DEM-2.B.4 contrasts a vetting body that removes candidates with independent commissions created to enhance electoral competition, so the level of competition the rules permit is the evidence that bears on democratization; chamber size, sitting days, party names, and the calendar do not."),
]
