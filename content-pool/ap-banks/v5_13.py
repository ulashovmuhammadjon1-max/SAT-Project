# AP U.S. GOVERNMENT AND POLITICS 5.13 Changing Media -- 30 questions
# CED V.1 (c) 2026, Unit 5 Political Participation.
# Learning objective 5.13.A: explain how INCREASINGLY DIVERSE CHOICES OF MEDIA
# AND COMMUNICATION OUTLETS influence POLITICAL INSTITUTIONS AND BEHAVIOR.
# Suggested skill for this topic (CED p. 116): 2.D, SCOTUS Analysis -- EXPLAIN
# HOW A REQUIRED SUPREME COURT CASE RELATES TO A RELEVANT POLITICAL PRINCIPLE,
# INSTITUTION, PROCESS, POLICY, OR BEHAVIOR.
#
# Essential knowledge relied on, quoted from the framework:
#   EK 5.13.A.1 -- "POLITICAL PARTICIPATION is influenced by a variety of MEDIA
#     COVERAGE, ANALYSIS, AND COMMENTARY on political events."
#   EK 5.13.A.2 -- "The RAPIDLY INCREASING DEMAND for media and political
#     communications outlets from an IDEOLOGICALLY DIVERSE AUDIENCE have led to
#     DEBATES OVER MEDIA BIAS and the IMPACT OF MEDIA OWNERSHIP AND PARTISAN
#     NEWS SITES."
#   EK 5.13.A.3 -- "The NATURE OF DEMOCRATIC DEBATE and the LEVEL OF POLITICAL
#     KNOWLEDGE among citizens IS AFFECTED BY:
#       i.   INCREASED MEDIA CHOICES
#       ii.  IDEOLOGICALLY ORIENTED PROGRAMMING
#       iii. CONSUMER-DRIVEN MEDIA OUTLETS AND EMERGING TECHNOLOGIES THAT
#            REINFORCE EXISTING BELIEFS
#       iv.  UNCERTAINTY OVER THE CREDIBILITY OF NEWS SOURCES AND INFORMATION"
#
# TWO WORDS CARRY THIS ENTIRE TOPIC, AND BOTH ARE DELIBERATELY UNCOMMITTED.
#
# EK 5.13.A.2's noun is DEBATES. The framework says the growth of outlets has led
# to debates OVER media bias, ownership and partisan news sites. It does not say
# the media are biased, and it does not say they are not. A student arrives at
# this topic already holding a view, so a key that quietly settles the debate
# would pass every structural check and teach the settlement as course content.
#
# EK 5.13.A.3's verb is AFFECTED, with no direction attached. The framework says
# the nature of democratic debate and the level of political knowledge ARE
# AFFECTED by its four factors. It does not say raised, lowered, improved or
# degraded. Every popular account of this subject supplies a direction; the
# framework supplies none, and items 12 and 23 make that boundary the question.
#
# Both restraints are enforced by the verifier rather than left to care, because
# an item asserting a direction reads perfectly well and nothing else would
# notice.
#
# THIS TOPIC IS NOT TOPIC 5.12. EK 5.12.A.1's object is HOW CITIZENS ACQUIRE
# POLITICAL INFORMATION; EK 5.13.A.1's object is POLITICAL PARTICIPATION. The
# two statements share the word commentary and share nothing else, so item 3
# names the difference rather than leaving a student to collide with it.
#
# Required Supreme Court cases used for skill 2.D. The CED's cross-reference
# table attaches no case to 5.13.A specifically, so items 19 to 21 apply cases
# whose stated holdings reach the situations described, using the CED's own
# sentences and nothing beyond them:
#   NEW YORK TIMES CO. V. US (1971) -- "bolstered the freedom of the press
#     protections of the First Amendment, establishing a 'heavy presumption
#     against prior restraint' even in cases involving national security."
#   CITIZENS UNITED V. FEDERAL ELECTION COMMISSION (2010) -- "Political spending
#     by corporations, associations, and labor unions is a form of protected
#     speech under the First Amendment."
#
# The CED's optional reading for this topic is marked NOT REQUIRED, so nothing
# here is keyed to it.
#
# BOTH TABLES ARE HYPOTHETICAL and say so in the stem, and both report what
# respondents SAY rather than any property of an outlet. That distinction is the
# design of the second table: EK 5.13.A.2 is about debates, and a survey of
# opinion is evidence about a debate rather than a resolution of it.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere. No LaTeX:
# this is a prose subject and export_units.py no longer typesets US_GOV.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("5.13", "Changing Media", 5)

