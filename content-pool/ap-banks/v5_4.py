# AP U.S. GOVERNMENT AND POLITICS 5.4 How and Why Political Parties Change and
# Adapt -- 30 questions
# CED V.1 (c) 2026, Unit 5 Political Participation.
# Learning objective 5.4.A: explain WHY AND HOW political parties CHANGE AND
# ADAPT.
# Suggested skill for this topic (CED p. 116): 4.B, source analysis -- explain
# how the ARGUMENT OR PERSPECTIVE IN THE SOURCE relates to political principles,
# institutions, processes, policies, and behaviors.
#
# Essential knowledge relied on:
#   EK 5.4.A.1 -- "Parties have adapted to CANDIDATE-CENTERED CAMPAIGNS where the
#     public focus is on the CHARACTERISTICS OF THE CANDIDATE AND NOT ON THE
#     PARTY. The role of parties in NOMINATING CANDIDATES HAS ALSO BEEN
#     WEAKENED."
#   EK 5.4.A.2 -- "Parties may adapt their POLICIES AND MESSAGING to appeal to
#     various DEMOGRAPHIC COALITIONS."
#   EK 5.4.A.3 -- "The structure of parties has been influenced by:
#       i.   CRITICAL ELECTIONS (elections in which there is a REALIGNMENT of
#            political party support among voters)
#       ii.  Campaign finance law
#       iii. Changes in communication and data management technology"
#   EK 5.4.A.4 -- "Parties use communication technology and voter data management
#     to DISSEMINATE, CONTROL, AND CLARIFY political messages and ENHANCE
#     OUTREACH AND MOBILIZATION efforts."
#
# EK 5.4.A.1 MAKES TWO CLAIMS AND THE SECOND IS THE ONE THAT VANISHES. The first
# is about where public attention sits -- on the candidate's characteristics AND
# NOT ON THE PARTY. The second is a separate fact about party power: the role of
# parties in NOMINATING candidates HAS BEEN WEAKENED. A summary that keeps only
# the first has described a change in voters and missed a change in the
# institution, which is what LO 5.4.A is actually asking about. The first table
# in this module measures public focus and item 27 says outright that it does
# not bear on the nominating claim at all.
#
# THE DIRECTION OF THAT SECOND CLAIM IS FIXED: WEAKENED. It is the one place in
# this topic where the framework commits to a direction rather than listing
# influences, and reversing it is a clean falsehood that reads as a reasonable
# thing to say about parties. The verifier refuses any key that has the
# nominating role strengthened or unchanged.
#
# CRITICAL ELECTIONS CARRY A PARENTHETICAL DEFINITION and it is not "an
# important election". EK 5.4.A.3.i says an election in which there is a
# REALIGNMENT OF POLITICAL PARTY SUPPORT AMONG VOTERS. A close election, a
# consequential election and a high-turnout election are none of them critical
# elections in the framework's sense unless support realigns. Items 14 and 15
# turn on it.
#
# NO REAL CAMPAIGN, CANDIDATE OR YEAR IS NAMED. The CED's illustrative examples
# for this topic are two named campaign technology operations from one election
# year, and it marks them NOT REQUIRED. The same refusal as 3.13, 4.6 and 4.10,
# and here it also keeps a topic about how parties operate from turning into
# commentary on particular campaigns.
#
# Documents the CED attaches to 5.4.A (p. 27): Federalist No. 10, which is
# attached to 5.3.A through 5.7.A. Items 22 and 23 quote it verbatim.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere. No LaTeX:
# this is a prose subject and export_units.py no longer typesets US_GOV.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("5.4", "How and Why Political Parties Change and Adapt", 5)

_FOCUS = ("A hypothetical survey asked voters, in four successive election cycles, whether the "
          "candidate's own characteristics or the party label mattered more to their choice.")
_FOCUS_TABLE = dict(
    headers=["Election cycle", "Candidate characteristics mattered more (%)",
             "Party label mattered more (%)", "Both mattered equally (%)"],
    rows=[["Cycle 1", "38", "49", "13"],
          ["Cycle 2", "45", "42", "13"],
          ["Cycle 3", "53", "35", "12"],
          ["Cycle 4", "58", "30", "12"]])

