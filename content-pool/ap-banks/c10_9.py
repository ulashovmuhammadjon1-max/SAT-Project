# CALC 10.9 Determining Absolute or Conditional Convergence — 25 questions
# Answers verified with sympy; see verify_c10_9.py
# Three outcomes, never two: absolutely convergent (sum |a_n| converges),
# conditionally convergent (sum a_n converges but sum |a_n| does not), and
# divergent.  The alternating harmonic series is the standard conditional case.
TOPIC = ("10.9", "Determining Absolute or Conditional Convergence", 10)
QUESTIONS = [
 dict(q="The series sum a_n converges absolutely means that", choices=[
   "sum |a_n| converges",
   "sum a_n converges and the terms are positive",
   "sum a_n converges but sum |a_n| diverges",
   "|sum a_n| is finite"], ans=0,
   why="Absolute convergence is convergence of the series of absolute values."),

 dict(q="The series sum a_n converges conditionally means that", choices=[
   "sum |a_n| converges but sum a_n diverges",
   "sum a_n converges but sum |a_n| diverges",
   "both sum a_n and sum |a_n| converge",
   "sum a_n converges only for certain values of n"], ans=1,
   why="Conditional convergence is convergence that survives the signs but not the absolute values."),

 dict(q="If sum |a_n| converges, then sum a_n", choices=[
   "converges",
   "diverges",
   "may converge or diverge",
   "converges only if the terms alternate"], ans=0,
   why="Absolute convergence implies convergence; this is why testing |a_n| is worth doing at all."),

 dict(q="Classify the series sum from n=1 to infinity of (-1)^n/n.", choices=[
   "converges absolutely",
   "converges conditionally",
   "diverges",
   "converges absolutely but not conditionally"], ans=1,
   why="The alternating series test gives convergence while the absolute series is the divergent harmonic series."),

 dict(q="Classify the series sum from n=1 to infinity of (-1)^n/n^2.", choices=[
   "converges absolutely",
   "converges conditionally",
   "diverges",
   "converges, but neither absolutely nor conditionally"], ans=0,
   why="The absolute series is the convergent p-series with p = 2."),

 dict(q="Classify the series sum from n=1 to infinity of (-1)^n/sqrt(n).", choices=[
   "converges absolutely",
   "converges conditionally",
   "diverges",
   "the alternating series test does not apply"], ans=1,
   why="1/sqrt(n) decreases to 0, but the absolute series is a p-series with p = 1/2, which diverges."),

 dict(q="Classify the series sum from n=1 to infinity of (-1)^n/n^3.", choices=[
   "converges conditionally",
   "converges absolutely",
   "diverges",
   "converges only because the terms alternate"], ans=1,
   why="The absolute series is a p-series with p = 3 > 1, so convergence does not depend on the signs."),

 dict(q="Classify the series sum from n=1 to infinity of (-1)^n*n/(n+1).", choices=[
   "converges absolutely",
   "converges conditionally",
   "diverges",
   "converges, since the terms alternate"], ans=2,
   why="The terms have absolute value approaching 1, so the series fails the nth term test and neither kind of convergence occurs."),

 dict(q="Classify the series sum from n=1 to infinity of (-1)^n/n!.", choices=[
   "converges absolutely",
   "converges conditionally",
   "diverges",
   "converges, but the absolute series diverges"], ans=0,
   why="sum 1/n! converges (to e - 1 starting at n = 1), so the convergence is absolute."),

 dict(q="Classify the series sum from n=1 to infinity of (-1)^n/2^n.", choices=[
   "converges conditionally",
   "converges absolutely",
   "diverges",
   "converges only for even n"], ans=1,
   why="The absolute series is geometric with r = 1/2, so it converges and the convergence is absolute."),

 dict(q="Classify the series sum from n=2 to infinity of (-1)^n*ln(n)/n.", choices=[
   "converges absolutely",
   "converges conditionally",
   "diverges",
   "the alternating series test does not apply"], ans=1,
   why="ln(n)/n decreases to 0 past n = 3, but sum ln(n)/n diverges by the integral test."),

 dict(q="Classify the series sum from n=2 to infinity of (-1)^n/ln(n).", choices=[
   "converges absolutely",
   "converges conditionally",
   "diverges",
   "converges absolutely, since 1/ln(n) < 1/n"], ans=1,
   why="1/ln(n) decreases to 0, but 1/ln(n) exceeds 1/n, so the absolute series diverges by comparison."),

 dict(q="Classify the series sum from n=1 to infinity of (-1)^(n+1)/(2n - 1).", choices=[
   "converges absolutely",
   "converges conditionally",
   "diverges",
   "converges absolutely to pi/4"], ans=1,
   why="It converges to pi/4 by the alternating series test, while sum 1/(2n-1) diverges by comparison with the harmonic series."),

 dict(q="Classify the series sum from n=1 to infinity of sin(n)/n^2.", choices=[
   "converges absolutely, since |sin(n)|/n^2 <= 1/n^2",
   "converges conditionally",
   "diverges, since sin(n) oscillates",
   "cannot be classified without knowing the signs of sin(n)"], ans=0,
   why="Comparison with the convergent p-series 1/n^2 settles the absolute series, and the erratic signs never matter."),

 dict(q="Classify the series sum from n=1 to infinity of (-1)^n*2n/(n^2 + 1).", choices=[
   "converges absolutely",
   "converges conditionally",
   "diverges",
   "the alternating series test does not apply"], ans=1,
   why="The terms decrease to 0, but a limit comparison of 2n/(n^2+1) with 1/n gives 2, so the absolute series diverges."),

 dict(q="Classify the series sum from n=1 to infinity of (-1)^n*3^n/n!.", choices=[
   "converges absolutely",
   "converges conditionally",
   "diverges",
   "converges only because 3^n < n! eventually"], ans=0,
   why="The ratio test on absolute values gives L = 0, so the series converges absolutely."),

 dict(q="If sum |a_n| diverges, then sum a_n", choices=[
   "diverges",
   "converges conditionally",
   "may converge conditionally or may diverge",
   "converges absolutely"], ans=2,
   why="Divergence of the absolute series rules out absolute convergence only; sum (-1)^n/n and sum 1/n show both remaining outcomes."),

 dict(q="A series for which sum a_n converges and sum |a_n| diverges is called", choices=[
   "absolutely convergent",
   "conditionally convergent",
   "divergent",
   "geometric"], ans=1,
   why="This is exactly the definition of conditional convergence."),

 dict(q="For which values of p does sum from n=1 to infinity of (-1)^n/n^p converge conditionally?", choices=[
   "p > 1",
   "0 < p <= 1",
   "p <= 0",
   "all p > 0"], ans=1,
   why="For 0 < p <= 1 the alternating series test applies while the p-series of absolute values diverges."),

 dict(q="For which values of p does sum from n=1 to infinity of (-1)^n/n^p converge absolutely?", choices=[
   "p > 0",
   "p >= 1",
   "p > 1",
   "0 < p <= 1"], ans=2,
   why="Absolute convergence is convergence of sum 1/n^p, which needs p > 1."),

 dict(q="True or false: every convergent alternating series converges conditionally.", choices=[
   "True, by the alternating series test",
   "True, since the absolute series always diverges",
   "False; sum (-1)^n/n^2 converges absolutely",
   "False; no alternating series converges"], ans=2,
   why="Alternating says nothing about the absolute series, and 1/n^2 converges, so that series is absolutely convergent."),

 dict(q="Classify the series sum from n=2 to infinity of (-1)^n/(n*ln(n)).", choices=[
   "converges absolutely",
   "converges conditionally",
   "diverges",
   "the alternating series test does not apply, since ln(n) increases"], ans=1,
   why="The terms decrease to 0, but the integral test shows sum 1/(n*ln(n)) diverges."),

 dict(q="Classify the series sum from n=1 to infinity of cos(n)/n^3.", choices=[
   "converges absolutely",
   "converges conditionally",
   "diverges",
   "cannot be classified, since the terms do not alternate regularly"], ans=0,
   why="|cos(n)|/n^3 <= 1/n^3, a convergent p-series, so the series converges absolutely."),

 dict(q="Classify the series sum from n=1 to infinity of (-1)^n*arctan(n)/n^2.", choices=[
   "converges absolutely, since arctan(n)/n^2 <= (pi/2)/n^2",
   "converges conditionally",
   "diverges, since arctan(n) approaches pi/2",
   "the alternating series test does not apply"], ans=0,
   why="arctan(n) is bounded by pi/2, so the absolute series is dominated by a convergent p-series."),

 dict(q="Which statement about rearranging the terms of a series is correct?", choices=[
   "Rearranging the terms of any convergent series leaves the sum unchanged",
   "The terms of an absolutely convergent series may be rearranged without changing the sum, but a conditionally convergent series can be rearranged to sum to any value",
   "Rearranging always destroys convergence",
   "A conditionally convergent series has the same sum under every rearrangement"], ans=1,
   why="This is Riemann's rearrangement theorem, and it is the deepest practical difference between the two kinds of convergence."),
]