_SOURCES = ("A hypothetical survey grouped respondents by how many news sources they use "
            "regularly and reported, for each group, the share who can name their own "
            "representative in Congress, the share who took part in a political activity during "
            "the past year, and the share who say most of the sources they use share their own "
            "point of view.")
_SOURCES_TABLE = dict(
    headers=["Number of regular news sources", "Can name their own representative (%)",
             "Took part in a political activity (%)",
             "Say most sources share their own point of view (%)"],
    rows=[["No regular source", "27", "9", "44"],
          ["One regular source", "41", "18", "52"],
          ["Two or three regular sources", "58", "29", "61"],
          ["Four or more regular sources", "73", "44", "70"]])

_AUDIENCE = ("A hypothetical survey grouped respondents by the kind of outlet they mainly use "
             "and reported what each group says about media bias, about the ownership of the "
             "outlet they use, and about encountering views they disagree with.")
_AUDIENCE_TABLE = dict(
    headers=["Kind of outlet mainly used", "Say media bias is a serious problem (%)",
             "Say they can usually tell who owns their main outlet (%)",
             "Say they regularly encounter views they disagree with (%)"],
    rows=[["A general news outlet", "54", "47", "58"],
          ["An opinion oriented outlet", "79", "31", "24"],
          ["Social media feeds", "66", "12", "41"],
          ["A mix of several kinds", "49", "52", "71"]])

