# AP STATISTICS 4.2 Constructing a Confidence Interval for a Population Mean
# or Population Mean Difference - 25 questions
# CED: AP Statistics Course and Exam Description, Effective Fall 2026, Unit 4.
# Objectives 4.2.A (describe t-distributions), 4.2.B (identify the procedure and
# the parameter, including the matched-pairs case), 4.2.C (verify the three
# conditions: randomization, 10 percent, sample data), 4.2.D (calculate the
# interval xbar +/- t* s/sqrt(n) with df = n - 1), 4.2.E (standard error and
# margin of error).
# Every critical value, standard error, margin of error and endpoint is
# recomputed in verify_s4_2.py from scipy.stats.t; nothing is read off a table.
TOPIC = ("4.2", "Constructing a Confidence Interval for a Population Mean or Population Mean Difference", 4)
QUESTIONS = [

 dict(q="A one-sample t-interval for a population mean is constructed from a random sample of 18 observations. How many degrees of freedom does the t-distribution have?", choices=[
   "16",
   "17",
   "18",
   "19",
   "36"], ans=1,
   why="For a one-sample t procedure the degrees of freedom are n - 1 = 18 - 1 = 17."),

 dict(q="What is the critical value t* for a 95 percent confidence interval for a population mean based on a random sample of 18 observations, rounded to three decimal places?", choices=[
   "1.740",
   "1.960",
   "2.110",
   "2.120",
   "2.567"], ans=2,
   why="With df = 17, the central 95 percent of the t-distribution runs to the 97.5th percentile, t* = 2.110; 1.960 is the standard normal critical value, which would be correct only if sigma were known."),

 dict(q="A random sample of 25 batteries has mean life 24.6 hours and standard deviation 3.2 hours. Battery life is approximately normally distributed. What is the 95 percent confidence interval for the population mean life?", choices=[
   "(23.279, 25.921)",
   "(23.346, 25.854)",
   "(21.400, 27.800)",
   "(24.560, 24.640)",
   "(18.995, 30.205)"], ans=0,
   why="With df = 24, t* = 2.064 and the standard error is 3.2/sqrt(25) = 0.64, so the margin of error is 1.321 and the interval is 24.6 +/- 1.321; (23.346, 25.854) is the interval you get by using z* = 1.96 instead of t*."),

 dict(q="A random sample of 36 observations has standard deviation 8.4. What is the standard error of the sample mean?", choices=[
   "0.23",
   "1.40",
   "2.80",
   "8.40",
   "50.40"], ans=1,
   why="The standard error of a sample mean is s/sqrt(n) = 8.4/sqrt(36) = 1.40; 0.23 divides by n rather than by its square root."),

 dict(q="A random sample of 12 measurements has standard deviation 5.1, and the data show no strong skewness or outliers. What is the margin of error for a 90 percent confidence interval for the population mean, rounded to three decimal places?", choices=[
   "0.425",
   "1.472",
   "2.422",
   "2.644",
   "3.242"], ans=3,
   why="With df = 11 the critical value is t* = 1.796, and the standard error is 5.1/sqrt(12) = 1.472, so the margin of error is 1.796 x 1.472 = 2.644; 1.472 is the standard error alone."),

 dict(q="A trainer records each of 20 athletes' sprint times before a training program and again after it, then wants to estimate the mean improvement. Which confidence interval procedure is appropriate?", choices=[
   "A one-sample t-interval for a population mean difference, using the 20 before-minus-after differences",
   "A two-sample t-interval for a difference between two population means, treating the before and after times as two independent samples",
   "A one-sample z-interval for a population mean, since 20 differences is enough for the central limit theorem",
   "Two separate one-sample t-intervals, one for the before times and one for the after times",
   "A one-sample t-interval for a population proportion of athletes who improved"], ans=0,
   why="Each athlete supplies a before value and an after value, so the two sets of times are dependent; a matched-pairs design is analyzed by reducing each pair to one difference and running a one-sample t procedure on those differences."),

 dict(q="A researcher has a random sample of 15 observations whose distribution is strongly right-skewed with one large outlier. She plans a one-sample t-interval for the population mean. Which condition is not met?", choices=[
   "The sample data condition, because n < 30 and the data show strong skewness and an outlier",
   "The randomization condition, because a skewed sample cannot be random",
   "The 10 percent condition, because 15 observations is too few",
   "The large counts condition, because 15 times the proportion is below 10",
   "All conditions are met, because t procedures never require normality"], ans=0,
   why="CED 4.2.C.1.iii: with n < 30 the sample data must be free from strong skewness and outliers; a skewed sample with an outlier fails that condition, and skewness says nothing about how the sample was selected."),

 dict(q="Why is a t-distribution rather than the standard normal distribution used to build a confidence interval for a population mean in most real settings?", choices=[
   "The population standard deviation is unknown and must be estimated by the sample standard deviation, which adds extra variability",
   "The sample mean is not an unbiased estimator of the population mean",
   "The t-distribution has a smaller standard deviation than the normal distribution",
   "The population distribution is never normal in practice",
   "The t-distribution removes the need for the randomization condition"], ans=0,
   why="Replacing sigma by s introduces additional sampling variability, and the wider-tailed t-distribution accounts for it; with sigma known the standard normal would be correct."),

 dict(q="Which statement about t-distributions is correct?", choices=[
   "They are symmetric and bell-shaped with tails heavier than the standard normal's, and they approach the standard normal as the degrees of freedom increase",
   "They are right-skewed for small degrees of freedom and become symmetric as the degrees of freedom increase",
   "They have thinner tails than the standard normal distribution, so their critical values are smaller",
   "They have mean 0 and standard deviation 1 for every value of the degrees of freedom",
   "They are used only when the sample size is at least 30"], ans=0,
   why="CED 4.2.A.1: the t family is symmetric and bell-shaped with fatter tails than the normal, and it converges to the standard normal as df grows; its standard deviation exceeds 1 for finite df."),

 dict(q="A researcher measures 12 pairs of twins and analyzes the 12 within-pair differences with a one-sample t-interval. How many degrees of freedom does the interval use?", choices=[
   "10",
   "11",
   "12",
   "22",
   "23"], ans=1,
   why="The matched-pairs analysis works with one sample of 12 differences, so df = 12 - 1 = 11; 22 would be the two-sample df, which does not apply to a paired design."),

 dict(q="Holding the sample the same, a 99 percent confidence interval for a population mean compared with a 95 percent interval from the same data is", choices=[
   "wider, because a larger critical value is needed to capture the parameter more often",
   "narrower, because higher confidence means more precision",
   "the same width, because the sample mean and standard deviation have not changed",
   "wider, but only if the sample size is at least 30",
   "narrower, because the standard error decreases with confidence"], ans=0,
   why="The standard error is fixed by the data; raising the confidence level raises t*, which lengthens the margin of error and widens the interval."),

 dict(q="Which change would most reduce the width of a confidence interval for a population mean without changing the confidence level?", choices=[
   "Increase the sample size",
   "Decrease the sample size",
   "Report the interval to more decimal places",
   "Use a sample with a larger standard deviation",
   "Use a two-sided interval instead of a one-sided interval"], ans=0,
   why="The margin of error is t* s/sqrt(n), so a larger n shrinks it both through the square root and through a smaller critical value; a larger s widens it instead."),

 dict(q="Eight volunteers each had their systolic blood pressure measured before and after a relaxation exercise. The before-minus-after differences, in mm Hg, were 4, 1, 5, 2, 6, 1, 4, 6. Assuming the conditions are met, what is the 95 percent confidence interval for the population mean difference?", choices=[
   "(1.898, 5.352)",
   "(2.895, 4.355)",
   "(2.164, 5.086)",
   "(3.098, 4.152)",
   "(1.559, 5.691)"], ans=0,
   why="The eight differences have mean 3.625 and standard deviation 2.066, so the standard error is 0.730; with df = 7, t* = 2.365 and the margin of error is 1.727, giving 3.625 +/- 1.727."),

 dict(q="A random sample of 30 households had a mean monthly water use of 68.2 units with standard deviation 9.4 units. What is the 99 percent confidence interval for the population mean, rounded to three decimals?", choices=[
   "(63.469, 72.931)",
   "(63.779, 72.621)",
   "(65.284, 71.116)",
   "(66.484, 69.916)",
   "(67.336, 69.064)"], ans=0,
   why="With df = 29, t* = 2.756 and the standard error is 9.4/sqrt(30) = 1.716, so the margin of error is 4.731; (63.779, 72.621) uses z* = 2.576 instead of t*, and (65.284, 71.116) is the 90 percent interval."),

 dict(q="A study compares each participant's reaction time using their dominant hand and their non-dominant hand. Which statement of the parameter for the confidence interval is best?", choices=[
   "The mean difference in reaction time, non-dominant minus dominant, for the population of all such participants",
   "The mean reaction time for the population of all such participants",
   "The difference in the mean reaction times of two independent populations of participants",
   "The mean difference in reaction time for the 40 participants in this study",
   "The proportion of participants whose non-dominant hand was slower"], ans=0,
   why="CED 4.2.B.3: the parameter is a population mean difference stated in context with the order of subtraction given; a confidence interval estimates a population parameter, never a statistic computed from the participants at hand."),

 dict(q="A 95 percent confidence interval for a population mean is reported as (14.2, 19.8). What are the sample mean and the margin of error?", choices=[
   "sample mean 17.0, margin of error 2.8",
   "sample mean 17.0, margin of error 5.6",
   "sample mean 14.2, margin of error 5.6",
   "sample mean 19.8, margin of error 2.8",
   "sample mean 34.0, margin of error 2.8"], ans=0,
   why="The sample mean is the midpoint, (14.2 + 19.8)/2 = 17.0, and the margin of error is half the width, (19.8 - 14.2)/2 = 2.8."),

 dict(q="A random sample of 40 commuters has mean travel cost 12.8 dollars with standard deviation 2.9 dollars. What is the 95 percent confidence interval for the population mean travel cost, rounded to three decimals?", choices=[
   "(11.873, 13.727)",
   "(11.901, 13.699)",
   "(12.341, 13.259)",
   "(9.900, 15.700)",
   "(12.754, 12.846)"], ans=0,
   why="With df = 39, t* = 2.023 and the standard error is 2.9/sqrt(40) = 0.4585, so the margin of error is 0.928; (11.901, 13.699) is the z* = 1.96 version."),

 dict(q="A club has 150 members. A researcher takes a simple random sample of 20 members, without replacement, and builds a one-sample t-interval for the mean annual dues paid. Regarding the 10 percent condition, the sample", choices=[
   "satisfies it, because the 20 members were chosen at random",
   "satisfies it, because 20 is less than 150",
   "does not satisfy it, because 20 is more than 10 percent of 150",
   "does not satisfy it, because 20 is less than 30",
   "cannot be assessed without knowing the population standard deviation"], ans=2,
   why="The condition is n <= 0.10N, and 0.10 x 150 = 15, so a sample of 20 is 13.3 percent of the population and the condition fails."),

 dict(q="Which is the correct interpretation of a standard error of 0.46 for a sample mean?", choices=[
   "In repeated samples of this size, sample means typically fall about 0.46 units from the population mean",
   "Individual observations typically fall about 0.46 units from the sample mean",
   "The sample mean is within 0.46 units of the population mean",
   "About 46 percent of the observations lie within one unit of the sample mean",
   "The population mean is 0.46 units from zero"], ans=0,
   why="The standard error estimates the sample-to-sample standard deviation of xbar; it describes the statistic's variability, not the spread of individual data and not a guarantee about this one sample."),

 dict(q="What is the critical value t* for a 98 percent confidence interval for a population mean based on a random sample of 30 observations, rounded to three decimal places?", choices=[
   "1.699",
   "2.045",
   "2.150",
   "2.326",
   "2.462"], ans=4,
   why="With df = 29 the central 98 percent runs to the 99th percentile of the t-distribution, t* = 2.462; 2.326 is the corresponding standard normal value."),

 dict(q="From a random sample of 20 observations with standard deviation 6.5, the margins of error for 90 percent and 95 percent confidence intervals for the population mean are, respectively, about", choices=[
   "2.513 and 3.042",
   "2.391 and 2.849",
   "3.042 and 2.513",
   "1.729 and 2.093",
   "0.325 and 0.363"], ans=0,
   why="The standard error is 6.5/sqrt(20) = 1.4534; with df = 19 the critical values are 1.729 and 2.093, so the margins of error are 2.513 and 3.042, and the higher confidence gives the larger one."),

 dict(q="A researcher randomly assigns 30 plants to fertilizer A and a different 30 plants to fertilizer B and measures growth. She wants a confidence interval for the difference in mean growth. Is a one-sample t-interval for a mean difference appropriate?", choices=[
   "No, the two groups contain different plants, so the samples are independent and a two-sample procedure is required",
   "No, because the sample sizes are equal",
   "Yes, because there are two measurements per fertilizer",
   "Yes, because the 30 growth values in each group can be paired in the order recorded",
   "Yes, because randomization was used"], ans=0,
   why="Matched pairs requires two measurements linked to the same unit; different plants in the two groups make the samples independent, and pairing them by recording order would be arbitrary."),

 dict(q="A random sample of 45 observations from a population that is not normally distributed shows moderate right skew and no outliers. Is the sample data condition for a one-sample t-interval met?", choices=[
   "Yes, because n = 45 is at least 30",
   "No, because the population is not normal",
   "No, because the sample is skewed",
   "Yes, but only if the population standard deviation is known",
   "It cannot be determined without a normal probability plot"], ans=0,
   why="CED 4.2.C.1.iii offers three routes, and one of them is n >= 30; the freedom-from-skewness requirement applies only when n < 30."),

 dict(q="A matched-pairs study produces 42 differences. Which statement about the sample data condition is correct?", choices=[
   "It is met because the number of differences is at least 30, so skewness in the differences is not disqualifying",
   "It is met only if both original samples are normally distributed",
   "It fails because 42 differences come from 84 measurements",
   "It requires the number of differences to be at least 10 percent of the population",
   "It cannot be met for matched pairs, which require a two-sample procedure"], ans=0,
   why="CED 4.2.C.1.iii treats the differences as the single sample: 30 or more differences satisfies the condition, and only below 30 must the differences be free from strong skewness and outliers."),

 dict(q="A student builds a 95 percent confidence interval from a random sample of 16 observations with mean 50.4 and standard deviation 7.2, but uses z* = 1.96 instead of the correct t*. Compared with the correct interval, the student's margin of error is", choices=[
   "too small by about 0.309, since the correct margin of error is 3.837 and the student's is 3.528",
   "too large by about 0.309, since the correct margin of error is 3.528 and the student's is 3.837",
   "correct, because n = 16 is large enough for z* to apply",
   "too small by about 1.877, since the correct margin of error is 5.405",
   "impossible to compare without the population standard deviation"], ans=0,
   why="With df = 15 the correct t* is 2.131, giving a margin of error of 2.131 x 1.8 = 3.837, while z* = 1.96 gives 3.528; using z* when sigma is unknown always understates the margin of error."),
]
