# CALC 10.6 Comparison Tests for Convergence — 25 questions
# Answers verified with sympy; see verify_c10_6.py
# A comparison only works in one direction: smaller than a CONVERGENT series
# proves convergence, larger than a DIVERGENT series proves divergence, and the
# other two arrangements prove nothing.  Several items are built on exactly the
# arrangements that prove nothing.
TOPIC = ("10.6", "Comparison Tests for Convergence", 10)
QUESTIONS = [
 dict(q="Suppose 0 <= a_n <= b_n for all n. If sum b_n converges, then sum a_n", choices=[
   "converges",
   "diverges",
   "may converge or diverge",
   "converges only if the terms are decreasing"], ans=0,
   why="A series of nonnegative terms bounded above by a convergent series has bounded partial sums, so it converges."),

 dict(q="Suppose 0 <= a_n <= b_n for all n. If sum a_n converges, then sum b_n", choices=[
   "converges",
   "diverges",
   "may converge or diverge",
   "converges to a larger number"], ans=2,
   why="The larger series is unconstrained: 1/n^2 <= 1/n^2 converges while 1/n^2 <= 1/n does not settle 1/n, which diverges."),

 dict(q="Suppose a_n >= b_n >= 0 for all n. If sum b_n diverges, then sum a_n", choices=[
   "converges",
   "diverges",
   "may converge or diverge",
   "converges if a_n approaches 0"], ans=1,
   why="The larger nonnegative series has partial sums at least as big as those of a divergent series, so it too diverges."),

 dict(q="Suppose 0 <= a_n <= b_n for all n. If sum b_n diverges, then sum a_n", choices=[
   "converges",
   "diverges",
   "may converge or diverge",
   "diverges, but more slowly"], ans=2,
   why="Being smaller than a divergent series says nothing: 1/n^2 and 1/n are both below 1/n but only one converges."),

 dict(q="The limit comparison test says that if a_n > 0, b_n > 0, and lim as n -> infinity of (a_n/b_n) = L, then sum a_n and sum b_n both converge or both diverge provided that", choices=[
   "L = 0",
   "L is a finite positive number",
   "L = 1",
   "L is any real number"], ans=1,
   why="A finite positive limit makes the two term sequences comparable in size, which is what the conclusion needs."),

 dict(q="sum from n=1 to infinity of 1/(n^2 + 1)", choices=[
   "converges, since 1/(n^2 + 1) < 1/n^2 and sum 1/n^2 converges",
   "diverges, since 1/(n^2 + 1) < 1/n and sum 1/n diverges",
   "converges, since 1/(n^2 + 1) > 1/n^2",
   "diverges, since the terms approach 0"], ans=0,
   why="The terms sit below those of a convergent p-series, which is a valid direct comparison."),

 dict(q="sum from n=2 to infinity of 1/(n - 1)", choices=[
   "converges, since 1/(n - 1) < 1/n^2",
   "diverges, since 1/(n - 1) > 1/n and sum 1/n diverges",
   "converges, since the terms approach 0",
   "diverges, since the terms do not approach 0"], ans=1,
   why="The terms exceed those of the divergent harmonic series, which is a valid direct comparison."),

 dict(q="sum from n=1 to infinity of (2 + cos(n))/n^2", choices=[
   "diverges, since cos(n) has no limit",
   "converges, since (2 + cos(n))/n^2 <= 3/n^2 and sum 3/n^2 converges",
   "diverges, since (2 + cos(n))/n^2 >= 1/n^2",
   "the comparison test does not apply, since the terms are not always positive"], ans=1,
   why="Because cos(n) never exceeds 1, the terms are trapped below a convergent multiple of the p-series 1/n^2."),

 dict(q="sum from n=1 to infinity of 1/(3^n + 1)", choices=[
   "diverges",
   "converges, since 1/(3^n + 1) < 1/3^n and sum 1/3^n converges",
   "converges, since 1/(3^n + 1) < 1/n^2",
   "converges to 1/2"], ans=1,
   why="The terms are below those of a convergent geometric series with r = 1/3."),

 dict(q="sum from n=1 to infinity of 1/(sqrt(n) + 1)", choices=[
   "converges, since 1/(sqrt(n) + 1) < 1/sqrt(n)",
   "converges, since the terms approach 0",
   "diverges, since 1/(sqrt(n) + 1) >= 1/(2*sqrt(n)) and sum 1/sqrt(n) diverges",
   "diverges, since the terms do not approach 0"], ans=2,
   why="For n >= 1 the denominator is at most 2*sqrt(n), putting the terms above a divergent p-series."),

 dict(q="sum from n=1 to infinity of 1/sqrt(n^2 + 1)", choices=[
   "converges, by comparison with sum 1/n^2",
   "diverges, since the limit comparison with sum 1/n gives 1",
   "converges, since the limit comparison with sum 1/n gives 1",
   "converges, since the terms approach 0"], ans=1,
   why="lim (1/sqrt(n^2+1))/(1/n) = 1, a finite positive number, so the series behaves like the divergent harmonic series."),

 dict(q="sum from n=1 to infinity of (3n^2 + 2)/(n^4 + 5)", choices=[
   "converges, by limit comparison with sum 1/n^2",
   "diverges, by limit comparison with sum 1/n",
   "converges, by limit comparison with sum 1/n^4",
   "diverges, since the numerator grows"], ans=0,
   why="The ratio to 1/n^2 has limit 3, a finite positive number, and sum 1/n^2 converges."),

 dict(q="sum from n=1 to infinity of (n + 2)/(n^3 + 1)", choices=[
   "diverges, by limit comparison with sum 1/n",
   "converges, by limit comparison with sum 1/n^2",
   "converges, by limit comparison with sum 1/n^3",
   "diverges, since n + 2 > n"], ans=1,
   why="The dominant behavior is n/n^3 = 1/n^2, and the limit of the ratio is 1."),

 dict(q="sum from n=1 to infinity of (2n + 1)/(n^2 + 3)", choices=[
   "converges, by limit comparison with sum 1/n^2",
   "diverges, by limit comparison with sum 1/n",
   "converges, since the terms approach 0",
   "diverges, since the terms approach 2"], ans=1,
   why="The ratio to 1/n has limit 2, so the series behaves like the divergent harmonic series."),

 dict(q="sum from n=1 to infinity of 1/(2^n + n)", choices=[
   "diverges, by comparison with sum 1/n",
   "converges, since 1/(2^n + n) < 1/2^n and sum 1/2^n converges",
   "converges, since 1/(2^n + n) < 1/n and sum 1/n converges",
   "diverges, since 2^n + n grows without bound"], ans=1,
   why="Adding n to the denominator only makes the terms smaller than those of a convergent geometric series."),

 dict(q="sum from n=2 to infinity of ln(n)/n^2", choices=[
   "diverges, since ln(n)/n^2 > 1/n^2",
   "converges, since ln(n) <= sqrt(n) gives ln(n)/n^2 <= 1/n^(3/2)",
   "diverges, by limit comparison with sum 1/n",
   "converges, since ln(n)/n^2 < 1/n"], ans=1,
   why="Because ln(n) grows more slowly than sqrt(n), the terms fall below a convergent p-series with p = 3/2."),

 dict(q="sum from n=2 to infinity of 1/(n + ln(n))", choices=[
   "converges, by comparison with sum 1/n^2",
   "converges, since 1/(n + ln(n)) < 1/n",
   "diverges, by limit comparison with sum 1/n",
   "diverges, since the terms do not approach 0"], ans=2,
   why="The ratio to 1/n has limit 1, and being smaller than the harmonic series would prove nothing on its own."),

 dict(q="sum from n=1 to infinity of (sin(n))^2/n^2", choices=[
   "diverges, since sin(n) oscillates",
   "converges, since (sin(n))^2/n^2 <= 1/n^2 and sum 1/n^2 converges",
   "the comparison test does not apply, since sin(n) can be negative",
   "converges, by limit comparison with sum 1/n"], ans=1,
   why="Squaring makes the numerator nonnegative and at most 1, so the terms lie below a convergent p-series."),

 dict(q="Which inequality is a correct basis for showing that sum from n=2 to infinity of 1/(n^2 - 1) converges?", choices=[
   "1/(n^2 - 1) <= 1/n^2 for n >= 2",
   "1/(n^2 - 1) <= 2/n^2 for n >= 2",
   "1/(n^2 - 1) >= 1/n^2 for n >= 2",
   "1/(n^2 - 1) <= 1/n for n >= 2"], ans=1,
   why="Since n^2 - 1 >= n^2/2 for n >= 2, the terms are at most 2/n^2, and the inequality with 1/n^2 alone is false."),

 dict(q="A student argues: 'Since 1/(2n + 1) < 1/n and sum 1/n diverges, sum 1/(2n + 1) diverges.' This argument is", choices=[
   "valid, and the conclusion is correct",
   "invalid, because being smaller than a divergent series proves nothing, although the conclusion happens to be correct",
   "invalid, and the series actually converges",
   "valid, because the terms are positive"], ans=1,
   why="The comparison runs the wrong way; a limit comparison with 1/n (limit 1/2) is what actually establishes divergence."),

 dict(q="To use the limit comparison test on sum from n=1 to infinity of (n^2 + 4)/(2n^5 + n), the most natural choice of b_n is", choices=[
   "1/n",
   "1/n^2",
   "1/n^3",
   "1/n^5"], ans=2,
   why="Keeping only the dominant powers gives n^2/(2n^5) = 1/(2n^3), so b_n = 1/n^3 gives the finite positive limit 1/2."),

 dict(q="sum from n=1 to infinity of 1/n!", choices=[
   "diverges, by comparison with sum 1/n",
   "converges, since 1/n! <= 1/2^(n-1) and sum 1/2^(n-1) converges",
   "converges, since 1/n! <= 1/n^2 for all n >= 1",
   "the comparison test does not apply to factorials"], ans=1,
   why="For n >= 1 we have n! >= 2^(n-1), so the terms lie below a convergent geometric series."),

 dict(q="sum from n=1 to infinity of 2^n/(3^n - 1)", choices=[
   "diverges, since 3^n - 1 < 3^n",
   "converges, by limit comparison with the geometric series sum (2/3)^n",
   "diverges, by limit comparison with sum 1/n",
   "converges to 2"], ans=1,
   why="The ratio to (2/3)^n has limit 1, and the geometric series with r = 2/3 converges."),

 dict(q="sum from n=1 to infinity of (1/n)*sin(1/n)", choices=[
   "diverges, by limit comparison with sum 1/n",
   "converges, by limit comparison with sum 1/n^2",
   "diverges, since sin(1/n) approaches 0",
   "the comparison test does not apply, since sin(1/n) oscillates"], ans=1,
   why="The ratio to 1/n^2 is n*sin(1/n), whose limit is 1, and sum 1/n^2 converges."),

 dict(q="If a_n > 0, b_n > 0, lim as n -> infinity of (a_n/b_n) = 0, and sum b_n converges, then sum a_n", choices=[
   "converges",
   "diverges",
   "may converge or diverge",
   "converges only if b_n is a p-series"], ans=0,
   why="A ratio tending to 0 makes a_n eventually smaller than b_n, so direct comparison with the convergent series applies."),
]
