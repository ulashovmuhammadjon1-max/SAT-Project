# AP COMPARATIVE GOVERNMENT AND POLITICS 3.8 Political and Social Cleavages
# CED effective Fall 2026, Unit 3 Political Culture and Participation. Enduring
# understanding LEG-2 (how governments respond to social and political divisions
# affects interactions between citizens and long-term regime stability); learning
# objectives LEG-2.A and LEG-2.B. Suggested skill 2.A, Country Comparison.
#
# Essential knowledge relied on:
#   LEG-2.A.1  social and political cleavages are INTERNAL DIVISIONS THAT STRUCTURE
#              SOCIETIES and may be based on CLASS, ETHNICITY, RELIGION or
#              TERRITORY, as represented by:
#     .a CHINA -- ethnic and regional divisions between the majority HAN group and
#        AT LEAST 55 RECOGNIZED ETHNIC MINORITIES, such as the UIGHURS in the
#        northwest and the TIBETANS in the southwest, and between AREAS THAT HAVE
#        DEVELOPED AT DIFFERENT RATES
#     .b IRAN -- religious divisions between the SHI'A MUSLIM MAJORITY and members
#        of other religions such as CHRISTIANITY, JUDAISM and ZOROASTRIANISM, which
#        have resulted in A THREATENING ATMOSPHERE DESPITE OFFICIAL RECOGNITION;
#        within Islam, divisions between the SHI'A MAJORITY and SUNNIS; and ethnic
#        cleavages between the majority PERSIANS and minorities including
#        AZERBAIJANIS and KURDS
#     .c MEXICO -- ethnic divisions between the AMERINDIAN population and WHITES AND
#        MESTIZOS, and regional divisions between NORTH and SOUTH
#     .d NIGERIA -- ethnic divisions among MORE THAN 250 ETHNIC GROUPS (including
#        HAUSA-FULANI, YORUBA and IGBO), and religious and regional cleavages
#        between the PREDOMINANTLY MUSLIM NORTH and the SOUTH, where CHRISTIANS AND
#        ANIMISTS are concentrated
#     .e RUSSIA -- cleavages between ETHNIC RUSSIANS, MORE THAN 80 PERCENT of the
#        population and tending to be RUSSIAN ORTHODOX, and minority non-Russian
#        populations including the CHECHENS in the Caucasus, PREDOMINANTLY MUSLIM
#     .f UNITED KINGDOM -- ethnic and regional differences between nations such as
#        the SCOTTISH, ENGLISH, WELSH and IRISH; religious differences between
#        PROTESTANTS AND CATHOLICS IN NORTHERN IRELAND; and RACIAL TENSIONS between
#        whites and non-European minorities whose heritage relates to the UNITED
#        KINGDOM'S COLONIAL HISTORY
#   LEG-2.B.1  major cleavages DIFFER ACROSS COURSE COUNTRIES and affect VOTING
#              BEHAVIOR and PARTY SYSTEMS as well as INFORMAL POLITICAL NETWORKS
#   LEG-2.B.2  course countries have RESPONDED DIFFERENTLY:
#     .a EVEN STABLE REGIMES are increasingly dealing with RADICAL/TERRORIST
#        RELIGIOUS ELEMENTS that have sprung from long-standing cleavages
#     .b responses range from BRUTE REPRESSION to RECOGNITION of ethnic/religious
#        minorities and the creation of AUTONOMOUS REGIONS and/or REPRESENTATION OF
#        MINORITIES IN GOVERNMENTAL INSTITUTIONS
#   LEG-2.B.3  examples of the USE OF CLEAVAGES TO STRENGTHEN LEGITIMACY AND HOLD
#              ONTO POWER can be found IN ALL COURSE COUNTRIES; such cleavages MAY
#              ALSO LEAD TO CONFLICT AND UNDERMINE LEGITIMACY
#   LEG-2.B.4  .a SEPARATIST MOVEMENTS in CHINA, IRAN, NIGERIA, RUSSIA and the
#              UNITED KINGDOM; .b groups demanding AUTONOMY BUT NOT INDEPENDENCE in
#              MEXICO and the UNITED KINGDOM; .c ethnicity has played a MORE
#              SIGNIFICANT role in NIGERIA THAN MEXICO because of DIFFERENT COLONIAL
#              HISTORIES and greater diversity and politicization in Nigeria
#
# Topic 1.10 already keys LEG-2.B.2.b's range and the two country lists of
# LEG-2.B.4 as prose items. This module keys the LEG-2.A.1 country detail those
# lists rest on, puts the two lists into a matrix instead of a sentence (items
# 26-27), and keys LEG-2.B.1 and LEG-2.B.3, which topic 1.10 does not use.
#
# The framework's own precise numbers here are AT LEAST 55 recognized ethnic
# minorities in China, MORE THAN 250 ethnic groups in Nigeria, and ethnic Russians
# at MORE THAN 80 PERCENT. Items 3, 8 and 9 key them; nothing else numerical is
# asserted about any country.
#
# Table figures and cases are HYPOTHETICAL and labelled so.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md.
TOPIC = ("3.8", "Political and Social Cleavages", 3)

