# AP STATISTICS 3.11 Justifying a Claim Based on a Confidence Interval for the
# Difference Between Two Population Proportions — 25 questions
# CED: Fall 2026, Unit 3. Skill 4.F (interpret the results of an inference
# method) and 4.G (justify a claim based on them).
#
# Topic 3.4 did this for ONE proportion. Everything there still applies, and one
# thing is added that has no counterpart in the one-sample case: the value 0 is
# now special. It is the value "the two population proportions are equal", so
# whether the interval contains 0 settles whether a difference has been
# established, and the SIGN of an interval that excludes 0 settles which
# proportion is larger.
#
# Three verdicts, and the module gives each its own interval so the contrast is
# arithmetic rather than described:
#     entirely above 0  ->  convincing evidence that p1 exceeds p2
#     containing 0      ->  no convincing evidence of any difference
#     entirely below 0  ->  convincing evidence that p2 exceeds p1
#
# The error this topic exists to prevent: reading an interval that contains 0 as
# evidence that the two proportions are EQUAL. Failing to rule out equality is
# not the same as establishing it -- the same asymmetry as "fail to reject"
# against "accept" in topic 3.7 -- and three items separate the two readings.
#
# Intervals used, all checked in verify_s3_11.py:
#   A  (0.03, 0.15)    excludes 0, positive
#   B  (-0.08, 0.02)   contains 0
#   C  (-0.20, -0.05)  excludes 0, negative
TOPIC = ("3.11", "Justifying a Claim Based on a Confidence Interval for the Difference Between Two Population Proportions", 3)

