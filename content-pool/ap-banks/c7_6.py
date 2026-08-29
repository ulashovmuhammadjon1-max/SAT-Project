# CALC 7.6 Finding General Solutions Using Separation of Variables — 25 questions
# Every general solution is substituted back into its differential equation by
# sympy; see verify_c7_6.py.
TOPIC = ("7.6", "Finding General Solutions Using Separation of Variables", 7)
QUESTIONS = [
 dict(q="What is the general solution of dy/dx = xy?", choices=[
   "y = C*e^(x^2/2)",
   "y = C*e^(x^2)",
   "y = x^2/2 + C",
   "y = C*e^x"], ans=0,
   why="Separating gives dy/y = x dx, so ln|y| = x^2/2 + C and y = C*e^(x^2/2)."),
 dict(q="For x > 0, what is the general solution of dy/dx = y/x?", choices=[
   "y = Cx",
   "y = C*e^x",
   "y = x + C",
   "y = C*ln(x)"], ans=0,
   why="Separating gives dy/y = dx/x, so ln|y| = ln|x| + C and y = Cx."),
 dict(q="What is the general solution of dy/dx = 2xy^2?", choices=[
   "y = -1/(x^2 + C)",
   "y = 1/(x^2 + C)",
   "y = C*e^(x^2)",
   "y = x^2*y^3/3 + C"], ans=0,
   why="Separating gives y^(-2) dy = 2x dx, so -1/y = x^2 + C and y = -1/(x^2 + C)."),
 dict(q="What is the general solution of dy/dx = x/y, written implicitly?", choices=[
   "y^2 = x^2 + C",
   "y^2 = x^2/2 + C",
   "y = x^2/2 + C",
   "y^2 - x^2 = 0"], ans=0,
   why="Separating gives y dy = x dx, so y^2/2 = x^2/2 + C and y^2 = x^2 + C."),
 dict(q="What is the general solution of dy/dx = 3y?", choices=[
   "y = C*e^(3x)",
   "y = C*e^(x/3)",
   "y = 3e^x + C",
   "y = 3x + C"], ans=0,
   why="Separating gives dy/y = 3 dx, so ln|y| = 3x + C and y = C*e^(3x)."),
 dict(q="What is the general solution of dy/dx = -2xy?", choices=[
   "y = C*e^(-x^2)",
   "y = C*e^(-2x)",
   "y = C*e^(x^2)",
   "y = -x^2 + C"], ans=0,
   why="Separating gives dy/y = -2x dx, so ln|y| = -x^2 + C and y = C*e^(-x^2)."),
 dict(q="What is the general solution of dy/dx = (x + 1)/y, written implicitly?", choices=[
   "y^2 = x^2 + 2x + C",
   "y^2 = x^2 + x + C",
   "y = x^2/2 + x + C",
   "y^2/2 = x + 1 + C"], ans=0,
   why="Separating gives y dy = (x + 1) dx, so y^2/2 = x^2/2 + x + C and doubling gives y^2 = x^2 + 2x + C."),
 dict(q="What is the general solution of dy/dx = e^x/y, written implicitly?", choices=[
   "y^2 = 2e^x + C",
   "y^2 = e^x + C",
   "y = e^x + C",
   "y^2 = e^(2x) + C"], ans=0,
   why="Separating gives y dy = e^x dx, so y^2/2 = e^x + C and y^2 = 2e^x + C."),
 dict(q="What is the general solution of dy/dx = y*cos(x)?", choices=[
   "y = C*e^(sin(x))",
   "y = C*e^(cos(x))",
   "y = C*sin(x)",
   "y = sin(x) + C"], ans=0,
   why="Separating gives dy/y = cos(x) dx, so ln|y| = sin(x) + C and y = C*e^(sin(x))."),
 dict(q="What is the general solution of dy/dx = sin(x)/y, written implicitly?", choices=[
   "y^2 = -2cos(x) + C",
   "y^2 = 2cos(x) + C",
   "y = -cos(x) + C",
   "y^2 = -cos(x) + C"], ans=0,
   why="Separating gives y dy = sin(x) dx, so y^2/2 = -cos(x) + C and y^2 = -2cos(x) + C."),
 dict(q="What is the general solution of dy/dx = 4x^3*y?", choices=[
   "y = C*e^(x^4)",
   "y = C*e^(4x^4)",
   "y = C*e^(x^3)",
   "y = x^4 + C"], ans=0,
   why="Separating gives dy/y = 4x^3 dx, so ln|y| = x^4 + C and y = C*e^(x^4)."),
 dict(q="For x > 0 and y > -1, what is the general solution of dy/dx = (1 + y)/x?", choices=[
   "y = Cx - 1",
   "y = Cx + 1",
   "y = C*e^x - 1",
   "y = ln(x) + C"], ans=0,
   why="Separating gives dy/(1 + y) = dx/x, so ln(1 + y) = ln(x) + C, 1 + y = Cx, and y = Cx - 1."),
 dict(q="What is the general solution of dy/dx = x(y + 1)?", choices=[
   "y = C*e^(x^2/2) - 1",
   "y = C*e^(x^2/2) + 1",
   "y = C*e^(x^2/2 + x)",
   "y = x^2/2 + x + C"], ans=0,
   why="Separating gives dy/(y + 1) = x dx, so ln|y + 1| = x^2/2 + C and y = C*e^(x^2/2) - 1."),
 dict(q="For y > 0, what is the general solution of dy/dx = 2*sqrt(y)?", choices=[
   "y = (x + C)^2",
   "y = (2x + C)^2",
   "y = 4(x + C)^2",
   "y = sqrt(x) + C"], ans=0,
   why="Separating gives y^(-1/2) dy = 2 dx, so 2*sqrt(y) = 2x + C and y = (x + C)^2."),
 dict(q="Which of the following is the correct first step in separating dy/dx = x^2*y^3?", choices=[
   "y^(-3) dy = x^2 dx",
   "y^3 dy = x^2 dx",
   "y^(-3) dy = x^(-2) dx",
   "dy = x^2*y^3 dx, which cannot be separated"], ans=0,
   why="All the y factors must be divided over to the dy side, which sends y^3 into the denominator."),
 dict(q="Which of the following differential equations is NOT separable?", choices=[
   "dy/dx = x + y",
   "dy/dx = xy",
   "dy/dx = x/y",
   "dy/dx = x^2*y^3"], ans=0,
   why="A sum of x and y cannot be written as a product of a function of x and a function of y."),
 dict(q="When both sides of a separated equation are integrated, why is only one constant of integration written?", choices=[
   "the two constants can be combined into a single arbitrary constant on one side",
   "the left integral never produces a constant",
   "the constants always cancel exactly",
   "a separated equation needs no constant at all"], ans=0,
   why="Two arbitrary constants differ by another arbitrary constant, so their difference is absorbed into a single C."),
 dict(q="What is the general solution of dy/dx = ky, where k is a constant?", choices=[
   "y = C*e^(kx)",
   "y = C*e^(k*x^2/2)",
   "y = kx + C",
   "y = e^(kx) + C"], ans=0,
   why="Separating gives dy/y = k dx, so ln|y| = kx + C and y = C*e^(kx)."),
 dict(q="What is the general solution of dy/dx = 2x/(3y^2), written implicitly?", choices=[
   "y^3 = x^2 + C",
   "y^3 = x^2/3 + C",
   "3y^3 = 2x^2 + C",
   "y^3 = 2x^2 + C"], ans=0,
   why="Separating gives 3y^2 dy = 2x dx, so y^3 = x^2 + C."),
 dict(q="What is the general solution of dy/dx = y^2 + 1?", choices=[
   "y = tan(x + C)",
   "y = arctan(x) + C",
   "y = C*e^(x) - 1",
   "y = -1/(x + C) + 1"], ans=0,
   why="Separating gives dy/(1 + y^2) = dx, so arctan(y) = x + C and y = tan(x + C)."),
 dict(q="What is the general solution of dy/dx = y*sec^2(x)?", choices=[
   "y = C*e^(tan(x))",
   "y = C*e^(sec(x))",
   "y = C*tan(x)",
   "y = tan(x) + C"], ans=0,
   why="Separating gives dy/y = sec^2(x) dx, so ln|y| = tan(x) + C and y = C*e^(tan(x))."),
 dict(q="What is the general solution of dy/dx = x*e^y?", choices=[
   "y = -ln(C - x^2/2)",
   "y = ln(x^2/2 + C)",
   "y = e^(x^2/2) + C",
   "y = x^2*e^y/2 + C"], ans=0,
   why="Separating gives e^(-y) dy = x dx, so -e^(-y) = x^2/2 + C, e^(-y) = C - x^2/2, and y = -ln(C - x^2/2)."),
 dict(q="What is the general solution of dy/dx = (3x^2 + 1)/(2y), written implicitly?", choices=[
   "y^2 = x^3 + x + C",
   "y^2 = 3x^3 + x + C",
   "2y^2 = x^3 + x + C",
   "y = x^3 + x + C"], ans=0,
   why="Separating gives 2y dy = (3x^2 + 1) dx, so y^2 = x^3 + x + C."),
 dict(q="What is the general solution of dy/dx = 6x^2*y?", choices=[
   "y = C*e^(2x^3)",
   "y = C*e^(6x^3)",
   "y = C*e^(2x^2)",
   "y = 2x^3 + C"], ans=0,
   why="Separating gives dy/y = 6x^2 dx, so ln|y| = 2x^3 + C and y = C*e^(2x^3)."),
 dict(q="After separating dy/dx = 2xy a student writes ln|y| = x^2 + C and then concludes y = e^(x^2) + C. What is the error?", choices=[
   "exponentiating both sides gives y = e^(x^2)*e^C = C*e^(x^2), a constant multiple rather than an added constant",
   "the integral of 2x is x^2/2, not x^2",
   "the left side should integrate to y, not ln|y|",
   "there is no error"], ans=0,
   why="The constant is inside the exponent before exponentiating, so it becomes a multiplicative factor afterward."),
]
