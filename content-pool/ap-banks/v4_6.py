# AP U.S. GOVERNMENT AND POLITICS 4.6 Evaluating Public Opinion Data
# -- 30 questions
# CED V.1 (c) 2026, Unit 4 American Political Ideologies and Beliefs.
# Learning objective 4.6.A: explain the QUALITY AND CREDIBILITY of claims based
# on public opinion data.
# Suggested skill for this topic (CED p. 107): 3.D, data analysis -- explain what
# the data IMPLIES OR ILLUSTRATES about political principles, institutions,
# processes, policies, and behaviors.
#
# Essential knowledge relied on. One statement, two factors:
#   EK 4.6.A.1 -- "The relationship between scientific polling and elections and
#     policy debates is affected by the:
#       i.  IMPORTANCE OF PUBLIC OPINION as a source of political influence IN A
#           GIVEN election or policy debate
#       ii. RELIABILITY AND VERACITY of public opinion data"
#
# TWO INDEPENDENT WAYS A POLLING-BASED CLAIM CAN FAIL, AND THE FIRST IS THE ONE
# THAT GETS LOST. Topic 4.5 was entirely about how data are produced, so the
# natural reading of 4.6 is "and here is more about data quality". It is not.
# EK 4.6.A.1's FIRST factor is not about the data at all: it is about how much
# public opinion actually bears on the outcome IN A GIVEN case. A poll can be
# impeccably conducted, accurately reported, and still tell you nothing about
# what a legislature will do, because opinion is one source of influence among
# others and its weight varies from debate to debate. Collapsing the topic into
# factor ii is the error this module is built against, and the verifier's
# _two_factors gate refuses it.
#
# The two tables that carry the distinction are a matched pair. The polls-and-
# outcomes table varies only the DATA question: did the polling hold up. The
# support-and-adoption table holds the data fixed and varies the INFLUENCE
# question: did majority support decide anything. Item 27 is the hinge -- data
# that were perfectly accurate still failed to predict adoption, and EK 4.6.A.1
# names that as a separate factor rather than as evidence the poll was wrong.
#
# "RELIABILITY AND VERACITY" IS TWO WORDS. Reliability is whether the same
# procedure would produce the same result; veracity is whether the result is
# truthful about what it claims to describe. A poll can be reliable and not
# veracious -- a consistently leading question produces a consistent wrong
# answer. Items 5 and 6 keep both.
#
# NO REAL ELECTION IS NAMED ANYWHERE IN THIS MODULE. The CED lists three
# elections against this topic and marks all three ILLUSTRATIVE EXAMPLES (NOT
# REQUIRED), exactly as it does for the cases in 3.13. Naming one would put
# content the exam cannot ask about beside content it can, and here the
# temptation is unusually strong because the famous polling misses are the first
# thing anyone reaches for. Item 16 makes the required-versus-illustrative
# distinction the question instead, and the verifier enforces the refusal.
#
# The CED attaches no foundational document and no required case to 4.6.A. All
# three tables are labelled hypothetical.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("4.6", "Evaluating Public Opinion Data", 4)

_OUTCOMES = ("A hypothetical study compared final polling with results in four contests. Each "
             "row reports the lead the polling leader held, the margin of error reported with "
             "that polling, and what happened to that candidate.")
_OUTCOMES_TABLE = dict(
    headers=["Contest", "Final lead for the polling leader (percentage points)",
             "Reported margin of error (percentage points)", "Outcome for the polling leader"],
    rows=[["Contest 1", "8", "3", "Won by 9"],
          ["Contest 2", "4", "3", "Won by 1"],
          ["Contest 3", "2", "3", "Lost by 3"],
          ["Contest 4", "6", "2", "Won by 5"]])

_ADOPTION = ("A hypothetical study of four policy debates recorded the share of the public "
             "supporting each proposal, measured by well conducted polls, and whether the "
             "proposal was adopted.")
