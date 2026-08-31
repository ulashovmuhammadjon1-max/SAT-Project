# AP U.S. GOVERNMENT AND POLITICS 5.10 Modern Campaigns -- 30 questions
# CED V.1 (c) 2026, Unit 5 Political Participation.
# Learning objective 5.10.A: explain how CAMPAIGN ORGANIZATIONS AND STRATEGIES
# affect the ELECTION PROCESS.
# Suggested skill for this topic (CED p. 116): 5.C, argumentation -- USE
# REASONING TO ORGANIZE AND ANALYZE EVIDENCE, EXPLAINING ITS SIGNIFICANCE to
# justify an argument or claim.
#
# Essential knowledge relied on. One statement, four features:
#   EK 5.10.A.1 -- "The BENEFITS AND DRAWBACKS of modern campaigns are
#     represented by:
#       i.   Dependence on PROFESSIONAL CONSULTANTS
#       ii.  RISING CAMPAIGN COSTS and INTENSIVE FUNDRAISING EFFORTS
#       iii. DURATION OF ELECTION CYCLES
#       iv.  IMPACT OF AND RELIANCE ON SOCIAL MEDIA for campaign communication
#            and fundraising"
#
# THE FRAMEWORK'S FIRST FOUR WORDS ARE THE WHOLE DESIGN OF THIS TOPIC: BENEFITS
# AND DRAWBACKS. Each of the four features REPRESENTS BOTH. The framework does
# not present a list of problems with modern campaigns, and every one of the four
# reads naturally as a complaint -- consultants, cost, length, social media --
# which is exactly why a module on this topic drifts into editorial without
# noticing. Treating any of the four as purely a drawback would be stating a
# position the CED declines to state, so items 9 to 14 make the two-sidedness the
# question and the verifier refuses one-sided keys.
#
# BOTH TABLES ARE BUILT TO CUT BOTH WAYS, and that is deliberate rather than
# decorative. The cost table shows campaign costs and fundraising time rising
# together with the share of money coming from small donations -- the same trend
# supplying a drawback and a benefit. The activity table gives social media the
# best figures on two measures and the worst on a third. Neither table can be
# read as an indictment or as a defence, which is what makes items 27 and 30
# answerable in the framework's own terms.
#
# SKILL 5.C ASKS FOR SIGNIFICANCE, WHICH IS A STEP PAST RELEVANCE. Topic 5.9's
# skill (5.B) asks whether evidence bears on a claim at all; 5.C asks what it
# SHOWS about the claim once it does -- whether it supports, qualifies or
# undercuts it, and why. Items 15 to 20 turn on that difference, and several of
# them have keys that QUALIFY a claim rather than confirming or refuting it,
# because qualification is what evidence cutting both ways actually licenses.
#
# Documents the CED attaches to 5.10.A (p. 27): Federalist No. 10. Items 21 and
# 22 quote it verbatim.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere. No LaTeX:
# this is a prose subject and export_units.py no longer typesets US_GOV.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("5.10", "Modern Campaigns", 5)

_COSTS = ("A hypothetical study reports, across four election cycles, the average cost of a "
          "competitive campaign, the share of a candidate's time spent raising money, and the "
          "share of funds coming from donations under 200 dollars.")
_COSTS_TABLE = dict(
    headers=["Election cycle", "Average campaign cost (thousands of dollars)",
             "Candidate time spent fundraising (%)", "Funds from small donations (%)"],
    rows=[["Cycle 1", "1200", "31", "12"],
          ["Cycle 2", "1850", "38", "19"],
          ["Cycle 3", "2600", "44", "28"],
          ["Cycle 4", "3900", "49", "41"]])

_ACTIVITIES = ("A hypothetical study of campaign activities reports how many campaigns use each, "
               "the median cost of reaching one voter, and the share of contacted voters who "
               "describe the message as unwanted.")
_ACTIVITIES_TABLE = dict(
    headers=["Campaign activity", "Campaigns using it (%)", "Median cost per voter (dollars)",
             "Contacted voters calling it unwanted (%)"],
    rows=[["Canvassing in person", "88", "4.20", "9"],
          ["Television advertising", "71", "2.10", "22"],
          ["Direct mail", "64", "1.40", "31"],
          ["Social media", "96", "0.15", "38"]])

