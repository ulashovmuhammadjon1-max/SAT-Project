# CALC 10.3 The nth Term Test for Divergence — 25 questions
# Answers verified with sympy; see verify_c10_3.py
# The whole topic turns on one asymmetry: lim a_n != 0 proves DIVERGENCE, while
# lim a_n = 0 proves NOTHING AT ALL.  Roughly a third of these questions put a
# series with terms tending to 0 in front of the student to see whether the test
# gets misused as a convergence test.
TOPIC = ("10.3", "The nth Term Test for Divergence", 10)
QUESTIONS = [
 dict(q="The nth term test for divergence says that", choices=[
   "if lim as n -> infinity of a_n = 0, then sum a_n converges",
   "if lim as n -> infinity of a_n is not 0 or does not exist, then sum a_n diverges",
   "if lim as n -> infinity of a_n = 0, then sum a_n diverges",
   "if sum a_n diverges, then lim as n -> infinity of a_n is not 0"], ans=1,
   why="The test concludes divergence from terms that fail to approach 0, and it is the only conclusion it can draw."),

 dict(q="If lim as n -> infinity of a_n = 0, the nth term test allows you to conclude that the series sum a_n", choices=[
   "converges",
   "diverges",
   "converges absolutely",
   "nothing; the test is inconclusive"], ans=3,
   why="Terms approaching 0 is necessary but not sufficient for convergence, so the test gives no conclusion."),

 dict(q="sum from n=1 to infinity of n/(2n+1)", choices=[
   "converges to 1/2 by the nth term test",
   "diverges by the nth term test",
   "converges to 0 by the nth term test",
   "cannot be analyzed by the nth term test"], ans=1,
   why="The terms approach 1/2, not 0, so the series diverges."),

 dict(q="sum from n=1 to infinity of (3n^2 + 1)/(n^2 + 5)", choices=[
   "converges to 3",
   "converges to 1/5",
   "diverges",
   "converges to 0"], ans=2,
   why="The terms approach 3, so by the nth term test the series diverges."),

 dict(q="Applied to the series sum from n=1 to infinity of 1/n, the nth term test shows that the series", choices=[
   "converges, because the terms approach 0",
   "diverges, because the terms approach 0",
   "converges to 1",
   "nothing; the terms approach 0 so the test is inconclusive"], ans=3,
   why="The harmonic series does diverge, but the nth term test cannot show it: the terms approach 0."),

 dict(q="sum from n=1 to infinity of (-1)^n", choices=[
   "converges to 0",
   "converges to -1/2",
   "diverges, because the terms do not approach a limit",
   "diverges, because the terms approach infinity"], ans=2,
   why="The terms alternate between -1 and 1, so lim a_n does not exist and the nth term test gives divergence."),

 dict(q="sum from n=1 to infinity of cos(n*pi)", choices=[
   "converges to 0",
   "converges to -1",
   "diverges by the nth term test",
   "diverges by the ratio test"], ans=2,
   why="cos(n*pi) = (-1)^n, whose limit does not exist, so the nth term test applies."),

 dict(q="sum from n=2 to infinity of n/ln(n)", choices=[
   "converges to 0",
   "diverges, because the terms increase without bound",
   "diverges, because the terms approach 1",
   "the nth term test is inconclusive"], ans=1,
   why="n/ln(n) -> infinity, so the terms are nowhere near 0 and the series diverges."),

 dict(q="sum from n=1 to infinity of (1 + 1/n)^n", choices=[
   "converges to e",
   "converges to 1",
   "diverges, because the terms approach e",
   "diverges, because the terms approach infinity"], ans=2,
   why="The terms approach e, which is not 0, so the series diverges even though the terms have a finite limit."),

 dict(q="sum from n=1 to infinity of n*sin(1/n)", choices=[
   "converges to 1",
   "converges to 0",
   "diverges, because the terms approach 1",
   "the nth term test is inconclusive"], ans=2,
   why="n*sin(1/n) -> 1 as n -> infinity, so the terms do not approach 0."),

 dict(q="For the series sum from n=1 to infinity of 2^n/n!, the nth term test", choices=[
   "proves the series converges",
   "proves the series diverges",
   "is inconclusive, because the terms approach 0",
   "does not apply, because the terms are not positive"], ans=2,
   why="The terms approach 0, so the test says nothing; some other test (the ratio test) is needed."),

 dict(q="For which of the following series does the nth term test establish divergence?", choices=[
   "sum from n=1 to infinity of 1/n",
   "sum from n=1 to infinity of 1/sqrt(n)",
   "sum from n=1 to infinity of n/(n+4)",
   "sum from n=1 to infinity of 1/n^2"], ans=2,
   why="Only n/(n+4) has terms with a nonzero limit, namely 1; the other three all have terms approaching 0."),

 dict(q="A student writes: 'The terms of sum 1/n^2 approach 0, so by the nth term test the series converges.' The error is that", choices=[
   "the terms of 1/n^2 do not approach 0",
   "the nth term test can never establish convergence",
   "the nth term test requires positive terms",
   "the series 1/n^2 actually diverges"], ans=1,
   why="The series does converge, but not for this reason: terms approaching 0 never by themselves prove convergence."),

 dict(q="For the series sum from n=2 to infinity of ln(n)/n, the nth term test", choices=[
   "gives divergence, since the terms approach infinity",
   "gives divergence, since the terms approach 1",
   "gives convergence, since the terms approach 0",
   "is inconclusive, since the terms approach 0"], ans=3,
   why="ln(n)/n -> 0, so no conclusion follows from this test (the series in fact diverges, by the integral test)."),

 dict(q="For the series sum from n=1 to infinity of e^(-n), the nth term test", choices=[
   "shows the series converges",
   "shows the series diverges",
   "is inconclusive",
   "does not apply"], ans=2,
   why="The terms approach 0, so the test is silent; the series converges, but as a geometric series with r = 1/e."),

 dict(q="sum from n=1 to infinity of n!/2^n", choices=[
   "converges to 0",
   "converges to 2",
   "diverges, because the terms increase without bound",
   "the nth term test is inconclusive"], ans=2,
   why="Factorial growth beats exponential growth, so n!/2^n -> infinity and the series diverges."),

 dict(q="sum from n=1 to infinity of arctan(n)", choices=[
   "converges to pi/2",
   "diverges, because the terms approach pi/2",
   "diverges, because the terms approach infinity",
   "the nth term test is inconclusive"], ans=1,
   why="arctan(n) -> pi/2, a nonzero limit, so the series diverges."),

 dict(q="For the series sum from n=1 to infinity of n^2/2^n, the nth term test", choices=[
   "gives divergence, since n^2 -> infinity",
   "gives convergence",
   "is inconclusive, since the terms approach 0",
   "does not apply, since the terms are not decreasing"], ans=2,
   why="The exponential in the denominator wins, so the terms approach 0 and the test is inconclusive."),

 dict(q="sum from n=1 to infinity of sqrt(n)/(sqrt(n) + 1)", choices=[
   "converges to 1",
   "converges to 0",
   "diverges",
   "the nth term test is inconclusive"], ans=2,
   why="Dividing by sqrt(n) shows the terms approach 1, so the series diverges."),

 dict(q="sum from n=1 to infinity of (5n^3 - 2)/(3n^3 + n)", choices=[
   "converges to 5/3",
   "converges to -2",
   "diverges",
   "the nth term test is inconclusive"], ans=2,
   why="The terms approach 5/3, which is not 0."),

 dict(q="sum from n=1 to infinity of sin(n)", choices=[
   "converges to 0",
   "diverges, because lim as n -> infinity of sin(n) does not exist",
   "diverges, because the terms approach infinity",
   "the nth term test is inconclusive"], ans=1,
   why="sin(n) oscillates without approaching any limit, and a failed limit is enough for the nth term test."),

 dict(q="If sum from n=1 to infinity of a_n is known to converge, then lim as n -> infinity of a_n", choices=[
   "equals 0",
   "equals the sum of the series",
   "may be any real number",
   "does not exist"], ans=0,
   why="This is the contrapositive of the nth term test: convergence forces the terms to approach 0."),

 dict(q="True or false: if lim as n -> infinity of a_n = 0, then sum from n=1 to infinity of a_n converges.", choices=[
   "True, by the nth term test",
   "True, provided the terms are positive",
   "False; the harmonic series sum 1/n is a counterexample",
   "False; no series with terms approaching 0 converges"], ans=2,
   why="The harmonic series has terms tending to 0 and still diverges, so the converse of the nth term test fails."),

 dict(q="sum from n=1 to infinity of (1 - 1/n)^n", choices=[
   "converges to 1/e",
   "converges to 0",
   "diverges, because the terms approach 1/e",
   "diverges, because the terms approach 1"], ans=2,
   why="(1 - 1/n)^n -> e^(-1), which is about 0.368 and not 0, so the series diverges."),

 dict(q="For which values of p does the nth term test prove that sum from n=1 to infinity of n^p diverges?", choices=[
   "p > 1",
   "p >= 0",
   "p > -1",
   "all real p"], ans=1,
   why="n^p fails to approach 0 exactly when p >= 0 (the limit is 1 at p = 0 and infinity for p > 0); for p < 0 the terms approach 0 and the test is inconclusive."),
]
