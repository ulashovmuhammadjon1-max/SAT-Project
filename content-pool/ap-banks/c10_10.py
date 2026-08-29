# CALC 10.10 Alternating Series Error Bound — 25 questions
# Answers verified with sympy; see verify_c10_10.py
# The bound is |S - S_n| <= b_(n+1): the absolute value of the FIRST OMITTED
# TERM.  It is available only for a series that satisfies the alternating
# series test, and it is a different tool from the Lagrange bound of 10.12,
# which uses the (n+1)st derivative.  Two items here draw that contrast.
TOPIC = ("10.10", "Alternating Series Error Bound", 10)
QUESTIONS = [
 dict(q="If sum (-1)^(n+1)*b_n satisfies the alternating series test and S_n is the sum of its first n terms, then |S - S_n| is at most", choices=[
   "b_n",
   "b_(n+1)",
   "the sum of all the omitted terms",
   "b_1"], ans=1,
   why="The error is bounded by the absolute value of the first omitted term."),

 dict(q="For sum from n=1 to infinity of (-1)^(n+1)/n, the error in using the sum of the first 4 terms is at most", choices=[
   "1/20",
   "1/6",
   "1/5",
   "1/4"], ans=2,
   why="The first omitted term is the n = 5 term, whose absolute value is 1/5."),

 dict(q="For sum from n=1 to infinity of (-1)^(n+1)/n, the smallest number of terms whose sum is guaranteed by the alternating series error bound to be within 0.01 of S is", choices=[
   "10",
   "50",
   "99",
   "100"], ans=2,
   why="The bound is 1/(n+1), and 1/(n+1) <= 0.01 first holds when n + 1 = 100, that is n = 99."),

 dict(q="For sum from n=1 to infinity of (-1)^n/n^2, the error in using the sum of the first 5 terms is at most", choices=[
   "1/49",
   "1/36",
   "1/25",
   "1/5"], ans=1,
   why="The first omitted term is the n = 6 term, with absolute value 1/36."),

 dict(q="The series sum from n=0 to infinity of (-1)^n/(2n+1) converges to pi/4. Using the sum of its first 4 terms, the error is at most", choices=[
   "1/11",
   "1/9",
   "1/7",
   "1/4"], ans=1,
   why="The first four terms end at n = 3, so the first omitted term is the n = 4 term, 1/9."),

 dict(q="For an alternating series satisfying the alternating series test, the error S - S_n", choices=[
   "is always positive",
   "is always negative",
   "has the same sign as the first omitted term",
   "has the same sign as the last included term"], ans=2,
   why="The tail is itself an alternating series whose sum takes the sign of its first term."),

 dict(q="For an alternating series satisfying the alternating series test, the sum S", choices=[
   "is larger than every partial sum",
   "is smaller than every partial sum",
   "always lies between S_n and S_(n+1)",
   "equals the average of S_n and S_(n+1)"], ans=2,
   why="The partial sums oscillate around S, tightening at each step, so consecutive partial sums bracket the sum."),

 dict(q="For sum from n=1 to infinity of (-1)^(n+1)/n^3, the smallest number of terms guaranteed by the error bound to give an error of at most 0.001 is", choices=[
   "8",
   "9",
   "10",
   "100"], ans=1,
   why="The bound 1/(n+1)^3 <= 0.001 first holds when n + 1 = 10, so n = 9 terms."),

 dict(q="Let S_N = sum from n=0 to N of (-1)^n/n!, which approximates 1/e. The smallest N for which the alternating series error bound guarantees |1/e - S_N| <= 0.001 is", choices=[
   "4",
   "5",
   "6",
   "7"], ans=2,
   why="The bound is 1/(N+1)!, and (N+1)! >= 1000 first holds at N + 1 = 7, since 6! = 720."),

 dict(q="The alternating series error bound may be used only when", choices=[
   "the terms alternate in sign",
   "the terms alternate in sign, decrease in absolute value, and approach 0",
   "the series converges",
   "the series converges absolutely"], ans=1,
   why="The bound comes from the alternating series test, so all of that test's hypotheses are required."),

 dict(q="A student uses the bound |S - S_n| <= b_(n+1) on the series sum from n=1 to infinity of 1/n^2. This is", choices=[
   "valid, since the terms decrease to 0",
   "valid, since the series converges",
   "invalid, since the series is not alternating",
   "valid, but only for n >= 2"], ans=2,
   why="Every hypothesis of the alternating series test must hold, and a series of positive terms does not alternate."),

 dict(q="Which error bound is the absolute value of the first omitted term?", choices=[
   "The alternating series error bound",
   "The Lagrange error bound",
   "The integral test remainder bound",
   "The ratio test bound"], ans=0,
   why="The Lagrange bound instead uses the maximum of the (n+1)st derivative, and the integral bound uses an improper integral."),

 dict(q="For sum from n=1 to infinity of (-1)^(n+1)/n, the error in using the sum of the first 10 terms is at most", choices=[
   "1/100",
   "1/12",
   "1/11",
   "1/10"], ans=2,
   why="The first omitted term is the n = 11 term, of absolute value 1/11."),

 dict(q="An alternating series has b_n = 1/(n*2^n) and satisfies the alternating series test. The error in using the sum of its first 3 terms is at most", choices=[
   "1/80",
   "1/64",
   "1/24",
   "1/16"], ans=1,
   why="The first omitted term is b_4 = 1/(4*2^4) = 1/64."),

 dict(q="An alternating series has b_n = 1/(n^2 + 1) and satisfies the alternating series test. The error in using the sum of its first 5 terms is at most", choices=[
   "1/50",
   "1/37",
   "1/36",
   "1/26"], ans=1,
   why="The first omitted term is b_6 = 1/(36 + 1) = 1/37."),

 dict(q="For a series satisfying the alternating series test with strictly decreasing b_n, the actual error |S - S_n| compared with the bound b_(n+1) is", choices=[
   "exactly equal to it",
   "strictly less than it",
   "greater than it",
   "sometimes greater and sometimes less"], ans=1,
   why="The omitted tail is b_(n+1) minus a positive quantity, so the true error falls strictly below the bound."),

 dict(q="For sum from n=1 to infinity of (-1)^(n+1)/n, the sum of the first 3 terms is 5/6. The alternating series error bound then guarantees that the sum S satisfies", choices=[
   "|S - 5/6| <= 1/3",
   "|S - 5/6| <= 1/4",
   "|S - 5/6| <= 1/5",
   "|S - 5/6| <= 1/6"], ans=1,
   why="The first omitted term is the n = 4 term, of absolute value 1/4, and indeed |ln(2) - 5/6| is about 0.14."),

 dict(q="For sum from n=1 to infinity of (-1)^(n+1)/n, the sum of the first 4 terms is 7/12. Compared with the true sum S, this partial sum is", choices=[
   "an overestimate, since the next term is negative",
   "an underestimate, since the next term is +1/5",
   "exactly equal to S",
   "an overestimate, since the terms are decreasing"], ans=1,
   why="The first omitted term is positive, so S exceeds S_4; the sum is ln(2), about 0.693, and 7/12 is about 0.583."),

 dict(q="An alternating series has b_n = n/2^n and satisfies the alternating series test. The error in using the sum of its first 4 terms is at most", choices=[
   "1/8",
   "5/32",
   "3/16",
   "1/4"], ans=1,
   why="The first omitted term is b_5 = 5/2^5 = 5/32."),

 dict(q="For sum from n=1 to infinity of (-1)^n/sqrt(n), the smallest number of terms guaranteed by the error bound to give an error of at most 0.05 is", choices=[
   "20",
   "200",
   "399",
   "400"], ans=2,
   why="The bound 1/sqrt(n+1) <= 0.05 requires n + 1 >= 400, so n = 399 terms."),

 dict(q="If the terms b_n of an alternating series approach 0 but are not decreasing, then the bound |S - S_n| <= b_(n+1)", choices=[
   "still holds",
   "is not justified, since the hypotheses of the alternating series test fail",
   "holds with b_(n+1) replaced by b_n",
   "holds only for even n"], ans=1,
   why="The bound is a conclusion of the alternating series test and is unavailable when a hypothesis fails."),

 dict(q="For sum from n=1 to infinity of (-1)^(n+1)/2^n, the sum of the first 3 terms is 3/8 and the error bound is", choices=[
   "1/32",
   "1/16",
   "1/8",
   "3/8"], ans=1,
   why="The first omitted term is the n = 4 term, 1/2^4 = 1/16; the true sum is 1/3, and |1/3 - 3/8| = 1/24 is indeed smaller."),

 dict(q="For sum from n=1 to infinity of (-1)^(n+1)/n^2, the smallest number of terms guaranteed by the error bound to give an error of at most 0.005 is", choices=[
   "10",
   "14",
   "15",
   "200"], ans=1,
   why="The bound 1/(n+1)^2 <= 0.005 requires (n+1)^2 >= 200, so n + 1 = 15 and n = 14 terms."),

 dict(q="For which of the following series is the bound |S - S_n| <= b_(n+1) available?", choices=[
   "sum from n=1 to infinity of (-1)^n*n/(n+1)",
   "sum from n=1 to infinity of (-1)^n/(n+1)",
   "sum from n=1 to infinity of 1/(n+1)",
   "sum from n=1 to infinity of (-1)^n*(n+1)/n^(1/2)"], ans=1,
   why="Only 1/(n+1) is an alternating series whose terms decrease to 0; the first and last fail the limit condition and the third does not alternate."),

 dict(q="For sum from n=1 to infinity of (-1)^(n+1)/n, the partial sums are S_4 = 7/12 and S_5 = 47/60. The error bound therefore locates the sum S in the interval", choices=[
   "from 7/12 to 47/60",
   "from 0 to 7/12",
   "from 47/60 to 1",
   "from 7/12 to 1"], ans=0,
   why="Consecutive partial sums of such a series bracket the sum, and ln(2) is about 0.693, between 0.583 and 0.783."),
]
