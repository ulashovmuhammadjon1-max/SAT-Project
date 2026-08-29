# CALC 2.9 The Quotient Rule — 25 questions
# Every derivative is confirmed with sp.diff in verify_c2_9.py, which also
# checks that no distractor is equivalent to the key. The table of values is
# read by the verifier from this file.
# Questions 1, 2 and 16 are conceptual (the statement of the rule, the
# reversed-numerator error, and when the rule is actually needed).
TOPIC = ("2.9", "The Quotient Rule", 2)

# Values of two differentiable functions and their derivatives.
TAB = dict(
    headers=["x", "f(x)", "f'(x)", "g(x)", "g'(x)"],
    rows=[["1", "2", "3", "4", "-1"],
          ["2", "6", "-2", "3", "4"],
          ["3", "-4", "1", "2", "5"]],
)

QUESTIONS = [
 dict(q="For differentiable functions f and g with g(x) not 0, d/dx[f(x)/g(x)] =", choices=[
   "(f'(x) g(x) - f(x) g'(x))/(g(x))^2",
   "(f(x) g'(x) - f'(x) g(x))/(g(x))^2",
   "(f'(x) g(x) - f(x) g'(x))/g(x)",
   "f'(x)/g'(x)"], ans=0,
   why="The numerator starts with the derivative of the top times the bottom, and the whole denominator is squared."),
 dict(q="A student differentiates f(x)/g(x) and writes (f(x) g'(x) - f'(x) g(x))/(g(x))^2. What is wrong?", choices=[
   "The two terms in the numerator are in the wrong order, so the result is the negative of the correct derivative",
   "The denominator should not be squared",
   "The numerator should be a sum, not a difference",
   "Nothing is wrong"], ans=0,
   why="Swapping the two products negates the numerator, so every answer comes out with the wrong sign."),
 dict(q="If f(x) = x/(x + 1), then f'(x) =", choices=[
   "1/(x + 1)^2", "-1/(x + 1)^2", "1/(x + 1)", "1"], ans=0,
   why="(1)(x + 1) - (x)(1) = 1, over (x + 1)^2; the second choice comes from reversing the numerator."),
 dict(q="If f(x) = x^2/(x - 1), then f'(x) =", choices=[
   "(x^2 - 2x)/(x - 1)^2",
   "(2x - x^2)/(x - 1)^2",
   "(x^2 - 2x)/(x - 1)",
   "2x"], ans=0,
   why="(2x)(x - 1) - (x^2)(1) = x^2 - 2x, over (x - 1)^2."),
 dict(q="If f(x) = sin(x)/x, then f'(x) =", choices=[
   "(x cos(x) - sin(x))/x^2",
   "(sin(x) - x cos(x))/x^2",
   "(x cos(x) - sin(x))/x",
   "cos(x)"], ans=0,
   why="(cos x)(x) - (sin x)(1) = x cos(x) - sin(x), over x^2; the last choice divides the derivatives."),
 dict(q="If f(x) = e^x/x, then f'(x) =", choices=[
   "(x e^x - e^x)/x^2",
   "(e^x - x e^x)/x^2",
   "(x e^x - e^x)/x",
   "e^x"], ans=0,
   why="(e^x)(x) - (e^x)(1) = x e^x - e^x, over x^2."),
 dict(q="If f(x) = ln(x)/x, then f'(x) =", choices=[
   "(1 - ln(x))/x^2",
   "(ln(x) - 1)/x^2",
   "1/x^2",
   "(1 - ln(x))/x"], ans=0,
   why="(1/x)(x) - (ln x)(1) = 1 - ln(x), over x^2."),
 dict(q="If f(x) = (3x + 1)/(2x - 5), then f'(x) =", choices=[
   "-17/(2x - 5)^2", "17/(2x - 5)^2", "3/2", "-17/(2x - 5)"], ans=0,
   why="(3)(2x - 5) - (3x + 1)(2) = 6x - 15 - 6x - 2 = -17, over (2x - 5)^2."),
 dict(q="If f(x) = 1/(x^2 + 1), then f'(x) =", choices=[
   "-2x/(x^2 + 1)^2", "2x/(x^2 + 1)^2", "-2x/(x^2 + 1)", "-1/(2x)"], ans=0,
   why="(0)(x^2 + 1) - (1)(2x) = -2x, over (x^2 + 1)^2."),
 dict(q="If f(x) = (x^2 + 1)/(x^2 - 1), then f'(x) =", choices=[
   "-4x/(x^2 - 1)^2", "4x/(x^2 - 1)^2", "-4x/(x^2 - 1)", "1"], ans=0,
   why="(2x)(x^2 - 1) - (x^2 + 1)(2x) = -4x, over (x^2 - 1)^2."),
 dict(q="The table gives values of f, f', g and g'. If h(x) = f(x)/g(x), then h'(2) =", table=TAB, choices=[
   "-10/3", "-10/9", "-2/3", "10/3"], ans=0,
   why="h'(2) = ((-2)(3) - (6)(4))/3^2 = -30/9 = -10/3."),
 dict(q="If f(x) = cos(x)/x^2, then f'(x) =", choices=[
   "(-x sin(x) - 2 cos(x))/x^3",
   "(-x sin(x) + 2 cos(x))/x^3",
   "(x sin(x) - 2 cos(x))/x^3",
   "-sin(x)/(2x)"], ans=0,
   why="(-sin x)(x^2) - (cos x)(2x) = -x^2 sin(x) - 2x cos(x), and dividing by x^4 cancels one factor of x."),
 dict(q="If f(x) = x/(x + 1), then f'(1) =", choices=[
   "1/4", "1/2", "1", "2"], ans=0,
   why="f'(x) = 1/(x + 1)^2, so f'(1) = 1/4."),
 dict(q="If f(x) = 2x/(x^2 + 1), then f'(0) =", choices=[
   "-2", "0", "1", "2"], ans=3,
   why="f'(x) = (2 - 2x^2)/(x^2 + 1)^2, so f'(0) = 2/1 = 2."),
 dict(q="If f(x) = 5/x^3, then f'(x) =", choices=[
   "-15/x^4", "15/x^4", "-15/x^2", "-5/(3x^2)"], ans=0,
   why="Rewriting as 5x^(-3) and using the power rule is faster than the quotient rule, and gives -15x^(-4)."),
 dict(q="For which of the following is the quotient rule genuinely needed, with no simpler route?", choices=[
   "y = sin(x)/x",
   "y = (x^3 + x)/x",
   "y = 5/x^2",
   "y = (x^2 - 9)/(x - 3)"], ans=0,
   why="The other three simplify first to x^2 + 1, 5x^(-2) and x + 3; sin(x)/x does not simplify."),
 dict(q="If f(x) = (x^3 - 8)/(x - 2) for x not 2, then f'(x) =", choices=[
   "2x + 2", "2x + 4", "3x^2", "2x"], ans=0,
   why="Factoring gives f(x) = x^2 + 2x + 4 for x not 2, so f'(x) = 2x + 2; the quotient rule gives the same thing with much more work."),
 dict(q="The graph of y = x/(x^2 + 1) has a horizontal tangent line at", choices=[
   "x = -1 and x = 1", "x = 0 only", "x = 1 only", "no value of x"], ans=0,
   why="dy/dx = (1 - x^2)/(x^2 + 1)^2, and the numerator is 0 at x = -1 and x = 1."),
 dict(q="If f(x) = e^x/(1 + e^x), then f'(x) =", choices=[
   "e^x/(1 + e^x)^2",
   "e^x/(1 + e^x)",
   "-e^x/(1 + e^x)^2",
   "1/(1 + e^x)^2"], ans=0,
   why="(e^x)(1 + e^x) - (e^x)(e^x) = e^x, over (1 + e^x)^2."),
 dict(q="Using the table, if h(x) = f(x)/x^2, then h'(2) =", table=TAB, choices=[
   "-2", "-1/2", "1/2", "2"], ans=0,
   why="h'(2) = (f'(2)(4) - f(2)(4))/16 = ((-2)(4) - (6)(4))/16 = -32/16 = -2."),
 dict(q="The slope of the line tangent to y = (x^2 - 4)/(x + 2) at x = 1 is", choices=[
   "0", "1", "2", "1/3"], ans=1,
   why="For x not -2 the expression simplifies to x - 2, a line of slope 1, so the tangent slope is 1 at every such point."),
 dict(q="If f(x) = sqrt(x)/(x + 1), then f'(x) =", choices=[
   "(1 - x)/(2 sqrt(x) (x + 1)^2)",
   "(x - 1)/(2 sqrt(x) (x + 1)^2)",
   "(1 - x)/(2 sqrt(x) (x + 1))",
   "1/(2 sqrt(x) (x + 1)^2)"], ans=0,
   why="The numerator is (x + 1)/(2 sqrt(x)) - sqrt(x) = (1 - x)/(2 sqrt(x)), all over (x + 1)^2."),
 dict(q="If f(x) = (x + 2)/x^2, then f'(x) =", choices=[
   "-1/x^2 - 4/x^3",
   "1/x^2 + 4/x^3",
   "-1/x^2 + 4/x^3",
   "1/(2x)"], ans=0,
   why="Split into x^(-1) + 2x^(-2) and differentiate: -x^(-2) - 4x^(-3)."),
 dict(q="Using the table, if h(x) = g(x)/f(x), then h'(3) =", table=TAB, choices=[
   "-11/8", "-7/8", "-11/4", "11/8"], ans=0,
   why="h'(3) = (g'(3)f(3) - g(3)f'(3))/(f(3))^2 = ((5)(-4) - (2)(1))/16 = -22/16 = -11/8."),
 dict(q="Using the table, if h(x) = f(x)/g(x), then h'(1) =", table=TAB, choices=[
   "-7/8", "5/8", "7/8", "7/4"], ans=2,
   why="h'(1) = ((3)(4) - (2)(-1))/4^2 = 14/16 = 7/8."),
]
