# CALC 2.7 Derivatives of cos x, sin x, e^x, and ln x — 25 questions
# Every derivative is confirmed with sp.diff in verify_c2_7.py, which also
# checks that no distractor is equivalent to the key.
# Questions 19 and 20 are conceptual (a diagnosed sign error and the domain on
# which d/dx[ln x] = 1/x holds).
TOPIC = ("2.7", "Derivatives of cos x, sin x, e^x, and ln x", 2)
QUESTIONS = [
 dict(q="d/dx[sin(x)] =", choices=[
   "cos(x)", "-cos(x)", "sin(x)", "-sin(x)"], ans=0,
   why="The derivative of sine is cosine, with no sign change."),
 dict(q="d/dx[cos(x)] =", choices=[
   "-sin(x)", "sin(x)", "cos(x)", "-cos(x)"], ans=0,
   why="The derivative of cosine carries a minus sign; this is the single most common sign error in the course."),
 dict(q="d/dx[e^x] =", choices=[
   "e^x", "x e^(x-1)", "e^(x-1)", "e^x/x"], ans=0,
   why="The natural exponential function is its own derivative; the power rule does not apply because the variable is the exponent."),
 dict(q="d/dx[ln(x)] =", choices=[
   "1/x", "ln(x)", "-1/x^2", "x ln(x) - x"], ans=0,
   why="The derivative of the natural logarithm is 1/x; the last choice is an antiderivative of ln(x)."),
 dict(q="If f(x) = 3 sin(x), then f'(x) =", choices=[
   "3 cos(x)", "3 sin(x)", "-3 cos(x)", "cos(x)"], ans=0,
   why="The constant 3 stays in front and sine differentiates to cosine."),
 dict(q="If f(x) = -2 cos(x), then f'(x) =", choices=[
   "2 sin(x)", "-2 sin(x)", "2 cos(x)", "-2 cos(x)"], ans=0,
   why="The derivative of cos(x) is -sin(x), and -2 times -sin(x) is +2 sin(x); the two minus signs cancel."),
 dict(q="If f(x) = sin(x) + cos(x), then f'(x) =", choices=[
   "cos(x) - sin(x)", "cos(x) + sin(x)", "sin(x) - cos(x)", "-sin(x) - cos(x)"], ans=0,
   why="Differentiate term by term: sine gives cosine and cosine gives -sine."),
 dict(q="If f(x) = 4e^x - 5 ln(x), then f'(x) =", choices=[
   "4e^x - 5/x", "4e^x - 5x", "4x e^(x-1) - 5/x", "4e^x + 5/x"], ans=0,
   why="e^x is unchanged, and -5 ln(x) differentiates to -5/x."),
 dict(q="If f(x) = 2 ln(x) + x^2, then f'(x) =", choices=[
   "2/x + 2x", "2/x + x^2", "2x + 2x", "2 ln(x) + 2x"], ans=0,
   why="2 ln(x) gives 2/x and x^2 gives 2x."),
 dict(q="If f(x) = sin(x), then f'(pi/2) =", choices=[
   "-1", "0", "1", "1/2"], ans=1,
   why="f'(x) = cos(x), and cos(pi/2) = 0; the value 1 is f(pi/2), not f'(pi/2)."),
 dict(q="If f(x) = cos(x), then f'(pi/3) =", choices=[
   "-sqrt(3)/2", "-1/2", "1/2", "sqrt(3)/2"], ans=0,
   why="f'(x) = -sin(x), so f'(pi/3) = -sin(pi/3) = -sqrt(3)/2; dropping the minus sign gives sqrt(3)/2."),
 dict(q="If f(x) = e^x, then f'(0) =", choices=[
   "0", "1", "e", "1/e"], ans=1,
   why="f'(x) = e^x, so f'(0) = e^0 = 1."),
 dict(q="If f(x) = ln(x), then f'(2) =", choices=[
   "1/2", "2", "ln(2)", "-1/4"], ans=0,
   why="f'(x) = 1/x, so f'(2) = 1/2; ln(2) is f(2), not f'(2)."),
 dict(q="If f(x) = e^x + ln(x), then f'(1) =", choices=[
   "e + 1", "e", "1", "e - 1"], ans=0,
   why="f'(x) = e^x + 1/x, so f'(1) = e + 1."),
 dict(q="The slope of the line tangent to y = sin(x) at x = 0 is", choices=[
   "-1", "0", "1", "pi"], ans=2,
   why="dy/dx = cos(x), and cos(0) = 1."),
 dict(q="An equation of the line tangent to y = e^x at the point (0, 1) is", choices=[
   "y = x + 1", "y = x", "y = ex", "y = x - 1"], ans=0,
   why="The slope is e^0 = 1 and the line passes through (0, 1), so y = x + 1."),
 dict(q="An equation of the line tangent to y = ln(x) at the point (1, 0) is", choices=[
   "y = x - 1", "y = x + 1", "y = x", "y = 1/x"], ans=0,
   why="The slope is 1/1 = 1 and the line passes through (1, 0), so y = x - 1."),
 dict(q="On the interval 0 <= x < 2pi, the graph of y = sin(x) has a horizontal tangent line at", choices=[
   "x = pi/2 and x = 3pi/2",
   "x = 0 and x = pi",
   "x = pi only",
   "no value of x"], ans=0,
   why="dy/dx = cos(x) is zero exactly at pi/2 and 3pi/2 on that interval; x = 0 and x = pi are where sin(x) itself is zero."),
 dict(q="A student writes d/dx[cos(x)] = sin(x). What is the error?", choices=[
   "The derivative of cos(x) is -sin(x); the minus sign was dropped",
   "The derivative of cos(x) is cos(x)",
   "The derivative of cos(x) is -cos(x)",
   "There is no error"], ans=0,
   why="Cosine is decreasing on (0, pi), where sin(x) is positive, so the derivative must be negative there."),
 dict(q="The formula d/dx[ln(x)] = 1/x holds for", choices=[
   "x > 0, the domain of ln(x)",
   "every real number x",
   "x > 1 only",
   "every x except x = 1"], ans=0,
   why="ln(x) is defined only for positive x, so the derivative formula is stated on that same domain."),
 dict(q="If f(x) = e, then f'(x) =", choices=[
   "0", "e", "e^x", "1"], ans=0,
   why="e is a constant, roughly 2.718, not the function e^x, so its derivative is 0."),
 dict(q="If f(x) = sin(x)/2 - 3e^x + 7, then f'(x) =", choices=[
   "cos(x)/2 - 3e^x",
   "cos(x)/2 - 3e^x + 7",
   "-sin(x)/2 - 3e^x",
   "cos(x)/2 - 3x e^(x-1)"], ans=0,
   why="Each term differentiates separately and the constant 7 contributes 0."),
 dict(q="On the interval 0 <= x < 2pi, the line tangent to y = cos(x) has slope 1 at", choices=[
   "x = 0", "x = pi/2", "x = 3pi/2", "x = pi"], ans=2,
   why="dy/dx = -sin(x), and -sin(x) = 1 requires sin(x) = -1, which happens at x = 3pi/2."),
 dict(q="For constants a and b, f(x) = a sin(x) + b cos(x) satisfies f'(0) = 3 and f'(pi/2) = -2. Then", choices=[
   "a = 3, b = 2",
   "a = 3, b = -2",
   "a = -2, b = 3",
   "a = 2, b = 3"], ans=0,
   why="f'(x) = a cos(x) - b sin(x), so f'(0) = a = 3 and f'(pi/2) = -b = -2, giving b = 2."),
 dict(q="The limit lim as h -> 0 of (sin(pi/6 + h) - sin(pi/6))/h is equal to", choices=[
   "-1/2", "1/2", "sqrt(2)/2", "sqrt(3)/2"], ans=3,
   why="This is the derivative of sin(x) at pi/6, which is cos(pi/6) = sqrt(3)/2; 1/2 is sin(pi/6)."),
]
