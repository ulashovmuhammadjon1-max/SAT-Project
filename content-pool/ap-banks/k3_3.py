# AP COMPARATIVE GOVERNMENT AND POLITICS 3.3 Political Ideologies
# CED effective Fall 2026, Unit 3 Political Culture and Participation. Enduring
# understanding IEF-1; learning objective IEF-1.C. Suggested skill 1.C, Concept
# Application.
#
# Essential knowledge relied on -- IEF-1.C.6, a POLITICAL IDEOLOGY is a set of
# values and beliefs about the GOALS OF GOVERNMENT, PUBLIC POLICY, OR POLITICS,
# represented by six named positions, each defined by the framework itself:
#   .a INDIVIDUALISM -- belief in INDIVIDUAL CIVIL LIBERTIES AND FREEDOM OVER
#      GOVERNMENTAL RESTRICTIONS
#   .b NEOLIBERALISM -- belief in LIMITED GOVERNMENTAL INTERVENTION IN THE ECONOMY
#      AND SOCIETY; supports PRIVATIZATION, FREE TRADE, DEREGULATION, and the
#      ELIMINATION OF STATE SUBSIDIES
#   .c COMMUNISM -- belief in the ABOLITION OF PRIVATE PROPERTY with NEAR TOTAL
#      GOVERNMENTAL CONTROL OF THE ECONOMY
#   .d SOCIALISM -- belief in the REDUCTION OF INCOME DISPARITIES and the
#      NATIONALIZATION OF MAJOR PRIVATE INDUSTRIES
#   .e FASCISM -- an EXTREME NATIONALIST ideology that favors AUTHORITARIAN RULE and
#      the RIGHTS OF THE ETHNIC MAJORITY over that of ETHNIC MINORITIES AND THE
#      POLITICAL OPPOSITION
#   .f POPULISM -- a political philosophy that supports the INTERESTS AND RIGHTS OF
#      THE COMMON PEOPLE OVER THAT OF THE ELITES
#
# THE PAIR MOST OFTEN COLLAPSED is communism and socialism. The framework separates
# them precisely: communism ABOLISHES private property and takes NEAR TOTAL control
# of the economy; socialism nationalizes MAJOR PRIVATE INDUSTRIES and reduces income
# disparities, which leaves private property in existence. Items 4, 5, 14 and 21
# depend on holding that line, and no item treats the two as interchangeable.
#
# WHAT NO ITEM DOES: assign an ideology from this list to a course country as a
# label. IEF-1.C.6 defines the six and attaches none of them to any of the six
# countries, so an item asking 'which ideology does country X hold' would have no
# defensible key. Country material appears only where another statement supplies it,
# such as PAU-4.A.2 on the values of centralism and order.
#
# Table cases are HYPOTHETICAL and labelled so.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md.
TOPIC = ("3.3", "Political Ideologies", 3)

_T_PLAT = dict(
    headers=["Party platform (hypothetical)", "Position on ownership of major industry",
             "Position on the distribution of income"],
    rows=[["Platform 1", "abolish private property and place the economy under near total government control",
           "eliminate private wealth altogether"],
          ["Platform 2", "nationalize major private industries while leaving smaller firms in private hands",
           "reduce income disparities substantially"],
          ["Platform 3", "privatize state-owned firms, end subsidies and deregulate",
           "leave distribution to markets"]])

_T_SUPP = dict(
    headers=["Position endorsed (hypothetical survey)", "Share of respondents in Country F (percent)",
             "Share of respondents in Country G (percent)"],
    rows=[["Individual civil liberties and freedom over governmental restrictions", "38", "19"],
          ["Limited governmental intervention in the economy and society", "22", "14"],
          ["Reduction of income disparities and nationalization of major industries", "17", "28"],
          ["The interests and rights of the common people over those of the elites", "23", "39"]])

