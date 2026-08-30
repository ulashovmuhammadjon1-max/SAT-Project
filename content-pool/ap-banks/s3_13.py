# AP STATISTICS 3.13 Carrying Out a Test for the Difference Between Two
# Population Proportions — 25 questions
# CED: Fall 2026, Unit 3. Skill 3.E (calculate the results of the inference
# method), with 4.F and 4.G for interpreting and concluding.
#
# The test statistic is
#     z = (p-hat1 - p-hat2) / sqrt( p-hat_c (1 - p-hat_c) (1/n1 + 1/n2) )
# where p-hat_c is the POOLED proportion (x1 + x2)/(n1 + n2) introduced in 3.12.
# The numerator is the observed difference; the denominator is the standard
# error the null hypothesis implies.
#
# Worked scenarios, all recomputed in verify_s3_13.py:
#   120/300 vs  90/300, two-sided : pooled 0.3500, SE 0.03894, z = 2.568, p = 0.0102
#    95/250 vs  70/250, p1 > p2   : pooled 0.3300, SE 0.04206, z = 2.378, p = 0.0087
#   140/400 vs 120/400, p1 > p2   : pooled 0.3250, SE 0.03312, z = 1.510, p = 0.0656
#    48/200 vs  36/150, two-sided : pooled 0.2400, SE 0.04613, z = 0.000, p = 1.0000
#
# The pooled and unpooled standard errors are numerically very close -- 0.0389
# against 0.0387 on the first scenario -- so the unpooled value is NOT offered as
# a numeric distractor anywhere here; a student using the wrong method would
# still round to the keyed choice. The distinction is tested as a direction of
# error instead, in q18, and conceptually in q2. This is the same decision, for
# the same reason, as the one recorded in the header of s3_10.py.
#
# That last scenario is deliberate: the two sample proportions are identical, so
# the observed difference is exactly 0, the test statistic is exactly 0 and the
# two-sided p-value is exactly 1. It is the clearest possible case of data that
# give no evidence whatever against the null, and it is worth one item because a
# p-value of 1 looks like an error to a student seeing it for the first time.
#
# The third scenario is the near-miss: p = 0.0656 fails at alpha = 0.05 and
# succeeds at alpha = 0.10, so the same data support opposite decisions under
# two defensible significance levels.
TOPIC = ("3.13", "Carrying Out a Test for the Difference Between Two Population Proportions", 3)