QUESTIONS = [
 dict(q="According to the course framework, what do the four features it lists represent about modern campaigns?",
   choices=[
     "Their benefits and drawbacks",
     "Their drawbacks only",
     "Their benefits only",
     "Their legal requirements",
     "Their historical origins"], ans=0,
   why="EK 5.10.A.1's own phrase is 'the benefits and drawbacks of modern campaigns are represented by', so each listed feature stands for both. The framework declines to present the list as a set of problems."),

 dict(q="Which four features does EK 5.10.A.1 list?",
   choices=[
     "Dependence on professional consultants, rising campaign costs and intensive fundraising, the duration of election cycles, and the impact of and reliance on social media",
     "Party conventions, primaries, caucuses, and general elections",
     "Incumbency advantage, open primaries, closed primaries, and the Electoral College",
     "Mobilization of voters, party platforms, candidate recruitment, and campaign management",
     "Structural barriers, political efficacy, demographics, and election type"], ans=0,
   why="EK 5.10.A.1 names exactly these four. The fourth option lists EK 5.3.B.1's party functions, which concern what a party does rather than what characterizes a modern campaign."),

 dict(q="What does EK 5.10.A.1 pair with RISING CAMPAIGN COSTS in the same item?",
   choices=[
     "Intensive fundraising efforts",
     "The duration of election cycles",
     "Dependence on professional consultants",
     "Reliance on social media",
     "Party conventions"], ans=0,
   why="EK 5.10.A.1.ii names rising campaign costs AND intensive fundraising efforts together, because the second follows from the first: money that must be spent must first be raised."),

 dict(q="For what two purposes does EK 5.10.A.1 say campaigns rely on social media?",
   choices=[
     "Campaign communication and fundraising",
     "Voter registration and ballot counting",
     "Candidate recruitment and platform drafting",
     "Polling and redistricting",
     "Legal compliance and reporting"], ans=0,
   why="EK 5.10.A.1.iv's phrase is 'for campaign communication and fundraising', so the framework attaches social media to both reaching voters and raising money. It is the only one of the four features named for two distinct purposes."),

 dict(q="Which feature in EK 5.10.A.1's list concerns how LONG campaigns run rather than how they operate?",
   choices=[
     "The duration of election cycles",
     "Dependence on professional consultants",
     "Rising campaign costs",
     "Reliance on social media",
     "Intensive fundraising efforts"], ans=0,
   why="EK 5.10.A.1.iii names the duration of election cycles, which is a fact about the length of the process rather than about the people or tools a campaign uses. The other items describe what a campaign does or depends on."),

 dict(q="What does DEPENDENCE ON PROFESSIONAL CONSULTANTS describe, in the framework's sense?",
   choices=[
     "Campaigns relying on paid specialists to run their operations",
     "Candidates relying on party officials to select them",
     "Voters relying on the media for information",
     "Parties relying on interest groups for funding",
     "Legislators relying on agencies for expertise"], ans=0,
   why="EK 5.10.A.1.i names dependence on professional consultants as a feature of modern campaigns, so the reliance is the campaign's and the specialists are paid to do campaign work. The other options describe reliance by other actors on other actors."),

 dict(q="How do EK 5.10.A.1's four features relate to LO 5.10.A's phrase CAMPAIGN ORGANIZATIONS AND STRATEGIES?",
   choices=[
     "Consultants and costs describe how a campaign is organized and resourced, while social media and cycle length describe the conditions its strategy operates in",
     "All four describe legal rules governing campaigns",
     "All four describe the behavior of voters",
     "None of them concerns campaign organization",
     "The features and the objective are unrelated"], ans=0,
   why="LO 5.10.A names organizations and strategies, and EK 5.10.A.1's items divide between what a campaign is made of and what it must work within. Both halves of the objective are needed to cover the four features."),

 dict(q="Which of EK 5.10.A.1's features is named for two distinct campaign purposes?",
   choices=[
     "Social media, named for campaign communication and fundraising",
     "Professional consultants, named for strategy and polling",
     "Election cycles, named for primaries and general elections",
     "Campaign costs, named for advertising and staffing",
     "None of them; each is named for one purpose"], ans=0,
   why="EK 5.10.A.1.iv attaches social media to campaign communication and to fundraising, while the other three items name a feature without splitting it by purpose. That double role is why social media appears in the framework's list at all."),

 dict(q="A student describes EK 5.10.A.1's four features as the problems with modern campaigns. What is the most important correction?",
   choices=[
     "The framework says the features represent benefits AND drawbacks, so presenting them as problems states a position the framework does not take",
     "The framework says the features represent benefits only",
     "The framework lists six features rather than four",
     "The framework says the features concern only presidential campaigns",
     "The framework says the features have no effect on elections"], ans=0,
   why="EK 5.10.A.1's opening phrase is BENEFITS AND DRAWBACKS, so each feature stands for both. All four read naturally as complaints, which is exactly why the framework's own wording has to be kept."),

 dict(q="What is a plausible BENEFIT of a campaign's dependence on professional consultants?",
   choices=[
     "Specialists bring experience that a campaign built from scratch each cycle would lack",
     "Consultants reduce the total cost of a campaign to nothing",
     "Consultants guarantee that the better candidate wins",
     "Consultants remove the need for any fundraising",
     "Consultants replace the need for voters"], ans=0,
   why="EK 5.10.A.1 presents each feature as representing benefits as well as drawbacks, and expertise is the benefit side of relying on paid specialists. The other options assert effects nothing in the framework supports."),

 dict(q="What is a plausible DRAWBACK of a campaign's dependence on professional consultants?",
   choices=[
     "Campaigns that cannot afford specialists compete on unequal terms",
     "Consultants make campaigns impossible to organize",
     "Consultants prevent candidates from appearing on the ballot",
     "Consultants eliminate the role of political parties entirely",
     "Consultants are prohibited by the framework"], ans=0,
   why="EK 5.10.A.1.i's feature has a drawback side as well as a benefit side, and unequal access to paid expertise is the natural one. The framework prohibits nothing and describes no elimination of parties."),

 dict(q="A campaign cycle that begins long before the election has which pair of effects, in the framework's two-sided terms?",
   choices=[
     "More time for candidates to become known and be examined, and a longer period during which money must be raised and attention held",
     "Only the benefit of greater familiarity",
     "Only the drawback of greater expense",
     "No effect on either candidates or voters",
     "An effect on primaries but not on general elections"], ans=0,
   why="EK 5.10.A.1.iii lists the duration of election cycles among features representing benefits AND drawbacks, so a longer cycle has to be read both ways. Length gives more room for scrutiny and requires sustaining a campaign for longer."),

 dict(q="Why is it difficult to write about EK 5.10.A.1's four features without taking a position?",
   choices=[
     "Because all four are commonly discussed as complaints, so restating them without the framework's BENEFITS AND DRAWBACKS framing quietly endorses one side",
     "Because the framework takes a position on each of them",
     "Because the features cannot be described in words",
     "Because no evidence about them exists",
     "Because the features apply only to one political party"], ans=0,
   why="Consultants, cost, length and social media are the standard subjects of complaint about modern campaigning, and EK 5.10.A.1 presents them as representing benefits as well as drawbacks. Dropping the framing is how a description becomes an argument without anyone deciding to make one."),

 dict(q="Which of the following does EK 5.10.A.1 NOT state?",
   choices=[
     "Whether modern campaigns are better or worse than earlier ones",
     "That dependence on professional consultants is a feature of modern campaigns",
     "That campaign costs have risen",
     "That election cycles have a duration worth noting",
     "That campaigns rely on social media for communication and fundraising"], ans=0,
   why="EK 5.10.A.1 names four features and says they represent benefits and drawbacks, which is a description rather than a verdict. Every other option restates part of the statement."),

 dict(q="The suggested skill for this topic asks students to explain the SIGNIFICANCE of evidence. How does that differ from showing that evidence is relevant?",
   choices=[
     "Relevance asks whether the evidence bears on the claim at all; significance asks what it shows about the claim once it does",
     "The two are the same requirement",
     "Significance asks whether the evidence is recent",
     "Significance asks how much evidence there is",
     "Relevance asks what the evidence shows and significance whether it applies"], ans=0,
   why="Skill 5.B asks for relevant evidence and skill 5.C asks for reasoning that explains its significance, so the second takes up where the first leaves off. Evidence can bear on a claim and support it, qualify it or undercut it."),

 dict(q="A claim states that rising campaign costs have made campaigns less accessible to new candidates. Evidence shows that the share of funds from small donations has risen over the same period. What is the significance of that evidence for the claim?",
   choices=[
     "It qualifies the claim, since a broader base of small donors is a route to money that does not depend on existing wealth or connections",
     "It confirms the claim without qualification",
     "It is irrelevant to the claim",
     "It proves that campaign costs have not risen",
     "It shows that new candidates never run"], ans=0,
   why="The evidence bears on the claim and points the other way, without settling it: costs may still rise while the means of meeting them broadens. Skill 5.C asks what evidence shows, and evidence that cuts against part of a claim qualifies rather than confirms or refutes it."),

 dict(q="A claim states that social media has made campaigning cheaper. Evidence shows a low median cost per voter contacted through social media. What further evidence would be needed before the claim is established?",
   choices=[
     "Whether total campaign spending fell, since a cheaper method of contact is consistent with more contacts and higher total cost",
     "Whether social media existed in earlier cycles",
     "Whether voters prefer social media to other methods",
     "Whether candidates use consultants to manage social media",
     "Whether campaigns report their spending accurately"], ans=0,
   why="A lower cost per unit and a lower total are different claims, and the second does not follow from the first if the number of units rises. Skill 5.C's reasoning step is what connects a per-contact figure to a claim about total cost."),

 dict(q="Two pieces of evidence about the same feature point in opposite directions. According to the framework's framing, what is the appropriate conclusion?",
   choices=[
     "That the feature has both benefits and drawbacks, which is what EK 5.10.A.1 says its features represent",
     "That one of the two pieces of evidence must be false",
     "That no conclusion is possible",
     "That the feature has no effect on campaigns",
     "That the evidence concerns different features"], ans=0,
   why="EK 5.10.A.1 introduces its list as representing benefits AND drawbacks, so evidence pulling both ways is what the framework leads a student to expect. Discarding one side to reach a verdict would be imposing a conclusion the framework does not draw."),

 dict(q="A student organizes evidence about modern campaigns into two columns, one headed BENEFITS and one headed DRAWBACKS. How does this bear on skill 5.C?",
   choices=[
     "Organizing evidence is the first half of the skill, and explaining what each column shows about the claim is the second",
     "Organizing evidence is the whole of the skill",
     "The skill concerns only the collection of evidence",
     "The skill forbids organizing evidence into categories",
     "The skill concerns only visual representations"], ans=0,
   why="Skill 5.C reads 'use reasoning to ORGANIZE AND ANALYZE evidence, EXPLAINING ITS SIGNIFICANCE', so it names both steps. Two columns of facts with nothing said about them stops halfway."),

 dict(q="A claim states that longer election cycles benefit well-known candidates. Which evidence would most directly bear on it, and what would it need to show?",
   choices=[
     "A comparison of how candidates with different levels of prior recognition fare as cycle length varies",
     "The total length of recent election cycles",
     "The number of candidates who ran in recent cycles",
     "The share of campaign funds spent on advertising",
     "The number of states holding early primaries"], ans=0,
   why="The claim relates cycle length to an advantage for one kind of candidate, so the evidence has to vary the length and observe how different candidates do. Cycle length alone establishes the condition without showing its effect on anyone."),

 dict(q="Read the following excerpt.\n\n“The most common and durable source of factions has been the various and unequal distribution of property.”\n—James Madison, Federalist No. 10, 1787\n\nHow does this observation bear on EK 5.10.A.1's feature of rising campaign costs?",
   choices=[
     "It suggests that unequal resources are a standing feature of politics, which is the background against which a rise in the cost of competing matters",
     "It states that campaign costs should be regulated",
     "It states that wealth has no role in politics",
     "It concerns social media rather than campaign finance",
     "It has no bearing on campaigns"], ans=0,
   why="Madison identifies unequal distribution of property as the most durable source of political division, and EK 5.10.A.1.ii names rising costs as a feature representing benefits and drawbacks. The CED attaches Federalist No. 10 to 5.10.A, and the essay supplies the standing condition rather than a recommendation."),

 dict(q="Read the following excerpt.\n\n“Extend the sphere, and you take in a greater variety of parties and interests.”\n—James Madison, Federalist No. 10, 1787\n\nHow might this reasoning be applied to EK 5.10.A.1's feature of social media?",
   choices=[
     "A medium that reaches further could take in a greater variety of voices, which is a benefit to weigh against the drawbacks the framework also attributes to the feature",
     "It shows that social media should be prohibited",
     "It shows that social media has only drawbacks",
     "It shows that social media has only benefits",
     "It concerns the size of a republic and cannot be applied at all"], ans=0,
   why="Madison's reasoning is about what a larger sphere admits, and EK 5.10.A.1.iv names social media's impact and the reliance on it as representing benefits and drawbacks. Applying the reasoning supplies one side, which is why the key says it must be weighed against the other."),

 dict(q="Why does the CED assign an argumentation skill to this topic rather than a data analysis one?",
   choices=[
     "Because the framework's own framing of benefits and drawbacks calls for weighing evidence on both sides rather than describing a pattern",
     "Because no data about campaigns exists",
     "Because campaigns cannot be measured",
     "Because argumentation is the only skill used in Unit 5",
     "Because the framework supplies its own conclusions"], ans=0,
   why="EK 5.10.A.1 presents four features as representing benefits AND drawbacks, which is a structure that requires reasoning about competing evidence. Unit 5 uses several data analysis skills in other topics, so the choice here is a substantive one."),

 dict(q="Which statement best summarizes what this topic establishes about modern campaigns?",
   choices=[
     "Four features characterize them, and each carries benefits and drawbacks that the framework declines to weigh for the student",
     "Four features characterize them, and all four are drawbacks",
     "Four features characterize them, and all four are benefits",
     "Modern campaigns are worse than earlier ones",
     "Modern campaigns are better than earlier ones"], ans=0,
   why="EK 5.10.A.1 names four features and says they represent benefits and drawbacks, and it draws no balance. The last two options are verdicts the framework does not state, and the second and third drop half its opening phrase."),

 dict(q=_COSTS + " Which conclusion is best supported by the data?",
   table=_COSTS_TABLE,
   choices=[
     "All three measures rose across the four cycles, with campaign costs more than tripling and the small-donation share more than tripling as well",
     "Campaign costs rose while the small-donation share fell",
     "Candidate time spent fundraising fell across the cycles",
     "All three measures were unchanged across the cycles",
     "The small-donation share exceeded half in the final cycle"], ans=0,
   why="Costs run 1200 to 3900 thousand dollars, fundraising time 31 to 49 percent, and small donations 12 to 41 percent, all rising. The final small-donation share is 41 percent, which is below half."),

 dict(q=_COSTS + " Which feature in EK 5.10.A.1 do the first two data columns correspond to?",
   table=_COSTS_TABLE,
   choices=[
     "Rising campaign costs and intensive fundraising efforts",
     "Dependence on professional consultants",
     "The duration of election cycles",
     "The impact of and reliance on social media",
     "Party platforms and candidate recruitment"], ans=0,
   why="EK 5.10.A.1.ii names rising campaign costs and intensive fundraising efforts in one item, and the table's first two data columns are exactly those two quantities. The framework pairs them because raising money is what meeting rising costs requires."),

 dict(q=_COSTS + " A student argues from this table that modern campaigning has become less accessible to candidates without wealthy backers. What is the significance of the third column for that argument?",
   table=_COSTS_TABLE,
   choices=[
     "It qualifies the argument, since the share of money coming from small donations more than tripled over the same period",
     "It confirms the argument, since small donations fell",
     "It is irrelevant, since it concerns donors rather than candidates",
     "It refutes the argument entirely, since costs did not rise",
     "It shows that campaign costs fell across the cycles"], ans=0,
   why="Small donations rise from 12 to 41 percent of funds while costs rise from 1200 to 3900 thousand dollars, so the same period shows both a higher barrier and a broader route over it. Skill 5.C asks what evidence shows, and evidence pulling against part of an argument qualifies rather than confirms or refutes it."),

 dict(q=_ACTIVITIES + " Which conclusion is best supported by the data?",
   table=_ACTIVITIES_TABLE,
   choices=[
     "Social media is used by more campaigns and costs least per voter contacted, and also draws the highest share of contacted voters calling the message unwanted",
     "Social media is used by the fewest campaigns",
     "Social media costs the most per voter contacted",
     "Canvassing in person draws the highest share calling the message unwanted",
     "Every activity is used by a similar share of campaigns"], ans=0,
   why="Social media stands at 96 percent use, 0.15 dollars per voter and 38 percent calling the message unwanted, which is the highest use, the lowest cost and the highest unwanted share. Canvassing in person has the lowest unwanted share at 9 percent and the highest cost per voter."),

 dict(q=_ACTIVITIES + " Which feature in EK 5.10.A.1 does the last row of this table bear on?",
   table=_ACTIVITIES_TABLE,
   choices=[
     "The impact of and reliance on social media for campaign communication and fundraising",
     "Dependence on professional consultants",
     "The duration of election cycles",
     "Rising campaign costs alone",
     "Party conventions"], ans=0,
   why="The row reports how widely social media is used and what it costs to reach a voter through it, which is the impact and the reliance EK 5.10.A.1.iv names. The framework attaches that feature to campaign communication, which is what the table measures."),

 dict(q=_ACTIVITIES + " What is the significance of the social media row for the framework's claim that its features represent benefits AND drawbacks?",
   table=_ACTIVITIES_TABLE,
   choices=[
     "One activity holds the best figures on two measures and the worst on a third, so the same feature supplies both a benefit and a drawback",
     "One activity holds the best figures on every measure, so the feature is purely a benefit",
     "One activity holds the worst figures on every measure, so the feature is purely a drawback",
     "The activities differ on no measure",
     "The table cannot bear on the framework's claim"], ans=0,
   why="Social media leads on use and on cost per voter and trails on the unwanted share, so the row cannot be read as an indictment or as a defence. EK 5.10.A.1's opening phrase is what that pattern illustrates."),
]
