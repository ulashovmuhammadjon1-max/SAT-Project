# AP STATISTICS 1.1 Introducing Statistics: What Can We Learn from Data? — 25 questions
# CED: Fall 2026, Unit 1. Learning objectives 1.1.A (identify components within a
# statistical study) and 1.1.B (determine an investigative question).
#
# This topic is definitional: population and N, sample and n, datum and data set,
# why a study samples at all, what "in context" means, and what makes an
# investigative question a usable one. The arithmetic that does appear is sampling
# fractions and counts; every such key is recomputed in verify_s1_1.py. The purely
# conceptual items are listed in that file's CONCEPTUAL set with their reasoning.
TOPIC = ("1.1", "Introducing Statistics: What Can We Learn from Data?", 1)
QUESTIONS = [
 dict(q="A statistical study is best described as a study in which",
   choices=[
     "every item or individual in a population is measured and the results are reported exactly",
     "data are collected from a sample in order to answer an investigative question about a larger population",
     "a mathematical formula is used to prove a claim about a population without collecting any data",
     "an opinion about a population is recorded and then defended with examples",
     "two populations are compared using only information already published by other researchers"],
   ans=1,
   why="A statistical study collects data from a sample and uses it to answer an investigative question about the larger population it came from."),

 dict(q="In a statistical study, the collection of all items or individuals of interest is called the",
   choices=["sample", "datum", "population", "statistic", "parameter"],
   ans=2,
   why="The population is all of the items or individuals of interest; the sample is only the subset actually measured."),

 dict(q="The symbols N and n are used in a statistical study to represent, respectively, the",
   choices=[
     "sample size and the population size",
     "population size and the sample size",
     "number of variables and the number of observational units",
     "number of categories and the number of numerical values",
     "number of studies and the number of investigative questions"],
   ans=1,
   why="N denotes the size of the population and n denotes the size of the sample selected from it."),

 dict(q="Why are statistical studies used instead of measuring every member of the population?",
   choices=[
     "Because a sample always gives a more accurate value than a census does",
     "Because populations are required by convention to remain unmeasured",
     "Because the population is often too large, or measuring every individual is too difficult or costly",
     "Because a population parameter cannot be defined unless a sample is drawn first",
     "Because samples eliminate all sources of error from a study"],
   ans=2,
   why="Sampling is used because reaching every individual in a large population is usually impractical, not because a sample is more accurate than a census."),

 dict(q="A single piece of information collected about one item or individual is called a",
   choices=["data set", "datum", "population", "variable", "sample"],
   ans=1,
   why="A datum is one piece of information about one item or individual; a collection of data is a data set."),

 dict(q="A researcher reports that the mean commute time in her sample of 240 workers is 27.4 minutes. Reporting this result 'in context' means that she should",
   choices=[
     "report the number 27.4 by itself, since the number is the result",
     "state the result as a mean of 27.4 minutes of commuting time for the workers studied, tying the number to the real-world quantity it measures",
     "convert the result to a percentage before reporting it",
     "compare the result to a different study before reporting it",
     "round the result to the nearest whole number so it is easier to read"],
   ans=1,
   why="Reporting in context means identifying the statistical result with the real-world component it came from, including the units and the individuals measured."),

 dict(q="A student begins a study with the investigative question 'Do students at this school sleep less on school nights than on weekend nights?' After looking at the data, she notices nothing interesting about sleep but does notice a pattern in screen time, so she rewrites her question to be about screen time. This is a problem because",
   choices=[
     "an investigative question may never mention time as a variable",
     "an investigative question should have a defined purpose set before analysis and should not be changed on the basis of the results",
     "screen time is a categorical variable and cannot be studied",
     "an investigative question must always compare exactly two populations",
     "a study may only be conducted once per school year"],
   ans=1,
   why="An investigative question is supposed to be fixed before the data are analyzed; changing it to match whatever the data happened to show is what makes the finding unreliable."),

 dict(q="Which of the following is the best investigative question for a statistical study?",
   choices=[
     "Is chocolate ice cream the best flavor?",
     "What is the meaning of a healthy diet?",
     "What proportion of students at this high school eat breakfast on a typical school day?",
     "Should the school cafeteria be better?",
     "Why is nutrition important?"],
   ans=2,
   why="Only this question names a specific population and a specific measurable quantity, so the data needed to answer it can actually be collected and analyzed."),

 dict(q="A quality inspector at a factory that produced 18,500 light bulbs in one week tests 150 of those bulbs. In this study, N and n are",
   choices=[
     "N = 150 and n = 150",
     "N = 150 and n = 18,500",
     "N = 18,500 and n = 150",
     "N = 18,500 and n = 18,350",
     "N = 18,650 and n = 150"],
   ans=2,
   why="The 18,500 bulbs produced are the population and the 150 tested are the sample, so N = 18,500 and n = 150."),

 dict(q="A town has 12,400 households. A researcher collects data from 310 of them. What percent of the population was sampled?",
   choices=["0.25%", "0.40%", "2.5%", "4.0%", "25%"],
   ans=2,
   why="310 divided by 12,400 is 0.025, which is 2.5 percent."),

 dict(q="A university with 21,000 enrolled students wants a sample that is 4% of the student body. How many students should be in the sample?",
   choices=["84", "420", "525", "840", "5,250"],
   ans=3,
   why="Four percent of 21,000 is 0.04 times 21,000, which is 840."),

 dict(q="A researcher surveys 96 members of a hiking club and reports that this was 15% of the club's membership. How many members does the club have?",
   choices=["144", "480", "640", "1,440", "6,400"],
   ans=2,
   why="If 96 is 15 percent of N, then N = 96 divided by 0.15, which is 640."),

 dict(q="A biologist wants to answer the question 'What is the mean wingspan of adult monarch butterflies in a particular reserve?' She captures and measures 45 adult monarchs in that reserve. The population in this study is",
   choices=[
     "the 45 monarchs she measured",
     "all adult monarch butterflies in that reserve",
     "all butterflies of every species in that reserve",
     "the mean wingspan of the 45 monarchs",
     "the wingspan measurement itself"],
   ans=1,
   why="The population is every individual the investigative question is about, which here is all adult monarchs in that reserve, not just the 45 captured."),

 dict(q="In the same butterfly study, the 45 monarchs that were captured and measured are the",
   choices=["population", "sample", "parameter", "investigative question", "data set size N"],
   ans=1,
   why="The subset of the population that is actually measured is the sample."),

 dict(q="Which statement about a sample and the population it comes from is correct?",
   choices=[
     "A summary computed from the sample is always equal to the corresponding summary for the population",
     "A summary computed from the sample is usually not equal to the population value but can be used as a basis for inference about it",
     "A sample provides no information at all about the population",
     "A sample is useful only when it contains more than half of the population",
     "A sample and a population must always be the same size"],
   ans=1,
   why="A sample summary is generally not exactly equal to the unknown population value, but it is the basis on which inferences about that value are made."),

 dict(q="A hospital administrator asks, 'Of the patients admitted to this hospital last year, what percent stayed longer than three nights?' Records for every patient admitted last year are complete and available. In this situation,",
   choices=[
     "no statistical study is needed, because the entire population can be examined directly",
     "a statistical study is required, because percents can only be estimated",
     "a statistical study is required, because hospital data are always incomplete",
     "the question is not a valid investigative question",
     "the population cannot be identified"],
   ans=0,
   why="Sampling exists because a population is usually too large or difficult to measure completely; when the whole population is already available, it can simply be examined."),

 dict(q="A set of information collected about many items or individuals is called a",
   choices=["datum", "parameter", "data set", "population size", "statistic"],
   ans=2,
   why="One piece of information is a datum; a collection of data is a data set."),

 dict(q="Which of the following questions could NOT be answered by collecting and analyzing data?",
   choices=[
     "What is the average height of players on this basketball team?",
     "What proportion of cars passing this intersection are red?",
     "Is it morally wrong to be late to an appointment?",
     "How many hours per week do employees at this company work?",
     "What percent of packages from this warehouse arrive damaged?"],
   ans=2,
   why="A question about moral right and wrong has no measurable quantity to collect, so no data set can settle it."),

 dict(q="A polling organization wants to estimate the proportion of all registered voters in a state who support a ballot measure. It contacts 1,200 registered voters. The investigative question in this study is about",
   choices=[
     "the 1,200 voters contacted",
     "all registered voters in the state",
     "the polling organization's employees",
     "the ballot measure's author",
     "the 1,200 responses considered as a population"],
   ans=1,
   why="The investigative question concerns the larger population the sample is meant to represent, which is all registered voters in the state."),

 dict(q="A market researcher writes the investigative question 'How many customers visited the store?' but does not say which store or over what period. The main weakness of this question is that",
   choices=[
     "it uses a count rather than a percent",
     "it does not identify the population and time frame clearly enough for the necessary data to be collected",
     "it concerns customers rather than employees",
     "counts cannot be analyzed statistically",
     "it can be answered, and so is not investigative"],
   ans=1,
   why="An investigative question has to be posed precisely enough that the required data can actually be collected, and this one leaves the population and the time period undefined."),

 dict(q="A shipping company handled 7,800 packages in a month and inspected 234 of them. The sampling fraction, expressed as a percent, is closest to",
   choices=["0.30%", "1.5%", "3.0%", "23.4%", "30%"],
   ans=2,
   why="234 divided by 7,800 is 0.03, which is 3.0 percent."),

 dict(q="Two students each want to study the same population of 5,000 concert attendees. Student A samples 100 attendees; Student B samples 500. Which statement is correct?",
   choices=[
     "Both studies have the same value of N but different values of n",
     "Both studies have the same value of n but different values of N",
     "Student A has the larger population",
     "Student B has changed the population by taking a larger sample",
     "Neither study has a population, because only samples were measured"],
   ans=0,
   why="The population of 5,000 attendees is the same for both, so N is the same; only the sample sizes n differ."),

 dict(q="An investigative question, a population, a sample, and a set of collected data are all components of",
   choices=[
     "a mathematical proof",
     "a statistical study",
     "a parameter",
     "a categorical variable",
     "a relative frequency table"],
   ans=1,
   why="These are precisely the components that make up a statistical study."),

 dict(q="A researcher studying 3,000 employees reports 'the mean number of sick days was 4.2.' A colleague objects that the report is not in context. The best fix is to write",
   choices=[
     "the mean was 4.2",
     "the mean was 4.2 units",
     "the sample mean was 4.2 sick days per employee for the employees studied during the past year",
     "the mean of the data set equals 4.2 exactly",
     "4.2 is the answer to the investigative question"],
   ans=2,
   why="Putting a result in context requires naming the quantity, its units, and the individuals and time frame it describes, not just the number."),

 dict(q="A student claims, 'Because my sample mean is 62.5, the population mean must also be 62.5.' The best response is that",
   choices=[
     "the claim is correct as long as the sample was large",
     "the claim is correct only if the population is small",
     "the sample mean is a value computed from one sample and generally differs from the unknown population mean, though it can be used to make an inference about it",
     "the population mean does not exist unless every individual is measured",
     "the sample mean and population mean are different names for the same number"],
   ans=2,
   why="A statistic computed from a sample is usually not equal to the corresponding population value; it is evidence about that value, not the value itself."),
]
