# AP STATISTICS 1.6 Descriptions for One Quantitative Variable Distributions — 25 questions
# CED: Fall 2026, Unit 1. Learning objectives 1.6.A (describe a distribution's
# shape, center, variability and unusual features) and 1.6.B (justify a claim
# from such a description). Essential knowledge 1.6.A.1 through 1.6.A.6.
#
# The four required vocabulary distinctions are tested directly, because each is
# routinely confused with a neighbour:
#   skewed right vs skewed left  -- named for the LONGER TAIL, not the side the
#     bulk of the data sits on, which is the single most common error here;
#   unimodal / bimodal / approximately uniform;
#   outlier (unusually small or large relative to the rest);
#   gap (a region with no observations) vs cluster (a concentration of values).
#
# Distributions are specified numerically -- as dotplot counts, stemplots or bin
# tables -- since this bank carries no figures. Every shape claim keyed below is
# checked against the actual reconstructed data in verify_s1_6.py, including the
# mean-versus-median relation that skew implies.
TOPIC = ("1.6", "Descriptions for One Quantitative Variable Distributions", 1)

# Right-skewed: a long tail toward large values. n = 30.
TABLE_SKEW_R = dict(
    headers=["Value", "Frequency"],
    rows=[["1", "9"], ["2", "8"], ["3", "5"], ["4", "3"], ["5", "2"],
          ["6", "1"], ["7", "1"], ["8", "1"]])

# Left-skewed: the mirror image, a long tail toward small values. n = 30.
TABLE_SKEW_L = dict(
    headers=["Value", "Frequency"],
    rows=[["1", "1"], ["2", "1"], ["3", "1"], ["4", "2"], ["5", "3"],
          ["6", "5"], ["7", "8"], ["8", "9"]])

# Bimodal with a gap between two clusters. n = 40.
TABLE_BIMODAL = dict(
    headers=["Value", "Frequency"],
    rows=[["10", "3"], ["11", "7"], ["12", "8"], ["13", "2"],
          ["14", "0"], ["15", "0"], ["16", "0"],
          ["17", "2"], ["18", "8"], ["19", "7"], ["20", "3"]])

# Approximately uniform. n = 42.
TABLE_UNIFORM = dict(
    headers=["Value", "Frequency"],
    rows=[["1", "7"], ["2", "7"], ["3", "6"], ["4", "7"], ["5", "8"], ["6", "7"]])

# A tight body with one far-out value. n = 12.
TABLE_OUTLIER = dict(
    headers=["Observation", "Value"],
    rows=[["1-11", "between 20 and 26"], ["12", "83"]])

