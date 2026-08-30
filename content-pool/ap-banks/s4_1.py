# AP STATISTICS 4.1 Sampling Distributions for Sample Means - 25 questions
# CED: AP Statistics Course and Exam Description, Effective Fall 2026, Unit 4.
# Learning objectives 4.1.A (mean and standard deviation of the sampling
# distribution of xbar), 4.1.B (justify the conditions), 4.1.C (interpret).
# The CED's conditions, verbatim in substance: the randomization condition; the
# 10% condition n <= 0.10N when sampling without replacement; and normality,
# which holds for any n if the population is normal and approximately for
# n >= 30 otherwise, with more needed if the population is extremely skewed.
# Every probability, z-score and standard deviation is recomputed in
# verify_s4_1.py with scipy.stats.norm.
TOPIC = ("4.1", "Sampling Distributions for Sample Means", 4)
QUESTIONS = [

 dict(q="A population has mean 68 and standard deviation 12. Random samples of size 36 are drawn. What are the mean and standard deviation of the sampling distribution of the sample mean?", choices=[
   "mean 68, standard deviation 0.33",
   "mean 68, standard deviation 2",
   "mean 68, standard deviation 12",
   "mean 11.33, standard deviation 2",
   "mean 2448, standard deviation 12"], ans=1,
   why="The sampling distribution of xbar is centered at the population mean 68, and its standard deviation is sigma/sqrt(n) = 12/sqrt(36) = 2."),

 dict(q="Scores on a placement exam are normally distributed with mean 500 and standard deviation 80. A random sample of 25 test takers is selected. What is the probability that the sample mean score exceeds 520?", choices=[
   "0.0062",
   "0.1056",
   "0.2500",
   "0.4013",
   "0.8944"], ans=1,
   why="The standard deviation of xbar is 80/sqrt(25) = 16, so z = (520 - 500)/16 = 1.25 and the upper-tail probability is 0.1056; 0.4013 is what you get by using sigma = 80 instead of 16."),

 dict(q="The distribution of repair costs at a garage is strongly right-skewed. A manager plans to use a normal model for the sampling distribution of the mean cost of a random sample of 12 repairs. Is that appropriate?", choices=[
   "No, because the population is not normal and n = 12 is below 30, so the central limit theorem does not yet apply",
   "No, because a normal model may never be used for a skewed population no matter how large the sample",
   "Yes, because the sample was random",
   "Yes, because the sampling distribution of a sample mean is always normal",
   "Yes, because 12 repairs is fewer than 10 percent of all repairs"], ans=0,
   why="Normality for xbar comes either from a normal population or from a large enough sample; with a strongly skewed population and n = 12 neither route is available, though a much larger n would work."),

 dict(q="A quality inspector takes a simple random sample of 100 bolts, without replacement, from a shipment containing 800 bolts. Which condition for modeling the sampling distribution of the sample mean fails?", choices=[
   "The 10 percent condition, because 100 is more than 10 percent of 800",
   "The 10 percent condition, because 800 is more than 10 times 100",
   "The randomization condition, because the sample was taken without replacement",
   "The large counts condition, because 100 times the proportion is less than 10",
   "None of the conditions fails"], ans=0,
   why="The 10 percent condition requires n <= 0.10N, that is 100 <= 80, which is false; sampling 12.5 percent of the shipment without replacement makes the observations non-independent enough to matter."),

 dict(q="A population has standard deviation 20. If the sample size is quadrupled from 25 to 100, the standard deviation of the sampling distribution of the sample mean", choices=[
   "is cut in half, from 4 to 2",
   "is cut to one quarter, from 4 to 1",
   "is unchanged at 20",
   "is doubled, from 4 to 8",
   "is quadrupled, from 4 to 16"], ans=0,
   why="Because sigma/sqrt(n) divides by the square root of the sample size, multiplying n by 4 divides the standard deviation by 2: 20/5 = 4 becomes 20/10 = 2."),

 dict(q="A population has standard deviation 9. What is the smallest sample size for which the standard deviation of the sampling distribution of the sample mean is at most 1.5?", choices=[
   "6",
   "14",
   "36",
   "54",
   "81"], ans=2,
   why="Solving 9/sqrt(n) <= 1.5 gives sqrt(n) >= 6, so n >= 36; the answer 6 comes from stopping at sqrt(n)."),

 dict(q="The number of text messages a teenager sends per day has mean 3.2 and standard deviation 1.1, with a right-skewed distribution. For a random sample of 50 teenagers, what is the approximate probability that the sample mean is less than 3.0?", choices=[
   "0.0993",
   "0.1841",
   "0.4279",
   "0.5721",
   "0.9007"], ans=0,
   why="With n = 50 >= 30 the central limit theorem applies; the standard deviation of xbar is 1.1/sqrt(50) = 0.1556, so z = (3.0 - 3.2)/0.1556 = -1.29 and the probability is about 0.0993."),

 dict(q="A population is normally distributed with mean 60 and standard deviation 8. For a random sample of 16 observations, what is the z-score of a sample mean of 63?", choices=[
   "0.375",
   "0.75",
   "1.50",
   "3.00",
   "6.00"], ans=2,
   why="The standard deviation of xbar is 8/sqrt(16) = 2, so z = (63 - 60)/2 = 1.50; 0.375 uses sigma = 8 in the denominator."),

 dict(q="A population is normally distributed with mean 250 and standard deviation 40. For random samples of size 16, what value does the sample mean exceed only 10 percent of the time?", choices=[
   "255.1",
   "258.4",
   "262.8",
   "271.3",
   "301.3"], ans=2,
   why="The standard deviation of xbar is 40/4 = 10, and the 90th percentile of the standard normal is 1.2816, so the value is 250 + 1.2816(10) = 262.8; 301.3 uses sigma = 40."),

 dict(q="Which of the following describes the sampling distribution of a sample mean?", choices=[
   "The distribution of the values of xbar over all possible random samples of a fixed size from the population",
   "The distribution of the individual observations in one particular sample",
   "The distribution of the individual values in the whole population",
   "The distribution of the sample sizes used by a group of researchers",
   "The distribution of the differences between each observation and the population mean"], ans=0,
   why="A sampling distribution is a distribution of a statistic across all possible samples of one size, not a distribution of individual data values."),

 dict(q="The lifetimes of a brand of light bulb are normally distributed. A researcher takes random samples of only 5 bulbs. Which statement about the sampling distribution of the sample mean lifetime is correct?", choices=[
   "It is exactly normal, because a normal population gives a normal sampling distribution for any sample size",
   "It is approximately normal only because 5 is a small number relative to the population",
   "It cannot be modeled as normal, because n is below 30",
   "It is right-skewed, because small samples produce skewed statistics",
   "It is normal only if the sample standard deviation is close to the population standard deviation"], ans=0,
   why="CED 4.1.B.2: if the population itself is normal, the sampling distribution of xbar is normal regardless of n; the n >= 30 rule is the fallback for populations that are not normal."),

 dict(q="What does the central limit theorem say?", choices=[
   "For a large enough sample size, the sampling distribution of the sample mean is approximately normal even when the population is not",
   "For a large enough sample size, the population distribution becomes approximately normal",
   "As the sample size grows, the sample mean gets closer to the sample median",
   "Any sample of size at least 30 is representative of its population",
   "The mean of a large sample equals the population mean exactly"], ans=0,
   why="The theorem is about the sampling distribution of the statistic, not about the population, and it never promises that one sample mean equals the parameter."),

 dict(q="A population has standard deviation 2.5. For random samples of size 64, what is the standard deviation of the sampling distribution of the sample mean?", choices=[
   "0.0391",
   "0.3125",
   "0.6250",
   "2.5000",
   "20.0000"], ans=1,
   why="2.5/sqrt(64) = 2.5/8 = 0.3125; 0.0391 divides by 64 instead of by its square root."),

 dict(q="Daily rainfall totals at a station have mean 120 mm and standard deviation 15 mm, and the distribution is approximately normal. For a random sample of 36 days, what is the probability that the sample mean total is between 118 mm and 124 mm?", choices=[
   "0.1585",
   "0.2119",
   "0.5934",
   "0.7333",
   "0.9545"], ans=3,
   why="The standard deviation of xbar is 15/6 = 2.5, so the interval runs from z = -0.8 to z = 1.6, and the area between them is 0.7333."),

 dict(q="A student is told that the standard deviation of the sampling distribution of the sample mean is 1.6 for random samples of size 25. What is the population standard deviation?", choices=[
   "0.32",
   "1.60",
   "6.40",
   "8.00",
   "40.00"], ans=3,
   why="From sigma/sqrt(25) = 1.6, sigma = 1.6 x 5 = 8.00; multiplying by 25 instead of by 5 gives 40."),

 dict(q="A population is normally distributed with mean 7.5 grams and standard deviation 0.8 grams. For a random sample of 4 items, what is the probability that the sample mean exceeds 7.9 grams?", choices=[
   "0.0228",
   "0.1587",
   "0.3085",
   "0.6915",
   "0.8413"], ans=1,
   why="The standard deviation of xbar is 0.8/2 = 0.4, so z = (7.9 - 7.5)/0.4 = 1.00 and the upper-tail probability is 0.1587; 0.3085 uses sigma = 0.8."),

 dict(q="A population has mean 50 and standard deviation 6. A student computes the probability that the mean of a random sample of 9 observations exceeds 52 by finding the area above z = (52 - 50)/6. What is wrong, and what is the correct probability?", choices=[
   "Nothing is wrong; the probability is 0.3694",
   "The student should have divided 6 by 9; the probability is 0.0013",
   "The student should have divided 6 by 3; the probability is 0.1587",
   "The student should have multiplied 6 by 3; the probability is 0.4562",
   "The student should have used the sample standard deviation; the probability cannot be found"], ans=2,
   why="The standard deviation of xbar is sigma/sqrt(n) = 6/3 = 2, not sigma = 6, so z = 1.00 and the probability is 0.1587 rather than the student's 0.3694."),

 dict(q="Which statement correctly interprets a standard deviation of 2.4 minutes for the sampling distribution of the mean wait time in random samples of 40 customers?", choices=[
   "In repeated random samples of 40 customers, the sample mean wait time typically varies about 2.4 minutes from the population mean wait time",
   "About 2.4 minutes is the typical distance of an individual customer's wait time from the population mean",
   "The mean wait time of any single sample of 40 customers will be within 2.4 minutes of the population mean",
   "About 2.4 percent of samples of 40 customers will have a mean far from the population mean",
   "The population mean wait time is 2.4 minutes"], ans=0,
   why="The standard deviation of a sampling distribution describes how much the statistic varies from sample to sample around the parameter, not how individual observations vary and not a guarantee about any one sample."),

 dict(q="Increasing the sample size from 25 to 100 while sampling from the same population changes the sampling distribution of the sample mean in which way?", choices=[
   "Same center, smaller spread",
   "Same center, larger spread",
   "Center shifted upward, same spread",
   "Center shifted toward the sample mean, smaller spread",
   "Same center and same spread, because the population has not changed"], ans=0,
   why="The mean of the sampling distribution stays at the population mean for every n, while the standard deviation sigma/sqrt(n) shrinks as n grows."),

 dict(q="A population has mean 100 and standard deviation 20. Consider the probability that a sample mean falls within 4 units of 100. Which sample size gives the larger probability, and what are the two probabilities?", choices=[
   "n = 100, with 0.9545 against 0.6827 for n = 25",
   "n = 25, with 0.9545 against 0.6827 for n = 100",
   "n = 100, with 0.6827 against 0.4772 for n = 25",
   "They are equal, both 0.6827",
   "n = 25, because a smaller sample varies less"], ans=0,
   why="For n = 25 the standard deviation of xbar is 4, so 4 units is one standard deviation and the probability is 0.6827; for n = 100 it is 2, so 4 units is two standard deviations and the probability is 0.9545."),

 dict(q="A researcher samples 200 employees at random from a company with 15,000 employees. Which conditions for the sampling distribution of the sample mean salary are satisfied?", choices=[
   "Randomization is satisfied and the 10 percent condition is satisfied, since 200 is well under 1,500",
   "Randomization is satisfied but the 10 percent condition fails, since 200 is more than 10 percent of 15,000",
   "The 10 percent condition is satisfied but randomization fails, since employees are not independent",
   "Neither condition is satisfied",
   "Only the large counts condition matters for a sample mean"], ans=0,
   why="The sample was chosen at random, and n = 200 is far below 10 percent of the population, which is 1,500; the large counts condition applies to proportions, not to means."),

 dict(q="Which of the following is NOT a condition the CED gives for modeling the sampling distribution of a sample mean with a normal distribution?", choices=[
   "The population standard deviation must be known",
   "The data should be collected using a random sample",
   "The sample size should be no more than 10 percent of the population when sampling without replacement",
   "The population should be normal, or the sample size should be at least 30",
   "A more extreme skew in the population calls for a sample size well above 30"], ans=0,
   why="Knowing sigma is not a condition for the shape of the sampling distribution; it only determines whether the standard deviation of xbar can be computed exactly or must be estimated."),

 dict(q="Two researchers sample from the same population, one using n = 40 and the other n = 400. Which statement about the two sampling distributions of the sample mean is correct?", choices=[
   "They have the same mean, and the n = 400 distribution has one tenth the variance of the n = 40 distribution",
   "They have the same mean, and the n = 400 distribution has one tenth the standard deviation of the n = 40 distribution",
   "The n = 400 distribution has a mean 10 times larger and the same standard deviation",
   "The n = 400 distribution has a mean one tenth as large and one tenth the standard deviation",
   "They are identical, because the population is the same"], ans=0,
   why="Both center on the population mean; the variance is sigma^2/n, so a tenfold increase in n divides the variance by 10 while dividing the standard deviation only by sqrt(10)."),

 dict(q="A population of 9,000 tree heights is extremely right-skewed. A forester takes a random sample of 30 trees and models the sampling distribution of the mean height as normal. What is the best critique?", choices=[
   "For an extremely skewed population, n = 30 may not be enough, and a substantially larger sample may be needed",
   "The model is fine, because n = 30 always guarantees normality of the sampling distribution",
   "The model is wrong, because 30 is more than 10 percent of 9,000",
   "The model is wrong, because the sampling distribution of a mean can never be normal",
   "The model is fine, because the sample itself will look normal"], ans=0,
   why="CED 4.1.B.3 says explicitly that an extremely skewed population may need a sample size much larger than 30; n = 30 is a rule of thumb, not a guarantee, and 30 is well under 10 percent of 9,000."),

 dict(q="An analyst reports that the sampling distribution of the sample mean has mean 45 and standard deviation 3, based on samples of size 49. What is the population mean, and what is the population standard deviation?", choices=[
   "mean 45, standard deviation 21",
   "mean 45, standard deviation 3",
   "mean 45, standard deviation 0.43",
   "mean 6.43, standard deviation 21",
   "mean 315, standard deviation 147"], ans=0,
   why="The sampling distribution is centered at the population mean, so mu = 45, and sigma = 3 x sqrt(49) = 21."),
]
