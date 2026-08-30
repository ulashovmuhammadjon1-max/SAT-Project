# AP STATISTICS 1.9 Comparisons of the Distributions for One Quantitative
# Variable — 25 questions
# CED: Fall 2026, Unit 1. Learning objectives 1.9.A and 1.9.B (compare two or
# more distributions graphically and by their numerical summaries), 1.9.C
# (justify a claim from such a comparison), 1.9.D (calculate z-scores) and
# 1.9.E (use z-scores to compare relative position within or between
# distributions).
#
# The z-score is the computational core of this topic: z = (x - mu) / sigma.
# Items run it in all four directions -- solve for z, for x, for mu and for
# sigma -- because a student who has only ever solved for z tends to stall when
# the unknown moves. Every one is recomputed in verify_s1_9.py.
#
# The comparison items are deliberately built so that the answer does NOT follow
# from the raw score alone: in q13 the higher raw score has the WORSE relative
# position, which is the whole reason standardizing exists.
TOPIC = ("1.9", "Comparisons of the Distributions for One Quantitative Variable", 1)

QUESTIONS = [
 dict(q="A standardized score, or z-score, measures",
   choices=[
     "the percent of observations below a data value",
     "the number of standard deviations a data value falls above or below the mean",
     "the difference between the largest and smallest values",
     "the proportion of the data lying between the quartiles",
     "the number of observations in the data set"],
   ans=1,
   why="A z-score converts a value into a count of standard deviations from the mean, which is what makes values from different distributions comparable."),

 dict(q="The z-score of a data value x is calculated as",
   choices=[
     "(x - mu) / sigma",
     "(mu - x) / sigma",
     "(x - sigma) / mu",
     "x / (mu + sigma)",
     "(x - mu) x sigma"],
   ans=0,
   why="The deviation from the mean is divided by the standard deviation, so z = (x - mu)/sigma."),

 dict(q="A data value has a negative z-score. This tells you that the value is",
   choices=[
     "below the mean of its distribution",
     "above the mean of its distribution",
     "equal to the mean of its distribution",
     "an outlier",
     "impossible, since z-scores cannot be negative"],
   ans=0,
   why="The sign of a z-score is the sign of x - mu, so a negative z-score places the value below the mean."),

 dict(q="A data value has a z-score of exactly 0. This tells you that the value",
   choices=[
     "is equal to the mean of its distribution",
     "is equal to zero",
     "is the smallest value in the data set",
     "is the median of the distribution",
     "cannot occur"],
   ans=0,
   why="A z-score of 0 means x - mu = 0, so the value sits exactly at the mean; whether it is also the median depends on the shape of the distribution."),

 dict(q="Scores on an exam have a mean of 72 and a standard deviation of 8. What is the z-score of a score of 84?",
   choices=["-1.50", "0.86", "1.17", "1.50", "12.00"],
   ans=3,
   why="z = (84 - 72)/8 = 12/8 = 1.50, so the score is one and a half standard deviations above the mean."),

 dict(q="A distribution has a mean of 70 and a standard deviation of 6. What is the z-score of the value 58?",
   choices=["-2.00", "-1.20", "-0.50", "1.20", "2.00"],
   ans=0,
   why="z = (58 - 70)/6 = -12/6 = -2.00, so the value lies two standard deviations below the mean."),

 dict(q="Adult heights in a population have a mean of 170 cm and a standard deviation of 8 cm. What is the z-score of a height of 158 cm?",
   choices=["-1.50", "-1.20", "-0.75", "1.50", "12.00"],
   ans=0,
   why="z = (158 - 170)/8 = -12/8 = -1.50, so the height is one and a half standard deviations below the mean."),

 dict(q="A distribution has a mean of 25 and a standard deviation of 4. What is the z-score of the value 33?",
   choices=["-2.00", "0.50", "1.00", "2.00", "8.00"],
   ans=3,
   why="z = (33 - 25)/4 = 8/4 = 2.00."),

 dict(q="A distribution has a mean of 500 and a standard deviation of 100. What value has a z-score of 1.8?",
   choices=["320", "501.8", "518", "680", "900"],
   ans=3,
   why="Solving z = (x - mu)/sigma for x gives x = mu + z(sigma) = 500 + 1.8(100) = 680."),

 dict(q="A distribution has a mean of 250 and a standard deviation of 40. What value has a z-score of -0.75?",
   choices=["-30", "220", "249.25", "280", "310"],
   ans=1,
   why="x = mu + z(sigma) = 250 + (-0.75)(40) = 250 - 30 = 220."),

 dict(q="In a distribution with mean 76, the value 88 has a z-score of 1.5. What is the standard deviation of the distribution?",
   choices=["1.5", "6", "8", "12", "18"],
   ans=2,
   why="From z = (x - mu)/sigma, sigma = (x - mu)/z = (88 - 76)/1.5 = 12/1.5 = 8."),

 dict(q="In a distribution with standard deviation 6, the value 45 has a z-score of -0.5. What is the mean of the distribution?",
   choices=["39", "42", "45", "48", "51"],
   ans=3,
   why="From x = mu + z(sigma), mu = x - z(sigma) = 45 - (-0.5)(6) = 45 + 3 = 48."),

 dict(q="Maria scored 84 on Exam A, which had a mean of 72 and a standard deviation of 8. She scored 78 on Exam B, which had a mean of 65 and a standard deviation of 10. Relative to the other test takers, Maria performed better on",
   choices=[
     "Exam A, because her z-score of 1.50 exceeds her z-score of 1.30 on Exam B",
     "Exam B, because her z-score of 1.30 exceeds her z-score of 1.50 on Exam A",
     "Exam A, because 84 is a higher raw score than 78",
     "Exam B, because Exam B had the larger standard deviation",
     "neither, because the two exams cannot be compared"],
   ans=0,
   why="Standardizing gives z = (84 - 72)/8 = 1.50 on Exam A and z = (78 - 65)/10 = 1.30 on Exam B, so her relative standing was higher on Exam A."),

 dict(q="Devon ran a race in 52 seconds, where the field had a mean of 58 seconds and a standard deviation of 4 seconds. Priya ran a different race in 47 seconds, where that field had a mean of 51 seconds and a standard deviation of 5 seconds. Since a lower time is better, the runner with the better performance relative to their own field is",
   choices=[
     "Devon, whose z-score of -1.50 is further below the mean than Priya's -0.80",
     "Priya, whose z-score of -0.80 is further below the mean than Devon's -1.50",
     "Devon, because 52 seconds is slower than 47 seconds",
     "Priya, because her raw time of 47 seconds is the lower of the two",
     "neither, because z-scores cannot be negative"],
   ans=0,
   why="Devon's z is (52 - 58)/4 = -1.50 and Priya's is (47 - 51)/5 = -0.80, and with lower times better, the more negative z-score is the stronger performance."),

 dict(q="Two students take different tests. Student 1 scores 90 on a test with mean 85 and standard deviation 2. Student 2 scores 95 on a test with mean 80 and standard deviation 10. Which statement is correct?",
   choices=[
     "Student 2 did better relative to their group, because 95 is the higher raw score",
     "Student 1 did better relative to their group, with a z-score of 2.5 against Student 2's 1.5",
     "Both students did equally well relative to their groups",
     "Student 2 did better relative to their group, with a z-score of 2.5",
     "The comparison is impossible without knowing the sample sizes"],
   ans=1,
   why="Student 1's z is (90 - 85)/2 = 2.5 and Student 2's is (95 - 80)/10 = 1.5, so the LOWER raw score carries the better relative position."),

 dict(q="Which of the following is true of z-scores?",
   choices=[
     "They have the same units as the original data",
     "They are unitless, because the units of the numerator and the denominator cancel",
     "They must always lie between 0 and 1",
     "They can only be computed for symmetric distributions",
     "They are always whole numbers"],
   ans=1,
   why="Both x - mu and sigma carry the variable's units, so dividing leaves a pure number, which is precisely why z-scores compare across different variables."),

 dict(q="Every value in a data set is converted to a z-score. The resulting set of z-scores has",
   choices=[
     "mean 0 and standard deviation 1",
     "mean 1 and standard deviation 0",
     "the same mean and standard deviation as the original data",
     "mean 0 and standard deviation equal to the original standard deviation",
     "mean equal to the original mean and standard deviation 1"],
   ans=0,
   why="Subtracting the mean centres the data at 0 and dividing by the standard deviation rescales the spread to 1."),

 dict(q="Standardizing a data set into z-scores does NOT change",
   choices=[
     "the mean of the data",
     "the standard deviation of the data",
     "the shape of the distribution",
     "the units of the data",
     "the numerical value of any observation"],
   ans=2,
   why="Standardizing is a linear transformation, so it slides and rescales the distribution but leaves its shape, including any skewness, exactly as it was."),

 dict(q="Which graphical display is specifically designed for comparing the distributions of one quantitative variable between exactly two groups?",
   choices=[
     "A pie chart",
     "A back-to-back stem-and-leaf plot",
     "A single dotplot of the combined groups",
     "A frequency table of one group",
     "A scatterplot"],
   ans=1,
   why="A back-to-back stem-and-leaf plot shares one column of stems between two groups so their distributions can be read against each other directly."),

 dict(q="Parallel boxplots of the same quantitative variable for several groups are useful for comparing",
   choices=[
     "centre, variability, outliers, and skewness across the groups",
     "the number of observations in each group",
     "whether any group's distribution is bimodal",
     "the exact values of every observation",
     "the mean of each group"],
   ans=0,
   why="Boxplots display the five-number summary, which reveals centre, spread, outliers and skewness, but not sample size, modality, individual values or the mean."),

 dict(q="Two groups are compared with histograms of the same quantitative variable drawn on the same scale. Group 1 is centred near 40 with values spanning 30 to 50; Group 2 is centred near 40 with values spanning 10 to 70. The best comparison is that the two groups have",
   choices=[
     "similar centres, with Group 2 far more variable",
     "similar centres, with Group 1 far more variable",
     "very different centres and similar variability",
     "identical distributions",
     "centres that cannot be compared from histograms"],
   ans=0,
   why="Both distributions sit around 40, so the centres are similar, while a span of 60 against a span of 20 makes Group 2 much more spread out."),

 dict(q="Two groups have the same mean but Group A has a much larger standard deviation than Group B. A value 5 units above the mean will have",
   choices=[
     "a larger z-score in Group A",
     "a larger z-score in Group B",
     "the same z-score in both groups",
     "a z-score of 5 in both groups",
     "a negative z-score in Group B"],
   ans=1,
   why="The same deviation of 5 is divided by a smaller standard deviation in Group B, producing the larger z-score and so the more unusual relative position."),

 dict(q="A manager compares monthly sales for two branches and reports: 'Branch X has a higher median, but Branch Y's interquartile range is much smaller.' The claim best justified by this comparison is that",
   choices=[
     "Branch X sells more in a typical month, while Branch Y's monthly sales are more consistent",
     "Branch Y sells more in a typical month",
     "Branch X has more employees",
     "the two branches have identical distributions",
     "Branch Y has more outliers"],
   ans=0,
   why="A higher median means a higher typical value and a smaller IQR means less month-to-month variability; nothing here speaks to staffing or outliers."),

 dict(q="When comparing two distributions of the same quantitative variable, a complete comparison should address",
   choices=[
     "centre only",
     "centre and variability only",
     "shape, centre, variability, and unusual features, with explicit comparative language",
     "the sample sizes only",
     "whichever single feature differs the most"],
   ans=2,
   why="A comparison covers the same four elements as a description of one distribution, and it must actually compare them rather than describe each group separately."),

 dict(q="A value from Distribution 1 has a z-score of 1.2, and a value from Distribution 2 has a z-score of 1.2. It follows that",
   choices=[
     "the two values are numerically equal",
     "the two values occupy the same relative position within their own distributions, each 1.2 standard deviations above its own mean",
     "the two distributions have the same mean",
     "the two distributions have the same standard deviation",
     "both values are outliers"],
   ans=1,
   why="Equal z-scores say the two values stand equally far above their own means in standard-deviation units, and say nothing about the raw values or the distributions' parameters."),
]
