# AP COMPARATIVE GOVERNMENT AND POLITICS 1.3 Democracy vs. Authoritarianism
# CED effective Fall 2026, Unit 1 Political Systems, Regimes, and Governments.
# Enduring understanding PAU-1; learning objective PAU-1.B (describe democracy
# and authoritarianism). Suggested skill 2.A, Country Comparison.
#
# Essential knowledge relied on:
#   PAU-1.B.1  factors indicating the degree of democracy or authoritarianism
#              include the extent of state adherence to RULE OF LAW, such as:
#     .a the principle that a state should be governed by law and not arbitrary
#        decisions made by individual government officials
#     .b the degree of state influence on or control of the media
#     .c the degree and practice of free and fair elections
#     .d the degree of transparency of governmental decision making
#     .e the nature of citizen participation in government
#   PAU-1.B.2  the branches of national government in democratic regimes are more
#              likely to be independent of one another than in authoritarian
#              regimes; independence can prevent any one branch from controlling
#              all governmental power
#   PAU-1.B.3  authoritarian regimes include illiberal democracies or hybrid
#              regimes, one-party states, theocracies, totalitarian governments,
#              and military regimes
#
# Supporting statements cited where a country appears:
#   PAU-1.D.1b Iran's transition from dictatorial rule to a theocracy based on
#              Islamic Sharia law after the 1979 Revolution
#   PAU-2.A.1  unitary states: China, Iran, the United Kingdom
#   PAU-4.A.2  China allows only the Communist Party of China to control governing
#              power while allowing eight other parties to exist to broaden
#              discussion and consultation
#   DEM-1.C.2  BOTH democratic and authoritarian regimes constrain the media to
#              protect citizens and maintain order; democratic regimes generally
#              tolerate a high degree of media freedom to encourage citizen
#              control of the political agenda and check power and corruption
#   DEM-1.C.3  stronger authoritarian regimes restrict media access further:
#              a China's Great Firewall, b Iranian courts suspending or revoking
#              media licences on a jury finding, c Russia's nationalization of
#              most broadcast media
#   DEM-1.C.4  a government is transparent when information about government and
#              policy making circulates openly; authoritarian regimes tend to
#              prefer secret or closed proceedings to maximize order
#   DEM-1.C.5  Russia is characterized as a competitive authoritarian regime or
#              illiberal democracy, holding contested elections with limited
#              competitiveness and minimal civil liberty protections and
#              governmental transparency
#   DEM-1.C.6  comparing data on civil liberties protection over time can
#              determine regime placement on an authoritarian/democratic scale
#   MPA-1.A.3  causation cannot be isolated and demonstrated with certainty
#
# No item asks a student to classify China or Iran as parliamentary,
# presidential or semi-presidential: PAU-3.A assigns those labels only to the
# United Kingdom, Mexico, Nigeria and Russia (see AP_COMP_GOV_CED.md note 2).
# Table figures are HYPOTHETICAL and the stems say so, because the framework
# prints no index values for any country.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md.
TOPIC = ("1.3", "Democracy vs. Authoritarianism", 1)

_T_ROL = dict(
    headers=["Country (hypothetical)", "Adherence to rule of law (0-10)",
             "State control of media (0 = none, 10 = total)",
             "Elections judged free and fair (0-10)",
             "Transparency of decision making (0-10)"],
    rows=[["Country P", "8.4", "1.2", "8.9", "7.6"],
          ["Country Q", "6.1", "3.5", "6.4", "5.2"],
          ["Country R", "3.2", "7.8", "3.9", "2.8"],
          ["Country S", "1.5", "9.1", "1.1", "1.4"]])

_T_MEDIA = dict(
    headers=["Country (hypothetical)", "Share of broadcast outlets under state ownership, 2010",
             "Share of broadcast outlets under state ownership, 2020"],
    rows=[["Country T", "18 percent", "22 percent"],
          ["Country U", "46 percent", "71 percent"],
          ["Country V", "9 percent", "8 percent"]])

