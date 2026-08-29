# CALC 10.15 Representing Functions as Power Series — 25 questions
# Answers verified with sympy; see verify_c10_15.py
# Two directions, both tested here: turning a function into a power series
# (rewrite it as a geometric series, or differentiate/integrate one you know),
# and running the process backwards to evaluate a numerical series by
# recognizing it as a known power series at a particular value of x.
TOPIC = ("10.15", "Representing Functions as Power Series", 10)
QUESTIONS = [
 dict(q="To represent f(x) = 1/(3 - x) as a geometric series, the first step is to rewrite it as", choices=[
   "(1/3)*1/(1 - x/3)",
   "3*1/(1 - x/3)",
   "(1/3)*1/(1 + x/3)",
   "1/(1 - 3x)"], ans=0,
   why="Factoring 3 out of the denominator puts the expression in the form a/(1 - r) with r = x/3."),

 dict(q="For |x| < 3, the power series representation of 1/(3 - x) is", choices=[
   "sum from n=0 to infinity of x^n/3^n",
   "sum from n=0 to infinity of x^n/3^(n+1)",
   "sum from n=0 to infinity of 3^n*x^n",
   "sum from n=0 to infinity of (-1)^n*x^n/3^(n+1)"], ans=1,
   why="(1/3)*sum (x/3)^n = sum x^n/3^(n+1), and the ratio |x/3| must be less than 1."),

 dict(q="For |x| < 2, the power series representation of 1/(2 + x) is", choices=[
   "sum from n=0 to infinity of x^n/2^(n+1)",
   "sum from n=0 to infinity of (-1)^n*x^n/2^(n+1)",
   "sum from n=0 to infinity of (-1)^n*x^n/2^n",
   "sum from n=0 to infinity of (-1)^n*2^n*x^n"], ans=1,
   why="(1/2)*sum (-x/2)^n gives alternating signs and a 2^(n+1) in the denominator."),

 dict(q="The power series representation of 1/(1 + x^3) is", choices=[
   "sum from n=0 to infinity of (-1)^n*x^(3n)",
   "sum from n=0 to infinity of (-1)^n*x^(n+3)",
   "sum from n=0 to infinity of x^(3n)",
   "sum from n=0 to infinity of (-1)^n*x^(3n)/(3n)!"], ans=0,
   why="It is geometric with ratio -x^3."),

 dict(q="The series representation of 1/(1 + x^3) is valid exactly for", choices=[
   "|x| < 1",
   "|x| < 3",
   "|x| < 1/3",
   "all real x"], ans=0,
   why="The geometric series converges when |-x^3| < 1, that is |x| < 1."),

 dict(q="For |x| < 1, the power series representation of x/(1 - x) is", choices=[
   "sum from n=0 to infinity of x^n",
   "sum from n=0 to infinity of x^(n+1)",
   "sum from n=0 to infinity of n*x^n",
   "sum from n=1 to infinity of x^(n+1)"], ans=1,
   why="Multiplying the geometric series by x raises every exponent by 1."),

 dict(q="For |x| < 1, the power series representation of x^2/(1 - x) is", choices=[
   "sum from n=0 to infinity of x^(n+2)",
   "sum from n=0 to infinity of x^(2n)",
   "sum from n=2 to infinity of x^(n+2)",
   "sum from n=0 to infinity of n^2*x^n"], ans=0,
   why="Multiplying by x^2 raises every exponent by 2, so the series starts at x^2."),

 dict(q="Differentiating the series sum from n=0 to infinity of x^n term by term gives the representation, for |x| < 1, of", choices=[
   "1/(1 - x)^2, as sum from n=0 to infinity of (n+1)*x^n",
   "1/(1 - x)^2, as sum from n=0 to infinity of n*x^n",
   "-ln(1 - x), as sum from n=1 to infinity of x^n/n",
   "1/(1 - x), as sum from n=1 to infinity of n*x^(n-1)"], ans=0,
   why="The derivative of 1/(1-x) is 1/(1-x)^2, and differentiating x^n term by term and re-indexing gives (n+1)x^n."),

 dict(q="For |x| < 1, the power series representation of 1/(1 - x^2) is", choices=[
   "sum from n=0 to infinity of x^(2n)",
   "sum from n=0 to infinity of (-1)^n*x^(2n)",
   "sum from n=0 to infinity of x^n/2",
   "sum from n=0 to infinity of 2^n*x^n"], ans=0,
   why="It is geometric with ratio x^2, so only even powers appear and all signs are positive."),

 dict(q="For |x| < 1, the power series representation of x/(1 + x^2) is", choices=[
   "sum from n=0 to infinity of (-1)^n*x^(2n+1)",
   "sum from n=0 to infinity of (-1)^n*x^(2n)",
   "sum from n=0 to infinity of x^(2n+1)",
   "sum from n=0 to infinity of (-1)^n*x^(2n+1)/(2n+1)"], ans=0,
   why="Multiply the series for 1/(1 + x^2), which is sum (-1)^n*x^(2n), by x."),

 dict(q="The power series representation of 3/(1 - 2x), and the values of x for which it is valid, are", choices=[
   "sum from n=0 to infinity of 3*2^n*x^n, for |x| < 1/2",
   "sum from n=0 to infinity of 3*2^n*x^n, for |x| < 2",
   "sum from n=0 to infinity of 6^n*x^n, for |x| < 1/6",
   "sum from n=0 to infinity of 3*x^n/2^n, for |x| < 2"], ans=0,
   why="The ratio is 2x, so the coefficient is 3*2^n and convergence needs |2x| < 1."),

 dict(q="The radius of convergence of the power series representation of 1/(4 + x^2) is", choices=[
   "1",
   "2",
   "4",
   "16"], ans=1,
   why="Writing it as (1/4)*1/(1 + (x/2)^2) needs |x/2|^2 < 1, that is |x| < 2."),

 dict(q="Differentiating a power series term by term produces a series whose radius of convergence is", choices=[
   "the same as the original",
   "one less than the original",
   "half the original",
   "always infinite"], ans=0,
   why="Term-by-term differentiation preserves the radius of convergence, though the behavior at the endpoints may change."),

 dict(q="Integrating a power series term by term produces a series with", choices=[
   "a larger radius of convergence",
   "a smaller radius of convergence",
   "the same radius of convergence, though the endpoint behavior may differ",
   "the same interval of convergence, endpoints included"], ans=2,
   why="The radius is unchanged, but an endpoint that diverged before may converge afterward, as sum x^n and sum x^n/n show at x = -1."),

 dict(q="Integrating the series for 1/(1 + t) from 0 to x term by term gives the representation of", choices=[
   "ln(1 + x)",
   "ln(1 - x)",
   "1/(1 + x)^2",
   "arctan(x)"], ans=0,
   why="The integral of 1/(1+t) from 0 to x is ln(1 + x), and integrating 1 - t + t^2 - ... gives x - x^2/2 + x^3/3 - ..."),

 dict(q="Integrating the series for 1/(1 + t^2) from 0 to x term by term gives the representation of", choices=[
   "ln(1 + x^2)",
   "arctan(x)",
   "arcsin(x)",
   "x/(1 + x^2)"], ans=1,
   why="The integral of 1/(1+t^2) is arctan, and the resulting series is x - x^3/3 + x^5/5 - ..."),

 dict(q="A power series representation for int from 0 to x of e^(-t^2) dt is", choices=[
   "sum from n=0 to infinity of (-1)^n*x^(2n+1)/(n!*(2n+1))",
   "sum from n=0 to infinity of (-1)^n*x^(2n)/n!",
   "sum from n=0 to infinity of (-1)^n*x^(2n+1)/(2n+1)!",
   "sum from n=0 to infinity of x^(2n+1)/(n!*(2n+1))"], ans=0,
   why="Integrating sum (-1)^n*t^(2n)/n! term by term raises each exponent by 1 and divides by 2n + 1."),

 dict(q="A power series representation for int from 0 to x of (sin(t)/t) dt is", choices=[
   "sum from n=0 to infinity of (-1)^n*x^(2n+1)/((2n+1)*(2n+1)!)",
   "sum from n=0 to infinity of (-1)^n*x^(2n+1)/(2n+1)!",
   "sum from n=0 to infinity of (-1)^n*x^(2n)/(2n+1)!",
   "sum from n=0 to infinity of (-1)^n*x^(2n+2)/((2n+2)*(2n+1)!)"], ans=0,
   why="sin(t)/t is sum (-1)^n*t^(2n)/(2n+1)!, and integrating contributes an extra factor of 2n + 1 in the denominator."),

 dict(q="Using the representation sum from n=1 to infinity of n*x^n = x/(1 - x)^2, the value of sum from n=1 to infinity of n/2^n is", choices=[
   "1",
   "3/2",
   "2",
   "4"], ans=2,
   why="Substituting x = 1/2 gives (1/2)/(1/2)^2 = 2."),

 dict(q="Using the representation -ln(1 - x) = sum from n=1 to infinity of x^n/n, the value of sum from n=1 to infinity of 1/(n*2^n) is", choices=[
   "ln(2)",
   "ln(1/2)",
   "1/2",
   "2*ln(2)"], ans=0,
   why="Substituting x = 1/2 gives -ln(1/2) = ln(2)."),

 dict(q="Using the Maclaurin series for arctan(x), the value of sum from n=0 to infinity of (-1)^n/(2n+1) is", choices=[
   "pi/6",
   "pi/4",
   "pi/2",
   "1"], ans=1,
   why="It is the arctangent series evaluated at x = 1, and arctan(1) = pi/4."),

 dict(q="Using the Maclaurin series for ln(1 + x), the value of sum from n=1 to infinity of (-1)^(n+1)/n is", choices=[
   "ln(2)",
   "1",
   "pi/4",
   "the series diverges"], ans=0,
   why="It is the series for ln(1 + x) at x = 1, which converges to ln(2) by the alternating series test."),

 dict(q="Using a geometric series, the value of sum from n=0 to infinity of (-1)^n/3^n is", choices=[
   "1/2",
   "2/3",
   "3/4",
   "3/2"], ans=2,
   why="It is geometric with r = -1/3, so the sum is 1/(1 + 1/3) = 3/4."),

 dict(q="Using the Maclaurin series for e^x, the value of sum from n=0 to infinity of 1/n! is", choices=[
   "1",
   "e - 1",
   "e",
   "2"], ans=2,
   why="It is the series for e^x at x = 1, and the sum starts at n = 0, so no term is missing."),

 dict(q="Differentiating the geometric series twice gives sum from n=2 to infinity of n*(n-1)*x^n = 2x^2/(1 - x)^3. The value of sum from n=2 to infinity of n*(n-1)/2^n is", choices=[
   "2",
   "3",
   "4",
   "8"], ans=2,
   why="Substituting x = 1/2 gives 2*(1/4)/(1/2)^3 = (1/2)/(1/8) = 4."),
]
