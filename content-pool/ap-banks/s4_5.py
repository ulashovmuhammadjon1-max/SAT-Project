# AP STATISTICS 4.5 Carrying Out a Test for a Population Mean or Population
# Mean Difference - 25 questions
# CED: AP Statistics Course and Exam Description, Effective Fall 2026, Unit 4.
# Objectives 4.5.A (t = (xbar - mu0)/(s/sqrt(n)) with df = n - 1, and its
# p-value), 4.5.B (interpret the p-value as a probability computed ASSUMING H0
# is true), 4.5.C (compare p to alpha, then state a non-definitive conclusion in
# context that names the parameter and the population).
# Four items also cover Type I and Type II error and power as they arise from a
# test about a mean; the CED gives those their own topic in Unit 3, but a
# student meeting a decision about mu needs them here.
# Every t statistic, p-value and critical value is recomputed in verify_s4_5.py
# from scipy.stats.t with the degrees of freedom stated; none is recalled.
TOPIC = ("4.5", "Carrying Out a Test for a Population Mean or Population Mean Difference", 4)
QUESTIONS = [

 dict(q="A random sample of 36 observations has mean 51.3 and standard deviation 4.2. For the hypotheses H0: mu = 50 versus Ha: mu > 50, what is the value of the test statistic?", choices=[
   "0.310",
   "1.857",
   "2.210",
   "7.429",
   "11.143"], ans=1,
   why="The one-sample t statistic is (51.3 - 50)/(4.2/sqrt(36)) = 1.3/0.7 = 1.857; 0.310 comes from dividing by s = 4.2 instead of by the standard error."),

 dict(q="For that same test (n = 36, xbar = 51.3, s = 4.2, H0: mu = 50, Ha: mu > 50), what is the p-value?", choices=[
   "0.0180",
   "0.0359",
   "0.0717",
   "0.9641",
   "0.4830"], ans=1,
   why="With df = 35 the upper-tail area beyond t = 1.857 is 0.0359; 0.0717 doubles it, which would be right only for a two-sided alternative."),

 dict(q="A random sample of 20 observations has mean 27.4 and standard deviation 6.1. For H0: mu = 30 versus Ha: mu < 30, what is the test statistic?", choices=[
   "-1.906",
   "-0.426",
   "-2.600",
   "1.906",
   "-8.525"], ans=0,
   why="t = (27.4 - 30)/(6.1/sqrt(20)) = -2.6/1.364 = -1.906; the sign must be kept, and -2.600 is the numerator alone."),

 dict(q="For that same test (n = 20, xbar = 27.4, s = 6.1, Ha: mu < 30), what is the p-value?", choices=[
   "0.0359",
   "0.0719",
   "0.9641",
   "0.0250",
   "0.1436"], ans=0,
   why="With df = 19 the lower-tail area below t = -1.906 is 0.0359; the alternative is one-sided, so the area is not doubled."),

 dict(q="A random sample of 25 observations has mean 104.2 and standard deviation 9.5. For H0: mu = 100 versus Ha: mu is not equal to 100, what is the test statistic?", choices=[
   "0.442",
   "1.105",
   "2.211",
   "4.200",
   "11.053"], ans=2,
   why="t = (104.2 - 100)/(9.5/sqrt(25)) = 4.2/1.9 = 2.211; the alternative being two-sided changes the p-value, not the statistic."),

 dict(q="For that same two-sided test (n = 25, xbar = 104.2, s = 9.5, mu0 = 100), what is the p-value?", choices=[
   "0.0184",
   "0.0368",
   "0.0736",
   "0.9632",
   "0.0250"], ans=1,
   why="With df = 24 the one-tail area beyond t = 2.211 is 0.0184, and a two-sided alternative doubles it to 0.0368; using 0.0184 is the single most common error on a two-sided test."),

 dict(q="Ten volunteers each performed a task before and after a training session. The before-minus-after differences in completion time, in seconds, were 3, -1, 4, 2, 5, 0, 3, 6, 1, 2. For H0: mu_d = 0 versus Ha: mu_d > 0, what is the test statistic?", choices=[
   "1.151",
   "2.500",
   "3.638",
   "7.500",
   "11.503"], ans=2,
   why="The ten differences have mean 2.5 and standard deviation 2.173, so the standard error is 0.687 and t = 2.5/0.687 = 3.638 with df = 9."),

 dict(q="For that same paired test (10 differences, mean 2.5, standard deviation 2.173, Ha: mu_d > 0), what is the p-value?", choices=[
   "0.0027",
   "0.0054",
   "0.0135",
   "0.9973",
   "0.0500"], ans=0,
   why="With df = 9 the upper-tail area beyond t = 3.638 is 0.0027; 0.0054 would be the two-sided p-value."),

 dict(q="A test of H0: mu = 12 against Ha: mu > 12 gives a p-value of 0.02. Which is the correct interpretation?", choices=[
   "If the population mean really were 12, there would be a 0.02 probability of getting a sample mean at least as large as the one observed",
   "There is a 0.02 probability that the population mean is 12",
   "There is a 0.02 probability that the population mean is greater than 12",
   "There is a 0.02 probability that the conclusion drawn from this test is wrong",
   "Two percent of the observations in the sample are larger than 12"], ans=0,
   why="CED 4.5.B.1: a p-value is computed by ASSUMING the null is true and is the probability of a result at least this extreme in the direction of Ha; it is a probability about data, not about the hypothesis."),

 dict(q="A student says a p-value of 0.03 means 'the probability that the null hypothesis is true is 0.03.' What is the error?", choices=[
   "The p-value is a probability about the data computed under the assumption that H0 is true, not a probability about H0 itself",
   "The p-value should have been 0.06, since it is always doubled",
   "The p-value is the probability that the alternative hypothesis is true",
   "There is no error, provided the sample was random",
   "The p-value is the probability of a Type II error"], ans=0,
   why="H0 is either true or false; the p-value conditions on H0 being true and measures how unusual the observed data would be in that case, so it cannot be the probability of H0."),

 dict(q="A test about a population mean gives a p-value of 0.031. What decisions follow at significance levels 0.05 and 0.01?", choices=[
   "Reject H0 at 0.05; fail to reject H0 at 0.01",
   "Reject H0 at both levels",
   "Fail to reject H0 at both levels",
   "Fail to reject H0 at 0.05; reject H0 at 0.01",
   "The decision cannot be made without the test statistic"], ans=0,
   why="The formal decision compares p with alpha: 0.031 <= 0.05 gives a rejection, while 0.031 > 0.01 does not."),

 dict(q="A one-sample t-test of H0: mu = 500 against Ha: mu < 500 has p-value 0.004 at alpha = 0.05. Which conclusion is stated correctly?", choices=[
   "There is convincing evidence that the mean fill volume of all bottles from this machine is less than 500 mL",
   "There is convincing evidence that the mean fill volume of the sampled bottles is less than 500 mL",
   "The mean fill volume of all bottles from this machine is definitely less than 500 mL",
   "There is convincing evidence that the mean fill volume of all bottles from this machine equals 500 mL",
   "There is a 0.004 probability that the mean fill volume is 500 mL"], ans=0,
   why="CED 4.5.C.3: the conclusion is stated in terms of the alternative, in context, with non-definitive language, and it references the population parameter rather than the sample."),

 dict(q="A test of H0: mu = 45 against Ha: mu is not equal to 45 gives a p-value of 0.42. What is the correct conclusion?", choices=[
   "There is not convincing evidence that the population mean differs from 45",
   "There is convincing evidence that the population mean equals 45",
   "The population mean is 45",
   "There is convincing evidence that the population mean differs from 45",
   "The test is inconclusive because the p-value exceeds 0.05 but is below 0.50"], ans=0,
   why="Failing to reject H0 means the data are consistent with mu = 45, which is not the same as evidence that mu equals 45; a large p-value never establishes the null."),

 dict(q="In a test of H0: mu = 100 against Ha: mu > 100, a Type I error would occur when", choices=[
   "the test rejects H0 although the population mean really is 100",
   "the test fails to reject H0 although the population mean is greater than 100",
   "the test rejects H0 and the population mean really is greater than 100",
   "the sample mean is greater than 100 although the population mean is 100",
   "the sample is not selected at random"], ans=0,
   why="A Type I error is rejecting a true null; a sample mean above 100 when mu = 100 is ordinary sampling variability and is not itself an error."),

 dict(q="In a test of H0: mu = 100 against Ha: mu > 100, a Type II error would occur when", choices=[
   "the test fails to reject H0 although the population mean is actually greater than 100",
   "the test rejects H0 although the population mean is actually 100",
   "the test fails to reject H0 and the population mean really is 100",
   "the p-value is larger than the significance level",
   "the sample standard deviation is larger than the population standard deviation"], ans=0,
   why="A Type II error is failing to detect a real departure from the null; a large p-value alone is a decision, not an error, since it may well be the right decision."),

 dict(q="A researcher changes the significance level of a test about a population mean from 0.05 to 0.01, keeping everything else the same. What happens to the two error probabilities?", choices=[
   "The probability of a Type I error decreases and the probability of a Type II error increases",
   "Both probabilities decrease",
   "Both probabilities increase",
   "The probability of a Type I error increases and the probability of a Type II error decreases",
   "Neither probability changes, because alpha only affects the conclusion's wording"], ans=0,
   why="Alpha is the Type I error rate, so lowering it makes rejection harder; with the same data and effect size, harder rejection means more failures to detect a real difference, so beta rises and power falls."),

 dict(q="Which change would increase the power of a one-sample t-test about a population mean, holding the true value of mu fixed?", choices=[
   "Increasing the sample size",
   "Decreasing the significance level from 0.05 to 0.01",
   "Increasing the population standard deviation",
   "Changing a one-sided alternative to a two-sided one",
   "Reporting the p-value to more decimal places"], ans=0,
   why="Power rises when the test statistic becomes larger in absolute value for the same true mu, which a larger n achieves by shrinking the standard error; a smaller alpha, a larger sigma and a two-sided alternative all reduce power."),

 dict(q="A random sample of 42 observations has mean 8.6 and standard deviation 1.4. For H0: mu = 9.0 versus Ha: mu is not equal to 9.0, what are the test statistic and p-value?", choices=[
   "t = -1.852, p-value = 0.0713",
   "t = -1.852, p-value = 0.0356",
   "t = -0.286, p-value = 0.7763",
   "t = 1.852, p-value = 0.9287",
   "t = -1.960, p-value = 0.0500"], ans=0,
   why="The standard error is 1.4/sqrt(42) = 0.2160, so t = -0.4/0.2160 = -1.852 with df = 41; the two-sided p-value doubles the lower-tail area 0.0356 to 0.0713."),

 dict(q="For the test in the previous question at alpha = 0.05, what is the decision and conclusion?", choices=[
   "Fail to reject H0; there is not convincing evidence that the population mean differs from 9.0",
   "Reject H0; there is convincing evidence that the population mean differs from 9.0",
   "Reject H0; there is convincing evidence that the population mean equals 9.0",
   "Fail to reject H0; there is convincing evidence that the population mean equals 9.0",
   "No decision is possible, because the test statistic is negative"], ans=0,
   why="The p-value 0.0713 exceeds 0.05, so H0 is not rejected; and a failure to reject is never evidence in favor of the null."),

 dict(q="A random sample of 49 observations has mean 212 and standard deviation 28. For H0: mu = 200 versus Ha: mu > 200, what are the test statistic and p-value?", choices=[
   "t = 3.000, p-value = 0.0021",
   "t = 3.000, p-value = 0.0043",
   "t = 0.429, p-value = 0.3350",
   "t = 12.000, p-value = 0.0000",
   "t = 3.000, p-value = 0.9979"], ans=0,
   why="The standard error is 28/7 = 4, so t = 12/4 = 3.000 with df = 48, and the upper-tail area is 0.0021; 0.0043 would double it for a two-sided alternative."),

 dict(q="For a one-sided upper-tail t-test about a population mean at alpha = 0.05 with a random sample of 36 observations, what is the critical value of t?", choices=[
   "1.645",
   "1.690",
   "1.960",
   "2.030",
   "2.438"], ans=1,
   why="With df = 35 the 95th percentile of the t-distribution is 1.690; 1.645 is the corresponding standard normal value and would be used only if sigma were known."),

 dict(q="A random sample of 16 observations has mean 3.42 and standard deviation 0.35. For H0: mu = 3.5 versus Ha: mu < 3.5, what are the test statistic and p-value?", choices=[
   "t = -0.914, p-value = 0.1875",
   "t = -0.914, p-value = 0.3750",
   "t = -0.229, p-value = 0.4111",
   "t = -3.657, p-value = 0.0011",
   "t = -0.914, p-value = 0.8125"], ans=0,
   why="The standard error is 0.35/4 = 0.0875, so t = -0.08/0.0875 = -0.914 with df = 15, and the lower-tail area is 0.1875; the alternative is one-sided, so the area is not doubled."),

 dict(q="A study of 40,000 observations finds a sample mean of 100.05 against H0: mu = 100, with a p-value of 0.001. Which comment is most appropriate?", choices=[
   "The result is statistically significant but the estimated difference of 0.05 may be too small to matter in practice",
   "The result proves that the population mean is 100.05",
   "A p-value that small means the difference must be practically important",
   "The result is not statistically significant, because the difference is only 0.05",
   "The p-value should be recomputed, since a large sample makes the test invalid"], ans=0,
   why="A very large sample makes even a trivial departure from mu0 detectable; statistical significance answers whether a difference is real, not whether it is large enough to matter."),

 dict(q="An analyst has a non-random convenience sample of 18 measurements that are strongly skewed with an outlier, and runs a one-sample t-test anyway, obtaining p = 0.03. What is the correct assessment?", choices=[
   "The conditions were not met, so the p-value is not trustworthy and no conclusion about the population is justified",
   "The conclusion is valid, because the p-value is below 0.05",
   "The conclusion is valid, because t procedures are robust to any violation",
   "Only the randomization condition matters, so the skewness can be ignored",
   "The p-value should simply be doubled to compensate for the skewness"], ans=0,
   why="Conditions are checked before the procedure is run, not after: a non-random sample fails randomization and n = 18 with strong skew and an outlier fails the sample data condition, so the reference t-distribution does not describe this statistic."),

 dict(q="For a sample mean that falls on the side of mu0 favored by Ha, how do the one-sided and two-sided p-values compare in a one-sample t-test? Using the sample with n = 25, xbar = 104.2, s = 9.5 and mu0 = 100, the two values are", choices=[
   "the two-sided p-value is exactly twice the one-sided one: 0.0184 and 0.0368",
   "the two-sided p-value is exactly half the one-sided one: 0.0368 and 0.0184",
   "the two p-values are equal at 0.0368",
   "the two-sided p-value is 0.0184 and the one-sided is 0.0092",
   "the relationship depends on the degrees of freedom"], ans=0,
   why="The t-distribution is symmetric, so the two-sided p-value adds an equal area in the opposite tail: 2 x 0.0184 = 0.0368; the factor of 2 holds for any df when the sample mean falls on the Ha side."),
]
