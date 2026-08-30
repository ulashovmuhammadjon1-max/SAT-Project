# AP STATISTICS 4.9 Setting Up a Test for the Difference Between Two Population
# Means - 25 questions
# CED: AP Statistics Course and Exam Description, Effective Fall 2026, Unit 4.
# Objectives 4.9.A (identify the two-sample t-test and state the parameters in
# context), 4.9.B (H0: mu1 - mu2 = 0, equivalently mu1 = mu2; Ha one- or
# two-sided), 4.9.C (the three conditions: two independent random samples or a
# randomized experiment; the 10 percent condition per population, unnecessary
# for an experiment; both n >= 30 or both populations approximately normal, and
# if either n < 30 BOTH sample distributions free from strong skewness and
# outliers).
# The distinction this topic must protect is two-sample versus matched pairs:
# it is settled by whether the two measurements come from the same unit, never
# by equal sample sizes or by sample size at all. Several items test it, and
# several test a condition that FAILS.
# Degrees of freedom and every 10 percent threshold are computed in
# verify_s4_9.py.
TOPIC = ("4.9", "Setting Up a Test for the Difference Between Two Population Means", 4)
QUESTIONS = [

 dict(q="A researcher wants to know whether two brands of tires differ in mean tread life, using an independent random sample of tires of each brand. What are the appropriate hypotheses?", choices=[
   "H0: mu1 = mu2 versus Ha: mu1 is not equal to mu2",
   "H0: mu1 = mu2 versus Ha: mu1 > mu2",
   "H0: mu1 is not equal to mu2 versus Ha: mu1 = mu2",
   "H0: xbar1 = xbar2 versus Ha: xbar1 is not equal to mu2",
   "H0: mu_d = 0 versus Ha: mu_d is not equal to 0"], ans=0,
   why="A question about a difference in either direction is two-sided, the null asserts no difference, and hypotheses concern population means; mu_d belongs to a matched-pairs design."),

 dict(q="Which test is appropriate for comparing the mean incomes of two independent random samples drawn from two different cities, when neither population standard deviation is known?", choices=[
   "A two-sample t-test for a difference between two population means",
   "A one-sample t-test for a population mean difference",
   "A two-sample z-test for a difference between two population means",
   "A one-sample t-test using the pooled data from both cities",
   "A chi-square test for independence"], ans=0,
   why="Two independent samples with unknown population standard deviations is exactly the two-sample t-test; the mean-difference procedure is for matched pairs, and pooling the two cities estimates a different parameter."),

 dict(q="A pharmaceutical trial randomly assigns patients to a new drug or a placebo and asks whether the new drug produces a higher mean improvement. With group 1 the drug and group 2 the placebo, what is the alternative hypothesis?", choices=[
   "Ha: mu1 > mu2",
   "Ha: mu1 < mu2",
   "Ha: mu1 is not equal to mu2",
   "Ha: xbar1 > xbar2",
   "Ha: mu1 - mu2 = 0"], ans=0,
   why="'Higher mean improvement for the drug' is a one-sided upper-tail alternative in terms of the population means; the sample means never appear in a hypothesis."),

 dict(q="A study measures the blood pressure of 40 patients before and after a treatment. Which test is appropriate?", choices=[
   "A one-sample t-test for a population mean difference, using the 40 differences",
   "A two-sample t-test for a difference between two population means",
   "A two-sample t-test, because there are 80 measurements",
   "A one-sample t-test for a population mean, using all 80 measurements",
   "A two-sample z-test, because 40 is at least 30"], ans=0,
   why="The two measurements come from the same patient, so the data are paired; the two-sample procedure requires independent samples, which these are not."),

 dict(q="A two-sample t-test compares mean scores from independent random samples of sizes 24 and 31. One of the two samples is strongly skewed with an outlier. Which condition fails?", choices=[
   "The sample data condition, because one sample size is below 30 and so both sample distributions must be free from strong skewness and outliers",
   "The randomization condition, because skewness indicates a biased sample",
   "The 10 percent condition, because 24 is below 30",
   "The sample data condition, because the two sample sizes are unequal",
   "No condition fails, because one sample size exceeds 30"], ans=0,
   why="CED 4.9.C.1.iii: once either sample size falls below 30, both sample distributions must be free from strong skewness and outliers, so the larger sample does not rescue the smaller."),

 dict(q="A study takes independent random samples of 90 students from a school of 800 students and 70 teachers from a district of 1,200 teachers. Which condition fails?", choices=[
   "The 10 percent condition, because 90 is more than 10 percent of 800",
   "The 10 percent condition, because 70 is more than 10 percent of 1,200",
   "The randomization condition, because students and teachers are different kinds of unit",
   "The sample data condition, because both samples exceed 30",
   "No condition fails"], ans=0,
   why="The condition n <= 0.10N is applied to each population separately: 0.10 x 800 = 80 and the student sample of 90 exceeds it, while 70 sits within 0.10 x 1,200 = 120."),

 dict(q="An experiment randomly assigns 25 seedlings to each of two light regimes and compares mean height. Which condition is NOT required?", choices=[
   "The 10 percent condition",
   "The randomization condition",
   "That both sample distributions be free from strong skewness and outliers",
   "That the two groups be independent of each other",
   "That the response variable be quantitative"], ans=0,
   why="CED 4.9.C.1.ii states the 10 percent condition is unnecessary for a randomized experiment; and since 25 is below 30, the freedom from skewness and outliers is still required for both groups."),

 dict(q="Which statement of the parameters is appropriate for a two-sample t-test comparing delivery times for two couriers?", choices=[
   "mu1 = the mean delivery time, in minutes, for all deliveries by courier 1, and mu2 = the same for courier 2",
   "xbar1 and xbar2 = the mean delivery times of the two samples",
   "mu = the mean delivery time for all deliveries by both couriers combined",
   "mu_d = the mean difference in delivery time within each pair of deliveries",
   "p1 and p2 = the proportions of late deliveries for the two couriers"], ans=0,
   why="CED 4.9.A.2: the parameters name the two population means, the response variable with its units, and the two populations; a mean difference parameter belongs to a paired design."),

 dict(q="A two-sample t-test is run on independent samples of sizes 18 and 22. What are the conservative degrees of freedom, and what is the largest value any acceptable df could take?", choices=[
   "17 conservative, 38 maximum",
   "18 conservative, 40 maximum",
   "21 conservative, 38 maximum",
   "17 conservative, 40 maximum",
   "39 conservative, 40 maximum"], ans=0,
   why="The conservative df is the smaller of n1 - 1 = 17 and n2 - 1 = 21, so 17; the upper end of the CED's bracket is n1 + n2 - 2 = 38."),

 dict(q="Which pair of hypotheses is written incorrectly for a two-sample t-test?", choices=[
   "H0: xbar1 - xbar2 = 0 versus Ha: xbar1 - xbar2 > 0",
   "H0: mu1 = mu2 versus Ha: mu1 > mu2",
   "H0: mu1 - mu2 = 0 versus Ha: mu1 - mu2 > 0",
   "H0: mu1 = mu2 versus Ha: mu1 is not equal to mu2",
   "H0: mu1 - mu2 = 0 versus Ha: mu1 - mu2 < 0"], ans=0,
   why="Hypotheses are claims about unknown parameters; the two sample means are already known from the data, so nothing about them is left to test."),

 dict(q="Twenty pairs of identical twins are recruited, and one twin from each pair is randomly assigned to a new tutoring program while the other receives the standard program. Which test compares mean improvement most appropriately?", choices=[
   "A one-sample t-test for a population mean difference, using the 20 within-pair differences",
   "A two-sample t-test, because the two twins received different treatments",
   "A two-sample t-test, because there are 40 students",
   "A one-sample t-test for a population mean, using all 40 improvements",
   "A two-sample z-test, because random assignment was used"], ans=0,
   why="The twins are matched by design, so the natural unit of analysis is the pair; differencing within a pair removes the family-to-family variation that would otherwise obscure the comparison."),

 dict(q="An economist wants evidence that mean household spending is LOWER in region A than in region B, using independent random samples. With A as population 1, which hypotheses are correct?", choices=[
   "H0: mu1 = mu2 versus Ha: mu1 < mu2",
   "H0: mu1 = mu2 versus Ha: mu1 > mu2",
   "H0: mu1 < mu2 versus Ha: mu1 = mu2",
   "H0: mu1 - mu2 = 0 versus Ha: mu1 - mu2 is not equal to 0",
   "H0: mu1 = mu2 versus Ha: mu_d < 0"], ans=0,
   why="Evidence that region A is lower is the one-sided alternative mu1 < mu2, equivalently mu1 - mu2 < 0; mu_d denotes a paired mean difference, which does not apply here."),

 dict(q="A researcher collects volunteers at two different shopping centers and compares their mean spending with a two-sample t-test. What is the most serious problem?", choices=[
   "The randomization condition fails, because neither group is a random sample and no treatment was randomly assigned",
   "The 10 percent condition fails, because volunteers cannot be counted",
   "The sample data condition fails, because volunteers are always skewed",
   "Nothing is wrong, provided both groups exceed 30",
   "The test should be a one-sample t-test instead"], ans=0,
   why="Without random sampling or random assignment there is no sampling distribution to refer the statistic to, and a large sample does not repair the problem."),

 dict(q="Independent random samples of sizes 52 and 61 come from populations that are both moderately right-skewed. Are the conditions for a two-sample t-test met?", choices=[
   "Yes, because both sample sizes are at least 30",
   "No, because both populations are skewed",
   "No, because the sample sizes are unequal",
   "Yes, but only if the two population standard deviations are equal",
   "It cannot be determined without the two sample means"], ans=0,
   why="CED 4.9.C.1.iii is satisfied when both sample sizes reach 30; the freedom-from-skewness requirement applies only when a sample falls below 30, and equal standard deviations are never required."),

 dict(q="Which of these is NOT one of the three conditions for a two-sample t-test for a difference between means?", choices=[
   "The two population standard deviations must be equal",
   "The data come from two independent random samples or from a randomized experiment",
   "Each sample is at most 10 percent of its own population when sampling without replacement",
   "Both samples reach 30, or both populations are approximately normal",
   "If either sample is below 30, both sample distributions are free from strong skewness and outliers"], ans=0,
   why="Nothing in the CED requires equal population standard deviations; the two-sample t procedure keeps s1 and s2 separate precisely so that they may differ."),

 dict(q="A test of H0: mu1 = mu2 against Ha: mu1 > mu2 is planned, but the researcher decides on the direction after seeing that xbar1 exceeded xbar2. What is the consequence?", choices=[
   "The true Type I error rate is larger than the stated significance level, because the favorable tail was chosen after seeing the data",
   "The p-value will be too large, making the test too conservative",
   "The degrees of freedom must be halved to compensate",
   "There is no consequence, since the alternative matches the data",
   "The test becomes a two-sided test automatically"], ans=0,
   why="Choosing the tail after looking guarantees the more favorable half of a two-sided test, so the procedure rejects a true null more often than alpha advertises."),

 dict(q="A two-sample t-test compares mean weights of packages from two machines using independent random samples of 45 and 50 packages from production runs of 5,000 and 6,000. Which conditions are met?", choices=[
   "All three: the samples are random and independent, each is under 10 percent of its run, and both sizes are at least 30",
   "Only randomization, since the 10 percent condition fails for both",
   "Only the sample data condition",
   "None, because the two production runs differ in size",
   "Only the 10 percent condition, since 45 is below 50"], ans=0,
   why="0.10 x 5,000 = 500 and 0.10 x 6,000 = 600, so both samples are far inside the 10 percent limit, and both sample sizes reach 30."),

 dict(q="Which of these designs requires a two-sample t-test rather than a one-sample t-test for a mean difference?", choices=[
   "Comparing the mean lifetime of bulbs from factory A with the mean lifetime of a separate set of bulbs from factory B",
   "Comparing each student's score on two versions of a test",
   "Comparing the fuel economy of 15 cars with and without a fuel additive, each car tested twice",
   "Comparing the yield of 20 fields under two fertilizers, each field split in half",
   "Comparing each subject's pulse before and after exercise"], ans=0,
   why="Only the first uses two separate sets of units, making the samples independent; the other four all measure the same unit or split the same unit under both conditions, which is matched pairs."),

 dict(q="For a two-sample t-test, what does the null hypothesis assert about the two population means?", choices=[
   "That they are equal, so their difference is 0",
   "That their difference equals the observed difference in sample means",
   "That the two sample means are equal",
   "That the two population standard deviations are equal",
   "That the two populations are both normal"], ans=0,
   why="CED 4.9.B.1: H0 is mu1 - mu2 = 0, equivalently mu1 = mu2; normality and equal standard deviations are conditions or assumptions, not the null hypothesis."),

 dict(q="Independent random samples of sizes 15 and 17 are taken from populations that are stated to be approximately normal. Is the sample data condition met?", choices=[
   "Yes, because both populations are stated to be approximately normal, which carries no sample-size requirement",
   "No, because both sample sizes are below 30",
   "No, because the sample sizes are unequal",
   "Yes, but only because the sample sizes sum to 32",
   "It cannot be determined without seeing the two sample distributions"], ans=0,
   why="CED 4.9.C.1.iii offers 'both populations approximately normal' as an alternative to both sample sizes reaching 30, and it applies at any sample size."),

 dict(q="A study compares mean scores between an experimental class of 28 students and a control class of 29 students, with students randomly assigned to the two classes. Both score distributions are roughly symmetric with no outliers. Which statement is correct?", choices=[
   "The conditions are met: random assignment covers randomization, the 10 percent condition does not apply to an experiment, and both distributions are well behaved despite n being below 30",
   "The conditions fail, because both sample sizes are below 30",
   "The conditions fail, because the 10 percent condition cannot be checked",
   "The conditions are met only because the two class sizes are nearly equal",
   "A one-sample t-test should be used, since the two classes came from one school"], ans=0,
   why="For an experiment the 10 percent condition is waived; with both n below 30 the sample data condition is met by the absence of strong skewness and outliers, which is stated here."),

 dict(q="Why must a two-sample t-test not be applied to a matched-pairs design?", choices=[
   "The two sets of measurements are dependent, so the standard error formula, which adds variances as if they were independent, is wrong",
   "The two sets of measurements always have the same mean",
   "The degrees of freedom would be too large to look up",
   "Matched pairs always produce sample sizes below 30",
   "A two-sample test cannot handle a one-sided alternative"], ans=0,
   why="Adding s1^2/n1 and s2^2/n2 assumes independence; when the same unit supplies both values the measurements are correlated, and the paired analysis on the differences is the correct procedure."),

 dict(q="A two-sample t-test uses independent samples of sizes 30 and 40. What is the largest value the degrees of freedom could take under the CED's bracket, and what is the smallest?", choices=[
   "largest 68, smallest 29",
   "largest 70, smallest 30",
   "largest 68, smallest 39",
   "largest 69, smallest 29",
   "largest 70, smallest 29"], ans=0,
   why="The bracket runs from the smaller of n1 - 1 = 29 and n2 - 1 = 39, which is 29, up to n1 + n2 - 2 = 68."),

 dict(q="A researcher writes H0: mu1 - mu2 = 5 for a two-sample t-test comparing two teaching methods. Is that a valid null hypothesis for the standard procedure described in the CED?", choices=[
   "No, the standard two-sample t-test uses a null difference of 0, so H0 is mu1 - mu2 = 0",
   "Yes, any value may be used as the null difference in the standard procedure",
   "No, because the null hypothesis must always be about a single mean",
   "Yes, provided the alternative is two-sided",
   "No, because a difference of 5 is too large to test"], ans=0,
   why="CED 4.9.B.1 writes the null as mu1 - mu2 = 0, equivalently mu1 = mu2, and 4.10.A.1's test statistic subtracts 0 in the numerator."),

 dict(q="Two independent random samples of sizes 12 and 14 are drawn from populations whose shapes are unknown, and neither sample shows skewness or outliers. What is the correct assessment of the sample data condition?", choices=[
   "It is met, because with sample sizes below 30 the requirement is that both sample distributions be free from strong skewness and outliers, which they are",
   "It fails, because neither sample size reaches 30",
   "It fails, because the population shapes are unknown",
   "It is met, because the sample sizes sum to 26",
   "It cannot be assessed without the population standard deviations"], ans=0,
   why="CED 4.9.C.1.iii names the sample distributions themselves as the fallback when n is below 30 and the population shape is not stated; well-behaved samples satisfy it."),
]