QUESTIONS = [
 dict(q="A complete description of the distribution of one quantitative variable should address",
   choices=[
     "the center only",
     "the center and the variability only",
     "the shape, the center, the variability, and any unusual features, all in context",
     "the number of categories and their labels",
     "the sample size and nothing else"],
   ans=2,
   why="EK 1.6.A.1 requires shape, center and variability together with unusual features such as outliers, gaps or clusters, all stated in context."),

 dict(q="The distribution of a quantitative variable is described as skewed to the right when",
   choices=[
     "the tail toward larger values is longer than the tail toward smaller values",
     "the tail toward smaller values is longer than the tail toward larger values",
     "most of the observations are large",
     "the left half is a mirror image of the right half",
     "the distribution has two prominent peaks"],
   ans=0,
   why="Skewness is named for the longer tail, so a right-skewed distribution has its long tail stretching toward the larger values."),

 dict(q="A distribution is skewed to the left when",
   choices=[
     "the right tail is longer than the left tail",
     "the left tail, toward the smaller values, is longer than the right tail",
     "all of the observations are negative",
     "the peak is exactly in the middle",
     "each value occurs about equally often"],
   ans=1,
   why="A left-skewed, or negatively skewed, distribution has its long tail running toward the smaller values."),

 dict(q="A distribution of one quantitative variable is approximately symmetric when",
   choices=[
     "it has exactly one peak",
     "its left half is approximately the mirror image of its right half",
     "it contains no outliers",
     "every value occurs the same number of times",
     "its mean is larger than its median"],
   ans=1,
   why="Approximate symmetry is the statement that one half of the distribution mirrors the other."),

 dict(q="A distribution with two prominent peaks is described as",
   choices=["unimodal", "bimodal", "uniform", "symmetric", "skewed"],
   ans=1,
   why="One main peak is unimodal and two prominent peaks is bimodal; a distribution with no prominent peak at all is approximately uniform."),

 dict(q="A distribution in which every value occurs with approximately the same frequency, with no prominent peaks, is described as approximately",
   choices=["unimodal", "bimodal", "uniform", "skewed right", "skewed left"],
   ans=2,
   why="Roughly equal frequencies across the range with no peak is what 'approximately uniform' means."),

 dict(q="In describing a distribution of one quantitative variable, an outlier is",
   choices=[
     "the value that occurs most often",
     "a data point that is unusually small or unusually large relative to the rest of the data",
     "any value above the mean",
     "the difference between the largest and smallest values",
     "a region of the distribution containing no data"],
   ans=1,
   why="An outlier is a point that stands well away from the rest of the data on either end."),

 dict(q="A gap in a distribution of one quantitative variable is",
   choices=[
     "a region between two values in which no data were observed",
     "the distance between the mean and the median",
     "a concentration of values in one part of the range",
     "the width of a histogram bin",
     "a category with no name"],
   ans=0,
   why="A gap is an interval inside the range of the data where no observations fall."),

 dict(q="Clusters in a distribution of one quantitative variable are",
   choices=[
     "concentrations of values, usually separated from one another by gaps",
     "the four quarters of the data",
     "observations that lie more than two standard deviations from the mean",
     "the bins of a histogram",
     "values that occur exactly once"],
   ans=0,
   why="Clusters are groups of values bunched together, and gaps are what separate one cluster from the next."),

 dict(q="The frequency table shown summarizes a data set. The shape of this distribution is best described as",
   table=TABLE_SKEW_R,
   choices=[
     "skewed to the left",
     "skewed to the right",
     "approximately symmetric",
     "approximately uniform",
     "bimodal"],
   ans=1,
   why="The frequencies fall away steadily from a peak at the smallest value, leaving a long thin tail stretching toward the larger values."),

 dict(q="For that same right-skewed data set, the relationship between the mean and the median is that the mean is",
   table=TABLE_SKEW_R,
   choices=[
     "less than the median",
     "equal to the median",
     "greater than the median",
     "equal to the mode",
     "impossible to compare without the standard deviation"],
   ans=2,
   why="The long right tail pulls the mean toward the large values while the median stays with the bulk of the data, so the mean sits above the median."),

 dict(q="A different data set is summarized by the frequency table shown. Its shape is best described as",
   table=TABLE_SKEW_L,
   choices=[
     "skewed to the left",
     "skewed to the right",
     "approximately symmetric",
     "approximately uniform",
     "bimodal with a gap"],
   ans=0,
   why="The bulk of the data sits at the large values with a long thin tail running down toward the small ones, which is left skew."),

 dict(q="For that left-skewed data set, the mean is",
   table=TABLE_SKEW_L,
   choices=[
     "greater than the median",
     "equal to the median",
     "less than the median",
     "equal to the maximum",
     "greater than the maximum"],
   ans=2,
   why="A long left tail drags the mean down toward the small values while the median stays with the bulk, so the mean falls below the median."),

 dict(q="A student says a distribution is 'skewed right' because most of its observations are at the right-hand, larger end of the range. This reasoning is",
   choices=[
     "correct, since skew is named for where most of the data lie",
     "incorrect, because skew is named for the direction of the longer tail, and a pile-up at the large values with a tail toward the small values is skewed LEFT",
     "correct, but only for distributions with an outlier",
     "incorrect, because a distribution with most data at the large values is always symmetric",
     "correct only if the mean equals the median"],
   ans=1,
   why="Skewness is named for the longer tail, not for where the bulk of the data sits, so a pile-up at the large values with a tail toward the small ones is left skew."),

 dict(q="The frequency table shown summarizes 40 observations. The most complete description of the shape of this distribution is",
   table=TABLE_BIMODAL,
   choices=[
     "unimodal and approximately symmetric",
     "bimodal, with two clusters separated by a gap",
     "approximately uniform",
     "skewed to the right",
     "skewed to the left"],
   ans=1,
   why="Frequencies peak near 12 and again near 18 with no observations at all at 14, 15 or 16, so there are two clusters separated by a gap."),

 dict(q="For that same 40-observation data set, the values 14, 15, and 16 form",
   table=TABLE_BIMODAL,
   choices=[
     "a cluster",
     "a gap",
     "an outlier",
     "a mode",
     "the median class"],
   ans=1,
   why="No observations at all fall at those three values, and a region inside the range with no observed data is a gap."),

 dict(q="Reporting only the mean and standard deviation of the 40-observation bimodal data set would be misleading mainly because",
   table=TABLE_BIMODAL,
   choices=[
     "the mean cannot be computed for a bimodal distribution",
     "a single center does not describe data that fall into two separated clusters, and the mean lands in the gap where no observations occur",
     "the standard deviation is always zero when there is a gap",
     "bimodal data have no variability",
     "the median would be equally uninformative in every distribution"],
   ans=1,
   why="With two separated groups the mean falls between them, in the empty region, so no single center represents the data."),

 dict(q="The frequency table shown summarizes 42 observations. This distribution is best described as approximately",
   table=TABLE_UNIFORM,
   choices=["bimodal", "uniform", "skewed to the right", "skewed to the left", "bimodal with a gap"],
   ans=1,
   why="Every value occurs six to eight times with no prominent peak, which is what approximately uniform means."),

 dict(q="Eleven of twelve measurements fall between 20 and 26, and the twelfth is 83. The value 83 is best described as",
   table=TABLE_OUTLIER,
   choices=[
     "a cluster",
     "a gap",
     "an outlier",
     "the mode",
     "evidence that the distribution is uniform"],
   ans=2,
   why="A single value far away from a tightly grouped body of data is unusually large relative to the rest, which is an outlier."),

 dict(q="For those twelve measurements, which pair of summaries is affected MORE by the value 83?",
   table=TABLE_OUTLIER,
   choices=[
     "The median and the interquartile range",
     "The mean and the standard deviation",
     "The mode and the median",
     "The minimum and the median",
     "None of the summaries is affected"],
   ans=1,
   why="The mean and standard deviation use every value's actual size, so one extreme observation moves both, while the median and IQR depend only on position and barely shift."),

 dict(q="Two distributions of the same quantitative variable have the same shape and the same center, but one has noticeably wider spread. The two differ in",
   choices=["shape", "center", "variability", "sample size", "modality"],
   ans=2,
   why="Spread is variability, the third of the three required elements of a description alongside shape and center."),

 dict(q="Which of the following is an unusual feature of a distribution rather than a description of its shape?",
   choices=[
     "Skewed to the right",
     "Approximately symmetric",
     "Unimodal",
     "A gap between two clusters of values",
     "Approximately uniform"],
   ans=3,
   why="Skewness, symmetry, modality and uniformity all describe shape, whereas gaps, clusters and outliers are the unusual features called out separately."),

 dict(q="A quality manager examines a distribution of part diameters and reports: 'roughly symmetric, centered near 5.0 mm, with values from 4.7 to 5.3 mm and no outliers.' This description is missing",
   choices=[
     "nothing; it addresses shape, center, variability and unusual features in context",
     "the shape",
     "the center",
     "any statement about variability",
     "any statement about unusual features"],
   ans=0,
   why="Symmetry gives the shape, 5.0 mm the center, the range from 4.7 to 5.3 the variability, and 'no outliers' addresses unusual features, all with units."),

 dict(q="Test scores for a class are strongly skewed to the left. Which measure of center best represents a typical student's score?",
   choices=[
     "The mean, because it uses every observation",
     "The median, because it is not pulled toward the long tail of low scores",
     "The maximum, because most scores are near it",
     "The range, because it covers all the scores",
     "The standard deviation, because it measures spread"],
   ans=1,
   why="A long left tail drags the mean below the bulk of the data, so the median gives the better sense of a typical score; range and standard deviation are not measures of center at all."),

 dict(q="A researcher observes that a distribution of household sizes is unimodal, skewed to the right, centered near 3 people, with most households between 1 and 6 people and a few reporting 9 or more. The claim best justified by this description is that",
   choices=[
     "the mean household size is smaller than the median household size",
     "a small number of unusually large households pull the mean above the median, so the median near 3 better describes a typical household",
     "household size is a categorical variable",
     "the distribution is approximately uniform between 1 and 9",
     "no household has more than 6 people"],
   ans=1,
   why="Right skew means the few large households stretch the upper tail and pull the mean above the median, so the median is the fairer summary of a typical household."),
]
