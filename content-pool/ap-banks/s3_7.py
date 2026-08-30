# AP STATISTICS 3.7 Carrying Out a Test for a Population Proportion
# — 25 questions
# CED: Fall 2026, Unit 3. Skill 3.E (calculate the results of the appropriate
# inference method), with 4.F and 4.G for interpreting and concluding.
#
# The test statistic is
#     z = (p-hat - p0) / sqrt(p0(1 - p0) / n)
# and the detail that separates it from the confidence interval of topic 3.3 is
# the DENOMINATOR: a test standardizes using the NULL value p0, because
# everything in a test is computed assuming H0 is true. An interval has no
# hypothesized value and must use p-hat. Using p-hat in a test statistic is the
# most common arithmetic error in this topic and it appears as a distractor.
#
# The conclusion must have three parts, and an item is devoted to each:
#   a decision (reject or fail to reject H0) tied to a comparison with alpha;
#   the evidence stated in terms of the alternative;
#   the whole thing in the context of the population and response variable.
# "Accept H0" is never correct, and neither is a conclusion that omits context.
#
# Worked scenarios, all recomputed in verify_s3_7.py:
#   92 of 200,  H0 p = 0.40, Ha p > 0.40   p-hat 0.46,  z =  1.732, p = 0.0416
#  178 of 400,  H0 p = 0.50, Ha p not =    p-hat 0.445, z = -2.200, p = 0.0278
#   63 of 300,  H0 p = 0.25, Ha p < 0.25   p-hat 0.21,  z = -1.600, p = 0.0548
#  340 of 500,  H0 p = 0.65, Ha p > 0.65   p-hat 0.68,  z =  1.406, p = 0.0798
TOPIC = ("3.7", "Carrying Out a Test for a Population Proportion", 3)

