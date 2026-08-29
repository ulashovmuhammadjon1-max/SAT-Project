# CALC 2.5 Applying the Power Rule — 25 questions
# Every derivative is confirmed with sp.diff in verify_c2_5.py, which also
# checks that no distractor is equivalent to the key.
# Questions 1, 8 and 16 are conceptual (the statement of the rule, the case it
# does not cover, and a diagnosed student error).
TOPIC = ("2.5", "Applying the Power Rule", 2)
QUESTIONS = [
 dict(q="The power rule states that for a constant n, d/dx[x^n] =", choices=[
   "n x^(n-1)", "n x^(n+1)", "x^(n-1)", "(1/(n+1)) x^(n+1)"], ans=0,
   why="The exponent multiplies in front and drops by one; the last choice is the antiderivative, not the derivative."),
 dict(q="If f(x) = x^5, then f'(x) =", choices=[
   "5x^4", "5x^5", "x^4", "(1/6)x^6"], ans=0,
   why="Multiply by the exponent 5 and reduce the exponent to 4."),
 dict(q="If f(x) = x^(-3), then f'(x) =", choices=[
   "-3x^(-4)", "-3x^(-2)", "3x^(-4)", "(-1/2)x^(-2)"], ans=0,
   why="The rule applies to negative exponents too: -3 in front and the exponent -3 - 1 = -4; the second choice adds 1 instead of subtracting."),
 dict(q="If f(x) = sqrt(x), then f'(x) =", choices=[
   "1/(2 sqrt(x))", "2 sqrt(x)", "1/sqrt(x)", "(1/2) sqrt(x)"], ans=0,
   why="Write sqrt(x) as x^(1/2), so f'(x) = (1/2)x^(-1/2) = 1/(2 sqrt(x))."),
 dict(q="If f(x) = x^(2/3), then f'(x) =", choices=[
   "(2/3)x^(-1/3)", "(2/3)x^(2/3)", "(3/2)x^(-1/3)", "(3/5)x^(5/3)"], ans=0,
   why="2/3 in front and the exponent 2/3 - 1 = -1/3; the second choice forgets to reduce the exponent and the last is the antiderivative."),
 dict(q="If f(x) = sqrt(x^3), then f'(x) =", choices=[
   "(3/2)x^(1/2)", "(3/2)x^(3/2)", "(2/3)x^(1/2)", "(1/2)x^(1/2)"], ans=0,
   why="Rewrite the radical as x^(3/2) first, giving (3/2)x^(1/2)."),
 dict(q="If f(x) = 1/x^4, then f'(x) =", choices=[
   "-4/x^5", "4/x^5", "-4/x^3", "-1/(4x^3)"], ans=0,
   why="Rewrite as x^(-4), so f'(x) = -4x^(-5) = -4/x^5."),
 dict(q="Why does the power rule not give the derivative of f(x) = 2^x?", choices=[
   "The power rule applies when the base is the variable and the exponent is constant, and here that is reversed",
   "The power rule applies only to positive integer exponents",
   "The power rule applies only when x is positive",
   "It does give the derivative, namely x 2^(x-1)"], ans=0,
   why="In 2^x the variable sits in the exponent, so it is an exponential function, not a power function."),
 dict(q="If f(x) = x^10, then f'(2) =", choices=[
   "512", "1024", "2560", "5120"], ans=3,
   why="f'(x) = 10x^9, so f'(2) = 10(512) = 5120; 1024 is f(2), not f'(2)."),
 dict(q="If f(x) = 1/x, then f'(3) =", choices=[
   "-1/3", "-1/9", "1/9", "1/3"], ans=1,
   why="f(x) = x^(-1) gives f'(x) = -x^(-2) = -1/x^2, so f'(3) = -1/9."),
 dict(q="If f(x) = x^(1/3), then f'(8) =", choices=[
   "1/12", "1/6", "2/3", "2"], ans=0,
   why="f'(x) = (1/3)x^(-2/3), so f'(8) = (1/3)(1/4) = 1/12; the value 2 is f(8)."),
 dict(q="If f(x) = x^(3/2), then f'(4) =", choices=[
   "3", "6", "8", "12"], ans=0,
   why="f'(x) = (3/2)x^(1/2), so f'(4) = (3/2)(2) = 3; 8 is f(4) and 12 comes from forgetting to reduce the exponent."),
 dict(q="If f(x) = 1/sqrt(x), then f'(x) =", choices=[
   "-1/(2x^(3/2))", "1/(2x^(3/2))", "-1/(2 sqrt(x))", "-2/x^(3/2)"], ans=0,
   why="Rewrite as x^(-1/2), so f'(x) = (-1/2)x^(-3/2) = -1/(2x^(3/2))."),
 dict(q="If f(x) = x^(5/2), then f'(x) =", choices=[
   "(5/2)x^(3/2)", "(5/2)x^(7/2)", "(2/7)x^(7/2)", "(3/2)x^(5/2)"], ans=0,
   why="5/2 in front and the exponent 5/2 - 1 = 3/2."),
 dict(q="If f(x) = x^100, then f'(x) =", choices=[
   "100x^99", "100x^100", "x^99", "(1/101)x^101"], ans=0,
   why="The exponent 100 multiplies in front and drops to 99."),
 dict(q="A student differentiates f(x) = x^4 and writes f'(x) = 4x^4. What is the error?", choices=[
   "The exponent must be reduced by 1, giving 4x^3",
   "The coefficient should be 1/4, not 4",
   "The exponent should be increased by 1, giving 4x^5",
   "There is no error"], ans=0,
   why="The student multiplied by the exponent but forgot to subtract 1 from it."),
 dict(q="If f(x) = x^(-2/3), then f'(x) =", choices=[
   "-(2/3)x^(-5/3)", "(2/3)x^(-5/3)", "-(2/3)x^(1/3)", "-(3/2)x^(-5/3)"], ans=0,
   why="-2/3 in front and the exponent -2/3 - 1 = -5/3; the third choice adds 1 to the exponent instead of subtracting."),
 dict(q="If f(x) = x^pi, then f'(x) =", choices=[
   "pi x^(pi - 1)", "pi x^pi", "x^(pi - 1)", "(1/(pi + 1))x^(pi + 1)"], ans=0,
   why="The power rule holds for any constant exponent, irrational ones included."),
 dict(q="If f(x) = (x^3)^2, then f'(x) =", choices=[
   "6x^5", "2x^3", "6x^6", "5x^6"], ans=0,
   why="Simplify to x^6 first, so f'(x) = 6x^5; the choice 2x^3 comes from treating x^3 as if it were the variable."),
 dict(q="The slope of the line tangent to y = x^3 at the point where x = 2 is", choices=[
   "6", "8", "12", "24"], ans=2,
   why="dy/dx = 3x^2, so the slope is 3(4) = 12; 8 is the y-coordinate, not the slope."),
 dict(q="An equation of the line tangent to y = x^4 at the point (1, 1) is", choices=[
   "y = 4x - 3", "y = 4x + 1", "y = 4x", "y = x + 3"], ans=0,
   why="The slope is 4(1)^3 = 4, so the point-slope form y - 1 = 4(x - 1) gives y = 4x - 3."),
 dict(q="The graph of y = x^3 has a horizontal tangent line at", choices=[
   "x = 0 only", "x = 1 only", "x = 0 and x = 1", "no value of x"], ans=0,
   why="dy/dx = 3x^2 equals 0 only at x = 0."),
 dict(q="For which of the following values of p is f(x) = x^p differentiable at x = 0?", choices=[
   "p = 4/3", "p = 2/3", "p = 1/3", "p = -1"], ans=0,
   why="f'(x) = (4/3)x^(1/3) is defined at 0, while the exponents 2/3 and 1/3 give derivatives that blow up there and x^(-1) is not even defined at 0."),
 dict(q="If f(x) = x^n for a positive integer n and f'(2) = 80, then n =", choices=[
   "4", "5", "6", "8"], ans=1,
   why="f'(2) = n 2^(n-1), and 5(2^4) = 5(16) = 80."),
 dict(q="If f(x) = x^(5/3), then f'(8) =", choices=[
   "4", "20/3", "40/3", "160/3"], ans=1,
   why="f'(x) = (5/3)x^(2/3), so f'(8) = (5/3)(4) = 20/3; 160/3 forgets to reduce the exponent."),
]
