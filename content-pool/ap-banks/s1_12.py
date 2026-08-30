# AP STATISTICS 1.12 Potential Problems with Sampling — 25 questions
# CED: Fall 2026, Unit 1. Learning objective 1.12.A, essential knowledge 1.12.A.1
# through 1.12.A.6: bias as a SYSTEMATIC error, then voluntary response,
# undercoverage, nonresponse and response bias, and why nonrandom methods invite
# all of them.
#
# The distinction this topic exists to teach, and the one worth the most items:
#   BIAS is a systematic error -- the statistic comes out consistently too high
#     or consistently too low, and a larger sample does not fix it;
#   VARIABILITY is how much the statistic bounces from sample to sample -- a
#     larger sample DOES reduce it.
# Several items pair the two directly, because "increase the sample size" is the
# reflex answer students give to a bias problem and it is always wrong.
#
# The four named biases are also easy to blur, so each is tested by definition
# and again by a scenario where a neighbouring bias is the tempting distractor:
#   undercoverage -- part of the population could never have been reached;
#   nonresponse   -- they were reached and selected, but did not answer;
#   voluntary response -- nobody was selected at all, people put themselves in;
#   response bias -- they answered, but the answers lean one way.
TOPIC = ("1.12", "Potential Problems with Sampling", 1)

