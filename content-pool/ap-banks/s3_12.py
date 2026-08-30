# AP STATISTICS 3.12 Setting Up a Test for the Difference Between Two
# Population Proportions — 25 questions
# CED: Fall 2026, Unit 3. Skills 2.C (identify the method), 2.E (state the
# hypotheses) and 4.E (verify the conditions).
#
# The procedure is the TWO-SAMPLE z-TEST FOR A DIFFERENCE OF PROPORTIONS.
#
# Hypotheses. The null says the two population proportions are equal, and it may
# be written either way round -- H0: p1 = p2, or equivalently H0: p1 - p2 = 0.
# Note what is NOT hypothesized: no particular value of p1 or p2 is claimed,
# only that they match. The alternative is one-sided (p1 > p2 or p1 < p2) or
# two-sided (p1 not equal to p2), and, as always, both hypotheses are about the
# PARAMETERS and never about p-hat1 and p-hat2.
#
# THE POOLED PROPORTION. Because the null says the two proportions are equal,
# there is a single common value to estimate, and the best estimate of it uses
# every observation from both samples:
#     p-hat_c = (x1 + x2) / (n1 + n2)
# This is where the pooled proportion comes from, and it is the reason the test
# and the interval of topic 3.10 differ. It is a weighted average of the two
# sample proportions -- weighted by sample size, not a plain average of them --
# and the plain average is the classic error, appearing as a distractor whenever
# the two sample sizes differ.
#
# CONDITIONS: both samples random and independent of each other, each within the
# 10% rule, and the expected counts computed FROM THE POOLED PROPORTION at least
# 10 in all four cells -- pooled, because a test computes everything under its
# null hypothesis.
TOPIC = ("3.12", "Setting Up a Test for the Difference Between Two Population Proportions", 3)

