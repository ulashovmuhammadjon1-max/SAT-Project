# AP COMPARATIVE GOVERNMENT AND POLITICS 3.1 Civil Society
# CED effective Fall 2026, Unit 3 Political Culture and Participation. Enduring
# understanding IEF-1 (political culture, including core beliefs and values that
# address the tension between order and liberty, shapes the relationship between a
# state and its citizens); learning objectives IEF-1.A and IEF-1.B. Suggested
# skill 1.E, Concept Application.
#
# Essential knowledge relied on:
#   IEF-1.A.1  CIVIL SOCIETY comprises a range of VOLUNTARY ASSOCIATIONS that are
#              AUTONOMOUS FROM THE STATE, including LOCAL RELIGIOUS AND
#              NEIGHBORHOOD ORGANIZATIONS, NEWS MEDIA, BUSINESS AND PROFESSIONAL
#              ASSOCIATIONS, and NONGOVERNMENTAL ORGANIZATIONS
#   IEF-1.A.2  the STRENGTH AND VARIETY of civil society organizations DIFFERS
#              DEPENDING ON THE REGIME TYPE in which they operate; they can be
#              LIMITED BY GOVERNMENT REGISTRATION AND MONITORING POLICIES
#   IEF-1.B.1  though civil society organizations are NOT NECESSARILY POLITICAL, a
#              ROBUST CIVIL SOCIETY SERVES AS AN AGENT OF DEMOCRATIZATION
#   IEF-1.B.2  across the course countries, civil society organizations, TO VARYING
#              DEGREES, can MONITOR AND LOBBY THE GOVERNMENT, EXPOSE GOVERNMENTAL
#              MALFEASANCE, REPRESENT THE INTERESTS OF MEMBERS, and PROVIDE MEMBERS
#              WITH ORGANIZATIONAL EXPERIENCE
#   IEF-1.B.3  across course countries, the placing of RESTRICTIONS ON NGOs AND
#              CIVIL SOCIETY TENDS TO HIGHLIGHT VIOLATIONS OF CIVIL LIBERTIES
#              protected under foundational documents
#
# Supporting statements, named in the verifier's claims where used:
#   LEG-1.C.3  reform pressure from citizen protest groups and CIVIL SOCIETY can
#              create new institutions or policies protecting civil liberties,
#              improving transparency, addressing election fairness and media bias,
#              limiting corruption and ensuring equality under law
#   DEM-1.C.2  both regime types constrain the media, democratic ones tolerating a
#              high degree of media freedom
#   PAU-1.C.1  democratization's aims
#
# THE DEFINING PROPERTY IS AUTONOMY FROM THE STATE. A state ministry, a state-owned
# broadcaster and a governing party's own organization are therefore NOT civil
# society however many members they have, and items 2, 4, 19 and 26 turn on that.
# The second half of IEF-1.B.1 is the one students drop: civil society is NOT
# NECESSARILY POLITICAL, and item 8 keys that rather than the democratization
# clause everyone remembers.
#
# Table figures are HYPOTHETICAL and labelled so.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md.
TOPIC = ("3.1", "Civil Society", 3)

_T_CS = dict(
    headers=["Country (hypothetical)", "Registered nongovernmental organizations per 100,000 people",
             "Share of such organizations reporting government monitoring of their finances (percent)",
             "Applications for registration refused in the past year (percent)"],
    rows=[["Country 1", "84", "12", "3"],
          ["Country 2", "9", "91", "64"],
          ["Country 3", "41", "38", "19"]])

_T_ACT = dict(
    headers=["Type of association (hypothetical sample)", "Number of organizations",
             "Number that published a report on government spending in the past year"],
    rows=[["Local religious and neighborhood organizations", "410", "12"],
          ["Business and professional associations", "180", "58"],
          ["News media organizations", "95", "71"],
          ["Nongovernmental organizations", "260", "142"]])