QUESTIONS = [
 dict(q="The numerator of the test statistic for a two-sample z-test for proportions is",
   choices=[
     "the difference between the two sample proportions",
     "the pooled proportion",
     "the sum of the two sample proportions",
     "the difference between the two sample sizes",
     "the difference between the two population proportions"],
   ans=0,
   why="The statistic measures how far the observed difference lies from the 0 the null predicts, and the observed difference is the difference of the sample proportions."),

 dict(q="The denominator of the test statistic for a two-sample z-test for proportions is built from",
   choices=[
     "each sample's own proportion",
     "the pooled proportion, applied to both samples",
     "the observed difference",
     "the larger sample only",
     "the significance level"],
   ans=1,
   why="The null asserts a single common proportion, so the standard error the test uses is computed from the pooled estimate of it."),

 dict(q="A study finds 120 successes in 300 for Group 1 and 90 in 300 for Group 2, tested two-sided. The standard error used in the test statistic is closest to",
   choices=["0.0015", "0.0275", "0.0389", "0.0779", "0.3500"],
   ans=2,
   why="Using the pooled proportion 0.35, the standard error is the square root of (0.35)(0.65)(1/300 + 1/300) = 0.0389; 0.0275 uses only one sample and 0.0015 is the variance rather than its square root."),

 dict(q="For that study of 120 of 300 against 90 of 300, the test statistic is closest to",
   choices=["0.100", "1.284", "2.568", "2.582", "5.136"],
   ans=2,
   why="z = (0.40 - 0.30)/0.0389 = 2.568."),

 dict(q="For that study with z = 2.568 and a two-sided alternative, the p-value is closest to",
   choices=["0.0051", "0.0102", "0.0204", "0.9898", "0.9949"],
   ans=1,
   why="The one-tail area beyond 2.568 is 0.0051, and doubling it for the two-sided alternative gives 0.0102."),

 dict(q="For that study with a two-sided p-value of 0.0102, the decision at alpha = 0.05 is to",
   choices=[
     "reject the null hypothesis and conclude there is convincing evidence that the two population proportions differ",
     "fail to reject the null hypothesis",
     "accept the null hypothesis",
     "conclude the difference is exactly 0.10",
     "conclude that Group 2's proportion is larger"],
   ans=0,
   why="0.0102 is below 0.05, and the observed difference is positive, so the evidence points to a genuine difference."),

 dict(q="A second study finds 95 successes in 250 for Group 1 and 70 in 250 for Group 2, tested against Ha: p1 > p2. The pooled proportion and standard error are closest to",
   choices=[
     "0.3300 and 0.0421",
     "0.3300 and 0.0431",
     "0.3000 and 0.0421",
     "0.6600 and 0.0421",
     "0.1000 and 0.0421"],
   ans=0,
   why="The pooled proportion is 165/500 = 0.33 and the standard error is the square root of (0.33)(0.67)(1/250 + 1/250) = 0.0421."),

 dict(q="For that second study, the test statistic is closest to",
   choices=["0.100", "1.189", "2.378", "2.383", "4.756"],
   ans=2,
   why="z = (0.38 - 0.28)/0.0421 = 2.378."),

 dict(q="For that second study with z = 2.378 and Ha: p1 > p2, the p-value is closest to",
   choices=["0.0087", "0.0174", "0.4913", "0.9913", "2.3780"],
   ans=0,
   why="A one-sided alternative uses the single right-tail area beyond 2.378, which is 0.0087."),

 dict(q="For that second study with a p-value of 0.0087, the decision at alpha = 0.01 is to",
   choices=[
     "reject the null hypothesis, since 0.0087 is below 0.01",
     "fail to reject the null hypothesis",
     "accept the null hypothesis",
     "reject the alternative hypothesis",
     "declare the test inconclusive"],
   ans=0,
   why="The p-value falls below even the stricter 1% standard, so the evidence is strong."),

 dict(q="A third study finds 140 successes in 400 for Group 1 and 120 in 400 for Group 2, tested against Ha: p1 > p2. The test statistic is closest to",
   choices=["0.050", "1.510", "1.526", "3.020", "6.040"],
   ans=1,
   why="The pooled proportion is 260/800 = 0.325, the standard error is 0.0331, and z = (0.35 - 0.30)/0.0331 = 1.510."),

 dict(q="For that third study with z = 1.510 and Ha: p1 > p2, the p-value is closest to",
   choices=["0.0328", "0.0656", "0.1311", "0.9344", "1.5100"],
   ans=1,
   why="The right-tail area beyond 1.510 is 0.0656."),

 dict(q="For that third study with a p-value of 0.0656, the decision at alpha = 0.05 is to",
   choices=[
     "reject the null hypothesis",
     "fail to reject the null hypothesis, since 0.0656 exceeds 0.05",
     "accept the null hypothesis as true",
     "conclude that Group 1's proportion is larger",
     "conclude the two proportions are equal"],
   ans=1,
   why="0.0656 is above the 5% standard, so the data do not provide convincing evidence at that level."),

 dict(q="For that same third study with p = 0.0656, the decision at alpha = 0.10 would be to",
   choices=[
     "reject the null hypothesis, since 0.0656 is below 0.10",
     "fail to reject the null hypothesis",
     "accept the null hypothesis",
     "make the same decision as at alpha = 0.05",
     "recompute the test statistic"],
   ans=0,
   why="The same evidence meets a 10% standard while failing a 5% one, which is why the significance level must be fixed in advance."),

 dict(q="A fourth study finds 48 successes in 200 for Group 1 and 36 in 150 for Group 2, tested two-sided. The test statistic is",
   choices=["-1.000", "0.000", "0.240", "1.000", "2.000"],
   ans=1,
   why="Both sample proportions are 0.24, so the observed difference is 0 and the test statistic is 0 regardless of the standard error."),

 dict(q="For that fourth study with a test statistic of exactly 0 and a two-sided alternative, the p-value is",
   choices=["0.0000", "0.2400", "0.5000", "0.9600", "1.0000"],
   ans=4,
   why="A statistic of 0 is the least extreme result possible, so every outcome is at least as extreme and the two-sided p-value is 1."),

 dict(q="A two-sided p-value of exactly 1 means that",
   choices=[
     "an error has been made",
     "the observed data match what the null hypothesis predicts as closely as possible, giving no evidence at all against it",
     "the null hypothesis is certainly true",
     "the two population proportions are equal",
     "the sample sizes were too small"],
   ans=1,
   why="A p-value of 1 says the result is the least surprising one available under the null, which is not the same as proving the null."),

 dict(q="A student uses each sample's own proportion in the denominator of a two-sample TEST statistic instead of the pooled proportion. For the study of 120 of 300 against 90 of 300, this gives a standard error of 0.0387 instead of 0.0389, so the test statistic is",
   choices=[
     "much smaller",
     "slightly larger, since the denominator is slightly smaller",
     "slightly smaller",
     "unchanged",
     "negative"],
   ans=1,
   why="A smaller denominator gives a larger quotient; the numerical effect is tiny here, but the method is wrong because a test computes its standard error under the null."),

 dict(q="Reversing which group is called Group 1 changes the two-sample test statistic by",
   choices=[
     "changing its magnitude",
     "changing its sign but not its magnitude",
     "leaving it entirely unchanged",
     "making it undefined",
     "doubling it"],
   ans=1,
   why="The numerator changes sign while the pooled standard error is unaffected, so a two-sided p-value is unchanged and a one-sided alternative must be relabelled to match."),

 dict(q="For a two-sided two-sample test, reversing which group is called Group 1 changes the p-value by",
   choices=[
     "doubling it",
     "halving it",
     "not changing it at all",
     "making it negative",
     "making it exceed 1"],
   ans=2,
   why="A two-sided p-value depends on the magnitude of the statistic, and reversing the groups changes only its sign."),

 dict(q="A complete conclusion for a two-sample test of proportions must state",
   choices=[
     "the test statistic only",
     "the decision, the comparison of p-value with alpha, and what the evidence says about the two populations in context",
     "the pooled proportion",
     "the two sample sizes",
     "that the null hypothesis is true or false"],
   ans=1,
   why="As in the one-sample case, a conclusion names what was decided, on what evidence, and about which populations and response variable."),

 dict(q="A test comparing a treatment group and a control group, with subjects randomly assigned, gives p = 0.0102. The strongest justified conclusion is that",
   choices=[
     "the treatment is merely associated with the outcome",
     "there is convincing evidence that the treatment caused a difference in the proportion, for subjects like those in the study",
     "the treatment causes the difference for everyone",
     "no conclusion is possible",
     "the two proportions are equal"],
   ans=1,
   why="Random assignment supports the causal claim, while the population it extends to depends on how the subjects were obtained."),

 dict(q="Two studies compare the same two proportions and obtain the same sample proportions, 0.40 and 0.30, but one uses samples of 300 each and the other samples of 1,200 each. The larger study's test statistic will be",
   choices=[
     "the same",
     "twice as large, so its p-value will be smaller",
     "half as large",
     "four times as large",
     "impossible to compare"],
   ans=1,
   why="The pooled standard error carries the square root of the sample sizes, so quadrupling both halves it and doubles the statistic."),

 dict(q="If a two-sample test gives a p-value below alpha, the corresponding confidence interval for the difference at the matching confidence level will generally",
   choices=[
     "contain the value zero",
     "exclude the value zero",
     "be centred at the value zero",
     "have a negative width",
     "be impossible to compute"],
   ans=1,
   why="The two procedures answer the same question from opposite directions, though they agree only generally, since the test pools the standard error and the interval does not."),

 dict(q="Before the test statistic is computed, the conditions must be checked because",
   choices=[
     "the p-value is an area under a normal curve, which is only the right null distribution when the conditions hold",
     "the conditions determine the pooled proportion",
     "the conditions fix the alternative hypothesis",
     "the conditions set the significance level",
     "they need not be checked if both samples exceed 30"],
   ans=0,
   why="If the sampling distribution of the difference is not approximately normal, the area computed from the standard normal curve is not the p-value the test reports."),
]
