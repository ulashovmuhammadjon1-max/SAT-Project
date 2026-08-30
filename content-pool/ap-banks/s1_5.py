# AP STATISTICS 1.5 Graphical Representations for One Quantitative Variable — 25 questions
# CED: Fall 2026, Unit 1. Learning objective 1.5.A, essential knowledge 1.5.A.1
# through 1.5.A.4: histograms, stem-and-leaf plots and dotplots.
#
# There are no images in this bank, but none is needed here: a stem-and-leaf plot
# IS text, a dotplot is fully specified by its value/count pairs, and a histogram
# is fully specified by its bins and their frequencies. Each is given as a table,
# so the student reads exactly what the display would show.
#
# Data sets:
#   F  dotplot, n = 20: value 3 x2, 4 x5, 5 x8, 6 x4, 7 x1
#        sum 97, mean 4.85, median 5, mode 5
#   G  stem-and-leaf, n = 16: 23 27 29 | 31 34 34 36 38 38 | 40 42 45 47 49 | 51 53
#        min 23, max 53, range 30, median 38, seven values at or above 40
#   H  histogram, n = 45, bins of width 10: 4, 11, 18, 9, 3
# Every count, proportion, mean, median and range keyed below is recomputed from
# these tables in verify_s1_5.py.
TOPIC = ("1.5", "Graphical Representations for One Quantitative Variable", 1)

TABLE_F = dict(
    headers=["Value", "Number of dots"],
    rows=[["3", "2"], ["4", "5"], ["5", "8"], ["6", "4"], ["7", "1"]])

TABLE_G = dict(
    headers=["Stem", "Leaf"],
    rows=[["2", "3 7 9"], ["3", "1 4 4 6 8 8"], ["4", "0 2 5 7 9"], ["5", "1 3"]])

TABLE_H = dict(
    headers=["Interval", "Frequency"],
    rows=[["0 to under 10", "4"], ["10 to under 20", "11"], ["20 to under 30", "18"],
          ["30 to under 40", "9"], ["40 to under 50", "3"]])

