# AP COMPARATIVE GOVERNMENT AND POLITICS 3.5 Nature and Role of Political
# Participation
# CED effective Fall 2026, Unit 3 Political Culture and Participation. Enduring
# understanding DEM-1 (the way a regime uses power and authority to support or
# suppress its citizens establishes a balance between order and individual
# liberty); learning objective DEM-1.A. Suggested skill 3.D, DATA ANALYSIS.
#
# Essential knowledge relied on:
#   DEM-1.A.1  political participation can be VOLUNTARY OR COERCED and may occur at
#              the INDIVIDUAL OR GROUP level
#   DEM-1.A.2  it can range from behavior SUPPORTIVE OF A REGIME (either
#              INDEPENDENTLY OR UNDER STATE DIRECTION) to OPPOSITIONAL BEHAVIOR that
#              seeks to CHANGE GOVERNMENTAL POLICIES OR OVERTHROW THE REGIME
#   DEM-1.A.3  certain political conditions make VIOLENT POLITICAL BEHAVIOR more
#              likely, INCLUDING WHEN CITIZENS FEEL THAT MORE CONVENTIONAL OPTIONS
#              FOR PARTICIPATION ARE INEFFECTIVE OR UNAVAILABLE
#   DEM-1.A.4  FORMAL political participation, including casting ballots, CAN BE
#              ENCOURAGED ACROSS REGIME TYPES to ENHANCE LEGITIMACY, GATHER INPUT,
#              ACT AS A SAFETY VALVE, or APPLY A CHECK ON GOVERNMENTAL POLICIES,
#              though AUTHORITARIAN regimes are more likely to use participation to
#              INTIMIDATE OPPOSITION OR GIVE AN ILLUSION OF INFLUENCE, while
#              DEMOCRATIC regimes hold elections to ALLOW CITIZEN CONTROL OF THE
#              POLICY-MAKING PROCESS
#   DEM-1.A.5  REFERENDA allow citizens to VOTE DIRECTLY ON POLICY QUESTIONS and are
#              used to PROMOTE DEMOCRATIC POLICY MAKING, to ALLOW A CHIEF EXECUTIVE
#              TO BYPASS THE LEGISLATURE, and to OBLIGE CITIZENS TO MAKE DIFFICULT
#              AND POTENTIALLY UNPOPULAR DECISIONS. The UNITED KINGDOM has used
#              referenda on the DEVOLUTION OF POWERS TO REGIONAL ASSEMBLIES, the
#              SEPARATION AND CREATION OF AN INDEPENDENT NATION-STATE, and its
#              WITHDRAWAL FROM THE EUROPEAN UNION.
#
# DEM-1.A.4 is the statement students most often halve. Formal participation is
# encouraged ACROSS REGIME TYPES and for four named purposes; the difference the
# framework draws is what each type is MORE LIKELY to use it for. Items 7, 10 and
# 20 key that, and no item treats encouraged voting as evidence of regime type on
# its own.
#
# The three United Kingdom referendum subjects at DEM-1.A.5 are the only country
# instances in this topic, and item 13 keys all three together rather than any one
# in isolation.
#
# Table figures are HYPOTHETICAL and labelled so.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md.
TOPIC = ("3.5", "Nature and Role of Political Participation", 3)

_T_TURN = dict(
    headers=["Country (hypothetical)", "Turnout at the most recent national election (percent)",
             "Share of seats contested by more than one candidate (percent)",
             "Share of voters saying voting is legally or socially required (percent)"],
    rows=[["Country P", "93", "11", "68"],
          ["Country Q", "62", "100", "4"],
          ["Country R", "78", "74", "21"]])

_T_PART = dict(
    headers=["Form of participation (hypothetical sample of episodes)", "Episodes recorded",
             "Episodes in which participants sought to change a governmental policy",
             "Episodes in which participants sought to overthrow the regime"],
    rows=[["Voting in a national election", "120", "96", "0"],
          ["Petition and lobbying", "86", "74", "0"],
          ["Street protest", "54", "41", "6"],
          ["Armed insurgency", "7", "0", "7"]])

