# AP STATISTICS 4.3 Justifying a Claim Based on a Confidence Interval for a
# Population Mean or Population Mean Difference - 25 questions
# CED: AP Statistics Course and Exam Description, Effective Fall 2026, Unit 4.
# Objectives 4.3.A (interpret the interval and the confidence level in context),
# 4.3.B (justify a claim from the interval), 4.3.C (relationships among sample
# size, confidence level, margin of error and width; width is approximately
# proportional to 1/sqrt(n)).
# The two errors this topic exists to correct: a confidence interval estimates a
# POPULATION parameter, never the sample statistic; and "95 percent confident"
# describes the long-run capture rate of the METHOD, not a probability that this
# one interval contains mu. Both are tested directly below.
# Every width, margin of error and count is recomputed in verify_s4_3.py.
TOPIC = ("4.3", "Justifying a Claim Based on a Confidence Interval for a Population Mean or Population Mean Difference", 4)
QUESTIONS = [

 dict(q="A 95 percent confidence interval for the mean daily commute time of all workers in a city is (18.6, 23.4) minutes. Which is the correct interpretation of the interval?", choices=[
   "We are 95 percent confident that the interval from 18.6 to 23.4 minutes contains the mean commute time of all workers in the city",
   "We are 95 percent confident that the interval from 18.6 to 23.4 minutes contains the mean commute time of the workers in the sample",
   "Ninety-five percent of all workers in the city have commute times between 18.6 and 23.4 minutes",
   "Ninety-five percent of samples of this size have mean commute times between 18.6 and 23.4 minutes",
   "The probability is 0.95 that a randomly chosen worker commutes between 18.6 and 23.4 minutes"], ans=0,
   why="An interval estimates a population parameter, so the interpretation must name the population mean; the sample mean is already known exactly and needs no interval, and the interval says nothing about where individual commute times fall."),

 dict(q="A 95 percent confidence interval for a population mean is (18.6, 23.4). Which statement is an INCORRECT interpretation?", choices=[
   "There is a 0.95 probability that the population mean lies between 18.6 and 23.4",
   "We are 95 percent confident that the population mean lies between 18.6 and 23.4",
   "The method used produces intervals that capture the population mean about 95 percent of the time",
   "If many samples of this size were taken, about 95 percent of the resulting intervals would contain the population mean",
   "The value 20 is a plausible value of the population mean"], ans=0,
   why="The population mean is a fixed number and this interval is already computed, so it either contains mu or it does not; the 95 percent describes how often the procedure succeeds in repeated sampling, not a probability attached to one finished interval."),

 dict(q="Which statement correctly interprets the confidence level of 90 percent?", choices=[
   "In repeated random sampling with the same sample size from the same population, about 90 percent of the intervals constructed would capture the population mean",
   "About 90 percent of the observations in the sample fall inside the interval",
   "About 90 percent of the population values fall inside the interval",
   "The interval is correct about 90 percent as often as a 95 percent interval is",
   "There is a 90 percent chance the sample mean is inside the interval"], ans=0,
   why="CED 4.3.A.2 defines the confidence level as the long-run capture rate of the procedure across repeated samples; it is a property of the method, not a description of the data."),

 dict(q="A researcher writes: 'We are 99 percent confident that the sample mean lies between 41.2 and 46.8.' What is wrong with this statement?", choices=[
   "A confidence interval estimates the population mean; the sample mean is known exactly and is the center of the interval",
   "Nothing is wrong; the sample mean is the parameter being estimated",
   "The confidence level should have been stated as a probability",
   "The interval should have been written with the larger number first",
   "A 99 percent interval cannot be interpreted at all, because it is too wide"], ans=0,
   why="The sample mean was computed from the data and sits at 44.0, the midpoint; there is no uncertainty about it, and the unknown quantity being estimated is the population mean."),

 dict(q="A 95 percent confidence interval for the mean fill volume of a bottling line is (12.4, 15.6) ounces. A manager claims the mean fill volume is 16 ounces. Does the interval support that claim?", choices=[
   "No, because 16 is outside the interval, so it is not a plausible value of the population mean",
   "No, because the interval is not centered at 16",
   "Yes, because 16 is close to the upper endpoint",
   "Yes, because a 95 percent interval leaves 5 percent of values outside it",
   "There is not enough information without the sample size"], ans=0,
   why="Values outside the interval are the ones the data give evidence against; 16 lies above the upper endpoint 15.6, so the interval does not support the claim."),

 dict(q="A 90 percent confidence interval for the population mean difference (after minus before) in test scores is (-0.4, 2.9) points. What does this say about whether the program changed mean scores?", choices=[
   "It does not give convincing evidence of a change, because 0 is a plausible value of the mean difference",
   "It gives convincing evidence of an increase, because most of the interval is positive",
   "It gives convincing evidence of no change, because 0 is inside the interval",
   "It gives convincing evidence of a decrease, because the lower endpoint is negative",
   "It is uninterpretable, because a confidence interval cannot contain negative numbers"], ans=0,
   why="An interval containing 0 leaves 'no mean change' among the plausible values, which is a failure to find evidence of a change and is not the same as evidence that the mean difference is exactly 0."),

 dict(q="A 95 percent confidence interval for the population mean difference (treated minus untreated) in plant height is (1.8, 4.6) cm. What does this support?", choices=[
   "Convincing evidence that the mean height is greater for treated plants, since every value in the interval is positive",
   "Convincing evidence that the mean height is greater for untreated plants",
   "No conclusion, because the interval does not contain 0",
   "Convincing evidence that the mean difference equals 3.2 cm exactly",
   "Convincing evidence that every treated plant is taller than every untreated plant"], ans=0,
   why="With the whole interval above 0, every plausible value of the mean difference is positive; the interval is about the mean, not about individual plants, and it does not pin the difference to its midpoint."),

 dict(q="From a random sample of 20 observations with standard deviation 8, the widths of the 90 percent and 99 percent confidence intervals for the population mean are, respectively, about", choices=[
   "6.186 and 10.236",
   "3.093 and 5.118",
   "10.236 and 6.186",
   "6.186 and 6.186",
   "1.729 and 2.861"], ans=0,
   why="The standard error is 8/sqrt(20) = 1.789; with df = 19 the critical values are 1.729 and 2.861, giving margins of error 3.093 and 5.118 and widths twice those, so raising the confidence level widens the interval."),

 dict(q="For a fixed confidence level, the width of a confidence interval for a population mean is approximately proportional to 1/sqrt(n). To cut the width approximately in half, the sample size should be multiplied by", choices=[
   "0.5",
   "2",
   "4",
   "8",
   "16"], ans=2,
   why="Halving 1/sqrt(n) requires sqrt(n) to double, so n must be multiplied by 4."),

 dict(q="A researcher wants the margin of error for a population mean to be about one third of its current value, keeping the same confidence level and population. By approximately what factor must the sample size be multiplied?", choices=[
   "3",
   "6",
   "9",
   "12",
   "27"], ans=2,
   why="The margin of error scales like 1/sqrt(n), so dividing it by 3 requires sqrt(n) to triple, which multiplies n by 9."),

 dict(q="A 95 percent confidence interval for a population mean is built from a random sample of 36 observations with standard deviation 12. If a second random sample of 144 observations from the same population also has standard deviation 12, the widths of the two 95 percent intervals are about", choices=[
   "8.120 and 3.953",
   "8.120 and 2.030",
   "4.060 and 1.977",
   "3.953 and 8.120",
   "8.120 and 8.120"], ans=0,
   why="The widths are 2t*s/sqrt(n): with df = 35, 2(2.030)(2) = 8.120, and with df = 143, 2(1.977)(1) = 3.953; quadrupling n roughly halves the width."),

 dict(q="From a random sample of 25 observations, the margin of error for a 90 percent confidence interval for the population mean is 2.5. What is the margin of error for a 95 percent interval from the same sample, rounded to three decimals?", choices=[
   "2.098",
   "2.500",
   "3.016",
   "3.220",
   "4.132"], ans=2,
   why="The standard error is 2.5/1.711 = 1.461 with df = 24, and the 95 percent critical value is 2.064, so the margin of error becomes 2.064 x 1.461 = 3.016."),

 dict(q="A population's standard deviation is estimated by s = 6 from earlier work. What is the smallest sample size for which a 95 percent t-interval for the population mean would have a margin of error no larger than 1, assuming the new sample also gives s = 6?", choices=[
   "36",
   "139",
   "141",
   "144",
   "864"], ans=2,
   why="Solving t*(n-1) x 6/sqrt(n) <= 1 by increasing n gives the first success at n = 141; the value 139 comes from using z* = 1.96 instead of t*, which understates the required size."),

 dict(q="A 95 percent confidence interval for a population mean is (34.1, 41.9). What are the margin of error and the width?", choices=[
   "margin of error 3.9, width 7.8",
   "margin of error 7.8, width 3.9",
   "margin of error 3.9, width 3.9",
   "margin of error 7.8, width 15.6",
   "margin of error 38.0, width 7.8"], ans=0,
   why="The margin of error is half the width: (41.9 - 34.1)/2 = 3.9, and the width is 7.8; the midpoint 38.0 is the sample mean, not a margin of error."),

 dict(q="Two hundred independent random samples of the same size are drawn from a population, and a 90 percent confidence interval for the population mean is built from each. About how many of those intervals would be expected to contain the population mean?", choices=[
   "20",
   "90",
   "100",
   "180",
   "200"], ans=3,
   why="The confidence level is the long-run capture rate, so about 0.90 x 200 = 180 of the intervals would capture mu and about 20 would miss it."),

 dict(q="A statistician constructs a 95 percent confidence interval and later learns that it does not contain the population mean. What is the best conclusion?", choices=[
   "Nothing was necessarily done wrong; about 5 percent of intervals built this way fail to capture the parameter",
   "The procedure was applied incorrectly, because a 95 percent interval must contain the parameter",
   "The sample size must have been too small",
   "The confidence level should be reported as 0 percent for this interval",
   "The population mean must have changed between sampling and analysis"], ans=0,
   why="A confidence level is a statement about how often the method succeeds; a particular interval either captures mu or it does not, and roughly 1 in 20 will not."),

 dict(q="A 99 percent confidence interval for the mean weight of a population of packages is (101.2, 108.8) grams. Which claim does the interval support?", choices=[
   "The population mean weight is greater than 100 grams",
   "The population mean weight is less than 100 grams",
   "The population mean weight is exactly 105 grams",
   "Every package weighs between 101.2 and 108.8 grams",
   "Ninety-nine percent of packages weigh more than 100 grams"], ans=0,
   why="Every plausible value in the interval exceeds 100, so the interval supports the claim that mu > 100; it does not pin mu to the midpoint and says nothing about individual packages."),

 dict(q="From one sample, two intervals for the population mean are computed: (46.1, 53.9) and (44.6, 55.4). Which is the 99 percent interval, and why?", choices=[
   "(44.6, 55.4), because a higher confidence level requires a larger critical value and therefore a wider interval",
   "(46.1, 53.9), because a higher confidence level means more precision and therefore a narrower interval",
   "(44.6, 55.4), because it has a larger sample mean",
   "(46.1, 53.9), because its center is closer to 50",
   "It cannot be determined, since both have the same center"], ans=0,
   why="Both are centered at 50, so only the critical value differs; the 99 percent level uses the larger t* and produces the wider of the two."),

 dict(q="A researcher increases the sample size from 40 to 90 and rebuilds a 95 percent confidence interval for the same population mean. Which description is most accurate?", choices=[
   "The interval will tend to be narrower, and its center may shift because a new sample gives a new sample mean",
   "The interval will be narrower and will have exactly the same center",
   "The interval will be wider, because more data introduces more variability",
   "The interval will have the same width, because the confidence level is unchanged",
   "The interval will be narrower and is guaranteed to contain the population mean"], ans=0,
   why="A larger n shrinks the standard error and so the width, but the new sample produces a new sample mean, so the center is not fixed; and no interval is guaranteed to capture mu."),

 dict(q="Which of the following would make a confidence interval for a population mean narrower without changing the confidence level or the sampling method?", choices=[
   "Collecting a larger random sample from the same population",
   "Raising the confidence level from 95 percent to 99 percent",
   "Reporting the endpoints to fewer decimal places",
   "Using the population median instead of the population mean",
   "Removing the observations farthest from the sample mean"], ans=0,
   why="Only a larger sample legitimately reduces the standard error; deleting extreme observations changes the data rather than improving the estimate, and raising the confidence level widens the interval."),

 dict(q="A 95 percent confidence interval for the population mean difference (post minus pre) in reaction time is (-32, -8) milliseconds. What is the best justified claim?", choices=[
   "The mean reaction time after the treatment is lower than before, since every plausible value of the mean difference is negative",
   "The mean reaction time after the treatment is higher than before",
   "There is no convincing evidence of a change",
   "The mean difference is exactly -20 milliseconds",
   "Ninety-five percent of the participants improved by between 8 and 32 milliseconds"], ans=0,
   why="With the whole interval below 0 and the order of subtraction being post minus pre, the plausible mean differences are all decreases; the interval describes the mean difference, not individual participants."),

 dict(q="For a 95 percent confidence interval for a population mean, what happens to the width when the confidence level is lowered to 80 percent, everything else held fixed?", choices=[
   "The width decreases, because the critical value decreases",
   "The width increases, because less confidence requires more room",
   "The width is unchanged, because the standard error is unchanged",
   "The width decreases, because the standard error decreases",
   "The width cannot be predicted without the sample size"], ans=0,
   why="CED 4.3.C.1: the standard error depends on the data alone, so lowering the confidence level lowers t* and shortens the interval; it buys precision at the cost of a lower capture rate."),

 dict(q="A 95 percent confidence interval for the mean score of a population is (72, 78). A student says this means 95 percent of scores in the population fall between 72 and 78. What is the flaw?", choices=[
   "The interval estimates the population mean, not the spread of individual scores",
   "The interval should have been built with a 68 percent confidence level to describe individual scores",
   "The student should have said 95 percent of sample means, which would be correct",
   "There is no flaw; a confidence interval does describe the middle 95 percent of the population",
   "The flaw is only that the endpoints are not stated to enough decimal places"], ans=0,
   why="An interval for a mean is far narrower than the spread of individual observations; describing individual values would require a different kind of interval altogether."),

 dict(q="A 90 percent confidence interval for a population mean is (14.8, 21.2). Which value is NOT a plausible value of the population mean at this confidence level?", choices=[
   "15.0",
   "18.0",
   "20.5",
   "21.0",
   "22.0"], ans=4,
   why="Plausible values are exactly those inside the interval; 22.0 lies above the upper endpoint 21.2, and every other listed value lies inside."),

 dict(q="Two researchers analyze the same random sample of 30 observations. One reports a 95 percent confidence interval for the population mean; the other reports a 95 percent confidence interval for the population mean using only the first 15 observations. Compared with the first, the second interval is expected to be", choices=[
   "wider, because a smaller sample has a larger standard error and a larger critical value",
   "narrower, because fewer observations means less variability",
   "the same width, because the confidence level is the same",
   "wider, but only because the population standard deviation changed",
   "narrower, because df drops from 29 to 14"], ans=0,
   why="Cutting n from 30 to 15 raises the standard error by a factor of about sqrt(2) and raises t* from 2.045 to 2.145 as df falls from 29 to 14, so both factors widen the interval."),
]
