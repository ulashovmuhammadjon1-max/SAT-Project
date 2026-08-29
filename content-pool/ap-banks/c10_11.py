# CALC 10.11 Finding Taylor Polynomial Approximations of Functions — 25 questions
# Answers verified with sympy; see verify_c10_11.py
# P_n(x) = sum from k=0 to n of f^(k)(a)*(x - a)^k/k!.  The two places students
# lose points: forgetting the k! in the denominator, and reading a coefficient
# as a derivative (the coefficient of (x-a)^k is f^(k)(a)/k!, not f^(k)(a)).
TOPIC = ("10.11", "Finding Taylor Polynomial Approximations of Functions", 10)
QUESTIONS = [
 dict(q="The nth-degree Taylor polynomial for f about x = a is", choices=[
   "sum from k=0 to n of f^(k)(a)*(x - a)^k/k!",
   "sum from k=0 to n of f^(k)(a)*(x - a)^k",
   "sum from k=0 to n of f^(k)(x)*(x - a)^k/k!",
   "sum from k=0 to n of f(a)*(x - a)^k/k!"], ans=0,
   why="Each term uses the kth derivative evaluated at the center, divided by k factorial."),

 dict(q="The nth-degree Taylor polynomial P_n for f about x = a is characterized by the property that", choices=[
   "P_n(x) = f(x) for all x near a",
   "P_n and f agree in value and in their first n derivatives at x = a",
   "P_n has the same zeros as f",
   "P_n and f have the same average value near a"], ans=1,
   why="Matching f and its first n derivatives at the center is exactly what the coefficients are chosen to do."),

 dict(q="A Maclaurin polynomial for f is a Taylor polynomial centered at", choices=[
   "x = 1",
   "x = 0",
   "the point where f is largest",
   "any point where f is differentiable"], ans=1,
   why="Maclaurin is the name for the Taylor expansion about 0."),

 dict(q="If f(0) = 2, f'(0) = -3, and f''(0) = 4, then the second-degree Maclaurin polynomial for f is", choices=[
   "2 - 3x + 4x^2",
   "2 - 3x + 2x^2",
   "2 - 3x + x^2/2",
   "2 + 3x + 2x^2"], ans=1,
   why="The x^2 coefficient is f''(0)/2! = 4/2 = 2."),

 dict(q="If f(1) = 5, f'(1) = 2, and f''(1) = -6, then the second-degree Taylor polynomial for f about x = 1 is", choices=[
   "5 + 2(x - 1) - 6(x - 1)^2",
   "5 + 2(x - 1) - 3(x - 1)^2",
   "5 + 2x - 3x^2",
   "5 + 2(x + 1) - 3(x + 1)^2"], ans=1,
   why="The quadratic coefficient is f''(1)/2! = -3, and the powers are of (x - 1)."),

 dict(q="The third-degree Maclaurin polynomial for e^x is", choices=[
   "1 + x + x^2 + x^3",
   "1 + x + x^2/2 + x^3/6",
   "1 + x + x^2/2 + x^3/3",
   "x + x^2/2 + x^3/6"], ans=1,
   why="Every derivative of e^x is 1 at 0, so the coefficients are 1/k!."),

 dict(q="The fourth-degree Maclaurin polynomial for cos(x) is", choices=[
   "1 - x^2/2 + x^4/24",
   "1 - x^2 + x^4",
   "1 - x^2/2 + x^4/12",
   "x - x^3/6"], ans=0,
   why="Only even powers appear, with coefficients (-1)^k/(2k)!."),

 dict(q="The third-degree Maclaurin polynomial for sin(x) is", choices=[
   "x - x^3/3",
   "x - x^3/6",
   "1 - x^2/2",
   "x + x^3/6"], ans=1,
   why="sin(0) = 0, sin'(0) = 1, sin''(0) = 0, sin'''(0) = -1, and -1/3! = -1/6."),

 dict(q="The second-degree Maclaurin polynomial for ln(1 + x) is", choices=[
   "x - x^2",
   "x - x^2/2",
   "1 + x - x^2/2",
   "x + x^2/2"], ans=1,
   why="The derivatives at 0 are 0, 1, and -1, and -1/2! = -1/2."),

 dict(q="The second-degree Taylor polynomial for sqrt(x) about x = 4 is", choices=[
   "2 + (1/4)(x - 4) - (1/64)(x - 4)^2",
   "2 + (1/4)(x - 4) - (1/32)(x - 4)^2",
   "2 + (1/2)(x - 4) - (1/64)(x - 4)^2",
   "2 + (1/4)(x - 4) + (1/64)(x - 4)^2"], ans=0,
   why="f'(4) = 1/4 and f''(4) = -1/32, and the quadratic coefficient is f''(4)/2! = -1/64."),

 dict(q="In the Maclaurin polynomial for e^x, the coefficient of x^4 is", choices=[
   "1",
   "1/4",
   "1/16",
   "1/24"], ans=3,
   why="The coefficient is f^(4)(0)/4! = 1/24."),

 dict(q="In the Maclaurin polynomial for sin(2x), the coefficient of x^3 is", choices=[
   "-4/3",
   "-2/3",
   "-1/6",
   "8/6"], ans=0,
   why="Substituting 2x into x - x^3/6 gives 2x - 8x^3/6 = 2x - (4/3)x^3."),

 dict(q="If the third-degree Maclaurin polynomial for f is 1 + 2x - x^2 + 5x^3, then f'''(0) equals", choices=[
   "5",
   "15",
   "30",
   "5/6"], ans=2,
   why="The coefficient of x^3 is f'''(0)/3!, so f'''(0) = 5 * 6 = 30."),

 dict(q="If the second-degree Taylor polynomial for f about x = 2 is 3 - 4(x - 2) + 7(x - 2)^2, then f''(2) equals", choices=[
   "7",
   "14",
   "7/2",
   "-4"], ans=1,
   why="The quadratic coefficient is f''(2)/2!, so f''(2) = 7 * 2 = 14."),

 dict(q="Using the second-degree Maclaurin polynomial for e^x, the approximation of e^(0.1) is", choices=[
   "1.1",
   "1.105",
   "1.1052",
   "1.11"], ans=1,
   why="1 + 0.1 + (0.1)^2/2 = 1.105."),

 dict(q="The first-degree Taylor polynomial for ln(x) about x = 1 is", choices=[
   "x",
   "x - 1",
   "1 - x",
   "ln(x) - 1"], ans=1,
   why="f(1) = 0 and f'(1) = 1, so P_1(x) = 0 + 1*(x - 1)."),

 dict(q="The fourth-degree Maclaurin polynomial for 1/(1 - x) is", choices=[
   "1 + x + x^2 + x^3 + x^4",
   "1 - x + x^2 - x^3 + x^4",
   "1 + x + x^2/2 + x^3/6 + x^4/24",
   "x + x^2 + x^3 + x^4"], ans=0,
   why="The kth derivative at 0 is k!, so every coefficient k!/k! equals 1."),

 dict(q="The second-degree Maclaurin polynomial for e^(2x) is", choices=[
   "1 + 2x + 2x^2",
   "1 + 2x + 4x^2",
   "1 + 2x + x^2",
   "1 + x + x^2/2"], ans=0,
   why="Substituting 2x into 1 + x + x^2/2 gives 1 + 2x + 4x^2/2 = 1 + 2x + 2x^2."),

 dict(q="The third-degree Taylor polynomial for cos(x) about x = pi/2 is", choices=[
   "1 - (x - pi/2)^2/2",
   "-(x - pi/2) + (x - pi/2)^3/6",
   "(x - pi/2) - (x - pi/2)^3/6",
   "-(x - pi/2) - (x - pi/2)^3/6"], ans=1,
   why="At pi/2 the values are 0, -1, 0, 1, so the polynomial is -(x - pi/2) + (x - pi/2)^3/3!."),

 dict(q="The third-degree Maclaurin polynomial for x*e^x is", choices=[
   "x + x^2 + x^3/2",
   "x + x^2 + x^3/6",
   "x + x^2/2 + x^3/6",
   "1 + x + x^2/2"], ans=0,
   why="Multiplying 1 + x + x^2/2 + ... by x gives x + x^2 + x^3/2 through degree 3."),

 dict(q="The fourth-degree Maclaurin polynomial for cos(x^2) is", choices=[
   "1 - x^4/2",
   "1 - x^4/24",
   "1 - x^2/2 + x^4/24",
   "1 - x^4/2 + x^8/24"], ans=0,
   why="Substituting x^2 into 1 - u^2/2 + ... gives 1 - x^4/2, and the next term has degree 8."),

 dict(q="The second-degree Taylor polynomial for 1/x about x = 1 is", choices=[
   "1 - (x - 1) + (x - 1)^2",
   "1 - (x - 1) + 2(x - 1)^2",
   "1 + (x - 1) + (x - 1)^2",
   "1 - (x - 1) + (x - 1)^2/2"], ans=0,
   why="f(1) = 1, f'(1) = -1, f''(1) = 2, and the quadratic coefficient is 2/2! = 1."),

 dict(q="The third-degree Maclaurin polynomial for e^x*sin(x) is", choices=[
   "x + x^2 + x^3/3",
   "x + x^2 + x^3/2",
   "x + x^2/2 + x^3/6",
   "x - x^3/6"], ans=0,
   why="Multiplying the two Maclaurin polynomials and keeping terms through degree 3 gives x + x^2 + x^3/3."),

 dict(q="If the fourth-degree Maclaurin polynomial for f is 2 - x + 3x^2 - x^3 + x^4/2, then f^(4)(0) equals", choices=[
   "1/2",
   "2",
   "12",
   "24"], ans=2,
   why="The coefficient of x^4 is f^(4)(0)/4!, so f^(4)(0) = (1/2)(24) = 12."),

 dict(q="The fifth-degree Maclaurin polynomial for sin(x) has how many nonzero terms?", choices=[
   "2",
   "3",
   "5",
   "6"], ans=1,
   why="Only the odd powers survive: x, -x^3/6, and x^5/120."),
]
