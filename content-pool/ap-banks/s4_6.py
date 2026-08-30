# AP STATISTICS 4.6 Sampling Distributions for the Difference Between Two
# Sample Means - 25 questions
# CED: AP Statistics Course and Exam Description, Effective Fall 2026, Unit 4.
# Objectives 4.6.A (mean mu1 - mu2 and standard deviation sqrt(sigma1^2/n1 +
# sigma2^2/n2)), 4.6.B (conditions: two INDEPENDENT random samples; the 10
# percent condition applied to each population separately; both populations
# normal, or both n >= 30; an experiment needs only random assignment),
# 4.6.C (interpret in the context of the two populations).
# The error this topic exists to correct: variances add, standard deviations do
# not -- and they add even when the difference is being taken. Several items
# corner that directly.
# Every standard deviation and probability is recomputed in verify_s4_6.py with
# scipy.stats.norm; the wrong values behind the distractors are computed too.
TOPIC = ("4.6", "Sampling Distributions for the Difference Between Two Sample Means", 4)
QUESTIONS = [

 dict(q="Population 1 has standard deviation 6 and population 2 has standard deviation 8. Independent random samples of sizes 40 and 50 are taken. What is the standard deviation of the sampling distribution of the difference in sample means?", choices=[
   "0.557",
   "1.477",
   "2.080",
   "2.180",
   "14.000"], ans=1,
   why="Variances add: sqrt(6^2/40 + 8^2/50) = sqrt(0.9 + 1.28) = sqrt(2.18) = 1.477; 2.080 comes from adding the two standard deviations of the sample means, and 2.180 is the variance rather than the standard deviation."),

 dict(q="Two independent populations have means 72 and 68. Independent random samples are taken. What is the mean of the sampling distribution of the difference in sample means, taken as sample 1 minus sample 2?", choices=[
   "-4",
   "0",
   "4",
   "70",
   "140"], ans=2,
   why="The mean of the sampling distribution of a difference is the difference of the population means, 72 - 68 = 4, regardless of the two sample sizes."),

 dict(q="Two populations have means 72 and 68 and standard deviations 6 and 8. Independent random samples of sizes 40 and 50 are drawn and both populations are approximately normal. What is the probability that the difference in sample means (sample 1 minus sample 2) exceeds 6?", choices=[
   "0.0228",
   "0.0878",
   "0.1587",
   "0.3971",
   "0.9122"], ans=1,
   why="The sampling distribution has mean 4 and standard deviation 1.477, so z = (6 - 4)/1.477 = 1.354 and the upper-tail probability is 0.0878."),

 dict(q="Why is the standard deviation of the difference between two independent sample means computed from the SUM of the two variances rather than their difference?", choices=[
   "Variances of independent random variables add whether the variables are added or subtracted, because subtracting one variable does not remove its variability",
   "Because the difference is always positive, so the variances must be added",
   "Because the two sample sizes are usually unequal",
   "Because the standard deviations themselves add, and squaring the sum gives the variance",
   "Because subtracting variances could give a negative value only if the sample sizes were equal"], ans=0,
   why="Each sample mean varies from sample to sample, and subtracting two quantities that each vary produces a difference that varies more than either one, so the variabilities compound rather than cancel."),

 dict(q="Independent random samples of sizes 36 and 25 are drawn from populations with standard deviations 12 and 15. What is the standard deviation of the sampling distribution of the difference in sample means?", choices=[
   "2.449",
   "3.606",
   "4.000",
   "9.000",
   "13.000"], ans=1,
   why="sqrt(12^2/36 + 15^2/25) = sqrt(4 + 9) = sqrt(13) = 3.606; 13.000 is the variance and 9.000 is the second term alone."),

 dict(q="A researcher takes independent random samples of 80 households from a village with 600 households and 50 households from a town with 900 households. Which condition fails?", choices=[
   "The 10 percent condition, because 80 is more than 10 percent of 600",
   "The 10 percent condition, because 50 is more than 10 percent of 900",
   "The randomization condition, because the two places differ in size",
   "The sample data condition, because 50 is below 60",
   "No condition fails"], ans=0,
   why="The 10 percent condition is applied to each population separately: 0.10 x 600 = 60 and the village sample of 80 exceeds it, while the town sample of 50 is within 0.10 x 900 = 90."),

 dict(q="Independent random samples of sizes 30 and 45 come from populations with standard deviations 2.5 and 3.1. What is the standard deviation of the sampling distribution of the difference in sample means?", choices=[
   "0.422",
   "0.600",
   "0.650",
   "0.919",
   "1.032"], ans=2,
   why="sqrt(2.5^2/30 + 3.1^2/45) = sqrt(0.2083 + 0.2136) = sqrt(0.4219) = 0.650; 0.422 is the variance and 0.919 adds the two standard errors instead of their squares."),

 dict(q="Two populations have means that differ by 1.5 (population 1 minus population 2) and standard deviations 4 and 5. Independent random samples of sizes 50 and 60 are taken. What is the probability that the difference in sample means is negative?", choices=[
   "0.0403",
   "0.0808",
   "0.1587",
   "0.4602",
   "0.9597"], ans=0,
   why="The standard deviation of the difference is sqrt(16/50 + 25/60) = 0.858, so z = (0 - 1.5)/0.858 = -1.748 and the lower-tail probability is 0.0403."),

 dict(q="Two population distributions are strongly right-skewed. Independent random samples of sizes 18 and 22 are taken. Can the sampling distribution of the difference in sample means be modeled with a normal distribution?", choices=[
   "No, because neither sample size reaches 30 and neither population is normal",
   "No, because the two sample sizes are unequal",
   "Yes, because the combined sample size 40 exceeds 30",
   "Yes, because differences are always approximately normal",
   "Yes, because both samples were selected at random"], ans=0,
   why="CED 4.6.B.3 and 4.6.B.4 require either both populations normal or both sample sizes at least 30; adding the two sample sizes together is not one of the routes."),

 dict(q="An experiment randomly assigns 20 subjects to a treatment and 20 to a control, then compares mean responses. Which conditions must be verified for the sampling distribution of the difference in sample means?", choices=[
   "Only the randomization condition, satisfied by the random assignment, plus the normality requirement; the 10 percent condition does not apply",
   "The randomization condition and the 10 percent condition, because 40 subjects come from a population",
   "Only the 10 percent condition, because random assignment guarantees normality",
   "No conditions, because an experiment establishes causation",
   "The 10 percent condition for each treatment group separately"], ans=0,
   why="CED 4.6.B.2: for data from an experiment the randomization condition is met by the random assignment of treatments, and the 10 percent condition, which is about sampling without replacement from a population, is not needed."),

 dict(q="Two populations both have standard deviation 10. Independent random samples of sizes 25 and 100 are drawn. What is the standard deviation of the sampling distribution of the difference in sample means?", choices=[
   "1.000",
   "2.000",
   "2.236",
   "3.000",
   "5.000"], ans=2,
   why="sqrt(100/25 + 100/100) = sqrt(4 + 1) = sqrt(5) = 2.236; the smaller sample contributes far more of the variability than the larger one."),

 dict(q="Two populations have equal means. Their standard deviations are 9 and 7, and independent random samples of sizes 45 and 40 are drawn from approximately normal populations. What is the probability that the two sample means differ by more than 3 in absolute value?", choices=[
   "0.0423",
   "0.0845",
   "0.0968",
   "0.1690",
   "0.9155"], ans=1,
   why="With equal population means the difference is centered at 0 with standard deviation sqrt(81/45 + 49/40) = 1.739, so z = 3/1.739 = 1.725 and both tails together give 0.0845."),

 dict(q="Which statement correctly interprets a standard deviation of 1.48 for the sampling distribution of the difference between two sample means?", choices=[
   "In repeated pairs of independent samples of these sizes, the difference in sample means typically varies about 1.48 units from the true difference in population means",
   "Individual observations in the two populations typically differ by about 1.48 units",
   "The difference between the two population means is 1.48 units",
   "About 1.48 percent of paired samples give a difference far from the true difference",
   "The two sample means always differ by at most 1.48 units"], ans=0,
   why="A sampling distribution's standard deviation describes how much the statistic varies from one pair of samples to the next around the parameter mu1 - mu2."),

 dict(q="A researcher plans to reduce the standard deviation of the sampling distribution of the difference in two sample means. Both populations have standard deviation 10, and the samples are currently 20 and 200. Which change helps most?", choices=[
   "Increase the sample of 20",
   "Increase the sample of 200",
   "Increase both samples by 10 observations each",
   "Decrease the sample of 200 so the two are more nearly equal",
   "Nothing can help, because the population standard deviations are fixed"], ans=0,
   why="The two variance terms are 100/20 = 5.0 and 100/200 = 0.5, so almost all the variability comes from the smaller sample; adding observations there has by far the largest effect."),

 dict(q="Two independent random samples are taken, and the sampling distribution of x1bar - x2bar has mean -2.4. What does that tell you?", choices=[
   "The mean of population 1 is 2.4 units below the mean of population 2",
   "The mean of population 1 is 2.4 units above the mean of population 2",
   "The sample from population 1 had a mean 2.4 units below the other sample",
   "The two populations have the same mean, since the value is small",
   "The difference in sample means will always be -2.4"], ans=0,
   why="The center of the sampling distribution of x1bar - x2bar is mu1 - mu2, so a value of -2.4 says mu1 is 2.4 below mu2; it is a statement about the parameters, not about one pair of samples."),

 dict(q="Which of the following is NOT required for modeling the sampling distribution of a difference between two sample means with a normal distribution?", choices=[
   "The two population standard deviations must be equal",
   "The two samples must be independent of each other",
   "Each sample must be at most 10 percent of its own population when sampling without replacement",
   "Both populations are approximately normal, or both sample sizes are at least 30",
   "The data must come from random samples or a randomized experiment"], ans=0,
   why="Nothing in the CED's conditions requires equal population standard deviations; the formula uses each sigma separately precisely so that they may differ."),

 dict(q="Two samples are taken by measuring the same 40 people before and after an intervention. Is the sampling distribution described in this topic the right model for the difference in the two sample means?", choices=[
   "No, because the two samples are not independent; the same people appear in both",
   "Yes, because 40 is at least 30",
   "Yes, because both samples have the same size",
   "No, because 40 people is too small a sample",
   "Yes, provided the population is approximately normal"], ans=0,
   why="The formula sqrt(sigma1^2/n1 + sigma2^2/n2) assumes the two samples are independent; measuring the same people twice creates a paired design, which is analyzed through the single sample of differences instead."),

 dict(q="Independent random samples of sizes 100 and 100 are drawn from two populations with standard deviations 20 and 20. What is the variance of the sampling distribution of the difference in sample means?", choices=[
   "2.828",
   "4",
   "8",
   "40",
   "800"], ans=2,
   why="The variance is 400/100 + 400/100 = 4 + 4 = 8; 2.828 is the standard deviation, sqrt(8)."),

 dict(q="A study takes independent random samples of 120 employees from a firm of 900 employees and 150 customers from a customer base of 20,000. Regarding the 10 percent condition, which is true?", choices=[
   "It fails for the employees, because 120 is more than 10 percent of 900",
   "It fails for the customers, because 150 is more than 10 percent of 20,000",
   "It fails for both samples",
   "It holds for both samples",
   "It does not apply, because the two populations are different in kind"], ans=0,
   why="Applying n <= 0.10N separately: 0.10 x 900 = 90 and 120 > 90, so the employee sample fails, while 150 <= 2,000 for the customers."),

 dict(q="Two independent random samples of sizes 30 and 30 are drawn from populations with standard deviations 5 and 12. Which sample contributes more to the standard deviation of the difference in sample means?", choices=[
   "The sample from the population with standard deviation 12, contributing 4.8 of the total variance 5.633",
   "The sample from the population with standard deviation 5, because smaller values dominate",
   "They contribute equally, because the sample sizes are equal",
   "Neither, because the standard deviations subtract",
   "It cannot be determined without the population means"], ans=0,
   why="The variance terms are 25/30 = 0.833 and 144/30 = 4.8, summing to 5.633, so the more variable population supplies about 85 percent of the total even with equal sample sizes."),

 dict(q="For the difference between two sample means, doubling BOTH sample sizes multiplies the standard deviation of the sampling distribution by", choices=[
   "1/sqrt(2), about 0.707",
   "1/2",
   "1/4",
   "sqrt(2), about 1.414",
   "1, leaving it unchanged"], ans=0,
   why="Both variance terms are halved, so the total variance is halved and the standard deviation is multiplied by 1/sqrt(2)."),

 dict(q="Two population distributions are approximately normal. Independent random samples of sizes 8 and 11 are drawn. Can the sampling distribution of the difference in sample means be modeled with a normal distribution?", choices=[
   "Yes, because normal populations give a normal sampling distribution for the difference at any sample sizes",
   "No, because both sample sizes are below 30",
   "No, because the sample sizes are unequal",
   "Yes, but only because the two sample sizes sum to 19",
   "It cannot be determined without the population standard deviations"], ans=0,
   why="CED 4.6.B.3: if both population distributions are normal, the difference in sample means is normally distributed for any sample sizes; the n >= 30 requirement is the fallback for non-normal populations."),

 dict(q="A student computes the standard deviation of the difference between two sample means as 6/sqrt(40) + 8/sqrt(50) = 2.080. What is the error, and what is the correct value?", choices=[
   "Standard deviations cannot be added; the variances add, giving 1.477",
   "The two terms should be subtracted, giving 0.183",
   "The sample sizes should be added first, giving 1.567",
   "Nothing is wrong; 2.080 is correct",
   "The standard deviations should be averaged, giving 1.040"], ans=0,
   why="The correct calculation squares each standard error, adds, then takes the square root: sqrt(0.9 + 1.28) = 1.477, which is smaller than the student's 2.080 because a sum of squares is less than the square of the sum."),

 dict(q="Two independent random samples of sizes 50 and 50 are drawn from populations with the same standard deviation sigma. If sigma doubles, the standard deviation of the sampling distribution of the difference in sample means", choices=[
   "doubles",
   "quadruples",
   "is unchanged",
   "is multiplied by sqrt(2)",
   "is halved"], ans=0,
   why="Both variance terms carry sigma^2, so doubling sigma quadruples the total variance and doubles its square root."),

 dict(q="An investigator samples 35 patients from Clinic A and, from the SAME 35 patients, records a second measurement to compare against Clinic A's baseline. She then applies the two-sample formula sqrt(s1^2/35 + s2^2/35). What is the most serious problem?", choices=[
   "The two sets of measurements are not independent, so the two-sample standard deviation formula does not apply",
   "The sample size 35 is too small for a two-sample procedure",
   "The formula should divide by 70 rather than by 35",
   "There is no problem, since 35 is at least 30",
   "The two standard deviations should be averaged before dividing"], ans=0,
   why="Independence between the two samples is what licenses adding the variances; repeated measurements on the same patients are correlated, and the correct analysis reduces each patient to a single difference."),
]