QUESTIONS = [
 dict(q="How does the framework define civil society?",
   choices=[
     "a range of voluntary associations that are autonomous from the state",
     "the set of institutions legally empowered to make binding decisions for a state",
     "the political parties permitted to contest elections",
     "the agencies through which a government implements policy",
     "the electorate considered as a whole"], ans=0,
   why="EK IEF-1.A.1 defines civil society as a range of voluntary associations that are autonomous from the state. The rejected options describe EK PAU-1.A.4's government, party systems, executive agencies and the electorate, none of which is autonomous from the state in the required sense."),
 dict(q="Which property does the framework treat as essential to an organization's being part of civil society?",
   choices=[
     "being autonomous from the state",
     "having a formal political programme",
     "being registered with a national ministry",
     "having more members than any political party",
     "receiving public funding"], ans=0,
   why="EK IEF-1.A.1 makes autonomy from the state definitive, and EK IEF-1.B.1 adds that such organizations are not necessarily political. Registration, size and funding bear on how a civil society organization operates rather than on whether it is one."),
 dict(q="Which set of organizations does the framework name as examples of civil society?",
   choices=[
     "local religious and neighborhood organizations, news media, business and professional associations, and nongovernmental organizations",
     "government ministries, state broadcasters, and the civil service",
     "political parties, electoral commissions, and legislatures",
     "courts, prosecutors, and police forces",
     "supranational organizations and foreign embassies"], ans=0,
   why="EK IEF-1.A.1 names exactly these four kinds of association. Each is voluntary and autonomous from the state, which is what the definition requires; ministries, commissions, courts and foreign bodies are not."),
 dict(q="Which of the following would NOT count as part of civil society on the framework's definition?",
   choices=[
     "a ministry of information that runs the state's broadcasting service",
     "a neighborhood association that organizes local services",
     "a professional association of engineers",
     "an independent newspaper",
     "a nongovernmental organization that reports on prison conditions"], ans=0,
   why="EK IEF-1.A.1 requires voluntary associations AUTONOMOUS FROM THE STATE, and a ministry running a state broadcaster is part of the state itself. The other four are among the kinds of association the same statement names."),
 dict(q="What does the framework say about how civil society varies across regimes?",
   choices=[
     "the strength and variety of civil society organizations differs depending on the regime type in which they operate",
     "civil society organizations are equally strong in every regime type",
     "civil society organizations exist only in democratic regimes",
     "civil society organizations exist only in authoritarian regimes",
     "the framework does not compare civil society across regime types"], ans=0,
   why="EK IEF-1.A.2 states that the strength and variety of civil society organizations differs depending on the regime type in which they operate. The framework describes a difference of degree rather than presence and absence, matching its treatment of media and participation at EK DEM-1.C.2 and EK DEM-1.B.3."),
 dict(q="By what means does the framework say civil society organizations can be limited?",
   choices=[
     "government registration and monitoring policies",
     "a requirement that they hold elections for their own officers",
     "the number of political parties in the legislature",
     "the territorial structure of the state",
     "the length of the head of government's term"], ans=0,
   why="EK IEF-1.A.2 states that civil society organizations can be limited by government registration and monitoring policies. Registration decides who may exist and monitoring decides what they may do unobserved, which is why the framework names both."),
 dict(q="What role does the framework assign to a robust civil society?",
   choices=[
     "it serves as an agent of democratization",
     "it replaces the legislature in making law",
     "it guarantees that the governing party will lose the next election",
     "it removes the need for civil liberties protections",
     "it transfers sovereignty from the state to voluntary associations"], ans=0,
   why="EK IEF-1.B.1 states that though civil society organizations are not necessarily political, a robust civil society serves as an agent of democratization. EK PAU-1.C.1 defines democratization as a transition from an authoritarian to a democratic regime, which is what such organizations are said to advance."),
 dict(q="Which qualification does the framework attach to its claim about civil society and democratization?",
   choices=[
     "civil society organizations are not necessarily political",
     "civil society organizations must be registered with the state",
     "civil society organizations must contest elections",
     "civil society organizations must be funded by their members alone",
     "civil society organizations exist only where democratization has already succeeded"], ans=0,
   why="EK IEF-1.B.1 opens by stating that civil society organizations are not necessarily political before saying that a robust civil society serves as an agent of democratization. A choir, a trade association and a neighborhood group can all belong to civil society without any political programme."),
 dict(q="Which set of activities does the framework attribute to civil society organizations across the course countries?",
   choices=[
     "monitoring and lobbying the government, exposing governmental malfeasance, representing the interests of members, and providing members with organizational experience",
     "nominating candidates for public office and forming governments",
     "certifying election results and registering political parties",
     "collecting taxes and enforcing regulations",
     "appointing judges and confirming ministers"], ans=0,
   why="EK IEF-1.B.2 names exactly these four, adding that civil society organizations can perform them TO VARYING DEGREES across the course countries. Nominating candidates and forming governments belong to parties, and the rest are state functions."),
 dict(q="An association publishes an analysis of a draft regulation and meets ministers to argue for changes. Which of the framework's civil society functions does this illustrate?",
   choices=[
     "monitoring and lobbying the government",
     "exposing governmental malfeasance",
     "representing the interests of members in disputes with employers",
     "providing members with organizational experience",
     "nominating candidates for public office"], ans=0,
   why="EK IEF-1.B.2 names monitoring and lobbying the government among the functions civil society organizations can perform. Analysis is the monitoring half and argument to ministers the lobbying half; the rejected options are other functions on the same list or a party function."),
 dict(q="A nongovernmental organization documents and publicizes the diversion of public funds by officials. Which of the framework's civil society functions does this illustrate?",
   choices=[
     "exposing governmental malfeasance",
     "representing the interests of members",
     "providing members with organizational experience",
     "monitoring and lobbying the government about a draft regulation",
     "certifying the results of an election"], ans=0,
   why="EK IEF-1.B.2 names exposing governmental malfeasance among the functions of civil society organizations, and EK LEG-1.C.3 describes reform pressure from civil society producing institutions that limit corruption. Publicizing diversion of funds is that exposure."),
 dict(q="A professional association negotiates on behalf of its members over the terms on which they may practise. Which of the framework's civil society functions does this illustrate?",
   choices=[
     "representing the interests of members",
     "exposing governmental malfeasance",
     "providing members with organizational experience",
     "monitoring and lobbying the government about corruption",
     "serving as an agent of democratization by contesting elections"], ans=0,
   why="EK IEF-1.B.2 names representing the interests of members among the functions of civil society organizations, and EK IEF-1.A.1 lists business and professional associations among the kinds of body that make up civil society."),
 dict(q="Members of a neighborhood association learn to run meetings, keep accounts and organize campaigns. Which of the framework's civil society functions does this illustrate?",
   choices=[
     "providing members with organizational experience",
     "exposing governmental malfeasance",
     "representing the interests of members before the courts",
     "monitoring and lobbying the government about spending",
     "nominating candidates for local office"], ans=0,
   why="EK IEF-1.B.2 names providing members with organizational experience among the functions of civil society organizations, and EK IEF-1.B.1's claim that a robust civil society serves as an agent of democratization rests partly on skills of this kind spreading beyond the association."),
 dict(q="What qualification does the framework attach to its list of civil society functions across the course countries?",
   choices=[
     "civil society organizations can perform them to varying degrees",
     "every civil society organization performs all four in every country",
     "no civil society organization performs any of them in an authoritarian regime",
     "the functions are performed only by organizations the state has registered",
     "the functions are performed only in federal states"], ans=0,
   why="EK IEF-1.B.2 states that across the course countries, civil society organizations can perform these functions TO VARYING DEGREES. EK IEF-1.A.2's point that strength and variety differ by regime type is why the qualification is there."),
 dict(q="What does the framework say tends to follow when restrictions are placed on NGOs and civil society?",
   choices=[
     "such restrictions tend to highlight violations of civil liberties protected under foundational documents",
     "such restrictions tend to increase the number of NGOs",
     "such restrictions tend to have no observable effect",
     "such restrictions tend to be imposed only by democratic regimes",
     "such restrictions tend to transfer NGO functions to political parties"], ans=0,
   why="EK IEF-1.B.3 states that across course countries, the placing of restrictions on NGOs and civil society tends to highlight violations of civil liberties protected under foundational documents. The restriction draws attention to the protection it cuts against."),
 dict(q="How does the framework connect civil society to institutional change?",
   choices=[
     "internal reform pressure from citizen protest groups and civil society can lead to new institutions or policies protecting civil liberties, improving transparency, addressing election fairness and media bias, limiting corruption, and ensuring equality under law",
     "civil society organizations draft and enact legislation themselves",
     "civil society organizations appoint the members of new institutions",
     "civil society has no bearing on the creation of institutions",
     "civil society organizations replace political parties in forming governments"], ans=0,
   why="EK LEG-1.C.3 states exactly this, and EK IEF-1.B.1's description of a robust civil society as an agent of democratization is the same claim stated more generally. Civil society applies pressure; the state creates the institution."),
 dict(q="Which comparison of civil society under democratic and authoritarian regimes is consistent with the framework?",
   choices=[
     "Civil society organizations exist under both, but their strength and variety differ with regime type and they can be limited by registration and monitoring policies",
     "Civil society organizations exist only under democratic regimes",
     "Civil society organizations are equally strong and various under both",
     "Civil society organizations are stronger under authoritarian regimes because the state supports them",
     "Civil society organizations are indistinguishable from state agencies under both"], ans=0,
   why="EK IEF-1.A.2 states that the strength and variety of civil society organizations differs depending on the regime type in which they operate and that they can be limited by government registration and monitoring policies. This matches EK DEM-1.C.2's and EK DEM-1.B.3's pattern of difference in degree rather than in presence."),
 dict(q="A state requires every association to re-register annually, refuses registration to groups whose stated aims it disapproves of, and audits the accounts of those it permits. Which framework claim does this most directly illustrate?",
   choices=[
     "that civil society organizations can be limited by government registration and monitoring policies",
     "that civil society organizations are not necessarily political",
     "that a robust civil society serves as an agent of democratization",
     "that civil society organizations represent the interests of their members",
     "that civil society comprises voluntary associations autonomous from the state"], ans=0,
   why="EK IEF-1.A.2 names government registration and monitoring policies as the means by which civil society organizations can be limited, and the scenario describes both. EK IEF-1.B.3 adds that such restrictions tend to highlight violations of civil liberties protected under foundational documents."),
 dict(q="A state-owned broadcaster and an independently owned newspaper both report on politics. Which is part of civil society on the framework's definition, and why?",
   choices=[
     "the independently owned newspaper, because civil society requires autonomy from the state",
     "the state-owned broadcaster, because it reaches more people",
     "both, because both report on politics",
     "neither, because news media are not part of civil society",
     "both, because both are registered with the state"], ans=0,
   why="EK IEF-1.A.1 names news media among the components of civil society but defines the whole category by autonomy from the state, which an outlet the state owns does not have. EK DEM-1.C.3.c describes the nationalization of most broadcast media as a way of tightening political control."),
 dict(q="The table reports hypothetical figures on nongovernmental organizations in three countries. Which country's civil society appears most limited by the means the framework names?",
   table=_T_CS,
   choices=[
     "Country 2, which has the fewest such organizations, the highest share reporting financial monitoring, and the highest share of registrations refused",
     "Country 1, which has the most such organizations",
     "Country 3, which is second on every measure",
     "None of the three, since registration policies cannot limit civil society",
     "All three equally, since each refuses some registrations"], ans=0,
   why="EK IEF-1.A.2 names government registration and monitoring policies as the means by which civil society organizations can be limited, and the table's three columns report exactly the count of organizations, the extent of monitoring and the refusal of registrations. One row is worst on all three."),
 dict(q="Using the same table, which country's civil society appears most robust on the framework's terms?",
   table=_T_CS,
   choices=[
     "Country 1, which has the most such organizations, the least financial monitoring, and the fewest registrations refused",
     "Country 2, which reports the most monitoring",
     "Country 3, which is between the other two on every measure",
     "None of the three, since robustness cannot be observed in data",
     "Both Country 1 and Country 3, since neither refuses most registrations"], ans=0,
   why="EK IEF-1.B.1 speaks of a ROBUST civil society serving as an agent of democratization, and EK IEF-1.A.2 makes registration and monitoring the constraints on it. One row leads on the count of organizations and is lowest on both constraints at once."),
 dict(q="According to the same table, the total number of registered nongovernmental organizations per 100,000 people across the three countries is",
   table=_T_CS,
   choices=[
     "134",
     "125",
     "93",
     "50",
     "84"], ans=0,
   why="Adding the first numeric column across the three rows gives the total. The alternatives arise from dropping the smallest row, from omitting the largest, from adding the two smaller rows, and from reading the largest single row as though it were the total."),
 dict(q="The table reports a hypothetical sample of associations by type. Which type published a report on government spending in the largest SHARE of its organizations?",
   table=_T_ACT,
   choices=[
     "news media organizations, with 71 of 95",
     "nongovernmental organizations, with 142 of 260",
     "business and professional associations, with 58 of 180",
     "local religious and neighborhood organizations, with 12 of 410",
     "the table does not report how many organizations of each type published such a report"], ans=0,
   why="EK IEF-1.B.2 names monitoring the government among the functions of civil society organizations, and the question asks for a proportion rather than a count. One row's share is the largest even though another row published more reports in absolute terms."),
 dict(q="According to the same table, the total number of organizations in the sample is",
   table=_T_ACT,
   choices=[
     "945",
     "283",
     "535",
     "670",
     "410"], ans=0,
   why="Adding the column of organization counts across all four rows gives the total. The alternatives arise from adding the other column instead, from dropping one or two rows, and from reading the largest single row as though it were the total."),
 dict(q="Which conclusion does the same table best support?",
   table=_T_ACT,
   choices=[
     "Every type of association listed belongs to civil society as the framework defines it, and each performed some government monitoring, though at very different rates",
     "Only nongovernmental organizations belong to civil society, and only they monitored government spending",
     "No type of association in the table performed any government monitoring",
     "Every organization in the sample published a report on government spending",
     "News media organizations are not part of civil society, so their reports do not count"], ans=0,
   why="EK IEF-1.A.1 names local religious and neighborhood organizations, news media, business and professional associations, and nongovernmental organizations as the components of civil society, and every row of the table is one of those four. EK IEF-1.B.2's 'to varying degrees' is what the differing rates illustrate."),
 dict(q="Which comparison of civil society organizations and political parties is consistent with the framework?",
   choices=[
     "Civil society organizations are voluntary associations autonomous from the state and are not necessarily political, whereas parties exist to contest elections and control governing power",
     "Civil society organizations and political parties are two names for the same kind of body",
     "Civil society organizations contest elections and parties do not",
     "Political parties are autonomous from the state and civil society organizations are not",
     "Neither civil society organizations nor political parties are permitted in authoritarian regimes"], ans=0,
   why="EK IEF-1.A.1 defines civil society by voluntary association and autonomy from the state and EK IEF-1.B.1 adds that such organizations are not necessarily political, while EK PAU-4.A.1 and EK PAU-4.A.2 describe party systems in terms of controlling governing power. EK PAU-4.A.2 also shows parties existing under an authoritarian regime."),
 dict(q="Which finding would most strongly support a claim that a country's civil society is robust in the framework's sense?",
   choices=[
     "Independent associations of many kinds operate without needing the state's approval, publish criticism of officials, and represent their members in dealings with government",
     "The state funds a large number of associations and appoints their officers",
     "A single national association exists for each profession, established by statute",
     "Associations are numerous but all are registered branches of the governing party",
     "The state broadcasts a weekly programme about community organizations"], ans=0,
   why="EK IEF-1.A.1 requires autonomy from the state, EK IEF-1.A.2 names registration and monitoring as the limits on it, and EK IEF-1.B.2 lists monitoring, exposure and representation among the functions. The rejected findings all describe bodies created, funded, staffed or owned by the state or the governing party."),
 dict(q="Which framework claim best explains why a regime that restricts NGOs may draw more criticism as a result?",
   choices=[
     "that placing restrictions on NGOs and civil society tends to highlight violations of civil liberties protected under foundational documents",
     "that civil society organizations are not necessarily political",
     "that civil society comprises voluntary associations autonomous from the state",
     "that a robust civil society serves as an agent of democratization",
     "that civil society organizations provide members with organizational experience"], ans=0,
   why="EK IEF-1.B.3 states that across course countries, restrictions on NGOs and civil society tend to highlight violations of civil liberties protected under foundational documents. The other statements are true of the framework but do not explain why a restriction draws attention to itself."),
 dict(q="Why does the framework count business and professional associations as part of civil society even when they take no position on any political question?",
   choices=[
     "because civil society is defined by voluntary association and autonomy from the state rather than by political purpose",
     "because every business association endorses a political party in practice",
     "because the state requires them to register and therefore regulates them",
     "because they are the only associations permitted in authoritarian regimes",
     "because they are funded from public money"], ans=0,
   why="EK IEF-1.A.1 names business and professional associations among the components of civil society and defines the category by voluntary association and autonomy from the state, while EK IEF-1.B.1 states that civil society organizations are not necessarily political."),
 dict(q="Taking the framework's statements on civil society together, which summary is most accurate?",
   choices=[
     "Civil society is the set of voluntary associations autonomous from the state; its strength varies with regime type and can be limited by registration and monitoring; and though not necessarily political, a robust civil society advances democratization and performs four named functions to varying degrees",
     "Civil society is the set of state agencies that consult the public, and its strength is the same in every regime",
     "Civil society consists only of political organizations, and it exists only in democracies",
     "Civil society is another name for the electorate, and it has no functions the framework names",
     "Civil society exists only where the state has registered and funded it"], ans=0,
   why="EK IEF-1.A.1 supplies the definition and the examples, EK IEF-1.A.2 the variation by regime type and the registration and monitoring limits, EK IEF-1.B.1 the not-necessarily-political qualification and the democratization claim, and EK IEF-1.B.2 the four functions performed to varying degrees."),
]
