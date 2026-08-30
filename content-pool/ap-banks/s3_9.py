# AP STATISTICS 3.9 Sampling Distributions for the Difference Between Sample
# Proportions — 25 questions
# CED: Fall 2026, Unit 3. Skills 3.D (calculate means, standard deviations and
# parameters for probability distributions) and 4.E (justify the use of a method
# by verifying conditions).
#
# For two INDEPENDENT random samples,
#     mean of (p-hat1 - p-hat2) = p1 - p2
#     standard deviation        = sqrt( p1(1-p1)/n1  +  p2(1-p2)/n2 )
#
# The single most important structural fact, and the one that looks wrong to
# every student who meets it: the two variances ADD even though the statistic is
# a DIFFERENCE. Subtracting two independent quantities does not cancel their
# variability, it compounds it -- the difference is less predictable than either
# proportion on its own, not more. Three items are built on that, including one
# that offers the subtracted version as a distractor.
#
# The conditions are the same three as for one proportion, applied to EACH
# sample separately, plus independence BETWEEN the two samples.
#
# Worked values, all recomputed in verify_s3_9.py:
#   p1 0.60 n1 200, p2 0.50 n2 150 : mean 0.10, sd 0.05354
#   p1 0.40 n1 100, p2 0.30 n2 100 : mean 0.10, sd 0.06708
#   p1 0.25 n1 400, p2 0.20 n2 500 : mean 0.05, sd 0.02809
TOPIC = ("3.9", "Sampling Distributions for the Difference Between Sample Proportions", 3)

