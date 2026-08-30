# AP STATISTICS 3.15 Carrying Out a Chi-Square Test for Homogeneity or
# Independence — 25 questions
# CED: Fall 2026, Unit 3. Learning objectives 3.15.A (calculate expected
# counts), 3.15.B (calculate the statistic and p-value), 3.15.C (interpret the
# p-value) and 3.15.D (justify a claim from the result).
#
#     expected count for a cell = (row total)(column total) / (table total)
#     chi-square statistic      = sum over all cells of (O - E)^2 / E
#     p-value                   = the RIGHT-TAIL area beyond the statistic,
#                                 on the chi-square distribution with
#                                 (rows - 1)(columns - 1) degrees of freedom
#
# The p-value is always a right-tail area, with no doubling and no left tail,
# because a small statistic means observed and expected agree and so supports
# the null. Students who have just finished the two-sided z-tests of 3.13
# reliably double it, and one item is aimed squarely at that.
#
# Three tables carry the computation. Every expected count, cell contribution,
# statistic, degrees of freedom and p-value is recomputed in verify_s3_15.py,
# independently of scipy's own chi2_contingency, and the two are cross-checked.
#
#   TABLE_T1, 2 x 2, df 1:   60  40  /  45  55     chi-square  4.511, p = 0.0337
#     expected 52.5, 47.5, 52.5, 47.5
#   TABLE_T2, 3 x 3, df 4:   40 30 30 / 30 45 25 / 20 35 45
#     every row totals 100, so every expected count is a column total over 3
#     chi-square 16.349, p = 0.0026
#   TABLE_T3, 3 x 2, df 2:   30 20 / 25 25 / 15 35   chi-square 9.375, p = 0.0092
TOPIC = ("3.15", "Carrying Out a Chi-Square Test for Homogeneity or Independence", 3)

TABLE_T1 = dict(
    headers=["Group", "Yes", "No", "Total"],
    rows=[["Group 1", "60", "40", "100"],
          ["Group 2", "45", "55", "100"],
          ["Total", "105", "95", "200"]])

TABLE_T2 = dict(
    headers=["Group", "Option A", "Option B", "Option C", "Total"],
    rows=[["Group 1", "40", "30", "30", "100"],
          ["Group 2", "30", "45", "25", "100"],
          ["Group 3", "20", "35", "45", "100"],
          ["Total", "90", "110", "100", "300"]])

TABLE_T3 = dict(
    headers=["Group", "Agree", "Disagree", "Total"],
    rows=[["Group 1", "30", "20", "50"],
          ["Group 2", "25", "25", "50"],
          ["Group 3", "15", "35", "50"],
          ["Total", "70", "80", "150"]])

