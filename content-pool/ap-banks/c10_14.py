# CALC 10.14 Finding Taylor or Maclaurin Series for a Function — 25 questions
# Answers verified with sympy; see verify_c10_14.py
# The five series a BC student is expected to know cold -- e^x, sin x, cos x,
# 1/(1-x) and ln(1+x) -- and the four ways new ones are built from them:
# substitution, multiplication by a power of x, differentiation, integration.
TOPIC = ("10.14", "Finding Taylor or Maclaurin Series for a Function", 10)
QUESTIONS = [
 dict(q="The Maclaurin series for e^x is", choices=[
   "sum from n=0 to infinity of x^n/n!",
   "sum from n=0 to infinity of x^n",
   "sum from n=1 to infinity of x^n/n",
   "sum from n=0 to infinity of (-1)^n*x^n/n!"], ans=0,
   why="Every derivative of e^x equals 1 at 0, so the coefficient of x^n is 1/n!."),

 dict(q="The Maclaurin series for sin(x) is", choices=[
   "sum from n=0 to infinity of (-1)^n*x^(2n)/(2n)!",
   "sum from n=0 to infinity of (-1)^n*x^(2n+1)/(2n+1)!",
   "sum from n=0 to infinity of x^(2n+1)/(2n+1)!",
   "sum from n=0 to infinity of (-1)^n*x^n/n!"], ans=1,
   why="sin is odd, so only odd powers appear, with alternating signs and factorials of the exponent."),

 dict(q="The Maclaurin series for cos(x) is", choices=[
   "sum from n=0 to infinity of (-1)^n*x^(2n)/(2n)!",
   "sum from n=0 to infinity of (-1)^n*x^(2n+1)/(2n+1)!",
   "sum from n=0 to infinity of x^(2n)/(2n)!",
   "sum from n=0 to infinity of (-1)^n*x^n/(2n)!"], ans=0,
   why="cos is even, so only even powers appear, with alternating signs."),

 dict(q="For |x| < 1, the Maclaurin series for 1/(1 - x) is", choices=[
   "sum from n=0 to infinity of x^n",
   "sum from n=0 to infinity of (-1)^n*x^n",
   "sum from n=1 to infinity of x^n/n",
   "sum from n=0 to infinity of x^n/n!"], ans=0,
   why="This is the geometric series with first term 1 and ratio x."),

 dict(q="For |x| < 1, the Maclaurin series for ln(1 + x) is", choices=[
   "sum from n=1 to infinity of x^n/n",
   "sum from n=1 to infinity of (-1)^(n+1)*x^n/n",
   "sum from n=0 to infinity of (-1)^n*x^n/n!",
   "sum from n=1 to infinity of (-1)^n*x^n/n!"], ans=1,
   why="Integrating 1 - x + x^2 - ... term by term gives x - x^2/2 + x^3/3 - ..."),

 dict(q="The Maclaurin series for e^(-x) is", choices=[
   "sum from n=0 to infinity of x^n/n!",
   "sum from n=0 to infinity of (-1)^n*x^n/n!",
   "sum from n=0 to infinity of (-x)^n/(-n)!",
   "-sum from n=0 to infinity of x^n/n!"], ans=1,
   why="Substituting -x into sum x^n/n! attaches (-1)^n to each term."),

 dict(q="The Maclaurin series for e^(x^2) is", choices=[
   "sum from n=0 to infinity of x^(2n)/n!",
   "sum from n=0 to infinity of x^(2n)/(2n)!",
   "sum from n=0 to infinity of x^n/(2n)!",
   "sum from n=0 to infinity of x^(n^2)/n!"], ans=0,
   why="Substituting x^2 for x replaces x^n by x^(2n) and leaves the n! alone."),

 dict(q="The Maclaurin series for sin(x^2) is", choices=[
   "sum from n=0 to infinity of (-1)^n*x^(2n+1)/(2n+1)!",
   "sum from n=0 to infinity of (-1)^n*x^(4n+2)/(2n+1)!",
   "sum from n=0 to infinity of (-1)^n*x^(4n+2)/(4n+2)!",
   "sum from n=0 to infinity of (-1)^n*x^(2n+1)/(4n+2)!"], ans=1,
   why="Replacing x by x^2 turns x^(2n+1) into x^(4n+2) while the factorial keeps its old index."),

 dict(q="For |x| < 1, the Maclaurin series for 1/(1 + x) is", choices=[
   "sum from n=0 to infinity of x^n",
   "sum from n=0 to infinity of (-1)^n*x^n",
   "sum from n=1 to infinity of (-1)^n*x^n/n",
   "sum from n=0 to infinity of (-1)^(n+1)*x^n"], ans=1,
   why="It is the geometric series with ratio -x."),

 dict(q="For |x| < 1/2, the Maclaurin series for 1/(1 - 2x) is", choices=[
   "sum from n=0 to infinity of 2^n*x^n",
   "sum from n=0 to infinity of 2*x^n",
   "sum from n=0 to infinity of x^n/2^n",
   "sum from n=0 to infinity of (2x)^n/n!"], ans=0,
   why="It is geometric with ratio 2x, so the nth term is (2x)^n = 2^n*x^n."),

 dict(q="The Maclaurin series for x*e^x is", choices=[
   "sum from n=0 to infinity of x^(n+1)/n!",
   "sum from n=0 to infinity of x^n/n!",
   "sum from n=0 to infinity of x^(n+1)/(n+1)!",
   "sum from n=0 to infinity of x^(2n)/n!"], ans=0,
   why="Multiplying the series for e^x by x raises every exponent by 1 and leaves the factorials alone."),

 dict(q="Differentiating the Maclaurin series for sin(x) term by term gives the series for", choices=[
   "cos(x)",
   "-cos(x)",
   "-sin(x)",
   "e^x"], ans=0,
   why="A power series may be differentiated term by term inside its interval of convergence, and the derivative of sin is cos."),

 dict(q="The Maclaurin series for arctan(x), obtained by integrating the series for 1/(1 + x^2), is", choices=[
   "sum from n=0 to infinity of (-1)^n*x^(2n+1)/(2n+1)",
   "sum from n=0 to infinity of (-1)^n*x^(2n+1)/(2n+1)!",
   "sum from n=0 to infinity of (-1)^n*x^(2n)/(2n+1)",
   "sum from n=0 to infinity of x^(2n+1)/(2n+1)"], ans=0,
   why="Integrating 1 - x^2 + x^4 - ... gives x - x^3/3 + x^5/5 - ..., with no factorials."),

 dict(q="The Maclaurin series for cos(2x) is", choices=[
   "sum from n=0 to infinity of (-1)^n*4^n*x^(2n)/(2n)!",
   "sum from n=0 to infinity of (-1)^n*2^n*x^(2n)/(2n)!",
   "sum from n=0 to infinity of (-1)^n*x^(2n)/(2n)!",
   "2*sum from n=0 to infinity of (-1)^n*x^(2n)/(2n)!"], ans=0,
   why="Substituting 2x gives (2x)^(2n) = 4^n*x^(2n)."),

 dict(q="The Taylor series for e^x about x = 1 is", choices=[
   "sum from n=0 to infinity of (x - 1)^n/n!",
   "sum from n=0 to infinity of e*(x - 1)^n/n!",
   "sum from n=0 to infinity of e^n*(x - 1)^n/n!",
   "sum from n=0 to infinity of e*(x - 1)^n"], ans=1,
   why="Every derivative equals e at x = 1, so each coefficient is e/n!."),

 dict(q="The Taylor series for 1/x about x = 1 is", choices=[
   "sum from n=0 to infinity of (x - 1)^n",
   "sum from n=0 to infinity of (-1)^n*(x - 1)^n",
   "sum from n=0 to infinity of (-1)^n*(x - 1)^n/n!",
   "sum from n=1 to infinity of (-1)^n*(x - 1)^n/n"], ans=1,
   why="Writing 1/x = 1/(1 + (x-1)) makes it geometric with ratio -(x - 1)."),

 dict(q="The first three nonzero terms of the Maclaurin series for e^x*cos(x) are", choices=[
   "1 + x + x^2/2",
   "1 + x - x^3/3",
   "1 + x + x^2",
   "1 - x^2/2 + x^4/24"], ans=1,
   why="The x^2 terms cancel: (1 + x + x^2/2 + x^3/6)(1 - x^2/2) = 1 + x + 0*x^2 - x^3/3 + ..."),

 dict(q="The Maclaurin series for x^2*sin(x) is", choices=[
   "sum from n=0 to infinity of (-1)^n*x^(2n+3)/(2n+1)!",
   "sum from n=0 to infinity of (-1)^n*x^(2n+1)/(2n+3)!",
   "sum from n=0 to infinity of (-1)^n*x^(2n+3)/(2n+3)!",
   "sum from n=0 to infinity of (-1)^n*x^(2n+2)/(2n+1)!"], ans=0,
   why="Multiplying by x^2 raises every exponent by 2 and changes nothing else."),

 dict(q="In the Maclaurin series for sin(x), the coefficient of x^5 is", choices=[
   "1/5",
   "1/24",
   "1/120",
   "-1/120"], ans=2,
   why="The x^5 term is (-1)^2*x^5/5! = x^5/120, so the coefficient is positive."),

 dict(q="For |x| < 1, the Maclaurin series for ln(1 - x) is", choices=[
   "sum from n=1 to infinity of x^n/n",
   "-sum from n=1 to infinity of x^n/n",
   "sum from n=1 to infinity of (-1)^n*x^n/n",
   "sum from n=0 to infinity of x^n/n!"], ans=1,
   why="Substituting -x into ln(1 + x) = x - x^2/2 + ... gives -x - x^2/2 - x^3/3 - ..."),

 dict(q="Integrating the series sum from n=0 to infinity of x^n term by term, with constant of integration 0, gives the series for", choices=[
   "1/(1 - x)^2",
   "-ln(1 - x)",
   "ln(1 + x)",
   "e^x"], ans=1,
   why="Term-by-term integration gives x + x^2/2 + x^3/3 + ..., which is -ln(1 - x)."),

 dict(q="Using Maclaurin series, lim as x -> 0 of (sin(x) - x)/x^3 equals", choices=[
   "0",
   "-1/6",
   "1/6",
   "-1"], ans=1,
   why="sin(x) - x = -x^3/6 + x^5/120 - ..., so dividing by x^3 leaves -1/6 in the limit."),

 dict(q="The Taylor series for f about x = a is", choices=[
   "sum from n=0 to infinity of f^(n)(a)*(x - a)^n/n!",
   "sum from n=0 to infinity of f^(n)(x)*(x - a)^n/n!",
   "sum from n=0 to infinity of f^(n)(a)*x^n/n!",
   "sum from n=0 to infinity of f(a)*(x - a)^n/n!"], ans=0,
   why="Each coefficient is the nth derivative at the center divided by n factorial."),

 dict(q="For |x| < 1, the Maclaurin series for 1/(1 + x^2) is", choices=[
   "sum from n=0 to infinity of (-1)^n*x^(2n)",
   "sum from n=0 to infinity of (-1)^n*x^n",
   "sum from n=0 to infinity of x^(2n)",
   "sum from n=0 to infinity of (-1)^n*x^(2n)/(2n)!"], ans=0,
   why="It is geometric with ratio -x^2."),

 dict(q="The first three terms of the Maclaurin series for e^x/(1 - x) are", choices=[
   "1 + x + x^2/2",
   "1 + 2x + 5x^2/2",
   "1 + 2x + 2x^2",
   "1 + x + 3x^2/2"], ans=1,
   why="Multiplying (1 + x + x^2/2 + ...) by (1 + x + x^2 + ...) gives 1, then 1 + 1 = 2, then 1 + 1 + 1/2 = 5/2."),
]
