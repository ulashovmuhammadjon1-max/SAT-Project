# CALC 10.5 Harmonic Series and p-Series — 25 questions
# Answers verified with sympy; see verify_c10_5.py
# The p-series family is the reference every later comparison depends on:
# sum 1/n^p converges if and only if p > 1, and the harmonic series p = 1 is the
# boundary case that diverges.
TOPIC = ("10.5", "Harmonic Series and p-Series", 10)
QUESTIONS = [
 dict(q="The p-series sum from n=1 to infinity of 1/n^p converges if and only if", choices=[
   "p > 0",
   "p >= 1",
   "p > 1",
   "0 < p < 1"], ans=2,
   why="The integral test gives a finite improper integral exactly when p exceeds 1."),

 dict(q="The harmonic series sum from n=1 to infinity of 1/n", choices=[
   "converges to 1",
   "converges, since the terms approach 0",
   "diverges",
   "converges to ln(2)"], ans=2,
   why="It is the p-series with p = 1, the boundary case, and it diverges."),

 dict(q="sum from n=1 to infinity of 1/n^2", choices=[
   "converges, since p = 2 > 1",
   "diverges, since p = 2 > 1",
   "converges, since the terms approach 0",
   "diverges, since it is a harmonic series"], ans=0,
   why="It is a p-series with p = 2, which exceeds 1, so it converges."),

 dict(q="Written as a p-series, sum from n=1 to infinity of 1/sqrt(n) has p = 1/2, and therefore the series", choices=[
   "converges, since p = 1/2",
   "converges, since the terms approach 0",
   "diverges, since p = 1/2 is not greater than 1",
   "diverges, since the terms do not approach 0"], ans=2,
   why="This is the p-series with p = 1/2, and p <= 1 gives divergence."),

 dict(q="sum from n=1 to infinity of 1/n^3", choices=[
   "diverges",
   "converges",
   "converges only if the terms are decreasing",
   "converges to 1/3"], ans=1,
   why="A p-series with p = 3 > 1 converges."),

 dict(q="sum from n=1 to infinity of 1/n^(0.999)", choices=[
   "converges, since 0.999 is nearly 1",
   "converges, since the terms approach 0",
   "diverges, since p = 0.999 is not greater than 1",
   "diverges, since the terms do not approach 0"], ans=2,
   why="Being close to 1 is not enough; the p-series converges only for p strictly greater than 1."),

 dict(q="sum from n=1 to infinity of 1/n^(1.001)", choices=[
   "converges",
   "diverges",
   "diverges, since 1.001 is nearly 1",
   "cannot be determined without more information"], ans=0,
   why="p = 1.001 > 1, so the p-series converges, however slowly."),

 dict(q="sum from n=1 to infinity of 1/n^(1/3)", choices=[
   "converges",
   "diverges",
   "converges to 3/2",
   "converges, since 1/3 < 1"], ans=1,
   why="Here p = 1/3, which is not greater than 1, so the series diverges."),

 dict(q="sum from n=1 to infinity of 5/n", choices=[
   "converges to 5",
   "converges, since the terms approach 0",
   "diverges",
   "converges, since 5 is a constant"], ans=2,
   why="A nonzero constant multiple of a divergent series still diverges."),

 dict(q="sum from n=100 to infinity of 1/n", choices=[
   "converges, since the first 99 terms have been removed",
   "converges to about 0.01",
   "diverges",
   "converges, since the terms are small"], ans=2,
   why="Deleting finitely many terms cannot change divergence; the tail of the harmonic series still diverges."),

 dict(q="sum from n=1 to infinity of (1/n^2 + 1/n)", choices=[
   "converges, since 1/n^2 converges",
   "diverges, since 1/n diverges",
   "converges to pi^2/6",
   "converges, since the terms approach 0"], ans=1,
   why="A convergent series plus a divergent series is divergent."),

 dict(q="sum from n=1 to infinity of 1/n^(4/3)", choices=[
   "converges",
   "diverges",
   "diverges, since 4/3 < 2",
   "converges to 4/3"], ans=0,
   why="p = 4/3 > 1, so the p-series converges."),

 dict(q="sum from n=1 to infinity of 1/(n*sqrt(n))", choices=[
   "diverges, since it contains 1/n",
   "converges, since it is the p-series with p = 3/2",
   "converges, since it is the p-series with p = 1/2",
   "diverges, since sqrt(n) grows slowly"], ans=1,
   why="n*sqrt(n) = n^(3/2), so p = 3/2 > 1 and the series converges."),

 dict(q="sum from n=1 to infinity of n^(-2/3)", choices=[
   "converges, since the exponent is negative",
   "converges, since p = 2/3 < 1",
   "diverges, since p = 2/3 is not greater than 1",
   "diverges, since the terms increase"], ans=2,
   why="The series is the p-series with p = 2/3, and p <= 1 means divergence."),

 dict(q="Which of the following series converges?", choices=[
   "sum from n=1 to infinity of 1/n^(2/3)",
   "sum from n=1 to infinity of 1/n",
   "sum from n=1 to infinity of 1/n^(5/4)",
   "sum from n=1 to infinity of 2/(3n)"], ans=2,
   why="Only 5/4 exceeds 1; the other three are p-series with p <= 1 or multiples of the harmonic series."),

 dict(q="sum from n=1 to infinity of (2/n^3 - 3/n)", choices=[
   "converges",
   "diverges",
   "converges to 2 - 3",
   "converges, since both parts have terms approaching 0"], ans=1,
   why="The first part converges and the second is a multiple of the harmonic series, so the difference diverges."),

 dict(q="For the harmonic series, the nth partial sum H_n satisfies", choices=[
   "H_n approaches a finite limit",
   "H_n - ln(n) approaches a finite constant, while H_n itself increases without bound",
   "H_n - ln(n) increases without bound",
   "H_n is bounded above by 2"], ans=1,
   why="H_n grows like ln(n) plus Euler's constant, so the difference settles down even though H_n does not."),

 dict(q="Which statement about the harmonic series is correct?", choices=[
   "Its terms do not approach 0, which is why it diverges",
   "Its terms approach 0, yet it diverges",
   "Its terms approach 0, so it converges",
   "It converges because it is a p-series"], ans=1,
   why="The harmonic series is the standard warning that terms approaching 0 does not imply convergence."),

 dict(q="sum from n=1 to infinity of sqrt(n)/n^2", choices=[
   "converges, since it is the p-series with p = 3/2",
   "diverges, since it is the p-series with p = 1/2",
   "converges, since it is the p-series with p = 2",
   "diverges, since sqrt(n) increases"], ans=0,
   why="sqrt(n)/n^2 = n^(1/2 - 2) = n^(-3/2), a p-series with p = 3/2 > 1."),

 dict(q="sum from n=1 to infinity of 3/n^(5/2)", choices=[
   "converges",
   "diverges",
   "diverges, since 5/2 > 1",
   "converges to 3"], ans=0,
   why="It is 3 times a p-series with p = 5/2 > 1, so it converges."),

 dict(q="sum from n=1 to infinity of 1/n^(-2)", choices=[
   "converges, since p = -2 < 1",
   "converges to 1/6",
   "diverges, since the series is sum of n^2",
   "diverges, since p = -2 is between -1 and 1"], ans=2,
   why="1/n^(-2) is n^2, whose terms increase without bound, so the series diverges."),

 dict(q="sum from n=1 to infinity of 1/n^0", choices=[
   "converges to 1",
   "converges to 0",
   "diverges, since every term equals 1",
   "diverges, since p = 0 makes the terms undefined"], ans=2,
   why="Each term is 1, so the partial sums are n and the series diverges."),

 dict(q="What is the smallest value of p for which the p-series sum 1/n^p converges?", choices=[
   "p = 1",
   "p = 1.0001",
   "p = 2",
   "There is no smallest such value"], ans=3,
   why="The set of values that work is p > 1, an open condition, so no smallest p exists."),

 dict(q="Of the two series sum 1/n^(2/3) and sum 1/n^(3/2), which converge?", choices=[
   "Both converge",
   "Only sum 1/n^(2/3) converges",
   "Only sum 1/n^(3/2) converges",
   "Neither converges"], ans=2,
   why="Only p = 3/2 exceeds 1; p = 2/3 gives divergence."),

 dict(q="For which values of k does sum from n=1 to infinity of n^k/n^3 converge?", choices=[
   "k < 2",
   "k < 3",
   "k > 2",
   "k > 3"], ans=0,
   why="The general term is n^(k-3) = 1/n^(3-k), which is a convergent p-series exactly when 3 - k > 1, that is k < 2."),
]