QUESTIONS = [
 dict(q="In a confidence interval for the difference between two population proportions, the value 0 is important because it represents",
   choices=[
     "a proportion of zero in the first population",
     "the case in which the two population proportions are equal",
     "the smallest possible sample proportion",
     "the confidence level",
     "an impossible value"],
   ans=1,
   why="The parameter is p1 minus p2, so 0 is exactly the statement that the two population proportions are the same."),

 dict(q="A 95% confidence interval for p1 minus p2 is (0.03, 0.15). The appropriate conclusion is that",
   choices=[
     "there is convincing evidence that the first population proportion is larger than the second",
     "there is convincing evidence that the second is larger",
     "the two proportions are equal",
     "no conclusion can be drawn",
     "the difference is exactly 0.09"],
   ans=0,
   why="Every plausible value of p1 minus p2 is positive, so 0 is ruled out and the first proportion is the larger."),

 dict(q="A 95% confidence interval for p1 minus p2 is (-0.08, 0.02). The appropriate conclusion is that",
   choices=[
     "there is convincing evidence that the second proportion is larger",
     "there is not convincing evidence of a difference between the two population proportions",
     "the two population proportions are proved equal",
     "there is convincing evidence that the first proportion is larger",
     "the interval was computed incorrectly"],
   ans=1,
   why="The interval contains 0, so 'no difference' remains among the plausible values and no difference has been established in either direction."),

 dict(q="A 95% confidence interval for p1 minus p2 is (-0.20, -0.05). The appropriate conclusion is that",
   choices=[
     "there is convincing evidence that the first population proportion is larger",
     "there is convincing evidence that the second population proportion is larger",
     "the two proportions are equal",
     "no conclusion can be drawn from a negative interval",
     "the interval must be recomputed with the groups reversed"],
   ans=1,
   why="Every plausible value of p1 minus p2 is negative, which means p2 exceeds p1 throughout the interval."),

 dict(q="A researcher obtains the interval (-0.08, 0.02) and writes, 'This proves the two population proportions are equal.' The error is that",
   choices=[
     "failing to rule out equality is not the same as establishing it; the interval also leaves values such as -0.06 and 0.01 plausible",
     "the interval should have been positive",
     "the confidence level was too low",
     "equality can never be discussed",
     "there is no error"],
   ans=0,
   why="An interval containing 0 contains many other values too, and it merely fails to distinguish among them; it is the same asymmetry as 'fail to reject' against 'accept'."),

 dict(q="A complete interpretation of a 95% confidence interval of (0.03, 0.15) for a difference in proportions states that",
   choices=[
     "95% of the differences lie between 0.03 and 0.15",
     "we are 95% confident that the interval from 0.03 to 0.15 captures the true difference between the two population proportions, described in context",
     "there is a 95% probability the difference is 0.09",
     "95% of individuals differ by between 3% and 15%",
     "the difference is significant"],
   ans=1,
   why="As in topic 3.4, the interpretation names the confidence level, the interval and the parameter, and here the parameter is a DIFFERENCE between two populations."),

 dict(q="Two independent studies each produce a 95% interval for the same difference: Study 1 gives (0.01, 0.19) and Study 2 gives (0.06, 0.14). Both exclude 0. The better-designed study is most likely",
   choices=[
     "Study 1, because its interval is wider",
     "Study 2, because a narrower interval at the same confidence level indicates larger samples and a more precise estimate",
     "Study 1, because it contains more values",
     "neither; the two are equivalent",
     "impossible to compare"],
   ans=1,
   why="At the same confidence level, width reflects the standard error, and a smaller standard error comes from larger samples."),

 dict(q="A 95% interval for p1 minus p2 is (0.03, 0.15). If the same data were used to build a 99% interval, the new interval would",
   choices=[
     "be narrower and might contain 0",
     "be wider and might contain 0",
     "be identical",
     "be narrower and certainly exclude 0",
     "have a different centre"],
   ans=1,
   why="Higher confidence needs a larger critical value, so the interval widens around the same centre and can extend past 0."),

 dict(q="A 90% interval for p1 minus p2 excludes 0. The corresponding 99% interval from the same data",
   choices=[
     "must also exclude 0",
     "may contain 0, since it is wider",
     "must contain 0",
     "must be narrower",
     "must have a different centre"],
   ans=1,
   why="Widening an interval can only add values, and 0 may be among them, so exclusion at one level does not guarantee it at a higher one."),

 dict(q="A 95% interval for p1 minus p2 is (0.03, 0.15). Interpreted in context for a study comparing the proportion of adults and the proportion of teenagers who own a library card, the interval says that",
   choices=[
     "between 3% and 15% of all people own a library card",
     "the proportion of adults with a card plausibly exceeds the proportion of teenagers with one by between 0.03 and 0.15",
     "3% to 15% of adults are teenagers",
     "adults are between 3 and 15 times more likely to own a card",
     "the two proportions differ by exactly 0.09"],
   ans=1,
   why="The parameter is a difference of two proportions, so the interval bounds how much one exceeds the other, not a proportion itself and not a ratio."),

 dict(q="A researcher reverses the two groups and recomputes the interval, obtaining (-0.15, -0.03) instead of (0.03, 0.15). The conclusion about which proportion is larger",
   choices=[
     "reverses as well",
     "is unchanged; the same group still has the larger proportion, since the parameter being estimated has been redefined in the opposite order",
     "becomes impossible to state",
     "now shows no difference",
     "depends on the confidence level"],
   ans=1,
   why="Negating both endpoints reflects the interval about 0 and redefines which group is subtracted from which; the underlying finding is identical."),

 dict(q="A 95% interval for p1 minus p2 is (-0.02, 0.30). A colleague says 'the evidence strongly favours group 1'. The most accurate response is that",
   choices=[
     "the interval contains 0, so a difference has not been established, even though most of the plausible values are positive",
     "the colleague is right, because most of the interval is positive",
     "the colleague is right, because the upper endpoint is large",
     "the interval shows group 2 is larger",
     "the interval is invalid"],
   ans=0,
   why="Containing 0 is what decides the question at the stated confidence level; how much of the interval lies on one side is not the criterion."),

 dict(q="Which of the following intervals for p1 minus p2 provides convincing evidence of a difference at the stated confidence level?",
   choices=[
     "(-0.05, 0.12)",
     "(-0.11, 0.00)",
     "(0.00, 0.14)",
     "(0.02, 0.19)",
     "(-0.09, 0.09)"],
   ans=3,
   why="Only this interval excludes 0 entirely; the two intervals with 0 as an endpoint do not rule it out, and the others straddle it."),

 dict(q="A study finds a 95% interval for p1 minus p2 of (0.04, 0.10) but the two groups were formed by letting participants choose which group to join. The strongest justified claim is that",
   choices=[
     "the treatment causes the difference",
     "there is convincing evidence of a difference in proportions between the two groups, but with no random assignment the difference cannot be attributed to the grouping variable",
     "no difference exists",
     "the interval is invalid",
     "the difference is exactly 0.07"],
   ans=1,
   why="An interval establishes association between the grouping and the response; causation requires random assignment, exactly as in topic 1.13."),

 dict(q="A 95% interval for p1 minus p2 is (0.04, 0.10), computed from random samples of two populations. The conclusion may be generalized to",
   choices=[
     "only the individuals in the two samples",
     "the two populations the samples were randomly drawn from",
     "all populations everywhere",
     "no population at all",
     "only populations of the same size"],
   ans=1,
   why="Random selection licenses generalizing to the sampled populations, which is topic 1.11's rule applied to a two-sample setting."),

 dict(q="An interval for p1 minus p2 whose endpoints are both negative tells you that",
   choices=[
     "the sample proportions were both negative",
     "the second population proportion is plausibly larger than the first throughout the interval",
     "an error was made, since proportions cannot be negative",
     "the difference is 0",
     "the first proportion is larger"],
   ans=1,
   why="Proportions are never negative, but their DIFFERENCE can be, and a negative difference means the subtracted proportion is the larger one."),

 dict(q="Increasing both sample sizes while the true difference stays the same will tend to make the interval",
   choices=[
     "wider, and more likely to contain 0",
     "narrower, and if a real difference exists, more likely to exclude 0",
     "unchanged",
     "centred at 0",
     "impossible to compute"],
   ans=1,
   why="Larger samples shrink the standard error, so the interval closes in on the true difference, and if that difference is not 0 the interval eventually excludes 0."),

 dict(q="A 99% interval for p1 minus p2 is (-0.01, 0.13) and a 90% interval from the same data is (0.01, 0.11). These two intervals",
   choices=[
     "contradict each other",
     "are consistent: the same data can fail to establish a difference at 99% confidence while establishing one at 90% confidence, because the required standard of evidence differs",
     "cannot both be computed",
     "must have different centres",
     "show that the data are unreliable"],
   ans=1,
   why="A higher confidence level demands a wider interval, so it is harder to exclude 0; the evidence has not changed, only the standard applied to it."),

 dict(q="For a difference of proportions, an interval of (0.00, 0.14) should be read as",
   choices=[
     "excluding 0 and establishing a difference",
     "including 0 as an endpoint, so 'no difference' is not ruled out",
     "invalid, since 0 cannot be an endpoint",
     "showing the second proportion is larger",
     "identical to (0.01, 0.14)"],
   ans=1,
   why="An endpoint is a plausible value like any other, so 0 remains within the set the interval does not rule out."),

 dict(q="The width of a confidence interval for a difference of proportions is determined by",
   choices=[
     "the difference between the two sample proportions",
     "the critical value and the standard error, which depends on both sample sizes and both sample proportions",
     "the two population sizes",
     "the value 0",
     "the number of groups"],
   ans=1,
   why="The centre carries the estimate and the width carries the precision; the two are determined by different quantities."),

 dict(q="Two 95% intervals for the same difference are computed from samples of 100 each and from samples of 900 each. The interval from the larger samples will be about",
   choices=[
     "the same width",
     "one third as wide",
     "one ninth as wide",
     "three times as wide",
     "nine times as wide"],
   ans=1,
   why="The standard error carries the square root of the sample size, so nine times the data gives three times the precision."),

 dict(q="A newspaper reports 'the two groups differ by 8 percentage points' from a study whose 95% interval for the difference was (-0.03, 0.19). The reporting is misleading because",
   choices=[
     "8 percentage points is the point estimate, but the interval shows that no difference at all remains plausible",
     "the two numbers do not match",
     "percentage points cannot be reported",
     "the interval is too narrow",
     "the report should have used the upper endpoint"],
   ans=0,
   why="Reporting a point estimate without the interval hides that the data do not establish any difference; the centre of (-0.03, 0.19) is indeed 0.08."),

 dict(q="A 95% interval for the difference in proportions between a treatment group and a control group, with subjects RANDOMLY ASSIGNED, is (0.05, 0.21). The strongest justified conclusion is that",
   choices=[
     "the treatment is associated with a higher proportion, but causation cannot be claimed",
     "the treatment causes a higher proportion among subjects like those studied, since the assignment was random",
     "no difference exists",
     "the result generalizes to everyone",
     "the interval is too wide to interpret"],
   ans=1,
   why="Random assignment licenses the causal claim, while the scope of the population depends separately on how the subjects were obtained."),

 dict(q="Which pair of facts together justify the strongest possible conclusion from a two-proportion study?",
   choices=[
     "a large sample and a narrow interval",
     "random selection from the populations of interest and random assignment of the treatments",
     "a high confidence level and a small p-value",
     "equal sample sizes and equal proportions",
     "an interval that contains 0"],
   ans=1,
   why="Random selection carries the conclusion to the populations and random assignment carries it to causation; together they support a causal claim about those populations."),

 dict(q="A confidence interval for a difference of proportions supports a claim about the difference when",
   choices=[
     "the claimed value lies inside the interval, making it plausible, or lies outside it, making it implausible",
     "the interval is narrow",
     "the confidence level exceeds 95%",
     "both sample proportions exceed 0.5",
     "the sample sizes are equal"],
   ans=0,
   why="Judging a claim against an interval is the same operation whatever the parameter: inside means plausible and outside means the data argue against it."),
]
