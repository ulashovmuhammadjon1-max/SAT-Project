# AP STATISTICS 2.11 The Normal Distribution — 25 questions
# CED: Fall 2026, Unit 2. Skills 3.C (calculate probabilities), 3.D (calculate
# means, standard deviations and parameters for probability distributions) and
# 4.C (describe distributions and compare relative positions within one).
#
# A graphing calculator with statistical capabilities is EXPECTED on this exam
# and normal tables are supplied, so items here may require a normal probability
# that only technology or a table gives. What they must not require is a reading
# so fine that the answer depends on which table edition a student holds, so
# every keyed probability is separated from its nearest distractor by far more
# than any table-versus-calculator discrepancy.
#
# Two distributions carry the work:
#   scores  mean 500, standard deviation 100
#   heights mean  68, standard deviation   3 (inches)
#
# The empirical rule (about 68%, 95% and 99.7% within one, two and three
# standard deviations) is tested as an approximation and is checked against the
# exact normal values in verify_s2_11.py, which is also where the difference
# between the two is quantified.
#
# The recurring error targeted here is running the standardization backwards:
# finding a VALUE from a percentile needs x = mu + z(sigma), and students who
# have only ever gone forwards divide instead of multiplying.
TOPIC = ("2.11", "The Normal Distribution", 2)