QUESTIONS = [
 dict(q="Bias in a sampling method is best defined as",
   choices=[
     "a systematic error in the sampling procedure that makes a statistic consistently larger or consistently smaller than the parameter",
     "the natural variation of a statistic from one sample to the next",
     "any mistake made while recording data",
     "the difference between the largest and smallest values in a sample",
     "a sample size that is too small"],
   ans=0,
   why="Bias is systematic: it pushes the estimate the same direction every time, which is what separates it from ordinary sampling variability."),

 dict(q="A researcher takes a badly biased sampling method and increases the sample size tenfold. The effect on the bias is that it",
   choices=[
     "is eliminated entirely",
     "is reduced to one tenth of its former size",
     "is unchanged, because bias comes from the procedure rather than from the number of units measured",
     "is reversed in direction",
     "becomes variability instead"],
   ans=2,
   why="A larger sample shrinks variability but leaves the systematic error exactly where it was, so a big biased sample is just a more precise wrong answer."),

 dict(q="Which of the following is reduced by increasing the sample size, while the sampling method stays the same?",
   choices=[
     "The bias of the estimate",
     "The variability of the estimate from sample to sample",
     "Both the bias and the variability",
     "Neither the bias nor the variability",
     "The size of the population"],
   ans=1,
   why="Sample size controls how much the statistic bounces around its own centre; where that centre sits is fixed by the method."),

 dict(q="The bias that may occur when a sample consists entirely of people who put themselves forward is called",
   choices=[
     "undercoverage bias",
     "nonresponse bias",
     "voluntary response bias",
     "response bias",
     "measurement precision"],
   ans=2,
   why="When individuals select themselves into the sample rather than being selected, the result is voluntary response bias."),

 dict(q="The bias that may occur when a sampling method fails to include part of the population, or makes part of it less likely to be selected, is called",
   choices=[
     "undercoverage bias",
     "nonresponse bias",
     "voluntary response bias",
     "response bias",
     "sampling variability"],
   ans=0,
   why="Undercoverage is a failure of the frame itself: some of the population could never have been chosen."),

 dict(q="The bias that may occur because some individuals who WERE chosen to be sampled do not supply a response is called",
   choices=[
     "undercoverage bias",
     "nonresponse bias",
     "voluntary response bias",
     "response bias",
     "stratification"],
   ans=1,
   why="Nonresponse bias arises when the people selected fail to answer and differ systematically from those who do."),

 dict(q="The bias that may occur when the answers people give tend to depart from the true value in one particular direction is called",
   choices=[
     "undercoverage bias",
     "nonresponse bias",
     "voluntary response bias",
     "response bias",
     "cluster bias"],
   ans=3,
   why="Response bias concerns the answers themselves leaning one way, whether because of question wording, the interviewer, or reluctance to admit something."),

 dict(q="A city polls residents about a proposed tax by calling numbers from a landline telephone directory. Households with no landline cannot be reached at all. This is an example of",
   choices=[
     "undercoverage bias",
     "nonresponse bias",
     "voluntary response bias",
     "response bias",
     "no bias, because telephone numbers were chosen at random"],
   ans=0,
   why="Part of the population had no chance of selection because it was missing from the list the sample was drawn from, which is undercoverage."),

 dict(q="A pollster mails questionnaires to 2,000 randomly selected households and receives 240 back. The 240 who replied may well differ from the 1,760 who did not. This is an example of",
   choices=[
     "undercoverage bias",
     "nonresponse bias",
     "voluntary response bias",
     "response bias",
     "sampling with replacement"],
   ans=1,
   why="Every household was properly selected and could have been reached; the problem is that most did not reply, which is nonresponse."),

 dict(q="A radio programme invites listeners to phone in and say whether they support a new stadium. Of the 1,500 who call, 82% say yes. The most serious problem with this result is",
   choices=[
     "undercoverage bias",
     "nonresponse bias",
     "voluntary response bias, because the callers chose themselves and people with strong opinions call disproportionately",
     "response bias",
     "nothing, because 1,500 is a large sample"],
   ans=2,
   why="No one was selected; the sample is made up of self-selected callers, and 1,500 of them is still 1,500 volunteers."),

 dict(q="An interviewer asks, 'Do you agree that our overworked and underpaid nurses deserve a pay rise?' The wording is likely to produce",
   choices=[
     "undercoverage bias",
     "nonresponse bias",
     "response bias, because the question is worded to push respondents toward one answer",
     "voluntary response bias",
     "no bias, because everyone is asked the same question"],
   ans=2,
   why="A leading question makes answers depart from the truth in one direction, which is response bias; asking everyone the same loaded question does not fix it."),

 dict(q="Respondents are asked by a uniformed police officer whether they have ever driven above the speed limit. Many say no when in fact they have. This is",
   choices=[
     "undercoverage bias",
     "nonresponse bias",
     "voluntary response bias",
     "response bias, because answers to a sensitive question asked by an authority figure lean systematically in one direction",
     "not bias, because some people genuinely never speed"],
   ans=3,
   why="The answers themselves are systematically untrue in one direction, which is response bias rather than a problem with who was selected."),

 dict(q="A survey of student opinion is conducted by handing forms to students leaving the library on a weekday afternoon. The most likely problem is that",
   choices=[
     "the sample is a simple random sample and so is fine",
     "students who never use the library, or who use it at other times, have little or no chance of selection, which is undercoverage",
     "the sample is too variable but unbiased",
     "the study is an experiment without a control group",
     "the response variable is categorical"],
   ans=1,
   why="The method reaches only one slice of the student body, so a whole part of the population is systematically underrepresented."),

 dict(q="Which of the following would be expected to reduce BIAS rather than variability?",
   choices=[
     "Increasing the sample size from 200 to 2,000",
     "Repeating the same survey many times and averaging the results",
     "Replacing a voluntary response survey with a simple random sample of the population",
     "Reporting the estimate to more decimal places",
     "Using a wider interval when reporting the estimate"],
   ans=2,
   why="Only changing the sampling procedure moves where the estimates centre; enlarging, repeating, or reporting more precisely all leave a systematic error untouched."),

 dict(q="Two survey designs are compared by simulation. Design A produces estimates centred on the true parameter with a wide spread. Design B produces estimates tightly clustered but centred well above the parameter. It is correct to say that",
   choices=[
     "Design A has low bias and high variability; Design B has high bias and low variability",
     "Design A has high bias and low variability; Design B has low bias and high variability",
     "both designs are unbiased",
     "both designs are biased",
     "Design B is better in every respect because its estimates are consistent"],
   ans=0,
   why="Where the estimates centre is bias and how much they spread is variability, and the two are separate properties; consistency around the wrong value is not accuracy."),

 dict(q="Nonrandom sampling methods such as convenience and voluntary response samples are problematic mainly because",
   choices=[
     "they always produce sample sizes that are too small",
     "they do not use random chance to select individuals, so there is no protection against systematic over- or under-representation",
     "they require more time to carry out",
     "they cannot be used with categorical variables",
     "they make the population smaller"],
   ans=1,
   why="Without a chance mechanism nothing prevents the selected group from differing systematically from the population, and no arithmetic afterward can repair that."),

 dict(q="A researcher notices that a survey estimate came out very close to the known population value on one occasion. This shows that the sampling method",
   choices=[
     "is definitely unbiased",
     "is definitely biased",
     "may or may not be biased, because bias is about the long-run centre of the estimates rather than any single sample",
     "has zero variability",
     "used a census"],
   ans=2,
   why="A biased method can still land near the truth once by chance; bias is a property of the procedure across all possible samples, not of one result."),

 dict(q="A polling organization wants to estimate the proportion of adults in a country who hold a particular view. Which change would most improve the trustworthiness of the estimate?",
   choices=[
     "Surveying 50,000 visitors to the organization's website instead of 1,000",
     "Drawing a random sample of 1,000 adults from a frame covering the whole adult population, and following up vigorously with those who do not initially respond",
     "Asking a more strongly worded question so that respondents give clearer answers",
     "Reporting the result to three decimal places",
     "Surveying only adults who are easy to contact, to save money"],
   ans=1,
   why="A proper frame addresses undercoverage, random selection addresses self-selection, and follow-up addresses nonresponse, whereas a huge self-selected sample multiplies the bias without touching it."),

 dict(q="A survey question asks, 'How many hours did you exercise last month?' Many respondents cannot remember accurately and tend to overstate. This is best described as",
   choices=[
     "undercoverage bias",
     "nonresponse bias",
     "voluntary response bias",
     "response bias, since the reported values depart from the true values in a consistent direction",
     "an outlier problem"],
   ans=3,
   why="The respondents were properly selected and did answer; the answers themselves are systematically too large, which is response bias."),

 dict(q="Which of these is NOT a source of bias, but rather ordinary sampling variability?",
   choices=[
     "A frame that omits part of the population",
     "A sample made up of volunteers",
     "The fact that two different random samples from the same population give slightly different estimates",
     "A leading question",
     "A low response rate whose nonrespondents differ from respondents"],
   ans=2,
   why="Two proper random samples differing a little is exactly what sampling variability is; it has no systematic direction and shrinks as n grows."),

 dict(q="A study samples households by knocking on doors between 9 a.m. and 3 p.m. on weekdays. Compared with the whole population of households, the sample will tend to over-represent households where someone is at home during the day. This is",
   choices=[
     "voluntary response bias",
     "undercoverage bias, since households with everyone at work are far less likely to be included",
     "response bias",
     "an unbiased method with high variability",
     "a stratified random sample"],
   ans=1,
   why="The method makes a large part of the population much less likely to be selected, which is undercoverage even though no one refused to answer."),

 dict(q="A magazine reports that 78% of its readers who returned a mail-in coupon favour a policy, and concludes that 78% of the country favours it. The most serious flaw is that",
   choices=[
     "78% is too large a percentage to be plausible",
     "the sample is composed of self-selected readers of one magazine, so it cannot represent the country",
     "the sample size is not reported, and no conclusion is ever possible without it",
     "percentages should be reported as proportions",
     "the magazine should have used a larger font on the coupon"],
   ans=1,
   why="Two problems compound here, undercoverage of everyone who does not read the magazine and voluntary response among those who do, and neither is fixed by any number of returned coupons."),

 dict(q="Bias and variability are best summarized by saying that",
   choices=[
     "bias is about where the estimates centre, and variability is about how spread out they are",
     "bias is about how spread out the estimates are, and variability is about where they centre",
     "bias and variability are two names for the same quantity",
     "an estimate with low variability must have low bias",
     "an estimate with low bias must have low variability"],
   ans=0,
   why="The two are independent properties: an estimate can be centred correctly but erratic, or tightly clustered around the wrong value."),

 dict(q="A researcher selects a proper simple random sample of 600 residents, but only 150 can be contacted, and those 150 are analyzed. The estimate from those 150 should be treated as",
   choices=[
     "unbiased, because the original selection was random",
     "potentially biased, because the 150 who were reached may differ systematically from the 450 who were not",
     "unbiased, because 150 is still a reasonably large sample",
     "biased only if fewer than 100 had responded",
     "a census of the 600"],
   ans=1,
   why="A random selection that ends in a low response rate is no longer protected by its randomness; the group actually analyzed is effectively self-selected by availability."),

 dict(q="Which statement about a large sample drawn by a biased method is correct?",
   choices=[
     "It is more trustworthy than a small sample drawn by a random method, because size matters most",
     "It gives a precise estimate of the wrong quantity, so its precision is misleading rather than reassuring",
     "It has both low bias and low variability",
     "Its bias decreases in proportion to the square root of the sample size",
     "It becomes a census once the sample is large enough"],
   ans=1,
   why="Enlarging a biased sample narrows the spread of the estimates around a centre that is still in the wrong place, which makes the wrong answer look more authoritative."),
]
