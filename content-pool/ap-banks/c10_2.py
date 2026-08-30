# CALC 10.2 Working with Geometric Series — 25 questions
# Answers verified with sympy; see verify_c10_2.py
# The recurring trap: the sum is a/(1 - r) where a is the FIRST TERM OF THE
# SERIES AS WRITTEN, not the term at n = 0.  Several items start at n = 2 or
# n = 3 so that a student who reads off the coefficient gets a wrong answer.
TOPIC = ("10.2", "Working with Geometric Series", 10)
QUESTIONS = [
 dict(q="The geometric series sum from n=0 to infinity of a*r^n (with a not 0) converges if and only if", choices=[
   "r > 0",
   "|r| < 1",
   "|r| <= 1",
   "|a| < 1"], ans=1,
   why="A geometric series converges exactly when the common ratio satisfies |r| < 1, and then its sum is a/(1 - r)."),

 dict(q="sum from n=0 to infinity of (1/3)^n equals", choices=[
   "1/2",
   "2/3",
   "3/2",
   "3"], ans=2,
   why="The first term is 1 and r = 1/3, so the sum is 1/(1 - 1/3) = 3/2."),

 dict(q="sum from n=1 to infinity of (1/3)^n equals", choices=[
   "1/3",
   "1/2",
   "2/3",
   "3/2"], ans=1,
   why="The first term written is 1/3, so the sum is (1/3)/(1 - 1/3) = 1/2."),

 dict(q="sum from n=2 to infinity of (1/3)^n equals", choices=[
   "1/9",
   "1/6",
   "1/3",
   "1/2"], ans=1,
   why="The series as written starts at (1/3)^2 = 1/9, so the sum is (1/9)/(1 - 1/3) = 1/6."),

 dict(q="sum from n=0 to infinity of 5(2/5)^n equals", choices=[
   "2",
   "5/3",
   "25/3",
   "10"], ans=2,
   why="With a = 5 and r = 2/5 the sum is 5/(1 - 2/5) = 25/3."),

 dict(q="sum from n=1 to infinity of 3(1/4)^(n-1) equals", choices=[
   "3/4",
   "1",
   "3",
   "4"], ans=3,
   why="The n = 1 term is 3 and the ratio is 1/4, so the sum is 3/(1 - 1/4) = 4."),

 dict(q="sum from n=3 to infinity of (1/2)^n equals", choices=[
   "1/8",
   "1/4",
   "1/2",
   "1"], ans=1,
   why="The first term written is (1/2)^3 = 1/8, so the sum is (1/8)/(1 - 1/2) = 1/4."),

 dict(q="sum from n=0 to infinity of (-1/2)^n equals", choices=[
   "-2",
   "1/2",
   "2/3",
   "2"], ans=2,
   why="With a = 1 and r = -1/2 the sum is 1/(1 + 1/2) = 2/3."),

 dict(q="sum from n=1 to infinity of 2(-1/3)^n equals", choices=[
   "-1/2",
   "-1/3",
   "1/2",
   "3/2"], ans=0,
   why="The first term written is -2/3 and r = -1/3, so the sum is (-2/3)/(1 + 1/3) = -1/2."),

 dict(q="sum from n=0 to infinity of (3/2)^n", choices=[
   "converges to -2",
   "converges to 2/5",
   "converges to 3",
   "diverges"], ans=3,
   why="The ratio 3/2 has absolute value greater than 1, so the terms grow and the series diverges."),

 dict(q="sum from n=0 to infinity of 4^n/5^(n+1) equals", choices=[
   "1/5",
   "4/5",
   "1",
   "5"], ans=2,
   why="Factoring out 1/5 leaves (1/5)*sum (4/5)^n = (1/5)(5) = 1."),

 dict(q="sum from n=1 to infinity of 2^(n+1)/3^n equals", choices=[
   "2/3",
   "2",
   "4",
   "6"], ans=2,
   why="The series is 2*sum from n=1 to infinity of (2/3)^n = 2*((2/3)/(1/3)) = 4."),

 dict(q="Written as a fraction in lowest terms, the repeating decimal 0.777... equals", choices=[
   "7/11",
   "7/10",
   "7/9",
   "7/8"], ans=2,
   why="It is the geometric series with a = 7/10 and r = 1/10, whose sum is (7/10)/(9/10) = 7/9."),

 dict(q="Written as a fraction in lowest terms, the repeating decimal 0.363636... equals", choices=[
   "12/35",
   "9/25",
   "4/11",
   "18/49"], ans=2,
   why="It is the geometric series with a = 36/100 and r = 1/100, giving 36/99 = 4/11 in lowest terms."),

 dict(q="sum from n=0 to infinity of 3(-1)^n", choices=[
   "converges to 0",
   "converges to 3/2",
   "converges to 3",
   "diverges"], ans=3,
   why="Here r = -1, so |r| is not less than 1 and the partial sums oscillate between 3 and 0."),

 dict(q="sum from n=0 to infinity of (-0.2)^n equals", choices=[
   "-5/4",
   "5/6",
   "1",
   "5/4"], ans=1,
   why="With a = 1 and r = -0.2 the sum is 1/(1 + 0.2) = 5/6."),

 dict(q="sum from n=1 to infinity of 2^n/7^(n-1) equals", choices=[
   "2/5",
   "7/5",
   "14/5",
   "7/2"], ans=2,
   why="The n = 1 term is 2 and the ratio is 2/7, so the sum is 2/(1 - 2/7) = 14/5."),

 dict(q="sum from n=2 to infinity of 3(1/2)^n equals", choices=[
   "3/4",
   "3/2",
   "3",
   "6"], ans=1,
   why="The first term written is 3(1/2)^2 = 3/4, so the sum is (3/4)/(1 - 1/2) = 3/2, not 3/(1 - 1/2)."),

 dict(q="If sum from n=0 to infinity of (x/3)^n = 4, then x equals", choices=[
   "3/4",
   "9/4",
   "3",
   "4"], ans=1,
   why="Solving 1/(1 - x/3) = 4 gives x/3 = 3/4, so x = 9/4, which satisfies |x/3| < 1."),

 dict(q="If sum from n=0 to infinity of 2x^n = 5, then x equals", choices=[
   "2/5",
   "3/5",
   "2/3",
   "5/2"], ans=1,
   why="Solving 2/(1 - x) = 5 gives 1 - x = 2/5, so x = 3/5."),

 dict(q="A ball is dropped from a height of 10 feet and on each bounce rebounds to 3/5 of its previous height. The total vertical distance the ball travels before coming to rest is", choices=[
   "15 feet",
   "25 feet",
   "30 feet",
   "40 feet"], ans=3,
   why="The distance is 10 + 2*sum from k=1 to infinity of 10(3/5)^k = 10 + 2(15) = 40 feet."),

 dict(q="sum from n=0 to infinity of (e/3)^n equals", choices=[
   "3/(3 - e)",
   "e/(3 - e)",
   "1/(3 - e)",
   "the series diverges"], ans=0,
   why="Since e/3 is about 0.906 the series converges, and 1/(1 - e/3) = 3/(3 - e)."),

 dict(q="sum from n=1 to infinity of (pi/4)^n equals", choices=[
   "pi/(4 - pi)",
   "4/(4 - pi)",
   "pi/4",
   "the series diverges"], ans=0,
   why="The first term is pi/4 and r = pi/4 < 1, so the sum is (pi/4)/(1 - pi/4) = pi/(4 - pi)."),

 dict(q="sum from n=1 to infinity of 3(-5/4)^n", choices=[
   "converges to -5/3",
   "converges to -3/4",
   "converges to 4/3",
   "diverges"], ans=3,
   why="The ratio has |r| = 5/4 > 1, so the terms do not approach 0 and the series diverges."),

 dict(q="sum from n=1 to infinity of (2^n + 3^n)/6^n equals", choices=[
   "1/2",
   "1",
   "3/2",
   "5/2"], ans=2,
   why="Splitting gives sum (1/3)^n + sum (1/2)^n = 1/2 + 1 = 3/2."),
]
