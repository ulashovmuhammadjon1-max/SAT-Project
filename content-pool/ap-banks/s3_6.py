# AP STATISTICS 3.6 p-Values — 25 questions
# CED: Fall 2026, Unit 3. Learning objective 3.6.A (interpret the p-value of a
# hypothesis test for a population proportion), skill 4.F.
#
# EK 3.6.A.1: given that the null hypothesis is TRUE, the test statistic has a
# probability distribution called the null distribution, and the p-value is the
# probability of obtaining a test statistic as extreme as, or more extreme than,
# the one observed, in the direction of the alternative hypothesis.
#
# Two things make p-values the most misread quantity in the course, and this
# module attacks both.
#
# 1. THE CONDITIONAL RUNS ONE WAY. A p-value is the probability of the DATA
#    given the null hypothesis. It is NOT the probability that the null
#    hypothesis is true, and it is NOT the probability that the alternative is
#    false. Four items separate those readings; the correct one always begins
#    "assuming the null hypothesis is true".
# 2. THE TAIL DEPENDS ON THE ALTERNATIVE. A two-sided alternative doubles the
#    one-sided area, so the SAME test statistic gives two different p-values
#    depending on how the alternative was written. Items 8, 9 and 10 use
#    z = 2.10 three ways so that the difference is unmissable.
#
# Values used, all recomputed with scipy in verify_s3_6.py:
#   z =  1.85, right tail       p = 0.0322
#   z = -2.10, left tail        p = 0.0179
#   z =  2.10, two-sided        p = 0.0357
#   z =  1.42, two-sided        p = 0.1556
#   z =  2.58, right tail       p = 0.0049
TOPIC = ("3.6", "p-Values", 3)

