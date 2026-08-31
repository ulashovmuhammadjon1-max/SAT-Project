# AP U.S. GOVERNMENT AND POLITICS 5.12 The Media -- 30 questions
# CED V.1 (c) 2026, Unit 5 Political Participation.
# Learning objective 5.12.A: explain the MEDIA'S ROLE AS A LINKAGE INSTITUTION.
# Suggested skill for this topic (CED p. 116): 5.D, argumentation -- RESPOND TO
# OPPOSING OR ALTERNATE PERSPECTIVES WITH REBUTTAL OR REFUTATION.
#
# Essential knowledge relied on, quoted from the framework:
#   EK 5.12.A.1 -- "AGENDA SETTING takes place when TRADITIONAL NEWS MEDIA, NEW
#     COMMUNICATION TECHNOLOGIES, and ADVANCES IN SOCIAL MEDIA influence HOW
#     CITIZENS ROUTINELY ACQUIRE POLITICAL INFORMATION, including NEWS EVENTS,
#     INVESTIGATIVE JOURNALISM, ELECTION COVERAGE, and POLITICAL COMMENTARY."
#   EK 5.12.A.2 -- "The media's USE OF POLLING RESULTS to convey POPULAR LEVELS
#     OF TRUST AND CONFIDENCE IN GOVERNMENT CAN AFFECT ELECTIONS by turning such
#     events into 'HORSE RACES' based more on POPULARITY and factors other than
#     QUALIFICATIONS AND PLATFORMS OF CANDIDATES."
#
# THE COURSE DEFINES AGENDA SETTING TWICE, AND THE TWO DEFINITIONS ARE NOT THE
# SAME. EK 2.7.A.1.ii makes the State of the Union and the bully pulpit tools
# for agenda setting, with the effect defined as influencing public views about
# WHICH POLICIES ARE MOST IMPORTANT; there the president is the actor and the
# media the instrument. EK 5.12.A.1 defines agenda setting as media influence on
# HOW CITIZENS ROUTINELY ACQUIRE POLITICAL INFORMATION; here the media are the
# actor and the object is the route rather than the ranking. A module on this
# topic that reaches for the familiar definition is answering topic 2.7's
# question, so item 6 makes the difference the question and the verifier refuses
# any key that defines agenda setting as telling citizens what to think.
#
# EK 5.12.A.2'S VERB IS "CAN AFFECT", AND THAT IS THE WHOLE CAUTION OF THE
# TOPIC. The framework states a possible effect of horse race coverage, not an
# established one, and it names precisely what such coverage displaces:
# QUALIFICATIONS AND PLATFORMS. Public commentary on this subject is confident
# in both directions and the framework is confident in neither, so items 11 and
# 24 turn on the modal and the verifier refuses any key asserting that poll
# coverage determines, decides or guarantees an election result.
#
# Required Supreme Court case the CED cross-references to 5.12.A (p. 33): NEW
# YORK TIMES CO. V. US (1971). CED holding (p. 30): the case "bolstered the
# freedom of the press protections of the First Amendment, establishing a 'heavy
# presumption against prior restraint' even in cases involving national
# security." Topic 3.4 owns the doctrine itself and asks thirty questions about
# it; item 21 here asks only what the holding means for the influence EK
# 5.12.A.1 attributes to the media, which is a question 3.4 does not ask.
#
# The CED's optional readings for this topic -- a blog and a foundation report
# -- are marked NOT REQUIRED, so nothing here is keyed to them.
#
# BOTH TABLES ARE HYPOTHETICAL and say so in the stem. No figure here describes
# a real survey, outlet or election. There is no sympy in this subject, and a
# number attributed to a real contest is a claim nobody downstream could check.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere. No LaTeX:
# this is a prose subject and export_units.py no longer typesets US_GOV.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("5.12", "The Media", 5)

_INFO = ("A hypothetical survey asked respondents whether they encounter each kind of political "
         "information in a typical week, and, for those who do, whether they encounter it mainly "
         "through traditional news media or mainly through social media and other new "
         "communication technologies.")
