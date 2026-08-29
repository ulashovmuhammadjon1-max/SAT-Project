# CALC 7.7 Finding Particular Solutions Using Initial Conditions and
# Separation of Variables — 25 questions
# Every particular solution is checked in verify_c7_7.py by substituting it
# into the differential equation and confirming the initial condition.
TOPIC = ("7.7", "Finding Particular Solutions Using Initial Conditions and Separation of Variables", 7)
QUESTIONS = [
 dict(q="Solve dy/dx = 2x with y(1) = 5.", choices=[
   "y = x^2 + 4",
   "y = x^2 + 5",
   "y = x^2 - 4",
   "y = 2x^2 + 3"], ans=0,
   why="Antidifferentiating gives y = x^2 + C, and 1 + C = 5 forces C = 4."),
 dict(q="Solve dy/dx = y with y(0) = 3.", choices=[
   "y = 3e^x",
   "y = e^x + 3",
   "y = e^x + 2",
   "y = e^(3x)"], ans=0,
   why="The general solution is y = C*e^x, and y(0) = C = 3."),
 dict(q="Solve dy/dx = xy with y(0) = 2.", choices=[
   "y = 2e^(x^2/2)",
   "y = 2e^(x^2)",
   "y = e^(x^2/2) + 1",
   "y = e^(2x)"], ans=0,
   why="The general solution is y = C*e^(x^2/2), and y(0) = C = 2."),
 dict(q="Solve dy/dx = -3y with y(0) = 5.", choices=[
   "y = 5e^(-3x)",
   "y = 5e^(3x)",
   "y = -3e^(5x)",
   "y = 5 - 3x"], ans=0,
   why="The general solution is y = C*e^(-3x), and y(0) = C = 5."),
 dict(q="For x > 0, solve dy/dx = y/x with y(1) = 4.", choices=[
   "y = 4x",
   "y = x + 3",
   "y = 4e^(x - 1)",
   "y = 4*ln(x) + 4"], ans=0,
   why="The general solution is y = Cx, and y(1) = C = 4."),
 dict(q="Solve dy/dx = x/y with y(0) = 3.", choices=[
   "y = sqrt(x^2 + 9)",
   "y = sqrt(x^2 + 3)",
   "y = sqrt(x^2) + 3",
   "y = x^2/2 + 3"], ans=0,
   why="Separating gives y^2 = x^2 + C, and 9 = 0 + C, so y = sqrt(x^2 + 9) on the positive branch."),
 dict(q="Solve dy/dx = x/y with y(0) = -3.", choices=[
   "y = -sqrt(x^2 + 9)",
   "y = sqrt(x^2 + 9)",
   "y = -sqrt(x^2 - 9)",
   "y = -x^2/2 - 3"], ans=0,
   why="Separating gives y^2 = x^2 + 9, and the initial value is negative, so the solution must be the negative square root."),
 dict(q="Solve dy/dx = y^2 with y(0) = 1.", choices=[
   "y = 1/(1 - x)",
   "y = 1/(1 + x)",
   "y = -1/(x + 1)",
   "y = e^x"], ans=0,
   why="Separating gives -1/y = x + C, and y(0) = 1 forces C = -1, so y = 1/(1 - x)."),
 dict(q="Let y be the solution of dy/dx = y^2 with y(0) = 1. What is y(1/2)?", choices=[
   "2",
   "1/2",
   "3/2",
   "2/3"], ans=0,
   why="The solution is y = 1/(1 - x), and 1/(1 - 1/2) = 2."),
 dict(q="Let y be the solution of dy/dx = y^2 with y(0) = 1. What is the largest interval containing x = 0 on which the solution exists?", choices=[
   "x < 1",
   "all real numbers",
   "x > 0",
   "-1 < x < 1"], ans=0,
   why="The solution y = 1/(1 - x) blows up as x approaches 1, so the interval of existence stops there."),
 dict(q="Solve dy/dx = 2x*y^2 with y(0) = -1.", choices=[
   "y = -1/(x^2 + 1)",
   "y = 1/(x^2 + 1)",
   "y = -1/(x^2 - 1)",
   "y = -e^(x^2)"], ans=0,
   why="Separating gives -1/y = x^2 + C, and y(0) = -1 gives C = 1, so y = -1/(x^2 + 1)."),
 dict(q="Solve dy/dx = e^x/y with y(0) = 2.", choices=[
   "y = sqrt(2e^x + 2)",
   "y = sqrt(2e^x + 4)",
   "y = sqrt(e^x + 3)",
   "y = 2e^x"], ans=0,
   why="Separating gives y^2 = 2e^x + C, and 4 = 2 + C forces C = 2."),
 dict(q="Solve dy/dx = y*cos(x) with y(0) = 4.", choices=[
   "y = 4e^(sin(x))",
   "y = 4e^(cos(x))",
   "y = 4 + sin(x)",
   "y = e^(4sin(x))"], ans=0,
   why="The general solution is y = C*e^(sin(x)), and y(0) = C*e^0 = C = 4."),
 dict(q="Solve dy/dx = x(y + 1) with y(0) = 1.", choices=[
   "y = 2e^(x^2/2) - 1",
   "y = e^(x^2/2) + 1",
   "y = 2e^(x^2/2) + 1",
   "y = 2e^(x^2) - 1"], ans=0,
   why="The general solution is y = C*e^(x^2/2) - 1, and 1 = C - 1 forces C = 2."),
 dict(q="Solve dy/dx = 3x^2*y with y(0) = 2.", choices=[
   "y = 2e^(x^3)",
   "y = 2e^(3x^3)",
   "y = e^(x^3) + 1",
   "y = 2e^(x^2)"], ans=0,
   why="The general solution is y = C*e^(x^3), and y(0) = C = 2."),
 dict(q="Let y be the solution of dy/dx = 2x with y(1) = 5. What is y(2)?", choices=[
   "8",
   "9",
   "4",
   "10"], ans=0,
   why="The solution is y = x^2 + 4, and 4 + 4 = 8."),
 dict(q="Let y be the solution of dy/dx = xy with y(0) = 2. What is y(1)?", choices=[
   "2*sqrt(e)",
   "2e",
   "e/2",
   "sqrt(2e)"], ans=0,
   why="The solution is y = 2e^(x^2/2), so y(1) = 2e^(1/2)."),
 dict(q="Solve dy/dx = 1/(2y) with y(0) = 1, taking the branch through the initial point.", choices=[
   "y = sqrt(x + 1)",
   "y = sqrt(x) + 1",
   "y = sqrt(2x + 1)",
   "y = (x + 1)/2"], ans=0,
   why="Separating gives 2y dy = dx, so y^2 = x + C, and 1 = C gives y = sqrt(x + 1)."),
 dict(q="For x > 0, solve dy/dx = -y/x with y(1) = 6.", choices=[
   "y = 6/x",
   "y = 6x",
   "y = -6x",
   "y = 6 - ln(x)"], ans=0,
   why="Separating gives ln|y| = -ln(x) + C, so y = C/x, and y(1) = C = 6."),
 dict(q="Solve dy/dx = y*cos(x) with y(pi/2) = 1.", choices=[
   "y = e^(sin(x) - 1)",
   "y = e^(sin(x))",
   "y = e^(sin(x) + 1)",
   "y = sin(x)"], ans=0,
   why="The general solution is y = C*e^(sin(x)), and 1 = C*e^1 gives C = e^(-1)."),
 dict(q="Solve dy/dx = 2x + 1 with y(0) = -3.", choices=[
   "y = x^2 + x - 3",
   "y = x^2 + x + 3",
   "y = 2x^2 + x - 3",
   "y = x^2 - 3"], ans=0,
   why="Antidifferentiating gives y = x^2 + x + C, and y(0) = C = -3."),
 dict(q="An object cools according to dT/dt = -k(T - 70) with T(0) = 170, where k is a positive constant. What is T as a function of t?", choices=[
   "T = 70 + 100e^(-kt)",
   "T = 70 + 170e^(-kt)",
   "T = 170e^(-kt)",
   "T = 70 - 100e^(-kt)"], ans=0,
   why="Separating gives T - 70 = C*e^(-kt), and T(0) = 170 forces C = 100."),
 dict(q="For x > 0, solve dy/dx = y/x^2 with y(1) = e.", choices=[
   "y = e^(2 - 1/x)",
   "y = e^(1 - 1/x)",
   "y = e^(1/x)",
   "y = e*x^2"], ans=0,
   why="Separating gives ln|y| = -1/x + C, so y = C*e^(-1/x), and e = C*e^(-1) forces C = e^2."),
 dict(q="For y > 0, solve dy/dx = sqrt(y) with y(0) = 4.", choices=[
   "y = (x + 4)^2/4",
   "y = (x + 2)^2",
   "y = (x/2 + 4)^2",
   "y = x^2/4 + 4"], ans=0,
   why="Separating gives 2*sqrt(y) = x + C, so 4 = C, and sqrt(y) = (x + 4)/2."),
 dict(q="A quantity satisfies dy/dt = ky with y(0) = 100 and y(2) = 400. What is y as a function of t?", choices=[
   "y = 100*2^t",
   "y = 100*4^t",
   "y = 100*e^(2t)",
   "y = 100 + 150t"], ans=0,
   why="From 400 = 100e^(2k) we get e^(2k) = 4, so k = ln(2) and y = 100e^(t*ln 2) = 100*2^t."),
]
