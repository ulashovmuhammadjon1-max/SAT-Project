# CALC 10.7 Alternating Series Test for Convergence — 25 questions
# Answers verified with sympy; see verify_c10_7.py
# The test needs BOTH conditions: b_n decreasing in absolute value AND b_n -> 0.
# Several items fail the second condition, one fails the first, and one is not
# actually alternating at all once (-1)^n*cos(n*pi) is simplified.
TOPIC = ("10.7", "Alternating Series Test for Convergence", 10)
QUESTIONS = [
 dict(q="The alternating series test says that sum from n=1 to infinity of (-1)^n*b_n, with b_n > 0, converges provided that", choices=[
   "lim as n -> infinity of b_n = 0",
   "b_n is eventually decreasing and lim as n -> infinity of b_n = 0",
   "b_n is eventually decreasing",
   "sum b_n converges"], ans=1,
   why="Both conditions are required: the terms must decrease in absolute value and must approach 0."),

 dict(q="sum from n=1 to infinity of (-1)^n*n/(n+1)", choices=[
   "converges by the alternating series test",
   "diverges, because b_n = n/(n+1) does not approach 0",
   "diverges, because b_n is increasing",
   "converges to -1/2"], ans=1,
   why="b_n approaches 1, so the terms do not approach 0 and the nth term test gives divergence."),

 dict(q="sum from n=1 to infinity of (-1)^n/n", choices=[
   "diverges, since sum 1/n diverges",
   "converges by the alternating series test",
   "diverges, since the terms do not approach 0",
   "converges, since it is a geometric series"], ans=1,
   why="b_n = 1/n decreases to 0, so the alternating series test applies even though the harmonic series diverges."),

 dict(q="sum from n=1 to infinity of (-1)^n/sqrt(n)", choices=[
   "converges by the alternating series test",
   "diverges, since sum 1/sqrt(n) diverges",
   "diverges, since b_n does not approach 0",
   "converges, since p = 1/2 < 1"], ans=0,
   why="1/sqrt(n) decreases to 0, which is all the alternating series test requires."),

 dict(q="sum from n=1 to infinity of (-1)^n/n^2", choices=[
   "diverges",
   "converges by the alternating series test",
   "converges only because the terms alternate",
   "diverges, since b_n is not decreasing"], ans=1,
   why="1/n^2 decreases to 0, so the alternating series test gives convergence."),

 dict(q="sum from n=1 to infinity of (-1)^n*n/(2n+1)", choices=[
   "converges by the alternating series test",
   "converges to -1/4",
   "diverges, because b_n approaches 1/2 rather than 0",
   "diverges, because b_n is increasing without bound"], ans=2,
   why="The alternating series test fails at the limit condition, and the nth term test then proves divergence."),

 dict(q="sum from n=2 to infinity of (-1)^n*ln(n)/n", choices=[
   "diverges, since ln(n)/n does not approach 0",
   "converges by the alternating series test, since ln(n)/n decreases to 0 for n >= 3",
   "diverges, since sum ln(n)/n diverges",
   "converges, since ln(n)/n < 1/n"], ans=1,
   why="ln(n)/n approaches 0 and is decreasing past n = e, so the test applies; the divergence of the absolute series is irrelevant here."),

 dict(q="sum from n=1 to infinity of (-1)^n/n!", choices=[
   "diverges",
   "converges by the alternating series test",
   "converges only if n! is replaced by 2^n",
   "diverges, since n! grows too quickly"], ans=1,
   why="1/n! decreases to 0, so the test applies; the sum is 1/e - 1."),

 dict(q="sum from n=1 to infinity of (-1)^n*n/(n^2 + 1)", choices=[
   "diverges, since b_n approaches 1",
   "converges by the alternating series test",
   "diverges, since sum n/(n^2 + 1) diverges",
   "the alternating series test does not apply, since b_n increases"], ans=1,
   why="b_n = n/(n^2+1) decreases to 0 for n >= 1, so the test applies even though the absolute series diverges."),

 dict(q="sum from n=1 to infinity of (-1)^n*2^n/n!", choices=[
   "diverges, since 2^n grows without bound",
   "converges by the alternating series test, since 2^n/n! decreases to 0 for n >= 2",
   "diverges, since b_n increases for n = 1",
   "converges, since it is a geometric series with r = -2"], ans=1,
   why="From n = 2 onward the ratio b_(n+1)/b_n = 2/(n+1) is less than 1, and 2^n/n! approaches 0."),

 dict(q="sum from n=1 to infinity of (-1)^n*sin(1/n)", choices=[
   "diverges, since sin(1/n) oscillates",
   "converges by the alternating series test",
   "diverges, since b_n does not approach 0",
   "the test does not apply, since sin(1/n) can be negative"], ans=1,
   why="For n >= 1, sin(1/n) is positive and decreases to 0."),

 dict(q="If b_n > 0 and lim as n -> infinity of b_n = 0 but b_n is not eventually decreasing, then the alternating series test", choices=[
   "still applies",
   "proves that sum (-1)^n*b_n diverges",
   "cannot be applied, and another argument is needed",
   "applies only if sum b_n converges"], ans=2,
   why="A hypothesis has failed, so the test yields no conclusion in either direction."),

 dict(q="sum from n=1 to infinity of (-1)^(n+1)/(2n - 1)", choices=[
   "diverges, since sum 1/(2n-1) diverges",
   "converges by the alternating series test",
   "diverges, since b_n does not approach 0",
   "converges, since it is geometric"], ans=1,
   why="1/(2n-1) decreases to 0; this is the classical Leibniz series, whose sum is pi/4."),

 dict(q="sum from n=1 to infinity of (-1)^n*cos(n*pi)/n", choices=[
   "converges by the alternating series test",
   "diverges, because the series simplifies to the harmonic series",
   "converges to ln(2)",
   "diverges, because the terms do not approach 0"], ans=1,
   why="cos(n*pi) = (-1)^n, so (-1)^n*cos(n*pi) = 1 and the series is sum 1/n, which is not alternating at all."),

 dict(q="sum from n=1 to infinity of (-1)^n*sqrt(n)/(n+1)", choices=[
   "diverges, since sqrt(n) increases",
   "converges by the alternating series test",
   "diverges, since b_n approaches 1",
   "the test does not apply, since b_n increases for small n"], ans=1,
   why="b_n = sqrt(n)/(n+1) decreases for n >= 1 and approaches 0."),

 dict(q="sum from n=1 to infinity of (-1)^n*e^(-n)", choices=[
   "diverges",
   "converges by the alternating series test",
   "converges only for n large",
   "diverges, since e^(-n) is not decreasing"], ans=1,
   why="e^(-n) decreases to 0; the series is also geometric with r = -1/e."),

 dict(q="For b_n = n/(n^2 + 4), the smallest integer N such that b_n is decreasing for all n >= N is", choices=[
   "1",
   "2",
   "3",
   "4"], ans=1,
   why="The derivative of x/(x^2+4) is (4 - x^2)/(x^2+4)^2, which is negative for x > 2, so the sequence decreases from n = 2 on."),

 dict(q="Which of the following alternating series diverges?", choices=[
   "sum from n=1 to infinity of (-1)^n/n^(1/3)",
   "sum from n=1 to infinity of (-1)^n*(n+1)/n^2",
   "sum from n=1 to infinity of (-1)^n*(n^2+1)/(n^2+2)",
   "sum from n=1 to infinity of (-1)^n/(n+3)"], ans=2,
   why="Only (n^2+1)/(n^2+2) fails to approach 0; it approaches 1, so that series diverges."),

 dict(q="sum from n=1 to infinity of (-1)^n*3n/(n+5)", choices=[
   "converges by the alternating series test",
   "converges to -3/2",
   "diverges, because b_n approaches 3",
   "diverges, because b_n increases without bound"], ans=2,
   why="b_n approaches 3, not 0, so the series diverges by the nth term test."),

 dict(q="sum from n=2 to infinity of (-1)^n/ln(n)", choices=[
   "diverges, since sum 1/ln(n) diverges",
   "converges by the alternating series test",
   "diverges, since 1/ln(n) does not approach 0",
   "the test does not apply, since ln(n) < n"], ans=1,
   why="1/ln(n) decreases to 0, so the alternating series test applies; the divergence of the absolute series does not matter."),

 dict(q="sum from n=1 to infinity of (-1)^n*n^2/2^n", choices=[
   "diverges, since n^2 increases without bound",
   "converges by the alternating series test, since n^2/2^n decreases to 0 for n >= 3",
   "diverges, since b_n increases for n = 1 and n = 2",
   "converges, since it is geometric with r = -1/2"], ans=1,
   why="The exponential in the denominator eventually dominates, so b_n decreases to 0 from n = 3 on."),

 dict(q="sum from n=1 to infinity of (-1)^n*(n+1)/n^2", choices=[
   "diverges, since sum (n+1)/n^2 diverges",
   "converges by the alternating series test",
   "diverges, since b_n approaches 1",
   "the test does not apply, since b_n is not positive"], ans=1,
   why="b_n = 1/n + 1/n^2 decreases to 0, so the test applies; the absolute series does diverge, which the test does not care about."),

 dict(q="sum from n=1 to infinity of (-1)^n*arctan(n)", choices=[
   "converges by the alternating series test",
   "converges to -pi/4",
   "diverges, because arctan(n) approaches pi/2",
   "diverges, because arctan(n) is decreasing"], ans=2,
   why="b_n approaches pi/2, so the terms do not approach 0 and the series diverges."),

 dict(q="sum from n=2 to infinity of (-1)^(n+1)/(n*ln(n))", choices=[
   "diverges, since sum 1/(n*ln(n)) diverges",
   "converges by the alternating series test",
   "diverges, since b_n does not approach 0",
   "the test does not apply, since ln(n) is increasing"], ans=1,
   why="1/(n*ln(n)) decreases to 0 for n >= 2, so the test applies even though the absolute series diverges."),

 dict(q="For which values of p does sum from n=1 to infinity of (-1)^n/n^p converge?", choices=[
   "p > 1",
   "p > 0",
   "p >= 1",
   "all real p"], ans=1,
   why="For p > 0 the sequence 1/n^p decreases to 0 and the alternating series test applies; for p <= 0 the terms do not approach 0."),
]
