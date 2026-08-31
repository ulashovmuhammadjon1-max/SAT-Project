# AP U.S. GOVERNMENT AND POLITICS 5.11 Campaign Finance -- 30 questions
# CED V.1 (c) 2026, Unit 5 Political Participation.
# Learning objective 5.11.A: explain how the ORGANIZATION, FINANCE, AND
# STRATEGIES of NATIONAL POLITICAL CAMPAIGNS affect the ELECTION PROCESS.
# Suggested skill for this topic (CED p. 116): 2.B, SCOTUS Application --
# EXPLAIN HOW A REQUIRED SUPREME COURT CASE RELATES TO A FOUNDATIONAL DOCUMENT
# or to other primary or secondary sources.
#
# Essential knowledge relied on, quoted from the framework:
#   EK 5.11.A.1 -- "Federal legislation and case law pertaining to campaign
#     finance demonstrate the ONGOING DEBATE OVER THE ROLE OF MONEY IN POLITICAL
#     AND FREE SPEECH, as set forth in:
#       i.  The BIPARTISAN CAMPAIGN REFORM ACT OF 2002, which was an effort to
#           BAN SOFT MONEY and REDUCE ATTACK ADS with 'Stand by Your Ad'
#           provision: 'I'm [candidate's name] and I approve this message'
#       ii. SUPREME COURT DECISIONS that ruled POLITICAL SPENDING BY
#           CORPORATIONS, ASSOCIATIONS, AND LABOR UNIONS is a FORM OF PROTECTED
#           SPEECH UNDER THE FIRST AMENDMENT"
#   EK 5.11.A.2 -- "Debates have increased over FREE SPEECH and COMPETITIVE AND
#     FAIR ELECTIONS related to money and campaign funding (including
#     contributions from INDIVIDUALS, POLITICAL ACTION COMMITTEES [PACs], and
#     POLITICAL PARTIES)."
#   EK 5.11.A.3 -- "DIFFERENT TYPES OF PACs influence ELECTIONS AND POLICYMAKING
#     through FUNDRAISING AND SPENDING."
#
# Required Supreme Court case the CED attaches to 5.11.A (p. 34): CITIZENS
# UNITED V. FEDERAL ELECTION COMMISSION (2010). The CED states its holding, on
# p. 30, in one sentence: "Political spending by corporations, associations, and
# labor unions is a form of protected speech under the First Amendment." That
# sentence is the whole of what this bank may attribute to the case.
#
# Foundational document the CED attaches to 5.11.A (p. 26): FEDERALIST NO. 10.
# The CED's own sample activity for skill 2.B (p. 155) is to "relate the
# reasoning, decision, and opinion in Citizens United v. Federal Election
# Commission (FEC) (2010) to Madison's argument in Federalist No. 10. (Topic
# 5.11)". Items 18 to 22 are that activity written as multiple choice.
#
# WHAT THIS MODULE DELIBERATELY DOES NOT SAY, and why the restraint is the
# design rather than a shortfall. Campaign finance is the topic on which public
# commentary is loudest and the framework is quietest. The CED states no
# contribution limit, no dollar figure, no definition of soft money beyond the
# word, no taxonomy of PACs beyond "different types", and no verdict on whether
# the 2002 act worked or on whether Citizens United was rightly decided. Every
# one of those is available in a student's memory and none of them is keyable
# here, so items 13, 17 and 24 make the boundary itself the question. Item 24 in
# particular refuses the single most common misstatement about the required
# case -- that it permitted unlimited direct contributions to candidates -- for
# the reason that the CED's sentence is about SPENDING and says nothing about
# contributions at all.
#
# THE TABLES ARE HYPOTHETICAL AND SAY SO IN THE STEM. No figure here describes a
# real election, a real committee or a real survey. There is no sympy in this
# subject, and a number attributed to a real contest is a claim nobody
# downstream could check.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere. No LaTeX:
# this is a prose subject and export_units.py no longer typesets US_GOV.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("5.11", "Campaign Finance", 5)

_ORGS = ("A hypothetical study of four organizations that raise and spend money in national "
         "elections reports the funds each raised during one election cycle, the share of that "
         "money spent on advertising, and the share given directly to candidate committees.")
_ORGS_TABLE = dict(
    headers=["Organization", "Funds raised (thousands of dollars)",
             "Share spent on advertising (%)", "Share given to candidate committees (%)"],
    rows=[["Organization W", "4800", "78", "6"],
          ["Organization X", "2500", "40", "35"],
          ["Organization Y", "1600", "55", "20"],
          ["Organization Z", "900", "30", "48"]])