QUESTIONS = [
 dict(q="A country publishes its statutes and its courts apply them consistently in most disputes, but a single cabinet minister grants and withdraws commercial licences by personal decision, without reference to any published standard. Which indicator of a regime's place on the democratic-authoritarian scale does this practice most directly bear on?",
   choices=[
     "whether the state is governed by law rather than by arbitrary decisions of individual officials",
     "the degree of state influence on or control of the media",
     "the nature of citizen participation in government",
     "whether the state distributes power to regional governments",
     "whether the state's economy is growing"], ans=0,
   why="EK PAU-1.B.1.a names as a rule-of-law indicator the principle that a state should be governed by law and not by arbitrary decisions made by individual government officials, which is exactly what an unreviewable ministerial licensing power defeats."),
 dict(q="Two states hold national elections on the same fixed schedule. In the first, opposition parties campaign without hindrance, broadcasters carry criticism of the government, and results are published constituency by constituency. In the second, a state body removes most opposition candidates before the ballot is printed and results are announced only as national totals. The framework locates the difference between them in",
   choices=[
     "the degree and practice of free and fair elections, which is not settled by the fact that elections occur",
     "whether elections are held at all, since only one of the two states holds them",
     "whether each state has a written constitution",
     "whether each state is federal or unitary",
     "the number of citizens eligible to vote in each state"], ans=0,
   why="EK PAU-1.B.1.c makes the indicator the degree AND practice of free and fair elections, not their occurrence. EK DEM-1.C.5 describes exactly this gap in competitive authoritarian regimes, which hold contested elections with limited degrees of competitiveness."),
 dict(q="The framework says the branches of national government in democratic regimes are more likely to be independent of one another than in authoritarian regimes. The purpose it attaches to that independence is that it",
   choices=[
     "can prevent any one branch from controlling all governmental power",
     "guarantees that policy will be made more quickly than under a unified government",
     "ensures that the members of every branch are directly elected",
     "removes the need for a written constitution",
     "requires that the state adopt a federal division of power"], ans=0,
   why="EK PAU-1.B.2 states that independence among branches can serve to prevent any one branch from controlling all governmental power. Speed, direct election, constitutional form and federalism are separate questions the framework treats elsewhere."),
 dict(q="Which set of regime types does the framework group together as authoritarian?",
   choices=[
     "illiberal democracies or hybrid regimes, one-party states, theocracies, totalitarian governments, and military regimes",
     "parliamentary systems, presidential systems, and semi-presidential systems",
     "federal states and unitary states",
     "consolidated democracies and democratizing states",
     "multiparty republics and coalition governments"], ans=0,
   why="EK PAU-1.B.3 lists these five kinds under the heading of authoritarian regimes. Executive-legislative type, territorial structure, stage of democratization and party arithmetic are separate classifications that cut across the democratic-authoritarian one."),
 dict(q="The framework describes Iran's 1979 Revolution as a transition of power from dictatorial rule to",
   choices=[
     "a theocracy based on Islamic Sharia law",
     "a one-party state governed by a single legal party",
     "a multiparty republic following military rule",
     "a managed democracy with election rules favoring one party",
     "a parliamentary system in which the legislature selects the executive"], ans=0,
   why="EK PAU-1.D.1.b states the transition of power from dictatorial rule in Iran to a theocracy based on Islamic Sharia law after the 1979 Revolution, and EK PAU-1.B.3 places theocracy among the authoritarian regime types. The rejected descriptions are the framework's words about Nigeria, Mexico and Russia."),
 dict(q="China allows eight parties other than the Communist Party of China to exist. The framework explains this arrangement as",
   choices=[
     "a way to broaden discussion and consultation while only one party retains control of governing power",
     "a multiparty system in which any of the nine parties may form a government after an election",
     "a proportional representation system that allocates seats to each party by vote share",
     "a hybrid arrangement in which contested elections decide which party governs",
     "a federal division of authority in which each party governs a different region"], ans=0,
   why="EK PAU-4.A.2 states that China's rules allow only the Communist Party of China to control governing power, to maintain the values of centralism and order, while allowing eight other parties to exist to broaden discussion and consultation. The permitted parties do not compete for control."),
 dict(q="The framework characterizes Russia as a competitive authoritarian regime or illiberal democracy. The combination of features it names in support of that characterization is",
   choices=[
     "contested elections held with limited degrees of competitiveness, alongside minimal protection of civil liberties and minimal governmental transparency",
     "no elections at all, combined with rule by a council of military officers",
     "fully competitive elections combined with weak protection of civil liberties",
     "contested elections combined with strong protection of civil liberties and open decision making",
     "rule by religious authorities under a legal code drawn from scripture"], ans=0,
   why="EK DEM-1.C.5 states that Russia is characterized as a competitive authoritarian regime or illiberal democracy, holding contested elections but with limited degrees of competitiveness and providing minimal civil liberty protections and governmental transparency. Elections happen and are contested, which is why the label is hybrid rather than simply authoritarian."),
 dict(q="A student writes that constraints on the media are found only in authoritarian regimes. Which framework statement most directly corrects this?",
   choices=[
     "Both democratic and authoritarian regimes impose constraints on the media, though democratic regimes generally tolerate a high degree of media freedom",
     "Media constraints are found only in regimes that are also one-party states",
     "Democratic regimes place no constraints on the media of any kind",
     "Authoritarian regimes place no constraints on the media because they control it already",
     "Media constraints exist only where a state owns every broadcast outlet"], ans=0,
   why="EK DEM-1.C.2 states that both democratic and authoritarian regimes impose constraints on the media to protect citizens and maintain order, and that democratic regimes generally tolerate a high degree of media freedom. The difference the framework draws is one of degree, not of presence and absence."),
 dict(q="According to the framework, democratic regimes tolerate a high degree of media freedom in order to",
   choices=[
     "encourage citizen control of the political agenda and check political power and corruption",
     "increase the state's share of broadcast ownership over time",
     "guarantee that every political party receives equal airtime by law",
     "reduce the number of parties competing in national elections",
     "remove the need for courts to review government decisions"], ans=0,
   why="EK DEM-1.C.2 gives exactly this reason: media freedom is tolerated to encourage citizen control of the political agenda and to check political power and corruption. The purpose is a check on government, not a distribution of airtime."),
 dict(q="China's Great Firewall and Russia's nationalization of most broadcast media are alike in that the framework presents both as ways in which a stronger authoritarian regime",
   choices=[
     "monitors and restricts citizens' media access to a greater degree in order to maintain political control",
     "delegates media regulation to an independent commission",
     "guarantees minority-language broadcasting across the country",
     "widens the range of political viewpoints available to citizens",
     "transfers ownership of broadcast outlets to regional governments"], ans=0,
   why="EK DEM-1.C.3 introduces both examples with the statement that stronger authoritarian regimes monitor and restrict citizens' media access to a greater degree to maintain political control, naming the Great Firewall's limits on political criticism and Russia's nationalization of most broadcast media with rigid controls on opposition news segments."),
 dict(q="Which of the following does the framework give as its example of media restriction in Iran?",
   choices=[
     "courts suspending or revoking media licences after a jury finds owners guilty of publishing anti-religious material or material detrimental to the national interest",
     "a national firewall filtering political criticism from social media platforms",
     "state ownership of most broadcast outlets combined with controls on opposition news segments",
     "a licensing commission appointed jointly by the head of state and an independent body",
     "a constitutional ban on all privately owned newspapers"], ans=0,
   why="EK DEM-1.C.3.b describes the Iranian court's suspension or revocation of media licences when a jury finds owners guilty of publishing anti-religious material or information detrimental to the national interest. The firewall example is China's and the broadcast nationalization is Russia's."),
 dict(q="In the framework's terms, a government is transparent when",
   choices=[
     "information about government and policy making is allowed to circulate openly",
     "its elections are contested by more than one party",
     "its constitution has been approved by a national referendum",
     "its branches are independent of one another",
     "its courts may strike down laws passed by the legislature"], ans=0,
   why="EK DEM-1.C.4 defines transparency as a government allowing information about government and policy making to circulate openly. Contested elections, constitutional ratification, branch independence and judicial review are separate indicators the framework lists elsewhere."),
 dict(q="The framework states that authoritarian regimes tend to prefer secret or closed proceedings. The reason it gives is that closed proceedings",
   choices=[
     "maximize order",
     "reduce the cost of administering government",
     "satisfy the requirements of a written constitution",
     "increase the number of parties represented in the legislature",
     "make the judiciary independent of the executive"], ans=0,
   why="EK DEM-1.C.4 states that authoritarian regimes tend to prefer secret or closed proceedings to maximize order, which is the framework's own account of the motive. Cost, constitutional compliance, party representation and judicial independence are not offered as reasons for closure."),
 dict(q="In one country a constitutional court has annulled several executive decrees and the executive has complied; in a second, the court has never ruled against the executive and its members serve at the executive's pleasure. This contrast speaks most directly to which framework claim?",
   choices=[
     "that branches of national government are more likely to be independent of one another in democratic than in authoritarian regimes",
     "that authoritarian regimes include theocracies and military regimes",
     "that both democratic and authoritarian regimes constrain the media",
     "that democratization aims at universal suffrage for adult citizens",
     "that unitary states concentrate power at the national level"], ans=0,
   why="EK PAU-1.B.2 is the claim about relative independence of branches, and a court whose members serve at the executive's pleasure and has never ruled against it is the framework's picture of the dependent case. The other four statements are true of the framework but bear on different indicators."),
 dict(q="The United Kingdom and China are both classified by the framework as unitary states, yet they sit at opposite ends of the democratic-authoritarian scale. This pairing shows that",
   choices=[
     "a regime's place on that scale is judged by rule of law, elections, media conditions, transparency and participation rather than by whether power is territorially concentrated",
     "unitary structure is evidence of authoritarianism in every case",
     "federal structure is a requirement of democracy in the framework",
     "the framework treats territorial structure and regime type as the same classification",
     "a unitary state cannot hold free and fair elections"], ans=0,
   why="EK PAU-2.A.1 lists China, Iran and the United Kingdom as unitary while EK PAU-1.B.1 supplies an entirely separate set of indicators for the democratic-authoritarian scale. Two states can therefore share a territorial structure and diverge sharply on the scale, which is why one classification cannot be read off the other."),
 dict(q="The table reports hypothetical scores on four indicators the framework names. Which conclusion does the table support?",
   table=_T_ROL,
   choices=[
     "The country with the highest state control of media also holds the lowest scores on rule of law, on free and fair elections, and on transparency.",
     "Every country scores higher on transparency of decision making than on adherence to rule of law.",
     "The two countries with the least state control of media hold the two lowest election scores.",
     "Adherence to rule of law and state control of media rise together across the four countries.",
     "All four countries score above 5 on at least three of the four measures."], ans=0,
   why="Reading down the columns, the country scoring highest for state control of media is also last on each of the other three indicators, so the pattern is consistent across every measure in the table rather than resting on one of them."),
 dict(q="Ordering the four countries in the table from the most to the least democratic on the indicators shown gives",
   table=_T_ROL,
   choices=[
     "Country P, then Country Q, then Country R, then Country S",
     "Country S, then Country R, then Country Q, then Country P",
     "Country Q, then Country P, then Country S, then Country R",
     "Country P, then Country R, then Country Q, then Country S",
     "No ordering is possible, because the four indicators disagree with one another"], ans=0,
   why="Three of the four columns are higher the more democratic the country and the media column is higher the less democratic it is, so the ordering must be read with that column inverted. Once it is, all four indicators place the countries in the same sequence."),
 dict(q="A student reads the same table and concludes that heavy state control of the media causes weak adherence to the rule of law. The strongest objection to that conclusion is that",
   table=_T_ROL,
   choices=[
     "the table shows the two measures moving together but contains nothing that isolates which of them produces the other",
     "the table contains no information about media at all",
     "an association of this kind establishes causation only in authoritarian regimes",
     "the four countries are too similar to one another for any comparison to be drawn",
     "adherence to the rule of law is not something that can be measured"], ans=0,
   why="EK MPA-1.A.3 states that numerous variables potentially influence political outcomes with no way to isolate and demonstrate which is producing the change, and EK MPA-1.A.4 calls an observed co-movement an association. Four paired observations fit the reverse account and a third-variable account equally well."),
 dict(q="The table reports hypothetical state ownership of broadcast outlets in three countries. Whose change over the decade is most consistent with the framework's description of a regime tightening its control of the media?",
   table=_T_MEDIA,
   choices=[
     "Country U, whose state-owned share rose by 25 percentage points",
     "Country T, whose state-owned share rose by 4 percentage points",
     "Country V, whose state-owned share fell by 1 percentage point",
     "None of the three, because no share was above half at the start of the period",
     "All three equally, because each share changed over the period"], ans=0,
   why="EK DEM-1.C.3.c presents nationalization of broadcast media as the mechanism of tighter control, so the country whose state-owned share grows by far the most over the decade is the one the description fits. A four-point rise and a one-point fall are not comparable movements."),
 dict(q="According to the same table, the only country in which the state owned a majority of broadcast outlets in 2020 was",
   table=_T_MEDIA,
   choices=[
     "Country U, at 71 percent",
     "Country U, at 46 percent",
     "Country T, at 22 percent",
     "Country V, at 8 percent",
     "none of the three, since no share reached half"], ans=0,
   why="A majority requires more than half of the outlets, and only one figure in the final column clears that line. The lower figure offered for the same country is its value at the start of the period rather than at the end."),
 dict(q="The framework says that comparing data on how far governments protect or restrict civil liberties over time can be used to",
   choices=[
     "determine a regime's placement on an authoritarian-democratic scale",
     "predict the date of a regime's next election",
     "establish which branch of government holds the most power",
     "measure the size of a country's economy",
     "identify whether a state is federal or unitary"], ans=0,
   why="EK DEM-1.C.6 states that comparing data showing the extent to which governments protect or restrict civil liberties over time can determine regime placement on an authoritarian/democratic scale. The framework treats the scale as a matter of degree, which is why data over time can locate a regime on it."),
 dict(q="Competitive authoritarian regimes are best described in the framework's terms as",
   choices=[
     "hybrids that combine democratic and authoritarian features in a single regime",
     "democracies whose branches of government are unusually independent",
     "regimes in which no elections of any kind are held",
     "regimes governed by religious authorities under a scriptural legal code",
     "regimes in which a council of military officers exercises lawmaking power"], ans=0,
   why="EK DEM-1.C.5 states that competitive authoritarian regimes act as a hybrid of democratic and authoritarian regimes. The listed alternatives describe a consolidated democracy, a closed authoritarian regime, a theocracy and a military regime, each of which EK PAU-1.B.3 treats as a distinct type."),
 dict(q="In one country, senior officers suspend the constitution, dissolve the legislature and rule by decree through a council of commanders. Which of the authoritarian regime types named by the framework does this most clearly illustrate?",
   choices=[
     "a military regime",
     "a theocracy",
     "an illiberal democracy",
     "a one-party state",
     "a totalitarian government defined by its control of the economy"], ans=0,
   why="EK PAU-1.B.3 names military regimes among the authoritarian types, and rule by a council of commanders after the suspension of the constitution is the clearest case of one. A theocracy rests on religious authority and an illiberal democracy still holds contested elections."),
 dict(q="Which comparison correctly distinguishes a theocracy from a one-party state as the framework uses the two terms?",
   choices=[
     "In a theocracy the claim to rule rests on religious authority and law drawn from scripture, whereas in a one-party state it rests on the exclusive governing role of a single legal party",
     "In a theocracy a single legal party governs, whereas in a one-party state religious authorities interpret the law",
     "A theocracy holds contested elections whereas a one-party state holds none of any kind",
     "A theocracy is a democratic regime type whereas a one-party state is an authoritarian one",
     "The two terms describe the same arrangement under different names"], ans=0,
   why="EK PAU-1.B.3 lists both among authoritarian regime types, and the framework's own illustrations separate them: EK PAU-1.D.1.b describes Iran's theocracy resting on Islamic Sharia law while EK PAU-4.A.2 describes China's rules reserving governing power to one legal party."),
 dict(q="Which finding would most strongly support a claim that a country's elections fall short of the framework's standard of free and fair elections?",
   choices=[
     "An unelected state body disqualified most opposition candidates before voting began",
     "Turnout at the most recent election was lower than at the previous one",
     "The governing party won a larger share of seats than of votes",
     "The election was held later in the year than the one before it",
     "Several small parties chose not to contest the election"], ans=0,
   why="EK PAU-1.B.1.c makes the degree and practice of free and fair elections the indicator, and EK DEM-2.B.4.a treats the exclusion of candidates by a vetting body as the clearest restriction of electoral competition. Turnout, a seat bonus produced by the counting rule, a shifted date and voluntary abstention are all consistent with a free contest."),
 dict(q="A regime permits citizens to vote in regular elections but prohibits independent candidacies, requires official approval for public demonstrations, and bars unregistered associations. Under the framework's fifth rule-of-law indicator, this regime differs from a democratic one in",
   choices=[
     "the kinds of participation it permits rather than in whether participation exists at all",
     "the absence of any citizen participation whatsoever",
     "the size of the electorate entitled to take part",
     "whether it holds elections at fixed intervals",
     "whether its executive and legislature are separately chosen"], ans=0,
   why="EK PAU-1.B.1.e names the nature of citizen participation in government as the indicator, which is a question about what forms participation may take. EK DEM-1.B.3 adds that both regime types regulate formal participation, authoritarian regimes simply to a much greater extent, so presence and absence is the wrong axis."),
 dict(q="Two states both hold multiparty elections. In the first, budget negotiations are published and ministers answer questions in public session; in the second, the same decisions are taken in closed meetings whose records are not released. On the framework's indicators, the second state scores lower on",
   choices=[
     "the transparency of governmental decision making",
     "the degree and practice of free and fair elections",
     "the nature of citizen participation in government",
     "the independence of its branches of government",
     "the extent of its territorial decentralization"], ans=0,
   why="EK PAU-1.B.1.d names the degree of transparency of governmental decision making as an indicator, and EK DEM-1.C.4 defines transparency as allowing information about government and policy making to circulate openly. Both states hold multiparty elections, so the electoral indicator does not separate them."),
 dict(q="A country's constitution grants its legislature the sole power to make law, but in practice the executive issues decrees with the force of law that the legislature has never rejected and the courts have never reviewed. A comparativist applying the framework would conclude that",
   choices=[
     "the branches are formally separate but not independent, since neither the legislature nor the courts constrains the executive in practice",
     "the branches must be independent, because the constitution says the legislature makes law",
     "the country cannot be evaluated, because the framework's indicators apply only to federal states",
     "the executive's decrees make the country a theocracy",
     "the arrangement is evidence that the country's elections are free and fair"], ans=0,
   why="EK PAU-1.B.2 concerns whether branches are in fact independent of one another and whether that independence prevents one branch from controlling all governmental power. A formal grant that no institution enforces leaves the executive exercising the legislature's power, which is the concentration the statement warns against."),
 dict(q="Which single change would move a regime furthest toward the authoritarian end of the framework's scale?",
   choices=[
     "Transferring editorial control of the main broadcasters to the executive and closing cabinet proceedings to the public",
     "Moving the date of a general election forward by three months",
     "Increasing the number of seats in the national legislature",
     "Adopting a new national flag and anthem",
     "Transferring responsibility for road maintenance from regional to national officials"], ans=0,
   why="EK PAU-1.B.1 makes state control of the media and the transparency of decision making two of its five indicators, so a change that worsens both moves a regime on two of the scale's own measures at once. An election date, a chamber's size, national symbols and the administrative level of road maintenance touch none of the five."),
 dict(q="An observer notes that a country holds genuinely contested elections, yet its journalists are prosecuted for criticism, its courts follow executive instruction, and most policy is made in unpublished sessions. Which of the framework's categories best fits this country?",
   choices=[
     "an illiberal democracy, since competitive elections coexist with minimal civil liberty protection and minimal transparency",
     "a consolidated democracy, since the elections are genuinely contested",
     "a totalitarian government, since the state controls the courts",
     "a military regime, since the executive dominates the other branches",
     "a unitary state, since policy is made centrally"], ans=0,
   why="EK PAU-1.B.3 lists illiberal democracies or hybrid regimes among the authoritarian types and EK DEM-1.C.5 describes exactly this combination, contested elections alongside minimal civil liberty protections and governmental transparency. The presence of real elections is what rules out the closed categories, and territorial structure is a different classification."),
]