QUESTIONS = [
 dict(q="Histograms, stem-and-leaf plots, and dotplots all display the distribution of a quantitative variable, and all three",
   choices=[
     "arrange the values in alphabetical order",
     "maintain the natural ordering of the variable's values from smallest to largest",
     "require the data to be measured in whole numbers",
     "show the relationship between two variables at once",
     "display exactly five categories"],
   ans=1,
   why="A quantitative variable has a natural numerical order, and all three displays place the values along an axis in that order."),

 dict(q="In a histogram, the height of each bar shows",
   choices=[
     "the width of the interval that bar covers",
     "the frequency or relative frequency of the observations falling in that interval",
     "the largest value in that interval",
     "the number of intervals used",
     "the mean of the observations in that interval"],
   ans=1,
   why="Each bar of a histogram stands for one interval, and its height is how many, or what proportion of, the observations fall in that interval."),

 dict(q="Two students build histograms from exactly the same data set but choose different bin widths. It follows that",
   choices=[
     "the two histograms must look identical",
     "the appearance of the distribution can differ between the two histograms even though the data are the same",
     "one of the two students must have made an arithmetic error",
     "the data set must contain an outlier",
     "the total number of observations shown will differ between the two histograms"],
   ans=1,
   why="Altering the bin width changes how observations are grouped and can noticeably change the shape a histogram appears to have, without changing the data at all."),

 dict(q="In a stem-and-leaf plot, each value of the quantitative variable is split so that",
   choices=[
     "the stem is the final digit and the leaf is the leading digit or digits",
     "the stem is the leading digit or digits and the leaf is usually the single digit that follows",
     "the stem is the mean and the leaf is the deviation from the mean",
     "the stem is the frequency and the leaf is the value",
     "the stem and the leaf are each half of the total number of observations"],
   ans=1,
   why="The stem holds the leading digit or digits and the leaf the digit after it, with both stems and leaves ordered from smallest to largest."),

 dict(q="In a dotplot, each individual dot represents",
   choices=[
     "one observation, placed at the position matching its value",
     "an interval of values",
     "the mean of a group of observations",
     "one category of a categorical variable",
     "ten observations, to save space"],
   ans=0,
   why="A dotplot draws one dot per observation at that observation's value, stacking dots for nearly identical values."),

 dict(q="A dotplot of a data set is summarized by the value-and-count table shown. How many observations are in the data set?",
   table=TABLE_F,
   choices=["5", "8", "17", "20", "25"],
   ans=3,
   why="The number of dots is 2 + 5 + 8 + 4 + 1 = 20."),

 dict(q="For the dotplot data set, which value has the most dots stacked above it?",
   table=TABLE_F,
   choices=["3", "4", "5", "6", "7"],
   ans=2,
   why="The value 5 carries 8 dots, more than any other value, so it is the mode."),

 dict(q="What proportion of the dotplot's observations have a value of 5?",
   table=TABLE_F,
   choices=["0.05", "0.20", "0.25", "0.40", "0.80"],
   ans=3,
   why="8 of the 20 observations equal 5, and 8/20 = 0.40."),

 dict(q="How many of the dotplot's observations are at most 4?",
   table=TABLE_F,
   choices=["2", "5", "7", "13", "15"],
   ans=2,
   why="Two observations equal 3 and five equal 4, so 2 + 5 = 7 are at most 4."),

 dict(q="What is the mean of the dotplot data set?",
   table=TABLE_F,
   choices=["4.00", "4.85", "5.00", "5.15", "19.40"],
   ans=1,
   why="The values total 3(2) + 4(5) + 5(8) + 6(4) + 7(1) = 97, and 97/20 = 4.85."),

 dict(q="What is the median of the dotplot data set?",
   table=TABLE_F,
   choices=["4.0", "4.5", "4.85", "5.0", "5.5"],
   ans=3,
   why="With 20 observations the median is the average of the 10th and 11th values in order, and both of those are 5."),

 dict(q="A stem-and-leaf plot of a data set is shown, where a stem of 2 and a leaf of 3 represent the value 23. How many values are in this data set?",
   table=TABLE_G,
   choices=["4", "9", "16", "20", "53"],
   ans=2,
   why="Counting the leaves gives 3 + 6 + 5 + 2 = 16 values."),

 dict(q="For the stem-and-leaf data, the smallest and largest values are",
   table=TABLE_G,
   choices=["2 and 5", "3 and 53", "23 and 51", "23 and 53", "20 and 59"],
   ans=3,
   why="The first leaf on the smallest stem gives 23 and the last leaf on the largest stem gives 53."),

 dict(q="What is the range of the stem-and-leaf data set?",
   table=TABLE_G,
   choices=["3", "16", "30", "38", "76"],
   ans=2,
   why="The range is the largest value minus the smallest, 53 - 23 = 30."),

 dict(q="How many values in the stem-and-leaf data set are 40 or greater?",
   table=TABLE_G,
   choices=["2", "5", "7", "9", "12"],
   ans=2,
   why="The stem-4 row holds five values and the stem-5 row holds two, so 5 + 2 = 7 values are at least 40."),

 dict(q="What is the median of the stem-and-leaf data set?",
   table=TABLE_G,
   choices=["34", "36", "38", "39", "40"],
   ans=2,
   why="With 16 values the median averages the 8th and 9th in order, and both of those are 38."),

 dict(q="What proportion of the stem-and-leaf data set is less than 30?",
   table=TABLE_G,
   choices=["0.1250", "0.1875", "0.3750", "0.4375", "0.5000"],
   ans=1,
   why="Three of the 16 values lie below 30, and 3/16 = 0.1875."),

 dict(q="A stem-and-leaf plot has an advantage over a histogram of the same data in that the stem-and-leaf plot",
   choices=[
     "is faster to draw for very large data sets",
     "retains the individual data values, which a histogram does not",
     "can display a categorical variable",
     "never has to be ordered",
     "always shows the mean directly"],
   ans=1,
   why="Every original value can be read back off a stem-and-leaf plot, whereas a histogram records only how many observations fell in each interval."),

 dict(q="A histogram of 45 measurements uses the intervals shown. How many measurements are less than 20?",
   table=TABLE_H,
   choices=["4", "11", "15", "18", "30"],
   ans=2,
   why="The first two intervals hold 4 and 11 measurements, so 4 + 11 = 15 fall below 20."),

 dict(q="For that histogram, what proportion of the measurements fall in the interval from 20 to under 30?",
   table=TABLE_H,
   choices=["0.067", "0.200", "0.244", "0.400", "0.600"],
   ans=3,
   why="18 of the 45 measurements fall in that interval, and 18/45 = 0.40."),

 dict(q="For that same histogram, how many measurements are 30 or greater?",
   table=TABLE_H,
   choices=["3", "9", "12", "18", "33"],
   ans=2,
   why="The last two intervals hold 9 and 3 measurements, so 9 + 3 = 12 are at least 30."),

 dict(q="From that histogram alone, the exact largest measurement in the data set",
   table=TABLE_H,
   choices=[
     "is 50, since that is where the last interval ends",
     "is 49, since the last interval stops just below 50",
     "cannot be determined, because a histogram records only how many values fall in each interval",
     "is 45, since there are 45 measurements",
     "is 3, since the last interval has a frequency of 3"],
   ans=2,
   why="A histogram groups values into intervals and discards their individual identities, so all that can be said is that the maximum lies somewhere in the interval from 40 to under 50."),

 dict(q="Which display would be a poor choice for showing the distribution of a single quantitative variable?",
   choices=[
     "A dotplot",
     "A histogram",
     "A stem-and-leaf plot",
     "A pie chart",
     "A histogram drawn with the bins on the vertical axis and the bars horizontal"],
   ans=3,
   why="A pie chart shows how a categorical variable divides a whole, and it cannot represent the ordering or spacing of numerical values."),

 dict(q="A dotplot is usually a better choice than a histogram when",
   choices=[
     "the data set is very large, with thousands of observations",
     "the data set is small, so that showing every individual observation is practical and informative",
     "the variable is categorical",
     "only the mean is of interest",
     "the values must be hidden from the reader"],
   ans=1,
   why="One dot per observation stays readable only while the data set is small; with thousands of values a histogram's grouped bars are far clearer."),

 dict(q="A student asserts that because bars in a histogram touch one another while bars in a bar chart do not, the difference is purely cosmetic. The best response is that the touching bars",
   choices=[
     "are indeed only a matter of style, and either display may be drawn either way",
     "reflect that a histogram's horizontal axis is a continuous number line divided into adjoining intervals, while a bar chart's axis holds separate category labels",
     "indicate that a histogram always has more observations than a bar chart",
     "show that a histogram cannot display relative frequencies",
     "mean that a histogram's intervals must all contain the same number of observations"],
   ans=1,
   why="Histogram bins are adjoining intervals of a number line, so the bars meet; a bar chart's categories are distinct labels with nothing between them."),
]
