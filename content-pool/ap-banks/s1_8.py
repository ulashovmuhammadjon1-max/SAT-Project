# AP STATISTICS 1.8 Graphical Representations of Summary Statistics for One
# Quantitative Variable — 25 questions
# CED: Fall 2026, Unit 1. Learning objectives 1.8.A (five-number summary and
# boxplots, including the outlier convention) and 1.8.B (describing a display in
# terms of the relationship between the mean and the median).
#
# A boxplot is completely determined by five numbers, so this topic needs no
# figure: every "boxplot" question here either gives the data set or gives the
# five-number summary directly, which is exactly the information a boxplot
# carries and no more. That last point is itself examinable -- several items turn
# on what a boxplot canNOT tell you (the mean, the sample size, modality, gaps).
#
# Data set P, n = 20:
#   12 16 18 19 20 21 23 24 25 26 27 28 30 31 33 34 36 40 44 58
#   min 12, Q1 20.5, median 26.5, Q3 33.5, max 58, IQR 13
#   fences 1.0 and 53.0, so 58 is the sole outlier and the upper whisker stops
#   at 44, the largest value that is not an outlier
#   mean 28.25 > median 26.5, consistent with the right skew the summary shows
TOPIC = ("1.8", "Graphical Representations of Summary Statistics for One Quantitative Variable", 1)

DATA_P = "12, 16, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 33, 34, 36, 40, 44, 58"

