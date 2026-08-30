# AP STATISTICS 2.12 Sampling Distributions and the Central Limit Theorem
# — 25 questions
# CED: Fall 2026, Unit 2. Skill 4.C, describing distributions and comparing
# relative positions of points within a distribution.
#
# A sampling distribution is the distribution of a STATISTIC over all possible
# samples of a fixed size. Three separate facts about the sampling distribution
# of the sample mean are tested, and students routinely merge them:
#   CENTRE  the mean of x-bar equals mu, whatever n is -- x-bar is unbiased;
#   SPREAD  the standard deviation of x-bar is sigma / sqrt(n), so it shrinks as
#           n grows, and shrinks with the SQUARE ROOT, which is why quadrupling
#           n only halves it;
#   SHAPE   normal for any n if the population is normal; approximately normal
#           for large n whatever the population's shape, by the CLT.
#
# The misconception this module attacks hardest: the CLT says nothing about the
# distribution of the POPULATION, and nothing about the distribution of the DATA
# IN ONE SAMPLE. A large sample from a skewed population still looks skewed; it
# is the distribution of x-bar across many such samples that becomes normal.
# Four items separate those three distributions explicitly.
#
# All values are recomputed in verify_s2_12.py, and the CLT items are checked by
# simulating the sampling distribution rather than by asserting the theorem.
TOPIC = ("2.12", "Sampling Distributions and the Central Limit Theorem", 2)

