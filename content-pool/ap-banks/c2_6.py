# CALC 2.6 Derivative Rules: Constant, Sum, Difference, and Constant Multiple — 25 questions
# Every derivative is confirmed with sp.diff in verify_c2_6.py, which also
# checks that no distractor is equivalent to the key.
# Questions 2, 3 and 25 are conceptual (the statements of the rules, and the
# product "rule" that does not exist).
TOPIC = ("2.6", "Derivative Rules: Constant, Sum, Difference, and Constant Multiple", 2)
QUESTIONS = [
 dict(q="If f(x) = 7, then f'(x) =", choices=[
   "0", "1", "7", "7x"], ans=0,
   why="A constant function has zero rate of change everywhere."),
 dict(q="For a constant c and a differentiable function f, d/dx[c f(x)] =", choices=[
   "c f'(x)", "f'(x)", "c f(x)", "0"], ans=0,
   why="A constant multiple passes straight through the derivative."),
 dict(q="For differentiable functions f and g, d/dx[f(x) - g(x)] =", choices=[
   "f'(x) - g'(x)", "f'(x) g'(x)", "f'(x) - g(x)", "g'(x) - f'(x)"], ans=0,
   why="Derivatives distribute over sums and differences term by term."),
 dict(q="If f(x) = 3x^2 + 5x - 4, then f'(x) =", choices=[
   "6x + 5", "6x^2 + 5", "6x + 5 - 4", "3x^2 + 5"], ans=0,
   why="Differentiate term by term; the constant -4 contributes 0, not -4."),
 dict(q="If f(x) = 4x^3 - 2x, then f'(x) =", choices=[
   "12x^2 - 2", "12x^2 - 2x", "12x^3 - 2", "4x^2 - 2"], ans=0,
   why="The power rule gives 12x^2 for the first term and -2 for the linear term."),
 dict(q="If f(x) = 5 sqrt(x), then f'(x) =", choices=[
   "5/(2 sqrt(x))", "5 sqrt(x)/2", "1/(2 sqrt(x))", "10 sqrt(x)"], ans=0,
   why="The constant 5 stays in front of the derivative of x^(1/2), which is 1/(2 sqrt(x))."),
 dict(q="If f(x) = x^4/2 - 3/x, then f'(x) =", choices=[
   "2x^3 + 3/x^2", "2x^3 - 3/x^2", "2x^3 + 3/x", "4x^3 + 3/x^2"], ans=0,
   why="Rewrite -3/x as -3x^(-1), whose derivative is 3x^(-2) = +3/x^2; the sign flips because the exponent is negative."),
 dict(q="If f(x) = (2x^3 - x)/x for x not 0, then f'(x) =", choices=[
   "4x", "6x^2 - 1", "4x - 1", "2x"], ans=0,
   why="Simplify to 2x^2 - 1 first, so f'(x) = 4x; differentiating numerator and denominator separately gives the wrong 6x^2 - 1."),
 dict(q="If f(x) = (x^2 + 3)(x - 1), then f'(x) =", choices=[
   "3x^2 - 2x + 3", "2x", "3x^2 + 3", "2x^2 - 2x + 3"], ans=0,
   why="Expand to x^3 - x^2 + 3x - 3 and differentiate term by term; multiplying the separate derivatives 2x and 1 is not a valid rule."),
 dict(q="If f(x) = 6x^5 - 3x^2 + 9, then f'(1) =", choices=[
   "12", "24", "30", "36"], ans=1,
   why="f'(x) = 30x^4 - 6x, so f'(1) = 30 - 6 = 24; the constant 9 contributes nothing."),
 dict(q="If f(x) = 2x^3 + x, then f'(2) =", choices=[
   "13", "24", "25", "49"], ans=2,
   why="f'(x) = 6x^2 + 1, so f'(2) = 24 + 1 = 25."),
 dict(q="If f'(3) = 5 and g'(3) = -2, then the derivative of 3f(x) - 2g(x) at x = 3 is", choices=[
   "7", "11", "19", "23"], ans=2,
   why="3(5) - 2(-2) = 15 + 4 = 19; the sign of g'(3) must be carried through the subtraction."),
 dict(q="If f is differentiable with f'(2) = 4, then the derivative of 5f(x) at x = 2 is", choices=[
   "4", "5", "9", "20"], ans=3,
   why="The constant multiple rule gives 5 f'(2) = 5(4) = 20."),
 dict(q="If h(x) = f(x) + 7 for a differentiable function f, then h'(x) =", choices=[
   "f'(x)", "f'(x) + 7", "f'(x) + 1", "7 f'(x)"], ans=0,
   why="Adding a constant shifts the graph vertically and leaves every slope unchanged."),
 dict(q="If f(x) = pi^2, then f'(x) =", choices=[
   "0", "pi^2", "2 pi", "2 pi x"], ans=0,
   why="pi^2 is a number, not a function of x, so its derivative is 0."),
 dict(q="If f(x) = x^2/3 + 3/x^2, then f'(x) =", choices=[
   "2x/3 - 6/x^3", "2x/3 + 6/x^3", "2x/3 - 6/x", "x/3 - 6/x^3"], ans=0,
   why="The first term gives 2x/3, and 3x^(-2) differentiates to -6x^(-3) = -6/x^3."),
 dict(q="The slope of the line tangent to y = 2x^3 - 6x at the point where x = 1 is", choices=[
   "-6", "0", "6", "12"], ans=1,
   why="dy/dx = 6x^2 - 6, which is 0 at x = 1, so the tangent line there is horizontal."),
 dict(q="The graph of y = x^3 - 3x has a horizontal tangent line at", choices=[
   "x = -1 and x = 1", "x = 0 only", "x = 3 only", "no value of x"], ans=0,
   why="3x^2 - 3 = 0 gives x^2 = 1, so x = -1 and x = 1."),
 dict(q="If f(x) = (x + 1)^2, then f'(x) =", choices=[
   "2x + 2", "2x", "2(x + 1)^2", "x^2 + 2x"], ans=0,
   why="Expand to x^2 + 2x + 1 and differentiate term by term."),
 dict(q="For constants a, b and c, if f(x) = ax^2 + bx + c then f'(x) =", choices=[
   "2ax + b", "2ax + b + c", "ax + b", "2ax"], ans=0,
   why="Each constant coefficient passes through the derivative and the constant term c contributes 0."),
 dict(q="If f(x) = x^3 + kx for a constant k and f'(1) = 7, then k =", choices=[
   "1", "3", "4", "7"], ans=2,
   why="f'(x) = 3x^2 + k, so f'(1) = 3 + k = 7 and k = 4."),
 dict(q="The curve y = ax^2 + bx passes through (1, 3) and has slope 5 there. The constants a and b are", choices=[
   "a = 2, b = 1",
   "a = 1, b = 2",
   "a = 3, b = 0",
   "a = 5, b = -2"], ans=0,
   why="The point gives a + b = 3 and the slope gives 2a + b = 5, so a = 2 and b = 1."),
 dict(q="If f(x) = 2 sqrt(x) - 3/sqrt(x), then f'(x) =", choices=[
   "1/sqrt(x) + 3/(2x^(3/2))",
   "1/sqrt(x) - 3/(2x^(3/2))",
   "2/sqrt(x) + 3/(2x^(3/2))",
   "1/(2 sqrt(x)) + 3/(2x^(3/2))"], ans=0,
   why="Write the terms as 2x^(1/2) - 3x^(-1/2); the second differentiates to (3/2)x^(-3/2), which is positive."),
 dict(q="For f(x) = x^3 - 6x^2 + 9x + 1, the values of x at which f'(x) = 0 are", choices=[
   "x = 1 and x = 3", "x = 3 only", "x = 0 and x = 2", "x = -1 and x = -3"], ans=0,
   why="f'(x) = 3x^2 - 12x + 9 = 3(x - 1)(x - 3), which vanishes at x = 1 and x = 3."),
 dict(q="Which of the following is NOT a valid derivative rule?", choices=[
   "d/dx[f(x) g(x)] = f'(x) g'(x)",
   "d/dx[f(x) + g(x)] = f'(x) + g'(x)",
   "d/dx[c f(x)] = c f'(x)",
   "d/dx[c] = 0"], ans=0,
   why="Derivatives distribute over sums and constant multiples but not over products; f(x) = g(x) = x already breaks the first statement."),
]