QUESTIONS = [
 dict(q="The five-number summary of a quantitative data set consists of",
   choices=[
     "the mean, median, mode, range, and standard deviation",
     "the minimum, first quartile, median, third quartile, and maximum",
     "the five most common values",
     "the mean and the four quartiles",
     "the minimum, mean, median, mode, and maximum"],
   ans=1,
   why="The five-number summary is the minimum, Q1, the median, Q3, and the maximum, and it is exactly what a boxplot displays."),

 dict(q="On a boxplot, the box itself represents",
   choices=[
     "all of the data",
     "the middle 50% of the data, from Q1 to Q3",
     "the middle 25% of the data",
     "the values within one standard deviation of the mean",
     "the outliers"],
   ans=1,
   why="The ends of the box are the quartiles, which bound the middle half of the ordered data."),

 dict(q="The line drawn inside the box of a boxplot marks the",
   choices=["mean", "median", "mode", "midrange", "standard deviation"],
   ans=1,
   why="A boxplot is built from the five-number summary, and the interior line is the median; the mean does not appear on a boxplot at all."),

 dict(q="On a boxplot with no outliers, each whisker represents approximately what share of the data?",
   choices=["10%", "25%", "50%", "75%", "100%"],
   ans=1,
   why="The quartiles cut the data into four roughly equal parts, so each whisker spans about a quarter of the observations."),

 dict(q="When a data set contains outliers, a boxplot is conventionally drawn so that",
   choices=[
     "the whiskers still extend all the way to the minimum and maximum",
     "the whiskers extend to the most extreme values that are not outliers, and each outlier is plotted separately with an asterisk or other symbol",
     "the outliers are deleted from the data set before plotting",
     "the box is widened to include the outliers",
     "no boxplot may be drawn"],
   ans=1,
   why="The whiskers stop at the most extreme non-outlying values so that the outliers show up individually rather than being hidden inside a long whisker."),

 dict(q=f"A data set of twenty values is {DATA_P}. What is the median?",
   choices=["25.0", "26.0", "26.5", "27.0", "28.25"],
   ans=2,
   why="With twenty values the median averages the 10th and 11th, which are 26 and 27, giving 26.5; 28.25 is the mean."),

 dict(q=f"What is the first quartile Q1 of the data set {DATA_P}?",
   choices=["18.0", "20.0", "20.5", "21.0", "23.0"],
   ans=2,
   why="Q1 is the median of the lower ten values, which averages the 5th and 6th of them, 20 and 21, giving 20.5."),

 dict(q=f"What is the third quartile Q3 of the data set {DATA_P}?",
   choices=["30.0", "31.0", "33.0", "33.5", "36.0"],
   ans=3,
   why="Q3 is the median of the upper ten values, which averages 33 and 34, giving 33.5."),

 dict(q=f"What is the interquartile range of the data set {DATA_P}?",
   choices=["6.0", "13.0", "20.5", "33.5", "46.0"],
   ans=1,
   why="The IQR is Q3 - Q1 = 33.5 - 20.5 = 13.0; 46 is the range."),

 dict(q=f"Using the 1.5 x IQR rule, which value or values would be plotted as outliers on a boxplot of the data set {DATA_P}?",
   choices=["12 only", "44 only", "58 only", "44 and 58", "there are no outliers"],
   ans=2,
   why="The boundaries are 20.5 - 19.5 = 1.0 and 33.5 + 19.5 = 53.0, and only 58 falls outside them; 44 is below 53 and so is not an outlier."),

 dict(q=f"Drawn as a boxplot using the standard outlier convention, the upper whisker for the data set {DATA_P} extends to",
   choices=["33.5", "36", "40", "44", "58"],
   ans=3,
   why="The whisker stops at the largest value that is not an outlier, which is 44, and 58 is plotted separately as an outlier."),

 dict(q=f"The lower whisker of the boxplot for the data set {DATA_P} extends to",
   choices=["1.0", "12", "16", "20.5", "26.5"],
   ans=1,
   why="There are no low outliers, since the lower boundary is 1.0 and the minimum is 12, so the lower whisker reaches the minimum value 12."),

 dict(q=f"What is the five-number summary of the data set {DATA_P}?",
   choices=[
     "12, 20.5, 26.5, 33.5, 58",
     "12, 20.5, 28.25, 33.5, 58",
     "12, 21, 26.5, 33, 44",
     "16, 20.5, 26.5, 33.5, 44",
     "12, 20, 26, 34, 58"],
   ans=0,
   why="The minimum is 12, Q1 is 20.5, the median is 26.5, Q3 is 33.5, and the maximum is 58; the maximum stays in the summary even though it is an outlier."),

 dict(q="What proportion of a data set lies between Q1 and Q3, the two ends of a boxplot's box?",
   choices=["0.25", "0.50", "0.68", "0.75", "0.95"],
   ans=1,
   why="Q1 and Q3 are the 25th and 75th percentiles, so the box spans the middle half of the data."),

 dict(q="On a boxplot, approximately what proportion of the data lies above Q3?",
   choices=["0.05", "0.25", "0.50", "0.75", "0.95"],
   ans=1,
   why="Q3 is the 75th percentile, so about a quarter of the observations lie above it."),

 dict(q="A distribution is relatively symmetric. The relationship between its mean and its median is that they are",
   choices=[
     "relatively close to each other",
     "always exactly equal, with no exceptions",
     "far apart, with the mean much larger",
     "far apart, with the mean much smaller",
     "unrelated to each other"],
   ans=0,
   why="Symmetry makes the two measures of center land near one another, though 'relatively close' is the accurate claim rather than exact equality."),

 dict(q="For a distribution that is skewed to the right, the mean is usually",
   choices=[
     "smaller than the median",
     "equal to the median",
     "larger than the median",
     "equal to the third quartile",
     "smaller than the minimum"],
   ans=2,
   why="The long right tail pulls the mean toward the large values while the median stays with the bulk of the data."),

 dict(q="For a distribution that is skewed to the left, the mean is usually",
   choices=[
     "larger than the median",
     "smaller than the median",
     "equal to the median",
     "equal to the first quartile",
     "larger than the maximum"],
   ans=1,
   why="The long left tail pulls the mean down toward the small values, so it typically falls below the median."),

 dict(q="A boxplot shows the median sitting much closer to Q1 than to Q3, with a much longer whisker on the right. The distribution is best described as",
   choices=[
     "skewed to the left",
     "skewed to the right",
     "approximately symmetric",
     "approximately uniform",
     "bimodal"],
   ans=1,
   why="A short left side and a long right side of both the box and the whiskers is the boxplot signature of a long upper tail, which is right skew."),

 dict(q="A boxplot shows the median sitting much closer to Q3 than to Q1, with a much longer whisker on the left. For this distribution you would expect the mean to be",
   choices=[
     "larger than the median",
     "smaller than the median",
     "exactly equal to the median",
     "equal to Q3",
     "outside the range of the data"],
   ans=1,
   why="That boxplot describes a long lower tail, which is left skew, and left skew pulls the mean below the median."),

 dict(q="Which of the following can NOT be determined from a boxplot alone?",
   choices=[
     "The median",
     "The interquartile range",
     "The mean",
     "The maximum value",
     "The range"],
   ans=2,
   why="A boxplot displays only the five-number summary, and the mean is not one of those five numbers and cannot be recovered from them."),

 dict(q="Two boxplots are drawn on the same scale from data sets of unknown size. From the boxplots alone, you cannot determine",
   choices=[
     "which data set has the larger median",
     "which data set has the larger interquartile range",
     "how many observations are in each data set",
     "which data set has the larger third quartile",
     "which data set has the larger maximum"],
   ans=2,
   why="A boxplot is built from five position summaries, and those five numbers are the same whether the data set holds 20 observations or 2,000."),

 dict(q="Two distributions have identical five-number summaries, so their boxplots are identical. It follows that",
   choices=[
     "the two data sets must contain exactly the same values",
     "the two distributions could still differ, for example in whether they are unimodal or bimodal, because a boxplot does not show gaps or clusters within the box",
     "the two data sets must have the same number of observations",
     "the two distributions must have the same mean",
     "neither distribution can contain an outlier"],
   ans=1,
   why="A boxplot compresses the data to five positions, so two very different shapes, including a bimodal one and a unimodal one, can produce the same picture."),

 dict(q="Boxplots of test scores for two classes are compared. Class A's box spans 62 to 78 with a median of 70; Class B's box spans 68 to 74 with a median of 71. The best comparison is that the two classes have",
   choices=[
     "similar medians, but Class A's middle half of scores is more spread out",
     "similar medians, but Class B's middle half of scores is more spread out",
     "very different medians and identical spread",
     "identical distributions",
     "medians that cannot be compared without the means"],
   ans=0,
   why="Medians of 70 and 71 are close, while an IQR of 16 for Class A against 6 for Class B says Class A's middle half is far more variable."),

 dict(q="A researcher reports that for a particular distribution the mean is 51.2 and the median is 50.9, and a boxplot shows whiskers of nearly equal length with the median near the middle of the box. Taken together, these facts most support the description",
   choices=[
     "strongly skewed to the right",
     "strongly skewed to the left",
     "roughly symmetric",
     "bimodal with a large gap",
     "containing several extreme outliers"],
   ans=2,
   why="A mean and median that nearly coincide, together with a median centered in the box and whiskers of similar length, are what approximate symmetry looks like."),
]
