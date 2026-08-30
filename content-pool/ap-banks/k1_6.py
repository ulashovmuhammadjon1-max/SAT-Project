# AP COMPARATIVE GOVERNMENT AND POLITICS 1.6 Change in Power and Authority
# CED effective Fall 2026, Unit 1 Political Systems, Regimes, and Governments.
# Enduring understanding PAU-1; learning objective PAU-1.D. Suggested skill 4.A,
# Source Analysis.
#
# Essential knowledge relied on:
#   PAU-1.D.2  how a regime chooses to use power in support of sovereignty is
#              determined in large part by its democratic or authoritarian
#              characteristics -- DEMOCRATIC REGIMES CAN MAINTAIN SOVEREIGNTY
#              USING LESS POWER THAN AUTHORITARIAN REGIMES
#   PAU-1.D.3  changes in REGIMES occur when rules and institutions are replaced
#              either INCREMENTALLY OR SUDDENLY, as a result of elections, coups,
#              or revolutions in which a large portion of the population supports
#              a change in the political system
#   PAU-1.D.4  GOVERNMENTS, including political officeholders, can be changed more
#              frequently and easily than regimes through the relatively peaceful
#              process of elections, appointments, and lines of succession;
#              however, governments also change by more violent means, such as
#              revolutions or coups d'etat, represented by such violent
#              transitions in IRAN AND NIGERIA
#
# Supporting statements, each named in the verifier's claim where it is used:
#   PAU-1.A.2  a regime is the fundamental rules controlling access to and exercise
#              of political power, and regimes typically endure from government to
#              government
#   PAU-1.D.1b Iran's transition from dictatorial rule to a theocracy after 1979
#   PAU-1.D.1c Nigeria and Mexico to multiparty republics following military rule
#              and single-party dominance respectively
#   PAU-1.D.1e constitutional reforms in the United Kingdom devolving power to
#              multiple parliaments, allowing the regime to maintain stability
#   PAU-4.A.3  rules ensuring one-party dominance in Russia (registration
#              requirements, threshold rules, eliminating gubernatorial elections)
#   PAU-4.A.4  rules facilitating Mexico's transition away from one-party dominance
#   LEG-1.B.2  peaceful resolution of conflicts and peaceful transfer of power
#              reinforce legitimacy
#
# PAU-1.D.2 is a POSITIVE CLAIM of the framework, not a value judgement to be
# hedged, and it is easy to misread as 'democracies are weaker'. Item 3 keys the
# correct reading. Table figures are HYPOTHETICAL and labelled so; no item asks
# how many times a real country has changed government, which would date.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md.
TOPIC = ("1.6", "Change in Power and Authority", 1)

_T_TURN = dict(
    headers=["Country (hypothetical)", "Changes of head of government, 1990-2020",
             "Changes of constitutional order, 1990-2020",
             "Changes of head of government occurring by election or succession"],
    rows=[["Country D", "9", "0", "9"],
          ["Country E", "7", "1", "4"],
          ["Country F", "4", "2", "1"],
          ["Country G", "2", "0", "2"]])

_T_MEANS = dict(
    headers=["Means of change", "Changes of government (hypothetical)",
             "Of those, changes that also replaced the regime"],
    rows=[["Election", "48", "2"],
          ["Appointment or line of succession", "23", "0"],
          ["Coup", "6", "4"],
          ["Revolution", "2", "2"]])