_T_REF = dict(
    headers=["Referendum (hypothetical)", "Stated reason for holding it", "Turnout (percent)"],
    rows=[["Referendum 1", "to decide whether powers should be devolved to a regional assembly", "64"],
          ["Referendum 2", "to let the chief executive settle a question the legislature had blocked", "51"],
          ["Referendum 3", "to oblige citizens to choose between two unpopular budget options", "38"]])

QUESTIONS = [
 dict(q="What does the framework say about the forms political participation can take?",
   choices=[
     "it can be voluntary or coerced, and may occur at the individual or group level",
     "it is always voluntary and always individual",
     "it is always coerced in authoritarian regimes and always voluntary in democratic ones",
     "it occurs only at the group level",
     "it consists only of casting ballots in elections"], ans=0,
   why="EK DEM-1.A.1 states that political participation can be voluntary or coerced and may occur at the individual or group level. Both distinctions are offered as available in principle rather than as fixed by regime type."),
 dict(q="What range does the framework say political participation can span?",
   choices=[
     "from behavior supportive of a regime to oppositional behavior that seeks to change governmental policies or overthrow the regime",
     "from voting to standing for office",
     "from individual behavior to group behavior only",
     "from lawful behavior to unlawful behavior only",
     "from participation in democratic regimes to non-participation in authoritarian ones"], ans=0,
   why="EK DEM-1.A.2 states that political participation can range from behavior supportive of a regime to oppositional behavior that seeks to change governmental policies or overthrow the regime. The range is defined by the participant's aim rather than by legality or by the number of people involved."),
 dict(q="What qualification does the framework attach to regime-supportive participation?",
   choices=[
     "it may occur either independently or under state direction",
     "it occurs only under state direction",
     "it occurs only independently of the state",
     "it occurs only in democratic regimes",
     "it occurs only where voting is compulsory"], ans=0,
   why="EK DEM-1.A.2 places 'either independently or under state direction' inside its description of behavior supportive of a regime. Supportive participation is therefore not by itself evidence that the state organized it."),
 dict(q="What two aims does the framework attribute to oppositional participation?",
   choices=[
     "seeking to change governmental policies, or seeking to overthrow the regime",
     "seeking to increase turnout, or seeking to reduce it",
     "seeking to join the governing party, or seeking to leave it",
     "seeking international recognition, or seeking supranational membership",
     "seeking to change the constitution only"], ans=0,
   why="EK DEM-1.A.2 describes oppositional behavior as seeking to change governmental policies or overthrow the regime, which are two different targets: a policy inside the rules, or the rules themselves. EK PAU-1.A.2's distinction between government and regime is the same boundary."),
 dict(q="What does the framework say about the conditions for violent political behavior?",
   choices=[
     "certain political conditions make it more likely that citizens will engage in violent political behavior",
     "violent political behavior occurs at random and cannot be connected to conditions",
     "violent political behavior occurs only in authoritarian regimes",
     "violent political behavior occurs only where voting is compulsory",
     "the framework does not discuss violent political behavior"], ans=0,
   why="EK DEM-1.A.3 states that certain political conditions make it more likely that citizens will engage in violent political behavior, and then names one such condition. The claim is about likelihood rather than certainty."),
 dict(q="Which condition does the framework name as making violent political behavior more likely?",
   choices=[
     "when citizens feel that more conventional options for political participation are ineffective or unavailable",
     "when turnout at the most recent election was unusually high",
     "when a country has more than three political parties",
     "when the state is federal rather than unitary",
     "when the head of government is serving a second term"], ans=0,
   why="EK DEM-1.A.3 names this condition explicitly: citizens feeling that more conventional options for political participation are ineffective or unavailable. Both halves matter, since an option can exist and still be believed useless."),
 dict(q="For what purposes does the framework say formal political participation can be encouraged?",
   choices=[
     "to enhance legitimacy, gather input, act as a safety valve, or apply a check on governmental policies",
     "to reduce the cost of administering elections",
     "to satisfy the requirements of a supranational organization",
     "to lengthen the term of the head of government",
     "to transfer authority from the national to the regional level"], ans=0,
   why="EK DEM-1.A.4 names exactly these four purposes and says formal participation can be encouraged ACROSS REGIME TYPES to serve them. The list is what makes encouraged voting compatible with either regime type."),
 dict(q="What does the framework say authoritarian regimes are more likely to use citizen participation for?",
   choices=[
     "to intimidate opposition or give an illusion of influence",
     "to allow citizen control of the policy-making process",
     "to select the head of the judiciary",
     "to determine the state's territorial structure",
     "to satisfy an obligation imposed by a foreign government"], ans=0,
   why="EK DEM-1.A.4 states that authoritarian regimes are more likely to use citizen participation to intimidate opposition or give an illusion of influence. The contrasting clause of the same sentence assigns citizen control of policy making to democratic regimes."),
 dict(q="What does the framework say democratic regimes hold elections for?",
   choices=[
     "to allow citizen control of the policy-making process",
     "to intimidate opposition",
     "to give an illusion of influence",
     "to satisfy a supranational organization's requirements",
     "to select judges for the highest court"], ans=0,
   why="EK DEM-1.A.4 states that democratic regimes hold elections to allow citizen control of the policy-making process, in contrast with the uses it attributes to authoritarian regimes in the same sentence."),
 dict(q="A student concludes that a government's encouraging citizens to vote shows the regime is democratic. What does the framework say?",
   choices=[
     "formal political participation can be encouraged across regime types, so encouragement alone shows nothing about regime type",
     "only democratic regimes encourage formal participation",
     "only authoritarian regimes encourage formal participation",
     "no regime encourages formal participation",
     "encouragement of voting is the framework's definition of democracy"], ans=0,
   why="EK DEM-1.A.4 states that formal political participation can be encouraged across regime types, for four named purposes, before distinguishing what each type is MORE LIKELY to use it for. EK DEM-1.B.1 adds that the difference lies in how open and competitive elections are."),
 dict(q="How does the framework define a referendum's function?",
   choices=[
     "it allows citizens to vote directly on policy questions",
     "it allows citizens to elect representatives to a legislature",
     "it allows a legislature to remove a chief executive",
     "it allows courts to review the constitutionality of a statute",
     "it allows a state to join a supranational organization automatically"], ans=0,
   why="EK DEM-1.A.5 states that referenda allow citizens to vote directly on policy questions. That directness is what separates a referendum from an election of representatives."),
 dict(q="Which set of reasons does the framework give for the use of referenda?",
   choices=[
     "to promote democratic policy making, to allow a chief executive to bypass the legislature, and to oblige citizens to make difficult and potentially unpopular decisions",
     "to select judges, to approve budgets, and to ratify treaties",
     "to remove a head of government, to dissolve a legislature, and to call an early election",
     "to register political parties and to certify election results",
     "to transfer sovereignty to a supranational organization"], ans=0,
   why="EK DEM-1.A.5 names exactly these three reasons, one of which is favorable to democratic policy making and one of which lets an executive go around the legislature. The framework offers them together, without ranking."),
 dict(q="On which questions does the framework say the United Kingdom has used referenda?",
   choices=[
     "the devolution of powers to regional assemblies, the separation and creation of an independent nation-state, and withdrawal from the European Union",
     "the choice of a head of state, the length of parliamentary terms, and the size of the elected chamber",
     "the appointment of judges and the composition of the House of Lords",
     "the adoption of proportional representation for local government only",
     "the annual budget and the level of taxation"], ans=0,
   why="EK DEM-1.A.5 names exactly these three subjects for the United Kingdom's referenda. EK PAU-1.D.1.e separately records the constitutional reforms that devolved power to multiple parliaments, so the first subject connects the two statements."),
 dict(q="In one country citizens who fail to vote face a fine and public listing of their names. Which of the framework's distinctions does this most directly illustrate?",
   choices=[
     "that political participation can be coerced as well as voluntary",
     "that political participation can occur at the group as well as the individual level",
     "that participation can be oppositional as well as supportive",
     "that referenda allow citizens to vote directly on policy questions",
     "that violent political behavior becomes more likely when conventional options fail"], ans=0,
   why="EK DEM-1.A.1 states that political participation can be voluntary or coerced, and a penalty attached to abstention is coercion in the plainest sense. The other distinctions in the framework concern level, aim, mechanism and conditions rather than compulsion."),
 dict(q="A state organizes rallies in support of its programme and instructs public employees to attend. In the framework's terms this is",
   choices=[
     "regime-supportive participation occurring under state direction",
     "oppositional participation seeking to change governmental policies",
     "oppositional participation seeking to overthrow the regime",
     "a referendum on a policy question",
     "an instance of violent political behavior"], ans=0,
   why="EK DEM-1.A.2 describes behavior supportive of a regime occurring either independently or under state direction, and organized attendance instructed by the state is the second of those. EK DEM-1.A.1's coerced participation is the same event described by its other axis."),
 dict(q="A coalition of associations campaigns to have a housing law amended, working through petitions, media coverage and meetings with legislators. In the framework's terms this is",
   choices=[
     "oppositional participation seeking to change governmental policies rather than to overthrow the regime",
     "oppositional participation seeking to overthrow the regime",
     "regime-supportive participation under state direction",
     "coerced participation at the individual level",
     "a referendum on a policy question"], ans=0,
   why="EK DEM-1.A.2 distinguishes oppositional behavior that seeks to change governmental policies from behavior that seeks to overthrow the regime, and amending a statute through petitions and legislators is the first. EK PAU-1.A.2's separation of government from regime is the same boundary."),
 dict(q="A chief executive whose bill has been rejected by the legislature puts the same question directly to voters and treats their approval as authority to proceed. Which of the framework's reasons for referenda does this illustrate?",
   choices=[
     "allowing a chief executive to bypass the legislature",
     "promoting democratic policy making",
     "obliging citizens to make a difficult and potentially unpopular decision",
     "gathering input in order to enhance legitimacy in an authoritarian regime",
     "applying a check on the judiciary"], ans=0,
   why="EK DEM-1.A.5 names allowing a chief executive to bypass the legislature among the reasons referenda are used, and the scenario is that reason exactly. The framework lists it alongside more favorable reasons without endorsing any of them."),
 dict(q="A government facing a choice between deep spending cuts and higher taxes puts both options to a national vote. Which of the framework's reasons for referenda does this illustrate?",
   choices=[
     "obliging citizens to make difficult and potentially unpopular decisions on public policy issues",
     "allowing a chief executive to bypass the legislature",
     "promoting democratic policy making by devolving powers",
     "intimidating the opposition",
     "certifying the results of a previous election"], ans=0,
   why="EK DEM-1.A.5 names obliging citizens to make difficult and potentially unpopular decisions on public policy issues among the reasons referenda are used. Putting two unwelcome options to voters transfers the choice rather than the initiative."),
 dict(q="In a country where opposition candidates are barred from the ballot and petitions are ignored, some citizens turn to violence. Which framework claim does this most directly illustrate?",
   choices=[
     "that violent political behavior becomes more likely when citizens feel conventional options are ineffective or unavailable",
     "that political participation can be voluntary or coerced",
     "that formal participation can be encouraged across regime types",
     "that referenda allow citizens to vote directly on policy questions",
     "that regime-supportive behavior can occur under state direction"], ans=0,
   why="EK DEM-1.A.3 names citizens feeling that more conventional options for political participation are ineffective or unavailable among the conditions making violent political behavior more likely, and the scenario supplies both halves, the barred ballot and the ignored petition."),
 dict(q="The table reports hypothetical election figures for three countries. Which record best fits the framework's description of participation used to give an illusion of influence?",
   table=_T_TURN,
   choices=[
     "Country P, with the highest turnout, the smallest share of contested seats, and the largest share of voters saying voting is required",
     "Country Q, with the lowest turnout but every seat contested",
     "Country R, which is between the other two on every measure",
     "None of the three, since high turnout always indicates genuine influence",
     "All three equally, since each held an election"], ans=0,
   why="EK DEM-1.A.4 states that authoritarian regimes are more likely to use citizen participation to intimidate opposition or give an illusion of influence, and EK DEM-1.B.1 adds that in many such elections there are few if any opposition candidates. Very high turnout with almost no contested seats and widespread compulsion is that combination."),
 dict(q="Using the same table, which record best fits the framework's description of elections held to allow citizen control of the policy-making process?",
   table=_T_TURN,
   choices=[
     "Country Q, where every seat is contested by more than one candidate and almost no voters describe voting as required",
     "Country P, where turnout is highest",
     "Country R, where turnout is second highest",
     "None of the three, since citizen control cannot be observed in election data",
     "Both Country P and Country Q, since each has high turnout"], ans=0,
   why="EK DEM-1.A.4 states that democratic regimes hold elections to allow citizen control of the policy-making process, and EK DEM-1.B.1 makes how open and competitive elections are the thing that decides how much impact citizens have. Turnout alone does not, which is why the highest-turnout row is not the key."),
 dict(q="According to the same table, the gap between the largest and smallest shares of seats contested by more than one candidate is",
   table=_T_TURN,
   choices=[
     "89 percentage points",
     "63 percentage points",
     "26 percentage points",
     "31 percentage points",
     "100 percentage points"], ans=0,
   why="Subtracting the smallest figure in that column from the largest gives the gap. The alternatives are the gaps between other pairs in the same column, the corresponding gap in the turnout column, and the largest single value read as a difference."),
 dict(q="The table reports a hypothetical sample of participation episodes by form. Which form shows episodes at both ends of the range the framework describes?",
   table=_T_PART,
   choices=[
     "street protest, which records episodes aimed at changing policy and episodes aimed at overthrowing the regime",
     "voting in a national election, which records the most episodes overall",
     "petition and lobbying, which records the most episodes aimed at changing policy after voting",
     "armed insurgency, which records the fewest episodes overall",
     "no form in the table records episodes with more than one aim"], ans=0,
   why="EK DEM-1.A.2 describes oppositional behavior as seeking to change governmental policies OR to overthrow the regime, which are the two ends of its range. Only one row of the table records episodes in both of those columns."),
 dict(q="According to the same table, the total number of episodes recorded across all four forms is",
   table=_T_PART,
   choices=[
     "267",
     "211",
     "147",
     "206",
     "120"], ans=0,
   why="Adding the episode column across all four rows gives the total. The alternatives arise from dropping a row, from adding a different column, and from reading the largest single row as though it were the total."),
 dict(q="Reading each row of the same table as a proportion rather than a count, which conclusion is best supported?",
   table=_T_PART,
   choices=[
     "As the form of participation becomes less conventional, the share of episodes aimed at overthrowing the regime rises",
     "Every form of participation in the table includes episodes aimed at overthrowing the regime",
     "No form of participation in the table includes episodes aimed at changing policy",
     "The form with the most episodes also has the largest share aimed at overthrowing the regime",
     "The share of episodes aimed at overthrowing the regime is the same for every form"], ans=0,
   why="EK DEM-1.A.2 sets out a range from regime-supportive to regime-overthrowing behavior, and EK DEM-1.A.3 links violent behavior to conventional options being ineffective or unavailable. Reading each row as a proportion, that share is zero for the two most conventional forms and rises through the two least conventional."),
 dict(q="The table describes three hypothetical referenda. Which one was held for the reason the framework describes as allowing a chief executive to bypass the legislature?",
   table=_T_REF,
   choices=[
     "Referendum 2, held to let the chief executive settle a question the legislature had blocked",
     "Referendum 1, held to decide whether powers should be devolved to a regional assembly",
     "Referendum 3, held to oblige citizens to choose between two unpopular budget options",
     "None of the three, since the framework does not name that reason",
     "All three, since a referendum always bypasses the legislature"], ans=0,
   why="EK DEM-1.A.5 names allowing a chief executive to bypass the legislature among the reasons referenda are used, and one row states that reason directly. The other two rows state the framework's other two reasons, so all three are on its list."),
 dict(q="Using the same table, which referendum's subject matches one the framework says the United Kingdom has actually used a referendum to decide?",
   table=_T_REF,
   choices=[
     "Referendum 1, on whether powers should be devolved to a regional assembly",
     "Referendum 2, on a question the legislature had blocked",
     "Referendum 3, on a choice between two budget options",
     "None of the three, since the framework names no referendum subjects",
     "All three, since each concerns a policy question"], ans=0,
   why="EK DEM-1.A.5 states that the United Kingdom has used referenda to decide questions about the devolution of powers to regional assemblies, the separation and creation of an independent nation-state, and its withdrawal from the European Union. Only one row's subject is among those three."),
 dict(q="Which finding would best illustrate formal participation acting as a safety valve, in the framework's sense?",
   choices=[
     "Citizens with grievances direct them into petitions, hearings and elections rather than into disorder, and the government treats those channels as the place for such complaints",
     "The government bans all public assemblies",
     "Turnout at the most recent election was the highest ever recorded",
     "The legislature met for more days than in the previous year",
     "The state broadcaster increased its coverage of the governing party"], ans=0,
   why="EK DEM-1.A.4 names acting as a safety valve among the purposes for which formal participation can be encouraged across regime types, and EK DEM-1.A.3 explains what it releases pressure from, since violent behavior becomes more likely when conventional options are felt to be ineffective or unavailable."),
 dict(q="Which finding would most strongly support a claim that a regime uses participation to give an illusion of influence?",
   choices=[
     "Citizens vote in large numbers, but the range of candidates is fixed in advance and no policy has ever changed as a result of an election",
     "Citizens vote in large numbers and the governing party's vote share fell at the last election",
     "Citizens vote in large numbers and turnout has risen steadily",
     "Citizens vote in large numbers and the legislature meets frequently",
     "Citizens vote in large numbers and the country has more than one legal party"], ans=0,
   why="EK DEM-1.A.4 names giving an illusion of influence among the uses authoritarian regimes are more likely to make of participation, and EK DEM-1.B.1 states that in many such elections there are few if any opposition candidates and that governments often intervene to ensure preferred candidates win. Volume of voting without consequence is that pattern."),
 dict(q="Taking the framework's statements on political participation together, which summary is most accurate?",
   choices=[
     "Participation may be voluntary or coerced and individual or group, ranges from regime-supportive to regime-overthrowing, becomes more likely to turn violent when conventional options fail, is encouraged across regime types for four named purposes though for different ends, and includes referenda used for three named reasons",
     "Participation is always voluntary and always aimed at supporting the regime",
     "Participation is encouraged only in democratic regimes and only through elections",
     "Participation has no bearing on whether political behavior turns violent",
     "Referenda are the only form of participation the framework describes"], ans=0,
   why="EK DEM-1.A.1 supplies the two axes, EK DEM-1.A.2 the range of aims, EK DEM-1.A.3 the condition for violent behavior, EK DEM-1.A.4 the cross-regime encouragement with its four purposes and its regime-specific ends, and EK DEM-1.A.5 the referendum and its three reasons."),
]
