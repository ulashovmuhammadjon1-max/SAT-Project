# AP STATISTICS 3.3 Constructing a Confidence Interval for a Population
# Proportion — 25 questions
# CED: Fall 2026, Unit 3. Learning objectives 3.3.A (identify the procedure and
# state the parameter in context), 3.3.B (verify the conditions), 3.3.C
# (calculate the interval) and 3.3.D (standard error, margin of error, and
# estimating a required sample size).
#
# The procedure is the ONE-SAMPLE z-INTERVAL FOR A POPULATION PROPORTION, and
# the interval is
#     p-hat  plus or minus  z* times sqrt(p-hat(1 - p-hat)/n).
#
# One detail separates this topic from 3.2 and is worth stating plainly, because
# it is the kind of thing a student never notices until it is pointed out: in
# 3.2 the normality condition used the EXPECTED counts np and n(1-p), because
# there p was known. Here p is exactly what is unknown, so EK 3.3.B.1.iii uses
# the OBSERVED counts -- the number of successes and failures actually seen.
# Two items turn on that.
#
# Worked values used below, all recomputed in verify_s3_3.py:
#   p-hat 0.35, n 400, 95%: SE 0.02385, ME 0.04674, CI (0.3033, 0.3967)
#   p-hat 0.60, n 500, 90%: SE 0.02191, ME 0.03604, CI (0.5640, 0.6360)
#   p-hat 0.64, n 250, 99%: SE 0.03036, ME 0.07820, CI (0.5618, 0.7182)
#   critical values z*: 1.645 at 90%, 1.960 at 95%, 2.576 at 99%
TOPIC = ("3.3", "Constructing a Confidence Interval for a Population Proportion", 3)

