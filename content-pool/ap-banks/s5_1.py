# AP STATISTICS 5.1 Graphical Representations Between Two Quantitative Variables
# - 25 questions
# CED: AP Statistics Course and Exam Description, Effective Fall 2026, Unit 5.
# Objectives 5.1.A (a bivariate data set is ordered pairs collected from the
# SAME individuals; the explanatory variable goes on the x-axis and the response
# on the y-axis), 5.1.B (describe form, direction, strength and unusual
# features), 5.1.C (justify a claim from a scatterplot).
# There are no figures in this bank, so every item that would normally show a
# scatterplot gives the ordered pairs as a list or a table in the stem instead.
# Whatever a stem asserts about direction, form or strength is confirmed in
# verify_s5_1.py by computing the correlation and the fitted line from those
# same numbers with numpy and scipy.stats.linregress.
TOPIC = ("5.1", "Graphical Representations Between Two Quantitative Variables", 5)
QUESTIONS = [

 dict(q="A researcher records the number of hours studied and the score earned for each of several students, and wants to use hours to predict score. In a scatterplot of these data, which variable belongs on the horizontal axis?", choices=[
   "Hours studied, because it is the explanatory variable",
   "Score, because it is the explanatory variable",
   "Hours studied, because it is the response variable",
   "Score, because it is the larger of the two numbers",
   "Either variable, because a scatterplot is symmetric in its two variables"], ans=0,
   why="CED 5.1.A.2: the explanatory variable, the one used to explain or predict, is plotted on the x-axis, and the response variable on the y-axis; swapping them changes the regression line that would be fitted."),

 dict(q="Which of the following is required for a set of measurements to form a bivariate quantitative data set suitable for a scatterplot?", choices=[
   "Both values in each ordered pair are measured on the same individual",
   "The two variables are measured on two separate groups of individuals",
   "The two variables have the same units",
   "The two variables have the same mean",
   "One of the two variables is categorical"], ans=0,
   why="CED 5.1.A.1: the ordered pairs come from the same individuals, which is what makes pairing the values meaningful; two variables measured on different groups cannot be paired at all."),

 dict(q="A scatterplot of eight ordered pairs would show the points (1, 3), (2, 5), (3, 6), (4, 8), (5, 9), (6, 11), (7, 12), (8, 14). Which description of the association is best?", choices=[
   "Positive, linear and strong",
   "Positive, linear and weak",
   "Negative, linear and strong",
   "Positive, non-linear and strong",
   "No association"], ans=0,
   why="As x increases y increases steadily by about 1.5 each time, so the association is positive and linear, and the points lie very close to a straight line, which is a strong association."),

 dict(q="A scatterplot would show the points (2, 95), (4, 88), (6, 80), (8, 74), (10, 66), (12, 59). Which description is best?", choices=[
   "Negative, linear and strong",
   "Negative, linear and weak",
   "Positive, linear and strong",
   "Negative, non-linear and strong",
   "No association"], ans=0,
   why="Every increase of 2 in x is matched by a drop of about 7 in y, giving a negative direction, a linear form and points that hug a straight line, which is strong."),

 dict(q="A scatterplot would show the points (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49). Which description is best?", choices=[
   "Positive, non-linear and strong",
   "Positive, linear and strong",
   "Negative, non-linear and strong",
   "Positive, non-linear and weak",
   "No association"], ans=0,
   why="The y-values rise by 3, 5, 7, 9, 11 and 13, an increasing rate that curves upward, so the form is non-linear even though the pattern is followed very closely."),

 dict(q="A scatterplot would show the points (1, 6), (2, 4), (3, 7), (4, 5), (5, 8), (6, 5), (7, 7), (8, 6). Which description is best?", choices=[
   "Weak positive association with no clear form",
   "Strong positive linear association",
   "Strong negative linear association",
   "Perfect linear association",
   "Strong non-linear association"], ans=0,
   why="The y-values drift up and down as x increases with only a slight upward tendency, so any association is weak and no clear form emerges."),

 dict(q="What does a POSITIVE association between two quantitative variables mean?", choices=[
   "As values of the explanatory variable increase, values of the response variable tend to increase",
   "Both variables take only positive values",
   "The response variable increases by the same amount for every unit increase in the explanatory variable",
   "The correlation coefficient equals 1",
   "The explanatory variable causes the response variable to increase"], ans=0,
   why="CED 5.1.B.3 defines direction as a tendency; it does not require constant increments, a perfect correlation, or any causal relationship."),

 dict(q="The strength of an association shown in a scatterplot refers to", choices=[
   "how closely the points follow the general pattern",
   "how steep the general pattern is",
   "how many points are plotted",
   "how far the points are from the origin",
   "how large the values of the response variable are"], ans=0,
   why="CED 5.1.B.4: strength is about scatter around the pattern, not about slope; a steep line with widely scattered points is a weak association, and a shallow line with tight points is a strong one."),

 dict(q="A scatterplot of daily high temperature and ice cream sales shows most points forming one upward band, plus three points far above the band on days when a festival was held. How should those three points be described?", choices=[
   "As an unusual feature of the scatterplot, since they do not fit the general pattern",
   "As evidence that the association is negative",
   "As proof that temperature does not affect sales",
   "As points that should be deleted before any description is written",
   "As a second explanatory variable"], ans=0,
   why="CED 5.1.B.5 counts clusters and points that do not fit the general pattern as unusual features to be described; deleting them because they are inconvenient is not justified."),

 dict(q="A scatterplot of two quantitative variables shows two distinct groups of points, one for each of two manufacturing plants. What is this an example of?", choices=[
   "Clustering, an unusual feature that should be mentioned in the description",
   "A negative association",
   "A non-linear form",
   "An error in the data collection",
   "A perfect correlation"], ans=0,
   why="CED 5.1.B.5 lists clusters among the unusual features; here the clusters signal that a third variable, the plant, is at work."),

 dict(q="Which of the following would be described as a strong negative linear association?", choices=[
   "The points lie tightly along a line that falls from upper left to lower right",
   "The points lie tightly along a line that rises from lower left to upper right",
   "The points are widely scattered with a slight downward drift",
   "The points lie tightly along a downward-opening curve",
   "The points form a horizontal band"], ans=0,
   why="A falling pattern gives the negative direction, a straight pattern gives the linear form, and points lying tightly along it gives the strength; a curve is non-linear no matter how tight it is."),

 dict(q="A table records six ordered pairs of (age of car in years, resale value in thousands): (1, 18), (2, 16), (3, 15), (4, 13), (5, 12), (6, 10). Which claim is best justified by a scatterplot of these data?", choices=[
   "Older cars in this sample tend to have lower resale values, and the pattern is close to linear",
   "Age has no relationship with resale value",
   "The relationship is positive and non-linear",
   "Increasing a car's age causes an increase in resale value",
   "Every car aged 7 years is worth exactly 8 thousand"], ans=0,
   why="Value falls by about 1.54 thousand per year of age with very little scatter, which supports a negative, nearly linear description; predicting a specific value at age 7 goes beyond the data."),

 dict(q="A scatterplot shows a clear upward pattern with substantial scatter. Which pair of descriptors fits best?", choices=[
   "Positive direction, moderate strength",
   "Negative direction, strong strength",
   "Positive direction, perfect strength",
   "No direction, strong strength",
   "Negative direction, weak strength"], ans=0,
   why="An upward pattern is positive, and substantial scatter around it rules out both a strong and a perfect description while an upward pattern rules out negative."),

 dict(q="Two students plot the same data set. One puts hours of exercise on the x-axis and resting heart rate on the y-axis; the other reverses them. What changes?", choices=[
   "Which variable is treated as explanatory, and therefore which regression line would be fitted",
   "The direction of the association",
   "The strength of the association",
   "The number of points plotted",
   "Nothing at all, since the same pairs are shown"], ans=0,
   why="Direction and strength are properties of the pairs and do not depend on the axes, but the roles of explanatory and response, and hence the least-squares line that predicts one from the other, do change."),

 dict(q="A scatterplot of six points shows (10, 22), (12, 19), (14, 24), (16, 21), (18, 26), (20, 23). Which description is best?", choices=[
   "A weak to moderate positive association with considerable scatter",
   "A strong positive linear association",
   "A strong negative linear association",
   "A perfect zigzag association",
   "No association whatsoever, since the values alternate"], ans=0,
   why="The y-values alternate down and up while drifting upward overall, so there is a mild positive tendency with a great deal of scatter around it; the alternation does not eliminate the tendency."),

 dict(q="Which claim canNOT be justified from a scatterplot alone, no matter how strong the pattern?", choices=[
   "That changes in the explanatory variable cause changes in the response variable",
   "That the association is positive",
   "That the form appears linear",
   "That certain points do not fit the general pattern",
   "That the association is strong"], ans=0,
   why="Direction, form, strength and unusual features are all visible in the plot, but a causal claim requires a randomized experiment or an argument that rules out other explanations."),

 dict(q="A scatterplot of a company's monthly advertising spending and monthly sales shows a strong upward linear pattern. A manager concludes that spending more on advertising will raise sales. What is the weakness in that reasoning?", choices=[
   "The data are observational, so a lurking variable such as overall demand could produce the pattern",
   "A strong pattern always indicates a non-linear relationship",
   "The scatterplot cannot show direction",
   "Sales should have been placed on the x-axis",
   "There is no weakness, because the pattern is strong"], ans=0,
   why="Months with high demand may see both more advertising and more sales; only a design that assigns spending levels could separate the effect of advertising from that of demand."),

 dict(q="In a study of children, height is plotted against age. Which is the response variable?", choices=[
   "Height, because it is being predicted from age",
   "Age, because it is being predicted from height",
   "Height, because it is measured in centimeters",
   "Age, because it is measured first",
   "Neither, because both are quantitative"], ans=0,
   why="The response variable is the one being explained or predicted, so height is the response and age the explanatory variable; both being quantitative is what makes the scatterplot possible, not what decides the roles."),

 dict(q="Which of the following describes the FORM of an association?", choices=[
   "Whether the pattern is linear or non-linear",
   "Whether the pattern rises or falls",
   "How tightly the points follow the pattern",
   "How many points lie far from the pattern",
   "Which variable was placed on the x-axis"], ans=0,
   why="CED 5.1.B.2 defines form as linear or non-linear; rising or falling is direction, tightness is strength, and stray points are unusual features."),

 dict(q="A scatterplot shows points that rise steeply from left to right but are spread widely around that rising trend. A student says the association must be strong because the rise is steep. What is the error?", choices=[
   "Steepness is not strength; strength is about how closely the points follow the pattern",
   "Steepness is not direction; the association is actually negative",
   "A steep rise means the form is non-linear",
   "Strength cannot be judged from a scatterplot at all",
   "There is no error"], ans=0,
   why="A steep pattern with wide scatter is a weak association, and a shallow pattern with tight points is a strong one; slope and strength are separate features."),

 dict(q="A table of five ordered pairs is given: (3, 12), (5, 17), (7, 22), (9, 27), (11, 32). What does a scatterplot of these points show?", choices=[
   "A perfectly linear positive association, since y rises by exactly 5 for each rise of 2 in x",
   "A perfectly linear negative association",
   "A non-linear positive association",
   "A weak positive association",
   "No association"], ans=0,
   why="The increments in y are constant at 5 for every increase of 2 in x, so all five points lie exactly on one line rising to the right."),

 dict(q="Why must both variables be quantitative for a scatterplot?", choices=[
   "Each axis needs a numerical scale on which a point can be located",
   "Because categorical variables cannot be measured on the same individual",
   "Because a scatterplot always shows a linear pattern",
   "Because the correlation coefficient requires equal units",
   "Because otherwise the explanatory and response roles cannot be assigned"], ans=0,
   why="Plotting an ordered pair requires a numerical position on each axis; categorical pairs are displayed with two-way tables and segmented bar charts instead."),

 dict(q="A scatterplot of 40 points shows a rising pattern for the first 30 points and then flattens for the last 10. How is the form best described?", choices=[
   "Non-linear, because the rate of increase changes across the range of x",
   "Linear, because the overall direction is upward",
   "Linear, because most of the points rise",
   "No form, because two patterns appear",
   "Negative, because the pattern eventually flattens"], ans=0,
   why="A single straight line cannot describe a pattern whose rate of change shifts; the direction remains positive throughout, but the form is curved."),

 dict(q="Which statement about a scatterplot showing a strong linear pattern with one point far from the pattern is best?", choices=[
   "The description should report the strong linear form and separately note the unusual point",
   "The unusual point proves the association is non-linear",
   "The unusual point should be removed and never mentioned",
   "The presence of one unusual point makes the association weak by definition",
   "The unusual point shows that the explanatory and response variables were reversed"], ans=0,
   why="CED 5.1.B.1 asks for form, direction, strength and unusual features together; a single stray point is reported as an unusual feature rather than allowed to redefine the form or to be quietly discarded."),

 dict(q="A scatterplot of two quantitative variables shows points scattered with no upward or downward tendency and no curve. What should the description say?", choices=[
   "There is no apparent association between the two variables",
   "There is a strong association with no direction",
   "There is a weak negative linear association",
   "The form is linear with slope 0, so the association is strong",
   "The scatterplot was constructed incorrectly"], ans=0,
   why="With neither a direction nor a curved pattern there is nothing for form or strength to describe; a horizontal band means the response does not tend to change with the explanatory variable."),
]
