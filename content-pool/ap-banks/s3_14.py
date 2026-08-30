# AP STATISTICS 3.14 Setting Up a Chi-Square Test for Homogeneity or
# Independence — 25 questions
# CED: Fall 2026, Unit 3. Learning objectives 3.14.A (describe chi-square
# distributions), 3.14.B (identify which of the two tests applies, naming the
# variables and populations in context), 3.14.C (state the hypotheses) and
# 3.14.D (verify the conditions).
#
# The chi-square topics were a separate unit in the retired 2019 CED (old Unit
# 8). The Fall 2026 redesign folds them into Unit 3, which is why they sit here
# after the two-proportion procedures rather than in a unit of their own.
#
# WHICH TEST APPLIES turns entirely on HOW THE DATA WERE COLLECTED, not on what
# the table looks like -- the two tests use the same expected counts, the same
# statistic and the same degrees of freedom, and a student cannot tell them
# apart from the table alone:
#   HOMOGENEITY   several separate populations or treatment groups were sampled
#                 or assigned, and the question is whether the distribution of
#                 one categorical variable is the same across them;
#   INDEPENDENCE  ONE population was sampled once and each individual was
#                 classified by TWO categorical variables, and the question is
#                 whether those variables are associated.
# Four items turn on that distinction, each giving the design rather than the
# table.
#
# The chi-square distribution itself (EK 3.14.A): values are positive, the shape
# is skewed right, and the skew fades as the degrees of freedom grow. The
# statistic measures the distance between observed and expected counts RELATIVE
# TO the expected counts, which is why a discrepancy of 10 matters more in a
# cell expecting 20 than in one expecting 2,000.
#
# Degrees of freedom for a two-way table: (rows - 1)(columns - 1). It depends
# only on the SHAPE of the table, never on the sample size -- the error students
# make most often here.
TOPIC = ("3.14", "Setting Up a Chi-Square Test for Homogeneity or Independence", 3)

