# AP STATISTICS 5.3 Linear Regression Models - 25 questions
# CED: AP Statistics Course and Exam Description, Effective Fall 2026, Unit 5.
# Objective 5.3.A: the predicted response is yhat = a + bx, where a is the
# y-intercept and b the slope (5.3.A.2); EXTRAPOLATION is prediction at an x
# beyond the interval of x-values used to fit the line and is less reliable the
# further it goes (5.3.A.3); INTERPOLATION is prediction at an x inside that
# interval (5.3.A.4).
# Note what this topic does NOT contain in the Fall 2026 framework: there is no
# inference for a slope anywhere in the course, so nothing here asks for a
# standard error of b, a t statistic or a p-value. Predicted values and the
# interpolation/extrapolation judgement are the whole of it.
# Every predicted value is recomputed in verify_s5_3.py, and every fitted line
# quoted from data is refitted with scipy.stats.linregress.
TOPIC = ("5.3", "Linear Regression Models", 5)
QUESTIONS = [

 dict(q="A least-squares regression model is yhat = 12.4 + 3.7x. What is the predicted response when x = 8?", choices=[
   "16.1",
   "29.6",
   "42.0",
   "99.2",
   "128.8"], ans=2,
   why="Substituting gives 12.4 + 3.7(8) = 12.4 + 29.6 = 42.0; 29.6 leaves out the intercept and 16.1 adds the coefficients instead of multiplying."),

 dict(q="A least-squares regression model is yhat = 85.2 - 1.6x. What is the predicted response when x = 15?", choices=[
   "24.0",
   "61.2",
   "83.6",
   "86.8",
   "109.2"], ans=1,
   why="85.2 - 1.6(15) = 85.2 - 24.0 = 61.2; 83.6 subtracts only 1.6, and 109.2 adds rather than subtracts."),

 dict(q="A least-squares regression model is yhat = -2.5 + 0.45x. What is the predicted response when x = 20?", choices=[
   "-2.05",
   "1.75",
   "6.50",
   "9.00",
   "11.50"], ans=2,
   why="-2.5 + 0.45(20) = -2.5 + 9.0 = 6.5; 9.00 forgets the intercept."),

 dict(q="A regression line was fitted using values of x ranging from 5 to 30. A prediction is made at x = 45. What is this an example of, and what is the concern?", choices=[
   "Extrapolation; the linear pattern is not known to continue beyond x = 30, so the prediction is less reliable",
   "Interpolation; the prediction is reliable because it uses the fitted line",
   "Extrapolation; the prediction is more reliable because it is far from the data",
   "Interpolation; the prediction is unreliable because 45 is a large number",
   "Neither, because a regression line can be used at any x"], ans=0,
   why="CED 5.3.A.3: predicting outside the interval of x-values used to fit the line is extrapolation, and the further out the prediction goes the less reliable it is."),

 dict(q="An analyst fits a line to observations whose explanatory values run from 5 to 30, then predicts the response at x = 18. What is this an example of?", choices=[
   "Interpolation, because 18 lies inside the interval of x-values used to fit the line",
   "Extrapolation, because 18 was not one of the observed x-values",
   "Extrapolation, because the fit used values as large as 30",
   "Neither, because 18 is not the mean of the x-values",
   "Interpolation, but only if 18 was one of the observed x-values"], ans=0,
   why="CED 5.3.A.4: interpolation is prediction at an x inside the interval used to determine the line, whether or not that exact value was observed."),

 dict(q="Six observations (3, 21), (5, 26), (8, 34), (10, 39), (12, 44), (15, 51) give the least-squares line yhat = 13.594 + 2.518x. What is the predicted response at x = 9?", choices=[
   "22.66",
   "31.24",
   "36.25",
   "39.00",
   "45.35"], ans=2,
   why="13.594 + 2.518(9) = 13.594 + 22.662 = 36.25, an interpolation because 9 lies between the smallest x of 3 and the largest of 15."),

 dict(q="For the same six observations, the mean of the x-values is 8.833 and the mean of the y-values is 35.833. What does the least-squares line predict at x = 8.833?", choices=[
   "35.83",
   "13.59",
   "22.24",
   "44.67",
   "It cannot be determined without more information"], ans=0,
   why="CED 5.5.A.1: the least-squares line always passes through the point of averages, so the prediction at the mean of x is exactly the mean of y."),

 dict(q="A model is yhat = 12.4 + 3.7x. If x increases by 5 units, by how much does the predicted response change?", choices=[
   "3.7",
   "5.0",
   "18.5",
   "30.9",
   "62.0"], ans=2,
   why="The predicted change is the slope times the change in x, 3.7 x 5 = 18.5; the intercept does not enter a change calculation."),

 dict(q="A model is yhat = 85.2 - 1.6x. If x increases by 10 units, by how much does the predicted response change?", choices=[
   "-160.0",
   "-16.0",
   "-1.6",
   "16.0",
   "69.2"], ans=1,
   why="The predicted change is -1.6 x 10 = -16.0, a decrease; the sign of the slope carries the direction."),

 dict(q="A model is yhat = 12.4 + 3.7x. For what value of x does the model predict a response of 100?", choices=[
   "23.68",
   "27.03",
   "30.38",
   "270.40",
   "382.40"], ans=0,
   why="Solving 100 = 12.4 + 3.7x gives x = 87.6/3.7 = 23.68; 27.03 divides 100 by 3.7 without removing the intercept first."),

 dict(q="A regression model predicting a child's height in centimeters from age in years is yhat = 76.5 + 6.2x, fitted from children aged 2 to 12. Why is the intercept of 76.5 interpretable here while a prediction at age 40 would not be?", choices=[
   "Age 0 is only two years below the data's range, while age 40 lies far outside it, so the second is a severe extrapolation",
   "The intercept is always interpretable and any prediction is always valid",
   "Because 76.5 is a positive number and the prediction at age 40 would be negative",
   "Because the slope is positive",
   "Because age 0 is inside the interval from 2 to 12"], ans=0,
   why="CED 5.3.A.3: reliability falls off with distance beyond the data, so a small step past the edge is far less troubling than predicting height at an age 28 years beyond the oldest child measured; age 0 is still outside the range and the intercept must be read with care."),

 dict(q="A model is yhat = 48.6 + 2.15x. What is the predicted response at x = 7?", choices=[
   "50.75",
   "55.65",
   "63.65",
   "65.80",
   "355.25"], ans=2,
   why="48.6 + 2.15(7) = 48.6 + 15.05 = 63.65."),

 dict(q="In the model yhat = a + bx, what does a represent?", choices=[
   "The predicted value of the response variable when the explanatory variable equals 0",
   "The predicted change in the response variable for a one-unit increase in the explanatory variable",
   "The correlation between the two variables",
   "The mean of the response variable",
   "The value of the response variable at the largest observed x"], ans=0,
   why="CED 5.3.A.2 and 5.5.B.3: a is the y-intercept, the predicted response at x = 0; the predicted change per unit of x is the slope b."),

 dict(q="A model is yhat = 3.2 + 0.85x. What is the predicted response at x = 12, and is that prediction an interpolation if the data used x-values from 1 to 20?", choices=[
   "13.40, and it is an interpolation",
   "13.40, and it is an extrapolation",
   "10.20, and it is an interpolation",
   "4.05, and it is an interpolation",
   "13.40, and it cannot be classified"], ans=0,
   why="3.2 + 0.85(12) = 13.40, and 12 lies between 1 and 20, so the prediction is an interpolation."),

 dict(q="Which of these predictions from a line fitted with x-values between 100 and 400 is the LEAST reliable?", choices=[
   "The prediction at x = 105",
   "The prediction at x = 250",
   "The prediction at x = 380",
   "The prediction at x = 410",
   "The prediction at x = 900"], ans=4,
   why="CED 5.3.A.3: extrapolation grows less reliable with distance from the data, and 900 is 500 units beyond the largest x used, while 410 is only 10 beyond and the others are inside."),

 dict(q="A regression model of monthly heating cost on average outdoor temperature is yhat = 210 - 3.4x, where x is temperature in degrees Fahrenheit. What does the model predict for a month averaging 35 degrees?", choices=[
   "91.0",
   "119.0",
   "206.6",
   "213.4",
   "329.0"], ans=0,
   why="210 - 3.4(35) = 210 - 119 = 91.0 dollars; 119.0 is the amount subtracted rather than the prediction."),

 dict(q="Why can a regression model give a nonsensical prediction, such as a negative weight, even when it fits the data well?", choices=[
   "Because the line continues indefinitely in both directions, but the relationship it describes need not hold outside the observed range of x",
   "Because least-squares regression always underestimates at small x",
   "Because the correlation must be negative",
   "Because the model uses the mean of y rather than individual values",
   "Because negative predictions mean the data were entered incorrectly"], ans=0,
   why="A fitted line is a summary of the observed range; extending it outside that range assumes a pattern the data never demonstrated, which is exactly what CED 5.3.A.3 warns about."),

 dict(q="Two students use the model yhat = 5.0 + 1.25x. One predicts at x = 4 and the other at x = 16. What is the difference between the two predicted values?", choices=[
   "1.25",
   "12.0",
   "15.0",
   "20.0",
   "25.0"], ans=2,
   why="The predicted values are 10.0 and 25.0, a difference of 15.0, which is also the slope times the change in x, 1.25 x 12."),

 dict(q="A regression model is used to predict a response at an x-value equal to the largest x in the data set. Is this interpolation or extrapolation?", choices=[
   "Interpolation, because that x-value lies within the interval of x-values used to fit the line",
   "Extrapolation, because that x-value is at the edge of the data",
   "Extrapolation, because the line continues beyond it",
   "Neither, because predictions can only be made at the mean of x",
   "It cannot be determined without the slope"], ans=0,
   why="CED 5.3.A.4: the interval of x-values used to fit the line includes its endpoints, so a prediction there is an interpolation, though it is the least secure interpolation available."),

 dict(q="A regression model of a company's sales (in thousands) on years since founding is yhat = 40 + 12x, fitted using years 1 through 10. The company asks for a prediction for year 30. What is the best response?", choices=[
   "The model predicts 400 thousand, but year 30 is far outside the fitted range, so the prediction should not be trusted",
   "The model predicts 400 thousand, and the prediction is reliable because the model fit well",
   "The model predicts 360 thousand, and the prediction is reliable",
   "The model cannot produce a number for year 30",
   "The model predicts 400 thousand, which is reliable because the slope is positive"], ans=0,
   why="Substituting gives 40 + 12(30) = 400, but year 30 is 20 years beyond the last year used, so the numerical answer must be reported with the extrapolation warning."),

 dict(q="A model predicting exam score from hours studied is yhat = 52 + 4.5x. A student who studied 6 hours scored 85. What did the model predict for that student?", choices=[
   "6.0",
   "27.0",
   "56.5",
   "79.0",
   "85.0"], ans=3,
   why="52 + 4.5(6) = 52 + 27 = 79.0, which is the predicted value; the observed 85 is the actual score, and the difference between them is the residual."),

 dict(q="Which statement about a linear regression model is correct?", choices=[
   "It should be fitted only when the data show a linear trend",
   "It can be fitted to any bivariate data set with equally good results",
   "It gives exact rather than predicted values of the response variable",
   "It requires that the explanatory variable be categorical",
   "It requires the two variables to have the same units"], ans=0,
   why="CED 5.4.C.3 states that a linear model should only be fit when the data exhibit a linear trend; a fitted line yields predicted values, not exact ones, and both variables must be quantitative."),

 dict(q="A model is yhat = 100 - 2.5x. At which of these x-values does the model predict a response of 0?", choices=[
   "25",
   "40",
   "50",
   "97.5",
   "250"], ans=1,
   why="Solving 0 = 100 - 2.5x gives x = 40; whether that prediction is meaningful depends on whether 40 lies within the range of x used to fit the line."),

 dict(q="A regression model is yhat = 18.0 + 0.75x, and a prediction is wanted at x = 24. What is the predicted value, and what is the predicted value at x = 25?", choices=[
   "36.00 and 36.75",
   "36.00 and 37.50",
   "18.75 and 19.50",
   "42.00 and 43.00",
   "36.75 and 37.50"], ans=0,
   why="18.0 + 0.75(24) = 36.00 and 18.0 + 0.75(25) = 36.75; the two differ by exactly the slope, because x increased by one unit."),

 dict(q="Data on x-values from 20 to 60 give the model yhat = 8.5 + 1.4x. Which prediction is an extrapolation?", choices=[
   "The prediction at x = 21",
   "The prediction at x = 40",
   "The prediction at x = 55",
   "The prediction at x = 60",
   "The prediction at x = 65"], ans=4,
   why="CED 5.3.A.3: only x = 65 lies outside the interval from 20 to 60; the endpoint 60 and every value between them are interpolations."),
]