QUESTIONS = [
 dict(q="A sampling distribution is",
   choices=[
     "the distribution of the values in one sample",
     "the distribution of a statistic over all possible samples of a given size from a population",
     "the distribution of the values in the population",
     "the distribution of the sample sizes used in a study",
     "the distribution of the parameters of a population"],
   ans=1,
   why="A sampling distribution describes how a statistic such as x-bar varies from sample to sample, not how individual values vary."),

 dict(q="For samples of size n from a population with mean mu and standard deviation sigma, the mean of the sampling distribution of the sample mean is",
   choices=["mu", "mu divided by n", "mu times n", "sigma", "sigma divided by the square root of n"],
   ans=0,
   why="The sample mean is an unbiased estimator, so its sampling distribution centres on the population mean no matter what n is."),

 dict(q="For samples of size n from a population with mean mu and standard deviation sigma, the standard deviation of the sampling distribution of the sample mean is",
   choices=[
     "sigma",
     "sigma divided by n",
     "sigma divided by the square root of n",
     "sigma times the square root of n",
     "mu divided by the square root of n"],
   ans=2,
   why="Averaging n observations damps the variation by a factor of the square root of n."),

 dict(q="The Central Limit Theorem states that, for a sufficiently large sample size,",
   choices=[
     "the population becomes approximately normal",
     "the data within a single sample become approximately normal",
     "the sampling distribution of the sample mean is approximately normal, whatever the shape of the population",
     "the sample mean equals the population mean",
     "the standard deviation of the population shrinks"],
   ans=2,
   why="The theorem is about the distribution of x-bar across samples; it changes nothing about the population or about the data inside any one sample."),

 dict(q="A population is strongly skewed to the right. A single random sample of 200 observations is drawn from it. A histogram of those 200 observations will most likely appear",
   choices=[
     "approximately normal, because 200 is a large sample",
     "strongly skewed to the right, resembling the population",
     "approximately uniform",
     "skewed to the left",
     "impossible to predict"],
   ans=1,
   why="A large sample resembles the population it came from; it is the sampling distribution of x-bar, not the sample itself, that the CLT makes normal."),

 dict(q="A population is strongly skewed to the right, with mean 40. Many random samples of size 100 are drawn and the sample mean recorded for each. The distribution of those sample means will be",
   choices=[
     "strongly skewed to the right, like the population",
     "approximately normal, centred near 40",
     "approximately uniform",
     "centred near 4, since 40 divided by 10 is 4",
     "impossible to describe without the population standard deviation"],
   ans=1,
   why="With n = 100 the Central Limit Theorem makes the sampling distribution of x-bar approximately normal, and it is centred at the population mean of 40."),

 dict(q="If the population itself is normally distributed, the sampling distribution of the sample mean is",
   choices=[
     "normal for any sample size, however small",
     "normal only when n is at least 30",
     "never exactly normal",
     "skewed for small n",
     "uniform"],
   ans=0,
   why="Sampling from a normal population gives an exactly normal sampling distribution at every n; the CLT is needed only when the population is not normal."),

 dict(q="A population has mean 70 and standard deviation 12. For random samples of size 36, the standard deviation of the sampling distribution of the sample mean is",
   choices=["0.33", "2.00", "6.00", "12.00", "72.00"],
   ans=1,
   why="12 divided by the square root of 36 is 12/6 = 2.00."),

 dict(q="A population has mean 70 and standard deviation 12. For random samples of size 36, the mean of the sampling distribution of the sample mean is",
   choices=["2.00", "11.67", "36.00", "70.00", "420.00"],
   ans=3,
   why="The sampling distribution of x-bar centres on the population mean, 70, regardless of the sample size."),

 dict(q="A population has mean 70 and standard deviation 12, and the sampling distribution of the mean of samples of size 36 is approximately normal. What is the probability that a sample mean exceeds 73?",
   choices=["0.067", "0.159", "0.401", "0.599", "0.933"],
   ans=0,
   why="The standard deviation of x-bar is 2, so z = (73 - 70)/2 = 1.50 and the right-tail area is 0.067."),

 dict(q="For that same population with mean 70, standard deviation 12, and samples of size 36, what is the probability that a sample mean falls below 68?",
   choices=["0.067", "0.159", "0.401", "0.500", "0.841"],
   ans=1,
   why="z = (68 - 70)/2 = -1.00, and the area to the left of -1.00 is 0.159."),

 dict(q="A population has mean 250 and standard deviation 40. For random samples of size 100, the standard deviation of the sample mean is",
   choices=["0.40", "4.00", "10.00", "40.00", "400.00"],
   ans=1,
   why="40 divided by the square root of 100 is 40/10 = 4.00."),

 dict(q="A population has mean 250 and standard deviation 40, and samples of size 100 are drawn. What is the probability that a sample mean falls between 245 and 255?",
   choices=["0.099", "0.383", "0.500", "0.789", "0.950"],
   ans=3,
   why="The standard deviation of x-bar is 4, so the z-scores are -1.25 and 1.25 and the area between them is 0.789."),

 dict(q="A population has standard deviation 20. If the sample size is increased from 25 to 100, the standard deviation of the sampling distribution of the sample mean changes from",
   choices=[
     "4.00 to 2.00",
     "4.00 to 1.00",
     "0.80 to 0.20",
     "20.00 to 5.00",
     "4.00 to 4.00"],
   ans=0,
   why="20 over the square root of 25 is 4.00 and 20 over the square root of 100 is 2.00, so quadrupling n halves the standard deviation."),

 dict(q="Quadrupling the sample size divides the standard deviation of the sampling distribution of the sample mean by",
   choices=["1", "2", "4", "8", "16"],
   ans=1,
   why="The standard deviation is sigma over the square root of n, and the square root of 4 is 2, so the spread is halved rather than quartered."),

 dict(q="To halve the standard deviation of the sampling distribution of the sample mean, the sample size must be",
   choices=[
     "halved",
     "doubled",
     "multiplied by 4",
     "multiplied by 8",
     "left unchanged"],
   ans=2,
   why="Since the spread depends on the square root of n, cutting it in half requires four times as many observations."),

 dict(q="Increasing the sample size affects the sampling distribution of the sample mean by",
   choices=[
     "moving its centre closer to the population mean",
     "reducing its spread while leaving its centre at the population mean",
     "increasing its spread",
     "changing the population mean",
     "making it skewed"],
   ans=1,
   why="The sample mean is unbiased at every n, so a larger sample buys precision, not a correction to the centre."),

 dict(q="A population has mean 50 and standard deviation 8. For samples of size 64, what is the probability that the sample mean exceeds 52?",
   choices=["0.023", "0.159", "0.401", "0.500", "0.599"],
   ans=0,
   why="The standard deviation of x-bar is 8/8 = 1, so z = (52 - 50)/1 = 2.00 and the right-tail area is 0.023."),

 dict(q="The standard deviation of a sampling distribution is smaller than the standard deviation of the population because",
   choices=[
     "the population is always more variable than any sample",
     "averaging several observations lets high and low values offset one another, so means vary less than individual values do",
     "the sample size is subtracted from the population standard deviation",
     "sampling removes outliers",
     "the population standard deviation is unknown"],
   ans=1,
   why="An average of n observations is far less erratic than a single observation, and the factor by which it is less erratic is the square root of n."),

 dict(q="A researcher uses a biased sampling method and increases the sample size from 100 to 10,000. The effect on the sampling distribution of the resulting statistic is that",
   choices=[
     "it becomes centred on the true parameter",
     "its spread shrinks, but its centre remains away from the true parameter",
     "both its centre and its spread move to the correct values",
     "nothing changes",
     "it becomes skewed"],
   ans=1,
   why="Sample size governs the spread of a sampling distribution; where that distribution is centred is fixed by the method, so a bigger biased sample is only more precisely wrong."),

 dict(q="Which of the following is a parameter rather than a statistic in the context of a sampling distribution?",
   choices=[
     "The sample mean x-bar computed from one sample",
     "The population mean mu",
     "The sample standard deviation s",
     "The sample proportion p-hat",
     "The sample size n"],
   ans=1,
   why="mu describes the population and is a fixed number; x-bar, s and p-hat all vary from sample to sample, which is exactly what a sampling distribution displays."),

 dict(q="A sampling distribution of the sample mean has a smaller spread than the population it came from. Compared with the population's shape, the sampling distribution for large n is",
   choices=[
     "identical in shape",
     "closer to normal, even when the population is skewed",
     "more skewed",
     "always uniform",
     "impossible to compare"],
   ans=1,
   why="That is exactly what the Central Limit Theorem asserts: the sampling distribution moves toward normality as n grows, whatever shape the population has."),

 dict(q="A student claims that with a sample of 400 from a skewed population, the sample data will be normally distributed. The best correction is that",
   choices=[
     "the claim is right, since 400 is far above 30",
     "the sample data will still look skewed; it is the distribution of the sample MEAN across many samples of 400 that is approximately normal",
     "the population will become normal",
     "the claim is right only if the sample is random",
     "no sample of 400 can be drawn from a skewed population"],
   ans=1,
   why="Sample size makes the sampling distribution of x-bar normal; it does nothing to the shape of the values inside any one sample."),

 dict(q="Three distributions are involved when a sample is drawn: the population, the sample, and the sampling distribution of x-bar. Which has the smallest standard deviation, assuming n is greater than 1?",
   choices=[
     "The population",
     "The sample",
     "The sampling distribution of x-bar",
     "They are all equal",
     "It cannot be determined"],
   ans=2,
   why="The population and the sample both describe individual values and have comparable spread, while the sampling distribution describes averages and has spread sigma over the square root of n."),

 dict(q="A population has mean 70 and standard deviation 12. A single observation is drawn, and separately a sample of 36 is drawn and averaged. Compared with the single observation, the sample mean is",
   choices=[
     "equally likely to fall far from 70",
     "much more likely to fall close to 70, because its standard deviation is 2 rather than 12",
     "much more likely to fall far from 70",
     "centred on a different value",
     "not comparable to a single observation"],
   ans=1,
   why="A single value has the population's spread of 12, while the mean of 36 has spread 2, so the mean is concentrated far more tightly around 70."),
]
