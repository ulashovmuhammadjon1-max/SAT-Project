# AP STATISTICS 1.7 Summary Statistics for One Quantitative Variable — 25 questions
# CED: Fall 2026, Unit 1. Learning objectives 1.7.A (measures of centre and
# position), 1.7.B (measures of variability), 1.7.C (effect of changing units),
# 1.7.D (the two outlier rules), 1.7.E (comparing distributions) and 1.7.F
# (justifying a resistant summary).
#
# Three data sets carry the computation. All three have an EVEN number of values
# so that the quartiles are unambiguous: with n even, the lower half and the
# upper half each contain exactly n/2 values and no convention question arises
# about whether the median is included.
#   J  n = 12: 4 7 8 10 11 13 14 16 18 21 24 30
#        mean 14.67, median 13.5, Q1 9, Q3 19.5, IQR 10.5, range 26
#   K  n = 12: 20 22 23 24 25 26 27 28 29 30 31 62   (one high outlier)
#        median 26.5, Q1 23.5, Q3 29.5, IQR 6, fences 14.5 and 38.5
#        mean 28.92, s 10.93 -- BOTH outlier rules flag 62 and nothing else,
#        which is deliberate, so the two rules cannot disagree on this data set
#   L  n =  8: 2 4 4 4 5 5 7 9
#        mean 5, sample variance 32/7 = 4.571, sample s = 2.138
# Every value keyed below is recomputed in verify_s1_7.py with `statistics`.
TOPIC = ("1.7", "Summary Statistics for One Quantitative Variable", 1)

DATA_J = "4, 7, 8, 10, 11, 13, 14, 16, 18, 21, 24, 30"
DATA_K = "20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 62"
DATA_L = "2, 4, 4, 4, 5, 5, 7, 9"

