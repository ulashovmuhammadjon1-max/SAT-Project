# AP STATISTICS 5.4 Residuals - 25 questions
# CED: AP Statistics Course and Exam Description, Effective Fall 2026, Unit 5.
# Objectives 5.4.A (residual = observed y - predicted y), 5.4.B (a POSITIVE
# residual means the model UNDERpredicts and a negative one that it
# OVERpredicts), 5.4.C (a residual plot graphs residuals against predicted
# values or against x; apparent randomness confirms the linear form and
# curvature says the linear model is not the most appropriate one).
# The sign convention is where nearly all the error lives, so it is tested from
# both directions: given the sign, say which way the model erred, and given the
# situation, produce the sign.
# There are no figures in this bank, so a residual plot is described in words or
# given as a table of residuals; every residual quoted is recomputed in
# verify_s5_4.py, including the fact that the residuals of a least-squares fit
# sum to zero.
TOPIC = ("5.4", "Residuals", 5)
QUESTIONS = [

 dict(q="For a particular observation the observed response is 47 and the predicted response from the regression model is 52.3. What is the residual?", choices=[
   "-5.3",
   "0.90",
   "5.3",
   "47.0",
   "99.3"], ans=0,
   why="CED 5.4.A.1: residual = observed - predicted = 47 - 52.3 = -5.3; reversing the subtraction gives the wrong sign and reverses the meaning."),

 dict(q="For a particular observation the observed response is 88 and the predicted response is 81.6. What is the residual, and what does its sign mean?", choices=[
   "6.4; the model underpredicts this observation",
   "6.4; the model overpredicts this observation",
   "-6.4; the model underpredicts this observation",
   "-6.4; the model overpredicts this observation",
   "6.4; the model predicts this observation exactly"], ans=0,
   why="88 - 81.6 = 6.4, and CED 5.4.B.1: a positive residual means the observed value lies above the line, so the model underpredicted it."),

 dict(q="A model is yhat = 14.2 + 2.6x. At x = 9 the observed response is 40. What is the residual?", choices=[
   "-2.4",
   "2.4",
   "25.8",
   "37.6",
   "40.0"], ans=1,
   why="The predicted value is 14.2 + 2.6(9) = 37.6, so the residual is 40 - 37.6 = 2.4."),

 dict(q="A model is yhat = 200 - 3.5x. At x = 24 the observed response is 110. What is the residual, and what does it say about the prediction?", choices=[
   "-6.0; the model overpredicted the response",
   "6.0; the model underpredicted the response",
   "-6.0; the model underpredicted the response",
   "-90.0; the model overpredicted the response",
   "116.0; the model predicted the response exactly"], ans=0,
   why="The predicted value is 200 - 3.5(24) = 116, so the residual is 110 - 116 = -6.0; a negative residual means the observed value fell below the line, so the model overpredicted."),

 dict(q="A residual is -4.7 and the predicted value is 61.2. What was the observed value?", choices=[
   "-4.7",
   "13.0",
   "56.5",
   "65.9",
   "287.6"], ans=2,
   why="From residual = observed - predicted, the observed value is 61.2 + (-4.7) = 56.5."),

 dict(q="What does a residual plot show?", choices=[
   "The residuals plotted against the predicted values or against the explanatory variable",
   "The observed response values plotted against the predicted response values",
   "The observed response values plotted against the explanatory variable",
   "The squared residuals plotted against the correlation",
   "The regression line plotted with the data points"], ans=0,
   why="CED 5.4.C.1 defines a residual plot as a scatterplot of the residuals against the predicted response values or against the explanatory-variable values."),

 dict(q="A residual plot for a linear model shows the points scattered randomly above and below zero with no pattern. What does that indicate?", choices=[
   "The linear model is an appropriate model for these data",
   "The linear model is not appropriate and a curved model is needed",
   "The correlation must be exactly zero",
   "The data contain an influential point",
   "The residuals were computed incorrectly, since they should show a pattern"], ans=0,
   why="CED 5.4.C.3: apparent randomness in a residual plot confirms the linear form of the association and indicates the simple linear model is appropriate."),

 dict(q="A residual plot for a linear model shows a clear U-shaped pattern. What does that indicate?", choices=[
   "The linear model is not the most appropriate model for these data",
   "The linear model is appropriate and the fit is strong",
   "The correlation must be close to 1",
   "The residuals must sum to a large positive number",
   "The explanatory and response variables were reversed"], ans=0,
   why="CED 5.4.C.4: curvature in the residual plot says the linear model is not the most appropriate one, no matter how large the correlation happens to be."),

 dict(q="For the six observations (2, 5), (4, 11), (6, 14), (8, 21), (10, 24), (12, 30), the least-squares line is yhat = 0.4 + 2.443x. What is the residual for the point (6, 14)?", choices=[
   "-15.06",
   "-1.06",
   "1.06",
   "14.00",
   "15.06"], ans=1,
   why="The predicted value is 0.4 + 2.443(6) = 15.06, so the residual is 14 - 15.06 = -1.06, meaning the model overpredicts at x = 6."),

 dict(q="For that same fitted line and those same six points, what is the sum of all six residuals?", choices=[
   "0",
   "6",
   "-1.06",
   "3.43",
   "It depends on the units of the response variable"], ans=0,
   why="Least squares chooses the line so that the residuals balance; their sum is zero for every least-squares fit, which is why the sum cannot be used to judge how well the line fits."),

 dict(q="Why is the sum of the residuals useless as a measure of how well a least-squares line fits the data?", choices=[
   "It is zero for every least-squares line, whether the fit is good or poor",
   "It is always positive, so it cannot distinguish directions",
   "It changes when the units of the response variable change",
   "It equals the correlation coefficient",
   "It cannot be computed without technology"], ans=0,
   why="Positive and negative residuals cancel exactly in a least-squares fit, so the sum carries no information about the size of the errors; squaring them first is what least squares actually minimizes."),

 dict(q="A residual plot shows residuals that are small near the middle of the x-range and grow steadily larger in magnitude toward both ends, with no curvature. What does this suggest?", choices=[
   "The linear form appears acceptable, but the size of the prediction errors is not constant across the range of x",
   "The linear model is clearly wrong and a curve should be fitted",
   "The correlation is exactly zero",
   "The data set contains no unusual points",
   "The residuals must have been computed with the wrong sign"], ans=0,
   why="Fanning residuals without curvature say the form is linear while the spread of the errors changes across x, which is a different concern from the wrong form."),

 dict(q="The residuals for five observations are 2.1, -3.4, 0.6, -1.2 and 1.9. For which observation did the model overpredict by the most?", choices=[
   "The one with residual -3.4",
   "The one with residual 2.1",
   "The one with residual 1.9",
   "The one with residual 0.6",
   "The one with residual -1.2"], ans=0,
   why="Overprediction means a negative residual, and -3.4 is the most negative, so the model missed high by 3.4 there."),

 dict(q="A point lies exactly on the least-squares regression line. What is its residual?", choices=[
   "0",
   "1",
   "-1",
   "The value of the response variable",
   "It cannot be determined without the slope"], ans=0,
   why="The residual is the vertical distance from the point to the line, so a point on the line has observed equal to predicted and a residual of exactly 0."),

 dict(q="A model is yhat = 6.5 + 0.9x. Three observations give (x, y) pairs of (10, 16.0), (20, 25.0) and (30, 32.5). Which has the residual largest in magnitude?", choices=[
   "The observation at x = 30, with residual -1.0",
   "The observation at x = 10, with residual 0.5",
   "The observation at x = 20, with residual 0.5",
   "The observation at x = 30, with residual 1.0",
   "All three have equal residuals"], ans=0,
   why="The predicted values are 15.5, 24.5 and 33.5, so the residuals are 0.5, 0.5 and -1.0, and the third is the largest in magnitude."),

 dict(q="A student says a residual of 0 means the linear model is a good model for the whole data set. What is the flaw?", choices=[
   "A residual of 0 describes one observation only; the model's adequacy is judged from the whole residual plot",
   "A residual can never equal 0",
   "A residual of 0 means the model overpredicts",
   "A residual of 0 means the correlation is 1",
   "There is no flaw"], ans=0,
   why="One point falling on the line says nothing about the others; CED 5.4.C.2 makes the appropriateness of the model a question about the pattern in the residual plot."),

 dict(q="A regression model consistently predicts values that are too high for small x, too low for middle x, and too high again for large x. What will the residual plot look like, and what does it say?", choices=[
   "It will show curvature, indicating the linear model is not the most appropriate one",
   "It will show random scatter, indicating the linear model is appropriate",
   "It will show all residuals equal to zero",
   "It will show a straight line with positive slope",
   "It will show that the correlation must be negative"], ans=0,
   why="Residuals that run negative, positive, then negative trace out a curve, and CED 5.4.C.4 reads curvature as a sign that a line is the wrong form."),

 dict(q="Which quantity does least-squares regression minimize?", choices=[
   "The sum of the squared residuals",
   "The sum of the residuals",
   "The largest residual",
   "The number of negative residuals",
   "The correlation coefficient"], ans=0,
   why="CED 5.5.A.1: the line is fitted by minimizing the sum of the squares of the residuals, which is why it is called the least-squares regression line; the plain sum is zero for any such line."),

 dict(q="A model is yhat = 42.0 - 1.25x. At x = 16 the observed value is 22.0. What is the residual?", choices=[
   "-2.0",
   "0.0",
   "2.0",
   "20.0",
   "22.0"], ans=1,
   why="The predicted value is 42.0 - 1.25(16) = 42.0 - 20.0 = 22.0, exactly the observed value, so the residual is 0."),

 dict(q="Two models are fitted to the same data. Model A has residuals 3, -2, 1, -3, 1 and Model B has residuals 8, -7, 2, -6, 3. Which fits better, and on what basis?", choices=[
   "Model A, because its residuals are smaller in magnitude",
   "Model B, because its residuals sum to zero",
   "Model B, because it has the larger individual residuals",
   "They fit equally well, because both sets of residuals sum to zero",
   "It cannot be judged from residuals"], ans=0,
   why="Both sets sum to zero, so the sums cannot separate them; the magnitudes can, and Model A's prediction errors are consistently smaller."),

 dict(q="In the definition residual = observed y - predicted y, which value comes from the regression line?", choices=[
   "The predicted value, yhat",
   "The observed value, y",
   "Both values",
   "Neither value",
   "The residual itself"], ans=0,
   why="CED 5.4.A.1: the observed value is the data point actually recorded and the predicted value is read off the fitted line; their difference is the residual."),

 dict(q="A residual plot of residuals against x shows all points close to a horizontal band around zero except one point far above the band. How should that point be described?", choices=[
   "As an observation the model fits poorly, with a large positive residual meaning the model badly underpredicted it",
   "As an observation the model fits poorly, with a large positive residual meaning the model badly overpredicted it",
   "As evidence that the linear form is wrong for all the data",
   "As a point that should be deleted before the model is refitted",
   "As a point with a residual of zero"], ans=0,
   why="A large positive residual means the observed value sits far above the line, so the model underpredicted it; one stray point does not by itself condemn the form for the rest of the data, and deleting it is not justified merely because it is inconvenient."),

 dict(q="For a data set, the model is yhat = 3.0 + 1.5x. At x = 4 the observed value is 9.0, and at x = 8 the observed value is 15.0. What are the two residuals?", choices=[
   "0.0 and 0.0",
   "9.0 and 15.0",
   "-1.5 and 1.5",
   "1.5 and -1.5",
   "3.0 and 3.0"], ans=0,
   why="The predicted values are 3.0 + 1.5(4) = 9.0 and 3.0 + 1.5(8) = 15.0, so both observations fall exactly on the line and both residuals are 0."),

 dict(q="What is the correct way to decide whether a linear regression model is an appropriate form for a bivariate data set?", choices=[
   "Examine the residual plot for curvature or other patterns",
   "Check whether the correlation exceeds 0.9",
   "Check whether the sum of the residuals is close to zero",
   "Check whether the slope is positive",
   "Check whether all residuals have the same sign"], ans=0,
   why="CED 5.4.C.2 makes the residual plot the tool for investigating appropriateness; a high correlation does not establish linearity (CED 5.2.A.3), and the residual sum is zero for any least-squares fit."),

 dict(q="A model underpredicts an observation by 12 units. What is that observation's residual?", choices=[
   "12",
   "-12",
   "0",
   "It depends on the predicted value",
   "It depends on the slope"], ans=0,
   why="CED 5.4.B.1: underprediction means the observed value exceeds the predicted value, so the residual observed minus predicted is +12."),
]