QUESTIONS = [
 dict(q="The appropriate procedure for estimating a single population proportion with an interval is",
   choices=[
     "a one-sample z-interval for a population proportion",
     "a one-sample t-interval for a population mean",
     "a two-sample z-interval for a difference of proportions",
     "a chi-square test for independence",
     "a one-sample z-test for a population proportion"],
   ans=0,
   why="A single proportion estimated with an interval calls for the one-sample z-interval; a test answers a different question from an interval."),

 dict(q="A confidence interval for a population proportion is best described as",
   choices=[
     "an interval estimate for the population parameter",
     "the range of the sample data",
     "an interval containing 95% of the sample values",
     "the set of all possible sample proportions",
     "a single best guess for the parameter"],
   ans=0,
   why="A confidence interval estimates a parameter with a range of plausible values rather than a single number."),

 dict(q="Which of the following is NOT one of the three conditions for a one-sample z-interval for a population proportion?",
   choices=[
     "The data were collected using a random sample",
     "When sampling without replacement, the population is at least ten times the sample size",
     "The observed numbers of successes and failures are each at least 10",
     "The population distribution is normal",
     "All three of the other conditions are required"],
   ans=3,
   why="Nothing is assumed about the shape of the population; the normality condition here concerns the SAMPLING distribution and is secured by the observed counts."),

 dict(q="For a confidence interval for a population proportion, the normality condition is checked using",
   choices=[
     "np and n(1 - p), the expected counts from a known p",
     "the observed number of successes and the observed number of failures, each at least 10",
     "the sample size alone, which must be at least 30",
     "the population size",
     "the confidence level"],
   ans=1,
   why="When constructing an interval the population proportion is unknown, so the check uses the counts actually observed rather than expected counts computed from p."),

 dict(q="A survey of 400 randomly selected adults found 140 who exercise daily. Checking the normality condition for a confidence interval gives",
   choices=[
     "140 successes and 260 failures, both at least 10, so the condition is met",
     "140 successes only, so the condition is not met",
     "0.35 successes, which is less than 10",
     "400 successes, so the condition is met",
     "the condition cannot be checked without the population size"],
   ans=0,
   why="The observed counts are 140 and 400 - 140 = 260, and both are far above 10."),

 dict(q="For a survey of 400 adults of whom 140 exercise daily, the sample proportion is",
   choices=["0.140", "0.260", "0.350", "0.400", "0.650"],
   ans=2,
   why="140 divided by 400 is 0.35; 0.65 is the proportion who do not exercise daily."),

 dict(q="For a sample proportion of 0.35 based on n = 400, the standard error is closest to",
   choices=["0.0006", "0.0238", "0.0467", "0.2275", "0.4770"],
   ans=1,
   why="The standard error is the square root of (0.35)(0.65)/400, which is about 0.0238; 0.0467 is the margin of error at 95% confidence."),

 dict(q="The critical value z* for a 95% confidence interval is closest to",
   choices=["1.282", "1.645", "1.960", "2.326", "2.576"],
   ans=2,
   why="A 95% interval leaves 2.5% in each tail, and the standard normal value cutting off the upper 2.5% is 1.960."),

 dict(q="The critical value z* for a 90% confidence interval is closest to",
   choices=["1.282", "1.645", "1.960", "2.326", "2.576"],
   ans=1,
   why="A 90% interval leaves 5% in each tail, and 1.645 cuts off the upper 5%."),

 dict(q="The critical value z* for a 99% confidence interval is closest to",
   choices=["1.645", "1.960", "2.326", "2.576", "3.090"],
   ans=3,
   why="A 99% interval leaves 0.5% in each tail, and 2.576 cuts off the upper 0.5%."),

 dict(q="For a sample proportion of 0.35 based on n = 400, the margin of error for a 95% confidence interval is closest to",
   choices=["0.0238", "0.0392", "0.0467", "0.0614", "0.0935"],
   ans=2,
   why="The margin of error is z* times the standard error, 1.960 times 0.0238, which is about 0.0467; 0.0935 is the full width of the interval."),

 dict(q="For a sample proportion of 0.35 based on n = 400, the 95% confidence interval is closest to",
   choices=[
     "(0.3262, 0.3738)",
     "(0.3033, 0.3967)",
     "(0.2565, 0.4435)",
     "(0.3500, 0.3967)",
     "(0.3033, 0.3500)"],
   ans=1,
   why="The interval is 0.35 plus or minus 0.0467, which runs from 0.3033 to 0.3967."),

 dict(q="A random sample of 500 voters found 300 in favour of a measure. The sample proportion is 0.60. The standard error is closest to",
   choices=["0.0005", "0.0219", "0.0360", "0.2400", "0.4899"],
   ans=1,
   why="The square root of (0.60)(0.40)/500 is about 0.0219; 0.0360 is the margin of error at 90% confidence."),

 dict(q="For a sample proportion of 0.60 based on n = 500, the 90% confidence interval is closest to",
   choices=[
     "(0.5781, 0.6219)",
     "(0.5640, 0.6360)",
     "(0.5571, 0.6429)",
     "(0.5136, 0.6864)",
     "(0.6000, 0.6360)"],
   ans=1,
   why="The margin of error is 1.645 times 0.0219, which is 0.0360, so the interval runs from 0.5640 to 0.6360."),

 dict(q="A random sample of 250 items contained 160 of a certain type. The sample proportion is 0.64. The 99% confidence interval is closest to",
   choices=[
     "(0.6096, 0.6704)",
     "(0.5905, 0.6895)",
     "(0.5618, 0.7182)",
     "(0.5794, 0.7006)",
     "(0.4800, 0.8000)"],
   ans=2,
   why="The standard error is 0.0304, and the margin of error is 2.576 times 0.0304 = 0.0782, so the interval runs from 0.5618 to 0.7182."),

 dict(q="The standard error of a sample proportion is best interpreted as",
   choices=[
     "an estimate of the typical amount by which a sample proportion varies from the population proportion",
     "the largest possible error in the estimate",
     "the width of the confidence interval",
     "the probability that the interval is wrong",
     "the difference between the sample and population sizes"],
   ans=0,
   why="The standard error estimates the standard deviation of the sampling distribution, which is a typical distance between the statistic and the parameter."),

 dict(q="The margin of error of a confidence interval for a proportion equals",
   choices=[
     "the standard error alone",
     "the critical value times the standard error",
     "the critical value divided by the standard error",
     "half the standard error",
     "the full width of the interval"],
   ans=1,
   why="The margin of error is z* times the standard error, and it is HALF the width of the interval, not the whole width."),

 dict(q="Holding everything else fixed, raising the confidence level from 90% to 99% makes the interval",
   choices=[
     "narrower, because more confidence means more precision",
     "wider, because a larger critical value is required",
     "unchanged",
     "narrower, because the standard error falls",
     "impossible to construct"],
   ans=1,
   why="Greater confidence needs a wider net: z* rises from 1.645 to 2.576 while the standard error is untouched, so the interval widens."),

 dict(q="Holding the confidence level and the sample proportion fixed, increasing the sample size makes the interval",
   choices=[
     "wider",
     "narrower, because the standard error falls as n grows",
     "unchanged",
     "narrower, because the critical value falls",
     "wider, because the critical value rises"],
   ans=1,
   why="The critical value depends only on the confidence level; it is the standard error, with n under a square root, that shrinks."),

 dict(q="To halve the margin of error of a confidence interval for a proportion, holding the confidence level and p-hat fixed, the sample size must be multiplied by",
   choices=["2", "4", "8", "16", "1/2"],
   ans=1,
   why="The margin of error is proportional to 1 over the square root of n, so four times the sample size halves it."),

 dict(q="A pollster wants a 95% confidence interval for a population proportion with a margin of error of at most 0.03, and uses the conservative value p* = 0.5. The required sample size is closest to",
   choices=["544", "752", "1068", "1503", "2135"],
   ans=2,
   why="Setting 1.960 times sqrt(0.25/n) equal to 0.03 gives n = 1067.07, and the sample size is rounded UP to 1,068 so the margin of error does not exceed 0.03."),

 dict(q="Why is p* = 0.5 used when planning a sample size and no prior estimate is available?",
   choices=[
     "Because it is the smallest possible value of p",
     "Because p(1 - p) is largest at 0.5, so it gives the most conservative, largest required sample size",
     "Because most population proportions are near 0.5",
     "Because it makes the arithmetic simpler",
     "Because it minimizes the required sample size"],
   ans=1,
   why="Using the value that maximizes p(1-p) guarantees the achieved margin of error is no larger than intended, whatever p turns out to be."),

 dict(q="A required sample size calculation produces n = 546.2. The sample size that should be used is",
   choices=["546", "546.2", "547", "550", "500"],
   ans=2,
   why="Rounding down would leave the margin of error slightly larger than required, so a sample size calculation is always rounded UP."),

 dict(q="Stated in context, the parameter estimated by a confidence interval built from a random sample of 400 adults in a city, 140 of whom exercise daily, is",
   choices=[
     "the proportion of the 400 sampled adults who exercise daily",
     "the proportion of all adults in that city who exercise daily",
     "the number of adults in the city who exercise daily",
     "the mean number of exercise sessions per adult",
     "the sample proportion 0.35"],
   ans=1,
   why="A parameter describes the population the sample was drawn from, and it must name the proportion, the response variable and the population."),

 dict(q="Two 95% confidence intervals for the same population proportion are built from independent samples of sizes 200 and 800. Compared with the smaller sample's interval, the larger sample's interval will be about",
   choices=[
     "the same width",
     "half as wide",
     "a quarter as wide",
     "twice as wide",
     "four times as wide"],
   ans=1,
   why="Quadrupling n divides the standard error, and hence the margin of error, by the square root of 4, which is 2."),
]
