# AP U.S. GOVERNMENT AND POLITICS 4.2 Political Socialization -- 30 questions
# CED V.1 (c) 2026, Unit 4 American Political Ideologies and Beliefs.
# Learning objective 4.2.A: explain how CULTURAL FACTORS influence political
# socialization.
# Suggested skill for this topic (CED p. 103): 3.A, data analysis -- DESCRIBE
# THE DATA PRESENTED.
#
# Essential knowledge relied on:
#   EK 4.2.A.1 -- "Political socialization refers to the PROCESS by which
#     individuals develop political BELIEFS, VALUES, OPINIONS, AND BEHAVIORS.
#     FAMILY, SCHOOLS, PEERS, MEDIA, and SOCIAL ENVIRONMENTS (INCLUDING CIVIC
#     AND RELIGIOUS ORGANIZATIONS) contribute to the development of an
#     individual's political attitudes and values through the process of
#     political socialization."
#   EK 4.2.A.2 -- "U.S. political culture is defined by its DEMOCRATIC IDEALS,
#     PRINCIPLES, AND CORE VALUES. As a result of GLOBALIZATION, U.S. political
#     culture has BOTH INFLUENCED AND BEEN INFLUENCED BY the values of other
#     countries."
#
# THREE THINGS THE FRAMEWORK'S TWO SENTENCES CONTAIN THAT A SUMMARY LOSES:
#
#   1. FOUR OUTPUTS, and the fourth is BEHAVIORS. Beliefs, values, opinions AND
#      behaviors. Socialization is not only a process that produces what people
#      think; the framework's own list ends with what they do. Items 3 to 6 and
#      the third table turn on the full four.
#
#   2. FIVE AGENTS, and the fifth has a parenthesis. Family, schools, peers,
#      media, and SOCIAL ENVIRONMENTS -- "including civic and religious
#      organizations". A list of four that stops at media drops the entire
#      category the framework spells out. Items 7 to 13 carry all five.
#
#   3. GLOBALIZATION RUNS BOTH WAYS. EK 4.2.A.2's verb phrase is "has both
#      INFLUENCED AND BEEN INFLUENCED BY the values of other countries". A
#      one-way reading -- in either direction -- is half the sentence, and both
#      halves are equally droppable depending on the reader's priors. Items 18
#      to 21 and the second table carry both directions.
#
# WHY THIS MODULE CARRIES NINE DATA ITEMS RATHER THAN SIX. The suggested skill
# for this topic is 3.A, DESCRIBE THE DATA PRESENTED -- the most purely
# quantitative skill in the course, and the only topic in this unit assigned it.
# So three tables rather than two, and the questions on them ask what the data
# say before they ask what the data mean, which is what skill 3.A actually
# tests. Each table is built around one of the three losses listed above: the
# agents, the two directions of influence, and the four outputs.
#
# Documents the CED attaches to 4.2.A (p. 27): Adam Smith, "The Wealth of
# Nations" -- through EK 4.2.A.2's account of U.S. political culture being
# defined by its core values, which EK 4.1.A.1 sources to that work.
#
# QUOTATION POLICY, per SOCIAL_BRIEF.md: all three tables are labelled
# hypothetical, and no quotation is attributed that could not be checked.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("4.2", "Political Socialization", 4)

_AGENTS = ("A hypothetical survey asked respondents which influence they consider most important "
           "in shaping their own political views. The table reports the share naming each, by "
           "age group.")
_AGENTS_TABLE = dict(
    headers=["Influence named as most important", "Under 30 (%)", "Ages 30 to 59 (%)",
             "Age 60 and older (%)"],
    rows=[["Family", "38", "44", "51"],
          ["Schools", "19", "14", "9"],
          ["Peers", "16", "9", "5"],
          ["Media", "21", "24", "26"],
          ["Social environments, including civic and religious organizations", "6", "9", "9"]])

_FLOWS = ("A hypothetical study of ten democracies traced four political practices and recorded, "
          "for each, how many of those countries adopted the practice from United States "
          "practice and how many instances there were of the United States adopting the practice "
          "from abroad.")
_FLOWS_TABLE = dict(
    headers=["Political practice", "Countries adopting it from U.S. practice",
             "Instances of U.S. adoption from abroad"],
    rows=[["Televised candidate debates", "7", "1"],
          ["Judicial review of legislation", "6", "0"],
          ["Proportional representation in a legislative chamber", "0", "3"],
          ["National health insurance systems", "0", "4"]])