QUESTIONS = [
 dict(q="The chi-square statistic measures",
   choices=[
     "the distance between observed and expected counts, relative to the expected counts",
     "the difference between two sample proportions",
     "the average of the observed counts",
     "the number of cells in the table",
     "the correlation between two variables"],
   ans=0,
   why="Each cell contributes a squared difference divided by its expected count, so the same absolute discrepancy counts for more where fewer observations were expected."),

 dict(q="Chi-square distributions are",
   choices=[
     "symmetric and centred at 0",
     "positive-valued and skewed to the right",
     "negative-valued and skewed to the left",
     "uniform",
     "always normal"],
   ans=1,
   why="The statistic sums squared quantities, so it cannot be negative, and the resulting family of density curves has a long right tail."),

 dict(q="As the degrees of freedom of a chi-square distribution increase, the distribution becomes",
   choices=[
     "more strongly skewed to the right",
     "less strongly skewed, moving toward a more symmetric shape",
     "skewed to the left",
     "narrower",
     "uniform"],
   ans=1,
   why="The skew becomes less pronounced with increasing degrees of freedom, which is why a large table's chi-square distribution looks far more symmetric than a small one's."),

 dict(q="A chi-square test statistic can never be",
   choices=["0", "negative", "large", "equal to the degrees of freedom", "greater than 10"],
   ans=1,
   why="Every term is a squared difference divided by a positive expected count, so the sum is at least 0."),

 dict(q="A chi-square statistic of 0 would mean that",
   choices=[
     "the observed counts exactly match the expected counts in every cell",
     "the table has no data",
     "the null hypothesis is false",
     "the expected counts are 0",
     "the sample size is 0"],
   ans=0,
   why="Each term vanishes only when observed equals expected, so a total of 0 requires perfect agreement across every cell."),

 dict(q="Researchers take independent random samples from three different cities and record whether each person recycles. To test whether the distribution of recycling behaviour is the same across the three cities, the appropriate test is",
   choices=[
     "a chi-square test for homogeneity",
     "a chi-square test for independence",
     "a two-sample z-test for proportions",
     "a one-sample z-test",
     "a chi-square goodness-of-fit test"],
   ans=0,
   why="Several separate populations were sampled and one categorical variable is compared across them, which is the homogeneity setting."),

 dict(q="Researchers take ONE random sample of 500 adults from a city and record each person's education level and whether they recycle. To test whether the two variables are related, the appropriate test is",
   choices=[
     "a chi-square test for homogeneity",
     "a chi-square test for independence",
     "a two-sample z-test for proportions",
     "a one-sample z-interval",
     "a matched pairs test"],
   ans=1,
   why="A single sample from one population, with each individual classified by two categorical variables, is the independence setting."),

 dict(q="What distinguishes a chi-square test for homogeneity from a chi-square test for independence?",
   choices=[
     "The formula for the test statistic",
     "How the data were collected: several populations or treatment groups sampled separately, against one population sampled once and classified two ways",
     "The number of rows in the table",
     "The degrees of freedom",
     "Whether the expected counts are computed"],
   ans=1,
   why="The arithmetic is identical in both; only the design, and therefore the wording of the hypotheses and the conclusion, differs."),

 dict(q="A researcher randomly assigns 300 volunteers to three treatments and records whether each improves. The appropriate test for whether the distribution of improvement differs across treatments is",
   choices=[
     "a chi-square test for independence",
     "a chi-square test for homogeneity",
     "a one-sample z-test",
     "a two-sample z-interval",
     "no test is appropriate"],
   ans=1,
   why="Randomly assigned treatment groups play the role of separate populations, so comparing one categorical variable across them is a test for homogeneity."),

 dict(q="The null hypothesis for a chi-square test for homogeneity states that",
   choices=[
     "there is no difference in the distributions of the categorical variable across the populations or treatments",
     "the two categorical variables are independent",
     "all the expected counts are equal",
     "the sample proportions are equal to 0.5",
     "the chi-square statistic is 0"],
   ans=0,
   why="Homogeneity asks whether one variable is distributed the same way in every group, so the null is that it is."),

 dict(q="The alternative hypothesis for a chi-square test for homogeneity states that",
   choices=[
     "there is a difference in the distributions of the categorical variable across the populations or treatments",
     "one particular population has the largest proportion",
     "the variables are associated",
     "the chi-square statistic is large",
     "the expected counts are wrong"],
   ans=0,
   why="The alternative is simply that the distributions are not all the same; it does not say which group differs or in which direction."),

 dict(q="The null hypothesis for a chi-square test for independence states that",
   choices=[
     "there is no association between the two categorical variables in the population",
     "the distributions are the same across several populations",
     "the two variables are associated",
     "all cells have the same count",
     "the sample was random"],
   ans=0,
   why="Independence asks whether the two variables are related in one population, so the null is that they are not."),

 dict(q="The alternative hypothesis for a chi-square test for independence states that",
   choices=[
     "there is an association between the two categorical variables in the population",
     "one variable causes the other",
     "the distributions differ across populations",
     "the expected counts differ from the observed counts",
     "the sample is biased"],
   ans=0,
   why="The alternative asserts an association; a chi-square test never speaks to causation and never names a direction."),

 dict(q="A chi-square alternative hypothesis is",
   choices=[
     "always one-sided in the sense that only large values of the statistic count as evidence",
     "always two-sided",
     "sometimes stated with a less-than sign",
     "stated about a single proportion",
     "not needed"],
   ans=0,
   why="A small statistic means observed and expected agree, which supports the null; only large values indicate a departure, so the p-value is always a right-tail area."),

 dict(q="For a two-way table with 3 rows and 4 columns, the degrees of freedom are",
   choices=["3", "6", "7", "11", "12"],
   ans=1,
   why="Degrees of freedom are (rows - 1)(columns - 1) = (3 - 1)(4 - 1) = 6."),

 dict(q="For a two-way table with 2 rows and 5 columns, the degrees of freedom are",
   choices=["1", "4", "5", "8", "10"],
   ans=1,
   why="(2 - 1)(5 - 1) = 4."),

 dict(q="For a two-way table with 4 rows and 3 columns based on a sample of 800, the degrees of freedom are",
   choices=["6", "7", "11", "12", "799"],
   ans=0,
   why="(4 - 1)(3 - 1) = 6; the degrees of freedom depend only on the shape of the table, never on the sample size."),

 dict(q="Two studies use tables of the same shape but sample sizes of 200 and 2,000. Their degrees of freedom are",
   choices=[
     "different, because the sample sizes differ",
     "the same, because degrees of freedom depend only on the numbers of rows and columns",
     "different, because the expected counts differ",
     "impossible to compare",
     "both equal to the sample size minus 1"],
   ans=1,
   why="Sample size affects the expected counts and hence the statistic, but not the shape of the null distribution used to judge it."),

 dict(q="Which of the following is NOT a condition for a chi-square test for homogeneity or independence?",
   choices=[
     "The data come from a random sample, independent random samples, or a randomized experiment",
     "When sampling without replacement, the sample is no more than 10% of the population",
     "All expected counts are at least 5",
     "The observed counts are all at least 30",
     "All three of the other conditions are required"],
   ans=3,
   why="The count condition applies to the EXPECTED counts, not the observed ones, and the threshold is 5 rather than 30."),

 dict(q="The count condition for a chi-square test requires that",
   choices=[
     "every observed count be at least 5",
     "every expected count be at least 5",
     "the total sample size be at least 5",
     "every observed count be at least 10",
     "the smallest cell have exactly 5 observations"],
   ans=1,
   why="The chi-square approximation relies on the expected counts being large enough, and an observed count of 0 is perfectly acceptable if its expected count is adequate."),

 dict(q="A two-way table has one cell with an observed count of 2 and an expected count of 11. Regarding the count condition, this cell",
   choices=[
     "violates the condition, because the observed count is below 5",
     "satisfies the condition, because the condition applies to the expected count, which is 11",
     "violates the condition, because 2 is less than 11",
     "cannot be assessed",
     "requires the cell to be removed"],
   ans=1,
   why="A small observed count in a cell where more were expected is exactly the sort of discrepancy the test is designed to detect, not a reason to abandon it."),

 dict(q="For a chi-square test for independence, the randomization condition requires",
   choices=[
     "a random sample from the single population of interest",
     "independent random samples from each of several populations",
     "no randomization at all",
     "equal sample sizes in every group",
     "a census"],
   ans=0,
   why="Independence concerns one population, so one random sample from it is what the design requires; several separate samples would be the homogeneity setting."),

 dict(q="For a chi-square test for homogeneity, the randomization condition is satisfied by",
   choices=[
     "one random sample classified two ways",
     "independent random samples from each population, or random assignment to treatment groups",
     "any convenience sample",
     "a sample of at least 30",
     "expected counts of at least 5"],
   ans=1,
   why="Homogeneity compares several groups, so each group must arise from its own random sample or from random assignment."),

 dict(q="Stated in context, the hypotheses for a chi-square test comparing recycling behaviour across three cities should reference",
   choices=[
     "the chi-square statistic and its degrees of freedom",
     "the categorical variable, recycling behaviour, and the three city populations being compared",
     "the sample sizes only",
     "the expected counts",
     "the significance level"],
   ans=1,
   why="EK 3.14.B.2 requires a homogeneity test to name the categorical variable and the populations, exactly as every other procedure in this unit is stated in context."),

 dict(q="A chi-square test for independence finds strong evidence of an association between two categorical variables in an observational study. The strongest justified conclusion is that",
   choices=[
     "one variable causes the other",
     "the two variables are associated in that population, but with no random assignment no causal conclusion follows",
     "the two variables are independent",
     "the association holds in every population",
     "no conclusion is possible"],
   ans=1,
   why="A chi-square test detects association only, and the scope-of-inference rules from Unit 1 apply here exactly as they do to every other inference procedure."),
]
