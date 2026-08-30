# AP STATISTICS 4.10 Carrying Out a Test for the Difference Between Two
# Population Means - 25 questions
# CED: AP Statistics Course and Exam Description, Effective Fall 2026, Unit 4.
# Objective 4.10.A: the two-sample test statistic is
#   t = ((xbar1 - xbar2) - 0) / sqrt(s1^2/n1 + s2^2/n2),
# with degrees of freedom from technology, lying between the smaller of
# n1 - 1 and n2 - 1 and n1 + n2 - 2. Every stem that asks for a p-value names
# WHICH df to use, because the conservative and the technology values give
# different answers; verify_s4_10.py computes both.
# The interpretation objectives are the same two that carry the most student
# error anywhere in inference, and both are tested directly: a p-value is
# P(a statistic at least this extreme GIVEN H0), never P(H0 true); and failing
# to reject H0 is not evidence FOR H0.
TOPIC = ("4.10", "Carrying Out a Test for the Difference Between Two Population Means", 4)
QUESTIONS = [

 dict(q="Independent random samples give n1 = 32 with xbar1 = 76.4 and s1 = 9.1, and n2 = 35 with xbar2 = 71.8 and s2 = 8.3. What is the two-sample t statistic for H0: mu1 = mu2?", choices=[
   "0.529",
   "1.010",
   "2.155",
   "4.600",
   "9.720"], ans=2,
   why="The standard error is sqrt(9.1^2/32 + 8.3^2/35) = sqrt(2.5878 + 1.9683) = 2.135, so t = 4.6/2.135 = 2.155; 4.600 is the numerator alone."),

 dict(q="For that same comparison (t = 2.155) against Ha: mu1 > mu2, what is the p-value using the conservative degrees of freedom?", choices=[
   "0.0175",
   "0.0195",
   "0.0390",
   "0.0500",
   "0.9805"], ans=1,
   why="The conservative df is the smaller of 31 and 34, namely 31, and the upper-tail area beyond 2.155 is 0.0195; technology's df of 62.91 would give the slightly smaller 0.0175, and 0.0390 is the two-sided value."),

 dict(q="Independent random samples give n1 = 15 with s1 = 4.2 and n2 = 18 with s2 = 5.6, and the difference in sample means is -2.8. What is the two-sample t statistic?", choices=[
   "-2.800",
   "-1.639",
   "-0.573",
   "1.639",
   "-4.788"], ans=1,
   why="The standard error is sqrt(4.2^2/15 + 5.6^2/18) = sqrt(1.176 + 1.742) = 1.708, so t = -2.8/1.708 = -1.639; the sign must be kept, because it carries the direction of the difference."),

 dict(q="For that same comparison (t = -1.639, n1 = 15, n2 = 18) against a two-sided alternative, what is the p-value using the conservative degrees of freedom?", choices=[
   "0.0617",
   "0.1235",
   "0.2470",
   "0.8765",
   "0.0500"], ans=1,
   why="The conservative df is 14, the lower-tail area below -1.639 is 0.0617, and doubling it for the two-sided alternative gives 0.1235."),

 dict(q="Independent random samples of 40 each give s1 = 6 and s2 = 7, with a difference in sample means of 3.2. What are the two-sample t statistic and the one-sided p-value using the conservative degrees of freedom?", choices=[
   "t = 2.195, p-value = 0.0171",
   "t = 2.195, p-value = 0.0342",
   "t = 2.195, p-value = 0.9829",
   "t = 0.492, p-value = 0.3128",
   "t = 3.200, p-value = 0.0014"], ans=0,
   why="The standard error is sqrt(36/40 + 49/40) = 1.458, so t = 3.2/1.458 = 2.195; with the conservative df = 39 the upper-tail area is 0.0171, and 0.0342 would be the two-sided value."),

 dict(q="A two-sample t-test comparing two population means gives a p-value of 0.03. Which interpretation is correct?", choices=[
   "If the two population means were equal, there would be a 0.03 probability of observing a difference in sample means at least as extreme as the one obtained",
   "There is a 0.03 probability that the two population means are equal",
   "There is a 0.03 probability that the two population means differ",
   "Three percent of the observations in the two samples overlap",
   "There is a 0.03 probability that the conclusion is wrong"], ans=0,
   why="CED 4.10: the p-value is computed by ASSUMING the null is true, so it is a probability about the data under H0 and never a probability about the hypotheses."),

 dict(q="A two-sample t-test gives p = 0.28 at alpha = 0.05. What conclusion is justified?", choices=[
   "There is not convincing evidence that the two population means differ",
   "There is convincing evidence that the two population means are equal",
   "The two population means are equal",
   "There is convincing evidence that the two population means differ",
   "The test must be repeated with a larger significance level"], ans=0,
   why="A large p-value means the observed difference is unsurprising when the means are equal; that fails to establish a difference and equally fails to establish equality."),

 dict(q="Independent random samples give n1 = 25 with xbar1 = 58.2 and s1 = 12.5, and n2 = 28 with xbar2 = 63.7 and s2 = 10.4. Using the conservative degrees of freedom and a two-sided alternative, what is the p-value?", choices=[
   "0.0483",
   "0.0966",
   "0.1932",
   "0.9034",
   "0.0250"], ans=1,
   why="The standard error is sqrt(156.25/25 + 108.16/28) = 3.180, so t = -5.5/3.180 = -1.730; with the conservative df = 24 the lower tail is 0.0483 and the two-sided p-value is 0.0966."),

 dict(q="For a one-sided upper-tail two-sample t-test at alpha = 0.05 with independent samples of sizes 32 and 35, what is the critical value using the conservative degrees of freedom?", choices=[
   "1.645",
   "1.696",
   "1.960",
   "2.040",
   "2.453"], ans=1,
   why="The conservative df is 31, and the 95th percentile of that t-distribution is 1.696; 1.645 is the standard normal value, appropriate only if both population standard deviations were known."),

 dict(q="A two-sample t-test yields t = 2.42 with a p-value of 0.011 for Ha: mu1 > mu2, at alpha = 0.01. What is the decision and conclusion?", choices=[
   "Fail to reject H0; there is not convincing evidence that mu1 exceeds mu2",
   "Reject H0; there is convincing evidence that mu1 exceeds mu2",
   "Reject H0; there is convincing evidence that mu1 equals mu2",
   "Fail to reject H0; there is convincing evidence that mu1 equals mu2",
   "The decision cannot be made without the degrees of freedom"], ans=0,
   why="The formal decision compares p with alpha: 0.011 > 0.01, so H0 is not rejected, and a failure to reject is not evidence for the null."),

 dict(q="A two-sample t-test on data from a randomized experiment rejects H0 at alpha = 0.05. Which conclusion is best?", choices=[
   "There is convincing evidence that the treatment causes a difference in mean response between the two groups",
   "There is convincing evidence of an association, but causation cannot be claimed from any study",
   "The treatment definitely causes a difference in mean response",
   "There is convincing evidence that the two population means are equal",
   "The result applies only to the subjects in this experiment"], ans=0,
   why="Random assignment supports a causal conclusion, which must still be stated in non-definitive language; 'definitely' overstates what a test can show."),

 dict(q="A student computes a two-sample t statistic as (xbar1 - xbar2)/(s1/sqrt(n1) + s2/sqrt(n2)) with xbar1 - xbar2 = 4.6, s1 = 9.1, n1 = 32, s2 = 8.3 and n2 = 35. What is the effect on the test statistic?", choices=[
   "The statistic is understated, 1.527 instead of the correct 2.155, because the denominator is too large",
   "The statistic is overstated, 2.155 instead of the correct 1.527",
   "There is no effect, because the two denominators are equal",
   "The statistic changes sign",
   "Only the degrees of freedom are affected"], ans=0,
   why="Adding standard errors gives 1.609 + 1.403 = 3.012 against the correct 2.135, and a larger denominator shrinks the statistic from 2.155 to 1.527, making a real difference harder to detect."),

 dict(q="Two researchers analyze the same two-sample data. One uses the conservative degrees of freedom and the other uses technology's larger value. How do their p-values compare for the same test statistic?", choices=[
   "The conservative df gives the larger p-value",
   "The conservative df gives the smaller p-value",
   "The two p-values are identical",
   "The conservative df gives a p-value more than twice as large",
   "The comparison depends on the sign of the test statistic"], ans=0,
   why="Fewer degrees of freedom mean heavier tails, so the same t value cuts off more area; the conservative approach makes rejection harder, which is why it is called conservative."),

 dict(q="A two-sample t-test of H0: mu1 = mu2 against Ha: mu1 is not equal to mu2 gives t = 1.85 with df = 40. What is the p-value?", choices=[
   "0.0250",
   "0.0359",
   "0.0717",
   "0.1436",
   "0.9641"], ans=2,
   why="The upper-tail area beyond 1.85 with df = 40 is 0.0359, and the two-sided alternative doubles it to 0.0717; failing to double is the most common error on a two-sided test."),

 dict(q="A two-sample t-test rejects H0 at alpha = 0.05, but the two samples were convenience samples of volunteers. What is the correct assessment?", choices=[
   "The randomization condition fails, so the p-value does not have its stated meaning and the rejection is not trustworthy",
   "The rejection stands, because the p-value was below 0.05",
   "The rejection stands, because t procedures are robust to non-random sampling",
   "Only the degrees of freedom need adjusting",
   "The p-value should be doubled to compensate for the volunteers"], ans=0,
   why="Conditions are checked before the procedure is run; without randomization there is no sampling distribution for the statistic, so the computed p-value does not measure what it claims to."),

 dict(q="In a two-sample t-test comparing two teaching methods, a Type I error would mean", choices=[
   "concluding the two methods have different mean effects when in fact they have the same mean effect",
   "concluding the two methods have the same mean effect when in fact they differ",
   "obtaining a difference in sample means when the population means are equal",
   "using the conservative degrees of freedom instead of technology's",
   "selecting a sample that is not representative"], ans=0,
   why="A Type I error is rejecting a true null; a nonzero difference in sample means when the population means are equal is ordinary sampling variability, not an error."),

 dict(q="Which change would increase the power of a two-sample t-test to detect a real difference in means?", choices=[
   "Increasing both sample sizes",
   "Lowering the significance level from 0.05 to 0.01",
   "Switching from a one-sided to a two-sided alternative",
   "Using the conservative degrees of freedom instead of technology's",
   "Increasing the variability within each group"], ans=0,
   why="Larger samples shrink the standard error and so enlarge |t| for the same real difference; a smaller alpha, a two-sided alternative, the conservative df and greater within-group variability all reduce power."),

 dict(q="A two-sample t-test comparing 5,000 observations in each group finds a difference in sample means of 0.03 with p = 0.002. What is the most appropriate comment?", choices=[
   "The difference is statistically significant but may be far too small to matter in practice",
   "The difference is both statistically significant and practically important, because p is small",
   "The p-value is unreliable because the samples are so large",
   "The result shows the two population means are equal",
   "The test should be repeated with smaller samples to confirm"], ans=0,
   why="Very large samples make the standard error tiny, so even a trivial difference produces a small p-value; significance and practical importance are separate questions."),

 dict(q="A researcher applies a two-sample t-test to before-and-after measurements on the same 30 subjects. What is the consequence for the p-value?", choices=[
   "The standard error is computed as if the measurements were independent, so the p-value does not correctly describe this design",
   "The p-value is exactly correct, because 30 is at least 30",
   "The p-value is exactly half what it should be",
   "The degrees of freedom double, but the p-value is unaffected",
   "The test statistic changes sign"], ans=0,
   why="Adding s1^2/n1 and s2^2/n2 assumes independence; with paired measurements the correct analysis reduces each subject to one difference and runs a one-sample t-test on the 30 differences."),

 dict(q="Which statement about the numerator of the two-sample t statistic is correct?", choices=[
   "It is the difference in sample means minus the null difference of 0, so it is simply xbar1 - xbar2",
   "It is the difference in the two population means",
   "It is the difference in the two sample standard deviations",
   "It is the difference in sample means minus the observed standard error",
   "It is always positive, since it measures a distance"], ans=0,
   why="CED 4.10.A.1 writes the numerator as (xbar1 - xbar2) - 0; the population means are unknown and the numerator keeps its sign."),

 dict(q="Two independent random samples give t = -2.41 for a two-sample test with Ha: mu1 < mu2 and conservative df = 20. Is the result significant at alpha = 0.05, and what is the approximate p-value?", choices=[
   "Yes; the p-value is about 0.0129",
   "No; the p-value is about 0.0257",
   "Yes; the p-value is about 0.0257",
   "No; the p-value is about 0.9871",
   "Yes; the p-value is about 0.0065"], ans=0,
   why="For the lower-tail alternative the p-value is the area below -2.41 with df = 20, which is 0.0129; that is below 0.05, so the result is significant, and 0.0257 would be the two-sided value."),

 dict(q="A two-sample t-test is reported with a p-value of 0.04. A reader concludes there is a 4 percent chance the null hypothesis is true. What is the flaw?", choices=[
   "The p-value is computed assuming H0 is true, so it cannot also be the probability that H0 is true",
   "The p-value should have been doubled first",
   "The reader should have said 96 percent instead",
   "There is no flaw if the samples were random",
   "The p-value is the probability of a Type II error, not a Type I error"], ans=0,
   why="Conditioning on H0 is built into the calculation; a probability computed under an assumption cannot be a probability about that assumption."),

 dict(q="A two-sample t-test is run twice on the same data, once with Ha: mu1 > mu2 and once with Ha: mu1 is not equal to mu2, and xbar1 exceeds xbar2. How do the two p-values compare?", choices=[
   "The two-sided p-value is exactly twice the one-sided one",
   "The two-sided p-value is exactly half the one-sided one",
   "They are equal",
   "The two-sided p-value is larger, but not by a fixed factor",
   "The comparison depends on the degrees of freedom"], ans=0,
   why="A t-distribution is symmetric, so the opposite tail beyond the same distance contributes an equal area; the factor of 2 holds at any degrees of freedom when the sample difference falls on the side favored by Ha."),

 dict(q="A two-sample t-test on independent random samples of sizes 9 and 11 is run, and both sample distributions are strongly skewed. The output shows p = 0.02. What should be concluded?", choices=[
   "No conclusion about the populations is justified, because the sample data condition fails for samples this small and this skewed",
   "There is convincing evidence of a difference, because p is below 0.05",
   "There is convincing evidence that the means are equal",
   "The p-value should be doubled and then compared with 0.05",
   "The samples should be pooled into one sample of 20"], ans=0,
   why="With both sample sizes below 30 and no claim of normal populations, the sample distributions must be free from strong skewness; when they are not, the reference t-distribution is wrong and the 0.02 does not mean what it appears to."),

 dict(q="For a two-sample t-test with independent samples of sizes 22 and 26, what is the conservative degrees of freedom, and what would the pooled upper bound be?", choices=[
   "21 conservative, 46 pooled",
   "22 conservative, 48 pooled",
   "25 conservative, 46 pooled",
   "21 conservative, 48 pooled",
   "47 conservative, 48 pooled"], ans=0,
   why="The conservative value is the smaller of n1 - 1 = 21 and n2 - 1 = 25, and the upper end of the CED's bracket is n1 + n2 - 2 = 46."),
]
