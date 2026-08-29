# CALC 10.8 Ratio Test for Convergence — 25 questions
# Answers verified with sympy; see verify_c10_8.py
# L = lim |a_(n+1)/a_n| decides convergence when L < 1 and divergence when
# L > 1, and decides NOTHING when L = 1.  Four items land exactly on L = 1,
# two of them converging and two diverging, so that "L = 1" can never be read
# as a verdict.
TOPIC = ("10.8", "Ratio Test for Convergence", 10)
QUESTIONS = [
 dict(q="If L = lim as n -> infinity of |a_(n+1)/a_n| exists, the ratio test says that sum a_n converges absolutely when", choices=[
   "L < 1",
   "L <= 1",
   "L > 1",
   "L = 1"], ans=0,
   why="A ratio limit below 1 makes the tail dominated by a convergent geometric series."),

 dict(q="If the ratio test gives L = 1 for a series, then the series", choices=[
   "converges",
   "diverges",
   "converges absolutely",
   "may converge or diverge; the test is inconclusive"], ans=3,
   why="L = 1 is precisely the case the ratio test cannot decide, and both outcomes occur there."),

 dict(q="For sum from n=1 to infinity of n/2^n, the ratio test gives L equal to", choices=[
   "0",
   "1/2",
   "1",
   "2"], ans=1,
   why="The ratio is (n+1)/(2n), whose limit is 1/2, so the series converges."),

 dict(q="sum from n=1 to infinity of 2^n/n!", choices=[
   "converges, since L = 0",
   "converges, since L = 2",
   "diverges, since L = 2",
   "the ratio test is inconclusive"], ans=0,
   why="The ratio is 2/(n+1), which approaches 0, so the series converges absolutely."),

 dict(q="sum from n=1 to infinity of n!/10^n", choices=[
   "converges, since L = 1/10",
   "converges, since L = 0",
   "diverges, since L = infinity",
   "the ratio test is inconclusive"], ans=2,
   why="The ratio is (n+1)/10, which increases without bound, so the series diverges."),

 dict(q="Applying the ratio test to sum from n=1 to infinity of 1/n gives", choices=[
   "L = 0, so the series converges",
   "L = 1, so the series diverges",
   "L = 1, so the test is inconclusive; the series in fact diverges",
   "L = infinity, so the series diverges"], ans=2,
   why="The ratio n/(n+1) approaches 1, so the ratio test says nothing and the p-series rule must be used."),

 dict(q="Applying the ratio test to sum from n=1 to infinity of 1/n^2 gives", choices=[
   "L = 1, so the test is inconclusive; the series in fact converges",
   "L = 1, so the series diverges",
   "L = 0, so the series converges",
   "L = 1/2, so the series converges"], ans=0,
   why="The ratio n^2/(n+1)^2 approaches 1, and this convergent series shows L = 1 cannot mean divergence."),

 dict(q="sum from n=1 to infinity of n^2/3^n", choices=[
   "diverges, since L = 3",
   "converges, since L = 1/3",
   "converges, since L = 0",
   "the ratio test is inconclusive"], ans=1,
   why="The ratio is (n+1)^2/(3n^2), whose limit is 1/3 < 1."),

 dict(q="sum from n=1 to infinity of (-1)^n*3^n/n!", choices=[
   "diverges, since L = 3",
   "converges absolutely, since L = 0",
   "converges conditionally, since L = 1",
   "the ratio test does not apply to alternating series"], ans=1,
   why="The ratio test uses absolute values, and 3/(n+1) approaches 0, giving absolute convergence."),

 dict(q="sum from n=1 to infinity of n!/(2n)!", choices=[
   "converges, since L = 0",
   "converges, since L = 1/2",
   "diverges, since L = infinity",
   "the ratio test is inconclusive"], ans=0,
   why="The ratio is (n+1)/((2n+2)(2n+1)), which approaches 0."),

 dict(q="sum from n=1 to infinity of 3^n/(n*2^n)", choices=[
   "converges, since L = 2/3",
   "diverges, since L = 3/2",
   "converges, since L = 1",
   "the ratio test is inconclusive"], ans=1,
   why="The ratio is (3/2)*n/(n+1), whose limit is 3/2 > 1, so the series diverges."),

 dict(q="sum from n=1 to infinity of (n!)^2/(2n)!", choices=[
   "diverges, since L = 4",
   "converges, since L = 1/4",
   "converges, since L = 0",
   "the ratio test is inconclusive"], ans=1,
   why="The ratio is (n+1)^2/((2n+1)(2n+2)), whose limit is 1/4 < 1."),

 dict(q="Applying the ratio test to sum from n=1 to infinity of n/(n^2 + 1) gives", choices=[
   "L = 1, so the test is inconclusive",
   "L = 1, so the series converges",
   "L = 0, so the series converges",
   "L = infinity, so the series diverges"], ans=0,
   why="Every rational function of n gives L = 1; a limit comparison with 1/n is what shows this series diverges."),

 dict(q="For sum from n=1 to infinity of 1/n!, the ratio test gives L equal to", choices=[
   "0",
   "1/2",
   "1",
   "e"], ans=0,
   why="The ratio is 1/(n+1), which approaches 0, so the series converges."),

 dict(q="sum from n=1 to infinity of (2n)!/(n!)^2", choices=[
   "converges, since L = 1/4",
   "diverges, since L = 4",
   "converges, since L = 0",
   "the ratio test is inconclusive"], ans=1,
   why="The ratio is (2n+1)(2n+2)/(n+1)^2, whose limit is 4 > 1."),

 dict(q="sum from n=1 to infinity of (-2)^n/n^2", choices=[
   "converges absolutely, since L = 1/2",
   "converges conditionally, since the terms alternate",
   "diverges, since L = 2",
   "the ratio test is inconclusive, since L = 1"], ans=2,
   why="The ratio of absolute values is 2n^2/(n+1)^2, whose limit is 2 > 1, so the terms do not even approach 0."),

 dict(q="sum from n=1 to infinity of n^n/n!", choices=[
   "converges, since L = 1/e",
   "diverges, since L = e",
   "converges, since L = 0",
   "the ratio test is inconclusive"], ans=1,
   why="The ratio simplifies to (1 + 1/n)^n, whose limit is e, which is greater than 1."),

 dict(q="sum from n=1 to infinity of 5^n/(n^2*4^n)", choices=[
   "converges, since L = 4/5",
   "diverges, since L = 5/4",
   "converges, since the n^2 in the denominator dominates",
   "the ratio test is inconclusive"], ans=1,
   why="The ratio is (5/4)*n^2/(n+1)^2, whose limit is 5/4 > 1, and the n^2 cannot offset an exponential."),

 dict(q="For which of the following series is the ratio test inconclusive?", choices=[
   "sum from n=1 to infinity of 3^n/n!",
   "sum from n=1 to infinity of (2n + 3)/(n^3 + 1)",
   "sum from n=1 to infinity of n!/5^n",
   "sum from n=1 to infinity of n/4^n"], ans=1,
   why="A ratio of polynomials always gives L = 1; the other three give 0, infinity, and 1/4."),

 dict(q="A student computes L = 1 for a series and concludes that the series diverges. This conclusion is", choices=[
   "correct, since L = 1 fails the condition L < 1",
   "correct, since the terms do not approach 0",
   "unjustified, since L = 1 gives no information at all",
   "correct only if the terms are positive"], ans=2,
   why="Both sum 1/n and sum 1/n^2 give L = 1, and they behave differently, so L = 1 supports no conclusion."),

 dict(q="sum from n=1 to infinity of (n+1)/(n*3^n)", choices=[
   "converges, since L = 1/3",
   "diverges, since L = 3",
   "converges, since L = 1",
   "the ratio test is inconclusive"], ans=0,
   why="The polynomial factor contributes a limit of 1 and the geometric factor a limit of 1/3."),

 dict(q="sum from n=1 to infinity of 1/(2n)!", choices=[
   "converges, since L = 0",
   "converges, since L = 1/2",
   "diverges, since L = infinity",
   "the ratio test is inconclusive"], ans=0,
   why="The ratio is 1/((2n+1)(2n+2)), which approaches 0."),

 dict(q="sum from n=1 to infinity of (-1)^n*n^3/n!", choices=[
   "converges absolutely, since L = 0",
   "converges conditionally, since L = 1",
   "diverges, since L = infinity",
   "the ratio test is inconclusive"], ans=0,
   why="The ratio of absolute values is (n+1)^2/n^3, which approaches 0, so the series converges absolutely."),

 dict(q="sum from n=1 to infinity of 2^n/n^2", choices=[
   "converges, since L = 1/2",
   "diverges, since L = 2",
   "converges, since n^2 grows",
   "the ratio test is inconclusive"], ans=1,
   why="The ratio is 2n^2/(n+1)^2, whose limit is 2 > 1, so the series diverges."),

 dict(q="For which values of x does the ratio test guarantee that sum from n=1 to infinity of n*x^n converges?", choices=[
   "|x| < 1",
   "|x| <= 1",
   "x > 0",
   "all real x"], ans=0,
   why="The ratio is |x|*(n+1)/n, whose limit is |x|, so the test gives convergence exactly when |x| < 1."),
]
