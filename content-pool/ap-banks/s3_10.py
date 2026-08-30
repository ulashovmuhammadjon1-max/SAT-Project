# AP STATISTICS 3.10 Constructing a Confidence Interval for the Difference
# Between Two Population Proportions — 25 questions
# CED: Fall 2026, Unit 3. Learning objectives on identifying the procedure
# (skill 2.C), verifying conditions (4.E) and calculating the interval (3.E).
#
# The procedure is the TWO-SAMPLE z-INTERVAL FOR A DIFFERENCE OF PROPORTIONS:
#     (p-hat1 - p-hat2)  plus or minus  z* times
#         sqrt( p-hat1(1 - p-hat1)/n1  +  p-hat2(1 - p-hat2)/n2 )
#
# THE DISTINCTION THAT MATTERS MOST, and the reason this topic and 3.13 must be
# learned together rather than blurred: this interval uses the SEPARATE, or
# unpooled, standard error, computed from each sample's own proportion. The
# two-proportion TEST of topic 3.13 pools the two samples into a single combined
# proportion first. The reason is the same one that governed p0 in topic 3.5 --
# a test assumes the null hypothesis, and the null there says the two population
# proportions are EQUAL, so a single pooled estimate is the right one to use.
# An interval assumes nothing, so it must keep the samples apart.
#
# Note for anyone extending this module: the pooled and unpooled standard errors
# are NUMERICALLY very close -- 0.0387 against 0.0389 on the data below -- so the
# pooled value makes a poor multiple-choice distractor, since the two round to
# nearly the same figure and a student who used the wrong one would still land
# on the keyed choice. That is precisely why the distinction is tested
# CONCEPTUALLY here, in q3 and q4, rather than numerically.
#
# The second idea is what an interval containing 0 means: 0 is the value "no
# difference", so an interval that contains it leaves "the two proportions are
# equal" plausible. Three items use that, including one interval built to
# contain 0 so the contrast is real rather than described.
#
# Worked values, all recomputed in verify_s3_10.py:
#   120/300 vs 90/300 at 95%: diff 0.10, SE 0.03873, CI (0.0241, 0.1759)
#   168/240 vs 144/240 at 90%: diff 0.10, SE 0.04330, CI (0.0288, 0.1712)
#    90/200 vs 70/200 at 99%: diff 0.10, SE 0.04873, CI (-0.0255, 0.2255)
TOPIC = ("3.10", "Constructing a Confidence Interval for the Difference Between Two Population Proportions", 3)

