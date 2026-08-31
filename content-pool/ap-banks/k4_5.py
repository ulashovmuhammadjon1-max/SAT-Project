# AP COMPARATIVE GOVERNMENT AND POLITICS 4.5 Impact of Social Movements and
# Interest Groups
# CED effective Fall 2026, Unit 4 Party and Electoral Systems and Citizen
# Organizations. Enduring understanding IEF-2 (strong and varied citizen
# organizations and movements foster and are reinforced by democratization);
# learning objective IEF-2.A. Suggested skill 5.D, Argumentation (use refutation,
# concession, or rebuttal in responding to opposing or alternate perspectives).
#
# Essential knowledge relied on:
#   IEF-2.A.1  SOCIAL MOVEMENTS involve LARGE GROUPS OF PEOPLE PUSHING COLLECTIVELY
#              for SIGNIFICANT POLITICAL OR SOCIAL CHANGE
#   IEF-2.A.2  INTEREST GROUPS are EXPLICITLY ORGANIZED to REPRESENT AND ADVOCATE
#              FOR A SPECIFIC INTEREST OR POLICY ISSUE, while SOCIAL MOVEMENTS
#              represent MULTIPLE GROUPS AND INDIVIDUALS advocating for BROAD
#              SOCIAL CHANGE
#   IEF-2.A.3  social movements across course countries have PUT PRESSURE ON THE
#              STATE to PROMOTE INDIGENOUS CIVIL RIGHTS, REDISTRIBUTE REVENUES FROM
#              KEY EXPORTS SUCH AS OIL, CONDUCT FAIR AND TRANSPARENT ELECTIONS, and
#              ENSURE FAIR TREATMENT OF CITIZENS OF DIFFERENT SEXUAL ORIENTATIONS,
#              including:
#     .a the GREEN MOVEMENT IN IRAN, which PROTESTED CORRUPTION IN THE 2009 ELECTION
#     .b the ZAPATISTAS or CHIAPAS UPRISING IN MEXICO, in response to SOCIOECONOMIC
#        INEQUALITY and the NEGATIVE IMPACT OF THE NORTH AMERICAN FREE TRADE
#        AGREEMENT (NAFTA)
#     .c MOVEMENTS IN NIGERIA (OFTEN MILITANT), including the MOVEMENT FOR THE
#        EMANCIPATION OF THE NIGER DELTA (MEND) and the MOVEMENT FOR THE SURVIVAL OF
#        THE OGONI PEOPLE (MOSOP), which have emerged to ADVOCATE FOR THE RIGHTS OF
#        AN ETHNIC MINORITY or PROTEST AGAINST UNJUST METHODS OF EXTRACTION AND
#        DISTRIBUTION OF OIL IN THE NIGER DELTA REGION
#     .d the BOKO HARAM movement ATTEMPTING TO ESTABLISH AN ISLAMIC STATE IN
#        NORTHERN NIGERIA
#     .e DOMESTIC PROTESTS OVER RUSSIAN STATE DUMA'S PASSAGE OF LEGISLATION AGAINST
#        SAME-SEX COUPLES
#   IEF-2.A.4  GRASSROOTS social movements EXERT THEIR POWER UP FROM THE LOCAL LEVEL
#              to the REGIONAL, NATIONAL, or INTERNATIONAL level
#   IEF-2.A.5  WITH LIMITED ORGANIZATIONAL HIERARCHIES, such movements are DIFFICULT
#              FOR STATE-RUN MILITARY OR LAW ENFORCEMENT TO SUPPRESS, BUT some social
#              movements ALSO HAVE DIFFICULTY IN ATTRACTING AND MOBILIZING SUPPORT
#              AMONG FELLOW CITIZENS OR NEGOTIATING WITH GOVERNMENTAL REPRESENTATIVES
#
# IEF-2.A.5 IS A CONCESSION SENTENCE, and the suggested skill for this topic is
# argumentation by refutation, concession and rebuttal. The same property -- a
# flat structure with few leadership levels -- is stated as an advantage against
# suppression and a disadvantage in mobilizing and in negotiating. A student who
# remembers only the first clause will treat leaderlessness as costless. Items
# 11, 12, 20 and 21-23 all turn on holding both clauses at once.
#
# IEF-2.A.2 IS THE DEFINITION PAIR THAT GETS COLLAPSED. An interest group is
# EXPLICITLY ORGANIZED around a SPECIFIC interest or policy issue; a social
# movement is MULTIPLE groups and individuals pushing for BROAD social change.
# Two axes, not one: how organized, and how wide the aim. Items 2, 3 and 18 key
# both axes rather than the size of the group.
#
# Table figures are HYPOTHETICAL and labelled so. The stated demands in the third
# table are the framework's own four pressures, worded as IEF-2.A.3 words them.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md.
TOPIC = ("4.5", "Impact of Social Movements and Interest Groups", 4)