QUESTIONS = [
 dict(q=f"A data set of twelve values, already in order, is {DATA_J}. What is the mean of this data set, rounded to two decimal places?",
   choices=["13.50", "14.67", "15.00", "16.00", "17.60"],
   ans=1,
   why="The twelve values total 176, and 176/12 = 14.67; 13.50 is the median, not the mean."),

 dict(q=f"For the data set {DATA_J}, what is the median?",
   choices=["11.0", "13.0", "13.5", "14.0", "14.67"],
   ans=2,
   why="With twelve values the median is the average of the 6th and 7th, which are 13 and 14, giving 13.5."),

 dict(q=f"For the data set {DATA_J}, what is the first quartile Q1?",
   choices=["8.0", "9.0", "10.0", "10.5", "11.0"],
   ans=1,
   why="Q1 is the median of the lower six values 4, 7, 8, 10, 11, 13, which is the average of 8 and 10, or 9."),

 dict(q=f"For the data set {DATA_J}, what is the third quartile Q3?",
   choices=["16.0", "18.0", "19.5", "21.0", "24.0"],
   ans=2,
   why="Q3 is the median of the upper six values 14, 16, 18, 21, 24, 30, which is the average of 18 and 21, or 19.5."),

 dict(q=f"For the data set {DATA_J}, what is the interquartile range?",
   choices=["6.0", "9.0", "10.5", "19.5", "26.0"],
   ans=2,
   why="The IQR is Q3 - Q1 = 19.5 - 9 = 10.5; 26 is the range, which is a different measure of spread."),

 dict(q=f"For the data set {DATA_J}, what is the range?",
   choices=["10.5", "14.0", "19.5", "26.0", "30.0"],
   ans=3,
   why="The range is the maximum minus the minimum, 30 - 4 = 26."),

 dict(q=f"A sample consists of the eight values {DATA_L}. What is the sample standard deviation, rounded to two decimal places?",
   choices=["2.00", "2.14", "4.00", "4.57", "5.00"],
   ans=1,
   why="The squared deviations from the mean of 5 total 32, and the square root of 32/7 is 2.14; 2.00 divides by n instead of n - 1."),

 dict(q=f"For that same sample {DATA_L}, what is the sample variance, rounded to two decimal places?",
   choices=["2.14", "4.00", "4.57", "5.00", "32.00"],
   ans=2,
   why="The sample variance is the sum of squared deviations divided by n - 1, or 32/7 = 4.57, and it is the square of the sample standard deviation."),

 dict(q="The sample standard deviation of a quantitative variable is best described as",
   choices=[
     "the difference between the largest and smallest values",
     "a typical deviation of the data values from their mean",
     "the middle value of the ordered data set",
     "the value that occurs most often",
     "the distance between the two quartiles"],
   ans=1,
   why="The standard deviation measures how far, typically, the observations fall from their mean."),

 dict(q="If every value in a data set is exactly the same number, then the standard deviation of the data set is",
   choices=["0", "1", "equal to the mean", "equal to the number of values", "undefined"],
   ans=0,
   why="Every deviation from the mean is zero, so the sum of squared deviations is zero and so is the standard deviation."),

 dict(q=f"A data set of twelve values is {DATA_K}. Using the 1.5 x IQR rule, what is the upper boundary above which a value is considered an outlier?",
   choices=["29.5", "32.5", "35.5", "38.5", "44.5"],
   ans=3,
   why="Q1 = 23.5 and Q3 = 29.5 give IQR = 6, so the upper boundary is Q3 + 1.5(6) = 29.5 + 9 = 38.5."),

 dict(q=f"For the data set {DATA_K}, using the 1.5 x IQR rule, which value or values are outliers?",
   choices=[
     "20 only",
     "62 only",
     "20 and 62",
     "31 and 62",
     "there are no outliers"],
   ans=1,
   why="The boundaries are 23.5 - 9 = 14.5 and 29.5 + 9 = 38.5; only 62 falls outside them, and the minimum 20 is comfortably above 14.5."),

 dict(q=f"For the data set {DATA_K}, what is the interquartile range?",
   choices=["3.0", "6.0", "9.0", "26.5", "42.0"],
   ans=1,
   why="Q3 - Q1 = 29.5 - 23.5 = 6.0; 42 is the range, which the outlier inflates."),

 dict(q=f"For the data set {DATA_K}, what is the median?",
   choices=["25.0", "26.0", "26.5", "28.92", "29.5"],
   ans=2,
   why="With twelve values the median averages the 6th and 7th, which are 26 and 27, giving 26.5; 28.92 is the mean, pulled up by the outlier."),

 dict(q="An alternative outlier rule declares a value an outlier when it lies more than two standard deviations from the mean. Compared with the 1.5 x IQR rule, this rule",
   choices=[
     "must always identify exactly the same values as outliers",
     "uses the mean and standard deviation, which are themselves affected by the extreme values being tested for",
     "can only be applied to symmetric distributions",
     "never identifies any value as an outlier",
     "requires the data set to have an even number of values"],
   ans=1,
   why="The two-standard-deviation rule is built from the mean and standard deviation, and an extreme value inflates both, so the rule is measured with a yardstick the outlier itself has bent."),

 dict(q="The pth percentile of a data set is the value that has",
   choices=[
     "p% of the data less than or equal to it when the data are ordered from smallest to largest",
     "p% of the data greater than it",
     "exactly p observations below it",
     "a value equal to p",
     "p% of the range below it"],
   ans=0,
   why="A percentile is a position measure: p percent of the ordered data sit at or below the pth percentile."),

 dict(q="The first quartile Q1 and the third quartile Q3 are the same as",
   choices=[
     "the 10th and 90th percentiles",
     "the 20th and 80th percentiles",
     "the 25th and 75th percentiles",
     "the 40th and 60th percentiles",
     "the minimum and maximum"],
   ans=2,
   why="Q1 is the 25th percentile and Q3 the 75th, and together they bound the middle 50 percent of the ordered data."),

 dict(q="A student's exam score is reported to be at the 90th percentile of all scores. This means that",
   choices=[
     "the student answered 90 percent of the questions correctly",
     "about 90 percent of the students who took the exam scored at or below this student",
     "about 90 percent of the students scored above this student",
     "the student's score was 90",
     "the student scored 90 points above the mean"],
   ans=1,
   why="A percentile describes a position within the distribution of scores, not the percent of questions answered correctly."),

 dict(q="Every value in a data set is increased by 5. Compared with the original data set, the new data set has",
   choices=[
     "a mean that is 5 larger and a standard deviation that is 5 larger",
     "a mean that is 5 larger and a standard deviation that is unchanged",
     "a mean that is unchanged and a standard deviation that is 5 larger",
     "both a mean and a standard deviation that are unchanged",
     "a mean that is 5 larger and a standard deviation that is 5 times as large"],
   ans=1,
   why="Adding a constant slides the whole distribution along the number line, moving every measure of centre by that constant while leaving every distance between values, and so every measure of spread, untouched."),

 dict(q="Every value in a data set is multiplied by 3. Compared with the original data set, the new data set has",
   choices=[
     "a mean 3 times as large and a standard deviation that is unchanged",
     "a mean that is unchanged and a standard deviation 3 times as large",
     "a mean 3 times as large and a standard deviation 3 times as large",
     "a mean 3 times as large and a standard deviation 9 times as large",
     "a mean 9 times as large and a standard deviation 3 times as large"],
   ans=2,
   why="Multiplying by a positive constant scales both the centre and every distance between values by that same constant, so the mean and the standard deviation are each tripled; the variance would be multiplied by 9."),

 dict(q="The heights of a group of students have a mean of 68 inches and a standard deviation of 4 inches. If every height is converted to centimetres by multiplying by 2.54, the new mean and standard deviation, in centimetres, are",
   choices=[
     "mean 172.72 and standard deviation 4.00",
     "mean 172.72 and standard deviation 10.16",
     "mean 68.00 and standard deviation 10.16",
     "mean 172.72 and standard deviation 25.81",
     "mean 70.54 and standard deviation 6.54"],
   ans=1,
   why="Multiplying every value by 2.54 multiplies the mean and the standard deviation by 2.54, giving 172.72 cm and 10.16 cm."),

 dict(q="Daily high temperatures have a mean of 77 degrees Fahrenheit and a standard deviation of 9 degrees Fahrenheit. Converted to Celsius using C = (F - 32) x 5/9, the mean and standard deviation become",
   choices=[
     "mean 25.0 and standard deviation 9.0",
     "mean 25.0 and standard deviation 5.0",
     "mean 45.0 and standard deviation 5.0",
     "mean 25.0 and standard deviation 3.2",
     "mean 77.0 and standard deviation 5.0"],
   ans=1,
   why="Subtracting 32 shifts the mean but not the spread, and multiplying by 5/9 scales both, so the mean is (77 - 32)(5/9) = 25.0 and the standard deviation is 9(5/9) = 5.0."),

 dict(q="Which pair of summary statistics is described as resistant, meaning that it is not strongly affected by a few extreme values?",
   choices=[
     "The mean and the standard deviation",
     "The median and the interquartile range",
     "The mean and the range",
     "The median and the range",
     "The mean and the interquartile range"],
   ans=1,
   why="The median depends on position rather than magnitude and the IQR uses only the middle half of the data, so neither is much moved by an extreme value; the mean, standard deviation and range all are."),

 dict(q="A data analyst is summarizing house prices in a city, a distribution that is strongly skewed to the right by a small number of very expensive houses. To describe a typical price and the spread of prices, the analyst should prefer",
   choices=[
     "the mean and the standard deviation, because they use every value",
     "the median and the interquartile range, because they are resistant to the extreme high prices",
     "the range, because it captures every price",
     "the mode and the range",
     "the mean and the range, because both are easy to compute"],
   ans=1,
   why="The few very expensive houses pull the mean and inflate the standard deviation and range, so the resistant pair gives the fairer picture of a typical price and typical spread."),

 dict(q="Two classes take the same test. Class A has a mean of 74 with a standard deviation of 12; Class B has a mean of 74 with a standard deviation of 4. Comparing the two distributions,",
   choices=[
     "Class A scored higher on average",
     "Class B scored higher on average",
     "the two classes have the same average, but Class A's scores are far more spread out",
     "the two classes have the same average and the same spread",
     "Class B must contain more students"],
   ans=2,
   why="Equal means say the centres match, while a standard deviation of 12 against 4 says Class A's scores are much more variable; nothing in these summaries reveals the class sizes."),
]