_PANEL = ("A hypothetical panel study followed the same adult respondents for ten years and "
          "recorded whether each of four things had changed by the end of the period.")
_PANEL_TABLE = dict(
    headers=["What was measured", "Respondents showing a change (%)",
             "Respondents showing no change (%)"],
    rows=[["Political beliefs", "34", "66"],
          ["Political values", "19", "81"],
          ["Political opinions on specific issues", "58", "42"],
          ["Political behaviors such as voting and volunteering", "41", "59"]])

QUESTIONS = [
 dict(q="According to the course framework, what does political socialization refer to?",
   choices=[
     "The process by which individuals develop political beliefs, values, opinions, and behaviors",
     "The process by which a legislature enacts a statute",
     "The process by which a court decides a constitutional question",
     "The process by which a party selects its nominee",
     "The process by which a citizen registers to vote"], ans=0,
   why="EK 4.2.A.1 defines political socialization in exactly these words. The framework's word PROCESS matters: it names something that happens over time to a person, not an action taken by an institution."),

 dict(q="Which four things does EK 4.2.A.1 say individuals develop through political socialization?",
   choices=[
     "Beliefs, values, opinions, and behaviors",
     "Beliefs, values, and opinions only",
     "Party membership, campaign contributions, and votes",
     "Statutes, regulations, and court decisions",
     "Income, education, and occupation"], ans=0,
   why="EK 4.2.A.1's list has four items and the fourth is BEHAVIORS. A definition that stops at what people think leaves out what the framework says the process also produces, which is what they do."),

 dict(q="Why does it matter that EK 4.2.A.1's list of what political socialization produces ends with BEHAVIORS?",
   choices=[
     "Because it makes socialization an account of what people do politically, not only of what they think",
     "Because it means beliefs and values are unimportant",
     "Because it limits socialization to election years",
     "Because it means only voters are socialized",
     "Because it means the process applies only to adults"], ans=0,
   why="EK 4.2.A.1 names beliefs, values, opinions and behaviors together, so the process the framework describes reaches conduct as well as attitude. Voting and joining an organization are outputs of socialization on the framework's own list."),

 dict(q="A researcher studies why some citizens attend local government meetings and others do not. Which part of EK 4.2.A.1's definition does this research address?",
   choices=[
     "Political behaviors, one of the four things the framework says socialization develops",
     "Political values only, since attendance reflects a value",
     "Neither, since the framework's definition concerns only attitudes",
     "Neither, since local government is outside the framework",
     "Political socialization only where the researcher studies children"], ans=0,
   why="Attendance is conduct, and EK 4.2.A.1's fourth output is behaviors. Nothing in the framework's definition confines the process to attitudes or to any age group."),

 dict(q="How do OPINIONS differ from VALUES in EK 4.2.A.1's list, as the terms are ordinarily used in this course?",
   choices=[
     "Opinions are positions on particular questions, while values are the more general commitments those positions draw on",
     "Opinions are more stable than values",
     "Values apply only to economic questions and opinions only to social ones",
     "Opinions are held by groups and values only by individuals",
     "The two words mean the same thing in the framework"], ans=0,
   why="EK 4.2.A.1 lists both separately, and EK 4.1.A.1's core values are described as things different interpretations of which produce different positions. A framework that listed them as synonyms would not have needed both words."),

 dict(q="EK 4.2.A.1 calls political socialization a PROCESS. What does that word indicate about how it operates?",
   choices=[
     "That it unfolds over time through repeated influence rather than occurring in a single moment",
     "That it is completed by a single decision of the individual",
     "That it is directed by a government agency",
     "That it applies only during a campaign",
     "That it can be reversed by a court order"], ans=0,
   why="A process is something that runs, and EK 4.2.A.1 pairs the word with a set of contributors that operate continuously in a person's life. The framework's own verb for those contributors is CONTRIBUTE TO THE DEVELOPMENT, which is gradual rather than instantaneous."),

 dict(q="Which contributors to political socialization does EK 4.2.A.1 name?",
   choices=[
     "Family, schools, peers, media, and social environments",
     "Family, schools, and peers only",
     "Courts, legislatures, and agencies",
     "Political parties, interest groups, and campaigns",
     "Federal, state, and local governments"], ans=0,
   why="EK 4.2.A.1 names five, and the fifth is social environments. A list that stops at media or at peers drops categories the framework spells out in the same sentence."),

 dict(q="What does EK 4.2.A.1 say SOCIAL ENVIRONMENTS include?",
   choices=[
     "Civic and religious organizations",
     "Federal agencies and state legislatures",
     "Political action committees and party committees",
     "Newspapers and broadcast networks",
     "Courts and law enforcement agencies"], ans=0,
   why="EK 4.2.A.1's parenthesis after social environments reads 'including civic and religious organizations', which makes those bodies course content for this topic rather than an example a reader supplies."),

 dict(q="A student joins a neighborhood association and begins attending its meetings, gradually forming views about how local services should be provided. Which contributor named in EK 4.2.A.1 does the association represent?",
   choices=[
     "A social environment, which the framework's parenthesis says includes civic organizations",
     "The media, since the association publishes a newsletter",
     "The family, since neighbors live nearby",
     "The schools, since the student attends meetings",
     "None of them, since the framework names only four contributors"], ans=0,
   why="EK 4.2.A.1's fifth contributor is social environments, including civic and religious organizations, and a neighborhood association is such an organization. The framework names five contributors, not four."),

 dict(q="A child's political views closely resemble those of the adults who raised the child. Which contributor named in EK 4.2.A.1 does this most directly illustrate?",
   choices=[
     "Family",
     "Schools",
     "Peers",
     "Media",
     "Civic organizations"], ans=0,
   why="EK 4.2.A.1 names family first among the contributors to the development of political attitudes and values. Resemblance between a child's views and those of the people who raised the child is the plainest case of that contribution."),

 dict(q="A required civics course leads students to form clearer views about how a bill becomes law and about whether they intend to vote. Which contributor named in EK 4.2.A.1 is at work, and which outputs does the example touch?",
   choices=[
     "Schools, touching both beliefs and behaviors",
     "Peers, touching only opinions",
     "Media, touching only values",
     "Family, touching only beliefs",
     "Social environments, touching only behaviors"], ans=0,
   why="EK 4.2.A.1 names schools among the five contributors, and the example produces both an understanding and an intention to act, which are two of the framework's four outputs."),

 dict(q="Two friends of the same age discuss politics regularly and find their views converging. Which contributor named in EK 4.2.A.1 does this illustrate?",
   choices=[
     "Peers",
     "Family",
     "Schools",
     "Civic organizations",
     "Religious organizations"], ans=0,
   why="EK 4.2.A.1 names peers among the five contributors, and people of similar age influencing one another outside a family or institutional setting is what the term picks out."),

 dict(q="LO 4.2.A asks how CULTURAL FACTORS influence political socialization. Which of the following is the clearest example of a cultural factor in the framework's sense?",
   choices=[
     "A religious organization in which a person participates regularly",
     "The number of seats a state holds in the House of Representatives",
     "The date on which a state holds its primary election",
     "The term length of a federal judge",
     "The number of signatures required for a ballot initiative"], ans=0,
   why="EK 4.2.A.1's fifth contributor is social environments including civic and religious organizations, which is where the objective's phrase CULTURAL FACTORS attaches. The other four options describe institutional rules rather than the settings in which a person's outlook forms."),

 dict(q="According to EK 4.2.A.2, what defines U.S. political culture?",
   choices=[
     "Its democratic ideals, principles, and core values",
     "Its system of federal courts",
     "Its two major political parties",
     "Its written constitution alone",
     "Its geographic size and population"], ans=0,
   why="EK 4.2.A.2 states this in exactly these words, which is what connects this topic to the four core values EK 4.1.A.1 lists. Institutions appear elsewhere in the course; political culture is defined here by ideals, principles and values."),

 dict(q="According to EK 4.2.A.2, what has been the effect of globalization on U.S. political culture?",
   choices=[
     "U.S. political culture has both influenced and been influenced by the values of other countries",
     "U.S. political culture has influenced other countries without being influenced by them",
     "U.S. political culture has been influenced by other countries without influencing them",
     "Globalization has had no effect on U.S. political culture",
     "Globalization has replaced U.S. political culture entirely"], ans=0,
   why="EK 4.2.A.2's phrase is 'has both influenced and been influenced by the values of other countries', and both halves are in the framework's own sentence. A one-way reading in either direction is half of what the framework says."),

 dict(q="Why is it a misreading of EK 4.2.A.2 to say that globalization has spread American values abroad?",
   choices=[
     "Because it reports one half of a sentence that the framework writes in both directions",
     "Because the framework says no values have crossed borders",
     "Because the framework says American values have not spread at all",
     "Because the framework says globalization affects only economics",
     "Because the framework says other countries have no values"], ans=0,
   why="The claim is not false so much as incomplete: EK 4.2.A.2 says U.S. political culture has BOTH influenced AND been influenced. Reporting only the outward direction states half the framework's sentence as though it were all of it."),

 dict(q="A country adopts a written bill of rights modeled partly on the U.S. Constitution, and in the same decade several U.S. states adopt a budgeting practice developed abroad. How does EK 4.2.A.2 describe this pattern?",
   choices=[
     "As the two directions of influence the framework says globalization has produced",
     "As evidence that only the United States influences other countries",
     "As evidence that only other countries influence the United States",
     "As unrelated to political culture",
     "As a violation of the Supremacy Clause"], ans=0,
   why="EK 4.2.A.2 says U.S. political culture has both influenced and been influenced by the values of other countries, and the scenario contains one instance of each direction. The framework treats both as consequences of globalization."),

 dict(q="How do EK 4.2.A.1 and EK 4.2.A.2 fit together?",
   choices=[
     "The first describes how an individual acquires political attitudes and the second describes the culture those attitudes are acquired within, and how it has changed",
     "The two statements describe the same process under different names",
     "The first concerns courts and the second concerns legislatures",
     "The second contradicts the first",
     "Neither statement concerns political socialization"], ans=0,
   why="EK 4.2.A.1's subject is the individual and the contributors that shape that individual; EK 4.2.A.2's subject is U.S. political culture and its exchange with the values of other countries. The topic pairs a process with the setting it runs in."),

 dict(q="A student argues that because political socialization happens through family and schools, a person's political views are fixed by adolescence. What does the course framework support saying in response?",
   choices=[
     "The framework names five contributors that operate throughout a person's life and calls socialization a process, so it does not describe a fixed endpoint",
     "The framework states that views are fixed by adolescence",
     "The framework names only family and schools as contributors",
     "The framework says political views never change",
     "The framework says socialization begins only in adulthood"], ans=0,
   why="EK 4.2.A.1 names media and social environments alongside family and schools, and its word for what they do is CONTRIBUTE TO THE DEVELOPMENT. EK 4.3.A.1's life cycle effects describe experiences at different life stages, which would be impossible if development stopped."),

 dict(q="Which statement best describes the relationship between political socialization and political ideology as the framework presents it?",
   choices=[
     "Socialization is the process through which attitudes develop, and ideology is shaped by that process",
     "Ideology is fixed at birth and socialization has no effect on it",
     "Socialization and ideology are the same thing",
     "Ideology determines which family a person is born into",
     "Socialization applies only to people with no ideology"], ans=0,
   why="EK 4.2.A.1 makes socialization the process that develops political attitudes and values, and EK 4.4.A.1 states directly that political socialization in turn influences political ideology. The framework orders them rather than equating them."),

 dict(q=_AGENTS + " Which statement most accurately describes the data?",
   table=_AGENTS_TABLE,
   choices=[
     "Family is named most often in every age group, and the share naming it rises across the three groups",
     "Media is named most often in every age group",
     "Schools are named most often among respondents under 30",
     "The share naming family falls across the three age groups",
     "Every influence is named by a similar share in every group"], ans=0,
   why="Family is the largest figure in each column at 38, 44 and 51, and those three figures rise. Media runs 21, 24 and 26, always below family, and schools reach only 19 in the youngest group."),

 dict(q=_AGENTS + " Which influence shows the largest decline in share across the three age groups shown?",
   table=_AGENTS_TABLE,
   choices=[
     "Peers, falling from 16 percent to 5 percent",
     "Family, which rises rather than falls",
     "Media, which rises rather than falls",
     "Social environments, which rise rather than fall",
     "Schools, which fall by more than peers do"], ans=0,
   why="Peers fall by 11 percentage points and schools by 10, so peers show the larger decline. Family, media and social environments all end higher in the oldest group than in the youngest."),

 dict(q=_AGENTS + " A student concludes from the table that media is the most commonly named influence among respondents under 30. What is the most important correction?",
   table=_AGENTS_TABLE,
   choices=[
     "Family is named by 38 percent of that group against 21 percent for media, so family leads there as well",
     "The table reports no figures for respondents under 30",
     "Media is named by more than half of that group",
     "Schools lead among respondents under 30",
     "The table reports only one age group, so no comparison is possible"], ans=0,
   why="In the youngest column family stands at 38 and media at 21, so media is second rather than first. Media is the only influence besides family to exceed 20 percent in that group, which is probably what makes the misreading tempting."),

 dict(q=_FLOWS + " Which statement most accurately describes the data?",
   table=_FLOWS_TABLE,
   choices=[
     "Two of the four practices spread outward from United States practice and two were adopted into it from abroad",
     "All four practices spread outward from United States practice",
     "All four practices were adopted into United States practice from abroad",
     "No practice moved in either direction",
     "Every practice moved in both directions in equal numbers"], ans=0,
   why="Televised debates and judicial review show 7 and 6 countries adopting from U.S. practice, while proportional representation and national health insurance show 3 and 4 instances of adoption into U.S. practice and none outward."),

 dict(q=_FLOWS + " Which statement in the course framework does this table most directly illustrate?",
   table=_FLOWS_TABLE,
   choices=[
     "That U.S. political culture has both influenced and been influenced by the values of other countries",
     "That political socialization develops beliefs, values, opinions, and behaviors",
     "That U.S. political culture is defined by its democratic ideals",
     "That family is the most important contributor to political socialization",
     "That generational effects contribute to political ideology"], ans=0,
   why="EK 4.2.A.2 makes exactly this claim about globalization, and a table with movement in both columns is that claim in observable form. The other statements are true of the framework but describe processes internal to an individual or to U.S. culture alone."),

 dict(q=_FLOWS + " A student concludes from the table that influence has run only outward from the United States. What is the most important correction?",
   table=_FLOWS_TABLE,
   choices=[
     "The table records 8 instances of the United States adopting a practice from abroad, across three of the four practices",
     "The table records no outward movement at all",
     "The table records movement for only one practice",
     "The table reports countries but not instances",
     "The table covers a single country, so no comparison is possible"], ans=0,
   why="Adding the second column gives 1 plus 0 plus 3 plus 4, which is 8 instances across three practices. Both columns are reported and both contain nonzero entries, which is why the one-way reading fails."),

 dict(q=_PANEL + " Which statement most accurately describes the data?",
   table=_PANEL_TABLE,
   choices=[
     "Opinions on specific issues changed for the largest share of respondents and values for the smallest",
     "Values changed for the largest share of respondents",
     "Behaviors changed for the smallest share of respondents",
     "All four categories changed for the same share of respondents",
     "No category changed for more than a fifth of respondents"], ans=0,
   why="The change column reads 34, 19, 58 and 41, so opinions on specific issues are highest and values lowest. Behaviors at 41 are the second highest rather than the lowest."),

 dict(q=_PANEL + " The four rows of this table correspond to which part of the course framework?",
   table=_PANEL_TABLE,
   choices=[
     "EK 4.2.A.1's list of what political socialization develops: beliefs, values, opinions, and behaviors",
     "EK 4.2.A.1's list of contributors to political socialization",
     "EK 4.2.A.2's account of globalization",
     "EK 4.1.A.1's list of core values",
     "EK 4.3.A.1's account of generational and life cycle effects"], ans=0,
   why="The row labels are the four outputs EK 4.2.A.1 names, in the framework's own order. The contributors are family, schools, peers, media and social environments, which are not what this table measures."),

 dict(q=_PANEL + " A student concludes from the table that political socialization is finished before adulthood. What is the most important correction?",
   table=_PANEL_TABLE,
   choices=[
     "Every category changed for a substantial share of these adult respondents over the ten years studied, with the smallest at 19 percent",
     "No category changed for any respondent",
     "The table covers children rather than adults",
     "Every category changed for more than half of respondents",
     "The table reports a single year, so no change can be observed"], ans=0,
   why="The smallest change figure in the table is 19 percent and the largest is 58, all among adults over a ten year period. EK 4.3.A.1's life cycle effects describe experiences encountered during different life stages, which presupposes that development continues."),

 dict(q="A person's family and the religious organization the person belongs to push toward opposite conclusions on a political question. What does the course framework allow a student to conclude about which influence will prevail?",
   choices=[
     "Nothing, because EK 4.2.A.1 lists the contributors without ranking them against one another",
     "That family will prevail, because the framework lists it first",
     "That the religious organization will prevail, because it is named in a parenthesis",
     "That neither influence has any effect where the two conflict",
     "That the person will adopt the view held by the media instead"], ans=0,
   why="EK 4.2.A.1 names family, schools, peers, media and social environments as contributors to the development of political attitudes and values, and supplies no weighting among them. Order of mention in a list is not a claim about strength, and inferring one would put a prediction into the framework that it does not make."),
]