QUESTIONS = [
 dict(q="Which statement about the relationship between regime type and the use of power does the framework assert?",
   choices=[
     "Democratic regimes can maintain sovereignty using less power than authoritarian regimes",
     "Authoritarian regimes can maintain sovereignty using less power than democratic regimes",
     "Every regime must use the same amount of power to maintain sovereignty",
     "Sovereignty does not depend on the use of power in any regime",
     "Only federal regimes can maintain sovereignty without the use of power"], ans=0,
   why="EK PAU-1.D.2 states this directly, adding that how a regime chooses to use power in support of sovereignty is determined in large part by its democratic or authoritarian characteristics. The framework offers it as a positive claim rather than as a preference."),
 dict(q="According to the framework, what determines in large part how a regime chooses to use power in support of its sovereignty?",
   choices=[
     "its democratic or authoritarian characteristics",
     "the size of its territory and population",
     "whether it is a member of a supranational organization",
     "the number of political parties registered within it",
     "the age of its written constitution"], ans=0,
   why="EK PAU-1.D.2 states that how a regime chooses to use power in support of sovereignty is determined in large part by its democratic or authoritarian characteristics. Territory, treaty membership, party counts and constitutional age are not offered anywhere as determinants of this."),
 dict(q="A student reads the framework's claim about power and sovereignty as meaning that democratic regimes possess less sovereignty than authoritarian ones. The best correction is that the framework says",
   choices=[
     "democracies need to expend less power to maintain the same sovereignty, which is a claim about the power required rather than about the sovereignty held",
     "democracies hold more sovereignty than authoritarian regimes and use more power to maintain it",
     "sovereignty is unrelated to how a regime uses power",
     "only authoritarian regimes possess sovereignty at all",
     "sovereignty is conferred on a regime by international organizations rather than held by the state"], ans=0,
   why="EK PAU-1.D.2 compares the POWER required, stating that democratic regimes can maintain sovereignty using less power than authoritarian regimes. EK PAU-1.A.4's sovereignty is a state's independent legal authority over a population and territory, which the statement does not say democracies have less of."),
 dict(q="The framework says changes in regimes occur when rules and institutions are replaced. Which set of routes does it name?",
   choices=[
     "elections, coups, or revolutions in which a large portion of the population supports a change in the political system",
     "revolutions alone, since rules cannot be replaced peacefully",
     "elections alone, since only voters may change a regime",
     "decisions of an international court, followed by ratification",
     "the resignation of a head of government followed by an appointment"], ans=0,
   why="EK PAU-1.D.3 names elections, coups and revolutions in which a large portion of the population supports a change in the political system, and says the replacement of rules and institutions can be incremental or sudden. Restricting the list to one route contradicts the sentence."),
 dict(q="Over fifteen years a state amends its constitution repeatedly: judicial appointments pass to the executive, the term of the head of state is extended twice, the electoral commission is folded into a ministry, and opposition parties are progressively deregistered. In the framework's terms this sequence is best described as",
   choices=[
     "a regime change accomplished incrementally, since the fundamental rules of access to and exercise of power have been replaced step by step",
     "a series of changes of government, since no single event replaced the constitution at once",
     "no change at all, since the constitution was amended rather than abolished",
     "a change of state, since the institutions differ from those the state began with",
     "a change of nation, since the population's political identity has altered"], ans=0,
   why="EK PAU-1.D.3 states that changes in regimes occur when rules and institutions are replaced either incrementally or suddenly, so a stepwise route is one the framework expressly recognizes. EK PAU-1.A.2 makes those fundamental rules the regime, and every amendment listed alters them."),
 dict(q="In a second state, a mass uprising drives out the existing ruler within weeks, the constitution is annulled, and an entirely new set of governing institutions is proclaimed. In the framework's terms this is",
   choices=[
     "a regime change accomplished suddenly, by revolution",
     "a change of government only, since a new leader has taken office",
     "an incremental regime change, because institutions take time to establish",
     "a change of state, since the territory is now governed differently",
     "a change of political culture rather than of rules"], ans=0,
   why="EK PAU-1.D.3 names revolutions in which a large portion of the population supports a change in the political system among the routes by which rules and institutions are replaced, and says the replacement may be sudden. Annulling the constitution and proclaiming new institutions is the replacement of the rules themselves, not merely of officeholders."),
 dict(q="The framework says that governments, including political officeholders, can be changed",
   choices=[
     "more frequently and easily than regimes",
     "less frequently and with more difficulty than regimes",
     "only at the same time as the regime that contains them",
     "only by revolution or coup",
     "only where the state is federal rather than unitary"], ans=0,
   why="EK PAU-1.D.4 states that governments, including political officeholders, can be changed more frequently and easily than regimes, and EK PAU-1.A.2 explains why: regimes typically endure from government to government because they are the rules under which officeholders are replaced."),
 dict(q="Which set of processes does the framework describe as the relatively peaceful means by which governments change?",
   choices=[
     "elections, appointments, and lines of succession",
     "revolutions, coups, and mass uprisings",
     "constitutional annulment and the proclamation of new institutions",
     "rulings of supranational courts and treaty obligations",
     "referendums on the transfer of territory"], ans=0,
   why="EK PAU-1.D.4 names elections, appointments and lines of succession as the relatively peaceful process by which governments change, and contrasts them with the more violent means it lists in the same statement."),
 dict(q="The framework adds that governments also change by more violent means. Which means does it name, and in which two course countries does it locate such transitions?",
   choices=[
     "revolutions or coups, in Iran and Nigeria",
     "revolutions or coups, in China and Russia",
     "elections and appointments, in Mexico and the United Kingdom",
     "referendums, in Russia and the United Kingdom",
     "supranational intervention, in Mexico and Nigeria"], ans=0,
   why="EK PAU-1.D.4 states that governments also change by more violent means such as revolutions or coups, represented by such violent transitions in Iran and Nigeria. The framework names those two countries and no others in this connection."),
 dict(q="Which comparison of the two course countries the framework associates with violent transitions is supported by its other statements?",
   choices=[
     "One moved from dictatorial rule to a theocracy after a revolution, while the other became a multiparty republic following military rule",
     "One moved from dictatorial rule to a theocracy, while the other became a one-party state",
     "Both moved from military rule to theocracies",
     "Both became managed democracies with election rules favoring one party",
     "Neither experienced any change of regime, only changes of government"], ans=0,
   why="EK PAU-1.D.4 names Iran and Nigeria as the sites of violent transitions, EK PAU-1.D.1.b describes Iran's move from dictatorial rule to a theocracy based on Islamic Sharia law after the 1979 Revolution, and EK PAU-1.D.1.c describes Nigeria's transition to a multiparty republic following military rule. The destinations differ even though both routes were violent."),
 dict(q="In one country officers seize the broadcasting station, remove the president and install a general in the same office; the constitution, the legislature and the courts continue to operate under their existing rules. In a second country officers do the same and then annul the constitution and dissolve the legislature. Applying the framework, the first is",
   choices=[
     "a change of government and the second a change of regime",
     "a change of regime and the second a change of government",
     "a change of regime in both cases, since force was used in both",
     "a change of government in both cases, since a single officeholder was replaced in both",
     "neither, since only elections can change a government or a regime"], ans=0,
   why="EK PAU-1.A.2 makes the regime the fundamental rules controlling access to and exercise of power, so what distinguishes the two cases is whether those rules were replaced. EK PAU-1.D.4 notes that governments change by violent as well as peaceful means, so the use of force does not by itself make a change a regime change."),
 dict(q="Under what circumstances does the framework treat an election as producing a change of regime rather than only a change of government?",
   choices=[
     "when the rules and institutions controlling access to and exercise of power are themselves replaced as a result",
     "whenever the governing party loses its majority",
     "whenever turnout rises above the previous election's level",
     "whenever a head of government from a different party takes office",
     "never, since elections can change only officeholders"], ans=0,
   why="EK PAU-1.D.3 lists elections among the routes by which rules and institutions are replaced, so an election can produce a regime change, but EK PAU-1.A.2 requires that the fundamental rules themselves change. A new majority or a new prime minister under unchanged rules is a change of government."),
 dict(q="The framework's account of revolutions specifies that they involve",
   choices=[
     "a large portion of the population supporting a change in the political system",
     "the intervention of a foreign state on behalf of the opposition",
     "a ruling by the highest court that the government is unlawful",
     "a vote of the legislature to dissolve itself",
     "the resignation of the head of state for reasons of health"], ans=0,
   why="EK PAU-1.D.3 describes revolutions in which a large portion of the population supports a change in the political system, which is what distinguishes a revolution in the framework's usage from a palace coup or a constitutional crisis."),
 dict(q="Applying the framework's distinctions to Iran's 1979 Revolution, which description is most accurate?",
   choices=[
     "Both the government and the regime changed, since the rules of access to and exercise of power were replaced along with the rulers",
     "The government changed but the regime did not, since the same territory and population remained",
     "The regime changed but the government did not, since the previous ministers stayed in office",
     "Neither changed, since the state retained its international recognition",
     "The state changed, since a new set of institutions was created"], ans=0,
   why="EK PAU-1.D.1.b describes a transition of power from dictatorial rule to a theocracy based on Islamic Sharia law, which is a replacement of the fundamental rules under EK PAU-1.A.2 and therefore a regime change; the rulers changed with them. EK PAU-1.A.2 also makes clear the state persists through such a change."),
 dict(q="Nigeria's transition to a multiparty republic following military rule illustrates which combination of the framework's claims?",
   choices=[
     "that regimes change when rules and institutions are replaced, and that a country whose governments have changed violently can arrive at a multiparty republic",
     "that regimes never change once a military has held power",
     "that only revolutions supported by most of the population can change a regime",
     "that changes of government and changes of regime are the same event",
     "that a change of regime requires the approval of a supranational organization"], ans=0,
   why="EK PAU-1.D.1.c records the transition to a multiparty republic following military rule, EK PAU-1.D.3 supplies the mechanism of rules and institutions being replaced, and EK PAU-1.D.4 names Nigeria among the countries with violent transitions. The three statements are consistent with one another."),
 dict(q="The framework describes a set of rules in one course country including higher party registration requirements, higher thresholds for ballot access, and the elimination of gubernatorial elections. In the vocabulary of this topic these are best described as",
   choices=[
     "an incremental replacement of the rules controlling access to power",
     "a sudden replacement of the rules by revolution",
     "a change of government leaving the rules of access untouched",
     "a devolution of power to regional parliaments",
     "a transition to a multiparty republic"], ans=0,
   why="EK PAU-4.A.3 lists these among the rules ensuring one-party dominance in Russia, and EK PAU-1.D.3 states that changes in regimes occur when rules and institutions are replaced either incrementally or suddenly. Each measure narrows access to power by rule change rather than by a single event."),
 dict(q="Constitutional reforms devolving power to multiple parliaments in the United Kingdom are presented by the framework as an example of",
   choices=[
     "rules and institutions being changed by constitutional means in a way that allowed the regime to maintain stability",
     "a sudden change of regime brought about by revolution",
     "a change of government accomplished through a line of succession",
     "a transition away from single-party dominance",
     "the replacement of a unitary state by a federal one"], ans=0,
   why="EK PAU-1.D.1.e states that constitutional reforms in the United Kingdom devolved power to multiple parliaments, allowing the regime to maintain stability, and EK PAU-2.A.1 continues to list the United Kingdom as a unitary state. The change was to institutions, by constitutional means, and it preserved rather than replaced the regime."),
 dict(q="Mexico's move away from one-party dominance came about through measures including the elimination of a nomination practice, privatization to decrease patronage, decentralization of party power, and the strengthening of a national electoral institute. In this topic's terms these measures are best described as",
   choices=[
     "a peaceful and largely incremental change in the rules governing access to power",
     "a violent transition of the kind the framework locates in Iran and Nigeria",
     "a change of government with no effect on the rules of access to power",
     "the devolution of power to regional parliaments",
     "the replacement of a theocracy by a multiparty republic"], ans=0,
   why="EK PAU-4.A.4 lists these rules as facilitating Mexico's transition away from one-party dominance and EK PAU-1.D.1.c records the destination as a multiparty republic. EK PAU-1.D.3's incremental route fits a sequence of rule changes, and EK PAU-1.D.4 names Iran and Nigeria rather than Mexico for violent transitions."),
 dict(q="The table reports hypothetical figures for four countries over three decades. Which country's record best illustrates the framework's claim that governments change more frequently and easily than regimes?",
   table=_T_TURN,
   choices=[
     "Country D, with nine changes of head of government, all by election or succession, and no change of constitutional order",
     "Country F, with four changes of head of government and two changes of constitutional order",
     "Country G, with two changes of head of government and no change of constitutional order",
     "Country E, because it had the second highest number of changes of head of government",
     "None of the four, because the framework supplies no figures for any country"], ans=0,
   why="EK PAU-1.D.4 pairs frequency with peacefulness, describing governments changing often through elections, appointments and lines of succession while regimes endure. The row that shows the most changes of officeholder, all by those peaceful routes, alongside no change of the constitutional order is the one that shows both halves at once."),
 dict(q="Using the same table, in which country did the largest share of changes of head of government occur by means other than election or succession?",
   table=_T_TURN,
   choices=[
     "Country F, where three of four such changes came by other means",
     "Country E, where three of seven such changes came by other means",
     "Country D, where none came by other means",
     "Country G, where none came by other means",
     "The table does not report the means by which any change occurred"], ans=0,
   why="Subtracting the count of changes occurring by election or succession from the total gives the number occurring by other means, and comparing that number with each country's total gives the share. EK PAU-1.D.4 treats those other means as the more violent ones, so the largest share marks the least peaceful record."),
 dict(q="Across all four countries in the table, the ratio of changes of head of government to changes of constitutional order is closest to",
   table=_T_TURN,
   choices=[
     "7 to 1",
     "1 to 7",
     "3 to 1",
     "22 to 1",
     "1 to 1"], ans=0,
   why="Summing each column gives twenty-two changes of head of government against three changes of constitutional order, a ratio a little above seven to one. EK PAU-1.D.4's claim that governments change more frequently than regimes is what such a ratio expresses in numbers."),
 dict(q="The table reports hypothetical counts of how governments changed across the six course countries over six decades, and how many of those changes also replaced the regime. Which conclusion does it support?",
   table=_T_MEANS,
   choices=[
     "The two most common means of changing a government almost never replaced the regime, whereas the two least common almost always did",
     "The two most common means of changing a government almost always replaced the regime",
     "Every change of government in the table also replaced the regime",
     "No change of government in the table replaced the regime",
     "Coups changed governments more often than elections did"], ans=0,
   why="Reading each row as a fraction, the two largest counts are followed by only a handful of regime replacements between them, while the two smallest are followed by regime replacement in most or all cases. That is EK PAU-1.D.4's contrast between the frequent peaceful routes and the rare violent ones, expressed as proportions."),
 dict(q="According to the same table, the total number of changes of government recorded across all four means is",
   table=_T_MEANS,
   choices=[
     "79",
     "71",
     "77",
     "31",
     "48"], ans=0,
   why="Adding the four figures in the changes-of-government column gives the total; the alternatives offered arise from omitting one of the smaller rows, from adding the wrong column, or from reading only the largest single row."),
 dict(q="Which of the following is a change of government but NOT a change of regime?",
   choices=[
     "A prime minister resigns and the governing party's new leader takes office under the same constitutional rules",
     "A constitution is annulled and lawmaking is vested in a council of officers",
     "Competitive elections are abolished and a single party is given exclusive governing power",
     "A monarchy is replaced by a republic with a wholly new set of institutions",
     "The rules controlling access to power are rewritten by a constituent assembly"], ans=0,
   why="EK PAU-1.A.2 makes the regime the fundamental rules controlling access to and exercise of power and EK PAU-1.D.4 identifies lines of succession among the peaceful routes by which governments change. A leadership succession under unchanged rules leaves the regime intact, while each rejected option replaces the rules themselves."),
 dict(q="Which of the following is most clearly a change of regime?",
   choices=[
     "A constitution is suspended, elections are cancelled indefinitely, and a council of officers assumes the power to legislate",
     "A governing coalition loses a confidence vote and a new coalition takes office",
     "A president completes a single permitted term and hands office to an elected successor",
     "A cabinet is reshuffled after a poor result at a regional election",
     "A legislature passes a budget over the executive's objection"], ans=0,
   why="EK PAU-1.D.3 describes regime change as the replacement of rules and institutions, including by coup, and EK PAU-1.A.2 identifies those rules as the regime. Suspending the constitution and cancelling elections replaces them; the four rejected events all occur inside rules that continue to operate."),
 dict(q="Why, on the framework's account, are governments easier to change than regimes?",
   choices=[
     "Because the rules that select officeholders are designed to replace them periodically, whereas changing those rules requires replacing the rules themselves",
     "Because officeholders serve fixed terms in every country",
     "Because international organizations require governments to be replaced at intervals",
     "Because regimes may be changed only by foreign intervention",
     "Because a government has no legal authority until a regime approves it"], ans=0,
   why="EK PAU-1.A.2 states that regimes typically endure from government to government, and EK PAU-1.D.4 that governments can be changed more frequently and easily through elections, appointments and lines of succession. Those routes are provided by the regime, so using them leaves the regime standing."),
 dict(q="Two states face the same wave of protest. One relies on courts, elections and negotiated concessions to restore order; the other deploys mass detentions and bans on assembly. The framework's claim about power and sovereignty predicts that",
   choices=[
     "the first is able to maintain sovereignty with a smaller expenditure of power because of its democratic characteristics",
     "the second is able to maintain sovereignty with a smaller expenditure of power because it acts decisively",
     "both must expend the same amount of power, since both face the same protest",
     "neither retains sovereignty once protest has begun",
     "sovereignty passes to whichever institution restores order first"], ans=0,
   why="EK PAU-1.D.2 states that democratic regimes can maintain sovereignty using less power than authoritarian regimes, and that how a regime uses power in support of sovereignty is determined in large part by its democratic or authoritarian characteristics. The prediction follows from the regime type rather than from the protest."),
 dict(q="Which comparison of a peaceful and a violent transition is most consistent with the framework's account of legitimacy?",
   choices=[
     "A peaceful transfer of power tends to reinforce legitimacy, whereas a violent seizure has no such effect and may leave the new government's right to rule contested",
     "A violent seizure of power reinforces legitimacy because it demonstrates the new government's strength",
     "Neither a peaceful nor a violent transfer bears on legitimacy, which depends only on economic growth",
     "Legitimacy is conferred by other states rather than by a government's own constituents",
     "Legitimacy and sovereignty are the same thing, so both change with every transfer of power"], ans=0,
   why="EK LEG-1.B.2 names peaceful resolution of conflicts and peaceful transfer of power among the things that reinforce legitimacy, and EK LEG-1.A.1 defines legitimacy as whether a government's constituents believe it has the right to use power in the way it does. Recognition by other states is a different matter, addressed under EK PAU-1.A.2's account of the state."),
 dict(q="A researcher claims that a country has undergone a regime change rather than merely a change of government. Which finding would most strongly support that claim?",
   choices=[
     "The procedures determining who may hold office and how power may be exercised were replaced, and the previous rules no longer govern anything",
     "A leader from a different party now heads the government",
     "Several ministries were merged and renamed",
     "The capital city was moved to another part of the country",
     "The governing party's share of the vote fell by twenty points"], ans=0,
   why="EK PAU-1.A.2 identifies the regime with the fundamental rules controlling access to and exercise of political power, so evidence of a regime change must be evidence about those rules. A new party in office, administrative reorganization, a new capital and a swing in vote share are all compatible with rules that have not changed."),
 dict(q="Taking the framework's three statements on change in power and authority together, which summary is most accurate?",
   choices=[
     "Regimes change when rules and institutions are replaced, incrementally or suddenly and by peaceful or violent routes, while governments change more often and more easily through routes the regime itself provides",
     "Regimes and governments change at the same rate, since both are replaced by elections",
     "Regimes change only by revolution and governments only by election",
     "Neither regimes nor governments can change without the intervention of another state",
     "Governments change only when the population as a whole supports a change in the political system"], ans=0,
   why="EK PAU-1.D.3 supplies the routes and the incremental or sudden pace of regime change, and EK PAU-1.D.4 supplies the greater frequency and ease of government change through elections, appointments and lines of succession while noting that violent routes exist for governments too. The summary keeps both halves rather than collapsing them."),
]