_T_VOTE = dict(
    headers=["Region (hypothetical)",
             "Share of the region's population belonging to one national group (percent)",
             "Share of the region's vote for the party associated with that group (percent)"],
    rows=[["Region 1", "88", "79"],
          ["Region 2", "41", "36"],
          ["Region 3", "12", "9"]])

_T_RESP = dict(
    headers=["State response to a cleavage (hypothetical case)", "Description"],
    rows=[["Response 1", "mass detention of members of a minority and a ban on their language in schools"],
          ["Response 2", "creation of an autonomous region with authority over language and education"],
          ["Response 3", "seats reserved for recognized minorities in the national legislature"],
          ["Response 4", "an official campaign blaming a minority for the country's economic difficulties"]])

_T_SEP = dict(
    headers=["Country (hypothetical)", "Separatist movements reported",
             "Groups demanding autonomy but not independence reported"],
    rows=[["Country J", "yes", "yes"],
          ["Country K", "no", "yes"],
          ["Country L", "yes", "no"],
          ["Country M", "no", "no"]])

QUESTIONS = [
 dict(q="How does the framework describe social and political cleavages, and on what may they be based?",
   choices=[
     "internal divisions that structure societies, which may be based on class, ethnicity, religion or territory",
     "external pressures applied by neighboring states and supranational organizations",
     "the constitutional rules controlling access to political power",
     "the collective attitudes and values of a whole citizenry",
     "the voluntary associations that are autonomous from the state"], ans=0,
   why="EK LEG-2.A.1 describes social and political cleavages as internal divisions that structure societies and names class, ethnicity, religion and territory as their possible bases. The rejected options are external actors, EK PAU-1.A.2's regime, EK IEF-1.C.1's political culture and EK IEF-1.A.1's civil society."),
 dict(q="Which cleavages does the framework describe in China?",
   choices=[
     "ethnic and regional divisions between the majority Han group and recognized ethnic minorities, and between areas that have developed at different rates",
     "religious divisions between a Shi'a majority and Sunni and non-Muslim minorities",
     "ethnic divisions between an Amerindian population and whites and mestizos",
     "religious and regional cleavages between a Muslim north and a Christian south",
     "national differences among four constituent nations and religious differences in one of them"], ans=0,
   why="EK LEG-2.A.1.a describes ethnic and regional divisions between the majority Han ethnic group and its recognized ethnic minorities, and between areas that have developed at different rates. The rejected descriptions are the framework's accounts of Iran, Mexico, Nigeria and the United Kingdom."),
 dict(q="How many recognized ethnic minorities does the framework attribute to China, and which does it name?",
   choices=[
     "at least 55, including the Uighurs in the northwest and the Tibetans in the southwest",
     "more than 250, including the Hausa-Fulani, Yoruba and Igbo",
     "exactly two, the Uighurs and the Tibetans",
     "more than 80, including the Chechens",
     "the framework gives no figure and names no minorities"], ans=0,
   why="EK LEG-2.A.1.a states at least 55 recognized ethnic minorities, such as the Uighurs in the northwest and the Tibetans in the southwest. The 250-group figure belongs to Nigeria under EK LEG-2.A.1.d and the Chechens to Russia under EK LEG-2.A.1.e."),
 dict(q="How does the framework describe the position of religious minorities in Iran?",
   choices=[
     "divisions between the Shi'a Muslim majority and members of other religions have resulted in a threatening atmosphere despite official recognition",
     "members of other religions are neither recognized nor tolerated in any form",
     "members of other religions hold a majority of seats in the legislature",
     "no religious division is reported in that country",
     "religious divisions there are confined to differences within Islam"], ans=0,
   why="EK LEG-2.A.1.b states that religious divisions between the Shi'a Muslim majority and members of other religions such as Christianity, Judaism and Zoroastrianism have resulted in a threatening atmosphere DESPITE OFFICIAL RECOGNITION. Recognition and a threatening atmosphere coexist in the framework's account, and EK DEM-2.A.1.b adds that a small number of Majles seats are reserved for non-Muslim minorities."),
 dict(q="Which division within Islam does the framework describe in Iran?",
   choices=[
     "between the Shi'a majority and those who are Sunni",
     "between the Sunni majority and those who are Shi'a",
     "between Muslims and Zoroastrians",
     "between Persians and Azerbaijanis",
     "no division within Islam is described"], ans=0,
   why="EK LEG-2.A.1.b states that within practitioners of Islam there are divisions between the Shi'a majority and those who are Sunni. The Persian-Azerbaijani division is described in the same statement as an ETHNIC cleavage rather than a religious one."),
 dict(q="Which ethnic cleavages does the framework describe in Iran?",
   choices=[
     "between the majority Persians and several ethnic minorities, including Azerbaijanis and Kurds",
     "between the majority Han and at least 55 recognized minorities",
     "between an Amerindian population and whites and mestizos",
     "between ethnic Russians and non-Russian populations",
     "among more than 250 ethnic groups"], ans=0,
   why="EK LEG-2.A.1.b names ethnic cleavages between the majority Persians and several ethnic minorities including Azerbaijanis and Kurds, alongside the religious divisions it describes in the same statement. The rejected descriptions belong to China, Mexico, Russia and Nigeria."),
 dict(q="Which cleavages does the framework describe in Mexico?",
   choices=[
     "ethnic divisions between the Amerindian population and whites and mestizos, and regional divisions between the north and the south",
     "religious divisions between a Shi'a majority and other religions",
     "national differences among four constituent nations",
     "cleavages between an ethnic majority of more than 80 percent and non-majority populations",
     "ethnic divisions among more than 250 groups"], ans=0,
   why="EK LEG-2.A.1.c describes ethnic divisions between the Amerindian, that is indigenous, population and whites and mestizos, together with regional divisions between the north and the south. The rejected descriptions are the framework's accounts of Iran, the United Kingdom, Russia and Nigeria."),
 dict(q="Which cleavages does the framework describe in Nigeria?",
   choices=[
     "ethnic divisions among more than 250 groups, and religious and regional cleavages between a predominantly Muslim north and a south where Christians and animists are concentrated",
     "ethnic divisions between a Han majority and recognized minorities",
     "regional divisions between north and south with no religious dimension",
     "religious divisions within Islam between a Shi'a majority and Sunnis",
     "racial tensions arising from a colonial history of immigration"], ans=0,
   why="EK LEG-2.A.1.d states ethnic divisions among more than 250 ethnic groups, including the Hausa-Fulani, Yoruba and Igbo, and religious and regional cleavages between the predominantly Muslim north and the south where Christians and animists are concentrated. Both the ethnic and the religious-regional halves are the framework's."),
 dict(q="How does the framework describe the principal cleavage in Russia?",
   choices=[
     "between ethnic Russians, more than 80 percent of the population and tending to be Russian Orthodox, and minority non-Russian populations including the predominantly Muslim Chechens",
     "between a Shi'a majority and Sunni and non-Muslim minorities",
     "among more than 250 ethnic groups of comparable size",
     "between an indigenous population and whites and mestizos",
     "between four constituent nations of roughly equal standing"], ans=0,
   why="EK LEG-2.A.1.e describes cleavages between ethnic Russians, who are more than 80 percent of the population and tend to be Russian Orthodox, and minority non-Russian populations including the Chechens in the Caucasus region, who are predominantly Muslim."),
 dict(q="Which three kinds of difference does the framework describe in the United Kingdom?",
   choices=[
     "national and regional differences among the Scottish, English, Welsh and Irish; religious differences between Protestants and Catholics in Northern Ireland; and racial tensions related to the country's colonial history",
     "ethnic divisions among more than 250 groups and a Muslim north against a Christian south",
     "divisions between a Shi'a majority and Sunni and non-Muslim minorities",
     "regional divisions between north and south and an indigenous-settler ethnic division",
     "a single ethnic majority of more than 80 percent against non-majority populations"], ans=0,
   why="EK LEG-2.A.1.f names ethnic and regional differences between nations such as the Scottish, English, Welsh and Irish; religious differences between Protestants and Catholics in Northern Ireland; and racial tensions between whites and non-European minorities whose heritage is related to the country's colonial history."),
 dict(q="What does the framework say major social and political cleavages affect?",
   choices=[
     "voting behavior and party systems, as well as informal political networks",
     "the territorial structure of the state and its international recognition",
     "the length of judicial terms and the method of judicial appointment",
     "the number of chambers in the legislature",
     "the rate of economic growth alone"], ans=0,
   why="EK LEG-2.B.1 states that major social and political cleavages differ across course countries and affect voting behavior and party systems as well as informal political networks. All three consequences are named in the same sentence."),
 dict(q="What does the framework say about stable regimes and religious radicalism?",
   choices=[
     "even stable regimes are increasingly dealing with radical or terrorist religious elements that have sprung from long-standing cleavages",
     "only unstable regimes face radical or terrorist religious elements",
     "radical religious elements arise only where a state has no official religion",
     "radical religious elements arise only in federal states",
     "the framework does not connect radicalism to cleavages"], ans=0,
   why="EK LEG-2.B.2.a states that even stable regimes are increasingly dealing with radical or terrorist religious elements that have sprung from long-standing cleavages. The word 'even' is what rules out confining the problem to unstable cases."),
 dict(q="A state faced with an ethnic cleavage detains members of the minority group in large numbers and bans their language from schools. Where does this response sit on the range the framework describes?",
   choices=[
     "at the brute repression end of the range",
     "at the recognition end of the range",
     "outside the range, since the framework describes only accommodating responses",
     "at the midpoint, since a language policy is not a use of force",
     "outside the range, since responses to cleavages are not described by the framework"], ans=0,
   why="EK LEG-2.B.2.b states that state responses can range from brute repression to recognition of ethnic and religious minorities and the creation of autonomous regions and/or representation of minorities in governmental institutions. Mass detention and a language ban sit at the first of those endpoints."),
 dict(q="What does the framework say about the use of cleavages by governments?",
   choices=[
     "examples of using cleavages to strengthen legitimacy and hold onto power can be found in all course countries, though such cleavages may also lead to conflict and undermine legitimacy",
     "cleavages are used to strengthen legitimacy only in authoritarian regimes",
     "cleavages always undermine legitimacy and never strengthen it",
     "cleavages always strengthen legitimacy and never undermine it",
     "no course country has used cleavages in this way"], ans=0,
   why="EK LEG-2.B.3 states that examples of the use of social and political cleavages to strengthen legitimacy and hold onto power can be found in ALL course countries, and that such cleavages may also lead to conflict and undermine legitimacy. Both halves are in the same statement."),
 dict(q="What does the framework's placing of the United Kingdom on two separate lists tell a reader?",
   choices=[
     "that separatist movements and groups demanding autonomy short of independence have both emerged there",
     "that no separatist movement has emerged there",
     "that every group there demands full independence",
     "that its cleavages are purely religious",
     "that it is the only country where either kind of movement has emerged"], ans=0,
   why="EK LEG-2.B.4.a names the United Kingdom among the five countries where separatist movements have emerged and EK LEG-2.B.4.b names it, with Mexico, among those where groups demanding autonomy but not independence have emerged. Being on both lists means both kinds of movement are present."),
 dict(q="A student writes that the framework says Mexico has no ethnic divisions. What is the correction?",
   choices=[
     "the framework describes ethnic divisions in Mexico between the Amerindian population and whites and mestizos, and says only that ethnicity has played a more significant role in Nigeria",
     "the framework does indeed say Mexico has no ethnic divisions",
     "the framework says Mexico's divisions are entirely religious",
     "the framework says Mexico's divisions are entirely based on class",
     "the framework does not mention Mexico among the course countries"], ans=0,
   why="EK LEG-2.A.1.c describes ethnic divisions between Mexico's Amerindian population and whites and mestizos, and EK LEG-2.B.4.c says only that ethnicity has played a MORE SIGNIFICANT role in Nigeria than in Mexico. The claim is comparative, not a denial."),
 dict(q="Why, according to the framework, has ethnicity mattered more in Nigeria than in Mexico?",
   choices=[
     "because of different colonial histories and a greater diversity and politicization of ethnic and religious identities in Nigeria",
     "because Mexico is unitary and Nigeria is federal",
     "because Nigeria holds elections and Mexico does not",
     "because Nigeria belongs to more supranational organizations",
     "because Mexico has no recognized minority groups"], ans=0,
   why="EK LEG-2.B.4.c gives exactly this explanation. EK PAU-2.A.1 in fact lists BOTH countries among the federal states, so territorial structure cannot be the difference."),
 dict(q="Which course country does the framework describe with cleavages that are religious and regional at the same time, running between two halves of the country?",
   choices=[
     "Nigeria, divided between a predominantly Muslim north and a south where Christians and animists are concentrated",
     "China, divided between a Han majority and recognized minorities",
     "Russia, divided between ethnic Russians and non-Russian populations",
     "Mexico, divided between an indigenous population and whites and mestizos",
     "Iran, divided between Persians and Azerbaijanis and Kurds"], ans=0,
   why="EK LEG-2.A.1.d describes religious and regional cleavages between the predominantly Muslim north and the south where Christians and animists are concentrated, so a single line divides the country on both dimensions at once. The rejected descriptions are ethnic or ethnic-and-regional rather than religious-and-regional."),
 dict(q="Which comparison of the cleavages the framework describes in China and Russia is accurate?",
   choices=[
     "Each is described as a division between a dominant group and recognized or identified minority populations, with a further regional dimension",
     "Each is described as a division between two religious communities of roughly equal size",
     "Neither is described as having any ethnic dimension",
     "Each is described as a division among more than 250 groups of comparable size",
     "Each is described as a division between an indigenous population and settlers"], ans=0,
   why="EK LEG-2.A.1.a describes a Han majority against at least 55 recognized minorities plus divisions between areas developing at different rates, and EK LEG-2.A.1.e describes ethnic Russians at more than 80 percent against minority non-Russian populations including the Chechens in the Caucasus region. Both pair a dominant group with minorities and locate minorities regionally."),
 dict(q="The table reports hypothetical figures for three regions of one country. Which conclusion does it support?",
   table=_T_VOTE,
   choices=[
     "The share voting for the party associated with the national group tracks that group's share of each region's population",
     "The party's vote share is the same in every region regardless of population",
     "The party's vote share is highest where the group's population share is lowest",
     "The party's vote share exceeds the group's population share in every region",
     "The table reports nothing about the party's vote"], ans=0,
   why="EK LEG-2.B.1 states that major social and political cleavages affect voting behavior and party systems, and the two columns rise and fall together across the three rows. The party's share is below the group's share in every region, which is why the reversed reading fails."),
 dict(q="Using the same table, in which region is the gap between the group's population share and the party's vote share largest?",
   table=_T_VOTE,
   choices=[
     "Region 1, where the gap is 9 percentage points",
     "Region 2, where the gap is 5 percentage points",
     "Region 3, where the gap is 3 percentage points",
     "The gaps are equal in all three regions",
     "The table does not permit the comparison"], ans=0,
   why="Subtracting each region's vote share from its population share gives the gap, and comparing the three identifies the largest. Each alternative states the true gap for a different region, so the item turns on comparing them rather than computing one."),
 dict(q="According to the same table, the second region's party vote share as a percentage of that region's group population share is closest to",
   table=_T_VOTE,
   choices=[
     "88 percent",
     "36 percent",
     "41 percent",
     "12 percent",
     "114 percent"], ans=0,
   why="Dividing that region's party vote share by its group population share and expressing the result as a percentage gives the answer. The alternatives offer the two raw figures, a figure from another row, and the same division performed the wrong way round."),
 dict(q="The table describes four hypothetical state responses to a cleavage. Which one sits at the brute repression end of the framework's range?",
   table=_T_RESP,
   choices=[
     "Response 1, mass detention of members of a minority and a ban on their language in schools",
     "Response 2, creation of an autonomous region with authority over language and education",
     "Response 3, seats reserved for recognized minorities in the national legislature",
     "Response 4, an official campaign blaming a minority for the country's economic difficulties",
     "None of the four, since the framework describes no repressive responses"], ans=0,
   why="EK LEG-2.B.2.b states that state responses range from brute repression to recognition of ethnic and religious minorities and the creation of autonomous regions and/or representation in governmental institutions. Only one row uses force and prohibition against the group itself."),
 dict(q="Using the same table, which two responses match the accommodating end of the framework's range?",
   table=_T_RESP,
   choices=[
     "Responses 2 and 3, the autonomous region and the reserved legislative seats",
     "Responses 1 and 4, the detentions and the official campaign",
     "Responses 1 and 2, the detentions and the autonomous region",
     "Responses 3 and 4, the reserved seats and the official campaign",
     "None of the four, since the framework describes only repression"], ans=0,
   why="EK LEG-2.B.2.b names recognition of ethnic and religious minorities, the creation of autonomous regions, and representation of minorities in governmental institutions as the accommodating endpoint, and two rows of the table state the last two of those exactly."),
 dict(q="Using the same table, which response best illustrates the framework's claim that governments use cleavages to hold onto power?",
   table=_T_RESP,
   choices=[
     "Response 4, an official campaign blaming a minority for the country's economic difficulties",
     "Response 2, creation of an autonomous region",
     "Response 3, seats reserved for recognized minorities",
     "Response 1, mass detention of members of a minority",
     "None of the four, since the framework says cleavages are never used in this way"], ans=0,
   why="EK LEG-2.B.3 states that examples of the use of social and political cleavages to strengthen legitimacy and hold onto power can be found in all course countries. An official campaign directing blame at a minority uses the cleavage rather than repressing or accommodating the group, and EK LEG-2.B.3 adds that such uses may also lead to conflict and undermine legitimacy."),
 dict(q="The table records, for four hypothetical countries, which kinds of movement have been reported. Which row matches the framework's description of the United Kingdom?",
   table=_T_SEP,
   choices=[
     "Country J, where both separatist movements and groups demanding autonomy without independence are reported",
     "Country K, where only groups demanding autonomy without independence are reported",
     "Country L, where only separatist movements are reported",
     "Country M, where neither is reported",
     "None of the four, since the framework reports no movements for that country"], ans=0,
   why="EK LEG-2.B.4.a names the United Kingdom among the five countries with separatist movements and EK LEG-2.B.4.b names it among the two with groups demanding autonomy but not independence, so it appears on both lists. Only one row of the table records both."),
 dict(q="Using the same table, which row matches the framework's description of Mexico?",
   table=_T_SEP,
   choices=[
     "Country K, where groups demanding autonomy without independence are reported but separatist movements are not",
     "Country J, where both kinds of movement are reported",
     "Country L, where only separatist movements are reported",
     "Country M, where neither is reported",
     "None of the four, since Mexico appears on both of the framework's lists"], ans=0,
   why="EK LEG-2.B.4.b names Mexico and the United Kingdom as the countries where groups demanding autonomy but not independence have emerged, while EK LEG-2.B.4.a's separatist list names China, Iran, Nigeria, Russia and the United Kingdom, with Mexico absent. Only one row records the second without the first."),
 dict(q="Which finding would most strongly support a claim that a government is using a cleavage to strengthen its own position?",
   choices=[
     "The governing party's campaigns present one group as the nation's rightful core and another as a threat, and its support rises among the first group whenever it does so",
     "The government has created an autonomous region with authority over language",
     "The government has reserved legislative seats for recognized minorities",
     "The government has published statistics on the size of each ethnic group",
     "The government has signed a treaty with a neighbouring state"], ans=0,
   why="EK LEG-2.B.3 states that examples of the use of social and political cleavages to strengthen legitimacy and hold onto power can be found in all course countries. Autonomy and reserved seats are EK LEG-2.B.2.b's accommodating responses, and publishing statistics or signing a treaty is neither."),
 dict(q="Which pair of measures does the framework name at the accommodating end of the range of state responses to cleavages?",
   choices=[
     "the creation of autonomous regions and the representation of minorities in governmental institutions",
     "mass detention and prohibition of a minority language",
     "the dissolution of minority organizations and the closure of their media",
     "the redrawing of international borders and the transfer of populations",
     "the suspension of the constitution and the cancellation of elections"], ans=0,
   why="EK LEG-2.B.2.b names recognition of ethnic and religious minorities and the creation of autonomous regions and/or representation of minorities in governmental institutions as the accommodating endpoint, with brute repression at the other. The rejected options are repressive or belong to other statements."),
 dict(q="Taking the framework's statements on cleavages together, which summary is most accurate?",
   choices=[
     "Cleavages are internal divisions based on class, ethnicity, religion or territory; they differ across the six countries and shape voting, party systems and informal networks; states respond along a range from brute repression to recognition and autonomy; and all six have examples of cleavages used to hold onto power as well as to divide",
     "Cleavages are external pressures applied by neighbouring states, and every country responds to them identically",
     "Cleavages exist in only two of the six course countries and always undermine legitimacy",
     "Cleavages affect only voting behavior and nothing else",
     "Cleavages are always responded to by repression in authoritarian regimes and by accommodation in democracies"], ans=0,
   why="EK LEG-2.A.1 supplies the definition and the four bases with a country-by-country account, EK LEG-2.B.1 the effects on voting, party systems and informal networks, EK LEG-2.B.2 the differing responses and their range, and EK LEG-2.B.3 the use of cleavages to hold onto power in all course countries alongside their capacity to undermine legitimacy."),
]
