# AP STATISTICS 3.2 Sampling Distributions for Sample Proportions — 25 questions
# CED: Fall 2026, Unit 3. Learning objectives 3.2.A (calculate the mean and
# standard deviation of the sampling distribution of a sample proportion),
# 3.2.B (justify the conditions) and 3.2.C (interpret them in context).
#
# The three facts, from EK 3.2.A.1 and 3.2.B:
#   mean of p-hat = p
#   standard deviation of p-hat = sqrt(p(1 - p) / n)
#   the sampling distribution is approximately normal when the conditions hold.
#
# The CED names three conditions and this module tests each separately, because
# students learn them as one blurred rule:
#   RANDOMIZATION  the data come from a random sample (EK 3.2.B.1.i);
#   THE 10% CONDITION  when sampling without replacement, the population must be
#     at least ten times the sample, n <= 0.10N (EK 3.2.B.1.ii) -- this is what
#     licenses treating the draws as independent;
#   LARGE COUNTS  np >= 10 AND n(1 - p) >= 10 (EK 3.2.B.2) -- this is what
#     licenses the normal approximation, and it is a condition on the expected
#     COUNTS of successes and failures, not on n alone.
# Several items give a scenario where exactly one condition fails, so the right
# answer requires knowing which condition does what.
#
# All values are recomputed in verify_s3_2.py.
TOPIC = ("3.2", "Sampling Distributions for Sample Proportions", 3)