QUESTIONS = [
 dict(q="The appropriate procedure for estimating the difference between two population proportions is",
   choices=[
     "a two-sample z-interval for a difference of proportions",
     "a one-sample z-interval for a population proportion",
     "a two-sample z-test for a difference of proportions",
     "a chi-square test for homogeneity",
     "a one-sample z-test"],
   ans=0,
   why="Two proportions estimated with an interval calls for the two-sample z-interval; a test answers a different question."),

 dict(q="The point estimate at the centre of a two-sample z-interval for a difference of proportions is",
   choices=[
     "the difference between the two sample proportions",
     "the sum of the two sample proportions",
     "the pooled proportion of both samples combined",
     "the larger of the two sample proportions",
     "the difference between the two sample sizes"],
   ans=0,
   why="An interval is built around the statistic that estimates the parameter, and the difference of the sample proportions estimates the difference of the population proportions."),

 dict(q="The standard error used in a two-sample z-interval for a difference of proportions is computed from",
   choices=[
     "a single pooled proportion combining both samples",
     "each sample's own proportion, with the two variances added",
     "the difference between the two sample proportions",
     "the larger sample only",
     "the null hypothesized value"],
   ans=1,
   why="An interval assumes nothing about whether the proportions are equal, so each sample contributes its own variance and the two are summed."),

 dict(q="Why does the two-sample INTERVAL use separate proportions while the two-sample TEST pools them?",
   choices=[
     "Because the test assumes under its null hypothesis that the two population proportions are equal, which justifies a single combined estimate; an interval assumes no such thing",
     "Because pooling is always more accurate",
     "Because the interval requires larger samples",
     "Because the test uses a different confidence level",
     "There is no real difference between them"],
   ans=0,
   why="The same logic that put p0 in the denominator of a one-sample test statistic puts the pooled proportion in the two-sample one: a test computes everything under its null."),

 dict(q="In a study, 120 of 300 people in Group 1 and 90 of 300 in Group 2 responded favourably. The difference between the sample proportions, Group 1 minus Group 2, is",
   choices=["0.0300", "0.0700", "0.1000", "0.3000", "0.7000"],
   ans=2,
   why="The two sample proportions are 0.40 and 0.30, and their difference is 0.10."),

 dict(q="For those samples of 120 of 300 and 90 of 300, the standard error of the difference is closest to",
   choices=["0.0015", "0.0283", "0.0387", "0.0548", "0.0775"],
   ans=2,
   why="The square root of (0.4)(0.6)/300 + (0.3)(0.7)/300 is 0.0387; 0.0283 uses only the first sample and 0.0015 is the variance rather than its square root."),

 dict(q="For those samples of 120 of 300 and 90 of 300, the 95% confidence interval for the difference in population proportions is closest to",
   choices=[
     "(0.0241, 0.1759)",
     "(0.0613, 0.1387)",
     "(-0.0241, 0.1759)",
     "(0.0000, 0.1000)",
     "(0.1000, 0.1759)"],
   ans=0,
   why="The margin of error is 1.96 times 0.0387 = 0.0759, so the interval is 0.10 plus or minus 0.0759."),

 dict(q="Since that 95% interval (0.0241, 0.1759) does not contain 0, the appropriate conclusion is that",
   choices=[
     "there is convincing evidence of a difference between the two population proportions, with Group 1's higher",
     "the two population proportions are equal",
     "no conclusion is possible",
     "Group 2's proportion is higher",
     "the difference is exactly 0.10"],
   ans=0,
   why="Zero is the value 'no difference', and the interval rules it out, with every plausible value positive so Group 1's proportion is the larger."),

 dict(q="In a second study, 168 of 240 in Group 1 and 144 of 240 in Group 2 responded favourably. The standard error of the difference is closest to",
   choices=["0.0019", "0.0433", "0.0442", "0.0712", "0.1000"],
   ans=1,
   why="The square root of (0.7)(0.3)/240 + (0.6)(0.4)/240 is 0.0433."),

 dict(q="For those samples of 168 of 240 and 144 of 240, the 90% confidence interval for the difference is closest to",
   choices=[
     "(0.0288, 0.1712)",
     "(0.0151, 0.1849)",
     "(-0.0288, 0.1712)",
     "(0.0567, 0.1433)",
     "(0.1000, 0.1712)"],
   ans=0,
   why="The margin of error is 1.645 times 0.0433 = 0.0712, so the interval is 0.10 plus or minus 0.0712."),

 dict(q="In a third study, 90 of 200 in Group 1 and 70 of 200 in Group 2 responded favourably. The standard error of the difference is closest to",
   choices=["0.0024", "0.0487", "0.0497", "0.1000", "0.1255"],
   ans=1,
   why="The square root of (0.45)(0.55)/200 + (0.35)(0.65)/200 is 0.0487."),

 dict(q="For those samples of 90 of 200 and 70 of 200, the 99% confidence interval for the difference is closest to",
   choices=[
     "(-0.0255, 0.2255)",
     "(0.0045, 0.1955)",
     "(0.0255, 0.2255)",
     "(0.0513, 0.1487)",
     "(-0.1255, 0.1255)"],
   ans=0,
   why="The margin of error is 2.576 times 0.0487 = 0.1255, so the interval is 0.10 plus or minus 0.1255 and runs from -0.0255 to 0.2255."),

 dict(q="Since that 99% interval (-0.0255, 0.2255) DOES contain 0, the appropriate conclusion is that",
   choices=[
     "there is convincing evidence of a difference",
     "there is not convincing evidence of a difference between the two population proportions, since 'no difference' remains a plausible value",
     "the two proportions are proved equal",
     "Group 2's proportion is higher",
     "the study should be discarded"],
   ans=1,
   why="An interval containing 0 leaves equality plausible; that is not the same as establishing that the two proportions are equal."),

 dict(q="An interval for a difference of proportions that contains 0 means that",
   choices=[
     "the two sample proportions were equal",
     "the value 'no difference' is among the plausible values for the difference in population proportions",
     "one of the samples was too small",
     "the calculation is wrong",
     "the difference must be exactly 0"],
   ans=1,
   why="Zero is a value of the parameter like any other; an interval containing it says only that it has not been ruled out."),

 dict(q="An interval for a difference of proportions that lies entirely BELOW 0 means that",
   choices=[
     "the first population proportion is plausibly larger",
     "the second population proportion is larger, since every plausible value of p1 minus p2 is negative",
     "the two proportions are equal",
     "the interval was computed incorrectly",
     "no conclusion can be drawn"],
   ans=1,
   why="A wholly negative interval for p1 minus p2 rules out equality and places every plausible value on the side where p2 exceeds p1."),

 dict(q="The conditions for a two-sample z-interval for a difference of proportions include",
   choices=[
     "both samples random and independent of each other, and at least 10 observed successes and 10 observed failures in EACH sample",
     "equal sample sizes",
     "both populations normally distributed",
     "at least 30 observations in total",
     "equal population proportions"],
   ans=0,
   why="The counts are checked in each sample separately, giving four counts, and the two samples must be independent for the variances to be added."),

 dict(q="For an INTERVAL for a difference of proportions, the normality condition uses",
   choices=[
     "the counts expected under a null hypothesis",
     "the observed numbers of successes and failures in each sample",
     "the pooled proportion",
     "the sample sizes only",
     "the confidence level"],
   ans=1,
   why="An interval has no hypothesized value to compute expected counts from, so the observed counts are used, exactly as in the one-sample interval of topic 3.3."),

 dict(q="Two independent samples of 300 each give 120 and 90 successes. Checking the conditions for an interval, the four counts are",
   choices=[
     "120, 180, 90, and 210, all at least 10",
     "120 and 90 only",
     "0.40 and 0.30",
     "300 and 300",
     "210 and 390"],
   ans=0,
   why="Each sample contributes its observed successes and its observed failures: 120 and 300 - 120 = 180, then 90 and 300 - 90 = 210."),

 dict(q="Holding everything else fixed, raising the confidence level for a difference of proportions makes the interval",
   choices=["narrower", "wider", "unchanged", "centred elsewhere", "impossible to compute"],
   ans=1,
   why="A larger critical value multiplies an unchanged standard error, so the margin of error and the width both grow."),

 dict(q="Holding the confidence level fixed, increasing BOTH sample sizes makes the interval",
   choices=["wider", "narrower", "unchanged", "centred elsewhere", "contain 0 automatically"],
   ans=1,
   why="Each variance carries its own sample size in the denominator, so raising both shrinks the standard error and narrows the interval."),

 dict(q="A 95% confidence interval for p1 minus p2 is (0.02, 0.18). The point estimate and margin of error are",
   choices=[
     "0.10 and 0.08",
     "0.10 and 0.16",
     "0.02 and 0.18",
     "0.08 and 0.10",
     "0.20 and 0.08"],
   ans=0,
   why="The centre is (0.02 + 0.18)/2 = 0.10 and the margin of error is half the width, (0.18 - 0.02)/2 = 0.08."),

 dict(q="A researcher reverses the order of subtraction, computing p-hat2 minus p-hat1 instead. The resulting interval is",
   choices=[
     "the same interval",
     "the original interval with both endpoints negated and the order swapped, carrying the same conclusion",
     "wider",
     "narrower",
     "no longer valid"],
   ans=1,
   why="The standard error is unaffected by the order, so an interval of (0.02, 0.18) becomes (-0.18, -0.02), which excludes 0 exactly as before."),

 dict(q="Interpreted in context, a 95% confidence interval of (0.0241, 0.1759) for the difference between two population proportions means that",
   choices=[
     "95% of the difference lies between those values",
     "we are 95% confident that the interval from 0.0241 to 0.1759 contains the true difference between the two population proportions",
     "there is a 95% probability the true difference is 0.10",
     "95% of individuals differ by that amount",
     "the two proportions differ by between 2% and 18% of the sample"],
   ans=1,
   why="The interpretation names the confidence level, the interval, and the parameter, which here is the difference between the two population proportions."),

 dict(q="A study compares the same group of people before and after an intervention and builds a two-sample z-interval for the difference in proportions. The flaw is that",
   choices=[
     "the two samples are not independent, since the same individuals appear in both, so the variances may not simply be added",
     "the sample size is too small",
     "the confidence level is wrong",
     "proportions cannot be compared before and after",
     "there is no flaw"],
   ans=0,
   why="Independence between the two samples is what licenses adding the variances, and repeated measurements on the same people violate it."),

 dict(q="Which change would be most likely to turn an interval that contains 0 into one that does not, assuming a real difference exists?",
   choices=[
     "raising the confidence level",
     "increasing both sample sizes",
     "reducing both sample sizes",
     "reversing the order of subtraction",
     "pooling the two samples"],
   ans=1,
   why="Larger samples narrow the interval around a centre that is not 0, which is what eventually excludes 0; a higher confidence level would widen it instead."),
]
