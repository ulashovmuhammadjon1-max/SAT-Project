# CALC 2.2 Defining the Derivative of a Function and Using Derivative Notation — 25 questions
# Answers verified with sympy; see verify_c2_2.py.
# Questions 1, 2, 3, 4, 12, 13 and 20 are conceptual (the two forms of the
# definition, matching a limit to a derivative, and notation) and carry no
# sympy check.
TOPIC = ("2.2", "Defining the Derivative of a Function and Using Derivative Notation", 2)
QUESTIONS = [
 dict(q="The derivative of a function f is defined by which expression?", choices=[
   "f'(x) = lim as h -> 0 of (f(x + h) - f(x))/h",
   "f'(x) = lim as h -> 0 of (f(x + h) - f(x))",
   "f'(x) = lim as x -> 0 of (f(x + h) - f(x))/h",
   "f'(x) = (f(x + h) - f(x))/h"], ans=0,
   why="The derivative is the limit of the difference quotient as h approaches 0, with the limit taken in h, not in x."),
 dict(q="Which expression is the alternate (difference-of-points) form of the derivative of f at x = a?", choices=[
   "lim as x -> a of (f(x) - f(a))/(x - a)",
   "lim as x -> a of (f(x) - f(a))",
   "lim as x -> 0 of (f(x) - f(a))/(x - a)",
   "lim as a -> x of (f(x) - f(a))/x"], ans=0,
   why="The alternate form lets x approach a and divides the change in f by the change in x, x - a."),
 dict(q="If f is differentiable at 3, which of the following limits equals f'(3)?", choices=[
   "lim as x -> 3 of (f(x) - f(3))/(x - 3)",
   "lim as x -> 3 of (f(x) - f(3))",
   "lim as h -> 0 of (f(3) - f(3 + h))/h",
   "lim as x -> 0 of (f(x) - f(3))/(x - 3)"], ans=0,
   why="The third choice is the negative of f'(3) because its numerator is subtracted in the wrong order, and the others are not difference quotients approaching 3."),
 dict(q="If f(x) = x^4, which of the following expressions represents f'(3)?", choices=[
   "lim as h -> 0 of ((3 + h)^4 - 81)/h",
   "lim as h -> 0 of ((3 + h)^4 - 81)/3",
   "lim as h -> 0 of ((3 + h)^4 - 3)/h",
   "lim as h -> 0 of ((x + h)^4 - x^4)/h"], ans=0,
   why="Substituting a = 3 into the definition gives f(3) = 81 in the numerator and h in the denominator; the last choice is f'(x), not f'(3)."),
 dict(q="Using the definition of the derivative, if f(x) = x^2 then f'(x) =", choices=[
   "2x", "x", "2", "x^2"], ans=0,
   why="((x + h)^2 - x^2)/h = (2xh + h^2)/h = 2x + h, and letting h -> 0 gives 2x."),
 dict(q="Using the definition of the derivative, if f(x) = 3x + 5 then f'(x) =", choices=[
   "3", "5", "3x", "3x + 5"], ans=0,
   why="((3(x + h) + 5) - (3x + 5))/h = 3h/h = 3 for every h, so the limit is 3."),
 dict(q="If f(x) = x^2, then f'(4) =", choices=[
   "2", "4", "8", "16"], ans=2,
   why="f'(x) = 2x, so f'(4) = 8; 16 is f(4), not f'(4)."),
 dict(q="The limit lim as h -> 0 of ((2 + h)^5 - 32)/h is equal to", choices=[
   "5", "32", "80", "160"], ans=2,
   why="This is f'(2) for f(x) = x^5, and f'(x) = 5x^4 gives 5(16) = 80."),
 dict(q="The limit lim as h -> 0 of (sqrt(9 + h) - 3)/h is equal to", choices=[
   "3", "1/2", "1/3", "1/6"], ans=3,
   why="This is the derivative of sqrt(x) at x = 9, which is 1/(2 sqrt(9)) = 1/6."),
 dict(q="The limit lim as x -> 1 of (x^3 - 1)/(x - 1) is equal to", choices=[
   "0", "1", "2", "3"], ans=3,
   why="This is the alternate form of the derivative of x^3 at x = 1, which is 3(1)^2 = 3."),
 dict(q="The limit lim as h -> 0 of (cos(pi/3 + h) - cos(pi/3))/h is equal to", choices=[
   "-sqrt(3)/2", "sqrt(3)/2", "-1/2", "1/2"], ans=0,
   why="This is the derivative of cos(x) at pi/3, and since d/dx[cos x] = -sin x, the value is -sin(pi/3) = -sqrt(3)/2."),
 dict(q="Which of the following does NOT denote the first derivative of y = f(x) with respect to x?", choices=[
   "d^2y/dx^2", "dy/dx", "y'", "d/dx[f(x)]"], ans=0,
   why="d^2y/dx^2 is the second derivative; the other three are standard notations for the first."),
 dict(q="If y = f(x), which of the following denotes the value of the derivative of f at x = 2?", choices=[
   "f'(2)", "d/dx[f(2)]", "f(2)", "dy/dx for every x"], ans=0,
   why="f(2) is a constant, so d/dx[f(2)] is 0; the value of the derivative at a point is written f'(2) or dy/dx evaluated at x = 2."),
 dict(q="Using the definition of the derivative, if f(x) = 1/x then f'(x) =", choices=[
   "-1/x^2", "1/x^2", "-1/x", "ln(x)"], ans=0,
   why="(1/(x + h) - 1/x)/h = -1/(x(x + h)), and letting h -> 0 gives -1/x^2."),
 dict(q="If f(x) = x^2 - 3x, then f'(a) =", choices=[
   "2a - 3", "2a", "a^2 - 3", "2a + 3"], ans=0,
   why="Differentiating term by term gives f'(x) = 2x - 3, so f'(a) = 2a - 3."),
 dict(q="For f(x) = x^2 + 1, the difference quotient (f(x + h) - f(x))/h simplifies, for h not 0, to", choices=[
   "2x + h", "2x", "2x + h + 1", "2xh + h^2"], ans=0,
   why="(x^2 + 2xh + h^2 + 1 - x^2 - 1)/h = (2xh + h^2)/h = 2x + h; the constant 1 cancels."),
 dict(q="For f(x) = x^3, the difference quotient (f(x + h) - f(x))/h simplifies, for h not 0, to", choices=[
   "3x^2 + 3xh + h^2", "3x^2", "3x^2 + h^2", "x^3 + 3x^2h"], ans=0,
   why="Expanding (x + h)^3 - x^3 gives 3x^2h + 3xh^2 + h^3, and dividing by h gives 3x^2 + 3xh + h^2."),
 dict(q="The limit lim as h -> 0 of (e^h - 1)/h is equal to", choices=[
   "0", "1", "e", "does not exist"], ans=1,
   why="This is the derivative of e^x at x = 0, which is e^0 = 1."),
 dict(q="The limit lim as h -> 0 of ln(1 + h)/h is equal to", choices=[
   "0", "1", "e", "ln(2)"], ans=1,
   why="This is the derivative of ln(x) at x = 1, which is 1/1 = 1."),
 dict(q="The statement f'(2) = 5 means that", choices=[
   "the slope of the line tangent to y = f(x) at x = 2 is 5",
   "the value of f at x = 2 is 5",
   "the average rate of change of f on [0, 2] is 5",
   "the graph of f passes through the point (5, 2)"], ans=0,
   why="The derivative at a point is the slope of the tangent line there, not a function value."),
 dict(q="The limit lim as h -> 0 of ((3 + h)^2 - 9)/h is equal to", choices=[
   "0", "3", "6", "9"], ans=2,
   why="This is the derivative of x^2 at x = 3, which is 2(3) = 6."),
 dict(q="If f is differentiable with f'(2) = 4, then lim as h -> 0 of (f(2 + 3h) - f(2))/h is equal to", choices=[
   "4/3", "3", "4", "12"], ans=3,
   why="Writing the quotient as 3 times (f(2 + 3h) - f(2))/(3h) gives 3 f'(2) = 12."),
 dict(q="If f is differentiable with f'(1) = 7, then lim as h -> 0 of (f(1 + h) - f(1 - h))/(2h) is equal to", choices=[
   "0", "7/2", "7", "14"], ans=2,
   why="The symmetric difference quotient splits into half the sum of two ordinary difference quotients, each approaching f'(1) = 7."),
 dict(q="Using the definition of the derivative, if g(x) = sqrt(x) then g'(x) =", choices=[
   "1/(2 sqrt(x))", "2 sqrt(x)", "1/sqrt(x)", "-1/(2 sqrt(x))"], ans=0,
   why="Multiplying the difference quotient by the conjugate gives 1/(sqrt(x + h) + sqrt(x)), which tends to 1/(2 sqrt(x))."),
 dict(q="The limit lim as x -> 4 of (x^(3/2) - 8)/(x - 4) is equal to", choices=[
   "3/2", "3", "8", "12"], ans=1,
   why="This is the derivative of x^(3/2) at x = 4, which is (3/2)(4)^(1/2) = 3."),
]