QUESTIONS = [
 dict(q="According to the course framework, what is influenced by a variety of media coverage, analysis, and commentary on political events?",
   choices=[
     "Political participation",
     "The number of seats each state holds in Congress",
     "The jurisdiction of the federal courts",
     "The length of a presidential term",
     "The procedures for amending the Constitution"], ans=0,
   why="EK 5.13.A.1 names political participation as what a variety of media output influences. The other options name features fixed by the Constitution rather than by anything the media do."),

 dict(q="Which three forms of media output does EK 5.13.A.1 name?",
   choices=[
     "Coverage, analysis, and commentary",
     "Advertising, endorsement, and polling",
     "Reporting, editing, and printing",
     "Broadcasting, streaming, and podcasting",
     "Interviews, debates, and press conferences"], ans=0,
   why="EK 5.13.A.1's phrase is a variety of media coverage, analysis, and commentary on political events, and the three differ in kind: what happened, what it means, and what should be thought of it. The framework names all three rather than reporting alone."),

 dict(q="An earlier topic states that agenda setting influences how citizens routinely acquire political information. What is the object of EK 5.13.A.1's statement instead?",
   choices=[
     "Political participation, meaning what citizens do rather than how they come by information",
     "The accuracy of the information citizens receive",
     "The number of outlets available to citizens",
     "The ownership structure of news organizations",
     "The constitutional protections available to publishers"], ans=0,
   why="EK 5.12.A.1's object is how citizens routinely acquire political information, while EK 5.13.A.1's object is political participation. The two statements share the word commentary and differ in what the media are said to influence."),

 dict(q="According to EK 5.13.A.2, the rapidly increasing demand for media and political communications outlets has led to what?",
   choices=[
     "Debates over media bias and the impact of media ownership and partisan news sites",
     "A federal requirement that outlets present opposing views",
     "A decline in the total number of news outlets",
     "A constitutional amendment governing broadcasting",
     "A single national standard for reporting on candidates"], ans=0,
   why="EK 5.13.A.2 states that the increased demand has led to debates over those three subjects. The framework reports that arguments have arisen, and it does not report how any of them was resolved."),

 dict(q="Whose demand does EK 5.13.A.2 identify as driving the growth in media and political communications outlets?",
   choices=[
     "An ideologically diverse audience",
     "The national committees of the two major parties",
     "Federal regulatory agencies",
     "Corporate owners acting without regard to audiences",
     "Candidates for federal office"], ans=0,
   why="EK 5.13.A.2's phrase is demand from an ideologically diverse audience, so the framework locates the driver in what audiences want rather than in a decision made by government or by owners. The diversity of the audience is part of the explanation for the diversity of outlets."),

 dict(q="A student writes that the framework states the media are biased. What is the most important correction?",
   choices=[
     "The framework states that debates over media bias have arisen, which reports a dispute rather than settling it",
     "The framework states that the media are not biased",
     "The framework does not mention media bias at all",
     "The framework states that only social media outlets are biased",
     "The framework states that bias was eliminated by increased competition"], ans=0,
   why="EK 5.13.A.2's noun is debates, and a debate over a question is not an answer to it. Reading the statement as a finding converts a description of an argument into a position within it."),

 dict(q="According to EK 5.13.A.3, which two things are affected by the four factors the framework lists?",
   choices=[
     "The nature of democratic debate and the level of political knowledge among citizens",
     "The number of candidates who file for office and the length of campaigns",
     "The rules of congressional procedure and the size of committees",
     "The jurisdiction of federal courts and the pace of litigation",
     "The apportionment of House seats and the drawing of district lines"], ans=0,
   why="EK 5.13.A.3 names democratic debate and the level of political knowledge among citizens as what its four factors affect. Both are properties of how citizens argue and what they know rather than features of any institution."),

 dict(q="Which four factors does EK 5.13.A.3 list?",
   choices=[
     "Increased media choices, ideologically oriented programming, consumer driven outlets and technologies that reinforce existing beliefs, and uncertainty over the credibility of news sources",
     "Newspaper circulation, broadcast licensing, cable subscription rates, and internet access",
     "Party identification, education, income, and age",
     "Campaign spending, incumbency, turnout, and district composition",
     "Editorial independence, professional training, fact checking, and corrections policy"], ans=0,
   why="EK 5.13.A.3 lists exactly those four, and they range from a count of options to a state of doubt. The other options name variables the framework discusses in other topics or does not discuss at all."),

 dict(q="EK 5.13.A.3 describes consumer driven media outlets and emerging technologies as doing what?",
   choices=[
     "Reinforcing existing beliefs",
     "Correcting inaccurate reports",
     "Requiring audiences to encounter opposing views",
     "Replacing all traditional outlets",
     "Setting the agenda for legislative committees"], ans=0,
   why="EK 5.13.A.3.iii's phrase is outlets and emerging technologies that reinforce existing beliefs, so reinforcement is what the framework attributes to them. The statement describes what such outlets do without saying whether the result is good or bad."),

 dict(q="EK 5.13.A.3 names uncertainty over what?",
   choices=[
     "The credibility of news sources and information",
     "The identity of the owners of each outlet",
     "The cost of subscribing to news services",
     "The dates on which elections will be held",
     "The number of outlets operating in a given market"], ans=0,
   why="EK 5.13.A.3.iv names uncertainty over the credibility of news sources and information. What the framework identifies is a state of doubt in the audience rather than a measured property of any source."),

 dict(q="Which of EK 5.13.A.3's four factors describes the content of what is broadcast rather than a number of options, a technology, or a state of doubt?",
   choices=[
     "Ideologically oriented programming",
     "Increased media choices",
     "Emerging technologies that reinforce existing beliefs",
     "Uncertainty over the credibility of news sources",
     "Consumer driven media outlets"], ans=0,
   why="EK 5.13.A.3.ii names ideologically oriented programming, which is a description of what a program contains. The other three factors describe how many options exist, what technologies do, and what audiences are unsure of."),

 dict(q="A student writes that the framework states increased media choices have raised the level of political knowledge among citizens. What is the most important correction?",
   choices=[
     "The framework says the level of political knowledge IS AFFECTED by increased media choices and does not say in which direction",
     "The framework says increased media choices have lowered the level of political knowledge",
     "The framework says the level of political knowledge is unaffected by media",
     "The framework says political knowledge is affected only by formal education",
     "The framework does not mention the level of political knowledge"], ans=0,
   why="EK 5.13.A.3's verb is affected, with no direction attached to any of its four factors. Supplying a direction the framework withholds is an addition to the course content rather than a reading of it."),

 dict(q="Learning objective 5.13.A says increasingly diverse choices of media and communication outlets influence what?",
   choices=[
     "Political institutions and behavior",
     "The text of the Constitution",
     "The boundaries of the states",
     "The number of federal courts",
     "The order of succession to the presidency"], ans=0,
   why="LO 5.13.A names political institutions and behavior as what diverse media choices influence, which pairs an effect on organizations with an effect on what people do. The other options name things no media development could alter."),

 dict(q="A viewer notices that the items an outlet recommends are consistently ones agreeing with views the viewer already holds. Which of EK 5.13.A.3's factors does this illustrate?",
   choices=[
     "Consumer driven outlets and emerging technologies that reinforce existing beliefs",
     "Uncertainty over the credibility of news sources",
     "Increased media choices, considered by itself",
     "Ideologically oriented programming produced by the outlet",
     "The nature of democratic debate"], ans=0,
   why="EK 5.13.A.3.iii names outlets and technologies that reinforce existing beliefs, and a recommendation shaped by what the viewer already accepts is that reinforcement in operation. Programming produced from an ideological standpoint is a separate factor in the same list."),

 dict(q="A reader encounters a report and cannot determine whether the site publishing it is reliable. Which of EK 5.13.A.3's factors does this illustrate?",
   choices=[
     "Uncertainty over the credibility of news sources and information",
     "Ideologically oriented programming",
     "Consumer driven outlets that reinforce existing beliefs",
     "Increased media choices, considered by itself",
     "The level of political knowledge among citizens"], ans=0,
   why="EK 5.13.A.3.iv names uncertainty over the credibility of news sources and information, and the reader's difficulty is exactly that uncertainty. The factor concerns the reader's inability to judge rather than any established fact about the site."),

 dict(q="A channel's programs argue consistently from one ideological standpoint and are produced for an audience that shares it. Which of EK 5.13.A.3's factors does this illustrate?",
   choices=[
     "Ideologically oriented programming",
     "Uncertainty over the credibility of news sources",
     "Increased media choices, considered by itself",
     "The nature of democratic debate",
     "The level of political knowledge among citizens"], ans=0,
   why="EK 5.13.A.3.ii names ideologically oriented programming, and consistent argument from one standpoint is what orients programming ideologically. The number of channels available is a different factor in the same list."),

 dict(q="Commentators disagree about whether it matters that one company owns several of the outlets in a market. Which framework statement names that disagreement?",
   choices=[
     "EK 5.13.A.2, which names debates over the impact of media ownership",
     "EK 5.13.A.1, which concerns influences on political participation",
     "EK 5.13.A.3, which lists factors affecting democratic debate",
     "Learning objective 5.13.A, which concerns diverse choices of outlets",
     "The framework's statement about agenda setting"], ans=0,
   why="EK 5.13.A.2 names debates over media bias and the impact of media ownership and partisan news sites, and the scenario is an argument about ownership. The framework records that the argument exists rather than deciding it."),

 dict(q="The suggested skill for this topic asks students to do what?",
   choices=[
     "Explain how a required Supreme Court case relates to a relevant political principle, institution, process, policy, or behavior",
     "Explain how a required Supreme Court case compares with a case that is not required",
     "Describe the facts and issue of a required Supreme Court case",
     "Explain the limitations of a visual representation of data",
     "Respond to opposing perspectives with rebuttal or refutation"], ans=0,
   why="Skill 2.D is stated in the CED in exactly those terms, and the CED assigns it to this topic. Comparing a required case with a non-required one and describing a case's facts are separate skills in the same category."),

 dict(q="In New York Times Co. v. United States (1971), the Supreme Court bolstered freedom of the press, establishing a heavy presumption against prior restraint even in cases involving national security. How does that holding relate to the growth in outlets EK 5.13.A.2 describes?",
   choices=[
     "The variety of outlets is not something government screens in advance, so disputes about what they publish are argued out among citizens rather than settled before publication",
     "The holding requires government to license each new outlet",
     "The holding requires outlets to present opposing viewpoints",
     "The holding limits the number of outlets that may operate",
     "The holding gives government the power to decide which outlets are credible"], ans=0,
   why="A heavy presumption against stopping publication in advance means the decision to publish rests with each outlet, which is the condition under which a rapidly growing and ideologically varied set of outlets can exist. EK 5.13.A.2 records the debates that follow, and the case explains why they are debates rather than administrative determinations."),

 dict(q="A citizen who is unsure whether an online report is credible proposes that government resolve such doubts by stopping unreliable reports before they appear. Which required Supreme Court case bears most directly on the proposal?",
   choices=[
     "New York Times Co. v. United States (1971), because a heavy presumption runs against stopping publication in advance",
     "Shaw v. Reno (1993), because it concerned the use of race in drawing districts",
     "United States v. Lopez (1995), because it concerned the reach of the commerce power",
     "McDonald v. Chicago (2010), because it concerned the right to keep and bear arms",
     "Wisconsin v. Yoder (1972), because it concerned compulsory school attendance"], ans=0,
   why="The proposal is that government block material before publication, and the CED states the holding as a heavy presumption against exactly that, even where national security is asserted. EK 5.13.A.3.iv names the citizen's uncertainty as a real feature of the current media environment, and the case explains why this particular remedy for it faces a heavy burden."),

 dict(q="A state law forbids a corporation that owns a news website from spending its own funds on advertisements supporting candidates. Which required Supreme Court case bears most directly on the law?",
   choices=[
     "Citizens United v. Federal Election Commission (2010), because political spending by corporations was held to be protected speech",
     "New York Times Co. v. United States (1971), because it concerned an attempt to stop publication in advance",
     "Gideon v. Wainwright (1963), because it concerned the right to counsel",
     "Tinker v. Des Moines Independent Community School District (1969), because it concerned symbolic expression in schools",
     "Marbury v. Madison (1803), because it established judicial review"], ans=0,
   why="The law reaches a corporation's own spending on election advertising, which is the situation the CED's stated holding addresses. The other case involving the press concerns blocking publication rather than restricting spending, which is a different act by government."),

 dict(q="EK 5.13.A.2 attributes the growth of outlets to RAPIDLY INCREASING DEMAND. What does that attribution rule out as the framework's explanation?",
   choices=[
     "That the growth was directed by government policy or by a decision of any single owner",
     "That audiences differ from one another ideologically",
     "That debates about media bias have arisen",
     "That partisan news sites exist",
     "That the number of outlets has grown"], ans=0,
   why="EK 5.13.A.2 locates the cause in demand from an ideologically diverse audience, so the framework's explanation runs from what audiences want to what gets produced. Every other option restates something the same statement asserts."),

 dict(q="Which of the following does the course framework NOT state in this topic?",
   choices=[
     "Whether increased media choices have raised or lowered the level of political knowledge",
     "That political participation is influenced by media coverage, analysis, and commentary",
     "That debates have arisen over media bias and the impact of media ownership",
     "That some outlets and technologies reinforce existing beliefs",
     "That uncertainty exists over the credibility of news sources and information"], ans=0,
   why="EK 5.13.A.3 says the level of political knowledge is affected by its four factors and stops there, attaching no direction to the effect. Every other option restates part of one of this topic's three statements."),

 dict(q="Why is this topic titled CHANGING MEDIA rather than simply THE MEDIA?",
   choices=[
     "Because its statements concern growth and diversification over time, from increasing demand to increased choices, rather than a fixed description of the media",
     "Because its statements concern only outlets founded in the last decade",
     "Because its statements concern changes in the law governing the press",
     "Because its statements concern changes in who owns the Constitution's protections",
     "Because its statements concern the replacement of all older outlets"], ans=0,
   why="Learning objective 5.13.A speaks of increasingly diverse choices, EK 5.13.A.2 of rapidly increasing demand, and EK 5.13.A.3 of increased media choices, so every statement in the topic is about a direction of change. The preceding topic states what the media do rather than how the set of them has grown."),

 dict(q=_SOURCES + " Which conclusion is best supported by the data?",
   table=_SOURCES_TABLE,
   choices=[
     "All three measures rise as the number of regular sources rises, including the share saying most of their sources share their own point of view",
     "The share who can name their own representative falls as the number of sources rises",
     "The share taking part in a political activity is unchanged across the groups",
     "The share saying most of their sources share their own point of view falls as the number of sources rises",
     "Respondents with no regular source lead on every measure"], ans=0,
   why="Naming a representative runs from 27 to 73 percent, taking part in a political activity from 9 to 44 percent, and saying most sources share one's own point of view from 44 to 70 percent. All three columns rise together, which is what makes the last column worth reporting alongside the first two."),

 dict(q=_SOURCES + " Which two of EK 5.13.A.3's factors do the first and third data columns bear on together?",
   table=_SOURCES_TABLE,
   choices=[
     "The level of political knowledge, and outlets and technologies that reinforce existing beliefs",
     "Ideologically oriented programming, and uncertainty over credibility",
     "Uncertainty over credibility, and the nature of democratic debate",
     "Media ownership, and partisan news sites",
     "Media coverage, and analysis of political events"], ans=0,
   why="Naming one's own representative is a measure of political knowledge, which EK 5.13.A.3 names as affected, and saying most of one's sources agree with oneself is the reinforcement EK 5.13.A.3.iii describes. Ownership and partisan sites belong to the framework's separate statement about debates."),

 dict(q=_SOURCES + " A student concludes from this table that the framework predicts more media choices will raise political knowledge. What is the most important correction?",
   table=_SOURCES_TABLE,
   choices=[
     "The framework says political knowledge is AFFECTED without saying in which direction, and this table's third column rises alongside the first",
     "The framework says political knowledge falls as media choices increase",
     "The table shows political knowledge falling as the number of sources rises",
     "The framework makes no statement about political knowledge",
     "The table reports nothing about political participation"], ans=0,
   why="EK 5.13.A.3 attaches no direction to the effect of its four factors, so a single hypothetical pattern cannot be a prediction of the framework. The same table shows self reinforcing source selection rising in step with knowledge, which is why a one directional reading of it is unsafe."),

 dict(q=_AUDIENCE + " Which conclusion is best supported by the data?",
   table=_AUDIENCE_TABLE,
   choices=[
     "The group mainly using an opinion oriented outlet is the most likely to say media bias is a serious problem and the least likely to say it regularly encounters views it disagrees with",
     "The group mainly using an opinion oriented outlet is the least likely to say media bias is a serious problem",
     "The group using a mix of several kinds is the least likely to say it regularly encounters views it disagrees with",
     "Every group reports the same ability to tell who owns its main outlet",
     "The group mainly using social media feeds leads on every measure"], ans=0,
   why="The opinion oriented group stands at 79 percent on bias, the highest in that column, and at 24 percent on encountering disagreement, the lowest in that column. The mixed group leads on encountering disagreement at 71 percent and on identifying ownership at 52 percent."),

 dict(q=_AUDIENCE + " Which framework statement do the first two data columns bear on?",
   table=_AUDIENCE_TABLE,
   choices=[
     "EK 5.13.A.2, which names debates over media bias and the impact of media ownership",
     "EK 5.13.A.1, which names influences on political participation",
     "EK 5.13.A.3's factor of uncertainty over the credibility of news sources",
     "Learning objective 5.13.A's reference to political institutions",
     "The framework's statement about how citizens acquire political information"], ans=0,
   why="EK 5.13.A.2 names media bias and the impact of media ownership among the subjects the increased demand for outlets has led people to argue about, and the two columns report what respondents say about each. The columns peak in different groups, which is what two separate debates look like in data."),

 dict(q=_AUDIENCE + " A student concludes from this table that the media are biased. What is the most important correction?",
   table=_AUDIENCE_TABLE,
   choices=[
     "Every column reports what respondents SAY, so the table is evidence about a debate rather than a finding about any outlet's content",
     "The table shows that the media are not biased",
     "The table measures the content of each outlet directly",
     "The framework states that the media are biased, so the conclusion is unnecessary",
     "The table reports nothing about media bias"], ans=0,
   why="Each column of this table begins with what a group says, which makes it a record of opinion rather than a measurement of any outlet. EK 5.13.A.2 names debates over media bias, and a survey of what people believe about a debate is evidence within it rather than a resolution of it."),
]