_VIEWS = ("A hypothetical survey asked respondents whether they agree that limits on political "
          "spending protect competitive and fair elections, and separately whether they agree "
          "that limits on political spending restrict free speech. The final column reports the "
          "share agreeing with both statements.")
_VIEWS_TABLE = dict(
    headers=["Respondent group", "Limits protect fair elections (%)",
             "Limits restrict free speech (%)", "Agree with both statements (%)"],
    rows=[["Under 30", "61", "54", "27"],
          ["Ages 30 to 49", "58", "57", "25"],
          ["Ages 50 to 64", "55", "61", "24"],
          ["Ages 65 and older", "52", "66", "23"]])

QUESTIONS = [
 dict(q="According to the course framework, what do federal legislation and case law pertaining to campaign finance demonstrate?",
   choices=[
     "An ongoing debate over the role of money in political and free speech",
     "A settled rule fixing how much may be spent on a national campaign",
     "That money plays no part in national election outcomes",
     "That the Constitution addresses campaign spending by name",
     "That campaign spending is left entirely to the states"], ans=0,
   why="EK 5.11.A.1's own words are that legislation and case law demonstrate the ongoing debate over the role of money in political and free speech. The framework describes a dispute that continues rather than a rule that has been settled."),

 dict(q="EK 5.11.A.1 says the debate over money in politics is set forth in which two things?",
   choices=[
     "The Bipartisan Campaign Reform Act of 2002 and Supreme Court decisions on political spending as protected speech",
     "The Voting Rights Act and decisions on legislative districting",
     "The Electoral College and the results of national conventions",
     "State ballot access rules and the party platforms adopted every four years",
     "The census and the reapportionment of House seats"], ans=0,
   why="EK 5.11.A.1's two subordinate items are an act of Congress and a line of Supreme Court decisions, which is why the framework's sentence begins with federal legislation AND case law. The other options name material the framework places in different topics."),

 dict(q="EK 5.11.A.1 describes the Bipartisan Campaign Reform Act of 2002 as an effort to do what?",
   choices=[
     "Ban soft money and reduce attack ads",
     "Abolish political action committees",
     "Require public financing of every national campaign",
     "Fix the length of the presidential election cycle",
     "Transfer the administration of federal elections to the states"], ans=0,
   why="EK 5.11.A.1.i names both purposes in one phrase: the act was an effort to ban soft money and to reduce attack ads. The framework describes the effort rather than assessing whether it succeeded."),

 dict(q="What does the STAND BY YOUR AD provision the framework attaches to the 2002 act require an advertisement to contain?",
   choices=[
     "A statement in which the candidate is named and says the message is approved",
     "A published list of everyone who paid for the advertisement",
     "Advance clearance from a federal agency before the advertisement may run",
     "A limit of one minute on the length of the advertisement",
     "A written summary of the candidate's policy positions"], ans=0,
   why="EK 5.11.A.1.i quotes the provision's formula as 'I'm [candidate's name] and I approve this message', so what the provision adds is the candidate's own name and approval. Disclosure of donors and advance clearance are different requirements the framework does not describe here."),

 dict(q="Why would a requirement that a candidate personally approve an advertisement serve the framework's stated purpose of REDUCING ATTACK ADS?",
   choices=[
     "Because attaching the candidate's own name and voice to the message makes the candidate publicly answerable for its content",
     "Because the requirement forbids any mention of an opposing candidate",
     "Because the requirement caps the number of advertisements a campaign may broadcast",
     "Because the requirement shifts the cost of the advertisement to the government",
     "Because the requirement bars advertising during the final weeks of a campaign"], ans=0,
   why="EK 5.11.A.1.i pairs the reduction of attack ads with a provision whose whole content is the candidate's stated approval, so the mechanism the framework implies is accountability for what the message says. The other options describe restrictions the framework does not attribute to the provision."),

 dict(q="What does EK 5.11.A.1 say Supreme Court decisions have ruled about political spending by corporations, associations, and labor unions?",
   choices=[
     "That it is a form of protected speech under the First Amendment",
     "That it may be prohibited whenever Congress finds it corrupting",
     "That it is governed entirely by state law",
     "That it is protected only during the final month of a campaign",
     "That it falls outside the Constitution altogether"], ans=0,
   why="EK 5.11.A.1.ii states the holding in those terms, and the CED's required-case list states the holding of Citizens United v. Federal Election Commission in the same sentence. The framework reports the ruling without endorsing or criticizing it."),

 dict(q="Which three kinds of organizations does EK 5.11.A.1.ii name in its statement about political spending?",
   choices=[
     "Corporations, associations, and labor unions",
     "States, counties, and municipalities",
     "Churches, schools, and charitable foundations",
     "Federal agencies, congressional committees, and courts",
     "Candidates, campaign managers, and consultants"], ans=0,
   why="EK 5.11.A.1.ii lists exactly those three, which is why the statement reaches organized entities rather than individual donors. Individuals appear in the framework's next statement, in a different list."),

 dict(q="Which required Supreme Court case does the CED state as holding that political spending by corporations, associations, and labor unions is a form of protected speech under the First Amendment?",
   choices=[
     "Citizens United v. Federal Election Commission (2010)",
     "New York Times Co. v. United States (1971)",
     "Shaw v. Reno (1993)",
     "McDonald v. Chicago (2010)",
     "United States v. Lopez (1995)"], ans=0,
   why="The CED's required-case list gives that holding for Citizens United, and the SCOTUS cross-reference table attaches the case to learning objective 5.11.A. The other cases concern prior restraint, districting, the Second Amendment and the Commerce Clause."),

 dict(q="EK 5.11.A.2 says debates have increased over which two things, in connection with money and campaign funding?",
   choices=[
     "Free speech, and competitive and fair elections",
     "Voter registration, and the counting of ballots",
     "Term limits, and the size of the House of Representatives",
     "Judicial appointments, and the confirmation process",
     "Party membership, and the rules of national conventions"], ans=0,
   why="EK 5.11.A.2 names free speech alongside competitive and fair elections, so the framework presents the dispute as one between two goods rather than between a good and a harm. That is what makes it a debate rather than a straightforward wrong to be corrected."),

 dict(q="EK 5.11.A.2 mentions contributions from which three sources?",
   choices=[
     "Individuals, political action committees, and political parties",
     "Foreign governments, corporations, and labor unions",
     "Federal agencies, state legislatures, and courts",
     "Candidates, consultants, and campaign staff",
     "Broadcasters, newspapers, and social media platforms"], ans=0,
   why="EK 5.11.A.2's parenthesis lists individuals, political action committees and political parties. The framework mentions those three as sources of contributions and does not extend the list to any other source."),

 dict(q="According to EK 5.11.A.3, different types of PACs influence what, and by what means?",
   choices=[
     "Elections and policymaking, through fundraising and spending",
     "Elections only, through fundraising alone",
     "Policymaking only, by testifying before congressional committees",
     "Judicial decisions, by filing briefs in pending cases",
     "Voter registration, by canvassing neighborhoods door to door"], ans=0,
   why="EK 5.11.A.3 names two objects of influence and two means, and the framework joins each pair rather than choosing between them. Restricting the statement to elections alone drops half of what it says."),

 dict(q="A student writes that the course framework treats PACs as a single uniform kind of organization. What is the most important correction?",
   choices=[
     "The framework's phrase is DIFFERENT TYPES of PACs, so it treats them as varied rather than uniform",
     "The framework says PACs are all identical in size and purpose",
     "The framework does not mention PACs anywhere",
     "The framework says PACs are agencies of the federal government",
     "The framework says PACs are prohibited from spending money"], ans=0,
   why="EK 5.11.A.3 opens with the words different types, so variety among PACs is part of the statement rather than an addition to it. The framework does not go on to name the types, which is a separate limit on what may be asserted."),

 dict(q="Which of the following does the course framework NOT state about campaign finance?",
   choices=[
     "The maximum amount any donor may lawfully contribute",
     "That the Bipartisan Campaign Reform Act of 2002 was an effort to ban soft money",
     "That debates have increased over free speech and fair elections",
     "That different types of PACs influence elections and policymaking",
     "That Supreme Court decisions treated political spending by organizations as protected speech"], ans=0,
   why="EK 5.11.A.1 through EK 5.11.A.3 name an act, a line of decisions, a debate and a set of actors, and none of them states a dollar limit. Every other option restates part of the framework."),

 dict(q="Learning objective 5.11.A names the organization, FINANCE, and strategies of national political campaigns, while the preceding topic's objective names only campaign organizations and strategies. What does the added word require a student to explain?",
   choices=[
     "How the way a campaign is paid for, and not only how it is run, affects the election process",
     "How campaigns select their nominees at national conventions",
     "How states administer polling places on election day",
     "How the Electoral College allocates votes among the states",
     "How members of Congress are assigned to committees"], ans=0,
   why="The two objectives share organization and strategies, so finance is the whole of what 5.11.A adds, and the object of the explanation stays the election process. The other options name processes neither objective mentions."),

 dict(q="A labor union pays for advertisements urging voters to support a particular candidate. An opponent argues that a state may forbid the union from spending its money this way. Which framework statement bears most directly on the argument?",
   choices=[
     "EK 5.11.A.1.ii, which reports decisions ruling that political spending by corporations, associations, and labor unions is protected speech under the First Amendment",
     "EK 5.11.A.2, which lists the sources of campaign contributions",
     "EK 5.11.A.3, which concerns the different types of PACs",
     "EK 5.11.A.1.i, which describes the Stand by Your Ad provision",
     "Learning objective 5.11.A, which concerns the length of the election cycle"], ans=0,
   why="The scenario involves a labor union spending its own money on political advertising, which is the exact subject of the framework's statement about protected speech. The Stand by Your Ad provision concerns what an advertisement must say, not whether the spending may occur."),

 dict(q="A televised advertisement closes with the candidate appearing on screen to say that the message is the candidate's own and is approved. Which part of the framework does this illustrate?",
   choices=[
     "The Stand by Your Ad provision of the Bipartisan Campaign Reform Act of 2002",
     "The soft money ban in the same act",
     "The Supreme Court decisions on political spending as protected speech",
     "The framework's statement about different types of PACs",
     "The framework's list of contribution sources"], ans=0,
   why="EK 5.11.A.1.i quotes the formula in which a candidate is named and states approval, and the scenario is that formula performed. The soft money ban in the same act concerns where money may come from rather than what an advertisement must say."),

 dict(q="Why does the framework describe the debate over money in politics as ONGOING rather than as resolved?",
   choices=[
     "Because it points to both an act of Congress and a line of Supreme Court decisions, so the question has been answered by different institutions in different ways",
     "Because no court has ever ruled on campaign spending",
     "Because Congress has never legislated on campaign finance",
     "Because the Constitution settles the question explicitly",
     "Because public opinion on the question is unanimous"], ans=0,
   why="EK 5.11.A.1 cites federal legislation and case law together, and the two sources it names pull in different directions: an act restricting certain money and decisions protecting certain spending as speech. A debate carried on by two branches is one the framework has reason to call ongoing."),

 dict(q="Read the following excerpt.\n\n“The inference to which we are brought is, that the causes of faction cannot be removed, and that relief is only to be sought in the means of controlling its effects.”\n—James Madison, Federalist No. 10, 1787\n\nHow does this reasoning relate to the framework's account of campaign finance legislation?",
   choices=[
     "It supports treating regulation as an attempt to control the effects of unequal resources rather than to eliminate their causes, which is how an act limiting certain money operates",
     "It shows that Madison recommended a ban on political contributions",
     "It shows that the causes of faction can be removed by legislation",
     "It shows that no regulation of any kind is possible",
     "It concerns religious liberty rather than political influence"], ans=0,
   why="Madison concludes that the causes of faction cannot be removed and that relief lies in controlling effects, and legislation reaching how money may be raised and how advertisements must be labeled operates on effects. The CED attaches Federalist No. 10 to this learning objective, and Madison recommends no campaign measure because none existed to recommend."),

 dict(q="Read the following excerpt.\n\n“Liberty is to faction what air is to fire, an aliment without which it instantly expires. But it could not be less folly to abolish liberty, which is essential to political life, because it nourishes faction, than it would be to wish the annihilation of air, which is essential to animal life, because it imparts to fire its destructive agency.”\n—James Madison, Federalist No. 10, 1787\n\nWhich side of the campaign finance debate described in EK 5.11.A.2 does this passage most directly support?",
   choices=[
     "The free speech side, since Madison argues that a liberty is not to be abolished merely because it feeds the conflict it makes possible",
     "The fair elections side, since Madison argues that liberty should be restricted to prevent faction",
     "Neither side, since Madison argues that faction is impossible in a republic",
     "Both sides equally, since Madison reaches no conclusion about liberty",
     "The fair elections side, since Madison recommends limits on political spending"], ans=0,
   why="Madison's air and fire comparison concludes that abolishing a liberty to suppress what it nourishes would be folly, which is a general argument against curing conflict by removing freedom. EK 5.11.A.2 names free speech as one of the two goods in the campaign finance dispute, and this reasoning bears on that half."),

 dict(q="Read the following excerpt.\n\n“The regulation of these various and interfering interests forms the principal task of modern legislation, and involves the spirit of party and faction in the necessary and ordinary operations of the government.”\n—James Madison, Federalist No. 10, 1787\n\nHow might a defender of campaign finance regulation use this passage?",
   choices=[
     "To argue that regulating competing interests is an ordinary legislative task rather than an unusual intrusion, which supports the competitive and fair elections side of the debate",
     "To argue that legislatures should never regulate competing interests",
     "To argue that the spirit of party has no place in government",
     "To argue that Madison wrote in favor of the Bipartisan Campaign Reform Act",
     "To argue that only courts, and never legislatures, may act on faction"], ans=0,
   why="Madison calls the regulation of interfering interests the principal task of modern legislation, which treats such regulation as normal rather than exceptional. Madison could not have addressed a statute enacted more than two centuries after the essay, which is why the key describes a use of the reasoning rather than an endorsement."),

 dict(q="The CED's suggested activity for this topic's skill asks students to relate the reasoning, decision, and opinion in Citizens United v. Federal Election Commission (2010) to Madison's argument in Federalist No. 10. What kind of task is that?",
   choices=[
     "Explaining how a required Supreme Court case relates to a foundational document",
     "Comparing a required Supreme Court case with a case that is not required",
     "Describing patterns and trends in a set of quantitative data",
     "Articulating a defensible claim and supporting it with evidence",
     "Explaining the limitations of a visual representation of data"], ans=0,
   why="Skill 2.B is stated as explaining how a required Supreme Court case relates to a foundational document or other source, and Federalist No. 10 is a required foundational document. Comparing a required case with a non-required one is a different skill in the same category."),

 dict(q="A student relating Citizens United v. Federal Election Commission (2010) to Federalist No. 10 writes only that both concern politics. Why is that insufficient for the skill this topic practices?",
   choices=[
     "Because the skill asks what the case and the document have in common and why, which requires naming a shared principle rather than a shared subject",
     "Because the skill asks only for the date each was produced",
     "Because the skill forbids using foundational documents with cases",
     "Because Federalist No. 10 is not a foundational document in this course",
     "Because Citizens United is not a required Supreme Court case"], ans=0,
   why="Skill 2.B asks a student to explain what the document and the case have in common and why, so a shared topic is the starting point rather than the answer. Both are course material the CED attaches to this learning objective, which is why the pairing is assigned at all."),

 dict(q="A state law forbids a nonprofit corporation from spending its own funds on advertisements that support or oppose candidates. Which required Supreme Court case would a challenger most plausibly rely on?",
   choices=[
     "Citizens United v. Federal Election Commission (2010), because it treated political spending by organizations as protected speech",
     "Shaw v. Reno (1993), because it concerned the drawing of legislative districts",
     "United States v. Lopez (1995), because it concerned the limits of the commerce power",
     "Wisconsin v. Yoder (1972), because it concerned the free exercise of religion",
     "Gideon v. Wainwright (1963), because it concerned the right to counsel"], ans=0,
   why="The scenario is an organization prevented from spending its funds on election advertising, which is the situation the CED's stated holding addresses. Each other case is stated by the CED as resolving an entirely different constitutional question."),

 dict(q="A student writes that Citizens United v. Federal Election Commission (2010) held that corporations may give unlimited amounts directly to candidates. What is the most important correction?",
   choices=[
     "The holding the CED states concerns political spending as protected speech and says nothing about direct contributions to candidates",
     "The holding concerned only labor unions and not corporations",
     "The Court held that political spending is not protected by the First Amendment",
     "The case concerned freedom of the press rather than political spending",
     "The case was decided before the Bipartisan Campaign Reform Act of 2002"], ans=0,
   why="The CED gives the holding as political spending by corporations, associations and labor unions being a form of protected speech, and spending money to speak and giving money to a candidate are different acts. Attributing to a required case something the framework does not state is the error the correction identifies."),

 dict(q=_ORGS + " Which conclusion is best supported by the data?",
   table=_ORGS_TABLE,
   choices=[
     "The organization that raised the most money devoted the largest share to advertising and the smallest share to candidate committees",
     "The organization that raised the most money devoted the largest share to candidate committees",
     "Every organization gave more than half its funds to candidate committees",
     "The organization that raised the least money spent the largest share on advertising",
     "All four organizations spent identical shares on advertising"], ans=0,
   why="The largest fundraiser reports 78 percent on advertising, the highest advertising share in the table, and 6 percent to candidate committees, the lowest such share. No organization gives more than half its funds to candidate committees, the largest such share being 48 percent."),

 dict(q=_ORGS + " Which framework statement do the second and third data columns together illustrate?",
   table=_ORGS_TABLE,
   choices=[
     "EK 5.11.A.3, since the columns show organizations influencing elections and policymaking through fundraising and spending",
     "EK 5.11.A.1.i, since the columns show the effect of the soft money ban",
     "The Stand by Your Ad provision, since the columns concern advertising content",
     "The CED's statement of the holding in a required Supreme Court case",
     "Learning objective 5.11.A's reference to the duration of national campaigns"], ans=0,
   why="The table reports what each organization raised and how it disposed of the money, which are the fundraising and spending EK 5.11.A.3 names as the means of influence. The advertising column measures how much was spent rather than what any advertisement said."),

 dict(q=_ORGS + " A student concludes from this table that the organization raising the most money supplied the most money to candidate committees. What is the most important correction?",
   table=_ORGS_TABLE,
   choices=[
     "A share must be applied to the amount raised, and a smaller fundraiser giving a much larger share supplied more dollars to candidate committees than the largest fundraiser did",
     "The table does not report how much any organization raised",
     "Every organization supplied the same number of dollars to candidate committees",
     "The largest fundraiser gave the largest share to candidate committees",
     "Shares and dollar amounts always rank organizations in the same order"], ans=0,
   why="The largest fundraiser gives 6 percent of 4800 thousand dollars, which is 288 thousand, while the organization raising 2500 thousand gives 35 percent of it, which is 875 thousand. A percentage of a larger base is not automatically a larger quantity, and this table is built so that it is not."),

 dict(q=_VIEWS + " Which conclusion is best supported by the data?",
   table=_VIEWS_TABLE,
   choices=[
     "A majority of every group agrees with each of the two statements, and roughly a quarter of every group agrees with both",
     "A majority of every group rejects both statements",
     "No respondent group contains anyone who agrees with both statements",
     "Agreement that limits protect fair elections rises steadily with age",
     "Agreement that limits restrict free speech falls steadily with age"], ans=0,
   why="Every entry in the first two data columns exceeds 50 percent, and the both statements column runs from 23 to 27 percent across the four groups. Agreement that limits protect fair elections falls with age while agreement that limits restrict free speech rises, which is the reverse of two of the options."),

 dict(q=_VIEWS + " Which framework statement does the pattern in the first two data columns most directly illustrate?",
   table=_VIEWS_TABLE,
   choices=[
     "EK 5.11.A.2, since the columns measure support for the two goods the framework says the debate is between",
     "EK 5.11.A.1.i, since the columns measure support for the soft money ban",
     "EK 5.11.A.3, since the columns measure the activity of different types of PACs",
     "The CED's statement of the holding in a required Supreme Court case",
     "Learning objective 5.11.A's reference to campaign organization"], ans=0,
   why="EK 5.11.A.2 names free speech and competitive and fair elections as the two concerns in the increased debate, and the two columns measure agreement with a statement about each. The columns move in opposite directions across the groups, which is what a debate between two goods looks like in data."),

 dict(q=_VIEWS + " A student concludes from this table that respondents divide into two camps, one holding each view. What is the most important correction?",
   table=_VIEWS_TABLE,
   choices=[
     "The two agreement shares sum to more than the whole in every group, so some respondents must accept both statements, and the final column reports that they do",
     "The two agreement shares sum to less than the whole in every group, so some respondents accept neither statement",
     "The table reports no overlap between the two groups of respondents",
     "The table shows that no respondent agrees that limits restrict free speech",
     "The table shows that the two statements are logically identical"], ans=0,
   why="Adding the first two data columns gives totals above 100 percent in every group, which is possible only if some respondents agree with both statements, and the third column reports shares from 23 to 27 percent doing exactly that. A debate between two goods can run inside a single respondent as well as between respondents."),
]
