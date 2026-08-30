# AP STATISTICS 5.2 Correlation - 25 questions
# CED: AP Statistics Course and Exam Description, Effective Fall 2026, Unit 5.
# Objective 5.2.A: r summarizes the strength and direction of the LINEAR
# association between two quantitative variables; it is unit-free and always
# between -1 and 1; r = 0 means no linear association and r = +/-1 a perfect
# one; an r close to +/-1 does NOT by itself mean a linear model is appropriate
# (5.2.A.3); and correlation does not imply causation (5.2.A.4).
# Two consequences of the definition that the CED does not spell out but that
# every AP student meets are tested here and confirmed numerically in
# verify_s5_2.py: r is unchanged by a linear rescaling of either variable
# (including a change of units), and r is unchanged by swapping which variable
# is called x -- because r standardizes both variables before combining them.
TOPIC = ("5.2", "Correlation", 5)
QUESTIONS = [

 dict(q="Which of the following is a possible value of a correlation coefficient?", choices=[
   "-1.20",
   "-0.85",
   "1.40",
   "2.00",
   "-3.00"], ans=1,
   why="CED 5.2.A.1: r always lies between -1 and 1 inclusive, so only -0.85 is possible."),

 dict(q="A correlation coefficient of r = 0 between two quantitative variables means", choices=[
   "there is no linear association between the two variables",
   "there is no association of any kind between the two variables",
   "the two variables are independent",
   "one variable is constant",
   "the scatterplot has no points"], ans=0,
   why="CED 5.2.A.2: r measures LINEAR association only, so r = 0 rules out a linear trend but leaves a strong curved relationship perfectly possible."),

 dict(q="The heights of a group of people are recorded in inches and their arm spans in inches, giving r = 0.94. If the heights are converted to centimeters and the correlation recomputed, what is the new value of r?", choices=[
   "0.94",
   "0.37",
   "2.39",
   "0.94 divided by 2.54",
   "It cannot be determined without the data"], ans=0,
   why="CED 5.2.A.1: r is unit-free, so multiplying every height by 2.54 leaves it unchanged; a correlation carries no units to convert."),

 dict(q="For a data set the correlation between x and y is 0.83. What is the correlation between y and x?", choices=[
   "0.83",
   "-0.83",
   "1/0.83",
   "0.69",
   "It depends on which variable is explanatory"], ans=0,
   why="Correlation standardizes both variables before combining them, so it is symmetric in the two; the roles of explanatory and response affect the regression line but not r."),

 dict(q="For the six pairs (2, 14), (4, 19), (5, 20), (7, 26), (9, 31), (11, 36), the correlation is about 0.998. If every y-value were doubled and then increased by 5, what would the new correlation be?", choices=[
   "0.998",
   "1.996",
   "0.499",
   "2.001",
   "0.501"], ans=0,
   why="A linear rescaling of one variable leaves the standardized values unchanged in size and sign, so r is unchanged at 0.998; only reversing the sign of a variable would change r, and then only its sign."),

 dict(q="For the same six pairs, if every y-value were multiplied by -1, what would the correlation become?", choices=[
   "-0.998",
   "0.998",
   "0.000",
   "-1.000",
   "1.000"], ans=0,
   why="Negating one variable reverses the direction of every standardized product, so r keeps its magnitude and flips sign."),

 dict(q="The correlation between two quantitative variables is 0.94. What is the coefficient of determination, and what does it mean?", choices=[
   "0.884; about 88.4 percent of the variation in the response variable is explained by the linear relationship with the explanatory variable",
   "0.884; about 88.4 percent of the data points lie on the regression line",
   "0.970; about 97.0 percent of the variation is explained",
   "0.884; the response variable increases 88.4 percent as fast as the explanatory variable",
   "0.94; the correlation itself gives the percent of variation explained"], ans=0,
   why="CED 5.5.A.5: the coefficient of determination is r^2 = 0.94^2 = 0.884, the proportion of variation in the response explained by the linear relationship; it is not the share of points lying on the line."),

 dict(q="A regression of y on x reports r^2 = 0.49, and the scatterplot shows a falling pattern. What is r?", choices=[
   "-0.70",
   "0.70",
   "-0.24",
   "0.24",
   "-0.49"], ans=0,
   why="Taking the square root of 0.49 gives 0.70 in magnitude, and the falling pattern fixes the sign as negative; r^2 alone cannot supply the sign."),

 dict(q="The correlation between the number of firefighters sent to a fire and the damage caused is strongly positive. What does this show?", choices=[
   "Nothing about causation; the size of the fire plausibly drives both variables",
   "That sending firefighters causes damage",
   "That damage causes firefighters to be sent, so the causation runs the other way",
   "That the correlation must have been computed incorrectly",
   "That the association is non-linear"], ans=0,
   why="CED 5.2.A.4: correlation does not imply causation, and here a lurking variable, the severity of the fire, raises both the response sent and the damage done."),

 dict(q="A scatterplot of seven points shows a clear U-shaped pattern: (1, 7), (2, 4), (3, 2), (4, 1), (5, 2), (6, 4), (7, 7). What is the approximate correlation, and what does it tell you?", choices=[
   "About 0; there is no LINEAR association, even though there is a very strong curved one",
   "About 1; the pattern is strong, so the correlation must be near 1",
   "About -1; the pattern falls before it rises",
   "About 0.5; a moderate association",
   "The correlation is undefined for a curved pattern"], ans=0,
   why="The falling and rising halves contribute standardized products of opposite sign that cancel, so r is essentially 0 even though the points follow a curve almost exactly; r measures only the linear part."),

 dict(q="A researcher reports r = 0.97 for a bivariate data set and concludes that a linear model is appropriate. What is the flaw?", choices=[
   "A high correlation does not confirm linearity; a curved pattern can produce a high r, so the residual plot must be examined",
   "There is no flaw; r above 0.95 always confirms linearity",
   "The value 0.97 is impossible for real data",
   "The researcher should have used r^2 = 0.94 instead",
   "The flaw is that r has no units"], ans=0,
   why="CED 5.2.A.3 says exactly this: an r near 1 does not necessarily mean a linear model is appropriate, which is why the form is checked with a residual plot rather than with r."),

 dict(q="Which correlation indicates the strongest linear association?", choices=[
   "-0.92",
   "-0.45",
   "0.00",
   "0.38",
   "0.85"], ans=0,
   why="CED 5.2.A.2: strength is measured by how close r is to -1 or 1, and |-0.92| = 0.92 exceeds |0.85|; the negative sign describes direction, not weakness."),

 dict(q="For the five pairs (1, 10), (2, 8), (3, 9), (4, 7), (5, 6), the correlation is -0.90. Which description is best?", choices=[
   "A strong negative linear association",
   "A weak negative linear association",
   "A strong positive linear association",
   "No linear association",
   "A perfect negative linear association"], ans=0,
   why="A value of -0.90 is close to -1, which is a strong association, and its sign is negative; only r = -1 exactly would be perfect."),

 dict(q="Six points lie exactly on a rising line, giving r = 1. One point is then moved far below the line, and the correlation is recomputed as about 0.23. What does this illustrate?", choices=[
   "Correlation is not resistant: a single point far from the pattern can change r dramatically",
   "Correlation is resistant, since five of the six points are unchanged",
   "Correlation can exceed 1 when a point is moved",
   "Moving a point always makes r negative",
   "The recomputed value must be an arithmetic error"], ans=0,
   why="Every point contributes to r through its standardized deviations, so one point far from the pattern can dominate the sum; correlation, like the mean, is not resistant."),

 dict(q="Two variables have correlation r = 0.6. What proportion of the variation in the response variable is NOT explained by the linear relationship with the explanatory variable?", choices=[
   "0.64",
   "0.36",
   "0.40",
   "0.60",
   "0.16"], ans=0,
   why="The explained proportion is r^2 = 0.36, so the unexplained proportion is 1 - 0.36 = 0.64; 0.40 is the mistake of using 1 - r."),

 dict(q="Which statement about the correlation coefficient is FALSE?", choices=[
   "Its value depends on the units in which the two variables are measured",
   "It always lies between -1 and 1 inclusive",
   "It measures only the strength and direction of a linear association",
   "Its value is unchanged if the explanatory and response variables are swapped",
   "A value near 1 does not guarantee that a linear model fits well"], ans=0,
   why="CED 5.2.A.1 states that r is unit-free; the other four statements are all true of correlation."),

 dict(q="A study finds a correlation of 0.72 between the number of hours of television watched per week and body mass index in a random sample of adults. Which conclusion is justified?", choices=[
   "Adults who watch more television tend to have higher body mass index, but the study cannot establish that television causes the difference",
   "Watching television causes body mass index to rise",
   "Higher body mass index causes people to watch more television",
   "There is no relationship, because the study is observational",
   "The correlation must be recomputed as an experiment"], ans=0,
   why="An observational study can establish an association and its direction, but only random assignment of the explanatory variable could support a causal claim."),

 dict(q="For a data set, r = -1 exactly. What must be true?", choices=[
   "Every point lies exactly on a single line with negative slope",
   "Every point lies exactly on a single line with positive slope",
   "The two variables are unrelated",
   "The response variable is constant",
   "The scatterplot shows a downward-opening curve"], ans=0,
   why="CED 5.2.A.2: r = -1 is a perfect negative linear association, which requires every point to lie on one falling line; a curve could never give a correlation of exactly -1."),

 dict(q="Which pair of correlations describes associations of equal strength but opposite direction?", choices=[
   "0.63 and -0.63",
   "0.63 and 0.37",
   "0.63 and -0.37",
   "0.36 and -0.63",
   "0.63 and 1.63"], ans=0,
   why="Strength is |r| and direction is the sign, so two values with the same magnitude and opposite signs describe equally strong associations running opposite ways."),

 dict(q="A correlation of 0.05 is found between shoe size and score on a history exam among adults. What is the most reasonable interpretation?", choices=[
   "There is essentially no linear association between the two variables in this group",
   "There is a strong association, because the correlation is positive",
   "Shoe size slightly causes higher history scores",
   "The variables must be measured in the same units before r is meaningful",
   "The value proves the two variables are independent"], ans=0,
   why="A correlation this close to 0 means the linear trend is negligible; it neither proves independence, since a curved relationship could still exist, nor supports any causal claim."),

 dict(q="A least-squares regression of y on x gives r = 0.8. Which quantity equals 0.64?", choices=[
   "The proportion of the variation in y explained by the linear relationship with x",
   "The proportion of the data points lying on the regression line",
   "The slope of the regression line",
   "The correlation between y and x",
   "The proportion of the variation in x explained by y"], ans=0,
   why="CED 5.5.A.5 defines r^2 = 0.64 as the proportion of variation in the RESPONSE explained by the linear relationship; it is not a count of points and not a slope."),

 dict(q="Two data sets have correlations 0.42 and -0.79. Which statement is correct?", choices=[
   "The second shows the stronger linear association, and it runs in the negative direction",
   "The first shows the stronger linear association, because 0.42 is greater than -0.79",
   "The two are equally strong, because they have similar magnitudes",
   "The second is weaker, because a negative correlation is always weaker",
   "Neither shows any linear association"], ans=0,
   why="Compare magnitudes: |-0.79| = 0.79 exceeds |0.42|, so the second is stronger; the negative sign says the association falls, not that it is weak."),

 dict(q="A data set has correlation r = 0.86 between x and y. A researcher computes the correlation again after adding 10 to every x-value. What is the new correlation?", choices=[
   "0.86",
   "0.096",
   "8.60",
   "0.96",
   "It cannot be determined"], ans=0,
   why="Adding a constant shifts every x-value by the same amount, leaving every deviation from the mean, and therefore every standardized value, unchanged; r is unaffected."),

 dict(q="Which of the following could NOT be concluded from a correlation of 0.95 between two variables in an observational study?", choices=[
   "That changing one variable would change the other",
   "That the points cluster closely around a rising line",
   "That the linear association is strong",
   "That the association is positive in direction",
   "That r^2 is about 0.90"], ans=0,
   why="CED 5.2.A.4: a strong correlation in an observational study leaves lurking variables unruled-out, so a claim about what would happen if one variable were changed is not supported."),

 dict(q="Why is r^2 rather than r usually quoted as a measure of how much of the response is accounted for by the model?", choices=[
   "r^2 is the proportion of the variation in the response explained by the linear relationship, which r is not",
   "r^2 is always larger than r, so it sounds better",
   "r^2 keeps the sign of the association while r does not",
   "r^2 is unit-free while r is not",
   "r^2 is resistant to unusual points while r is not"], ans=0,
   why="CED 5.5.A.5 gives r^2 that interpretation directly; note that for |r| < 1 the square is SMALLER than |r|, both quantities are unit-free, and neither is resistant."),
]
