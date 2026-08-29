# CALC 10.1 Defining Convergent and Divergent Infinite Series — 25 questions
# Answers verified with sympy; see verify_c10_1.py
# Definitional questions (what convergence of a series means, how adding or
# scaling series behaves) carry no sympy check and are marked in the verifier.
TOPIC = ("10.1", "Defining Convergent and Divergent Infinite Series", 10)
QUESTIONS = [
 dict(q="The infinite series sum from n=1 to infinity of a_n converges if and only if", choices=[
   "the terms a_n approach 0",
   "the sequence of partial sums S_n = a_1 + a_2 + ... + a_n approaches a finite limit",
   "the terms a_n are decreasing",
   "the sequence a_n is bounded"], ans=1,
   why="A series is defined to converge exactly when its sequence of partial sums has a finite limit."),

 dict(q="For the series sum from n=1 to infinity of 1/2^n, the third partial sum S_3 equals", choices=[
   "1/8",
   "3/8",
   "7/8",
   "1"], ans=2,
   why="S_3 = 1/2 + 1/4 + 1/8 = 7/8."),

 dict(q="sum from n=1 to infinity of (1/n - 1/(n+1)) equals", choices=[
   "0",
   "1/2",
   "1",
   "the series diverges"], ans=2,
   why="The sum telescopes to S_n = 1 - 1/(n+1), which approaches 1."),

 dict(q="sum from n=1 to infinity of 1/(n(n+1)) equals", choices=[
   "1/2",
   "1",
   "2",
   "the series diverges"], ans=1,
   why="Partial fractions give 1/n - 1/(n+1), so S_n = 1 - 1/(n+1) -> 1."),

 dict(q="sum from n=1 to infinity of (1/(n+1) - 1/(n+2)) equals", choices=[
   "0",
   "1/3",
   "1/2",
   "1"], ans=2,
   why="The telescoping partial sum is S_n = 1/2 - 1/(n+2), which approaches 1/2."),

 dict(q="A series has nth partial sum S_n = 3n/(n+1). The series", choices=[
   "diverges",
   "converges to 1",
   "converges to 3",
   "converges to 0"], ans=2,
   why="The sum of the series is lim as n -> infinity of S_n = 3."),

 dict(q="A series has nth partial sum S_n = (2n^2 + 1)/(n^2 + 3). The sum of the series is", choices=[
   "1/3",
   "2",
   "3",
   "the series diverges"], ans=1,
   why="The sum is the limit of the partial sums, and the ratio of leading coefficients gives 2."),

 dict(q="A series has nth partial sum S_n = n^2/(n+1). The series", choices=[
   "converges to 0",
   "converges to 1",
   "converges to n",
   "diverges"], ans=3,
   why="S_n grows without bound, so the partial sums have no finite limit."),

 dict(q="A series has nth partial sum S_n = 5 - 2/n. The third term a_3 of the series equals", choices=[
   "1/3",
   "2/3",
   "1",
   "13/3"], ans=0,
   why="a_3 = S_3 - S_2 = (5 - 2/3) - (5 - 1) = 1/3."),

 dict(q="Which statement about the sequence a_n = 1/n and the series sum from n=1 to infinity of 1/n is correct?", choices=[
   "Both the sequence and the series converge",
   "The sequence converges to 0 but the series diverges",
   "The sequence diverges but the series converges",
   "Both the sequence and the series diverge"], ans=1,
   why="The terms tend to 0, yet the harmonic series' partial sums grow without bound."),

 dict(q="sum from n=1 to infinity of (1/(2n-1) - 1/(2n+1)) equals", choices=[
   "0",
   "1/2",
   "1",
   "2"], ans=2,
   why="It telescopes to S_n = 1 - 1/(2n+1), which approaches 1."),

 dict(q="sum from n=1 to infinity of (ln(n+1) - ln(n))", choices=[
   "converges to 0",
   "converges to ln(2)",
   "converges to 1",
   "diverges"], ans=3,
   why="The partial sum telescopes to ln(n+1), which increases without bound."),

 dict(q="sum from n=2 to infinity of 1/(n^2 - 1) equals", choices=[
   "1/2",
   "3/4",
   "1",
   "3/2"], ans=1,
   why="Partial fractions give (1/2)(1/(n-1) - 1/(n+1)), and the telescoped limit is (1/2)(1 + 1/2) = 3/4."),

 dict(q="If sum a_n converges to 6 and sum b_n converges to -2, then sum (a_n + b_n)", choices=[
   "converges to 4",
   "converges to 8",
   "converges to -12",
   "may diverge"], ans=0,
   why="Convergent series add termwise, so the sums add: 6 + (-2) = 4."),

 dict(q="If sum a_n converges and sum b_n diverges, then sum (a_n + b_n)", choices=[
   "converges",
   "diverges",
   "converges only if the terms b_n approach 0",
   "may either converge or diverge"], ans=1,
   why="If the combined series converged, subtracting the convergent sum a_n would force sum b_n to converge, a contradiction."),

 dict(q="Deleting the first 10 terms of an infinite series", choices=[
   "can change a convergent series into a divergent one",
   "cannot change whether the series converges, though it may change the sum",
   "cannot change the sum of the series",
   "always makes a divergent series converge"], ans=1,
   why="Convergence is a statement about the tail, so finitely many terms affect only the value of the sum."),

 dict(q="If sum from n=1 to infinity of a_n converges to 7, then sum from n=1 to infinity of 4a_n", choices=[
   "converges to 7",
   "converges to 11",
   "converges to 28",
   "diverges"], ans=2,
   why="A nonzero constant factors out of the partial sums, so the sum is multiplied by 4."),

 dict(q="To say that sum a_n diverges means that", choices=[
   "the terms a_n do not approach 0",
   "the terms a_n are unbounded",
   "the sequence of partial sums does not approach a finite limit",
   "the partial sums approach infinity"], ans=2,
   why="Divergence is failure of the partial sums to have a finite limit, whether they grow, oscillate, or do neither."),

 dict(q="sum from n=0 to infinity of (-1)^n", choices=[
   "converges to 0",
   "converges to 1/2",
   "converges to 1",
   "diverges"], ans=3,
   why="The partial sums oscillate between 1 and 0 and never settle on a single limit."),

 dict(q="If sum from n=1 to infinity of a_n converges to 7, then lim as n -> infinity of a_n equals", choices=[
   "0",
   "1",
   "7",
   "the limit cannot be determined"], ans=0,
   why="Since a_n = S_n - S_(n-1) and both partial sums approach 7, the terms approach 7 - 7 = 0."),

 dict(q="A series has nth partial sum S_n = 4 - 3(1/2)^n. The first term a_1 of the series is", choices=[
   "1/2",
   "3/2",
   "5/2",
   "4"], ans=2,
   why="a_1 = S_1 = 4 - 3(1/2) = 5/2."),

 dict(q="For the series sum from k=1 to infinity of 1/(k(k+1)), a formula for the nth partial sum is", choices=[
   "S_n = 1/(n+1)",
   "S_n = n/(n+1)",
   "S_n = 1 - 1/n",
   "S_n = (n+1)/n"], ans=1,
   why="Telescoping gives S_n = 1 - 1/(n+1) = n/(n+1)."),

 dict(q="sum from n=1 to infinity of (sqrt(n+1) - sqrt(n))", choices=[
   "converges to 0",
   "converges to sqrt(2) - 1",
   "converges to 1",
   "diverges"], ans=3,
   why="The telescoped partial sum sqrt(n+1) - 1 increases without bound even though the terms approach 0."),

 dict(q="sum from n=1 to infinity of 1/(n(n+2)) equals", choices=[
   "1/2",
   "3/4",
   "1",
   "3/2"], ans=1,
   why="Partial fractions give (1/2)(1/n - 1/(n+2)), leaving (1/2)(1 + 1/2) = 3/4."),

 dict(q="sum from n=1 to infinity of (1/n - 1/(n+3)) equals", choices=[
   "1/3",
   "1",
   "11/6",
   "the series diverges"], ans=2,
   why="Three terms survive the telescoping: 1 + 1/2 + 1/3 = 11/6."),
]