QUESTIONS = [
 dict(q="For two independent random samples, the mean of the sampling distribution of the difference between the two sample proportions is",
   choices=[
     "the difference between the two population proportions",
     "the sum of the two population proportions",
     "zero, always",
     "the average of the two population proportions",
     "the larger of the two population proportions"],
   ans=0,
   why="The difference of two unbiased estimators is unbiased for the difference of the parameters."),

 dict(q="For two independent random samples, the standard deviation of the sampling distribution of the difference between two sample proportions is the square root of",
   choices=[
     "the difference of the two variances",
     "the sum of the two variances",
     "the product of the two variances",
     "the larger of the two variances",
     "the average of the two variances"],
   ans=1,
   why="Variances of independent quantities add whether the statistics are added or subtracted, so the two variances are summed before the square root is taken."),

 dict(q="A student subtracts the two variances instead of adding them when finding the standard deviation of a difference of proportions. The reasoning error is that",
   choices=[
     "variability does not cancel when two independent quantities are subtracted; uncertainty from both samples contributes, so the variances add",
     "the two samples are dependent",
     "the formula requires a pooled proportion",
     "the difference should be taken in the other order",
     "there is no error"],
   ans=0,
   why="Each sample brings its own sampling error, and those errors compound rather than offset, so the difference is MORE variable than either proportion alone."),

 dict(q="Two independent samples have p1 = 0.60 with n1 = 200 and p2 = 0.50 with n2 = 150. The mean of the sampling distribution of the difference p-hat1 minus p-hat2 is",
   choices=["0.0000", "0.0500", "0.1000", "0.5500", "1.1000"],
   ans=2,
   why="The mean of the difference is p1 - p2 = 0.60 - 0.50 = 0.10."),

 dict(q="For those samples with p1 = 0.60, n1 = 200, p2 = 0.50, and n2 = 150, the standard deviation of the difference is closest to",
   choices=["0.0029", "0.0212", "0.0535", "0.0577", "0.1000"],
   ans=2,
   why="The variances are 0.0012 and 0.0016667; their sum is 0.0028667, whose square root is 0.0535. Subtracting the variances would give 0.0212, which is the trap."),

 dict(q="Two independent samples have p1 = 0.40 with n1 = 100 and p2 = 0.30 with n2 = 100. The standard deviation of the difference is closest to",
   choices=["0.0045", "0.0173", "0.0671", "0.0949", "0.1000"],
   ans=2,
   why="The variances 0.0024 and 0.0021 sum to 0.0045, and the square root of 0.0045 is 0.0671."),

 dict(q="Two independent samples have p1 = 0.25 with n1 = 400 and p2 = 0.20 with n2 = 500. The mean and standard deviation of the sampling distribution of the difference are closest to",
   choices=[
     "0.0500 and 0.0281",
     "0.0500 and 0.0008",
     "0.4500 and 0.0281",
     "0.0500 and 0.0530",
     "0.0250 and 0.0281"],
   ans=0,
   why="The mean is 0.25 - 0.20 = 0.05, and the standard deviation is the square root of 0.000469 + 0.00032 = 0.000789, which is 0.0281."),

 dict(q="Compared with the standard deviation of either sample proportion alone, the standard deviation of the difference between two independent sample proportions is",
   choices=[
     "smaller than both",
     "larger than both",
     "equal to the smaller one",
     "equal to their difference",
     "equal to zero"],
   ans=1,
   why="The sum of two positive variances exceeds either one, so the difference varies more from sample pair to sample pair than either proportion does on its own."),

 dict(q="If p1 = p2, the mean of the sampling distribution of the difference between the two sample proportions is",
   choices=["0", "1", "the common value of the two proportions", "the sum of the two proportions", "undefined"],
   ans=0,
   why="The mean is p1 - p2, which vanishes when the two population proportions are equal; the standard deviation, however, is still positive."),

 dict(q="If p1 = p2, the standard deviation of the sampling distribution of the difference between the two sample proportions is",
   choices=[
     "0, since the difference is always 0",
     "still positive, since each sample proportion still varies from sample to sample",
     "equal to the common value of the two proportions",
     "equal to one",
     "undefined"],
   ans=1,
   why="Equal parameters make the difference centre at 0, but individual sample pairs still produce nonzero differences, which is exactly why a test is needed."),

 dict(q="Which condition must hold for the usual standard deviation formula for a difference of proportions to apply?",
   choices=[
     "The two samples must be the same size",
     "The two samples must be independent of each other, and each must be a random sample",
     "The two populations must be the same size",
     "The two proportions must be equal",
     "One sample must be at least twice the other"],
   ans=1,
   why="Independence between the samples is what allows the variances to be added, and randomization is what makes each sampling distribution behave as described."),

 dict(q="For a difference of two sample proportions, the large counts condition requires that",
   choices=[
     "n1 + n2 be at least 30",
     "the expected numbers of successes and of failures be at least 10 in EACH of the two samples, giving four counts to check",
     "the expected number of successes be at least 10 in one sample",
     "the two sample sizes be equal",
     "the population sizes be known"],
   ans=1,
   why="The condition applies to each sample separately, so four counts are checked rather than two."),

 dict(q="Samples of n1 = 200 with p1 = 0.60 and n2 = 150 with p2 = 0.50 are drawn. Checking the large counts condition gives",
   choices=[
     "120, 80, 75, and 75, all at least 10, so the condition is met",
     "120 and 75 only, so the condition is not met",
     "0.60 and 0.50, both less than 10, so the condition fails",
     "350, so the condition is met",
     "the condition cannot be checked without the population sizes"],
   ans=0,
   why="The four expected counts are 200(0.6) = 120, 200(0.4) = 80, 150(0.5) = 75 and 150(0.5) = 75, and all exceed 10."),

 dict(q="Samples of n1 = 250 with p1 = 0.03 and n2 = 250 with p2 = 0.40 are drawn. Does the large counts condition hold?",
   choices=[
     "Yes, because both samples are large",
     "No, because the first sample's expected successes number 7.5, which is below 10",
     "No, because the second sample's expected failures are below 10",
     "Yes, because 0.03 and 0.40 are both between 0 and 1",
     "The condition applies only to one-sample situations"],
   ans=1,
   why="Checking all four counts, 250(0.03) = 7.5 falls short even though the other three are comfortable; a single failure among the four is enough."),

 dict(q="Two samples are collected from the same group of people, measuring each person before and after a treatment. Using the two-independent-proportions standard deviation formula here would be",
   choices=[
     "appropriate, since there are two proportions",
     "inappropriate, because the two samples are not independent; the same individuals appear in both",
     "appropriate, provided the sample is large",
     "appropriate, provided the proportions differ",
     "inappropriate only if the sample is small"],
   ans=1,
   why="Adding the variances assumes the two sampling errors are unrelated, and measurements on the same individuals are related by construction."),

 dict(q="For two independent samples with p1 = 0.60, n1 = 200, p2 = 0.50, n2 = 150, and all conditions met, what is the approximate probability that the difference p-hat1 minus p-hat2 exceeds 0.20?",
   choices=["0.0309", "0.0668", "0.1587", "0.9332", "0.9691"],
   ans=0,
   why="The difference has mean 0.10 and standard deviation 0.0535, so z = (0.20 - 0.10)/0.0535 = 1.868 and the right-tail area is 0.0309."),

 dict(q="For those same two samples, what is the approximate probability that the difference p-hat1 minus p-hat2 is negative, that is, that the second sample proportion comes out larger?",
   choices=["0.0000", "0.0309", "0.0668", "0.5000", "0.9691"],
   ans=1,
   why="z = (0 - 0.10)/0.0535 = -1.868, so the left-tail area is 0.0309; a negative difference is possible even though p1 exceeds p2."),

 dict(q="Increasing BOTH sample sizes, holding the two population proportions fixed, changes the sampling distribution of the difference by",
   choices=[
     "moving its centre toward 0",
     "leaving its centre at p1 - p2 and reducing its standard deviation",
     "increasing its standard deviation",
     "leaving it entirely unchanged",
     "making its centre equal to p1 + p2"],
   ans=1,
   why="Each variance has its own n in the denominator, so both shrink, while the centre depends only on the two parameters."),

 dict(q="The sampling distribution of the difference between two sample proportions is approximately normal when",
   choices=[
     "the two sample sizes are equal",
     "both samples are random and independent and all four expected counts are at least 10",
     "the two proportions are equal",
     "the sample sizes exceed 30",
     "the populations are normal"],
   ans=1,
   why="Randomization and independence make the formulas apply, and the four large counts are what make the normal approximation trustworthy."),

 dict(q="Which of the following is the correct expression for the standard deviation of the difference between two independent sample proportions?",
   choices=[
     "the square root of the first variance minus the second variance",
     "the square root of the first variance plus the second variance",
     "the first standard deviation minus the second standard deviation",
     "the first standard deviation plus the second standard deviation",
     "the square root of the sum of the two proportions"],
   ans=1,
   why="Variances add and standard deviations do not, so the sum is taken before the square root, not after."),

 dict(q="Adding the two STANDARD DEVIATIONS instead of the two variances would give an answer that is",
   choices=[
     "smaller than the correct value",
     "larger than the correct value",
     "exactly correct",
     "negative",
     "zero"],
   ans=1,
   why="The square root of a sum is less than the sum of the square roots for positive quantities, so adding standard deviations overstates the variability."),

 dict(q="Two independent samples of size 100 each are drawn from populations with p1 = p2 = 0.50. The sampling distribution of the difference is centred at 0 with standard deviation closest to",
   choices=["0.0500", "0.0707", "0.1000", "0.2500", "0.5000"],
   ans=1,
   why="Each variance is 0.0025, the sum is 0.005, and the square root of 0.005 is 0.0707."),

 dict(q="For two independent samples, the order of subtraction, p-hat1 minus p-hat2 rather than p-hat2 minus p-hat1,",
   choices=[
     "changes the standard deviation",
     "changes the sign of the mean but leaves the standard deviation unchanged",
     "changes nothing at all",
     "makes the distribution non-normal",
     "is not allowed"],
   ans=1,
   why="Reversing the order negates the centre; variability is unaffected because the two variances are added either way."),

 dict(q="A researcher plans to compare two proportions and wants the sampling distribution of the difference to be as narrow as possible. The most effective step is to",
   choices=[
     "make the two proportions equal",
     "increase both sample sizes",
     "increase only the larger sample",
     "decrease the smaller sample",
     "use dependent samples"],
   ans=1,
   why="Both terms of the variance carry their own sample size, so reducing the total variability means increasing both, and increasing only one leaves the other term untouched."),

 dict(q="The sampling distribution of the difference between two sample proportions describes",
   choices=[
     "the values in the two samples",
     "how the difference between the two sample proportions varies across repeated pairs of samples",
     "the difference between the two populations' sizes",
     "the values of the two parameters",
     "the difference between the two sample sizes"],
   ans=1,
   why="Like any sampling distribution, it describes the behaviour of a statistic across repeated sampling, not the data in any one pair of samples."),
]
