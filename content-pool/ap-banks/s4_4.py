# AP STATISTICS 4.4 Setting Up a Test for a Population Mean or Population Mean
# Difference - 25 questions
# CED: AP Statistics Course and Exam Description, Effective Fall 2026, Unit 4.
# Objectives 4.4.A (identify the testing method and the parameter, including the
# matched-pairs case), 4.4.B (H0: mu = mu0 with Ha one- or two-sided; for a mean
# difference H0: mu_d = 0), 4.4.C (the same three conditions as 4.2: random,
# 10 percent, sample data).
# The two errors this topic exists to correct: hypotheses are statements about a
# PARAMETER and never about xbar, and the paired-versus-two-sample choice is
# settled by whether the two measurements come from the same unit. Both are
# tested repeatedly below, including cases where a condition FAILS.
# Degrees of freedom and every 10 percent-condition threshold are recomputed in
# verify_s4_4.py.
TOPIC = ("4.4", "Setting Up a Test for a Population Mean or Population Mean Difference", 4)
QUESTIONS = [

 dict(q="A manufacturer claims the mean lifetime of its batteries is 40 hours. A consumer group suspects the true mean is lower and takes a random sample. What are the appropriate hypotheses?", choices=[
   "H0: mu = 40 versus Ha: mu < 40",
   "H0: mu = 40 versus Ha: mu > 40",
   "H0: mu = 40 versus Ha: mu is not equal to 40",
   "H0: xbar = 40 versus Ha: xbar < 40",
   "H0: mu < 40 versus Ha: mu = 40"], ans=0,
   why="The null states the claimed value of the population mean and the alternative states the suspicion, which is one-sided and downward; hypotheses are never written about the sample mean."),

 dict(q="Why can a hypothesis never be stated in terms of the sample mean xbar?", choices=[
   "The sample mean is a known number computed from the data, so there is nothing about it left to test",
   "The sample mean is always equal to the population mean, so the test would be trivial",
   "The sample mean is not a random variable",
   "The sample mean has no units, so it cannot be compared to a hypothesized value",
   "Hypotheses may be written about xbar as long as the sample is random"], ans=0,
   why="A test asks whether an unknown parameter could plausibly equal a stated value; xbar has already been observed, so a hypothesis about it would be answered by looking at the data rather than by inference."),

 dict(q="A one-sample t-test for a population mean is run on a random sample of 23 observations. How many degrees of freedom does the test statistic have?", choices=[
   "21",
   "22",
   "23",
   "24",
   "46"], ans=1,
   why="For a one-sample t procedure df = n - 1 = 23 - 1 = 22."),

 dict(q="Sixteen students each take a typing test with a standard keyboard and again with an ergonomic keyboard, in random order. A test compares mean typing speeds. What procedure and degrees of freedom apply?", choices=[
   "A one-sample t-test for a population mean difference with 15 degrees of freedom",
   "A one-sample t-test for a population mean difference with 16 degrees of freedom",
   "A two-sample t-test with 30 degrees of freedom",
   "A two-sample t-test with 15 degrees of freedom",
   "A one-sample z-test for a population mean difference"], ans=0,
   why="Each student supplies both measurements, so the design is matched pairs; the analysis uses one sample of 16 differences and df = 16 - 1 = 15."),

 dict(q="For a matched-pairs t-test in which the differences are computed as after minus before, what is the null hypothesis?", choices=[
   "H0: mu_d = 0",
   "H0: xbar_d = 0",
   "H0: mu_after = mu_before, tested with a two-sample procedure",
   "H0: mu_d is not equal to 0",
   "H0: d = 0 for every pair"], ans=0,
   why="CED 4.4.B.2: the null for a population mean difference is mu_d = 0, a statement about the population mean of the differences rather than about the observed mean difference or about individual pairs."),

 dict(q="A dietitian randomly assigns 25 volunteers to diet A and a different 25 volunteers to diet B, then compares mean weight loss. Which procedure is appropriate?", choices=[
   "A two-sample t-test for a difference between two population means, because the two groups contain different people",
   "A one-sample t-test for a population mean difference, pairing the volunteers by the order they enrolled",
   "A one-sample t-test for a population mean, using all 50 weight losses",
   "A matched-pairs t-test, because the group sizes are equal",
   "A one-sample z-test, because 50 is at least 30"], ans=0,
   why="Pairing requires two measurements on the same unit; different volunteers in the two arms make the samples independent, and equal group sizes do not create pairs."),

 dict(q="A random sample of 28 members is drawn without replacement from a club of 250 members for a one-sample t-test of the mean annual dues. Which condition fails?", choices=[
   "The 10 percent condition, because 28 exceeds 25",
   "The 10 percent condition, because 250 exceeds 10 times 28",
   "The randomization condition, because the sample was drawn without replacement",
   "The sample data condition, because 28 is below 30",
   "No condition fails"], ans=0,
   why="The condition is n <= 0.10N, and 0.10 x 250 = 25, so a sample of 28 is 11.2 percent of the club and the condition fails; being below 30 is not itself a failure, since the sample data condition can be met by an absence of strong skewness and outliers."),

 dict(q="A researcher plans a one-sample t-test using a random sample of 45 observations drawn without replacement. What is the smallest population size for which the 10 percent condition is satisfied?", choices=[
   "45",
   "90",
   "450",
   "455",
   "4,500"], ans=2,
   why="The condition n <= 0.10N requires N >= 10n = 450."),

 dict(q="A quality engineer wants to know whether a machine's mean fill differs from 500 mL in either direction. What is the alternative hypothesis?", choices=[
   "Ha: mu is not equal to 500",
   "Ha: mu > 500",
   "Ha: mu < 500",
   "Ha: xbar is not equal to 500",
   "Ha: mu = 500"], ans=0,
   why="A concern about a difference in either direction is two-sided, and the alternative is always a statement about the population mean."),

 dict(q="A random sample of 14 observations for a one-sample t-test shows a clear outlier and pronounced right skew. What should the analyst conclude about the conditions?", choices=[
   "The sample data condition is not met, because with n < 30 the data must be free from strong skewness and outliers",
   "The sample data condition is met, because t procedures are robust to any departure from normality",
   "The randomization condition is not met, because outliers indicate a biased sample",
   "The 10 percent condition is not met, because the sample is small",
   "All conditions are met, because the sample was randomly selected"], ans=0,
   why="CED 4.4.C.1.iii: with n below 30 and no stated normal population, the sample itself must be free from strong skewness and outliers; an outlier plus strong skew fails it."),

 dict(q="Which statement of the parameter is appropriate for a one-sample t-test in a study of household electricity use?", choices=[
   "mu = the mean monthly electricity use, in kilowatt-hours, for all households in the city",
   "xbar = the mean monthly electricity use for the 40 households sampled",
   "mu = the mean monthly electricity use for the 40 households sampled",
   "p = the proportion of households whose use exceeds the mean",
   "mu = the monthly electricity use of a randomly chosen household"], ans=0,
   why="CED 4.4.A.3: the parameter names the population, the response variable and its units; it is not the sample mean and not a single household's value."),

 dict(q="A city claims its mean emergency response time is at most 8 minutes. A reporter wants evidence that the mean exceeds 8 minutes. What are the hypotheses?", choices=[
   "H0: mu = 8 versus Ha: mu > 8",
   "H0: mu = 8 versus Ha: mu < 8",
   "H0: mu > 8 versus Ha: mu = 8",
   "H0: mu is not equal to 8 versus Ha: mu = 8",
   "H0: mu = 8 versus Ha: mu is not equal to 8"], ans=0,
   why="The null takes the boundary value 8 and the alternative expresses what the reporter is trying to demonstrate, an increase, so the test is one-sided upward."),

 dict(q="For a paired design measuring blood pressure before and after a drug, with differences taken as before minus after, which alternative expresses 'the drug lowers blood pressure on average'?", choices=[
   "Ha: mu_d > 0",
   "Ha: mu_d < 0",
   "Ha: mu_d is not equal to 0",
   "Ha: mu_before < mu_after",
   "Ha: xbar_d > 0"], ans=0,
   why="With before minus after, a drop in blood pressure makes each difference positive, so 'the drug lowers pressure' is mu_d > 0; the order of subtraction has to be read before the alternative is written."),

 dict(q="Why must the direction of a one-sided alternative be chosen before the data are examined?", choices=[
   "Choosing the direction after seeing which way the sample mean fell makes the stated error rate wrong",
   "The direction has no effect on the p-value, so it can be chosen at any time",
   "A one-sided alternative requires a larger sample than a two-sided one",
   "The t-distribution is not symmetric, so the direction changes the degrees of freedom",
   "The direction must match the sign of the sample mean for the test to be valid"], ans=0,
   why="Picking the tail after seeing the data guarantees the more favorable half and inflates the true Type I error rate above the stated alpha; the hypotheses must come from the research question."),

 dict(q="A researcher takes a random sample of 60 observations from a population that is clearly right-skewed and wants to test a claim about the population mean. Are the conditions for a one-sample t-test met?", choices=[
   "Yes, because n = 60 is at least 30, so the sample data condition is satisfied despite the skewness",
   "No, because the population is not normal",
   "No, because the sample is skewed",
   "Yes, but only if the population standard deviation is known",
   "It cannot be determined without a histogram of the sample"], ans=0,
   why="CED 4.4.C.1.iii offers n >= 30 as an alternative route to the sample data condition; skewness disqualifies only when n is below 30."),

 dict(q="A test is run on a matched-pairs design with 34 pairs. Which statement about the sample data condition is correct?", choices=[
   "It is satisfied because there are at least 30 differences",
   "It is satisfied only if both original samples are normal",
   "It fails because 34 pairs means 68 measurements, which are not independent",
   "It requires the differences to be free from skewness regardless of how many there are",
   "It cannot be evaluated for a paired design"], ans=0,
   why="For matched pairs the CED applies the condition to the differences: at least 30 differences suffices, and freedom from strong skewness and outliers is required only below 30."),

 dict(q="Which of the following is NOT one of the three conditions for a one-sample t-test for a population mean?", choices=[
   "The population standard deviation must be known",
   "The data come from a random sample or a randomized experiment",
   "When sampling without replacement, the sample is at most 10 percent of the population",
   "The population is approximately normal, or n is at least 30, or the sample shows no strong skewness or outliers",
   "For matched pairs, the condition is applied to the sample of differences"], ans=0,
   why="A known sigma would call for a z procedure rather than t; the CED's three conditions are randomization, 10 percent, and the sample data condition."),

 dict(q="A school district tests whether a new curriculum changed the mean score from the historical value of 72. The sample mean turns out to be 75.4. What are the correct hypotheses?", choices=[
   "H0: mu = 72 versus Ha: mu is not equal to 72",
   "H0: mu = 75.4 versus Ha: mu is not equal to 75.4",
   "H0: mu = 72 versus Ha: mu > 72",
   "H0: xbar = 72 versus Ha: xbar = 75.4",
   "H0: mu = 75.4 versus Ha: mu > 72"], ans=0,
   why="The question asks whether the mean changed, which is two-sided, and the hypothesized value is the historical 72; the observed 75.4 belongs in the test statistic, never in the hypotheses."),

 dict(q="A study measures the fuel economy of 12 cars, first with a standard tire and then with a low-resistance tire on the same car. Which is the strongest reason to analyze the data as matched pairs rather than as two independent samples?", choices=[
   "Both measurements come from the same car, so car-to-car differences are removed from the comparison",
   "The two samples have the same size",
   "Twelve is below 30, so a paired analysis is required",
   "Fuel economy is a quantitative variable",
   "A paired analysis always produces a smaller p-value"], ans=0,
   why="Pairing is justified by the link between the two measurements on one unit; differencing within a car removes the variation between cars, which is usually the largest source of noise, but it is the design and not the sample size or the hoped-for p-value that decides."),

 dict(q="An investigator collects a convenience sample of 50 volunteers at a shopping center for a one-sample t-test about a population mean. Which condition is violated?", choices=[
   "The randomization condition, because the sample was not chosen at random and not produced by a randomized experiment",
   "The 10 percent condition, because volunteers cannot be counted",
   "The sample data condition, because 50 is greater than 30",
   "No condition is violated, since 50 is a large sample",
   "All three conditions are violated"], ans=0,
   why="A large sample does not repair a non-random selection; without randomization the sampling distribution the test relies on does not describe how the data arose."),

 dict(q="For a one-sample t-test with H0: mu = 100, which alternative would a researcher use who wants evidence that a training program raised the mean above 100?", choices=[
   "Ha: mu > 100",
   "Ha: mu < 100",
   "Ha: mu is not equal to 100",
   "Ha: mu = 100",
   "Ha: mu_d > 0"], ans=0,
   why="Evidence of an increase calls for a one-sided upper-tail alternative; mu_d applies to a paired design, which this is not."),

 dict(q="A one-sample t-test uses 41 matched-pair differences. What are the degrees of freedom?", choices=[
   "39",
   "40",
   "41",
   "80",
   "82"], ans=1,
   why="The sample consists of the 41 differences, so df = 41 - 1 = 40; 80 would be a two-sample figure and does not apply to a paired design."),

 dict(q="Which situation calls for a one-sample t-test for a population mean rather than for a population mean difference?", choices=[
   "A random sample of 30 loaves is weighed once each and compared with the labeled weight of 800 grams",
   "Thirty loaves are weighed before baking and again after baking",
   "Thirty tasters each rate two recipes",
   "Fifteen loaves from oven A and fifteen from oven B are weighed",
   "Thirty students each take a pretest and a posttest"], ans=0,
   why="Only the first has a single measurement per unit compared against a fixed claimed value; the second, third and fifth are paired, and the fourth is two independent samples."),

 dict(q="A researcher writes H0: mu = 25 and Ha: mu < 25, then collects a random sample of 9 observations from a population described as approximately normal. Is the sample data condition met?", choices=[
   "Yes, because the population is stated to be approximately normal, which satisfies the condition at any sample size",
   "No, because n = 9 is well below 30",
   "No, because a one-sided test requires n of at least 30",
   "Yes, because the sample is random",
   "It cannot be determined without the sample standard deviation"], ans=0,
   why="CED 4.4.C.1.iii lists an approximately normal population as the first route to the sample data condition, and it carries no sample-size requirement; randomness is a separate condition."),

 dict(q="A researcher plans a matched-pairs t-test on 22 differences and finds that the differences are strongly skewed with two outliers. What is the appropriate response?", choices=[
   "The sample data condition is not met, because with fewer than 30 differences the differences must be free from strong skewness and outliers",
   "The condition is met, because 22 pairs means 44 measurements, which exceeds 30",
   "The condition is met, because skewness in the differences is irrelevant to a paired test",
   "The condition fails only if the two original samples are also skewed",
   "The researcher should switch to a two-sample t-test, which has no such condition"], ans=0,
   why="The paired analysis has one sample of 22 differences, so the below-30 branch applies to those differences; counting the 44 raw measurements is exactly the error the paired design removes."),
]
