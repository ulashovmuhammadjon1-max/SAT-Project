# AP U.S. GOVERNMENT AND POLITICS 4.5 Measuring Public Opinion -- 30 questions
# CED V.1 (c) 2026, Unit 4 American Political Ideologies and Beliefs.
# Learning objective 4.5.A: DESCRIBE THE ELEMENTS OF A SCIENTIFIC POLL.
# Suggested skill for this topic (CED p. 106): 3.C, data analysis -- EXPLAIN
# PATTERNS AND TRENDS IN DATA TO DRAW CONCLUSIONS.
#
# Essential knowledge relied on. Two statements, seven named items, and every
# one of them carries the framework's own parenthesis:
#   EK 4.5.A.1 -- public opinion data "that can affect elections and policy
#     debates is influenced by different TYPES of scientific polls such as:
#       i.   OPINION POLLS (measuring public opinion on various issues)
#       ii.  BENCHMARK POLLS (creating BASELINE views of a candidate)
#       iii. TRACKING POLLS (following HOW VIEWS OF A CANDIDATE CHANGE DURING A
#            CAMPAIGN)
#       iv.  EXIT POLLS (collecting data on WHY PEOPLE VOTED THE WAY THEY DID)"
#   EK 4.5.A.2 -- the same data "is influenced by POLLING METHODOLOGY. Polling
#     methodology is MORE PRECISE when it includes:
#       i.   Accurate SAMPLING methods, INCLUDING CALCULATING A MARGIN OF ERROR
#       ii.  NEUTRAL FRAMING of questions (specific and unbiased wording)
#       iii. ACCURATE REPORTING (clear reporting and conclusions that CAN BE
#            SUPPORTED BY THE DATA)"
#
# THE FOUR POLL TYPES ARE DISTINGUISHED BY PURPOSE, NOT BY TIMING. Three of them
# concern a candidate and two of those happen during a campaign, so the tempting
# way to sort them -- before, during, after -- gets benchmark and tracking right
# by accident and exit polls wrong on the point that matters. An exit poll is
# defined by WHY people voted the way they did, not by when it is taken and not
# by who won. Items 3 to 9 turn on purpose, and the verifier refuses any key
# that gives one type another's parenthesis.
#
# "MORE PRECISE" IS A COMPARATIVE, AND THE FRAMEWORK CHOSE IT. EK 4.5.A.2 does
# not divide polls into accurate and inaccurate; it says methodology is MORE
# PRECISE when it includes three things. A poll missing one of them is worse
# methodology, not a non-poll, and a poll including all three is not thereby
# correct. Items 15 and 16 make the comparative the question.
#
# WHY THE MARGIN OF ERROR IS THE HINGE OF THIS TOPIC. It sits inside EK
# 4.5.A.2.i as part of ACCURATE SAMPLING, and it is the only element of the
# seven that changes what a reader may CONCLUDE from a number rather than how
# the number was produced. A lead smaller than the margin of error does not
# establish a lead, and reporting one as though it did fails EK 4.5.A.2.iii's
# standard that conclusions be supportable by the data. The suggested skill for
# this topic is 3.C -- explain patterns and trends in data TO DRAW CONCLUSIONS
# -- so items 24, 29 and 30 are built on exactly that limit.
#
# The CED attaches no foundational document and no required case to 4.5.A. All
# three tables are labelled hypothetical and nothing here is quoted.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("4.5", "Measuring Public Opinion", 4)

_TRACKING = ("A hypothetical polling organization surveyed voters four times during one "
             "campaign, asking the same question each time. Each poll reported a margin of "
             "error of 3 percentage points.")
_TRACKING_TABLE = dict(
    headers=["Week of the campaign", "Candidate A (%)", "Candidate B (%)", "Undecided (%)"],
    rows=[["Week 1", "38", "35", "27"],
          ["Week 4", "40", "37", "23"],
          ["Week 8", "43", "41", "16"],
          ["Week 12", "45", "44", "11"]])

_WORDING = ("Four hypothetical polls asked about the same proposal in the same week, using "
            "different wording. The table reports the share expressing support in each.")
_WORDING_TABLE = dict(
    headers=["Wording of the question asked", "Expressed support (%)"],
    rows=[["Do you favor or oppose the proposal?", "48"],
          ["Do you favor or oppose the proposal, which experts say would help families?", "67"],
          ["Do you favor or oppose the costly proposal?", "34"],
          ["Do you support the proposal that would finally fix the problem?", "71"]])

_SAMPLES = ("Four hypothetical polls of the same electorate were released in the same week. The "
            "table reports each poll's sample size, its reported margin of error, and the lead "
            "it reported for one candidate.")