_ADOPTION_TABLE = dict(
    headers=["Policy debate", "Public support for the proposal (%)", "Proposal adopted?"],
    rows=[["Debate 1", "72", "Yes"],
          ["Debate 2", "68", "No"],
          ["Debate 3", "44", "Yes"],
          ["Debate 4", "31", "No"]])

_RESPONSE = ("Four hypothetical polls of the same electorate reported how many people they "
             "contacted, how many completed an interview, and the resulting response rate.")
_RESPONSE_TABLE = dict(
    headers=["Poll", "People contacted", "Completed an interview", "Response rate (%)"],
    rows=[["Poll A", "4000", "1200", "30"],
          ["Poll B", "9000", "900", "10"],
          ["Poll C", "2500", "1000", "40"],
          ["Poll D", "20000", "1000", "5"]])

QUESTIONS = [
 dict(q="According to the course framework, what two things affect the relationship between scientific polling and elections and policy debates?",
   choices=[
     "The importance of public opinion as a source of political influence in a given case, and the reliability and veracity of the data",
     "The reliability of the data and the speed with which it is published",
     "The importance of public opinion and the number of polls conducted",
     "The sample size and the identity of the polling organization",
     "The cost of the poll and the season in which it is taken"], ans=0,
   why="EK 4.6.A.1 names exactly two factors, and only one of them concerns the data. The other concerns how much public opinion actually bears on the outcome in the particular election or debate at issue."),

 dict(q="Which of EK 4.6.A.1's two factors is NOT about the poll itself?",
   choices=[
     "The importance of public opinion as a source of political influence in a given election or policy debate",
     "The reliability of public opinion data",
     "The veracity of public opinion data",
     "The sampling method used",
     "The wording of the questions asked"], ans=0,
   why="EK 4.6.A.1.i concerns the weight public opinion carries in a particular case, which is a fact about the political setting rather than about how the poll was conducted. Sampling and wording belong to EK 4.5.A.2's account of methodology."),

 dict(q="EK 4.6.A.1's first factor includes the phrase IN A GIVEN election or policy debate. What does that phrase indicate?",
   choices=[
     "That the weight public opinion carries varies from case to case rather than being fixed",
     "That public opinion carries the same weight in every case",
     "That public opinion carries weight only in elections",
     "That public opinion carries weight only in policy debates",
     "That public opinion never carries any weight"], ans=0,
   why="The framework attaches the importance of public opinion to a GIVEN election or debate rather than stating it in general. A factor that varies by case is one that has to be assessed case by case, which is what LO 4.6.A asks students to do."),

 dict(q="A poll is well sampled, neutrally worded, and accurately reported, and its findings still do not predict what a legislature does. Which of EK 4.6.A.1's factors best explains this?",
   choices=[
     "The importance of public opinion as a source of influence in that particular debate, which may be limited whatever the data show",
     "The reliability of the data, which must have been poor",
     "The veracity of the data, which must have been misstated",
     "The sampling method, which must have been unrepresentative",
     "The question wording, which must have been biased"], ans=0,
   why="The stem stipulates that every element of EK 4.5.A.2's methodology was satisfied, so the failure cannot be located in the data. EK 4.6.A.1.i names the other factor: opinion is one source of influence among others and its weight varies by debate."),

 dict(q="What does RELIABILITY of public opinion data refer to?",
   choices=[
     "Whether the same procedure applied again would produce the same result",
     "Whether the finding agrees with the analyst's expectations",
     "Whether the poll was published quickly",
     "Whether the poll was paid for by a neutral party",
     "Whether a majority of respondents agreed with one another"], ans=0,
   why="EK 4.6.A.1.ii pairs reliability with veracity as two properties of the data. Reliability concerns consistency of the procedure; veracity concerns whether the result is truthful about what it claims to describe."),

 dict(q="Why does EK 4.6.A.1 name both RELIABILITY and VERACITY rather than only one of them?",
   choices=[
     "Because a poll can be consistent and still not truthful, as when a leading question reliably produces the same distorted answer",
     "Because the two words mean exactly the same thing",
     "Because reliability applies to elections and veracity to policy debates",
     "Because veracity concerns the sponsor and reliability the sample",
     "Because only one of the two can be assessed at a time"], ans=0,
   why="Consistency and truthfulness come apart: EK 4.5.A.2.ii's biased wording would produce the same slanted result every time it was used, which is reliable and not veracious. Naming both makes each separately checkable."),

 dict(q="LO 4.6.A asks students to explain the QUALITY AND CREDIBILITY of claims based on public opinion data. Which pair of questions does that objective require?",
   choices=[
     "Whether the data support the claim, and whether public opinion is the kind of influence that bears on the outcome the claim is about",
     "Whether the poll was expensive, and whether it was widely reported",
     "Whether the claim is popular, and whether it agrees with other claims",
     "Whether the claim concerns an election, and whether it concerns a policy debate",
     "Whether the poll had a large sample, and whether it was recent"], ans=0,
   why="EK 4.6.A.1's two factors are the two things the objective is built on, and a claim can fail either test independently. Evaluating only the data would answer half the objective's question."),

 dict(q="Why is the distinction between EK 4.6.A.1's two factors easy to lose?",
   choices=[
     "Because the preceding topic concerns how polls are conducted, so the natural reading of this one is more about data quality",
     "Because the framework states only one factor",
     "Because the two factors are defined in the same words",
     "Because the framework says the two factors always agree",
     "Because neither factor concerns polling"], ans=0,
   why="Topic 4.5 is entirely about the elements of a scientific poll, so a reader arrives at 4.6 primed to evaluate data. EK 4.6.A.1's first factor is not about the data at all, which is what makes it the half that disappears."),

 dict(q="A commentator says a poll was accurate but irrelevant to the outcome of a policy debate. Under EK 4.6.A.1, is this a coherent thing to say?",
   choices=[
     "Yes, because accuracy concerns the second factor and relevance to the outcome concerns the first",
     "No, because an accurate poll is always relevant to the outcome",
     "No, because the framework recognizes only accuracy",
     "Yes, but only if the poll concerned an election rather than a policy debate",
     "No, because relevance is a property of the data"], ans=0,
   why="EK 4.6.A.1 separates the reliability and veracity of the data from the importance of public opinion in a given case, so the two can point in different directions. A claim can be well founded in data and still not bear on what happened."),

 dict(q="A claim states that because a proposal has 70 percent public support, it will be enacted. Which of EK 4.6.A.1's factors does the claim assume without examining?",
   choices=[
     "The importance of public opinion as a source of influence in that particular debate",
     "The reliability of the polling data",
     "The veracity of the polling data",
     "The sampling method behind the figure",
     "The wording of the question that produced the figure"], ans=0,
   why="The claim takes the figure at face value and moves straight to an outcome, which requires public opinion to be decisive in that debate. EK 4.6.A.1.i is precisely the assumption being skipped."),

 dict(q="Which of the following would most improve the credibility of a claim based on public opinion data?",
   choices=[
     "Showing both that the data were soundly produced and that public opinion carries weight in the case at issue",
     "Showing only that the sample was large",
     "Showing only that the poll agreed with another poll",
     "Showing only that the poll was recent",
     "Showing only that the claim is widely believed"], ans=0,
   why="LO 4.6.A pairs quality with credibility, and EK 4.6.A.1 supplies the two things a full showing must cover. Sample size, recency and agreement with other polls all bear on the second factor alone."),

 dict(q="Two polls of the same question, conducted the same week by different organizations using sound methods, report figures 4 percentage points apart. What does EK 4.6.A.1 suggest about this?",
   choices=[
     "Small differences between soundly conducted polls are expected, and neither poll is thereby shown to lack reliability or veracity",
     "One of the two organizations must have fabricated its data",
     "Public opinion must have changed within the week",
     "Both polls should be disregarded",
     "The larger figure is necessarily the more accurate one"], ans=0,
   why="EK 4.5.A.2.i places a margin of error inside accurate sampling, so two sound polls will differ by some amount as a matter of course. EK 4.6.A.1.ii asks whether data are reliable and veracious, and a difference of this size does not by itself answer either question against them."),

 dict(q="A poll reports that a proposal has majority support, and the proposal is not adopted. Which conclusion does EK 4.6.A.1 best support?",
   choices=[
     "Either the data were flawed or public opinion was not decisive in that debate, and the two possibilities have to be distinguished",
     "The poll was certainly inaccurate",
     "Public opinion certainly had no influence at all",
     "The legislature acted unconstitutionally",
     "The proposal must not have had majority support"], ans=0,
   why="EK 4.6.A.1 names two factors, so a mismatch between a poll and an outcome is consistent with a failure of either. Assigning the mismatch to the data without examining the first factor is the error the framework's two-part structure exists to prevent."),

 dict(q="Which of the following best describes what makes public opinion IMPORTANT as a source of political influence in a given case, in the framework's sense?",
   choices=[
     "The extent to which the decision at issue is responsive to what the public wants",
     "The number of people who were surveyed",
     "The number of news outlets that reported the poll",
     "The margin of error attached to the finding",
     "The share of respondents who said they were certain of their view"], ans=0,
   why="EK 4.6.A.1.i concerns public opinion as a SOURCE OF POLITICAL INFLUENCE in a particular election or debate, which is a question about how the decision gets made. The other four options are properties of a poll or its coverage."),

 dict(q="The CED lists several past elections alongside this topic and marks them as illustrative examples that are not required. What does that designation mean for a student preparing for the exam?",
   choices=[
     "They may help illustrate the two factors, but the exam will not require knowledge of them the way it requires the content of the essential knowledge statements",
     "They are required and must be memorized with their polling figures",
     "They are the only content the exam may test for this topic",
     "They replace the required case list for this unit",
     "They indicate that the framework rejects the examples it lists"], ans=0,
   why="The CED distinguishes required course content from ILLUSTRATIVE EXAMPLES marked NOT REQUIRED, and this topic's examples fall in the second category. Treating an illustrative example as required content misrepresents what the exam can ask."),

 dict(q="Which of the following does EK 4.6.A.1 NOT state?",
   choices=[
     "Which particular elections illustrate the limits of polling",
     "That the importance of public opinion varies by election or policy debate",
     "That the reliability of public opinion data affects the relationship",
     "That the veracity of public opinion data affects the relationship",
     "That polling stands in a relationship to elections and policy debates"], ans=0,
   why="EK 4.6.A.1 states two factors and names no election within the essential knowledge itself. The elections the CED lists for this topic are marked illustrative examples that are not required."),

 dict(q="How does topic 4.6 differ from topic 4.5?",
   choices=[
     "Topic 4.5 concerns how a poll is produced, while this topic concerns what may be concluded from polling in a particular political setting",
     "Topic 4.5 concerns elections and this topic concerns policy debates",
     "Topic 4.5 concerns data and this topic concerns a different kind of data",
     "The two topics cover the same content in different words",
     "Topic 4.5 concerns individuals and this topic concerns institutions"], ans=0,
   why="EK 4.5.A.1 and EK 4.5.A.2 list types of poll and elements of methodology; EK 4.6.A.1 adds the question of how much opinion matters in a given case. Both topics mention elections and policy debates, so that is not what separates them."),

 dict(q="A student evaluating a claim based on polling checks the sample, the wording, and the reporting, and concludes the claim is credible. What has the student not yet done?",
   choices=[
     "Assessed whether public opinion is an important source of influence in the case the claim concerns",
     "Assessed whether the poll had a margin of error",
     "Assessed whether the questions were specific",
     "Assessed whether the conclusions were supportable by the data",
     "Assessed whether the sample was drawn accurately"], ans=0,
   why="The three things checked are EK 4.5.A.2's three elements of methodology, which together answer EK 4.6.A.1's second factor. The first factor has not been touched, and LO 4.6.A's word CREDIBILITY covers both."),

 dict(q="Which question would a political scientist studying LO 4.6.A be most likely to ask about a claim based on polling?",
   choices=[
     "Do the data support this claim, and is public opinion the kind of influence that would shape the outcome it concerns?",
     "How many people read the poll when it was published?",
     "Which organization has published the most polls this year?",
     "What is the average sample size of polls in this country?",
     "How many polls were conducted during the last campaign?"], ans=0,
   why="LO 4.6.A asks about the quality and credibility of claims, and EK 4.6.A.1's two factors are what a full evaluation covers. Counting polls or readers answers neither factor."),

 dict(q="Which statement best describes the limit of what EK 4.6.A.1 establishes?",
   choices=[
     "It names two factors that affect the relationship between polling and outcomes, without stating how much weight either carries in any case",
     "It states which factor is more important",
     "It states that polling never predicts outcomes",
     "It states that polling always predicts outcomes",
     "It states which elections polling has failed to predict"], ans=0,
   why="EK 4.6.A.1 lists two factors and stops. Its own first factor says the importance of public opinion varies by case, which is itself a refusal to state a general weight, and the elections the CED lists for the topic are illustrative rather than required."),

 dict(q="The suggested skill for this topic asks students to explain what data IMPLIES OR ILLUSTRATES, rather than to describe it. What does that ask for beyond a description?",
   choices=[
     "A statement of what the pattern shows about how politics works, which requires connecting the numbers to a claim about influence or about the data itself",
     "A restatement of the largest and smallest figures in the table",
     "A calculation of the average of every column",
     "A judgment about whether the poll was expensive",
     "A prediction of the next figure in the series"], ans=0,
   why="Skill 3.D asks what data implies or illustrates about political principles, institutions, processes, policies and behaviors, which is a further step than reporting the figures. EK 4.6.A.1's two factors are the two kinds of claim that step can reach in this topic."),

 dict(q=_OUTCOMES + " What does the data most directly illustrate?",
   table=_OUTCOMES_TABLE,
   choices=[
     "The polling leader won every contest in which the lead exceeded the reported margin of error, and lost the one in which it did not",
     "The polling leader lost every contest in the table",
     "The polling leader won every contest in the table",
     "The reported margin of error was the same in every contest",
     "The size of the lead was unrelated to the outcome"], ans=0,
   why="Contests 1, 2 and 4 report leads of 8, 4 and 6 against margins of 3, 3 and 2, and the polling leader won all three. Contest 3 reports a lead of 2 against a margin of 3, and the polling leader lost."),

 dict(q=_OUTCOMES + " Which of EK 4.6.A.1's two factors does this table bear on most directly?",
   table=_OUTCOMES_TABLE,
   choices=[
     "The reliability and veracity of public opinion data",
     "The importance of public opinion as a source of political influence in a given case",
     "The distinction between benchmark and tracking polls",
     "The definition of neutral framing",
     "Neither factor, since the table concerns elections"], ans=0,
   why="Every column of the table concerns the polling and how it compared with what happened, which is EK 4.6.A.1's second factor. The first factor concerns how much weight opinion carries in a case, which this table does not measure."),

 dict(q=_OUTCOMES + " A student concludes from this table that polling is unreliable because a polling leader lost. What is the most important correction?",
   table=_OUTCOMES_TABLE,
   choices=[
     "The only loss occurred where the lead was smaller than the reported margin of error, which is precisely where the polling never claimed a lead",
     "The table shows the polling leader losing every contest",
     "The table does not report margins of error",
     "The table shows every lead exceeding its margin of error",
     "The table covers a single contest, so no pattern can be described"], ans=0,
   why="Contest 3's lead of 2 sits inside its reported margin of 3, so that polling did not establish a leader in the first place. Treating a result the data never claimed as a failure of the data misreads what the margin of error means."),

 dict(q=_ADOPTION + " What does the data most directly illustrate?",
   table=_ADOPTION_TABLE,
   choices=[
     "Majority support did not always produce adoption, and one proposal was adopted without majority support",
     "Every proposal with majority support was adopted",
     "No proposal was adopted",
     "Every proposal was adopted",
     "Public support was identical across the four debates"], ans=0,
   why="Debate 2 reports 68 percent support and no adoption, while Debate 3 reports 44 percent and adoption. Two proposals were adopted and two were not, and support ranges from 31 to 72 percent."),

 dict(q=_ADOPTION + " Which of EK 4.6.A.1's two factors does this table bear on most directly?",
   table=_ADOPTION_TABLE,
   choices=[
     "The importance of public opinion as a source of political influence in a given policy debate",
     "The reliability of the polling data",
     "The veracity of the polling data",
     "The margin of error attached to each figure",
     "Neither factor, since the table concerns policy rather than elections"], ans=0,
   why="The stem stipulates that the support figures came from well conducted polls, so the data question is settled and what varies is whether opinion carried the debate. EK 4.6.A.1.i is that factor, and it names policy debates alongside elections."),

 dict(q=_ADOPTION + " A student concludes from this table that the polls must have been inaccurate, since support and adoption do not line up. What is the most important correction?",
   table=_ADOPTION_TABLE,
   choices=[
     "The stem states the polls were well conducted, and EK 4.6.A.1 names the importance of public opinion in a given debate as a factor separate from the data's reliability",
     "The table shows support and adoption lining up exactly",
     "The table does not report whether proposals were adopted",
     "Every proposal in the table had majority support",
     "The table covers a single debate, so no pattern can be described"], ans=0,
   why="A mismatch between opinion and outcome is exactly what EK 4.6.A.1's first factor predicts where opinion is not decisive, so it is not evidence about the second factor at all. Assigning every mismatch to bad data is the collapse the framework's two-part structure is written against."),

 dict(q=_RESPONSE + " What does the data most directly illustrate?",
   table=_RESPONSE_TABLE,
   choices=[
     "Polls completing similar numbers of interviews can have very different response rates, because they contacted very different numbers of people",
     "The poll contacting the most people achieved the highest response rate",
     "Every poll achieved the same response rate",
     "The poll completing the most interviews contacted the fewest people",
     "Response rate and number contacted are unrelated in this table"], ans=0,
   why="Polls C and D each completed 1000 interviews, but C contacted 2500 people and D contacted 20000, giving response rates of 40 and 5 percent. The poll contacting the most people has the lowest rate, not the highest."),

 dict(q=_RESPONSE + " Which of EK 4.6.A.1's two factors does a poll's response rate bear on?",
   table=_RESPONSE_TABLE,
   choices=[
     "The reliability and veracity of public opinion data",
     "The importance of public opinion as a source of political influence",
     "The definition of a benchmark poll",
     "The distinction between elections and policy debates",
     "Neither factor, since response rates are a matter of cost"], ans=0,
   why="A response rate describes who among those contacted actually answered, which is a property of how the data were produced. EK 4.6.A.1.ii covers the reliability and veracity of the data; the first factor concerns the political setting instead."),

 dict(q=_RESPONSE + " A student ranks the four polls by the number of people contacted, treating a larger number as a sign of a better poll. What is the most important correction?",
   table=_RESPONSE_TABLE,
   choices=[
     "The poll contacting the most people, 20000, completed 1000 interviews for a response rate of 5 percent, the lowest in the table",
     "The poll contacting the most people also completed the most interviews",
     "Every poll contacted the same number of people",
     "The table does not report how many interviews were completed",
     "The table covers a single poll, so no ranking is possible"], ans=0,
   why="Contacts are attempts and interviews are data, and the two come apart sharply here: the largest contact pool yields the lowest response rate. Ranking on the count of attempts measures effort rather than anything EK 4.6.A.1.ii is about."),
]