QUESTIONS = [
 dict(q="A normal distribution is",
   choices=[
     "symmetric, unimodal, and bell-shaped, fully determined by its mean and standard deviation",
     "always skewed to the right",
     "a distribution in which every value is equally likely",
     "a distribution of counts rather than measurements",
     "any distribution with mean 0"],
   ans=0,
   why="A normal curve is a symmetric bell, and naming its mean and standard deviation names the curve completely."),

 dict(q="The standard normal distribution has",
   choices=[
     "mean 0 and standard deviation 1",
     "mean 1 and standard deviation 0",
     "mean 100 and standard deviation 15",
     "mean equal to its standard deviation",
     "no mean"],
   ans=0,
   why="Standardizing any normal variable produces the standard normal, centred at 0 with spread 1."),

 dict(q="According to the empirical rule, approximately what percent of the values of a normal distribution lie within one standard deviation of the mean?",
   choices=["50%", "68%", "75%", "95%", "99.7%"],
   ans=1,
   why="The empirical rule gives about 68 percent within one standard deviation, about 95 percent within two, and about 99.7 percent within three."),

 dict(q="According to the empirical rule, approximately what percent of the values of a normal distribution lie within two standard deviations of the mean?",
   choices=["68%", "75%", "90%", "95%", "99.7%"],
   ans=3,
   why="About 95 percent of a normal distribution lies within two standard deviations of the mean."),

 dict(q="According to the empirical rule, approximately what percent of the values of a normal distribution lie within three standard deviations of the mean?",
   choices=["68%", "95%", "99.7%", "100%", "99.0%"],
   ans=2,
   why="About 99.7 percent lies within three standard deviations, which is why a value beyond that is treated as remarkable."),

 dict(q="Scores on a test are normally distributed with mean 500 and standard deviation 100. What is the z-score of a score of 650?",
   choices=["-1.50", "0.65", "1.50", "6.50", "150.00"],
   ans=2,
   why="z = (650 - 500)/100 = 1.50, so the score lies one and a half standard deviations above the mean."),

 dict(q="Scores are normally distributed with mean 500 and standard deviation 100. What proportion of scores are below 650?",
   choices=["0.067", "0.401", "0.500", "0.933", "0.966"],
   ans=3,
   why="The z-score is 1.50, and the area to its left under the standard normal curve is 0.933."),

 dict(q="Scores are normally distributed with mean 500 and standard deviation 100. What proportion of scores are above 420?",
   choices=["0.212", "0.288", "0.500", "0.712", "0.788"],
   ans=4,
   why="z = (420 - 500)/100 = -0.80, and the area to the right of -0.80 is 0.788."),

 dict(q="Scores are normally distributed with mean 500 and standard deviation 100. What proportion of scores fall between 450 and 600?",
   choices=["0.150", "0.309", "0.533", "0.691", "0.841"],
   ans=2,
   why="The z-scores are -0.50 and 1.00, and the area between them is 0.841 - 0.309 = 0.533."),

 dict(q="Scores are normally distributed with mean 500 and standard deviation 100. A score at the 90th percentile is closest to",
   choices=["500", "590", "628", "656", "690"],
   ans=2,
   why="The 90th percentile of the standard normal is z = 1.282, so x = 500 + 1.282(100) = 628."),

 dict(q="Scores are normally distributed with mean 500 and standard deviation 100. A score at the 25th percentile is closest to",
   choices=["375", "400", "433", "467", "475"],
   ans=2,
   why="The 25th percentile of the standard normal is z = -0.674, so x = 500 + (-0.674)(100) = 433."),

 dict(q="To find the value x in a normal distribution that corresponds to a given z-score, the correct formula is",
   choices=[
     "x = mu + z(sigma)",
     "x = mu - z(sigma)",
     "x = z(mu) + sigma",
     "x = (z - mu)/sigma",
     "x = sigma + z/mu"],
   ans=0,
   why="Solving z = (x - mu)/sigma for x multiplies the z-score by the standard deviation and adds the mean; dividing instead is the standard error here."),

 dict(q="Adult heights in a population are normally distributed with mean 68 inches and standard deviation 3 inches. What proportion of adults are taller than 72 inches?",
   choices=["0.091", "0.159", "0.250", "0.500", "0.909"],
   ans=0,
   why="z = (72 - 68)/3 = 1.333, and the area to the right of 1.333 is 0.091."),

 dict(q="For those heights with mean 68 inches and standard deviation 3 inches, what proportion of adults are shorter than 65 inches?",
   choices=["0.091", "0.159", "0.250", "0.500", "0.841"],
   ans=1,
   why="z = (65 - 68)/3 = -1.00, and the area to the left of -1.00 is 0.159."),

 dict(q="For those heights with mean 68 inches and standard deviation 3 inches, the height that separates the tallest 10% from the rest is closest to",
   choices=["68.0 inches", "70.0 inches", "71.8 inches", "73.7 inches", "77.0 inches"],
   ans=2,
   why="The 90th percentile has z = 1.282, so the cutoff is 68 + 1.282(3) = 71.8 inches."),

 dict(q="For those heights with mean 68 inches and standard deviation 3 inches, the empirical rule says that about 95% of adults have heights between",
   choices=[
     "65 and 71 inches",
     "62 and 74 inches",
     "59 and 77 inches",
     "66.5 and 69.5 inches",
     "68 and 74 inches"],
   ans=1,
   why="Two standard deviations is 6 inches, so the interval is 68 - 6 to 68 + 6, that is 62 to 74 inches."),

 dict(q="A value in a normal distribution has a z-score of -2.00. This value is",
   choices=[
     "two standard deviations below the mean, and lower than about 97.7% of the distribution",
     "two standard deviations below the mean, and lower than about 2.3% of the distribution",
     "two standard deviations above the mean",
     "equal to twice the mean",
     "impossible in a normal distribution"],
   ans=1,
   why="Only about 2.3 percent of a normal distribution lies below z = -2.00, so the value sits below about 2.3 percent and above the other 97.7 percent."),

 dict(q="Two students take different normally distributed exams. Ana scores 1.8 standard deviations above her exam's mean; Ben scores 1.2 standard deviations above his. Relative to their own exams,",
   choices=[
     "Ana performed better, because a larger z-score corresponds to a higher percentile in any normal distribution",
     "Ben performed better, because a smaller z-score is preferable",
     "they performed identically",
     "no comparison is possible without the raw scores",
     "no comparison is possible without the two means"],
   ans=0,
   why="Standardizing puts both on the same scale, and in a normal distribution the percentile increases with the z-score."),

 dict(q="In a normal distribution, the mean, median, and mode are",
   choices=[
     "all equal, at the centre of the distribution",
     "all different",
     "equal only when the standard deviation is 1",
     "equal only when the mean is 0",
     "impossible to determine"],
   ans=0,
   why="A normal curve is symmetric and unimodal, so the balance point, the middle value and the peak coincide."),

 dict(q="Changing the standard deviation of a normal distribution while keeping the mean fixed",
   choices=[
     "shifts the curve left or right",
     "changes how spread out the curve is without moving its centre",
     "changes the total area under the curve",
     "makes the curve asymmetric",
     "has no visible effect"],
   ans=1,
   why="The mean locates the curve and the standard deviation controls its width; the area under any normal curve is always 1."),

 dict(q="The total area under any normal curve is",
   choices=["0", "0.5", "1", "the standard deviation", "the mean"],
   ans=2,
   why="A normal curve is a probability distribution, so the area beneath it accounts for all of the probability."),

 dict(q="For a continuous random variable such as a normal one, P(X = 500) equals",
   choices=[
     "0, because a single point has no area beneath the curve",
     "0.5",
     "the height of the curve at 500",
     "1",
     "the same as P(X <= 500)"],
   ans=0,
   why="Probability for a continuous variable is area over an interval, and a single point spans no interval; this is why P(X < 500) and P(X <= 500) are equal here, unlike in the discrete case."),

 dict(q="Scores are normally distributed with mean 500 and standard deviation 100. Approximately what percent of scores lie between 400 and 600?",
   choices=["34%", "50%", "68%", "95%", "99.7%"],
   ans=2,
   why="400 and 600 are exactly one standard deviation either side of the mean, so the empirical rule gives about 68 percent."),

 dict(q="A distribution of incomes is strongly skewed to the right. Using normal-curve calculations to find the proportion of incomes above a given value would be",
   choices=[
     "appropriate, because any large data set is normal",
     "inappropriate, because normal calculations assume a symmetric bell shape that this distribution does not have",
     "appropriate, provided the mean is known",
     "appropriate, because incomes are quantitative",
     "inappropriate only if there are outliers"],
   ans=1,
   why="Normal probabilities are areas under a symmetric bell, so applying them to a strongly skewed distribution gives answers that do not describe the data."),

 dict(q="A student needs the score separating the bottom 15% of a normal distribution and computes it as mu - 1.04/sigma. This is wrong because the correct expression is",
   choices=[
     "mu - 1.04(sigma), since the z-score is multiplied by the standard deviation, not divided into it",
     "mu + 1.04(sigma)",
     "mu/1.04 - sigma",
     "1.04(mu) - sigma",
     "sigma - 1.04(mu)"],
   ans=0,
   why="Rearranging z = (x - mu)/sigma gives x = mu + z(sigma), so a z-score of -1.04 produces mu - 1.04 times sigma."),
]
