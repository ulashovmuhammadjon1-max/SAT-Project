# AP STATISTICS 5.5 Least-Squares Regression - 25 questions
# CED: AP Statistics Course and Exam Description, Effective Fall 2026, Unit 5.
# Objectives 5.5.A (the LSRL minimizes the sum of the SQUARED residuals, passes
# through (xbar, ybar), and its slope, intercept, r and r^2 come from
# technology; r^2 is the proportion of the variation in the response explained
# by the linear relationship with the explanatory variable) and 5.5.B (interpret
# the slope as the predicted change in the response per one-unit increase in
# the explanatory variable, and the intercept as the predicted response at
# x = 0, both in context -- noting that the intercept is sometimes not
# interpretable because x = 0 is an extrapolation or because the predicted value
# is impossible).
# Two items read a coefficients table from computer regression output. They ask
# only for a and b: the Fall 2026 framework contains NO inference for a slope,
# so there is deliberately no question here about a standard error of b, a t
# statistic or df = n - 2.
# Every coefficient, prediction and r^2 is recomputed in verify_s5_5.py with
# scipy.stats.linregress and numpy.
TOPIC = ("5.5", "Least-Squares Regression", 5)
QUESTIONS = [

 dict(q="The least-squares regression line is chosen to minimize which quantity?", choices=[
   "The sum of the squared residuals",
   "The sum of the residuals",
   "The largest absolute residual",
   "The sum of the vertical distances from the points to the line",
   "The correlation coefficient"], ans=0,
   why="CED 5.5.A.1: the model is fitted by minimizing the sum of the squares of the residuals, which is where the name least-squares comes from; the plain sum of the residuals is zero for any such line."),

 dict(q="Through which point does every least-squares regression line pass?", choices=[
   "The point of averages, (xbar, ybar)",
   "The origin, (0, 0)",
   "The point with the largest x-value",
   "The point with the smallest residual",
   "The point (a, b) formed by the intercept and the slope"], ans=0,
   why="CED 5.5.A.1: the least-squares line always passes through the point whose coordinates are the two sample means."),

 dict(q="A least-squares regression of y on x gives a slope of 2.4, and the sample means are xbar = 15 and ybar = 68. What is the y-intercept?", choices=[
   "32.0",
   "36.0",
   "53.0",
   "68.0",
   "104.0"], ans=0,
   why="Because the line passes through (15, 68), the intercept is a = ybar - b xbar = 68 - 2.4(15) = 68 - 36 = 32.0."),

 dict(q="A regression predicting monthly electricity cost in dollars from the number of air conditioners in a home gives yhat = 41.5 + 18.7x. What is the correct interpretation of the slope?", choices=[
   "For each additional air conditioner, the predicted monthly cost increases by 18.7 dollars",
   "For each additional dollar of monthly cost, the predicted number of air conditioners increases by 18.7",
   "A home with no air conditioners has a monthly cost of 18.7 dollars",
   "The average monthly cost of all homes is 18.7 dollars",
   "Each additional air conditioner causes the monthly cost to rise by 18.7 dollars"], ans=0,
   why="CED 5.5.B.2: the slope is the PREDICTED change in the response per one-unit increase in the explanatory variable, stated in context; observational regression supports no causal claim."),

 dict(q="For that same model, yhat = 41.5 + 18.7x, what is the correct interpretation of the y-intercept?", choices=[
   "A home with no air conditioners has a predicted monthly cost of 41.5 dollars",
   "A home with no air conditioners has an actual monthly cost of exactly 41.5 dollars",
   "For each additional air conditioner, the predicted cost rises by 41.5 dollars",
   "The average number of air conditioners is 41.5",
   "The predicted cost is 41.5 dollars for every home"], ans=0,
   why="CED 5.5.B.3: the intercept is the PREDICTED value of the response when x = 0, in context; it does not promise an exact value for any particular home."),

 dict(q="A regression predicting a runner's finishing time in minutes from training distance in kilometers per week gives yhat = 214 - 1.8x. What is the correct interpretation of the slope?", choices=[
   "For each additional kilometer per week of training, the predicted finishing time decreases by 1.8 minutes",
   "For each additional kilometer per week of training, the predicted finishing time increases by 1.8 minutes",
   "For each additional minute of finishing time, training decreases by 1.8 kilometers per week",
   "A runner who does not train has a predicted time of 1.8 minutes",
   "Training an extra kilometer per week causes a runner to finish 1.8 minutes sooner"], ans=0,
   why="A negative slope means the predicted response falls as x rises, so the interpretation must say 'decreases'; the sign is the entire content of the direction, and the data being observational rules out the causal wording."),

 dict(q="A regression predicting the weight of a fish in grams from its length in centimeters gives yhat = -180 + 42x, fitted from fish between 20 and 45 cm. Why is the intercept not interpretable here?", choices=[
   "A length of 0 cm is far outside the range of lengths used, and a predicted weight of -180 grams is impossible",
   "The slope is positive, so the intercept has no meaning",
   "The intercept is negative, and negative numbers can never appear in a regression model",
   "The intercept can only be interpreted when the correlation is above 0.9",
   "The intercept is interpretable; a fish of length 0 weighs -180 grams"], ans=0,
   why="CED 5.5.B.3 names both reasons an intercept can fail to be meaningful: x = 0 may be an extrapolation, and the predicted value may be impossible for the response variable."),

 dict(q="Seven observations (4, 31), (7, 38), (9, 43), (12, 50), (15, 58), (18, 64), (20, 69) are fitted with a least-squares line. Technology reports the slope as 2.381. What is the y-intercept?", choices=[
   "2.38",
   "12.14",
   "21.51",
   "28.91",
   "50.43"], ans=2,
   why="The means are xbar = 12.143 and ybar = 50.429, so a = 50.429 - 2.381(12.143) = 21.51; 50.43 is the mean of y and 12.14 the mean of x."),

 dict(q="For those same seven observations, technology reports r = 0.9997. What is the coefficient of determination, and what does it mean?", choices=[
   "0.9993; about 99.93 percent of the variation in the response is explained by the linear relationship with the explanatory variable",
   "0.9997; about 99.97 percent of the variation is explained",
   "0.9993; about 99.93 percent of the points lie on the regression line",
   "0.9993; the response increases 99.93 percent as fast as the explanatory variable",
   "0.9998; about 99.98 percent of the variation is explained"], ans=0,
   why="CED 5.5.A.5: r^2 = 0.9997^2 = 0.9993 is the proportion of variation in the response explained by the linear relationship; it is not a count of points on the line."),

 dict(q="A least-squares regression reports r = 0.88. What proportion of the variation in the response variable is explained by the linear relationship with the explanatory variable?", choices=[
   "0.1200",
   "0.2256",
   "0.7744",
   "0.8800",
   "0.9381"], ans=2,
   why="The coefficient of determination is r^2 = 0.88^2 = 0.7744; 0.9381 is the square root of r, and 0.2256 is the unexplained proportion."),

 dict(q="Computer output for a least-squares regression is shown. What is the fitted regression equation?", table=dict(headers=["Predictor", "Coef"], rows=[["Constant", "12.85"], ["Hours", "3.42"]]),
   choices=[
   "yhat = 12.85 + 3.42x",
   "yhat = 3.42 + 12.85x",
   "yhat = 12.85 - 3.42x",
   "yhat = 3.42x",
   "yhat = 16.27x"], ans=0,
   why="The Constant row gives the y-intercept and the row named for the explanatory variable gives its slope, so the equation is yhat = 12.85 + 3.42x."),

 dict(q="For the regression output in the previous question, with 'Hours' as the explanatory variable and predicted score as the response, what is the predicted score for 6 hours?", choices=[
   "3.42",
   "12.85",
   "20.52",
   "33.37",
   "98.02"], ans=3,
   why="12.85 + 3.42(6) = 12.85 + 20.52 = 33.37; 20.52 leaves out the intercept."),

 dict(q="Computer output for a least-squares regression of fuel use on outdoor temperature is shown. What is the correct interpretation of the coefficient in the Temperature row?", table=dict(headers=["Predictor", "Coef"], rows=[["Constant", "186.4"], ["Temperature", "-2.75"]]),
   choices=[
   "For each additional degree of outdoor temperature, predicted fuel use decreases by 2.75 units",
   "For each additional unit of fuel use, predicted temperature decreases by 2.75 degrees",
   "At a temperature of 0 degrees, predicted fuel use is 2.75 units",
   "Predicted fuel use is 2.75 units for every temperature",
   "Each additional degree causes fuel use to fall by 2.75 units"], ans=0,
   why="The coefficient on the explanatory variable is the slope: a predicted decrease of 2.75 units of fuel per additional degree; the Constant row would be needed for a statement about temperature 0, and observational data supports no causal wording."),

 dict(q="Using the relationship b = r(s_y/s_x), a regression has r = -0.6, s_y = 8 and s_x = 5. What is the slope of the least-squares line?", choices=[
   "-3.75",
   "-0.96",
   "-0.6",
   "-0.375",
   "0.96"], ans=1,
   why="b = -0.6(8/5) = -0.6(1.6) = -0.96; the sign of the slope always matches the sign of the correlation, and -0.375 inverts the ratio of standard deviations."),

 dict(q="Two variables have r = 0.75. Which statement about the least-squares line is correct?", choices=[
   "Its slope is positive, and about 56 percent of the variation in the response is explained by the linear relationship",
   "Its slope is 0.75",
   "Its slope is positive, and about 75 percent of the variation in the response is explained",
   "Its slope is negative, because r^2 is smaller than r",
   "Its slope cannot be determined even in sign"], ans=0,
   why="The slope shares the sign of r, so it is positive, and r^2 = 0.5625 gives about 56 percent explained; the slope equals r only when the two standard deviations happen to be equal."),

 dict(q="Which of the following changes would NOT change the value of the least-squares slope?", choices=[
   "Reporting the fitted equation to more decimal places",
   "Adding a new observation far from the pattern",
   "Measuring the response variable in different units",
   "Swapping which variable is explanatory and which is response",
   "Removing an observation with a large residual"], ans=0,
   why="Rounding the reported value changes nothing about the fit; every other listed change alters either the data or the roles of the variables and so alters the slope."),

 dict(q="A regression predicting exam score from hours studied gives yhat = 25.6 + 2.15x, fitted from students who studied between 1 and 20 hours. What is the predicted score for a student who studied 14 hours, and is that an interpolation?", choices=[
   "55.70, and yes it is an interpolation",
   "55.70, and no it is an extrapolation",
   "30.10, and yes it is an interpolation",
   "27.75, and yes it is an interpolation",
   "55.70, and it cannot be classified"], ans=0,
   why="25.6 + 2.15(14) = 25.6 + 30.1 = 55.70, and 14 lies between 1 and 20, so the prediction is an interpolation."),

 dict(q="Why is a slope interpretation always phrased in terms of a PREDICTED change rather than an actual change?", choices=[
   "The line summarizes an average relationship, and individual observations scatter around it",
   "Because the slope is computed with technology rather than by hand",
   "Because the slope is always smaller than the true change",
   "Because slopes have no units",
   "Because the slope is a population parameter"], ans=0,
   why="The fitted line gives predicted responses, and CED 5.5.B.2 states the interpretation in those terms; individual cases differ from the prediction by their residuals."),

 dict(q="A regression of a city's daily bus ridership on the day's rainfall in millimeters gives yhat = 8,200 + 46x. A reporter writes that adding one millimeter of rain adds 46 riders. What is the flaw?", choices=[
   "The data are observational, so the model supports a predicted association, not a causal effect",
   "The slope should be interpreted per rider rather than per millimeter",
   "The intercept should have been used instead of the slope",
   "The slope is too large to be interpreted",
   "There is no flaw"], ans=0,
   why="Regression from observational data describes how the predicted response varies with the explanatory variable; ruling out lurking variables would require an experiment, so the causal wording is not supported."),

 dict(q="A regression reports r^2 = 0.36. What can be said about the correlation?", choices=[
   "Its magnitude is 0.6, and its sign matches the sign of the slope",
   "It equals 0.36",
   "It equals 0.1296",
   "Its magnitude is 0.6, and it must be positive",
   "It cannot be recovered from r^2 at all"], ans=0,
   why="Taking the square root of 0.36 gives 0.6 in magnitude, and only the direction of the association, visible in the sign of the slope, decides the sign."),

 dict(q="A least-squares regression of height on age is refitted after the age variable is converted from years to months. What happens to r and to the slope?", choices=[
   "r is unchanged; the slope is divided by 12",
   "Both r and the slope are unchanged",
   "r is divided by 12; the slope is unchanged",
   "Both r and the slope are divided by 12",
   "r is unchanged; the slope is multiplied by 12"], ans=0,
   why="A correlation is unit-free, but a slope carries units of response per explanatory: predicted growth per month is one twelfth of predicted growth per year."),

 dict(q="A regression predicting a car's fuel economy in miles per gallon from its weight in thousands of pounds gives yhat = 48.2 - 6.4x. What does the model predict for a car weighing 3,500 pounds?", choices=[
   "-22,351.80",
   "22.40",
   "25.80",
   "41.80",
   "48.20"], ans=2,
   why="A weight of 3,500 pounds is x = 3.5 in thousands, so the prediction is 48.2 - 6.4(3.5) = 48.2 - 22.4 = 25.80; forgetting to convert the units gives a nonsensical answer."),

 dict(q="Which statement about r^2 is correct?", choices=[
   "It is between 0 and 1 and carries no information about the direction of the association",
   "It is between -1 and 1 and carries the direction of the association",
   "It equals the slope of the least-squares line",
   "It is the proportion of the data points lying on the regression line",
   "It is larger than the absolute value of r whenever the fit is good"], ans=0,
   why="Squaring removes the sign and maps every correlation into [0, 1]; for any |r| < 1 the square is SMALLER than |r|, and r^2 counts explained variation rather than points."),

 dict(q="Two least-squares lines are fitted to the same response variable using two different explanatory variables. The first gives r^2 = 0.81 and the second r^2 = 0.49. What does this comparison say?", choices=[
   "The first explanatory variable accounts for more of the variation in the response",
   "The first explanatory variable has a larger slope",
   "The first model has smaller residuals for every single observation",
   "The second explanatory variable has a negative correlation with the response",
   "Nothing, because r^2 cannot be compared across models"], ans=0,
   why="CED 5.5.A.5 makes r^2 a proportion of variation explained, so 0.81 against 0.49 is a statement about explained variation; it says nothing about the slopes, the sign of the second correlation, or any individual residual."),

 dict(q="A least-squares line is fitted, and then one observation with a very large residual is removed and the line refitted. What is most likely to happen?", choices=[
   "Both the slope and the intercept change, and r^2 typically increases",
   "The slope and intercept are unchanged, because least squares is resistant",
   "r^2 must decrease, because there are fewer points",
   "The line must pass through the same point of averages as before",
   "Nothing changes unless the removed point was the largest x-value"], ans=0,
   why="Least squares minimizes squared residuals, so a point with a large residual pulls the line strongly; removing it moves the fit and generally raises the proportion of variation explained, and the point of averages itself shifts because the means change."),
]