QUESTIONS = [
 dict(q="For random samples of size n from a population with proportion p and failure proportion q, the mean of the sampling distribution of the sample proportion p-hat is",
   choices=[
     "p",
     "p divided by n",
     "np",
     "the square root of pq/n",
     "pq"],
   ans=0,
   why="The sample proportion is unbiased, so its sampling distribution centres on the population proportion whatever n is."),

 dict(q="Writing q for the failure proportion, the standard deviation of the sampling distribution of p-hat for random samples of size n is",
   choices=[
     "pq",
     "pq/n",
     "the square root of pq/n",
     "the square root of npq",
     "p divided by the square root of n"],
   ans=2,
   why="This is the standard deviation of a proportion rather than of a count; the square root of np(1-p) is the standard deviation of the COUNT of successes."),

 dict(q="A population has proportion p = 0.4. For random samples of size 200, the standard deviation of the sampling distribution of p-hat is closest to",
   choices=["0.0012", "0.0346", "0.0490", "0.2400", "6.9282"],
   ans=1,
   why="The square root of (0.4)(0.6)/200 is the square root of 0.0012, which is 0.0346; 0.0012 is the variance and 6.93 is the standard deviation of the count."),

 dict(q="A population has proportion p = 0.4. For random samples of size 200, the mean of the sampling distribution of p-hat is",
   choices=["0.0346", "0.4000", "0.6000", "80.0000", "200.0000"],
   ans=1,
   why="The sampling distribution of p-hat centres on p = 0.4; 80 is the expected COUNT of successes, not the proportion."),

 dict(q="A population has proportion p = 0.6. For random samples of size 150, the standard deviation of p-hat is",
   choices=["0.0016", "0.0400", "0.0632", "0.2400", "6.0000"],
   ans=1,
   why="The square root of (0.6)(0.4)/150 is the square root of 0.0016, which is exactly 0.0400."),

 dict(q="A population has proportion p = 0.25. For random samples of size 400, the standard deviation of p-hat is closest to",
   choices=["0.0005", "0.0217", "0.0433", "0.1875", "8.6603"],
   ans=1,
   why="The square root of (0.25)(0.75)/400 is the square root of 0.00046875, which is about 0.0217."),

 dict(q="A population has proportion p = 0.5. For random samples of size 100, the standard deviation of p-hat is",
   choices=["0.0025", "0.0500", "0.2500", "5.0000", "25.0000"],
   ans=1,
   why="The square root of (0.5)(0.5)/100 is the square root of 0.0025, which is exactly 0.0500."),

 dict(q="The large counts condition for the sampling distribution of a sample proportion requires that",
   choices=[
     "n be at least 30",
     "both the expected number of successes and the expected number of failures be at least 10",
     "np be at least 10",
     "the population be normally distributed",
     "n be at least 10% of the population"],
   ans=1,
   why="BOTH the expected number of successes and the expected number of failures must be at least 10, since either one being small leaves the distribution skewed."),

 dict(q="The 10% condition for the sampling distribution of a sample proportion requires that",
   choices=[
     "at least 10% of the population be sampled",
     "the population be at least ten times as large as the sample",
     "p be at least 0.10",
     "the sample size be at least 10",
     "the expected number of successes be at least 10"],
   ans=1,
   why="When sampling without replacement, taking no more than a tenth of the population keeps the draws close enough to independent for the formula to apply."),

 dict(q="A random sample of 200 is taken from a population with p = 0.4. Checking the large counts condition gives",
   choices=[
     "np = 80 and n(1 - p) = 120, both at least 10, so the condition is met",
     "np = 80 only, so the condition is not met",
     "np = 0.4, which is less than 10, so the condition fails",
     "np = 200, so the condition is met",
     "the condition cannot be checked without the population size"],
   ans=0,
   why="200(0.4) = 80 expected successes and 200(0.6) = 120 expected failures, and both comfortably exceed 10."),

 dict(q="A random sample of 200 is taken from a population in which p = 0.03. Does the large counts condition hold?",
   choices=[
     "Yes, because n = 200 is large",
     "No, because np = 6, which is less than 10, even though n(1 - p) = 194 is large",
     "No, because n(1 - p) is less than 10",
     "Yes, because both np and n(1 - p) exceed 10",
     "The condition does not apply to proportions"],
   ans=1,
   why="A large n is not enough: with p so small the expected number of successes is only 6, so the sampling distribution is still noticeably right-skewed."),

 dict(q="A simple random sample of 200 is drawn without replacement from a population of 1,500. Does the 10% condition hold?",
   choices=[
     "Yes, because 200 is less than 1,500",
     "No, because 200 is more than 10% of 1,500, which is 150",
     "Yes, because 1,500 is more than ten times 10",
     "No, because the sample is not large enough",
     "The condition depends on p, which is not given"],
   ans=1,
   why="Ten percent of 1,500 is 150, and a sample of 200 exceeds it, so the draws are not close enough to independent for the usual standard deviation formula."),

 dict(q="A simple random sample of 200 is drawn without replacement from a population of 50,000. Does the 10% condition hold?",
   choices=[
     "Yes, because 200 is far less than 10% of 50,000, which is 5,000",
     "No, because 50,000 is too large",
     "No, because 200 is more than 10% of 50,000",
     "Yes, but only if p is at least 0.10",
     "It cannot be determined"],
   ans=0,
   why="A sample of 200 from 50,000 is 0.4 percent of the population, comfortably within the limit."),

 dict(q="A population has p = 0.4, and samples of size 200 are drawn, satisfying all conditions. What is the probability that a sample proportion exceeds 0.45?",
   choices=["0.074", "0.126", "0.443", "0.500", "0.926"],
   ans=0,
   why="The standard deviation of p-hat is 0.0346, so z = (0.45 - 0.40)/0.0346 = 1.44 and the right-tail area is 0.074."),

 dict(q="A population has p = 0.6, and samples of size 150 are drawn, satisfying all conditions. What is the probability that a sample proportion falls below 0.55?",
   choices=["0.106", "0.211", "0.394", "0.500", "0.894"],
   ans=0,
   why="The standard deviation of p-hat is 0.0400, so z = (0.55 - 0.60)/0.0400 = -1.25 and the left-tail area is 0.106."),

 dict(q="A population has p = 0.25, and samples of size 400 are drawn, satisfying all conditions. What is the probability that a sample proportion falls between 0.22 and 0.28?",
   choices=["0.083", "0.417", "0.606", "0.834", "0.917"],
   ans=3,
   why="The standard deviation of p-hat is 0.0217, so the z-scores are -1.39 and 1.39 and the area between them is 0.834."),

 dict(q="Holding p fixed and increasing the sample size n, the standard deviation of the sampling distribution of p-hat",
   choices=[
     "increases",
     "decreases, in proportion to 1 over the square root of n",
     "decreases, in proportion to 1 over n",
     "stays the same",
     "becomes 0 once n exceeds 30"],
   ans=1,
   why="The n sits under a square root, so quadrupling the sample size halves the standard deviation rather than quartering it."),

 dict(q="For a fixed sample size n, the standard deviation of p-hat is largest when p equals",
   choices=["0.10", "0.25", "0.50", "0.75", "0.90"],
   ans=2,
   why="The product p(1 - p) is maximized at p = 0.5, which is why a conservative sample-size calculation uses 0.5."),

 dict(q="Interpreted in context, saying that the sampling distribution of p-hat has standard deviation 0.0346 for a population with p = 0.4 means that",
   choices=[
     "each sample proportion differs from 0.4 by exactly 0.0346",
     "sample proportions from repeated samples of this size typically differ from 0.4 by about 0.0346",
     "3.46% of the population has the characteristic",
     "the population proportion is 0.0346",
     "the sample size is 346"],
   ans=1,
   why="The standard deviation of a sampling distribution is a typical distance between a sample statistic and the parameter it estimates."),

 dict(q="A sample proportion p-hat is best described as",
   choices=[
     "a parameter, since it describes a proportion",
     "a statistic, whose value varies from sample to sample",
     "a constant fixed by the population",
     "the same as p whenever the conditions are met",
     "the standard deviation of the population"],
   ans=1,
   why="p-hat is computed from a sample and therefore varies; p is the fixed population value it estimates."),

 dict(q="Why is the randomization condition required for the sampling distribution of p-hat?",
   choices=[
     "Without random selection the statistic may be systematically biased, so its sampling distribution need not centre on p",
     "Random selection makes n larger",
     "Random selection guarantees the large counts condition",
     "Random selection makes the population normal",
     "It is not really required"],
   ans=0,
   why="The formulas describe the sampling distribution of a statistic from a random sample; a biased method shifts the centre, and no formula repairs that."),

 dict(q="A sample of 40 is drawn from a population with p = 0.5, and a sample of 40 from a population with p = 0.05. Comparing the two sampling distributions of p-hat,",
   choices=[
     "both are approximately normal, since n is the same",
     "the first is approximately normal since np = 20 and n(1 - p) = 20, but the second is not, since np = 2",
     "neither is approximately normal",
     "the second is approximately normal and the first is not",
     "normality depends only on n, so both are the same"],
   ans=1,
   why="The large counts condition depends on p as well as n: 40(0.05) = 2 expected successes leaves a badly skewed distribution."),

 dict(q="If the large counts condition fails, the consequence is that",
   choices=[
     "the mean of the sampling distribution is no longer p",
     "the standard deviation formula becomes invalid",
     "the normal approximation to the sampling distribution is not trustworthy, though the mean is still p",
     "the sample proportion becomes biased",
     "no sampling distribution exists"],
   ans=2,
   why="p-hat remains unbiased and its standard deviation formula still applies; what fails is the assumption that the shape is close to normal."),

 dict(q="To halve the standard deviation of the sampling distribution of p-hat while keeping p fixed, the sample size must be",
   choices=[
     "halved",
     "doubled",
     "multiplied by 4",
     "multiplied by 8",
     "multiplied by 16"],
   ans=2,
   why="The standard deviation is proportional to 1 over the square root of n, so cutting it in half requires four times the sample size."),

 dict(q="Two populations have p = 0.3, and samples of size 100 and 900 are drawn. The sampling distribution of p-hat for the larger sample is",
   choices=[
     "centred at a larger value",
     "centred at the same value, 0.3, but three times narrower",
     "centred at the same value and equally wide",
     "centred at 0.3 but nine times narrower",
     "centred at 0.1"],
   ans=1,
   why="Both centre at p = 0.3; the standard deviation falls by the square root of 9, which is 3, not by 9."),
]