QUESTIONS = [
 dict(q="The test statistic for a one-sample z-test for a population proportion is",
   choices=[
     "the difference between p-hat and p0, divided by the standard deviation of the null distribution",
     "the difference between p-hat and p0, divided by the sample size",
     "p-hat divided by p0",
     "the difference between p-hat and p0, multiplied by n",
     "p-hat minus the margin of error"],
   ans=0,
   why="A test statistic measures how many standard deviations the observed statistic lies from the hypothesized value, in the null distribution's own units."),

 dict(q="In the denominator of the test statistic for a one-sample z-test for a proportion, the standard deviation is computed using",
   choices=[
     "the observed sample proportion p-hat",
     "the hypothesized value p0, since a test assumes the null hypothesis is true",
     "the midpoint of p-hat and p0",
     "the sample size alone",
     "the confidence level"],
   ans=1,
   why="Every quantity in a test is computed under the assumption that H0 holds, which is exactly why the interval, having no hypothesized value, must instead use p-hat."),

 dict(q="A test of H0: p = 0.40 against Ha: p > 0.40 is based on 92 successes in 200 trials. The sample proportion is",
   choices=["0.400", "0.440", "0.460", "0.540", "0.920"],
   ans=2,
   why="92 divided by 200 is 0.46."),

 dict(q="For that test of H0: p = 0.40 with n = 200, the standard deviation used in the denominator of the test statistic is closest to",
   choices=["0.0012", "0.0346", "0.0352", "0.2400", "0.4900"],
   ans=1,
   why="It is the square root of (0.40)(0.60)/200 = 0.0346, computed from p0; using p-hat = 0.46 would give the incorrect 0.0352."),

 dict(q="For that test of H0: p = 0.40 against Ha: p > 0.40 with 92 successes in 200 trials, the test statistic is closest to",
   choices=["-1.732", "0.060", "1.703", "1.732", "12.000"],
   ans=3,
   why="z = (0.46 - 0.40)/0.0346 = 1.732; the value 1.703 is what results from wrongly using p-hat in the denominator."),

 dict(q="For that test with z = 1.732 and Ha: p > 0.40, the p-value is closest to",
   choices=["0.0416", "0.0832", "0.4584", "0.9584", "1.7320"],
   ans=0,
   why="A greater-than alternative uses the right-tail area beyond 1.732, which is 0.0416; 0.0832 would be the two-sided value."),

 dict(q="For that test with a p-value of 0.0416, the decision at alpha = 0.05 is to",
   choices=[
     "reject H0, since 0.0416 is less than 0.05",
     "fail to reject H0, since 0.0416 is less than 0.05",
     "accept H0",
     "accept Ha as proved",
     "reject H0, since 0.0416 is greater than 0.05"],
   ans=0,
   why="A p-value below the significance level is the condition for rejecting the null."),

 dict(q="A test of H0: p = 0.50 against Ha: p not equal to 0.50 is based on 178 successes in 400 trials. The test statistic is closest to",
   choices=["-2.200", "-2.209", "-0.055", "2.200", "2.209"],
   ans=0,
   why="p-hat = 0.445 and the null standard deviation is sqrt(0.25/400) = 0.025, so z = (0.445 - 0.50)/0.025 = -2.200."),

 dict(q="For that two-sided test with z = -2.200, the p-value is closest to",
   choices=["0.0139", "0.0278", "0.9722", "0.9861", "2.2000"],
   ans=1,
   why="A two-sided alternative doubles the one-tail area: 2(0.0139) = 0.0278."),

 dict(q="For that two-sided test with a p-value of 0.0278, the decision at alpha = 0.05 is to",
   choices=[
     "reject the null hypothesis",
     "fail to reject the null hypothesis",
     "accept the null hypothesis as true",
     "conclude that the population proportion equals 0.445",
     "collect a larger sample before deciding"],
   ans=0,
   why="0.0278 is below 0.05, so there is convincing evidence that the proportion differs from 0.50."),

 dict(q="A test of H0: p = 0.25 against Ha: p < 0.25 is based on 63 successes in 300 trials. The test statistic is closest to",
   choices=["-1.600", "-1.643", "-0.040", "1.600", "1.643"],
   ans=0,
   why="p-hat = 0.21 and the null standard deviation is sqrt((0.25)(0.75)/300) = 0.025, so z = (0.21 - 0.25)/0.025 = -1.600."),

 dict(q="For that test with z = -1.600 and Ha: p < 0.25, the p-value is closest to",
   choices=["0.0274", "0.0548", "0.1096", "0.9452", "1.6000"],
   ans=1,
   why="A less-than alternative uses the left-tail area below -1.600, which is 0.0548."),

 dict(q="For that test with a p-value of 0.0548, the decision at alpha = 0.05 is to",
   choices=[
     "reject H0, since 0.0548 is close to 0.05",
     "fail to reject H0, since 0.0548 exceeds 0.05",
     "accept H0 as true",
     "conclude that p is less than 0.25",
     "declare the result significant"],
   ans=1,
   why="A p-value above the significance level, however narrowly, does not meet the stated standard for rejecting the null."),

 dict(q="A test of H0: p = 0.65 against Ha: p > 0.65 is based on 340 successes in 500 trials. The test statistic is closest to",
   choices=["-1.406", "0.030", "1.398", "1.406", "1.435"],
   ans=3,
   why="p-hat = 0.68 and the null standard deviation is sqrt((0.65)(0.35)/500) = 0.02133, so z = (0.68 - 0.65)/0.02133 = 1.406."),

 dict(q="For that test with z = 1.406 and Ha: p > 0.65, the p-value is closest to",
   choices=["0.0399", "0.0798", "0.1596", "0.9202", "0.9601"],
   ans=1,
   why="The right-tail area beyond 1.406 is 0.0798."),

 dict(q="For that test with a p-value of 0.0798, the decision at alpha = 0.05 is to",
   choices=[
     "reject the null hypothesis",
     "fail to reject the null hypothesis, since 0.0798 exceeds 0.05",
     "accept the null hypothesis as true",
     "conclude that the proportion exceeds 0.65",
     "reject the alternative hypothesis"],
   ans=1,
   why="The data are not surprising enough under the null to meet the 0.05 standard, so the null is not rejected."),

 dict(q="A complete conclusion to a hypothesis test must include",
   choices=[
     "the test statistic only",
     "a decision about H0, linked to a comparison of the p-value with alpha, and a statement about the alternative in the context of the population",
     "the p-value only",
     "the sample proportion and the sample size",
     "a statement that the null hypothesis is true or false"],
   ans=1,
   why="A conclusion has to say what was decided, on what evidence, and about which population and response variable."),

 dict(q="Which conclusion is stated correctly for a test that rejected H0: p = 0.40 in favour of Ha: p > 0.40 at alpha = 0.05?",
   choices=[
     "We accept that p = 0.40",
     "Since the p-value of 0.0416 is less than 0.05, we reject H0 and conclude there is convincing evidence that the proportion of all such items exceeding the standard is greater than 0.40",
     "The proportion is proved to be greater than 0.40",
     "We reject H0, so the alternative hypothesis is true",
     "The sample proportion is 0.46, so p is 0.46"],
   ans=1,
   why="It compares the p-value with alpha, states the decision, describes the evidence in terms of the alternative, and names the population in context, without claiming proof."),

 dict(q="Which conclusion is stated correctly for a test that did NOT reject H0?",
   choices=[
     "We accept H0 and conclude that p equals the null value",
     "Since the p-value exceeds alpha, we fail to reject H0; there is not convincing evidence that the proportion differs from the null value",
     "The null hypothesis is true",
     "The alternative hypothesis is false",
     "The test was inconclusive because the conditions failed"],
   ans=1,
   why="Failing to find convincing evidence against a claim leaves the claim unestablished in either direction, which is why 'accept' is never used."),

 dict(q="A student computes the test statistic using sqrt(p-hat(1 - p-hat)/n) in the denominator instead of the null value. For the test of H0: p = 0.40 with p-hat = 0.46 and n = 200, this error makes the test statistic",
   choices=[
     "much larger, changing the conclusion",
     "slightly smaller, since the denominator computed from p-hat is slightly larger",
     "negative",
     "exactly the same",
     "impossible to compute"],
   ans=1,
   why="The denominator becomes 0.0352 instead of 0.0346, so the statistic falls from 1.732 to about 1.703; the error is small here but the method is wrong regardless."),

 dict(q="Rejecting H0 at alpha = 0.05 means that",
   choices=[
     "the null hypothesis has been proved false",
     "the observed result would occur less than 5% of the time if the null hypothesis were true, which is treated as convincing evidence against it",
     "there is a 5% chance the null is true",
     "95% of the population supports the alternative",
     "the sample was biased"],
   ans=1,
   why="The decision rests on how surprising the data are under the null, and it carries a known chance of being wrong rather than any certainty."),

 dict(q="Before computing a test statistic, the conditions for the one-sample z-test must be verified because",
   choices=[
     "the p-value is computed from a normal null distribution, which is only the right distribution when the conditions hold",
     "the conditions determine the value of alpha",
     "the conditions change the hypotheses",
     "the conditions are needed to find p-hat",
     "they are not really necessary if n is large"],
   ans=0,
   why="If the sampling distribution of p-hat is not approximately normal, the area computed from the standard normal curve is not the p-value the test claims it is."),

 dict(q="Two tests of the same hypotheses use samples of 100 and 900, and both produce a sample proportion of 0.46 against H0: p = 0.40. Compared with the smaller sample's test statistic, the larger sample's is",
   choices=[
     "smaller, so the p-value is larger",
     "three times as large, so the p-value is smaller",
     "the same",
     "nine times as large",
     "negative"],
   ans=1,
   why="The same deviation of 0.06 is divided by a standard deviation that is three times smaller, since the standard deviation carries the square root of n."),

 dict(q="A test statistic of z = 0 would arise when",
   choices=[
     "the sample proportion equals the hypothesized value p0",
     "the sample proportion is 0",
     "the sample size is 0",
     "the p-value is 0",
     "the null hypothesis is false"],
   ans=0,
   why="The numerator p-hat - p0 vanishes exactly when the observed proportion matches the value the null hypothesizes, giving the least surprising possible result."),

 dict(q="Which statement about the relationship between a two-sided test at alpha = 0.05 and a 95% confidence interval for the same proportion is generally correct?",
   choices=[
     "They always give contradictory results",
     "A value rejected by the two-sided test at alpha = 0.05 will generally fall outside the 95% confidence interval",
     "The interval and the test use the same standard error, so they always agree exactly",
     "The confidence interval requires a smaller sample",
     "A test cannot be compared with an interval"],
   ans=1,
   why="The two answer the same question from opposite directions, though they do not agree exactly for proportions because the test standardizes with p0 and the interval with p-hat."),
]