_SAMPLES_TABLE = dict(
    headers=["Poll", "Sample size", "Reported margin of error (percentage points)",
             "Reported lead for Candidate A (percentage points)"],
    rows=[["Poll 1", "400", "5", "3"],
          ["Poll 2", "1000", "3", "3"],
          ["Poll 3", "1600", "2", "3"],
          ["Poll 4", "2500", "2", "6"]])

QUESTIONS = [
 dict(q="According to the course framework, what two things can public opinion data affect?",
   choices=[
     "Elections and policy debates",
     "Court decisions and constitutional amendments",
     "Treaty ratification and military deployment",
     "Judicial appointments and impeachment trials",
     "State ratification of federal statutes"], ans=0,
   why="Both EK 4.5.A.1 and EK 4.5.A.2 open with the same phrase, 'public opinion data that can affect elections and policy debates'. That phrase is what makes polling methodology a subject of this course rather than of statistics alone."),

 dict(q="EK 4.5.A.1 introduces its list with the phrase SUCH AS. What does that indicate about the four types of poll it names?",
   choices=[
     "That they are examples rather than a complete catalogue of scientific polls",
     "That they are the only four types of poll that exist",
     "That they are ranked in order of accuracy",
     "That each is used only once per campaign",
     "That the framework rejects the four it names"], ans=0,
   why="EK 4.5.A.1 says data is influenced by different types of scientific polls SUCH AS the four listed, which marks the list as illustrative. A question treating the four as exhaustive would assert a completeness the framework does not claim."),

 dict(q="According to the course framework, what does an OPINION POLL measure?",
   choices=[
     "Public opinion on various issues",
     "Baseline views of a candidate",
     "How views of a candidate change during a campaign",
     "Why people voted the way they did",
     "The number of votes each candidate received"], ans=0,
   why="EK 4.5.A.1.i's parenthesis is 'measuring public opinion on various issues'. Each of the other four options is the parenthesis the framework attaches to a different type of poll, or is not a poll at all."),

 dict(q="According to the course framework, what does a BENCHMARK POLL do?",
   choices=[
     "Creates baseline views of a candidate",
     "Measures public opinion on various issues",
     "Follows how views of a candidate change during a campaign",
     "Collects data on why people voted the way they did",
     "Determines the official result of an election"], ans=0,
   why="EK 4.5.A.1.ii's parenthesis is 'creating baseline views of a candidate'. The framework's word BASELINE is what makes it a starting measurement that later polls are compared against."),

 dict(q="According to the course framework, what does a TRACKING POLL do?",
   choices=[
     "Follows how views of a candidate change during a campaign",
     "Creates baseline views of a candidate",
     "Measures public opinion on various issues",
     "Collects data on why people voted the way they did",
     "Counts the ballots cast on election day"], ans=0,
   why="EK 4.5.A.1.iii's parenthesis is 'following how views of a candidate change during a campaign'. Its distinguishing feature is repetition over time, which is what allows change to be observed at all."),

 dict(q="According to the course framework, what does an EXIT POLL collect?",
   choices=[
     "Data on why people voted the way they did",
     "Baseline views of a candidate before a campaign begins",
     "Public opinion on various issues unrelated to any candidate",
     "The official certified vote totals",
     "The number of registered voters in a district"], ans=0,
   why="EK 4.5.A.1.iv's parenthesis is 'collecting data on why people voted the way they did'. The framework defines it by its subject, the reasons behind a vote, and not by the fact that it is taken on election day."),

 dict(q="A student sorts the four poll types by when each is taken: before a campaign, during it, and after voting. Which type does that sorting describe least accurately?",
   choices=[
     "Exit polls, because the framework defines them by the reasons behind a vote rather than by their timing",
     "Benchmark polls, because the framework defines them by their timing",
     "Tracking polls, because the framework says nothing about a campaign",
     "Opinion polls, because the framework says they occur only after an election",
     "None of them, because the framework defines all four by timing"], ans=0,
   why="Three of EK 4.5.A.1's parentheses mention a candidate or a campaign, so timing sorts them roughly right. But EK 4.5.A.1.iv defines an exit poll by what it collects, data on WHY people voted as they did, and a poll taken after voting that asked something else would not be one."),

 dict(q="A campaign commissions a poll before it begins advertising, in order to have a measurement to compare later polls against. Which type is this?",
   choices=[
     "A benchmark poll, since it creates baseline views of a candidate",
     "A tracking poll, since it will be compared with later polls",
     "An exit poll, since it precedes the vote",
     "An opinion poll, since it concerns a candidate",
     "None of the four, since the framework covers only polls taken during a campaign"], ans=0,
   why="EK 4.5.A.1.ii defines a benchmark poll by the creation of baseline views of a candidate, which is exactly the purpose described. That later polls are compared against it is what a baseline is for, not what makes something a tracking poll."),

 dict(q="A news organization surveys voters as they leave polling places, asking which issues most affected their choice. Which type is this?",
   choices=[
     "An exit poll, since it collects data on why people voted the way they did",
     "A tracking poll, since it is taken at the end of a campaign",
     "A benchmark poll, since it establishes a final measurement",
     "An opinion poll, since it asks about issues",
     "None of the four, since votes have already been cast"], ans=0,
   why="EK 4.5.A.1.iv's parenthesis is data on why people voted the way they did, and asking which issues affected a choice is that. The mention of issues does not make it an opinion poll, because the question is tied to a vote already cast."),

 dict(q="According to EK 4.5.A.2, what else influences public opinion data besides the type of poll?",
   choices=[
     "Polling methodology",
     "The number of candidates in the race",
     "The month in which the election is held",
     "The size of the state being surveyed",
     "The party affiliation of the respondents"], ans=0,
   why="EK 4.5.A.2 states that public opinion data affecting elections and policy debates is influenced by polling methodology, and then lists three things that make methodology more precise."),

 dict(q="Which three things does EK 4.5.A.2 say make polling methodology more precise?",
   choices=[
     "Accurate sampling methods, neutral framing of questions, and accurate reporting",
     "Large sample size, rapid publication, and media coverage",
     "Random dialing, weekend interviewing, and repeated calls",
     "Party balance, geographic spread, and age quotas",
     "Government certification, academic review, and public funding"], ans=0,
   why="EK 4.5.A.2 lists exactly these three. Each carries its own parenthesis in the framework, and none of the other options appears in the statement at all."),

 dict(q="What does EK 4.5.A.2 say accurate sampling methods include?",
   choices=[
     "Calculating a margin of error",
     "Interviewing every eligible voter",
     "Publishing the results before the election",
     "Weighting responses by party registration",
     "Excluding respondents who are undecided"], ans=0,
   why="EK 4.5.A.2.i's own words are 'accurate sampling methods, including calculating a margin of error'. The framework places the margin of error inside sampling rather than treating it as a separate element."),

 dict(q="According to the course framework, what does NEUTRAL FRAMING of questions mean?",
   choices=[
     "Specific and unbiased wording of questions",
     "Asking the same question in every poll",
     "Asking questions only about candidates",
     "Allowing respondents to write their own answers",
     "Asking questions in the order the client prefers"], ans=0,
   why="EK 4.5.A.2.ii's parenthesis is 'specific and unbiased wording of questions'. Both adjectives are the framework's own: a question can be unbiased and still too vague to interpret, and specific while still leading."),

 dict(q="According to the course framework, what does ACCURATE REPORTING require?",
   choices=[
     "Clear reporting, and conclusions that can be supported by the data",
     "Publishing only results that favor the sponsor",
     "Reporting the sample size but not the questions",
     "Withholding results until after an election",
     "Reporting only the results that agree with other polls"], ans=0,
   why="EK 4.5.A.2.iii's parenthesis is 'clear reporting and conclusions that can be supported by the data'. The second half is a limit on what may be claimed, which is what distinguishes this element from the two that concern how the data were gathered."),

 dict(q="EK 4.5.A.2 says polling methodology is MORE PRECISE when it includes the three elements. What does that comparative wording indicate?",
   choices=[
     "That the three elements improve methodology by degree rather than dividing polls into valid and invalid ones",
     "That a poll lacking any one of them is not a poll at all",
     "That a poll including all three is guaranteed to be correct",
     "That precision is unrelated to methodology",
     "That only one of the three is actually necessary"], ans=0,
   why="The framework's phrase is MORE PRECISE, a comparative, so the three elements describe a scale rather than a threshold. A poll missing one is worse methodology, and a poll including all three can still be wrong about the electorate."),

 dict(q="A poll uses careful sampling and neutral wording, but its published summary claims a conclusion the numbers do not support. Which element of EK 4.5.A.2 does it fail?",
   choices=[
     "Accurate reporting, since the framework requires conclusions that can be supported by the data",
     "Accurate sampling, since the sample must have been wrong",
     "Neutral framing, since the wording must have been biased",
     "None, since the data themselves were properly collected",
     "All three equally, since the poll was published"], ans=0,
   why="EK 4.5.A.2.iii is the element that governs what may be claimed from data already gathered, and the stem states that the first two were done well. A poll can be collected properly and reported beyond its evidence, which is why the framework lists reporting separately."),

 dict(q="Why does the framework treat the margin of error as part of accurate sampling rather than as a separate element?",
   choices=[
     "Because it is a property of how the sample was drawn, expressing the uncertainty that sampling a subset rather than everyone creates",
     "Because it is calculated after the results are reported",
     "Because it describes how the questions were worded",
     "Because it measures how many respondents refused to answer",
     "Because it is required by law rather than by methodology"], ans=0,
   why="EK 4.5.A.2.i names accurate sampling methods 'including calculating a margin of error', which places the calculation inside sampling. The margin exists because a poll measures some of the population rather than all of it."),

 dict(q="Two polls of the same electorate in the same week report different results. Which explanation is most consistent with EK 4.5.A.2?",
   choices=[
     "Differences in methodology, such as how the sample was drawn or how the questions were worded, can produce different data from the same electorate",
     "One of the two polls must have been fabricated",
     "Public opinion must have changed within the week",
     "The two polls must have surveyed different countries",
     "Polls of the same electorate never differ"], ans=0,
   why="EK 4.5.A.2's whole claim is that public opinion data is influenced by polling methodology, and it names sampling and question wording among the influences. Divergent results from one electorate are what that claim predicts."),

 dict(q="LO 4.5.A asks students to DESCRIBE the elements of a scientific poll. Which of the following is an element in the framework's sense?",
   choices=[
     "The sampling method used, including the margin of error calculated from it",
     "The name of the organization that paid for the poll",
     "The day of the week on which interviews were conducted",
     "The number of polls released that month",
     "The eventual result of the election"], ans=0,
   why="EK 4.5.A.2 lists sampling, question framing and reporting as what makes methodology more precise, and EK 4.5.A.2.i names the margin of error inside sampling. The other four options are facts about a poll that the framework nowhere makes elements of one."),

 dict(q="A poll's reported lead for one candidate is smaller than its margin of error. What conclusion does EK 4.5.A.2 support?",
   choices=[
     "The poll does not establish that either candidate leads, and reporting one as leading would exceed what the data support",
     "The candidate with the higher number is leading, since the numbers are what was measured",
     "The poll should be disregarded entirely",
     "The margin of error should be recalculated until the lead exceeds it",
     "The poll shows the two candidates are exactly tied"], ans=0,
   why="EK 4.5.A.2.i makes the margin of error part of accurate sampling and EK 4.5.A.2.iii requires conclusions that can be supported by the data. A difference inside the margin is not distinguishable from no difference, and the poll is neither useless nor evidence of an exact tie."),

 dict(q="Which of the following does the course framework NOT state about scientific polls?",
   choices=[
     "Which of the four types of poll produces the most reliable data",
     "That opinion polls measure public opinion on various issues",
     "That accurate sampling includes calculating a margin of error",
     "That neutral framing means specific and unbiased wording",
     "That accurate reporting requires conclusions supportable by the data"], ans=0,
   why="EK 4.5.A.1 lists four types without ranking them, and EK 4.5.A.2's three elements apply to any of them. Every other option restates one of the framework's own parentheses."),

 dict(q=_TRACKING + " Which conclusion is best supported by the data?",
   table=_TRACKING_TABLE,
   choices=[
     "Both candidates gained support across the campaign while the undecided share fell, and the gap between the two candidates narrowed",
     "Both candidates lost support across the campaign",
     "The undecided share rose across the campaign",
     "The gap between the two candidates widened across the campaign",
     "Neither candidate's share changed across the campaign"], ans=0,
   why="Candidate A runs 38, 40, 43, 45 and Candidate B runs 35, 37, 41, 44, while the undecided share falls from 27 to 11. The gap between the candidates narrows from 3 points to 1."),

 dict(q=_TRACKING + " Which type of poll named in EK 4.5.A.1 does this series best illustrate?",
   table=_TRACKING_TABLE,
   choices=[
     "A tracking poll, since it follows how views of a candidate change during a campaign",
     "A benchmark poll, since the first week creates a baseline",
     "An exit poll, since the last week is near the election",
     "An opinion poll, since it measures public opinion",
     "None of the four, since the same question was asked each time"], ans=0,
   why="EK 4.5.A.1.iii's parenthesis is following how views of a candidate change during a campaign, and repeating one question at four points in a campaign is that. A benchmark poll is a single baseline measurement rather than a series."),

 dict(q=_TRACKING + " In the final week, what conclusion about the two candidates does the data support?",
   table=_TRACKING_TABLE,
   choices=[
     "Neither candidate can be said to lead, since the difference between them is smaller than the reported margin of error",
     "Candidate A leads, since the reported figure is higher",
     "Candidate B leads, since the candidate gained more across the campaign",
     "The two candidates are exactly tied at equal support",
     "No conclusion is possible, since the undecided share is not zero"], ans=0,
   why="Week 12 reports 45 against 44, a difference of 1 point against a reported margin of error of 3. EK 4.5.A.2.iii requires conclusions supportable by the data, and a gap inside the margin is not distinguishable from no gap, which is also not a finding of an exact tie."),

 dict(q=_WORDING + " Which conclusion is best supported by the data?",
   table=_WORDING_TABLE,
   choices=[
     "The wording of the question moved reported support by 37 percentage points, from 34 to 71, for the same proposal in the same week",
     "The four wordings produced nearly identical results",
     "Support for the proposal fell over the course of the week",
     "The wording of a question has no measurable effect on reported support",
     "Only one of the four wordings produced any support at all"], ans=0,
   why="The support column reads 48, 67, 34 and 71, so the highest and lowest differ by 37 points. The stem states that all four polls were taken in the same week about the same proposal, which rules out an explanation based on changing opinion."),

 dict(q=_WORDING + " Which element of EK 4.5.A.2 does this table bear on most directly?",
   table=_WORDING_TABLE,
   choices=[
     "Neutral framing of questions, which the framework glosses as specific and unbiased wording",
     "Accurate sampling methods, including calculating a margin of error",
     "Accurate reporting, meaning conclusions supportable by the data",
     "The distinction between benchmark and tracking polls",
     "The definition of an exit poll"], ans=0,
   why="EK 4.5.A.2.ii is the element concerned with how a question is worded, and the table holds the sample, the proposal and the week constant while varying only the wording. The other two elements concern how respondents were selected and what was claimed afterward."),

 dict(q=_WORDING + " Which of the four wordings best satisfies the framework's standard of neutral framing?",
   table=_WORDING_TABLE,
   choices=[
     "The wording that asks whether the respondent favors or opposes the proposal without describing it further",
     "The wording that mentions what experts say the proposal would do",
     "The wording that calls the proposal costly",
     "The wording that says the proposal would finally fix the problem",
     "None of them, since every question influences the answer"], ans=0,
   why="EK 4.5.A.2.ii's gloss is specific and unbiased wording. Three of the four wordings attach a characterization to the proposal before asking about it, and only the plain favor or oppose question offers both alternatives without one."),

 dict(q=_SAMPLES + " Which pattern in the data is best supported?",
   table=_SAMPLES_TABLE,
   choices=[
     "As sample size rises across the four polls, the reported margin of error falls or stays the same",
     "As sample size rises, the reported margin of error rises",
     "The reported margin of error is the same in all four polls",
     "Sample size and margin of error are unrelated in this table",
     "The largest poll reports the largest margin of error"], ans=0,
   why="Sample sizes run 400, 1000, 1600 and 2500 while the margins run 5, 3, 2 and 2, so the margin never rises as the sample grows. The last two polls share a margin of 2 despite different sample sizes, which is why the pattern is stated as falls or stays the same."),

 dict(q=_SAMPLES + " In which polls does the reported lead exceed the reported margin of error?",
   table=_SAMPLES_TABLE,
   choices=[
     "Polls 3 and 4 only",
     "Poll 4 only",
     "Polls 1 and 2 only",
     "All four polls",
     "None of the four polls"], ans=0,
   why="Comparing the last two columns gives 3 against 5, 3 against 3, 3 against 2 and 6 against 2. Only the third and fourth polls report a lead larger than their own margin, and Poll 2's lead exactly equals its margin rather than exceeding it."),

 dict(q=_SAMPLES + " A student concludes from Poll 1 that Candidate A is leading. What is the most important correction?",
   table=_SAMPLES_TABLE,
   choices=[
     "Poll 1 reports a lead of 3 points against a margin of error of 5, so the lead is inside the margin and the poll does not establish one",
     "Poll 1 reports no lead for either candidate",
     "Poll 1 has the largest sample of the four polls",
     "Poll 1 reports the smallest margin of error of the four polls",
     "The table reports margins of error but not leads"], ans=0,
   why="Poll 1's reported lead of 3 points sits inside its reported margin of 5, so the difference is not distinguishable from none. EK 4.5.A.2.iii requires conclusions that can be supported by the data, and this one is not, even though the reported figure is real."),
]