_COALITION = ("A hypothetical study tracked the composition of one party's voters across two "
              "election cycles and counted the planks in its later platform addressing each "
              "group.")
_COALITION_TABLE = dict(
    headers=["Demographic group", "Share of the party's voters, earlier cycle (%)",
             "Share of the party's voters, later cycle (%)",
             "Planks addressing the group in the later platform"],
    rows=[["Group P", "34", "27", "3"],
          ["Group Q", "22", "31", "9"],
          ["Group R", "28", "24", "4"],
          ["Group S", "16", "18", "6"]])

QUESTIONS = [
 dict(q="According to the course framework, what have parties adapted to in CANDIDATE-CENTERED campaigns?",
   choices=[
     "A public focus on the characteristics of the candidate and not on the party",
     "A public focus on the party label rather than the candidate",
     "A requirement that parties select all nominees",
     "A prohibition on campaign advertising",
     "A shift of elections from states to the national government"], ans=0,
   why="EK 5.4.A.1 states this, and both halves of the framework's phrase matter: the focus is ON the candidate's characteristics AND NOT ON the party. It describes where public attention sits rather than what parties do."),

 dict(q="What SECOND claim does EK 5.4.A.1 make, beyond describing candidate-centered campaigns?",
   choices=[
     "That the role of parties in nominating candidates has been weakened",
     "That the role of parties in nominating candidates has been strengthened",
     "That parties no longer adopt platforms",
     "That parties no longer raise money",
     "That parties have been replaced by interest groups"], ans=0,
   why="EK 5.4.A.1's second sentence says the role of parties in nominating candidates has ALSO BEEN WEAKENED. It is a claim about the institution's power rather than about public attention, and it is the half a summary usually drops."),

 dict(q="Why does it matter that EK 5.4.A.1 makes two separate claims rather than one?",
   choices=[
     "Because the first describes a change in voters and the second a change in what parties are able to do, and evidence about one is not evidence about the other",
     "Because the two claims contradict each other",
     "Because only the first claim is course content",
     "Because the second claim applies only to third parties",
     "Because the two claims are different wordings of the same fact"], ans=0,
   why="A survey of what voters attend to bears on the first claim and says nothing about who controls nominations, which is the second. LO 5.4.A asks how parties change and adapt, so the institutional claim is at least as much the point as the attitudinal one."),

 dict(q="In which direction does EK 5.4.A.1 say the role of parties in nominating candidates has moved?",
   choices=[
     "It has been weakened",
     "It has been strengthened",
     "It has been unchanged",
     "It has been transferred to the courts",
     "The framework does not say"], ans=0,
   why="EK 5.4.A.1's own word is WEAKENED. It is one of the few places in this topic where the framework commits to a direction rather than listing influences that may operate either way."),

 dict(q="A party organization finds that a candidate it did not favor has won its nomination through a primary. How does this relate to EK 5.4.A.1?",
   choices=[
     "It illustrates the weakened role of parties in nominating candidates that the framework describes",
     "It illustrates a strengthened party role in nominations",
     "It illustrates a candidate-centered campaign but not the nominating claim",
     "It contradicts the framework, which says parties control all nominations",
     "It concerns campaign finance rather than nominations"], ans=0,
   why="EK 5.4.A.1's second sentence is about the party's role in nominating candidates, and a nomination decided against the organization's preference is that role weakened. EK 5.8.A.1.ii names open and closed primaries among the processes affecting outcomes."),

 dict(q="A candidate builds a personal campaign organization, raises money independently, and advertises without reference to the party label. Which part of EK 5.4.A.1 does this illustrate?",
   choices=[
     "The candidate-centered campaign, in which the public focus is on the candidate rather than the party",
     "The strengthened nominating role of parties",
     "The party platform function of EK 5.3.B.1.ii",
     "The committee systems in legislatures",
     "None of it, since the candidate is running under a party label"], ans=0,
   why="EK 5.4.A.1 describes campaigns in which the focus is on the characteristics of the candidate and not on the party, and a campaign built around the candidate's own organization and message is that description applied. Running under a label does not make a campaign party-centered."),

 dict(q="How does EK 5.4.A.1's account of candidate-centered campaigns relate to EK 5.3.B.1's list of party functions?",
   choices=[
     "It describes a change in the setting in which those functions are performed, including a weakening of the candidate recruitment and nomination role",
     "It states that parties no longer perform any of those functions",
     "It states that the functions have been transferred to interest groups",
     "It concerns only the committee systems in legislatures",
     "The two statements are unrelated"], ans=0,
   why="EK 5.3.B.1 lists candidate recruitment and campaign management among party functions, and EK 5.4.A.1 says the nominating role has been weakened and the public focus has moved to candidates. The functions remain on the list; the conditions under which parties perform them have changed."),

 dict(q="Which of the following would be evidence for EK 5.4.A.1's SECOND claim rather than its first?",
   choices=[
     "A finding about who in practice determines which candidates appear on a general election ballot",
     "A survey of what voters say mattered most in their choice",
     "A count of how often candidates appear in advertising",
     "A measure of how many voters can name their party's platform",
     "A tally of party membership over time"], ans=0,
   why="The second claim concerns the party's role in nominating candidates, so evidence for it has to be about who controls nominations. The other four options all measure public attention or attachment, which bears on the first claim."),

 dict(q="According to EK 5.4.A.2, what may parties adapt in order to appeal to various demographic coalitions?",
   choices=[
     "Their policies and messaging",
     "The rules governing federal elections",
     "The structure of Congress",
     "The dates on which primaries are held",
     "The requirements for voter registration"], ans=0,
   why="EK 5.4.A.2 names policies and messaging specifically. Both are things the party itself controls, unlike election rules, which EK 5.2.A.2 assigns to the states."),

 dict(q="EK 5.4.A.2 says parties MAY adapt their policies and messaging. What does that modal verb indicate?",
   choices=[
     "That such adaptation is something parties can do rather than something the framework says always happens",
     "That such adaptation is required by law",
     "That such adaptation has never occurred",
     "That only one party is capable of it",
     "That adaptation happens automatically without any decision"], ans=0,
   why="MAY ADAPT states a possibility rather than a regularity, so the framework identifies a strategy available to parties without claiming how often it is used. Several statements in this topic are hedged the same way."),

 dict(q="A party revises its platform and changes how it presents its positions in order to win support from a group whose share of the electorate is growing. Which framework statement does this illustrate?",
   choices=[
     "EK 5.4.A.2's statement that parties may adapt their policies and messaging to appeal to various demographic coalitions",
     "EK 5.4.A.1's statement about candidate-centered campaigns",
     "EK 5.4.A.3's list of influences on party structure",
     "EK 5.4.A.4's account of communication technology",
     "EK 5.3.A.1's definition of a linkage institution"], ans=0,
   why="The scenario changes both policies and messaging and aims at a demographic group, which is EK 5.4.A.2's statement in full. The other options concern public focus, party structure, technology, and the definition of a linkage institution."),

 dict(q="What is a DEMOGRAPHIC COALITION, in the sense EK 5.4.A.2 uses the term?",
   choices=[
     "A combination of demographic groups whose support a party seeks to assemble",
     "A formal alliance between two political parties",
     "A committee within a legislature",
     "A group of states that vote together",
     "An organization that files amicus curiae briefs"], ans=0,
   why="EK 5.4.A.2 pairs demographic coalitions with the policies and messaging a party uses to appeal to them, so the term picks out the combination of groups a party is trying to hold together. A coalition of parties and a legislative committee are different things entirely."),

 dict(q="According to EK 5.4.A.3, what three things have influenced the STRUCTURE of parties?",
   choices=[
     "Critical elections, campaign finance law, and changes in communication and data management technology",
     "Party platforms, candidate recruitment, and campaign management",
     "Voter turnout, political efficacy, and demographics",
     "Interest groups, elections, and media",
     "Open primaries, closed primaries, and caucuses"], ans=0,
   why="EK 5.4.A.3 lists exactly these three. Its subject is the STRUCTURE of parties rather than their functions, which EK 5.3.B.1 lists separately."),

 dict(q="According to the course framework, what is a CRITICAL ELECTION?",
   choices=[
     "An election in which there is a realignment of political party support among voters",
     "An election decided by a very small margin",
     "An election in which turnout is unusually high",
     "An election that determines control of a legislature",
     "An election held during a national emergency"], ans=0,
   why="EK 5.4.A.3.i's parenthesis defines a critical election by a REALIGNMENT of political party support among voters. Closeness, turnout and consequence are all features an election may have without any realignment occurring."),

 dict(q="An election is decided by a fraction of a percentage point and draws record turnout, but the groups supporting each party afterward are the same as before. Is it a critical election in the framework's sense?",
   choices=[
     "No, because no realignment of political party support among voters occurred",
     "Yes, because the margin was small",
     "Yes, because turnout was high",
     "Yes, because every close election is critical",
     "The framework does not define the term"], ans=0,
   why="EK 5.4.A.3.i's definition turns on a realignment of party support, and the stem states that the pattern of support did not change. Margin and turnout are not part of the framework's definition."),

 dict(q="Why does EK 5.4.A.3 list CAMPAIGN FINANCE LAW among the influences on party structure?",
   choices=[
     "Because rules about how money may be raised and spent shape how a party organizes itself to do so",
     "Because campaign finance law determines who may vote",
     "Because campaign finance law sets party platforms",
     "Because campaign finance law establishes legislative committees",
     "Because campaign finance law abolished political parties"], ans=0,
   why="EK 5.4.A.3's subject is the structure of parties, and the law governing fundraising is a constraint an organization builds itself around. Topic 5.11 takes up campaign finance in its own right."),

 dict(q="According to EK 5.4.A.4, what do parties use communication technology and voter data management to do?",
   choices=[
     "Disseminate, control, and clarify political messages, and enhance outreach and mobilization efforts",
     "Register voters and count ballots",
     "Draft and enact legislation",
     "Appoint judges and confirm nominees",
     "Set the dates of primary elections"], ans=0,
   why="EK 5.4.A.4 names all five purposes: three verbs applied to messages and two to outreach and mobilization. Registering voters and counting ballots are functions of state governments under EK 5.2.A.2."),

 dict(q="Three of the purposes EK 5.4.A.4 names apply to political messages. What are they?",
   choices=[
     "Disseminating, controlling, and clarifying them",
     "Drafting, amending, and repealing them",
     "Funding, auditing, and reporting them",
     "Translating, printing, and mailing them",
     "Testing, polling, and rejecting them"], ans=0,
   why="EK 5.4.A.4's three verbs for messages are disseminate, control and clarify. CONTROL is the one most easily lost, and it is the purpose that distinguishes managing a message from merely sending it."),

 dict(q="How does EK 5.4.A.4 relate to EK 5.4.A.3's third influence on party structure?",
   choices=[
     "EK 5.4.A.3 says technology has changed how parties are structured and EK 5.4.A.4 describes what parties use that technology for",
     "The two statements contradict each other",
     "EK 5.4.A.4 concerns state governments rather than parties",
     "EK 5.4.A.3 concerns technology and EK 5.4.A.4 concerns campaign finance",
     "The two statements describe the same fact in identical words"], ans=0,
   why="EK 5.4.A.3.iii names changes in communication and data management technology as an influence on party structure, and EK 5.4.A.4 lists the purposes to which parties put that same technology. One statement gives a cause of structural change and the other gives a use."),

 dict(q="A party invests in a system that records what its supporters care about and lets it send different messages to different supporters. Which two framework statements does this illustrate?",
   choices=[
     "EK 5.4.A.4's use of voter data management to control and clarify messages, and EK 5.4.A.2's adaptation of messaging to demographic coalitions",
     "EK 5.4.A.1's candidate-centered campaigns, and EK 5.3.A.1's definition of a linkage institution",
     "EK 5.4.A.3.i's critical elections, and EK 5.2.A.1's structural barriers",
     "EK 5.3.B.1.v's committee systems, and EK 5.4.A.3.ii's campaign finance law",
     "EK 5.2.A.4's factors influencing voter choice, and EK 5.1.B.1's models of voting behavior"], ans=0,
   why="The system is voter data management used to tailor messages, which is EK 5.4.A.4, and tailoring by what different supporters care about is EK 5.4.A.2's adaptation of messaging to coalitions. Both statements describe the same investment from different angles."),

 dict(q="Which of the following does EK 5.4.A.3 NOT state?",
   choices=[
     "Which of the three influences has changed party structure most",
     "That critical elections have influenced party structure",
     "That campaign finance law has influenced party structure",
     "That changes in communication and data management technology have influenced party structure",
     "That a critical election involves a realignment of party support among voters"], ans=0,
   why="EK 5.4.A.3 lists three influences and ranks none of them. Every other option restates part of the statement, including the parenthetical definition attached to its first item."),

 dict(q="Read the following excerpt.\n\n“A zeal for different opinions concerning religion, concerning government, and many other points… have, in turn, divided mankind into parties, inflamed them with mutual animosity, and rendered them much more disposed to vex and oppress each other than to co-operate for their common good.”\n—James Madison, Federalist No. 10, 1787\n\nHow does this passage relate to a topic about parties changing and adapting?",
   choices=[
     "It treats division into parties as arising from durable differences, which is why parties persist while adapting rather than dissolving",
     "It predicts that parties will disappear once opinions converge",
     "It describes the specific structure modern parties have adopted",
     "It argues that parties should be prohibited by law",
     "It has no bearing on political parties"], ans=0,
   why="Madison locates the division into parties in a zeal for different opinions, which is a standing condition rather than a passing one. The CED attaches Federalist No. 10 to 5.4.A, and read for what follows from it, a permanent source of division explains why parties adapt instead of vanishing."),

 dict(q="Read the following excerpt.\n\n“The latent causes of faction are thus sown in the nature of man; and we see them everywhere brought into different degrees of activity, according to the different circumstances of civil society.”\n—James Madison, Federalist No. 10, 1787\n\nWhat does the second half of this sentence add that bears on LO 5.4.A?",
   choices=[
     "That the same underlying causes produce different degrees and forms of political division as circumstances change, which is a reason organizations built on them would change too",
     "That the causes of faction disappear as circumstances change",
     "That civil society determines which party wins an election",
     "That factions exist only in large republics",
     "That the causes of faction can be removed by legislation"], ans=0,
   why="Madison's clause ties the ACTIVITY of the causes to the circumstances of civil society while the causes themselves stay constant. LO 5.4.A asks why and how parties change, and a constant cause operating in changing circumstances is an answer to the WHY."),

 dict(q="A commentator argues that parties have become weaker because voters now form attachments to individual candidates rather than to party labels. Which framework statement does this argument most closely track, and what does it leave out?",
   choices=[
     "It tracks EK 5.4.A.1's candidate-centered campaigns, and leaves out that the framework locates the weakening specifically in the role of parties in nominating candidates",
     "It tracks EK 5.4.A.2's demographic coalitions, and leaves out campaign finance law",
     "It tracks EK 5.4.A.3's critical elections, and leaves out realignment",
     "It tracks EK 5.4.A.4's use of technology, and leaves out mobilization",
     "It tracks nothing in the framework"], ans=0,
   why="The argument restates the first sentence of EK 5.4.A.1 and infers weakness from it, while the framework's own claim about weakening is the separate sentence about nominations. Skill 4.B asks how a source's argument relates to the framework, and this one relates by overlapping with part of it."),

 dict(q=_FOCUS + " Which conclusion is best supported by the data?",
   table=_FOCUS_TABLE,
   choices=[
     "The share saying candidate characteristics mattered more rose across the four cycles while the share saying the party label mattered more fell, and the two crossed between the first and second cycles",
     "The share saying the party label mattered more rose across the four cycles",
     "The two shares were equal in every cycle",
     "The share saying both mattered equally rose sharply",
     "The two shares crossed between the third and fourth cycles"], ans=0,
   why="The candidate column runs 38, 45, 53, 58 and the party column 49, 42, 35, 30. The party column leads in the first cycle only and trails from the second on, and the both-equally column stays between 12 and 13."),

 dict(q=_FOCUS + " Which statement in the course framework does this pattern most directly illustrate?",
   table=_FOCUS_TABLE,
   choices=[
     "EK 5.4.A.1's candidate-centered campaigns, in which the public focus is on the characteristics of the candidate and not on the party",
     "EK 5.4.A.1's statement that the role of parties in nominating candidates has been weakened",
     "EK 5.4.A.3.i's definition of a critical election",
     "EK 5.4.A.4's account of communication technology",
     "EK 5.3.A.1's definition of a linkage institution"], ans=0,
   why="Both data columns measure what voters said mattered to their choice, which is the public focus EK 5.4.A.1's first sentence describes. The second option is the other claim in that same statement, and this table does not measure it."),

 dict(q=_FOCUS + " A student uses this table as evidence that the role of parties in nominating candidates has been weakened. What is the most important limitation?",
   table=_FOCUS_TABLE,
   choices=[
     "Every column measures what voters said mattered to their choice, and none measures who controls nominations",
     "The table reports only one election cycle",
     "The table shows the party label column rising",
     "The table does not report the candidate characteristics column",
     "The table covers a single voter, so no share can be computed"], ans=0,
   why="EK 5.4.A.1 makes two claims and this table bears on the first, since its three columns are all about voter attention. The nominating claim is about who determines which candidates appear on a ballot, which nothing here measures."),

 dict(q=_COALITION + " Which conclusion is best supported by the data?",
   table=_COALITION_TABLE,
   choices=[
     "The group whose share of the party's voters grew most is also the group with the most planks addressing it in the later platform",
     "The group whose share fell most has the most planks addressing it",
     "Every group's share of the party's voters grew",
     "The four groups have equal numbers of planks addressing them",
     "The group with the largest share in the later cycle has the fewest planks"], ans=0,
   why="Group Q rises from 22 to 31 percent, the largest gain, and carries 9 planks, the most in the table. Group P falls from 34 to 27 and carries 3 planks, the fewest, and two groups fall while two rise."),

 dict(q=_COALITION + " Which statement in the course framework does this pattern most directly illustrate?",
   table=_COALITION_TABLE,
   choices=[
     "EK 5.4.A.2's statement that parties may adapt their policies and messaging to appeal to various demographic coalitions",
     "EK 5.4.A.1's statement about candidate-centered campaigns",
     "EK 5.4.A.3.ii's campaign finance law",
     "EK 5.3.A.1's definition of a linkage institution",
     "EK 5.2.A.2's influences on voter turnout"], ans=0,
   why="The table pairs the changing composition of a party's coalition with the content of its platform, which is EK 5.4.A.2's adaptation of policies and messaging to demographic coalitions. Platform planks are policies and messaging in the framework's sense."),

 dict(q=_COALITION + " What is the most important limitation of this data as evidence about how parties adapt?",
   table=_COALITION_TABLE,
   choices=[
     "The table reports the shift and the planks side by side but nothing about which came first, so it cannot show whether the platform followed the coalition or helped produce it",
     "The table does not report the number of planks",
     "The table covers only one election cycle",
     "The table shows no relationship between the two columns",
     "The table reports counts rather than shares for the coalition columns"], ans=0,
   why="Two cycles of shares and one count of planks are consistent with a party responding to a shift already under way and with a party producing the shift by campaigning for it. Skill 4.B asks how evidence relates to a claim, and this evidence is compatible with the claim running either way."),
]
