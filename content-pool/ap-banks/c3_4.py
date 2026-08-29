# CALC 3.4 Differentiating Inverse Trigonometric Functions — 25 questions
# Every derivative is confirmed with sp.diff in verify_c3_4.py, which also
# checks that no distractor is equivalent to the key -- the real hazard here,
# since 1/(2 sqrt(x) sqrt(1 - x)) and 1/(2 sqrt(x - x^2)) are the same function.
# Questions 17, 18 and 19 are conceptual (why the arcsin and arccos derivatives
# are negatives, why the formula fails at x = 1, and the implicit derivation).
TOPIC = ("3.4", "Differentiating Inverse Trigonometric Functions", 3)
QUESTIONS = [
 dict(q="d/dx[arcsin(x)] =", choices=[
   "1/sqrt(1 - x^2)", "-1/sqrt(1 - x^2)", "1/(1 + x^2)", "1/sqrt(x^2 - 1)"], ans=0,
   why="The arcsine derivative has the radical 1 - x^2 underneath and no minus sign."),
 dict(q="d/dx[arccos(x)] =", choices=[
   "-1/sqrt(1 - x^2)", "1/sqrt(1 - x^2)", "-1/(1 + x^2)", "-1/sqrt(x^2 - 1)"], ans=0,
   why="Arccosine is decreasing on its domain, so its derivative is the negative of the arcsine derivative."),
 dict(q="d/dx[arctan(x)] =", choices=[
   "1/(1 + x^2)", "-1/(1 + x^2)", "1/sqrt(1 - x^2)", "1/(1 - x^2)"], ans=0,
   why="The arctangent derivative is rational, with 1 + x^2 in the denominator and no radical."),
 dict(q="d/dx[arccot(x)] =", choices=[
   "-1/(1 + x^2)", "1/(1 + x^2)", "-1/sqrt(1 - x^2)", "-1/(1 - x^2)"], ans=0,
   why="Like the other co-functions, arccotangent has a negative derivative."),
 dict(q="If f(x) = arcsin(2x), then f'(x) =", choices=[
   "2/sqrt(1 - 4x^2)", "1/sqrt(1 - 4x^2)", "2/sqrt(1 - x^2)", "-2/sqrt(1 - 4x^2)"], ans=0,
   why="The chain rule contributes the inner derivative 2, and the inside 2x is squared under the radical."),
 dict(q="If f(x) = arctan(3x), then f'(x) =", choices=[
   "3/(1 + 9x^2)", "1/(1 + 9x^2)", "3/(1 + 3x^2)", "3/(1 + x^2)"], ans=0,
   why="The inner derivative 3 multiplies, and (3x)^2 = 9x^2 sits in the denominator."),
 dict(q="If f(x) = arcsin(x^2), then f'(x) =", choices=[
   "2x/sqrt(1 - x^4)", "1/sqrt(1 - x^4)", "2x/sqrt(1 - x^2)", "-2x/sqrt(1 - x^4)"], ans=0,
   why="The inner derivative is 2x and (x^2)^2 = x^4 goes under the radical."),
 dict(q="If f(x) = arctan(x^2), then f'(x) =", choices=[
   "2x/(1 + x^4)", "1/(1 + x^4)", "2x/(1 + x^2)", "2x/(1 + x^4)^2"], ans=0,
   why="The inner derivative is 2x and the denominator is 1 + (x^2)^2."),
 dict(q="If f(x) = arccos(2x), then f'(x) =", choices=[
   "-2/sqrt(1 - 4x^2)", "2/sqrt(1 - 4x^2)", "-1/sqrt(1 - 4x^2)", "-2/sqrt(1 - x^2)"], ans=0,
   why="The arccosine minus sign and the chain rule factor 2 both appear."),
 dict(q="If f(x) = x arctan(x), then f'(x) =", choices=[
   "arctan(x) + x/(1 + x^2)",
   "arctan(x) + 1/(1 + x^2)",
   "x/(1 + x^2)",
   "1/(1 + x^2)"], ans=0,
   why="The product rule gives (1)(arctan x) + (x)(1/(1 + x^2))."),
 dict(q="If f(x) = e^(arctan(x)), then f'(x) =", choices=[
   "e^(arctan(x))/(1 + x^2)",
   "e^(arctan(x))",
   "e^(1/(1 + x^2))",
   "e^(arctan(x))/(1 + x^2)^2"], ans=0,
   why="The exponential is its own outer derivative, times the inner derivative 1/(1 + x^2)."),
 dict(q="If f(x) = arcsin(x), then f'(1/2) =", choices=[
   "sqrt(3)/2", "2/3", "2 sqrt(3)/3", "4/3"], ans=2,
   why="f'(1/2) = 1/sqrt(1 - 1/4) = 1/(sqrt(3)/2) = 2/sqrt(3) = 2 sqrt(3)/3."),
 dict(q="If f(x) = arctan(x), then f'(1) =", choices=[
   "1/4", "1/2", "1", "2"], ans=1,
   why="f'(1) = 1/(1 + 1) = 1/2."),
 dict(q="If f(x) = arccos(x), then f'(0) =", choices=[
   "-1", "-1/2", "0", "1"], ans=0,
   why="f'(0) = -1/sqrt(1 - 0) = -1."),
 dict(q="If f(x) = arcsin(x/3), then f'(x) =", choices=[
   "1/sqrt(9 - x^2)", "3/sqrt(9 - x^2)", "1/(3 sqrt(9 - x^2))", "1/sqrt(1 - x^2)"], ans=0,
   why="The chain rule gives (1/3)/sqrt(1 - x^2/9), and pulling 1/3 inside the radical leaves 1/sqrt(9 - x^2)."),
 dict(q="If f(x) = arctan(x/2), then f'(x) =", choices=[
   "2/(4 + x^2)", "1/(4 + x^2)", "1/(2(1 + x^2))", "2/(1 + x^2)"], ans=0,
   why="The chain rule gives (1/2)/(1 + x^2/4), and multiplying top and bottom by 4 gives 2/(4 + x^2)."),
 dict(q="Why are the derivatives of arcsin(x) and arccos(x) negatives of each other?", choices=[
   "Because arcsin(x) + arccos(x) = pi/2 for every x in [-1, 1], and the derivative of a constant is 0",
   "Because sine and cosine are negatives of each other",
   "Because arccos(x) = -arcsin(x)",
   "Because both functions are decreasing"], ans=0,
   why="Their sum is the constant pi/2, so their derivatives must sum to 0."),
 dict(q="The formula for d/dx[arcsin(x)] fails at x = 1 and x = -1 because", choices=[
   "sqrt(1 - x^2) is 0 there, and the graph of arcsin has a vertical tangent line at each endpoint",
   "arcsin(x) is undefined there",
   "arcsin(x) is not continuous there",
   "the derivative is 0 there"], ans=0,
   why="arcsin(1) = pi/2 is defined, but the tangent line is vertical, so no finite derivative exists."),
 dict(q="Setting y = arcsin(x) and differentiating sin(y) = x implicitly gives cos(y) dy/dx = 1. The next step uses which identity to reach 1/sqrt(1 - x^2)?", choices=[
   "cos(y) = sqrt(1 - sin^2(y)) = sqrt(1 - x^2), valid because cos(y) >= 0 on the range of arcsin",
   "cos(y) = 1 - sin(y)",
   "cos(y) = sqrt(1 + x^2)",
   "cos(y) = x"], ans=0,
   why="The range of arcsin is [-pi/2, pi/2], where cosine is not negative, so the positive square root is the right one."),
 dict(q="If f(x) = arcsin(sqrt(x)) for 0 < x < 1, then f'(x) =", choices=[
   "1/(2 sqrt(x - x^2))",
   "1/sqrt(1 - x)",
   "1/(2 sqrt(x))",
   "1/(2 sqrt(1 - x^2))"], ans=0,
   why="The chain rule gives (1/sqrt(1 - x))(1/(2 sqrt(x))), and combining the radicals gives 1/(2 sqrt(x - x^2))."),
 dict(q="If f(x) = arctan(e^x), then f'(x) =", choices=[
   "e^x/(1 + e^(2x))",
   "e^x/(1 + e^x)",
   "1/(1 + e^(2x))",
   "e^x/(1 + e^x)^2"], ans=0,
   why="The inner derivative is e^x and the denominator is 1 + (e^x)^2 = 1 + e^(2x)."),
 dict(q="If f(x) = (arctan(x))^2, then f'(x) =", choices=[
   "2 arctan(x)/(1 + x^2)",
   "2 arctan(x)",
   "2/(1 + x^2)",
   "(arctan(x))^2/(1 + x^2)"], ans=0,
   why="The outer power rule gives 2 arctan(x), times the inner derivative 1/(1 + x^2)."),
 dict(q="An equation of the line tangent to y = arctan(x) at x = 1 is", choices=[
   "y = (1/2)(x - 1) + pi/4",
   "y = 2(x - 1) + pi/4",
   "y = (1/2)(x - 1) + pi/2",
   "y = (1/2)x + pi/4"], ans=0,
   why="The slope is 1/(1 + 1) = 1/2 and arctan(1) = pi/4, so the line passes through (1, pi/4)."),
 dict(q="For -1 < x < 1, d/dx[arcsin(x) + arccos(x)] =", choices=[
   "0", "2/sqrt(1 - x^2)", "1", "2 arcsin(x)"], ans=0,
   why="The two derivatives are exact opposites, so they cancel; equivalently the sum is the constant pi/2."),
 dict(q="If f(x) = arcsec(x), then f'(2) =", choices=[
   "1/(4 sqrt(3))", "1/(2 sqrt(3))", "1/sqrt(3)", "2/sqrt(3)"], ans=1,
   why="f'(x) = 1/(|x| sqrt(x^2 - 1)), so f'(2) = 1/(2 sqrt(3))."),
]
