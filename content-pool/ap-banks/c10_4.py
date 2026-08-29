# CALC 10.4 Integral Test for Convergence — 25 questions
# Answers verified with sympy; see verify_c10_4.py
# Two things the topic must not let slide: the three hypotheses (positive,
# continuous, DECREASING on [k, infinity)) are checked before the test is used,
# and the value of the improper integral is NOT the sum of the series.
TOPIC = ("10.4", "Integral Test for Convergence", 10)
QUESTIONS = [
 dict(q="The integral test may be applied to sum from n=k to infinity of a_n provided that a_n = f(n) where f is", choices=[
   "positive, continuous, and decreasing on [k, infinity)",
   "positive and continuous on [k, infinity)",
   "continuous and increasing on [k, infinity)",
   "differentiable on [k, infinity) with lim as x -> infinity of f(x) = 0"], ans=0,
   why="All three hypotheses -- positive, continuous, and decreasing -- are required for the comparison with the improper integral to work."),

 dict(q="For which of the following series does the integral test NOT apply directly?", choices=[
   "sum from n=1 to infinity of 1/(n^2 + 1)",
   "sum from n=1 to infinity of (-1)^n/n",
   "sum from n=1 to infinity of n*e^(-n)",
   "sum from n=2 to infinity of 1/(n*ln(n))"], ans=1,
   why="The terms of the alternating series are not positive, so the first hypothesis of the integral test fails."),

 dict(q="Because int from 1 to infinity of (1/x^2) dx converges, the integral test shows that sum from n=1 to infinity of 1/n^2", choices=[
   "converges",
   "diverges",
   "converges to 1",
   "converges only if the terms are decreasing"], ans=0,
   why="A convergent improper integral of a positive decreasing function forces the corresponding series to converge."),

 dict(q="int from 1 to infinity of (1/x^2) dx = 1. It follows that sum from n=1 to infinity of 1/n^2", choices=[
   "equals 1",
   "equals 1/2",
   "converges, but the integral's value is not the sum",
   "diverges"], ans=2,
   why="The integral test decides convergence only; the actual sum is pi^2/6, which is about 1.645, not 1."),

 dict(q="sum from n=2 to infinity of 1/(n*ln(n))", choices=[
   "converges, because int from 2 to infinity of dx/(x*ln(x)) converges",
   "diverges, because int from 2 to infinity of dx/(x*ln(x)) diverges",
   "converges, because the terms approach 0",
   "diverges, because the terms do not approach 0"], ans=1,
   why="The substitution u = ln(x) gives ln(ln(x)), which increases without bound, so both the integral and the series diverge."),

 dict(q="sum from n=2 to infinity of 1/(n*(ln(n))^2)", choices=[
   "converges",
   "diverges",
   "converges to 1/ln(2)",
   "the integral test does not apply"], ans=0,
   why="The substitution u = ln(x) gives an integral equal to 1/ln(2), which is finite, so the series converges (though not to that value)."),

 dict(q="sum from n=1 to infinity of n*e^(-n^2)", choices=[
   "converges",
   "diverges",
   "converges to 1/(2e)",
   "the integral test does not apply, since the terms are not decreasing"], ans=0,
   why="int from 1 to infinity of x*e^(-x^2) dx = 1/(2e) is finite, so the series converges; the integral's value is not the sum."),

 dict(q="The integral test applied to sum from n=1 to infinity of 1/(n^2 + 1) uses the improper integral whose value is", choices=[
   "pi/4",
   "pi/2",
   "1",
   "infinity"], ans=0,
   why="int from 1 to infinity of dx/(x^2 + 1) = pi/2 - pi/4 = pi/4, so the series converges."),

 dict(q="sum from n=1 to infinity of n/(n^2 + 1)", choices=[
   "converges, since the terms approach 0",
   "converges to 1/2",
   "diverges, since int from 1 to infinity of x/(x^2 + 1) dx diverges",
   "the integral test does not apply"], ans=2,
   why="The antiderivative (1/2)ln(x^2 + 1) grows without bound, so the integral and therefore the series diverge."),

 dict(q="sum from n=1 to infinity of 1/sqrt(n)", choices=[
   "converges, since int from 1 to infinity of x^(-1/2) dx = 2",
   "converges, since the terms approach 0",
   "diverges, since int from 1 to infinity of x^(-1/2) dx diverges",
   "the integral test is inconclusive here"], ans=2,
   why="int x^(-1/2) dx = 2*sqrt(x), which is unbounded, so the integral and the series both diverge."),

 dict(q="sum from n=2 to infinity of ln(n)/n", choices=[
   "converges",
   "diverges",
   "converges to (ln(2))^2/2",
   "the integral test does not apply because ln(x)/x is not positive"], ans=1,
   why="int ln(x)/x dx = (ln(x))^2/2, which increases without bound, so the series diverges."),

 dict(q="On which interval is f(x) = x/(x^2 + 1) decreasing, so that the integral test may be used on the corresponding series?", choices=[
   "x > 0",
   "x >= 1",
   "x >= 2",
   "f is increasing everywhere"], ans=1,
   why="f'(x) = (1 - x^2)/(x^2 + 1)^2 is negative for x > 1 and zero at x = 1, so f decreases on [1, infinity)."),

 dict(q="For the series sum from n=2 to infinity of ln(n)/n, the smallest integer k for which f(x) = ln(x)/x is decreasing on [k, infinity) is", choices=[
   "1",
   "2",
   "3",
   "4"], ans=2,
   why="f'(x) = (1 - ln(x))/x^2 is negative for x > e, and the smallest integer greater than e is 3."),

 dict(q="For sum from n=1 to infinity of 1/n^2, the integral test remainder bound gives R_10 = S - S_10 is at most", choices=[
   "1/100",
   "1/10",
   "1/2",
   "1"], ans=1,
   why="R_10 <= int from 10 to infinity of dx/x^2 = 1/10."),

 dict(q="For sum from n=1 to infinity of 1/n^3, the integral test bounds the remainder R_5 = S - S_5 by", choices=[
   "1/125",
   "1/50",
   "1/25",
   "1/5"], ans=1,
   why="R_5 <= int from 5 to infinity of x^(-3) dx = 1/(2*25) = 1/50."),

 dict(q="If f is positive, continuous, and decreasing with a_n = f(n) and S is the sum of the convergent series, then the integral test gives", choices=[
   "S_n + int from n to infinity of f(x) dx <= S <= S_n + int from (n+1) to infinity of f(x) dx",
   "S_n + int from (n+1) to infinity of f(x) dx <= S <= S_n + int from n to infinity of f(x) dx",
   "S <= S_n",
   "S = S_n + int from n to infinity of f(x) dx"], ans=1,
   why="The remainder is trapped between the two integrals, with the integral starting at n giving the larger bound."),

 dict(q="sum from n=1 to infinity of e^(-n)", choices=[
   "diverges",
   "converges, since int from 1 to infinity of e^(-x) dx = 1/e",
   "converges to 1/e",
   "the integral test does not apply, since e^(-x) is not decreasing"], ans=1,
   why="The improper integral equals 1/e and is finite, so the series converges; its actual sum is 1/(e - 1)."),

 dict(q="sum from n=1 to infinity of 1/n^(3/2)", choices=[
   "converges, since int from 1 to infinity of x^(-3/2) dx = 2",
   "converges, since the integral equals 3/2",
   "diverges, since the integral diverges",
   "diverges, since the terms approach 0 too slowly"], ans=0,
   why="int from 1 to infinity of x^(-3/2) dx = 2 is finite, so the series converges."),

 dict(q="sum from n=1 to infinity of arctan(n)/(1 + n^2)", choices=[
   "converges",
   "diverges",
   "converges to pi/2",
   "the integral test does not apply, since arctan(x) is increasing"], ans=0,
   why="With u = arctan(x) the integral is (arctan(x))^2/2, whose limit 3*pi^2/32 above x = 1 is finite, so the series converges."),

 dict(q="For sum from n=1 to infinity of (2 + sin(n))/n^2, the integral test", choices=[
   "shows the series converges",
   "shows the series diverges",
   "cannot be used, because f(x) = (2 + sin(x))/x^2 is not decreasing on any interval [k, infinity)",
   "cannot be used, because the terms are not positive"], ans=2,
   why="The terms are positive but f is not eventually decreasing, so a hypothesis fails and another test (comparison with 3/n^2) is needed."),

 dict(q="sum from n=2 to infinity of 1/(n*(ln(n))^p) converges for exactly which values of p?", choices=[
   "p > 0",
   "p >= 1",
   "p > 1",
   "all real p"], ans=2,
   why="With u = ln(x) the integral becomes int of du/u^p above ln(2), which converges exactly when p > 1."),

 dict(q="sum from n=1 to infinity of 1/(3n + 2)", choices=[
   "converges, since the terms approach 0",
   "converges to 1/3",
   "diverges, since int from 1 to infinity of dx/(3x + 2) diverges",
   "the integral test does not apply"], ans=2,
   why="The antiderivative (1/3)ln(3x + 2) is unbounded, so the integral and the series both diverge."),

 dict(q="sum from n=1 to infinity of n/e^n", choices=[
   "converges, since int from 1 to infinity of x*e^(-x) dx = 2/e",
   "converges to 2/e",
   "diverges, since x*e^(-x) is increasing near x = 0",
   "diverges, since n -> infinity"], ans=0,
   why="Integration by parts gives 2/e for the improper integral, which is finite, so the series converges."),

 dict(q="The integral test shows that exactly one of the following converges. Which one?", choices=[
   "sum from n=1 to infinity of 1/sqrt(n)",
   "sum from n=2 to infinity of 1/(n*ln(n))",
   "sum from n=1 to infinity of 1/n^(1.1)",
   "sum from n=1 to infinity of n/(n^2 + 1)"], ans=2,
   why="Only p = 1.1 exceeds 1; the other three all have divergent improper integrals."),

 dict(q="Using the integral test remainder bound for sum from n=1 to infinity of 1/n^2, the smallest number of terms n that guarantees R_n <= 0.01 is", choices=[
   "10",
   "50",
   "100",
   "1000"], ans=2,
   why="R_n <= int from n to infinity of dx/x^2 = 1/n, and 1/n <= 0.01 first holds at n = 100."),
]
