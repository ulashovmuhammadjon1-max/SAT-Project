# AP STATISTICS 4.7 Constructing a Confidence Interval for the Difference
# Between Two Population Means - 25 questions
# CED: AP Statistics Course and Exam Description, Effective Fall 2026, Unit 4.
# Objectives 4.7.A (identify the two-sample t-interval and its parameter),
# 4.7.B (conditions: two independent random samples or a randomized experiment;
# the 10 percent condition per population, unnecessary for an experiment; both
# n >= 30 or both populations approximately normal, and if either n < 30 both
# sample distributions free from strong skewness and outliers),
# 4.7.C (the interval (x1bar - x2bar) +/- t* sqrt(s1^2/n1 + s2^2/n2)),
# 4.7.D (standard error and margin of error).
# Degrees of freedom: CED 4.7.C.2 says technology supplies them and that they
# fall between the smaller of n1 - 1 and n2 - 1 and n1 + n2 - 2. Every stem
# below states WHICH df to use, because the two choices give different answers;
# verify_s4_7.py computes both, including the Welch-Satterthwaite value.
TOPIC = ("4.7", "Constructing a Confidence Interval for the Difference Between Two Population Means", 4)
QUESTIONS = [

 dict(q="Independent random samples give n1 = 25 with s1 = 6.2 and n2 = 30 with s2 = 5.4. What is the standard error of the difference in sample means?", choices=[
   "0.402",
   "1.584",
   "2.084",
   "2.510",
   "11.600"], ans=1,
   why="The standard error is sqrt(6.2^2/25 + 5.4^2/30) = sqrt(1.5376 + 0.9720) = sqrt(2.5096) = 1.584; 2.510 is the variance and 2.084 adds the two standard errors instead of their squares."),

 dict(q="Independent random samples give xbar1 = 48.3 with s1 = 6.2 and n1 = 25, and xbar2 = 44.1 with s2 = 5.4 and n2 = 30. Using the conservative degrees of freedom, the smaller of n1 - 1 and n2 - 1, what is the 95 percent confidence interval for mu1 - mu2?", choices=[
   "(-3.270, 3.270)",
   "(0.930, 7.470)",
   "(1.015, 7.385)",
   "(2.616, 5.784)",
   "(4.200, 7.470)"], ans=1,
   why="The point estimate is 4.2 and the standard error is 1.584; with the conservative df = 24 the critical value is 2.064, so the margin of error is 3.270 and the interval is 4.2 +/- 3.270. The interval (1.015, 7.385) is what technology's df = 48.04 gives, which is narrower."),

 dict(q="For those same two samples (n1 = 25, s1 = 6.2, n2 = 30, s2 = 5.4), what degrees of freedom does technology report, and between what two values must any acceptable df lie?", choices=[
   "df = 48.04, between 24 and 53",
   "df = 48.04, between 25 and 55",
   "df = 53, between 24 and 53",
   "df = 24, between 24 and 55",
   "df = 55, between 25 and 53"], ans=0,
   why="The Welch-Satterthwaite value is 48.04, and CED 4.7.C.2 places any acceptable df between the smaller of n1 - 1 and n2 - 1, which is 24, and n1 + n2 - 2 = 53."),

 dict(q="Which confidence interval procedure is appropriate for estimating the difference in mean commuting time between the residents of two different cities, based on an independent random sample from each?", choices=[
   "A two-sample t-interval for a difference between two population means",
   "A one-sample t-interval for a population mean difference",
   "A one-sample z-interval for a population mean",
   "A two-sample z-interval, since the samples are independent",
   "A one-sample t-interval for each city, reported separately"], ans=0,
   why="Two independent samples and two unknown population standard deviations call for the two-sample t-interval; the one-sample mean-difference procedure belongs to matched pairs, which this is not."),

 dict(q="Independent random samples give n1 = 40 with s1 = 8.1 and n2 = 36 with s2 = 7.4. What is the standard error of the difference in sample means?", choices=[
   "0.626",
   "1.778",
   "2.514",
   "3.161",
   "15.500"], ans=1,
   why="sqrt(8.1^2/40 + 7.4^2/36) = sqrt(1.6403 + 1.5211) = sqrt(3.1614) = 1.778; 3.161 is the variance."),

 dict(q="For those two samples (n1 = 40, xbar1 = 32.5, s1 = 8.1; n2 = 36, xbar2 = 29.0, s2 = 7.4), what is the 90 percent confidence interval for mu1 - mu2 using the conservative degrees of freedom?", choices=[
   "(0.496, 6.504)",
   "(1.722, 5.278)",
   "(-0.428, 7.428)",
   "(3.004, 3.996)",
   "(2.575, 4.425)"], ans=0,
   why="The point estimate is 3.5 and the standard error is 1.778; the conservative df is 35, giving t* = 1.690 and a margin of error of 3.004."),

 dict(q="What is the parameter estimated by a two-sample t-interval comparing two teaching methods?", choices=[
   "The difference in the mean test scores of the two populations of students taught by the two methods",
   "The difference in the mean test scores of the two samples of students",
   "The mean test score of all students in both populations combined",
   "The proportion of students who scored higher under the first method",
   "The difference between each student's score and the overall mean"], ans=0,
   why="CED 4.7.A.2: the parameter names the difference in the population means, the response variable and the two populations; the difference in sample means is the point estimate, not the parameter."),

 dict(q="A researcher takes independent random samples of sizes 12 and 14. One of the two sample distributions is strongly skewed with an outlier. Are the conditions for a two-sample t-interval met?", choices=[
   "No, because with a sample size below 30 both sample distributions must be free from strong skewness and outliers",
   "No, because the two sample sizes are unequal",
   "Yes, because the total 26 is close to 30",
   "Yes, because only one of the two samples is skewed",
   "Yes, because the samples were selected at random"], ans=0,
   why="CED 4.7.B.1.iii: when either sample size is below 30, BOTH sample data distributions must be free from strong skewness and outliers; one badly behaved sample is enough to fail the condition."),

 dict(q="A randomized experiment assigns 18 plants to each of two fertilizers, and a two-sample t-interval is constructed for the difference in mean growth. Which condition does NOT need to be checked?", choices=[
   "The 10 percent condition",
   "The randomization condition",
   "The sample data condition for the first group",
   "The sample data condition for the second group",
   "That the two groups are independent of each other"], ans=0,
   why="CED 4.7.B.1.ii notes explicitly that the 10 percent condition is unnecessary for data from a randomized experiment, because nothing was sampled without replacement from a population."),

 dict(q="Independent random samples give n1 = 20 with s1 = 12 and n2 = 18 with s2 = 15. What is the standard error of the difference in sample means?", choices=[
   "1.421",
   "4.439",
   "6.219",
   "19.700",
   "27.000"], ans=1,
   why="sqrt(144/20 + 225/18) = sqrt(7.2 + 12.5) = sqrt(19.7) = 4.439; 19.700 is the variance and 6.219 adds the two standard errors."),

 dict(q="For those two samples (n1 = 20, s1 = 12; n2 = 18, s2 = 15) the difference in sample means is 6.0. What is the 95 percent confidence interval for mu1 - mu2 using the conservative degrees of freedom?", choices=[
   "(-3.364, 15.364)",
   "(-2.700, 14.700)",
   "(1.561, 10.439)",
   "(-3.000, 15.000)",
   "(2.700, 9.300)"], ans=0,
   why="The conservative df is 17, so t* = 2.110 and the margin of error is 2.110 x 4.439 = 9.364, giving 6.0 +/- 9.364; the interval contains 0, so it gives no convincing evidence of a difference."),

 dict(q="Independent random samples give a difference in sample means of -2.3, a standard error of 1.003, and a conservative df of 44. What is the 99 percent confidence interval for mu1 - mu2?", choices=[
   "(-5.000, 0.400)",
   "(-4.283, -0.317)",
   "(-3.303, -1.297)",
   "(-2.700, 2.700)",
   "(-2.300, 2.700)"], ans=0,
   why="With df = 44 the 99 percent critical value is 2.692, so the margin of error is 2.700 and the interval is -2.3 +/- 2.700."),

 dict(q="A two-sample t-interval for mu1 - mu2 is reported as (-1.4, 5.8). What can be concluded about the two population means?", choices=[
   "There is no convincing evidence of a difference, because 0 is a plausible value of mu1 - mu2",
   "There is convincing evidence that mu1 is larger, because most of the interval is positive",
   "There is convincing evidence that the two population means are equal",
   "There is convincing evidence that mu1 is smaller, because the lower endpoint is negative",
   "Nothing can be concluded without the two sample sizes"], ans=0,
   why="An interval containing 0 leaves equality among the plausible values; that is a failure to find a difference, not evidence that the means are equal."),

 dict(q="Why does the two-sample t-interval add the two squared standard errors rather than subtracting them, even though the parameter is a difference?", choices=[
   "The two sample means each vary from sample to sample, and independent variabilities combine by adding variances",
   "Because the difference in sample means might be negative",
   "Because the two sample sizes are usually different",
   "Because subtraction would make the interval too wide",
   "Because the two population standard deviations are assumed equal"], ans=0,
   why="Var(X - Y) = Var(X) + Var(Y) for independent X and Y, so estimating a difference is less precise than estimating either mean alone."),

 dict(q="Holding the data fixed, a two-sample t-interval computed with the conservative degrees of freedom compared with one computed using technology's degrees of freedom is", choices=[
   "wider, because fewer degrees of freedom give a larger critical value",
   "narrower, because fewer degrees of freedom give a smaller critical value",
   "the same width, because the standard error is unchanged",
   "wider, because the standard error is recomputed with fewer degrees of freedom",
   "not comparable, because the two use different point estimates"], ans=0,
   why="The point estimate and standard error do not depend on the df; the conservative df is the smaller number, its t* is larger, and the resulting interval is wider, which is why the approach is called conservative."),

 dict(q="Independent random samples of sizes 55 and 30 are drawn without replacement from populations of 500 and 400 respectively. Which condition fails?", choices=[
   "The 10 percent condition, because 55 is more than 10 percent of 500",
   "The 10 percent condition, because 30 is more than 10 percent of 400",
   "The randomization condition, because two different populations were sampled",
   "The sample data condition, because neither sample exceeds 60",
   "No condition fails"], ans=0,
   why="The condition n <= 0.10N is applied to each population separately: 0.10 x 500 = 50 and the first sample of 55 exceeds it, while the second sample of 30 sits within 0.10 x 400 = 40."),

 dict(q="What is the point estimate used at the center of a two-sample t-interval for mu1 - mu2?", choices=[
   "The difference in the two sample means, xbar1 - xbar2",
   "The difference in the two population means",
   "The mean of the two sample means",
   "The difference in the two sample standard deviations",
   "Zero, since the null hypothesis assumes no difference"], ans=0,
   why="CED 4.7.C.1: the point estimate for mu1 - mu2 is xbar1 - xbar2; a confidence interval makes no use of a null hypothesis."),

 dict(q="Two independent random samples both have size 25. Their sample standard deviations are 4 and 9. Which sample contributes more to the standard error of the difference?", choices=[
   "The sample with s = 9, contributing 3.24 of the total 3.88",
   "The sample with s = 4, because a smaller value is more precise",
   "They contribute equally, because the sample sizes are equal",
   "Neither, because the standard errors subtract",
   "It cannot be determined without the sample means"], ans=0,
   why="The squared terms are 16/25 = 0.64 and 81/25 = 3.24, summing to 3.88, so the more variable sample supplies about 84 percent of the squared standard error even at equal sample sizes."),

 dict(q="A 95 percent two-sample t-interval for the difference in mean weekly earnings between two job categories, category A minus category B, is (42, 118) dollars. Which interpretation is correct?", choices=[
   "We are 95 percent confident that the interval from 42 to 118 dollars contains the true difference in mean weekly earnings between all workers in category A and all workers in category B",
   "We are 95 percent confident that the interval contains the difference in the mean earnings of the two samples",
   "Ninety-five percent of category A workers earn between 42 and 118 dollars more than category B workers",
   "There is a 0.95 probability that the true difference lies between 42 and 118 dollars",
   "Ninety-five percent of the differences between individual workers fall between 42 and 118 dollars"], ans=0,
   why="The interval estimates a difference in POPULATION means; the sample difference is known exactly, the interval says nothing about individual workers, and the confidence level describes the method's long-run capture rate rather than a probability for this interval."),

 dict(q="A researcher doubles both sample sizes while the two sample standard deviations stay the same. Approximately what happens to the margin of error of the two-sample t-interval?", choices=[
   "It is multiplied by about 1/sqrt(2), roughly 0.707",
   "It is halved",
   "It is quartered",
   "It is unchanged",
   "It is multiplied by sqrt(2)"], ans=0,
   why="Both squared terms halve, so the standard error is multiplied by 1/sqrt(2); the critical value also shrinks slightly as the degrees of freedom grow, which makes the reduction a little larger than 0.707."),

 dict(q="Which pair of samples would allow a two-sample t-interval rather than a one-sample t-interval for a mean difference?", choices=[
   "Reaction times of 30 randomly chosen adults and 30 randomly chosen teenagers",
   "Reaction times of 30 adults measured before and after coffee",
   "Blood pressure of 25 patients on two different days",
   "Scores of 40 students on a pretest and the same 40 students on a posttest",
   "Weights of 20 packages measured on two different scales"], ans=0,
   why="Only the first pair involves two different sets of people, making the samples independent; the other four measure the same units twice and are matched-pairs designs."),

 dict(q="Two independent random samples of sizes 45 and 50 are drawn from populations that are both strongly right-skewed. Are the conditions for a two-sample t-interval met?", choices=[
   "Yes, because both sample sizes are at least 30",
   "No, because both populations are skewed",
   "No, because the sample sizes are unequal",
   "Yes, but only if the two skews are in the same direction",
   "It cannot be determined without the sample standard deviations"], ans=0,
   why="CED 4.7.B.1.iii is satisfied when both sample sizes reach 30; the freedom-from-skewness requirement applies only when at least one sample is below 30."),

 dict(q="Given a difference in sample means of 3.5 and a 95 percent margin of error of 4.1, what is the confidence interval, and does it support a claim that the two population means differ?", choices=[
   "(-0.6, 7.6); it does not support the claim, since 0 is inside",
   "(-0.6, 7.6); it supports the claim, since the estimate is positive",
   "(3.5, 7.6); it supports the claim",
   "(-4.1, 4.1); it does not support the claim",
   "(0.6, 7.6); it supports the claim"], ans=0,
   why="The interval is 3.5 +/- 4.1 = (-0.6, 7.6), and because 0 lies inside it, no difference remains a plausible value."),

 dict(q="A student builds a two-sample t-interval using the standard error s1/sqrt(n1) + s2/sqrt(n2) instead of sqrt(s1^2/n1 + s2^2/n2), with s1 = 6.2, n1 = 25, s2 = 5.4 and n2 = 30. What is the effect?", choices=[
   "The standard error is inflated from 1.584 to 2.226, so the interval is too wide",
   "The standard error is reduced from 2.226 to 1.584, so the interval is too narrow",
   "There is no effect, because the two formulas are equivalent",
   "The interval is shifted upward but keeps its width",
   "The degrees of freedom change, but the width does not"], ans=0,
   why="Adding standard errors gives 1.240 + 0.986 = 2.226 against the correct 1.584, because a sum of positive numbers always exceeds the square root of the sum of their squares; the interval comes out too wide."),

 dict(q="Two independent random samples give a 95 percent interval for mu1 - mu2 of (2.1, 9.7). What is the point estimate and the margin of error?", choices=[
   "point estimate 5.9, margin of error 3.8",
   "point estimate 5.9, margin of error 7.6",
   "point estimate 3.8, margin of error 5.9",
   "point estimate 2.1, margin of error 7.6",
   "point estimate 9.7, margin of error 3.8"], ans=0,
   why="The point estimate is the midpoint (2.1 + 9.7)/2 = 5.9, and the margin of error is half the width, (9.7 - 2.1)/2 = 3.8."),
]
