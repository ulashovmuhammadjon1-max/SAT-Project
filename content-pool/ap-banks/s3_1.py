# AP STATISTICS 3.1 Estimators - 25 questions
# CED: AP Statistics Course and Exam Description, Effective Fall 2026, Unit 3.
# Learning objectives 3.1.A (justify why an estimator is or is not unbiased) and
# 3.1.B (calculate estimates for a population parameter).
# Every numeric key is recomputed in verify_s3_1.py with statistics/numpy;
# the conceptual items are listed there with the reasoning that fixes the key.
TOPIC = ("3.1", "Estimators", 3)
QUESTIONS = [

 dict(q="In a random sample of 400 registered voters in a large county, 138 said they had voted in the most recent local election. What is the point estimate of the proportion of all registered voters in the county who voted in that election?", choices=[
   "0.138",
   "0.257",
   "0.345",
   "0.655",
   "2.899"], ans=2,
   why="A sample proportion is successes over sample size, 138/400 = 0.345; 0.655 is the proportion who did not vote and 2.899 inverts the ratio."),

 dict(q="A researcher wants to estimate the mean number of hours per week that adults in a city spend commuting. Which of the following is a point estimator of that population mean?", choices=[
   "The sample mean number of commuting hours",
   "The population standard deviation of commuting hours",
   "The size of the sample",
   "The margin of error of the interval",
   "The confidence level used"], ans=0,
   why="A point estimator is the sample statistic that corresponds to the parameter, so the sample mean estimates the population mean."),

 dict(q="An estimator of a population parameter is described as unbiased. What does that mean?", choices=[
   "Over all possible samples of that size, the estimator's values center on the parameter, neither systematically too high nor too low",
   "Every sample of that size produces a value exactly equal to the parameter",
   "The estimator has the smallest possible standard deviation among all estimators",
   "The estimator's value gets closer to the parameter every time the sample size increases by one",
   "The sample was chosen so that no one in the population was left out"], ans=0,
   why="Unbiasedness is a statement about the center of the sampling distribution, not about any single sample and not about spread."),

 dict(q="A random sample of eight commuters reported these travel times, in minutes: 22, 31, 27, 35, 19, 28, 24, 30. What is the point estimate of the mean travel time for all commuters in this population?", choices=[
   "24.0 minutes",
   "27.0 minutes",
   "27.5 minutes",
   "28.0 minutes",
   "30.0 minutes"], ans=1,
   why="The sample mean is 216/8 = 27.0 minutes; 27.5 is the sample median, which estimates the population median instead."),

 dict(q="For the same eight travel times (22, 31, 27, 35, 19, 28, 24, 30), what is the point estimate of the population standard deviation, rounded to two decimal places?", choices=[
   "4.85",
   "5.18",
   "5.83",
   "26.86",
   "27.00"], ans=1,
   why="The sample standard deviation divides the sum of squared deviations by n - 1 = 7, giving 5.18; 4.85 divides by n and 26.86 is the sample variance."),

 dict(q="A student computes the variance of a sample by dividing the sum of squared deviations from the sample mean by n instead of by n - 1. As an estimator of the population variance, this quantity is", choices=[
   "biased, and it tends to underestimate the population variance",
   "biased, and it tends to overestimate the population variance",
   "unbiased, because the sample mean is unbiased",
   "unbiased, but with a larger standard deviation than the usual estimator",
   "neither biased nor unbiased, because variance is not a parameter"], ans=0,
   why="Deviations are taken from the sample mean rather than the population mean, which makes the sum of squares too small; dividing by n - 1 rather than n corrects that and is what makes the sample variance unbiased."),

 dict(q="Two estimators of the same population parameter, whose true value is 42, are studied by simulation. Estimator A has a sampling distribution centered at 42.0 with standard deviation 3.1. Estimator B has a sampling distribution centered at 44.5 with standard deviation 1.2. Which statement is correct?", choices=[
   "A is unbiased but more variable; B is biased but less variable",
   "B is unbiased but more variable; A is biased but less variable",
   "Both are unbiased, and B is preferable because it is less variable",
   "Both are biased, because neither has standard deviation 0",
   "A is biased because its standard deviation exceeds B's"], ans=0,
   why="Bias is read from the center of the sampling distribution and variability from its standard deviation; A centers on 42 and B does not, but B is the tighter of the two."),

 dict(q="In one random sample of 400 adults, 138 hold a library card. In an independent random sample of 250 teenagers, 96 hold a library card. What is the point estimate of the difference (adults minus teenagers) in the population proportions?", choices=[
   "-0.039",
   "0.039",
   "0.345",
   "0.384",
   "0.729"], ans=0,
   why="The difference of the two sample proportions is 138/400 - 96/250 = 0.345 - 0.384 = -0.039; adding rather than subtracting gives 0.729."),

 dict(q="Of 180 randomly selected trees in a large forest, 57 showed signs of a particular fungus. What is the point estimate of the proportion of all trees in the forest with the fungus, rounded to three decimal places?", choices=[
   "0.180",
   "0.317",
   "0.350",
   "0.570",
   "0.683"], ans=1,
   why="57/180 = 0.3167, which rounds to 0.317; 0.683 is the proportion without the fungus."),

 dict(q="Household incomes in a large city are strongly right-skewed. A researcher uses the median of a random sample as an estimator of the mean household income for the city. This estimator is", choices=[
   "biased, and it will tend to underestimate the population mean",
   "biased, and it will tend to overestimate the population mean",
   "unbiased, because the sample was random",
   "unbiased, because the median is a resistant measure of center",
   "unbiased only if the sample size is at least 30"], ans=0,
   why="In a right-skewed population the mean sits above the median, so a sample median centers near the population median and lands below the population mean on average."),

 dict(q="A sampling method produces an estimator that is biased. The researcher quadruples the sample size while keeping the same method. What is the effect on the estimator?", choices=[
   "The bias is unchanged, but the variability decreases",
   "The bias is cut to one quarter, and the variability is unchanged",
   "Both the bias and the variability are cut in half",
   "Both the bias and the variability are eliminated",
   "The bias is unchanged, and the variability is unchanged"], ans=0,
   why="Sample size controls the spread of the sampling distribution but not where it is centered, so a larger sample makes a biased estimator more precisely wrong."),

 dict(q="A wildlife biologist uses the largest weight in a random sample of fish as an estimator of the heaviest weight in the whole lake population. As an estimator of that population maximum, the sample maximum is", choices=[
   "biased, because it can never exceed the population maximum and is usually below it",
   "biased, because it can never fall below the population maximum",
   "unbiased, because each fish was equally likely to be selected",
   "unbiased, because the maximum is a single observed value rather than an average",
   "unbiased whenever the sample size is more than 10 percent of the population"], ans=0,
   why="No sample value can exceed the population maximum, and most samples miss the single heaviest fish, so the sample maximum is systematically too small."),

 dict(q="A random sample of ten bags of flour had these net weights, in kilograms: 4.1, 3.7, 4.6, 3.9, 4.2, 4.5, 3.8, 4.4, 4.0, 4.3. What is the point estimate of the mean net weight for the whole production run?", choices=[
   "4.05 kg",
   "4.10 kg",
   "4.15 kg",
   "4.20 kg",
   "4.25 kg"], ans=2,
   why="The ten weights total 41.5 kg, so the sample mean is 4.15 kg."),

 dict(q="For the same ten net weights (4.1, 3.7, 4.6, 3.9, 4.2, 4.5, 3.8, 4.4, 4.0, 4.3), what is the point estimate of the population standard deviation, rounded to three decimal places?", choices=[
   "0.092",
   "0.287",
   "0.303",
   "0.415",
   "0.958"], ans=2,
   why="Dividing the sum of squared deviations by n - 1 = 9 and taking the square root gives 0.303 kg; 0.287 divides by n and 0.092 is the variance."),

 dict(q="Which of the following is an unbiased estimator of the population variance?", choices=[
   "The sample variance, computed with n - 1 in the denominator",
   "The sample variance, computed with n in the denominator",
   "The sample standard deviation, computed with n - 1 in the denominator",
   "The sample range",
   "The sample interquartile range"], ans=0,
   why="Dividing by n - 1 makes the sample variance unbiased for the population variance; taking the square root of it does not preserve unbiasedness, and range and IQR estimate spread but not the variance."),

 dict(q="A point estimate is reported as a single number. What is its main limitation as a summary of what a sample says about a parameter?", choices=[
   "It carries no information about how far from the parameter it is likely to be",
   "It can only be computed when the population is normally distributed",
   "It is always further from the parameter than an interval estimate is",
   "It requires the population size to be known exactly",
   "It changes the value of the parameter it is estimating"], ans=0,
   why="A single value conveys no sense of sampling variability, which is why interval estimates are reported alongside it."),

 dict(q="A town has 1,200 households. A simple random sample of 50 of those households had a mean of 3.4 residents per household. What is the point estimate of the total number of residents living in the town's households?", choices=[
   "170",
   "1,200",
   "4,080",
   "40,800",
   "60,000"], ans=2,
   why="The estimated total is the estimated mean times the number of households, 3.4 x 1,200 = 4,080; 170 is the estimated total for the sample alone."),

 dict(q="An independent random sample of 40 students from School A had a mean quiz score of 78.4, and an independent random sample of 35 students from School B had a mean quiz score of 72.9. What is the point estimate of the difference in population mean scores (School A minus School B)?", choices=[
   "0.5",
   "5.5",
   "75.7",
   "151.3",
   "5.0"], ans=1,
   why="The difference of the two sample means, 78.4 - 72.9 = 5.5, estimates the difference of the population means; 75.7 is their average."),

 dict(q="A measuring instrument is tested repeatedly on an object whose true length is 50.0 cm. The readings cluster tightly between 51.6 cm and 51.9 cm. As an estimator of the true length, the instrument's reading is best described as", choices=[
   "biased with low variability",
   "biased with high variability",
   "unbiased with low variability",
   "unbiased with high variability",
   "unbiased, because the readings are so consistent"], ans=0,
   why="The readings are consistent with each other, which is low variability, but they center near 51.75 cm rather than 50.0 cm, which is bias; consistency is not accuracy."),

 dict(q="A website posts a survey and computes the proportion of respondents who agree with a statement, using the usual formula for a sample proportion. Only visitors who choose to answer are included. Is that sample proportion an unbiased estimator of the population proportion?", choices=[
   "No, because volunteers who respond tend to differ systematically from those who do not",
   "No, because the formula for a sample proportion applies only to random samples",
   "Yes, because the formula for a sample proportion is itself unbiased",
   "Yes, provided that at least 30 people responded",
   "Yes, provided the number of respondents is less than 10 percent of the population"], ans=0,
   why="Unbiasedness depends on how the data were collected, not on the arithmetic; voluntary response systematically favors people with strong opinions, so the estimator is biased no matter how large the response."),

 dict(q="A random sample of twelve deliveries took these times, in minutes: 12, 15, 11, 18, 14, 13, 17, 12, 16, 14, 15, 13. What is the point estimate of the population mean delivery time, rounded to two decimal places?", choices=[
   "13.50",
   "14.00",
   "14.17",
   "14.50",
   "15.00"], ans=2,
   why="The twelve times total 170 minutes, so the sample mean is 170/12 = 14.17 minutes; 14.00 is the sample median."),

 dict(q="For the same twelve delivery times (12, 15, 11, 18, 14, 13, 17, 12, 16, 14, 15, 13), what is the point estimate of the population standard deviation, rounded to two decimal places?", choices=[
   "2.03",
   "2.12",
   "2.61",
   "4.52",
   "7.00"], ans=1,
   why="Dividing the sum of squared deviations by n - 1 = 11 and taking the square root gives 2.12 minutes; 2.03 divides by n and 4.52 is the sample variance."),

 dict(q="A pollster wants the sample proportion to vary less from sample to sample without changing what it estimates. Which change accomplishes that?", choices=[
   "Take a larger random sample from the same population",
   "Replace the random sample with a convenience sample of the same size",
   "Report the sample proportion of failures instead of successes",
   "Use the same sample but state the result to more decimal places",
   "Survey the same people a second time and average the two results"], ans=0,
   why="Increasing n shrinks the standard deviation of the sampling distribution while leaving its center at p; a convenience sample introduces bias, and rounding or re-asking the same people adds no new information about the population."),

 dict(q="A parameter of interest equals 0.60. Four estimation procedures are simulated 10,000 times each, and the means of the 10,000 estimates are 0.601 for procedure I, 0.548 for procedure II, 0.662 for procedure III, and 0.599 for procedure IV. Which procedures show no evidence of bias?", choices=[
   "I and IV only",
   "I and II only",
   "II and III only",
   "III and IV only",
   "All four"], ans=0,
   why="The simulated means for I and IV sit at 0.601 and 0.599, essentially on the parameter 0.60, while II is about 0.05 below it and III about 0.06 above it."),

 dict(q="An estimator T of a parameter theta has the property that the mean of its sampling distribution is 0.90 times theta for every sample size. By what constant should T be multiplied to obtain an unbiased estimator of theta?", choices=[
   "0.900",
   "1.000",
   "1.100",
   "1.111",
   "1.900"], ans=3,
   why="Multiplying T by 1/0.90 = 1.111 makes the mean of the sampling distribution equal to theta; 1.100 is the common error of adding the 10 percent shortfall back to 1 instead of dividing."),
]