_T_SUPPRESS = dict(
    headers=["Movement (hypothetical)", "Formal leadership levels",
             "Participants arrested as a share of all participants (percent)",
             "Formal agreements negotiated with government representatives"],
    rows=[["Movement 1", "1", "4", "0"],
          ["Movement 2", "6", "21", "6"],
          ["Movement 3", "3", "12", "2"]])

_T_SCALE = dict(
    headers=["Stage (hypothetical)", "Highest level at which the movement was active",
             "Local groups taking part", "Governments responding publicly"],
    rows=[["Stage 1", "Local", "5", "0"],
          ["Stage 2", "Regional", "34", "1"],
          ["Stage 3", "National", "112", "1"],
          ["Stage 4", "International", "149", "4"]])

_T_DEMANDS = dict(
    headers=["Movement (hypothetical)", "Stated demand"],
    rows=[["Movement W", "Fair and transparent conduct of a disputed national election"],
          ["Movement X", "Redistribution of the revenues earned from the country's oil exports"],
          ["Movement Y", "Fair treatment of citizens of different sexual orientations"],
          ["Movement Z", "Relief from socioeconomic inequality worsened by a regional free trade agreement"]])

QUESTIONS = [
 dict(q="How does the framework define a social movement?",
   choices=[
     "large groups of people pushing collectively for significant political or social change",
     "an organization formally registered with the state to contest elections",
     "a body of state-sanctioned representatives of an economic sector",
     "a single association employing professional staff to lobby one ministry",
     "an alliance of parties formed to nominate a joint candidate"], ans=0,
   why="EK IEF-2.A.1 states that social movements involve large groups of people pushing collectively for significant political or social change. The word collectively and the breadth of the aim are both parts of the definition."),
 dict(q="How does the framework define an interest group?",
   choices=[
     "a body explicitly organized to represent and advocate for a specific interest or policy issue",
     "a loose network of individuals with no stated aim",
     "any large gathering of citizens in a public place",
     "an association that nominates candidates for legislative office",
     "a chamber of the legislature reserved for economic sectors"], ans=0,
   why="EK IEF-2.A.2 states that interest groups are explicitly organized to represent and advocate for a specific interest or policy issue, so both the deliberate organization and the narrowness of the aim belong to the definition."),
 dict(q="On the framework's account, an interest group and a social movement differ along which two dimensions at once?",
   choices=[
     "how explicitly they are organized, and how broad the change they seek is",
     "how many members they have, and how much money they raise",
     "whether they are legal, and whether they are violent",
     "whether they contest elections, and whether they hold seats",
     "whether they are national, and whether they are recognized abroad"], ans=0,
   why="EK IEF-2.A.2 contrasts a body explicitly organized around a specific interest or policy issue with multiple groups and individuals advocating for broad social change, which is a contrast in organization and in breadth of aim rather than in size alone."),
 dict(q="What does the framework say the Green Movement in Iran protested?",
   choices=[
     "corruption in the 2009 election",
     "the removal of agricultural subsidies",
     "the terms of a regional free trade agreement",
     "methods of oil extraction in a delta region",
     "legislation passed against same-sex couples"], ans=0,
   why="EK IEF-2.A.3.a names the Green Movement in Iran as having protested corruption in the 2009 election. The rejected objects of protest belong to the framework's Mexican, Nigerian and Russian examples."),
 dict(q="To what does the framework attribute the Zapatista or Chiapas uprising in Mexico?",
   choices=[
     "socioeconomic inequality and the negative impact of the North American Free Trade Agreement",
     "corruption in a disputed presidential election",
     "the passage of legislation against same-sex couples",
     "unjust methods of oil extraction in a delta region",
     "an attempt to establish a religious state in the north of the country"], ans=0,
   why="EK IEF-2.A.3.b states that the Zapatistas or Chiapas uprising in Mexico arose in response to socioeconomic inequality and the negative impact of the North American Free Trade Agreement. The other options are the framework's Iranian, Russian and Nigerian examples."),
 dict(q="What does the framework say the Movement for the Emancipation of the Niger Delta and the Movement for the Survival of the Ogoni People emerged to do?",
   choices=[
     "advocate for the rights of an ethnic minority or protest against unjust methods of extraction and distribution of oil in the Niger Delta region",
     "contest national legislative elections under a party label",
     "negotiate wage agreements on behalf of a single industry",
     "protest the outcome of a disputed presidential election",
     "oppose the terms of a regional free trade agreement"], ans=0,
   why="EK IEF-2.A.3.c names both movements as having emerged to advocate for the rights of an ethnic minority or to protest against unjust methods of extraction and distribution of oil in the Niger Delta region."),
 dict(q="Which country's social movements does the framework describe as often militant?",
   choices=[
     "Nigeria",
     "the United Kingdom",
     "Mexico",
     "China",
     "Iran"], ans=0,
   why="EK IEF-2.A.3.c introduces the movements it names with the parenthetical that movements in Nigeria are often militant. No other country's movements carry that description in the framework."),
 dict(q="What does the framework say the Boko Haram movement is attempting to do?",
   choices=[
     "establish an Islamic state in northern Nigeria",
     "secure a larger share of oil revenues for a delta region",
     "overturn the result of a disputed election",
     "reverse a regional free trade agreement",
     "repeal legislation directed at same-sex couples"], ans=0,
   why="EK IEF-2.A.3.d states that the Boko Haram movement is attempting to establish an Islamic state in northern Nigeria. The rejected aims belong to the framework's other four examples."),
 dict(q="What does the framework identify as the object of the domestic protests it records in Russia?",
   choices=[
     "the State Duma's passage of legislation against same-sex couples",
     "a disputed presidential election result",
     "the privatization of a state-owned oil company",
     "the terms of accession to a supranational organization",
     "the reinstatement of single-member districts"], ans=0,
   why="EK IEF-2.A.3.e records domestic protests over the Russian State Duma's passage of legislation against same-sex couples, which places the protest against an act of the legislature."),
 dict(q="Which set of demands does the framework name as the pressures social movements have placed on states across the course countries?",
   choices=[
     "promoting indigenous civil rights, redistributing revenues from key exports such as oil, conducting fair and transparent elections, and ensuring fair treatment of citizens of different sexual orientations",
     "raising tariffs, nationalizing banks, expanding the armed forces, and leaving supranational organizations",
     "lengthening legislative terms, abolishing term limits, and enlarging the cabinet",
     "creating special economic zones, cutting subsidies, and privatizing state industries",
     "changing threshold rules, redrawing districts, and registering new parties"], ans=0,
   why="EK IEF-2.A.3 names exactly those four pressures before listing its five country examples. The rejected sets are economic liberalization measures and electoral rule changes treated under other statements."),
 dict(q="In which direction does the framework say grassroots social movements exert their power?",
   choices=[
     "up from the local level to the regional, national, or international level",
     "down from an international body to national and then local affiliates",
     "outward from the capital to the provinces",
     "from the legislature to the executive",
     "from a party's leadership to its ordinary members"], ans=0,
   why="EK IEF-2.A.4 states that grassroots social movements exert their power up from the local level to the regional, national, or international level, so the movement begins where its participants live rather than at a national headquarters."),
 dict(q="What advantage does the framework attribute to a social movement with limited organizational hierarchies?",
   choices=[
     "it is difficult for state-run military or law enforcement to suppress",
     "it can compel a government to negotiate with it",
     "it attracts support among fellow citizens more easily",
     "it is guaranteed representation in the legislature",
     "it can be registered as a political party without conditions"], ans=0,
   why="EK IEF-2.A.5 states that with limited organizational hierarchies such movements are difficult for state-run military or law enforcement to suppress, because there is no command structure to remove."),
 dict(q="Which difficulties does the framework say some social movements also face?",
   choices=[
     "attracting and mobilizing support among fellow citizens, and negotiating with governmental representatives",
     "recruiting professional staff and renting offices",
     "obtaining recognition from foreign governments and joining supranational bodies",
     "clearing the threshold for legislative representation and registering candidates",
     "collecting membership dues and publishing a platform"], ans=0,
   why="EK IEF-2.A.5 states that some social movements have difficulty in attracting and mobilizing support among fellow citizens or in negotiating with governmental representatives, which is the concession that follows its claim about resisting suppression."),
 dict(q="What relationship does the framework state between citizen organizations and movements on one side and democratization on the other?",
   choices=[
     "strong and varied citizen organizations and movements foster democratization and are in turn reinforced by it",
     "democratization produces citizen organizations but is unaffected by them",
     "citizen organizations produce democratization but are unaffected by it",
     "the two are unrelated",
     "citizen organizations arise only after democratization is complete"], ans=0,
   why="Enduring understanding IEF-2 states that strong and varied citizen organizations and movements foster and are reinforced by democratization, which makes the relationship mutual rather than one-directional."),
 dict(q="Which comparison of the Iranian and Russian examples in the framework is accurate?",
   choices=[
     "One protested corruption in the conduct of an election; the other protested a law the national legislature had passed",
     "Both protested the conduct of an election",
     "Both protested a law the national legislature had passed",
     "One protested a trade agreement and the other an election result",
     "Neither example is described by the framework"], ans=0,
   why="EK IEF-2.A.3.a names the Green Movement as protesting corruption in the 2009 election and EK IEF-2.A.3.e names domestic protests over the State Duma's passage of legislation against same-sex couples, so one targets an electoral process and the other a legislative act."),
 dict(q="Which comparison of the Nigerian and Mexican examples in the framework is accurate?",
   choices=[
     "Both concern how the benefits of an economy are distributed, one over the extraction and distribution of oil in a particular region and the other over inequality worsened by a trade agreement",
     "Both concern the conduct of national elections",
     "Both concern the treatment of citizens of different sexual orientations",
     "Neither concerns economic conditions",
     "Both arose in response to the same trade agreement"], ans=0,
   why="EK IEF-2.A.3.c describes protest against unjust methods of extraction and distribution of oil in the Niger Delta region and EK IEF-2.A.3.b names socioeconomic inequality and the negative impact of the North American Free Trade Agreement, and EK IEF-2.A.3 lists redistribution of revenues from key exports among the pressures movements apply."),
 dict(q="A body employs a small permanent staff, publishes position papers on a single piece of legislation, and meets ministry officials about it. In the framework's terms this body is",
   choices=[
     "an interest group, since it is explicitly organized around one policy issue",
     "a social movement, since it seeks political change",
     "a political party, since it engages with government",
     "a peak association, since it employs staff",
     "a grassroots movement, since it began locally"], ans=0,
   why="EK IEF-2.A.2 defines interest groups as explicitly organized to represent and advocate for a specific interest or policy issue, and a permanent staff working on one bill is that description exactly, whereas a social movement represents multiple groups pursuing broad social change."),
 dict(q="Tens of thousands of people from many different associations and no association at all take part in demonstrations demanding a wide change in how a government treats a whole category of citizens. In the framework's terms this is",
   choices=[
     "a social movement, since multiple groups and individuals are advocating for broad social change",
     "an interest group, since the demand is directed at government",
     "a political party, since it seeks to change policy",
     "a corporatist peak association, since it speaks for many people",
     "a coalition, since several organizations are involved"], ans=0,
   why="EK IEF-2.A.2 states that social movements represent multiple groups and individuals advocating for broad social change, and EK IEF-2.A.1 adds that they involve large groups pushing collectively, which distinguishes them from a body organized around one policy issue."),
 dict(q="A movement with no central leadership survives repeated attempts by the security forces to break it up, yet after two years it has won no concessions and its numbers have not grown. Which framework claim does this best illustrate?",
   choices=[
     "that limited organizational hierarchies make a movement hard to suppress but can also leave it unable to mobilize support or negotiate with government representatives",
     "that grassroots movements exert power up from the local level",
     "that interest groups are explicitly organized around a specific policy issue",
     "that social movements have pressured states over the conduct of elections",
     "that citizen organizations are reinforced by democratization"], ans=0,
   why="EK IEF-2.A.5 states both halves in one sentence, and the scenario shows both: the movement resists suppression and at the same time fails to attract support or reach agreement with governmental representatives."),
 dict(q="A commentator argues that a movement should stay leaderless because leaderless movements always achieve more. Which rebuttal draws most directly on the framework?",
   choices=[
     "The same absence of hierarchy that frustrates suppression is also stated to hinder mobilizing fellow citizens and negotiating with governmental representatives, so the advantage is not free",
     "The framework states that leaderless movements are always suppressed quickly",
     "The framework states that only registered organizations may address a government",
     "The framework states that movements are irrelevant to democratization",
     "The framework states that hierarchy has no effect on a movement's prospects"], ans=0,
   why="EK IEF-2.A.5 concedes the advantage and then states the cost in the same sentence, so the rebuttal is that the two follow from the same structural feature rather than that the advantage is false."),
 dict(q="The table describes three hypothetical movements. Which conclusion does it support about the movement with the fewest formal leadership levels?",
   table=_T_SUPPRESS,
   choices=[
     "It has both the lowest share of participants arrested and the fewest agreements negotiated with government representatives",
     "It has both the highest share of participants arrested and the most agreements negotiated",
     "It has the lowest share of participants arrested and the most agreements negotiated",
     "It has the highest share of participants arrested and the fewest agreements negotiated",
     "Its leadership structure bears no relationship to either figure"], ans=0,
   why="EK IEF-2.A.5 states that limited organizational hierarchies make a movement hard to suppress but can also leave it unable to negotiate with governmental representatives. The row with fewest leadership levels shows both effects at once."),
 dict(q="According to the same table, the number of formal agreements negotiated with government representatives across all three movements is",
   table=_T_SUPPRESS,
   choices=[
     "8",
     "37",
     "10",
     "6",
     "45"], ans=0,
   why="Adding the agreements column across the three rows gives the total. The alternatives are the arrest column's total, the leadership column's total, the largest single row, and two columns added together."),
 dict(q="Using the same table, the gap between the highest and lowest shares of participants arrested is",
   table=_T_SUPPRESS,
   choices=[
     "17 percentage points",
     "9 percentage points",
     "8 percentage points",
     "21 percentage points",
     "4 percentage points"], ans=0,
   why="Subtracting the smallest figure in the arrest column from the largest gives the gap. The alternatives are the gaps between other pairs in that column and the two extreme values read as though they were differences."),
 dict(q="The table follows one hypothetical movement through four stages. What does it show about how the movement grew?",
   table=_T_SCALE,
   choices=[
     "It began at the local level and reached the regional, then national, then international level, with more local groups taking part at each stage",
     "It began at the international level and worked downward to the local level",
     "It remained at the local level throughout",
     "It reached the national level before any local groups joined",
     "The number of local groups taking part fell as the movement widened"], ans=0,
   why="EK IEF-2.A.4 states that grassroots social movements exert their power up from the local level to the regional, national, or international level. The stages run in that order and the participation column rises at each one."),
 dict(q="According to the same table of stages, the total number of local groups taking part across the four stages is",
   table=_T_SCALE,
   choices=[
     "300",
     "306",
     "154",
     "149",
     "295"], ans=0,
   why="Adding the participation column across the four stages gives the total. The alternatives are the two columns added together, the first and last stages added, the largest single stage, and the total with the smallest stage omitted."),
 dict(q="Using the same table of stages, the increase in local groups taking part between the first stage and the third is",
   table=_T_SCALE,
   choices=[
     "107",
     "144",
     "78",
     "37",
     "112"], ans=0,
   why="Subtracting the first stage's figure from the third stage's gives the increase. The alternatives are the increase to the fourth stage, the increase between the second and third stages, the increase between the fourth and third stages, and a raw stage figure read as an increase."),
 dict(q="The table lists the stated demands of four hypothetical movements. Which demand corresponds to the pressure the framework attributes to the Green Movement in Iran?",
   table=_T_DEMANDS,
   choices=[
     "the demand for fair and transparent conduct of a disputed national election",
     "the demand for redistribution of oil export revenues",
     "the demand for fair treatment of citizens of different sexual orientations",
     "the demand for relief from inequality worsened by a trade agreement",
     "none of the four, since the framework gives no demand for that movement"], ans=0,
   why="EK IEF-2.A.3.a states that the Green Movement in Iran protested corruption in the 2009 election, and EK IEF-2.A.3 names conducting fair and transparent elections among the pressures movements have placed on states."),
 dict(q="Using the same table of demands, which one corresponds to the pressure the framework attributes to the Nigerian movements it names?",
   table=_T_DEMANDS,
   choices=[
     "the demand for redistribution of the revenues earned from oil exports",
     "the demand for fair and transparent conduct of an election",
     "the demand for fair treatment of citizens of different sexual orientations",
     "the demand for relief from inequality worsened by a trade agreement",
     "none of the four, since the framework gives no demand for those movements"], ans=0,
   why="EK IEF-2.A.3.c states that the Nigerian movements it names emerged to advocate for the rights of an ethnic minority or to protest against unjust methods of extraction and distribution of oil in the Niger Delta region, and EK IEF-2.A.3 names redistribution of revenues from key exports such as oil among the pressures."),
 dict(q="Which finding would most strongly support a claim that a movement has developed in the way EK IEF-2.A.4 describes?",
   choices=[
     "It began with meetings in a handful of towns, spread to neighboring regions, then drew participants nationwide and attention from abroad",
     "It was founded by an international body that opened national and then local offices",
     "It was created by a governing party to organize its supporters",
     "It employs a professional staff to lobby a single ministry",
     "It has never operated outside the capital"], ans=0,
   why="EK IEF-2.A.4 states that grassroots social movements exert their power up from the local level to the regional, national, or international level, so the supporting evidence must show power moving upward from where participants live rather than downward from a headquarters."),
 dict(q="Taking EK IEF-2.A as a whole, which summary of social movements and interest groups is most accurate?",
   choices=[
     "They differ in how tightly they are organized and how broad their aims are, they have pressed states across the course countries over elections, resources, and the treatment of particular groups, they typically build upward from local participation, and a loose structure both protects them and limits them",
     "They are interchangeable terms for the same kind of organization",
     "They matter only in democracies and have no presence in authoritarian regimes",
     "They always succeed when they avoid formal leadership",
     "They pursue economic aims only and leave social questions to political parties"], ans=0,
   why="EK IEF-2.A.2 supplies the distinction, EK IEF-2.A.3 the four pressures and five country examples, EK IEF-2.A.4 the upward direction of grassroots power, and EK IEF-2.A.5 both the protection and the limitation that a flat structure brings."),
]
