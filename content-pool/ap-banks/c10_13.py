# CALC 10.13 Radius and Interval of Convergence of Power Series — 25 questions
# Answers verified with sympy; see verify_c10_13.py
# The ratio test gives the radius and nothing more: at each endpoint it returns
# L = 1 and is inconclusive, so BOTH endpoints must be tested separately by
# another test.  Six items here have one endpoint that converges and one that
# does not, which is the case a student who checks only one will get wrong.
TOPIC = ("10.13", "Radius and Interval of Convergence of Power Series", 10)
QUESTIONS = [
 dict(q="For a power series sum c_n*(x - a)^n, the radius of convergence R is the number such that", choices=[
   "the series converges for |x - a| < R and diverges for |x - a| > R",
   "the series converges for |x - a| <= R and diverges for |x - a| > R",
   "the series converges only at x = a + R",
   "the series diverges for |x - a| < R"], ans=0,
   why="Inside the radius there is convergence and outside there is divergence; the two endpoints are left undecided."),

 dict(q="At an endpoint of the interval of convergence, the ratio test", choices=[
   "shows convergence",
   "shows divergence",
   "gives L = 1 and is inconclusive, so another test is needed",
   "cannot be applied because the terms are not positive"], ans=2,
   why="The endpoints are exactly where the ratio limit equals 1, which is the case the test cannot decide."),

 dict(q="The interval of convergence of sum from n=1 to infinity of x^n/n is", choices=[
   "(-1, 1)",
   "[-1, 1)",
   "(-1, 1]",
   "[-1, 1]"], ans=1,
   why="At x = 1 the series is the divergent harmonic series; at x = -1 it is the convergent alternating harmonic series."),

 dict(q="The interval of convergence of sum from n=1 to infinity of x^n/n^2 is", choices=[
   "(-1, 1)",
   "[-1, 1)",
   "(-1, 1]",
   "[-1, 1]"], ans=3,
   why="Both endpoints give convergent series: sum 1/n^2 and sum (-1)^n/n^2."),

 dict(q="The interval of convergence of sum from n=0 to infinity of x^n is", choices=[
   "(-1, 1)",
   "[-1, 1]",
   "[-1, 1)",
   "all real numbers"], ans=0,
   why="At both endpoints the terms fail to approach 0, so the geometric series diverges there."),

 dict(q="The interval of convergence of sum from n=0 to infinity of x^n/n! is", choices=[
   "(-1, 1)",
   "[-1, 1]",
   "all real numbers",
   "only x = 0"], ans=2,
   why="The ratio |x|/(n+1) approaches 0 for every x, so the radius is infinite."),

 dict(q="The interval of convergence of sum from n=0 to infinity of n!*x^n is", choices=[
   "all real numbers",
   "(-1, 1)",
   "only x = 0",
   "[-1, 1]"], ans=2,
   why="The ratio (n+1)|x| becomes infinite for every x other than 0, so the radius of convergence is 0."),

 dict(q="The interval of convergence of sum from n=1 to infinity of (x - 2)^n/n is", choices=[
   "(1, 3)",
   "[1, 3)",
   "(1, 3]",
   "[1, 3]"], ans=1,
   why="The center is 2 with R = 1; at x = 1 the alternating harmonic series converges and at x = 3 the harmonic series diverges."),

 dict(q="The interval of convergence of sum from n=0 to infinity of (x + 3)^n/3^n is", choices=[
   "(-6, 0)",
   "[-6, 0]",
   "(-3, 3)",
   "[-6, 0)"], ans=0,
   why="R = 3 about the center -3, and at both endpoints the terms are (+/-1)^n, which do not approach 0."),

 dict(q="The interval of convergence of sum from n=1 to infinity of (2x)^n/n is", choices=[
   "(-1/2, 1/2)",
   "[-1/2, 1/2)",
   "(-1/2, 1/2]",
   "[-1/2, 1/2]"], ans=1,
   why="R = 1/2; at x = 1/2 the series is the harmonic series and at x = -1/2 it is the alternating harmonic series."),

 dict(q="The interval of convergence of sum from n=1 to infinity of (x - 1)^n/(n*2^n) is", choices=[
   "(-1, 3)",
   "[-1, 3)",
   "(-1, 3]",
   "[-1, 3]"], ans=1,
   why="The center is 1 with R = 2; at x = -1 the series becomes sum (-1)^n/n, which converges, and at x = 3 it becomes sum 1/n, which does not."),

 dict(q="The interval of convergence of sum from n=1 to infinity of n*x^n is", choices=[
   "(-1, 1)",
   "[-1, 1)",
   "(-1, 1]",
   "[-1, 1]"], ans=0,
   why="R = 1, and at both endpoints |n*x^n| = n does not approach 0."),

 dict(q="The interval of convergence of sum from n=1 to infinity of x^n/sqrt(n) is", choices=[
   "(-1, 1)",
   "[-1, 1)",
   "(-1, 1]",
   "[-1, 1]"], ans=1,
   why="At x = 1 the p-series with p = 1/2 diverges; at x = -1 the alternating series test gives convergence."),

 dict(q="The radius of convergence of sum from n=1 to infinity of x^(2n)/n is", choices=[
   "1/2",
   "1",
   "2",
   "infinite"], ans=1,
   why="The ratio test gives |x|^2 < 1, so |x| < 1 and R = 1."),

 dict(q="If the coefficients of a power series centered at x = 0 satisfy lim as n -> infinity of |c_(n+1)/c_n| = 1/5, then the radius of convergence is", choices=[
   "1/5",
   "1",
   "5",
   "25"], ans=2,
   why="The ratio test requires |x|/5 < 1, so |x| < 5."),

 dict(q="Knowing the radius of convergence R of a power series, the interval of convergence is determined", choices=[
   "completely, since it is always (a - R, a + R)",
   "completely, since it is always [a - R, a + R]",
   "except at the two endpoints, which must be tested separately",
   "only if the coefficients are positive"], ans=2,
   why="Every combination of endpoint behavior is possible, so each endpoint needs its own convergence test."),

 dict(q="The interval of convergence of sum from n=0 to infinity of (-1)^n*x^n/(n+1) is", choices=[
   "(-1, 1)",
   "[-1, 1)",
   "(-1, 1]",
   "[-1, 1]"], ans=2,
   why="At x = 1 the alternating series converges; at x = -1 the series becomes sum 1/(n+1), which diverges."),

 dict(q="A power series centered at x = 3 converges at x = 5 and diverges at x = 9. Its radius of convergence R must satisfy", choices=[
   "R = 2",
   "R = 6",
   "2 <= R <= 6",
   "R >= 6"], ans=2,
   why="Convergence at distance 2 forces R >= 2, and divergence at distance 6 forces R <= 6."),

 dict(q="The center of the power series sum from n=1 to infinity of (x + 4)^n/n^2 is", choices=[
   "x = 4",
   "x = -4",
   "x = 0",
   "x = 1"], ans=1,
   why="Writing (x + 4) as (x - (-4)) shows the center is -4."),

 dict(q="The interval of convergence of sum from n=1 to infinity of (x - 2)^n/n^2 is", choices=[
   "(1, 3)",
   "[1, 3)",
   "(1, 3]",
   "[1, 3]"], ans=3,
   why="R = 1 about the center 2, and at both endpoints the series is a convergent p-series with p = 2 (with signs at one end)."),

 dict(q="A power series centered at x = 1 has radius of convergence 4. The series is guaranteed to converge for", choices=[
   "-3 < x < 5",
   "-4 < x < 4",
   "1 < x < 5",
   "-3 <= x <= 5"], ans=0,
   why="Convergence is guaranteed strictly inside the radius, which is the open interval from 1 - 4 to 1 + 4."),

 dict(q="Every power series sum c_n*(x - a)^n converges", choices=[
   "for all x",
   "at x = a, at least",
   "for no x if R = 0",
   "only on a closed interval"], ans=1,
   why="At x = a every term after the first is 0, so the series always converges there, even when R = 0."),

 dict(q="The radius of convergence of sum from n=1 to infinity of n^2*x^n/2^n is", choices=[
   "1/2",
   "1",
   "2",
   "4"], ans=2,
   why="The ratio is |x|/2 times (n+1)^2/n^2, whose limit is |x|/2, so |x| < 2."),

 dict(q="The interval of convergence of sum from n=1 to infinity of n*x^n/2^n is", choices=[
   "(-2, 2)",
   "[-2, 2)",
   "(-2, 2]",
   "[-2, 2]"], ans=0,
   why="R = 2, and at x = 2 and x = -2 the terms have absolute value n, which does not approach 0."),

 dict(q="The interval of convergence of sum from n=1 to infinity of (x - 1)^n/(n^2*3^n) is", choices=[
   "(-2, 4)",
   "[-2, 4)",
   "(-2, 4]",
   "[-2, 4]"], ans=3,
   why="The center is 1 with R = 3, and at both endpoints the series is dominated by the convergent p-series sum 1/n^2."),
]