_INFO_TABLE = dict(
    headers=["Kind of political information", "Encountering it in a typical week (%)",
             "Mainly through traditional news media (%)",
             "Mainly through social media or new technologies (%)"],
    rows=[["News events", "84", "46", "38"],
          ["Election coverage", "71", "39", "32"],
          ["Political commentary", "63", "21", "42"],
          ["Investigative journalism", "29", "19", "10"]])

_COVERAGE = ("A hypothetical study of one broadcaster's election segments divides every minute of "
             "coverage into three categories and reports the share falling in each during the "
             "four weeks before an election.")
_COVERAGE_TABLE = dict(
    headers=["Period", "Coverage of poll standings (%)",
             "Coverage of candidate qualifications (%)", "Coverage of candidate platforms (%)"],
    rows=[["Fourth week before the election", "22", "30", "48"],
          ["Third week before the election", "34", "27", "39"],
          ["Second week before the election", "47", "24", "29"],
          ["Final week before the election", "61", "20", "19"]])

QUESTIONS = [
 dict(q="According to the course framework, agenda setting takes place when the media influence what?",
   choices=[
     "How citizens routinely acquire political information",
     "Which candidates are permitted to appear on the ballot",
     "How many seats each state receives in the House of Representatives",
     "Which bills a congressional committee reports to the floor",
     "How federal agencies write their regulations"], ans=0,
   why="EK 5.12.A.1 defines agenda setting as media influence on how citizens routinely acquire political information. The object of the influence in the framework's sentence is the route by which information reaches people."),

 dict(q="Which three kinds of media does EK 5.12.A.1 name as taking part in agenda setting?",
   choices=[
     "Traditional news media, new communication technologies, and advances in social media",
     "Newspapers, magazines, and books",
     "Broadcast networks, cable channels, and satellite radio",
     "Party newsletters, campaign advertisements, and direct mail",
     "Government press offices, agency websites, and official records"], ans=0,
   why="EK 5.12.A.1 lists exactly those three, and the list ranges from the long established to the recent. The framework does not narrow the statement to any particular outlet or platform."),

 dict(q="EK 5.12.A.1 says political information includes which four things?",
   choices=[
     "News events, investigative journalism, election coverage, and political commentary",
     "Party platforms, nominating conventions, primaries, and caucuses",
     "Polling, redistricting, apportionment, and reapportionment",
     "Bills, hearings, markups, and floor votes",
     "Editorials, advertisements, endorsements, and letters"], ans=0,
   why="EK 5.12.A.1's list names those four, and they differ in kind: one is reporting of what happened, one is reporting that had to be dug for, one is coverage of a contest and one is opinion about it. The other options list material the framework places in other topics."),

 dict(q="What does the word ROUTINELY add to EK 5.12.A.1's statement?",
   choices=[
     "It makes the statement about the ordinary repeated ways information is acquired rather than about any single occasion",
     "It restricts the statement to information acquired during election years",
     "It means citizens acquire information without any effort",
     "It means the same information reaches every citizen",
     "It restricts the statement to information supplied by the government"], ans=0,
   why="EK 5.12.A.1 concerns how citizens routinely acquire political information, and a habit is what a routine is. Influence over a habit is a different and larger claim than influence over one occasion."),

 dict(q="A student writes that agenda setting, as this topic defines it, means the media tell citizens what opinions to hold. What is the most important correction?",
   choices=[
     "The framework's sentence is about how citizens acquire political information, not about what conclusions they reach from it",
     "The framework says the media have no influence of any kind",
     "The framework says agenda setting is performed only by government officials",
     "The framework says citizens acquire no political information from the media",
     "The framework says opinions are formed entirely by family and school"], ans=0,
   why="EK 5.12.A.1's object is how citizens routinely acquire political information, which concerns the route rather than the conclusion. The framework makes no claim about what citizens then believe."),

 dict(q="An earlier topic in this course defines agenda setting as a president's influence over which policies the public sees as most important. How does EK 5.12.A.1's use of the term differ?",
   choices=[
     "In the earlier statement the president is the actor and the media a tool; here the media are the actor and the object is how citizens acquire information",
     "The two statements define the term identically",
     "The earlier statement concerns the media and this one concerns the president",
     "Neither statement identifies who does the agenda setting",
     "The earlier statement concerns elections and this one concerns legislation"], ans=0,
   why="EK 2.7.A.1.ii names the State of the Union and the bully pulpit as tools a president uses to influence which policies the public sees as most important, while EK 5.12.A.1 makes the media themselves the influence and the route of acquisition the object. Using one course statement to answer a question about the other is the mistake this item exists to prevent."),

 dict(q="An earlier statement in this course lists media among the channels through which individuals communicate their preferences to policymakers, while EK 5.12.A.1 describes media influencing how citizens acquire information. What does holding both statements require of a student?",
   choices=[
     "Recognizing that the framework asserts both, so the media's role runs toward citizens as well as toward policymakers",
     "Choosing whichever of the two statements is more recent",
     "Treating the earlier statement as withdrawn by this one",
     "Concluding that the media are not a linkage institution",
     "Concluding that the framework contains no statement about the media and policymakers"], ans=0,
   why="EK 5.3.A.1 lists media among linkage institutions and EK 5.12.A.1 describes media influence on how citizens acquire information, and both are the framework's. Learning objective 5.12.A asks for the media's role as a linkage institution, which is why the second statement does not replace the first."),

 dict(q="According to EK 5.12.A.2, what do the media use polling results to convey?",
   choices=[
     "Popular levels of trust and confidence in government",
     "The exact number of votes each candidate will receive",
     "The constitutional qualifications for holding office",
     "The rules governing ballot access in each state",
     "The size of each party's membership rolls"], ans=0,
   why="EK 5.12.A.2 names trust and confidence in government as what polling results are used to convey. The statement is about what polls are used to show, not about whether the polls are accurate."),

 dict(q="EK 5.12.A.2 says the media's use of polling results can affect elections by turning such events into what?",
   choices=[
     "Horse races",
     "Referendums on a single issue",
     "Party caucuses",
     "Judicial proceedings",
     "Constitutional conventions"], ans=0,
   why="EK 5.12.A.2 uses the phrase horse races for what election coverage can become, and the image is of a contest reported by who is ahead. The framework supplies the term rather than leaving it to a student's own vocabulary."),

 dict(q="According to EK 5.12.A.2, horse race coverage is based more on what?",
   choices=[
     "Popularity and factors other than the qualifications and platforms of candidates",
     "The constitutional powers of the office being sought",
     "The voting records of incumbent candidates",
     "The endorsements each candidate has received from newspapers",
     "The amount each candidate has raised and spent"], ans=0,
   why="EK 5.12.A.2 states that horse race coverage rests more on popularity and on factors other than qualifications and platforms. The framework names what such coverage displaces, which is what makes the concern a definite one."),

 dict(q="A student writes that the framework says horse race coverage determines who wins an election. What is the most important correction?",
   choices=[
     "The framework says such coverage CAN AFFECT elections, which states a possibility rather than a settled outcome",
     "The framework says such coverage has no effect on elections at all",
     "The framework says such coverage determines only primary elections",
     "The framework says elections are determined entirely by polling accuracy",
     "The framework makes no statement about election coverage"], ans=0,
   why="EK 5.12.A.2's verb is can affect, which asserts that an effect is possible without asserting that it occurs in any particular contest. Reading a modal as a certainty converts a cautious framework statement into a claim it does not make."),

 dict(q="Which two things about candidates does EK 5.12.A.2 say horse race coverage displaces?",
   choices=[
     "Their qualifications and their platforms",
     "Their party membership and their age",
     "Their fundraising totals and their staff",
     "Their endorsements and their debate performances",
     "Their residence and their prior offices"], ans=0,
   why="EK 5.12.A.2's phrase is factors other than the qualifications and platforms of candidates, so those two are what the framework says the coverage moves away from. Naming them is what gives the statement its content."),

 dict(q="A broadcaster's nightly election segment reports which candidate leads in the latest survey and by how much, and returns to that question each evening. Which framework statement does this most directly illustrate?",
   choices=[
     "EK 5.12.A.2, on the media's use of polling results turning elections into horse races",
     "EK 5.12.A.1's category of investigative journalism",
     "EK 5.12.A.1's category of political commentary",
     "Learning objective 5.12.A's reference to linkage institutions between elections",
     "The framework's statement about how citizens acquire information from traditional news media alone"], ans=0,
   why="The segment reports poll standings repeatedly and reports little else, which is the coverage EK 5.12.A.2 describes. Investigative journalism and commentary are separate categories in the framework's other statement."),

 dict(q="A news organization spends months obtaining records that a federal agency had not released and publishes what they show. Which of EK 5.12.A.1's four kinds of political information is this?",
   choices=[
     "Investigative journalism",
     "Political commentary",
     "Election coverage",
     "Routine reporting of news events",
     "Polling analysis"], ans=0,
   why="EK 5.12.A.1 lists investigative journalism separately from news events, and the difference is that the material had to be uncovered rather than observed. Nothing in the scenario concerns a candidate or an opinion offered about one."),

 dict(q="An evening program in which a host argues that a proposed law would be harmful belongs to which of EK 5.12.A.1's four categories?",
   choices=[
     "Political commentary",
     "Investigative journalism",
     "Election coverage",
     "News events",
     "Public opinion polling"], ans=0,
   why="EK 5.12.A.1 lists political commentary among the kinds of political information citizens acquire, and an argument about whether a law is good is opinion offered about politics. Reporting that the law was proposed would be a news event instead."),

 dict(q="The suggested skill for this topic asks students to do what?",
   choices=[
     "Respond to opposing or alternate perspectives with rebuttal or refutation",
     "Describe the facts and holding of a required Supreme Court case",
     "Explain the limitations of a visual representation of data",
     "Describe patterns and trends in quantitative data",
     "Articulate a defensible claim about a political institution"], ans=0,
   why="Skill 5.D is stated in the CED as responding to opposing or alternate perspectives with rebuttal or refutation, and the CED assigns it to this topic. The other options state different skills from the course's skill categories."),

 dict(q="How does responding to an opposing perspective differ from supporting a claim with relevant evidence?",
   choices=[
     "Supporting a claim assembles the evidence for it, while responding takes up the evidence against it and explains why the claim is still the better one",
     "The two requirements are the same",
     "Responding to an opposing perspective means abandoning the original claim",
     "Responding to an opposing perspective means restating the claim more forcefully",
     "Supporting a claim requires ignoring any evidence that conflicts with it"], ans=0,
   why="The CED's prompts for this skill ask what evidence goes against the claim and, taking that evidence into account, why the claim is still the best. Assembling supporting evidence is a separate skill in the same category."),

 dict(q="A claim states that the media's coverage of polls damages elections. Someone objects that poll reporting gives voters real information about the state of a contest. Which response best uses the framework?",
   choices=[
     "Grant that poll results carry information, then argue the framework's concern is the displacement of qualifications and platforms rather than the reporting of polls as such",
     "Deny that polls contain any information at all",
     "Restate the original claim without addressing the objection",
     "Concede the objection and abandon the claim entirely",
     "Argue that the framework forbids the publication of poll results"], ans=0,
   why="EK 5.12.A.2 objects to coverage based more on popularity and on factors other than qualifications and platforms, which is a claim about proportion rather than about publication. A response that grants the true part of an objection and identifies where it misses the claim is what this topic's skill asks for."),

 dict(q="A claim states that agenda setting makes citizens passive recipients of whatever the media supply. Which response draws most directly on the framework's own wording?",
   choices=[
     "The framework's sentence is about how citizens ACQUIRE information, and acquiring is something a citizen does rather than something done to a citizen",
     "The framework states that citizens have no role in obtaining political information",
     "The framework states that agenda setting does not occur",
     "The framework states that citizens choose their information without any influence",
     "The framework states that only investigative journalism reaches citizens"], ans=0,
   why="EK 5.12.A.1 describes influence on how citizens routinely acquire political information, and the verb assigns an activity to the citizen even while the influence is real. A response built on the framework's own verb neither denies the influence nor accepts the strong version of the objection."),

 dict(q="What distinguishes a genuine rebuttal from a restatement of the original claim?",
   choices=[
     "A rebuttal takes the opposing evidence into account and explains why the claim remains the better position",
     "A rebuttal repeats the claim in stronger language",
     "A rebuttal ignores the opposing evidence in order to stay focused",
     "A rebuttal concedes the opposing position without qualification",
     "A rebuttal replaces the claim with the opposing position"], ans=0,
   why="The CED's prompts for this skill ask what someone with an opposing view could say and then why, taking that evidence into account, the claim is still the best. A response that never engages the objection has not done either half."),

 dict(q="In New York Times Co. v. United States (1971), the Supreme Court bolstered freedom of the press, establishing a heavy presumption against prior restraint even in cases involving national security. What does that holding mean for the influence EK 5.12.A.1 attributes to the media?",
   choices=[
     "The choice of what to publish stays with the outlets, so the influence over how citizens acquire information is exercised by the media rather than by government",
     "The holding transfers the choice of what to publish to a federal agency",
     "The holding means the media may not report on national security at all",
     "The holding removes any media influence on how citizens acquire information",
     "The holding applies only to political commentary and not to news events"], ans=0,
   why="A heavy presumption against stopping publication in advance leaves publication decisions with publishers, and EK 5.12.A.1 attributes influence over the route of information to the media themselves. The CED cross-references this case to learning objective 5.12.A for that reason."),

 dict(q="EK 5.12.A.1 names new communication technologies and advances in social media as separate items. What does naming both accomplish?",
   choices=[
     "It states a general category and then singles out one development within it rather than leaving that development implicit",
     "It names two categories that have nothing in common",
     "It restricts the statement to technologies that existed before broadcasting",
     "It excludes social media from the statement",
     "It makes the statement apply only to printed material"], ans=0,
   why="Advances in social media are a kind of new communication technology, so listing both is the framework choosing to name the particular case as well as the general one. A list that named only the general category would leave a reader to decide whether the particular case was covered."),

 dict(q="Which of the following does the course framework NOT state in this topic?",
   choices=[
     "Whether any particular outlet's coverage is fair or unfair",
     "That agenda setting concerns how citizens routinely acquire political information",
     "That the media use polling results to convey trust and confidence in government",
     "That horse race coverage rests more on popularity than on qualifications and platforms",
     "That investigative journalism is among the kinds of political information citizens acquire"], ans=0,
   why="EK 5.12.A.1 and EK 5.12.A.2 describe a process and a possible effect, and neither reaches a verdict about any outlet. Every other option restates part of one of the two statements."),

 dict(q="Why is an argumentation skill about answering opposing views a fitting one for this topic?",
   choices=[
     "Because the framework states a possible effect of media coverage rather than an established one, so a student must be able to take the contrary case into account",
     "Because the framework settles the question of media influence conclusively",
     "Because no evidence about media influence exists",
     "Because media influence cannot be discussed in words",
     "Because the framework supplies the rebuttals a student should use"], ans=0,
   why="EK 5.12.A.2 says horse race coverage CAN AFFECT elections, which invites disagreement about whether and when it does. Skill 5.D asks a student to respond to that disagreement rather than to write as though it did not exist."),

 dict(q=_INFO + " Which conclusion is best supported by the data?",
   table=_INFO_TABLE,
   choices=[
     "News events reach the largest share in a typical week and investigative journalism the smallest, and commentary is the only category reached mainly through social media by more respondents than through traditional news media",
     "Investigative journalism reaches the largest share in a typical week",
     "Every category is reached mainly through social media by more respondents than through traditional news media",
     "No category is reached mainly through social media by more respondents than through traditional news media",
     "All four categories reach a similar share of respondents in a typical week"], ans=0,
   why="Weekly reach runs from 84 percent for news events down to 29 percent for investigative journalism. Only the commentary row shows a larger social media share than traditional share, at 42 percent against 21 percent."),

 dict(q=_INFO + " Where do the four row labels in this table come from?",
   table=_INFO_TABLE,
   choices=[
     "EK 5.12.A.1's list of what political information includes",
     "EK 5.12.A.2's account of horse race coverage",
     "The framework's list of linkage institutions",
     "The CED's list of required Supreme Court cases",
     "The framework's list of campaign finance provisions"], ans=0,
   why="EK 5.12.A.1 names news events, investigative journalism, election coverage and political commentary as the kinds of political information citizens acquire, and the table reports one row for each. The framework's other statement in this topic concerns polling rather than categories of information."),

 dict(q=_INFO + " A student claims that traditional news media no longer influence how citizens acquire political information. Which rebuttal is best supported by this table?",
   table=_INFO_TABLE,
   choices=[
     "Traditional news media is the more common route for three of the four categories, including the two with the widest weekly reach",
     "Traditional news media is the more common route for all four categories",
     "Traditional news media is the more common route for none of the categories",
     "The table reports nothing about how respondents encounter each category",
     "Every category is encountered by fewer than half of respondents in a typical week"], ans=0,
   why="News events, election coverage and investigative journalism each show a larger traditional share than social share, and the first two are the categories with the widest weekly reach at 84 and 71 percent. The rebuttal concedes the commentary row and shows why the general claim still fails."),

 dict(q=_COVERAGE + " Which conclusion is best supported by the data?",
   table=_COVERAGE_TABLE,
   choices=[
     "Coverage of poll standings rises in every period while coverage of qualifications and of platforms each falls, and poll standings take the largest share only in the final week",
     "Coverage of poll standings falls as the election approaches",
     "Coverage of candidate platforms rises as the election approaches",
     "Coverage of poll standings takes the largest share in every period",
     "The three categories hold equal shares throughout the four periods"], ans=0,
   why="Poll standings run from 22 to 61 percent while qualifications fall from 30 to 20 and platforms from 48 to 19. Platforms hold the largest share in the earliest period, so poll standings lead only at the end."),

 dict(q=_COVERAGE + " Which framework statement does this pattern most directly illustrate?",
   table=_COVERAGE_TABLE,
   choices=[
     "EK 5.12.A.2, since coverage shifts toward who is ahead and away from qualifications and platforms",
     "EK 5.12.A.1's category of investigative journalism",
     "EK 5.12.A.1's list of the three kinds of media",
     "The framework's definition of a linkage institution",
     "The framework's statement about the duration of election cycles"], ans=0,
   why="EK 5.12.A.2 describes coverage resting more on popularity and on factors other than the qualifications and platforms of candidates, and the table's two shrinking columns are exactly those two subjects. The growing column reports standing in a contest, which is what the framework calls a horse race."),

 dict(q=_COVERAGE + " Someone objects that this table shows only how one broadcaster allocated its time and cannot establish that horse race coverage affects election outcomes. What is the best response?",
   table=_COVERAGE_TABLE,
   choices=[
     "Accept the limit and note that the framework itself says such coverage CAN AFFECT elections, so the table supports the described shift in coverage without establishing an effect on any result",
     "Reject the objection, since a single broadcaster's shares establish a nationwide effect",
     "Reject the objection, since the framework states that horse race coverage determines election outcomes",
     "Accept the objection and conclude that the table shows nothing at all",
     "Accept the objection and conclude that coverage of platforms rose over the period"], ans=0,
   why="EK 5.12.A.2 states a possible effect rather than an established one, so a table showing a shift in coverage is evidence of the shift and not of a changed result. Conceding what the evidence cannot reach while keeping what it can is what this topic's skill asks for."),
]