QUESTIONS = [
 dict(q="The appropriate procedure for testing whether two population proportions differ is",
   choices=[
     "a two-sample z-test for a difference of proportions",
     "a one-sample z-test for a population proportion",
     "a two-sample z-interval for a difference of proportions",
     "a one-sample z-interval",
     "a chi-square goodness-of-fit test"],
   ans=0,
   why="Two proportions compared by a test call for the two-sample z-test; the interval estimates rather than tests."),

 dict(q="The null hypothesis for a two-sample test of proportions states that",
   choices=[
     "the two population proportions are equal",
     "the two sample proportions are equal",
     "the first population proportion is larger",
     "both proportions equal 0.5",
     "the two samples are the same size"],
   ans=0,
   why="The null is a statement of no difference between the two population parameters; it makes no claim about what their common value is."),

 dict(q="Which of the following is an acceptable way to write the null hypothesis for a two-sample test of proportions?",
   choices=[
     "H0: p1 = p2, or equivalently H0: p1 - p2 = 0",
     "H0: p-hat1 = p-hat2",
     "H0: p1 > p2",
     "H0: p1 = 0.5 and p2 = 0.5",
     "H0: n1 = n2"],
   ans=0,
   why="Either form says the same thing, and both are about the parameters rather than the statistics."),

 dict(q="A researcher believes the proportion in population 1 is greater than that in population 2. The alternative hypothesis is",
   choices=[
     "Ha: p1 > p2",
     "Ha: p1 < p2",
     "Ha: p1 = p2",
     "Ha: p-hat1 > p-hat2",
     "Ha: p1 - p2 = 0"],
   ans=0,
   why="The belief being investigated becomes the one-sided alternative, written about the parameters."),

 dict(q="A researcher wants to know only whether the two population proportions differ, without specifying a direction. The alternative hypothesis is",
   choices=[
     "Ha: p1 > p2",
     "Ha: p1 < p2",
     "Ha: p1 not equal to p2",
     "Ha: p1 = p2",
     "Ha: p1 - p2 > 0"],
   ans=2,
   why="A question with no direction is answered by a two-sided alternative."),

 dict(q="A student writes H0: p-hat1 = p-hat2 for a two-sample test. The error is that",
   choices=[
     "hypotheses must be about the population parameters, not the sample statistics, whose values are already known from the data",
     "the two sample proportions can never be equal",
     "the null must specify a numerical value",
     "the null must be one-sided",
     "there is no error"],
   ans=0,
   why="Once the samples are collected, p-hat1 and p-hat2 are known numbers; the unknowns being tested are p1 and p2."),

 dict(q="The pooled, or combined, sample proportion used in a two-sample z-test is calculated as",
   choices=[
     "the total number of successes in both samples divided by the total number of observations in both samples",
     "the average of the two sample proportions",
     "the difference between the two sample proportions",
     "the larger sample proportion",
     "the product of the two sample proportions"],
   ans=0,
   why="Under the null the two populations share one proportion, and the best estimate of it uses every observation from both samples."),

 dict(q="Why is a pooled proportion used in the two-sample z-TEST but not in the two-sample z-INTERVAL?",
   choices=[
     "Because the test's null hypothesis asserts that the two proportions are equal, so there is a single common value to estimate; an interval makes no such assumption",
     "Because pooling always reduces the standard error",
     "Because the interval uses a different critical value",
     "Because the test requires equal sample sizes",
     "It is used in both"],
   ans=0,
   why="A test computes every quantity under its null hypothesis, and here the null supplies the very assumption that makes a single combined estimate the right one."),

 dict(q="In one study, 120 of 300 in Group 1 and 90 of 300 in Group 2 were successes. The pooled proportion is",
   choices=["0.100", "0.300", "0.350", "0.400", "0.700"],
   ans=2,
   why="The pooled proportion is (120 + 90)/(300 + 300) = 210/600 = 0.35."),

 dict(q="In a second study, 95 of 250 in Group 1 and 70 of 250 in Group 2 were successes. The pooled proportion is",
   choices=["0.100", "0.280", "0.330", "0.380", "0.660"],
   ans=2,
   why="The pooled proportion is (95 + 70)/(250 + 250) = 165/500 = 0.33."),

 dict(q="In a third study, 48 of 200 in Group 1 and 36 of 150 in Group 2 were successes. The pooled proportion is",
   choices=["0.120", "0.240", "0.245", "0.250", "0.480"],
   ans=1,
   why="The pooled proportion is (48 + 36)/(200 + 150) = 84/350 = 0.24."),

 dict(q="For that third study, the two sample proportions are 0.24 and 0.24. What does this tell you about the pooled proportion?",
   choices=[
     "It must equal 0.24 as well, since the two sample proportions agree",
     "It must be larger than both",
     "It must be smaller than both",
     "It cannot be determined without the population sizes",
     "It must be 0.48"],
   ans=0,
   why="A weighted average of two equal values equals that value whatever the weights, so unequal sample sizes make no difference here."),

 dict(q="When the two sample sizes are UNEQUAL, the pooled proportion is",
   choices=[
     "the plain average of the two sample proportions",
     "a weighted average of the two sample proportions, weighted by sample size, and therefore generally different from the plain average",
     "always equal to the larger sample proportion",
     "always equal to the smaller sample proportion",
     "undefined"],
   ans=1,
   why="Every observation counts once, so the larger sample pulls the pooled value toward its own proportion; the plain average is the standard error here."),

 dict(q="A study has 60 successes in 100 observations for Group 1 and 90 successes in 300 for Group 2. The pooled proportion and the plain average of the two sample proportions are, respectively,",
   choices=[
     "0.375 and 0.450",
     "0.450 and 0.375",
     "0.375 and 0.375",
     "0.300 and 0.600",
     "0.150 and 0.450"],
   ans=0,
   why="Pooled is (60 + 90)/400 = 0.375, while the plain average of 0.60 and 0.30 is 0.45; the larger second sample pulls the pooled value down."),

 dict(q="For a two-sample z-test of proportions, the normality condition is checked using expected counts computed from",
   choices=[
     "each sample's own proportion",
     "the pooled proportion, since the test assumes the null hypothesis that the proportions are equal",
     "the observed counts",
     "the difference between the two proportions",
     "the significance level"],
   ans=1,
   why="The test proceeds under its null, so the expected counts come from the single combined estimate rather than from the two separate ones."),

 dict(q="For the study with 120 of 300 and 90 of 300 and a pooled proportion of 0.35, the four expected counts are",
   choices=[
     "105, 195, 105, and 195",
     "120, 180, 90, and 210",
     "105 and 195 only",
     "210 and 390",
     "0.35 and 0.65"],
   ans=0,
   why="Each sample's expected counts are 300(0.35) = 105 successes and 300(0.65) = 195 failures, and the pooled value is used for both samples."),

 dict(q="Comparing the expected counts for a two-sample TEST with the observed counts used for a two-sample INTERVAL on the same data,",
   choices=[
     "they are always identical",
     "they differ, because the test uses the pooled proportion and the interval uses each sample's own results",
     "the interval uses larger numbers by definition",
     "only the test's counts must exceed 10",
     "neither set needs checking"],
   ans=1,
   why="On the study above the test gives 105, 195, 105, 195 while the interval gives 120, 180, 90, 210, which is the same distinction as p0 against p-hat in the one-sample case."),

 dict(q="Which of the following is NOT a condition for a two-sample z-test for a difference of proportions?",
   choices=[
     "Both samples are randomly selected or the treatments are randomly assigned",
     "The two samples are independent of each other",
     "All four expected counts are at least 10",
     "The two sample sizes are equal",
     "Each sample is no more than 10% of its population when sampling without replacement"],
   ans=3,
   why="Nothing requires the samples to be the same size; unequal sizes are handled by the weighting inside the pooled proportion."),

 dict(q="Two samples of 200 each have a pooled proportion of 0.04. Does the normality condition hold?",
   choices=[
     "Yes, because both samples are large",
     "No, because the expected successes are 8 in each sample, which is below 10",
     "No, because the expected failures are below 10",
     "Yes, because 0.04 is a valid proportion",
     "The condition does not apply to two-sample tests"],
   ans=1,
   why="200(0.04) = 8 expected successes in each sample falls short of 10, even though the expected failures, 192 each, are ample."),

 dict(q="A study measures the same group of people before and after a campaign and compares the two proportions with a two-sample z-test. The problem is that",
   choices=[
     "the two samples are not independent, since the same individuals appear in both",
     "the sample size is too small",
     "the pooled proportion cannot be computed",
     "proportions cannot be compared over time",
     "there is no problem"],
   ans=0,
   why="Independence between the samples is an explicit condition, and repeated measurements on the same individuals violate it."),

 dict(q="A study randomly assigns 200 subjects to a treatment and 200 to a control, then compares the proportions who improve. The randomization requirement is satisfied by",
   choices=[
     "the random assignment of subjects to the two groups",
     "the equal group sizes",
     "the large sample size",
     "the fact that the proportions are close",
     "nothing; this design cannot satisfy it"],
   ans=0,
   why="For an experiment the random assignment plays the role that random selection plays for observational samples."),

 dict(q="For a two-sample test with Ha: p1 > p2, evidence in the direction of the alternative would be",
   choices=[
     "p-hat1 noticeably greater than p-hat2",
     "p-hat1 noticeably less than p-hat2",
     "the two sample proportions exactly equal",
     "a large pooled proportion",
     "unequal sample sizes"],
   ans=0,
   why="Evidence supports the alternative when the observed difference falls on the alternative's side of zero."),

 dict(q="Stated in context, the parameters for a two-sample test comparing the proportion of city residents and the proportion of rural residents who recycle are",
   choices=[
     "the two sample proportions who recycle",
     "the proportion of all city residents who recycle and the proportion of all rural residents who recycle",
     "the number of residents who recycle",
     "the pooled proportion",
     "the difference between the two sample sizes"],
   ans=1,
   why="Each parameter names a proportion, the response variable and its own population; the pooled value is a computed statistic, not a parameter."),

 dict(q="A researcher writes H0: p1 - p2 = 0.05 for a two-sample test. In AP Statistics this is",
   choices=[
     "the standard form of the null hypothesis",
     "not the standard form; the null for this procedure states no difference, that is, p1 - p2 = 0",
     "acceptable only for one-sided tests",
     "acceptable only when the samples are equal in size",
     "the correct alternative hypothesis"],
   ans=1,
   why="The two-sample z-test as taught here tests equality, and the pooled standard error is derived from exactly that assumption."),

 dict(q="If the two sample proportions are equal, the pooled proportion",
   choices=[
     "equals that common value",
     "equals zero",
     "equals one",
     "is undefined",
     "equals the average of the two sample sizes"],
   ans=0,
   why="A weighted average of identical values returns that value, so the pooled proportion coincides with both sample proportions and the observed difference is 0."),
]