QUESTIONS = [
 dict(q="The expected count for a cell of a two-way table, under the null hypothesis of a chi-square test, is calculated as",
   choices=[
     "the row total times the column total, divided by the table total",
     "the row total plus the column total, divided by the table total",
     "the table total divided by the number of cells",
     "the observed count divided by the table total",
     "the row total divided by the column total"],
   ans=0,
   why="Under the null the cell's share of the table is the product of its row share and its column share, which gives row total times column total over the grand total."),

 dict(q="The chi-square test statistic is calculated as",
   choices=[
     "the sum over all cells of the observed count minus the expected count",
     "the sum over all cells of the squared difference between observed and expected, divided by the expected count",
     "the sum over all cells of the squared difference between observed and expected, divided by the observed count",
     "the largest single difference between observed and expected",
     "the sum of all the expected counts"],
   ans=1,
   why="Squaring stops positive and negative discrepancies from cancelling, and dividing by the expected count is what makes the contribution relative to how many were expected."),

 dict(q="For a chi-square test, the p-value is",
   choices=[
     "the right-tail area beyond the test statistic",
     "the left-tail area below the test statistic",
     "twice the right-tail area beyond the test statistic",
     "the area between plus and minus the test statistic",
     "the value of the test statistic itself"],
   ans=0,
   why="Only a large statistic indicates a departure from the null, so the evidence lies entirely in the upper tail and nothing is doubled."),

 dict(q="A two-way table of 200 responses is shown. What is the expected count for the Group 1, Yes cell?",
   table=TABLE_T1,
   choices=["47.5", "50.0", "52.5", "57.5", "60.0"],
   ans=2,
   why="The row total is 100 and the column total is 105, so the expected count is (100)(105)/200 = 52.5."),

 dict(q="For that same 2-by-2 table, the expected count for the Group 1, No cell is",
   table=TABLE_T1,
   choices=["40.0", "45.0", "47.5", "52.5", "55.0"],
   ans=2,
   why="(100)(95)/200 = 47.5; note that the two expected counts in the row sum to the row total of 100."),

 dict(q="For that same 2-by-2 table, the contribution of the Group 1, Yes cell to the chi-square statistic is closest to",
   table=TABLE_T1,
   choices=["0.143", "1.071", "1.184", "4.511", "7.500"],
   ans=1,
   why="The cell contributes (60 - 52.5) squared divided by 52.5, which is 56.25/52.5 = 1.071."),

 dict(q="For that same 2-by-2 table, the chi-square statistic is closest to",
   table=TABLE_T1,
   choices=["1.071", "2.143", "4.511", "7.500", "9.022"],
   ans=2,
   why="The four cell contributions are 1.071, 1.184, 1.071 and 1.184, and they total 4.511."),

 dict(q="For that same 2-by-2 table, the degrees of freedom are",
   table=TABLE_T1,
   choices=["1", "2", "3", "4", "199"],
   ans=0,
   why="(2 - 1)(2 - 1) = 1; the sample size of 200 plays no part."),

 dict(q="For that 2-by-2 table with a chi-square statistic of 4.511 on 1 degree of freedom, the p-value is closest to",
   table=TABLE_T1,
   choices=["0.0168", "0.0337", "0.0674", "0.9663", "4.5110"],
   ans=1,
   why="The right-tail area beyond 4.511 on 1 degree of freedom is 0.0337; 0.0674 is what doubling it would give, which a chi-square test never does."),

 dict(q="For that table with a p-value of 0.0337, the decision at alpha = 0.05 is to",
   table=TABLE_T1,
   choices=[
     "reject the null hypothesis, since 0.0337 is less than 0.05",
     "fail to reject the null hypothesis",
     "accept the null hypothesis",
     "conclude the two groups are identical",
     "recompute the expected counts"],
   ans=0,
   why="The p-value falls below the significance level, so there is convincing evidence that the distributions differ."),

 dict(q="A 3-by-3 table of 300 responses is shown, in which each row totals 100. What is the expected count for the Group 1, Option B cell?",
   table=TABLE_T2,
   choices=["30.00", "33.33", "36.67", "40.00", "110.00"],
   ans=2,
   why="(100)(110)/300 = 36.67; because every row total is 100, every cell in the Option B column has this same expected count."),

 dict(q="For that same 3-by-3 table, the expected count for the Group 3, Option A cell is",
   table=TABLE_T2,
   choices=["20.00", "30.00", "33.33", "36.67", "90.00"],
   ans=1,
   why="(100)(90)/300 = 30.00, the same as for every other cell in the Option A column, since all three row totals are equal."),

 dict(q="For that same 3-by-3 table, the degrees of freedom are",
   table=TABLE_T2,
   choices=["2", "4", "6", "8", "9"],
   ans=1,
   why="(3 - 1)(3 - 1) = 4."),

 dict(q="For that same 3-by-3 table, the chi-square statistic is closest to",
   table=TABLE_T2,
   choices=["4.511", "9.488", "16.349", "24.000", "32.697"],
   ans=2,
   why="Summing the nine contributions of (O - E) squared over E gives 16.349; 9.488 is the critical value at alpha = 0.05 with 4 degrees of freedom, not the statistic."),

 dict(q="For that 3-by-3 table with a chi-square statistic of 16.349 on 4 degrees of freedom, the p-value is closest to",
   table=TABLE_T2,
   choices=["0.0013", "0.0026", "0.0052", "0.9974", "16.3490"],
   ans=1,
   why="The right-tail area beyond 16.349 on 4 degrees of freedom is 0.0026, which is strong evidence against the null."),

 dict(q="A 3-by-2 table of 150 responses is shown, in which each row totals 50. What is the expected count for the Group 1, Agree cell?",
   table=TABLE_T3,
   choices=["20.00", "23.33", "25.00", "26.67", "30.00"],
   ans=1,
   why="(50)(70)/150 = 23.33."),

 dict(q="For that same 3-by-2 table, the degrees of freedom and chi-square statistic are closest to",
   table=TABLE_T3,
   choices=[
     "2 and 9.375",
     "1 and 9.375",
     "2 and 5.992",
     "4 and 9.375",
     "2 and 18.750"],
   ans=0,
   why="(3 - 1)(2 - 1) = 2 degrees of freedom, and the six cell contributions total 9.375."),

 dict(q="For that 3-by-2 table with a chi-square statistic of 9.375 on 2 degrees of freedom, the p-value is closest to",
   table=TABLE_T3,
   choices=["0.0046", "0.0092", "0.0184", "0.9908", "9.3750"],
   ans=1,
   why="The right-tail area beyond 9.375 on 2 degrees of freedom is 0.0092."),

 dict(q="A student computes a chi-square p-value and then doubles it because the alternative hypothesis 'goes both ways'. This is wrong because",
   choices=[
     "a chi-square alternative is not directional, and any departure from the null in any direction already produces a LARGE statistic, so all the evidence lies in one tail",
     "the p-value should be halved instead",
     "chi-square p-values are always exactly 0.05",
     "doubling is required only for tables larger than 2 by 2",
     "the student should have used the left tail"],
   ans=0,
   why="Discrepancies in every cell, in either direction, are squared and added, so they all push the statistic up; there is no second tail to account for."),

 dict(q="Within a two-way table, the cell contributing most to a large chi-square statistic is",
   choices=[
     "the cell with the largest observed count",
     "the cell with the largest value of (observed minus expected) squared divided by expected",
     "the cell with the largest expected count",
     "the cell in the first row and first column",
     "always the cell with the smallest count"],
   ans=1,
   why="Examining the individual cell contributions is how a significant result is followed up, since the test itself says only that some departure exists."),

 dict(q="A chi-square test gives a p-value of 0.0026. Interpreted in context, this means that",
   choices=[
     "there is a 0.26% probability that the null hypothesis is true",
     "assuming the null hypothesis is true, there is a 0.26% chance of obtaining a chi-square statistic at least as large as the one observed",
     "0.26% of the observations fall in the wrong cells",
     "the association is 0.26% strong",
     "the test should be repeated"],
   ans=1,
   why="As with every p-value, the probability is computed assuming the null, and it concerns results at least as extreme as the one observed, stated in context."),

 dict(q="After rejecting the null in a chi-square test for homogeneity across three groups, the correct conclusion is that",
   choices=[
     "there is convincing evidence that the distributions of the categorical variable are not all the same across the three groups",
     "all three groups differ from one another",
     "Group 1 has the largest proportion",
     "the variables are independent",
     "one group causes the difference"],
   ans=0,
   why="The test detects that a difference exists somewhere; it does not identify which groups differ, nor rank them, nor establish causation."),

 dict(q="A chi-square test yields a p-value of 0.28. The correct conclusion is to",
   choices=[
     "reject the null hypothesis",
     "fail to reject the null hypothesis; there is not convincing evidence of a difference or association",
     "accept the null hypothesis and conclude the distributions are identical",
     "conclude the variables are independent",
     "conclude the sample was too small"],
   ans=1,
   why="A large p-value means the observed table is the sort the null routinely produces, which leaves the null unrejected rather than established."),

 dict(q="Doubling every count in a two-way table, so that the table's shape is unchanged but the sample size doubles, has what effect on the chi-square statistic?",
   choices=[
     "no effect",
     "it doubles the statistic, and so lowers the p-value, since the same pattern in a larger sample is stronger evidence",
     "it halves the statistic",
     "it squares the statistic",
     "it changes the degrees of freedom"],
   ans=1,
   why="Every expected count doubles, each numerator quadruples and each denominator doubles, so every contribution doubles; the degrees of freedom, depending only on shape, are unchanged."),

 dict(q="A chi-square statistic is computed for a table in which every observed count exactly equals its expected count. The p-value is",
   choices=["0", "0.05", "0.50", "1", "undefined"],
   ans=3,
   why="The statistic is 0, and the entire chi-square distribution lies at or above 0, so the right-tail area is 1 and the data give no evidence at all against the null."),
]