QUESTIONS = [
 dict(q="The p-value of a hypothesis test is",
   choices=[
     "the probability that the null hypothesis is true",
     "the probability, assuming the null hypothesis is true, of obtaining a test statistic as extreme as or more extreme than the one observed",
     "the probability that the alternative hypothesis is true",
     "the probability of making a wrong decision",
     "the proportion of the sample that supports the alternative"],
   ans=1,
   why="A p-value is computed from the null distribution, so it is a probability about the DATA given the null, not a probability about the hypothesis."),

 dict(q="The distribution used to compute a p-value is called the null distribution because it is the distribution of the test statistic",
   choices=[
     "when the alternative hypothesis is true",
     "given that the null hypothesis is true",
     "in the sample actually collected",
     "of the population",
     "when the sample size is zero"],
   ans=1,
   why="Every p-value calculation begins by assuming the null hypothesis and asking how surprising the observed statistic would then be."),

 dict(q="A small p-value indicates that",
   choices=[
     "the observed result would be unlikely if the null hypothesis were true, giving evidence against the null",
     "the null hypothesis is definitely false",
     "the alternative hypothesis is definitely true",
     "the sample size was too small",
     "the observed result is exactly what the null predicts"],
   ans=0,
   why="A small p-value means the data are surprising under the null, which counts as evidence against it without proving anything."),

 dict(q="A large p-value indicates that",
   choices=[
     "the null hypothesis has been proved true",
     "the observed result is consistent with what the null hypothesis predicts, so there is not convincing evidence against the null",
     "the alternative hypothesis is true",
     "an error was made in the calculation",
     "the sample was not random"],
   ans=1,
   why="A large p-value means the data are unremarkable under the null; failing to find evidence against a claim is not the same as establishing it."),

 dict(q="A test of H0: p = 0.40 against Ha: p > 0.40 produces a test statistic of z = 1.85. The p-value is closest to",
   choices=["0.0161", "0.0322", "0.0644", "0.9678", "1.8500"],
   ans=1,
   why="A one-sided alternative in the greater-than direction uses the right-tail area beyond z = 1.85, which is 0.0322; 0.0644 would be the two-sided value."),

 dict(q="A test of H0: p = 0.60 against Ha: p < 0.60 produces a test statistic of z = -2.10. The p-value is closest to",
   choices=["0.0089", "0.0179", "0.0357", "0.9821", "2.1000"],
   ans=1,
   why="A less-than alternative uses the left-tail area below z = -2.10, which is 0.0179."),

 dict(q="A test of H0: p = 0.60 against Ha: p not equal to 0.60 produces a test statistic of z = -2.10. The p-value is closest to",
   choices=["0.0089", "0.0179", "0.0357", "0.9643", "0.9821"],
   ans=2,
   why="A two-sided alternative counts both tails, so the p-value is twice the one-tail area: 2(0.0179) = 0.0357."),

 dict(q="Comparing the two previous items, the SAME test statistic z = -2.10 gives p-values of 0.0179 and 0.0357. The reason is that",
   choices=[
     "one of the calculations is wrong",
     "the p-value depends on the alternative hypothesis: a two-sided alternative counts both tails and so doubles the one-sided area",
     "the sample sizes differ",
     "the null hypotheses differ",
     "p-values are only approximate"],
   ans=1,
   why="'As extreme or more extreme' is measured in the direction the alternative specifies, so how Ha is written changes which area is counted."),

 dict(q="A test of H0: p = 0.25 against Ha: p not equal to 0.25 produces z = 1.42. The p-value is closest to",
   choices=["0.0778", "0.1556", "0.4222", "0.8444", "0.9222"],
   ans=1,
   why="The one-tail area beyond 1.42 is 0.0778, and doubling it for the two-sided alternative gives 0.1556."),

 dict(q="A test of H0: p = 0.10 against Ha: p > 0.10 produces z = 2.58. The p-value is closest to",
   choices=["0.0049", "0.0099", "0.4951", "0.9901", "0.9951"],
   ans=0,
   why="The right-tail area beyond z = 2.58 is 0.0049, a small p-value indicating strong evidence against the null."),

 dict(q="A p-value of 0.03 is best interpreted as",
   choices=[
     "there is a 3% chance the null hypothesis is true",
     "assuming the null hypothesis is true, there is a 3% chance of getting a result at least as extreme as the one observed",
     "there is a 97% chance the alternative hypothesis is true",
     "3% of the sample supports the alternative",
     "the test will be wrong 3% of the time"],
   ans=1,
   why="The interpretation must state the conditional on the null and describe the probability of results at least as extreme, in the alternative's direction."),

 dict(q="A student writes, 'The p-value of 0.03 means there is a 3% probability that the null hypothesis is true.' This is wrong because",
   choices=[
     "the p-value is a probability about the data computed under the assumption that the null is true, not a probability about the hypothesis itself",
     "3% is too small a probability",
     "p-values cannot be expressed as percentages",
     "the null hypothesis has no probability at all in any framework",
     "the statement is actually correct"],
   ans=0,
   why="The conditioning runs from hypothesis to data, and reversing it is the single most common misreading of a p-value."),

 dict(q="A student writes, 'The p-value of 0.03 means there is a 97% probability that the alternative hypothesis is true.' This is wrong because",
   choices=[
     "the complement of a p-value is not the probability that the alternative is true; the p-value says nothing directly about the probability of any hypothesis",
     "97% is too large",
     "the alternative hypothesis is always false",
     "the complement should be 3%",
     "the statement is actually correct"],
   ans=0,
   why="Subtracting a p-value from 1 does not convert a statement about data into a statement about a hypothesis."),

 dict(q="Two tests of the same null hypothesis produce p-values of 0.002 and 0.20. The stronger evidence against the null comes from",
   choices=[
     "the test with p-value 0.002, because such an extreme result is very unlikely if the null is true",
     "the test with p-value 0.20, because it is larger",
     "neither; the two are equivalent",
     "whichever test used the larger sample",
     "it cannot be determined without the significance level"],
   ans=0,
   why="The smaller the p-value, the more surprising the data are under the null, and so the stronger the evidence against it."),

 dict(q="At a significance level of alpha = 0.05, a p-value of 0.032 leads to the decision to",
   choices=[
     "reject the null hypothesis, since 0.032 is less than 0.05",
     "fail to reject the null hypothesis, since 0.032 is less than 0.05",
     "accept the null hypothesis",
     "accept the alternative hypothesis as proved",
     "declare the test invalid"],
   ans=0,
   why="A p-value below the significance level means the result is too extreme to attribute to chance under the null, so the null is rejected."),

 dict(q="At a significance level of alpha = 0.01, a p-value of 0.032 leads to the decision to",
   choices=[
     "reject the null hypothesis",
     "fail to reject the null hypothesis, since 0.032 is greater than 0.01",
     "accept the null hypothesis as true",
     "reverse the hypotheses",
     "recompute the p-value"],
   ans=1,
   why="The same p-value can lead to different decisions at different significance levels, which is why alpha must be fixed before the data are examined."),

 dict(q="When a test does not produce a small p-value, the correct conclusion is to",
   choices=[
     "accept the null hypothesis as true",
     "fail to reject the null hypothesis, since there is not convincing evidence against it",
     "conclude the alternative is false",
     "conclude the parameter equals the null value exactly",
     "repeat the study until the p-value is small"],
   ans=1,
   why="A test can find evidence against a claim but never establish one, so the language is 'fail to reject' rather than 'accept'."),

 dict(q="For a fixed alternative direction and a fixed null hypothesis, a test statistic further from 0 produces",
   choices=[
     "a larger p-value",
     "a smaller p-value",
     "the same p-value",
     "a p-value greater than 1",
     "a negative p-value"],
   ans=1,
   why="Moving further into the tail leaves less area beyond the statistic, so the observed result becomes more surprising under the null."),

 dict(q="A p-value of 0.62 for a test of H0: p = 0.50 means that",
   choices=[
     "the population proportion is 0.62",
     "results at least as extreme as the one observed would occur about 62% of the time if the null hypothesis were true, so the data are entirely unsurprising",
     "62% of the sample supported the claim",
     "the null hypothesis is 62% likely",
     "the test statistic is 0.62"],
   ans=1,
   why="A p-value that large says the observed result is the sort of thing the null routinely produces, so it gives no evidence against the null."),

 dict(q="A p-value can never be",
   choices=[
     "smaller than 0.001",
     "greater than 1",
     "equal to 0.5",
     "based on a one-sided alternative",
     "computed without a significance level"],
   ans=1,
   why="A p-value is a probability, so it lies between 0 and 1; a two-sided calculation that produced a value above 1 signals doubling an area larger than one half."),

 dict(q="The significance level alpha should be chosen",
   choices=[
     "after computing the p-value, so that the decision comes out as hoped",
     "before the data are collected and analyzed",
     "to equal the p-value",
     "to equal the sample proportion",
     "only when the p-value is small"],
   ans=1,
   why="Setting alpha after seeing the p-value lets the researcher pick the conclusion, and the stated error rate then no longer describes the procedure used."),

 dict(q="In a test with Ha: p > p0, a sample proportion BELOW the null value produces a test statistic that is negative, and therefore a p-value that is",
   choices=[
     "very small, giving strong evidence for the alternative",
     "greater than 0.5, giving no evidence at all for the alternative",
     "exactly 0",
     "exactly 1",
     "negative"],
   ans=1,
   why="The right-tail area beyond a negative z exceeds one half, which correctly reports that data on the wrong side of the null are no evidence for a greater-than alternative."),

 dict(q="A researcher reports 'p-value = 0.048, so we reject H0 at alpha = 0.05 and conclude the proportion has increased.' A second researcher reports 'p-value = 0.052, so we fail to reject at alpha = 0.05.' The best comment is that",
   choices=[
     "the two studies reached opposite conclusions about reality",
     "the two p-values are nearly identical, so the evidence is nearly the same and treating 0.05 as a sharp boundary overstates the difference",
     "one of the studies must have made an error",
     "the second study should lower its significance level",
     "p-values near 0.05 cannot be interpreted"],
   ans=1,
   why="A p-value is a continuous measure of how surprising the data are, and 0.048 against 0.052 is a negligible difference in evidence despite a different decision at a fixed alpha."),

 dict(q="A p-value is computed assuming which of the following?",
   choices=[
     "the alternative hypothesis is true",
     "the null hypothesis is true and the test's conditions are met",
     "the sample proportion equals the population proportion",
     "the significance level is 0.05",
     "the population is normal"],
   ans=1,
   why="The null distribution is derived under the null hypothesis, and it is only the right distribution if the randomization, 10% and normality conditions hold."),

 dict(q="Which sequence correctly describes how a p-value is used?",
   choices=[
     "compute the p-value, then choose the hypotheses to match it",
     "state the hypotheses and alpha, check conditions, compute the test statistic, find the p-value in the alternative's direction, then decide",
     "choose alpha after seeing the p-value, then state the hypotheses",
     "compute the p-value, then check whether the conditions were met",
     "reject the null first, then compute the p-value to confirm"],
   ans=1,
   why="Hypotheses and significance level come first, conditions are verified before the calculation is trusted, and the decision comes last."),
]