QUESTIONS = [
 dict(q="How does the framework define a political ideology?",
   choices=[
     "a set of values and beliefs about the goals of government, public policy, or politics",
     "the collective attitudes, values and beliefs of an entire citizenry",
     "the fundamental rules controlling access to and the exercise of political power",
     "the lifelong process of acquiring beliefs about the political system",
     "a voluntary association autonomous from the state"], ans=0,
   why="EK IEF-1.C.6 defines a political ideology as a set of values and beliefs about the goals of government, public policy, or politics. The rejected options are EK IEF-1.C.1's political culture, EK PAU-1.A.2's regime, EK IEF-1.C.3's socialization and EK IEF-1.A.1's civil society."),
 dict(q="How does the framework define individualism?",
   choices=[
     "belief in individual civil liberties and freedom over governmental restrictions",
     "belief in limited governmental intervention in the economy and society",
     "belief in the abolition of private property",
     "belief in the reduction of income disparities through nationalization",
     "support for the interests of the common people over those of the elites"], ans=0,
   why="EK IEF-1.C.6.a defines individualism as belief in individual civil liberties and freedom over governmental restrictions. The rejected definitions are the framework's own for neoliberalism, communism, socialism and populism."),
 dict(q="How does the framework define neoliberalism?",
   choices=[
     "belief in limited governmental intervention in the economy and society, supporting privatization, free trade, deregulation and the elimination of state subsidies",
     "belief in individual civil liberties and freedom over governmental restrictions",
     "belief in the nationalization of major private industries",
     "an extreme nationalist ideology favoring authoritarian rule",
     "support for the rights of the common people over those of the elites"], ans=0,
   why="EK IEF-1.C.6.b defines neoliberalism as belief in limited governmental intervention in the economy and society, and names privatization, free trade, deregulation and the elimination of state subsidies as the policies it supports."),
 dict(q="How does the framework define communism?",
   choices=[
     "belief in the abolition of private property with near total governmental control of the economy",
     "belief in the reduction of income disparities and the nationalization of major private industries",
     "belief in limited governmental intervention in the economy and society",
     "belief in individual civil liberties over governmental restrictions",
     "an extreme nationalist ideology favoring the rights of the ethnic majority"], ans=0,
   why="EK IEF-1.C.6.c defines communism as belief in the abolition of private property with near total governmental control of the economy. The first rejected option is the framework's definition of socialism, which nationalizes major industries without abolishing private property."),
 dict(q="How does the framework define socialism?",
   choices=[
     "belief in the reduction of income disparities and the nationalization of major private industries",
     "belief in the abolition of private property with near total governmental control of the economy",
     "belief in limited governmental intervention in the economy and society",
     "belief in individual civil liberties over governmental restrictions",
     "support for the interests of the common people over those of the elites"], ans=0,
   why="EK IEF-1.C.6.d defines socialism as belief in the reduction of income disparities and the nationalization of major private industries. The first rejected option is the framework's definition of communism, which goes further by abolishing private property altogether."),
 dict(q="How does the framework define fascism?",
   choices=[
     "an extreme nationalist ideology that favors authoritarian rule and the rights of the ethnic majority over those of ethnic minorities and the political opposition",
     "a political philosophy supporting the interests of the common people over those of the elites",
     "belief in the abolition of private property",
     "belief in individual civil liberties over governmental restrictions",
     "belief in limited governmental intervention in the economy and society"], ans=0,
   why="EK IEF-1.C.6.e defines fascism as an extreme nationalist ideology that favors authoritarian rule and the rights of the ethnic majority over that of ethnic minorities and the political opposition. Both the ethnic and the opposition clauses are the framework's."),
 dict(q="How does the framework define populism?",
   choices=[
     "a political philosophy that supports the interests and rights of the common people over those of the elites",
     "an extreme nationalist ideology favoring authoritarian rule",
     "belief in the nationalization of major private industries",
     "belief in limited governmental intervention in the economy and society",
     "belief in the abolition of private property"], ans=0,
   why="EK IEF-1.C.6.f defines populism as a political philosophy that supports the interests and rights of the common people over that of the elites. The framework's definition turns on the contrast between common people and elites and says nothing about ownership of industry."),
 dict(q="A movement campaigns against restrictions on speech, assembly and personal conduct, arguing that individuals should decide such matters for themselves. Which of the framework's ideologies does this most closely match?",
   choices=[
     "individualism",
     "socialism",
     "communism",
     "fascism",
     "populism"], ans=0,
   why="EK IEF-1.C.6.a defines individualism as belief in individual civil liberties and freedom over governmental restrictions, which is exactly what the campaign asserts. The other five are defined by positions on ownership, distribution, nationhood or the common people."),
 dict(q="A government sells state-owned enterprises, removes tariffs, repeals regulations on business and ends subsidies to agriculture. Which of the framework's ideologies does this programme most closely match?",
   choices=[
     "neoliberalism",
     "socialism",
     "communism",
     "individualism",
     "fascism"], ans=0,
   why="EK IEF-1.C.6.b names privatization, free trade, deregulation and the elimination of state subsidies as the policies neoliberalism supports, and the programme in the item is all four. EK IEF-1.C.6.a's individualism concerns civil liberties rather than economic policy."),
 dict(q="A movement proposes to abolish private ownership of productive property and place the whole economy under governmental control. Which of the framework's ideologies does this most closely match?",
   choices=[
     "communism",
     "socialism",
     "neoliberalism",
     "populism",
     "individualism"], ans=0,
   why="EK IEF-1.C.6.c defines communism as belief in the abolition of private property with near total governmental control of the economy. EK IEF-1.C.6.d's socialism nationalizes major private industries and reduces income disparities without abolishing private property."),
 dict(q="A party proposes to take the largest banks and utilities into public ownership and to raise taxes on high incomes in order to narrow the gap between rich and poor, while leaving most businesses private. Which ideology does this most closely match?",
   choices=[
     "socialism",
     "communism",
     "neoliberalism",
     "fascism",
     "individualism"], ans=0,
   why="EK IEF-1.C.6.d defines socialism as belief in the reduction of income disparities and the nationalization of major private industries, and the programme does both while leaving most property private. That last feature is what distinguishes it from EK IEF-1.C.6.c's communism."),
 dict(q="A movement calls for rule by a single strong authority, asserts the primacy of one ethnic group, and treats opposition parties as enemies to be suppressed. Which ideology does this most closely match?",
   choices=[
     "fascism",
     "populism",
     "communism",
     "socialism",
     "individualism"], ans=0,
   why="EK IEF-1.C.6.e defines fascism as an extreme nationalist ideology favoring authoritarian rule and the rights of the ethnic majority over those of ethnic minorities and the political opposition. All three elements of the item appear in that definition."),
 dict(q="A movement presents politics as a contest between ordinary citizens and a self-serving establishment, and promises to govern for the first against the second. Which ideology does this most closely match?",
   choices=[
     "populism",
     "fascism",
     "neoliberalism",
     "communism",
     "individualism"], ans=0,
   why="EK IEF-1.C.6.f defines populism as a political philosophy supporting the interests and rights of the common people over those of the elites, which is the contrast the movement draws. Nothing in the framework's definition requires a position on ethnicity or on ownership."),
 dict(q="Which comparison of communism and socialism follows the framework's definitions?",
   choices=[
     "Communism calls for the abolition of private property and near total governmental control of the economy, whereas socialism nationalizes major private industries and reduces income disparities without abolishing private property",
     "Socialism calls for the abolition of private property, whereas communism nationalizes only major industries",
     "The two are defined identically by the framework",
     "Communism concerns civil liberties and socialism concerns ownership",
     "Neither takes any position on the ownership of industry"], ans=0,
   why="EK IEF-1.C.6.c and EK IEF-1.C.6.d are written so as to separate the two: abolition of private property and near total control on one side, nationalization of major private industries and reduced income disparities on the other. Reversing them contradicts both definitions."),
 dict(q="Which comparison of individualism and neoliberalism follows the framework's definitions?",
   choices=[
     "Individualism is defined by civil liberties and freedom against governmental restrictions, whereas neoliberalism is defined by limited governmental intervention in the economy and society",
     "Individualism is defined by economic policy and neoliberalism by civil liberties",
     "Both are defined by the nationalization of major industries",
     "Both are defined as extreme nationalist ideologies",
     "Neither takes any position on the role of government"], ans=0,
   why="EK IEF-1.C.6.a defines individualism in terms of individual civil liberties and freedom over governmental restrictions, and EK IEF-1.C.6.b defines neoliberalism in terms of limited governmental intervention in the economy and society with a named list of policies. Both limit government, in different domains."),
 dict(q="Which comparison of fascism and populism follows the framework's definitions?",
   choices=[
     "Fascism is defined as extreme nationalism favoring authoritarian rule and an ethnic majority, whereas populism is defined by support for the common people against the elites",
     "Populism is defined as extreme nationalism and fascism by support for the common people",
     "Both are defined by their position on the ownership of industry",
     "Both are defined as beliefs in limited governmental intervention in the economy",
     "The framework defines neither of them"], ans=0,
   why="EK IEF-1.C.6.e defines fascism as an extreme nationalist ideology favoring authoritarian rule and the rights of the ethnic majority over those of minorities and the opposition, while EK IEF-1.C.6.f defines populism by the common people against the elites. Neither definition mentions ownership of industry."),
 dict(q="Which of the framework's six ideologies is defined partly by its treatment of ethnic minorities and of the political opposition?",
   choices=[
     "fascism",
     "populism",
     "socialism",
     "neoliberalism",
     "individualism"], ans=0,
   why="EK IEF-1.C.6.e is the only one of the six whose definition names ethnic minorities and the political opposition, favoring the rights of the ethnic majority over both. The other five definitions concern liberties, economic intervention, property, distribution and the common people."),
 dict(q="Which of the framework's six ideologies is defined by a contrast between two groups within a society rather than by a position on the economy or on liberties?",
   choices=[
     "populism, defined by the common people against the elites",
     "neoliberalism, defined by limited governmental intervention",
     "communism, defined by the abolition of private property",
     "socialism, defined by nationalization and reduced income disparities",
     "individualism, defined by civil liberties over governmental restrictions"], ans=0,
   why="EK IEF-1.C.6.f defines populism as supporting the interests and rights of the common people over that of the elites, which is a claim about whose interests should prevail rather than about ownership or liberty. Each rejected option quotes the framework's definition of a different ideology accurately."),
 dict(q="Which comparison of socialism and neoliberalism on the state's economic role follows the framework's definitions?",
   choices=[
     "Socialism calls for nationalizing major private industries, whereas neoliberalism calls for privatization, deregulation and the elimination of state subsidies",
     "Socialism calls for privatization, whereas neoliberalism calls for nationalization",
     "Both call for the abolition of private property",
     "Both call for limited governmental intervention in the economy",
     "Neither takes a position on the state's economic role"], ans=0,
   why="EK IEF-1.C.6.d and EK IEF-1.C.6.b place the two at opposite ends of the same question: nationalization of major private industries against privatization, free trade, deregulation and the elimination of state subsidies."),
 dict(q="The table describes three hypothetical party platforms. Which one matches the framework's definition of communism?",
   table=_T_PLAT,
   choices=[
     "Platform 1, which would abolish private property and place the economy under near total government control",
     "Platform 2, which would nationalize major industries while leaving smaller firms private",
     "Platform 3, which would privatize state-owned firms and deregulate",
     "None of the three, since the framework does not define communism",
     "Both Platform 1 and Platform 2, since each would extend public ownership"], ans=0,
   why="EK IEF-1.C.6.c defines communism as belief in the abolition of private property with near total governmental control of the economy, and only one row states both. The row that leaves smaller firms private is EK IEF-1.C.6.d's socialism instead."),
 dict(q="Using the same table, which platform matches the framework's definition of socialism?",
   table=_T_PLAT,
   choices=[
     "Platform 2, which would nationalize major private industries and reduce income disparities while leaving smaller firms in private hands",
     "Platform 1, which would abolish private property",
     "Platform 3, which would leave distribution to markets",
     "None of the three, since socialism and communism are defined identically",
     "Both Platform 1 and Platform 2, since each would reduce private wealth"], ans=0,
   why="EK IEF-1.C.6.d defines socialism as belief in the reduction of income disparities and the nationalization of major private industries, which leaves private property in existence. EK IEF-1.C.6.c's communism abolishes it, so the two are not defined identically."),
 dict(q="Using the same table, which platform matches the framework's definition of neoliberalism?",
   table=_T_PLAT,
   choices=[
     "Platform 3, which would privatize state-owned firms, end subsidies and deregulate",
     "Platform 1, which would place the economy under near total government control",
     "Platform 2, which would nationalize major private industries",
     "None of the three, since neoliberalism concerns civil liberties rather than the economy",
     "Both Platform 2 and Platform 3, since each addresses ownership"], ans=0,
   why="EK IEF-1.C.6.b names privatization, free trade, deregulation and the elimination of state subsidies as the policies neoliberalism supports, and one row states three of the four. EK IEF-1.C.6.a's individualism, not neoliberalism, is the framework's civil liberties position."),
 dict(q="The table reports hypothetical survey figures for two countries. Support for which position rose most from the first country to the second?",
   table=_T_SUPP,
   choices=[
     "the interests and rights of the common people over those of the elites, by 16 percentage points",
     "the reduction of income disparities and nationalization of major industries, by 11 percentage points",
     "individual civil liberties and freedom over governmental restrictions, by 19 percentage points",
     "limited governmental intervention in the economy and society, by 8 percentage points",
     "no position rose between the two countries"], ans=0,
   why="Each row of the table states one of EK IEF-1.C.6's definitions, so the comparison is inside the framework's own list. Two rows rise and two fall between the columns, and taking the signed change identifies the largest rise; the largest absolute movement belongs to a row that falls."),
 dict(q="Using the same table, which country shows greater combined support for the two positions the framework associates with limiting what government does?",
   table=_T_SUPP,
   choices=[
     "Country F, whose two relevant shares total 60 percent against 33 percent",
     "Country G, whose two relevant shares total 60 percent against 33 percent",
     "Neither, since the two countries' totals are equal",
     "Country G, because its largest single share is bigger than any share in Country F",
     "Neither, since no position in the table concerns limiting government"], ans=0,
   why="EK IEF-1.C.6.a defines individualism as freedom over governmental restrictions and EK IEF-1.C.6.b defines neoliberalism as limited governmental intervention in the economy and society, so those two rows are the ones that limit government. Adding each country's shares on those rows separates them clearly."),
 dict(q="Using the same table, the position with the largest share in the second country corresponds to which of the framework's ideologies?",
   table=_T_SUPP,
   choices=[
     "populism",
     "individualism",
     "neoliberalism",
     "socialism",
     "communism"], ans=0,
   why="The leading row in that column states support for the interests and rights of the common people over those of the elites, which is EK IEF-1.C.6.f's definition of populism word for word. No row of the table states EK IEF-1.C.6.c's abolition of private property."),
 dict(q="A party platform promises to defend national traditions, restrict immigration on ethnic grounds, concentrate authority in a single leader, and outlaw rival parties. Which of the framework's ideologies does this most closely match, and why not populism?",
   choices=[
     "fascism, because the framework's definition of populism does not include authoritarian rule or the primacy of an ethnic majority",
     "populism, because the platform appeals to ordinary citizens",
     "communism, because the platform concentrates power",
     "socialism, because the platform is nationalist",
     "individualism, because the platform defends traditions"], ans=0,
   why="EK IEF-1.C.6.e's fascism is defined by extreme nationalism, authoritarian rule and the rights of the ethnic majority over those of minorities and the opposition, while EK IEF-1.C.6.f's populism is defined only by the common people against the elites. Outlawing rival parties and ranking ethnic groups belong to the first definition and not the second."),
 dict(q="A platform promises to protect freedom of expression and personal choice from government interference but takes no position on the ownership of industry. Which of the framework's ideologies does it most closely match?",
   choices=[
     "individualism",
     "neoliberalism",
     "socialism",
     "communism",
     "populism"], ans=0,
   why="EK IEF-1.C.6.a defines individualism as belief in individual civil liberties and freedom over governmental restrictions, and takes no position on the economy. EK IEF-1.C.6.b's neoliberalism is defined by limited governmental intervention in the economy and society, which the platform is silent on."),
 dict(q="Which two of the framework's six ideologies are defined by opposite answers to the same question about who should own major industry?",
   choices=[
     "neoliberalism and socialism",
     "individualism and populism",
     "fascism and populism",
     "individualism and fascism",
     "populism and socialism"], ans=0,
   why="EK IEF-1.C.6.b defines neoliberalism by privatization and EK IEF-1.C.6.d defines socialism by the nationalization of major private industries, which are opposite answers to one question. EK IEF-1.C.6.a, .e and .f are defined by liberties, nationhood and the common people rather than by ownership."),
 dict(q="Why can a party be described as populist without that description settling its position on the economy?",
   choices=[
     "because the framework defines populism only by support for the interests and rights of the common people over those of the elites",
     "because the framework defines populism as identical to socialism",
     "because the framework defines populism as identical to neoliberalism",
     "because the framework says populism is not a political ideology",
     "because the framework says every populist party nationalizes major industries"], ans=0,
   why="EK IEF-1.C.6.f defines populism as a political philosophy supporting the interests and rights of the common people over that of the elites, and says nothing about ownership, distribution or regulation. Those questions are the content of EK IEF-1.C.6.b, .c and .d instead."),
 dict(q="Taking the framework's account of political ideologies together, which summary is most accurate?",
   choices=[
     "An ideology is a set of values and beliefs about the goals of government, public policy or politics, and the framework names six, defined variously by liberties, by the state's economic role, by nationhood, and by whose interests should prevail",
     "An ideology is the collective attitude of an entire citizenry, and the framework names two",
     "The framework's six ideologies are all defined by their positions on the ownership of industry",
     "The framework's six ideologies are all defined by their positions on civil liberties",
     "The framework defines the six ideologies and assigns one to each course country"], ans=0,
   why="EK IEF-1.C.6 supplies the definition and its six representations, and those six are defined on different axes: liberties in .a, economic intervention in .b, .c and .d, nationhood and authoritarian rule in .e, and the common people against the elites in .f. The framework assigns none of them to a course country."),
]
