# CALC 7.2 Verifying Solutions for Differential Equations — 25 questions
# Substituting a proposed function and its derivatives into a differential
# equation. Every key is confirmed by sympy substitution; see verify_c7_2.py.
TOPIC = ("7.2", "Verifying Solutions for Differential Equations", 7)
QUESTIONS = [
 dict(q="Which of the following functions is a solution of dy/dx = 3y?", choices=[
   "y = e^(3x)",
   "y = 3e^x",
   "y = x^3",
   "y = 3x"], ans=0,
   why="Differentiating e^(3x) gives 3e^(3x), which is 3 times the function itself."),
 dict(q="Which of the following functions is a solution of dy/dx = -5y?", choices=[
   "y = 4e^(-5x)",
   "y = -5e^(4x)",
   "y = 4e^(5x)",
   "y = -5x + 4"], ans=0,
   why="The derivative of 4e^(-5x) is -20e^(-5x), which equals -5 times 4e^(-5x)."),
 dict(q="The function y = x^2 + 3 is a solution of which differential equation?", choices=[
   "dy/dx = 2x",
   "dy/dx = 2x + 3",
   "dy/dx = 2y",
   "dy/dx = x^2"], ans=0,
   why="The derivative of x^2 + 3 is 2x; the constant 3 disappears under differentiation."),
 dict(q="Which of the following is a solution of y'' + 9y = 0?", choices=[
   "y = cos(3x)",
   "y = cos(9x)",
   "y = e^(3x)",
   "y = sin(x/3)"], ans=0,
   why="If y = cos(3x) then y'' = -9cos(3x), so y'' + 9y = 0."),
 dict(q="Which of the following is NOT a solution of dy/dx = y?", choices=[
   "y = x*e^x",
   "y = e^x",
   "y = 2e^x",
   "y = -3e^x"], ans=0,
   why="The derivative of x*e^x is e^x + x*e^x, which is not equal to x*e^x."),
 dict(q="The function y = 5e^(x^2) is a solution of which differential equation?", choices=[
   "dy/dx = 2xy",
   "dy/dx = 2y",
   "dy/dx = x^2*y",
   "dy/dx = 10x"], ans=0,
   why="By the chain rule dy/dx = 5*(2x)*e^(x^2) = 2x*y."),
 dict(q="For x not 0, the function y = 1/x is a solution of which differential equation?", choices=[
   "dy/dx = -y^2",
   "dy/dx = y^2",
   "dy/dx = -y",
   "dy/dx = 1/y"], ans=0,
   why="dy/dx = -1/x^2 = -(1/x)^2 = -y^2."),
 dict(q="The function y = tan(x) is a solution of which differential equation?", choices=[
   "dy/dx = 1 + y^2",
   "dy/dx = 1 - y^2",
   "dy/dx = y^2",
   "dy/dx = sec(x)"], ans=0,
   why="The derivative of tan(x) is sec^2(x), and the identity sec^2(x) = 1 + tan^2(x) makes this 1 + y^2."),
 dict(q="For x > 0, the function y = x*ln(x) is a solution of which differential equation?", choices=[
   "x*dy/dx = y + x",
   "x*dy/dx = y",
   "dy/dx = y/x",
   "dy/dx = ln(x)"], ans=0,
   why="dy/dx = ln(x) + 1, so x*dy/dx = x*ln(x) + x = y + x."),
 dict(q="The function y = e^(-x) + 2 is a solution of which differential equation?", choices=[
   "dy/dx = 2 - y",
   "dy/dx = y - 2",
   "dy/dx = -y",
   "dy/dx = y + 2"], ans=0,
   why="dy/dx = -e^(-x), and 2 - y = 2 - (e^(-x) + 2) = -e^(-x)."),
 dict(q="If x^2 + y^2 = 25 defines y implicitly as a function of x, which differential equation does y satisfy for y not 0?", choices=[
   "dy/dx = -x/y",
   "dy/dx = x/y",
   "dy/dx = -y/x",
   "dy/dx = -2x"], ans=0,
   why="Implicit differentiation gives 2x + 2y*dy/dx = 0, so dy/dx = -x/y."),
 dict(q="For x not 0, the function y = 3x^2 is a solution of which differential equation?", choices=[
   "x*dy/dx = 2y",
   "x*dy/dx = y",
   "dy/dx = 2y",
   "dy/dx = y/x"], ans=0,
   why="dy/dx = 6x, so x*dy/dx = 6x^2 = 2*(3x^2) = 2y."),
 dict(q="Verify: is y = e^(2x) a solution of y'' - 5y' + 6y = 0?", choices=[
   "Yes, because 4e^(2x) - 10e^(2x) + 6e^(2x) = 0",
   "No, because the left side simplifies to 2e^(2x)",
   "No, because y'' = 2e^(2x)",
   "Yes, but only at x = 0"], ans=0,
   why="y' = 2e^(2x) and y'' = 4e^(2x), and 4 - 10 + 6 = 0 makes the whole expression vanish for every x."),
 dict(q="Which of the following is a solution of y'' - y = 0?", choices=[
   "y = e^(-x)",
   "y = sin(x)",
   "y = cos(x)",
   "y = x^2"], ans=0,
   why="The second derivative of e^(-x) is e^(-x) itself, so y'' - y = 0."),
 dict(q="The function y = 2e^(3t) - 1 is the solution of which initial value problem?", choices=[
   "dy/dt = 3y + 3, y(0) = 1",
   "dy/dt = 3y, y(0) = 1",
   "dy/dt = 3y - 3, y(0) = 1",
   "dy/dt = 3y + 3, y(0) = 2"], ans=0,
   why="dy/dt = 6e^(3t) and 3y + 3 = 6e^(3t) - 3 + 3 = 6e^(3t), while y(0) = 2 - 1 = 1."),
 dict(q="For which value of k is y = e^(kx) a solution of y'' + y' - 6y = 0?", choices=[
   "k = 2",
   "k = 3",
   "k = -2",
   "k = 6"], ans=0,
   why="Substituting gives (k^2 + k - 6)e^(kx) = 0, so k^2 + k - 6 = 0 and k = 2 or k = -3."),
 dict(q="For which value of r is y = x^r a solution of x^2*y'' - 2y = 0 for x > 0?", choices=[
   "r = 2",
   "r = 1",
   "r = -2",
   "r = 3"], ans=0,
   why="Substituting gives r(r - 1) - 2 = 0, so r^2 - r - 2 = 0 and r = 2 or r = -1."),
 dict(q="For which value of C is y = x^2 + C the particular solution of dy/dx = 2x that satisfies y(2) = 7?", choices=[
   "C = 3",
   "C = 7",
   "C = -3",
   "C = 11"], ans=0,
   why="Substituting x = 2 gives 4 + C = 7, so C = 3."),
 dict(q="For which values of the constant A is y = A*x^3 a solution of dy/dx = 3y/x on x > 0?", choices=[
   "every real number A",
   "only A = 1",
   "only A = 3",
   "only A = 0"], ans=0,
   why="dy/dx = 3A*x^2 and 3y/x = 3A*x^3/x = 3A*x^2 for every A, so the whole family works."),
 dict(q="What is the general solution of dy/dx = 4x^3?", choices=[
   "y = x^4 + C",
   "y = x^4",
   "y = 12x^2 + C",
   "y = 4x^4 + C"], ans=0,
   why="Antidifferentiating 4x^3 gives x^4, and the arbitrary constant must be included."),
 dict(q="A function f is a solution of a differential equation on an interval I provided that", choices=[
   "substituting f and its derivatives into the equation produces a true statement for every x in I",
   "f satisfies the equation at one point of I",
   "f is continuous on I",
   "f is the only function satisfying the equation on I"], ans=0,
   why="A solution must make the equation true at every point of the interval, not merely at one point."),
 dict(q="A student knows that y = e^(2x) satisfies dy/dx = 2y and concludes that y = e^(2x) + 5 also satisfies it. Is the student right?", choices=[
   "No, because dy/dx = 2e^(2x) but 2y = 2e^(2x) + 10",
   "Yes, because adding a constant never changes a derivative",
   "Yes, because 5 is a solution of dy/dx = 2y",
   "No, because e^(2x) + 5 is not differentiable"], ans=0,
   why="Adding a constant leaves the left side unchanged but increases the right side by 10, so the equation fails."),
 dict(q="Which family of functions solves dy/dx = y^2?", choices=[
   "y = -1/(x + C)",
   "y = 1/(x + C)",
   "y = C*e^x",
   "y = C/x"], ans=0,
   why="If y = -1/(x + C) then dy/dx = 1/(x + C)^2 = y^2."),
 dict(q="The function y = sqrt(x^2 + 4) is a solution of which differential equation?", choices=[
   "dy/dx = x/y",
   "dy/dx = y/x",
   "dy/dx = 2x/y",
   "dy/dx = x*y"], ans=0,
   why="dy/dx = x/sqrt(x^2 + 4), and sqrt(x^2 + 4) is exactly y."),
 dict(q="The function y = e^(x^2/2) is a solution of which differential equation?", choices=[
   "dy/dx = x*y",
   "dy/dx = y",
   "dy/dx = x^2*y/2",
   "dy/dx = x*e^x"], ans=0,
   why="By the chain rule dy/dx = x*e^(x^2/2) = x*y."),
]
